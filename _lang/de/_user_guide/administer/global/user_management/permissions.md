---
nav_title: Berechtigungen
article_title: "Braze-Berechtigungen"
page_order: 1
page_type: reference
alias: /braze_permissions/
description: "Dieser Referenzartikel beschreibt, wie Nutzer:innen-Berechtigungen in Braze funktionieren. Hier erfahren Sie, wie Sie Nutzer:innen-Berechtigungen bearbeiten und festlegen und bestimmen, wer darauf zugreifen kann."
tool: Dashboard
---

# Braze-Berechtigungen {#braze-permissions}

> Erfahren Sie, wie Sie Berechtigungssätze erstellen, Rollen erstellen, Nutzer:innen-Berechtigungen bearbeiten und Nutzer:innen-Berechtigungen exportieren, damit Ihre Nutzer:innen nur auf die Workspaces und Features zugreifen können, die sie am meisten benötigen.
>
> {% multi_lang_include video.html id="nv699nw706" source="wistia" %}

## Berechtigungssatz erstellen {#create-a-permission-set}

Verwenden Sie Berechtigungssätze, um Berechtigungen zu bündeln, die sich auf bestimmte Themenbereiche oder Aktionen beziehen. Sie können Berechtigungssätze Dashboard-Nutzer:innen zuweisen, die in verschiedenen Workspaces denselben Zugriff benötigen. Um einen Berechtigungssatz zu erstellen, gehen Sie zu **Einstellungen** > **Nutzer:innenverwaltung** > **Berechtigungssätze** und wählen Sie dann **Berechtigungssatz erstellen**. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

{% tabs local %}
{% tab Beispiel-Berechtigungssätze %}
| Name | Berechtigungen |
|-----------|----------------|
| Entwickler:innen | „View API Keys“, „Edit API Keys“, „View Internal Groups“, „Edit Internal Groups“, „View Message Activity Log“, „View Event User Log“, „View API identifiers“, „View API Usage Dashboard“, „View API Limits“, „View API Usage Alerts“, „Edit API Usage Alerts“, „View SDK or Software-Development-Kit Debugger“, „Edit SDK or Software-Development-Kit Debugger“. |
| Marketer | „View Campaigns“, „Edit Campaigns“, „Archive Campaigns“, „View Canvase“, „Edit Canvase“, „Archive Canvase“, „View Frequency Capping Rules“, „Edit Frequency Capping Rules“, „View Message Prioritization“, „Edit Message Prioritization“, „View Content Blocks“, „View Feature Flags“, „Edit Feature Flags“, „Archive Feature Flags“, „View Segments“, „Edit Segments“, „Edit Global Control Group“, „View IAM Templates“, „Edit IAM Templates“, „Archive IAM Templates“, „View Email Templates“, „Edit Email Templates“, „Archive Email Templates“, „View Webhook Templates“, „Edit Webhook Templates“, „Archive Webhook Templates“, „View Email Link Templates“, „Edit Email Link Templates“, „View Media Library Assets“, „View Locations“, „Edit Locations“, „Archive Locations“, „View Promotion Codes“, „Edit Promotion Codes“, „Export Promotion Codes“, „View Preference Centers“, „Edit Preference Centers“, „Edit Dashboard Reports“, „View Banner Templates“, „View Localization Settings“, „Use Operator“, „View Decisioning Studio Agents“. |
| Nutzer:innenverwaltung | „Edit Dashboard Users“, „View Teams“, „Edit Teams“, „Archive Teams“. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Beispiel-Berechtigungssatz" }
{% endtab %}
{% endtabs %}

## Erstellen einer Rolle {#creating-a-role}

Rollen ermöglichen eine bessere Strukturierung, indem sie Ihre individuellen benutzerdefinierten Berechtigungen mit Workspace-Zugriffskontrollen bündeln. Dies ist besonders nützlich, wenn Sie viele Marken oder regionale Workspaces in einem Dashboard haben. Mit Rollen können Sie Dashboard-Nutzer:innen den entsprechenden Workspaces hinzufügen und ihnen direkt die zugehörigen Berechtigungen gewähren. Um eine Rolle zu erstellen, gehen Sie zu **Einstellungen** > **Nutzer:innenverwaltung** > **Rollen** und wählen Sie **Rolle erstellen**. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

{% tabs local %}
{% tab Beispielrollen %}
| Rollenname | Workspace | Berechtigungen
----------- | ----------- | ---------
| Marketer - Modemarken | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | „Campaigns anzeigen“, „Campaigns bearbeiten“, „Campaigns archivieren“, „Canvase anzeigen“, „Canvase bearbeiten“, „Canvase archivieren“, „Content Blocks anzeigen“, „Content Blocks bearbeiten“, „Content Blocks archivieren“, „Content Blocks starten“, „Feature-Flags anzeigen“, „Feature-Flags bearbeiten“, „Feature-Flags archivieren“, „Segments anzeigen“, „Segments bearbeiten“, „Banner-Templates anzeigen“, „Banner-Templates bearbeiten“, „E-Mail-Templates anzeigen“, „E-Mail-Templates bearbeiten“, „Medienbibliothek-Assets anzeigen“, „Medienbibliothek-Assets bearbeiten“, „Medienbibliothek-Assets löschen“, „Standorte anzeigen“, „Standorte bearbeiten“, „Standorte archivieren“, „Aktionscodes anzeigen“, „Aktionscodes bearbeiten“, „Aktionscodes exportieren“, „Präferenzcenter anzeigen“, „Präferenzcenter bearbeiten“. |
| Marketer - Hautpflegemarken | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | „Campaigns anzeigen“, „Campaigns bearbeiten“, „Campaigns archivieren“, „Canvase anzeigen“, „Canvase bearbeiten“, „Canvase archivieren“, „Content Blocks anzeigen“, „Content Blocks bearbeiten“, „Content Blocks archivieren“, „Content Blocks starten“, „Feature-Flags anzeigen“, „Feature-Flags bearbeiten“, „Feature-Flags archivieren“, „Segments anzeigen“, „Segments bearbeiten“, „Banner-Templates anzeigen“, „Banner-Templates bearbeiten“, „E-Mail-Templates anzeigen“, „E-Mail-Templates bearbeiten“, „Medienbibliothek-Assets anzeigen“, „Medienbibliothek-Assets bearbeiten“, „Medienbibliothek-Assets löschen“, „Standorte anzeigen“, „Standorte bearbeiten“, „Standorte archivieren“, „Aktionscodes anzeigen“, „Aktionscodes bearbeiten“, „Aktionscodes exportieren“, „Präferenzcenter anzeigen“, „Präferenzcenter bearbeiten“. |
| Nutzer:innenverwaltung - Alle Marken | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | „Dashboard-Nutzer:innen bearbeiten“, „Teams anzeigen“, „Teams bearbeiten“, „Teams archivieren“ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Beispielrollen" }
{% endtab %}
{% endtabs %}

## Wie unterscheiden sich Berechtigungssätze und Rollen von Teams? {#how-do-permission-sets-and-roles-differ-from-teams}

{% multi_lang_include permissions/differences.md content="Differences" %}

### Überlegungen zum Hinzufügen von Nutzer:innen-Berechtigungen zu Teams {#considerations-for-adding-user-permissions-to-teams}

Beim Versuch, Berechtigungen im Braze-Dashboard zu speichern, können Schwierigkeiten auftreten – insbesondere beim Hinzufügen oder Entfernen von Nutzer:innen aus einem Workspace oder beim Hinzufügen zu einem Team. Der Button **Save/Update or aktualisieren Users** kann ausgegraut sein, wenn die Berechtigungen der Nutzer:innen mit denen identisch sind, die sie bereits auf Workspace-Ebene besitzen. Diese Einschränkung besteht, weil ein Team keinen Vorteil bietet, wenn alle Nutzer:innen dieselben Berechtigungen wie der gesamte Workspace haben.

Um Nutzer:innen erfolgreich zu einem Team hinzuzufügen und dabei dieselben Berechtigungen beizubehalten, weisen Sie keine Berechtigungen auf Workspace-Ebene zu. Weisen Sie Berechtigungen stattdessen ausschließlich auf Team-Ebene zu.

## Nutzer:innen mit eingeschränktem Zugriff {#limited-users}

Nutzer:innen mit eingeschränktem Zugriff verfügen über spezifische Berechtigungen, die es ihnen ermöglichen, bestimmte Aspekte des Braze-Dashboards zu verwalten, wobei sie im Vergleich zu Unternehmensadmins und Workspace-Admins Einschränkungen haben.

| Geltungsbereich | Beschreibung |
| --- | --- |
| Berechtigungen | Nutzer:innen mit eingeschränktem Zugriff können die Berechtigungen anderer eingeschränkter Nutzer:innen bearbeiten, wenn sie über die Berechtigung „Dashboard-Nutzer:innen bearbeiten“ verfügen. Sie können auch neue eingeschränkte Nutzer:innen erstellen und deren Berechtigungssätze ändern. Sie können jedoch keine Unternehmensadmin-Konten erstellen oder verwalten. |
| Rolleneinschränkungen | Wenn eingeschränkte Nutzer:innen über alle Berechtigungen außer „Workspace-Admin“ verfügen, haben sie dennoch Zugriff auf alle anderen Berechtigungen, die normalerweise einem Workspace-Admin gewährt werden. |
| Sichtbarkeit von Berechtigungen | Wenn eingeschränkte Nutzer:innen die Berechtigung „Dashboard-Nutzer:innen bearbeiten“ für einen Workspace (z. B. Dev) haben, aber nicht für einen anderen (z. B. Prod), sehen sie die Berechtigungen des Prod-Workspaces nicht auf der Detailseite ihrer Dashboard-Nutzer:innen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Berechtigungen für Nutzer:innen mit eingeschränktem Zugriff" }

### Vergleich von Nutzer:innen mit eingeschränktem Zugriff {#compare-limited-users}

| Typ | Beschreibung |
| --- | --- |
| Workspace-Admin | Workspace-Admins haben Berechtigungen, die speziell auf die Verwaltung von Workspaces ausgerichtet sind, verfügen aber nicht über die gleiche Autorität wie Unternehmensadmins. Nutzer:innen mit eingeschränktem Zugriff können Berechtigungen erben, die denen von Workspace-Admins ähneln, wenn die entsprechenden Berechtigungen aktiviert sind. |
| Admin (Unternehmensadmin) | Unternehmensadmins haben umfassendere Berechtigungen, einschließlich der Möglichkeit, Dashboard-Nutzer:innen zu löschen. Sie können jedoch nicht ihr eigenes Konto löschen und müssen sich dafür an einen anderen Unternehmensadmin wenden. |
| Schreibgeschützter Zugriff | Um auf Teile des Dashboards zuzugreifen, wie z. B. die Campaigns-Seite, müssen Nutzer:innen über die entsprechenden Anzeigeberechtigungen verfügen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Vergleich von Nutzer:innen mit eingeschränktem Zugriff" }

