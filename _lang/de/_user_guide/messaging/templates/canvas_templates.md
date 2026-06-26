---
nav_title: Canvas-Templates
article_title: Ein Canvas-Template erstellen
page_order: 2
alias: "/canvas_templates/"
description: "Erstellen und verwalten Sie wiederverwendbare Canvas-Templates oder starten Sie mit vorgefertigten Braze-Templates für gängige Anwendungsfälle."
---

# Ein Canvas-Template erstellen {#create-a-canvas-template}

> Dieser Referenzartikel beschreibt, wie Sie Templates für Canvas erstellen und verwalten. Die Verwendung von Templates kann Ihr Messaging verfeinern, indem ein konsistentes Framework erstellt wird, das einfach an Ihre spezifischen Ziele in Ihren Canvases angepasst werden kann.

{% alert tip %}
Sparen Sie Zeit und optimieren Sie Ihre Canvas-Erstellung mit [Braze-Canvas-Templates](#available-braze-templates)! Durchsuchen Sie unsere Bibliothek vorgefertigter Templates, um eines zu finden, das zu Ihrem Anwendungsfall passt, und passen Sie es an Ihre spezifischen Anforderungen an.
{% endalert %}

## Methode 1: Aus einem bestehenden Canvas erstellen {#method-1-create-from-an-existing-canvas}

### 1. Schritt: Wählen Sie Ihr bestehendes Canvas aus {#step-1-select-your-existing-canvas}

Gehen Sie im Braze-Dashboard zu **Messaging** > **Canvas** und wählen Sie ein bestehendes Canvas aus, das Sie als Template verwenden möchten.

### 2. Schritt: Erstellen Sie Ihr Template {#step-2-create-your-template}

Wählen Sie im Canvas-Editor **Canvas bearbeiten** oder **Entwurf bearbeiten**, je nachdem, ob Ihr Canvas aktiv ist oder sich im Entwurf befindet. Erweitern Sie das Dropdown **Als Entwurf speichern** in der Fußzeile und wählen Sie **Als Template speichern**.


### 3. Schritt: Speichern Sie Ihr Template {#step-3-save-your-template}

Geben Sie Ihrem Template als Nächstes einen Namen und fügen Sie relevante Tags hinzu. Wählen Sie dann **Save**. Ihr Template ist jetzt einsatzbereit, um ein Canvas zu erstellen, und gibt Ihnen einen Vorsprung, da die grundlegenden Einstellungen und Schritte bereits vorhanden sind.

## Methode 2: Über den Canvas-Template-Editor erstellen {#method-2-create-via-canvas-template-editor}

### 1. Schritt: Gehen Sie zum Canvas-Template-Editor {#step-1-go-to-the-canvas-template-editor}

Gehen Sie im Braze-Dashboard zu **Inhalt** > **Canvas**.

### 2. Schritt: Erstellen Sie ein neues Template {#step-2-create-a-new-template}

Wählen Sie **Template erstellen** und beginnen Sie mit der Einrichtung Ihrer Canvas-Details. Sie können damit beginnen, Ihrem Canvas-Template einen Namen zu geben.

![Ein Beispiel für ein Canvas-Template mit dem Namen „Annual sale Canvas template“ und der Beschreibung „Use for annual spring promotion“.]({% image_buster /assets/img/canvas_template_example.png %})

### 3. Schritt: Passen Sie Ihr Template an {#step-3-customize-your-template}

Passen Sie als Nächstes Ihr Template an, indem Sie [Ihr Canvas einrichten]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-2-build-your-canvas). Sie können entscheiden, wann Nutzer:innen das Canvas betreten sollen, festlegen, welche Nutzer:innen dieses Canvas betreten können, Ihre Sendeeinstellungen anpassen und die User-Journey für das Template erstellen.

### 4. Schritt: Speichern Sie Ihr Template {#step-4-save-your-template}

