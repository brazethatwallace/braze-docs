---
nav_title: DNS-Einträge verstehen
article_title: DNS-Einträge verstehen
page_order: 2
page_type: reference
description: "Dieser Referenzartikel erklärt, wie DNS-Einträge bei den E-Mail-Anbietern von Braze funktionieren, einschließlich SPF, DKIM, DMARC und E-Mail-Anbieter or ESP-spezifischer Eintragsstrukturen."
channel: email
---

# DNS-Einträge verstehen {#understanding-dns-records}

> Diese Referenz erklärt, wie DNS-Einträge in Braze über drei primäre E-Mail-Anbieter (ESPs) funktionieren: SparkPost, SendGrid und Amazon Simple Email Service (SES). Eine korrekte DNS-Konfiguration ist essenziell für die E-Mail-Authentifizierung (SPF, DKIM, DMARC) und die Markenausrichtung und wirkt sich direkt auf die Zustellbarkeit aus.

Weitere Informationen finden Sie unter [E-Mail-Authentifizierung]({{site.baseurl}}/user_guide/channels/email/email_setup/authentication).

## Grundlagen der E-Mail-Authentifizierung {#core-email-authentication-fundamentals}

Bevor Sie sich die anbieterspezifischen Strukturen ansehen, sollten Sie verstehen, was diese Einträge bewirken und wie Braze sie nutzt, um eine korrekte Ausrichtung zu erreichen.

### Sender Policy Framework (SPF) {#spf}

SPF ist ein DNS-Eintrag auf einer Domain, der festlegt, welche IP-Adressen berechtigt sind, E-Mails im Namen dieser Domain zu versenden.

Braze fordert Sie nicht auf, SPF-Einträge auf Ihrer Unternehmens-Root-Domain (z. B. `example.com`) zu ändern oder zu ergänzen. Stattdessen isoliert Braze die Zustellung durch die Verwendung einer dedizierten, angepassten Return-Path-Domain (auch als Bounce-Domain, MAIL-FROM-Domain oder Envelope-From-Domain bekannt), wie etwa `bounce.mail.example.com`.

Da empfangende Postfachanbieter SPF gegen diese Return-Path-Domain und nicht gegen die sichtbare `From:`-Header-Domain validieren, befindet sich die SPF-Konfiguration vollständig auf Subdomain-Ebene. Je nach zugrunde liegendem E-Mail-Anbieter or ESP handhabt Braze diese Validierung auf eine von zwei Arten:

- CNAME-Delegation (SendGrid und SparkPost): Erstellen Sie einen `CNAME`, der Ihre Subdomain zurück zum E-Mail-Anbieter or ESP verweist. Der E-Mail-Anbieter or ESP hostet und aktualisiert die SPF-Richtlinien auf seiner Infrastruktur und besteht die SPF-Prüfung automatisch.
- Expliziter TXT-Eintrag (Amazon SES): Veröffentlichen Sie einen fest codierten `TXT`-Eintrag direkt auf der Bounce-Subdomain mit einem expliziten Autorisierungs-String (zum Beispiel `v=spf1 include:amazonses.com ~all`), der AWS die Berechtigung erteilt, E-Mails aus dieser Zone zu versenden.

### Domain Keys Identified Mail (DKIM) {#dkim}

DKIM fügt dem E-Mail-Header eine kryptografische digitale Signatur hinzu. Der empfangende Server verwendet den öffentlichen Schlüssel des Senders (veröffentlicht im DNS), um zu überprüfen, dass die E-Mail vom Domain-Inhaber stammt und während der Übertragung nicht verändert wurde.

Braze erfordert, dass öffentliche DKIM-Schlüssel über `TXT`- oder `CNAME`-Einträge veröffentlicht werden, damit empfangende ISPs die kryptografischen Signaturen validieren können, die von Ihrem E-Mail-Anbieter or ESP generiert werden.

### DMARC-Ausrichtung {#dmarc}

Damit eine E-Mail DMARC besteht, muss die Domain im für Nutzer:innen sichtbaren `From:`-Header mit der Domain übereinstimmen (ausgerichtet sein), die entweder durch SPF (den Return-Path) oder DKIM validiert wurde. Da Braze-Setups die Ausrichtung sowohl über SPF als auch über DKIM erreichen, werden Ihre DMARC-Richtlinien sicher erfüllt.

Braze übernimmt die grundlegende SPF- und DKIM-Authentifizierung standardmäßig, aber Sie müssen dennoch einen DMARC-Eintrag zu Ihrer Versand-Domain hinzufügen. DMARC ist ein unverzichtbares Authentifizierungswerkzeug, das von nahezu allen großen Posteingangsanbietern verlangt wird. Es beweist, dass Ihre E-Mails legitim sind, baut die Reputation Ihrer Domain auf und hält Ihre Zustellbarkeit langfristig gesund.

