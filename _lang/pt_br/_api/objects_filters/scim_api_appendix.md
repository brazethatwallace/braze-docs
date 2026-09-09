---
nav_title: "Objetos e apêndice da API SCIM"
article_title: "Objetos e apêndice da API SCIM"
page_type: reference
description: "Este artigo explica os diferentes objetos e o apêndice da API SCIM."
alias: /scim_api_appendix/
---

# Objetos e apêndice da API SCIM {#scim-api-objects-and-appendix}

> Este artigo explica os diferentes objetos e o apêndice da API SCIM.

{% sdktabs %}
{% sdktab Granular SCIM API %}

## Migração para permissões granulares {#granular-permissions-migration}

As integrações SCIM existentes e os [objetos da API SCIM legada]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api) continuam funcionando após a migração para permissões granulares, mas a Braze deixará de aceitar valores da API SCIM legada em dezembro de 2026.

Não é necessário tomar nenhuma ação imediata. No entanto, revise suas integrações para verificar permissões que migram para permissões granulares. Por exemplo, se você está enviando `basic_access` na API atualmente, atualize sua integração após a migração para permissões granulares para incluir as permissões específicas (por exemplo, `"appGroupPermissions":["view_campaigns","edit_campaigns"]`). A Braze continua aceitando strings legadas, como `basic_access`, após a migração para permissões granulares, para que as integrações existentes não sejam interrompidas.

## Objeto de permissões {#permissions-object}

O objeto de permissões é um campo encontrado em algumas das solicitações e respostas ao interagir com o recurso de usuário por meio de permissões de ID SCIM.

{% alert note %}
Os grupos de apps foram renomeados para espaços de trabalho na Braze, mas as chaves nesta página ainda fazem referência à terminologia antiga (por exemplo, `appGroup`, `appGroupName`).
{% endalert %}

```
{
  "permissions": {
    "companyPermissions": (required, array),
    "appGroup": (required, array)
  }
}
```

Um objeto de permissões válido é um objeto JSON com os seguintes pares de chave-valor:

| Chave | Obrigatória | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `companyPermissions` | Opcional | Array | Array de [strings de permissão no nível da empresa]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_company), em que a presença da string corresponde ao usuário ter a permissão correspondente. |
| `roles` | Opcional | Array | Array de [objetos de função]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_role-object). |
| `appGroup` | Obrigatória | Array | Array de [objetos de permissão do espaço de trabalho]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de permissões" }

### Objeto de permissões do espaço de trabalho {#workspace-permissions-object}

Um objeto de permissão do espaço de trabalho válido é um objeto JSON com os seguintes pares de chave-valor:

| Chave | Obrigatória | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `appGroupName` | Opcional | String | Nome do espaço de trabalho. Usado para especificar a qual espaço de trabalho as permissões contidas neste objeto se referem. |
| `appGroupId` | Obrigatória se `appGroupName` estiver ausente | String | ID do espaço de trabalho, servindo como um método alternativo de especificar o espaço de trabalho. |
| `appGroupPermissionSets` | Opcional | Array | Array com um único [objeto de conjunto de permissões do espaço de trabalho]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-set-object). Forneça `appGroupPermissions` ou `appGroupPermissionSets` por entrada de espaço de trabalho, não ambos. |
| `appGroupPermissions` | Condicionalmente obrigatória | Array | Array de strings de permissão no nível do espaço de trabalho da tabela [strings de permissão do espaço de trabalho]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-strings). Obrigatória quando `appGroupPermissionSets` não é fornecido. |
| `team` | Opcional | Array | Array de [objetos de permissão de equipe]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de permissões do espaço de trabalho" }

### Objeto de conjunto de permissões do espaço de trabalho {#workspace-permissions-set-object}

Um objeto de conjunto de permissões do espaço de trabalho válido é um objeto JSON com os seguintes pares de chave-valor:

| Chave | Obrigatória | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | Opcional | String | Nome do conjunto de permissões do espaço de trabalho que está sendo atribuído ao usuário para este espaço de trabalho. |
| `appGroupPermissionSetId` | Obrigatória se `appGroupPermissionSetName` estiver ausente | String | ID do conjunto de permissões do espaço de trabalho, servindo como um método alternativo de especificar o conjunto de permissões do espaço de trabalho atribuído ao usuário para este espaço de trabalho. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de conjunto de permissões do espaço de trabalho #workspace-permissions-set-object" }

### Objeto de permissões de equipe {#team-permissions-object}

Um objeto de permissão de equipe válido é um objeto JSON com os seguintes pares de chave-valor:

