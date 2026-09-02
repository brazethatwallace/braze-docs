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

### Schritt 1: Wählen Sie, wo Sie Ihre Nachricht erstellen möchten {#step-1-choose-where-to-build-your-message}

Sind Sie unsicher, ob Ihre Nachricht über eine Campaign oder ein Canvas gesendet werden soll? Campaigns eignen sich besser für einzelne, einfache Messaging-Kampagnen, während Canvase besser für mehrstufige User Journeys geeignet sind.

{% tabs %}
{% tab Campaign %}
1. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Campaign erstellen**.
2. Wählen Sie **Kurzmitteilungsdienst or SMS/MMS/RCS** oder für Campaigns, die auf mehrere Kanäle abzielen, **Multichannel**.
3. Geben Sie Ihrer Campaign einen aussagekräftigen Namen.
4. Fügen Sie bei Bedarf [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) und [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) hinzu.
   * Tags erleichtern das Auffinden Ihrer Campaigns und das Erstellen von Berichten. Wenn Sie beispielsweise den [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder) verwenden, können Sie nach bestimmten Tags filtern.

{: start="5"}
5. Fügen Sie so viele Varianten hinzu und benennen Sie diese, wie Sie für Ihre Campaign benötigen. Sie können für jede hinzugefügte Variante unterschiedliche Plattformen, Nachrichtentypen und Layouts wählen. Weitere Informationen zu diesem Thema finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing).
- **Kurzmitteilungsdienst or SMS- und RCS-Varianten-Tests**: Braze ermöglicht es Ihnen, sowohl Kurzmitteilungsdienst or SMS- als auch RCS-Varianten in einer einzelnen Campaign einzuschließen, sodass Sie die Performance der einzelnen Varianten vergleichen können. Sie können Kurzmitteilungsdienst or SMS- und RCS-Varianten im ersten Schritt der Nachrichtenkomposition hinzufügen.

{: start="6"}
6. Wählen Sie eine RCS-fähige [Abo-Gruppe]({{site.baseurl}}/sms_rcs_subscription_groups) aus. Beim Auswählen einer Abo-Gruppe fügt Braze automatisch einen Segmentierungsfilter hinzu, der sicherstellt, dass nur abonnierte Nutzer:innen die Campaign erhalten. Nur Langcodes und Shortcodes, die zu dieser Abo-Gruppe gehören, werden zum Senden von Kurzmitteilungsdienst or SMS an Ihre Zielgruppe verwendet.
- **Kurzmitteilungsdienst or SMS-Fallback**: Braze empfiehlt dringend, dass jede Abo-Gruppe, die einen RCS-Sender enthält, auch mindestens einen Kurzmitteilungsdienst or SMS-Code als Fallback beinhaltet. Dies ist wichtig für die Zustellbarkeit, falls RCS-Nachrichten nicht zugestellt werden können. Gründe hierfür können unter anderem Inkompatibilität des Nutzergeräts und unvollständige Carrier-Abdeckung in einem bestimmten Land oder einer bestimmten Region sein. Durch die Aktivierung des Kurzmitteilungsdienst or SMS-Fallbacks wird Ihre Nachricht dennoch an Ihre Nutzer:innen zugestellt, sodass Sie nie die Gelegenheit verpassen, mit ihnen in Kontakt zu treten.

{: start="7"}
7. Wählen Sie zwischen Kurzmitteilungsdienst or SMS und RCS. Bevor Sie RCS-Nachrichten verfassen, wählen Sie den Kanal, über den Sie senden möchten. Wir empfehlen im Allgemeinen, RCS zu verwenden, wo immer es möglich ist, da es im Vergleich zu Kurzmitteilungsdienst or SMS erhebliche Vorteile für das Nutzer-Engagement bietet; allerdings bieten wir immer die Option, mit Kurzmitteilungsdienst or SMS zu senden, damit Sie maximale Flexibilität und Kontrolle haben.

![Optionen zur Auswahl eines RCS- oder Kurzmitteilungsdienst or SMS/MMS-Nachrichtentyps.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% alert tip %}
Wenn alle Nachrichten in Ihrer Campaign ähnlich sein oder denselben Inhalt haben werden, verfassen Sie Ihre Nachricht, bevor Sie zusätzliche Varianten hinzufügen. Sie können dann **Von Variante kopieren** aus dem Dropdown **Variante hinzufügen** wählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Erstellen Sie Ihr Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) mit dem Canvas-Composer.
2. Nachdem Sie Ihr Canvas eingerichtet haben, fügen Sie im Canvas-Builder einen **Kurzmitteilungsdienst or SMS/MMS/RCS**-Nachrichtenschritt hinzu.
3. Geben Sie Ihrem Schritt einen aussagekräftigen Namen.
4. Wählen Sie eine RCS-fähige [Abo-Gruppe]({{site.baseurl}}/sms_rcs_subscription_groups) aus. Beim Auswählen einer Abo-Gruppe fügt Braze automatisch einen Segmentierungsfilter hinzu, der sicherstellt, dass nur abonnierte Nutzer:innen die Campaign erhalten. Nur Langcodes und Shortcodes, die zu dieser Abo-Gruppe gehören, werden zum Targeting Ihrer Zielgruppe verwendet.
- **Kurzmitteilungsdienst or SMS-Fallback**: Braze empfiehlt dringend, dass jede Abo-Gruppe, die einen RCS-Sender enthält, auch mindestens einen Kurzmitteilungsdienst or SMS-Code als Fallback beinhaltet. Dies ist wichtig für die Zustellbarkeit, falls RCS-Nachrichten nicht zugestellt werden können. Gründe hierfür können unter anderem Inkompatibilität des Nutzergeräts und unvollständige Carrier-Abdeckung in einem bestimmten Land oder einer bestimmten Region sein. Durch die Aktivierung des Kurzmitteilungsdienst or SMS-Fallbacks wird Ihre Nachricht dennoch an Ihre Nutzer:innen zugestellt, sodass Sie nie die Gelegenheit verpassen, mit ihnen in Kontakt zu treten.

{: start="5"}
5. Wählen Sie zwischen Kurzmitteilungsdienst or SMS und RCS. Bevor Sie RCS-Nachrichten verfassen, wählen Sie den Kanal, über den Sie senden möchten. Wir empfehlen im Allgemeinen, RCS zu verwenden, wo immer es möglich ist, da es im Vergleich zu Kurzmitteilungsdienst or SMS erhebliche Vorteile für das Nutzer-Engagement bietet; allerdings bieten wir immer die Option, mit Kurzmitteilungsdienst or SMS zu senden, damit Sie maximale Flexibilität und Kontrolle haben.

![Optionen zur Auswahl eines RCS- oder Kurzmitteilungsdienst or SMS/MMS-Nachrichtentyps.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% endtab %}
{% endtabs %}

### Schritt 2: Wählen Sie Ihren RCS-Nachrichtentyp {#step-2-select-your-rcs-message-type}

Wählen Sie während der Campaign- und Canvas-Erstellung aus drei RCS-Nachrichtentypen (Text, Medien, Rich Card), um Nachrichten zu konfigurieren, die am besten zu Ihren Zielen passen.

![Optionen zur Auswahl eines Text-, Medien- oder Card-Nachrichtentyps.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_text_media.png %}){: style="max-width:65%;"}

{% tabs local %}
{% tab Text %}
Wie der Name schon sagt, konzentrieren sich RCS-Textnachrichten auf Text als Medium. Wenn Sie bis zu 160 Zeichen eingeben, wird die RCS-Nachricht als reine Textnachricht (oder „Basic“-Nachricht) abgerechnet. Wenn Sie 160 Zeichen überschreiten oder ein Rich-Element verwenden, wird die Nachricht als Rich-Nachricht (oder „Single“-RCS-Nachricht) abgerechnet (und das Zeichenlimit erhöht sich auf 3072 Zeichen).

#### Features

