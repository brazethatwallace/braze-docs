---
name: reference-repos
description: >
  Verifies Braze documentation against sibling SDK, platform, and tooling repos as source of truth.
  Use when verifying product behavior, APIs, SDK behavior, cross-referencing docs with source code,
  documenting limits from code, or when the user mentions @reference-repos or reference repos.
---

# Reference repos for content verification

When verifying documentation (SDK behavior, APIs, product behavior), use the following repos in this workspace as source-of-truth. Prefer searching and citing these over docs alone.

| Folder | Use for |
|--------|--------|
| `braze-android-sdk` | Android SDK |
| `braze-swift-sdk` | iOS / Swift SDK |
| `braze-web-sdk` | Web / JavaScript SDK |
| `braze-react-native-sdk` | React Native SDK |
| `braze-flutter-sdk` | Flutter SDK |
| `braze-unity-sdk` | Unity SDK |
| `braze-unreal-sdk` | Unreal SDK |
| `braze-roku-sdk` | Roku SDK |
| `braze-cordova-sdk` | Cordova SDK |
| `braze-expo-plugin` | Expo plugin |
| `braze-xamarin-sdk` | Xamarin SDK |
| `braze-shopify-app` | Shopify app |
| `liquid` | Liquid templating |
| `grapesjs` | Drag-and-drop editor (GrapesJS) |
| `event-replay` | Event replay |
| `event-modeling-service` | Event modeling |
| `platform` | Main Braze platform (backend/product) |

### Where to search in the platform repo

The platform repo uses a domain-driven architecture — most feature logic lives in `shared_code/domains/` rather than `api/app/models/`. Always search `shared_code/domains/` first or you'll miss most business logic.

| What you're looking for | Where to search |
|------------------------|----------------|
| Feature behavior & business rules | `shared_code/domains/` → `api/app/models/`, `api/lib/` |
| UI labels, tooltips, helper text | `dashboard/app/javascript/src/` |
| Validation rules & error messages | `shared_code/domains/` + `dashboard/app/javascript/src/` |
| Default values & numeric limits | `dashboard/app/javascript/src/lib/shared_constants.json`, then `shared_code/domains/`, `api/config/` |
| Channel-specific logic (push, email, SMS) | `shared_code/domains/channel_*/` |

**Feature naming conventions:** Braze product names map predictably to code names — Canvas → `canvas`, Campaigns → `campaign`, Content Cards → `content_card`, In-App Messages → `in_app_message`, Segments → `segment`.

### Localized UI terms (translations)

Use these paths when you need to reference how Braze translates UI terms (e.g. for docs, glossaries, or consistency):

| Repo | Location | Format | Use for |
|------|----------|--------|--------|
| `braze-swift-sdk` | `Sources/BrazeUICompat/ABKInAppMessage/Resources/<locale>.lproj/AppboyInAppMessageLocalizable.strings` (and `ABKContentCards/Resources/.../AppboyContentCardsLocalizable.strings`) | `.strings` (key = value) | In-app message and Content Cards UI (e.g. Close) on iOS |
| `braze-android-sdk` | `android-sdk-ui/src/main/res/values/strings.xml` (default), `values-<locale>/strings.xml` (e.g. `values-de/strings.xml`) | Android `strings.xml` | Content Cards, in-app, push UI on Android |
| `grapesjs` | `src/i18n/locale/<code>.js` (e.g. `en.js`, `de.js`) | JS objects | Drag-and-drop editor UI (labels, buttons, panel titles) |
| `liquid` | `lib/liquid/locales/en.yml` | YAML | Liquid template error/syntax messages (en only in repo) |
| `braze-shopify-app` | `extensions/braze-app-embed/locales/en.default.json` | JSON | Shopify app embed copy |

To have these folders available in the workspace, open **`braze-workspace.code-workspace`** (File → Open Workspace from File) instead of opening the braze-docs folder alone.

**Layout:** The workspace uses relative paths. It works for anyone as long as braze-docs and all reference repos are **sibling folders** in the same parent (e.g. `~/Documents/braze-docs`, `~/Documents/platform`, …). The parent folder can be anywhere (Documents, `~/code`, etc.).

### PR descriptions and public output

When content has been verified using these Braze source repos, include the relevant repo-relative source file paths in PR descriptions so reviewers can trace the verification (for example, `platform/shared_code/...`). Do not include local filesystem paths such as `/Users/...` or `../platform/...`. All reference repos are private.

For other public-facing output (for example, content that may be pasted externally), don't include private repo paths, internal file names, or other details from these private repos. Instead, summarize the verification at a high level without exposing private source information.

### Keeping repos up to date

Keep your reference repos current when verifying SDK behavior, APIs, or product behavior so documentation checks use the latest code.

**Before using reference repos for verification:** As your first step, run `git pull --ff-only` in each sibling repo you plan to read or search (only the repos the task needs—for example, just `braze-web-sdk` for a Web SDK doc check). Do this before searching or opening files in those repos so conclusions reflect the latest code.

**When you can skip pulling:** You don't need to pull reference repos when the task clearly doesn't depend on them (for example, typos, style-only edits, or docs that don't claim behavior tied to SDK or platform code).

**How to pull:** From the parent folder (the one containing `braze-docs` and the reference repos), run `git pull --ff-only` in each repo you need, or use a loop to update several at once.

If you're unsure whether a repo is current, run a pull before you rely on it for verification.

### Verification rules

- **Don't guess.** If you can't find the behavior in the code, say so. Don't infer or speculate — flag it as unverified.
- **Flag discrepancies.** If the codebase contradicts the docs, say so explicitly: "The docs say X, but the code shows Y." Don't silently reconcile them.
