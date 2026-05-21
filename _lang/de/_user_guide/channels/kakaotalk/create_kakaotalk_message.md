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

> Nutzen Sie den [KakaoTalk-Messaging-Kanal]({{site.baseurl}}/kakaotalk/), um Nutzer:innen direkt über die KakaoTalk-Plattform zu erreichen. Erstellen Sie ein personalisiertes Nutzererlebnis, indem Sie Liquid und andere dynamische Inhalte verwenden, um eine Umgebung zu schaffen, die ein reichhaltiges Nutzererlebnis mit Ihrer Marke fördert und verbessert.<br><br>Informationen zur Einrichtung Ihres KakaoTalk-Messaging-Kanals finden Sie unter [KakaoTalk einrichten]({{site.baseurl}}/kakaotalk_setup/).

## 1. Schritt: Wählen Sie, wo Sie Ihre Nachricht erstellen möchten {#step-1-choose-where-to-build-your-message}

KakaoTalk wird sowohl in Campaigns als auch in Canvas unterstützt. Campaigns eignen sich am besten für einzelne Messaging-Kampagnen, während Canvases es Ihnen ermöglichen, mehrstufige, kanalübergreifende Nutzer-Journeys zu orchestrieren.

{% tabs local %}
{% tab Campaign %}

1. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Create Campaign**.
2. Wählen Sie **KakaoTalk** für eine Einzelkanal-Kampagne oder **Multichannel Campaign** für eine Mehrkanal-Kampagne.

![Panel mit Optionen zur Auswahl des Messaging-Kanals.]({% image_buster /assets/img/kakaotalk/kakaotalk_campaign.png %}){: style="max-width:30%" }

