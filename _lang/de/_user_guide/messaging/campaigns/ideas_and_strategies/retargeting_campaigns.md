---
nav_title: Retargeting von Kampagnen
article_title: Retargeting von Kampagnen
page_order: 2
page_type: reference
description: "Dieser Referenzartikel erläutert, wie und warum Sie Retargeting von Kampagnen basierend auf Nachrichten, die Ihre Nutzer:innen erhalten, in Betracht ziehen sollten."
tool:
  - Campaigns

---

# Retargeting von Kampagnen {#retarget-campaigns}

> Durch das Retargeting von Kampagnen basierend auf früheren Aktionen der Nutzer:innen – zum Beispiel ob sie eine E-Mail geöffnet haben oder nicht – können Sie Ihre Nutzer:innen neu klassifizieren und den Weg für einen effektiven, datengestützten Marketing-Ansatz ebnen.

Braze bietet Support für das Retargeting von Nutzer:innen basierend auf Nachrichten, die sie erhalten haben. Sie können Nutzer:innen anhand ihrer Interaktionen mit Ihren Kampagnen und Canvase retargeten.

Jeder dieser Retargeting-Filter bietet Ihnen nach dem Hinzufügen mehrere Optionen. Weitere Informationen zum Targeting von Nutzer:innen finden Sie in unserem [Braze-Lernkurs](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) zur Kampagneneinrichtung!

![Abschnitt „Segment Details“ mit dem Dropdown-Menü für die verfügbaren Filter.]({% image_buster /assets/img_archive/retarget.png %}){: style="max-width:80%;"}

## Retargeting-Filter {#retargeting-filters}

Sie können die Retargeting-Filter in diesem Abschnitt für Ihre Nutzer:innen innerhalb Ihrer Kampagnen und Canvase verwenden.

### Kampagne angeklickt/geöffnet {#clickedopened-campaign}

Verwenden Sie diesen Filter, um Nutzer:innen zu finden, die Folgendes getan oder nicht getan haben:

- Eine E-Mail angeklickt
- Eine In-App-Nachricht angeklickt
- Eine Push-Benachrichtigung direkt geöffnet
- Eine E-Mail geöffnet
- Eine In-App-Nachricht angesehen

![Filter „Kampagne angeklickt/geöffnet“ mit Optionen für Kanalinteraktionen.]({% image_buster /assets/img_archive/clickedopened.png %})

Dies kann weiter spezifiziert werden, indem Sie auswählen, welche Kampagne Sie retargeten möchten.

### Kampagne oder Canvas mit Tag angeklickt oder geöffnet {#clicked-or-opened-campaign-or-canvas-with-tag}

Verwenden Sie diesen Filter, um Nutzer:innen zu finden, die mit Kampagnen oder Canvase mit einem bestimmten Tag interagiert haben oder nicht:

- Eine E-Mail angeklickt
- Eine In-App-Nachricht angeklickt
- Eine Push-Benachrichtigung direkt geöffnet
- Eine E-Mail geöffnet
- Eine In-App-Nachricht angesehen

![Filter „Kampagne oder Canvas mit Tag angeklickt oder geöffnet“.]({% image_buster /assets/img_archive/retarget_tag_filter.png %})

### Aus Kampagne konvertiert {#converted-from-campaign}

Verwenden Sie diesen Filter, um Nutzer:innen zu finden, die in Ihrer Zielkampagne konvertiert haben oder nicht (basierend auf der primären Konversion).

Bei wiederkehrenden Kampagnen bezieht sich dieser Filter darauf, ob Nutzer:innen bei der letzten Nachricht der Kampagne konvertiert haben.

![Filter „Aus Kampagne konvertiert“ mit Kampagnenauswahl.]({% image_buster /assets/img_archive/converted_from_campaign.png %})

### Aus Canvas konvertiert {#converted-from-canvas}

Verwenden Sie diesen Filter, um Nutzer:innen zu finden, die in Ihrem Ziel-Canvas konvertiert haben oder nicht (basierend auf der primären Konversion).

Bei wiederkehrenden Canvase bezieht sich dieser Filter darauf, ob Nutzer:innen jemals konvertiert haben, wenn sie den Canvas durchlaufen haben.

![Filter „Aus Canvas konvertiert“ mit Canvas-Auswahl.]({% image_buster /assets/img_archive/converted_from_canvas.png %})

### In Kampagnen-Kontrollgruppe {#in-campaign-control-group}

Verwenden Sie diesen Filter, um Nutzer:innen zu finden, die in der Kontrollgruppe Ihrer Zielkampagne sind oder nicht.

![Filter „In Kampagnen-Kontrollgruppe“ mit Kampagnenauswahl.]({% image_buster /assets/img_archive/campaign_control_group.png %})

### In Canvas-Kontrollgruppe {#in-canvas-control-group}

Verwenden Sie diesen Filter, um Nutzer:innen zu finden, die in der Kontrollgruppe Ihres Ziel-Canvas sind oder nicht. Der Canvas kann im Dropdown ausgewählt werden.

![Filter „In Canvas-Kontrollgruppe“ mit Canvas-Auswahl.]({% image_buster /assets/img_archive/canvas_control_group.png %})

### Letzte Nachricht von bestimmter Kampagne erhalten {#last-received-message-from-specific-campaign}

Verwenden Sie diesen Filter, um Nutzer:innen zu finden, die zuletzt eine bestimmte Kampagne vor oder nach einem bestimmten Datum oder einer bestimmten Anzahl von Tagen erhalten haben. Dieser Filter berücksichtigt nicht, wann Nutzer:innen andere Kampagnen erhalten haben.

{% multi_lang_include audience/segments.md section='same channel identifier' %}

![Filter „Letzte Nachricht von bestimmter Kampagne erhalten“ mit Datumsoptionen.]({% image_buster /assets/img_archive/last_received_specific_campaign.png %})

### Letzte Nachricht von Kampagne oder Canvas mit Tag erhalten {#last-received-message-from-campaign-or-canvas-with-tag}

Verwenden Sie diesen Filter, um Nutzer:innen zu finden, die zuletzt eine Kampagne oder einen Canvas mit einem bestimmten Tag vor oder nach einem bestimmten Datum oder einer bestimmten Anzahl von Tagen erhalten haben. Dieser Filter berücksichtigt nicht, wann Nutzer:innen andere Kampagnen oder Canvase erhalten haben.

![Filter „Letzte Nachricht von Kampagne oder Canvas mit Tag erhalten“.]({% image_buster /assets/img_archive/last_received_campaign_with_tag.png %})

### Nachricht von Kampagne erhalten {#received-message-from-campaign}

Verwenden Sie diesen Filter, um Nutzer:innen zu finden, die Ihre Zielkampagne erhalten haben oder nicht.

{% multi_lang_include audience/segments.md section='same channel identifier' %}

![Filter „Nachricht von Kampagne erhalten“ mit Kampagnenauswahl.]({% image_buster /assets/img_archive/receivedcamp.png %})

### Nachricht von Kampagne oder Canvas mit Tag erhalten {#received-message-from-campaign-or-canvas-with-tag}

Verwenden Sie diesen Filter, um Nutzer:innen zu finden, die eine Kampagne oder einen Canvas mit Ihrem Ziel-Tag erhalten haben oder nicht.

![Filter „Nachricht von Kampagne oder Canvas mit Tag erhalten“.]({% image_buster /assets/img_archive/received_campaign_with_tag.png %})

## Vorteile des Retargetings von Kampagnen {#advantages-with-retargeting-campaigns}

Retargeting ist besonders effektiv, wenn das ursprüngliche Segment auch eine bestimmte Aktion enthielt, die Nutzer:innen ausführen sollen. Nehmen wir zum Beispiel an, Sie haben eine Card, die sich an Nutzer:innen richtet, die noch nie einen Kauf getätigt haben. Die Card bewirbt eine Aktion für einen vergünstigten In-App-Kauf. Das ursprüngliche Segment sieht folgendermaßen aus:

- In der App ausgegebenes Geld ist genau 0
- App zuletzt vor weniger als 14 Tagen verwendet

Die Gesamtzahl der Nutzer:innen im Segment beträgt 100.000, und aus der Content-Card-Statistik wissen Sie, dass 60.000 eindeutige Nutzer:innen die Card angesehen und 20.000 eindeutige Nutzer:innen die Card angeklickt haben. Über den Segmenter können wir sehen, wie viele der Nutzer:innen, die die Card angeklickt haben, tatsächlich einen Kauf getätigt haben:

- In der App ausgegebenes Geld ist mehr als 0
- Angeklickte Card ist Name der Card

Nach der Auswertung dieser Statistiken können wir ein Segment von Nutzer:innen erstellen, die die Card angeklickt, aber keinen Kauf getätigt haben:

- In der App ausgegebenes Geld ist genau 0
- Angeklickte Card ist Name der Card

Wir können dieses Segment mit zusätzlichem Messaging rund um die Aktion oder einen anderen In-App-Kauf retargeten. Retargeting kann mit einer Messaging-Kampagne durchgeführt werden. Ein Multichannel-Ansatz ermöglicht es Ihnen, Nutzer:innen dort zu erreichen, wo sie am wahrscheinlichsten reagieren, und so die Effektivität Ihrer Kampagnen zu steigern.