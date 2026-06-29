---
nav_title: Traducciones
article_title: Puntos finales de traducción
search_tag: Endpoint
page_order: 9
layout: dev_guide

description: "Esta página de destino enumera los puntos finales de traducción de Braze."
page_type: landing

guide_top_header: "Puntos finales de traducción"
guide_top_text: "Usa los puntos finales de traducción de Braze para administrar y actualizar las traducciones en tus Campaigns, Canvas y Content Blocks."

guide_featured_title: "Puntos finales de Campaign"
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

guide_menu_title: "Puntos finales de Canvas"
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

guide_menu_title2: "Puntos finales de plantillas de correo electrónico"
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

guide_menu_title3: "Puntos finales de bloques de contenido"
guide_menu_list3:
  - name: "GET: Ver todas las traducciones de un bloque de contenido"
    link: /docs/api/endpoints/translations/content_blocks/get_translation_content_block
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: Actualizar la traducción en un bloque de contenido"
    link: /docs/api/endpoints/translations/content_blocks/put_update_translation_content_block
    image: /assets/img/braze_icons/target-04.svg

---

{% multi_lang_include alerts/early_access_beta_alert.md feature='Access to the Braze translation endpoints' %}

## Cómo funcionan nuestros puntos finales de traducción {#how-our-translation-endpoints-work}

Nuestros puntos finales de traducción funcionan con la [composición multilingüe]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings), en la que un mensaje puede tener diferentes versiones que se pueden mostrar en función del usuario que reciba el mensaje.

### Requisitos previos {#prerequisites}

Antes de usar estos puntos finales, debes [añadir tus configuraciones regionales]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings#add-a-locale).

### Cómo probar tus traducciones {#how-to-test-your-translations}

Hay dos formas de validar la compatibilidad con la traducción usando la API y el dashboard de Braze en Campaigns, Canvas (incluidos pasos individuales), Content Blocks y plantillas de correo electrónico:

- Durante la composición (antes del lanzamiento)
- Después del lanzamiento (usando borradores posteriores al lanzamiento)

Antes de probar la actualización de las traducciones, debes:

1. [Añadir tus configuraciones regionales]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings#add-a-locale).
2. Crear un mensaje y usar etiquetas de traducción cuando sea necesario.
3. Guardar el mensaje.
4. Seleccionar las configuraciones regionales que deseas incluir.