Da dies Zugriff auf die Domain-Registrierung Ihres Unternehmens erfordert, müssen Sie oder Ihre Netzwerkadministrator:innen diesen Eintrag auf Root-Domain-Ebene hinzufügen. Wenn Sie gerade erst anfangen, erfüllt eine einfache Richtlinie wie `p=none` die Mindestanforderungen der Posteingangsanbieter. Weitere Informationen zu DMARC finden Sie unter [DMARC.org](https://dmarc.org/). Braze-spezifische DMARC-Anleitungen finden Sie unter [E-Mail-Authentifizierung]({{site.baseurl}}/user_guide/channels/email/email_setup/authentication#dmarc).

## E-Mail-Anbieter or ESP-spezifische DNS-Architektur {#esp-specific-dns-architecture}

Verschiedene E-Mail-Anbieter or ESP-Architekturen handhaben die DNS-Delegation unterschiedlich. Verwenden Sie bei der Einrichtung Ihrer Umgebung genau die Einträge, die Ihrem spezifischen E-Mail-Anbieter or ESP-Cluster zugeordnet sind.

### SparkPost-Architektur {#sparkpost-architecture}

SparkPost verwendet ein hybrides Setup. Es nutzt explizite `CNAME`-Einträge, um Tracking- und Return-Path-Infrastruktur auf SparkPost zurückzuverweisen, während ein reiner `TXT`-Eintrag für die DKIM-Authentifizierung verwendet wird.

- SPF- und Return-Path-Konfiguration: SparkPost fordert eine Subdomain an, die für Bounces vorgesehen ist (zum Beispiel `mail.example.com`). Ein `CNAME`-Eintrag verweist diese Subdomain auf die eingehenden Bounce-Prozessoren von SparkPost. Dadurch wird der Bounce-Verkehr korrekt geroutet und SPF automatisch validiert, da der Zielserver von SparkPost das Protokoll verwaltet.
- DKIM-Konfiguration: SparkPost erfordert einen `TXT`-Eintrag, der den exakten Public-Key-String enthält, der einem bestimmten Selektor zugeordnet ist.
- Klick- und Öffnungs-Tracking: Konfigurieren Sie eine Tracking-Subdomain mit einem `CNAME`, der auf SparkPost-Tracking-Endpunkte verweist (oder einen CDN-Proxy, falls SSL-Tracking angefordert wird).

#### Beispiel einer SparkPost-DNS-Tabelle {#example-sparkpost-dns-table}

Die folgende Tabelle zeigt beispielhafte DNS-Einträge für ein SparkPost-Setup.

| Eintragstyp | Host/Name | Wert/Ziel | Zweck |
| --- | --- | --- | --- |
| CNAME | mail.example.com | smtp.sparkpostmail.com | Return-Path / SPF-Alignment |
| TXT | scph1226._domainkey.mail.example.com | v=DKIM1; k=rsa; p=... | Kryptografische DKIM-Authentifizierung |
| CNAME | Klick, der or klicken.mail.example.com | spgo.io (oder CDN-Endpunkt) | Klick- und Öffnungs-Tracking |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Beispiel einer SparkPost-DNS-Tabelle" }

### SendGrid-Architektur {#sendgrid-architecture}

SendGrid basiert auf einer automatisierten Infrastruktur, die als Domain Authentication bekannt ist. Anstatt rohe `TXT`-Schlüssel bereitzustellen, liefert SendGrid eine Reihe von `CNAME`-Einträgen, die direkt auf von SendGrid verwaltete Server verweisen.

- SPF- und Return-Path-Konfiguration: SendGrid verwendet einen spezifischen `CNAME` (oft mit dem Präfix `em`), der Ihre Sende-Subdomain auf `uXXXXXX.wl.sendgrid.net` abbildet. SendGrid hostet und aktualisiert den SPF-Eintrag auf diesem Endpunkt dynamisch.
- DKIM-Konfiguration: SendGrid generiert zwei separate `CNAME`-Einträge für DKIM (häufig mit Selektoren wie `s1` und `s2`). Diese verweisen zurück auf die Schlüssel von SendGrid.
- SendGrid stellt zwei DKIM-`CNAME`-Einträge bereit, damit kryptografische Schlüssel automatisch rotiert werden können, ohne dass Sie Ihr DNS manuell Update or aktualisieren or aktualisieren müssen.

#### Beispiel einer SendGrid-DNS-Tabelle {#example-sendgrid-dns-table}

Die folgende Tabelle zeigt beispielhafte DNS-Einträge für ein SendGrid-Setup.

| Eintragstyp | Host/Name | Wert/Ziel | Zweck |
| --- | --- | --- | --- |
| CNAME | em.mail.example.com | u123456.wl.sendgrid.net | Return-Path / dynamisches SPF |
| CNAME | s1._domainkey.mail.example.com | s1.domainkey.u123456.wl.sendgrid.net | Primärer DKIM-Schlüssel (rotierend) |
| CNAME | s2._domainkey.mail.example.com | s2.domainkey.u123456.wl.sendgrid.net | Sekundärer DKIM-Schlüssel (rotierend) |
| CNAME | email.mail.example.com | sendgrid.net (oder CDN-Endpunkt) | Klick- und Öffnungs-Tracking |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Beispiel einer SendGrid-DNS-Tabelle" }

### Amazon-SES-Architektur {#amazon-ses-architecture}

Amazon SES verwendet Easy DKIM mit `CNAME`-Einträgen zusammen mit explizitem `MX`- und `TXT`-Routing für angepasstes Bounce-Tracking.

- DKIM-Konfiguration: Amazon SES verwendet Easy DKIM und stellt drei `CNAME`-Einträge bereit. Diese verweisen auf von AWS verwaltete Subdomains, die die Public Keys enthalten. SES rotiert diese Schlüssel automatisch und transparent, um die Sicherheitskonformität aufrechtzuerhalten.
- SPF- und benutzerdefinierte MAIL-FROM-Konfiguration: SendGrid und SparkPost verwalten das Bounce-Domain-Routing über einen `CNAME`. Amazon SES erfordert einen expliziten `MX`-Eintrag und einen `TXT`-Eintrag, die direkt auf der vorgesehenen MAIL-FROM-Subdomain platziert werden. Der `MX`-Eintrag stellt sicher, dass Bounce-Benachrichtigungen an die Server von Amazon zurückgeleitet werden, und der `TXT`-Eintrag enthält den autorisierten, fest codierten SPF-String.

Weitere Informationen finden Sie unter [Amazon-SES-Einrichtung]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/amazon_ses).

