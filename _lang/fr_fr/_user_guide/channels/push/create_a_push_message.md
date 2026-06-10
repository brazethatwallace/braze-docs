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

> Les notifications push sont idéales pour les appels à l'action urgents, ainsi que pour réengager les utilisateurs qui n'ont pas ouvert l'application depuis un certain temps. Des campagnes push réussies dirigent l'utilisateur directement vers le contenu et démontrent la valeur de votre application. Pour voir des exemples de notifications push, consultez nos [études de cas](https://www.braze.com/customers).

## Étape 1 : Choisir où créer votre message {#create-new-campaign-push}

{% alert tip %}
Vous hésitez entre une campagne et un Canvas ? Les Campaigns sont plus adaptées aux campagnes de communication ciblées et ponctuelles, tandis que les Canvas sont plus adaptés aux parcours utilisateur en plusieurs étapes.
{% endalert %}

{% tabs %}
{% tab Campaign %}
1. Allez dans **Messaging** > **Campaigns**, puis sélectionnez **Create campaign**.
2. Pour les campagnes ciblant plusieurs canaux, sélectionnez **Multichannel**. Sinon, sélectionnez **Push notification**. Si vous n'êtes toujours pas sûr, consultez **Choisir entre une campagne push standard ou multicanal** ci-dessous.
3. Donnez à votre campagne un nom clair et significatif.
4. Ajoutez des [Équipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) et des [Étiquettes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/) selon vos besoins.

{% alert tip %}
Les étiquettes facilitent la recherche de vos campagnes et la création de rapports. Par exemple, lorsque vous utilisez le [Générateur de rapports]({{site.baseurl}}/user_guide/analytics/reports/report_builder/), vous pouvez filtrer par étiquettes spécifiques.
{% endalert %}

{: start="5"}
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez choisir différentes plateformes, types de messages et dispositions pour chacune de vos variantes ajoutées. Pour en savoir plus sur ce sujet, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/).

{% details Choisir entre une campagne push standard ou multicanal %}

Si vous avez l'intention de cibler plusieurs appareils et plateformes, comme toute combinaison de mobile, web, Kindle, iOS et Android, votre sélection à cette étape peut avoir un impact sur la disponibilité de certaines fonctionnalités et paramètres par la suite.

Consultez le diagramme de décision suivant avant de créer une campagne multicanal ou de notification push :

![Diagramme de flux pour sélectionner le type de campagne. Commence par décider si vous ciblez plusieurs appareils et plateformes. Si non, cela mène à « Sélectionner Notification push ». Si oui, cela demande « Quel type de message push ? » et les options sont « Push standard » menant à un point de décision « Avez-vous besoin d'utiliser des paramètres spécifiques à l'appareil ? » Si non, cela mène à « Sélectionner Notification push et utiliser le push rapide ». Si oui, cela mène à « Sélectionner Multicanal ». Retour à « Quel type de message push ? », si la réponse est « Push Stories ou image intégrée », cela dirige vers « Sélectionner Multicanal ».]({% image_buster /assets/img_archive/flowchart_quickpush.png %})

Si vous sélectionnez **Push notification** et choisissez de cibler plusieurs appareils et plateformes, vous créez automatiquement une campagne push rapide. Avec le push rapide, certains paramètres spécifiques à l'appareil ne sont pas disponibles :

- Boutons d'action push
- Canaux et groupes de notification
- Durée de vie du push (TTL)
- Priorité d'affichage
- Sons

Avant de continuer, consultez [Campagnes push rapides]({{site.baseurl}}/quick_push/) pour comprendre ce qui diffère dans cette expérience d'édition.

{% enddetails %}

