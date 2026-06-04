# Braze Docs — Bugbot review rules

For pull requests that change localized documentation under `_lang/`, follow the translation rules in [scripts/translation_prompt.md](../scripts/translation_prompt.md).

## Localized dashboard navigation paths are correct

**Do not flag** bold dashboard breadcrumb paths in `_lang/` files when they are translated from English into the target language.

Examples that are **valid** in Spanish (`es`):

- `**Configuración** > **Configuración de administrador** > **Configuración de seguridad**`
- `**Configuración** > **Configuración de administrador** > **Configuración de seguridad** > **Descarga de evento de seguridad**`

These match the Braze dashboard UI for that locale. The English source uses US-dashboard labels such as **Settings** > **Admin Settings** > **Security Settings** > **Security Event Download**; localized docs should mirror what users see when the dashboard is set to that language.

## Localized `aria-label` values are correct

**Do not flag** translated `aria-label` values on tables, Kramdown IAL lines, or inline icons in `_lang/` files.

Examples that are **valid** in Spanish (`es`):

- `{: .reset-td-br-1 aria-label="Casos de uso" }` (English source: `"Use cases"`)
- `<table aria-label="Encabezados de correo electrónico">` (English source: `"Email headers"`)
- `<i class="fas fa-gear" aria-label="Configuración">` (English source: `"Settings"`)

Table-accessibility CI adds `aria-label` to tables in English source files. Localized mirrors should translate those labels for screen readers in the target language—same as table headings and other descriptive UI copy.

## What must stay in English in `_lang/` files

Only flag missing English when the string is one of these categories:

- **Code blocks and inline code** — wire tokens, JSON keys, API field names, shell commands
- **YAML front matter keys** — `nav_title`, `layout`, `permalink`, etc. (keys only; values may be translated per the prompt)
- **Filter / taxonomy tokens** — `{% apitags %}` comma-separated tokens, `search_tag`, glossary filter `name`/`tags` for non-Latin locales
- **Permission names in quotes** — literal dashboard permission strings such as `"View WhatsApp Message Templates"` where the prompt requires verbatim English
- **Braze product names** — Canvas, Campaign, Currents, Content Cards, Liquid, etc., per the glossary
- **Locale-specific exceptions** documented in `translation_prompt.md` (for example pt-BR **Analytics** in nav paths, Korean SMS keyword breadcrumbs)

## Mixed-language procedure lists

Flag **inconsistent** lists where some bold UI controls in the same numbered step are English and others are localized (for example **Zeilen** beside **Done**). Do **not** flag a list where **all** breadcrumb labels in that step are consistently localized to the target language.

## Auto-translation PRs

PRs labeled `auto-translation` from branch `auto-translate/*` are machine-translated. Prefer dismissing false positives over reverting correct localized UI paths or `aria-label` values to English.
