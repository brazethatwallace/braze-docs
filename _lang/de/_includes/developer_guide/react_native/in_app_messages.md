{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Nachrichtentypen {#message-types}

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Datenmodell {#data-model}

Das Modell für In-App-Nachrichten ist im React Native SDK or Software-Development-Kit verfügbar. Braze verfügt über vier In-App-Nachrichtentypen, die dasselbe Datenmodell verwenden: **Slideup**, **Modal**, **Full** und **HTML Full**.

### Nachrichten {#messages}

Das In-App-Nachricht-Modell bildet die Grundlage für alle In-App-Nachrichten.

| Eigenschaft | Beschreibung |
|------------------|------------------------------------------------------------------------------------------------------------------------|
| `inAppMessageJsonString` | Die JSON-Darstellung der Nachricht. |
| `message` | Der Text der Nachricht. |
| `header` | Die Kopfzeile der Nachricht. |
| `uri` | Die URI, die mit der Klick-Aktion des Buttons verbunden ist. |
| `imageUrl` | Die Bild-URL der Nachricht. |
| `zippedAssetsUrl` | Die gezippten Assets, die für die Anzeige von HTML-Inhalten vorbereitet sind. |
| `useWebView` | Gibt an, ob die Klick-Aktion des Buttons über eine Webansicht umgeleitet werden soll. |
| `duration` | Die Anzeigedauer der Nachricht. |
| `clickAction` | Der Aktionstyp für den Klick auf den Button. Die Typen sind: `URI` und `NONE`. |
| `dismissType` | Die Art des Schließens der Nachricht. Die beiden Arten sind: `SWIPE` und `AUTO_DISMISS`. |
| `messageType` | Der vom SDK or Software-Development-Kit unterstützte Typ der In-App-Nachricht. Die vier Typen sind: `SLIDEUP`, `MODAL`, `FULL` und `HTML_FULL`. |
| `extras` | Das Extras-Wörterbuch der Nachricht. Standardwert: `[:]`. |
| `buttons` | Die Liste der Buttons in der In-App-Nachricht. |
| `toString()` | Die Nachricht als String-Darstellung. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Messages" }

Eine vollständige Referenz des In-App-Nachricht-Modells finden Sie in der Dokumentation für [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/index.html) und [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage).

### Buttons

In-App-Nachrichten können Buttons hinzugefügt werden, um Aktionen durchzuführen und Analytics zu protokollieren. Das Button-Modell bildet die Grundlage für alle In-App-Nachricht-Buttons.

| Eigenschaft | Beschreibung |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `text` | Der Text auf dem Button. |
| `uri` | Die URI, die mit der Klick-Aktion des Buttons verbunden ist. |
| `useWebView` | Gibt an, ob die Klick-Aktion des Buttons über eine Webansicht umgeleitet werden soll. |
| `clickAction` | Die Art der Klick-Aktion, die verarbeitet wird, wenn Nutzer:innen auf den Button klicken. Die Typen sind: `URI` und `NONE`. |
| `id` | Die ID des Buttons in der Nachricht. |
| `toString()` | Der Button als String-Darstellung. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Buttons" }

Eine vollständige Referenz des Button-Modells finden Sie in der Dokumentation für [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html) und [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/button).