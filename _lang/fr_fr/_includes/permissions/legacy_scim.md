{% alert important %}
Braze introduit les [autorisations granulaires]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions), une méthode plus flexible pour gérer l'accès des utilisateurs. Consultez la section [Migration vers les autorisations granulaires]({{site.baseurl}}/granular_permissions_migration) pour en savoir plus sur le processus de migration, ainsi que l'onglet [API SCIM granulaire]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api/) pour afficher les objets API SCIM granulaires et l'annexe.
{% endalert %}

## Objet Autorisations {#permissions-object}

L'objet Autorisations est un champ que l'on retrouve dans certaines demandes et réponses lors de l'interaction avec la ressource utilisateur via les autorisations de l'ID SCIM.

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

Un objet Autorisations valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Requis | Type de données | Description |
| --- | --- | --- | --- |
| `companyPermissions` | Facultatif | Tableau | Tableau de chaînes de caractères d'autorisations au niveau de l'entreprise provenant du tableau des [chaînes de caractères d'autorisations de l'entreprise]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_company), dans lequel la présence de la chaîne correspond à l'utilisateur disposant de l'autorisation correspondante. |
| `roles` | Facultatif | Tableau | Tableau d'[objets de rôle]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_role-object). |
| `appGroup` | Requis | Tableau | Tableau d'[objets d'autorisations de l'espace de travail]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-permissions-set-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objet Autorisations" }

### Objet d'autorisations de l'espace de travail {#workspace-permission-object}

Un objet d'autorisations de groupe d'applications valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Requis | Type de données | Description |
| --- | --- | --- | --- |
| `appGroupName` | Facultatif | Chaîne de caractères | Nom de l'espace de travail. Utilisé pour spécifier l'espace de travail pour lequel les autorisations contenues dans cet objet s'appliquent. |
| `appGroupId` | Requis si `appGroupName` est absent | Chaîne de caractères | ID de l'espace de travail, servant de méthode alternative pour spécifier l'espace de travail. |
| `appGroupPermissionSets` | Facultatif | Tableau | Tableau contenant un seul [objet ensemble d'autorisations de l'espace de travail]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-permissions-set-object). |
| `appGroupPermissions` | Requis | Tableau | Tableau de chaînes de caractères d'autorisations au niveau de l'espace de travail provenant du tableau des [chaînes de caractères d'autorisations de l'espace de travail]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-strings), dans lequel la présence de la chaîne correspond à l'utilisateur disposant de l'autorisation correspondante pour l'espace de travail donné. |
| `team` | Facultatif | Tableau | Tableau d'[objets d'autorisations d'équipe]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_team-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objet d'autorisations de l'espace de travail #workspace-permission-object" }

### Objet ensemble d'autorisations de l'espace de travail {#workspace-permissions-set-object}

Un objet ensemble d'autorisations de l'espace de travail valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Requis | Type de données | Description |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | Facultatif | Chaîne de caractères | Nom de l'ensemble d'autorisations de l'espace de travail attribué à l'utilisateur pour cet espace de travail. |
| `appGroupPermissionSetID` | Requis si `appGroupPermissionSetName` est absent | Chaîne de caractères | ID de l'espace de travail, servant de méthode alternative pour spécifier l'ensemble d'autorisations de l'espace de travail attribué à l'utilisateur pour cet espace de travail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objet ensemble d'autorisations de l'espace de travail #workspace-permissions-set-object" }

### Objet d'autorisations d'équipe {#team-permissions-object}

