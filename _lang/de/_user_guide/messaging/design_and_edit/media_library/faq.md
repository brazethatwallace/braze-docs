---
nav_title: FAQ
article_title: FAQ zur Medienbibliothek
page_order: 2
page_type: FAQ
tool: Media
description: "Dieser Artikel enthält Antworten auf häufig gestellte Fragen zur Medienbibliothek in Braze."

---

# Häufig gestellte Fragen {#frequently-asked-questions}

> Diese Seite enthält Antworten auf häufig gestellte Fragen zur Medienbibliothek in Braze.

## Allgemein {#general}

### Gibt es Speicherlimits für Bilder in der Medienbibliothek? {#are-there-storage-limits-for-images-within-the-media-library}

Nein, es gibt keine Speicherlimits für Assets in der Medienbibliothek. Es gibt jedoch Größenbeschränkungen für Assets (maximal 5 MB).

### Gibt es Ablaufdaten für hochgeladene Assets? {#are-there-expiration-dates-for-uploaded-assets}

Nein, Assets, die in die Medienbibliothek hochgeladen werden, bleiben für die gesamte Dauer Ihres Vertrags mit Braze erhalten.

### Kann ich Video-Assets hochladen? {#can-i-upload-video-assets}

Nein, die Medienbibliothek unterstützt keine Videodateien. Wir empfehlen, diese extern oder auf einer Plattform wie YouTube zu hosten.

### Kann ich alle Bildtypen zuschneiden? {#can-i-crop-all-image-types}

Nein, die Medienbibliothek unterstützt das Zuschneiden von GIF-Bildern nicht.

### Wie kopiere ich die URL eines in die Medienbibliothek hochgeladenen Bildes? {#how-do-i-copy-the-url-of-an-image-uploaded-to-the-media-library}

Um die URL eines in die Medienbibliothek hochgeladenen Bildes zu kopieren, navigieren Sie zu **Inhalt** > **Medienbibliothek**. Bewegen Sie den Mauszeiger über das gewünschte Bild und wählen Sie dann das Symbol **Bild-URL kopieren** aus, um die Bild-URL in Ihre Zwischenablage zu kopieren.

### Kann ich SVG-Bilder in E-Mails verwenden? {#can-i-use-svg-images-in-email}

SVG-Bilder werden für E-Mails nicht empfohlen, da die Unterstützung bei E-Mail-Clients eingeschränkt ist. Gmail und mehrere andere große E-Mail-Anbieter rendern SVG-Bilder nicht, was zu fehlerhaften oder fehlenden Bildern bei Empfänger:innen führen kann. Verwenden Sie für eine zuverlässige E-Mail-Darstellung stattdessen die Formate PNG, JPEG oder GIF.

### Wie schneide ich ein vorhandenes Bild zu? {#how-do-i-crop-an-existing-image}

Sie können ein vorhandenes Bild zuschneiden, indem Sie das Bild in der Medienbibliothek auswählen und auf **Zuschneiden und als neues Bild speichern** klicken.

![Vorschau eines Bildes in der Medienbibliothek.]({% image_buster /assets/img_archive/media_library_crop1.png %}){: height="75%" width="75%"}

Sie werden dann zu einem Zuschneideeditor weitergeleitet, in dem Sie Ihr Seitenverhältnis auswählen und den Namen des neuen Bildes bearbeiten können. Wenn Sie **Speichern** auswählen, kann Ihr neues Bild verwendet werden.

![Fenster zum Zuschneiden und Speichern eines Bildes in der Medienbibliothek.]({% image_buster /assets/img_archive/media_library_crop2.png %}){: height="75%" width="75%"}

### Mein Bild läuft beim Hochladen immer in ein Timeout. Was kann ich dagegen tun? {#my-image-keeps-timing-out-when-i-try-to-upload-it-what-can-i-do-about-this}

Dies kann verschiedene Ursachen haben, aber eine gängige Lösung besteht darin, Ihr Bild vor dem Hochladen zu optimieren. Das bedeutet, Ihr Bild durch einen Bildoptimierer wie [ImageOptim](https://imageoptim.com/mac) laufen zu lassen.

Wenn Ihr Bild außerdem in Photoshop (oder einer ähnlichen Software) erstellt wurde und viele Ebenen enthält, kann das Zusammenführen und Reduzieren der Ebenenanzahl ebenfalls helfen.

### Ich sehe einen „Unerwarteter Fehler“ beim Hochladen eines Bildes, obwohl es unter 5 MB groß ist und ein unterstütztes Format hat. Was ist falsch? {#i-see-an-unexpected-error-when-uploading-an-image-even-though-its-under-5-mb-and-in-a-supported-format-whats-wrong}

Dies kann zwei Hauptursachen haben:

1. **Ungültige Metadaten in der Datei:** Die Software, die Braze zur Bildverarbeitung verwendet, kann Dateien mit ungültigen oder inkompatiblen Metadaten ablehnen. In einigen Fällen kann die Datei auch so verarbeitet werden, dass sie das 5-MB-Limit überschreitet. Versuchen Sie, ein anderes Bild zu verwenden (z. B. das Bild aus Ihrem Bildeditor erneut exportieren oder speichern) oder ein Bild aus einer anderen Quelle.
2. **Sonderzeichen im Dateinamen:** Dateinamen, die Sonderzeichen enthalten (wie `&` oder `%`), können dazu führen, dass der Upload fehlschlägt. Benennen Sie die Datei um, sodass sie nur Buchstaben, Zahlen, Bindestriche oder Unterstriche enthält, und versuchen Sie den Upload erneut.

### Warum kann ich nicht jedes beliebige Bild in die Push-Composer hochladen? {#why-cant-i-upload-any-image-i-want-into-the-push-composers}

Das liegt daran, dass die meisten Composer Einschränkungen hinsichtlich des zulässigen Bildseitenverhältnisses haben.

### Ein Bild mit KI generieren {#generate-an-image-using-ai}

Sie können Bilder unter **Inhalt** > **Medienbibliothek** generieren, indem Sie **KI-Bildgenerator** auswählen. Sie benötigen die Berechtigung **Medienbibliothek-Assets bearbeiten**. Wenn Sie die Option nicht sehen, wenden Sie sich an Ihr Braze-Kundenteam. Weitere Informationen zu den Schritten und Richtlinien finden Sie unter [Bilder mit BrazeAI generieren]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-images) und [Bilder mit BrazeAI generieren]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#generate-ai).

### Kann ich Vanity-URLs für Bild-Assets in der Medienbibliothek erstellen? {#can-i-create-vanity-urls-for-media-library-image-assets}

Vanity-URLs für Assets in der Medienbibliothek werden nicht unterstützt, da benutzerdefinierte URLs die CDN-Zustellung beeinträchtigen würden. Sie können ein Bild unter seiner bestehenden URL ersetzen, wenn Campaigns bereits auf diese URL verweisen. Weitere Informationen finden Sie unter [Eine Datei ersetzen]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#replace-a-file).