---
nav_title: Créer une campagne
article_title: Créer une campagne
page_order: 1
page_type: tutorial
description: "Découvrez comment créer une campagne de communication Braze, de la rédaction au lancement, y compris les envois multicanaux, et comment planifier la distribution, cibler les audiences, affecter des événements de conversion, envoyer des tests et lancer."
tool: Campaigns
---

# Créer une campagne {#create-a-campaign}

> Utilisez les campagnes lorsque vous souhaitez atteindre les consommateurs avec une seule étape de communication sur un ou plusieurs canaux pris en charge. Pour les parcours à plusieurs étapes, utilisez [Canvas]({{site.baseurl}}/user_guide/messaging/canvas).

## Prérequis {#prerequisites}

Pour créer et lancer une campagne, vous avez besoin des permissions « Edit Campaigns » et « Launch Campaigns ». Pour une liste complète des permissions d'espace de travail et leur affichage dans le tableau de bord, consultez [Permissions]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

### Avant de commencer {#before-you-begin}

- Créez ou choisissez les [segments]({{site.baseurl}}/user_guide/audience/segments) qui définissent les destinataires de vos messages.
- Consultez les [bases des campagnes]({{site.baseurl}}/user_guide/messaging/campaigns/campaign_basics) pour vous assurer que les canaux de communication, les types de réception et les objectifs de conversion correspondent à votre cas d'usage.
- Pour un parcours guidé sur la réception, le ciblage et les conversions, suivez le cours d'apprentissage Braze [Campaign Setup](https://learning.braze.com/campaign-setup-delivery-targeting-conversions).
- Demandez à Operator de vous aider à rédiger votre campagne à partir d'un brief, ou à affiner vos choix de ciblage et de réception. Pour en savoir plus, consultez [Ce que vous pouvez faire avec Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#campaigns-and-audiences).

## Compositeur de campagne {#campaign-composer}

Le compositeur de campagne est l'endroit où vous définissez les paramètres de réception, d'audiences, de conversions et de lancement. Décidez si vous créez une campagne monocanal ou multicanal avant de continuer.

{% tabs %}
{% tab Monocanal %}

Une campagne monocanal atteint les utilisateurs via un seul canal de communication par lancement.

### Ce qui change {#whats-different}

#### Conversions et rapports {#single-channel-conversions}

Pour les campagnes monocanal, Braze suit les [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) que vous assignez à la campagne par rapport aux envois de ce canal. Pour les fenêtres d'attribution et les règles de comptage, consultez [Règles de suivi des conversions]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#conversion-tracking-rules).

Les [limites de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) et les limites d'envoi de l'espace de travail s'appliquent toujours.

### Créer une campagne monocanal {#create-a-single-channel-campaign}

Pour créer une campagne :

1. Accédez à **Messaging** > **Campaigns**.
2. Sélectionnez **Create campaign**.
3. Sélectionnez le [canal]({{site.baseurl}}/user_guide/channels) adapté à votre cas d'usage.
4. À l'[étape de composition](#step-1-compose-messages), rédigez et prévisualisez le contenu pour ce canal.

Chaque campagne utilise un seul type de canal à la fois. Ajoutez des variantes lorsque vous souhaitez comparer des déclinaisons créatives ou effectuer un [test A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% endtab %}
{% tab Multicanal %}

Une campagne multicanal atteint les utilisateurs via plusieurs canaux de communication en un seul lancement. Par exemple, vous pouvez envoyer un e-mail et une notification push simultanément.

{% alert note %}
Les [In-App Messages]({{site.baseurl}}/user_guide/channels/in_app_messages) ne sont pas disponibles dans les campagnes multicanal. Créez plutôt une campagne monocanal ou un Canvas.
{% endalert %}

### Ce qui change

#### Groupes de contrôle {#multichannel-control-groups}

Les groupes de contrôle de campagne comparent les variantes au sein d'un même canal (par exemple, E-mail A contre E-mail B). Ils ne servent pas à comparer des canaux entiers au sein d'une même campagne multicanal. Pour tester les canaux, les créations ou le timing ensemble tout au long d'un parcours, utilisez [Canvas]({{site.baseurl}}/user_guide/messaging/canvas).

#### Conversions et rapports {#multichannel-conversions}

Pour les campagnes multicanal, Braze suit les [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) par canal. Lorsqu'un utilisateur convertit après avoir reçu des messages sur plusieurs canaux, Braze peut attribuer cette conversion à l'ensemble de ces canaux. Le nombre de conversions peut dépasser le nombre d'*utilisateurs uniques*, et les taux peuvent dépasser 100 %. Pour les règles complètes, consultez [Règles de suivi des conversions]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#conversion-tracking-rules).

Les limites de débit pour les envois couvrant plusieurs canaux sont décrites dans [Campagnes multicanal et Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#multichannel-campaigns-and-canvases). Pour les règles à l'échelle de l'espace de travail (y compris la façon dont les envois multicanal sont comptabilisés dans les plafonds), consultez [Limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).

### Créer une campagne multicanal {#create-a-multichannel-campaign}

1. Accédez à **Messaging** > **Campaigns**.
2. Sélectionnez **Create campaign**.
3. Sélectionnez **Multichannel**.
4. À l'[étape de composition](#step-1-compose-messages), sélectionnez **Add channel** et choisissez chaque canal dont vous avez besoin. Sélectionnez les icônes de canal pour basculer entre les compositeurs pendant que vous rédigez le contenu de chaque canal.

{% endtab %}
{% endtabs %}

## Étape 1 : Rédiger les messages {#step-1-compose-messages}

### Détails de la campagne {#campaign-details}

Utilisez les champs suivants pour enregistrer les métadonnées qui aident votre équipe à trouver et gérer la campagne.

| Champ | Objectif |
| --- | --- |
| Nom | Utilisez un nom clair qui reflète l'objectif de la campagne. |
| Description | Facultatif. Expliquez l'intention ou ajoutez des liens vers des briefs pour les collaborateurs. |
| Équipe | Facultatif. Affectez des [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) pour que les bons groupes puissent modifier ou consulter les rapports de cet envoi. |
| Étiquettes | Facultatif. Ajoutez des [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) pour filtrer dans les listes et les outils tels que le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reports/report_builder). |
| ID de campagne | Lorsqu'il est affiché dans l'éditeur ou le résumé, copiez cet identifiant pour les appels API, les rapports et les intégrations qui font référence à une campagne spécifique. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Détails de la campagne" }

### Canaux et éditeurs {#channels-and-editors}

Rédigez le contenu spécifique à chaque canal dans cette étape. Pour des instructions détaillées, consultez [Canaux]({{site.baseurl}}/user_guide/channels) et ouvrez l'article correspondant au canal que vous avez sélectionné.

### Variantes {#variants}

Ajoutez des variantes lorsque vous souhaitez comparer des déclinaisons créatives ou de distribution. Pour en savoir plus sur les expériences et les contrôles, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Lorsque chaque variante utilise un contenu similaire, rédigez le message **avant** d'ajouter des variantes supplémentaires. Utilisez ensuite **Copier depuis la variante** dans le menu **Ajouter une variante** pour réutiliser votre travail entre les variantes ou les canaux.
{% endalert %}

## Étape 2 : Planifier la distribution {#step-2-schedule-delivery}

Choisissez quand les utilisateurs deviennent éligibles pour recevoir la campagne :

| Type de distribution | Résumé |
| --- | --- |
| [Distribution planifiée]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery) | Envoyez à une heure ou une cadence spécifiée. |
| [Livraison par événement]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) | Envoyez lorsque les utilisateurs effectuent des comportements ou remplissent des conditions que vous définissez. |
| [Distribution déclenchée par API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) | Envoyez lorsque vos systèmes appellent Braze pour déclencher la campagne pour les utilisateurs éligibles. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 2 : Planifier la distribution" }

Pour les concepts de planification dans Braze, consultez [Planifier votre campagne]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

### Contrôles de distribution {#delivery-controls}

Selon le type de distribution, vous pouvez ajuster la [rééligibilité]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) (si les utilisateurs peuvent entrer à nouveau dans la campagne) et respecter les règles de [limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) de l'espace de travail. Vous pouvez également configurer les [heures calmes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) pour que les messages ne soient pas envoyés pendant des fenêtres restreintes.

## Étape 3 : Cibler les audiences {#step-3-target-audiences}

Dans **Publics cibles**, définissez qui est éligible pour recevoir la campagne. Pour toutes les options de ciblage, les parcours de l'interface et les captures d'écran, consultez [Cibler les utilisateurs]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users).

### Options de ciblage {#targeting-options}

Dans cette section, vous pouvez cibler les utilisateurs en choisissant des Segments ou des filtres pour affiner votre audience. Les utilisateurs éligibles doivent toujours remplir le déclencheur ou les critères que vous définissez à l'étape **Planifier la distribution**. L'audience cible fonctionne comme une salle d'attente : seules les personnes déjà à l'intérieur peuvent avancer lorsque l'action suivante se produit.

Les [listes de suppression]({{site.baseurl}}/user_guide/audience/suppression_lists) de l'espace de travail excluent automatiquement les utilisateurs répertoriés, sauf si vous autorisez une exception pour cette campagne.

### Résumé de l'audience {#audience-summary}

Après avoir ajouté des Segments ou des filtres, le **résumé de l'audience** donne un aperçu de la population de ce segment, y compris le nombre d'utilisateurs joignables via les canaux sélectionnés. Les comptages de joignabilité reflètent les données de votre espace de travail, la configuration des canaux et les filtres. Gardez à l'esprit que l'appartenance exacte au segment est toujours calculée avant l'envoi du message. Pour les très grandes audiences, Braze peut afficher des estimations jusqu'à ce que vous calculiez les statistiques exactes.

{% alert note %}
Si vous avez configuré un [groupe de contrôle global]({{site.baseurl}}/user_guide/audience/global_control_group), le nombre d'utilisateurs joignables affiché dans l'audience cible de votre campagne est inférieur au nombre d'utilisateurs joignables affiché pour le même segment. Cela s'explique par le fait que la campagne exclut les utilisateurs du groupe de contrôle global, contrairement au comptage du segment.
{% endalert %}

### Recherche d'utilisateur {#user-lookup}

Après avoir ajouté des Segments ou des filtres, vous pouvez vérifier si votre audience est configurée comme prévu en recherchant un utilisateur pour confirmer qu'il correspond aux critères du segment. Pour ce faire, recherchez l'`external_id` ou le `braze_id` d'un utilisateur dans la section **Recherche d'utilisateur**. Vous ne pouvez pas effectuer de recherche par adresse e-mail ici. Consultez [Tester les segments]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments) pour en savoir plus.

Lorsqu'un utilisateur correspond aux critères du segment, du filtre et de l'application, une alerte l'indique. Lorsqu'un utilisateur ne correspond pas à une partie ou à l'ensemble des critères du segment, du filtre ou de l'application, les critères manquants sont répertoriés à des fins de résolution des problèmes.

### Envoyer à ces utilisateurs {#send-to-these-users}

Pour les canaux basés sur l'abonnement (e-mail, SMS et similaires), utilisez **Envoyer à ces utilisateurs** pour n'envoyer votre campagne qu'aux utilisateurs ayant un statut d'abonnement spécifique, comme ceux qui sont abonnés et ont opté pour l'e-mail.

### Limiter le volume d'envoi {#limit-send-volume}

Vous pouvez limiter le nombre total d'utilisateurs qui reçoivent votre message. Cela sert de vérification indépendante de vos filtres de campagne. Pour plus de détails, consultez [Définir un plafond d'utilisateurs maximum]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#setting-a-maximum-user-cap).

### Limiter le débit d'envoi de cette campagne {#limit-the-rate-at-which-this-campaign-sends}

Si vous anticipez que de grandes campagnes provoquent un pic d'activité utilisateur et surchargent vos serveurs, vous pouvez spécifier une limite de débit par minute pour l'envoi des messages, ce qui signifie que Braze n'envoie pas plus que votre paramètre de limite de débit en une minute. Pour plus de détails, consultez [Limitation du débit de distribution]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting).

### Tests A/B {#ab-testing}

Vous pouvez créer un [test multivarié ou A/B]({{site.baseurl}}/user_guide/messaging/ab_testing) pour toute campagne ciblant un seul canal, même si ce canal inclut plusieurs appareils. Par exemple, si vous souhaitez utiliser un test multivarié ou A/B pour une campagne push, vous pouvez cibler uniquement les appareils iOS ou uniquement les appareils Android, mais pas les deux types d'appareils dans la même campagne.

Pour les campagnes push, e-mail et webhook planifiées pour un envoi unique, vous pouvez également utiliser une [optimisation]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations). Une optimisation réserve une partie de votre audience cible du test A/B et la conserve pour un second envoi optimisé basé sur les résultats du premier test.

## Étape 4 : Affecter des événements de conversion {#step-4-assign-conversion-events}

Les [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) mesurent les résultats après qu'un utilisateur a reçu votre campagne (ou est entré dans le groupe de contrôle). Braze définit par défaut **Starts Session** dans une courte fenêtre (trois jours). Vous pouvez définir des événements de conversion correspondant à vos KPI, jusqu'à quatre événements par campagne.

Après le lancement, utilisez le [tableau de bord des conversions]({{site.baseurl}}/user_guide/analytics/dashboards/conversions) pour analyser les tendances de conversion sur plusieurs campagnes ou Canvas, comparer les canaux et ajuster les plages de dates, les méthodes d'attribution et les ventilations en un seul endroit.

{% alert important %}
Vous ne pouvez pas ajouter ou supprimer des événements de conversion après le lancement de la campagne. Confirmez les événements avant de lancer.
{% endalert %}

## Étape 5 : Vérifier le résumé et lancer {#step-5-review-summary-and-launch}

L'étape **Résumé de vérification** affiche la planification, l'audience, les variantes et les choix de communication. Avant de lancer votre campagne :

1. Confirmez que les segments, les variantes et les paramètres de distribution correspondent à votre intention.
2. [Envoyez des messages de test]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) pour valider le rendu et le comportement sur vos appareils de test ou auprès de destinataires internes.

Lorsque vous êtes prêt, sélectionnez **Lancer la campagne**.

### Approbations {#approvals}

Si votre espace de travail utilise les approbations, un membre de l'équipe disposant de l'autorisation d'approuver les campagnes doit donner son accord avant le lancement. Pour plus d'informations, consultez [Approbations pour les campagnes et les Canvas]({{site.baseurl}}/user_guide/messaging/governance/approvals).

## Articles connexes {#related-articles}

- [Concevoir et modifier]({{site.baseurl}}/user_guide/messaging/design_and_edit)
- [Tests A/B]({{site.baseurl}}/user_guide/messaging/ab_testing)
- [À savoir avant d'envoyer]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/know_before_you_send)
- [Analyse de Campaign]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics)