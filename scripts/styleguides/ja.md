# Japanese style guide

## Latin product names next to Japanese particles

- When Braze docs keep an English product or SDK token (**Segment**, **Canvas**, **Campaign**, **SDK**, **Content Cards**, **In-App Messages**, **REST API**, etc.) and the next morpheme is a hiragana particle (**を**, **の**, **は**, **と**, **が**, **も**), write the particle **flush** against the Latin word — **no ASCII space** in between (e.g. **Segmentを**, **Canvasの**, **SDKの**). A space before the particle reads like sloppy mixed typography and was flagged on localized feature-flag docs (PR #13316).

## Email campaigns in prose

- For the *idea* of email campaigns in Japanese sentences, prefer **メールキャンペーン** or **Eメールキャンペーン** — avoid half-mixed **メール Campaign** when you mean the localized concept (PR #13314). Keep bare **Campaign** / **Campaigns** when echoing English UI labels.

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