- Text-Nachrichtentypen umfassen alle Kurzmitteilungsdienst or SMS-Features. Für URL-Klick-Tracking ist nur Advanced Tracking möglich, um Ihnen Berichtsgranularität auf Nutzerebene zu bieten.
- Darüber hinaus haben Sie jetzt die Möglichkeit, ansprechende **Suggested Replies** und **Suggested Actions** Buttons einzufügen, die zu nutzeraktiven Handlungen mit hohem Engagement führen, wie z. B. den Besuch einer Landing-Page oder das Aufgeben einer Bestellung.
    - **Suggested Replies** sind Buttons mit vorgeschlagenen Antworten, auf die Nutzer:innen klicken können, um diese in ihrer Texteingabe vorzubefüllen. So wird die Hürde genommen, sich eine Antwort überlegen zu müssen, indem eine begrenzte Auswahl an Optionen bereitgestellt wird.
    - **Suggested Actions** sind Buttons, die eine Aktion auf dem Gerät der Nutzer:innen auslösen. Sie bestehen in der Regel aus einem oder zwei beschreibenden Wörtern und einem visuellen Symbol, das den Nutzer:innen hilft zu verstehen, was der Button bewirkt. Braze unterstützt derzeit OpenURL Suggested Actions. Dies funktioniert ähnlich wie eine URL, wobei Nutzer:innen, die den Button auswählen, zu einer Webseite oder einem anderen URL-identifizierten Ziel weitergeleitet werden.

![Ein GIF mit drei Suggested Actions für eine RCS-Nachricht, die trendige Modestile bewirbt: „Fairytale royalty“, „Edgy academia“ und „Show me your other styles“.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_suggested_actions.gif %}){: style="max-width:70%;"}

#### Hinweise {#considerations}

- Für die Zeichenbegrenzung bei Text können Sie bis zu 160 Zeichen für eine reine Text-RCS-Nachricht (Basic) oder bis zu 3072 Zeichen für eine Rich-RCS-Nachricht (Single) schreiben.
- Für Button-Limits können Sie bis zu fünf Buttons pro Nachricht hinzufügen. Diese Buttons können entweder Suggested Actions oder Suggested Replies sein.
- Längere Textblöcke und zu viele Buttons können Nutzer:innen frustrieren, daher empfehlen wir nach Möglichkeit, auf Einfachheit zu setzen.
- In einigen Fällen kann es kostengünstiger sein, längere reine Textnachrichten über RCS statt über Kurzmitteilungsdienst or SMS zu senden. Dies liegt daran, dass längere Kurzmitteilungsdienst or SMS-Nachrichten in mehrere Segmente aufgeteilt werden, von denen jedes einzeln abgerechnet wird, während RCS-Nachrichten stattdessen pro Nachricht abgerechnet werden. Wenden Sie sich an Ihren Braze Account Manager:in für weitere Details und Beratung.
{% endtab %}

{% tab Medien %}
RCS-Mediennachrichten ermöglichen es Ihnen, ansprechende Medienformate zu nutzen, die mit Kurzmitteilungsdienst or SMS nicht möglich sind. Dazu gehören Bild-, Video- und Dokumentdateien. Diese Medienoptionen helfen Ihnen, Ihre Zielgruppe noch intensiver anzusprechen und völlig neue Anwendungsfälle zu ermöglichen. Derzeit wird nur das Hochladen von Bildern über die [Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications) unterstützt.

#### Features

- Medien-Nachrichtentypen unterstützen alles, was in Text-Nachrichtentypen verfügbar ist, einschließlich Text, Suggested Replies und Suggested Actions.
- Unterstützt Bilddateien, einschließlich der Dateiformate JPEG und PNG. Bilddateien sind über den Upload aus der Medienbibliothek verfügbar.
- Unterstützt Videodateien, einschließlich der Dateiformate MP4, MPEG und MV4. Videodateien können per URL direkt im Nachrichten-Editor hinzugefügt werden.
- Unterstützt Dokumentdateien im PDF-Format. Dokumentdateien können über die URL direkt im Nachrichten-Editor hinzugefügt werden.

![RCS-Composer mit einer Option zum Hochladen einer Mediendatei.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_media_type.png %})

#### Dateispezifikationen {#file-specifications}

| Dateityp | Spezifikationen |
| --- | --- |
| Alle | - Die Dateigröße ist auf 100 MB begrenzt <br><br>- Die Datei-URL kann bis zu 2048 Zeichen haben |
| Bilddateien | Unterstützte Dateiformate: JPG, JPEG und GIF |
| Videodateien | Unterstützte Dateiformate: H263, M4V, MP4, MPEG-4, MPEG, WEBM |
| Dokumentdateien | Unterstütztes Dateiformat: PDF |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Hinweise

Die Nutzererfahrung beim Empfang von RCS-Nachrichten kann je nach verschiedenen Faktoren leicht variieren, darunter Carrier-Abdeckung im Zielland, mobile Gerätehardware und mobiles Betriebssystem.

Im Allgemeinen integriert sich RCS natürlicher mit Android-Geräten (diese Methode wurde größtenteils von Google implementiert, und Peer-to-Peer-RCS-Messaging ist in der Android-Community weit verbreitet). Verschiedene Geräte können die Erfahrung mit unterschiedlicher Geschwindigkeit und Qualität darstellen.
{% endtab %}

{% tab Rich Card %}

{% alert important %}
Rich Cards befinden sich im Early Access. Wenden Sie sich an Ihren Braze CSM or Customer-Success-Manager or Customer-Success-Manager:in, wenn Sie an diesem Early Access teilnehmen möchten.
{% endalert %}

Eine Rich Card kombiniert Medien, Text und Buttons in einer einzigen Nachricht und schafft so ein intuitiveres und ansprechenderes Erlebnis für Ihre Kund:innen. Sie können zwei Untertypen von Rich Cards erstellen: Text und Medien.

{% subtabs %}
{% subtab Text %}
Eine Text Rich Card ist eine kompakte Nachricht, die sich auf Text konzentriert. Sie muss die folgenden Elemente enthalten:

- **Titel:** Bis zu 200 Zeichen. Kann mit Liquid personalisiert werden.
- **Beschreibung:** Bis zu 2.000 Zeichen. Kann mit Liquid personalisiert werden.
- **Buttons:** Mindestens ein Button ist erforderlich. Sie können bis zu vier Buttons mit **Suggested Reply**- oder **Open Web URL**-Aktionen hinzufügen.

{% endsubtab %}
{% subtab Medien %}

Eine Medien Rich Card ist eine visuelle Nachricht, die ein Bild oder Video enthält. Sie muss die folgenden Elemente enthalten:

- **Medien:** Ein Bild, GIF oder Video.
    - Benutzerdefinierte Video-Thumbnails werden im Early Access nicht unterstützt. Der Early Access unterstützt nur ein vertikales Layout mit großer Medienhöhe sowohl für Bild- als auch für Videodateien.
- **Buttons:** Mindestens ein Button ist erforderlich. Sie können bis zu vier Buttons mit **Suggested Reply**- oder **Open Web URL**-Aktionen hinzufügen.

{% alert note %}
Auf iOS werden GIFs in Rich Cards als statische Bilder angezeigt. Auf Android werden sie wie erwartet animiert. Um animierte Inhalte an iOS zu senden, verwenden Sie eine RCS-**Medien**-Nachricht oder fügen Sie ein Video in die Rich Card ein. Ein GIF kann in der Braze-Vorschau weiterhin animiert sein, senden Sie daher einen Test an ein iOS-Gerät.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}

### Features
- **Card-Buttons** und **Vorschläge:** Sie können bis zu vier Buttons und fünf Vorschläge (jeweils bis zu 25 Zeichen) am unteren Rand der Rich Card (Buttons) oder am unteren Rand des Nachrichtenbildschirms (Vorschläge) hinzufügen. Nutzer:innen können diese Klick-Tipp-Optionen auswählen, um eine bestimmte Antwort zu senden oder eine bestimmte Aktion auszuführen.
- **Personalisierung:** Sie können Liquid verwenden, um alle Rich Card-Elemente zu personalisieren, einschließlich Titel, Beschreibung, Medien und Buttons.
- **Abrechnung:** Rich Cards werden als einzelne Rich-RCS-Nachricht (oder „Single“-RCS-Nachricht) abgerechnet.
- **URL-Hinweis:** URLs, die als reiner Text im Titel oder in der Beschreibung eingegeben werden, sind nicht klickbar. Sie müssen einen **OpenURL-Button** verwenden, um Nutzer:innen zu einer Website weiterzuleiten.

