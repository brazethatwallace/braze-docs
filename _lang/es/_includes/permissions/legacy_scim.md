{% alert important %}
Braze presenta [los permisos granulares]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions), una forma más flexible de administrar el acceso de los usuarios. Consulta [Migración a permisos granulares]({{site.baseurl}}/granular_permissions_migration) para obtener más información sobre el proceso de migración, y la pestaña [API SCIM granular]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api/) para ver los objetos de la API SCIM granular y el apéndice.
{% endalert %}

## Objeto permisos {#permissions-object}

El objeto permisos es un campo que se encuentra en algunas de las solicitudes y respuestas cuando se interactúa con el recurso usuario a través de los permisos de ID SCIM.

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
| `companyPermissions` | Opcional | Matriz | Matriz de cadenas de permisos a nivel de empresa de la tabla [Cadenas de permisos de empresa]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_company), en la que la presencia de la cadena indica que el usuario tiene el permiso correspondiente. |
| `roles` | Opcional | Matriz | Matriz de [objetos de rol]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_role-object). |
| `appGroup` | Obligatoria | Matriz | Matriz de [objetos de permisos del espacio de trabajo]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-permissions-set-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto permisos" }

### Objeto de permisos del espacio de trabajo {#workspace-permission-object}

Un objeto de permisos de grupo de aplicaciones válido es un objeto JSON con los siguientes pares clave-valor:

| Clave | Obligatoria | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `appGroupName` | Opcional | Cadena | Nombre del espacio de trabajo. Sirve para especificar a qué espacio de trabajo corresponden los permisos contenidos en este objeto. |
| `appGroupId` | Obligatorio si falta `appGroupName` | Cadena | ID del espacio de trabajo, que sirve como método alternativo para especificar el espacio de trabajo. |
| `appGroupPermissionSets` | Opcional | Matriz | Matriz con un único [objeto de conjunto de permisos del espacio de trabajo]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-permissions-set-object). |
| `appGroupPermissions` | Obligatoria | Matriz | Matriz de cadenas de permisos a nivel del espacio de trabajo de la tabla de [cadenas de permisos del espacio de trabajo]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-strings), en la que la presencia de la cadena indica que el usuario tiene el permiso correspondiente para el espacio de trabajo especificado. |
| `team` | Opcional | Matriz | Matriz de [objetos de permisos del equipo]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_team-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de permisos del espacio de trabajo #workspace-permission-object" }

### Objeto de conjunto de permisos del espacio de trabajo {#workspace-permissions-set-object}

Un objeto de conjunto de permisos del espacio de trabajo válido es un objeto JSON con los siguientes pares clave-valor:

| Clave | Obligatoria | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | Opcional | Cadena | Nombre del conjunto de permisos del espacio de trabajo que se está asignando al usuario para este espacio de trabajo. |
| `appGroupPermissionSetID` | Obligatorio si falta `appGroupPermissionSetName` | Cadena | ID del espacio de trabajo, que sirve como método alternativo para especificar el conjunto de permisos del espacio de trabajo asignado al usuario para este espacio de trabajo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de conjunto de permisos del espacio de trabajo #workspace-permissions-set-object" }

### Objeto de permisos del equipo {#team-permissions-object}

Un objeto de permisos del equipo válido es un objeto JSON con los siguientes pares clave-valor:

| Clave | Obligatoria | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `teamName` | Opcional | Cadena | Nombre del equipo, que puede utilizarse para especificar a qué equipo corresponden los permisos de este objeto. |
| `teamId` | Obligatorio si falta `teamName` | Cadena | ID del equipo, que sirve como método alternativo para especificar el equipo. |
| `teamPermissions` | Obligatoria | Matriz | Matriz de cadenas de permisos a nivel de equipo de la tabla de [cadenas de permisos de equipos]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_team), en la que la presencia de la cadena indica que el usuario tiene el permiso correspondiente para el equipo especificado. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de permisos del equipo" }

## Objeto de rol {#role-object}

Un objeto de rol válido es un objeto JSON con los siguientes pares clave-valor:

| Clave | Obligatoria | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `roleName` | Opcional | Cadena | Nombre del rol que se está asignando al usuario. |
| `roleId` | Obligatorio si falta `roleName` | Cadena | ID del rol, que sirve como método alternativo para especificar el rol. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de rol" }

## Apéndice {#appendix}

### Cadenas de permisos de empresa {#company}

| Como se muestra en la IU | Cadena API SCIM |
| --- | --- |
| Administrator | `admin` |
| Can Manage Company Settings | `manage_company_settings` |
| Can Add/Remove Workspaces | `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cadenas de permisos de empresa #company" }

### Cadenas de permisos del espacio de trabajo {#workspace-strings}

| Nombre del permiso | Cadena API SCIM |
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cadenas de permisos del espacio de trabajo #workspace-strings" }

### Cadenas de permisos del equipo {#team}

| Nombre del permiso | Cadena API SCIM |
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cadenas de permisos del equipo #team" }

### Cadenas del departamento {#department-strings}

| Como se muestra en la IU | Cadena API SCIM |
| --- | --- |
| Agency / Third Party | `agency` |
| BI / Analytics | `bi` |
| C-Suite | `c_suite` |
| Engineering | `engineering` |
| Finance | `finance` |
| Marketing / Editorial | `marketing` |
| Product Management | `pm` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cadenas del departamento" }