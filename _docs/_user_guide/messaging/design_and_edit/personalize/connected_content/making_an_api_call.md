---
nav_title: Make a Connected Content call
article_title: Make a Connected Content API call
page_order: 0
description: "This reference article covers how to make a Connected Content API call, as well as helpful examples and advanced Connected Content use cases."
search_rank: 2
toc_headers: h2
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"}Make a Connected Content API call

> Use Connected Content to insert any information accessible by API directly into messages you send to users. You can pull content either directly from your web server or from publicly accessible APIs.<br><br>This page covers how to make Connected Content API calls, advanced Connected Content use cases, error handling, and more.

## About Connected Content call volume {#understanding-connected-content-call-volume}

{% alert important %}
One send does not equal one Connected Content call. Braze does not guarantee a 1:1 ratio between message sends and Connected Content requests. The system is designed to favor correct message rendering and delivery over minimizing the number of calls. Your endpoints must be built to handle more requests than the number of recipients or messages sent.
{% endalert %}

Braze may make the same Connected Content API call more than once per recipient. Common reasons include:

- **Email with multiple parts:** A single email can trigger separate rendering passes for the HTML body, plain text body, and Accelerated Mobile Pages (AMP) version (if present). Each pass can trigger Connected Content in that part, so one recipient may generate multiple identical or similar calls.
- **Validation and retries:** Message payloads can be rendered multiple times per recipient for validation, retry logic, or other internal purposes.
- **Channel behavior:** Connected Content executes when the message is rendered. For in-app messages, the message is rendered at impression time.

If you see more Connected Content calls in your logs than sends or recipients, that behavior is expected. For guidance on reducing load and planning for scale, see [Best practices for high-volume endpoints](#best-practices-for-high-volume-endpoints).

## Send a Connected Content call

To send a Connected Content call, use the {% raw %}`{% connected_content %}`{% endraw %} tag. With this tag, assign or declare variables by using `:save`. Aspects of these variables can be referenced later in the message with [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid).

### Break down the API call

The following example uses the Sunrise-Sunset API and includes today's sunrise time in a message:

{% raw %}
```
{% connected_content https://api.sunrise-sunset.org/v2?lat=40.7128&lng=-74.0060&date=today :save result %}
Hi there, today's sunrise in NYC is at {{result.sunrise}}.
```
{% endraw %}

Here's what each part does:

| Component | What it does |
| --- | --- |
| `connected_content` tag | Tells Braze to make an HTTP request while rendering the message. |
| `https://api.sunrise-sunset.org/v2` | The API endpoint Braze calls. |
| `lat=40.7128&lng=-74.0060` | Query parameters for New York City coordinates. |
| `date=today` | Requests data for the current day at those coordinates. |
| `:save result` | Stores the API response in a local variable named `result`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Break down the API call" }

### How the Sunrise-Sunset API response works

This endpoint returns JSON with top-level fields such as `sunrise`, `sunset`, and `tzid`. Times are returned in the location's timezone by default (for this example, New York time).

For example, the response shape is similar to:

```json
{
  "date": "2026-07-23",
  "tzid": "America/New_York",
  "sunrise": "2026-07-23T05:42:11-04:00",
  "sunset": "2026-07-23T20:21:32-04:00"
}
```

### Map the API response to Liquid

Because the response is saved as `result`, reference each field directly from that object.

{% raw %}
```liquid
{{result.sunrise}}
{{result.sunset}}
{{result.tzid}}
```
{% endraw %}

Use this pattern whenever you save JSON from Connected Content:

1. Save the API response with `:save`.
2. Find the field you want in the JSON response.
3. Reference it in Liquid as `saved_variable.field_name`.

### Add variables

You can also include user profile attributes as variables in the URL string when making Connected Content requests. 

For example, you may have a web service that returns content based on a user's email address and ID. If you're passing attributes containing special characters, such as the at sign (@), make sure to use the Liquid filter `url_param_escape` to replace any characters not allowed in URLs with their URL-friendly escaped versions, as shown in the following email address attribute.

{% raw %}
```
Hi, here are some articles that you might find interesting:

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```
{% endraw %}
{% alert note %}
Attribute values must be surrounded by `${}` to operate properly within our version of Liquid syntax.
{% endalert %}

Connected Content requests support GET and POST requests only.

## Error handling

If the URL is unavailable and reaches a 404 page, Braze renders an empty string in its place. If the URL reaches an HTTP 500 or 502 page, the URL fails on the retry logic.

If the endpoint returns JSON, you can detect that by checking if the `connected` value is null, and then [conditionally abort the message]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content). Braze only allows URLs that communicate over port 80 (HTTP) and 443 (HTTPS).

