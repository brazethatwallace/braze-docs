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

Nein, die Medienbibliothek unterstützt keine Videodateien. Hosten Sie diese extern oder auf einer Plattform wie YouTube.

### Kann ich alle Bildtypen zuschneiden? {#can-i-crop-all-image-types}

Nein, die Medienbibliothek unterstützt das Zuschneiden von GIF-Bildern nicht.

### Wie kopiere ich die URL eines in die Medienbibliothek hochgeladenen Bildes? {#how-do-i-copy-the-url-of-an-image-uploaded-to-the-media-library}

Um die URL eines in die Medienbibliothek hochgeladenen Bildes zu kopieren, navigieren Sie zu **Inhalt** > **Medienbibliothek**. Bewegen Sie den Mauszeiger über das gewünschte Bild und wählen Sie dann das Symbol **Bild-URL kopieren** aus, um die Bild-URL in Ihre Zwischenablage zu kopieren.

### Kann ich SVG-Bilder in E-Mails verwenden? {#can-i-use-svg-images-in-email}

SVG-Bilder werden für E-Mails nicht empfohlen, da die Unterstützung bei E-Mail-Clients eingeschränkt ist. Gmail und mehrere andere große E-Mail-Anbieter rendern SVG-Bilder nicht, was zu fehlerhaften oder fehlenden Bildern bei Empfänger:innen führen kann. Verwenden Sie für eine zuverlässige E-Mail-Darstellung stattdessen die Formate PNG, JPEG oder GIF.

### Wie schneide ich ein vorhandenes Bild zu? {#how-do-i-crop-an-existing-image}

Sie können ein vorhandenes Bild zuschneiden, indem Sie das Bild in der Medienbibliothek auswählen und auf **Zuschneiden & als neues Bild speichern** klicken.

![Vorschau eines Bildes in der Medienbibliothek.]({% image_buster /assets/img_archive/media_library_crop1.png %}){: height="75%" width="75%"}

Der Zuschnitt-Editor öffnet sich, in dem Sie Ihr Seitenverhältnis auswählen und den Namen des neuen Bildes bearbeiten können. Wenn Sie **Speichern** auswählen, können Sie Ihr neues Bild verwenden.

![Fenster zum Zuschneiden und Speichern eines Bildes in der Medienbibliothek.]({% image_buster /assets/img_archive/media_library_crop2.png %}){: height="75%" width="75%"}

### Mein Bild läuft beim Hochladen immer in ein Timeout. Was kann ich dagegen tun? {#my-image-keeps-timing-out-when-i-try-to-upload-it-what-can-i-do-about-this}

Dies kann verschiedene Ursachen haben, aber eine häufige Lösung besteht darin, Ihr Bild vor dem Hochladen zu optimieren. Das bedeutet, Ihr Bild durch einen Bildoptimierer wie [ImageOptim](https://imageoptim.com/mac) laufen zu lassen.

Wenn Ihr Bild außerdem in Photoshop (oder ähnlicher Software) erstellt wurde und viele Ebenen enthält, kann das Zusammenführen und Reduzieren der Ebenenanzahl ebenfalls helfen.

### Ich sehe einen „Unerwarteter Fehler“ beim Hochladen eines Bildes, obwohl es unter 5 MB groß ist und ein unterstütztes Format hat. Was ist falsch? {#i-see-an-unexpected-error-when-uploading-an-image-even-though-its-under-5-mb-and-in-a-supported-format-whats-wrong}

Dies kann zwei Hauptursachen haben:

1. **Ungültige Metadaten in der Datei:** Die Software, die Braze zur Bildverarbeitung verwendet, kann Dateien mit ungültigen oder inkompatiblen Metadaten ablehnen. In einigen Fällen kann die Datei auch so verarbeitet werden, dass sie das 5-MB-Limit überschreitet. Versuchen Sie, ein anderes Bild zu verwenden (z. B. das Bild aus Ihrem Bildeditor erneut exportieren oder speichern) oder ein Bild aus einer anderen Quelle.
2. **Sonderzeichen im Dateinamen:** Dateinamen, die Sonderzeichen enthalten (wie `&` oder `%`), können dazu führen, dass der Upload fehlschlägt. Benennen Sie die Datei um, sodass sie nur Buchstaben, Zahlen, Bindestriche oder Unterstriche enthält, und versuchen Sie den Upload erneut.

### Warum kann ich nicht jedes beliebige Bild in die Push-Editoren hochladen? {#why-cant-i-upload-any-image-i-want-into-the-push-composers}

Das liegt daran, dass die meisten Editoren Einschränkungen hinsichtlich des zulässigen Bildseitenverhältnisses haben.

### Ein Bild mit KI generieren {#generate-an-image-using-ai}

Sie können Bilder unter **Inhalt** > **Medienbibliothek** generieren, indem Sie **Mit Operator generieren** auswählen. Sie benötigen die Berechtigung „Edit Media Library Assets“. Wenn Sie die Option nicht sehen, wenden Sie sich an Ihr Braze-Kontoteam. Weitere Informationen zu den Schritten und Richtlinien finden Sie unter [Bilder mit BrazeAI generieren]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-images) und [Bilder mit BrazeAI generieren]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#generate-ai).

