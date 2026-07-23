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
| Email displays Liquid code or broken links | [Unbalanced HTML in Liquid templates](#unbalanced-html-in-liquid-templates) |
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

**Symptom:** Some users receive a modified version of the email where Liquid code displays in the message, links are broken, or spacing looks incorrect.

Braze uses an internal HTML parser to prepare emails before sending. This parser supports features like preheader generation, tracking pixel placement, link templating, and link aliasing. When HTML tags are not balanced within their corresponding Liquid logic blocks or content blocks, the parser may modify the underlying HTML in unexpected ways. This can result in:

- Newlines from Liquid rendering in some mail clients
- Odd spacing from `<p>` tags added to the email body
- `<head>` tag content moved to the preheader
- Inconsistent rendering across mobile operating systems
- AMP-specific code removed from AMP email bodies, causing validation failures
- Broken links when many different query parameters or media queries are used

**Balance HTML within Liquid blocks**

Ensure that all HTML tags open and close within their corresponding Liquid logic block or content block. This prevents the internal parser from interpreting the HTML as invalid and modifying it.

**Unbalanced example:**

```liquid
<img src={% if ${language} == 'en' %}"https://example.com/images/banner-en.png" style="width: 100%"{% elsif ${language} == 'de' %}"https://example.com/images/banner-de.png"{% else %}"https://example.com/images/banner-default.png" {% endif %} />
```

In this example, the opening `<img` tag starts outside of any Liquid block, and different parts of the tag's attributes are split across Liquid conditional statements. This confuses the parser.

**Balanced example:**

```liquid
{% if ${language} == 'en' %}
  <img src="https://example.com/images/banner-en.png" style="width: 100%;" />
{% elsif ${language} == 'de' %}
  <img src="https://example.com/images/banner-de.png" style="width: 100%;" />
{% else %}
  <img src="https://example.com/images/banner-default.png" style="width: 100%;" />
{% endif %}
```

In the balanced version, each Liquid branch contains a complete, self-contained `<img>` tag. This approach ensures the parser processes each branch correctly.

**Additional fixes**

If you're experiencing rendering issues with media queries or many query parameters, try turning off CSS inlining in your email settings. This can resolve conflicts between the HTML parser and complex CSS rules.

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
