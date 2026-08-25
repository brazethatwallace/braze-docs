---
nav_title: SSL at Braze
article_title: SSL Overview
page_order: 5
page_type: reference
description: "This reference article covers SSL, what it is used for, and how it is used at Braze."
channel: email

---

# SSL at Braze

> A secure socket layer (SSL) encrypts a URL with HTTPS instead of HTTP. HTTPS indicates that a valid and trusted SSL or TLS certificate exists and that the website is safe to visit.

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

## Why is SSL important?

Most domains do not require SSL, but Braze strongly recommends using SSL for these reasons.

Securing your website and links with SSL is a common practice even for companies that don't deal directly with sensitive customer information. Users are more trusting of links that are secured with SSL, and the additional layer of authentication helps protect your data.

### Necessary for click and open tracking

Braze transforms your links using your branded link tracking subdomain to track clicks and opens. By default these links begin with HTTP. Users with browsers or extensions that restrict non-secure traffic may have difficulty passing through the redirect before the destination URL, even if the URL is secure. This can cause broken images and inaccurate tracking. Apply SSL to the link tracking subdomain to confirm secure redirects.

## Requirements

### Browser

Major browsers such as Google Chrome restrict traffic through non-secure URLs to protect users. Using SSL helps confirm that content is trusted and minimizes issues like broken links and images in emails.

### HSTS domains 

If you have an HTTP Strict Transport Security (HSTS) domain, set up SSL and configure a CDN to send required security certificates. Without SSL, image and web links break.

## Acquire an SSL certificate

Acquire an SSL certificate through a third party, usually a Content Delivery Network (CDN). A CDN hosts the certificate and serves it to the browser when a user clicks a link by redirecting traffic through the CDN to apply certificates before sending it to SendGrid or SparkPost.

To start SSL setup, contact your Braze customer success manager to initiate a full Braze email setup.

After Braze initiates setup, follow these steps:

1. Braze will provide DNS records to add to your domain registry.
2. Braze will verify if records have been added to your registry correctly.
3. After this, select a CDN and obtain SSL certificates from a third-party provider.
4. At this point, you set up your CDN. Note that Braze cannot help troubleshoot CDN configuration. Contact your CDN provider for any further assistance.
5. Contact your customer success manager to get SSL turned on.

## What is a CDN, and why do I need it?

A content delivery network (CDN) is a platform of servers that helps ensure quick load times of content across multiple mediums while also handling security certificates. 

{% alert important %}
CDN configuration always follows after getting your DNS records validated by Braze. If you have not yet initiated this step, contact your customer success manager for more information on how to get started.
{% endalert %}

For click and open tracking, delivery partners transform links using a branded subdomain and the CDN applies the SSL certificate to those transformed links. Partners often must present valid certificates to the recipient's browser for links and images to display correctly. Because Braze doesn't request or manage certificates, you must set this up through a CDN. 

{% alert note %}
If you can't or don't want to use the listed CDNs for SSL click and open tracking, you may set up a custom SSL configuration. Alternate CDNs or custom proxies can result in a more complex setup. Refer to [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) and [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/) documentation.
{% endalert %}

### Additional resources

{% alert important %}
For troubleshooting your CDN configuration, contact your CDN provider or see [Troubleshooting]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/troubleshooting) for generic guidance.
{% endalert %}

Refer to the following resources by ESP partners on how to configure certain CDNs. While your specific CDN may not be listed, you must make sure your CDN has the ability to apply SSL certificates. 

When you configure your CDN's click-tracking domain, enable the `X-Forwarded-Host` header to prevent potential security issues such as host header attacks. Refer to CDN documentation or your support team for steps.

