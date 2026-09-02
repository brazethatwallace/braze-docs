---
nav_title: KakaoTalk-Nachricht erstellen
article_title: KakaoTalk-Nachricht erstellen
description: "Dieser Referenzartikel beschreibt, wie Sie eine KakaoTalk-Nachricht erstellen."
page_order: 1
alias: /create_kakaotalk_message/
channel:
  - KakaoTalk
---

# KakaoTalk-Nachricht erstellen {#create-a-kakaotalk-message}

> Nutzen Sie den [KakaoTalk-Messaging-Kanal]({{site.baseurl}}/kakaotalk), um Nutzer:innen direkt über die KakaoTalk-Plattform zu erreichen. Erstellen Sie ein personalisiertes Nutzererlebnis, indem Sie Liquid und andere dynamische Inhalte verwenden, um eine Umgebung zu schaffen, die ein reichhaltiges Nutzererlebnis mit Ihrer Marke fördert und verbessert.<br><br>Informationen zur Einrichtung Ihres KakaoTalk-Messaging-Kanals finden Sie unter [KakaoTalk einrichten]({{site.baseurl}}/kakaotalk_setup).

## Schritt 1: Wählen Sie, wo Sie Ihre Nachricht erstellen {#step-1-choose-where-to-build-your-message}

KakaoTalk wird sowohl in Campaigns als auch in Canvas unterstützt. Campaigns eignen sich am besten für einzelne Messaging-Kampagnen, während Canvase es Ihnen ermöglichen, mehrstufige, kanalübergreifende Nutzer:innen-Journeys zu orchestrieren.

{% tabs local %}
{% tab Campaign %}

1. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Create Campaign**.
2. Wählen Sie **KakaoTalk** für eine Einzelkanal-Campaign oder **Multichannel Campaign** für eine Mehrkanal-Campaign.

![Panel mit Optionen zur Auswahl des Messaging-Kanals.]({% image_buster /assets/img/kakaotalk/kakaotalk_campaign.png %}){: style="max-width:30%" }

3. Sie können zusätzliche Varianten zu Ihrer Campaign hinzufügen, um verschiedene Nachrichtentypen und Layouts auszuwählen. Weitere Informationen finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% endtab %}
{% tab Canvas %}

1. [Erstellen Sie Ihren Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas).
2. Fügen Sie im Canvas-Builder einen Nachrichtenschritt hinzu und wählen Sie **KakaoTalk**.

![Auswahl der Messaging-Kanäle im Canvas.]({% image_buster /assets/img/kakaotalk/kakaotalk_canvas.png %})

{% endtab %}
{% endtabs %}

## Schritt 2: Ihre KakaoTalk-Nachricht verfassen {#step-2-compose-your-kakaotalk-message}

1. Wählen Sie das Dropdown-Menü **KakaoTalk-Kanal** aus, das eine Liste der KakaoTalk-Kanäle anzeigt, die Sie über die Technologie-Partnerseite eingerichtet haben, und wählen Sie den KakaoTalk-Kanal aus, über den die Nachricht gesendet werden soll.
2. Wählen Sie den zu sendenden Nachrichtentyp aus:
   - Text
   - Bild
       - Schmal
       - Breit
   - Listeneinträge
   - Karussell

{% tabs local %}
{% tab Text %}

Eine KakaoTalk-Textnachricht ist die einfachste Form der Kommunikation: eine Standard-Textnachricht.

### Spezifikationen {#specifications}

| Bereich | Spezifikationen |
| --- | --- |
| Inhalt | Textinhalt, einschließlich Emojis und Liquid-Personalisierung |
| Textkapazität | Bis zu 1.000 Zeichen |
| Buttons | Bis zu 5 optionale Buttons. Derzeit kann dies nur verwendet werden, um beim Klick eine URL zu öffnen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Spezifikationen" }

![Eine KakaoTalk-Textnachricht im Composer.]({% image_buster /assets/img/kakaotalk/kakaotalk_text.png %})

{% endtab %}
{% tab Bild %}

Ein Bild ist eine Nachricht, die ein visuelles Element mit unterstützendem Text kombiniert. Braze übernimmt automatisch den Upload des Bildes auf die KakaoTalk-Server.

### Allgemeine Spezifikationen {#general-specifications}

| Bereich | Spezifikationen |
| --- | --- |
| Inhalt | Ein Bild und unterstützender Text |
| Akzeptierte Dateiformate | JPEG oder PNG |
| Empfohlene Breite | 500px |
| Dateigröße | Bis zu 500 KB |
| Seitenverhältnis | Muss zwischen 2:1 (breit) und 3:4 (hoch) liegen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Allgemeine Spezifikationen" }

