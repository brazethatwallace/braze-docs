---
nav_title: Roku SDK
article_title: Roku SDK Repository-Leitfaden
page_order: 8
description: "Braze Roku SDK README-Referenz, gespiegelt von GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Roku SDK Repository-Leitfaden {#roku-sdk-repository-guide}

## Über das Braze Roku SDK {#about-the-braze-roku-sdk}

Das Braze Roku SDK hilft Ihnen, Braze Messaging, Analytics und Nutzer:innen-Engagement-Funktionen in Ihre Anwendung zu integrieren.

Für den Einstieg stehen Ihnen die folgenden Ressourcen zur Verfügung:

- [Braze User Guide](https://www.braze.com/docs/user_guide/introduction/)
- [Braze Developer Guide](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=roku)

## Erste SDK-Integration {#initial-sdk-integration}

Das Braze Roku SDK stellt Ihnen eine API zur Verfügung, um Informationen für Analytics, Segmentierung und Engagement zu übermitteln.

## Schritt 1: Dateien hinzufügen {#step-1-add-files}

1. Fügen Sie `BrazeSDK.brs` zu Ihrer App im Verzeichnis `source` hinzu.
2. Fügen Sie `BrazeTask.brs` und `BrazeTask.xml` zu Ihrer App in das Verzeichnis `components` hinzu.

## Schritt 2: Referenzen hinzufügen {#step-2-add-references}

Fügen Sie einen Verweis auf `BrazeSDK.brs` in Ihre Hauptszene ein, indem Sie das folgende `script`-Element verwenden:

``` text
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

## Schritt 3: Konfigurieren {#step-3-configure}

Legen Sie unter `main.brs` die Braze-Konfiguration auf dem globalen Knoten fest:

``` text
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = "YOUR_API_KEY_HERE"
config[config_fields.ENDPOINT] = "YOUR_ENDPOINT_HERE (e.g. https://sdk.iad-01.braze.com/)"
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

## Schritt 4: Braze initialisieren {#step-4-initialize-braze}

Initialisieren Sie die Braze-Instanz:

``` text
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## Einrichtung von In-App-Nachrichten {#in-app-message-setup}

Zum Verarbeiten von In-App-Nachrichten können Sie einen Observer auf `BrazeTask.BrazeInAppMessage` hinzufügen:

``` text
m.BrazeTask.observeField("BrazeInAppMessage", "onInAppMessageReceived")
```

Dann haben Sie innerhalb Ihres Handlers Zugriff auf die In-App-Nachricht mit der höchsten Priorität, die Ihre Campaigns getriggert haben:

``` text
in_app_message = m.BrazeTask.BrazeInAppMessage
```

Anschließend können Sie entscheiden, was mit der In-App-Nachricht geschehen soll. Einige der verfügbaren Felder:

- `in_app_message.message` – Der Textkörper der In-App-Nachricht
- `in_app_message.buttons` – Liste der Buttons (kann eine leere Liste sein).
- `in_app_message.id` – ID, die beim Protokollieren von Impressionen oder Klicks verwendet wird
- `in_app_message.extras` – Schlüssel/Wert-Paare
- `in_app_message.image_url` – Bild-URL
- `in_app_message.click_action` – Wenn keine Buttons vorhanden sind, bestimmt dieses Feld, was passiert, wenn Nutzer:innen auf „OK“ klicken, während die IAM angezeigt wird. Kann „URI“ oder „NONE“ sein.
- `in_app_message.dismiss_type` – Kann „AUTO_DISMISS“ oder „SWIPE“ sein
- `in_app_message.display_delay` – Wartezeit (in Sekunden) bis zur Anzeige der In-App-Nachricht
- `in_app_message.duration` – Wie lange (in Millisekunden) die Nachricht angezeigt werden soll, wenn `dismiss_type` „AUTO_DISMISS“ ist
- `in_app_message.header` – Der Header-Text der In-App-Nachricht
- `in_app_message.uri` – Wenn `click_action` „URI“ ist, sollte dieser Wert angezeigt werden

Es gibt auch verschiedene Styling-Felder, die Sie über das Dashboard nutzen können. Alternativ können Sie die In-App-Nachricht implementieren und innerhalb Ihrer Roku-Anwendung mit einer Standardpalette gestalten.
- `in_app_message.bg_color` – Hintergrundfarbe
- `in_app_message.close_button_color` – Farbe des Schließen-Buttons
- `in_app_message.frame_color` – Die Farbe des Hintergrund-Overlays
- `in_app_message.header_text_color` – Farbe des Header-Texts
- `in_app_message.message_text_color` – Farbe des Nachrichtentexts
- `in_app_message.text_align` – Kann „START“, „CENTER“ oder „END“ sein

Button-Felder umfassen:
- `buttons[0].click_action` – Kann „URI“ sein, um das `uri`-Feld zu öffnen. Kann „NONE“ sein, um die In-App-Nachricht zu schließen.
- `buttons[0].id` – Der ID-Wert des Buttons selbst
- `buttons[0].text` – Der auf dem Button angezeigte Text
- `buttons[0].uri` – Wenn `click_action` „URI“ ist, sollte dieser Wert angezeigt werden
- `buttons[0].bg_color` – Hintergrundfarbe des Buttons
- `buttons[0].border_color` – Rahmenfarbe des Buttons
- `buttons[0].text_color` – Textfarbe des Buttons

Wenn eine Nachricht angezeigt oder gesehen wird, protokollieren Sie eine Impression:

``` text
LogInAppMessageImpression(in_app_message.id, brazetask)
```

Sobald Nutzer:innen auf die Nachricht klicken, protokollieren Sie einen Klick:
``` text
LogInAppMessageClick(in_app_message.id, brazetask)
```
und verarbeiten dann `in_app_message.click_action`

Wenn Nutzer:innen auf einen Button klicken, protokollieren Sie den Button-Klick:

``` text
LogInAppMessageButtonClick(inappmessage.id, inappmessage.buttons[selected].id, brazetask)
```
und verarbeiten dann `inappmessage.buttons[selected].click_action`

Nach der Verarbeitung einer In-App-Nachricht sollten Sie das Feld löschen:

``` text
m.BrazeTask.BrazeInAppMessage = invalid
```

## Grundlegende SDK-Integration abgeschlossen {#basic-sdk-integration-complete}

Braze sollte nun Daten aus Ihrer Anwendung erfassen. In unserer öffentlichen Dokumentation erfahren Sie, wie Sie Attribute, Ereignisse und Käufe in unserem SDK protokollieren. Die Szene `MainScene.brs` unserer Beispiel-App enthält ebenfalls Beispiele zur Nutzung der API.

`BrazeInAppMessage.brs` und `CustomSideBySideInAppMessage.brs` zeigen Beispiele für die Handhabung von In-App-Nachrichten. `onInAppMessageTriggered()` in `MainScene.brs` zeigt, wie Sie mehrere Layouts unterstützen können.

## Zusätzliche Referenz {#additional-reference}

Das Verzeichnis `torchietv` enthält eine Beispiel-App mit integriertem Braze SDK.
<!-- END GENERATED README CONTENT -->

Für Repository-Details und Beispielprojekte siehe [https://github.com/braze-inc/braze-roku-sdk](https://github.com/braze-inc/braze-roku-sdk).