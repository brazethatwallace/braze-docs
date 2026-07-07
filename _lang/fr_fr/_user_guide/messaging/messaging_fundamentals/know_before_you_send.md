---
nav_title: "À savoir avant l'envoi"
article_title: "À savoir avant l'envoi"
description: "Après avoir consulté notre guide de pré-lancement, référez-vous à cette liste finale de vérifications ou de « pièges » pour les Content Cards, l'e-mail, les messages in-app, les notifications push et les SMS."
alias: /know_before_send/
page_order: 7
tool:
    - Campaigns
    - Canvas
---

# À savoir avant l'envoi : canaux {#know-before-you-send-channels}

> Lancez vos Campaigns et Canvas en toute confiance ! Référez-vous à cette liste finale de vérifications ou de « pièges » pour les [canaux]({{site.baseurl}}/user_guide/channels) d'envoi de messages populaires dans Braze.

{% alert note %}
Bien que nous fournissions une liste exhaustive de ressources à consulter avant l'envoi, chaque canal possède des nuances individuelles qui continuent d'évoluer avec nos produits. Les vérifications listées ci-dessous sont des suggestions utiles, et nous recommandons de tester minutieusement vos Campaigns et vos envois importants avant de les envoyer.
{% endalert %}

## Général {#general}

### Points à vérifier {#things-to-check}
- [**Limites de débit de l'API**](https://braze.com/resources/articles/whats-rate-limiting) : Consultez les [limites de débit]({{site.baseurl}}/api/api_limits) de l'API Braze pour vos espaces de travail afin d'éviter les erreurs. Si vous souhaitez augmenter vos limites de débit (et que vous regroupez déjà vos requêtes par lots), contactez votre gestionnaire de la satisfaction client. Gardez à l'esprit que ce processus nécessite un délai de préparation, planifiez en conséquence.
- [**Dérogations nécessaires à la limite de fréquence**]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) : Certaines Campaigns, comme les messages transactionnels, doivent toujours atteindre l'utilisateur, même si vous avez déjà atteint sa limite de fréquence (par exemple, une notification de livraison). Si vous souhaitez qu'une Campaign particulière contourne les règles de limite de fréquence, vous pouvez configurer cela dans le tableau de bord de Braze lors de la planification de la distribution de cette Campaign en désactivant la limite de fréquence.

### Points à connaître {#things-to-know}
- [**Groupes de contrôle global**]({{site.baseurl}}/user_guide/audience/global_control_group) : Si vous utilisez un groupe de contrôle global, un pourcentage d'utilisateurs ne recevra aucune Campaign ni aucun Canvas. (Vous pouvez créer des exceptions avec les [paramètres d'exclusion]({{site.baseurl}}/user_guide/audience/global_control_group#step-3-assign-exclusion-settings)). Pour voir la liste de ces utilisateurs, exportez-les via CSV ou [API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group).
- [**Limites de débit Canvas**]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) : Dans un Canvas, la limite de débit s'applique à l'ensemble du Canvas, pas aux étapes individuelles. Par exemple, si vous définissez une limite de débit de 10 000 messages par minute sur un Canvas comportant plusieurs étapes, il sera toujours limité à 10 000 messages car la limite aura été atteinte dès la première étape.
- **Limite de fréquence** :
  - Les règles de limite de fréquence s'appliquent aux notifications push, aux e-mails, aux SMS et aux webhooks, mais pas aux messages in-app ni aux Content Cards.
  - La limite de fréquence globale est planifiée en fonction du fuseau horaire de l'utilisateur et est calculée par jours calendaires, et non par périodes de 24 heures. Par exemple, si vous configurez une règle de limite de fréquence n'autorisant pas plus d'une Campaign par jour, un utilisateur peut recevoir un message à 23 h dans son fuseau horaire local et être éligible pour recevoir un autre message une heure plus tard.

{% alert tip %}
Pour obtenir une assistance supplémentaire concernant la résolution des problèmes de Canvas et de Campaign, assurez-vous de contacter l'assistance Braze dans les 30 jours suivant la survenue de votre problème, car nous ne disposons que des 30 derniers jours de journaux de diagnostic.
{% endalert %}

