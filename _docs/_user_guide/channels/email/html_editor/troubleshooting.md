---
nav_title: Troubleshooting
article_title: Troubleshoot HTML emails
page_order: 9
description: "Diagnose HTML email rendering and editor issues using a symptom index and standard troubleshooting steps."
channel: email
---

# Troubleshoot HTML emails

> Use this page to resolve common HTML email editor and test-send issues. For Inbox Vision and deliverability, see [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) and [Email setup]({{site.baseurl}}/user_guide/channels/email/email_setup).

## Start here: Match your symptom

Match your symptom in the table to navigate to the relevant section.

| Symptom | Go to |
| --- | --- |
| Test email HTML looks wrong | [HTML renders incorrectly in test emails](#html-renders-incorrectly-in-test-emails) |
| Editor behaves oddly in Chrome | [Extension conflicts](#extension-conflicts) |
| Email looks different across clients | [Email rendering](#email-rendering) |
| Email HTML modified in user inbox | [Unbalanced HTML in Liquid templates](#unbalanced-html-in-liquid-templates) |
| Inbox Vision preview doesn't match sent email | [CSS inlining](#css-inlining) |
| White space or lines after images in test emails | [White space under images](#white-space-under-images) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="HTML email symptom" }

## Standard investigation path

Use this workflow when HTML email rendering or editor behavior doesn't match what you expect. Start at step 1.

1. Validate your HTML markup in the editor or an external validator.
2. Send a [test email]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa) and note which email clients or browsers show the issue.
3. Preview with [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) to compare rendering across clients.
4. Rule out [browser extension conflicts](#extension-conflicts) if the editor itself misbehaves.
5. If the issue persists, open a [support ticket]({{site.baseurl}}/braze_support) with screenshots from Inbox Vision and the affected clients.

## HTML renders incorrectly in test emails {#html-renders-incorrectly-in-test-emails}

**Symptom:** A [test email]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa) doesn't match what you expect from the editor.

Check your HTML setup first, then review [extension conflicts](#extension-conflicts), [email rendering](#email-rendering), [CSS inlining](#css-inlining), and [white space under images](#white-space-under-images).

### Extension conflicts {#extension-conflicts}

Certain browser extensions may cause issues with the email editor. One example is [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en) when used with Google Chrome. If you're using one of these extensions, you should either:

- Edit Braze emails in a browser that does not have Grammarly as a browser extension
- Contact your Braze account manager and ask to switch your email editors to HTML only or plain text.

The plain text view removes your `WYSIWYG` (what you see is what you get) editor, so you should first confirm that all team members are comfortable with HTML before making this request.

### Email rendering {#email-rendering}

Emails render differently depending on browsers and email clients, so take note of which browsers and email clients you're experiencing issues with.

- Preview your emails using [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision) to see what your emails look like in different browsers and email clients.
- After you've identified which browsers or email clients are causing issues, let your developer team know that they'll need to modify their HTML and make edits to accommodate those browsers or email clients.

#### Unbalanced HTML in Liquid templates {#unbalanced-html-in-liquid-templates}

**Symptom:** Email HTML renders differently in the end user's inbox than expected, with missing elements or broken layouts.

This can occur when HTML tags are not balanced within their corresponding Liquid logic blocks. Braze's HTML parser may modify the underlying HTML if it detects tags that span across Liquid logic boundaries in unexpected ways.

To avoid this, ensure that all HTML tags open and close within the same Liquid block. Do not split HTML tags across Liquid conditionals or loops.

**Example of unbalanced HTML/Liquid:**

```liquid
{% raw %}{% if user.premium %}
<div class="premium-content">
{% endif %}
  <p>Your content here</p>
{% if user.premium %}
</div>
{% endif %}{% endraw %}
```

In this example, the opening `<div>` tag is inside the conditional, but the content and closing tag are split across the logic boundary.

**Correct approach:**

```liquid
{% raw %}{% if user.premium %}
<div class="premium-content">
  <p>Your content here</p>
</div>
{% endif %}{% endraw %}
```

Ensure all HTML tags are fully contained within their Liquid blocks so that the parser can properly validate the HTML structure.

### CSS inlining {#css-inlining}

There are times when the previews in Inbox Vision still don't match what is sent with Braze. This may be caused by the difference in CSS inlining performed by Braze and by other tools. If you suspect that this is the case, turn off CSS inlining.

### White space under images {#white-space-under-images}

**Symptom:** White space or lines appear after images in test emails.

If you notice white space or lines appearing after images in your test emails, this is typically caused by how email clients render inline-level elements. Images are inline-level by default and are aligned to the baseline, which allows browsers to accommodate descenders (the part of letters like "g" or "y" that extend beyond the baseline). This creates a small gap that appears as white space.

To fix this, add `display: block;` to your image CSS:

```html
<style>
  img {
    display: block;
  }
</style>
```

Alternatively, apply the style directly to specific images:

```html
<img src="https://example.com/image.jpg" style="display: block;" alt="Image description" />
```
