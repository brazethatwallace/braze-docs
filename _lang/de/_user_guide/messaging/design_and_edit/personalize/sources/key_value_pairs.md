---
nav_title: Schlüssel-Wert-Paare
article_title: Schlüssel-Wert-Paare
page_order: 4
description: "Dieser Referenzartikel behandelt Schlüssel-Wert-Paare und wie Sie diese verwenden können, um zusätzliche Daten-Payloads an Nutzergeräte zu senden."
channel:
  - push
  - in-app messages
  - content cards

---

# Schlüssel-Wert-Paare {#key-value-pairs}

> Diese Seite beschreibt, wie Sie Schlüssel-Wert-Paare verwenden können, um zusätzliche Daten-Payloads an Nutzergeräte zu senden. Dieses Feature ist über Push-, In-App-, E-Mail- und Content-Card-Messaging-Kanäle verfügbar.

Verwenden Sie Schlüssel-Wert-Paare, um strukturierte Metadaten zu Nachrichten hinzuzufügen. Diese zusätzlichen Daten-Payloads können Nachrichten mit weiteren kontextuellen Informationen anreichern, die beeinflussen können, wie eine Nachricht dargestellt oder verarbeitet wird.

Da Schlüssel-Wert-Paare Metadaten sind, sind diese Daten nicht unbedingt für die Empfänger:innen sichtbar, können aber von Ihren verbundenen Systemen oder Prozessen verwendet werden, um die Nachrichtenverarbeitung anzupassen.

Jedes Paar besteht aus:

- **Schlüssel:** Der Bezeichner (Beispiel: `utm_source`)
- **Wert:** Die zugehörigen Daten (Beispiel: `newsletter`)

## Anwendungsfälle {#use-cases}

Hier sind einige Beispiel-Anwendungsfälle für das Hinzufügen von Metadaten mit Schlüssel-Wert-Paaren:

1. **Tracking-Parameter:** UTM-Parameter für Analysezwecke anhängen
   - Schlüssel: `utm_campaign`
   - Wert: `spring_sale`
2. **Angepasste Tags:** Tags für internes Routing oder Kategorisierung hinzufügen
   - Schlüssel: `priority`
   - Wert: `high`
3. **Verhaltens-Trigger or triggern:** Metadaten, die verwendet werden, um In-App-Verhaltensweisen zu Trigger or triggern or triggern oder anzupassen
   - Schlüssel: `deep_link`
   - Wert: `app://promo-page`

## Push-Benachrichtigungen {#push-notifications}

Schlüssel-Wert-Paare können zu Android-, iOS- und Web-Push-Benachrichtigungen hinzugefügt werden. Sie können Schlüssel-Wert-Paare verwenden, um interne Metriken und App-Inhalte zu Update or aktualisieren or aktualisieren oder Push-Benachrichtigungseigenschaften wie Alarmpriorisierung, Lokalisierung und Töne anzupassen.

Wählen Sie im Nachrichten-Editor den Tab **Einstellungen**, wählen Sie **Neues Paar hinzufügen** und geben Sie Ihre Schlüssel-Wert-Paare an.

Wenn Sie Schlüssel-Wert-Paare im Nachrichten-Editor hinzufügen, werden Werte als Strings gesendet. Bei iOS-Push werden reservierte Apple Push Notification service (APNs) Alert-Schlüssel, die Sie über **Alert-Optionen** hinzufügen (wie `loc-args` für Lokalisierungsargumente), mit den korrekten JSON-Typen in der Payload formatiert. Bei angepassten Schlüsseln empfängt Ihre App String-Werte, sofern Sie diese nicht in Ihrer Integration parsen.

### iOS

Der Apple Push Notification service (APNs) unterstützt die Konfiguration von Alert-Einstellungen und das Senden angepasster Daten mittels Schlüssel-Wert-Paaren. APNs verwendet die Apple-reservierte `aps`-Bibliothek, die vordefinierte Schlüssel und Werte enthält, welche Alert-Eigenschaften steuern.

#### APS-Bibliothek {#aps-library}

