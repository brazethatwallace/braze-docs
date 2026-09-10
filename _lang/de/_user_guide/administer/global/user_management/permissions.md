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

Verwenden Sie Berechtigungssätze, um Berechtigungen zu bündeln, die sich auf bestimmte Themenbereiche oder Aktionen beziehen. Sie können Berechtigungssätze auf Dashboard-Nutzer:innen anwenden, die in verschiedenen Workspaces denselben Zugriff benötigen. Um einen Berechtigungssatz zu erstellen, gehen Sie zu **Einstellungen** > **Nutzer:innenverwaltung** > **Berechtigungssätze** und wählen Sie dann **Berechtigungssatz erstellen** aus. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

{% tabs local %}
{% tab Beispiel-Berechtigungssätze %}
| Name | Berechtigungen |
|-----------|----------------|
| Entwickler:innen | „API-Schlüssel anzeigen“, „API-Schlüssel bearbeiten“, „Interne Gruppen anzeigen“, „Interne Gruppen bearbeiten“, „Nachrichtenaktivitätsprotokoll anzeigen“, „Event-Nutzerprotokoll anzeigen“, „API-Bezeichner anzeigen“, „API-Nutzungs-Dashboard anzeigen“, „API-Limits anzeigen“, „API-Nutzungswarnungen anzeigen“, „API-Nutzungswarnungen bearbeiten“, „SDK-Debugger anzeigen“, „SDK-Debugger bearbeiten“. |
| Marketer | „Campaigns anzeigen“, „Campaigns bearbeiten“, „Campaigns archivieren“, „Canvases anzeigen“, „Canvases bearbeiten“, „Canvases archivieren“, „Frequency-Capping-Regeln anzeigen“, „Frequency-Capping-Regeln bearbeiten“, „Nachrichtenpriorisierung anzeigen“, „Nachrichtenpriorisierung bearbeiten“, „Content Blocks anzeigen“, „Feature-Flags anzeigen“, „Feature-Flags bearbeiten“, „Feature-Flags archivieren“, „Segmente anzeigen“, „Segmente bearbeiten“, „Globale Kontrollgruppe bearbeiten“, „IAM-Templates anzeigen“, „IAM-Templates bearbeiten“, „IAM-Templates archivieren“, „E-Mail-Templates anzeigen“, „E-Mail-Templates bearbeiten“, „E-Mail-Templates archivieren“, „Webhook-Templates anzeigen“, „Webhook-Templates bearbeiten“, „Webhook-Templates archivieren“, „E-Mail-Link-Templates anzeigen“, „E-Mail-Link-Templates bearbeiten“, „Medienbibliothek-Assets anzeigen“, „Standorte anzeigen“, „Standorte bearbeiten“, „Standorte archivieren“, „Aktionscodes anzeigen“, „Aktionscodes bearbeiten“, „Aktionscodes exportieren“, „Präferenzcenter anzeigen“, „Präferenzcenter bearbeiten“, „Dashboard-Berichte bearbeiten“, „Banner-Templates anzeigen“, „Lokalisierungseinstellungen anzeigen“, „Operator verwenden“, „Decisioning Studio Agents anzeigen“. |
| Nutzer:innenverwaltung | „Dashboard-Nutzer:innen bearbeiten“, „Teams anzeigen“, „Teams bearbeiten“, „Teams archivieren“. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Beispiel-Berechtigungssatz" }
{% endtab %}
{% endtabs %}

## Erstellen einer Rolle {#creating-a-role}