### Unhealthy host detection

Connected Content employs an unhealthy host detection mechanism to detect when the target host experiences a high rate of significant slowness or overload, resulting in timeouts, too many requests, or other outcomes that prevent Braze from successfully communicating with the target endpoint. It acts as a safeguard to reduce unnecessary load that may be causing the target host to struggle. It also serves to stabilize Braze infrastructure and maintain fast messaging speeds.

If the target host experiences a high rate of significant slowness or overload, Braze temporarily halts requests to the target host for one minute, instead simulating responses indicating the failure. After one minute, Braze probes the host's health using a small number of requests before resuming requests at full speed if the host is found to be healthy. If the host is still unhealthy, Braze waits another minute before trying again.

If requests to the target host are halted by the unhealthy host detector, Braze continues to render messages and follow your Liquid logic as if it received an error response code. If you want to ensure that these Connected Content requests are retried when they're halted by the unhealthy host detector, use the `:retry` option. For more information on the `:retry` option, see [Connected Content retries]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries).

If you believe the unhealthy host detection may be causing issues, contact [Braze Support]({{site.baseurl}}/support_contact).

{% alert note %}
You can allowlist specific URLs to be used for Connected Content. To access this feature, contact your customer success manager.
{% endalert %}

{% alert tip %}
For more information about common error codes, see [Troubleshoot webhook and Connected Content requests]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#unhealthy-host-detection).
{% endalert %}

### Rate limits (429) versus unhealthy host detection

The following are different mechanisms:

- **429 Too Many Requests:** Your endpoint (or an upstream service) is returning this response. It means your server or middleware is refusing traffic, often because it has its own rate limit. Braze does not apply a separate rate limit to Connected Content; Connected Content request volume scales directly with your [message delivery speed rate limit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting). Because messages can be rendered multiple times per recipient (for example, for email HTML, plain text, and AMP), the number of Connected Content requests can exceed that rate limit—do not assume it will be less than or equal to the messages per minute you set. If you see 429s, scale your endpoint or middleware to handle the expected request volume, or lower the campaign or Canvas [delivery speed rate limit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) so that fewer messages (and thus fewer Connected Content calls) are sent per minute.
- **Unhealthy host detection:** A Braze-side safeguard that triggers after a high rate and volume of *failures* in a one-minute window. The failure count includes `408`, `429`, `502`, `503`, `504`, and `529` status codes. When triggered, Braze temporarily halts requests to that host and simulates a failure response. This is independent of your own rate limiting. For detection thresholds and more detail, see [Troubleshoot webhook and Connected Content requests]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#unhealthy-host-detection). To avoid hitting unhealthy host detection, ensure your endpoint can handle the call volume described in [Understanding Connected Content call volume](#understanding-connected-content-call-volume) and [Best practices for high-volume endpoints](#best-practices-for-high-volume-endpoints).

## Allow for efficient performance {#allowing-for-efficient-performance}

Because Braze delivers messages at a very fast rate, ensure your server can handle thousands of concurrent connections so it doesn't get overloaded when pulling down content. When using public APIs, confirm your usage won't violate any rate-limiting that the API provider may employ. Braze requires the server response time to be less than two seconds for performance reasons; if the server takes longer than two seconds to respond, the content is not inserted.

