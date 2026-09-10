---
nav_title: "Bonnes pratiques"
article_title: Bonnes pratiques pour les SMS, MMS et RCS
page_order: 2
description: "Cet article de référence présente les bonnes pratiques pour les SMS/MMS."
alias: /sms_mms_rcs_best_practices/
page_type: reference
channel:
  - SMS
  - MMS
  - RCS



---

# Bonnes pratiques pour les SMS, MMS et RCS {#best-practices-for-sms-mms-and-rcs}

> Découvrez les bonnes pratiques pour les SMS, MMS et RCS avec Braze, y compris nos recommandations pour le suivi des désinscriptions et le trafic frauduleux (traffic pumping).

## Recommandations relatives à la surveillance des désabonnements {#opt-out-monitoring-recommendations}

Le respect des demandes de désabonnement des destinataires est une obligation légale. Le non-respect des demandes de désabonnement des destinataires de SMS peut entraîner des sanctions, y compris des amendes, et peut donner lieu à des poursuites judiciaires. Braze dispose de fonctionnalités permettant une gestion robuste de l'abonnement et du désabonnement aux SMS et MMS, ainsi que de mécanismes contribuant à s'assurer que les demandes sont correctement traitées.

En vertu de leurs contrats d'abonnement avec nous, nos clients sont seuls responsables du respect de la législation applicable dans le cadre de leur utilisation de nos services. Par conséquent, nous recommandons vivement aux clients de porter une attention particulière à la configuration de leurs paramètres SMS, de tester ces configurations de manière approfondie, de prendre des mesures pour surveiller la conformité des désabonnements et d'agir rapidement s'ils identifient des cas de non-respect des demandes de désabonnement.

