---
nav_title: FAQ
article_title: FAQ sur les Campaigns
page_order: 10
page_type: FAQ
description: "Cette page fournit des réponses aux questions fréquemment posées sur les Campaigns."
tool: Campaigns
---

# Questions fréquemment posées {#frequently-asked-questions}

> Cet article fournit des réponses à certaines questions fréquemment posées sur les Campaigns.

## Comment créer une campagne multicanal ? {#how-do-i-create-a-multichannel-campaign}

Consultez la section [Campaigns multicanal]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#create-a-multichannel-campaign) dans **Créer une Campaign** pour les étapes de configuration et les canaux pris en charge.

### Puis-je ajouter un groupe de contrôle à ma Campaign multicanal ? {#can-i-add-a-control-group-to-my-multichannel-campaign}

Consultez la section [Groupes de contrôle]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#multichannel-control-groups) dans **Créer une Campaign**. Pour les tests cross-canal, utilisez [Canvas]({{site.baseurl}}/user_guide/messaging/canvas).

### Comment puis-je commencer à tester et optimiser mes Campaigns ? {#what-are-some-ways-i-can-start-testing-and-optimizing-campaigns}

Les Campaigns multivariées et les Canvas avec plusieurs variantes sont un excellent point de départ ! Par exemple, vous pouvez exécuter une [Campaign multivariée]({{site.baseurl}}/user_guide/messaging/ab_testing) pour tester un message avec différentes versions de texte ou lignes d'objet. Les Canvas avec plusieurs variantes permettent de tester des workflows entiers.

### Pourquoi le taux d'ouverture de ma Campaign a-t-il diminué ? {#why-did-the-open-rate-for-my-campaign-decrease}

Un faible taux d'ouverture n'est pas toujours lié à un problème technique. Il peut y avoir des problèmes de troncature d'e-mail, ce qui entraîne l'absence du pixel de suivi. Cependant, il est aussi possible que moins d'utilisateurs ouvrent leurs e-mails en raison du contenu ou de changements dans la taille de l'audience.

### Comment les audiences des Campaigns sont-elles évaluées ? {#how-are-campaign-audiences-evaluated}

Par défaut, les Campaigns vérifient les filtres d'audience au moment de l'entrée. Pour les Campaigns par événement avec un délai, il existe une option pour réévaluer les critères de Segment au moment de l'envoi afin de s'assurer que les utilisateurs font toujours partie de l'audience cible lorsque le message est envoyé.

### Pourquoi y a-t-il une différence entre le nombre de destinataires uniques et le nombre d'envois pour une Campaign ou un Canvas donné ? {#why-is-there-a-difference-between-the-number-of-unique-recipients-and-the-number-of-sends-for-a-given-campaign-or-canvas}

Une explication possible est que la Campaign ou le Canvas a la rééligibilité activée, ce qui signifie que les utilisateurs qui correspondent au Segment et aux paramètres de distribution peuvent recevoir le message plus d'une fois. Si la rééligibilité n'est pas activée, la différence entre les envois et les destinataires uniques peut s'expliquer par le fait que les utilisateurs possèdent plusieurs appareils, sur différentes plateformes, associés à leurs profils.

Par exemple, si vous avez un Canvas qui comporte à la fois des notifications push iOS et web, un utilisateur donné possédant des appareils mobiles et de bureau peut recevoir plus d'un message.

### Pourquoi le nombre de *destinataires uniques* est-il supérieur au nombre d'utilisateurs ciblés ? {#why-is-_unique-recipients_-higher-than-the-number-of-users-i-targeted}

Le nombre de *destinataires uniques* peut être supérieur à l'audience attendue car Braze comptabilise les destinataires uniques quotidiens pour le reporting. Cela permet à Braze d'attribuer les conversions au sein de la fenêtre de conversion à chaque réception du message par un utilisateur, au lieu de regrouper plusieurs réceptions en un seul comptage global (ce qui fausserait le calcul des conversions).

Par exemple, si un utilisateur reçoit une Campaign le lundi puis à nouveau le vendredi et convertit après chaque envoi, Braze peut signaler cela comme deux réceptions et deux conversions. Si Braze ne comptait qu'un seul « destinataire unique » global pour les deux envois, vous perdriez soit une conversion valide, soit la comptabiliseriez deux fois pour un seul destinataire, ce qui compliquerait la lecture des performances de la Campaign.

Le même principe s'applique aux Campaigns récurrentes et à la rééligibilité : si deux utilisateurs reçoivent chacun un envoi récurrent aujourd'hui et à nouveau demain, le nombre de *destinataires uniques* comptabilise quatre lignes de destinataires quotidiens et non deux profils.

### Pourquoi le nombre de conversions peut-il dépasser le nombre d'utilisateurs uniques pour les Campaigns multicanal ? {#why-can-the-number-of-conversions-exceed-the-number-of-unique-users-for-multichannel-campaigns}

