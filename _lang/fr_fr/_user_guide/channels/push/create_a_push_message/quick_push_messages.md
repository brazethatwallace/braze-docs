---
nav_title: "Messages push rapides"
article_title: "Messages push rapides"
alias: "/quick_push/"
description: "Cet article décrit les points à connaître lors de la création d'une campagne push ou d'un Canvas utilisant l'expérience d'édition push rapide."
page_order: 4
---

# Messages push rapides {#quick-push-messages}

> Cet article décrit ce qu'il faut savoir lorsque vous créez une campagne push ou un Canvas utilisant l'expérience d'édition push rapide pour cibler plusieurs plateformes et appareils depuis un seul compositeur.

Lorsque vous créez une campagne push ou un Canvas dans Braze, vous pouvez sélectionner plusieurs plateformes et appareils pour rédiger un seul message pour toutes les plateformes dans une expérience d'édition unique appelée push rapide.

## Cas d'utilisation {#use-cases}

Cette expérience d'édition est idéale pour les cas d'utilisation suivants :

- Les campagnes push mobiles et les étapes de message Canvas qui doivent être envoyées à plusieurs types d'appareils (comme iOS et Android).
- Les notifications push urgentes qui doivent cibler plusieurs plateformes rapidement et avec précision, lorsque le contenu est identique sur toutes les plateformes (comme les actualités de dernière minute ou les mises à jour de matchs en direct).

## Créer une campagne ou un Canvas push rapide {#creating-a-quick-push-campaign-or-canvas}

Pour créer une campagne ciblant plusieurs plateformes et appareils :

1. Créez une campagne ou ajoutez une [étape de message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) à un Canvas.
2. Sélectionnez **Push notification**.
3. Sélectionnez les plateformes souhaitées (Mobile, Web, Kindle) et les appareils mobiles (iOS, Android). Si vous sélectionnez plusieurs appareils, le test multivarié ne sera pas disponible pour votre campagne.

### Sélection des plateformes pour une campagne {#selecting-platforms-for-a-campaign}
![Options pour sélectionner plusieurs plateformes pour une campagne push, telles que Mobile, Web et Kindle, et plusieurs appareils, tels qu'iOS et Android.]({% image_buster /assets/img_archive/quick_push_1.png %})

### Sélection des plateformes pour une étape Canvas {#selecting-platforms-for-a-canvas-step}
![Options pour sélectionner plusieurs plateformes pour une étape de message push, telles que Mobile, Web et Kindle, et plusieurs appareils, tels qu'iOS et Android.]({% image_buster /assets/img_archive/quick_push_4.png %})

{:start="4"}
4. Sélectionnez **Confirmer**. Après avoir sélectionné **Confirmer**, vous ne pourrez plus modifier les plateformes ou appareils sélectionnés.
5. Continuez la configuration de votre campagne ou Canvas.

Votre compositeur aura un aspect légèrement différent de l'habitude. Poursuivez votre lecture pour découvrir ce qui change.

### Ce qui change {#whats-different}

Dans l'onglet **Rédiger**, vous pouvez spécifier un titre, un message et un comportement au clic uniques pour toutes les plateformes et appareils que vous avez choisis.

Le volet de prévisualisation affiche une approximation de l'apparence de votre message pour chaque plateforme. Bien qu'il puisse vous donner une bonne indication des limites de caractères que vous pourriez atteindre, pensez toujours à tester vos messages sur un appareil réel avant d'envoyer votre campagne.

![Vue d'édition unique avec un titre, un message et un champ de comportement au clic pour trois types de push : iOS, Android et Web.]({% image_buster /assets/img_archive/quick_push_2.png %})

Dans la section **Actifs**, sélectionnez ou téléchargez les images que vous souhaitez afficher pour chaque plateforme. Gardez à l'esprit que les différents appareils ont des spécifications différentes pour les images et le nombre de caractères. Consultez [Formats des messages push et des images]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats/) pour obtenir de l'aide.

![Section Actifs de la vue d'édition unique avec des champs pour l'image de l'icône push, l'image de notification iOS, l'image de notification Android et l'image de notification Web.]({% image_buster /assets/img_archive/quick_push_3.png %}){:style="max-width:50%"}

Ensuite, terminez la configuration de votre campagne push comme d'habitude. Consultez [Créer une campagne push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/) pour plus de détails.

## Points à connaître {#things-to-know}

### Type de notification {#notification-type}

Le type de notification est défini par défaut sur « Push standard » et ne peut pas être modifié. Si vous souhaitez créer un autre type de push, comme Push Stories ou Image intégrée (Android), créez des campagnes distinctes pour chaque type d'appareil.

### Test multivarié {#multivariate-testing}

Si vous sélectionnez plusieurs appareils pour les plateformes mobiles, comme iOS et Android, le test multivarié ne sera pas disponible pour votre campagne. Si vous souhaitez effectuer un test multivarié, créez des campagnes distinctes pour chaque type d'appareil.

### Paramètres spécifiques aux appareils {#device-specific-settings}

Vous pouvez modifier les paramètres spécifiques à chaque plateforme dans l'éditeur. Cela inclut des paramètres tels que les [boutons d'action push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons/), les canaux et groupes de notification, le TTL, la priorité d'affichage, les sons, et plus encore.

Notez que les boutons d'action push ne sont pas pris en charge lorsque vous ciblez à la fois iOS et Android avec des campagnes push rapides. Pour plus d'informations sur les paramètres spécifiques aux appareils, consultez les collections d'articles suivantes :

- [Options iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/)
- [Options Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/)