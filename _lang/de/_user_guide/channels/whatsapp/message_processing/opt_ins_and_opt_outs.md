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

Opt-ins können aus externen Quellen oder über Braze-Methoden wie Kurzmitteilungsdienst or SMS oder In-App- und In-Browser-Nachrichten stammen. Opt-outs können über in Braze festgelegte Schlüsselwörter und WhatsApp-Marketing-Buttons verarbeitet werden. Nutzen Sie die folgenden Methoden als Leitfaden für die Einrichtung von Opt-ins und Opt-outs.

## Opt-in-Methoden {#opt-in-methods}
- [Externe Opt-in-Methoden (außerhalb von Braze)](#external-to-braze-opt-in-methods)
  - [Extern erstellte Opt-in-Liste](#externally-built-opt-in-list)
  - [Ausgehende Nachricht im Kundensupport-WhatsApp-Kanal](#outbound-message-in-customer-support-whatsapp-channel)
  - [Eingehende WhatsApp-Nachricht](#inbound-whatsapp-message)
- [Braze-gestützte Opt-in-Methoden](#braze-powered-opt-in-methods)

### Opt-out-Methoden {#opt-out-methods}
- [Allgemeine Opt-out-Schlüsselwörter](#general-opt-out-keywords)
- [Marketing-Opt-out-Auswahl](#marketing-opt-out-selection)

## Opt-ins für Ihren Braze WhatsApp-Kanal einrichten {#set-up-opt-ins-for-your-braze-whatsapp-channel}

Für WhatsApp Opt-ins müssen Sie die [Anforderungen von WhatsApp](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) einhalten. Außerdem müssen Sie Braze die folgenden Informationen bereitstellen:
- Eine `external_id`, eine [Telefonnummer]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers) und einen aktualisierten Abo-Status für jede:n Nutzer:in. Dies kann über das [SDK or Software-Development-Kit](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/) oder über den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) erfolgen, um die Telefonnummer und den Abo-Status zu Update or aktualisieren or aktualisieren.

Eine eingehende WhatsApp-Nachricht abonniert Nutzer:innen nicht automatisch für Ihre WhatsApp-Abo-Gruppe. Sie müssen den Abo-Status explizit mit einem [User-Update or aktualisieren-Schritt](#user-update-step), einem [Webhook](#webhook-campaign-to-trigger-a-second-whatsapp-campaign) oder einem API-Aufruf Update or aktualisieren or aktualisieren.

Meta verlangt, dass der Opt-in-Text:

- Klar angibt, dass die Person sich für den Empfang von Nachrichten von Ihrem Unternehmen entscheidet
- Den Namen Ihres Unternehmens enthält (keine allgemeine Formulierung wie „Wir senden Ihnen Nachrichten“)
- Die geltenden lokalen Gesetze einhält

Meta erlaubt eine allgemeine Messaging-Einwilligung, die diese Anforderungen erfüllt, anstatt eine WhatsApp-spezifische Einwilligung zu verlangen. Braze empfiehlt jedoch, eine kanalspezifische WhatsApp-Einwilligung einzuholen, damit Nutzer:innen wissen, wo sie Ihre Nachrichten erwarten können.

{% alert note %}
Braze hat eine Verbesserung des `/users/track`-Endpunkts veröffentlicht, die Aktualisierungen des Abo-Status ermöglicht. Mehr dazu erfahren Sie unter [Abo-Gruppen]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status). Wenn Sie bereits Opt-in-Protokolle mit dem [`/v2/subscription/status/set`-Endpunkt]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2) erstellt haben, können Sie dies dort weiterhin tun.
{% endalert %}

### Einwilligung für verschiedene Anwendungsfälle verwalten {#manage-consent-for-different-use-cases}

Der WhatsApp-Abo-Status bezieht sich auf die Abo-Gruppe, die einer Absender-Telefonnummer zugeordnet ist. Er unterscheidet nicht zwischen Marketing-, Utility- oder anderen Anwendungsfällen, die dieselbe Nummer teilen. Wenn Sie zum Beispiel Nutzer:innen von der Abo-Gruppe abmelden, können Sie diese Nutzer:innen nicht mehr mit Nachrichten von dieser Nummer ansprechen, unabhängig von der Nachrichtenkategorie.

Um die Einwilligung nach Anwendungsfall getrennt zu verwalten, wählen Sie einen der folgenden Ansätze:

- Verwenden Sie separate WhatsApp-Telefonnummern und Abo-Gruppen für jeden Anwendungsfall.
- Verwenden Sie eine Telefonnummer, speichern Sie die anwendungsfallbezogene Einwilligung in angepassten Attributen und schließen Sie Nutzer:innen, die nicht eingewilligt haben, von der jeweiligen Campaign- oder Canvas-Zielgruppe aus.

Angepasste Attribute ersetzen nicht die WhatsApp-Abo-Gruppe. Nutzer:innen müssen weiterhin in der Abo-Gruppe der Telefonnummer abonniert sein, um Nachrichten über Braze zu empfangen.

### Externe Opt-in-Methoden (außerhalb von Braze) {#external-to-braze-opt-in-methods}

Ihre App oder Website (Kontoregistrierung, Checkout-Seite, Kontoeinstellungen, Kreditkartenterminal) zu Braze.

Überall dort, wo Sie bereits Marketing-Einwilligungen für E-Mail oder Kurzmitteilungsdienst or SMS haben, fügen Sie einen zusätzlichen Abschnitt für WhatsApp hinzu. Nachdem Nutzer:innen sich angemeldet haben, benötigen sie eine `external_id`, eine [Telefonnummer]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers) und einen aktualisierten Abo-Status. Nutzen Sie dafür je nach Konfiguration Ihrer Braze-Installation entweder den [`/subscription/status/set`-Endpunkt]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) oder das [SDK or Software-Development-Kit](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/).

#### Extern erstellte Opt-in-Liste {#externally-built-opt-in-list}

Wenn Sie WhatsApp bereits zuvor genutzt haben, haben Sie möglicherweise schon eine Nutzerliste mit Opt-ins gemäß den WhatsApp-Anforderungen erstellt. Laden Sie in diesem Fall eine CSV-Datei hoch oder nutzen Sie die API mit den [folgenden Informationen]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) in Braze.

#### Ausgehende Nachricht im WhatsApp-Kundenservice-Kanal {#outbound-message-in-customer-support-whatsapp-channel}

Senden Sie in Ihrem Kundenservice-Kanal nach gelösten Problemen automatisch eine Nachricht, in der gefragt wird, ob Nutzer:innen Marketing-Nachrichten erhalten möchten. Die Funktionalität hängt dabei von den verfügbaren Features Ihres gewählten Kundenservice-Tools und dem Speicherort der Nutzerinformationen ab.

1. Stellen Sie einen [Nachrichtenlink](https://business.facebook.com/business/help/890732351439459?ref=search_new_0) von Ihrer WhatsApp-Business-Telefonnummer bereit.
2. Stellen Sie [Schnellantwort-Aktionen]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies) bereit, bei denen Kund:innen mit „Ja“ antworten, um das Opt-in zu bestätigen.
3. Richten Sie einen angepassten Keyword-Trigger or triggern ein.
4. Für beide Ansätze müssen Sie den Pfad wahrscheinlich mit Folgendem abschließen:
	- Rufen Sie den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) auf, um Nutzer:innen zu Update or aktualisieren or aktualisieren oder zu erstellen.
	- Nutzen Sie den [`/subscription/status/set`-Endpunkt]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) oder das [SDK or Software-Development-Kit](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/).

