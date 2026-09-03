---
nav_title: "Objet Attributs d'utilisateur"
article_title: "Objet Attributs d'utilisateur"
page_order: 11
page_type: reference
description: "Cet article de référence explique les différents composants de l'objet Attributs d'utilisateur."
---

# Objet Attributs d'utilisateur {#user-attributes-object}

> Une requête API contenant des champs dans l'objet attributes crée ou met à jour un attribut de ce nom avec la valeur indiquée dans le profil utilisateur spécifié.

Utilisez les noms de champs de profil utilisateur Braze (énumérés ci-après ou tout autre répertorié dans la section [Champs de profil utilisateur Braze](#braze-user-profile-fields)) pour mettre à jour ces valeurs spéciales sur le profil utilisateur dans le tableau de bord, ou ajoutez vos propres données d'attributs personnalisés à l'utilisateur.

## Corps de l'objet {#object-body}

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
  "external_id" : (optional, string) see external user ID,
  "user_alias" : (optional, User alias object),
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  // Setting this flag to true puts the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" defaults to true.
  "_update_existing_only" : (optional, boolean),
  // See note regarding anonymous push token imports
  "push_token_import" : (optional, boolean),
  // Braze User Profile Fields
  "first_name" : "Alex",
  "email" : "bob@example.com",
  // Custom Attributes
  "my_custom_attribute" : value,
  "my_custom_attribute_2" : {"inc" : int_value},
  "my_array_custom_attribute":[ "Value1", "Value2" ],
  // Adding a new value to an array custom attribute
  "my_array_custom_attribute" : { "add" : ["Value3"] },
  // Removing a value from an array custom attribute
  "my_array_custom_attribute" : { "remove" : [ "Value1" ]},
  // Array of objects custom attribute
  "my_array_of_objects_attribute": [{"key": "value"}, {"key": "value"}],
  // Adding to an array of objects (nested custom attribute syntax)
  "my_array_of_objects_attribute": { "$add": [{"key": "value"}] },
  // Removing from an array of objects (nested custom attribute syntax)
  "my_array_of_objects_attribute": { "$remove": [{"$identifier_key": "key", "$identifier_value": "value"}] },
}
```

- [ID externe]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)
- [Alias d'utilisateur]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)

{% alert note %}
Pour les attributs personnalisés de type tableau classique, utilisez `add` et `remove` (sans `$`).

Pour les tableaux d'objets (attributs personnalisés imbriqués), utilisez `$add`, `$remove` et `$update` dans les payloads de requête `/users/track`. Ces opérateurs appliquent des modifications au niveau de l'objet en faisant correspondre des identifiants (`$identifier_key` et `$identifier_value`) et prennent en charge les mises à jour sur place avec `$new_object`.

Utilisez ce format lorsque vous devez ajouter, supprimer ou mettre à jour des objets à l'intérieur d'un tableau existant tout en préservant le reste de l'état du tableau. Pour des exemples de requêtes complets, consultez [Exemple d'API pour les tableaux d'objets]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#api-example) et [Exemple SDK pour les tableaux d'objets]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#sdk-example).
{% endalert %}

Pour supprimer un attribut de profil, définissez-le sur `null`. Certains champs, comme `external_id` et `user_alias`, ne peuvent pas être supprimés une fois ajoutés à un profil utilisateur.

### Résolution des identifiants {#identifier-resolution}

Sauf si vous effectuez une [importation anonyme de jetons push](#push-token-import), chaque objet d'attributs utilisateur doit contenir au moins un identifiant : `external_id`, `user_alias`, `braze_id`, `email` ou `phone`. Dans la mesure du possible, incluez un seul identifiant par objet afin d'éviter toute ambiguïté quant au profil utilisateur mis à jour ou créé.

Gardez les points suivants à l'esprit lors de l'utilisation des identifiants :

- **`external_id` et `user_alias` sont mutuellement exclusifs.** Inclure les deux dans le même objet d'attributs utilisateur renvoie une erreur. Pour ajouter un alias à un utilisateur qui possède déjà un `external_id`, utilisez l'[endpoint `/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias).
- **`email` a la priorité sur `phone`.** Si `email` et `phone` sont tous deux inclus dans le même objet, Braze utilise `email` comme identifiant. Cela signifie que les attributs sont appliqués au profil utilisateur associé à cette adresse e-mail, même si le numéro de téléphone appartient à un profil différent.

