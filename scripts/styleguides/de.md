# German style guide

## Grammatical gender for "Braze"

Omit articles before "Braze" unless grammar requires one. When an article is needed, use the gender of the head noun in the compound:

- "das Braze SDK" (because "das SDK")

## Section headings vs English IA mirrors

- When a German page sits under the same topic as English (for example ``channels/email/use_cases.md`` alongside ``message_building_by_channel/email/best_practices/use_cases.md``), keep **`##` / `###` slug text** aligned with the English heading and the established German sibling — do not invent a different English loanword for the same section (e.g. **Social** in English must not become **Social Media** in German if the sibling page already uses **Social**; PR #13314).

## Quotation marks

- In prose and table cells, use German double quotation marks: `„` (U+201E) at the opening and `“` (U+201C) at the closing — for example `„überwachen“`, not `„überwachen"`.
- Never pair the low opening quote `„` with a straight ASCII double quote `"` as the closer.
- The same rule applies inside **markdown image alt text** (`![…]({% image_buster … %})`): screen readers read the full alt aloud, so use `„` … `“` there too (for example workspace names shown in a screenshot).

## Register and tone

- Use formal German (Sie) — this is the standard for friendly technical content in German
- The tone should be friendly, conversational, and informative — approachable rather than stiff or academic
- Content should sound conversational, as if explaining something to an acquaintance, while consistently using the formal address (Sie)

## Numbered steps in links (BrazeAI Agents and similar)

- Headings may use forms like `### 3. Schritt: …`, but in **prose link text** write **Schritt 3** (for example `[Schritt 3](#agent-instructions)`), not `3. Schritt`, so the sentence reads naturally in German.

## English martech terminology

Keep established English marketing technology terms in English — do not translate them into German. German martech professionals universally use these English terms, and the German translations sound awkward and unnatural. Key terms to keep in English include:

- **Bounce / Bounces** (not "Absprung" / "Absprünge")
- **Churn** (not "Abwanderung")
- **Conversion / Conversions** (not "Konversion" / "Konversionen")
- **Journey / Journeys** (not "Reise" / "Kundenreise")
- **Canvas / Canvases** (Braze product name, always English)

When forming German compound words with these terms, use a hyphen: Bounce-Rate, Churn-Risiko, Churn-Definition, Conversion Goal.

## Braze „Banners“-Kanal (Navigation)

- In Kurztiteln (`nav_title`, `article_title`) und ähnlichen Navigationsbezeichnungen heißt der Kanal durchgängig **„Banner“** (Singular), nicht das englische Pluralwort **„Banners“**.
- In Fließtext und `description` verwenden Sie natürliche deutsche Plural- und Kasusformen (z. B. **„Bannern“**, **„Banner-Kanal“**, **„Braze-Banner-Kanal“**), keine wörtlichen englischen Mischformen wie *„Braze-Banners-Kanal“* oder *„zum Erstellen von Banners“*.
