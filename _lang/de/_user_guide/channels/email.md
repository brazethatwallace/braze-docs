---
nav_title: E-Mail
article_title: E-Mail
page_order: 3
page_type: landing
description: "Erstellen Sie angepasste und personalisierte E-Mail-Campaigns in Braze mit Drag-and-Drop- und HTML-Editoren, Abo-Management und mehr."
channel:
  - email
search_rank: 2
---

# E-Mail {#email}

> Mit E-Mail bei Braze können Sie vollständig angepasste und personalisierte E-Mail-Nachrichten in Campaigns oder Canvas erstellen, die die Aufmerksamkeit Ihrer Nutzer:innen außerhalb Ihrer App oder Website gewinnen. Passen Sie Ihre E-Mail-Nachrichten an – von der Verwaltung Ihrer Zielgruppe bis hin zu auffälligen Multimedia-Inhalten. Beispiele für E-Mail-Campaigns finden Sie in den Braze-[Fallstudien](https://www.braze.com/customers/).

## Voraussetzungen {#prerequisites}

Bevor Sie E-Mails mit Braze versenden können, müssen Sie Ihre dedizierten IPs, Domains, E-Mail-Authentifizierung und IP-Warming konfigurieren. Eine vollständige Anleitung finden Sie unter [E-Mail-Einrichtung]({{site.baseurl}}/user_guide/channels/email/email_setup).

## E-Mails anpassen {#customize-your-emails}

Sie können Ihr E-Mail-Messaging auf verschiedene Arten anpassen, darunter:

- [Braze E-Mail-Templates]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template)
- [Benutzerdefinierte HTML-Templates]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template)
- [Editor-Blöcke (E-Mail)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email)
- [Nutzer:innen-Abos]({{site.baseurl}}/user_guide/channels/email/subscriptions)

## Testen Sie Ihre E-Mails {#test-your-emails}

[Seed-Gruppen]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups) senden automatisch Kopien Ihrer E-Mail-Campaigns an interne Nutzer:innen, um eine Qualitätssicherung durchzuführen. Seed-E-Mails enthalten `[SEED]` am Anfang der Betreffzeile, damit Sie sie leicht identifizieren können.

## Anwendungsfälle {#use-cases}

| Anwendungsfall | Erklärung |
| --- | --- |
| Erneute Interaktion | Erreichen Sie Nutzer:innen außerhalb Ihrer App, einschließlich derjenigen, die die App nicht installiert haben. |
| Onboarding | Begrüßen Sie neue Nutzer:innen und ermutigen Sie sie, Push-Benachrichtigungen zu aktivieren oder die App in sozialen Netzwerken zu teilen. |
| Rich-Nachrichten | Ermöglichen Sie reichhaltige und dynamische HTML-Nachrichten. |
| Multimedia-Inhalte | Einfache Platzierung von Multimedia-Inhalten wie Videos und Bildern, die Nutzer:innen ansprechen. |
| Newsletter | Versenden Sie bequem monatliche oder wöchentliche Newsletter, um das Nutzer:innen-Engagement aufrechtzuerhalten. |
| Transaktionen | Benachrichtigen Sie Nutzer:innen über kürzlich getätigte Käufe und liefern Sie wichtige Produkt- und Versandinformationen mit [Transaktions-E-Mails]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email).
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anwendungsfälle" }

## E-Mail-Dienste {#email-services}

Wenn Sie zusätzliche Unterstützung für Ihr E-Mail-Programm benötigen, bietet Braze wiederkehrende und einmalige Serviceleistungen gegen Aufpreis an. Kontaktieren Sie Ihren Braze Account Manager für weitere Informationen.

### E-Mail-Zustellbarkeitsdienste {#email-deliverability-services}

Braze bietet zwei Stufen des wiederkehrenden E-Mail-Supports:
1. Deluxe
2. Standard

Diese Dienste können Folgendes umfassen:

- Prüfung historischer und aktueller E-Mail-Versandpraktiken mit einer Überprüfung von Targeting-, Kadenz- und Messaging-Strategien
- Allowlist-Konfiguration und individueller IP-Warming-Plan, erstellt von einem Zustellbarkeitsexperten
  - Regelmäßige Check-in-Anrufe während Ihres ersten Monats (dreimal pro Woche für Deluxe und einmal pro Woche für Standard)
- Regelmäßige Anrufe mit einem Zustellbarkeitsexperten (zweimal pro Monat für Deluxe und monatlich für Standard) mit folgenden Inhalten:
  - Überwachung der Zustellbarkeits-Performance nach Domain
  - Empfehlungen zur Verbesserung der E-Mail-Programm-Performance und der Ergebnisse unter Nutzung von Daten und bewährten Best Practices
- Mitigieren und Beheben von Krisensituationen bei Ereignissen, die zu Problemen wie einer Blocklist für die Zustellbarkeit führen

## Nächste Schritte {#next-steps}

- [E-Mail-Einrichtung]({{site.baseurl}}/user_guide/channels/email/email_setup)
- [Eine E-Mail mit dem Drag-and-Drop-Editor erstellen]({{site.baseurl}}/user_guide/channels/email/drag_and_drop)
- [Eine E-Mail mit dem HTML-Editor erstellen]({{site.baseurl}}/user_guide/channels/email/html_editor)