{% alert important %}
Pour éviter tout comportement inattendu, utilisez un seul identifiant par objet d'attributs utilisateur. Fournir plusieurs identifiants qui référencent des profils utilisateur différents peut entraîner l'application d'attributs au mauvais profil.
{% endalert %}

#### Mettre à jour uniquement les profils existants {#update-existing-profiles-only}

Si vous souhaitez mettre à jour uniquement les profils utilisateur existants dans Braze, vous devez passer la clé `_update_existing_only` avec la valeur `true` dans le corps de votre requête. Si cette valeur est omise, Braze crée un nouveau profil utilisateur si l'`external_id` n'existe pas déjà.

{% alert note %}
Si vous créez un profil utilisateur de type alias uniquement via l'endpoint `/users/track`, vous devez définir `_update_existing_only` sur `false`. Si vous omettez cette valeur, Braze ne crée pas le profil de type alias uniquement.
{% endalert %}

#### Importation de jetons push {#push-token-import}

Avant d'importer des jetons push vers Braze, vérifiez bien si cela est nécessaire. Lorsque les SDK Braze sont mis en place, ils gèrent les jetons push automatiquement sans qu'il soit nécessaire de les télécharger via l'API.

Si vous estimez devoir les télécharger via l'API, ils peuvent être téléchargés pour des utilisateurs identifiés ou des utilisateurs anonymes. Cela signifie qu'un `external_id` doit être présent, ou que les utilisateurs anonymes doivent avoir le flag `push_token_import` défini sur `true`.

{% alert note %}
Lors de l'importation de jetons push depuis d'autres systèmes, un `external_id` n'est pas toujours disponible. Pour maintenir la communication avec ces utilisateurs pendant votre transition vers Braze, vous pouvez importer les jetons historiques pour les utilisateurs anonymes sans fournir d'`external_id` en spécifiant `push_token_import` comme `true`.
{% endalert %}

Lorsque vous spécifiez `push_token_import` comme `true` :

* `external_id` et `braze_id` ne doivent **pas** être spécifiés
* L'objet d'attribut **doit** contenir un jeton push
* Si le jeton existe déjà dans Braze, la requête est ignorée ; sinon, Braze crée un profil utilisateur temporaire et anonyme pour chaque jeton afin de vous permettre de continuer à envoyer des messages à ces personnes

Après l'importation, lorsque chaque utilisateur lance la version de votre application compatible avec Braze, Braze déplace automatiquement son jeton push importé vers son profil utilisateur Braze et nettoie le profil temporaire.

Braze vérifie une fois par mois s'il existe un profil anonyme avec le flag `push_token_import` qui ne possède pas de jeton push. Si le profil anonyme n'a plus de jeton push, Braze supprime le profil. Cependant, si le profil anonyme possède encore un jeton push, ce qui suggère que l'utilisateur réel ne s'est pas encore connecté à l'appareil avec ce jeton push, Braze ne fait rien.

Pour plus d'informations, consultez [Migration des jetons push](#migrate-push-tokens).

#### Types de données des attributs personnalisés {#custom-attribute-data-types}

Les types de données suivants peuvent être stockés en tant qu'attribut personnalisé :

