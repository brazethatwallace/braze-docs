---
nav_title: Prise en charge de visionOS
article_title: Prise en charge de visionOS
page_order: 7.2
platform:
  - iOS
description: "Cet article aborde les fonctionnalités prises en charge sur visionOS."
---

# Prise en charge de visionOS {#visionos-support}

> À partir de la version [8.0.0 du SDK Braze Swift](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#800), vous pouvez utiliser Braze avec [visionOS](https://developer.apple.com/visionos/), la plateforme de calcul spatial d'Apple pour l'Apple Vision Pro. Pour découvrir un exemple d'application visionOS utilisant Braze, consultez [Exemples d'applications]({{site.baseurl}}/developer_guide/references?tab=swift).

## Fonctionnalités entièrement prises en charge {#fully-supported-features}

La plupart des fonctionnalités disponibles sur iOS sont également disponibles sur visionOS, notamment :

- Analyse (sessions, événements personnalisés, achats, etc.)
- Envoi de messages in-app (modèles de données et interface utilisateur)
- Content Cards (modèles de données et interface utilisateur)
- Notifications push (visibles par l'utilisateur avec des boutons d'action et des notifications silencieuses)
- Indicateurs de fonctionnalité
- Analyse de localisation

## Fonctionnalités partiellement prises en charge {#partially-supported-features}

Certaines fonctionnalités ne sont que partiellement prises en charge sur visionOS, mais Apple devrait y remédier à l'avenir :

- Notifications push riches
  - Les images sont prises en charge.
  - Les GIF et les vidéos affichent la vignette de prévisualisation, mais ne peuvent pas être lus.
  - La lecture audio n'est pas prise en charge.
- Push Stories
  - Le défilement et la sélection de la page Push Story sont pris en charge.
  - La navigation entre les pages Push Story à l'aide de **Next** n'est pas prise en charge.

## Fonctionnalités non prises en charge {#unsupported-features}

- La surveillance des géorepérages n'est pas prise en charge. Apple n'a pas mis à disposition les API Core Location pour la surveillance des régions sur visionOS.
- Les activités en direct ne sont pas prises en charge. Actuellement, ActivityKit n'est disponible que sur iOS et iPadOS.