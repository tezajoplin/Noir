// @ts-check
import { defineConfig } from 'astro/config';

export default defineConfig({
	site: 'https://noirjersey.com',
	i18n: {
		defaultLocale: 'id',
		locales: ['id', 'en'],
		routing: { prefixDefaultLocale: false },
	},
});
