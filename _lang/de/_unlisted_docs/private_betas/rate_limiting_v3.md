---
article_title: Rate-Limiting für Push-Campaigns und Multichannel-Canvases
permalink: /rate_limiting_v3/
page_type: reference
description: "Dieser Artikel beschreibt die Rate-Limits für die Zustellgeschwindigkeit bei Push-Campaigns und Multichannel-Canvases."
---

# Rate-Limiting für Push-Campaigns und Multichannel-Canvases {#rate-limiting-for-push-campaigns-and-multichannel-canvases}

> Diese Seite behandelt das Rate-Limiting für Push-Campaigns und Multichannel-Canvases, einschließlich wichtiger Überlegungen, die Sie bei der Steuerung Ihrer Nachrichten beachten sollten.

Beim Festlegen der Rate-Limits für die Zustellgeschwindigkeit bei Push-Campaigns und Multichannel-Canvases können Sie jetzt zwischen folgenden Optionen wählen:

- Rate-Limits pro Kanal
- Ein übergreifendes Rate-Limit, das über alle Nachrichtenkanäle hinweg geteilt wird.

{% alert important %}
Rate-Limiting für Push-Campaigns und Multichannel-Canvases befindet sich im Early Access. Kontaktieren Sie Ihren Braze Account Manager, wenn Sie an der Teilnahme an diesem Early Access interessiert sind.
{% endalert %}

Die folgenden Funktionen sind in diesem Early Access **nicht** enthalten:

- Festlegen von Rate-Limits pro Kanal für Multichannel-Campaigns jeglichen Typs und API-getriggerte Canvases
- Festlegen eines globalen Rate-Limits
- Festlegen von Rate-Limits pro Nachrichtenschritt in Canvas

## Überlegungen {#considerations}

- Dieses Rate-Limiting-Update hindert Sie nicht daran, ein sehr niedriges Rate-Limit festzulegen. Das bedeutet, dass Sie ohne diese Schutzmaßnahme ein Rate-Limit setzen könnten, das je nach Zielgruppengröße dazu führen kann, dass Ihre Nachrichten extrem langsam versendet werden.
- Die **Sendeeinstellungen**-Zusammenfassungen für Campaigns und Canvases können ungenaue Beschreibungen für die festgelegten Rate-Limits enthalten: <br><br>![Sendeeinstellungen für Campaigns, bei denen es keine Einschränkungen für die Rate gibt, mit der Nutzer:innen Nachrichten erhalten.]({% image_buster /assets/unlisted_docs/img/send_settings_example.png %}){: style="max-width:65%"}<br><br>
- Rate-Limiting für Multichannel-Campaigns (nicht Canvases oder Push-Campaigns) spiegelt das [nicht aktualisierte Rate-Limiting-Verhalten für Multichannel-Campaigns](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting) wider. Wir empfehlen, während dieser Phase des Early Access keine Multichannel-Campaigns mit Rate-Limiting zu erstellen.