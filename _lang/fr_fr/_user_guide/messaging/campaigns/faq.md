---
nav_title: FAQ
article_title: FAQ sur les campagnes
page_order: 10
page_type: FAQ
description: "Cette page répond aux questions fréquemment posées sur les campagnes."
tool: Campaigns

---

# Questions fréquemment posées {#frequently-asked-questions}

> Cet article répond à certaines questions fréquemment posées sur les campagnes.

## Comment créer une campagne multicanale ? {#how-do-i-create-a-multichannel-campaign}

Consultez [Campaigns multicanales]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#create-a-multichannel-campaign) dans **Créer une Campaign** pour les étapes de configuration et les canaux pris en charge.

### Puis-je ajouter un groupe de contrôle à ma Campaign multicanale ? {#can-i-add-a-control-group-to-my-multichannel-campaign}

Consultez [Groupes de contrôle]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#multichannel-control-groups) dans **Créer une Campaign**. Pour les tests cross-canal, utilisez [Canvas]({{site.baseurl}}/user_guide/messaging/canvas).

### Quels sont les moyens de commencer à tester et optimiser les Campaigns ? {#what-are-some-ways-i-can-start-testing-and-optimizing-campaigns}

Les Campaigns multivariées et l'exécution de Canvas avec plusieurs variantes constituent un excellent point de départ ! Par exemple, vous pouvez lancer une [Campaign multivariée]({{site.baseurl}}/user_guide/messaging/ab_testing) pour tester un message avec différentes copies ou lignes d'objet. Les Canvas avec plusieurs variantes peuvent aider à tester des workflows entiers.

### Pourquoi le taux d'ouverture de ma Campaign a-t-il diminué ? {#why-did-the-open-rate-for-my-campaign-decrease}

Un faible taux d'ouverture n'est pas toujours lié à un problème technique. Il peut y avoir des problèmes de troncature d'e-mail, ce qui entraîne l'absence du pixel de suivi. Cependant, il est également possible que moins d'utilisateurs ouvrent leurs e-mails en raison du contenu ou de changements dans la taille de l'audience.

### Comment les audiences des Campaigns sont-elles évaluées ? {#how-are-campaign-audiences-evaluated}

Par défaut, les Campaigns vérifient les filtres d'audience au moment de l'entrée. Pour les Campaigns basées sur des actions avec un délai, il existe une option pour réévaluer les critères de Segment au moment de l'envoi afin de s'assurer que les utilisateurs font toujours partie de l'audience cible lorsque le message est envoyé.

### Pourquoi y a-t-il une différence entre le nombre de destinataires uniques et le nombre d'envois pour une Campaign ou un Canvas donné ? {#why-is-there-a-difference-between-the-number-of-unique-recipients-and-the-number-of-sends-for-a-given-campaign-or-canvas}

Une explication possible est que la Campaign ou le Canvas a la rééligibilité activée, ce qui signifie que les utilisateurs qui correspondent au Segment et aux paramètres de distribution pourront recevoir le message plus d'une fois. Si la rééligibilité n'est pas activée, l'explication probable de la différence entre les envois et les destinataires uniques peut être due au fait que les utilisateurs possèdent plusieurs appareils, sur différentes plateformes, associés à leurs profils.

Par exemple, si vous avez un Canvas qui comporte à la fois des notifications push iOS et web, un utilisateur donné possédant à la fois un appareil mobile et un ordinateur de bureau pourrait recevoir plus d'un message.

### Pourquoi les *destinataires uniques* sont-ils plus élevés que le nombre d'utilisateurs ciblés ? {#why-is-_unique-recipients_-higher-than-the-number-of-users-i-targeted}

Les *destinataires uniques* peuvent être plus élevés que l'audience attendue car Braze suit les destinataires uniques quotidiens à des fins de reporting. Cela permet à Braze d'attribuer les conversions dans la fenêtre de conversion chaque fois qu'un utilisateur reçoit le message, au lieu de regrouper plusieurs réceptions en un seul comptage à vie (ce qui fausserait le calcul des conversions).

Par exemple, si un utilisateur reçoit une Campaign le lundi et à nouveau le vendredi et convertit après chaque envoi, Braze peut rapporter cela comme deux réceptions et deux conversions. Si Braze ne comptait qu'un seul « unique » à vie pour les deux envois, vous perdriez soit une conversion valide, soit la compteriez en double pour un seul destinataire, ce qui rendrait la performance de la Campaign plus difficile à interpréter.

Le même schéma s'applique aux Campaigns récurrentes et à la rééligibilité : si deux utilisateurs reçoivent chacun un envoi récurrent aujourd'hui et à nouveau demain, les *destinataires uniques* comptent quatre lignes de destinataires quotidiens, et non deux profils.

