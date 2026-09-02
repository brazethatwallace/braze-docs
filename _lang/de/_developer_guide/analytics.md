---
nav_title: Analytics
article_title: Über Analytics für das Braze SDK
page_order: 2.6
description: "Erfahren Sie mehr über die Analytics des Braze SDK, damit Sie besser verstehen, welche Daten Braze erfasst, was der Unterschied zwischen angepassten Events und angepassten Attributen ist und wie Sie Analytics am besten verwalten."
platform:
  - Android
  - Swift
  - Web
  - Cordova
  - FireOS
  - Flutter
  - React Native
  - Roku
  - Unity
  - .NET MAUI
---

# Analytics

> Erfahren Sie mehr über die Analytics des Braze SDK, damit Sie besser verstehen, welche Daten Braze erfasst, was der Unterschied zwischen angepassten Events und angepassten Attributen ist und wie Sie Analytics am besten verwalten.

{% alert tip %}
Besprechen Sie während der Implementierung von Braze unbedingt die Marketingziele mit Ihrem Team, damit Sie am besten entscheiden können, welche Daten Sie tracken möchten und wie Sie sie mit Braze tracken wollen. Ein Beispiel finden Sie in unserem Anwendungsbeispiel zur [Taxi-/Mitfahr-App](#example-case) am Ende dieses Leitfadens.
{% endalert %}

## Automatisch erfasste Daten {#automatically-collected-data}

Bestimmte Nutzerdaten werden automatisch von unserem SDK erfasst – zum Beispiel „Erste App-Nutzung“, „Letzte App-Nutzung“, „Gesamtanzahl der Sitzungen“, „Geräte-Betriebssystem“ usw. Wenn Sie unsere Integrationsleitfäden befolgen, um unsere SDKs zu implementieren, können Sie diese [standardmäßige Datenerfassung]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection) nutzen. Ein Blick auf diese Liste kann Ihnen helfen, zu vermeiden, dass dieselben Informationen über Nutzer:innen mehrfach gespeichert werden. Mit Ausnahme von Sitzungsstart und -ende zählen alle anderen automatisch erfassten Daten nicht zu Ihrer Datenpunkt-Nutzung.

Lesen Sie unseren Artikel [SDK-Überblick]({{site.baseurl}}/developer_guide/getting_started/sdk_overview), um Prozesse auf die Allowlist zu setzen, die die standardmäßige Erfassung bestimmter Datenelemente blockieren.

## Angepasste Events {#custom-events}

Angepasste Events sind Aktionen, die Ihre Nutzer:innen ausführen. Sie eignen sich am besten zum Tracking von wichtigen Nutzer:innen-Interaktionen mit Ihrer Anwendung. Das Protokollieren eines angepassten Events kann eine beliebige Anzahl von Folgekampagnen mit konfigurierbaren Verzögerungen auslösen und ermöglicht die folgenden Segmentierungsfilter rund um die Aktualität und Häufigkeit dieses Events:

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen |
| ---------------------| --------------- | ------------- |
| Prüfen, ob das angepasste Event **mehr als X Mal** aufgetreten ist | **MEHR ALS** | **ANZAHL** |
| Prüfen, ob das angepasste Event **weniger als X Mal** aufgetreten ist | **WENIGER ALS** | **ANZAHL** |
| Prüfen, ob das angepasste Event **genau X Mal** aufgetreten ist | **GENAU** | **ANZAHL** |
| Prüfen, ob das angepasste Event zuletzt **nach dem Datum X** aufgetreten ist | **NACH** | **ZEITPUNKT** |
| Prüfen, ob das angepasste Event zuletzt **vor dem Datum X** aufgetreten ist | **VOR** | **ZEITPUNKT** |
| Prüfen, ob das angepasste Event zuletzt **vor mehr als X Tagen** aufgetreten ist | **MEHR ALS** | **ANZAHL TAGE HER** (positive Zahl) |
| Prüfen, ob das angepasste Event zuletzt **vor weniger als X Tagen** aufgetreten ist | **WENIGER ALS** | **ANZAHL TAGE HER** (positive Zahl) |
| Prüfen, ob das angepasste Event **mehr als X (Max = 50) Mal** aufgetreten ist | **MEHR ALS** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** |
| Prüfen, ob das angepasste Event **weniger als X (Max = 50) Mal** aufgetreten ist | **WENIGER ALS** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** |
| Prüfen, ob das angepasste Event **genau X (Max = 50) Mal** aufgetreten ist | **GENAU** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Angepasste Events" }

