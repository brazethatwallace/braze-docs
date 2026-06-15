# Portuguese (Brazil) style guide

## Quotation marks in image alt text

- Do **not** paste the German low-9 double quote **„** (U+201E) into Brazilian Portuguese — models sometimes do this when paraphrasing quoted UI or email screenshots. Use consistent **ASCII `"…"`** pairs or Brazilian **“…”** for nested quotations inside ``![alt](...)`` (auto-translate PR #13314).

## BrazeAI generative images (`brazeai/generative_ai/images.md`)

- Translate numbered-step bold labels (**AI Image Generator**, **Generate Images**) and Font Awesome `title="..."` tooltips into Portuguese when the rest of the page is pt-BR — do not leave US-English UI scraps in the middle of localized instructions (PR #13313).

## Grammatical gender for "Braze"

"Braze" is **feminine** in Portuguese (the implied noun is "a empresa/plataforma"). Always use feminine articles and contractions:

- **Correct**: a Braze, da Braze, na Braze, para a Braze
- **Incorrect**: o Braze, do Braze, no Braze, para o Braze

## Capitalization

- Inside a sentence, use sentence case for common phrases — do not use English headline capitalization (for example *tomada de decisões*, not *Tomada de decisões*, when it is not a heading or proper name)

## Register and tone

- Use informal Portuguese (você) — this is the standard for friendly technical content in Brazilian Portuguese
- The tone should be informal, friendly, and informative — approachable rather than stiff or academic
- Content should sound conversational, as if explaining something to an acquaintance

## BrazeAI — Otimizador de Conteúdo (Content Optimizer)

- On **Content Optimizer** docs (`brazeai/content_optimizer.md` and related Canvas step pages), use **Otimizador de Conteúdo** consistently in running text, alerts, and link anchors. Do not mix English **Content Optimizer** with Portuguese titles or navigation labels.

## Analytics and reporting vocabulary

- Prefer **desempenho** (and related forms like *desempenho da mensagem*, *desempenho histórico*) for “message performance” / “historical performance” in reporting and analytics prose. Avoid the English loanword **performance** in those contexts unless it is a fixed product string.
- When English shows the Braze dashboard’s top-level **Analytics** section in bold navigation paths (for example `**Analytics** > **Report Builder (New)**`) or as “the **Analytics** page”, keep **`Analytics`** in Brazilian Portuguese for that product chrome—do **not** swap in `**Análise de dados**` for those UI slots. Generic prose about *análise de dados* (data analysis) is still fine in lowercase or unbolded running text (auto-translate PR #13386).

## Clarity over literal accuracy

- When the English source uses abstract or indirect phrasing, rephrase for clarity in Portuguese rather than translating word-for-word
- Definitions and explanations should be immediately understandable to a Portuguese-speaking reader — if a literal translation sounds confusing or unnatural, rewrite the sentence to convey the same meaning more directly
- For example, prefer "o intervalo de inatividade para ser considerado um cliente perdido" over a literal rendering like "o intervalo em que a atividade de um usuário atende aos critérios de churn"

## Sentence structure

- Break long, complex sentences into shorter ones — Portuguese reads better with shorter, direct sentences
- Avoid overly literal phrase-by-phrase translations that produce unnaturally long sentences in Portuguese; split at logical points and start new sentences with connectors like "Então", "Portanto", "Nesse caso"
- Prefer natural Portuguese expressions over literal translations of English idioms: use "em retrospecto" instead of "olhando para trás" (for "looking back"), for example
