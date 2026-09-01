---
nav_title: Nachricht erstellen
article_title: Eine SMS-, MMS- oder RCS-Nachricht erstellen
page_order: 1
description: "Erstellen Sie eine SMS-, MMS- oder RCS-Nachricht und konfigurieren Sie kanalspezifische Nachrichtentypen, Felder, Link-Shortening, Zustellungseinstellungen und Verhalten."
page_type: reference
alias: /create_sms_mms_rcs_message/
tool:
  - Campaigns
  - Canvas
channel:
  - SMS
  - MMS
  - RCS
search_rank: 1
---

# Eine SMS-, MMS- oder RCS-Nachricht erstellen {#create-an-sms-mms-or-rcs-message}

> Erstellen Sie personalisierte SMS-, MMS- und Rich Communication Services (RCS)-Nachrichten in Campaigns oder Canvas. Die ausgewählte Abo-Gruppe bestimmt, welche Nachrichtentypen und Absender verfügbar sind.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, stellen Sie sicher, dass Sie über Folgendes verfügen:

| Voraussetzung | Beschreibung |
| --- | --- |
| Sender-Einrichtung | Schließen Sie die [Sender-Einrichtung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup) ab. Um MMS zu senden, benötigt Ihre Abo-Gruppe eine MMS-fähige Telefonnummer. Um RCS zu senden, schließen Sie die [RCS-Einrichtung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup) ab und fügen Sie einen verifizierten RCS-Sender hinzu. |
| Abo-Gruppe | Erstellen Sie eine [Abo-Gruppe]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups), die die Sender für diese Nachricht enthält. |
| Telefonnummern und Einwilligung der Nutzer:innen | Importieren Sie die Telefonnummern Ihrer Nutzer:innen und erfassen Sie die entsprechenden [SMS-, MMS- und RCS-Opt-ins]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins). |
| Campaign oder Canvas | Verwenden Sie eine Campaign für eine einzelne gezielte Nachricht oder ein Canvas für eine mehrstufige User-Journey. |
| Nachrichten- oder Aktionsguthaben | Vergewissern Sie sich, dass Ihr Konto über verfügbare Guthaben verfügt. Der Versand von SMS-, MMS- und RCS-Nachrichten über Braze verwendet diese Guthaben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen für SMS-, MMS- und RCS-Nachrichten" }

## Nachricht erstellen {#create-a-message}

### Schritt 1: Wählen Sie, wo Sie Ihre Nachricht erstellen möchten {#step-1-choose-where-to-build-your-message}

{% tabs %}
{% tab Campaign %}

1. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Campaign erstellen**.
2. Wählen Sie **SMS/MMS/RCS** oder, für Campaigns, die auf mehrere Kanäle abzielen, **Multichannel Campaign**.
3. Geben Sie Ihrer Campaign einen aussagekräftigen Namen.
4. Fügen Sie nach Bedarf [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) und [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) hinzu.
  - Tags erleichtern das Auffinden und Verwenden Ihrer Campaigns in Berichten.
5. Fügen Sie die Varianten für Ihre Campaign hinzu und benennen Sie sie. Sie können SMS/MMS- und RCS-Varianten in derselben Campaign verwenden. Weitere Informationen finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Wenn die Varianten Ihrer Campaign ähnliche Inhalte haben, verfassen Sie zunächst die erste Nachricht, bevor Sie weitere Varianten hinzufügen. Wählen Sie dann **Aus Variante kopieren** aus dem Dropdown **Variante hinzufügen**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

### Schritt 2: Abo-Gruppe und Nachrichtentyp auswählen {#step-2-select-a-subscription-group-and-message-type}

Wählen Sie die **Abo-Gruppe** aus, die den Absender für diese Nachricht enthält. Braze verwendet die ausgewählte Gruppe zur Berechnung der erreichbaren Zielgruppe und zur Bestimmung der Sendezeitberechtigung.

Die gewählte Abo-Gruppe bestimmt, welche Nachrichtentypen im Editor verfügbar sind:

| Abo-Gruppentyp | Verfügbare Nachrichtentypen |
| --- | --- |
| Nur SMS | SMS |
| SMS mit MMS-fähigen Nummern | SMS und MMS |
| RCS-fähig mit einem verifizierten RCS-Absender | RCS und SMS, wenn die Gruppe auch einen SMS-Absender enthält. MMS ist ebenfalls verfügbar, wenn dieser Absender MMS-fähig ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Verfügbare Nachrichtentypen nach Abo-Gruppe" }

{% alert tip %}
Fügen Sie einer RCS-Abo-Gruppe mindestens einen SMS-Absender hinzu, damit Sie einen SMS-Fallback senden können, wenn die RCS-Zustellung fehlschlägt.
{% endalert %}

Wenn die Abo-Gruppe beide Protokolle unterstützt, wählen Sie **SMS/MMS** oder **RCS**. Für RCS wählen Sie **Text**, **Media** oder **Card**.

### Schritt 3: Nachricht verfassen {#step-3-compose-your-message}

Die Felder und Begrenzungen im Editor hängen vom gewählten Nachrichtentyp ab.

{% tabs local %}
{% tab SMS und MMS %}

#### Felder und Einstellungen für SMS und MMS {#sms-and-mms-fields-and-settings}

| Feld oder Einstellung | Beschreibung |
| --- | --- |
| **Sprache** | Fügen Sie sprachspezifische Inhalte in die Nachricht ein. |
| **Nachricht** | Geben Sie bis zu 1.600 Zeichen ein, einschließlich Liquid, Connected-Content und Emojis. Der Editor schätzt die Kodierung, die Zeichenanzahl und die Anzahl der abrechenbaren SMS-Segmente. Eine MMS-Nachricht kann Medien ohne Nachrichtentext enthalten. |
| **Medien** | Für eine MMS-fähige Abo-Gruppe fügen Sie ein PNG-, JPEG- oder GIF-Bild aus der Medienbibliothek oder per URL hinzu. Sie können anstelle eines Bildes auch eine vCard hinzufügen. |
| **Link-Verkürzung** | Verkürzt HTTP- und HTTPS-URLs und trackt das Engagement. Für ältere Link-Verkürzung wählen Sie einfaches oder erweitertes Tracking. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Felder und Einstellungen für SMS und MMS" }

SMS-Nachrichten verwenden GSM-7- oder UCS-2-Kodierung und werden pro Nachrichtensegment abgerechnet. Ein einzelnes Zeichen kann die Kodierung ändern und die Anzahl der abrechenbaren Segmente erhöhen. Informationen zu Kodierungsregeln, Segmentgrößen und dem Segment-Rechner finden Sie unter [SMS- und RCS-Abrechnungsrechner]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator).

![SMS-Editor mit Nachrichtentext und der geschätzten Zeichen- und Segmentanzahl.]({% image_buster /assets/img/sms_campaign_compose.png %})

#### MMS-Medienspezifikationen {#mms-media-specifications}

{% multi_lang_include channels/image_specs.md variable_name='sms and mms' %}

Informationen zum Versenden von Geschäftsdaten, die Nutzer:innen in ihren Gerätekontakten speichern können, finden Sie unter [Kontaktkarten]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card). Das Senden einer Kontaktkarte wird als MMS abgerechnet.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

Die Verfügbarkeit und Darstellung von MMS hängen vom empfangenden Mobilfunkanbieter ab. Wenn ein Anbieter keine MMS akzeptieren kann, wird das Medium über den Provider zu einem Link im SMS-Text. Vermeiden Sie den MMS-Versand an Google-Voice-Nummern, da die eingeschränkte MMS-Unterstützung zu unzuverlässiger Zustellung führen kann.

Wenn Nutzer:innen eingehende Medien senden, stellt Braze deren URLs in [Currents-SMS-Eingangs-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events) und über {% raw %}`{{sms.${inbound_media_urls}}}`{% endraw %} in Liquid bereit.

{% endtab %}
{% tab RCS %}

#### RCS-Nachrichtentypen {#rcs-message-types}

| Nachrichtentyp | Felder und Einstellungen | Limits und Verhalten |
| --- | --- | --- |
| **Text** | Pflicht-Nachrichtentext, optionale vorgeschlagene Antworten oder Open-URL-Aktionen, optionaler SMS-Fallback und Link-Verkürzung | Der Nachrichtentext kann je nach SMS-Dienstanbieter bis zu 1.600 oder 3.072 Zeichen enthalten. Fügen Sie bis zu fünf Vorschläge hinzu. |
| **Media** | Erforderliches Bild, Video, Dokument oder Audio; optionaler Nachrichtentext; optionale Vorschläge, SMS-Fallback und Link-Verkürzung | Der Nachrichtentext kann je nach Anbieter bis zu 1.600 oder 3.072 Zeichen enthalten und wird als zusätzliche RCS-Nachricht abgerechnet. Fügen Sie bis zu fünf Vorschläge hinzu. |
| **Card** | Medien-Card oder reine Text-Card, Titel, Beschreibung, Buttons, optionale Vorschläge und optionaler SMS-Fallback | Der Titel kann bis zu 200 Zeichen enthalten. Die Beschreibung kann je nach Anbieter bis zu 1.600 oder 2.000 Zeichen enthalten. Fügen Sie zwischen einem und vier Buttons hinzu. Die Anbieterunterstützung bestimmt, ob reine Text-Cards und Vorschläge außerhalb der Card verfügbar sind. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="RCS-Nachrichtentypen, Felder und Limits" }

Vorschläge können vorgeschlagene Antworten sein, die die Texteingabe der Nutzer:innen vorausfüllen, oder Open-URL-Aktionen. Fügen Sie jedem Vorschlag bis zu 25 Zeichen Text und jeder Open-URL-Aktion eine URL mit bis zu 2.048 Zeichen hinzu.

Aktivieren Sie für jeden RCS-Nachrichtentyp **SMS senden, wenn RCS fehlschlägt**, um eine Fallback-Nachricht mit bis zu 1.600 Zeichen hinzuzufügen. Die ausgewählte Abo-Gruppe muss einen SMS-Absender enthalten. Bei **Card**-Nachrichten sind Links in der Beschreibung nicht klickbar – verwenden Sie stattdessen einen Open-URL-Button.

Einige SMS-Dienstanbieter unterstützen keine eigenständigen **Media**-Nachrichten oder reine Text-Cards. Der Editor zeigt nur die unterstützten RCS-Nachrichtentypen an. Bei **Card**-Nachrichten gilt die Link-Verkürzung nur für Links im SMS-Fallback.

Die Abrechnung von RCS-Nachrichten hängt vom Nachrichtentyp und Inhalt ab. Informationen zu Abrechnungsregeln für einfache, Rich- und Rich-Card-Nachrichten finden Sie unter [RCS-Nachrichtenabrechnung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#rcs-message-billing).

#### RCS-Medienspezifikationen {#rcs-media-specifications}

Der Editor akzeptiert eine Medien-URL mit bis zu 1.000 Zeichen. Verfügbare Formate und maximale Dateigröße hängen vom SMS-Dienstanbieter ab.

| Dateityp | Spezifikationen |
| --- | --- |
| Alle | Maximale Dateigröße ist 16&nbsp;MB oder 100&nbsp;MB, je nach Anbieter. |
| Bild | JPEG, JPG, GIF, PNG |
| Video | H263, M4V, MP4, MPEG, MPEG-4, WEBM |
| Dokument | PDF. Verfügbar für **Media**-Nachrichten, aber nicht für Medien-Cards. |
| Audio | AAC, MP3, MPEG, MP4, 3GPP, OGG. Anbieterunterstützung variiert. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="RCS-Medienspezifikationen" }

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% endtab %}
{% endtabs %}

#### Personalisierung {#personalization}

Verwenden Sie [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), Emojis und sprachspezifische Inhalte, um Ihre Nachricht zu personalisieren. Fügen Sie einen Standardwert für die Liquid-Personalisierung hinzu, damit Profile mit unvollständigen Daten keine leeren Inhalte erhalten.

Um Nachrichtentexte aus einer Eingabeaufforderung zu erstellen, verwenden Sie [Text generieren]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy) mit Operator.

Für Sprachen, die von rechts nach links geschrieben werden, siehe [Nachrichten von rechts nach links erstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

#### Konversationelle Nachrichten-Workflows erstellen (RCS) {#create-conversational-message-workflows-rcs}

Konversationelle Nachrichten-Workflows ermöglichen es Ihnen, dynamisch auf Nutzer:innen zu reagieren und ein interaktives Messaging-Erlebnis zu schaffen. Um einen Workflow zu erstellen, erstellen Sie einen Canvas und kombinieren dann vorgeschlagene Antworten mit [Aktionspfaden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths), um den Workflow basierend auf der vom Nutzer bzw. der Nutzerin gewählten Antwort zu steuern.

1. Erstellen Sie im Canvas-Builder einen RCS-Nachrichtenschritt mit mehreren vorgeschlagenen Antworten.

![RCS-Nachrichten-Editor mit vorgeschlagenen Antworten.]({% image_buster /assets/img/rcs/suggested_replies.png %})

{: start="2"}
2. Verbinden Sie diese Nachricht mit einem Aktionspfad, der für jede vorgeschlagene Antwort eine Aktionsgruppe enthält.
3. Für jede Aktionsgruppe:
   - Wählen Sie den Trigger **Eingehende SMS-Nachricht senden**.
   - Setzen Sie den Nachrichtentext so, dass er mit der entsprechenden vorgeschlagenen Antwort übereinstimmt.

![Aktionspfad-Schritt mit drei Aktionsgruppen, je eine für jede vorgeschlagene Antwort.]({% image_buster /assets/img/rcs/quick_reply.png %})

{: start="4"}
4. Verbinden Sie jede Aktionsgruppe mit einem RCS-Nachrichtenschritt und fügen Sie dann Inhalte basierend auf der zugehörigen vorgeschlagenen Antwort hinzu.
5. Setzen Sie den konversationellen Workflow fort, indem Sie vorgeschlagene Antworten zu Folgenachrichten hinzufügen.
6. Wiederholen Sie die Schritte 2–4, bis der Workflow vollständig ist.

![Canvas mit einem konversationellen Workflow mit zwei Aktionspfaden.]({% image_buster /assets/img/rcs/full_conversational_workflow.png %})

### Schritt 4: Link-Verkürzung konfigurieren {#step-4-configure-link-shortening}

Aktivieren Sie die **Link-Verkürzung**, um HTTP- und HTTPS-URLs zu verkürzen und Klicks für SMS, MMS und unterstützte RCS-Links zu tracken. Wählen Sie je nach Version in Ihrem Workspace einfaches oder erweitertes Tracking oder verwenden Sie die vereinheitlichte Link-Verkürzung.

Erweitertes Tracking fügt Klickdaten auf Nutzer:innenebene für Segmentierung und Retargeting hinzu. Die vereinheitlichte Link-Verkürzung fasst verkürzte SMS- und RCS-Links in einem personalisierten Format zusammen. Informationen zu unterstützten URLs, Liquid-Verhalten, Testanforderungen, angepassten Domains und Retargeting finden Sie unter [Link-Verkürzung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening).

Braze verkürzt bis zu 25 Links in einer Nachricht. Eine URL mit mehr als 4.000 Zeichen kann nicht verkürzt werden und führt dazu, dass die Nachricht beim Senden fehlschlägt.

### Schritt 5: Nachricht in der Vorschau anzeigen und testen {#step-5-preview-and-test-your-message}

Gehen Sie zum Tab **Test**, um die Nachricht als Nutzer:in in der Vorschau anzuzeigen oder eine Test-SMS, -MMS oder -RCS-Nachricht an eine [Inhaltstest-Gruppe]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) oder einzelne:n Nutzer:in zu senden.

{% alert tip %}
Verwenden Sie den [SMS-Segment-Rechner]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator), um abzuschätzen, wie viele Segmente Ihre Nachricht enthält.
{% endalert %}

![Vorschau des SMS-Textes im Tab „Test“ des Editors. Im Profilbereich ist das Feld „Vorname“ auf „James“ gesetzt. Im Vorschaubereich lautet die SMS jetzt: „Hi James, we appreciate your support!“]({% image_buster /assets/img/sms_campaign_test.png %})

Bei MMS bestimmt das empfangende Telefon, ob das Medium vor oder nach dem Nachrichtentext angezeigt wird.

