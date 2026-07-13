---
nav_title: Guide de mise à niveau vers iOS 16
article_title: Guide de mise à niveau iOS 16
page_order: 7
platform:
  - iOS
description: "Cet article de référence aborde iOS 16, la mise à niveau, les mises à jour du SDK, et bien plus encore."
hidden: true
noindex: true
---

# Guide de mise à jour du SDK iOS 16 {#ios-16-sdk-upgrade-guide}

> Ce guide décrit les modifications pertinentes introduites dans iOS 16 (2022) et leur impact sur votre intégration SDK Braze pour iOS. Consultez les [notes de version d'iOS 16](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-16-release-notes) pour un guide complet de migration.

## Modifications dans iOS 16 {#changes-in-ios-16}

### Notifications push Web Safari {#safari-web-push}

Apple a annoncé deux changements concernant sa fonctionnalité de notification push Web.

#### Notifications push Web sur ordinateur de bureau (macOS) {#macos-push}

Auparavant, Apple prenait en charge les notifications push sur macOS (ordinateur de bureau) en utilisant ses propres API push Safari.

À partir de macOS Ventura (sorti le 24 octobre 2022), [Safari a ajouté la prise en charge](https://webkit.org/blog/12824/news-from-wwdc-webkit-features-in-safari-16-beta/#web-push-for-macos) des API de notification push Web en plus des notifications push Safari. Il s'agit d'une norme d'API multi-navigateurs existante utilisée par d'autres navigateurs populaires.

Si vous envoyez déjà des notifications push Web pour Safari via Braze, aucune modification n'est nécessaire.

#### Notifications push Web sur appareil mobile (iOS et iPadOS) {#ios-push}

Auparavant, Safari sur iPhone et iPad ne prenait pas en charge la réception de notifications push.

En 2023, Apple ajoutera la prise en charge des notifications push Web sur les appareils iPhone et iPad via Safari.

Braze prendra en charge ces nouvelles notifications push Web pour iOS et iPadOS sans nécessiter de modifications ou de mises à niveau supplémentaires.

## Préparation pour iOS 16 {#next-steps}

Bien que vous n'ayez pas besoin de mettre à jour votre SDK Braze pour iOS afin de prendre en charge iOS 16, voici deux autres mises à jour intéressantes :

1. Braze a lancé un [nouveau SDK Swift](https://github.com/braze-inc/braze-swift-sdk). Il offre de meilleures performances, de nouvelles fonctionnalités et de nombreuses améliorations.
2. Notre SDK Braze Swift prend en charge une nouvelle [fonctionnalité de « push primer » sans code]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) !