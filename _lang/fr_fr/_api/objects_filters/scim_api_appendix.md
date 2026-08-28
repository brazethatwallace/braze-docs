---
nav_title: "Objets API SCIM et annexes"
article_title: "Objets API SCIM et annexes"
page_type: reference
description: "Cet article présente les différents objets de l'API SCIM ainsi que les annexes associées."
alias: /scim_api_appendix/
---

# Objets API SCIM et annexes {#scim-api-objects-and-appendix}

> Cet article présente les différents objets de l'API SCIM ainsi que les annexes associées.

{% sdktabs %}
{% sdktab Granular SCIM API %}

## Migration vers les permissions granulaires {#granular-permissions-migration}

Les intégrations SCIM existantes et les [objets de l'API SCIM héritée]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api) continuent de fonctionner après la migration vers les permissions granulaires, mais Braze cessera d'accepter les valeurs de l'API SCIM héritée en décembre 2026.

Aucune action immédiate n'est requise de votre part. Cependant, passez en revue vos intégrations pour les permissions qui migrent vers les permissions granulaires. Par exemple, si vous envoyez actuellement `basic_access` dans l'API, mettez à jour votre intégration après la migration vers les permissions granulaires pour inclure les permissions spécifiques (par exemple, `"appGroupPermissions":["view_campaigns","edit_campaigns"]`). Braze continue d'accepter les chaînes héritées, comme `basic_access`, après la migration vers les permissions granulaires afin que les intégrations existantes ne soient pas interrompues.

## Objet permissions {#permissions-object}

L'objet permissions est un champ présent dans certaines requêtes et réponses lors de l'interaction avec la ressource utilisateur via les permissions d'ID SCIM.

{% alert note %}
Les groupes d'applications ont été renommés en espaces de travail dans Braze, mais les clés de cette page font toujours référence à l'ancienne terminologie (par exemple, `appGroup`, `appGroupName`).
{% endalert %}

```
{
  "permissions": {
    "companyPermissions": (required, array),
    "appGroup": (required, array)
  }
}
```

Un objet permissions valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Obligatoire | Type de données | Description |
| --- | --- | --- | --- |
| `companyPermissions` | Facultatif | Tableau | Tableau de [chaînes de permissions au niveau de l'entreprise]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_company), dans lequel la présence de la chaîne indique que l'utilisateur dispose de la permission correspondante. |
| `roles` | Facultatif | Tableau | Tableau d'[objets rôle]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_role-object). |
| `appGroup` | Obligatoire | Tableau | Tableau d'[objets permissions d'espace de travail]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objet permissions" }

### Objet permissions d'espace de travail {#workspace-permissions-object}

Un objet permissions d'espace de travail valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Obligatoire | Type de données | Description |
| --- | --- | --- | --- |
| `appGroupName` | Facultatif | Chaîne de caractères | Nom de l'espace de travail. Utilisé pour spécifier à quel espace de travail les permissions contenues dans cet objet s'appliquent. |
| `appGroupId` | Obligatoire si `appGroupName` est absent | Chaîne de caractères | ID de l'espace de travail, servant de méthode alternative pour spécifier l'espace de travail. |
| `appGroupPermissionSets` | Facultatif | Tableau | Tableau contenant un seul [objet ensemble de permissions d'espace de travail]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-set-object). |
| `appGroupPermissions` | Obligatoire | Tableau | Tableau de chaînes de permissions au niveau de l'espace de travail provenant du tableau [Chaînes de permissions d'espace de travail]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-strings), dans lequel la présence de la chaîne indique que l'utilisateur dispose de la permission correspondante pour l'espace de travail spécifié. |
| `team` | Facultatif | Tableau | Tableau d'[objets permissions Teams]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objet permissions d'espace de travail" }

### Objet ensemble de permissions d'espace de travail {#workspace-permissions-set-object}

Un objet ensemble de permissions d'espace de travail valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Obligatoire | Type de données | Description |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | Facultatif | Chaîne de caractères | Nom de l'ensemble de permissions d'espace de travail attribué à l'utilisateur pour cet espace de travail. |
| `appGroupPermissionSetID` | Obligatoire si `appGroupPermissionSetName` est absent | Chaîne de caractères | ID de l'espace de travail, servant de méthode alternative pour spécifier l'ensemble de permissions d'espace de travail attribué à l'utilisateur pour cet espace de travail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objet ensemble de permissions d'espace de travail #workspace-permissions-set-object" }

### Objet permissions Teams {#team-permissions-object}

