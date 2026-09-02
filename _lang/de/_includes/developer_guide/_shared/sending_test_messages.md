# Testnachrichten senden {#sending-test-messages}

> Bevor Sie eine Messaging-Kampagne an Ihre Nutzer:innen senden, empfehlen wir, diese zu testen, um sicherzustellen, dass sie richtig aussieht und wie gewünscht funktioniert. Sie können das Dashboard verwenden, um Testnachrichten mit Push-Benachrichtigungen, In-App-Nachrichten (IAM) oder E-Mails zu erstellen und zu versenden.

## Testnachricht senden {#sending-a-test-message}

### 1. Schritt: Ein bestimmtes Testsegment erstellen <a class="margin-fix" name="test-segment"></a> {#step-1-create-a-designated-test-segment}

Nachdem Sie ein Testsegment eingerichtet haben, können Sie es verwenden, um jeden Ihrer Braze-Messaging-Kanäle zu testen. Bei richtiger Einrichtung muss dies nur ein einziges Mal geschehen.

Um ein Testsegment einzurichten, gehen Sie zu **Segments** und erstellen Sie ein neues Segment. Wählen Sie **Add Filter** und wählen Sie dann einen der Testfilter aus.

![Eine Braze-Testkampagne, die die im Targeting-Schritt verfügbaren Filter anzeigt.]({% image_buster /assets/img_archive/testmessages1.png %})

Mit Testfiltern können Sie sicherstellen, dass nur Nutzer:innen mit einer bestimmten E-Mail-Adresse oder [externen Nutzer-ID]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#setting-user-ids) die Testnachricht erhalten.

![Ein Dropdown-Menü mit mehreren Filtern, die unter der Überschrift „Testing“ aufgelistet sind]({% image_buster /assets/img_archive/testmessages2.png %})

Sowohl die Filter für E-Mail-Adressen als auch für externe Nutzer-IDs bieten die folgenden Optionen:

| Operator          | Beschreibung |
|------------------|--------------------------------------------------------------------------------------------------------------------------------|
| `equals`      | Es wird nach einer genauen Übereinstimmung mit der von Ihnen angegebenen E-Mail oder Nutzer-ID gesucht. Verwenden Sie diese Option, wenn Sie die Testkampagnen nur an Geräte senden möchten, die mit einer einzigen E-Mail oder Nutzer-ID verknüpft sind. |
| `does not equal` | Verwenden Sie diese Option, wenn Sie eine bestimmte E-Mail oder Nutzer-ID von Testkampagnen ausschließen möchten. |
| `matches`     | So finden Sie Nutzer:innen, deren E-Mail-Adressen oder Nutzer-IDs mit einem Teil des von Ihnen angegebenen Suchbegriffs übereinstimmen. Damit können Sie nur die Nutzer:innen finden, die eine `@yourcompany.com`-Adresse haben, sodass Sie Nachrichten an alle Mitglieder Ihres Teams senden können. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 1: Create a designated test segment a class="margin-fix" name="test-segment"/a" }

Sie können mehrere bestimmte E-Mails auswählen, indem Sie die Option „`matches`“ verwenden und die E-Mail-Adressen mit einem &#124;-Zeichen trennen. Zum Beispiel: „`matches`“ „`email1@braze.com` &#124; `email2@braze.com`“. Sie können auch mehrere Operatoren miteinander kombinieren. Das Testsegment könnte zum Beispiel einen Filter für E-Mail-Adressen enthalten, der „`matches`“ „`@braze.com`“ und einen anderen Filter, der „`does not equal`“ „`sales@braze.com`“.

Nachdem Sie die Testfilter zu Ihrem Testsegment hinzugefügt haben, können Sie überprüfen, ob sie funktionieren, indem Sie **Preview** auswählen oder indem Sie **Settings** > **CSV Export All User Data** wählen, um die Nutzerdaten dieses Segments in eine CSV-Datei zu exportieren.

![Ein Abschnitt einer Braze-Kampagne mit dem Titel „Segment Details“]({% image_buster /assets/img_archive/testmessages3.png %})

{% alert note %}
Der Export der Nutzerdaten des Segments in eine CSV-Datei ist die genaueste Überprüfungsmethode, da die Vorschau nur eine Stichprobe Ihrer Nutzer:innen zeigt und möglicherweise nicht alle Nutzer:innen umfasst.
{% endalert %}

### 2. Schritt: Nachricht senden {#step-2-send-the-message}

Sie können eine Nachricht über das Braze-Dashboard oder die Befehlszeile senden.

