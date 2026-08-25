---
nav_title: Katalog erstellen
article_title: Katalog erstellen
alias: "/catalogs/"
page_order: 1
description: "In diesem Referenzartikel erfahren Sie, wie Sie Kataloge erstellen, die über Liquid auf Nicht-Nutzerdaten in Ihren Braze-Campaigns verweisen."
---

# Katalog erstellen {#create-a-catalog}

> Um einen Katalog zu erstellen, importieren Sie eine CSV-Datei mit Nicht-Nutzerdaten in Braze. Anschließend können Sie auf diese Informationen zugreifen, um Ihre Nachrichten anzureichern. Sie können jede Art von Daten in einen Katalog einbringen. Bei diesen Daten handelt es sich in der Regel um Metadaten Ihres Unternehmens, z. B. Produktinformationen für ein E-Commerce-Unternehmen oder Kursinformationen für einen Bildungsanbieter.

## Anwendungsfälle {#use-cases}

Gängige Anwendungsfälle für Kataloge umfassen:

- Produkte
- Serviceleistungen
- Lebensmittel
- Bevorstehende Events
- Musik
- Pakete

Nachdem diese Informationen importiert wurden, können Sie in Ihren Nachrichten darauf zugreifen – auf ähnliche Weise wie auf angepasste Attribute oder Event-Eigenschaften über Liquid.

## Unterstützte Datentypen {#supported-data-types}

Die folgende Tabelle listet die unterstützten Katalogdatentypen auf und zeigt, wie sie erstellt oder aktualisiert werden können.

