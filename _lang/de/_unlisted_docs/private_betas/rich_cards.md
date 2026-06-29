---
nav_title: "RCS-Nachricht erstellen"
article_title: "RCS-Nachricht erstellen"
permalink: /create_rcs_message/
description: "Dieser Artikel beschreibt, wie Sie eine RCS-Nachricht erstellen."
hidden: true
---

# RCS-Nachricht erstellen {#creating-an-rcs-message}

> RCS-Campaigns eignen sich hervorragend, um Ihre Kund:innen direkt zu erreichen und programmatisch mit ihnen zu kommunizieren. Sie können Liquid und andere dynamische Inhalte verwenden, um ein persönliches Erlebnis für Ihre Nutzer:innen zu schaffen und eine Umgebung zu fördern, die ein unaufdringliches Nutzererlebnis mit Ihrer Marke unterstützt und verbessert.

## RCS-Nachricht erstellen

### 1. Schritt: Wählen Sie, wo Sie Ihre Nachricht erstellen möchten {#step-1-choose-where-to-build-your-message}

Sind Sie unsicher, ob Ihre Nachricht über eine Campaign oder ein Canvas gesendet werden soll? Campaigns eignen sich besser für einzelne, einfache Messaging-Kampagnen, während Canvases besser für mehrstufige Nutzer-Journeys geeignet sind.

{% tabs %}
{% tab Campaign %}
1. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Kampagne erstellen**.
2. Wählen Sie **SMS/MMS/RCS** oder, für Campaigns, die auf mehrere Kanäle abzielen, **Multichannel**.
3. Geben Sie Ihrer Campaign einen klaren und aussagekräftigen Namen.
4. Fügen Sie nach Bedarf [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) und [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) hinzu.
   * Tags erleichtern das Auffinden Ihrer Campaigns und das Erstellen von Berichten. Wenn Sie beispielsweise den [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) verwenden, können Sie nach bestimmten Tags filtern.

{: start="5"}
5. Fügen Sie so viele Varianten hinzu und benennen Sie sie, wie Sie für Ihre Campaign benötigen. Sie können für jede hinzugefügte Variante verschiedene Plattformen, Nachrichtentypen und Layouts wählen. Weitere Informationen zu diesem Thema finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
- **SMS- und RCS-Variantentests**: Braze ermöglicht es Ihnen, sowohl SMS- als auch RCS-Varianten in einer einzigen Campaign einzuschließen, sodass Sie die Performance beider vergleichen können. Sie können SMS- und RCS-Varianten im ersten Schritt der Nachrichtenkomposition hinzufügen.

{: start="6"}
6. Wählen Sie eine RCS-fähige [Abo-Gruppe]({{site.baseurl}}/sms_rcs_subscription_groups/). Bei der Auswahl einer Abo-Gruppe fügt Braze automatisch einen Segmentierungsfilter hinzu, der sicherstellt, dass nur abonnierte Nutzer:innen die Campaign erhalten. Nur Langcodes und Shortcodes, die zu dieser Abo-Gruppe gehören, werden zum Senden von SMS an Zielnutzer:innen verwendet.
- **SMS-Fallback**: Braze empfiehlt dringend, dass jede Abo-Gruppe, die einen RCS-Sender enthält, auch mindestens einen SMS-Code als Fallback enthält. Dies ist wichtig für die Zustellbarkeit in Fällen, in denen RCS-Nachrichten nicht zugestellt werden können. Gründe dafür können unter anderem Inkompatibilität des Nutzergeräts und unvollständige Carrier-Abdeckung in einem bestimmten Land oder einer Region sein. Durch die Aktivierung des SMS-Fallbacks wird Ihre Nachricht dennoch an Ihre Nutzer:innen zugestellt, sodass Sie nie die Gelegenheit verpassen, mit ihnen in Kontakt zu treten.

