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

Bevor Sie beginnen, stellen Sie sicher, dass Sie Folgendes haben:

| Anforderung | Beschreibung |
| --- | --- |
| Sender-Einrichtung | Schließen Sie die [Sender-Einrichtung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup) ab. Um MMS zu senden, benötigt Ihre Abo-Gruppe eine MMS-fähige Telefonnummer. Um RCS zu senden, schließen Sie die [RCS-Einrichtung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup) ab und fügen Sie einen verifizierten RCS-Sender hinzu. |
| Abo-Gruppe | Erstellen Sie eine [Abo-Gruppe]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups), die die Sender für diese Nachricht enthält. |
| Telefonnummern und Einwilligung der Nutzer:innen | Importieren Sie die Telefonnummern der Nutzer:innen und erfassen Sie die entsprechenden [SMS-, MMS- und RCS-Opt-ins]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins). |
| Campaign oder Canvas | Verwenden Sie eine Campaign für eine einzelne zielgerichtete Nachricht oder Canvas für eine mehrstufige User-Journey. |
| Nachrichten- oder Aktionsguthaben | Stellen Sie sicher, dass Ihr Konto über verfügbare Guthaben verfügt. Der Versand von SMS-, MMS- und RCS-Nachrichten über Braze verwendet diese Guthaben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen für SMS-, MMS- und RCS-Nachrichten" }

## Eine Nachricht erstellen {#create-a-message}

### 1. Schritt: Wählen Sie, wo Sie Ihre Nachricht erstellen möchten {#step-1-choose-where-to-build-your-message}

{% tabs %}
{% tab Campaign %}

1. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Campaign erstellen**.
2. Wählen Sie **SMS/MMS/RCS** oder für Campaigns, die mehrere Kanäle ansprechen, **Multichannel Campaign**.
3. Geben Sie Ihrer Campaign einen klaren und aussagekräftigen Namen.
4. Fügen Sie bei Bedarf [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) und [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) hinzu.
  - Tags erleichtern das Auffinden und Verwenden Ihrer Campaigns in Berichten.
5. Fügen Sie Varianten für Ihre Campaign hinzu und benennen Sie diese. Sie können SMS/MMS- und RCS-Varianten in derselben Campaign einbinden. Weitere Informationen finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Wenn Ihre Campaign-Varianten ähnliche Inhalte haben, verfassen Sie zuerst die erste Nachricht, bevor Sie weitere Varianten hinzufügen. Sie können dann **Aus Variante kopieren** im **Variante hinzufügen**-Dropdown auswählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}

{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

### 2. Schritt: Abo-Gruppe und Nachrichtentyp auswählen {#step-2-select-a-subscription-group-and-message-type}

Wählen Sie die **Abo-Gruppe** aus, die den Absender für diese Nachricht enthält. Braze verwendet die ausgewählte Gruppe zur Berechnung der erreichbaren Zielgruppe und zur Ermittlung der Sendezeitberechtigung.

Die von Ihnen ausgewählte Abo-Gruppe bestimmt, welche Nachrichtentypen im Editor verfügbar sind:

| Typ der Abo-Gruppe | Verfügbare Nachrichtentypen |
| --- | --- |
| Nur SMS | SMS |
| SMS mit MMS-fähigen Nummern | SMS und MMS |
| RCS-fähig mit verifiziertem RCS-Absender | RCS und SMS, wenn die Gruppe auch einen SMS-Absender enthält. MMS ist ebenfalls verfügbar, wenn dieser Absender MMS-fähig ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Verfügbare Nachrichtentypen nach Abo-Gruppe" }

{% alert tip %}
Fügen Sie einer RCS-Abo-Gruppe mindestens einen SMS-Absender hinzu, damit Sie einen SMS-Fallback senden können, wenn die RCS-Zustellung fehlschlägt.
{% endalert %}

Wenn die Abo-Gruppe beide Protokolle unterstützt, wählen Sie **SMS/MMS** oder **RCS**. Für RCS wählen Sie **Text**, **Media** oder **Card**.

### 3. Schritt: Nachricht verfassen {#step-3-compose-your-message}

Die Felder und Begrenzungen im Editor hängen vom gewählten Nachrichtentyp ab.

{% tabs local %}
{% tab SMS und MMS %}

#### SMS- und MMS-Felder und -Einstellungen {#sms-and-mms-fields-and-settings}

| Feld oder Einstellung | Beschreibung |
| --- | --- |
| **Sprache** | Sprachspezifische Inhalte in die Nachricht einfügen. |
| **Nachricht** | Geben Sie bis zu 1.600 Zeichen ein, einschließlich Liquid, Connected-Content und Emojis. Der Editor schätzt die Codierung, die Zeichenanzahl und die Anzahl der abrechenbaren SMS-Nachrichtensegmente. Eine MMS-Nachricht kann Medien ohne Nachrichtentext enthalten. |
| **Medien** | Für eine MMS-fähige Abo-Gruppe fügen Sie ein PNG-, JPEG- oder GIF-Bild aus der Medienbibliothek oder per URL hinzu. Sie können anstelle eines Bildes auch eine vCard hinzufügen. |
| **Linkverkürzung** | HTTP- und HTTPS-URLs verkürzen und Engagement tracken. Für die klassische Linkverkürzung wählen Sie Basis- oder erweitertes Tracking. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMS- und MMS-Felder und -Einstellungen" }

SMS-Nachrichten verwenden GSM-7- oder UCS-2-Codierung und werden pro Nachrichtensegment abgerechnet. Ein einzelnes Zeichen kann die Codierung ändern und die Anzahl der abrechenbaren Segmente erhöhen. Informationen zu Codierungsregeln, Segmentgrößen und dem Segment-Rechner finden Sie unter [SMS- und RCS-Abrechnungsrechner]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator).

![SMS-Editor mit Nachrichtentext und den geschätzten Zeichen- und Segmentanzahlen.]({% image_buster /assets/img/sms_campaign_compose.png %})

#### MMS-Medienspezifikationen {#mms-media-specifications}

{% multi_lang_include channels/image_specs.md variable_name='sms and mms' %}

Um Geschäftsdaten zu senden, die Nutzer:innen in ihren Gerätekontakten speichern können, lesen Sie [Kontaktkarten]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card). Das Senden einer Kontaktkarte wird als MMS abgerechnet.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

Die MMS-Verfügbarkeit und -Darstellung hängen vom empfangenden Mobilfunkanbieter ab. Wenn ein Anbieter MMS nicht akzeptieren kann, werden die Medien über den Provider zu einem Link im SMS-Text. Vermeiden Sie das Senden von MMS an Google-Voice-Nummern, da die eingeschränkte MMS-Unterstützung zu unzuverlässiger Zustellung führen kann.

Wenn Nutzer:innen eingehende Medien senden, stellt Braze deren URLs in [Currents-SMS-Eingangs-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events) und über {% raw %}`{{sms.${inbound_media_urls}}}`{% endraw %} in Liquid bereit.

{% endtab %}
{% tab RCS %}

#### RCS-Nachrichtentypen {#rcs-message-types}

| Nachrichtentyp | Felder und Einstellungen | Begrenzungen und Verhalten |
| --- | --- | --- |
| **Text** | Erforderlicher Nachrichtentext, optionale vorgeschlagene Antworten oder Open-URL-Aktionen, optionaler SMS-Fallback und Linkverkürzung | Der Nachrichtentext kann bis zu 1.600 oder 3.072 Zeichen enthalten, abhängig vom SMS-Dienstanbieter. Fügen Sie bis zu fünf Vorschläge hinzu. |
| **Media** | Erforderliches Bild, Video, Dokument oder Audio; optionaler Nachrichtentext; optionale Vorschläge, SMS-Fallback und Linkverkürzung | Der Nachrichtentext kann bis zu 1.600 oder 3.072 Zeichen enthalten, abhängig vom Anbieter, und wird als zusätzliche RCS-Nachricht abgerechnet. Fügen Sie bis zu fünf Vorschläge hinzu. |
| **Card** | Medienkarte oder Nur-Text-Karte, Titel, Beschreibung, Buttons, optionale Vorschläge und optionaler SMS-Fallback | Der Titel kann bis zu 200 Zeichen enthalten. Die Beschreibung kann bis zu 1.600 oder 2.000 Zeichen enthalten, abhängig vom Anbieter. Fügen Sie zwischen einem und vier Buttons hinzu. Die Anbieterunterstützung bestimmt, ob Nur-Text-Karten und Vorschläge außerhalb der Karte verfügbar sind. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="RCS-Nachrichtentypen, Felder und Begrenzungen" }

Vorschläge können vorgeschlagene Antworten sein, die das Texteingabefeld der Nutzer:innen vorab ausfüllen, oder Open-URL-Aktionen. Fügen Sie jedem Vorschlag bis zu 25 Zeichen Text und jeder Open-URL-Aktion eine URL von bis zu 2.048 Zeichen hinzu.

Aktivieren Sie für jeden RCS-Nachrichtentyp **SMS senden, wenn RCS fehlschlägt**, um eine Fallback-Nachricht von bis zu 1.600 Zeichen hinzuzufügen. Die ausgewählte Abo-Gruppe muss einen SMS-Absender enthalten. Bei **Card**-Nachrichten sind Links in der Beschreibung nicht anklickbar; verwenden Sie stattdessen einen Open-URL-Button.

Einige SMS-Dienstanbieter unterstützen keine eigenständigen **Media**-Nachrichten oder Nur-Text-Karten. Der Editor zeigt nur die unterstützten RCS-Nachrichtentypen an. Bei **Card**-Nachrichten gilt die Linkverkürzung nur für Links im SMS-Fallback.

Die Abrechnung von RCS-Nachrichten hängt vom Nachrichtentyp und Inhalt ab. Informationen zu Abrechnungsregeln für Basis-, Rich- und Rich-Card-Nachrichten finden Sie unter [RCS-Nachrichtenabrechnung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#rcs-message-billing).

#### RCS-Medienspezifikationen {#rcs-media-specifications}

Der Editor akzeptiert eine Medien-URL mit bis zu 1.000 Zeichen. Verfügbare Formate und maximale Dateigröße hängen vom SMS-Dienstanbieter ab.

| Dateityp | Spezifikationen |
| --- | --- |
| Alle | Maximale Dateigröße beträgt 16&nbsp;MB oder 100&nbsp;MB, abhängig vom Anbieter. |
| Bild | JPEG, JPG, GIF, PNG |
| Video | H263, M4V, MP4, MPEG, MPEG-4, WEBM |
| Dokument | PDF. Verfügbar für **Media**-Nachrichten, aber nicht für Medienkarten. |
| Audio | AAC, MP3, MPEG, MP4, 3GPP, OGG. Anbieterunterstützung variiert. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="RCS-Medienspezifikationen" }

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% endtab %}
{% endtabs %}

#### Personalisierung {#personalization}

Verwenden Sie [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), Emojis und sprachspezifische Inhalte, um Ihre Nachricht zu personalisieren. Fügen Sie einen Standardwert für die Liquid-Personalisierung hinzu, damit Profile mit unvollständigen Daten keine leeren Inhalte erhalten.

Um Nachrichtentexte aus einem Prompt zu erstellen, verwenden Sie [Text generieren]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy) mit Operator.

Informationen zu Sprachen, die von rechts nach links geschrieben werden, finden Sie unter [Nachrichten von rechts nach links erstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

#### Konversationsbasierte Nachrichten-Workflows erstellen (RCS) {#create-conversational-message-workflows-rcs}

Konversationsbasierte Nachrichten-Workflows ermöglichen es Ihnen, dynamisch auf Nutzer:innen zu reagieren und ein dialogorientiertes Messaging-Erlebnis zu schaffen. Um einen Workflow zu erstellen, erstellen Sie einen Canvas und kombinieren dann vorgeschlagene Antworten mit [Aktionspfaden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths), um Ihren Workflow basierend auf der Antwort der Nutzer:innen zu steuern.

1. Erstellen Sie im Canvas-Builder einen RCS-Nachrichtenschritt mit mehreren vorgeschlagenen Antworten.

![RCS-Nachrichten-Editor mit vorgeschlagenen Antworten.]({% image_buster /assets/img/rcs/suggested_replies.png %})

{: start="2"}
2. Verbinden Sie diese Nachricht mit einem Aktionspfad, der eine Aktionsgruppe für jede vorgeschlagene Antwort enthält.
3. Für jede Aktionsgruppe:
   - Wählen Sie den Trigger **Eingehende SMS-Nachricht senden**.
   - Setzen Sie den Nachrichtentext auf denselben Text wie die entsprechende vorgeschlagene Antwort.

![Aktionspfad-Schritt mit drei Aktionsgruppen konfiguriert, eine für jede vorgeschlagene Antwort.]({% image_buster /assets/img/rcs/quick_reply.png %})

{: start="4"}
4. Verbinden Sie jede Aktionsgruppe mit einem RCS-Nachrichtenschritt und fügen Sie dann Inhalte basierend auf der zugehörigen vorgeschlagenen Antwort hinzu.
5. Setzen Sie den konversationsbasierten Workflow fort, indem Sie vorgeschlagene Antworten zu allen Folgenachrichten hinzufügen.
6. Wiederholen Sie die Schritte 2–4, bis der Workflow abgeschlossen ist.

![Canvas mit einem konversationsbasierten Workflow mit zwei Aktionspfaden.]({% image_buster /assets/img/rcs/full_conversational_workflow.png %})

### 4. Schritt: Linkverkürzung konfigurieren {#step-4-configure-link-shortening}

Aktivieren Sie **Linkverkürzung**, um HTTP- und HTTPS-URLs zu verkürzen und Klicks für SMS-, MMS- und unterstützte RCS-Links zu tracken. Wählen Sie je nach der in Ihrem Workspace verfügbaren Version Basis- oder erweitertes Tracking oder verwenden Sie die einheitliche Linkverkürzung.

Erweitertes Tracking fügt Klickdaten auf Nutzer:innen-Ebene für Segmentierung und Retargeting hinzu. Die einheitliche Linkverkürzung fasst verkürzte SMS- und RCS-Links in einem personalisierten Format zusammen. Informationen zu unterstützten URLs, Liquid-Verhalten, Testanforderungen, angepassten Domains und Retargeting finden Sie unter [Linkverkürzung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening).

Braze verkürzt bis zu 25 Links in einer Nachricht. Eine URL mit mehr als 4.000 Zeichen kann nicht verkürzt werden und führt dazu, dass die Nachricht beim Senden fehlschlägt.

### 5. Schritt: Nachricht in der Vorschau anzeigen und testen {#step-5-preview-and-test-your-message}

Gehen Sie zum Tab **Test**, um die Nachricht als Nutzer:in in der Vorschau anzuzeigen oder eine Test-SMS, -MMS oder -RCS an eine [Content-Testgruppe]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) oder einzelne Nutzer:innen zu senden.

{% alert tip %}
Verwenden Sie den [SMS-Segment-Rechner]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator), um abzuschätzen, wie viele Segmente Ihre Nachricht enthält.
{% endalert %}

![Vorschau des SMS-Textes im Test-Tab des Editors. Im Profilbereich ist das Feld „Vorname“ auf „James“ gesetzt. Im Vorschaubereich lautet die SMS nun: „Hi James, we appreciate your support!“]({% image_buster /assets/img/sms_campaign_test.png %})

Bei MMS bestimmt das empfangende Telefon, ob die Medien vor oder nach dem Nachrichtentext angezeigt werden.

{% alert note %}
Da die RCS-Darstellung vom Betriebssystem, Gerätehersteller, Mobilfunkanbieter und der Messaging-App der Nutzer:innen gesteuert wird (zum Beispiel Google Messages im Vergleich zu Apple Messages), kann das Erscheinungsbild der Nachricht variieren. Die in Braze angezeigte Vorschau stimmt möglicherweise nicht genau mit dem überein, was Endnutzer:innen erhalten. Validieren Sie die endgültige Darstellung nach Möglichkeit auf echten Geräten. Details zur RCS-Darstellung auf iOS-Geräten finden Sie unter [Warum wird meine RCS-Nachricht auf iOS-Geräten nicht korrekt dargestellt?]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#why-doesnt-my-rcs-message-render-accurately-on-ios-devices). Informationen zu GIFs in Rich Cards finden Sie unter [Warum erscheinen GIFs in RCS Rich Cards auf iOS statisch?]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#why-do-gifs-in-rcs-rich-cards-appear-static-on-ios).
{% endalert %}

Weitere Informationen finden Sie unter [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=sms%2Fmms%20and%20rcs).

### 6. Schritt: Den Rest Ihrer Campaign oder Ihres Canvas erstellen {#step-6-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

#### Zustellungszeitplan oder Trigger wählen {#choose-a-delivery-schedule-or-trigger}

Senden Sie Nachrichten zu einem geplanten Zeitpunkt oder als Reaktion auf eine Aktion oder einen API-Trigger. Informationen zu Zeitplan- und Trigger-Optionen finden Sie unter [Campaign planen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Konfigurieren Sie Zustellungskontrollen wie [Wiederzulassung]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) und [Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping). Legen Sie für die aktionsbasierte Zustellung die Campaign-Dauer und [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) fest.

#### Zielgruppe zusammenstellen {#choose-users-to-target}

[Stellen Sie die Zielgruppe zusammen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users), indem Sie Segmente und Filter auswählen. Braze berechnet die genaue Segment-Zugehörigkeit vor dem Senden der Nachricht.

Die ausgewählte Abo-Gruppe filtert nach abonnierten Nutzer:innen. SMS- und MMS-Empfänger:innen benötigen außerdem eine gültige Telefonnummer. RCS-Empfänger:innen benötigen ein RCS-fähiges Gerät und eine Mobilfunkanbieterverbindung; verwenden Sie einen SMS-Fallback, um berechtigte Nutzer:innen zu erreichen, wenn die RCS-Zustellung fehlschlägt.

{% multi_lang_include audience/target_audiences.md %}

Informationen zum Klick- und Interaktions-Targeting finden Sie unter [Nutzer:innen-Retargeting]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting).

#### Konversions-Events wählen {#choose-conversion-events}

Verwenden Sie [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), um Aktionen zu messen, nachdem Nutzer:innen die Campaign erhalten haben. Legen Sie ein Konversionsfenster von bis zu 30 Tagen fest.

{% endtab %}
{% tab Canvas %}

Vervollständigen Sie die verbleibenden Abschnitte Ihres Canvas. Informationen zu Eintrittszeitplänen, Zielgruppen-Einstellungen und Sendekontrollen finden Sie unter [Canvas erstellen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas).

{% endtab %}
{% endtabs %}

### 7. Schritt: Überprüfen und bereitstellen {#step-7-review-and-deploy}

Nachdem Sie Ihre Campaign oder Ihren Canvas fertiggestellt haben, überprüfen Sie die Details und testen Sie die Nachricht, bevor Sie sie senden.

Verwenden Sie nach dem Start die [SMS-, MMS- und RCS-Berichterstattung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting), um die Nachrichten-Performance zu überprüfen.

## Wissenswertes {#things-to-know}

- SMS wird pro Nachrichtensegment abgerechnet, MMS zu einem eigenen Tarif und RCS je nach Nachrichtentyp. Überprüfen Sie die [SMS- und RCS-Abrechnungsrechner]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator), bevor Sie Nachrichten senden.
- MMS unterstützt ein Bild oder eine vCard. Ob Empfänger:innen Medien oder einen Bildlink erhalten, hängt von der Unterstützung durch den Mobilfunkanbieter ab.
- RCS-Funktionen und -Beschränkungen variieren je nach SMS-Dienstanbieter. Der Editor zeigt nur die Optionen an, die für die ausgewählte Abo-Gruppe verfügbar sind.
- Sie können eine aufgezeichnete Voicemail als Audio in einer RCS-**Media**-Nachricht senden.
- Darstellung und Interaktionsverhalten variieren je nach Gerät, Mobilfunkanbieter, Betriebssystem und Messaging-App.