![Panel mit Optionen zur Auswahl einer Medien- oder Text-Rich-Card.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_media_text.png %}){: style="max-width:65%;"}

{% endtab %}
{% endtabs %}

### Schritt 3: Verfassen Sie Ihre RCS-Nachricht {#step-3-compose-your-rcs-message}

Schreiben Sie Ihre Nachricht mit Sprachen und Personalisierung ([Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) und Emojis) nach Bedarf. Achten Sie darauf, unsere Nachrichtentextlimits einzuhalten, um das Risiko von Zusatzkosten zu reduzieren.

{% alert important %}
Bevor Sie fortfahren, lesen Sie unsere [Richtlinien für RCS-Nachrichtenlimits](#step-2-select-your-rcs-message-type). RCS-Nachrichten werden [pro Nachricht abgerechnet]({{site.baseurl}}/sms_rcs_billing_calculators), daher ist es ratsam, die Feinheiten zu verstehen, was in jedem RCS-Nachrichtentyp enthalten sein kann.
{% endalert %}

### Schritt 4: Vorschau und Test Ihrer Nachricht {#step-4-preview-and-test-your-message}

Braze empfiehlt immer, Ihre Nachricht vor dem Senden in der Vorschau anzuzeigen und zu testen. Gehen Sie zum Tab **Test**, um eine Test-RCS an Content-Testgruppen oder einzelne Nutzer:innen zu senden, oder zeigen Sie die Nachricht als Nutzer:in direkt in Braze in der Vorschau an.

### Schritt 5: Erstellen Sie den Representational State Transfer Ihrer Campaign oder Ihres Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

Erstellen Sie als Nächstes den Representational State Transfer Ihrer Campaign oder Ihres Canvas. In den folgenden Abschnitten finden Sie weitere Details dazu, wie Sie unsere Tools am besten zum Erstellen von RCS-Nachrichten nutzen können.

#### Schritt 5.1: Wählen Sie Zeitplan oder Trigger or triggern für die Zustellung {#step-51-choose-delivery-schedule-or-trigger}

RCS-Nachrichten können basierend auf einer geplanten Zeit, einer Aktion oder einem API-Trigger or triggern zugestellt werden. Weitere Informationen finden Sie unter [Ihre Campaign planen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Bei aktionsbasierter Zustellung können Sie auch die Dauer der Campaign und Ruhezeiten festlegen.

Legen Sie Ihre Zustellungskontrollen fest, z. B. ob Nutzer:innen erneut für den Empfang der Campaign berechtigt werden können oder ob Frequency-Capping-Regeln aktiviert werden sollen.

#### Schritt 5.2: Wählen Sie die Zielgruppe aus {#step-52-choose-users-to-target}

Sprechen Sie Nutzer:innen an, indem Sie Segments oder Filter auswählen, um Ihre Zielgruppe einzugrenzen. Sie sollten bereits die Abo-Gruppe ausgewählt haben, die die Nutzer:innen nach dem Grad oder der Kategorie der Kommunikation eingrenzt, die sie mit Ihnen haben möchten.

{% multi_lang_include audience/target_audiences.md %}

Als Nächstes wählen Sie die größere Zielgruppe aus Ihren Segments aus und grenzen dieses Segment mit optionalen [Filtern]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) weiter ein. Sie erhalten automatisch eine Vorschau darauf, wie die ungefähre Segmentpopulation derzeit aussieht. Beachten Sie, dass die genaue Segmentzugehörigkeit immer kurz vor dem Senden der Nachricht berechnet wird.

{% alert tip %}
Sind Sie daran interessiert, RCS-Retargeting zu nutzen, um Nutzer:innen basierend auf ihren Kurzmitteilungsdienst or SMS- und RCS-Interaktionen anzusprechen? Weitere Informationen finden Sie unter [Retargeting]({{site.baseurl}}/sms_mms_rcs_user_retargeting).
{% endalert %}

#### Schritt 5.3: Wählen Sie Konversions-Events {#step-53-choose-conversion-events}

Braze ermöglicht es Ihnen, zu verfolgen, wie oft Nutzer:innen nach dem Empfang einer Campaign bestimmte Aktionen oder Konversions-Events durchführen. Sie können ein Zeitfenster von bis zu 30 Tagen festlegen, in dem eine Konversion gezählt wird, wenn die Nutzer:innen die angegebene Aktion ausführen.

Konversions-Events helfen Ihnen, den Erfolg Ihrer Campaign zu messen. Zum Beispiel:
- Wenn Sie Geotargeting verwenden, um eine RCS-Nachricht auszulösen, deren Endziel ein Kauf durch die Nutzer:innen ist, setzen Sie das Konversions-Event auf **Kauf**.
- Wenn Sie versuchen, die Nutzer:innen in Ihre App zu bringen, setzen Sie das Konversions-Event auf **Startet Sitzung**.

Sie können auch benutzerdefinierte Konversions-Events basierend auf Ihrem spezifischen Anwendungsfall festlegen. Seien Sie kreativ dabei, wie Sie den Erfolg Ihrer Campaign wirklich messen möchten.

### Schritt 6: Überprüfen und Bereitstellen {#step-6-review-and-deploy}

Nachdem Sie Ihre Campaign oder Ihr Canvas fertiggestellt haben, überprüfen Sie die Details, testen Sie sie und senden Sie sie dann!

Lesen Sie als Nächstes [Reporting für Kurzmitteilungsdienst or SMS, MMS und RCS]({{site.baseurl}}/sms_mms_rcs_reporting), um zu erfahren, wie Sie auf die Ergebnisse Ihrer RCS-Campaigns zugreifen können.

## Analytics und Berichterstattung {#analytics-and-reporting}

Ihre Campaign- oder Canvas-Analytics umfassen:

- _Gesamtklicks_-Statistiken, die alle Interaktionen mit der Rich Card beinhalten, wie Button-Klicks und vorgeschlagene Antworten oder Aktionen.
- Eine Aufschlüsselungstabelle, die eine detailliertere Ansicht dieser Interaktionen bietet.

{% alert note %}
Der Early Access umfasst kein Klick-Tracking auf Nutzer:innen-Ebene. _Gesamtklicks_ werden bei jedem Button-Klick erhöht. Wenn beispielsweise ein:e Nutzer:in denselben Button dreimal anklickt, erhöht sich die Klickanzahl um drei.
{% endalert %}

## Tipps {#tips}

### Liquid für die Nachrichtenpersonalisierung verwenden {#using-liquid-for-message-personalization}

Wenn Sie Liquid verwenden möchten, sollten Sie unbedingt einen Standardwert für Ihre gewählte Personalisierung angeben. So wird den Empfänger:innen bei einem unvollständigen Kundenprofil or Nutzerprofil nicht ein leerer Platzhalter wie `Hi, !` anstelle ihres Namens oder eines sinnvollen Satzes angezeigt.

### KI or künstliche Intelligenz-gestützte Texte erstellen {#generating-ai-copy}

Brauchen Sie Hilfe beim Erstellen ansprechender Texte? Nutzen Sie den [KI or künstliche Intelligenz-Textassistenten]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy). Geben Sie einen Produktnamen oder eine Beschreibung ein, und die KI or künstliche Intelligenz generiert menschlich klingende Marketingtexte zur Verwendung in Ihrem Messaging.

![Nachrichten-Editor mit einem Symbol zum Öffnen des KI or künstliche Intelligenz-Textassistenten.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_ai_copywriter.png %}){: style="max-width:70%;"}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Kann ich vorab aufgezeichnete Voicemails mit RCS senden? {#can-i-send-pre-recorded-voicemails-with-rcs}

Ja, Sie können Mediennachrichten verwenden, um Audio-Dateien zu unterstützen.