---
nav_title: E-Mail-Registrierung mit Bild
article_title: E-Mail-Registrierung mit Hintergrundbild
alias: "/email_image/"
page_order: 5
description: "Diese Seite beschreibt, wie Sie den Drag-and-Drop-Editor für In-App-Nachrichten verwenden, um Ihren Markenstil mit einer einfachen Nachricht zu präsentieren und Ihre E-Mail-Liste aufzubauen."
---

# E-Mail-Registrierung mit Hintergrundbild {#email-sign-up-with-background-image}

> Verwenden Sie den Drag-and-Drop-Editor für In-App-Nachrichten, um Ihren Markenstil mit einer einfachen Nachricht zu präsentieren und Ihre E-Mail-Liste aufzubauen.

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Ein E-Mail-Registrierungsformular mit Hintergrundbild erstellen {#creating-an-email-sign-up-form-with-a-background-image}

### 1. Schritt: Template auswählen {#step-1-choose-your-template}

Wählen Sie beim Erstellen einer Drag-and-Drop-In-App-Nachricht **Email sign-up with background image** als Template aus und klicken Sie dann auf **Build message**. Dieses Template wird sowohl für mobile Apps als auch für Webbrowser unterstützt.

![Der In-App-Nachrichten-Editor mit dem Template für ein E-Mail-Registrierungsformular mit Hintergrundbild.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_image.png %})

### 2. Schritt: Nachrichtenstile einrichten {#step-2-set-up-your-message-styles}

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### 3. Schritt: E-Mail-Registrierungskomponente anpassen {#step-3-customize-your-email-sign-up-component}

Um mit dem Erstellen Ihres E-Mail-Registrierungsformulars zu beginnen, wählen Sie das E-Mail-Erfassungselement im Editor aus. Standardmäßig erhalten erfasste E-Mail-Adressen die globale Abo-Gruppe **Abonniert**. Um Nutzer:innen für bestimmte Abo-Gruppen anzumelden, lesen Sie [E-Mail-Abo-Status aktualisieren]({{site.baseurl}}/user_guide/channels/email/subscriptions#updating-email-subscription-states).

Sie können den Platzhaltertext und den Beschriftungstext des E-Mail-Erfassungselements anpassen.

![Der In-App-Nachrichten-Editor mit einem Seitenmenü zum Anpassen des E-Mail-Erfassungselements.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field_image.png %})

#### E-Mail-Validierung {#email-validation}

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### 4. Schritt: Haftungsausschluss hinzufügen (optional) {#step-4-add-disclaimer-language-optional}

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### 5. Schritt: Nachricht gestalten {#step-5-style-your-message}

Passen Sie das Erscheinungsbild Ihres Registrierungsformulars mithilfe der Drag-and-Drop-[Komponenten für In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings#message-components) an. Fügen Sie Ihr eigenes Hintergrundbild hinzu, indem Sie die Standard-Hintergrundbild-URL im Menü **Message container** ersetzen, oder entfernen Sie die URL und wählen Sie Ihr Bild aus der [Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) aus.

## Ergebnisse analysieren {#analyzing-the-results}

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Best Practices {#best-practices}

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}