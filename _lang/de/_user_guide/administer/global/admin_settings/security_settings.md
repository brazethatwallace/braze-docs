---
nav_title: Sicherheitseinstellungen
article_title: Sicherheitseinstellungen
page_order: 2
toc_headers: h2
page_type: reference
description: "Dieser Referenzartikel behandelt allgemeine unternehmensübergreifende Sicherheitseinstellungen, einschließlich Authentifizierungsregeln, IP-Zulassungslisten, personenbezogene Daten und Zwei-Faktor-Authentifizierung (2FA)."

---

# Sicherheitseinstellungen

> Als Administrator steht die Sicherheit ganz oben auf Ihrer Liste der Anliegen. Die Seite **Sicherheitseinstellungen** hilft Ihnen bei der Verwaltung der allgemeinen, unternehmensübergreifenden Sicherheitseinstellungen, einschließlich Authentifizierungsregeln, IP-Zulassungsliste und Zwei-Faktor-Authentifizierung.

Um auf diese Seite zuzugreifen, gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen**.

## Regeln für die Authentifizierung

### Passwortlänge

Verwenden Sie dieses Feld, um die erforderliche Mindestlänge des Passworts zu ändern. Der Standardwert beträgt mindestens acht Zeichen.

### Passwortkomplexität

Wählen Sie **Enforce complex passwords**, um zu verlangen, dass Passwörter mindestens eines der folgenden Elemente enthalten müssen:
- Großbuchstabe
- Kleinbuchstabe
- Zahl
- Sonderzeichen

### Wiederverwendbarkeit von Passwörtern

Legt die Mindestanzahl neuer Passwörter fest, die festgelegt werden müssen, bevor ein:e Nutzer:in ein Passwort erneut verwenden kann. Die Standardeinstellung ist drei.

### Regel für den Ablauf von Passwörtern

Verwenden Sie dieses Feld, um festzulegen, wann die Nutzer:innen Ihres Braze-Kontos ihr Passwort zurücksetzen sollen.

### Regeln für die Sitzungsdauer

Verwenden Sie dieses Feld, um festzulegen, wie lange Braze Ihre Sitzung aufrechterhalten soll. Nachdem Braze Ihre Sitzung als inaktiv einstuft (keine Aktivität für die festgelegte Anzahl von Minuten), wird der/die Nutzer:in abgemeldet. Die maximale Anzahl von Minuten, die Sie eingeben können, beträgt 10.080 (entspricht einer Woche), wenn die Zwei-Faktor-Authentifizierung für Ihr Unternehmen erzwungen wird. Andernfalls beträgt die maximale Sitzungsdauer 1.440 Minuten (entspricht 24 Stunden).

### Single Sign-on (SSO)-Authentifizierung

Sie können Ihre Nutzer:innen darauf beschränken, sich entweder mit einem Passwort oder per SSO anzumelden.

Für [SAML SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on) müssen Kund:innen ihre SAML-Einstellungen konfigurieren, bevor sie die Erzwingung aktivieren. Wenn Kund:innen Google SSO verwenden, müssen sie lediglich die Sicherheitseinstellungen-Seite erzwingen, ohne zusätzlichen Aufwand.

## Dashboard-IP-Zulassungsliste

Verwenden Sie das angezeigte Feld, um bestimmte IP-Adressen und Subnetze auf die Zulassungsliste zu setzen, von denen aus sich Nutzer:innen bei Ihrem Konto anmelden können (z. B. aus einem Unternehmensnetzwerk oder VPN). Geben Sie IP-Adressen und Subnetze als CIDR-Bereiche in einer kommagetrennten Liste an. Wenn nichts angegeben ist, können sich Nutzer:innen von jeder IP-Adresse aus anmelden.

## Zwei-Faktor-Authentifizierung (2FA)

Die Zwei-Faktor-Authentifizierung ist für alle Unternehmensnutzer:innen erforderlich. Sie fügt einer Kontoanmeldung eine zweite Ebene der Identitätsüberprüfung hinzu und macht sie sicherer als nur einen Benutzernamen und ein Passwort. Wenn Ihr Dashboard die Zwei-Faktor-Authentifizierung nicht unterstützen kann, wenden Sie sich an Ihren geschäftskunden-Success-Manager.