{: start="7"}
7. Wählen Sie zwischen SMS und RCS. Bevor Sie RCS-Nachrichten verfassen, wählen Sie den Kanal, über den Sie senden möchten. Wir empfehlen generell, RCS wo immer möglich zu verwenden, da es erhebliche Vorteile beim Nutzer-Engagement gegenüber SMS bietet. Wir bieten jedoch immer die Option, per SMS zu senden, damit Sie maximale Flexibilität und Kontrolle haben.

![Optionen zur Auswahl eines RCS- oder SMS/MMS-Nachrichtentyps.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% alert tip %}
Wenn alle Nachrichten in Ihrer Campaign ähnlich sein oder denselben Inhalt haben werden, verfassen Sie Ihre Nachricht, bevor Sie zusätzliche Varianten hinzufügen. Sie können dann **Aus Variante kopieren** aus dem Dropdown **Variante hinzufügen** wählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Erstellen Sie Ihr Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) mit dem Canvas-Composer.
2. Nachdem Sie Ihr Canvas eingerichtet haben, fügen Sie einen **SMS/MMS/RCS**-Nachrichtenschritt im Canvas-Builder hinzu.
3. Geben Sie Ihrem Schritt einen klaren und aussagekräftigen Namen.
4. Wählen Sie eine RCS-fähige [Abo-Gruppe]({{site.baseurl}}/sms_rcs_subscription_groups/). Bei der Auswahl einer Abo-Gruppe fügt Braze automatisch einen Segmentierungsfilter hinzu, der sicherstellt, dass nur abonnierte Nutzer:innen die Campaign erhalten. Nur Langcodes und Shortcodes, die zu dieser Abo-Gruppe gehören, werden zum Targeting von Nutzer:innen verwendet.
- **SMS-Fallback**: Braze empfiehlt dringend, dass jede Abo-Gruppe, die einen RCS-Sender enthält, auch mindestens einen SMS-Code als Fallback enthält. Dies ist wichtig für die Zustellbarkeit in Fällen, in denen RCS-Nachrichten nicht zugestellt werden können. Gründe dafür können unter anderem Inkompatibilität des Nutzergeräts und unvollständige Carrier-Abdeckung in einem bestimmten Land oder einer Region sein. Durch die Aktivierung des SMS-Fallbacks wird Ihre Nachricht dennoch an Ihre Nutzer:innen zugestellt, sodass Sie nie die Gelegenheit verpassen, mit ihnen in Kontakt zu treten.

{: start="5"}
5. Wählen Sie zwischen SMS und RCS. Bevor Sie RCS-Nachrichten verfassen, wählen Sie den Kanal, über den Sie senden möchten. Wir empfehlen generell, RCS wo immer möglich zu verwenden, da es erhebliche Vorteile beim Nutzer-Engagement gegenüber SMS bietet. Wir bieten jedoch immer die Option, per SMS zu senden, damit Sie maximale Flexibilität und Kontrolle haben.

![Optionen zur Auswahl eines RCS- oder SMS/MMS-Nachrichtentyps.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% endtab %}
{% endtabs %}

### 2. Schritt: Wählen Sie Ihren RCS-Nachrichtentyp {#step-2-select-your-rcs-message-type}

Wählen Sie während der Campaign- und Canvas-Erstellung aus drei RCS-Nachrichtentypen (Text, Media, Rich Card), um Nachrichten zu konfigurieren, die am besten zu Ihren Zielen passen.

![Optionen zur Auswahl eines Text-, Media- oder Card-Nachrichtentyps.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_text_media.png %}){: style="max-width:65%;"}

{% tabs local %}
{% tab Text %}
Wie der Name schon sagt, konzentrieren sich RCS-Textnachrichten auf Text als Medium. Wenn Sie bis zu 160 Zeichen eingeben, wird die RCS-Nachricht als reine Textnachricht (oder „Basic“-Nachricht) abgerechnet. Wenn Sie 160 Zeichen überschreiten oder ein Rich-Element verwenden, wird die Nachricht als Rich-Nachricht (oder „Single“-RCS-Nachricht) abgerechnet (und das Zeichenlimit erhöht sich auf 3072 Zeichen).

#### Features

- Text-Nachrichtentypen umfassen alle SMS-Features. Nur Advanced Tracking ist für URL-Klick-Tracking möglich, um Ihnen eine Berichtsgranularität auf Nutzerebene zu bieten.
- Darüber hinaus haben Sie jetzt die Möglichkeit, ansprechende **Suggested Replies**- und **Suggested Actions**-Buttons einzubinden, die Nutzeraktionen mit hohem Engagement fördern, wie z. B. den Besuch einer Landing-Page oder das Aufgeben einer Bestellung.
    - **Suggested Replies** sind Buttons mit vorgeschlagenen Antworten, die Nutzer:innen anklicken können, um sie in ihrer Texteingabe vorzufüllen. So wird die Hürde beseitigt, sich eine Antwort ausdenken zu müssen, indem eine begrenzte Auswahl an Optionen bereitgestellt wird.
    - **Suggested Actions** sind Buttons, die eine Aktion auf dem Gerät der Nutzer:innen auslösen. Sie bestehen typischerweise aus ein bis zwei beschreibenden Wörtern und einem visuellen Symbol, das den Nutzer:innen hilft zu verstehen, was der Button bewirkt. Braze unterstützt derzeit OpenURL Suggested Actions. Diese funktionieren ähnlich wie eine URL, bei der Nutzer:innen, die den Button auswählen, zu einer Webseite oder einem anderen URL-identifizierten Ort weitergeleitet werden.

![Ein GIF mit drei Suggested Actions für eine RCS-Nachricht, die trendige Modestile bewirbt: „Fairytale royalty“, „Edgy academia“ und „Show me your other styles“.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_suggested_actions.gif %}){: style="max-width:70%;"}

#### Hinweise {#considerations}

- Für Zeichenlimits bei Text können Sie bis zu 160 Zeichen für eine reine Text-RCS-Nachricht (Basic) oder bis zu 3072 Zeichen für eine Rich-RCS-Nachricht (Single) schreiben.
- Für Button-Limits können Sie bis zu fünf Buttons pro Nachricht hinzufügen. Diese Buttons können entweder Suggested Actions oder Suggested Replies sein.
- Längere Textblöcke und zu viele Buttons können Nutzer:innen frustrieren, daher empfehlen wir, wo immer möglich, auf Einfachheit zu setzen.
- In einigen Fällen kann es kosteneffizienter sein, längere reine Textnachrichten über RCS statt per SMS zu senden. Das liegt daran, dass längere SMS-Nachrichten in mehrere Segmente aufgeteilt werden, von denen jedes einzeln abgerechnet wird, während RCS-Nachrichten pro Nachricht abgerechnet werden. Kontaktieren Sie Ihren Braze Account Manager für weitere Details und Beratung.
{% endtab %}

{% tab Media %}
RCS-Media-Nachrichten ermöglichen es Ihnen, ansprechende Medienformate zu verwenden, die mit SMS nicht möglich sind. Dazu gehören Bild-, Video- und Dokumentdateien. Diese Medienoptionen helfen Ihnen, Ihre Zielgruppe noch intensiver anzusprechen und völlig neue Anwendungsfälle zu ermöglichen. Derzeit wird nur der Bild-Upload über die [Medienbibliothek]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) unterstützt.

#### Features

- Media-Nachrichtentypen unterstützen alles, was in Text-Nachrichtentypen verfügbar ist, einschließlich Text, Suggested Replies und Suggested Actions.
- Unterstützt Bilddateien, einschließlich JPEG- und PNG-Dateiformate. Bilddateien sind über den Upload aus der Medienbibliothek verfügbar.
- Unterstützt Videodateien, einschließlich MP4-, MPEG- und MV4-Dateiformate. Videodateien können per URL direkt im Nachrichten-Editor hinzugefügt werden.
- Unterstützt Dokumentdateien im PDF-Format. Dokumentdateien können über die URL direkt im Nachrichten-Editor hinzugefügt werden.

