---
nav_title: FAQ
article_title: FAQ SMS, MMS et RCS
page_order: 30
description: "Cet article répond aux questions fréquemment posées sur l'envoi de messages SMS, MMS et RCS."
page_type: FAQ
alias: /sms_mms_rcs_faq/
channel:
  - SMS
  - MMS
  - RCS
---

# Questions fréquemment posées {#frequently-asked-questions}

> Cet article répond aux questions fréquemment posées sur l'envoi de messages SMS, MMS et RCS.

## Général {#general}

### Qu'est-ce qu'un `app_id` dans l'objet API SMS ? {#what-is-an-app_id-in-the-sms-api-object}

L'identifiant d'application ou clé API `app_id` est un paramètre qui associe une activité à une application spécifique de votre espace de travail. Il désigne l'application avec laquelle vous interagissez au sein de l'espace de travail. Par exemple, vous disposez d'un `app_id` pour votre application iOS, d'un `app_id` pour votre application Android et d'un `app_id` pour votre intégration web.

Pour les SMS, le paramètre `app_id` est requis lors de l'envoi de messages SMS via l'API (comme l'endpoint `/messages/send`). Il spécifie quelle application de votre espace de travail est associée à l'activité SMS ou à l'appel API. Vous pouvez utiliser n'importe quel `app_id` valide d'une application configurée dans votre espace de travail pour l'envoi de SMS, que l'utilisateur ait ou non cette application spécifique sur son profil.

Vous pouvez trouver votre `app_id` en accédant à **Paramètres** > **Paramètres de l'application** et en localisant la section **Identification**.

### Que se passe-t-il si plusieurs utilisateurs partagent le même numéro de téléphone ? {#what-happens-if-multiple-users-have-the-same-phone-number}

Lorsque plusieurs profils utilisateur partageant le même numéro de téléphone (activé pour les SMS) sont éligibles à une Campaign ou un composant Canvas déclenchés par un événement, par la réception d'un SMS entrant, Braze déduplique les utilisateurs au niveau du composant Canvas. Cela empêche les utilisateurs de recevoir plus d'un SMS pour un composant Canvas, même si plusieurs utilisateurs partagent le même numéro de téléphone.

{% alert note %}
Braze ne déduplique pas par numéro de téléphone pour les Canvas planifiés.
{% endalert %}

Braze utilise le processus suivant pour déterminer le profil destinataire :
- Vérifier quel profil a reçu un SMS le plus récemment (jusqu'à 7 jours auparavant) ; si un tel profil existe, envoyer le message à cet utilisateur.
- Si aucun profil n'a reçu de SMS au cours des 7 derniers jours, envoyer le message à l'utilisateur possédant un alias utilisateur « phone » correspondant au numéro de téléphone.
- Si aucun de ces cas ne s'applique, envoyer le message à un profil aléatoire parmi ceux disponibles.

Si vous recevez un mot-clé « START » ou « STOP » provenant du numéro de téléphone partagé, tous les profils utilisateur seront abonnés et activés pour les SMS ou désabonnés. Cela s'applique également aux changements d'état via l'API. Par exemple, si plusieurs profils avec des ID externes différents partagent le même numéro de téléphone, un changement d'état de groupe d'abonnement via l'API mettra à jour tous les profils associés à ce numéro de téléphone, même si un seul ID externe est spécifié.

{% alert important %}
Si vous échelonnez l'entrée de vos utilisateurs dans un Canvas avec des horaires de planification différents pour chaque composant Canvas, un utilisateur ayant le même e-mail ou numéro de téléphone peut recevoir des messages en double.
{% endalert %}

Pour éviter des mises à jour inutilement volumineuses, Braze met à jour un maximum de 100 profils utilisateur partageant un identifiant lors d'une mise à jour d'abonnement. Si plus de 100 profils utilisateur partagent le même numéro de téléphone, tous les profils ne seront pas mis à jour.

### Pourquoi est-ce que j'observe un pic d'abonnements SMS provenant d'une source spécifique ? {#why-do-i-see-a-spike-in-sms-subscriptions-from-a-specific-source}

Si vous constatez une augmentation anormalement importante du nombre d'abonnements, notamment en examinant les données de l'endpoint [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) via Currents, cela peut être dû à des profils utilisateur en double.

Lorsqu'une requête est envoyée à l'endpoint `/subscription/status/set` avec uniquement un numéro de téléphone (sans `external_id` fourni), Braze met à jour tous les profils utilisateur partageant ce numéro de téléphone. Si votre espace de travail contient des profils en double, le nombre d'utilisateurs ayant mis à jour leur état d'abonnement est gonflé, alors qu'un seul numéro de téléphone a réellement changé.

Pour analyser les données d'abonnement de manière plus précise lorsque vous les extrayez de Currents, modifiez votre requête pour compter les numéros de téléphone distincts plutôt que de compter tous les événements de changement d'état d'abonnement.

### Que sont les codes courts partagés ? {#what-are-shared-short-codes}

Avec un code court partagé, tous les messages texte, quelle que soit l'entreprise ou l'organisation qui les envoie, arrivent sur l'appareil mobile du consommateur depuis le même numéro de téléphone à 5-6 chiffres. Bien que les codes courts partagés soient relativement peu coûteux et immédiatement disponibles, cela signifie que votre entreprise ne disposera pas d'un code court dédié.

Voici quelques inconvénients de cette approche :

- Si vos clients se désabonnent des messages d'une autre entreprise partageant un code court avec vous, ils se seront également désabonnés de vos messages.
- Si une entreprise enfreint les règles, les messages de toutes les entreprises sont suspendus.
- Problèmes de sécurité

## Facturation et tarification {#billing-and-pricing}

### Comment suis-je facturé pour les SMS ? {#how-will-i-be-billed-for-sms}

Outre les frais liés aux codes courts et aux codes longs, Braze fournit une allocation de messages SMS pour différents pays. Autrement dit, nous collaborons avec vous pour définir un certain nombre de segments de message pour différents pays, que vous utiliserez pour envoyer des campagnes SMS. La facturation est calculée en fonction du nombre de segments de message envoyés par pays. Pour en savoir plus sur le calcul des segments de message, consultez notre guide [Segments de message et limites de texte]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator). Votre gestionnaire de compte vous contactera pour vous informer si vous approchez de votre maximum, en vous fournissant des rapports pertinents pour vous tenir informé. Pour toute question concernant les dépassements, contactez votre conseiller Braze.

### Les tarifs MMS et SMS sont-ils différents ? {#does-mms-and-sms-pricing-differ}

Les MMS et les SMS ont des coûts différents et sont facturés séparément en fonction du volume. Contactez l'équipe d'onboarding de Braze pour obtenir des informations tarifaires.

### Comment puis-je éviter les dépassements ? {#how-can-i-avoid-overages}

Bien que nous ne puissions pas garantir que vous n'aurez jamais de dépassement, vous pouvez suivre ces précautions pour réduire les risques de dépasser vos limites allouées :

- Faites attention au nombre de caractères de votre SMS. Envoyer involontairement plus d'un segment peut entraîner des dépassements. Pour plus de détails, consultez notre [répartition des segments]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator).
- Calculez soigneusement le nombre de caractères de votre SMS pour tenir compte de Liquid ou du contenu connecté. Le composeur SMS de Braze dans votre tableau de bord n'estime pas et ne prend pas en compte l'utilisation de l'une ou l'autre de ces fonctionnalités.
- Tenez compte du type d'encodage utilisé par votre message. Si votre message utilise l'encodage GSM-7, vous pouvez généralement estimer 160 caractères par segment de message (moins si vous utilisez des caractères de la table d'extension GSM-7). Si votre message utilise l'encodage [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set), vous pouvez généralement estimer 67 caractères par segment de message.
- Testez, testez et testez encore ! Testez toujours vos messages SMS avant de les lancer, en particulier lorsque vous utilisez Liquid et le contenu connecté.

### Si un message est envoyé à un téléphone fixe, est-il tout de même comptabilisé dans mon nombre d'envois SMS ? {#if-a-message-is-sent-to-a-landline-will-the-message-still-count-toward-my-sms-send-count}

Aux États-Unis, au Canada et au Royaume-Uni :
- Si un SMS est envoyé à un téléphone fixe, il est marqué comme **Non distribué**. Le comportement de facturation dépend de votre fournisseur de services SMS. Avec Twilio, la tentative de distribution est tout de même facturée, de sorte que les messages marqués comme **Envoyé**, **Distribué** ou **Non distribué** dans vos journaux de messages sont facturés.
- Au Royaume-Uni, certains opérateurs convertissent le SMS en message vocal, permettant ainsi la distribution du message.

Dans les autres pays :
- Avec Twilio, une erreur est générée et la tentative d'envoi du SMS ne vous est pas facturée.

### Pourquoi le tableau de bord de Braze m'avertit-il que des segments de message supplémentaires pourraient m'être facturés alors que mon message fait moins de 160 (GSM-7) ou 67 (UCS-2) caractères ? {#why-is-the-braze-dashboard-warning-me-i-may-be-charged-for-additional-message-segments-when-my-message-is-under-160-gsm-7-or-67-ucs-2-characters}

Des segments de message supplémentaires peuvent vous être facturés si votre message contient de la personnalisation Liquid. Le rendu des blocs de contenu ne s'effectue pas avant que le message ne soit prêt à être envoyé. Lorsque vous modifiez un SMS contenant un bloc de contenu, Braze ne sait pas ce que le bloc de contenu contiendra, mais fournit une estimation approximative. Nous recommandons aux utilisateurs d'utiliser le volet de test pour prévisualiser le message afin de mieux comprendre à quoi s'attendre.

## Envoi et livrabilité {#sending-and-deliverability}

### Est-il possible d'inclure des liens dans un SMS ? {#can-you-include-links-in-an-sms}

Vous pouvez inclure n'importe quel lien dans n'importe quelle Campaign SMS. Cependant, il y a quelques points à prendre en compte :

- Les liens peuvent occuper une grande partie de la limite de 160 caractères des SMS. Si vous incluez un lien et du texte, cela peut entraîner l'envoi de deux SMS au lieu d'un seul.
- Les entreprises utilisent souvent des raccourcisseurs de liens pour limiter l'impact sur le nombre de caractères. Cependant, si vous envoyez un lien raccourci via un code long, les opérateurs peuvent bloquer ou refuser le message, car ils peuvent être méfiants vis-à-vis de la redirection du lien.
- L'utilisation d'un [code court]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup) serait le type de numéro le plus fiable pour inclure des liens.

Braze dispose également de sa propre fonctionnalité de raccourcissement de liens qui raccourcit les liens et fournit automatiquement des analyses de clics. Consultez [Raccourcissement de liens]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening) pour plus d'informations.

### Faut-il limiter le débit d'envoi des SMS ? {#do-you-need-to-rate-limit-how-fast-you-send-sms-messages}

Le taux de concurrence et le débit par défaut permettent d'envoyer environ 360 000 messages par heure par code court. Un débit supplémentaire nécessite des codes courts supplémentaires.

### Comment ajouter des URL à la liste d'autorisation pour les SMS ? {#how-do-you-allowlist-urls-for-sms}

Avant d'envoyer des SMS contenant des URL aux utilisateurs de certains pays (par exemple, la Suède ou les pays nordiques), vous devez faire enregistrer ces URL auprès de l'opérateur. Contactez votre gestionnaire de compte Braze pour obtenir de l'aide. Ce processus prend environ cinq jours.

### Quelles sont les meilleures pratiques d'envoi pour éviter la détection de spam pour les SMS ? {#what-are-the-best-sending-practices-to-avoid-spam-detection-for-sms}

1. Assurez-vous que les instructions d'abonnement et de désabonnement sont claires.
2. Assurez-vous que vous (la marque) avez une relation avec le client.
3. Assurez-vous que le contenu est pertinent par rapport à la relation et à ce que l'utilisateur a accepté de recevoir.

Pour plus de recommandations sur la façon d'éviter la détection de spam, consultez les [lois et réglementations relatives aux SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations).

