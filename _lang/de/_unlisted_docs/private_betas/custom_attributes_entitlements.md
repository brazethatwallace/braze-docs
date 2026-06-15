---
article_title: Angepasste Attribute
permalink: "/custom_attributes_entitlements/"
hidden: true
---

# [![Braze-Lernkurs]({% image_buster /assets/unlisted_docs/img/logos/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Angepasste Attribute {#braze-learning-course-image_buster-assetsunlisted_docsimglogosbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-attributes}

> Diese Seite behandelt angepasste Attribute, die eine Sammlung der einzigartigen Merkmale Ihrer Nutzer:innen darstellen. Angepasste Attribute eignen sich am besten zum Speichern von Attributen über Ihre Nutzer:innen oder von Informationen über Aktionen mit geringem Wert innerhalb Ihrer Anwendung.

Wenn sie in Braze gespeichert werden, können angepasste Attribute verwendet werden, um Zielgruppen-Segmente aufzubauen und Nachrichten mithilfe von Liquid zu personalisieren. Beachten Sie, dass wir keine Zeitreihendaten für angepasste Attribute speichern, sodass Sie keine Diagramme auf deren Basis erstellen können, wie es bei angepassten Events möglich ist.

## Berechtigungen {#entitlements}

Berechtigungen bestimmen Ihre Kapazität für angepasste Attribute, die die Anzahl der verschiedenen Attributnamen verfolgt, die Sie definieren. Sie können bis zu 1.000 angepasste Attribute pro Workspace haben. Wenn Sie Ihre Kapazität erhöhen müssen, wenden Sie sich an Ihren Braze Account Manager für weitere Informationen.

Wenn sich Ihr Workspace der maximalen Anzahl angepasster Attribute nähert, erhalten Sie Benachrichtigungen im Dashboard und per E-Mail, um Sie auf dem Laufenden zu halten.

Auch nach Erreichen der Kapazität können bestehende angepasste Attribute weiterhin empfangen werden. Sie können jedoch keine neuen angepassten Attribute erstellen. Alle Daten, die für angepasste Attribute empfangen werden, die noch nicht existieren, werden nicht verarbeitet.

## Angepasste Attribute verwalten {#managing-custom-attributes}

Um angepasste Attribute im Dashboard zu erstellen und zu verwalten, gehen Sie zu **Dateneinstellungen** > **Angepasste Attribute**.

![Vier angepasste Attribute, die boolesche Werte sind.]({% image_buster /assets/unlisted_docs/img/custom_attributes_entitlements/export_custom_attributes.png %})

Die Spalte **Zuletzt aktualisiert** zeigt den letzten Zeitpunkt an, zu dem das angepasste Attribut bearbeitet wurde, z. B. wann es zuletzt auf die Blockliste gesetzt oder aktiviert wurde.

{% alert important %}
Für ein korrektes Nachrichten-Targeting stellen Sie sicher, dass der Datentyp Ihres angepassten Attributs mit dem tatsächlichen angepassten Attribut übereinstimmt.
{% endalert %}

Von dieser Seite aus können Sie bestehende angepasste Attribute anzeigen, verwalten, erstellen oder auf die Blockliste setzen. Wählen Sie das Menü neben einem angepassten Attribut für die folgenden Aktionen:

### Auf die Blockliste setzen {#blocklisting}

Angepasste Attribute können einzeln über das Aktionsmenü auf die Blockliste gesetzt werden, oder es können bis zu 100 Attribute ausgewählt und in einem Vorgang auf die Blockliste gesetzt werden. Wenn Sie ein angepasstes Attribut blockieren, werden keine Daten mehr zu diesem Attribut erfasst, bestehende Daten sind nicht verfügbar, es sei denn, sie werden reaktiviert, und blockierte Attribute werden nicht in Filtern oder Diagrammen angezeigt. Wenn das Attribut derzeit von Filtern oder Triggern in anderen Bereichen des Braze-Dashboards referenziert wird, erscheint außerdem ein Warnhinweis, der erklärt, dass alle Instanzen der Filter oder Trigger, die darauf verweisen, entfernt und archiviert werden.

### Als personenbezogene Daten (PII) markieren {#marking-as-personally-identifiable-information-pii}

Administrator:innen können auch angepasste Attribute erstellen und sie auf dieser Seite als PII markieren. Diese Attribute sind nur für Administrator:innen und Dashboard-Nutzer:innen mit der Berechtigung „Als PII markierte angepasste Attribute anzeigen“ sichtbar.

### Beschreibungen hinzufügen {#adding-descriptions}