Wenn die Zwei-Faktor-Authentifizierung aktiviert ist:

- Zusätzlich zur Eingabe eines Passworts müssen Nutzer:innen bei der Anmeldung bei ihrem Braze-Konto einen Verifizierungscode eingeben. Der Code kann über eine Authenticator-App, per E-Mail oder SMS gesendet werden.
- Das Kontrollkästchen **Remember this account for 30 days** wird für Nutzer:innen verfügbar.

Braze sperrt Nutzer:innen, die ihre Zwei-Faktor-Authentifizierung nicht einrichten, aus ihrem Braze-Konto aus. Braze-Kontonutzer:innen können die Zwei-Faktor-Authentifizierung auch selbstständig in den **Kontoeinstellungen** einrichten, auch wenn dies nicht vom Administrator verlangt wird.

Vergessen Sie nicht, Ihre Änderungen zu speichern, bevor Sie die Seite verlassen!

### Dieses Konto 30 Tage merken {#remember-me}

Dieses Feature ist verfügbar, wenn die Zwei-Faktor-Authentifizierung aktiviert ist.

Wenn Sie **Remember this account for 30 days** auswählen, wird ein Cookie auf Ihrem Gerät gespeichert, sodass Sie sich innerhalb von 30 Tagen nur einmal mit der Zwei-Faktor-Authentifizierung anmelden müssen.

