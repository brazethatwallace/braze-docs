Você pode usar esse modelo para criar a documentação da parceira de tecnologia. Para ver um exemplo, consulte [Scuba Analytics]({{site.baseurl}}/partners/data_and_analytics).

{% details Mostrar modelo %}
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
| A Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Your endpoint depends on the Braze URL for your instance.  |
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

Substitua o seguinte:

| Placeholder     | Descrição      |
|---------------------|---------------------|
| `BRAZE_API_ENDPOINT`    | A URL do endpoint REST da Braze da sua instância atual da Braze. Para saber mais, consulte [Chaves da API REST]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab#rest-api-keys). |
| `BRAZE_API_KEY`         | Sua chave da API REST da Braze com a permissão `users.track`. |                                                                                                                                    | `HOSTNAME`                  | O hostname da sua instância atual de PARTNER_NAME.  |
| `PARTNER_NAME_API_TOKEN`       | Seu token de API PARTNER_NAME.  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 2: Fazer uma solicitação POST" }

#### Comportamento padrão

CONTENT.

#### Limite de frequência

CONTENT.

## Personalizando TOOL_NAME
<!-- Uma seção opcional que você pode usar para descrever etapas adicionais de personalização. É importante ser conciso e descrever apenas as etapas mínimas necessárias. -->

### Etapa 1: ACTION_TO_COMPLETE

CONTENT.

### Etapa 2: ACTION_TO_COMPLETE

CONTENT.

## Usando TOOL_NAME com a Braze / USE_CASE
<!-- Uma seção que descreve como usar sua integração com a Braze. Por exemplo, como acessar os dados enviados para a Braze, como aproveitar sua integração com o envio de mensagens da Braze ou como concluir um determinado caso de uso da seção "Casos de uso". -->

### Etapa 1: ACTION_TO_COMPLETE

CONTENT.

### Etapa 2: ACTION_TO_COMPLETE

CONTENT.

## Considerações
<!-- Uma seção opcional que lista informações adicionais que podem afetar a forma como os usuários interagem com a sua integração. -->

### CONSIDERATION_ITEM

CONTENT.

## Solução de problemas
<!-- Uma seção opcional que orienta os usuários sobre problemas que podem encontrar ao configurar sua integração. Você também pode direcionar os usuários para o seu site de documentação com hiperlinks. -->

### TROUBLESHOOTING_ITEM

CONTENT.
`````
{% endraw %}
{% enddetails %}