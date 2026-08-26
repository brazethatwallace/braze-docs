# Writing Style Reference

Condensed reference for the braze-docs AI skill. Distilled from
`docs/contributing/style_guide/writing_style_guide.md`, which is the canonical
source of truth. If this file and the in-repo guide conflict, follow the in-repo
guide and update this file to match.

## Voice and tone

The Braze voice is **straightforward**, **empowering**, and **human**.

- Explain complicated things simply. Be concise.
- Explain the "why" and "how" to give users confidence to take action.
- Aim for a conversational tone, not a formal one.
- Cut jargon and acronyms. If unavoidable, define them on first use.
- Write for a global audience. Avoid slang, idioms, and culturally specific humor.

## Core writing rules

### Active voice

Use active voice. Avoid passive voice unless de-emphasizing a subject (to avoid
blaming the reader) or when who performed the action is unimportant.

- Do: "Braze connects consumers to the brands they love."
- Don't: "Consumers are connected to the brands they love."

### Second person

Address the reader as "you". Avoid first person ("we", "our") except when
referring to Braze as an organization. Use the imperative for direct instructions.

- Do: "Upload the CSV file."
- Don't: "You can upload the CSV file." / "We can upload the CSV file."

### Present tense

Use present tense instead of **future** tense. Present tense conveys immediacy and
demonstrates confidence. Avoid using "will" or hypothetical "would", especially when
referring to the result of user action.

- Do: "Archived subscription groups cannot be edited and no longer appear in segment filters."
- Don't: "Archived subscription groups cannot be edited and will no longer appear in segment filters."

Only use future tense when you are actually talking about the future.

**Exceptions (do not rewrite to present tense for "consistency"):**
- Troubleshooting, FAQs, and incident write-ups describing **events that already happened**
  (for example "The message was aborted", "The email went to the spam folder").
- Markdown table **Possible cause** rows that name a past delivery outcome.
- Epistemic hedging: "may", "may have", "might" when describing uncertain provider or user behavior
  (for example "The mailbox provider may route the message to spam").

### Contractions

