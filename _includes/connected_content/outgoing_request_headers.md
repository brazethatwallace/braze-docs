Braze adds the following headers to outgoing Connected Content requests. Most are set only when you have not already provided them in the tag. Headers you supply with `:headers`, credentials, or tag options are sent as provided.

| Header | When Braze sets it |
| --- | --- |
| `User-Agent` | If you have not already set it, Braze sends `Braze Sender <version>`. The version string can change. If you filter traffic by `User-Agent`, allow all values that start with `Braze Sender`. To send a consistent value, set `User-Agent` in `:headers`. |
| `X-Braze-Sender-Version` | Always set to the Connected Content sender version. |
| `Accept-Encoding` | If you have not already set it, Braze sends `gzip`. |
| `Authorization` | If the URL includes a username and password (`user:pass@host`), Braze adds a Basic `Authorization` header derived from those credentials. An explicit `Authorization` header overrides it. Prefer [`:basic_auth`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#using-basic-authentication) or `:headers` instead of putting credentials in the URL. |
| `Host` | Hostname from the request URL (for example, `www.example.com` for `https://www.example.com/abc/123`), unless you set a `Host` header. |
| `Content-Length` | Size of the request body in bytes when a body is present. |
| `BrazeToBraze` | Set to `true` only for requests to Braze REST endpoints. Omitted for other destinations. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Outgoing request headers Braze adds to Connected Content" }
