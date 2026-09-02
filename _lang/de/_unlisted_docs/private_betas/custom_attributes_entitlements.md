---
article_title: Angepasste Attribute
permalink: "/custom_attributes_entitlements/"
hidden: true
---

# [![Braze-Lernkurs]({% image_buster /assets/unlisted_docs/img/logos/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Angepasste Attribute {#braze-learning-course-image_buster-assetsunlisted_docsimglogosbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-attributes}

> Diese Seite behandelt angepasste Attribute, die eine Sammlung der einzigartigen Merkmale Ihrer Nutzer:innen darstellen. Angepasste Attribute eignen sich am besten zum Speichern von Attributen über Ihre Nutzer:innen oder von Informationen über Aktionen mit geringem Wert innerhalb Ihrer Anwendung.

Wenn sie in Braze gespeichert werden, können angepasste Attribute verwendet werden, um Zielgruppen-Segmente aufzubauen und Nachrichten mithilfe von Liquid zu personalisieren. Beachten Sie, dass wir keine Zeitreihendaten für angepasste Attribute speichern, sodass Sie keine Diagramme auf deren Basis erstellen können, wie es bei angepassten Events möglich ist.

## Berechtigungen {#entitlements}

Berechtigungen bestimmen Ihre Kapazität für angepasste Attribute, die die Anzahl der verschiedenen Attributnamen nachverfolgt, die Sie definieren. Sie können bis zu 1.000 angepasste Attribute pro Workspace haben. Wenn Sie Ihre Kapazität erhöhen müssen, wenden Sie sich an Ihren Braze-Account Manager:in für weitere Informationen.

Wenn sich Ihr Workspace der maximalen Anzahl angepasster Attribute nähert, erhalten Sie Benachrichtigungen im Dashboard und per E-Mail, damit Sie den Überblick behalten.

Auch nach Erreichen der Kapazitätsgrenze können bestehende angepasste Attribute weiterhin empfangen werden. Sie können jedoch keine neuen angepassten Attribute erstellen. Alle Daten, die für angepasste Attribute empfangen werden, die noch nicht existieren, werden nicht verarbeitet.

## Verwalten angepasster Attribute {#managing-custom-attributes}

Um angepasste Attribute im Dashboard zu erstellen und zu verwalten, gehen Sie zu **Dateneinstellungen** > **Angepasste Attribute**.

![Vier angepasste Attribute, die boolesche Werte sind.]({% image_buster /assets/unlisted_docs/img/custom_attributes_entitlements/export_custom_attributes.png %})

Die Spalte **Zuletzt aktualisiert** zeigt an, wann das angepasste Attribut zuletzt bearbeitet wurde, z. B. wann es zuletzt auf die Sperrliste gesetzt oder aktiviert wurde.

{% alert important %}
Um ein korrektes Nachrichten-Targeting zu gewährleisten, stellen Sie sicher, dass der Datentyp Ihres angepassten Attributs mit dem tatsächlichen angepassten Attribut übereinstimmt.
{% endalert %}

Auf dieser Seite können Sie vorhandene angepasste Attribute anzeigen, verwalten, erstellen oder auf die Sperrliste setzen. Wählen Sie das Menü neben einem angepassten Attribut für die folgenden Aktionen aus:

### Sperrliste {#blocklisting}

Angepasste Attribute können einzeln über das Aktionsmenü auf die Sperrliste gesetzt werden, oder es können bis zu 100 Attribute ausgewählt und in einem Schritt gesperrt werden. Wenn Sie ein angepasstes Attribut sperren, werden keine Daten mehr zu diesem Attribut erfasst, vorhandene Daten sind nicht verfügbar, sofern sie nicht reaktiviert werden, und gesperrte Attribute werden nicht in Filtern oder Diagrammen angezeigt. Wenn das Attribut derzeit von Filtern oder Triggern in anderen Bereichen des Braze-Dashboards referenziert wird, erscheint außerdem ein Warn-Modal, das erklärt, dass alle Instanzen der Filter oder Trigger, die darauf verweisen, entfernt und archiviert werden.

### Als personenbezogene Informationen (PII) kennzeichnen {#marking-as-personally-identifiable-information-pii}

Administrator:innen können auf dieser Seite auch angepasste Attribute erstellen und als PII kennzeichnen. Diese Attribute sind nur für Administrator:innen und Dashboard-Nutzer:innen mit der Berechtigung „Angepasste Attribute anzeigen, die als PII gekennzeichnet sind“ sichtbar.

