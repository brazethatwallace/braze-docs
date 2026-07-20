---
nav_title: NiftyImages
article_title: NiftyImages
description: "Learn how to connect NiftyImages to Braze to create personalized dynamic visuals, sync contact properties, and publish assets as reusable Content Blocks."
alias: /partners/niftyimages/
page_type: partner
search_tag: Partner
---

# NiftyImages

> [NiftyImages](https://niftyimages.com) helps Braze customers create personalized, real-time visual content for email, mobile, and in-app messaging. By connecting live customer, product, and business data to dynamic images and content, brands can deliver timely, relevant experiences such as countdown timers, personalized recommendations, localized messaging, inventory updates, and promotional offers that drive engagement and conversions.

_This integration is maintained by NiftyImages._

## About the integration

The NiftyImages integration for Braze helps you create personalized, dynamic visuals using Braze contact data. Teams can build assets like personalized images, countdown timers, maps, calendars, loyalty visuals, and more, then publish them as reusable Braze [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/) for use across campaigns and Canvases. This saves time, reduces errors, and simplifies personalized content management.

## Use cases

You can use NiftyImages to:

- **Personalize images:** Create images that include each customer's name, loyalty status, reward balance, location, product preference, membership tier, account details, or other Braze contact properties.
- **Add countdown timers:** Add real-time countdown timers for sales, product drops, events, limited-time offers, appointments, onboarding deadlines, and personalized expiration dates.
- **Show dynamic maps:** Show the closest store, event location, service area, dealer, club, branch, or pickup location based on customer location data or Braze contact properties.
- **Display calendars:** Display personalized dates, events, appointments, renewal periods, campaign moments, or customer milestones directly inside campaign visuals.
- **Run live polls:** Add interactive polls to campaigns and display live updating results after customers vote.
- **Create scratch-offs:** Create gamified scratch-off experiences that reveal a personalized reward, discount, offer, image, or message.
- **Visualize loyalty data:** Turn customer data into progress bars, account summaries, loyalty visuals, charts, and graphs that are personalized to each recipient.
- **Apply rule-based content:** Display different visuals based on time, location, device, customer data, audience segment, or campaign logic.
- **Reuse dynamic content:** Publish completed NiftyImages assets into Braze Content Blocks so teams can reuse them across marketing emails, templates, campaigns, and shared brand assets.

## Prerequisites

Before you begin, confirm you have the following:

| Requirements | Description |
| ------------ | ----------- |
| NiftyImages account | A [NiftyImages account](https://niftyimages.com/Signup) is required to create and manage personalized images, timers, maps, calendars, scratch-offs, charts, and other dynamic visuals. |
| Braze account | A Braze account is required to use NiftyImages within Braze campaigns, Canvases, email templates, and messaging channels. |
| Braze REST API key | A Braze REST API key with `custom_attributes.get` and `content_blocks.create` permissions.<br><br>This can be created in the Braze dashboard from **Settings** > **APIs and Identifiers**. |
| Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/api/basics/#endpoints). Your endpoint depends on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

Connect your Braze account in NiftyImages to sync contact properties and publish assets to Braze Content Blocks.

### Step 1: Open integrations in NiftyImages

1. In NiftyImages, go to **Settings** > **Integrations**.
2. Select **Braze**.
3. Select **Connect Braze**.

### Step 2: Create your Braze REST API key

1. In Braze, go to **Settings** > **APIs and Identifiers**.
2. Create or select a REST API key for the NiftyImages integration.
3. Under **Custom Attributes**, select `custom_attributes.get`.
4. Under **Content Blocks**, select `content_blocks.create`.
5. Save the API key, then copy the REST API key and your [REST endpoint]({{site.baseurl}}/api/basics/#endpoints).

### Step 3: Connect your Braze account in NiftyImages

1. Return to the Braze integration screen in NiftyImages.
2. Paste the Braze REST API key.
3. Enter your Braze REST endpoint.
4. Confirm the connection.
5. Verify your Braze account appears under **Connected Braze accounts** with an **Active** or **Connected** status.

You can connect multiple Braze accounts if needed, which is useful for agencies, multi-brand teams, or organizations managing several Braze instances.

## Customize assets in NiftyImages

After you connect Braze, use Contact Variable Sync and Content Block publishing to manage personalized visuals.

### Use Contact Variable Sync

Contact Variable Sync lets you use existing Braze contact properties directly inside NiftyImages without manually typing or recreating merge tags.

1. Create or edit a personalized image or other NiftyImages asset.
2. Open the merge tag or personalization picker.
3. Select **Pick from connected integrations**, then choose the Braze properties you want to use.
4. Add those values to text, image, timer, map, chart, calendar, or dynamic content layers.
5. Save the image.

Saved images that use Braze variables automatically include those personalization values in the NiftyImages image URL.

### Publish to Braze Content Blocks

1. Finish your NiftyImages asset.
2. Select **Send to Braze**.

## Use NiftyImages in Braze

Use published Content Blocks in Braze email templates, campaigns, and Canvases.

### Add a NiftyImages asset to a Braze email

1. Open an email template, campaign, or Canvas email message in Braze.
2. In the message editor, open the personalization menu and select **Content Blocks** as the personalization type.
3. Select the NiftyImages Content Block you published from NiftyImages.

### Reuse NiftyImages assets across Braze

1. Use the published Content Block across marketing emails, email templates, campaigns, shared brand assets, and automated flows.
2. When a NiftyImages asset uses dynamic variables, Braze passes the contact values based on the message and channel.
3. Update the source asset in NiftyImages when you need creative changes.

### Disconnect a Braze account

1. Return to **Settings** > **Integrations** in NiftyImages.
2. Open the Braze connection page.
3. Select the remove or disconnect icon for the account you want to remove.
4. Confirm the disconnection.

## Considerations

- **REST API permissions:** The Braze REST API key must include `custom_attributes.get` for contact property sync and `content_blocks.create` for publishing assets into Braze Content Blocks.
- **Contact property availability:** Only contact properties available to the connected Braze account can be synced into NiftyImages.
- **Fallback values:** Use fallback values when building personalized visuals so every customer sees a polished image even when a contact property is missing.
- **Reusable Content Blocks:** Publishing to Braze Content Blocks helps teams avoid manual HTML copy and paste, reduce merge tag errors, and reuse assets across campaigns and templates.
- **Multiple Braze accounts:** NiftyImages supports multiple connected Braze accounts, which is helpful for agencies, multi-brand teams, and teams managing multiple Braze instances.
- **Testing:** Test the final Braze message with sample customer profiles before you launch a campaign or Canvas.

## Troubleshooting

Refer to the following table if you experience issues with the NiftyImages integration.

| Issue | Resolution |
| ----- | ---------- |
| Braze account doesn't connect | Confirm the REST API key is valid, the REST endpoint is correct, and the key includes the required permissions. |
| Braze contact properties don't appear in NiftyImages | Confirm the API key includes `custom_attributes.get`. Then refresh the Braze connection inside NiftyImages. |
| The asset doesn't publish to Braze Content Blocks | Confirm the API key includes `content_blocks.create` and that the connected Braze account allows Content Block creation. |
| Personalization doesn't show correctly | Check that the selected Braze contact property contains a value for the test user. Add fallback values in NiftyImages where needed. |
| The image doesn't render in Braze | Confirm the NiftyImages asset is saved, active, and published correctly. Send a Braze test message to verify the image in the intended channel. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }
