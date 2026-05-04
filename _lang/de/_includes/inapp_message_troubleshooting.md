## Grundlegende Checks {#basic-checks}

### Meine In-App-Nachricht wurde bei einer Person nicht angezeigt {#my-in-app-message-wasnt-shown-for-one-user}

1. War die Person zu Beginn der Sitzung im Segment, als das SDK neue In-App-Nachrichten anforderte?
2. War die Person berechtigt oder erneut berechtigt, die In-App-Nachricht gemäß den Targeting-Regeln der Campaign zu erhalten?
3. War die Person von einer Frequenzbegrenzung betroffen?
4. War die Person in einer Kontrollgruppe? Prüfen Sie, ob Ihre Campaign für AB-Tests konfiguriert ist.
5. Wurde eine andere In-App-Nachricht mit höherer Priorität anstelle der erwarteten Nachricht angezeigt?
6. War mein Gerät in der von der Campaign vorgegebenen Ausrichtung?
7. Wurde meine Nachricht durch das standardmäßige 30-Sekunden-Mindestzeitintervall zwischen Triggern unterdrückt, das vom SDK erzwungen wird?

### Meine In-App-Nachricht wurde nicht allen Nutzer:innen auf dieser Plattform angezeigt {#my-in-app-message-wasnt-shown-to-all-users-on-this-platform}

1. Ist Ihre Campaign so konfiguriert, dass sie entweder auf mobile Apps oder Webbrowser abzielt? Wenn Ihre Campaign zum Beispiel nur auf Webbrowser abzielt, wird sie nicht an Android-Geräte gesendet.
2. Haben Sie eine angepasste UI implementiert, und funktioniert sie wie gewünscht? Gibt es eine andere app-seitige angepasste Behandlung oder Unterdrückung, die die Anzeige stören könnte?
3. Hat diese bestimmte Plattform und App-Version jemals erfolgreich In-App-Nachrichten angezeigt?
4. Fand der Trigger lokal auf dem Gerät statt? Beachten Sie, dass ein REST-Aufruf nicht verwendet werden kann, um eine In-App-Nachricht im SDK zu triggern.

### Meine In-App-Nachricht wurde nicht für alle Nutzer:innen angezeigt {#my-in-app-message-wasnt-shown-for-all-users}

1. Wurde die Trigger-Aktion sowohl im Dashboard als auch in der App-Integration richtig eingerichtet?
2. Wurde eine andere In-App-Nachricht mit höherer Priorität anstelle der erwarteten Nachricht angezeigt?
3. Verwenden Sie eine aktuelle Version des SDK? Für einige Arten von In-App-Nachrichten gelten SDK-Versionsanforderungen.
4. Wurden die Sitzungen in Ihrer Integration ordnungsgemäß integriert? Funktionieren die Sitzungs-Analytics für diese App?
5. Verwenden Sie eine angepasste Komponentenbibliothek, die die Anzeige von In-App-Nachrichten beeinträchtigen könnte?

### Meine In-App-Nachricht hat sehr lange gebraucht, um zu erscheinen {#my-in-app-message-took-a-lot-of-time-to-appear}

1. Wenn Sie große Bild- oder Videodateien von Ihrem CDN an eine HTML-basierte In-App-Nachricht senden, stellen Sie sicher, dass Ihre Dateien so klein wie möglich optimiert sind und dass Ihr CDN leistungsfähig ist.
2. Überprüfen Sie, ob Sie eine `delay` für Ihre In-App-Nachricht im Dashboard konfiguriert haben.
{% case include.sdk %}
  {% when "iOS", "Android" %}
3. Je nach Umständen laden In-App-Nachrichten die entsprechenden Bilder vor der Anzeige entweder herunter oder laden sie von der Festplatte. Wenn Sie über eine langsame Netzwerkverbindung oder ein sehr leistungsschwaches Gerät verfügen, kann dieser Vorgang einige Zeit dauern. Achten Sie darauf, dass Ihre Bilder so klein wie möglich optimiert sind.
{% endcase %}

Eine ausführlichere Diskussion dieser Szenarien finden Sie im <a id="troubleshooting-in-app-advanced">Abschnitt zur erweiterten Fehlerbehebung</a>.

## Probleme mit Impressionen und Klick-Analytics {#issues-with-impressions-and-click-analytics}

