---
nav_title: Datentypen
article_title: Datentypen
page_order: 1
page_type: reference
description: "Referenz für unterstützte Datentypen für angepasste Attribute, Event-Eigenschaften und Kataloge in Braze."
toc_headers: h2
---

# Datentypen {#data-types}

> Diese Seite fasst die unterstützten Datentypen für angepasste Attribute, Event-Eigenschaften und Kataloge zusammen. Jeder angepasste Datentyp hat leicht unterschiedliche Unterstützung und Einschränkungen.

## Definitionen {#definitions}

Verwenden Sie diese Tabelle, um zu sehen, welche Datentypen Sie für Nutzerprofilattribute, Event-Daten oder Katalogartikel verwenden können. In den folgenden Abschnitten finden Sie Informationen zur Verwendung und zu Einschränkungen für jeden Typ.

<table role="presentation" class="definitions-table reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4 reset-td-br-5">
  <thead>
    <tr>
      <th>Datentyp</th>
      <th>Definition</th>
      <th>Angepasste Attribute</th>
      <th>Event-Eigenschaften</th>
      <th>Kataloge</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Boolescher Wert</td>
      <td>Wert <code>true</code> oder <code>false</code></td>
      <td>✅ Unterstützt</td>
      <td>✅ Unterstützt</td>
      <td>✅ Unterstützt</td>
    </tr>
    <tr>
      <td>Zahl</td>
      <td>Ganzzahl oder Dezimalzahl</td>
      <td>✅ Unterstützt</td>
      <td>✅ Unterstützt</td>
      <td>✅ Unterstützt</td>
    </tr>
    <tr>
      <td>String</td>
      <td>Text; 255 Zeichen oder weniger</td>
      <td>✅ Unterstützt</td>
      <td>✅ Unterstützt</td>
      <td>✅ Unterstützt</td>
    </tr>
    <tr>
      <td>Zeit</td>
      <td>Datum und Uhrzeit in einem Standardformat (<a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a>)</td>
      <td>✅ Unterstützt</td>
      <td>✅ Unterstützt</td>
      <td>✅ Unterstützt</td>
    </tr>
    <tr>
      <td>Array</td>
      <td>Geordnete Liste von Werten</td>
      <td>✅ Unterstützt</td>
      <td>✅ Unterstützt</td>
      <td>✅ Unterstützt</td>
    </tr>
    <tr>
      <td>Objekt</td>
      <td>Strukturierte Daten mit benannten Feldern (verschachtelte Schlüssel-Wert-Paare)</td>
      <td>✅ Unterstützt</td>
      <td>✅ Unterstützt</td>
      <td>✅ Unterstützt</td>
    </tr>
    <tr>
      <td>Array von Objekten</td>
      <td>Liste von Objekten</td>
      <td>✅ Unterstützt</td>
      <td>❌ Nicht unterstützt</td>
      <td>❌ Nicht unterstützt</td>
    </tr>
  </tbody>
</table>

### Wichtige Hinweise {#important-considerations}

- **Array:** Angepasste Attribute und Event-Eigenschaften haben Größenbeschränkungen. Datetimes werden innerhalb von Arrays in Event-Eigenschaften nicht unterstützt. Kataloge unterstützen nur String-Arrays mit maximal 100 Elementen.
- **Objekt:** In Braze wird dies als „verschachtelte angepasste Attribute“ für angepasste Attribute, „verschachtelte Objekte“ für Event-Eigenschaften und „JSON-Objekt“ für Kataloge bezeichnet.
- **Zeit:** In Event-Eigenschaften wird dieser Typ als „Datetime“ bezeichnet.

## Datentypen für angepasste Attribute {#custom-attribute-data-types}

Angepasste Attribute unterstützen die in der Tabelle [Definitionen](#definitions) aufgeführten Datentypen. Im Folgenden werden die Verwendung und Segmentierung für jeden unterstützten Datentyp beschrieben.

{% tabs %}
{% tab Boolescher Wert %}

Sie können angepasste Attribute einzeln über das Aktionsmenü auf die Blockliste setzen oder bis zu 100 Attribute gleichzeitig auswählen und in großen Mengen auf die Blockliste setzen. Wenn Sie ein angepasstes Attribut blockieren, werden keine Daten zu diesem Attribut mehr erfasst, vorhandene Daten sind nicht verfügbar, sofern sie nicht reaktiviert werden, und blockierte Attribute werden nicht in Filtern oder Diagrammen angezeigt. Wenn das Attribut derzeit von Filtern oder Triggern in anderen Bereichen des Braze-Dashboards referenziert wird, erscheint außerdem ein Warnhinweis, der erklärt, dass alle Instanzen der Filter oder Trigger, die darauf verweisen, entfernt und archiviert werden.

### Als personenbezogene Daten (PII) markieren {#marking-as-personally-identifiable-information-pii}

Administrator:innen können auch angepasste Attribute erstellen und sie auf dieser Seite als PII markieren. Diese Attribute sind nur für Administrator:innen und Dashboard-Nutzer:innen mit der Berechtigung „Als PII markierte angepasste Attribute anzeigen“ sichtbar.

### Beschreibungen hinzufügen {#adding-descriptions}

Sie können einem angepassten Attribut nach der Erstellung eine Beschreibung hinzufügen, wenn Sie die [Nutzerberechtigung]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions) `Manage Events, Attributes, Purchases` haben. Bearbeiten Sie das angepasste Attribut und geben Sie ein, was Sie möchten, z. B. eine Notiz für Ihr Team.

### Tags hinzufügen {#adding-tags}

Sie können einem angepassten Attribut nach der Erstellung Tags hinzufügen, wenn Sie die [Nutzerberechtigung]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions) „Manage Events, Attributes, Purchases“ haben. Sie können die Tags dann verwenden, um die Liste der Attribute zu filtern.

### Angepasste Attribute entfernen {#removing-custom-attributes}

Es gibt zwei Möglichkeiten, angepasste Attribute aus Nutzerprofilen zu entfernen:

- Wählen Sie den Namen des zu entfernenden angepassten Attributs in einem [Nutzeraktualisierungs-Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update#removing-custom-attributes) aus.
- Setzen Sie den Wert `null` in Ihrer API-Anfrage an den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

#### Den Wert `null` setzen {#setting-the-null-value}

{% alert important %}
Ein Attribut auf `null` zu setzen und es auf `""` (leerer String) zu setzen, ist nicht dasselbe.
{% endalert %}

- `null` entfernt das Attribut vollständig aus dem Nutzerprofil. Es erscheint nicht im Profil und stimmt mit keinem **IS NOT BLANK**-Filter überein.
- `""` setzt das Attribut auf einen leeren String-Wert. Das Attribut erscheint im Profil mit einem leeren String-Wert, stimmt aber nicht mit **IS NOT BLANK**-Filtern überein (es wird als leer behandelt).

Außerdem ist `""` nur für String-Attribute gültig. Wenn der Datentyp des Attributs im Dashboard auf einen Nicht-String-Typ (wie Boolescher Wert, Zahl oder Zeit) gesetzt ist, löscht das Senden von `""` den Wert nicht – verwenden Sie stattdessen `null`.

### Daten exportieren {#exporting-data}

Um die Liste der angepassten Attribute als CSV-Datei zu exportieren, wählen Sie oben auf der Seite **Export all** aus. Das System generiert eine CSV-Datei und sendet Ihnen einen Download-Link per E-Mail.

## Nutzungsberichte anzeigen {#viewing-usage-reports}

Der Nutzungsbericht listet alle Canvases, Campaigns und Segmente auf, die ein bestimmtes angepasstes Attribut verwenden. Diese Liste enthält keine Verwendungen von Liquid.

Sie können bis zu 100 Nutzungsberichte gleichzeitig anzeigen, indem Sie die Kontrollkästchen neben den jeweiligen angepassten Attributen aktivieren und dann **View usage report** auswählen.

### Registerkarte „Values“ {#values-tab}

Wenn Sie einen Nutzungsbericht anzeigen, wählen Sie die Registerkarte **Values** aus, um die häufigsten Werte der ausgewählten angepassten Attribute basierend auf einer Stichprobe von etwa 250.000 Nutzer:innen anzuzeigen. Da die Ergebnisse aus einer Teilmenge von Nutzer:innen stammen, enthält die Stichprobe nicht alle vorhandenen Werte. Das bedeutet, dass die Registerkarte **Values** nicht für die Fehlerbehebung oder für Anwendungsfälle verwendet werden sollte, die Daten aller Nutzer:innen erfordern.

![Nutzungsbericht für ausgewählte angepasste Attribute mit einer geöffneten Registerkarte „Values“, die ein Kreisdiagramm der Länderattributwerte wie „US“ und „PR“ zeigt.]({% image_buster /assets/img/usage_report_values.png %}){: style="max-width:80%;"}

## Angepasste Attribute setzen {#setting-custom-attributes}

Im Folgenden finden Sie Methoden für verschiedene Plattformen, die zum Setzen angepasster Attribute verwendet werden.

{% details Für plattformspezifische Dokumentation aufklappen %}

- [Android und FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=unity)
- [.NET MAUI (ehemals Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes)

{% enddetails %}

## Speicherung angepasster Attribute {#custom-attribute-storage}

Alle im **Nutzerprofil** gespeicherten Daten, einschließlich angepasster Attributdaten, werden unbegrenzt aufbewahrt, solange jedes Profil [aktiv]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival#active-users) ist.

## Datentypen für angepasste Attribute

Angepasste Attribute sind äußerst flexible Werkzeuge, die ein präzises Targeting ermöglichen.

Die folgenden Datentypen können als angepasste Attribute gespeichert werden:

- [Boolesche Werte](#booleans)
- [Zahlen](#numbers)
- [Strings](#strings)
- [Arrays](#arrays)
- [Zeit](#time)
- [Objekte]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support)
- [Arrays von Objekten]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects)

### Boolesche Werte (true/false) {#booleans}

Boolesche Attribute eignen sich zum Speichern einfacher binärer Daten über Ihre Nutzer:innen, wie z. B. Abo-Status. Sie können Nutzer:innen finden, bei denen eine Variable explizit auf true oder false gesetzt ist, sowie solche, bei denen noch kein Wert für dieses Attribut erfasst wurde.

Für **boolesche** Attribute stehen die folgenden Segmentierungsoptionen zur Verfügung.

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen, ob der boolesche Wert entweder true, false, true oder nicht gesetzt, oder false oder nicht gesetzt **ist** | **IS**  | **TRUE**, **FALSE**, **TRUE OR NOT SET** oder **FALSE OR NOT SET** | Wenn dieser Filter `coffee_drinker` angibt, stimmt ein:e Nutzer:in unter folgenden Umständen mit diesem Filter überein: <br> {::nomarkdown}<ul><li>Wenn dieser Filter <code>true</code> ist und der/die Nutzer:in den Wert <code>coffee_drinker</code> hat</li><li>Wenn dieser Filter <code>false</code> ist und der/die Nutzer:in den Wert <code>coffee_drinker</code> nicht hat</li><li>Wenn dieser Filter <code>true or not set</code> ist und der/die Nutzer:in den Wert <code>coffee_drinker</code> oder keinen Wert hat</li><li>Wenn dieser Filter <code>false or not set</code> ist und der/die Nutzer:in <code>coffee_drinker</code> oder keinen Wert hat</li></ul>{:/} |
| Prüfen, ob der boolesche Wert im Nutzerprofil **vorhanden** und nicht null ist | **IS NOT BLANK**  | **N/A** | Wenn dieser Filter `coffee_drinker` angibt und ein Nutzerprofil einen Wert für das Attribut `coffee_drinker` hat, stimmt der/die Nutzer:in mit diesem Filter überein. |
| Prüfen, ob der boolesche Wert im Nutzerprofil **nicht vorhanden** oder null ist | **IS BLANK**  | **N/A** | Wenn dieser Filter `coffee_drinker` angibt und ein Nutzerprofil entweder das Attribut `coffee_drinker` nicht hat oder der Wert für `coffee_drinker` null ist, stimmt der/die Nutzer:in mit diesem Filter überein.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Booleans (true/false) #booleans" }

{% endtab %}
{% tab Zahlen %}

{% alert tip %}
Ausgegebene Beträge sollten nicht über diese Methode erfasst werden. Verwenden Sie stattdessen [Kauf-Events]({{site.baseurl}}/user_guide/data/activation/events/purchase_events).
{% endalert %}

Für **Zahlen**-Attribute stehen die folgenden Segmentierungsoptionen zur Verfügung.

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen, ob das numerische Attribut **genau** einer **Zahl** entspricht| **EXACTLY** | **NUMBER** | Wenn dieser Filter `10` angibt und ein Nutzerprofil den Wert `10` hat, stimmt der/die Nutzer:in mit diesem Filter überein. |
| Prüfen, ob das numerische Attribut **nicht gleich** einer **Zahl** ist| **DOES NOT EQUAL** | **NUMBER** | Wenn dieser Filter `10` angibt und ein Nutzerprofil nicht den Wert `10` hat, stimmt der/die Nutzer:in mit diesem Filter überein. |
| Prüfen, ob das numerische Attribut **größer als** eine **Zahl** ist| **MORE THAN** | **NUMBER** | Wenn dieser Filter `10` angibt und ein Nutzerprofil einen Wert größer als `10` hat, stimmt der/die Nutzer:in mit diesem Filter überein. |
| Prüfen, ob das numerische Attribut **kleiner als** eine **Zahl** ist| **LESS THAN** | **NUMBER** | Wenn dieser Filter `10` angibt und ein Nutzerprofil einen Wert kleiner als `10` hat, stimmt der/die Nutzer:in mit diesem Filter überein. |
| Prüfen, ob das numerische Attribut im Nutzerprofil **vorhanden** und nicht null ist | **IS NOT BLANK** | **N/A** | Wenn ein Nutzerprofil das angegebene numerische Attribut enthält, unabhängig vom Wert, stimmt der/die Nutzer:in mit diesem Filter überein. |
| Prüfen, ob das numerische Attribut im Nutzerprofil **nicht vorhanden** oder null ist | **IS BLANK** | **N/A** | Wenn ein Nutzerprofil das angegebene numerische Attribut nicht enthält oder der Wert des Attributs null ist, stimmt der/die Nutzer:in mit diesem Filter überein.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Booleans (true/false) #booleans" }

#### Details zu Zahlenattributen {#number-attribute-details}

- Die Filter „Exactly 0“ und „Less Than“ schließen Nutzer:innen mit NULL-Feldern ein
  - Um Nutzer:innen ohne Wert für angepasste Attribute auszuschließen, müssen Sie den Filter **is not blank** einbeziehen.

{% endtab %}
{% tab Strings %}

String-Attribute können bis zu 255 Zeichen lang sein. Beachten Sie, dass Braze bei der Eingabe von Werten mit Leerzeichen zwischen, vor oder nach Wörtern auch nach denselben Leerzeichen sucht.

Für **String**-Attribute stehen die folgenden Segmentierungsoptionen zur Verfügung.

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen, ob das String-Attribut **teilweise** einem eingegebenen String **ODER** regulären Ausdruck entspricht | **MATCHES REGEX** | **STRING** **OR** **REGULAR EXPRESSION** <br>Nicht case-sensitiv; maximal 32.764 Zeichen |
| Prüfen, ob das String-Attribut **nicht teilweise** einem eingegebenen String **ODER** regulären Ausdruck entspricht | **DOES NOT MATCH REGEX** * | **STRING** **OR** **REGULAR EXPRESSION**<br>Nicht case-sensitiv; maximal 32.764 Zeichen |
| Prüfen, ob das String-Attribut im Nutzerprofil **vorhanden** und kein leerer String ist | **IS NOT BLANK** | **N/A** | Wenn dieser Filter `favorite_genre` angibt und ein Nutzerprofil das Attribut `favorite_genre` hat, stimmt der/die Nutzer:in mit diesem Filter überein, unabhängig vom Attributwert. Zum Beispiel kann der/die Nutzer:in `sci-fi`, `romance` oder einen anderen Wert haben.|
| Prüfen, ob das String-Attribut im Nutzerprofil **nicht vorhanden** ist | **BLANK** | **N/A** | Wenn dieser Filter `favorite_genre` angibt und ein Nutzerprofil das Attribut `favorite_genre` nicht hat, stimmt der/die Nutzer:in mit diesem Filter überein.|
| Prüfen, ob der String genau mit **einem** der eingegebenen Strings übereinstimmt | **IS ANY OF** | **STRING**<br>Case-sensitiv; mehrere Strings erlaubt (maximal 256) | Wenn dieser Filter `book`, `bookmark` und `reading light` angibt und ein Nutzerprofil mindestens einen dieser Strings hat, stimmt der/die Nutzer:in mit diesem Filter überein. |
| Prüfen, ob das String-Attribut **mit keinem** der eingegebenen Strings genau übereinstimmt | **IS NONE OF** |**STRING**<br>Case-sensitiv; mehrere Strings erlaubt (maximal 256) | Wenn dieser Filter `book`, `bookmark` und `reading light` angibt und ein Nutzerprofil keinen dieser Strings enthält, stimmt der/die Nutzer:in mit dem Filter überein.|
| Prüfen, ob das String-Attribut **teilweise mit einem** der eingegebenen Strings übereinstimmt | **CONTAINS ANY OF** | **STRING**<br>Case-sensitiv; mehrere Strings erlaubt (maximal 256) | Wenn dieser Filter `gold` angibt und ein Nutzerprofil `gold` in einem beliebigen String enthält, wie z. B. `gold_tier` oder `former_gold_tier`, stimmt der/die Nutzer:in mit dem Filter überein. |
| Prüfen, ob das String-Attribut **nicht teilweise mit einem** der eingegebenen Strings übereinstimmt | **DOESN'T CONTAIN ANY OF** | **STRING**<br>Case-sensitiv; mehrere Strings erlaubt (maximal 256) | Wenn dieser Filter `gold` angibt und ein Nutzerprofil `gold` in keinem String enthält, stimmt der/die Nutzer:in mit diesem Filter überein.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Number attribute details" }

{% multi_lang_include alerts/note_alerts.md alert='Custom Attributes time attribute' %}

{% alert important %}
Bei der Segmentierung mit dem Filter **DOES NOT MATCH REGEX** muss bereits ein angepasstes Attribut mit einem zugewiesenen Wert in diesem Nutzerprofil vorhanden sein. Braze empfiehlt die Verwendung von „OR“-Logik, um zu prüfen, ob ein angepasstes Attribut leer ist, damit Nutzer:innen korrekt angesprochen werden.
{% endalert %}

{% endtab %}
{% tab Arrays %}

Arrays haben eine maximale Größe von 100&nbsp;KB. Die Standardlänge für ein Attribut beträgt bis zu 500 Elemente (wenn Sie beispielsweise ein Attribut wie „Angesehene Filme“ mit 500 Einträgen senden und ein:e Nutzer:in einen 501. Film ansieht, wird der erste Film entfernt und der neueste hinzugefügt). Beachten Sie, dass Braze bei der Eingabe von Werten mit Leerzeichen zwischen, vor oder nach Wörtern auch nach denselben Leerzeichen sucht.

Angepasste Attribute vom Typ Array können nicht über [CSV-Import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) importiert werden. Um Array-Werte hochzuladen, verwenden Sie den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) oder die [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/cloud_ingestion).

{% alert note %}
Die Option zur Erhöhung der maximalen Länge ist nicht verfügbar, wenn das Attribut auf automatische Erkennung des Datentyps eingestellt ist; der Datentyp muss auf Array gesetzt sein.
{% endalert %}

Für **Array**-Attribute stehen die folgenden Segmentierungsoptionen zur Verfügung.

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen, ob das Array-Attribut **einen Wert enthält, der genau** einem eingegebenen Wert entspricht| **INCLUDES VALUE** | **STRING** | Wenn dieser Filter `sci-fi` angibt und ein Nutzerprofil den Wert `sci-fi` hat, stimmt der/die Nutzer:in mit diesem Filter überein.|
| Prüfen, ob das Array-Attribut **keinen Wert enthält, der genau** einem eingegebenen Wert entspricht| **DOESN'T INCLUDE VALUE** | **STRING** | Wenn dieser Filter `sci-fi` angibt und ein Nutzerprofil den Wert `sci-fi` nicht hat, stimmt der/die Nutzer:in mit diesem Filter überein.|
| Prüfen, ob das Array-Attribut **einen Wert enthält, der teilweise** einem eingegebenen Wert **ODER** regulären Ausdruck entspricht | **MATCHES REGEX** | **STRING** **OR** **REGULAR EXPRESSION**<br>Maximal 32.764 Zeichen | |
| Prüfen, ob das Array-Attribut **einen beliebigen Wert hat** oder nicht leer ist | **HAS A VALUE** | **N/A** | Wenn dieser Filter `favorite_genres` angibt und ein Nutzerprofil `favorite_genres` mit einem beliebigen Wert enthält, stimmt der/die Nutzer:in mit diesem Filter überein. |
| Prüfen, ob das Array-Attribut **leer ist** oder nicht existiert | **IS EMPTY** | **N/A** | Wenn dieser Filter `favorite_genres` angibt und ein Nutzerprofil `favorite_genres` nicht enthält oder `favorite_genres` enthält, aber keine Werte hat, stimmt der/die Nutzer:in mit diesem Filter überein.|
| Prüfen, ob das Array-Attribut **einen Wert enthält, der genau mit einem** der eingegebenen Werte übereinstimmt | **INCLUDES ANY OF** | **STRING**<br>Case-sensitiv; mehrere Werte erlaubt (maximal 256) | Wenn dieser Filter `sci-fi, fantasy, romance` angibt und ein Nutzerprofil eine beliebige Kombination von `sci-fi`, `fantasy` oder `romance` hat, einschließlich nur eines davon (z. B. nur `sci-fi`). Ein:e Nutzer:in kann `horror` oder einen anderen Wert in seinem/ihrem String haben, wenn er/sie auch einen der Werte `sci-fi`, `fantasy` und `romance` hat.|
| Prüfen, ob das Array-Attribut **keinen Wert enthält, der genau mit einem** der eingegebenen Werte übereinstimmt | **INCLUDES NONE OF** | **STRING**<br>Case-sensitiv; mehrere Werte erlaubt (maximal 256) | Wenn dieser Filter `sci-fi, fantasy, romance` angibt und ein Nutzerprofil keine Kombination von `sci-fi`, `fantasy` oder `romance` hat, stimmt der/die Nutzer:in mit diesem Filter überein. Der/die Nutzer:in kann `horror` oder einen anderen Wert haben, wenn er/sie keinen der Werte `sci-fi`, `fantasy` oder `romance` hat.|
| Prüfen, ob das Array-Attribut **einen Wert enthält, der teilweise mit einem** der eingegebenen Werte übereinstimmt | **VALUES CONTAIN ANY OF** | **STRING**<br>Case-sensitiv; mehrere Werte erlaubt (maximal 256) | Wenn dieser Filter `gold` angibt und ein Nutzerprofil-Array `gold` in mindestens einem String enthält, stimmt der/die Nutzer:in mit diesem Filter überein. Dies schließt String-Werte wie `gold_tier`, `former_gold_tier` und andere ein.|
| Prüfen, ob das Array-Attribut **keinen Wert enthält, der teilweise mit einem** der eingegebenen Werte übereinstimmt | **VALUES DON'T CONTAIN ANY OF** | **STRING**<br>Case-sensitiv; mehrere Werte erlaubt (maximal 256) | Wenn dieser Filter `gold` angibt und ein Nutzerprofil-Array `gold` in keinem String enthält, stimmt der/die Nutzer:in mit diesem Filter überein. Das bedeutet, dass Nutzer:innen mit String-Werten wie `gold_tier` und `former_gold_tier` nicht mit diesem Filter übereinstimmen.|
| Prüfen, ob das Array-Attribut **alle** eingegebenen Werte enthält | **IS ALL OF** | **STRING**<br>Case-sensitiv; mehrere Werte erlaubt (maximal 256) | Wenn dieser Filter `sci-fi, fantasy, romance` angibt und ein Nutzerprofil alle diese Werte hat, stimmt der/die Nutzer:in mit diesem Filter überein. Der/die Nutzer:in kann auch `horror` oder andere Werte haben und trotzdem mit diesem Filter übereinstimmen.|
| Prüfen, ob das Array-Attribut **nicht alle** eingegebenen Werte enthält | **ISN'T ALL OF** | **STRING**<br>Case-sensitiv; mehrere Werte erlaubt (maximal 256)|  Wenn dieser Filter `sci-fi, fantasy, romance` angibt und ein Nutzerprofil nicht alle diese Werte hat, stimmt der/die Nutzer:in mit diesem Filter überein.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Number attribute details" }

{% alert tip %}
Weitere Informationen zur Verwendung regulärer Ausdrücke (Regex) finden Sie in diesen Ressourcen:

- [Perl-kompatible reguläre Ausdrücke (PCRE)](https://www.regextester.com/pregsyntax.html)
- [Regex mit Braze]({{site.baseurl}}/user_guide/audience/segments/regex)
- [Regex-Debugger und -Tester](https://www.regex101.com/)
- [Regex-Tutorial](https://www.medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

{% endtab %}
{% tab Zeit %}

Zeitattribute eignen sich zum Speichern des letzten Zeitpunkts, zu dem eine bestimmte Aktion durchgeführt wurde, sodass Sie Ihren Nutzer:innen inhaltsspezifische Nachrichten zur erneuten Interaktion senden können.

Zeitfilter mit relativen Daten (z. B. mehr als 1 Tag her, weniger als 2 Tage her) messen 1 Tag als 24 Stunden. Jede Campaign, die Sie mit diesen Filtern ausführen, erfasst alle Nutzer:innen in 24-Stunden-Schritten. Zum Beispiel erfasst `last used app more than 1 day ago` alle Nutzer:innen, die die App „vor mehr als 24 Stunden“ zuletzt verwendet haben, gerechnet ab dem genauen Zeitpunkt der Campaign-Ausführung. Dasselbe gilt für Campaigns mit längeren Zeiträumen – fünf Tage ab Aktivierung bedeuten die vorherigen 120 Stunden.

Um Nutzer:innen anzusprechen, deren Zeitattribut in einen bestimmten Zeitraum fällt, verwenden Sie zwei Zielgruppenfilter: `in more than` für die untere Grenze und `in less than` für die obere Grenze. Ein einzelner Filter kann nicht beide Seiten dieses Bereichs abdecken. Um beispielsweise Nutzer:innen mit einem Zeitattribut in den nächsten 24 Stunden (zwischen jetzt und einem Tag ab jetzt) anzusprechen, wenden Sie `in more than 0 days` und `in less than 1 day` an.

{% alert warning %}
Das letzte Datum, an dem ein angepasstes Event oder Kauf-Event stattfand, wird automatisch erfasst und sollte nicht erneut über ein angepasstes Zeitattribut erfasst werden.
{% endalert %}

Für **Zeit**-Attribute stehen die folgenden Segmentierungsoptionen zur Verfügung.

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen, ob das Zeitattribut **vor** einem **ausgewählten Datum** liegt| **BEFORE** | **CALENDAR DATE SELECTOR** | Wenn dieser Filter `2024-01-31` angibt und ein Nutzerprofil ein Datum vor `2024-1-31` hat, stimmt der/die Nutzer:in mit diesem Filter überein. |
| Prüfen, ob das Zeitattribut **nach** einem **ausgewählten Datum** liegt| **AFTER** | **CALENDAR DATE SELECTOR** | Wenn dieser Filter `2024-01-31` angibt und ein Nutzerprofil ein Datum nach `2024-1-31` hat, stimmt der/die Nutzer:in mit diesem Filter überein. |
| Prüfen, ob das Zeitattribut **mehr als X Tage** her ist | **MORE THAN** | **NUMBER OF DAYS AGO** | Wenn dieser Filter `7` angibt und ein Nutzerprofil ein Datum hat, das mehr als sieben Tage zurückliegt, stimmt der/die Nutzer:in mit diesem Filter überein. |
| Prüfen, ob das Zeitattribut **weniger als X Tage** her ist| **LESS THAN** | **NUMBER OF DAYS AGO** | Wenn dieser Filter `7` angibt und ein Nutzerprofil ein Datum hat, das weniger als sieben Tage zurückliegt, stimmt der/die Nutzer:in mit diesem Filter überein.|
| Prüfen, ob das Zeitattribut **in mehr als X Tagen** in der Zukunft liegt | **IN MORE THAN** | **NUMBER OF DAYS IN FUTURE** | Wenn dieser Filter `7` angibt und ein Nutzerprofil ein Datum hat, das mehr als sieben Tage in der Zukunft liegt, stimmt der/die Nutzer:in mit diesem Filter überein.|
| Prüfen, ob das Zeitattribut **in weniger als X Tagen** in der Zukunft liegt | **IN LESS THAN** | **NUMBER OF DAYS IN FUTURE**  | Wenn dieser Filter `7` angibt und ein Nutzerprofil ein Datum hat, das weniger als sieben Tage in der Zukunft liegt, stimmt der/die Nutzer:in mit diesem Filter überein.|
| Prüfen, ob das Zeitattribut im Nutzerprofil **vorhanden** und nicht null ist | **IS NOT BLANK** | **N/A** | Wenn dieser Filter ein Zeitattribut angibt, das in einem Nutzerprofil vorhanden ist, stimmt der/die Nutzer:in mit diesem Filter überein.|
| Prüfen, ob das Zeitattribut im Nutzerprofil **nicht vorhanden** oder null ist | **IS BLANK** | **N/A** | Wenn dieser Filter ein Zeitattribut angibt, das nicht in einem Nutzerprofil vorhanden ist, stimmt der/die Nutzer:in mit diesem Filter überein. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Number attribute details" }

#### Details zu Zeitattributen {#time-attribute-details}

- Tag eines wiederkehrenden Events
  - Wenn Sie den Filter „Tag eines wiederkehrenden Events“ verwenden und dann aufgefordert werden, den „Kalendertag des wiederkehrenden Events“ auszuwählen, wird bei Auswahl von `IS LESS THAN` oder `IS MORE THAN` das aktuelle Datum für diesen Segmentierungsfilter mitgezählt.
  - Wenn Sie beispielsweise am 10. März 2020 das Datum des Attributs auf `LESS THAN ... March 10, 2020` setzen, werden Attribute für die Tage bis einschließlich 10. März 2020 berücksichtigt.
- Weniger als X Tage her: Der Filter „Weniger als X Tage her“ umfasst Daten zwischen X Tagen in der Vergangenheit und dem aktuellen Datum/der aktuellen Uhrzeit.
- Weniger als X Tage in der Zukunft: Umfasst Daten zwischen dem aktuellen Datum/der aktuellen Uhrzeit und X Tagen in der Zukunft.

{% endtab %}
{% tab Objekte %}

Sie können verschachtelte angepasste Attribute verwenden, um Objekte als Datentyp für angepasste Attribute zu senden. Weitere Informationen finden Sie unter [Verschachtelte angepasste Attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support).

{% endtab %}
{% tab Arrays von Objekten %}

Verwenden Sie ein Array von Objekten, um zusammengehörige Attribute zu gruppieren. Weitere Details finden Sie unter [Array von Objekten]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects).

{% endtab %}
{% endtabs %}

Sie können den Datentyp Ihres angepassten Attributs ändern, sollten sich aber der Auswirkungen bewusst sein. Weitere Informationen finden Sie unter [Datentyp eines angepassten Attributs oder Events ändern](#changing-custom-attribute-or-event-data-type).

### Konsolidierte Operatoren {#consolidated-operators}

Wir haben die Liste der verfügbaren Operatoren für Attributfilter, Filter für angepasste Attribute und Filter für verschachtelte angepasste Attribute konsolidiert. Wenn Sie bestehende Filter mit diesen Operatoren haben, werden diese automatisch auf die neuen Operatoren aktualisiert.

| Datentyp | Alter Operator | Neuer Operator | Wert |
| --- | --- | --- | --- |
| String | equals | is any of | Mindestens 1 Wert |
| String | does not equal | is none of | Mindestens 1 Wert |
| Array | includes value | includes any of | Mindestens 1 Wert |
| Array | doesn't include value | includes none of | Mindestens 1 Wert |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Consolidated operators #consolidated-operators" }

## Datentypen für Event-Eigenschaften {#event-property-data-types}

Wenn Sie ein Event protokollieren, können Sie zusätzliche Informationen (z. B. Produktname oder Preis) als Event-Eigenschaften anhängen. Jede Eigenschaft hat einen Namen und einen Wert. Event-Eigenschaftswerte unterstützen die Datentypen in der Tabelle [Definitionen](#definitions) (Zeit wird in Event-Eigenschaften als „Datetime“ bezeichnet).

### Erwartetes Format {#expected-format}

Eigenschaftswerte werden als Objekt gesendet: Schlüssel sind die Eigenschaftsnamen und Werte sind die Eigenschaftswerte. Eigenschaftsnamen müssen nicht-leere Strings mit 255 Zeichen oder weniger sein, ohne führende Dollarzeichen (`$`).

Spezifische Regeln für Event-Eigenschaften:

- **Zeit (Datetime):** Verwenden Sie das Format [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) oder `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Wird innerhalb von Arrays nicht unterstützt.
- **Array:** Datetimes werden innerhalb von Arrays nicht unterstützt.
- **Verschachteltes Objekt:** Siehe [Verschachtelte Objekte]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects).
- **Payload:** Event-Eigenschaftsobjekte, die Array- oder Objektwerte enthalten, können bis zu 102.400 Bytes (100&nbsp;KiB) groß sein.

Sie können den Datentyp Ihrer angepassten Event-Eigenschaft ändern, sollten sich aber der Auswirkungen einer [Änderung des Datentyps](#changing-custom-attribute-or-event-data-type) bewusst sein, nachdem Daten erfasst wurden.

Für das vollständige Verhalten von Event-Eigenschaften, reservierte Schlüssel und die Verwendung in Triggern und Personalisierung siehe [Angepasste Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties).

## Kauf-Events und Umsatz {#purchase-events-and-revenue}

Kauf- und Umsatzdaten werden über [Kauf-Events]({{site.baseurl}}/user_guide/data/activation/events/purchase_events) oder empfohlene E-Commerce-Events erfasst.

{% alert note %}
Empfohlene Events haben vordefinierte Schemas mit festgelegten Datentypen. Weitere Details finden Sie unter [Empfohlene E-Commerce-Events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events).
{% endalert %}

Das Protokollieren von Kauf-Events legt den Lifetime-Value (LTV) für jedes Nutzerprofil fest, und diese Daten sind auf der Umsatzseite als Zeitreihe einsehbar. Sie können nach ausgegebenem Betrag, letztem Kaufdatum, Anzahl der Käufe in einem Zeitfenster und mehr segmentieren.

### Datentypen für Kauf-Event-Eigenschaften {#purchase-event-property-data-types}

Kauf-Event-Eigenschaftswerte (das `properties`-Objekt bei einem Kauf) unterstützen die Datentypen in der Tabelle [Definitionen](#definitions) mit derselben Struktur und denselben Benennungsregeln wie [Event-Eigenschaften](#expected-format).

{% include data_activation/purchase_event_property_data_types.md %}

Für das vollständige Schema des Kauf-Objekts und Beispiele siehe [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object). Für das Protokollieren von Kauf-Events, Segmentierungsfilter und vollständige Details siehe [Kauf-Events]({{site.baseurl}}/user_guide/data/activation/events/purchase_events).

## Datentyp eines angepassten Attributs oder Events ändern {#changing-custom-attribute-or-event-data-type}

So ändern Sie den Datentyp eines angepassten Attributs oder Events:

1. Gehen Sie zu **Data Settings** und wählen Sie entweder **Custom Attributes** oder **Custom Events**.
2. Suchen Sie Ihr Attribut oder Event in der Liste und wählen Sie <i class="fa fa-ellipsis-v" aria-label="Weitere Aktionen"></i> **More actions**.
3. Wählen Sie einen neuen **Data type** aus dem Dropdown.
4. Wählen Sie **Save**.

Wenn Sie den Datentyp eines angepassten Attributs oder Events ändern (z. B. von `time` zu `string`), beachten Sie Folgendes:

- **Filter werden nicht automatisch aktualisiert.** Segmente, Campaigns, Canvases oder andere Stellen, die das geänderte Attribut oder Event verwenden, werden nicht aktualisiert. Bevor Sie den Datentyp ändern, stoppen Sie alle Campaigns oder Canvases, die das Attribut in Segmenten oder Filtern verwenden, und entfernen Sie das Attribut aus Filtern, die darauf verweisen.
- **Bestehende Nutzerdaten werden nicht rückwirkend aktualisiert.** Wenn das geänderte Attribut vor der Änderung in einem Nutzerprofil vorhanden war, behält dieser Wert den alten Datentyp. Nutzer:innen können aus Segmenten herausfallen, die das geänderte Attribut enthalten, da der Filter nach dem neuen Datentyp sucht. Aktualisieren Sie diese Nutzerprofile (z. B. mit dem [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track)), damit sie dem neuen Typ entsprechen und bei Bedarf wieder in das Segment aufgenommen werden.
- **Neue Daten müssen dem neuen Typ entsprechen.** API-Aufrufe, die den vorherigen Datentyp für das geänderte Attribut senden, werden nicht akzeptiert. Senden Sie den neuen Datentyp.

{% alert important %}
Die Möglichkeit, die automatische Erkennung daran zu hindern, den Datentyp des angepassten Attributs zu aktualisieren, befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Customer-Success-Manager, wenn Sie daran teilnehmen möchten.
{% endalert %}

## Katalog-Datentypen {#catalog-data-types}

Kataloge unterstützen die in der Tabelle [Definitionen](#definitions) aufgeführten Typen. Die folgende Tabelle listet jeden Typ auf, wie er erstellt oder aktualisiert werden kann, sowie Format und Beispiele.

| Datentyp | Beschreibung | Verfügbar per CSV-Upload | Verfügbar per API und CDI |
| --- | --- | --- | --- |
| String | Eine Zeichenfolge (z. B. Namen, Beschreibungen, IDs). | ✅ Ja | ✅ Ja |
| Zahl | Ein numerischer Wert, entweder Ganzzahl oder Gleitkommazahl (z. B. Preise, Mengen, Bewertungen). | ✅ Ja | ✅ Ja |
| Boolescher Wert | Ein `true`- oder `false`-Wert. | ✅ Ja | ✅ Ja |
| Zeit | Datum und Uhrzeit im [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)-Format oder als Unix-Zeitstempel in Sekunden. | ✅ Ja | ✅ Ja |
| JSON-Objekt (Objekt) | Verschachteltes Objekt mit Schlüssel-Wert-Paaren. Wird in der Plattform angezeigt, kann aber nur über die API oder CDI erstellt oder aktualisiert werden. | ❌ Nein | ✅ Ja |
| String-Array (Array) | Eine Liste von Strings. Wird in der Plattform angezeigt, kann aber nur über die API oder CDI erstellt oder aktualisiert werden. Maximal 100 Elemente. | ❌ Nein | ✅ Ja |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Katalog-Datentypen" }

### Format und Beispiele {#format-and-examples}

| Datentyp | Format | Beispiel |
| --- | --- | --- |
| String | Text | <code>"Hello World"</code> |
| Zeit | ISO 8601 oder Unix-Zeitstempel (Sekunden) | <code>"2024-03-15T14:30:00Z"</code> |
| Boolescher Wert | <code>true</code> oder <code>false</code> | <code>true</code> |
| Zahl | Ganzzahl oder Dezimalzahl | <code>42</code> oder <code>19.99</code> |
| Objekt | JSON-Objekt | <code>{"key": "value", "price": 10}</code> |
| Array | String-Array | <code>["red", "blue", "green"]</code> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Format und Beispiele" }

Informationen zum Erstellen und Aktualisieren von Katalogen finden Sie unter [Katalog erstellen]({{site.baseurl}}/user_guide/data/activation/catalogs/create).