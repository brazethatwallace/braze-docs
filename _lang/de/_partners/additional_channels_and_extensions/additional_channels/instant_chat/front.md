---
nav_title: Front
article_title: Front
description: "Erfahren Sie, wie Sie Front in Braze integrieren"
alias: /partners/front/
page_type: partner
search_tag: Partner

---

# Front

> Mit der Integration von Front können Sie die Braze-Datentransformation und Webhooks beider Plattformen nutzen, um eine bidirektionale SMS-Pipeline für Konversationen einzurichten.

Der eingehende Webhook von Front enthält eine Nutzlast mit der vom Live-Agenten gesendeten Nachricht. Die Anfrage muss neu formatiert werden, bevor sie von Braze-Endpunkten akzeptiert werden kann. Das Front-Datentransformations-Template formatiert die Nutzlast um und schreibt ein angepasstes Event mit dem Titel **Outbound SMS Sent** in das Kundenprofil, wobei der Nachrichtentext als Event-Eigenschaft übergeben wird.

Bevor Sie eine neue Transformation in Braze einrichten, empfehlen wir Ihnen, die Support-Matrix für jede Ebene in unserer Dokumentation zur [Datentransformation]({{site.baseurl}}/user_guide/data/unification/data_transformation) zu lesen. Unsere Free- und Pro-Tiers bieten eine unterschiedliche Anzahl aktiver Transformationen und eingehender Anfragen pro Monat. Vergewissern Sie sich, dass Ihr aktueller Plan Ihren Anwendungsfall unterstützen kann.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung | Beschreibung |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Ein Front-Konto | Um diese Partnerschaft zu nutzen, ist ein Front-Konto erforderlich. |
| Braze-Datentransformations-Webhook-URL | Die [Braze-Datentransformation]({{site.baseurl}}/user_guide/data/unification/data_transformation) wird verwendet, um den eingehenden Webhook von Front so umzuformatieren, dass er vom Braze-Endpunkt /users/track akzeptiert werden kann. |
| Ein Front-REST-API-Schlüssel | Ein Front-REST-API-Schlüssel wird verwendet, um eine ausgehende Webhook-Anfrage von Braze an Front zu stellen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

- Optimieren Sie Ihren Lead-Generierungsprozess mit automatisiertem SMS-Messaging von Braze, um Nutzerpräferenzen zu erkennen und Live-Vertriebsmitarbeitern die Möglichkeit zu geben, nachzufassen und Verkäufe abzuschließen.
- Binden Sie Kund:innen, die ihren Warenkorb verlassen haben, erneut ein, indem Sie Conversions durch automatisierte SMS-Antworten und Live-Chat-Support fördern.

## Front integrieren {#integrating-front}

### 1. Schritt: Datentransformation erstellen {#step-1-create-a-data-transformation}

Zunächst erstellen Sie eine neue Datentransformation in Braze. Die folgenden Schritte sind vereinfacht. Eine vollständige Anleitung finden Sie unter [Transformation erstellen]({{site.baseurl}}/user_guide/data/unification/data_transformation/creating_a_transformation).

1. Gehen Sie in Braze zu **Dateneinstellungen** > **Data Transformations** und wählen Sie dann **Create Transformation**.
2. Wählen Sie unter **Editing Experience** die Option **Start from scratch**.
3. Wählen Sie unter **Select Destination** die Option **POST: Track Users**.
4. Kopieren Sie das folgende Transformations-Template, fügen Sie es ein, speichern und aktivieren Sie den Endpunkt.
    {% raw %}
    ```liquid

    // This is a default template that you can use as a starting point. Feel free to delete this entirely to start from
    // scratch, or to delete specific components as you see fit

    // First, this code defines a variable, "brazecall", to build up a /users/track request
    // Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in
    // desired values in your /users/track request with JS dot notation, such as payload.x.y.z

    let brazecall = {
    "events": [
      {
      "phone": payload.recipients[1].handle,
      "_update_existing_only": true,
      "name": "Outbound SMS Sent",
      "time": new Date().toISOString(),
      "properties": {
        "message_id": payload.id,
        "message_body": payload.body,
        "front_author_username": payload.author.username
      }
      }
    ]
    };

    // After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
    return brazecall;
    ```
    {% endraw %}

    Ihre Transformation sollte dem JavaScript-Beispiel oben entsprechen; passen Sie Eigenschaftsnamen und Pfade an die Payload Ihres Front-Webhooks an.

