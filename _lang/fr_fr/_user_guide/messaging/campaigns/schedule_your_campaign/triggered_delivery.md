---
nav_title: Livraison par événement
article_title: Livraison par événement
page_order: 1
page_type: reference
description: "Cet article de référence décrit comment déclencher l'envoi de campagnes après qu'un utilisateur a effectué une action spécifique."
tool: Campaigns
---

# Livraison par événement {#action-based-delivery}

> Les campagnes à livraison par événement, également appelées campagnes déclenchées par événement, sont très efficaces pour les messages transactionnels ou liés à des accomplissements. Au lieu d'envoyer votre campagne à des jours précis, vous pouvez déclencher l'envoi après qu'un utilisateur a effectué une action spécifique.

## Configurer une campagne déclenchée {#setting-up-a-triggered-campaign}

### Étape 1 : Sélectionner un événement déclencheur {#step-1-select-a-trigger-event}

Sélectionnez un événement déclencheur. Il peut s'agir de l'un des éléments suivants :
- Passer une commande
- Démarrer une session
- Effectuer un événement personnalisé
- Effectuer l'événement de conversion principal de la campagne
- Ajouter une adresse e-mail à un profil utilisateur
- Modifier la valeur d'un attribut personnalisé
- Mettre à jour un statut d'abonnement
- Mettre à jour un statut du groupe d'abonnement
- Interagir avec d'autres campagnes
    - Voir un message in-app
    - Cliquer sur un message in-app
    - Cliquer sur les boutons d'un message in-app
    - Cliquer sur un e-mail
    - Cliquer sur un alias dans un e-mail
    - Cliquer sur un alias dans n'importe quelle Campaign ou étape du Canvas
    - Ouvrir un e-mail
    - Ouvrir un e-mail (ouvertures automatiques)
    - Ouvrir un e-mail (autres ouvertures)
    - Ouvrir directement une notification push
    - Cliquer sur un bouton de notification push
    - Cliquer sur une page Push Stories
    - Effectuer un événement de conversion
    - Recevoir un e-mail
    - Recevoir un SMS
    - Cliquer sur un lien SMS raccourci
    - Recevoir une notification push
    - Recevoir un webhook
    - Être inscrit dans un groupe de contrôle
    - Voir une Content Card
    - Cliquer sur une Content Card
    - Rejeter une Content Card
- Entrer dans un emplacement
- Effectuer l'événement d'exception d'une autre campagne
- Interagir avec une étape du Canvas
- Déclencher un géorepérage
- Envoyer un message SMS entrant
- Envoyer un message WhatsApp entrant

