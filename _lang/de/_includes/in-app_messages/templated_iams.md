In-App-Nachrichten werden als Template-basierte In-App-Nachrichten zugestellt, wenn **Kampagnenberechtigung vor der Anzeige erneut prüfen** ausgewählt ist oder wenn einer der folgenden Liquid-Tags in der Nachricht vorhanden ist:

- `canvas_entry_properties`
- `connected_content`
- Kurzmitteilungsdienst or SMS-Variablen wie {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Das bedeutet, dass das Gerät beim Sitzungsstart den Trigger or triggern dieser In-App-Nachricht anstelle der gesamten Nachricht erhält. Wenn Nutzer:innen die In-App-Nachricht Trigger or triggern or triggern, stellt das Gerät eine Netzwerkanfrage, um die eigentliche Nachricht abzurufen.

{% alert note %}
Die Nachricht wird nicht zugestellt, wenn das Gerät keinen Internetzugang hat. Die Nachricht wird möglicherweise nicht zugestellt, wenn die Auflösung der Liquid-Logik zu lange dauert.
{% endalert %}