#### Beispiel einer Amazon-SES-DNS-Tabelle {#example-amazon-ses-dns-table}

Die folgende Tabelle zeigt beispielhafte DNS-Einträge für ein Amazon-SES-Setup.

| Eintragstyp | Host/Name | Wert/Ziel | Zweck |
| --- | --- | --- | --- |
| CNAME | sel1._domainkey.mail.example.com | sel1.dkim.amazonses.com | Easy-DKIM-Schlüssel 1 (rotierend) |
| CNAME | sel2._domainkey.mail.example.com | sel2.dkim.amazonses.com | Easy-DKIM-Schlüssel 2 (rotierend) |
| CNAME | sel3._domainkey.mail.example.com | sel3.dkim.amazonses.com | Easy-DKIM-Schlüssel 3 (rotierend) |
| MX | bounce.mail.example.com | 10 feedback-smtp.us-east-1.amazonses.com | Leitet Bounce-Verarbeitung an AWS weiter |
| TXT | bounce.mail.example.com | v=spf1 include:amazonses.com ~all | Explizite SPF-Autorisierung |
| CNAME | track.mail.example.com | r.us-east-1.awstrack.me (oder CDN) | Klick- und Öffnungs-Tracking |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Beispiel einer Amazon-SES-DNS-Tabelle" }

## Erweiterte DNS-Überlegungen {#advanced-dns-considerations}

### Aufteilung von TXT-DKIM-Eintragsstrings {#txt-dkim-record-string-splitting}

Beim Einrichten von SparkPost oder manuellen DKIM-Konfigurationen können lange kryptografische Schlüssel (2048-Bit-DKIM-Schlüssel) auftreten.

Die grundlegende DNS-Spezifikation (RFC 1035) begrenzt jeden einzelnen Zeichenstring innerhalb eines `TXT`-Eintrags auf maximal 255 Zeichen. Ein 2048-Bit-Public-Key überschreitet routinemäßig 400 Zeichen, was dazu führt, dass Domain-Registrierungsstellen den einzelnen String ablehnen oder abschneiden und damit die Signatur ungültig machen.

Die Aufteilung von Strings löst dieses Problem. Teilen Sie den Zeichenstring in Abschnitte von weniger als 255 Zeichen auf. Schließen Sie jeden Abschnitt in gerade Anführungszeichen ein, getrennt durch ein Leerzeichen, innerhalb desselben `TXT`-Eintrags.

{% alert note %}
Wenn Sie DNS-Anbieter wie Cloudflare oder AWS Route 53 verwenden, übernehmen diese Schnittstellen die Aufteilung automatisch, wenn Sie einen langen String einfügen. Ältere Systeme (wie GoDaddy oder Network Solutions) erfordern eine manuelle Formatierung der Aufteilung mithilfe der Technik mit doppelten Anführungszeichen.
{% endalert %}

