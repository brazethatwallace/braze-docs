---
nav_title: FAQ
article_title: Drag-and-Drop Editor FAQ
alias: "/dnd/faq/"
channel: email
page_order: 5
description: "Frequently asked questions about the drag-and-drop email editor."
tool: 
  - Campaigns
  - Canvas
  
---

# Frequently asked questions

> This page provides answers to some frequently asked questions related to the drag-and-drop editor for email.

## Can I preview how my email appears in dark mode?

Yes. Go to the **Preview and Test** section of the drag-and-drop editor and turn on **Dark mode**. We recommend also previewing and testing your emails across different user platforms and using transparent images for row background images when possible.

## How should I design emails for dark mode and light mode?

Emails do not need to be sent in separate light and dark layouts because email clients and devices can apply their own dark theme. However, this may invert colors or hide backgrounds if explicit colors are not set on the outer container and major sections. To prevent this, we recommend setting solid background colors so your message reads clearly in both dark and light mode.

Some email clients replace background images or invert low-contrast text in dark mode, so body copy can look missing or render differently between clients (for example, Gmail on iOS versus Android). Set `background-color` on the outer container and major sections instead of relying on background images alone for light backgrounds.

## Why doesn't my custom font appear in drag-and-drop email preview?

Custom fonts load in the editor preview when a **Text** block in the message references the font. If the preview still shows a fallback font after you configure a custom font in **Drag-and-Drop Email Editor** settings, add a **Text** block that uses that font so the editor loads it for preview. Confirm that cross-origin resource sharing (CORS) is enabled on your font file. Recheck **Preview and Test** and your target email clients before you send. For setup steps, see [Custom font]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings/#custom-font).

## How can I carry over text formatting when I copy and paste from another application?

Different text editors and applications have their own ways of handling text formatting that may not be universally recognized. When you copy and paste formatted text from outside Braze into the drag-and-drop editor, the rich formatting may not carry over.

To paste text without rich formatting, use one of these methods:
- On Mac: Press <kbd>cmd</kbd>+<kbd>shift</kbd>+<kbd>V</kbd> instead of <kbd>cmd</kbd>+<kbd>V</kbd>
- On Windows: Press <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>V</kbd> instead of <kbd>ctrl</kbd>+<kbd>V</kbd>
- Right-click within the editor and select **Paste and Match Style**

## How can I change the email padding on mobile without updating the padding in the web view?

You cannot edit the padding for mobile and web views exclusively, so any edits are reflected in both views. However, you can add CSS logic in the HTML editor that sets the padding based on different screen sizes. This isn't supported in the drag-and-drop editor, so you can export the HTML file and use the HTML editor instead.

## How can I optimize a row of buttons to remain horizontal on desktop and mobile?

When building an email using the drag-and-drop editor, if you create a horizontal row of call-to-action buttons, you may find that the buttons are changed to a vertical orientation on mobile. 

To retain the same format across device sizes, we recommend creating a separate row with CTA buttons that have padding optimized for mobile and are set to hide the row on a desktop device. Having two separate rows means that you can set the desired padding for the best text rendering on desktop and mobile devices.

## Can I adjust the row height in the drag-and-drop editor?

The row height auto-adjusts to the content. As an alternative, we recommend that you:
1. Add a divider block.
2. Click the toggle to turn on its transparency.
3. Adjust the height.

## Is it possible to build layers in the editor? Can I add a background image, layer on an image, and add a text layer over that?

The drag-and-drop editor currently supports two layers. You can set a row background image and customize background colors.

## Can I save my drag-and-drop email as a template after I build it within my campaign or Canvas?

No. You can't save a drag-and-drop email from a campaign or Canvas as a drag-and-drop **Email Template** in **Templates** > **Email Templates**. Recreate the layout under **Templates** > **Email Templates**, or start from a saved template next time. For instructions, see [Create an email template]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template).

If you need a reusable HTML template instead, select **Download file** while editing the drag-and-drop body, open the HTML from the ZIP, and paste the markup into an [HTML email template]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template) using the HTML code editor. Recheck Liquid, links, and hosted assets afterward.

For more information about where templates live, see [Templates and Media]({{site.baseurl}}/user_guide/messaging/templates).

## Why can't I change a button's fill color in the drag-and-drop editor?

Page-level styles can override message-level styles. If updating **Fill** on a button or block does nothing, try the following:
1. Open [email global style settings]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings) and select **Reset to default** on the conflicting page style so the message-level color can apply.
2. Set the color again on the block.

## Can I add email attachments to the drag-and-drop editor?

Yes. You can add attachments to your email message by going to **Sending Settings** > **Advanced**.

## How do I download the raw HTML for a drag-and-drop email?

1. Open your campaign or Canvas and edit the email message.
2. Select **Edit email body** to open the drag-and-drop editor.
3. Select **Download file** (bottom of the editor). Extract the archive to access the generated HTML.

You can paste that HTML into an [HTML block]({{site.baseurl}}/user_guide/channels/email/drag_and_drop#content) or the HTML editor when you need low-level edits—for example, to [turn off click tracking for specific links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links#turning-off-click-tracking-on-a-link-to-link-basis).

## Why is my drag-and-drop layout breaking?

Layout issues are often caused by **custom HTML or CSS** that conflicts with the markup the editor generates. Try these steps:

1. Remove or isolate custom HTML blocks to see if the problem disappears.
2. Check **Drag-and-Drop Email Editor** settings for custom fonts that may not load in all clients.
3. In **Row Properties**, review column padding and widths.
4. When you add custom HTML, prefer table-based layouts, fluid images, and total table widths that fit your email width—fixed pixel images or non-table structures often break in Outlook and other clients.

## Why doesn't my Content Block render in email preview?

If a Content Block doesn't render in email preview, check for unclosed anchor tags. For Connected Content URLs, use the `replace` filter to convert double-encoded ampersands (`&amp;amp;`) to a single encoded ampersand (`&amp;`). Limit Content Block nesting to two levels.

## Why does a drag-and-drop Content Block lose mobile styling inside a Custom Code block?

When you place a drag-and-drop **Content Block** inside a **Custom Code** (HTML) block, mobile-specific styling and alignment from the Content Block may not apply in the sent message. When both the Content Block and the template use the drag-and-drop editor, add the Content Block as its own row instead of nesting it inside Custom Code.

When you stack multiple Content Blocks, use a separate row for each block instead of placing several blocks in a single row.

## Why is the drag-and-drop editor ignoring alignment settings?

If the drag-and-drop editor ignores alignment settings, remove custom CSS or HTML blocks, remove custom fonts, check for CSS conflicts, and avoid duplicating row blocks. Contact Braze Support if the issue persists.

## Why does my chosen hex color code not match the font in my email?

If you're using a Content Block, the block may have its own font color setting. Select the text block inside the Content Block and clear any local **Font color** override so your hex color from global or paragraph styling can apply.
