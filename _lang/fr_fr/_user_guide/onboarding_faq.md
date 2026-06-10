---
article_title: FAQ
hidden: true
permalink: /onboarding_faq/
excerpt_separator: ""
page_type: glossary
layout: onboarding_faq
description: "Cette page contient un ensemble de questions fréquemment posées, classées par catégorie."

---

{% multi_lang_include video.html id="keAZAlBR9zc" source="youtube" %}


<!--- Users --->

{% api %}

### Comment gérer les données des utilisateurs anonymes ? {#how-do-i-handle-anonymous-user-data}

{% apitags %}
Users
{% endapitags %}

Initialement, lorsqu'un profil utilisateur est reconnu via le SDK, Braze crée un profil utilisateur anonyme avec un `braze_id` associé : un identifiant utilisateur unique défini par Braze.

Pour mieux suivre les utilisateurs anonymes, vous pouvez mettre en place des [alias d'utilisateurs]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/#user-aliases) qui vous permettent d'étiqueter les utilisateurs anonymes à l'aide d'un identifiant. Ces utilisateurs peuvent alors être exportés à l'aide de leurs alias ou référencés par l'API.

Si un profil utilisateur anonyme avec un alias est reconnu ultérieurement avec un `external_id`, il sera traité comme un profil utilisateur identifié normal, mais conservera son alias existant et pourra toujours être référencé par cet alias.

Pour les utilisateurs avec alias que vous souhaitez fusionner avec des utilisateurs identifiés, vous pouvez regrouper tous les champs pertinents pour le profil que vous souhaitez conserver. Vous devrez exporter ces données avant de les supprimer du profil d'alias à l'aide de notre [endpoint Exporter le profil utilisateur par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/). Vous pouvez ensuite utiliser notre [endpoint Suivi des utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour publier ces événements dans le profil que vous avez conservé. Cela vous permettra de préserver les données que vous souhaitez conserver, comme les attributs qui étaient enregistrés auparavant sur un profil et pas l'autre.

Pour une analyse complète des différentes méthodes de collecte des données des utilisateurs nouveaux et existants dans Braze, consultez les [bonnes pratiques en matière de collecte de données]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices/).

{% endapi %}
{% api %}

### Comment importer des utilisateurs déjà collectés et identifiés en dehors de Braze ? {#how-can-i-import-users-i-have-already-collected-and-identified-outside-of-braze}

{% apitags %}
Users
{% endapitags %}

Pour importer des utilisateurs déjà identifiés, vous pouvez charger un CSV dans Braze ou envoyer des données via l'API.

#### CSV

Vous pouvez charger et mettre à jour les profils utilisateurs via des fichiers CSV depuis **Audience** > **Import Users**. Lors de l'importation des données client, vous devez spécifier l'identifiant unique de chaque client, également appelé `external_id`.

Avant de commencer votre importation CSV, il est important de vérifier avec votre équipe d'ingénierie comment les utilisateurs seront identifiés dans Braze. Il s'agit généralement d'un ID de base de données utilisé en interne. Cela doit correspondre à la façon dont les utilisateurs seront identifiés par le SDK de Braze sur mobile et web, afin que chaque client dispose d'un profil utilisateur unique dans Braze sur l'ensemble de ses appareils. En savoir plus sur le [cycle de vie du profil utilisateur]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/) de Braze.

Lorsque vous fournissez un `external_id` dans votre importation, Braze met à jour tout utilisateur existant avec le même `external_id` ou crée un nouvel utilisateur identifié avec cet `external_id` s'il n'en trouve pas.

Pour plus d'informations et pour télécharger des modèles d'importation CSV, consultez la rubrique [Importation d'utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/#csv).

#### API

Pour charger des utilisateurs via l'API, vous pouvez utiliser notre [endpoint Suivi des utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour les importer dans Braze.

Si vous n'êtes pas sûr que l'utilisateur existe déjà dans Braze, vous pouvez utiliser notre [endpoint Exporter le profil utilisateur par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) pour vérifier. Si vous constatez que l'utilisateur existe déjà dans Braze, vous pouvez utiliser notre endpoint `/users/track` pour publier les nouvelles données que vous souhaitez ajouter au profil utilisateur existant dans Braze.

{% alert note %}
Gardez les nuances suivantes à l'esprit lorsque vous utilisez l'endpoint `/users/track` :

- Lorsque vous créez des utilisateurs alias uniquement via cet endpoint, vous devez explicitement définir l'indicateur `_update_existing_only` sur false.
- La mise à jour de l'état de l'abonnement avec cet endpoint mettra à jour l'utilisateur spécifié par son ID externe (par exemple User1) et mettra à jour l'état de l'abonnement de tous les utilisateurs ayant le même e-mail que cet utilisateur (User1).
{% endalert %}

{% endapi %}
{% api %}

### Quelle est la différence entre les statuts d'abonnement aux notifications push ? {#whats-the-difference-between-the-push-subscription-statuses}

{% apitags %}
Users
{% endapitags %}

Il existe trois options d'état d'abonnement aux notifications push : abonné, inscrit et désabonné.

Par défaut, pour que votre utilisateur reçoive vos messages par notification push, son état d'abonnement doit être soit abonné soit inscrit, et il doit être activé pour les notifications push. Vous pouvez remplacer ce paramètre si nécessaire lors de la rédaction d'un message.

| État d'inscription | Description |
|---|---|
| Abonné | État d'abonnement aux notifications push par défaut lorsqu'un profil utilisateur est créé dans Braze. |
| Inscrit | Un utilisateur a explicitement exprimé une préférence pour recevoir des notifications push. Braze déplace automatiquement l'état d'inscription d'un utilisateur vers `Opted-In` si celui-ci accepte une invite de notification push au niveau du système d'exploitation.<br><br>Ceci ne s'applique pas aux utilisateurs sur Android 12 ou antérieur. |
| Désabonné | Un utilisateur s'est explicitement désabonné des notifications push via votre application ou d'autres méthodes fournies par votre marque. Par défaut, les Campaigns de notification push de Braze ciblent uniquement les utilisateurs qui sont `Subscribed` ou `Opted-in` pour les notifications push. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Quelle est la différence entre les statuts d'abonnement aux notifications push ?" }

{% endapi %}
{% api %}

### Que faire si j'ai identifié des utilisateurs en double ? {#what-if-ive-identified-duplicated-users}

{% apitags %}
Users
{% endapitags %}

Si vous avez identifié des utilisateurs en double, vous devrez nettoyer ces profils utilisateurs. Voici la marche à suivre :

1. Exportez les profils utilisateurs à l'aide de notre endpoint `/users/export/ids`.
2. Identifiez le bon profil utilisateur (votre équipe devra, au final, déterminer les informations correctes) et soit :
    - Fusionnez tous les champs pertinents pour le profil que vous souhaitez conserver à l'aide de l'endpoint `/user/track`.
    - Supprimez le doublon, le profil inutile, sans fusionner de données en utilisant l'endpoint users/delete. Une fois que vous avez supprimé un profil utilisateur, **il n'y a aucun moyen de récupérer les informations**.

{% alert important %}
Nous vous recommandons d'importer d'abord les nouveaux profils utilisateurs avec le bon `external_id` ainsi que les attributs personnalisés et événements correspondants. Une fois les profils utilisateurs supprimés, ils ne peuvent plus être récupérés. La suppression doit donc être la toute dernière étape.
{% endalert %}

Quelques points supplémentaires à prendre en compte :

- Toutes les données d'engagement (telles que les Campaigns ou les Canvas reçus) sur les profils utilisateurs en double seront perdues. La seule manière de conserver le contexte d'engagement d'origine est de l'ajouter en tant qu'attribut personnalisé (par exemple, un attribut personnalisé sous forme de tableau de toutes les Campaigns ou Canvas reçus).
- Lors de la migration des profils utilisateurs, votre équipe doit décider quel profil utilisateur en double conserver. Braze ne peut pas décider ou vous fournir une liste de profils à supprimer.
- En fin de compte, il sera important pour votre équipe d'évaluer le processus d'inscription du point de vue de l'expérience de vos utilisateurs et de s'assurer que vous n'appelez la méthode `changeUser()` que lorsqu'un utilisateur est identifié.

{% endapi %}
{% api %}

<!-- Segments -->

### Comment créer un segment lorsque j'importe un groupe d'utilisateurs par CSV ? {#how-do-i-create-a-segment-when-i-import-a-group-of-users-through-csv}

{% apitags %}
Segments
{% endapitags %}

Pour importer votre fichier CSV, accédez à la page **User Import** dans la section Users. Le tableau des **Recent Imports** répertorie jusqu'à vingt de vos importations les plus récentes, leur nom de fichier, le nombre de lignes dans le fichier, le nombre de lignes importées avec succès, le nombre total de lignes dans chaque fichier et l'état de chaque importation.

Le panneau **Import CSV** contient les instructions d'importation et un bouton pour commencer l'importation. Cliquez sur **Select CSV File** et sélectionnez le fichier souhaité. Ensuite, avant de cliquer sur **Start Import**, vous avez la possibilité d'indiquer à Braze ce qu'il doit faire de cette liste sous « What do you want us to do with the users in this CSV ».

Sélectionnez **Import Users in this CSV and also make it possible to retarget this specific batch of users as a group**, puis sélectionnez **Automatically generate a segment from the users who are imported from this CSV**. Après avoir cliqué sur **Start Import**, Braze charge votre fichier, vérifie les en-têtes de colonne et les types de données de chaque colonne, et crée un segment.

Pour télécharger un modèle CSV, consultez la rubrique [Importation d'utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/#csv).

{% endapi %}
{% api %}

### Quels types de filtres puis-je utiliser lors de la création d'un segment ? {#what-types-of-filters-can-i-use-when-creating-a-segment}

{% apitags %}
Segments
{% endapitags %}

Le SDK de Braze met à votre disposition un puissant arsenal de filtres pour segmenter et cibler vos utilisateurs en fonction de fonctionnalités et d'attributs spécifiques. Vous pouvez utiliser le glossaire des [filtres de segmentation]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/) pour rechercher ou affiner ces filtres par catégorie (données personnalisées, activité de l'utilisateur, reciblage, activité marketing, attributs de l'utilisateur, attribution d'installation, activité sociale, test, autre).

{% endapi %}
{% api %}

### Comment paramétrer le ciblage par localisation pour segmenter les utilisateurs en fonction de leur emplacement le plus récent et l'utiliser dans mes campagnes et stratégies basées sur la localisation ? {#how-do-i-set-up-location-targeting-so-that-i-can-segment-users-by-their-most-recent-location-and-use-it-in-my-location-based-campaigns-and-strategies}

{% apitags %}
Segments
{% endapitags %}

Accédez à la page **Segments**, sous Engagement, pour afficher tous vos segments d'utilisateurs actuels. Sur cette page, vous pouvez créer et nommer de nouveaux segments. Pour commencer, cliquez sur **Create Segment** et donnez un nom à votre segment.

Après avoir créé votre segment, ajoutez un filtre `Most Recent Location` pour cibler les utilisateurs en fonction du dernier emplacement où ils ont utilisé votre application. Vous pouvez sélectionner des utilisateurs dans une région circulaire standard ou créer une région polygonale personnalisée.

- Pour les régions circulaires, vous pouvez déplacer l'origine et ajuster le rayon de localisation pour votre segmentation.
- Pour les régions polygonales, vous pouvez désigner plus précisément les zones que vous souhaitez inclure dans votre segment.

{% alert tip %}
Vous souhaitez tirer parti du ciblage par localisation avec l'aide d'un partenaire Braze ? Consultez nos [partenaires de localisation contextuelle]({{site.baseurl}}/partners/message_personalization/) Braze disponibles.
{% endalert %}

{% endapi %}
{% api %}

### Comment cibler des listes précises d'utilisateurs en fonction de leurs événements personnalisés ou de leur comportement d'achat sur les 365 derniers jours ? {#how-can-i-target-precise-lists-of-users-based-on-their-custom-event-and-purchase-behavior-in-the-past-365-days}

{% apitags %}
Segments
{% endapitags %}

Vous pouvez utiliser les [extensions de segments]({{site.baseurl}}/user_guide/audience/segments/segment_extension/) ! Les extensions de segments vous permettent de cibler une liste d'utilisateurs plus précise que ce que vous pourriez faire avec un segment classique.

Vous pouvez créer jusqu'à 10 extensions de segments par espace de travail. Une fois ces listes d'extension générées, elles peuvent être incluses ou exclues en tant que filtre dans vos segments. Lorsque vous créez une extension de segment, vous pouvez également choisir que la liste soit régénérée une fois toutes les 24 heures.

1. Sous Engagements, développez **Segments** et cliquez sur **Segment Extension**.
2. Dans le tableau des extensions de segments, cliquez sur **+ Create New Extension**.
3. Nommez votre extension de segment en décrivant le type d'utilisateurs que vous souhaitez cibler. Cela vous permettra de retrouver facilement cette extension lorsque vous souhaiterez l'utiliser comme filtre dans votre segment.
4. Sélectionnez un critère d'achat ou d'événement personnalisé pour le ciblage.
5. Choisissez quel produit acheté ou événement personnalisé spécifique vous souhaitez cibler pour votre liste d'utilisateurs.
6. Choisissez combien de fois (supérieur à, inférieur à ou égal à) l'utilisateur devrait avoir effectué l'événement, et le nombre de jours à analyser, jusqu'à 365 jours.

Pour accroître la précision du ciblage, vous pouvez sélectionner **Add Property Filters** et segmenter en fonction des propriétés spécifiques de votre achat ou événement personnalisé. Braze prend en charge la segmentation des propriétés d'événement basée sur les objets de type chaîne de caractères, numérique, booléen et temporel.

Nous prenons également en charge la segmentation basée sur les [propriétés de l'événement imbriqué]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects/).

Les extensions de segments s'appuient sur le stockage à long terme des propriétés d'événement et ne sont pas soumises à la limite de stockage de 30 jours des propriétés d'événement personnalisé. Cela signifie que vous pouvez analyser les propriétés d'événement suivies au cours de l'année écoulée, et que le suivi n'attend pas que l'extension ait été configurée au préalable.

{% alert note %}
L'utilisation de propriétés d'événement dans les extensions de segments n'affecte pas la consommation de vos points de données.
{% endalert %}

{% endapi %}
{% api %}

#### Maintenir les extensions de segments à jour {#keeping-segment-extensions-up-to-date}

{% apitags %}
Segments
{% endapitags %}

Vous pouvez indiquer si vous souhaitez que cette extension représente un instantané à un moment donné, ou si vous souhaitez qu'elle soit régénérée quotidiennement. Votre extension sera toujours traitée après la sauvegarde initiale. Si vous souhaitez que l'extension soit régénérée quotidiennement, sélectionnez **Regenerate Extension Daily** et la régénération commencera chaque jour vers minuit dans le fuseau horaire de votre entreprise.

Lorsque vous avez terminé, cliquez sur **Save**. Votre extension va commencer à être traitée. La durée nécessaire pour générer votre extension dépend du nombre d'utilisateurs que vous avez, du nombre d'événements personnalisés ou d'événements d'achat que vous collectez, et du nombre de jours que vous analysez dans l'historique.

Enfin, après avoir créé une extension, vous pouvez l'utiliser comme filtre lorsque vous créez un segment ou définissez une audience pour une campagne ou un Canvas. Commencez par choisir `Braze Segment Extension` dans la liste des filtres de la section **User Attributes**. Dans la liste des filtres Braze Segment Extension, choisissez l'extension que vous souhaitez inclure ou exclure de ce segment. Pour afficher les critères de l'extension, cliquez sur **View Extension Details**. Vous pouvez maintenant créer votre segment comme d'habitude.

{% endapi %}
{% api %}

<!-- Campaigns -->

### Comment créer une campagne multicanale ? {#how-do-you-create-a-multichannel-campaign}

{% apitags %}
Campaigns
{% endapitags %}

Consultez [Campaigns multicanales]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign/#multichannel-campaigns) dans **Créer une campagne** pour les étapes de configuration, les canaux pris en charge et la façon de basculer entre les composeurs.

{% endapi %}
{% api %}

### Comment commencer à tester et optimiser les campagnes ? {#what-are-some-ways-i-can-start-testing-and-optimizing-campaigns}

{% apitags %}
Campaigns
{% endapitags %}

La création de campagnes multivariées et l'exécution de Canvas avec plusieurs variantes sont un excellent point de départ ! Par exemple, vous pouvez lancer une [campagne multivariée]({{site.baseurl}}/user_guide/messaging/ab_testing/) pour tester un message avec différentes copies ou lignes d'objet. Les Canvas avec plusieurs variantes sont utiles pour tester des flux de travail complets.

{% endapi %}
{% api %}

### Pourquoi y a-t-il une différence entre le nombre de destinataires uniques et le nombre d'envois pour une campagne ou un Canvas donné ? {#why-is-there-a-difference-between-the-number-of-unique-recipients-and-the-number-of-sends-for-a-given-campaign-or-canvas}

{% apitags %}
Campaigns
{% endapitags %}

Une explication possible de cette différence est que la rééligibilité est activée pour la campagne ou le Canvas. Dans ce cas, les utilisateurs qui remplissent les conditions du segment et des paramètres de distribution peuvent recevoir le message plusieurs fois. Si la rééligibilité n'est pas activée, l'explication probable de la différence entre les envois et les destinataires uniques est que des utilisateurs possèdent plusieurs appareils sur différentes plateformes associés à leurs profils.

Par exemple, si vous avez un Canvas qui comporte à la fois des notifications push iOS et web, un utilisateur donné possédant à la fois un téléphone et un ordinateur de bureau peut recevoir plus d'un message.

{% endapi %}
{% api %}

### Qu'offre la distribution selon le fuseau horaire local ? {#what-does-local-time-zone-delivery-offer}

{% apitags %}
Campaigns
{% endapitags %}

La distribution selon le fuseau horaire local vous permet de distribuer des campagnes de communication à un segment en fonction du fuseau horaire individuel de chaque utilisateur. Sans cette option, les campagnes seront planifiées en fonction des paramètres de fuseau horaire de votre entreprise dans Braze.

Par exemple, une entreprise basée à Londres qui envoie une campagne à midi atteindra les utilisateurs sur la côte ouest des États-Unis à 4 h du matin. Si votre application n'est disponible que dans certains pays, cela peut ne pas poser de problème, sinon nous vous recommandons vivement d'éviter d'envoyer des notifications push tôt le matin à votre base d'utilisateurs !

{% endapi %}
{% api %}

### Comment Braze reconnaît-il le fuseau horaire d'un utilisateur ? {#how-does-braze-recognize-a-users-time-zone}

{% apitags %}
Campaigns
{% endapitags %}

Braze détermine automatiquement le fuseau horaire d'un utilisateur à partir de son appareil. Cela garantit la précision des fuseaux horaires et une couverture complète de vos utilisateurs. Les utilisateurs créés via l'API utilisateur ou n'ayant pas de fuseau horaire auront le fuseau horaire de votre entreprise comme fuseau par défaut jusqu'à ce qu'ils soient reconnus dans votre application par le SDK.

Vous pouvez vérifier le fuseau horaire de votre entreprise dans les [paramètres de votre entreprise]({{site.baseurl}}/user_guide/administer/global/admin_settings/).

{% endapi %}
{% api %}

### Comment planifier une campagne selon le fuseau horaire local ? {#how-do-i-schedule-a-local-time-zone-campaign}

{% apitags %}
Campaigns
{% endapitags %}

Lors de la planification d'une campagne, vous devez choisir de l'envoyer à une heure donnée, puis sélectionner **Send campaign to users in their local time zone**.

Braze recommande vivement de planifier toutes les campagnes selon le fuseau horaire local 24 heures à l'avance. Étant donné qu'une telle campagne doit être envoyée sur une journée entière, les planifier 24 heures à l'avance permet à votre message d'atteindre l'ensemble de votre segment. Cependant, vous pouvez planifier ces campagnes moins de 24 heures à l'avance si nécessaire. N'oubliez pas que Braze n'enverra pas de messages aux utilisateurs qui ont manqué l'heure d'envoi de plus d'une heure.

Par exemple, s'il est 13 h et que vous planifiez une campagne selon le fuseau horaire local pour 15 h, celle-ci sera immédiatement envoyée à tous les utilisateurs dont l'heure locale est comprise entre 15 h et 16 h, mais pas à ceux dont l'heure locale est 17 h. De plus, l'heure d'envoi que vous choisissez pour votre campagne ne doit pas encore être dépassée dans le fuseau horaire de votre entreprise.

La modification d'une campagne selon le fuseau horaire local planifiée moins de 24 heures à l'avance ne modifiera pas la planification du message. Si vous décidez de modifier une campagne selon le fuseau horaire local pour qu'elle soit envoyée plus tard (par exemple, à 19 h au lieu de 18 h), les utilisateurs qui se trouvaient dans le segment ciblé lorsque l'heure d'envoi initiale a été choisie recevront toujours le message à l'heure d'origine (18 h). Si vous modifiez le fuseau horaire local pour que l'envoi se fasse plus tôt (par exemple, à 16 h au lieu de 17 h), la campagne sera toujours envoyée à tous les membres du segment à l'heure d'origine (17 h).

{% alert note %}
Pour les étapes de Canvas, les utilisateurs n'ont pas besoin d'être dans l'étape pendant 24 heures pour recevoir l'étape suivante lors de la distribution selon le fuseau horaire local.
{% endalert %}

Si vous avez permis aux utilisateurs de devenir rééligibles pour la campagne, ils la recevront à nouveau à l'heure d'origine (17 h). Cependant, pour toutes les occurrences ultérieures de votre campagne, vos messages ne seront envoyés qu'à l'heure mise à jour.

{% endapi %}
{% api %}

### Quand les modifications apportées aux campagnes selon le fuseau horaire local prennent-elles effet ? {#when-do-changes-to-local-time-zone-campaigns-take-effect}

{% apitags %}
Campaigns
{% endapitags %}

Les segments cibles pour les campagnes selon le fuseau horaire local doivent inclure une fenêtre d'au moins 48 heures pour que les filtres temporels garantissent la distribution à l'ensemble du segment. Par exemple, considérez un segment ciblant les utilisateurs lors de leur deuxième jour avec les filtres suivants :

- Première utilisation de l'application il y a plus d'un jour
- Première utilisation de l'application il y a moins de 2 jours

La distribution selon le fuseau horaire local peut manquer des utilisateurs de ce segment en fonction de l'heure de distribution et de leur fuseau horaire local. Cela est dû au fait qu'un utilisateur peut quitter le segment avant que son fuseau horaire ne déclenche la distribution.

{% endapi %}
{% api %}

### Quels changements puis-je apporter aux campagnes planifiées avant le lancement ? {#what-changes-can-i-make-to-scheduled-campaigns-ahead-of-launch}

{% apitags %}
Campaigns
{% endapitags %}

Lorsque la campagne est planifiée, les modifications portant sur autre chose que la composition du message doivent être effectuées avant la mise en file d'attente des messages pour l'envoi. Comme pour toutes les campagnes, vous ne pouvez pas modifier les événements de conversion après le lancement de la campagne.

{% endapi %}
{% api %}

### Quelle est la « zone sécurisée » avant que les messages d'une campagne planifiée soient mis en file d'attente ? {#what-is-the-safe-zone-before-messages-on-a-scheduled-campaign-are-queued}

{% apitags %}
Campaigns
{% endapitags %}

- Les campagnes planifiées ponctuelles peuvent être modifiées jusqu'à l'heure d'envoi prévue.
- Les campagnes planifiées récurrentes peuvent être modifiées jusqu'à l'heure d'envoi prévue.
- Les campagnes à heure d'envoi locale peuvent être modifiées jusqu'à 24 heures avant l'heure d'envoi prévue.
- Les campagnes à heure d'envoi optimale peuvent être modifiées jusqu'à 24 heures avant le jour où la campagne est planifiée pour l'envoi.

{% endapi %}
{% api %}

### Que se passe-t-il si je fais une modification dans la « zone sécurisée » ? {#what-if-i-make-an-edit-within-the-safe-zone}

{% apitags %}
Campaigns
{% endapitags %}

Modifier l'heure d'envoi des campagnes à ce moment-là peut entraîner un comportement indésirable, par exemple :

- Braze n'enverra pas de messages aux utilisateurs qui ont manqué l'heure d'envoi de plus d'une heure.
- Les messages déjà mis en file d'attente peuvent toujours être envoyés à l'heure initialement prévue, plutôt qu'à l'heure modifiée.

{% endapi %}
{% api %}

### Que dois-je faire si la « zone sécurisée » est déjà passée ? {#what-should-i-do-if-the-safe-zone-has-already-passed}

{% apitags %}
Campaigns
{% endapitags %}

Pour garantir que les campagnes fonctionnent comme souhaité, nous vous recommandons d'arrêter la campagne en cours (cela annulera tous les messages mis en file d'attente). Vous pouvez ensuite dupliquer la campagne, apporter les modifications nécessaires et lancer la nouvelle campagne. Vous devrez peut-être exclure de cette campagne les utilisateurs qui ont déjà reçu la première.

Assurez-vous de réajuster les heures de planification de la campagne pour permettre l'envoi selon le fuseau horaire.

{% endapi %}
{% api %}

### Quand Braze évalue-t-il les utilisateurs pour la distribution selon le fuseau horaire local ? {#when-does-braze-evaluate-users-for-local-time-zone-delivery}

{% apitags %}
Campaigns
{% endapitags %}

Braze évalue l'éligibilité des utilisateurs à l'entrée à deux moments :

- À l'heure des Samoa (UTC+13) du jour planifié
- À l'heure locale de l'utilisateur le jour planifié

Pour qu'un utilisateur soit éligible à l'entrée, il doit remplir les conditions lors des deux vérifications. Par exemple, si un Canvas est prévu pour être lancé le 7 août 2021 à 14 h selon le fuseau horaire local, cibler un utilisateur situé à New York nécessite les vérifications d'éligibilité suivantes :

- New York, le 6 août 2021 à 21 h
- New York, le 7 août 2021 à 14 h

Pour être éligible, l'utilisateur doit correspondre à votre audience et à vos filtres lors des deux évaluations. Si l'utilisateur n'est pas éligible lors de la première vérification, Braze ne procède pas à la seconde. Il n'y a pas de durée minimale pendant laquelle un utilisateur doit avoir été dans le segment avant le lancement — seule l'éligibilité à chaque vérification compte.

Ce comportement d'évaluation est distinct de [la planification anticipée de la campagne dans le tableau de bord]({{site.baseurl}}/user_guide/messaging/campaigns/faq/#how-do-i-schedule-a-local-time-zone-campaign). Pour l'explication complète, des exemples et des conseils de planification, consultez [Quand Braze évalue-t-il les utilisateurs pour la distribution selon le fuseau horaire local ?]({{site.baseurl}}/user_guide/messaging/campaigns/faq/#when-does-braze-evaluate-users-for-local-time-zone-delivery) et [Comment planifier une campagne selon le fuseau horaire local ?]({{site.baseurl}}/user_guide/messaging/campaigns/faq/#how-do-i-schedule-a-local-time-zone-campaign) dans la FAQ Campaigns.

{% endapi %}
{% api %}

### Pourquoi le nombre d'utilisateurs entrant dans une campagne ne correspond-il pas au nombre attendu ? {#why-does-the-number-of-users-entering-a-campaign-not-match-the-expected-number}

{% apitags %}
Campaigns
{% endapitags %}

Le nombre d'utilisateurs entrant dans une campagne peut différer du nombre attendu en raison de la façon dont les audiences et les déclencheurs sont évalués. Dans Braze, une audience est évaluée avant le déclencheur (sauf en cas d'utilisation d'un [déclencheur de changement d'attribut]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers/#change-custom-attribute-value)). Les utilisateurs seront alors exclus de la campagne s'ils ne font pas initialement partie de l'audience sélectionnée, avant l'évaluation des actions de déclenchement.

{% endapi %}
{% api %}

<!-- Canvases -->

### Que se passe-t-il si l'audience et l'heure d'envoi sont identiques pour un Canvas qui a une variante, mais plusieurs branches ? {#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches}

{% apitags %}
Canvases
{% endapitags %}

Nous mettons en file d'attente un travail pour chaque étape — ils s'exécutent à peu près au même moment et l'un d'entre eux « gagne ». En pratique, la répartition peut être relativement uniforme, mais il y a probablement un léger biais en faveur de l'étape créée en premier.

De plus, nous ne pouvons pas garantir avec précision ce à quoi ressemblera cette répartition. Si vous souhaitez garantir un partage égal, ajoutez un filtre de [numéro de compartiment aléatoire]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/).

{% endapi %}
{% api %}

### Que se passe-t-il lorsque vous arrêtez un Canvas ? {#what-happens-when-you-stop-a-canvas}

{% apitags %}
Canvases
{% endapitags %}

Lorsque vous arrêtez un Canvas, les éléments suivants s'appliquent :

- Les utilisateurs ne pourront plus entrer dans le Canvas.
- Plus aucun message ne sera envoyé, quel que soit le niveau auquel se situe un utilisateur dans le flux.
    - **Exception :** les Canvas par e-mail ne s'arrêteront pas immédiatement. Une fois que les requêtes d'envoi sont transmises à SendGrid, il n'est plus possible d'empêcher leur distribution à l'utilisateur.

{% alert note %}
Arrêter un Canvas ne fera pas sortir les utilisateurs qui attendent dans une étape. Si vous réactivez le Canvas et que les utilisateurs attendent toujours, ils termineront l'étape et passeront au composant suivant. Cependant, si le moment où l'utilisateur aurait dû passer au composant suivant est dépassé, il quittera le Canvas.
{% endalert %}

{% endapi %}
{% api %}

### À quel moment un événement d'exception est-il déclenché ? {#when-does-an-exception-event-trigger}

{% apitags %}
Canvases
{% endapitags %}

Les événements d'exception ne se déclenchent que lorsque l'utilisateur attend de recevoir le composant Canvas auquel il est associé. Si un utilisateur effectue une action à l'avance, l'événement d'exception ne sera pas déclenché.

Si vous souhaitez exclure les utilisateurs qui ont effectué un certain événement à l'avance, utilisez plutôt des [filtres]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/).

{% endapi %}
{% api %}

### En quoi la modification d'un Canvas affecte-t-elle les utilisateurs déjà présents dans le Canvas ? {#how-does-editing-a-canvas-affect-users-already-in-the-canvas}

{% apitags %}
Canvases
{% endapitags %}

Si vous modifiez certaines étapes d'un Canvas à plusieurs étapes, les utilisateurs qui étaient déjà dans l'audience mais n'ont pas encore reçu les étapes recevront la version mise à jour du message. Notez que cela ne se produira que s'ils n'ont pas encore été évalués pour l'étape.

Pour plus d'informations sur ce que vous pouvez ou ne pouvez pas modifier après le lancement, consultez [Modifier votre Canvas après le lancement]({{site.baseurl}}/post-launch_edits/).

{% endapi %}
{% api %}

### Comment le suivi des conversions utilisateur est-il effectué dans un Canvas ? {#how-are-user-conversions-tracked-in-a-canvas}

{% apitags %}
Canvases
{% endapitags %}

Un utilisateur ne peut effectuer qu'une seule conversion par entrée dans un Canvas.

Les conversions sont attribuées au message le plus récent reçu par l'utilisateur pour cette entrée. Le bloc de synthèse au début d'un Canvas reflète toutes les conversions effectuées par les utilisateurs dans ce parcours, qu'ils aient reçu un message ou non. Chaque étape suivante n'affichera que les conversions qui se sont produites lorsque c'était l'étape la plus récente reçue par l'utilisateur.

{% details Cas d'utilisation %}

#### Cas d'utilisation 1 {#use-case-1}

Il existe un parcours Canvas avec 10 notifications push et l'événement de conversion est « lancement de session » (« Ouvre l'application ») :

- L'utilisateur A ouvre l'application après être entré mais avant de recevoir le premier message.
- L'utilisateur B ouvre l'application après chaque notification push.

**Résultat :**
La synthèse affichera deux conversions tandis que les étapes individuelles afficheront une conversion pour la première étape et zéro pour toutes les étapes suivantes.

{% alert note %}
Si les heures calmes sont actives lorsque l'événement de conversion se produit, les mêmes règles s'appliquent.
{% endalert %}

#### Cas d'utilisation 2 {#use-case-2}

Il existe un Canvas d'une seule étape avec des heures calmes :

1. L'utilisateur entre dans le Canvas.
2. La première étape ne présente pas de délai, mais se situe dans les heures calmes, le message est donc supprimé.
3. L'utilisateur effectue l'événement de conversion.

**Résultat :**
L'utilisateur sera comptabilisé comme converti dans la variante globale du Canvas, mais pas dans l'étape puisqu'il ne l'a pas reçue.

{% enddetails %}

{% endapi %}
{% api %}

### Lorsqu'on examine le nombre d'utilisateurs uniques, l'analytique Canvas ou le segmenteur est-il plus précis ? {#when-looking-at-the-number-of-unique-users-is-canvas-analytics-or-the-segmenter-more-accurate}

{% apitags %}
Canvases
{% endapitags %}

Le segmenteur fournit une statistique plus précise pour les données d'utilisateurs uniques par rapport aux statistiques de Canvas ou de campagne. En effet, les statistiques de Canvas et de campagne sont des nombres que Braze incrémente lorsqu'un événement se produit — ce qui signifie que des variables peuvent entraîner des différences par rapport au segmenteur. Par exemple, les utilisateurs peuvent effectuer plusieurs conversions pour un Canvas ou une campagne.

{% endapi %}
{% api %}

### Pourquoi le nombre d'utilisateurs entrant dans un Canvas ne correspond-il pas au nombre attendu ? {#why-does-the-number-of-users-entering-a-canvas-not-match-the-expected-number}

{% apitags %}
Canvases
{% endapitags %}

Le nombre d'utilisateurs entrant dans un Canvas peut différer du nombre attendu en raison de la façon dont les audiences et les déclencheurs sont évalués. Dans Braze, une audience est évaluée avant le déclencheur (sauf en cas d'utilisation d'un déclencheur de [changement d'attribut]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers/#change-custom-attribute-value)). Les utilisateurs seront alors exclus du Canvas s'ils ne font pas partie de l'audience sélectionnée, avant l'évaluation des actions de déclenchement.

