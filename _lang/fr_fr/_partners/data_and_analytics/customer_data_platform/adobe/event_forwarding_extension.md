---
nav_title: "Extension du transfert d'événements"
article_title: Adobe
description: "Cet article de référence décrit l'extension de transfert d'événements Braze qui vous permet d'exploiter les données capturées dans Adobe Experience Platform Edge Network et de les envoyer à Braze sous la forme d'événements côté serveur."
page_type: partner
page_order: 2
search_tag: Partner
---

# Extension de transfert d'événements de l'API Track Events {#track-events-api-event-forwarding-extension}

> L'extension de [transfert d'événements](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en) de l'API Track Events de Braze vous permet d'exploiter les données capturées dans Adobe Experience Platform Edge Network et de les envoyer à Braze sous la forme d'événements côté serveur à l'aide de l'API [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

Ce document décrit les cas d'usage de l'extension, comment l'installer dans vos bibliothèques de transfert d'événements et comment utiliser ses fonctionnalités dans une [règle](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) de transfert d'événements.

{% alert note %}
L'utilisation du transfert d'événements Adobe peut augmenter votre consommation de points de données Braze. Pour plus d'informations, reportez-vous à la documentation de Braze sur les [points de données]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points#billable-data-points).
{% endalert %}

## Cas d'usage {#use-cases}

Cette extension doit utiliser les données de l'Edge Network dans Braze pour tirer parti de ses capacités d'analyse client et de ciblage.

Par exemple, prenons une organisation de vente au détail avec une présence multicanale (site web et mobile) qui capture des données transactionnelles ou conversationnelles sous forme de données d'événements depuis ses plateformes web et mobiles.

