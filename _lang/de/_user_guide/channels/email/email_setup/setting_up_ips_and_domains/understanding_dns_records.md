---
nav_title: DNS-Einträge verstehen
article_title: DNS-Einträge verstehen
page_order: 2
page_type: reference
description: "Dieser Referenzartikel erklärt, wie DNS-Einträge bei den E-Mail-Anbietern von Braze funktionieren, einschließlich SPF, DKIM, DMARC und ESP-spezifischer Eintragsstrukturen."
channel: email
---

# DNS-Einträge verstehen {#understanding-dns-records}

> Diese Referenz erklärt, wie DNS-Einträge in Braze über drei primäre E-Mail-Anbieter (ESPs) funktionieren: SparkPost, SendGrid und Amazon Simple Email Service (SES). Eine korrekte DNS-Konfiguration ist essenziell für die E-Mail-Authentifizierung (SPF, DKIM, DMARC) und die Markenausrichtung und wirkt sich direkt auf die Zustellbarkeit aus.

Weitere Informationen finden Sie unter [E-Mail-Authentifizierung]({{site.baseurl}}/user_guide/channels/email/email_setup/authentication).

## Grundlagen der E-Mail-Authentifizierung {#core-email-authentication-fundamentals}

Bevor Sie die anbieterspezifischen Strukturen prüfen, sollten Sie verstehen, was diese Einträge bewirken und wie Braze sie für eine korrekte Ausrichtung nutzt.

### Sender Policy Framework (SPF) {#spf}

SPF ist ein DNS-Eintrag auf einer Domain, der festlegt, welche IP-Adressen berechtigt sind, E-Mails im Namen dieser Domain zu versenden.

Braze fordert Sie nicht auf, SPF-Einträge auf Ihrer Unternehmens-Root-Domain (wie `example.com`) zu ändern oder zu ergänzen. Stattdessen isoliert Braze die Zustellung durch die Verwendung einer dedizierten, angepassten Return-Path-Domain (auch als Bounce-Domain, MAIL-FROM-Domain oder Envelope-From-Domain bekannt), wie z. B. `bounce.mail.example.com`.

Da empfangende Postfachanbieter SPF gegen diese Return-Path-Domain und nicht gegen die sichtbare `From:`-Header-Domain validieren, befindet sich die SPF-Konfiguration vollständig auf Subdomain-Ebene. Je nach zugrunde liegendem ESP handhabt Braze diese Validierung auf eine von zwei Arten:

- CNAME-Delegation (SendGrid und SparkPost): Erstellen Sie einen `CNAME`, der Ihre Subdomain zurück zum ESP verweist. Der ESP hostet und aktualisiert die SPF-Richtlinien auf seiner Infrastruktur und besteht die SPF-Prüfung automatisch.
- Expliziter TXT-Eintrag (Amazon SES): Veröffentlichen Sie einen fest codierten `TXT`-Eintrag direkt auf der Bounce-Subdomain mit einem expliziten Autorisierungsstring (zum Beispiel `v=spf1 include:amazonses.com ~all`), der AWS die Berechtigung gibt, aus dieser Zone zu senden.

### Domain Keys Identified Mail (DKIM) {#dkim}

DKIM fügt dem E-Mail-Header eine kryptografische digitale Signatur hinzu. Der empfangende Server verwendet den öffentlichen Schlüssel des Senders (veröffentlicht im DNS), um zu überprüfen, dass die E-Mail vom Domain-Inhaber stammt und während der Übertragung nicht verändert wurde.

Braze erfordert, dass öffentliche DKIM-Schlüssel über `TXT`- oder `CNAME`-Einträge veröffentlicht werden, damit empfangende ISPs die kryptografischen Signaturen validieren können, die von Ihrem ESP generiert werden.

### DMARC-Ausrichtung {#dmarc}

