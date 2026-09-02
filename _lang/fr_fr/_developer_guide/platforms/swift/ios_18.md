---
nav_title: Mise à jour vers iOS 18
article_title: Mise à jour vers iOS 18
page_order: 7.1
platform:
  - iOS
description: "Cet article couvre les informations sur la version iOS 18 pour vous aider à mettre à jour votre SDK de façon fluide."
---

# Mise à jour vers iOS 18 {#upgrading-to-ios-18}

> Vous souhaitez savoir comment Braze se prépare à la prochaine version d'iOS ? Cet article résume nos informations sur la version iOS 18 pour vous aider à créer une expérience fluide pour vous et vos utilisateurs.

La [WWDC](https://developer.apple.com/wwdc24/) d'Apple a eu lieu du 9 au 11 juin 2024. Découvrez leurs annonces dans notre [article de blog](https://www.braze.com/resources/articles/wwdc-announcements-bring-apple-intelligence-rcs-and-more-to-ios-18), ou poursuivez votre lecture pour savoir comment tirer parti d'iOS 18 avec Braze.

## Changements dans iOS 18 {#changes-in-ios-18}

### en direct or en ligne/en production/instantané Activities sur Apple Watch {#live-activities-on-apple-watch}

Les [en direct or en ligne/en production/instantané Activities]({{site.baseurl}}/developer_guide/live_notifications?sdktab=swift) seront prises en charge sur watchOS 11. Aucune configuration supplémentaire n'est requise. Cependant, Apple offre la possibilité de personnaliser l'interface de la montre.

### Apple Vision Pro

Le Vision Pro est désormais disponible en Chine, au Japon, à Singapour, en Australie, au Canada, en France, en Allemagne et au Royaume-Uni. Consultez notre blog pour découvrir comment [Braze prend en charge visionOS](https://www.braze.com/resources/articles/building-braze-a-new-era-of-customer-engagement-braze-announces-visionos-support).

### Notifications iPhone sur macOS {#iphone-notifications-on-macos}

La nouvelle fonctionnalité [Recopie de l'iPhone](https://www.apple.com/newsroom/2024/06/macos-sequoia-takes-productivity-and-intelligence-on-mac-to-new-heights/) d'Apple permet aux utilisateurs de recevoir les notifications iPhone sur leurs appareils macOS. Gardez à l'esprit que certains types de médias, tels que les images Push Story et les GIF, ne sont pas pris en charge, car ils ne peuvent pas être rendus sous forme de notification macOS.

### Apple Intelligence

[Apple Intelligence](https://developer.apple.com/documentation/Updates/Apple-Intelligence) est désormais disponible pour les appareils fonctionnant sous iOS 18.1 et versions ultérieures.

En tant qu'utilisateur de Braze, la nouvelle fonctionnalité la plus importante à connaître est celle des [résumés de notifications](https://support.apple.com/en-us/108781), qui utilise le traitement sur l'appareil pour regrouper automatiquement et générer des résumés textuels pour les notifications push associées envoyées depuis une même application. Les utilisateurs finaux peuvent appuyer sur un résumé pour le développer et afficher chaque notification push telle qu'elle a été envoyée à l'origine.

En raison de la manière dont ces résumés sont générés, vous n'aurez pas de contrôle sur leur comportement spécifique ni sur le texte généré. Cependant, cela n'aura aucun impact sur les fonctionnalités d'analyse ou de reporting, telles que le suivi des clics sur les notifications push.

![Exemple de capture d'écran d'un aperçu de résumé de notification push.]({% image_buster /assets/img/apple/apple_intelligence/notification_preview_summary.png %})