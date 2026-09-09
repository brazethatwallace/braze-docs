---
nav_title: Email
article_title: Email
page_order: 3
page_type: landing
description: "Create customized and personalized email campaigns in Braze with drag-and-drop and HTML editors, subscription management, and more."
channel:
  - email
search_rank: 2
---

# Email

> With email at Braze, you create customized and personalized email messages in campaigns or Canvases that reach users outside your app or website. This hub covers email setup, drag-and-drop and HTML editors, subscription management, templates, and testing so you can launch compliant, on-brand email programs. Use Braze email templates or custom HTML to match your brand voice and layout. Start with [Email setup]({{site.baseurl}}/user_guide/channels/email/email_setup) if you are configuring a new sending domain. To see examples of email campaigns, refer to the Braze [case studies](https://www.braze.com/customers/).

## Prerequisites

Before you can send email with Braze, you need to configure your dedicated IPs, domains, email authentication, and IP warming. For a full walkthrough, refer to [Email setup]({{site.baseurl}}/user_guide/channels/email/email_setup).

## Customize your emails

You can customize your email messaging in a variety of ways, including:

- [Braze email templates]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template)
- [Custom HTML templates]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template)
- [Editor blocks (email)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email)
- [User subscriptions]({{site.baseurl}}/user_guide/channels/email/subscriptions)
- [Subscription groups]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups)

## Test your emails

[Seed Groups]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups) automatically send copies of your email campaigns to internal users to perform quality assurance. Seed emails include `[SEED]` prepended to the subject line to help you identify them.

## Use cases

| Use case | Explanation |
| --- | --- |
| Re-engagement | Reach users outside of your app, including those who have not installed the app. |
| Onboarding | Onboard and encourage new users to turn on push notifications or share the app on social networks. |
| Rich messages | Allow for rich and dynamic HTML messages. |
| Multimedia content | Ease of multimedia content placement that engages users such as videos and images. |
| Newsletters | Conveniently send monthly or weekly newsletters to maintain user engagement. |
| Transactions | Notify users of recent purchases and deliver important product and shipping information with [transactional emails]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email).
{: .reset-td-br-1 .reset-td-br-2 aria-label="Use cases" }

## Email services {#email-services}

If you need additional support with your email program, Braze offers recurring and one-time services at an additional cost. For more information, contact your Braze account manager.

### Email deliverability services {#email-deliverability-services}

Braze offers two tiers of recurring email support:
1. Deluxe  
2. Standard 

These services can include:

- Audit of historical and current email sending practices with a review of targeting, cadence, and messaging strategies
- Allowlist configuration and customized IP warming plan created by an email deliverability expert
  - Regular check-in calls during your first month (three times per week for Deluxe and once per week for Standard)
- Regular calls with deliverability expert (twice per month for Deluxe and monthly Standard) to provide:
  - Monitoring of deliverability performance by domain
  - Recommendations to improve email program performance and results utilizing data and established best practices
- Mitigate and remediate crisis triage for events that lead to issues like a blocklist for deliverability

## Frequently asked questions

### How do I set up email sending in Braze? {#how-do-i-set-up-email-sending-in-braze}

Configure dedicated IPs, domains, authentication, and IP warming before your first send. Refer to [Email setup]({{site.baseurl}}/user_guide/channels/email/email_setup) for the full checklist.

### What is the difference between user subscriptions and subscription groups? {#what-is-the-difference-between-user-subscriptions-and-subscription-groups}

User subscriptions control global opt-in status for a channel (for example, subscribed or unsubscribed to email). Subscription groups let users choose specific message categories within that channel. Refer to [User subscriptions]({{site.baseurl}}/user_guide/channels/email/subscriptions) and [Subscription groups]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups).

### How can I test an email before I send a campaign? {#how-can-i-test-an-email-before-i-send-a-campaign}

Use [seed groups]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups) to send preview copies to internal reviewers and confirm rendering across clients.

## Next steps

{% article_tiles %}
- name: Email setup
  link: /docs/user_guide/channels/email/email_setup
- name: Create an email with the drag-and-drop editor
  link: /docs/user_guide/channels/email/drag_and_drop
- name: Create an email with the HTML editor
  link: /docs/user_guide/channels/email/html_editor
{% endarticle_tiles %}
