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

# E-Mail-Reporting

> Dieser Artikel behandelt die verschiedenen Komponenten Ihres E-Mail-Reportings und wo diese im Dashboard zu finden sind.

{% multi_lang_include analytics/campaign_analytics.md channel="email" %}

## Fehlerbehebung

### E-Mail-Bounces

- **554 5.7.1 [internal] recipient address was suppressed due to customer policy:** Versuchen Sie eine andere Adresse, reaktivieren Sie den Kontakt über einen anderen Kanal oder entfernen Sie die Adresse nur für Ihre eigenen Testadressen von der Unterdrückungsliste. Vermeiden Sie es, echte Nutzer:innen-Unterdrückungen aufzuheben, da dies Ihrer Reputation schaden kann.
- **Mailbox full / invalid account:** Häufig ein Signal für die Listenqualität. Priorisieren Sie Nutzer:innen, die kürzlich eine E-Mail geöffnet oder angeklickt haben (z. B. in den letzten 30–60 Tagen), während Sie inaktive oder fehlerhafte Adressen bereinigen.

### Ungültige Domains

Fehler wie `unable to get mx info` bedeuten oft, dass viele Zieladressen fehlerhafte Domains verwenden (z. B. Tippfehler). Segmentieren, exportieren und korrigieren Sie diese Profile und importieren Sie sie anschließend erneut.

### Gedrosselte IPs

Wenn ein Empfänger-Server Ihre IP drosselt, reduzieren Sie das Sendevolumen an diese Domain, verbessern Sie das Engagement und wenden Sie sich an den Zustellbarkeits-Support, falls die Drosselung anhält.