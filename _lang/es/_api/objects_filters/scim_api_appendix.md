---
nav_title: "Objetos y apéndice de la API SCIM"
article_title: "Objetos y apéndice de la API SCIM"
page_type: reference
description: "Este artículo explica los diferentes objetos de la API SCIM y el apéndice."
alias: /scim_api_appendix/
---

# Objetos y apéndice de la API SCIM {#scim-api-objects-and-appendix}

> Este artículo explica los diferentes objetos de la API SCIM y el apéndice.

{% sdktabs %}
{% sdktab Granular SCIM API %}

## Migración de permisos granulares {#granular-permissions-migration}

Las integraciones SCIM existentes y los [objetos de la API SCIM heredada]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api) siguen funcionando después de la migración de permisos granulares, pero Braze dejará de aceptar valores de la API SCIM heredada en diciembre de 2026.

No es necesario que tomes ninguna acción inmediata. Sin embargo, revisa tus integraciones en busca de permisos que se trasladen a permisos granulares. Por ejemplo, si actualmente envías `basic_access` en la API, actualiza tu integración después de migrar a permisos granulares para incluir los permisos específicos (por ejemplo, `"appGroupPermissions":["view_campaigns","edit_campaigns"]`). Braze sigue aceptando cadenas heredadas, como `basic_access`, después de la migración de permisos granulares para que las integraciones existentes no se rompan.

## Objeto de permisos {#permissions-object}

El objeto de permisos es un campo que se encuentra en algunas de las solicitudes y respuestas al interactuar con el recurso de usuario a través de los permisos de ID SCIM.

{% alert note %}
Los grupos de aplicaciones se han renombrado a espacios de trabajo en Braze, pero las claves en esta página aún hacen referencia a la terminología anterior (por ejemplo, `appGroup`, `appGroupName`).
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

| Clave | Obligatorio | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `companyPermissions` | Opcional | Array | Array de [cadenas de permisos a nivel de empresa]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_company), en la que la presencia de la cadena corresponde a que el usuario tiene el permiso correspondiente. |
| `roles` | Opcional | Array | Array de [objetos de rol]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_role-object). |
| `appGroup` | Obligatorio | Array | Array de [objetos de permisos de espacio de trabajo]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de permisos" }

### Objeto de permisos de espacio de trabajo {#workspace-permissions-object}

Un objeto de permisos de espacio de trabajo válido es un objeto JSON con los siguientes pares clave-valor:

| Clave | Obligatorio | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `appGroupName` | Opcional | String | Nombre del espacio de trabajo. Se utiliza para especificar a qué espacio de trabajo corresponden los permisos contenidos en este objeto. |
| `appGroupId` | Obligatorio si falta `appGroupName` | String | ID del espacio de trabajo, que sirve como método alternativo para especificar el espacio de trabajo. |
| `appGroupPermissionSets` | Opcional | Array | Array con un único [objeto de conjunto de permisos de espacio de trabajo]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-set-object). |
| `appGroupPermissions` | Obligatorio | Array | Array de cadenas de permisos a nivel de espacio de trabajo de la tabla [cadenas de permisos de espacio de trabajo]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-strings), en la que la presencia de la cadena corresponde a que el usuario tiene el permiso correspondiente para el espacio de trabajo especificado. |
| `team` | Opcional | Array | Array de [objetos de permisos de equipo]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de permisos de espacio de trabajo" }

### Objeto de conjunto de permisos de espacio de trabajo {#workspace-permissions-set-object}

Un objeto de conjunto de permisos de espacio de trabajo válido es un objeto JSON con los siguientes pares clave-valor:

| Clave | Obligatorio | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | Opcional | String | Nombre del conjunto de permisos de espacio de trabajo que se asigna al usuario para este espacio de trabajo. |
| `appGroupPermissionSetID` | Obligatorio si falta `appGroupPermissionSetName` | String | ID del espacio de trabajo, que sirve como método alternativo para especificar el conjunto de permisos de espacio de trabajo asignado al usuario para este espacio de trabajo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de conjunto de permisos de espacio de trabajo #workspace-permissions-set-object" }