![RCS-Composer mit einer Option zum Hochladen einer Mediendatei.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_media_type.png %})

#### Dateispezifikationen {#file-specifications}

| Dateityp | Spezifikationen |
| --- | --- |
| Alle | - Dateigröße ist auf 100 MB begrenzt <br><br>- Datei-URL kann bis zu 2048 Zeichen haben |
| Bilddateien | Unterstützte Dateiformate sind JPG, JPEG und GIF |
| Videodateien | Unterstützte Dateiformate sind H263, M4V, MP4, MPEG-4, MPEG, WEBM |
| Dokumentdateien | Unterstütztes Dateiformat: PDF |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Hinweise

Das Nutzererlebnis beim Empfang von RCS-Nachrichten kann je nach einer Reihe von Faktoren leicht variieren, darunter Carrier-Abdeckung im Zielland, Mobilgerät-Hardware und Betriebssystem des Mobilgeräts.

Generell integriert sich RCS natürlicher in Android-Geräte (diese Methode wurde größtenteils von Google implementiert, und Peer-to-Peer-RCS-Messaging ist in der Android-Community weit verbreitet). Verschiedene Geräte können das Erlebnis mit unterschiedlicher Geschwindigkeit und Qualität darstellen.
{% endtab %}

{% tab Rich Card %}

{% alert important %}
Rich Cards befinden sich im Early Access. Kontaktieren Sie Ihren Braze Customer-Success-Manager, wenn Sie an der Teilnahme an diesem Early Access interessiert sind.
{% endalert %}

Eine Rich Card kombiniert Media, Text und Buttons in einer einzigen Nachricht und schafft so ein intuitiveres und ansprechenderes Erlebnis für Ihre Kund:innen. Sie können zwei Untertypen von Rich Cards erstellen: Text und Media.

{% subtabs %}
{% subtab Text %}
Eine Text-Rich-Card ist eine kompakte Nachricht mit Fokus auf Text. Sie muss die folgenden Elemente enthalten:

- **Titel:** Bis zu 200 Zeichen. Kann mit Liquid personalisiert werden.
- **Beschreibung:** Bis zu 2.000 Zeichen. Kann mit Liquid personalisiert werden.
- **Buttons:** Mindestens ein Button ist erforderlich. Sie können bis zu vier Buttons mit **Suggested Reply**- oder **Open web URL**-Aktionen hinzufügen.

{% endsubtab %}
{% subtab Media %}

Eine Media-Rich-Card ist eine visuelle Nachricht mit einem Bild oder Video. Sie muss die folgenden Elemente enthalten:

- **Media:** Ein Bild, GIF oder Video.
    - Benutzerdefinierte Video-Thumbnails werden im Early Access nicht unterstützt. Der Early Access unterstützt nur ein vertikales Layout mit großer Medienhöhe für sowohl Bild- als auch Videodateien.
- **Buttons:** Mindestens ein Button ist erforderlich. Sie können bis zu vier Buttons mit **Suggested Reply**- oder **Open web URL**-Aktionen hinzufügen.

{% endsubtab %}
{% endsubtabs %}

### Features
- **Card-Buttons** und **Suggestions:** Sie können bis zu vier Buttons und fünf Suggestions (jeweils bis zu 25 Zeichen) am unteren Rand der Rich Card (Buttons) oder am unteren Rand des Nachrichtenbildschirms (Suggestions) hinzufügen. Nutzer:innen können diese Klick-/Tipp-Optionen auswählen, um eine bestimmte Antwort zu senden oder eine bestimmte Aktion auszuführen.
- **Personalisierung:** Sie können Liquid verwenden, um alle Rich-Card-Elemente zu personalisieren, einschließlich Titel, Beschreibung, Media und Buttons.
- **Abrechnung:** Rich Cards werden als einzelne Rich-RCS-Nachricht (oder „Single“-RCS-Nachricht) abgerechnet.
- **URL-Hinweis:** URLs, die als Klartext im Titel oder in der Beschreibung eingegeben werden, sind nicht klickbar. Sie müssen einen **OpenURL-Button** verwenden, um Nutzer:innen auf eine Website zu leiten.

