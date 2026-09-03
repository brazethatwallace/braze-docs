---
nav_title: Traduções
article_title: Endpoints de Tradução
search_tag: Endpoint
page_order: 9
layout: dev_guide

description: "Esta landing page lista os endpoints de tradução da Braze."
page_type: landing

guide_top_header: "Endpoints de Tradução"
guide_top_text: "Use os endpoints de tradução da Braze para gerenciar e atualizar traduções em suas Campaigns, Canvas, Content Blocks, modelos de e-mail e modelos de webhook."

guide_featured_title: "Endpoints de Campaign"
guide_featured_list:
  - name: "GET: Ver tradução de uma Campaign"
    link: /docs/api/endpoints/translations/campaigns/get_translation_campaign
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: Atualizar tradução em uma Campaign"
    link: /docs/api/endpoints/translations/campaigns/put_update_translation_campaign
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: Ver traduções de origem padrão de uma Campaign"
    link: /docs/api/endpoints/translations/campaigns/get_source_campaign
    image: /assets/img/braze_icons/message-plus-square.svg

guide_menu_title: "Endpoints de Canvas"
guide_menu_list:
  - name: "GET: Ver tradução de um Canvas"
    link: /docs/api/endpoints/translations/canvas/get_translation_canvas
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: Atualizar tradução em um Canvas"
    link: /docs/api/endpoints/translations/canvas/put_update_translation_canvas
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: Ver traduções de origem padrão de um Canvas"
    link: /docs/api/endpoints/translations/canvas/get_source_canvas
    image: /assets/img/braze_icons/message-plus-square.svg

guide_menu_title2: "Endpoints de modelos de e-mail"
guide_menu_list2:
  - name: "GET: Ver traduções de origem padrão de um modelo de e-mail"
    link: /docs/api/endpoints/translations/email_templates/get_view_source_template
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET: Ver tradução e localidade específicas"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_locale_template
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: Ver todas as traduções e localidades"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_template
    image: /assets/img/braze_icons/target-04.svg
  - name: "PUT: Atualizar traduções em um modelo de e-mail"
    link: /docs/api/endpoints/translations/email_templates/put_update_template
    image: /assets/img/braze_icons/target-04.svg

guide_menu_title3: "Endpoints de blocos de conteúdo"
guide_menu_list3:
  - name: "GET: Ver todas as traduções de um bloco de conteúdo"
    link: /docs/api/endpoints/translations/content_blocks/get_translation_content_block
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: Atualizar tradução em um bloco de conteúdo"
    link: /docs/api/endpoints/translations/content_blocks/put_update_translation_content_block
    image: /assets/img/braze_icons/target-04.svg

guide_menu_title4: "Endpoints de modelos de webhook"
guide_menu_list4:
  - name: "GET: Ver traduções de origem padrão de um modelo de webhook"
    link: /docs/api/endpoints/translations/webhook_templates/get_view_source_webhook_template
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET: Ver traduções de um modelo de webhook"
    link: /docs/api/endpoints/translations/webhook_templates/get_view_translations_webhook_template
    image: /assets/img/braze_icons/target-04.svg
  - name: "PUT: Atualizar traduções em um modelo de webhook"
    link: /docs/api/endpoints/translations/webhook_templates/put_update_webhook_template
    image: /assets/img/braze_icons/target-04.svg

---

{% multi_lang_include alerts/early_access_beta_alert.md feature='Access to the Braze translation endpoints' %}

## Como nossos endpoints de tradução funcionam {#how-our-translation-endpoints-work}

Nossos endpoints de tradução funcionam com a [composição multilíngue]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings), onde uma mensagem pode ter diferentes versões que podem ser renderizadas dependendo do usuário que recebe a mensagem.

### Pré-requisitos {#prerequisites}

Antes de usar esses endpoints, você deve [adicionar seus locais]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings#add-a-locale).

### Como testar suas traduções {#how-to-test-your-translations}

Existem duas maneiras de validar o suporte a traduções usando a API e o dashboard da Braze em Campaigns, Canvas (incluindo etapas individuais), Content Blocks, modelos de e-mail e modelos de webhook:

- Durante a composição (antes do lançamento)
- Após o lançamento (usando rascunhos pós-lançamento)

Antes de testar a atualização de traduções, você deve:

1. [Adicionar seus locais]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings#add-a-locale).
2. Criar uma mensagem e usar tags de tradução onde for apropriado.
3. Salvar a mensagem.
4. Selecionar os locais a serem incluídos.