Schmale und breite Bildnachrichten haben jeweils unterschiedliche Zeichenanzahl- und Button-Anforderungen.

{% subtabs %}
{% subtab Schmales Bild %}

#### Schmales Bild {#narrow-image}

Eine schmale Bildnachricht zeigt ein etwas höheres, schmales Bild mit umfangreicheren Text- und Button-Optionen.

##### Spezifikationen

| Bereich | Spezifikationen |
| --- | --- |
| Inhalt | Ein Bild und unterstützender Text |
| Textkapazität | Bis zu 500 Zeichen |
| Buttons | Bis zu 5 optionale Buttons |
| Bildquelle | Bilder können über die Braze-Medienbibliothek oder eine direkte URL hinzugefügt werden |
| Anpassung | Sie können das Klickverhalten für das Bild festlegen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Spezifikationen" }

![Eine schmale KakaoTalk-Nachricht.]({% image_buster /assets/img/kakaotalk/narrow_image.png %})

{% endsubtab %}
{% subtab Breites Bild %}

#### Breites Bild {#wide-image}

Eine breite Bildnachricht zeigt ein prominentes breites Bild, das sich für wirkungsvolle visuelle Kommunikation eignet, mit minimalem unterstützendem Text.

##### Spezifikationen

| Bereich | Spezifikationen |
| --- | --- |
| Inhalt | Ein Bild und unterstützender Text |
| Textkapazität | Bis zu 76 Zeichen |
| Buttons | Bis zu 2 optionale Buttons |
| Bildquelle | Bilder können über die Braze-Medienbibliothek oder eine direkte URL hinzugefügt werden |
| Anpassung | Sie können das Klickverhalten des Bildes festlegen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Spezifikationen" }

![Eine breite KakaoTalk-Nachricht.]({% image_buster /assets/img/kakaotalk/wide_image.png %})

{% endsubtab %}
{% endsubtabs %}

### Bilder hinzufügen {#add-images}

Sie können Bilder über die Braze-Medienbibliothek hinzufügen oder eine URL einfügen, die eine JPEG- oder PNG-Datei hostet. Sie können auch das Klickverhalten des Bildes festlegen, um Nutzer:innen, die darauf klicken, zu einer bestimmten URL weiterzuleiten.

Braze übernimmt automatisch alle Bild-Upload-Anforderungen von KakaoTalk. Das bedeutet, dass Sie Bilder nicht vor dem Senden von Nachrichten bei KakaoTalk-Anbietern hochladen müssen. Laden Sie einfach Bilder hoch und senden Sie die Nachricht direkt über Braze!

![Bereich mit ausgewählten Symbolen zum Hinzufügen eines schmalen Bildes.]({% image_buster /assets/img/kakaotalk/add_image.png %})

{% endtab %}
{% tab Listeneinträge %}


Eine KakaoTalk-Artikellisten-Nachricht ist dafür konzipiert, eine Liste von Inhaltsartikeln in einem übersichtlichen, vertikalen Format darzustellen.

Listeneintrags-Nachrichten bestehen aus einem Header, einem Artikellistenbereich und einem optionalen Button-Bereich.

#### Spezifikationen

| Bereich | Spezifikationen |
| --- | --- |
| Artikelanzahl | Erfordert mindestens 2 oder 3 Artikel |
| Header | Bis zu 250 Zeichen |
| Artikeltitel | Bis zu 25 Zeichen |
| Website-URL (pro Artikel, Zeilenklick) | Erforderlich. Bis zu 250 Zeichen. Wird geöffnet, wenn Nutzer:innen auf das Bild oder den Titel des Artikels tippen. |
| Buttons (auf Nachrichtenebene) | Bis zu 5 optionale Buttons mit eigenen URLs oder Aktionen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Spezifikationen" }

![Eine KakaoTalk-Listeneintrags-Nachricht.]({% image_buster /assets/img/kakaotalk/item_list.png %})

{% endtab %}
{% tab Karussell %}

Eine KakaoTalk-Karussell-Nachricht enthält bis zu sechs scrollbare Karten. Jede Karte hat ein Bild, einen Header, eine Nachricht, eine optionale **Website-URL** und mindestens einen Button.

Sowohl die Karte als auch ihre Buttons verwenden im Composer ein Feld mit der Bezeichnung **Website-URL**, das jedoch für unterschiedliche Tipp-Ziele gilt:

- **Website-URL der Karte:** (Optional) Wird geöffnet, wenn Nutzer:innen auf das Kartenbild tippen. Wenn Sie dieses Feld leer lassen, ist das Bild nicht antippbar.
- **Website-URL des Buttons:** Wird geöffnet, wenn Nutzer:innen auf diesen Button tippen. Jeder Web-Button benötigt eine eigene URL und kann auf ein anderes Ziel als das Kartenbild verweisen.