Damit eine E-Mail DMARC besteht, muss die Domain im für Nutzer:innen sichtbaren `From:`-Header mit der Domain übereinstimmen (ausgerichtet sein), die entweder durch SPF (den Return-Path) oder DKIM validiert wird. Da Braze-Setups die Ausrichtung sowohl über SPF als auch über DKIM erreichen, werden Ihre DMARC-Richtlinien sicher erfüllt.

Braze übernimmt die grundlegende SPF- und DKIM-Authentifizierung standardmäßig, aber Sie müssen dennoch einen DMARC-Eintrag zu Ihrer Sendedomain hinzufügen. DMARC ist ein essenzielles Authentifizierungswerkzeug, das von fast allen großen Posteingangsanbietern verlangt wird. Es beweist, dass Ihre E-Mails legitim sind, baut die Reputation Ihrer Domain auf und hält Ihre Zustellbarkeit langfristig gesund.

Da dies Zugriff auf die Domain-Registrierung Ihres Unternehmens erfordert, müssen Sie oder Ihre Netzwerkadministrator:innen diesen Eintrag auf Root-Domain-Ebene hinzufügen. Wenn Sie gerade erst anfangen, erfüllt eine grundlegende Richtlinie wie `p=none` die Mindestanforderungen der Posteingangsanbieter. Weitere Informationen zu DMARC finden Sie unter [DMARC.org](https://dmarc.org/). Für Braze-spezifische DMARC-Anleitungen siehe [E-Mail-Authentifizierung]({{site.baseurl}}/user_guide/channels/email/email_setup/authentication#dmarc).

## ESP-spezifische DNS-Architektur {#esp-specific-dns-architecture}

Verschiedene ESP-Architekturen handhaben die DNS-Delegation unterschiedlich. Verwenden Sie bei der Bereitstellung Ihrer Umgebung die exakten Einträge, die Ihrem spezifischen ESP-Cluster zugeordnet sind.

### SparkPost-Architektur {#sparkpost-architecture}

SparkPost verwendet ein hybrides Setup. Es nutzt explizite `CNAME`-Einträge, um Tracking- und Return-Path-Infrastruktur zurück zu SparkPost zu verweisen, während ein roher `TXT`-Eintrag für die DKIM-Authentifizierung verwendet wird.

- SPF- und Return-Path-Konfiguration: SparkPost fordert eine für Bounces vorgesehene Subdomain an (zum Beispiel `mail.example.com`). Ein `CNAME`-Eintrag verweist diese Subdomain auf die eingehenden Bounce-Prozessoren von SparkPost. Dies leitet den Bounce-Verkehr korrekt weiter und validiert SPF automatisch, da der Zielserver von SparkPost das Protokoll verwaltet.
- DKIM-Konfiguration: SparkPost erfordert einen `TXT`-Eintrag, der den exakten öffentlichen Schlüsselstring enthält, der einem bestimmten Selektor zugeordnet ist.
- Klick- und Öffnungs-Tracking: Konfigurieren Sie eine Tracking-Subdomain mit einem `CNAME`, der auf SparkPost-Tracking-Endpunkte verweist (oder einen CDN-Proxy, wenn SSL-Tracking angefordert wird).

#### Beispiel einer SparkPost-DNS-Tabelle {#example-sparkpost-dns-table}

Die folgende Tabelle zeigt beispielhafte DNS-Einträge für ein SparkPost-Setup.

| Eintragstyp | Host/Name | Wert/Ziel | Zweck |
| --- | --- | --- | --- |
| CNAME | mail.example.com | smtp.sparkpostmail.com | Return-Path / SPF-Ausrichtung |
| TXT | scph1226._domainkey.mail.example.com | v=DKIM1; k=rsa; p=... | Kryptografische DKIM-Authentifizierung |
| CNAME | click.mail.example.com | spgo.io (oder CDN-Endpunkt) | Klick- und Öffnungs-Tracking |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Beispiel einer SparkPost-DNS-Tabelle" }

### SendGrid-Architektur {#sendgrid-architecture}

SendGrid basiert auf einer automatisierten Infrastruktur, die als Domain Authentication bekannt ist. Anstatt rohe `TXT`-Schlüssel bereitzustellen, liefert SendGrid eine Reihe von `CNAME`-Einträgen, die direkt auf von SendGrid verwaltete Server verweisen.

- SPF- und Return-Path-Konfiguration: SendGrid verwendet einen spezifischen `CNAME` (oft mit dem Präfix `em`), der Ihre Sende-Subdomain auf `uXXXXXX.wl.sendgrid.net` abbildet. SendGrid hostet und aktualisiert den SPF-Eintrag auf diesem Endpunkt dynamisch.
- DKIM-Konfiguration: SendGrid generiert zwei separate `CNAME`-Einträge für DKIM (oft mit Selektoren wie `s1` und `s2`). Diese verweisen zurück auf die Schlüssel von SendGrid.
- SendGrid stellt zwei DKIM-`CNAME`-Einträge bereit, damit kryptografische Schlüssel automatisch rotiert werden können, ohne dass Sie Ihr DNS manuell aktualisieren müssen.

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

- DKIM-Konfiguration: Amazon SES verwendet Easy DKIM und stellt drei `CNAME`-Einträge bereit. Diese verweisen auf von AWS verwaltete Subdomains, die die öffentlichen Schlüssel enthalten. SES rotiert diese Schlüssel automatisch und transparent, um die Sicherheitskonformität aufrechtzuerhalten.
- SPF- und angepasste MAIL-FROM-Konfiguration: SendGrid und SparkPost verwalten das Bounce-Domain-Routing über einen `CNAME`. Amazon SES erfordert einen expliziten `MX`-Eintrag und einen `TXT`-Eintrag, die direkt auf der vorgesehenen MAIL-FROM-Subdomain platziert werden. Der `MX`-Eintrag stellt sicher, dass Bounce-Benachrichtigungen an die Server von Amazon zurückkehren, und der `TXT`-Eintrag enthält den autorisierten, fest codierten SPF-String.

Weitere Informationen finden Sie unter [Amazon-SES-Setup]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/amazon_ses).

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