| Type de données | Notes |
| --- | --- |
| Tableaux | Les tableaux d'attributs personnalisés sont pris en charge. Lorsque vous ajoutez un élément, il est ajouté à la fin du tableau. Si l'élément existe déjà, il est déplacé de sa position actuelle vers la fin.<br><br>Seules les valeurs uniques sont stockées. Par exemple, l'importation de `['hotdog','hotdog','hotdog','pizza']` donne `['hotdog', 'pizza']`.<br><br>Vous pouvez définir un tableau directement (par exemple, `"my_array_custom_attribute":[ "Value1", "Value2" ]`), ajouter à un tableau existant avec `"my_array_custom_attribute" : { "add" : ["Value3"] }`, ou supprimer des valeurs avec `"my_array_custom_attribute" : { "remove" : [ "Value1" ]}`.<br><br>Le nombre d'éléments par défaut et maximum dans un tableau est de 500. Vous pouvez mettre à jour le nombre maximum de tableaux dans le tableau de bord de Braze, sous **Data Settings** > **Custom Attributes**. Pour plus d'informations, consultez [Tableaux]({{site.baseurl}}/developer_guide/analytics#arrays). |
| Tableaux d'objets | Utilisez un tableau d'objets pour définir une liste d'objets où chaque objet contient un ensemble d'attributs. Ce type permet de stocker plusieurs ensembles de données liées pour un utilisateur, comme des séjours à l'hôtel, un historique d'achats ou des préférences. <br><br>Par exemple, définissez un attribut personnalisé nommé `hotel_stays` sur un profil utilisateur sous forme de tableau où chaque objet représente un séjour distinct, avec des attributs comme `hotel_name`, `check_in_date` et `nights_stayed`.<br><br>Les tableaux d'objets n'ont pas de limite sur le nombre d'éléments, mais ont une taille maximale de 100&nbsp;Ko. Si une mise à jour provoque le dépassement de cette limite par le tableau, Braze rejette la mise à jour et l'attribut reste inchangé.<br><br>Pour les payloads `/users/track` et SDK, utilisez `$add`, `$remove` et `$update` pour les opérations sur les tableaux d'objets. Utilisez `add` et `remove` (sans `$`) pour les attributs personnalisés de type tableau classique contenant des valeurs scalaires. Pour plus de détails, consultez [Exemple d'API pour les tableaux d'objets]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#api-example), [Exemple SDK pour les tableaux d'objets]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#sdk-example) et [Exemple de tableau d'objets](#array-of-objects-example). |
| Booléens | `true` ou `false` |
| Dates | Stockez les dates au format [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) (recommandé) ou dans l'un des formats suivants : <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>Notez que « T » est un indicateur de temps, pas un espace réservé, et ne doit pas être modifié ou supprimé. <br><br>Les valeurs de date qui ne correspondent à aucun des formats répertoriés sont stockées sous forme de chaînes de caractères sur le profil utilisateur au lieu du type de données Time. Cela signifie que les filtres de segmentation temporels (tels que « avant », « après » ou « au cours des X derniers jours ») ne fonctionnent pas pour ces attributs. Par exemple, `Mar 26 2026 06:12 PM +00:00` est stocké en tant que chaîne de caractères car il ne correspond pas à un format pris en charge. Pour éviter cela, utilisez le format ISO 8601 (par exemple, `2026-03-26T18:12:00Z`). <br><br>Les attributs temporels sans fuseau horaire adoptent par défaut minuit UTC (et sont formatés dans le tableau de bord comme l'équivalent de minuit UTC dans le fuseau horaire de l'entreprise). Pour spécifier un fuseau horaire, ajoutez un décalage UTC à l'horodatage (par exemple, `2024-11-10T18:00:00-05:00` pour EST). Si le décalage du fuseau horaire est manquant ou mal formaté, la valeur adopte par défaut UTC. <br><br>Les heures sont affichées dans le tableau de bord dans le fuseau horaire de votre entreprise. Par exemple, `2024-11-10T18:00:00-05:00` (18 h 00 EST) apparaîtrait comme l'heure équivalente dans le fuseau horaire configuré de votre entreprise. <br><br>Les événements avec des horodatages dans le futur adoptent par défaut l'heure actuelle. <br><br>Pour les attributs personnalisés classiques, si l'année est inférieure à 0 ou supérieure à 3000, Braze stocke la valeur en tant que chaîne de caractères sur le profil utilisateur. |
| Floats | Les attributs personnalisés de type float sont des nombres positifs ou négatifs avec une virgule décimale. Par exemple, vous pouvez utiliser les floats pour stocker des soldes de comptes ou des notes utilisateur pour des produits ou services. |
| Entiers | Vous pouvez incrémenter les attributs personnalisés de type entier en assignant un objet avec le champ « inc » et le montant à ajouter. <br><br>Exemple : `"my_custom_attribute_2" : {"inc" : int_value},`|
| Attributs personnalisés imbriqués | Les attributs personnalisés imbriqués définissent un ensemble d'attributs comme propriété d'un autre attribut. Lorsque vous définissez un objet d'attribut personnalisé, vous ajoutez un ensemble d'attributs à cet objet. Pour plus d'informations, consultez [Attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support). |
| Chaînes de caractères | Les attributs personnalisés de type chaîne de caractères sont des séquences de caractères utilisées pour stocker des données textuelles. Par exemple, vous pouvez utiliser des chaînes de caractères pour stocker les prénoms et noms, les adresses e-mail ou les préférences. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Types de données des attributs personnalisés" }

