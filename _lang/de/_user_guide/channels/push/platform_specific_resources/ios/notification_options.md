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

Wenn Sie Ihre Nachrichten kategorisieren und in der Benachrichtigungsleiste Ihrer Nutzer:innen gruppieren möchten, können Sie das iOS-Feature „Benachrichtigungsgruppen“ über Braze nutzen.

Erstellen Sie Ihre iOS-Push-Campaign und gehen Sie dann zum Tab **Settings**. Öffnen Sie dort das Dropdown-Menü **Notification group**.

![Der Tab „Settings“ mit einem Dropdown-Menü „Notification group“, in dem der Wert „Coupons“ ausgewählt ist.]({% image_buster /assets/img_archive/notification_group_dropdown.png %}){: style="max-width:50%;" }

Wählen Sie Ihre Benachrichtigungsgruppen aus dem Dropdown-Menü aus. Wenn Ihre Benachrichtigungsgruppen-Einstellungen nicht funktionieren oder Sie **None** aus dem Dropdown-Menü auswählen, wird die Nachricht automatisch wie gewohnt an alle definierten Nutzer:innen im Workspace gesendet.

Wenn hier keine Benachrichtigungsgruppen aufgelistet sind, können Sie eine über die iOS-Thread-ID hinzufügen. Sie benötigen eine iOS-Thread-ID für jede Benachrichtigungsgruppe, die Sie hinzufügen möchten. Fügen Sie sie dann zu Ihren Benachrichtigungsgruppen hinzu, indem Sie im Dropdown-Menü auf **Manage Notification Groups** klicken und die erforderlichen Felder im erscheinenden Fenster **Manage iOS Push Notification Groups** ausfüllen.

![Fenster zum Verwalten von iOS-Push-Benachrichtigungsgruppen.]({% image_buster /assets/img_archive/managenotgroups.png %}){: style="max-width:70%;" }

Erstellen Sie Ihre iOS-Push-Campaign und schauen Sie dann oben im Composer nach. Dort finden Sie ein Dropdown-Menü mit der Bezeichnung **Notification Groups**.

### Zusammenfassungsargumente {#summary-arguments}

Zusätzlich zur Gruppierung von Benachrichtigungen nach Thread-IDs ermöglicht Apple die Bearbeitung der Zusammenfassungen, die angezeigt werden, wenn Benachrichtigungen gruppiert sind. Braze-Nutzer:innen können die Zusammenfassungskategorie, die Zusammenfassungsanzahl und das Zusammenfassungsargument beim Erstellen einer Push-Campaign mit unserem Tool angeben.

{% alert tip %}
Beachten Sie, dass die Art und Weise, wie Benachrichtigungen mit derselben Thread-ID in der Benachrichtigungsleiste gruppiert werden, vom Betriebssystem gesteuert wird. iOS kann Benachrichtigungen mit derselben Thread-ID je nach Optimierung einzeln oder in Gruppen anzeigen.
{% endalert %}

Aktivieren Sie das Kontrollkästchen **Alert Options** im **Push Composer**.

Wählen Sie dann `summary-arg` und `summary-arg-count` als Schlüssel aus und geben Sie die entsprechenden Werte in der zugehörigen Spalte ein. Wenn Sie keinen Wert für `summary-arg` festlegen, wird standardmäßig 1 verwendet.

### Zusammenfassungskategorien {#summary-categories}

Zusammenfassungskategorien ermöglichen es Ihnen, die gesamte Zusammenfassung anzupassen, die angezeigt wird, wenn Benachrichtigungen gruppiert werden. Sie können mehrere Kategorien erstellen und anwenden.

Um eine Kategorie in Ihrer Nachricht zu verwenden, arbeiten Sie mit Ihren Entwickler:innen zusammen, um die Implementierung anhand des folgenden Beispiels vorzunehmen:

```
UNNotificationCategory *newsCategory = [UNNotificationCategory categoryWithIdentifier:@"news"
                                                      actions:@[likeAction, unlikeAction]
                                                      intentIdentifiers:@[]
                                                      hiddenPreviewsBodyPlaceholder:@""
                                                      categorySummaryFormat:@"%u more news articles from %@"
                                                       Options:0];
```

{% alert important %}
Dies erfordert kein SDK-Update.
{% endalert %}

{% alert tip %}
Beachten Sie, dass `%u` und `%@` Formatierungsstrings für die Zusammenfassungsanzahl bzw. das Zusammenfassungsargument sind. Wenn die Zusammenfassung angezeigt wird, werden diese Platzhalter durch die Werte für `summary-count` und `summary-arg` ersetzt.
{% endalert %}

Sobald dies in Ihrer App eingerichtet ist, verwenden Sie die Zusammenfassungskategorie, indem Sie das Kontrollkästchen **Notification Buttons** aktivieren und **Enter Pre-registered iOS Category** auswählen.

