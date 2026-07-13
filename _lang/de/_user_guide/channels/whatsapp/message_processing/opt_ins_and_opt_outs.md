---
nav_title: "Opt-ins und Opt-outs"
article_title: "Opt-ins und Opt-outs"
description: "Dieser Referenzartikel behandelt verschiedene WhatsApp-Opt-in- und Opt-out-Methoden."
page_type: partner
search_tag: Partner
page_order: 5
channel:
  - WhatsApp
---

# Opt-in und Opt-out {#opt-in-and-opt-out}

> Die Handhabung von WhatsApp-Opt-ins und -Opt-outs ist entscheidend, da WhatsApp Ihre [Qualitätsbewertung der Telefonnummer](https://www.facebook.com/business/help/896873687365001) überwacht und niedrige Bewertungen dazu führen können, dass Ihre Nachrichtenlimits reduziert werden. <br><br>Eine Möglichkeit, eine hohe Qualitätsbewertung aufzubauen, besteht darin, zu verhindern, dass Nutzer:innen Ihr Unternehmen blockieren oder melden. Dies kann erreicht werden, indem Sie [qualitativ hochwertige Nachrichten](https://developers.facebook.com/docs/whatsapp/messaging-limits#quality-rating-and-messaging-limits) bereitstellen (z. B. Mehrwert für Ihre Nutzer:innen), die Nachrichtenhäufigkeit kontrollieren und Kund:innen die Möglichkeit geben, den Empfang zukünftiger Kommunikation abzulehnen. <br><br>Diese Seite beschreibt, wie Sie Opt-ins und Opt-outs einrichten und welche Unterschiede zwischen den Modifikatoren „Regex“ und „is“ bestehen.

Opt-ins können aus externen Quellen oder über Braze-Methoden wie SMS oder In-App- und In-Browser-Nachrichten stammen. Opt-outs können über in Braze festgelegte Schlüsselwörter und WhatsApp-Marketing-Buttons verarbeitet werden. Nutzen Sie die folgenden Methoden als Leitfaden für die Einrichtung von Opt-ins und Opt-outs.

## Opt-in-Methoden {#opt-in-methods}
- [Externe Opt-in-Methoden außerhalb von Braze](#external-to-braze-opt-in-methods)
  - [Extern erstellte Opt-in-Liste](#externally-built-opt-in-list)
  - [Ausgehende Nachricht im Kundensupport-WhatsApp-Kanal](#outbound-message-in-customer-support-whatsapp-channel)
  - [Eingehende WhatsApp-Nachricht](#inbound-whatsapp-message)
- [Braze-gestützte Opt-in-Methoden](#braze-powered-opt-in-methods)

### Opt-out-Methoden {#opt-out-methods}
- [Allgemeine Opt-out-Schlüsselwörter](#general-opt-out-keywords)
- [Marketing-Opt-out-Auswahl](#marketing-opt-out-selection)

## Opt-ins für Ihren Braze-WhatsApp-Kanal einrichten {#set-up-opt-ins-for-your-braze-whatsapp-channel}

Für WhatsApp-Opt-ins müssen Sie die [Anforderungen von WhatsApp](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) einhalten. Außerdem müssen Sie Braze die folgenden Informationen bereitstellen:
- Eine `external_id`, eine [Telefonnummer]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers) und einen aktualisierten Abo-Status für jede:n Nutzer:in. Dies kann über das [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/) oder den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) erfolgen, um die Telefonnummer und den Abo-Status zu aktualisieren.

{% alert note %}
Braze hat eine Verbesserung des `/users/track`-Endpunkts veröffentlicht, die Aktualisierungen des Abo-Status ermöglicht. Mehr dazu erfahren Sie unter [Abo-Gruppen]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status). Wenn Sie jedoch bereits Opt-in-Protokolle über den [`/v2/subscription/status/set`-Endpunkt]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2) erstellt haben, können Sie diese weiterhin dort verwenden.
{% endalert %}

### Externe Opt-in-Methoden außerhalb von Braze {#external-to-braze-opt-in-methods}

Ihre App oder Website (Kontoregistrierung, Checkout-Seite, Kontoeinstellungen, Kreditkartenterminal) an Braze.

Überall dort, wo Sie bereits eine Marketingeinwilligung für E-Mail oder SMS haben, fügen Sie einen zusätzlichen Abschnitt für WhatsApp hinzu. Nachdem sich ein:e Nutzer:in angemeldet hat, benötigt er/sie eine `external_id`, eine [Telefonnummer]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers) und einen aktualisierten Abo-Status. Nutzen Sie dazu, je nach Ihrer Braze-Installation, entweder den [`/subscription/status/set`-Endpunkt]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) oder das [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/).

#### Extern erstellte Opt-in-Liste {#externally-built-opt-in-list}

Wenn Sie WhatsApp bereits zuvor verwendet haben, haben Sie möglicherweise schon eine Nutzerliste mit Opt-ins gemäß den WhatsApp-Anforderungen erstellt. Laden Sie in diesem Fall eine CSV-Datei hoch oder verwenden Sie die API mit den [folgenden Informationen]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#csv) in Braze.

#### Ausgehende Nachricht im Kundensupport-WhatsApp-Kanal {#outbound-message-in-customer-support-whatsapp-channel}

Senden Sie in Ihrem Kundensupport-Kanal nach gelösten Anfragen eine automatische Nachricht, in der gefragt wird, ob die Kund:innen Marketing-Nachrichten erhalten möchten. Die Funktionalität hängt hier von den verfügbaren Features in Ihrem gewählten Kundensupport-Tool ab und davon, wo Sie Nutzerinformationen speichern.

1. Stellen Sie einen [Nachrichtenlink](https://business.facebook.com/business/help/890732351439459?ref=search_new_0) von Ihrer WhatsApp-Business-Telefonnummer bereit.
2. Stellen Sie [Schnellantwort-Aktionen]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies) bereit, bei denen die Kund:innen mit „Ja“ antworten, um das Opt-in zu bestätigen.
3. Richten Sie einen benutzerdefinierten Schlüsselwort-Trigger ein.
4. Für beide Ansätze müssen Sie den Pfad wahrscheinlich wie folgt abschließen:
	- Rufen Sie den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) auf, um eine:n Nutzer:in zu aktualisieren oder zu erstellen.
	- Nutzen Sie den [`/subscription/status/set`-Endpunkt]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) oder verwenden Sie das [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/).