{% if include.sdk == "iOS" %}
### Impressionen und Klicks werden nicht protokolliert {#impressions-and-clicks-arent-being-logged}

Wenn Sie einen Delegaten für In-App-Nachrichten so eingestellt haben, dass er die Anzeige von Nachrichten oder Klickaktionen manuell steuert, müssen Sie [Klicks](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logclick(buttonid:using:)) und [Impressionen](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logimpression(using:)) auf der In-App-Nachricht manuell protokollieren.
{% elsif include.sdk == "Android" %}
### Impressionen und Klicks werden nicht protokolliert {#impressions-and-clicks-arent-being-logged}
Wenn Sie einen Delegaten für In-App-Nachrichten so eingestellt haben, dass er die Anzeige von Nachrichten oder Klickaktionen manuell steuert, müssen Sie Klicks und Impressionen auf der In-App-Nachricht manuell protokollieren.
{% endif %}

### *Impressionen* sind größer als *Eindeutige Impressionen* {#impressions-are-greater-than-unique-impressions}

Das ist erwartetes Verhalten und kann in folgenden Fällen auftreten:

- Auch wenn die erneute Berechtigung deaktiviert ist, können Nutzer:innen, die die Campaign erhalten haben, mehr als ein Gerät besitzen. Der Campaign-Trigger wird beim nächsten Sitzungsstart aktualisiert, sodass ein Gerät nicht weiß, ob ein anderes Gerät die Campaign bereits getriggert hat, bis eine neue Sitzung gestartet wird.
- Wenn Ihre In-App-Nachricht eine geplante Verzögerung von einigen Minuten nach dem Trigger-Event hat, können Nutzer:innen die Nachricht mehr als einmal erhalten haben.

Weitere Informationen zur erneuten Berechtigung finden Sie unter [Erneute Berechtigung für Campaigns und Canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/).

### Impressionen sind niedriger als erwartet {#impressions-are-lower-than-expected}

1. Die Synchronisierung der Trigger mit dem Gerät beim Sitzungsstart nimmt einige Zeit in Anspruch, sodass es zu einer Race-Condition kommen kann, wenn Nutzer:innen ein Event oder einen Kauf direkt nach dem Start einer Sitzung protokollieren. Ein möglicher Workaround könnte darin bestehen, die Campaign so zu ändern, dass sie beim Sitzungsstart getriggert wird, und dann nach dem beabsichtigten Event oder Kauf zu segmentieren. Beachten Sie, dass dies die In-App-Nachricht beim nächsten Sitzungsstart nach Eintreten des Events zustellen würde.

2. Wenn die Campaign durch einen Sitzungsstart oder ein angepasstes Event getriggert wird, sollten Sie sicherstellen, dass dieses Event oder diese Sitzung häufig genug stattfindet, um die Nachricht zu triggern. Überprüfen Sie diese Daten auf den Seiten [Übersicht]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#understanding-your-app-usage-data) (für Sitzungsdaten) oder [Angepasste Events]({{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting):

![Die Seite „Angepasste Events“ zeigt in einem Diagramm, wie oft das angepasste Event „Zu den Favoriten hinzugefügt“ in einem Monat aufgetreten ist.]({% image_buster /assets/img_archive/trouble5.png %})

Weitere Gründe sind:

- Nutzer:innen haben die In-App-Nachricht nicht gesehen, sodass keine Impressionen protokolliert werden.
- Mehrere In-App-Nachrichten blockieren sich gegenseitig (z. B. mehrere Nachrichten mit hoher Priorität).
- Wenn sich die Nachricht in einem Canvas befindet, durchlaufen Nutzer:innen möglicherweise einen Verzögerungsschritt, der länger als das Sitzungs-Timeout ist, bevor sie die In-App-Nachricht erhalten.

### Impressionen sind niedriger als früher {#impressions-are-lower-than-they-used-to-be}

1. Stellen Sie sicher, dass niemand das Segment oder die Campaign seit dem Start unbeabsichtigt verändert hat. Unsere Changelogs für Segmente und Campaigns geben Ihnen Einblick in die Änderungen, die vorgenommen wurden, wer die Änderung vorgenommen hat und wann sie erfolgt ist.

