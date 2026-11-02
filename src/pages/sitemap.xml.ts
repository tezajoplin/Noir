import type { APIRoute } from 'astro';
import { languages, pathForLang, type Lang } from '../i18n';

// Every page file except the 404 becomes a sitemap entry, with its ID/EN alternates.
const files = Object.keys(import.meta.glob('./**/*.astro', { eager: false }));

const toPath = (file: string) =>
	file
		.replace(/^\./, '')
		.replace(/\.astro$/, '')
		.replace(/\/index$/, '/')
		.replace(/([^/])$/, '$1/');

const paths = files
	.map(toPath)
	.filter((p) => p !== '/404/' && !p.startsWith('/en/'))
	.sort();

export const GET: APIRoute = ({ site }) => {
	const abs = (path: string) => new URL(path, site).href;
	const codes = Object.keys(languages) as Lang[];

	const entry = (path: string, lang: Lang) => {
		const loc = abs(pathForLang(path, lang));
		const links = codes
			.map((c) => `<xhtml:link rel="alternate" hreflang="${c}" href="${abs(pathForLang(path, c))}"/>`)
			.concat(`<xhtml:link rel="alternate" hreflang="x-default" href="${abs(path)}"/>`)
			.join('');
		return `<url><loc>${loc}</loc>${links}</url>`;
	};

	const body = paths.flatMap((p) => codes.map((c) => entry(p, c))).join('');

	return new Response(
		`<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">${body}</urlset>`,
		{ headers: { 'Content-Type': 'application/xml; charset=utf-8' } },
	);
};