## Bannières {#banners}

### Points à vérifier
- **Dimensions des bannières :** Créez vos bannières en utilisant un élément à dimensions fixes et testez-les dans l'éditeur.
- **Priorité :** Si vous lancez plusieurs bannières, vous pouvez définir manuellement la priorité d'affichage de chaque bannière.

### Points à connaître
- **Personnalisation Liquid :** La personnalisation Liquid est actualisée à chaque requête d'actualisation.
- **Ratio placement et bannière :** Chaque placement de bannière peut être utilisé dans jusqu'à 25 messages dans un espace de travail.
- **Clics et impressions :** Les clics et les impressions des bannières sont suivis automatiquement avec le SDK.
- **Limitations :** Actuellement, les fonctionnalités suivantes ne sont pas prises en charge : l'intégration Canvas, les Campaigns déclenchées par API et basées sur des actions, le Contenu connecté, les codes de promotion et `catalog_items` utilisant la [balise `:rerender`]({{site.baseurl}}/user_guide/data/activation/catalogs/use#using-liquid).
- **Tests :** Pour afficher la bannière de test, l'appareil que vous utilisez doit pouvoir recevoir des notifications push au premier plan.
- **HTML personnalisé :** Utilisez le [pont JavaScript]({{site.baseurl}}/user_guide/channels/in_app_messages/customize#javascript-bridge) pour enregistrer les clics lorsque vous utilisez du HTML personnalisé pour définir des actions de clic, comme des liens et des boutons. Les actions de clic ne sont enregistrées automatiquement que lors de l'utilisation des composants prédéfinis dans l'éditeur par glisser-déposer.
- **Requête de placements :** Jusqu'à 10 placements peuvent être renvoyés au SDK dans une seule requête d'actualisation. Chaque placement inclura la bannière de priorité la plus élevée pour laquelle un utilisateur est éligible.

## Content Cards

### Points à vérifier
- **Taille des Content Cards** : Les champs de message des Content Cards sont limités à 2&nbsp;Ko en taille avant compression, calculée en additionnant la longueur en octets des champs suivants : titre, message, URL de l'image, texte du lien, URL des liens et paires clé-valeur. Les messages dépassant cette taille ne seront pas envoyés. Notez que cela n'inclut pas la taille de l'image elle-même, mais plutôt la longueur de l'URL de l'image.
- **Mise à jour du contenu après envoi** : Après l'envoi d'une carte, vous ne pourrez pas mettre à jour le contenu de cette même carte. Consultez [Mise à jour des cartes envoyées]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#updating-sent-cards) pour comprendre comment aborder ce scénario.

### Points à connaître
- **Limite de Campaigns Content Cards actives** : Vous pouvez avoir jusqu'à 500 Campaigns Content Cards actives. Ce décompte inclut les Content Cards envoyées avec l'une ou l'autre des options de [création de carte]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#card-creation).
- [**Termes de reporting**]({{site.baseurl}}/user_guide/channels/content_cards/reporting) : Consultez les termes tels que impressions totales, impressions uniques et destinataires uniques, car les définitions peuvent parfois prêter à confusion.
- **Actualisation des Content Cards** : Par défaut, Braze actualise les requêtes de Content Cards lors de la synchronisation au démarrage de la session, lors du balayage vers le bas du flux (mobile) et lorsque la vue des cartes est ouverte si la dernière actualisation remonte à plus d'une minute.
- **Mise en cache des Content Cards** : Les options de mise en cache des Content Cards sont disponibles dans notre documentation [Android/FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization/custom_styling#customizing-card-rendering-for-android) et [Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#getcachedcontentcards).
- **Limite de fréquence** : La limite de fréquence ne s'applique pas aux Content Cards.
- **Impressions** : Les impressions sont généralement enregistrées lorsqu'une carte est vue. Par exemple, si vous avez une boîte de réception pleine de Content Cards, une impression ne sera pas enregistrée tant que l'utilisateur n'aura pas fait défiler jusqu'à la Content Card spécifique. Il existe quelques nuances entre les plateformes Web, Android et iOS.
- **Sessions SDK et création de cartes** : Les Content Cards ne sont pas créées pour les utilisateurs sans sessions SDK, même si ces utilisateurs répondent aux critères du segment. Cependant, si un utilisateur a déjà une session Android, les Content Cards avec des actions de clic spécifiques à iOS seront quand même créées, et l'utilisateur pourra voir ces Content Cards sur iOS une fois qu'il aura une session sur cette plateforme. Consultez [Création de carte]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#card-creation) pour plus d'informations sur le moment où les cartes sont créées.

## E-mail {#email}

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

### Points à vérifier
- **Consentement des clients** : Avant d'envoyer vos premiers e-mails, il est important d'obtenir d'abord la permission de vos clients. Consultez [Consentement et collecte d'adresses]({{site.baseurl}}/user_guide/channels/email/email_setup/consent_and_address_collection) et notre [Politique d'utilisation acceptable de Braze](https://www.braze.com/company/legal/aup) pour plus d'informations.
- **Volume anticipé** : 2 millions d'e-mails par jour pour une seule IP est la recommandation générale tant que ce volume a été [correctement préchauffé]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming#ip-warming).
  - Si vous prévoyez d'envoyer régulièrement un volume supérieur, pour éviter que les fournisseurs ne limitent la réception des e-mails, ce qui entraînerait un nombre élevé d'échecs provisoires d'envoi, un taux de livrabilité réduit et une réputation IP diminuée, envisagez d'utiliser plusieurs adresses IP regroupées dans un pool d'IP.
  - Si vous souhaitez envoyer dans un délai plus court uniquement, nous recommandons d'examiner la vitesse à laquelle les différents fournisseurs acceptent le courrier pour déterminer le nombre approprié d'IP à utiliser pour l'envoi.

### Points à connaître
- **Facteurs de volume d'envoi** : Certains facteurs déterminent les volumes d'envoi possibles pour une IP, notamment :
  - Boîtes de réception : Les grands fournisseurs d'e-mail peuvent probablement gérer des millions par jour depuis une seule IP, tandis qu'un fournisseur de boîtes de réception régional plus petit ou disposant d'une infrastructure plus limitée pourrait ne pas être en mesure de gérer ce volume.
  - Réputation de l'expéditeur : Vous pourrez peut-être envoyer un volume plus important par jour depuis une seule IP si l'expéditeur a progressivement augmenté jusqu'à ce volume et si sa réputation d'expéditeur est suffisamment solide auprès de chaque boîte de réception ou domaine vers lequel il envoie.
- **Bonnes pratiques** : Consultez les [bonnes pratiques e-mail]({{site.baseurl}}/user_guide/channels/email/best_practices) de Braze et contactez votre équipe de compte Braze si vous souhaitez en savoir plus sur les services de livrabilité.

## Messages in-app {#in-app-messages}

### Points à connaître
- **Déclenchement des messages in-app** : Au démarrage de la session, le SDK demande que tous les messages in-app éligibles soient envoyés à l'appareil avec leurs déclencheurs, de sorte que si l'utilisateur effectue l'événement pendant la session, il puisse recevoir le message in-app rapidement et de manière fiable.
- **Envoyé versus impressions** : Pour les messages in-app, le concept d'« envoyé » diffère des autres canaux disponibles. Pour voir un message in-app, un utilisateur doit démarrer une session, faire partie de l'audience éligible et effectuer le déclencheur. C'est pourquoi nous suivons les « impressions », car c'est plus clair.
- **Déclenchement** : Par défaut, les messages in-app sont déclenchés par des événements enregistrés par le SDK. Si vous souhaitez déclencher des messages in-app par des événements envoyés par le serveur, vous pouvez également y parvenir grâce à ces guides pour [iOS]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=swift) et [Android]({{site.baseurl}}/developer_guide/in_app_messages/customization?sdktab=android).
- [Messages in-app dans Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas#advancement-behavior-options) : Ces messages apparaissent la première fois que votre utilisateur ouvre l'application (déclenchés par le démarrage de la session) après que le message planifié dans le composant Canvas leur a été envoyé.
- **Appels de Contenu connecté** : L'utilisation du Contenu connecté vous permet d'envoyer du contenu dynamique dans les messages. Lorsque vous envoyez des messages via un canal comme les messages in-app, cela peut créer davantage de connexions simultanées aux appareils de vos utilisateurs (les messages sont envoyés un par un plutôt que par lots). Pour gérer cela, nous recommandons de [limiter le débit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) de vos messages.

## Push {#push}

### Points à vérifier
- [**Opt-in/abonné et push activé**]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states) : Pour que les utilisateurs reçoivent un message push de Braze, leur statut d'abonnement doit être soit opt-in (iOS) soit abonné (Android) et `Push Enabled = True`. Notez qu'Android 13 introduit un changement majeur dans la façon dont les utilisateurs gèrent les applications qui envoient des notifications push. Le [guide de mise à niveau du SDK Android 13]({{site.baseurl}}/developer_guide/platforms/android/android_13) de Braze continuera d'être mis à jour à mesure que de nouvelles versions bêta d'Android 13 seront publiées.

### Points à connaître
- **Push Web** : Si vous avez configuré le [SDK Web de Braze]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web), envisagez d'utiliser le push Web pour engager les utilisateurs. Le push Web fonctionne de la même manière que les notifications push d'application sur votre téléphone. Pour plus d'informations sur la composition d'un push Web, consultez [Créer une notification push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#creating-a-push-message).
- **Ciblage d'une application unique** : Consultez les [différences de segmentation]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration#targeting-a-singular-app) pour cibler une application unique et ses utilisateurs.

## SMS

### Points à vérifier
- **Allocations et débit** : Comprenez quelles allocations SMS sont actuellement rattachées à votre compte (code court, code long et similaires) et [quel débit cela vous fournit]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup) pour confirmer que vous disposez d'un débit suffisant pour envoyer dans le délai souhaité.
- **Estimation des segments à partir du contenu SMS** : Testez votre contenu SMS dans le [calculateur de segments SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator). Gardez à l'esprit que le nombre de segments SMS doit être pris en compte avec vos capacités de débit. (Audience × segments SMS = débit nécessaire). Consultez la FAQ SMS sur [comment éviter les dépassements]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs).
- **Lois et réglementations SMS** : [Consultez les lois, réglementations et la prévention des abus SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations) pour confirmer que vous utilisez les services SMS en conformité avec toutes les lois applicables. Assurez-vous de solliciter l'avis de votre conseiller juridique avant l'envoi.

