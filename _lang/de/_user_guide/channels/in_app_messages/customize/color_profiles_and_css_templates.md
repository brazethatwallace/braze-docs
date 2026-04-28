---
nav_title: Farbprofile und CSS-Templates
article_title: Farbprofile und CSS-Templates
page_order: 3
page_type: reference
description: "Dieser Artikel bietet eine Übersicht über Farbprofile und CSS-Templates für In-App-Nachrichten."
channel:
  - in-app messages
---

# Farbprofile und CSS-Templates {#reusable-color-profiles}

> Sie können In-App-Nachrichten- und In-Browser-Nachrichten-Templates im Dashboard speichern, um schnell neue Campaigns und Nachrichten mit Ihrem Stil zu erstellen. Dieser Artikel bezieht sich auf den [traditionellen Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/). Wenn Sie den Drag-and-Drop-Editor verwenden, lesen Sie stattdessen [Stileinstellungen]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/).

Gehen Sie zu **Templates** > **In-App-Templates**.

Auf dieser Seite können Sie entweder vorhandene Templates bearbeiten oder auf **+ Erstellen** klicken und **Farbprofil** oder **CSS-Template** auswählen, um neue Templates für Ihre In-App-Nachrichten zu erstellen.

## Farbprofil {#color-profile}

Sie können das Farbschema Ihres Nachrichten-Templates anpassen, indem Sie entweder einen HEX-Farbcode eingeben oder auf das farbige Feld klicken und eine Farbe mit dem Farbwähler auswählen.

Klicken Sie auf **Farbprofil speichern**, wenn Sie fertig sind.

### Farbprofile verwalten {#managing-color-profiles}

Sie können Templates auch [duplizieren]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/) und [archivieren]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/)! Erfahren Sie mehr über das Erstellen und Verwalten von Templates und kreativen Inhalten unter [Templates und Medien]({{site.baseurl}}/user_guide/messaging/templates/).

## CSS-Template {#in-app-message-templates}

Sie können ein vollständiges CSS-Template für Ihre [Web-Modal-In-App-Nachricht](#web-modal-css) anpassen.

Benennen und taggen Sie Ihr CSS-Template und wählen Sie dann, ob es Ihr Standard-Template sein soll oder nicht. Sie können Ihr eigenes CSS in dem bereitgestellten Bereich schreiben. Dieser Bereich ist bereits mit dem CSS vorausgefüllt, das in Ihrer Nachrichtenvorschau angezeigt wird. Sie können es gerne leicht anpassen, um es an Ihre Anforderungen anzupassen.

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

Wie Sie sehen, können Sie alles bearbeiten – von der Hintergrundfarbe über die Schriftgröße und -stärke bis hin zu vielem mehr.

### CSS-Templates verwalten {#managing-css-templates}

Sie können Templates auch [duplizieren]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/) und [archivieren]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/)! Erfahren Sie mehr über das Erstellen und Verwalten von Templates und kreativen Inhalten unter [Templates und Medien]({{site.baseurl}}/user_guide/messaging/templates/).

## Modal mit CSS (nur Web) {#web-modal-css}

Wenn Sie eine reine Web-Modal-Nachricht mit CSS verwenden möchten, können Sie Ihr eigenes Template anwenden oder Ihr eigenes CSS in dem bereitgestellten Bereich schreiben. Dieser Bereich ist bereits mit dem CSS vorausgefüllt, das in Ihrer Nachrichtenvorschau angezeigt wird. Sie können es gerne leicht anpassen, um es an Ihre Anforderungen anzupassen.

Wenn Sie Ihr eigenes Template anwenden möchten, klicken Sie auf **Template anwenden** und wählen Sie aus der In-App-Nachrichten-Template-Galerie. Wenn keine Optionen vorhanden sind, können Sie ein [CSS-Template]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/color_profiles_and_css_templates/#in-app-message-templates) mit dem CSS-Template-Builder hochladen.