### Pourquoi le nombre de conversions peut-il dépasser le nombre d'utilisateurs uniques pour les Campaigns multicanales ? {#why-can-the-number-of-conversions-exceed-the-number-of-unique-users-for-multichannel-campaigns}

Consultez [Conversions et reporting]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#multichannel-conversions) dans **Créer une Campaign** et [Règles de suivi des conversions]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#conversion-tracking-rules) dans **Événements de conversion**.

### Pourquoi ma Campaign a-t-elle une base d'utilisateurs atteignables plus petite que le Segment que j'utilise pour la Campaign ? {#why-does-my-campaign-have-a-smaller-reachable-user-base-than-the-segment-that-im-using-for-the-campaign}

Si vous avez configuré un [groupe de contrôle global]({{site.baseurl}}/user_guide/audience/global_control_group), cela empêchera un pourcentage de votre audience atteignable de recevoir des Campaigns. Cela signifie que le nombre d'utilisateurs atteignables pour votre Segment peut parfois être supérieur au nombre d'utilisateurs atteignables pour votre Campaign, même si la Campaign utilise ce même Segment.

### Qu'offre la distribution en fuseau horaire local ? {#what-does-local-time-zone-delivery-offer}

La distribution en fuseau horaire local vous permet de distribuer des Campaigns de communication à un Segment en fonction du fuseau horaire individuel de chaque utilisateur. Sans la distribution en fuseau horaire local, les Campaigns seront planifiées en fonction des paramètres de fuseau horaire de votre entreprise dans Braze.

Par exemple, une entreprise basée à Londres envoyant une Campaign à 12 h atteindra les utilisateurs de la côte ouest des États-Unis à 4 h du matin. Si votre application n'est disponible que dans certains pays, cela peut ne pas poser de problème. Sinon, nous recommandons fortement d'éviter d'envoyer des notifications push tôt le matin à votre base d'utilisateurs.

### Comment Braze reconnaît-il le fuseau horaire d'un utilisateur ? {#how-does-braze-recognize-a-users-time-zone}

Braze détermine automatiquement le fuseau horaire d'un utilisateur à partir de son appareil. Cela garantit la précision du fuseau horaire et une couverture complète de vos utilisateurs. Les utilisateurs créés via l'API utilisateur ou autrement sans fuseau horaire auront le fuseau horaire de votre entreprise comme fuseau horaire par défaut jusqu'à ce qu'ils soient reconnus dans votre application par le SDK.

Vous pouvez vérifier le fuseau horaire de votre entreprise dans les [paramètres de votre entreprise]({{site.baseurl}}/user_guide/administer/global/admin_settings) sur le tableau de bord.

### Quand Braze évalue-t-il les utilisateurs pour la distribution en fuseau horaire local ? {#when-does-braze-evaluate-users-for-local-time-zone-delivery}

Braze évalue l'éligibilité des utilisateurs à l'entrée à :

- L'heure des Samoa (UTC+13) le jour planifié
- L'heure locale du jour planifié

Pour qu'un utilisateur soit éligible à l'entrée, il doit être éligible aux deux vérifications. Par exemple, si un Canvas est planifié pour être lancé le 7 août 2021 à 14 h en fuseau horaire local, alors le ciblage d'un utilisateur situé à New York nécessiterait les vérifications d'éligibilité suivantes :

- New York le 6 août 2021 à 21 h
- New York le 7 août 2021 à 14 h

Pour entrer, un utilisateur doit correspondre à votre audience et à vos filtres aux deux moments d'évaluation. Si l'utilisateur n'est pas éligible lors de la première vérification, Braze n'effectue pas la seconde. Il n'y a pas de durée minimale pendant laquelle un utilisateur doit avoir été dans le Segment avant le lancement. Seule l'éligibilité à chaque vérification compte.