| Schlüssel         | Werttyp                     | Wertbeschreibung |
|-------------------|-----------------------------|----------------------------------|
| alert             | String oder Dictionary-Objekt | Bei String-Eingaben wird ein Alert mit dem String als Nachricht sowie den Buttons „Schließen“ und „Anzeigen“ dargestellt; bei Nicht-String-Eingaben wird je nach untergeordneten Eigenschaften ein Alert oder Banner angezeigt |
| badge             | Nummer                      | Steuert die Zahl, die als Badge auf dem App-Symbol angezeigt wird                                                                                                                              |
| sound             | String                      | Der Name der Audiodatei, die als Alert abgespielt wird; muss sich im App-Bundle oder im Ordner ```Library/Sounds``` befinden                                                                                    |
| content-available | Nummer                      | Eingabewerte von 1 signalisieren der App die Verfügbarkeit neuer Informationen beim Start oder bei Wiederaufnahme der Sitzung |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="APS-Bibliothek" }


##### Alert-Eigenschaften-Bibliothek {#alert-properties-library}

| Schlüssel      | Werttyp                  | Wertbeschreibung                                                                                                                             |
|----------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| title         | String                   | Ein kurzer String, den die Apple Watch kurzzeitig als Teil einer Benachrichtigung anzeigt                                                                    |
| body         | String                   | Der Inhalt der Push-Benachrichtigung                                                                                                                  |
| title-loc-key  | String oder null           | Ein Schlüssel, der den Titelstring für die aktuelle Lokalisierung aus der Datei ```Localizable.strings``` festlegt                                          |
| title-loc-args | String-Array oder null | String-Werte, die anstelle der Lokalisierungsformat-Spezifizierer im title-loc-key erscheinen können                                           |
| action-loc-key | String-Array oder null  | Falls vorhanden, legt der angegebene String die Lokalisierung für die Buttons „Schließen“ und „Anzeigen“ fest                                                         |
| loc-key        | String oder null           | Ein Schlüssel, der die Benachrichtigungsnachricht für die aktuelle Lokalisierung aus der Datei ```Localizable.strings``` festlegt                                  |
| loc-args       | String-Array         | String-Werte, die anstelle der Lokalisierungsformat-Spezifizierer im loc-key erscheinen können                                                       |
| launch-image   | Strings                  | Der Name einer Bilddatei im App-Bundle, die als Startbild verwendet werden soll, wenn Nutzer:innen den Aktions-Button antippen oder den Aktions-Slider bewegen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Alert-Eigenschaften-Bibliothek" }

Der Braze-Nachrichten-Editor übernimmt automatisch die Erstellung der folgenden Schlüssel: **alert** und **seine Eigenschaften**, **content-available**, **sound** und **category**.

Diese Werte können im Tab **Einstellungen** beim Erstellen einer Push-Nachricht eingegeben werden. Wählen Sie **Alert-Optionen** und wählen Sie einen Alert-Dictionary-Schlüssel, damit der Schlüssel automatisch in einem neuen Schlüssel-Wert-Eintrag ausgefüllt wird.

![Diese Werte können im Tab „Einstellungen“ beim Erstellen einer Push-Nachricht eingegeben werden. Wählen Sie „Alert-Optionen“ und wählen Sie einen Alert-Dictionary-Schlüssel, damit der Schlüssel automatisch in einem neuen Schlüssel-Wert-Eintrag ausgefüllt wird.]({% image_buster /assets/img_archive/keyvalue_automatickeys.png %})
{% raw %}
Wenn Braze eine Push-Benachrichtigung an APNs sendet, wird die Payload als JSON formatiert.

**Einfache Payload**

```
{
    "aps" : { "alert" : "Message received from Spencer" },
}
```

**Komplexe Payload**

```
{
    "aps" : {
        "alert" : {
            "body" : "Hi, welcome to our app!",
            "loc-key" : "France",
            "loc-args" : ["Bonjour", "bienvenue"],
            "action-loc-key" : "Button_Type_1",
            "launch-image" : "Paris"
      },
        "content-available" : 1
    },
}
```

{% endraw %}

##### Angepasste Schlüssel-Wert-Paare {#custom-key-value-pairs}

Zusätzlich zu den Payload-Werten der `aps`-Bibliothek können Sie angepasste Schlüssel-Wert-Paare an das Gerät einer Nutzer:in senden. Die Werte in diesen Paaren sind auf primitive Typen beschränkt: Dictionary (Objekt), Array, String, Nummer und Boolean.

![Screenshot zu angepassten Schlüssel-Wert-Paaren.]({% image_buster /assets/img_archive/keyvalue_enterpairs.png %})

Anwendungsfälle für angepasste Schlüssel-Wert-Paare umfassen unter anderem die interne Metrik-Erfassung und die Kontextsetzung für die Benutzeroberfläche. Braze ermöglicht es Ihnen, zusätzliche Schlüssel-Wert-Paare zusammen mit einer Push-Benachrichtigung zu senden, die über den [Extras-Schlüssel]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=swift#swift_settings) in Ihrer Anwendung genutzt werden können. Wenn Sie einen anderen Schlüssel bevorzugen, stellen Sie sicher, dass Ihre App diesen angepassten Schlüssel verarbeiten kann.

{% alert warning %}
Sie sollten es vermeiden, in Ihrer Anwendung einen Top-Level-Schlüssel oder ein Dictionary namens „ab“ zu verarbeiten.
{% endalert %}

Apple rät davon ab, Kundeninformationen oder sensible Daten als angepasste Payload-Daten einzuschließen. Darüber hinaus empfiehlt Apple, dass jede mit einer Alert-Nachricht verbundene Aktion keine Daten auf dem Gerät löschen sollte.

{% alert warning %}
Wenn Sie die HTTP/2-Provider-API verwenden, darf jede einzelne Payload, die Sie an APNs senden, eine Größe von 4096 Bytes nicht überschreiten. Die ältere binäre Schnittstelle, die bald eingestellt wird, unterstützt nur eine Payload-Größe von 2048 Bytes.
{% endalert %}

###### API-getriggerte Campaigns {#api-triggered-campaigns}

Braze ermöglicht es Ihnen, angepasste String-Schlüssel-Wert-Paare zu senden, die als `extras` bekannt sind. Um auf Ihre Extras in API-getriggerten und geplanten API-getriggerten Campaigns zuzugreifen, legen Sie im Dashboard einen Schlüssel als „example_key“ und einen Wert als {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %} fest. Dies ergibt eine Entwicklungskonsolen-Ausgabe von `"extras": { "test": { "foo": 1, "bar": 1 }`.

### Android

Braze ermöglicht es Ihnen, zusätzliche Daten-Payloads in Push-Benachrichtigungen mittels Schlüssel-Wert-Paaren zu senden.

#### Daten-Payload {#data-payload}

Ähnlich wie bei iOS-Push können Sie angepasste Schlüssel-Wert-Paare an das Gerät einer Nutzer:in senden.

Einige Anwendungsfälle für angepasste Schlüssel-Wert-Paare umfassen die interne Metrik-Erfassung und die Kontextsetzung für die Benutzeroberfläche, sie können jedoch für jeden beliebigen Zweck verwendet werden.

{% alert important %}
Das Backend Ihrer App muss in der Lage sein, angepasste Schlüssel-Wert-Paare zu verarbeiten, damit die Daten-Payload korrekt funktioniert.
{% endalert %}

##### API-getriggerte Campaigns

Braze ermöglicht es Ihnen, angepasste String-Schlüssel-Wert-Paare zu senden, die als `extras` bekannt sind. Um auf Ihre Extras in API-getriggerten und geplanten API-getriggerten Campaigns zuzugreifen, legen Sie im Dashboard einen Schlüssel als „example_key“ und einen Wert als {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %} fest. Dies ergibt eine Entwicklungskonsolen-Ausgabe von `"extras": { "test": { "foo": 1, "bar": 1 }`.

##### FCM-Messaging-Optionen {#fcm-messaging-options}

Android-Push-Benachrichtigungen können mit FCM-Nachrichtenoptionen weiter angepasst werden. Dazu gehören [Benachrichtigungspriorität]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_settings), [Sound]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_settings), Verzögerung, Lebensdauer und Zusammenfassbarkeit. Diese Werte können im Tab **Einstellungen** beim Erstellen einer Push-Nachricht angegeben werden. Weitere Anweisungen zur Konfiguration dieser Optionen im Braze-Nachrichten-Editor finden Sie unter [Erweiterte Push-Benachrichtigungseinstellungen]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_settings).

![Screenshot zu FCM-Messaging-Optionen.]({% image_buster /assets/img_archive/keyvalue_androidkeys.png %})

### Stille Push-Benachrichtigungen {#silent-push-notifications}

Eine stille Push-Benachrichtigung ist eine Push-Benachrichtigung ohne Alert-Nachricht oder Sound, die verwendet wird, um die Oberfläche oder den Inhalt Ihrer App im Hintergrund zu Update or aktualisieren or aktualisieren. Diese Benachrichtigungen nutzen Schlüssel-Wert-Paare, um diese Hintergrund-App-Aktionen auszulösen. Stille Push-Benachrichtigungen ermöglichen auch unser [Uninstall-Tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking).

