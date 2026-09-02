{% alert important %}
A Braze está introduzindo [permissões granulares]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions), uma forma mais flexível de gerenciar o acesso do usuário. Consulte [Migrando para permissões granulares]({{site.baseurl}}/granular_permissions_migration) para saber mais sobre o processo de migração, e a guia [API or interface de programação do aplicativo (API) SCIM granular]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api/) para visualizar os objetos e o apêndice da API or interface de programação do aplicativo (API) SCIM granular.
{% endalert %}

## Objeto de permissões {#permissions-object}

O objeto de permissões é um campo encontrado em algumas das solicitações e respostas ao interagir com o recurso de usuário por meio de permissões de ID SCIM.

{% alert note %}
Os grupos de apps foram renomeados como espaços de trabalho na Braze, mas as chaves nesta página ainda fazem referência à terminologia antiga (por exemplo, `appGroup`, `appGroupName`).
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
| `companyPermissions` | Opcional | Vetor | Vetor de strings de permissão no nível da empresa da tabela de [strings de permissão da empresa]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_company), na qual a presença da string corresponde ao usuário ter a permissão correspondente. |
| `roles` | Opcional | Vetor | Vetor de [objetos de função]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_role-object). |
| `appGroup` | Obrigatória | Vetor | Vetor de [objetos de permissão do espaço de trabalho]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-permissions-set-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de permissões" }

### Objeto de permissões do espaço de trabalho {#workspace-permission-object}

Um objeto de permissão de grupo de apps válido é um objeto JSON com os seguintes pares de chave-valor:

| Chave | Obrigatória | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `appGroupName` | Opcional | String | Nome do espaço de trabalho. Usado para especificar para qual espaço de trabalho as permissões contidas nesse objeto se destinam. |
| `appGroupId` | Obrigatória se `appGroupName` estiver ausente | String | ID do espaço de trabalho, servindo como um método alternativo de especificação do espaço de trabalho. |
| `appGroupPermissionSets` | Opcional | Vetor | Vetor com um único [objeto de conjunto de permissões do espaço de trabalho]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-permissions-set-object). |
| `appGroupPermissions` | Obrigatória | Vetor | Vetor de strings de permissão no nível do espaço de trabalho da tabela de [strings de permissão do espaço de trabalho]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-strings), na qual a presença da string corresponde ao usuário ter a permissão correspondente para o espaço de trabalho especificado. |
| `team` | Opcional | Vetor | Vetor de [objetos de permissão da equipe]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_team-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de permissões do espaço de trabalho #workspace-permission-object" }

### Objeto do conjunto de permissões do espaço de trabalho {#workspace-permissions-set-object}

Um objeto válido de conjunto de permissões do espaço de trabalho é um objeto JSON com os seguintes pares de chave-valor:

| Chave | Obrigatória | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | Opcional | String | Nome do conjunto de permissões do espaço de trabalho que está sendo atribuído ao usuário para esse espaço de trabalho. |
| `appGroupPermissionSetID` | Obrigatória se `appGroupPermissionSetName` estiver ausente | String | ID do espaço de trabalho, servindo como um método alternativo de especificar o conjunto de permissões do espaço de trabalho atribuído ao usuário para esse espaço de trabalho. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto do conjunto de permissões do espaço de trabalho #workspace-permissions-set-object" }

### Objeto de permissões da equipe {#team-permissions-object}

Um objeto de permissão de equipe válido é um objeto JSON com os seguintes pares de chave-valor:

| Chave | Obrigatória | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `teamName` | Opcional | String | Nome da equipe, que pode ser usado para especificar a qual equipe se destinam as permissões desse objeto. |
| `teamId` | Obrigatória se `teamName` estiver ausente | String | ID da equipe, servindo como um método alternativo de especificar a equipe. |
| `teamPermissions` | Obrigatória | Vetor | Vetor de strings de permissão no nível da equipe da tabela de [strings de permissão da equipe]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_team), na qual a presença da string corresponde ao usuário ter a permissão correspondente para a equipe especificada. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de permissões da equipe" }

## Objeto de função {#role-object}

Um objeto de função válido é um objeto JSON com os seguintes pares de chave-valor:

| Chave | Obrigatória | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `roleName` | Opcional | String | Nome da função que está sendo atribuída ao usuário. |
| `roleId` | Obrigatória se `roleName` estiver ausente | String | ID da função, servindo como um método alternativo de especificação da função. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objeto de função" }

## Apêndice {#appendix}

### Strings de permissão da empresa {#company}

| Conforme exibido na interface do usuário | String da API or interface de programação do aplicativo (API) SCIM |
| --- | --- |
| Administrator | `admin` |
| Can Manage Company Settings | `manage_company_settings` |
| Can Add/Remove Workspaces | `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Strings de permissão da empresa #company" }

### Strings de permissão do espaço de trabalho {#workspace-strings}

| Nome da permissão | String da API or interface de programação do aplicativo (API) SCIM |
| --- | --- |
| Admin | `admin` |
| Access Campaigns, Canvases, Cards, Segments, Media Library | `basic_access` |
| Approve and Deny Canvases | `approve_deny_campaigns` |
| Send Campaigns, Canvases | `send_campaigns_canvases` |
| Publish Cards | `publish_cards` |
| Edit Segments | `edit_segments` |
| Export User Data | `export_user_data` |
| View IPI | `view_pii` |
| View User Profiles IPI Compliant | `view_user_profile` |
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

### Strings de permissão da equipe {#team}

| Nome da permissão | String da API or interface de programação do aplicativo (API) SCIM |
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Strings de permissão da equipe #team" }

### Strings do departamento {#department-strings}

| Conforme exibido na interface do usuário | String da API or interface de programação do aplicativo (API) SCIM |
| --- | --- |
| Agency / Third Party | `agency` |
| BI / Analytics | `bi` |
| C-Suite | `c_suite` |
| Engineering | `engineering` |
| Finance | `finance` |
| Marketing / Editorial | `marketing` |
| Product Management | `pm` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Strings do departamento" }