Beim Einsatz von SparkPost oder manuellen DKIM-Setups können Sie auf lange kryptografische Schlüssel stoßen (2048-Bit-DKIM-Schlüssel).

Die grundlegende DNS-Spezifikation (RFC 1035) begrenzt jeden einzelnen Zeichenstring innerhalb eines `TXT`-Eintrags auf maximal 255 Zeichen. Ein öffentlicher 2048-Bit-Schlüssel überschreitet routinemäßig 400 Zeichen, was dazu führt, dass Domain-Registrierungen den einzelnen String ablehnen oder abschneiden und damit die Signatur ungültig machen.

Die String-Aufteilung löst dieses Problem. Teilen Sie den Zeichenstring in Blöcke von weniger als 255 Zeichen auf. Schließen Sie jeden Block in gerade Anführungszeichen ein, getrennt durch ein Leerzeichen, innerhalb desselben `TXT`-Eintrags.

{% alert note %}
Wenn Sie DNS-Anbieter wie Cloudflare oder AWS Route 53 verwenden, übernehmen diese Schnittstellen die Aufteilung automatisch, wenn Sie einen langen String einfügen. Legacy-Systeme (wie GoDaddy oder Network Solutions) erfordern, dass Sie die Aufteilung manuell mit der Technik der doppelten Anführungszeichen formatieren.
{% endalert %}

### Dedizierte Subdomains verwenden {#dedicated-subdomains}

Ein häufiger Fehler beim Onboarding ist die Anforderung, eine Top-Level-Organisationsdomain (wie `example.com`) direkt in Braze als Sendedomain zu verwenden. Braze erfordert die Verwendung einer dedizierten Subdomain (zum Beispiel `mail.example.com` oder `engage.example.com`).

Die Verwendung der übergeordneten Domain kann die Unternehmensinfrastruktur auf folgende Weise beeinträchtigen:

#### MX-Eintragskonflikte {#mx-record-conflicts}