Marketer sollten testen, ob stille Push-Benachrichtigungen das erwartete Verhalten auslösen, bevor sie diese an die Nutzer:innen ihrer App senden. Nachdem Sie Ihre stille Push-Benachrichtigung für [iOS]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=swift) oder [Android]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=android) erstellt haben, stellen Sie sicher, dass Sie nur eine Testnutzer:in ansprechen, indem Sie nach [externer Nutzer-ID]({{site.baseurl}}/api/endpoints/messaging#external-user-id) oder [E-Mail-Adresse]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) filtern.

Nach dem Start der Campaign sollten Sie überprüfen, ob Sie keine sichtbare Push-Benachrichtigung auf Ihrem Testgerät erhalten haben.

{% alert note %}
Das iOS-Gating für stille Benachrichtigungen kann folgende Symptome verursachen:

- Niedriger als erwartete Uninstall-Tracking-Metriken für iOS-Nutzer:innen
- Inkonsistente oder verzögerte Zustellung stiller Push-Benachrichtigungen
- [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories), die nicht angezeigt werden
- Push Stories, die ohne ihre erwarteten Bilder, Videos oder Seiten ankommen

Dies ist eine Einschränkung der Apple-Plattform und kein Braze-Problem. iOS kann Hintergrundbenachrichtigungen für einige Braze-Features verzögern oder verwerfen, einschließlich Uninstall-Tracking und Push Stories. Details dazu, was iOS einschränkt und wann, finden Sie unter [iOS-Einschränkungen]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=swift#ios-limitations).
{% endalert %}

## In-App Messages {#in-app-messages}

Sie können einem In-App-Nachricht ein Schlüssel-Wert-Paar hinzufügen, indem Sie im [traditionellen Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional) den Tab **Einstellungen** auswählen, dann **Neues Paar hinzufügen** wählen und anschließend Ihre Schlüssel-Wert-Paare angeben.

{% alert note %}
Schlüssel-Wert-Paare können nicht über den Drag-and-Drop-Editor für In-App Messages festgelegt werden.
{% endalert %}
![Screenshot zu In-App Messages.]({% image_buster /assets/img_archive/keyvalue_iam.png %})

### API-getriggerte Campaigns

Braze ermöglicht es Ihnen, benutzerdefinierte String-Schlüssel-Wert-Paare zu senden, die als `extras` bezeichnet werden. Um auf Ihre Extras in API-getriggerten und zeitplangesteuerten API-getriggerten Campaigns zuzugreifen, legen Sie im Dashboard einen Schlüssel als „example_key“ und einen Wert als {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %} fest. Dies führt zu einer Ausgabe in der Entwicklungskonsole von `"extras": { "test": { "foo": 1, "bar": 1 }`.

## E-Mails {#emails}

Sowohl SparkPost als auch SendGrid unterstützen Schlüssel-Wert-Paare in E-Mails. Wenn Sie SendGrid verwenden, werden Schlüssel-Wert-Paare als [Unique Arguments](https://docs.sendgrid.com/for-developers/sending-email/unique-arguments) gesendet. SendGrid erlaubt es Ihnen, eine unbegrenzte Anzahl von Schlüssel-Wert-Paaren mit bis zu 10.000 Bytes an Daten anzuhängen. Diese Schlüssel-Wert-Paare können in Posts des SendGrid [Event Webhook](https://sendgrid.com/docs/for-developers/tracking-events/event/) eingesehen werden.

{% alert note %}
Zurückgewiesene E-Mails liefern keine Schlüssel-Wert-Paare an SparkPost oder SendGrid.
{% endalert %}

![Tab „Sendeinformationen“ des E-Mail-Nachrichten-Editors in Braze.]({% image_buster /assets/img_archive/keyvalue_email.png %})

## Content Cards

Um ein Schlüssel-Wert-Paar zu einer Content Card hinzuzufügen, gehen Sie zum Tab **Settings** im Braze-Nachrichten-Editor und wählen Sie **Add New Pair**.

![Schlüssel-Wert-Paar zu Content Card hinzufügen]({% image_buster /assets/img_archive/kvp_content_cards.png %}){: style="max-width:70%;"}

{% alert note %}
Kontrollvarianten unterstützen keine Schlüssel-Wert-Paare. Wenn Sie Analytics für Kontrollgruppen in A/B-Tests erfassen müssen, erstellen Sie eine Nachrichtenvariante mit einem Schlüssel-Wert-Paar wie `control=true` und blenden Sie diese in Ihrem App-Code aus, während Sie Impressionen protokollieren.
{% endalert %}