{% alert tip %}
Pour savoir quand utiliser un événement personnalisé plutôt qu'un attribut personnalisé, consultez [Événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events) et [Attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes).
{% endalert %}

##### Exemple de tableau d'objets {#array-of-objects-example}

Ce tableau d'objets vous permet de créer des Segments basés sur des critères spécifiques au sein des séjours, et de personnaliser vos messages en utilisant les données de chaque séjour avec les modèles Liquid.

```json
{"hotel_stays": [
  { "hotel_name": "Ocean View Resort", "check_in_date": "2023-06-15", "nights_stayed": 5 },
  { "hotel_name": "Mountain Lodge", "check_in_date": "2023-09-10", "nights_stayed": 3 }
]}
```

Pour des exemples de tableaux d'objets utilisant `$add`, `$remove` et `$update`, consultez [Exemple d'API pour les tableaux d'objets]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#api-example) et [Exemple SDK pour les tableaux d'objets]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects#sdk-example).

#### Champs du profil utilisateur Braze {#braze-user-profile-fields}

{% alert important %}
Les champs de profil utilisateur suivants sont sensibles à la casse, assurez-vous donc de les référencer en minuscules.
{% endalert %}

{% alert tip %}
Pour une référence destinée aux clients sur les attributs standard, organisée par catégorie et incluant des recommandations pour le SDK, l'API, le CSV et l'ingestion de données cloud, consultez [Attributs standard]({{site.baseurl}}/user_guide/data/activation/attributes/standard_attributes).
{% endalert %}

