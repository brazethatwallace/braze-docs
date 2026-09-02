{% multi_lang_include developer_guide/prerequisites/roku.md %} Außerdem werden In-App-Nachrichten nur an Roku-Geräte gesendet, auf denen die minimal unterstützte SDK or Software-Development-Kit-Version läuft:

{% sdk_min_versions roku:0.1.2 %}

## Nachrichtentypen {#message-types}

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Aktivieren von In-App-Nachrichten {#enabling-in-app-messages}

### 1. Schritt: Einen Observer hinzufügen {#step-1-add-an-observer}

Zum Verarbeiten von In-App-Nachrichten können Sie einen Observer auf `BrazeTask.BrazeInAppMessage` hinzufügen:

```brightscript
m.BrazeTask.observeField("BrazeInAppMessage", "onInAppMessageReceived")
```

### 2. Schritt: Zugriff auf getriggerte Nachrichten {#step-2-access-triggered-messages}

Dann haben Sie innerhalb Ihres Handlers Zugriff auf die In-App-Nachricht mit der höchsten Priorität, die Ihre Campaigns getriggert haben:

```brightscript
sub onInAppMessageReceived()
  in_app_message = m.BrazeTask.BrazeInAppMessage
  ...
end sub
```

## Felder für Nachrichten {#message-fields}

### Handhabung {#handling}

Im Folgenden sind die Felder aufgeführt, die Sie für die Handhabung Ihrer In-App-Nachrichten benötigen:

| Felder | Beschreibung |
| ------ | ----------- |
| `buttons` | Liste der Buttons (kann eine leere Liste sein). |
| `click_action` | `"URI"` oder `"NONE"`. Verwenden Sie dieses Feld, um anzugeben, ob die In-App-Nachricht einen URI-Link öffnen oder die Nachricht schließen soll, wenn darauf geklickt wird. Wenn es keine Buttons gibt, sollte dies geschehen, wenn Nutzer:innen auf „OK“ klicken, während die In-App-Nachricht angezeigt wird. |
| `dismiss_type` | `"AUTO_DISMISS"` oder `"SWIPE"`. Verwenden Sie dieses Feld, um anzugeben, ob Ihre In-App-Nachricht automatisch ausgeblendet werden soll oder eine Swipe-Geste zum Ausblenden erforderlich ist. |
| `display_delay` | Wartezeit (in Sekunden), bis die In-App-Nachricht angezeigt wird. |
| `duration` | Anzeigedauer der Nachricht (in Millisekunden), wenn `dismiss_type` auf `"AUTO_DISMISS"` festgelegt ist. |
| `extras` | Schlüssel-Wert-Paare. |
| `header` | Der Kopfzeilentext. |
| `id` | Die ID, die zum Protokollieren von Impressionen oder Klicks verwendet wird. |
| `image_url` | Bild-URL der In-App-Nachricht. |
| `message` | Nachrichtentext. |
| `uri` | URI, an die Nutzer:innen basierend auf der `click_action` weitergeleitet werden. Dieses Feld muss enthalten sein, wenn `click_action` `"URI"` ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Handling" }

{% alert important %}
Bei In-App-Nachrichten mit Buttons wird die `click_action` der Nachricht ebenfalls in die endgültige Payload aufgenommen, wenn die Klickaktion vor dem Hinzufügen des Button-Textes hinzugefügt wird.
{% endalert %}

### Styling

Über das Dashboard können verschiedene Styling-Felder ausgewählt werden:

| Felder | Beschreibung |
| ------ | ----------- |
| `bg_color` | Hintergrundfarbe. |
| `close_button_color` | Farbe des Schließen-Buttons. |
| `frame_color` | Farbe des Overlays für den Hintergrundbildschirm. |
| `header_text_color` | Textfarbe der Überschrift. |
| `message_text_color` | Farbe des Nachrichtentextes. |
| `text_align` | „START“, „CENTER“ oder „END“. Ihre ausgewählte Textausrichtung. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Styling" }

Alternativ können Sie die In-App-Nachricht implementieren und sie innerhalb Ihrer Roku-Anwendung mit einer Standardpalette gestalten:

### Buttons

| Felder | Beschreibung |
| ------ | ----------- |
| `click_action` | `"URI"` oder `"NONE"`. Verwenden Sie dieses Feld, um anzugeben, ob die In-App-Nachricht einen URI-Link öffnen oder die Nachricht schließen soll, wenn darauf geklickt wird. |
| `id` | Der ID-Wert des Buttons. |
| `text` | Der Text, der auf dem Button angezeigt werden soll. |
| `uri` | URI, an die Nutzer:innen basierend auf der `click_action` weitergeleitet werden. Dieses Feld muss enthalten sein, wenn `click_action` `"URI"` ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Buttons" }