### Points à connaître
- **Envoi par défaut des messages SMS** : Les messages SMS sont normalement envoyés par défaut depuis le code court du pool d'expéditeurs.
- **Identifiant d'expéditeur alphanumérique** : La messagerie bidirectionnelle ne fonctionnera plus si vous utilisez un identifiant d'expéditeur alphanumérique ; ceux-ci sont désormais unidirectionnels uniquement.
- **Débit mis à jour aux États-Unis** : Le débit a changé aux États-Unis avec l'[enregistrement A2P 10DLC aux États-Unis](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US). Notez que nous ne nous engageons contractuellement sur aucun SLA de vitesse d'envoi en raison de multiples facteurs tels que la congestion du trafic et les problèmes d'opérateurs qui peuvent affecter les taux de livraison réels.
- **Groupe d'abonnement** : Pour lancer une Campaign SMS via Braze, un groupe d'abonnement doit être sélectionné. De plus, pour respecter les [directives et la conformité internationales en matière de télécommunications]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations), Braze n'enverra jamais de SMS aux utilisateurs qui ne se sont pas [abonnés au groupe d'abonnement sélectionné]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#how-to-check-a-users-sms-subscription-group).

## WhatsApp

### Points à connaître

- [**Bonnes pratiques**]({{site.baseurl}}/user_guide/channels/whatsapp/best_practices) : Consultez nos bonnes pratiques suggérées pour WhatsApp.