Karten- und Button-URLs werden unabhängig voneinander gekürzt und getrackt, wenn das Klick-Tracking aktiviert ist.

Braze lädt Kartenbilder automatisch auf die KakaoTalk-Server hoch, wenn Sie die Nachricht senden, ähnlich wie bei Bildnachrichten.

{% alert note %}
Der Nachrichtentyp **Karussell** wird möglicherweise erst in Ihrem Workspace angezeigt, wenn er für Ihr Konto aktiviert wurde.
{% endalert %}

### Spezifikationen

| Bereich | Spezifikationen |
| --- | --- |
| Karten | 2–6 scrollbare Karten |
| Header (pro Karte) | Bis zu 20 Zeichen |
| Nachricht (pro Karte) | Bis zu 180 Zeichen |
| Bild (pro Karte) | Erforderlich |
| Akzeptierte Dateiformate | JPG oder PNG |
| Mindestbreite | 500px |
| Seitenverhältnis | 2:1, 16:10, 3:2, 4:3, 1:1 oder 3:4 |
| Website-URL (pro Karte, Bildklick) | (Optional) Bis zu 250 Zeichen. Wird geöffnet, wenn Nutzer:innen auf das Kartenbild tippen. |
| Buttons (pro Karte) | Mindestens 1, bis zu 2 |
| Button-Text (pro Karte) | Bis zu 8 Zeichen |
| Button-Typen | Web-URL öffnen, App-Link oder Textantwort |
| Button-Website-URL (pro **Web-URL öffnen**-Button) | Erforderlich. Bis zu 500 Zeichen. Wird geöffnet, wenn Nutzer:innen auf diesen Button tippen. |
| Personalisierung | Liquid wird in Kartenfeldern und URLs unterstützt |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Spezifikationen" }

![Eine KakaoTalk-Karussell-Nachricht.]({% image_buster /assets/img/kakaotalk/carousel_message.png %})

{% endtab %}
{% endtabs %}

## Schritt 3: Klick-Tracking einrichten {#step-3-set-up-click-tracking}

Wenn das KakaoTalk-Klick-Tracking aktiviert ist, kürzt Braze Ihre URLs automatisch, fügt Tracking-Mechanismen hinzu und zeichnet Klicks in Echtzeit auf. Diese Daten ermöglichen es Ihnen, gezieltere Segmentierungs- und Retargeting-Strategien zu entwickeln, z. B. Nutzer:innen basierend auf dem Klickverhalten zu segmentieren und Nachrichten als Reaktion auf bestimmte Klicks auszulösen.

Klick-Tracking wird für Text-, Bild-, Listenelement- und Karussell-Nachrichten unterstützt. Es unterstützt Links innerhalb von Buttons und Bild-Klick-Aktionen. Sie können URLs auch mit Liquid und benutzerdefinierten Domains personalisieren.

Um das Klick-Tracking zu aktivieren, aktivieren Sie **Klick, der or klicken Tracking** im Abschnitt **Link options** des Composers. URLs werden mit der Standard-Braze-Domain (`https://brz.ai`) oder der für die Abo-Gruppe angegebenen benutzerdefinierten Domain gekürzt und für die Nutzer:innen personalisiert.

Ausführliche Informationen zu Klick-Tracking, benutzerdefinierten Domains, Liquid-Personalisierung in URLs, Reporting und Retargeting finden Sie unter [KakaoTalk-Klick-Tracking]({{site.baseurl}}/kakaotalk_click_tracking).

### Retargeting von Nutzer:innen {#retargeting-users}

Sie können Nutzer:innen, die auf eine URL in einer KakaoTalk-Nachricht geklickt haben, mit den folgenden Segmentierungsfiltern und Trigger or triggern or triggern erneut ansprechen:

- Aktionsbasierte Trigger or triggern
    - Interact with Campaign
    - Interact with Step

- Segmentierungsfilter
    - Clicked/Opened Campaign
    - Clicked/Opened Campaign or Canvas with Tag
    - Clicked/Opened Step

## Schritt 4: Vorschau und Test Ihrer KakaoTalk-Nachricht {#step-4-preview-and-test-your-kakaotalk-message}

Die Nachrichtenvorschau wird automatisch aktualisiert, während Sie Ihre KakaoTalk-Nachricht verfassen. Wenn Sie bereit zum Testen sind, wechseln Sie zum Tab **Test**, um eine Testnachricht an Content-Testgruppen oder einzelne Nutzer:innen zu senden oder die Nachricht als bestehende:r oder angepasste:r Nutzer:in direkt in Braze in der Vorschau anzuzeigen.

