{% multi_lang_include alerts/important_alerts.md alert="granular permissions ea" %}

{% multi_lang_include video.html id="nv699nw706" source="wistia" %}

## Erstellen eines Berechtigungssatzes {#creating-a-permission-set}

Mit Berechtigungssätzen können Sie Berechtigungen für bestimmte Themenbereiche oder Aktionen bündeln. Sie können Berechtigungssätze auf Dashboard-Nutzer:innen anwenden, die in verschiedenen Workspaces denselben Zugriff benötigen. Um einen Berechtigungssatz zu erstellen, gehen Sie zu **Einstellungen** > **Berechtigungseinstellungen** und wählen Sie dann **Berechtigungssatz erstellen**. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab Beispiel-Berechtigungssätze %}
| Name | Berechtigungen |
|-----------|----------------|
| Entwickler:innen | „API-Schlüssel anzeigen“, „API-Schlüssel bearbeiten“, „Interne Gruppen anzeigen“, „Interne Gruppen bearbeiten“, „Nachrichtenaktivitätsprotokoll anzeigen“, „Event-Nutzerprotokoll anzeigen“, „API-Bezeichner anzeigen“, „API-Nutzungs-Dashboard anzeigen“, „API-Limits anzeigen“, „API-Nutzungswarnungen anzeigen“, „API-Nutzungswarnungen bearbeiten“, „SDK-Debugger anzeigen“, „SDK-Debugger bearbeiten“. |
| Marketer | „Campaigns anzeigen“, „Campaigns bearbeiten“, „Campaigns archivieren“, „Canvases anzeigen“, „Canvases bearbeiten“, „Canvases archivieren“, „Frequency-Capping-Regeln anzeigen“, „Frequency-Capping-Regeln bearbeiten“, „Nachrichtenpriorisierung anzeigen“, „Nachrichtenpriorisierung bearbeiten“, „Content Blocks anzeigen“, „Feature-Flags anzeigen“, „Feature-Flags bearbeiten“, „Feature-Flags archivieren“, „Segmente anzeigen“, „Segmente bearbeiten“, „Globale Kontrollgruppe bearbeiten“, „IAM-Templates anzeigen“, „IAM-Templates bearbeiten“, „IAM-Templates archivieren“, „E-Mail-Templates anzeigen“, „E-Mail-Templates bearbeiten“, „E-Mail-Templates archivieren“, „Webhook-Templates anzeigen“, „Webhook-Templates bearbeiten“, „Webhook-Templates archivieren“, „E-Mail-Link-Templates anzeigen“, „E-Mail-Link-Templates bearbeiten“, „Medienbibliothek-Assets anzeigen“, „Standorte anzeigen“, „Standorte bearbeiten“, „Standorte archivieren“, „Aktionscodes anzeigen“, „Aktionscodes bearbeiten“, „Aktionscodes exportieren“, „Präferenzzentren anzeigen“, „Präferenzzentren bearbeiten“, „Dashboard-Berichte bearbeiten“, „Banner-Templates anzeigen“, „Lokalisierungseinstellungen anzeigen“, „Operator verwenden“, „Decisioning Studio-Agenten anzeigen“. |
| Nutzerverwaltung | „Dashboard-Nutzer:innen bearbeiten“, „Teams anzeigen“, „Teams bearbeiten“, „Teams archivieren“. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Erstellen eines Berechtigungssatzes" }
{% endtab %}
{% endtabs %}

## Eine Rolle erstellen {#creating-a-role}

