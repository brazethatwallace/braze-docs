---
nav_title: Übersetzungen
article_title: Übersetzungsendpunkte
search_tag: Endpoint
page_order: 9
layout: dev_guide

description: "Diese Landing-Page listet die Braze-Übersetzungsendpunkte auf."
page_type: landing

guide_top_header: "Übersetzungsendpunkte"
guide_top_text: "Verwenden Sie die Braze-Übersetzungsendpunkte, um Übersetzungen in Ihren Campaigns, Canvases und Content Blocks zu verwalten und zu aktualisieren."

guide_featured_title: "Campaign-Endpunkte"
guide_featured_list:
  - name: "GET: Übersetzung für eine Campaign anzeigen"
    link: /docs/api/endpoints/translations/campaigns/get_translation_campaign/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: Übersetzung in einer Campaign aktualisieren"
    link: /docs/api/endpoints/translations/campaigns/put_update_translation_campaign/
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: Standardquellwerte für Campaign-Übersetzungen anzeigen"
    link: /docs/api/endpoints/translations/campaigns/get_source_campaign/
    image: /assets/img/braze_icons/message-plus-square.svg

guide_menu_title: "Canvas-Endpunkte"
guide_menu_list:
  - name: "GET: Übersetzung für ein Canvas anzeigen"
    link: /docs/api/endpoints/translations/canvas/get_translation_canvas/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: Übersetzung in einem Canvas aktualisieren"
    link: /docs/api/endpoints/translations/canvas/put_update_translation_canvas/
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: Standardquellwerte für Canvas-Übersetzungen anzeigen"
    link: /docs/api/endpoints/translations/canvas/get_source_canvas/
    image: /assets/img/braze_icons/message-plus-square.svg

guide_menu_title2: "E-Mail-Template-Endpunkte"
guide_menu_list2:
  - name: "GET: Standardquellwerte für E-Mail-Template-Übersetzungen anzeigen"
    link: /docs/api/endpoints/translations/email_templates/get_view_source_template/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET: Bestimmte Übersetzung und Locale anzeigen"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_locale_template/
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: Alle Übersetzungen und Locales anzeigen"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_template/
    image: /assets/img/braze_icons/target-04.svg
  - name: "PUT: Übersetzungen in einem E-Mail-Template aktualisieren"
    link: /docs/api/endpoints/translations/email_templates/put_update_template/
    image: /assets/img/braze_icons/target-04.svg

guide_menu_title3: "Content-Block-Endpunkte"
guide_menu_list3:
  - name: "GET: Alle Übersetzungen für einen Content-Block anzeigen"
    link: /docs/api/endpoints/translations/content_blocks/get_translation_content_block/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: Übersetzung in einem Content-Block aktualisieren"
    link: /docs/api/endpoints/translations/content_blocks/put_update_translation_content_block/
    image: /assets/img/braze_icons/target-04.svg

---

{% multi_lang_include early_access_beta_alert.md feature='Access to the Braze translation endpoints' %}

## So funktionieren unsere Übersetzungsendpunkte {#how-our-translation-endpoints-work}

Unsere Übersetzungsendpunkte arbeiten mit der [mehrsprachigen Komposition]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings/), bei der eine Nachricht verschiedene Versionen haben kann, die je nach empfangender Nutzer:in unterschiedlich gerendert werden.

### Voraussetzungen {#prerequisites}

Bevor Sie diese Endpunkte verwenden, müssen Sie [Ihre Locales hinzufügen]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#add-a-locale).

### So testen Sie Ihre Übersetzungen {#how-to-test-your-translations}

Es gibt zwei Möglichkeiten, die Übersetzungsunterstützung mithilfe der API und des Braze-Dashboards für Campaigns, Canvases (einschließlich einzelner Schritte), Content Blocks und E-Mail-Templates zu überprüfen:

- Während der Komposition (vor dem Start)
- Nach dem Start (mithilfe von Entwürfen nach dem Start)

Bevor Sie das Aktualisieren von Übersetzungen testen, müssen Sie:

1. [Ihre Locales hinzufügen]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#add-a-locale).
2. Eine Nachricht erstellen und gegebenenfalls Übersetzungs-Tags verwenden.
3. Die Nachricht speichern.
4. Die einzubeziehenden Locales auswählen.