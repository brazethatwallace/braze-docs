---
nav_title: "Extension du transfert d'événements"
article_title: Adobe
description: "Cet article de référence décrit l'extension de transfert d'événements Braze qui vous permet d'exploiter les données capturées dans Adobe Experience Platform Edge Network et de les envoyer à Braze sous la forme d'événements côté serveur."
page_type: partner
page_order: 2
search_tag: Partner

---

# Extension de transfert d'événements de l'API Track Events {#track-events-api-event-forwarding-extension}

> L'extension de [transfert d'événements](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en) de l'API Track Events de Braze vous permet d'exploiter les données capturées dans Adobe Experience Platform Edge Network et de les envoyer à Braze sous la forme d'événements côté serveur à l'aide de l'API [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

Ce document décrit les cas d'utilisation de l'extension, comment l'installer dans vos bibliothèques de transfert d'événements et comment utiliser ses fonctionnalités dans une [règle](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) de transfert d'événements.

{% alert note %}
L'utilisation du transfert d'événements Adobe peut augmenter votre consommation de points de données Braze. Pour plus d'informations, reportez-vous à la documentation de Braze sur les [points de données]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#billable-data-points).
{% endalert %}

## Cas d'utilisation {#use-cases}

Cette extension doit utiliser les données du réseau Edge dans Braze pour tirer parti de ses capacités d'analyse et de ciblage des clients.

Prenons l'exemple d'une organisation de retail ayant une présence multicanal (site web et mobile) et capturant des entrées transactionnelles ou conversationnelles sous forme de données d'événement à partir de son site web et de ses plateformes mobiles.

À l'aide de diverses règles de [balises](https://experienceleague.adobe.com/docs/experience-platform/tags/home.html?lang=en), ces données sont envoyées en temps réel au réseau Edge. À partir de là, l'extension de transfert d'événements de Braze envoie automatiquement les événements pertinents à Braze depuis le serveur.

## Limites de débit {#rate-limits}

