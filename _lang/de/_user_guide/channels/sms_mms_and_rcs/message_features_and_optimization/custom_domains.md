---
nav_title: Self-Service-Custom-Domains
article_title: Self-Service-Custom-Domains
page_order: 2
description: "Diese Seite beschreibt, wie Sie Custom Domains mit Link-Shortening verwenden, um das Erscheinungsbild Ihrer gekürzten URLs zu personalisieren."
page_type: reference
alias: "/custom_domains/"
tool:
  - Campaigns
channel:
  - SMS
---

# Self-Service-Custom-Domains {#self-serve-custom-domains}

> Diese Seite beschreibt, wie Sie Ihre eigenen Custom Domains im Braze-Dashboard einrichten. Custom Domains ermöglichen es Ihnen, einen gebrandeten gekürzten Link zu verwenden, der die Identität Ihrer Marke widerspiegelt, anstatt eines generischen gekürzten Links oder der Braze-Domain (`brz.ai`) – das verbessert das Vertrauen der Nutzer:innen und das Campaign-Engagement bei SMS-Links.

Self-Service-Custom-Domains ermöglichen es Ihnen, Ihre eigenen Custom Domains für SMS, RCS und WhatsApp direkt über Ihr Braze-Dashboard zu konfigurieren und zu verwalten. Sie können ganz einfach bis zu 10 Custom Domains an einem Ort hinzufügen, überwachen und verwalten.

## Vorteile von Self-Service-Custom-Domains {#benefits-of-self-serve-custom-domains}

- **Vereinfachte Einrichtung:** Konfigurieren Sie Ihre Domains auf der Seite **Unternehmenseinstellungen**, um die Einrichtungszeit zu verkürzen.
- **Verbesserte Transparenz:** Erhalten Sie Realtime-Updates zum Einrichtungsstatus Ihrer Domain über Banner im Dashboard.
- **Proaktive Benachrichtigungen:** Erhalten Sie sofortige Warnungen, wenn Ihre Custom Domain verbunden ist oder wenn Konfigurationsfehler auftreten.

## Domain-Anforderungen {#domain-requirements}

- Domains müssen von Ihnen beschafft, besessen und verwaltet werden. Dies kann über einen Domain-Registrar wie GoDaddy, Amazon Route 53 oder Google Domains erfolgen.
- Die für dieses Feature verwendete Domain muss:
  - Eindeutig sein (anders als Ihre Website-Domain)
  - Darf nicht zum Hosten von Webinhalten verwendet werden
    - Sie können auch eindeutige Subdomains verwenden. Zum Beispiel könnte die Domain `braze.com` Subdomains wie `sms.braze.com` oder `whatsapp.braze.com` haben.

## Delegierung Ihrer Custom Domain {#delegating-your-custom-domain}

Wir verlangen, dass Sie Ihre Custom Domain an Braze delegieren, damit wir ein ordnungsgemäßes Routing und die Infrastrukturkompatibilität mit unseren Link-Shortening- und Klick-Tracking-Diensten sicherstellen können. Wenn Sie Ihre Domain an Braze delegieren, übernehmen wir automatisch die Zertifikatserneuerung, um eine Unterbrechung des Dienstes zu verhindern.

## Hinzufügen einer Custom Domain {#adding-a-custom-domain}

1. Gehen Sie in Braze zu **Unternehmenseinstellungen** > **SMS/RCS and Messaging Apps Domains**.
![Seite „SMS/RCS and Messaging Apps Domains“ mit mehreren aufgelisteten Domains.]({% image_buster /assets/img/main_page.png %})

{: start="2"}
2. Wählen Sie **Add Domain** aus, um eine neue Custom-Domain-Einrichtung zu starten.
3. Geben Sie die von Ihnen erworbene Custom Domain in unser In-App-Eingabefeld ein, das unsere bestehende Validierungslogik für die korrekte Formatierung verwendet, und wählen Sie dann **Next** und **Submit** aus.

![Button „Add Domain“ auf der Seite „SMS/RCS and Messaging Apps Domains“.]({% image_buster /assets/img/custom_domain_button.png %}){: style="max-width:70%;"}

{: start="4"}
4. Lassen Sie Ihr technisches Team (z. B. Engineering oder IT) Ihre DNS-Konfiguration mit den angezeigten Cloudflare-DNS-Eintragsdetails aktualisieren. Ihr technisches Team muss Ihre DNS-Einträge mit diesen Details innerhalb von 45 Tagen aktualisieren.
  - Wenn Sie zusätzliche Zeit für die Aktualisierung Ihrer DNS-Einträge benötigen, können Sie den Prozess neu starten und einen neuen Satz von DNS-Einträgen für Ihre Domain generieren.

Braze überprüft Ihre DNS-Konfiguration ungefähr alle 30 Minuten auf Aktualisierungen.

![Abschnitt „DNS record“ mit 3 Schritten, die zum Abschluss der Domain-Einrichtung erforderlich sind.]({% image_buster /assets/img/dns_record.png %})

{% alert note %}
Ihr Domain-Fortschritt wird automatisch gespeichert. Wenn Sie den Vorgang zwischendurch verlassen müssen, können Sie später fortfahren, indem Sie den ausstehenden Domain-Eintrag auf der Seite **SMS/RCS and Messaging Apps Domains** auswählen.
{% endalert %}

### Laufende Verwaltung und Nutzung {#ongoing-management-and-usage}

Nachdem Ihre Domain verifiziert wurde, erscheinen Ihre Custom Domains in der Tabelle auf der Seite **SMS/RCS and Messaging Apps Domains** mit Statusanzeigen. Sie können verbundene Domains sofort über mehrere Abo-Gruppen, Workspaces und über SMS-, RCS- und WhatsApp-Kanäle hinweg verwenden.

![Liste von Custom Domains und Status.]({% image_buster /assets/img/custom_domain_statuses.png %}){: style="max-width:60%;"}

Live-Monitoring warnt Sie im Braze-Dashboard, wenn eine Ihrer aktiven Domains ein Problem hat, damit Ihre angepassten Links nutzbar bleiben. Wenn Sie auf Probleme stoßen, lesen Sie die In-App-Fehlerdetails oder kontaktieren Sie den Braze-[Support]({{site.baseurl}}/braze_support/) für Unterstützung.

## Zuweisen von Custom Domains zu Abo-Gruppen {#assigning-custom-domains-to-subscription-groups}

Nach der Konfiguration können Custom Domains einer oder mehreren SMS-, RCS- und WhatsApp-Abo-Gruppen zugewiesen werden.

1. Gehen Sie zu **Zielgruppe** > **Abo-Gruppen-Verwaltung**.
2. Suchen und wählen Sie Ihre Abo-Gruppe in der Liste aus.
3. Wählen Sie unter **Details zur Abo-Gruppe** Ihre Custom Domain im Dropdown **Link Shortening Domain** aus.

Campaigns, die mit aktiviertem Link-Shortening gesendet werden, verwenden die zugewiesene Domain, die mit Ihrer SMS-, RCS- oder WhatsApp-Abo-Gruppe verknüpft ist.

![Vorschau des SMS-Nachrichten-Editors mit einer gekürzten Link-Domain, die sich von der Domain im Feld „Message“ unterscheidet.]({% image_buster /assets/img/custom_domain2.png %})

## Häufig gestellte Fragen {#frequently-asked-questions}

### Können delegierte Domains über mehrere Abo-Gruppen hinweg geteilt werden? {#can-delegated-domains-be-shared-across-multiple-subscription-groups}

Ja. Eine einzelne Domain kann mit mehreren Abo-Gruppen verwendet werden. Wählen Sie dazu die Domain für jede Abo-Gruppe aus, mit der sie verknüpft werden soll.

### Können delegierte Domains über mehrere Workspaces hinweg geteilt werden? {#can-delegated-domains-be-shared-across-multiple-workspaces}

Ja. Domains können mit Abo-Gruppen in mehreren Workspaces verknüpft werden, vorausgesetzt, die Workspaces befinden sich innerhalb desselben Unternehmens.

### Wie viele Custom Domains kann ich hinzufügen? {#how-many-custom-domains-can-i-add}

Sie können bis zu 10 Custom Domains pro Dashboard hinzufügen.

### Was passiert, wenn ich meine DNS-Einträge nicht innerhalb von 45 Tagen aktualisiere? {#what-happens-if-i-dont-update-my-dns-records-within-45-days}

Obwohl Ihre Cloudflare-DNS-Eintragsdetails nach 45 Tagen ablaufen, können Sie den Einrichtungsprozess mit derselben Domain neu starten, und Braze generiert einen neuen Satz von DNS-Einträgen, um Ihr Einrichtungsfenster zu verlängern.

### Werde ich benachrichtigt, wenn während des DNS-Update-Prozesses ein Fehler auftritt? {#will-i-be-notified-if-there-is-an-error-during-the-dns-update-process}

Ja. Wenn ein Fehler auftritt, erhalten Sie ein Banner im Braze-Dashboard mit Details zum Problem sowie Schritten zur Behebung.

### Kann ich eine Custom Domain über mehrere Kanäle hinweg verwenden? {#can-i-use-a-custom-domain-across-multiple-channels}

Ja. Nachdem eine Custom Domain verifiziert wurde, kann sie in allen SMS-, RCS- und WhatsApp-Abo-Gruppen über alle Workspaces innerhalb eines Dashboards verwendet werden.

### Was ist, wenn ich Fragen habe oder weiteren Support benötige? {#what-if-i-have-questions-or-need-further-support}

Für detailliertere Anleitungen zur Einrichtung und Verwaltung von Custom Domains, einschließlich Fehlerbehebungsschritten und technischen Anforderungen, [kontaktieren Sie den Support]({{site.baseurl}}/braze_support/).