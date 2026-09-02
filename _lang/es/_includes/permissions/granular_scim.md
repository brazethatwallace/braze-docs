## Migración de permisos granulares {#granular-permissions-migration}

Las integraciones SCIM existentes y [los objetos API SCIM heredados]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api) seguirán funcionando después de la migración de permisos granulares a finales de abril.

No es necesario que tomes ninguna medida inmediata. Sin embargo, te recomendamos que revises tus integraciones para ver si hay permisos que vayan a ser granularizados. Por ejemplo, si actualmente estás enviando `basic_access` en la API, te sugerimos que actualices tu integración después de la granularización para incluir los permisos específicos (por ejemplo, `"appGroupPermissions":["view_campaigns","edit_campaigns"]`). Braze seguirá aceptando cadenas heredadas, como `basic_access`, después de la migración de permisos granulares, para que las integraciones existentes no se vean afectadas.

## Objeto de permisos {#permissions-object}

El objeto de permisos es un campo que se encuentra en algunas de las peticiones y respuestas cuando se interactúa con el recurso de usuario a través de los permisos de ID SCIM.

{% alert note %}
Los grupos de aplicaciones han pasado a llamarse espacios de trabajo en Braze, pero las claves de esta página siguen haciendo referencia a la terminología antigua (por ejemplo, `appGroup`, `appGroupName`).
{% endalert %}

```
{
  "permissions": {
    "companyPermissions": (required, array),
    "appGroup": (required, array)
  }
}
```

Un objeto de permisos válido es un objeto JSON con los siguientes pares clave-valor:

| Clave | Obligatoria | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `companyPermissions` | Opcional | Matriz | Matriz de [cadenas de permisos a nivel de empresa]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_company), en la que la presencia de la cadena corresponde a que el usuario tiene el permiso correspondiente. |
| `roles` | Opcional | Matriz | Matriz de [objetos de rol]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_role-object). |
| `appGroup` | Obligatoria | Matriz | Matriz de [objetos de permisos del espacio de trabajo]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de permisos" }

### Objeto de permisos del espacio de trabajo {#workspace-permissions-object}

Un objeto de permisos del espacio de trabajo válido es un objeto JSON con los siguientes pares clave-valor:

| Clave | Obligatoria | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `appGroupName` | Opcional | Cadena | Nombre del espacio de trabajo. Sirve para especificar a qué espacio de trabajo corresponden los permisos contenidos en este objeto. |
| `appGroupId` | Obligatorio si falta `appGroupName` | Cadena | ID del espacio de trabajo, que sirve como método alternativo para especificar el espacio de trabajo. |
| `appGroupPermissionSets` | Opcional | Matriz | Matriz con un único [objeto de conjunto de permisos del espacio de trabajo]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-set-object). |
| `appGroupPermissions` | Obligatoria | Matriz | Matriz de cadenas de permisos a nivel del espacio de trabajo de la tabla de [cadenas de permisos del espacio de trabajo]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-strings), en la que la presencia de la cadena corresponde a que el usuario tiene el permiso correspondiente para el espacio de trabajo especificado. |
| `team` | Opcional | Matriz | Matriz de [objetos de permisos del equipo]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de permisos del espacio de trabajo" }

### Objeto de conjunto de permisos del espacio de trabajo {#workspace-permissions-set-object}

Un objeto de conjunto de permisos del espacio de trabajo válido es un objeto JSON con los siguientes pares clave-valor:

| Clave | Obligatoria | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | Opcional | Cadena | Nombre del conjunto de permisos del espacio de trabajo que se está asignando al usuario para este espacio de trabajo. |
| `appGroupPermissionSetID` | Obligatorio si falta `appGroupPermissionSetName` | Cadena | ID del espacio de trabajo, que sirve como método alternativo para especificar el conjunto de permisos del espacio de trabajo asignado al usuario para este espacio de trabajo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de conjunto de permisos del espacio de trabajo" }

### Objeto de permisos del equipo {#team-permissions-object}

Un objeto de permisos del equipo válido es un objeto JSON con los siguientes pares clave-valor:

| Clave | Obligatoria | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `teamName` | Opcional | Cadena | Nombre del equipo, que puede utilizarse para especificar a qué equipo corresponden los permisos de este objeto. |
| `teamId` | Obligatorio si falta `teamName` | Cadena | ID del equipo, que sirve como método alternativo para especificar el equipo. |
| `teamPermissions` | Obligatoria | Matriz | Matriz de cadenas de permisos a nivel de equipo de la tabla de [cadenas de permisos del equipo]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team), en la que la presencia de la cadena corresponde a que el usuario tiene el permiso correspondiente para el equipo especificado. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de permisos del equipo" }

## Objeto de rol {#role-object}

Un objeto de rol válido es un objeto JSON con los siguientes pares clave-valor:

| Clave | Obligatoria | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `roleName` | Opcional | Cadena | Nombre del rol que se está asignando al usuario. |
| `roleId` | Obligatorio si falta `roleName` | Cadena | ID del rol, que sirve como método alternativo para especificar el rol. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de rol" }

## Anexo {#appendix}

### Cadenas de permisos de empresa {#company}

| Como se muestra en la IU | Cadena API SCIM |
| --- | --- |
| Administrator | `admin` |
| Manage Company Settings | `manage_company_settings` |
| Create and delete workspaces| `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cadenas de permisos de empresa" }

### Cadenas de permisos del espacio de trabajo {#workspace-strings}

| Nombre del permiso | Cadena API SCIM |
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
| Import Users	| `import_users` |
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
| View SDK or kit de desarrollo de software Debugger | `view_sdk_debugger` |
| Edit SDK or kit de desarrollo de software Debugger | `edit_sdk_debugger` |
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
| View Custom Events	 | `view_custom_events` |
| Edit Custom Events | `edit_custom_events` |
| Blocklist Custom Events | `blocklist_custom_events` |
| Delete Custom Events | `delete_custom_events` |
| Export Custom Events | `export_custom_events` |
| Edit Custom Event Property Segmentation | `edit_custom_event_property_segmentation` |
| View Products | `view_products` |
| Edit Products	 | `edit_products` |
| Blocklist Products | `blocklist_products` |
| Edit Purchase Property Segmentation | `edit_purchase_property_segmentation` |
| View Tags | `view_tags` |
| Edit Tags | `edit_tags` |
| Delete Tags | `delete_tags` |
| View Email Settings	| `view_email_settings` |
| Edit Email Settings | `edit_email_settings` |
| View Catalogs | `view_catalogs` |
| Edit Catalogs	 | `edit_catalogs` |
| Export Catalogs | `export_catalogs` |
| Delete Catalogs | `delete_catalogs` |
| View Whatsapp Settings | `view_whatsapp_settings` |
| Edit Technology Partners | `edit_technology_partners` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cadenas de permisos del espacio de trabajo" }

### Cadenas de permisos del equipo {#team}

| Nombre del permiso | Cadena API SCIM |
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cadenas de permisos del equipo" }

### Cadenas de departamento {#department-strings}

| Como se muestra en la IU | Cadena API SCIM |
| --- | --- |
| Agency / Third Party | `agency` |
| BI / Analytics | `bi` |
| C-Suite | `c_suite` |
| Engineering | `engineering` |
| Finance | `finance` |
| Marketing / Editorial | `marketing` |
| Product Management | `pm` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cadenas de departamento" }