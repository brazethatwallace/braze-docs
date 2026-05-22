---
nav_title: Attributs standard
article_title: Attributs standard
page_order: 0.5
page_type: reference
description: "Cet article de référence répertorie les attributs utilisateur standard de Braze (clés réservées) ainsi que les exigences de syntaxe pour chacun d'entre eux."
---

# Attributs standard {#standard-attributes}

> Les attributs standard sont des champs prédéfinis que Braze reconnaît sur chaque profil utilisateur. Utilisez cette page comme référence rapide pour le nom du champ, le type de données et le format attendu de chaque attribut standard.

Les attributs standard (parfois appelés *attributs par défaut* ou *clés réservées*) sont différents des [attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/), qui sont propres à votre entreprise. Lorsque vous envoyez des données à Braze avec l'un des noms de champ répertoriés sur cette page, Braze les stocke dans le champ de profil prédéfini au lieu de créer un nouvel attribut personnalisé.

Vous pouvez définir les attributs standard via l'une de ces méthodes :

- Le [SDK Braze]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/)
- L'[objet d'attributs utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/) sur l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
- L'[import CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/)
- L'[Ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/)

{% alert important %}
Les noms des attributs standard sont sensibles à la casse. Utilisez toujours des minuscules (par exemple, `first_name`, et non `First_Name`). Si l'orthographe ou la casse ne correspond pas exactement, Braze stocke la valeur en tant qu'[attribut personnalisé]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/).
{% endalert %}

## Identifiants {#identifiers}

Les identifiants indiquent à Braze quel profil utilisateur mettre à jour ou créer. Chaque requête API et chaque ligne CSV doit inclure au moins un identifiant. Pour plus de détails sur le choix du bon identifiant, consultez [Résolution des identifiants]({{site.baseurl}}/api/objects_filters/user_attributes_object/#identifier-resolution).

| Champ | Type de données | Format et notes |
|---|---|---|
| `external_id` | Chaîne de caractères | Un identifiant utilisateur unique que vous attribuez. Une fois défini sur un profil, Braze l'utilise pour reconnaître l'utilisateur sur tous les appareils. Ne peut pas être supprimé après avoir été ajouté. |
| `braze_id` | Chaîne de caractères | Un identifiant attribué par Braze, créé lorsque le SDK détecte un appareil pour la première fois. En lecture seule. Ne peut pas être modifié. |
| `user_alias` | Objet | Un objet contenant `alias_name` (chaîne de caractères) et `alias_label` (chaîne de caractères), utilisé pour identifier les utilisateurs sans `external_id`. Mutuellement exclusif avec `external_id` dans la même requête. |
| `email` | Chaîne de caractères | Peut être utilisé comme identifiant lorsque `external_id` et `user_alias` sont absents. Prend la priorité sur `phone` si les deux sont envoyés. |
| `phone` | Chaîne de caractères | Peut être utilisé comme identifiant lorsque `external_id`, `user_alias` et `email` sont absents. Utilisez le format [E.164]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers/#recommended-format) (par exemple, `+14155552671`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Champs de profil {#profile-fields}

Ces champs capturent les données démographiques, de contact et de localisation de vos utilisateurs.

| Champ | Type de données | Format et notes |
|---|---|---|
| `first_name` | Chaîne de caractères | Le prénom de l'utilisateur (par exemple, `Jane`). |
| `last_name` | Chaîne de caractères | Le nom de famille de l'utilisateur (par exemple, `Doe`). |
| `email` | Chaîne de caractères | L'adresse e-mail de l'utilisateur (par exemple, `jane.doe@braze.com`). |
| `phone` | Chaîne de caractères | Le numéro de téléphone de l'utilisateur. Utilisez le format [E.164]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers/#recommended-format) (par exemple, `+14155552671`). |
| `dob` | Chaîne de caractères | Date de naissance au format `YYYY-MM-DD` (par exemple, `1988-02-14`). Permet le ciblage par anniversaire. |
| `gender` | Chaîne de caractères | L'une des valeurs suivantes : `M`, `F`, `O` (autre), `N` (non applicable), `P` (préfère ne pas répondre) ou `null` (inconnu). |
| `country` | Chaîne de caractères | Un code pays au format [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1) (par exemple, `US`, `GB`). Définir `country` via un import CSV ou l'API empêche le SDK de le capturer automatiquement. |
| `home_city` | Chaîne de caractères | La ville de résidence de l'utilisateur (par exemple, `London`). |
| `language` | Chaîne de caractères | Un code de langue au format [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (par exemple, `en`). Consultez la [liste des langues acceptées]({{site.baseurl}}/user_guide/data/unification/user_data/language_codes/). Définir `language` via un import CSV ou l'API empêche le SDK de le capturer automatiquement. |
| `time_zone` | Chaîne de caractères | Un nom de fuseau horaire issu de la [base de données des fuseaux horaires IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (par exemple, `America/New_York` ou `Eastern Time (US & Canada)`). |
| `current_location` | Objet | Un objet contenant `longitude` et `latitude` (par exemple, `{"longitude": -73.991443, "latitude": 40.753824}`). |
| `image_url` | Chaîne de caractères | Une URL vers l'image de profil de l'utilisateur. Jusqu'à 1 024 caractères. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Abonnement et consentement {#subscription-and-consent}

Ces champs gèrent la manière dont un utilisateur reçoit des messages sur les différents canaux. Leur mise à jour ne compte pas dans votre consommation de points de donnée.

| Champ | Type de données | Format et notes |
|---|---|---|
| `email_subscribe` | Chaîne de caractères | L'une des valeurs suivantes : `opted_in` (inscrit explicitement pour recevoir des e-mails), `unsubscribed` (désabonné explicitement des e-mails) ou `subscribed` (ni inscrit ni désabonné). |
| `push_subscribe` | Chaîne de caractères | L'une des valeurs suivantes : `opted_in`, `unsubscribed` ou `subscribed`. Mêmes définitions que pour `email_subscribe`. |
| `subscription_groups` | Tableau d'objets | Un tableau où chaque objet contient un `subscription_group_id` (chaîne de caractères) et un `subscription_state` (`subscribed` ou `unsubscribed`). Par exemple : `[{"subscription_group_id": "abc-123", "subscription_state": "subscribed"}]`. |
| `email_open_tracking_disabled` | Valeur booléenne | `true` ou `false`. Définissez sur `true` pour désactiver le pixel de suivi d'ouverture des e-mails pour cet utilisateur. Disponible uniquement pour SparkPost et SendGrid. |
| `email_click_tracking_disabled` | Valeur booléenne | `true` ou `false`. Définissez sur `true` pour désactiver le suivi des clics dans les e-mails pour cet utilisateur. Disponible uniquement pour SparkPost et SendGrid. |
| `marked_email_as_spam_at` | Chaîne de caractères | Horodatage auquel l'e-mail de l'utilisateur a été marqué comme spam. Utilisez le format [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Pour plus de détails sur la configuration des groupes d'abonnement, consultez [Groupes d'abonnement]({{site.baseurl}}/user_guide/channels/email/subscriptions/#subscription-groups).

## Sessions et engagement {#sessions-and-engagement}

Ces champs capturent la date à laquelle l'utilisateur a interagi pour la première ou la dernière fois avec votre application. Le SDK les enregistre automatiquement ; vous ne les définissez généralement via l'API ou un CSV que lors d'une migration depuis une autre plateforme.

| Champ | Type de données | Format et notes |
|---|---|---|
| `date_of_first_session` | Chaîne de caractères | La date à laquelle l'utilisateur a utilisé l'application pour la première fois. Utilisez le format [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) ou l'un des formats suivants : `yyyy-MM-ddTHH:mm:ss:SSSZ`, `yyyy-MM-ddTHH:mm:ss`, `yyyy-MM-dd HH:mm:ss`, `yyyy-MM-dd`, `MM/dd/yyyy` ou `ddd MM dd HH:mm:ss.TZD YYYY`. |
| `date_of_last_session` | Chaîne de caractères | La date à laquelle l'utilisateur a utilisé l'application pour la dernière fois. Mêmes formats acceptés que pour `date_of_first_session`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Jetons de notification push {#push-tokens}

Utilisez ces champs lors de la migration de jetons de notification push depuis une autre plateforme. Après l'intégration du SDK Braze, les jetons de notification push sont capturés automatiquement. Pour des conseils de migration, consultez [Migration des jetons de notification push]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens).

| Champ | Type de données | Format et notes |
|---|---|---|
| `push_tokens` | Tableau d'objets | Un tableau où chaque objet contient un `app_id` (chaîne de caractères) et un `token` (chaîne de caractères). Incluez éventuellement un `device_id` (chaîne de caractères). Par exemple : `[{"app_id": "YOUR_APP_ID", "token": "abcd", "device_id": "optional_device_id"}]`. |
| `push_token_import` | Valeur booléenne | Indicateur de niveau supérieur (non imbriqué dans `attributes`). Définissez sur `true` pour importer des jetons de notification push hérités pour les utilisateurs anonymes sans `external_id`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Profil social {#social-profile}

Ces champs stockent les données provenant des intégrations de réseaux sociaux.

| Champ | Type de données | Format et notes |
|---|---|---|
| `facebook` | Objet | Un objet contenant l'un des éléments suivants : `id` (chaîne de caractères), `likes` (tableau de chaînes de caractères) ou `num_friends` (entier). |
| `twitter` | Objet | Un objet contenant l'un des éléments suivants : `id` (entier), `screen_name` (chaîne de caractères, identifiant X), `followers_count` (entier), `friends_count` (entier) ou `statuses_count` (entier). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Exemple d'API {#api-example}

La requête suivante définit des attributs standard sur deux utilisateurs via l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

```http
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes": [
    {
      "external_id": "user1",
      "first_name": "Jane",
      "last_name": "Doe",
      "email": "jane.doe@example.com",
      "country": "US",
      "language": "en",
      "time_zone": "America/New_York",
      "dob": "1988-02-14",
      "email_subscribe": "opted_in"
    },
    {
      "external_id": "user2",
      "first_name": "Alex",
      "phone": "+14155552671",
      "current_location": {
        "longitude": -73.991443,
        "latitude": 40.753824
      },
      "subscription_groups": [
        {
          "subscription_group_id": "abc-123",
          "subscription_state": "subscribed"
        }
      ]
    }
  ]
}
```

Pour le contrat API complet, consultez l'[objet d'attributs utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/).

## Exemple CSV {#csv-example}

Le CSV suivant met à jour les attributs standard de deux utilisateurs. Les en-têtes de colonnes doivent correspondre exactement aux noms de champs de cet article. Les en-têtes qui ne correspondent pas (par exemple, `First_name` au lieu de `first_name`) sont importés en tant qu'attributs personnalisés.

```plaintext
external_id,first_name,last_name,email,country,language,dob,email_subscribe
user1,Jane,Doe,jane.doe@example.com,US,en,1988-02-14,opted_in
user2,Alex,Smith,alex.smith@example.com,GB,en,1992-09-30,subscribed
```

Certains attributs standard ne peuvent pas être définis via un import CSV. Vous devez envoyer les tableaux, les jetons de notification push et les objets imbriqués via l'API ou l'[Ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/). Pour la liste complète des champs pris en charge par le CSV et les étapes d'import, consultez [Attributs par défaut]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/#default-attributes).

## Considérations {#considerations}

Gardez ces points à l'esprit lorsque vous travaillez avec les attributs standard :

- **Les noms de champs sont sensibles à la casse.** Utilisez toujours des minuscules. Un en-tête ou une clé qui ne correspond pas exactement au nom d'un attribut standard est traité comme un attribut personnalisé.
- **La capture automatique du SDK est désactivée lorsque vous définissez des valeurs via l'API ou un CSV.** Lorsque vous définissez `country` ou `language` via l'API ou un CSV, Braze cesse de capturer automatiquement ces champs depuis le SDK pour cet utilisateur.
- **`null` supprime une valeur.** Définir un attribut standard sur `null` le supprime du profil. Certains champs, notamment `external_id` et `user_alias`, ne peuvent pas être supprimés après avoir été définis.
- **Les valeurs vides dans un CSV n'écrasent pas les données existantes.** Une cellule vide dans un import CSV conserve la valeur existante sur le profil. Pour effacer une valeur, utilisez l'API.
- **Les fuseaux horaires sont par défaut en UTC.** Les chaînes de date sans décalage sont interprétées comme minuit UTC et affichées dans le fuseau horaire de votre espace de travail. Pour spécifier un fuseau horaire, ajoutez un décalage UTC (par exemple, `2024-11-10T18:00:00-05:00`).

## Pages associées {#related-pages}

- [Objet d'attributs utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/) — Contrat API complet pour l'objet d'attributs.
- [Endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) — Endpoint REST pour créer et mettre à jour les profils utilisateur.
- [Définir les attributs utilisateur]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/) — Méthodes du SDK pour définir les attributs standard et personnalisés.
- [Import CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/) — Charger des attributs standard via un fichier CSV.
- [Attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) — Définir des attributs propres à votre entreprise.
- [Types de données]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/) — Référence des types de données pris en charge.