Use standard contractions (you're, can't, don't) for an approachable tone. Do
not use noun+verb contractions (Braze'll) or double contractions (mightn't've).

### Avoid condescending language

Never use "simple", "simply", "just", "easy", or "it's easy" when describing
steps or instructions.

### Avoid antithesis constructions

Do not use "not X, but Y" or "it isn't this, it's that" at the sentence level.
State the positive directly. This ban is separate from contrast.

Contrast is fine when it lives in the framing, not in a clever clause. Anchor
the current state against what it replaced (hidden → tracked, manual → systemic,
ad hoc → shared standard). Let the before/after carry the value in how you frame
the point, not in an antithesis sentence.

- Don't: "This isn't a deprecation; it's a migration."
- Do: "These capabilities now live in Operator. The entry point changed; the functionality did not."
- Don't: "Operator doesn't just generate copy — it understands your workspace."
- Do: "Operator generates copy using your workspace context — brand guidelines, attributes, and the page you're working on."

### Oxford comma

Always use the Oxford (serial) comma before the last conjunction in a series.

- Do: "campaigns, Canvases, and segments"
- Don't: "campaigns, Canvases and segments"

### Abbreviations

Spell out uncommon abbreviations on first mention, followed by the abbreviation
in parentheses. Use the abbreviation for subsequent mentions. Do not spell out
common abbreviations (PDF, USB, API, SDK).

- Pluralize without an apostrophe: APIs, SDKs
- Use "a" or "an" based on pronunciation: "an ISP", "a CSV file"

## Inclusive language

- Use gender-neutral pronouns ("they/them/theirs" is always acceptable as singular).
- Use gender-neutral job titles (salesperson, not salesman).
- Avoid ableist language (do not use "crazy", "insane", "blind to", "cripple", "dumb").
- Do not refer to age, disability, race, religion, or ethnicity unless specifically relevant.
- Use "customers" for brands Braze works with. Never say "clients".
- Use "consumers" for customers' customers. Reserve "users" for user-metric contexts.

## Formatting conventions

### Headings and titles

- Use sentence case capitalization for all headings and titles.
- Use gerunds (-ing words) for article titles when applicable.
- Use imperative verbs for task-based headings.
- Do not skip heading levels (h3 follows h2, etc.).
- Use an h1 for page titles only.

### UI interaction verbs

Use these specific verbs when describing interactions with the Braze dashboard:

| Verb | Usage | Example |
|---|---|---|
| Open | Apps, files, folders | Open the `braze.xml` file. |
| Close | Apps, files, folders | Close the `braze.xml` file. |
| Go to | Pages, tabs, sections, webpages | Go to the **Segments** page. |
| > | Sequential steps of the same type | Go to **Segments** > **Segment Insights**. |
| Choose | Subjective, strategic, or open-ended decisions | Choose a campaign strategy. |
| Select | Checkboxes, dropdowns, tabs, simple decisions | Select **Show Password**. |
| Clear | Deselecting a checkbox | Clear the **Show Password** checkbox. |
| Click | Clicking a UI element | Click **Save**. |
| Turn on | Enabling a toggle | Turn on the **List-Unsubscribe header**. |
| Turn off | Disabling a toggle | Turn off **Inline CSS on New Emails by Default**. |
| Enter | Typing a value into a field | In the text field, enter the name of your custom attribute. |

### UI elements in instructions

| Element | Formatting | Example |
|---------|-----------|---------|
| Buttons | **Bold** the label. Do not say "the X button". | Click **Add Languages**. |
| Checkboxes | **Bold** the label. Use "select/clear", not "check/uncheck". | Select **Send in local time zone**. |
| Pages | **Bold** the page name. Use "the X page". | Go to the **Segments** page. |
| Tabs | **Bold** the tab name. | Select the **Settings** tab. |
| Filters/operators | `Code text`. Match UI case. | Select the `First Used App` filter. |
| Filenames/paths | `Code text`. | Open the `braze.xml` file. |
| Error messages | "Quotation marks". | "Push Bounced: MismatchSenderId" |
| Metrics (in text) | *Italics* with initial caps. | The *Machine Opens* metric shows... |
| Permissions | "Quotation marks". | Grant the "Manage Segments" permission. |

### Bold text — UI labels only

**Bold** dashboard UI labels the reader interacts with (buttons, pages, tabs, checkboxes, toggles, menu items). Do **not** bold words for emphasis, importance, or scanning.

| Do | Don't |
|---|---|
| Click **Save**. | Click **Save** to **finalize** your changes. |
| Go to the **Campaigns** page. | Create a **campaign** that targets… |
| Turn on **Intelligent Timing**. | This is **important** for delivery. |

If a sentence has no UI label, leave it in plain text. Prefer rewriting for clarity over adding bold.

### Code samples

- Indent with two spaces per level.
- Specify the language for syntax highlighting (e.g., `json`, `javascript`, `swift`, `bash`, `python`, `liquid`).
- Introduce with an expository sentence where possible.
- Use straight quotation marks, not curly quotes.

### Code in text

Use backtick code font for: attribute names/values, API parameters, filenames,
file paths, method/variable/parameter names, HTML/XML elements, HTTP status
codes, terminal input.

### Placeholder text

**In API code blocks** — enclose in curly brackets, uppercase with underscores:

```json
{
  "api_key": "{YOUR_API_KEY}",
  "external_id": "{YOUR_EXTERNAL_ID}"
}
```

**In Liquid code blocks** — uppercase with underscores (no curly brackets beyond Liquid syntax):

```liquid
{%- connected_content YOUR-API-URL :save items -%}
```

**Inline** — use italicized code: *`YOUR_API_KEY`*

Guidelines:
- Use as many words as needed for clarity: *`CAMPAIGN_NAME`* not *`NAME`*.
- Call out placeholders immediately after the code block.
- For two or more placeholders, list each in order of appearance.

### Lists

- Bulleted lists: unordered information.
- Numbered lists: sequential steps.
- Lettered lists: mutually exclusive options.
- Start each item with a capital letter.
- Omit ending punctuation for single words, fragments without verbs, code items, or link/title items.
- Use parallel syntax across all items.

### Numbers

- Spell out numerals one through nine. Use numerals for 10+.
- Use commas for numbers over three digits (1,000).
- Never start a sentence with a numeral (except years).
- Percentages: use numeral + % with no space (10%). Spell out if starting a sentence.

### Units of measurement and `&nbsp;`

In Markdown and HTML, use a non-breaking space (`&nbsp;`) between a number and its
unit so they do not wrap onto separate lines. This applies to most units: distance,
pixels, points, weight, storage (KB, MB, GB), and degrees of temperature (between
the degree symbol and C/F).

- Do: `512&nbsp;MB`, `2&nbsp;KB`, `240 x 240&nbsp;px`, `1&nbsp;MB`
- Do not use a regular space: `512 MB` (may wrap badly in HTML output)
- Do not use `&nbsp;` for currency, percent, or degrees of angle: `10%`, `$50`, `90°`
- For ranges, repeat the unit for each number: `5&nbsp;MB to 10&nbsp;MB`
- In UI steps, `</i>&nbsp;**Button label**` between an icon and bold UI text is acceptable
- In schema tables, `` `type,`&nbsp;`other` `` between type tokens is acceptable

Do not suggest removing `&nbsp;` when it separates a number from a measurement unit
or appears in the icon/UI or schema-table patterns above.

### Links

- Use descriptive link text. Never use "Learn more", "here", "click here", or "this document".
- Use "For more information, see [Topic Name]" or "For more information about X, see [Topic Name]".
- Match link text to the destination's title or heading.
- Do not place two links back to back without separating text.

### Alerts

Four types: Important, Note, Tip, Warning. Use sparingly.

- **Important:** Essential info (deprecated features, billing impacts, beta status).
- **Note:** One-off caveats or helpful callouts.
- **Tip:** Supplementary knowledge, shortcuts, additional resources.
- **Warning:** Irreversible consequences, feature-breaking behavior, data loss.

Do not use alerts for essential article structure (intros, setup steps). Avoid
stacking two or more alerts in a row. Keep alert content short and concise.

### Tables

- Default to plain text for status/comparison cells ("Supported", "Not supported"). Add an emoji alongside the text only when it adds real scanning value (for example, a wide support matrix).
- Always mark decorative status emoji `aria-hidden="true"` — never rely on a screen reader announcing the raw emoji name.
- Icon-only cells (dropping visible text) are acceptable only in wide tables (4+ columns) with tight space, and only when all three hold: `aria-hidden="true"` on the emoji, a `.sr-only` span per cell with the full text, and a visible legend near the table defining each symbol.

Example pattern:

```html
<td><span aria-hidden="true">✅</span><span class="sr-only">Supported</span></td>
```

## Procedures and instructions

- Do not jump straight into steps. Provide context and list prerequisites first.
- Structure around what the user can do, not what the product can do.
  - Do: "Use this feature to send targeted messages."
  - Don't: "This feature sends targeted messages."
- Provide location steps: "On the **Settings** page, click **Edit**."
- Put conditional clauses first: "If you need X, do A then B."
- Use "When you've" or "After you've" to reinforce task order. Avoid "Once you've" (does not translate well).

## Accessibility

- Use plain language. Aim for no more than 20 words per sentence, five sentences per paragraph.
- Front-load sections with the most important information (inverted pyramid).
- Provide alt text for every image.
- Do not use images as the only way to show information.
- Do not use ampersands (&) in place of "and" unless matching UI text.
- Avoid Latin phrases; use simple alternatives.

## Punctuation quick reference

- **Colons:** Introductory sentence must stand alone as a complete sentence before the colon. Bold the colon if preceding text is bold.
- **Semicolons:** Use to separate closely related independent clauses. Use sparingly.
- **Apostrophes:** Singular nouns ending in S take 's (Chris's). Plural nouns ending in S take only ' (users').
- **Ampersands:** Do not use & for "and" in text or headings unless matching UI.

## Describing limitations

Write candidly about product limitations. Do not distort or minimize. Frame
limitations with appropriate, positive context without promising future features.

## YAML metadata (`date_published`)

When you add a new public article in `user_guide`, `developer_guide`, `api`, `partners`, or `help`, include `date_published` as a quoted `YYYY-MM-DD` value. Use today's UTC date, or the UTC date you expect this PR to merge. The value must not be in the past. Confirm it is still accurate before merge. Do not change it after the article is public.

If the page is `hidden: true` or `config_only: true` at first, add `date_published` when you make it public, unless a date is already present—then keep that date. Do not add a date within the last 14 days (or a future date) to an already-public article that lacks the field.

## Reviews

When reviewing content, verify compliance with all rules above. Flag and correct
violations. For detailed guidance on any topic, consult the relevant source file
listed in the style guide source files table in SKILL.md.

For terminology decisions (banned words, caution words, capitalization of product
names), load [glossary.md](glossary.md).
