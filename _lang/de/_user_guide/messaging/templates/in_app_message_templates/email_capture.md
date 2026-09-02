---
nav_title: E-Mail-Registrierungsformular
article_title: E-Mail-Registrierungsformular
alias: "/email_capture/"
page_order: 3
description: "Diese Seite beschreibt, wie Sie ein E-Mail-Registrierungsformular mit dem Drag-and-Drop-Editor für In-App-Nachrichten erstellen."
---

# E-Mail-Registrierungsformular {#email-sign-up-form}

> Verwenden Sie das Drag-and-Drop-Template für E-Mail-Registrierungs-In-App-Nachrichten, um E-Mail-Adressen von Nutzer:innen zu erfassen und Ihre Abo-Gruppen zu vergrößern.

{% multi_lang_include drag_and_drop/templates.md section='SDK or Software-Development-Kit requirements' %}

## Ein E-Mail-Registrierungsformular erstellen {#creating-an-email-sign-up-form}

### 1. Schritt: Template auswählen {#step-1-choose-your-template}

Wenn Sie eine Drag-and-Drop-In-App-Nachricht erstellen, wählen Sie **Email Registrierung or registrieren** als Template und dann **Build message**. Dieses Template wird sowohl für mobile Apps als auch für Webbrowser unterstützt.

![Der In-App-Nachrichten-Editor mit dem Template für ein E-Mail-Erfassungsformular.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_template1.png %})

### 2. Schritt: Nachrichtenstile einrichten {#step-2-set-up-your-message-styles}

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### 3. Schritt: E-Mail-Registrierungskomponente anpassen {#step-3-customize-your-email-sign-up-component}

Um mit der Erstellung Ihres E-Mail-Registrierungsformulars zu beginnen, wählen Sie das E-Mail-Erfassungselement im Editor aus. Standardmäßig erhalten erfasste E-Mail-Adressen den globalen Abo-Gruppen-Status **Abonniert**. Um Nutzer:innen für bestimmte Abo-Gruppen anzumelden, lesen Sie [E-Mail-Abo-Status Update or aktualisieren or aktualisieren]({{site.baseurl}}/user_guide/channels/email/subscriptions#updating-email-subscription-states).

Sie können den Platzhaltertext und den Beschriftungstext des E-Mail-Erfassungselements anpassen.

![Der In-App-Nachrichten-Editor mit einem Seitenmenü zur Anpassung des E-Mail-Erfassungselements.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field1.png %})

#### E-Mail-Validierung {#email-validation}

Wenn Nutzer:innen eine E-Mail-Adresse eingeben, die nicht akzeptierte Sonderzeichen enthält, wird ein allgemeiner Fehlerindikator angezeigt und das Formular kann nicht gesendet werden. Diese Fehlermeldung ist nicht anpassbar. Sie können das Fehlerverhalten im Tab **Preview & Test** und auf Ihrem Testgerät überprüfen. Erfahren Sie mehr darüber, wie Braze E-Mail-Adressen formatiert, unter [E-Mail-Validierung]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation).

### 4. Schritt: Haftungsausschluss hinzufügen (optional) {#step-4-add-disclaimer-language-optional}

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### 5. Schritt: Nachricht gestalten {#step-5-style-your-message}

Passen Sie das Erscheinungsbild Ihres Registrierungsformulars mithilfe der Drag-and-Drop-[In-App-Nachrichten-Komponenten]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings#message-components) an.

## Ergebnisse analysieren {#analyzing-the-results}

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Best Practices {#best-practices}

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}