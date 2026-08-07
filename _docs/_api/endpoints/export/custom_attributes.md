---
nav_title: Custom attributes
config_only: true
noindex: true
page_order: 10
---

---

## Troubleshooting

### I receive "Error while parsing request body. Please check your syntax."

Braze returns this error when the request body is not valid JSON. Common causes include trailing commas, comments inside JSON, single-quoted strings, an extra opening `{` before the payload, or sending a concatenated string instead of a JSON-encoded object.

Before you retry:

1. Validate the payload with a JSON linter.
2. Set `Content-Type: application/json` and send UTF-8 encoded JSON.
3. Compare your request structure to the [example batch request]({{site.baseurl}}/api/api_limits#example-batch-request) and the batching guidance for [`/users/track`]({{site.baseurl}}/api/api_limits#batch-user-track).

For additional `400` causes (payload size, per-request object limits), see [Why do I get `400 Bad Request` with a bad syntax or parse error?]({{site.baseurl}}/api/endpoints/user_data/post_user_track#why-do-i-get-400-bad-request-with-a-bad-syntax-or-parse-error) and [Fatal errors]({{site.baseurl}}/api/errors#fatal-errors).