For more on planning endpoint capacity and reducing call volume, see [Best practices for high-volume endpoints](#best-practices-for-high-volume-endpoints).

## Things to know

- Braze does not charge for API calls and does not count toward your given data point usage.
- There is a 1 MB limit for Connected Content responses.
- Connected Content executes when the message is rendered. For in-app messages, the message is rendered at impression time.
- Connected Content calls do not follow redirects.

### How Connected Content calls are processed

Connected Content calls within a single message template are executed sequentially (top to bottom) during Liquid rendering. This means downstream calls can reference variables set by upstream calls. In this example, the first call retrieves user data, and the second call uses that data to fetch preferences:

{% raw %}
```liquid
{% connected_content https://api.example.com/user :save user_data %}
{% connected_content https://api.example.com/preferences?user_id={{user_data.id}} :save preferences %}
```
{% endraw %}

### Global sending and request volume

While Connected Content calls execute sequentially within a single message, messages are sent in parallel across your campaigns and Canvases. High-volume sends can generate significant request traffic to your endpoints during peak sending periods. To manage and throttle that traffic—including workspace messaging rate limits, delivery speed rate limiting, and caching—see [Best practices for high-volume endpoints](#best-practices-for-high-volume-endpoints).

## Best practices for high-volume endpoints

If your messages use Connected Content and you send at high volume, plan for more requests than the number of recipients or sends:

- **Estimate peak load:** Use a conservative multiplier when sizing your endpoint or middleware—Connected Content requests can exceed the number of recipients or messages sent. For example, for email a single recipient can generate multiple calls (HTML, plain text, and AMP), so recipients × 2 or × 3 is often used as a conservative estimate.
- **Use caching where appropriate:** GET requests are cached by default. For POST requests, add `:cache_max_age` when the response can be reused for a period (for example, token or content that doesn't change per request). See [Caching responses]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses) and the [POST caching FAQ](#what-is-caching-behavior) in the following section.
- **Set message rate limits:** [Workspace messaging rate limits]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) and [delivery speed rate limiting]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) on campaigns or Canvases indirectly limit Connected Content request volume—Braze does not rate limit Connected Content itself. These are proxies, not perfect ones, because Connected Content requests are not 1:1 with messages. Use them to keep message (and thus Connected Content) volume within what your endpoint can handle.
- **Design for idempotency and retries:** Braze may call your endpoint more than once per recipient. Ensure your endpoint can tolerate duplicate requests without incorrect side effects.

## Authentication types

### Using basic authentication

If the URL requires basic authentication, Braze can store a basic authentication credential for you to use in your API call. You can manage existing basic authentication credentials and add new ones at **Settings** > **Connected Content**.

![The Connected Content settings in the Braze dashboard.]({% image_buster /assets/img/connected_content/basic_auth_mgmt.png %})

To add a new credential, select **Add credential** > **Basic authentication**. 

!["Add credential" dropdown with the option to use basic authentication or token authentication.]({% image_buster /assets/img/connected_content/add_credential_button.png %}){: style="max-width:60%"}

Give your credential a name and enter the username and password.

![The "Create New Credential" window with the option to enter a name, username, and password.]({% image_buster /assets/img/connected_content/basic_auth_token.png %}){: style="max-width:60%"}

You can then use this basic authentication credential in your API calls by referencing the token's name:

{% raw %}
```
Hi there, here is some fun trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
If you delete a credential, keep in mind that any Connected Content calls trying to use it will be aborted.
{% endalert %}

Stored credentials apply to {% raw %}`{% connected_content %}`{% endraw %} requests while Braze renders a message. They are not applied to the primary HTTP request configured in a [webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#authentication-and-connected-content-credentials) step. Use Request headers or a {% raw %}`{% connected_content %}`{% endraw %} tag inside a webhook header or body field when you need to retrieve secrets for that call.

### Using token authentication

When using Braze Connected Content, you may find that certain APIs require a token instead of a username and password. Braze can also store credentials that hold token authentication header values.

To add a credential that holds token values, select **Add credential** > **Token authentication**. Then, add the key-value pairs for your API call headers and the allowed domain.

![An example token "token_credential_abc" with token authentication details.]({% image_buster /assets/img/connected_content/token_auth.png %}){: style="max-width:60%"}

You can then use this credential in your API calls by referencing the credential name:

{% raw %}
```
{% assign campaign_name="New Year Sale" %}
{% connected_content
     https://api.endpoint.com/your_path
     :method post
     :auth_credentials token_credential_abc
     :body campaign={{campaign_name}}&customer={{${user_id}}}&channel=Braze
     :content_type application/json
     :save publication
%}
```
{% endraw %}

### Use Open Authentication (OAuth)

Some API configurations require the retrieval of an access token that can then be used to authenticate the API endpoint that you want to access.

#### Step 1: Retrieve the access token

The following example illustrates retrieving and saving an access token to a local variable, which can then be used to authenticate the subsequent API call. A `:cache_max_age` parameter can be added to match the time that the access token is valid for and reduce the number of outbound Connected Content calls. See [Configurable Caching]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses) for more information.

{% raw %}
```
{% connected_content
     https://your_API_access_token_endpoint_here/
     :method post
     :auth_credentials access_token_credential_abc
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE"
     }
     :cache_max_age 900
     :save token_response
%}
```
{% endraw %}

{% alert note %}
When the token endpoint expects `application/x-www-form-urlencoded` and you pass credentials in `:body`, URL-encode any special characters in parameter values. For example, forward slashes (`/`) become `%2F` and plus signs (`+`) become `%2B`. Unencoded special characters may cause OAuth token requests to fail.
{% endalert %}

#### Step 2: Authorize the API using the retrieved access token

After the token is saved, it can be dynamically templated into the subsequent Connected Content call to authorize the request:

{% raw %}
```
{% connected_content
     https://your_API_endpoint_here/
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE",
       "Authorization": "{{token_response}}"
     }
     :body key1=value1&key2=value2
     :save response
%}
```
{% endraw %}

### Editing credentials

You can edit the credential name for authentication types.

- For basic authentication, you can update the username and password. Note that the previously entered password will not be visible.
- For token authentication, you can update the header key-value pairs and the allowed domain. Note that the previously set header values will not be visible.


## Connected Content IP allowlisting

When a message using Connected Content is sent from Braze, the Braze servers automatically make network requests to our customers' or third parties' servers to pull back data. With IP allowlisting, you can verify that Connected Content requests are actually coming from Braze, adding a layer of security.

Braze will send Connected Content requests from the following IP ranges. The listed ranges are automatically and dynamically added to any API keys that have been opted in for allowlisting. 

Braze has a reserved set of IPs used for all services, not all of which are active at a given time. This is designed for Braze to send from a different data center or do maintenance, if necessary, without impacting customers. Braze may use one, a subset, or all of the following IPs listed when making Connected Content requests.

If Connected Content requests consistently return `403 Forbidden` and authentication is configured correctly, allowlist these IPs on the server that receives the request. A `403` can also indicate insufficient permissions or invalid credentials, so confirm both network and auth settings. For webhook-specific guidance, see [403 Forbidden and IP allowlisting]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#403-forbidden-and-ip-allowlisting).

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### Using IP allowlisting with Amazon S3

When using Connected Content to retrieve files from Amazon S3, configure your bucket to allow unauthenticated HTTP `GET` requests from Braze IP addresses.

1. **Add a bucket policy with IP conditions:** Grant `s3:GetObject` on your bucket objects with `Principal: "*"` and an `IpAddress` condition that uses the [Braze IP ranges](#connected-content-ip-allowlisting) for your instance. You do not need to set public-read ACLs on individual objects.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*",
      "Condition": {
        "IpAddress": {
          "aws:SourceIp": ["{YOUR_BRAZE_IP_RANGE}"]
        }
      }
    }
  ]
}
```

