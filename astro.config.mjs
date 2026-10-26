// @ts-check
import { defineConfig } from 'astro/config';

export default defineConfig({
	// Current Vercel production domain; replace when a custom domain is connected.
	site: 'https://noir-plum-omega.vercel.app',
	i18n: {
		defaultLocale: 'id',
		locales: ['id', 'en'],
		routing: { prefixDefaultLocale: false },
	},
});
