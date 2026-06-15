---
nav_title: Exemples d'applications
article_title: Exemples d'applications pour iOS
platform: iOS
page_order: 9
description: "Cet article de référence couvre les exemples d'applications iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Exemples d'applications {#sample-apps}

Les SDK de Braze sont tous accompagnés d'exemples d'applications dans le référentiel pour vous faciliter la tâche. Chacune de ces applications est entièrement modulable afin que vous puissiez tester les fonctionnalités de Braze et les implémenter dans vos propres applications. Tester le comportement dans votre propre application par rapport au comportement attendu et aux chemins de code des exemples d'applications est un excellent moyen de déboguer les problèmes que vous pourriez rencontrer.

## Créer les applications de test {#building-test-applications}
Plusieurs applications de test sont disponibles dans le [dépôt GitHub du SDK iOS](https://github.com/appboy/appboy-ios-sdk). Suivez ces instructions pour créer et exécuter nos applications de test.

1. Créez un nouvel [espace de travail]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps) et notez la clé API d'identification de l'application.
2. Placez votre clé API dans le champ approprié du fichier `AppDelegate.m`.

Les notifications push pour l'application de test iOS nécessitent une configuration supplémentaire. Consultez notre [intégration push iOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration/) pour plus de détails.