Rollen ermöglichen eine bessere Strukturierung durch die Bündelung Ihrer individuell angepassten Berechtigungen mit den Zugriffskontrollen für den Workspace. Das ist besonders nützlich, wenn Sie viele Marken oder regionale Workspaces in einem Dashboard haben. Mit Rollen können Sie Dashboard-Nutzer:innen zu den richtigen Workspaces hinzufügen und ihnen direkt die entsprechenden Berechtigungen erteilen. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab Beispielrollen %}
| Rollenname | Workspace | Berechtigungen
----------- | ----------- | ---------
| Marketer – Modemarken | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | „Campaigns anzeigen“, „Campaigns bearbeiten“, „Campaigns archivieren“, „Canvases anzeigen“, „Canvases bearbeiten“, „Canvases archivieren“, „Content Blocks anzeigen“, „Content Blocks bearbeiten“, „Content Blocks archivieren“, „Content Blocks starten“, „Feature-Flags anzeigen“, „Feature-Flags bearbeiten“, „Feature-Flags archivieren“, „Segmente anzeigen“, „Segmente bearbeiten“, „Banner-Templates anzeigen“, „Banner-Templates bearbeiten“, „E-Mail-Templates anzeigen“, „E-Mail-Templates bearbeiten“, „Medienbibliothek-Assets anzeigen“, „Medienbibliothek-Assets bearbeiten“, „Medienbibliothek-Assets löschen“, „Standorte anzeigen“, „Standorte bearbeiten“, „Standorte archivieren“, „Aktionscodes anzeigen“, „Aktionscodes bearbeiten“, „Aktionscodes exportieren“, „Präferenzzentren anzeigen“, „Präferenzzentren bearbeiten“. |
| Marketer – Hautpflegemarken | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | „Campaigns anzeigen“, „Campaigns bearbeiten“, „Campaigns archivieren“, „Canvases anzeigen“, „Canvases bearbeiten“, „Canvases archivieren“, „Content Blocks anzeigen“, „Content Blocks bearbeiten“, „Content Blocks archivieren“, „Content Blocks starten“, „Feature-Flags anzeigen“, „Feature-Flags bearbeiten“, „Feature-Flags archivieren“, „Segmente anzeigen“, „Segmente bearbeiten“, „Banner-Templates anzeigen“, „Banner-Templates bearbeiten“, „E-Mail-Templates anzeigen“, „E-Mail-Templates bearbeiten“, „Medienbibliothek-Assets anzeigen“, „Medienbibliothek-Assets bearbeiten“, „Medienbibliothek-Assets löschen“, „Standorte anzeigen“, „Standorte bearbeiten“, „Standorte archivieren“, „Aktionscodes anzeigen“, „Aktionscodes bearbeiten“, „Aktionscodes exportieren“, „Präferenzzentren anzeigen“, „Präferenzzentren bearbeiten“. |
| Nutzerverwaltung – Alle Marken | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | „Dashboard-Nutzer:innen bearbeiten“, „Teams anzeigen“, „Teams bearbeiten“, „Teams archivieren“ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Eine Rolle erstellen" }
{% endtab %}
{% endtabs %}

## Wie unterscheiden sich Berechtigungssätze und Rollen von Teams? {#how-do-permission-sets-and-roles-differ-from-teams}

{% multi_lang_include permissions.md content="Differences" %}

### Überlegungen zum Hinzufügen von Nutzerberechtigungen zu Teams {#considerations-for-adding-user-permissions-to-teams}

Es kann zu Schwierigkeiten kommen, wenn Sie versuchen, Berechtigungen im Braze-Dashboard zu speichern – insbesondere beim Hinzufügen oder Entfernen von Nutzer:innen aus einem Workspace oder beim Hinzufügen zu einem Team. Der Button **Nutzer:innen speichern/aktualisieren** kann ausgegraut sein, wenn die Berechtigungen der Nutzer:innen mit denen identisch sind, die sie bereits auf Workspace-Ebene besitzen. Diese Einschränkung besteht, da es keinen Vorteil bietet, ein Team zu haben, wenn alle Nutzer:innen über dieselben Berechtigungen wie der gesamte Workspace verfügen.

Um Nutzer:innen erfolgreich zu einem Team hinzuzufügen und dabei die gleichen Berechtigungen beizubehalten, weisen Sie keine Berechtigungen auf Workspace-Ebene zu. Weisen Sie Berechtigungen stattdessen ausschließlich auf Team-Ebene zu.

## Eingeschränkte Nutzer:innen {#limited-users}

Eingeschränkte Nutzer:innen verfügen über spezifische Berechtigungen, die es ihnen ermöglichen, bestimmte Aspekte des Braze-Dashboards zu verwalten, wobei sie im Vergleich zu Unternehmensadministratoren und Workspace-Administratoren Einschränkungen unterliegen.

| Geltungsbereich | Beschreibung |
| --- | --- |
| Berechtigungen | Eingeschränkte Nutzer:innen können die Berechtigungen anderer eingeschränkter Nutzer:innen bearbeiten, wenn sie über die Berechtigung „Dashboard-Nutzer:innen bearbeiten“ verfügen. Sie können auch neue eingeschränkte Nutzer:innen anlegen und deren Berechtigungssätze ändern. Sie können jedoch keine Unternehmensadministratorkonten erstellen oder verwalten. |
| Rollenbeschränkungen | Wenn eingeschränkte Nutzer:innen über alle Berechtigungen außer „Workspace-Administrator“ verfügen, haben sie dennoch Zugriff auf alle anderen Berechtigungen, die normalerweise einem Workspace-Administrator gewährt werden. |
| Sichtbarkeit von Berechtigungen | Wenn eingeschränkte Nutzer:innen die Berechtigung „Dashboard-Nutzer:innen bearbeiten“ für einen Workspace (z. B. Dev) besitzen, jedoch nicht für einen anderen (z. B. Prod), werden die Berechtigungen für den Workspace Prod auf der Detailseite für Dashboard-Nutzer:innen nicht angezeigt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eingeschränkte Nutzer:innen" }

### Vergleich eingeschränkter Nutzer:innen {#comparing-limited-users}

| Eingeschränkter Nutzertyp | Beschreibung |
| --- | --- |
| Workspace-Administrator | Workspace-Administratoren verfügen über spezifische Berechtigungen für die Verwaltung von Workspaces, jedoch nicht über dieselben Befugnisse wie Unternehmensadministratoren. Eingeschränkte Nutzer:innen können ähnliche Berechtigungen wie Workspace-Administratoren erhalten, wenn die erforderlichen Berechtigungen aktiviert sind. |
| Administrator (Unternehmensadministrator) | Unternehmensadministratoren verfügen über umfassendere Berechtigungen, einschließlich der Möglichkeit, Dashboard-Nutzer:innen zu löschen. Sie können jedoch ihre eigenen Konten nicht löschen und müssen sich für diese Aktion an einen anderen Unternehmensadministrator wenden. |
| Nur-Lese-Zugriff | Um auf bestimmte Bereiche des Dashboards zugreifen zu können, wie beispielsweise die Campaigns-Seite, müssen Nutzer:innen über die entsprechenden Anzeigeberechtigungen verfügen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Vergleich eingeschränkter Nutzer:innen" }

### Fehler bei eingeschränktem Zugriff {#limited-access-error}

Nutzer:innen können Meldungen wie „Sie benötigen die Berechtigung ‚Landing-Pages anzeigen', um auf diese Seite zugreifen zu können“ erhalten. In solchen Fällen sollten die Nutzer:innen und der Kontoadministrator überprüfen, ob die erforderlichen Berechtigungen erteilt wurden. Ist dies der Fall, versuchen Sie, das Problem zu beheben, indem Sie die Berechtigungen der Nutzer:innen deaktivieren und anschließend wieder aktivieren.

{% alert note %}
Es ist nicht möglich, Nutzerberechtigungen von einer Dashboard-Nutzer:in auf eine andere zu übertragen oder zu importieren.
{% endalert %}

## Bearbeiten der Berechtigungen von Nutzer:innen {#editing-a-users-permissions}

Um die aktuellen Administrator-, Unternehmens- oder Workspace-Berechtigungen von Nutzer:innen zu bearbeiten, navigieren Sie zu **Einstellungen** > **Unternehmensnutzer:innen** und wählen Sie den entsprechenden Namen aus.

![Die Seite „Unternehmensnutzer:innen“ in Braze mit einer Tabelle der Dashboard-Nutzer:innen.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Admin %}

### Admin

Admins haben Zugriff auf alle Features und können alle Unternehmenseinstellungen ändern. Sie können:

- [Genehmigungseinstellungen]({{site.baseurl}}/user_guide/messaging/governance/approvals/#turning-on-the-approval-workflow) ändern
- Andere [Braze-Nutzer:innen]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users/#adding-company-users) hinzufügen, bearbeiten, löschen, suspendieren oder die Suspendierung aufheben
- Braze-Nutzer:innen als CSV-Datei exportieren

Um Admin-Rechte zu gewähren oder zu entfernen, wählen Sie **This user is an admin** und dann **Update user**.

![Die Details der ausgewählten Nutzer:in mit dem Admin-Kontrollkästchen im Fokus.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:70%;"}

{% alert warning %}
Wenn Sie Nutzer:innen die Administratorrechte entziehen, können diese nicht mehr auf Braze zugreifen, bis Sie ihnen mindestens eine [Berechtigung auf Unternehmens- oder Workspace-Ebene]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/?tab=company&sdktab=granular%20permissions#granularpermissions_editing-a-users-permissions) zuweisen.
{% endalert %}

{% endtab %}
{% tab Unternehmen %}

### Unternehmen {#company}

Um die folgenden Berechtigungen auf Unternehmensebene für Nutzer:innen zu verwalten, aktivieren oder deaktivieren Sie das Kästchen neben der jeweiligen Berechtigung. Wenn Sie fertig sind, wählen Sie **Update user**.

| Berechtigungsname | Beschreibung |
|----------|-----------|
| Unternehmenseinstellungen verwalten | Ermöglicht es Nutzer:innen, Berechtigungseinstellungen und die Senderüberprüfung anzupassen. |
| Workspaces erstellen und löschen | Ermöglicht es Nutzer:innen, Workspaces zu erstellen und zu löschen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Unternehmen" }

{% endtab %}
{% tab Workspace %}

### Workspace

Sie können Nutzer:innen unterschiedliche Berechtigungen für jeden Workspace erteilen, dem sie in Braze angehören. Um die Berechtigungen auf Workspace-Ebene zu verwalten, wählen Sie **Select workspaces and permissions** und legen Sie dann die Berechtigungen manuell fest oder weisen Sie einen zuvor erstellten [Berechtigungssatz oder eine Rolle]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/?sdktab=granular%20permissions#granularpermissions_creating-a-permission-set) zu. Um Nutzer:innen unterschiedliche Berechtigungen für verschiedene Workspaces zu vergeben, wiederholen Sie diesen Vorgang so oft wie nötig. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/?sdktab=granular%20permissions#granularpermissions_list-of-permissions).

{% subtabs %}
{% subtab Manuell auswählen %}

Wählen Sie unter **Workspaces** einen oder mehrere Workspaces aus der Dropdown-Liste. Wählen Sie anschließend unter **Permissions** eine oder mehrere Berechtigungen aus. Diese Berechtigungen gelten nur für die von Ihnen ausgewählten Workspaces. Optional können Sie **Assign workspace admin access** auswählen, wenn Sie den Nutzer:innen stattdessen vollständige Berechtigungen für diesen Workspace gewähren möchten.

Wenn Sie fertig sind, wählen Sie **Update user**.

![Berechtigungen auf Workspace-Ebene, die manuell in Braze ausgewählt werden.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Berechtigungssatz zuweisen %}

Wählen Sie unter **Workspaces** einen oder mehrere Workspaces aus der Dropdown-Liste. Wählen Sie dann unter **Permission Sets** einen Berechtigungssatz aus. Diese Berechtigungen gelten nur für die von Ihnen ausgewählten Workspaces.

Wenn Sie fertig sind, wählen Sie **Update user**.

![Berechtigungen auf Workspace-Ebene, die über einen Berechtigungssatz in Braze zugewiesen werden.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% subtab Rolle zuweisen %}

Wählen Sie unter **Workspaces** einen oder mehrere Workspaces aus der Dropdown-Liste. Wählen Sie anschließend unter **Role** eine Rolle aus. Diese Berechtigungen gelten nur für die von Ihnen ausgewählten Workspaces.

Wenn Sie fertig sind, wählen Sie **Update user**.

![Berechtigungen auf Workspace-Ebene, die über eine Rolle in Braze zugewiesen werden.]({% image_buster /assets/img/braze_permissions/workspace_level_role.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Nutzerberechtigungen exportieren {#exporting-user-permissions}

Um eine Liste Ihrer Nutzer:innen und deren Berechtigungen herunterzuladen, gehen Sie zu **Einstellungen** > **Unternehmensnutzer:innen** und wählen Sie dann **Export Users**. Eine CSV-Datei wird in Kürze an Ihre E-Mail-Adresse gesendet.

![Die Seite „Unternehmensnutzer:innen“ in Braze mit der Option „Export Users“ im Fokus.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

Sie können keine vollständige Berechtigungsmatrix für alle Dashboard-Nutzer:innen in einem Schritt aus dem Braze-Dashboard exportieren. Wenn Sie mehr Details benötigen, als **Export Users** bietet, ziehen Sie die folgenden Optionen in Betracht:

- Verwenden Sie die [automatisierte Nutzerbereitstellung]({{site.baseurl}}/user_guide/administer/global/user_management/automated_user_provisioning/) (SCIM), um Dashboard-Nutzerkonten zu verwalten. Sie können beispielsweise [eine Dashboard-Nutzer:in per E-Mail suchen]({{site.baseurl}}/api/endpoints/scim/get_search_existing_dashboard_user/) oder Nutzerdetails anhand der Ressourcen-ID abrufen, wie unter [Nutzerkontoinformationen anzeigen]({{site.baseurl}}/api/endpoints/scim/get_see_user_account_information/) beschrieben.
- [Kontaktieren Sie den Braze-Support]({{site.baseurl}}/braze_support/). In einigen Fällen kann der Support eine Liste der Konten bereitstellen, jedoch keine vollständige Berechtigungsmatrix.
- Filtern Sie den [Sicherheitsereignisbericht]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/#security-event-report) Ihres Unternehmens, der Ereignisse wie **Konto hinzugefügt** und **Berechtigungen aktualisiert** aufzeichnet, um Berechtigungsänderungen außerhalb des Dashboards zu überprüfen.

## Liste der Berechtigungen {#list-of-permissions}

### Messaging

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| Campaigns | Campaigns anzeigen | Campaigns anzeigen |
| Campaigns | Campaigns starten | Bestehende Campaigns starten, stoppen, pausieren oder fortsetzen |
| Campaigns | Campaigns archivieren | Campaigns in das Archiv verschieben |
| Campaigns | Campaigns bearbeiten | Campaigns erstellen und aktualisieren |
| Campaigns | Campaigns genehmigen und ablehnen | Campaigns genehmigen oder ablehnen. Der [Genehmigungs-Workflow für Campaigns]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) muss aktiviert sein, damit diese Berechtigung gilt. Diese Einstellung befindet sich derzeit in der Early-Access-Phase. Kontaktieren Sie Ihren Account Manager, wenn Sie an einer Teilnahme am Early Access interessiert sind. |
| Canvas | Canvases anzeigen | Canvases anzeigen |
| Canvas | Canvases archivieren | Canvases in das Archiv verschieben |
| Canvas | Canvases bearbeiten | Canvases erstellen und aktualisieren |
| Canvas | Canvases starten | Bestehende Canvases starten, stoppen, pausieren oder fortsetzen |
| Canvas | Canvases genehmigen und ablehnen | Canvases genehmigen oder ablehnen. Der [Genehmigungs-Workflow für Canvases]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) muss aktiviert sein, damit diese Berechtigung gilt. Diese Einstellung befindet sich derzeit in der Early-Access-Phase. Kontaktieren Sie Ihren Account Manager, wenn Sie an einer Teilnahme am Early Access interessiert sind. |
| Feature-Flags | Feature-Flags anzeigen | Feature-Flags anzeigen |
| Feature-Flags | Feature-Flags archivieren | Feature-Flags in das Archiv verschieben |
| Feature-Flags | Feature-Flags bearbeiten | Feature-Flags erstellen und aktualisieren |
| Frequency-Caps | Frequency-Capping-Regeln anzeigen | Frequency-Capping-Regeln anzeigen |
| Frequency-Caps | Frequency-Capping-Regeln bearbeiten | Frequency-Capping-Regeln erstellen und aktualisieren |
| Landing-Pages | Landing-Pages anzeigen | Landing-Pages anzeigen |
| Landing-Pages | Landing-Pages veröffentlichen | Einen Landing-Page-Entwurf aktivieren |
| Landing-Pages | Landing-Page-Entwürfe bearbeiten | Landing-Page-Entwürfe erstellen und speichern |
| Nachrichtenarchivierungseinstellungen | Nachrichtenarchivierungseinstellungen anzeigen | Nachrichtenarchivierungseinstellungen anzeigen, ohne Änderungen vorzunehmen |
| Nachrichtenarchivierungseinstellungen | Nachrichtenarchivierungseinstellungen bearbeiten | Nachrichtenarchivierungseinstellungen erstellen und aktualisieren |
| Nachrichtenpriorisierung | Nachrichtenpriorisierung anzeigen | Nachrichtenpriorisierungseinstellungen anzeigen, ohne Änderungen vorzunehmen |
| Nachrichtenpriorisierung | Nachrichtenpriorisierung bearbeiten | Nachrichtenpriorisierungseinstellungen erstellen und aktualisieren |
| WhatsApp Flows | WhatsApp Flows anzeigen | Alle WhatsApp Flows anzeigen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Messaging" }

### Zielgruppe {#audience}

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| Globale Kontrollgruppe | Globale Kontrollgruppe anzeigen | Die Einrichtungsseite der Globalen Kontrollgruppe anzeigen |
| Globale Kontrollgruppe | Globale Kontrollgruppe bearbeiten | Änderungen an der Globalen Kontrollgruppe erstellen und speichern. Nutzer:innen mit der Berechtigung „Globale Kontrollgruppe bearbeiten“ müssen auch die Berechtigungen „Campaigns bearbeiten“ und „Canvases bearbeiten“ erhalten. Nutzer:innen mit der Berechtigung „Globale Kontrollgruppe bearbeiten“ erhalten auch die Berechtigung „Globale Kontrollgruppe anzeigen“. |
| Standorte | Standorte archivieren | Standorte in das Archiv verschieben |
| Standorte | Standorte anzeigen | Standorte anzeigen |
| Standorte | Standorte bearbeiten | Standorte erstellen und bearbeiten |
| Segmente | Segmente anzeigen | Segmente anzeigen. Nutzer:innen müssen über die Berechtigung „Segmente anzeigen“ verfügen, um die Berechtigung „Segmente bearbeiten“ oder „Segmente archivieren“ zu erhalten. |
| Segmente | Segmente archivieren | Segmente archivieren und aus dem Archiv entfernen. Nutzer:innen mit der Berechtigung „Segmente archivieren“ muss auch die Berechtigung „Segmente anzeigen“ erteilt werden. |
| Segmente | Segmente bearbeiten | Segmente erstellen und aktualisieren. Nutzer:innen mit der Berechtigung „Segmente bearbeiten“ muss auch die Berechtigung „Segmente anzeigen“ erteilt werden. |
| Nutzerdaten | Importierte Nutzer:innen anzeigen | CSV-Nutzerimporte anzeigen, ohne Änderungen vorzunehmen |
| Nutzerdaten | Nutzer:innen importieren | Nutzer:innen in das Dashboard hochladen |
| Nutzerdaten | Nutzerdaten bearbeiten | Nutzerdaten erstellen und aktualisieren |
| Nutzerdaten | Nutzerdaten exportieren | Nutzer:innen vom Dashboard herunterladen |
| Zusammenführungsprotokolle für Nutzer:innen | Zusammengeführte Nutzer:innen anzeigen | Eine Liste der Zusammenführungsdatensätze für Nutzer:innen anzeigen |
| Nutzer:innen | Nutzerprofile PII-konform anzeigen | Nutzerprofile in PII-konformer Weise anzeigen |
| Doppelte Nutzer:innen | Doppelte Nutzer:innen zusammenführen | Doppelte Nutzer:innen zu einer Nutzer:in zusammenführen. Duplikate werden nach dem Zusammenführen entfernt. |
| Nutzer:innen | Nutzer:innen löschen | Nutzer:innen dauerhaft einzeln oder in großen Mengen aus dem Dashboard löschen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Zielgruppe" }

### Template

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| Banner-Templates | Banner-Templates anzeigen | Banner-Templates anzeigen |
| Banner-Templates | Banner-Templates archivieren | Banner-Templates in das Archiv verschieben |
| Banner-Templates | Banner-Templates bearbeiten | Banner-Templates erstellen und aktualisieren |
| Canvas-Templates | Canvas-Templates anzeigen | Canvas-Templates anzeigen |
| Canvas-Templates | Canvas-Templates archivieren | Canvas-Templates in das Archiv verschieben |
| Canvas-Templates | Canvas-Templates erstellen und bearbeiten | Canvas-Templates erstellen und aktualisieren |
| Content Blocks | Content Blocks anzeigen | Content Blocks anzeigen |
| Content Blocks | Content Blocks starten | Entwürfe von Content Blocks veröffentlichen sowie gestartete Content Blocks bearbeiten, archivieren und aus dem Archiv entfernen |
| Content Blocks | Content Blocks archivieren | Content Blocks in das Archiv verschieben |
| Content Blocks | Content Blocks bearbeiten | Content Blocks erstellen und Entwürfe von Content Blocks bearbeiten |
| E-Mail-Link-Templates | E-Mail-Link-Templates anzeigen | Link-Templates anzeigen, ohne Änderungen vorzunehmen |
| E-Mail-Link-Templates | E-Mail-Link-Templates bearbeiten | Link-Templates erstellen und aktualisieren |
| E-Mail-Templates | E-Mail-Templates anzeigen | E-Mail-Templates anzeigen |
| E-Mail-Templates | E-Mail-Templates archivieren | E-Mail-Templates in das Archiv verschieben |
| E-Mail-Templates | E-Mail-Templates bearbeiten | E-Mail-Templates erstellen und aktualisieren |
| IAM-Templates | IAM-Templates anzeigen | In-App-Nachrichten-Templates anzeigen, ohne Änderungen vorzunehmen |
| IAM-Templates | IAM-Templates archivieren | IAM-Templates in das Archiv verschieben |
| IAM-Templates | IAM-Templates bearbeiten | In-App-Nachrichten-Templates erstellen und aktualisieren |
| Landing-Page-Templates | Landing-Page-Templates anzeigen | Landing-Page-Templates anzeigen |
| Landing-Page-Templates | Landing-Page-Templates archivieren | Landing-Page-Templates in das Archiv verschieben |
| Landing-Page-Templates | Landing-Page-Templates bearbeiten | Landing-Page-Templates erstellen und aktualisieren |
| Webhook-Templates | Webhook-Templates anzeigen | Webhook-Templates anzeigen, ohne Änderungen vorzunehmen |
| Webhook-Templates | Webhook-Templates archivieren | Webhook-Templates in das Archiv verschieben |
| Webhook-Templates | Webhook-Templates bearbeiten | Webhook-Templates erstellen und aktualisieren |
| WhatsApp-Nachrichten-Templates | WhatsApp-Nachrichten-Templates anzeigen | Ermöglicht es Nutzer:innen, [WhatsApp-Nachrichten-Templates]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/#step-2-compose-your-whatsapp-message) anzuzeigen. |
| WhatsApp-Nachrichten-Templates | WhatsApp-Nachrichten-Templates bearbeiten | Ermöglicht es Nutzer:innen, WhatsApp-Nachrichten-Templates im Template-Builder zu erstellen. Dieses Feature befindet sich derzeit in der Early-Access-Phase. |
| WhatsApp-Nachrichten-Templates von Meta | WhatsApp-Nachrichten-Templates von Meta anzeigen | Alle WhatsApp-Templates anzeigen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Template" }

### Partnerintegrationen {#partner-integrations}

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| Currents-Integrationen | Currents-Integrationen anzeigen | Currents-Integrationen anzeigen |
| Currents-Integrationen | Currents-Integrationen bearbeiten | Currents-Integrationen erstellen, aktualisieren und löschen |
| Technologie-Partner | Technologie-Partner bearbeiten | Technologie-Partner erstellen und aktualisieren |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Partnerintegrationen" }

### Dateneinstellungen {#data-settings}

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| Kataloge | Kataloge anzeigen | Kataloge und Auswahlen anzeigen |
| Kataloge | Kataloge löschen | Kataloge dauerhaft löschen |
| Kataloge | Kataloge exportieren | Kataloge vom Dashboard herunterladen |
| Kataloge | Kataloge bearbeiten | Kataloge und Auswahlen erstellen und aktualisieren |
| Cloud-Datenaufnahme | Cloud-Datenaufnahme bearbeiten | Quellen und Synchronisierungen erstellen, aktualisieren und löschen |
| Angepasste Attribute | Angepasste Attribute anzeigen | Angepasste Attribute und Nutzungsbericht anzeigen |
| Angepasste Attribute | Angepasste Attribute exportieren | Angepasste Attribute vom Dashboard herunterladen |
| Angepasste Attribute | Angepasste Attribute löschen | Angepasste Attribute dauerhaft löschen |
| Angepasste Attribute | Sperrliste für angepasste Attribute | Angepasste Attribute zu einer Sperrliste hinzufügen, die die Verwendung im Dashboard einschränkt |
| Angepasste Attribute | Angepasste Attribute bearbeiten | Angepasste Attribute erstellen und aktualisieren |
| Segmentierung von angepassten Event-Eigenschaften | Segmentierung von angepassten Event-Eigenschaften bearbeiten | Segmentierung für angepasste Event-Eigenschaften aktivieren und deaktivieren |
| Angepasste Events | Angepasste Events anzeigen | Angepasste Events und Nutzungsberichte anzeigen und angepasste Events zum täglichen Analytics-Bericht per E-Mail hinzufügen |
| Angepasste Events | Angepasste Events exportieren | Angepasste Events vom Dashboard herunterladen |
| PII | PII anzeigen | PII anzeigen |
| Angepasste Events | Angepasste Events löschen | Angepasste Events dauerhaft löschen |
| Angepasste Events | Sperrliste für angepasste Events | Angepasste Events zu einer Sperrliste hinzufügen, die die Verwendung im Dashboard einschränkt |
| Angepasste Events | Angepasste Events bearbeiten | Angepasste Events erstellen und aktualisieren |
| Produkte | Produkte anzeigen | Produkte anzeigen |
| Produkte | Sperrliste für Produkte | Produkte zu einer Sperrliste hinzufügen, die die Verwendung im Dashboard einschränkt |
| Produkte | Produkte bearbeiten | Produkte erstellen und aktualisieren |
| Segmentierung von Kaufeigenschaften | Segmentierung von Kaufeigenschaften bearbeiten | Segmentierung für Kauf-Event-Eigenschaften aktivieren und deaktivieren |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Dateneinstellungen" }

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
| App-Einstellungen | App-Einstellungen bearbeiten | Apps innerhalb der App-Einstellungen erstellen, bearbeiten und aktualisieren |
| App-Einstellungen | App-Einstellungen anzeigen | Die Seite „App-Einstellungen“ anzeigen |
| Audience-Sync-Einstellungen | Audience-Sync-Einstellungen anzeigen | Alle Einstellungen der verbundenen Audience-Sync-Partner anzeigen |
| Dashboard-Nutzer:innen | Dashboard-Nutzer:innen bearbeiten | Unternehmensnutzer:innen anzeigen, erstellen und bearbeiten |
| E-Mail-Einstellungen | E-Mail-Einstellungen anzeigen | E-Mail-Präferenzen anzeigen |
| E-Mail-Einstellungen | E-Mail-Einstellungen bearbeiten | E-Mail-Präferenzen aktivieren und aktualisieren |
| Event-Nutzerprotokoll | Event-Nutzerprotokoll anzeigen | Event-Nutzerprotokolle anzeigen |
| Interne Gruppen | Interne Gruppen anzeigen | Interne Gruppen anzeigen |
| Interne Gruppen | Interne Gruppen löschen | Interne Gruppen löschen |
| Interne Gruppen | Interne Gruppen bearbeiten | Interne Gruppen erstellen und aktualisieren |
| Nachrichtenaktivitätsprotokoll | Nachrichtenaktivitätsprotokoll anzeigen | Nachrichtenaktivitätsprotokolle anzeigen |
| Mehrsprachige Einstellungen | Lokalisierungseinstellungen anzeigen | Die Seite für mehrsprachige Gebietsschemaeinstellungen anzeigen |
| Mehrsprachige Einstellungen | Lokalisierungseinstellungen löschen | Mehrsprachige Gebietsschemaeinstellungen löschen |
| Mehrsprachige Einstellungen | Lokalisierungseinstellungen bearbeiten | Mehrsprachige Gebietsschemaeinstellungen erstellen |
| Präferenzzentren | Präferenzzentren anzeigen | Präferenzzentren anzeigen |
| Präferenzzentren | Präferenzzentren bearbeiten | Präferenzzentren erstellen und aktualisieren |
| Präferenzzentren | Präferenzzentren starten | Einen Entwurf für das Präferenzzentrum aktivieren oder ein bestehendes aktualisieren |
| Push-Einstellungen | Push-Einstellungen anzeigen | Push-Einstellungen anzeigen |
| Push-Einstellungen | Push-Einstellungen bearbeiten | Push-Einstellungen erstellen und aktualisieren |
| SDK-Debugger | SDK-Debugger anzeigen | SDK-Debugger oder Debugging-Sitzungen anzeigen |
| SDK-Debugger | SDK-Debugger bearbeiten | SDK-Debugger-Sitzungen erstellen und herunterladen |
| Tags | Tags anzeigen | Tags anzeigen |
| Tags | Tags löschen | Tags dauerhaft löschen |
| Tags | Tags bearbeiten | Tags erstellen und aktualisieren |
| Teams | Teams anzeigen | Teams anzeigen |
| Teams | Teams archivieren | Teams in das Archiv verschieben |
| Teams | Teams bearbeiten | Teams erstellen und aktualisieren |
| WhatsApp-Einstellungen | WhatsApp-Einstellungen anzeigen | Alle WhatsApp-Kanaleinstellungen anzeigen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Einstellungen" }

### Decisioning Studio

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| Decisioning Studio-Agenten | Decisioning Studio-Agenten anzeigen | Konfiguration der Decisioning Studio-Agenten anzeigen, ohne Änderungen vorzunehmen |
| Decisioning Studio-Zielgruppe | Decisioning Studio-Zielgruppe anzeigen | Zielgruppendetails in den Konfigurationsübersichten der Decisioning Studio-Agenten anzeigen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Decisioning Studio" }

### Sonstiges {#other}

| Produktbereich | Berechtigung | Definition |
| --- | --- | --- |
| App-Nutzung | Nutzungsdaten anzeigen | Nutzungsdaten anzeigen |
| Abrechnung | Rechnungsdetails anzeigen | Rechnungsdetails anzeigen |
| Angepasste Agenten | Angepasste KI-Agenten der Agentenkonsole anzeigen | Ermöglicht es Nutzer:innen, angepasste KI-Agenten anzuzeigen |
| Angepasste Agenten | Angepasste KI-Agenten der Agentenkonsole archivieren | Ermöglicht es Nutzer:innen, angepasste KI-Agenten zu archivieren |
| Angepasste Agenten | Angepasste KI-Agenten der Agentenkonsole bearbeiten | Ermöglicht es Nutzer:innen, angepasste KI-Agenten zu erstellen und zu aktualisieren |
| Als PII gekennzeichnete angepasste Attribute | Als PII gekennzeichnete angepasste Attribute anzeigen | Als PII gekennzeichnete angepasste Attribute anzeigen |
| Dashboard-Berichte | Dashboard-Berichte anzeigen | Berichte anzeigen, ohne Änderungen vorzunehmen |
| Dashboard-Berichte | Dashboard-Berichte löschen | Berichte dauerhaft löschen |
| Dashboard-Berichte | Dashboard-Berichte bearbeiten | Berichte erstellen und aktualisieren |
| Domain-Einstellungen | Domain-Einstellungen bearbeiten | Delegierte Domains und angepasste Domains unter „Verifizierte Domains“ hinzufügen |
| Verschlüsselung auf Feldebene | Verschlüsselung auf Bezeichner-Feldebene bearbeiten | Einstellungen für die Verschlüsselung auf Feldebene aktivieren und aktualisieren |
| Medienbibliothek-Assets | Medienbibliothek-Assets anzeigen | Medienbibliothek-Assets anzeigen |
| Medienbibliothek-Assets | Medienbibliothek-Assets löschen | Medienbibliothek-Assets dauerhaft löschen |
| Medienbibliothek-Assets | Medienbibliothek-Assets bearbeiten | Medienbibliothek-Assets erstellen und aktualisieren |
| Messaging-Rate-Limits | Messaging-Rate-Limits anzeigen | Messaging-Rate-Limits auf Workspace-Ebene anzeigen |
| Messaging-Rate-Limits | Messaging-Rate-Limits bearbeiten | Messaging-Rate-Limits auf Workspace-Ebene konfigurieren und bearbeiten |
| Operator | BrazeAI Operator<sup>TM</sup> verwenden | Auf BrazeAI Operator zugreifen und ihn nutzen, um Fragen zu beantworten, die Einrichtung zu unterstützen, Probleme zu beheben und Ideen zu entwickeln |
| Platzierungen | Platzierungen anzeigen | Bannerplatzierungen anzeigen |
| Platzierungen | Platzierungen archivieren | Bannerplatzierungen in das Archiv verschieben |
| Platzierungen | Platzierungen bearbeiten | Bannerplatzierungen anzeigen, ohne Änderungen vorzunehmen |
| Aktionscodes | Aktionscodes anzeigen | Aktionscodes anzeigen |
| Aktionscodes | Aktionscodes exportieren | Eine Liste mit Aktionscodes vom Dashboard herunterladen |
| Aktionscodes | Aktionscodes bearbeiten | Aktionscodes erstellen und aktualisieren |
| Abo-Gruppen | Abos bearbeiten | Abo-Gruppen erstellen und aktualisieren |
| Transformationen | Datentransformationen bearbeiten | Datentransformationen erstellen und aktualisieren |
| Transformationen | Datentransformationen anzeigen | Datentransformationen anzeigen |
| Löschprotokolle für Nutzer:innen | Löschprotokolle für Nutzer:innen anzeigen | Löschprotokolle für Nutzer:innen anzeigen |
| Support-Tickets | Support-Ticket erstellen | Support-Tickets erstellen und aktualisieren |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Sonstiges" }