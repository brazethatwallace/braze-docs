---
nav_title: "SCIM-API-Objekte und Anhang"
article_title: "SCIM-API-Objekte und Anhang"
page_type: reference
description: "Dieser Artikel erläutert die verschiedenen SCIM-API-Objekte und den Anhang."
alias: /scim_api_appendix/
---

# SCIM-API-Objekte und Anhang {#scim-api-objects-and-appendix}

> Dieser Artikel erläutert die verschiedenen SCIM-API-Objekte und den Anhang.

{% sdktabs %}
{% sdktab Granular SCIM API %}

## Migration zu granularen Berechtigungen {#granular-permissions-migration}

Bestehende SCIM-Integrationen und [Legacy-SCIM-API-Objekte]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api) funktionieren auch nach der Migration zu granularen Berechtigungen weiterhin, aber Braze wird Legacy-SCIM-API-Werte ab Dezember 2026 nicht mehr akzeptieren.

Sie müssen nicht sofort handeln. Überprüfen Sie jedoch Ihre Integrationen auf Berechtigungen, die zu granularen Berechtigungen migriert werden. Wenn Sie beispielsweise derzeit `basic_access` in der API senden, aktualisieren Sie Ihre Integration nach der Migration zu granularen Berechtigungen, um die spezifischen Berechtigungen einzuschließen (zum Beispiel `"appGroupPermissions":["view_campaigns","edit_campaigns"]`). Braze akzeptiert weiterhin Legacy-Strings wie `basic_access` nach der Migration zu granularen Berechtigungen, damit bestehende Integrationen nicht unterbrochen werden.

## Berechtigungsobjekt {#permissions-object}

Das Berechtigungsobjekt ist ein Feld, das in einigen Anfragen und Antworten bei der Interaktion mit der Nutzerressource über SCIM-ID-Berechtigungen vorkommt.

{% alert note %}
App-Gruppen wurden in Braze in Workspaces umbenannt, aber die Schlüssel auf dieser Seite verwenden weiterhin die alte Terminologie (zum Beispiel `appGroup`, `appGroupName`).
{% endalert %}

```
{
  "permissions": {
    "companyPermissions": (required, array),
    "appGroup": (required, array)
  }
}
```

Ein gültiges Berechtigungsobjekt ist ein JSON-Objekt mit den folgenden Schlüssel-Wert-Paaren:

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `companyPermissions` | Optional | Array | Array von [Berechtigungs-Strings auf Unternehmensebene]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_company), wobei das Vorhandensein des Strings bedeutet, dass die Nutzer:in die entsprechende Berechtigung hat. |
| `roles` | Optional | Array | Array von [Rollenobjekten]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_role-object). |
| `appGroup` | Erforderlich | Array | Array von [Workspace-Berechtigungsobjekten]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Berechtigungsobjekt" }

### Workspace-Berechtigungsobjekt {#workspace-permissions-object}

Ein gültiges Workspace-Berechtigungsobjekt ist ein JSON-Objekt mit den folgenden Schlüssel-Wert-Paaren:

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `appGroupName` | Optional | String | Name des Workspace. Wird verwendet, um anzugeben, für welchen Workspace die in diesem Objekt enthaltenen Berechtigungen gelten. |
| `appGroupId` | Erforderlich, wenn `appGroupName` fehlt | String | ID des Workspace, dient als alternative Methode zur Angabe des Workspace. |
| `appGroupPermissionSets` | Optional | Array | Array mit einem einzelnen [Workspace-Berechtigungsset-Objekt]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-set-object). |
| `appGroupPermissions` | Erforderlich | Array | Array von Berechtigungs-Strings auf Workspace-Ebene aus der Tabelle [Workspace-Berechtigungs-Strings]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-strings), wobei das Vorhandensein des Strings bedeutet, dass die Nutzer:in die entsprechende Berechtigung für den angegebenen Workspace hat. |
| `team` | Optional | Array | Array von [Team-Berechtigungsobjekten]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Workspace-Berechtigungsobjekt" }

### Workspace-Berechtigungsset-Objekt {#workspace-permissions-set-object}

Ein gültiges Workspace-Berechtigungsset-Objekt ist ein JSON-Objekt mit den folgenden Schlüssel-Wert-Paaren:

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | Optional | String | Name des Workspace-Berechtigungssets, das der Nutzer:in für diesen Workspace zugewiesen wird. |
| `appGroupPermissionSetID` | Erforderlich, wenn `appGroupPermissionSetName` fehlt | String | ID des Workspace, dient als alternative Methode zur Angabe des Workspace-Berechtigungssets, das der Nutzer:in für diesen Workspace zugewiesen wird. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Workspace-Berechtigungsset-Objekt" }