![Link zur Anzeige des Changelogs auf der Seite „Campaign-Details“ mit sieben Änderungen seit der letzten Ansicht der Campaign]({% image_buster /assets/img_archive/trouble4.png %})

{: start="2"}
2. Stellen Sie sicher, dass Sie Ihr Trigger-Event nicht in einer separaten In-App-Nachrichten-Campaign mit höherer Priorität wiederverwendet haben.

## Erweiterte Fehlerbehebung {#troubleshooting-in-app-advanced}

Die meisten Probleme mit In-App-Nachrichten lassen sich in zwei Hauptkategorien unterteilen: Zustellung und Anzeige. Um herauszufinden, warum eine erwartete In-App-Nachricht nicht auf Ihrem Gerät angezeigt wurde, bestätigen Sie zunächst, dass die <a id="troubleshooting-in-app-message-delivery">In-App-Nachricht an das Gerät zugestellt wurde</a>, und führen Sie dann die <a id="troubleshooting-in-app-message-display">Fehlerbehebung für die Anzeige</a> durch.

### Fehlerbehebung bei der Zustellung {#troubleshooting-in-app-message-delivery}

Das SDK fordert beim Sitzungsstart In-App-Nachrichten von den Braze-Servern an. Um zu überprüfen, ob In-App-Nachrichten an Ihr Gerät zugestellt werden, müssen Sie sicherstellen, dass In-App-Nachrichten sowohl vom SDK angefordert als auch von den Braze-Servern zurückgegeben werden.

#### Prüfen, ob Nachrichten angefordert und zurückgegeben werden {#check-if-messages-are-requested-and-returned}

1. Fügen Sie sich als [Testnutzer:in]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users) im Dashboard hinzu.
2. Richten Sie eine In-App-Nachrichten-Campaign ein, die auf Sie als Nutzer:in abzielt.
3. Stellen Sie sicher, dass in Ihrer Anwendung eine neue Sitzung stattfindet.
4. Überprüfen Sie anhand der [Event-Nutzerprotokolle]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab), ob Ihr Gerät beim Sitzungsstart In-App-Nachrichten anfordert. Suchen Sie die SDK-Anfrage, die mit dem Sitzungsstart-Event Ihrer Testperson verknüpft ist.
  - Wenn Ihre App getriggerte In-App-Nachrichten anfordern sollte, sollten Sie `trigger` im Feld **Requested Responses** unter **Response Data** sehen.
  - Wenn Ihre App originale In-App-Nachrichten anfordern sollte, sollten Sie `in_app` im Feld **Requested Responses** unter **Response Data** sehen.
5. Überprüfen Sie anhand der [Event-Nutzerprotokolle]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab), ob die korrekten In-App-Nachrichten in den Antwortdaten zurückgegeben werden.<br>![]({% image_buster /assets/img_archive/event_user_log_iams.png %})

##### Fehlerbehebung bei nicht angeforderten Nachrichten {#troubleshoot-messages-not-being-requested}

Wenn Ihre In-App-Nachrichten nicht angefordert werden, verfolgt Ihre App möglicherweise die Sitzungen nicht korrekt, da In-App-Nachrichten beim Sitzungsstart aktualisiert werden. Vergewissern Sie sich außerdem, dass Ihre App tatsächlich eine Sitzung gemäß der Sitzungs-Timeout-Semantik Ihrer App startet:

![Die SDK-Anfrage in den Event-Nutzerprotokollen zeigt ein erfolgreiches Sitzungsstart-Event an.]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

##### Fehlerbehebung bei nicht zurückgegebenen Nachrichten {#troubleshoot-messages-not-being-returned}

Wenn Ihre In-App-Nachrichten nicht zurückgegeben werden, liegt wahrscheinlich ein Problem mit dem Targeting Ihrer Campaign vor:

1. Ihr Segment enthält Ihre Person nicht.
  - Überprüfen Sie den Tab [**Engagement**]({{ site.baseurl }}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) der Person, um sicherzustellen, dass das korrekte Segment unter **Segments** angezeigt wird.
2. Die Person hat die In-App-Nachricht bereits erhalten und war nicht erneut berechtigt, sie zu erhalten.
  - Überprüfen Sie die [Einstellungen für die erneute Berechtigung der Campaign]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/) im Schritt **Delivery** des **Campaign Composers** und stellen Sie sicher, dass die Einstellungen für die erneute Berechtigung mit Ihrer Testkonfiguration übereinstimmen.
