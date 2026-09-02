### Fehlerbehebung bei der Anzeige {#troubleshooting-in-app-message-display}

Wenn Ihre App In-App-Nachrichten anfordert und empfängt, diese aber nicht angezeigt werden, kann die geräteseitige Logik die Anzeige verhindern:

1. Wird das Trigger-Event wie erwartet ausgelöst? Um dies zu testen, konfigurieren Sie die Nachricht so, dass sie durch eine andere Aktion (z. B. Sitzungsstart) getriggert wird, und überprüfen Sie, ob sie angezeigt wird.
{% if include.sdk == "iOS" %}
2. Getriggerte In-App-Nachrichten unterliegen einem Rate-Limit basierend auf dem [minimalen Zeitintervall zwischen Triggern]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=swift#overriding-the-default-rate-limit), das standardmäßig 30 Sekunden beträgt.
{% elsif include.sdk == "Android" %}
2. Getriggerte In-App-Nachrichten unterliegen einem Rate-Limit basierend auf dem [minimalen Zeitintervall zwischen Triggern]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=android#overriding-the-default-rate-limit), das standardmäßig 30 Sekunden beträgt.
{% elsif include.sdk == "Web" %}
2. Getriggerte In-App-Nachrichten unterliegen einem Rate-Limit basierend auf dem [minimalen Zeitintervall zwischen Triggern]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web#overriding-the-default-rate-limit), das standardmäßig 30 Sekunden beträgt.
{% endif %}
3. Fehlgeschlagene Bild-Downloads verhindern die Anzeige von In-App-Nachrichten mit Bildern. Überprüfen Sie die Geräteprotokolle auf Download-Fehler. Versuchen Sie, das Bild vorübergehend zu entfernen, um zu sehen, ob die Nachricht dann angezeigt wird.
{% case include.sdk %}
  {% when "iOS" %}
4. Wenn Sie einen Delegaten zum Anpassen der Handhabung von In-App-Nachrichten festgelegt haben, stellen Sie sicher, dass er die Anzeige nicht unterdrückt. Siehe [Anpassung]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=swift).
  {% when "Android" %}
4. Wenn Sie einen Delegaten zum Anpassen der Handhabung von In-App-Nachrichten festgelegt haben, stellen Sie sicher, dass er die Anzeige nicht unterdrückt. Siehe [Anpassung]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android).
  {% when "Web" %}
4. Wenn Sie eine angepasste Handhabung von In-App-Nachrichten über [`braze.subscribeToInAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) verwenden, stellen Sie sicher, dass der Callback die Anzeige nicht unterdrückt. Siehe [Anpassung]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=web).
{% endcase %}
{% case include.sdk %}
  {% when "iOS", "Android" %}
5. Wenn die Ausrichtung des Geräts nicht mit der Einstellung der In-App-Nachricht übereinstimmt, wird die Nachricht nicht angezeigt.
{% endcase %}
{% case include.sdk %}
  {% when "iOS", "Android" %}
6. Je nach Netzwerkbedingungen werden Bilder möglicherweise vor der Anzeige heruntergeladen. Bei langsamen Verbindungen oder leistungsschwachen Geräten sollten Sie zusätzliche Zeit einplanen oder die Asset-Größe optimieren.
{% endcase %}

{% if include.sdk == "iOS" %}
### Impressionen und Klicks werden nicht protokolliert {#impressions-and-clicks-arent-being-logged}

Wenn Sie einen Delegaten für In-App-Nachrichten so eingestellt haben, dass er die Anzeige von Nachrichten oder Klickaktionen manuell steuert, müssen Sie [Klicks](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logclick(buttonid:using:)) und [Impressionen](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logimpression(using:)) für die In-App-Nachricht manuell protokollieren.
{% elsif include.sdk == "Android" %}
### Impressionen und Klicks werden nicht protokolliert

Wenn Sie einen Delegaten für In-App-Nachrichten so eingestellt haben, dass er die Anzeige von Nachrichten oder Klickaktionen manuell steuert, müssen Sie Klicks und Impressionen für die In-App-Nachricht manuell protokollieren.
{% endif %}