{% endapi %}
{% api %}

<!-- Analytics -->

### Quels indicateurs Braze mesure-t-il ? {#what-metrics-does-braze-measure}

{% apitags %}
Analytics
{% endapitags %}

Selon le canal, Braze mesure une variété d'indicateurs pour vous permettre de déterminer le succès d'une campagne et d'orienter les campagnes futures. Vous trouverez une liste complète dans notre [glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/analytics/metrics_glossary/).

{% endapi %}
{% api %}

### Comment le chiffre d'affaires est-il calculé dans Braze ? {#how-is-revenue-calculated-in-braze}

{% apitags %}
Analytics
{% endapitags %}

Sur la page **Revenue**, vous pouvez consulter des données sur le chiffre d'affaires ou les achats sur des périodes spécifiques, pour un produit spécifique, ou le total du chiffre d'affaires ou des achats de votre application. Ces montants sont générés à partir des achats effectués par les destinataires des campagnes au cours d'une période de conversion donnée.

Cela dit, il est important de noter que Braze est un outil de marketing et non un outil de gestion du chiffre d'affaires. Notre [objet d'achat]({{site.baseurl}}/api/objects_filters/purchase_object/) ne prend pas en charge les remboursements et les annulations, il se peut donc que vous constatiez des écarts lorsque vous comparez les données avec d'autres outils.

