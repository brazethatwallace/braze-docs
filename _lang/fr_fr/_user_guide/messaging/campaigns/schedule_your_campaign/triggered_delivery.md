---
nav_title: Livraison par événement
article_title: Livraison par événement
page_order: 1
page_type: reference
description: "Cet article de référence décrit comment déclencher l'envoi de campagnes après qu'un utilisateur a effectué une action spécifique."
tool: Campaigns
local_redirect:
  use-cases: '/docs/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#examples'

---

# Livraison par événement {#action-based-delivery}

> Les campagnes à livraison par événement, également appelées campagnes déclenchées par événement, sont très efficaces pour les messages transactionnels ou liés à des accomplissements. Au lieu d'envoyer votre campagne à des jours précis, vous pouvez déclencher l'envoi après qu'un utilisateur a effectué une action spécifique.

## Configurer une campagne déclenchée {#setting-up-a-triggered-campaign}

### Étape 1 : Sélectionner un événement déclencheur {#step-1-select-a-trigger-event}

Sélectionnez un événement déclencheur. Les événements sont organisés par catégorie et sont disponibles en fonction de votre espace de travail et des canaux activés.

- **eCommerce**
    - **Place Order**
    - **Perform Cart Updated Event**
    - **Perform Checkout Started Event**
    - **Perform Checkout Completed Event**
    - **Make Purchase**
- **General activity**
    - **Interact With Campaign**
    - **Interact With Step**
    - **Interact with Landing Page**
    - **Perform Conversion Event**
    - **Perform Custom Event**
    - **Perform Exception Event For Campaign**
    - **Start Session**
- **Inbound messaging**
    - **Send an SMS inbound message**
    - **Send a WhatsApp inbound message**
    - **Send a LINE inbound message**
- **Location**
    - **Enter a Location**
    - **Trigger a Geofence**
- **Profile updates**
    - **Add an Email Address**
    - **Change Custom Attribute Value**
    - **Update Subscription Status**
    - **Update Subscription Group Status**

Le groupe **eCommerce** répertorie également les événements eCommerce recommandés, tels que **Perform Product Viewed Event**, **Perform Order Cancelled Event** et **Perform Order Refunded Event**. Ces options utilisent **Perform Custom Event** avec le nom de l'événement prérempli.

Les campagnes de messages in-app prennent en charge un ensemble plus restreint de déclencheurs : **Make Purchase**, **Place Order**, **Start Session**, **Perform Custom Event** et **Interact With Campaign**. Pour les campagnes de messages in-app, **Interact With Campaign** couvre uniquement l'ouverture d'une notification push depuis n'importe quelle Campaign ou une Campaign spécifique. Cela n'inclut pas la liste d'interactions de Campaign suivante.

Pour les campagnes autres que les messages in-app, lorsque vous sélectionnez **Interact With Campaign**, **Interact With Step** ou **Interact with Landing Page**, choisissez l'interaction sur laquelle déclencher. Chacun de ces déclencheurs propose ses propres interactions, et les interactions disponibles dépendent de vos canaux activés.

{% details Interactions pour Interact With Campaign %}

- **View in-app message**
- **Click in-app message**
- **Click in-app message button 1**
- **Click in-app message button 2**
- **Submit in-app message survey**
- **Click email**
- **Open email**
- **Open email (machine opens)**
- **Open email (other opens)**
- **Click alias in email**
- **Clicked Alias in any campaign or canvas step**
- **Directly open push notification**
- **Click push notification button**
- **Click push story page**
- **Perform conversion event**
- **Receive email**
- **Receive push notification**
- **Receive webhook**
- **Receive SMS**
- **Click shortened SMS link**
- **View content card**
- **Click content card**
- **Dismiss content card**
- **View banner**
- **Click banner**
- **Dismiss banner**
- **Click tracked WhatsApp link**
- **Click tracked LINE link**
- **Click tracked KakaoTalk link**
- **Are enrolled in control group**

{% enddetails %}

{% details Interactions pour Interact With Step %}

- **View in-app message**
- **Start in-app message availability window**
- **Submit in-app message survey**
- **Click email**
- **Open email**
- **Open email (machine opens)**
- **Open email (other opens)**
- **Click alias in email**
- **Clicked Alias in any campaign or canvas step**
- **Directly open push notification**
- **Click push notification button**
- **Click push story page**
- **Receive email**
- **Receive push notification**
- **Receive webhook**
- **Receive SMS**
- **Click shortened SMS link**
- **View content card**
- **Click content card**
- **Dismiss content card**
- **View banner**
- **Click banner**
- **Dismiss banner**
- **Click tracked WhatsApp link**
- **Click tracked LINE link**
- **Click tracked KakaoTalk link**

{% enddetails %}

{% details Interactions pour Interact with Landing Page %}

- **Submit form**
- **Submit survey**

{% enddetails %}

Vous pouvez également affiner le filtrage des événements déclencheurs grâce aux [propriétés d'événement personnalisé]({{site.baseurl}}/user_guide/data/activation/events/custom_events) de Braze, ce qui permet de définir des propriétés d'événement personnalisables pour les événements personnalisés et les achats in-app. Cette fonctionnalité vous permet d'affiner davantage quels utilisateurs reçoivent un message en fonction des attributs spécifiques de l'événement personnalisé, offrant ainsi une personnalisation accrue des campagnes et une collecte de données plus sophistiquée.

Par exemple, supposons que nous ayons une Campaign avec un événement personnalisé de panier abandonné, davantage ciblée par le filtre de propriété « valeur du panier ». Cette Campaign n'atteint que les utilisateurs qui ont laissé entre 100 $ et 200 $ de marchandises dans leur panier.

![Campaign de panier abandonné filtrée par une propriété d'événement personnalisé pour une valeur de panier comprise entre 100 $ et 200 $.]({% image_buster /assets/img_archive/customEventProperties.png %})

{% alert note %}
L'événement déclencheur **Start Session** peut correspondre à la toute première ouverture de l'application par l'utilisateur si le Segment de votre Campaign s'applique aux nouveaux utilisateurs (par exemple, si votre Segment est composé d'utilisateurs sans aucune session).
{% endalert %}

N'oubliez pas que vous pouvez toujours envoyer une campagne déclenchée à un Segment d'utilisateurs spécifique, de sorte que les utilisateurs qui ne font pas partie du Segment ne reçoivent pas la Campaign même s'ils accomplissent l'événement déclencheur.

Concernant l'événement déclencheur lorsqu'un utilisateur ajoute une adresse e-mail à son profil, les règles suivantes s'appliquent :

- L'événement déclencheur se déclenche après la mise à jour de l'attribut du profil utilisateur. Cela signifie que l'évaluation des Segments et des filtres de la Campaign intervient après toute mise à jour d'attribut. C'est avantageux, car cela vous permet de configurer des filtres comme « l'adresse e-mail correspond à gmail.com » pour créer une campagne déclenchée qui n'envoie qu'aux utilisateurs Gmail et se déclenche dès qu'ils ajoutent leur adresse e-mail.
- L'événement déclencheur se déclenche lorsqu'une adresse e-mail est ajoutée à un profil utilisateur. Si vous avez plusieurs profils utilisateur créés avec la même adresse e-mail, la Campaign peut se déclencher plusieurs fois, une fois pour chaque profil utilisateur.

De plus, les messages in-app déclenchés respectent toujours les règles de distribution des messages in-app et apparaissent au début d'une session de l'application.

### Étape 2 : Sélectionner la durée du délai {#step-2-select-delay-length}

Sélectionnez le temps d'attente avant l'envoi de la Campaign après que les critères de déclenchement ont été remplis. Si la durée du délai choisie est supérieure à la durée d'envoi du message, aucun utilisateur ne reçoit la Campaign.

Les campagnes de messages in-app peuvent retarder la distribution après l'événement déclencheur de deux heures maximum (7 200 secondes). Les options de délai sont **Immediately** et **After a delay**. Pour un délai plus long, ajoutez une étape [Délai]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) avant une étape de message in-app dans un Canvas.

{% alert important %}
Braze utilise l'horodatage envoyé avec l'événement personnalisé pour évaluer le délai d'une campagne par événement. Si cet horodatage est antidaté, Braze peut considérer que le délai est déjà écoulé et envoyer le message immédiatement ou plus tôt que prévu. Pour éviter un timing de distribution involontaire, envoyez l'horodatage de l'événement personnalisé avec l'heure actuelle.
{% endalert %}

De plus, les utilisateurs qui accomplissent l'événement déclencheur après le lancement de votre Campaign sont les premiers à recevoir le message une fois le délai écoulé. Les utilisateurs qui ont accompli l'événement déclencheur avant le lancement de la Campaign ne sont pas éligibles pour la recevoir.

Vous pouvez également envoyer la Campaign un jour spécifique de la semaine en sélectionnant **On the next day of the week**, ou un nombre défini de jours dans le futur en sélectionnant **After a number of calendar days**. Vous pouvez aussi envoyer votre message en utilisant le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) au lieu de sélectionner manuellement une heure de distribution.

### Étape 3 : Sélectionner les événements d'exception {#step-3-select-exception-events}

Sélectionnez un événement d'exception qui disqualifie les utilisateurs de la réception de cette Campaign. Vous ne pouvez le faire que si votre message déclenché est envoyé après un délai. Les [événements d'exception]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria#exception-events) peuvent être un achat, le démarrage d'une session, la réalisation de l'un des [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) désignés de la Campaign, ou l'exécution d'un événement personnalisé.

Si un utilisateur accomplit l'événement déclencheur puis accomplit votre événement d'exception avant l'envoi du message en raison du délai, il ne reçoit pas la Campaign. Les utilisateurs qui ne reçoivent pas la Campaign en raison de l'événement d'exception sont automatiquement éligibles pour la recevoir à l'avenir, la prochaine fois qu'ils accomplissent l'événement déclencheur, même si vous n'avez pas choisi de rendre les utilisateurs [rééligibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).

Pour plus d'informations sur l'utilisation des événements d'exception, consultez les [exemples](#examples).

Si vous envoyez une Campaign avec un événement déclencheur qui correspond à l'événement d'exception, Braze annule la Campaign et replanifie automatiquement une nouvelle Campaign basée sur l'heure de distribution du message de l'événement d'exception. Par exemple, si votre premier événement déclencheur commence à cinq minutes et que l'événement d'exception commence à 10 minutes, vous vous appuyez sur les 10 minutes de l'événement d'exception comme heure officielle de distribution du message de la Campaign.

{% alert note %}
Vous ne pouvez pas définir un « démarrage de session » à la fois comme événement déclencheur et comme événement d'exception pour une Campaign. Cependant, vous pouvez toujours sélectionner n'importe quel autre événement personnalisé en dehors de cette option.
{% endalert %}

### Étape 4 : Définir la durée {#step-4-assign-duration}

Définissez la durée de la Campaign en spécifiant une heure de début et une heure de fin facultative.

Si un utilisateur accomplit un événement déclencheur pendant la période spécifiée mais se qualifie pour le message en dehors de cette période en raison d'un délai planifié, il ne reçoit pas la Campaign. Par conséquent, si vous définissez un délai plus long que la période du message, aucun utilisateur ne reçoit votre Campaign. De plus, vous pouvez choisir d'envoyer le message dans les [fuseaux horaires locaux]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#local-time-zone-campaigns) des utilisateurs.

### Étape 5 : Sélectionner la plage horaire {#step-5-select-time-frame}

Indiquez si l'utilisateur reçoit la Campaign pendant une portion spécifique de la journée. Si vous attribuez une plage horaire au message et que l'utilisateur accomplit l'événement déclencheur en dehors de la plage horaire, ou que le délai du message lui fait manquer la plage horaire, alors par défaut, l'utilisateur ne reçoit pas votre message.

Dans le cas où un utilisateur accomplit l'événement déclencheur dans la plage horaire, mais que le délai du message fait sortir l'utilisateur de la plage horaire, vous pouvez cocher la case **Send at the next available time if the delivery time falls outside the specified portion of the day** pour que ces utilisateurs reçoivent tout de même la Campaign.

Si un utilisateur ne reçoit pas le message parce qu'il a manqué la plage horaire, il reste néanmoins éligible pour le recevoir la prochaine fois qu'il accomplit l'événement déclencheur, même si vous n'avez pas choisi de rendre les utilisateurs [rééligibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility). Si vous choisissez de rendre les utilisateurs rééligibles, ils peuvent recevoir la Campaign à chaque fois qu'ils accomplissent l'événement déclencheur, à condition de se qualifier pendant la plage horaire spécifiée.

Si vous avez également attribué une durée à la Campaign, l'utilisateur doit se qualifier à la fois dans la durée et dans la portion spécifique de la journée pour recevoir le message.

### Étape 6 : Définir la rééligibilité {#step-6-determine-re-eligibility}

Déterminez si les utilisateurs peuvent devenir [rééligibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) pour la Campaign. Si vous autorisez les utilisateurs à devenir rééligibles, vous pouvez spécifier un délai avant que l'utilisateur puisse recevoir la Campaign à nouveau. Cela évite que vos campagnes déclenchées ne deviennent trop intrusives.

## Exemples {#examples}

Les campagnes déclenchées sont très efficaces pour les messages transactionnels ou liés à des accomplissements.

Les campagnes transactionnelles incluent les messages envoyés après qu'un utilisateur a effectué un achat ou ajouté un article à son panier. Ce dernier cas est un excellent exemple de Campaign qui bénéficie d'un événement d'exception. Imaginons que votre Campaign rappelle aux utilisateurs les articles dans leur panier qu'ils n'ont pas encore achetés. L'événement d'exception, dans ce cas, est l'achat par l'utilisateur des produits présents dans son panier. Pour les campagnes basées sur les accomplissements, vous pouvez envoyer un message cinq minutes après qu'un utilisateur a effectué une conversion ou terminé un niveau de jeu.

De plus, lors de la création de campagnes d'accueil, vous pouvez déclencher l'envoi de messages après qu'un utilisateur s'est inscrit ou a configuré un compte. Échelonner les messages pour qu'ils soient envoyés à différents jours suivant l'inscription vous permet de créer un processus d'onboarding complet.

## Questions fréquemment posées {#frequently-asked-questions}

### Quel est le délai maximum après un déclencheur pour les campagnes de messages in-app ? {#what-is-the-maximum-delay-after-a-trigger-for-in-app-message-campaigns}

Deux heures (7 200 secondes). Pour les options de délai disponibles et la manière de définir une attente plus longue, consultez l'[Étape 2 : sélectionner la durée du délai](#step-2-select-delay-length).

### Pourquoi un utilisateur n'a-t-il pas reçu ma Campaign déclenchée ? {#why-did-a-user-not-receive-my-triggered-campaign}

L'une des raisons suivantes peut empêcher un utilisateur ayant effectué l'événement déclencheur de recevoir la Campaign :

- L'utilisateur a effectué l'événement d'exception avant que le délai ne se soit entièrement écoulé.
- Une [logique `abort_message`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) Liquid a été utilisée et le message a été abandonné en fonction de la logique ou des règles `abort_message`.
- Le délai a fait en sorte que l'utilisateur soit devenu éligible à recevoir la Campaign après la fin de la durée.
- Le délai a fait en sorte que l'utilisateur soit devenu éligible à recevoir la Campaign en dehors de la portion de journée spécifiée.
- L'utilisateur a déjà reçu la Campaign (y compris l'attribution via des identifiants de canal partagés — par exemple, s'il partage un e-mail avec quelqu'un qui l'a reçu, ouvert ou cliqué), et les utilisateurs ne redeviennent pas éligibles.
- Bien que les utilisateurs soient rééligibles pour recevoir la Campaign, ils ne peuvent la redéclencher qu'après un certain laps de temps, et ce laps de temps ne s'est pas encore écoulé.

La [segmentation]({{site.baseurl}}/user_guide/audience/segments) d'une Campaign déclenchée en fonction des données utilisateur enregistrées au moment de l'événement peut provoquer une [condition de concurrence]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions). Cela se produit lorsque l'attribut utilisateur sur lequel la Campaign est segmentée est modifié, mais que le changement n'a pas encore été traité pour l'utilisateur au moment de l'envoi de la Campaign. Étant donné que les Campaigns vérifient l'appartenance au Segment à l'entrée, cela peut conduire l'utilisateur à ne pas recevoir la Campaign.

