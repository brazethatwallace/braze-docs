---
nav_title: Webhooks
article_title: Webhooks
page_order: 9
page_type: landing
alias: /about_webhooks/
description: "Verbinden Sie Ihre Systeme mit Webhooks in Braze, die durch angepasste Events getriggert werden, um Daten und programmatische Nachrichten an externe Endpunkte zu senden."
channel:
  - webhooks
search_rank: 3
---

# Webhooks {#webhooks}

> Ein Webhook ist eine automatisierte Nachricht von einem System an ein anderes, nachdem bestimmte Kriterien erfüllt sind. In Braze ist dieses Kriterium in der Regel das Triggern eines angepassten Events. Webhooks bieten dynamischen und flexiblen Zugriff auf Daten und programmatische Funktionalität und ermöglichen es Ihnen, geschäftskunden Journeys einzurichten, die Prozesse optimieren.

## Voraussetzungen {#prerequisites}

Die Verfügbarkeit von Webhooks hängt von Ihrem Braze-Paket ab. Kontaktieren Sie Ihren Account Manager oder geschäftskunden-Success-Manager, um loszulegen.

## Anwendungsfälle {#use-cases}

Webhooks sind eine hervorragende Möglichkeit, Ihre Systeme miteinander zu verbinden – schließlich kommunizieren Apps über Webhooks. Hier sind einige allgemeine Szenarien, in denen Webhooks besonders nützlich sein können:

- Daten an und von Braze senden
- Nachrichten über Kanäle an Ihre Kund:innen senden, die nicht direkt von Braze unterstützt werden
- An Braze-APIs posten

Einige spezifischere Anwendungsfälle umfassen Folgendes:

- Erstellen Sie einen [Lead-Scoring-Workflow]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/lead_scoring) mit Webhooks und Canvas, um Leads zu qualifizieren und weiterzuleiten.
- Wenn sich ein:e Nutzer:in von E-Mails abmeldet, könnte ein Webhook Ihre Analytics-Datenbank oder Ihr CRM mit denselben Informationen aktualisieren, um eine ganzheitliche Sicht auf das Verhalten dieser Nutzer:in zu gewährleisten.
- Senden Sie [transaktionale Nachrichten]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign) an Nutzer:innen innerhalb von Facebook Messenger oder Line.
- Senden Sie Direkt-Mailings an Kund:innen als Reaktion auf deren In-App- und Internet-Aktivitäten, indem Sie Webhooks verwenden, um mit Drittanbieterdiensten wie [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob) zu kommunizieren.
- Wenn ein:e Spieler:in ein bestimmtes Level erreicht oder eine bestimmte Anzahl von Punkten sammelt, verwenden Sie Webhooks und Ihr bestehendes API-Setup, um ein Charakter-Upgrade oder Münzen direkt auf das Konto zu senden. Wenn Sie den Webhook als Teil einer Multichannel-Messaging-Kampagne senden, können Sie gleichzeitig eine Push-Nachricht oder eine andere Nachricht senden, um die:den Spieler:in über die Belohnung zu informieren.
- Wenn Sie eine Fluggesellschaft sind, können Sie Webhooks und Ihr bestehendes API-Setup verwenden, um das Konto einer geschäftskunden mit einem Rabatt zu versehen, nachdem eine bestimmte Anzahl von Flügen gebucht wurde.
- Endlose „If This Then That“ ([IFTTT](https://ifttt.com/about))-Rezepte – zum Beispiel: Wenn sich ein:e geschäftskunden über E-Mail in die App einloggt, kann diese Adresse automatisch in Salesforce konfiguriert werden.

## Webhook-Fehlerbehandlung und Rate-Limiting {#webhook-error-handling-and-rate-limiting}

Braze wiederholt die Webhook-Zustellung nur bei bestimmten HTTP-Antworten (zum Beispiel `408`, `429` und `5XX`). Die meisten anderen Antworten, einschließlich `401 Unauthorized` und anderer `4XX`-Fehler, werden nicht wiederholt. Antwort-Header wie `Retry-After` und `X-Rate-Limit-*` können das Backoff-Timing beeinflussen, **wenn eine Antwort bereits für einen erneuten Versuch qualifiziert ist**; sie veranlassen Braze nicht, Fehler zu wiederholen, die außerhalb der wiederholbaren Menge liegen.

Die vollständige Tabelle der Antwortcodes, Wiederholungslimits und das Timeout-Verhalten finden Sie unter [Antwortcodes und Wiederholungslogik]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#response-codes-and-retry-logic).

Wenn die Mehrheit der Webhook-Anfragen an einen bestimmten Host fehlschlägt, verschiebt Braze vorübergehend alle Sendeversuche an diesen Host. Das Senden wird nach einer definierten Abkühlungsphase wieder aufgenommen, damit sich Ihr System erholen kann.

## Webhooks mit Braze-Partnern verwenden {#utilizing-webhooks}

Es gibt viele Möglichkeiten, Webhooks zu nutzen, und mit unseren Technologie-Partnern (Alloys) können Sie Webhooks verwenden, um Ihre Kommunikation direkt mit Ihren Kund:innen und Nutzer:innen zu verbessern.

Schauen Sie sich an:
* [Messenger]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/instant_chat/messenger)
* [Remerge]({{site.baseurl}}/partners/remerge)
* [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob)
* Und viele weitere unserer [Technologie-Partner]({{site.baseurl}}/partners/home)!

## Nächste Schritte {#next-steps}

- [Webhook erstellen]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook)
- [Einen Braze-zu-Braze-Webhook erstellen]({{site.baseurl}}/user_guide/channels/webhooks/use_case_create_a_braze_to_braze_webhook)