En utilisant diverses règles de [tags](https://experienceleague.adobe.com/docs/experience-platform/tags/home.html?lang=en), ces données sont envoyées à l'Edge Network en temps réel. À partir de là, l'extension de transfert d'événements Braze envoie automatiquement les événements pertinents à Braze depuis le côté serveur.

## Limites de débit {#rate-limits}

| API | Limites de débit |
| --- | --- |
| User Track | 50 000 requêtes par minute.<br><br>Consultez la [documentation de l'API User Track]({{site.baseurl}}/api/endpoints/user_data/post_user_track#rate-limit) pour plus de détails.
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limites de débit" }

## Intégration {#integration}

### Étape 1 : Rassembler les informations de configuration requises {#step-1-gather-required-configuration-details}

Pour connecter le réseau Edge Network à Braze, les éléments suivants sont nécessaires :

| Type de clé | Description |
| --- | --- |
| Instance Braze | Votre instance Braze peut être obtenue auprès de votre gestionnaire d'onboarding Braze ou consultée sur la [page d'aperçu de l'API]({{site.baseurl}}/api/basics#endpoints). |
| Clé API REST Braze | Une clé API REST Braze avec toutes les permissions. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 1 : Rassembler les informations de configuration requises" }

### Étape 2 : Créer un secret {#step-2-create-a-secret}

Créez un nouveau [secret de transfert d'événements](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/secrets.html?lang=en) et définissez la valeur sur votre [clé API Braze](https://experienceleague.adobe.com/docs/experience-platform/tags/extensions/server/braze/overview.html?lang=en#configuration-details). Celui-ci sera utilisé pour authentifier la connexion à votre compte tout en sécurisant la valeur.

### Étape 3 : Installer et configurer l'extension Braze {#step-3-install-and-configure-the-braze-extension}

1. Pour installer l'extension, [créez une propriété de transfert d'événements](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en#properties) ou choisissez une propriété existante à modifier.
2. Ensuite, sélectionnez **Extensions** dans la navigation de gauche. Dans l'onglet **Catalog**, sélectionnez **Install** sur la carte de l'extension Braze.
3. Sur l'écran suivant, saisissez votre instance REST et votre clé API, puis sélectionnez **Save** lorsque vous avez terminé.

### Étape 4 : Créer une règle d'envoi d'événement {#step-4-create-a-send-event-rule}

Après avoir installé l'extension, créez une nouvelle [règle](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) de transfert d'événements et configurez ses conditions selon vos besoins. Lors de la configuration des actions pour la règle, sélectionnez l'extension **Braze**, puis sélectionnez **Send Event** comme type d'action.

![Action de règle de transfert d'événements Adobe configurée pour utiliser Braze Send Event.]({% image_buster /assets/img/efe.png %})

{% tabs local %}
{% tab Identification de l'utilisateur %}

| Champ | Description |
| --- | --- |
| External user ID | Un UUID ou GUID long, aléatoire et bien distribué. Si vous choisissez une autre méthode pour nommer vos ID utilisateur, ils doivent également être longs, aléatoires et bien distribués. En savoir plus sur la [convention de nommage suggérée pour les ID utilisateur]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web#naming-best-practices). |
| Braze user ID | Identifiant utilisateur Braze. |
| User alias | Un alias sert d'identifiant utilisateur unique alternatif. Utilisez les alias pour identifier les utilisateurs selon des dimensions différentes de votre ID utilisateur principal.<br><br>L'objet alias utilisateur est composé de deux parties : un `alias_name` pour l'identifiant lui-même et un `alias_label` indiquant le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des labels différents, mais un seul `alias_name` par `alias_label`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 4 : Créer une règle d'envoi d'événement" }

{% alert note %}
Pour associer l'événement à un utilisateur, vous devez renseigner soit le champ `External User ID`, soit le champ `Braze User Identifier`, soit la section `User Alias`.
{% endalert %}

{% endtab %}
{% tab Données d'événement %}

| Champ | Description | Obligatoire |
| --- | --- | --- |
| Event name | Nom de l'événement. | Oui |
| Event time | Date et heure sous forme de chaîne de caractères au format ISO 8601 ou `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. | Oui |
| App identifier | L'identifiant d'application ou `app_id` est un paramètre associant l'activité à une application spécifique dans votre espace de travail. Il désigne l'application avec laquelle vous interagissez au sein de l'espace de travail. | Non |
| Event Properties | Un objet JSON contenant les propriétés personnalisées de l'événement. | Non |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 4 : Créer une règle d'envoi d'événement" }

{% alert note %}
L'action **Braze Send Event** ne nécessite que la spécification d'un **Event Name** et d'un **Event Time**, mais vous devriez inclure autant d'informations que possible dans le champ des propriétés personnalisées. Consultez l'[objet événement]({{site.baseurl}}/api/objects_filters/event_object) pour plus de détails.
{% endalert %}

{% endtab %}
{% tab Attribut utilisateur %}

Les attributs utilisateur peuvent être un objet JSON contenant des champs qui créeront ou mettront à jour un attribut avec le nom et la valeur fournis sur le profil utilisateur spécifié. Les propriétés suivantes sont prises en charge :

| Attribut utilisateur | Description |
| --- | --- |
| First Name | Prénom de l'utilisateur. |
| Last Name | Nom de famille de l'utilisateur. |
| Phone | Numéro de téléphone de l'utilisateur. |
| Email | Adresse e-mail de l'utilisateur. |
| Gender | L'une des chaînes de caractères suivantes : "M", "F", "O" (autre), "N" (non applicable), "P" (préfère ne pas dire). |
| City | La ville de l'utilisateur. |
| Country | Le pays de l'utilisateur sous forme de chaîne de caractères au format [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). |
| Language | La langue de l'utilisateur sous forme de chaîne de caractères au format [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). |
| Date of Birth | La date de naissance de l'utilisateur sous forme de chaîne de caractères au format "YYYY-MM-DD" (par exemple, 1980-12-21). |
| Time Zone | Le nom du fuseau horaire issu de la base de données [IANA Time Zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (par exemple, 'America/New_York' ou 'Eastern Time (US & Canada)'). |
| Facebook | Un hash contenant l'un des éléments suivants : `id` (chaîne de caractères), `likes` (tableau de chaînes de caractères), `num_friends` (entier). |
| Twitter | Hash contenant l'un des éléments suivants : id (entier), `screen_name` (chaîne de caractères, identifiant X (anciennement Twitter)), `followers_count` (entier), `friends_count` (entier), `statuses_count` (entier). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 4 : Créer une règle d'envoi d'événement" }

{% alert note %}
Tous les attributs ajoutés dans la configuration seront envoyés à chaque fois que l'événement est envoyé à Braze, que la valeur de l'attribut ait changé ou non. Lors de la configuration des attributs utilisateur, assurez-vous de comprendre l'impact que cela aura sur votre consommation de points de donnée.
{% endalert %}

{% endtab %}
{% endtabs %}

### Étape 5 : Créer une règle d'envoi d'événement d'achat {#step-5-create-a-send-purchase-event-rule}

Après avoir installé l'extension, créez une nouvelle [règle](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) de transfert d'événements et configurez ses conditions selon vos besoins. Lors de la configuration des actions pour la règle, sélectionnez l'extension **Braze**, puis sélectionnez **Send Purchase Event** comme type d'action.

![Action de règle de transfert d'événements Adobe configurée pour utiliser Braze Send Purchase Event.]({% image_buster /assets/img/efe2.png %})

{% tabs local %}
{% tab Identification de l'utilisateur %}

| Champ | Description |
| --- | --- |
| External user ID | Un UUID ou GUID long, aléatoire et bien distribué. Si vous choisissez une autre méthode pour nommer vos ID utilisateur, ils doivent également être longs, aléatoires et bien distribués. En savoir plus sur la [convention de nommage suggérée pour les ID utilisateur]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web#naming-best-practices). |
| Braze user ID | Identifiant utilisateur Braze. |
| User alias | Un alias sert d'identifiant utilisateur unique alternatif. Utilisez les alias pour identifier les utilisateurs selon des dimensions différentes de votre ID utilisateur principal.<br><br>L'objet alias utilisateur est composé de deux parties : un `alias_name` pour l'identifiant lui-même et un `alias_label` indiquant le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des labels différents, mais un seul `alias_name` par `alias_label`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 5 : Créer une règle d'envoi d'événement d'achat" }

{% alert note %}
Pour associer l'événement à un utilisateur, vous devez renseigner soit le champ `External User ID`, soit le champ `Braze User Identifier`, soit la section `User Alias`.
{% endalert %}

{% endtab %}
{% tab Données d'achat %}

| Champ | Description | Obligatoire |
| --- | --- | --- |
| Product ID | Identifiant de l'achat. (par exemple, nom du produit ou catégorie du produit) | Oui |
| Purchase time | Date et heure sous forme de chaîne de caractères au format ISO 8601 ou `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. | Oui |
| Currency | Devise sous forme de chaîne de caractères au format de code alphabétique [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217). | Oui |
| Price | Le prix de l'objet. | Oui |
| Quantity | La quantité achetée. Si non fournie, la valeur par défaut sera 1. La valeur maximale doit être inférieure à 100. | Non |
| App identifier | L'identifiant d'application ou `app_id` est un paramètre associant l'activité à une application spécifique dans votre espace de travail. Il désigne l'application avec laquelle vous interagissez au sein de l'espace de travail. | Non |
| Purchase properties | Un objet JSON contenant les propriétés personnalisées de l'achat. | Non |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Étape 5 : Créer une règle d'envoi d'événement d'achat" }

{% alert note %}
L'action **Send Purchase Event** ne nécessite que la spécification d'un `Product ID`, d'un `Purchase Time`, d'une `Currency` et d'un `Price`, mais vous devriez inclure autant d'informations que possible dans le champ des propriétés d'achat. Consultez l'[objet achat]({{site.baseurl}}/api/objects_filters/purchase_object) pour plus de détails.
{% endalert %}

{% endtab %}
{% tab Attributs utilisateur %}

Vous pouvez choisir d'envoyer ou non des attributs avec chaque événement dans la vue de configuration.

Les attributs utilisateur peuvent être un objet JSON contenant des champs qui créeront ou mettront à jour un attribut avec le nom et la valeur fournis sur le profil utilisateur spécifié. Les propriétés suivantes sont prises en charge :

| Attribut utilisateur | Description |
| --- | --- |
| First name | Prénom de l'utilisateur. |
| Last name | Nom de famille de l'utilisateur. |
| Phone | Numéro de téléphone de l'utilisateur. |
| Email | Adresse e-mail de l'utilisateur. |
| Gender | L'une des chaînes de caractères suivantes : "M", "F", "O" (autre), "N" (non applicable), "P" (préfère ne pas dire). |
| City | La ville de l'utilisateur. |
| Country | Le pays de l'utilisateur sous forme de chaîne de caractères au format [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). |
| Language | La langue de l'utilisateur sous forme de chaîne de caractères au format [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). |
| Date of birth | La date de naissance de l'utilisateur sous forme de chaîne de caractères au format "YYYY-MM-DD" (par exemple, 1980-12-21). |
| Time zone | Le nom du fuseau horaire issu de la base de données [IANA Time Zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (par exemple, 'America/New_York' ou 'Eastern Time (US & Canada)'). |
| Facebook | Un hash contenant l'un des éléments suivants : `id` (chaîne de caractères), `likes` (tableau de chaînes de caractères), `num_friends` (entier). |
| Twitter | Hash contenant l'un des éléments suivants : id (entier), `screen_name` (chaîne de caractères, identifiant X (anciennement Twitter)), `followers_count` (entier), `friends_count` (entier), `statuses_count` (entier). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 5 : Créer une règle d'envoi d'événement d'achat" }

{% alert note %}
Tous les attributs ajoutés dans la configuration seront envoyés à chaque fois que l'événement est envoyé à Braze, que la valeur de l'attribut ait changé ou non. Lors de la configuration des attributs utilisateur, assurez-vous de comprendre l'impact que cela aura sur votre consommation de points de donnée.
{% endalert %}

{% endtab %}
{% endtabs %}

### Étape 6 : Valider les données dans Braze {#step-6-validate-data-within-braze}

Si la collecte d'événements et l'intégration avec Adobe Experience Platform ont réussi, vous verrez les événements dans la console Braze lors de la [consultation des profils utilisateur]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles). Plus précisément, les nouvelles données d'événement envoyées à Braze sont reflétées dans la section **Purchases** ou **Custom Events** de l'[onglet d'aperçu]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles#overview-tab) d'un utilisateur donné.