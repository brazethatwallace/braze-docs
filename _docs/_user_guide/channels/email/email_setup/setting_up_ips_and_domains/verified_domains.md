---
nav_title: Verified domains
article_title: Verified domains
page_order: 0
page_type: tutorial
channel: email
description: "This how-to article covers how to set up verified domains so Braze can manage DNS for email sending and HTTPS click tracking."
toc_headers: h2
---

# Verified domains

> Verified domains let you grant Braze control of a specific subdomain to automate email setup and HTTPS tracking. With DNS domain delegation, Braze manages the DNS records needed for email sending and click tracking. For example, if your subdomain is "mail.example.com", you can delegate it to Braze to set up your sending and tracking domains.

{% alert important %}
Verified domains currently support Amazon SES only. If you're using SendGrid or SparkPost, this feature isn't available.<br><br>Verified domains is supported for email only. {% multi_lang_include product_feedback_cta.md context="gap" feature="verified domains for channels other than email" %}
{% endalert %}

## Benefits

- Faster onboarding: Automating these steps reduces email onboarding time.
- Less coordination: You no longer need to work with Braze Support for domain configuration tasks, which moves you toward a fully self-serve experience.
- Automated SSL management: Braze handles SSL certificate creation and renewal, which removes a common point of failure and manual overhead. Securing your links with SSL is a standard best practice—recipients are more likely to trust secured links, and the additional layer of authentication helps protect your data.
- Fewer configuration errors: Guided onboarding flows and automated validation replace error-prone manual DNS setup, so you have fewer chances to misconfigure records and break email setup.
- Proactive monitoring: Braze monitors your DNS records and notifies you when it detects issues, instead of waiting for failures to surface.

## Considerations

Before you start, keep the following details in mind:

- Choose a dedicated subdomain. After completing domain delegation, Braze manages all DNS records for that subdomain. Braze recommends delegating a subdomain rather than your brand's parent domain, because delegating a parent domain means you lose visibility and control over it. If you want to use a parent domain, use one that isn't used anywhere else.
- NS (nameserver) delegation is required so that Braze can manage your subdomain's DNS records such as SPF, DKIM, and HTTPS tracking without requiring you to configure each one manually.

{% alert note %}
CNAME delegation isn't supported. {% multi_lang_include product_feedback_cta.md context="gap" feature="CNAME delegation for verified domains" %}
{% endalert %}

- Plan for a minimum three-level sending subdomain. Because Braze creates a subdomain under your delegated domain (such as "mail.example.com"), your sending domain needs to be at least three levels deep. An example is "e.mail.example.com".
- Braze manages your DNS records. After delegation is complete, Braze is responsible for the DNS records on the delegated subdomain. Don't modify these records on your own, as this can cause an issue with your email sending.
- The "Edit Domain Settings" permission is required for you to set up verified domains.

## Step 1: Add the verified domain

1. Go to **Settings** > **Verified Domains** > **Add verified domain**. 
2. Enter the subdomain and the root name. For example, if you are delegating the subdomain "mail.example.com" to Braze, the root name is "example.com", and the subdomain is "mail".
3. Confirm that the subdomain you choose is not in use elsewhere and does not have any conflicting DNS records.
4. Select **Add** to receive the TXT and NS records.

## Step 2: Configure DNS records

After submitting the verified domain, Braze generates the required DNS records you must add to your DNS provider. This step may require you to coordinate with your IT or DNS team. You have 30 days for the records to be verified before they expire. After that, you need to go through setup again.

{% alert tip %}
Confirm all four NS records are explicitly present using the `dig` command and that the domain validates in the dashboard before considering setup complete. DNS verification expires after 30 days.
{% endalert %}

## Step 3: Verify the domain

After DNS records have been propagated, Braze verifies the records are present and correctly configured within 24 hours. On successful verification:

- The domain status updates to **Verified**.
- Braze sends an email notifying you that the domain is ready.
- The domain appears as active in the **Verified Domains** list.

After a subdomain is successfully delegated, create email domains such as your sending and tracking domains by going to **Add custom domain**. Then, you're directed to the **Sender Verification** page to finish your setup. For detailed steps, see [Email self-serve]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/email_self_serve).
