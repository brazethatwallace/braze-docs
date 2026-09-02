---
nav_title: E-Mail-Registrierung mit Bestätigung
article_title: E-Mail-Registrierung mit Bestätigungsseite
alias: "/email_confirmation_page/"
page_order: 7
description: "Diese Seite beschreibt, wie Sie den Drag-and-Drop-Editor für In-App-Nachrichten verwenden, um ein E-Mail-Registrierungsformular mit einer Bestätigungsseite zu erstellen."
---

# E-Mail-Registrierung mit Bestätigungsseite {#email-sign-up-with-confirmation-page}

> Verwenden Sie den Drag-and-Drop-Editor für In-App-Nachrichten, um ein E-Mail-Registrierungsformular mit einer Bestätigungsseite zu erstellen.

{% multi_lang_include drag_and_drop/templates.md section='SDK or Software-Development-Kit requirements' %}

## Ein E-Mail-Registrierungsformular mit Bestätigungsseite erstellen {#creating-an-email-sign-up-form-with-a-confirmation-page}

### 1. Schritt: Template auswählen {#step-1-choose-your-template}

Wählen Sie beim Erstellen einer Drag-and-Drop-In-App-Nachricht **E-Mail-Registrierung mit Bestätigungsseite** als Template aus und klicken Sie dann auf **Nachricht erstellen**. Dieses Template wird sowohl für mobile Apps als auch für Webbrowser unterstützt.

![Der In-App-Nachrichten-Editor mit dem Template für ein E-Mail-Registrierungsformular mit Bestätigungsseite.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_confirmation.png %})

### 2. Schritt: Nachrichtenstile einrichten {#step-2-set-up-your-message-styles}

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### 3. Schritt: E-Mail-Registrierungskomponente anpassen {#step-3-customize-your-email-sign-up-component}

Um mit dem Erstellen Ihres E-Mail-Registrierungsformulars zu beginnen, wählen Sie das E-Mail-Erfassungselement im Editor aus. Standardmäßig erhalten erfasste E-Mail-Adressen die globale Abo-Gruppe **Abonniert**. Um Nutzer:innen für bestimmte Abo-Gruppen anzumelden, lesen Sie [E-Mail-Abo-Status Update or aktualisieren or aktualisieren]({{site.baseurl}}/user_guide/channels/email/subscriptions#updating-email-subscription-states).

Sie können den Platzhaltertext und den Beschriftungstext des E-Mail-Erfassungselements anpassen.

![Der In-App-Nachrichten-Editor mit einem Seitenmenü zum Anpassen des E-Mail-Erfassungselements.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field_confirmation.png %})

#### E-Mail-Validierung {#email-validation}

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### 4. Schritt: Haftungsausschluss hinzufügen (optional) {#step-4-add-disclaimer-language-optional}

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### 5. Schritt: Nachricht gestalten {#step-5-style-your-message}

Passen Sie das Erscheinungsbild Ihres E-Mail-Registrierungsformulars und Ihrer Bestätigungsseite mithilfe der Drag-and-Drop-[Komponenten für In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings#message-components) an.

## Ergebnisse analysieren {#analyzing-the-results}

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Best Practices {#best-practices}

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}