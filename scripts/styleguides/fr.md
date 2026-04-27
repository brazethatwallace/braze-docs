# French style guide

## Apostrophes (elision)

- In elided words (**d’utilisation**, **l’e-mail**, **l’application**, **n’**, **j’**, **qu’**, etc.), use the typographic apostrophe **’** (U+2019), not the ASCII apostrophe **'** (U+0027), so copy matches other `fr_fr` pages and passes typography review (PR #13314).

## BrazeAI generative docs (`brazeai/generative_ai/`)

- On **`images.md`**, translate bold step labels and HTML `title` tooltips into French; use complete phrases (**Ajouter une image à la bibliothèque multimédia**, not *Ajouter image à…*). On **`brand_guidelines.md`**, keep `nav_title` / `article_title` wording consistent when the page centers on *directives de marque* (PR #13313).

## Grammatical gender for "Braze"

Avoid gendered articles directly before "Braze" when possible (prefer "de Braze", "avec Braze"). When an article is required in a compound name, match the gender of the head noun:

- "la Braze Intelligence Suite" (because "la suite")
- "le Braze SDK" (because "le SDK")

## Capitalization

- Use normal French sentence capitalization; do not import English title case into the middle of a sentence (for example *une décision automatisée*, not *une Décision automatisée*, unless it starts a sentence or is a proper name)

## Brand phrases

- "Be Absolutely Engaging" must always be translated as **"L'Engagement, réinventé"** — ensure it fits naturally in the surrounding sentence context

## Register and tone

- Use formal address in French (pronoun "vous"), not "tu" — this is the standard for friendly technical content in French
- Use a friendly, conversational, and informative tone — approachable rather than stiff or academic
- Content should sound conversational, as if explaining something to a professional acquaintance
- **Avoid robotic or overly literal phrasing.** The translation must read as natural, fluent French — not as a word-for-word rendering of English. Rephrase sentences freely to match how a French technical writer would express the same idea
- Vary sentence structure and vocabulary; avoid repetitive patterns that make the text feel machine-generated
- Prefer concise, direct sentences over long, complex constructions

## API and HTTP vocabulary

- For request/webhook **body** terminology, use **payload** / **payloads** (lowercase, plural *payloads* when needed) or a natural French equivalent such as *corps de requête*. Avoid all-caps **PAYLOAD** in running text and headings—it mirrors English shouting and looks out of place in French documentation.

## Job titles and roles

- Keep established English job titles in English when they are commonly used as-is in French professional contexts (e.g., "Account Manager", "Customer Success Manager")
- If a French equivalent is well-established and widely used in the industry, you may use it — but never invent awkward literal translations

## Analytics and reporting tables

- In “Available metrics” / “Indicateurs disponibles” tables, **translate the metric row labels** — do not leave them in English. Follow the same pattern as the DE/ES/JA/KO/PT-BR translations of the eCommerce revenue dashboard:
  - `eCommerce Revenue` → **Chiffre d’affaires eCommerce**
  - `Daily Orders Placed` → **Commandes quotidiennes passées**
  - `Average Daily eCommerce Revenue` → **Chiffre d’affaires eCommerce quotidien moyen**
  - `eCommerce Revenue Over Time` → **Chiffre d’affaires eCommerce au fil du temps**
  - `eCommerce Revenue by Campaign / by Canvas` → **Chiffre d’affaires eCommerce par campagne / par Canvas**
  - `Total Revenue` → **Chiffre d’affaires total**
  - `Total Orders` → **Total des commandes**
- Keep only the actual Braze dashboard **product UI name** in English when that is how French users see it in-product (e.g. `eCommerce Revenue - Last Touch Attribution`). Normal descriptor metric names belong in French.