Ce comportement d'évaluation est distinct de [la durée d'avance avec laquelle vous planifiez la Campaign dans le tableau de bord](#how-do-i-schedule-a-local-time-zone-campaign). Planifier au moins 24 heures à l'avance est une recommandation car cela aide les messages à être distribués sur l'ensemble de la fenêtre de 24 heures en fuseau horaire local, et non une exigence que chaque utilisateur ait été dans l'audience pendant 24 heures.

#### Exemples {#examples}

Par exemple, si une Campaign est planifiée pour être distribuée à 19 h UTC, nous commençons à mettre en file d'attente les envois de la Campaign dès qu'un fuseau horaire est identifié (comme les Samoa). Cela signifie que nous nous préparons à envoyer le message, pas que nous envoyons la Campaign. Si les utilisateurs ne correspondent à aucun filtre lorsque nous vérifions l'éligibilité, ils ne feront pas partie de l'audience cible.

Autre exemple : supposons que vous souhaitiez créer deux Campaigns planifiées pour être envoyées le même jour — une le matin et une le soir — et ajouter un filtre pour que les utilisateurs ne puissent recevoir la seconde Campaign que s'ils ont déjà reçu la première. Avec la distribution en fuseau horaire local, certains utilisateurs pourraient ne pas recevoir la seconde Campaign. En effet, nous vérifions l'éligibilité lorsque le fuseau horaire de l'utilisateur est identifié, donc si l'heure planifiée n'est pas encore arrivée dans leur fuseau horaire, ils n'ont pas reçu la première Campaign, ce qui signifie qu'ils ne seront pas éligibles pour la seconde.

La chronologie suivante suppose une définition de Segment qui inclut une fenêtre d'appartenance limitée dans le temps. Dans cet exemple, les utilisateurs quittent le Segment 24 heures après y avoir été ajoutés. Ce comportement de filtre est l'une des raisons pour lesquelles un utilisateur peut réussir la première vérification et échouer à la seconde.

![Chronologie d'un utilisateur entrant dans le Segment avant la première vérification, puis le quittant avant la seconde.]({% image_buster /assets/img/local_time_zone_diagram.png %})

{% details Description de la chronologie %}

1. L'utilisateur A entre dans le Segment à 6 h 59 PST (4 h 59 heure des Samoa).
2. Braze vérifie l'appartenance au Segment à 7 h heure des Samoa pour déterminer quels utilisateurs sont éligibles pour recevoir la Campaign dans les 24 prochaines heures. L'utilisateur A est dans le Segment à ce moment.
3. Le Segment a une fenêtre de 24 heures, donc l'utilisateur A quitte le Segment 24 heures après y être entré : 6 h 59 PST (4 h 59 heure des Samoa).
4. La Campaign en heure locale s'envoie à 7 h PST, mais l'utilisateur A a déjà quitté le Segment.

{% enddetails %}

### Comment planifier une Campaign en fuseau horaire local ? {#how-do-i-schedule-a-local-time-zone-campaign}

La section précédente décrit quand Braze évalue l'éligibilité pour la distribution en fuseau horaire local (les deux vérifications). Cette section décrit quand vous définissez la planification de la Campaign dans le tableau de bord (délai de planification) et quels utilisateurs reçoivent encore le message si vous planifiez avec moins de 24 heures de préavis.

Lors de la planification d'une Campaign, choisissez de l'envoyer à une heure désignée, puis sélectionnez **Envoyer la Campaign aux utilisateurs dans leur fuseau horaire local**.

Braze recommande fortement que toutes les Campaigns en fuseau horaire local soient planifiées 24 heures à l'avance. Comme une telle Campaign doit être envoyée sur une journée entière, la planifier 24 heures à l'avance garantit que votre message atteindra l'ensemble de votre Segment. Cependant, vous pouvez planifier ces Campaigns moins de 24 heures à l'avance si nécessaire. Gardez à l'esprit que Braze n'enverra pas de messages aux utilisateurs qui ont manqué l'heure d'envoi de plus d'une heure.

Par exemple, s'il est 13 h et que vous planifiez une Campaign en fuseau horaire local pour 15 h, la Campaign sera immédiatement envoyée à tous les utilisateurs dont l'heure locale est entre 15 h et 16 h, mais pas aux utilisateurs dont l'heure locale est 17 h. De plus, l'heure d'envoi que vous choisissez pour votre Campaign ne doit pas encore être passée dans le fuseau horaire de votre entreprise.

La modification d'une Campaign en fuseau horaire local planifiée moins de 24 heures à l'avance ne modifiera pas la planification du message. Si vous décidez de modifier une Campaign en fuseau horaire local pour l'envoyer à une heure ultérieure (par exemple, 19 h au lieu de 18 h), les utilisateurs qui étaient dans le Segment ciblé lorsque l'heure d'envoi originale a été choisie recevront toujours le message à l'heure originale (18 h). Si vous modifiez un fuseau horaire local pour envoyer à une heure antérieure (par exemple, 16 h au lieu de 17 h), la Campaign sera toujours envoyée à tous les membres du Segment à l'heure originale (17 h).

{% alert note %}
Pour les composants Canvas, les utilisateurs n'ont pas besoin d'être dans le composant pendant 24 heures pour recevoir le composant suivant du parcours utilisateur pour la distribution en fuseau horaire local.
{% endalert %}

Si vous avez autorisé les utilisateurs à redevenir éligibles pour la Campaign, ils la recevront à nouveau à l'heure originale (17 h). Pour toutes les occurrences suivantes de votre Campaign, cependant, vos messages ne seront envoyés qu'à l'heure mise à jour.

### Quand les modifications apportées aux Campaigns en fuseau horaire local prennent-elles effet ? {#when-do-changes-to-local-time-zone-campaigns-take-effect}

Les Segments cibles pour les Campaigns en fuseau horaire local doivent inclure au moins une fenêtre de 48 heures pour tout filtre basé sur le temps afin de garantir la distribution à l'ensemble du Segment. Par exemple, considérez un Segment ciblant les utilisateurs à leur deuxième jour avec les filtres suivants :

- Première utilisation de l'application il y a plus d'un jour
- Première utilisation de l'application il y a moins de deux jours

La distribution en fuseau horaire local peut manquer des utilisateurs dans ce Segment en fonction de l'heure de distribution et du fuseau horaire local des utilisateurs. En effet, un utilisateur peut quitter le Segment au moment où son fuseau horaire déclenche la distribution.

### Quelles modifications puis-je apporter aux Campaigns planifiées avant le lancement ? {#what-changes-can-i-make-to-scheduled-campaigns-ahead-of-launch}

Lorsque la Campaign est planifiée, vous devez effectuer les modifications sur tout élément autre que la composition du message avant que nous mettions les messages en file d'attente pour l'envoi. Comme pour toutes les Campaigns, vous ne pouvez pas modifier les événements de conversion après le lancement.

### J'ai mis à jour ma Campaign planifiée. Pourquoi ne s'est-elle pas lancée ? {#i-updated-my-scheduled-campaign-why-didnt-it-launch}

Cela peut se produire lorsqu'une Campaign est planifiée pour être lancée exactement au moment où elle a été mise à jour. Par exemple, s'il est actuellement 15 h 10 et que vous avez modifié la Campaign pour qu'elle se lance à 15 h 10 et sélectionné **Mettre à jour la Campaign**, il est maintenant passé 15 h 10, ce qui signifie que l'heure planifiée pour le lancement est dépassée. Au lieu de planifier la Campaign pour la même heure, sélectionnez **Envoyer dès le lancement de la Campaign**.

### Quelle est la « zone de sécurité » avant que les messages d'une Campaign planifiée ne soient mis en file d'attente ? {#what-is-the-safe-zone-before-messages-on-a-scheduled-campaign-are-enqueued}

Nous recommandons d'apporter des modifications aux messages dans les délais suivants :

- **Campaigns planifiées ponctuelles :** Modifiez jusqu'à l'heure d'envoi planifiée.
- **Campaigns planifiées récurrentes :** Modifiez jusqu'à l'heure d'envoi planifiée.
- **Campaigns en heure locale :** Modifiez jusqu'à 24 heures avant l'heure d'envoi planifiée.
- **Campaigns à heure d'envoi optimale :** Modifiez jusqu'à 24 heures avant le jour où la Campaign est planifiée pour être envoyée.

Si vous apportez des modifications à votre message en dehors de ces recommandations, vous pourriez ne pas voir les mises à jour reflétées dans le message envoyé. Par exemple, si vous modifiez l'heure d'envoi trois heures avant qu'une Campaign ne soit planifiée pour être envoyée à 12 h en heure locale, les situations suivantes peuvent se produire :

- Braze n'envoie pas de messages aux utilisateurs qui ont manqué l'heure d'envoi de plus d'une heure.
- Les messages déjà mis en file d'attente peuvent toujours être envoyés à l'heure initialement prévue, plutôt qu'à l'heure ajustée.

Si vous devez apporter des modifications, nous recommandons d'arrêter la Campaign en cours (cela annule tous les messages en file d'attente). Vous pouvez ensuite dupliquer la Campaign, effectuer les modifications nécessaires et lancer la nouvelle Campaign. Vous devrez peut-être exclure de cette Campaign les utilisateurs qui ont déjà reçu la première Campaign. Assurez-vous de réajuster les heures de planification de la Campaign pour tenir compte de l'envoi par fuseau horaire.

### Pourquoi aucun utilisateur n'est-il entré dans ma Campaign planifiée quotidienne le jour du changement d'heure ? {#why-did-no-users-enter-my-daily-scheduled-campaign-on-daylight-saving-time-day}

Les jours de transition vers l'heure d'été ou d'hiver (DST), les Campaigns planifiées quotidiennement peuvent s'exécuter jusqu'à une heure plus tôt ou plus tard que d'habitude, selon que les horloges avancent ou reculent. Si votre Segment repose sur des attributs personnalisés ou des événements avec des horodatages qui se situent dans l'heure précédant l'heure d'envoi planifiée, ces utilisateurs pourraient ne pas encore être éligibles lorsque la Campaign évalue l'éligibilité le jour du changement d'heure.

Par exemple, supposons que les utilisateurs reçoivent généralement une mise à jour d'attribut personnalisé à 15 h UTC, et que votre Campaign s'exécute quotidiennement à 10 h 30 à New York (heure de l'Est). Lorsque New York est à l'heure standard (UTC-5), 10 h 30 ET correspond à 15 h 30 UTC, donc la Campaign s'exécute après l'enregistrement de l'attribut. Lorsque New York passe à l'heure d'été (UTC-4), 10 h 30 ET correspond à 14 h 30 UTC, donc le jour du passage à l'heure d'été, la Campaign peut s'exécuter avant la mise à jour de l'attribut à 15 h UTC. Comme l'attribut qualifiant n'existe pas encore, ces utilisateurs sont filtrés. Si la rééligibilité est désactivée, les utilisateurs qui sont entrés les jours précédents ne peuvent pas réentrer, ce qui entraîne zéro entrée pour ce jour.

Pour éviter cela, assurez-vous que vos mises à jour d'attributs personnalisés ou d'événements se produisent plus d'une heure avant l'heure d'envoi planifiée de la Campaign.

### Pourquoi le nombre d'utilisateurs entrant dans une Campaign ne correspond-il pas au nombre attendu ? {#why-does-the-number-of-users-entering-a-campaign-not-match-the-expected-number}

Le nombre d'utilisateurs entrant dans une Campaign peut différer du nombre attendu en raison de la façon dont les audiences et les déclencheurs sont évalués. Dans Braze, une audience est évaluée avant le déclencheur (sauf lors de l'utilisation d'un déclencheur de [changement d'attribut]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Cela entraînera l'exclusion des utilisateurs de la Campaign s'ils ne font pas initialement partie de votre audience sélectionnée avant que les actions de déclenchement ne soient évaluées.

{% alert tip %}
Pour une assistance supplémentaire concernant la résolution des problèmes de Campaign, assurez-vous de contacter le support Braze dans les 30 jours suivant la survenue de votre problème, car nous ne disposons que des 30 derniers jours de journaux de diagnostic.
{% endalert %}

### Pourquoi les utilisateurs ont-ils reçu ma Campaign deux fois après que je l'ai modifiée ? {#why-did-users-receive-my-campaign-twice-after-i-edited-it}

Si vous modifiez une Campaign active sans l'arrêter au préalable, les utilisateurs peuvent recevoir le message deux fois. Cela se produit parce que la modification d'une Campaign active remet les utilisateurs en file d'attente pour la version mise à jour alors que la file d'attente originale est encore en cours de traitement. Les utilisateurs qui n'ont pas encore reçu le message original peuvent se retrouver dans les deux files d'attente. Pour éviter cela, [arrêtez toujours la Campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch#stopping-your-campaign) avant d'apporter des modifications.

### Quelle est la différence entre les options Exporter les données utilisateur en CSV et Exporter les adresses e-mail en CSV sur ma page d'analyse de Campaign ? {#what-is-the-difference-between-the-csv-export-user-data-and-csv-export-email-address-options-on-my-campaign-analytics-page}

Sélectionner l'option **Exporter les adresses e-mail en CSV** télécharge les données uniquement pour les utilisateurs ayant des adresses e-mail. Par exemple, si vous avez un Segment de 100 000 utilisateurs, mais que seulement 50 000 d'entre eux ont des adresses e-mail, et que vous cliquez sur **Exporter les adresses e-mail en CSV**, l'export ne contient que 50 000 lignes de données. En comparaison, sélectionner **Exporter les données utilisateur en CSV** exporte toutes les données utilisateur.

### Puis-je rechercher une Campaign par son identifiant API ? {#can-i-search-for-a-campaign-by-its-api-identifier}

Oui, utilisez le filtre `api_id:YOUR_API_ID` sur la page **Campaigns** pour rechercher une Campaign par son identifiant API. Consultez [Rechercher des Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/search_campaigns) pour en savoir plus.

### Pourquoi les espaces apparaissent-ils différemment dans les champs de saisie par rapport au texte affiché ? {#why-does-whitespace-appear-differently-in-input-fields-versus-displayed-text}

La gestion des espaces diffère entre les champs de saisie et les composants de texte affichés en raison du style CSS. Dans les composants de texte avec le CSS par défaut `white-space: normal`, plusieurs espaces consécutifs sont réduits à un seul espace lors de l'affichage. Il s'agit du comportement HTML standard pour le texte rendu.

Les champs de saisie préservent les espaces multiples exactement tels que vous les saisissez, car vous devez voir et modifier l'espacement exact pour une saisie de données précise. Cela signifie que du texte avec plusieurs espaces peut apparaître différemment lorsqu'il est affiché dans un champ de saisie (où tous les espaces sont préservés) par rapport à son affichage dans d'autres parties du tableau de bord (où le CSS peut réduire les espaces multiples).

Par exemple, si vous saisissez un nom de Campaign ou un paramètre UTM avec plusieurs espaces dans un champ de saisie, vous voyez tous les espaces préservés. Cependant, lorsque ce même texte apparaît dans les résultats de recherche, les listes de Campaigns ou d'autres composants de texte, les espaces multiples peuvent apparaître comme un seul espace en raison de la gestion CSS des espaces.

### Quelle est la différence entre les Campaigns API et les Campaigns déclenchées par API ? {#what-is-the-difference-between-api-campaigns-and-api-triggered-campaigns}

Les Campaigns déclenchées par API vous permettent de gérer le contenu de la Campaign, les tests multivariés et les règles de rééligibilité dans le tableau de bord de Braze tout en déclenchant la distribution de ce contenu depuis vos propres serveurs et systèmes. Ces messages peuvent également inclure des données supplémentaires à intégrer dans les messages en temps réel.

Les Campaigns API sont utilisées pour suivre les messages envoyés via l'API. Contrairement à la plupart des Campaigns, vous ne spécifiez pas le message, les destinataires ou la planification, mais transmettez plutôt les identifiants dans vos appels API.

### Comment puis-je confirmer si mes utilisateurs ont reçu une Campaign déclenchée par API ? {#how-can-i-confirm-if-my-users-received-an-api-triggered-campaign}

Vous pouvez [créer un Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) en utilisant le filtre **A reçu la Campaign**, puis sélectionner la Campaign déclenchée par API spécifique que vous souhaitez vérifier. Après avoir enregistré le Segment, utilisez l'[endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) pour exporter les utilisateurs de ce Segment.

### Puis-je supprimer une Campaign ? {#can-i-delete-a-campaign}

Non, mais vous pouvez [archiver une Campaign]({{site.baseurl}}/user_guide/messaging/governance/archiving).

### Quelle est la différence entre les Campaigns basées sur des actions et les Campaigns déclenchées par API ? {#what-is-the-difference-between-action-based-and-api-triggered-campaigns}

<style>
table th:nth-child(1) {
    width: 50%;
}
table th:nth-child(3) {
    width: 50%;
}
</style>

#### Basées sur des actions {#action-based}

Les Campaigns à livraison par événement ou déclenchées par événement sont très efficaces pour les messages transactionnels ou basés sur des accomplissements et vous permettent de les déclencher après qu'un utilisateur a effectué un certain événement.

| Avantages | Inconvénients |
| ---- | ---- |
| • Visibilité des payloads JSON entrants dans la plateforme (si l'événement est déclenché par un utilisateur test) via le **Journal d'activité des messages**<br><br>• Les éléments de personnalisation sont inclus dans les propriétés d'événement personnalisé<br><br>• L'événement personnalisé peut être utilisé pour créer des Segments d'utilisateurs éligibles au message | • Consomme des points de donnée |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Basées sur des actions" }

#### Déclenchées par API {#api-triggered}

Les Campaigns déclenchées par API et par serveur sont idéales pour gérer des transactions plus avancées, vous permettant de déclencher la distribution du contenu de la Campaign depuis vos propres serveurs et systèmes. La requête API pour déclencher le message peut également inclure des données supplémentaires à intégrer dans le message en temps réel.

| Avantages | Considérations |
| ---- | ---- |
| • Ne consomme pas de points de donnée<br><br>• Les éléments de personnalisation sont inclus dans les propriétés du payload JSON | • Ne permet pas de créer un Segment d'utilisateurs éligibles au message dans les propriétés du payload JSON<br><br>• Impossible de voir les payloads JSON entrants avec le **Journal d'activité des messages** |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Déclenchées par API" }

### Que dois-je inclure lors de la soumission d'un ticket de support pour une erreur « Request Timed Out » ? {#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error}

Si vous rencontrez une erreur « Request Timed Out » lors de la création ou de la modification d'une Campaign ou d'un Canvas et que vous devez contacter le [support Braze]({{site.baseurl}}/braze_support), incluez les informations suivantes pour accélérer la résolution :

{% multi_lang_include messaging/support_ticket_request_timed_out_details.md context='campaign' %}

### Pourquoi mes analyses d'envoi ne correspondent-elles pas à la limite maximale de destinataires que j'ai définie ? {#why-dont-my-send-analytics-match-the-maximum-recipient-limit-i-set}

Si vous ajoutez ou modifiez une limite maximale de destinataires sur une Campaign active, la limite peut ne pas être reflétée dans vos analyses d'envoi pour les raisons suivantes :

- **Limite ajoutée après le lancement :** Si la limite maximale de destinataires n'est pas définie au lancement de la Campaign, les messages déjà mis en file d'attente avant l'application de la limite sont quand même envoyés. La limite ne prend effet que pour les envois mis en file d'attente après l'enregistrement de la modification.
- **Interaction avec la limitation du débit :** Si une Campaign est également soumise à une limitation du débit, les messages peuvent être distribués sur une fenêtre de temps plus longue. La limite maximale de destinataires est évaluée lorsque les messages sont mis en file d'attente, pas lorsqu'ils sont distribués. Si la limite est modifiée alors que des messages sont déjà dans la file d'attente, la limite originale s'applique à ces messages.
- **Campaigns récurrentes :** Pour les Campaigns récurrentes, chaque envoi planifié évalue la limite maximale de destinataires indépendamment. Modifier la limite entre les envois n'ajuste pas rétroactivement les comptages d'envois précédents.

Pour éviter les décalages, définissez la limite maximale de destinataires avant de lancer la Campaign et évitez de la modifier pendant que des envois sont en cours.

### Pourquoi les envois sont-ils inférieurs à la taille estimée de l'audience ? {#why-are-sends-lower-than-the-estimated-audience-size}

Plusieurs facteurs peuvent faire que le nombre d'envois soit inférieur à la taille estimée de l'audience :

- **Livraison par événement :** Les utilisateurs ne génèrent des envois qu'après avoir effectué le déclencheur, donc les envois s'accumulent au fil du temps et peuvent être en retard par rapport à l'estimation initiale affichée lors de la création de la Campaign.
- **Modifications de l'audience après le lancement :** Modifier les filtres d'entrée ou de ciblage après le lancement peut désynchroniser l'instantané de l'**audience estimée** par rapport aux utilisateurs qui sont encore éligibles lors des envois ultérieurs (par exemple, lorsque les utilisateurs ne sont pas éligibles pour réentrer).
- **Étape Parcours d'audience :** Pour Canvas, une étape [Parcours d'audience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) n'envoie des messages qu'aux utilisateurs qui correspondent à la branche de plus haute priorité pour laquelle ils sont éligibles, ce qui peut réduire les envois par rapport à un comptage de Segment simple.
- **Groupes de contrôle :** Si un [groupe de contrôle global]({{site.baseurl}}/user_guide/audience/global_control_group) ou un groupe de contrôle au niveau de la Campaign est utilisé, une partie de l'audience est exclue de la distribution.
- **Timing de distribution et fenêtres :** Pour les Campaigns en fuseau horaire local ou planifiées, les utilisateurs doivent être éligibles à la fois à l'entrée et au moment de l'envoi ; les utilisateurs dans certains fuseaux horaires peuvent se trouver en dehors de la fenêtre de distribution.
- **Déduplication des e-mails :** Votre Campaign ou Canvas cible plusieurs utilisateurs avec des e-mails identiques, donc un utilisateur aléatoire avec cette adresse e-mail est choisi au moment de l'envoi. Le message n'est envoyé qu'une seule fois et est dédupliqué pour ne pas être envoyé plusieurs fois à la même adresse e-mail, mais votre taille d'audience estimée inclut tous les utilisateurs.
- **Filtres de livrabilité des e-mails :** Pour les Campaigns par e-mail, Braze exclut les utilisateurs qui ont subi un hard bounce, se sont désabonnés des e-mails, ont été marqués comme spam, n'ont pas d'adresse e-mail sur leur profil ou ne sont pas abonnés à un groupe d'abonnement requis. Ces vérifications s'exécutent au moment de l'envoi, donc un utilisateur présent dans votre Segment peut quand même être exclu du comptage réel des envois.
- **Limite de fréquence globale :** Les plafonds au niveau du workspace peuvent empêcher les utilisateurs éligibles de recevoir un autre message dans la même fenêtre, ce qui réduit les envois réalisés.
- **Utilisateurs nouvellement importés :** Les profils qui viennent de devenir éligibles peuvent ne pas recevoir le message avant la prochaine évaluation ou le prochain passage d'envoi, donc les comptages rattrapent lors d'une exécution ultérieure.
- **Accessibilité push :** Pour les Campaigns push, confirmez que l'audience est activée pour les notifications push pour la bonne application. Si vous ne filtrez pas les utilisateurs activés pour les notifications push, l'audience estimée peut inclure des profils qui ne peuvent pas recevoir de notifications push. Vérifiez les **utilisateurs atteignables** dans l'étape **Utilisateurs cibles** pour une estimation opérationnelle plus précise.
- **Limitation du débit de distribution :** Une [limitation du débit de distribution]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) plafonne le nombre de messages que Braze envoie par minute lors d'une seule occurrence d'envoi. Braze répartit la distribution sur une fenêtre plus longue, donc certains envois peuvent être différés, pas encore reflétés dans le comptage, ou non terminés si la limite est faible par rapport à l'audience éligible.
- **Fenêtres de rééligibilité :** Les utilisateurs qui ne sont pas encore rééligibles ne recevront pas le message à nouveau pendant la période de refroidissement, donc les envois sont inférieurs à la taille estimée de l'audience pour cette période.
- **Fenêtre de reporting :** La plage temporelle des analyses peut ne pas inclure tous les envois.
- **Réévaluation du Segment :** Pour les Campaigns basées sur des actions ou planifiées qui réévaluent au moment de l'envoi, les utilisateurs qui étaient dans le Segment lorsque la Campaign a été mise en file d'attente peuvent ne plus être éligibles lorsque le message est effectivement envoyé.
- **Plafonds d'envoi :** Un nombre maximum d'utilisateurs (ou un plafond similaire) dans **Audiences cibles** arrête la distribution lorsque le plafond est atteint.
- **Filtres stricts d'appareil ou de navigateur :** Les filtres qui ne correspondent qu'aux versions les plus récentes d'applications ou de navigateurs réduisent l'ensemble atteignable au moment de l'envoi par rapport à un aperçu de Segment large.

### Où se trouvent les questions fréquemment posées sur la limite de fréquence globale ? {#where-are-frequently-asked-questions-about-global-frequency-capping}

Pour les questions sur les jours calendaires, les notifications push silencieuses, les webhooks, le comportement de Canvas et les sujets connexes, consultez les [Questions fréquemment posées]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/faq) pour [Limitation du débit et limite de fréquence]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).