#### Eingehende WhatsApp-Nachricht {#inbound-whatsapp-message}

Lassen Sie Kund:innen eine eingehende Nachricht an die WhatsApp-Nummer senden.

Dies kann als Canvas oder Campaign eingerichtet werden, je nachdem, ob die Nutzer:innen eine Bestätigungsnachricht auf dem neuen Kanal erhalten sollen.

1. Erstellen Sie eine Campaign mit dem aktionsbasierten Zustellungstrigger einer eingehenden Nachricht.
2. Erstellen Sie eine Webhook-Campaign. Ein Beispiel-Webhook finden Sie unter [Abo-Gruppen]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs#update-subscription-status).

{% alert tip %}
Beachten Sie, dass Sie eine URL oder einen QR-Code zum Beitritt zu einem WhatsApp-Kanal im [WhatsApp-Manager](https://business.facebook.com/wa/manage/phone-numbers/) unter **Phone Number** > **Message Links** erstellen können.<br>![WhatsApp-QR-Code-Ersteller.]({% image_buster /assets/img/whatsapp/whatsapp115.png %}){: style="max-width:55%;"}
{% endalert %}

### Braze-gestützte Opt-in-Methoden {#braze-powered-opt-in-methods}

#### SMS-Nachricht {#sms-message}

Richten Sie in Canvas eine Campaign ein, die Kund:innen fragt, ob sie WhatsApp-Nachrichten erhalten möchten, indem Sie eine der folgenden Methoden verwenden:
- Kundensegment: abonnierte Marketinggruppe außerhalb der USA
- Benutzerdefinierter Schlüsselwort-Trigger

Erfahren Sie mehr über die Aktualisierung des Abo-Status von Nutzerprofilen unter [Abo-Gruppen]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status).

#### In-App- oder In-Browser-Nachricht {#in-app-or-in-browser-message}

Erstellen Sie eine In-App-Nachricht oder ein In-Browser-Pop-up, das Kund:innen auffordert, sich für die WhatsApp-Nutzung anzumelden.

Verwenden Sie eine [HTML-In-App-Nachricht](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal) mit [JavaScript-„Bridge“]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge), um mit dem Braze SDK zu kommunizieren. Stellen Sie sicher, dass Sie die WhatsApp-Abo-Gruppen-ID verwenden.

#### Telefonnummer-Erfassungsformular {#phone-number-capture-form}

Verwenden Sie das [Telefonnummer-Erfassungsformular]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/phone_number_capture)-Template im Drag-and-Drop-Editor für In-App-Nachrichten, um Telefonnummern von Nutzer:innen zu erfassen und Ihre WhatsApp-Abo-Gruppen zu erweitern.

## Opt-outs für Ihren Braze-WhatsApp-Kanal einrichten {#set-up-opt-outs-for-your-braze-whatsapp-channel}

### WhatsApp-Schalter „Angebote und Ankündigungen“ {#whatsapp-offers-and-announcements-toggle}

WhatsApp bietet in den App-Einstellungen einen Schalter „Angebote und Ankündigungen“, mit dem Nutzer:innen Marketing-Nachrichten ablehnen können. Dieser Schalter funktioniert unabhängig von Braze-Abo-Gruppen:

- **Braze-Abo-Gruppen** werden über Ihre Braze-Integration (API, Präferenzzentrum oder SDK) verwaltet und steuern, welche Nutzer:innen Sie für Nachrichten ansprechen.
- **Der native WhatsApp-Schalter** wird von Meta gesteuert und auf Plattformebene durchgesetzt, außerhalb von Braze.

Diese beiden Ebenen synchronisieren sich nicht automatisch. Wenn ein:e Nutzer:in den Schalter „Angebote und Ankündigungen“ in WhatsApp deaktiviert, blockiert Meta die Zustellung von Marketing-Nachrichten auf Plattformebene, selbst wenn der Braze-Abo-Status der Nutzer:innen als „Abonniert“ angezeigt wird. Die Präferenz der Nutzer:innen wird zum Zeitpunkt der Zustellung berücksichtigt.

{% alert note %}
Da Braze kein Opt-out-Signal erhält, bis ein Sendeversuch unternommen wird und Meta einen Fehler zurückgibt, spiegeln die Abo-Zahlen in Braze möglicherweise nicht die Nutzer:innen wider, die sich über den WhatsApp-Schalter abgemeldet haben, bis eine Nachricht versucht wird. Das bedeutet, dass Reichweitenschätzungen leicht überhöht sein können, bis diese Rückkopplungsschleife stattfindet.
{% endalert %}

### Allgemeine Opt-out-Schlüsselwörter {#general-opt-out-keywords}

Sie können eine Campaign oder ein Canvas einrichten, das Nutzer:innen, die bestimmte Wörter senden, von zukünftigen Nachrichten abmeldet. Canvases können besonders vorteilhaft sein, da sie Ihnen ermöglichen, eine Folgenachricht einzufügen, die das erfolgreiche Opt-out bestätigt.

#### 1. Schritt: Canvas mit dem Trigger „Eingehende WhatsApp-Nachricht“ erstellen {#step-1-create-a-canvas-with-a-trigger-of-inbound-whatsapp-message}

![Aktionsbasierter Canvas-Eingangsschritt, der Nutzer:innen aufnimmt, die eine eingehende WhatsApp-Nachricht senden.]({% image_buster /assets/img/whatsapp/whatsapp116.png %}){: style="max-width:85%;"}

Wenn Sie Schlüsselwort-Trigger auswählen, fügen Sie Wörter wie „Stop“ oder „Keine Nachrichten“ hinzu. Wenn Sie diese Methode wählen, stellen Sie sicher, dass Ihre Kund:innen Ihre Opt-out-Wörter kennen. Fügen Sie beispielsweise nach dem ersten Opt-in eine Folgeantwort hinzu wie: „Um sich von diesen Nachrichten abzumelden, senden Sie jederzeit „Stop“."

![Nachrichtenschritt zum Senden einer eingehenden WhatsApp-Nachricht, bei der der Nachrichtentext „STOP“ oder „NO MESSAGE“ lautet.]({% image_buster /assets/img/whatsapp/whatsapp117.png %}){: style="max-width:85%;"}

#### 2. Schritt: Nutzerprofil aktualisieren {#step-2-update-the-users-profile}

Aktualisieren Sie das Nutzerprofil mit einer der unter [Abo-Gruppen]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status) beschriebenen Methoden.

### Marketing-Opt-out-Auswahl {#marketing-opt-out-selection}

Innerhalb des WhatsApp-Nachrichtentemplate-Erstellers können Sie die Option „Marketing-Opt-out“ einfügen. Wenn Sie diese Option verwenden, stellen Sie sicher, dass das Template in einem Canvas mit einem nachfolgenden Schritt für eine Abo-Gruppenänderung verwendet wird.

1. Erstellen Sie ein Nachrichtentemplate mit der Schnellantwort „Marketing-Opt-out“.<br>![Nachrichtentemplate mit einer Fußzeilenoption „Marketing opt-out“.]({% image_buster /assets/img/whatsapp/whatsapp121.png %})<br><br>![Abschnitt zur Konfiguration eines Marketing-Opt-out-Buttons.]({% image_buster /assets/img/whatsapp/whatsapp122.png %})<br><br>
2. Erstellen Sie ein Canvas, das dieses Nachrichtentemplate verwendet.<br><br>
3. Folgen Sie den Schritten im vorherigen Beispiel, aber mit dem Triggertext „STOP PROMOTIONS“.<br><br>
4. Aktualisieren Sie den Abo-Status der Nutzer:innen mit einer der unter [Abo-Gruppen]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status) beschriebenen Methoden.

## Opt-in- und Opt-out-Workflows einrichten {#set-up-opt-in-and-opt-out-workflows}

Sie können „START“- und „STOP“-Schlüsselwort-Antwort-Workflows für WhatsApp mit diesen beiden Methoden konfigurieren:

- [Nutzeraktualisierungsschritt](#user-update-step)
- [Webhook-Campaign zum Auslösen einer zweiten WhatsApp-Campaign](#webhook-campaign-to-trigger-a-second-whatsapp-campaign)

### Nutzeraktualisierungsschritt {#user-update-step}

Der [Nutzeraktualisierungsschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) kann die Telefonnummer der Nutzer:innen zur WhatsApp-Abo-Gruppe hinzufügen, wenn sie ein Schlüsselwort an die Telefonnummer der Abo-Gruppe senden.

Der Nutzeraktualisierungsschritt vermeidet Race-Conditions, da die Nutzer:innen nicht zum nächsten Schritt im Canvas weitergeleitet werden, bevor ihre Telefonnummer zur Abo-Gruppe hinzugefügt wurde. Er erfordert außerdem weniger Einrichtungsschritte als die anderen Methoden, weshalb Braze diese Methode generell empfiehlt.

1. Erstellen Sie ein Canvas mit dem aktionsbasierten Schritt **Send a WhatsApp Inbound Message**. Wählen Sie **Where the message body** und geben Sie „START“ für **Is** ein.

{% alert important %}
Für „STOP“-Nachrichten kehren Sie den Nachrichtenschritt zur Bestätigung des Opt-outs und den Nutzeraktualisierungsschritt um. Andernfalls werden die Nutzer:innen zuerst aus der Abo-Gruppe entfernt und sind dann nicht mehr berechtigt, die Bestätigungsnachricht zu erhalten.
{% endalert %}

![Ein WhatsApp-Nachrichtenschritt, bei dem der Nachrichtentext „START“ lautet.]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:80%;"}

{: start="2"}
2. Erstellen Sie im Canvas einen Schritt **Set Up User Update** und wählen Sie für **Action** die Option **Advanced JSON Editor**. <br><br>![Nutzeraktualisierungsschritt mit der Aktion „Advanced JSON Editor“.]({% image_buster /assets/img/whatsapp/user_update.png %})<br><br>
3. Füllen Sie das **User Update object** mit dem folgenden JSON-Payload aus und ersetzen Sie `XXXXXXXXXXX` durch Ihre Abo-Gruppen-ID:

{% raw %}
```json
{
    "attributes": [
        {
            "subscription_groups": [
                {
                    "subscription_group_id": "XXXXXXXXXXX",
                    "subscription_state": "subscribed"
                }
            ]
        }
    ]
}
```
{% endraw %}

{: start="4"}
4. Fügen Sie einen nachfolgenden WhatsApp-Nachrichtenschritt hinzu. <br><br>![Nutzeraktualisierungsschritt in einem Canvas.]({% image_buster /assets/img/whatsapp/message_step.png %}){: style="max-width:25%;"}

#### Hinweise {#considerations}

Das Update kann mit unterschiedlicher Geschwindigkeit abgeschlossen werden, da Braze die Anfragen des [Nutzeraktualisierungsschritts]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) bündelt.

### Webhook-Campaign zum Auslösen einer zweiten WhatsApp-Campaign {#webhook-campaign-to-trigger-a-second-whatsapp-campaign}

Eine Webhook-Campaign kann den Eintritt in eine zweite Campaign auslösen, nachdem die Telefonnummer der Nutzer:innen zur WhatsApp-Abo-Gruppe hinzugefügt wurde, wenn sie ein Schlüsselwort an die Telefonnummer der Abo-Gruppe senden.

{% alert important %}
Sie müssen diese Methode nicht für STOP-Nachrichten verwenden. Die Bestätigungsnachricht wird gesendet, bevor die Nutzer:innen aus der Abo-Gruppe entfernt werden, sodass Sie einen der beiden anderen Schritte verwenden können.
{% endalert %}

1. Erstellen Sie eine Campaign oder ein Canvas mit einem aktionsbasierten Schritt **Send a WhatsApp Inbound Message**. Wählen Sie **Where the message body** und geben Sie „START“ für **Is** ein.

![WhatsApp-Nachrichtenschritt, bei dem der Nachrichtentext „START“ lautet.]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:85%;"}

{: start="2"}
2. Erstellen Sie in der Campaign oder im Canvas einen Webhook-Nachrichtenschritt und ändern Sie den **Request Body** auf **Raw Text**.

![Nachrichtenschritt für einen Webhook.]({% image_buster /assets/img/whatsapp/webhook_step.png %}){: style="max-width:85%;"}

{: start="3"}
3. Geben Sie die [Endpunkt-URL]({{site.baseurl}}/api/basics) der Kund:innen in die **Webhook URL** ein, gefolgt vom Endpunkt-Link `campaigns/trigger/send`. Zum Beispiel `https://dashboard-02.braze.eu/campaigns/trigger/send`.

![Webhook-URL-Feld im Abschnitt „Webhook verfassen“.]({% image_buster /assets/img/whatsapp/campaigns_webhook_url.png %}){: style="max-width:70%;"}

{: start="4"}
4. Geben Sie im Rohtext den folgenden JSON-Payload ein und ersetzen Sie `XXXXXXXXXXX` durch Ihre Abo-Gruppen-ID. Sie müssen die `campaign_id` ersetzen, nachdem Sie Ihre zweite Campaign erstellt haben.

{% raw %}
```json
{
    "campaign_id": "XXXXXXXXXXX",
    "recipients": [
        {
            "external_user_id": "{{${user_id}}}",
            "attributes": {
                "subscription_groups": [
                    {
                        "subscription_group_id": "XXXXXXXXXXX",
                        "subscription_state": "subscribed"
                    }
                ]
            }
        }
    ]
}
```
{% endraw %}

{: start="5"}
5. Erstellen Sie eine WhatsApp-Campaign (Ihre zweite Campaign) und setzen Sie den Trigger auf API. Stellen Sie sicher, dass Sie diese `campaign_id` in den JSON-Payload Ihrer ersten Campaign kopieren.

#### Hinweise

- Attribut-Updates aus dem Canvas-API-Trigger-JSON-Payload werden noch nicht unterstützt, sodass Sie nur eine WhatsApp-Campaign für die WhatsApp-Antwortnachricht auslösen können (wie in Schritt 2).
- Ein WhatsApp-Template muss genehmigt sein, um es als Antwortnachricht zu senden. Dies liegt daran, dass eine Schnellantwort erfordert, dass der Trigger für eingehende Nachrichten innerhalb derselben Campaign oder desselben Canvas liegt. Wenn Sie einen [Nutzeraktualisierungsschritt](#user-update-step) verwenden, können Sie eine Schnellantwort-Nachricht ohne Meta-Genehmigung senden.

## Den Unterschied zwischen den Modifikatoren „Regex“ und „is“ verstehen {#understanding-the-difference-between-regex-and-is-modifiers}

In dieser Tabelle wird `STOP` als Beispiel-Triggerwort verwendet, um zu zeigen, wie die Modifikatoren funktionieren.

| Modifikator | Triggerwort | Aktion |
| --- | --- | --- |
| `Is` | `STOP` | Erfasst jede vollständige Wortverwendung von „stop“ unabhängig von der Groß-/Kleinschreibung. Dies erfasst beispielsweise „stop“, aber nicht „please stop“. |
| `Matches regex` | `STOP` | Erfasst jede Verwendung von „STOP“ in genau dieser Schreibweise. Dies erfasst beispielsweise „STOP“ und „PLEASE STOP“, aber nicht „stop“. |
| `Matches regex` | `(?i)STOP(?-i)` | Erfasst jede Verwendung von „STOP“ in beliebiger Schreibweise. Dies erfasst beispielsweise „stop“, „please stop“ und „never stop sending me messages“. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Den Unterschied zwischen den Modifikatoren „Regex“ und „is“ verstehen" }