---
nav_title: Smartling
article_title: Smartling
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Smartling, einer cloudbasierten Software für die Lokalisierung. Der Braze Connector unterstützt die Übersetzung von HTML-E-Mail-Templates, Content Blocks, Canvase und E-Mail-Nachrichten in Campaigns."
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> [Smartling](https://www.smartling.com/) ist eine End-to-End-Cloud-Übersetzungsmanagement-Software für Kund:innen, die die Übersetzung von Websites, Anwendungen und Kundenerlebnissen automatisieren möchten.

_Diese Integration wird von Smartling gepflegt._

## Über die Integration {#about-the-integration}

Der Braze Connector unterstützt Übersetzungen für Nachrichten in Campaigns und Canvase (E-Mail, Push, In-App-Nachrichten und Banner), E-Mail-Templates und Content Blocks. In der folgenden Tabelle erfahren Sie, welche Editor-Typen für die einzelnen Kanäle oder Features unterstützt werden.

| Kanal/Feature | Traditioneller Editor (z. B. HTML) | Drag-and-Drop-Editor |
| --------------- | ----------------------------- | -------------------- |
| [E-Mail]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email) | ✅ | ✅ |
| [IAM]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message) | ✅ | ✅ |
| [Push]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push) | ✅ | k. A. |
| E-Mail-Template | ✅ | ✅ |
| Banner | k. A. | ✅ |
| Content Blocks | ✅ | ✅ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="About the integration" }


## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Smartling-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Smartling-Konto](https://dashboard.smartling.com/). |
| Smartling-Übersetzungsprojekt | Um Ihr Braze-Konto mit Smartling zu verbinden, müssen Sie sich zunächst anmelden und [ein Übersetzungsprojekt erstellen](https://help.smartling.com/hc/en-us/articles/115003074093). |
| Braze Representational State Transfer-API-Schlüssel | Ein Braze Representational State Transfer-API-Schlüssel mit den folgenden Berechtigungen: <br>- campaigns.translations.get<br>- campaigns.translations.Update or aktualisieren<br>- campaigns.list<br>- campaigns.details<br>- Canvas.translations.get<br>- Canvas.translations.Update or aktualisieren<br>- campaigns.details<br>- templates.email.create<br>- templates.email.Update or aktualisieren<br>- templates.email.list<br>- templates.email.info<br>- templates.translations.get<br>- templates.translations.Update or aktualisieren<br>- content_blocks.info<br>- content_blocks.list<br>- content_blocks.create<br>- content_blocks.Update or aktualisieren<br><br> Diesen können Sie im Braze-Dashboard unter **Einstellungen > API-Schlüssel** erstellen. |
| Braze Representational State Transfer-Endpunkt | [Ihre URL für den Representational State Transfer-Endpunkt]({{site.baseurl}}/api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Braze-Mehrspracheneinstellungen | [Vollständige Mehrspracheneinstellungen in Braze]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

### 1. Schritt: Mehrsprachige Einstellungen in Braze einrichten {#step-1-set-up-multi-language-settings-in-braze}

Sehen Sie sich [die mehrsprachige Setup-Anleitung von Braze]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) an, um Lokalisierungen in Braze einzurichten.

### 2. Schritt: Braze-Projekt in Smartling TMS einrichten {#step-2-set-up-the-braze-project-in-smartling-tms}

Einzelheiten zur Konfiguration des Konnektors finden Sie in der [Smartling-Dokumentation](https://help.smartling.com/hc/en-us/articles/13248549217435).

### Braze mit Smartling verbinden {#connecting-braze-to-smartling}

1. Erstellen Sie in Ihrem [Smartling-Konto](https://dashboard.smartling.com/) einen [Braze Connector](https://help.smartling.com/hc/en-us/articles/115003074093)-Projekttyp.

![Braze-Verbindung in Smartling.]({% image_buster /assets/img/smartling/image1_Connecting_Braze_to_Smartling.png %})

{: start="2"}
2. Wählen Sie in diesem Projekt **Settings** > **Braze Settings** > **Connect to Braze**.
3. Füllen Sie die erforderlichen Felder aus, z. B. API-URL und API-Schlüssel. Wenn die Testverbindung erfolgreich ist, speichern Sie die Verbindung. Wenn der Test nicht erfolgreich ist, überprüfen Sie, ob Sie die richtige API-URL und den richtigen API-Schlüssel eingegeben haben.

![Braze-Verbindung in den Smartling-API-Einstellungen.]({% image_buster /assets/img/smartling/image2_API.png %})

{: start="4"}
4. Fügen Sie zusätzliche Projektsprachen hinzu.

![Braze-Verbindung in Smartling-Projektsprachen.]({% image_buster /assets/img/smartling/image3_project_languages.png %})

{: start="5"}
5. Überprüfen Sie in den Braze-Einstellungen, ob die Werte in der Spalte **Target Language (Braze)** mit den in den Braze-Mehrspracheneinstellungen konfigurierten Lokalisierungen übereinstimmen. Die Benennungskonvention der Lokalisierung muss genau übereinstimmen.

![Braze-Verbindung in der Smartling-Sprachbestätigung.]({% image_buster /assets/img/smartling/image4_language_confirmation.png %})

### 3. Schritt: Übersetzungstags zu Ihrer Braze-Nachricht hinzufügen {#step-3-add-translation-tags-to-your-braze-message}

Sehen Sie sich [die Anleitung von Braze]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/?tab%3Dhtml%2520editor#prerequisites) an, wie Sie Ihren Nachrichten Übersetzungstags hinzufügen können:

- [E-Mail]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email)
- [Push]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push)
- [In-App-Nachrichten]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message)

