import type { Lang } from '../../i18n';

// Facts here are owner-confirmed; keep any new answer to the same standard.
const faq: Record<Lang, Array<[string, string]>> = {
	id: [
		['Apa itu NOIR?', 'NOIR adalah brand jersey custom dari Pontianak, berdiri Juli 2022 untuk tim dan komunitas olahraga.'],
		['Di mana toko jersey custom NOIR di Pontianak?', 'Booth NOIR ada di Jalan Paris 1, Gang Perwira No. 16 A, Pontianak. Datang aja langsung, atau bisa juga WhatsApp.'],
		['Berapa harga custom jersey di NOIR?', 'Mulai Rp135K per set. Angka akhirnya tergantung bahan, finishing, dan tambahan. Untuk detail, bisa langsung tanyakan melalui WhatsApp.'],
		['Berapa minimal pesanan?', 'Minimal 10 pcs. Kalau kamu ada request tersendiri, bisa tanya-tanya aja dulu.'],
		['Apakah desain sudah termasuk?', 'Sudah, jadi tidak ada biaya jasa desain terpisah. Desainnya dibuat dari keinginan dan identitas tim kamu. We support you.'],
		['Berapa lama produksinya?', '3–14 hari, dihitung dari tanggal pemesanan.'],
		['Apakah NOIR menjual jersey ready stock?', 'Tidak. Sesuai dengan pedoman kami, we help you to create your team’s identity.'],
		['Apakah NOIR menyewakan jersey?', 'Ya, untuk jersey sepak bola. Tarif dan syarat disampaikan lewat WhatsApp.'],
	],
	en: [
		['What is NOIR?', 'NOIR is a custom jersey brand from Pontianak, founded in July 2022 for sports teams and communities.'],
		['Where is NOIR’s custom jersey shop in Pontianak?', 'The NOIR booth is at Jalan Paris 1, Gang Perwira No. 16 A, Pontianak. Just drop by, or message us on WhatsApp.'],
		['How much do custom jerseys cost at NOIR?', 'From IDR 135K per set. The final figure depends on fabric, finish and extras. For details, just ask on WhatsApp.'],
		['What is the minimum order?', 'Minimum 10 pcs. If you have a special request, feel free to ask first.'],
		['Is the design included?', 'Yes, so there is no separate design fee. The design is built from your wishes and your team’s identity. We support you.'],
		['How long does production take?', '3–14 days, counted from the order date.'],
		['Does NOIR sell ready-stock jerseys?', 'No. In line with our principles, we help you create your team’s identity.'],
		['Does NOIR rent out jerseys?', 'Yes, football jerseys. Rates and terms are shared over WhatsApp.'],
	],
};

export const homeFaq = (lang: Lang) => faq[lang];

export const faqSchema = (lang: Lang) => ({
	'@context': 'https://schema.org',
	'@type': 'FAQPage',
	mainEntity: faq[lang].map(([q, a]) => ({ '@type': 'Question', name: q, acceptedAnswer: { '@type': 'Answer', text: a } })),
});
