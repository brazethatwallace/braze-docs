---
nav_title: Reporting
article_title: E-Mail-Reporting
page_order: 21
description: "Dieser Referenzartikel behandelt die verschiedenen Komponenten des E-Mail-Reportings und wo diese im Dashboard zu finden sind."
tool:
  - Reports
channel:
  - email

---

# E-Mail-Reporting {#email-reporting}

> Dieser Artikel behandelt die verschiedenen Komponenten Ihres E-Mail-Reportings und wo diese im Dashboard zu finden sind.

{% multi_lang_include analytics/campaign_analytics.md channel="email" %}

## Fehlerbehebung {#troubleshooting}

### Zurückgewiesene E-Mails (Bounces) {#bounced-emails}

- **554 5.7.1 [internal] recipient address was suppressed due to customer policy:** Versuchen Sie eine andere Adresse, kontaktieren Sie die Person über einen anderen Kanal oder entfernen Sie die Adresse nur für Ihre eigenen Testadressen von der Unterdrückungsliste. Vermeiden Sie es, Unterdrückungen echter Nutzer:innen aufzuheben, da dies Ihrer Reputation schaden kann.
- **Mailbox full / invalid account:** Häufig ein Signal für die Listenqualität. Priorisieren Sie Nutzer:innen, die kürzlich geöffnet oder geklickt haben (z. B. in den letzten 30–60 Tagen), während Sie inaktive oder ungültige Adressen bereinigen.

#### Soft-Bounce-Wiederholungsverhalten {#soft-bounce-retry-behavior}

Wenn eine E-Mail aufgrund vorübergehender Probleme (z. B. volles Postfach, Server vorübergehend nicht erreichbar oder andere temporäre Zustellbarkeitsfehler) einen Soft Bounce verursacht, wiederholt Braze die Zustellung automatisch bis zu 72 Stunden lang. Die Anzahl der Wiederholungsversuche variiert je nach Empfängerserver.

Wenn die E-Mail nach dem Wiederholungszeitraum nicht erfolgreich zugestellt wird, protokolliert Braze ein einzelnes Soft-Bounce-Ereignis für diesen Campaign-Versand. Diese Soft Bounces erscheinen nicht in den Campaign-Analytics, aber Sie können:
- Sie im [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) überwachen, um Bounce-Gründe einzusehen
- Den [Segmentfilter „Soft Bounced“]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#soft-bounced) verwenden, um diese Nutzer:innen von zukünftigen Sendungen auszuschließen

Aufgrund dieses Wiederholungszeitraums ergeben die E-Mail-Zustellungsmetriken (Zustellungen, Bounces und Spam-Rate) bei Campaigns, bei denen Soft-Bounce-E-Mails letztlich nicht zugestellt werden, möglicherweise nicht 100 %.

Weitere Informationen zu Soft Bounces finden Sie im [E-Mail-Analytics-Glossar]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary#soft-bounce).

### Ungültige Domains {#invalid-domains}

Fehler wie `unable to get mx info` bedeuten häufig, dass viele Empfänger:innen ungültige Domains verwenden (z. B. Tippfehler). Segmentieren, exportieren und korrigieren Sie diese Profile und importieren Sie sie erneut.

### Gedrosselte IPs {#throttled-ips}

Möglicherweise sehen Sie die Meldung `Email was deferred due to the following reason(s): [IPs were throttled by recipient server]` im [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), wenn ein Postfachanbieter die Zustellung von Ihrer IP vorübergehend verlangsamt oder blockiert – aufgrund von Volumen, Reputation oder beidem. Braze wiederholt verzögerte Nachrichten; wenn sich Verzögerungen häufen, sehen Sie häufig auch erhöhte Soft Bounces.

Dieses Muster bedeutet in der Regel, dass Sie schneller senden, als der Postfachanbieter bei Ihrer aktuellen Reputation akzeptiert. Neben der Verbesserung von Engagement und Listenqualität können Sie [Rate-Limiting für die Zustellgeschwindigkeit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) verwenden, um zu begrenzen, wie schnell Nachrichten Braze für eine Campaign oder ein Canvas verlassen. Das hilft, Drosselungen zu reduzieren, während Sie mit Ihrem Zustellbarkeitsteam an langfristigen Lösungen arbeiten.

Wenn die Drosselung bei bestimmten Domains anhält, reduzieren Sie das Volumen für diese Domains und wenden Sie sich an den Braze-Zustellbarkeitssupport.

### Unbekannter IP-Reputationsstatus {#unknown-ip-reputation-status}

Wenn Ihr E-Mail-Performance-Bericht einen „unbekannten“ Wert für die IP-Reputation anzeigt, kann dies mit einem Ausfall der Google Postmaster Tools zusammenhängen. Google Postmaster Tools liefert Reputationsdaten für die Gmail-Zustellbarkeit, und vorübergehende Dienstunterbrechungen können zu fehlenden oder unbekannten Reputationswerten führen.

Wenn Sie einen unbekannten Reputationsstatus sehen und Fragen zu Ihrer E-Mail-Zustellbarkeit haben, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/support_contact).