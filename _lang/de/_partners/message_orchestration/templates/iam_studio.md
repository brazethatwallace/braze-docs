---
nav_title: IAM Studio
article_title: IAM Studio
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und IAM Studio, einer Plattform zur Personalisierung von Nachrichten, die es Ihnen erlaubt, personalisierte, reichhaltige In-App-Erlebnisse zu erstellen und diese über Braze zuzustellen."
alias: /partners/iam_studio/
page_type: partner
search_tag: Partner

---

# IAM Studio

> [IAM Studio](https://www.inappmessage.com) ist eine No-Code-Plattform zur Personalisierung von Nachrichten, die es Ihnen erlaubt, personalisierte, reichhaltige In-App-Erlebnisse zu erstellen und diese über Braze zuzustellen.

_Diese Integration wird von IAM Studio gepflegt._

## Über die Integration {#about-the-integration}

Mit der Integration von Braze und IAM Studio können Sie ganz einfach anpassbare In-App-Nachrichtentemplates in Ihre Braze In-App-Nachrichten einfügen. Dazu gehören Bildersatz, Textänderung, Deeplink-Einstellungen, angepasste Attribute und Ereigniseinstellungen. Mit IAM Studio können Sie die Produktionszeit für Nachrichten reduzieren und mehr Zeit für die Planung von Inhalten aufwenden.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| IAM Studio-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [IAM Studio-Konto](https://www.inappmessage.com/register). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

- Anregung zum Kauf von Waren
- Sammlung von Nutzerinformationen
- Steigerung der Mitgliederregistrierungen
- Informationen zur Ausgabe von Kupons

## Integration

### 1. Schritt: Template auswählen {#step-1-choose-a-template}

Wählen Sie ein Template für In-App-Nachrichten aus der Galerie der In-App-Nachrichtentemplates aus, das Sie verwenden möchten.

![Die IAM Studio Template-Galerie zeigt verschiedene Templates wie „Carousel Slide Modal“, „Simple Icon Modal“, „Modal Full Image“ und mehr.]({% image_buster /assets/img/iam_studio/iam_template_gallery.png %})

### 2. Schritt: Template anpassen {#step-2-customize-the-template}

Passen Sie zunächst das Bild, den Text und den Button für Ihren Inhalt an. Stellen Sie sicher, dass Sie **Deeplink** für das Bild und den Button verbinden.

{% tabs local %}
{% tab Image %}
![Das IAM Studio UI zeigt die Optionen zum Anpassen des Bildes. Diese Optionen umfassen das Bild, den Bildradius und das abgeblendete Bild.]({% image_buster /assets/img/iam_studio/iam_customize_image.png %})
{% endtab %}
{% tab Text %}
![Das IAM Studio UI zeigt die Optionen zum Anpassen des Titels und des Untertitels Ihrer Nachricht. Diese Optionen umfassen Text, Formatierung und Schriftart.]({% image_buster /assets/img/iam_studio/iam_customize_text.png %})
{% endtab %}
{% tab Button %}
![Das IAM Studio UI zeigt die Optionen zum Anpassen des Haupt-, linken und rechten Buttons. Zu diesen Optionen gehören Farbe, Deeplink, Text und Formatierung.]({% image_buster /assets/img/iam_studio/iam_customize_button.png %})
{% endtab %}
{% endtabs %}

Als Nächstes erstellen Sie Ihre personalisierte In-App-Nachricht, indem Sie angepasste Schriftarten hinzufügen und Liquid-Tags verwenden. Um die Protokollierung und das Tracking zu aktivieren, wählen Sie **Log data and track user behavior**.

{% tabs local %}
{% tab Fonts %}
![Das IAM Studio UI zeigt die Optionen zum Hinzufügen von Liquid. Zu diesen Optionen gehört die Erstellung personalisierter Sätze.]({% image_buster /assets/img/iam_studio/iam_custom_font.png %})
{% endtab %}
{% tab Liquid %}
![Das IAM Studio UI zeigt die Optionen zur Anpassung der Ereignis-/Attribut-Protokollierung. Diese Optionen beinhalten die Protokollierung des Nutzerverhaltens.]({% image_buster /assets/img/iam_studio/iam_liquid.png %})
{% endtab %}
{% tab Logging and Tracking %}
![Das IAM Studio UI zeigt die Optionen zum Anpassen der Schriftart. Zu diesen Optionen gehört, dass Nutzer:innen den Schriftstil anpassen können.]({% image_buster /assets/img/iam_studio/iam_tracking_logging.png  %})
{% endtab %}
{% endtabs %}

### 3. Schritt: Template exportieren {#step-3-export-the-template}

Wenn Sie alle Bearbeitungen abgeschlossen haben, exportieren Sie das Template, indem Sie auf **Export** klicken. Nach dem Exportieren wird der HTML-Code für die In-App-Nachricht generiert. Kopieren Sie diesen Code, indem Sie auf den Button **Copy code** klicken.

![IAM Studio Exportdialog mit generiertem In-App-Nachrichten-HTML und der Aktion „Code kopieren“.]({% image_buster /assets/img/iam_studio/export_iam_code.png %}){: style="max-width:45%;"}

### 4. Schritt: Code in Braze verwenden {#step-4-use-code-in-braze}

Navigieren Sie zu Braze, und fügen Sie in Ihrer In-App-Nachricht den angepassten Code in das **HTML Input**-Feld ein. Testen Sie Ihre Nachricht, um sicherzustellen, dass sie korrekt angezeigt wird.

![Braze In-App-Nachrichten-Campaign-Editor mit eingefügtem IAM Studio HTML im HTML-Input-Feld.]({% image_buster /assets/img/iam_studio/braze_campaign_editor.png %}){: style="max-width:85%;"}