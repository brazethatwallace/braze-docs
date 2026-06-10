---
nav_title: Lokalise
article_title: Lokalise
description: "This reference article outlines the partnership between Braze and Lokalise, a translation management service for agile teams."
alias: /partners/lokalise/
page_type: partner
search_tag: Partner

---

# Lokalise

> [Lokalise](https://lokalise.com) is a translation management service for agile teams.

_This integration is maintained by Lokalise._

## About the integration

Lokalise offers two integration options for Braze:

- **Multi-language integration (recommended)**: Uses Braze's [Multi-Language Composition API]({{site.baseurl}}/api/endpoints/translations/) to provide a direct two-way sync between Lokalise and Braze. This integration works with localized message variants for Campaigns, Canvases, and Email Templates, and supports pre-launch and post-launch workflows for Push, Email, and In-App Messages.
- **Connected Content integration (legacy)**: Uses Braze Connected Content to insert translated content based on user language settings.

This article covers setup for both integrations.

## Multi-language integration (recommended)

The Multi-language integration uses Braze's Multi-Language Composition API to provide a streamlined, automated way to manage multilingual Braze content inside Lokalise.

### Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Lokalise account | A Lokalise account is required to take advantage of this partnership. |
| Lokalise translation project | Create a Lokalise project with the **Marketing and support** type and choose **Braze** as the **Content integration**. |
| Braze multi-language settings | [Multi-language support]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings/) must be enabled in your Braze workspace. |
| Braze REST API key | A Braze REST API key with permissions to read and update Campaigns, Canvases, and Email Templates. You can create one in the Braze dashboard from **Settings** > **API Keys**. |
| Braze server region | Your [Braze server region]({{site.baseurl}}/api/basics/#endpoints) (for example, US-01, EU-01). You can find this in the Braze dashboard. |
| Translation tags in Braze content | Messages must use [translation tags]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) to identify translatable content. Wrap each translatable block in {% raw %}`{% translation ID %}...{% endtranslation %}`{% endraw %} tags with a unique ID. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

### Setup and usage

