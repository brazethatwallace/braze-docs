---
nav_title: Bynder
article_title: Bynder
description: "This reference article outlines the partnership between Braze and Bynder, a digital asset management (DAM) platform that lets you search for and insert approved asset URLs into Braze campaigns and Canvases through the Universal Compact View Chrome extension."
alias: /partners/bynder/
page_type: partner
search_tag: Partner
---

# Bynder

> [Bynder](https://www.bynder.com) is a digital asset management (DAM) platform that helps customers create, manage, find, and distribute approved digital assets (images, videos, and other creative) from a single source of truth. When integrated with Braze, Bynder's Universal Compact View (UCV) Google Chrome extension lets marketers search for and select Bynder assets without leaving the Braze dashboard. Insert links to those assets directly into campaigns and Canvases.

_This integration is maintained by Bynder._

## About this integration

Connecting Bynder to Braze through the UCV Chrome extension gives marketers access to their Bynder asset library within the Braze content editor. Open the Universal Compact View as an overlay on any browser tab, including the Braze dashboard. Search or filter for the right creative, then paste the asset's URL into your campaign.

This keeps Braze campaigns aligned with Bynder's single source of truth: the correct permissions, the most current file version, and the correct usage rights.

## Use cases

- Marketers building an email, in-app message, or Content Block in Braze can insert hero images, banners, or promotional video links sourced directly from Bynder so campaigns use the latest approved version of an asset.
- Campaign managers can use the Universal Compact View's search and filter bar to locate approved regional or localized creative for a specific audience segment before adding it to a Canvas step.
- Creative teams can apply Bynder's Dynamic Asset Transformation to resize or reformat an asset for a specific channel before copying the link into Braze. For example, use a compact crop for a push notification or a full-size banner for email.

## Prerequisites

Before you start, you need the following:

| Requirement | Description |
| --- | --- |
| A Bynder account | A Bynder account with access to the DAM assets you want to reference in Braze. |
| Bynder Universal Compact View (UCV) Chrome extension | Installed from the Chrome Web Store and connected to your Bynder portal. Available for Google Chrome only. |
| Public assets and derivatives | Any asset, and the specific derivative you plan to link to, must be marked public in Bynder so its URL resolves correctly for message recipients. |
| A Braze account | Access to the messaging channel (email, Content Block, in-app message, Canvas, and so on) where the asset is used. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

### Step 1: Install and connect the Bynder UCV Chrome extension

1. Go to the [Bynder UCV extension](https://chromewebstore.google.com/detail/bynders-universal-compact/ilghhphnbdblpbdhmbdfiaidganphema) in the Chrome Web Store.
2. Click **Add to Chrome**, review the requested permissions, then click **Add extension**.
3. From the Chrome toolbar, select the Bynder UCV icon (pin it to the toolbar first if it isn't already visible).
4. Enter your Bynder portal domain (without `https://`), then click **Connect**.
5. In the window that opens, log in to your Bynder portal with your usual credentials.

### Step 2: Search for and select a Bynder asset

1. With the extension connected, open the Universal Compact View from any browser tab, including your Braze dashboard.
2. Use the smart filter and search bar to locate the image, video, document, or audio asset you need.
3. Select the asset, then select the derivative (or the original file, if it's public) you want to use.
4. Click **Add Asset** to copy the selected asset's URL to your clipboard.

### Step 3: Add the asset URL to your Braze campaign

1. In Braze, open the email, Content Block, in-app message, or Canvas step where you want to add the asset.
2. Paste the copied Bynder asset URL into the relevant field. For example, use an `<img src="">` tag or a Content Block's image URL field.

   Example image URL:

   ```html
   <img src="https://your-portal.bynder.com/m/abcdef123456/original/campaign-banner.jpg" alt="Summer Campaign">
   ```

{: start="3"}
3. Save and preview your message to confirm the asset renders as expected.

## Tips

### Apply Dynamic Asset Transformations before copying the URL

Within the Universal Compact View, use the available transformation options to resize, crop, or reformat an asset for the channel you're targeting. This avoids uploading separate cropped versions to Bynder.

### Generate channel-specific derivative URLs

Each transformation or derivative produces its own distinct URL. Generate one version sized for email, another for push, and another for in-app messages, then paste each into the corresponding Braze channel or Canvas step.

### Reuse one asset URL across channels

Because a pasted link points back to a specific asset and derivative in Bynder, the same URL format can be reused across email, Content Blocks, in-app messages, and Canvas steps. This keeps creative consistent everywhere it's used in a campaign.

### Update the source asset without editing your campaigns

If the underlying file in Bynder is replaced while keeping the same public asset and derivative settings, any live Braze message referencing that URL automatically reflects the update. You don't need to edit the campaign itself.

## Considerations

- The Bynder UCV Chrome extension is available only for Google Chrome. In other browsers, copy asset URLs directly from the full Bynder portal.
- Only assets (and the specific derivatives being linked to) that are marked public in Bynder resolve when pasted into Braze. Private assets return an access error to recipients.
- If pop-up windows are not allowed or the portal is already open in another tab, the login window may not open correctly. Before connecting, confirm pop-up windows are allowed and close any other tab where the portal is open.
- Access within the extension follows the company user's existing permissions in the Bynder DAM, so they see and can select only assets they're already authorized to access.

## Troubleshooting

| Issue | Resolution |
| --- | --- |
| The extension icon isn't visible | Pin the Bynder UCV extension to the Chrome toolbar from the Extensions menu. |
| **Connect** doesn't open a login window | Confirm Chrome pop-ups are allowed for your Bynder portal domain, and close any other tab where the portal is already open. |
| Asset URL doesn't render in Braze | Confirm that the asset and the specific derivative used are marked public in the Bynder portal. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

For more information, see Bynder's [Universal Compact View documentation](https://support.bynder.com/hc/en-us/sections/16936397091858-Universal-Compact-View-UCV) or contact Bynder Support.
