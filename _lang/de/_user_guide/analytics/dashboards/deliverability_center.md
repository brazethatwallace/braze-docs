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

## Google-Postmaster-Konto einrichten {#set-up-your-google-postmaster-account}

Bevor Sie eine Verbindung zum Deliverability Center herstellen, müssen Sie ein Google-Postmaster-Tools-Konto einrichten. Sie können ein geschäftliches oder persönliches Gmail-Konto verwenden, um Google Postmaster einzurichten.

1. Rufen Sie das [Google-Postmaster-Tools-Dashboard](https://postmaster.google.com/managedomains?pli=1) auf.
2. Wählen Sie unten auf der Seite <i class="fas fa-plus-circle"></i> **Domain hinzufügen** aus.
3. Geben Sie Ihre Root-(übergeordnete) Domain ein, um Ihre E-Mail zu authentifizieren. Stellen Sie sicher, dass der TXT-Eintrag mit dieser Root-(übergeordneten) Domain verknüpft ist und **nicht** mit der Subdomain, die Sie über Braze verwenden. Durch die Verifizierung der Root-(übergeordneten) Domain können Sie später Subdomains in Postmaster Tools hinzufügen, ohne zusätzliche TXT-Einträge erstellen zu müssen. Wenn Sie beispielsweise `braze.com` verifizieren, können Sie später `demo.braze.com` als separate Subdomain in Postmaster Tools hinzufügen, um Metriken auf Subdomain-Ebene einzusehen.
4. Google generiert einen TXT-Eintrag, der direkt zum DNS Ihrer Domain hinzugefügt werden kann. Dieser wird in der Regel von der Person verwaltet, die für Ihr DNS zuständig ist. Informationen und Anleitungen zur Aktualisierung Ihres spezifischen DNS finden Sie unter [Domain verifizieren (hostspezifische Schritte)](https://support.google.com/a/topic/1409901).
5. Wählen Sie **Weiter** aus. <br>![Eine Beispiel-Domain „demo.braze.com“ zur Authentifizierung einer E-Mail.]({% image_buster /assets/img_archive/domain_authentication.png %})
6. Nachdem der TXT-Eintrag zum DNS hinzugefügt wurde, kehren Sie zum Google-Postmaster-Tools-Dashboard zurück und wählen Sie **Verifizieren** aus. Dieser Schritt bestätigt, dass Sie die Domain besitzen, sodass Sie in Ihrem Postmaster-Konto auf Gmail-Zustellbarkeitsmetriken zugreifen können. <br>![Eine Aufforderung zur Verifizierung des Eigentums an der Domain „demo.braze.com“.]({% image_buster /assets/img_archive/domain_verification.png %})
7. Nachdem Sie die Root-(übergeordnete) Domain verifiziert haben, fügen Sie Ihre Sende-Subdomains zu Google Postmaster hinzu.

{% alert note %}
Wenn Ihre Subdomains nicht im Deliverability Center für Google Postmaster enthalten sind, kann dies daran liegen, dass nur die Root-(übergeordnete) Domain zu Google Postmaster hinzugefügt wurde. Nachdem die Root-Domains in Google Postmaster verifiziert wurden, können Sie Ihre Subdomains hinzufügen, die automatisch verifiziert werden. Dieser Vorgang ermöglicht es Google, Metriken auf Subdomain-Ebene zurückzumelden, die dann in das Braze Deliverability Center übernommen werden können.
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

#### IP-Reputation {#ip-reputation}

Die folgende Tabelle hilft Ihnen, die Bewertungen der IP-Reputation zu verstehen:

| Reputationsbewertung | Definition |
| ----- | ---------- |
| Hoch | Hat eine gute Erfolgsbilanz bei der Generierung niedriger Spam-Beschwerden (z. B. wenn Nutzer:innen den „Spam“-Button klicken). |
| Mittel/Ausreichend | Bekannt für positives Engagement, erhält aber gelegentlich Spam-Beschwerden. Die meisten E-Mails von dieser Domain werden in den Posteingang zugestellt, außer wenn Spam-Beschwerden zunehmen. |
| Niedrig | Bekannt dafür, regelmäßig erhöhte Raten von Spam-Beschwerden zu erhalten. E-Mails von diesem Sender werden wahrscheinlich in den Spam-Ordner gefiltert. |
| Schlecht | Hat eine Vorgeschichte mit erhöhten Raten von Spam-Beschwerden. E-Mails von dieser Domain werden fast immer bei der Verbindung abgelehnt oder in den Spam-Ordner gefiltert. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="IP-Reputation" }

{% alert important %}
Die in Braze angezeigten Spam-Beschwerdedaten basieren auf Feedback-Loop-Berichten (FBL) von E-Mail-Anbietern, die diese teilen, wie z. B. Microsoft, Yahoo und Comcast. Wenn Nutzer:innen bei diesen Anbietern E-Mails als Spam melden, werden diese Beschwerden an Braze zurückgesendet.<br><br>
Gmail und iCloud betreiben jedoch keine herkömmlichen Feedback-Loops und melden Spam-Beschwerden nicht an Braze zurück. Das bedeutet:<br>
- Spam-Beschwerden von Gmail-Nutzer:innen sind nicht in den Braze-Metriken enthalten und stehen auch nicht in Snowflake- oder Currents-Daten zur Verfügung.<br>
- Sie können Gmail-Spam-Daten nur als aggregierte Prozentsätze in den [Gmail Postmaster Tools](https://www.gmail.com/postmaster/) einsehen, nicht als einzelne Adressen.<br>
- Wenn Sie hohe Spam-Raten in den Gmail Postmaster Tools sehen, stimmen diese Zahlen nicht mit Ihren Braze-Spam-Beschwerdemetriken überein, da Gmail diese Daten nicht mit Absendern teilt.
{% endalert %}

#### Domain-Reputation {#domain-reputation}

Verwenden Sie die folgende Tabelle, um Ihre Domain-Reputationsbewertungen zu überwachen und zu verstehen, damit Sie vermeiden, in den Spam-Ordner gefiltert zu werden.

| Reputationsbewertung | Definition |
| ----- | ---------- |
| Hoch | Hat eine gute Erfolgsbilanz mit sehr niedrigen Spam-Beschwerden. Entspricht den Absenderrichtlinien von Gmail. E-Mails werden selten in den Spam-Ordner gefiltert. Hat eine gute Erfolgsbilanz mit einer sehr niedrigen Spam-Rate. Entspricht den [Absenderrichtlinien von Gmail](https://developers.google.com/gmail/markup/registering-with-google). |
| Mittel/Ausreichend | Bekannt für positives Engagement, hat aber gelegentlich ein geringes Volumen an Spam-Beschwerden erhalten. Die meisten E-Mails von dieser Domain erreichen den Posteingang (außer bei einem deutlichen Anstieg des Spam-Niveaus). |
| Niedrig | Bekannt dafür, regelmäßig Spam-Beschwerden zu erhalten. E-Mails von diesem Sender werden wahrscheinlich in den Spam-Ordner gefiltert. |
| Schlecht | Hat eine Vorgeschichte mit erhöhten Raten von Spam-Beschwerden. E-Mails von dieser Domain werden fast immer bei der Verbindung abgelehnt oder in den Spam-Ordner gefiltert. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Domain-Reputation" }

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

Weitere Ideen zur Verbesserung der Zustellbarkeit finden Sie unter [Zustellbarkeitsfallen und Spam-Traps]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps). Lesen Sie auch unsere [Best Practices für E-Mails]({{site.baseurl}}/user_guide/channels/email/best_practices), um zu erfahren, was Sie vor dem Versand einer E-Mail-Kampagne überprüfen sollten.

## Microsoft Smart Network Data Services (SNDS) einrichten {#set-up-microsoft-smart-network-data-services-snds}

Wenn Microsoft Ihr wichtigster Postfachanbieter ist, können Sie Microsoft-SNDS-Daten im Deliverability Center einsehen. Dies umfasst dedizierte Sende-IPs für Workspaces, die Amazon SES, SendGrid oder SparkPost verwenden. Nutzen Sie diese Daten, um den Zustand Ihrer IPs zu überwachen und zu verstehen, wie Microsoft-Postfachanbieter Ihren Versand bewerten.

Microsoft SNDS liefert IP-bezogene Daten zu Spam-Beschwerden, Spam-Trap-Treffern und Sendevolumen, wie sie von Microsoft-Postfachanbietern wie Outlook, Hotmail und Live gemeldet werden.

{% alert important %}
Wenn Ihre Daten nicht im Deliverability Center angezeigt werden, wenden Sie sich mit einer Liste Ihrer IP-Adressen an den [Support]({{site.baseurl}}/user_guide/administer/personal/braze_support).
{% endalert %}

### Amazon SES

Für Workspaces, die E-Mails über Amazon SES versenden, zeigt das Deliverability Center Microsoft-SNDS-Metriken für Ihre dedizierten Sende-IPs an. Braze füllt bis zu 90 Tage historischer SNDS-Daten nach, wenn dieses Feature für Ihren Workspace aktiviert wird.

{% alert note %}
Amazon SES stellt keine Metriken für **Trap-Nachrichtenzeitraum – Start** oder **Trap-Nachrichtenzeitraum – Ende** bereit. Für SES-Sende-IPs sind diese Spalten in der Microsoft-SNDS-Tabelle ausgeblendet. Sie können dennoch andere SNDS-Metriken für diese IPs einsehen, einschließlich Spam-Trap-Treffer.
{% endalert %}

![Ein Beispiel für Ergebnisse von Microsoft SNDS, einschließlich Beispiel-IPs, Empfänger:innen, RCPT-Befehle, DATA-Befehle, Filterergebnis, Beschwerderate, Trap-Nachrichtenzeitraum – Start und Ende sowie Spam-Trap-Treffer.]({% image_buster /assets/img_archive/deliverability_center_msnds.png %})

### Metriken und Definitionen

Die folgenden Metriken gelten für Microsoft SNDS.

#### Empfänger:innen {#recipients}

Diese Metrik bezieht sich auf die Anzahl der Empfänger:innen von Nachrichten, die von der IP übermittelt wurden.

#### DATA-Befehle {#data-commands}

Diese Metrik erfasst die Anzahl der von der IP gesendeten DATA-Befehle. DATA-Befehle sind Teil des SMTP-Protokolls, das zum Versenden von E-Mails verwendet wird.

#### Filterergebnisse {#filter-results}

Entnehmen Sie dieser Tabelle die Bedeutung der Filterergebnisse:

| Ergebnis | Definition |
| ----- | ---------- |
| Grün | Wurde von Microsofts Spam-Filter in bis zu 10 % des angegebenen Zeitraums als Spam eingestuft. |
| Gelb | Wurde von Microsofts Spam-Filter in 10 % bis 90 % des angegebenen Zeitraums als Spam eingestuft. |
| Rot | Wurde von Microsofts Spam-Filter in mehr als 90 % des angegebenen Zeitraums als Spam eingestuft. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Filterergebnisse" }

#### Beschwerderate {#complaint-rate}

Dies ist der Anteil der Fälle, in denen eine von der IP empfangene Nachricht während des Aktivitätszeitraums von Hotmail- oder Windows-Live-Nutzer:innen als Spam gemeldet wird. Nutzer:innen haben die Möglichkeit, nahezu alle Nachrichten über die Web-Benutzeroberfläche als Junk zu melden.

Um die Beschwerderate zu berechnen, teilen Sie die Anzahl der Beschwerden durch die Anzahl der Nachrichtenempfänger:innen.

| Ergebnis | Definition |
| ----- | ---------- |
| Weniger als 0,3 % | Die ideale Beschwerderate. |
| Mehr als 0,3 % | Überprüfen Sie Ihren Registrierungsprozess und stellen Sie sicher, dass Ihr Abmeldelink funktioniert. Überlegen Sie außerdem, ob die E-Mail besser auf Ihre Zielgruppe personalisiert werden könnte. |
| Mehr als 100 % | Beachten Sie, dass SNDS Beschwerden für den Tag anzeigt, an dem sie gemeldet wurden, und nicht rückwirkend für den Tag, an dem die beanstandete E-Mail zugestellt wurde. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Beschwerderate" }

#### Spam-Trap-Treffer {#spam-trap-hits}

Spam-Trap-Treffer sind die Anzahl der Nachrichten, die an „Trap-Konten“ gesendet wurden. Dies sind Konten, die von Outlook.com betrieben werden und keinerlei E-Mails anfordern. Es ist wahrscheinlich, dass alle an diese Trap-Konten gesendeten Nachrichten als Spam eingestuft werden. Daher ist es wichtig, diese Metrik zu überwachen und sicherzustellen, dass sie niedrig bleibt. Niedrige Spam-Trap-Treffer bedeuten, dass die Nachrichten nicht an diese Konten gesendet werden, sondern an tatsächliche Konten zugestellt werden.

#### Trap-Nachrichtenzeitraum – Start und Ende {#trap-message-period-start-and-end}

Diese Spalten zeigen an, wann die erste und letzte Nachricht, die an Trap-Konten gesendet wurde, während des Aktivitätszeitraums von der IP empfangen wurde. Amazon SES stellt diese Metriken nicht bereit, daher sind die Spalten ausgeblendet, wenn Sie in der Microsoft-SNDS-Tabelle nur SES-Sende-IPs anzeigen.

{% alert tip %}
Wenn Sie nach Einträgen zu einer Ihrer verifizierten Domains in Braze suchen, beachten Sie, dass das Deliverability Center Ihre Daten von Google Postmaster oder Microsoft SNDS auflistet. Das bedeutet, dass eine der beiden Plattformen möglicherweise keine Daten hat, die sie mit Braze teilen kann. Alternativ können Sie versuchen, eine konsistente E-Mail-Zustellung aufrechtzuerhalten, da dies zu einer höheren Reputation führen kann.
{% endalert %}

## Spam-Beschwerden und Feedback-Loops {#spam-complaints-and-feedback-loops}

Ein E-Mail-Feedback-Loop (FBL) ermöglicht es E-Mail-Absendern, Berichte zu erhalten, wenn Empfänger:innen Nachrichten als Spam markieren. Gmail und iCloud bieten jedoch keine herkömmlichen Feedback-Loops an, was bedeutet, dass Braze (über SparkPost oder SendGrid) keine Spam-Beschwerdedaten von diesen Anbietern erhält.

Da Spam-Beschwerdedaten von Gmail und iCloud nicht verfügbar sind, ist es wichtig, andere Tools zu nutzen, um den Zustand und die Reputation Ihrer E-Mails bei diesen großen Anbietern zu überwachen:

- Verwenden Sie [Google Postmaster Tools](https://www.gmail.com/postmaster/), um die Domain- und IP-Reputation, Spam-Raten und das Nutzer:innen-Engagement zu überwachen. Sie können Google Postmaster wie unter [Google Postmaster integrieren](#integrating-google-postmaster) beschrieben in Braze integrieren.
- Apple bietet kein öffentliches Postmaster-Tool an, das dem von Google entspricht. Konzentrieren Sie sich darauf, starke Engagement-Metriken beizubehalten und E-Mail-Best-Practices zu befolgen.

Um eine gute Zustellbarkeit bei allen Anbietern aufrechtzuerhalten, implementieren Sie eine [Sunset-Richtlinie]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies), um den Versand an nicht engagierte Nutzer:innen automatisch zu stoppen. Dies hilft zu verhindern, dass Ihre E-Mails als Spam markiert werden, und schützt Ihre Absender-Reputation.