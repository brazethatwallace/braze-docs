{% alert note %}
For RCS messages, link shortening and URL-level click tracking are supported for URLs in the message body, but not for URLs in suggested actions. Clicks on suggested action URLs are recorded as RCS click events, but the `URL` and `SHORT_URL` fields will be null in Currents and Snowflake.
{% endalert %}