| Chave | Obrigatória | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `teamName` | Opcional | String | Nome da equipe, que pode ser usado para especificar a qual equipe as permissões dentro deste objeto se referem. |
| `teamId` | Obrigatória se `teamName` estiver ausente | String | ID da equipe, servindo como um método alternativo de especificar a equipe. |
| `teamPermissions` | Obrigatória | Array | Array de strings de permissão no nível da equipe da tabela [strings de permissão de equipe]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team), em que a presença da string corresponde ao usuário ter a permissão correspondente para a equipe especificada. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de permissões de equipe" }

## Objeto de função {#role-object}

Um objeto de função válido é um objeto JSON com os seguintes pares de chave-valor:

| Chave | Obrigatória | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `roleName` | Opcional | String | Nome da função que está sendo atribuída ao usuário. |
| `roleId` | Obrigatória se `roleName` estiver ausente | String | ID da função, servindo como um método alternativo de especificar a função. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de função" }

## Apêndice {#appendix}

### Strings de permissão da empresa {#company}

| Exibição na interface | String da API SCIM |
| --- | --- |
| Administrator | `admin` |
| Manage Company Settings | `manage_company_settings` |
| Create and delete workspaces | `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Strings de permissão da empresa #company" }

### Strings de permissão do espaço de trabalho {#workspace-strings}

| Nome da permissão | String da API SCIM |
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
| Approve Campaigns | `approve_deny_campaigns` |
| Approve Canvases | `approve_deny_canvases` |
| Send Campaigns, Canvases | `send_campaigns_canvases` |
| Publish Cards | `publish_cards` |
| Export User Data | `export_user_data` |
| View PII | `view_pii` |
| View User Profiles (PII Redacted) | `view_user_profile` |
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Strings de permissão do espaço de trabalho #workspace-strings" }

### Strings de permissão de equipe {#team}

| Nome da permissão | String da API SCIM |
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Strings de permissão de equipe #team" }

### Strings de departamento {#department-strings}

| Exibição na interface | String da API SCIM |
| --- | --- |
| Agency / Third Party | `agency` |
| BI / Analytics | `bi` |
| C-Suite | `c_suite` |
| Engineering | `engineering` |
| Finance | `finance` |
| Marketing / Editorial | `marketing` |
| Product Management | `pm` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Strings de departamento" }
{% endsdktab %}
{% sdktab Legacy SCIM API %}


{% alert important %}
A Braze agora oferece [permissões granulares]({{site.baseurl}}/user_guide/administer/global/user_management/permissions?sdktab=granular%20permissions), uma forma mais flexível de gerenciar o acesso dos usuários. Para saber mais, consulte [Migração para permissões granulares]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) e a guia [API SCIM granular]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api/) para visualizar os objetos e o apêndice da API SCIM granular. A Braze deixará de aceitar valores da API SCIM legada em dezembro de 2026.
{% endalert %}

## Objeto de permissões

O objeto de permissões é um campo encontrado em algumas das solicitações e respostas ao interagir com o recurso de usuário por meio de permissões de ID SCIM.

{% alert note %}
Os grupos de apps foram renomeados para espaços de trabalho na Braze, mas as chaves nesta página ainda fazem referência à terminologia antiga (por exemplo, `appGroup`, `appGroupName`).
{% endalert %}

```
{
  "permissions": {
    "companyPermissions": (required, array),
    "appGroup": (required, array)
  }
}
```

Um objeto de permissões válido é um objeto JSON com os seguintes pares de chave-valor:

| Chave | Obrigatória | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `companyPermissions` | Opcional | Array | Array de strings de permissão no nível da empresa da tabela [Strings de permissão da empresa]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_company), em que a presença da string corresponde ao usuário ter a permissão correspondente. |
| `roles` | Opcional | Array | Array de [objetos de função]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_role-object). |
| `appGroup` | Obrigatória | Array | Array de [objetos de permissão do espaço de trabalho]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-permission-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de permissões" }

### Objeto de permissões do espaço de trabalho {#workspace-permission-object}

Um objeto de permissão do espaço de trabalho válido é um objeto JSON com os seguintes pares de chave-valor:

| Chave | Obrigatória | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `appGroupName` | Opcional | String | Nome do espaço de trabalho. Usado para especificar a qual espaço de trabalho as permissões contidas neste objeto se referem. |
| `appGroupId` | Obrigatória se `appGroupName` estiver ausente | String | ID do espaço de trabalho, servindo como um método alternativo de especificar o espaço de trabalho. |
| `appGroupPermissionSets` | Opcional | Array | Array com um único [objeto de conjunto de permissões do espaço de trabalho]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-permissions-set-object). Forneça `appGroupPermissions` ou `appGroupPermissionSets` por entrada de espaço de trabalho, não ambos. |
| `appGroupPermissions` | Condicionalmente obrigatória | Array | Array de strings de permissão no nível do espaço de trabalho da tabela [strings de permissão do espaço de trabalho]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-strings). Obrigatória quando `appGroupPermissionSets` não é fornecido. |
| `team` | Opcional | Array | Array de [objetos de permissão de equipe]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_team-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de permissões do espaço de trabalho #workspace-permission-object" }

### Objeto de conjunto de permissões do espaço de trabalho

Um objeto de conjunto de permissões do espaço de trabalho válido é um objeto JSON com os seguintes pares de chave-valor:

| Chave | Obrigatória | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | Opcional | String | Nome do conjunto de permissões do espaço de trabalho que está sendo atribuído ao usuário para este espaço de trabalho. |
| `appGroupPermissionSetId` | Obrigatória se `appGroupPermissionSetName` estiver ausente | String | ID do conjunto de permissões do espaço de trabalho, servindo como um método alternativo de especificar o conjunto de permissões do espaço de trabalho atribuído ao usuário para este espaço de trabalho. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de conjunto de permissões do espaço de trabalho #workspace-permissions-set-object" }

### Objeto de permissões de equipe

Um objeto de permissão de equipe válido é um objeto JSON com os seguintes pares de chave-valor:

| Chave | Obrigatória | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `teamName` | Opcional | String | Nome da equipe, que pode ser usado para especificar a qual equipe as permissões dentro deste objeto se referem. |
| `teamId` | Obrigatória se `teamName` estiver ausente | String | ID da equipe, servindo como um método alternativo de especificar a equipe. |
| `teamPermissions` | Obrigatória | Array | Array de strings de permissão no nível da equipe da tabela [strings de permissão de equipe]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_team), em que a presença da string corresponde ao usuário ter a permissão correspondente para a equipe especificada. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de permissões de equipe" }

## Objeto de função

Um objeto de função válido é um objeto JSON com os seguintes pares de chave-valor:

| Chave | Obrigatória | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `roleName` | Opcional | String | Nome da função que está sendo atribuída ao usuário. |
| `roleId` | Obrigatória se `roleName` estiver ausente | String | ID da função, servindo como um método alternativo de especificar a função. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de função" }

## Apêndice

### Strings de permissão da empresa

| Exibição na interface | String da API SCIM |
| --- | --- |
| Administrator | `admin` |
| Can Manage Company Settings | `manage_company_settings` |
| Can Add/Remove Workspaces | `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Strings de permissão da empresa #company" }