Consultez [Conversions et reporting]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#multichannel-conversions) dans **Créer une Campaign** et [Règles de suivi des conversions]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#conversion-tracking-rules) dans **Événements de conversion**.

### Pourquoi ma Campaign a-t-elle une base d'utilisateurs atteignables plus petite que le Segment que j'utilise pour cette Campaign ? {#why-does-my-campaign-have-a-smaller-reachable-user-base-than-the-segment-that-im-using-for-the-campaign}

Si vous avez configuré un [groupe de contrôle global]({{site.baseurl}}/user_guide/audience/global_control_group), cela empêchera un pourcentage de votre audience atteignable de recevoir des Campaigns. Le nombre d'utilisateurs atteignables pour votre Segment peut donc parfois être supérieur au nombre d'utilisateurs atteignables pour votre Campaign, même si la Campaign utilise ce même Segment.

### Qu'offre la livraison selon le fuseau horaire local ? {#what-does-local-time-zone-delivery-offer}

La livraison selon le fuseau horaire local vous permet de distribuer des Campaigns de communication à un Segment en fonction du fuseau horaire individuel de chaque utilisateur. Sans la livraison selon le fuseau horaire local, les Campaigns seront planifiées en fonction du fuseau horaire de votre entreprise défini dans Braze.

Par exemple, une entreprise basée à Londres envoyant une Campaign à 12 h atteindra les utilisateurs de la côte ouest américaine à 4 h du matin. Si votre application n'est disponible que dans certains pays, cela ne pose peut-être pas de risque. Sinon, nous recommandons fortement d'éviter d'envoyer des notifications push tôt le matin à votre base d'utilisateurs.

### Comment Braze reconnaît-il le fuseau horaire d'un utilisateur ? {#how-does-braze-recognize-a-users-time-zone}

Braze détermine automatiquement le fuseau horaire d'un utilisateur à partir de son appareil. Cela garantit la précision du fuseau horaire et une couverture complète de vos utilisateurs. Les utilisateurs créés via l'API utilisateur ou sans fuseau horaire défini auront le fuseau horaire de votre entreprise comme fuseau horaire par défaut jusqu'à ce qu'ils soient reconnus dans votre application par le SDK.

