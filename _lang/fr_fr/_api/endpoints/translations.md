---
nav_title: Traductions
article_title: Endpoints de traduction
search_tag: Endpoint
page_order: 9
layout: dev_guide

description: "Cette page de destination répertorie les endpoints de traduction de Braze."
page_type: landing

guide_top_header: "Endpoints de traduction"
guide_top_text: "Utilisez les endpoints de traduction de Braze pour gérer et mettre à jour les traductions dans vos Campaigns, Canvas, Content Blocks, modèles d'e-mail et modèles de webhook."

guide_featured_title: "Endpoints de Campaign"
guide_featured_list:
  - name: "GET : Afficher la traduction d'une Campaign"
    link: /docs/api/endpoints/translations/campaigns/get_translation_campaign
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT : Mettre à jour la traduction dans une Campaign"
    link: /docs/api/endpoints/translations/campaigns/put_update_translation_campaign
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET : Afficher les valeurs sources par défaut pour les étiquettes de traduction de Campaign"
    link: /docs/api/endpoints/translations/campaigns/get_source_campaign
    image: /assets/img/braze_icons/message-plus-square.svg

guide_menu_title: "Endpoints Canvas"
guide_menu_list:
  - name: "GET : Afficher la traduction d'un Canvas"
    link: /docs/api/endpoints/translations/canvas/get_translation_canvas
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT : Mettre à jour la traduction dans un Canvas"
    link: /docs/api/endpoints/translations/canvas/put_update_translation_canvas
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET : Afficher les valeurs sources par défaut pour les traductions d'un Canvas"
    link: /docs/api/endpoints/translations/canvas/get_source_canvas
    image: /assets/img/braze_icons/message-plus-square.svg

guide_menu_title2: "Endpoints de modèles d'e-mail"
guide_menu_list2:
  - name: "GET : Afficher les valeurs sources par défaut pour les traductions d'un modèle d'e-mail"
    link: /docs/api/endpoints/translations/email_templates/get_view_source_template
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET : Afficher une traduction et une locale spécifiques"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_locale_template
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET : Afficher toutes les traductions et locales"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_template
    image: /assets/img/braze_icons/target-04.svg
  - name: "PUT : Mettre à jour les traductions dans un modèle d'e-mail"
    link: /docs/api/endpoints/translations/email_templates/put_update_template
    image: /assets/img/braze_icons/target-04.svg

guide_menu_title3: "Endpoints de blocs de contenu"
guide_menu_list3:
  - name: "GET : Afficher toutes les traductions d'un bloc de contenu"
    link: /docs/api/endpoints/translations/content_blocks/get_translation_content_block
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT : Mettre à jour la traduction dans un bloc de contenu"
    link: /docs/api/endpoints/translations/content_blocks/put_update_translation_content_block
    image: /assets/img/braze_icons/target-04.svg

guide_menu_title4: "Endpoints de modèles de webhook"
guide_menu_list4:
  - name: "GET : Afficher les valeurs sources par défaut pour les traductions d'un modèle de webhook"
    link: /docs/api/endpoints/translations/webhook_templates/get_view_source_webhook_template
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET : Afficher les traductions d'un modèle de webhook"
    link: /docs/api/endpoints/translations/webhook_templates/get_view_translations_webhook_template
    image: /assets/img/braze_icons/target-04.svg
  - name: "PUT : Mettre à jour les traductions dans un modèle de webhook"
    link: /docs/api/endpoints/translations/webhook_templates/put_update_webhook_template
    image: /assets/img/braze_icons/target-04.svg

---

{% multi_lang_include alerts/early_access_beta_alert.md feature='Access to the Braze translation endpoints' %}

## Fonctionnement de nos endpoints de traduction {#how-our-translation-endpoints-work}

Nos endpoints de traduction fonctionnent avec la [composition multilingue]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings), où un message peut avoir différentes versions pouvant être rendues en fonction de l'utilisateur recevant le message.

### Prérequis {#prerequisites}

Avant d'utiliser ces endpoints, vous devez [ajouter vos locales]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings#add-a-locale).

### Comment tester vos traductions {#how-to-test-your-translations}

Il existe deux façons de valider la prise en charge des traductions en utilisant l'API et le tableau de bord de Braze pour les Campaigns, les Canvas (y compris les étapes individuelles), les Content Blocks, les modèles d'e-mail et les modèles de webhook :

- Pendant la composition (avant le lancement)
- Après le lancement (en utilisant des brouillons post-lancement)

Avant de tester la mise à jour des traductions, vous devez :

1. [Ajouter vos locales]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings#add-a-locale).
2. Créer un message et utiliser les tags de traduction là où c'est approprié.
3. Enregistrer le message.
4. Sélectionner les locales à inclure.