| Partner | CDN | Documentation |
| --- | --- | --- |
| Amazon SES | AWS CloudFront | [Using HTTPS with CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html) |
| Amazon SES | CloudFlare | [Get started with SSL/TLS](https://developers.cloudflare.com/ssl/get-started/) |
| Amazon SES | Fastly | [Setting up TLS with certificates Fastly manages](https://www.fastly.com/documentation/guides/getting-started/domains/securing-domains/setting-up-tls-with-certificates-fastly-manages/) |
| Amazon SES | KeyCDN | [How to set up custom SSL](https://www.keycdn.com/support/how-to-setup-custom-ssl) |
| Amazon SES | Google Cloud | [Google-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs) |
| SendGrid | AWS CloudFront | [How to configure SSL for click tracking using CloudFront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront) |
| SendGrid | CloudFlare | [Using CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare) |
| SendGrid | Fastly | [Using Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly) |
| SendGrid | KeyCDN | [Using KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) |
| SparkPost | AWS CloudFront | [Step-by-step guide with AWS CloudFront](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-aws-cloudfront) |
| SparkPost | CloudFlare | [Step-by-step guide with Cloudflare](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-cloudflare) |
| SparkPost | Fastly | [Step-by-step guide with Fastly](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-fastly) |
| SparkPost | Google Cloud Platform | [Step-by-step guide with Google Cloud Platform](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-google-cloud-platform) |
| SparkPost | Microsoft Azure | [Step-by-step guide with Microsoft Azure](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Additional resources" }

### Amazon SES

If you are using Amazon SES as your ESP, refer to **Option 2: Configuring an HTTPS domain** in [Amazon SES's documentation](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) and specify the AWS tracking domain by region based on your Braze cluster:

- **Braze US clusters:** `r.us-east-1.awstrack.me`
- **Braze EU clusters:** `r.eu-central-1.awstrack.me`

{% alert important %}
When you configure your CDN's click-tracking domain, enable the `X-Forwarded-Host` header to prevent potential security issues such as host header attacks. Refer to your CDN provider for steps.
{% endalert %}

## Click and open tracking URL patterns

Your email service provider (ESP) rewrites each tracked link to point at your click tracking domain, then adds a path prefix that marks the request as a tracked click or open. Braze doesn't build these paths. Your ESP adds them when it rewrites the link. For CDN or proxy rules, security allowlists, or mobile app link handling, use your ESP's documentation as the source of truth.

| ESP | Path patterns | ESP documentation |
| --- | --- | --- |
| SendGrid | `/wf/click?upn=...` for tracked clicks, and `/uni/wf/click?upn=...` for links you flag as universal links. Depending on your configuration, branded links can also use `/ls/click` (long signed) or `/ss/` (shortened). | [Universal links](https://www.twilio.com/docs/sendgrid/ui/sending-email/universal-links) and [shortened links](https://support.sendgrid.com/hc/en-us/articles/44375837088795-How-to-Know-if-my-Links-Are-Shortened-by-SendGrid) |
| SparkPost | `/f/` for tracked clicks and `/q/` for tracked opens. Links that set a `data-msys-sublink` custom path follow `/f/{custom_path}/`. | [Deep links](https://docs.sparkpost.com/docs/tech-resources/deep-links-self-serve) |
| Amazon SES | `/CL0/{encodedUrl}/{index}/{messageId}/{hmac}` for tracked clicks. Links that set the `ses:custom-path` attribute follow `/CL1/{customPath}/{encodedUrl}/...`. | [Custom open and click domains](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Click and open tracking URL patterns by ESP" }

For example, if your click tracking domain is `clicks.example.com` and your ESP is SparkPost, a tracked click resolves to a URL that starts with `https://clicks.example.com/f/`.

{% alert important %}
Your ESP owns these path prefixes and can change them or add new ones, so Braze can't guarantee a permanent or exhaustive list. When your security tooling supports it, allowlist your full click tracking domain instead of individual paths, and confirm current patterns in your ESP's documentation.
{% endalert %}

To handle these paths in your mobile app, refer to [Universal links and App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links).

## Troubleshooting

While you should handle CDN configuration, certificates, and proxy issues with your CDN, use these tips to identify common SSL click tracking issues. For troubleshooting guidance, refer to [Troubleshooting]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/troubleshooting).

