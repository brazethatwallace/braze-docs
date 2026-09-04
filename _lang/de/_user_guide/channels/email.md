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

> Mit E-Mail bei Braze erstellen Sie angepasste und personalisierte E-Mail-Nachrichten in Campaigns oder Canvases, die Nutzer:innen außerhalb Ihrer App oder Website erreichen. Dieser Hub behandelt die E-Mail-Einrichtung, Drag-and-Drop- und HTML-Editoren, Abo-Management, Templates und Tests, damit Sie konforme, markengerechte E-Mail-Programme starten können. Nutzen Sie Braze-E-Mail-Templates oder benutzerdefiniertes HTML, um Ihre Markenstimme und Ihr Layout umzusetzen. Beginnen Sie mit der [E-Mail-Einrichtung]({{site.baseurl}}/user_guide/channels/email/email_setup), wenn Sie eine neue Versanddomain konfigurieren. Beispiele für E-Mail-Campaigns finden Sie in den Braze-[Fallstudien](https://www.braze.com/customers/).

## Voraussetzungen {#prerequisites}

Bevor Sie E-Mails mit Braze versenden können, müssen Sie Ihre dedizierten IPs, Domains, E-Mail-Authentifizierung und IP-Warming konfigurieren. Eine vollständige Anleitung finden Sie unter [E-Mail-Einrichtung]({{site.baseurl}}/user_guide/channels/email/email_setup).

## E-Mails anpassen {#customize-your-emails}

Sie können Ihr E-Mail-Messaging auf verschiedene Arten anpassen, unter anderem mit:

- [Braze E-Mail-Templates]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template)
- [Angepasste HTML-Templates]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template)
- [Editor-Blöcke (E-Mail)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email)
- [Nutzer:innen-Abos]({{site.baseurl}}/user_guide/channels/email/subscriptions)
- [Abo-Gruppen]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups)

## Testen Sie Ihre E-Mails {#test-your-emails}

[Seed-Gruppen]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups) senden automatisch Kopien Ihrer E-Mail-Campaigns an interne Nutzer:innen, um eine Qualitätssicherung durchzuführen. Seed-E-Mails enthalten `[SEED]` vor der Betreffzeile, damit Sie sie leicht identifizieren können.

## Anwendungsfälle {#use-cases}

| Anwendungsfall | Erläuterung |
| --- | --- |
| Erneute Interaktion | Erreichen Sie Nutzer:innen außerhalb Ihrer App, einschließlich derjenigen, die die App nicht installiert haben. |
| Onboarding | Begrüßen Sie neue Nutzer:innen und ermutigen Sie sie, Push-Benachrichtigungen zu aktivieren oder die App in sozialen Netzwerken zu teilen. |
| Rich Messages | Ermöglichen Sie reichhaltige und dynamische HTML-Nachrichten. |
| Multimedia-Inhalte | Einfache Einbindung von Multimedia-Inhalten wie Videos und Bildern, die Nutzer:innen ansprechen. |
| Newsletter | Versenden Sie bequem monatliche oder wöchentliche Newsletter, um das Engagement der Nutzer:innen aufrechtzuerhalten. |
| Transaktionen | Benachrichtigen Sie Nutzer:innen über kürzlich getätigte Käufe und übermitteln Sie wichtige Produkt- und Versandinformationen mit [Transaktions-E-Mails]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email).
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anwendungsfälle" }

## E-Mail-Dienste {#email-services}

Wenn Sie zusätzliche Unterstützung für Ihr E-Mail-Programm benötigen, bietet Braze wiederkehrende und einmalige Serviceleistungen gegen Aufpreis an. Kontaktieren Sie Ihren Braze Account Manager:in für weitere Informationen.

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

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie richte ich den E-Mail-Versand in Braze ein? {#how-do-i-set-up-email-sending-in-braze}

Konfigurieren Sie dedizierte IPs, Domains, Authentifizierung und IP-Warming, bevor Sie Ihre erste E-Mail versenden. Die vollständige Checkliste finden Sie unter [E-Mail-Einrichtung]({{site.baseurl}}/user_guide/channels/email/email_setup).

### Was ist der Unterschied zwischen Nutzer:innen-Abos und Abo-Gruppen? {#what-is-the-difference-between-user-subscriptions-and-subscription-groups}

Nutzer:innen-Abos steuern den globalen Opt-in-Status für einen Kanal (z. B. für E-Mail angemeldet oder abgemeldet). Abo-Gruppen ermöglichen es Nutzer:innen, bestimmte Nachrichtenkategorien innerhalb dieses Kanals auszuwählen. Weitere Informationen finden Sie unter [Nutzer:innen-Abos]({{site.baseurl}}/user_guide/channels/email/subscriptions) und [Abo-Gruppen]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups).

### Wie kann ich eine E-Mail testen, bevor ich eine Campaign sende? {#how-can-i-test-an-email-before-i-send-a-campaign}

Verwenden Sie [Seed-Gruppen]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups), um Vorschau-Kopien an interne Prüfer:innen zu senden und die Darstellung in verschiedenen E-Mail-Clients zu überprüfen.

## Nächste Schritte {#next-steps}

{% article_tiles %}
- name: E-Mail-Einrichtung
  link: /docs/user_guide/channels/email/email_setup
- name: Eine E-Mail mit dem Drag-and-Drop-Editor erstellen
  link: /docs/user_guide/channels/email/drag_and_drop
- name: Eine E-Mail mit dem HTML-Editor erstellen
  link: /docs/user_guide/channels/email/html_editor
{% endarticle_tiles %}