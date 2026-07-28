---
nav_title: Media library
article_title: Media library
page_order: 2
page_type: reference
description: "This reference article covers the media library. Here, you can learn how to manage your assets in a single, centralized location, generate images using AI, access media in your message composer."
tool: Media

---

# Media library

> The media library allows you to manage your assets in a single, centralized location. 

## Prerequisites

| Requirements | Description |
|---|---|
| "View Media Library Assets" permission | View media library assets |
| "Edit Media Library Assets" permission | Create and update media library assets |
| "Delete Media Library Assets" permission | Remove media library assets from the UI. Deleted assets remain hosted by Braze to prevent breaking messages that reference them. To permanently delete an asset, contact Braze Support. |
| "Replace Media Library Assets" permission | Replace the file of an existing media library asset while keeping its URL and asset ID stable |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Media library permissions" }

For more information, see [User permissions]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

## Media library versus CDN

Using the media library instead of a Content Delivery Network (CDN) provides better caching and performance for in-app messages. All media library assets found in an in-app message will be pre-cached for faster display and will be available for offline display. Additionally, the media library is integrated with Braze composers, allowing marketers to select or tag images instead of copying and pasting image URLs.

## Accessing the media library

Within the media library, you can see the asset type, size, dimensions, URL, the date it was added to the library, and other information. To access your Braze media library, go to **Content** > **Media Library**. Here, you can:

* Upload multiple images at one time
* Upload Virtual Contact Files (.vcf)
* Upload video files for use in WhatsApp messages
* Upload a folder with your images (up to 50 images)
* [Generate an image using AI](#generate-ai) and store it in the media library
* Crop an existing image to create the right ratio for your messages
* Replace the file of an existing asset while keeping its URL stable
* Add tags or teams to help further organize your images
* Search by tags or teams in the media library grid
* Drag and drop images or folders to be uploaded
* Delete images

![Media Library page that includes an "Upload To Library" section to drag and drop or upload files. There is also a list of uploaded content in the media library.]({% image_buster /assets/img_archive/media_library_main.png %})

Later, when drafting a message in Braze, you can pull in your images from the media library.

![Two common ways of accessing the media library depending on the message composer. One shows the email Drag and Drop Editor with the title "Images and GIFs" and a button to "Add from Media Library". The other shows the standard editors, such as push and in-app messages, with the title "Media" and a button to "Add Image".]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} For more help with the media library, check out our [Media library FAQ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/faq). {% endalert %}

## ZIP file uploads {#zip-file-uploads}

When you upload a ZIP file to the media library, all files must be in the root of the ZIP folder—do not include subdirectories.

This applies to every file in the archive—including font files (`.ttf`, `.woff`, `.otf`, `.woff2`), HTML, CSS, JavaScript, and images. Place each file in the root of the ZIP alongside the others.

Alternatively, upload assets individually to the media library without zipping them.

## Replace a file

You can replace the file of an existing asset in the media library while keeping its URL and asset ID stable. Because the URL doesn't change, any message or campaign that references that asset—including already-sent emails—automatically reflects the updated file. This is useful when you want to update a shared asset (such as a logo) in one place rather than updating every campaign individually.

To replace an asset, you must have the "Replace Media Library Assets" permission:

1. Go to **Content** > **Media Library**.
2. Select the asset you want to replace.
3. In the modal, select **Replace file**.
4. Upload the replacement file.

![Media library edit modal showing the Replace file, Crop image, and Delete buttons for an asset.]({% image_buster /assets/img_archive/media_library_replace_file.png %}){: style="max-width:60%;border:none"}

### Requirements and limitations

- The replacement file must have the same file extension as the original. For example, you can't replace a `.png` asset with a `.jpg` file.
- Video assets cannot be replaced.
- After replacement, the updated file may take some time to display for all consumers due to CDN caching.

### Channels with processed image copies

Some channels create an optimized copy of the image when the message is set up, resulting in a separate URL. Replacing the original media library asset does not update what consumers see for messages created using those channels, including in-app messages, Content Cards, push notifications, and banners.

You can also replace an asset programmatically using the [`PUT /media_library/replace_file`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/replace_file) endpoint.

## Image specifications

All images uploaded to the media library must be less than 5&nbsp;MB. Supported file types are PNG, JPEG, GIF, SVG, and WebP. For recommended image sizes and specifications by messaging channel, refer to [Image specifications]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications).

{% alert important %}
GIFs with very elongated shapes (for example, 3000 x 2 pixels) or 300 or more frames may fail to upload, even if the total file size is small.
{% endalert %}

## Generating images with BrazeAI<sup>TM</sup> {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
Before using this feature, review [how your data is used and sent to OpenAI]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#data-privacy-and-security).
{% endalert %}

If you don't see **AI Image Generator** on the **Media Library** page, confirm you have **Edit Media Library Assets** permission. If the option is still missing, contact your Braze customer team to confirm your workspace has access to BrazeAI image generation. If generation fails, review the [OpenAI content policy]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#data-privacy-and-security).

