### External font domains

When creating custom {{ include.page_type }} pages, Braze sanitizes HTML inputs to prevent cross-site scripting (XSS) attacks. As part of this security measure, external resource URLs—including font URLs—are removed unless they're from the following allowed domains:

- `assets.appboycdn.com`
- `braze-images.com`
- `cdn.braze.com`
- `cdn.braze.eu`
- `fonts.googleapis.com`
- `fonts.gstatic.com`

If you need to use custom fonts in your {{ include.page_type }} page, reference fonts from one of these domains or use [web-safe fonts](https://www.w3schools.com/cssref/css_websafe_fonts.php) instead.

For email list management best practices, see [Email subscriptions]({{site.baseurl}}/user_guide/channels/email/subscriptions/).