Rollen ermöglichen eine bessere Struktur, indem sie Ihre individuellen angepassten Berechtigungen mit Workspace-Zugriffskontrollen bündeln. Dies ist besonders nützlich, wenn Sie viele Marken oder regionale Workspaces in einem Dashboard haben. Mit Rollen können Sie Dashboard-Nutzer:innen den entsprechenden Workspaces hinzufügen und ihnen direkt die zugehörigen Berechtigungen gewähren. Um eine Rolle zu erstellen, gehen Sie zu **Einstellungen** > **Nutzer:innenverwaltung** > **Rollen** und wählen Sie **Rolle erstellen**. Eine Beschreibung jeder Berechtigung finden Sie unter [Liste der Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

{% tabs local %}
{% tab Beispielrollen %}
| Rollenname    | Workspace | Berechtigungen
----------- | ----------- | ---------
| Marketer – Modemarken | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | „View Campaigns“, „Edit Campaigns“, „Archive Campaigns“, „View Canvases“, „Edit Canvases“, „Archive Canvases“, „View Content Blocks“, „Edit Content Blocks“, „Archive Content Blocks“, „Launch Content Blocks“, „View Feature Flags“, „Edit Feature Flags“, „Archive Feature Flags“, „View Segments“, „Edit Segments“, „View Banner Templates“, „Edit Banner Templates“, „View Email Templates“, „Edit Email Templates“, „View Media Library Assets“, „Edit Media Library Assets“, „Delete Media Library Assets“, „View Locations“, „Edit Locations“, „Archive Locations“, „View Promotion Codes“, „Edit Promotion Codes“, „Export Promotion Codes“, „View Preference Centers“, „Edit Preference Centers“. |
| Marketer – Hautpflegemarken | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | „View Campaigns“, „Edit Campaigns“, „Archive Campaigns“, „View Canvases“, „Edit Canvases“, „Archive Canvases“, „View Content Blocks“, „Edit Content Blocks“, „Archive Content Blocks“, „Launch Content Blocks“, „View Feature Flags“, „Edit Feature Flags“, „Archive Feature Flags“, „View Segments“, „Edit Segments“, „View Banner Templates“, „Edit Banner Templates“, „View Email Templates“, „Edit Email Templates“, „View Media Library Assets“, „Edit Media Library Assets“, „Delete Media Library Assets“, „View Locations“, „Edit Locations“, „Archive Locations“, „View Promotion Codes“, „Edit Promotion Codes“, „Export Promotion Codes“, „View Preference Centers“, „Edit Preference Centers“.|
| Nutzer:innenverwaltung – Alle Marken | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | „Edit Dashboard Users“, „View Teams“, „Edit Teams“, „Archive Teams“|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Beispielrollen" }
{% endtab %}
{% endtabs %}

## Worin unterscheiden sich Berechtigungssätze und Rollen von Teams? {#how-do-permission-sets-and-roles-differ-from-teams}

{% multi_lang_include permissions/differences.md content="Differences" %}

### Überlegungen zum Hinzufügen von Nutzer:innen-Berechtigungen zu Teams {#considerations-for-adding-user-permissions-to-teams}

Beim Versuch, Berechtigungen im Braze-Dashboard zu speichern, können Schwierigkeiten auftreten – insbesondere beim Hinzufügen oder Entfernen von Nutzer:innen aus einem Workspace oder beim Hinzufügen zu einem Team. Der Button **Save/Update Users** kann ausgegraut sein, wenn die Berechtigungen für die Nutzer:innen mit denen identisch sind, die sie bereits auf Workspace-Ebene besitzen. Diese Einschränkung besteht, weil es keinen Vorteil bringt, ein Team zu haben, wenn alle Nutzer:innen die gleichen Berechtigungen wie der gesamte Workspace besitzen.

Um Nutzer:innen erfolgreich einem Team hinzuzufügen und dabei die gleichen Berechtigungen beizubehalten, weisen Sie auf Workspace-Ebene keine Berechtigungen zu. Weisen Sie Berechtigungen stattdessen ausschließlich auf Team-Ebene zu.

## Eingeschränkte Nutzer:innen {#limited-users}

Eingeschränkte Nutzer:innen verfügen über spezifische Berechtigungen, die es ihnen ermöglichen, bestimmte Aspekte des Braze-Dashboards zu verwalten, wobei sie im Vergleich zu Unternehmensadmins und Workspace-Admins Einschränkungen unterliegen.

| Geltungsbereich | Beschreibung |
| --- | --- |
| Berechtigungen | Eingeschränkte Nutzer:innen können die Berechtigungen anderer eingeschränkter Nutzer:innen bearbeiten, wenn sie über die Berechtigung „Dashboard-Nutzer:innen bearbeiten“ verfügen. Sie können auch neue eingeschränkte Nutzer:innen erstellen und deren Berechtigungssätze ändern. Sie können jedoch keine Unternehmensadmin-Konten erstellen oder verwalten. |
| Rolleneinschränkungen | Wenn eingeschränkte Nutzer:innen über alle Berechtigungen außer „Workspace-Admin“ verfügen, haben sie dennoch Zugriff auf alle anderen Berechtigungen, die normalerweise Workspace-Admins gewährt werden. |
| Sichtbarkeit von Berechtigungen | Wenn eingeschränkte Nutzer:innen die Berechtigung „Dashboard-Nutzer:innen bearbeiten“ für einen Workspace (z. B. Dev), aber nicht für einen anderen (z. B. Prod) haben, sehen sie die Prod-Workspace-Berechtigungen nicht auf der Detailseite ihrer Dashboard-Nutzer:innen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Berechtigungen für eingeschränkte Nutzer:innen" }

### Eingeschränkte Nutzer:innen im Vergleich {#compare-limited-users}

| Eingeschränkter Nutzer:innentyp | Beschreibung |
| --- | --- |
| Workspace-Admin | Workspace-Admins haben Berechtigungen, die speziell auf die Verwaltung von Workspaces ausgerichtet sind, verfügen jedoch nicht über die gleiche Autorität wie Unternehmensadmins. Eingeschränkte Nutzer:innen können Berechtigungen erben, die denen von Workspace-Admins ähneln, wenn die entsprechenden Berechtigungen aktiviert sind. |
| Admin (Unternehmensadmin) | Unternehmensadmins haben umfassendere Berechtigungen, einschließlich der Möglichkeit, Dashboard-Nutzer:innen zu löschen. Sie können jedoch nicht ihre eigenen Konten löschen und müssen sich dafür an andere Unternehmensadmins wenden. |
| Schreibgeschützter Zugriff | Um auf Teile des Dashboards zuzugreifen, wie z. B. die Campaigns-Seite, müssen Nutzer:innen über die entsprechenden Anzeigeberechtigungen verfügen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Vergleich eingeschränkter Nutzer:innen" }

### Fehler bei eingeschränktem Zugriff {#limited-access-error}

Nutzer:innen können Meldungen wie „Sie benötigen die Berechtigung „Landing-Pages anzeigen“, um auf diese Seite zuzugreifen" erhalten. In solchen Fällen sollten die Nutzer:innen und der Kontoadmin überprüfen, ob die erforderlichen Berechtigungen erteilt wurden. Falls ja, versuchen Sie das Problem zu beheben, indem Sie die Berechtigungen der Nutzer:innen deaktivieren und anschließend wieder aktivieren.

{% alert note %}
Es ist nicht möglich, Nutzer:innenberechtigungen von einer Dashboard-Nutzer:in auf eine andere zusammenzuführen oder zu importieren.
{% endalert %}

## Nuancen der Nutzer:innen-Berechtigungen {#nuances-of-user-permissions}

Beachten Sie die folgenden Verhaltensweisen, wenn Sie den Dashboard-Zugriff zuweisen:

- **Workspace-Admin versus Unternehmens-Admin:** Workspace-Admins verwalten Berechtigungen innerhalb der zugewiesenen Workspaces. Unternehmens-Admins haben unternehmensweite Befugnisse, einschließlich des Löschens anderer Dashboard-Nutzer:innen.
- **Eingeschränkte Nutzer:innen:** Eingeschränkte Nutzer:innen mit der Berechtigung „Dashboard-Nutzer:innen bearbeiten“ können andere eingeschränkte Nutzer:innen verwalten, jedoch keine Unternehmens-Admin-Konten erstellen oder verwalten.
- **Geltungsbereich von „Dashboard-Nutzer:innen verwalten“:** Auf der Detailseite für Nutzer:innen werden Berechtigungen nur für Workspaces angezeigt, auf die die bearbeitende Person Zugriff hat. Eingeschränkte Nutzer:innen, die in einem Workspace andere Nutzer:innen bearbeiten können, sehen möglicherweise die Berechtigungs-Checkboxen eines anderen Workspace nicht.
- **Button „Berechtigungen zuweisen“:** Wenn Sie Nutzer:innen bearbeiten und diese bereits Berechtigungen auf Workspace-Ebene oder Berechtigungssätze für alle Workspaces haben, die Sie verwalten können, verschwindet der Button **Berechtigungen zuweisen**. Dies geschieht, weil keine weiteren Workspaces mehr auf Workspace-Ebene zugewiesen werden können.
- **Nutzerdaten exportieren:** Für den Export von Nutzerdaten ist neben der Export-Berechtigung auch ein Zugriff auf Workspace-Ebene erforderlich.
- **Zusammengesetzte Berechtigungen:** Einige Bereiche erfordern mehrere Berechtigungen. Beispielsweise erfordert die Konfiguration von [Technologie-Partnern]({{site.baseurl}}/partners) in der Regel sowohl den Partnerzugriff als auch eine grundlegende Leseberechtigung für die zugehörigen Workspace-Features.
- **Nutzerdaten importieren und aktualisieren:** Diese Berechtigung umfasst die Möglichkeit, App-Nutzer:innen-Profile über Import-Flows zu bearbeiten, nicht nur Dashboard-Nutzer:innen-Datensätze.

## Berechtigungen von Nutzer:innen bearbeiten {#edit-a-users-permissions}

Um die aktuellen Admin-, Unternehmens- oder Workspace-Berechtigungen von Nutzer:innen zu bearbeiten, gehen Sie zu **Einstellungen** > **Nutzer:innenverwaltung** > **Unternehmensnutzer:innen** und wählen Sie den entsprechenden Namen aus.

![Die Seite „Unternehmensnutzer:innen“ in Braze mit einer Tabelle der Dashboard-Nutzer:innen.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Admin %}

### Admin {#admin}

Admins haben Zugriff auf alle Features und können alle Unternehmenseinstellungen ändern. Sie können:

- [Genehmigungseinstellungen]({{site.baseurl}}/user_guide/messaging/governance/approvals#turning-on-the-approval-workflow) ändern
- Andere [Braze-Nutzer:innen]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users#adding-company-users) hinzufügen, bearbeiten, löschen, sperren oder entsperren
- Braze-Nutzer:innen als CSV-Datei exportieren

Um Admin-Berechtigungen zu gewähren oder zu entziehen, wählen Sie **This user is an admin** und anschließend **Update user**.

{% alert warning %}
Wenn Sie Admin-Berechtigungen von Nutzer:innen entfernen, können diese nicht mehr auf Braze zugreifen, bis Sie ihnen mindestens eine [Berechtigung auf Unternehmens- oder Workspace-Ebene]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#edit-a-users-permissions) zuweisen.
{% endalert %}

{% endtab %}
{% tab Unternehmen %}

### Unternehmen {#company}

Um die folgenden Berechtigungen auf Unternehmensebene für Nutzer:innen zu verwalten, aktivieren oder deaktivieren Sie das Kontrollkästchen neben der jeweiligen Berechtigung. Wenn Sie fertig sind, wählen Sie **Update user**.

| Berechtigungsname | Beschreibung |
|----------|-----------|
| Unternehmenseinstellungen verwalten | Ermöglicht Nutzer:innen, Berechtigungseinstellungen und Absenderverifizierung zu ändern. |
| Workspaces erstellen und löschen | Ermöglicht Nutzer:innen, Workspaces zu erstellen und zu löschen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Berechtigungen auf Unternehmensebene" }

{% endtab %}
{% tab Workspace %}

### Workspace {#workspace}

Sie können Nutzer:innen für jeden Workspace, dem sie in Braze angehören, unterschiedliche Berechtigungen erteilen. Um deren Berechtigungen auf Workspace-Ebene zu verwalten, wählen Sie **Select workspaces and permissions** und legen Sie die Berechtigungen manuell fest oder weisen Sie einen zuvor erstellten [Berechtigungssatz oder eine Rolle]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#create-a-permission-set) zu. Wenn Sie Nutzer:innen unterschiedliche Berechtigungen für verschiedene Workspaces erteilen müssen, wiederholen Sie diesen Vorgang so oft wie nötig. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

{% subtabs %}
{% subtab Manuell auswählen %}

Wählen Sie unter **Workspaces** einen oder mehrere Workspaces aus dem Dropdown aus. Wählen Sie dann unter **Permissions** eine oder mehrere Berechtigungen aus. Diese Berechtigungen werden nur für die ausgewählten Workspaces zugewiesen. Optional können Sie **Assign workspace admin access** auswählen, um stattdessen alle Berechtigungen für diesen Workspace zu erteilen.

Wenn Sie fertig sind, wählen Sie **Update user**.

![Berechtigungen auf Workspace-Ebene werden in Braze manuell ausgewählt.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Berechtigungssatz zuweisen %}

Wählen Sie unter **Workspaces** einen oder mehrere Workspaces aus dem Dropdown aus. Wählen Sie dann unter **Permission Sets** einen Berechtigungssatz aus. Diese Berechtigungen werden nur für die ausgewählten Workspaces zugewiesen.

Wenn Sie fertig sind, wählen Sie **Update user**.

![Berechtigungen auf Workspace-Ebene werden in Braze über einen Berechtigungssatz zugewiesen.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% subtab Rolle zuweisen %}

Wählen Sie unter **Workspaces** einen oder mehrere Workspaces aus dem Dropdown aus. Wählen Sie dann unter **Role** eine Rolle aus. Diese Berechtigungen werden nur für die ausgewählten Workspaces zugewiesen.

Wenn Sie fertig sind, wählen Sie **Update user**.

![Berechtigungen auf Workspace-Ebene werden in Braze über eine Rolle zugewiesen.]({% image_buster /assets/img/braze_permissions/workspace_level_role.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exportieren von Nutzer:innen-Berechtigungen {#exporting-user-permissions}

Um eine Liste Ihrer Nutzer:innen und deren Berechtigungen herunterzuladen, gehen Sie zu **Einstellungen** > **Nutzer:innenverwaltung** > **Unternehmensnutzer:innen** und wählen Sie dann **Nutzer:innen exportieren** aus. Eine CSV-Datei wird in Kürze an Ihre E-Mail-Adresse gesendet.

## Liste der Berechtigungen {#list-of-permissions}

### Messaging {#messaging}

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| Campaigns | Campaigns anzeigen | Campaigns anzeigen |
| Campaigns | Campaigns starten | Bestehende Campaigns starten, stoppen, pausieren oder fortsetzen |
| Campaigns | Campaigns archivieren | Campaigns ins Archiv verschieben |
| Campaigns | Campaigns bearbeiten | Campaigns erstellen und aktualisieren |
| Campaigns | Campaigns genehmigen und ablehnen | Campaigns genehmigen oder ablehnen. Der [Genehmigungsworkflow für Campaigns]({{site.baseurl}}/user_guide/messaging/governance/approvals) muss aktiviert sein, damit diese Berechtigung greift. |
| Canvas | Canvases anzeigen | Canvases anzeigen |
| Canvas | Canvases archivieren | Canvases ins Archiv verschieben |
| Canvas | Canvases bearbeiten | Canvases erstellen und aktualisieren |
| Canvas | Canvases starten | Bestehende Canvases starten, stoppen, pausieren oder fortsetzen |
| Canvas | Canvases genehmigen und ablehnen | Canvases genehmigen oder ablehnen. Der [Genehmigungsworkflow für Canvases]({{site.baseurl}}/user_guide/messaging/governance/approvals) muss aktiviert sein, damit diese Berechtigung greift. |
| Feature-Flags | Feature-Flags anzeigen | Feature-Flags anzeigen |
| Feature-Flags | Feature-Flags archivieren | Feature-Flags ins Archiv verschieben |
| Feature-Flags | Feature-Flags bearbeiten | Feature-Flags erstellen und aktualisieren |
| Frequency-Capping | Frequency-Capping-Regeln anzeigen | Frequency-Capping-Regeln anzeigen |
| Frequency-Capping | Frequency-Capping-Regeln bearbeiten | Frequency-Capping-Regeln erstellen und aktualisieren |
| Landing-Pages | Landing-Pages anzeigen | Landing-Pages anzeigen |
| Landing-Pages | Landing-Pages veröffentlichen | Einen Landing-Page-Entwurf aktivieren |
| Landing-Pages | Landing-Page-Entwürfe bearbeiten | Landing-Page-Entwürfe erstellen und speichern |
| Nachrichtenarchivierungs-Einstellungen | Nachrichtenarchivierungs-Einstellungen anzeigen | Nachrichtenarchivierungs-Einstellungen anzeigen, ohne Änderungen vorzunehmen |
| Nachrichtenarchivierungs-Einstellungen | Nachrichtenarchivierungs-Einstellungen bearbeiten | Nachrichtenarchivierungs-Einstellungen erstellen und aktualisieren |
| Nachrichtenpriorisierung | Nachrichtenpriorisierung anzeigen | Einstellungen zur Nachrichtenpriorisierung anzeigen, ohne Änderungen vorzunehmen |
| Nachrichtenpriorisierung | Nachrichtenpriorisierung bearbeiten | Einstellungen zur Nachrichtenpriorisierung erstellen und aktualisieren |
| WhatsApp Flows | WhatsApp Flows anzeigen | Alle WhatsApp Flows anzeigen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Messaging-Berechtigungen" }

### Zielgruppe {#audience}

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| Globale Kontrollgruppe | Globale Kontrollgruppe anzeigen | Einrichtungsseite der globalen Kontrollgruppe anzeigen |
| Globale Kontrollgruppe | Globale Kontrollgruppe bearbeiten | Änderungen an der globalen Kontrollgruppe erstellen und speichern. Nutzer:innen mit der Berechtigung „Globale Kontrollgruppe bearbeiten“ benötigen zusätzlich die Berechtigungen „Campaigns bearbeiten“ und „Canvases bearbeiten“. Nutzer:innen mit der Berechtigung „Globale Kontrollgruppe bearbeiten“ erhalten automatisch auch die Berechtigung „Globale Kontrollgruppe anzeigen“. |
| Standorte | Standorte archivieren | Standorte ins Archiv verschieben |
| Standorte | Standorte anzeigen | Standorte anzeigen |
| Standorte | Standorte bearbeiten | Standorte erstellen und bearbeiten |
| Segments | Segmente anzeigen | Segmente anzeigen. Nutzer:innen benötigen die Berechtigung „Segmente anzeigen“, um die Berechtigung „Segmente bearbeiten“ oder „Segmente archivieren“ zu erhalten. |
| Segments | Segmente archivieren | Segmente archivieren und aus dem Archiv wiederherstellen. Nutzer:innen mit der Berechtigung „Segmente archivieren“ benötigen zusätzlich die Berechtigung „Segmente anzeigen“. |
| Segments | Segmente bearbeiten | Segmente erstellen und aktualisieren. Nutzer:innen mit der Berechtigung „Segmente bearbeiten“ benötigen zusätzlich die Berechtigung „Segmente anzeigen“. |
| Nutzerdaten | Nutzerimporte anzeigen | CSV-Nutzerimporte anzeigen, ohne Änderungen vorzunehmen |
| Nutzerdaten | Nutzer:innen importieren | Nutzer:innen ins Dashboard hochladen |
| Nutzerdaten | Nutzerdaten bearbeiten | Nutzerdaten erstellen und aktualisieren |
| Nutzerdaten | Nutzerdaten exportieren | Nutzer:innen aus dem Dashboard herunterladen |
| Doppelte Nutzer:innen | Zusammenführungs-Datensätze anzeigen | Eine Liste der Nutzer:innen-Zusammenführungsdatensätze anzeigen |
| Nutzer:innen | Nutzerprofile anzeigen (PII geschwärzt) | Nutzerprofile unter Einhaltung von PII-Vorgaben anzeigen. Nutzer:innen mit dieser Berechtigung können keine Campaigns speichern oder starten, die auf als PII gekennzeichnete angepasste Attribute verweisen, es sei denn, sie verfügen auch über die Berechtigung „Als PII gekennzeichnete angepasste Attribute anzeigen“.<br><br>Die Berechtigung „Nutzerprofile anzeigen (PII geschwärzt)“ muss vor der Nutzung aktiviert werden. Wenden Sie sich an Ihre:n Customer-Success-Manager:in, um sie für Ihren Workspace zu aktivieren. |
| Nutzer:innen | Event-Eigenschaften von Nutzer:innen anzeigen | Event-Eigenschaften im Tab **Event-Verlauf** in Nutzerprofilen anzeigen |
| Doppelte Nutzer:innen | Doppelte Nutzer:innen zusammenführen | Doppelte Nutzer:innen zu einem:einer Nutzer:in zusammenführen. Duplikate werden nach dem Zusammenführen entfernt. |
| Nutzer:innen löschen | Löschprotokolle von Nutzer:innen anzeigen | Eine Liste der Löschprotokolle von Nutzer:innen anzeigen |
| Nutzer:innen löschen | Nutzer:innen löschen | Nutzer:innen einzeln oder in großen Mengen dauerhaft aus dem Dashboard löschen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Zielgruppen-Berechtigungen" }

### Template {#template}

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| Banner-Templates | Banner-Templates anzeigen | Banner-Templates anzeigen |
| Banner-Templates | Banner-Templates archivieren | Banner-Templates ins Archiv verschieben |
| Banner-Templates | Banner-Templates bearbeiten | Banner-Templates erstellen und aktualisieren |
| Canvas-Templates | Canvas-Templates anzeigen | Canvas-Templates anzeigen |
| Canvas-Templates | Canvas-Templates archivieren | Canvas-Templates ins Archiv verschieben |
| Canvas-Templates | Canvas-Templates erstellen und bearbeiten | Canvas-Templates erstellen und aktualisieren |
| Content Blocks | Content Blocks anzeigen | Content Blocks anzeigen |
| Content Blocks | Content Blocks veröffentlichen | Entworfene Content Blocks veröffentlichen sowie veröffentlichte Content Blocks bearbeiten, archivieren und aus dem Archiv wiederherstellen |
| Content Blocks | Content Blocks archivieren | Content Blocks ins Archiv verschieben |
| Content Blocks | Content Blocks bearbeiten | Content Blocks erstellen und Entwürfe von Content Blocks bearbeiten |
| E-Mail-Link-Templates | E-Mail-Link-Templates anzeigen | Link-Templates anzeigen, ohne Änderungen vorzunehmen |
| E-Mail-Link-Templates | E-Mail-Link-Templates bearbeiten | Link-Templates erstellen und aktualisieren |
| E-Mail-Templates | E-Mail-Templates anzeigen | E-Mail-Templates anzeigen |
| E-Mail-Templates | E-Mail-Templates archivieren | E-Mail-Templates ins Archiv verschieben |
| E-Mail-Templates | E-Mail-Templates bearbeiten | E-Mail-Templates erstellen und aktualisieren |
| IAM-Templates | IAM-Templates anzeigen | In-App-Nachrichten-Templates anzeigen, ohne Änderungen vorzunehmen |
| IAM-Templates | IAM-Templates archivieren | IAM-Templates ins Archiv verschieben |
| IAM-Templates | IAM-Templates bearbeiten | In-App-Nachrichten-Templates erstellen und aktualisieren |
| Landing-Page-Templates | Landing-Page-Templates anzeigen | Landing-Page-Templates anzeigen |
| Landing-Page-Templates | Landing-Page-Templates archivieren | Landing-Page-Templates ins Archiv verschieben |
| Landing-Page-Templates | Landing-Page-Templates bearbeiten | Landing-Page-Templates erstellen und aktualisieren |
| Webhook-Templates | Webhook-Templates anzeigen | Webhook-Templates anzeigen, ohne Änderungen vorzunehmen |
| Webhook-Templates | Webhook-Templates archivieren | Webhook-Templates ins Archiv verschieben |
| Webhook-Templates | Webhook-Templates bearbeiten | Webhook-Templates erstellen und aktualisieren |
| WhatsApp-Nachrichten-Templates | WhatsApp-Nachrichten-Templates anzeigen | Ermöglicht es Nutzer:innen, [WhatsApp-Nachrichten-Templates]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-2-compose-your-whatsapp-message) anzuzeigen |
| WhatsApp-Nachrichten-Templates | WhatsApp-Nachrichten-Templates bearbeiten | Ermöglicht es Nutzer:innen, WhatsApp-Nachrichten-Templates im Template-Builder zu erstellen. Dieses Feature befindet sich derzeit im Early Access. |
| WhatsApp-Nachrichten-Templates von Meta | WhatsApp-Nachrichten-Templates von Meta anzeigen | Alle WhatsApp-Templates anzeigen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Template-Berechtigungen" }

### Partnerintegrationen {#partner-integrations}

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| Currents-Integrationen | Currents-Integrationen anzeigen | Currents-Integrationen und Datenfreigaben (Snowflake Data Sharing und Databricks Delta Sharing) anzeigen |
| Currents-Integrationen | Currents-Integrationen bearbeiten | Currents-Integrationen und Datenfreigaben erstellen, aktualisieren und löschen |
| Technologie-Partner | Technologie-Partner bearbeiten | Technologie-Partner erstellen und aktualisieren |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Partnerintegrationen-Berechtigungen" }

### Dateneinstellungen {#data-settings}

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| Kataloge | Kataloge anzeigen | Kataloge und Selektionen anzeigen |
| Kataloge | Kataloge löschen | Kataloge dauerhaft löschen |
| Kataloge | Kataloge exportieren | Kataloge aus dem Dashboard herunterladen |
| Kataloge | Kataloge bearbeiten | Kataloge und Selektionen erstellen und aktualisieren |
| Cloud-Datenaufnahme | Cloud-Datenaufnahme bearbeiten | Quellen und Synchronisierungen erstellen, aktualisieren und löschen |
| Angepasste Attribute | Angepasste Attribute anzeigen | Angepasste Attribute und Nutzungsbericht anzeigen |
| Angepasste Attribute | Angepasste Attribute exportieren | Angepasste Attribute aus dem Dashboard herunterladen |
| Angepasste Attribute | Angepasste Attribute löschen | Angepasste Attribute dauerhaft löschen |
| Angepasste Attribute | Angepasste Attribute auf Blockliste setzen | Angepasste Attribute zu einer Blockliste hinzufügen, die deren Verwendung im Dashboard einschränkt |
| Angepasste Attribute | Angepasste Attribute bearbeiten | Angepasste Attribute erstellen und aktualisieren |
| Segmentierung nach angepassten Event-Eigenschaften | Segmentierung nach angepassten Event-Eigenschaften bearbeiten | Segmentierung nach angepassten Event-Eigenschaften aktivieren und deaktivieren |
| Angepasste Events | Angepasste Events anzeigen | Angepasste Events und Nutzungsbericht anzeigen sowie angepasste Events zur täglichen Analytics-Berichts-E-Mail hinzufügen |
| Angepasste Events | Angepasste Events exportieren | Angepasste Events aus dem Dashboard herunterladen |
| PII | PII anzeigen | PII anzeigen |
| Angepasste Events | Angepasste Events löschen | Angepasste Events dauerhaft löschen |
| Angepasste Events | Angepasste Events auf Blockliste setzen | Angepasste Events zu einer Blockliste hinzufügen, die deren Verwendung im Dashboard einschränkt |
| Angepasste Events | Angepasste Events bearbeiten | Angepasste Events erstellen und aktualisieren |
| Produkte | Produkte anzeigen | Produkte anzeigen |
| Produkte | Produkte auf Blockliste setzen | Produkte zu einer Blockliste hinzufügen, die deren Verwendung im Dashboard einschränkt |
| Produkte | Produkte bearbeiten | Produkte erstellen und aktualisieren |
| Segmentierung nach Kauf-Eigenschaften | Segmentierung nach Kauf-Eigenschaften bearbeiten | Segmentierung nach Kauf-Event-Eigenschaften aktivieren und deaktivieren |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Dateneinstellungen-Berechtigungen" }

### Einstellungen {#settings}

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| API-Bezeichner | API-Bezeichner anzeigen | API-Bezeichner und andere Bezeichner anzeigen |
| API-Schlüssel | API-Schlüssel anzeigen | API-Schlüssel anzeigen |
| API-Schlüssel | API-Schlüssel bearbeiten | API-Schlüssel erstellen und aktualisieren |
| API-Limits | API-Limits anzeigen | API-Rate-Limits anzeigen |
| API-Nutzungswarnungen | API-Nutzungswarnungen anzeigen | API-Nutzungswarnungen anzeigen |
| API-Nutzungswarnungen | API-Nutzungswarnungen bearbeiten | API-Nutzungswarnungen erstellen und aktualisieren |
| API-Nutzungsdaten | API-Nutzungs-Dashboard anzeigen | Das API-Nutzungs-Dashboard anzeigen |
| App-Einstellungen | App-Einstellungen bearbeiten | Apps in den App-Einstellungen erstellen, bearbeiten und aktualisieren |
| App-Einstellungen | App-Einstellungen anzeigen | Die Seite „App-Einstellungen“ anzeigen |
| Audience-Sync-Einstellungen | Audience-Sync-Einstellungen anzeigen | Alle Einstellungen der verbundenen Audience-Sync-Partner anzeigen |
| Dashboard-Nutzer:innen | Dashboard-Nutzer:innen bearbeiten | Unternehmensnutzer:innen anzeigen, erstellen und bearbeiten |
| E-Mail-Einstellungen | E-Mail-Einstellungen anzeigen | E-Mail-Einstellungen anzeigen |
| E-Mail-Einstellungen | E-Mail-Einstellungen bearbeiten | E-Mail-Einstellungen aktivieren und aktualisieren |
| Event-Nutzerprotokoll | Event-Nutzerprotokoll anzeigen | Event-Nutzerprotokolle anzeigen |
| Interne Gruppen | Interne Nutzergruppen anzeigen | Interne Gruppen anzeigen |
| Interne Gruppen | Interne Nutzergruppen löschen | Interne Gruppen löschen |
| Interne Gruppen | Interne Nutzergruppen bearbeiten | Interne Gruppen erstellen und aktualisieren |
| Nachrichtenaktivitätsprotokoll | Nachrichtenaktivitätsprotokoll anzeigen | Nachrichtenaktivitätsprotokolle anzeigen |
| Mehrsprachige Einstellungen | Lokalisierungseinstellungen anzeigen | Die Seite für mehrsprachige Gebietsschema-Einstellungen anzeigen |
| Mehrsprachige Einstellungen | Lokalisierungseinstellungen löschen | Mehrsprachige Gebietsschemata löschen |
| Mehrsprachige Einstellungen | Lokalisierungseinstellungen bearbeiten | Mehrsprachige Gebietsschemata erstellen |
| Präferenzcenter | Präferenzcenter anzeigen | Präferenzcenter anzeigen |
| Präferenzcenter | Präferenzcenter bearbeiten | Präferenzcenter erstellen und aktualisieren |
| Präferenzcenter | Präferenzcenter veröffentlichen | Einen Präferenzcenter-Entwurf aktivieren oder ein bestehendes Präferenzcenter aktualisieren |
| Push-Einstellungen | Push-Einstellungen anzeigen | Push-Einstellungen anzeigen |
| Push-Einstellungen | Push-Einstellungen bearbeiten | Push-Einstellungen erstellen und aktualisieren |
| SDK-Debugger | SDK-Debugger anzeigen | SDK-Debugger oder Debugging-Sitzungen anzeigen |
| SDK-Debugger | SDK-Debugger bearbeiten | SDK-Debugger-Sitzungen erstellen und herunterladen |
| Tags | Tags anzeigen | Tags anzeigen |
| Tags | Tags löschen | Tags dauerhaft löschen |
| Tags | Tags bearbeiten | Tags erstellen und aktualisieren |
| Teams | Teams anzeigen | Teams anzeigen |
| Teams | Teams archivieren | Teams ins Archiv verschieben |
| Teams | Teams bearbeiten | Teams erstellen und aktualisieren |
| WhatsApp-Einstellungen | WhatsApp-Einstellungen anzeigen | Alle WhatsApp-Kanaleinstellungen anzeigen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Einstellungen-Berechtigungen" }

### Decisioning Studio

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| Decisioning Studio Agents | Decisioning Studio Agent anzeigen | Die Konfiguration von Decisioning Studio Agents anzeigen, ohne Änderungen vorzunehmen |
| Decisioning Studio Audience | Decisioning Studio Audience anzeigen | Zielgruppendetails in den Konfigurationsübersichten von Decisioning Studio Agents einsehen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Decisioning-Studio-Berechtigungen" }

### Sonstiges {#other}

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| App-Nutzung | Nutzungsdaten anzeigen | Nutzungsdaten anzeigen |
| Abrechnung | Abrechnungsdetails anzeigen | Abrechnungsdetails anzeigen |
| Angepasste Agents | KI-Agents der Agent-Konsole anzeigen | Ermöglicht es Nutzer:innen, angepasste KI-Agents anzuzeigen |
| Angepasste Agents | KI-Agents der Agent-Konsole archivieren | Ermöglicht es Nutzer:innen, angepasste KI-Agents zu archivieren |
| Angepasste Agents | KI-Agents der Agent-Konsole bearbeiten | Ermöglicht es Nutzer:innen, angepasste KI-Agents zu erstellen und zu aktualisieren |
| Als PII gekennzeichnete angepasste Attribute | Als PII gekennzeichnete angepasste Attribute anzeigen | Als PII gekennzeichnete angepasste Attribute anzeigen |
| Dashboard-Berichte | Dashboard-Berichte anzeigen | Berichte anzeigen, ohne Änderungen vorzunehmen |
| Dashboard-Berichte | Dashboard-Berichte löschen | Berichte dauerhaft löschen |
| Dashboard-Berichte | Dashboard-Berichte bearbeiten | Berichte erstellen und aktualisieren |
| Domain-Einstellungen | Domain-Einstellungen bearbeiten | Delegierte Domains und benutzerdefinierte Domains unter „Verifizierte Domains“ hinzufügen |
| Verschlüsselung auf Feldebene | Verschlüsselung auf Bezeichner-Feldebene bearbeiten | Einstellungen für die Verschlüsselung auf Feldebene aktivieren und aktualisieren |
| Medienbibliotheks-Assets | Medienbibliotheks-Assets anzeigen | Medienbibliotheks-Assets anzeigen |
| Medienbibliotheks-Assets | Medienbibliotheks-Assets löschen | Medienbibliotheks-Assets aus der Benutzeroberfläche entfernen. Gelöschte Assets werden weiterhin von Braze gehostet, um das Brechen von Nachrichten zu verhindern, die auf sie verweisen. Um ein Asset dauerhaft zu löschen, wenden Sie sich an den Braze-Support. |
| Medienbibliotheks-Assets | Medienbibliotheks-Assets bearbeiten | Medienbibliotheks-Assets erstellen und aktualisieren |
| Medienbibliotheks-Assets | Medienbibliotheks-Assets ersetzen | Die Datei eines bestehenden Medienbibliotheks-Assets ersetzen, wobei URL und Asset-ID stabil bleiben |
| Messaging-Rate-Limits | Messaging-Rate-Limits anzeigen | Messaging-Rate-Limits auf Workspace-Ebene anzeigen |
| Messaging-Rate-Limits | Messaging-Rate-Limits bearbeiten | Messaging-Rate-Limits auf Workspace-Ebene konfigurieren und bearbeiten |
| Operator | BrazeAI Operator<sup>TM</sup> verwenden | Auf den Braze Operator zugreifen und ihn nutzen, um Fragen zu beantworten, die Einrichtung zu begleiten, Probleme zu beheben und Ideen zu entwickeln |
| Placements | Placements anzeigen | Banner-Placements anzeigen |
| Placements | Placements archivieren | Banner-Placements ins Archiv verschieben |
| Placements | Placements bearbeiten | Banner-Placements erstellen und aktualisieren |
| Aktionscodes | Aktionscodes anzeigen | Aktionscodes anzeigen |
| Aktionscodes | Aktionscodes exportieren | Eine Liste von Aktionscodes aus dem Dashboard herunterladen |
| Aktionscodes | Aktionscodes bearbeiten | Aktionscodes erstellen und aktualisieren |
| Abo-Gruppen | Abos bearbeiten | Abo-Gruppen erstellen und aktualisieren |
| Transformationen | Datentransformation bearbeiten | Datentransformationen erstellen und aktualisieren |
| Transformationen | Datentransformation anzeigen | Datentransformationen anzeigen |
| Support-Tickets | Support-Ticket erstellen | Support-Tickets erstellen und aktualisieren |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Sonstige Berechtigungen" }