# Korean style guide

## Technical loanwords

- For English **query** in the database / SQL / analytics sense, write **쿼리** (the standard hangul loanword). Do **not** write **퀴리** — that sequence is a common mis-rendering and reads as a misspelling to Korean readers. Use **SQL 쿼리 빌더**, **AI 쿼리 빌더**, etc., when localizing Query Builder and related UI copy.

## Canvas in navigation and chrome

- In **`nav_title`** and other very short YAML labels, avoid gluing the English product name **Canvas** to Korean grammar with **의** (for example `Canvas의 …`). Prefer **캔버스** in compounds when that matches the **Cross-section consistency** / sibling pages for the same locale, so left-nav and search cards stay consistent (PR #13316).

## SDK link wording

- When English refers to an SDK **method** (for example a **refresh** method in developer docs), prefer **메서드** in the Korean link text or sentence — not the generic **방법** — when you mean a callable API/SDK method.

## Register and tone

- Use polite Korean (합니다 form) — this is the standard for friendly technical content in Korean
- The tone should be friendly, conversational, and informative — approachable rather than stiff or academic
- Content should sound conversational, as if explaining something to an acquaintance
