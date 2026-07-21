---
nav_title: Nachricht erstellen
article_title: Eine SMS-, MMS- oder RCS-Nachricht erstellen
page_order: 1
description: "In diesem Artikel erfahren Sie, wie Sie eine SMS-, MMS- oder RCS-Nachricht in Braze erstellen und versenden."
page_type: reference
alias: /create_sms_mms_rcs_message/
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS
search_rank: 1
---

# Eine SMS-, MMS- oder RCS-Nachricht erstellen {#create-an-sms-mms-or-rcs-message}

> SMS-, MMS- und RCS-Kampagnen eignen sich hervorragend, um Ihre Kund:innen direkt zu erreichen und programmatisch mit ihnen zu kommunizieren. Sie können Liquid und andere dynamische Inhalte verwenden, um ein persönliches Erlebnis für Ihre Nutzer:innen zu schaffen und eine Umgebung zu fördern, die ein unaufdringliches Nutzererlebnis mit Ihrer Marke unterstützt und verbessert.

## 1. Schritt: Wählen Sie, wo Sie Ihre Nachricht erstellen möchten {#step-1-choose-where-to-build-your-message}

Sind Sie unsicher, ob Ihre Nachricht über eine Campaign oder ein Canvas gesendet werden soll? Campaigns eignen sich besser für einzelne, gezielte Messaging-Kampagnen, während Canvases besser für mehrstufige User-Journeys geeignet sind.

{% tabs %}
{% tab Campaign %}

1. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Campaign erstellen**.
2. Wählen Sie **SMS/MMS/RCS** oder, für Campaigns, die auf mehrere Kanäle abzielen, **Multichannel**.
3. Geben Sie Ihrer Campaign einen klaren und aussagekräftigen Namen.
4. Fügen Sie nach Bedarf [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) und [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) hinzu.
   * Tags erleichtern das Auffinden Ihrer Campaigns und das Erstellen von Berichten. Wenn Sie beispielsweise den [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder) verwenden, können Sie nach bestimmten Tags filtern.
5. Fügen Sie so viele Varianten hinzu und benennen Sie sie, wie Sie für Ihre Campaign benötigen. Sie können für jede hinzugefügte Variante verschiedene Plattformen, Nachrichtentypen und Layouts wählen. Weitere Informationen zu diesem Thema finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing).
   * Braze ermöglicht es Ihnen, sowohl SMS- als auch RCS-Varianten innerhalb einer einzelnen Campaign einzuschließen, sodass Sie die Performance beider vergleichen können.

{% alert tip %}
Wenn alle Nachrichten in Ihrer Campaign ähnlich sein oder denselben Inhalt haben werden, verfassen Sie Ihre Nachricht, bevor Sie zusätzliche Varianten hinzufügen. Anschließend können Sie im Dropdown **Variante hinzufügen** die Option **Von Variante kopieren** wählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Erstellen Sie Ihr Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) mit dem Canvas-Composer.
2. Nachdem Sie Ihr Canvas eingerichtet haben, fügen Sie im Canvas-Builder einen **SMS/MMS/RCS**-Nachrichtenschritt hinzu.
3. Geben Sie Ihrem Schritt einen klaren und aussagekräftigen Namen.
4. Wählen Sie einen [Schritt-Zeitplan]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types) und legen Sie bei Bedarf eine Verzögerung fest.
5. Filtern Sie Ihre Zielgruppe für diesen Schritt nach Bedarf. Sie können die Empfänger:innen dieses Schritts weiter eingrenzen, indem Sie Segmente angeben und zusätzliche Filter hinzufügen. Die Zielgruppenoptionen werden nach der Verzögerung zum Zeitpunkt des Nachrichtenversands überprüft.
6. Wählen Sie Ihr [Fortschrittsverhalten]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases).
7. Wählen Sie alle weiteren Messaging-Kanäle, die Sie mit Ihrer Nachricht kombinieren möchten.

{% endtab %}
{% endtabs %}

## 2. Schritt: Wählen Sie eine Abo-Gruppe {#step-2-select-a-subscription-group}

Wählen Sie eine [Abo-Gruppe]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups), um sicherzustellen, dass Sie Ihre Nachricht an die richtigen Nutzer:innen senden. Bei der Auswahl einer Abo-Gruppe fügt Braze automatisch einen Segmentierungsfilter hinzu, sodass nur abonnierte Nutzer:innen die Campaign erhalten.

Die von Ihnen gewählte Abo-Gruppe bestimmt, welche Nachrichtentypen im Composer verfügbar sind:

| Abo-Gruppentyp | Verfügbare Nachrichtentypen |
| --- | --- |
| Nur SMS | SMS |
| SMS mit MMS-fähigen Nummern | SMS und MMS |
| RCS-fähig (mit RCS-verifiziertem Sender) | SMS, MMS (falls aktiviert) und RCS |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Abo-Gruppe auswählen" }

{% alert tip %}
Braze empfiehlt dringend, dass jede Abo-Gruppe, die einen RCS-Sender enthält, auch mindestens einen SMS-Code als Fallback umfasst. So wird sichergestellt, dass die Nachricht Ihre Nutzer:innen auch dann per SMS erreicht, wenn eine RCS-Nachricht nicht zugestellt werden kann (z. B. aufgrund von Geräteinkompatibilität oder unvollständiger Carrier-Abdeckung).
{% endalert %}

Nachdem Sie Ihre Abo-Gruppe ausgewählt haben, wählen Sie den Nachrichtentyp, den Sie verfassen möchten. Wenn Ihre Abo-Gruppe mehrere Typen unterstützt, werden Ihnen Optionen zur Auswahl angezeigt.

![Optionen zur Auswahl zwischen einem RCS- oder SMS/MMS-Nachrichtentyp.]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

## 3. Schritt: Verfassen Sie Ihre Nachricht {#step-3-compose-your-message}

Das Verfassen-Erlebnis ändert sich je nach gewähltem Nachrichtentyp. Wählen Sie den Tab für Ihren Nachrichtentyp.

{% tabs local %}
{% tab SMS %}

Verfassen Sie Ihre Nachricht mit Sprachen und Personalisierung (Liquid, Connected-Content und Emojis) nach Bedarf. Achten Sie darauf, unsere Zeichenlimits einzuhalten, um Ihre Chancen auf Zusatzkosten zu reduzieren.

{% alert important %}
Bevor Sie fortfahren, lesen Sie die Richtlinien zu [SMS-Nachrichtensegmenten und Zeichenlimits]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator). SMS-Nachrichtensegmente sind die Zeichenpakete, die Mobilfunkanbieter zur Messung von Textnachrichten verwenden. Nachrichten werden pro Nachrichtensegment abgerechnet, daher ist es sinnvoll, die Feinheiten der Nachrichtenaufteilung zu verstehen.
{% endalert %}

![SMS-Composer in Braze mit der Nachricht „Hi first_name, wir schätzen Ihre Unterstützung! Warum besuchen Sie nicht einen unserer Shops und zeigen diese SMS für einen exklusiven Rabatt? Antworten Sie STOP, um keine Nachrichten mehr von uns zu erhalten.“]({% image_buster /assets/img/sms_campaign_compose.png %})

### Kontaktkarte hinzufügen {#adding-a-contact-card}

Sie können Ihrer SMS-Nachricht eine Kontaktkarte hinzufügen, damit Kund:innen Ihre Geschäfts- und Kontaktinformationen zu ihren Gerätekontakten hinzufügen können. Sie können Eigenschaften wie Unternehmensname, Telefonnummer, Adresse, E-Mail und ein kleines Foto zuweisen. Weitere Details finden Sie unter [Kontaktkarten]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card).

{% endtab %}
{% tab MMS %}

Um eine MMS-Nachricht zu senden, muss Ihre Abo-Gruppe mindestens eine MMS-fähige Telefonnummer enthalten. Dies wird durch ein **MMS**-Tag neben der Abo-Gruppe im Composer angezeigt.

Geben Sie Ihren Nachrichtentext ein und laden Sie dann ein PNG-, JPEG- oder GIF-Bild aus der [Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) hoch oder geben Sie eine Bild-URL an. Pro Nachricht wird nur ein Bild unterstützt.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

![Der Tab „Verfassen“ zum Schreiben einer MMS-Nachricht.]({% image_buster /assets/img/sms/mms_composer.png %}){: style="max-width:80%;"}

### Bildspezifikationen {#image-specifications}

| Eigenschaft | Empfehlung |
| --- | --- |
| Größe | Bis zu 600&nbsp;KB |
| Dateitypen | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Bildspezifikationen" }

### Kontaktkarten {#contact-cards}

Sie können auch eine [Kontaktkarte]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card) (vCard) anstelle eines Bildes einfügen.

### Carrier-Verhalten {#carrier-behavior}

MMS-Nachrichten werden zu einem anderen Tarif als reine SMS-Textnachrichten abgerechnet. Nicht alle Carrier können MMS empfangen. In diesen Fällen wird die MMS automatisch in einen Bildlink umgewandelt, den die Nutzer:innen auswählen können.

{% alert note %}
Vermeiden Sie das Senden von MMS an Google-Voice-Nummern. Google Voice bietet nur eingeschränkte MMS-Unterstützung, was zu unzuverlässiger Nachrichtenzustellung führt.
{% endalert %}

### Eingehende MMS und Personalisierung {#inbound-mms-and-personalization}

Wenn Kund:innen eine eingehende Nachricht mit Medien senden, stellt Braze die Medien in [Currents-SMS-Eingangs-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events) und in Liquid als {% raw %}`{{sms.${inbound_media_urls}}}`{% endraw %} bereit (z. B. in Retargeting- oder Folgenachrichten). Weitere Informationen zur Verwendung eingehender SMS-Eigenschaften in Canvas finden Sie unter [Nachrichtenschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step).

{% endtab %}
{% tab RCS %}

Sehen Sie sich diese kurze Anleitung an, um zu erfahren, wie Sie eine RCS-Text- oder Mediennachricht erstellen.

{% multi_lang_include video.html id="3y0iiqqygw" source="wistia" %}

Wählen Sie zwischen einem **Text**- oder **Medien**-Nachrichtentyp.

![Optionen zur Auswahl zwischen einem Text- oder Medien-Nachrichtentyp.]({% image_buster /assets/img/rcs/rcs_text_media.png %}){: style="max-width:65%;"}

{% subtabs %}
{% subtab Text %}

RCS-Textnachrichten konzentrieren sich auf Text als Medium. Wenn Ihre Nachricht bis zu 160 Zeichen ohne Rich-Elemente umfasst, wird sie als einfache RCS-Nachricht abgerechnet. Wenn Sie 160 Zeichen überschreiten oder ein Rich-Element verwenden, wird sie als Rich-RCS-Nachricht (einzeln) mit einem Zeichenlimit von 3.072 abgerechnet.

**Features:**

- Alle SMS-Features sind enthalten, mit erweitertem Tracking für URL-Klick-Tracking.
- **Vorgeschlagene Antworten**: Buttons mit vorgeschlagenen Antworten, die Nutzer:innen auswählen können, um sie in ihr Texteingabefeld zu übernehmen.
- **Vorgeschlagene Aktionen**: Buttons, die eine Aktion auf dem Gerät der Nutzer:innen auslösen. Braze unterstützt derzeit OpenURL-vorgeschlagene Aktionen, die Nutzer:innen zu einer Webseite oder einem anderen URL-identifizierten Ort weiterleiten.

![Drei vorgeschlagene Aktionen für eine RCS-Nachricht, die trendige Modestile bewirbt.]({% image_buster /assets/img/rcs/rcs_suggested_actions.gif %}){: style="max-width:70%;"}

**Hinweise:**

- Android und iOS können unterschiedlich kürzen: Android zeigt den vollständigen Rich-Nachrichtentext an, während iOS nach der dritten Zeile kürzt.
- Sie können bis zu fünf Buttons pro Nachricht hinzufügen. Diese können entweder vorgeschlagene Aktionen oder vorgeschlagene Antworten sein.
- Längere Textblöcke und viele Buttons können Empfänger:innen überfordern; bevorzugen Sie Einfachheit, wenn möglich.
- In einigen Fällen kann es kostengünstiger sein, längere reine Textnachrichten über RCS statt per SMS zu senden, da längere SMS-Nachrichten in mehrere abrechnungsfähige Segmente aufgeteilt werden, während RCS-Nachrichten pro Nachricht abgerechnet werden.

