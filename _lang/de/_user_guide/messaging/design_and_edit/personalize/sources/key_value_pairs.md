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

1. **Tracking-Parameter:** UTM-Parameter zu Analysezwecken anhängen
   - Schlüssel: `utm_campaign`
   - Wert: `spring_sale`
2. **Benutzerdefinierte Tags:** Tags für internes Routing oder Kategorisierung hinzufügen
   - Schlüssel: `priority`
   - Wert: `high`
3. **Verhaltens-Trigger:** Metadaten, die zum Auslösen oder Anpassen von In-App-Verhalten verwendet werden
   - Schlüssel: `deep_link`
   - Wert: `app://promo-page`

## Push-Benachrichtigungen {#push-notifications}

Schlüssel-Wert-Paare können zu Android-, iOS- und Web-Push-Benachrichtigungen hinzugefügt werden. Sie können Schlüssel-Wert-Paare verwenden, um interne Metriken und App-Inhalte zu aktualisieren oder Eigenschaften von Push-Benachrichtigungen anzupassen, wie z. B. Alert-Priorisierung, Lokalisierung und Töne.

Wählen Sie im Nachrichten-Editor den Tab **Einstellungen**, wählen Sie **Neues Paar hinzufügen** und geben Sie Ihre Schlüssel-Wert-Paare an.

Wenn Sie Schlüssel-Wert-Paare im Nachrichten-Editor hinzufügen, werden die Werte als Strings gesendet. Bei iOS-Push werden reservierte Apple Push Notification Service (APNs) Alert-Keys, die Sie über **Alert-Optionen** hinzufügen (wie z. B. `loc-args` für Lokalisierungsargumente), mit den korrekten JSON-Typen im Payload formatiert. Bei angepassten Keys empfängt Ihre App String-Werte, sofern Sie diese nicht in Ihrer Integration parsen.

### iOS

Der Apple Push Notification Service (APNs) unterstützt das Festlegen von Alert-Einstellungen und das Senden angepasster Daten mithilfe von Schlüssel-Wert-Paaren. APNs nutzt die Apple-reservierte `aps`-Bibliothek, die vordefinierte Keys und Werte enthält, die Alert-Eigenschaften steuern.

#### APS-Bibliothek {#aps-library}

| Key  | Werttyp  | Wertbeschreibung |
|-------------------|-----------------------------|----------------------------------|
| alert             | String oder Dictionary-Objekt | Bei String-Eingaben wird ein Alert mit dem String als Nachricht angezeigt, mit den Buttons „Schließen“ und „Anzeigen“; bei Nicht-String-Eingaben wird ein Alert oder Banner abhängig von den untergeordneten Eigenschaften der Eingabe angezeigt |
| badge             | Zahl                      | Steuert die Zahl, die als Badge auf dem App-Symbol angezeigt wird                                                                                                                              |
| sound             | String                      | Der Name der Sounddatei, die als Alert abgespielt wird; muss sich im App-Bundle oder im Ordner ```Library/Sounds``` befinden                                                                                    |
| content-available | Zahl                      | Eingabewerte von 1 signalisieren der App die Verfügbarkeit neuer Informationen beim Start oder bei der Wiederaufnahme einer Sitzung |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="APS-Bibliothek" }


##### Bibliothek der Alert-Eigenschaften {#alert-properties-library}

| Key            | Werttyp               | Wertbeschreibung                                                                                                                             |
|----------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| title         | String                   | Ein kurzer String, den die Apple Watch kurz als Teil einer Benachrichtigung anzeigt                                                                    |
| body         | String                   | Der Inhalt der Push-Benachrichtigung                                                                                                                  |
| title-loc-key  | String oder null           | Ein Key, der den Titel-String für die aktuelle Lokalisierung aus der ```Localizable.strings```-Datei festlegt                                          |
| title-loc-args | String-Array oder null | String-Werte, die anstelle der Titel-Lokalisierungsformat-Spezifizierer in title-loc-key erscheinen können                                           |
| action-loc-key | String-Array oder null  | Falls vorhanden, legt der angegebene String die Lokalisierung für die Buttons „Schließen“ und „Anzeigen“ fest                                                         |
| loc-key        | String oder null           | Ein Key, der die Benachrichtigungsnachricht für die aktuelle Lokalisierung aus der ```Localizable.strings```-Datei festlegt                                  |
| loc-args       | String-Array         | String-Werte, die anstelle der Lokalisierungsformat-Spezifizierer in loc-key erscheinen können                                                       |
| launch-image   | Strings                  | Der Name einer Bilddatei im App-Bundle, die als Startbild verwendet werden soll, wenn Nutzer:innen den Aktions-Button antippen oder den Aktions-Slider bewegen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Bibliothek der Alert-Eigenschaften" }

Der Braze Nachrichten-Editor erstellt automatisch die folgenden Keys: **alert** und **seine Eigenschaften**, **content-available**, **sound** und **category**.

Diese Werte können im Tab **Einstellungen** beim Erstellen einer Push-Nachricht eingegeben werden. Wählen Sie **Alert-Optionen** und wählen Sie einen Alert-Dictionary-Key aus, damit der Key automatisch in einem neuen Schlüssel-Wert-Eintrag vorausgefüllt wird.

![Diese Werte können im Tab „Einstellungen“ beim Erstellen einer Push-Nachricht eingegeben werden. Wählen Sie „Alert-Optionen“ und wählen Sie einen Alert-Dictionary-Key aus, damit der Key automatisch in einem neuen Schlüssel-Wert-Eintrag vorausgefüllt wird.]({% image_buster /assets/img_archive/keyvalue_automatickeys.png %})
{% raw %}
Wenn Braze eine Push-Benachrichtigung an APNs sendet, wird der Payload als JSON formatiert.

**Einfacher Payload**

```
{
    "aps" : { "alert" : "Message received from Spencer" },
}
```

**Komplexer Payload**

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

Zusätzlich zu den `aps`-Bibliothek-Payload-Werten können Sie angepasste Schlüssel-Wert-Paare an das Gerät von Nutzer:innen senden. Die Werte in diesen Paaren sind auf primitive Typen beschränkt: Dictionary (Objekt), Array, String, Zahl und Boolean.

![Screenshot zu angepassten Schlüssel-Wert-Paaren.]({% image_buster /assets/img_archive/keyvalue_enterpairs.png %})

Anwendungsfälle für angepasste Schlüssel-Wert-Paare umfassen unter anderem die Pflege interner Metriken und das Festlegen des Kontexts für die Benutzeroberfläche. Braze ermöglicht es Ihnen, zusätzliche Schlüssel-Wert-Paare zusammen mit einer Push-Benachrichtigung zu senden, die über Ihre Anwendung im [Extras-Key]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=swift#swift_settings) genutzt werden können. Wenn Sie einen anderen Key bevorzugen, stellen Sie sicher, dass Ihre App diesen angepassten Key verarbeiten kann.

{% alert warning %}
Sie sollten vermeiden, einen Top-Level-Key oder ein Dictionary namens „ab“ in Ihrer Anwendung zu verarbeiten.
{% endalert %}

Apple empfiehlt, keine Kund:inneninformationen oder sensiblen Daten als angepasste Payload-Daten aufzunehmen. Darüber hinaus empfiehlt Apple, dass keine mit einer Alert-Nachricht verbundene Aktion Daten auf einem Gerät löschen sollte.

{% alert warning %}
Wenn Sie die HTTP/2-Provider-API verwenden, darf ein einzelner Payload, den Sie an APNs senden, eine Größe von 4096 Bytes nicht überschreiten. Die veraltete binäre Schnittstelle, die bald eingestellt wird, unterstützt nur eine Payload-Größe von 2048 Bytes.
{% endalert %}

###### API-getriggerte Campaigns {#api-triggered-campaigns}

Braze ermöglicht es Ihnen, benutzerdefinierte String-Schlüssel-Wert-Paare zu senden, die als `extras` bekannt sind. Um auf Ihre Extras in API-getriggerten und geplanten API-getriggerten Campaigns zuzugreifen, legen Sie im Dashboard einen Key als „example_key“ und einen Wert als {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %} fest. Dies ergibt eine Entwicklungskonsolen-Ausgabe von `"extras": { "test": { "foo": 1, "bar": 1 }`.

### Android

Braze ermöglicht es Ihnen, zusätzliche Daten-Payloads in Push-Benachrichtigungen mithilfe von Schlüssel-Wert-Paaren zu senden.

#### Daten-Payload {#data-payload}

Ähnlich wie bei iOS-Push können Sie angepasste Schlüssel-Wert-Paare an das Gerät von Nutzer:innen senden.

Einige Anwendungsfälle für angepasste Schlüssel-Wert-Paare umfassen die Pflege interner Metriken und das Festlegen des Kontexts für die Benutzeroberfläche, können jedoch für jeden beliebigen Zweck verwendet werden.

{% alert important %}
Das Backend Ihrer App muss in der Lage sein, angepasste Schlüssel-Wert-Paare zu verarbeiten, damit der Daten-Payload ordnungsgemäß funktioniert.
{% endalert %}

##### API-getriggerte Campaigns

Braze ermöglicht es Ihnen, benutzerdefinierte String-Schlüssel-Wert-Paare zu senden, die als `extras` bekannt sind. Um auf Ihre Extras in API-getriggerten und geplanten API-getriggerten Campaigns zuzugreifen, legen Sie im Dashboard einen Key als „example_key“ und einen Wert als {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %} fest. Dies ergibt eine Entwicklungskonsolen-Ausgabe von `"extras": { "test": { "foo": 1, "bar": 1 }`.

##### FCM-Nachrichtenoptionen {#fcm-messaging-options}

Android-Push-Benachrichtigungen können mit FCM-Nachrichtenoptionen weiter angepasst werden. Dazu gehören [Benachrichtigungspriorität]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_settings), [Sound]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_settings), Verzögerung, Lebensdauer und Zusammenlegbarkeit. Diese Werte können im Tab **Einstellungen** beim Erstellen einer Push-Nachricht angegeben werden. Weitere Anweisungen zum Festlegen dieser Optionen im Braze Nachrichten-Editor finden Sie unter [Erweiterte Push-Benachrichtigungseinstellungen]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_settings).

![Screenshot zu FCM-Nachrichtenoptionen.]({% image_buster /assets/img_archive/keyvalue_androidkeys.png %})

### Stille Push-Benachrichtigungen {#silent-push-notifications}

Eine stille Push-Benachrichtigung ist eine Push-Benachrichtigung ohne Alert-Nachricht oder Sound, die dazu dient, die Benutzeroberfläche oder den Inhalt Ihrer App im Hintergrund zu aktualisieren. Diese Benachrichtigungen nutzen Schlüssel-Wert-Paare, um diese Hintergrund-App-Aktionen auszulösen. Stille Push-Benachrichtigungen unterstützen auch unser [Uninstall-Tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking).

