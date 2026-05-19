# Message engagement glossary tag fixes

Plan to resolve filter tag gaps on the [Message engagement events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) glossary page. Excludes Email Soft Bounce (requires a new product tag). Operator page-size work and `_lang/` mirror updates are out of scope.

## Problem

Checkbox filters use **AND** logic (`matchAllTags`): an event must include every selected tag. Several events share identical `{% apitags %}` or omit a secondary tag, so filters return multiple unrelated events.

## A. JavaScript (`_layouts/message_engagement_events_glossary.html`)

| Change | Rationale |
|--------|-----------|
| Add `parseTagsQueryParam()` | Strip empty tokens from `?tags=` so `''` does not break `matchAllTags` (`indexOf('')` matches all items). |
| Use parsed array for URL pre-check | Each checkbox is checked if its value appears in the URL list (OR for deep links only). |
| Run `search_apis()` only when parsed list is non-empty | Avoid unnecessary filter pass on every page load. |
| Keep `matchAllTags` for checkbox filtering | Multi-tag selection uses AND. |

## B. `{% apitags %}` updates (`message_engagement_events.md`)

| Event | Tags |
|-------|------|
| Agent executed events | `Agent` (unchanged) |
| Tool invocation events | `Agent, Tool` |
| Global Subscription State Change events | `Subscription, Global` |
| Subscription Group State Change events | `Subscription, Subscription Group` |
| Exit Match Audience events | `Exit, Canvas, Match Audience` |
| Exit Perform Event events | `Exit, Canvas, Perform Event` |
| Experiment Step Conversion events | `Canvas, Conversion` |
| Experiment Split Entry events | `Canvas, Entry` |
| Push Notification iOS Foreground Open events | `Push, iOS, Opens` |
| SMS Carrier Send events | `SMS, Sends, Carrier` |
| SMS Delivery Failure events | `SMS, Delivery, Failure` |
| SMS Send events | `SMS, Sends` (unchanged) |

**Excluded:** Email Soft Bounce and Email Bounce both remain `Email, Bounce` until product adds a distinct tag.

## C. i18n (`_data/i18n.yml`)

Add keys under `currents_message_engagement_tag_labels` for **en**, **ja**, and **ko**:

| Key | en |
|-----|-----|
| `carrier` | Carrier |
| `global` | Global |
| `tool` | Tool |
| `match audience` | Match Audience |
| `perform event` | Perform Event |
| `subscription group` | Subscription Group |

Existing keys reused: `conversion`, `entry`, `failure`, `opens`.

## D. Test plan

- [x] `bundle exec jekyll build` succeeds
- [x] Filter **Banner** + **Dismissal** → only Banner Dismissal events
- [x] Filter **SMS** + **Delivery** + **Failure** → only SMS Delivery Failure (not SMS Delivery)
- [x] Filter **SMS** + **Sends** + **Carrier** → only SMS Carrier Send (not SMS Send)
- [x] Filter **Agent** + **Tool** → only Tool invocation (not Agent executed)
- [x] `?tags=banner,dismissal` pre-checks both boxes; results match AND
- [x] `?tags=` and `?tags=banner,` do not break filtering (`parseTagsQueryParam` strips empty tokens)
- [ ] VoiceOver / search accessibility behavior unchanged (manual QA)

## E. Out of scope

- Email Soft Bounce vs hard bounce tag split
- `_lang/` localized markdown mirrors (translation pipeline)
- Lazy partner tab / Operator size changes (separate work on branch)