Un objet permissions Teams valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Obligatoire | Type de données | Description |
| --- | --- | --- | --- |
| `teamName` | Facultatif | Chaîne de caractères | Nom de l'équipe, qui peut être utilisé pour spécifier à quelle équipe les permissions contenues dans cet objet s'appliquent. |
| `teamId` | Obligatoire si `teamName` est absent | Chaîne de caractères | ID de l'équipe, servant de méthode alternative pour spécifier l'équipe. |
| `teamPermissions` | Obligatoire | Tableau | Tableau de chaînes de permissions au niveau de l'équipe provenant du tableau [Chaînes de permissions Teams]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team), dans lequel la présence de la chaîne indique que l'utilisateur dispose de la permission correspondante pour l'équipe spécifiée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objet permissions Teams" }

## Objet rôle {#role-object}

Un objet rôle valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Obligatoire | Type de données | Description |
| --- | --- | --- | --- |
| `roleName` | Facultatif | Chaîne de caractères | Nom du rôle attribué à l'utilisateur. |
| `roleId` | Obligatoire si `roleName` est absent | Chaîne de caractères | ID du rôle, servant de méthode alternative pour spécifier le rôle. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objet rôle" }

## Annexes {#appendix}

### Chaînes de permissions d'entreprise {#company}

| Affichage dans l'interface | Chaîne API SCIM |
| --- | --- |
| Administrator | `admin` |
| Manage Company Settings | `manage_company_settings` |
| Create and delete workspaces | `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Chaînes de permissions d'entreprise #company" }

### Chaînes de permissions d'espace de travail {#workspace-strings}

| Nom de la permission | Chaîne API SCIM |
| --- | --- |
| View Campaigns | `view_campaigns` |
| Edit Campaigns | `edit_campaigns` |
| Archive Campaigns | `archive_campaigns` |
| View Canvases | `view_canvases` |
| Edit Canvases | `edit_canvases` |
| Archive Canvases | `archive_canvases` |
| View Frequency Capping Rules | `view_frequency_caps` |
| Edit Frequency Capping Rules | `edit_frequency_caps` |
| View Message Prioritization | `view_message_prioritization` |
| Edit Message Prioritization | `edit_message_prioritization` |
| View Content Blocks | `view_content_blocks` |
| Edit Content Blocks | `edit_content_blocks` |
| Archive Content Blocks | `archive_content_blocks` |
| View Feature Flags | `view_feature_flags` |
| Edit Feature Flags | `edit_feature_flags` |
| Archive Feature Flags | `archive_feature_flags` |
| View Segments | `view_segments` |
| Edit Segments | `edit_segments` |
| Archive Segments | `archive_segments` |
| View Global Control Group | `view_global_control_group` |
| Edit Global Control Group | `edit_global_control_group` |
| View IAM Templates | `view_iam_templates` |
| Edit IAM Templates | `edit_iam_templates` |
| Archive IAM Templates | `archive_iam_templates` |
| View Email Templates | `view_email_templates` |
| Edit Email Templates | `edit_email_templates` |
| Archive Email Templates | `archive_email_templates` |
| View Webhook Templates | `view_webhook_templates` |
| Edit Webhook Templates | `edit_webhook_templates` |
| Archive Webhook Templates | `archive_webhook_templates` |
| View Email Link Templates | `view_link_templates` |
| Edit Email Link Templates | `edit_link_templates` |
| View Media Library Assets | `view_media_library_assets` |
| View Locations | `view_locations` |
| Edit Locations | `edit_locations` |
| Archive Locations | `archive_locations` |
| View Promotion Codes | `view_promotion_codes` |
| Edit Promotion Codes | `edit_promotion_codes` |
| Export Promotion Codes | `export_promotion_codes` |
| View Preference Centers | `view_preference_centers` |
| Edit Preference Centers | `edit_preference_centers` |
| Edit Reports | `edit_reports` |
| View Placements | `view_placements` |
| Edit Placements | `edit_placements` |
| Archive Placements | `archive_placements` |
| View Banner Templates | `view_banner_templates` |
| View Multi Language Settings | `view_multi_language_settings` |
| Use BrazeAI Operator<sup>TM</sup> | `use_operator` |
| View Decisioning Studio Agents | `view_decisioning_studio_agents` |
| View Decisioning Studio Audience | `view_decisioning_studio_audience` |
| View Decisioning Studio Conversion Event | `view_decisioning_studio_conversion_event` |
| View Decisioning Studio Guardrails | `view_decisioning_studio_guardrails` |
| Launch Campaigns | `launch_campaigns` |
| Launch Canvases | `launch_canvases` |
| Edit Dashboard Users | `edit_dashboard_users` |
| Edit Media Library Assets | `edit_media_library_assets` |
| Delete Media Library Assets | `delete_media_library_assets` |
| View Import Users | `view_import_users` |
| Import Users | `import_users` |
| Edit User Data | `edit_user_data` |
| View User Merge Records | `view_user_merge_records` |
| Merge Duplicate Users | `merge_duplicate_users` |
| View API Keys | `view_api_keys` |
| Edit API Keys | `edit_api_keys` |
| View Internal Groups | `view_internal_user_groups` |
| Edit Internal Groups | `edit_internal_user_groups` |
| Delete Internal Groups | `delete_internal_user_groups` |
| View Message Activity Log | `view_message_activity_log` |
| View Event User Log | `view_event_user_log` |
| View API Identifiers | `view_api_identifiers` |
| View API Usage Dashboard | `view_api_usage_dashboard` |
| View API Limits | `view_api_limits` |
| View API Usage Alerts | `view_api_usage_alerts` |
| Edit API Usage Alerts | `edit_api_usage_alerts` |
| View SDK Debugger | `view_sdk_debugger` |
| Edit SDK Debugger | `edit_sdk_debugger` |
| Launch Content Blocks | `launch_content_blocks` |
| Edit Cloud Data Ingestion | `edit_cloud_data_ingestion` |
| View App Settings | `view_app_settings` |
| Edit App Settings | `edit_app_settings` |
| View Push Settings | `view_push_settings` |
| Edit Push Settings | `edit_push_settings` |
| View Teams | `view_teams` |
| Edit Teams | `edit_teams` |
| Archive Teams | `archive_teams` |
| View Custom Attributes | `view_custom_attributes` |
| Edit Custom Attributes | `edit_custom_attributes` |
| Blocklist Custom Attributes | `blocklist_custom_attributes` |
| Delete Custom Attributes | `delete_custom_attributes` |
| Export Custom Attributes | `export_custom_attributes` |
| View Custom Events | `view_custom_events` |
| Edit Custom Events | `edit_custom_events` |
| Blocklist Custom Events | `blocklist_custom_events` |
| Delete Custom Events | `delete_custom_events` |
| Export Custom Events | `export_custom_events` |
| Edit Custom Event Property Segmentation | `edit_custom_event_property_segmentation` |
| View Products | `view_products` |
| Edit Products | `edit_products` |
| Blocklist Products | `blocklist_products` |
| Edit Purchase Property Segmentation | `edit_purchase_property_segmentation` |
| View Tags | `view_tags` |
| Edit Tags | `edit_tags` |
| Delete Tags | `delete_tags` |
| View Email Settings | `view_email_settings` |
| Edit Email Settings | `edit_email_settings` |
| View Catalogs | `view_catalogs` |
| Edit Catalogs | `edit_catalogs` |
| Export Catalogs | `export_catalogs` |
| Delete Catalogs | `delete_catalogs` |
| View Whatsapp Settings | `view_whatsapp_settings` |
| Edit Technology Partners | `edit_technology_partners` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Chaînes de permissions d'espace de travail #workspace-strings" }

### Chaînes de permissions Teams {#team}

| Nom de la permission | Chaîne API SCIM |
| --- | --- |
| View Campaigns | `view_campaigns` |
| Edit Campaigns | `edit_campaigns` |
| Archive Campaigns | `archive_campaigns` |
| View Canvases | `view_canvases` |
| Edit Canvases | `edit_canvases` |
| Archive Canvases | `archive_canvases` |
| View Frequency Capping Rules | `view_frequency_caps` |
| Edit Frequency Capping Rules | `edit_frequency_caps` |
| View Message Prioritization | `view_message_prioritization` |
| Edit Message Prioritization | `edit_message_prioritization` |
| View Content Blocks | `view_content_blocks` |
| View Feature Flags | `view_feature_flags` |
| Edit Feature Flags | `edit_feature_flags` |
| Archive Feature Flags | `archive_feature_flags` |
| View Segments | `view_segments` |
| Edit Segments | `edit_segments` |
| Edit Global Control Group | `edit_global_control_group` |
| View IAM Templates | `view_iam_templates` |
| Edit IAM Templates | `edit_iam_templates` |
| Archive IAM Templates | `archive_iam_templates` |
| View Email Templates | `view_email_templates` |
| Edit Email Templates | `edit_email_templates` |
| Archive Email Templates | `archive_email_templates` |
| View Webhook Templates | `view_webhook_templates` |
| Edit Webhook Templates | `edit_webhook_templates` |
| Archive Webhook Templates | `archive_webhook_templates` |
| View Email Link Templates | `view_link_templates` |
| Edit Email Link Templates | `edit_link_templates` |
| View Media Library Assets | `view_media_library_assets` |
| View Locations | `view_locations` |
| Edit Locations | `edit_locations` |
| Archive Locations | `archive_locations` |
| View Promotion Codes | `view_promotion_codes` |
| Edit Promotion Codes | `edit_promotion_codes` |
| Export Promotion Codes | `export_promotion_codes` |
| View Preference Centers | `view_preference_centers` |
| Edit Preference Centers | `edit_preference_centers` |
| View Reports | `view_reports` |
| Create Reports | `create_reports` |
| Edit Reports | `edit_reports` |
| View Banner Templates | `view_banner_templates` |
| View Multi Language Settings | `view_multi_language_settings` |
| Use BrazeAI Operator<sup>TM</sup> | `use_operator` |
| View Decisioning Studio Agents | `view_decisioning_studio_agents` |
| Launch Campaigns | `launch_campaigns` |
| Launch Canvases | `launch_canvases` |
| Edit Dashboard Users | `edit_dashboard_users` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Chaînes de permissions Teams #team" }

### Chaînes de départements {#department-strings}

| Affichage dans l'interface | Chaîne API SCIM |
| --- | --- |
| Agency / Third Party | `agency` |
| BI / Analytics | `bi` |
| C-Suite | `c_suite` |
| Engineering | `engineering` |
| Finance | `finance` |
| Marketing / Editorial | `marketing` |
| Product Management | `pm` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Chaînes de départements" }
{% endsdktab %}
{% sdktab Legacy SCIM API %}


{% alert important %}
Braze propose désormais des [permissions granulaires]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions), un moyen plus flexible de gérer l'accès des utilisateurs. Pour en savoir plus, consultez [Migration vers les permissions granulaires]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) et l'onglet [API SCIM granulaire]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api/) pour afficher les objets et annexes de l'API SCIM granulaire. Braze cessera d'accepter les valeurs de l'API SCIM héritée en décembre 2026.
{% endalert %}

## Objet permissions

L'objet permissions est un champ présent dans certaines requêtes et réponses lors de l'interaction avec la ressource utilisateur via les permissions d'ID SCIM.

{% alert note %}
Les groupes d'applications ont été renommés en espaces de travail dans Braze, mais les clés de cette page font toujours référence à l'ancienne terminologie (par exemple, `appGroup`, `appGroupName`).
{% endalert %}

```
{
  "permissions": {
    "companyPermissions": (required, array),
    "appGroup": (required, array)
  }
}
```

Un objet permissions valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Obligatoire | Type de données | Description |
| --- | --- | --- | --- |
| `companyPermissions` | Facultatif | Tableau | Tableau de chaînes de permissions au niveau de l'entreprise provenant du tableau [Chaînes de permissions d'entreprise]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_company), dans lequel la présence de la chaîne indique que l'utilisateur dispose de la permission correspondante. |
| `roles` | Facultatif | Tableau | Tableau d'[objets rôle]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_role-object). |
| `appGroup` | Obligatoire | Tableau | Tableau d'[objets permissions d'espace de travail]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-permission-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objet permissions" }

### Objet permissions d'espace de travail {#workspace-permission-object}

Un objet permissions d'espace de travail valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Obligatoire | Type de données | Description |
| --- | --- | --- | --- |
| `appGroupName` | Facultatif | Chaîne de caractères | Nom de l'espace de travail. Utilisé pour spécifier à quel espace de travail les permissions contenues dans cet objet s'appliquent. |
| `appGroupId` | Obligatoire si `appGroupName` est absent | Chaîne de caractères | ID de l'espace de travail, servant de méthode alternative pour spécifier l'espace de travail. |
| `appGroupPermissionSets` | Facultatif | Tableau | Tableau contenant un seul [objet ensemble de permissions d'espace de travail]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-permissions-set-object). |
| `appGroupPermissions` | Obligatoire | Tableau | Tableau de chaînes de permissions au niveau de l'espace de travail provenant du tableau [Chaînes de permissions d'espace de travail]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-strings), dans lequel la présence de la chaîne indique que l'utilisateur dispose de la permission correspondante pour l'espace de travail spécifié. |
| `team` | Facultatif | Tableau | Tableau d'[objets permissions Teams]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_team-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objet permissions d'espace de travail #workspace-permission-object" }

### Objet ensemble de permissions d'espace de travail

Un objet ensemble de permissions d'espace de travail valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Obligatoire | Type de données | Description |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | Facultatif | Chaîne de caractères | Nom de l'ensemble de permissions d'espace de travail attribué à l'utilisateur pour cet espace de travail. |
| `appGroupPermissionSetID` | Obligatoire si `appGroupPermissionSetName` est absent | Chaîne de caractères | ID de l'espace de travail, servant de méthode alternative pour spécifier l'ensemble de permissions d'espace de travail attribué à l'utilisateur pour cet espace de travail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objet ensemble de permissions d'espace de travail #workspace-permissions-set-object" }

### Objet permissions Teams

Un objet permissions Teams valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Obligatoire | Type de données | Description |
| --- | --- | --- | --- |
| `teamName` | Facultatif | Chaîne de caractères | Nom de l'équipe, qui peut être utilisé pour spécifier à quelle équipe les permissions contenues dans cet objet s'appliquent. |
| `teamId` | Obligatoire si `teamName` est absent | Chaîne de caractères | ID de l'équipe, servant de méthode alternative pour spécifier l'équipe. |
| `teamPermissions` | Obligatoire | Tableau | Tableau de chaînes de permissions au niveau de l'équipe provenant du tableau [Chaînes de permissions Teams]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_team), dans lequel la présence de la chaîne indique que l'utilisateur dispose de la permission correspondante pour l'équipe spécifiée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objet permissions Teams" }

## Objet rôle

Un objet rôle valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Obligatoire | Type de données | Description |
| --- | --- | --- | --- |
| `roleName` | Facultatif | Chaîne de caractères | Nom du rôle attribué à l'utilisateur. |
| `roleId` | Obligatoire si `roleName` est absent | Chaîne de caractères | ID du rôle, servant de méthode alternative pour spécifier le rôle. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objet rôle" }

## Annexes

### Chaînes de permissions d'entreprise

| Affichage dans l'interface | Chaîne API SCIM |
| --- | --- |
| Administrator | `admin` |
| Can Manage Company Settings | `manage_company_settings` |
| Can Add/Remove Workspaces | `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Chaînes de permissions d'entreprise #company" }

