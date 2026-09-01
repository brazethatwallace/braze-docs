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

## Recommandations pour le suivi des désabonnements {#opt-out-monitoring-recommendations}

Le respect des demandes de désabonnement des destinataires est exigé par la loi. Le non-respect des demandes de désabonnement des destinataires par SMS peut entraîner des sanctions, y compris des amendes, et peut donner lieu à des poursuites judiciaires. Braze dispose de fonctionnalités permettant une gestion robuste des abonnements et désabonnements SMS et MMS, ainsi que des mécanismes pour s'assurer que les demandes sont correctement traitées.

En vertu de leurs contrats d'abonnement conclus avec nous, nos clients sont seuls responsables de leur conformité aux lois applicables dans le cadre de l'utilisation de nos services. Nous recommandons donc vivement à nos clients de porter une attention particulière à la configuration correcte de leur environnement SMS, de tester minutieusement ces configurations, de prendre des mesures pour surveiller la conformité des désabonnements et d'agir rapidement s'ils identifient des cas de non-respect des demandes de désabonnement.

Lors de la configuration des SMS et MMS dans Braze pour gérer les abonnements et les désabonnements, consultez la liste de ressources suivante :
* [Groupes d'abonnement SMS]({{site.baseurl}}/sms_rcs_subscription_groups) : Groupes d'abonnement, méthodes et statuts d'abonnement/désabonnement.
* [REST API des groupes d'abonnement]({{site.baseurl}}/api/endpoints/subscription_groups) : Comment traiter les abonnements et désabonnements reçus depuis une source autre qu'une réponse directe à un message.
* [Traitement des mots-clés]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing) : Explications sur la manière dont Braze gère le traitement et la gestion des mots-clés.
* [Double abonnement SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) : Exige que les utilisateurs confirment explicitement leur intention d'abonnement avant de pouvoir recevoir des messages SMS. Le double abonnement SMS est une exigence dans certains pays, c'est pourquoi Braze recommande de le configurer.
* [Envoi de messages SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sms_sending) : Les fondamentaux de l'envoi de SMS avec Braze, notamment l'importance des groupes d'abonnement, les exigences relatives aux segments SMS et aux corps de message, et plus encore.

### Points à prendre en compte {#considerations}

Lorsque les SMS et MMS sont configurés sur plusieurs instances, une mauvaise configuration peut entraîner l'envoi des désabonnements de Campaign ou de Canvas vers le mauvais espace de travail.

* Braze dispose d'un système de surveillance pour identifier de tels cas. Si ce comportement est détecté, Braze applique ces désabonnements à la bonne instance et complète rétroactivement ceux survenus pendant la période concernée.
* Nous recommandons vivement aux clients de tester les désabonnements pour chaque groupe d'abonnement dont ils disposent dans Braze. Identifier ce problème avant de lancer un message est préférable à le résoudre après qu'un incident a été constaté.

Braze gère les abonnements SMS/MMS à la fois au niveau du profil utilisateur (`user_id`) et au niveau du numéro de téléphone (`channel_id`). Lorsqu'un numéro de téléphone est abonné ou désabonné, la mise à jour s'applique à tous les profils qui partagent ce numéro. Dans le cas où un utilisateur s'est abonné avec un certain numéro de téléphone, puis change de numéro, le nouveau numéro hérite du statut du groupe d'abonnement de l'utilisateur. Par conséquent, si un utilisateur s'est désabonné, puis accède de nouveau à l'application ou au site web avec un nouveau numéro de téléphone, il ne reçoit pas de messages indésirables.

## Recommandations pour l'hygiène de la liste de numéros de téléphone {#phone-number-list-hygiene-recommendations}

Le maintien de l'hygiène de la liste de numéros de téléphone vous aide à conserver des données de consentement et de joignabilité valides au fil du temps. Braze marque certains numéros de téléphone comme invalides afin de réduire les risques de non-conformité, de soutenir les pratiques de communication basées sur le consentement et d'éviter l'envoi de messages à des numéros qui pourraient ne plus appartenir à l'utilisateur d'origine.

Pour connaître les raisons pour lesquelles les numéros de téléphone sont généralement marqués comme invalides, consultez [Gestion des numéros de téléphone invalides]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#handling-invalid-phone-numbers).

Nous recommandons le workflow suivant pour supprimer les numéros de téléphone invalides :

1. Identifiez les numéros de téléphone concernés via l'[endpoint `/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers).
2. Faites la distinction entre les numéros de téléphone désactivés et les numéros de téléphone ayant reçu des erreurs de la part du fournisseur.
3. Pour les numéros de téléphone désactivés, vérifiez à nouveau le numéro de téléphone auprès de l'utilisateur. Une fois que l'utilisateur a confirmé son numéro de téléphone, supprimez le numéro de téléphone de la liste des numéros invalides via l'[endpoint `/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers).

## Recommandations contre le traffic pumping {#traffic-pumping-recommendations}

### Qu'est-ce que le traffic pumping ? {#what-is-traffic-pumping}

Le traffic pumping est une forme de fraude qui se produit lorsqu'un acteur malveillant utilise un formulaire en ligne pour déclencher l'envoi de messages SMS en grand volume (par exemple, des messages d'abonnement ou des mots de passe à usage unique). L'acteur malveillant met en place un numéro surtaxé vers lequel ces messages sont envoyés et perçoit une part des revenus auprès de l'opérateur mobile avec lequel le numéro surtaxé a été configuré, générant ainsi des revenus illicites.

### Comment détecter le traffic pumping {#how-to-spot-traffic-pumping}

* Les numéros surtaxés utilisés pour ce type de fraude sont souvent, mais pas toujours, configurés dans des pays situés en dehors de vos zones d'envoi habituelles.
* Des pics inhabituels d'envoi de messages depuis des formulaires en ligne peuvent indiquer un traffic pumping.
    * Nous vous recommandons de configurer des [alertes de campagne]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/campaign_alerts) pour plafonner et être notifié si un nombre anormalement élevé de messages est envoyé.
* Des formulaires en ligne incomplets peuvent indiquer un remplissage programmatique de formulaires.
* Lors de la création de formulaires en ligne, nous vous recommandons de définir des règles pour vous assurer que les formulaires sont entièrement remplis et d'utiliser des outils tels que le CAPTCHA pour minimiser les risques.

### Impact du traffic pumping {#impact-of-traffic-pumping}

Les clients sont responsables de la surveillance du trafic qu'ils envoient et sont facturés pour tous les SMS envoyés via leur compte. Entre Braze et le client, c'est le client qui est le mieux placé pour détecter et prévenir le traffic pumping.

## Envoi de SMS multi-pays {#multi-country-sms-sending}

Certaines marques souhaitent envoyer des messages à un groupe d'utilisateurs dont les numéros de téléphone proviennent de différents pays. Pour envoyer un SMS à un numéro de téléphone dans un pays particulier, la bonne pratique consiste à utiliser un code long ou un code court originaire du même pays. En effet, les codes courts ne peuvent envoyer des SMS qu'aux numéros de téléphone du même pays que celui dans lequel le code court a été créé.

Pour pallier cette limitation, lors du [processus de configuration]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups) des groupes d'abonnement, les groupes peuvent être configurés pour contenir des codes longs et des codes courts de plusieurs pays différents. Une fois cette configuration effectuée, les numéros d'envoi partageant le même indicatif pays que le numéro de téléphone de l'utilisateur cible seront automatiquement utilisés lors du lancement d'une Campaign. Vous n'aurez pas besoin de créer des Campaigns distinctes pour les utilisateurs dont les numéros de téléphone ont des indicatifs pays différents, ce qui vous permet de lancer une seule Campaign ou d'utiliser un seul composant Canvas pour cibler les utilisateurs concernés.

![Les payloads SMS sont envoyés en utilisant le même indicatif pays que le numéro de téléphone de l'utilisateur cible.]({% image_buster /assets/img/sms/multi_country_subgroups.png %})

### Bonnes pratiques générales pour l'envoi {#general-sending-best-practices}

1. **Obtenez le consentement.** L'une des règles les plus importantes lors de l'utilisation du SMS en entreprise est de d'abord obtenir la permission des clients pour les contacter. Ne pas le faire peut nuire à votre marque et entraîner des frais juridiques importants.
2. **Choisissez le bon numéro pour votre cas d'usage.** Trois principaux types de numéros de téléphone peuvent envoyer et recevoir des SMS : les codes longs, les codes courts et les identifiants d'expéditeur alphanumériques. Leurs capacités et leur disponibilité selon les régions varient. Réfléchissez à l'avance pour déterminer si un code personnalisé conviendrait mieux à votre entreprise.
3. **Prêtez attention au timing.** Gardez à l'esprit que les clients sont plus réceptifs aux messages qui leur sont directement adressés. Un peu de personnalisation peut faire toute la différence, comme utiliser le prénom du destinataire ou ajouter une touche conversationnelle reflétant les centres d'intérêt de vos clients.
4. **Engagez des conversations bidirectionnelles.** Le SMS est un canal si efficace pour interagir avec les clients qu'il est important d'anticiper et de gérer efficacement les réponses à vos messages. 85 % des consommateurs souhaitent non seulement recevoir des informations, mais aussi répondre aux entreprises ou engager une conversation.
5. **Mesurez ce qui fonctionne.** Contactez-vous les clients au bon moment, à la bonne fréquence, et avec les appels à l'action les plus efficaces ? Utiliser les bons outils de suivi peut fournir des indicateurs directs et mesurables qui démontrent votre ROI.

## Envoi à haut volume {#high-volume-sending}

Vous prévoyez des envois à haut volume ? Voici quelques bonnes pratiques pour que tout se passe sans accroc.

- Ajustez la limitation du débit de distribution pour votre Campaign ou vos Canvas en fonction de la taille de l'audience cible. Cela garantit que vous atteignez le volume d'envoi souhaité et que Braze envoie les messages au rythme attendu par Twilio et que celui-ci peut gérer.
- Veillez à respecter la limite de 160 caractères et gardez à l'esprit que les caractères spéciaux comptent double (par exemple, les barres obliques inversées `\`, les accents circonflexes `^` et les tildes `~`).

## Recommandations relatives aux heures calmes {#quiet-hours-recommendations}

{% alert warning %}
**Les heures calmes natives de Braze ne garantissent pas les horaires de réception au niveau de l'appareil.** Lorsqu'un message est envoyé, il est transmis à un opérateur. Une fois que l'opérateur accepte le message, Braze n'a plus de contrôle sur le moment précis où il est livré sur l'appareil de l'utilisateur.<br><br> Par exemple, si un message est transmis à un opérateur à 20 h 59, il peut ne pas arriver sur l'appareil avant 21 h 02. Pour réduire ce risque, nous recommandons d'utiliser la méthode d'heures calmes basée sur Liquid décrite ci-dessous. Celle-ci supprime le message au niveau du moteur Braze avant la transmission.
{% endalert %}

### Heures calmes natives de Braze {#braze-native-quiet-hours}

Nous recommandons vivement d'activer les [heures calmes]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing#quiet-hours) sur l'ensemble de vos Campaigns et Canvas SMS afin de respecter les réglementations régionales et les bonnes pratiques.

### Protection supplémentaire via les Content Blocks {#additional-safeguard-through-content-blocks}

Vous pouvez ajouter une vérification basée sur Liquid à l'intérieur d'un Content Block. Cela offre une protection fiable et évolutive qui fonctionne en complément des paramètres natifs.

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

- {% raw %}`time_zone: ${time_zone}`{% endraw %} permet d'évaluer la fenêtre par rapport au fuseau horaire local de chaque utilisateur, et non par rapport à une heure globale fixe, comme expliqué dans la [FAQ Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/faq#what-does-local-time-zone-delivery-offer).
- Les messages supprimés par {% raw %}`abort_message()`{% endraw %} ne sont pas reprogrammés pour le jour suivant ; ils sont annulés.
- {% raw %} Par défaut, les messages annulés ne sont pas visibles dans les rapports standard de Campaign. Cependant, lorsque Liquid annule un envoi avec `{% abort_message %}`, Braze l'enregistre dans le journal d'activité des messages comme une erreur de message (par défaut, il affiche `{% abort_message %}` appelé). Si vous transmettez une chaîne de caractères, cette raison apparaît dans le journal, par exemple `{% abort_message('language was nil') %}`{% endraw %}. Pour avoir une visibilité sur ces suppressions dans le tableau de bord, contactez votre gestionnaire du succès des clients afin d'accéder au [tableau de bord de diagnostic de la communication]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard).