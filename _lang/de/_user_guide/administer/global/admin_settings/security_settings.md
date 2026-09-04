---
nav_title: Sicherheitseinstellungen
article_title: Sicherheitseinstellungen
page_order: 2
toc_headers: h2
page_type: reference
description: "Dieser Referenzartikel behandelt allgemeine unternehmensübergreifende Sicherheitseinstellungen, einschließlich Authentifizierungsregeln, IP-Zulassungslisten, PII und Zwei-Faktor-Authentifizierung (2FA)."
---

# Sicherheitseinstellungen

> Als Administrator:in steht die Sicherheit ganz oben auf Ihrer Prioritätenliste. Die Seite **Sicherheitseinstellungen** hilft Ihnen bei der Verwaltung der allgemeinen, unternehmensübergreifenden Sicherheitseinstellungen, einschließlich Authentifizierungsregeln, IP-Zulassungslisten und Zwei-Faktor-Authentifizierung.

Um auf diese Seite zuzugreifen, gehen Sie zu **Einstellungen** > **Unternehmenseinstellungen** > **Administratoreinstellungen** > **Sicherheitseinstellungen**.

## Authentifizierungsregeln

### Passwortlänge

Verwenden Sie dieses Feld, um die erforderliche Mindestlänge für Passwörter zu ändern. Der Standardmindestwert beträgt acht Zeichen.

### Passwortkomplexität

Wählen Sie **Komplexe Passwörter erzwingen** aus, um zu verlangen, dass Passwörter mindestens eines der folgenden Zeichen enthalten:
- Großbuchstabe
- Kleinbuchstabe
- Zahl
- Sonderzeichen (jedes Zeichen, das kein Buchstabe oder keine Zahl ist, z. B. `!`, `@`, `#` oder `(`)

### Wiederverwendbarkeit von Passwörtern

Bestimmt die Mindestanzahl neuer Passwörter, die festgelegt werden müssen, bevor Nutzer:innen ein Passwort wiederverwenden können. Der Standardwert ist drei.

### Regeln für den Passwortablauf

Verwenden Sie dieses Feld, um festzulegen, wann Nutzer:innen Ihres Braze-Kontos ihr Passwort zurücksetzen sollen.

### Regeln für die Sitzungsdauer

Verwenden Sie dieses Feld, um festzulegen, wie lange Braze Ihre Sitzung aktiv hält. Nachdem Braze Ihre Sitzung als inaktiv eingestuft hat (keine Aktivität für die festgelegte Anzahl von Minuten), meldet Braze die Nutzer:innen ab. Die maximale Anzahl an Minuten, die Sie eingeben können, beträgt 10.080 (entspricht einer Woche), wenn die Zwei-Faktor-Authentifizierung für Ihr Unternehmen erzwungen wird. Andernfalls beträgt die maximale Sitzungsdauer 1.440 Minuten (entspricht 24 Stunden).

### Single-Sign-on-Authentifizierung (SSO)

Sie können Ihre Nutzer:innen darauf beschränken, sich nur mit einem Passwort oder mit SSO anzumelden.

Für [SAML SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on) müssen Kund:innen ihre SAML-Einstellungen konfigurieren, bevor sie diese erzwingen. Wenn Kund:innen Google SSO verwenden, müssen sie lediglich die Sicherheitseinstellungsseite erzwingen, ohne zusätzlichen Aufwand.

## Dashboard-IP-Allowlisting {#dashboard-ip-allowlisting}

Verwenden Sie das angezeigte Feld, um bestimmte IP-Adressen und Subnetze auf die Allowlist zu setzen, von denen aus sich Nutzer:innen bei Ihrem Konto anmelden können (z. B. über ein Firmennetzwerk oder VPN). Geben Sie IP-Adressen und Subnetze als CIDR-Bereiche in einer kommagetrennten Liste an. Wenn keine Angabe erfolgt, können sich Nutzer:innen von jeder beliebigen IP-Adresse aus anmelden.

## Zwei-Faktor-Authentifizierung (2FA)

Die Zwei-Faktor-Authentifizierung ist für alle Unternehmensnutzer:innen erforderlich. Sie fügt einer Kontoanmeldung eine zweite Ebene der Identitätsüberprüfung hinzu und macht sie damit sicherer als nur einen Nutzernamen und ein Passwort. Wenn Ihr Dashboard die Zwei-Faktor-Authentifizierung nicht unterstützen kann, wenden Sie sich an Ihren Customer-Success-Manager.

Wenn die Zwei-Faktor-Authentifizierung aktiviert ist:

- Zusätzlich zur Eingabe eines Passworts müssen Nutzer:innen bei der Anmeldung bei ihrem Braze-Konto einen Verifizierungscode eingeben. Der Code kann über eine Authentifizierungs-App, per E-Mail oder per SMS gesendet werden.
- Das Kontrollkästchen **Dieses Konto für 30 Tage merken** wird für Nutzer:innen verfügbar.

Braze sperrt Nutzer:innen aus ihrem Braze-Konto, die ihre Zwei-Faktor-Authentifizierung nicht einrichten. Braze-Konto-Nutzer:innen können die Zwei-Faktor-Authentifizierung auch eigenständig unter **Kontoeinstellungen** einrichten, selbst wenn sie vom Administrator nicht verlangt wird.

Stellen Sie sicher, dass Sie Ihre Änderungen speichern, bevor Sie die Seite verlassen!

### Dieses Konto für 30 Tage merken {#remember-me}

Dieses Feature ist verfügbar, wenn die Zwei-Faktor-Authentifizierung aktiviert ist.

Wenn Sie **Dieses Konto für 30 Tage merken** auswählen, wird ein Cookie auf Ihrem Gerät gespeichert, sodass Sie sich über einen Zeitraum von 30 Tagen nur einmal mit der Zwei-Faktor-Authentifizierung anmelden müssen.

![Kontrollkästchen „Dieses Konto für 30 Tage merken“]({% image_buster /assets/img/remember_me.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Kund:innen mit mehreren Konten unter einem Dashboard-Unternehmen können bei der Nutzung dieses Features auf Probleme stoßen, da das Cookie an ein bestimmtes Gerät gebunden ist. Wenn Nutzer:innen dasselbe Gerät verwenden, um sich bei mehreren Konten anzumelden, wird das Cookie für die zuvor autorisierten Konten auf diesem Gerät ersetzt. Braze erwartet, dass nur ein Gerät mit einem Konto verknüpft ist, nicht ein Gerät für mehrere Konten.

### Zurücksetzen der Nutzerauthentifizierung

Wenn Sie Probleme bei der Anmeldung mit der Zwei-Faktor-Authentifizierung haben, wenden Sie sich an Ihre Unternehmensadministratoren, um Ihre Zwei-Faktor-Authentifizierung zurückzusetzen. Administratoren können die folgenden Schritte ausführen:

1. Gehen Sie zu **Einstellungen** > **Unternehmenseinstellungen** > **Nutzerverwaltung** > **Unternehmensnutzer:innen**.
2. Wählen Sie den/die Nutzer:in aus der bereitgestellten Liste aus.
3. Wählen Sie **Zurücksetzen** unter **Zwei-Faktor-Authentifizierung** aus.

Ein Zurücksetzen kann häufige Authentifizierungsprobleme lösen, wie z. B. Probleme mit Authentifizierungs-Apps, nicht gesendete E-Mail-Verifizierungen, Anmeldefehler aufgrund von SMS-Ausfällen oder Nutzerfehlern und mehr.

### Anforderungen für 2FA auf Unternehmensebene

Überprüfen Sie zunächst, ob 2FA für Ihr Dashboard aktiviert ist, indem Sie zu **Einstellungen** > **Unternehmenseinstellungen** > **Administratoreinstellungen** > **Sicherheitseinstellungen** > **Zwei-Faktor-Authentifizierung** gehen. Wenn der Umschalter grau ist, wurde 2FA für Ihr Unternehmen nicht aktiviert und ist für alle Unternehmensnutzer:innen nicht verpflichtend.

#### Nutzeroptionen, wenn 2FA nicht verpflichtend ist

Wenn 2FA nicht auf Unternehmensebene durchgesetzt wird, können einzelne Nutzer:innen 2FA für sich selbst auf ihrer Kontoeinstellungsseite einrichten. In diesem Fall werden Nutzer:innen nicht aus ihren Konten ausgesperrt, wenn sie es nicht einrichten. Sie können feststellen, welche Nutzer:innen 2FA aktiviert haben, indem Sie die Liste **Unternehmensnutzer:innen** überprüfen.

#### Anforderungen, wenn 2FA verpflichtend ist

Wenn 2FA auf Unternehmensebene durchgesetzt wird, werden Nutzer:innen, die es bei der Anmeldung nicht in ihren eigenen Konten einrichten, vom Dashboard ausgesperrt. Nutzer:innen müssen die 2FA-Einrichtung abschließen, um den Zugriff aufrechtzuerhalten.

{% alert important %}
2FA ist nur dann für alle Unternehmensnutzer:innen erforderlich, wenn Single Sign-on (SSO) nicht aktiviert ist. Wenn SSO verwendet wird, muss 2FA nicht auf Unternehmensebene durchgesetzt werden.
{% endalert %}

## Zwei-Faktor-Authentifizierung manuell einrichten

Um die Zwei-Faktor-Authentifizierung (2FA) für Ihr Braze-Konto manuell zu aktivieren, führen Sie die folgenden Schritte aus:

1. Wählen Sie in Braze Ihr Profilsymbol in der globalen Kopfzeile und dann **Konto verwalten** aus. Scrollen Sie zum Abschnitt **Zwei-Faktor-Authentifizierung** und wählen Sie **Einrichtung starten** aus.
2. Geben Sie Ihr Passwort in das Anmeldefenster ein und wählen Sie dann **Passwort überprüfen** aus.
3. Geben Sie im Fenster **Einrichtung der Zwei-Faktor-Authentifizierung** Ihre Telefonnummer ein und wählen Sie dann **Aktivieren** aus.
4. Kopieren Sie den generierten siebenstelligen Code aus Ihrer E-Mail oder SMS-Nachricht, kehren Sie dann zu Braze zurück und fügen Sie ihn im Fenster **Einrichtung der Zwei-Faktor-Authentifizierung** ein. Wählen Sie **Überprüfen** aus.
5. (Optional) Um in den nächsten 30 Tagen keine 2FA eingeben zu müssen, aktivieren Sie die Option **Dieses Konto 30 Tage lang merken**.

## Elevated Access

Elevated Access fügt eine zusätzliche Sicherheitsebene für sensible Aktionen in Ihrem Braze-Dashboard hinzu. Wenn es aktiv ist, müssen Nutzer:innen ihr Konto erneut verifizieren, bevor sie ein Segment exportieren oder einen API-Schlüssel anzeigen. Um Elevated Access zu verwenden, gehen Sie zu **Einstellungen** > **Unternehmenseinstellungen** > **Administratoreinstellungen** > **Sicherheitseinstellungen** und schalten Sie es ein.

Wenn ein:e Nutzer:in die erneute Verifizierung nicht durchführen kann, wird er/sie dorthin zurückgeleitet, wo er/sie aufgehört hat, und kann die sensible Aktion nicht fortsetzen. Nach einer erfolgreichen erneuten Verifizierung muss dies für die nächste Stunde nicht erneut durchgeführt werden – es sei denn, der/die Nutzer:in meldet sich vorher ab.

## Herunterladen eines Sicherheitsereignisberichts {#security-event-report}

Der Sicherheitsereignisbericht ist ein CSV-Bericht über Sicherheitsereignisse wie Kontoeinladungen, Kontoentfernungen, fehlgeschlagene und erfolgreiche Anmeldeversuche und andere Aktivitäten. Sie können ihn für interne Audits verwenden.

Um diesen Bericht herunterzuladen, gehen Sie wie folgt vor:

1. Gehen Sie zu **Einstellungen** > **Unternehmenseinstellungen** > **Administratoreinstellungen** > **Sicherheitseinstellungen**.
2. Gehen Sie zum Abschnitt **Sicherheitsereignis-Download**.
3. Wählen Sie **Bericht herunterladen**.

Dieser manuelle Berichtsdownload enthält nur die letzten 10.000 Sicherheitsereignisse für Ihr Konto. Wenn Ihre exportierte CSV-Datei genau 10.001 Zeilen enthält (einschließlich der Kopfzeile), haben Sie die Obergrenze von 10.000 Ereignissen erreicht und ältere Ereignisse sind möglicherweise nicht enthalten.

Um Sicherheitsereignisse ohne diese Zeilenbegrenzung nach Amazon S3 zu exportieren, siehe [Export von Sicherheitsereignissen mit Amazon S3]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/security_export_s3).

### Spaltendefinitionen der CSV-Datei

Die CSV-Datei des Sicherheitsereignisberichts enthält die folgenden Spalten:

| Spalte | Beschreibung |
|--------|-------------|
| CreatedAt | Zeitstempel, wann das Ereignis aufgezeichnet wurde, in UTC. |
| EmailAtTimeOfEvent | E-Mail-Adresse der/des Dashboard-Nutzer:in, die/der das Ereignis ausgelöst hat, wie zum Zeitpunkt des Ereignisses erfasst. |
| CurrentEmail | Aktuelle E-Mail-Adresse der/des Dashboard-Nutzer:in, die/der das Ereignis ausgelöst hat. Wenn die/der Nutzer:in nicht mehr existiert, wird stattdessen die Entwickler-ID verwendet. |
| EventName | Art des Sicherheitsereignisses. Siehe das Dropdown **Gemeldete Sicherheitsereignisse** nach dieser Tabelle. |
| OtherAccount | E-Mail-Adresse einer/eines anderen Dashboard-Nutzer:in, die/der von dem Ereignis betroffen ist, sofern zutreffend (z. B. wenn ein Konto hinzugefügt oder entfernt wird). |
| JsonProperties | Ereignisspezifische Eigenschaften im JSON-Format. Die enthaltenen Felder variieren je nach Ereignistyp. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Spaltendefinitionen der CSV-Datei" }

[S3-Exporte]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/security_export_s3) enthalten diese Spalten plus `Version`, die Schemaversion für das Exportformat (derzeit `1`).

