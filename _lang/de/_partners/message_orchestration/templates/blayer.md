---
nav_title: B.Layer
article_title: B.Layer
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und B.Layer, einem In-App-Nachrichten-Builder, mit dem Sie einfach, schnell und ohne Code angepasste In-App-Nachrichten erstellen können."
alias: /partners/blayer-inapps/
page_type: partner
search_tag: Partner

---

# B.Layer

> [B.Layer](https://blayer.phiture.com) ist der In-App-Nachrichten-Builder von Phiture, mit dem CRM-Teams für mobile Apps einfach, schnell und ohne Programmieraufwand angepasste In-App-Nachrichten erstellen können.

_Diese Integration wird von B.Layer gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und B.Layer erlaubt es Ihnen, den B.Layer In-App-Nachrichten-Builder zu verwenden, um markengerechte In-App-Nachrichten zu erstellen, die als ZIP-Datei oder Inline-HTML nach Braze exportiert werden können. Diese Integration erfordert keine zusätzlichen Entwickler:innen-Ressourcen, wodurch Sie Zeit und Budget sparen.

![]({% image_buster /assets/img/blayer/blayer2.png %})

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| B.Layer-Konto | Ein [B.Layer](https://blayer.phiture.com)-Konto ist erforderlich, um die Vorteile dieser Partnerschaft zu nutzen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Anwendungsfälle {#use-cases}

Mit B.Layer gibt es unendlich viele Möglichkeiten zum Erstellen und Experimentieren, darunter Schieberegler für Produktempfehlungen, mehrstufiges Onboarding oder Umfragen, NPS, E-Mail-Erfassung, Sonderangebote und vieles mehr.

Sie arbeiten mit Marken wie Lifesum, Blinkist, OnX Hunt und vielen anderen zusammen, um deren Nutzererlebnis ohne zusätzliche Ressourcen zu verbessern. Wir gehören außerdem zu den Finalisten der APS Awards 2022 in der Kategorie App-Innovation.

## Integration

### 1. Schritt: Erstellen Sie Ihre In-App-Nachricht {#step-1-create-your-in-app-message}

#### Markenfarben und Schriftarten festlegen {#set-brand-colors-and-fonts}

Klicken Sie in B.Layer im Hamburger-Menü oben auf der Seite auf **Brand assets > add your brand assets**. Hier können Sie Ihre Markenfarben und Schriftarten zuweisen.
Damit sind Sie startklar. Jetzt können Sie mit der Gestaltung Ihrer In-App-Nachricht beginnen.

![]({% image_buster /assets/img/blayer/blayer4.png %})

#### Gestalten Sie Ihre In-App-Nachricht {#design-your-in-app-message}

Um Ihre In-App-Nachricht zu gestalten, wählen Sie eine einzelne In-App-Nachricht aus. Anschließend gestalten Sie Ihre Nachricht und fügen die benötigten Komponenten hinzu. Jede Komponente kann angepasst werden.

![]({% image_buster /assets/img/blayer/blayer5.png %})

### In-App-Nachricht herunterladen {#download-your-in-app-message}

Sobald Sie fertig sind, laden Sie Ihre Nachricht herunter. Ihre Nachricht kann als ZIP- oder Inline-HTML-Datei heruntergeladen werden.

### 2. Schritt: Angepassten B.Layer-Code hinzufügen {#step-2-add-blayer-custom-code}

Erstellen Sie in Braze eine In-App-Nachricht mit angepasstem Code. Wenn Sie eine ZIP-Datei haben, ziehen Sie sie per Drag-and-Drop in das Feld über dem Code-Bereich. Wenn Sie eine Inline-HTML-Datei haben, fügen Sie das Inline-HTML in den HTML-Bereich ein.

![]({% image_buster /assets/img/blayer/blayer6.png %})

## Button-Tracking

Mit B.Layer können Sie Button-Interaktionen oder Texteingaben als Braze-Attribut protokollieren. Das können Sie direkt im Editor erledigen. Ein beliebtes Beispiel ist eine NPS-Umfrage.

B.Layer verwendet das Braze-Button-Tracking, das zu den von Ihnen eingegebenen Links hinzugefügt wird (z. B. `?button=0`). Auf diese Weise können Sie die Button-Klicks im Analytics-Bereich Ihrer Campaign sehen.