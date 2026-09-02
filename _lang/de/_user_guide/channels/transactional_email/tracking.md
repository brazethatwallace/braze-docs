---
nav_title: "Tracking einrichten"
article_title: "Tracking"
page_order: 2
description: "Dieser Referenzartikel behandelt die Einrichtung von Realtime-Tracking für Transaktions-E-Mail-Campaigns."
page_type: reference
tool:
  - Campaigns
channel: email

---

# Transaktions-E-Mails tracken {#track-transactional-emails}

> Diese Seite beschreibt, wie Sie Realtime-Tracking für [Transaktions-E-Mail-Campaigns]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email) einrichten. Weitere Informationen zum Endpunkt selbst finden Sie unter [Transaktions-E-Mails über API-getriggerte Zustellung senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).

Wenn Sie Transaktions-E-Mails versenden – wie Bestellbestätigungen oder Passwort-Zurücksetzungen – ist es wichtig zu wissen, ob diese Ihre Kund:innen erreichen. Mit den transaktionalen HTTP-Event-Postbacks von Braze erhalten Sie Realtime-Insights zum Status jeder Transaktions-E-Mail, sodass Sie bei Problemen schnell reagieren können.

Nutzen Sie dieses Feature, um:

- **Ihre E-Mails in Realtime zu überwachen:** Sehen Sie sofort, ob Nachrichten gesendet, verarbeitet, zugestellt wurden oder auf Probleme stoßen.
- **Proaktiv zu reagieren:** Senden Sie Nachrichten erneut, wechseln Sie zu einem anderen Kanal wie Kurzmitteilungsdienst or SMS oder nutzen Sie Fallback-Systeme, um sicherzustellen, dass Ihre Kommunikation zugestellt wird.

## Ihre Transaktions-E-Mails tracken {#tracking-your-transactional-emails}

{% multi_lang_include channels/transactional_email/http_event_postback.md %}