### Chaînes de permissions d'espace de travail

| Nom de la permission | Chaîne API SCIM |
| --- | --- |
| Admin | `admin` |
| Access Campaigns, Canvases, Cards, Segments, Media Library | `basic_access` |
| Approve and Deny Canvases | `approve_deny_campaigns` |
| Send Campaigns, Canvases | `send_campaigns_canvases` |
| Publish Cards | `publish_cards` |
| Edit Segments | `edit_segments` |
| Export User Data | `export_user_data` |
| View PII | `view_pii` |
| View User Profiles PII Compliant | `view_user_profile` |
| Manage Dashboard Users | `manage_dashboard_users` |
| Manage Media Library Assets | `manage_media_library` |
| View Usage Data | `view_usage_data` |
| Import and Update User Data | `import_update_user_data` |
| View Billing Details | `view_billing_details` |
| Access Dev Console | `dev_console` |
| Launch Content Blocks | `launch_content_blocks` |
| Manage External Integrations | `manage_external_integrations` |
| Manage Apps | `manage_apps` |
| Manage Teams | `manage_teams` |
| Manage Events, Attributes, Purchases | `manage_events_attributes_purchases` |
| Manage Tags | `manage_tags` |
| Manage Email Settings | `manage_email_settings` |
| Manage Subscription Groups | `manage_subscription_groups` |
| Manage Approval Settings | `manage_approval_settings` |
| Manage Catalogs Dashboard Permission | `manage_catalogs_dashboard_permission` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Chaînes de permissions d'espace de travail #workspace-strings" }

### Chaînes de permissions Teams

| Nom de la permission | Chaîne API SCIM |
| --- | --- |
| Admin | `admin` |
| Access Campaigns, Canvases, Cards, Segments, Media Library | `basic_access` |
| Approve and Deny Canvases | `approve_deny_campaigns` |
| Send Campaigns, Canvases | `send_campaigns_canvases` |
| Publish Cards | `publish_cards` |
| Edit Segments | `edit_segments` |
| Export User Data | `export_user_data` |
| View User Profile | `view_user_profile` |
| Manage Dashboard Users | `manage_dashboard_users` |
| Manage Media Library Assets | `manage_media_library` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Chaînes de permissions Teams #team" }

### Chaînes de départements

| Affichage dans l'interface | Chaîne API SCIM |
| --- | --- |
| Agency / Third Party | `agency` |
| BI / Analytics | `bi` |
| C-Suite | `c_suite` |
| Engineering | `engineering` |
| Finance | `finance` |
| Marketing / Editorial | `marketing` |
| Product Management | `pm` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Chaînes de départements" }
{% endsdktab %}
{% endsdktabs %}