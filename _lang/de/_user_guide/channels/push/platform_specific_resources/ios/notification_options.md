---
nav_title: "Benachrichtigungsoptionen"
article_title: iOS-Benachrichtigungsoptionen
page_order: 2
page_layout: reference
description: "Dieser Referenzartikel behandelt iOS-Benachrichtigungsoptionen wie kritische Warnungen, stille Benachrichtigungen, vorläufige Push-Benachrichtigungen und mehr."

platform: iOS
channel:
  - push
---

# Benachrichtigungsoptionen {#notification-options}

> Mit der Veröffentlichung von Apples iOS 12 bietet Braze Unterstützung für mehrere seiner Features, darunter [Benachrichtigungsgruppen](#notification-groups), [Stille Benachrichtigungen/Vorläufige Autorisierung](#provisional-push-authentication--quiet-notifications) und [Kritische Warnungen](#critical-alerts).

## Benachrichtigungsgruppen {#notification-groups}

Wenn Sie Ihre Nachrichten kategorisieren und in der Benachrichtigungsleiste Ihrer Nutzer:innen gruppieren möchten, können Sie die iOS-Funktion für Benachrichtigungsgruppen über Braze nutzen.

Erstellen Sie Ihre iOS-Push-Campaign und wechseln Sie dann zum Tab **Settings**. Öffnen Sie dort das Dropdown-Menü **Notification group**.

![Der Tab „Settings“ mit einem Dropdown-Menü „Notification group“, in dem der Wert „Coupons“ ausgewählt ist.]({% image_buster /assets/img_archive/notification_group_dropdown.png %}){: style="max-width:50%;" }

Wählen Sie Ihre Benachrichtigungsgruppen aus dem Dropdown-Menü aus. Falls die Einstellungen Ihrer Benachrichtigungsgruppe fehlerhaft sind oder Sie **None** im Dropdown auswählen, wird die Nachricht automatisch als normale Nachricht an alle definierten Nutzer:innen im Workspace gesendet.

Wenn hier keine Benachrichtigungsgruppen aufgelistet sind, können Sie eine mithilfe der iOS Thread ID hinzufügen. Sie benötigen eine iOS Thread ID für jede Benachrichtigungsgruppe, die Sie hinzufügen möchten. Fügen Sie diese dann zu Ihren Benachrichtigungsgruppen hinzu, indem Sie im Dropdown-Menü auf **Manage Notification Groups** klicken und die erforderlichen Felder im Fenster **Manage iOS Push Notification Groups** ausfüllen.

![Fenster zur Verwaltung von iOS-Push-Benachrichtigungsgruppen.]({% image_buster /assets/img_archive/managenotgroups.png %}){: style="max-width:70%;" }

Erstellen Sie Ihre iOS-Push-Campaign und schauen Sie dann oben im Composer nach. Dort finden Sie ein Dropdown-Menü mit der Bezeichnung **Notification Groups**.

### Zusammenfassungsargumente {#summary-arguments}

Neben der Gruppierung von Benachrichtigungen nach Thread IDs ermöglicht Apple Ihnen auch, die Zusammenfassungen zu bearbeiten, die angezeigt werden, wenn Benachrichtigungen gruppiert sind. Braze-Nutzer:innen können beim Erstellen einer Push-Campaign mit unserem Tool die Zusammenfassungskategorie, die Zusammenfassungsanzahl und das Zusammenfassungsargument festlegen.

{% alert tip %}
Beachten Sie, dass die Art und Weise, wie Benachrichtigungen mit derselben Thread ID in der Benachrichtigungsleiste gruppiert werden, vom Betriebssystem gesteuert wird. iOS kann Benachrichtigungen mit derselben Thread ID je nach Einschätzung separat oder gruppiert anzeigen.
{% endalert %}

Aktivieren Sie das Kontrollkästchen **Alert Options** im **Push Composer**.

Wählen Sie dann `summary-arg` und `summary-arg-count` als Schlüssel aus und geben Sie die entsprechenden Werte in der zugehörigen Spalte ein. Wenn Sie keinen Wert für `summary-arg` festlegen, wird standardmäßig 1 verwendet.

### Zusammenfassungskategorien {#summary-categories}

Mit Zusammenfassungskategorien können Sie die gesamte Zusammenfassung anpassen, die angezeigt wird, wenn Benachrichtigungen gruppiert werden. Sie können mehrere Kategorien erstellen und anwenden.

Um eine Kategorie in Ihrer Nachricht zu verwenden, arbeiten Sie mit Ihren Entwickler:innen zusammen, um die Implementierung anhand des folgenden Beispiels umzusetzen:

```
UNNotificationCategory *newsCategory = [UNNotificationCategory categoryWithIdentifier:@"news"
                                                      actions:@[likeAction, unlikeAction]
                                                      intentIdentifiers:@[]
                                                      hiddenPreviewsBodyPlaceholder:@""
                                                      categorySummaryFormat:@"%u more news articles from %@"
                                                       Options:0];
```

{% alert important %}
Hierfür ist kein SDK-Update erforderlich.
{% endalert %}

{% alert tip %}
Beachten Sie, dass `%u` und `%@` Formatierungsstrings für die Zusammenfassungsanzahl bzw. das Zusammenfassungsargument sind. Wenn die Zusammenfassung angezeigt wird, werden diese Platzhalter durch die Werte für `summary-count` und `summary-arg` ersetzt.
{% endalert %}

Sobald dies in Ihrer App eingerichtet ist, verwenden Sie die Zusammenfassungskategorie, indem Sie das Kontrollkästchen **Notification Buttons** aktivieren und **Enter Pre-registered iOS Category** auswählen.

Geben Sie dann den Bezeichner der Zusammenfassungskategorie ein, den Sie in Ihrer App festgelegt haben.

### Vorläufige Push-Authentifizierung und stille Benachrichtigungen {#provisional-push}

Apple bietet Marken die Möglichkeit, stille Push-Benachrichtigungen an die Benachrichtigungszentren ihrer Nutzer:innen zu senden, bevor diese offiziell und ausdrücklich zugestimmt haben. So erhalten Sie die Chance, den Wert Ihrer Nachrichten frühzeitig zu demonstrieren. Sie müssen lediglich die [vorläufige Push-Benachrichtigung einrichten](#set-up-provisional-push-notifications) in Ihrer App – danach erhalten alle Nutzer:innen mit einem vorläufigen Push-Token / Textbaustein Ihre Nachrichten.

Im Gegensatz zu einem herkömmlichen iOS-Push-Token / Textbaustein fungiert ein vorläufiges Push-Token / Textbaustein als eine Art „Probezugang“, der es Marken ermöglicht, neue Nutzer:innen zu erreichen, bevor diese die native Push-Opt-in-Aufforderung von Apple gesehen und angeklickt haben. Mit diesem Feature wird Ihre Push-Benachrichtigung direkt in der Benachrichtigungsleiste Ihrer neuen Nutzer:innen zugestellt – mit der Option, zukünftige Benachrichtigungen zu „behalten“ oder „abzuschalten“. Anstatt einen „Opt-in“-Prozess zu durchlaufen, erleben Nutzer:innen eher einen „Opt-out“-Prozess.

{% alert tip %}
Die vorläufige Autorisierung hat das Potenzial, Ihre Opt-in-Rate drastisch zu erhöhen – allerdings nur, wenn Nutzer:innen Wert in Ihren Nachrichten erkennen. Stellen Sie sicher, dass Sie unsere Features für [Nutzersegmentierung]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), [Standort-Targeting]({{site.baseurl}}/user_guide/audience/locations_and_geofences) und [Personalisierung]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) nutzen, um sicherzustellen, dass die richtigen Nutzer:innen diese „Probe“-Benachrichtigungen zur richtigen Zeit erhalten. Anschließend können Sie Nutzer:innen ermutigen, sich vollständig für Ihre Push-Benachrichtigungen zu entscheiden, in dem Wissen, dass diese einen Mehrwert für das App-Erlebnis Ihrer Nutzer:innen bieten.
{% endalert %}