Braze erfasst, wie oft diese Events aufgetreten sind und wann sie zuletzt von den jeweiligen Nutzer:innen ausgeführt wurden, um eine Segmentierung zu ermöglichen. Auf der Analytics-Seite **Custom Events** können Sie aggregiert sehen, wie oft jedes angepasste Event auftritt, und dies im Zeitverlauf nach Segment für eine detailliertere Analyse betrachten. Dies ist besonders nützlich, um zu überprüfen, wie Ihre Campaigns die Aktivität angepasster Events beeinflusst haben, indem Sie die grauen Linien betrachten, die Braze über die Zeitreihe legt, um anzuzeigen, wann zuletzt eine Campaign gesendet wurde.

![Ein Analytics-Diagramm für angepasste Events mit Statistiken zu Nutzer:innen, die eine Kreditkarte hinzugefügt und eine Suche durchgeführt haben, über einen Zeitraum von dreißig Tagen.]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

{% alert note %}
[Inkrementierende angepasste Attribute]({{site.baseurl}}/api/endpoints/messaging) können verwendet werden, um einen Zähler für eine Nutzer:innen-Aktion ähnlich einem angepassten Event zu führen. Sie können jedoch keine Daten zu angepassten Attributen in einer Zeitreihe anzeigen. Nutzer:innen-Aktionen, die nicht in Zeitreihen analysiert werden müssen, sollten mit dieser Methode erfasst werden.
{% endalert %}

### Speicherung angepasster Events {#custom-event-storage}

Alle Nutzerprofildaten (angepasste Events, angepasste Attribute, angepasste Daten) werden gespeichert, solange diese Profile aktiv sind.

### Eigenschaften angepasster Events {#custom-event-properties}

Mit Eigenschaften angepasster Events ermöglicht Braze das Festlegen von Eigenschaften für angepasste Events und Käufe. Diese Eigenschaften können dann verwendet werden, um Trigger-Bedingungen weiter zu qualifizieren, die Personalisierung im Messaging zu verbessern und durch den Rohdatenexport anspruchsvollere Analytics zu erstellen. Eigenschaftswerte können String, Zahl, boolescher Wert oder Zeitobjekte sein. Eigenschaftswerte können jedoch keine Array-Objekte sein.

Wenn beispielsweise eine E-Commerce-Anwendung eine Nachricht an Nutzer:innen senden möchte, die ihren Warenkorb verlassen haben, könnte sie zusätzlich ihre Zielgruppe verbessern und eine stärkere Campaign-Personalisierung ermöglichen, indem sie eine angepasste Event-Eigenschaft für den `cart_value` der Warenkörbe der Nutzer:innen hinzufügt.

![Ein Beispiel für ein angepasstes Event, das eine Campaign an Nutzer:innen sendet, die ihren Warenkorb mit einem Warenkorbwert von mehr als 100 und weniger als 200 verlassen haben.]({% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png")

Eigenschaften angepasster Events können auch für die Personalisierung innerhalb des Messaging-Templates verwendet werden. Jede Campaign, die [aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) mit einem Trigger-Event verwendet, kann Eigenschaften angepasster Events dieses Events für die Messaging-Personalisierung nutzen. Wenn eine Gaming-Anwendung eine Nachricht an Nutzer:innen senden möchte, die ein Level abgeschlossen haben, könnte sie die Nachricht zusätzlich mit einer Eigenschaft für die Zeit personalisieren, die die Nutzer:innen zum Abschluss dieses Levels benötigt haben. In diesem Beispiel wird die Nachricht für drei verschiedene Segmente mithilfe von [bedingter Logik]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic) personalisiert. Die angepasste Event-Eigenschaft namens ``time_spent`` kann in die Nachricht eingefügt werden, indem ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}`` aufgerufen wird.

{% raw %}
```liquid
{% if {{event_properties.${time_spent}}} < 600 %}
Congratulations on beating that level so fast! Check out our online portal where you can play against top players from around the world!
{% elsif {{event_properties.${time_spent}}} < 1800 %}
Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Talk to villagers for essential tips on how to beat levels!
{% endif %}
```
{% endraw %}

Eigenschaften angepasster Events sollen Ihnen helfen, Ihr Messaging zu personalisieren oder granulare Campaigns mit aktionsbasierter Zustellung zu erstellen. Wenn Sie Segmente auf der Grundlage von Event-Eigenschafts-Aktualität und -Häufigkeit erstellen möchten, wenden Sie sich an Ihren Customer-Success-Manager oder unser Support-Team.

## Angepasste Attribute {#custom-attributes}

Angepasste Attribute sind außerordentlich flexible Werkzeuge, mit denen Sie Nutzer:innen gezielter ansprechen können, als es mit Standardattributen möglich wäre. Angepasste Attribute eignen sich hervorragend zum Speichern markenspezifischer Informationen über Ihre Nutzer:innen. Beachten Sie, dass wir keine Zeitreihendaten für angepasste Attribute speichern, sodass Sie keine Diagramme auf deren Basis erhalten – anders als im vorherigen Beispiel für angepasste Events.

### Speicherung angepasster Attribute {#custom-attribute-storage}

Alle Nutzerprofil-Daten (angepasste Events, angepasste Attribute, angepasste Daten) werden gespeichert, solange diese Profile aktiv sind.

### Datentypen angepasster Attribute {#custom-attribute-data-types}

Die folgenden Datentypen können als angepasste Attribute gespeichert werden:

#### Strings (alphanumerische Zeichen) {#strings-alphanumeric-characters}

String-Attribute sind nützlich, um Nutzereingaben zu speichern, z. B. eine Lieblingsmarke, eine Telefonnummer oder den letzten Suchbegriff in Ihrer Anwendung. String-Attribute unterliegen den [Längenbeschränkungen](#length-constraints) für angepasste Daten (479 Bytes; ca. 479 Einzelbyte-Zeichen oder ca. 160 Zeichen bei Mehrbyte-Schriften wie Japanisch).

Die folgende Tabelle beschreibt die verfügbaren Segmentierungsoptionen für String-Attribute.

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen |
| ---------------------| --------------- | ------------- |
| Prüfen, ob das String-Attribut **exakt mit** einem eingegebenen String **übereinstimmt** | **EQUALS** | **STRING** |
| Prüfen, ob das String-Attribut **teilweise mit** einem eingegebenen String **ODER** regulären Ausdruck **übereinstimmt** | **MATCHES REGEX** | **STRING** **ODER** **REGULAR EXPRESSION** |
| Prüfen, ob das String-Attribut **nicht teilweise mit** einem eingegebenen String **ODER** regulären Ausdruck **übereinstimmt** | **DOES NOT MATCH REGEX** | **STRING** **ODER** **REGULAR EXPRESSION** |
| Prüfen, ob das String-Attribut **nicht mit** einem eingegebenen String **übereinstimmt** | **DOES NOT EQUAL** | **STRING** |
| Prüfen, ob das String-Attribut **im Nutzerprofil vorhanden ist** | **IS BLANK** | **N/A** |
| Prüfen, ob das String-Attribut **nicht im Nutzerprofil vorhanden ist** | **IS NOT BLANK** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Strings (alphanumerische Zeichen)" }

{% alert important %}
Bei der Segmentierung mit dem Filter **DOES NOT MATCH REGEX** muss bereits ein angepasstes Attribut mit einem zugewiesenen Wert in diesem Nutzerprofil existieren. Braze empfiehlt die Verwendung von „ODER“-Logik, um zu prüfen, ob ein angepasstes Attribut leer ist, damit Sie Nutzer:innen korrekt ansprechen können.
{% endalert %}

{% alert tip %}
Weitere Informationen zur Verwendung unseres Regex-Filters finden Sie in dieser Dokumentation zu [Perl-kompatiblen regulären Ausdrücken (PCRE)](http://www.regextester.com/pregsyntax.html).
<br>
Weitere Ressourcen zu Regex:
- [Regex mit Braze]({{site.baseurl}}/user_guide/audience/segments/regex)
- [Regex-Debugger und -Tester](https://regex101.com/)
- [Regex-Tutorial](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

#### Arrays

Array-Attribute eignen sich gut zum Speichern zusammengehöriger Informationslisten über Ihre Nutzer:innen. Beispielsweise ermöglicht das Speichern der letzten 100 angesehenen Inhalte in einem Array eine spezifische Interessenssegmentierung.

Arrays angepasster Attribute sind eindimensionale Mengen; mehrdimensionale Arrays werden nicht unterstützt. **Beim Hinzufügen eines Elements zu einem Array eines angepassten Attributs wird das Element am Ende des Arrays angefügt, sofern es nicht bereits vorhanden ist – in diesem Fall wird es von seiner aktuellen Position ans Ende des Arrays verschoben.** Wenn beispielsweise ein Array `['hotdog','hotdog','hotdog','pizza']` importiert würde, wird es als `['hotdog', 'pizza']` im Array-Attribut angezeigt, da nur eindeutige Werte unterstützt werden.

Wenn das Array seine Höchstzahl an Elementen erreicht hat, wird das erste Element verworfen und das neue Element am Ende hinzugefügt. Der folgende Beispielcode zeigt das Array-Verhalten im Web-SDK:

```js
var abUser = appboy.getUser();
// initialize array for this user, assuming max length of favorite_foods is set to 4.
abUser.setCustomUserAttribute('favorite_foods', ['pizza', 'wings', 'pasta']); // => ['pizza', 'wings', 'pasta']
abUser.addToCustomAttributeArray('favorite_foods', 'fries'); // => ['pizza', 'wings', 'pasta', 'fries']
abUser.addToCustomAttributeArray('favorite_foods', 'pizza'); // => ['wings', 'pasta', 'fries', 'pizza']
abUser.addToCustomAttributeArray('favorite_foods', 'ice cream'); // => ['pasta', 'fries', 'pizza', 'ice cream']
```

Die Standard- und Höchstzahl an Elementen in einem Array beträgt 500. Sie können die Höchstzahl der Arrays im Braze-Dashboard unter **Data Settings** > **Custom Attributes** aktualisieren. Arrays, die die Höchstzahl an Elementen überschreiten, werden auf die Höchstzahl der Elemente gekürzt.

{% alert note %}
Wenn ein angepasstes Array-Attribut in einem Nutzerprofil angezeigt wird, aber keine Werte enthält, überprüfen Sie die **Max Length** des Attributs unter **Data Settings** > **Custom Attributes**. Eine **Max Length** von `0` verhindert, dass Werte im Profil angezeigt werden. Schritte zur Fehlerbehebung finden Sie unter [Datentypen angepasster Attribute]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#arrays).
{% endalert %}

Die folgende Tabelle beschreibt die verfügbaren Segmentierungsoptionen für Array-Attribute.

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen |
| ---------------------| --------------- | ------------- |
| Prüfen, ob das Array-Attribut **einen Wert enthält, der exakt mit** einem eingegebenen Wert **übereinstimmt** | **INCLUDES VALUE** | **STRING** |
| Prüfen, ob das Array-Attribut **keinen Wert enthält, der exakt mit** einem eingegebenen Wert **übereinstimmt** | **DOESN'T INCLUDE VALUE** | **STRING** |
| Prüfen, ob das Array-Attribut **einen Wert enthält, der teilweise mit** einem eingegebenen Wert **ODER** regulären Ausdruck **übereinstimmt** | **MATCHES REGEX** | **STRING** **ODER** **REGULAR EXPRESSION** |
| Prüfen, ob das Array-Attribut **einen beliebigen Wert hat** | **HAS A VALUE** | **N/A** |
| Prüfen, ob das Array-Attribut **leer ist** | **IS EMPTY** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Arrays" }

{% alert note %}
Wir verwenden [Perl-kompatible reguläre Ausdrücke (PCRE)](http://www.regextester.com/pregsyntax.html).
{% endalert %}

#### Datumsangaben {#dates}

Zeitattribute sind nützlich, um den letzten Zeitpunkt einer bestimmten Aktion zu speichern, sodass Sie Ihren Nutzer:innen inhaltlich gezielte Nachrichten zur erneuten Interaktion senden können.

{% alert note %}
Das letzte Datum, an dem ein angepasstes Event oder Kauf-Event stattgefunden hat, wird automatisch aufgezeichnet und sollte nicht zusätzlich über ein angepasstes Zeitattribut erfasst werden.
{% endalert %}

Datumsfilter, die relative Datumsangaben verwenden (z. B. vor mehr als 1 Tag, vor weniger als 2 Tagen), messen 1 Tag als 24 Stunden. Jede Campaign, die Sie mit diesen Filtern ausführen, erfasst alle Nutzer:innen in 24-Stunden-Schritten. Beispielsweise erfasst „App zuletzt vor mehr als 1 Tag verwendet“ alle Nutzer:innen, die die App zum exakten Zeitpunkt der Campaign-Ausführung „vor mehr als 24 Stunden zuletzt verwendet“ haben. Dasselbe gilt für Campaigns mit längeren Datumsbereichen – fünf Tage ab Aktivierung bedeuten die vorangegangenen 120 Stunden.

Die folgende Tabelle beschreibt die verfügbaren Segmentierungsoptionen für Zeitattribute.

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen |
| ---------------------| --------------- | ------------- |
| Prüfen, ob das Zeitattribut **vor** einem **ausgewählten Datum** liegt | **BEFORE** | **CALENDAR DATE SELECTOR** |
| Prüfen, ob das Zeitattribut **nach** einem **ausgewählten Datum** liegt | **AFTER** | **CALENDAR DATE SELECTOR** |
| Prüfen, ob das Zeitattribut **mehr als X Tage** zurückliegt | **MORE THAN** | **NUMBER OF DAYS AGO** |
| Prüfen, ob das Zeitattribut **weniger als X Tage** zurückliegt | **LESS THAN** | **NUMBER OF DAYS AGO** |
| Prüfen, ob das Zeitattribut **mehr als X Tage in der Zukunft** liegt | **IN MORE THAN** | **NUMBER OF DAYS IN FUTURE** |
| Prüfen, ob das Zeitattribut **weniger als X Tage in der Zukunft** liegt | **IN LESS THAN** | **NUMBER OF DAYS IN FUTURE** |
| Prüfen, ob das Zeitattribut **im Nutzerprofil vorhanden ist** | **BLANK** | **N/A** |
| Prüfen, ob das Zeitattribut **nicht im Nutzerprofil vorhanden ist** | **IS NOT BLANK** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Datumsangaben" }

#### Zahlen {#integers}

Numerische Attribute haben vielfältige Anwendungsfälle. Inkrementierende numerische angepasste Attribute eignen sich zum Speichern, wie oft eine bestimmte Aktion oder ein Event stattgefunden hat. Standardzahlen haben vielfältige Verwendungsmöglichkeiten, z. B. zur Erfassung der Schuhgröße, Taillenweite oder der Häufigkeit, mit der Nutzer:innen ein bestimmtes Produkt-Feature oder eine Kategorie angesehen haben.

{% alert note %}
Ausgaben sollten nicht mit dieser Methode erfasst werden. Verwenden Sie stattdessen unsere [Kauf-Methoden]({{site.baseurl}}/developer_guide/analytics#purchase-events--revenue-tracking).
{% endalert %}

Die folgende Tabelle beschreibt die verfügbaren Segmentierungsoptionen für numerische Attribute.

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen |
| ---------------------| --------------- | ------------- |
| Prüfen, ob das numerische Attribut **größer als** eine **Zahl** ist | **MORE THAN** | **NUMBER** |
| Prüfen, ob das numerische Attribut **kleiner als** eine **Zahl** ist | **LESS THAN** | **NUMBER** |
| Prüfen, ob das numerische Attribut **exakt** einer **Zahl** entspricht | **EXACTLY** | **NUMBER** |
| Prüfen, ob das numerische Attribut **ungleich** einer **Zahl** ist | **DOES NOT EQUAL** | **NUMBER** |
| Prüfen, ob das numerische Attribut **im Nutzerprofil vorhanden ist** | **EXISTS** | **N/A** |
| Prüfen, ob das numerische Attribut **nicht im Nutzerprofil vorhanden ist** | **DOES NOT EXIST** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Zahlen #integers" }

#### Boolesche Werte (wahr/falsch) {#booleans-truefalse}

Boolesche Attribute sind nützlich, um Abo-Status und andere einfache binäre Daten über Ihre Nutzer:innen zu speichern. Die bereitgestellten Eingabeoptionen ermöglichen es Ihnen, Nutzer:innen zu finden, für die eine Variable explizit auf einen booleschen Wert gesetzt wurde, sowie solche, bei denen dieses Attribut noch nicht erfasst wurde.

Die folgende Tabelle beschreibt die verfügbaren Segmentierungsoptionen für boolesche Attribute.

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen |
| ---------------------| --------------- | ------------- |
| Prüfen, ob der boolesche Wert **ist** | **IS** | **TRUE**, **FALSE**, **TRUE OR NOT SET** oder **FALSE OR NOT SET** |
| Prüfen, ob der boolesche Wert **im Nutzerprofil vorhanden ist** | **EXISTS** | **N/A** |
| Prüfen, ob der boolesche Wert **nicht im Nutzerprofil vorhanden ist** | **DOES NOT EXIST** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Boolesche Werte (wahr/falsch)" }

## Kauf-Events / Umsatz-Tracking {#purchase-events-revenue-tracking}

Die Verwendung unserer Kaufmethoden zur Erfassung von In-App-Käufen legt den Lifetime Value (LTV) für jedes einzelne Nutzerprofil fest. Diese Daten können auf unserer Umsatzseite in Zeitreihendiagrammen eingesehen werden.

Die folgende Tabelle beschreibt die verfügbaren Segmentierungsoptionen für Kauf-Events.

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen |
| ---------------------| --------------- | ------------- |
| Prüfen, ob der ausgegebene Gesamtbetrag in Dollar **größer als** eine **Zahl** ist | **GREATER THAN** | **NUMBER** |
| Prüfen, ob der ausgegebene Gesamtbetrag in Dollar **kleiner als** eine **Zahl** ist | **LESS THAN** | **NUMBER** |
| Prüfen, ob der ausgegebene Gesamtbetrag in Dollar **genau** einer **Zahl** entspricht | **EXACTLY** | **NUMBER** |
| Prüfen, ob der letzte Kauf **nach einem Datum X** stattfand | **AFTER** | **TIME** |
| Prüfen, ob der letzte Kauf **vor einem Datum X** stattfand | **BEFORE** | **TIME** |
| Prüfen, ob der letzte Kauf **vor mehr als X Tagen** stattfand | **MORE THAN** | **TIME** |
| Prüfen, ob der letzte Kauf **vor weniger als X Tagen** stattfand | **LESS THAN** | **TIME** |
| Prüfen, ob der Kauf **mehr als X-mal (Max = 50)** stattfand | **MORE THAN** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** |
| Prüfen, ob der Kauf **weniger als X-mal (Max = 50)** stattfand | **LESS THAN** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** |
| Prüfen, ob der Kauf **genau X-mal (Max = 50)** stattfand | **EXACTLY** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Kauf-Events / Umsatz-Tracking" }

{% alert note %}
Wenn Sie nach der Anzahl der Käufe eines bestimmten Produkts segmentieren möchten, sollten Sie diesen Kauf zusätzlich als einzelnes [inkrementierendes angepasstes Attribut](#integers) erfassen.
{% endalert %}

## Anwendungsfall Taxi-/Mitfahr-App {#example-case}

Nehmen wir als Beispiel eine Mitfahr-App, die entscheiden möchte, welche Nutzerdaten sie erfassen will. Die folgenden Fragen und der Brainstorming-Prozess sind ein hervorragendes Modell für Marketing- und Entwicklungsteams. Am Ende dieser Übung sollten beide Teams ein solides Verständnis davon haben, welche angepassten Events und Attribute sinnvollerweise erfasst werden sollten, um ihr Ziel zu erreichen.

**Fallfrage Nr. 1: Was ist das Ziel?**

Ihr Ziel ist ganz einfach: Sie wollen, dass Nutzer:innen über ihre App Taxifahrten anfordern.

**Fallfrage Nr. 2: Was sind die Zwischenschritte auf dem Weg von der App-Installation zu diesem Ziel?**

1. Die Nutzer:innen müssen den Registrierungsprozess beginnen und ihre persönlichen Daten ausfüllen.
2. Die Nutzer:innen müssen den Registrierungsprozess abschließen und verifizieren, indem sie einen Code in die App eingeben, den sie per SMS erhalten.
3. Sie müssen versuchen, ein Taxi zu rufen.
4. Um ein Taxi anzufordern, muss eines verfügbar sein, wenn sie suchen.

Diese Aktionen könnten dann als die folgenden angepassten Events getaggt werden:

- Registrierung begonnen
- Registrierung abgeschlossen
- Erfolgreiche Taxirufe
- Erfolglose Taxirufe

Nachdem Sie die Events implementiert haben, können Sie nun die folgenden Campaigns durchführen:

1. Nachrichten an Nutzer:innen senden, die mit der Registrierung begonnen, aber das Event „Registrierung abgeschlossen“ nicht innerhalb eines bestimmten Zeitrahmens ausgelöst haben.
2. Glückwunschnachrichten an Nutzer:innen senden, die die Registrierung abgeschlossen haben.
3. Entschuldigungen und Aktionsguthaben an Nutzer:innen senden, die erfolglos ein Taxi gerufen haben und auf die nicht innerhalb einer bestimmten Zeitspanne ein erfolgreicher Taxiruf folgte.
4. Aktionen an leistungsstarke Nutzer:innen mit vielen erfolgreichen Taxirufen senden, um ihnen für ihre Treue zu danken.

Und viele mehr!

**Fallfrage Nr. 3: Welche anderen Informationen sollten wir über unsere Nutzer:innen wissen, um unser Messaging zu verbessern?**

- Ob sie über Aktionsguthaben verfügen oder nicht?
- Die durchschnittliche Bewertung, die sie ihren Fahrer:innen geben?
- Eindeutige Aktionscodes für die Nutzer:innen?

Diese Merkmale könnten dann als die folgenden angepassten Attribute getaggt werden:

- Aktionsguthaben (Dezimaltyp)
- Durchschnittliche Fahrerbewertung (Zahlentyp)
- Eindeutiger Aktionscode (String-Typ)

Wenn Sie diese Attribute hinzufügen, haben Sie die Möglichkeit, Campaigns an Nutzer:innen zu senden, z. B.:

1. Erinnern Sie Nutzer:innen, die sich seit sieben Tagen nicht mehr eingeloggt haben, aber über ein Aktionsguthaben verfügen, daran, dass ihr Guthaben existiert und dass sie die App erneut besuchen sollten, um es zu nutzen!
2. Schreiben Sie Nutzer:innen, die niedrige Fahrerbewertungen abgeben, eine Nachricht, um direktes Kundenfeedback zu erhalten und zu erfahren, warum ihnen die Fahrt nicht gefallen hat.
3. Nutzen Sie unsere [Features zur Template-Erstellung und Personalisierung von Nachrichten]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize), um das eindeutige Aktionscode-Attribut in das Messaging für die Nutzer:innen einzufügen.

## Best Practices

### Allgemeine Best Practices {#general-best-practices}

#### Event-Eigenschaften verwenden {#use-event-properties}

- Benennen Sie ein angepasstes Event so, dass es eine Aktion beschreibt, die ein:e Nutzer:in ausführt.
- Nutzen Sie Event-Eigenschaften großzügig, um wichtige Daten über ein Event darzustellen.
- Anstatt beispielsweise ein separates angepasstes Event für das Ansehen von 50 verschiedenen Filmen zu erfassen, wäre es effektiver, einfach das Ansehen eines Films als Event zu erfassen und eine Event-Eigenschaft zu verwenden, die den Namen des Films enthält.

### Best Practices für die Entwicklung {#development-best-practices}

#### Nutzer:innen-IDs für alle Nutzer:innen festlegen {#set-user-ids-for-every-user}

Nutzer:innen-IDs sollten für alle Ihre Nutzer:innen festgelegt werden. Diese sollten unveränderlich und verfügbar sein, wenn ein:e Nutzer:in die App öffnet. Wir **empfehlen dringend**, diesen Bezeichner bereitzustellen, da er Ihnen Folgendes ermöglicht:

- Ihre Nutzer:innen geräte- und plattformübergreifend zu verfolgen, was die Qualität Ihrer Verhaltens- und demografischen Daten verbessert.
- Daten über Ihre Nutzer:innen mithilfe unserer [Nutzerdaten-API]({{site.baseurl}}/api/endpoints/user_data) zu importieren.
- Bestimmte Nutzer:innen mit unserer [Messaging-API]({{site.baseurl}}/api/endpoints/messaging) sowohl für allgemeine als auch für transaktionale Nachrichten anzusprechen.

Nutzer:innen-IDs müssen weniger als 512 Zeichen lang sein und sollten privat und nicht leicht zu ermitteln sein (zum Beispiel keine einfache E-Mail-Adresse oder kein Nutzername). Falls ein solcher Bezeichner nicht verfügbar ist, weist Braze Ihren Nutzer:innen einen eindeutigen Bezeichner zu, jedoch fehlen Ihnen dann die für Nutzer:innen-IDs aufgeführten Möglichkeiten. Sie sollten es vermeiden, Nutzer:innen-IDs für Nutzer:innen festzulegen, für die Sie keinen eindeutigen Bezeichner haben, der an sie als Individuum gebunden ist. Das Übergeben eines Geräte-Bezeichners bietet keinen Vorteil gegenüber dem automatischen anonymen Nutzer:innen-Tracking, das Braze standardmäßig anbietet. Im Folgenden finden Sie einige Beispiele für geeignete und ungeeignete Nutzer:innen-IDs.

Gute Optionen für Nutzer:innen-IDs:

- Gehashte E-Mail-Adresse oder eindeutiger Nutzername
- Eindeutiger Datenbankbezeichner

Diese sollten nicht als Nutzer:innen-IDs verwendet werden:

- Geräte-ID
- Zufallszahl oder Session-ID
- Jede nicht-eindeutige ID
- E-Mail-Adresse
- Nutzer:innen-ID eines anderen Drittanbieters

{% multi_lang_include alerts/important_alerts.md alert='SDK auth' %}

#### Angepassten Events und Attributen lesbare Namen geben {#give-custom-events-and-attributes-readable-names}

Stellen Sie sich vor, Sie sind ein Marketer, der ein oder zwei Jahre nach der Implementierung mit der Nutzung von Braze beginnt. Eine Dropdown-Liste voller Namen wie „usr_no_acct“ ohne weiteren Kontext zu lesen, kann einschüchternd sein. Wenn Sie Ihren Events und Attributen identifizierbare und lesbare Namen geben, wird es für alle Nutzer:innen Ihrer Plattform einfacher. Beachten Sie die folgenden Best Practices:

- Beginnen Sie ein angepasstes Event nicht mit einem Zahlenzeichen. Die Dropdown-Liste ist alphabetisch sortiert, und ein Anfang mit einer Zahl erschwert die Segmentierung nach dem gewünschten Filter.
- Vermeiden Sie nach Möglichkeit undurchsichtige Abkürzungen oder Fachjargon.
  - Beispiel: `usr_ctry` mag als Variablenname für das Land eines:einer Nutzer:in innerhalb eines Code-Abschnitts in Ordnung sein, aber das angepasste Attribut sollte an Braze als etwas wie `user_country` gesendet werden, um einem Marketer, der das Dashboard später nutzt, etwas Klarheit zu verschaffen.

#### Attribute nur protokollieren, wenn sie sich ändern {#only-log-attributes-when-they-change}

Wir zählen jedes an Braze übergebene Attribut als Datenpunkt, selbst wenn das übergebene Attribut denselben Wert enthält wie zuvor gespeichert. Das Protokollieren von Daten nur bei Änderungen hilft, redundante Datenpunkt-Nutzung zu vermeiden, und unterstützt ein reibungsloseres Erlebnis, indem unnötige API-Aufrufe vermieden werden.

#### Programmatisches Generieren von Event-Namen vermeiden {#avoid-programmatically-generating-event-names}

Wenn Sie ständig neue Event-Namen erstellen, wird es unmöglich, Ihre Nutzer:innen sinnvoll zu segmentieren. Sie sollten in der Regel generische Events erfassen (z. B. „Video angesehen“ oder „Artikel gelesen“) anstelle hochspezifischer Events wie „Gangnam Style angesehen“ oder „Artikel gelesen: Die 10 besten Mittagslokale in Midtown Manhattan“. Die spezifischen Daten über das Event sollten als Event-Eigenschaft und nicht als Teil des Event-Namens enthalten sein.

### Technische Einschränkungen und Beschränkungen {#technical-limitations-and-constraints}

Beachten Sie die folgenden Einschränkungen und Beschränkungen bei der Implementierung angepasster Events:

#### Längenbeschränkungen {#length-constraints}

Braze erzwingt eine Längenbeschränkung in Bytes (479 Bytes) für angepasste Event-Namen, angepasste Attributnamen (Schlüssel) und String-Werte angepasster Events. Werte, die dieses Limit überschreiten, werden abgeschnitten. In Zeichen ausgedrückt entspricht dies ungefähr 479 Ein-Byte-Zeichen (zum Beispiel ASCII) oder ungefähr 160 Zeichen für Mehrbyte-Schriftsysteme wie Japanisch (bei etwa 3 Bytes pro Zeichen in UTF-8). Halten Sie Namen und Werte idealerweise so kurz wie möglich, um die Netzwerk- und Akkuleistung Ihrer App zu verbessern — begrenzen Sie sie wenn möglich auf 50 Zeichen.

#### Inhaltsbeschränkungen {#content-constraints}

Die folgenden Inhalte werden programmatisch aus Ihren Attributen und Events entfernt. Achten Sie darauf, Folgendes nicht zu verwenden:

- Führende und nachfolgende Leerzeichen
- Zeilenumbrüche
- Alle Nicht-Ziffern in Telefonnummern
  - Beispiel: „(732) 178-1038“ wird zu „7321781038“ zusammengefasst
- Nicht-Leerzeichen müssen in Leerzeichen umgewandelt werden
- $ sollte nicht als Präfix für angepasste Events verwendet werden
- Alle ungültigen UTF-8-Kodierungswerte
  - „My \x80 Field“ wird zu „My Field“ zusammengefasst

#### Reservierte Schlüssel {#reserved-keys}

Die folgenden Schlüssel sind reserviert und können nicht als angepasste Event-Eigenschaften verwendet werden:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

#### Wertedefinitionen {#value-definitions}

- Ganzzahlen sind 64-Bit
- Dezimalzahlen haben standardmäßig 15 Dezimalstellen

### Parsen eines generischen Namensfelds {#parsing-a-generic-name-field}

Wenn für eine:n Nutzer:in nur ein einzelnes generisches Namensfeld vorhanden ist (zum Beispiel „JohnDoe“), können Sie diesen gesamten Titel dem Vornamen-Attribut Ihres:Ihrer Nutzer:in zuweisen. Zusätzlich können Sie versuchen, sowohl den Vor- als auch den Nachnamen des:der Nutzer:in anhand von Leerzeichen zu parsen, aber diese Methode birgt das potenzielle Risiko, einige Ihrer Nutzer:innen falsch zu benennen.