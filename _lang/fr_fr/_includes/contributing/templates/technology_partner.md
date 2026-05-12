Vous pouvez utiliser ce modèle pour créer la documentation du partenaire technologique. Pour un exemple, voir [Scuba Analytics]({{site.baseurl}}/partners/data_and_analytics/business_intelligence/scuba/).

{% details Afficher le modèle %}
{% raw %}
`````markdown
---
nav_title: PARTNER_NAME
article_title: PARTNER_NAME
description: "This reference article outlines the partnership between Braze and PARTNER_NAME."
alias: /partners/PARTNER_NAME/
page_type: partner
search_tag: Partner
---

# ARTICLE_TITLE
<!-- In most cases, the ARTICLE_TITLE will be your company name. If your tool requires several separate pages on Braze Docs, you can add a relevant page descriptor to those pages’ titles, such as "MyCompany Analytics." -->

> DESCRIPTION.
<!-- The description starts with a '>' character and contains an introduction to your company, a link to your main site, and a concise overview of your integration.-->

<-- Only include the following line if the partner manages the integration. If Braze manages the integration, don’t include it. -->
*This integration is maintained by PARTNER_NAME*

## About this integration
<-- Highlight the relationship between your company and Braze and how this partnership helps your customers. -->

ADDITIONAL_INFORMATION.

## Use cases
<!--Though the ‘Use cases’ section is optional, this is a good place to outline typical or even novel use cases for the integration. Use this section as a way to sell or upsell your integration to customers and Braze account teams; it provides context, ideas, and most importantly, a way to visualize the capabilities of your integration.-->

CONTENT.

<!-- When including screenshots, use the following format to specify where each screenshot should be placed. PARTNER_NAME and IMAGE_NAME should be all lowercase. -->
![ALT_TEXT]({% image_buster /assets/img/PARTNER_NAME/IMAGE_NAME.png %})

## Prerequisites
<!-- Most partner integrations require the following prerequisites. However, you may add additional prerequisites as needed. -->

Before you start, you need the following:

| Prerequisite       | Description |
|-----------------------|-----------------|
| A PARTNER_NAME account   | A PARTNER_NAME account is required to take advantage of this partnership.  |
| A Braze REST API key  | A Braze REST API key with `users.track` permissions. <br><br> Create this key in the Braze dashboard from **Settings** > **API Keys**. |
| A Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint depends on the Braze URL for your instance.  |
{: .reset-td-br-1 .reset-td-br-2 aria-label=”Prerequisites” }

## Integrating TOOL_NAME
<!-- Create step-by-step instructions for integrating your tool with Braze. It's important to be concise and outline the minimum necessary steps. -->

### Step 1: ACTION_TO_COMPLETE

CONTENT.

### Step 2: Make a POST request
<!-- Use the "Make a POST request", "Default behavior," and "Rate limit" sections to outline how users can make a POST request. If this information isn't required for your integration, you can remove these sections. -->

{% alert important %}
The following request uses cURL. For better API request management, we recommend using an API client, such as Postman.
{% endalert %}

To upload your PARTNER_NAME data to Braze, make a POST request to `PARTNER_POST_URL` using the `application/json` content-type:

```bash
curl -X POST "PARTNER_POST_URL" \
-H "content-type: application/json" \
-d '{"braze_host":"BRAZE_API_ENDPOINT", \
"braze_api_key":"BRAZE_API_KEY", \
"PARTNER_host":"HOSTNAME", \
"PARTNER_token":"PARTNER_NAME_API_TOKEN"}'
```

Remplacez les éléments suivants :

| Marque substitutive | Description |
|---------------------|---------------------|
| `BRAZE_API_ENDPOINT` | L'URL de l'endpoint REST Braze de votre instance Braze actuelle. Pour plus d'informations, consultez [Clés API REST]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys). |
| `BRAZE_API_KEY` | Votre clé API REST Braze avec l'autorisation `users.track`. |
| `HOSTNAME` | Le nom d'hôte de votre instance PARTNER_NAME actuelle. |
| `PARTNER_NAME_API_TOKEN` | Votre jeton API PARTNER_NAME. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 2 : Effectuer une requête POST" }

#### Comportement par défaut

CONTENT.

#### Limite de débit

CONTENT.

## Personnalisation de TOOL_NAME
<!-- Une section facultative que vous pouvez utiliser pour décrire des étapes de personnalisation supplémentaires. Il est important d'être concis et de décrire les étapes minimales nécessaires. -->

### Étape 1 : ACTION_TO_COMPLETE

CONTENT.

### Étape 2 : ACTION_TO_COMPLETE

CONTENT.

## Utilisation de TOOL_NAME avec Braze / USE_CASE
<!-- Une section décrivant comment utiliser votre intégration avec Braze. Par exemple, comment accéder aux données envoyées à Braze, comment tirer parti de votre intégration avec l'envoi de messages Braze, ou comment réaliser un cas d'utilisation spécifique de la section « Cas d'utilisation ». -->

### Étape 1 : ACTION_TO_COMPLETE

CONTENT.

### Étape 2 : ACTION_TO_COMPLETE

CONTENT.

## Considérations
<!-- Une section facultative listant des informations supplémentaires pouvant avoir un impact sur la façon dont les utilisateurs interagissent avec votre intégration. -->

### CONSIDERATION_ITEM

CONTENT.

## Résolution des problèmes
<!-- Une section facultative guidant les utilisateurs à travers les problèmes qu'ils peuvent rencontrer lors de la configuration de votre intégration. Vous pouvez également diriger les utilisateurs vers votre site de documentation avec des liens hypertextes. -->

### TROUBLESHOOTING_ITEM

CONTENT.
`````
{% endraw %}
{% enddetails %}