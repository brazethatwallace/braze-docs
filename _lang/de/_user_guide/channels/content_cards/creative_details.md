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

> Die Anpassung von Content Cards und des Feeds, in dem sie sich befinden, kann nicht während der Kampagnenerstellung vorgenommen werden – Sie müssen mit Ihren Entwickler:innen zusammenarbeiten, um Ihre Cards zu erstellen und anzupassen. Technische Details finden Sie in unserer [Entwickler:innen-Dokumentation]({{site.baseurl}}/developer_guide/getting_started/customization_overview/).

## Content-Card-Typen {#content-card-types}

{% tabs %}
{% tab Klassisch %}

Die klassische Card eignet sich hervorragend für Standard-Nachrichten und Benachrichtigungen oder auch zur visuellen Kategorisierung von Nachrichten mit Icons. Das Bild ist optional, muss aber ein Seitenverhältnis von 1:1 haben.

![Bild einer klassischen Card mit empfohlenen Details und einem Beispiel für eine klassische Card]({% image_buster /assets/img/content_card_classic.png %}){: style="max-width:45%;border:0;"}

| Card-Eigenschaft | Details |
| --- | ---|
| Überschrift | 18px; Fett <br> Eine Textzeile ist ideal. <br> Sie können hier Liquid verwenden, um Ihre Nachricht zu personalisieren. |
| Nachrichtentext | 13px; Normale Schriftstärke <br> Zwei bis vier Textzeilen sind ideal. <br> Sie können hier Liquid verwenden, um Ihre Nachricht zu personalisieren. |
| Linktext | Optional. <br> 13&nbsp;px <br> Link zu einer Webseite oder Deeplink innerhalb Ihrer App. |
| Bild | Optional. <br> Muss ein Seitenverhältnis von 1:1 haben. <br> Wir empfehlen eine Bildqualität von 60 x 60&nbsp;px. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content-Card-Typen" }

{% endtab %}
{% tab Captioned Image %}

Die Captioned-Image-Card ist eine großartige Möglichkeit, wichtige Inhalte hervorzuheben und Aufmerksamkeit zu erregen, z. B. für einen großen Sale oder ein neues App-Feature.

![Bild einer Captioned-Image-Card mit empfohlenen Details und einem Beispiel für eine Captioned-Image-Card]({% image_buster /assets/img/content_card_captioned.png %}){: style="max-width:90%;border:0;"}

| Card-Eigenschaft | Details |
| --- | ---|
| Überschrift | 18px; Fett <br> Eine Textzeile ist ideal. <br> Sie können hier Liquid verwenden, um Ihre Nachricht zu personalisieren. |
| Nachrichtentext | 13px; Normale Schriftstärke <br> Zwei bis vier Textzeilen sind ideal. <br> Sie können hier Liquid verwenden, um Ihre Nachricht zu personalisieren. |
| Linktext | Optional. <br> 13&nbsp;px <br> Link zu einer Webseite oder Deeplink innerhalb Ihrer App. |
| Bild | Empfohlenes Seitenverhältnis 4:3. <br> Mindestbreite 600&nbsp;px. <br> Unterstützt hochauflösende PNG-, JPEG- und GIF-Dateien. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content-Card-Typen" }

{% endtab %}
{% tab Nur Bild %}

Wenn Sie mehr kreative Kontrolle wünschen, ist die Image-only-Card genau das Richtige für Sie. Erstellen Sie Ihr Bild mit einem beliebigen Tool und laden Sie es in diesen Card-Typ hoch.

![Bild einer Image-only-Content-Card mit empfohlenen Details und einem Image-only-Beispiel]({% image_buster /assets/img/content_card_banner.png %}){: style="max-width:45%;border:0;"}

| Card-Eigenschaft | Details |
| --- | ---|
| Verlinkte Card | Optional. <br> 13&nbsp;px <br> Klick-Verhalten verlinkt auf eine Webseite oder einen Deeplink innerhalb Ihrer App. |
| Bild | Jedes Seitenverhältnis wird unterstützt. <br> Mindestbreite 600&nbsp;px. <br> Unterstützt hochauflösende PNG-, JPEG- und GIF-Dateien. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content-Card-Typen" }

{% endtab %}
{% endtabs %}

## Allgemeine Kreativdetails {#general}

Content Cards unterstützen standardmäßig Text und Bilder, einschließlich GIFs. Derzeit können angepasste Stile für die Card, wie z. B. verschiedene Schriftfarben oder mehrere Bilder, nicht im Dashboard vorgenommen werden. Sie können Ihre Content Cards und den Feed während der Integration individuell gestalten. Weitere Details finden Sie unter [Cards anpassen]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/) für das Braze SDK.

### Verhalten beim Schließen {#dismissal-behavior}

Um eine Card zu schließen, können Nutzer:innen sie auf dem Mobilgerät wegwischen oder die `close X`-Funktion verwenden, wie im folgenden Screenshot gezeigt. Das `x` erscheint beim Hovern nur im Web-SDK.

![Bild, das das Wisch- oder Schließ-Verhalten für eine Card zeigt]({% image_buster /assets/img/dismissal-cc.png %})

Wenn Nutzer:innen alle ihre Cards geschlossen haben oder Sie keine neuen Updates gesendet haben, sieht der Feed der Nutzer:innen normalerweise so aus:

![Bild eines leeren Content-Card-Feeds]({% image_buster /assets/img/empty-cc.png %}){: style="max-width:45%"}

{% alert tip %}
Halten Sie Content Cards relevant, indem Sie sie so einstellen, dass sie geschlossen werden, wenn Nutzer:innen relevante Aktionen ausführen. Stellen Sie z. B. Werbe-Content-Cards so ein, dass sie geschlossen werden, sobald Nutzer:innen einen Kauf tätigen, damit sie nicht weiterhin ein Angebot für etwas sehen, das sie bereits gekauft haben.
{% endalert %}

### GIFs in Content Cards verwenden {#using-gifs-in-content-cards}

| Content Cards für Android | Content Cards für iOS | Content Cards für Web |
| --- | --- |---|
| Das Android-SDK bietet standardmäßig keine Unterstützung für animierte GIFs. Weitere Details zur Aktivierung der GIF-Unterstützung finden Sie unter [GIFs]({{site.baseurl}}/developer_guide/content_cards/embedding_gifs/?sdktab=android). | Das Swift-SDK bietet standardmäßig keine Unterstützung für animierte GIFs. Weitere Details zur Aktivierung der GIF-Unterstützung finden Sie im [GIF-Support-Tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support). | GIF-Unterstützung ist standardmäßig in der Web-SDK-Integration enthalten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="GIFs in Content Cards verwenden" }