Nachdem Sie Ihr Template fertig angepasst haben, wählen Sie den Button **Template speichern**. Auf der Seite **Canvas-Template** können Sie die Details Ihres Canvas-Templates anzeigen, indem Sie <i class="fas fa-list"></i> **Template-Details** auswählen.

## Canvas-Templates verwenden {#using-canvas-templates}

Es gibt zwei Möglichkeiten, Ihr Template beim Erstellen eines Canvas zu verwenden:

- **Über Messaging**: Gehen Sie zu **Messaging** > **Canvas**. Wählen Sie den Button **Canvas erstellen** und dann **Canvas-Template verwenden**.
- **Über Inhalt**: Gehen Sie zu **Inhalt** > **Canvas** und suchen Sie Ihr gewünschtes Template unter **Canvas-Templates**. Wählen Sie dann das Menü <i class="fas fa-ellipsis-vertical"></i> und anschließend **Template anwenden**. Dadurch gelangen Sie zu einem neuen Canvas, bei dem das Template im Canvas-Composer angewendet wurde.

### Verfügbare Braze-Templates {#available-braze-templates}

Eine Liste der verfügbaren Canvas-Templates finden Sie unter [Braze-Canvas-Templates]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates/). Details zur Verwendung von E-Commerce-Canvas-Templates finden Sie unter [So verwenden Sie empfohlene E-Commerce-Events]({{site.baseurl}}/ecommerce_use_cases/).

## Canvas-Templates verwalten {#managing-canvas-templates}

Canvas-Templates können dupliziert und archiviert werden, ähnlich wie ein tatsächliches Canvas. Um ein Canvas-Template zu bearbeiten, wählen Sie das Template und dann **<i class="fas fa-pencil-alt"></i>Bearbeiten**.

Auf Workspace-Ebene können Sie Berechtigungen für Nutzer:innen aktualisieren, um den Zugriff zum Erstellen, Bearbeiten, Anzeigen oder Archivieren von Canvas-Templates zu erlauben oder einzuschränken.

### Berechtigungen für Teams und Workspaces {#permissions-for-teams-and-workspaces}

Um nur bestimmten Nutzer:innen den Zugriff auf und die Verwendung bestimmter Canvas-Templates zu ermöglichen, [fügen Sie ein Team]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) zu den Templates hinzu und weisen Sie dann die Team-Berechtigung „Zugriff auf Campaigns, Canvases, Content Cards, Content Blocks, Feature-Flags, Segments, Medienbibliothek und Präferenzzentrum“ zu.

Wenn Sie eine der folgenden Berechtigungen auf Team-Ebene, aber nicht auf Workspace-Ebene zuweisen, können Sie nur Folgendes tun, das Ihrem Team zugewiesen ist:

- Canvas-Templates erstellen und bearbeiten
- Canvas-Templates anzeigen
- Canvas-Templates archivieren

Wenn Berechtigungen sowohl auf Workspace- als auch auf Team-Ebene gewährt werden, haben die Berechtigungen auf Workspace-Ebene Vorrang.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Kann ich einen unvollständigen Schritt in einem Canvas-Template speichern? {#can-i-save-an-incomplete-step-in-a-canvas-template}

Ja, Sie können unvollständige Schritte als Canvas-Template speichern. Wenn das Template jedoch verwendet wird, erscheint ein Fehler auf dem Button **Template speichern**, der angibt, was zum Starten des Canvas benötigt wird.

### Kann ich meine Canvas-Builder-Einstellungen als Template speichern, oder kann ich nur Schritte speichern? {#can-i-save-my-canvas-builder-settings-as-a-template-or-can-i-only-save-steps}

Ja, Sie können Einstellungen im Canvas-Builder innerhalb eines Canvas-Templates speichern. Wenn Sie beispielsweise häufig eine Kombination aus Segmenten und Filtern verwenden möchten, können Sie diese **Zielgruppe**-Einstellungen als Teil Ihres Canvas-Templates speichern.