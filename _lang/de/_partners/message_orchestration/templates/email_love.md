---
nav_title: "Email Love"
article_title: "Email Love"
description: "Erfahren Sie, wie Sie Braze mit Email Love integrieren, einem Figma-Plugin, mit dem Sie responsive und barrierefreie HTML-E-Mails direkt aus Figma entwerfen und exportieren können."
alias: /partners/email_love/
page_type: partner
search_tag: Partner

---

# Email Love

> [Email Love](https://emaillove.com/) ist ein Figma-Plugin, mit dem Sie responsive und barrierefreie HTML-E-Mails direkt aus Figma heraus entwerfen und exportieren können. Das Feature „Export to Braze“ von Email Love verwendet die Braze API, um Ihre E-Mail-Templates nahtlos auf Braze hochzuladen.

## Voraussetzungen {#prerequisites}

| Anforderung            | Beschreibung                                                      |
|------------------------|------------------------------------------------------------------|
| **Email Love-Konto** | Ein Email Love-Konto ist erforderlich, um diese Partnerschaft nutzen zu können. |
| **Braze REST-API-Schlüssel** | Ein Braze REST-API-Schlüssel mit vollständig aktivierter `Templates`-Berechtigung. Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Email Love mit Braze verwenden {#using-email-love-with-braze}

### 1. Schritt: Plugin starten {#step-1-run-the-plugin}

Um Ihr E-Mail-Template zu gestalten, müssen Sie zunächst das Plugin laden. Ausführlichere Anweisungen finden Sie in der Dokumentation von Email Love zum [Hochladen Ihrer E-Mail auf Braze](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm).

### 2. Schritt: Ersten Frame erstellen {#step-2-create-your-first-frame}

Wählen Sie im Plugin den Button **[+ No Template Selected]**, um einen neuen Frame für Ihr E-Mail-Design zu erstellen.

### 3. Schritt: Template mit den vorgefertigten Komponenten von Email Love gestalten {#step-3-design-the-template-with-email-loves-pre-built-components}

Wählen Sie den erstellten Frame aus und fügen Sie Komponenten (Header, Content Blocks, CTAs und Footer) aus der **Assets**-Bibliothek des Plugins hinzu, um Ihre E-Mail zu strukturieren.

![Vorgefertigte Komponenten von Email Love.]({% image_buster /assets/img/email_love/emaillove1_content.png %})

### 4. Schritt: Komponenten anpassen {#step-4-customize-the-components}

Passen Sie die Komponenten mit den Figma-Werkzeugen an, um Text, Bilder, Farben und Layout-Elemente so zu ändern, dass das Design des Templates zu Ihrer Marke passt. Wenn Sie eine Footer-Komponente hinzufügen, wird beim Exportieren automatisch ein Braze-Abmeldelink eingefügt.

![Komponenten in Figma anpassen.]({% image_buster /assets/img/email_love/emaillove2_components.png %})

### 5. Schritt: E-Mail-Template nach Braze exportieren {#step-5-export-your-email-template-to-braze}

1. Wenn Sie fertig sind, wählen Sie den Frame aus, den Sie exportieren möchten. Beachten Sie, dass Sie einen Email Love-Footer mit einem Abmeldelink verwenden müssen, damit der Export funktioniert.
2. Wählen Sie im Plugin den Button **Export** und wählen Sie **Braze** aus dem Dropdown-Menü.
3. Kopieren Sie Ihren API-Schlüssel und fügen Sie ihn in das Feld **Braze API Key** innerhalb des Email Love Figma-Plugins ein.
4. Wählen Sie den Button **Set API Key**.
5. Wählen Sie **Change Instance ID** und wählen Sie dann Ihre Braze-Instanz-ID aus.

![Ein Template aus dem Email Love-Plugin nach Braze exportieren.]({% image_buster /assets/img/email_love/emaillove3_exportbraze.png %}){: style="max-width:50%;"}

### 6. Schritt: E-Mail in Braze bearbeiten {#step-6-edit-your-email-in-braze}

Gehen Sie in Braze zu **Templates** > **Edit Templates** > **Edit Message**. Im Template-Editor können Sie entweder Ihre E-Mail im HTML-Format bearbeiten oder den **Rich Text editor** im Tab **Classic** verwenden.

## Support und Fehlerbehebung {#support-and-troubleshooting}

Ausführlichere Anweisungen finden Sie in der Dokumentation von Email Love zum [Exportieren eines E-Mail-Designs](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm). Für zusätzlichen Support wenden Sie sich an das Email Love Support-Team.