---
nav_title: Lokalisierung
article_title: Lokalisierung
page_order: 8
description: "Dieser Referenzartikel behandelt die Grundlagen der Lokalisierung, listet die Vorteile verschiedener Orchestrierungsansätze für Campaigns und Canvases auf und beschreibt verschiedene Möglichkeiten, wie Nutzer:innen die Personalisierung in ihrem Messaging handhaben können."
tool:
    - Campaigns
    - Canvas
---

# Lokalisierung {#localization}

> Für Unternehmen mit Kund:innen in vielen Ländern kann eine frühzeitige Lokalisierung auf Ihrer Braze-Journey Zeit und Ressourcen sparen.

## Funktionsweise {#how-it-works}

Locale-Informationen werden im Profil von Nutzer:innen gespeichert, basierend auf Daten, die Sie über ein [Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration) (automatisch) oder die [REST API]({{ site.baseurl }}/api/endpoints/user_data/post_user_track) erfassen. Das Locale enthält die Sprache und eine Regionskennung. Diese Informationen sind im Braze-Segmentierungs-Tool unter **Country** und **Language** verfügbar.

{% alert tip %}
Technische Details zur Erfassung des Locales durch unsere SDKs finden Sie in der offiziellen Dokumentation für [iOS](https://developer.apple.com/library/ios/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html), [Android](http://developer.android.com/reference/java/util/Locale.html) und [Web](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/language).
{% endalert %}

## Übersetzungsverwaltung {#translation-management}

Berücksichtigen Sie die folgenden Ansätze für die Verwaltung Ihrer Übersetzungen.

{% tabs local %}
{% tab Campaign %}
### Ein Template für alle {#one-template-for-all}

Bei diesem Ansatz wird die Lokalisierung mithilfe von [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) auf ein einzelnes Template in Braze angewendet. Nach dem Versand stellt das Dashboard aggregierte Campaign-Analytics bereit. Das Engagement auf Nutzer:innenebene kann mithilfe angepasster Segment-Funnel gemessen werden, z. B. durch die Kombination der Filter **Land** und **Campaign erhalten**.

| Vorteile | Überlegungen |
| --- | --- |
| - Zentralisierter Ansatz<br>- Reduzierte E-Mail-Erstellungszeit, kein Bedarf, eine E-Mail mehrfach zu erstellen | - Manueller Berichtsaufbau<br>- Campaign-Bericht zeigt aggregierte Metriken statt Metriken pro Land<br>- Liquid muss gründlich getestet werden, um sicherzustellen, dass es wie erwartet befüllt wird<br>- Je nachdem, wie Sie den Länderwert abrufen oder wie viele Länder Sie eingerichtet haben, kann es schwierig sein, jedes Land zu testen<br>- Schwieriger, Versendungen für bestimmte Zeiten über Zeitzonen hinweg zu planen<br>- Schwieriger zu verwenden, wenn Sie separate Inhalte pro Land senden möchten. |
| --- | --- | --- |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ein Template für alle" }

### Ein Template pro Land {#one-template-per-country}

Bei diesem Ansatz werden Templates in verschiedene Versandregionen aufgeteilt. Nach dem Versand zeigt das Dashboard die Versandanalysen für jedes Land separat an, und alle nachgelagerten [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents#how-to-access-currents)-Ereignisse auf Nutzer:innenebene werden ebenfalls einer bestimmten Campaign zugeordnet.

- Templates profitieren von der Implementierung von [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) für Wartungs- und Tracking-Zwecke.
- Campaigns können die Konfigurationen desselben [Braze-Templates]({{site.baseurl}}/user_guide/messaging/templates) und derselben [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) übernehmen (z. B. [E-Mail-Templates]({{site.baseurl}}/user_guide/messaging/templates/email_templates), die Liquid enthalten).
- Bereits vorhandene Campaigns und Templates können [dupliziert]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/duplicating) werden, um eine schnellere Wertschöpfung zu ermöglichen.

| Vorteile | Überlegungen |
| --- | --- |
| - Skalierbar auf mehrere Standorte<br>- Berichterstattung über Umsatz pro Land innerhalb von Braze (z. B. pro Campaign)<br>- Flexibilität, wenn sich die Inhalte pro Land stark unterscheiden | - Erfordert strategische Strukturierung<br>- Mehr Erstellungsaufwand erforderlich (z. B. separate Campaigns für jedes Land) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ein Template pro Land" }
{% endtab %}

{% tab Canvas %}
### Eine Journey für alle {#one-journey-for-all}

Bei diesem Ansatz wird die Lokalisierung innerhalb der [Canvas-Grundlagen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_basics#building-the-customer-journey) und mit Liquid gehandhabt, um das Messaging für jede:n Nutzer:in zu definieren.

Nach dem Versand eines Canvas stellt das Dashboard aggregierte [Canvas-Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics) bereit, während das Engagement auf Nutzer:innenebene über angepasste [Segment-Funnel]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size) gemessen werden kann, z. B. durch die Kombination der Filter [**Land**]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#country) und [**Canvas-Schritt erhalten**]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#received-message-from-canvas-step).

| Vorteile | Überlegungen |
| --- | --- |
| - Zentralisierter Ansatz<br>- Reduzierte E-Mail-Erstellungszeit – kein Bedarf, eine E-Mail mehrfach zu erstellen. | - Manueller Berichtsaufbau<br>- Canvas-Bericht zeigt aggregierte Metriken statt Metriken pro Land<br>- Liquid muss gründlich getestet werden, um sicherzustellen, dass es wie erwartet befüllt wird<br>- Je nachdem, wie Sie den Länderwert abrufen oder wie viele Länder Sie eingerichtet haben, kann es schwierig sein, jedes Land zu testen<br>- Schwieriger, Versendungen für bestimmte Zeiten über Zeitzonen hinweg zu planen<br>- Schwieriger zu verwenden, wenn Sie separate Inhalte pro Land senden möchten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eine Journey für alle" }

### Eine Journey pro Land {#one-journey-per-country}

Bei diesem Ansatz bietet der [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)-Journey-Builder die Flexibilität, Nutzer:innen-Journeys über mehrere [Canvas-Komponenten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components) zu erstellen. Diese Komponenten können auf Komponenten- und Gesamtjourney-Ebene [dupliziert]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/duplicating) werden.

Die Lokalisierung kann mit den folgenden Methoden erreicht werden:

- Separate Canvases pro Land – so wird sichergestellt, dass die komplexen Nutzer:innen-Journeys am Anfang des Funnels mithilfe von Zielgruppenfiltern definiert werden
- Maßgeschneiderte Nutzer:innen-Journeys pro Land – die Implementierung von [Zielgruppenpfaden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths), um Nutzer:innen intuitiv in großem Umfang für jede Journey zu segmentieren, indem separate Nachrichtenstränge für jedes Land in einem einzigen Canvas erstellt werden

Nach dem Versand stellt das Dashboard dynamische Analytics pro Land bereit, und innerhalb der [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents#how-to-access-currents)-Ereignisse auf Nutzer:innenebene basierend auf dem aktuellen Standort der Kund:innen.

| Vorteile | Überlegungen |
| --- | --- |
| - Berichterstattung über Umsatz pro Land innerhalb von Braze (z. B. pro Canvas, Variante oder Schritt)<br>- Flexibilität, wenn sich die Inhalte pro Land stark unterscheiden<br>- Weitere Kanäle können in Zukunft als Teil der Journey hinzugefügt werden | - Erfordert strategische Strukturierung<br>- Mehr Erstellungsaufwand erforderlich (z. B. separate Nachrichtenschritte für jedes Land)<br>- Canvas kann groß und schwer lesbar werden, wenn Sie angepasste, komplexe Journeys für jedes Land in einem einzigen Canvas haben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eine Journey pro Land" }
{% endtab %}
{% endtabs %}

## Übersetzte Nachrichten senden {#sending-translated-messages}

Um personalisierte Nachrichten basierend auf der Sprache, dem Locale oder angepassten Attributen von Nutzer:innen zu senden, verwenden Sie eine der folgenden Methoden.

### Übersetzungs-Liquid-Tags (empfohlen) {#translation-liquid-tag}

Braze unterstützt einen {% raw %}`{% translation salutation %}Hello!{% endtranslation %}`{% endraw %} Liquid-Tag, um Nutzer:innen in verschiedenen Sprachen mit einer einzigen Nachricht anzusprechen.

Eine vollständige Anleitung finden Sie im [Leitfaden zur Verwendung von Übersetzungs-Tags]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

### Alternative Ansätze {#alternative-approaches}

{% tabs local %}
{% tab Angepasstes Liquid %}
Sie können Ihre Inhalte manuell in den Nachrichtentext einfügen und [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) verwenden, um die richtige Sprache [bedingt]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#conditional-logic) für die Empfänger:innen anzuzeigen. Gehen Sie dazu wie folgt vor:

1. Verfassen Sie Ihre Nachricht und wählen Sie dann **Sprache** aus, um bedingte Liquid-Logik für jede Ihrer ausgewählten Sprachen zu generieren.
2. Sie können das folgende Liquid-Template verwenden, um Ihre Nachricht aufzubauen. Für jedes Feld mit Templating sollten Sie die Variationen nach dem eingeklammerten Templating-Abschnitt eingeben. Die Variation sollte dem Sprachcode entsprechen, der in den Klammern davor referenziert wird.
    {% raw %}
    ```liquid
    {% if ${language} == 'en' %}
    This is a message in English from Braze!
    {% elsif ${language} == 'es' %}
    Este es un mensaje en español de Braze !
    {% elsif ${language} == 'zh' %}
    这是一条来自Braze的中文消息。
    {% else %}
    This is a message from Braze! This will go to anyone who does not match the other specified languages!
    {% endif %}
    ```
    {% endraw %}
3. Testen Sie Ihre Nachricht vor dem Senden, indem Sie die ID oder E-Mail-Adresse von Nutzer:innen eingeben, um zu prüfen, wie eine Nachricht je nach Sprache für eine Person aussehen würde.

{% alert tip %}
Wir empfehlen immer, eine {% raw %}`{% else %}`{% endraw %}-Anweisung in Ihre Nachrichten einzufügen. Während die meisten Nutzer:innen Nachrichten in ihrer spezifischen Sprache sehen werden, ist der Text für diejenigen sichtbar, die:
- Keine Sprache ausgewählt haben
- Eine Sprache haben, die Braze nicht unterstützt
- Ein Gerät haben, bei dem die Sprache nicht erkannt werden kann
{% endalert %}
{% endtab %}

{% tab Content Blocks %}
Braze [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) sind wiederverwendbare Inhaltsblöcke. Wenn ein Block geändert wird, ändern sich alle Referenzen auf diesen Block. Zum Beispiel werden Aktualisierungen an einem E-Mail-Header oder einer Fußzeile in allen E-Mails widergespiegelt oder können Übersetzungen beherbergen. Diese Blöcke können auch über die REST API [erstellt]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) und [aktualisiert]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block) werden, und Nutzer:innen können Übersetzungen programmatisch hochladen.

Beim Erstellen einer Campaign im Dashboard können Content Blocks mit dem Tag {% raw %}`{{content_blocks.${name_of_content_block}}}`{% endraw %} referenziert werden. Diese Blöcke können alle Übersetzungen innerhalb bedingter Logik für jede Sprache enthalten, wie in Option 1 gezeigt, oder es kann ein separater Block für jede Sprache verwendet werden.

Content Blocks können auch als Übersetzungsmanagement-Prozess genutzt werden, bei dem Inhalte, die übersetzt werden müssen, in einem Content-Block gespeichert, abgerufen, übersetzt und dann aktualisiert werden:
1. Erstellen Sie manuell einen Content-Block im Dashboard mit dem Tag „Needs Translation“.
2. Ihr Dienst führt einen nächtlichen Abruf aller Content Blocks über den [`/content_blocks/list`-Endpunkt]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) durch.
3. Ihr Dienst ruft Details zu jedem Content-Block über den [`/content_blocks/info`-Endpunkt]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) ab, um zu sehen, welche Blöcke zur Übersetzung markiert sind.
4. Ihr Übersetzungsdienst übersetzt den Inhalt aller Content Blocks mit dem Tag „Needs Translation“.
5. Ihr Dienst ruft den [`/content_block/update`-Endpunkt]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block) auf, um den übersetzten Inhalt zu aktualisieren und den Tag auf „Translation Complete“ zu ändern.
{% endtab %}

{% tab Kataloge %}
[Kataloge]({{site.baseurl}}/user_guide/data/activation/catalogs) ermöglichen es Ihnen, auf Daten aus importierten JSON-Objekten über API und CSV-Dateien zuzugreifen, um Ihre Nachrichten anzureichern – ähnlich wie angepasste Attribute oder angepasste Event-Eigenschaften über Liquid. Zum Beispiel:

{% subtabs local %}
{% subtab API %}

Erstellen Sie einen Katalog über den folgenden API-Aufruf:
```bash
curl --location --request POST 'https://your_api_endpoint/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "catalogs": [
   {
     "name": "translations",
     "description": "My localization samples",
     "fields": [
       {
         "name": "id",
         "type": "string"
       },
       {
         "name": "context",
         "type": "string"
       },
       {
         "name": "language",
         "type": "string"
       },
       {
         "name": "body",
         "type": "string"
       }
     ]
   }
 ]
}'
```

Fügen Sie Artikel über den folgenden API-Aufruf hinzu:

```bash
curl --location --request POST 'https://your_api_endpoint/catalogs/translations/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "items": [
   {
     "id": "1",
     "context": "1",
     "language": "en",
     "body": "Hey"
   },
   {
     "id": "2",
     "context": "1",
     "language": "es",
     "body": "Hola"
   },
   {
     "id": "3",
     "context": "1",
     "language": "pt",
     "body": "Oi"
   },
   {
     "id": "4",
     "context": "1",
     "language": "de",
     "body": "Hallo"
   }
 ]
}'
```
{% endsubtab%}
{% subtab CSV %}
Erstellen Sie eine CSV-Datei im folgenden Format:

| id | context | language | body |
| --- | --- | --- | --- |
| 1 | 1 | en | Hey |
| 2 | 1 | es | Hola |
| 3 | 1 | pt | Oi |
| 4 | 1 | de | Hallo |
| 5 | 2 | en | Hey |
| 6 | 2 | es | Hola |
| 7 | 2 | pt | Oi |
| 8 | 2 | de | Hallo |
| 9 | 3 | en | Hey |
| 10 | 3 | es | Hola |
| 11 | 3 | pt | Oi |
| 12 | 3 | de | Hallo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Alternative Ansätze" }
{% endsubtab %}
{% endsubtabs %}

Diese Katalogartikel können dann über [Personalisierung]({{site.baseurl}}/user_guide/data/activation/catalogs/create) referenziert werden, wie im folgenden Beispiel gezeigt, oder über [Selections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections), mit denen Sie Datengruppen erstellen können.

{% raw %}
```liquid
{% catalog_items translations 1 %}
{{items[0].body}}
//returns “Hey”
```
{% endraw %}
{% endtab %}

{% tab Braze-Partner %}
Viele Braze-Partner bieten Lokalisierungslösungen an, darunter [Transifex]({{site.baseurl}}/partners/message_personalization/localization/transifex#about-the-integration) und [Crowdin](https://crowdin.com/). In der Regel nutzen Nutzer:innen die Plattform zusammen mit einem internen Team und einer Übersetzungsagentur. Diese Übersetzungen werden dort hochgeladen und sind dann über die REST API zugänglich. Diese Dienste nutzen häufig auch [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), sodass Nutzer:innen die Übersetzungen über die API abrufen können.

Zum Beispiel rufen die folgenden Connected-Content-Aufrufe Transifex und Crowdin auf, um eine Übersetzung abzurufen, wobei {% raw %}`{{${language}}}`{% endraw %} verwendet wird, um die richtige Übersetzung für bestimmte Nutzer:innen zu identifizieren. Diese Übersetzung wird dann im JSON-Block „strings“ gespeichert und referenziert.

{% subtabs local %}
{% subtab Transifex-Beispiel %}
{% raw %}
```liquid
{% connected_content https://www.transifex.com/api/2/project/example/resource/example/translation/{{${language}}}/strings :basic_auth semc :save strings %}
{{strings[0].translation}}
```
{% endraw %}
{% endsubtab %}
{% subtab Crowdin-Beispiel %}
{% raw %}
```liquid
{% connected_content https://api.crowdin.com/api/project/braze-test/export-file?key=you_api_key&language={{${language}}}&file=test.json&export_translated_only=1 :save response %}
{{response.value_1}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Tabellenkalkulationen %}
Speichern Sie Übersetzungen in einer Tabellenkalkulation und verwenden Sie dann eine der folgenden Methoden, um Ihre Nachricht in der entsprechenden Sprache zu senden.

{% subtabs local %}
{% subtab Connected Content %}
Sie können mit einer Übersetzungsagentur zusammenarbeiten, um Übersetzungen in einer Google-Tabelle zu speichern, und diesen Inhalt dann über [Braze Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) abfragen. Wenn Sie eine Nachricht senden, wird die entsprechende Übersetzung für alle Nutzer:innen basierend auf ihrer ausgewählten Sprache in Ihren Campaign-Text eingefügt.

{% alert note %}
Die Google Sheets API hat ein Limit von 500 Anfragen pro 100 Sekunden pro Projekt. Connected-Content-Aufrufe können zwischengespeichert werden, aber diese Lösung ist nicht skalierbar für eine Campaign mit hohem Traffic.
{% endalert %}
{% endsubtab %}

{% subtab JSON-API über SheetDB %}
Diese Option bietet eine alternative Methode, um Google Sheets in JSON-Objekte umzuwandeln, die über Connected Content abgefragt werden. Indem Sie eine Tabellenkalkulation über SheetDB in eine JSON-API umwandeln, können Sie aus [mehreren Abo-Stufen](https://sheetdb.io/pricing) je nach Häufigkeit der API-Aufrufe wählen.

Die Tabellenstruktur folgt den Schritten in Option 4, aber SheetDB bietet auch [zusätzliche Filter](https://docs.sheetdb.io/#sheetdb-api), um die Objekte abzufragen.

Einige Nutzer:innen bevorzugen möglicherweise die Implementierung von SheetDB mit weniger Liquid- und Connected-Block-Abhängigkeiten, indem sie die [Suchmethode](https://docs.sheetdb.io/#get-search-in-document) von SheetDB in GET-Anfragen verwenden, um die JSON-Objekte basierend auf dem {% raw %}`{{${language}}}`{% endraw %} Liquid-Tag zu filtern und automatisch die Ergebnisse für eine einzelne Sprache zurückzugeben, anstatt große bedingte Blöcke zu erstellen.

#### Schritt 1: Google-Tabelle formatieren {#step-1-format-the-google-sheet}

Erstellen Sie zunächst die Google-Tabelle so, dass die Sprachen verschiedene Objekte sind:

| language | title1 | body1 | title2 | body2 |
| en | Hey | 1 | Hey2 | 5 |
| es | Hola | 2 | Hola2 | 6 |
| pt | Oi | 3 | Oi2 | 7 |
| de | Hallo | 4 | Hallo2 | 8 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Schritt 1: Google-Tabelle formatieren" }

#### Schritt 2: Den Sprach-Liquid-Tag in einem Connected-Content-Aufruf verwenden {#step-2-use-the-language-liquid-tag-in-a-connected-content-call}

Implementieren Sie als Nächstes den {% raw %}`{{${language}}}`{% endraw %} Liquid-Tag innerhalb eines Connected-Content-Aufrufs. Beachten Sie, dass SheetDB die `sheet_id` automatisch beim Erstellen der Tabellenkalkulation generiert.

{% raw %}
```liquid
{% connected_content https://sheetdb.io/api/v1/[sheet_id]/search?language={{${language}}} :save result%}
```
{% endraw %}

#### Schritt 3: Nachrichten mit Templates erstellen {#step-3-template-your-messages}

Verwenden Sie abschließend Liquid für das Templating Ihrer Nachrichten:

{% raw %}
```liquid
{{result[0].title1}} //returns “Hey”
{{result[0].title2}} //returns “Hey2”
```
{% endraw %}

##### Hinweise {#considerations}

- Das Feld {% raw %}`{{${language}}}`{% endraw %} muss für alle Nutzer:innen definiert sein; andernfalls muss ein bedingter Liquid-Block als Fallback-Handler für Nutzer:innen ohne Sprache eingebunden werden.
- Die Datenmodellierung in Google Sheets muss einer anderen sprachgesteuerten vertikalen Struktur folgen, anstatt Nachrichtenobjekte zu verwenden.
- SheetDB bietet ein begrenztes kostenloses Konto und mehrere kostenpflichtige Optionen, die basierend auf Ihrer Campaign-Strategie berücksichtigt werden sollten.
- Connected-Content-Aufrufe können zwischengespeichert werden. Wir empfehlen, die voraussichtliche Häufigkeit der API-Aufrufe zu messen und einen alternativen Ansatz zu untersuchen, bei dem der Haupt-SheetDB-Endpunkt aufgerufen wird, anstatt die Suchmethode zu verwenden.
{% endsubtab %}
{% subtab JSON-API über Sheetlabs %}

Diese Option wandelt eine Google-Tabelle in eine JSON-API um, die Sie mit Connected Content abfragen können. Sheetlabs unterstützt große Abfragevolumen und bietet kostenlose und kostenpflichtige Stufen.

#### Schritt 1: Übersetzungstabelle in Google Sheets vorbereiten {#step-1-prepare-your-translations-sheet-in-google-sheets}

Erstellen Sie die Google-Tabelle so, dass jede Zeile eine Sprache darstellt. Zum Beispiel:

| language | greeting | title1 | legal1 |
| ---- | ---- | ---- | ---- |
| en | Welcome! | Your exclusive offer is here | ... |
| fr | Bienvenue! | Votre offre exclusive est arrivée | ... |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Schritt 1: Übersetzungstabelle in Google Sheets vorbereiten" }

#### Schritt 2: Sheetlabs verwenden, um die Tabelle zu importieren und eine API zu erstellen {#step-2-use-sheetlabs-to-import-the-sheet-and-create-an-api}

1. Registrierung Sie sich bei [Sheetlabs](https://sheetlabs.com).
2. Folgen Sie den Sheetlabs-Anweisungen, um Daten aus Google Sheets zu importieren.
3. Wählen Sie die Tabellenkalkulation aus, die Sie in Schritt 1 erstellt haben.
4. Wählen Sie **Create a matching API** aus.

#### Schritt 3: Sheetlabs-Authentifizierungstoken zu Braze hinzufügen (optional) {#step-3-add-your-sheetlabs-authentication-token-to-braze-optional}

Wenn Ihre Sheetlabs-API öffentlich ist, überspringen Sie diesen Schritt. Wenn eine Authentifizierung erforderlich ist:

1. Gehen Sie zur Seite **My Account** in Sheetlabs und kopieren Sie Ihren API-Token / Textbaustein.
2. Folgen Sie den Schritten unter [Braze-Authentifizierung mit Basic Auth]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#using-basic-authentication), um eine Basic-Authentication-Anmeldeinformation in Braze zu erstellen. Verwenden Sie Ihren Sheetlabs-Benutzernamen (E-Mail-Adresse) und den kopierten API-Token / Textbaustein.
3. Speichern Sie die Anmeldeinformation mit einem Namen wie `sheetlabs_creds`.

#### Schritt 4: Sheetlabs-API über Connected Content aufrufen {#step-4-call-the-sheetlabs-api-from-connected-content}

Fügen Sie einen Connected-Content-Aufruf an Sheetlabs hinzu. Ersetzen Sie `/XXX/yourapi` durch den Pfad zu der API, die Sie in Schritt 2 erstellt haben.

{% raw %}
```liquid
{% connected_content https://sheetlabs.com/XXX/yourapi?language={{${language}}} :save translations :basic_auth sheetlabs_creds %}

```
{% endraw %}

#### Schritt 5: Nachrichten mit Templates erstellen {#step-5-template-your-messages}

Verwenden Sie Liquid, um die zurückgegebenen Felder zu referenzieren. Zum Beispiel:

{% raw %}
```liquid
{{translations[0].greeting}} {{${first_name}}},
{{translations[0].body1}}
```
{% endraw %}

#### Hinweise

- Definieren Sie das Feld {% raw %}`{{${language}}}`{% endraw %} für alle Nutzer:innen, die Sie zuordnen möchten. Wenn Nutzer:innen keine Sprache festgelegt haben, fügen Sie einen Liquid-Fallback ein.
- Connected-Content-Aufrufe können zwischengespeichert werden. Messen Sie Ihre voraussichtliche API-Häufigkeit bei der Auswahl eines Sheetlabs-Plans.

Weitere Informationen finden Sie unter [Sheetlabs mit Braze verwenden](https://app.sheetlabs.com/docs/producers/braze/).

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}