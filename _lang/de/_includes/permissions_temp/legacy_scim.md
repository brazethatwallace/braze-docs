{% alert important %}
Braze führt [detaillierte Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions) ein, eine flexiblere Methode zur Verwaltung des Zugriffs von Nutzer:innen. Unter [Migration zu detaillierten Berechtigungen]({{site.baseurl}}/granular_permissions_migration/) erfahren Sie mehr über den Migrationsprozess. Auf dem Tab [Detaillierte SCIM-API]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api/) können Sie die detaillierten SCIM-API-Objekte und den Anhang einsehen.
{% endalert %}

## Berechtigungsobjekt {#permissions-object}

Das Berechtigungsobjekt ist ein Feld, das in einigen Anfragen und Antworten vorkommt, wenn Sie über SCIM-ID-Berechtigungen mit der Nutzer:innen-Ressource interagieren.

{% alert note %}
App-Gruppen wurden in Braze in Workspaces umbenannt, aber die Schlüssel auf dieser Seite beziehen sich noch auf die alte Terminologie (zum Beispiel `appGroup`, `appGroupName`).
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
| `companyPermissions` | Optional | Array | Array von Berechtigungsstrings auf Unternehmensebene aus der Tabelle [Unternehmens-Berechtigungsstrings]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_company), wobei das Vorhandensein des Strings bedeutet, dass die Nutzer:in die entsprechende Berechtigung besitzt. |
| `roles` | Optional | Array | Array von [Rollenobjekten]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_role-object). |
| `appGroup` | Erforderlich | Array | Array von [Workspace-Berechtigungsobjekten]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-permissions-set-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Permissions object" }

### Workspace-Berechtigungsobjekt {#workspace-permission-object}

Ein gültiges App-Gruppen-Berechtigungsobjekt ist ein JSON-Objekt mit den folgenden Schlüssel-Wert-Paaren:

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `appGroupName` | Optional | String | Name des Workspace. Wird verwendet, um anzugeben, für welchen Workspace die in diesem Objekt enthaltenen Berechtigungen gelten. |
| `appGroupId` | Erforderlich, wenn `appGroupName` fehlt | String | ID des Workspace, die als alternative Methode zur Angabe des Workspace dient. |
| `appGroupPermissionSets` | Optional | Array | Array mit einem einzelnen [Workspace-Berechtigungssatz-Objekt]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-permissions-set-object). |
| `appGroupPermissions` | Erforderlich | Array | Array von Berechtigungsstrings auf Workspace-Ebene aus der Tabelle [Workspace-Berechtigungsstrings]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-strings), wobei das Vorhandensein des Strings bedeutet, dass die Nutzer:in die entsprechende Berechtigung für den angegebenen Workspace besitzt. |
| `team` | Optional | Array | Array von [Team-Berechtigungsobjekten]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_team-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Workspace permissions object #workspace-permission-object" }

### Workspace-Berechtigungssatz-Objekt {#workspace-permissions-set-object}

Ein gültiges Workspace-Berechtigungssatz-Objekt ist ein JSON-Objekt mit den folgenden Schlüssel-Wert-Paaren:

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | Optional | String | Name des Workspace-Berechtigungssatzes, der der Nutzer:in für diesen Workspace zugewiesen wird. |
| `appGroupPermissionSetID` | Erforderlich, wenn `appGroupPermissionSetName` fehlt | String | ID des Workspace, die als alternative Methode zur Angabe des der Nutzer:in zugewiesenen Workspace-Berechtigungssatzes dient. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Workspace permissions set object #workspace-permissions-set-object" }

### Team-Berechtigungsobjekt {#team-permissions-object}

Ein gültiges Team-Berechtigungsobjekt ist ein JSON-Objekt mit den folgenden Schlüssel-Wert-Paaren:

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `teamName` | Optional | String | Name des Teams, der verwendet werden kann, um anzugeben, für welches Team die Berechtigungen in diesem Objekt gelten. |
| `teamId` | Erforderlich, wenn `teamName` fehlt | String | ID des Teams, die als alternative Methode zur Angabe des Teams dient. |
| `teamPermissions` | Erforderlich | Array | Array von Berechtigungsstrings auf Team-Ebene aus der Tabelle [Team-Berechtigungsstrings]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_team), wobei das Vorhandensein des Strings bedeutet, dass die Nutzer:in die entsprechende Berechtigung für das angegebene Team besitzt. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Team permissions object" }

