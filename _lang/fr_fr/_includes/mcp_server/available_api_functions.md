# Fonctions du serveur Braze MCP {#braze-mcp-server-functions}

> Le serveur Braze MCP expose un ensemble de fonctions API qui correspondent à des endpoints REST API Braze spécifiques. Les clients MCP tels que Claude et Cursor peuvent appeler ces fonctions pour récupérer des données non personnelles et, avec les autorisations appropriées, effectuer des actions d'écriture sans données personnelles identifiables. Pour des informations plus générales, consultez [le serveur Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Conditions préalables {#prerequisites}

Avant de pouvoir utiliser cette fonctionnalité, vous devez [configurer le serveur Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Fonctions API Braze disponibles {#available-braze-api-functions}

Votre client MCP fait référence aux fonctions API suivantes pour interagir avec le serveur Braze MCP.

### Fonctions générales {#general-functions}

Ces fonctions aident votre client MCP à découvrir et exécuter les fonctions API Braze disponibles.

| Fonction | Description |
|----------|-------------|
| `list_functions` | Répertorie toutes les fonctions API Braze disponibles avec leurs descriptions et leurs paramètres. |
| `call_function` | Appelle une fonction API Braze spécifique en lecture seule avec les paramètres fournis. |
| `call_write_function` | Appelle une fonction API Braze spécifique en écriture avec les paramètres fournis. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="General functions" }

### Campaigns

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) | Exporte une liste de Campaigns avec leurs métadonnées. |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) | Obtient des informations détaillées sur des Campaigns spécifiques. |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) | Récupère les données d'analyse chronologiques pour les Campaigns. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Campaigns" }

### Canvas {#canvases}

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) | Exporte une liste de Canvas avec leurs métadonnées. |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) | Obtient des informations détaillées sur des Canvas spécifiques. |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) | Obtient un résumé analytique des performances de Canvas. |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) | Récupère les données d'analyse chronologiques pour les Canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Canvases" }

### Catalogues {#catalogs}

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) | Renvoie une liste des catalogues dans un espace de travail. |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/) | Renvoie plusieurs éléments du catalogue et leur contenu avec prise en charge de la pagination. |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/) | Renvoie un élément spécifique du catalogue et son contenu par ID. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Catalogs" }

### Ingestion de données cloud {#cloud-data-ingestion}

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/) | Renvoie une liste des intégrations CDI existantes. |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status/) | Renvoie les statuts de synchronisation passés pour une intégration CDI donnée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Cloud Data Ingestion" }

### Content Blocks

Les fonctions `create_content_block` et `update_content_block` sont des fonctions d'écriture. Votre client MCP doit les appeler avec `call_write_function`, et votre clé API doit disposer de l'autorisation `content_blocks.create` ou `content_blocks.update` correspondante.

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_content_blocks_list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) | Liste vos Content Blocks disponibles. |
| `get_content_blocks_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) | Obtient des informations sur vos Content Blocks. |
| `create_content_block` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/) | Crée un bloc de contenu. Nécessite `name` et `content`. Les champs facultatifs sont `description`, `state` (doit être `active` ou `draft`) et `tags`. |
| `update_content_block` | [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) | Met à jour un bloc de contenu existant. Nécessite `content_block_id` et au moins un champ modifiable : `name`, `content`, `description`, `state` (doit être `active` ou `draft`) ou `tags`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Content Blocks" }

### Attributs personnalisés {#custom-attributes}

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_custom_attributes` | [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes/) | Exporte les attributs personnalisés enregistrés pour votre application. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Custom Attributes" }

### Événements {#events}

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) | Exporte une liste des événements personnalisés enregistrés pour votre application. |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) | Récupère les données chronologiques pour les événements personnalisés. |
| `get_events` | [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data/) | Obtient des données détaillées sur les événements avec prise en charge de la pagination. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Events" }

### Indicateurs clés de performance {#kpis}

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_new_users_data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) | Série quotidienne du nombre de nouveaux utilisateurs. |
| `get_dau_data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) | Données chronologiques relatives aux utilisateurs actifs quotidiens. |
| `get_mau_data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) | Données chronologiques relatives aux utilisateurs actifs mensuels. |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) | Données chronologiques relatives aux désinstallations d'applications. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="KPIs" }

### Bibliothèque multimédia {#media-library}

La fonction `create_media_library_asset` est une fonction d'écriture. Votre client MCP doit l'appeler avec `call_write_function`, et votre clé API doit disposer de l'autorisation `media_library.create`.

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `create_media_library_asset` | [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create/) | Téléverse une ressource dans votre bibliothèque multimédia Braze. Vous pouvez fournir soit une URL accessible publiquement (`asset_url`), soit un fichier encodé en base64 (`asset_file_base64`), mais pas les deux. La taille des images est limitée à 5 Mo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Media Library" }

### Messages

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_scheduled_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/) | Liste les Campaigns et Canvas planifiés à venir. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Messages" }

### Centres de préférences {#preference-centers}

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_preference_centers` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/) | Liste vos centres de préférences disponibles. |
| `get_preference_center_details` | [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/) | Affiche les détails d'un centre de préférences spécifique, y compris le contenu HTML et les options. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Preference Centers" }

### Achats {#purchases}

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) | Exporte une liste paginée des ID de produits. |
| `get_revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) | Données chronologiques d'analyse du chiffre d'affaires. |
| `get_quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) | Données chronologiques relatives aux quantités achetées. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Purchases" }

### Segments

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) | Exporte la liste des Segments avec le statut de suivi analytique. |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) | Données d'analyse chronologiques pour les Segments. |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) | Informations détaillées sur des Segments spécifiques. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Segments" }

### Envois {#sends}

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | Analyses quotidiennes des envois de Campaigns suivis. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Sends" }

### Sessions

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) | Données chronologiques relatives au nombre de sessions d'application. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Sessions" }

### Clés d'authentification SDK {#sdk-authentication-keys}

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_sdk_authentication_keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys/) | Liste toutes les clés d'authentification SDK pour votre application. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SDK Authentication Keys" }

### Abonnement {#subscription}

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_user_subscription_groups` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) | Répertorie et obtient les groupes d'abonnement d'un utilisateur donné. |
| `get_subscription_group_status` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) | Obtient l'état d'abonnement d'un utilisateur dans un groupe d'abonnement. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Subscription" }

### Modèles {#templates}

Les fonctions `create_email_template` et `update_email_template` sont des fonctions d'écriture. Votre client MCP doit les appeler avec `call_write_function`, et votre clé API doit disposer de l'autorisation `templates.email.create` ou `templates.email.update` correspondante.

| Fonction | Endpoint | Description |
|----------|----------|-------------|
| `get_email_templates_list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) | Liste vos modèles d'e-mail disponibles. |
| `get_email_template_info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | Obtient des informations sur vos modèles d'e-mail. |
| `create_email_template` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) | Crée un modèle d'e-mail. Nécessite `template_name`, `subject` et `body`. Les champs facultatifs sont `plaintext_body`, `preheader`, `tags` et `should_inline_css`. |
| `update_email_template` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) | Met à jour un modèle d'e-mail existant. Nécessite `email_template_id` et au moins un champ modifiable : `template_name`, `subject`, `body`, `plaintext_body`, `preheader`, `tags` ou `should_inline_css`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Templates" }

{% multi_lang_include mcp_server/legal_disclaimer.md %}