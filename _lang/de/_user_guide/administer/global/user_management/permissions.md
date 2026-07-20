---
nav_title: Berechtigungen
article_title: Nutzer:innen-Berechtigungen im Unternehmen
page_order: 1
page_type: reference
alias: /braze_permissions/
description: "Dieser Referenzartikel beschreibt, wie Nutzer:innen-Berechtigungen in Braze funktionieren. Hier erfahren Sie, wie Sie Nutzer:innen-Berechtigungen bearbeiten und festlegen und bestimmen, wer auf Ihre Apps im Dashboard zugreifen kann."
tool: Dashboard

---

# Braze-Berechtigungen {#braze-permissions}

> Erfahren Sie, wie Sie Berechtigungssätze erstellen, Rollen erstellen, Nutzer:innen-Berechtigungen bearbeiten und Nutzer:innen-Berechtigungen exportieren, damit Ihre Nutzer:innen nur auf die Workspaces und Features zugreifen können, die sie am meisten benötigen.
>
> {% multi_lang_include video.html id="nv699nw706" source="wistia" %}

## Berechtigungssatz erstellen {#create-a-permission-set}

Verwenden Sie Berechtigungssätze, um Berechtigungen zu bündeln, die sich auf bestimmte Themenbereiche oder Aktionen beziehen. Sie können Berechtigungssätze auf Dashboard-Nutzer:innen anwenden, die in verschiedenen Workspaces denselben Zugriff benötigen. Um einen Berechtigungssatz zu erstellen, gehen Sie zu **Einstellungen** > **Nutzer:innenverwaltung** > **Berechtigungssätze** und wählen Sie dann **Berechtigungssatz erstellen**. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

{% tabs local %}
{% tab Beispiel-Berechtigungssätze %}
| Name | Berechtigungen |
|-----------|----------------|
| Entwickler:innen | „API-Schlüssel anzeigen“, „API-Schlüssel bearbeiten“, „Interne Gruppen anzeigen“, „Interne Gruppen bearbeiten“, „Nachrichten-Aktivitätsprotokoll anzeigen“, „Event-Nutzerprotokoll anzeigen“, „API-Bezeichner anzeigen“, „API-Nutzungs-Dashboard anzeigen“, „API-Limits anzeigen“, „API-Nutzungswarnungen anzeigen“, „API-Nutzungswarnungen bearbeiten“, „SDK-Debugger anzeigen“, „SDK-Debugger bearbeiten“. |
| Marketer | „Campaigns anzeigen“, „Campaigns bearbeiten“, „Campaigns archivieren“, „Canvases anzeigen“, „Canvases bearbeiten“, „Canvases archivieren“, „Frequency-Capping-Regeln anzeigen“, „Frequency-Capping-Regeln bearbeiten“, „Nachrichtenpriorisierung anzeigen“, „Nachrichtenpriorisierung bearbeiten“, „Content Blocks anzeigen“, „Feature-Flags anzeigen“, „Feature-Flags bearbeiten“, „Feature-Flags archivieren“, „Segments anzeigen“, „Segments bearbeiten“, „Globale Kontrollgruppe bearbeiten“, „In-App-Templates anzeigen“, „In-App-Templates bearbeiten“, „In-App-Templates archivieren“, „E-Mail-Templates anzeigen“, „E-Mail-Templates bearbeiten“, „E-Mail-Templates archivieren“, „Webhook-Templates anzeigen“, „Webhook-Templates bearbeiten“, „Webhook-Templates archivieren“, „E-Mail-Link-Templates anzeigen“, „E-Mail-Link-Templates bearbeiten“, „Medienbibliothek-Assets anzeigen“, „Standorte anzeigen“, „Standorte bearbeiten“, „Standorte archivieren“, „Aktionscodes anzeigen“, „Aktionscodes bearbeiten“, „Aktionscodes exportieren“, „Präferenzzentren anzeigen“, „Präferenzzentren bearbeiten“, „Dashboard-Berichte bearbeiten“, „Banner-Templates anzeigen“, „Lokalisierungseinstellungen anzeigen“, „Operator verwenden“, „Decisioning Studio Agents anzeigen“. |
| Nutzer:innenverwaltung | „Dashboard-Nutzer:innen bearbeiten“, „Teams anzeigen“, „Teams bearbeiten“, „Teams archivieren“. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Beispiel-Berechtigungssatz" }
{% endtab %}
{% endtabs %}

## Rolle erstellen {#creating-a-role}

Rollen ermöglichen mehr Struktur, indem sie Ihre individuellen angepassten Berechtigungen mit Workspace-Zugriffskontrollen bündeln. Dies ist besonders nützlich, wenn Sie viele Marken oder regionale Workspaces in einem Dashboard haben. Mit Rollen können Sie Dashboard-Nutzer:innen den richtigen Workspaces hinzufügen und ihnen direkt die zugehörigen Berechtigungen erteilen. Um eine Rolle zu erstellen, gehen Sie zu **Einstellungen** > **Nutzer:innenverwaltung** > **Rollen** und wählen Sie dann **Rolle erstellen**. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

{% tabs local %}
{% tab Beispielrollen %}
| Rollenname | Workspace | Berechtigungen
----------- | ----------- | ---------
| Marketer – Modemarken | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | „Campaigns anzeigen“, „Campaigns bearbeiten“, „Campaigns archivieren“, „Canvases anzeigen“, „Canvases bearbeiten“, „Canvases archivieren“, „Content Blocks anzeigen“, „Content Blocks bearbeiten“, „Content Blocks archivieren“, „Content Blocks starten“, „Feature-Flags anzeigen“, „Feature-Flags bearbeiten“, „Feature-Flags archivieren“, „Segments anzeigen“, „Segments bearbeiten“, „Banner-Templates anzeigen“, „Banner-Templates bearbeiten“, „E-Mail-Templates anzeigen“, „E-Mail-Templates bearbeiten“, „Medienbibliothek-Assets anzeigen“, „Medienbibliothek-Assets bearbeiten“, „Medienbibliothek-Assets löschen“, „Standorte anzeigen“, „Standorte bearbeiten“, „Standorte archivieren“, „Aktionscodes anzeigen“, „Aktionscodes bearbeiten“, „Aktionscodes exportieren“, „Präferenzzentren anzeigen“, „Präferenzzentren bearbeiten“. |
| Marketer – Hautpflegemarken | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | „Campaigns anzeigen“, „Campaigns bearbeiten“, „Campaigns archivieren“, „Canvases anzeigen“, „Canvases bearbeiten“, „Canvases archivieren“, „Content Blocks anzeigen“, „Content Blocks bearbeiten“, „Content Blocks archivieren“, „Content Blocks starten“, „Feature-Flags anzeigen“, „Feature-Flags bearbeiten“, „Feature-Flags archivieren“, „Segments anzeigen“, „Segments bearbeiten“, „Banner-Templates anzeigen“, „Banner-Templates bearbeiten“, „E-Mail-Templates anzeigen“, „E-Mail-Templates bearbeiten“, „Medienbibliothek-Assets anzeigen“, „Medienbibliothek-Assets bearbeiten“, „Medienbibliothek-Assets löschen“, „Standorte anzeigen“, „Standorte bearbeiten“, „Standorte archivieren“, „Aktionscodes anzeigen“, „Aktionscodes bearbeiten“, „Aktionscodes exportieren“, „Präferenzzentren anzeigen“, „Präferenzzentren bearbeiten“. |
| Nutzer:innenverwaltung – Alle Marken | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | „Dashboard-Nutzer:innen bearbeiten“, „Teams anzeigen“, „Teams bearbeiten“, „Teams archivieren“ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Beispielrollen" }
{% endtab %}
{% endtabs %}

## Wie unterscheiden sich Berechtigungssätze und Rollen von Teams? {#how-do-permission-sets-and-roles-differ-from-teams}

{% multi_lang_include permissions/differences.md content="Differences" %}

### Hinweise zum Hinzufügen von Nutzer:innen-Berechtigungen zu Teams {#considerations-for-adding-user-permissions-to-teams}

Beim Speichern von Berechtigungen im Braze-Dashboard können Schwierigkeiten auftreten, insbesondere beim Hinzufügen oder Entfernen von Nutzer:innen aus einem Workspace oder beim Hinzufügen zu einem Team. Der Button **Nutzer:innen speichern/aktualisieren** kann ausgegraut sein, wenn die Berechtigungen der Nutzer:innen mit denen identisch sind, die sie bereits auf Workspace-Ebene haben. Diese Einschränkung besteht, weil es keinen Vorteil bringt, ein Team zu haben, wenn alle Nutzer:innen dieselben Berechtigungen wie der gesamte Workspace besitzen.

Um Nutzer:innen erfolgreich einem Team hinzuzufügen und dabei dieselben Berechtigungen beizubehalten, weisen Sie keine Berechtigungen auf Workspace-Ebene zu. Weisen Sie Berechtigungen stattdessen ausschließlich auf Team-Ebene zu.

## Eingeschränkte Nutzer:innen {#limited-users}

Eingeschränkte Nutzer:innen haben bestimmte Berechtigungen, die es ihnen ermöglichen, bestimmte Aspekte des Braze-Dashboards zu verwalten, während sie im Vergleich zu Unternehmensadmins und Workspace-Admins Einschränkungen haben.

| Geltungsbereich | Beschreibung |
| --- | --- |
| Berechtigungen | Eingeschränkte Nutzer:innen können die Berechtigungen anderer eingeschränkter Nutzer:innen bearbeiten, wenn sie die Berechtigung „Dashboard-Nutzer:innen bearbeiten“ haben. Sie können auch neue eingeschränkte Nutzer:innen erstellen und deren Berechtigungssätze ändern. Sie können jedoch keine Unternehmensadminkonten erstellen oder verwalten. |
| Rolleneinschränkungen | Wenn eingeschränkte Nutzer:innen alle Berechtigungen außer „Workspace-Admin“ haben, haben sie dennoch Zugriff auf alle anderen Berechtigungen, die normalerweise einem Workspace-Admin gewährt werden. |
| Sichtbarkeit von Berechtigungen | Wenn eingeschränkte Nutzer:innen die Berechtigung „Dashboard-Nutzer:innen bearbeiten“ für einen Workspace (z. B. Dev) haben, aber nicht für einen anderen (z. B. Prod), sehen sie die Prod-Workspace-Berechtigungen nicht auf der Detailseite der Dashboard-Nutzer:innen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Berechtigungen für eingeschränkte Nutzer:innen" }

### Eingeschränkte Nutzer:innen vergleichen {#compare-limited-users}

| Typ eingeschränkter Nutzer:innen | Beschreibung |
| --- | --- |
| Workspace-Admin | Workspace-Admins haben Berechtigungen, die speziell für die Verwaltung von Workspaces gelten, haben aber nicht dieselbe Autorität wie Unternehmensadmins. Eingeschränkte Nutzer:innen können Berechtigungen erben, die denen von Workspace-Admins ähneln, wenn die erforderlichen Berechtigungen aktiviert sind. |
| Admin (Unternehmensadmin) | Unternehmensadmins haben umfassendere Berechtigungen, einschließlich der Möglichkeit, Dashboard-Nutzer:innen zu löschen. Sie können jedoch nicht ihre eigenen Konten löschen und müssen dafür einen anderen Unternehmensadmin kontaktieren. |
| Schreibgeschützter Zugriff | Um auf Teile des Dashboards zuzugreifen, wie z. B. die Campaigns-Seite, müssen Nutzer:innen die entsprechenden Anzeigeberechtigungen zugewiesen bekommen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Vergleich eingeschränkter Nutzer:innen" }

### Fehler bei eingeschränktem Zugriff {#limited-access-error}

Nutzer:innen können Meldungen wie „Sie benötigen die Berechtigung „Landing-Pages anzeigen“, um auf diese Seite zuzugreifen" erhalten. In solchen Fällen sollten die Nutzer:innen und der Kontoadmin überprüfen, ob die erforderlichen Berechtigungen erteilt wurden. Falls ja, versuchen Sie das Problem zu lösen, indem Sie die Berechtigungen der Nutzer:innen deaktivieren und dann wieder aktivieren.

{% alert note %}
Es ist nicht möglich, Nutzer:innen-Berechtigungen von einem Dashboard-Nutzer zu einem anderen zusammenzuführen oder zu importieren.
{% endalert %}

## Nuancen von Nutzer:innen-Berechtigungen {#nuances-of-user-permissions}

Beachten Sie die folgenden Verhaltensweisen, wenn Sie Dashboard-Zugriff zuweisen:

- **Workspace-Admin versus Unternehmensadmin:** Workspace-Admins verwalten Berechtigungen innerhalb zugewiesener Workspaces. Unternehmensadmins haben unternehmensweite Autorität, einschließlich der Möglichkeit, andere Dashboard-Nutzer:innen zu löschen.
- **Eingeschränkte Nutzer:innen:** Eingeschränkte Nutzer:innen mit der Berechtigung „Dashboard-Nutzer:innen bearbeiten“ können andere eingeschränkte Nutzer:innen verwalten, aber keine Unternehmensadminkonten erstellen oder verwalten.
- **Geltungsbereich „Dashboard-Nutzer:innen verwalten“:** Auf der Nutzer:innen-Detailseite werden Berechtigungen nur für Workspaces angezeigt, auf die die bearbeitende Person Zugriff hat. Eingeschränkte Nutzer:innen, die Nutzer:innen in einem Workspace bearbeiten können, sehen möglicherweise die Berechtigungs-Kontrollkästchen eines anderen Workspaces nicht.
- **Button „Berechtigungen zuweisen“:** Wenn Sie Nutzer:innen bearbeiten und diese bereits Berechtigungen auf Workspace-Ebene oder Berechtigungssätze für jeden Workspace haben, den Sie verwalten können, verschwindet der Button **Berechtigungen zuweisen**. Dies geschieht, weil keine weiteren Workspaces mehr auf Workspace-Ebene zugewiesen werden können.
- **Nutzerdaten exportieren:** Für den Export von Nutzerdaten ist zusätzlich zur Exportberechtigung ein Zugriff auf Workspace-Ebene erforderlich.
- **Zusammengesetzte Berechtigungen:** Einige Bereiche erfordern mehrere Berechtigungen. Beispielsweise erfordert die Konfiguration von [Technologie-Partnern]({{site.baseurl}}/partners) in der Regel sowohl den Partnerzugriff als auch eine grundlegende Leseberechtigung für die zugehörigen Workspace-Features.
- **Nutzerdaten importieren und aktualisieren:** Diese Berechtigung umfasst die Möglichkeit, App-Nutzer:innen-Profile über Importabläufe zu bearbeiten, nicht nur Dashboard-Nutzer:innen-Datensätze.

## Berechtigungen von Nutzer:innen bearbeiten {#edit-a-users-permissions}

Um die aktuellen Admin-, Unternehmens- oder Workspace-Berechtigungen von Nutzer:innen zu bearbeiten, gehen Sie zu **Einstellungen** > **Nutzer:innenverwaltung** > **Unternehmensnutzer:innen** und wählen Sie deren Namen aus.

![Die Seite „Unternehmensnutzer:innen“ in Braze mit einer Tabelle der Dashboard-Nutzer:innen.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Admin %}

### Admin {#admin}

Admins haben Zugriff auf alle Features und die Möglichkeit, alle Unternehmenseinstellungen zu ändern. Sie können:

- [Genehmigungseinstellungen]({{site.baseurl}}/user_guide/messaging/governance/approvals#turning-on-the-approval-workflow) ändern
- Andere [Braze-Nutzer:innen]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users#adding-company-users) hinzufügen, bearbeiten, löschen, sperren oder entsperren
- Braze-Nutzer:innen als CSV exportieren

Um Admin-Berechtigungen zu erteilen oder zu entfernen, wählen Sie **This user is an admin** und dann **Update user**.

{% alert warning %}
Wenn Sie Admin-Berechtigungen von Nutzer:innen entfernen, können diese nicht mehr auf Braze zugreifen, bis Sie ihnen mindestens eine [Berechtigung auf Unternehmens- oder Workspace-Ebene]({{site.baseurl}}/user_guide/administer/global/user_management/permissions?tab=company&sdktab=granular%20permissions#granularpermissions_editing-a-users-permissions) zuweisen.
{% endalert %}

{% endtab %}
{% tab Unternehmen %}

### Unternehmen {#company}

Um die folgenden Berechtigungen auf Unternehmensebene für Nutzer:innen zu verwalten, aktivieren oder deaktivieren Sie das Kontrollkästchen neben der jeweiligen Berechtigung. Wenn Sie fertig sind, wählen Sie **Update user**.

| Berechtigungsname | Beschreibung |
|----------|-----------|
| Unternehmenseinstellungen verwalten | Ermöglicht Nutzer:innen, Berechtigungseinstellungen und die Senderüberprüfung zu ändern. |
| Workspaces erstellen und löschen | Ermöglicht Nutzer:innen, Workspaces zu erstellen und zu löschen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Berechtigungen auf Unternehmensebene" }

{% endtab %}
{% tab Workspace %}

### Workspace {#workspace}

Sie können Nutzer:innen für jeden Workspace, dem sie in Braze angehören, unterschiedliche Berechtigungen erteilen. Um deren Berechtigungen auf Workspace-Ebene zu verwalten, wählen Sie **Select workspaces and permissions** und wählen Sie dann deren Berechtigungen manuell aus oder weisen Sie einen zuvor erstellten [Berechtigungssatz oder eine Rolle]({{site.baseurl}}/user_guide/administer/global/user_management/permissions?sdktab=granular%20permissions#granularpermissions_creating-a-permission-set) zu. Wenn Sie Nutzer:innen für verschiedene Workspaces unterschiedliche Berechtigungen erteilen müssen, wiederholen Sie diesen Vorgang so oft wie nötig. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions?sdktab=granular%20permissions#granularpermissions_list-of-permissions).

{% subtabs %}
{% subtab Manuell auswählen %}

Wählen Sie unter **Workspaces** einen oder mehrere Workspaces aus dem Dropdown-Menü aus. Wählen Sie dann unter **Permissions** eine oder mehrere Berechtigungen aus. Diese Berechtigungen werden nur für die von Ihnen ausgewählten Workspaces zugewiesen. Optional können Sie **Assign workspace admin access** auswählen, wenn Sie stattdessen vollständige Berechtigungen für diesen Workspace erteilen möchten.

Wenn Sie fertig sind, wählen Sie **Update user**.

![Berechtigungen auf Workspace-Ebene werden in Braze manuell ausgewählt.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Berechtigungssatz zuweisen %}

Wählen Sie unter **Workspaces** einen oder mehrere Workspaces aus dem Dropdown-Menü aus. Wählen Sie dann unter **Permission Sets** einen Berechtigungssatz aus. Diese Berechtigungen werden nur für die von Ihnen ausgewählten Workspaces zugewiesen.

Wenn Sie fertig sind, wählen Sie **Update user**.

![Berechtigungen auf Workspace-Ebene werden über einen Berechtigungssatz in Braze zugewiesen.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% subtab Rolle zuweisen %}

Wählen Sie unter **Workspaces** einen oder mehrere Workspaces aus dem Dropdown-Menü aus. Wählen Sie dann unter **Role** eine Rolle aus. Diese Berechtigungen werden nur für die von Ihnen ausgewählten Workspaces zugewiesen.

Wenn Sie fertig sind, wählen Sie **Update user**.

![Berechtigungen auf Workspace-Ebene werden über eine Rolle in Braze zugewiesen.]({% image_buster /assets/img/braze_permissions/workspace_level_role.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Nutzer:innen-Berechtigungen exportieren {#exporting-user-permissions}

Um eine Liste Ihrer Nutzer:innen und deren Berechtigungen herunterzuladen, gehen Sie zu **Einstellungen** > **Nutzer:innenverwaltung** > **Unternehmensnutzer:innen** und wählen Sie dann **Export Users**. Eine CSV-Datei wird in Kürze an Ihre E-Mail-Adresse gesendet.

## Liste der Berechtigungen {#list-of-permissions}

### Messaging {#messaging}

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| Campaigns | View Campaigns | Campaigns anzeigen |
| Campaigns | Launch Campaigns | Bestehende Campaigns starten, stoppen, pausieren oder fortsetzen |
| Campaigns | Archive Campaigns | Campaigns archivieren |
| Campaigns | Edit Campaigns | Campaigns erstellen und aktualisieren |
| Campaigns | Approve and Deny Campaigns | Campaigns genehmigen oder ablehnen. Der [Genehmigungs-Workflow für Campaigns]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals) muss aktiviert sein, damit diese Berechtigung gilt. Diese Einstellung befindet sich derzeit im Early Access. Kontaktieren Sie Ihren Account Manager, wenn Sie am Early Access teilnehmen möchten. |
| Canvas | View Canvases | Canvases anzeigen |
| Canvas | Archive Canvases | Canvases archivieren |
| Canvas | Edit Canvases | Canvases erstellen und aktualisieren |
| Canvas | Launch Canvases | Bestehende Canvases starten, stoppen, pausieren oder fortsetzen |
| Canvas | Approve and Deny Canvases | Canvases genehmigen oder ablehnen. Der [Genehmigungs-Workflow für Canvases]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals) muss aktiviert sein, damit diese Berechtigung gilt. Diese Einstellung befindet sich derzeit im Early Access. Kontaktieren Sie Ihren Account Manager, wenn Sie am Early Access teilnehmen möchten. |
| Feature-Flags | View Feature Flags | Feature-Flags anzeigen |
| Feature-Flags | Archive Feature Flags | Feature-Flags archivieren |
| Feature-Flags | Edit Feature Flags | Feature-Flags erstellen und aktualisieren |
| Frequency-Caps | View Frequency Capping Rules | Frequency-Capping-Regeln anzeigen |
| Frequency-Caps | Edit Frequency Capping Rules | Frequency-Capping-Regeln erstellen und aktualisieren |
| Landing-Pages | View Landing Pages | Landing-Pages anzeigen |
| Landing-Pages | Publish Landing Pages | Einen Landing-Page-Entwurf aktivieren |
| Landing-Pages | Edit Landing Page Drafts | Landing-Page-Entwürfe erstellen und speichern |
| Nachrichtenarchivierungseinstellungen | View Message Archiving Settings | Nachrichtenarchivierungseinstellungen anzeigen, ohne Änderungen vorzunehmen |
| Nachrichtenarchivierungseinstellungen | Edit Message Archiving Settings | Nachrichtenarchivierungseinstellungen erstellen und aktualisieren |
| Nachrichtenpriorisierung | View Message Prioritization | Nachrichtenpriorisierungseinstellungen anzeigen, ohne Änderungen vorzunehmen |
| Nachrichtenpriorisierung | Edit Message Prioritization | Nachrichtenpriorisierungseinstellungen erstellen und aktualisieren |
| WhatsApp Flows | View WhatsApp Flows | Alle WhatsApp Flows anzeigen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Messaging-Berechtigungen" }

### Zielgruppe {#audience}

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| Globale Kontrollgruppe | View Global Control Group | Einrichtungsseite der globalen Kontrollgruppe anzeigen |
| Globale Kontrollgruppe | Edit Global Control Group | Änderungen an der globalen Kontrollgruppe erstellen und speichern. Nutzer:innen mit der Berechtigung „Globale Kontrollgruppe bearbeiten“ müssen auch die Berechtigungen „Campaigns bearbeiten“ und „Canvases bearbeiten“ erhalten. Nutzer:innen mit der Berechtigung „Globale Kontrollgruppe bearbeiten“ erhalten auch die Berechtigung „Globale Kontrollgruppe anzeigen“. |
| Standorte | Archive Locations | Standorte archivieren |
| Standorte | View Locations | Standorte anzeigen |
| Standorte | Edit Locations | Standorte erstellen und bearbeiten |
| Segments | View Segments | Segments anzeigen. Nutzer:innen müssen die Berechtigung „Segments anzeigen“ haben, um die Berechtigung „Segments bearbeiten“ oder „Segments archivieren“ zu erhalten |
| Segments | Archive Segments | Segments archivieren und dearchivieren. Nutzer:innen mit der Berechtigung „Segments archivieren“ müssen auch die Berechtigung „Segments anzeigen“ erhalten |
| Segments | Edit Segments | Segments erstellen und aktualisieren. Nutzer:innen mit der Berechtigung „Segments bearbeiten“ müssen auch die Berechtigung „Segments anzeigen“ erhalten |
| Nutzerdaten | View Import Users | CSV-Nutzerimporte anzeigen, ohne Änderungen vorzunehmen |
| Nutzerdaten | Import Users | Nutzer:innen in das Dashboard hochladen |
| Nutzerdaten | Edit User Data | Nutzerdaten erstellen und aktualisieren |
| Nutzerdaten | Export User Data | Nutzer:innen aus dem Dashboard herunterladen |
| Doppelte Nutzer:innen | View User Merge Records | Eine Liste der Nutzer:innen-Zusammenführungsprotokolle anzeigen |
| Nutzer:innen | View User Profiles (PII Redacted) | Nutzer:innen-Profile in einer PII-konformen Weise anzeigen. Nutzer:innen mit dieser Berechtigung können keine Campaigns speichern oder starten, die auf als PII markierte angepasste Attribute verweisen, es sei denn, sie haben auch die Berechtigung „Als PII markierte angepasste Attribute anzeigen“.<br><br>Die Berechtigung „Nutzer:innen-Profile anzeigen (PII geschwärzt)“ muss vor der Verwendung aktiviert werden. Kontaktieren Sie Ihren Customer-Success-Manager, um sie für Ihren Workspace zu aktivieren. |
| Nutzer:innen | View User Event Properties | Event-Eigenschaften im Tab **Event-Verlauf** in Nutzer:innen-Profilen anzeigen |
| Doppelte Nutzer:innen | Merge Duplicate Users | Doppelte Nutzer:innen zu einem zusammenführen. Duplikate werden nach der Zusammenführung entfernt |
| Nutzer:innen löschen | View User Deletion Records | Eine Liste der Nutzer:innen-Löschprotokolle anzeigen |
| Nutzer:innen löschen | Delete Users | Nutzer:innen dauerhaft einzeln oder in großen Mengen aus dem Dashboard löschen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Zielgruppen-Berechtigungen" }

### Template {#template}

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| Banner-Templates | View Banner Templates | Banner-Templates anzeigen |
| Banner-Templates | Archive Banner Templates | Banner-Templates archivieren |
| Banner-Templates | Edit Banner Templates | Banner-Templates erstellen und aktualisieren |
| Canvas-Templates | View Canvas Templates | Canvas-Templates anzeigen |
| Canvas-Templates | Archive Canvas Templates | Canvas-Templates archivieren |
| Canvas-Templates | Create and Edit Canvas Templates | Canvas-Templates erstellen und aktualisieren |
| Content Blocks | View Content Blocks | Content Blocks anzeigen |
| Content Blocks | Launch Content Blocks | Entwürfe von Content Blocks veröffentlichen sowie gestartete Content Blocks bearbeiten, archivieren und dearchivieren |
| Content Blocks | Archive Content Blocks | Content Blocks archivieren |
| Content Blocks | Edit Content Blocks | Content Blocks erstellen und Entwürfe von Content Blocks bearbeiten |
| E-Mail-Link-Templates | View Email Link Templates | Link-Templates anzeigen, ohne Änderungen vorzunehmen |
| E-Mail-Link-Templates | Edit Email Link Templates | Link-Templates erstellen und aktualisieren |
| E-Mail-Templates | View Email Templates | E-Mail-Templates anzeigen |
| E-Mail-Templates | Archive Email Templates | E-Mail-Templates archivieren |
| E-Mail-Templates | Edit Email Templates | E-Mail-Templates erstellen und aktualisieren |
| In-App-Templates | View IAM Templates | In-App-Nachricht-Templates anzeigen, ohne Änderungen vorzunehmen |
| In-App-Templates | Archive IAM Templates | In-App-Templates archivieren |
| In-App-Templates | Edit IAM Templates | In-App-Nachricht-Templates erstellen und aktualisieren |
| Landing-Page-Templates | View Landing Page Templates | Landing-Page-Templates anzeigen |
| Landing-Page-Templates | Archive Landing Page Template | Landing-Page-Templates archivieren |
| Landing-Page-Templates | Edit Landing Page Templates | Landing-Page-Templates erstellen und aktualisieren |
| Webhook-Templates | View Webhook Templates | Webhook-Templates anzeigen, ohne Änderungen vorzunehmen |
| Webhook-Templates | Archive Webhook Templates | Webhook-Templates archivieren |
| Webhook-Templates | Edit Webhook Templates | Webhook-Templates erstellen und aktualisieren |
| WhatsApp-Nachricht-Templates | View WhatsApp Message Templates | Ermöglicht Nutzer:innen, [WhatsApp-Nachricht-Templates]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-2-compose-your-whatsapp-message) anzuzeigen |
| WhatsApp-Nachricht-Templates | Edit WhatsApp Message Templates | Ermöglicht Nutzer:innen, WhatsApp-Nachricht-Templates im Template-Builder zu erstellen. Dieses Feature befindet sich derzeit im Early Access. |
| WhatsApp-Nachricht-Templates von Meta | View WhatsApp Message Templates From Meta | Alle WhatsApp-Templates anzeigen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Template-Berechtigungen" }

### Partnerintegrationen {#partner-integrations}

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| Currents-Integrationen | View Currents Integration | Currents-Integrationen anzeigen |
| Currents-Integrationen | Edit Currents Integrations | Currents-Integrationen erstellen, aktualisieren und löschen |
| Technologie-Partner | Edit Technology Partners | Technologie-Partner erstellen und aktualisieren |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Partnerintegrationen-Berechtigungen" }

### Dateneinstellungen {#data-settings}

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| Kataloge | View Catalogs | Kataloge und Auswahlen anzeigen |
| Kataloge | Delete Catalogs | Kataloge dauerhaft löschen |
| Kataloge | Export Catalogs | Kataloge aus dem Dashboard herunterladen |
| Kataloge | Edit Catalogs | Kataloge und Auswahlen erstellen und aktualisieren |
| Cloud-Datenaufnahme | Edit Cloud Data Ingestion | Quellen und Synchronisierungen erstellen, aktualisieren und löschen |
| Angepasste Attribute | View Custom Attributes | Angepasste Attribute und Nutzungsbericht anzeigen |
| Angepasste Attribute | Export Custom Attributes | Angepasste Attribute aus dem Dashboard herunterladen |
| Angepasste Attribute | Delete Custom Attributes | Angepasste Attribute dauerhaft löschen |
| Angepasste Attribute | Blocklist Custom Attributes | Angepasste Attribute zu einer Sperrliste hinzufügen, die die Nutzung im Dashboard einschränkt |
| Angepasste Attribute | Edit Custom Attributes | Angepasste Attribute erstellen und aktualisieren |
| Segmentierung angepasster Event-Eigenschaften | Edit Custom Event Property Segmentation | Segmentierung für angepasste Event-Eigenschaften aktivieren und deaktivieren |
| Angepasste Events | View Custom Events | Angepasste Events und Nutzungsbericht anzeigen sowie angepasste Events zum täglichen Analytics-Bericht per E-Mail hinzufügen |
| Angepasste Events | Export Custom Events | Angepasste Events aus dem Dashboard herunterladen |
| PII | View PII | PII anzeigen |
| Angepasste Events | Delete Custom Events | Angepasste Events dauerhaft löschen |
| Angepasste Events | Blocklist Custom Events | Angepasste Events zu einer Sperrliste hinzufügen, die die Nutzung im Dashboard einschränkt |
| Angepasste Events | Edit Custom Events | Angepasste Events erstellen und aktualisieren |
| Produkte | View Products | Produkte anzeigen |
| Produkte | Blocklist Products | Produkte zu einer Sperrliste hinzufügen, die die Nutzung im Dashboard einschränkt |
| Produkte | Edit Products | Produkte erstellen und aktualisieren |
| Segmentierung von Kauf-Eigenschaften | Edit Purchase Property Segmentation | Segmentierung für Kauf-Event-Eigenschaften aktivieren und deaktivieren |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Dateneinstellungen-Berechtigungen" }

### Einstellungen {#settings}

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| API-Bezeichner | View API identifiers | API-Bezeichner und andere Bezeichner anzeigen |
| API-Schlüssel | View API Keys | API-Schlüssel anzeigen |
| API-Schlüssel | Edit API Keys | API-Schlüssel erstellen und aktualisieren |
| API-Limits | View API Limits | API-Rate-Limits anzeigen |
| API-Nutzungswarnungen | View API Usage Alerts | API-Nutzungswarnungen anzeigen |
| API-Nutzungswarnungen | Edit API Usage Alerts | API-Nutzungswarnungen erstellen und aktualisieren |
| API-Nutzungsdaten | View API Usage Dashboard | Das API-Nutzungs-Dashboard anzeigen |
| App-Einstellungen | Edit App Settings | Apps innerhalb der App-Einstellungen erstellen, bearbeiten und aktualisieren |
| App-Einstellungen | View App Settings | Die Seite „App-Einstellungen“ anzeigen |
| Audience-Sync-Einstellungen | View Audience Sync Settings | Alle Einstellungen der verbundenen Audience-Sync-Partner anzeigen |
| Dashboard-Nutzer:innen | Edit Dashboard Users | Unternehmensnutzer:innen anzeigen, erstellen und bearbeiten |
| E-Mail-Einstellungen | View Email Settings | E-Mail-Präferenzen anzeigen |
| E-Mail-Einstellungen | Edit Email Settings | E-Mail-Präferenzen aktivieren und aktualisieren |
| Event-Nutzerprotokoll | View Event User Log | Event-Nutzerprotokolle anzeigen |
| Interne Gruppen | View Internal User Groups | Interne Gruppen anzeigen |
| Interne Gruppen | Delete Internal User Groups | Interne Gruppen löschen |
| Interne Gruppen | Edit Internal User Groups | Interne Gruppen erstellen und aktualisieren |
| Nachrichten-Aktivitätsprotokoll | View Message Activity Log | Nachrichten-Aktivitätsprotokolle anzeigen |
| Mehrsprachigkeitseinstellungen | View Localization Settings | Die Seite für Mehrsprachigkeits-Lokalisierungseinstellungen anzeigen |
| Mehrsprachigkeitseinstellungen | Delete Localization Settings | Mehrsprachigkeits-Lokalisierung löschen |
| Mehrsprachigkeitseinstellungen | Edit Localization Settings | Mehrsprachigkeits-Lokalisierungen erstellen |
| Präferenzzentren | View Preference Centers | Präferenzzentren anzeigen |
| Präferenzzentren | Edit Preference Centers | Präferenzzentren erstellen und aktualisieren |
| Präferenzzentren | Launch Preference Centers | Einen Präferenzzentrum-Entwurf aktivieren oder ein bestehendes aktualisieren |
| Push-Einstellungen | View Push Settings | Push-Einstellungen anzeigen |
| Push-Einstellungen | Edit Push Settings | Push-Einstellungen erstellen und aktualisieren |
| SDK-Debugger | View SDK Debugger | SDK-Debugger oder Debugging-Sitzungen anzeigen |
| SDK-Debugger | Edit SDK Debugger | SDK-Debugger-Sitzungen erstellen und herunterladen |
| Tags | View Tags | Tags anzeigen |
| Tags | Delete Tags | Tags dauerhaft löschen |
| Tags | Edit Tags | Tags erstellen und aktualisieren |
| Teams | View Teams | Teams anzeigen |
| Teams | Archive Teams | Teams archivieren |
| Teams | Edit Teams | Teams erstellen und aktualisieren |
| WhatsApp-Einstellungen | View WhatsApp Settings | Alle WhatsApp-Kanaleinstellungen anzeigen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Einstellungen-Berechtigungen" }

### Decisioning Studio

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| Decisioning Studio Agents | View Decisioning Studio Agent | Decisioning Studio Agents-Konfiguration anzeigen, ohne Änderungen vorzunehmen |
| Decisioning Studio Audience | View Decisioning Studio Audience | Zielgruppendetails in den Konfigurationsübersichten der Decisioning Studio Agents anzeigen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Decisioning-Studio-Berechtigungen" }

### Sonstiges {#other}

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| App-Nutzung | View Usage Data | Nutzungsdaten anzeigen |
| Abrechnung | View Billing Details | Abrechnungsdetails anzeigen |
| Angepasste Agents | View Agent Console AI Agents | Ermöglicht Nutzer:innen, angepasste KI-Agents anzuzeigen |
| Angepasste Agents | Archive Agent Console AI Agents | Ermöglicht Nutzer:innen, angepasste KI-Agents zu archivieren |
| Angepasste Agents | Edit Agent Console AI Agents | Ermöglicht Nutzer:innen, angepasste KI-Agents zu erstellen und zu aktualisieren |
| Als PII markierte angepasste Attribute | View Custom Attributes Marked as PII | Als PII markierte angepasste Attribute anzeigen |
| Dashboard-Berichte | View Dashboard Reports | Berichte anzeigen, ohne Änderungen vorzunehmen |
| Dashboard-Berichte | Delete Dashboard Reports | Berichte dauerhaft löschen |
| Dashboard-Berichte | Edit Dashboard Reports | Berichte erstellen und aktualisieren |
| Domain-Einstellungen | Edit Domain Settings | Delegierte Domains und angepasste Domains unter „Verifizierte Domains“ hinzufügen |
| Verschlüsselung auf Feldebene | Edit Identifier Field-Level Encryption | Einstellungen für die Verschlüsselung auf Feldebene aktivieren und aktualisieren |
| Medienbibliothek-Assets | View Media Library Assets | Medienbibliothek-Assets anzeigen |
| Medienbibliothek-Assets | Delete Media Library Assets | Medienbibliothek-Assets aus der Benutzeroberfläche entfernen. Gelöschte Assets werden weiterhin von Braze gehostet, um zu verhindern, dass Nachrichten, die auf sie verweisen, fehlerhaft werden. Um ein Asset dauerhaft zu löschen, kontaktieren Sie den Braze-Support. |
| Medienbibliothek-Assets | Edit Media Library Assets | Medienbibliothek-Assets erstellen und aktualisieren |
| Medienbibliothek-Assets | Replace Media Library Assets | Die Datei eines vorhandenen Medienbibliothek-Assets ersetzen, wobei URL und Asset-ID stabil bleiben |
| Messaging-Rate-Limits | View Messaging Rate Limits | Messaging-Rate-Limits auf Workspace-Ebene anzeigen |
| Messaging-Rate-Limits | Edit Messaging Rate Limits | Messaging-Rate-Limits auf Workspace-Ebene konfigurieren und bearbeiten |
| Operator | Use BrazeAI Operator<sup>TM</sup> | Auf Braze Operator zugreifen und ihn verwenden, um Fragen zu beantworten, die Einrichtung zu unterstützen, Probleme zu beheben und Ideen zu entwickeln |
| Placements | View Placements | Banner-Placements anzeigen |
| Placements | Archive Placements | Banner-Placements archivieren |
| Placements | Edit Placements | Banner-Placements anzeigen, ohne Änderungen vorzunehmen |
| Aktionscodes | View Promotion Codes | Aktionscodes anzeigen |
| Aktionscodes | Export Promotion Codes | Eine Liste von Aktionscodes aus dem Dashboard herunterladen |
| Aktionscodes | Edit Promotion Codes | Aktionscodes erstellen und aktualisieren |
| Abo-Gruppen | Edit Subscriptions | Abo-Gruppen erstellen und aktualisieren |
| Transformationen | Edit Data Transformation | Datentransformationen erstellen und aktualisieren |
| Transformationen | View Data Transformation | Datentransformationen anzeigen |
| Support-Tickets | Create Support Ticket | Support-Tickets erstellen und aktualisieren |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Sonstige Berechtigungen" }