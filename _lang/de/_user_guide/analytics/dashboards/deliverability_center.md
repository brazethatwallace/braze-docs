---
nav_title: Deliverability Center
article_title: Deliverability Center
alias: "/deliverability_center/"
page_order: 4
description: "Dieser Referenzartikel beschreibt, wie Sie das Deliverability Center einrichten – ein Feature, mit dem Marketer die Reputation ihrer E-Mail-Versanddomains und IPs einsehen und ihre E-Mail-Zustellbarkeit besser verstehen können."
channel:
  - email

---

# Deliverability Center {#deliverability-center}

> Das Deliverability Center bietet Ihnen tiefere Einblicke in Ihre E-Mail-Performance, indem es die Nutzung der [Gmail Postmaster Tools](https://www.gmail.com/postmaster/) unterstützt, um Daten über versendete E-Mails zu verfolgen und Informationen über Ihre Versanddomain zu sammeln.

E-Mail-Zustellbarkeit ist der Kern des Kampagnenerfolgs. Mit dem Deliverability Center im Braze-Dashboard können Sie Ihre Domains nach **IP Reputation** oder **Delivery Errors** anzeigen, um potenzielle Probleme mit der E-Mail-Zustellbarkeit zu erkennen und zu beheben.

Um auf das Deliverability Center zuzugreifen, benötigen Sie die [Nutzer:innenberechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) im folgenden Dropdown für Ihren Workspace.

{% details Nutzer:innenberechtigungen für das Deliverability Center %}

- Campaigns anzeigen
- Campaigns bearbeiten
- Campaigns archivieren
- Canvases anzeigen
- Canvases bearbeiten
- Canvases archivieren
- Frequency-Capping-Regeln anzeigen
- Frequency-Capping-Regeln bearbeiten
- Nachrichtenpriorisierung anzeigen
- Nachrichtenpriorisierung bearbeiten
- Content Blocks anzeigen
- Feature-Flags anzeigen
- Feature-Flags bearbeiten
- Feature-Flags archivieren
- Segmente anzeigen
- Segmente bearbeiten
- IAM-Templates anzeigen
- IAM-Templates bearbeiten
- IAM-Templates archivieren
- E-Mail-Templates anzeigen
- E-Mail-Templates bearbeiten
- E-Mail-Templates archivieren
- Webhook-Templates anzeigen
- Webhook-Templates bearbeiten
- Webhook-Templates archivieren
- E-Mail-Link-Templates anzeigen
- E-Mail-Link-Templates bearbeiten
- Medienbibliothek-Assets anzeigen
- Medienbibliothek-Assets bearbeiten
- Medienbibliothek-Assets löschen
- Standorte anzeigen
- Standorte bearbeiten
- Standorte archivieren
- Aktionscodes anzeigen
- Aktionscodes bearbeiten
- Aktionscodes exportieren
- Präferenzzentren anzeigen
- Präferenzzentren bearbeiten
- Berichte anzeigen
- Berichte bearbeiten
- Nutzungsdaten anzeigen

{% enddetails %}

## Ihr Google Postmaster-Konto einrichten {#set-up-your-google-postmaster-account}

Bevor Sie sich mit dem Deliverability Center verbinden, müssen Sie ein Google Postmaster Tools-Konto einrichten. Sie können ein geschäftliches oder persönliches Gmail-Konto verwenden, um Google Postmaster einzurichten.

1. Gehen Sie zum [Google Postmaster Tools-Dashboard](https://postmaster.google.com/managedomains?pli=1).
2. Wählen Sie unten auf der Seite <i class="fas fa-plus-circle"></i> **Add domain**.
3. Geben Sie Ihre Root-(Eltern-)Domain ein, um Ihre E-Mail zu authentifizieren. Stellen Sie sicher, dass der TXT-Eintrag mit dieser Root-(Eltern-)Domain verknüpft ist, **nicht** mit der Subdomain, die Sie über Braze verwenden. Durch die Verifizierung der Root-(Eltern-)Domain können Sie später Subdomains in den Postmaster Tools hinzufügen, ohne zusätzliche TXT-Einträge erstellen zu müssen. Wenn Sie beispielsweise `braze.com` verifizieren, können Sie später `demo.braze.com` als separate Subdomain in den Postmaster Tools hinzufügen, um Metriken auf Subdomain-Ebene einzusehen.
4. Google generiert einen TXT-Eintrag, der direkt zum DNS Ihrer Domain hinzugefügt werden kann. Dies wird in der Regel von der Person verwaltet, die für Ihr DNS zuständig ist. Informationen und Anleitungen zur Aktualisierung Ihres spezifischen DNS finden Sie unter [Domain verifizieren (hostspezifische Schritte)](https://support.google.com/a/topic/1409901).
5. Wählen Sie **Next**. <br>![Eine Beispiel-Domain „demo.braze.com“ zur Authentifizierung einer E-Mail.]({% image_buster /assets/img_archive/domain_authentication.png %})
6. Nachdem der TXT-Eintrag zum DNS hinzugefügt wurde, kehren Sie zum Google Postmaster Tools-Dashboard zurück und wählen Sie **Verify**. Dieser Schritt bestätigt, dass Sie die Domain besitzen, sodass Sie in Ihrem Postmaster-Konto auf Gmail-Zustellbarkeitsmetriken zugreifen können. <br>![Eine Aufforderung zur Verifizierung des Eigentums an der Domain „demo.braze.com“.]({% image_buster /assets/img_archive/domain_verification.png %})
7. Fügen Sie nach der Verifizierung der Root-(Eltern-)Domain Ihre Versand-Subdomains zu Google Postmaster hinzu.

{% alert note %}
Wenn Ihre Subdomains nicht im Deliverability Center für Google Postmaster angezeigt werden, kann dies daran liegen, dass nur die Root-(Eltern-)Domain zu Google Postmaster hinzugefügt wurde. Nachdem die Root-Domains in Google Postmaster verifiziert wurden, können Sie Ihre Subdomains hinzufügen, die automatisch verifiziert werden. Dieser Prozess ermöglicht es Google, Metriken auf Subdomain-Ebene zurückzumelden, die dann in das Braze Deliverability Center übernommen werden können.
{% endalert %}

## Google Postmaster integrieren {#integrating-google-postmaster}

{% alert important %}
**Migration zu Google Postmaster Tools v2**<br>
Google stellt die alten Postmaster Tools (v1) ein und hat eine Version der nächsten Generation (v2) mit einer modernen Benutzeroberfläche und neuen Dashboards veröffentlicht, darunter ein Compliance-Dashboard zur Überwachung der Einhaltung der Gmail-Absenderrichtlinien. Alle Nutzer:innen müssen bis zum 31. Oktober 2026 auf v2 migrieren.<br><br>
Um Ihre Google Postmaster Tool-Verbindung erneut zu autorisieren, gehen Sie zu **Partnerintegrationen** > **Technologie-Partner**, öffnen Sie **Google Postmaster** und wählen Sie **Change Account**, um sich mit den neuen v2-Berechtigungen erneut zu authentifizieren. Danach sind Sie auf v2 aktualisiert und erhalten Zugriff auf neue Dashboards und Daten.<br><br>
Weitere Informationen finden Sie in [Googles Ankündigung zu den neuen Postmaster Tools](https://support.google.com/mail/answer/16594218?hl=en).
{% endalert %}

Bevor Sie Ihr Deliverability Center einrichten, stellen Sie sicher, dass Ihre Domains [zu den Gmail Postmaster Tools hinzugefügt](https://support.google.com/mail/answer/9981691?hl=en) wurden.

Folgen Sie diesen Schritten, um Google Postmaster zu integrieren und Ihr Deliverability Center einzurichten:

1. Gehen Sie zu **Analytics** > **Email Performance**.
2. Wählen Sie den Tab **Deliverability Center**. <br>![Ein Deliverability Center mit nicht verbundenem Google Postmaster.]({% image_buster /assets/img_archive/deliverability_center1.png %})
3. Wählen Sie **Connect with Google Postmaster**.
4. Wählen Sie Ihr Google-Konto aus und dann **Allow**, um Braze die Anzeige von E-Mail-Traffic-Metriken für die in den Postmaster Tools registrierten Domains zu erlauben.

Ihre verifizierten Domains werden im Deliverability Center angezeigt.

![Zwei verifizierte Domains für Google Postmaster mit mittlerer und niedriger Reputation.]({% image_buster /assets/img_archive/deliverability_center2.png %})

Sie können auch über das Braze-Dashboard auf Google Postmaster zugreifen, indem Sie zu **Partnerintegrationen** > **Technologie-Partner** > **Google Postmaster** navigieren. Nach der Integration ruft Braze Reputations- und Fehlerdaten der letzten 30 Tage ab. Die Daten sind möglicherweise nicht sofort verfügbar und es kann einige Minuten dauern, bis sie geladen sind.

### Ungültige oder abgelaufene Autorisierung {#invalid-or-expired-authorization}

Wenn Sie eine Warnung erhalten, dass die Zugangsdaten für die Google Postmaster Tools-Autorisierung ungültig sind, ist der E-Mail-Versand über Braze **nicht** betroffen. Nur die Verbindung zwischen Braze und Google Postmaster wird unterbrochen, wodurch Gmail-Reputations- und Fehlerdaten nicht mehr mit dem Deliverability Center synchronisiert werden, bis Sie die Verbindung wiederherstellen.

Um die Integration wiederherzustellen, gehen Sie zu **Partnerintegrationen** > **Technologie-Partner**, öffnen Sie **Google Postmaster**, wählen Sie **Disconnect** und durchlaufen Sie dann den Verbindungsprozess erneut (dieselben Schritte wie unter [Google Postmaster integrieren](#integrating-google-postmaster)).

### Metriken und Definitionen {#metrics-and-definitions}

Die folgenden Metriken und Definitionen gelten für Google Postmaster Tools.

#### IP Reputation {#ip-reputation}

Die folgende Tabelle hilft Ihnen, die Bewertungen der IP Reputation zu verstehen:

| Reputationsbewertung | Definition |
| ----- | ---------- |
| Hoch | Hat eine gute Erfolgsbilanz bei der Generierung niedriger Spam-Beschwerden (z. B. wenn Nutzer:innen den „Spam“-Button klicken). |
| Mittel/Ausreichend | Bekannt für positives Engagement, erhält aber gelegentlich Spam-Beschwerden. Die meisten E-Mails von dieser Domain werden in den Posteingang zugestellt, außer wenn Spam-Beschwerden zunehmen. |
| Niedrig | Bekannt dafür, regelmäßig erhöhte Raten von Spam-Beschwerden zu erhalten. E-Mails von diesem Sender werden wahrscheinlich in den Spam-Ordner gefiltert. |
| Schlecht | Hat eine Vorgeschichte mit erhöhten Raten von Spam-Beschwerden. E-Mails von dieser Domain werden fast immer bei der Verbindung abgelehnt oder in den Spam-Ordner gefiltert. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="IP Reputation" }

#### Domain Reputation {#domain-reputation}

Verwenden Sie die folgende Tabelle, um Ihre Domain-Reputationsbewertungen zu überwachen und zu verstehen, damit Sie vermeiden, in den Spam-Ordner gefiltert zu werden.

| Reputationsbewertung | Definition |
| ----- | ---------- |
| Hoch | Hat eine gute Erfolgsbilanz mit sehr niedrigen Spam-Beschwerden. Entspricht den Absenderrichtlinien von Gmail. E-Mails werden selten in den Spam-Ordner gefiltert. Hat eine gute Erfolgsbilanz mit einer sehr niedrigen Spam-Rate. Entspricht den [Absenderrichtlinien von Gmail](https://developers.google.com/gmail/markup/registering-with-google). |
| Mittel/Ausreichend | Bekannt für positives Engagement, hat aber gelegentlich ein geringes Volumen an Spam-Beschwerden erhalten. Die meisten E-Mails von dieser Domain erreichen den Posteingang (außer bei einem deutlichen Anstieg des Spam-Niveaus). |
| Niedrig | Bekannt dafür, regelmäßig Spam-Beschwerden zu erhalten. E-Mails von diesem Sender werden wahrscheinlich in den Spam-Ordner gefiltert. |
| Schlecht | Hat eine Vorgeschichte mit erhöhten Raten von Spam-Beschwerden. E-Mails von dieser Domain werden fast immer bei der Verbindung abgelehnt oder in den Spam-Ordner gefiltert. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Domain Reputation" }

#### Authentifizierung {#authentication}

Verwenden Sie das Authentifizierungs-Dashboard, um den Prozentsatz der E-Mails zu überprüfen, die das Sender Policy Framework (SPF), DomainKeys Identified Mail (DKIM) und Domain-based Message Authentication, Reporting and Conformance (DMARC) bestanden haben.

| Diagrammtyp | Definition |
| ----- | ---------- |
| SPF | Zeigt den Prozentsatz der E-Mails, die SPF bestanden haben, im Verhältnis zu allen E-Mails von der Domain, bei denen SPF geprüft wurde. Gefälschte E-Mails sind hiervon ausgeschlossen. |
| DKIM | Zeigt den Prozentsatz der E-Mails, die DKIM bestanden haben, im Verhältnis zu allen E-Mails von der Domain, bei denen DKIM geprüft wurde. |
| DMARC | Zeigt den Prozentsatz der E-Mails, die die DMARC-Ausrichtung bestanden haben, im Verhältnis zu allen E-Mails, die von der Domain empfangen wurden und entweder SPF oder DKIM bestanden haben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Authentifizierung" }

#### Verschlüsselung {#encryption}

In dieser Tabelle erfahren Sie, welcher Prozentsatz Ihres eingehenden und ausgehenden Traffics verschlüsselt ist.

| Begriff | Definition |
| ----- | ---------- |
| TLS eingehend | Zeigt den Prozentsatz der eingehenden E-Mails (an Gmail), die TLS bestanden haben, im Verhältnis zu allen von dieser Domain empfangenen E-Mails. |
| TLS ausgehend | Zeigt den Prozentsatz der ausgehenden E-Mails (von Gmail), die über TLS akzeptiert wurden, im Verhältnis zu allen an diese Domain gesendeten E-Mails. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Verschlüsselung" }

Weitere Ideen zur Verbesserung der Zustellbarkeit finden Sie unter [Zustellbarkeitsfallen und Spam-Traps]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps#deliverability-pitfalls-and-spam-traps). Lesen Sie auch unsere [Best Practices für E-Mails]({{site.baseurl}}/user_guide/channels/email/best_practices), um zu erfahren, was Sie vor dem Versand einer E-Mail-Campaign überprüfen sollten.

## Microsoft Smart Network Data Services (SNDS) einrichten {#set-up-microsoft-smart-network-data-services-snds}

Wenn Microsoft Ihr Haupt-Mailbox-Anbieter ist, können Sie Microsoft SNDS-Daten im Deliverability Center einsehen. Dies umfasst dedizierte Versand-IPs für Workspaces, die Amazon SES, SendGrid oder SparkPost verwenden. Nutzen Sie diese Daten, um den Zustand Ihrer IPs zu überwachen und zu verstehen, wie Microsoft-Posteingangsanbieter Ihren Versand bewerten.

Microsoft SNDS liefert Daten auf IP-Ebene zu Spam-Beschwerden, Spam-Trap-Treffern und Versandvolumen, wie sie von Microsoft-Posteingangsanbietern wie Outlook, Hotmail und Live gemeldet werden.

{% alert important %}
Wenn Sie Ihre Daten nicht im Deliverability Center sehen, kontaktieren Sie den [Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) mit einer Liste Ihrer IP-Adressen.
{% endalert %}

### Amazon SES

Für Workspaces, die E-Mails über Amazon SES versenden, zeigt das Deliverability Center Microsoft SNDS-Metriken für Ihre dedizierten Versand-IPs an. Braze füllt bis zu 90 Tage historischer SNDS-Daten nach, wenn dieses Feature für Ihren Workspace aktiviert wird.

{% alert note %}
Amazon SES stellt keine Metriken für **Trap-Nachrichtenzeitraum Start** oder **Trap-Nachrichtenzeitraum Ende** bereit. Für SES-Versand-IPs werden diese Spalten in der Microsoft SNDS-Tabelle ausgeblendet. Sie können weiterhin andere SNDS-Metriken für diese IPs einsehen, einschließlich Spam-Trap-Treffer.
{% endalert %}

![Ein Beispiel für Ergebnisse von Microsoft SNDS, einschließlich Beispiel-IPs, Empfänger:innen, RCPT-Befehle, DATA-Befehle, Filterergebnis, Beschwerderate, Trap-Nachrichtenzeitraum Start und Ende sowie Spam-Trap-Treffer.]({% image_buster /assets/img_archive/deliverability_center_msnds.png %})

### Metriken und Definitionen

Die folgenden Metriken gelten für Microsoft SNDS.

#### Empfänger:innen {#recipients}

Diese Metrik bezieht sich auf die Anzahl der Empfänger:innen von Nachrichten, die von der IP übermittelt wurden.

#### DATA-Befehle {#data-commands}

Diese Metrik erfasst die Anzahl der DATA-Befehle, die von der IP gesendet wurden. DATA-Befehle sind Teil des SMTP-Protokolls, das zum Versenden von E-Mails verwendet wird.

#### Filterergebnisse {#filter-results}

In der folgenden Tabelle erfahren Sie mehr über die Filterergebnisse:

| Ergebnis | Definition |
| ----- | ---------- |
| Grün | Wurde von Microsofts Spam-Filter in bis zu 10 % des angegebenen Zeitraums als Spam eingestuft. |
| Gelb | Wurde von Microsofts Spam-Filter in 10 % bis 90 % des angegebenen Zeitraums als Spam eingestuft. |
| Rot | Wurde von Microsofts Spam-Filter in mehr als 90 % des angegebenen Zeitraums als Spam eingestuft. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Filterergebnisse" }

#### Beschwerderate {#complaint-rate}

Dies ist der Anteil der Zeit, in der eine von der IP empfangene Nachricht von Hotmail- oder Windows Live-Nutzer:innen während des Aktivitätszeitraums als Spam gemeldet wird. Nutzer:innen haben die Möglichkeit, nahezu alle Nachrichten über die Web-Benutzeroberfläche als Junk zu melden.

Um die Beschwerderate zu berechnen, teilen Sie die Anzahl der Beschwerden durch die Anzahl der Nachrichtenempfänger:innen.

| Ergebnis | Definition |
| ----- | ---------- |
| Weniger als 0,3 % | Die ideale Beschwerderate. |
| Mehr als 0,3 % | Überprüfen Sie Ihren Registrierungsprozess und stellen Sie sicher, dass Ihr Abmeldelink funktioniert. Überlegen Sie auch, ob die E-Mail besser auf Ihre Zielgruppe personalisiert werden könnte. |
| Mehr als 100 % | Beachten Sie, dass SNDS Beschwerden für den Tag anzeigt, an dem sie gemeldet wurden, nicht rückwirkend für den Tag, an dem die beanstandete E-Mail zugestellt wurde. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Beschwerderate" }

#### Spam-Trap-Treffer {#spam-trap-hits}

Spam-Trap-Treffer sind die Anzahl der Nachrichten, die an „Trap-Konten“ gesendet wurden – Konten, die von Outlook.com betrieben werden und keine E-Mails anfordern. Es ist wahrscheinlich, dass alle an diese Trap-Konten gesendeten Nachrichten als Spam betrachtet werden. Daher ist es wichtig, diese Metrik zu überwachen und sicherzustellen, dass sie niedrig bleibt. Niedrige Spam-Trap-Treffer bedeuten, dass die Nachrichten nicht an diese Konten gesendet werden, sondern an tatsächliche Konten.

#### Trap-Nachrichtenzeitraum Start und Ende {#trap-message-period-start-and-end}

Diese Spalten zeigen an, wann die erste und letzte Nachricht, die an Trap-Konten gesendet wurde, während des Aktivitätszeitraums von der IP empfangen wurde. Amazon SES stellt diese Metriken nicht bereit, daher werden die Spalten ausgeblendet, wenn Sie nur SES-Versand-IPs in der Microsoft SNDS-Tabelle anzeigen.

{% alert tip %}
Wenn Sie nach Einträgen zu einer Ihrer verifizierten Domains in Braze suchen, beachten Sie, dass das Deliverability Center Ihre Daten von Google Postmaster oder Microsoft SNDS auflistet. Das bedeutet, dass eine der beiden Plattformen möglicherweise keine Daten hat, die sie mit Braze teilen kann. Alternativ können Sie versuchen, einen konsistenten E-Mail-Versand aufrechtzuerhalten, da dies zu einer höheren Reputation führen kann.
{% endalert %}