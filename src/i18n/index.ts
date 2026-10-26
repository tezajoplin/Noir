export type Lang = 'id' | 'en';

export const languages: Record<Lang, { label: string; htmlLang: string; ogLocale: string }> = {
	id: { label: 'ID', htmlLang: 'id', ogLocale: 'id_ID' },
	en: { label: 'EN', htmlLang: 'en', ogLocale: 'en_US' },
};

// Indonesian lives at the root, English under /en/.
export function langFromUrl(url: URL): Lang {
	return url.pathname === '/en' || url.pathname.startsWith('/en/') ? 'en' : 'id';
}

// Prefix an internal path ('/about/', '/#built') for the given language.
export function lp(lang: Lang, path: string): string {
	return lang === 'en' ? `/en${path}` : path;
}

// The same page in another language, e.g. '/en/about/' -> '/about/'.
export function pathForLang(pathname: string, lang: Lang): string {
	const bare = pathname === '/en' ? '/' : pathname.replace(/^\/en(?=\/)/, '');
	return lp(lang, bare);
}
