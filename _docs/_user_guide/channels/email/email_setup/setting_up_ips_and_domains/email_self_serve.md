---
nav_title: Email self-serve
article_title: Email self-serve
page_order: 0
page_type: tutorial
channel: email
description: "This how-to article covers how to set up sending and tracking domains with email self-serve in Braze."
toc_headers: h2
---

# Email self-serve

> This page covers how to set up sending and tracking domains in Braze so your From domain and tracking links share the same subdomain.

## Prerequisites

To use self-service email setup, you must meet the following prerequisites:

- Be a new customer in onboarding
- Have the "Edit Domain Settings" company-level permission
- Have an IP pool, IP addresses, and a verified domain

## Considerations

- Plan for a minimum three-level sending subdomain. Because Braze creates a subdomain under your delegated domain (such as "marketing.example.com"), your sending domain needs to be at least three levels deep (such as "e.marketing.example.com").
- The sending domain must be subordinate to a domain you own. For example, if you own "example.com", a subdomain could be "mail.example.com", which allows you to use the sending address "@mail.example.com".
- Domain limits apply. The total number of tracking domains is limited to 2 multiplied by the number of verified domains in your contract. If you need more, contact your account manager.

## Setup

### Step 1: Add a sending domain

Your sending subdomain is the address your emails are sent from. It determines the "from" address your recipients see.

1. In the **Domains** section, select **Add domain**.
2. Add your sending domain to the **Mail from** and **Sending domain** fields for the IP pool. 
    - The **Mail from** (envelope sender or return path) address is what handles bounces behind the scenes. Your recipients do not see this on an email. For example, you might use "bounce" as the subdomain, so the custom mail from email is "bounce.mail.example.com". Using this subdomain is a best practice for DMARC SPF alignment. 
    - The **Sending domain** is the domain in the From address that recipients see in their inbox. For example, if the From address is "hello@e.mail.example.com", then "e.mail.example.com" is the sending domain.
{: start="3"}
3. Select your verified domain from the dropdown.

Sending domains can't be changed after they're submitted. Braze creates DNS records for verification and authentication and adds them to your DNS settings. If you need to delete a sending domain, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) for assistance.

### Step 2: Add a tracking domain

A tracking domain is used to wrap links in your emails for click-tracking and branding purposes. Recipients see this when they hover over or click links in your emails. It must be a subdomain of your sending or verified domain for proper DNS delegation.

1. Select whether you are using a **Verified domain** or **Sending domain** to be used as the subdomain for your tracking domain:
    - If you want the tracking URL to match the sending domain for brand consistency, select **Sending domain**. 
    - If you want a shorter tracking URL, select the **Verified domain**.

{: start="2"}
2. Enter your tracking subdomain. This prepends the subdomain selected previously.

The following example shows how the tracking domain displays in the email based on your selection:

|  | Selection | Tracking domain |
| --- | --- | ---|
| Verified domain | mail.example.com | links.mail.example.com |
| Sending domain | marketing.mail.example.com | links.marketing.mail.example.com |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tracking domain by selection" }

{: start="3"}
3. Select the associated verified or sending subdomain to be used from the dropdown.
4. Select **Submit**. You can see the sending and tracking domains with a **Pending** status. 

It can take 5 to 10 minutes for the DNS records to propagate for sending domains. When your domain is ready to use, you receive a notification email. DNS records for tracking domains can take up to 24 hours to propagate, though it usually takes less. You may see the sending subdomain become ready before the tracking domain.

### Step 3: Select workspaces

Select the workspaces that should have access to the domain, then select **Confirm**. You can also choose to automatically add the sending domain to new workspaces when they're created.

### Step 4: Set up universal links (optional)

Universal links let the links in your messages open directly in your mobile app instead of a mobile browser. Braze can host the association files on your tracking domains on your behalf.

{% alert note %}
Universal links are applied per tracking domain. The same file contents can be shared across domains, but each domain hosts its own copy.
{% endalert %}

1. Go to **Settings** > **Company Settings** > **Verified Domains** > **Universal Links**.
2. Select **Set up universal links**.
3. Enter a universal links set name.
4. Turn on iOS configuration and add your AASA file. JSON is the only accepted file type. Braze reads the file and shows the number of app IDs and components it found, plus a preview of the generated file.
5. Turn on Android configuration and add your Digital Asset Links file the same way. Braze shows the package names, the SHA-256 certificate fingerprint, and the number of statements, plus a preview.
6. Check each preview to confirm the contents look right, then select **Next: Select tracking domains**. Only verified tracking domains appear. One set can apply to multiple tracking domains.
7. Your set appears on the Universal Links page along with its tracking domains, channels, iOS status, Android status, and creation date. Braze checks that the AASA file is properly hosted for each domain and reports the result in the status column.

### Step 5: Test your email sending

After both the sending and tracking domains show a **Ready for use** status, test your setup:

1. In your workspace, go to **Settings** > **Email Settings**.
2. Verify the new sending domain is listed in the **Display Name Address** section.
3. Add a From address using the new domain (for example, "hello@e.mail.example.com").
4. Select **Save**.
5. Create a test email campaign and send it to yourself. Then, confirm that:
    - Your email was delivered successfully.
    - The From address is correct.
    - Click tracking links use the tracking domain.
    - Universal links are opening the app or website as expected based on the recipient's device.
    - Email headers display properly.

## Next steps

After your sender verification is complete, Braze recommends IP warming so that your messages reach their destination inboxes at a consistently high rate. After completing this setup, consult with the Braze Onboarding team to confirm whether your domains and [IP warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) are working.

## Troubleshooting

### DNS propagation is taking longer than expected

Sending domain records typically propagate within 5 to 10 minutes. Tracking domain records can take up to 24 hours depending on your DNS provider's TTL settings. If propagation takes longer, confirm that the NS records were added correctly first, and then contact Braze Support.

### I'm not able to remove a verified domain

Verified domains can't be removed directly in the dashboard as this can potentially break your sending if not properly reviewed. Contact Braze Support to help you remove the domain from your account.

### My universal links aren't opening the app

Check the iOS and Android statuses on the Universal Links page first. If a domain isn't hosting a valid file, open the set, correct the configuration, and save again. If the statuses look fine, make sure you're testing from a link in an email on a real device rather than pasting the URL into the browser address bar.

## Frequently asked questions

### Can Braze manage my SSL certificate without NS delegation?

Verified Domains requires NS (Name Server) records for DNS ownership delegation to Braze. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="Braze-hosted SSL certificates without NS delegation" %}

### Can I delegate a root domain instead?

Verified Domains is primarily designed and recommended for use with subdomains. We don't recommend delegating your brand's primary parent domain for security purposes, because you lose visibility and control over it. If you want to delegate a parent domain, use a parent domain that isn't used anywhere else besides Braze.

### Why can't my verified domain also be the sending domain? 

Braze can only create a sending subdomain under your verified domain, which is typically a subdomain of the parent domain (`mail.example.com`). Therefore, the minimum depth of the sending domain in this case is three levels (`e.mail.example.com`), instead of the typical two levels. 

### What happens if I modify any of my NS records after setup?

Verified domains are fully dependent on the NS records being intact. If you make changes to any of your NS records, this can break your email sending and tracking. 

### Can I add only one of four NS record lines, since my dig command shows all four records? 

Confirm all four NS records are explicitly present using the `dig` command and that the domain validates in the dashboard before considering setup complete. 
