---
nav_title: FAQ
article_title: FAQ zu In-App-Nachrichten
page_order: 30
description: "Dieser Artikel enthält Antworten auf häufig gestellte Fragen zu In-App Messages."
tool: in-app messages

---

# Häufig gestellte Fragen {#frequently-asked-questions}

> Dieser Artikel enthält Antworten auf einige häufig gestellte Fragen zu In-App-Nachrichten.

### Was ist eine In-Browser-Nachricht und wie unterscheidet sie sich von einer In-App-Nachricht? {#what-is-an-in-browser-message-and-how-does-it-differ-from-an-in-app-message}

In-Browser-Nachrichten sind In-App-Nachrichten, die an Webbrowser gesendet werden. Um eine In-Browser-Nachricht zu erstellen, wählen Sie beim Erstellen Ihrer In-App-Nachricht-Campaign oder Ihres Canvas unter dem Feld **Send To** die Option **Web Browser** aus.

### Wird eine In-App-Nachricht angezeigt, wenn ein Gerät offline ist? {#will-an-in-app-message-display-if-a-device-is-offline}

Das kommt darauf an. Da In-App-Nachrichten beim Sitzungsstart zugestellt werden, kann das Gerät die Payload herunterladen, bevor es offline geht. In diesem Fall kann die In-App-Nachricht auch offline angezeigt werden. Wenn die Payload nicht heruntergeladen wurde, wird die In-App-Nachricht nicht angezeigt.

### Wenn ein:e Nutzer:in bereits eine In-App-Nachricht-Payload auf dem Gerät hat und das Ablaufdatum der Nachricht geändert wird, wird das Ablaufdatum auf dem Gerät aktualisiert? {#if-a-user-already-has-an-in-app-message-payload-on-their-device-and-the-message-expiration-is-changed-will-the-expiration-be-updated-on-their-device}

Wenn ein:e Nutzer:in eine Sitzung startet, prüft Braze, ob Änderungen an In-App-Nachrichten vorgenommen wurden, für die sie berechtigt sind, und aktualisiert diese entsprechend. Wenn sich also das Ablaufdatum geändert hat und eine Sitzung protokolliert wird, wird die In-App-Nachricht mit den aktualisierten Informationen an das Gerät gesendet.

### Wie richte ich Ruhezeiten für eine In-App-Nachricht-Campaign ein? {#how-do-i-set-up-quiet-hours-for-an-in-app-message-campaign}

Das Feature „Ruhezeiten“ ist für In-App-Nachricht-Campaigns nicht verfügbar. Dieses Feature wird verwendet, um zu verhindern, dass Nachrichten während bestimmter Stunden an Ihre Nutzer:innen gesendet werden. Bei In-App-Nachricht-Campaigns erhalten Ihre Nutzer:innen In-App-Nachrichten nur, wenn sie in der App aktiv sind.