Marketer sollten testen, ob stille Push-Benachrichtigungen das erwartete Verhalten auslösen, bevor sie diese an die Nutzer:innen ihrer App senden. Nachdem Sie Ihre stille Push-Benachrichtigung für [iOS]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=swift) oder [Android]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=android) erstellt haben, stellen Sie sicher, dass Sie nur Testnutzer:innen ansprechen, indem Sie nach [externer Nutzer-ID]({{site.baseurl}}/api/endpoints/messaging#external-user-id) oder [E-Mail-Adresse]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) filtern.

Nach dem Campaign-Start sollten Sie prüfen, ob Sie keine sichtbare Push-Benachrichtigung auf Ihrem Testgerät erhalten haben.

{% alert note %}
Die iOS-Drosselung stiller Benachrichtigungen kann folgende Symptome verursachen:

- Niedrigere Uninstall-Tracking-Metriken als erwartet für iOS-Nutzer:innen
- Inkonsistente oder verzögerte Zustellung stiller Push-Benachrichtigungen
- [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories), die nicht angezeigt werden
- Push Stories, die ohne die erwarteten Bilder, Videos oder Seiten eintreffen

Dies ist eine Einschränkung der Apple-Plattform und kein Braze-Problem. iOS kann Hintergrundbenachrichtigungen für einige Braze-Features verzögern oder verwerfen, einschließlich Uninstall-Tracking und Push Stories. Weitere Informationen dazu, was iOS drosselt und wann, finden Sie unter [iOS-Einschränkungen]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=swift#ios-limitations).
{% endalert %}

## In-App-Nachrichten {#in-app-messages}

Fügen Sie Schlüssel-Wert-Paare zu In-App-Nachrichten hinzu, die Sie mit dem [traditionellen Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional) erstellen.

1. Erstellen oder bearbeiten Sie in Ihrer Campaign oder Ihrem Canvas eine In-App-Nachricht und wählen Sie den traditionellen Editor aus (nicht Drag-and-Drop).
2. Wählen Sie im Nachrichten-Editor den Tab **Settings** aus.
3. Wählen Sie unter **Key value pairs** die Option **Add new pair** aus.
4. Geben Sie für jedes Paar einen Schlüssel und einen Wert ein. Um ein weiteres Paar hinzuzufügen, wählen Sie erneut **Add new pair** aus.

{% alert note %}
Schlüssel-Wert-Paare sind im Drag-and-Drop-Editor für In-App-Nachrichten nicht verfügbar. Verwenden Sie den traditionellen Editor, um sie hinzuzufügen.
{% endalert %}

### API-getriggerte Campaigns

Braze ermöglicht es Ihnen, benutzerdefinierte String-Schlüssel-Wert-Paare zu senden, die als `extras` bezeichnet werden. Um auf Ihre Extras in API-getriggerten und geplanten API-getriggerten Campaigns zuzugreifen, legen Sie im Dashboard einen Schlüssel als „example_key“ und einen Wert als {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %} fest. Dies führt zu einer Ausgabe in der Entwicklungskonsole von `"extras": { "test": { "foo": 1, "bar": 1 }`.

## E-Mails {#emails}

Sowohl SparkPost als auch SendGrid unterstützen Schlüssel-Wert-Paare in E-Mails. Wenn Sie SendGrid verwenden, werden Schlüssel-Wert-Paare als [Unique Arguments](https://docs.sendgrid.com/for-developers/sending-email/unique-arguments) gesendet. SendGrid erlaubt es Ihnen, eine unbegrenzte Anzahl von Schlüssel-Wert-Paaren mit bis zu 10.000 Bytes an Daten anzuhängen. Diese Schlüssel-Wert-Paare können in Posts vom SendGrid [Event Webhook](https://sendgrid.com/docs/for-developers/tracking-events/event/) eingesehen werden.

{% alert note %}
Gebouncte E-Mails übermitteln keine Schlüssel-Wert-Paare an SparkPost oder SendGrid.
{% endalert %}

![Tab „Sendeinformationen“ des E-Mail-Nachrichten-Editors in Braze.]({% image_buster /assets/img_archive/keyvalue_email.png %})

## Content Cards

Um ein Schlüssel-Wert-Paar zu einer Content Card hinzuzufügen, gehen Sie zum Tab **Settings** im Braze-Nachrichten-Editor und wählen Sie **Add New Pair**.

![Schlüssel-Wert-Paar zu Content Card hinzufügen]({% image_buster /assets/img_archive/kvp_content_cards.png %}){: style="max-width:70%;"}

{% alert note %}
Kontrollvarianten unterstützen keine Schlüssel-Wert-Paare. Wenn Sie Analytics für Kontrollgruppen in A/B-Tests erfassen müssen, erstellen Sie eine Nachrichtenvariante mit einem Schlüssel-Wert-Paar wie `control=true` und blenden Sie diese in Ihrem App-Code aus, während Sie Impressionen protokollieren.
{% endalert %}