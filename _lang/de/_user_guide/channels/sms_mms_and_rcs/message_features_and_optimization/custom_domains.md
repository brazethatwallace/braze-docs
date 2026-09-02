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

## Vorteile angepasster Self-Service-Domains {#benefits-of-self-serve-custom-domains}

- **Vereinfachte Einrichtung:** Konfigurieren Sie Ihre Domains auf der Seite **Company Settings**, um die Einrichtungszeit zu verkürzen.
- **Verbesserte Transparenz:** Erhalten Sie Realtime-Updates zum Einrichtungsstatus Ihrer Domain über Banner im Dashboard.
- **Proaktive Benachrichtigungen:** Erhalten Sie sofortige Benachrichtigungen, wenn Ihre angepasste Domain verbunden ist oder Konfigurationsfehler auftreten.

## Domain-Anforderungen {#domain-requirements}

- Domains müssen von Ihnen beschafft, besessen und verwaltet werden. Dies kann über einen Domain-Registrar wie GoDaddy, Amazon Route 53 oder Cloudflare erfolgen.
- Die für dieses Feature verwendete Domain muss:
  - Eindeutig sein (anders als Ihre Website-Domain)
  - Kann nicht zum Hosten von Webinhalten verwendet werden
    - Sie können auch eindeutige Subdomains verwenden. Zum Beispiel könnte die Domain `braze.com` Subdomains wie `sms.braze.com` oder `whatsapp.braze.com` haben.

## Delegieren Ihrer angepassten Domain {#delegating-your-custom-domain}

Wir benötigen, dass Sie Ihre angepasste Domain an Braze delegieren, damit wir ein ordnungsgemäßes Routing und die Infrastrukturkompatibilität mit unseren Diensten zur Linkverkürzung und zum Klick-Tracking sicherstellen können. Wenn Sie Ihre Domain an Braze delegieren, kümmern wir uns automatisch um die Zertifikatserneuerung, um eine Unterbrechung des Dienstes zu verhindern.

{% alert important %}
Wenn Ihre DNS-Einträge nicht innerhalb von 45 Tagen aktualisiert werden, läuft das Setup-Token / Textbaustein ab. Starten Sie die Domain-Einrichtung über **SMS/RCS and Messaging Apps Domains** neu, um neue DNS-Einträge zu generieren.
{% endalert %}

## Hinzufügen einer angepassten Domain {#adding-a-custom-domain}

1. Gehen Sie in Braze zu **Unternehmenseinstellungen** > **SMS/RCS und Messaging-Apps-Domains**.
![Seite „SMS/RCS und Messaging-Apps-Domains“ mit mehreren aufgelisteten Domains.]({% image_buster /assets/img/main_page.png %})

{: start="2"}
2. Wählen Sie **Add Domain** aus, um eine neue angepasste Domain einzurichten.
3. Geben Sie die von Ihnen erworbene angepasste Domain in das In-App-Eingabefeld ein, das unsere bestehende Validierungslogik für die korrekte Formatierung verwendet, und wählen Sie dann **Next** und **Submit** aus.

![Button „Add Domain“ auf der Seite „SMS/RCS und Messaging-Apps-Domains“.]({% image_buster /assets/img/custom_domain_button.png %}){: style="max-width:70%;"}

{: start="4"}
4. Lassen Sie Ihr technisches Team (z. B. Engineering oder IT) Ihre DNS-Konfiguration mit den angezeigten Cloudflare-DNS-Eintragsdetails aktualisieren. Ihr technisches Team muss Ihre DNS-Einträge innerhalb von 45 Tagen mit diesen Details aktualisieren.
  - Wenn Sie zusätzliche Zeit für die Aktualisierung Ihrer DNS-Einträge benötigen, können Sie den Prozess neu starten und einen neuen Satz von DNS-Einträgen für Ihre Domain generieren.

Braze prüft Ihre DNS-Konfiguration ungefähr alle 30 Minuten auf Aktualisierungen.

![Abschnitt „DNS record“ mit 3 Schritten, die zum Abschluss der Domain-Einrichtung erforderlich sind.]({% image_buster /assets/img/dns_record.png %})

{% alert note %}
Ihr Domain-Fortschritt wird automatisch gespeichert. Wenn Sie den Vorgang zwischendurch abbrechen müssen, können Sie ihn später fortsetzen, indem Sie den ausstehenden Domain-Eintrag auf der Seite **SMS/RCS und Messaging-Apps-Domains** auswählen.
{% endalert %}

### Laufende Verwaltung und Nutzung {#ongoing-management-and-usage}

Nachdem Ihre Domain verifiziert wurde, werden Ihre angepassten Domains in der Tabelle auf der Seite **SMS/RCS und Messaging-Apps-Domains** mit Statusanzeigen angezeigt. Sie können verbundene Domains sofort über mehrere Abo-Gruppen, Workspaces und über SMS-, RCS- und WhatsApp-Kanäle hinweg nutzen.

