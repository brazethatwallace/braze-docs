---
nav_title: In-App-Nachricht-Template erstellen
article_title: In-App-Nachricht-Template erstellen
page_order: 0
description: "Dieser Referenzartikel beschreibt, wie Sie In-App-Nachricht-Templates im Bereich „Templates“ des Braze-Dashboards erstellen, speichern und verwalten – einschließlich Farbprofilen und CSS-Templates für den traditionellen Editor."
tool:
  - Templates
channel:
  - in-app messages
search_rank: 1
---

# In-App-Nachricht-Template erstellen {#create-an-in-app-message-template}

> Verwenden Sie **Content** > **In-App Message**, um eine wiederverwendbare Bibliothek von In-App- und In-Browser-Nachrichtenlayouts aufzubauen. Sie können Designs aus dem Drag-and-Drop-Editor speichern oder **Farbprofil**- und **CSS-Template**-Assets für den [traditionellen Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/) erstellen.

## 1. Schritt: In-App-Nachricht-Templates öffnen {#step-1-open-in-app-message-templates}

Gehen Sie im Braze-Dashboard zu **Content** > **In-App Message**.

## 2. Schritt: Erstellungsmethode wählen {#step-2-choose-how-to-create-a-template}

Wie Sie ein Template hinzufügen, hängt von Ihrem Ziel ab:

| Ziel | Vorgehensweise |
|------|----------------|
| Ein Drag-and-Drop-Layout zur Wiederverwendung speichern | Wählen Sie im [Drag-and-Drop-In-App-Nachrichten-Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/) die Option **Save as template**, nachdem Sie den Editor verlassen haben (Sie müssen die Campaign zuerst starten ODER als Entwurf speichern). Das Template erscheint unter **Templates** > **In-App Message Templates** für Ihre nächste Nachricht. |
| Ein Farbprofil oder CSS-Template erstellen (traditioneller Editor) | Wählen Sie auf der Seite **In-App Message Templates** die Option **+ Create** und dann **Color Profile** oder **CSS Template**. Weitere Informationen finden Sie unter [Farbprofile und CSS-Templates](#reusable-color-profiles). |
| Ein Braze-Template anpassen | [Erstellen Sie eine In-App-Nachricht]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/) im Drag-and-Drop-Editor, wählen Sie ein Braze-Template aus, nehmen Sie Ihre Anpassungen vor und wählen Sie **Save as template**. Beschreibungen der einzelnen Braze-Templates finden Sie unter [In-App-Nachricht-Templates]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="2. Schritt: Erstellungsmethode wählen" }

{% alert note %}
Farbprofile und CSS-Templates gelten für den traditionellen Editor. Wenn Sie den Drag-and-Drop-Editor verwenden, nutzen Sie die [Stileinstellungen]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/) für die Gestaltung auf Nachrichtenebene.
{% endalert %}

## 3. Schritt: Templates verwalten {#step-3-manage-your-templates}

Unter **Content** > **In-App Message** können Sie Templates filtern, suchen oder öffnen, um sie zu bearbeiten. Sie können Templates wie andere Template-Typen [duplizieren]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/#duplicate-templates) und [archivieren]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/#archive-templates). Einen Überblick über Template- und Medien-Workflows finden Sie unter [Templates]({{site.baseurl}}/user_guide/messaging/templates/).

Um auf In-App-Nachricht-Templates zuzugreifen, benötigen Sie [Nutzer:innenberechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) zum Anzeigen oder Bearbeiten von In-App-Nachricht-Templates.

### Farbprofile und CSS-Templates erstellen {#reusable-color-profiles}

{% alert note %}
Die folgenden Optionen gelten für den [traditionellen Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/). Wenn Sie den Drag-and-Drop-Editor verwenden, nutzen Sie stattdessen die [Stileinstellungen]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/).
{% endalert %}

Sie können vorhandene Templates bearbeiten oder **+ Create** wählen und **Color Profile** oder **CSS Template** auswählen, um neue Templates für Ihre In-App-Nachrichten zu erstellen.

#### Farbprofil {#color-profile}

Sie können das Farbschema Ihres Nachricht-Templates anpassen, indem Sie entweder einen HEX-Farbcode eingeben oder auf das farbige Feld klicken und eine Farbe mit dem Farbwähler auswählen. Wenn dieses Profil standardmäßig angewendet werden soll, wenn Sie neue In-App-Nachrichten im traditionellen Editor erstellen, wählen Sie **Use as default profile**.

Wählen Sie **Save Color Profile**, wenn Sie fertig sind.

![Der Editor für In-App-Nachricht-Farbprofil-Templates.]({% image_buster /assets/img/drag_and_drop/templates/color_profile_template.png %})

#### CSS-Template {#in-app-message-templates}

Sie können ein vollständiges CSS-Template für Ihre [Web-Modal-In-App-Nachricht](#web-modal-css) anpassen.

Benennen und taggen Sie Ihr CSS-Template und wählen Sie dann, ob es Ihr Standard-Template sein soll. Sie können Ihr eigenes CSS in den bereitgestellten Bereich schreiben. Dieser Bereich ist bereits mit dem CSS vorausgefüllt, das in Ihrer Nachrichtenvorschau angezeigt wird, und Sie können es an Ihre Bedürfnisse anpassen.

```css
.ab-message-header, .ab-message-text {
  color: #333333;
  text-align: center;
}

.ab-message-header {
  font-size: 20px;
  font-weight: bold;
}

.ab-message-text {
  font-size: 14px;
  font-weight: normal;
}

.ab-close-button svg {
  fill: #9b9b9b;
}

.ab-message-button {
  border: 1px solid #1b78cf;
  font-size: 14px;
  font-weight: bold;
}
.ab-message-button:first-of-type {
  background-color: white;
  color: #1b78cf;
}
.ab-message-button:last-of-type, .ab-message-button:first-of-type:last-of-type {
  background-color: #1b78cf;
  color: white;
}

.ab-background {
  background-color: white;
}

.ab-icon {
  background-color: #0073d5;
  color: white;
}

.ab-page-blocker {
  background-color: rgba(51, 51, 51, .75);
}
```

Sie können alles bearbeiten – von der Hintergrundfarbe bis hin zu Schriftgröße und -stärke und mehr.

#### Modal mit CSS (nur Web) {#web-modal-css}

Wenn Sie eine reine Web-Nachricht vom Typ „Web Modal mit CSS“ verwenden, können Sie Ihr eigenes Template anwenden oder Ihr eigenes CSS in den bereitgestellten Bereich schreiben. Dieser Bereich ist bereits mit dem CSS vorausgefüllt, das in Ihrer Nachrichtenvorschau angezeigt wird, aber Sie können es an Ihre Bedürfnisse anpassen.

Wenn Sie Ihr eigenes Template anwenden möchten, wählen Sie **Apply Template** und wählen Sie aus der In-App-Nachricht-Template-Galerie. Wenn keine Optionen verfügbar sind, können Sie ein [CSS-Template](#in-app-message-templates) mit dem CSS-Template-Builder unter **Templates** > **In-App Message Templates** hinzufügen.