### Combien de caractères un emoji utilise-t-il ? {#how-many-characters-does-an-emoji-use}

Les emojis peuvent poser problème, car il n'existe pas de nombre de caractères standard pour tous les emojis. Il y a un risque que l'emoji dépasse la limite de caractères et divise le SMS en plusieurs messages, même s'il apparaît comme un seul message dans le compositeur de Braze. Lorsque vous testez vos messages, vous pouvez mieux vérifier si un message sera divisé en utilisant notre [calculateur de segments]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator).

## Groupes d'abonnement et abonnement/désabonnement {#subscription-groups-and-opt-inopt-out}

### Comment créer une logique d'abonnement sélectif aux SMS pour que les utilisateurs soient dans le bon groupe d'abonnement ? {#how-do-you-create-logic-for-selective-opt-ins-to-sms-so-users-are-in-the-right-subscription-group}

Les mots-clés personnalisés sont enregistrés en tant qu'événements personnalisés. Vous devez donc créer des segments basés sur les mots-clés que les clients peuvent envoyer par SMS. Par exemple, si un utilisateur s'abonne aux SMS pour les messages VIP mais pas pour les alertes, vous pouvez créer un segment VIP et un segment alertes, puis attribuer l'utilisateur au segment approprié.

### Si un utilisateur envoie « Stop » à notre code court, est-il désabonné du groupe d'abonnement ? {#if-a-user-texts-stop-to-our-short-code-are-they-unsubscribed-from-the-subscription-group}

