import type { Lang } from '../../i18n';

// Facts here are owner-confirmed; keep any new answer to the same standard.
const faq: Record<Lang, Array<[string, string]>> = {
	id: [
		['Apa itu NOIR?', 'NOIR adalah brand jersey custom dari Pontianak, berdiri Juli 2022 untuk tim dan komunitas olahraga.'],
		['Di mana toko jersey custom NOIR di Pontianak?', 'Booth NOIR ada di Jalan Paris 1, Gang Perwira No. 16 A, Pontianak. Mampir langsung, atau pesan lewat WhatsApp dari mana saja.'],
		['Berapa harga custom jersey di NOIR?', 'Mulai Rp135K per set. Angka akhirnya tergantung bahan, finishing, dan tambahan. Cara tercepat tahu angkanya: tanya lewat WhatsApp.'],
		['Berapa minimal pesanan?', '10 pcs. Satu jersey itu pakaian, sepuluh itu tim.'],
		['Apakah desain sudah termasuk?', 'Sudah, jadi tidak ada biaya jasa desain terpisah. Desainnya dibuat dari identitas tim Anda, bukan template dengan nama ditempel.'],
		['Berapa lama produksinya?', '3–14 hari, dihitung dari tanggal pemesanan.'],
		['Apakah NOIR menjual jersey ready stock?', 'Tidak. Setiap jersey NOIR dibuat untuk satu tim saja: tim Anda.'],
		['Apakah NOIR menyewakan jersey?', 'Ya, untuk jersey sepak bola. Tarif dan syarat disampaikan lewat WhatsApp.'],
	],
	en: [
		['What is NOIR?', 'NOIR is a custom jersey brand from Pontianak, founded in July 2022 for sports teams and communities.'],
		['Where is NOIR’s custom jersey shop in Pontianak?', 'The NOIR booth is at Jalan Paris 1, Gang Perwira No. 16 A, Pontianak. Drop by, or order over WhatsApp from anywhere.'],
		['How much do custom jerseys cost at NOIR?', 'From IDR 135K per set. The final figure depends on fabric, finish and extras. The fastest way to get it: ask on WhatsApp.'],
		['What is the minimum order?', '10 pcs. One jersey is an outfit. Ten is a team.'],
		['Is the design included?', 'Yes, so there is no separate design fee. The design is built around your team’s identity, not a template with a name stuck on.'],
		['How long does production take?', '3–14 days, counted from the order date.'],
		['Does NOIR sell ready-stock jerseys?', 'No. Every NOIR jersey is made for one team only: yours.'],
		['Does NOIR rent out jerseys?', 'Yes, football jerseys. Rates and terms are shared over WhatsApp.'],
	],
};

export const homeFaq = (lang: Lang) => faq[lang];

export const faqSchema = (lang: Lang) => ({
	'@context': 'https://schema.org',
	'@type': 'FAQPage',
	mainEntity: faq[lang].map(([q, a]) => ({ '@type': 'Question', name: q, acceptedAnswer: { '@type': 'Answer', text: a } })),
});
