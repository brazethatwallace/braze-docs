---
nav_title: Ein HTML-E-Mail-Template hochladen
article_title: Ein HTML-E-Mail-Template hochladen
page_order: 2
description: "Dieser Referenzartikel beschreibt, wie Sie ein HTML-E-Mail-Template über das Braze-Dashboard erstellen, verwalten und Fehler beheben können."
tool:
  - Templates
channel:
  - email

---

# Ein HTML-E-Mail-Template hochladen {#upload-an-html-email-template}

> Das Braze-Dashboard ermöglicht es Ihnen, Ihre eigenen HTML-E-Mail-Templates hochzuladen und für die spätere Verwendung in Campaigns zu speichern. Sie können auch [ein E-Mail-Template erstellen]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template), indem Sie unseren Editor verwenden.

## Voraussetzungen {#upload-requirements}

Zunächst müssen Sie Ihr HTML-E-Mail-Template erstellen. Es muss sich um eine ZIP-Datei handeln, die Folgendes enthält:

* Eine einzelne HTML-Datei – der Textkörper Ihrer E-Mail
* Einen Ordner mit Bildern, auf die in der HTML-Datei verwiesen wird
* Weniger als 50 Bilddateien
* Eine Gesamtgröße von weniger als 5&nbsp;MB

## Ihr Template hochladen {#uploading-your-template}

### 1. Schritt: Zum E-Mail-Template-Editor navigieren {#step-1-go-to-the-email-template-editor}

Gehen Sie zu **Inhalt** > **E-Mail**. Wählen Sie **E-Mail-Template erstellen**.

### 2. Schritt: Template-Details hinzufügen {#step-2-add-template-details}

Geben Sie einen Template-Namen ein. Optional können Sie eine Beschreibung, Teams und Tags hinzufügen.

### 3. Schritt: Ihr Template hochladen {#step-3-upload-your-template}

Wählen Sie im Abschnitt **Template-Inhalt** die Option **Datei hochladen**. Wählen Sie Ihr Template von Ihrem Computer aus. Lesen Sie den Abschnitt [Voraussetzungen](#upload-requirements), um sicherzustellen, dass Ihr Template die Upload-Anforderungen erfüllt.

### 4. Schritt: Ihr Template fertigstellen und speichern {#step-4-finish-and-save-your-template}

Stellen Sie sicher, dass Sie Ihr Template speichern, indem Sie **Template speichern** auswählen. Sie können dieses Template jetzt in jeder Campaign oder jedem Canvas verwenden.

{% alert note %}
Wenn Sie Änderungen an einem bestehenden Template vornehmen, werden diese Änderungen nicht in Campaigns übernommen, die mit früheren Versionen dieses Templates erstellt wurden.
{% endalert %}

## Ihre Templates in API-Campaigns verwenden {#api_for_upload_email_templates}

Um Ihre E-Mail für eine API-Campaign zu verwenden, benötigen Sie die `email_template_id`, die am Ende jedes in Braze erstellten E-Mail-Templates zu finden ist.

![API-Bezeichner-Abschnitt eines HTML-E-Mail-Templates.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:50%;"}

## E-Mail-Templates verwalten {#managing-email-templates}

Sie können E-Mail-Templates [duplizieren]({{site.baseurl}}/user_guide/messaging/templates/managing_templates) und [archivieren]({{site.baseurl}}/user_guide/messaging/templates/managing_templates)! Erfahren Sie mehr über das Erstellen und Verwalten von Templates und kreativen Inhalten unter [Templates]({{site.baseurl}}/user_guide/messaging/templates).

## Fehlerbehebung {#troubleshooting}

Es gibt verschiedene E-Mail-Fehlermeldungen, die beim Hochladen einer HTML-Template-Datei auftreten können. Wenn Sie eine Fehlermeldung erhalten, finden Sie in der folgenden Tabelle häufige Probleme und empfohlene Lösungen:

| Fehler | Lösung |
|------|---|
| `.zip over 5&nbsp;MB` | Reduzieren Sie die Dateigröße und versuchen Sie es erneut.|
| `.zip corrupt` | Überprüfen Sie Ihre Datei und versuchen Sie es erneut. |
| `Missing HTML` | Fügen Sie die HTML-Datei zu Ihrer ZIP-Datei hinzu und versuchen Sie es erneut.|
| `Multiple HTML` | Entfernen Sie eine der HTML-Dateien und versuchen Sie es erneut.|
| `Images over 5&nbsp;MB` | Reduzieren Sie die Anzahl der Bilder und versuchen Sie es erneut. |
| `Extra Images` | Möglicherweise befinden sich zusätzliche Bilder in Ihrer Datei, auf die in Ihrer HTML-Datei nicht verwiesen wird. Dies verursacht keinen Fehler, aber die zusätzlichen Bilder werden verworfen. Wenn diese Bilder in der HTML-Datei referenziert werden sollten, überprüfen Sie den Inhalt, korrigieren Sie eventuelle Fehler und versuchen Sie es erneut.|
| `Missing Images` | Wenn in Ihrer HTML-Datei auf Bilder verwiesen wird, diese aber nicht im Bilderordner der ZIP-Datei enthalten sind, erhalten Sie einen Dateifehler. Überprüfen Sie Ihre Datei und korrigieren Sie eventuelle Fehler (wie Tippfehler), oder fügen Sie die fehlenden Bilder zu Ihrer ZIP-Datei hinzu und versuchen Sie es erneut.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fehlerbehebung" }

Beachten Sie, dass beim Herunterladen der Dateien für HTML-Campaigns, Canvas-Schritte mit E-Mail-Nachrichten oder Templates auf einem Windows-Computer das Zeichen `|` (Pipe-Zeichen) nicht unterstützt wird. Möglicherweise müssen Sie eine andere Anwendung verwenden, um den Inhalt der ZIP-Datei zu extrahieren.

## Häufig gestellte Fragen {#frequently-asked-questions}

Antworten auf häufig gestellte Fragen zu E-Mail-Templates finden Sie auf unserer Seite [FAQ zu E-Mail- und Link-Templates]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq).