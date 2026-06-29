---
nav_title: "Sender Verification"
article_title: Sender Verification
permalink: /sender_verification/
description: "This article covers how to set up sender verification and delegate your own subdomains to Braze."
hidden: true
---

# Sender Verification

> This page covers how to delegate your own subdomains to Braze. Use sender verification to set up and delegate control of a dedicated sending subdomain to Braze—allowing for stronger brand consistency with your From domain and tracking links living under the same subdomain.

{% alert important %}
This feature is in beta and is only available to internal Braze teams. 
{% endalert %}

## How Sender Verification works

Domain delegation is a DNS setup option that allows you to delegate control of a specific sending subdomain to Braze. For example, if you use “marketing.example.com” as your subdomain, Braze manages its DNS records required for messaging features, such as email.

### Benefits

Using sender verification helps simplify setup and maintenance. Braze creates and updates what’s needed, which means there are fewer opportunities for DNS misconfiguration. 

### Considerations

- Choose a dedicated subdomain.
- After completing domain delegation, Braze manages your DNS records for the delegated subdomain. 
- If you have multiple brands or Braze workspaces, you can select one delegated subdomain per brand.
- There is a limit of 50 sending domains and 50 tracking domains to Sender Verification. If you need to add more, please reach out to the Braze Support team.

## Step 1: Complete prerequisites

In the Braze dashboard, go to **Settings** > **Sender Verification** under **Company Settings** and work with your onboarding manager to complete the following prerequisites:

- Add an IP pool
- Add IP addresses
- Add a delegated domain and verify NS record

## Step 2: Add your sending subdomain

1. In the **Sending domains** section, select **Add sending domain**. 
2. Enter the **Mail from** and **Sending domain** fields with your sending subdomain for the IP pool. An example is "marketing.mail.example.com"
3. Select your delegated domain from the dropdown.
4. Then, select **Submit**. 

![Form showing fields for Mail from address and Sending domain, with a delegated domain dropdown and Submit button.]({% image_buster /assets/unlisted_docs/img/sender_verification/sending_subdomain.png %}){: style="max-width:85%;"}

It takes 5 to 10 minutes for the DNS records to propagate. After that is completed, you’ll receive a notification email that your domain is ready for use.

{% alert important %}
Domains can’t be changed after they’re submitted. Braze creates DNS records for verification and authentication and add them to your DNS settings.
{% endalert %}

## Step 3: Add your tracking subdomain

After creating a subdomain and having it verified:

1. Select **Add tracking domain**.
2. Enter the tracking subdomain. For example, if your tracking subdomain is “click”, your subdomain would be: "click.marketing.mail.example.com"
3. Select the associated sending domain from the dropdown. 
4. Then, select **Submit**. 

![An example tracking domain to be added.]({% image_buster /assets/unlisted_docs/img/sender_verification/tracking_domain.png %}){: style="max-width:85%;"}

It can take up to 24 hours for these DNS records to propagate, but usually takes less time. After that is completed, you’ll receive a notification email that your domain is ready for use.

{% alert important %}
The tracking domain must be a subdomain of the sending domain for proper DNS delegation.
{% endalert %}

## Step 4: Select the workspaces

Next, select workspaces that should have access to the domain and select **Confirm**. You can optionally automatically add a sending domain to new workspaces when they are created.

![Dialog showing workspace selection checkboxes with option to automatically add sending domain to new workspaces and a Confirm button.]({% image_buster /assets/unlisted_docs/img/sender_verification/select_workspaces_domain.png %}){: style="max-width:85%;"}

## Step 5: Test your email sending

When the sending and tracking domains have a **Ready for use** status, you can test email sending by doing the following:

1. In your workspace, go to **Settings** > **Email Settings**. 
2. Verify that the new sending domain is listed in the **Display Name Address** section.
3. Add the email address using the new domain (such as “marketing@marketing.mail.example.com”)
4. Select **Save**.
5. Next, create a test email campaign and send an email to yourself to confirm the following:
- Your email was delivered successfully.
- The From address is correct.
- The click tracking link uses the tracking domain.
- Your email headers display properly.
