---
nav_title: Crowdin
article_title: Crowdin
description: "Verwenden Sie die Crowdin-Integration, um Campaigns, Canvas-Erlebnisse, E-Mail-Templates und Content Blocks mit Translation Memory, Glossaren und maschineller Übersetzung zu übersetzen."
alias: /partners/crowdin/
page_type: partner
search_tag: Partner

---

# Crowdin

> [Crowdin](https://crowdin.com/) ist eine KI-gestützte Plattform zur Verwaltung der Lokalisierung, die Teams dabei unterstützt, die Übersetzung ihrer Software, Apps und Marketing-Inhalte zu automatisieren.

Verbinden Sie Crowdin mit Braze, um Übersetzungen für Ihre Campaigns und Canvas-Erlebnisse zu verwalten. Die automatische Synchronisierung arbeitet mit maschineller Übersetzung, Translation Memory und Glossaren, sodass manuelle und automatisierte Workflows konsistent bleiben.

_Diese Integration wird von Crowdin gepflegt._

## Über die Integration {#about-the-integration}

Crowdin bietet zwei Apps für Braze an: [Braze Campaigns & Canvas](https://store.crowdin.com/braze-content-translation) und [Braze Email Templates](https://store.crowdin.com/braze-app). Wählen Sie die App basierend auf den Braze-Features aus, die Sie lokalisieren möchten. Die folgende Tabelle vergleicht die beiden.

### Die richtige Crowdin-App auswählen {#choose-the-right-crowdin-app}

| Kanal oder Feature | Braze Campaigns & Canvas | Braze Email Templates |
| --- | --- | --- |
| **Campaigns** | ✅ Unterstützt | ❌ Nicht unterstützt |
| **Canvas-Schritte** | ✅ Unterstützt | ❌ Nicht unterstützt |
| **E-Mail-Templates** | ❌ Nicht unterstützt | ✅ Unterstützt |
| **Content Blocks** | ❌ Nicht unterstützt | ✅ Unterstützt |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Die richtige Crowdin-App auswählen" }

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| **Crowdin-Konto** | Ein [Crowdin.com-Konto](https://accounts.crowdin.com/register) oder ein [Crowdin-Enterprise-Konto](https://accounts.crowdin.com/workspace/create) ist erforderlich. |
| **Crowdin-Projekt** | Bevor Sie Braze verbinden, [erstellen Sie ein Übersetzungsprojekt](https://support.crowdin.com/creating-project/) in Crowdin oder Crowdin Enterprise. |
| **Braze-REST-API-Schlüssel** | Ein Braze-REST-API-Schlüssel mit Berechtigungen für Campaigns, Canvas, Content Blocks, angepasste Attribute, E-Mail und Templates. |
| **Braze-REST-Endpunkt** | Ihre spezifische Braze-REST-Endpunkt-URL (zum Beispiel `https://rest.iad-03.braze.com`). |
| **Braze-Mehrsprachigkeitseinstellungen** | Locales müssen in Ihrem Braze-Dashboard unter **Einstellungen** > **Lokalisierungseinstellungen** konfiguriert sein. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Braze Campaigns & Canvas-Integration

Wenn Sie Inhalte in aktiven Nachrichten lokalisieren, verwenden Sie die [Braze Campaigns & Canvas-App](https://store.crowdin.com/braze-content-translation), um übersetzbare Strings aus Ihren Campaign- und Canvas-Entwürfen mit der Braze-Mehrsprachenunterstützung zu synchronisieren.

Eine Video-Anleitung finden Sie unter [Braze Campaigns & Canvas-Integration](https://youtu.be/ahG1ET4VRKA).

### Schritt 1: Mehrsprachige Einstellungen in Braze konfigurieren {#step-1-set-up-multi-language-settings-in-braze}

Bevor Sie Crowdin verbinden, fügen Sie Ihre Zielsprachen in Braze hinzu.

1. Navigieren Sie in Braze zu **Einstellungen** > **Lokalisierungseinstellungen**.
2. Fügen Sie die Sprachen hinzu, die Sie unterstützen möchten.

![Braze-Seite „Locales“ unter „Einstellungen“ mit Locale-Namen, Locale-Schlüsseln und „Locale hinzufügen“.]({% image_buster /assets/img/crowdin/braze_locales.png %})

{: start="3"}
3. Notieren Sie sich jeden **Locale-Schlüssel** (zum Beispiel `en-US`, `fr-FR`, `es-ES`). Sie verwenden diese Werte, wenn Sie die Sprachen in Crowdin zuordnen.

### Schritt 2: Braze-Projekt in Crowdin einrichten {#step-2-set-up-the-braze-project-in-crowdin}

1. Gehen Sie in Ihrem Crowdin Enterprise- oder Crowdin.com-Konto im Navigationsmenü zu **Store**.
2. Suchen Sie nach **Braze Campaigns & Canvas** und wählen Sie **Install**.

![Crowdin Store mit ausgewähltem Braze Campaigns & Canvas und hervorgehobenem „Install“.]({% image_buster /assets/img/crowdin/crowdin_store_campaigns_canvas.png %})

{: start="3"}
3. Wählen Sie das Projekt (oder die Projekte) aus, in dem/denen Sie diese Integration verwenden möchten.
4. Um die Integration zu öffnen, navigieren Sie zu Ihrem Projekt unter **Integrations** > **Braze Campaigns & Canvas**.

#### Braze mit Crowdin verbinden {#connecting-braze-to-crowdin}

Autorisieren Sie die Verbindung mit Ihren Braze-API-Zugangsdaten:

![Crowdin-Verbindungsformular für Braze Campaigns & Canvas mit REST-API-Schlüssel, REST-Endpunkt und „Log in with Braze Campaigns & Canvas“.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_login.png %})

- **Braze REST-API-Schlüssel:** Erstellen Sie diesen in Braze unter **Einstellungen** > **APIs und Bezeichner** > **API-Schlüssel**. Gewähren Sie die Berechtigungen, die diese Integration benötigt (Campaigns, Canvas, Content Blocks und angepasste Attribute).
- **Braze REST-Endpunkt:** Geben Sie die URL Ihrer Braze-Instanz ein (zum Beispiel `https://rest.iad-03.braze.com`). Weitere Informationen finden Sie unter [REST API-Endpunkte]({{site.baseurl}}/api/basics#endpoints).

![Braze-Seite „REST API Keys“ mit „Create API Key“ und dem Kopier-Steuerelement für den REST-Endpunkt.]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %})

Wählen Sie **Log in with Braze Campaigns & Canvas**.

### Schritt 3: Sprachzuordnung in Crowdin konfigurieren {#step-3-configure-language-mapping-in-crowdin}

Nachdem Sie Ihr Konto verbunden haben, ordnen Sie jede Crowdin-Projektsprache dem passenden Braze-Locale zu.

1. Wählen Sie im Dashboard der **Braze Campaigns & Canvas**-Integration in der oberen Aktionsleiste das Zahnradsymbol **Settings**.

![Bildschirm der Braze Campaigns & Canvas-Integration mit „Settings“ in der oberen Aktionsleiste.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_settings.png %})

{: start="2"}
2. Öffnen Sie den Tab **General Settings**.
3. Geben Sie die Locale-Schlüssel ein. Crowdin listet Ihre Projektsprachen auf (zum Beispiel Französisch, Italienisch). Geben Sie in jedem Feld den passenden **Braze-Locale-Schlüssel** ein.
   - Wenn Braze beispielsweise `it` für Italienisch verwendet, geben Sie `it` neben Italienisch in Crowdin ein.
   - Jeder Eintrag muss exakt dem **Locale-Schlüssel** für das jeweilige Locale in den Braze-**Lokalisierungseinstellungen** entsprechen.

![Einstellungsmodal auf dem Tab „General Settings“ mit Dateifilterfeldern und Sprachzuordnungszeilen (zum Beispiel Französisch zugeordnet zu „fr“).]({% image_buster /assets/img/crowdin/crowdin_language_mapping_settings.png %})

{: start="4"}
4. Wählen Sie **Save**, um die Zuordnung zu bestätigen.

### Schritt 4: Übersetzungs-Tags zu Ihrer Braze-Nachricht hinzufügen {#step-4-add-translation-tags-to-your-braze-message}

Crowdin liest dieselben Liquid-**Übersetzungs-Tags**, die Braze für mehrsprachige Nachrichten verwendet. Fügen Sie {% raw %}`{% translation your_id_here %}` und `{% endtranslation %}`{% endraw %} um jedes Textstück, jede Bild-URL oder Link-URL hinzu, das/die übersetzt werden soll. Jeder Block benötigt eine eindeutige `id` (zum Beispiel `greeting` oder `welcome_header`).

**Beispiel:**

{% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

Für HTML, Liquid in Links und andere Muster gelten dieselben Regeln wie unter [Locales übersetzen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) (zum Beispiel Tags um die kleinstmöglichen Abschnitte setzen und nur sprachspezifische Teile von URLs umschließen, wenn Links lokalisiert werden).

Speichern Sie Ihre Braze-Nachricht als **Entwurf**, bevor Crowdin den Inhalt erkennen und abrufen kann.

### Schritt 5: Übersetzungen in Crowdin verwalten {#step-5-manage-translations-in-crowdin}

Der Integrationsbildschirm hat zwei Seiten:

- **Braze-Panel:** Ihre Campaigns und Canvases.
- **Crowdin-Panel:** Bereits zur Übersetzung synchronisierte Inhalte.

![Crowdin- und Braze Campaigns & Canvas-Panels mit Ordnern für Campaigns und Locales, „Sync to Braze“ und „Sync to Crowdin“.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_sync_panels.png %})

#### Inhalte synchronisieren {#syncing-content}

1. Aktivieren Sie im **Braze**-Panel das Kontrollkästchen für die Campaign oder den Canvas, der übersetzt werden soll.
2. Wählen Sie **Sync to Crowdin**.
3. Wenn die Synchronisierung abgeschlossen ist, erscheint die Datei im **Crowdin**-Panel. Übersetzer:innen können die Strings im Crowdin-Editor öffnen.

#### Übersetzungen an Braze zurückgeben {#returning-translations-to-braze}

1. Wenn die Übersetzungen in Crowdin zu 100 % abgeschlossen sind, kehren Sie zum Tab **Integrations** zurück.
2. Wählen Sie den abgeschlossenen Inhalt im **Crowdin**-Panel aus.
3. Wählen Sie **Sync to Braze**. Dadurch werden die übersetzten Strings in die entsprechenden Sprachvarianten Ihrer Braze-Campaign übertragen.

### Schritt 6: Nachricht als mehrsprachige:r Nutzer:in in Braze anzeigen {#step-6-preview-the-message-as-a-multi-language-user-in-braze}

So bestätigen Sie die Integration:

1. Öffnen Sie Ihre Campaign im **Braze Nachrichten-Editor**.
2. Wechseln Sie zum Tab **Test**.
3. Wählen Sie **Preview Message as User**.
4. Suchen Sie nach einem Kundenprofil, dessen `language`-Attribut einem Ihrer übersetzten Locales entspricht.
5. Bestätigen Sie, dass der Inhalt von der Ausgangssprache zur übersetzten Version wechselt.

## Integration von Braze E-Mail-Templates {#braze-email-templates-integration}

Wenn Sie E-Mails auf Template-Ebene lokalisieren, verwenden Sie die [Braze Email Templates-App](https://store.crowdin.com/braze-app), um HTML aus Ihrer Braze-Medienbibliothek zu synchronisieren.

Eine Videoanleitung finden Sie unter [Integration von Braze Email Templates](https://youtu.be/g0YMKW3jEjk).

### Schritt 1: App installieren {#step-1-install-the-app}

1. Gehen Sie in Ihrem Crowdin-Projekt zum Tab **Store**.
2. Suchen Sie nach **Braze Email Templates** und wählen Sie **Install** aus.

![Crowdin Store mit ausgewähltem Eintrag „Braze Email Templates“ und hervorgehobener Schaltfläche „Install“.]({% image_buster /assets/img/crowdin/crowdin_store_email_templates.png %})

{: start="3"}
3. Wählen Sie das Projekt (oder die Projekte) aus, in dem/denen Sie diese Integration verwenden möchten.
4. Um die Integration zu öffnen, navigieren Sie in Ihrem Projekt zu **Integrations** > **Braze Email Templates**.

### Schritt 2: Mit Braze verbinden {#step-2-connect-to-braze}

Autorisieren Sie die Verbindung mit Ihren Braze-API-Zugangsdaten:

![Crowdin-Verbindungsformular für Braze Email Templates mit REST-API-Schlüssel, REST-Endpunkt und der Schaltfläche „Log in with Braze Email Templates“.]({% image_buster /assets/img/crowdin/crowdin_email_templates_login.png %}){: style="max-width:85%;"}

1. **Braze REST-API-Schlüssel:** Gewähren Sie die Berechtigungen `templates.email` und `content_blocks` (Lesen und Schreiben). Erstellen Sie den Schlüssel in Braze unter **Einstellungen** > **APIs und Bezeichner** > **API-Schlüssel**.

![Seite für Braze REST-API-Schlüssel mit der Schaltfläche „Create API Key“ und dem Kopier-Steuerelement für den REST-Endpunkt.]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %})

{: start="2"}
2. Geben Sie unter **Braze REST endpoint** Ihre instanzspezifische URL ein (zum Beispiel `https://rest.iad-03.braze.com`).
3. Wählen Sie **Log in with Braze Email Templates** aus.

### Schritt 3: Inhalte zur Übersetzung synchronisieren {#step-3-sync-content-for-translation}

Der Integrationsbildschirm zeigt Ihre Braze-Bibliothek:

- **Braze-Panel:** **Email Templates** und **Content Blocks**, die Sie synchronisieren können.
- **Crowdin-Panel:** Inhalte in der Übersetzung.

1. Aktivieren Sie im **Braze**-Panel das Kontrollkästchen neben den Templates oder Blöcken, die Sie lokalisieren möchten.
2. Wählen Sie **Sync to Crowdin** aus.
3. Crowdin ruft den HTML-Quelltext ab. Übersetzer:innen arbeiten im Crowdin-Editor mit einer Live-**WYSIWYG-Vorschau**, sodass das Layout erhalten bleibt.

![Vorschau-Tab im Crowdin-Editor mit lokalisiertem E-Mail-HTML und übersetzbaren Strings.]({% image_buster /assets/img/crowdin/crowdin_editor_wysiwyg_preview.png %}){: style="max-width:85%;"}

### Schritt 4: Übersetzte Templates bereitstellen {#step-4-deliver-translated-templates}

Wenn die Übersetzungen eine Fertigstellung von 100 % erreichen:

1. Wählen Sie die fertiggestellten Dateien im **Crowdin**-Panel aus.
2. Wählen Sie **Sync to Braze** aus.
3. Crowdin erstellt automatisch lokalisierte Versionen dieser Assets in Ihrer Braze-Medienbibliothek (zum Beispiel `Template_Name_fr`).

![Crowdin- und Braze-Email-Templates-Panels mit E-Mail-Templates und Content Blocks sowie den Schaltflächen „Sync to Braze“ und „Sync to Crowdin“.]({% image_buster /assets/img/crowdin/crowdin_email_templates_sync_panels.png %})