### Team-Berechtigungsobjekt {#team-permissions-object}

Ein gültiges Team-Berechtigungsobjekt ist ein JSON-Objekt mit den folgenden Schlüssel-Wert-Paaren:

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `teamName` | Optional | String | Name des Teams, der verwendet werden kann, um anzugeben, für welches Team die Berechtigungen in diesem Objekt gelten. |
| `teamId` | Erforderlich, wenn `teamName` fehlt | String | ID des Teams, dient als alternative Methode zur Angabe des Teams. |
| `teamPermissions` | Erforderlich | Array | Array von Berechtigungs-Strings auf Team-Ebene aus der Tabelle [Team-Berechtigungs-Strings]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team), wobei das Vorhandensein des Strings bedeutet, dass die Nutzer:in die entsprechende Berechtigung für das angegebene Team hat. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Team-Berechtigungsobjekt" }

## Rollenobjekt {#role-object}

Ein gültiges Rollenobjekt ist ein JSON-Objekt mit den folgenden Schlüssel-Wert-Paaren:

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `roleName` | Optional | String | Name der Rolle, die der Nutzer:in zugewiesen wird. |
| `roleId` | Erforderlich, wenn `roleName` fehlt | String | ID der Rolle, dient als alternative Methode zur Angabe der Rolle. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Rollenobjekt" }

## Anhang {#appendix}

### Unternehmens-Berechtigungs-Strings {#company}