{% alert tip %}
Si tous les messages de votre campagne vont être similaires ou avoir le même contenu, composez votre message avant d'ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copy from Variant** dans le menu déroulant **Add Variant**.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Créez votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) à l'aide du compositeur Canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape dans le générateur Canvas. Donnez à votre étape un nom clair et significatif.
3. Choisissez un [calendrier d'étape]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types/#schedule-delay) et spécifiez un délai si nécessaire.
4. Filtrez votre audience pour cette étape selon vos besoins. Vous pouvez affiner davantage les destinataires de cette étape en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options d'audience seront vérifiées après le délai, au moment de l'envoi des messages.
5. Choisissez votre [comportement d'avancement]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases/).
6. Choisissez tout autre canal de communication que vous souhaitez associer à votre message.

{% endtab %}
{% endtabs %}

## Étape 2 : Sélectionner les plateformes push {#step-2-select-push-platforms}

Ensuite, choisissez quelle combinaison de plateforme et d'appareil mobile doit recevoir la notification push. Utilisez cette sélection pour limiter la distribution d'une notification push à un ensemble spécifique d'applications.

Il existe plusieurs façons de procéder en fonction de vos sélections précédentes :

| Sélection précédente | Options |
| --- | --- |
| Campagne de notification push | Sélectionnez une ou plusieurs plateformes et appareils. Si vous choisissez de cibler plusieurs appareils et plateformes, vous créez automatiquement une campagne push rapide. Cela offre une expérience d'édition optimisée pour rédiger un message pour toutes les plateformes sélectionnées dans un seul éditeur. Consultez [Campagnes push rapides]({{site.baseurl}}/quick_push/) pour comprendre ce qui diffère dans cette expérience d'édition. |
| Campagne multicanal | Sélectionnez **Add Messaging Channel** pour ajouter des plateformes push supplémentaires. Comme les sélections de plateformes sont spécifiques à chaque variante, vous pouvez tester l'engagement des messages par plateforme. |
| Canvas | Dans votre étape Message, sélectionnez **+ Add more** pour ajouter des plateformes push supplémentaires. Comme pour les campagnes multicanal, les sélections de plateformes sont spécifiques à chaque variante. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2: Select push platforms" }

## Étape 3 : Sélectionner le type de notification (iOS et Android) {#step-3-select-notification-type-ios-and-android}

Si vous créez une campagne push rapide, le type de notification est automatiquement défini sur **Standard push** et ne peut pas être modifié.

![Type de notification avec Push standard sélectionné comme exemple.]({% image_buster /assets/img_archive/push_2.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Sinon, pour iOS et Android, sélectionnez votre type de notification :

- Push standard
- [Contenu push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories/)
- Image intégrée (Android uniquement)

Si vous souhaitez inclure des images dans votre campagne push, consultez les guides suivants sur la création d'une notification enrichie pour [iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications/) ou [Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/rich_notifications/).

## Étape 4 : Composer votre message push {#step-4-compose-your-push-message}

Il est maintenant temps de rédiger votre message push ! L'onglet **Compose** vous permet de modifier tous les aspects du contenu et du comportement de votre message.

![Onglet Compose de la création d'une notification push.]({% image_buster /assets/img_archive/push_compose.png %})

Le contenu de l'onglet **Compose** varie en fonction du type de notification choisi à l'étape précédente, mais peut inclure l'une des options suivantes :

#### Canal ou groupe de notification (iOS et Android) {#notification-channel-or-group-ios-and-android}

Pour plus d'informations sur les options de notification spécifiques à chaque plateforme, consultez [Options de notification iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options/) ou [Options de notification Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_options/).

#### Langue {#language}

Ajoutez du texte dans plusieurs langues à l'aide du bouton **Add Languages**. Nous vous recommandons de sélectionner vos langues avant de rédiger votre contenu afin de pouvoir insérer votre texte aux bons endroits dans le Liquid. Pour consulter notre liste complète des langues disponibles, reportez-vous à [Langues prises en charge]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

Si vous ajoutez du texte dans une langue qui s'écrit de droite à gauche, notez que l'apparence finale des messages de droite à gauche dépend en grande partie de la façon dont les fournisseurs de services les affichent. Pour les bonnes pratiques de rédaction de messages de droite à gauche qui s'affichent aussi fidèlement que possible, consultez [Créer des messages de droite à gauche]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages/).

#### Titre et corps {#title-and-body}

{% tabs local %}
{% tab ios %}
Commencez à taper dans la zone de message et observez un aperçu apparaître dans la zone de prévisualisation à gauche. Les messages push doivent être formatés en texte brut.

Ajoutez un titre à l'aide du champ **Title**. Pour rendre votre push personnalisé et ciblé, vous pouvez inclure du [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/).
{% endtab %}

{% tab android %}
Commencez à taper dans la zone de message et observez un aperçu apparaître dans la zone de prévisualisation à gauche. Les messages push doivent être formatés en texte brut.

Pour rendre votre push personnalisé et ciblé, vous pouvez inclure du [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/).

{% alert important %}
Vous **ne pouvez pas** envoyer un message push Android sans titre&#8212;cependant, vous pouvez saisir un seul espace à la place. Gardez à l'esprit que si votre message ne contient qu'un seul espace, il sera envoyé comme une notification push silencieuse. Pour plus d'informations, consultez [Notifications push silencieuses]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android).
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Besoin d'aide pour créer un texte percutant ? Essayez d'utiliser l'[assistant de rédaction IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Saisissez un nom ou une description de produit et l'IA générera un texte marketing de qualité humaine à utiliser dans vos messages.

![Bouton Lancer le rédacteur IA, situé dans le champ Corps du compositeur push.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_push.png %}){: style="max-width:60%"}
{% endalert %}

#### Image {#image}

Lorsque c'est pris en charge, l'icône de votre application est automatiquement ajoutée comme image pour votre notification push. Vous avez également la possibilité d'envoyer des notifications enrichies, qui permettent une personnalisation plus poussée de vos notifications push en ajoutant du contenu supplémentaire au-delà du texte.

Pour des conseils supplémentaires sur l'utilisation d'images dans vos notifications push, consultez les articles suivants :

- [Créer des notifications enrichies pour iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications/)
- [Créer des notifications enrichies pour Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/rich_notifications/)

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### Comportement au clic {#on-click-behavior}

Spécifiez ce qui se passe lorsqu'un utilisateur sélectionne le corps d'une notification push avec **On-Click Behavior**. Par exemple, vous pouvez inviter les clients à ouvrir votre application, rediriger les clients vers une URL web spécifique, ou même ouvrir une page spécifique de votre application avec un [lien profond]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/).

Ici, vous pouvez également configurer des invites de boutons dans votre notification push, telles que :

- Accepter/Refuser
- Oui/Non
- Confirmer/Annuler
- Plus

#### Options d'envoi {#sending-options}

Si un utilisateur a votre application installée sur plusieurs appareils, par défaut, votre message push est envoyé à tous les appareils disposant d'un jeton de notification push valide. Si vous le souhaitez, vous pouvez sélectionner **Most recently used device**.

![Case à cocher des options d'appareil pour envoyer ce push uniquement à l'appareil le plus récemment utilisé par l'utilisateur.]({% image_buster /assets/img_archive/push_recent_device.png %}){: style="max-width:70%;" }

Il y a quelques nuances pour ce paramètre. Si cette option est sélectionnée, Braze limitera les envois multiples, sauf lorsqu'une campagne cible plusieurs plateformes, comme iOS et Android. Si l'utilisateur a votre application sur un appareil iOS et un appareil Android, il recevra un push pour les deux plateformes. Si l'appareil le plus récemment utilisé d'un utilisateur n'est pas [activé pour le push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states/#foreground-push-enabled), le message ne sera pas envoyé.

Par défaut, Braze envoie les messages à chaque appareil d'un utilisateur disposant d'un jeton de notification push valide. Pour iOS, vous pouvez affiner davantage votre portée en choisissant d'envoyer des notifications uniquement aux appareils iPad, ou uniquement aux appareils iPhone et iPod.

Si vous le souhaitez, vous pouvez définir la destination du push sur **Most recently used device**.

##### Appareil utilisé le plus récemment {#most-recently-used-device}

« Appareil utilisé le plus récemment » est un statut technique, pas comportemental. Comme Braze envoie par défaut à tous les appareils, passer à ce paramètre réduit considérablement votre portée et repose entièrement sur le statut du seul appareil disposant du jeton le plus récent.

L'appareil le plus récemment utilisé est déterminé par l'appareil dont le jeton de notification push a été mis à jour le plus récemment, plutôt que par l'appareil ayant eu la session la plus récente.
* Si le jeton de notification push d'un nouvel appareil est ajouté à un profil utilisateur via l'API, cet appareil est immédiatement considéré comme le plus récemment utilisé, même si l'utilisateur n'a pas encore démarré de session dessus.
* Si l'appareil le plus récemment utilisé d'un utilisateur n'est pas [activé pour le push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states/#foreground-push-enabled), le message ne sera pas envoyé du tout.

Des envois multiples peuvent toujours se produire si une campagne cible différentes plateformes, comme iOS et Android. Si un utilisateur a l'application sur les deux, il peut recevoir un push pour les deux plateformes.

Pour iOS, vous pouvez limiter davantage l'envoi en n'envoyant des notifications push qu'aux appareils iPad, ou uniquement aux appareils iPhone et iPod.

## Étape 5 : Prévisualiser et tester votre message (facultatif) {#step-5-preview-and-test-your-message-optional}

Tester est sans doute l'une des étapes les plus critiques. Après avoir terminé la composition de votre message push parfait, testez-le avant de l'envoyer. Sélectionnez l'onglet **Test** pour choisir parmi les options de test de votre message push. Dans **Test Recipients**, vous pouvez sélectionner un groupe de test de contenu ou des utilisateurs individuels. Vous pouvez également utiliser **Preview message as user** pour avoir une idée de l'apparence de votre message sur mobile pour un utilisateur aléatoire, un utilisateur existant, un utilisateur personnalisé ou un utilisateur multilingue.

Pour plus d'informations, consultez [Envoyer des messages de test]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=push).

## Étape 6 : Construire le reste de votre campagne ou Canvas {#step-6-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Construisez le reste de votre campagne ; consultez les sections suivantes pour plus de détails sur la meilleure façon d'utiliser nos outils pour créer des notifications push.

#### Choisir le calendrier de livraison ou le déclencheur {#choose-delivery-schedule-or-trigger}

Les messages push peuvent être envoyés selon un horaire planifié, une action ou un déclencheur API. Pour en savoir plus, consultez [Planifier votre campagne]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/).

Pour la livraison par événement, vous pouvez également définir la durée de la campagne et les [heures calmes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/).

Cette étape est également celle où vous pouvez spécifier les contrôles de livraison, comme permettre aux utilisateurs de devenir [rééligibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility/#campaigns) pour recevoir la campagne, ou activer les règles de [limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#frequency-capping).

#### Choisir les utilisateurs à cibler {#choose-users-to-target}

Ensuite, vous devez [cibler les utilisateurs]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/) en choisissant des segments ou des filtres pour affiner votre audience. Vous recevez automatiquement un aperçu de la population approximative de ce segment. Les statistiques détaillées de l'audience pour les canaux ciblés par votre campagne sont disponibles dans le pied de page. Pour voir quel pourcentage de votre base d'utilisateurs est ciblé et la valeur vie client pour ce segment, sélectionnez **Show Additional Stats**.

{% multi_lang_include target_audiences.md %}

{% details Pourquoi mon indicateur Total des utilisateurs atteignables ne correspond-il pas à la somme de tous les canaux ? %}

Lorsque vous consultez le Total des utilisateurs atteignables pour votre audience filtrée, vous pouvez remarquer que la somme des colonnes individuelles est inférieure au Total des utilisateurs atteignables. Cet écart est généralement dû au fait qu'un certain nombre d'utilisateurs remplissent les critères du segment ou des filtres de la campagne, mais ne sont pas atteignables par push (par exemple, parce qu'ils n'ont pas de [jetons de notification push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle/#push-tokens) valides ou actifs).

{% enddetails %}

![Tableau des statistiques détaillées de l'audience pour les utilisateurs atteignables.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

Gardez à l'esprit que l'appartenance exacte au segment est toujours calculée avant l'envoi du message.

Vous pouvez également choisir de n'envoyer votre campagne qu'aux utilisateurs ayant un [statut d'abonnement]({{site.baseurl}}/user_guide/channels/email/subscriptions/) spécifique, comme ceux qui sont abonnés et ont opté pour le push.

Facultativement, vous pouvez également limiter la livraison à un nombre spécifié d'utilisateurs au sein du segment, ou permettre aux utilisateurs de recevoir le même message deux fois lors d'une récurrence de la campagne.

##### Campagnes multicanal avec e-mail et push {#multichannel-campaigns-with-email-and-push}

Pour les campagnes multicanal ciblant à la fois les canaux e-mail et push, vous pouvez souhaiter limiter votre campagne afin que seuls les utilisateurs ayant explicitement opté reçoivent le message (en excluant les utilisateurs abonnés ou désabonnés). Par exemple, supposons que vous ayez trois utilisateurs avec des statuts d'opt-in différents :

- **L'utilisateur A** est abonné aux e-mails et est activé pour le push. Cet utilisateur ne reçoit pas l'e-mail mais recevra le push.
- **L'utilisateur B** a opté pour les e-mails mais n'est pas activé pour le push. Cet utilisateur recevra l'e-mail mais ne recevra pas le push.
- **L'utilisateur C** a opté pour les e-mails et est activé pour le push. Cet utilisateur recevra à la fois l'e-mail et le push.

Pour ce faire, sous **Audience Summary**, sélectionnez l'envoi de cette campagne aux « utilisateurs ayant opté uniquement ». Cette option garantira que seuls les utilisateurs ayant opté recevront votre e-mail, et Braze n'enverra votre push qu'aux utilisateurs activés pour le push par défaut.

{% alert important %}
Avec cette configuration, n'incluez aucun filtre dans l'étape **Target Audiences** qui limiterait l'audience à un seul canal (par exemple, `Foreground Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

#### Choisir les événements de conversion {#choose-conversion-events}

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, les [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/), après avoir reçu une campagne. Vous avez la possibilité d'autoriser une fenêtre allant jusqu'à 30 jours pendant laquelle une conversion sera comptabilisée si l'utilisateur effectue l'action spécifiée.

{% endtab %}

{% tab Canvas %}

Si ce n'est pas déjà fait, complétez les sections restantes de votre composant Canvas. Pour plus de détails sur la façon de construire le reste de votre Canvas, d'implémenter les tests multivariés et la Sélection intelligente, et plus encore, consultez l'étape [Construire votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation Canvas.

{% endtab %}
{% endtabs %}

## Étape 7 : Vérifier et déployer {#review-and-deploy-push}

Après avoir terminé la construction de votre campagne ou Canvas, vérifiez ses détails. Pour les campagnes, la dernière page vous donne un résumé de la campagne que vous avez conçue. Confirmez tous les détails pertinents, assurez-vous d'avoir testé votre message, puis envoyez-le et observez les données affluer !

Ensuite, consultez [Rapports push]({{site.baseurl}}/user_guide/channels/push/reporting/) pour découvrir comment accéder aux résultats de votre campagne push. Pour les notifications push, vous pourrez consulter les statistiques relatives au nombre de messages envoyés, livrés, rejetés, ouverts et ouverts directement.

### Résolution des problèmes {#troubleshooting}

#### Comportement au clic

Si vous utilisez le comportement au clic par défaut pour votre version du SDK et que la sélection d'une notification push avec une URL web ouvre l'application au lieu du navigateur web, consultez les guides d'intégration suivants pour déterminer la gestion des notifications push :

- [Swift]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-2-enable-push-capabilities)
- [Android]({{site.baseurl}}/developer_guide/push_notifications/#android_step-1-register-braze-firebase-messaging-service)

{% alert important %}
Vous devez assigner votre objet délégué en utilisant `center.delegate = self` de manière synchrone avant que votre application ne termine son lancement, de préférence dans `application:didFinishLaunchingWithOptions:`. Sinon, votre application risque de manquer les notifications push entrantes. Consultez la [documentation `UNUserNotificationCenterDelegate` d'Apple](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) pour en savoir plus.
{% endalert %}