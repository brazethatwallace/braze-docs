---
nav_title: Link templates
article_title: Link Templates
page_order: 4
description: "This article covers how to create different types of link templates in your emails."
tool:
  - Templates
channel:
  - email

---

# Link templates

> With link templates, you can create dynamic and reusable links for your email campaigns by appending parameters or prepending URLs. This can create consistency in the URLs across your campaigns and messages. 

{% alert note %}
Link templates are an optional feature. If **Email Link Templates** is missing from the **Templates** section, contact your account manager to turn on the feature.
{% endalert %}

## How it works

Link templates are most often used in these following use cases:

- Appending Google Analytics query parameters to all links in a given email message
- Prepending a URL to all links in a given email message

Let's say you're running a promotional email campaign for a new product launch. You can use a link template that directs users to the product page and personalize the link to include your user's name or a specific promotional code. This can allow you to track how many users have clicked on the link and have made a purchase. This way, you can create consistency across your links and better track your analytics.

## Creating a link template

You can create an unlimited number of link templates to support your various needs. To create a link template, do the following:

1. Go to **Content** > **Email Link**.
2. Select **Create email link template**.
3. Give your link template a name.
4. (Optional) Add a description, team, or tag to add details about the link template.
5. (Optional) Select the toggle to automatically add the link template to links in email campaigns and Canvases. This applies when adding a new link to any new or existing email.

There are two types of link templates you can create:

- [Link template that inserts before a URL](#prepend-link-template)
- [Link template that inserts after a URL](#append-link-template)

When using link templates and [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/), Liquid must only be added within the body tag to ensure consistent rendering.

### Prepend: Create a link template that inserts before a URL {#prepend-link-template}

To add a string or URL before the links in your email message, do the following:

1. Create a new link template.
2. Set the **Template Position** to **Before URL**. 
3. Enter a string that will always get prepended to your URL. 

The **Template preview** is provided to give you an example of how the link template will be inserted before a URL.

![Template Position, Prepend URL, and Template Preview fields for the link template insertion process before a URL.]({% image_buster /assets/img_archive/link_template_preappend.png %}){: style="max-width:90%;"}

### Append: Create a link template that inserts after a URL {#append-link-template}

If you want to add query parameters after a URL in your email message:

1. Create a new link template.
2. Set the **Template Position** to **After URL**. 
3. Enter the query parameters (`value=example`) to the end of each URL. You can have multiple parameters appended to the end of a URL.

![Template Position, Query Parameters, and Template Preview fields for the link template insertion process after a URL.]({% image_buster /assets/img_archive/link_template_postappend.png %}){: style="max-width:90%;"}

## Using link templates in email campaigns

After you set up your link templates, you can apply them in your email.

To apply a link template in the HTML editor or the drag-and-drop editor, follow these steps:

{% alert important %}
To access the **Link Management** tab in the updated HTML editor or the drag-and-drop editor, you must have link aliasing turned on. To turn on link aliasing, contact your account manager. For more information, see [Link aliasing]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing/).
{% endalert %}

- **Updated HTML editor:** On the **Content** tab, select **Link Management**, select **Add a Link Template**, choose your link template, and then select **Add**.
- **Drag-and-drop editor:** On the **Content** tab, select **Link Management**, select **Add a Link Template**, choose your link template, and then select **Add**.

![Link Management tab in the drag-and-drop editor with an example list of link templates.]({% image_buster /assets/img_archive/link_template_messagecomposer2.png %})

{% alert note %}
Link templates aren't applied to plain text. This means Currents may show clicks that don't include the parameters from the link templates as those clicks may come from the plain text version of the email.
{% endalert %}

As you add link templates in the **Link Management** tab, scroll to the right to view the templates. If existing links within an email already have a link template added, newly added links also have the link template added by default.

{% alert tip %}
When including links in your message, be sure to start the URLs with `http://` or `https://`.
{% endalert %}

## Managing link templates

You can also [duplicate]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/) link templates. Learn more about creating and managing templates and creative content in [Templates & Media]({{site.baseurl}}/user_guide/messaging/templates/).

{% alert important %}
Archiving templates is not currently available for link templates.
{% endalert %}

## Troubleshooting

### Missing UTM parameters

Link templates aren't applied to links in standard HTML comments (`<!-- ... -->`). For Outlook conditional comments (for example, `<!--[if mso]>`), link templates are applied when link aliasing is enabled for your workspace. Workspaces without link aliasing enabled still skip conditional comments.

### UTM parameters aren't displaying in each link, but do appear when you view the email in a browser

This can happen when the URL path in your email doesn't match the full path you intend (for example, a shortened or different path than the website's full URL).

- **What to check:** The `href` in the email includes the complete path to the page (not only a partial path that relies on redirects).
- **What to expect:** If the path in the email is incomplete or different, UTM parameters from your link template may not be applied to that link when it's clicked, even though the website might still redirect the visitor to the right page.

For example, if the full link is `https://www.somewebsite.com/women/designer/johnjane` but the email uses `https://www.somewebsite.com/designer/johnjane`, it is expected that UTM parameters won't be added to the email link.

### UTM parameters aren't appending for a link rendered from a Liquid tag

When applying link templates, Braze parses each URL to determine where to append parameters. If a Liquid tag renders a URL that cannot be parsed as a valid URI, the link template is silently skipped. Check that your Liquid output produces a well-formed URL. Test by previewing the message for a specific user and verifying the rendered URL is valid. If the URL includes Liquid variables in the path or query string, confirm the output doesn't contain invalid characters or broken encoding.

### UTM values don't populate compared to the preview in a test send

When test sending link templates, {% raw %}`{{${user_id}}}`{% endraw %} does not get rendered. Instead, duplicate the campaign and set it to target your internal users' email or `external_id` and launch the campaign to verify that all UTM parameters from the link template are populated.

## Frequently asked questions

For answers to frequently asked questions about link templates, check out our [Templates FAQ]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq/) page.

