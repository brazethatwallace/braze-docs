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

> Die Handhabung von WhatsApp-Opt-ins und -Opt-outs ist entscheidend, da WhatsApp Ihre [Qualitätsbewertung der Telefonnummer](https://www.facebook.com/business/help/896873687365001) überwacht und niedrige Bewertungen dazu führen können, dass Ihre Nachrichtenlimits reduziert werden. <br><br>Eine Möglichkeit, eine hohe Qualitätsbewertung aufzubauen, besteht darin, zu verhindern, dass Nutzer:innen Ihr Unternehmen blockieren oder melden. Dies kann erreicht werden, indem Sie [qualitativ hochwertige Nachrichten](https://developers.facebook.com/docs/whatsapp/messaging-limits#quality-rating-and-messaging-limits) bereitstellen (z. B. Mehrwert für Ihre Nutzer:innen), die Nachrichtenhäufigkeit kontrollieren und Kund:innen die Möglichkeit geben, den Empfang zukünftiger Kommunikation abzulehnen. <br><br>Einen kanalübergreifenden Überblick über den WhatsApp-Abo-Status finden Sie unter [Abo-Status]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#whatsapp). Diese Seite beschreibt, wie Sie Opt-ins und Opt-outs einrichten und welche Unterschiede zwischen den Modifikatoren „Regex“ und „is“ bestehen.

Opt-ins können aus externen Quellen oder über Braze-Methoden wie SMS oder In-App- und In-Browser-Nachrichten stammen. Opt-outs können über in Braze festgelegte Schlüsselwörter und WhatsApp-Marketing-Buttons verarbeitet werden. Nutzen Sie die folgenden Methoden als Leitfaden für die Einrichtung von Opt-ins und Opt-outs.

## Opt-in-Methoden {#opt-in-methods}
- [Externe Opt-in-Methoden (außerhalb von Braze)](#external-to-braze-opt-in-methods)
  - [Extern erstellte Opt-in-Liste](#externally-built-opt-in-list)
  - [Ausgehende Nachricht im Kundensupport-WhatsApp-Kanal](#outbound-message-in-customer-support-whatsapp-channel)
  - [Eingehende WhatsApp-Nachricht](#inbound-whatsapp-message)
- [Braze-gestützte Opt-in-Methoden](#braze-powered-opt-in-methods)

### Opt-out-Methoden {#opt-out-methods}
- [Allgemeine Opt-out-Schlüsselwörter](#general-opt-out-keywords)
- [Marketing-Opt-out-Auswahl](#marketing-opt-out-selection)

## Opt-ins für Ihren Braze-WhatsApp-Kanal einrichten {#set-up-opt-ins-for-your-braze-whatsapp-channel}

Für WhatsApp-Opt-ins müssen Sie die [Anforderungen von WhatsApp](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) einhalten. Außerdem müssen Sie Braze die folgenden Informationen bereitstellen:
- Eine `external_id`, eine [Telefonnummer]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers) und einen aktualisierten Abo-Status für alle Nutzer:innen. Dies kann über das [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/) oder den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) erfolgen, um die Telefonnummer und den Abo-Status zu aktualisieren.

Eine eingehende WhatsApp-Nachricht abonniert Nutzer:innen nicht automatisch für Ihre WhatsApp-Abo-Gruppe. Sie müssen den Abo-Status explizit über einen [User-Update-Schritt](#user-update-step), einen [Webhook](#webhook-campaign-to-trigger-a-second-whatsapp-campaign) oder einen API-Aufruf aktualisieren.

Meta verlangt, dass der Opt-in-Text:

- Klar angibt, dass die Person dem Empfang von Nachrichten Ihres Unternehmens zustimmt
- Ihren Unternehmensnamen enthält (keine allgemeine Formulierung wie „Wir schreiben Ihnen“)
- Den geltenden lokalen Gesetzen entspricht

{% alert note %}
Braze hat eine Verbesserung des `/users/track`-Endpunkts veröffentlicht, die Aktualisierungen des Abo-Status ermöglicht. Mehr dazu erfahren Sie unter [Abo-Gruppen]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status). Wenn Sie jedoch bereits Opt-in-Protokolle mit dem [`/v2/subscription/status/set`-Endpunkt]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2) erstellt haben, können Sie diese weiterhin dort verwenden.
{% endalert %}

### Externe Opt-in-Methoden außerhalb von Braze {#external-to-braze-opt-in-methods}

Ihre App oder Website (Kontoregistrierung, Checkout-Seite, Kontoeinstellungen, Kreditkartenterminal) an Braze.

Überall dort, wo Sie bereits eine Marketing-Einwilligung für E-Mail oder SMS haben, fügen Sie einen zusätzlichen Abschnitt für WhatsApp hinzu. Nachdem Nutzer:innen sich angemeldet haben, benötigen sie eine `external_id`, eine [Telefonnummer]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers) und einen aktualisierten Abo-Status. Nutzen Sie dazu, je nach Konfiguration Ihrer Braze-Installation, entweder den [`/subscription/status/set`-Endpunkt]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) oder das [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/).

#### Extern erstellte Opt-in-Liste {#externally-built-opt-in-list}

Wenn Sie WhatsApp bereits zuvor verwendet haben, haben Sie möglicherweise schon eine Nutzerliste mit Opt-ins gemäß den WhatsApp-Anforderungen erstellt. Laden Sie in diesem Fall eine CSV-Datei hoch oder verwenden Sie die API mit den [folgenden Informationen]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) in Braze.

#### Ausgehende Nachricht im Kundensupport-WhatsApp-Kanal {#outbound-message-in-customer-support-whatsapp-channel}

Senden Sie in Ihrem Kundensupport-Kanal nach gelösten Anfragen eine automatische Nachricht, in der gefragt wird, ob die Kund:innen Marketing-Nachrichten erhalten möchten. Die Funktionalität hängt hier von den verfügbaren Features in Ihrem Kundensupport-Tool und davon ab, wo Sie Nutzerinformationen speichern.

1. Stellen Sie einen [Nachrichtenlink](https://business.facebook.com/business/help/890732351439459?ref=search_new_0) von Ihrer WhatsApp-Business-Telefonnummer bereit.
2. Stellen Sie [Schnellantwort-Aktionen]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies) bereit, bei denen Kund:innen mit „Ja“ antworten, um das Opt-in zu bestätigen.
3. Richten Sie einen angepassten Keyword-Trigger ein.
4. Für beide Ideen müssen Sie den Pfad wahrscheinlich wie folgt abschließen:
	- Rufen Sie den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) auf, um Nutzer:innen zu aktualisieren oder zu erstellen.
	- Nutzen Sie den [`/subscription/status/set`-Endpunkt]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) oder verwenden Sie das [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/).

#### Eingehende WhatsApp-Nachricht {#inbound-whatsapp-message}

Lassen Sie Kund:innen eine eingehende Nachricht an die WhatsApp-Nummer senden.

Dies kann als Canvas oder als Campaign eingerichtet werden, je nachdem, ob Nutzer:innen eine Bestätigungsnachricht auf dem neuen Kanal erhalten sollen.

1. Erstellen Sie eine Campaign mit dem aktionsbasierten Zustellungstrigger einer eingehenden Nachricht.
2. Erstellen Sie eine Webhook-Campaign. Ein Beispiel-Webhook finden Sie unter [Abo-Gruppen]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs#step-2-update-the-users-profile).

{% alert tip %}
Sie können eine URL oder einen QR-Code erstellen, um einem WhatsApp-Kanal beizutreten – direkt im [WhatsApp-Manager](https://business.facebook.com/wa/manage/phone-numbers/) unter **Phone Number** > **Message Links**.<br>![WhatsApp-QR-Code-Ersteller.]({% image_buster /assets/img/whatsapp/whatsapp115.png %}){: style="max-width:55%;"}
{% endalert %}

### Braze-gestützte Opt-in-Methoden {#braze-powered-opt-in-methods}

#### SMS-Nachricht {#sms-message}

Richten Sie in Canvas eine Campaign ein, die Kund:innen fragt, ob sie WhatsApp-Nachrichten erhalten möchten, indem Sie eine der folgenden Methoden verwenden:
- Kundensegment: abonnierte Marketing-Gruppe außerhalb der USA
- Angepasster Keyword-Trigger

Erfahren Sie mehr über die Aktualisierung des Abo-Status von Nutzerprofilen unter [Abo-Gruppen]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status).

#### In-App- oder In-Browser-Nachricht {#in-app-or-in-browser-message}

Erstellen Sie eine In-App-Nachricht oder ein In-Browser-Pop-up, das Kund:innen auffordert, sich für die WhatsApp-Nutzung anzumelden.

Verwenden Sie eine [HTML-In-App-Nachricht](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal) mit [JavaScript-„Bridge“]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge), um eine Schnittstelle zum Braze SDK herzustellen. Stellen Sie sicher, dass Sie die WhatsApp-Abo-Gruppen-ID verwenden.

#### Formular zur Erfassung der Telefonnummer {#phone-number-capture-form}

Verwenden Sie das Template [Formular zur Erfassung der Telefonnummer]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/phone_number_capture) im Drag-and-Drop-Editor für In-App-Nachrichten, um Telefonnummern von Nutzer:innen zu erfassen und Ihre WhatsApp-Abo-Gruppen zu vergrößern.

## Opt-outs für Ihren Braze-WhatsApp-Kanal einrichten {#set-up-opt-outs-for-your-braze-whatsapp-channel}

### WhatsApp-Schalter „Angebote und Ankündigungen“ {#whatsapp-offers-and-announcements-toggle}

WhatsApp bietet in den App-Einstellungen einen Schalter „Angebote und Ankündigungen“, mit dem Nutzer:innen Marketing-Nachrichten abbestellen können. Dieser Schalter funktioniert unabhängig von Braze-Abo-Gruppen:

- **Braze-Abo-Gruppen** werden über Ihre Braze-Integration (API, Präferenzcenter oder SDK) verwaltet und steuern, welche Nutzer:innen Sie für Messaging ansprechen.
- **Der native WhatsApp-Schalter** wird von Meta gesteuert und auf Plattformebene durchgesetzt, außerhalb von Braze.

Diese beiden Ebenen synchronisieren sich absichtlich nicht automatisch. Wenn Nutzer:innen den Schalter „Angebote und Ankündigungen“ in WhatsApp deaktivieren, blockiert Meta die Zustellung von Marketing-Nachrichten auf Plattformebene – selbst wenn der Braze-Abo-Status der Nutzer:innen als „Subscribed“ angezeigt wird. Die Präferenz der Nutzer:innen wird zum Zeitpunkt der Zustellung berücksichtigt.

{% alert note %}
Da Braze kein Opt-out-Signal erhält, bis ein Sendeversuch unternommen wird und Meta einen Fehler zurückgibt, spiegeln die Abo-Zahlen in Braze möglicherweise nicht die Nutzer:innen wider, die sich über den WhatsApp-Schalter abgemeldet haben, bis eine Nachricht versucht wurde. Das bedeutet, dass Reichweitenschätzungen leicht überhöht sein können, bis diese Feedback-Schleife stattfindet.
{% endalert %}

### Allgemeine Opt-out-Schlüsselwörter {#general-opt-out-keywords}

Sie können eine Campaign oder ein Canvas einrichten, die es Nutzer:innen, die bestimmte Wörter senden, ermöglicht, sich von zukünftigen Nachrichten abzumelden. Canvases können besonders vorteilhaft sein, da Sie eine Folgenachricht einfügen können, die das erfolgreiche Opt-out bestätigt.

#### Schritt 1: Ein Canvas mit dem Trigger „Eingehende WhatsApp-Nachricht“ erstellen {#step-1-create-a-canvas-with-a-trigger-of-inbound-whatsapp-message}

![Aktionsbasierter Canvas-Entry-Schritt, der Nutzer:innen aufnimmt, die eine eingehende WhatsApp-Nachricht senden.]({% image_buster /assets/img/whatsapp/whatsapp116.png %}){: style="max-width:85%;"}

Wenn Sie Schlüsselwort-Trigger auswählen, fügen Sie Wörter wie „Stop“ oder „Keine Nachricht“ hinzu. Wenn Sie diese Methode wählen, stellen Sie sicher, dass Ihre Kund:innen Ihre Opt-out-Wörter kennen. Fügen Sie beispielsweise nach dem ersten Opt-in eine Folgeantwort hinzu wie: „Um sich von diesen Nachrichten abzumelden, senden Sie jederzeit „Stop“."

![Nachrichtenschritt zum Senden einer eingehenden WhatsApp-Nachricht, bei der der Nachrichtentext „STOP“ oder „NO MESSAGE“ lautet.]({% image_buster /assets/img/whatsapp/whatsapp117.png %}){: style="max-width:85%;"}

#### Schritt 2: Das Profil der Nutzer:innen aktualisieren {#step-2-update-the-users-profile}

Aktualisieren Sie das Profil der Nutzer:innen, indem Sie eine der in [Abo-Gruppen]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status) beschriebenen Methoden verwenden.

### Marketing-Opt-out-Auswahl {#marketing-opt-out-selection}

Im WhatsApp-Nachrichten-Template-Creator können Sie die Option „Marketing-Opt-out“ einfügen. Wenn Sie diese Option verwenden, stellen Sie sicher, dass das Template in einem Canvas mit einem nachfolgenden Schritt für eine Abo-Gruppen-Änderung verwendet wird.

1. Erstellen Sie ein Nachrichten-Template mit der Schnellantwort „Marketing-Opt-out“.<br>![Nachrichten-Template mit einer Fußzeilenoption „Marketing-Opt-out“]({% image_buster /assets/img/whatsapp/whatsapp121.png %})<br><br>![Bereich zum Konfigurieren eines Marketing-Opt-out-Buttons.]({% image_buster /assets/img/whatsapp/whatsapp122.png %})<br><br>
2. Erstellen Sie ein Canvas, das dieses Nachrichten-Template verwendet.<br><br>
3. Folgen Sie den Schritten im vorherigen Beispiel, jedoch mit dem Trigger-Text „STOP PROMOTIONS“.<br><br>
4. Aktualisieren Sie den Abo-Status der Nutzer:innen, indem Sie eine der in [Abo-Gruppen]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status) beschriebenen Methoden verwenden.

## Opt-in- und Opt-out-Workflows einrichten {#set-up-opt-in-and-opt-out-workflows}

Sie können „START“- und „STOP“-Keyword-Antwort-Workflows für WhatsApp mit diesen beiden Methoden konfigurieren:

- [User-Update-Schritt](#user-update-step)
- [Webhook-Campaign zum Auslösen einer zweiten WhatsApp-Campaign](#webhook-campaign-to-trigger-a-second-whatsapp-campaign)

### User-Update-Schritt {#user-update-step}

Der [User-Update-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) kann die Telefonnummer der Nutzer:innen zur WhatsApp-Abo-Gruppe hinzufügen, wenn sie ein Keyword an die Telefonnummer der Abo-Gruppe senden.

Der User-Update-Schritt vermeidet Race-Conditions, da die Nutzer:innen nicht zum nächsten Schritt im Canvas weitergeleitet werden, bevor ihre Telefonnummer zur Abo-Gruppe hinzugefügt wurde. Außerdem sind weniger Schritte zur Einrichtung erforderlich als bei den anderen Methoden, weshalb Braze diese Methode generell empfiehlt.

1. Erstellen Sie einen Canvas mit dem aktionsbasierten Schritt **Send a WhatsApp Inbound Message**. Wählen Sie **Where the message body** und geben Sie „START“ für **Is** ein.

{% alert important %}
Für „STOP“-Nachrichten kehren Sie den Nachrichtenschritt zur Bestätigung des Opt-outs und den User-Update-Schritt um. Andernfalls werden die Nutzer:innen zuerst aus der Abo-Gruppe entfernt und sind dann nicht mehr berechtigt, die Bestätigungsnachricht zu empfangen.
{% endalert %}

![Ein WhatsApp-Nachrichtenschritt, bei dem der Nachrichtentext „START“ lautet.]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:80%;"}

{: start="2"}
2. Erstellen Sie im Canvas einen **Set Up User Update**-Schritt und wählen Sie für **Action** die Option **Advanced JSON Editor**. <br><br>![User-Update-Schritt mit der Aktion „Advanced JSON Editor“.]({% image_buster /assets/img/whatsapp/user_update.png %})<br><br>
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
4. Fügen Sie einen nachfolgenden WhatsApp-Nachrichtenschritt hinzu. <br><br>![User-Update-Schritt in einem Canvas.]({% image_buster /assets/img/whatsapp/message_step.png %}){: style="max-width:25%;"}

#### Hinweise {#considerations}

Das Update kann mit unterschiedlicher Geschwindigkeit abgeschlossen werden, da Braze die Anfragen des [User-Update-Schritts]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) bündelt. Für zeitkritische Opt-in-Flows, bei denen die Bestätigung sofort nach dem Abo-Update gesendet werden muss, verwenden Sie stattdessen die [Webhook-Methode](#webhook-campaign-to-trigger-a-second-whatsapp-campaign) anstelle eines User-Update-Schritts.

### Webhook-Campaign zum Auslösen einer zweiten WhatsApp-Campaign {#webhook-campaign-to-trigger-a-second-whatsapp-campaign}

Eine Webhook-Campaign kann den Eintritt in eine zweite Campaign auslösen, nachdem die Telefonnummer der Nutzer:innen zur WhatsApp-Abo-Gruppe hinzugefügt wurde, wenn sie ein Keyword an die Telefonnummer der Abo-Gruppe senden.

{% alert important %}
Sie müssen diese Methode nicht für STOP-Nachrichten verwenden. Die Bestätigungsnachricht wird gesendet, bevor die Nutzer:innen aus der Abo-Gruppe entfernt werden, sodass Sie einen der beiden anderen Schritte verwenden können.
{% endalert %}

1. Erstellen Sie eine Campaign oder einen Canvas mit einem aktionsbasierten Schritt **Send a WhatsApp Inbound Message**. Wählen Sie **Where the message body** und geben Sie „START“ für **Is** ein.

![WhatsApp-Nachrichtenschritt, bei dem der Nachrichtentext „START“ lautet.]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:85%;"}

{: start="2"}
2. Erstellen Sie in der Campaign oder im Canvas einen Webhook-Nachrichtenschritt und ändern Sie den **Request Body** auf **Raw Text**.

![Nachrichtenschritt für einen Webhook.]({% image_buster /assets/img/whatsapp/webhook_step.png %}){: style="max-width:85%;"}

{: start="3"}
3. Geben Sie die [Endpunkt-URL]({{site.baseurl}}/api/basics) der Kund:innen in die **Webhook URL** ein, gefolgt vom Endpunkt-Link `campaigns/trigger/send`. Zum Beispiel: `https://dashboard-02.braze.eu/campaigns/trigger/send`.

![Webhook-URL-Feld im Abschnitt „Compose Webhook“.]({% image_buster /assets/img/whatsapp/campaigns_webhook_url.png %}){: style="max-width:70%;"}

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
- Ein WhatsApp-Template muss genehmigt sein, um es als Antwortnachricht zu senden. Dies liegt daran, dass eine Schnellantwort erfordert, dass der Trigger für eingehende Nachrichten innerhalb derselben Campaign oder desselben Canvas liegt. Wenn Sie einen [User-Update-Schritt](#user-update-step) verwenden, können Sie eine Schnellantwort-Nachricht ohne Meta-Genehmigung senden.

## Den Unterschied zwischen den Modifikatoren „Regex“ und „ist“ verstehen {#understanding-the-difference-between-regex-and-is-modifiers}

In dieser Tabelle wird `STOP` als Beispiel-Trigger-Wort verwendet, um die Funktionsweise der Modifikatoren zu veranschaulichen.

| Modifikator | Trigger-Wort | Aktion |
| --- | --- | --- |
| `Is` | `STOP` | Erkennt jede Verwendung von „stop“ als ganzes Wort, unabhängig von der Groß-/Kleinschreibung. Dies erkennt beispielsweise „stop“, aber nicht „please stop“. |
| `Matches regex` | `STOP` | Erkennt jede Verwendung von „STOP“ in genau dieser Schreibweise. Dies erkennt beispielsweise „STOP“ und „PLEASE STOP“, aber nicht „stop“. |
| `Matches regex` | `(?i)STOP(?-i)` | Erkennt jede Verwendung von „STOP“ unabhängig von der Groß-/Kleinschreibung. Dies erkennt beispielsweise „stop“, „please stop“ und „never stop sending me messages“. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Den Unterschied zwischen den Modifikatoren „Regex“ und „ist“ verstehen" }