Geben Sie dann den Zusammenfassungskategorie-Bezeichner ein, den Sie in Ihrer App festgelegt haben.

### Vorläufige Push-Authentifizierung und stille Benachrichtigungen {#provisional-push}

Apple bietet Marken die Möglichkeit, stille Push-Benachrichtigungen an die Benachrichtigungszentren ihrer Nutzer:innen zu senden, bevor diese offiziell und ausdrücklich zugestimmt haben. So haben Sie die Chance, den Wert Ihrer Nachrichten frühzeitig zu demonstrieren. Sie müssen lediglich [vorläufige Push-Benachrichtigungen einrichten](#set-up-provisional-push-notifications) in Ihrer App, und dann erhalten alle Nutzer:innen mit einem vorläufigen Push-Token Ihre Nachrichten.

Im Gegensatz zu einem herkömmlichen iOS-Push-Token fungiert ein vorläufiges Push-Token als „Probepass“, der es Marken ermöglicht, neue Nutzer:innen zu erreichen, bevor diese die native Push-Opt-in-Aufforderung von Apple gesehen und angeklickt haben. Mit diesem Feature wird Ihre Push-Benachrichtigung direkt in der Benachrichtigungsleiste Ihrer neuen Nutzer:innen zugestellt – mit der Option, zukünftige Benachrichtigungen zu „Behalten“ oder zu „Deaktivieren“. Anstatt eine „Opt-in“-Journey zu erleben, erleben Nutzer:innen eher eine „Opt-out“-Journey.

{% alert tip %}
Die vorläufige Autorisierung hat das Potenzial, Ihre Opt-in-Rate dramatisch zu steigern, aber nur, wenn Nutzer:innen einen Wert in Ihren Nachrichten sehen. Nutzen Sie unbedingt unsere Features für [Nutzersegmentierung]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/), [Standort-Targeting]({{site.baseurl}}/user_guide/audience/locations_and_geofences/) und [Personalisierung]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/), um sicherzustellen, dass die richtigen Nutzer:innen diese „Probe“-Benachrichtigungen zur richtigen Zeit erhalten. Dann können Sie Nutzer:innen ermutigen, sich vollständig für Ihre Push-Benachrichtigungen zu entscheiden, in dem Wissen, dass diese einen Mehrwert für das App-Erlebnis Ihrer Nutzer:innen bieten.
{% endalert %}

Welche Option die Nutzer:innen auch wählen, das entsprechende Token oder der entsprechende [Abo-Status]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states/) wird zu ihren [Kontakteinstellungen]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/#engagement-tab) unter dem Tab **Engagement** in ihrem Nutzerprofil hinzugefügt.

![Kontakteinstellungen mit einem Push-Abo-Status.]({% image_buster /assets/img/profile-push-prov-auth.png %}){: width="50%"}

Sie können Ihre Nutzer:innen mithilfe unserer [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/) danach ansprechen, ob sie vorläufig autorisiert sind oder nicht.

![Segment-Details-Panel mit dem Beispiel-Segmentfilter „Provisionally Authorized on iOS Stopwatch (iOS) is true“, um Nutzer:innen anzusprechen.]({% image_buster /assets/img/segment-push-prov-auth.png %})

{% alert tip %}
Wenn Nutzer:innen sich entscheiden, vorläufige Push-Benachrichtigungen von Ihnen zu „Deaktivieren“, werden sie keine weiteren vorläufigen Push-Nachrichten von Ihnen sehen. Seien Sie bedacht bei den Nachrichteninhalten und der Sendefrequenz, die Sie mit dieser Funktionalität verwenden!
{% endalert %}

{% alert important %}
Wenn Sie zusätzliche Push-Aufforderungen oder [In-App-Push-Primer](https://www.braze.com/resources/glossary/priming-for-push/) (eine In-App-Nachricht, die Nutzer:innen ermutigt, Push-Benachrichtigungen zu aktivieren) verwenden, wenden Sie sich an Ihre Braze-Vertretung für zusätzliche Beratung.
{% endalert %}

#### Vorläufige Push-Benachrichtigungen einrichten {#set-up-provisional-push-notifications}

Braze ermöglicht es Ihnen, sich für die vorläufige Authentifizierung zu registrieren, indem Sie Ihren Code in Ihrem Token-Registrierungs-Snippet innerhalb Ihrer Braze iOS SDK-Implementierung aktualisieren. Verwenden Sie die folgenden Snippets als Beispiel (senden Sie diese an Ihre Entwickler:innen oder stellen Sie sicher, dass sie [die vorläufige Push-Authentifizierung während des Integrationsprozesses implementieren]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10)).

{% alert warning %}
Die Implementierung der vorläufigen Push-Authentifizierung unterstützt nur iOS 12+ und führt zu einem Fehler, wenn das Deployment-Ziel davor liegt. Mehr dazu erfahren Sie [in unserer ausführlicheren Implementierungsdokumentation hier]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10).
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

![iOS-Benachrichtigungseinstellungen-Seite, die zeigt, dass Benachrichtigungen für sofortige Zustellung aktiviert sind und zeitkritische Benachrichtigungen aktiviert sind.]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="max-width:40%"}

Apps können nun angeben, welche Unterbrechungsstufe eine Benachrichtigung basierend auf ihrer Dringlichkeit haben soll.

Um die Unterbrechungsstufe für eine iOS-Push-Benachrichtigung zu ändern, wählen Sie den Tab **Settings** und wählen Sie die gewünschte Stufe aus dem Dropdown-Menü **Interruption Level**.

![Dropdown-Menü zur Auswahl der Unterbrechungsstufe.]({% image_buster /assets/img/ios/interruption_level.png %}){: style="max-width:50%"}

Dieses Feature hat keine Mindestanforderungen an die SDK-Version, wird aber nur auf Geräten mit iOS 15+ angewendet.

Bedenken Sie, dass die Nutzer:innen letztendlich die Kontrolle über ihren Fokus haben, und selbst wenn eine zeitkritische Benachrichtigung zugestellt wird, können sie festlegen, welche Apps ihren Fokus nicht durchbrechen dürfen.

Die folgende Tabelle enthält die Unterbrechungsstufen und ihre Beschreibungen.

| Unterbrechungsstufe | Beschreibung | Wann verwenden | Durchbricht Fokusmodus |
|--|--|--|--|
| [Passiv](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/passive) | Sendet eine Benachrichtigung ohne Ton, Vibration oder Bildschirmaktivierung. | Benachrichtigungen, die keine sofortige Aufmerksamkeit erfordern. | Nein |
| [Aktiv](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active) (Standard) | Erzeugt nur dann einen Ton, eine Vibration und aktiviert den Bildschirm, wenn sich die Nutzer:innen nicht im Fokusmodus befinden. | Benachrichtigungen, die sofortige Aufmerksamkeit erfordern, es sei denn, die Nutzer:innen haben den Fokusmodus aktiviert. | Nein |
| [Zeitkritisch](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive) | Erzeugt einen Ton, vibriert und aktiviert den Bildschirm auch im Fokusmodus. Dies erfordert, dass die **Time Sensitive Notifications capability** in Xcode zu Ihrer App hinzugefügt wird. | Zeitkritische Benachrichtigungen, die Nutzer:innen unabhängig von ihrem Fokusmodus stören sollten, wie z. B. Mitfahrgelegenheits- oder Lieferbenachrichtigungen. | Ja |
| [Kritisch](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical) | Erzeugt einen Ton, vibriert und aktiviert den Bildschirm, selbst wenn der **Nicht stören**-Schalter des Telefons aktiviert ist. Dies [erfordert eine ausdrückliche Genehmigung von Apple](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/). | Notfälle wie schwere Unwetterwarnungen oder Sicherheitswarnungen. | Ja |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Relevanzbewertung (iOS 15+) {#relevance-score}

![Eine Benachrichtigungszusammenfassung für iOS mit dem Titel „Your Evening Summary“ mit drei Benachrichtigungen.]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15 führt außerdem eine neue Möglichkeit ein, mit der Nutzer:innen optional eine Zusammenfassungsgruppierung mehrerer Benachrichtigungen zu festgelegten Zeiten über den Tag hinweg planen können. Dies dient dazu, ständige Unterbrechungen im Tagesverlauf für Benachrichtigungen zu vermeiden, die keine sofortige Aufmerksamkeit erfordern.

Apps können angeben, welche Push-Benachrichtigungen am relevantesten sind, indem sie eine **Relevanzbewertung** festlegen. Apple verwendet diese Bewertung, um zu bestimmen, welche Benachrichtigungen in der geplanten Benachrichtigungszusammenfassung hervorgehoben werden sollen, während andere verfügbar sind, wenn Nutzer:innen in die Zusammenfassung klicken.

Alle Benachrichtigungen sind weiterhin in der Benachrichtigungszentrale der Nutzer:innen zugänglich.

Um die Relevanzbewertung einer iOS-Benachrichtigung festzulegen, geben Sie einen Wert zwischen `0.0` und `1.0` im Tab **Settings** ein. Beispielsweise sollte die wichtigste Nachricht mit `1.0` gesendet werden, während eine Nachricht mittlerer Wichtigkeit mit `0.5` gesendet werden kann.

![Relevanzbewertung von „0.5“.]({% image_buster /assets/img/ios/relevance-score.png %}){: style="max-width:80%;"}

Dieses Feature hat keine Mindestanforderungen an die SDK-Version, wird aber nur auf Geräten mit iOS 15+ angewendet.

Weitere Informationen zu maximalen Nachrichtenlängen für verschiedene Nachrichtentypen finden Sie in den folgenden Ressourcen:

- [Bild- und Textspezifikationen]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats/)
- [iOS-Zeichenanzahl-Richtlinien]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications/#character-count)