Lors de la configuration des SMS et MMS dans Braze pour gérer les abonnements et désabonnements, consultez la liste de ressources suivante :
* [Groupes d'abonnement SMS]({{site.baseurl}}/sms_rcs_subscription_groups) : groupes d'abonnement ainsi que méthodes et statuts d'abonnement et de désabonnement.
* [REST API des groupes d'abonnement]({{site.baseurl}}/api/endpoints/subscription_groups) : comment traiter les abonnements et désabonnements reçus d'une source autre qu'une réponse directe à un message.
* [Traitement des mots-clés]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing) : explications sur la façon dont Braze gère le traitement et la gestion des mots-clés.
* [Double abonnement SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) : exige que les utilisateurs confirment explicitement leur intention d'abonnement avant de pouvoir recevoir des messages SMS. Le double abonnement SMS est une obligation dans certains pays, c'est pourquoi Braze recommande de le configurer.
* [Envoi de messages SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sms_sending) : fondamentaux de l'envoi de SMS avec Braze, incluant l'importance des groupes d'abonnement, les exigences relatives aux segments SMS et aux corps de messages, et plus encore.

### Points à prendre en compte {#considerations}

Lorsque les SMS et MMS sont configurés sur plusieurs instances, une mauvaise configuration peut entraîner l'envoi des désabonnements de Campaign ou de Canvas vers le mauvais espace de travail.

* Braze dispose d'une surveillance pour identifier de tels cas. Si ce comportement est détecté, Braze redirige les désabonnements vers l'instance correcte et rattrape tous les désabonnements survenus pendant la période concernée.
* Nous recommandons vivement aux clients de tester les désabonnements pour chaque groupe d'abonnement qu'ils possèdent dans Braze. Identifier ce problème avant le lancement d'un message est préférable à la résolution après qu'un problème a été identifié.

Braze gère les abonnements SMS/MMS à la fois au niveau du profil utilisateur (`user_id`) et au niveau du numéro de téléphone (`channel_id`). Lorsqu'un numéro de téléphone est abonné ou désabonné, la mise à jour s'applique à tous les profils partageant ce numéro. Dans le cas où un utilisateur final s'est abonné avec un certain numéro de téléphone puis change de numéro, le nouveau numéro hérite du statut du groupe d'abonnement de l'utilisateur. Ainsi, si un utilisateur final s'est désabonné puis accède à nouveau à l'application ou au site avec un nouveau numéro de téléphone, il ne reçoit pas de messages non sollicités.

## Recommandations pour l'hygiène de la liste des numéros de téléphone {#phone-number-list-hygiene-recommendations}

Maintenir l'hygiène de votre liste de numéros de téléphone vous aide à conserver des données de consentement et de joignabilité valides au fil du temps. Braze marque certains numéros de téléphone comme invalides afin de réduire les risques de non-conformité, de soutenir les pratiques de communication basées sur le consentement et d'éviter d'envoyer des messages à des numéros qui n'appartiennent peut-être plus à l'utilisateur d'origine.

Pour connaître les raisons pour lesquelles les numéros de téléphone sont généralement marqués comme invalides, consultez [Gestion des numéros de téléphone invalides]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#handling-invalid-phone-numbers).

Nous recommandons le flux de travail suivant pour supprimer les numéros de téléphone invalides :

1. Identifiez les numéros de téléphone concernés via l'[endpoint `/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers).
2. Distinguez les numéros de téléphone désactivés, ceux marqués comme invalides en raison d'erreurs du fournisseur et ceux marqués comme invalides en raison de problèmes de formatage (`invalid_format`, comme les numéros non conformes au format E.164). Utilisez le filtre `reason` sur l'API des numéros de téléphone invalides pour effectuer une requête par catégorie. Pour plus d'informations, consultez [Gestion des numéros de téléphone invalides]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#handling-invalid-phone-numbers).
3. Pour les numéros de téléphone désactivés, vérifiez à nouveau le numéro de téléphone auprès de l'utilisateur. Une fois que l'utilisateur a confirmé son numéro de téléphone, supprimez le numéro de la liste des invalides via l'[endpoint `/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers).

## Recommandations concernant le traffic pumping {#traffic-pumping-recommendations}

### Qu'est-ce que le traffic pumping ? {#what-is-traffic-pumping}

Le traffic pumping est une forme de fraude qui survient lorsqu'un acteur malveillant utilise un formulaire en ligne pour déclencher l'envoi de SMS en masse (par exemple, des messages d'abonnement ou des mots de passe à usage unique). L'acteur malveillant met en place un numéro surtaxé vers lequel ces messages sont envoyés et perçoit une part des revenus auprès de l'opérateur mobile avec lequel le numéro surtaxé a été configuré, générant ainsi des revenus illicites.

### Comment détecter le traffic pumping {#how-to-spot-traffic-pumping}

* Les numéros surtaxés utilisés pour ce type d'arnaque sont souvent, mais pas toujours, configurés dans des pays situés en dehors de vos zones d'envoi habituelles.
* Des pics inhabituels dans l'envoi de messages depuis des formulaires en ligne peuvent indiquer du traffic pumping.
    * Nous vous recommandons de configurer des [alertes de campagne]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/campaign_alerts) pour plafonner et recevoir une notification si un nombre anormalement élevé de messages est envoyé.
* Des formulaires en ligne remplis de manière incomplète peuvent indiquer un remplissage automatisé.
* Lors de la création de formulaires en ligne, nous vous recommandons de définir des règles pour vous assurer que les formulaires sont entièrement remplis et d'utiliser des outils tels que les CAPTCHA pour minimiser les risques.

### Impact du traffic pumping {#impact-of-traffic-pumping}

Les clients sont responsables de la surveillance du trafic qu'ils envoient et sont facturés pour tous les SMS envoyés via leur compte. Entre Braze et le client, c'est le client qui est le mieux placé pour détecter et prévenir le traffic pumping.

## Envoi de SMS multi-pays {#multi-country-sms-sending}

Certaines marques peuvent souhaiter envoyer des messages à un groupe d'utilisateurs dont les numéros de téléphone proviennent de différents pays. Pour envoyer un SMS à un numéro de téléphone dans un pays donné, il est recommandé d'utiliser un code long ou un code court provenant du même pays. En effet, les codes courts ne peuvent envoyer des SMS qu'aux numéros de téléphone du même pays que celui dans lequel le code court a été créé.

Pour contourner cette limitation, lors du [processus de configuration]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups) des groupes d'abonnement, les groupes peuvent être configurés pour contenir des codes longs et des codes courts de plusieurs pays différents. Une fois cette configuration terminée, les numéros de téléphone dont l'indicatif pays correspond à celui du numéro de téléphone de l'utilisateur cible sont automatiquement utilisés lors du lancement d'une Campaign. Vous n'avez pas besoin de créer des Campaigns distinctes pour les utilisateurs dont les numéros de téléphone ont des indicatifs pays différents, ce qui vous permet de lancer une seule Campaign ou d'utiliser un seul composant Canvas pour cibler les utilisateurs concernés.