| Champ du profil utilisateur | Spécification du type de données |
| ---| --- |
| alias_name | (string) |
| alias_label | (string) |
| braze_id | (string, facultatif) Lorsqu'un profil utilisateur est reconnu par le SDK, un profil utilisateur anonyme est créé avec un `braze_id` associé. Le `braze_id` est automatiquement attribué par Braze, ne peut pas être modifié et est spécifique à l'appareil. |
| country | (string) Les codes pays doivent être transmis à Braze selon la norme [ISO-3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1). Notre API fait de son mieux pour mapper les pays reçus dans différents formats. Par exemple, « Australia » peut être mappé sur « AU ». Cependant, si la valeur saisie ne correspond pas à une norme [ISO-3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1) donnée, la valeur du pays est définie sur `NULL`. <br><br>Définir `country` sur un utilisateur par importation CSV ou API empêche Braze de capturer automatiquement cette information via le SDK. |
| current_location | (object) De la forme {"longitude": -73.991443, "latitude": 40.753824} |
| date_of_first_session | (date à laquelle l'utilisateur a utilisé l'application pour la première fois) Chaîne de caractères au format ISO 8601 ou dans l'un des formats suivants : <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| date_of_last_session | (date à laquelle l'utilisateur a utilisé l'application pour la dernière fois) Chaîne de caractères au format ISO 8601 ou dans l'un des formats suivants : <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY`  |
| dob | (date de naissance) Chaîne de caractères au format « YYYY-MM-DD », par exemple 1980-12-21. |
| email | (string) |
| email_subscribe | (string) Les valeurs disponibles sont « opted_in » (inscription explicite à la réception d'e-mails), « unsubscribed » (désabonnement explicite des e-mails) et « subscribed » (ni inscrit ni désabonné).  |
| email_open_tracking_disabled |(boolean) `true` ou `false` accepté. Définissez sur `true` pour désactiver l'ajout du pixel de suivi d'ouverture à tous les futurs e-mails envoyés à cet utilisateur.|
| email_click_tracking_disabled |(boolean) `true` ou `false` accepté. Définissez sur `true` pour désactiver le suivi des clics pour tous les liens dans un futur e-mail envoyé à cet utilisateur.|
| external_id | (string) Un identifiant unique pour un profil utilisateur. Une fois un `external_id` attribué, Braze identifie le profil utilisateur sur l'ensemble des appareils de l'utilisateur. Lors de la première attribution d'un external_id à un profil utilisateur inconnu, Braze migre toutes les données du profil utilisateur existant vers le nouveau profil utilisateur. |
| facebook | Hash contenant l'un des éléments suivants : `id` (string), `likes` (tableau de chaînes de caractères), `num_friends` (entier). |
| first_name | (string) |
| gender | (string) « M », « F », « O » (autre), « N » (non applicable), « P » (préfère ne pas dire) ou null (inconnu). |
| home_city | (string) |
| language | (string) La langue doit être transmise à Braze selon la norme [ISO-639-1](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). Pour les langues prises en charge, consultez notre [liste des langues acceptées]({{site.baseurl}}/user_guide/data/unification/user_data/language_codes).<br><br>Définir `language` sur un utilisateur par importation CSV ou API empêche Braze de capturer automatiquement cette information via le SDK. |
| last_name | (string) |
| marked_email_as_spam_at | (string) Date à laquelle l'e-mail de l'utilisateur a été marqué comme spam. Apparaît au format ISO 8601 ou dans l'un des formats suivants : <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| phone | (string) Nous recommandons de fournir les numéros de téléphone au format [E.164](https://en.wikipedia.org/wiki/E.164). Pour plus de détails, consultez [Numéros de téléphone des utilisateurs]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#recommended-format).|
| push_subscribe | (string) Les valeurs disponibles sont « opted_in » (inscription explicite à la réception de notifications push), « unsubscribed » (désabonnement explicite des notifications push) et « subscribed » (ni inscrit ni désabonné).  |
| push_tokens | Tableau d'objets avec les chaînes `app_id` et `token`. Vous pouvez éventuellement fournir un `device_id` pour l'appareil auquel ce jeton est associé, par exemple `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`. Si aucun `device_id` n'est fourni, un identifiant est généré aléatoirement. |
| subscription_groups| Tableau d'objets avec les chaînes `subscription_group_id` et `subscription_state`, par exemple `[{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]`. Les valeurs disponibles pour `subscription_state` sont « subscribed » et « unsubscribed ».|
| time_zone | (string) Nom du fuseau horaire de la [base de données de fuseaux horaires IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (par exemple, « America/New_York » ou « Eastern Time (US & Canada) »). Seules les valeurs de fuseau horaire valides sont définies. |
| twitter | Hash contenant l'un des éléments suivants : `id` (entier), `screen_name` (string, identifiant X (anciennement Twitter)), `followers_count` (entier), `friends_count` (entier), `statuses_count` (entier). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Champs du profil utilisateur Braze" }

Les valeurs de langue définies explicitement via cette API ont la priorité sur les informations de localisation que Braze reçoit automatiquement de l'appareil.

####  Exemple de requête d'attributs utilisateur {#user-attribute-example-request}

Cet exemple contient quatre objets d'attributs utilisateur, sur un total de 75 objets d'attributs autorisés par appel API.

```http
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes" : [
    {
      "external_id" : "user1",
      "first_name" : "Alex",
      "has_profile_picture" : true,
      "dob": "1988-02-14",
      "music_videos_favorited" : { "add" : [ "calvinharris-summer" ], "remove" : ["nickiminaj-anaconda"] }
    },
    {
      "external_id" : "user2",
      "first_name" : "Lee",
      "has_profile_picture" : false,
      "push_tokens": [{"app_id": "Your App Identifier", "token": "abcd", "device_id": "optional_field_value"}]

    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "first_name" : "Yuri",
      "has_profile_picture" : false
    },
    {
      "external_id": "user3",
      "subscription_groups" : [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]
    }
  ]
}
```

## Migrer les jetons push {#migrate-push-tokens}

Si vous envoyiez des notifications push avant d'intégrer Braze, que ce soit par vos propres moyens ou via un autre fournisseur, la migration des jetons push vous permet de continuer à envoyer des notifications push à vos utilisateurs disposant de jetons push enregistrés.

### Migration automatique via le SDK {#automatic-migration-through-sdk}

Après avoir [intégré le SDK Braze]({{site.baseurl}}/developer_guide/sdk_integration), les jetons push de vos utilisateurs ayant accepté les notifications sont automatiquement migrés lors de leur prochaine ouverture de votre application. Jusqu'alors, vous ne pouvez pas envoyer de notifications push à ces utilisateurs via Braze.

Vous pouvez également [migrer vos jetons push manuellement](#manual-migration-through-api), ce qui vous permet de réengager vos utilisateurs plus rapidement.

#### Considérations relatives aux jetons web {#web-token-considerations}

En raison de la nature des jetons push web, tenez compte des éléments suivants lors de l'implémentation du push pour le web :

|Considération|Détails|
|----------------------|------------|
| **Services de traitement** | Par défaut, le SDK Web recherche un service de traitement à l'emplacement `./service-worker`, sauf si une autre option est spécifiée, comme `manageServiceWorkerExternally` ou `serviceWorkerLocation`. Si votre service de traitement n'est pas correctement configuré, cela peut entraîner l'expiration des jetons push de vos utilisateurs. |
| **Jetons expirés** | Si un utilisateur n'a pas démarré de session web dans les 60 jours, son jeton push expire. Comme Braze ne peut pas migrer les jetons push expirés, vous devez envoyer un [push primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) pour les réengager. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Considérations relatives aux jetons web" }

### Migration manuelle via l'API {#manual-migration-through-api}

La migration manuelle des jetons push consiste à importer ces clés précédemment créées dans votre plateforme Braze via l'API.

Migrez de manière programmatique les jetons iOS (APNs) et Android (FCM) vers votre plateforme en utilisant l'[endpoint `users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Vous pouvez migrer aussi bien les utilisateurs identifiés (utilisateurs associés à un ID externe) que les utilisateurs anonymes (utilisateurs sans ID externe).