### Was passiert, wenn ich ein Bild aus der Medienbibliothek lösche? {#what-happens-when-i-delete-an-image-from-the-media-library}

Durch das Löschen eines Assets wird es aus der Medienbibliothek-Oberfläche entfernt, aber Braze behält die Datei unter ihrer bestehenden URL gehostet, sodass aktive Campaigns und Canvases, die auf diese URL verweisen, das Bild weiterhin laden. Um ein Asset dauerhaft vom Braze-Hosting zu entfernen, wenden Sie sich an den Braze-Support. Um zu ändern, was Empfänger:innen sehen, ohne die URLs in jeder Nachricht zu ändern, verwenden Sie stattdessen [Eine Datei ersetzen]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#replace-a-file).

### Kann ich Bild-Assets in bereits gesendeten E-Mails ändern? {#can-i-change-image-assets-in-emails-that-have-already-been-sent}

Sie können das Bild in einer bereits gesendeten E-Mail aktualisieren, indem Sie [die Datei]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#replace-a-file) unter ihrer bestehenden URL ersetzen. Die URL und ID des Assets bleiben gleich, sodass jede Nachricht, die darauf verweist – einschließlich bereits gesendeter E-Mails – die neue Datei widerspiegelt. Einige Empfänger:innen sehen möglicherweise noch das vorherige Bild, wenn es bereits auf ihrem Gerät zwischengespeichert war, bevor Sie die Änderung vorgenommen haben. Dies garantiert also nicht, dass alle Empfänger:innen die Aktualisierung sofort sehen.

### Speichert Braze Bilder zwischen, die über eine externe URL in Content Cards und In-App-Nachrichten hinzugefügt werden? {#does-braze-cache-images-added-through-an-external-url-in-content-cards-and-in-app-messages}

Das hängt vom Kanal ab:

- **Content Cards und traditionelle In-App-Nachrichten** (Modal, Slideup und Vollbild): Ja. Wenn Sie die Nachricht einrichten, kopiert Braze das Bild auf sein eigenes CDN. Das Bild in der Nachricht wird von dieser Kopie bereitgestellt, sodass das Ändern oder Löschen der Originalquelle (z. B. das Entfernen des Assets aus einem S3-Bucket) keine Auswirkungen auf bereits erstellte oder gesendete Content Cards hat.
- **HTML-In-App-Nachrichten und Drag-and-Drop-In-App-Nachrichten:** Nein. Braze speichert das Bild nicht zwischen. Die Nachricht lädt das Bild direkt von der von Ihnen angegebenen URL, sodass das Ändern oder Entfernen der Quell-URL das Bild in aktiven Campaigns beschädigt.
- **E-Mail:** Das Verhalten hängt davon ab, wie das Bild hinzugefügt wurde. Weitere Informationen finden Sie unter [Kann ich Bild-Assets in bereits gesendeten E-Mails ändern?](#can-i-change-image-assets-in-emails-that-have-already-been-sent).

### Kann ich Vanity-URLs für Bild-Assets in der Medienbibliothek erstellen? {#can-i-create-vanity-urls-for-media-library-image-assets}

Vanity-URLs für Assets in der Medienbibliothek werden nicht unterstützt, da benutzerdefinierte URLs die CDN-Zustellung beeinträchtigen würden. Sie können ein Bild unter seiner bestehenden URL ersetzen, wenn Campaigns bereits auf diese URL verweisen. Weitere Informationen finden Sie unter [Eine Datei ersetzen]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#replace-a-file).

### Warum speichert Chrome JPEG- oder PNG-Bilder als WebP-Dateien? {#why-does-chrome-save-jpeg-or-png-images-as-webp-files}

Wenn Sie Chrome verwenden, um Bilder aus der Medienbibliothek zu speichern, konvertiert der Browser JPEG- oder PNG-Dateien möglicherweise automatisch in das WebP-Format. Dies ist das Standardverhalten von Chrome für Bild-Downloads und nicht spezifisch für Braze. Wenn Sie Bilder in ihrem Originalformat speichern müssen, verwenden Sie einen anderen Browser wie Safari oder Firefox.