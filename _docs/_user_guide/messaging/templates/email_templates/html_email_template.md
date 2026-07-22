---
nav_title: Upload an HTML email template
article_title: Upload an HTML Email Template
page_order: 2
description: "This reference article covers how to create, manage, and troubleshoot an HTML email template using the Braze dashboard."
tool:
  - Templates
channel:
  - email

---

# Upload an HTML email template

> The Braze dashboard allows you to upload your very own HTML email templates and save them for later use in campaigns. You can also [create an email template]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template) using our editor.

## Requirements {#upload-requirements}

First, you'll need to create your HTML email template. This must be a ZIP file that contains the following:

* A single HTML file—the body of your email
* A folder of images that are referenced in the HTML file
* Less than 50 image files
* Be less than 5&nbsp;MB

## Uploading your template

### Step 1: Go to the email template editor

Go to **Content** > **Email**. Select **Create email template**.

### Step 2: Add template details

Provide a template name. Optionally, add a description, teams, and tags.

### Step 3: Upload your template

In the **Template content** section, select **Upload file**. Select your template from your computer. Refer to the [Requirements](#upload-requirements) section to ensure your template meets the upload requirements.

### Step 4: Finish and save your template

Be sure to save your template by selecting **Save template**. You're now ready to use this template in any campaign or Canvas you choose.

{% alert note %}
If you make any edits to an existing template, those changes will not be reflected in campaigns that were created using previous versions of that template.
{% endalert %}

## Using your templates in API campaigns {#api_for_upload_email_templates}

To use your email for an API campaign, you need the `email_template_id`, which can be found at the bottom of any email template created in Braze.

![API Identifier section of an HTML email template.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:50%;"}

## Managing email templates

You can [duplicate]({{site.baseurl}}/user_guide/messaging/templates/managing_templates) and [archive]({{site.baseurl}}/user_guide/messaging/templates/managing_templates) email templates! Learn more about creating and managing templates and creative content in [Templates]({{site.baseurl}}/user_guide/messaging/templates).

## Troubleshooting

### Upload errors

There are several email error messages you may receive when uploading an HTML template file. If you receive an error, refer to the following table for common issues and their recommended fixes:

| Error | Fix |
|------|---|
|`.zip over 5&nbsp;MB`| Reduce your file size and try uploading again.|
|`.zip corrupt`| Inspect your file and try uploading again. |
|`Missing HTML`| Add the HTML file to your ZIP file and try uploading again.|
|`Multiple HTML`| Remove one of the HTML files and try uploading again.|
|`Images over 5&nbsp;MB`| Reduce the number of images and try uploading again. |
|`Extra Images`| There may be additional images in your file that are not referenced in your HTML file. This does not cause a fail error, but the extra images are discarded. If those images were supposed to be referenced in the HTML file, then check the content, correct any errors, and try uploading again.|
|`Missing Images`| If there are images referenced in your HTML file, but those images are not included in the image folder of the ZIP file, you receive a file error. Inspect your file and correct any errors (like misspellings), or add the missing images to your ZIP file and try uploading again.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

Note that when downloading the files for HTML campaigns, Canvas steps with email messages, or templates on a Windows machine, the `|` (pipe character) is not supported, so you may need to use a different application to extract the download contents from the ZIP file.

### Email not rendering properly

If your email doesn't render properly, check each content block to make sure there are no additional `<!doctype>` headers.

If there is a `<!doctype>` header in the HTML template itself along with an HTML doctype in one of the content blocks, the email doesn't render properly. Treat content blocks as additional HTML being added to the email template, not a brand new HTML doctype. This means the content block shouldn't contain extra body tags or any of the template HTML code.


## Frequently asked questions

For answers to frequently asked questions about email templates, check out our [email and link templates FAQ]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq) page.


