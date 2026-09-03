# Japanese style guide

## Product names in Japanese prose

- In reader-facing Japanese sentences, use glossary Japanese product names — **キャンペーン**, **キャンバス**, **セグメント** — not English **Campaign**, **Canvas**, or **Segment** (JA partner review, 2026-06).
- When the next morpheme is a hiragana particle (**を**, **の**, **は**, **と**, **が**, **も**), write the particle **flush** against the product name — **no ASCII space** (e.g. **キャンペーンを**, **キャンバスの**, **セグメントを**). Same rule applies to Latin tokens we keep in English (**SDK**, **Content Cards**, **In-App Messages**, **REST API**, etc.): **SDKの**, not **SDK の**.
- Multi-word dashboard labels follow `ja.json` (e.g. **Create Campaign** → **キャンペーンを作成**, **Campaign Details** → **キャンペーンの詳細**).

## Email campaigns in prose

- For the *idea* of email campaigns, prefer **メールキャンペーン** or **Eメールキャンペーン** — never **メール Campaign** (PR #13314).

## BrazeAI generative brand guidelines (YAML)

- For `brazeai/generative_ai/brand_guidelines.md`, keep **`nav_title` / `article_title`** aligned with the administrative **ブランド・ガイドライン** hub: use the **・** form in those keys so left-nav matches sibling pages (PR #13313).

## Register and tone

- Always use です/ます form (polite style) for all sentences — never use plain/dictionary form (だ/である endings)
- This applies consistently throughout the entire document — do not mix polite and plain styles
- For example, use 「記録します」(kiroku-shimasu) instead of 「記録する」(kiroku-suru)
- The tone should be friendly and informative while maintaining です/ます form throughout

## Inclusivity

- Follow traditional Japanese grammar, but phrase translations to avoid gendered language as much as possible
- Use gender-neutral nouns for job titles and professions (e.g., use 看護師 instead of 看護婦)

## Untranslated references

- For documents, research studies, or publications that do not have an official Japanese translation, leave the title in English