3. Sie können zusätzliche Varianten zu Ihrer Kampagne hinzufügen, sodass Sie verschiedene Nachrichtentypen und Layouts auswählen können. Weitere Informationen finden Sie unter [Multivariate und A/B-Tests](https://www.braze.com/docs/user_guide/messaging/ab_testing/).

{% endtab %}
{% tab Canvas %}

1. [Erstellen Sie Ihren Canvas](https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas/).
2. Fügen Sie einen Nachrichtenschritt im Canvas-Builder hinzu und wählen Sie **KakaoTalk**.

![Canvas-Messaging-Kanal-Auswahl.]({% image_buster /assets/img/kakaotalk/kakaotalk_canvas.png %})

{% endtab %}
{% endtabs %}

## 2. Schritt: Verfassen Sie Ihre KakaoTalk-Nachricht {#step-2-compose-your-kakaotalk-message}

1. Wählen Sie das Dropdown-Menü **KakaoTalk channel**, das eine Liste der KakaoTalk-Kanäle anzeigt, die Sie über die Technologie-Partner-Seite eingerichtet haben, und wählen Sie den KakaoTalk-Kanal aus, über den die Nachricht gesendet werden soll.
2. Wählen Sie den zu sendenden Nachrichtentyp:
- Text
- Bild
- Listenelement
    - Schmal
    - Breit

![KakaoTalk-Varianten-Bereich mit drei auswählbaren Nachrichtentypen.]({% image_buster /assets/img/kakaotalk/kakaotalk_variants.png %})

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
| Dateigröße | Bis zu 500kb |
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

Braze übernimmt automatisch alle Bild-Upload-Anforderungen von KakaoTalk. Das bedeutet, dass Sie Bilder **nicht** vor dem Senden von Nachrichten bei KakaoTalk-Anbietern hochladen müssen. Laden Sie einfach Bilder hoch und senden Sie die Nachricht direkt über Braze!

![Bereich mit ausgewählten Symbolen zum Hinzufügen eines schmalen Bildes.]({% image_buster /assets/img/kakaotalk/add_image.png %})

{% endtab %}
{% tab Listenelement %}


Eine KakaoTalk-Artikellisten-Nachricht ist dafür konzipiert, eine Liste von Inhaltselementen in einem übersichtlichen, vertikalen Format darzustellen.

Listenelement-Nachrichten bestehen aus einer Kopfzeile, einem Artikellisten-Bereich und einem optionalen Button-Bereich.

#### Spezifikationen

| Bereich | Spezifikationen |
| --- | --- |
| Artikelanzahl | Erfordert mindestens 2 oder 3 Artikel |
| Buttons | Bis zu 5 optionale Buttons |
| Kopfzeile | Bis zu 250 Zeichen |
| Artikeltitel | Bis zu 25 Zeichen |
| Website-URL (pro Artikel) | Bis zu 250 Zeichen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Spezifikationen" }

![Eine KakaoTalk-Listenelement-Nachricht.]({% image_buster /assets/img/kakaotalk/item_list.png %})

{% endtab %}
{% endtabs %}


## 3. Schritt: Klick-Tracking einrichten {#step-3-set-up-click-tracking}

Wenn das KakaoTalk-Klick-Tracking aktiviert ist, kürzt Braze automatisch Ihre URLs, fügt Tracking-Mechanismen hinzu und zeichnet Klicks in Echtzeit auf. Diese Daten ermöglichen es Ihnen, gezieltere Segmentierungs- und Retargeting-Strategien zu erstellen, z. B. Nutzer:innen basierend auf dem Klickverhalten zu segmentieren und Nachrichten als Reaktion auf bestimmte Klicks auszulösen.

Klick-Tracking wird für Text-, Bild- und Listenelement-Nachrichten unterstützt. Es unterstützt Links innerhalb von Buttons und Bild-Klick-Aktionen. Sie können URLs auch mit Liquid und benutzerdefinierten Domains personalisieren.

Um Klick-Tracking zu aktivieren, setzen Sie ein Häkchen bei **Click Tracking** im Abschnitt **Link options** des Composers. URLs werden mit der Standard-Braze-Domain (`https://brz.ai`) oder der für die Abo-Gruppe angegebenen benutzerdefinierten Domain gekürzt und für die Nutzer:innen personalisiert.

Ausführliche Informationen zu Klick-Tracking, benutzerdefinierten Domains, Liquid-Personalisierung in URLs, Reporting und Retargeting finden Sie unter [KakaoTalk-Klick-Tracking]({{site.baseurl}}/kakaotalk_click_tracking/).

### Nutzer:innen retargeten {#retargeting-users}

Sie können Nutzer:innen retargeten, die auf eine URL in einer KakaoTalk-Nachricht geklickt haben, indem Sie die folgenden Segmentierungsfilter und Trigger verwenden:

- Aktionsbasierte Trigger
    - Interact with Campaign
    - Interact with Step

- Segmentierungsfilter
    - Clicked/Opened Campaign
    - Clicked/Opened Campaign or Canvas with Tag
    - Clicked/Opened Step

## 4. Schritt: Vorschau und Test Ihrer KakaoTalk-Nachricht {#step-4-preview-and-test-your-kakaotalk-message}

Die Nachrichtenvorschau wird automatisch aktualisiert, während Sie Ihre KakaoTalk-Nachricht verfassen. Wenn Sie bereit zum Testen sind, gehen Sie zum Tab **Test**, um eine Testnachricht an Inhalts-Testgruppen oder einzelne Nutzer:innen zu senden, oder um die Nachricht als bestehende:r oder benutzerdefinierte:r Nutzer:in direkt in Braze in der Vorschau anzuzeigen.

Nachdem Sie Ihre Testnutzer:innen ausgewählt haben, wählen Sie **Send Test**. Eine Benachrichtigung zeigt die Ergebnisse Ihres Testversands an. Für CJ OliveNetworks erhalten Sie eine „C100“-Antwort. Wenn Sie einen anderen Fehler sehen, konsultieren Sie die [CJ KakaoTalk-Nutzerdokumentation](https://developers.kakao.com/docs/latest/en/index).

![Vorschaufenster für eine KakaoTalk-Nachricht.]({% image_buster /assets/img/kakaotalk/preview_message.png %})

{% alert note %}
Um eine Nachricht für bestehende Nutzer:innen in der Vorschau anzuzeigen und eine Testnachricht zu senden, benötigen Sie die Berechtigung „View PII“. Sie können eine Nachricht für benutzerdefinierte Nutzer:innen ohne diese Berechtigungen in der Vorschau anzeigen und als Test senden.
{% endalert %}

Um die Ergebnisse eines Versands zu überprüfen oder Probleme zu beheben, gehen Sie zu **Settings** > **Message Activity Log**. Weitere Informationen finden Sie unter [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/).

## 5. Schritt: Erstellen Sie den Rest Ihrer Kampagne oder Ihres Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

In den folgenden Abschnitten finden Sie Details dazu, wie Sie unsere Tools am besten zum Erstellen von KakaoTalk-Nachrichten nutzen können.

### Zustellungszeitplan oder Trigger wählen {#choose-delivery-schedule-or-trigger}

KakaoTalk-Nachrichten können basierend auf einem geplanten Zeitpunkt, einer Aktion oder einem API-Trigger zugestellt werden. Weitere Informationen zu Zeitplan- und Trigger-Optionen finden Sie unter [Ihre Kampagne planen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/) oder [Entry-Zeitplan-Typen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#entry-schedule-types) (für Ihren Canvas).

Sie können Zustellungs-Kontrollgruppen festlegen, z. B. Nutzer:innen erlauben, erneut für den Empfang der Kampagne berechtigt zu werden, oder Frequency-Capping-Regeln aktivieren. Für die aktionsbasierte Zustellung können Sie auch die Dauer der Kampagne und [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/) festlegen.

### Zielgruppe zusammenstellen {#choose-users-to-target}

Richten Sie Ihre Zielgruppe aus, indem Sie Segmente oder Filter auswählen, um Ihre Zielgruppe einzugrenzen. Derzeit kann KakaoTalk nur Freunde des Kanals anschreiben. Wir empfehlen, ein angepasstes Attribut zu setzen, um Kanalfreunde zu kennzeichnen, damit Sie Ihre Nutzer:innen richtig segmentieren und vermeiden, KakaoTalk-Nachrichten an Nutzer:innen zu senden, die diese nicht empfangen können.

### Konversions-Events wählen {#choose-conversion-events}

Braze ermöglicht es Ihnen zu verfolgen, wie oft Nutzer:innen bestimmte Aktionen (Konversions-Events) nach Erhalt einer Kampagne ausführen. Sie haben die Möglichkeit, ein Zeitfenster von bis zu 30 Tagen festzulegen, in dem eine Conversion gezählt wird, wenn die Nutzer:innen die angegebene Aktion ausführen.

Konversions-Events helfen Ihnen, den Erfolg Ihrer Kampagne zu messen. Wenn Sie beispielsweise versuchen, Nutzer:innen zur Nutzung Ihrer App zu bewegen, setzen Sie das Konversions-Event auf **Starts Session**.

Sie können auch benutzerdefinierte Konversions-Events basierend auf Ihrem spezifischen Anwendungsfall festlegen. Seien Sie kreativ und überlegen Sie, wie Sie den Erfolg Ihrer Kampagne messen möchten.

## 6. Schritt: Überprüfen und bereitstellen {#step-6-review-and-deploy}

Nachdem Sie den letzten Teil Ihrer Kampagne oder Ihres Canvas fertiggestellt haben, überprüfen Sie die Details, testen Sie alles und senden Sie ab!