![Les payloads SMS sont envoyés en utilisant le même indicatif pays que le numéro de téléphone de l'utilisateur cible.]({% image_buster /assets/img/sms/multi_country_subgroups.png %})

### Bonnes pratiques générales d'envoi {#general-sending-best-practices}

1. **Obtenez le consentement.** L'une des règles les plus importantes pour utiliser le SMS en tant qu'entreprise est d'obtenir au préalable l'autorisation de vos clients pour les contacter. Ne pas le faire peut nuire à votre marque et entraîner des frais juridiques importants.
2. **Choisissez le bon numéro pour votre cas d'usage.** Trois types principaux de numéros de téléphone peuvent envoyer et recevoir des SMS : les codes longs, les codes courts et les identifiants d'expéditeur alphanumériques. Leurs capacités et leur disponibilité varient selon les régions. Réfléchissez à l'avance si un code personnalisé serait plus adapté à votre activité.
3. **Soignez le timing.** Gardez à l'esprit que les clients sont plus réceptifs aux contenus qui leur sont directement adressés. Un peu de personnalisation fait toute la différence, comme utiliser le prénom du destinataire ou ajouter une touche conversationnelle qui reflète les centres d'intérêt de vos clients.
4. **Engagez des conversations bidirectionnelles.** Le SMS est un canal si efficace pour interagir avec les clients qu'il est important d'anticiper et de gérer efficacement les réponses à vos messages. 85 % des consommateurs souhaitent non seulement recevoir des informations, mais aussi répondre aux entreprises ou engager une conversation.
5. **Mesurez ce qui fonctionne.** Contactez-vous vos clients au bon moment, à la bonne fréquence et avec les appels à l'action les plus efficaces ? L'utilisation des bons outils de suivi permet d'obtenir des indicateurs directs et mesurables qui prouvent leur ROI.

## Envois à haut volume {#high-volume-sending}

Vous prévoyez des envois à haut volume ? Voici quelques bonnes pratiques pour que tout se passe sans accroc.

- Ajustez la limitation du débit de réception de votre Campaign ou de vos Canvas selon vos besoins, en fonction de la taille de l'audience cible. Cela vous permet d'atteindre le volume d'envoi souhaité et de vous assurer que Braze envoie les messages au rythme attendu et supporté par votre fournisseur SMS ou RCS.
- Veillez à respecter la limite de 160 caractères et tenez compte du fait que certains caractères spéciaux comptent double (par exemple, les barres obliques inversées `\`, les accents circonflexes `^` et les tildes `~`).

## Recommandations pour les heures calmes {#quiet-hours-recommendations}

{% alert warning %}
**Les heures calmes natives de Braze ne garantissent pas les horaires de réception au niveau de l'appareil.** Lorsqu'un message est envoyé, il est transmis à un opérateur. Une fois que l'opérateur a accepté le message, Braze n'a plus de contrôle sur le moment précis où il est livré sur l'appareil de l'utilisateur.<br><br> Par exemple, si un message est transmis à un opérateur à 20 h 59, il peut ne pas arriver sur l'appareil avant 21 h 02. Pour réduire ce risque, nous recommandons d'utiliser la méthode d'heures calmes basée sur Liquid décrite ci-dessous. Celle-ci supprime le message au niveau du moteur Braze avant la transmission.
{% endalert %}

### Heures calmes natives de Braze {#braze-native-quiet-hours}

Vous pouvez activer les [heures calmes]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing#quiet-hours) pour les SMS Campaigns et les Canvas en tant que contrôle de planification supplémentaire. Pour les envois soumis à des exigences de conformité, utilisez la protection basée sur Liquid décrite dans la section suivante comme contrôle principal avant que les messages ne soient transmis aux opérateurs.

### Protection supplémentaire via les Content Blocks {#additional-safeguard-through-content-blocks}

Vous pouvez ajouter une vérification basée sur Liquid à l'intérieur d'un Content Block. Cela fournit une protection fiable et évolutive qui fonctionne en complément des paramètres natifs.

#### Configuration {#setup}

Incluez l'extrait de code suivant en haut du corps de votre message SMS. Cet exemple annule l'envoi s'il se situe en dehors d'une fenêtre de 9 h à 21 h dans le [fuseau horaire local]({{site.baseurl}}/user_guide/messaging/campaigns/faq#what-does-local-time-zone-delivery-offer) de l'utilisateur.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour >= 21 or hour < 9 %}
  {% abort_message("Outside allowed time window") %}
{% endif %}
```
{% endraw %}

#### Points à prendre en compte

- {% raw %}`time_zone: ${time_zone}`{% endraw %} permet d'évaluer la fenêtre par rapport au fuseau horaire local de chaque utilisateur, et non par rapport à un fuseau horaire global fixe, comme expliqué dans la [FAQ Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/faq#what-does-local-time-zone-delivery-offer).
- Les messages supprimés par {% raw %}`abort_message()`{% endraw %} ne sont pas reprogrammés pour le lendemain ; ils sont annulés.
- {% raw %} Par défaut, les messages annulés ne sont pas visibles dans les rapports standard de Campaign. Cependant, lorsque Liquid annule un envoi avec `{% abort_message %}`, Braze l'enregistre dans le journal d'activité des messages en tant qu'erreur de message (par défaut, `{% abort_message %}` called s'affiche). Si vous transmettez une chaîne de caractères, cette raison est celle qui apparaît dans le journal, comme `{% abort_message('language was nil') %}`{% endraw %}. Pour avoir de la visibilité sur ces suppressions dans le tableau de bord, contactez votre gestionnaire de la satisfaction client pour accéder au [tableau de bord de diagnostic de la communication]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard).