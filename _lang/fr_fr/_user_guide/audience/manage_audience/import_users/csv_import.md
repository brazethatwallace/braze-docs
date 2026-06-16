---
nav_title: Importation CSV
article_title: Importation CSV
description: "Découvrez comment enregistrer et mettre à jour les attributs utilisateur et les événements personnalisés à l'aide de l'importation CSV."
page_order: 1.2
---

# Importation CSV {#csv-import}

> Découvrez comment enregistrer et mettre à jour les attributs utilisateur et les événements personnalisés à l'aide de l'importation CSV.

## À propos de l'importation CSV {#about-csv-import}

Vous pouvez utiliser l'importation CSV pour enregistrer et mettre à jour les attributs utilisateur et événements personnalisés suivants. Braze accepte ces données sous forme de fichiers CSV standard dans les limites de taille maximale indiquées dans le tableau suivant.

| Type | Définition | Exemple | Taille maximale du fichier |
|---|---|---|---|
| Attributs par défaut | Attributs utilisateur réservés reconnus par Braze. | `first_name`, `email` | 500 Mo |
| Attributs personnalisés | Attributs utilisateur propres à votre entreprise. | `last_destination_searched` | 500 Mo |
| Événements personnalisés | Événements propres à votre entreprise qui représentent des actions utilisateur. | `trip_booked` | 50 Mo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="À propos de l'importation CSV" }

## Utiliser l'importation CSV {#using-csv-import}

### Étape 1 : Télécharger un modèle CSV {#step-1-download-a-csv-template}

Pour ouvrir l'importation CSV, accédez à **Audiences** > **Import Users**. Vous y trouverez un tableau répertoriant les détails des importations les plus récentes, tels que la date de téléversement, le nom de la personne ayant effectué le téléversement, le nom du fichier, la disponibilité du ciblage, le nombre de lignes importées et le statut de l'importation.

Pour commencer, sélectionnez **Attributes** ou **Events**, puis téléchargez le modèle approprié pour vous aider à construire votre fichier CSV à téléverser.

![La page « Import Users » dans le tableau de bord de Braze.]({% image_buster /assets/img/csv_import/import_users_page.png %})

### Étape 2 : Choisir un identifiant {#choose-an-identifier}

Le fichier CSV que vous importez doit contenir un identifiant dédié. Choisissez l'un des types d'identifiants suivants pour votre importation :

{% tabs local %}
<!-- TAB -->
{% tab ID externe %}
Lors de l'importation de vos données client, vous pouvez utiliser un `external_id` comme identifiant unique pour chaque client. Lorsque vous fournissez un `external_id` dans votre importation, Braze met à jour tout utilisateur existant ayant le même `external_id` ou crée un nouvel utilisateur identifié avec cet `external_id` si aucun n'est trouvé.

- Télécharger : [Modèle d'importation d'attributs CSV : ID externe]({{site.baseurl}}/assets/download_file/braze-user-import-template-csv.xlsx?3aafd0c03634ac03f248b3055fbc3126)
- Télécharger : [Modèle d'importation d'événements CSV : ID externe](https://braze.com/unlisted_docs/assets/download_file/braze-csv-events-import-template.csv?3b64ea284baa9a21cfe0a7ab4b46fce4)

{% alert note %}
Si vous téléversez un mélange d'utilisateurs avec un `external_id` et d'utilisateurs sans, vous devez créer un CSV pour chaque importation. Un CSV ne peut pas contenir à la fois des `external_ids` et des alias d'utilisateur.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab Alias d'utilisateur %}
Pour cibler les utilisateurs qui n'ont pas d'`external_id`, vous pouvez importer une liste d'utilisateurs avec des alias d'utilisateur. Un alias sert d'identifiant utilisateur unique alternatif et peut être utile si vous essayez de communiquer avec des utilisateurs anonymes qui ne se sont pas inscrits ou n'ont pas créé de compte sur votre application.

Si vous téléversez ou mettez à jour des profils utilisateur qui ne possèdent qu'un alias, vous devez avoir les deux colonnes suivantes dans votre CSV :

- `user_alias_name` : Un identifiant utilisateur unique ; une alternative à l'`external_id`
- `user_alias_label` : Un libellé commun permettant de regrouper les alias d'utilisateur

| `user_alias_name` | `user_alias_label` | `last_name` | `email` | sample_attribute |
| :---- | :---- | :---- | :---- | :---- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Étape 2 : Choisir un identifiant" }

Lorsque vous fournissez à la fois un `user_alias_name` et un `user_alias_label` dans votre importation, Braze met à jour tout utilisateur existant ayant les mêmes `user_alias_name` et `user_alias_label`. Si aucun utilisateur n'est trouvé, Braze crée un nouvel utilisateur identifié avec ce `user_alias_name`.

{% alert important %}
Vous ne pouvez pas utiliser une importation CSV pour mettre à jour un utilisateur existant avec un `user_alias_name` s'il possède déjà un `external_id`. Cela crée à la place un nouveau profil utilisateur avec le `user_alias_name` associé. Pour associer un utilisateur possédant uniquement un alias à un `external_id`, utilisez l'[endpoint Identifier les utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).
{% endalert %}