Sie können einem angepassten Attribut nach der Erstellung eine Beschreibung hinzufügen, wenn Sie die [Nutzerberechtigung](https://www.braze.com/docs/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) `Manage Events, Attributes, Purchases` haben. Bearbeiten Sie das angepasste Attribut und geben Sie ein, was Sie möchten, z. B. eine Notiz für Ihr Team.

### Tags hinzufügen {#adding-tags}

Sie können einem angepassten Attribut nach der Erstellung Tags hinzufügen, wenn Sie die [Nutzerberechtigung](https://www.braze.com/docs/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) „Manage Events, Attributes, Purchases“ haben. Die Tags können dann verwendet werden, um die Liste der Attribute zu filtern.

### Angepasste Attribute entfernen {#removing-custom-attributes}

Es gibt zwei Möglichkeiten, angepasste Attribute aus Nutzerprofilen zu entfernen:

* Wählen Sie den Namen des zu entfernenden angepassten Attributs in einem [Nutzeraktualisierung-Schritt](https://www.braze.com/docs/user_guide/engagement_tools/canvas/canvas_components/user_update/#removing-custom-attributes) aus.
* Setzen Sie den Wert `null` in Ihrer API-Anfrage an den [`/users/track`-Endpunkt](https://www.braze.com/docs/api/endpoints/user_data/post_user_track#user-track).

### Nutzungsberichte anzeigen {#viewing-usage-reports}

Der Nutzungsbericht listet alle Canvases, Campaigns und Segmente auf, die ein bestimmtes angepasstes Attribut verwenden. Diese Liste enthält keine Verwendungen von Liquid.

Sie können bis zu 100 Nutzungsberichte gleichzeitig anzeigen, indem Sie die Kontrollkästchen neben den jeweiligen angepassten Attributen aktivieren und dann **Nutzungsbericht anzeigen** auswählen.

### Daten exportieren {#exporting-data}

Um die Liste der angepassten Attribute als CSV-Datei zu exportieren, wählen Sie **Alle exportieren** oben auf der Seite. Die CSV-Datei wird generiert, und ein Download-Link wird Ihnen per E-Mail zugesendet.

## Angepasste Attribute festlegen {#setting-custom-attributes}

Im Folgenden finden Sie Methoden für verschiedene Plattformen, die zum Festlegen angepasster Attribute verwendet werden.

{% details Für Dokumentation nach Plattform aufklappen %}

- [Android und FireOS](https://www.braze.com/docs/developer_guide/analytics/setting_user_attributes/?sdktab=android)
- [iOS](https://www.braze.com/docs/developer_guide/analytics/setting_user_attributes/?sdktab=swift)
- [Web](https://www.braze.com/docs/developer_guide/analytics/setting_user_attributes/?sdktab=web)
- [React Native](https://www.braze.com/docs/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-attributes)
- [Unity](https://www.braze.com/docs/developer_guide/platform_integration_guides/unity/Analytics/setting_custom_attributes/)
- [Xamarin](https://www.braze.com/docs/developer_guide/platform_integration_guides/xamarin/analytics/#setting-custom-attributes)
- [Roku](https://www.braze.com/docs/developer_guide/analytics/setting_user_attributes/)

{% enddetails %}

## Speicherung angepasster Attribute {#custom-attribute-storage}

Alle auf dem **Nutzerprofil** gespeicherten Daten, einschließlich der Daten angepasster Attribute, werden auf unbestimmte Zeit aufbewahrt, solange jedes Profil [aktiv](https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users) ist.

## Datentypen angepasster Attribute {#custom-attribute-data-types}

Angepasste Attribute sind außerordentlich flexible Werkzeuge, die ein präzises Targeting ermöglichen.

Die folgenden Datentypen können als angepasste Attribute gespeichert werden:

- [Boolesche Werte](#booleans)
- [Zahlen](#numbers)
- [Strings](#strings)
- [Arrays](#arrays)
- [Zeit](#time)
- [Objekte](https://www.braze.com/docs/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/)
- [Arrays von Objekten](https://www.braze.com/docs/user_guide/data/custom_data/custom_attributes/array_of_objects/)

### Boolesche Werte (wahr/falsch) {#booleans}

Boolesche Attribute sind nützlich zum Speichern einfacher binärer Daten über Ihre Nutzer:innen, wie z. B. Abo-Status. Sie können Nutzer:innen finden, bei denen eine Variable explizit auf einen wahren oder falschen Wert gesetzt ist, sowie solche, bei denen noch kein Eintrag für dieses Attribut vorliegt.

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen, ob der boolesche Wert entweder wahr, falsch, wahr oder nicht gesetzt, oder falsch oder nicht gesetzt **ist** | **IS**  | **TRUE**, **FALSE**, **TRUE OR NOT SET** oder **FALSE OR NOT SET** | Wenn dieser Filter `coffee_drinker` angibt, wird ein:e Nutzer:in diesen Filter unter folgenden Umständen erfüllen: <br> {::nomarkdown}<ul><li>Wenn dieser Filter <code>true</code> ist und der/die Nutzer:in den Wert <code>coffee_drinker</code> hat</li><li>Wenn dieser Filter <code>false</code> ist und der/die Nutzer:in den Wert <code>coffee_drinker</code> nicht hat</li><li>Wenn dieser Filter <code>true or not set</code> ist und der/die Nutzer:in den Wert <code>coffee_drinker</code> oder keinen Wert hat</li><li>Wenn dieser Filter <code>false or not set</code> ist und der/die Nutzer:in <code>coffee_drinker</code> oder keinen Wert hat</li></ul>{:/} |
| Prüfen, ob der boolesche Wert im Profil eines/einer Nutzer:in **existiert** und nicht null ist | **IS NOT BLANK**  | **N/A** | Wenn dieser Filter `coffee_drinker` angibt und ein Nutzerprofil einen Wert für das Attribut `coffee_drinker` hat, wird der/die Nutzer:in diesen Filter erfüllen. |
| Prüfen, ob der boolesche Wert im Profil eines/einer Nutzer:in **nicht existiert** oder null ist | **IS BLANK**  | **N/A** | Wenn dieser Filter `coffee_drinker` angibt und ein:e Nutzer:in entweder das Attribut `coffee_drinker` nicht hat oder der Wert für `coffee_drinker` null ist, wird der/die Nutzer:in diesen Filter erfüllen.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Zahlen {#numbers}

Numerische Attribute umfassen [Ganzzahlen](https://en.wikipedia.org/wiki/Integer) und [Gleitkommazahlen](https://en.wikipedia.org/wiki/Floating-point_arithmetic) und haben eine Vielzahl von Anwendungsfällen. Inkrementierende numerische angepasste Attribute sind nützlich, um zu speichern, wie oft eine bestimmte Aktion oder ein bestimmtes Ereignis stattgefunden hat, ohne Ihr Datenkontingent zu belasten. Standardzahlen haben vielfältige Verwendungsmöglichkeiten, wie z. B. die Erfassung von:

- Schuhgröße
- Taillenumfang
- Anzahl der Male, die ein:e Nutzer:in ein bestimmtes Produktfeature oder eine Kategorie angesehen hat

{% alert tip %}
Ausgegebenes Geld sollte nicht mit dieser Methode erfasst werden. Stattdessen sollte es über unsere [Kaufmethoden](#purchase-revenue-tracking) erfasst werden.
{% endalert %}

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen, ob das numerische Attribut **genau** einer **Zahl** entspricht | **EXACTLY** | **NUMBER** | Wenn dieser Filter `10` angibt und ein Nutzerprofil den Wert `10` hat, wird der/die Nutzer:in diesen Filter erfüllen. |
| Prüfen, ob das numerische Attribut **nicht gleich** einer **Zahl** ist | **DOES NOT EQUAL** | **NUMBER** | Wenn dieser Filter `10` angibt und ein Nutzerprofil nicht den Wert `10` hat, wird der/die Nutzer:in diesen Filter erfüllen. |
| Prüfen, ob das numerische Attribut **mehr als** eine **Zahl** ist | **MORE THAN** | **NUMBER** | Wenn dieser Filter `10` angibt und ein Nutzerprofil einen Wert größer als `10` hat, wird der/die Nutzer:in diesen Filter erfüllen. |
| Prüfen, ob das numerische Attribut **weniger als** eine **Zahl** ist | **LESS THAN** | **NUMBER** | Wenn dieser Filter `10` angibt und ein Nutzerprofil einen Wert kleiner als `10` hat, wird der/die Nutzer:in diesen Filter erfüllen. |
| Prüfen, ob das numerische Attribut im Profil eines/einer Nutzer:in **existiert** und nicht null ist | **IS NOT BLANK** | **N/A** | Wenn ein Nutzerprofil das angegebene numerische Attribut enthält, unabhängig vom Wert, wird der/die Nutzer:in diesen Filter erfüllen. |
| Prüfen, ob das numerische Attribut im Profil eines/einer Nutzer:in **nicht existiert** oder null ist | **IS BLANK** | **N/A** | Wenn ein Nutzerprofil das angegebene numerische Attribut nicht enthält oder der Wert des Attributs null ist, wird der/die Nutzer:in diesen Filter erfüllen.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Details zu Zahlenattributen {#number-attribute-details}

- Die Filter „Exactly 0“ und „Less Than“ schließen Nutzer:innen mit NULL-Feldern ein
  - Um Nutzer:innen ohne einen Wert für angepasste Attribute auszuschließen, müssen Sie den Filter **is not blank** einbeziehen.

### Strings (alphanumerische Zeichen) {#strings}

String-Attribute sind nützlich zum Speichern von Nutzereingaben, wie z. B. einer Lieblingsmarke, einer Telefonnummer oder eines letzten Suchbegriffs innerhalb Ihrer Anwendung. String-Attribute können bis zu 255 Zeichen lang sein.

Beachten Sie, dass Braze bei der Eingabe von Werten mit Leerzeichen zwischen, vor oder nach Wörtern auch nach denselben Leerzeichen sucht.

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen, ob das String-Attribut **genau mit** einem eingegebenen String **übereinstimmt** | **EQUALS** | **STRING**<br>Groß-/Kleinschreibung beachten | Wenn dieser Filter `book` angibt und ein Nutzerprofil ein String-Attribut für `last_item_purchased` hat, das `book` enthält, wird der/die Nutzer:in diesen Filter erfüllen. |
| Prüfen, ob das String-Attribut **teilweise mit** einem eingegebenen String **ODER** regulären Ausdruck **übereinstimmt** | **MATCHES REGEX** | **STRING** **OR** **REGULAR EXPRESSION** <br>Groß-/Kleinschreibung nicht beachten; maximal 32.764 Zeichen |
| Prüfen, ob das String-Attribut **nicht teilweise mit** einem eingegebenen String **ODER** regulären Ausdruck **übereinstimmt** | **DOES NOT MATCH REGEX** * | **STRING** **OR** **REGULAR EXPRESSION**<br>Groß-/Kleinschreibung nicht beachten; maximal 32.764 Zeichen |
| Prüfen, ob das String-Attribut **nicht mit** einem eingegebenen String **übereinstimmt** | **DOES NOT EQUAL** | **STRING**<br>Groß-/Kleinschreibung nicht beachten  | Wenn dieser Filter `book` angibt und ein Nutzerprofil ein String-Attribut für `last_item_purchased` hat, das nicht `book` enthält, wird der/die Nutzer:in diesen Filter erfüllen.|
| Prüfen, ob das String-Attribut im Profil eines/einer Nutzer:in **existiert** und kein leerer String ist | **IS NOT BLANK** | **N/A** | Wenn dieser Filter `favorite_genre` angibt und ein Nutzerprofil das Attribut `favorite_genre` hat, wird der/die Nutzer:in diesen Filter unabhängig vom Attributwert erfüllen. Zum Beispiel kann der/die Nutzer:in `sci-fi`, `romance` oder einen anderen Wert haben.|
| Prüfen, ob das String-Attribut im Profil eines/einer Nutzer:in **nicht existiert** | **BLANK** | **N/A** | Wenn dieser Filter `favorite_genre` angibt und ein Nutzerprofil das Attribut `favorite_genre` nicht hat, wird der/die Nutzer:in diesen Filter erfüllen.|
| Prüfen, ob der String genau mit **einem der** eingegebenen Strings **übereinstimmt** | **IS ANY OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Strings erlaubt (maximal 256) | Wenn dieser Filter `book`, `bookmark` und `reading light` angibt und ein Nutzerprofil mindestens einen dieser Strings hat, wird der/die Nutzer:in diesen Filter erfüllen. |
| Prüfen, ob das String-Attribut **nicht genau mit einem der** eingegebenen Strings **übereinstimmt** | **IS NONE OF** |**STRING**<br>Groß-/Kleinschreibung beachten; mehrere Strings erlaubt (maximal 256) | Wenn dieser Filter `book`, `bookmark` und `reading light` angibt und ein Nutzerprofil keinen dieser Strings enthält, wird der/die Nutzer:in den Filter erfüllen.|
| Prüfen, ob das String-Attribut **teilweise mit einem der** eingegebenen Strings **übereinstimmt** | **CONTAINS ANY OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Strings erlaubt (maximal 256) | Wenn dieser Filter `gold` angibt und ein Nutzerprofil `gold` in einem beliebigen String enthält, wie z. B. `gold_tier` oder `former_gold_tier`, wird der/die Nutzer:in den Filter erfüllen. |
| Prüfen, ob das String-Attribut **nicht teilweise mit einem der** eingegebenen Strings **übereinstimmt** | **DOESN'T CONTAIN ANY OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Strings erlaubt (maximal 256) | Wenn dieser Filter `gold` angibt und ein Nutzerprofil `gold` in keinem String enthält, wird der/die Nutzer:in diesen Filter erfüllen.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
Ein Datumsstring wie „12-1-2021“ oder „12/1/2021“ wird in ein Datetime-Objekt konvertiert und als [Zeitattribut](https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#time) behandelt.
{% endalert %}

{% alert important %}
Bei der Segmentierung mit dem Filter **DOES NOT MATCH REGEX** müssen Sie bereits ein angepasstes Attribut mit einem zugewiesenen Wert in diesem Nutzerprofil haben. Braze empfiehlt die Verwendung von „ODER“-Logik, um zu prüfen, ob ein angepasstes Attribut leer ist, damit Nutzer:innen korrekt angesprochen werden.
{% endalert %}

### Arrays {#arrays}

Array-Attribute eignen sich gut zum Speichern zusammengehöriger Informationslisten über Ihre Nutzer:innen. Zum Beispiel ermöglicht das Speichern der letzten 100 angesehenen Inhalte eines/einer Nutzer:in in einem Array eine spezifische Interessensegmentierung.

Standardmäßig ist die maximale Länge eines Arrays für ein Attribut auf 25 festgelegt und kann für ein einzelnes Array auf 100 erhöht werden. Wenn Sie beispielsweise ein Attribut wie „Angesehene Filme“ senden und es auf 100 eingestellt ist, wird beim Ansehen eines 101. Films der erste Film aus dem Array entfernt und der neueste Film hinzugefügt.

Wenn Sie dieses Maximum erhöhen möchten, wenden Sie sich an Ihren Customer-Success-Manager. Ihr Dashboard-Administrator kann dann die maximale Länge für einzelne Arrays auf über 100 erhöhen, und zwar über den Tab **Angepasste Attribute** auf der Seite **Einstellungen verwalten**.

Beachten Sie, dass Braze bei der Eingabe von Werten mit Leerzeichen zwischen, vor oder nach Wörtern auch nach denselben Leerzeichen sucht.

{% alert note %}
Die Option zur Erhöhung der maximalen Länge ist nicht verfügbar, wenn das Attribut auf automatische Erkennung des Datentyps eingestellt ist; der Datentyp muss auf Array gesetzt sein.
{% endalert %}

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen, ob das Array-Attribut **einen Wert enthält, der genau mit** einem eingegebenen Wert **übereinstimmt** | **INCLUDES VALUE** | **STRING** | Wenn dieser Filter `sci-fi` angibt und ein Nutzerprofil den Wert `sci-fi` hat, wird der/die Nutzer:in diesen Filter erfüllen.|
| Prüfen, ob das Array-Attribut **keinen Wert enthält, der genau mit** einem eingegebenen Wert **übereinstimmt** | **DOESN'T INCLUDE VALUE** | **STRING** | Wenn dieser Filter `sci-fi` angibt und ein Nutzerprofil den Wert `sci-fi` nicht hat, wird der/die Nutzer:in diesen Filter erfüllen.|
| Prüfen, ob das Array-Attribut **einen Wert enthält, der teilweise mit** einem eingegebenen Wert **ODER** regulären Ausdruck **übereinstimmt** | **MATCHES REGEX** | **STRING** **OR** **REGULAR EXPRESSION**<br>Maximal 32.764 Zeichen | |
| Prüfen, ob das Array-Attribut **einen beliebigen Wert hat** oder nicht leer ist | **HAS A VALUE** | **N/A** | Wenn dieser Filter `favorite_genres` angibt und ein Nutzerprofil `favorite_genres` mit einem beliebigen Wert enthält, wird der/die Nutzer:in diesen Filter erfüllen. |
| Prüfen, ob das Array-Attribut **leer ist** oder nicht existiert | **IS EMPTY** | **N/A** | Wenn dieser Filter `favorite_genres` angibt und ein Nutzerprofil `favorite_genres` nicht enthält oder `favorite_genres` enthält, aber keine Werte hat, wird der/die Nutzer:in diesen Filter erfüllen.|
| Prüfen, ob das Array-Attribut **einen Wert enthält, der genau mit einem der** eingegebenen Werte **übereinstimmt** | **INCLUDES ANY OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Werte erlaubt (maximal 256) | Wenn dieser Filter `sci-fi, fantasy, romance` angibt und ein Nutzerprofil eine beliebige Kombination von `sci-fi`, `fantasy` oder `romance` hat, einschließlich nur eines davon (wie nur `sci-fi`). Ein:e Nutzer:in kann `horror` oder einen anderen Wert in seinem/ihrem String haben, wenn er/sie auch einen der Werte `sci-fi`, `fantasy` und `romance` hat.|
| Prüfen, ob das Array-Attribut **keinen Wert enthält, der genau mit einem der** eingegebenen Werte **übereinstimmt** | **INCLUDES NONE OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Werte erlaubt (maximal 256) | Wenn dieser Filter `sci-fi, fantasy, romance` angibt und ein Nutzerprofil keine Kombination von `sci-fi`, `fantasy` oder `romance` hat, wird der/die Nutzer:in diesen Filter erfüllen. Der/die Nutzer:in kann `horror` oder einen anderen Wert haben, wenn er/sie keinen der Werte `sci-fi`, `fantasy` oder `romance` hat.|
| Prüfen, ob das Array-Attribut **einen Wert enthält, der teilweise mit einem der** eingegebenen Werte **übereinstimmt** | **VALUES CONTAIN ANY OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Werte erlaubt (maximal 256) | Wenn dieser Filter `gold` angibt und ein Nutzerprofil-Array `gold` in mindestens einem String enthält, wird der/die Nutzer:in diesen Filter erfüllen. Dies schließt String-Werte wie `gold_tier`, `former_gold_tier` und andere ein.|
| Prüfen, ob das Array-Attribut **keinen Wert enthält, der teilweise mit einem der** eingegebenen Werte **übereinstimmt** | **VALUES DON'T CONTAIN ANY OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Werte erlaubt (maximal 256) | Wenn dieser Filter `gold` angibt und ein Nutzerprofil-Array `gold` in keinem String enthält, wird der/die Nutzer:in diesen Filter erfüllen. Das bedeutet, dass Nutzer:innen mit String-Werten wie `gold_tier` und `former_gold_tier` diesen Filter nicht erfüllen.|
| Prüfen, ob das Array-Attribut **alle** eingegebenen Werte **enthält** | **IS ALL OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Werte erlaubt (maximal 256) | Wenn dieser Filter `sci-fi, fantasy, romance` angibt und ein Nutzerprofil alle diese Werte hat, wird der/die Nutzer:in diesen Filter erfüllen. Der/die Nutzer:in kann auch `horror` oder andere Werte haben und diesen Filter trotzdem erfüllen.|
| Prüfen, ob das Array-Attribut **nicht alle** eingegebenen Werte **enthält** | **ISN'T ALL OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Werte erlaubt (maximal 256) | Wenn dieser Filter `sci-fi, fantasy, romance` angibt und ein Nutzerprofil nicht alle diese Werte hat, wird der/die Nutzer:in diesen Filter erfüllen.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
Weitere Informationen zur Verwendung regulärer Ausdrücke (Regex) finden Sie in diesen Ressourcen:
- [Perl-kompatible reguläre Ausdrücke (PCRE)](https://www.regextester.com/pregsyntax.html)
- [Regex mit Braze](https://www.braze.com/docs/user_guide/engagement_tools/segments/regex/)
- [Regex-Debugger und -Tester](https://www.regex101.com/)
- [Regex-Tutorial](https://www.medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

### Zeit {#time}

Zeitattribute sind nützlich zum Speichern des letzten Zeitpunkts, zu dem eine bestimmte Aktion durchgeführt wurde, sodass Sie Ihren Nutzer:innen inhaltsspezifische Nachrichten zur erneuten Interaktion anbieten können.

Zeitfilter mit relativen Daten (z. B. mehr als 1 Tag her, weniger als 2 Tage her) messen 1 Tag als 24 Stunden. Jede Campaign, die Sie mit diesen Filtern ausführen, schließt alle Nutzer:innen in 24-Stunden-Schritten ein. Zum Beispiel erfasst `App zuletzt vor mehr als 1 Tag verwendet` alle Nutzer:innen, die „die App vor mehr als 24 Stunden“ ab dem genauen Zeitpunkt der Campaign-Ausführung zuletzt verwendet haben. Dasselbe gilt für Campaigns mit längeren Zeiträumen – fünf Tage ab Aktivierung bedeuten die vorherigen 120 Stunden.

Um beispielsweise ein Segment zu erstellen, das Nutzer:innen mit einem Zeitattribut zwischen 24 und 48 Stunden in der Zukunft anspricht, wenden Sie die Filter `in more than 1 day in the future` und `in less than 2 days in the future` an.

{% alert warning %}
Das letzte Datum, an dem ein angepasstes Event oder Kauf-Event aufgetreten ist, wird automatisch erfasst und sollte nicht erneut über ein angepasstes Zeitattribut erfasst werden.
{% endalert %}

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen, ob das Zeitattribut **vor** einem **ausgewählten Datum** liegt | **BEFORE** | **CALENDAR DATE SELECTOR** | Wenn dieser Filter `2024-01-31` angibt und ein Nutzerprofil ein Datum vor `2024-1-31` hat, wird der/die Nutzer:in diesen Filter erfüllen. |
| Prüfen, ob das Zeitattribut **nach** einem **ausgewählten Datum** liegt | **AFTER** | **CALENDAR DATE SELECTOR** | Wenn dieser Filter `2024-01-31` angibt und ein Nutzerprofil ein Datum nach `2024-1-31` hat, wird der/die Nutzer:in diesen Filter erfüllen. |
| Prüfen, ob das Zeitattribut **mehr als X Tage** **her** ist | **MORE THAN** | **NUMBER OF DAYS AGO** | Wenn dieser Filter `7` angibt und ein Nutzerprofil ein Datum hat, das mehr als sieben Tage zurückliegt, wird der/die Nutzer:in diesen Filter erfüllen. |
| Prüfen, ob das Zeitattribut **weniger als X Tage** **her** ist | **LESS THAN** | **NUMBER OF DAYS AGO** | Wenn dieser Filter `7` angibt und ein Nutzerprofil ein Datum hat, das weniger als sieben Tage zurückliegt, wird der/die Nutzer:in diesen Filter erfüllen.|
| Prüfen, ob das Zeitattribut **in mehr als X Tagen** **in der Zukunft** liegt | **IN MORE THAN** | **NUMBER OF DAYS IN FUTURE** | Wenn dieser Filter `7` angibt und ein Nutzerprofil ein Datum hat, das mehr als sieben Tage in der Zukunft liegt, wird der/die Nutzer:in diesen Filter erfüllen.|
| Prüfen, ob das Zeitattribut **in weniger als X Tagen** **in der Zukunft** liegt | **IN LESS THAN** | **NUMBER OF DAYS IN FUTURE**  | Wenn dieser Filter `7` angibt und ein Nutzerprofil ein Datum hat, das weniger als sieben Tage in der Zukunft liegt, wird der/die Nutzer:in diesen Filter erfüllen.|
| Prüfen, ob das Zeitattribut im Profil eines/einer Nutzer:in **existiert** und nicht null ist | **IS NOT BLANK** | **N/A** | Wenn dieser Filter ein Zeitattribut angibt, das in einem Nutzerprofil vorhanden ist, wird der/die Nutzer:in diesen Filter erfüllen.|
| Prüfen, ob das Zeitattribut im Profil eines/einer Nutzer:in **nicht existiert** oder null ist | **IS BLANK** | **N/A** | Wenn dieser Filter ein Zeitattribut angibt, das nicht in einem Nutzerprofil vorhanden ist, wird der/die Nutzer:in diesen Filter erfüllen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Details zu Zeitattributen {#time-attribute-details}

- Tag eines wiederkehrenden Ereignisses
  - Wenn Sie den Filter „Tag eines wiederkehrenden Ereignisses“ verwenden und dann aufgefordert werden, den „Kalendertag des wiederkehrenden Ereignisses“ auszuwählen, wird bei Auswahl von `IS LESS THAN` oder `IS MORE THAN` das aktuelle Datum für diesen Segmentierungsfilter mitgezählt.
  - Wenn Sie beispielsweise am 10. März 2020 das Datum des Attributs auf `LESS THAN ... March 10, 2020` setzen, werden Attribute für die Tage bis einschließlich 10. März 2020 berücksichtigt.
- Less than X Days Ago: Der Filter „Less than X Days Ago“ umfasst Daten zwischen X Tagen in der Vergangenheit und dem aktuellen Datum/der aktuellen Uhrzeit.
- Less than X Days in the Future: Umfasst Daten zwischen dem aktuellen Datum/der aktuellen Uhrzeit und X Tagen in der Zukunft.

### Objekte {#objects}

Sie können verschachtelte angepasste Attribute verwenden, um Objekte als Datentyp für angepasste Attribute zu senden. Weitere Informationen finden Sie unter [Verschachtelte angepasste Attribute](https://www.braze.com/docs/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/).

### Arrays von Objekten {#arrays-of-objects}

Verwenden Sie ein Array von Objekten, um zusammengehörige Attribute zu gruppieren. Weitere Details finden Sie in unserem Artikel zu [Arrays von Objekten](https://www.braze.com/docs/user_guide/data/custom_data/custom_attributes/array_of_objects/).

### Konsolidierte Operatoren {#consolidated-operators}

Wir haben die Liste der verfügbaren Operatoren für Attributfilter, angepasste Attributfilter und verschachtelte angepasste Attributfilter konsolidiert. Wenn Sie bestehende Filter mit diesen Operatoren haben, werden diese automatisch auf die neuen Operatoren aktualisiert.

| Datentyp | Alter Operator | Neuer Operator | Wert |
| --- | --- | --- | --- |
| String | equals | is any of | Mindestens 1 Wert |
| String | does not equal | is none of | Mindestens 1 Wert |
| Array | includes value | includes any of | Mindestens 1 Wert |
| Array | doesn't include value | includes none of | Mindestens 1 Wert |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Kauf- und Umsatz-Tracking {#purchase-revenue-tracking}

Die Verwendung unserer Kaufmethoden zur Erfassung von In-App-Käufen legt den Lifetime-Value (LTV) für jedes einzelne Nutzerprofil fest. Diese Daten sind auf unserer Umsatzseite in Zeitreihen einsehbar.

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen, ob der Gesamtbetrag der ausgegebenen Dollar **größer als** eine **Zahl** ist | **GREATER THAN** | **NUMBER** | Wenn dieser Filter `500` angibt und ein Nutzerprofil einen Wert größer als `500` hat, wird der/die Nutzer:in diesen Filter erfüllen. |
| Prüfen, ob der Gesamtbetrag der ausgegebenen Dollar **weniger als** eine **Zahl** ist | **LESS THAN** | **NUMBER** | Wenn dieser Filter `500` angibt und ein Nutzerprofil einen Wert kleiner als `500` hat, wird der/die Nutzer:in diesen Filter erfüllen.|
| Prüfen, ob der Gesamtbetrag der ausgegebenen Dollar **genau** einer **Zahl** entspricht | **EXACTLY** | **NUMBER** | Wenn dieser Filter `500` angibt und ein Nutzerprofil den Wert `500` hat, wird der/die Nutzer:in diesen Filter erfüllen. |
| Prüfen, ob der letzte Kauf **nach dem Datum X** stattfand | **AFTER** | **TIME** | Wenn dieser Filter `2024/31/1` angibt und der letzte Kauf eines/einer Nutzer:in nach `2024/31/1` war, wird der/die Nutzer:in diesen Filter erfüllen.|
| Prüfen, ob der letzte Kauf **vor dem Datum X** stattfand | **BEFORE** | **TIME** | Wenn dieser Filter `2024/31/1` angibt und der letzte Kauf eines/einer Nutzer:in vor `2024/31/1` war, wird der/die Nutzer:in diesen Filter erfüllen.|
| Prüfen, ob der letzte Kauf **mehr als X Tage her** ist | **MORE THAN** | **TIME** | Wenn dieser Filter `7` angibt und der letzte Kauf eines/einer Nutzer:in mehr als sieben Tage ab heute zurückliegt, wird der/die Nutzer:in diesen Filter erfüllen.|
| Prüfen, ob der letzte Kauf **weniger als X Tage her** ist | **LESS THAN** | **TIME** | Wenn dieser Filter `7` angibt und der letzte Kauf eines/einer Nutzer:in weniger als sieben Tage ab heute zurückliegt, wird der/die Nutzer:in diesen Filter erfüllen.|
| Prüfen, ob der Kauf **mehr als X (Max = 50) Mal** stattfand | **MORE THAN** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** | Wenn dieser Filter `7` Mal und `21` Tage angibt und ein:e Nutzer:in in den letzten 21 Tagen mehr als sieben Käufe getätigt hat, wird der/die Nutzer:in diesen Filter erfüllen.|
| Prüfen, ob der Kauf **weniger als X (Max = 50) Mal** stattfand | **LESS THAN** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** | Wenn dieser Filter `7` Mal und `21` Tage angibt und ein:e Nutzer:in in den letzten 21 Tagen weniger als sieben Käufe getätigt hat, wird der/die Nutzer:in diesen Filter erfüllen.|
| Prüfen, ob der Kauf **genau X (Max = 50) Mal** stattfand | **EXACTLY** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** | Wenn dieser Filter `7` Mal und `21` Tage angibt und ein:e Nutzer:in in den letzten 21 Tagen sieben Käufe getätigt hat, wird der/die Nutzer:in diesen Filter erfüllen.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
Wenn Sie nach der Anzahl der Male segmentieren möchten, die ein bestimmter Kauf stattgefunden hat, sollten Sie diesen Kauf auch einzeln als [inkrementierendes angepasstes Attribut](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/#incrementingdecrementing-custom-attributes) erfassen.
{% endalert %}

Sie können den Datentyp Ihres angepassten Attributs ändern, sollten sich jedoch der Auswirkungen einer [Änderung des Datentyps](https://www.braze.com/docs/help/help_articles/data/change_custom_data_type/) bewusst sein.