| Datentyp | Beschreibung | Verfügbar per CSV-Upload | Verfügbar per API und CDI |
|--------------|-----------------------------------------------|:------------------------:|:-------------------------:|
| String | Eine Zeichenfolge. | ✅ Ja | ✅ Ja |
| Zahl | Ein numerischer Wert, entweder Ganzzahl oder Gleitkommazahl. | ✅ Ja | ✅ Ja |
| Boolescher Wert | Ein `true`- oder `false`-Wert. | ✅ Ja | ✅ Ja |
| Zeitangabe | Ein String im [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)-Format. | ✅ Ja | ✅ Ja |
| Geolocation | Ein `[longitude, latitude]`-Koordinaten-Array. Der Breitengrad muss zwischen -90 und 90 liegen; der Längengrad muss zwischen -180 und 180 liegen. Beispiel: `[-73.988103, 40.779109]`. | ✅ Ja | ✅ Ja |
| JSON-Objekt | Ein verschachteltes Objekt mit Schlüssel-Wert-Paaren. Kann in der Plattform angezeigt, aber nur über die API oder CDI erstellt oder aktualisiert werden. | ⛔ Nein | ✅ Ja |
| String-Array | Eine Liste von Strings. Kann in der Plattform angezeigt, aber nur über die API oder CDI erstellt oder aktualisiert werden. Maximal 100 Elemente. | ⛔ Nein | ✅ Ja |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Einen Katalog erstellen {#creating-a-catalog}

Um einen Katalog zu erstellen, gehen Sie zu **Dateneinstellungen** > **Kataloge** und wählen Sie dann **Neuen Katalog erstellen** und eine der folgenden Optionen:

{% tabs local %}
{% tab CSV hochladen %}
### Schritt 1: CSV-Datei überprüfen {#step-1-review-your-csv-file}

Bevor Sie Ihre CSV-Datei hochladen, stellen Sie sicher, dass sie die folgenden Anforderungen erfüllt:

| CSV-Anforderung | Details |
|-----------------|---------|
| Kopfzeilen | Die erste Spalte in der CSV-Datei muss `id` heißen, und jede Zeile muss einen eindeutigen `id`-Wert haben. |
| Spalten | Eine CSV-Datei kann maximal 1.000 Felder (Spalten) enthalten, und jeder Spaltenname kann bis zu 250 Zeichen lang sein. |
| Dateigröße | Beim Free-Plan ist die Gesamtgröße aller CSV-Dateien eines Unternehmens auf 500 MB begrenzt. Beim Pro-Plan beträgt die maximale Dateigröße für eine einzelne CSV-Datei 2 GB. |
| Feldwerte | Jede Zelle (Feldwert) kann bis zu 5.000 Zeichen enthalten. |
| Gültige Zeichen | Die Spalte `id` und alle Kopfzeilenwerte dürfen nur Buchstaben, Zahlen, Bindestriche und Unterstriche enthalten. |
| Datentypen | Unterstützte Datentypen für CSV-Uploads sind String, Zahl, Boolean, Zeit und Geolocation. Die vollständige Liste der Datentypen, einschließlich derjenigen, die nur über die API und CDI verfügbar sind, finden Sie unter [Unterstützte Datentypen](#supported-data-types). |
| Formatierung | Formatieren Sie den gesamten Text in Kleinbuchstaben, um die Konsistenz zu gewährleisten. |
| Kodierung | Speichern und laden Sie die CSV-Datei mit UTF-8-Kodierung hoch. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
Benötigen Sie mehr Speicherplatz für Ihre CSV-Dateien? Wenden Sie sich an Ihren Braze Account Manager, um mehr über das Upgrade Ihrer Kataloge zu erfahren.
{% endalert %}

### Schritt 2: CSV hochladen {#step-2-upload-csv}

Ziehen Sie Ihre Datei per Drag-and-Drop in den Upload-Bereich oder wählen Sie **CSV hochladen** und wählen Sie Ihre Datei aus.

![Ziehen Sie Ihre Datei per Drag-and-Drop in den Upload-Bereich oder wählen Sie „CSV hochladen“ und wählen Sie Ihre Datei aus.]({% image_buster /assets/img_archive/catalog_CSV_upload.png %}){: style="max-width:80%;"}

Wählen Sie einen Datentyp für jede Spalte aus.

{% alert note %}
Dieser Datentyp kann nach der Einrichtung Ihres Katalogs nicht mehr bearbeitet werden. Außerdem wird ein `NULL`-Wert beim CSV-Upload nicht unterstützt und als String behandelt.
{% endalert %}

![Dieser Datentyp kann nach der Einrichtung Ihres Katalogs nicht mehr bearbeitet werden. Außerdem wird ein NULL-Wert beim CSV-Upload nicht unterstützt und als String behandelt.]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:80%;"}

Geben Sie einen Namen und eine optionale Beschreibung für Ihren Katalog ein. Beachten Sie die folgenden Anforderungen bei der Benennung Ihres Katalogs:

  - Muss eindeutig sein
  - Maximal 250 Zeichen
  - Darf nur Zahlen, Buchstaben, Bindestriche und Unterstriche enthalten

{% alert tip %}
Sie können auch [Templates in einem Katalognamen verwenden](#template-catalog-names), um Katalognamen dynamisch basierend auf Variablen wie Sprache oder Campaign zu generieren.
{% endalert %}

![Ein Katalog mit dem Namen „my_catalog“.]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}

Wählen Sie **Katalog verarbeiten**, um den Katalog zu erstellen.

{% alert important %}
Ihre CSV-Datei kann abgelehnt werden, wenn Sie die Grenzen Ihres [Tarifs](#tiers) überschreiten.
{% endalert %}

### Tutorial: Einen Katalog aus einer CSV-Datei erstellen {#tutorial-creating-a-catalog-from-a-csv-file}

In diesem Tutorial verwenden wir einen Katalog, der zwei Spiele, deren Kosten und einen Bildlink auflistet.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg" aria-label="Tutorial: Einen Katalog aus einer CSV-Datei erstellen">
<thead>
  <tr>
    <th class="tg-0pky">id</th>
    <th class="tg-0pky">title</th>
    <th class="tg-0pky">price</th>
    <th class="tg-0pky">image_link</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">1234</td>
    <td class="tg-0pky">Tales</td>
    <td class="tg-0pky">7.49</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
  <tr>
    <td class="tg-0pky">1235</td>
    <td class="tg-0pky">Regeneration</td>
    <td class="tg-0pky">22.49</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
</tbody>
</table>

Wir erstellen den Katalog, indem wir eine CSV-Datei hochladen. Die Datentypen für `id`, `title`, `price` und `image_link` sind String, String, Zahl bzw. String.

{% alert note %}
Dieser Datentyp kann nach der Einrichtung Ihres Katalogs nicht mehr bearbeitet werden.
{% endalert %}

![Vier Katalogspaltennamen: „id“, „title“, „price“, „image_link“.]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:85%;"}

Als Nächstes benennen wir diesen Katalog „games_catalog“ und wählen den Button **Katalog verarbeiten**. Braze prüft den Katalog dann vor der Erstellung auf Fehler.

![Ein Katalog mit dem Namen „games_catalog“.]({% image_buster /assets/img_archive/catalog_new_name.png %}){: style="max-width:85%;"}

Beachten Sie, dass Sie diesen Namen nach der Erstellung des Katalogs nicht mehr bearbeiten können. Sie können einen Katalog löschen und eine aktualisierte Version mit demselben Katalognamen erneut hochladen.

Nachdem Sie den Katalog erstellt haben, können Sie damit beginnen, den [Katalog in einer Campaign]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs) zu referenzieren.

{% alert important %}
Zuvor hochgeladene CSV-Dateien stehen auf der Seite **Kataloge** 30 Tage ab dem Upload-Datum zum Download bereit. Nach 30 Tagen wird die Datei dauerhaft gelöscht und ist nicht mehr zugänglich.
{% endalert %}
{% endtab %}

{% tab Im Browser erstellen %}
### Voraussetzungen {#prerequisites}

Bevor Sie Kataloge im Browser bearbeiten oder erstellen können, benötigen Sie die folgenden [Nutzerberechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) für Ihren Workspace:

- Kataloge anzeigen
- Kataloge bearbeiten
- Kataloge exportieren
- Kataloge löschen

### Schritt 1: Katalogdetails eingeben {#step-1-enter-catalog-details}

Geben Sie einen Namen und eine optionale Beschreibung für Ihren Katalog ein. Beachten Sie die folgenden Anforderungen bei der Benennung Ihres Katalogs:

- Muss eindeutig sein
- Maximal 250 Zeichen
- Darf nur Zahlen, Buchstaben, Bindestriche und Unterstriche enthalten

{% alert tip %}
Sie können auch [Templates in einem Katalognamen verwenden](#template-catalog-names), um Katalognamen dynamisch basierend auf Variablen wie Sprache oder Campaign zu generieren.
{% endalert %}

![Ein Katalog mit dem Namen „my_catalog“.]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}

### Schritt 2: Katalog erstellen {#step-2-create-your-catalog}

Wählen Sie Ihren Katalog aus der Liste und dann **Katalog aktualisieren** > **Felder hinzufügen**. Geben Sie den **Feldnamen** ein und verwenden Sie das Dropdown-Menü, um den Datentyp auszuwählen. Wiederholen Sie den Vorgang nach Bedarf.

![Zwei Beispielfelder „rating“ und „name“.]({% image_buster /assets/img_archive/add_catalog_fields.png %}){: style="max-width:50%;"}

Wählen Sie **Katalog aktualisieren** > **Artikel hinzufügen**, um einen Artikel zu Ihrem Katalog hinzuzufügen, indem Sie die Informationen basierend auf den zuvor hinzugefügten Feldern eingeben. Wählen Sie dann **Artikel speichern** oder **Speichern und weiteren hinzufügen**, um weitere Artikel hinzuzufügen.

![Einen Katalogartikel hinzufügen.]({% image_buster /assets/img_archive/add_catalog_items.png %}){: style="max-width:50%;"}

{% alert note %}
Braze verarbeitet Zeitwerte basierend auf dem Dashboard-Zeitstempel. Wenn beispielsweise eine Spalte den Wert „03/13/2024“ enthält und Ihre Zeitzone die pazifische Zeitzone ist, wird diese Zeit als „12. Mär. 2024, 17:00 Uhr“ in Braze importiert.
{% endalert %}
{% endtab %}
{% endtabs %}

## Katalog-Datentypen {#catalog-data-types}

Kataloge unterstützen verschiedene Datentypen, die Ihnen helfen, Ihre Daten effektiv zu organisieren und zu strukturieren. Die folgende Tabelle beschreibt jeden unterstützten Datentyp und wie er den CSV- und API-Typnamen zugeordnet wird:

| Datentyp | Format | Beispiel | Beschreibung |
|----------|--------|----------|--------------|
| String | Text | `"Hello World"` | Eine beliebige Zeichenfolge, die für Textdaten wie Namen, Beschreibungen und IDs verwendet wird. Entspricht dem Typ `string` in CSV- und API-Importen. |
| Zeit | ISO 8601 oder Unix-Zeitstempel (Sekunden) | `"2024-03-15T14:30:00Z"` | Datums- und Zeitwerte, formatiert als ISO 8601 oder Unix-Zeitstempel in Sekunden. Entspricht dem Typ `time` in der API und dem Typ `datetime` in CSV-Importen. |
| Boolean | `true` oder `false` | `true` | Logische Werte, die „wahr“ oder „falsch“ darstellen. Entspricht dem Typ `boolean` in CSV- und API-Importen. |
| Nummer | Ganzzahl oder Dezimalzahl | `42` oder `19.99` | Numerische Werte einschließlich Ganzzahlen und Gleitkommazahlen für Preise, Mengen, Bewertungen und mehr. Entspricht den Typen `integer` und `float` in CSV-Importen und dem Typ `number` in der API. |
| Geolocation | `[longitude, latitude]`-Array | `[-73.988103, 40.779109]` | Ein Koordinatenpaar, das einen geografischen Standort darstellt. Der Längengrad muss zwischen -180 und 180 liegen; der Breitengrad muss zwischen -90 und 90 liegen. Der API-`type`-Wert ist `geo`. Kann über den Bereich **Add Fields** in der Katalog-UI, per CSV-Upload oder über die REST API hinzugefügt werden. |
| Objekt | JSON-Objekt | `{"key": "value", "price": 10}` | Komplexe, verschachtelte Datenstrukturen. Der API-`type`-Wert ist `object`. Wird im Dashboard als JSON Object angezeigt. Nur über die API oder Cloud Data Ingestion (CDI) verfügbar. |
| Array | String-Array | `["red", "blue", "green"]` | Listen von String-Werten. Der API-`type`-Wert ist `array`. Wird im Dashboard als String array angezeigt. Nur über die API oder CDI verfügbar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

## Verwendung von Templates in Katalognamen {#template-catalog-names}

Bei der Benennung Ihres Katalogs können Sie auch Templates in einem Katalognamen verwenden. Auf diese Weise können Sie Katalognamen dynamisch auf der Grundlage von Variablen wie Sprache oder Campaign generieren. Sie können zum Beispiel Folgendes verwenden:

{% raw %}
```liquid
{% assign language = "content_spanish" %}

{% catalog_items {{language}} fall_campaign %}
{{ items[0].body }}
```
{% endraw %}

## Kataloge verwalten {#managing-catalogs}

### Im Dashboard {#in-the-dashboard}

Um Ihren Katalog nach dem Hochladen einer CSV-Datei oder dem Erstellen eines Katalogs im Browser zu aktualisieren, wählen Sie **Katalog aktualisieren > CSV hochladen** und dann, ob Sie Artikel in Ihrem Katalog aktualisieren, hinzufügen oder löschen möchten.

### Über die REST API {#using-the-rest-api}

Wenn Sie weitere Kataloge erstellen, können Sie auch den [Endpunkt „Kataloge auflisten“]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) verwenden, um eine Liste der Kataloge in einem Workspace zurückzugeben.

Die REST API unterstützt alle [Katalog-Datentypen](#supported-data-types), einschließlich JSON-Objekte und String-Arrays. JSON-Objekte und String-Arrays können nur über die REST API erstellt oder aktualisiert werden.

### Über Cloud Data Ingestion {#using-cloud-data-ingestion}

Sie können Kataloge über [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data) pflegen, indem Sie Katalogdaten direkt aus Ihrem Data Warehouse (wie Snowflake, Redshift, BigQuery, Databricks, Microsoft Fabric oder S3) planmäßig synchronisieren.

## Katalogartikel verwalten {#managing-catalog-items}

Zusätzlich zur Verwaltung Ihrer Kataloge können Sie auch asynchrone und synchrone Endpunkte verwenden, um die Katalogartikel zu verwalten. Dazu gehört die Möglichkeit, Katalogartikel zu bearbeiten und zu löschen sowie Details zu Katalogartikeln aufzulisten.

Wenn Sie beispielsweise einen einzelnen Katalogartikel bearbeiten möchten, können Sie den [`/catalogs/catalog_name/items/item_id`-Endpunkt]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item) verwenden.

## Katalogspeicher {#tiers}

Die kostenlose Version von Catalogs unterstützt CSV-Dateien mit einer Gesamtgröße von bis zu 500 MB für alle CSV-Dateien in Ihrem Unternehmen, während die Catalogs-Pro-Version CSV-Dateien mit einer Größe von bis zu 2 GB für eine einzelne CSV-Datei unterstützt.

{% alert important %}
Der im Braze-Dashboard angezeigte Paketanspruch wird aus optischen Gründen auf die nächste Einheit gerundet; Sie haben jedoch weiterhin Anspruch auf den vollen erworbenen Umfang. Um ein Upgrade für den Katalogspeicher anzufordern, wenden Sie sich an Ihren Braze Account Manager.
{% endalert %}

### Kostenlose Version {#free-version}

Die Speichergröße der kostenlosen Version von Catalogs beträgt bis zu 500&nbsp;MB. Sie können eine unbegrenzte Anzahl von Artikeln haben, solange sie unter 500&nbsp;MB bleiben.

#### Catalogs Pro {#catalogs-pro}

Auf Unternehmensebene richtet sich der maximale Speicherplatz für Catalogs Pro nach der Größe der Katalogdaten. Die verfügbaren Speichergrößen sind: 5&nbsp;GB, 10&nbsp;GB oder 15&nbsp;GB. Beachten Sie, dass der Speicherplatz der kostenlosen Version (500&nbsp;MB) in jedem dieser Tarife enthalten ist.

## Spezifikationen {#specifications}

Die folgende Tabelle fasst die Spezifikationen zusammen, was Sie in Katalogen einfügen können.

| Bereich | Spezifikationen |
|------|-----------|
| Zeichenanzahl für Artikelwerte | Bis zu 5.000 Zeichen in einem einzelnen Wert. Wenn Sie beispielsweise ein Feld mit der Bezeichnung `description` haben, beträgt die maximale Zeichenanzahl innerhalb des Feldes 5.000. |
| Zeichenanzahl für Artikelspaltennamen | Bis zu 250 Zeichen |
| Selections pro Katalog | Bis zu 30 Selections pro Katalog |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Katalog-Liquid-Tags können nicht rekursiv verwendet werden. Das bedeutet, dass Sie keinen Katalogartikel referenzieren können, der dann innerhalb derselben Liquid-Auswertung einen zweiten Katalogartikel aufruft.
{% endalert %}