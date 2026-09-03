---
nav_title: Transaktions-E-Mails
article_title: Transaktions-E-Mails
page_order: 4
page_type: landing
channel:
  - email
search_rank: 3
description: "Senden Sie Transaktions-E-Mails für kritische, zeitkritische Benachrichtigungen, die durch API-Aufrufe in Braze getriggert werden."
---

# Transaktions-E-Mails {#transactional-email}

> Transaktions-E-Mails sind speziell für den Versand automatisierter, nicht-werblicher Nachrichten konzipiert, um eine vereinbarte Transaktion zwischen Ihnen und Ihren Kund:innen abzuwickeln. Verwenden Sie Transaktions-E-Mail-Campaigns in Braze, um kritische, zeitkritische Benachrichtigungen zu senden, die durch API-Aufrufe getriggert werden, wie z. B. Bestellbestätigungen, Passwortzurücksetzungen und Versand-Updates.

## Voraussetzungen {#prerequisites}

Transaktions-E-Mails sind nur als Teil ausgewählter Braze-Pakete verfügbar. Kontaktieren Sie Ihren Braze-CSM oder eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/user_guide/administer/personal/braze_support) für weitere Details.

Bevor Sie beginnen, stellen Sie sicher, dass Folgendes vorhanden ist:

- Abgeschlossene [E-Mail-Einrichtung]({{site.baseurl}}/user_guide/channels/email/email_setup), einschließlich IP- und Domain-Konfiguration, Authentifizierung und IP-Warming
- Ein **Braze-REST-API-Schlüssel** mit der Berechtigung `transactional.send`

## Anwendungsfälle {#use-cases}

Transaktions-E-Mails sind für den Versand nicht-werblicher, dienstausgelöster Nachrichten konzipiert. Häufige Anwendungsfälle sind:

| Anwendungsfall | Erklärung |
| --- | --- |
| Bestellbestätigungen | Bestätigen Sie, dass der Kauf einer Kund:in eingegangen ist und bearbeitet wird. |
| Passwortzurücksetzungen | Stellen Sie sichere, zeitkritische Links bereit, über die Kund:innen ihre Zugangsdaten zurücksetzen können. |
| Versandbenachrichtigungen | Benachrichtigen Sie Kund:innen, wenn ihre Bestellung versandt wurde, einschließlich Tracking-Informationen und voraussichtlicher Liefertermine. |
| Kontobenachrichtigungen | Senden Sie wichtige kontobezogene Benachrichtigungen, wie z. B. fehlgeschlagene Zahlungen, Abo-Änderungen oder Sicherheitswarnungen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anwendungsfälle" }

## Unterschiede zwischen Transaktions-E-Mails und Marketing-E-Mails {#how-transactional-email-differs-from-marketing-email}

Transaktions-E-Mails werden über eine dedizierte [transaktionale HTTP-API]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email) von Braze versendet, die auf Geschwindigkeit und Zuverlässigkeit optimiert ist. Im Gegensatz zu Marketing-E-Mails gilt für Transaktions-E-Mails:

- Sie erfordern kein Opt-in der Nutzer:innen für Marketing-Kommunikation
- Sie werden durch API-Aufrufe ausgelöst und nicht durch zeitgesteuerte oder aktionsbasierte Trigger
- Sie unterstützen eine nahezu Realtime-Zustellung für zeitkritische Inhalte

## Nächste Schritte {#next-steps}

{% article_tiles %}
- name: Transaktions-E-Mail erstellen
  link: /docs/user_guide/channels/transactional_email/create_a_transactional_email
- name: Tracking
  link: /docs/user_guide/channels/transactional_email/tracking
{% endarticle_tiles %}