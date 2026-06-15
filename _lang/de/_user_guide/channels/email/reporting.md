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

### E-Mail-Bounces {#bounced-emails}

- **554 5.7.1 [internal] recipient address was suppressed due to customer policy:** Versuchen Sie eine andere Adresse, reaktivieren Sie den Kontakt über einen anderen Kanal oder entfernen Sie die Adresse nur für Ihre eigenen Testadressen von der Unterdrückungsliste. Vermeiden Sie es, echte Nutzer:innen-Unterdrückungen aufzuheben, da dies Ihrer Reputation schaden kann.
- **Mailbox full / invalid account:** Häufig ein Signal für die Listenqualität. Priorisieren Sie Nutzer:innen, die kürzlich eine E-Mail geöffnet oder angeklickt haben (z. B. in den letzten 30–60 Tagen), während Sie inaktive oder fehlerhafte Adressen bereinigen.

### Ungültige Domains {#invalid-domains}

Fehler wie `unable to get mx info` bedeuten oft, dass viele Zieladressen fehlerhafte Domains verwenden (z. B. Tippfehler). Segmentieren, exportieren und korrigieren Sie diese Profile und importieren Sie sie anschließend erneut.

### Gedrosselte IPs {#throttled-ips}

Möglicherweise sehen Sie im [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/) die Meldung `Email was deferred due to the following reason(s): [IPs were throttled by recipient server]`, wenn ein E-Mail-Anbieter die Zustellung von Ihrer IP vorübergehend verlangsamt oder blockiert – aufgrund von Sendevolumen, Reputation oder beidem. Braze versucht verzögerte Nachrichten erneut zuzustellen. Wenn sich Verzögerungen häufen, sehen Sie häufig auch erhöhte Soft Bounces.

Dieses Muster bedeutet in der Regel, dass Sie schneller senden, als der E-Mail-Anbieter bei Ihrer aktuellen Reputation akzeptiert. Neben der Verbesserung von Engagement und Listenqualität können Sie [Rate-Limiting für die Zustellgeschwindigkeit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#delivery-speed-rate-limiting) nutzen, um zu begrenzen, wie schnell Nachrichten für eine Campaign oder ein Canvas Braze verlassen. Das hilft, Drosselungen zu reduzieren, während Sie mit Ihrem Zustellbarkeits-Team an langfristigen Lösungen arbeiten.

Wenn die Drosselung bei bestimmten Domains anhält, reduzieren Sie das Sendevolumen an diese Domains und wenden Sie sich an den Braze-Zustellbarkeits-Support für weitere Unterstützung.