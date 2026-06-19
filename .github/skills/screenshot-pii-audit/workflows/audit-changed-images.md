# Workflow: Audit changed screenshots for PII

## Step 1: Collect changed images

From the git diff against `develop`, collect added or modified files matching:

- `assets/img/**/*.png`
- `assets/img/**/*.jpg`
- `assets/img/**/*.jpeg`

If none, report:

> No changed screenshots under `assets/img/` — nothing to audit.

Stop.

## Step 2: Run the PII scanner

Requires [Tesseract OCR](https://github.com/tesseract-ocr/tesseract):

- macOS: `brew install tesseract`
- Ubuntu/CI: `apt-get install tesseract-ocr`

```bash
python3 scripts/check_screenshot_pii.py --json /tmp/pii-violations.json path/to/image1.png path/to/image2.png
```

If the script exits **2**, report the dependency or sidecar JSON error and stop.

## Step 3: Handle results

### Clean pass (exit 0)

> Screenshot PII audit passed for [N] image(s).

Stop.

### Violations (exit 1)

For each active (non-dismissed) violation:

1. **Read the image** with vision to confirm the OCR finding.
2. Classify:
   - **True positive** → instruct author to retake from [dashboard-06](https://dashboard-06.braze.com/) or blur identifiers.
   - **False positive** → add a sidecar file (see below).

Report using this template:

```markdown
## Screenshot PII audit — action required

| File | ID | Type | Match | Action |
|------|----|------|-------|--------|
| `assets/img/...` | abc12345 | numeric_user_id | `42004428` | Blur or retake |

### How to fix true positives

- Use dashboard-06 (FakeBrandz) fixture data — never production exports.
- Blur `external_id` columns, preview rows, and customer-specific attribute names.
- Replace **real person names** (employees, customers) with fictional examples from the writing style guide.
- For **fictional example names** already in the screenshot, add a sidecar documenting they are not real (see references).
- Replace production CSV filenames with generic examples (`sample_import.csv`).

### False positive dismissal

Create `assets/img/your-image.png.pii-audit-dismiss.json`:

\`\`\`json
{
  "reason": "Explain why this is safe to publish (required audit trail, min 10 chars)",
  "dismiss_ids": ["abc12345"]
}
\`\`\`

Re-run the script locally to confirm a clean pass. A maintainer may add the `pii-audit-dismissed` label after review.
```

## Step 4: Re-run until clean

After fixes or sidecars, re-run:

```bash
python3 scripts/check_screenshot_pii.py --json /tmp/pii-violations.json [images...]
```

Do not mark the task complete until exit code is 0, or the user confirms a maintainer label dismissal.

## Reference patterns

See [references/pii-patterns.md](references/pii-patterns.md) for what the scanner flags and common false positives.