Unabhängig von der Wahl der Nutzer:innen wird das entsprechende Token / Textbaustein oder der entsprechende [Abo-Status]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states) in ihren [Kontakteinstellungen]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#engagement-tab) im Tab **Engagement** ihres Nutzerprofils hinzugefügt.

![Kontakteinstellungen mit einem Push-Abo-Status „subscribed“.]({% image_buster /assets/img/profile-push-prov-auth.png %}){: width="50%"}

Sie können Ihre Nutzer:innen mithilfe unserer [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) danach ansprechen, ob sie vorläufig autorisiert sind oder nicht.

![Panel „Segment Details“ mit dem Beispiel-Segmentfilter „Provisionally Authorized on iOS Stopwatch (iOS) is true“, um Nutzer:innen anzusprechen.]({% image_buster /assets/img/segment-push-prov-auth.png %})

{% alert tip %}
Wenn Nutzer:innen sich dafür entscheiden, vorläufige Push-Benachrichtigungen von Ihnen „abzuschalten“, werden sie keine weiteren vorläufigen Push-Nachrichten von Ihnen sehen. Überlegen Sie sich den Nachrichteninhalt und die Sendefrequenz bei dieser Funktion sorgfältig!
{% endalert %}

{% alert important %}
Wenn Sie zusätzliche Push-Aufforderungen oder [In-App-Push-Primer](https://www.braze.com/resources/glossary/priming-for-push/) (eine In-App-Nachricht, die Nutzer:innen zum Opt-in für Push-Benachrichtigungen ermutigt) verwenden, wenden Sie sich an Ihre Braze-Vertretung für zusätzliche Unterstützung.
{% endalert %}

#### Vorläufige Push-Benachrichtigungen einrichten {#set-up-provisional-push-notifications}

Braze ermöglicht es Ihnen, sich für die vorläufige Authentifizierung zu registrieren, indem Sie Ihren Code im Token / Textbaustein-Registrierungs-Snippet innerhalb Ihrer Braze iOS SDK-Implementierung aktualisieren. Verwenden Sie die folgenden Snippets als Beispiel (senden Sie diese an Ihre Entwickler:innen oder stellen Sie sicher, dass diese die [vorläufige Push-Authentifizierung während des Integrationsprozesses implementieren]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift)).