{% endapi %}
{% api %}

### Quelles capacités de reporting Currents offre-t-il ? {#what-reporting-capabilities-does-currents-enable}

{% apitags %}
Analytics
{% endapitags %}

Currents diffuse en continu des données d'engagement de messagerie et de comportement des clients vers l'un de nos nombreux partenaires de données, vous permettant d'exploiter les données uniques et précieuses créées par Braze pour alimenter vos efforts d'aide à la décision et d'analytique avec d'autres partenaires de premier plan.

Ces données vont au-delà des simples indicateurs d'engagement des messages et peuvent également inclure des données plus complexes comme les attributs personnalisés et la performance des événements. Pour plus de détails, consultez notre [glossaire des événements Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/).

{% endapi %}
{% api %}

### Comment planifier un rapport d'engagement récurrent ? {#how-can-i-schedule-a-recurring-engagement-report}

{% apitags %}
Analytics
{% endapitags %}

Pour planifier un rapport d'engagement récurrent, procédez comme suit :

1. Dans votre tableau de bord, accédez à **Engagement Reports**, sous **Data**.
2. Cliquez sur **+ Create New Report**.
3. Ajoutez les [Campaigns et messages Canvas]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports/#manually-select-campaigns-or-canvases) (individuellement ou [par tag]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports/#automatically-select-campaigns-or-canvases)) que vous souhaitez compiler dans votre rapport.
4. [Ajoutez des statistiques]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports/#add-statistics-to-your-report) à votre rapport.
5. Sélectionnez la compression et le délimiteur pour votre rapport.
6. Saisissez les adresses e-mail des utilisateurs de l'entreprise qui doivent recevoir ce rapport.
7. Sélectionnez la [période]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports/#time-frame) sur laquelle vous souhaitez que votre rapport analyse les données.
8. Sélectionnez les [intervalles (quotidien, hebdomadaire, etc.)]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports/#data-display) auxquels vous souhaitez voir la ventilation de vos données.
9. Planifiez votre rapport pour un [envoi immédiat]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports/#send-immediately) ou à une [date future spécifiée]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports/#send-at-designated-time).
10. Exécutez le rapport, puis ouvrez-le dans votre e-mail quand il arrive !

{% endapi %}
{% api %}

### Quelle est la différence entre les rapports d'engagement et le générateur de rapports ? {#whats-the-difference-between-engagement-reports-and-the-report-builder}

{% apitags %}
Analytics
{% endapitags %}

Les rapports d'engagement vous fournissent des CSV de statistiques d'engagement pour des messages spécifiques de Campaigns et Canvas via un e-mail déclenché. Certaines données sont agrégées au niveau de la campagne ou du Canvas et non au niveau de la variante ou de l'étape individuelle. Les rapports ne sont pas enregistrés dans le tableau de bord, et relancer le rapport peut fournir des statistiques actualisées.

Le générateur de rapports vous permet de comparer les résultats de plusieurs Campaigns ou Canvas dans une vue unique afin de déterminer facilement quelles stratégies d'engagement ont le plus impacté vos indicateurs clés. Pour les Campaigns comme pour les Canvas, vous pouvez exporter vos données et enregistrer votre rapport pour une consultation ultérieure.

Pour plus d'informations sur l'utilisation des rapports et de l'analytique dans Braze, consultez l'[aperçu des rapports]({{site.baseurl}}/user_guide/analytics/reports/).

{% endapi %}