### Beschreibungen hinzufügen {#adding-descriptions}

Sie können einem angepassten Attribut nach der Erstellung eine Beschreibung hinzufügen, wenn Sie über die [Nutzerberechtigung]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) `Manage Events, Attributes, Purchases` verfügen. Bearbeiten Sie das angepasste Attribut und geben Sie einen beliebigen Text ein, beispielsweise eine Notiz für Ihr Team.

### Tags hinzufügen {#adding-tags}

Sie können einem angepassten Attribut nach der Erstellung Tags hinzufügen, wenn Sie über die [Nutzerberechtigung]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) „Manage Events, Attributes, Purchases“ verfügen. Die Tags können dann verwendet werden, um die Liste der Attribute zu filtern.

### Angepasste Attribute entfernen {#removing-custom-attributes}

Es gibt zwei Möglichkeiten, angepasste Attribute aus Nutzerprofilen zu entfernen:

* Wählen Sie den Namen des zu entfernenden angepassten Attributs in einem [Nutzeraktualisierung-Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update#removing-custom-attributes) aus.
* Setzen Sie den Wert `null` in Ihrer API-Anfrage an den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

### Nutzungsberichte anzeigen {#viewing-usage-reports}

Der Nutzungsbericht listet alle Canvases, Campaigns und Segments auf, die ein bestimmtes angepasstes Attribut verwenden. Diese Liste enthält keine Liquid-Verwendungen.

Sie können bis zu 100 Nutzungsberichte gleichzeitig anzeigen, indem Sie die Kontrollkästchen neben den entsprechenden angepassten Attributen aktivieren und dann **Nutzungsbericht anzeigen** auswählen.

### Daten exportieren {#exporting-data}

Um die Liste der angepassten Attribute als CSV-Datei zu exportieren, wählen Sie oben auf der Seite **Alle exportieren** aus. Die CSV-Datei wird erstellt, und ein Download-Link wird Ihnen per E-Mail zugesandt.

## Angepasste Attribute festlegen {#setting-custom-attributes}

Die folgenden Listen enthalten Methoden für verschiedene Plattformen, die zum Festlegen angepasster Attribute verwendet werden.

{% details Für Dokumentation nach Plattform aufklappen %}

- [Android und FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift)
- [Internet]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=unity)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes)

{% enddetails %}

## Speicherung angepasster Attribute {#custom-attribute-storage}

Alle auf dem **Kundenprofil** gespeicherten Daten, einschließlich Daten angepasster Attribute, werden unbegrenzt aufbewahrt, solange jedes Profil [aktiv]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival#active-users) ist.

## Datentypen angepasster Attribute {#custom-attribute-data-types}

Angepasste Attribute sind außerordentlich flexible Werkzeuge, die ein sehr gezieltes Targeting ermöglichen.

Die folgenden Datentypen können als angepasste Attribute gespeichert werden:

- [Boolesche Werte](#booleans)
- [Zahlen](#numbers)
- [Strings](#strings)
- [Arrays](#arrays)
- [Zeit](#time)
- [Objekte]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support)
- [Arrays von Objekten]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects)

### Boolesche Werte (true/false) {#booleans}

Boolesche Attribute eignen sich zum Speichern einfacher binärer Daten über Ihre Nutzer:innen, z. B. Abo-Status. Sie können Nutzer:innen finden, bei denen eine Variable explizit auf true oder false gesetzt ist, sowie solche, für die noch kein Eintrag dieses Attributs vorliegt.

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen, ob der boolesche Wert entweder true, false, true oder nicht gesetzt, oder false oder nicht gesetzt **ist** | **IS**  | **TRUE**, **FALSE**, **TRUE OR NOT SET** oder **FALSE OR NOT SET** | Wenn dieser Filter `coffee_drinker` angibt, stimmt ein:e Nutzer:in in folgenden Fällen überein: <br> {::nomarkdown}<ul><li>Wenn dieser Filter <code>true</code> ist und die/der Nutzer:in den Wert <code>coffee_drinker</code> hat</li><li>Wenn dieser Filter <code>false</code> ist und die/der Nutzer:in den Wert <code>coffee_drinker</code> nicht hat</li><li>Wenn dieser Filter <code>true or not set</code> ist und die/der Nutzer:in den Wert <code>coffee_drinker</code> oder keinen Wert hat</li><li>Wenn dieser Filter <code>false or not set</code> ist und die/der Nutzer:in weder <code>coffee_drinker</code> noch einen anderen Wert hat</li></ul>{:/} |
| Prüfen, ob der boolesche Wert im Profil einer/eines Nutzer:in **existiert** und nicht null ist | **IS NOT BLANK**  | **N/A** | Wenn dieser Filter `coffee_drinker` angibt und ein Kundenprofil einen Wert für das Attribut `coffee_drinker` hat, stimmt die/der Nutzer:in mit diesem Filter überein. |
| Prüfen, ob der boolesche Wert im Profil einer/eines Nutzer:in **nicht existiert** oder null ist | **IS BLANK**  | **N/A** | Wenn dieser Filter `coffee_drinker` angibt und ein Kundenprofil das Attribut `coffee_drinker` nicht hat oder der Wert für `coffee_drinker` null ist, stimmt die/der Nutzer:in mit diesem Filter überein.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Zahlen {#numbers}

Numerische Attribute umfassen [Ganzzahlen](https://en.wikipedia.org/wiki/Integer) und [Gleitkommazahlen](https://en.wikipedia.org/wiki/Floating-point_arithmetic) und bieten vielfältige Einsatzmöglichkeiten. Inkrementierende numerische angepasste Attribute eignen sich zum Speichern der Häufigkeit, mit der eine bestimmte Aktion oder ein bestimmtes Ereignis aufgetreten ist, ohne Ihr Datenlimit zu belasten. Standardzahlen haben vielfältige Verwendungsmöglichkeiten, z. B. zur Erfassung von:

- Schuhgröße
- Taillenumfang
- Anzahl der Male, die ein:e Nutzer:in ein bestimmtes Produkt-Feature oder eine Kategorie angesehen hat

{% alert tip %}
Ausgegebene Beträge sollten nicht mit dieser Methode erfasst werden. Verwenden Sie stattdessen unsere [Kauf-Methoden](#purchase-revenue-tracking).
{% endalert %}

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen, ob das numerische Attribut **genau** einer **Zahl** entspricht | **EXACTLY** | **NUMBER** | Wenn dieser Filter `10` angibt und ein Kundenprofil den Wert `10` hat, stimmt die/der Nutzer:in mit diesem Filter überein. |
| Prüfen, ob das numerische Attribut **nicht gleich** einer **Zahl** ist | **DOES NOT EQUAL** | **NUMBER** | Wenn dieser Filter `10` angibt und ein Kundenprofil nicht den Wert `10` hat, stimmt die/der Nutzer:in mit diesem Filter überein. |
| Prüfen, ob das numerische Attribut **größer als** eine **Zahl** ist | **MORE THAN** | **NUMBER** | Wenn dieser Filter `10` angibt und ein Kundenprofil einen Wert größer als `10` hat, stimmt die/der Nutzer:in mit diesem Filter überein. |
| Prüfen, ob das numerische Attribut **kleiner als** eine **Zahl** ist | **LESS THAN** | **NUMBER** | Wenn dieser Filter `10` angibt und ein Kundenprofil einen Wert kleiner als `10` hat, stimmt die/der Nutzer:in mit diesem Filter überein. |
| Prüfen, ob das numerische Attribut im Profil einer/eines Nutzer:in **existiert** und nicht null ist | **IS NOT BLANK** | **N/A** | Wenn ein Kundenprofil das angegebene numerische Attribut enthält, unabhängig vom Wert, stimmt die/der Nutzer:in mit diesem Filter überein. |
| Prüfen, ob das numerische Attribut im Profil einer/eines Nutzer:in **nicht existiert** oder null ist | **IS BLANK** | **N/A** | Wenn ein Kundenprofil das angegebene numerische Attribut nicht enthält oder der Wert des Attributs null ist, stimmt die/der Nutzer:in mit diesem Filter überein.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Details zu Zahlenattributen {#number-attribute-details}

- Die Filter „Exactly 0“ und „Less Than“ schließen Nutzer:innen mit NULL-Feldern ein
  - Um Nutzer:innen ohne Wert für angepasste Attribute auszuschließen, müssen Sie den Filter **is not blank** hinzufügen.

### Strings (alphanumerische Zeichen) {#strings}

String-Attribute eignen sich zum Speichern von Nutzereingaben, wie z. B. einer Lieblingsmarke, einer Telefonnummer oder des letzten Suchbegriffs in Ihrer Anwendung. String-Attribute können bis zu 255 Zeichen lang sein.

Beachten Sie, dass Braze bei der Eingabe von Werten mit Leerzeichen zwischen, vor oder nach Wörtern auch nach denselben Leerzeichen sucht.

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen, ob das String-Attribut **genau** einem eingegebenen String **entspricht** | **EQUALS** | **STRING**<br>Groß-/Kleinschreibung beachten | Wenn dieser Filter `book` angibt und ein Kundenprofil ein String-Attribut für `last_item_purchased` hat, das `book` enthält, stimmt die/der Nutzer:in mit diesem Filter überein. |
| Prüfen, ob das String-Attribut einem eingegebenen String **ODER** regulären Ausdruck **teilweise entspricht** | **MATCHES REGEX** | **STRING** **ODER** **REGULÄRER AUSDRUCK** <br>Groß-/Kleinschreibung wird nicht beachtet; maximal 32.764 Zeichen |
| Prüfen, ob das String-Attribut einem eingegebenen String **ODER** regulären Ausdruck **nicht teilweise entspricht** | **DOES NOT MATCH REGEX** * | **STRING** **ODER** **REGULÄRER AUSDRUCK**<br>Groß-/Kleinschreibung wird nicht beachtet; maximal 32.764 Zeichen |
| Prüfen, ob das String-Attribut einem eingegebenen String **nicht entspricht** | **DOES NOT EQUAL** | **STRING**<br>Groß-/Kleinschreibung wird nicht beachtet  | Wenn dieser Filter `book` angibt und ein Kundenprofil ein String-Attribut für `last_item_purchased` hat, das `book` nicht enthält, stimmt die/der Nutzer:in mit diesem Filter überein.|
| Prüfen, ob das String-Attribut im Profil einer/eines Nutzer:in **existiert** und kein leerer String ist | **IS NOT BLANK** | **N/A** | Wenn dieser Filter `favorite_genre` angibt und ein Kundenprofil das Attribut `favorite_genre` hat, stimmt die/der Nutzer:in mit diesem Filter überein, unabhängig vom Attributwert. Zum Beispiel kann die/der Nutzer:in `sci-fi`, `romance` oder einen anderen Wert haben.|
| Prüfen, ob das String-Attribut im Profil einer/eines Nutzer:in **nicht existiert** | **BLANK** | **N/A** | Wenn dieser Filter `favorite_genre` angibt und ein Kundenprofil das Attribut `favorite_genre` nicht hat, stimmt die/der Nutzer:in mit diesem Filter überein.|
| Prüfen, ob der String **irgendeinem** der eingegebenen Strings **genau entspricht** | **IS ANY OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Strings erlaubt (maximal 256) | Wenn dieser Filter `book`, `bookmark` und `reading light` angibt und ein Kundenprofil mindestens einen dieser Strings enthält, stimmt die/der Nutzer:in mit diesem Filter überein. |
| Prüfen, ob das String-Attribut **keinem** der eingegebenen Strings **genau entspricht** | **IS NONE OF** |**STRING**<br>Groß-/Kleinschreibung beachten; mehrere Strings erlaubt (maximal 256) | Wenn dieser Filter `book`, `bookmark` und `reading light` angibt und ein Kundenprofil keinen dieser Strings enthält, stimmt die/der Nutzer:in mit diesem Filter überein.|
| Prüfen, ob das String-Attribut **irgendeinem** der eingegebenen Strings **teilweise entspricht** | **CONTAINS ANY OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Strings erlaubt (maximal 256) | Wenn dieser Filter `gold` angibt und ein Kundenprofil `gold` in irgendeinem String enthält, z. B. `gold_tier` oder `former_gold_tier`, stimmt die/der Nutzer:in mit diesem Filter überein. |
| Prüfen, ob das String-Attribut **keinem** der eingegebenen Strings **teilweise entspricht** | **DOESN'T CONTAIN ANY OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Strings erlaubt (maximal 256) | Wenn dieser Filter `gold` angibt und ein Kundenprofil `gold` in keinem String enthält, stimmt die/der Nutzer:in mit diesem Filter überein.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
Ein Datums-String wie „12-1-2021“ oder „12/1/2021“ wird in ein Datetime-Objekt konvertiert und als [Zeitattribut]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#time) behandelt.
{% endalert %}

{% alert important %}
Wenn Sie mit dem Filter **DOES NOT MATCH REGEX** segmentieren, muss im Kundenprofil bereits ein angepasstes Attribut mit einem zugewiesenen Wert vorhanden sein. Braze empfiehlt die Verwendung von „ODER“-Logik, um zu prüfen, ob ein angepasstes Attribut leer ist, damit Nutzer:innen korrekt angesprochen werden.
{% endalert %}

### Arrays {#arrays}

Array-Attribute eignen sich hervorragend zum Speichern verwandter Informationslisten über Ihre Nutzer:innen. Wenn Sie beispielsweise die letzten 100 angesehenen Inhalte einer/eines Nutzer:in in einem Array speichern, ermöglicht dies eine gezielte interessenbasierte Segmentierung.

Standardmäßig ist die maximale Länge eines Arrays für ein Attribut auf 25 festgelegt und kann für ein einzelnes Array auf 100 erhöht werden. Wenn Sie beispielsweise ein Attribut wie „Angesehene Filme“ senden und es auf 100 eingestellt ist, wird beim Ansehen des 101. Films der erste Film aus dem Array entfernt und der neueste Film hinzugefügt.

Wenn Sie dieses Maximum erhöhen möchten, wenden Sie sich an Ihren CSM. Ihre Dashboard-Administrator:innen können dann die maximale Länge für einzelne Arrays auf über 100 auf dem Tab **Angepasste Attribute** der Seite **Einstellungen verwalten** erhöhen.

Beachten Sie, dass Braze bei der Eingabe von Werten mit Leerzeichen zwischen, vor oder nach Wörtern auch nach denselben Leerzeichen sucht.

{% alert note %}
Die Option zur Erhöhung der maximalen Länge ist nicht verfügbar, wenn das Attribut auf automatische Datentyperkennung eingestellt ist; der Datentyp muss auf Array gesetzt sein.
{% endalert %}

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen, ob das Array-Attribut **einen Wert enthält, der genau** einem eingegebenen Wert **entspricht** | **INCLUDES VALUE** | **STRING** | Wenn dieser Filter `sci-fi` angibt und ein Kundenprofil den Wert `sci-fi` hat, stimmt die/der Nutzer:in mit diesem Filter überein.|
| Prüfen, ob das Array-Attribut **keinen Wert enthält, der genau** einem eingegebenen Wert **entspricht** | **DOESN'T INCLUDE VALUE** | **STRING** | Wenn dieser Filter `sci-fi` angibt und ein Kundenprofil den Wert `sci-fi` nicht hat, stimmt die/der Nutzer:in mit diesem Filter überein.|
| Prüfen, ob das Array-Attribut **einen Wert enthält, der teilweise** einem eingegebenen Wert **ODER** regulären Ausdruck **entspricht** | **MATCHES REGEX** | **STRING** **ODER** **REGULÄRER AUSDRUCK**<br>Maximal 32.764 Zeichen | |
| Prüfen, ob das Array-Attribut **irgendeinen Wert hat** oder nicht leer ist | **HAS A VALUE** | **N/A** | Wenn dieser Filter `favorite_genres` angibt und ein Kundenprofil `favorite_genres` mit irgendeinem Wert enthält, stimmt die/der Nutzer:in mit diesem Filter überein. |
| Prüfen, ob das Array-Attribut **leer ist** oder nicht existiert | **IS EMPTY** | **N/A** | Wenn dieser Filter `favorite_genres` angibt und ein Kundenprofil `favorite_genres` nicht enthält oder `favorite_genres` enthält, aber keine Werte hat, stimmt die/der Nutzer:in mit diesem Filter überein.|
| Prüfen, ob das Array-Attribut **einen Wert enthält, der irgendeinem** der eingegebenen Werte **genau entspricht** | **INCLUDES ANY OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Werte erlaubt (maximal 256) | Wenn dieser Filter `sci-fi, fantasy, romance` angibt und ein Kundenprofil eine beliebige Kombination aus `sci-fi`, `fantasy` oder `romance` hat, einschließlich nur eines davon (z. B. nur `sci-fi`). Ein:e Nutzer:in kann `horror` oder einen anderen Wert in seinem/ihrem String haben, wenn er/sie auch einen der Werte `sci-fi`, `fantasy` und `romance` hat.|
| Prüfen, ob das Array-Attribut **keinen Wert enthält, der irgendeinem** der eingegebenen Werte **genau entspricht** | **INCLUDES NONE OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Werte erlaubt (maximal 256) | Wenn dieser Filter `sci-fi, fantasy, romance` angibt und ein Kundenprofil keine Kombination aus `sci-fi`, `fantasy` oder `romance` hat, stimmt die/der Nutzer:in mit diesem Filter überein. Die/der Nutzer:in kann `horror` oder einen anderen Wert haben, wenn er/sie keinen der Werte `sci-fi`, `fantasy` oder `romance` hat.|
| Prüfen, ob das Array-Attribut **einen Wert enthält, der irgendeinem** der eingegebenen Werte **teilweise entspricht** | **VALUES CONTAIN ANY OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Werte erlaubt (maximal 256) | Wenn dieser Filter `gold` angibt und ein Kundenprofil-Array `gold` in mindestens einem String enthält, stimmt die/der Nutzer:in mit diesem Filter überein. Dies schließt String-Werte wie `gold_tier`, `former_gold_tier` und andere ein.|
| Prüfen, ob das Array-Attribut **keinen Wert enthält, der irgendeinem** der eingegebenen Werte **teilweise entspricht** | **VALUES DON'T CONTAIN ANY OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Werte erlaubt (maximal 256) | Wenn dieser Filter `gold` angibt und ein Kundenprofil-Array `gold` in keinem String enthält, stimmt die/der Nutzer:in mit diesem Filter überein. Das bedeutet, dass Nutzer:innen mit String-Werten wie `gold_tier` und `former_gold_tier` nicht mit diesem Filter übereinstimmen.|
| Prüfen, ob das Array-Attribut **alle** eingegebenen Werte **enthält** | **IS ALL OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Werte erlaubt (maximal 256) | Wenn dieser Filter `sci-fi, fantasy, romance` angibt und ein Kundenprofil alle diese Werte hat, stimmt die/der Nutzer:in mit diesem Filter überein. Die/der Nutzer:in kann auch `horror` oder andere Werte haben und trotzdem mit diesem Filter übereinstimmen.|
| Prüfen, ob das Array-Attribut **nicht alle** eingegebenen Werte **enthält** | **ISN'T ALL OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Werte erlaubt (maximal 256) | Wenn dieser Filter `sci-fi, fantasy, romance` angibt und ein Kundenprofil nicht alle diese Werte hat, stimmt die/der Nutzer:in mit diesem Filter überein.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
Weitere Informationen zur Verwendung regulärer Ausdrücke (Regex) finden Sie in diesen Ressourcen:
- [Perl-kompatible reguläre Ausdrücke (PCRE)](https://www.regextester.com/pregsyntax.html)
- [Regex mit Braze]({{site.baseurl}}/user_guide/audience/segments/regex)
- [Regex-Debugger und -Tester](https://www.regex101.com/)
- [Regex-Tutorial](https://www.medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

### Zeit {#time}

Zeitattribute eignen sich zum Speichern des Zeitpunkts, zu dem eine bestimmte Aktion zuletzt ausgeführt wurde, sodass Sie Ihren Nutzer:innen inhaltsspezifische Nachrichten zur erneuten Interaktion senden können.

Zeitfilter mit relativen Daten (z. B. mehr als 1 Tag her, weniger als 2 Tage her) messen 1 Tag als 24 Stunden. Jede Campaign, die Sie mit diesen Filtern ausführen, erfasst alle Nutzer:innen in 24-Stunden-Schritten. Zum Beispiel erfasst `last used app more than 1 day ago` alle Nutzer:innen, die „die App zuletzt vor mehr als 24 Stunden“ ab dem genauen Zeitpunkt der Campaign-Ausführung verwendet haben. Dasselbe gilt für Campaigns mit längeren Datumsbereichen — fünf Tage ab Aktivierung bedeuten also die vorherigen 120 Stunden.

Um beispielsweise ein Segment zu erstellen, das Nutzer:innen mit einem Zeitattribut zwischen 24 und 48 Stunden in der Zukunft anspricht, wenden Sie die Filter `in more than 1 day in the future` und `in less than 2 days in the future` an.

{% alert warning %}
Das letzte Datum, an dem ein angepasstes Event oder ein Kauf-Event aufgetreten ist, wird automatisch erfasst und sollte nicht erneut über ein angepasstes Zeitattribut aufgezeichnet werden.
{% endalert %}

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen, ob das Zeitattribut **vor** einem **ausgewählten Datum** liegt | **BEFORE** | **KALENDERDATUMSAUSWAHL** | Wenn dieser Filter `2024-01-31` angibt und ein Kundenprofil ein Datum vor `2024-1-31` hat, stimmt die/der Nutzer:in mit diesem Filter überein. |
| Prüfen, ob das Zeitattribut **nach** einem **ausgewählten Datum** liegt | **AFTER** | **KALENDERDATUMSAUSWAHL** | Wenn dieser Filter `2024-01-31` angibt und ein Kundenprofil ein Datum nach `2024-1-31` hat, stimmt die/der Nutzer:in mit diesem Filter überein. |
| Prüfen, ob das Zeitattribut **mehr als X Tage** **zurückliegt** | **MORE THAN** | **ANZAHL DER TAGE ZURÜCK** | Wenn dieser Filter `7` angibt und ein Kundenprofil ein Datum hat, das mehr als sieben Tage zurückliegt, stimmt die/der Nutzer:in mit diesem Filter überein. |
| Prüfen, ob das Zeitattribut **weniger als X Tage** **zurückliegt** | **LESS THAN** | **ANZAHL DER TAGE ZURÜCK** | Wenn dieser Filter `7` angibt und ein Kundenprofil ein Datum hat, das weniger als sieben Tage zurückliegt, stimmt die/der Nutzer:in mit diesem Filter überein.|
| Prüfen, ob das Zeitattribut **in mehr als X Tagen** **in der Zukunft** liegt | **IN MORE THAN** | **ANZAHL DER TAGE IN DER ZUKUNFT** | Wenn dieser Filter `7` angibt und ein Kundenprofil ein Datum hat, das mehr als sieben Tage in der Zukunft liegt, stimmt die/der Nutzer:in mit diesem Filter überein.|
| Prüfen, ob das Zeitattribut **in weniger als X Tagen** **in der Zukunft** liegt | **IN LESS THAN** | **ANZAHL DER TAGE IN DER ZUKUNFT** | Wenn dieser Filter `7` angibt und ein Kundenprofil ein Datum hat, das weniger als sieben Tage in der Zukunft liegt, stimmt die/der Nutzer:in mit diesem Filter überein.|
| Prüfen, ob das Zeitattribut im Profil einer/eines Nutzer:in **existiert** und nicht null ist | **IS NOT BLANK** | **N/A** | Wenn dieser Filter ein Zeitattribut angibt, das in einem Kundenprofil vorhanden ist, stimmt die/der Nutzer:in mit diesem Filter überein.|
| Prüfen, ob das Zeitattribut im Profil einer/eines Nutzer:in **nicht existiert** oder null ist | **IS BLANK** | **N/A** | Wenn dieser Filter ein Zeitattribut angibt, das nicht in einem Kundenprofil vorhanden ist, stimmt die/der Nutzer:in mit diesem Filter überein. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Details zu Zeitattributen {#time-attribute-details}

{% multi_lang_include data_activation/day_of_recurring_event_filter.md %}

### Objekte {#objects}

Sie können verschachtelte angepasste Attribute verwenden, um Objekte als Datentyp für angepasste Attribute zu senden. Weitere Informationen finden Sie unter [Verschachtelte angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support).

### Arrays von Objekten {#arrays-of-objects}

Verwenden Sie ein Array von Objekten, um verwandte Attribute zu gruppieren. Weitere Details finden Sie in unserem Artikel über [Array von Objekten]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects).

### Konsolidierte Operatoren {#consolidated-operators}

Wir haben die Liste der verfügbaren Operatoren für Attributfilter, angepasste Attributfilter und verschachtelte angepasste Attributfilter konsolidiert. Wenn Sie vorhandene Filter mit diesen Operatoren verwenden, werden diese automatisch auf die neuen Operatoren aktualisiert.

| Datentyp | Alter Operator | Neuer Operator | Wert |
| --- | --- | --- | --- |
| String | equals | is any of | Mindestens 1 Wert |
| String | does not equal | is none of | Mindestens 1 Wert |
| Array | includes value | includes any of | Mindestens 1 Wert |
| Array | doesn't include value | includes none of | Mindestens 1 Wert |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Kauf- und Umsatz-Tracking {#purchase-revenue-tracking}

Die Verwendung unserer Kaufmethoden zur Erfassung von In-App-Käufen legt den Lifetime Value (LTV) für jedes einzelne Kundenprofil fest. Diese Daten sind auf unserer Umsatzseite in Zeitreihen einsehbar.

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen, ob der Gesamtbetrag der ausgegebenen Dollar **größer als** eine **Zahl** ist | **GREATER THAN** | **NUMBER** | Wenn dieser Filter `500` angibt und ein Kundenprofil einen Wert größer als `500` hat, wird der/die Nutzer:in diesen Filter erfüllen. |
| Prüfen, ob der Gesamtbetrag der ausgegebenen Dollar **weniger als** eine **Zahl** ist | **LESS THAN** | **NUMBER** | Wenn dieser Filter `500` angibt und ein Kundenprofil einen Wert kleiner als `500` hat, wird der/die Nutzer:in diesen Filter erfüllen. |
| Prüfen, ob der Gesamtbetrag der ausgegebenen Dollar **genau** einer **Zahl** entspricht | **EXACTLY** | **NUMBER** | Wenn dieser Filter `500` angibt und ein Kundenprofil den Wert `500` hat, wird der/die Nutzer:in diesen Filter erfüllen. |
| Prüfen, ob der letzte Kauf **nach dem Datum X** stattfand | **AFTER** | **TIME** | Wenn dieser Filter `2024/31/1` angibt und der letzte Kauf eines/einer Nutzer:in nach `2024/31/1` war, wird der/die Nutzer:in diesen Filter erfüllen. |
| Prüfen, ob der letzte Kauf **vor dem Datum X** stattfand | **BEFORE** | **TIME** | Wenn dieser Filter `2024/31/1` angibt und der letzte Kauf eines/einer Nutzer:in vor `2024/31/1` war, wird der/die Nutzer:in diesen Filter erfüllen. |
| Prüfen, ob der letzte Kauf **mehr als X Tage her** ist | **MORE THAN** | **TIME** | Wenn dieser Filter `7` angibt und der letzte Kauf eines/einer Nutzer:in mehr als sieben Tage ab heute zurückliegt, wird der/die Nutzer:in diesen Filter erfüllen. |
| Prüfen, ob der letzte Kauf **weniger als X Tage her** ist | **LESS THAN** | **TIME** | Wenn dieser Filter `7` angibt und der letzte Kauf eines/einer Nutzer:in weniger als sieben Tage ab heute zurückliegt, wird der/die Nutzer:in diesen Filter erfüllen. |
| Prüfen, ob der Kauf **mehr als X (Max = 50) Mal** stattfand | **MORE THAN** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** | Wenn dieser Filter `7` Mal und `21` Tage angibt und ein:e Nutzer:in in den letzten 21 Tagen mehr als sieben Käufe getätigt hat, wird der/die Nutzer:in diesen Filter erfüllen. |
| Prüfen, ob der Kauf **weniger als X (Max = 50) Mal** stattfand | **LESS THAN** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** | Wenn dieser Filter `7` Mal und `21` Tage angibt und ein:e Nutzer:in in den letzten 21 Tagen weniger als sieben Käufe getätigt hat, wird der/die Nutzer:in diesen Filter erfüllen. |
| Prüfen, ob der Kauf **genau X (Max = 50) Mal** stattfand | **EXACTLY** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** | Wenn dieser Filter `7` Mal und `21` Tage angibt und ein:e Nutzer:in in den letzten 21 Tagen sieben Käufe getätigt hat, wird der/die Nutzer:in diesen Filter erfüllen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
Wenn Sie nach der Anzahl der Male segmentieren möchten, die ein bestimmter Kauf stattgefunden hat, sollten Sie diesen Kauf auch einzeln als [inkrementierendes angepasstes Attribut]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes#incrementingdecrementing-custom-attributes) erfassen.
{% endalert %}

Sie können den Datentyp Ihres angepassten Attributs ändern, sollten sich jedoch der Auswirkungen einer [Änderung des Datentyps]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#changing-custom-attribute-or-event-data-type) bewusst sein.