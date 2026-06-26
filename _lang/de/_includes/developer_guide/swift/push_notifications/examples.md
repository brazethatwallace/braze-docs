{% multi_lang_include developer_guide/prerequisites/swift.md %} Sie müssen außerdem [Push-Benachrichtigungen einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

{% alert note %}
Dieser Implementierungsleitfaden konzentriert sich auf eine Swift-Implementierung. Für Interessierte werden jedoch Objective-C-Snippets bereitgestellt.
{% endalert %}

## App-Erweiterungen für Benachrichtigungsinhalte {#notification-content-app-extensions}

![Zwei nebeneinander angezeigte Push-Nachrichten. Die Nachricht auf der linken Seite zeigt, wie ein Push mit der Standard-UI aussieht. Die Nachricht auf der rechten Seite zeigt einen Push für eine Kaffeelochkarte, der durch die Implementierung einer angepassten Push-UI erstellt wurde.]({% image_buster /assets/img/push_implementation_guide/push1.png %}){: style="max-width:65%;border:0;margin-top:10px"}

App-Erweiterungen für Benachrichtigungsinhalte bieten Ihnen eine hervorragende Möglichkeit zur Anpassung von Push-Benachrichtigungen. Sie zeigen eine angepasste Oberfläche für die Benachrichtigungen Ihrer App an, wenn eine Push-Benachrichtigung erweitert wird.

Push-Benachrichtigungen können auf drei verschiedene Arten erweitert werden:
- Langes Drücken auf das Push-Banner
- Auf dem Push-Banner nach unten streichen
- Das Banner nach links streichen und „Anzeigen“ auswählen

Diese angepassten Ansichten bieten intelligente Möglichkeiten für das Engagement Ihrer Kund:innen, indem sie verschiedene Arten von Inhalten anzeigen – darunter interaktive Benachrichtigungen, mit Nutzerdaten gefüllte Benachrichtigungen und sogar Push-Nachrichten, die Informationen wie Telefonnummern und E-Mail-Adressen erfassen können. Eines unserer bekannten Features bei Braze, [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), ist ein Paradebeispiel dafür, wie eine App-Erweiterung für Push-Benachrichtigungsinhalte aussehen kann!

### Voraussetzungen {#requirements}

![]({% image_buster /assets/img/push_implementation_guide/push15.png %}){: style="float:right;max-width:50%;margin-left:10px; border:0;margin-top:10px"}
- [Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) erfolgreich in Ihre App integriert
- Die folgenden Dateien, die von Xcode basierend auf Ihrer Programmiersprache generiert werden:

**Swift**<br>
- `NotificationViewController.swift`
- `MainInterface.storyboard`

**Objective-C**<br>
- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

## Interaktive Push-Benachrichtigung {#interactive-push-notification}

Push-Benachrichtigungen können auf Aktionen von Nutzer:innen innerhalb einer App-Erweiterung reagieren. Für Nutzer:innen mit iOS 12 oder höher bedeutet dies, dass Sie Ihre Push-Benachrichtigungen in vollständig interaktive Nachrichten verwandeln können! Dies bietet eine spannende Möglichkeit, Interaktivität in Ihre Aktionen und Anwendungen einzuführen. Ihre Push-Benachrichtigung kann zum Beispiel ein Spiel, ein Glücksrad für Rabatte oder einen „Gefällt mir“-Button zum Speichern eines Eintrags oder Songs enthalten.

Das folgende Beispiel zeigt eine Push-Benachrichtigung, bei der Nutzer:innen innerhalb der erweiterten Benachrichtigung ein Zuordnungsspiel spielen können.

![Ein Diagramm, das zeigt, wie die Phasen einer interaktiven Push-Benachrichtigung aussehen könnten. Eine Sequenz zeigt, wie eine Person auf eine Push-Benachrichtigung drückt, die ein interaktives Zuordnungsspiel anzeigt.]({% image_buster /assets/img/push_implementation_guide/push12.png %}){: style="border:0"}

### Dashboard-Konfiguration {#dashboard-configuration}

Um eine interaktive Push-Benachrichtigung zu erstellen, müssen Sie in Ihrem Dashboard eine angepasste Ansicht einrichten.

1. Klicken Sie auf der Seite **Campaigns** auf **Create Campaign**, um eine neue Push-Benachrichtigungskampagne zu starten.
2. Schalten Sie auf dem Tab **Compose** die **Notification Buttons** ein.
3. Geben Sie eine angepasste iOS-Kategorie in das Feld **iOS Notification Category** ein.
4. Legen Sie in der `.plist` Ihres Notification Content Extension Target das Attribut `UNNotificationExtensionCategory` auf Ihre angepasste iOS-Kategorie fest. Der hier angegebene Wert muss mit dem übereinstimmen, der im Braze-Dashboard unter **iOS Notification Category** eingestellt ist.
5. Setzen Sie den Schlüssel `UNNotificationExtensionInteractionEnabled` auf `true`, um Nutzerinteraktionen in einer Push-Benachrichtigung zu aktivieren.

![Die Optionen für Benachrichtigungsbuttons in den Einstellungen des Nachrichten-Editors.]({% image_buster /assets/img/push_implementation_guide/push16.png %}){: style="max-width:75%;border:0;margin-top:10px"}
![]({% image_buster /assets/img/push_implementation_guide/push17.png %}){: style="max-width:75%;border:0;margin-top:10px"}

## Personalisierte Push-Benachrichtigungen {#personalized-push-notifications}

![Zwei iPhones werden nebeneinander angezeigt. Das erste iPhone zeigt die nicht erweiterte Ansicht der Push-Nachricht. Das zweite iPhone zeigt die erweiterte Version der Push-Nachricht mit einer Fortschrittsanzeige, die zeigt, wie weit der Kurs fortgeschritten ist, den Namen der nächsten Sitzung und wann die nächste Sitzung abgeschlossen sein muss.]({% image_buster /assets/img/push_implementation_guide/push6.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

Push-Benachrichtigungen können nutzerspezifische Informationen innerhalb einer Inhaltserweiterung anzeigen. So können Sie nutzerfokussierte Push-Inhalte erstellen, z. B. die Option, Ihren Fortschritt auf verschiedenen Plattformen zu teilen, freigeschaltete Erfolge anzuzeigen oder Onboarding-Checklisten darzustellen. Dieses Beispiel zeigt eine Push-Benachrichtigung, die einer Person angezeigt wird, nachdem sie eine bestimmte Aufgabe im Braze-Lernkurs abgeschlossen hat. Durch Erweitern der Benachrichtigung können die Nutzer:innen ihren Fortschritt auf ihrem Lernpfad sehen. Die hier bereitgestellten Informationen sind nutzerspezifisch und können über einen API-Trigger ausgelöst werden, wenn eine Sitzung abgeschlossen ist oder eine bestimmte Nutzeraktion durchgeführt wird.

### Dashboard-Konfiguration {#dashboard-configuration-1}

Um eine personalisierte Push-Benachrichtigung zu erstellen, müssen Sie in Ihrem Dashboard eine angepasste Ansicht einrichten.

1. Klicken Sie auf der Seite **Campaigns** auf **Create Campaign**, um eine neue Push-Benachrichtigungskampagne zu starten.
2. Schalten Sie auf dem Tab **Compose** die **Notification Buttons** ein.
3. Geben Sie eine angepasste iOS-Kategorie in das Feld **iOS Notification Category** ein.
4. Erstellen Sie auf dem Tab **Settings** Schlüssel-Wert-Paare mit Standard-Liquid. Legen Sie die entsprechenden Nutzerattribute fest, die in der Nachricht angezeigt werden sollen. Diese Ansichten können basierend auf bestimmten Nutzerattributen eines bestimmten Nutzerprofils personalisiert werden.
5. Legen Sie in der `.plist` Ihres Notification Content Extension Target das Attribut `UNNotificationExtensionCategory` auf Ihre angepasste iOS-Kategorie fest. Der hier angegebene Wert muss mit dem übereinstimmen, der im Braze-Dashboard unter **iOS Notification Category** eingestellt ist.

![Vier Sätze von Schlüssel-Wert-Paaren, wobei „next_session_name“ und „next_session_complete_date“ als API-Trigger-Eigenschaft mit Liquid und „completed_session count“ und „total_session_count“ als angepasstes Nutzerattribut mit Liquid festgelegt werden.]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

### Umgang mit Schlüssel-Wert-Paaren {#handling-key-value-pairs}

Die Methode `didReceive` wird aufgerufen, wenn die App-Erweiterung für Benachrichtigungsinhalte eine Benachrichtigung erhalten hat. Diese Methode finden Sie in `NotificationViewController`. Die im Dashboard bereitgestellten Schlüssel-Wert-Paare werden im Code durch die Verwendung eines `userInfo`-Wörterbuchs dargestellt.

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

Push-Benachrichtigungen können Nutzerinformationen innerhalb einer Inhaltserweiterung erfassen und so die Grenzen dessen erweitern, was mit einem Push möglich ist. Durch das Anfordern von Nutzereingaben über Push-Benachrichtigungen können Sie nicht nur grundlegende Informationen wie Name oder E-Mail abfragen, sondern Nutzer:innen auch auffordern, Feedback zu geben oder ein unvollständiges Nutzerprofil zu vervollständigen.

{% alert tip %}
Weitere Informationen finden Sie unter [Protokollierung von Daten für Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/analytics/logging_channel_data/push_notifications/).
{% endalert %}

Im folgenden Ablauf kann die angepasste Ansicht auf Zustandsänderungen reagieren. Diese Zustandsänderungskomponenten werden in jedem Bild dargestellt.

1. Die Person erhält eine Push-Benachrichtigung.
2. Der Push wird geöffnet. Nach dem Erweitern fordert der Push zur Eingabe von Informationen auf. In diesem Beispiel wird die E-Mail-Adresse abgefragt, aber Sie können jede beliebige Information anfordern.
3. Die Informationen werden eingegeben, und wenn sie im erwarteten Format vorliegen, wird der Registrierungs-Button angezeigt.
3. Die Bestätigungsansicht wird angezeigt und der Push wird geschlossen.


### Dashboard-Konfiguration {#dashboard-configuration-2}

Um eine Push-Benachrichtigung zur Informationserfassung zu erstellen, müssen Sie in Ihrem Dashboard eine angepasste Ansicht einrichten.

1. Klicken Sie auf der Seite **Campaigns** auf **Create Campaign**, um eine neue Push-Benachrichtigungskampagne zu starten.
2. Schalten Sie auf dem Tab **Compose** die **Notification Buttons** ein.
3. Geben Sie eine angepasste iOS-Kategorie in das Feld **iOS Notification Category** ein.
4. Erstellen Sie auf dem Tab **Settings** Schlüssel-Wert-Paare mit Standard-Liquid. Legen Sie die entsprechenden Nutzerattribute fest, die in der Nachricht angezeigt werden sollen.
5. Legen Sie in der `.plist` Ihres Notification Content Extension Target das Attribut `UNNotificationExtensionCategory` auf Ihre angepasste iOS-Kategorie fest. Der hier angegebene Wert muss mit dem übereinstimmen, der im Braze-Dashboard unter **iOS Notification Category** eingestellt ist.

Wie im Beispiel zu sehen, können Sie auch ein Bild in Ihre Push-Benachrichtigung einfügen. Dazu müssen Sie [Rich-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=swift) integrieren, den Benachrichtigungsstil in Ihrer Campaign auf Rich-Benachrichtigung einstellen und ein Rich-Push-Bild einfügen.

![Eine Push-Nachricht mit drei Sätzen von Schlüssel-Wert-Paaren. 1. „Braze_id“ als Liquid-Aufruf zum Abrufen der Braze-ID festgelegt. 2. „cert_title“ als „Braze Marketer Certification“ festgelegt. 3. „Cert_description“ als „Certified Braze marketers drive…“ festgelegt.]({% image_buster /assets/img/push_implementation_guide/push9.png %})

### Verarbeitung von Button-Aktionen {#handling-button-actions}

Jeder Aktions-Button ist eindeutig gekennzeichnet. Der Code prüft, ob der Antwort-Bezeichner mit dem `actionIdentifier` übereinstimmt, und weiß dann, dass die Person auf den Aktions-Button geklickt hat.

**Verarbeitung von Antworten auf Aktions-Buttons in Push-Benachrichtigungen**<br>

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

### Ausblenden von Pushes {#dismissing-pushes}

Push-Benachrichtigungen können durch Drücken eines Aktions-Buttons automatisch ausgeblendet werden. Es gibt drei vorgefertigte Optionen zum Ausblenden von Push-Nachrichten, die wir empfehlen:

1. `completion(.dismiss)` – Blendet die Benachrichtigung aus
2. `completion(.doNotDismiss)` – Die Benachrichtigung bleibt geöffnet
3. `completion(.dismissAndForward)` – Der Push wird ausgeblendet und die Person wird in die Anwendung weitergeleitet