Hier sehen Sie ein Beispiel für eine HTML-E-Mail-Campaign mit Übersetzungstags.

![Braze-E-Mail mit Übersetzungstags.]({% image_buster /assets/img/smartling/image5_translation_tags.png %})

Sie müssen die Nachricht als Entwurf speichern, bevor Sie Lokalisierungen auswählen können.

### 4. Schritt: Übersetzungen in Smartling verwalten {#step-4-manage-translations-in-smartling}

Nachdem Sie den Braze Connector verbunden und eingerichtet haben, finden Sie Braze-Inhalte auf dem Braze-Tab in Ihrem Smartling-Projekt. Weitere Informationen finden Sie in der [Smartling-Dokumentation](https://help.smartling.com/hc/en-us/articles/13248577069979).

Smartling bietet erweiterte Features zum Suchen und Auswählen von Inhalten nach:
- Schlüsselwort-Suche
- Braze-Inhaltstyp
- Braze-Tagging

1. In diesem Beispiel wurde die E-Mail-Campaign zur Neujahrsaktion in [Schritt 3](#step-3-add-translation-tags-to-your-braze-message) erstellt.

![Braze-E-Mail mit Übersetzungstags.]({% image_buster /assets/img/smartling/image6_ny_promotion.png %})

{: start="2"}
2. Nachdem Sie die Campaign gefunden haben, die Sie übersetzen möchten, wählen Sie den Ordner aus, wählen Sie die Varianten und wählen Sie **Request Translation**.

![Übersetzungen anfragen.]({% image_buster /assets/img/smartling/image7_request_translation.png %})

{: start="3"}
3. Erstellen Sie einen neuen Auftrag für die Übersetzung.

![Einen neuen Auftrag für die Übersetzung erstellen.]({% image_buster /assets/img/smartling/image8_request_translation.png %})

{: start="4"}
4. Nachdem der Auftrag genehmigt wurde, bearbeiten Sie jede Übersetzung im CAT-Tool.

![Übersetzung im CAT-Tool.]({% image_buster /assets/img/smartling/image9_translation_job.png %})

{: start="5"}
5. Nachdem die Übersetzungen fertiggestellt sind, speichern Sie Ihre Übersetzung und senden Sie sie an Braze.

![Übersetzung an Braze senden.]({% image_buster /assets/img/smartling/image10_translations.png %})

### 5. Schritt: Nachricht als mehrsprachige:r Nutzer:in in Braze in der Vorschau anzeigen {#step-5-preview-the-message-as-a-multi-language-user-in-braze}

Zeigen Sie in Braze eine Vorschau Ihrer Campaign als mehrsprachige:r Nutzer:in an, um zu überprüfen, ob die Übersetzungen korrekt angewendet werden.

![Mehrsprachige Vorschau für Nutzer:innen.]({% image_buster /assets/img/smartling/image11_preview.png %})

## Häufig gestellte Fragen {#frequently-asked-questions}

### Werden Übersetzungstags für den Drag-and-Drop-Editor unterstützt? {#are-translation-tags-supported-for-the-drag-and-drop-editor}

Für den Drag-and-Drop-Editor (E-Mail, Content Block, In-App-Nachricht) müssen Sie Übersetzungstags manuell als Liquid-Tags hinzufügen.

### Wie übersetzt man Text innerhalb eines Liquid-Tags? {#how-do-you-translate-text-within-a-liquid-tag}

Smartling erkennt Liquid-Tags und macht sie zu nicht editierbaren Variablen im Composer. Jeder andere Text innerhalb des Liquid-Tags, wie z. B. Standardtext oder Filter wie „join“, wird in Smartling ebenfalls nicht editierbar. Entfernen Sie jedoch den Liquid-Tag in Smartling und erstellen Sie den Liquid-Tag mit dem übersetzten Standardtext neu. Beim Speichern der Übersetzung erscheint eine Warnung.