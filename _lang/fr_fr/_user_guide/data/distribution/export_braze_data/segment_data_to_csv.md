---
nav_title: Données de segment
article_title: Exporter les données de segment
page_order: 4
page_type: reference
description: "Cet article de référence explique comment exporter les données d'un segment au format CSV, les autorisations requises pour exporter les données utilisateur, les exportations d'étapes Canvas et les champs inclus dans l'exportation."

---

# Exporter les données de segment au format CSV {#export-segment-data-to-csv}

> Cette page explique comment demander une exportation CSV des données utilisateur d'un segment, ainsi que les données incluses dans l'exportation.

{% alert note %}
Les options d'exportation CSV apparaissent dans le menu déroulant **User Data** uniquement pour les utilisateurs de l'entreprise disposant de l'[autorisation « Exporter les données utilisateur en CSV »]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) pour cet espace de travail.
{% endalert %}

Pour exporter les données d'un segment vers un fichier CSV, sélectionnez le menu déroulant **User Data** lorsque vous modifiez un segment et choisissez d'exporter soit les données utilisateur, soit les adresses e-mail pour le segment.

![Section Détails du segment avec le menu déroulant User Data affichant les options d'exportation.]({% image_buster /assets/img_archive/csvexport.png %})

Vous pouvez également demander une exportation CSV à partir de la page principale **Segments** en sélectionnant le menu déroulant <i class="fas fa-gear" aria-label="Paramètres"></i> **Settings** pour un segment :

![Menu déroulant Settings sur la page principale des Segments.]({% image_buster /assets/img_archive/csvexport2.png %})

{% alert tip %}
Pour exporter les données de tous vos profils utilisateurs, créez un segment sans filtre, puis demandez une exportation CSV.
{% endalert %}

Le fichier CSV contient les données de chaque profil utilisateur capturé dans le segment au moment de l'exportation. Vous pouvez exporter n'importe quel segment en sélectionnant l'icône d'engrenage, puis l'exportation CSV. Braze génère le rapport en arrière-plan et l'envoie par e-mail à l'utilisateur actuellement connecté.

## Détails de l'exportation CSV de segment {#segment-csv-export-details}

{% alert note %}
Les utilisateurs du tableau de bord doivent disposer de l'autorisation **Exporter les données utilisateur** pour utiliser les options d'exportation CSV. S'ils ne disposent pas de cette autorisation, les options d'exportation CSV n'apparaissent pas.
{% endalert %}

**Exporter les adresses e-mail en CSV** inclut uniquement les lignes des utilisateurs du segment qui possèdent une adresse e-mail. Par exemple, si votre segment contient 100 000 utilisateurs mais que seulement 50 000 ont une adresse e-mail, **Exporter les adresses e-mail en CSV** produit environ 50 000 lignes. **Exporter les données utilisateur en CSV** exporte toutes les données utilisateur du segment.

{% alert important %}
En raison des limites de taille de fichier, votre exportation peut échouer si la taille estimée de votre segment dépasse 500 000 utilisateurs. Notez que cette restriction est basée sur la taille estimée de votre segment, et non sur le calcul exact. Pour plus de détails, reportez-vous à la section [Exporter des segments volumineux](#exporting-large-segments).
{% endalert %}

Si vous avez lié vos [identifiants Amazon S3]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/#amazon-s3-integration) à Braze, le fichier CSV sera téléchargé dans votre compartiment S3 sous la clé `segment-export/SEGMENT_ID/YYYY-MM-dd/users-RANDOMSTRING.zip`. Vous devez être connecté au tableau de bord pour accéder au lien de téléchargement qui vous a été envoyé par e-mail.

{% multi_lang_include alerts/important_alerts.md alert='S3 file bucket export' %}

## Données incluses dans l'exportation {#data-included-in-export}

Les éléments suivants sont inclus dans votre exportation en fonction de votre sélection.

### Exporter les données utilisateur en CSV {#csv-export-user-data}

| Nom du champ                | Description                                              |
| --------------------------- | -------------------------------------------------------- |
| Appboy ID                   | ID interne (non modifiable)                              |
| country                     | Pays                                                     |
| created_at                  | Date et heure de création du profil utilisateur          |
| created_from                | Méthode utilisée pour créer le profil utilisateur (par exemple, REST API, SDK ou importation CSV) |
| devices                     | Informations sur l'appareil                              |
| date_of_birth               | Date de naissance                                        |
| email                       | Adresse e-mail                                           |
| unsubscribed_from_emails_at | Date de désabonnement aux e-mails                        |
| user_id                     | ID externe                                               |
| first_name                  | Prénom                                                   |
| first_session               | Date et heure de la première session                     |
| gender                      | Genre                                                    |
| google_ad_ids               | ID publicitaires Google associés à l'utilisateur         |
| city                        | Ville                                                    |
| IDFAs                       | Valeurs de l'identifiant pour la publicité (IDFA)        |
| IDFVs                       | Valeurs de l'identifiant du fournisseur (IDFV)           |
| language                    | Langue dans la norme ISO-639-1                           |
| last_app_version_used       | Dernière version de l'application utilisée               |
| last_name                   | Nom                                                      |
| last_session                | Date et heure de la dernière session                     |
| number_of_google_ad_ids     | Nombre d'ID publicitaires Google associés                |
| number_of_IDFAs             | Nombre d'IDFA associés                                   |
| number_of_IDFVs             | Nombre d'IDFV associés                                   |
| number_of_push_tokens       | Nombre de jetons de notification push associés           |
| number_of_roku_ad_ids       | Nombre d'ID publicitaires Roku associés                  |
| number_of_windows_ad_ids    | Nombre d'ID publicitaires Windows associés               |
| phone_number                | Numéro de téléphone                                      |
| opted_into_push_at          | Date d'abonnement aux notifications push                 |
| unsubscribed_from_push_at   | Date de désabonnement aux notifications push             |
| random_bucket               | Numéro de compartiment aléatoire                         |
| roku_ad_ids                 | ID publicitaires Roku                                    |
| session_count               | Nombre total de sessions                                 |
| timezone                    | Fuseau horaire de l'utilisateur dans le même format que la base de données des fuseaux horaires de l'IANA |
| in_app_purchase_total       | Montant total dépensé en achats in-app                   |
| user_aliases                | Alias de l'utilisateur, le cas échéant                   |
| windows_ad_ids              | ID publicitaires Windows                                 |
| Custom events               | En fonction de la sélection à l'exportation              |
| Custom attributes           | En fonction de la sélection à l'exportation              |
{: .reset-td-br-1 .reset-td-br-2 aria-label="CSV export user data" }

{% alert note %}
Lorsque vous exportez les données utilisateur d'une étape Canvas, le fichier CSV inclut tous les utilisateurs qui sont passés par cette étape au cours de la durée de vie de l'étape Canvas. Vous ne pouvez pas limiter l'exportation à une plage de dates ou à une autre fenêtre temporelle. Pour savoir comment effectuer ces exportations, consultez [Exporter les données Canvas]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data/).
{% endalert %}

### Exporter les adresses e-mail en CSV {#csv-export-email-addresses}

| Nom du champ                | Description                        |
| --------------------------- | ---------------------------------- |
| user_id                     | ID externe de l'utilisateur        |
| first_name                  | Prénom                             |
| last_name                   | Nom                                |
| email                       | E-mail                             |
| unsubscribed_from_emails_at | Date de désabonnement aux e-mails  |
| opted_in_to_emails_at       | Date d'abonnement aux e-mails     |
| user_aliases                | Alias de l'utilisateur, le cas échéant |
{: .reset-td-br-1 .reset-td-br-2 aria-label="CSV Export Email Addresses" }

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, consultez notre article de [résolution des problèmes]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/).
{% endalert %}

{% alert note %}
Les données des groupes d'abonnement ne sont pas disponibles via les exportations de segment. Pour identifier les utilisateurs par statut d'abonnement, créez un segment distinct basé sur l'appartenance à un groupe d'abonnement et exportez ce segment.
{% endalert %}

## Exporter des segments volumineux {#exporting-large-segments}

Il existe plusieurs méthodes pour exporter un segment d'utilisateurs volumineux contenant plus de 500 000 utilisateurs.

{% tabs %}
{% tab Segments multiples %}

Vous pouvez diviser un segment volumineux en segments plus petits, puis exporter chacun d'entre eux depuis Braze.

{% endtab %}
{% tab Numéros de compartiment aléatoire %}

Vous pouvez également utiliser des [numéros de compartiment aléatoire]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/) pour diviser votre base d'utilisateurs en plusieurs segments, puis les combiner après l'exportation. Par exemple, si vous devez diviser votre segment en deux, vous pouvez le faire avec les filtres suivants :
- Segment 1 : le numéro de compartiment aléatoire est inférieur à 5 000 (inclut 0-4999)
- Segment 2 : le numéro de compartiment aléatoire est supérieur à 4999 (inclut 5000-9999)

{% endtab %}
{% tab Endpoints %}

Vous pouvez également tirer parti des endpoints suivants pour exporter les données utilisateur d'un segment spécifique. Notez que ces endpoints sont soumis à des limites de données et à des [limites de débit]({{site.baseurl}}/api/basics/).
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)

Si vous avez connecté vos [identifiants Amazon S3]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/#amazon-s3-integration), les exportations volumineuses peuvent être livrées dans votre compartiment en plus du lien de téléchargement envoyé par e-mail, comme décrit dans [Détails de l'exportation CSV de segment](#segment-csv-export-details).

{% endtab %}
{% endtabs %}