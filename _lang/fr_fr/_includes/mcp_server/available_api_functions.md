# Fonctions du serveur Braze MCP {#braze-mcp-server-functions}

> Le serveur Braze MCP expose des outils en lecture et en écriture qui correspondent à des endpoints REST API Braze spécifiques. Pour en savoir plus, consultez [le serveur Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Prérequis {#prerequisites}

Avant de pouvoir utiliser cette fonctionnalité, vous devrez [configurer le serveur Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Fonctions API Braze disponibles {#available-braze-api-functions}

Votre client MCP fait référence à ces outils pour interagir avec le serveur Braze MCP.

### Espaces de travail {#workspaces}

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `get_workspaces` | N/A | lecture | Découvrir quels espaces de travail Braze le jeton d'accès OAuth actuel peut atteindre. Appelez cet outil en premier : chaque `id` d'espace de travail renvoyé correspond à l'`app_group_id` requis par tous les autres outils. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Espaces de travail" }

### Campaigns

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | lecture | Exporter une liste de Campaigns avec le nom, l'identifiant API de la Campaign, le drapeau API-campaign et les tags. |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | lecture | Récupérer les informations pertinentes sur une Campaign spécifiée par `campaign_id`. |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | lecture | Séries quotidiennes de statistiques de Campaign au fil du temps (envois, ouvertures, clics, conversions par canal). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Campaigns" }

### Canvas {#canvases}

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | lecture | Exporter une liste de Canvas avec le nom, l'identifiant API du Canvas et les tags. |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | lecture | Exporter les métadonnées d'un Canvas : nom, date de création, statut actuel, et plus encore. |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | lecture | Exporter les données de séries temporelles pour un Canvas. |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | lecture | Exporter les agrégations des données de séries temporelles d'un Canvas pour un résumé concis des résultats. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Canvas" }

### Catalogues {#catalogs}

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | lecture | Lister les catalogues d'un espace de travail. |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | lecture | Renvoyer plusieurs éléments de catalogue et leur contenu. |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | lecture | Renvoyer un seul élément de catalogue et son contenu. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Catalogues" }

### Attributs personnalisés {#custom-attributes}

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `get_custom_attributes` | [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | lecture | Exporter les attributs personnalisés enregistrés pour votre application, par groupes de 50, par ordre alphabétique. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Attributs personnalisés" }

### Événements personnalisés {#custom-events}

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `get_events` | [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | lecture | Exporter les événements personnalisés enregistrés pour votre application, par groupes de 50, par ordre alphabétique (pagination par curseur). |
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | lecture | Exporter les noms d'événements personnalisés, par groupes de 250, par ordre alphabétique (pagination par page). |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | lecture | Occurrences d'un événement personnalisé sur une période donnée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Événements personnalisés" }

### Intégrations CDI {#cdi-integrations}

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | lecture | Lister les intégrations Cloud Data Ingestion existantes, 10 par appel. |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | lecture | Statuts de synchronisation passés pour une intégration CDI donnée, 10 par appel. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Intégrations CDI" }

### KPI

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `get_dau_data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | lecture | Séries quotidiennes d'utilisateurs actifs uniques par date. |
| `get_mau_data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | lecture | Séries quotidiennes d'utilisateurs actifs uniques sur une fenêtre glissante de 30 jours. |
| `get_new_users_data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | lecture | Séries quotidiennes du nombre total de nouveaux utilisateurs par date. |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | lecture | Séries quotidiennes du nombre total de désinstallations par date. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="KPI" }

### Bibliothèque multimédia {#media-library}

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `create_media_library_asset` | [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) | création | Importer une ressource dans la bibliothèque multimédia de Braze via une URL externe ou un contenu de fichier en base64. Un seul mode d'importation doit être fourni. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Bibliothèque multimédia" }

### Achats {#purchases}

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `get_product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | lecture | Liste paginée des identifiants de produits. |
| `get_quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | lecture | Nombre total d'achats dans votre application sur une période donnée. |
| `get_revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | lecture | Total des dépenses dans votre application sur une période donnée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Achats" }

### Segments

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | lecture | Exporter les Segments avec le nom, l'identifiant API du Segment et le drapeau de suivi analytique. |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | lecture | Récupérer les informations pertinentes sur un Segment par `segment_id`. |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | lecture | Séries quotidiennes de la taille estimée d'un Segment au fil du temps. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Segments" }

### Envois {#sends}

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | lecture | Statistiques quotidiennes pour un `send_id` suivi (Campaigns API). Braze conserve les analyses d'envoi pendant 14 jours après l'envoi. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Envois" }

### Sessions

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | lecture | Nombre de sessions pour votre application sur une période donnée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Sessions" }

### Modèles {#templates}

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `get_email_templates` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | lecture | Lister les modèles d'e-mail disponibles dans votre compte Braze. |
| `get_email_template_info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | lecture | Obtenir les informations d'un modèle d'e-mail spécifique. Les modèles de l'éditeur par glisser-déposer ne sont pas acceptés. |
| `create_email_template` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template) | création | Créer un modèle d'e-mail dans le tableau de bord de Braze. |
| `update_email_template` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template) | mise à jour | Mettre à jour un modèle d'e-mail existant. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Modèles" }

### Blocs de contenu {#content-blocks}

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `get_content_blocks` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | lecture | Lister les informations des blocs de contenu existants. |
| `get_content_block_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | lecture | Obtenir les informations d'un bloc de contenu existant, avec en option les données d'inclusion dans une Campaign ou un Canvas. |
| `create_content_block` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) | création | Créer un bloc de contenu. |
| `update_content_block` | [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block) | mise à jour | Mettre à jour un bloc de contenu. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Blocs de contenu" }

{% multi_lang_include mcp_server/legal_disclaimer.md %}