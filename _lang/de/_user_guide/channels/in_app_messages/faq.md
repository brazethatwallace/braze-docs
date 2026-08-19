---
nav_title: FAQ
article_title: FAQ zu In-App-Nachrichten
page_order: 30
description: "Dieser Artikel enthält Antworten auf häufig gestellte Fragen zu In-App Messages."
tool: in-app messages

---

# Häufig gestellte Fragen {#frequently-asked-questions}

> Dieser Artikel enthält Antworten auf einige häufig gestellte Fragen zu In-App-Nachrichten.

## Was ist eine In-Browser-Nachricht und wie unterscheidet sie sich von einer In-App-Nachricht? {#what-is-an-in-browser-message-and-how-does-it-differ-from-an-in-app-message}

In-Browser-Nachrichten sind In-App-Nachrichten, die an Webbrowser gesendet werden. Um eine In-Browser-Nachricht zu erstellen, wählen Sie beim Erstellen Ihrer In-App-Nachricht-Campaign oder Ihres Canvas im Feld **Senden an** die Option **Web Browser** aus.

## Wird eine In-App-Nachricht angezeigt, wenn ein Gerät offline ist? {#does-an-in-app-message-display-if-a-device-is-offline}

Das kommt darauf an. Da In-App-Nachrichten zu Beginn der Sitzung zugestellt werden, kann das Gerät die Payload herunterladen, bevor es offline geht. In diesem Fall kann die In-App-Nachricht auch offline angezeigt werden. Wenn die Payload nicht heruntergeladen wurde, wird die In-App-Nachricht nicht angezeigt.

## Wenn Nutzer:innen bereits eine In-App-Nachrichten-Payload auf ihrem Gerät haben und das Ablaufdatum der Nachricht geändert wird, wird das Ablaufdatum auf ihrem Gerät aktualisiert? {#if-a-user-already-has-an-in-app-message-payload-on-their-device-and-the-message-expiration-is-changed-does-the-expiration-update-on-their-device}

Wenn Nutzer:innen eine Sitzung starten, prüft Braze, ob Änderungen an In-App-Nachrichten vorgenommen wurden, für die sie berechtigt sind, und aktualisiert diese entsprechend. Wenn sich also das Ablaufdatum geändert hat und sie eine Sitzung protokollieren, wird die In-App-Nachricht mit den aktualisierten Informationen an das Gerät gesendet.

## Wie richte ich Ruhezeiten für eine In-App-Nachricht-Campaign ein? {#how-do-i-set-up-quiet-hours-for-an-in-app-message-campaign}

Das Feature „Ruhezeiten“ ist für In-App-Nachricht-Campaigns nicht verfügbar. Dieses Feature wird verwendet, um zu verhindern, dass Nachrichten während bestimmter Stunden an Ihre Nutzer:innen gesendet werden. Bei In-App-Nachricht-Campaigns erhalten Ihre Nutzer:innen In-App-Nachrichten nur, wenn sie in der App aktiv sind.

Als Workaround zum Senden von In-App-Nachrichten während eines bestimmten Zeitraums können Sie den folgenden Liquid-Beispielcode verwenden. Dieser ermöglicht es, die Nachricht abzubrechen, wenn die In-App-Nachricht nach 19:59 Uhr oder vor 8:00 Uhr in der angegebenen Zeitzone angezeigt wird.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 19 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}
MESSAGE HERE
```
{% endraw %}

## Können Nutzer:innen eine In-App-Nachricht erneut erhalten, nachdem sie sie geschlossen haben? {#can-users-receive-an-in-app-message-again-after-they-dismiss-it}

### Campaigns {#campaigns}

Bei In-App-Nachrichten-Campaigns können Sie Nutzer:innen erlauben, erneut für den Empfang der Campaign berechtigt zu werden, indem Sie die erneute Berechtigung unter **Zustellungskontrollen** aktivieren (**Nutzer:innen erlauben, erneut für den Empfang der Campaign berechtigt zu werden**). Wie schnell sie die Nachricht erneut erhalten können, hängt vom eingestellten Zeitfenster für die erneute Berechtigung ab und davon, wie Braze den vorherigen Versand erfasst hat. Weitere Informationen zum Campaign-Verhalten, einschließlich des Zusammenhangs zwischen erneuter Berechtigung und Nachrichtenempfang, finden Sie unter [Erneute Berechtigung für Campaigns und Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).

Wenn die erneute Berechtigung deaktiviert ist, erhalten Nutzer:innen dieselbe Campaign in der Regel nicht erneut, sobald sie sie einmal erhalten haben – unabhängig davon, ob sie die Qualifizierungskriterien erneut erfüllen.

### Canvases {#canvases}

Bei In-App-Nachrichten, die über einen Canvas gesendet werden, hängt es von den Canvas-Eintrittskontrollen (z. B. ob Nutzer:innen den Canvas erneut betreten dürfen) und Ihrer Schritt-Konfiguration ab, ob Nutzer:innen die Nachricht erneut sehen können – nicht nur von den Zustellungskontrollen der Campaign.

## Wann wird die Berechtigung für eine In-App-Nachricht berechnet? {#when-is-eligibility-for-an-in-app-message-calculated}

Die Berechtigung für eine In-App-Nachricht wird zum Zeitpunkt der Zustellung berechnet. Wenn eine In-App-Nachricht für 7 Uhr morgens geplant ist, wird die Berechtigung für diese In-App-Nachricht um 7 Uhr morgens geprüft.

Wenn die In-App-Nachricht angezeigt wird, hängt die Berechtigung davon ab, wann die In-App-Nachricht heruntergeladen und getriggert wurde.

## Warum liefert meine archivierte In-App-Nachricht-Campaign weiterhin In-App-Nachricht-Impressionen? {#why-is-my-archived-in-app-message-campaign-still-delivering-in-app-message-impressions}

Dies kann bei Nutzer:innen auftreten, die die Segmentkriterien erfüllt haben, als die In-App-Nachricht-Campaign noch aktiv war.

Um dies zu verhindern, wählen Sie während der Campaign-Einrichtung **Re-evaluate campaign eligibility before displaying** aus.

## Warum sehe ich keine Öffnungen für In-App-Nachrichten? {#why-dont-i-see-opens-for-in-app-messages}

In-App-Nachrichten verwenden keine Metrik für *Öffnungen*. Braze protokolliert *Impressionen*, wenn die Nachricht auf dem Bildschirm sichtbar wird, und *Klicks*, wenn Nutzer:innen mit dem Nachrichtentext oder den Buttons interagieren. Wenn ein kanalübergreifender Export oder Bericht Zeilen für In-App-Nachrichten enthält, vergleichen Sie *Impressionen* und *Klicks* anstelle von E-Mail-typischen Öffnungen. Definitionen finden Sie unter [In-App-Nachricht-Reporting]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting).

## Können mehrere In-App-Nachrichten in derselben Sitzung angezeigt werden? {#can-multiple-in-app-messages-display-in-the-same-session}

Ja, aber pro Auftreten eines [Trigger-Events]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#choose-a-trigger) kann nur eine In-App-Nachricht angezeigt werden. Wenn mehrere In-App-Nachricht-Campaigns denselben Trigger teilen (zum Beispiel Sitzungsstart), wird jedes Mal, wenn dieser Trigger ausgelöst wird, nur die Nachricht mit der höchsten Priorität angezeigt. Bei Sitzungsstart-Triggern bedeutet dies, dass pro Sitzung nur eine Nachricht angezeigt werden kann und die nächste Gelegenheit, eine weitere berechtigte Nachricht anzuzeigen, die nächste Sitzung ist.

Wenn mehrere Nachrichten dieselbe Prioritätsstufe haben, wird die zuletzt erstellte Nachricht zuerst angezeigt. Bei Sitzungsstart-Triggern wird die nächstaktuellste Nachricht in einer nachfolgenden Sitzung angezeigt; bei anderen Trigger-Typen wird die nächstaktuellste Nachricht beim nächsten Auftreten dieses Trigger-Events angezeigt, was innerhalb derselben Sitzung oder in einer späteren Sitzung sein kann.

Um die Anzeigereihenfolge innerhalb einer Prioritätsstufe zu steuern, gehen Sie zu den Zustellungseinstellungen einer der Campaigns und wählen Sie **Set exact priority** aus. Ziehen Sie die Campaigns dann per Drag-and-Drop in die gewünschte Reihenfolge. Weitere Informationen finden Sie unter [Priorität auswählen]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#choose-a-priority).

## Wie werden Impressionen und Klicks von In-App-Nachrichten protokolliert? {#how-are-in-app-message-impressions-and-clicks-logged}

Unter [In-App-Nachrichten-Reporting]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting) erfahren Sie, wie Impressionen und Klicks nach Nutzer:innen-Aktion protokolliert werden. Beispiele speziell für Vollbild-Nachrichten, die mit dem traditionellen Editor erstellt wurden, finden Sie unter [Vollbild-Nachrichten-Metriken nach Nutzer:innen-Aktion]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting#fullscreen-metrics-by-user-action).

## Wie berechnet Braze den Ablauf einer In-App-Nachricht, die auf „nach 1 Tag(en)“ eingestellt ist? {#how-does-braze-calculate-an-in-app-message-expiration-set-to-after-1-days}

Braze berechnet eine Ablaufzeit von einem Tag als 24 Stunden, nachdem Nutzer:innen berechtigt sind, eine Nachricht zu erhalten.

## Was sind Template-basierte In-App-Nachrichten? {#what-are-templated-in-app-messages}

In-App-Nachrichten werden als Template-basierte In-App-Nachrichten zugestellt, wenn **Kampagnenberechtigung vor der Anzeige erneut prüfen** ausgewählt ist oder wenn einer der folgenden Liquid-Tags in der Nachricht vorhanden ist:

- `canvas_entry_properties`
- `connected_content`
- SMS-Variablen wie {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Das bedeutet, dass das Gerät beim Sitzungsstart den Trigger dieser In-App-Nachricht anstelle der gesamten Nachricht erhält. Wenn die Nutzer:innen die In-App-Nachricht triggern, stellt das Gerät eine Netzwerkanfrage, um die eigentliche Nachricht abzurufen.

{% alert note %}
Die Nachricht wird nicht zugestellt, wenn das Gerät keinen Internetzugang hat. Die Nachricht wird möglicherweise nicht zugestellt, wenn die Liquid-Logik zu lange für die Auflösung benötigt.
{% endalert %}

## Wie funktioniert das Abbruchverhalten bei In-App-Nachrichten? {#how-does-abort-behavior-work-for-in-app-messages}

Bei Braze tritt ein Abbruch auf, wenn Nutzer:innen eine Aktion ausführen, die sie für den Empfang einer Nachricht qualifiziert, sie die Nachricht jedoch nicht erhalten, weil die Liquid-Logik sie als nicht berechtigt kennzeichnet. Zum Beispiel:

1. Sam führt eine Aktion aus, die eine E-Mail-Campaign triggern sollte.
2. Der E-Mail-Text enthält Liquid-Logik, die besagt: Wenn ein angepasstes Attribut „Score“ kleiner als 50 ist, soll diese E-Mail nicht gesendet werden.
3. Sams angepasstes Attribut „Score“ beträgt 20.
4. Braze erkennt, dass Sam diese E-Mail nicht erhalten sollte, und die E-Mail wird abgebrochen.
5. Ein Abbruch-Event wird protokolliert.

Da In-App-Nachrichten jedoch ein Pull-Kanal sind, funktionieren Abbrüche bei ihnen etwas anders.

### Standard-Abbruchverhalten bei In-App-Nachrichten {#standard-in-app-message-abort-behavior}

In-App-Nachrichten werden beim Sitzungsstart vom Gerät abgerufen und auf dem Gerät zwischengespeichert, sodass die Nachricht unabhängig von der Internetverbindungsqualität sofort an die Nutzer:innen zugestellt werden kann. Wenn Nutzer:innen beispielsweise fünf In-App-Nachrichten innerhalb ihrer Sitzung erhalten, werden alle fünf beim Sitzungsstart abgerufen. Die Nachrichten werden lokal zwischengespeichert und erscheinen, wenn ihre definierten Trigger-Events eintreten (Sitzungsstart, Nutzer:innen klicken auf einen Button, der ein angepasstes Event protokolliert, oder andere).

Mit anderen Worten: Die Logik, die bestimmt, ob eine In-App-Nachricht abgebrochen werden soll, wird ausgeführt, **bevor** der Trigger eingetreten ist. Um dies zu veranschaulichen, nehmen wir an, dass Sam aus dem E-Mail-Beispiel Push-Benachrichtigungen abonniert hat.

1. Sam startet eine Sitzung, indem er eine Braze-gestützte App auf seinem Telefon öffnet.
2. Basierend auf den Zielgruppenkriterien der aktiven Campaigns im Workspace könnte Sam für fünf verschiedene Campaigns berechtigt sein. Alle fünf werden auf sein Telefon geladen und zwischengespeichert.
3. Sam **hat keine** Aktionen ausgeführt, die diese Nachrichten triggern würden, könnte sie aber während der Sitzung erhalten.
4. Die Liquid-Logik in zwei der In-App-Nachrichten enthält Regeln, die Sam vom Empfang der Nachricht ausschließen (z. B. weil sein angepasstes Attribut „Score“ nicht hoch genug ist).
5. Sam erhält die beiden In-App-Nachrichten, die ihn ausschließen, nicht, bekommt aber die anderen drei Nachrichten.
6. Es werden keine Abbruch-Events protokolliert.

Braze protokolliert in Sams Fall keine Abbruch-Events, da dies nicht der Definition eines Abbruchs entspricht: Sam **hat keine** Aktionen ausgeführt, die die Nachrichten triggern würden. Bei In-App-Nachrichten führen Nutzer:innen den Trigger nie tatsächlich aus, bevor Braze entscheidet, dass sie die Nachricht nicht sehen sollen.

### Abbruchverhalten bei vorlagenbasierten In-App-Nachrichten {#templated-in-app-message-abort-behavior}

[Vorlagenbasierte In-App-Nachrichten](#what-are-templated-in-app-messages) veranlassen das SDK, beim Eintreten des Trigger-Events erneut zu prüfen, ob eine Nachricht angezeigt werden soll. Dies führt zu einem anderen Abbruchverhalten. Betrachten Sie zur Veranschaulichung dieses Beispiel:

1. Sam startet eine Braze-Sitzung, indem er eine Braze-gestützte App auf seinem Telefon öffnet.
2. Die Zielgruppenkriterien der aktiven Campaigns besagen, dass Sam für eine vorlagenbasierte In-App-Nachricht berechtigt sein könnte, daher werden die Trigger-Informationen ohne den Nachrichteninhalt an sein Gerät gesendet.
3. Sam klickt auf einen Button, der ein angepasstes Event protokolliert und die vorlagenbasierte In-App-Nachricht triggert.
4. Sams Gerät sendet eine Netzwerkanfrage, um die In-App-Nachricht abzurufen.
5. Die Liquid-Logik der Nachricht führt zu einem Abbruch, daher protokolliert Braze dies als Abbruch; Sam hat die Trigger-Aktion vor dieser Auswertung ausgeführt.

### Vergleich des Abbruchverhaltens bei In-App-Nachrichten {#comparing-in-app-message-abort-behavior}

Diese Tabelle vergleicht die In-App-Nachrichten-Abläufe, die Sam erlebt hat:

| In-App-Nachricht | Abbruchverhalten |
| --- | --- |
| Standard | Es wurde kein Abbruch-Event protokolliert, da Sam keine Aktionen ausgeführt hat, die eine Nachricht triggern würden.<br><br>Standard-In-App-Nachrichten protokollieren keine Abbrüche, da die Definition eines Abbruchs lautet: „hat die Nachricht trotz Ausführung der Trigger-Aktion nicht gesehen.“ Da In-App-Nachrichten vor den Trigger-Aktionen an das Gerät zugestellt werden, ist es nicht sinnvoll, In-App-Nachrichten, die aufgrund von Liquid-Logik ausgelassen wurden, als Abbrüche zu betrachten. |
| Vorlagenbasiert | Es wurde ein Abbruch-Event protokolliert, da Sam die Trigger-Aktion ausgeführt hat, um die vorlagenbasierte In-App-Nachricht zu triggern, aber beim Liquid-Templating einen Abbruch erhalten hat.<br><br>Vorlagenbasierte In-App-Nachrichten protokollieren Abbrüche, da die Liquid-Auswertung nach der Ausführung der Trigger-Aktion erfolgt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Vergleich des Abbruchverhaltens bei In-App-Nachrichten" }

### Wann wird Connected Content bei In-App-Nachrichten ausgeführt? {#when-does-connected-content-run-for-in-app-messages}

Bei [vorlagenbasierten In-App-Nachrichten](#what-are-templated-in-app-messages) werden Connected Content und andere Liquid-Tags aufgelöst, wenn das Trigger-Event eintritt und das Gerät den Nachrichteninhalt anfordert – nicht wenn Nutzer:innen auf einen Button innerhalb der Nachricht klicken. Jeder vorlagenbasierte Abruf kann Connected-Content-Aufrufe für diese Anzeige enthalten.

Wenn Ihr HTML auf REST-Daten verweist, die von Connected Content zurückgegeben werden, stehen diese Daten für die Sitzung zur Verfügung, in der die Nachricht vorlagenbasiert erstellt wurde. Mehrere Buttons können auf dieselbe Connected-Content-Antwort verweisen, ohne beim Klick zusätzliche Aufrufe auszulösen.

### Warum gibt es eine Verzögerung, bevor meine In-App-Nachricht angezeigt wird? {#why-is-there-a-delay-before-my-in-app-message-displays}

Standard-In-App-Nachrichten werden angezeigt, sobald der zwischengespeicherte Inhalt nach dem Trigger-Event bereit ist. Auf Android und iOS können große Bilder oder andere CDN-gehostete Assets, auf die in der Nachricht verwiesen wird, eine kurze Verzögerung verursachen, während diese Ressourcen heruntergeladen werden, bevor die In-App-Nachricht erscheint.

[Vorlagenbasierte In-App-Nachrichten](#what-are-templated-in-app-messages) und Campaigns mit aktivierter Option **Campaign-Berechtigung vor der Anzeige erneut prüfen** erfordern nach dem Trigger eine zusätzliche Netzwerkanfrage, bevor die Nachricht erscheint. Dies kann eine kurze Verzögerung verursachen (typischerweise unter 100 ms bei einer stabilen Verbindung). Weitere Informationen finden Sie unter [Zielnutzer:innen auswählen]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#choose-users-to-target).

### Warum sieht meine In-App-Nachricht anders aus als die Dashboard-Vorschau? {#why-does-my-in-app-message-look-different-from-the-dashboard-preview}

Zugestellte In-App-Nachrichten können von der Dashboard-Vorschau abweichen, wenn:

- Ihre Integration angepasste Stile anwendet oder die Standard-UI für In-App-Nachrichten auf bestimmten Plattformen überschreibt
- Die Vorschau ein Testnutzer:innen-Profil mit anderen Attributen als die Empfänger:innen verwendet
- Vorlagenbasierte Inhalte zum Sendezeitpunkt anders aufgelöst werden als im Vorschaumodus

Verwenden Sie [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message) mit Testnutzer:innen, deren Profil Ihrer Zielgruppe entspricht, um das Erscheinungsbild zu überprüfen.

### Warum verwendet eine mehrseitige In-App-Nachricht auf jeder Seite denselben Hintergrund? {#why-does-a-multi-page-in-app-message-use-the-same-background-on-every-page}

Wenn **Hintergrundbild** auf einer Seite einer mehrseitigen In-App-Nachricht aktiviert ist, wird dieser Hintergrund auf alle Seiten der Nachricht angewendet. Um verschiedene Hintergründe pro Seite zu verwenden, nutzen Sie einen angepassten HTML-Block mit JavaScript, um Bilder zwischen den Seiten zu wechseln.

### Wie teste ich Web-In-App-Nachrichten? {#how-do-i-test-web-in-app-messages}

Testversendungen von Web-In-App-Nachrichten erfordern, dass Push auf dem Testgerät aktiviert ist, da der Testablauf eine Push-Benachrichtigung sendet, die die App oder Website öffnet, in der die In-App-Nachricht angezeigt wird. Derselbe Push-basierte Testpfad gilt auf jeder Plattform, auf der Push nicht mit Braze konfiguriert ist, obwohl fehlendes Push am häufigsten im Web auftritt, da viele mobile Integrationen Push bereits aktiviert haben. Verwenden Sie stattdessen eine Live-Campaign an ein internes Testsegment. Schritte finden Sie unter [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message).

### Benötigen In-App-Nachrichten eine Push-Integration? {#do-in-app-messages-require-push-integration}

In-App-Nachrichten benötigen keine Push-Benachrichtigungen, um in der Produktion zu funktionieren. In-App-Nachrichten werden über das Braze SDK zugestellt und erscheinen während einer aktiven App-Sitzung, ohne dass eine Push-Integration erforderlich ist.

Testversendungen für In-App-Nachrichten erfordern jedoch, dass Push auf Ihren Testgeräten aktiviert ist. Dies liegt daran, dass Test-In-App-Nachrichten über eine Push-Benachrichtigung zugestellt werden, die die Anzeige der In-App-Nachricht triggert. Die Testnutzer:innen müssen Push aktiviert haben und auf die Test-Push-Benachrichtigung tippen, um die In-App-Nachricht anzuzeigen.

Bei Produktions-Campaigns sehen Nutzer:innen In-App-Nachrichten basierend auf Ihren Campaign-Triggern (wie Sitzungsstart oder angepasste Events), ohne dass Push beteiligt ist.

### Warum erscheinen zusätzliche oder nicht gerenderte Zeichen in meiner In-App-Nachricht? {#why-do-extra-or-unrendered-characters-appear-in-my-in-app-message}

Das Kopieren von Text aus einer anderen App (z. B. einem Textverarbeitungsprogramm oder einer Webseite) kann unsichtbare oder nicht druckbare Zeichen in Ihren Nachrichtentext einfügen. Diese Zeichen können als unerwünschte Symbole erscheinen oder Liquid und HTML in angepassten Nachrichten beschädigen.

Um unerwünschte oder nicht gerenderte Zeichen zu beheben, geben Sie den betroffenen Text im Braze-Editor erneut ein oder löschen Sie die unerwünschten Zeichen direkt, anstatt nur den sichtbaren Text auszuwählen und zu ersetzen. Fügen Sie bei angepassten HTML-Nachrichten mit Sonderzeichen `<meta charset="UTF-8">` in Ihren HTML-`<head>` ein. Weitere Details finden Sie unter [Zeichenkodierung]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#character-encoding).

## Warum ist der Schließen-Button bei Vollbild-HTML-In-App-Nachrichten auf Android ausgeblendet? {#why-is-the-close-button-hidden-on-full-screen-html-in-app-messages-on-android}

Auf Geräten mit randlosem Display (einschließlich Android 15+) können Vollbild-HTML-In-App-Nachrichten hinter der System-Statusleiste gezeichnet werden und ein Schließen-Steuerelement am oberen Rand des Layouts verdecken.

Ab Version 37.0.0 des Braze Android SDK werden Window-Insets standardmäßig auf HTML-In-App-Nachrichten angewendet, sodass Steuerelemente im sicheren Bereich bleiben. Falls Nutzer:innen weiterhin Überlappungen sehen, aktualisieren Sie auf die neueste Version des Braze Android SDK.

Bei älteren SDK-Versionen konnten Entwickler:innen `BrazeConfig.setIsHtmlInAppMessageApplyWindowInsetsEnabled(true)` aktivieren, bevor dieses Verhalten zum Standard wurde.

## Was sollte ich bei der Anpassung von Drag-and-Drop-In-App-Nachrichten beachten? {#what-should-i-know-when-customizing-drag-and-drop-in-app-messages}

Der [Drag-and-Drop-Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) unterstützt die Anzeigetypen Modal und Vollbild. Sie erstellen Inhalte innerhalb dieser Container mit Editor-Blöcken.

Beachten Sie Folgendes:

- **Links und Deeplinks:** Jede Klick-Aktion hat standardmäßig ein URL-Feld. Verwenden Sie Liquid in der URL, um Links je nach Gerät, App-Typ oder Nutzer:innen-Attributen zu variieren. Im **Nachrichten-Container** können Sie außerdem plattformspezifisches Klickverhalten aktivieren, um unterschiedliche Links pro Plattform festzulegen.
- **Deckkraft und Hintergründe:** Die Deckkraft des Nachrichten-Containers wirkt sich auf den gesamten Nachrichtenhintergrund aus. Einzelne Blöcke können eigene Hintergrundfarben festlegen. Für eine feinere Steuerung fügen Sie angepasstes CSS in einem Custom-Code-Block hinzu.
- **Nachrichtenbreite:** Die maximale Breite des **Nachrichten-Containers** kann im Editor nicht unter 325 px eingestellt werden, damit Inhalte auf kleineren Bildschirmen lesbar bleiben. Verwenden Sie angepasstes CSS, wenn Sie ein schmaleres Layout benötigen.
- **Plattformspezifische Hintergründe:** Eine einzelne Nachricht verwendet dasselbe Hintergrundbild und dieselben Farben auf Web und Mobilgeräten. Im Editor können Sie keine unterschiedlichen Hintergründe pro Plattform festlegen.
- **Mehrseitige Nachrichten:** Hintergrundbilder und Klick-Aktionen auf Nachrichtenebene gelten für alle Seiten einer mehrseitigen Nachricht. Um auf jeder Seite unterschiedliche Vollbilder zu verwenden, fügen Sie Buttons hinzu, die zur nächsten Seite verlinken.
- **Stile auf Nachrichtenebene:** Stile auf Nachrichtenebene gelten für die gesamte Nachricht.
- **Hintergrundbilder:** Hintergrundbilder werden gestreckt, um das Modal auszufüllen.

Weitere Hinweise zum Editor finden Sie im [Vorbereitungsleitfaden für In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices/prep_guide#drag-and-drop-editor-considerations).

## Was bedeutet „Event was published, but no subscribers were found“ in den Android-SDK-Logs? {#what-does-event-was-published-but-no-subscribers-were-found-mean-in-android-sdk-logs}

Diese Log-Zeile ist in der Regel kein Fehler. Sie erscheint häufig, wenn Braze ein internes Event (z. B. `NoMatchingTriggerEvent`) veröffentlicht und zu diesem Zeitpunkt kein In-App-Nachrichten- oder Content-Card-Listener registriert ist.

Wenn diese Meldung erscheint, obwohl Sie erwarten, dass ein angepasstes Event eine In-App-Nachricht auslöst, überprüfen Sie, ob das Event protokolliert wurde, ob die Nutzer:innen zur Zielgruppe der Campaign oder des Canvas gehören und ob Content Cards synchronisiert sind, wenn die Nachricht davon abhängt.