Télécharger : [Modèle d'importation d'attributs CSV : Alias d'utilisateur]({{site.baseurl}}/assets/download_file/braze-user-import-alias-template-csv.xlsx?c0ce6c0aa1e901395161d87c5ba17747)
{% endtab %}

<!-- TAB -->
{% tab ID Braze %}
Pour mettre à jour des profils utilisateur existants dans Braze en utilisant un ID Braze interne au lieu d'un `external_id` ou d'un `user_alias_name` et `user_alias_label`, spécifiez `braze_id` comme en-tête de colonne.

Cela peut être utile si vous avez exporté des données utilisateur depuis Braze via notre option d'exportation CSV dans la segmentation et que vous souhaitez ajouter un nouvel attribut personnalisé à ces utilisateurs existants.

{% alert important %}
Vous ne pouvez pas utiliser une importation CSV pour créer un nouvel utilisateur en utilisant `braze_id`. Cette méthode ne peut être utilisée que pour mettre à jour des utilisateurs préexistants dans la plateforme Braze.
{% endalert %}

{% alert tip %}
La valeur `braze_id` peut être libellée `Appboy ID` dans les exportations CSV du tableau de bord de Braze. Cet ID est identique au `braze_id` d'un utilisateur, vous pouvez donc renommer cette colonne en `braze_id` lorsque vous réimportez le CSV.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab Adresse e-mail et numéros de téléphone %}
Vous pouvez omettre un ID externe ou un alias d'utilisateur et utiliser une adresse e-mail ou un numéro de téléphone pour importer des utilisateurs. Avant d'importer un fichier CSV avec des adresses e-mail ou des numéros de téléphone, vérifiez les points suivants :

- Vérifiez que vous n'avez pas d'ID externes ou d'alias d'utilisateur pour ces profils dans votre fichier CSV. Si c'est le cas, Braze donnera la priorité à l'ID externe ou à l'alias d'utilisateur avant l'adresse e-mail pour identifier les profils.
- Confirmez que votre fichier CSV est correctement formaté.

{% alert note %}
Si vous incluez à la fois des adresses e-mail et des numéros de téléphone dans votre fichier CSV, l'adresse e-mail est prioritaire sur le numéro de téléphone lors de la recherche de profils.
{% endalert %}

Si un profil existant possède cette adresse e-mail ou ce numéro de téléphone, ce profil est mis à jour et Braze ne crée pas de nouveau profil. S'il existe plusieurs profils avec la même adresse e-mail, Braze utilise la même logique que l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) où le profil mis à jour le plus récemment sera mis à jour.

Si un profil avec cette adresse e-mail ou ce numéro de téléphone n'existe pas, Braze crée un nouveau profil avec cet identifiant. Vous pouvez utiliser l'[endpoint `/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) pour identifier ce profil ultérieurement. Pour supprimer un profil utilisateur, vous pouvez également utiliser l'endpoint [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/).
{% endtab %}
{% endtabs %}

### Étape 3 : Construire votre fichier CSV {#step-3-build-your-csv-file}

Vous pouvez téléverser l'un des types de données suivants dans un seul fichier CSV. Pour téléverser plus d'un type de données, téléversez plusieurs fichiers CSV.

- **Attributs utilisateur :** Cela inclut les attributs utilisateur par défaut et personnalisés. Les attributs utilisateur par défaut sont des clés réservées dans Braze (telles que `first_name` ou `email`) et les attributs personnalisés sont des attributs utilisateur propres à votre entreprise (tels que `last_destination_searched`).
- **Événements personnalisés :** Ceux-ci sont propres à votre entreprise et reflètent les actions effectuées par un utilisateur, comme `trip_booked` pour une application de réservation de voyages.

Lorsque vous êtes prêt à construire votre fichier CSV, consultez les informations suivantes :

{% tabs local %}
<!-- TAB -->
{% tab Attributs utilisateur %}
#### Identifiants requis {#required-identifiers-attributes}

Bien que `external_id` ne soit pas requis, votre fichier CSV doit inclure un identifiant utilisateur pouvant être associé à **l'un** des identifiants suivants. Pour plus de détails sur chacun d'entre eux, consultez [Choisir un identifiant](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **et** `user_alias_label`
- `email`
- `phone`

#### Attributs personnalisés {#custom-attributes}

Les types de données suivants peuvent être utilisés comme attributs personnalisés pour l'importation CSV. Les en-têtes de colonne qui ne correspondent pas exactement à un [attribut par défaut](#default-attributes) sont importés comme attributs personnalisés dans Braze, sauf modification lors de l'étape de mappage.

| Type de données | Description |
|---|---|
| Date et heure | Doit être stocké au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601). |
| Valeur booléenne | Accepte `true` ou `false`. |
| Nombre | Doit être un entier ou un nombre à virgule flottante sans espaces ni virgules. Les nombres à virgule flottante doivent utiliser un point (`.`) comme séparateur décimal. |
| Chaîne de caractères | Peut contenir des virgules si la valeur est encadrée par des guillemets doubles (`""`). |
| Vide | Les valeurs vides n'écraseront pas les valeurs existantes sur le profil utilisateur, et vous n'avez pas besoin d'inclure tous les attributs utilisateur existants dans votre fichier CSV. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Attributs personnalisés" }

{% alert important %}
Les tableaux, les jetons de notification push et les types de données d'événements personnalisés ne sont pas pris en charge dans l'importation d'utilisateurs, car les virgules dans votre fichier CSV seront interprétées comme un séparateur de colonne et provoqueront des erreurs lors de l'analyse de votre fichier.<br><br>Pour téléverser ce type de valeurs, utilisez plutôt l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) ou l'[Ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/).
{% endalert %}

#### Attributs par défaut {#default-attributes}

{% alert important %}
Lors de l'importation d'attributs par défaut, les en-têtes de colonne que vous utilisez doivent correspondre exactement à l'orthographe et à la casse des attributs utilisateur par défaut. Sinon, Braze les détecte comme des [attributs personnalisés](#custom-attributes).
{% endalert %}

{% alert tip %}
Pour la liste complète des attributs standard reconnus par Braze (via le SDK, l'API, le CSV et l'Ingestion de données cloud), consultez [Attributs standard]({{site.baseurl}}/user_guide/data/activation/attributes/standard_attributes/). Le tableau suivant ne couvre que le sous-ensemble pouvant être défini via l'importation CSV.
{% endalert %}

Les attributs par défaut suivants sont disponibles pour l'importation d'utilisateurs.

| Champ du profil utilisateur | Type de données | Description | Requis ? |
| :---- | :---- | :---- | :---- |
| `external_id` | Chaîne de caractères | Un identifiant utilisateur unique pour votre client. | Conditionnel. Voir [Identifiants requis](#required-identifiers-attributes). |
| `user_alias_name` | Chaîne de caractères | Un identifiant utilisateur unique pour les utilisateurs anonymes, servant d'alternative à `external_id`. Doit être utilisé avec `user_alias_label`. | Conditionnel. Voir [Identifiants requis](#required-identifiers-attributes). |
| `user_alias_label` | Chaîne de caractères | Un libellé commun permettant de regrouper les alias d'utilisateur. Doit être utilisé avec `user_alias_name`. | Conditionnel. Voir [Identifiants requis](#required-identifiers-attributes). |
| `first_name` | Chaîne de caractères | Le prénom de vos utilisateurs tel qu'ils l'ont indiqué (par exemple, `Jane`). | Non |
| `last_name` | Chaîne de caractères | Le nom de famille de vos utilisateurs tel qu'ils l'ont indiqué (par exemple, `Doe`). | Non |
| `email` | Chaîne de caractères | L'adresse e-mail de vos utilisateurs telle qu'ils l'ont indiquée (par exemple, `jane.doe@braze.com`). | Non |
| `country` | Chaîne de caractères | Les codes pays doivent être transmis à Braze selon la norme ISO-3166-1 alpha-2 (par exemple, `GB`). | Non |
| `dob` | Chaîne de caractères | Doit être transmis au format « AAAA-MM-JJ » (par exemple, `1980-12-21`). Cela importe la date de naissance de votre utilisateur et vous permet de cibler les utilisateurs dont l'anniversaire est « aujourd'hui ». | Non |
| `gender` | Chaîne de caractères | « M », « F », « O » (autre), « N » (non applicable), « P » (préfère ne pas dire), ou nil (inconnu). | Non |
| `home_city` | Chaîne de caractères | La ville de résidence de vos utilisateurs telle qu'ils l'ont indiquée (par exemple, `London`). | Non |
| `language` | Chaîne de caractères | La langue doit être transmise à Braze selon la norme ISO-639-1 (par exemple, `en`). Consultez notre [liste des langues acceptées]({{site.baseurl}}/user_guide/data/unification/user_data/language_codes/). | Non |
| `phone` | Chaîne de caractères | Un numéro de téléphone tel qu'indiqué par vos utilisateurs, au format `E.164` (par exemple, `+442071838750`). Consultez [Numéros de téléphone des utilisateurs]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers/) pour des conseils de formatage. | Non |
| `email_open_tracking_disabled` | Valeur booléenne | Accepte true ou false. Définissez sur true pour désactiver l'ajout du pixel de suivi d'ouverture à tous les futurs e-mails envoyés à cet utilisateur. Disponible uniquement pour SparkPost et SendGrid. | Non |
| `email_click_tracking_disabled` | Valeur booléenne | Accepte true ou false. Définissez sur true pour désactiver le suivi des clics pour tous les liens dans un futur e-mail envoyé à cet utilisateur. Disponible uniquement pour SparkPost et SendGrid. | Non |
| `email_subscribe` | Chaîne de caractères | Les valeurs disponibles sont `opted_in` (explicitement inscrit pour recevoir des e-mails), `unsubscribed` (explicitement désabonné des e-mails) et `subscribed` (ni inscrit ni désabonné). | Non |
| `push_subscribe` | Chaîne de caractères | Les valeurs disponibles sont `opted_in` (explicitement inscrit pour recevoir des notifications push), `unsubscribed` (explicitement désabonné des notifications push) et `subscribed` (ni inscrit ni désabonné). | Non |
| `time_zone` | Chaîne de caractères | Le fuseau horaire doit être transmis à Braze dans le même format que la base de données des fuseaux horaires IANA (par exemple, `America/New_York` ou `Eastern Time (US & Canada)`). | Non |
| `date_of_first_session`  `date_of_last_session` | Chaîne de caractères | Peut être transmis dans l'un des formats ISO 8601 suivants : « AAAA-MM-JJ » « AAAA-MM-JJTHH:MM:SS+00:00 » « AAAA-MM-JJTHH:MM:SSZ » « AAAA-MM-JJTHH:MM:SS » (par exemple, 2019-11-20T18:38:57) | Non |
| `subscription_group_id` | Chaîne de caractères | L'`id` de votre groupe d'abonnement. Cet identifiant se trouve sur la page des groupes d'abonnement de votre tableau de bord. | Non |
| `subscription_state` | Chaîne de caractères | L'état d'abonnement pour le groupe d'abonnement spécifié par `subscription_group_id`. Les valeurs autorisées sont `unsubscribed` (pas dans le groupe d'abonnement) ou `subscribed` (dans le groupe d'abonnement). | Non, mais fortement recommandé si `subscription_group_id` est utilisé |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Attributs par défaut" }

#### Mettre à jour le statut du groupe d'abonnement (facultatif) {#updating-subscription-group-status-optional}

De plus, vous pouvez ajouter des utilisateurs à des groupes d'abonnement e-mail ou SMS via l'importation d'utilisateurs. Cela est particulièrement utile pour les SMS, car un utilisateur doit être inscrit dans un groupe d'abonnement SMS pour recevoir des messages via le canal SMS. Pour plus d'informations, consultez [Groupes d'abonnement SMS](https://www.braze.com/docs/sms_rcs_subscription_groups#subscription-group-mms-enablement).

Si vous mettez à jour les statuts des groupes d'abonnement, vous devez avoir les deux colonnes suivantes dans votre CSV :

- `subscription_group_id` : L'`id` du [groupe d'abonnement](https://www.braze.com/docs/user_guide/channels/email/subscriptions#subscription-groups).
- `subscription_state` : Les valeurs disponibles sont `unsubscribed` (pas dans le groupe d'abonnement) ou `subscribed` (dans le groupe d'abonnement).

| external_id | first_name | subscription_group_id | subscription_state |
| :---- | :---- | :---- | :---- |
| A8i3mkd99 | Colby | 6ff593d7-cf69-448b-aca9-abf7d7b8c273 | subscribed |
| k2LNhj8Ks | Tom | aea02307-a91e-4bc0-abad-1c0bee817dfa | subscribed |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Mettre à jour le statut du groupe d'abonnement (facultatif)" }

{% alert note %}
Un seul `subscription_group_id` peut être défini par ligne dans l'importation d'utilisateurs. Différentes lignes peuvent avoir des valeurs `subscription_group_id` différentes. Cependant, si vous devez inscrire les mêmes utilisateurs dans plusieurs groupes d'abonnement, vous devrez effectuer plusieurs importations.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab Événements personnalisés %}
#### Identifiants requis {#required-identifiers-custom-events}

Bien que `external_id` ne soit pas requis, vous **devez** inclure **l'un** des identifiants suivants comme en-tête dans votre fichier CSV. Pour plus de détails sur chacun d'entre eux, consultez [Choisir un identifiant](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **et** `user_alias_label`
- `email`
- `phone`

#### Champs d'événements personnalisés {#custom-event-fields}

En plus des champs suivants, votre CSV peut également contenir des en-têtes de colonne supplémentaires pour les propriétés d'événement. Ces propriétés doivent avoir un en-tête de colonne au format `<event_name>.properties.<property name>.`

Par exemple, l'événement personnalisé `trip_booked` peut avoir les propriétés `destination` et `duration`. Celles-ci peuvent être importées en utilisant les en-têtes de colonne `trip_booked.properties.destination` et `trip_booked.properties.duration`.

| Champ du profil utilisateur | Type de données | Informations | Requis ? |
| :---- | :---- | :---- | :---- |
| `external_id` | Chaîne de caractères | Un identifiant utilisateur unique pour votre utilisateur. | Conditionnel. Voir [Identifiants requis](#required-identifiers-custom-events). |
| `braze_id` | Chaîne de caractères | Un identifiant attribué par Braze pour votre utilisateur. | Conditionnel. Voir [Identifiants requis](#required-identifiers-custom-events). |
| `user_alias_name` | Chaîne de caractères | Un identifiant utilisateur unique pour les utilisateurs anonymes, servant d'alternative à `external_id`. Doit être utilisé avec `user_alias_label`. | Conditionnel. Voir [Identifiants requis](#required-identifiers-custom-events). |
| `user_alias_label` | Chaîne de caractères | Un libellé commun permettant de regrouper les alias d'utilisateur. Doit être utilisé avec `user_alias_name`. | Conditionnel. Voir [Identifiants requis](#required-identifiers-custom-events). |
| `email` | Chaîne de caractères | L'adresse e-mail de vos utilisateurs telle qu'ils l'ont indiquée (par exemple, `jane.doe@braze.com`). | Non, et ne peut être utilisé qu'en l'absence d'autres identifiants. Voir la note suivante. |
| `phone` | Chaîne de caractères | Un numéro de téléphone tel qu'indiqué par vos utilisateurs, au format `E.164` (par exemple, `+442071838750`). Consultez [Numéros de téléphone des utilisateurs]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers/) pour des conseils de formatage. | Non, et ne peut être utilisé qu'en l'absence d'autres identifiants. Voir la note suivante. |
| `name` | Chaîne de caractères | Un événement personnalisé de vos utilisateurs. | Oui |
| `time` | Chaîne de caractères | L'heure de l'événement. Peut être transmis dans l'un des formats ISO-8601 suivants : « AAAA-MM-JJ » « AAAA-MM-JJTHH:MM:SS+00:00 » « AAAA-MM-JJTHH:MM:SSZ » « AAAA-MM-JJTHH:MM:SS » (par exemple, 2019-11-20T18:38:57) | Oui |
| `<event name>.properties.<property name>` | Plusieurs | Une propriété d'événement associée à un événement personnalisé. Un exemple est `trip_booked.properties.destination` | Non |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Champs d'événements personnalisés" }

#### Exigences de format pour les événements personnalisés {#format-requirements-for-custom-events}

Lors de l'importation d'événements personnalisés par CSV, vous devez formater votre fichier selon les exigences suivantes pour une importation de données réussie.

##### Comprendre le formatage des événements personnalisés {#understanding-custom-event-formatting}

Il est important de formater correctement votre CSV d'événements personnalisés en utilisant la notation par points afin que chaque propriété soit associée au bon événement. Si le format est incorrect, les propriétés peuvent être ignorées ou l'importation peut échouer, en particulier lorsque plusieurs types d'événements sont inclus dans un même fichier.

##### Utiliser la notation par points pour les propriétés d'événement {#use-dot-notation-for-event-properties}

La notation par points est utilisée pour définir la relation hiérarchique entre un événement personnalisé et ses propriétés. Cette convention de formatage vous permet d'importer des données d'événement structurées qui incluent des attributs spécifiques pour chaque événement.

Le format de la notation par points suit cette structure : `event_name.properties.property_name`

La notation par points fonctionne dans l'ordre suivant :

1. Le nom de l'événement vient en premier
2. Suivi de `.properties.` pour indiquer que ce qui suit est une propriété d'événement
3. Enfin, le nom spécifique de la propriété

**Exemple :**

Pour un événement personnalisé appelé `rented_movie` avec les propriétés `movie_name` et `genre`, vos en-têtes de colonne CSV seraient :

- `rented_movie.properties.movie_name`
- `rented_movie.properties.genre`

Cette notation indique à Braze de créer un événement personnalisé nommé `rented_movie` et d'attacher les propriétés `movie_name` et `genre` à cette instance d'événement spécifique.

##### Un événement par ligne {#one-event-per-row}

Chaque ligne de votre CSV représente un seul événement personnalisé pour un seul utilisateur. Si un utilisateur a plusieurs événements, vous devez inclure une ligne distincte pour chaque événement, même s'ils partagent le même identifiant utilisateur.

{% alert important %}
Lorsqu'une ligne contient des données pour un événement spécifique, ne remplissez que les colonnes correspondant aux propriétés de cet événement. Laissez les colonnes des autres événements vides.
{% endalert %}

##### Exemple de structure CSV {#example-csv-structure}

Le tableau suivant illustre le formatage correct pour l'importation d'événements personnalisés avec des propriétés. Cet exemple montre deux utilisateurs ayant chacun effectué des événements différents : l'un a loué un film et l'autre a acheté un film.

| external_id | name | time | rented_movie.properties.movie_name | rented_movie.properties.genre | bought_movie.properties.movie_name | bought_movie.properties.genre |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 123 | rented_movie | 2024-06-10T12:00:00Z | Ghostbusters | Action | | |
| 456 | bought_movie | 2024-06-12T12:00:00Z | | | Ghostbusters | Action |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 .reset-td-br-7 aria-label="Exemple de structure CSV" }

Dans cet exemple :

- L'utilisateur `123` a déclenché l'événement `rented_movie` avec les propriétés `movie_name` (Ghostbusters) et `genre` (Action)
- L'utilisateur `456` a déclenché l'événement `bought_movie` avec les propriétés `movie_name` (Ghostbusters) et `genre` (Action)
- Chaque événement ne remplit que ses colonnes de propriétés pertinentes, laissant les colonnes de propriétés des autres événements vides

{% endtab %}
{% endtabs %}

### Étape 4 : Téléverser votre fichier {#step-4-upload-your-file}

Pour téléverser votre fichier, sélectionnez **Attributes** ou **Events**, cliquez sur **Browse Files**, puis téléversez votre CSV. Braze affiche un aperçu des premières lignes et un résumé des champs détectés.

Pour les fichiers volumineux (jusqu'à 500 Mo pour les attributs par défaut et personnalisés, ou 50 Mo pour les événements personnalisés), le tableau de bord peut sembler temporairement non réactif pendant le téléversement du fichier et le calcul de l'importation par Braze. Ces téléversements et calculs peuvent prendre plus de temps que pour des fichiers plus petits. Laissez cette étape se terminer. Pour plus de contexte sur les limites de fichiers et les délais, consultez [Construire votre CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#constructing-your-csv).

Dans le champ **Import name**, vous pouvez renommer votre importation. Par défaut, le nom du fichier est utilisé.

{% alert note %}
L'aperçu du fichier n'affiche que les premières lignes de votre fichier. Pour vérifier chaque ligne avant l'importation, utilisez la [validation du fichier](#file-validation).
{% endalert %}

### Étape 5 : Mapper vos champs (pour les attributs) {#csv-data-mapping}

Après l'aperçu, vous pouvez mapper les en-têtes de votre CSV aux attributs Braze. Braze mappe automatiquement les champs de votre fichier CSV aux attributs portant des noms identiques et crée de nouveaux attributs si nécessaire. Vous avez également la possibilité d'ajuster manuellement les suggestions ou de sélectionner des attributs différents pour n'importe quelle colonne.

![La page de mappage des colonnes.]({% image_buster /assets/img/csv_import/column_mapping_mapped.png %})

#### Statuts de mappage {#mapping-statuses}

La colonne de statut de mappage indique l'action qui se produit lorsque votre fichier CSV est importé et peut être l'une des suivantes.

| Statut de mappage | Signification |
|:---|:---|
| **Mappé** | Champ mappé à un attribut ou identifiant existant. |
| **Nouvel attribut** | Braze crée un nouvel attribut lors de l'importation. Vous pouvez modifier cet attribut en sélectionnant le bouton **Edit new attribute**. |
| **Incompatibilité de type de données** | Le type de données détecté de la colonne CSV ne correspond pas au type de données de l'attribut ou identifiant existant. Braze tente de convertir le type de données lors de l'importation pour correspondre à l'attribut existant. La valeur est ignorée si cela n'est pas possible. |
| **Attribut sur liste de blocage** | Le champ CSV correspond au nom d'un attribut sur liste de blocage. Sélectionnez un attribut différent pour le mappage, sinon la colonne ne sera pas importée. |
| **Attribut en double** | Il y a un ou plusieurs champs portant le même nom dans votre fichier CSV. Mappez les colonnes portant le même nom à des attributs différents, sinon seule la première colonne sera importée. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Statuts de mappage" }


#### Modifier les nouveaux attributs {#editing-new-attributes}

Lorsqu'un attribut correspondant n'existe pas dans votre espace de travail, Braze tente de créer un nouvel attribut lors de l'importation en utilisant le nom du champ CSV et le type de données détecté. Vous pouvez modifier ce nouvel attribut avant l'importation en sélectionnant le bouton **Edit new attribute** à côté du statut de mappage.

![Le bouton de modification du nouvel attribut sur la page de mappage des colonnes.]({% image_buster /assets/img/csv_import/column_mapping_edit_attribute_button.png %})


{% alert note %}
Vous ne pouvez pas passer à l'étape suivante tant qu'un identifiant n'est pas mappé. Braze mappe automatiquement un identifiant lorsque c'est possible. Consultez la section **Champs requis** pour vérifier si un identifiant est mappé.
{% endalert %}

### Étape 6 : Choisir les préférences de ciblage {#targeting-preferences}

Après le mappage, vous pouvez choisir parmi les préférences de ciblage suivantes sur la page des paramètres d'importation. Si vous n'avez pas besoin de créer un nouveau filtre de ciblage ou segment à partir de votre importation, sélectionnez **Do not make this list available as a targeting filter**.

| Option | Description |
|---|---|
| Filtre de ciblage | Pour convertir votre fichier CSV en option de reciblage lors de la création de segments, choisissez votre fichier dans le menu déroulant **Updated/Imported from CSV**, puis sélectionnez **Create targeting filter**. |
| Nouveaux segments | Pour créer également un nouveau segment à partir de votre nouveau filtre de ciblage, sélectionnez **Create targeting filter and add to new segment**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 6 : Choisir les préférences de ciblage" }

![Un groupe de filtres avec le filtre « Updated/Imported from CSV » incluant un fichier CSV intitulé « Halloween season fun ».]({% image_buster /assets/img/csv_import/add_filter_group.png %}){: style="max-width:85%;"}

### Étape 7 : Valider votre fichier (facultatif) {#file-validation}

Avant de lancer votre importation, vous pouvez exécuter une validation du fichier pour vérifier chaque ligne à la recherche d'erreurs et d'avertissements. Pour valider votre fichier, sélectionnez **Validate file before importing** sur la page des paramètres d'importation, puis sélectionnez **Next**.

La validation peut prendre jusqu'à 2 minutes pour les fichiers à la taille maximale autorisée. Pendant la validation, vous pouvez sélectionner **Skip validation** pour la contourner et procéder immédiatement.

#### Résultats de la validation {#validation-results}

Lorsque la validation est terminée, l'un des résultats suivants apparaît.

| Résultat | Signification | Étape suivante |
|---|---|---|
| **Validation terminée** | Aucun problème trouvé. | Sélectionnez **Import data**. |
| **Problèmes trouvés** | Certaines lignes contiennent des erreurs ou des avertissements. | Téléchargez le rapport d'erreurs pour les examiner, puis sélectionnez **Import anyway** pour continuer ou **Cancel** pour corriger votre fichier d'abord. |
| **Validation expirée** | La validation a manqué de temps. Les lignes vérifiées ne présentaient aucun problème. | Sélectionnez **Import data**. Un rapport complet sera disponible dans quelques minutes. |
| **Validation expirée avec des problèmes** | La validation a manqué de temps et a trouvé des erreurs dans certaines des lignes vérifiées. | Téléchargez le rapport partiel pour examiner ce qui a été trouvé, puis sélectionnez **Import anyway** ou **Cancel**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Résultats de la validation" }

![La page de résumé montrant la section des problèmes trouvés, avec un décompte des lignes contenant des erreurs et des avertissements, et des options pour revenir en arrière, télécharger le rapport d'erreurs ou lancer l'importation.]({% image_buster /assets/img/csv_import/summary_page_validation_results.png %})

#### Comprendre le rapport d'erreurs {#understanding-the-error-report}

Le rapport d'erreurs est un fichier CSV qui contient chaque ligne signalée avec ses données d'origine et une description du problème.

| Type de problème | Description |
|---|---|
| **Erreur** | La ligne sera entièrement ignorée lors de l'importation. |
| **Avertissement** | La ligne sera importée, mais certaines valeurs seront ignorées. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprendre le rapport d'erreurs" }

Après avoir examiné le rapport, vous pouvez corriger les problèmes dans votre fichier d'origine et le retéléverser, ou procéder à l'importation et accepter les résultats partiels.



### Étape 8 : Lancer votre importation CSV {#step-8-start-your-csv-import}

Lorsque vous êtes prêt, sélectionnez **Start Import**. Vous pouvez suivre la progression en cours sur la page **Import Users**, qui s'actualise automatiquement toutes les 5 secondes.
Le traitement peut prendre de quelques minutes à quelques heures selon la taille de votre CSV. Pendant ce temps, le tableau de bord peut sembler non réactif ou répondre lentement, mais l'importation est toujours en cours.

{% alert note %}
Vous pouvez importer plusieurs CSV en même temps. Les importations CSV s'exécutent simultanément, donc l'ordre des mises à jour n'est pas garanti comme étant séquentiel. Si vous avez besoin que les importations CSV s'exécutent l'une après l'autre, attendez qu'une importation CSV soit terminée avant d'en téléverser une seconde.
{% endalert %}

#### Statuts d'importation {#import-statuses}

Après avoir lancé votre importation, vous pouvez vérifier son statut sur la page **Import Users**.

| Statut | Description |
|---|---|
| **Complete** | Toutes les lignes ont été importées avec succès. |
| **Partial success** | Certaines lignes ont échoué. Sélectionnez le menu à trois points à côté de l'importation pour télécharger un rapport d'erreurs ou le CSV téléversé d'origine. |
| **In progress** | L'importation est en cours d'exécution. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Statuts d'importation" }

![La page Import Users montrant un statut Partial success avec le menu contextuel ouvert, affichant les options Download error report et Download uploaded CSV.]({% image_buster /assets/img/csv_import/partial_success_menu.png %})

Le rapport d'erreurs post-importation inclut les lignes qui ont échoué pour des raisons que la validation ne couvre pas, comme lorsqu'un utilisateur n'existe pas dans Braze.

{% alert important %}
Les fichiers CSV précédemment téléversés sont disponibles au téléchargement depuis la page **Import Users** pendant 14 jours après la date de téléversement. Après 14 jours, le fichier est définitivement supprimé et ne peut plus être consulté.
{% endalert %}

## Considérations relatives aux points de donnée {#data-point-considerations}

Chaque donnée client importée depuis un fichier CSV écrase la valeur existante sur les profils utilisateur et enregistre un point de donnée, à l'exception des ID externes et des valeurs vides. Si vous avez des questions sur les subtilités des points de donnée Braze, votre gestionnaire de compte Braze peut y répondre.

| Considération | Détails |
|---|---|
| ID externes | Le téléversement d'un CSV contenant uniquement des `external_id` n'enregistre pas de points de donnée. Cela vous permet de segmenter les utilisateurs Braze existants sans impacter les limites de données. Cependant, l'inclusion de champs comme `email` ou `phone` écrase les données utilisateur existantes et **enregistre** des points de donnée. <br><br>Les importations CSV utilisées uniquement pour la segmentation n'enregistrent pas de points de donnée, comme celles contenant uniquement `external_id`, `braze_id` ou `user_alias_name`. |
| Valeurs vides | Les valeurs vides dans votre CSV n'écraseront pas les données existantes du profil utilisateur. Vous n'avez pas besoin d'inclure tous les attributs utilisateur ou événements personnalisés lors de l'importation. |
| États d'abonnement | La mise à jour de `email_subscribe`, `push_subscribe`, `subscription_group_id` ou `subscription_state` **ne compte pas** dans l'utilisation des points de donnée. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Considérations relatives aux points de donnée" }

{% alert important %}
Définir `language` ou `country` sur un utilisateur via l'importation CSV ou l'API empêche Braze de capturer automatiquement ces informations via le SDK.
{% endalert %}

## Résolution des problèmes {#troubleshooting}

Si vous avez utilisé la [validation du fichier](#file-validation), commencez par le rapport d'erreurs, car il inclut le problème spécifique pour chaque ligne signalée et une description de la façon de le corriger. Pour les lignes qui ont échoué lors de l'importation plutôt que lors de la validation, téléchargez le rapport d'erreurs en survolant la ligne et en sélectionnant le bouton <i class="fas fa-download" title="Télécharger"></i> sur la page **Import Users**.

Pour la résolution des problèmes d'importation CSV, consultez les problèmes courants ci-dessous.

### Utiliser un e-mail comme `external_id` {#use-email-as-external_id}

Braze ne recommande pas d'utiliser une adresse e-mail comme `external_id`. Si vous utilisez un e-mail comme `external_id`, incluez les colonnes `external_id` et `email` dans votre CSV afin que les utilisateurs restent ciblables sur le canal e-mail. Utilisez une virgule (`,`) comme délimiteur de colonne, et non un deux-points (`:`).

### Caractères de guillemets dans les valeurs `external_id` {#quote-characters-in-external_id-values}

Si une cellule `external_id` contient un guillemet double, échappez-le en doublant le caractère (`""`), comme décrit dans [Guillemets doubles non échappés ou déséquilibrés](#missing-row). L'importation CSV n'utilise pas l'échappement par barre oblique inverse.

### L'importation CSV n'est pas disponible comme filtre de segment {#csv-import-isnt-available-as-a-segment-filter}

Vous ne pouvez utiliser une importation CSV comme filtre de segment que si vous avez activé une préférence de ciblage lors du téléversement.

Pour vérifier si la disponibilité du ciblage est activée pour une importation existante :

1. Sur la page **Import Users**, trouvez votre importation CSV.
2. Vérifiez si **Go to Segment** apparaît pour cette importation.
3. Si **Go to Segment** apparaît, votre CSV est disponible dans le filtre de segment `Updated/Imported from CSV`.
4. Si **Go to Segment** n'apparaît pas, la disponibilité du ciblage n'a pas été activée pour cette importation.

Vous ne pouvez pas activer la disponibilité du ciblage après la fin d'un téléversement CSV. Pour utiliser ce CSV comme filtre de segment, retéléversez le fichier et, à l'[étape 6 : Choisir les préférences de ciblage](#step-6-choose-targeting-preferences), sélectionnez **Create targeting filter** ou **Create targeting filter and add to new segment**.

Si votre objectif est de créer un segment sans mettre à jour les données de profil, téléversez un CSV qui ne contient que des colonnes d'identifiants (par exemple, `external_id` ou des colonnes d'identifiants d'alias), puis sélectionnez **Create targeting filter and add to new segment**.

### Problèmes de formatage du fichier {#file-formatting-issues}

#### Ligne mal formée {#malformed-row}

Si votre téléversement s'est terminé avec des erreurs, il peut y avoir une ligne mal formée dans votre fichier CSV.

Pour importer correctement les données, il doit y avoir une ligne d'en-tête. Chaque ligne doit avoir le même nombre de cellules que la ligne d'en-tête. Les lignes ayant plus ou moins de valeurs que la ligne d'en-tête seront exclues de l'importation. Les virgules dans une valeur seront interprétées comme un séparateur et peuvent provoquer cette erreur.

De plus, toutes les données doivent être encodées en UTF-8. Si le fichier est enregistré avec un encodage hérité (par exemple, certains paramètres par défaut d'Excel), les caractères spéciaux et les URL dans les cellules peuvent être corrompus et apparaître sous forme de points d'interrogation (`?`) dans Braze ou dans les messages envoyés.

Si votre fichier CSV contient des lignes vides et importe moins de lignes que le nombre total de lignes dans le fichier CSV, cela peut ne pas indiquer un problème avec l'importation puisque les lignes vides n'ont pas besoin d'être importées. Vérifiez le nombre de lignes correctement importées et assurez-vous qu'il correspond au nombre d'utilisateurs que vous essayez d'importer.

#### Ligne manquante {#missing-row}

Il y a plusieurs raisons pour lesquelles le nombre d'utilisateurs importés peut ne pas correspondre au nombre total de lignes dans votre fichier CSV :

| Problème | Résolution |
|---|---|
| ID externes, alias d'utilisateur, ID Braze, adresses e-mail ou numéros de téléphone en double | S'il y a des colonnes d'ID externes en double, cela peut provoquer des lignes mal formées ou non importées même si les lignes sont correctement formatées. Dans certains cas, cela peut ne pas signaler d'erreur spécifique. Vérifiez les doublons et supprimez-les avant de retéléverser. |
| Caractères accentués | Votre CSV peut contenir des noms ou des attributs avec des accents. Assurez-vous que le fichier est encodé en UTF-8 pour éviter les problèmes d'importation. |
| L'ID Braze appartient à un utilisateur orphelin | Si un utilisateur a été fusionné avec un autre et que Braze ne peut pas associer l'ID Braze au profil restant, la ligne ne sera pas importée. |
| Ligne vide | Les lignes vides dans le CSV peuvent provoquer des erreurs de données mal formées. Vérifiez à l'aide d'un éditeur de texte brut, pas Excel ou Sheets. |
| Guillemets doubles non échappés ou déséquilibrés (`"`) | Les guillemets doubles encadrent les valeurs de chaîne contenant des virgules. Si une valeur contient elle-même un guillemet double, échappez-le en le doublant (`""`). Les guillemets doubles non échappés ou déséquilibrés provoquent une ligne mal formée. |
| Sauts de ligne incohérents | Des sauts de ligne mixtes (par exemple, `\n` et `\r\n`) peuvent faire en sorte que la première ligne de données soit traitée comme faisant partie de l'en-tête. Utilisez un éditeur hexadécimal ou un éditeur de texte avancé pour inspecter et corriger. |
| Fichier mal encodé | Même si les accents sont autorisés, le fichier doit être encodé en UTF-8. D'autres encodages peuvent fonctionner partiellement mais ne sont pas entièrement pris en charge. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ligne manquante" }

#### Guillemets de chaîne {#string-quotation}

Les valeurs encadrées par des guillemets simples (`''`) ou doubles (`""`) seront lues comme des chaînes de caractères lors de l'importation.

#### Dates mal formatées {#incorrectly-formatted-dates}

Les dates qui ne sont pas au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) ne seront pas lues comme `datetimes` lors de l'importation.

### Problèmes de structure des données {#data-structure-issues}

#### Adresses e-mail invalides {#invalid-email-addresses}

Si votre téléversement s'est terminé avec des erreurs, il peut y avoir une ou plusieurs adresses e-mail chiffrées invalides. Confirmez que toutes les adresses e-mail sont correctement chiffrées avant de les importer dans Braze.

- **Lors de la [mise à jour ou de l'importation d'adresses e-mail]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption/#step-3-import-and-update-users)** dans Braze, utilisez la valeur e-mail hachée partout où un e-mail est inclus. Ces valeurs e-mail hachées sont fournies par votre équipe interne.
- **Lors de la création d'un nouvel utilisateur**, vous devez ajouter `email_encrypted` avec la valeur e-mail chiffrée de l'utilisateur. Sinon, Braze ne créera pas l'utilisateur. De même, si vous ajoutez une adresse e-mail à un utilisateur existant qui n'en a pas, vous devez ajouter `email_encrypted`. Sinon, Braze ne mettra pas à jour l'utilisateur.

#### Données importées comme attribut personnalisé {#data-imported-as-custom-attribute}

Si une donnée utilisateur par défaut (telle que `email` ou `first_name`) est importée comme attribut personnalisé, vérifiez la casse et l'espacement de votre fichier CSV. Par exemple, `First_name` est importé comme attribut personnalisé, tandis que `first_name` est correctement importé dans le champ « prénom » du profil d'un utilisateur.

#### Modifier le type de données d'un attribut personnalisé {#change-a-custom-attributes-data-type}

Si vous devez modifier le type de données d'un attribut personnalisé existant (par exemple, de chaîne de caractères à valeur booléenne), mettez à jour le type de données sur la page [**Attributs personnalisés**]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/) du tableau de bord avant d'importer votre CSV. Si le type de données dans votre CSV ne correspond pas au type de données actuellement défini pour l'attribut, l'importation échoue avec une erreur.

#### Types de données multiples {#multiple-data-types}

Braze s'attend à ce que chaque valeur d'une colonne soit du même type de données. Les valeurs qui ne correspondent pas au type de données de leur attribut provoquent des erreurs de segmentation.

De plus, commencer un attribut numérique par zéro causera des problèmes car les nombres commençant par zéro sont considérés comme des chaînes de caractères. Lorsque Braze convertit cette chaîne, elle peut être traitée comme une valeur octale (qui utilise les chiffres de zéro à sept), ce qui signifie qu'elle est convertie en sa valeur décimale correspondante. Par exemple, si la valeur dans le fichier CSV est 0130, le profil Braze affiche 88. Pour éviter ce problème, utilisez des attributs avec des types de données chaîne de caractères. Cependant, ce type de données n'est pas disponible dans la comparaison numérique de segmentation.

#### Types d'attributs par défaut {#default-attribute-types}

Certains attributs par défaut n'acceptent que certaines valeurs comme valides pour les mises à jour utilisateur. Pour des conseils, consultez [Construire votre CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/).

Les espaces en fin de chaîne et les différences de casse peuvent faire en sorte qu'une valeur soit interprétée comme invalide. Par exemple, dans le fichier CSV suivant, seul l'utilisateur de la première ligne (`brazetest1`) voit ses statuts e-mail et push mis à jour avec succès car les valeurs acceptées sont `unsubscribed`, `subscribed` et `opted_in`.

```plaintext
external_id,email,email_subscribe,push_subscribe
brazetest1,test1@braze.com,unsubscribed,unsubscribed
brazetest2,test2@braze.com,Unsubscribed,Unsubscribed
```

### « Sélectionner un fichier CSV » ne fonctionne pas {#select-csv-file-is-not-working}

Il y a plusieurs raisons pour lesquelles le bouton **Select CSV File** peut ne pas fonctionner :

| Problème | Résolution |
|---|---|
| Bloqueur de fenêtres contextuelles | Cela peut empêcher la page de s'afficher. Confirmez que votre navigateur autorise les fenêtres contextuelles sur le site du tableau de bord de Braze. |
| Navigateur obsolète | Assurez-vous que votre navigateur est à jour ; sinon, mettez-le à jour vers la dernière version. |
| Processus en arrière-plan | Fermez toutes les instances du navigateur, puis redémarrez votre ordinateur. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="« Sélectionner un fichier CSV » ne fonctionne pas" }