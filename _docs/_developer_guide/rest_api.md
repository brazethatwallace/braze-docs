---
nav_title: REST API
config_only: true
noindex: true
page_order: 2.9
---

---

## Troubleshooting

### Should I use uppercase or lowercase for REST API request headers?

Treat HTTP request headers as case-insensitive. Braze accepts common header names such as `Authorization` and `Content-Type` regardless of casing.

For example, all of the following are valid:

- `Authorization: Bearer YOUR-REST-API-KEY`
- `authorization: Bearer YOUR-REST-API-KEY`

Use consistent casing in your client, but do not rely on exact-case header matching for authentication. For request examples, see [API key authentication]({{site.baseurl}}/api/basics/#api-key-authentication).