{% endsubtab %}
{% subtab Medien %}

RCS-Mediennachrichten ermöglichen es Ihnen, ansprechende Medienformate zu verwenden, die mit SMS nicht möglich sind, einschließlich Bild-, Video- und Dokumentdateien.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

**Features:**

- Unterstützt alles, was in Textnachrichtentypen verfügbar ist, einschließlich Text, vorgeschlagene Antworten und vorgeschlagene Aktionen.
- Bilddateien (JPEG, PNG), die aus der [Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) hochgeladen werden.
- Videodateien (MP4, MPEG, MV4), die per URL im Nachrichten-Composer hinzugefügt werden.
- Dokumentdateien (PDF), die per URL im Nachrichten-Composer hinzugefügt werden.

![RCS-Composer mit einer Option zum Hochladen einer Mediendatei.]({% image_buster /assets/img/rcs/rcs_media_type.png %})

**Dateispezifikationen:**

| Dateityp | Spezifikationen |
| --- | --- |
| Alle | Dateigröße begrenzt auf 100 MB. Datei-URL kann bis zu 2.048 Zeichen haben. |
| Bild | Unterstützte Formate: JPG, JPEG, GIF |
| Video | Unterstützte Formate: H263, M4V, MP4, MPEG-4, MPEG, WEBM |
| Dokument | Unterstütztes Format: PDF |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Dateispezifikationen" }

**Hinweise:**

Das Nutzererlebnis beim Empfang von RCS-Nachrichten kann je nach Carrier-Abdeckung, Mobilgerät-Hardware und Betriebssystem variieren. RCS integriert sich natürlicher in Android-Geräte, und verschiedene Geräte können das Erlebnis mit unterschiedlicher Geschwindigkeit und Qualität darstellen.

{% endsubtab %}
{% endsubtabs %}

Verfassen Sie Ihre Nachricht mit Sprachen und Personalisierung ([Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) und Emojis) nach Bedarf. Achten Sie darauf, die Zeichenlimits einzuhalten, um Ihre Chancen auf Zusatzkosten zu reduzieren.

{% alert important %}
Bevor Sie fortfahren, lesen Sie die oben genannten [Richtlinien für RCS-Nachrichtentypen](#step-3-compose-your-message). RCS-Nachrichten werden [pro Nachricht abgerechnet]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator), daher ist es sinnvoll zu verstehen, was in jedem Typ enthalten sein kann.
{% endalert %}

{% endtab %}
{% endtabs %}

### Tipps {#tips}

#### Liquid verwenden {#using-liquid}

{% raw %}
Wenn Sie Liquid verwenden möchten, stellen Sie sicher, dass Sie einen Standardwert für Ihre gewählte Personalisierung angeben, damit im Falle eines unvollständigen Nutzerprofils kein leerer Platzhalter `Hi, !` anstelle des Namens oder eines zusammenhängenden Satzes angezeigt wird.
{% endraw %}

#### KI-generierten Text erstellen {#generating-ai-copy}

Probieren Sie den [KI-Textassistenten]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy) aus. Geben Sie einen Produktnamen oder eine Beschreibung ein, und die KI generiert menschenähnlichen Marketingtext zur Verwendung in Ihrem Messaging.

![Button „KI-Textassistent starten“ im Nachrichtenfeld des SMS-Composers.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_sms.png %}){: style="max-width:60%"}

#### Rechts-nach-links-Nachrichten erstellen {#creating-right-to-left-messages}

Das endgültige Erscheinungsbild von Rechts-nach-links-Nachrichten hängt weitgehend davon ab, wie Dienstanbieter sie darstellen. Best Practices zum Erstellen von Rechts-nach-links-Nachrichten, die so genau wie möglich angezeigt werden, finden Sie unter [Rechts-nach-links-Nachrichten erstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

#### Konversationelle Nachrichten-Workflows erstellen (RCS) {#create-conversational-message-workflows-rcs}

Konversationelle Nachrichten-Workflows ermöglichen es Ihnen, dynamisch auf Nutzer:innen zu reagieren und ein Hin-und-Her-Messaging-Erlebnis zu schaffen. Um einen Workflow zu erstellen, erstellen Sie ein Canvas und kombinieren Sie dann vorgeschlagene Antworten mit [Aktionspfaden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths), um Ihren Workflow basierend auf der Antwort der Nutzer:innen zu steuern.

1. Erstellen Sie im Canvas-Builder einen RCS-Nachrichtenschritt mit mehreren vorgeschlagenen Antworten.

![RCS-Nachrichten-Composer mit vorgeschlagenen Antworten.]({% image_buster /assets/img/rcs/suggested_replies.png %})

{: start="2"}
2. Verbinden Sie diese Nachricht mit einem Aktionspfad mit einer Aktionsgruppe für jede vorgeschlagene Antwort.
3. Für jede Aktionsgruppe:
   - Wählen Sie den Trigger **Eingehende SMS-Nachricht senden**.
   - Setzen Sie den Nachrichtentext auf denselben Text wie die entsprechende vorgeschlagene Antwort.

![Aktionspfad-Schritt mit drei Aktionsgruppen konfiguriert, eine für jede vorgeschlagene Antwort.]({% image_buster /assets/img/rcs/quick_reply.png %})

{: start="4"}
4. Verbinden Sie jede Aktionsgruppe mit einem RCS-Nachrichtenschritt und fügen Sie dann Inhalt basierend auf der zugehörigen vorgeschlagenen Antwort hinzu.
5. Setzen Sie den konversationellen Workflow fort, indem Sie vorgeschlagene Antworten zu allen Folgenachrichten hinzufügen.
6. Wiederholen Sie die Schritte 2–4, bis der Workflow vollständig ist.

![Canvas mit einem konversationellen Workflow mit zwei Aktionspfaden.]({% image_buster /assets/img/rcs/full_conversational_workflow.png %})

## 4. Schritt: Vorschau und Test Ihrer Nachricht {#step-4-preview-and-test-your-message}

Braze empfiehlt immer, Ihre Nachricht vor dem Versand in der Vorschau anzuzeigen und zu testen. Wechseln Sie zum Tab **Test**, um eine Test-SMS, -MMS oder -RCS-Nachricht an [Inhalts-Testgruppen]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) oder einzelne Nutzer:innen zu senden, oder zeigen Sie die Nachricht als Nutzer:in direkt in Braze in der Vorschau an.

{% alert tip %}
Wenn Sie testen möchten, in wie viele Segmente Ihre SMS aufgeteilt werden könnte, testen Sie Ihre Textlänge mit dem [SMS-Segment-Rechner]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator).
{% endalert %}

![Vorschau des SMS-Textes im Tab „Test“ des Composers. Im Profilbereich ist das Feld „Vorname“ auf „James“ gesetzt. Im Vorschaubereich lautet die SMS jetzt „Hi James, wir schätzen Ihre Unterstützung!“]({% image_buster /assets/img/sms_campaign_test.png %})

{% alert note %}
Bei MMS kann die Reihenfolge der Assets (Bild und Nachrichtentext) nicht angepasst werden. Die Reihenfolge hängt vom empfangenden Telefon ab.
{% endalert %}

{% alert note %}
Da das RCS-Rendering vom Betriebssystem, Gerätehersteller, Carrier und der Messaging-App der Nutzer:innen gesteuert wird (z. B. Google Messages vs. Apple Messages), kann das Erscheinungsbild der Nachricht variieren. Die in Braze angezeigte Vorschau stimmt möglicherweise nicht genau mit dem überein, was Endnutzer:innen erhalten. Validieren Sie das endgültige Rendering nach Möglichkeit auf echten Geräten. Weitere Informationen zum RCS-Rendering auf iOS-Geräten finden Sie unter [Warum wird meine RCS-Nachricht auf iOS-Geräten nicht korrekt dargestellt?]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#why-doesnt-my-rcs-message-render-accurately-on-ios-devices).
{% endalert %}

Weitere Informationen finden Sie unter [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=sms%2Fmms%20and%20rcs).

## 5. Schritt: Erstellen Sie den Rest Ihrer Campaign oder Ihres Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Erstellen Sie als Nächstes den Rest Ihrer Campaign. In den folgenden Abschnitten finden Sie weitere Details zur optimalen Nutzung unserer Tools zum Erstellen Ihrer Nachricht.

### Zustellungszeitplan oder Trigger wählen {#choose-delivery-schedule-or-trigger}

Nachrichten können basierend auf einem geplanten Zeitpunkt, einer Aktion oder einem API-Trigger zugestellt werden. Weitere Informationen finden Sie unter [Ihre Campaign planen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Für aktionsbasierte Zustellung können Sie auch die Dauer der Campaign und [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) festlegen.

In diesem Schritt können Sie auch Zustellungskontrollen festlegen, z. B. ob Nutzer:innen [erneut berechtigt]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) werden können, die Campaign zu erhalten, oder ob [Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping)-Regeln aktiviert werden sollen.

### Zielgruppe zusammenstellen {#choose-users-to-target}

Als Nächstes [stellen Sie Ihre Zielgruppe zusammen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users), indem Sie Segmente oder Filter auswählen, um Ihre Zielgruppe einzugrenzen. Sie sollten bereits die Abo-Gruppe gewählt haben, die Nutzer:innen nach dem Grad oder der Kategorie der Kommunikation eingrenzt, die sie mit Ihnen wünschen.

{% multi_lang_include audience/target_audiences.md %}

Wählen Sie die größere Zielgruppe aus Ihren Segmenten und grenzen Sie dieses Segment mit optionalen Filtern weiter ein. Sie erhalten automatisch eine Vorschau der ungefähren Segmentpopulation. Beachten Sie, dass die genaue Segmentzugehörigkeit immer vor dem Versand der Nachricht berechnet wird.

{% alert tip %}
Interessiert an Retargeting? Weitere Informationen finden Sie unter [Nutzer-Retargeting]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting).
{% endalert %}

### Konversions-Events wählen {#choose-conversion-events}

Braze ermöglicht es Ihnen zu verfolgen, wie oft Nutzer:innen bestimmte Aktionen, [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), nach Erhalt einer Campaign ausführen. Sie haben die Möglichkeit, ein Zeitfenster von bis zu 30 Tagen festzulegen, in dem eine Konversion gezählt wird, wenn die Nutzer:innen die angegebene Aktion ausführen.

Konversions-Events helfen Ihnen, den Erfolg Ihrer Campaign zu messen. Zum Beispiel:

- Wenn Sie Geotargeting verwenden, um eine Nachricht auszulösen, deren Endziel ein Kauf ist, setzen Sie das Konversions-Event auf `Purchase`.
- Wenn Sie versuchen, Nutzer:innen in Ihre App zu bringen, setzen Sie das Konversions-Event auf `Starts Session`.

Sie können auch angepasste Konversions-Events basierend auf Ihrem spezifischen Anwendungsfall festlegen.

{% endtab %}
{% tab Canvas %}

Falls noch nicht geschehen, vervollständigen Sie die verbleibenden Abschnitte Ihrer Canvas-Komponente. Weitere Details zum Aufbau des restlichen Canvas, zur Implementierung von multivariaten Tests und intelligenter Auswahl und mehr finden Sie im Schritt [Canvas erstellen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas) unserer Canvas-Dokumentation.

{% endtab %}
{% endtabs %}

## 6. Schritt: Überprüfen und bereitstellen {#step-6-review-and-deploy}

Nachdem Sie den letzten Teil Ihrer Campaign oder Ihres Canvas fertiggestellt haben, überprüfen Sie die Details, testen Sie sie und senden Sie sie ab!

Lesen Sie als Nächstes [SMS-, MMS- und RCS-Reporting]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting), um zu erfahren, wie Sie auf die Ergebnisse Ihrer Campaigns zugreifen können.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Kann ich vorab aufgezeichnete Sprachnachrichten mit RCS senden? {#can-i-send-pre-recorded-voicemails-with-rcs}

Ja, Sie können Mediennachrichten verwenden, um Audio-Dateien zu unterstützen.