{% alert tip %}
Sie können dieses Template an Ihre speziellen Bedürfnisse anpassen. Sie können zum Beispiel den voreingestellten Namen des angepassten Events ändern. Weitere Informationen finden Sie unter [Übersicht über Datentransformationen]({{site.baseurl}}/user_guide/data/unification/data_transformation).
{% endalert %}

### 2. Schritt: Ausgehende SMS-Campaign erstellen {#step-2-create-an-outbound-sms-campaign}

Als Nächstes erstellen Sie eine SMS-Campaign, die auf Webhooks von Front wartet und eine angepasste SMS-Antwort an Ihre Kund:innen sendet.

#### Schritt 2.1: Nachricht verfassen {#step-21-compose-your-message}

Fügen Sie in das Textfeld **Message** den folgenden Liquid-Code ein, zusammen mit einer Opt-out-Sprache oder anderen statischen Inhalten.

{% raw %}
```liquid
{{event_properties.${message_body}}}
```
{% endraw %}

Ihre Nachricht sollte in etwa so aussehen:

![Eine Beispielnachricht mit Liquid-Code.]({% image_buster /assets/img/front/sms_to_braze.png %}){: style="max-width:80%;"}

#### 2.2 Zustellung planen {#22-schedule-the-delivery} {#22-schedule-the-delivery}

Wählen Sie als Zustellungstyp **Aktionsbasierte Zustellung** und dann als angepassten Event-Trigger **Outbound SMS Sent**.

![Die Seite „Zustellung planen“.]({% image_buster /assets/img/front/custom_event_trigger.png %})

{% alert note %}
Bei diesem angepassten Event handelt es sich um die Datentransformation, die in das Profil der Nutzer:innen geschrieben wird. Nachrichten von Agenten werden als Event-Eigenschaft dieses Events gespeichert.
{% endalert %}

Aktivieren Sie abschließend unter **Zustellungssteuerung** die Wiederzulassung.

![Wiederzulassung aktiviert unter „Zustellungssteuerung“.]({% image_buster /assets/img/front/braze_reeligibility.png %})

### 3. Schritt: Angepassten Kanal erstellen {#step-3-create-a-custom-channel}

Gehen Sie im Front-Dashboard zu **Settings** > **Channels** > **Add Channels**, wählen Sie dann **Custom Channel** und geben Sie einen Namen für Ihren neuen Braze-Kanal ein.

![Ein angepasster Kanal für Braze im Front-Dashboard.]({% image_buster /assets/img/front/front_custom_channel.png %})

### 4. Schritt: Einstellungen konfigurieren {#step-4-configure-the-settings}