| Anzeige in der UI | SCIM-API-String |
| --- | --- |
| Administrator | `admin` |
| Manage Company Settings | `manage_company_settings` |
| Create and delete workspaces | `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Unternehmens-Berechtigungs-Strings" }

### Workspace-Berechtigungs-Strings {#workspace-strings}

| Berechtigungsname | SCIM-API-String |
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Workspace-Berechtigungs-Strings" }

### Team-Berechtigungs-Strings {#team}

| Berechtigungsname | SCIM-API-String |
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Team-Berechtigungs-Strings" }

### Abteilungs-Strings {#department-strings}

| Anzeige in der UI | SCIM-API-String |
| --- | --- |
| Agency / Third Party | `agency` |
| BI / Analytics | `bi` |
| C-Suite | `c_suite` |
| Engineering | `engineering` |
| Finance | `finance` |
| Marketing / Editorial | `marketing` |
| Product Management | `pm` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Abteilungs-Strings" }
{% endsdktab %}
{% sdktab Legacy SCIM API %}


{% alert important %}
Braze bietet jetzt [granulare Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions), eine flexiblere Möglichkeit, den Zugriff von Nutzer:innen zu verwalten. Weitere Informationen finden Sie unter [Migration zu granularen Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) und im Tab [Granular SCIM API]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api/), um die granularen SCIM-API-Objekte und den Anhang einzusehen. Braze wird ab Dezember 2026 keine Legacy-SCIM-API-Werte mehr akzeptieren.
{% endalert %}

## Berechtigungsobjekt

Das Berechtigungsobjekt ist ein Feld, das in einigen Anfragen und Antworten bei der Interaktion mit der Nutzerressource über SCIM-ID-Berechtigungen vorkommt.

{% alert note %}
App-Gruppen wurden in Braze in Workspaces umbenannt, aber die Schlüssel auf dieser Seite verwenden weiterhin die alte Terminologie (zum Beispiel `appGroup`, `appGroupName`).
{% endalert %}

```
{
  "permissions": {
    "companyPermissions": (required, array),
    "appGroup": (required, array)
  }
}
```

Ein gültiges Berechtigungsobjekt ist ein JSON-Objekt mit den folgenden Schlüssel-Wert-Paaren:

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `companyPermissions` | Optional | Array | Array von Berechtigungs-Strings auf Unternehmensebene aus der Tabelle [Unternehmens-Berechtigungs-Strings]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_company), wobei das Vorhandensein des Strings bedeutet, dass die Nutzer:in die entsprechende Berechtigung hat. |
| `roles` | Optional | Array | Array von [Rollenobjekten]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_role-object). |
| `appGroup` | Erforderlich | Array | Array von [Workspace-Berechtigungsobjekten]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-permission-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Berechtigungsobjekt" }

### Workspace-Berechtigungsobjekt {#workspace-permission-object}

Ein gültiges Workspace-Berechtigungsobjekt ist ein JSON-Objekt mit den folgenden Schlüssel-Wert-Paaren:

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `appGroupName` | Optional | String | Name des Workspace. Wird verwendet, um anzugeben, für welchen Workspace die in diesem Objekt enthaltenen Berechtigungen gelten. |
| `appGroupId` | Erforderlich, wenn `appGroupName` fehlt | String | ID des Workspace, dient als alternative Methode zur Angabe des Workspace. |
| `appGroupPermissionSets` | Optional | Array | Array mit einem einzelnen [Workspace-Berechtigungsset-Objekt]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-permissions-set-object). |
| `appGroupPermissions` | Erforderlich | Array | Array von Berechtigungs-Strings auf Workspace-Ebene aus der Tabelle [Workspace-Berechtigungs-Strings]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-strings), wobei das Vorhandensein des Strings bedeutet, dass die Nutzer:in die entsprechende Berechtigung für den angegebenen Workspace hat. |
| `team` | Optional | Array | Array von [Team-Berechtigungsobjekten]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_team-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Workspace-Berechtigungsobjekt" }

### Workspace-Berechtigungsset-Objekt {#workspace-permissions-set-object}

Ein gültiges Workspace-Berechtigungsset-Objekt ist ein JSON-Objekt mit den folgenden Schlüssel-Wert-Paaren:

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | Optional | String | Name des Workspace-Berechtigungssets, das der Nutzer:in für diesen Workspace zugewiesen wird. |
| `appGroupPermissionSetID` | Erforderlich, wenn `appGroupPermissionSetName` fehlt | String | ID des Workspace, dient als alternative Methode zur Angabe des Workspace-Berechtigungssets, das der Nutzer:in für diesen Workspace zugewiesen wird. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Workspace-Berechtigungsset-Objekt" }

### Team-Berechtigungsobjekt {#team-permissions-object}

Ein gültiges Team-Berechtigungsobjekt ist ein JSON-Objekt mit den folgenden Schlüssel-Wert-Paaren:

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `teamName` | Optional | String | Name des Teams, der verwendet werden kann, um anzugeben, für welches Team die Berechtigungen in diesem Objekt gelten. |
| `teamId` | Erforderlich, wenn `teamName` fehlt | String | ID des Teams, dient als alternative Methode zur Angabe des Teams. |
| `teamPermissions` | Erforderlich | Array | Array von Berechtigungs-Strings auf Team-Ebene aus der Tabelle [Team-Berechtigungs-Strings]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_team), wobei das Vorhandensein des Strings bedeutet, dass die Nutzer:in die entsprechende Berechtigung für das angegebene Team hat. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Team-Berechtigungsobjekt" }

## Rollenobjekt {#role-object}

Ein gültiges Rollenobjekt ist ein JSON-Objekt mit den folgenden Schlüssel-Wert-Paaren:

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `roleName` | Optional | String | Name der Rolle, die der Nutzer:in zugewiesen wird. |
| `roleId` | Erforderlich, wenn `roleName` fehlt | String | ID der Rolle, dient als alternative Methode zur Angabe der Rolle. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Rollenobjekt" }

## Anhang

### Unternehmens-Berechtigungs-Strings {#company}

| Anzeige in der UI | SCIM-API-String |
| --- | --- |
| Administrator | `admin` |
| Can Manage Company Settings | `manage_company_settings` |
| Can Add/Remove Workspaces | `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Unternehmens-Berechtigungs-Strings" }

### Workspace-Berechtigungs-Strings {#workspace-strings}

| Berechtigungsname | SCIM-API-String |
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Workspace-Berechtigungs-Strings" }

### Team-Berechtigungs-Strings {#team}

| Berechtigungsname | SCIM-API-String |
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Team-Berechtigungs-Strings" }

### Abteilungs-Strings

| Anzeige in der UI | SCIM-API-String |
| --- | --- |
| Agency / Third Party | `agency` |
| BI / Analytics | `bi` |
| C-Suite | `c_suite` |
| Engineering | `engineering` |
| Finance | `finance` |
| Marketing / Editorial | `marketing` |
| Product Management | `pm` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Abteilungs-Strings" }
{% endsdktab %}
{% endsdktabs %}