---
nav_title: Lokalise
article_title: Lokalise
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Lokalise, einem Dienst für das Übersetzungsmanagement agiler Teams."
alias: /partners/lokalise/
page_type: partner
search_tag: Partner

---

# Lokalise

> [Lokalise](https://lokalise.com) ist ein Dienst für das Übersetzungsmanagement agiler Teams.

_Diese Integration wird von Lokalise gepflegt._

## Über die Integration {#about-the-integration}

Lokalise bietet zwei Integrationsoptionen für Braze:

- **Mehrsprachige Integration (empfohlen)**: Nutzt die [Multi-Language Composition API]({{site.baseurl}}/api/endpoints/translations/) von Braze, um eine direkte bidirektionale Synchronisierung zwischen Lokalise und Braze bereitzustellen. Diese Integration funktioniert mit lokalisierten Nachrichtenvarianten für Campaigns, Canvases und E-Mail-Templates und unterstützt Workflows vor und nach dem Start für Push, E-Mail und In-App Messages.
- **Connected-Content-Integration (Legacy)**: Nutzt Braze Connected-Content, um übersetzte Inhalte basierend auf den Spracheinstellungen der Nutzer:innen einzufügen.

Dieser Artikel behandelt die Einrichtung beider Integrationen.

## Mehrsprachige Integration (empfohlen) {#multi-language-integration-recommended}

Die mehrsprachige Integration nutzt die Multi-Language Composition API von Braze, um eine optimierte, automatisierte Verwaltung mehrsprachiger Braze-Inhalte in Lokalise zu ermöglichen.

### Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Lokalise-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Lokalise-Konto. |
| Lokalise-Übersetzungsprojekt | Erstellen Sie ein Lokalise-Projekt mit dem Typ **Marketing and support** und wählen Sie **Braze** als **Content integration**. |
| Braze-Einstellungen für mehrere Sprachen | Die [Unterstützung mehrerer Sprachen]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings/) muss in Ihrem Braze-Workspace aktiviert sein. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit Berechtigungen zum Lesen und Aktualisieren von Campaigns, Canvases und E-Mail-Templates. Sie können einen im Braze-Dashboard unter **Settings** > **API Keys** erstellen. |
| Braze-Serverregion | Ihre [Braze-Serverregion]({{site.baseurl}}/api/basics/#endpoints) (z. B. US-01, EU-01). Sie finden diese im Braze-Dashboard. |
| Übersetzungs-Tags in Braze-Inhalten | Nachrichten müssen [Übersetzungs-Tags]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) verwenden, um übersetzbare Inhalte zu kennzeichnen. Umschließen Sie jeden übersetzbaren Block mit {% raw %}`{% translation ID %}...{% endtranslation %}`{% endraw %}-Tags mit einer eindeutigen ID. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

### Einrichtung und Verwendung {#setup-and-usage}

Detaillierte Anweisungen zum Verbinden der mehrsprachigen Braze-Integration in Lokalise, zum Importieren von Inhalten, zum Übersetzen und zum Exportieren von Übersetzungen zurück nach Braze finden Sie in der [Braze-Integrationsdokumentation von Lokalise](https://docs.lokalise.com/en/articles/13654162-braze).

Die Integration unterstützt:
- Direkte bidirektionale Synchronisierung zwischen Lokalise und Braze (keine manuelle Dateiverarbeitung)
- Lokalisierte Nachrichtenvarianten für Campaigns, Canvases und E-Mail-Templates
- Übersetzungsworkflows vor und nach dem Start

{% alert note %}
Nur Inhalte, die in Braze für die mehrsprachige Nutzung konfiguriert und in Übersetzungs-Tags eingeschlossen sind, stehen für den Import in Lokalise zur Verfügung. Die Sprachcodes müssen in Braze und Lokalise exakt übereinstimmen, damit die Übersetzungen korrekt synchronisiert werden.
{% endalert %}

## Connected-Content-Integration (Legacy)

Die Legacy-Integration nutzt Braze Connected-Content, um übersetzte Inhalte basierend auf den Spracheinstellungen der Nutzer:innen einzufügen.

### Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Lokalise-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Lokalise-Konto. |
| Lokalise-Übersetzungsprojekt | Erstellen Sie ein Lokalise-Projekt mit dem Projekttyp **Software Localization**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

### Erstellen Sie ein neues Lokalise-Projekt {#create-a-new-lokalise-project}

Um ein neues Übersetzungsprojekt zu erstellen, melden Sie sich bei Lokalise an und wählen Sie **New Project**. Als Nächstes benennen Sie Ihr Projekt, wählen eine **Base Language** (die Sprache, aus der Sie übersetzen werden), fügen eine oder mehrere **Target Languages** hinzu und wählen den Projekttyp **Software Localization**. Wenn Sie bereit sind, klicken Sie auf **Proceed**.

### Integration

In Lokalise erstellen Sie für jede der Connected-Content-Variablen, die Sie in Braze definieren, einen Übersetzungsschlüssel. Wenn die Übersetzungen fertig sind, können Sie eine JSON-Datei pro Sprache generieren und sie auf den URLs veröffentlichen, die Ihre Connected-Content-Inhalte bereitstellen werden.

#### 1. Schritt: Konfiguration der Nutzer:innen-Sprachen {#step-1-configure-user-languages}

Falls Sie es noch nicht getan haben, öffnen Sie das Braze-Dashboard und gehen Sie zu **Users > User Import**. Hier können Sie Ihre Nutzer:innen importieren. Wenn Sie eine CSV-Datei für den Import vorbereiten, stellen Sie sicher, dass Sie eine Sprachspalte mit den Sprachen der Nutzer:innen einfügen. Dieses Sprachfeld wird später bei der Anzeige von Übersetzungen verwendet.

{% alert important %}
Die verwendeten Sprachcodes müssen sowohl in Braze als auch in Lokalise übereinstimmen.
{% endalert %}

#### 2. Schritt: Vorbereitungen für Ihre Übersetzungen auf Lokalise {#step-2-prepare-your-translations-on-lokalise}

Um Ihre Übersetzungen in Lokalise vorzubereiten, müssen Sie als Nächstes manuell die Übersetzungsschlüssel mit demselben Namen erstellen, den Sie in den Variablen von Braze Connected-Content verwenden.

Lassen Sie uns zum Beispiel einen einfachen Übersetzungsschlüssel erstellen: `description`:
1. Öffnen Sie Ihr Lokalise-Projekt, klicken Sie auf **Add Key** und geben Sie „description“ in das Feld **Key** ein.
2. Geben Sie „Demo description“ in das Feld **Base Language Value** ein.
3. Fügen Sie „Web“ in der Dropdown-Liste **Platforms** hinzu.
4. Wenn Sie fertig sind, klicken Sie auf **Save**.

![]({% image_buster /assets/img/lokalise/1_add_key.png %}){: style="max-width:60%"}

Ihr Übersetzungsschlüssel sollte im Projekteditor erscheinen:

![]({% image_buster /assets/img/lokalise/2_translation_key_added.png %}){: style="max-width:90%"}

##### Bekannte Probleme {#known-issues}

- Ihre Schlüssel müssen der **Web**-Plattform zugewiesen sein.
- Vermeiden Sie die Verwendung von Schlüsseln, die Punkte (`.`) oder den String `_on` enthalten. Verwenden Sie zum Beispiel `this_is_the_key` anstelle von `this.is.the.key` und `join_us_instagram` anstelle von `join_us_on_instagram`.

#### 3. Schritt: Konfigurieren der Braze-App auf Lokalise {#step-3-configure-the-braze-app-on-lokalise}

Öffnen Sie Ihr Lokalise-Projekt und klicken Sie auf **Apps**. Suchen und installieren Sie hier die Braze-App. Sie sehen dann den folgenden Bildschirm:

![Braze-Konfiguration auf Lokalise mit Angabe der Projekt-ID und der URL der Übersetzungsdateien.]({% image_buster /assets/img/lokalise/3_lokalise_braze_app.png %})

In der **Translation File URL** veröffentlicht Lokalise eine JSON-Datei mit allen Übersetzungen für Ihre Schlüssel im Projekt. Sie erhalten so viele URLs von Übersetzungsdateien, wie Sie Zielsprachen in Ihrem Projekt haben. Aus diesem Grund bestehen die URLs der Übersetzungsdateien aus zwei Teilen:

1. Der erste Teil des URL-Pfads ist für alle Sprachen gleich.
2. Der JSON-Dateiname am Ende der URL basiert auf dem Sprachcode.

Die URL der Übersetzungsdatei ist die URL, die Sie benötigen, wenn Sie eine Braze-Campaign konfigurieren. Sie können den Inhalt der JSON-Datei aktualisieren, indem Sie auf **Refresh** klicken. Beachten Sie, dass die URL gleich bleibt und Sie Ihren Connected-Content-Aufruf in Braze nicht ändern müssen.

##### Test-URL

Um diese URL zu testen, kopieren Sie sie und ersetzen Sie {% raw %}`{{${language}}}`{% endraw %} durch einen Sprachcode (z. B. `en`) und öffnen Sie diese URL in Ihrem Browser. Sie sehen dann eine JSON-Datei mit Ihren Schlüsseln und Übersetzungen:

![]({% image_buster /assets/img/lokalise/4_testing_json_lokalise.png %})

#### 4. Schritt: Übersetzungen in der Braze-Campaign verwenden {#step-4-use-translations-in-braze-campaign}

##### Connected-Content-Aufruf einfügen {#insert-connected-content-call}

Wenn Sie fertig sind, kehren Sie zu Braze zurück und öffnen eine bestehende Campaign oder erstellen eine neue. Für dieses Beispiel erstellen wir eine neue E-Mail-Campaign mit Beispielinhalten. Klicken Sie auf **Edit Email Body**.

Um Ihre Übersetzungen einzufügen, müssen Sie die Connected-Content-Anfrage in den HTML-Code einfügen, entweder am Anfang des Dokuments oder direkt vor der ersten Stelle, an der eine Übersetzung benötigt wird. Dies kann durch Einfügen des folgenden Markups geschehen:

{% raw %}
`{% connected_content https://exports.live.lokalise.cloud/braze/123abc/456xyz/{{${language}}}.json :save translations %}`
{% endraw %}

Ersetzen Sie die URL `https://exports.live.lokalise.cloud/...` durch die URL der Übersetzungsdatei, die Sie im vorherigen Schritt abgerufen haben.

{% raw %}

- `{{${language}}}` bedeutet „Nutzer:innen-Sprache an dieser Stelle einfügen“. Alternativ können Sie den Sprachcode auch fest codieren, z. B. `en.json`.
  - Um sicherzustellen, dass für jede:n Nutzer:in die passende übersetzte JSON-Datei abgerufen wird, müssen Sie entweder das Profilattribut `{{${language}}}` oder ein ähnliches angepasstes Attribut, das die Sprache der Nutzer:innen enthält, an das Ende der URL der Übersetzungsdateien setzen (z. B. `/{{${language}}}.json`). Die in diesen Attributen enthaltenen Werte müssen mit dem Präfix jeder der übersetzten JSON-Dateien übereinstimmen. So wird sichergestellt, dass für jede:n Nutzer:in die richtige Übersetzungsdatei zurückgegeben wird.
- `:save translations` speichert den JSON-Inhalt unter der Variable „translations“.

##### Übersetzungen anzeigen {#display-translations}

Verwenden Sie nun die Variable „translations“, um die gewünschten Übersetzungen nach ihren Schlüsseln anzuzeigen.

Um zum Beispiel den Schlüssel `description` anzuzeigen, verwenden Sie `{{ translations.description }}`.

{% endraw %}
![]({% image_buster /assets/img/lokalise/6_integration_usage_sample.png %})

Zum Schluss speichern Sie das E-Mail-Template und zeigen es in der Vorschau an. Sie sollten sehen, dass Ihre Übersetzung angezeigt wird.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Was passiert, wenn ich versehentlich einen Schlüssel aus Lokalise lösche? {#what-happens-if-i-accidentally-delete-a-key-from-lokalise}

Für den entsprechenden String auf Braze gibt es dann keine Übersetzung mehr.

### Wenn ich eine `en`-Lokalisierung habe, diese aber mit `en-US` auf Lokalise überschreibe, wird Braze sie dann als `en-US` lesen? {#if-i-have-an-en-locale-but-override-it-with-en-us-on-lokalise-will-braze-read-it-as-en-us}

Nein, die ISO-Codes der Lokalisierung müssen auf Braze und Lokalise übereinstimmen.

### Können wir das Flag `:rerender` verwenden, wenn wir Lokalise-Inhalte verbinden? {#can-we-use-the-rerender-flag-when-connecting-lokalise-content}

Ja, selbstverständlich. Sie können in der Braze-Dokumentation nachlesen, wie Sie dieses Flag hinzufügen können.

### Warum kann ich nach dem Aktualisieren der Übersetzungsdatei auf Lokalise keine Änderungen an den übersetzten Inhalten auf Braze sehen? {#after-refreshing-the-translation-file-on-lokalise-why-cant-i-see-any-changes-in-the-translated-content-on-braze}

Braze speichert übersetzte Inhalte im Cache. Die Aktualisierung kann einige Minuten dauern. Wenn Sie Ihre Campaigns testen und die Ergebnisse der Übersetzungen sofort sehen müssen, können Sie den Parameter `:cache_max_age` verwenden, wie in diesem Referenzartikel beschrieben.