Bei RCS steuern das Betriebssystem, der Gerätehersteller, der Mobilfunkanbieter und die Messaging-App die Darstellung. Testen Sie auf echten Geräten, da die Braze-Vorschau von der empfangenen Nachricht abweichen kann. Weitere Informationen finden Sie unter [Warum wird meine RCS-Nachricht auf iOS-Geräten nicht korrekt dargestellt?]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#why-doesnt-my-rcs-message-render-accurately-on-ios-devices).

Weitere Informationen finden Sie unter [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=sms%2Fmms%20and%20rcs).

### Schritt 6: Restliche Campaign oder restlichen Canvas aufbauen {#step-6-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

#### Zustellungszeitplan oder Trigger wählen {#choose-a-delivery-schedule-or-trigger}

Stellen Sie Nachrichten zu einem geplanten Zeitpunkt oder als Reaktion auf eine Aktion oder einen API-Trigger zu. Informationen zu Zeitplan- und Trigger-Optionen finden Sie unter [Campaign planen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Konfigurieren Sie Zustellungskontrollen wie [Re-Eligibility]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) und [Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping). Legen Sie bei aktionsbasierter Zustellung die Campaign-Dauer und die [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) fest.

#### Zielgruppe zusammenstellen {#choose-users-to-target}

[Stellen Sie Ihre Zielgruppe zusammen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users), indem Sie Segmente und Filter auswählen. Braze berechnet die genaue Segment-Zugehörigkeit vor dem Senden der Nachricht.

Die ausgewählte Abo-Gruppe filtert nach abonnierten Nutzer:innen. SMS- und MMS-Empfänger:innen benötigen außerdem eine gültige Telefonnummer. RCS-Empfänger:innen benötigen ein RCS-fähiges Gerät und eine Mobilfunkanbieterverbindung – verwenden Sie einen SMS-Fallback, um berechtigte Nutzer:innen zu erreichen, wenn die RCS-Zustellung fehlschlägt.

{% multi_lang_include audience/target_audiences.md %}

Informationen zum Klick- und Interaktions-Targeting finden Sie unter [Nutzer:innen-Retargeting]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting).

#### Konversions-Events auswählen {#choose-conversion-events}

Verwenden Sie [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), um Aktionen zu messen, nachdem Nutzer:innen die Campaign erhalten haben. Legen Sie ein Konversionsfenster von bis zu 30 Tagen fest.

{% endtab %}
{% tab Canvas %}

Vervollständigen Sie die verbleibenden Abschnitte Ihres Canvas. Informationen zu Entry-Zeitplänen, Zielgruppeneinstellungen und Sendekontrollen finden Sie unter [Canvas erstellen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas).

{% endtab %}
{% endtabs %}

### Schritt 7: Überprüfen und bereitstellen {#step-7-review-and-deploy}

Nachdem Sie Ihre Campaign oder Ihren Canvas fertiggestellt haben, überprüfen Sie die Details und testen Sie die Nachricht, bevor Sie sie senden.

Verwenden Sie nach dem Start die [SMS-, MMS- und RCS-Berichterstattung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting), um die Performance Ihrer Nachrichten auszuwerten.

## Wissenswertes {#things-to-know}

- SMS wird pro Nachrichtensegment abgerechnet, MMS zu einem eigenen Tarif und RCS pro Nachrichtentyp. Lesen Sie sich die [SMS- und RCS-Abrechnungsrechner]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator) vor dem Versand durch.
- MMS unterstützt ein Bild oder eine vCard. Die Unterstützung durch den Mobilfunkanbieter bestimmt, ob Empfänger:innen Medien oder einen Bild-Link erhalten.
- RCS-Funktionen und -Limits variieren je nach SMS-Dienstanbieter. Der Editor zeigt nur die Optionen an, die für die ausgewählte Abo-Gruppe verfügbar sind.
- Sie können eine voraufgezeichnete Voicemail als Audio in einer RCS-**Medien**-Nachricht senden.
- Darstellung und Interaktionsverhalten variieren je nach Gerät, Mobilfunkanbieter, Betriebssystem und Messaging-App.