## Rollenobjekt {#role-object}

Ein gültiges Rollenobjekt ist ein JSON-Objekt mit den folgenden Schlüssel-Wert-Paaren:

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `roleName` | Optional | String | Name der Rolle, die der Nutzer:in zugewiesen wird. |
| `roleId` | Erforderlich, wenn `roleName` fehlt | String | ID der Rolle, die als alternative Methode zur Angabe der Rolle dient. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Role object" }

## Anhang {#appendix}

### Unternehmens-Berechtigungsstrings {#company}

| Anzeige in der UI | SCIM-API-String |
| --- | --- |
| Administrator | `admin` |
| Kann Unternehmenseinstellungen verwalten | `manage_company_settings` |
| Kann Workspaces hinzufügen/entfernen | `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Company permission strings #company" }

### Workspace-Berechtigungsstrings {#workspace-strings}

| Berechtigungsname | SCIM-API-String |
| --- | --- |
| Admin | `admin` |
| Zugriff auf Campaigns, Canvases, Cards, Segmente, Medienbibliothek | `basic_access` |
| Canvases genehmigen und ablehnen | `approve_deny_campaigns` |
| Campaigns, Canvases senden | `send_campaigns_canvases` |
| Cards veröffentlichen | `publish_cards` |
| Segmente bearbeiten | `edit_segments` |
| Nutzerdaten exportieren | `export_user_data` |
| PII ansehen | `view_pii` |
| Nutzerprofile PII-konform anzeigen | `view_user_profile` |
| Dashboard-Nutzer:innen verwalten | `manage_dashboard_users` |
| Medienbibliothek-Assets verwalten | `manage_media_library` |
| Nutzungsdaten anzeigen | `view_usage_data` |
| Nutzerdaten importieren und aktualisieren | `import_update_user_data` |
| Rechnungsdetails anzeigen | `view_billing_details` |
| Dev-Konsole öffnen | `dev_console` |
| Content Blocks starten | `launch_content_blocks` |
| Externe Integrationen verwalten | `manage_external_integrations` |
| Apps verwalten | `manage_apps` |
| Teams verwalten | `manage_teams` |
| Ereignisse, Attribute und Käufe verwalten | `manage_events_attributes_purchases` |
| Tags verwalten | `manage_tags` |
| E-Mail-Einstellungen verwalten | `manage_email_settings` |
| Abo-Gruppen verwalten | `manage_subscription_groups` |
| Genehmigungseinstellungen verwalten | `manage_approval_settings` |
| Kataloge-Dashboard-Berechtigung verwalten | `manage_catalogs_dashboard_permission` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Workspace permission strings #workspace-strings" }

### Team-Berechtigungsstrings {#team}

| Berechtigungsname | SCIM-API-String |
| --- | --- |
| Admin | `admin` |
| Zugriff auf Campaigns, Canvases, Cards, Segmente, Medienbibliothek | `basic_access` |
| Canvases genehmigen und ablehnen | `approve_deny_campaigns` |
| Campaigns, Canvases senden | `send_campaigns_canvases` |
| Cards veröffentlichen | `publish_cards` |
| Segmente bearbeiten | `edit_segments` |
| Nutzerdaten exportieren | `export_user_data` |
| Nutzerprofil anzeigen | `view_user_profile` |
| Dashboard-Nutzer:innen verwalten | `manage_dashboard_users` |
| Medienbibliothek-Assets verwalten | `manage_media_library` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Team permission strings #team" }

### Abteilungsstrings {#department-strings}

| Anzeige in der UI | SCIM-API-String |
| --- | --- |
| Agentur / Drittanbieter | `agency` |
| BI / Analytics | `bi` |
| C-Suite | `c_suite` |
| Engineering | `engineering` |
| Finanzen | `finance` |
| Marketing / Redaktion | `marketing` |
| Produktmanagement | `pm` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Department strings" }