Par exemple, imaginons que vous souhaitiez envoyer une Campaign déclenchée par un événement aux utilisateurs masculins qui viennent de s'inscrire. Lorsque l'utilisateur s'inscrit, vous enregistrez un événement personnalisé `registration` et définissez simultanément l'attribut `gender` de l'utilisateur. L'événement peut déclencher la Campaign avant que Braze n'ait traité le genre de l'utilisateur, l'empêchant ainsi de recevoir la Campaign.

En tant que bonne pratique, assurez-vous que l'attribut sur lequel la Campaign est segmentée est envoyé aux serveurs Braze avant l'événement. Si ce n'est pas possible, le meilleur moyen de garantir la distribution est d'utiliser des [propriétés d'événement personnalisé]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) pour rattacher les propriétés utilisateur pertinentes à l'événement et d'appliquer un filtre de propriété pour la propriété d'événement spécifique au lieu d'un filtre de segmentation. Pour notre exemple, ajoutez une propriété `gender` à l'événement personnalisé `registration` afin que Braze dispose des données nécessaires lorsque votre Campaign est déclenchée.

De plus, si une Campaign est basée sur une action et comporte un délai, vous pouvez cocher l'option **Re-evaluate segment membership at send-time** pour vous assurer que les utilisateurs font toujours partie de l'audience cible lorsque le message est envoyé.

#### Évaluation des critères d'audience {#audience-criteria-evaluation}

Pour les Campaigns qui impliquent un délai avant l'envoi (y compris la limitation du débit, le fuseau horaire local, le timing intelligent ou une planification déclenchée), le moment où le Segment est réévalué dépend du type de Campaign et de ses paramètres.

Dans les Campaigns basées sur une action avec un délai, si vous sélectionnez **Re-evaluate segment membership at send-time**, les utilisateurs sont réévalués avant l'envoi du message, de sorte que seuls les utilisateurs qui remplissent encore les critères du Segment au moment de l'envoi reçoivent le message.

Si votre Campaign est déclenchée par un événement personnalisé spécifique et que vous sélectionnez un Segment comme audience, les utilisateurs doivent effectuer le même événement personnalisé pour être inclus dans le Segment. Cela signifie que les utilisateurs doivent faire partie de l'audience avant qu'une Campaign basée sur une action puisse être déclenchée. Le flux de travail général d'une Campaign déclenchée est le suivant :

1. **Rejoindre l'audience :** Lorsqu'un utilisateur effectue l'événement personnalisé, il est ajouté à l'audience cible de la Campaign.
2. **Déclencher l'e-mail :** Un utilisateur doit effectuer à nouveau l'événement personnalisé pour déclencher l'e-mail, car il doit faire partie de l'audience avant que l'e-mail puisse être envoyé.

Nous recommandons soit de modifier l'audience cible pour inclure tous les utilisateurs, soit de vérifier que les utilisateurs censés effectuer l'événement font déjà partie de l'audience de la Campaign pour que le message soit déclenché.

![Capture d'écran liée à l'évaluation des critères d'audience.]({% image_buster /assets/img_archive/reevaluate_segment_membership.png %})

#### Résolution des problèmes liés aux événements personnalisés {#troubleshooting-custom-events}

Commencez par confirmer que l'événement personnalisé est bien transmis à Braze. Accédez à **Analytics** > **Custom Events Report**, puis sélectionnez l'événement personnalisé et la plage de dates concernés. Si l'événement ne s'affiche pas, vérifiez qu'il est correctement configuré et que l'utilisateur a effectué l'action correcte.

Si l'événement personnalisé s'affiche, poursuivez la résolution des problèmes en procédant comme suit :

- Consultez le téléchargement du profil de l'utilisateur pour confirmer qu'il a déclenché l'événement et quand il l'a fait. Si l'événement a été déclenché, comparez l'horodatage du déclenchement de l'événement avec le moment où la Campaign a été mise en ligne. L'événement a peut-être été déclenché avant la mise en ligne de la Campaign.
- Examinez les journaux des modifications de la Campaign et de tout Segment utilisé dans le ciblage pour déterminer si l'utilisateur était dans le Segment lorsque son événement personnalisé a été déclenché. S'il n'était pas dans le Segment, il n'aurait pas reçu la Campaign.
- Vérifiez si l'utilisateur a été intégré dans un groupe de contrôle via la segmentation et a par conséquent été empêché de recevoir la Campaign.
- S'il existe un délai planifié, vérifiez si l'événement personnalisé de l'utilisateur a été déclenché avant le délai. Si l'événement a été déclenché avant le délai, l'utilisateur n'aurait pas reçu la Campaign.

{% alert note %}
Les messages in-app ne peuvent être déclenchés que par des événements envoyés via le SDK, et non par la REST API.
{% endalert %}

### Quand les Campaigns basées sur une action évaluent-elles l'appartenance à l'audience ? {#when-do-action-based-campaigns-evaluate-audience-membership}

Braze évalue l'appartenance à l'audience lorsqu'il traite l'événement déclencheur, avant l'envoi du message. Par défaut, Braze vérifie si l'utilisateur correspond à l'audience cible au moment de la mise en file d'attente. Si la Campaign comporte un délai, vous pouvez sélectionner **Re-evaluate segment membership at send-time** pour vérifier à nouveau les critères d'audience juste avant l'envoi — par exemple, lorsqu'un utilisateur pourrait effectuer l'action de déclenchement puis quitter l'audience avant la fin de l'envoi.

Pour plus d'informations, consultez [Évaluation des critères d'audience](#audience-criteria-evaluation).