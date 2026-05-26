---
nav_title: Google Tag Manager
article_title: Google Tag Manager avec le SDK Braze
platform:
  - Android
  - FireOS
  - Swift
page_order: 1.1
description: "Découvrez comment initialiser le SDK Braze à l'aide de méthodes telles que l'initialisation au moment de l'exécution, l'initialisation différée ou Google Tag Manager."

---

# Google Tag Manager avec le SDK Braze {#google-tag-manager-with-the-braze-sdk}

> Découvrez comment utiliser [Google Tag Manager (GTM)](https://developers.google.com/tag-platform/tag-manager) avec le SDK Braze afin de contrôler à distance le suivi des événements Braze et les mises à jour des attributs utilisateur sans avoir à modifier le code ou à publier de nouvelles versions de l'application.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/google_tag_manager.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/google_tag_manager.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/google_tag_manager.md %}
{% endsdktab %}
{% endsdktabs %}

## Résolution des problèmes {#troubleshooting}

Si Braze ne s'initialise pas ou si les événements n'apparaissent pas comme prévu, vérifiez que votre conteneur GTM est publié, que les déclencheurs et l'ordre de déclenchement des balises correspondent au [cycle de vie et à la stratégie d'initialisation]({{site.baseurl}}/developer_guide/sdk_integration/) de votre SDK, et que les appareils de test ne bloquent pas les endpoints de Braze.

En cas d'échec de l'initialisation, vérifiez que la balise Braze ou le fournisseur d'étiquettes personnalisé reçoit le `actionType` et les paramètres attendus (consultez les onglets Android, Swift et Web sur cette page). Pour activer la journalisation détaillée lors de la validation des événements déclenchés par GTM, activez la journalisation de débogage du SDK de votre plateforme comme décrit dans les guides d'intégration de la plateforme accessibles depuis ces onglets.