---
nav_title: Testen
article_title: Push-Benachrichtigungstests für iOS
platform: iOS
page_order: 29
description: "Dieser Referenzartikel behandelt das Testen von Push-Benachrichtigungen über die Befehlszeile für Ihre iOS-Push-Benachrichtigungen."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Testen {#push-testing}

Wenn Sie In-App- und Push-Benachrichtigungen über die Befehlszeile testen möchten, können Sie über CURL und die [Messaging API]({{site.baseurl}}/api/endpoints/messaging) eine einzelne Benachrichtigung über das Terminal senden. Sie müssen die folgenden Felder durch die richtigen Werte für Ihren Testfall ersetzen:

Erforderliche Felder:

- `YOUR-API-KEY-HERE` – verfügbar unter **Einstellungen** > **API-Schlüssel**. Stellen Sie sicher, dass der Schlüssel berechtigt ist, Nachrichten über den Representational State Transfer-API-Endpunkt `/messages/send` zu versenden.
- `EXTERNAL_USER_ID` – verfügbar auf der Seite **Nutzer:innen suchen**.
- `REST_API_ENDPOINT_URL` – aufgeführt auf der Braze-Seite [Instanzen]({{site.baseurl}}/api/basics#endpoints. Ensure using the endpoint corresponds to the Braze instance your workspace is on.

Optional fields:
- `YOUR_KEY1` (optional). Stellen Sie sicher, dass der verwendete Endpunkt der Braze-Instanz entspricht, auf der sich Ihr Workspace befindet.

Optionale Felder:
- `YOUR_KEY1` (optional)
- `YOUR_VALUE1` (optional)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer YOUR-API-KEY-HERE" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://{REST_API_ENDPOINT_URL}/messages/send
```
