---
nav_title: Messenger
article_title: Facebook Messenger
alias: /partners/messenger/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Facebook Messenger, einer der weltweit beliebtesten Instant-Messaging-Plattformen."
page_type: partner
search_tag: Partner

---

# Facebook Messenger

> [Facebook Messenger](https://developers.facebook.com/docs/messenger-platform/) ist eine der beliebtesten Instant-Messaging-Plattformen der Welt, die von fast einer Milliarde monatlich aktiver Nutzer:innen genutzt wird. Über diese Plattform können Marken ansprechende Chatbots erstellen, die intelligent und automatisch mit ihren Kund:innen interagieren.

Die Braze- und Facebook-Integration nutzt Braze-Webhooks, Segmentierung, Personalisierung und Triggering-Features, um Ihren Nutzer:innen im Facebook Messenger über die Messenger Platform API Nachrichten zu senden. Ein angepasstes Facebook Messenger Webhook-Template ist in unserer Plattform unter **Content** > **Webhook** enthalten.

Die Facebook Messenger-Plattform ist für „nicht werbliche Nachrichten gedacht, die eine bereits bestehende Transaktion erleichtern, andere Aktionen zur Kundenbetreuung anbieten oder von einer Person angefragte Inhalte liefern.“ Weitere Informationen finden Sie in den [Richtlinien der Facebook-Plattform](https://developers.facebook.com/docs/messenger-platform) und in den [Beispielen für akzeptable Anwendungsfälle](https://developers.facebook.com/docs/messenger-platform/app-review#examples_acceptable).

## Voraussetzungen {#prerequisites}

Bestätigen Sie die folgenden Punkte, bevor Sie mit der Integration fortfahren:

- Facebook lässt die Nutzung der Messenger-Plattform zum Versenden von Marketing-Nachrichten nicht zu.
- Sie benötigen die ausdrückliche Zustimmung der Nutzer:innen für Nachrichten von Ihrer Seite.
- Um Nachrichten an Nutzer:innen zu senden, die keine Testnutzer:innen Ihrer Facebook App sind, muss Ihre App die [App-Prüfung](https://developers.facebook.com/docs/messenger-platform/app-review) von Facebook bestehen.<br><br>

| Anforderung | Herkunft | Zugang | Beschreibung |
| --- | --- | --- | --- |
| Facebook Messenger-Seite | Facebook | [https://www.facebook.com/pages/create](https://www.facebook.com/pages/create) | Eine Facebook-Seite wird als Identität für Ihren Bot verwendet. Wenn Nutzer:innen mit Ihrer App chatten, sehen sie den Seitennamen und das Profilbild. |
| Facebook Messenger App | Facebook | [https://developers.facebook.com/apps](https://developers.facebook.com/apps) | Die Facebook App enthält die Einstellungen für Ihren Messenger-Bot, einschließlich der Zugriffstoken. |
| App-Bot-Überprüfung und -Genehmigung | Facebook | [https://developers.facebook.com/docs/messenger-platform/app-review](https://developers.facebook.com/docs/messenger-platform/app-review) | Wenn Sie bereit sind, Ihren Bot für die Öffentlichkeit freizugeben, müssen Sie ihn bei Facebook zur Überprüfung und Genehmigung einreichen. Mit diesem Überprüfungsprozess stellen wir sicher, dass Ihr Messenger-Bot unsere Richtlinien einhält und wie erwartet funktioniert, bevor er für alle Nutzer:innen im Messenger verfügbar gemacht wird. |
| Seitenbereichs-IDs (PSIDs) | Facebook | [https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages) | Sie benötigen die PSIDs der Nutzer:innen, um Nachrichten im Facebook Messenger zu versenden. Wenn Nutzer:innen über Messenger mit Ihrer App interagieren, erstellt Facebook eine PSID. Diese PSID kann als angepasstes Attribut in Form eines Strings an Braze gesendet werden. |
| Token für den Seitenzugriff | Facebook | [https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token](https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token) | Diese Token ähneln den Nutzerzugriffstoken, mit dem Unterschied, dass sie APIs die Erlaubnis erteilen, die Daten einer Facebook-Seite zu lesen, zu schreiben oder zu ändern. Um ein Token für den Seitenzugriff zu erhalten, müssen Sie ein Nutzerzugriffstoken anfordern und die Berechtigung `manage_pages` anfragen. Nachdem Sie das Nutzerzugriffstoken haben, erhalten Sie das Seitenzugriffstoken über die Graph API. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Voraussetzungen" }

## Integration

Im Folgenden wird gezeigt, wie Sie einen Braze Facebook Messenger Webhook einrichten.
Wenn Sie zusätzliche Hilfe bei der Einrichtung Ihres Bots benötigen, finden Sie im [GitHub-Repository von Braze](https://github.com/Appboy/appboy-fb-messenger-bot) ein vollständiges Tutorial zum Messenger-Bot und Beispielcode!

### Schritt 1: Sammeln Sie Ihre PSIDs {#step-1-collect-your-psids}

Um Nachrichten im Facebook Messenger zu versenden, müssen Sie die seitenbezogenen IDs (PSIDs) Ihrer Nutzer:innen erfassen, um sie zu identifizieren und einheitlich mit ihnen zu interagieren. PSIDs sind nicht dasselbe wie die Facebook-ID der Nutzer:innen. Facebook erstellt diesen Bezeichner jedes Mal, wenn Sie einer Kund:in eine Nachricht senden oder wenn eine Kund:in Ihnen eine Nachricht sendet.

PSIDs können über einen der verschiedenen [Eingänge](https://developers.facebook.com/docs/messenger-platform/discovery), die Facebook bietet, gefunden werden. Nachdem Nutzer:innen eine Nachricht an Ihre App geschickt oder eine Aktion in einer Konversation durchgeführt haben, wie z. B. das Antippen eines Buttons oder das Senden einer Nachricht, wird ihre PSID in die Eigenschaft `sender.id` des Webhook-Ereignisses aufgenommen, sodass Ihr Bot erkennen kann, wer die Aktion durchgeführt hat.

```
{
  "sender":{
    "id":"<PSID>"
  },
  "recipient":{
    "id":"<PAGE_ID>"
  },
  "timestamp":1458692752478,
  "message":{
    "mid":"mid.1457764197618:41d102a3e1ae206a38",
    "text":"hello, world!",
    "quick_reply": {
      "payload": "<DEVELOPER_DEFINED_PAYLOAD>"
    }
  }
}
```

Wann immer Sie eine Nachricht senden, wird die PSID in die Eigenschaft `recipient.id` der Anfrage aufgenommen, um zu identifizieren, wer die Nachricht erhalten soll.

### Schritt 2: An Braze als angepasstes Attribut senden {#step-2-send-to-braze-as-a-custom-attribute}

Sobald Sie sicher sind, dass Sie PSIDs erhalten, koordinieren Sie dies mit Ihren Entwickler:innen, um die PSIDs als [angepasstes Attribut]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes#custom-attributes) an Braze zu senden. PSIDs sind Strings, auf die durch einen [API-Aufruf](https://developers.facebook.com/documentation/business-messaging/messenger-platform/send-messages) zugegriffen werden kann.

### Schritt 3: Richten Sie Ihr Webhook-Template ein {#step-3-set-up-your-webhook-template}

So erstellen Sie ein Facebook Messenger Webhook-Template:

1. Gehen Sie zu **Content** > **Webhook** und wählen Sie **Create webhook template**.
2. Wählen Sie **Templates** > **Braze templates**.
3. Suchen und wählen Sie das Template „Facebook Messenger“.
4. Wählen Sie **Select template**.

1. Geben Sie einen Template-Namen an und fügen Sie Teams und Tags hinzu, falls erforderlich.
2. Geben Sie Ihre Nachricht ein oder wählen Sie ein Nachrichten-Template aus den [von Facebook zur Verfügung gestellten](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages). Sie können auch die [Art](https://developers.facebook.com/docs/messenger-platform/send-messages#message_types) Ihrer Nachricht oder Ihren [Tag](https://developers.facebook.com/docs/messenger-platform/send-messages/message-tags) auswählen.
3. Fügen Sie die PSID als angepasstes Attribut ein. Verwenden Sie dazu den blau-weißen Button **+** in der Ecke des Feldes **Request Body**.
3. Fügen Sie Ihr Token für den Seitenzugriff in die Webhook-URL ein, indem Sie `FACEBOOK_PAGE_ACCESS_TOKEN` durch Ihr Token ersetzen.

#### Vorschau und Test Ihres Webhooks {#previewing-and-testing-your-webhook}

Bevor Sie Ihre Nachricht versenden, testen Sie Ihren Webhook. Vergewissern Sie sich, dass Ihre Messenger-ID in Braze gespeichert ist (oder suchen Sie sie und testen Sie als angepasste:r Nutzer:in), und verwenden Sie die Vorschau, um die Testnachricht zu versenden:

![Tab „Test“ im Facebook Messenger Webhook-Template, der zeigt, wie Sie eine Vorschau der Nachricht anzeigen können, indem Sie sie an eine:n bestehende:n Nutzer:in senden.]({% image_buster /assets/img_archive/fbm-test.png %})

Wenn Sie die Nachricht erfolgreich empfangen haben, können Sie die Einstellungen für die Zustellung konfigurieren.

## Verwendung dieser Integration {#using-this-integration}

Sobald Sie diese Integration eingerichtet haben, können Sie sie nutzen, um Nutzer:innen des Facebook Messenger gezielt anzusprechen. Wenn Sie Nachrichten nicht über die Telefonnummern der Nutzer:innen versenden und planen, Messenger-Nachrichten wiederholt zu versenden, sollten Sie für alle Nutzer:innen, für die die Messenger-ID als angepasstes Attribut existiert, [ein Segment erstellen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#creating-a-segment) und das [Analytics-Tracking]({{site.baseurl}}/user_guide/audience/segments/segment_data) aktivieren, um Ihre Messenger-Abo-Raten im Laufe der Zeit zu verfolgen.

![Segment-Filter „messenger_id“ auf „ist nicht leer“ gesetzt.]({% image_buster /assets/img_archive/fbm-segmentation.png %})

Wenn Sie sich dafür entscheiden, kein spezielles Segment für Messenger-Abonnent:innen zu erstellen, stellen Sie sicher, dass Sie einen Filter für die vorhandene Messenger-ID einfügen, um Fehler zu vermeiden.

Sie können auch andere Segmentierungen für das Targeting Ihrer Messenger-Campaigns verwenden, und der Rest des Erstellungsprozesses funktioniert wie bei jeder anderen Campaign.