{% tabs local %}
{% tab Using the dashboard %}
{% subtabs %}
{% subtab push or in-app message %}
Um Push-Benachrichtigungen oder In-App-Nachrichten zum Test zu versenden, müssen Sie Ihr zuvor erstelltes Testsegment adressieren. Beginnen Sie mit der Erstellung Ihrer Campaign und folgen Sie den üblichen Schritten. Wenn Sie den Schritt **Target Audiences** erreichen, wählen Sie Ihr Testsegment aus dem Dropdown-Menü aus.

![Eine Braze-Testkampagne, die die im Targeting-Schritt verfügbaren Segmente anzeigt.]({% image_buster /assets/img_archive/test_segment.png %})

Bestätigen Sie Ihre Campaign und starten Sie sie, um Ihre Push-Benachrichtigungen und In-App-Nachrichten zu testen.

{% alert note %}
Stellen Sie sicher, dass Sie im Abschnitt **Schedule** des Campaign-Composers die Option **Allow users to become re-eligible to receive campaign** auswählen, wenn Sie eine einzelne Campaign verwenden möchten, um sich selbst mehr als einmal eine Testnachricht zu senden.
{% endalert %}
{% endsubtab %}

{% subtab email message %}
Wenn Sie ausschließlich E-Mail-Nachrichten testen, müssen Sie nicht unbedingt ein Testsegment einrichten. Im ersten Schritt des Campaign-Composers, in dem Sie die E-Mail-Nachricht Ihrer Campaign verfassen, klicken Sie auf **Send Test** und geben die E-Mail-Adresse ein, an die Sie eine Test-E-Mail senden möchten.

![Eine Braze-Campaign mit ausgewähltem Tab „Send Test“]({% image_buster /assets/img_archive/testmessages45.png %})

{% alert tip %}
Sie können auch aktivieren oder deaktivieren, dass [TEST (oder SEED)]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#append-email-subject-lines) an Ihre Testnachrichten angehängt wird.
{% endalert %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Using the command line %}
Alternativ können Sie eine einzelne Benachrichtigung mit cURL und der [Braze Messaging API]({{site.baseurl}}/api/endpoints/messaging/) senden. Beachten Sie, dass diese Beispiele eine Anfrage über die Instanz `US-01` stellen. Um Ihre herauszufinden, lesen Sie den Abschnitt [API-Endpunkte]({{site.baseurl}}/api/basics/#endpoints).

{% subtabs local %}
{% subtab android %}
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "CUSTOM_KEY":"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}

{% subtab swift %}
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert": "Test push",
      "extra": {
        "CUSTOM_KEY" :"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}

{% subtab kindle %}
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "kindle_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "CUSTOM_KEY":"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}
{% endsubtabs %}

Ersetzen Sie Folgendes:

| Platzhalter         | Beschreibung                                               |
|---------------------|-----------------------------------------------------------|
| `BRAZE_API_KEY`      | Ihr Braze-API-Schlüssel, der für die Authentifizierung verwendet wird. Gehen Sie in Braze zu **Settings** > **API Keys**, um Ihren Schlüssel zu finden. |
| `EXTERNAL_USER_ID` | Die externe Nutzer-ID, mit der Sie Ihre Nachricht an eine:n bestimmte:n Nutzer:in senden. Gehen Sie in Braze zu **Audience** > **Search Users** und suchen Sie dann nach einer/einem Nutzer:in. |
| `CUSTOM_KEY`         | (Optional) Ein angepasster Schlüssel für zusätzliche Daten.              |
| `CUSTOM_VALUE`       | (Optional) Ein angepasster Wert, der Ihrem angepassten Schlüssel zugewiesen ist.    |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2: Send the message" }
{% endtab %}
{% endtabs %}

## Einschränkungen beim Testen {#test-limitations}

Es gibt einige Situationen, in denen Testnachrichten nicht die gleichen Funktionen aufweisen wie der Start einer Campaign oder eines Canvas für eine echte Gruppe von Nutzer:innen. In diesen Fällen sollten Sie die Campaign oder das Canvas für eine begrenzte Anzahl von Testnutzer:innen starten, um dieses Verhalten zu überprüfen.

- Wenn Sie das Braze-[Präferenzzentrum]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) über **Testnachrichten** aufrufen, ist der Button „Senden“ ausgegraut.
- Der list-unsubscribe-Header ist in E-Mails, die über die Testnachrichten-Funktionalität gesendet werden, nicht enthalten.
- Für In-App-Nachrichten und Content Cards muss die/der Zielnutzer:in über ein Push-Token / Textbaustein für das Zielgerät verfügen.