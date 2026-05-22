---
nav_title: Kontaktkarten
article_title: Kontaktkarten
page_order: 3
description: "Dieser Referenzartikel behandelt, wie Sie eine Kontaktkarte erstellen, die Sie in Ihre MMS- und SMS-Nachrichten einfügen können."
page_type: reference
alias: /mms_contact_cards/
channel:
  - MMS

---

# Kontaktkarten {#contact-cards}

> Kontaktkarten (manchmal auch als vCard oder Virtual Contact Files (VCF) bezeichnet) sind ein standardisiertes Dateiformat zum Versenden von Geschäfts- und Kontaktinformationen, die sich einfach in Adressbücher oder Kontaktverzeichnisse importieren lassen.

{% alert note %}
Das Senden einer Kontaktkarte wird als MMS berechnet. Überprüfen Sie Ihr erwartetes MMS-Volumen und die Nutzung von Nachrichtenguthaben, wenn Sie Kontaktkarten erstellen, und bestätigen Sie die Kosten auf Ihrer Braze-[Abrechnungsseite]({{site.baseurl}}/user_guide/administer/global/billing/).
{% endalert %}

Kontaktkarten können [programmatisch](https://www.twilio.com/blog/send-vcard-twilio-sms) erstellt und in die Braze-[Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/#media-library) hochgeladen oder über unseren integrierten Kontaktkarten-Generator erstellt werden. Diesen Karten können gängige Eigenschaften wie Ihr Unternehmensname, Ihre Telefonnummer, Adresse, E-Mail und ein kleines Foto zugewiesen werden. Um mit der Erstellung von Kontaktkarten zu beginnen, stellen Sie zunächst sicher, dass Sie für die Nutzung von MMS in Braze eingerichtet sind.

## Kontaktkarten-Generator {#contact-card-generator}

### 1. Schritt: Name zuweisen {#step-1-assign-name}

Kontaktkarten können über den SMS- und MMS-Editor erstellt werden. Wählen Sie den Tab **Contact Card Generator**, um zu beginnen.

Als Nächstes werden Sie aufgefordert, Ihren Unternehmensnamen oder Spitznamen einzugeben. Dies ist der Name, den Ihre Nutzer:innen sehen, wenn sie die Karte speichern. Es gilt ein Limit von 20 Zeichen, damit Nutzer:innen Ihren vollständigen Unternehmensnamen oder Alias in ihren Kontakten und ihrer Messaging-App sehen können.

![Der Tab „Contact Card Generator“.]({% image_buster /assets/img/sms/contact_card1.png %}){: style="max-width:60%" }

### 2. Schritt: Telefonnummer zuweisen {#step-2-assign-phone-number}

Wählen Sie die Abo-Gruppe und die gewünschte Telefonnummer aus den verfügbaren Dropdown-Optionen aus. Diese Nummer wird in Ihrer Kontaktkarte aufgeführt und steht nach dem Speichern auf dem Telefon zum Versenden von Textnachrichten zur Verfügung.

Beachten Sie, dass alphanumerische Codes nicht mit bidirektionalem Messaging kompatibel sind und für Kontaktkarten nicht unterstützt werden.

### 3. Schritt: Optionale Felder {#step-3-optional-fields}

![Optionale Felder für den Kontaktkarten-Generator.]({% image_buster /assets/img/sms/contact_card2.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

#### Kontaktfoto für die Kontaktkarte hochladen {#upload-contact-card-contact-photo}

Sie können ein optionales Thumbnail-Kontaktfoto für Ihre Kontaktkarte hochladen. Wir empfehlen ein JPEG- oder PNG-Bild mit 240 x 240&nbsp;px. Alle hochgeladenen hochauflösenden Bilder werden auf 240 x 240&nbsp;px verkleinert, um die Zustellbarkeit Ihrer Nachricht sicherzustellen, da MMS-Nachrichten größer als 5&nbsp;MB fehlschlagen können.

#### Weitere Informationen hinzufügen {#add-more-information}

Weitere Felder ermöglichen es Ihnen, Ihren Namen, eine Unterüberschrift, eine Adresse und andere Kontaktinformationen einzufügen, die Ihre Nutzer:innen möglicherweise zur Verfügung haben möchten.

### 4. Schritt: Kontaktkarte speichern {#step-4-saving-your-contact-card}

Nachdem Sie alle erforderlichen Felder ausgefüllt haben, klicken Sie auf **Generate Contact Card**, und die Karte wird automatisch an Ihre **Campaign** oder Ihren Canvas angehängt. Von hier aus können Sie eine Nachricht hinzufügen, Ihre Kontaktkarte testen und Ihre **Campaign** oder Ihren Canvas starten.

Die Kontaktkarte wird auch in der [Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/#media-library) gespeichert, um sie in zukünftigen **Campaigns** und Canvases einfach wiederverwenden zu können.

## Eine vorhandene Kontaktkarte hinzufügen {#adding-an-existing-contact-card}

Um eine vorhandene Kontaktkarte hinzuzufügen, erstellen Sie eine **Campaign** oder einen Canvas und wählen Sie Ihre gewünschte Abo-Gruppe aus. Anschließend erscheint im Nachrichten-Editor-Fenster die Option **Add Media**. Hier können Sie eine vorhandene Kontaktkartendatei hochladen oder eine über die Medienbibliothek suchen.