![Liste der angepassten Domains und ihrer Status.]({% image_buster /assets/img/custom_domain_statuses.png %}){: style="max-width:60%;"}

Das Live-Monitoring benachrichtigt Sie im Braze-Dashboard, wenn eine Ihrer aktiven Domains ein Problem aufweist, sodass Ihre angepassten Links weiterhin nutzbar bleiben. Falls Probleme auftreten, sehen Sie sich die In-App-Fehlerdetails an oder wenden Sie sich an den Braze-[Support]({{site.baseurl}}/user_guide/administer/personal/braze_support).

## Zuweisen angepasster Domains zu Abo-Gruppen {#assigning-custom-domains-to-subscription-groups}

Nach der Konfiguration können angepasste Domains einer oder mehreren SMS-, RCS- und WhatsApp-Abo-Gruppen zugewiesen werden.

1. Gehen Sie zu **Zielgruppe** > **Abo-Gruppenverwaltung**.
2. Suchen und wählen Sie Ihre Abo-Gruppe in der Liste aus.
3. Wählen Sie unter **Details zur Abo-Gruppe** Ihre angepasste Domain im Dropdown-Menü **Link Shortening Domain** aus.

Campaigns, die mit aktivierter Linkverkürzung gesendet werden, verwenden die zugewiesene Domain, die mit Ihrer SMS-, RCS- oder WhatsApp-Abo-Gruppe verknüpft ist.

![Vorschau des SMS-Nachrichten-Editors mit einer verkürzten Link-Domain, die sich von der Domain im „Nachricht“-Feld unterscheidet.]({% image_buster /assets/img/custom_domain2.png %})

## Häufig gestellte Fragen {#frequently-asked-questions}

### Können delegierte Domains über mehrere Abo-Gruppen hinweg geteilt werden? {#can-delegated-domains-be-shared-across-multiple-subscription-groups}

Ja. Eine einzelne Domain kann mit mehreren Abo-Gruppen verwendet werden. Wählen Sie dazu die Domain für jede Abo-Gruppe aus, der sie zugeordnet werden soll.

### Können delegierte Domains über mehrere Workspaces hinweg geteilt werden? {#can-delegated-domains-be-shared-across-multiple-workspaces}

Ja. Domains können mit Abo-Gruppen in mehreren Workspaces verknüpft werden, sofern die Workspaces zum selben Unternehmen gehören.

### Wie viele angepasste Domains kann ich hinzufügen? {#how-many-custom-domains-can-i-add}

Sie können bis zu 10 angepasste Domains pro Dashboard hinzufügen. Braze kann auf Anfrage ein höheres Limit für Ihr Unternehmen konfigurieren.

Domains mit dem Status **Pending** oder **Error** werden auf dieses Limit angerechnet. Löschen Sie diese oder beheben Sie den Fehler auf der Seite **SMS/RCS and Messaging Apps Domains**.

Sie können keine Domain löschen, die einer Abo-Gruppe als **Link Shortening Domain** zugewiesen ist. Weisen Sie die Domain zunächst bei jeder Abo-Gruppe neu zu und löschen Sie die Domain anschließend.

### Was passiert, wenn ich meine DNS-Einträge nicht innerhalb von 45 Tagen aktualisiere? {#what-happens-if-i-dont-update-my-dns-records-within-45-days}

Obwohl Ihre Cloudflare-DNS-Eintragsdetails nach 45 Tagen ablaufen, können Sie den Einrichtungsprozess mit derselben Domain neu starten. Braze generiert dann einen neuen Satz DNS-Einträge, um Ihr Einrichtungsfenster zu verlängern.

### Werde ich benachrichtigt, wenn während des DNS-Aktualisierungsprozesses ein Fehler auftritt? {#am-i-notified-if-there-is-an-error-during-the-dns-update-process}

Ja. Wenn ein Fehler auftritt, erhalten Sie im Braze-Dashboard ein Banner mit Details zum Problem sowie Schritten zur Behebung.

### Kann ich eine angepasste Domain über mehrere Kanäle hinweg verwenden? {#can-i-use-a-custom-domain-across-multiple-channels}

Ja. Nachdem eine angepasste Domain verifiziert wurde, kann sie in allen SMS-, RCS- und WhatsApp-Abo-Gruppen über alle Workspaces innerhalb eines Dashboards verwendet werden.

### Was ist, wenn ich Fragen habe oder weitere Unterstützung benötige? {#what-if-i-have-questions-or-need-further-support}

Für detailliertere Anleitungen zur Einrichtung und Verwaltung angepasster Domains, einschließlich Schritte zur Fehlerbehebung und technischer Anforderungen, [kontaktieren Sie den Support]({{site.baseurl}}/user_guide/administer/personal/braze_support).