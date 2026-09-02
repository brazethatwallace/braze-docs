---
nav_title: Kreativdetails
article_title: Kreativdetails für Content Cards
page_order: 2
description: "Dieser Artikel behandelt Kreativdetails wie Empfehlungen zur Bildgröße und das Verhalten beim Schließen der drei Standard-Content-Card-Typen."
channel:
  - content cards
tool: Media

---

# Kreativdetails für Content Cards {#creative-details-for-content-cards}

> Die Anpassung von Content Cards und des Feeds, in dem sie sich befinden, kann nicht während der Kampagnenerstellung vorgenommen werden – Sie müssen mit Ihren Entwickler:innen zusammenarbeiten, um Ihre Cards zu erstellen und anzupassen. Technische Details finden Sie in unserer [Entwickler:innen-Dokumentation]({{site.baseurl}}/developer_guide/getting_started/customization_overview).

## Content-Card-Typen {#content-card-types}

{% tabs %}
{% tab Klassisch %}

Die klassische Card eignet sich hervorragend für Standard-Nachrichten und -Benachrichtigungen oder auch zur visuellen Kategorisierung von Nachrichten mithilfe von Symbolen. Das Bild ist optional, muss aber ein Seitenverhältnis von 1:1 haben.

![Darstellung einer klassischen Card mit empfohlenen Details und ein Beispiel einer klassischen Card]({% image_buster /assets/img/content_card_classic.png %}){: width="1358" height="2871" style="max-width:45%;border:0;"}

| Card-Funktion | Details |
| --- | ---|
| Kopfzeilentext | 18 px; Fett <br> Eine Textzeile ist ideal. <br> Sie können hier Liquid verwenden, um Ihre Nachricht zu personalisieren. |
| Nachrichtentext | 13 px; Normale Schriftstärke <br> Zwei bis vier Textzeilen sind ideal. <br> Sie können hier Liquid verwenden, um Ihre Nachricht zu personalisieren. |
| Linktext | Optional. <br> 13&nbsp;px <br> Link zu einer Webseite oder Deeplink in Ihre App. |
| Bild | Optional. <br> Muss ein 1:1-Verhältnis haben. <br> Wir empfehlen eine Bildqualität von 60 x 60&nbsp;px. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content-Card-Typen" }

{% endtab %}
{% tab Bild mit Beschriftung %}

Die Card „Bild mit Beschriftung“ ist eine großartige Möglichkeit, wichtige Inhalte wie eine große Aktion oder ein neues App-Feature hervorzuheben und Aufmerksamkeit zu erregen.

![Darstellung einer Card mit beschriftetem Bild mit empfohlenen Details und ein Beispiel einer Card mit beschriftetem Bild]({% image_buster /assets/img/content_card_captioned.png %}){: width="2880" height="2877" style="max-width:90%;border:0;"}

| Card-Funktion | Details |
| --- | ---|
| Kopfzeilentext | 18 px; Fett <br> Eine Textzeile ist ideal. <br> Sie können hier Liquid verwenden, um Ihre Nachricht zu personalisieren. |
| Nachrichtentext | 13 px; Normale Schriftstärke <br> Zwei bis vier Textzeilen sind ideal. <br> Sie können hier Liquid verwenden, um Ihre Nachricht zu personalisieren. |
| Linktext | Optional. <br> 13&nbsp;px <br> Link zu einer Webseite oder Deeplink in Ihre App. |
| Bild | Empfohlenes Seitenverhältnis 4:3. <br> Mindestbreite 600&nbsp;px. <br> Unterstützt hochauflösende PNG-, JPEG- und GIF-Dateien. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content-Card-Typen" }

{% endtab %}
{% tab Nur Bild %}

Wenn Sie mehr kreative Kontrolle wünschen, ist die Card „Nur Bild“ genau das Richtige für Sie. Erstellen Sie Ihr Bild mit einem beliebigen Tool und laden Sie es in diesen Card-Typ hoch.

![Darstellung einer Content-Card „Nur Bild“ mit empfohlenen Details und ein Beispiel einer reinen Bild-Card]({% image_buster /assets/img/content_card_banner.png %}){: width="1358" height="2871" style="max-width:45%;border:0;"}

| Card-Funktion | Details |
| --- | ---|
| Verlinkte Card | Optional. <br> 13&nbsp;px <br> Klickverhalten verlinkt zu einer Webseite oder einem Deeplink in Ihre App. |
| Bild | Jedes Seitenverhältnis wird unterstützt. <br> Mindestbreite 600&nbsp;px. <br> Unterstützt hochauflösende PNG-, JPEG- und GIF-Dateien. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content-Card-Typen" }

{% endtab %}
{% endtabs %}

## Allgemeine Kreativdetails {#general}

Content Cards unterstützen standardmäßig Text und Bilder, einschließlich GIFs. Derzeit können angepasste Stile für die Card, wie z. B. verschiedene Schriftfarben oder mehrere Bilder, nicht im Dashboard vorgenommen werden. Sie können Ihre Content Cards und den Feed während der Integration individuell gestalten. Weitere Details finden Sie unter [Cards anpassen]({{site.baseurl}}/developer_guide/content_cards/customizing_cards) für das Braze SDK.

### Verhalten beim Schließen {#dismissal-behavior}

Um eine Card zu schließen, können Nutzer:innen sie auf dem Mobilgerät wegwischen oder die `close X`-Funktion verwenden, wie im folgenden Screenshot gezeigt. Das `x` erscheint beim Hovern nur im Web-SDK.

![Bild, das das Wisch- oder Schließ-Verhalten für eine Card zeigt]({% image_buster /assets/img/dismissal-cc.png %}){: width="1800" height="504"}

Wenn Nutzer:innen alle ihre Cards geschlossen haben oder Sie keine neuen Updates gesendet haben, sieht der Feed der Nutzer:innen normalerweise so aus:

![Bild eines leeren Content-Card-Feeds]({% image_buster /assets/img/empty-cc.png %}){: width="832" height="1478" style="max-width:45%"}

{% alert tip %}
Halten Sie Content Cards relevant, indem Sie sie so einstellen, dass sie geschlossen werden, wenn Nutzer:innen relevante Aktionen ausführen. Stellen Sie z. B. Werbe-Content-Cards so ein, dass sie geschlossen werden, sobald Nutzer:innen einen Kauf tätigen, damit sie nicht weiterhin ein Angebot für etwas sehen, das sie bereits gekauft haben.
{% endalert %}

### GIFs in Content Cards verwenden {#using-gifs-in-content-cards}

| Content Cards für Android | Content Cards für iOS | Content Cards für Web |
| --- | --- |---|
| Das Android-SDK bietet standardmäßig keine Unterstützung für animierte GIFs. Weitere Details zur Aktivierung der GIF-Unterstützung finden Sie unter [GIFs]({{site.baseurl}}/developer_guide/content_cards/embedding_gifs?sdktab=android). | Das Swift-SDK bietet standardmäßig keine Unterstützung für animierte GIFs. Weitere Details zur Aktivierung der GIF-Unterstützung finden Sie im [GIF-Support-Tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support). | GIF-Unterstützung ist standardmäßig in der Web-SDK-Integration enthalten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="GIFs in Content Cards verwenden" }