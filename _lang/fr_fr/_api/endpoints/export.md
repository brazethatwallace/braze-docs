---
nav_title: Exporter
article_title: Endpoints d'exportation
search_tag: Endpoint
page_order: 2
description: "Cet article de référence présente les endpoints d'exportation de Braze, y compris les conditions préalables, ce que vous pouvez exporter, la manière dont les données sont livrées et une liste complète des endpoints."
page_type: reference
---

# Endpoints d'exportation {#export-endpoints}

Avec cette collection d'endpoints, vous pouvez accéder à et exporter différents niveaux de détails sur vos indicateurs clés de performance, sessions d'application, utilisateurs, Segments, Campaigns et Canvas. Assurez-vous de connaître votre [instance Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints), votre [clé API]({{site.baseurl}}/api/api_key) et votre [identifiant API]({{site.baseurl}}/api/identifier_types) lors de l'élaboration de vos paramètres et corps de requête.

## Conditions préalables {#prerequisites}

Avant de commencer, assurez-vous de disposer des éléments suivants :

| Exigence | Description |
| --- | --- |
| Clé REST API de Braze | Une clé REST API avec les autorisations d'exportation appropriées pour les endpoints que vous prévoyez d'appeler. Les clés API sont limitées à des endpoints spécifiques, et les autorisations ne peuvent pas être modifiées après la création. Pour plus de détails, consultez [Clé REST API]({{site.baseurl}}/api/basics#about-rest-api-keys). |
| Identifiants pertinents | Les identifiants des données que vous souhaitez exporter, tels qu'un ID de Campaign, un ID de Segment ou un ID de Canvas. Vous pouvez les trouver sur le tableau de bord de Braze. Pour une liste complète, consultez [Types d'identifiants API]({{site.baseurl}}/api/identifier_types). |
| Identifiants de stockage cloud (facultatif) | Si vous exportez de grands ensembles de données, connectez un compartiment [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3), [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents) ou [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents) pour que les fichiers d'exportation soient écrits directement dans votre stockage. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

{% alert note %}
Si vous êtes un marketeur ou un membre d'équipe sans accès à l'API, coordonnez-vous avec un développeur ou un administrateur de votre organisation pour configurer les clés API et les intégrations.
{% endalert %}

## Ce que vous pouvez exporter {#what-you-can-export}

Le tableau suivant résume les catégories de données disponibles via les API d'exportation.

| Catégorie | Ce qu'elle inclut | Référence API |
| --- | --- | --- |
| Campaigns | Analyses de performance, détails des Campaigns, listes de Campaigns et analyses d'envoi | [Endpoints Campaign]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) |
| Canvas | Analyses de séries de données, résumés d'analyses, détails de Canvas et listes de Canvas | [Endpoints Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) |
| Segments | Listes de Segments, analyses de Segments et détails de Segments | [Endpoints Segment]({{site.baseurl}}/api/endpoints/export/segments/get_segment) |
| Données utilisateur | Profils utilisateur complets par identifiant ou par Segment, et utilisateurs par groupe de contrôle global | [Endpoints de données utilisateur]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) |
| Indicateurs clés de performance | Utilisateurs actifs quotidiens, utilisateurs actifs mensuels, nouveaux utilisateurs quotidiens et désinstallations par date | [Endpoints KPI]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) |
| Sessions | Données de séries temporelles des sessions d'application | [Endpoint Sessions]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) |
| Événements personnalisés | Noms d'événements, listes d'événements et analyses d'événements dans le temps | [Endpoints d'événements personnalisés]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) |
| Attributs personnalisés | Noms d'attributs | [Endpoint d'attributs personnalisés]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) |
| Achats | Données de chiffre d'affaires par période, listes d'identifiants de produit et nombre d'achats | [Endpoints d'achats]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Ce que vous pouvez exporter" }

## Comment les données d'exportation sont livrées {#how-export-data-is-delivered}

Les exportations API renvoient les données au format JSON, contrairement aux fichiers CSV que vous téléchargez depuis le tableau de bord. La méthode de livraison dépend de la connexion ou non d'un stockage cloud :

- **Sans stockage cloud :** Braze écrit les fichiers d'exportation dans son propre compartiment S3 et inclut une URL de téléchargement temporaire dans la réponse de l'API. Cette URL expire après quatre heures, et l'exportation est empaquetée sous forme d'archive compressée (ZIP ou GZIP, selon le paramètre `output_format`) contenant des fichiers JSON. Chaque ligne des fichiers JSON représente un objet de données.
- **Avec un stockage cloud connecté :** Braze écrit les fichiers d'exportation directement dans votre compartiment configuré. La réponse de l'API n'inclut pas d'URL de téléchargement. Les fichiers suivent vos propres politiques de rétention et sont généralement plus fiables pour les exportations volumineuses.

{% alert tip %}
« Stockage cloud » désigne votre propre compartiment de stockage (par exemple, Amazon S3, Microsoft Azure Blob Storage ou Google Cloud Storage). Vous pouvez connecter votre compartiment dans **Intégrations partenaires** > **Partenaires technologiques** afin que Braze puisse écrire les fichiers d'exportation directement dedans.
{% endalert %}

Pour plus de détails sur la livraison des exportations et la résolution des problèmes, consultez [Résolution des problèmes d'exportation]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).

## Endpoints d'exportation

Le tableau suivant répertorie toutes les API d'exportation disponibles.

| Catégorie | Méthode | Endpoint |
| --- | --- | --- |
| Campaigns | GET | [Campaign Analytics]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) |
| Campaigns | GET | [Campaign Details]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) |
| Campaigns | GET | [Campaigns List]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) |
| Campaigns | GET | [Send Analytics]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) |
| Canvas | GET | [Canvas Data Series Analytics]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) |
| Canvas | GET | [Canvas Analytics Summary]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) |
| Canvas | GET | [Canvas Details]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) |
| Canvas | GET | [Canvas List]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) |
| Événements personnalisés | GET | [Custom Events]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) |
| Événements personnalisés | GET | [Custom Events List]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) |
| Événements personnalisés | GET | [Custom Event Analytics]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) |
| Attributs personnalisés | GET | [Custom Attributes]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) |
| Indicateurs clés de performance | GET | [KPIs for Daily New Users by Date]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) |
| Indicateurs clés de performance | GET | [KPIs for Daily Active Users by Date]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) |
| Indicateurs clés de performance | GET | [KPIs for Monthly Active Users Over Last 30 Days]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) |
| Indicateurs clés de performance | GET | [KPIs for Uninstalls by Date]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) |
| Achats | GET | [Product IDs List]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) |
| Achats | GET | [Number of Purchases]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) |
| Achats | GET | [Revenue Data by Time]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) |
| Segments | GET | [Segment List]({{site.baseurl}}/api/endpoints/export/segments/get_segment) |
| Segments | GET | [Segment Analytics]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) |
| Segments | GET | [Segment Details]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) |
| Sessions | GET | [App Sessions Time-Series Data]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) |
| Données utilisateur | POST | [User Data by Identifier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) |
| Données utilisateur | POST | [User Data by Segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) |
| Données utilisateur | POST | [User Data by Global Control Group]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Endpoints d'exportation" }

## Articles connexes {#related-articles}

Pour des exportations ponctuelles depuis le tableau de bord, consultez ces articles :

- [Exporter les données de Campaign]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_campaign_results_data)
- [Exporter les données de Canvas]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data)
- [Exporter les données de Segment au format CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv)