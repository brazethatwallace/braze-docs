---
nav_title: "Messages push multiplateformes"
article_title: "Messages multiplateformes"
alias: "/multiple_platform_push/"
description: "Cet article décrit les points à connaître lors de la création d'une campagne push ou d'un Canvas avec plusieurs plateformes sélectionnées."
page_order: 4
---

# Messages push multiplateformes {#multiple-platform-push-messages}

> Cet article décrit ce qu'il faut savoir lorsque vous créez une campagne push ou un Canvas pour cibler plusieurs plateformes et appareils à partir d'un seul compositeur.

Lorsque vous créez une campagne push ou un Canvas dans Braze, vous pouvez sélectionner plusieurs plateformes et appareils pour composer un seul message destiné à toutes les plateformes dans une expérience d'édition unique.

## Cas d'usage {#use-cases}

Cette expérience d'édition est idéale pour les cas d'usage suivants :

- Les Campaigns et les étapes de message Canvas pour les notifications push mobiles qui doivent être envoyées à plusieurs types d'appareils (par exemple, à la fois iOS et Android).
- Les notifications push urgentes qui doivent cibler plusieurs plateformes rapidement et avec précision, lorsque le contenu est identique sur toutes les plateformes (par exemple, les dernières nouvelles ou les mises à jour en direct or en ligne/en production/instantané d'un événement sportif).

## Création d'une campagne push multiplateforme ou d'un Canvas {#creating-a-multiple-platform-push-campaign-or-canvas}

Pour créer une campagne ciblant plusieurs plateformes et appareils :

1. Créez une campagne ou ajoutez une [étape Message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) à un Canvas.
2. Sélectionnez **Notification push**.
3. Sélectionnez les plateformes souhaitées (Mobile, Web, Kindle) et les appareils mobiles (iOS, Android). Si vous sélectionnez plusieurs appareils, le test multivarié ne sera pas disponible pour votre campagne.

### Sélection des plateformes pour une campagne {#selecting-platforms-for-a-campaign}
![Options pour sélectionner plusieurs plateformes pour une campagne push, telles que Mobile, Web et Kindle, et plusieurs appareils, tels qu'iOS et Android.]({% image_buster /assets/img_archive/push_multiple_platform_message_selection.png %})

### Sélection des plateformes pour une étape Canvas {#selecting-platforms-for-a-canvas-step}
![Options pour sélectionner plusieurs plateformes pour une étape Message push, telles que Mobile, Web et Kindle, et plusieurs appareils, tels qu'iOS et Android.]({% image_buster /assets/img_archive/push_multiple_platform_message_selection_canvas.png %})

{:start="4"}
4. Sélectionnez **Confirm**. Après avoir sélectionné **Confirm**, vous ne pouvez plus modifier les plateformes ou les appareils sélectionnés.
5. Continuez la configuration de votre campagne ou de votre Canvas.

## Exécuter un test multivarié multi-plateforme {#running-a-multi-platform-multivariate-test}

Les tests multivariés sont pris en charge pour les campagnes multi-plateformes. Sélectionnez l'icône plus à côté du nom de la variante comme vous le feriez pour une campagne sur une seule plateforme. Pour les étapes de configuration, consultez [Créer des tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests).

Pour optimiser automatiquement vos variantes, consultez [Optimiser les tests A/B avec BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection).

![Tests multivariés multi-plateformes simplifiés]({% image_buster /assets/img_archive/push_multiple_platform_message_composer_multivariate.png %})

## Ce qu'il faut savoir {#things-to-know}

### Communication unifiée {#unified-messaging}
Dans l'onglet **Composer**, vous pouvez spécifier un titre, un message et un comportement au clic uniques pour l'ensemble de vos plateformes et appareils sélectionnés.

Le panneau d'aperçu affiche une approximation de l'apparence de votre message pour chaque plateforme. Bien qu'il puisse vous donner une bonne indication des limites de caractères que vous pourriez atteindre, n'oubliez pas de toujours tester vos messages sur un appareil réel avant d'envoyer votre Campaign.

![Vue d'édition unique avec un titre, un message et un champ de comportement au clic pour trois types de notifications push : iOS, Android et Web.]({% image_buster /assets/img_archive/push_multiple_platform_message_composer.png %})

### Ressources séparées {#separate-assets}
Dans la section **Ressources**, sélectionnez ou téléchargez les images que vous souhaitez afficher pour chaque plateforme. Gardez à l'esprit que les différents appareils ont des spécifications différentes pour les images et le nombre de caractères. Consultez [Formats de messages push et d'images]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats) pour obtenir de l'aide.

![Section Ressources de la vue d'édition unique avec des champs pour l'image de l'icône push, l'image de notification iOS, l'image de notification Android et l'image de notification Web.]({% image_buster /assets/img_archive/push_multiple_platform_message_composer_assets.png %}){:style="max-width:50%"}

### Type de notification {#notification-type}

Le type de notification est défini par défaut sur « Notification push standard » et ne peut pas être modifié. Si vous souhaitez créer un autre type de notification push, comme les Push Stories ou les images intégrées (Android), créez des Campaigns distinctes pour chaque type d'appareil.

### Paramètres spécifiques à l'appareil {#device-specific-settings}

Vous pouvez modifier les paramètres spécifiques à chaque plateforme dans l'éditeur. Cela inclut des paramètres tels que les [boutons d'action push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons), les canaux et groupes de notification, la TTL, la priorité d'affichage, les sons, et bien plus encore.

Pour plus d'informations sur les paramètres spécifiques à chaque appareil, consultez les collections d'articles suivantes :

- [Options iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios)
- [Options Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android)

### Push Stories

Les Push Stories sont disponibles sur plusieurs plateformes, uniquement sur Android et iOS. Si vous sélectionnez Web ou Kindle comme plateforme d'envoi, cette option n'est pas disponible.