### Pourquoi ma Campaign connaît-elle des taux d'envoi plus faibles ? {#why-is-my-campaign-experiencing-lower-send-rates}

Si vous constatez que vos Campaigns planifiées quotidiennement envoient à moins d'utilisateurs au fil du temps, vérifiez les points suivants :

- **Vérifiez si la rééligibilité est activée :** Sans rééligibilité, Braze n'envoie le message à chaque utilisateur qu'une seule fois. Pour les Campaigns planifiées quotidiennement, seuls les utilisateurs qui correspondent à l'audience et n'ont pas encore reçu le message sont éligibles pour chaque envoi. À mesure que davantage d'utilisateurs reçoivent le message, chaque envoi ultérieur a moins d'utilisateurs éligibles, donc le volume d'envoi diminue.
- **Vérifiez si l'audience a une composition fixe :** Les audiences construites à partir d'une liste d'utilisateurs fixe (comme un [import CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) utilisé comme filtre de Segment) n'acquièrent pas automatiquement de nouveaux membres. Sans nouveaux entrants, le volume d'envoi ne peut pas remonter à mesure que les utilisateurs sont contactés.

Pour les [limitations du débit de distribution]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) et d'autres facteurs qui réduisent les envois pour une seule occurrence, consultez [Pourquoi les envois sont-ils inférieurs à la taille estimée de l'audience ?](#why-are-sends-lower-than-the-estimated-audience-size).

### Pourquoi les destinataires uniques peuvent-ils dépasser les envois pour les e-mails et les SMS ? {#why-can-unique-recipients-exceed-sends-for-email-and-sms}

Pour les e-mails et les SMS, Braze incrémente les **destinataires uniques** avant la tentative d'envoi par le fournisseur de services de messagerie (ESP) et incrémente les **envois** après une réponse réussie de l'ESP. Les erreurs permanentes (comme les adresses e-mail invalides) ou les adresses en double font que les destinataires uniques dépassent les envois.

### Pourquoi **Dernier envoi** ne correspond-il pas à mon heure d'envoi planifiée ? {#why-doesnt-last-sent-match-my-scheduled-send-time}

Pour une Campaign avec un seul envoi planifié, **Dernier envoi** correspond à l'heure de lancement. Pour les Campaigns récurrentes avec **Envoyer en fuseau horaire local** activé, **Dernier envoi** peut apparaître plus tôt que l'heure planifiée car les envois aux utilisateurs dans des fuseaux horaires antérieurs (par exemple, GMT par rapport à PST) se terminent avant l'heure de planification de votre workspace.

### Pourquoi une Campaign historique arrêtée n'affiche-t-elle plus d'indicateurs sur la page **Analytics** ? {#why-does-a-stopped-historical-campaign-no-longer-show-metrics-on-the-analytics-page}

L'onglet **Analytics** affiche par défaut les 90 derniers jours. Si la Campaign a été envoyée pour la dernière fois en dehors de cette fenêtre, les indicateurs peuvent apparaître à zéro jusqu'à ce que vous ajustiez la plage de dates sur la page **Analytics** pour inclure la période d'envoi de la Campaign. Pour plus d'informations, consultez [Analyse de Campaign]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics).

**Restaurer les données d'interaction** ne restaure pas les analyses de Campaign. Cela s'applique uniquement aux filtres de reciblage et à l'historique d'interaction des utilisateurs. Pour plus d'informations, consultez [Données d'interaction de communication]({{site.baseurl}}/messaging_interaction_data).