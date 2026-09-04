---
nav_title: Traducciones
article_title: Endpoints de traducción
search_tag: Endpoint
page_order: 9
layout: dev_guide

description: "Esta página de destino enumera los endpoints de traducción de Braze."
page_type: landing

guide_top_header: "Endpoints de traducción"
guide_top_text: "Usa los endpoints de traducción de Braze para administrar y actualizar las traducciones en tus Campaigns, Canvas, Content Blocks, plantillas de correo electrónico y plantillas de webhook."

guide_featured_title: "Endpoints de Campaign"
guide_featured_list:
  - name: "GET: Ver la traducción de una Campaign"
    link: /docs/api/endpoints/translations/campaigns/get_translation_campaign
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: Actualizar la traducción en una Campaign"
    link: /docs/api/endpoints/translations/campaigns/put_update_translation_campaign
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: Ver los valores de fuente predeterminados para las etiquetas de traducción de Campaign"
    link: /docs/api/endpoints/translations/campaigns/get_source_campaign
    image: /assets/img/braze_icons/message-plus-square.svg

guide_menu_title: "Endpoints de Canvas"
guide_menu_list:
  - name: "GET: Ver la traducción de un Canvas"
    link: /docs/api/endpoints/translations/canvas/get_translation_canvas
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: Actualizar la traducción en un Canvas"
    link: /docs/api/endpoints/translations/canvas/put_update_translation_canvas
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: Ver los valores de fuente predeterminados para las etiquetas de traducción de un Canvas"
    link: /docs/api/endpoints/translations/canvas/get_source_canvas
    image: /assets/img/braze_icons/message-plus-square.svg

guide_menu_title2: "Endpoints de plantillas de correo electrónico"
guide_menu_list2:
  - name: "GET: Ver los valores de fuente predeterminados para las etiquetas de traducción de una plantilla de correo electrónico"
    link: /docs/api/endpoints/translations/email_templates/get_view_source_template
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET: Ver traducción y configuración regional específicas"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_locale_template
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: Ver todas las traducciones y configuraciones regionales"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_template
    image: /assets/img/braze_icons/target-04.svg
  - name: "PUT: Actualizar traducciones en una plantilla de correo electrónico"
    link: /docs/api/endpoints/translations/email_templates/put_update_template
    image: /assets/img/braze_icons/target-04.svg

guide_menu_title3: "Endpoints de bloques de contenido"
guide_menu_list3:
  - name: "GET: Ver todas las traducciones de un bloque de contenido"
    link: /docs/api/endpoints/translations/content_blocks/get_translation_content_block
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: Actualizar la traducción en un bloque de contenido"
    link: /docs/api/endpoints/translations/content_blocks/put_update_translation_content_block
    image: /assets/img/braze_icons/target-04.svg

guide_menu_title4: "Endpoints de plantillas de webhook"
guide_menu_list4:
  - name: "GET: Ver los valores de fuente predeterminados para las etiquetas de traducción de una plantilla de webhook"
    link: /docs/api/endpoints/translations/webhook_templates/get_view_source_webhook_template
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET: Ver las traducciones de una plantilla de webhook"
    link: /docs/api/endpoints/translations/webhook_templates/get_view_translations_webhook_template
    image: /assets/img/braze_icons/target-04.svg
  - name: "PUT: Actualizar traducciones en una plantilla de webhook"
    link: /docs/api/endpoints/translations/webhook_templates/put_update_webhook_template
    image: /assets/img/braze_icons/target-04.svg

---

{% multi_lang_include alerts/early_access_beta_alert.md feature='Access to the Braze translation endpoints' %}

## Cómo funcionan nuestros endpoints de traducción {#how-our-translation-endpoints-work}

Nuestros endpoints de traducción funcionan con la [composición multilingüe]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings), donde un mensaje puede tener diferentes versiones que se pueden renderizar según el usuario que recibe el mensaje.

### Requisitos previos {#prerequisites}

Antes de usar estos endpoints, debes [agregar tus configuraciones regionales]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings#add-a-locale).

### Cómo probar tus traducciones {#how-to-test-your-translations}

Hay dos formas de validar la compatibilidad con traducciones usando la API y el panel de Braze en Campaigns, Canvas (incluidos los pasos individuales), Content Blocks, plantillas de correo electrónico y plantillas de webhook:

- Durante la composición (antes del lanzamiento)
- Después del lanzamiento (usando borradores posteriores al lanzamiento)

Antes de probar la actualización de traducciones, debes:

1. [Agregar tus configuraciones regionales]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings#add-a-locale).
2. Crear un mensaje y usar etiquetas de traducción donde corresponda.
3. Guardar el mensaje.
4. Seleccionar las configuraciones regionales que se incluirán.