### Strings de permissão do espaço de trabalho

| Nome da permissão | String da API SCIM |
| --- | --- |
| Admin | `admin` |
| Access Campaigns, Canvases, Cards, Segments, Media Library | `basic_access` |
| Approve Campaigns | `approve_deny_campaigns` |
| Approve Canvases | `approve_deny_canvases` |
| Send Campaigns, Canvases | `send_campaigns_canvases` |
| Publish Cards | `publish_cards` |
| Edit Segments | `edit_segments` |
| Export User Data | `export_user_data` |
| View PII | `view_pii` |
| View User Profiles (PII Redacted) | `view_user_profile` |
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Strings de permissão do espaço de trabalho #workspace-strings" }

### Strings de permissão de equipe

| Nome da permissão | String da API SCIM |
| --- | --- |
| Admin | `admin` |
| Access Campaigns, Canvases, Cards, Segments, Media Library | `basic_access` |
| Approve Campaigns | `approve_deny_campaigns` |
| Approve Canvases | `approve_deny_canvases` |
| Send Campaigns, Canvases | `send_campaigns_canvases` |
| Publish Cards | `publish_cards` |
| Edit Segments | `edit_segments` |
| Export User Data | `export_user_data` |
| View User Profiles (PII Redacted) | `view_user_profile` |
| Manage Dashboard Users | `manage_dashboard_users` |
| Manage Media Library Assets | `manage_media_library` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Strings de permissão de equipe #team" }

### Strings de departamento

| Exibição na interface | String da API SCIM |
| --- | --- |
| Agency / Third Party | `agency` |
| BI / Analytics | `bi` |
| C-Suite | `c_suite` |
| Engineering | `engineering` |
| Finance | `finance` |
| Marketing / Editorial | `marketing` |
| Product Management | `pm` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Strings de departamento" }
{% endsdktab %}
{% endsdktabs %}