#### Eingehende WhatsApp-Nachricht {#inbound-whatsapp-message}

Lassen Sie Kund:innen eine eingehende Nachricht an die WhatsApp-Nummer senden.

Dies kann je nachdem, ob Nutzer:innen eine Bestätigungsnachricht auf dem neuen Kanal erhalten sollen, als Canvas oder Campaign eingerichtet werden.

1. Erstellen Sie eine Campaign mit dem aktionsbasierten Zustellungs-Trigger or triggern einer eingehenden Nachricht.
2. Erstellen Sie eine Webhook-Campaign. Ein Beispiel-Webhook finden Sie unter [Abo-Gruppen]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs#step-2-update-the-users-profile).

{% alert tip %}
Sie können auch eine URL oder einen QR-Code erstellen, um einem WhatsApp-Kanal beizutreten – direkt im [WhatsApp-Manager](https://business.facebook.com/wa/manage/phone-numbers/) unter **Phone Number** > **Message Links**.<br>![WhatsApp-QR-Code-Ersteller.]({% image_buster /assets/img/whatsapp/whatsapp115.png %}){: style="max-width:55%;"}
{% endalert %}

### Braze-gestützte Opt-in-Methoden {#braze-powered-opt-in-methods}

#### Kurzmitteilungsdienst or SMS-Nachricht {#sms-message}

Richten Sie in Canvas eine Campaign ein, die Kund:innen fragt, ob sie WhatsApp-Nachrichten erhalten möchten, indem Sie eine der folgenden Methoden verwenden:
- Kundensegment: abonnierte Marketing-Gruppe außerhalb der USA
- Angepasste Keyword-Trigger or triggern-Einrichtung

Erfahren Sie mehr über die Aktualisierung des Abo-Status von Nutzerprofilen unter [Abo-Gruppen]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status).