Eine Domain kann nur einen Satz primärer Routing-`MX`-Einträge unterstützen. Wenn Sie Ihre übergeordnete Domain (`example.com`) auf die ESP-Infrastruktur von Braze abbilden, überschreiben die für Bounces erforderlichen angepassten `MX`-Einträge Ihre Unternehmens-E-Mail-Einträge. Dies kann interne Unternehmens-Messaging-Plattformen wie Google Workspace oder Microsoft 365 stören.

#### SPF-Include-Aufblähung und das 10-Lookup-Limit {#spf-include-bloat-and-the-10-lookup-limit}

Die SPF-Spezifikation (RFC 7208) begrenzt empfangende Mailserver auf maximal 10 DNS-Lookups bei der Validierung eines SPF-Eintrags.

- Wenn eine übergeordnete Domain die ESP-Mechanismen von Braze hinzufügt (`include:sparkpostmail.com` oder `include:amazonses.com`), zählt dies stark gegen dieses Limit.
- Wenn das Limit überschritten wird, löst dies einen permanenten SPF-PermError aus, wodurch alle Unternehmens-E-Mails die Authentifizierung nicht bestehen.

#### IP- und Domain-Reputationsisolierung {#ip-and-domain-reputation-isolation}

Wenn Marketing-Kampagnen, transaktionale Belege und interne Mitarbeiter-E-Mails denselben Root-Domain-Bereich teilen, kann ein plötzlicher Anstieg von Marketing-Spam-Beschwerden die Reputation der übergeordneten Domain beschädigen. Dies riskiert, dass kritische Unternehmenskommunikation in Spam-Ordner geleitet wird. Die Verwendung einer separaten Subdomain isoliert die Reputation Ihres Marketing-Outreach.

## Implementierungs-Workflow {#implementation-workflow}

Um eine reibungslose Übergabe und Implementierung sicherzustellen, folgen Sie dieser Reihenfolge:

1. Stellen Sie die strukturierten Einträge Ihren IT- oder Netzwerkadministrator:innen zur Verfügung, damit diese sie zu Ihrer Hosting-Plattform hinzufügen können (Cloudflare, Route 53 usw.).
2. Setzen Sie einen niedrigen Time-To-Live-Wert (TTL) (zum Beispiel 300 Sekunden oder fünf Minuten) für erste Tests. Dies ermöglicht eine schnelle Wiederherstellung, falls bei der Eingabe ein Tippfehler gemacht wird.
3. Führen Sie einen DNS-Lookup durch (zum Beispiel `dig CNAME mail.example.com`) oder verwenden Sie ein Validierungstool, um zu bestätigen, dass die Einträge korrekt aufgelöst werden, bevor Sie zur Aufwärmphase übergehen.

## DNS-Anbieter-Dokumentation {#dns-provider-documentation}

Jeder DNS-Anbieter hat eine eigene Schnittstelle. Teilen Sie diese Spezifikationen mit Ihren Netzwerkadministrator:innen oder lesen Sie die Dokumentation Ihres spezifischen Anbieters, um Einträge korrekt in Ihre Zonendatei einzutragen.

Die folgende Tabelle listet die offizielle Dokumentation für häufig verwendete DNS-Anbieter auf.

| DNS-Anbieter | Ressourcen |
| --- | --- |
| Cloudflare | [Manage DNS records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) |
| Amazon Route 53 | [Creating resource record sets](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html) |
| GoDaddy | [Manage DNS records](https://www.godaddy.com/help/manage-dns-records-680) |
| Google Cloud DNS | [Set up DNS records for a domain name](https://cloud.google.com/dns/docs/set-up-dns-records-domain-name) |
| Microsoft Azure DNS | [Manage DNS records using the Azure portal](https://learn.microsoft.com/en-us/azure/dns/dns-operations-recordsets-portal) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="DNS-Anbieter-Dokumentation" }

Weitere Ressourcen zu Domain-Anbietern finden Sie unter [IPs und Domains einrichten]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains#step-3-add-dns-records).