Spécifiez l'`app_id` de votre application lors de la migration des jetons push pour associer le jeton push approprié à l'application correspondante. Chaque application (iOS, Android, etc.) dispose de son propre `app_id`, que vous pouvez trouver dans la section **Identification** de la page [Clés API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers). Veillez à utiliser l'`app_id` de la plateforme correcte.

{% alert important %}
Il n'est pas possible de migrer les jetons push web via l'API. En effet, les jetons push web ne respectent pas le même schéma que les autres plateformes.

<br>Si vous tentez de migrer des jetons push web de manière programmatique, vous pourriez voir une erreur semblable à la suivante : `Received '400: Invalid subscription auth' sending to 'https://fcm.googleapis.com/fcm/send`

<br>
Comme alternative à la migration par API, nous vous recommandons d'intégrer le SDK et de laisser votre base de jetons se reconstituer naturellement.
{% endalert %}

{% tabs local %}
{% tab ID externe présent %}
Pour les utilisateurs identifiés, définissez l'indicateur `push_token_import` sur `false` (ou omettez le paramètre) et spécifiez les valeurs `external_id`, `app_id` et `token` dans l'objet `attributes` de l'utilisateur.

Par exemple :

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes" : [
    {
      "push_token_import" : false,
      "external_id": "example_external_id",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING"}
      ]
    }
  ]
}'
```
{% endtab %}

{% tab ID externe absent %}
Lors de l'importation de jetons push depuis d'autres systèmes, un `external_id` n'est pas toujours disponible. Dans ce cas, définissez votre indicateur `push_token_import` sur `true` et spécifiez les valeurs `app_id` et `token`. Braze crée un profil utilisateur temporaire et anonyme pour chaque jeton afin de vous permettre de continuer à envoyer des messages à ces personnes. Si le jeton existe déjà dans Braze, la requête est ignorée.

Par exemple :

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes": [
    {
      "push_token_import" : true,
      "email": "braze.test1@example.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
      ]
    },

    {
      "push_token_import" : true,
      "email": "braze.test2@example.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE_1": "YOUR_VALUE",
      "YOUR_CUSTOM_ATTRIBUTE_2": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
      ]
    }
  ]
}'
```

Après l'importation, lorsque l'utilisateur anonyme lance la version de votre application intégrant Braze, Braze transfère automatiquement le jeton push importé vers le profil utilisateur Braze de cet utilisateur et supprime le profil temporaire.