Replace `{YOUR_BRAZE_IP_RANGE}` with the Braze IP ranges for your instance listed in [Connected Content IP allowlisting](#connected-content-ip-allowlisting). You can add one or more ranges as separate values in the `aws:SourceIp` array.

{: start="2"}
2. **Review S3 Block Public Access settings:** Bucket policies that use `Principal: "*"` are treated as public access by AWS, even with IP conditions. You may need to allow bucket-policy-based public access while keeping ACL-based public access blocked.

3. **Use the S3 object URL in your Connected Content tag:** Reference the object with its standard S3 URL (for example, `https://your-bucket.s3.amazonaws.com/path/to/object.json`).

For more information about bucket policies and condition keys, refer to the [AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html).

### `User-Agent` header

Braze includes a `User-Agent` header in all Connected Content and webhook requests that is similar to the following:

```text
Braze Sender 75e404755ae1270441f07eb238f0faf25e44dfdc
```

{% alert tip %}
Keep in mind that the hash value changes regularly. If you're filtering traffic by `User-Agent`, allow all values that start with `Braze Sender`.
{% endalert %}

## Troubleshooting

If your Connected Content call is not rendering correctly or at all, check for the following details:

- **Confirm that a Connected Content call was made:** You can check that a call was made at the [Messaging History tab]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/#messaging-history-tab). You can also test send a single Connected Content request.
- **Verify through Postman or a CURL request to check if the ideal request succeeds:** If the request works and returns a response, compare the request in detail (including headers). Confirm that the headers are captured in key-value pairs with double quotations.
- **Validate authorization is handled correctly:** Confirm the `:basic_auth`/`:auth_credentials` option is used and has added the Connected Content authorization to the Connected Content workspace settings. Sometimes the Connected Content URL requires headers beyond authentication that need to be entered.
- **Verify the data is in an expected format:** For the response body, Braze parses valid JSON into a Liquid object; otherwise, the response is treated as plain text (including HTML). The `:content_type` option sets outbound `Content-Type` and `Accept` headers on your request and doesn't affect response parsing. For the request `:body`, if your JSON contains spaces, follow the guidance in the [Providing JSON body]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/local_connected_content_variables/#providing-json-body) section.
- **Confirm the data has been parsed correctly:** Check that the Liquid is correctly referencing the expected field. For nested JSON, use {% raw %}`{{sampleresult.data[0].sample_field}}`{% endraw %} to point at the intended nested field. You can check the nested JSON properties by printing out the expected outcome with {% raw %}`RESPONSE:{{sampleresult.data}}`{% endraw %}.
- **Check the response status code:** The response status code must be a `2XX` code. Connected Content does not have a way to consume the response when the code is not `2XX`.

You can also use [Webhook.site](https://webhook.site/) to troubleshoot your Connected Content calls and to diagnose issues with the request headers, request body, and other information that is being sent in the call.

1. Switch the URL in your Connected Content call with the unique URL generated on the site.
2. Preview and test your campaign or Canvas step to see the requests come through to this website.

You can also verify the Liquid tag includes the parameters your endpoint expects (for example, `:method`, `:headers`, `:content_type`, `:body`, and `:basic_auth` when required). If you rely on the HTTP status code key in a saved JSON object, the endpoint must return a JSON object and a `2XX` status.

For high error rates from your host, review [Unhealthy host detection]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors#unhealthy-host-detection) and [Connected Content call volume](#understanding-connected-content-call-volume).

## Frequently asked questions

### Why are there more Connected Content calls than users or sends?

Braze may make the same Connected Content API call more than once per recipient to render a message payload. Message payloads can be rendered multiple times per recipient for validation, retry logic, or other internal purposes. However, note that only one of the Connected Content calls populates a message. 

It’s expected that a Connected Content API call can be made more than once per recipient, even if the retry logic is not used in the call. We recommend setting the rate limit of any messages that contain Connected Content or configuring your servers to be better able to handle the expected volume that accounts for multiple Connected Content calls being made per message send.  

See [Understanding Connected Content call volume](#understanding-connected-content-call-volume) and [Best practices for high-volume endpoints](#best-practices-for-high-volume-endpoints) for details and mitigation.

### How does rate limiting work with Connected Content?

Connected Content doesn’t have its own rate limit. Instead, the rate limit is based on the message-sending rate. We recommend setting the messaging rate limit higher than your intended Connected Content rate limit if there are more Connected Content calls than messages sent.  

### What is caching behavior?

GET requests are cached by default (see [Caching responses]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses)). **POST requests are not cached by default**, but you can enable caching by adding `:cache_max_age` to the Connected Content call. This can reduce endpoint load when the same POST (for example, a token or content request) would be made repeatedly within the cache window.

{% raw %}
```liquid
{% connected_content https://api.example.com/token :method post :body grant_type=client_credentials :cache_max_age 900 :save token %}
```
{% endraw %}

Caching can help reduce duplicate Connected Content calls but isn't guaranteed to result in a single call per user. Cache duration is between five minutes and four hours. For full details, see [Caching responses]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses).

### What is the Connected Content HTTP default behavior? 

{% multi_lang_include connected_content/sections.md section='default behavior' %}

{% multi_lang_include connected_content/sections.md section='http post' %}

### What happens if I use the same Connected Content call in multiple places?

Each Connected Content tag is evaluated separately, even if multiple tags use the same URL and parameters. When the URL and cache settings allow, identical requests may be served from cache rather than triggering a new outbound request (see [Caching responses]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/caching_responses) for details).