Nachdem Sie Ihre Testnutzer:innen ausgewählt haben, wählen Sie **Test senden**. Eine Benachrichtigung zeigt die Ergebnisse Ihres Testversands an. Für CJ OliveNetworks erhalten Sie eine „C100“-Antwort. Wenn Sie einen anderen Fehler sehen, konsultieren Sie die [CJ KakaoTalk-Nutzerdokumentation](https://developers.kakao.com/docs/latest/en/index).

![Vorschaufenster für eine KakaoTalk-Nachricht.]({% image_buster /assets/img/kakaotalk/preview_message.png %})

{% alert note %}
Um eine Vorschau anzuzeigen und eine Testnachricht an bestehende Nutzer:innen zu senden, benötigen Sie die Berechtigung „View PII“. Sie können eine Vorschau anzeigen und eine Testnachricht an angepasste Nutzer:innen ohne diese Berechtigung senden.
{% endalert %}

Um die Ergebnisse eines Versands zu überprüfen oder Probleme zu beheben, gehen Sie zu **Einstellungen** > **Nachrichtenaktivitätsprotokoll**. Weitere Informationen finden Sie unter [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log).

## Schritt 5: Erstellen Sie den Representational State Transfer Ihrer Campaign oder Ihres Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

In den folgenden Abschnitten erfahren Sie, wie Sie unsere Tools am besten nutzen, um KakaoTalk-Nachrichten zu erstellen.

### Zustellungszeitplan oder Trigger or triggern wählen {#choose-delivery-schedule-or-trigger}

KakaoTalk-Nachrichten können basierend auf einem geplanten Zeitpunkt, einer Aktion oder einem API-Trigger or triggern zugestellt werden. Weitere Informationen zu Zeitplan- und Trigger or triggern-Optionen finden Sie unter [Campaign planen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign) oder [Entry-Zeitplantypen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#entry-schedule-types) (für Ihr Canvas).

Sie können Zustellungskontrollen festlegen, z. B. ob Nutzer:innen erneut für den Empfang der Campaign berechtigt werden, oder Frequency-Capping-Regeln aktivieren. Bei aktionsbasierter Zustellung können Sie außerdem die Dauer der Campaign und [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) festlegen.

{% alert important %}
KakaoTalk erzwingt Ruhezeiten von ca. 20:50 bis 08:00 Uhr Korea Standard Time (KST). Nachrichten, die in diesem Zeitfenster geplant sind, werden erst nach Ende der Ruhezeiten gesendet. Diese Einschränkung wird von den KakaoTalk-Zustellungsanbietern (CJ OliveNetworks und Infobip) durchgesetzt und gilt für alle KakaoTalk-Nachrichtentypen, unabhängig von der optionalen Ruhezeiten-Einstellung in Braze.
{% endalert %}

### Zielgruppe zusammenstellen {#choose-users-to-target}

Wählen Sie Nutzer:innen aus, indem Sie Segments oder Filter verwenden, um Ihre Zielgruppe einzugrenzen. Derzeit kann KakaoTalk nur Freunde des Kanals anschreiben. Wir empfehlen, ein angepasstes Attribut festzulegen, das Kanalfreunde kennzeichnet, damit Sie Ihre Nutzer:innen korrekt segmentieren und vermeiden, KakaoTalk-Nachrichten an Nutzer:innen zu senden, die diese nicht empfangen können.

### Konversions-Events wählen {#choose-conversion-events}

Braze ermöglicht es Ihnen, nachzuverfolgen, wie oft Nutzer:innen bestimmte Aktionen – Konversions-Events – nach dem Empfang einer Campaign ausführen. Sie haben die Möglichkeit, ein Zeitfenster von bis zu 30 Tagen festzulegen, in dem eine Konversion gezählt wird, wenn die Nutzer:innen die angegebene Aktion ausführen.

Konversions-Events helfen Ihnen, den Erfolg Ihrer Campaign zu messen. Wenn Sie beispielsweise Nutzer:innen dazu bringen möchten, Ihre App zu verwenden, setzen Sie das Konversions-Event auf **Starts Session**.

Sie können auch angepasste Konversions-Events basierend auf Ihrem spezifischen Anwendungsfall festlegen. Werden Sie kreativ und überlegen Sie, wie Sie den Erfolg Ihrer Campaign messen möchten.

## Schritt 6: Überprüfen und bereitstellen {#step-6-review-and-deploy}

Nachdem Sie den letzten Teil Ihrer Campaign oder Ihres Canvas fertig erstellt haben, überprüfen Sie die Details, testen Sie alles und senden Sie es ab!