Vous pouvez également affiner le filtrage des événements déclencheurs grâce aux [propriétés d'événement personnalisé]({{site.baseurl}}/user_guide/data/activation/events/custom_events) de Braze, ce qui permet de définir des propriétés d'événement personnalisables pour les événements personnalisés et les achats in-app. Cette fonctionnalité vous permet de cibler plus précisément les utilisateurs qui recevront un message en fonction des attributs spécifiques de l'événement personnalisé, offrant ainsi une personnalisation plus poussée des campagnes et une collecte de données plus sophistiquée.

Par exemple, supposons que nous ayons une campagne avec un événement personnalisé de panier abandonné, ciblée davantage par le filtre de propriété « valeur du panier ». Cette campagne n'atteindra que les utilisateurs ayant laissé entre 100 $ et 200 $ de produits dans leur panier.

![Campagne de panier abandonné filtrée par une propriété d'événement personnalisé pour une valeur de panier comprise entre 100 $ et 200 $.]({% image_buster /assets/img_archive/customEventProperties.png %})

{% alert note %}
L'événement déclencheur « démarrage de session » peut correspondre à la toute première ouverture de l'application par l'utilisateur si le Segment de votre campagne s'applique aux nouveaux utilisateurs (par exemple, si votre Segment est composé d'utilisateurs sans aucune session).
{% endalert %}

Gardez à l'esprit que vous pouvez toujours envoyer une campagne déclenchée à un Segment spécifique d'utilisateurs. Les utilisateurs ne faisant pas partie du Segment ne recevront donc pas la campagne, même s'ils effectuent l'événement déclencheur.

En ce qui concerne l'événement déclencheur lié à l'ajout d'une adresse e-mail au profil d'un utilisateur, les règles suivantes s'appliquent :

- L'événement déclencheur sera déclenché après la mise à jour de l'attribut du profil utilisateur. Cela signifie que l'évaluation des Segments et des filtres de la campagne aura lieu après toute mise à jour des attributs. C'est un avantage car cela vous permet de configurer des filtres tels que « l'adresse e-mail correspond à gmail.com » pour créer une campagne déclenchée qui n'envoie qu'aux utilisateurs Gmail et se déclenche dès qu'ils ajoutent leur adresse e-mail.
- L'événement déclencheur se déclenchera lorsqu'une adresse e-mail est ajoutée à un profil utilisateur. Si vous avez plusieurs profils utilisateur créés avec la même adresse e-mail, la campagne peut se déclencher plusieurs fois, une fois pour chaque profil utilisateur.

De plus, les messages in-app déclenchés respectent toujours les règles de distribution des messages in-app et apparaissent au début d'une session de l'application.

![Planification de distribution d'une campagne par événement montrant les options de configuration de l'événement déclencheur.]({% image_buster /assets/img_archive/schedule_triggered1.png %})

### Étape 2 : Sélectionner la durée du délai {#step-2-select-delay-length}

Sélectionnez le temps d'attente avant l'envoi de la campagne une fois les critères de déclenchement remplis. Si la durée du délai choisie est plus longue que la durée d'envoi du message, aucun utilisateur ne recevra la campagne.

Les campagnes de messages in-app peuvent retarder la distribution après l'événement déclencheur d'un maximum de deux heures (7 200 secondes). Les options de délai sont **Immédiatement** et **Après un délai**. Pour une attente plus longue, ajoutez une étape [Délai]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) avant une étape de message in-app dans un Canvas.

{% alert important %}
Braze utilise l'horodatage envoyé avec l'événement personnalisé pour évaluer le délai d'une campagne par événement. Si cet horodatage est antidaté, Braze peut considérer que le délai est déjà écoulé et envoyer le message immédiatement ou plus tôt que prévu. Pour éviter tout problème de timing de distribution, envoyez l'horodatage de l'événement personnalisé avec l'heure actuelle.
{% endalert %}

De plus, les utilisateurs qui effectuent l'événement déclencheur après le lancement de votre campagne seront les premiers à recevoir le message une fois le délai écoulé. Les utilisateurs ayant effectué l'événement déclencheur avant le lancement de la campagne ne seront pas éligibles pour la recevoir.

![Capture d'écran liée à l'étape 2 : sélectionner la durée du délai.]({% image_buster /assets/img_archive/schedule_triggered22.png %})

Vous pouvez également choisir d'envoyer la campagne un jour spécifique de la semaine (en choisissant « le prochain » puis en sélectionnant un jour) ou un nombre spécifique de jours (en sélectionnant « dans ») dans le futur. Vous pouvez aussi choisir d'envoyer votre message en utilisant la fonctionnalité de [Timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) au lieu de sélectionner manuellement un horaire de distribution.

![Vous pouvez également choisir d'envoyer la campagne un jour spécifique de la semaine ou un nombre spécifique de jours dans le futur. Vous pouvez aussi utiliser la fonctionnalité de Timing intelligent au lieu de sélectionner manuellement un horaire de distribution.]({% image_buster /assets/img_archive/schedule_triggered7.png %})
![Vous pouvez également choisir d'envoyer la campagne un jour spécifique de la semaine ou un nombre spécifique de jours dans le futur. Vous pouvez aussi utiliser la fonctionnalité de Timing intelligent au lieu de sélectionner manuellement un horaire de distribution.]({% image_buster /assets/img_archive/schedule_triggered8.png %})

### Étape 3 : Sélectionner les événements d'exception {#step-3-select-exception-events}

Sélectionnez un événement d'exception qui rendra les utilisateurs inéligibles à la réception de cette campagne. Vous ne pouvez le faire que si votre message déclenché est envoyé après un délai. Les [événements d'exception]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria#exception-events) peuvent être un achat, le démarrage d'une session, l'exécution de l'un des [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) désignés pour la campagne, ou l'exécution d'un événement personnalisé. Si un utilisateur effectue l'événement déclencheur puis effectue votre événement d'exception avant l'envoi du message en raison du délai, il ne recevra pas la campagne. Les utilisateurs ne recevant pas la campagne en raison de l'événement d'exception seront automatiquement éligibles pour la recevoir à l'avenir, la prochaine fois qu'ils effectueront l'événement déclencheur, même si vous n'avez pas choisi de rendre les utilisateurs [rééligibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).

![Sélectionnez un événement d'exception qui rendra les utilisateurs inéligibles à la réception de cette campagne. Les événements d'exception peuvent être un achat, le démarrage d'une session, l'exécution de l'un des événements de conversion désignés, ou l'exécution d'un événement personnalisé.]({% image_buster /assets/img_archive/schedule_triggered32.png %})

Vous pouvez en apprendre davantage sur l'utilisation des événements d'exception dans notre section sur les [cas d'usage]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#use-cases).

> Si vous envoyez une campagne avec un événement déclencheur qui correspond à l'événement d'exception, Braze annulera la campagne et replanifiera automatiquement une nouvelle campagne en fonction de l'horaire de distribution du message de l'événement d'exception. Par exemple, si votre premier événement déclencheur commence à cinq minutes et que l'événement d'exception commence à 10 minutes, l'horaire de distribution officiel de la campagne sera celui de l'événement d'exception, soit 10 minutes.

{% alert note %}
Vous ne pouvez pas définir un « démarrage de session » comme événement déclencheur et événement d'exception pour une même campagne. Cependant, vous avez toujours la possibilité de sélectionner n'importe quel autre événement personnalisé en dehors de cette option.
{% endalert %}

### Étape 4 : Définir la durée {#step-4-assign-duration}

Définissez la durée de la campagne en spécifiant une heure de début et une heure de fin facultative.

![Capture d'écran liée à l'étape 4 : définir la durée.]({% image_buster /assets/img_archive/schedule_triggered43.png %})

Si un utilisateur effectue un événement déclencheur pendant la période spécifiée mais devient éligible au message en dehors de cette période en raison d'un délai planifié, il ne recevra pas la campagne. Par conséquent, si vous définissez un délai plus long que la durée du message, aucun utilisateur ne recevra votre campagne. De plus, vous pouvez choisir d'envoyer le message dans les [fuseaux horaires locaux]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#local-time-zone-campaigns) des utilisateurs.

### Étape 5 : Sélectionner la plage horaire {#step-5-select-time-frame}

Sélectionnez si l'utilisateur recevra la campagne pendant une portion spécifique de la journée. Si vous attribuez une plage horaire au message et que l'utilisateur effectue l'événement déclencheur en dehors de cette plage ou que le délai du message lui fait manquer cette plage, alors par défaut, l'utilisateur ne recevra pas votre message.

![Sélectionnez si l'utilisateur recevra la campagne pendant une portion spécifique de la journée. Si vous attribuez une plage horaire au message et que l'utilisateur effectue l'événement déclencheur en dehors de cette plage ou que le délai du message lui fait manquer cette plage, alors par défaut, l'utilisateur ne recevra pas votre message.]({% image_buster /assets/img_archive/schedule_triggered5.png %})

Dans le cas où un utilisateur effectue l'événement déclencheur dans la plage horaire, mais que le délai du message le fait sortir de cette plage, vous pouvez cocher la case suivante pour que ces utilisateurs reçoivent tout de même la campagne.

![Capture d'écran liée à l'étape 5 : sélectionner la plage horaire.]({% image_buster /assets/img_archive/schedule_triggered_next_available.png %})

Si un utilisateur ne reçoit pas le message parce qu'il a manqué la plage horaire, il sera tout de même éligible pour le recevoir la prochaine fois qu'il effectuera l'événement déclencheur, même si vous n'avez pas choisi de rendre les utilisateurs [rééligibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility). Si vous choisissez de rendre les utilisateurs rééligibles, ils pourront recevoir la campagne à chaque fois qu'ils effectueront l'événement déclencheur, à condition qu'ils soient éligibles pendant la plage horaire spécifiée.

Si vous avez également attribué une durée à la campagne, l'utilisateur doit être éligible à la fois pendant la durée et pendant la portion spécifique de la journée pour recevoir le message.

### Étape 6 : Déterminer la rééligibilité {#step-6-determine-re-eligibility}

Déterminez si les utilisateurs peuvent devenir [rééligibles]({% image_buster /assets/img_archive/ReEligible.png %}) pour la campagne. Si vous autorisez les utilisateurs à devenir rééligibles, vous pouvez spécifier un délai avant que l'utilisateur puisse recevoir la campagne à nouveau. Cela évitera que vos campagnes déclenchées ne deviennent trop intrusives.

![Capture d'écran liée à l'étape 6 : déterminer la rééligibilité.]({% image_buster /assets/img_archive/schedule_triggered6.png %})

## Cas d'usage {#use-cases}

Les campagnes déclenchées sont très efficaces pour les messages transactionnels ou liés à des accomplissements.

Les campagnes transactionnelles incluent les messages envoyés après qu'un utilisateur a effectué un achat ou ajouté un article à son panier. Ce dernier cas est un excellent exemple de Campaign qui bénéficierait d'un événement d'exception. Imaginons que votre Campaign rappelle aux utilisateurs les articles dans leur panier qu'ils n'ont pas encore achetés. L'événement d'exception, dans ce cas, serait l'achat par l'utilisateur des produits dans son panier. Pour les campagnes basées sur les accomplissements, vous pouvez envoyer un message 5 minutes après que l'utilisateur a effectué une conversion ou terminé un niveau de jeu.

De plus, lors de la création de campagnes d'accueil, vous pouvez déclencher l'envoi de messages après que l'utilisateur s'est inscrit ou a configuré un compte. Échelonner les messages pour qu'ils soient envoyés à différents jours suivant l'inscription vous permet de créer un processus d'onboarding complet.

## Questions fréquemment posées {#frequently-asked-questions}

### Quel est le délai maximum après un déclencheur pour les campagnes de messages in-app ? {#what-is-the-maximum-delay-after-a-trigger-for-in-app-message-campaigns}

Les campagnes de messages in-app peuvent retarder la distribution après l'événement déclencheur jusqu'à deux heures (7 200 secondes). Les options de délai sont **Immédiatement** et **Après un délai**. Pour une attente plus longue, ajoutez une étape [Délai]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) avant une étape de message in-app dans un Canvas.

### Pourquoi un utilisateur n'a-t-il pas reçu ma campagne déclenchée ? {#why-did-a-user-not-receive-my-triggered-campaign}

L'un des éléments suivants peut empêcher un utilisateur ayant accompli l'événement déclencheur de recevoir la campagne :

- L'utilisateur a accompli l'événement d'exception avant que le délai ne se soit entièrement écoulé.
- La [logique `abort_message`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) Liquid a été utilisée et le message a été abandonné en fonction de la logique ou des règles `abort_message`.
- Le délai a fait que l'utilisateur est devenu éligible pour recevoir la campagne après la fin de sa durée.
- Le délai a fait que l'utilisateur est devenu éligible pour recevoir la campagne en dehors de la portion de journée spécifiée.
- L'utilisateur a déjà reçu la campagne (y compris l'attribution via des identifiants de canal partagés — par exemple, s'il partage un e-mail avec quelqu'un qui l'a reçu, ouvert ou cliqué), et les utilisateurs ne redeviennent pas éligibles.
- Bien que les utilisateurs soient rééligibles pour recevoir la campagne, ils ne peuvent la redéclencher qu'après une certaine période, et cette période ne s'est pas encore écoulée.

La [segmentation]({{site.baseurl}}/user_guide/audience/segments) d'une campagne déclenchée sur des données utilisateur enregistrées au moment de l'événement peut provoquer une [condition de concurrence]({{site.baseurl}}/help/best_practices/race_conditions#race-conditions). Cela se produit lorsque l'attribut utilisateur sur lequel la campagne est segmentée est modifié, mais que la modification n'a pas encore été traitée pour l'utilisateur au moment de l'envoi de la campagne. Puisque les campagnes vérifient l'appartenance au Segment à l'entrée, l'utilisateur peut ne pas recevoir la campagne.

Par exemple, imaginons que vous souhaitez envoyer une campagne déclenchée par événement aux utilisateurs masculins qui viennent de s'inscrire. Lorsque l'utilisateur s'inscrit, vous enregistrez un événement personnalisé `registration` et définissez simultanément l'attribut `gender` de l'utilisateur. L'événement peut déclencher la campagne avant que Braze n'ait traité le genre de l'utilisateur, l'empêchant de recevoir la campagne.

En tant que bonne pratique, assurez-vous que l'attribut sur lequel la campagne est segmentée est transmis aux serveurs Braze avant l'événement. Si ce n'est pas possible, le meilleur moyen de garantir la distribution est d'utiliser les [propriétés d'événement personnalisé]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) pour attacher les propriétés utilisateur pertinentes à l'événement et d'appliquer un filtre de propriété pour la propriété d'événement spécifique plutôt qu'un filtre de segmentation. Dans notre exemple, vous ajouteriez une propriété `gender` à l'événement personnalisé `registration` afin que Braze dispose assurément des données nécessaires lorsque votre campagne est déclenchée.

De plus, si une campagne est par événement et comporte un délai, vous pouvez cocher l'option **Réévaluer l'appartenance au segment au moment de l'envoi** pour vous assurer que les utilisateurs font toujours partie de l'audience cible lorsque le message est envoyé.

#### Évaluation des critères d'audience {#audience-criteria-evaluation}

Pour les campagnes impliquant un délai avant l'envoi (y compris la limitation du débit, le fuseau horaire local, le timing intelligent ou une planification de déclenchement), le moment où le Segment est réévalué dépend du type de campagne et de ses paramètres.

Dans les campagnes par événement avec un délai, si vous sélectionnez **Réévaluer l'appartenance au segment au moment de l'envoi**, les utilisateurs sont réévalués avant l'envoi du message, de sorte que seuls les utilisateurs qui répondent encore aux critères du Segment au moment de l'envoi reçoivent le message.

Si votre campagne est déclenchée par un événement personnalisé spécifique et que vous sélectionnez un Segment comme audience, les utilisateurs doivent effectuer le même événement personnalisé pour être inclus dans le Segment. Cela signifie que les utilisateurs doivent faire partie de l'audience avant qu'une campagne par événement puisse être déclenchée. Le flux de travail général pour une campagne déclenchée est le suivant :

1. **Rejoindre l'audience :** Lorsqu'un utilisateur effectue l'événement personnalisé, il est ajouté à l'audience cible de la campagne.
2. **Déclencher l'e-mail :** Un utilisateur doit effectuer à nouveau l'événement personnalisé pour déclencher l'e-mail, car il doit faire partie de l'audience avant que l'e-mail puisse être envoyé.

Nous recommandons soit de modifier l'audience cible pour inclure tous les utilisateurs, soit de vérifier que les utilisateurs censés effectuer l'événement font déjà partie de l'audience de la campagne pour que le message soit déclenché.

![Capture d'écran liée à l'évaluation des critères d'audience.]({% image_buster /assets/img_archive/reevaluate_segment_membership.png %})

#### Résolution des problèmes liés aux événements personnalisés {#troubleshooting-custom-events}

Commencez par confirmer que l'événement personnalisé est bien transmis à Braze. Accédez à **Analytics** > **Rapport d'événements personnalisés**, puis sélectionnez l'événement personnalisé concerné et la plage de dates. Si l'événement ne s'affiche pas, confirmez qu'il est correctement configuré et que l'utilisateur a effectué l'action appropriée.

Si l'événement personnalisé s'affiche, poursuivez la résolution des problèmes en procédant comme suit :

- Vérifiez le téléchargement du profil de l'utilisateur pour confirmer qu'il a déclenché l'événement et à quel moment. Si l'événement a été déclenché, comparez l'horodatage du déclenchement de l'événement avec le moment où la campagne est passée en production. L'événement a peut-être été déclenché avant la mise en ligne de la campagne.
- Consultez les journaux des modifications de la campagne et de tous les Segments utilisés dans le ciblage pour déterminer si l'utilisateur faisait partie du Segment lorsque son événement personnalisé a été déclenché. S'il n'était pas dans le Segment, il n'aurait pas reçu la campagne.
- Vérifiez si l'utilisateur a été intégré à un groupe de contrôle via la segmentation et a par conséquent été empêché de recevoir la campagne.
- S'il y a un délai planifié, vérifiez si l'événement personnalisé de l'utilisateur a été déclenché avant le délai. Si l'événement a été déclenché avant le délai, il n'aurait pas reçu la campagne.

{% alert note %}
Les messages in-app ne peuvent être déclenchés que par des événements envoyés via le SDK, et non par la REST API.
{% endalert %}

### Quand les campagnes par événement évaluent-elles l'appartenance à l'audience ? {#when-do-action-based-campaigns-evaluate-audience-membership}

Braze évalue l'appartenance à l'audience lorsqu'il traite l'événement déclencheur, avant l'envoi du message. Par défaut, Braze vérifie si l'utilisateur correspond à l'audience cible au moment de la mise en file d'attente. Si la campagne comporte un délai, vous pouvez sélectionner **Réévaluer l'appartenance au segment au moment de l'envoi** pour vérifier à nouveau les critères d'audience juste avant l'envoi — par exemple, lorsqu'un utilisateur pourrait effectuer l'action de déclenchement puis quitter l'audience avant la fin de l'envoi.

Pour plus d'informations, consultez [Évaluation des critères d'audience](#audience-criteria-evaluation).