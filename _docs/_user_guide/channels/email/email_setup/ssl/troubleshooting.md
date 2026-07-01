---
nav_title: Troubleshooting
article_title: Troubleshoot SSL click tracking
page_order: 5
page_type: reference
description: "Diagnose SSL click-tracking and CDN configuration issues using a symptom index and standard investigation path."
channel: email
---

# Troubleshoot SSL click tracking

> Use this page to identify common SSL click tracking issues. The troubleshooting guidance is generic because every CDN is unique. For CDN configuration, certificates, or proxy issues, contact your CDN's support team, as these configurations take place outside of the Braze ecosystem.

## Start here: Match your symptom

| Symptom | Go to |
| --- | --- |
| Email open rates dropped suddenly | [Low email open rates](#low-email-open-rates) |
| Tracked links return HTTP 403 | [HTTP 403 on redirect links](#http-403-on-redirect-links) |
| DNS or CNAME points to ESP instead of CDN | [Domain registry issues](#domain-registry-issues) |
| "Connection isn't private" or links break during setup | [CDN issues](#cdn-issues) |
| SSL setup complete but links still show HTTP | [SSL enablement status](#ssl-enablement-status) |
| Tracked URL fails but untracked URL works | [Click tracking issues](#click-tracking-issues) |
| Amazon SES–specific SSL enablement errors | [Amazon SES](#amazon-ses) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SSL symptom" }

## Standard investigation path

1. Confirm your click-tracking subdomain points to your [content delivery network (CDN)]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#what-is-a-cdn-and-why-do-i-need-it)—not directly to your email service provider (SendGrid, SparkPost, or Amazon SES). Ask your IT or web team to verify your domain settings match your Braze setup. For Braze requirements, see [Acquire an SSL certificate]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#acquire-an-ssl-certificate).
2. Confirm your SSL certificate is active for the tracking domain. Ask your IT or web team to confirm the certificate is current and covers your click-tracking subdomain. For setup steps and CDN-specific guides, see [Acquire an SSL certificate]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#acquire-an-ssl-certificate) and [Additional resources]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#additional-resources).
3. Send a test email using the [click tracking troubleshooting template](#click-tracking-issues). Compare tracked versus untracked URLs.
4. If tracked links fail with 403, review CDN and WAF rules (user agents, query strings, redirect patterns).
5. If setup is complete but links remain HTTP, contact your Braze customer success manager to confirm Braze enabled SSL.
6. For persistent issues, coordinate with your CDN or IT team and contact [Braze Support]({{site.baseurl}}/braze_support) with error codes and any details from your CDN or domain provider.

## Key concepts

- **Tracked URL:** Wraps the original HTTPS link in your tracking domain. When a user clicks it, the tracking domain resolves the request and redirects to the final destination. A CDN allows you to track secure (HTTPS) URLs. Without it, users may encounter a "connection is not secure" privacy error.
- **Untracked URL:** Maintains the original URL intact, bypassing the CDN to serve as a control environment.

## Low email open rates {#low-email-open-rates}

**Symptom:** Email open rates dropped suddenly after SSL or CDN changes.

If you're suddenly experiencing low email open rates, confirm that the SSL certificate is up-to-date. If it's expired, you must renew that SSL certificate with your CDN or certificate provider.

## HTTP 403 on redirect links {#http-403-on-redirect-links}

**Symptom:** Tracked email links return "403 Forbidden".

If tracked redirect links return "403 Forbidden", the failure often occurs at your content delivery network (CDN) or web application firewall (WAF)—for example, rules on AWS WAF or Amazon CloudFront that block certain user agents, query strings, or redirect patterns. Review blocked-request logs and metrics with your CDN or cloud provider. For AWS, see [Troubleshooting issues with CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/troubleshooting.html).

To see whether the problem is specific to click tracking, turn off click tracking for one test link (see [Turning off click-tracking on a link-to-link basis]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links#turning-off-click-tracking-on-a-link-to-link-basis)). If the destination URL loads when click tracking is off but returns 403 when tracking is on, focus on configuration for your click-tracking domain, CDN, and WAF.

## Domain registry issues {#domain-registry-issues}

**Symptom:** DNS or CNAME for your tracking subdomain points to your ESP instead of your CDN.

Run a dig command to confirm you point link tracking at the CDN. In your terminal run `dig CNAME link_tracking_subdomain`. Under `ANSWER SECTION`, it lists where your CNAME points. If it points to the email service provider (SendGrid, SparkPost, or Amazon SES) and not your CDN, reconfigure your domain registry to point to your CDN.

## CDN issues {#cdn-issues}

**Symptom:** Users see "connection isn't private" errors, or links break during CDN setup.

If live email links break during setup, you likely pointed DNS toward your CDN before proper configuration. This can appear as a "wrong link" error. Contact your CDN provider and review their documentation to troubleshoot configuration.

If you see an error message that your connection isn't private, this can indicate that your SSL or CDN isn't configured correctly. Run a `dig` command in your terminal (for example, `dig CNAME your_link_tracking_subdomain`). In the `ANSWER SECTION`, if the result points to your ESP instead of your CDN, the issue is a misconfiguration. For Braze SSL click tracking to work, the CNAME should point to your CDN. Coordinate with the team that manages your SSL and CDN configuration for further assistance.

## SSL enablement status {#ssl-enablement-status}

**Symptom:** SSL setup is complete but tracked links still appear as HTTP.

If you complete SSL setup and links still appear as HTTP, contact your Braze customer success manager to confirm Braze enabled SSL. Braze enables SSL only after all setup steps are complete.

### Amazon SES

If you're using Amazon SES as your email service provider, the following configuration issues can prevent Braze from enabling SSL or cause errors during setup:

- **Region mismatch:** Confirm your CDN origin points to the AWS tracking domain for your Braze cluster. US clusters use `r.us-east-1.awstrack.me`. EU clusters use `r.eu-central-1.awstrack.me`. Using the wrong region can block SSL enablement.
- **Host header:** Amazon SES requires your CDN to forward the correct host header. Enable the `X-Forwarded-Host` header on your click-tracking domain. For more information, refer to the [Amazon SES](#amazon-ses) section.
- **Proxy configuration:** A proxy or CDN setup that overrides or conflicts with the host header can cause SSL enablement to fail. Review proxy settings with your CDN provider to confirm they don't interfere with host header forwarding.
- **Route 53 alias record:** If you use Route 53 to manage DNS for your domain, create an [alias record in Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html) that points to your CDN distribution (for example, `d111111abcdef8.cloudfront.net`). Using a standard CNAME instead of an alias record can return HTTP 400 errors.
- **Header forwarding disabled:** If SSL enablement still fails after you configure `X-Forwarded-Host`, try disabling header forwarding on your CDN or proxy. Some setups resolve the issue when forwarding is turned off entirely. Work with your IT team or CDN provider to test this configuration.

## Click tracking issues {#click-tracking-issues}

**Symptom:** Tracked email links fail but untracked links work, or users see certificate or DNS errors after clicking.

Common redirection issues typically result from an improper configuration between the CDN hosting the tracking domain and its associated SSL certificates or DNS CNAME records. These misconfigurations often cause users to receive a "connection is not secure" privacy error or a `404` failure after clicking a tracked email link.

Use the following template to test the CDN configuration of your tracking domain, which is the mechanism supporting analytics for links within your emails.

1. Copy and paste the following template into a Braze HTML email campaign.

{% details Click tracking troubleshooting template %}
{% raw %}
```html
<!DOCTYPE html>
<html lang="en" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="color-scheme" content="light dark">
    <meta name="supported-color-schemes" content="light dark">
    <title>Click Tracking Test</title>
    <style>
        /* Base Dark Mode (Default) */
        body { 
            margin: 0; 
            padding: 0; 
            background-color: #2b0562; 
            font-family: 'Helvetica Neue', Arial, sans-serif; 
            color: #ffd1e9; 
        }
        
        .email-container { 
            width: 100%; 
            max-width: 600px; 
            margin: 40px auto; 
            background-color: rgba(255, 255, 255, 0.05); 
            border: 1px solid #F3697F; 
            border-radius: 16px; 
            overflow: hidden; 
        }
        
        .header { 
            background: linear-gradient(135deg, #E83F21 0%, #F3697F 100%); 
            padding: 40px 20px 50px 20px; 
            text-align: center; 
        }

        .logo {
            display: block;
            margin: 0 auto 25px auto;
            border: 0;
            outline: none;
            text-decoration: none;
        }
        
        .header h1 { 
            color: #ffffff; 
            margin: 0; 
            font-size: 26px; 
            font-weight: 800; 
            letter-spacing: -0.5px; 
        }
        
        .content { 
            padding: 40px 40px 20px 40px; 
            line-height: 1.8; 
            font-size: 15px; 
        }

        .troubleshoot {
            margin: 0 40px 40px 40px;
            padding: 25px;
            background-color: rgba(253, 167, 216, 0.1);
            border-radius: 12px;
            font-size: 14px;
            border: 1px dashed #F3697F;
        }
        
        .troubleshoot h2 {
            margin-top: 0;
            font-size: 18px;
            color: #ffffff;
        }

        .btn-section { 
            padding: 0 40px 40px 40px; 
            text-align: center; 
        }
        
        .btn { 
            display: inline-block; 
            padding: 16px 32px; 
            border-radius: 12px; 
            font-weight: 700; 
            text-decoration: none; 
            margin: 10px;
            font-size: 14px;
        }
        
        .btn-tracked { 
            background-color: #F3697F; 
            color: #ffffff; 
        }
        
        .btn-untracked { 
            border: 2px solid #FDA7D8; 
            color: #FDA7D8; 
            background-color: transparent;
        }

        .footer { 
            text-align: center; 
            font-size: 12px; 
            color: #FDA7D8; 
            padding-bottom: 40px; 
            opacity: 0.6; 
        }

        /* Light Mode Overrides */
        @media (prefers-color-scheme: light) {
            body { background-color: #F7FCFF !important; color: #2b0562 !important; }
            .email-container { background-color: #ffffff !important; border: 1px solid #FDA7D8 !important; box-shadow: 0 4px 20px rgba(43, 5, 98, 0.1); }
            .content { color: #2b0562 !important; }
            .troubleshoot { background-color: #F7FCFF !important; border-color: #F3697F !important; color: #2b0562 !important; }
            .troubleshoot h2 { color: #E83F21 !important; }
            .btn-untracked { color: #F3697F !important; border-color: #F3697F !important; }
            .footer { color: #2b0562 !important; }
            strong { color: #E83F21 !important; }
        }

        /* Mobile Optimization */
        @media only screen and (max-width: 480px) {
            .btn { display: block !important; margin: 10px 0 !important; width: auto !important; }
            .content, .troubleshoot { padding: 25px !important; }
        }
    </style>
</head>
{%- capture url -%}https://example.com{%- endcapture -%}
<body>
    <center>
        <table class="email-container" role="presentation" width="600" border="0" cellpadding="0" cellspacing="0">
            <tr>
                <td class="header">
                    <img src="https://cdn-staging.braze.com/appboy/communication/assets/image_assets/images/60aecba96a93150c749b4d57/original.png?1622068137" 
                         width="150" 
                         alt="Logo" 
                         class="logo">
                    <h1>Testing Click Tracking Functionality</h1>
                </td>
            </tr>
            <tr>
                <td class="content">
                    <p>
                        Use this template to test the <strong>CDN configuration</strong> of your tracking domain—the mechanism supporting analytics for links within your emails.
                    </p>
                    <p>
                        A <strong>Tracked URL</strong> wraps the original HTTPS link in your tracking domain. When a user clicks it, the tracking domain resolves the request and redirects to the final destination. A CDN allows you to track secure (HTTPS) URLs; without it, users may encounter a "connection is not secure" privacy error. An <strong>Untracked URL</strong> maintains the original URL intact, bypassing the CDN to serve as a control environment.
                    </p>
                    <p>
                        Common redirection issues typically result from an improper configuration between the CDN hosting the tracking domain and the <strong>associated SSL certificate or DNS CNAME records.</strong>
                    </p>
                    <p>
                        <i style="font-size: 13px;">This template uses "example.com" as the destination URL. To test your own domain, replace the URL in the <strong>capture</strong> tag located on line 125.</i>
                    </p>
                </td>
            </tr>
            <tr>
                <td class="btn-section">
                    <a href="{{url}}" class="btn btn-tracked">Tracked URL</a>
                    
                    <a href="{{url}}" 
                       class="btn btn-untracked"
                       clicktracking="off" 
                       data-msys-clicktrack="0" 
                       ses:no-track="true">
                       Untracked URL
                    </a>
                </td>
            </tr>
            <tr>
                <td>
                    <div class="troubleshoot">
                        <h2>Troubleshooting the Test</h2>
                        <ul>
                            <li><strong>Tracked URL Fails / Untracked Works:</strong> This indicates a CDN or SSL certificate issue. Verify that your SSL certificate is valid and correctly bound to your tracking domain.</li>
                            <li><strong>Privacy Error (HTTPS):</strong> Ensure your CDN is configured to handle port 443 traffic and that the certificate matches your tracking CNAME.</li>
                            <li><strong>Both URLs Fail:</strong> Check the destination URL or your internal network firewall settings.</li>
                            <li>For more information, visit: <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/channels/email/email_setup/ssl">SSL at Braze</a></li>
                        </ul>
                    </div>
                </td>
            </tr>
        </table>
        <div class="footer">
            Braze :: 63 Madison Avenue, 13th Floor :: New York, NY 10016
        </div>
    </center>
</body>
</html>
```
{% endraw %}
{% enddetails %}

{: start="2"} 
2. Configure your URL. Replace the URL in the `capture` tag near the top of the template body (where `https://example.com` is set). For example, replace `https://example.com` with `https://braze.com/docs`.
3. Send a test email to yourself and select both buttons.
4. Verify that the expected behavior and success criteria are as described in the template.

If your untracked URL works but your tracked URL fails, you may have a configuration gap. To troubleshoot, refer to the documentation for your specific ESP and CDN provider. You can also review the [SSL at Braze]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl) for detailed requirements on certificate provisioning.

Use the following table to diagnose common errors when testing click tracking.

| Error code | Troubleshooting | 
| --- | --- | 
| `"Your connection is not private" (NET::ERR_CERT_COMMON_NAME_INVALID)` | Verify that your tracking domain has a valid SSL certificate. |
| `"This site can’t be reached" (DNS_PROBE_FINISHED_NXDOMAIN)` | Check your DNS settings. Ensure your tracking subdomain is configured per your CDN and ESP recommended configuration. |
| `525 / 526 SSL Error` | Check that the SSL setting in your CDN (like Cloudflare) matches your Origin's capability. |
| `404 Not Found` | Check that your CDN is configured to forward the entire URL path to the ESP, rather than pointing to a blank root directory. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Error codes and troubleshooting" }