| API | Limites de débit |
| --- | --- |
| Suivi des utilisateurs | 50 000 requêtes par minute.<br><br>Reportez-vous à la [documentation de l'API de suivi des utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#rate-limit) pour plus de détails.
{: .reset-td-br-1 .reset-td-br-2 aria-label="Rate limits" }

## Intégration {#integration}

### Étape 1 : Rassembler les détails de configuration requis {#step-1-gather-required-configuration-details}

Pour connecter le réseau Edge à Braze, les éléments suivants sont nécessaires :

| Type de clé | Description |
| --- | --- |
| Instance de Braze | Votre instance Braze peut être obtenue auprès de votre gestionnaire d'onboarding Braze ou sur la [page d'aperçu de l'API]({{site.baseurl}}/api/basics/#endpoints). |
| Clé API REST de Braze | Une clé API REST Braze avec toutes les autorisations. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Settings** > **API Keys**.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 1: Gather required configuration details" }

### Étape 2 : Créer un secret {#step-2-create-a-secret}

Créez un nouveau [secret de transfert d'événements](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/secrets.html?lang=en) et définissez la valeur sur votre [clé API Braze](https://experienceleague.adobe.com/docs/experience-platform/tags/extensions/server/braze/overview.html?lang=en#configuration-details). Cela permet d'authentifier la connexion à votre compte tout en sécurisant la valeur.

### Étape 3 : Installer et configurer l'extension Braze {#step-3-install-and-configure-the-braze-extension}

1. Pour installer l'extension, [créez une propriété de transfert d'événements](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en#properties) ou choisissez une propriété existante à modifier.
2. Ensuite, sélectionnez **Extensions** dans la navigation de gauche. Dans l'onglet **Catalog**, sélectionnez **Install** sur la carte de l'extension Braze.
3. Sur l'écran suivant, saisissez votre instance REST et votre clé API, puis sélectionnez **Save** lorsque vous avez terminé.

### Étape 4 : Créer une règle d'envoi d'événement {#step-4-create-a-send-event-rule}

Après avoir installé l'extension, créez une nouvelle [règle](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) de transfert d'événements et configurez ses conditions comme vous le souhaitez. Lors de la configuration des actions pour la règle, sélectionnez l'extension **Braze**, puis sélectionnez **Send Event** pour le type d'action.

![]({% image_buster /assets/img/efe.png %})

{% tabs local %}
{% tab User Identification %}

| Entrée | Description |
| --- | --- |
| ID d'utilisateur externe | Un UUID ou GUID long, aléatoire et bien distribué. Si vous choisissez une autre méthode pour nommer vos ID d'utilisateur, ils doivent également être longs, aléatoires et bien répartis. En savoir plus sur la [convention de dénomination suggérée pour les ID d'utilisateurs]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#suggested-user-id-naming-convention). |
| ID utilisateur Braze | Identifiant de l'utilisateur Braze. |
| Alias d'utilisateur | Un alias sert d'identifiant unique alternatif pour l'utilisateur. Utilisez des alias pour identifier les utilisateurs selon d'autres dimensions que votre ID d'utilisateur principal.<br><br>L'objet alias d'utilisateur se compose de deux parties : un `alias_name` pour l'identifiant lui-même et un `alias_label` indiquant le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des libellés différents, mais un seul `alias_name` par `alias_label`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 4: Create a send event rule" }

{% alert note %}
Pour lier l'événement à un utilisateur, vous devez remplir soit le champ `External User ID`, soit le champ `Braze User Identifier`, soit la section `User Alias`.
{% endalert %}

{% endtab %}
{% tab Event Data %}

| Entrée | Description | Requis |
| --- | --- | --- |
| Nom de l'événement | Nom de l'événement. | Oui |
| Heure de l'événement | Date-heure sous forme de chaîne de caractères au format ISO 8601 ou `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. | Oui |
| Identifiant de l'application | L'identifiant de l'application ou `app_id` est un paramètre qui associe l'activité à une application spécifique dans votre espace de travail. Il désigne l'application avec laquelle vous interagissez au sein de l'espace de travail. | Non |
| Propriétés d'événement | Un objet JSON contenant les propriétés personnalisées de l'événement. | Non |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 4: Create a send event rule" }

{% alert note %}
L'action **Braze Send Event** ne requiert que la spécification d'un **Event Name** et d'un **Event Time**, mais vous devriez inclure autant d'informations que possible dans le champ des propriétés personnalisées. Reportez-vous à l'[objet événement]({{site.baseurl}}/api/objects_filters/event_object/) pour plus de détails.
{% endalert %}

{% endtab %}
{% tab User Attribute %}

Les attributs utilisateur peuvent être un objet JSON contenant des champs qui créeront ou mettront à jour un attribut avec le nom et la valeur fournis sur le profil utilisateur spécifié. Les propriétés suivantes sont prises en charge :

| Attribut utilisateur | Description |
| --- | --- |
| Prénom | Prénom de l'utilisateur. |
| Nom de famille | Nom de famille de l'utilisateur. |
| Téléphone | Numéro de téléphone de l'utilisateur. |
| E-mail | Adresse e-mail de l'utilisateur. |
| Genre | Une des chaînes de caractères suivantes : « M », « F », « O » (autre), « N » (sans objet), « P » (préfère ne pas se prononcer). |
| Ville | La ville de l'utilisateur. |
| Pays | Le pays de l'utilisateur sous forme de chaîne de caractères au format [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). |
| Langue | La langue de l'utilisateur sous forme de chaîne de caractères au format [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). |
| Date de naissance | La date de naissance de l'utilisateur sous forme de chaîne de caractères au format « AAAA-MM-JJ » (par exemple, 1980-12-21). |
| Fuseau horaire | Nom du fuseau horaire de la base de données [IANA Time Zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (par exemple, 'America/New_York' ou 'Eastern Time (US & Canada)'). |
| Facebook | Un hachage contenant l'un des éléments suivants : `id` (chaîne de caractères), `likes` (tableau de chaînes de caractères), `num_friends` (nombre entier). |
| Twitter | Un hachage contenant l'un des éléments suivants : id (nombre entier), `screen_name` (chaîne de caractères, identifiant X (anciennement Twitter)), `followers_count` (nombre entier), `friends_count` (nombre entier), `statuses_count` (nombre entier). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 4: Create a send event rule" }

{% alert note %}
Tous les attributs ajoutés dans la configuration seront envoyés à chaque fois que l'événement est envoyé à Braze, que la valeur de l'attribut ait changé ou non. Lorsque vous configurez les attributs utilisateur, assurez-vous de savoir comment cela affectera votre consommation de points de données.
{% endalert %}

{% endtab %}
{% endtabs %}

### Étape 5 : Créer une règle d'envoi d'événement d'achat {#step-5-create-a-send-purchase-event-rule}

Après avoir installé l'extension, créez une nouvelle [règle](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) de transfert d'événements et configurez ses conditions comme vous le souhaitez. Lors de la configuration des actions pour la règle, sélectionnez l'extension **Braze**, puis sélectionnez **Send Purchase Event** pour le type d'action.

![]({% image_buster /assets/img/efe2.png %})

{% tabs local %}
{% tab User Identification %}

| Entrée | Description |
| --- | --- |
| ID d'utilisateur externe | Un UUID ou GUID long, aléatoire et bien distribué. Si vous choisissez une autre méthode pour nommer vos ID d'utilisateur, ils doivent également être longs, aléatoires et bien répartis. En savoir plus sur la [convention de dénomination suggérée pour les ID d'utilisateurs]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#suggested-user-id-naming-convention). |
| ID utilisateur Braze | Identifiant de l'utilisateur Braze. |
| Alias d'utilisateur | Un alias sert d'identifiant unique alternatif pour l'utilisateur. Utilisez des alias pour identifier les utilisateurs selon d'autres dimensions que votre ID d'utilisateur principal.<br><br>L'objet alias d'utilisateur se compose de deux parties : un `alias_name` pour l'identifiant lui-même et un `alias_label` indiquant le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des libellés différents, mais un seul `alias_name` par `alias_label`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 5: Create a send purchase event rule" }

{% alert note %}
Pour lier l'événement à un utilisateur, vous devez remplir soit le champ `External User ID`, soit le champ `Braze User Identifier`, soit la section `User Alias`.
{% endalert %}

{% endtab %}
{% tab Purchase Data %}

| Entrée | Description | Requis |
| --- | --- | --- |
| ID du produit | Identifiant de l'achat (par exemple, le nom du produit ou la catégorie du produit). | Oui |
| Heure de l'achat | Date-heure sous forme de chaîne de caractères au format ISO 8601 ou `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. | Oui |
| Devise | Devise sous forme de chaîne de caractères au format du code alphabétique de la devise [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217). | Oui |
| Prix | Le prix de l'objet. | Oui |
| Quantité | La quantité achetée. Si elle n'est pas fournie, la valeur par défaut est 1. La valeur maximale doit être inférieure à 100. | Non |
| Identifiant de l'application | L'identifiant de l'application ou `app_id` est un paramètre qui associe l'activité à une application spécifique dans votre espace de travail. Il désigne l'application avec laquelle vous interagissez au sein de l'espace de travail. | Non |
| Propriétés d'achat | Un objet JSON contenant les propriétés personnalisées de l'achat. | Non |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Step 5: Create a send purchase event rule" }

{% alert note %}
L'action **Send Purchase Event** ne nécessite que la spécification des paramètres `Product ID`, `Purchase Time`, `Currency` et `Price`, mais vous devriez inclure autant d'informations que possible dans le champ des propriétés d'achat. Reportez-vous à l'[objet achat]({{site.baseurl}}/api/objects_filters/purchase_object/) pour plus de détails.
{% endalert %}

{% endtab %}
{% tab User Attributes %}

Vous pouvez choisir d'envoyer ou non des attributs avec chaque événement dans la vue de configuration.

Les attributs utilisateur peuvent être un objet JSON contenant des champs qui créeront ou mettront à jour un attribut avec le nom et la valeur fournis sur le profil utilisateur spécifié. Les propriétés suivantes sont prises en charge :

| Attribut utilisateur | Description |
| --- | --- |
| Prénom | Prénom de l'utilisateur. |
| Nom de famille | Nom de famille de l'utilisateur. |
| Téléphone | Numéro de téléphone de l'utilisateur. |
| E-mail | Adresse e-mail de l'utilisateur. |
| Genre | Une des chaînes de caractères suivantes : « M », « F », « O » (autre), « N » (sans objet), « P » (préfère ne pas se prononcer). |
| Ville | La ville de l'utilisateur. |
| Pays | Le pays de l'utilisateur sous forme de chaîne de caractères au format [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). |
| Langue | La langue de l'utilisateur sous forme de chaîne de caractères au format [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). |
| Date de naissance | La date de naissance de l'utilisateur sous forme de chaîne de caractères au format « AAAA-MM-JJ » (par exemple, 1980-12-21). |
| Fuseau horaire | Nom du fuseau horaire de la base de données [IANA Time Zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (par exemple, 'America/New_York' ou 'Eastern Time (US & Canada)'). |
| Facebook | Un hachage contenant l'un des éléments suivants : `id` (chaîne de caractères), `likes` (tableau de chaînes de caractères), `num_friends` (nombre entier). |
| Twitter | Un hachage contenant l'un des éléments suivants : id (nombre entier), `screen_name` (chaîne de caractères, identifiant X (anciennement Twitter)), `followers_count` (nombre entier), `friends_count` (nombre entier), `statuses_count` (nombre entier). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 5: Create a send purchase event rule" }

{% alert note %}
Tous les attributs ajoutés dans la configuration seront envoyés à chaque fois que l'événement est envoyé à Braze, que la valeur de l'attribut ait changé ou non. Lorsque vous configurez les attributs utilisateur, assurez-vous de savoir comment cela affectera votre consommation de points de données.
{% endalert %}

{% endtab %}
{% endtabs %}

### Étape 6 : Valider les données dans Braze {#step-6-validate-data-within-braze}

Si la collecte des événements et l'intégration d'Adobe Experience Platform ont réussi, vous verrez les événements dans la console Braze lorsque vous [consulterez les profils utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/). Plus précisément, les nouvelles données d'événement envoyées à Braze sont reflétées dans la section **Purchases** ou **Custom Events** de l'[onglet d'aperçu]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#overview-tab) d'un utilisateur particulier.