Als Workaround zum Senden von In-App-Nachrichten zu einem bestimmten Zeitpunkt können Sie den folgenden Liquid-Beispielcode verwenden. Dieser ermöglicht es, die Nachricht abzubrechen, wenn die In-App-Nachricht nach 19:59 Uhr oder vor 8:00 Uhr in der angegebenen Zeitzone angezeigt wird.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 19 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}
MESSAGE HERE
```
{% endraw %}

### Können Nutzer:innen eine In-App-Nachricht erneut erhalten, nachdem sie sie geschlossen haben? {#can-users-receive-an-in-app-message-again-after-they-dismiss-it}

#### Campaigns {#campaigns}

Bei In-App-Nachricht-Campaigns können Sie Nutzer:innen erlauben, erneut für den Empfang der Campaign berechtigt zu werden, indem Sie die erneute Berechtigung in den **Zustellungs-Kontrollgruppen** aktivieren (**Nutzer:innen erlauben, erneut für den Empfang der Campaign berechtigt zu werden**). Wie schnell sie die Nachricht erneut erhalten können, hängt vom eingestellten Zeitfenster für die erneute Berechtigung ab und davon, wie Braze den vorherigen Versand erfasst hat. Weitere Informationen finden Sie unter [Erneute Berechtigung für Campaigns und Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility/) zum Campaign-Verhalten, einschließlich der Beziehung zwischen erneuter Berechtigung und Nachrichtenempfang.

Wenn die erneute Berechtigung deaktiviert ist, erhalten Nutzer:innen dieselbe Campaign in der Regel nicht erneut allein basierend auf den Qualifizierungskriterien, nachdem sie sie bereits erhalten haben.

#### Canvases {#canvases}

Bei In-App-Nachrichten, die aus einem Canvas gesendet werden, hängt es davon ab, ob ein:e Nutzer:in die Nachricht erneut sehen kann, von den Canvas-Eintrittskontrollen (z. B. ob Nutzer:innen den Canvas erneut betreten dürfen) und Ihrer Schritt-Konfiguration – nicht nur von den Campaign-Zustellungskontrollen.

### Wann wird die Berechtigung für eine In-App-Nachricht berechnet? {#when-is-eligibility-for-an-in-app-message-calculated}

Die Berechtigung für eine In-App-Nachricht wird zum Zeitpunkt der Zustellung berechnet. Wenn eine In-App-Nachricht für den Versand um 7:00 Uhr geplant ist, wird die Berechtigung für diese In-App-Nachricht um 7:00 Uhr geprüft.

Sobald die In-App-Nachricht angezeigt wird, hängt die Berechtigung davon ab, wann die In-App-Nachricht heruntergeladen und getriggert wurde.

### Warum liefert meine archivierte In-App-Nachricht-Campaign weiterhin In-App-Nachricht-Impressionen? {#why-is-my-archived-in-app-message-campaign-still-delivering-in-app-message-impressions}

Dies kann bei Nutzer:innen auftreten, die die Segmentkriterien erfüllt haben, als die In-App-Nachricht-Campaign aktiv war.

Um dies zu verhindern, wählen Sie während der Campaign-Einrichtung **Campaign-Berechtigung vor der Anzeige erneut prüfen** aus.

### Können mehrere In-App-Nachrichten in derselben Sitzung angezeigt werden? {#can-multiple-in-app-messages-display-in-the-same-session}

Ja, aber pro Auftreten eines [Trigger-Events]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/create/#choose-a-trigger) kann nur eine In-App-Nachricht angezeigt werden. Wenn mehrere In-App-Nachricht-Campaigns denselben Trigger teilen (z. B. Sitzungsstart), wird jedes Mal, wenn dieser Trigger auftritt, nur die Nachricht mit der höchsten Priorität angezeigt. Bei Sitzungsstart-Triggern bedeutet dies, dass pro Sitzung nur eine Nachricht angezeigt werden kann und die nächste Gelegenheit, eine weitere berechtigte Nachricht anzuzeigen, die nächste Sitzung ist.

Wenn mehrere Nachrichten dieselbe Prioritätsstufe teilen, wird die zuletzt erstellte Nachricht zuerst angezeigt. Bei Sitzungsstart-Triggern wird die nächstaktuellste Nachricht in einer nachfolgenden Sitzung angezeigt; bei anderen Trigger-Typen wird die nächstaktuellste Nachricht beim nächsten Auftreten dieses Trigger-Events angezeigt, was innerhalb derselben Sitzung oder in einer späteren Sitzung sein kann.

Um die Anzeigereihenfolge innerhalb einer Prioritätsstufe zu steuern, gehen Sie zu den Zustellungseinstellungen einer der Campaigns und wählen Sie **Genaue Priorität festlegen**. Ziehen Sie die Campaigns dann per Drag-and-Drop in die gewünschte Reihenfolge. Weitere Details finden Sie unter [Priorität wählen]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/create/#choose-a-priority).

### Wie berechnet Braze ein In-App-Nachricht-Ablaufdatum von „nach 1 Tag(en)“? {#how-does-braze-calculate-an-in-app-message-expiration-set-to-after-1-days}

Braze berechnet eine Ablaufzeit von einem Tag als 24 Stunden, nachdem Nutzer:innen berechtigt sind, eine Nachricht zu erhalten.

### Was sind vorlagenbasierte In-App-Nachrichten? {#what-are-templated-in-app-messages}

In-App-Nachrichten werden als vorlagenbasierte In-App-Nachrichten zugestellt, wenn **Campaign-Berechtigung vor der Anzeige erneut prüfen** ausgewählt ist oder wenn einer der folgenden Liquid-Tags in der Nachricht vorhanden ist:

- `canvas_entry_properties`
- `connected_content`
- SMS-Variablen wie {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Das bedeutet, dass das Gerät beim Sitzungsstart den Trigger dieser In-App-Nachricht erhält, nicht die gesamte Nachricht. Wenn der/die Nutzer:in die In-App-Nachricht triggert, stellt das Gerät eine Netzwerkanfrage, um die eigentliche Nachricht abzurufen.

{% alert note %}
Die Nachricht wird nicht zugestellt, wenn das Gerät keinen Internetzugang hat. Die Nachricht wird möglicherweise nicht zugestellt, wenn die Liquid-Logik zu lange für die Auflösung benötigt.
{% endalert %}

### Wie funktioniert das Abbruchverhalten bei In-App-Nachrichten? {#how-does-abort-behavior-work-for-in-app-messages}

Bei Braze tritt ein Abbruch auf, wenn ein:e Nutzer:in eine Aktion ausführt, die sie für den Empfang einer Nachricht berechtigt, die Nachricht aber nicht erhält, weil die Liquid-Logik sie als nicht berechtigt kennzeichnet. Zum Beispiel:

1. Sam führt eine Aktion aus, die eine E-Mail-Campaign triggern sollte.
2. Der E-Mail-Text enthält Liquid-Logik, die besagt: Wenn ein angepasstes Attribut „Score“ kleiner als 50 ist, soll diese E-Mail nicht gesendet werden.
3. Sams angepasstes Attribut „Score“ beträgt 20.
4. Braze erkennt, dass Sam diese E-Mail nicht erhalten sollte, und die E-Mail wird abgebrochen.
5. Ein Abbruch-Event wird protokolliert.

Da In-App-Nachrichten jedoch ein Pull-Kanal sind, funktionieren Abbrüche bei ihnen etwas anders.

#### Standard-Abbruchverhalten bei In-App-Nachrichten {#standard-in-app-message-abort-behavior}

In-App-Nachrichten werden beim Sitzungsstart vom Gerät abgerufen und auf dem Gerät zwischengespeichert, sodass die Nachricht unabhängig von der Internetverbindungsqualität sofort an den/die Nutzer:in zugestellt werden kann. Wenn ein:e Nutzer:in beispielsweise fünf In-App-Nachrichten innerhalb einer Sitzung erhält, werden alle fünf beim Sitzungsstart empfangen. Die Nachrichten werden lokal zwischengespeichert und erscheinen, wenn ihre definierten Trigger-Events auftreten (Sitzungsstart, Nutzer:in klickt auf einen Button, der ein angepasstes Event protokolliert, oder andere).

Mit anderen Worten: Die Logik, die bestimmt, ob eine In-App-Nachricht abgebrochen werden soll, wird **vor** dem Auftreten des Triggers ausgeführt. Um dies zu veranschaulichen, nehmen wir an, dass Sam aus dem E-Mail-Beispiel Push-Benachrichtigungen abonniert hat.

1. Sam startet eine Sitzung, indem er eine Braze-gestützte App auf seinem Telefon öffnet.
2. Basierend auf den Zielgruppenkriterien der aktiven Campaigns im Workspace könnte Sam für fünf verschiedene Campaigns berechtigt sein. Alle fünf werden auf sein Telefon geladen und zwischengespeichert.
3. Sam **hat keine** Aktionen ausgeführt, die diese Nachrichten triggern würden, könnte sie aber in der Sitzung erhalten.
4. Die Liquid-Logik in zwei der In-App-Nachrichten enthält Regeln, die Sam vom Empfang der Nachricht ausschließen (z. B. weil sein angepasstes Attribut „Score“ nicht hoch genug ist).
5. Sam erhält die beiden In-App-Nachrichten, die ihn ausschließen, nicht, aber er erhält die anderen drei Nachrichten.
6. Es werden keine Abbruch-Events protokolliert.

Braze protokolliert in Sams Fall keine Abbruch-Events, da dies nicht der Definition eines Abbruchs entspricht; Sam **hat keine** Aktionen ausgeführt, die die Nachrichten triggern würden. Bei In-App-Nachrichten führen Nutzer:innen den Trigger nie tatsächlich aus, bevor Braze entscheidet, dass sie die Nachricht nicht sehen sollten.

#### Abbruchverhalten bei vorlagenbasierten In-App-Nachrichten {#templated-in-app-message-abort-behavior}

[Vorlagenbasierte In-App-Nachrichten](#what-are-templated-in-app-messages) veranlassen das SDK, beim Auftreten des Trigger-Events erneut zu prüfen, ob eine Nachricht angezeigt werden soll. Dies hat ein anderes Abbruchverhalten. Betrachten Sie zur Veranschaulichung dieses Beispiel:

1. Sam startet eine Braze-Sitzung, indem er eine Braze-gestützte App auf seinem Telefon öffnet.
2. Die Zielgruppenkriterien der aktiven Campaigns besagen, dass Sam für eine vorlagenbasierte In-App-Nachricht berechtigt sein könnte, sodass die Trigger-Informationen ohne die Nachricht-Payload an sein Gerät gesendet werden.
3. Sam wählt einen Button aus, der ein angepasstes Event protokolliert und die vorlagenbasierte In-App-Nachricht triggert.
4. Sams Gerät stellt eine Netzwerkanfrage, um die In-App-Nachricht abzurufen.
5. Die Liquid-Logik der Nachricht führt zu einem Abbruch, sodass Braze dies als Abbruch protokolliert; Sam hat die Trigger-Aktion vor dieser Auswertung ausgeführt.

#### Vergleich des Abbruchverhaltens bei In-App-Nachrichten {#comparing-in-app-message-abort-behavior}

Diese Tabelle vergleicht die In-App-Nachricht-Abläufe, die Sam erlebt hat:

| In-App-Nachricht | Abbruchverhalten |
| --- | --- |
| Standard | Ein Abbruch-Event wurde nicht protokolliert, da Sam keine Aktionen ausgeführt hat, die eine Nachricht triggern würden.<br><br>Standard-In-App-Nachrichten protokollieren keine Abbrüche, da die Definition eines Abbruchs lautet: „hat die Nachricht trotz Ausführung der Trigger-Aktion nicht gesehen.“ Da In-App-Nachrichten vor den Trigger-Aktionen an das Gerät zugestellt werden, ist es nicht sinnvoll, In-App-Nachrichten, die aufgrund von Liquid-Logik ausgelassen wurden, als Abbrüche zu betrachten. |
| Vorlagenbasiert | Ein Abbruch-Event wurde protokolliert, da Sam die Trigger-Aktion ausgeführt hat, um die vorlagenbasierte In-App-Nachricht zu triggern, aber einen Abbruch im Liquid-Templating erhalten hat.<br><br>Vorlagenbasierte In-App-Nachrichten protokollieren Abbrüche, da die Liquid-Auswertung nach der Ausführung der Trigger-Aktion erfolgt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Vergleich des Abbruchverhaltens bei In-App-Nachrichten" }

### Warum ist der Schließen-Button bei Vollbild-HTML-In-App-Nachrichten auf Android ausgeblendet? {#why-is-the-close-button-hidden-on-full-screen-html-in-app-messages-on-android}

Auf Geräten mit randlosen Displays (einschließlich Android 15+) können Vollbild-HTML-In-App-Nachrichten hinter der System-Statusleiste gezeichnet werden und ein Schließen-Steuerelement am oberen Rand des Layouts verdecken.

Braze Android SDK Version 37.0.0 und höher wendet standardmäßig Fenster-Insets auf HTML-In-App-Nachrichten an, sodass Steuerelemente im sicheren Bereich bleiben. Wenn Nutzer:innen weiterhin Überlappungen sehen, aktualisieren Sie auf die neueste Version des Braze Android SDK.

Bei älteren SDK-Versionen konnten Entwickler:innen `BrazeConfig.setIsHtmlInAppMessageApplyWindowInsetsEnabled(true)` aktivieren, bevor dieses Verhalten zum Standard wurde.

### Welche bekannten Einschränkungen hat der Drag-and-Drop-Editor für In-App-Nachrichten? {#what-are-known-limitations-of-the-drag-and-drop-in-app-message-editor}

Der [Drag-and-Drop-Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/) unterstützt nicht jede Anpassung, die bei [angepassten HTML]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html/)-In-App-Nachrichten verfügbar ist. Beachten Sie Folgendes:

- Ein Deeplink pro Nachricht (nicht verschiedene Links pro Gerätetyp)
- Deckkraft gilt für den gesamten Nachrichtenhintergrund, nicht für einzelne Elemente
- Die maximale Nachrichtenbreite kann nicht unter 325 px eingestellt werden
- Hintergrundbilder und -farben gelten für die gesamte Nachricht, nicht pro Plattform
- Stile auf Nachrichtenebene gelten für die gesamte Nachricht
- Abstandsblöcke verwenden nur Pixelwerte
- Nur modale und Vollbild-Nachrichtentypen
- Hintergrundbilder werden gestreckt, um in das Modal zu passen
- Hintergrundbilder und Klick-Aktionen bleiben über Seiten hinweg in mehrseitigen Nachrichten erhalten

### Was bedeutet „Event was published, but no subscribers were found“ in den Android-SDK-Logs? {#what-does-event-was-published-but-no-subscribers-were-found-mean-in-android-sdk-logs}

Diese Log-Zeile ist in der Regel kein Fehler. Sie erscheint häufig, wenn Braze ein internes Event (z. B. `NoMatchingTriggerEvent`) veröffentlicht und zu diesem Zeitpunkt kein In-App-Nachricht- oder Content-Card-Listener abonniert ist.

Wenn Sie diesen Log sehen, obwohl Sie erwarten, dass ein angepasstes Event eine In-App-Nachricht triggert, überprüfen Sie, ob das Event protokolliert wird, ob sich der/die Nutzer:in in der Campaign- oder Canvas-Zielgruppe befindet und ob Content Cards synchronisiert sind, wenn die Nachricht davon abhängt.