For detailed instructions on connecting the Braze Multi-language integration in Lokalise, importing content, translating, and exporting translations back to Braze, refer to [Lokalise's Braze integration documentation](https://docs.lokalise.com/en/articles/13654162-braze).

The integration supports:
- Direct two-way sync between Lokalise and Braze (no manual file handling)
- Localized message variants for Campaigns, Canvases, and Email Templates
- Pre-launch and post-launch translation workflows

{% alert note %}
Only content configured for multilingual use in Braze and wrapped in translation tags is available for import to Lokalise. Language codes must match exactly in both Braze and Lokalise for translations to sync correctly.
{% endalert %}

## Connected Content integration (legacy)

The legacy integration uses Braze Connected Content to insert translated content based on user language settings.

### Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Lokalise account | A Lokalise account is required to take advantage of this partnership. |
| Lokalise translation project | Create a Lokalise project with the **Software Localization** project type. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

### Create a new Lokalise project

To create a new translation project, log in to Lokalise and select **New Project**. Next, name your project, choose a **Base Language** (the language you will translate from), add one or more **Target Languages**, and choose **Software Localization** project type. When you are ready, click **Proceed**.

### Integration

In Lokalise, you will create a translation key for each of the Connected Content variables you define in Braze. When the translations are ready, you can generate one JSON file per language and publish it on the URLs that will serve your Connected Content.

#### Step 1: Configure user languages

If you haven't done so already, open the Braze dashboard and proceed to **Users > User import**. Here, you can import your users. When preparing a CSV file for importing, make sure to include a language column with users' languages. This language field will be used later when displaying translations. 

{% alert important %}
Language codes used must match across both Braze and Lokalise.
{% endalert %}

#### Step 2: Prepare your translations on Lokalise

Next, to prepare your translations on Lokalise, you'll need to manually create the translation keys with the same name you're using on Braze Connected Content variables. 

For example, let's create a simple translation key, `description`:
1. Open your Lokalise project, click **Add Key**, enter "description" in the **Key** field.
2. Type "Demo description" in the **Base Language Value** field.
3. Add "Web" in the **Platforms** dropdown. 
4. When you are ready, click **Save**.

![]({% image_buster /assets/img/lokalise/1_add_key.png %}){: style="max-width:60%"}

Your translation key should appear in the project editor:

![]({% image_buster /assets/img/lokalise/2_translation_key_added.png %}){: style="max-width:90%"}

##### Known issues

- Your keys must be assigned to the **Web** platform.
- Avoid using keys that contain periods (`.`) or the `_on` string. For instance, use `this_is_the_key` instead of `this.is.the.key`, and use `join_us_instagram` instead of `join_us_on_instagram`.

#### Step 3: Configure the Braze app on Lokalise

Open your Lokalise project, and click **Apps**. Here, search and install the Braze app. You will see the following screen:

![Braze configuration on Lokalise listing the project ID and the translation files URL.]({% image_buster /assets/img/lokalise/3_lokalise_braze_app.png %})

In the **Translation File URL**, Lokalise publishes a JSON file containing all the translations for your keys in the project. You'll get as many translation file URLs as target languages you have in your project. This is why the resulting translation file URLs have two pieces:

1. The first part of the URL path is common to all languages.
2. The JSON file name at the end of the URL is based on the language code.

The translation file URL is the URL that you will need when configuring a Braze campaign. You can update the content on the JSON file by clicking **Refresh**. Note that the URL will stay the same, and you won't need to change your Connected Content call in Braze.

##### Test URL

To test this URL, copy it and replace {% raw %}`{{${language}}}`{% endraw %} with a language code (for example, `en`) and open this URL in your browser. You will see a JSON file with your keys and translations:

![]({% image_buster /assets/img/lokalise/4_testing_json_lokalise.png %})

#### Step 4: Use translations in Braze campaign

##### Insert Connected Content call

When ready, return to Braze and open an existing campaign or create a new one. We'll create a new email campaign with sample content for this example. Click **Edit Email Body**.

To insert your translations, you need to add the Connected Content request in the HTML, either at the top of the document or right before the first place where a translation is needed. This can be done by inserting the following markup:

{% raw %}
`{% connected_content https://exports.live.lokalise.cloud/braze/123abc/456xyz/{{${language}}}.json :save translations %}`
{% endraw %}

Replace the `https://exports.live.lokalise.cloud/...` URL with the translation file URL fetched in the previous step.

{% raw %}

- `{{${language}}}` means "insert user language on this position". Alternatively, you can hard-code your language code, for example, `en.json`.
  - To ensure that the appropriate translated JSON file is retrieved for each user, you must place either the `{{${language}}}` profile attribute or another similar custom attribute that holds the user's language at the end of the translation files URL. (for example, `/{{${language}}}.json`) The values held in these attributes must match the prefix of each of the translated JSON files. This will ensure the correct translation file is returned for each user.
- `:save translations` will save the JSON content under the translations variable.

##### Display translations

Now use the translations variable to display the desired translations by their keys.

For example, to display the `description` key, use`{{ translations.description }}`.

{% endraw %}
![]({% image_buster /assets/img/lokalise/6_integration_usage_sample.png %})

Lastly, save the email template and preview it. You should see your translation being displayed.

## Frequently asked questions

### What happens if I accidentally delete a key from Lokalise?

The corresponding string on Braze won't have a translation anymore.

### If I have an `en` locale but override it with `en-US` on Lokalise, will Braze read it as `en-US`?

No, locale ISO codes must match on Braze and Lokalise.

### Can we use the `:rerender` flag when connecting Lokalise content?

Yes, sure. You can consult Braze docs to learn how to add this flag.

### After refreshing the translation file on Lokalise, why can't I see any changes in the translated content on Braze?

Braze caches translated content, which can take a few minutes to refresh. If you're testing your campaigns and need to see the results of translations immediately, you can use the `:cache_max_age` parameter as explained in this reference article.