3. Die Person hat die Frequenzbegrenzung für die Campaign erreicht.
  - Überprüfen Sie die [Frequency-Capping-Einstellungen]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) der Campaign und stellen Sie sicher, dass diese mit Ihrer Testkonfiguration übereinstimmen.
4. Wenn es in der Campaign eine Kontrollgruppe gab, könnte die Person in die Kontrollgruppe gefallen sein.
  - Sie können überprüfen, ob dies geschehen ist, indem Sie ein Segment mit einem Filter für empfangene Kampagnenvarianten erstellen, bei dem die Kampagnenvariante auf **Control** eingestellt ist, und prüfen, ob die Person in dieses Segment fällt.
  - Wenn Sie Campaigns für Integrationstests erstellen, achten Sie darauf, keine Kontrollgruppe hinzuzufügen.


### Fehlerbehebung bei der Anzeige {#troubleshooting-in-app-message-display}

Wenn Ihre App erfolgreich In-App-Nachrichten anfordert und empfängt, diese aber nicht angezeigt werden, kann die geräteseitige Logik die Anzeige verhindern:

1. Wird das Trigger-Event wie erwartet ausgelöst? Um dies zu testen, konfigurieren Sie die Nachricht so, dass sie durch eine andere Aktion (z. B. Sitzungsstart) getriggert wird, und überprüfen Sie, ob sie angezeigt wird.
{% if include.sdk == "iOS" %}
2. Getriggerte In-App-Nachrichten werden auf Basis des [minimalen Zeitintervalls zwischen Triggern]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers) begrenzt, das standardmäßig 30 Sekunden beträgt.
{% elsif include.sdk == "Android" %}
2. Getriggerte In-App-Nachrichten werden auf Basis des [minimalen Zeitintervalls zwischen Triggern]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers) begrenzt, das standardmäßig 30 Sekunden beträgt.
{% elsif include.sdk == "Web" %}
2. Getriggerte In-App-Nachrichten werden auf Basis des [minimalen Zeitintervalls zwischen Triggern]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers) begrenzt, das standardmäßig 30 Sekunden beträgt.
{% endif %}
3. Fehlgeschlagene Bild-Downloads verhindern die Anzeige von In-App-Nachrichten mit Bildern. Überprüfen Sie Ihre Geräteprotokolle, um sicherzustellen, dass Bild-Downloads nicht fehlschlagen. Versuchen Sie, Ihr Bild vorübergehend aus Ihrer Nachricht zu entfernen, um zu sehen, ob sie dann angezeigt wird.
{% case include.sdk %}
  {% when "iOS", "Android" %}
4. Wenn Sie einen Delegaten zum Anpassen der Handhabung von In-App-Nachrichten festgelegt haben, überprüfen Sie Ihren Delegaten, um sicherzustellen, dass er die Anzeige der In-App-Nachrichten nicht beeinträchtigt.
  {% when "Web" %}
5. Wenn Sie eine angepasste Handhabung von In-App-Nachrichten über `braze.subscribeToInAppMessage` oder `appboy.subscribeToNewInAppMessages` verwenden, überprüfen Sie dieses Abonnement, um sicherzustellen, dass es die Anzeige von In-App-Nachrichten nicht beeinträchtigt.
{% endcase %}
{% case include.sdk %}
  {% when "iOS", "Android" %}
6. Wenn die Ausrichtung des Geräts nicht mit der von der In-App-Nachricht angegebenen Ausrichtung übereinstimmt, wird die In-App-Nachricht nicht angezeigt. Vergewissern Sie sich, dass Ihr Gerät die richtige Ausrichtung hat.
{% endcase %}
7. Wenn Ihre In-App-Nachricht durch den Sitzungsstart getriggert wird und Sie ein verlängertes Sitzungs-Timeout eingestellt haben, wirkt sich dies darauf aus, wie schnell Sie Nachrichten anzeigen können. Wenn Ihr Sitzungs-Timeout beispielsweise auf 300 Sekunden eingestellt ist, wird die Sitzung durch Schließen und erneutes Öffnen der App in weniger als dieser Zeit nicht aktualisiert, sodass eine durch einen Sitzungsstart getriggerte In-App-Nachricht nicht angezeigt wird.