Vous pouvez vérifier le fuseau horaire de votre entreprise dans les [paramètres de l'entreprise]({{site.baseurl}}/user_guide/administer/global/admin_settings) sur le tableau de bord.

### Quand Braze évalue-t-il les utilisateurs pour la livraison selon le fuseau horaire local ? {#when-does-braze-evaluate-users-for-local-time-zone-delivery}

Braze évalue l'éligibilité des utilisateurs à l'entrée à :

- L'heure des Samoa (UTC+13) le jour planifié
- L'heure locale du jour planifié

Pour qu'un utilisateur soit éligible à l'entrée, il doit satisfaire les deux vérifications. Par exemple, si un Canvas est planifié pour être lancé le 7 août 2021 à 14 h en fuseau horaire local, le ciblage d'un utilisateur situé à New York nécessiterait les vérifications d'éligibilité suivantes :

- New York le 6 août 2021 à 21 h
- New York le 7 août 2021 à 14 h

Pour entrer, un utilisateur doit correspondre à votre audience et à vos filtres aux deux moments d'évaluation. Si l'utilisateur n'est pas éligible lors de la première vérification, Braze n'effectue pas la seconde. Il n'y a pas de durée minimale pendant laquelle un utilisateur doit avoir été dans le Segment avant le lancement. Seule l'éligibilité à chaque vérification compte.

Ce comportement d'évaluation est distinct de [la planification anticipée de la Campaign dans le tableau de bord](#how-do-i-schedule-a-local-time-zone-campaign). Planifier au moins 24 heures à l'avance est une recommandation car cela permet aux messages d'être distribués sur l'ensemble de la fenêtre de 24 heures des fuseaux horaires locaux ; ce n'est pas une exigence selon laquelle chaque utilisateur doit avoir été dans l'audience pendant 24 heures.

#### Exemples {#examples}

Par exemple, si une Campaign est planifiée pour être distribuée à 19 h UTC, nous commençons à mettre en file d'attente les envois de la Campaign dès qu'un fuseau horaire est identifié (comme celui des Samoa). Cela signifie que nous nous préparons à envoyer le message, et non que nous envoyons la Campaign. Si les utilisateurs ne correspondent à aucun filtre lors de la vérification d'éligibilité, ils ne feront pas partie de l'audience cible.

Autre exemple : supposons que vous souhaitiez créer deux Campaigns planifiées pour être envoyées le même jour, l'une le matin et l'autre le soir, et ajouter un filtre pour que les utilisateurs ne puissent recevoir la seconde Campaign que s'ils ont déjà reçu la première. Avec la livraison selon le fuseau horaire local, certains utilisateurs pourraient ne pas recevoir la seconde Campaign. En effet, nous vérifions l'éligibilité lorsque le fuseau horaire de l'utilisateur est identifié, et si l'heure planifiée ne s'est pas encore produite dans son fuseau horaire, il n'a pas reçu la première Campaign et ne sera donc pas éligible pour la seconde.

La chronologie suivante suppose une définition de Segment qui inclut une fenêtre d'appartenance limitée dans le temps. Dans cet exemple, les utilisateurs quittent le Segment 24 heures après y être entrés. Ce comportement de filtre est l'une des raisons pour lesquelles un utilisateur peut passer la première vérification et échouer à la seconde.

![Chronologie montrant un utilisateur entrant dans le Segment avant la première vérification, puis le quittant avant la seconde.]({% image_buster /assets/img/local_time_zone_diagram.png %})

{% details Description de la chronologie %}

1. L'utilisateur A entre dans le Segment à 6 h 59 PST (4 h 59 heure des Samoa).
2. Braze vérifie l'appartenance au Segment à 7 h heure des Samoa pour déterminer quels utilisateurs sont éligibles pour recevoir la Campaign dans les prochaines 24 heures. L'utilisateur A fait partie du Segment à ce moment.
3. Le Segment a une fenêtre de 24 heures, donc l'utilisateur A quitte le Segment 24 heures après y être entré : 6 h 59 PST (4 h 59 heure des Samoa).
4. La Campaign en heure locale s'envoie à 7 h PST, mais l'utilisateur A a déjà quitté le Segment.

{% enddetails %}

### Comment planifier une Campaign en fuseau horaire local ? {#how-do-i-schedule-a-local-time-zone-campaign}

La section précédente décrit quand Braze évalue l'éligibilité pour la livraison selon le fuseau horaire local (les deux vérifications). Cette section décrit quand vous définissez la planification de la Campaign dans le tableau de bord (délai de planification) et quels utilisateurs recevront toujours le message si vous planifiez avec moins de 24 heures d'avance.

Lors de la planification d'une Campaign, choisissez de l'envoyer à une heure désignée puis sélectionnez **Envoyer la Campaign aux utilisateurs dans leur fuseau horaire local**.

Braze recommande fortement que toutes les Campaigns en fuseau horaire local soient planifiées au moins 24 heures à l'avance. Comme une telle Campaign doit être envoyée sur une journée entière, la planifier 24 heures à l'avance garantit que votre message atteindra l'ensemble de votre Segment. Cependant, vous pouvez planifier ces Campaigns moins de 24 heures à l'avance si nécessaire. Gardez à l'esprit que Braze n'enverra pas de messages aux utilisateurs ayant dépassé l'heure d'envoi de plus d'une heure.

Par exemple, s'il est 13 h et que vous planifiez une Campaign en fuseau horaire local pour 15 h, la Campaign sera immédiatement envoyée à tous les utilisateurs dont l'heure locale est entre 15 h et 16 h, mais pas aux utilisateurs dont l'heure locale est 17 h. De plus, l'heure d'envoi que vous choisissez pour votre Campaign ne doit pas encore être passée dans le fuseau horaire de votre entreprise.

La modification d'une Campaign en fuseau horaire local planifiée moins de 24 heures à l'avance ne modifiera pas la planification du message. Si vous décidez de modifier une Campaign en fuseau horaire local pour un envoi à une heure ultérieure (par exemple, 19 h au lieu de 18 h), les utilisateurs qui faisaient partie du Segment ciblé lorsque l'heure d'envoi initiale a été choisie recevront toujours le message à l'heure initiale (18 h). Si vous modifiez un fuseau horaire local pour un envoi à une heure antérieure (par exemple, 16 h au lieu de 17 h), la Campaign sera quand même envoyée à tous les membres du Segment à l'heure initiale (17 h).

{% alert note %}
Pour les composants Canvas, les utilisateurs n'ont pas besoin d'être dans le composant pendant 24 heures pour recevoir le composant suivant du parcours utilisateur lors de la livraison selon le fuseau horaire local.
{% endalert %}

Si vous avez autorisé les utilisateurs à redevenir éligibles pour la Campaign, ils la recevront à nouveau à l'heure initiale (17 h). Cependant, pour toutes les occurrences suivantes de votre Campaign, vos messages seront uniquement envoyés à l'heure mise à jour.

### Quand les modifications apportées aux Campaigns en fuseau horaire local prennent-elles effet ? {#when-do-changes-to-local-time-zone-campaigns-take-effect}

Les Segments cibles pour les Campaigns en fuseau horaire local doivent inclure une fenêtre d'au moins 48 heures pour tout filtre temporel afin de garantir la distribution à l'ensemble du Segment. Par exemple, considérons un Segment ciblant les utilisateurs à leur deuxième jour avec les filtres suivants :

- Première utilisation de l'application il y a plus d'un jour
- Première utilisation de l'application il y a moins de deux jours

La livraison selon le fuseau horaire local peut manquer des utilisateurs dans ce Segment en fonction de l'heure de distribution et du fuseau horaire local des utilisateurs. En effet, un utilisateur peut quitter le Segment avant que son fuseau horaire ne déclenche la distribution.

### Quelles modifications puis-je apporter aux Campaigns planifiées avant le lancement ? {#what-changes-can-i-make-to-scheduled-campaigns-ahead-of-launch}

Lorsque la Campaign est planifiée, vous devez effectuer les modifications de tout ce qui n'est pas la composition du message avant que nous mettions les messages en file d'attente pour l'envoi. Comme pour toutes les Campaigns, vous ne pouvez pas modifier les événements de conversion après le lancement.

### J'ai mis à jour ma Campaign planifiée. Pourquoi ne s'est-elle pas lancée ? {#i-updated-my-scheduled-campaign-why-didnt-it-launch}

Cela peut se produire lorsqu'une Campaign est planifiée pour être lancée exactement au moment où elle a été mise à jour. Par exemple, s'il est actuellement 15 h 10 et que vous modifiez la Campaign pour un lancement à 15 h 10 puis sélectionnez **Mettre à jour la Campaign**, il est maintenant passé 15 h 10, ce qui signifie que l'heure planifiée pour le lancement est dépassée. Au lieu de planifier la Campaign pour la même heure, sélectionnez **Envoyer dès le lancement de la Campaign**.

### Quelle est la « zone de sécurité » avant la mise en file d'attente des messages d'une Campaign planifiée ? {#what-is-the-safe-zone-before-messages-on-a-scheduled-campaign-are-enqueued}

Nous recommandons d'apporter des modifications aux messages dans les délais suivants :

- **Campaigns planifiées ponctuelles :** Modifiez jusqu'à l'heure d'envoi planifiée.
- **Campaigns planifiées récurrentes :** Modifiez jusqu'à l'heure d'envoi planifiée.
- **Campaigns en heure locale :** Modifiez jusqu'à 24 heures avant l'heure d'envoi planifiée.
- **Campaigns à heure d'envoi optimale :** Modifiez jusqu'à 24 heures avant le jour où la Campaign est planifiée.

Si vous apportez des modifications en dehors de ces recommandations, les mises à jour pourraient ne pas être reflétées dans le message envoyé. Par exemple, si vous modifiez l'heure d'envoi trois heures avant qu'une Campaign soit planifiée pour 12 h en heure locale, les événements suivants peuvent se produire :

- Braze n'envoie pas de messages aux utilisateurs ayant dépassé l'heure d'envoi de plus d'une heure.
- Les messages déjà mis en file d'attente peuvent toujours être envoyés à l'heure initialement mise en file d'attente, plutôt qu'à l'heure ajustée.

Si vous devez apporter des modifications, nous vous recommandons d'arrêter la Campaign en cours (cela annule tous les messages mis en file d'attente). Vous pouvez ensuite dupliquer la Campaign, effectuer les modifications nécessaires et lancer la nouvelle Campaign. Vous devrez peut-être exclure de cette Campaign les utilisateurs qui ont déjà reçu la première Campaign. Assurez-vous de réajuster les horaires de planification de la Campaign pour tenir compte de l'envoi par fuseau horaire.

### Pourquoi aucun utilisateur n'est-il entré dans ma Campaign quotidienne planifiée le jour du changement d'heure ? {#why-did-no-users-enter-my-daily-scheduled-campaign-on-daylight-saving-time-day}

Les jours de transition du changement d'heure (heure d'été/hiver), les Campaigns quotidiennes planifiées peuvent s'exécuter jusqu'à une heure plus tôt ou plus tard que d'habitude, selon que les horloges avancent ou reculent. Si votre Segment repose sur des attributs personnalisés ou des événements avec des horodatages situés dans l'heure précédant l'heure d'envoi planifiée, ces utilisateurs peuvent ne pas encore être qualifiés lorsque la Campaign évalue l'éligibilité le jour du changement d'heure.

Par exemple, supposons que les utilisateurs reçoivent habituellement une mise à jour d'attribut personnalisé à 15 h UTC, et que votre Campaign s'exécute quotidiennement à 10 h 30 à New York (heure de l'Est). Lorsque New York est en heure standard (UTC-5), 10 h 30 ET correspond à 15 h 30 UTC, donc la Campaign s'exécute après l'enregistrement de l'attribut. Lorsque New York passe à l'heure d'été (UTC-4), 10 h 30 ET correspond à 14 h 30 UTC, donc le jour du passage à l'heure d'été, la Campaign peut s'exécuter avant la mise à jour de l'attribut à 15 h UTC. L'attribut qualifiant n'existant pas encore, ces utilisateurs sont filtrés. Si la rééligibilité est désactivée, les utilisateurs entrés les jours précédents ne peuvent pas réintégrer la Campaign, ce qui entraîne zéro entrée pour cette journée.

Pour éviter cela, assurez-vous que les mises à jour de vos attributs personnalisés ou événements se produisent plus d'une heure avant l'heure d'envoi planifiée de la Campaign.

### Pourquoi le nombre d'utilisateurs entrant dans une Campaign ne correspond-il pas au nombre attendu ? {#why-does-the-number-of-users-entering-a-campaign-not-match-the-expected-number}

Le nombre d'utilisateurs entrant dans une Campaign peut différer du nombre attendu en raison de la manière dont les audiences et les déclencheurs sont évalués. Dans Braze, une audience est évaluée avant le déclencheur (sauf lors de l'utilisation d'un déclencheur de [modification d'attribut]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Les utilisateurs sont donc exclus de la Campaign s'ils ne font pas initialement partie de l'audience sélectionnée avant l'évaluation des actions de déclenchement.

{% alert tip %}
Pour toute assistance supplémentaire concernant la résolution des problèmes de Campaign, assurez-vous de contacter le support Braze dans les 30 jours suivant la survenue de votre problème, car nous ne disposons que des 30 derniers jours de journaux de diagnostic.
{% endalert %}

### Pourquoi les utilisateurs ont-ils reçu ma Campaign deux fois après l'avoir modifiée ? {#why-did-users-receive-my-campaign-twice-after-i-edited-it}

Si vous modifiez une Campaign en cours sans l'arrêter au préalable, les utilisateurs peuvent recevoir le message deux fois. Cela se produit car la modification d'une Campaign en cours remet les utilisateurs en file d'attente pour la version mise à jour tandis que la file d'attente d'origine est toujours en cours de traitement. Les utilisateurs qui n'ont pas encore reçu le message d'origine peuvent se retrouver dans les deux files d'attente. Pour éviter cela, [arrêtez toujours la Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/change_your_campaign_after_launch#stopping-your-campaign) avant d'apporter des modifications.

### Quelle est la différence entre les options Exporter les données utilisateur en CSV et Exporter les adresses e-mail en CSV sur la page d'analyse de ma Campaign ? {#what-is-the-difference-between-the-csv-export-user-data-and-csv-export-email-address-options-on-my-campaign-analytics-page}

Sélectionner l'option **Exporter les adresses e-mail en CSV** télécharge uniquement les données des utilisateurs disposant d'adresses e-mail. Par exemple, si vous avez un Segment de 100 000 utilisateurs, mais que seuls 50 000 d'entre eux ont des adresses e-mail, et que vous cliquez sur **Exporter les adresses e-mail en CSV**, l'exportation ne contient que 50 000 lignes de données. En comparaison, sélectionner **Exporter les données utilisateur en CSV** exporte toutes les données utilisateur.

### Puis-je rechercher une Campaign par son identifiant API ? {#can-i-search-for-a-campaign-by-its-api-identifier}

Oui, utilisez le filtre `api_id:YOUR_API_ID` sur la page **Campaigns** pour rechercher une Campaign par son identifiant API. Consultez la section [Rechercher des Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/search_campaigns) pour en savoir plus.

### Pourquoi les espaces apparaissent-ils différemment entre les champs de saisie et le texte affiché ? {#why-does-whitespace-appear-differently-in-input-fields-versus-displayed-text}

La gestion des espaces diffère entre les champs de saisie et les composants de texte affiché en raison du style CSS. Dans les composants de texte avec le CSS par défaut `white-space: normal`, les espaces consécutifs multiples sont réduits à un seul espace lors de l'affichage. Il s'agit du comportement HTML standard pour le texte rendu.

Les champs de saisie conservent les espaces multiples exactement tels que vous les entrez, car vous devez voir et modifier l'espacement exact pour une saisie de données précise. Cela signifie qu'un texte contenant des espaces multiples peut apparaître différemment lorsqu'il est affiché dans un champ de saisie (où tous les espaces sont conservés) par rapport à son affichage dans d'autres parties du tableau de bord (où le CSS peut réduire les espaces multiples).

Par exemple, si vous saisissez un nom de Campaign ou un paramètre UTM avec des espaces multiples dans un champ de saisie, vous verrez tous les espaces conservés. Cependant, lorsque ce même texte apparaît dans les résultats de recherche, les listes de Campaigns ou d'autres composants textuels, les espaces multiples peuvent apparaître comme un seul espace en raison de la gestion CSS des espaces.

### Quelle est la différence entre les Campaigns API et les Campaigns déclenchées par API ? {#what-is-the-difference-between-api-campaigns-and-api-triggered-campaigns}

Les Campaigns déclenchées par API vous permettent de gérer le contenu de la Campaign, les tests multivariés et les règles de rééligibilité dans le tableau de bord de Braze tout en déclenchant la distribution de ce contenu depuis vos propres serveurs et systèmes. Ces messages peuvent également inclure des données supplémentaires à intégrer dans les messages en temps réel.

Les Campaigns API sont utilisées pour suivre les messages envoyés via l'API. Contrairement à la plupart des Campaigns, vous ne spécifiez pas le message, les destinataires ou la planification, mais transmettez plutôt les identifiants dans vos appels API.

### Comment puis-je confirmer si mes utilisateurs ont reçu une Campaign déclenchée par API ? {#how-can-i-confirm-if-my-users-received-an-api-triggered-campaign}

Vous pouvez [créer un Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) en utilisant le filtre **A reçu la Campaign**, puis sélectionner la Campaign déclenchée par API spécifique que vous souhaitez vérifier. Après avoir enregistré le Segment, utilisez l'[endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) pour exporter les utilisateurs de ce Segment.

### Puis-je supprimer une Campaign ? {#can-i-delete-a-campaign}

Non, mais vous pouvez [archiver une Campaign]({{site.baseurl}}/user_guide/messaging/governance/archiving).

### Quelle est la différence entre les Campaigns par événement et les Campaigns déclenchées par API ? {#what-is-the-difference-between-action-based-and-api-triggered-campaigns}

<style>
table th:nth-child(1) {
    width: 50%;
}
table th:nth-child(3) {
    width: 50%;
}
</style>

#### Par événement {#action-based}

Les Campaigns à livraison par événement sont très efficaces pour les messages transactionnels ou liés à des accomplissements et vous permettent de les déclencher après qu'un utilisateur a effectué un certain événement.

| Avantages | Inconvénients |
| ---- | ---- |
| • Visibilité des payloads JSON entrants dans la plateforme (si l'événement est déclenché par un utilisateur test) via le **Journal d'activité des messages**<br><br>• Les éléments de personnalisation sont inclus dans les propriétés d'événement personnalisé<br><br>• L'événement personnalisé peut être utilisé pour créer des Segments d'utilisateurs éligibles pour le message | • Consomme des points de donnée |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Par événement" }

#### Déclenchées par API {#api-triggered}

Les Campaigns déclenchées par API et par serveur sont idéales pour gérer des transactions plus avancées, vous permettant de déclencher la distribution du contenu de la Campaign depuis vos propres serveurs et systèmes. La requête API pour déclencher le message peut également inclure des données supplémentaires à intégrer dans le message en temps réel.

| Avantages | Points à considérer |
| ---- | ---- |
| • Ne consomme pas de points de donnée<br><br>• Les éléments de personnalisation sont inclus dans les propriétés du payload JSON | • Ne permet pas de créer un Segment d'utilisateurs éligibles pour le message dans les propriétés du payload JSON<br><br>• Impossible de voir les payloads JSON entrants avec le **Journal d'activité des messages** |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Déclenchées par API" }

### Que dois-je inclure lors de la soumission d'un ticket de support pour une erreur « Délai de requête dépassé » ? {#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error}

Si vous rencontrez une erreur « Délai de requête dépassé » lors de la création ou de la modification d'une Campaign ou d'un Canvas et que vous devez contacter le [support Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support), incluez les informations suivantes pour accélérer la résolution :

{% multi_lang_include messaging/support_ticket_request_timed_out_details.md context='campaign' %}

### Pourquoi mes analyses d'envoi ne correspondent-elles pas à la limite maximale de destinataires que j'ai définie ? {#why-dont-my-send-analytics-match-the-maximum-recipient-limit-i-set}

Si vous ajoutez ou modifiez une limite maximale de destinataires sur une Campaign active, la limite peut ne pas être reflétée dans vos analyses d'envoi pour les raisons suivantes :

- **Limite ajoutée après le lancement :** Si la limite maximale de destinataires n'est pas définie au lancement de la Campaign, les messages déjà mis en file d'attente avant l'application de la limite sont toujours envoyés. La limite ne prend effet que pour les envois mis en file d'attente après l'enregistrement de la modification.
- **Interaction avec la limitation du débit :** Si une Campaign est également soumise à une limitation du débit, les messages peuvent être distribués sur une fenêtre temporelle plus longue. La limite maximale de destinataires est évaluée lorsque les messages sont mis en file d'attente, et non lorsqu'ils sont distribués. Si la limite est modifiée alors que des messages sont déjà en file d'attente, la limite initiale s'applique à ces messages.
- **Campaigns récurrentes :** Pour les Campaigns récurrentes, chaque envoi planifié évalue la limite maximale de destinataires indépendamment. La modification de la limite entre les envois n'ajuste pas rétroactivement les comptages d'envois précédents.

Pour éviter les désalignements, définissez la limite maximale de destinataires avant le lancement de la Campaign et évitez de la modifier pendant que des envois sont en cours.

### Pourquoi le nombre d'envois est-il inférieur à la taille estimée de l'audience ? {#why-are-sends-lower-than-the-estimated-audience-size}

Plusieurs facteurs peuvent faire en sorte que le nombre d'envois soit inférieur à la taille estimée de l'audience :

- **Livraison par événement :** Les utilisateurs ne génèrent des envois qu'après avoir effectué l'action de déclenchement, de sorte que les envois s'accumulent au fil du temps et peuvent être en retard par rapport à l'estimation initiale affichée lors de la création de la Campaign.
- **Modifications de l'audience après le lancement :** La modification des filtres d'entrée ou de ciblage après le lancement peut désynchroniser l'instantané de l'**audience estimée** par rapport aux utilisateurs qui restent qualifiés lors des envois ultérieurs (par exemple, lorsque les utilisateurs ne sont pas éligibles à la réentrée).
- **Étape Parcours d'audience :** Pour Canvas, une étape [Parcours d'audience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) n'envoie de messages qu'aux utilisateurs correspondant à la branche prioritaire la plus élevée pour laquelle ils sont qualifiés, ce qui peut réduire les envois par rapport à un comptage de Segment simple.
- **Groupes de contrôle :** Si un [groupe de contrôle global]({{site.baseurl}}/user_guide/audience/global_control_group) ou un groupe de contrôle au niveau de la Campaign est utilisé, une partie de l'audience est retenue de la distribution.
- **Timing de distribution et fenêtres :** Pour les Campaigns en fuseau horaire local ou planifiées, les utilisateurs doivent être qualifiés à la fois à l'entrée et au moment de l'envoi ; les utilisateurs de certains fuseaux horaires peuvent se trouver en dehors de la fenêtre de distribution.
- **Déduplication d'e-mails :** Votre Campaign ou Canvas cible plusieurs utilisateurs avec des adresses e-mail identiques, de sorte qu'un utilisateur aléatoire avec cette adresse e-mail est choisi au moment de l'envoi. Le message n'est envoyé qu'une seule fois et est dédupliqué afin de ne pas être envoyé plusieurs fois à la même adresse e-mail, mais la taille estimée de votre audience inclut tous les utilisateurs.
- **Filtres de livrabilité e-mail :** Pour les Campaigns par e-mail, Braze exclut les utilisateurs qui ont subi un hard bounce, se sont désabonnés des e-mails, ont été marqués comme spam, n'ont pas d'adresse e-mail dans leur profil ou ne sont pas abonnés à un groupe d'abonnement requis. Ces vérifications sont effectuées au moment de l'envoi, de sorte qu'un utilisateur présent dans votre Segment peut être exclu du nombre réel d'envois.
- **Timing d'importation CSV :** Lorsque l'appartenance au Segment est maintenue par [importation CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import), les adresses e-mail ajoutées après l'envoi d'une Campaign planifiée ne sont pas atteintes par cet envoi. Comme Braze ne conserve pas d'instantané de l'appartenance au Segment au moment de l'envoi, la taille actuelle du Segment peut dépasser le nombre d'utilisateurs effectivement contactés.
- **Limite de fréquence globale :** Les limites au niveau du workspace peuvent empêcher les utilisateurs éligibles de recevoir un autre message dans la même fenêtre, ce qui réduit les envois réalisés.
- **Utilisateurs nouvellement importés :** Les profils qui viennent de devenir éligibles peuvent ne pas recevoir le message avant la prochaine évaluation ou passe d'envoi, de sorte que les comptages rattrapent lors d'une exécution ultérieure.
- **Accessibilité push :** Pour les Campaigns push, confirmez que l'audience est activée pour le push pour l'application correcte. Si vous ne filtrez pas les utilisateurs activés pour le push, l'audience estimée peut inclure des profils qui ne peuvent pas recevoir de push. Vérifiez les **utilisateurs atteignables** dans l'étape **Utilisateurs cibles** pour une estimation opérationnelle plus précise.
- **Limitation du débit :** Une [limite de débit de distribution]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) plafonne le nombre de messages que Braze envoie par minute lors d'un envoi unique. Braze répartit la distribution sur une fenêtre plus longue, de sorte que certains envois peuvent être différés, pas encore reflétés dans le comptage, ou non terminés si la limite est faible par rapport à l'audience éligible.
- **Fenêtres de rééligibilité :** Les utilisateurs qui ne sont pas encore rééligibles ne recevront pas le message à nouveau pendant la période de refroidissement, de sorte que les envois sont inférieurs à la taille estimée de l'audience pour cette période.
- **Fenêtre de reporting :** La plage temporelle d'analyse peut ne pas inclure chaque envoi.
- **Réévaluation du Segment :** Pour les Campaigns par événement ou planifiées qui réévaluent au moment de l'envoi, les utilisateurs qui faisaient partie du Segment lorsque la Campaign a été mise en file d'attente peuvent ne plus être qualifiés lorsque le message est effectivement envoyé.
- **Limites d'envoi :** Un nombre maximum d'utilisateurs (ou une limite similaire) dans **Audiences cibles** arrête la distribution lorsque la limite est atteinte.
- **Filtres stricts d'appareil ou de navigateur :** Les filtres qui ne correspondent qu'aux versions les plus récentes de l'application ou du navigateur réduisent l'ensemble atteignable au moment de l'envoi par rapport à un aperçu de Segment large.

### Où se trouvent les questions fréquemment posées sur la limite de fréquence globale ? {#where-are-frequently-asked-questions-about-global-frequency-capping}

Pour les questions sur les jours calendaires, les push silencieux, les webhooks, le comportement Canvas et les sujets connexes, consultez les [questions fréquemment posées]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/faq) sur la [limitation du débit et la limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).

### Pourquoi ma Campaign connaît-elle des taux d'envoi plus faibles ? {#why-is-my-campaign-experiencing-lower-send-rates}

Si vous constatez que vos Campaigns quotidiennes planifiées envoient à moins d'utilisateurs au fil du temps, vérifiez les points suivants :

- **Vérifiez si la rééligibilité est activée :** Sans rééligibilité, Braze n'envoie le message à chaque utilisateur qu'une seule fois. Pour les Campaigns quotidiennes planifiées, seuls les utilisateurs qui correspondent à l'audience et n'ont pas encore reçu le message sont éligibles pour chaque envoi. À mesure que davantage d'utilisateurs reçoivent le message, chaque envoi ultérieur a moins d'utilisateurs éligibles, donc le volume d'envois diminue.
- **Vérifiez si l'audience a un membership fixe :** Les audiences construites à partir d'une liste d'utilisateurs fixe (comme une [importation CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) utilisée comme filtre de Segment) ne gagnent pas automatiquement de nouveaux membres. Sans nouveaux entrants, le volume d'envois ne peut pas rebondir à mesure que les utilisateurs sont contactés.

Pour les [limites de débit de distribution]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) et les autres facteurs qui réduisent les envois pour une occurrence unique, consultez [Pourquoi le nombre d'envois est-il inférieur à la taille estimée de l'audience ?](#why-are-sends-lower-than-the-estimated-audience-size).

### Pourquoi le nombre de destinataires uniques peut-il dépasser le nombre d'envois pour les e-mails et les SMS ? {#why-can-unique-recipients-exceed-sends-for-email-and-sms}

Pour les e-mails et les SMS, Braze incrémente les **destinataires uniques** avant la tentative d'envoi via le fournisseur de services d'e-mail (fournisseur de services d'e-mailing) et incrémente les **envois** après une réponse réussie de l'fournisseur de services d'e-mailing. Les erreurs permanentes (telles que les adresses e-mail invalides) ou les adresses en double entraînent un nombre de destinataires uniques supérieur au nombre d'envois.

### Pourquoi le champ **Dernier envoi** ne correspond-il pas à l'heure d'envoi planifiée ? {#why-doesnt-last-sent-match-my-scheduled-send-time}

Pour une Campaign avec un seul envoi planifié, **Dernier envoi** correspond à l'heure de lancement. Pour les Campaigns récurrentes avec **Envoyer en fuseau horaire local** activé, **Dernier envoi** peut apparaître plus tôt que l'heure planifiée car les envois aux utilisateurs dans des fuseaux horaires antérieurs (par exemple, GMT par rapport à PST) se terminent avant l'heure de planification de votre workspace.

### Pourquoi une Campaign historique arrêtée n'affiche-t-elle plus d'indicateurs sur la page **Analytics** ? {#why-does-a-stopped-historical-campaign-no-longer-show-metrics-on-the-analytics-page}

L'onglet **Analytics** affiche par défaut les 90 derniers jours. Si la Campaign a été envoyée pour la dernière fois en dehors de cette fenêtre, les indicateurs peuvent apparaître comme nuls jusqu'à ce que vous ajustiez la plage de dates sur la page **Analytics** pour inclure la période d'envoi de la Campaign. Pour plus d'informations, consultez [Analyse des Campaigns]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics).

**Restaurer les données d'interaction** ne restaure pas les analyses de Campaign. Cela s'applique uniquement aux filtres de reciblage et à l'historique des interactions utilisateur. Pour plus d'informations, consultez [Données d'interaction de messaging]({{site.baseurl}}/messaging_interaction_data).