![Panel mit Optionen zur Auswahl einer Media- oder Text-Rich-Card.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_media_text.png %}){: style="max-width:65%;"}

{% endtab %}
{% endtabs %}

### 3. Schritt: Verfassen Sie Ihre RCS-Nachricht {#step-3-compose-your-rcs-message}

Schreiben Sie Ihre Nachricht unter Verwendung von Sprachen und Personalisierung ([Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) und Emojis) nach Bedarf. Achten Sie darauf, unsere Limits für Nachrichtentexte einzuhalten, um das Risiko von Zusatzkosten zu reduzieren.

{% alert important %}
Bevor Sie fortfahren, lesen Sie unsere [Richtlinien für RCS-Nachrichtenlimits](#step-2-select-your-rcs-message-type). RCS-Nachrichten werden [pro Nachricht abgerechnet]({{site.baseurl}}/sms_rcs_billing_calculators/), daher ist es sinnvoll, die Nuancen zu verstehen, was in jedem RCS-Nachrichtentyp enthalten sein kann.
{% endalert %}

### 4. Schritt: Vorschau und Test Ihrer Nachricht {#step-4-preview-and-test-your-message}

Braze empfiehlt immer, Ihre Nachricht vor dem Senden in der Vorschau anzuzeigen und zu testen. Gehen Sie zum Tab **Test**, um eine Test-RCS an Content-Testgruppen oder einzelne Nutzer:innen zu senden, oder zeigen Sie die Nachricht als Nutzer:in direkt in Braze in der Vorschau an.

### 5. Schritt: Erstellen Sie den Rest Ihrer Campaign oder Ihres Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

Erstellen Sie als Nächstes den Rest Ihrer Campaign oder Ihres Canvas. In den folgenden Abschnitten finden Sie weitere Details zur optimalen Nutzung unserer Tools zum Erstellen von RCS-Nachrichten.

#### Schritt 5.1: Wählen Sie Zustellungszeitplan oder Trigger {#step-51-choose-delivery-schedule-or-trigger}

RCS-Nachrichten können basierend auf einem geplanten Zeitpunkt, einer Aktion oder einem API-Trigger zugestellt werden. Weitere Informationen finden Sie unter [Ihre Campaign planen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Für aktionsbasierte Zustellung können Sie auch die Dauer der Campaign und Ruhezeiten festlegen.

Legen Sie Ihre Zustellungskontrollen fest, z. B. ob Nutzer:innen erneut für den Empfang der Campaign berechtigt werden können oder ob Frequency-Capping-Regeln aktiviert werden sollen.

#### Schritt 5.2: Wählen Sie die Zielnutzer:innen {#step-52-choose-users-to-target}

Richten Sie Ihre Zielgruppe aus, indem Sie Segmente oder Filter wählen, um Ihre Zielgruppe einzugrenzen. Sie sollten bereits die Abo-Gruppe ausgewählt haben, die Nutzer:innen nach dem Grad oder der Kategorie der Kommunikation eingrenzt, die sie mit Ihnen haben möchten.

{% multi_lang_include audience/target_audiences.md %}

Als Nächstes wählen Sie die größere Zielgruppe aus Ihren Segmenten und grenzen dieses Segment mit optionalen [Filtern]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) weiter ein. Sie erhalten automatisch eine Vorschau, wie die ungefähre Segmentpopulation aktuell aussieht. Beachten Sie, dass die genaue Segmentzugehörigkeit immer erst unmittelbar vor dem Senden der Nachricht berechnet wird.

{% alert tip %}
Möchten Sie RCS-Retargeting verwenden, um Nutzer:innen basierend auf ihren SMS- und RCS-Interaktionen anzusprechen? Weitere Informationen finden Sie unter [Retargeting]({{site.baseurl}}/sms_mms_rcs_user_retargeting/).
{% endalert %}

#### Schritt 5.3: Wählen Sie Konversions-Events {#step-53-choose-conversion-events}

Braze ermöglicht es Ihnen zu verfolgen, wie oft Nutzer:innen bestimmte Aktionen oder Konversions-Events nach dem Empfang einer Campaign ausführen. Sie können ein Zeitfenster von bis zu 30 Tagen festlegen, in dem eine Conversion gezählt wird, wenn die Nutzer:innen die angegebene Aktion ausführen.

Konversions-Events helfen Ihnen, den Erfolg Ihrer Campaign zu messen. Zum Beispiel:
- Wenn Sie Geotargeting verwenden, um eine RCS-Nachricht auszulösen, deren Endziel ein Kauf durch die Nutzer:innen ist, setzen Sie das Konversions-Event auf **Kauf**.
- Wenn Sie versuchen, die Nutzer:innen in Ihre App zu bringen, setzen Sie das Konversions-Event auf **Sitzung starten**.

Sie können auch benutzerdefinierte Konversions-Events basierend auf Ihrem spezifischen Anwendungsfall festlegen. Seien Sie kreativ dabei, wie Sie den Erfolg Ihrer Campaign wirklich messen möchten.

### 6. Schritt: Überprüfen und bereitstellen {#step-6-review-and-deploy}

Nachdem Sie Ihre Campaign oder Ihr Canvas fertig erstellt haben, überprüfen Sie die Details, testen Sie es und senden Sie es ab!

Lesen Sie als Nächstes [Reporting für SMS, MMS und RCS]({{site.baseurl}}/sms_mms_rcs_reporting/), um zu erfahren, wie Sie auf die Ergebnisse Ihrer RCS-Campaigns zugreifen können.

## Analytics und Reporting {#analytics-and-reporting}

Ihre Campaign- oder Canvas-Analytics umfassen:

- _Total Click_-Statistiken, die alle Interaktionen mit der Rich Card einschließen, wie Button-Klicks und Suggested Replies oder Actions.
- Eine Aufschlüsselungstabelle, die eine detailliertere Ansicht dieser Interaktionen bietet.

{% alert note %}
Der Early Access umfasst kein Klick-Tracking auf Nutzerebene. _Total Clicks_ wird bei jedem Button-Klick erhöht. Wenn beispielsweise ein:e Nutzer:in denselben Button dreimal anklickt, erhöht sich der Klickzähler um drei.
{% endalert %}

## Tipps {#tips}

### Liquid für Nachrichtenpersonalisierung verwenden {#using-liquid-for-message-personalization}

Wenn Sie Liquid verwenden möchten, stellen Sie sicher, dass Sie einen Standardwert für Ihre gewählte Personalisierung angeben, damit Empfänger:innen mit unvollständigem Nutzerprofil keinen leeren Platzhalter `Hi, !` anstelle ihres Namens oder eines zusammenhängenden Satzes erhalten.

### KI-Texte generieren {#generating-ai-copy}

Brauchen Sie Hilfe beim Erstellen ansprechender Texte? Probieren Sie den [KI-Textassistenten]({{site.baseurl}}/user_guide/brazeai/operator/capabilities/#generate-copy) aus. Geben Sie einen Produktnamen oder eine Beschreibung ein, und die KI generiert menschenähnliche Marketingtexte zur Verwendung in Ihren Nachrichten.

![Nachrichten-Editor mit einem Symbol zum Öffnen des KI-Textassistenten.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_ai_copywriter.png %}){: style="max-width:70%;"}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Kann ich vorab aufgezeichnete Sprachnachrichten mit RCS senden? {#can-i-send-pre-recorded-voicemails-with-rcs}

Ja, Sie können Media-Nachrichten verwenden, um Audio-Dateien zu unterstützen.