{% alert warning %}
Die Implementierung der vorläufigen Push-Authentifizierung unterstützt nur iOS 12+ und gibt bei einem früheren Deployment-Target einen Fehler aus. Weitere Informationen finden Sie [in unserer ausführlicheren Implementierungsdokumentation hier]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift).
{% endalert %}

{% tabs local %}
  {% tab Swift %}
**Swift**

```
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
```
  {% endtab %}
  {% tab Objective-C %}

**Objective-C**

```
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
center.delegate = self;
UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
if (@available(iOS 12.0, *)) {
    options = options | UNAuthorizationOptionProvisional;
}
```
  {% endtab %}
{% endtabs %}

### Unterbrechungsstufe (iOS 15+) {#interruption-level}

Mit dem neuen Fokusmodus von iOS 15 haben Nutzer:innen mehr Kontrolle darüber, wann App-Benachrichtigungen sie mit einem Ton oder einer Vibration „unterbrechen“ können.

![iOS-Benachrichtigungseinstellungen, die zeigen, dass Benachrichtigungen für sofortige Zustellung aktiviert und zeitkritische Benachrichtigungen eingeschaltet sind.]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="max-width:40%"}

Apps können jetzt angeben, welche Unterbrechungsstufe eine Benachrichtigung basierend auf ihrer Dringlichkeit haben soll.

Um die Unterbrechungsstufe für eine iOS-Push-Benachrichtigung zu ändern, wählen Sie den Tab **Settings** und wählen Sie die gewünschte Stufe aus dem Dropdown-Menü **Interruption Level** aus.

![Dropdown-Menü zur Auswahl der Unterbrechungsstufe.]({% image_buster /assets/img/ios/interruption_level.png %}){: style="max-width:50%"}