À quoi cela ressemble-t-il sur le profil utilisateur ? Le groupe d'abonnement apparaît comme désabonné sous **Paramètres de contact**, et il existe des événements personnalisés pour l'abonnement et le désabonnement.

### Si un utilisateur s'est désabonné et envoie un mot-clé à notre code court ou code long, reçoit-il la réponse que nous avons configurée pour ce mot-clé dans Braze ? {#if-a-user-is-opted-out-and-sends-a-keyword-to-our-short-and-long-code-do-they-receive-the-response-we-configured-for-that-keyword-in-braze}

Si un utilisateur s'est désabonné et envoie un mot-clé appartenant à l'une des [catégories de mots-clés par défaut]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout), il recevra la réponse associée à ce mot-clé. Si un utilisateur s'est désabonné et envoie un [mot-clé personnalisé]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling), il ne recevra pas la réponse associée à ce mot-clé.

### Les propriétés d'événement SMS capturent-elles les mots-clés dans une phrase ? {#will-sms-event-properties-capture-keywords-in-a-sentence}

Pour qu'un mot-clé soit reconnu au sein d'une phrase (par exemple, « veuillez arrêter de m'envoyer des messages »), vous devez utiliser une instruction Liquid dans le message pour identifier le mot spécifique. Les propriétés d'événement ont une limite de 256 caractères ; en dehors de cela, il n'y a pas de limite de caractères.

## Test {#testing}

### Les SMS de test sont-ils décomptés des limites ? {#do-test-text-messages-count-toward-limits}

Oui. Gardez cela à l'esprit lors du test de vos messages.

### Un utilisateur doit-il faire partie d'un groupe d'abonnement SMS pour recevoir des SMS de test ? {#does-a-user-need-to-be-part-of-an-sms-subscription-group-to-receive-sms-test-messages}

Oui. Les utilisateurs doivent disposer d'un numéro de téléphone valide, faire partie du groupe d'abonnement SMS utilisé pour l'envoi de test et avoir au moins un pays sélectionné dans **Geographic Permissions** pour les SMS.

### Existe-t-il un moyen de vérifier si un alias existe sur un profil utilisateur ? {#is-there-a-way-to-see-if-an-alias-exists-on-a-user-profile}

Les alias ne sont pas visibles sur le profil utilisateur. Vous devez utiliser les endpoints [Exporter les données utilisateur]({{site.baseurl}}/api/endpoints/export) pour confirmer que les alias sont bien définis.

## MMS

### Y a-t-il des changements dans les données Currents lors de l'envoi d'un MMS ? {#are-there-any-changes-to-currents-data-when-sending-an-mms}

Non, le même niveau d'informations sera fourni lors de l'envoi d'un message MMS.

### Puis-je contrôler l'ordre dans lequel l'image et le corps du message d'un MMS sont distribués ? {#can-i-control-the-order-in-which-the-image-and-message-body-of-an-mms-are-delivered}

Braze n'a aucun contrôle sur l'ordre d'affichage lorsqu'un corps de message et des images sont inclus dans un message MMS. Cela dépend de plusieurs facteurs, notamment mais sans s'y limiter :

- L'opérateur recevant le message
- L'appareil recevant le message
- La taille globale du message

### Le MMS nécessite-t-il un processus d'onboarding séparé ? {#does-mms-require-a-separate-onboarding-process}

Non. Le MMS est désormais inclus dans notre processus d'onboarding SMS. Les clients existants qui ont déjà effectué l'onboarding peuvent commencer à envoyer des campagnes MMS après avoir complété les étapes suivantes :

1. Acheter le MMS.
2. Contacter l'équipe d'onboarding de Braze pour demander l'activation de la fonctionnalité MMS. Cela activera le MMS et un groupe d'abonnement SMS/MMS sera créé ou mis à jour pour vous.

Ensuite, l'équipe d'onboarding de Braze s'assurera que vos codes courts et longs sont activés (aux États-Unis et au Canada) pour le MMS. Elle mettra également à jour vos groupes d'abonnement pour afficher vos numéros actuels qui ont été ajoutés ou activés pour le MMS. Une fois ces étapes terminées, vous pouvez envoyer des messages MMS immédiatement depuis notre compositeur SMS natif.

### Pourquoi ne puis-je pas trouver le MMS sur mon tableau de bord alors que la fonctionnalité est activée ? {#why-cant-i-find-mms-on-my-dashboard-even-though-the-feature-is-enabled}

Le MMS n'est affiché sur le tableau de bord de Braze que lorsqu'un groupe d'abonnement est considéré comme « activé pour le MMS ». Cela se reflète par une étiquette MMS lors de la sélection du groupe d'abonnement dans le compositeur d'un message SMS/MMS. Cela signifie qu'au moins un numéro dans le groupe d'abonnement est capable d'envoyer un message MMS.

De plus, certaines situations nécessiteront que Twilio réapprouve l'activation de codes courts qui n'avaient pas initialement le MMS activé. Ce processus d'approbation peut prendre plusieurs semaines.

### Pourquoi mon MMS contenant une image ne parvient-il pas à s'envoyer ? {#why-does-my-mms-with-an-image-fail-to-send}

Certains fournisseurs SMS valident l'en-tête `Content-Type` des URL d'images. Si un MMS contenant une image est interrompu, vérifiez que l'URL de l'image hébergée renvoie `image/png` ou un autre type d'image pris en charge (par exemple, avec `curl -I <image-url>`). Hébergez à nouveau la ressource dans la bibliothèque multimédia de Braze ou sur un CDN qui renvoie le bon `Content-Type`.

### Pourquoi l'image de ma fiche contact n'apparaît-elle pas dans un MMS ? {#why-doesnt-my-contact-card-image-appear-in-an-mms}

Les photos des fiches contact MMS peuvent ne pas s'afficher lorsque le fichier de la fiche contact fait référence à une URL d'image que l'appareil du destinataire ne peut pas récupérer. Créez la fiche contact sur un téléphone, exportez le fichier, puis téléchargez-le dans la bibliothèque multimédia pour l'utiliser dans votre message MMS.

## RCS

### Pourquoi mon message RCS ne s'affiche-t-il pas correctement sur les appareils iOS ? {#why-doesnt-my-rcs-message-render-accurately-on-ios-devices}

Les messages RCS peuvent s'afficher différemment sur un appareil iOS en fonction du système d'exploitation et de l'application de messagerie. Sur les appareils iOS, les comportements suivants peuvent se produire :

- Les actions suggérées provenant de différents messages RCS dans le même fil de conversation peuvent être regroupées et affichées dans le mauvais ordre.
- Les boutons de carte enrichie et les actions suggérées situées en dehors de la carte enrichie peuvent rester visibles même après avoir appuyé sur un bouton de carte enrichie ou une action suggérée.
- Les GIF dans les cartes enrichies s'affichent sous forme d'images statiques. Pour plus de détails, consultez [Pourquoi les GIF dans les cartes enrichies RCS apparaissent-ils comme statiques sur iOS ?](#why-do-gifs-in-rcs-rich-cards-appear-static-on-ios).

{% alert note %}
Braze envoie le payload RCS que vous composez, tandis que le client de messagerie contrôle la façon dont les actions suggérées sont ordonnées, regroupées et masquées. Veillez à tester les messages RCS, en particulier ceux qui utilisent des cartes enrichies avec des actions suggérées ou des réponses suggérées, sur les appareils Android et iOS avant l'envoi.
{% endalert %}

### Pourquoi les GIF dans les cartes enrichies RCS apparaissent-ils comme statiques sur iOS ? {#why-do-gifs-in-rcs-rich-cards-appear-static-on-ios}

Sur iOS, les GIF dans les cartes enrichies RCS s'affichent sous forme d'image statique (la première image). Sur Android, ils s'animent comme prévu.

Le client de messagerie iOS contrôle ce comportement. Un GIF peut toujours s'animer dans l'aperçu Braze. Envoyez un message de test à un appareil iOS pour vérifier l'apparence du message livré.

Pour envoyer du contenu animé sur iOS :

- Utilisez un message RCS de type **Média**, qui envoie le GIF sous forme de fichier
- Utilisez une vidéo dans la carte enrichie

### Puis-je envoyer des messages vocaux préenregistrés avec RCS ? {#can-i-send-pre-recorded-voicemails-with-rcs}

Oui, vous pouvez utiliser les messages multimédias pour prendre en charge les fichiers audio.

### Pourquoi les abonnements SMS via la REST API ne correspondent-ils pas au **Total des abonnements** sur la page SMS/MMS/RCS Performance ? {#why-do-rest-api-sms-opt-ins-not-match-total-opt-ins-on-smsmmsrcs-performance}

Le **Total des abonnements** et le **Total des désabonnements** sur le tableau de bord [SMS/MMS/RCS Performance]({{site.baseurl}}/user_guide/analytics/dashboards) comptabilisent les changements d'abonnement déclenchés par le traitement des mots-clés SMS entrants (par exemple, un utilisateur envoyant un mot-clé d'abonnement à votre code court). Ils n'incluent pas toutes les mises à jour d'abonnement effectuées via la REST API, le tableau de bord ou d'autres sources.

Pour analyser les abonnements et les désabonnements par source, utilisez le [Générateur de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder) sur `USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED` et filtrez sur `STATE_CHANGE_SOURCE` (par exemple, **Rest API** versus **Inbound Message**).