{% details Gemeldete Sicherheitsereignisse %}
### Anmeldung und Konto
- Signed In
- Failed Login
- Two-Factor Auth Setup Completed
- Two-Factor Auth Reset Completed
- Cleared Developer 2FA
- Added Additional Developer
- Added Account
- Developer Suspended
- Developer Unsuspended
- Developer Updated
- Removed Developer
- Removed Account
- User Subscription Status Updated
- User Updated
- Developer Account Updated

### Elevated Access
- Started Elevated Access Flow
- Completed Elevated Access Flow
- Failed 2FA Verification For Elevated Access
- Enabled Elevated Access Enforcement
- Disabled Elevated Access Enforcement

### Campaign
- Added Campaign
- Edited Campaign

### Canvas
- Added Canvas
- Edited Canvas

### Segment
- Added Segment
- Edited Segment
- Exported data to CSV
- Exported Segment via API
- Segment Users Deleted
- Cleared Cohort

### REST-API-Schlüssel
- Added REST API key
- Removed REST API key

### Basic-Auth-Zugangsdaten
- Added Basic Auth credential
- Updated Basic Auth credential
- Removed Basic Auth credential

### Berechtigung
- Cleared Developer 2FA
- Updated Account Permission
- Added Team
- Edited Team
- Archived Team
- Unarchived Team
- Created App Group Permission Set
- Edited App Group Permission Set
- Removed App Group Permission Set
- Created Custom Role
- Updated Custom Role
- Deleted Custom Role

### Unternehmenseinstellungen
- Added App Group
- Added App
- Company Settings Changed
- Updated Company Security Settings
- Updated Security Event Cloud Export
- Added Landing Pages Custom Domain
- Removed Landing Pages Custom Domain
- Custom Domain Created
- Custom Domain Deleted
- Enabled Global Control Group
- Disabled Global Control Group
- Updated Global Control Exclusions
- Updated Subscription Group SMS Allow List

### E-Mail-Template
- Added Email Template
- Updated Email Template

### Push-Zugangsdaten
- Updated Push Credential
- Removed Push Credential

### SDK-Debugger
- Started SDK Debugger Session
- Exported SDK Debugger Log