#### In-App- oder In-Browser-Nachricht {#in-app-or-in-browser-message}

Erstellen Sie eine In-App-Nachricht oder ein In-Browser-Pop-up, das Kund:innen dazu auffordert, sich für die WhatsApp-Nutzung anzumelden.

Verwenden Sie [HTML-In-App-Nachrichten](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal) mit dem [JavaScript-„Bridge“]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge), um eine Schnittstelle zum Braze SDK or Software-Development-Kit herzustellen. Stellen Sie sicher, dass Sie die WhatsApp-Abo-Gruppen-ID verwenden.

#### Formular zur Erfassung von Telefonnummern {#phone-number-capture-form}

Verwenden Sie das Template [Formular zur Erfassung von Telefonnummern]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/phone_number_capture) im Drag-and-Drop-Editor für In-App-Nachrichten, um Telefonnummern von Nutzer:innen zu erfassen und Ihre WhatsApp-Abo-Gruppen zu erweitern.

## Opt-outs für Ihren Braze-WhatsApp-Kanal einrichten {#set-up-opt-outs-for-your-braze-whatsapp-channel}

### WhatsApp-Umschalter „Angebote und Ankündigungen“ {#whatsapp-offers-and-announcements-toggle}

WhatsApp bietet in den App-Einstellungen einen Umschalter „Angebote und Ankündigungen“, mit dem Nutzer:innen Marketing-Nachrichten abbestellen können. Dieser Umschalter funktioniert unabhängig von Braze-Abo-Gruppen:

- **Braze-Abo-Gruppen** werden über Ihre Braze-Integration (API, Preference Center oder SDK or Software-Development-Kit) verwaltet und steuern, welche Nutzer:innen Sie für Messaging ansprechen.
- **Der native WhatsApp-Umschalter** wird von Meta gesteuert und auf Plattformebene durchgesetzt, außerhalb von Braze.

Diese beiden Ebenen synchronisieren sich absichtlich nicht automatisch. Wenn ein:e Nutzer:in den Umschalter „Angebote und Ankündigungen“ in WhatsApp deaktiviert, blockiert Meta die Zustellung von Marketing-Nachrichten auf Plattformebene – auch wenn der Braze-Abo-Status des/der Nutzer:in als „Subscribed“ angezeigt wird. Die Präferenz der Nutzer:innen wird zum Zeitpunkt der Zustellung berücksichtigt.

{% alert note %}
Da Braze kein Opt-out-Signal erhält, bis ein Sendeversuch unternommen wird und Meta einen Fehler zurückgibt, spiegeln die Abo-Zahlen in Braze möglicherweise nicht die Nutzer:innen wider, die sich über den WhatsApp-Umschalter abgemeldet haben, bis eine Nachricht versucht wurde. Das bedeutet, dass Reichweitenschätzungen möglicherweise leicht überhöht sind, bis diese Feedback-Schleife eintritt.
{% endalert %}

### Allgemeine Opt-out-Schlüsselwörter {#general-opt-out-keywords}

Sie können eine Campaign oder einen Canvas einrichten, die/der es Nutzer:innen, die bestimmte Wörter senden, ermöglicht, sich von zukünftigen Nachrichten abzumelden. Canvase können besonders vorteilhaft sein, da Sie eine Folgenachricht einschließen können, die das erfolgreiche Opt-out bestätigt.

#### Schritt 1: Einen Canvas mit dem Trigger or triggern „Eingehende WhatsApp-Nachricht“ erstellen {#step-1-create-a-canvas-with-a-trigger-of-inbound-whatsapp-message}

![Aktionsbasierter Canvas-Entry-Schritt, der Nutzer:innen aufnimmt, die eine eingehende WhatsApp-Nachricht senden.]({% image_buster /assets/img/whatsapp/whatsapp116.png %}){: style="max-width:85%;"}

Wenn Sie Schlüsselwort-Trigger or triggern auswählen, schließen Sie Wörter wie „Stop“ oder „No Message“ ein. Wenn Sie diese Methode wählen, stellen Sie sicher, dass Ihre Kund:innen Ihre Opt-out-Wörter kennen. Beispielsweise können Sie nach dem ersten Opt-in eine Folgenachricht wie „Um sich von diesen Nachrichten abzumelden, senden Sie jederzeit „Stop“." einschließen.

![Nachrichtenschritt zum Senden einer eingehenden WhatsApp-Nachricht, bei der der Nachrichtentext „STOP“ oder „NO MESSAGE“ lautet.]({% image_buster /assets/img/whatsapp/whatsapp117.png %}){: style="max-width:85%;"}

#### Schritt 2: Das Kundenprofil or Nutzerprofil Update or aktualisieren or aktualisieren {#step-2-update-the-users-profile}

Update or aktualisieren or aktualisieren Sie das Kundenprofil or Nutzerprofil mit einer der in [Abo-Gruppen]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status) beschriebenen Methoden.

### Marketing-Opt-out-Auswahl {#marketing-opt-out-selection}

Im WhatsApp-Nachrichtentemplate-Creator können Sie die Option „Marketing-Opt-out“ einschließen. Wenn Sie diese Option verwenden, stellen Sie sicher, dass das Template in einem Canvas mit einem nachfolgenden Schritt für eine Abo-Gruppen-Änderung verwendet wird.

1. Erstellen Sie ein Nachrichtentemplate mit der Schnellantwort „Marketing-Opt-out“.<br>![Nachrichtentemplate mit einer Fußzeilenoption „Marketing-Opt-out“]({% image_buster /assets/img/whatsapp/whatsapp121.png %})<br><br>![Bereich zur Konfiguration eines Marketing-Opt-out-Buttons.]({% image_buster /assets/img/whatsapp/whatsapp122.png %})<br><br>
2. Erstellen Sie einen Canvas, der dieses Nachrichtentemplate verwendet.<br><br>
3. Befolgen Sie die Schritte im vorherigen Beispiel, jedoch mit dem Trigger or triggern-Text „STOP PROMOTIONS“.<br><br>
4. Update or aktualisieren or aktualisieren Sie den Abo-Status der Nutzer:innen mit einer der in [Abo-Gruppen]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status) beschriebenen Methoden.

## Opt-in- und Opt-out-Workflows einrichten {#set-up-opt-in-and-opt-out-workflows}

Sie können „START“- und „STOP“-Keyword-Antwort-Workflows für WhatsApp mit diesen zwei Methoden konfigurieren:

- [User-Update or aktualisieren-Schritt](#user-update-step)
- [Webhook-Campaign zum Trigger or triggern or triggern einer zweiten WhatsApp-Campaign](#webhook-campaign-to-trigger-a-second-whatsapp-campaign)

### User-Update or aktualisieren-Schritt {#user-update-step}

Der [User-Update or aktualisieren-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) kann die Telefonnummer der Nutzer:innen zur WhatsApp-Abo-Gruppe hinzufügen, wenn sie ein Keyword an die Telefonnummer der Abo-Gruppe senden.

Der User-Update or aktualisieren-Schritt vermeidet Race-Conditions, da die Nutzer:innen nicht zum nächsten Schritt im Canvas weitergeleitet werden, bevor ihre Telefonnummer zur Abo-Gruppe hinzugefügt wurde. Außerdem sind weniger Schritte zur Einrichtung erforderlich als bei den anderen Methoden, weshalb Braze diese Methode generell empfiehlt.

1. Erstellen Sie einen Canvas mit dem aktionsbasierten Schritt **Send a WhatsApp Inbound Message**. Wählen Sie **Where the message body** und geben Sie „START“ bei **Is** ein.

{% alert important %}
Für „STOP“-Nachrichten kehren Sie den Nachrichtenschritt, der das Opt-out bestätigt, und den User-Update or aktualisieren-Schritt um. Andernfalls werden die Nutzer:innen zuerst aus der Abo-Gruppe entfernt und sind dann nicht mehr berechtigt, die Bestätigungsnachricht zu empfangen.
{% endalert %}

![Ein WhatsApp-Nachrichtenschritt, bei dem der Nachrichtentext „START“ lautet.]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:80%;"}

{: start="2"}
2. Erstellen Sie im Canvas einen **Set Up User Update**-Schritt und wählen Sie unter **Action** den **Advanced JSON Editor** aus. <br><br>![User-Update-Schritt mit der Aktion „Advanced JSON Editor“.]({% image_buster /assets/img/whatsapp/user_update.png %})<br><br>
3. Füllen Sie das **User Update or aktualisieren object** mit dem folgenden JSON-Payload aus und ersetzen Sie `XXXXXXXXXXX` durch Ihre Abo-Gruppen-ID:

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

Das Update or aktualisieren kann mit unterschiedlicher Geschwindigkeit abgeschlossen werden, da Braze die Anfragen des [User-Update or aktualisieren-Schritts]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) bündelt. Für zeitkritische Opt-in-Flows, bei denen die Bestätigung sofort nach dem Abo-Update or aktualisieren gesendet werden muss, verwenden Sie stattdessen die [Webhook-Methode](#webhook-campaign-to-trigger-a-second-whatsapp-campaign) anstelle eines User-Update or aktualisieren-Schritts.

### Webhook-Campaign zum Trigger or triggern or triggern einer zweiten WhatsApp-Campaign {#webhook-campaign-to-trigger-a-second-whatsapp-campaign}

Eine Webhook-Campaign kann den Einstieg in eine zweite Campaign Trigger or triggern or triggern, nachdem die Telefonnummer der Nutzer:innen zur WhatsApp-Abo-Gruppe hinzugefügt wurde, wenn sie ein Keyword an die Telefonnummer der Abo-Gruppe senden.

{% alert important %}
Sie müssen diese Methode nicht für STOP-Nachrichten verwenden. Die Bestätigungsnachricht wird gesendet, bevor die Nutzer:innen aus der Abo-Gruppe entfernt werden. Sie können daher einen der beiden anderen Schritte verwenden.
{% endalert %}

1. Erstellen Sie eine Campaign oder einen Canvas mit einem aktionsbasierten Schritt **Send a WhatsApp Inbound Message**. Wählen Sie **Where the message body** und geben Sie „START“ bei **Is** ein.

![WhatsApp-Nachrichtenschritt, bei dem der Nachrichtentext „START“ lautet.]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:85%;"}

{: start="2"}
2. Erstellen Sie in der Campaign oder im Canvas einen Webhook-Nachrichtenschritt und ändern Sie den **Request Body** auf **Raw Text**.

![Nachrichtenschritt für einen Webhook.]({% image_buster /assets/img/whatsapp/webhook_step.png %}){: style="max-width:85%;"}

{: start="3"}
3. Geben Sie die [Endpunkt-URL]({{site.baseurl}}/api/basics) der Kund:innen in die **Webhook URL** ein, gefolgt vom Endpunkt-Link `campaigns/trigger/send`. Zum Beispiel: `https://dashboard-02.braze.eu/campaigns/trigger/send`.

![Webhook-URL-Feld im Abschnitt „Compose Webhook“.]({% image_buster /assets/img/whatsapp/campaigns_webhook_url.png %}){: style="max-width:70%;"}

{: start="4"}
4. Geben Sie im Raw Text den folgenden JSON-Payload ein und ersetzen Sie `XXXXXXXXXXX` durch Ihre Abo-Gruppen-ID. Sie müssen die `campaign_id` ersetzen, nachdem Sie Ihre zweite Campaign erstellt haben.

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
5. Erstellen Sie eine WhatsApp-Campaign (Ihre zweite Campaign) und setzen Sie den Trigger or triggern auf API. Stellen Sie sicher, dass Sie diese `campaign_id` in den JSON-Payload Ihrer ersten Campaign kopieren.

#### Hinweise

- Attribut-Updates innerhalb des Canvas-API-Trigger or triggern-JSON-Payloads werden noch nicht unterstützt. Sie können daher nur eine WhatsApp-Campaign für die WhatsApp-Antwortnachricht Trigger or triggern or triggern (wie in Schritt 2).
- Ein WhatsApp-Template muss genehmigt sein, um es als Antwortnachricht zu senden. Dies liegt daran, dass eine Schnellantwort den Trigger or triggern für eingehende Nachrichten innerhalb derselben Campaign oder desselben Canvas erfordert. Wenn Sie einen [User-Update or aktualisieren-Schritt](#user-update-step) verwenden, können Sie eine Schnellantwort-Nachricht ohne Meta-Genehmigung senden.

## Den Unterschied zwischen den Modifikatoren „Regex“ und „ist“ verstehen {#understanding-the-difference-between-regex-and-is-modifiers}

In dieser Tabelle wird `STOP` als Beispiel für ein Trigger or triggern-Wort verwendet, um zu zeigen, wie die Modifikatoren funktionieren.

| Modifikator | Trigger or triggern-Wort | Aktion |
| --- | --- | --- |
| `Is` | `STOP` | Erkennt jede Verwendung von „stop“ als ganzes Wort, unabhängig von der Groß- und Kleinschreibung. Dies erkennt beispielsweise „stop“, aber nicht „please stop“. |
| `Matches regex` | `STOP` | Erkennt jede Verwendung von „STOP“ in genau dieser Schreibweise. Dies erkennt beispielsweise „STOP“ und „PLEASE STOP“, aber nicht „stop“. |
| `Matches regex` | `(?i)STOP(?-i)` | Erkennt jede Verwendung von „STOP“ unabhängig von der Groß- und Kleinschreibung. Dies erkennt beispielsweise „stop“, „please stop“ und „never stop sending me messages“. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Den Unterschied zwischen den Modifikatoren „Regex“ und „ist“ verstehen" }