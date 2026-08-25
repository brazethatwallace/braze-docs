---
nav_title: Importer des données utilisateur et des événements CSV
article_title: Importer des données utilisateur et des événements CSV
permalink: "/csv_events/"
description: "Cet article de référence explique comment importer des données utilisateur et comment importer des événements personnalisés à l'aide de fichiers CSV."
page_type: reference
---

# Importation de données utilisateur (accès anticipé aux événements CSV) {#importing-user-data-csv-events-early-access}

> Braze propose plusieurs façons d'importer des données utilisateur dans la plateforme : SDK, API, ingestion de données cloud, intégrations de partenaires technologiques et fichiers CSV. Cet article fournit des instructions détaillées sur l'importation de données utilisateur, y compris l'[importation d'événements personnalisés via des fichiers CSV (accès anticipé)](#importing-custom-events).

{% alert important %}
N'envoyez pas d'e-mails transactionnels légalement requis vers des passerelles SMS, car il est fort probable que ces e-mails ne soient pas délivrés.

Bien que les e-mails que vous envoyez en utilisant un numéro de téléphone et le domaine de passerelle e-mail-vers-SMS du fournisseur (MM3) puissent aboutir à la réception de l'e-mail sous forme de message SMS (texte), certains fournisseurs de messagerie ne prennent pas en charge ce comportement. Par exemple, si vous envoyez un e-mail à un numéro de téléphone T-Mobile (tel que « 9999999999@tmomail.net »), votre message SMS serait envoyé au propriétaire de ce numéro de téléphone sur le réseau T-Mobile.

Même si ces e-mails ne sont pas délivrés à la passerelle SMS, ils sont tout de même comptabilisés dans votre facturation d'e-mails. Pour éviter d'envoyer des e-mails à des passerelles non prises en charge, consultez la [liste des noms de domaine de passerelle non pris en charge](https://www.fcc.gov/consumer-governmental-affairs/about-bureau/consumer-policy-division/can-spam/domain-name-downloads).
{% endalert %}


Avant de continuer, notez que Braze ne nettoie pas (ne valide pas et ne formate pas correctement) les données HTML lors de l'importation. Cela signifie que les balises de script doivent être supprimées de toutes les données d'importation destinées à la personnalisation web.

## REST API

Vous pouvez utiliser l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) pour enregistrer des événements personnalisés, des attributs utilisateur et des achats pour les utilisateurs.

## Importation CSV {#csv-import}

Vous pouvez charger et mettre à jour des profils utilisateur via des fichiers CSV depuis **Audience** > **Import Users**.

L'importation de données utilisateur à l'aide de fichiers CSV permet d'enregistrer et de mettre à jour des attributs utilisateur tels que le prénom et l'e-mail, en plus d'attributs personnalisés tels que la pointure. Vous pouvez importer un CSV en spécifiant l'un des deux identifiants utilisateur uniques : un `external_id` ou un alias d'utilisateur.

{% alert important %}
L'importation d'utilisateurs prend également en charge l'enregistrement et la mise à jour d'événements personnalisés utilisateur. Comme pour les attributs utilisateur, vous pouvez importer avec un `external_id`, un `braze_id` ou avec `user_alias_name` et `user_alias_label`. Pour plus de détails, consultez [Importer des événements personnalisés](#importing-custom-events).
{% endalert %}

{% alert note %}
Si vous chargez un mélange d'utilisateurs avec un `external_id` et d'utilisateurs sans, vous devez créer un fichier CSV pour chaque importation. Un même fichier CSV ne peut pas contenir à la fois des `external_ids` et des alias d'utilisateur.
{% endalert %}

### Importation avec un ID externe {#importing-with-external-id}

Lors de l'importation de vos données client, vous devez spécifier l'identifiant unique de chaque client, également appelé `external_id`. Avant de commencer votre importation CSV, il est important de comprendre auprès de votre équipe d'ingénierie comment les utilisateurs seront identifiés dans Braze. En général, il s'agit d'un ID de base de données interne. Celui-ci doit correspondre à la manière dont les utilisateurs seront identifiés par le SDK Braze sur mobile et web, et est conçu pour que chaque client dispose d'un seul profil utilisateur dans Braze sur l'ensemble de ses appareils. En savoir plus sur le [cycle de vie du profil utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle) Braze.

Lorsque vous fournissez un `external_id` dans votre importation, Braze mettra à jour tout utilisateur existant avec le même `external_id` ou créera un nouvel utilisateur identifié avec cet `external_id` défini si aucun n'est trouvé.

- **Télécharger :** [Modèle d'importation CSV d'attributs][import_template]
- **Télécharger :** [Modèle d'importation CSV d'événements][events_template]

### Importation avec un alias d'utilisateur {#importing-with-user-alias}

Pour cibler des utilisateurs qui n'ont pas d'`external_id`, vous pouvez importer une liste d'utilisateurs avec des alias d'utilisateur. Un alias sert d'identifiant utilisateur unique alternatif et peut être utile si vous essayez de cibler des utilisateurs anonymes qui ne se sont pas inscrits ou n'ont pas créé de compte sur votre application.

Si vous chargez ou mettez à jour des profils utilisateur qui sont uniquement des alias, vous devez avoir les deux colonnes suivantes dans votre CSV :

- `user_alias_name` : un identifiant utilisateur unique ; une alternative à l'`external_id`
- `user_alias_label` : un libellé commun permettant de regrouper les alias d'utilisateur

| user_alias_name | user_alias_label | last_name | email | sample_attribute |
| --- | --- | --- | --- | --- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Lorsque vous fournissez à la fois un `user_alias_name` et un `user_alias_label` dans votre importation, Braze mettra à jour tout utilisateur existant avec les mêmes `user_alias_name` et `user_alias_label`. Si aucun utilisateur n'est trouvé, Braze créera un nouvel utilisateur identifié avec ce `user_alias_name` défini.

{% alert important %}
Vous ne pouvez pas utiliser une importation CSV pour mettre à jour un utilisateur existant avec un `user_alias_name` s'il possède déjà un `external_id`. À la place, cela créera un nouveau profil utilisateur avec le `user_alias_name` associé. Pour associer un utilisateur uniquement alias à un `external_id`, utilisez l'[endpoint Identifier les utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_identify).
{% endalert %}

- **Télécharger :** [Modèle d'importation CSV d'attributs d'alias][template_alias_attributes]
- **Télécharger :** [Modèle d'importation CSV d'événements d'alias][template_alias_events]

### Importation avec un Braze ID {#importing-with-braze-id}

Pour mettre à jour des profils utilisateur existants dans Braze en utilisant une valeur interne de Braze ID au lieu d'un `external_id` ou d'un `user_alias_name` et `user_alias_label`, spécifiez `braze_id` comme en-tête de colonne.

Cela peut être utile si vous avez exporté des données utilisateur depuis Braze via notre option d'exportation CSV dans la segmentation et que vous souhaitez ajouter un nouvel attribut personnalisé à ces utilisateurs existants.

{% alert important %}
Vous ne pouvez pas utiliser une importation CSV pour créer un nouvel utilisateur à l'aide d'un `braze_id`. Cette méthode ne peut être utilisée que pour mettre à jour des utilisateurs préexistants sur la plateforme Braze.
{% endalert %}

{% alert tip %}
La valeur `braze_id` peut être libellée `Appboy ID` dans les exportations CSV depuis le tableau de bord de Braze. Cet ID sera identique au `braze_id` d'un utilisateur, vous pouvez donc renommer cette colonne en `braze_id` lorsque vous réimportez le CSV.
{% endalert %}

### Importation d'attributs par défaut {#importing-default-attributes}

Pour importer des attributs par défaut pour les utilisateurs, accédez à **Import Users** > **Attributes**. Les attributs utilisateur par défaut sont des clés réservées dans Braze. Par exemple, `first_name` ou `email`. Les attributs personnalisés sont propres à votre activité. Par exemple, une application de réservation de voyages peut avoir un attribut personnalisé appelé `last_destination_searched`.

{% alert important %}
Lors de l'importation de données client en tant qu'attributs, les en-têtes de colonne que vous utilisez doivent correspondre exactement à l'orthographe et à la casse des attributs utilisateur par défaut. Dans le cas contraire, Braze créera automatiquement un attribut personnalisé sur le profil de cet utilisateur.
{% endalert %}

#### En-têtes de colonne des données utilisateur par défaut {#default-user-data-column-headers}

| CHAMP DU PROFIL UTILISATEUR | TYPE DE DONNÉE | INFORMATIONS | OBLIGATOIRE |
|---|---|---|---|
| `external_id` | String | Un identifiant utilisateur unique pour votre client. | Oui, voir la [note suivante](#about-external-ids). |
| `user_alias_name` | String | Un identifiant utilisateur unique pour les utilisateurs anonymes. Une alternative à l'`external_id`. | Non, voir la [note suivante](#about-external-ids). |
| `user_alias_label` | String | Un libellé commun permettant de regrouper les alias d'utilisateur. | Oui, si `user_alias_name` est utilisé. |
| `first_name` | String | Le prénom de vos utilisateurs tel qu'ils l'ont indiqué (par exemple, `Jane`). | Non |
| `last_name` | String | Le nom de famille de vos utilisateurs tel qu'ils l'ont indiqué (par exemple, `Doe`). | Non |
| `email` | String | L'e-mail de vos utilisateurs tel qu'ils l'ont indiqué (par exemple, `jane.doe@braze.com`). | Non |
| `country` | String | Les codes pays doivent être transmis à Braze selon la norme ISO-3166-1 alpha-2 (par exemple, `GB`). | Non |
| `dob` | String | Doit être transmis au format « AAAA-MM-JJ » (par exemple, `1980-12-21`). Cela importera la date de naissance de votre utilisateur et vous permettra de cibler les utilisateurs dont l'anniversaire est « aujourd'hui ». | Non |
| `gender` | String | « M », « F », « O » (autre), « N » (non applicable), « P » (préfère ne pas dire) ou nil (inconnu). | Non |
| `home_city` | String | La ville de résidence de vos utilisateurs telle qu'ils l'ont indiquée (par exemple, `London`). | Non |
| `language` | String | La langue doit être transmise à Braze selon la norme ISO-639-1 (par exemple, `en`). <br>Consultez notre [liste des langues acceptées]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes). | Non |
| `phone` | String | Un numéro de téléphone tel qu'indiqué par vos utilisateurs, au format `E.164` (par exemple, `+442071838750`). <br> Consultez [Numéros de téléphone des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers) pour les consignes de formatage. | Non |
| `email_open_tracking_disabled` | Boolean | true ou false acceptés. Définissez sur true pour désactiver l'ajout du pixel de suivi d'ouverture à tous les futurs e-mails envoyés à cet utilisateur. | Non |
| `email_click_tracking_disabled` | Boolean | true ou false acceptés. Définissez sur true pour désactiver le suivi des clics pour tous les liens dans les futurs e-mails envoyés à cet utilisateur. | Non |
| `email_subscribe` | String | Les valeurs disponibles sont `opted_in` (explicitement inscrit pour recevoir des e-mails), `unsubscribed` (explicitement désabonné des e-mails) et `subscribed` (ni inscrit ni désabonné). | Non |
| `push_subscribe` | String | Les valeurs disponibles sont `opted_in` (explicitement inscrit pour recevoir des notifications push), `unsubscribed` (explicitement désabonné des notifications push) et `subscribed` (ni inscrit ni désabonné). | Non |
| `time_zone` | String | Le fuseau horaire doit être transmis à Braze dans le même format que la base de données des fuseaux horaires IANA (par exemple, `America/New_York` ou `Eastern Time (US & Canada)`). | Non |
| `date_of_first_session` <br><br> `date_of_last_session`| String | Peut être transmis dans l'un des formats ISO-8601 suivants : {::nomarkdown} <ul> <li> « AAAA-MM-JJ » </li> <li> « AAAA-MM-JJTHH:MM:SS+00:00 » </li> <li> « AAAA-MM-JJTHH:MM:SSZ » </li> <li> « AAAA-MM-JJTHH:MM:SS » (par exemple, 2019-11-20T18:38:57) </li> </ul> {:/} | Non |
| `subscription_group_id` | String | L'`id` de votre groupe d'abonnement. Cet identifiant se trouve sur la page des groupes d'abonnement de votre tableau de bord. | Non |
| `subscription_state` | String | Le statut d'abonnement pour le groupe d'abonnement spécifié par `subscription_group_id`. Les valeurs autorisées sont `unsubscribed` (pas dans le groupe d'abonnement) ou `subscribed` (dans le groupe d'abonnement). | Non, mais fortement recommandé si `subscription_group_id` est utilisé. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

##### À propos des ID externes {#about-external-ids}

Bien que l'`external_id` ne soit pas obligatoire, vous **devez** inclure l'un de ces champs :
- `external_id` : un identifiant utilisateur unique pour votre client, **ou**
- `braze_id` : un identifiant utilisateur unique récupéré pour les utilisateurs Braze existants, **ou**
- `user_alias_name` et `user_alias_label` : un identifiant utilisateur unique pour un utilisateur anonyme

### Importation d'attributs personnalisés {#importing-custom-attributes}

Vous pouvez importer des attributs personnalisés pour les utilisateurs en accédant à **Import Users** > **Attributes**. Tout en-tête qui ne correspond pas exactement à un attribut par défaut créera un attribut personnalisé dans Braze.

Les types de données suivants sont acceptés lors de l'importation d'utilisateurs :

| Type de donnée | Description |
|-----------|-------------|
| Datetime | Doit être stocké au format ISO-8601 |
| Boolean | TRUE ou FALSE |
| Number | Entier ou float sans espaces ni virgules ; les floats doivent utiliser un point (.) comme séparateur décimal |
| String | Peut contenir des virgules à condition que des guillemets doubles entourent la valeur de la colonne |
| Vide | Les valeurs vides n'écraseront pas les valeurs existantes du profil utilisateur, et vous n'avez pas besoin d'inclure tous les attributs utilisateur existants dans votre fichier CSV |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Les tableaux et les jetons de notification push ne sont pas pris en charge dans l'importation d'utilisateurs. En particulier pour les tableaux, les virgules de votre fichier CSV seront interprétées comme des séparateurs de colonnes, de sorte que toute virgule dans les valeurs entraînera des erreurs lors de l'analyse du fichier. <br>Pour charger ce type de valeurs, utilisez l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) ou l'[ingestion de données cloud]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion).
{% endalert %}

### Mise à jour du statut des groupes d'abonnement {#updating-subscription-group-status}

Vous pouvez ajouter des utilisateurs à des groupes d'abonnement e-mail ou SMS via l'importation d'utilisateurs. C'est particulièrement utile pour le SMS, car un utilisateur doit être inscrit dans un groupe d'abonnement SMS pour recevoir des messages via le canal SMS. Pour plus d'informations, consultez [Groupes d'abonnement SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group#subscription-group-mms-enablement).

Si vous mettez à jour le statut d'un groupe d'abonnement, vous devez avoir les deux colonnes suivantes dans votre CSV :

- `subscription_group_id` : l'`id` du [groupe d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#subscription-groups).
- `subscription_state` : les valeurs disponibles sont `unsubscribed` (pas dans le groupe d'abonnement) ou `subscribed` (dans le groupe d'abonnement).

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg" aria-label="Mise à jour du statut des groupes d'abonnement">
<thead>
  <tr>
    <th class="tg-0pky">external_id</th>
    <th class="tg-0pky">first_name</th>
    <th class="tg-0pky">subscription_group_id</th>
    <th class="tg-0pky">subscription_state</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">A8i3mkd99</td>
    <td class="tg-0pky">Colby</td>
    <td class="tg-0pky">6ff593d7-cf69-448b-aca9-abf7d7b8c273</td>
    <td class="tg-0pky">subscribed</td>
  </tr>
  <tr>
    <td class="tg-0pky">k2LNhj8Ks</td>
    <td class="tg-0pky">Tom</td>
    <td class="tg-0pky">aea02307-a91e-4bc0-abad-1c0bee817dfa</td>
    <td class="tg-0pky">subscribed</td>
  </tr>
</tbody>
</table>

{% alert important %}
Un seul `subscription_group_id` peut être défini par ligne dans l'importation d'utilisateurs. Différentes lignes peuvent avoir des valeurs `subscription_group_id` différentes. Cependant, si vous devez inscrire les mêmes utilisateurs dans plusieurs groupes d'abonnement, vous devrez effectuer plusieurs importations.
{% endalert %}

### Importation d'événements personnalisés (accès anticipé) {#importing-custom-events}

{% alert important %}
L'importation d'événements personnalisés est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l'accès anticipé.
{% endalert %}

Pour importer des événements personnalisés pour vos utilisateurs, accédez à **Import Users** > **Events**.

Les événements personnalisés sont propres à votre activité. Par exemple, une application de streaming peut avoir un événement personnalisé appelé rented_movie. Votre CSV doit contenir des en-têtes de colonne pour :

- L'un des éléments suivants :
  - `external_id`, **ou**
  - `braze_id`, **ou**
  - `user_alias_name` et `user_alias_label`
- Name
- Time

Les événements personnalisés peuvent avoir des propriétés d'événement. Par exemple, l'événement personnalisé rented_movie peut avoir les propriétés title et genre. Ces propriétés d'événement doivent avoir un en-tête de colonne au format `<event_name>.properties.<property name>`. Par exemple, `rented_movie.properties.title`.

| CHAMP DU PROFIL UTILISATEUR | TYPE DE DONNÉE | INFORMATIONS | OBLIGATOIRE |
|-----------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `external_id` | String | Un identifiant utilisateur unique pour votre utilisateur. | Oui, l'un des suivants est obligatoire : `external_id`, `braze_id`, ou `user_alias_name` et `user_alias_label`. |
| `braze_id` | String | Un identifiant attribué par Braze pour votre utilisateur. | Oui, l'un des suivants est obligatoire : `external_id`, `braze_id`, ou `user_alias_name` et `user_alias_label`. |
| `user_alias_name` | String | Un identifiant utilisateur unique pour les utilisateurs anonymes. Une alternative à l'external_id. | Oui, l'un des suivants est obligatoire : `external_id`, `braze_id`, ou `user_alias_name` et `user_alias_label`. |
| `user_alias_label` | String | Un libellé commun permettant de regrouper les alias d'utilisateur. | Oui, l'un des suivants est obligatoire : `external_id`, `braze_id`, ou `user_alias_name` et `user_alias_label`. |
| `name` | String | Un événement personnalisé de vos utilisateurs. | Oui |
| `time` | String | L'heure de l'événement. Peut être transmis dans l'un des formats ISO-8601 suivants : {::nomarkdown} <ul> <li> « AAAA-MM-JJ » </li> <li> « AAAA-MM-JJTHH:MM:SS+00:00 » </li> <li> « AAAA-MM-JJTHH:MM:SSZ » </li> <li> « AAAA-MM-JJTHH:MM:SS » (par exemple, 2019-11-20T18:38:57) </li> </ul> {:/} | Oui |
| `<event name>.properties.<property name>` | Multiple | Une propriété d'événement associée à un événement personnalisé. Par exemple, `rented_movie.properties.title` | Non |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Bien que l'external_id en lui-même ne soit pas obligatoire, vous devez inclure l'un des champs suivants : <br>- `external_id` : un identifiant utilisateur unique pour votre client <br>- `braze_id` : un identifiant utilisateur unique récupéré pour les utilisateurs Braze existants <br>- `user_alias_name` : un identifiant utilisateur unique pour un utilisateur anonyme
{% endalert %}

#### Taille du CSV {#csv-size}

Braze accepte les données utilisateur au format CSV standard à partir de fichiers d'une taille maximale de 500 Mo. Pour télécharger l'un de nos modèles de fichier CSV, consultez [Importation avec un ID externe](#importing-with-external-id) ou [Importation avec un alias d'utilisateur](#importing-with-user-alias).

#### Considérations relatives aux points de donnée {#data-point-considerations}

Chaque donnée client importée via CSV écrasera la valeur existante dans les profils utilisateur et sera comptabilisée comme un point de donnée, à l'exception des ID externes et des valeurs vides.

- Les ID externes chargés via l'importation CSV ne consommeront pas de points de donnée. Si vous chargez un fichier CSV pour segmenter des utilisateurs Braze existants en ne chargeant que des ID externes, cela peut être fait sans consommer de points de donnée. Si vous ajoutiez des données supplémentaires telles que l'e-mail ou le numéro de téléphone d'un utilisateur dans votre importation, cela écraserait les données utilisateur existantes et consommerait vos points de donnée.
    - Les importations CSV à des fins de segmentation (importations effectuées avec `external_id`, `braze_id` ou `user_alias_name` comme seul champ) ne consommeront pas de points de donnée.
- Les valeurs vides n'écraseront pas les valeurs existantes du profil utilisateur, et vous n'avez pas besoin d'inclure tous les attributs utilisateur existants ou événements personnalisés dans votre fichier CSV.
- La mise à jour de `email_subscribe`, `push_subscribe`, `subscription_group_id` ou `subscription_state` ne sera pas comptabilisée dans la consommation de points de donnée.

{% alert important %}
Définir la langue ou le pays d'un utilisateur via l'importation CSV ou l'API empêchera Braze de capturer automatiquement ces informations via le SDK.
{% endalert %}

## Importation d'un CSV {#importing-a-csv}

Pour importer votre fichier CSV :
1. Allez dans **Audience** > **Import Users**.
2. Sélectionnez **Browse Files** et choisissez le fichier souhaité, puis sélectionnez **Start import**. Braze téléchargera votre fichier et vérifiera les en-têtes de colonnes ainsi que les types de données de chaque colonne.

{% alert important %}
Les importations CSV sont sensibles à la casse. Cela signifie que les lettres majuscules dans les importations CSV enregistreront le champ comme un attribut personnalisé plutôt que comme un attribut standard. Par exemple, « email » est correct, mais « Email » serait enregistré comme un attribut personnalisé.
{% endalert %}

![L'option « Events » est sélectionnée comme type d'informations utilisateur à importer.][5]

Une fois le téléchargement terminé, vous pouvez afficher un aperçu du contenu de votre fichier. Les informations du tableau sont basées sur les valeurs des premières lignes de votre fichier CSV.

Vous pouvez suivre la progression sur la page **Import Users**, qui s'actualise toutes les cinq secondes, ou lorsque vous sélectionnez **Refresh table**. Vous pouvez continuer à utiliser le reste du tableau de bord de Braze pendant l'importation, et vous recevrez des notifications lorsque l'importation commence et se termine.

Vous pouvez également consulter vos importations les plus récentes, leurs noms de fichiers, le type de CSV, le nombre de lignes dans le fichier, le nombre de lignes importées avec succès, le nombre total de lignes dans chaque fichier et le statut de chaque importation.

Vous pouvez importer plusieurs fichiers CSV en même temps. Les importations CSV s'exécutent simultanément, ce qui signifie que l'ordre des mises à jour n'est pas garanti comme étant séquentiel. Si vous avez besoin que les importations CSV s'exécutent l'une après l'autre, vous devez attendre qu'une importation CSV soit terminée avant d'en télécharger une deuxième.

Si le processus d'importation rencontre une erreur, une icône d'avertissement apparaîtra à côté du nombre total de lignes dans le fichier. Vous pouvez survoler l'icône pour voir les détails sur les raisons de l'échec de certaines lignes. Une fois l'importation terminée, toutes les données seront ajoutées aux profils existants, ou de nouveaux profils seront créés.

![Téléchargement du fichier CSV terminé avec des erreurs liées à des types de données mixtes dans une seule colonne][4]{: style="max-width:70%"}

### Considérations {#considerations}

Si Braze détecte un élément mal formé dans les premières lignes de votre fichier lors du téléchargement, ces erreurs seront affichées avec le résumé. Par exemple, si votre fichier contient une ligne mal formée, cette erreur sera signalée dans l'aperçu lorsque vous importerez le fichier. Bien qu'un fichier puisse être importé avec des erreurs, il est recommandé de corriger ces erreurs dans votre fichier avant de poursuivre l'importation.

De plus, il est important d'examiner l'intégralité du fichier CSV avant le téléchargement, car Braze n'analyse pas chaque ligne du fichier d'entrée pour l'aperçu. Cela signifie que des erreurs peuvent exister sans que Braze ne les détecte lors de la génération de cet aperçu.

Les lignes mal formées et les lignes sans ID externe ne seront pas importées. Toutes les autres erreurs peuvent être importées, mais peuvent interférer avec le filtrage lors de la création d'un Segment. Pour plus d'informations, passez à la section [Résolution des problèmes](#troubleshooting).

{% alert warning %}
Les erreurs sont basées uniquement sur le type de données et la structure du fichier. Par exemple, une adresse e-mail mal formatée serait tout de même importée, car elle peut encore être analysée comme une chaîne de caractères.
{% endalert %}

### Importation CSV d'utilisateurs via Lambda {#lambda-user-csv-import}

Vous pouvez utiliser notre script Lambda S3 serverless d'importation CSV pour télécharger des attributs utilisateur vers la plateforme. Cette solution fonctionne comme un outil de téléchargement de CSV : vous déposez vos fichiers CSV dans un compartiment S3, et les scripts les téléchargent via notre API.

Les temps d'exécution estimés pour un fichier d'un million de lignes sont d'environ cinq minutes. Pour plus d'informations, consultez [Importation CSV d'attributs utilisateur vers Braze]({{site.baseurl}}/user_csv_lambda).

## Segmentation {#segmenting}

L'importation d'utilisateurs crée et met à jour les profils utilisateur, et peut également être utilisée pour créer des Segments. Pour créer un Segment, sélectionnez **Automatically generate a segment from the users who are imported from this CSV** avant de lancer l'importation.

Vous pouvez définir le nom du Segment ou accepter la valeur par défaut, qui correspond au nom de votre fichier. Les fichiers utilisés pour créer un Segment comporteront un lien permettant de consulter le Segment une fois l'importation terminée.

Le filtre utilisé pour créer le Segment sélectionne les utilisateurs qui ont été créés ou mis à jour lors d'une importation donnée, et il est disponible avec tous les autres filtres sur la page de modification du Segment.

## Résolution des problèmes {#troubleshooting}

### Lignes manquantes {#missing-rows}

Il existe plusieurs raisons pour lesquelles le nombre d'utilisateurs importés peut ne pas correspondre au nombre total de lignes dans votre fichier CSV :

- **ID externes en double :** S'il y a des colonnes d'ID externe en double, cela peut provoquer des lignes mal formées ou non importées même si les lignes sont correctement formatées. Dans certains cas, cela peut ne pas signaler d'erreur spécifique. Vérifiez s'il y a des ID externes en double dans votre CSV. Si c'est le cas, supprimez les doublons et essayez de charger à nouveau.
- **Caractères accentués :** Votre fichier CSV peut contenir des noms ou des attributs qui incluent des accents. Assurez-vous que votre fichier est encodé en UTF-8 pour éviter tout problème.

### Ligne mal formée {#malformed-row}

Vous devez inclure une ligne d'en-tête dans votre fichier CSV pour importer correctement vos données. Chaque ligne doit avoir le même nombre de cellules que la ligne d'en-tête. Les lignes ayant plus ou moins de valeurs que la ligne d'en-tête seront exclues de l'importation. Les virgules dans une valeur seront interprétées comme un séparateur et peuvent provoquer cette erreur. De plus, toutes les données doivent être encodées en UTF-8.

Si votre fichier CSV contient des lignes vides et importe moins de lignes que le nombre total de lignes dans le fichier CSV, cela peut ne pas indiquer un problème avec l'importation puisque les lignes vides n'ont pas besoin d'être importées. Vérifiez le nombre de lignes correctement importées et assurez-vous qu'il correspond au nombre d'utilisateurs que vous essayez d'importer.

### Types de données multiples {#multiple-data-types}

Braze s'attend à ce que chaque valeur d'une colonne soit du même type de données. Les valeurs qui ne correspondent pas au type de données de leur attribut provoqueront des erreurs lors de la segmentation.

### Dates mal formatées {#incorrectly-formatted-dates}

Les dates qui ne sont pas au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) ne seront pas lues comme des dates/heures lors de l'importation.

### Guillemets de chaîne de caractères {#string-quotation}

Les valeurs encapsulées dans des guillemets simples ('') ou doubles ("") seront lues comme des chaînes de caractères lors de l'importation.

### Données importées comme attribut personnalisé {#data-imported-as-custom-attribute}

Si vous constatez qu'une donnée utilisateur par défaut (par exemple, `email` ou `first_name`) est importée comme un attribut personnalisé, vérifiez la casse et l'espacement de votre fichier CSV. Par exemple, `First_name` serait importé comme un attribut personnalisé, tandis que `first_name` serait correctement importé dans le champ « prénom » du profil d'un utilisateur.

[import_template]: {% image_buster /assets/unlisted_docs/download_file/braze-user-import-template-csv.xlsx %}
[events_template]: {% image_buster /assets/unlisted_docs/download_file/braze-csv-events-import-template.csv %}
[template_alias_attributes]: {% image_buster /assets/unlisted_docs/download_file/braze-user-import-alias-template-csv.xlsx %}
[template_alias_events]: {% image_buster /assets/unlisted_docs/download_file/braze-events-csv-example-user-alias.csv %}
[3]: {% image_buster /assets/unlisted_docs/img/importcsv5.png %}
[4]: {% image_buster /assets/unlisted_docs/img/importcsv2.png %}
[5]: {% image_buster /assets/unlisted_docs/img/importcsv3.png %}
[7]: {% image_buster /assets/unlisted_docs/img/segment-imported-users.png %}
[8]: {% image_buster /assets/unlisted_docs/img_archive/user_alias_import_1.png %}
[9]: {% image_buster /assets/unlisted_docs/img/subscription_group_import.png %}