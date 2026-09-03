---
nav_title: "Créer un message push"
article_title: "Créer un message push"
page_order: 1
page_type: tutorial
description: "Cette page de tutoriel couvre les différents composants impliqués dans la création d'un message push, notamment la configuration, l'envoi, le ciblage, et plus encore."
channel: push
tool:
  - Campaigns



---

# Créer un message push {#create-a-push-message}

> Les notifications push sont idéales pour les appels à l'action urgents, ainsi que pour réengager les utilisateurs qui n'ont pas ouvert l'application depuis un certain temps. Des campagnes push réussies dirigent l'utilisateur directement vers le contenu et démontrent la valeur de votre application. Pour voir des exemples de notifications push, consultez les [études de cas Braze](https://www.braze.com/customers).

## Étape 1 : Choisir où créer votre message {#create-new-campaign-push}

{% alert tip %}
Vous hésitez entre une campagne et un Canvas ? Les Campaigns sont plus adaptées aux campagnes de communication ciblées et ponctuelles, tandis que les Canvas sont plus adaptés aux parcours utilisateur en plusieurs étapes.
{% endalert %}

{% tabs %}
{% tab Campaign %}
1. Allez dans **Messaging** > **Campaigns**, puis sélectionnez **Créer une campagne**.
2. Pour les campagnes ciblant plusieurs canaux, sélectionnez **Multicanal**. Sinon, sélectionnez **Notification push**.
3. Donnez à votre campagne un nom clair et significatif.
4. Ajoutez des [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) et des [étiquettes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) selon vos besoins.

{% alert tip %}
Les étiquettes facilitent la recherche de vos campagnes et la création de rapports. Par exemple, lorsque vous utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reports/report_builder), vous pouvez filtrer par étiquettes spécifiques.
{% endalert %}

