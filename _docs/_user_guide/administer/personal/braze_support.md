---
nav_title: Braze Support
article_title: Braze Support
page_order: 4
description: "This page will help you locate the Braze Support Portal to submit Braze product feedback. This page will only be accessible to Braze customers."
alias: /braze_support/
page_type: reference
search_rank: 7
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/the-braze-support-portal/){: style="float:right;width:120px;border:0;" class="noimgborder"}Braze Support

> Learn how to access the Braze Support Portal, submit and track support cases, and provide the information needed for efficient troubleshooting.

## Access the Support Portal

To contact the Braze Support team, navigate to the Braze dashboard and select **Support** > **Get help with Operator** > **Contact Support**.

This opens BrazeAI Operator<sup>TM</sup> with the option to file a support ticket directly. Operator can troubleshoot your issue using context from your conversation and the current screen. If Operator can't resolve your issue, you can ask it to draft a support ticket based on your conversation, and then submit the ticket in the Braze Support Portal (if you are a designated support contact) or through our standard support form.

For more information, see [file support tickets with BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets). If you're unsure whether you are a Braze support contact, contact your company's Braze administrator, Braze success manager, or account owner.

![The "Support" dropdown showing "Get help with Operator".]({% image_buster /assets/img_archive/get_help.png %}){: style="max-width:50%;"}


## Adding designated support contacts

Designated support contacts can access all support cases for your company, regardless of who submitted them. You can set users as designated support contacts directly from the **Edit user** page. 

1. Go to **Settings** > **Company Users**, then search for the user by their name or email address.
2. Either select the user name or hover over the user name row to display a menu. 
3. In the menu, select **Edit** to be redirected to the **Edit user** page.
4. Check the checkbox for **Set this user as a Designated Support Contact for Braze Support Portal**.

### Gaining access

After a user is designated as a support contact, the Braze Support Portal sends that user a welcome email with instructions to set up their access.

## View cases from your company

If you're a designated support contact, use the **My Org's** filter views in the support portal to view all cases submitted by users in your company. Cases from all submission channels (BrazeAI Operator<sup>TM</sup>, web form, email, or portal) are included in these views.

## Best practices for submitting a support case

### Provide as much information as possible

The more insights you can offer, the better. Include specifics like the workspace, the URL to the campaign or segment, and any relevant external IDs. This can help us troubleshoot your issue more efficiently.

### Provide a sample of users

Share a sampling of users rather than the entire affected segment. Providing a smaller number of users helps us narrow our scope and speed up our investigations.

### Clarify expected versus actual behavior

Let us know what you were expecting and what actually happened. This can help us narrow down the possible causes of the issue.

### Attach relevant images

Consider attaching a screenshot to illustrate the problem. Providing these images can significantly aid our understanding of the issue and speed up the resolution process.

### Assess the impact

Select the appropriate severity level to help us assign the right resources to address the problem. 

{% alert important %}
Marking an issue as "Critical" means your production instance is down, and all work within Braze has stopped.
{% endalert %}

## Troubleshooting dashboard load issues

If the Braze dashboard isn't loading correctly, try the following before you contact Support:

1. Open the dashboard in a different browser or an incognito or private window.
2. [Clear your browser cache and cookies]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account#clearing-your-browser-cache-and-cookies).
3. Disable ad blockers and browser extensions, then reload the dashboard.
4. If you use a VPN, disconnect and try again.

If your browser developer console shows `ERR_BLOCKED_BY_CLIENT`, an extension or ad blocker is blocking dashboard resources. Disable the blocker for your Braze dashboard URL and reload the page.

## Troubleshooting access

If you receive an error when logging into the Braze Support Portal, such as `Check your entry`, make sure you followed the link in your welcome email to set a password for the portal. If you've done that or were previously able to log into the portal, create a Support ticket.
