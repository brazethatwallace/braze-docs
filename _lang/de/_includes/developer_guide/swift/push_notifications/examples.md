{% multi_lang_include developer_guide/prerequisites/swift.md %} Sie müssen außerdem [Push-Benachrichtigungen einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

{% alert note %}
Dieser Implementierungsleitfaden konzentriert sich auf eine Swift-Implementierung. Für Interessierte werden jedoch Objective-C-Snippets bereitgestellt.
{% endalert %}

## App-Erweiterungen für Benachrichtigungsinhalte {#notification-content-app-extensions}

![Zwei Push-Nachrichten nebeneinander. Die linke Nachricht zeigt, wie ein Push mit der Standard-UI aussieht. Die rechte Nachricht zeigt einen Kaffee-Stempelkarten-Push, der durch die Implementierung einer angepassten Push-UI erstellt wurde.]({% image_buster /assets/img/push_implementation_guide/push1.png %}){: style="max-width:65%;border:0;margin-top:10px"}

App-Erweiterungen für Benachrichtigungsinhalte bieten Ihnen eine hervorragende Möglichkeit zur Anpassung von Push-Benachrichtigungen. App-Erweiterungen für Benachrichtigungsinhalte zeigen eine angepasste Oberfläche für die Benachrichtigungen Ihrer App an, wenn eine Push-Benachrichtigung erweitert wird.

Push-Benachrichtigungen können auf drei verschiedene Arten erweitert werden:
- Langes Drücken auf das Push-Banner
- Nach unten wischen auf dem Push-Banner
- Das Banner horizontal wischen und „Anzeigen“ auswählen

Diese angepassten Ansichten bieten intelligente Möglichkeiten, Kund:innen anzusprechen, indem verschiedene Arten von Inhalten angezeigt werden, darunter interaktive Benachrichtigungen, mit Nutzerdaten gefüllte Benachrichtigungen und sogar Push-Nachrichten, die Informationen wie Telefonnummern und E-Mail-Adressen erfassen können. Eines unserer bekannten Features bei Braze, [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories), ist ein hervorragendes Beispiel dafür, wie eine App-Erweiterung für Push-Benachrichtigungsinhalte aussehen kann!

### Voraussetzungen {#requirements}

![Xcodes Bildschirm „Vorlage für neues Target auswählen“ mit „Notification Content Extension“ unter „Application Extension“ ausgewählt.]({% image_buster /assets/img/push_implementation_guide/push15.png %}){: style="float:right;max-width:50%;margin-left:10px; border:0;margin-top:10px"}
- [Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) erfolgreich in Ihrer App integriert
- Die folgenden von Xcode basierend auf Ihrer Programmiersprache generierten Dateien:

**Swift**<br>
- `NotificationViewController.swift`
- `MainInterface.storyboard`

**Objective-C**<br>
- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

## Interaktive Push-Benachrichtigung {#interactive-push-notification}

Push-Benachrichtigungen können auf Nutzeraktionen innerhalb einer Content-App-Erweiterung reagieren. Für Nutzer:innen mit iOS 12 oder höher bedeutet dies, dass Sie Ihre Push-Benachrichtigungen in vollständig interaktive Nachrichten verwandeln können! Dies bietet eine spannende Möglichkeit, Interaktivität in Ihre Aktionen und Anwendungen einzuführen. Zum Beispiel kann Ihre Push-Benachrichtigung ein Spiel für Nutzer:innen enthalten, ein Glücksrad für Rabatte oder einen „Gefällt mir“-Button, um ein Angebot oder einen Song zu speichern.

Das folgende Beispiel zeigt eine Push-Benachrichtigung, bei der Nutzer:innen innerhalb der erweiterten Benachrichtigung ein Memory-Spiel spielen können.

![Ein Diagramm, das die Phasen einer interaktiven Push-Benachrichtigung zeigt. Eine Sequenz zeigt, wie eine Nutzer:in auf eine Push-Benachrichtigung tippt, die ein interaktives Memory-Spiel anzeigt.]({% image_buster /assets/img/push_implementation_guide/push12.png %}){: style="border:0"}

### Dashboard-Konfiguration {#dashboard-configuration}

Um eine interaktive Push-Benachrichtigung zu erstellen, müssen Sie eine angepasste Ansicht in Ihrem Dashboard einrichten.

1. Klicken Sie auf der Seite **Campaigns** auf **Create Campaign**, um eine neue Push-Benachrichtigungs-Campaign zu starten.
2. Aktivieren Sie auf dem Tab **Compose** die Option **Notification Buttons**.
3. Geben Sie eine angepasste iOS-Kategorie im Feld **iOS Notification Category** ein.
4. Setzen Sie in der `.plist` Ihres Notification Content Extension Targets das Attribut `UNNotificationExtensionCategory` auf Ihre angepasste iOS-Kategorie. Der hier angegebene Wert muss mit dem übereinstimmen, was im Braze-Dashboard unter **iOS Notification Category** festgelegt ist.
5. Setzen Sie den Schlüssel `UNNotificationExtensionInteractionEnabled` auf `true`, um Nutzerinteraktionen in einer Push-Benachrichtigung zu aktivieren.

![Die Optionen für Benachrichtigungs-Buttons in den Einstellungen des Push-Nachrichten-Editors.]({% image_buster /assets/img/push_implementation_guide/push16.png %}){: style="max-width:75%;border:0;margin-top:10px"}
![Eine plist-Datei, die NSExtension mit UNNotificationExtensionCategory auf „your_custom_category“, UNNotificationExtensionDefaultContentHidden auf 1 und UNNotificationExtensionInitialContentSizeRatio auf 1 gesetzt zeigt.]({% image_buster /assets/img/push_implementation_guide/push17.png %}){: style="max-width:75%;border:0;margin-top:10px"}

## Personalisierte Push-Benachrichtigungen {#personalized-push-notifications}

![Zwei iPhones nebeneinander dargestellt. Das erste iPhone zeigt die nicht erweiterte Ansicht der Push-Nachricht. Das zweite iPhone zeigt die erweiterte Version der Push-Nachricht mit einem „Fortschritts“-Überblick, wie weit der Nutzer in einem Kurs ist, dem Namen der nächsten Sitzung und dem Fälligkeitsdatum der nächsten Sitzung.]({% image_buster /assets/img/push_implementation_guide/push6.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

Push-Benachrichtigungen können nutzerspezifische Informationen innerhalb einer Content Extension anzeigen. So können Sie nutzerzentrierte Push-Inhalte erstellen, z. B. die Möglichkeit, Ihren Fortschritt über verschiedene Plattformen hinweg zu teilen, freigeschaltete Erfolge anzuzeigen oder Onboarding-Checklisten darzustellen. Dieses Beispiel zeigt eine Push-Benachrichtigung, die einem Nutzer angezeigt wird, nachdem er eine bestimmte Aufgabe im Braze-Lernkurs abgeschlossen hat. Durch das Erweitern der Benachrichtigung kann der Nutzer seinen Fortschritt im Lernpfad sehen. Die hier bereitgestellten Informationen sind nutzerspezifisch und können ausgelöst werden, wenn eine Sitzung abgeschlossen oder eine bestimmte Nutzeraktion durch einen API-Trigger or triggern durchgeführt wird.

### Dashboard-Konfiguration

Um eine personalisierte Push-Benachrichtigung zu erstellen, müssen Sie in Ihrem Dashboard eine angepasste Ansicht festlegen.

1. Klicken Sie auf der Seite **Campaigns** auf **Create Campaign**, um eine neue Push-Benachrichtigungs-Campaign zu starten.
2. Aktivieren Sie auf dem Tab **Compose** die Option **Notification Buttons**.
3. Geben Sie eine angepasste iOS-Kategorie im Feld **iOS Notification Category** ein.
4. Erstellen Sie auf dem Tab **Settings** Schlüssel-Wert-Paare mithilfe von Standard-Liquid. Legen Sie die passenden Nutzerattribute fest, die die Nachricht anzeigen soll. Diese Ansichten können basierend auf bestimmten Nutzerattributen eines bestimmten Nutzerprofils personalisiert werden.
5. Setzen Sie in der `.plist` Ihres Notification Content Extension Targets das Attribut `UNNotificationExtensionCategory` auf Ihre angepasste iOS-Kategorie. Der hier angegebene Wert muss mit dem übereinstimmen, was im Braze-Dashboard unter **iOS Notification Category** eingestellt ist.

![Vier Sätze von Schlüssel-Wert-Paaren, wobei „next_session_name“ und „next_session_complete_date“ als API-Trigger-Eigenschaft mithilfe von Liquid festgelegt sind und „completed_session count“ sowie „total_session_count“ als angepasstes Nutzerattribut mithilfe von Liquid festgelegt sind.]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

### Verarbeitung von Schlüssel-Wert-Paaren {#handling-key-value-pairs}

Die Methode `didReceive` wird aufgerufen, wenn die Notification Content App Extension eine Benachrichtigung empfangen hat. Diese Methode befindet sich im `NotificationViewController`. Die im Dashboard bereitgestellten Schlüssel-Wert-Paare werden im Code über ein `userInfo`-Dictionary dargestellt.

#### Schlüssel-Wert-Paare aus Push-Benachrichtigungen parsen {#parsing-key-value-pairs-from-push-notifications}

{% tabs %}
{% tab Swift %}
``` swift
func didReceive(_ notification: UNNotification) {
  let userInfo = notification.request.content.userInfo

  guard let value = userInfo["YOUR-KEY-VALUE-PAIR"] as? String,
        let otherValue = userInfo["YOUR-OTHER-KEY-VALUE-PAIR"] as? String,
  else { fatalError("Key-Value Pairs are incorrect.")}

  ...
}
```
{% endtab %}
{% tab Objective-C %}
```objc
- (void)didReceiveNotification:(nonnull UNNotification *)notification {
  NSDictionary *userInfo = notification.request.content.userInfo;

  if (userInfo[@"YOUR-KEY-VALUE-PAIR"] && userInfo[@"YOUR-OTHER-KEY-VALUE-PAIR"]) {

  ...

  } else {
    [NSException raise:NSGenericException format:@"Key-Value Pairs are incorrect"];
  }
}
```
{% endtab %}
{% endtabs %}

## Push-Benachrichtigung zur Informationserfassung {#information-capture-push-notification}

Push-Benachrichtigungen können Nutzerinformationen innerhalb einer Content-App-Erweiterung erfassen und erweitern so die Möglichkeiten, was mit einem Push realisierbar ist. Durch die Eingabeaufforderung über Push-Benachrichtigungen können Sie nicht nur grundlegende Informationen wie Name oder E-Mail-Adresse abfragen, sondern auch Nutzer:innen dazu auffordern, Feedback zu geben oder ein unvollständiges Kundenprofil or Nutzerprofil zu vervollständigen.

{% alert tip %}
Weitere Informationen finden Sie unter [Push-Benachrichtigungsdaten protokollieren]({{site.baseurl}}/developer_guide/analytics/logging_channel_data/push_notifications).
{% endalert %}

Im folgenden Ablauf kann die angepasste Ansicht auf Statusänderungen reagieren. Diese Statusänderungskomponenten sind in jedem Bild dargestellt.

1. Nutzer:in erhält eine Push-Benachrichtigung.
2. Der Push wird geöffnet. Nach dem Aufklappen fordert der Push die Nutzer:innen zur Eingabe von Informationen auf. In diesem Beispiel wird die E-Mail-Adresse der Nutzer:innen abgefragt, aber es kann jede Art von Information angefordert werden.
3. Die Information wird eingegeben, und wenn sie im erwarteten Format vorliegt, wird der Registrierungsbutton angezeigt.
3. Die Bestätigungsansicht wird angezeigt, und der Push wird geschlossen.


### Dashboard-Konfiguration

Um eine Push-Benachrichtigung zur Informationserfassung zu erstellen, müssen Sie eine angepasste Ansicht in Ihrem Dashboard einrichten.

1. Klicken Sie auf der Seite **Campaigns** auf **Create Campaign**, um eine neue Push-Benachrichtigungs-Campaign zu starten.
2. Aktivieren Sie auf dem Tab **Compose** die Option **Notification Buttons**.
3. Geben Sie eine angepasste iOS-Kategorie im Feld **iOS Notification Category** ein.
4. Erstellen Sie im Tab **Settings** Schlüssel-Wert-Paare mithilfe von Standard-Liquid. Legen Sie die entsprechenden Nutzerattribute fest, die die Nachricht anzeigen soll.
5. Setzen Sie in der `.plist` Ihres Notification Content Extension Targets das Attribut `UNNotificationExtensionCategory` auf Ihre angepasste iOS-Kategorie. Der hier eingegebene Wert muss mit dem übereinstimmen, was im Braze-Dashboard unter **iOS Notification Category** festgelegt ist.

Wie im Beispiel gezeigt, können Sie auch ein Bild in Ihre Push-Benachrichtigung einfügen. Dazu müssen Sie [Rich-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=swift) integrieren, den Benachrichtigungsstil in Ihrer Campaign auf Rich-Benachrichtigung setzen und ein Rich-Push-Bild einfügen.

![Eine Push-Nachricht mit drei Schlüssel-Wert-Paaren. 1. „Braze_id“ als Liquid-Aufruf zum Abrufen der Braze-ID. 2. „cert_title“ als „Braze Marketer Certification“. 3. „Cert_description“ als „Certified Braze marketers drive...“.]({% image_buster /assets/img/push_implementation_guide/push9.png %})

### Verarbeitung von Button-Aktionen {#handling-button-actions}

Jeder Aktions-Button wird eindeutig identifiziert. Der Code prüft, ob Ihr Antwortbezeichner gleich dem `actionIdentifier` ist, und erkennt so, dass die Nutzer:innen den Aktions-Button angeklickt haben.

**Verarbeitung von Antworten auf Push-Benachrichtigungs-Aktions-Buttons**<br>

{% tabs %}
{% tab Swift %}
``` swift
func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
  if response.actionIdentifier == "YOUR-REGISTER-IDENTIFIER" {
    // do something
  } else {
    // do something else
  }
}
```
{% endtab %}
{% tab Objective-C %}
```objc
- (void)didReceiveNotificationResponse:(UNNotificationResponse *)response completionHandler:(void (^)(UNNotificationContentExtensionResponseOption))completion {
  if ([response.actionIdentifier isEqualToString:@"YOUR-REGISTER-IDENTIFIER"]) {
    completion(UNNotificationContentExtensionResponseOptionDismiss);
  } else {
    completion(UNNotificationContentExtensionResponseOptionDoNotDismiss);
  }
}
```
{% endtab %}
{% endtabs %}

### Push-Benachrichtigungen schließen {#dismissing-pushes}

Push-Benachrichtigungen können automatisch durch einen Aktions-Button-Klick geschlossen werden. Es gibt drei vorgefertigte Optionen zum Schließen von Push-Benachrichtigungen, die wir empfehlen:

1. `completion(.dismiss)` – Schließt die Benachrichtigung
2. `completion(.doNotDismiss)` – Benachrichtigung bleibt geöffnet
3. `completion(.dismissAndForward)` – Push wird geschlossen und die Nutzer:innen werden in die Anwendung weitergeleitet