Braze vérifie une fois par mois s'il existe des profils anonymes avec l'indicateur `push_token_import` qui ne possèdent plus de jeton push. Si le profil anonyme n'a plus de jeton push, Braze supprime le profil. Cependant, si le profil anonyme possède toujours un jeton push, ce qui suggère que l'utilisateur réel ne s'est pas encore connecté à l'appareil avec ce jeton push, Braze ne prend aucune mesure.
{% endtab %}
{% endtabs %}

### Importer des jetons push iOS {#import-ios-push-tokens}

Lors de la migration de jetons push iOS avec `/users/track`, le champ `gateway` n'est pas défini sur le jeton push. Braze suppose que les jetons importés via l'API sont des jetons push de premier plan valides, mais ne peut pas déterminer à quel environnement APNs le jeton appartient.

Sans le champ gateway, Braze utilise le paramètre d'environnement de secours configuré pour votre application lors de l'envoi de notifications push. Cela peut entraîner des erreurs `BadDeviceToken` si l'environnement réel du jeton diffère du paramètre de secours configuré. Par exemple, un jeton de développement envoyé via le gateway de production échouera.

Pour éviter les problèmes de distribution :

- Assurez-vous que le paramètre d'environnement de votre application dans le tableau de bord de Braze correspond aux jetons que vous importez.
- Pour les applications en production, importez uniquement les jetons de production.
- Pour les environnements de test, vérifiez que la configuration de votre application et les jetons importés utilisent l'environnement de développement.

{% alert note %}
Les jetons enregistrés via le SDK Braze incluent automatiquement le champ gateway, car le SDK détecte l'environnement à partir des droits de votre application.
{% endalert %}

### Importer des jetons push Android {#import-android-push-tokens}

{% alert important %}
La considération suivante s'applique uniquement aux applications Android. Les applications iOS ne nécessitent pas ces étapes car cette plateforme ne dispose que d'un seul framework pour l'affichage des notifications push, et les notifications push s'affichent immédiatement tant que Braze dispose des jetons push et des certificats nécessaires.
{% endalert %}

Si vous devez envoyer des notifications push Android à vos utilisateurs avant que l'intégration du SDK Braze ne soit terminée, utilisez des paires clé-valeur pour valider les notifications push.

Vous devez disposer d'un récepteur pour gérer et afficher les payloads push. Pour notifier le récepteur du payload push, ajoutez les paires clé-valeur nécessaires à la Campaign push. Les valeurs de ces paires dépendent du fournisseur de push spécifique que vous utilisiez avant Braze.

{% alert note %}
Pour certains fournisseurs de notifications push, Braze doit aplatir les paires clé-valeur afin qu'elles puissent être correctement interprétées. Pour aplatir les paires clé-valeur d'une application Android spécifique, contactez votre gestionnaire du succès des clients.
{% endalert %}

## Questions fréquentes {#frequently-asked-questions}

### Comment trouver les utilisateurs traités comme spam ou bloqués pour la communication ? {#how-do-i-find-users-treated-as-spam-or-blocked-from-messaging}

Braze ne fournit pas de liste de spam dédiée dans le tableau de bord. Braze bloque les profils utilisateurs individuels (« utilisateurs fictifs ») ayant plus de cinq millions de sessions, plus de 20 000 noms d'événements personnalisés distincts ou plus de 20 000 noms de produits distincts dans les achats, et cesse d'ingérer toutes les données entrantes pour ce profil, aussi bien depuis les SDK que depuis la REST API. Si un identifiant est bloqué, [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) peut renvoyer l'erreur `"provided external_id is blacklisted and disallowed"`. Ce libellé est repris tel quel de la réponse de l'API. Pour trouver les profils bloqués en raison d'un nombre excessif de sessions, créez un [Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) avec le filtre **Session Count** défini sur **more than 5,000,000**, exportez le Segment au format CSV, puis vérifiez les champs du profil dans **Engagement** > **Search users** ou avec l'endpoint [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier). Il n'existe pas de filtre équivalent pour les noms d'événements personnalisés distincts ou les noms de produits, contactez donc votre gestionnaire de compte Braze pour identifier les profils bloqués pour ces raisons. Pour en savoir plus, consultez [Blocage du spam]({{site.baseurl}}/user_archival).