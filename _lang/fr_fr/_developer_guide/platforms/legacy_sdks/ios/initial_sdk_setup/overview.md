---
nav_title: Aperçu
article_title: Aperçu de l'intégration pour iOS
platform: iOS
page_order: 0
layout: dev_guide
search_rank: 6
guide_top_header: "Aperçu de l'intégration"
guide_top_text: ""
description: "Cette page d'accueil couvre les guides d'intégration SDK de Braze pour CocoaPods, le gestionnaire de paquets Swift, Carthage, et plus encore."

guide_featured_title: "Options d'intégration de base"
guide_featured_list:
- name: CocoaPods
  link: /developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/installation_methods/cocoapods/
  image: /assets/img/cocoapods.png
- name: Gestionnaire de paquets Swift (SPM)
  link: /docs/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview
  image: /assets/img/braze_icons/swift.svg
- name: Carthage
  link: /docs/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview
  image: /assets/img/carthage.png
- name: Manuel
  link: /docs/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview
  image: /assets/img/braze_icons/tool-01.svg
- name: "Terminer l'intégration"
  link: /docs/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview
  image: /assets/img/braze_icons/flag-05.svg
- name: "Autres personnalisations SDK facultatives"
  link: /docs/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview
  image: /assets/img/braze_icons/user-square.svg

noindex: true
---
<br>

{% multi_lang_include deprecations/objective-c.md %}

L'installation du SDK Braze pour iOS vous offrira des fonctionnalités d'analyse de base (gestion de session) et des messages in-app de base. Vous devez personnaliser davantage votre intégration pour accéder à des canaux et fonctionnalités supplémentaires. <br> <br> Le SDK Braze pour iOS peut être installé ou mis à jour à l'aide de CocoaPods, Carthage, du gestionnaire de paquets Swift ou d'une intégration manuelle. <br> <br> De plus, le SDK Braze pour iOS prend entièrement en charge les applications RubyMotion.

{% alert important %}
Le SDK iOS ajoutera 1&nbsp;Mo à 2&nbsp;Mo au fichier IPA de l'application, en plus d'un fichier APP, et 30&nbsp;Mo pour le framework.
{% endalert %}

Après avoir effectué l'intégration en utilisant l'une des options citées, suivi les étapes pour [terminer l'intégration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration) et activé d'autres personnalisations SDK (facultatif), passez à l'intégration, à l'activation et à la personnalisation de canaux et fonctionnalités supplémentaires pour répondre aux besoins de vos futures campagnes.

<br>