### Nutzer:innen
- Users Deleted
- Users Viewed
- User Import Started
- User Subscription Group Status Updated
- User Deleted
- Single User Deletion Cancelled
- Bulk User Deletion Cancelled

### Kataloge
- Catalog Created
- Catalog Deleted

### Braze Agents
- Created Agent
- Edited Agent

### BrazeAI Operator
- Requested BrazeAI Operator Response
- BrazeAI Operator Responded
{% enddetails %}

## Anzeigen personenbezogener Daten (PII) {#view-pii}

Die Berechtigung **View PII** ist nur für einige ausgewählte Unternehmensnutzer:innen zugänglich. Standardmäßig ist bei allen Administratoren die Berechtigung **View PII** in den Nutzerberechtigungen aktiviert. Das bedeutet, dass sie alle Standard- und angepassten Attribute sehen können, die Ihr Unternehmen als PII im gesamten Dashboard definiert hat. Wenn diese Berechtigung für Nutzer:innen deaktiviert ist, können diese Nutzer:innen keines dieser Attribute sehen.

{% alert note %}
Sie benötigen die Berechtigung **View PII**, um den [Abfrage-Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder/building_queries) zu verwenden, da dieser direkten Zugriff auf einige Kundendaten ermöglicht.
{% endalert %}

Informationen zu den bestehenden Team-Berechtigungsfunktionen finden Sie unter [Nutzerberechtigungen festlegen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

### PII definieren

{% alert important %}
Das Auswählen und Definieren bestimmter Felder als PII-Felder wirkt sich nur darauf aus, was Nutzer:innen im Braze-Dashboard sehen können, und hat keinen Einfluss darauf, wie die Endnutzer:innendaten in solchen PII-Feldern verarbeitet werden.<br><br>Wenden Sie sich an Ihr Rechtsteam, um die Einstellungen Ihres Dashboards mit allen für Ihr Unternehmen geltenden Datenschutzvorschriften und -richtlinien abzustimmen, einschließlich derjenigen im Zusammenhang mit der [Datenaufbewahrung]({{site.baseurl}}/data_retention).
{% endalert %}

Sie können die Felder auswählen, die Ihr Unternehmen als PII im Dashboard kennzeichnet. Gehen Sie dazu zu **Einstellungen** > **Unternehmenseinstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen**.

Die folgenden Attribute können als PII gekennzeichnet und vor Unternehmensnutzer:innen verborgen werden, die keine Berechtigung **View PII** haben.

#### Potenzielle PII-Attribute

| Standardattribute | Angepasste Attribute |
| ------------------- | ----------------- |
| {::nomarkdown}<ul> <li>E-Mail-Adresse </li> <li> Telefonnummer </li> <li> Vorname </li> <li> Nachname </li> <li> Geschlecht </li> <li> Geburtstag </li> <li> Geräte-IDs </li> <li> LINE-ID </li> <li> Letzter bekannter Standort </li> </ul> {:/} | {::nomarkdown} <ul> <li> Alle angepassten Attribute<ul><li>Einzelne angepasste Attribute können als PII markiert werden, wenn Sie nicht alle Attribute ausblenden müssen.</li></ul></li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Potenzielle PII-Attribute" }

### Eingeschränkte Bereiche

Im Folgenden wird davon ausgegangen, dass alle Felder als PII festgelegt sind und die genannten Nutzer:innen Unternehmensnutzer:innen sind, die die Braze-Plattform verwenden. Außerdem beziehen sich „vorstehende“ Attribute auf die in der Tabelle [Potenzielle PII-Attribute](#potential-pii-attributes). Das Entfernen von PII-Berechtigungen von einem/einer Nutzer:in kann die Nutzbarkeit über diese aufgelisteten Bereiche hinaus beeinträchtigen.

| Dashboard-Navigation | Ergebnis | Hinweise |
| -------------------- | ------ | ----- |
| Nutzersuche | Der/die angemeldete Nutzer:in kann nicht nach E-Mail-Adresse, Telefonnummer, Vorname oder Nachname suchen: {::nomarkdown} <ul> <li> Die vorstehenden Standard- und angepassten Attribute werden beim Anzeigen eines Nutzerprofils nicht angezeigt. </li> <li> Die vorstehenden Standardattribute eines Nutzerprofils können nicht über das Braze-Dashboard bearbeitet werden. </li> <li> Der Abo-Status eines Nutzerprofils kann nicht aktualisiert werden. </li></ul> {:/} | Der Zugriff auf diesen Bereich erfordert weiterhin die Berechtigung zum Anzeigen eines Nutzerprofils. |
| Nutzerimport | Der/die Nutzer:in kann keine Dateien von der Seite **Nutzerimport** herunterladen. | |
| {::nomarkdown} <ul> <li> Segments </li> <li> Campaigns </li> <li> Canvas </li> </ul> {:/} | Im Dropdown **User Data**: {::nomarkdown} <ul> <li> Der/die Nutzer:in hat nicht die Option <b>CSV Export Email Address</b>. </li> <li> Dem/der Nutzer:in werden die vorstehenden Standard- und angepassten Attribute in der CSV-Datei nicht bereitgestellt, wenn <b>CSV Export User Data</b> ausgewählt wird. </li> </ul> {:/} | |
| Interne Testgruppe | Der/die Nutzer:in hat keinen Zugriff auf die vorstehenden Standardattribute von Nutzer:innen, die der internen Testgruppe hinzugefügt wurden. | |
| Nachrichten-Aktivitätsprotokoll | Der/die Nutzer:in hat keinen Zugriff auf die vorstehenden Standardattribute für Nutzer:innen, die im Nachrichten-Aktivitätsprotokoll identifiziert wurden. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Eingeschränkte Bereiche" }

{% alert note %}
Bei der Vorschau einer Nachricht wird die Berechtigung **View PII** nicht angewendet, sodass Nutzer:innen die [vorstehenden Standardattribute](#potential-pii-attributes) sehen können, wenn sie in der Nachricht über Liquid referenziert wurden.
{% endalert %}

## Einstellungen zur Datenlöschung

Sie können diese Einstellung verwenden, um festzulegen, ob Braze bestimmte Felder während des Nutzer:innen-Löschvorgangs für Events löschen soll. Diese Einstellungen betreffen nur Daten von Nutzer:innen, die Braze gelöscht hat.

Wenn Nutzer:innen gelöscht werden, entfernt Braze alle PII aus den Event-Daten, behält aber die anonymisierten Daten für Analytics-Zwecke bei. Einige nutzerdefinierte Felder können PII enthalten, wenn Sie Endnutzer:innen-Informationen an Braze senden. Falls diese Felder PII enthalten, können Sie sich dafür entscheiden, die Daten zu löschen, wenn Braze Event-Daten für gelöschte Nutzer:innen anonymisiert. Falls die Felder keine PII enthalten, können Sie sie für Analytics beibehalten.

Sie sind dafür verantwortlich, die richtigen Einstellungen für Ihren Workspace zu bestimmen. Der beste Weg, die passenden Einstellungen zu ermitteln, besteht darin, sich mit internen Teams abzustimmen, die Event-Daten an Braze senden, und mit Teams, die Message Extras in Braze verwenden, um zu bestätigen, ob die Felder PII enthalten können.

### Relevante Felder

| Event-Name oder -Typ | Feld | Hinweise |
| -------------------- | ------ | ----- |
| Angepasstes Event | properties |  |
| Kauf-Event | properties |  |
| Nachrichtenversand | message_extras | Mehrere Event-Typen enthalten ein `message_extras`-Feld. Die Einstellung gilt für alle Nachrichtenversand-Event-Typen, die `message_extras` unterstützen, einschließlich künftig hinzugefügter Event-Typen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Relevante Felder" }

{% alert warning %}
**Das Löschen ist endgültig!** Wenn Sie sich dafür entscheiden, Felder aus Snowflake für gelöschte Nutzer:innen zu entfernen, gilt die Einstellung für alle historischen Daten in Ihren Workspaces und für alle Events von Nutzer:innen, die in der Zukunft gelöscht werden. Nachdem Braze den Prozess zur Anwendung der Einstellungen auf historische Event-Daten gelöschter Nutzer:innen ausgeführt hat, können Sie die Daten **nicht wiederherstellen**.
{% endalert %}

### Einstellungen konfigurieren

Legen Sie Standardeinstellungen fest, indem Sie die Kontrollkästchen für alle Felder aktivieren, die Braze entfernen soll, wenn Nutzer:innen gelöscht werden. Wählen Sie alle Felder aus, die PII enthalten. Diese Einstellung gilt für alle aktuellen und künftigen Workspaces, sofern Workspaces nicht explizit einer Einstellungsgruppe hinzugefügt werden.

Um Einstellungen nach Workspace anzupassen, können Sie Einstellungsgruppen mit abweichenden Einstellungen vom Standard hinzufügen. Wir wenden die Standardeinstellungen auf alle Workspaces an, die keiner zusätzlichen Einstellungsgruppe hinzugefügt wurden, einschließlich künftig erstellter Workspaces.

![Bereich „Einstellungen zur Datenlöschung“ mit aktiviertem Umschalter zur Anpassung der Datenlöschungseinstellungen nach Workspace.]({% image_buster /assets/img/deletion_preferences_1.png %})

## Fehlerbehebung

### Endlosschleife bei der Einrichtung der Zwei-Faktor-Authentifizierung (2FA)

Wenn Sie nach erfolgreicher Eingabe Ihrer Telefonnummer für die 2FA in einer Schleife gefangen sind und immer wieder zur Anmeldeseite weitergeleitet werden, liegt dies wahrscheinlich daran, dass die Verifizierung beim ersten Versuch fehlgeschlagen ist. Gehen Sie wie folgt vor, um dieses Problem zu beheben:

1. Deaktivieren Sie alle Werbeblocker.
2. Aktivieren Sie Cookies in Ihren Browsereinstellungen.
3. Starten Sie Ihren PC oder Laptop neu.
4. Versuchen Sie erneut, die 2FA einzurichten.

Wenn das Problem nach diesen Schritten weiterhin besteht, wenden Sie sich an den [Support]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### Zwei-Faktor-Authentifizierung (2FA) lässt sich nicht aktivieren

Wenn die 2FA aktiviert ist, aber nichts passiert, wenn Sie den Button **Aktivieren** auswählen, blockiert Ihr Browser möglicherweise die Weiterleitung, die zum Senden des Verifizierungscodes per SMS erforderlich ist. Gehen Sie wie folgt vor, um dieses Problem zu beheben:

1. Deaktivieren Sie vorübergehend alle Werbeblocker in Ihrem Browser.
2. Stellen Sie sicher, dass Drittanbieter-Cookies in Ihren Browsereinstellungen aktiviert sind.
3. Versuchen Sie, die 2FA einzurichten.

### Verifizierungscode wird nicht gesendet

Wenn bei der Eingabe Ihrer Telefonnummer auf der Authy-Seite Probleme auftreten und Sie keine SMS erhalten, gehen Sie wie folgt vor:

1. Installieren Sie die Authy-App auf Ihrem Telefon und melden Sie sich beim Authy-Authenticator an.
2. Geben Sie Ihre Telefonnummer ein und prüfen Sie die Authy-App auf Änderungen oder SMS-Benachrichtigungen.
3. Wenn Sie die SMS immer noch nicht erhalten, versuchen Sie eine andere Netzwerkverbindung, z. B. Ihr Heimnetzwerk oder ein WLAN außerhalb des Unternehmensnetzwerks. Unternehmensnetzwerke können Sicherheitsrichtlinien haben, die die SMS-Zustellung beeinträchtigen.

Wenn die Probleme weiterhin bestehen, löschen Sie das alte Profil in der Authy-App und scannen Sie den QR-Code erneut, um die 2FA einzurichten. Stellen Sie sicher, dass Sie alle Werbeblocker deaktiviert, Drittanbieter-Cookies aktiviert oder einen anderen Browser verwendet haben, bevor Sie die Einrichtung erneut versuchen.

## Nächste Schritte

Weitere Informationen zu Authentifizierung und Zugriff finden Sie unter:

{% article_tiles %}
- name: SAML & Single Sign-on
  link: /docs/user_guide/administer/global/saml_single_sign_on
- name: Berechtigungen
  link: /docs/user_guide/administer/global/user_management/permissions
{% endarticle_tiles %}