### Objeto de permisos de equipo {#team-permissions-object}

Un objeto de permisos de equipo válido es un objeto JSON con los siguientes pares clave-valor:

| Clave | Obligatorio | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `teamName` | Opcional | String | Nombre del equipo, que se puede utilizar para especificar a qué equipo corresponden los permisos dentro de este objeto. |
| `teamId` | Obligatorio si falta `teamName` | String | ID del equipo, que sirve como método alternativo para especificar el equipo. |
| `teamPermissions` | Obligatorio | Array | Array de cadenas de permisos a nivel de equipo de la tabla [cadenas de permisos de equipo]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team), en la que la presencia de la cadena corresponde a que el usuario tiene el permiso correspondiente para el equipo especificado. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de permisos de equipo" }

## Objeto de rol {#role-object}

Un objeto de rol válido es un objeto JSON con los siguientes pares clave-valor:

| Clave | Obligatorio | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `roleName` | Opcional | String | Nombre del rol que se asigna al usuario. |
| `roleId` | Obligatorio si falta `roleName` | String | ID del rol, que sirve como método alternativo para especificar el rol. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de rol" }

## Apéndice {#appendix}

### Cadenas de permisos de empresa {#company}

| Como se muestra en la interfaz | Cadena de la API SCIM |
| --- | --- |
| Administrator | `admin` |
| Manage Company Settings | `manage_company_settings` |
| Create and delete workspaces | `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cadenas de permisos de empresa #company" }

### Cadenas de permisos de espacio de trabajo {#workspace-strings}

| Nombre del permiso | Cadena de la API SCIM |
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cadenas de permisos de espacio de trabajo #workspace-strings" }

### Cadenas de permisos de equipo {#team}

| Nombre del permiso | Cadena de la API SCIM |
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cadenas de permisos de equipo #team" }

### Cadenas de departamento {#department-strings}

| Como se muestra en la interfaz | Cadena de la API SCIM |
| --- | --- |
| Agency / Third Party | `agency` |
| BI / Analytics | `bi` |
| C-Suite | `c_suite` |
| Engineering | `engineering` |
| Finance | `finance` |
| Marketing / Editorial | `marketing` |
| Product Management | `pm` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cadenas de departamento" }
{% endsdktab %}
{% sdktab Legacy SCIM API %}


{% alert important %}
Braze ahora ofrece [permisos granulares]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions), una forma más flexible de gestionar el acceso de los usuarios. Para más información, consulta [Migración a permisos granulares]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) y la pestaña [API SCIM granular]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api/) para ver los objetos y el apéndice de la API SCIM granular. Braze dejará de aceptar valores de la API SCIM heredada en diciembre de 2026.
{% endalert %}

## Objeto de permisos

El objeto de permisos es un campo que se encuentra en algunas de las solicitudes y respuestas al interactuar con el recurso de usuario a través de los permisos de ID SCIM.

{% alert note %}
Los grupos de aplicaciones se han renombrado a espacios de trabajo en Braze, pero las claves en esta página aún hacen referencia a la terminología anterior (por ejemplo, `appGroup`, `appGroupName`).
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

| Clave | Obligatorio | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `companyPermissions` | Opcional | Array | Array de cadenas de permisos a nivel de empresa de la tabla [cadenas de permisos de empresa]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_company), en la que la presencia de la cadena corresponde a que el usuario tiene el permiso correspondiente. |
| `roles` | Opcional | Array | Array de [objetos de rol]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_role-object). |
| `appGroup` | Obligatorio | Array | Array de [objetos de permisos de espacio de trabajo]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-permission-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de permisos" }

### Objeto de permisos de espacio de trabajo {#workspace-permission-object}

Un objeto de permisos de espacio de trabajo válido es un objeto JSON con los siguientes pares clave-valor:

| Clave | Obligatorio | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `appGroupName` | Opcional | String | Nombre del espacio de trabajo. Se utiliza para especificar a qué espacio de trabajo corresponden los permisos contenidos en este objeto. |
| `appGroupId` | Obligatorio si falta `appGroupName` | String | ID del espacio de trabajo, que sirve como método alternativo para especificar el espacio de trabajo. |
| `appGroupPermissionSets` | Opcional | Array | Array con un único [objeto de conjunto de permisos de espacio de trabajo]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-permissions-set-object). |
| `appGroupPermissions` | Obligatorio | Array | Array de cadenas de permisos a nivel de espacio de trabajo de la tabla [cadenas de permisos de espacio de trabajo]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-strings), en la que la presencia de la cadena corresponde a que el usuario tiene el permiso correspondiente para el espacio de trabajo especificado. |
| `team` | Opcional | Array | Array de [objetos de permisos de equipo]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_team-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de permisos de espacio de trabajo #workspace-permission-object" }

### Objeto de conjunto de permisos de espacio de trabajo

Un objeto de conjunto de permisos de espacio de trabajo válido es un objeto JSON con los siguientes pares clave-valor:

| Clave | Obligatorio | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | Opcional | String | Nombre del conjunto de permisos de espacio de trabajo que se asigna al usuario para este espacio de trabajo. |
| `appGroupPermissionSetID` | Obligatorio si falta `appGroupPermissionSetName` | String | ID del espacio de trabajo, que sirve como método alternativo para especificar el conjunto de permisos de espacio de trabajo asignado al usuario para este espacio de trabajo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de conjunto de permisos de espacio de trabajo #workspace-permissions-set-object" }

### Objeto de permisos de equipo

Un objeto de permisos de equipo válido es un objeto JSON con los siguientes pares clave-valor:

| Clave | Obligatorio | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `teamName` | Opcional | String | Nombre del equipo, que se puede utilizar para especificar a qué equipo corresponden los permisos dentro de este objeto. |
| `teamId` | Obligatorio si falta `teamName` | String | ID del equipo, que sirve como método alternativo para especificar el equipo. |
| `teamPermissions` | Obligatorio | Array | Array de cadenas de permisos a nivel de equipo de la tabla [cadenas de permisos de equipo]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_team), en la que la presencia de la cadena corresponde a que el usuario tiene el permiso correspondiente para el equipo especificado. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de permisos de equipo" }

## Objeto de rol

Un objeto de rol válido es un objeto JSON con los siguientes pares clave-valor:

| Clave | Obligatorio | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `roleName` | Opcional | String | Nombre del rol que se asigna al usuario. |
| `roleId` | Obligatorio si falta `roleName` | String | ID del rol, que sirve como método alternativo para especificar el rol. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de rol" }

## Apéndice

### Cadenas de permisos de empresa

| Como se muestra en la interfaz | Cadena de la API SCIM |
| --- | --- |
| Administrator | `admin` |
| Can Manage Company Settings | `manage_company_settings` |
| Can Add/Remove Workspaces | `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cadenas de permisos de empresa #company" }

### Cadenas de permisos de espacio de trabajo

| Nombre del permiso | Cadena de la API SCIM |
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cadenas de permisos de espacio de trabajo #workspace-strings" }

### Cadenas de permisos de equipo

| Nombre del permiso | Cadena de la API SCIM |
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cadenas de permisos de equipo #team" }

### Cadenas de departamento

| Como se muestra en la interfaz | Cadena de la API SCIM |
| --- | --- |
| Agency / Third Party | `agency` |
| BI / Analytics | `bi` |
| C-Suite | `c_suite` |
| Engineering | `engineering` |
| Finance | `finance` |
| Marketing / Editorial | `marketing` |
| Product Management | `pm` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cadenas de departamento" }
{% endsdktab %}
{% endsdktabs %}