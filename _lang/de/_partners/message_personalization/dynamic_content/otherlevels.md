---
nav_title: OtherLevels
article_title: OtherLevels
alias: /partners/otherlevels/
description: "Dieser Artikel behandelt die Integration zwischen der OtherLevels Experience Platform und Braze."
page_type: partner
search_tag: OtherLevels

---

# OtherLevels

> Die [OtherLevels](https://www.otherlevels.com/) Experience Platform nutzt GenAI, um die Art und Weise zu verändern, wie Sportmarken, Verlage und Betreiber mit ihren Kund:innen in Kontakt treten, indem sie traditionelle Inhalte in markengerechte, personalisierte Video- und Rich-Media-Erlebnisse in großem Umfang umwandelt.

*Diese Integration wird von OtherLevels gepflegt.*

## Übersicht {#overview}

Die Integration von Braze und OtherLevels ermöglicht es Ihnen, angepasste GenAI-Videos über API-Aufrufe an die OtherLevels Experience Platform zu erstellen und diese Videos dann als iOS-Push-Videos über [Braze Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call) an Ihre Nutzer:innen zu senden.

Bieten Sie Ihren Nutzer:innen ein besseres Erlebnis mit den KI or künstliche Intelligenz-gestützten Erfahrungen von OtherLevels. Transformieren Sie vorhandene und Drittanbieter-Inhalte in hochskalierbare Videos und Rich Media für Zielgruppen, die Inhalte bereits anders konsumieren und stark auf kontextuell personalisierte Erlebnisse reagieren.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung          | Beschreibung                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Ein OtherLevels-Konto   | Um die Vorteile dieser Partnerschaft zu nutzen, ist ein OtherLevels-Konto erforderlich.                                                                     |
| Ein Braze-Representational State Transfer-API-Schlüssel  | Ein Braze-Representational State Transfer-API-Schlüssel mit `users.track`-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Ein Braze-Representational State Transfer-Endpunkt | [Ihre Representational State Transfer-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab.                                                 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

Diese Integration erfordert den Aufruf der OtherLevels Experience Platform API als Teil des Video-Generierungsprozesses, bevor Nachrichten von Braze an Ihre Nutzer:innen gesendet werden können. cURL-Beispiele werden als Teil dieser Dokumentation bereitgestellt, wir empfehlen jedoch die Verwendung von API-Clients wie Postman, um die API-Aufrufe zu automatisieren.

## Anwendungsfälle {#use-cases}

Nutzen Sie GenAI-Videos, die mit der OtherLevels Experience Platform erstellt wurden, um:
- Bessere Erlebnisse für Sporteigentümer:innen und Ligen, Fan-Engagement, Sportwetten, iGaming und Lotterien zu schaffen.
- Ihr Kundenmarketing zu verstärken, indem Sie textbasierte Inhalte in Rich Media und Video transformieren und so menschliche und ansprechende Erlebnisse schaffen.
- Ergebnisse von der Akquise bis zur Bindung zu verbessern, indem Sie Ihre bestehende Braze-Integration erweitern, statt sie umzurüsten.

## Integration der OtherLevels Experience Platform {#integrating-the-otherlevels-experience-platform}

### 1. Schritt: Rufen Sie die OtherLevels Experience Platform API auf, um ein Video zu generieren {#step-1}

Der erste Schritt der Integration besteht darin, die OtherLevels Experience Platform API aufzurufen, um ein neues Video zu generieren. Beachten Sie, dass die Videogenerierung nicht sofort erfolgt. Je nach Länge und Komplexität des Videos kann die Erstellung der Inhalte bis zu einer halben Stunde dauern. Planen Sie Ihre Messaging-Zeitpläne und API-Aufrufe entsprechend, damit die API-Aufrufe zur Videogenerierung rechtzeitig vor dem geplanten Versand Ihrer Braze-Nachrichten erfolgen.

{% alert important %}
Die folgende Anfrage verwendet cURL. Für eine effizientere Verwaltung von API-Anfragen empfehlen wir die Verwendung eines API-Clients wie Postman.
{% endalert %}

Das folgende Beispiel zeigt, wie Sie Ihren API-Aufruf strukturieren sollten. Weitere Informationen zum Anpassen der Video-Spezifikationen und zur Strukturierung Ihres API-Aufrufs finden Sie unter [Anpassen des GenAI-Videos](#customizing-the-genai-video).

{% raw %}
```bash
curl --request POST \
  --url 'https://exp-platform-api.prod.awsotherlevels.com/v1/app/OTHERLEVELS_PROJECT_KEY/media?=' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/10.3.0' \
  --data '{
    "task": {
        "type": "tasks",
        "tasks": {
            "image_video_overlay": {
                "width": "= .orientation == '\''portrait'\'' ? '\''1080'\'' : .orientation == '\''landscape'\'' ? '\''1920'\''",
                "height": "= .orientation == '\''portrait'\'' ? '\''1920'\'' : .orientation == '\''landscape'\'' ? '\''1080'\''",
                "color": "255,255,255,0",
                "y_pos": "0",
                "x_pos": "0",
                "image_input": "= tasks.resize_image.jpg ?? tasks.resize_image.png",
                "video_input": "= tasks.talking_talent_replace_bg.mp4",
                "type": "compose.ImageVideoOverlay"
            },
            "resize_image": {
                "media_input": "= tasks.bg_image.jpg ?? tasks.bg_image.png",
                "type": "compose.MediaResize",
                "width": "= .orientation == '\''portrait'\'' ? '\''1080'\'' : .orientation == '\''landscape'\'' ? '\''1920'\''",
                "height": "= .orientation == '\''portrait'\'' ? '\''1920'\'' : .orientation == '\''landscape'\'' ? '\''1080'\''"
            },
            "bg_image": {
                "type": "load",
                "url": "BACKGROUND_IMAGE_URL",
                "refresh_interval": "12h"
            },
            "talking_head": {
                "test": false,
                "title": "INSERT_TITLE",
                "caption": false,
                "templateId": "TALENT_TEMPLATE",
                "type": "TALENT_MODEL",
                "variables": {
                    "script": {
                        "name": "script",
                        "properties": {
                            "content": "= tasks.translate_text.text"
                        },
                        "type": "text"
                    }
                }
            },
            "translate_text": {
                "type": "translate_text",
                "source": "en",
                "target": "en",
                "text": "INSERT_SCRIPT"
            },
            "talking_talent_speed": {
                "type": "compose.VideoSetSpeed",
                "speed": "1.0",
                "video_input": "= tasks.talking_head.mp4"
            },
            "talking_talent_replace_bg": {
                "type": "compose.VideoReplaceBg",
                "video_background": "= tasks.resize_image.jpg ?? tasks.resize_image.png",
                "video_input": "= tasks.talking_talent_speed.mp4"
            }
        },
        "output": "image_video_overlay"
    }
}'
```
{% endraw %}

Ersetzen Sie Folgendes:

| Platzhalter          | Beschreibung                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `OTHERLEVELS_PROJECT_KEY`   | Ein OtherLevels-Projektschlüssel wird Ihnen bei der Einrichtung Ihres OtherLevels-Kontos bereitgestellt.                                                                     |
| `BACKGROUND_IMAGE_URL`  | Eine HTTPS-URL für den Hintergrund des Videos. |
| `INSERT_TITLE` | Der Titel des Videos – dies ist eine interne Referenz und wird im Video nicht angezeigt.                                                 |
| `TALENT_TEMPLATE` | Eine Talent-Template-ID. OtherLevels wird bei der Kontoeinrichtung mit Ihnen zusammenarbeiten, um ein Talent (Avatar) zu erstellen. Sie erhalten eine oder mehrere Talent-IDs, die Sie verwenden können.                                                 |
| `TALENT_MODEL` | Eine Talent-Model-ID. OtherLevels wird bei der Kontoeinrichtung mit Ihnen zusammenarbeiten, um ein Talent (Avatar) zu erstellen. Sie erhalten ein oder mehrere Talent-Modelle, die Sie verwenden können.                                                 |
| `INSERT_SCRIPT` | Das genaue Skript, das das Talent während des Videos sprechen soll.                                                 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 1: OtherLevels Experience Platform API aufrufen, um ein Video zu generieren" }

Als Teil der API-Antwort gibt OtherLevels eine JSON-Nutzlast zurück, die einen erfolgreichen API-Aufruf anzeigt. Die JSON-Datei enthält eine eindeutige `recipe_id` zur Identifizierung des generierten Videos. Die `recipe_id` wird im nächsten Schritt benötigt.

Hier ist eine Beispielantwort der API:

{% raw %}
```bash
{"$schema":"https://exp-platform-api.prod.awsotherlevels.com/schemas/GenerateMediaResBody.json","message":"success","recipe_id":"LMINHWXV2BBD6JGV5VF3ZNZV7BDDRR7FH5FJH6MMX4BVLTPRKTWQ","media_short_id":"LMINHWX","status":"triggered"}
```
{% endraw %}

### 2. Schritt: Festlegen der `recipe_id` als angepasstes Attribut {#step-2-setting-the-recipe_id-as-a-custom-attribute}

Die `recipe_id`, die Sie in [Schritt 1](#step-1) erhalten haben, wird nun als angepasstes Braze-Attribut für die Nutzer:innen festgelegt, an die Sie die Videos senden möchten.

Je nach Anwendungsfall haben Sie möglicherweise ein einzelnes Video erstellt, das für eine große Zielgruppe bestimmt ist – in diesem Fall kann dieselbe `recipe_id` für mehrere Nutzer:innen festgelegt werden. Alternativ haben Sie möglicherweise mehrere eindeutige Videos erstellt, die jeweils auf unterschiedliche Nutzer:innen abzielen – in diesem Fall sollte für jede:n Nutzer:in die jeweilige `recipe_id` als angepasstes Braze-Attribut festgelegt werden.

{% alert important %}
Die folgende Anfrage verwendet cURL. Für eine effizientere Verwaltung von API-Anfragen empfehlen wir die Verwendung eines API-Clients wie Postman.
{% endalert %}

{% raw %}
```bash
curl --location --request POST 'BRAZE_API_ENDPOINT/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer BRAZE_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "USER_ID",
      "olxpmedia": "RECIPE_ID"
    }
  ]
}'
```
{% endraw %}

Ersetzen Sie Folgendes:

| Platzhalter             | Beschreibung                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_ENDPOINT`    | Die URL des Braze-Representational State Transfer-Endpunkts Ihrer aktuellen Braze-Instanz. Weitere Informationen finden Sie unter [Representational State Transfer-API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab#rest-api-keys). |
| `BRAZE_API_KEY`         | Ihr Braze-Representational State Transfer-API-Schlüssel mit der Berechtigung `users.track`.                                                                                                                                      |
| `USER_ID`              | Die Nutzer-ID der Person, die dieses Video erhalten soll. Weitere Beispiele für verwendbare Bezeichner finden Sie unter [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track).                                                                                                                                                  |
| `RECIPE_ID`       | Die `recipe_id`, die Sie aus der OtherLevels-API-Antwort in [Schritt 1](#step-1) erhalten haben.                                                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 2: Festlegen der recipe_id als angepasstes Attribut" }

### 3. Schritt: Versand über Braze Connected Content {#step-3-sending-through-braze-connected-content}

Um die GenAI-Videos als iOS-Push-Nachrichten an Ihre Nutzer:innen zu senden, gehen Sie folgendermaßen vor:

1. Erstellen Sie eine Braze-iOS-Push-Benachrichtigungs-Campaign.
2. Gehen Sie bei der Erstellung Ihrer Campaign in den Bereich **Assets** und fügen Sie die folgende Connected-Content-Syntax in das Feld **Add from URL** ein.

{% raw %}
```
{% connected_content https://exp-platform-api-external.prod.awsotherlevels.com/v1/app/OTHERLEVELS_PROJECT_KEY/media/{{custom_attribute.${olxpmedia}}} %}
```
{% endraw %}

Ersetzen Sie anschließend `OTHERLEVELS_PROJECT_KEY` durch den von OtherLevels bereitgestellten Projektschlüssel.

{: start="3"}
3. Wählen Sie im Dropdown-Menü für **URL file format** die Option **MP4** aus.
4. Konfigurieren Sie den Representational State Transfer der Campaign (z. B. Nachrichteninhalt, Versandzeitplan und Zielgruppe) nach Ihren Wünschen.

![Beispiel für Asset-Felder bei Connected Content.]({% image_buster /assets/img/otherlevels/1.png %})

## Anpassen des GenAI-Videos {#customizing-the-genai-video}

### Videogröße und Attribute {#video-size-and-attributes}

Der Video-Hintergrund kann über den Schlüssel `bg_image` festgelegt werden.

| Parameter             | Beschreibung                  |
|-------------------------|----------------------------|
| `url`    | HTTPS-URL für das Hintergrundbild. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Videogröße und Attribute" }

Die Größe des Video-Hintergrunds kann über den Schlüssel `resize_image` festgelegt werden. Wir empfehlen, dass das Hintergrundbild dieselbe Größe hat wie die hier konfigurierte.

| Parameter             | Beschreibung                  |
|-------------------------|----------------------------|
| `width`    | Breite des Hintergrundbildes, mit Optionen für Hoch- und Querformat. |
| `height`     | Höhe des Hintergrundbildes, mit Optionen für Hoch- und Querformat.                              |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Videogröße und Attribute" }

Video-Overlay-Optionen können über den Schlüssel `image_video_overlay` festgelegt werden.

| Parameter             | Beschreibung                  |
|-------------------------|----------------------------|
| `width`    | Breite des Overlays, mit Optionen für Hoch- und Querformat. |
| `height`         | Höhe des Overlays, mit Optionen für Hoch- und Querformat.                                              |
| `color`              | Farbe des Overlays, angegeben in RGB zusammen mit dem Transparenzwert.                                                                   |
| `y_pos`       | Y-Achsen-Versatz vom Zentrum.                                                              |
| `x_pos`    | X-Achsen-Versatz vom Zentrum. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Videogröße und Attribute" }

### Talent und Skript {#talent-and-script}

Im Rahmen der Bereitstellung wird OtherLevels mit Ihnen zusammenarbeiten, um ein oder mehrere Talente (manchmal auch als Avatare bezeichnet) für die Verwendung in Ihren Videos zu erstellen. Je nach Anwendungsfall und Marke kann dies in Form eines Ihrer bestehenden Markenbotschafter:innen oder einer einzigartigen Kreation erfolgen.

Nachdem diese erstellt wurden, erhalten Sie verwendbare `TALENT_TEMPLATE`- und `TALENT_MODEL`-IDs zur Nutzung mit unserer API.

Das Sprachmodell, das zur Verarbeitung von Eingabeskripten verwendet wird, funktioniert am besten mit einem natürlichen Skript, das ein Mensch vorlesen würde. In den meisten Fällen benötigen Sie keine zusätzliche Interpunktion, um das Skript manuell zu steuern. Wir empfehlen jedoch, alle Ihre Skripte zu testen, bevor Sie sie an eine echte Zielgruppe senden. Die Geschwindigkeit, mit der das Talent das Skript liest, kann über den Schlüssel `talking_talent_speed` festgelegt werden.

| Parameter             | Beschreibung                  |
|-------------------------|----------------------------|
| `speed`    | Legen Sie die Geschwindigkeit fest, mit der das Talent das Skript lesen soll. Zum Beispiel: `1.5`.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Talent und Skript" }

## Zusätzliche Hinweise {#additional-considerations}

- Nur die iOS-Push-Benachrichtigungsplattform unterstützt nativ Videomedien. Android-Push-Benachrichtigungen unterstützen nativ keine Videos, daher kann diese Integration nur für Ihre iOS-Zielgruppe verwendet werden.
- Beim Empfang von Video-Push-Benachrichtigungen auf iOS-Geräten müssen Nutzer:innen die Push-Benachrichtigung gedrückt halten, damit das Video geladen und abgespielt wird. Dies ist ein Standardverhalten auf der iOS-Plattform und kann nicht angepasst werden.