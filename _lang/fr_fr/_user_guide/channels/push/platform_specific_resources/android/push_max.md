---
nav_title: Push Max
article_title: Push Max
page_type: reference
description: "Push Max amplifie les notifications push Android en suivant les notifications push échouées et en renvoyant la notification push lorsque l'utilisateur est plus susceptible de la recevoir."

permalink: /user_guide/channels/push/platform_specific_resources/android/push_max/
platform: Android
channel:
  - Push

---

# Push Max

> Découvrez Push Max et comment vous pouvez utiliser cette fonctionnalité pour potentiellement améliorer la livrabilité des notifications push Android vers les [appareils OEM chinois]({{site.baseurl}}/user_guide/channels/push/best_practices/chinese_push_deliverability/).

## Qu'est-ce que Push Max ? {#what-is-push-max}

Push Max amplifie les notifications push Android en suivant les notifications push échouées et en renvoyant la notification push lorsque l'utilisateur est plus susceptible de la recevoir.

Certains appareils Android fabriqués par des fabricants d'équipements d'origine (OEM) chinois, tels que Xiaomi, OPPO et Vivo, utilisent un système robuste d'optimisation de la batterie pour prolonger l'autonomie. Ce comportement peut avoir pour conséquence involontaire d'arrêter le traitement des applications en arrière-plan, ce qui réduit la livrabilité des notifications push sur ces appareils si l'application n'est pas au premier plan. Cette situation se produit le plus souvent sur les marchés Asie-Pacifique (APAC).

## Disponibilité {#availability}

- Disponible uniquement pour les notifications push Android
- Non pris en charge pour les messages déclenchés par une action ou par l'API
- Non pris en charge lorsque l'option [envoyer uniquement au dernier appareil utilisé par l'utilisateur]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/#device-options) est sélectionnée

## Conditions préalables {#prerequisites}

Les notifications push envoyées à l'aide de Push Max ne seront distribuées qu'aux appareils disposant au minimum de la [version SDK minimale]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions) suivante :

{% sdk_min_versions android:29.0.1 %}

## Utiliser Push Max {#using-push-max}

{% tabs %}
{% tab Campaigns %}

Pour utiliser Push Max dans votre Campaign :

1. Créez une Campaign push.
2. Sélectionnez **Android Push** comme plateforme.
3. Accédez à l'étape **Schedule Delivery**.
4. Sélectionnez **Send using Push Max**.

![Section Android Push Deliverability de l'étape Schedule Delivery avec l'option « Send using Push Max ».]({% image_buster /assets/img_archive/push_max_campaigns.png %})

{% endtab %}
{% tab Canvas %}

Pour utiliser Push Max dans votre Canvas :

1. Ajoutez une étape Message à votre Canvas.
2. Sélectionnez **Android Push** comme plateforme.
3. Accédez à l'onglet **Delivery Settings**.
4. Sélectionnez **Send using Push Max**.

![Onglet Delivery Settings d'une étape de message Android Push avec l'option « Send using Push Max ».]({% image_buster /assets/img_archive/push_max_canvas.png %})

{% endtab %}
{% endtabs %}

Les deux fonctionnalités suivantes, le timing intelligent et la durée de vie, peuvent être utilisées conjointement avec Push Max pour potentiellement améliorer la livrabilité de vos notifications push Android.

### Timing intelligent {#intelligent-timing}

Push Max fonctionne de manière optimale lorsque le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/) est activé. Le timing intelligent peut calculer et envoyer la notification push au moment où l'utilisateur est le plus susceptible d'utiliser l'application et où la notification a le plus de chances d'être distribuée.

### Durée de vie (TTL) {#time-to-live-ttl}

La durée de vie (TTL) peut suivre les notifications push échouées vers Firebase Cloud Messaging (FCM) et réessayer l'envoi de la notification lorsque l'utilisateur est susceptible de la recevoir.

Par défaut, la durée de vie est définie sur 28 jours, ce qui correspond au maximum. Vous pouvez diminuer la durée de vie par défaut pour tous les nouveaux messages push Android depuis **Settings** > **Workspace Settings** > **Push Settings**, ou vous pouvez configurer le nombre de jours par message dans l'onglet **Settings** lors de la composition d'une notification push Android.

![Champ Durée de vie défini sur 28 jours.]({% image_buster /assets/img_archive/time_to_live.png %}){: style="max-width:60%"}

## Informations importantes {#things-to-know}

### Codes de promotion {#promotion-codes}

Nous vous recommandons de ne pas utiliser les [codes de promotion]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/) Braze dans les messages où Push Max est activé.

En effet, les codes de promotion sont uniques. Si une notification push contenant un code de promotion échoue à la distribution, lorsque cette notification est renvoyée grâce à Push Max, un nouveau code de promotion sera envoyé. Cela peut entraîner une consommation de codes de promotion plus rapide que prévu.

### Propriétés d'événement et propriétés d'entrée Canvas {#canvas-event-properties-and-entry-properties}

Push Max peut ne pas fonctionner comme prévu si vous incluez des références Liquid aux [propriétés d'entrée Canvas ou propriétés d'événement]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/) dans votre message. En effet, les propriétés d'entrée et d'événement ne sont pas disponibles lorsque Push Max tente de renvoyer le message.