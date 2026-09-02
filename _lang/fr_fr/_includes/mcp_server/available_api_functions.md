# Fonctions du serveur Braze MCP {#braze-mcp-server-functions}

> Le serveur Braze MCP expose des outils en lecture et en écriture qui correspondent à des endpoints REST API Braze spécifiques. Pour en savoir plus, consultez [le serveur Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

{% alert note %}
Le serveur Braze MCP inclut des outils qui ne sont disponibles que pour les clients participant à des programmes bêta. Si vous tentez d'accéder à un outil faisant partie d'un programme bêta et que votre compte n'a pas la fonctionnalité activée, vous pourriez recevoir une réponse d'erreur. Pour rejoindre un programme bêta, contactez votre gestionnaire de compte.
{% endalert %}

## Prérequis {#prerequisites}

Avant de pouvoir utiliser cette fonctionnalité, vous devrez [configurer le serveur Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Fonctions API Braze disponibles {#available-braze-api-functions}

Votre client MCP fait référence à ces outils pour interagir avec le serveur Braze MCP.

### Espaces de travail {#workspaces}

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `get_workspaces` | N/A | lecture | Découvre quels espaces de travail Braze le jeton d'accès OAuth actuel peut atteindre. Appelez cet outil en premier : chaque `id` d'espace de travail renvoyé correspond au `app_group_id` requis par tous les autres outils. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Espaces de travail" }

### Campaigns

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | lecture | Exporte une liste de Campaigns avec le nom, l'identifiant API de la Campaign, l'indicateur API-campaign et les tags. |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | lecture | Récupère les informations pertinentes sur une Campaign spécifiée par `campaign_id`. |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | lecture | Séries quotidiennes de statistiques de Campaign au fil du temps (envois, ouvertures, clics, conversions par canal). |
| `duplicate_campaign` | [`/campaigns/duplicate`]({{site.baseurl}}/api/endpoints/messaging/duplicate_messages/post_duplicate_campaigns) | création | Duplique une Campaign existante. |
| `create_campaign`<sup>*</sup> | N/A | création | Crée une nouvelle Campaign. |
| `edit_campaign`<sup>*</sup> | N/A | mise à jour | Modifie une Campaign existante. |
| `launch_campaign`<sup>*</sup> | N/A | mise à jour | Lance une Campaign. |
| `stop_campaign`<sup>*</sup> | N/A | mise à jour | Arrête une Campaign en cours d'exécution. |
| `archive_campaign`<sup>*</sup> | N/A | mise à jour | Archive une Campaign. |
| `unarchive_campaign`<sup>*</sup> | N/A | mise à jour | Désarchive une Campaign. |
| `get_campaign_draft`<sup>*</sup> | N/A | lecture | Récupère les détails du brouillon d'une Campaign. |
| `get_campaign_live_details`<sup>*</sup> | N/A | lecture | Récupère les détails d'une Campaign en direct or en ligne/en production/instantané. |
| `create_campaign_message`<sup>*</sup> | N/A | création | Crée un message au sein d'une Campaign. |
| `update_campaign_message`<sup>*</sup> | N/A | mise à jour | Met à jour un message de Campaign. |
| `delete_campaign_message`<sup>*</sup> | N/A | suppression | Supprime un message de Campaign. |
| `create_campaign_message_variation`<sup>*</sup> | N/A | création | Crée une variante de message au sein d'une Campaign. |
| `update_campaign_message_variation`<sup>*</sup> | N/A | mise à jour | Met à jour une variante de message de Campaign. |
| `delete_campaign_message_variation`<sup>*</sup> | N/A | suppression | Supprime une variante de message de Campaign. |
| `update_campaign_distribution`<sup>*</sup> | N/A | mise à jour | Met à jour les paramètres de distribution d'une Campaign. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Campaigns" }

<sup>*</sup> Cet outil est uniquement disponible pour les clients participant au programme bêta des API de Campaign. Si cette fonctionnalité n'est pas activée pour votre compte, vous pouvez recevoir une erreur en tentant de l'utiliser. Pour rejoindre le programme bêta, contactez votre gestionnaire de compte.
{: .reset-td-br-1 }

### Canvas {#canvases}

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | lecture | Exporte une liste de Canvas avec le nom, l'identifiant API du Canvas et les tags. |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | lecture | Exporte les métadonnées d'un Canvas : nom, date de création, statut actuel, et plus encore. |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | lecture | Exporte les données de séries temporelles pour un Canvas. |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | lecture | Exporte les données agrégées des séries temporelles d'un Canvas pour un résumé concis des résultats. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Canvas" }

### Catalogues {#catalogs}

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | lecture | Liste les catalogues d'un espace de travail. |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | lecture | Renvoie plusieurs éléments de catalogue et leur contenu. |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | lecture | Renvoie un seul élément de catalogue et son contenu. |
| `create_catalog` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog) | création | Crée un catalogue. |
| `delete_catalog` | [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog) | suppression | Supprime un catalogue. |
| `create_catalog_fields` | [`/catalogs/{catalog_name}/fields`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields) | création | Crée plusieurs champs dans un catalogue. |
| `delete_catalog_field` | [`/catalogs/{catalog_name}/fields/{field_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field) | suppression | Supprime un champ de catalogue. |
| `create_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk) | création | Crée plusieurs éléments dans un catalogue. Jusqu'à 50 éléments par requête. |
| `edit_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk) | mise à jour | Modifie plusieurs éléments existants dans un catalogue. Jusqu'à 50 éléments par requête. |
| `replace_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items) | mise à jour | Remplace plusieurs éléments dans un catalogue. Crée les éléments s'ils n'existent pas. Jusqu'à 50 éléments par requête. |
| `delete_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) | suppression | Supprime plusieurs éléments dans un catalogue. Jusqu'à 50 éléments par requête. |
| `create_catalog_selection` | [`/catalogs/{catalog_name}/selections`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections) | création | Crée une sélection dans un catalogue. |
| `delete_catalog_selection` | [`/catalogs/{catalog_name}/selections/{selection_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection) | suppression | Supprime une sélection de catalogue. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Catalogues" }

### Attributs personnalisés {#custom-attributes}

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `get_custom_attributes` | [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | lecture | Exporte les attributs personnalisés enregistrés pour votre application, par groupes de 50, par ordre alphabétique. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Attributs personnalisés" }

### Événements personnalisés {#custom-events}

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `get_events` | [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | lecture | Exporte les événements personnalisés enregistrés pour votre application, par groupes de 50, par ordre alphabétique (pagination par curseur). |
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | lecture | Exporte les noms d'événements personnalisés, par groupes de 250, par ordre alphabétique (pagination par page). |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | lecture | Nombre d'occurrences d'un événement personnalisé sur une période donnée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Événements personnalisés" }

### Intégrations CDI {#cdi-integrations}

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | lecture | Liste les intégrations Cloud Data Ingestion existantes, 10 par appel. |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | lecture | Statuts de synchronisation passés pour une intégration CDI donnée, 10 par appel. |
| `trigger_integration_sync` | [`/cdi/integrations/{integration_id}/sync`]({{site.baseurl}}/api/endpoints/cdi/post_job_sync) | écriture | Déclenche une synchronisation pour une intégration CDI donnée. |
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
| `create_media_library_asset` | [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) | création | Télécharge une ressource vers la bibliothèque multimédia de Braze via une URL externe ou un contenu de fichier encodé en base64. Un seul mode de téléchargement doit être fourni. |
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
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | lecture | Exporte les Segments avec le nom, l'identifiant API du Segment et l'indicateur de suivi analytique. |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | lecture | Récupère les informations pertinentes sur un Segment par `segment_id`. |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | lecture | Séries quotidiennes de la taille estimée d'un Segment au fil du temps. |
| `get_segment_filters`<sup>*</sup> | N/A | lecture | Récupère les définitions de filtres de Segment. |
| `create_segment`<sup>*</sup> | N/A | création | Crée un nouveau Segment. |
| `edit_segment`<sup>*</sup> | N/A | mise à jour | Modifie un Segment existant. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Segments" }

<sup>*</sup> Cet outil est uniquement disponible pour les clients participant au programme bêta des API de Segment. Si cette fonctionnalité n'est pas activée pour votre compte, vous pouvez recevoir une erreur en tentant de l'utiliser. Pour rejoindre le programme bêta, contactez votre gestionnaire de compte.
{: .reset-td-br-1 }

### Envois {#sends}

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | lecture | Statistiques quotidiennes pour un `send_id` suivi (Campaigns API). Braze conserve les données analytiques d'envoi pendant 14 jours après l'envoi. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Envois" }

### Sessions

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | lecture | Nombre de sessions pour votre application sur une période donnée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Sessions" }

### Modèles {#templates}

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `get_email_templates` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | lecture | Liste les modèles d'e-mail disponibles dans votre compte Braze. |
| `get_email_template_info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | lecture | Récupère les informations d'un modèle d'e-mail spécifique. Les modèles de l'éditeur par glisser-déposer ne sont pas acceptés. |
| `create_email_template` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template) | création | Crée un modèle d'e-mail sur le tableau de bord de Braze. |
| `update_email_template` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template) | mise à jour | Met à jour un modèle d'e-mail existant. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Modèles" }

### Content Blocks

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `get_content_blocks` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | lecture | Liste les informations sur les Content Blocks existants. |
| `get_content_block_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | lecture | Récupère les informations d'un Content Block existant, avec en option les données d'inclusion dans une Campaign ou un Canvas. |
| `create_content_block` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) | création | Crée un Content Block. |
| `update_content_block` | [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block) | mise à jour | Met à jour un Content Block. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Content Blocks" }

### Operator

| Outil | Endpoint API | Accès | Description |
| --- | --- | --- | --- |
| `send_operator_prompt` | N/A | mise à jour | Envoie un prompt en langage naturel à BrazeAI Operator. Soumet une tâche en arrière-plan et renvoie un job_id. |
| `get_operator_result` | N/A | lecture | Interroge le résultat d'une tâche Operator soumise à l'aide de son job_id. |
| `cancel_operator_job` | N/A | mise à jour | Annule une tâche Operator en cours d'exécution. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Operator" }

{% alert important %}
Ces outils sont uniquement disponibles pour les clients participant au programme bêta d'Operator. Si cette fonctionnalité n'est pas activée pour votre compte, vous pouvez recevoir une erreur en tentant de l'utiliser. Pour rejoindre le programme bêta, contactez votre gestionnaire de compte.
{% endalert %}

{% multi_lang_include mcp_server/legal_disclaimer.md %}