---
nav_title: SMS-, RCS- und WhatsApp-Registrierungsformular
article_title: SMS-, RCS- und WhatsApp-Registrierungsformular
alias: "/phone_number_capture/"
page_order: 2
description: "Diese Seite beschreibt, wie Sie ein SMS-, RCS- und WhatsApp-Registrierungsformular mit dem Drag-and-Drop-Editor für In-App-Nachrichten erstellen."
---

# SMS-, RCS- und WhatsApp-Registrierungsformular {#sms-rcs-and-whatsapp-sign-up-form}

> Die SMS-, RCS- und WhatsApp-Registrierungsformulare sind Templates, die im Drag-and-Drop-Editor für In-App-Nachrichten verfügbar sind. Verwenden Sie diese Templates, um die Telefonnummern Ihrer Nutzer:innen zu erfassen und Ihre SMS-, MMS-, RCS- und WhatsApp-Abo-Gruppen zu vergrößern.

![Drei Beispiele für In-App-Nachrichten, die mit dem Template für Telefonnummer-Registrierungsformulare erstellt wurden.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_example2.png %})

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Ein Telefonnummer-Registrierungsformular erstellen {#creating-a-phone-number-sign-up-form}

### 1. Schritt: Template auswählen {#step-1-choose-your-template}

Wenn Sie eine Drag-and-Drop-In-App-Nachricht erstellen, wählen Sie **SMS sign-up** (dies deckt auch die RCS-Registrierung ab) oder **WhatsApp sign-up** als Template und dann **Build message**. Diese Templates werden sowohl für mobile Apps als auch für Webbrowser unterstützt.

![Modal zur Auswahl von „SMS sign-up“ oder „WhatsApp sign-up“ als Template beim Erstellen einer In-App-Nachricht.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_template.png %}){: style="max-width:80%"}

### 2. Schritt: Nachrichtenstile einrichten {#step-2-set-up-your-message-styles}

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

![Workflow zum Hochladen und Auswählen einer benutzerdefinierten Schriftart.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_custom_font.gif %})

### 3. Schritt: Telefonnummer-Eingabekomponente anpassen {#step-3-customize-your-phone-number-input-component}

Um mit dem Erstellen Ihres Registrierungsformulars zu beginnen, wählen Sie die Telefonnummer-Eingabekomponente im Editor aus.

![Vorschaubereich beim Erstellen eines Registrierungsformulars mit ausgewählter Telefonnummer-Eingabekomponente.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%"}

Geben Sie im Seitenmenü an, für welche Abo-Gruppe dieses Template Telefonnummern erfassen soll. Um die Best Practices für Compliance einzuhalten, können Sie pro Telefonnummer-Registrierungsformular nur die Einwilligung für eine Abo-Gruppe erfassen. Bei Bedarf können Sie jedoch mehrere Formulare verwenden, um die Einwilligung für weitere Abo-Gruppen einzuholen.

![Dropdown für Abo-Gruppen mit einer ausgewählten Abo-Gruppe.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_subscription.png %}){: style="max-width:40%"}

Standardmäßig werden Nummern weltweit erfasst. Sie können jedoch die Anzahl der Länder einschränken, aus denen Nummern erfasst werden. Dies ist hilfreich, wenn Sie nur Nutzer:innen mit Telefonnummern in bestimmten Ländern kontaktieren möchten, und kann zur Listenqualität beitragen. Deaktivieren Sie dazu **Collect numbers from all countries** und verwenden Sie das Dropdown, um bestimmte Länder auszuwählen. Ihre Nutzer:innen können nur Länder auswählen, die Sie explizit hinzugefügt haben.

![Länder-Dropdown zur Auswahl der Länder, aus denen Sie Nummern erfassen möchten.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_countries.png %}){: style="max-width:40%"}

#### Ungültige Telefonnummern {#invalid-phone-numbers}

Wenn Ihre Nutzer:innen eine Telefonnummer eingeben, die nicht akzeptierte Sonderzeichen enthält, wird ein allgemeiner Fehlerindikator angezeigt, der nicht anpassbar ist, und das Formular kann nicht abgesendet werden. Sie können das Fehlerverhalten im Tab **Preview & Test** und auf Ihrem Testgerät überprüfen. Lesen Sie diesen Artikel, um zu erfahren, [wie Braze Telefonnummern formatiert]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers/#importing-phone-numbers).

### 4. Schritt: Haftungsausschluss hinzufügen (für SMS- und RCS-Registrierungsformulare) {#step-4-add-disclaimer-language-for-sms-and-rcs-sign-up-forms}

Für SMS- und RCS-Registrierungsformulare ist es wichtig, klar zu kommunizieren, welche Art von SMS oder RCS Sie senden werden. Stellen Sie sicher, dass Ihr Listenwachstum konform ist, indem Sie die folgenden Informationen in Ihr Formular aufnehmen:

- Beschreibung der Arten von SMS- und RCS-Nachrichten, die Ihre Kund:innen erwarten können (Warenkorb-Erinnerungen, Aktionen und Angebote, Terminerinnerungen usw.). Sie müssen nicht jeden Anwendungsfall auflisten, sollten aber eine Beschreibung der Nachrichtentypen bereitstellen, die Ihre Marke senden wird.
- Hinweis, dass die Einwilligung keine Bedingung für einen Kauf ist (falls zutreffend).
- Nachrichtenhäufigkeit und Hinweis, dass Nachrichten- und Datengebühren anfallen. Wenn Sie die genaue Nachrichtenhäufigkeit nicht kennen, können Sie angeben, dass die Häufigkeit variieren kann.
- Links zu Ihren Allgemeinen Geschäftsbedingungen und der SMS- und RCS-Datenschutzrichtlinie.
- Hinweis auf Hilfe- und Abmelde-Schlüsselwörter (HELP für Hilfe; STOP zum Abbestellen).

Wir haben im Template einen Platzhalter-Haftungsausschluss ausschließlich als Beispiel bereitgestellt – er stellt keine Rechtsberatung dar und sollte nicht für Compliance-Zwecke herangezogen werden. Es ist wichtig, mit Ihrem Rechtsteam zusammenzuarbeiten, um eine Formulierung zu entwickeln, die auf Ihre spezifische Marke zugeschnitten ist.

{% alert note %}
Diese Dokumentation ist nicht dazu bestimmt, Rechtsberatung zu erteilen, und darf auch nicht vollständig als solche herangezogen werden.
{% endalert %}

Weitere Informationen zur SMS- und RCS-Compliance finden Sie unter [Gesetze und Vorschriften für SMS, MMS und RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations/).

### 5. Schritt: Nachricht gestalten {#step-5-style-your-message}

Passen Sie das Erscheinungsbild Ihrer Nachricht mit den Drag-and-Drop-[In-App-Nachricht-Komponenten]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/#message-components) an.

## Ergebnisse analysieren {#analyzing-the-results}

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

![Performance-Panel für In-App-Nachrichten mit Klicks für jeden Link in der In-App-Nachricht.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_analytics.png %})