![Kontrollkästchen „Dieses Konto 30 Tage merken“]({% image_buster /assets/img/remember_me.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Kund:innen mit mehreren Konten unter einem Dashboard-Unternehmen können Probleme bei der Nutzung dieses Features haben, da das Cookie an ein bestimmtes Gerät gebunden ist. Wenn Nutzer:innen dasselbe Gerät verwenden, um sich bei mehreren Konten anzumelden, wird das Cookie für die zuvor autorisierten Konten auf diesem Gerät ersetzt. Braze erwartet, dass nur ein Gerät mit einem Konto verknüpft ist, nicht ein Gerät für mehrere Konten.

### Zurücksetzen der Nutzerauthentifizierung

Wenn Sie Probleme bei der Anmeldung mit der Zwei-Faktor-Authentifizierung haben, wenden Sie sich an Ihre Unternehmensadministratoren, um Ihre Zwei-Faktor-Authentifizierung zurückzusetzen. Administratoren können die folgenden Schritte ausführen:

1. Gehen Sie zu **Einstellungen** > **Unternehmensnutzer:innen**.
2. Wählen Sie den/die Nutzer:in aus der bereitgestellten Liste aus.
3. Wählen Sie **Reset** unter **Two Factor Authentication**.

Ein Zurücksetzen kann häufige Authentifizierungsprobleme lösen, wie z. B. Schwierigkeiten mit Authenticator-Apps, nicht gesendete E-Mail-Verifizierungen, Anmeldefehler aufgrund von SMS-Ausfällen oder Nutzerfehlern und mehr.

### Anforderungen für 2FA auf Unternehmensebene

Überprüfen Sie zunächst, ob 2FA für Ihr Dashboard aktiviert ist, indem Sie zu **Unternehmenseinstellungen** > **Sicherheitseinstellungen** > **Two Factor Authentication** gehen. Wenn der Schalter grau ist, wurde 2FA für Ihr Unternehmen nicht aktiviert und ist nicht für alle Unternehmensnutzer:innen verpflichtend.

#### Nutzeroptionen, wenn 2FA nicht verpflichtend ist

Wenn 2FA nicht auf Unternehmensebene erzwungen wird, können einzelne Nutzer:innen 2FA für sich selbst auf ihrer Kontoeinstellungen-Seite einrichten. In diesem Fall werden Nutzer:innen nicht aus ihren Konten ausgesperrt, wenn sie es nicht einrichten. Sie können feststellen, welche Nutzer:innen sich für die Aktivierung von 2FA entschieden haben, indem Sie die Seite „Nutzer:innen verwalten“ überprüfen.

#### Anforderungen, wenn 2FA verpflichtend ist

Wenn 2FA auf Unternehmensebene erzwungen wird, werden Nutzer:innen, die es nicht in ihren eigenen Konten bei der Anmeldung einrichten, aus dem Dashboard ausgesperrt. Nutzer:innen müssen die 2FA-Einrichtung abschließen, um den Zugang aufrechtzuerhalten.

{% alert important %}
2FA ist nur dann für alle Unternehmensnutzer:innen erforderlich, wenn Single Sign-on (SSO) nicht aktiviert ist. Wenn SSO verwendet wird, muss 2FA nicht auf Unternehmensebene erzwungen werden.
{% endalert %}

## 2FA manuell einrichten

Um die Zwei-Faktor-Authentifizierung (2FA) manuell in Ihrem Braze-Konto zu aktivieren, folgen Sie diesen Schritten:

1. Wählen Sie in Braze Ihr Profilsymbol in der globalen Kopfzeile und dann **Konto verwalten**. Scrollen Sie zum Abschnitt **Two-Factor Authentication** und wählen Sie **Start Setup**.
2. Geben Sie Ihr Passwort in das Anmelde-Modal ein und wählen Sie **Check Password**.
3. Geben Sie im Modal **Two-Factor Authentication Setup** Ihre Telefonnummer ein und wählen Sie **Enable**.
4. Kopieren Sie den generierten siebenstelligen Code aus Ihrer E-Mail oder SMS-Nachricht, gehen Sie zurück zu Braze und fügen Sie ihn in das Modal **Two-Factor Authentication Setup** ein. Wählen Sie **Verify**.
5. (Optional) Um die 2FA-Eingabe für die nächsten 30 Tage zu vermeiden, aktivieren Sie die Option **Remember this account for 30 days**.

## Elevated Access

Elevated Access fügt eine zusätzliche Sicherheitsebene für sensible Aktionen in Ihrem Braze-Dashboard hinzu. Wenn es aktiv ist, müssen Nutzer:innen ihr Konto erneut verifizieren, bevor sie ein Segment exportieren oder einen API-Schlüssel anzeigen. Um Elevated Access zu verwenden, gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen** und schalten Sie es ein.

Wenn ein:e Nutzer:in die erneute Verifizierung nicht durchführen kann, wird er/sie dorthin zurückgeleitet, wo er/sie aufgehört hat, und kann die sensible Aktion nicht fortsetzen. Nach einer erfolgreichen erneuten Verifizierung muss dies für die nächste Stunde nicht erneut durchgeführt werden – es sei denn, der/die Nutzer:in meldet sich vorher ab.

## Herunterladen eines Sicherheitsereignisberichts {#security-event-report}

Der Sicherheitsereignisbericht ist ein CSV-Bericht über Sicherheitsereignisse wie Kontoeinladungen, Kontoentfernungen, fehlgeschlagene und erfolgreiche Anmeldeversuche und andere Aktivitäten. Sie können ihn für interne Audits verwenden.

Um diesen Bericht herunterzuladen, gehen Sie wie folgt vor:

1. Gehen Sie zu **Einstellungen** > **Admin-Einstellungen**.
2. Wählen Sie den Tab **Sicherheitseinstellungen** und gehen Sie zum Abschnitt **Security Event Download**.
3. Wählen Sie **Download report**.

Dieser manuelle Berichtsdownload enthält nur die letzten 10.000 Sicherheitsereignisse für Ihr Konto. Wenn Ihre exportierte CSV-Datei genau 10.001 Zeilen enthält (einschließlich der Kopfzeile), haben Sie die Obergrenze von 10.000 Ereignissen erreicht und ältere Ereignisse sind möglicherweise nicht enthalten.

Um Sicherheitsereignisse ohne diese Zeilenbegrenzung nach Amazon S3 zu exportieren, siehe [Export von Sicherheitsereignissen mit Amazon S3]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/security_export_s3).

### Spaltendefinitionen der CSV-Datei

Die CSV-Datei des Sicherheitsereignisberichts enthält die folgenden Spalten:

| Spalte | Beschreibung |
|--------|-------------|
| CreatedAt | Zeitstempel, wann das Ereignis aufgezeichnet wurde, in UTC. |
| EmailAtTimeOfEvent | E-Mail-Adresse des/der Dashboard-Nutzer:in, der/die das Ereignis ausgelöst hat, wie zum Zeitpunkt des Ereignisses erfasst. |
| CurrentEmail | Aktuelle E-Mail-Adresse des/der Dashboard-Nutzer:in, der/die das Ereignis ausgelöst hat. Wenn der/die Nutzer:in nicht mehr existiert, wird stattdessen die Entwickler-ID verwendet. |
| EventName | Art des Sicherheitsereignisses. Siehe das Dropdown **Gemeldete Sicherheitsereignisse** nach dieser Tabelle. |
| OtherAccount | E-Mail-Adresse eines/einer anderen Dashboard-Nutzer:in, der/die von dem Ereignis betroffen ist, sofern zutreffend (z. B. wenn ein Konto hinzugefügt oder entfernt wird). |
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
Das Auswählen und Definieren bestimmter Felder als PII-Felder wirkt sich nur darauf aus, was Nutzer:innen im Braze-Dashboard sehen können, und hat keinen Einfluss darauf, wie die Endnutzerdaten in solchen PII-Feldern verarbeitet werden.<br><br>Wenden Sie sich an Ihr Rechtsteam, um die Einstellungen Ihres Dashboards mit allen für Ihr Unternehmen geltenden Datenschutzvorschriften und -richtlinien abzustimmen, einschließlich derjenigen im Zusammenhang mit der [Datenaufbewahrung]({{site.baseurl}}/data_retention).
{% endalert %}

Sie können die Felder auswählen, die Ihr Unternehmen als PII im Dashboard kennzeichnet. Gehen Sie dazu zu **Unternehmenseinstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen**.

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

Sie können diese Einstellung verwenden, um Präferenzen festzulegen, ob Braze bestimmte Felder während des Nutzerlöschungsprozesses für Ereignisse löschen soll. Diese Präferenzen betreffen nur Daten von Nutzer:innen, die Braze gelöscht hat.

Wenn ein:e Nutzer:in gelöscht wird, entfernt Braze alle PII aus den Ereignisdaten, behält aber die anonymisierten Daten für Analytics-Zwecke bei. Einige nutzerdefinierte Felder können PII enthalten, wenn Sie Endnutzerinformationen an Braze senden. Wenn diese Felder PII enthalten, können Sie die Daten löschen lassen, wenn Braze Ereignisdaten für gelöschte Nutzer:innen anonymisiert. Wenn die Felder keine PII enthalten, können Sie sie für Analytics beibehalten.

Sie sind dafür verantwortlich, die richtigen Präferenzen für Ihren Workspace festzulegen. Der beste Weg, die geeigneten Einstellungen zu bestimmen, ist die Überprüfung mit internen Teams, die Ereignisdaten an Braze senden, und mit Teams, die Message Extras in Braze verwenden, um zu bestätigen, ob die Felder PII enthalten können.

### Relevante Felder

| Ereignisname oder -typ | Feld | Hinweise |
| -------------------- | ------ | ----- |
| Angepasstes Event | properties |  |
| Kauf-Event | properties |  |
| Nachrichtenversand | message_extras | Mehrere Ereignistypen enthalten ein `message_extras`-Feld. Die Präferenz gilt für alle Nachrichtenversand-Ereignistypen, die `message_extras` unterstützen, einschließlich zukünftig hinzugefügter Ereignistypen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Relevante Felder" }

{% alert warning %}
**Die Löschung ist dauerhaft!** Wenn Sie sich dafür entscheiden, Felder aus Snowflake für gelöschte Nutzer:innen zu entfernen, gilt die Einstellung für alle historischen Daten in Ihren Workspaces und alle Ereignisse für zukünftig gelöschte Nutzer:innen. Nachdem Braze den Prozess zur Anwendung der Einstellungen auf historische Ereignisdaten für gelöschte Nutzer:innen ausgeführt hat, können Sie die Daten **nicht wiederherstellen**.
{% endalert %}

### Präferenzen konfigurieren

Legen Sie Standardpräferenzen fest, indem Sie die Kontrollkästchen für alle Felder aktivieren, die Braze entfernen soll, wenn ein:e Nutzer:in gelöscht wird. Wählen Sie alle Felder aus, die PII enthalten. Diese Präferenz gilt für alle aktuellen und zukünftigen Workspaces, es sei denn, Workspaces werden explizit einer Präferenzgruppe hinzugefügt.

Um Präferenzen nach Workspace anzupassen, können Sie Präferenzgruppen mit anderen Einstellungen als den Standardeinstellungen hinzufügen. Wir wenden die Standardeinstellungen auf alle Workspaces an, die keiner zusätzlichen Präferenzgruppe hinzugefügt wurden, einschließlich zukünftig erstellter Workspaces.

![Abschnitt „Einstellungen zur Datenlöschung“ mit aktiviertem Schalter zur Anpassung der Datenlöschungspräferenzen nach Workspace.]({% image_buster /assets/img/deletion_preferences_1.png %})

## Fehlerbehebung

### Probleme mit der Einrichtungsschleife der Zwei-Faktor-Authentifizierung (2FA)

Wenn Sie nach erfolgreicher Eingabe Ihrer Telefonnummer für 2FA in einer Schleife gefangen sind und zur Anmeldeseite zurückgeleitet werden, liegt dies wahrscheinlich daran, dass die Verifizierung beim ersten Versuch fehlgeschlagen ist. Um dieses Problem zu beheben, folgen Sie diesen Schritten:

1. Deaktivieren Sie alle Werbeblocker.
2. Aktivieren Sie Cookies in Ihren Browsereinstellungen.
3. Starten Sie Ihren PC oder Laptop neu.
4. Versuchen Sie erneut, 2FA einzurichten.

Wenn das Problem nach diesen Schritten weiterhin besteht, wenden Sie sich an den [Support]({{site.baseurl}}/braze_support) für Unterstützung.

### Zwei-Faktor-Authentifizierung (2FA) kann nicht aktiviert werden

Wenn 2FA aktiviert ist, aber nichts passiert, wenn Sie den Button **Enable** auswählen, kann dies daran liegen, dass Ihr Browser die Weiterleitung blockiert, die zum Senden des Verifizierungscodes per SMS erforderlich ist. Hier sind Schritte zur Fehlerbehebung:

1. Deaktivieren Sie vorübergehend alle Werbeblocker, die Sie in Ihrem Browser aktiviert haben.
2. Bestätigen Sie, dass Sie Drittanbieter-Cookies in Ihren Browsereinstellungen aktiviert haben.
3. Versuchen Sie, 2FA einzurichten.

### Verifizierungscode wird nicht gesendet

Wenn Sie Probleme bei der Eingabe Ihrer Telefonnummer auf der Authy-Seite haben und keine SMS erhalten, folgen Sie diesen Schritten:

1. Installieren Sie die Authy-App auf Ihrem Telefon und melden Sie sich beim Authy-Authenticator an.
2. Geben Sie Ihre Telefonnummer ein und überprüfen Sie die Authy-App auf Änderungen oder SMS-Benachrichtigungen.
3. Wenn Sie immer noch keine SMS erhalten, versuchen Sie eine andere Netzwerkverbindung, z. B. Ihr Heimnetzwerk oder ein nicht-unternehmenseigenes WLAN. Unternehmensnetzwerke können Sicherheitsrichtlinien haben, die die SMS-Zustellung beeinträchtigen.

Wenn die Probleme weiterhin bestehen, löschen Sie das alte Profil in der Authy-App und scannen Sie den QR-Code erneut, um 2FA einzurichten. Stellen Sie sicher, dass Sie alle Werbeblocker deaktiviert, Drittanbieter-Cookies aktiviert oder einen anderen Browser verwendet haben, bevor Sie die Einrichtung erneut versuchen.

## Nächste Schritte

Weitere Informationen zu Authentifizierung und Zugriff finden Sie unter:

- [SAML und Single Sign-on]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on) zur Einrichtung von SSO mit Ihrem Identitätsanbieter.
- [Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) zur Steuerung, welche Aktionen Nutzer:innen im Dashboard ausführen können.