---
nav_title: Fehlerbehebung
article_title: Fehlerbehebung für In-App-Nachrichten im Braze SDK
page_order: 50
description: "Diagnostizieren Sie, warum In-App-Nachrichten nicht zugestellt oder angezeigt werden, mithilfe eines Symptomindex, eines standardisierten Untersuchungspfads, Canvas-IAM-Hinweisen und plattformspezifischen SDK-Prüfungen."
channel:
  - in-app messages

---

# Fehlerbehebung für In-App-Nachrichten {#troubleshoot-in-app-messages}

> Verwenden Sie diese Seite, um zu diagnostizieren, warum In-App-Nachrichten nicht zugestellt oder auf einem Gerät angezeigt werden. Informationen zur Dashboard-Einrichtung (Priorität, Trigger, Segmente und Wiederberechtigung) finden Sie in den [FAQ zu In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).

Bevor Sie mit dem Debugging beginnen, fügen Sie sich als [Testnutzer:in]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users) hinzu und lesen Sie [Testnachrichten senden]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages).

## Hier starten: Symptom zuordnen {#start-here-match-your-symptom}

| Symptom | Gehe zu |
| --- | --- |
| In-App-Nachricht wurde für eine:n Nutzer:in nicht angezeigt | [Eine:r Nutzer:in](#in-app-message-not-shown-for-one-user) |
| In-App-Nachricht wurde auf einer Plattform nicht angezeigt (Android, iOS oder Web) | [Eine Plattform](#in-app-message-not-shown-on-one-platform) |
| In-App-Nachricht aus einem **Canvas**-Schritt wurde nicht angezeigt | [Canvas-In-App-Nachrichten](#canvas-in-app-messages) |
| In-App-Nachricht wurde verspätet oder nach einer Verzögerung angezeigt | [Timing und verzögerte Anzeige](#timing-and-delayed-display) |
| Impressionen oder Klicks sehen falsch aus | [Impressionen und Analytics](#impressions-and-analytics) |
| `triggers` fehlen oder sind leer in den Event-Nutzerprotokollen | [Fehlerbehebung bei der Zustellung](#delivery-troubleshooting) |
| Trigger wurden zurückgegeben, aber nichts wird auf dem Gerät angezeigt | [Plattformspezifische Fehlerbehebung bei der Anzeige](#platform-specific-display-troubleshooting) |
| In-App-Nachrichten-Assets können nicht geladen werden (iOS, `NSURLError` -1008) | [Asset-Laden (Swift-Tab)](?sdktab=swift#swift_asset-loading) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Symptom für In-App-Nachrichten" }

## Standardisierter Untersuchungspfad {#standard-investigation-path}

Verwenden Sie diesen Workflow für jeden Vorfall. Beginnen Sie bei Schritt 1.

1. Bestätigen Sie, dass ein **Sitzungsstart** für das Testgerät protokolliert wird. In-App-Nachrichten werden beim Sitzungsstart angefordert.
2. Öffnen Sie die [Event-Nutzerprotokolle]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log) und suchen Sie die SDK-Anfrage für diesen Sitzungsstart. In den **Antwortdaten**:
   - Bestätigen Sie im Roh-JSON, dass `respond_with` `"triggers": true` enthält.
   - Die Zeile **Requested Responses** sollte **`triggers`** enthalten.
   - **Trigger In-App Message**-Zeilen listen jede In-App-Nachricht auf, die für diese Anfrage zurückgegeben wurde.
   - Wenn kein `triggers`-Schlüssel oder keine **Trigger In-App Message**-Zeilen vorhanden sind, gehen Sie zu [Fehlerbehebung: Nachrichten werden nicht angefordert](#troubleshoot-messages-not-being-requested).
   - Wenn `triggers` vorhanden, aber leer ist (`[]`), gehen Sie zu [Fehlerbehebung: Nachrichten werden nicht zurückgegeben](#troubleshoot-messages-not-being-returned).
   - Wenn **Trigger In-App Message**-Zeilen vorhanden sind, aber nichts angezeigt wird, gehen Sie zu [Plattformspezifische Fehlerbehebung bei der Anzeige](#platform-specific-display-troubleshooting).
   - Jeder Trigger-Payload enthält einen `type`: `inapp` (Standard) oder `templated_iam` (erfordert eine Template-Anfrage vor der Anzeige). Siehe [Typen von In-App-Nachrichten]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#types-of-in-app-messages).
3. Informationen zur Dashboard-seitigen Berechtigung (Segment, Wiederberechtigung, Frequency Caps, Priorität, Kontrollgruppen) finden Sie unter [Fehlerbehebung bei der Zustellung](#delivery-troubleshooting) und in den [FAQ zu In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).
4. Bei geräteseitigen Anzeigeproblemen (Delegates, Rate-Limits, Ausrichtung, Sitzungs-Timeout) wählen Sie Ihren SDK-Tab unter [Plattformspezifische Fehlerbehebung bei der Anzeige](#platform-specific-display-troubleshooting).

## Canvas-In-App-Nachrichten {#canvas-in-app-messages}

**Symptom:** Ein:e Nutzer:in ist in einen Canvas-In-App-Nachrichten-Schritt eingetreten, hat die Nachricht aber nicht wie erwartet gesehen.

Drei Verhaltensweisen verursachen die meisten Canvas- und In-App-Nachrichten-Tickets:

1. **Anzeige bei nächster Sitzung:** Canvas-In-App-Nachrichten sind beim *nächsten* Sitzungsstart berechtigt, nachdem der Schritt verarbeitet wurde – nicht sofort mitten in der Sitzung. Siehe [Wann werden In-App-Nachrichten in Canvas gesendet?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#when-are-in-app-messages-in-canvas-sent) in den Canvas-FAQ.
2. **Zustellungsvalidierungen beim Schritteintritt:** Wenn **Zielgruppe beim Nachrichtenversand validieren** im Nachrichten-Schritt aktiviert ist, werden Segmentzugehörigkeit und Frequency Caps ausgewertet, wenn der/die Nutzer:in **in den Schritt eintritt**, nicht zum Anzeigezeitpunkt. Siehe [Zustellungsvalidierungen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations).
3. **Verzögerung und Sitzungs-Timeout:** Wenn ein:e Nutzer:in in einen Verzögerungsschritt eintritt, der länger als Ihr SDK-Sitzungs-Timeout ist, kann eine neue Sitzung beginnen, bevor der In-App-Nachrichten-Schritt erreicht wird. Die Nachricht wird möglicherweise nicht beim Sitzungsstart abgerufen, wenn Sie erwarten, dass sie angezeigt wird.

Informationen zu Verfügbarkeitsfenstern, Ablauf und null _Sends_ in Canvas-Analytics finden Sie unter [In-App-Nachrichten und Zustellung]({{site.baseurl}}/user_guide/messaging/canvas/faqs#messages-and-delivery) in den Canvas-FAQ.

{% alert important %}
In-App-Nachrichten in Canvas können nur durch Ereignisse getriggert werden, die über das SDK gesendet werden, nicht über die REST API.
{% endalert %}

## In-App-Nachricht wurde für eine:n Nutzer:in nicht angezeigt {#in-app-message-not-shown-for-one-user}

**Symptom:** Ein:e Nutzer:in hat eine erwartete In-App-Nachricht nicht erhalten; andere Nutzer:innen sind möglicherweise nicht betroffen.

Überprüfen Sie Folgendes:

- War der/die Nutzer:in beim **Sitzungsstart** im Segment, wenn das SDK neue In-App-Nachrichten anfordert?
- War der/die Nutzer:in gemäß den Targeting-Regeln der Campaign oder des Canvas berechtigt oder wiederberechtigt? Siehe [Wiederberechtigung für Campaigns und Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).
- Galt ein [Frequency Cap]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping)?
- War der/die Nutzer:in in einer Campaign-Kontrollgruppe? Prüfen Sie, ob die Campaign für A/B-Tests konfiguriert ist.
- Wurde stattdessen eine In-App-Nachricht mit höherer Priorität angezeigt? Siehe [Können mehrere In-App-Nachrichten in derselben Sitzung angezeigt werden?]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#can-multiple-in-app-messages-display-in-the-same-session) in den FAQ zu In-App-Nachrichten.
- War das Gerät in der von der Campaign angegebenen Ausrichtung?
- Wurde die Nachricht durch das standardmäßige Mindestintervall von 30 Sekunden zwischen Triggern unterdrückt? Siehe [Überschreiben des Standard-Rate-Limits]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#overriding-the-default-rate-limit).

Folgen Sie dann dem [standardisierten Untersuchungspfad](#standard-investigation-path).

## In-App-Nachricht wurde auf einer Plattform nicht angezeigt {#in-app-message-not-shown-on-one-platform}

**Symptom:** In-App-Nachrichten werden auf Android, iOS oder Web nicht angezeigt, funktionieren aber möglicherweise auf anderen Plattformen.

| Wahrscheinliche Ursache | Was zu prüfen ist |
| --- | --- |
| Falsches **Senden an**-Ziel | Bestätigen Sie, dass die Campaign oder der Canvas-Schritt entsprechend auf **Mobile Apps** oder **Web Browsers** ausgerichtet ist. Eine reine Web-Campaign wird nicht an Android-Geräte gesendet. |
| Angepasste UI oder Handler unterdrückt die Anzeige | Überprüfen Sie Delegates (Mobilgerät) oder [`braze.subscribeToInAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) (Web). Siehe [Anpassung]({{site.baseurl}}/developer_guide/in_app_messages/customization) und Ihren SDK-Tab für Ihre Plattform. |
| Integration hat auf dieser Plattform nie funktioniert | Bestätigen Sie, dass diese Plattform und App-Version zuvor In-App-Nachrichten angezeigt haben. |
| Trigger wurde auf dem Gerät nicht ausgelöst | Der Trigger muss lokal über das SDK erfolgen. Ein REST-API-Aufruf kann keine In-App-Nachricht im SDK triggern. Siehe [Nachrichten triggern]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages). |
| Leere `triggers` in den Event-Nutzerprotokollen | Segment, Wiederberechtigung, Frequency Cap oder Kontrollgruppe. Siehe [Fehlerbehebung: Nachrichten werden nicht zurückgegeben](#troubleshoot-messages-not-being-returned). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Plattform-Symptom-Ursache" }

## In-App-Nachricht wurde für alle Nutzer:innen nicht angezeigt {#in-app-message-not-shown-for-all-users}

**Symptom:** Keine oder weniger Nutzer:innen als erwartet haben die In-App-Nachricht erhalten.

Überprüfen Sie Folgendes:

- Ist die Trigger-Aktion im Dashboard und in der App-Integration korrekt konfiguriert?
- Hat eine In-App-Nachricht mit höherer Priorität die Campaign abgefangen? Siehe die [FAQ zu In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#can-multiple-in-app-messages-display-in-the-same-session).
- Verwenden Sie eine aktuelle SDK-Version? Einige In-App-Nachrichtentypen haben Mindestanforderungen an die SDK-Version.
- Sind Sitzungen korrekt integriert? Bestätigen Sie, dass die Sitzungs-Analytics für diese App funktionieren.
- Stört eine angepasste UI-Bibliothek die Anzeige? Siehe [Anpassung]({{site.baseurl}}/developer_guide/in_app_messages/customization).

Folgen Sie dann dem [standardisierten Untersuchungspfad](#standard-investigation-path).

## Timing und verzögerte Anzeige {#timing-and-delayed-display}

**Symptom:** Die In-App-Nachricht erschien später als erwartet oder erst bei einer neuen Sitzung.

Häufige Ursachen:

- **Sitzungsstart-Prefetch der Campaign:** In-App-Nachrichten werden beim Sitzungsstart zwischengespeichert und angezeigt, wenn der Trigger ausgelöst wird. Ein Trigger, der vor dem nächsten Sitzungsstart auftritt, wird erst in dieser Sitzung angezeigt. Siehe [Nachrichten triggern]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages).
- **Canvas-Verhalten bei nächster Sitzung:** Siehe [Canvas-In-App-Nachrichten](#canvas-in-app-messages).
- **Geplante Dashboard-Verzögerung:** Prüfen Sie, ob eine Verzögerung für die Campaign oder den Schritt konfiguriert ist.
- **Trigger-Synchronisierungs-Race-Condition:** Wenn Nutzer:innen ein Ereignis unmittelbar nach dem Sitzungsstart protokollieren, sind die Trigger möglicherweise noch nicht synchronisiert. Erwägen Sie, den Trigger auf den Sitzungsstart zu setzen und nach dem beabsichtigten Ereignis zu segmentieren, damit die Zustellung in der nächsten Sitzung nach dem Ereignis erfolgt.
- **Sequenzielle In-App-Nachrichten:** Wenn Sie Nachrichten in einer Tour zurückstellen oder wiederherstellen, siehe [Getriggerte In-App-Nachrichten zurückstellen]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages).
- **Große Assets oder langsames CDN:** Optimieren Sie Bilder und Videos für HTML-In-App-Nachrichten. Auf Mobilgeräten können Bilder bei langsamen Netzwerken vor der Anzeige heruntergeladen werden – wählen Sie Ihren SDK-Tab für plattformspezifische Hinweise.

{% alert note %}
Wenn Ihre In-App-Nachricht durch den Sitzungsstart getriggert wird und Sie ein verlängertes Sitzungs-Timeout festgelegt haben, wird das Schließen und erneute Öffnen der App innerhalb dieses Zeitfensters die Sitzung nicht aktualisieren. Beispiel: Bei einem 300-Sekunden-Timeout wird eine Sitzungsstart-In-App-Nachricht erst angezeigt, wenn die Sitzung tatsächlich aktualisiert wird. Passen Sie das Sitzungs-Timeout oder den Trigger-Typ an, wenn dies Ihren Test beeinflusst.
{% endalert %}

## Fehlerbehebung bei der Zustellung {#delivery-troubleshooting}

Die meisten Probleme mit In-App-Nachrichten betreffen die **Zustellung** (das Gerät hat keine Trigger erhalten) oder die **Anzeige** (Trigger sind angekommen, wurden aber nicht angezeigt). Bestätigen Sie zuerst die [Zustellung](#troubleshooting-in-app-message-delivery) und prüfen Sie dann die [Anzeige](#platform-specific-display-troubleshooting).

### Fehlerbehebung bei der Zustellung {#troubleshooting-in-app-message-delivery}

Das SDK fordert In-App-Nachrichten beim Sitzungsstart von den Braze-Servern an. Bestätigen Sie, dass das SDK Trigger anfordert und Braze diese zurückgibt.

#### Prüfen, ob Nachrichten angefordert und zurückgegeben werden {#check-if-messages-are-requested-and-returned}

1. Fügen Sie sich als [Testnutzer:in]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users) hinzu.
2. Richten Sie eine In-App-Nachrichten-Campaign ein, die auf Ihre:n Nutzer:in ausgerichtet ist.
3. Starten Sie eine neue Sitzung in Ihrer Anwendung.
4. Suchen Sie in den [Event-Nutzerprotokollen]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log) die SDK-Anfrage für das Sitzungsstart-Ereignis. In den **Antwortdaten**:
   - Bestätigen Sie im Roh-JSON, dass `respond_with` `"triggers": true` enthält.
   - Die Zeile **Requested Responses** listet die Top-Level-Schlüssel in der Antwort auf. Für In-App-Nachrichten erwarten Sie **`triggers`**.
   - **Trigger In-App Message**-Zeilen listen jede In-App-Nachricht auf, die für diese Anfrage zurückgegeben wurde.

   Dann triagieren:
   - Wenn kein `triggers`-Schlüssel oder keine **Trigger In-App Message**-Zeilen vorhanden sind, siehe [Fehlerbehebung: Nachrichten werden nicht angefordert](#troubleshoot-messages-not-being-requested).
   - Wenn `triggers` vorhanden, aber leer ist (`[]`), siehe [Fehlerbehebung: Nachrichten werden nicht zurückgegeben](#troubleshoot-messages-not-being-returned).
   - Wenn **Trigger In-App Message**-Zeilen vorhanden sind, aber nichts auf dem Gerät angezeigt wird, siehe [Plattformspezifische Fehlerbehebung bei der Anzeige](#platform-specific-display-troubleshooting).
   - Jeder Trigger-Payload enthält einen `type`: `inapp` (Standard) oder `templated_iam` (erfordert eine Template-Anfrage vor der Anzeige). Siehe [Typen von In-App-Nachrichten]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#types-of-in-app-messages).
5. Bestätigen Sie, dass die richtigen In-App-Nachrichten in den Antwortdaten erscheinen.

![Event-Nutzerprotokoll mit SDK-Anfragen und Antwortdaten.]({% image_buster /assets/img_archive/event_user_log_iams.png %})

##### Fehlerbehebung: Nachrichten werden nicht angefordert {#troubleshoot-messages-not-being-requested}

Wenn In-App-Nachrichten nicht angefordert werden, verfolgt Ihre App möglicherweise Sitzungen nicht korrekt – In-App-Nachrichten werden beim Sitzungsstart aktualisiert. Bestätigen Sie, dass die App eine Sitzung basierend auf Ihrer Sitzungs-Timeout-Semantik startet:

![Die SDK-Anfrage in den Event-Nutzerprotokollen, die ein erfolgreiches Sitzungsstart-Ereignis anzeigt.]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

##### Fehlerbehebung: Nachrichten werden nicht zurückgegeben {#troubleshoot-messages-not-being-returned}

Wenn In-App-Nachrichten nicht zurückgegeben werden, liegt wahrscheinlich ein Targeting- oder Berechtigungsproblem vor:

1. Ihr Segment enthält Ihre:n Nutzer:in nicht.
   - Überprüfen Sie den Tab [**Engagement**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#engagement-tab) des/der Nutzer:in auf das erwartete Segment.
2. Ihr:e Nutzer:in hat die Nachricht bereits erhalten und war nicht wiederberechtigt.
   - Überprüfen Sie die [Wiederberechtigungseinstellungen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) und die [FAQ zu In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#campaigns).
3. Ihr:e Nutzer:in hat das Frequency Cap erreicht.
   - Überprüfen Sie die [Frequency-Cap-Einstellungen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).
4. Ihr:e Nutzer:in ist in eine Kontrollgruppe gefallen.
   - Erstellen Sie ein Segment mit einem Filter **Received campaign variant**, der auf **Control** gesetzt ist, oder deaktivieren Sie Kontrollgruppen während der Integrationstests.
5. Eine In-App-Nachricht mit höherer Priorität hatte Vorrang. Siehe die [FAQ zu In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#can-multiple-in-app-messages-display-in-the-same-session).

Informationen zu archivierten Campaigns, Trigger-Konfiguration und Ruhezeiten finden Sie in den [FAQ zu In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).

## Impressionen und Analytics {#impressions-and-analytics}

**Symptom:** Impressionen- oder Klickzahlen entsprechen nicht den Erwartungen.

- **_Impressionen_ größer als _Eindeutige Impressionen_:** Erwartet, wenn Nutzer:innen mehrere Geräte haben oder wenn eine geplante Verzögerung dazu führt, dass derselbe/dieselbe Nutzer:in sich mehr als einmal qualifiziert. Siehe [Wiederberechtigung für Campaigns und Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).
- **Impressionen niedriger als erwartet:** Nutzer:innen haben die Nachricht möglicherweise nicht gesehen (Impressionen werden bei der Anzeige protokolliert), mehrere Nachrichten mit hoher Priorität können sich gegenseitig abfangen, oder Trigger-Synchronisierungs-Race-Conditions können auftreten. Für Canvas-In-App-Nachrichten siehe [Canvas-In-App-Nachrichten](#canvas-in-app-messages). Vollständige Metrikdefinitionen finden Sie unter [Reporting für In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting) und in den [FAQ zu In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).
- **Impressionen niedriger als zuvor:** Überprüfen Sie die Segment- und Campaign-Changelogs. Bestätigen Sie, dass Sie nicht dasselbe Trigger-Ereignis in einer Campaign mit höherer Priorität wiederverwendet haben.

![Link zum Anzeigen des Changelogs auf der Campaign-Detailseite mit sieben Änderungen seit der letzten Ansicht der Campaign durch den/die Nutzer:in.]({% image_buster /assets/img_archive/trouble4.png %})

Wenn Sie einen Delegate oder angepassten Handler verwenden, um In-App-Nachrichten manuell anzuzeigen, müssen Sie Impressionen und Klicks selbst protokollieren. Siehe Ihren SDK-Tab unter [Plattformspezifische Fehlerbehebung bei der Anzeige](#platform-specific-display-troubleshooting) für Swift- und Android-Details oder [In-App-Nachrichtendaten protokollieren]({{site.baseurl}}/developer_guide/in_app_messages/logging_message_data) für Web.

## Plattformspezifische Fehlerbehebung bei der Anzeige {#platform-specific-display-troubleshooting}

Wenn **Trigger In-App Message**-Zeilen in den Event-Nutzerprotokollen erscheinen, aber nichts auf dem Gerät angezeigt wird, wählen Sie Ihren SDK-Tab für Anzeige-Prüfungen (Delegates, Rate-Limits, Ausrichtung und angepasste Handler).

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/in_app_messages/troubleshooting.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/in_app_messages/troubleshooting.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/in_app_messages/troubleshooting.md %}
{% endsdktab %}
{% endsdktabs %}