### Dedizierte Subdomains verwenden {#dedicated-subdomains}

Ein häufiger Fehler beim Onboarding ist die Anfrage, eine übergeordnete Organisationsdomain (wie `example.com`) direkt in Braze als Versanddomain zu verwenden. Braze erfordert die Verwendung einer dedizierten Subdomain (zum Beispiel `mail.example.com` oder `engage.example.com`).

Die Verwendung der übergeordneten Domain kann die Unternehmensinfrastruktur auf folgende Weise beeinträchtigen:

#### MX-Eintragskonflikte {#mx-record-conflicts}

Eine Domain kann nur einen Satz primärer Routing-`MX`-Einträge unterstützen. Wenn Sie Ihre übergeordnete Domain (`example.com`) der E-Mail-Anbieter or ESP-Infrastruktur von Braze zuordnen, überschreiben die für Bounces erforderlichen benutzerdefinierten `MX`-Einträge Ihre Unternehmens-E-Mail-Einträge. Dies kann interne Messaging-Plattformen des Unternehmens wie Google Workspace oder Microsoft 365 stören.

#### SPF-Include-Aufblähung und das Limit von 10 Lookups {#spf-include-bloat-and-the-10-lookup-limit}

Die SPF-Spezifikation (RFC 7208) begrenzt empfangende Mailserver auf maximal 10 DNS-Lookups bei der Validierung eines SPF-Eintrags.

- Wenn eine übergeordnete Domain die E-Mail-Anbieter or ESP-Mechanismen von Braze hinzufügt (`include:sparkpostmail.com` oder `include:amazonses.com`), zählt dies erheblich gegen dieses Limit.
- Wird das Limit überschritten, löst dies einen permanenten SPF-PermError aus, wodurch alle Unternehmens-E-Mails die Authentifizierung nicht bestehen.

#### Isolation von IP- und Domain-Reputation {#ip-and-domain-reputation-isolation}

Wenn Marketing-Campaigns, transaktionale Belege und interne Mitarbeiter-E-Mails denselben Root-Domain-Bereich teilen, kann ein plötzlicher Anstieg von Marketing-Spam-Beschwerden die Reputation der übergeordneten Domain beschädigen. Dies birgt das Risiko, dass kritische Unternehmenskommunikation in Spam-Ordner geleitet wird. Die Verwendung einer eigenen Subdomain isoliert die Reputation Ihrer Marketing-Kommunikation.

## Implementierungs-Workflow {#implementation-workflow}

Um eine reibungslose Übergabe und Implementierung sicherzustellen, folgen Sie dieser Reihenfolge:

1. Stellen Sie die strukturierten Einträge Ihrer IT- oder Netzwerkadministration zur Verfügung, damit diese in Ihrer Hosting-Plattform (Cloudflare, Route 53 usw.) hinzugefügt werden können.
2. Legen Sie einen niedrigen TTL-Wert (Time-To-Live) fest (zum Beispiel 300 Sekunden oder fünf Minuten) für erste Tests. Dies ermöglicht eine schnelle Wiederherstellung, falls bei der Eingabe ein Tippfehler gemacht wird.
3. Führen Sie eine DNS-Abfrage durch (zum Beispiel `dig CNAME mail.example.com`) oder verwenden Sie ein Validierungstool, um zu bestätigen, dass die Einträge korrekt aufgelöst werden, bevor Sie zur Aufwärmphase übergehen.

## Dokumentation der DNS-Anbieter {#dns-provider-documentation}

Jeder DNS-Anbieter hat eine eigene Schnittstelle. Teilen Sie diese Spezifikationen mit Ihrem Netzwerkadministrator oder lesen Sie die Dokumentation Ihres jeweiligen Anbieters, um Einträge korrekt in Ihre Zonendatei einzutragen.

Die folgende Tabelle enthält offizielle Dokumentationen für häufig verwendete DNS-Anbieter.

| DNS-Anbieter | Ressourcen |
| --- | --- |
| Cloudflare | [DNS-Einträge verwalten](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) |
| Amazon Route 53 | [Ressourcen-Datensätze erstellen](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html) |
| GoDaddy | [DNS-Einträge verwalten](https://www.godaddy.com/help/manage-dns-records-680) |
| Google Cloud DNS | [DNS-Einträge für einen Domainnamen einrichten](https://cloud.google.com/dns/docs/set-up-dns-records-domain-name) |
| Microsoft Azure DNS | [DNS-Einträge über das Azure-Portal verwalten](https://learn.microsoft.com/en-us/azure/dns/dns-operations-recordsets-portal) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Dokumentation der DNS-Anbieter" }

Weitere Ressourcen zu Domain-Anbietern finden Sie unter [IPs und Domains einrichten]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains#step-2-add-and-verify-a-sending-domain).