Un objet d'autorisations d'équipe valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Requis | Type de données | Description |
| --- | --- | --- | --- |
| `teamName` | Facultatif | Chaîne de caractères | Nom de l'équipe, qui peut être utilisé pour spécifier à quelle équipe sont destinées les autorisations de cet objet. |
| `teamId` | Requis si `teamName` est absent | Chaîne de caractères | ID de l'équipe, servant de méthode alternative pour spécifier l'équipe. |
| `teamPermissions` | Requis | Tableau | Tableau de chaînes de caractères d'autorisations au niveau de l'équipe provenant du tableau des [chaînes de caractères d'autorisations des équipes]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_team), dans lequel la présence de la chaîne correspond à l'utilisateur disposant de l'autorisation correspondante pour l'équipe spécifiée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objet d'autorisations d'équipe" }

## Objet de rôle {#role-object}

Un objet de rôle valide est un objet JSON avec les paires clé-valeur suivantes :

| Clé | Requis | Type de données | Description |
| --- | --- | --- | --- |
| `roleName` | Facultatif | Chaîne de caractères | Nom du rôle attribué à l'utilisateur. |
| `roleId` | Requis si `roleName` est absent | Chaîne de caractères | ID du rôle, servant de méthode alternative pour spécifier le rôle. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Objet de rôle" }

## Annexe {#appendix}

### Chaînes de caractères d'autorisations de l'entreprise {#company}

| Telles qu'affichées dans l'interface utilisateur | Chaîne de caractères API SCIM |
| --- | --- |
| Administrateur | `admin` |
| Peut gérer les paramètres de l'entreprise | `manage_company_settings` |
| Peut ajouter/supprimer des espaces de travail | `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Chaînes de caractères d'autorisations de l'entreprise #company" }

### Chaînes de caractères d'autorisations de l'espace de travail {#workspace-strings}

| Nom de l'autorisation | Chaîne de caractères API SCIM |
| --- | --- |
| Admin | `admin` |
| Accéder aux Campaigns, Canvas, cartes, Segments, bibliothèque multimédia | `basic_access` |
| Approuver et refuser des Canvas | `approve_deny_campaigns` |
| Envoyer des Campaigns, Canvas | `send_campaigns_canvases` |
| Publier des cartes | `publish_cards` |
| Modifier les Segments | `edit_segments` |
| Exporter les données utilisateur | `export_user_data` |
| Afficher les données d'identification | `view_pii` |
| Voir les profils utilisateur conformes aux données d'identification | `view_user_profile` |
| Gérer les utilisateurs du tableau de bord | `manage_dashboard_users` |
| Gérer les ressources de la bibliothèque multimédia | `manage_media_library` |
| Afficher les données d'utilisation | `view_usage_data` |
| Importer et mettre à jour les données utilisateur | `import_update_user_data` |
| Afficher les détails de facturation | `view_billing_details` |
| Accéder à la console de développement | `dev_console` |
| Lancer des Content Blocks | `launch_content_blocks` |
| Gérer les intégrations externes | `manage_external_integrations` |
| Gérer les applications | `manage_apps` |
| Gérer les équipes | `manage_teams` |
| Gérer les événements, attributs, achats | `manage_events_attributes_purchases` |
| Gérer les étiquettes | `manage_tags` |
| Gérer les paramètres des e-mails | `manage_email_settings` |
| Gérer les groupes d'abonnement | `manage_subscription_groups` |
| Gérer les paramètres d'approbation | `manage_approval_settings` |
| Gérer les autorisations du tableau de bord des catalogues | `manage_catalogs_dashboard_permission` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Chaînes de caractères d'autorisations de l'espace de travail #workspace-strings" }

### Chaînes de caractères d'autorisations d'équipe {#team}

| Nom de l'autorisation | Chaîne de caractères API SCIM |
| --- | --- |
| Admin | `admin` |
| Accéder aux Campaigns, Canvas, cartes, Segments, bibliothèque multimédia | `basic_access` |
| Approuver et refuser des Canvas | `approve_deny_campaigns` |
| Envoyer des Campaigns, Canvas | `send_campaigns_canvases` |
| Publier des cartes | `publish_cards` |
| Modifier les Segments | `edit_segments` |
| Exporter les données utilisateur | `export_user_data` |
| Afficher le profil utilisateur | `view_user_profile` |
| Gérer les utilisateurs du tableau de bord | `manage_dashboard_users` |
| Gérer les ressources de la bibliothèque multimédia | `manage_media_library` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Chaînes de caractères d'autorisations d'équipe #équipe" }

### Chaînes de caractères du service {#department-strings}

| Telles qu'affichées dans l'interface utilisateur | Chaîne de caractères API SCIM |
| --- | --- |
| Agence / tiers | `agency` |
| BI / analyses | `bi` |
| Cadre supérieur | `c_suite` |
| Ingénierie | `engineering` |
| Finance | `finance` |
| Marketing / éditorial | `marketing` |
| Gestion des produits | `pm` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Chaînes de caractères du service" }