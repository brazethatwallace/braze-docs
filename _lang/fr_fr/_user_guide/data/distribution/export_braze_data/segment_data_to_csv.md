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
Les options d'exportation CSV apparaissent dans le menu déroulant **User Data** uniquement pour les utilisateurs de l'entreprise disposant de l'[autorisation « Exporter les données utilisateur »]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) pour cet espace de travail.
{% endalert %}

Pour exporter les données d'un segment vers un fichier CSV, sélectionnez le menu déroulant **User Data** lorsque vous modifiez un segment et choisissez d'exporter soit les données utilisateur, soit les adresses e-mail pour le segment.

![Section Détails du segment avec le menu déroulant User Data affichant les options d'exportation.]({% image_buster /assets/img_archive/csvexport.png %})

Vous pouvez également demander une exportation CSV à partir de la page principale **Segments** en sélectionnant le menu déroulant <i class="fas fa-gear" aria-label="Paramètres"></i> **Settings** pour un segment :

![Menu déroulant Settings sur la page principale des Segments.]({% image_buster /assets/img_archive/csvexport2.png %})

{% alert tip %}
Pour exporter les données de tous vos profils utilisateurs, créez un segment sans filtre, puis demandez une exportation CSV.
{% endalert %}

Le fichier CSV contient les données de chaque profil utilisateur capturé dans le segment au moment de l'exportation. Vous pouvez exporter n'importe quel segment en sélectionnant l'icône d'engrenage, puis l'exportation CSV. Braze génère le rapport en arrière-plan et l'envoie par e-mail à l'utilisateur actuellement connecté.

## Détails de l'exportation CSV de Segment {#segment-csv-export-details}

{% alert note %}
Les utilisateurs du tableau de bord doivent disposer de la permission **Export user data** pour utiliser les options d'exportation CSV. S'ils ne disposent pas de cette permission, les options d'exportation CSV n'apparaissent pas.
{% endalert %}

**CSV Export Email Addresses** n'inclut que les lignes des utilisateurs du Segment qui possèdent une adresse e-mail. Par exemple, si votre Segment comprend 100 000 utilisateurs mais que seuls 50 000 ont une adresse e-mail, **CSV Export Email Addresses** produit environ 50 000 lignes. **CSV Export User Data** exporte toutes les données utilisateur du Segment.

{% alert important %}
En raison de restrictions de taille de fichier, votre exportation peut échouer si la taille estimée de votre Segment dépasse 500 000 utilisateurs. Notez que cette restriction utilise la taille estimée de votre Segment, et non le calcul exact. Pour plus de détails, consultez [Exporter des Segments volumineux](#exporting-large-segments).
{% endalert %}

Si vous avez associé vos [identifiants Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3#integration) à Braze, le fichier CSV sera importé dans votre compartiment S3 sous la clé `segment-export/SEGMENT_ID/YYYY-MM-dd/users-RANDOMSTRING.zip`. Vous devez être connecté au tableau de bord pour accéder au lien de téléchargement qui vous est envoyé par e-mail.

{% multi_lang_include alerts/important_alerts.md alert='S3 file bucket export' %}

## Données incluses dans l'exportation {#data-included-in-export}

Les éléments suivants sont inclus dans votre exportation en fonction de votre sélection.

### Exportation CSV des données utilisateur {#csv-export-user-data}

| Nom du champ                | Description                                              |
| --------------------------- | -------------------------------------------------------- |
| Appboy ID                   | ID interne (ne peut pas être modifié)                     |
| country                     | Pays                                                     |
| created_at                  | Date et heure de création du profil utilisateur           |
| created_from                | Méthode utilisée pour créer le profil utilisateur (par exemple, REST API, SDK ou importation CSV) |
| devices                     | Informations sur l'appareil                              |
| date_of_birth               | Date de naissance                                        |
| email                       | Adresse e-mail                                           |
| unsubscribed_from_emails_at | Date de désabonnement des e-mails                        |
| user_id                     | ID externe                                               |
| first_name                  | Prénom                                                   |
| first_session               | Date et heure de la première session                     |
| gender                      | Genre                                                    |
| google_ad_ids               | ID publicitaires Google associés à l'utilisateur         |
| city                        | Ville                                                    |
| IDFAs                       | Valeurs d'identifiant publicitaire (IDFA)                |
| IDFVs                       | Valeurs d'identifiant de fournisseur (IDFV)              |
| language                    | Langue au standard ISO-639-1                             |
| last_app_version_used       | Dernière version de l'application utilisée               |
| last_name                   | Nom de famille                                           |
| last_session                | Date et heure de la dernière session                     |
| number_of_google_ad_ids     | Nombre d'ID publicitaires Google associés                |
| number_of_IDFAs             | Nombre d'IDFA associés                                   |
| number_of_IDFVs             | Nombre d'IDFV associés                                   |
| number_of_push_tokens       | Nombre de jetons de notification push associés           |
| number_of_roku_ad_ids       | Nombre d'ID publicitaires Roku associés                  |
| number_of_windows_ad_ids    | Nombre d'ID publicitaires Windows associés               |
| phone_number                | Numéro de téléphone                                      |
| opted_into_push_at          | Date d'abonnement aux notifications push                 |
| unsubscribed_from_push_at   | Date de désabonnement des notifications push             |
| random_bucket               | Numéro de compartiment aléatoire                         |
| roku_ad_ids                 | ID publicitaires Roku                                    |
| session_count               | Nombre total de sessions                                 |
| timezone                    | Fuseau horaire de l'utilisateur au même format que la base de données des fuseaux horaires de l'IANA |
| in_app_purchase_total       | Montant total dépensé en achats intégrés                 |
| user_aliases                | Alias d'utilisateur, le cas échéant                      |
| windows_ad_ids              | ID publicitaires Windows                                 |
| Custom events               | Basé sur la sélection lors de l'exportation              |
| Custom attributes           | Basé sur la sélection lors de l'exportation              |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exportation CSV des données utilisateur" }

{% alert note %}
Lorsque vous exportez les données utilisateur d'une étape Canvas, le CSV inclut tous les utilisateurs ayant participé à cette étape pendant toute la durée de vie de l'étape Canvas. Vous ne pouvez pas limiter l'exportation à une plage de dates ou à une autre fenêtre temporelle. Pour savoir comment effectuer ces exportations, consultez [Exporter les données Canvas]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data).
{% endalert %}

### Exportation CSV des adresses e-mail {#csv-export-email-addresses}

| Nom du champ                | Description                        |
| --------------------------- | ---------------------------------- |
| user_id                     | ID externe de l'utilisateur        |
| first_name                  | Prénom                             |
| last_name                   | Nom de famille                     |
| email                       | E-mail                             |
| unsubscribed_from_emails_at | Date de désabonnement des e-mails  |
| opted_in_to_emails_at       | Date d'abonnement aux e-mails      |
| user_aliases                | Alias d'utilisateur, le cas échéant |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exportation CSV des adresses e-mail" }

{% alert tip %}
Pour obtenir de l'aide concernant les exportations CSV et API, consultez notre article de [résolution des problèmes]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

{% alert note %}
Les données de groupe d'abonnement ne sont pas disponibles via les exportations de Segments. Pour identifier les utilisateurs par statut d'abonnement, créez un Segment distinct basé sur l'appartenance au groupe d'abonnement et exportez ce Segment.
{% endalert %}

## Exporter de grands Segments {#exporting-large-segments}

Il existe plusieurs méthodes pour exporter un grand Segment d'utilisateurs contenant plus de 500 000 utilisateurs.

{% tabs %}
{% tab Segments multiples %}

Vous pouvez diviser un grand Segment en Segments plus petits, puis exporter chacun de ces Segments depuis Braze.

{% endtab %}
{% tab Numéros de compartiment aléatoires %}

Vous pouvez également utiliser les [numéros de compartiment aléatoires]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) pour répartir votre base d'utilisateurs en plusieurs Segments, puis les combiner après l'exportation. Par exemple, si vous devez diviser votre Segment en deux Segments différents, vous pouvez le faire avec les filtres suivants :
- Segment 1 : le numéro de compartiment aléatoire est inférieur à 5000 (inclut 0-4999)
- Segment 2 : le numéro de compartiment aléatoire est supérieur à 4999 (inclut 5000-9999)

{% endtab %}
{% tab Endpoints %}

Vous pouvez également tirer parti des endpoints suivants pour exporter les données utilisateur d'un Segment spécifique. Notez que ces endpoints sont soumis à des limites de données et à des [limites de débit]({{site.baseurl}}/api/basics).
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group)

Si vous avez connecté des [identifiants Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3#integration), les exportations volumineuses peuvent être livrées dans votre compartiment en plus du lien de téléchargement envoyé par e-mail, comme décrit dans [Détails de l'exportation CSV de Segments](#segment-csv-export-details).

{% endtab %}
{% endtabs %}