{: start="5"}
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez choisir différentes plateformes, types de messages et dispositions pour chacune de vos variantes ajoutées. Pour en savoir plus sur ce sujet, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Si tous les messages de votre campagne vont être similaires ou avoir le même contenu, composez votre message avant d'ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copier depuis la variante** dans le menu déroulant **Ajouter une variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}
{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

## Étape 2 : Sélectionner les plateformes push {#step-2-select-push-platforms}

Ensuite, choisissez quelle combinaison de plateforme et d'appareil mobile doit recevoir la notification push. Utilisez cette sélection pour limiter la distribution d'une notification push à un ensemble spécifique d'applications.

Il existe plusieurs façons de procéder selon vos sélections précédentes :

| Sélection précédente | Options |
| --- | --- |
| Campagne de notification push | Sélectionnez une ou plusieurs plateformes et appareils. Si vous choisissez de cibler plusieurs appareils et plateformes, votre expérience d'édition est optimisée pour rédiger un seul message pour toutes les plateformes sélectionnées. Consultez [Messages push multiplateformes]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/multiple_platform_push) pour comprendre ce qui diffère dans cette expérience d'édition. |
| Campagne multicanal | Sélectionnez **Add Messaging Channel** pour ajouter des plateformes push supplémentaires. Comme les sélections de plateforme sont spécifiques à chaque variante, vous pouvez tester l'engagement des messages par plateforme. |
| Canvas | Dans votre étape de message, sélectionnez **+ Add more** pour ajouter des plateformes push supplémentaires. Comme pour les campagnes multicanal, les sélections de plateforme sont spécifiques à chaque variante. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 2 : Sélectionner les plateformes push" }

## Étape 3 : Sélectionner le type de notification (iOS et Android) {#step-3-select-notification-type-ios-and-android}

Si vous créez une campagne push multiplateforme et que vous sélectionnez Web et/ou Kindle, le type de notification est automatiquement défini sur **Standard push** et ne peut pas être modifié.

![Type de notification avec Standard Push sélectionné comme exemple.]({% image_buster /assets/img_archive/push_2.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Sinon, pour iOS et Android, sélectionnez votre type de notification :

- Standard push
- [Contenu push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories) (pris en charge sur Android + iOS)
- Image intégrée (Android uniquement)

Si vous souhaitez inclure des images dans votre campagne push, consultez les guides suivants sur la création d'une notification enrichie pour [iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications) ou [Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/rich_notifications).

## Étape 4 : Composez votre notification push {#step-4-compose-your-push-message}

Il est maintenant temps de rédiger votre notification push ! L'onglet **Rédiger** vous permet de modifier tous les aspects du contenu et du comportement de votre message.

![Onglet Rédiger lors de la création d'une notification push.]({% image_buster /assets/img_archive/push_multiple_platform_message_composer.png %})

Le contenu de l'onglet **Rédiger** varie en fonction du type de notification choisi à l'étape précédente, mais peut inclure l'une des options suivantes :

### Canal ou groupe de notifications (iOS et Android) {#notification-channel-or-group-ios-and-android}

Pour plus d'informations sur les options de notification spécifiques à chaque plateforme, consultez [Options de notification iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options) ou [Options de notification Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_options).

### Langue {#language}

Ajoutez du texte dans plusieurs langues à l'aide du bouton **Add Languages**. Nous vous recommandons de sélectionner vos langues avant de rédiger votre contenu afin de pouvoir remplir votre texte là où il doit apparaître dans le Liquid. Pour consulter la liste complète des langues disponibles, reportez-vous à [Langues prises en charge]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization#languages-supported).

Si vous ajoutez du texte dans une langue qui s'écrit de droite à gauche, sachez que l'apparence finale des messages de droite à gauche dépend en grande partie de la façon dont les fournisseurs de services les affichent. Pour connaître les bonnes pratiques de rédaction de messages de droite à gauche qui s'affichent aussi fidèlement que possible, consultez [Créer des messages de droite à gauche]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

### Titre et corps {#title-and-body}

{% tabs local %}
{% tab iOS %}
Commencez à taper dans la zone de message et observez l'aperçu apparaître dans la boîte de prévisualisation à côté. Les notifications push doivent être formatées en texte brut.

Ajoutez un titre à l'aide du champ **Title**. Pour personnaliser et cibler votre notification push, vous pouvez inclure du [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid).
{% endtab %}

{% tab Android %}
Commencez à taper dans la zone de message et observez l'aperçu apparaître dans la boîte de prévisualisation à côté. Les notifications push doivent être formatées en texte brut.

Pour personnaliser et cibler votre notification push, vous pouvez inclure du [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid).

{% alert important %}
Vous **ne pouvez pas** envoyer une notification push Android sans titre&#8212;cependant, vous pouvez saisir un espace unique à la place. Gardez à l'esprit que si votre message ne contient qu'un seul espace, il sera envoyé en tant que notification push silencieuse. Pour plus d'informations, consultez [Notifications push silencieuses]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=android).
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Besoin d'aide pour rédiger un texte percutant ? Essayez l'[assistant de rédaction par IA]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy). Saisissez un nom ou une description de produit et l'IA génèrera un texte marketing au ton naturel à utiliser dans vos communications.

![Bouton Lancer l'assistant de rédaction par IA, situé dans le champ Corps du compositeur de notifications push.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_push.png %}){: style="max-width:60%"}
{% endalert %}

### Image {#image}

Lorsque c'est pris en charge, l'icône de votre application est automatiquement ajoutée comme image de votre notification push. Vous avez également la possibilité d'envoyer des notifications enrichies, qui permettent davantage de personnalisation en ajoutant du contenu supplémentaire au-delà du texte.

Pour des conseils supplémentaires sur l'utilisation d'images dans vos notifications push, consultez les articles suivants :

- [Créer des notifications enrichies pour iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications)
- [Créer des notifications enrichies pour Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/rich_notifications)

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

### Comportement au clic {#on-click-behavior}

Spécifiez ce qui se passe lorsqu'un utilisateur sélectionne le corps d'une notification push avec **On-Click Behavior**. Par exemple, vous pouvez inciter les clients à ouvrir votre application, les rediriger vers une URL web spécifique, ou même ouvrir une page spécifique de votre application avec un [deep link]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls).

Ici, vous pouvez également configurer des boutons d'action au sein de votre notification push, tels que :

- Accepter/Refuser
- Oui/Non
- Confirmer/Annuler
- Plus

### Options d'envoi {#sending-options}

Si un utilisateur a votre application installée sur plusieurs appareils, par défaut, votre notification push est envoyée à tous les appareils disposant d'un jeton push valide. Si vous le souhaitez, vous pouvez sélectionner **Most recently used device**.

![Case à cocher des options d'appareil pour n'envoyer cette notification push qu'à l'appareil le plus récemment utilisé par l'utilisateur.]({% image_buster /assets/img_archive/push_recent_device.png %}){: style="max-width:70%;" }

Ce paramètre présente quelques nuances. Lorsque cette option est sélectionnée, Braze limitera les envois multiples, sauf lorsqu'une campagne cible plusieurs plateformes, comme iOS et Android simultanément. Si l'utilisateur a votre application sur un appareil iOS et un appareil Android, il recevra une notification push pour les deux plateformes. Si l'appareil le plus récemment utilisé par l'utilisateur n'est pas [activé pour les notifications push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#foreground-push-enabled), le message ne sera pas envoyé.

Par défaut, Braze envoie les messages à chaque appareil de l'utilisateur disposant d'un jeton push valide. Pour iOS, vous pouvez affiner davantage votre portée en choisissant d'envoyer les notifications uniquement aux appareils iPad, ou uniquement aux appareils iPhone et iPod.

Si vous le souhaitez, vous pouvez définir la destination push sur **Most recently used device**.

#### Appareil le plus récemment utilisé {#most-recently-used-device}

« Appareil le plus récemment utilisé » est un statut technique, et non comportemental. Comme Braze cible par défaut tous les appareils, passer à ce paramètre réduit considérablement votre portée et repose entièrement sur le statut du seul appareil disposant du jeton le plus récent.

L'appareil le plus récemment utilisé est déterminé par l'appareil dont le jeton push a été mis à jour le plus récemment, et non par l'appareil ayant eu la session la plus récente.
* Si le jeton push d'un nouvel appareil est ajouté à un profil utilisateur via l'API, cet appareil est immédiatement considéré comme le plus récemment utilisé, même si l'utilisateur n'a pas encore démarré de session dessus.
* Si l'appareil le plus récemment utilisé par un utilisateur n'est pas [activé pour les notifications push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#foreground-push-enabled), le message ne sera pas envoyé du tout.

Des envois multiples peuvent toujours se produire si une campagne cible différentes plateformes, comme iOS et Android simultanément. Si un utilisateur a l'application sur les deux, il peut recevoir une notification push pour chaque plateforme.

Pour iOS, vous pouvez limiter davantage les envois en n'envoyant les notifications push qu'aux appareils iPad, ou uniquement aux appareils iPhone et iPod.

## Étape 5 : Prévisualisez et testez votre message (facultatif) {#step-5-preview-and-test-your-message-optional}

Le test est sans doute l'une des étapes les plus critiques. Après avoir composé votre notification push parfaite, testez-la avant de l'envoyer. Sélectionnez l'onglet **Test** pour choisir parmi les options de test de votre notification push. Dans **Test Recipients**, vous pouvez sélectionner un groupe de test de contenu ou des utilisateurs individuels. Vous pouvez également utiliser **Preview message as user** pour avoir un aperçu de l'affichage de votre message sur mobile pour un utilisateur aléatoire, un utilisateur existant, un utilisateur personnalisé ou un utilisateur multilingue.

Pour plus d'informations, consultez [Envoyer des messages de test]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=push).

## Étape 6 : Finaliser votre campagne ou Canvas {#step-6-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Finalisez le reste de votre campagne ; consultez les sections suivantes pour plus de détails sur la meilleure façon d'utiliser nos outils pour créer des notifications push.

### Choisir une planification ou un déclencheur de réception {#choose-delivery-schedule-or-trigger}

Les notifications push peuvent être envoyées selon une planification, une action ou un déclencheur API. Pour en savoir plus, consultez [Planifier votre campagne]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Pour la livraison par événement, vous pouvez également définir la durée de la campagne et les [heures calmes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

Cette étape vous permet également de spécifier les contrôles de réception, comme autoriser les utilisateurs à redevenir [rééligibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) pour recevoir la campagne, ou activer les règles de [limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping).

### Choisir les utilisateurs à cibler {#choose-users-to-target}

Ensuite, vous devez [cibler les utilisateurs]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) en choisissant des Segments ou des filtres pour affiner votre audience. Vous recevez automatiquement un aperçu de la population approximative de ce Segment. Des statistiques d'audience détaillées pour les canaux ciblés par votre campagne sont disponibles dans le pied de page. Pour voir quel pourcentage de votre base d'utilisateurs est ciblé et la valeur vie client pour ce Segment, sélectionnez **Show Additional Stats**.

{% multi_lang_include audience/target_audiences.md %}

{% details Pourquoi la métrique Total des utilisateurs joignables ne correspond-elle pas à la somme de tous les canaux ? %}

Lorsque vous consultez le total des utilisateurs joignables pour votre audience filtrée, vous remarquerez peut-être que la somme des colonnes individuelles est inférieure au total des utilisateurs joignables. Cet écart s'explique généralement par le fait qu'un certain nombre d'utilisateurs correspondent au Segment ou aux filtres de la campagne, mais ne sont pas joignables par notification push (par exemple, parce qu'ils n'ont pas de [jetons push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle#push-tokens) valides ou actifs).

{% enddetails %}

![Tableau des statistiques d'audience détaillées pour les utilisateurs joignables.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

Gardez à l'esprit que l'appartenance exacte à un Segment est toujours calculée avant l'envoi du message.

Vous pouvez également choisir d'envoyer votre campagne uniquement aux utilisateurs ayant un [statut d'abonnement]({{site.baseurl}}/user_guide/channels/email/subscriptions) spécifique, comme ceux qui sont abonnés et ont accepté les notifications push.

Vous pouvez aussi limiter la réception à un nombre spécifié d'utilisateurs au sein du Segment, ou autoriser les utilisateurs à recevoir le même message deux fois lors d'une récurrence de la campagne.

#### Campaigns multicanales avec e-mail et push {#multichannel-campaigns-with-email-and-push}

Pour les Campaigns multicanales ciblant à la fois les canaux e-mail et push, vous souhaiterez peut-être limiter votre campagne afin que seuls les utilisateurs ayant explicitement accepté reçoivent le message (en excluant les utilisateurs abonnés ou désabonnés). Par exemple, supposons que vous ayez trois utilisateurs avec des statuts d'abonnement différents :

{% multi_lang_include messaging/intelligent_channel_user_examples.md %}

Pour ce faire, sous **Audience Summary**, sélectionnez l'envoi de cette campagne uniquement aux « utilisateurs ayant explicitement accepté ». Cette option garantit que seuls les utilisateurs ayant accepté recevront votre e-mail, et Braze n'enverra vos notifications push qu'aux utilisateurs pour lesquels le push est activé par défaut.

{% alert important %}
Avec cette configuration, n'incluez aucun filtre à l'étape **Target Audiences** qui limite l'audience à un seul canal (par exemple, `Foreground Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

### Choisir les événements de conversion {#choose-conversion-events}

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, les [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), après avoir reçu une campagne. Vous avez la possibilité de définir une fenêtre allant jusqu'à 30 jours pendant laquelle une conversion sera comptabilisée si l'utilisateur effectue l'action spécifiée.

{% endtab %}

{% tab Canvas %}

Si ce n'est pas déjà fait, complétez les sections restantes de votre composant Canvas. Pour plus de détails sur la création du reste de votre Canvas, y compris les tests multivariés et l'[optimisation avec BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai), consultez [Créer votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas).

{% endtab %}
{% endtabs %}

## Étape 7 : Vérifier et déployer {#review-and-deploy-push}

Après avoir terminé la construction de votre campagne ou Canvas, vérifiez ses détails. Pour les campagnes, la dernière page vous donne un résumé de la campagne que vous avez conçue. Confirmez tous les détails pertinents, assurez-vous d'avoir testé votre message, puis envoyez-le et observez les données affluer !

Ensuite, consultez [Rapports push]({{site.baseurl}}/user_guide/channels/push/reporting) pour découvrir comment accéder aux résultats de votre campagne push. Pour les notifications push, vous pourrez consulter les statistiques relatives au nombre de messages envoyés, livrés, rejetés, ouverts et ouverts directement.

### Résolution des problèmes {#troubleshooting}

#### Comportement au clic

Si vous utilisez le comportement au clic par défaut pour votre version du SDK et que la sélection d'une notification push avec une URL web ouvre l'application au lieu du navigateur web, consultez les guides d'intégration suivants pour déterminer la gestion des notifications push :

- [Swift]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift#swift_step-2-enable-push-capabilities)
- [Android]({{site.baseurl}}/developer_guide/push_notifications#android_step-1-register-braze-firebase-messaging-service)

{% alert important %}
Vous devez assigner votre objet délégué en utilisant `center.delegate = self` de manière synchrone avant que votre application ne termine son lancement, de préférence dans `application:didFinishLaunchingWithOptions:`. Sinon, votre application risque de manquer les notifications push entrantes. Consultez la [documentation `UNUserNotificationCenterDelegate` d'Apple](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) pour en savoir plus.
{% endalert %}