Geben Sie im Feld für den ausgehenden API-Endpunkt die Datentransformations-Webhook-URL ein, [die Sie zuvor erstellt haben](#step-1-set-up-a-data-transformation-in-braze). Alle ausgehenden Nachrichten von Live-Agenten auf Ihrem neuen Braze-Kanal werden hierher gesendet. Dieser Kanal stellt auch eine Endpunkt-URL bereit, an die Braze SMS-Nachrichten im Feld **Incoming URL** weiterleiten kann.

Notieren Sie sich diese URL&#8212;Sie werden sie später benötigen.

![Die Kanaleinstellungen für den neu erstellten Braze-Kanal in Front.]({% image_buster /assets/img/front/front_custom_channel2.png %}){: style="max-width:65%;"}

### 5. Schritt: Eingehende SMS-Weiterleitung einrichten {#step-5-set-up-inbound-sms-forwarding}

Als Nächstes erstellen Sie zwei neue Webhook-Campaigns in Braze, damit Sie eingehende SMS von Kund:innen an den Posteingang von Front weiterleiten können.

| Nummer | Zweck |
|---|---|
| Webhook-Campaign 1 | Signalisiert Front, dass ein Live-Chat-Gespräch angefragt wird. |
| Webhook-Campaign 2 | Leitet alle vom Kunden eingehenden SMS-Antworten an den Posteingang von Front weiter. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 5: Eingehende SMS-Weiterleitung einrichten" }

#### Schritt 5.1: SMS-Schlüsselwortkategorie erstellen {#step-51-create-an-sms-keyword-category}

Gehen Sie im Braze-Dashboard auf **Zielgruppe**, wählen Sie Ihre **SMS-Abo-Gruppe** und wählen Sie dann **Add Custom Keyword**. Um eine exklusive SMS-Schlüsselwortkategorie für Front zu erstellen, füllen Sie die folgenden Felder aus.

| Feld | Beschreibung |
|---|---|
| Keyword Category | Der Name Ihrer Schlüsselwortkategorie, z. B. `FrontSMS1`. |
| Keywords | Ihre angepassten Schlüsselwörter, z. B. `TIMETOMOW`. Vermeiden Sie gebräuchliche Wörter, um versehentliche Trigger zu vermeiden. Beachten Sie, dass bei Schlüsselwörtern die Groß- und Kleinschreibung keine Rolle spielt – `lawn` würde also auf `LAWN` passen. |
| Reply Message | Die Nachricht, die gesendet wird, wenn ein Schlüsselwort erkannt wird, z. B. „Ein Landschaftsgärtner wird sich in Kürze bei Ihnen melden.“ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 5.1: SMS-Schlüsselwortkategorie erstellen" }

![Ein Beispiel für eine SMS-Schlüsselwortkategorie in Braze.]({% image_buster /assets/img/front/front_keyword.png %}){: style="max-width:65%;"}

#### Schritt 5.2: Erste Webhook-Campaign erstellen {#step-52-create-your-first-webhook-campaign}

Erstellen Sie im Braze-Dashboard Ihre erste Webhook-Campaign mit der URL, [die Sie zuvor erstellt haben](#step-3-configure-the-settings-for-your-new-custom-braze-channel).

![Ein Beispiel für die erste Webhook-Campaign, die in Braze erstellt werden sollte.]({% image_buster /assets/img/front/sms_to_front.png %}){: style="max-width:65%;"}

Fügen Sie Ihrem Anfrage-Text Folgendes hinzu:

{% raw %}
```liquid
{
 "sender": {
  "handle": "{{${phone_number}}}",
  "name": "{{${user_id}}}"
 },
 "body_format": "markdown",
 "metadata": {
  "headers": {
   "first_name": "{{${first_name}}}",
   "last_name": "{{${last_name}}}"
  }
 },
 "body": "{{sms.${inbound_message_body} | default : "no body available" }}"
}
```
{% endraw %}

Konfigurieren Sie auf dem Tab „Einstellungen“ die Anfrage-Header `Authorization`, `content-type` und `accept`.

![Eine Beispielanfrage mit den drei erforderlichen Headern.]({% image_buster /assets/img/front/webhook_settings.png %}){: style="max-width:65%;"}

#### Schritt 5.3: Erste Zustellung planen {#step-53-schedule-the-first-delivery}

Wählen Sie für **Zustellung planen** die Option **Aktionsbasierte Zustellung** und dann als Trigger-Typ **Send an SMS Inbound Message**. Fügen Sie außerdem die SMS-Abo-Gruppe und die Schlüsselwortkategorie hinzu, die Sie [zuvor eingerichtet haben](#step-51-create-an-sms-keyword-category).

![Die Seite „Zustellung planen“ für die erste Webhook-Campaign.]({% image_buster /assets/img/front/front_actionbased_keyword.png %})

Aktivieren Sie unter **Zustellungssteuerung** die Wiederzulassung.

![Wiederzulassung ausgewählt unter „Zustellungssteuerung“ für die erste Webhook-Campaign.]({% image_buster /assets/img/front/braze_reeligibility.png %})

#### Schritt 5.4: Zweite Webhook-Campaign erstellen {#step-54-create-your-second-webhook-campaign}

Da Ihre zweite Webhook-Campaign mit der ersten übereinstimmt, können Sie [die erste duplizieren und umbenennen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns#duplicating-segments-or-campaigns).

#### Schritt 5.5: Zweite Zustellung planen {#step-55-schedule-the-second-delivery}

Legen Sie für **Zustellung planen** den **aktionsbasierten Trigger** und die **SMS-Abo-Gruppe** genauso fest wie bei [der ersten Zustellung](#step-53-schedule-the-first-delivery). Wählen Sie jedoch für die **Keyword Category** die Option **Other**.

![Die Seite „Zustellung planen“ für die zweite Webhook-Campaign, wobei als Schlüsselwortkategorie „Other“ gewählt wurde.]({% image_buster /assets/img/front/front_actionbased_other_keyword.png %})

#### Schritt 5.6: Zielgruppenfilter hinzufügen {#step-56-add-an-audience-filter}

Ihre Webhook-Campaign kann jetzt eingehende SMS-Antworten Ihrer Kund:innen weiterleiten. Um SMS-Antworten zu filtern, sodass nur Nachrichten für Live-Chats weitergeleitet werden, fügen Sie den Segmentierungsfilter **Last Received Message From Specific Campaign** zum Schritt **Zielgruppe** hinzu.

![Ein Zielgruppenfilter mit der Auswahl „Last Received Message From Specific Campaign“.]({% image_buster /assets/img/front/front_segment_last_received_message.png %}){: style="max-width:65%;"}

Konfigurieren Sie dann Ihren Filter:

1. Wählen Sie unter **Campaign** die SMS-Campaign aus, [die Sie zuvor erstellt haben](#step-2-create-an-outbound-sms-campaign).
2. Wählen Sie für **Operator** die Option **Less Than**.
3. Wählen Sie für **Time Window** die Zeitspanne, die ein Chat ohne Antwort der Kund:innen geöffnet bleiben soll.

![Die Konfigurationseinstellungen für den ausgewählten Zielgruppenfilter.]({% image_buster /assets/img/front/front_target_audience.png %})

## Überlegungen {#considerations}

### Abrechenbare Segmente {#billable-segments}

- SMS-Nachrichten werden bei Braze pro Nachrichtensegment berechnet. Wenn Sie verstehen, was ein Segment definiert und wie diese Nachrichten aufgeteilt werden, können Sie besser nachvollziehen, wie Ihnen Nachrichten in Rechnung gestellt werden. Weitere Informationen finden Sie in unserer [Dokumentation]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator).
- Lange Agentenantworten verbrauchen mehr abrechenbare Segmente.

### Datenpunkte protokollieren {#logging-data-points}

Derzeit erfordert diese Integration, dass jedes Mal ein angepasstes Event in ein Kundenprofil geschrieben wird, wenn ein Live-Agent eine SMS von Front sendet. Dies mag für einen schnellen Austausch mit nur wenigen Nachrichten geeignet sein – aber je länger die Konversationen werden, desto mehr Datenpunkte fallen an. Wenn Sie Fragen zu den Feinheiten der Braze-Datenpunkte haben, kann Ihr Braze Account Manager:in diese beantworten.

### Links in SMS-Nachrichten einfügen {#including-links-in-sms-messages}

Das Senden eines Links aus dem Front-Live-Chat wird mit zusätzlichen HTML-Tags dargestellt.

### Bilddatei von Front anhängen {#attaching-image-file-from-front}

Bilddateien in Front werden in SMS-Nachrichten, die von Braze gesendet werden, nicht dargestellt.

### Opt-outs

Bei Konversationsnachrichten besteht ein höheres Risiko, dass sie das Wort „Stopp“ oder ähnliche Formulierungen enthalten, die als unscharfe Opt-outs erkannt werden können.