### Fehler bei eingeschränktem Zugriff {#limited-access-error}

Nutzer:innen können auf Meldungen wie „Sie benötigen die Berechtigung „Landing-Pages anzeigen“, um auf diese Seite zuzugreifen" stoßen. In solchen Fällen sollten die betroffenen Nutzer:innen und der Account-Admin überprüfen, ob die erforderlichen Berechtigungen erteilt wurden. Falls ja, versuchen Sie das Problem zu beheben, indem Sie die Berechtigungen der Nutzer:innen deaktivieren und anschließend wieder aktivieren.

{% alert note %}
Es ist nicht möglich, Nutzerberechtigungen von einem Dashboard-Konto auf ein anderes zusammenzuführen oder zu importieren.
{% endalert %}

## Nuancen der Nutzer:innen-Berechtigungen {#nuances-of-user-permissions}

Beachten Sie die folgenden Verhaltensweisen, wenn Sie Dashboard-Zugriff zuweisen:

- **Workspace-Admin vs. Unternehmens-Admin:** Workspace-Admins verwalten Berechtigungen innerhalb zugewiesener Workspaces. Unternehmens-Admins verfügen über unternehmensweite Befugnisse, einschließlich des Löschens anderer Dashboard-Nutzer:innen.
- **Eingeschränkte Nutzer:innen:** Eingeschränkte Nutzer:innen mit der Berechtigung „Dashboard-Nutzer:innen bearbeiten“ können andere eingeschränkte Nutzer:innen verwalten, jedoch keine Unternehmens-Admin-Konten erstellen oder verwalten.
- **Umfang von „Dashboard-Nutzer:innen verwalten“:** Auf der Nutzer:innen-Detailseite werden Berechtigungen nur für Workspaces angezeigt, auf die die bearbeitende Person Zugriff hat. Eingeschränkte Nutzer:innen, die Nutzer:innen in einem Workspace bearbeiten können, sehen möglicherweise nicht die Berechtigungs-Checkboxen eines anderen Workspace.
- **Button „Berechtigungen zuweisen“:** Wenn Sie eine:n Nutzer:in bearbeiten und diese:r bereits über Berechtigungen auf Workspace-Ebene oder Berechtigungssätze für jeden Workspace verfügt, den Sie verwalten können, verschwindet der Button **Berechtigungen zuweisen**. Dies geschieht, weil es keine weiteren Workspaces gibt, die auf Workspace-Ebene zugewiesen werden können.
- **Nutzerdaten exportieren:** Für den Export von Nutzerdaten ist neben der Export-Berechtigung auch ein Zugriff auf Workspace-Ebene erforderlich.
- **Zusammengesetzte Berechtigungen:** Einige Bereiche erfordern mehrere Berechtigungen. Beispielsweise erfordert die Konfiguration von [Technologie-Partnern]({{site.baseurl}}/partners) in der Regel sowohl den Partner-Zugriff als auch eine grundlegende Leseberechtigung für die zugehörigen Workspace-Features.
- **Nutzerdaten importieren und Update or aktualisieren or aktualisieren:** Diese Berechtigung umfasst die Möglichkeit, App-Nutzerprofile über Importabläufe zu bearbeiten – nicht nur Dashboard-Nutzerdatensätze.

## Berechtigungen von Nutzer:innen bearbeiten {#edit-a-users-permissions}

Um die aktuellen Admin-, Unternehmens- oder Workspace-Berechtigungen von Nutzer:innen zu bearbeiten, gehen Sie zu **Einstellungen** > **Nutzerverwaltung** > **Unternehmensnutzer:innen** und wählen Sie den Namen aus.

![Die Seite „Unternehmensnutzer:innen“ in Braze mit einer Tabelle der Dashboard-Nutzer:innen.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Admin %}

### Admin {#admin}

Admins haben Zugriff auf alle Features und können sämtliche Unternehmenseinstellungen ändern. Sie können:

- [Genehmigungseinstellungen]({{site.baseurl}}/user_guide/messaging/governance/approvals#turning-on-the-approval-workflow) ändern
- Andere [Braze-Nutzer:innen]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users#adding-company-users) hinzufügen, bearbeiten, löschen, sperren oder entsperren
- Braze-Nutzer:innen als CSV-Datei exportieren

Um Admin-Berechtigungen zu gewähren oder zu entziehen, wählen Sie **This user is an admin** und dann **Update or aktualisieren user**.

{% alert warning %}
Wenn Sie einer Person die Admin-Berechtigungen entziehen, kann diese nicht mehr auf Braze zugreifen, bis Sie ihr mindestens eine [Berechtigung auf Unternehmens- oder Workspace-Ebene]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#edit-a-users-permissions) zuweisen.
{% endalert %}

{% endtab %}
{% tab Unternehmen %}

### Unternehmen {#company}

Um die folgenden Berechtigungen auf Unternehmensebene für Nutzer:innen zu verwalten, aktivieren oder deaktivieren Sie das Kontrollkästchen neben der jeweiligen Berechtigung. Wenn Sie fertig sind, wählen Sie **Update or aktualisieren user**.

| Berechtigungsname | Beschreibung |
|----------|-----------|
| Unternehmenseinstellungen verwalten | Ermöglicht es Nutzer:innen, Berechtigungseinstellungen und die Sender-Verifizierung zu ändern. |
| Workspaces erstellen und löschen | Ermöglicht es Nutzer:innen, Workspaces zu erstellen und zu löschen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Berechtigungen auf Unternehmensebene" }

{% endtab %}
{% tab Workspace %}

### Workspace {#workspace}

Sie können Nutzer:innen für jeden Workspace, dem sie in Braze angehören, unterschiedliche Berechtigungen zuweisen. Um ihre Berechtigungen auf Workspace-Ebene zu verwalten, wählen Sie **Select workspaces and permissions** und legen Sie dann die Berechtigungen manuell fest oder weisen Sie einen zuvor erstellten [Berechtigungssatz oder eine Rolle]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#create-a-permission-set) zu. Wenn Sie Nutzer:innen für verschiedene Workspaces unterschiedliche Berechtigungen zuweisen möchten, wiederholen Sie diesen Vorgang so oft wie nötig. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

{% subtabs %}
{% subtab Manuell auswählen %}

Wählen Sie unter **Workspaces** einen oder mehrere Workspaces aus dem Dropdown aus. Wählen Sie dann unter **Permissions** eine oder mehrere Berechtigungen aus. Diese Berechtigungen werden nur für die von Ihnen ausgewählten Workspaces zugewiesen. Optional können Sie **Assign workspace admin access** auswählen, um stattdessen volle Berechtigungen für diesen Workspace zu gewähren.

Wenn Sie fertig sind, wählen Sie **Update or aktualisieren user**.

![Berechtigungen auf Workspace-Ebene werden in Braze manuell ausgewählt.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Berechtigungssatz zuweisen %}

Wählen Sie unter **Workspaces** einen oder mehrere Workspaces aus dem Dropdown aus. Wählen Sie dann unter **Permission Sets** einen Berechtigungssatz aus. Diese Berechtigungen werden nur für die von Ihnen ausgewählten Workspaces zugewiesen.

Wenn Sie fertig sind, wählen Sie **Update or aktualisieren user**.

![Berechtigungen auf Workspace-Ebene werden in Braze über einen Berechtigungssatz zugewiesen.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% subtab Rolle zuweisen %}

Wählen Sie unter **Workspaces** einen oder mehrere Workspaces aus dem Dropdown aus. Wählen Sie dann unter **Role** eine Rolle aus. Diese Berechtigungen werden nur für die von Ihnen ausgewählten Workspaces zugewiesen.

Wenn Sie fertig sind, wählen Sie **Update or aktualisieren user**.

![Berechtigungen auf Workspace-Ebene werden in Braze über eine Rolle zugewiesen.]({% image_buster /assets/img/braze_permissions/workspace_level_role.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Berechtigungen von Nutzer:innen exportieren {#exporting-user-permissions}

Um eine Liste Ihrer Nutzer:innen und deren Berechtigungen herunterzuladen, gehen Sie zu **Einstellungen** > **Nutzerverwaltung** > **Unternehmensnutzer:innen** und wählen Sie dann **Nutzer:innen exportieren** aus. Eine CSV-Datei wird in Kürze an Ihre E-Mail-Adresse gesendet.

## Liste der Berechtigungen {#list-of-permissions}

### Messaging {#messaging}

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| Campaigns | Campaigns anzeigen | Campaigns anzeigen |
| Campaigns | Campaigns starten | Bestehende Campaigns starten, stoppen, pausieren oder fortsetzen |
| Campaigns | Campaigns archivieren | Campaigns ins Archiv verschieben |
| Campaigns | Campaigns bearbeiten | Campaigns erstellen und Update or aktualisieren or aktualisieren |
| Campaigns | Campaigns genehmigen und ablehnen | Campaigns genehmigen oder ablehnen. Der [Genehmigungsworkflow für Campaigns]({{site.baseurl}}/user_guide/messaging/governance/approvals) muss aktiviert sein, damit diese Berechtigung wirksam wird. Diese Einstellung befindet sich derzeit im Early Access. Kontaktieren Sie Ihren Account Manager:in, wenn Sie am Early Access teilnehmen möchten. |
| Canvas | Canvase anzeigen | Canvase anzeigen |
| Canvas | Canvase archivieren | Canvase ins Archiv verschieben |
| Canvas | Canvase bearbeiten | Canvase erstellen und Update or aktualisieren or aktualisieren |
| Canvas | Canvase starten | Bestehende Canvase starten, stoppen, pausieren oder fortsetzen |
| Canvas | Canvase genehmigen und ablehnen | Canvase genehmigen oder ablehnen. Der [Genehmigungsworkflow für Canvase]({{site.baseurl}}/user_guide/messaging/governance/approvals) muss aktiviert sein, damit diese Berechtigung wirksam wird. Diese Einstellung befindet sich derzeit im Early Access. Kontaktieren Sie Ihren Account Manager:in, wenn Sie am Early Access teilnehmen möchten. |
| Feature-Flags | Feature-Flags anzeigen | Feature-Flags anzeigen |
| Feature-Flags | Feature-Flags archivieren | Feature-Flags ins Archiv verschieben |
| Feature-Flags | Feature-Flags bearbeiten | Feature-Flags erstellen und Update or aktualisieren or aktualisieren |
| Frequency-Capping | Frequency-Capping-Regeln anzeigen | Frequency-Capping-Regeln anzeigen |
| Frequency-Capping | Frequency-Capping-Regeln bearbeiten | Frequency-Capping-Regeln erstellen und Update or aktualisieren or aktualisieren |
| Landing-Pages | Landing-Pages anzeigen | Landing-Pages anzeigen |
| Landing-Pages | Landing-Pages veröffentlichen | Einen Landing-Page-Entwurf aktivieren |
| Landing-Pages | Landing-Page-Entwürfe bearbeiten | Landing-Page-Entwürfe erstellen und speichern |
| Nachrichtenarchivierungs-Einstellungen | Nachrichtenarchivierungs-Einstellungen anzeigen | Nachrichtenarchivierungs-Einstellungen ohne Änderungen anzeigen |
| Nachrichtenarchivierungs-Einstellungen | Nachrichtenarchivierungs-Einstellungen bearbeiten | Nachrichtenarchivierungs-Einstellungen erstellen und Update or aktualisieren or aktualisieren |
| Nachrichtenpriorisierung | Nachrichtenpriorisierung anzeigen | Einstellungen zur Nachrichtenpriorisierung ohne Änderungen anzeigen |
| Nachrichtenpriorisierung | Nachrichtenpriorisierung bearbeiten | Einstellungen zur Nachrichtenpriorisierung erstellen und Update or aktualisieren or aktualisieren |
| WhatsApp Flows | WhatsApp Flows anzeigen | Alle WhatsApp Flows anzeigen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Messaging-Berechtigungen" }

### Zielgruppe {#audience}

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| Globale Kontrollgruppe | Globale Kontrollgruppe anzeigen | Einrichtungsseite der globalen Kontrollgruppe anzeigen |
| Globale Kontrollgruppe | Globale Kontrollgruppe bearbeiten | Änderungen an der globalen Kontrollgruppe erstellen und speichern. Nutzer:innen mit der Berechtigung „Globale Kontrollgruppe bearbeiten“ müssen zusätzlich die Berechtigungen „Campaigns bearbeiten“ und „Canvase bearbeiten“ besitzen. Nutzer:innen mit der Berechtigung „Globale Kontrollgruppe bearbeiten“ erhalten automatisch auch die Berechtigung „Globale Kontrollgruppe anzeigen“. |
| Standorte | Standorte archivieren | Standorte ins Archiv verschieben |
| Standorte | Standorte anzeigen | Standorte anzeigen |
| Standorte | Standorte bearbeiten | Standorte erstellen und bearbeiten |
| Segments | Segments anzeigen | Segments anzeigen. Nutzer:innen benötigen die Berechtigung „Segments anzeigen“, um die Berechtigungen „Segments bearbeiten“ oder „Segments archivieren“ zu erhalten. |
| Segments | Segments archivieren | Segments archivieren und dearchivieren. Nutzer:innen mit der Berechtigung „Segments archivieren“ müssen zusätzlich die Berechtigung „Segments anzeigen“ besitzen. |
| Segments | Segments bearbeiten | Segments erstellen und Update or aktualisieren or aktualisieren. Nutzer:innen mit der Berechtigung „Segments bearbeiten“ müssen zusätzlich die Berechtigung „Segments anzeigen“ besitzen. |
| Nutzerdaten | Nutzerimporte anzeigen | CSV-Nutzerimporte ohne Änderungen anzeigen |
| Nutzerdaten | Nutzer:innen importieren | Nutzer:innen ins Dashboard hochladen |
| Nutzerdaten | Nutzerdaten bearbeiten | Nutzerdaten erstellen und Update or aktualisieren or aktualisieren |
| Nutzerdaten | Nutzerdaten exportieren | Nutzer:innen aus dem Dashboard herunterladen |
| Doppelte Nutzer:innen | Zusammenführungseinträge anzeigen | Eine Liste der Zusammenführungseinträge von Nutzer:innen anzeigen |
| Nutzer:innen | Nutzerprofile anzeigen (PII geschwärzt) | Nutzerprofile in PII-konformer Weise anzeigen. Nutzer:innen mit dieser Berechtigung können keine Campaigns speichern oder starten, die als PII gekennzeichnete angepasste Attribute referenzieren, es sei denn, sie verfügen zusätzlich über die Berechtigung „Als PII gekennzeichnete angepasste Attribute anzeigen“.<br><br>Die Berechtigung „Nutzerprofile anzeigen (PII geschwärzt)“ muss vor der Nutzung aktiviert werden. Wenden Sie sich an Ihren CSM or Customer-Success-Manager or Customer-Success-Manager:in, um sie für Ihren Workspace zu aktivieren. |
| Nutzer:innen | Event-Eigenschaften von Nutzer:innen anzeigen | Event-Eigenschaften im Tab **Event-Verlauf** in Nutzerprofilen anzeigen |
| Doppelte Nutzer:innen | Doppelte Nutzer:innen zusammenführen | Doppelte Nutzer:innen zu einem/einer Nutzer:in zusammenführen. Duplikate werden nach dem Zusammenführen entfernt. |
| Nutzer:innen löschen | Löscheinträge von Nutzer:innen anzeigen | Eine Liste der Löscheinträge von Nutzer:innen anzeigen |
| Nutzer:innen löschen | Nutzer:innen löschen | Nutzer:innen einzeln oder in Masse dauerhaft aus dem Dashboard löschen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Zielgruppen-Berechtigungen" }

### Template {#template}

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| Banner-Templates | Banner-Templates anzeigen | Banner-Templates anzeigen |
| Banner-Templates | Banner-Templates archivieren | Banner-Templates ins Archiv verschieben |
| Banner-Templates | Banner-Templates bearbeiten | Banner-Templates erstellen und Update or aktualisieren or aktualisieren |
| Canvas-Templates | Canvas-Templates anzeigen | Canvas-Templates anzeigen |
| Canvas-Templates | Canvas-Templates archivieren | Canvas-Templates ins Archiv verschieben |
| Canvas-Templates | Canvas-Templates erstellen und bearbeiten | Canvas-Templates erstellen und Update or aktualisieren or aktualisieren |
| Content Blocks | Content Blocks anzeigen | Content Blocks anzeigen |
| Content Blocks | Content Blocks veröffentlichen | Entwürfe von Content Blocks veröffentlichen sowie veröffentlichte Content Blocks bearbeiten, archivieren und dearchivieren |
| Content Blocks | Content Blocks archivieren | Content Blocks ins Archiv verschieben |
| Content Blocks | Content Blocks bearbeiten | Content Blocks erstellen und Entwürfe von Content Blocks bearbeiten |
| E-Mail-Link-Templates | E-Mail-Link-Templates anzeigen | Link-Templates ohne Änderungen anzeigen |
| E-Mail-Link-Templates | E-Mail-Link-Templates bearbeiten | Link-Templates erstellen und Update or aktualisieren or aktualisieren |
| E-Mail-Templates | E-Mail-Templates anzeigen | E-Mail-Templates anzeigen |
| E-Mail-Templates | E-Mail-Templates archivieren | E-Mail-Templates ins Archiv verschieben |
| E-Mail-Templates | E-Mail-Templates bearbeiten | E-Mail-Templates erstellen und Update or aktualisieren or aktualisieren |
| IAM-Templates | IAM-Templates anzeigen | In-App-Nachricht-Templates ohne Änderungen anzeigen |
| IAM-Templates | IAM-Templates archivieren | IAM-Templates ins Archiv verschieben |
| IAM-Templates | IAM-Templates bearbeiten | In-App-Nachricht-Templates erstellen und Update or aktualisieren or aktualisieren |
| Landing-Page-Templates | Landing-Page-Templates anzeigen | Landing-Page-Templates anzeigen |
| Landing-Page-Templates | Landing-Page-Templates archivieren | Landing-Page-Templates ins Archiv verschieben |
| Landing-Page-Templates | Landing-Page-Templates bearbeiten | Landing-Page-Templates erstellen und Update or aktualisieren or aktualisieren |
| Webhook-Templates | Webhook-Templates anzeigen | Webhook-Templates ohne Änderungen anzeigen |
| Webhook-Templates | Webhook-Templates archivieren | Webhook-Templates ins Archiv verschieben |
| Webhook-Templates | Webhook-Templates bearbeiten | Webhook-Templates erstellen und Update or aktualisieren or aktualisieren |
| WhatsApp-Nachricht-Templates | WhatsApp-Nachricht-Templates anzeigen | Ermöglicht es Nutzer:innen, [WhatsApp-Nachricht-Templates]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-2-compose-your-whatsapp-message) anzuzeigen |
| WhatsApp-Nachricht-Templates | WhatsApp-Nachricht-Templates bearbeiten | Ermöglicht es Nutzer:innen, WhatsApp-Nachricht-Templates im Template-Builder zu erstellen. Dieses Feature befindet sich derzeit im Early Access. |
| WhatsApp-Nachricht-Templates von Meta | WhatsApp-Nachricht-Templates von Meta anzeigen | Alle WhatsApp-Templates anzeigen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Template-Berechtigungen" }

### Partnerintegrationen {#partner-integrations}

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| Currents-Integrationen | Currents-Integration anzeigen | Currents-Integrationen anzeigen |
| Currents-Integrationen | Currents-Integrationen bearbeiten | Currents-Integrationen erstellen, Update or aktualisieren or aktualisieren und löschen |
| Technologie-Partner | Technologie-Partner bearbeiten | Technologie-Partner erstellen und Update or aktualisieren or aktualisieren |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Partnerintegrations-Berechtigungen" }

### Dateneinstellungen {#data-settings}

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| Kataloge | Kataloge anzeigen | Kataloge und Selektionen anzeigen |
| Kataloge | Kataloge löschen | Kataloge dauerhaft löschen |
| Kataloge | Kataloge exportieren | Kataloge aus dem Dashboard herunterladen |
| Kataloge | Kataloge bearbeiten | Kataloge und Selektionen erstellen und Update or aktualisieren or aktualisieren |
| Cloud-Datenaufnahme | Cloud-Datenaufnahme bearbeiten | Quellen und Synchronisierungen erstellen, Update or aktualisieren or aktualisieren und löschen |
| Angepasste Attribute | Angepasste Attribute anzeigen | Angepasste Attribute und Nutzungsbericht anzeigen |
| Angepasste Attribute | Angepasste Attribute exportieren | Angepasste Attribute aus dem Dashboard herunterladen |
| Angepasste Attribute | Angepasste Attribute löschen | Angepasste Attribute dauerhaft löschen |
| Angepasste Attribute | Angepasste Attribute auf Blockliste setzen | Angepasste Attribute zu einer Blockliste hinzufügen, die die Nutzung im Dashboard einschränkt |
| Angepasste Attribute | Angepasste Attribute bearbeiten | Angepasste Attribute erstellen und Update or aktualisieren or aktualisieren |
| Segmentierung nach angepassten Event-Eigenschaften | Segmentierung nach angepassten Event-Eigenschaften bearbeiten | Segmentierung nach angepassten Event-Eigenschaften aktivieren und deaktivieren |
| Angepasste Events | Angepasste Events anzeigen | Angepasste Events und Nutzungsbericht anzeigen sowie angepasste Events zur täglichen Analytics-Bericht-E-Mail hinzufügen |
| Angepasste Events | Angepasste Events exportieren | Angepasste Events aus dem Dashboard herunterladen |
| PII | PII anzeigen | PII anzeigen |
| Angepasste Events | Angepasste Events löschen | Angepasste Events dauerhaft löschen |
| Angepasste Events | Angepasste Events auf Blockliste setzen | Angepasste Events zu einer Blockliste hinzufügen, die die Nutzung im Dashboard einschränkt |
| Angepasste Events | Angepasste Events bearbeiten | Angepasste Events erstellen und Update or aktualisieren or aktualisieren |
| Produkte | Produkte anzeigen | Produkte anzeigen |
| Produkte | Produkte auf Blockliste setzen | Produkte zu einer Blockliste hinzufügen, die die Nutzung im Dashboard einschränkt |
| Produkte | Produkte bearbeiten | Produkte erstellen und Update or aktualisieren or aktualisieren |
| Segmentierung nach Kauf-Eigenschaften | Segmentierung nach Kauf-Eigenschaften bearbeiten | Segmentierung nach Kauf-Event-Eigenschaften aktivieren und deaktivieren |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Dateneinstellungs-Berechtigungen" }

### Einstellungen {#settings}

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| API-Bezeichner | API-Bezeichner anzeigen | API-Bezeichner und andere Bezeichner anzeigen |
| API-Schlüssel | API-Schlüssel anzeigen | API-Schlüssel anzeigen |
| API-Schlüssel | API-Schlüssel bearbeiten | API-Schlüssel erstellen und Update or aktualisieren or aktualisieren |
| API-Limits | API-Limits anzeigen | API-Rate-Limits anzeigen |
| API-Nutzungsbenachrichtigungen | API-Nutzungsbenachrichtigungen anzeigen | API-Nutzungsbenachrichtigungen anzeigen |
| API-Nutzungsbenachrichtigungen | API-Nutzungsbenachrichtigungen bearbeiten | API-Nutzungsbenachrichtigungen erstellen und Update or aktualisieren or aktualisieren |
| API-Nutzungsdaten | API-Nutzungs-Dashboard anzeigen | Das API-Nutzungs-Dashboard anzeigen |
| App-Einstellungen | App-Einstellungen bearbeiten | Apps in den App-Einstellungen erstellen, bearbeiten und Update or aktualisieren or aktualisieren |
| App-Einstellungen | App-Einstellungen anzeigen | Die Seite „App-Einstellungen“ anzeigen |
| Audience-Sync-Einstellungen | Audience-Sync-Einstellungen anzeigen | Alle Einstellungen der verbundenen Audience-Sync-Partner anzeigen |
| Dashboard-Nutzer:innen | Dashboard-Nutzer:innen bearbeiten | Unternehmensnutzer:innen anzeigen, erstellen und bearbeiten |
| E-Mail-Einstellungen | E-Mail-Einstellungen anzeigen | E-Mail-Präferenzen anzeigen |
| E-Mail-Einstellungen | E-Mail-Einstellungen bearbeiten | E-Mail-Präferenzen aktivieren und Update or aktualisieren or aktualisieren |
| Event-Nutzerprotokoll | Event-Nutzerprotokoll anzeigen | Event-Nutzerprotokolle anzeigen |
| Interne Gruppen | Interne Gruppen anzeigen | Interne Gruppen anzeigen |
| Interne Gruppen | Interne Gruppen löschen | Interne Gruppen löschen |
| Interne Gruppen | Interne Gruppen bearbeiten | Interne Gruppen erstellen und Update or aktualisieren or aktualisieren |
| Nachrichtenaktivitätsprotokoll | Nachrichtenaktivitätsprotokoll anzeigen | Nachrichtenaktivitätsprotokolle anzeigen |
| Mehrsprachigkeitseinstellungen | Lokalisierungseinstellungen anzeigen | Seite für Einstellungen der mehrsprachigen Locales anzeigen |
| Mehrsprachigkeitseinstellungen | Lokalisierungseinstellungen löschen | Mehrsprachige Locales löschen |
| Mehrsprachigkeitseinstellungen | Lokalisierungseinstellungen bearbeiten | Mehrsprachige Locales erstellen |
| Präferenzcenter | Präferenzcenter anzeigen | Präferenzcenter anzeigen |
| Präferenzcenter | Präferenzcenter bearbeiten | Präferenzcenter erstellen und Update or aktualisieren or aktualisieren |
| Präferenzcenter | Präferenzcenter veröffentlichen | Einen Präferenzcenter-Entwurf aktivieren oder ein bestehendes Präferenzcenter Update or aktualisieren or aktualisieren |
| Push-Einstellungen | Push-Einstellungen anzeigen | Push-Einstellungen anzeigen |
| Push-Einstellungen | Push-Einstellungen bearbeiten | Push-Einstellungen erstellen und Update or aktualisieren or aktualisieren |
| SDK or Software-Development-Kit-Debugger | SDK or Software-Development-Kit-Debugger anzeigen | SDK or Software-Development-Kit-Debugger oder Debugging-Sitzungen anzeigen |
| SDK or Software-Development-Kit-Debugger | SDK or Software-Development-Kit-Debugger bearbeiten | SDK or Software-Development-Kit-Debugger-Sitzungen erstellen und herunterladen |
| Tags | Tags anzeigen | Tags anzeigen |
| Tags | Tags löschen | Tags dauerhaft löschen |
| Tags | Tags bearbeiten | Tags erstellen und Update or aktualisieren or aktualisieren |
| Teams | Teams anzeigen | Teams anzeigen |
| Teams | Teams archivieren | Teams ins Archiv verschieben |
| Teams | Teams bearbeiten | Teams erstellen und Update or aktualisieren or aktualisieren |
| WhatsApp-Einstellungen | WhatsApp-Einstellungen anzeigen | Alle Einstellungen des WhatsApp-Kanals anzeigen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Einstellungs-Berechtigungen" }

### Decisioning Studio

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| Decisioning Studio Agents | Decisioning Studio Agent anzeigen | Konfiguration von Decisioning Studio Agents ohne Änderungen anzeigen |
| Decisioning Studio Zielgruppe | Decisioning Studio Zielgruppe anzeigen | Zielgruppendetails in den Konfigurationszusammenfassungen von Decisioning Studio Agents einsehen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Decisioning-Studio-Berechtigungen" }

### Sonstiges {#other}

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| App-Nutzung | Nutzungsdaten anzeigen | Nutzungsdaten anzeigen |
| Abrechnung | Abrechnungsdetails anzeigen | Abrechnungsdetails anzeigen |
| Angepasste Agents | KI or künstliche Intelligenz-Agents der Agent-Konsole anzeigen | Ermöglicht es Nutzer:innen, angepasste KI or künstliche Intelligenz-Agents anzuzeigen |
| Angepasste Agents | KI or künstliche Intelligenz-Agents der Agent-Konsole archivieren | Ermöglicht es Nutzer:innen, angepasste KI or künstliche Intelligenz-Agents zu archivieren |
| Angepasste Agents | KI or künstliche Intelligenz-Agents der Agent-Konsole bearbeiten | Ermöglicht es Nutzer:innen, angepasste KI or künstliche Intelligenz-Agents zu erstellen und zu Update or aktualisieren or aktualisieren |
| Als PII gekennzeichnete angepasste Attribute | Als PII gekennzeichnete angepasste Attribute anzeigen | Als PII gekennzeichnete angepasste Attribute anzeigen |
| Dashboard-Berichte | Dashboard-Berichte anzeigen | Berichte ohne Änderungen anzeigen |
| Dashboard-Berichte | Dashboard-Berichte löschen | Berichte dauerhaft löschen |
| Dashboard-Berichte | Dashboard-Berichte bearbeiten | Berichte erstellen und Update or aktualisieren or aktualisieren |
| Domain-Einstellungen | Domain-Einstellungen bearbeiten | Delegierte Domains und angepasste Domains unter „Verifizierte Domains“ hinzufügen |
| Verschlüsselung auf Feldebene | Verschlüsselung auf Bezeichner-Feldebene bearbeiten | Einstellungen für die Verschlüsselung auf Feldebene aktivieren und Update or aktualisieren or aktualisieren |
| Medienbibliothek-Assets | Medienbibliothek-Assets anzeigen | Medienbibliothek-Assets anzeigen |
| Medienbibliothek-Assets | Medienbibliothek-Assets löschen | Medienbibliothek-Assets aus der UI entfernen. Gelöschte Assets werden weiterhin von Braze gehostet, um bestehende Nachrichten, die darauf verweisen, nicht zu beeinträchtigen. Kontaktieren Sie den Braze-Support, um ein Asset dauerhaft zu löschen. |
| Medienbibliothek-Assets | Medienbibliothek-Assets bearbeiten | Medienbibliothek-Assets erstellen und Update or aktualisieren or aktualisieren |
| Medienbibliothek-Assets | Medienbibliothek-Assets ersetzen | Die Datei eines bestehenden Medienbibliothek-Assets ersetzen, wobei URL und Asset-ID stabil bleiben |
| Messaging-Rate-Limits | Messaging-Rate-Limits anzeigen | Messaging-Rate-Limits auf Workspace-Ebene anzeigen |
| Messaging-Rate-Limits | Messaging-Rate-Limits bearbeiten | Messaging-Rate-Limits auf Workspace-Ebene konfigurieren und bearbeiten |
| Operator | BrazeAI<sup>TM</sup> Operator verwenden | Auf Braze Operator zugreifen und damit Fragen beantworten, bei der Einrichtung navigieren, Probleme beheben und Ideen sammeln |
| Placements | Placements anzeigen | Banner-Placements anzeigen |
| Placements | Placements archivieren | Banner-Placements ins Archiv verschieben |
| Placements | Placements bearbeiten | Banner-Placements erstellen und Update or aktualisieren or aktualisieren |
| Aktionscodes | Aktionscodes anzeigen | Aktionscodes anzeigen |
| Aktionscodes | Aktionscodes exportieren | Eine Liste der Aktionscodes aus dem Dashboard herunterladen |
| Aktionscodes | Aktionscodes bearbeiten | Aktionscodes erstellen und Update or aktualisieren or aktualisieren |
| Abo-Gruppen | Abos bearbeiten | Abo-Gruppen erstellen und Update or aktualisieren or aktualisieren |
| Transformationen | Datentransformation bearbeiten | Datentransformationen erstellen und Update or aktualisieren or aktualisieren |
| Transformationen | Datentransformation anzeigen | Datentransformationen anzeigen |
| Support-Tickets | Support-Ticket erstellen | Support-Tickets erstellen und Update or aktualisieren or aktualisieren |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Sonstige Berechtigungen" }