Dieses Feature hat keine Mindestanforderungen an die SDK-Version, wird jedoch nur auf Geräten mit iOS 15+ angewendet.

Bedenken Sie, dass die Nutzer:innen letztlich die Kontrolle über ihren Fokus haben und selbst wenn eine zeitkritische Benachrichtigung zugestellt wird, können sie festlegen, welche Apps ihren Fokus nicht durchbrechen dürfen.

Die folgende Tabelle enthält die Unterbrechungsstufen und ihre Beschreibungen.

| Unterbrechungsstufe | Beschreibung | Wann verwenden | Durchbricht den Fokusmodus |
|--|--|--|--|
| [Passive](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/passive) | Sendet eine Benachrichtigung ohne Ton, Vibration oder Bildschirmaktivierung. | Benachrichtigungen, die keine sofortige Aufmerksamkeit erfordern. | Nein |
| [Active](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active) (Standard) | Erzeugt nur dann einen Ton, eine Vibration und aktiviert den Bildschirm, wenn der/die Nutzer:in sich nicht im Fokusmodus befindet. | Benachrichtigungen, die sofortige Aufmerksamkeit erfordern, es sei denn, der/die Nutzer:in hat den Fokusmodus aktiviert. | Nein |
| [Time Sensitive](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive) | Erzeugt einen Ton, vibriert und aktiviert den Bildschirm auch im Fokusmodus. Hierfür muss die **Time Sensitive Notifications capability** in Xcode zu Ihrer App hinzugefügt werden. | Zeitkritische Benachrichtigungen, die Nutzer:innen unabhängig von ihrem Fokusmodus stören sollen, wie z. B. Mitfahr- oder Lieferbenachrichtigungen. | Ja |
| [Critical](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical) | Erzeugt einen Ton, vibriert und aktiviert den Bildschirm auch bei aktiviertem **Nicht stören**-Schalter. Dies [erfordert eine ausdrückliche Genehmigung von Apple](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/). | Notfälle wie schwere Unwetterwarnungen oder Sicherheitswarnungen. | Ja |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Unterbrechungsstufe (iOS 15+)" }

### Relevanzbewertung (iOS 15+) {#relevance-score}

![Eine Benachrichtigungszusammenfassung für iOS mit dem Titel „Your Evening Summary“ und drei Benachrichtigungen.]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15 bietet Nutzer:innen außerdem eine neue Möglichkeit, optional eine Zusammenfassungsgruppierung mehrerer Benachrichtigungen zu bestimmten Tageszeiten zu planen. Damit sollen ständige Unterbrechungen durch Benachrichtigungen vermieden werden, die keine sofortige Aufmerksamkeit erfordern.

Apps können angeben, welche Push-Benachrichtigungen am relevantesten sind, indem sie eine **Relevanzbewertung** festlegen. Apple verwendet diese Bewertung, um zu bestimmen, welche Benachrichtigungen in der geplanten Benachrichtigungszusammenfassung hervorgehoben werden sollen, während andere verfügbar sind, wenn Nutzer:innen in die Zusammenfassung klicken.

Alle Benachrichtigungen sind weiterhin in der Benachrichtigungszentrale der Nutzer:innen zugänglich.

Um die Relevanzbewertung einer iOS-Benachrichtigung festzulegen, geben Sie im Tab **Settings** einen Wert zwischen `0.0` und `1.0` ein. Beispielsweise sollte die wichtigste Nachricht mit `1.0` gesendet werden, während eine Nachricht mittlerer Wichtigkeit mit `0.5` gesendet werden kann.

![Relevanzbewertung von „0.5“.]({% image_buster /assets/img/ios/relevance-score.png %}){: style="max-width:80%;"}

Dieses Feature hat keine Mindestanforderungen an die SDK-Version, wird jedoch nur auf Geräten mit iOS 15+ angewendet.

Weitere Informationen zu maximalen Nachrichtenlängen für verschiedene Nachrichtentypen finden Sie in den folgenden Ressourcen:

- [Bild- und Textspezifikationen]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats)
- [iOS-Zeichenanzahlrichtlinien]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications#character-count)