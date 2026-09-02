---
nav_title: SQL-Variablen
article_title: SQL-Variablen im Abfrage-Builder
page_order: 2
page_type: reference
description: "Erfahren Sie, wie Sie Variablen im Abfrage-Builder verwenden, um Ihre Abfragen wiederzuverwenden und das Hartcodieren von Daten in Ihrem Code zu vermeiden."
tool: Reports
---

# SQL-Variablen im Abfrage-Builder {#query-builder-sql-variables}

> Erfahren Sie, wie Sie SQL-Variablen im Abfrage-Builder verwenden, um Ihre Abfragen wiederzuverwenden und das Hartcodieren von Daten in Ihrem Code zu vermeiden.

## Warum SQL-Variablen verwenden? {#why-use-sql-variables}

Die Vorteile der Verwendung von SQL-Variablen umfassen:

{% multi_lang_include analytics/sql_variables_benefits.md %}

## Variablen verwenden {#using-variables}

### Schritt 1: Variable hinzufügen {#step-1-add-a-variable}

Um eine Variable zu Ihrer Abfrage hinzuzufügen, verwenden Sie die folgende Syntax:

{% raw %}
```sql
{{variable_type.${custom_label}}}
```
{% endraw %}

Ersetzen Sie Folgendes:

| Platzhalter | Beschreibung |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `variable_type` | Der vordefinierte Variablentyp, den Sie verwenden möchten, z. B. `campaign` oder `catalog_fields`. Die vollständige Liste finden Sie unter [Unterstützte Variablentypen](#variable-types). |
| `custom_label` | Das Label zur Identifizierung der Variable im Tab **Variablen** Ihres Abfrage-Builders. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 1: Variable hinzufügen" }

Im folgenden Beispiel wird die Gesamtzahl der Nutzer:innen zwischen dem ersten und letzten Tag eines Monats für eine Campaign abgefragt. Jeder Variable wird im nächsten Schritt ein Wert zugewiesen.

{% raw %}
```sql
SELECT COUNT(*) AS total_users
FROM USERS_CAMPAIGNS_REVENUE_SHARED
WHERE campaign_id = '{{campaign.${Campaign}}}'
  AND TIME > '{{start_date.${Month First Day}}}'
  AND TIME < '{{end_date.${Month Last Day}}}';
```
{% endraw %}

### Schritt 2: Wert zuweisen {#step-2-assign-a-value}

Standardmäßig wird der Tab **Variablen** im Abfrage-Builder nicht angezeigt. Er erscheint erst, nachdem Sie Ihre erste Variable zur Abfrage hinzugefügt haben. Dort können Sie ihr einen Wert zuweisen. Die spezifischen Werte, die Sie auswählen können, hängen vom [Typ](#variable-types) der jeweiligen Variable ab.

Im folgenden Beispiel wird die Campaign „Summer Feature Launch“ als Wert zugewiesen, zusammen mit dem ersten und letzten Tag des Juni 2025.

![Der Tab „Variablen“ im Abfrage-Builder mit dem angegebenen Beispiel.]({% image_buster /assets/img/query_builder_example.png %})

## Allgemeine Variablentypen {#variable-types}

### Zahl {#number}

`number` kann in Kombination mit anderen Nicht-String-Variablen verwendet werden. Akzeptiert jede positive oder negative Zahl, einschließlich Dezimalzahlen, wie z. B. `5.5`.

{% tabs %}
{% tab Verwendung %}
{% raw %}
```sql
some_number_column < {{number.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### String {#string}

Zum Ändern sich wiederholender String-Werte zwischen Berichtsausführungen. Verwenden Sie diese Variable, um das Hartcodieren eines Werts an mehreren Stellen in Ihrem SQL zu vermeiden.

{% tabs %}
{% tab Verwendung %}
{% raw %}
```sql
'{{string.${add a string here.}}}'
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Liste {#list}

Zur Auswahl aus einer Liste von Optionen.

{% tabs local %}
{% tab Einzelauswahl %}
{% subtabs %}
{% subtab Verwendung %}
{% raw %}
```sql
{{options.${metrics} | is_radio_button: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Mehrfachauswahl %}
{% subtabs %}
{% subtab Verwendung %}
{% raw %}
```sql
{{options.${metrics} | is_multi_select: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### Optionsfeld (Radio Button) {#radio-button}

Zum Anzeigen von Optionen als Optionsfelder anstelle eines Auswahl-Dropdowns im Tab **Variablen**. Dies kann nicht eigenständig verwendet werden&#8212;es muss in Kombination mit einer [Liste](#list) verwendet werden.

{% tabs %}
{% tab Verwendung %}
```sql
is_radio_button: 'true'
```
{% endtab %}
{% endtabs %}

![Ein Beispiel für ein in Braze gerendertes Optionsfeld.]({% image_buster /assets/img_archive/sql_variables_campaigns.png %}){: style="max-width:50%;"}

#### Mehrfachauswahl {#multi-select}

Legt fest, ob das Auswahl-Dropdown eine Einzel- oder Mehrfachauswahl ermöglicht. Dies kann nicht eigenständig verwendet werden&#8212;es muss in Kombination mit einer [Liste](#list) verwendet werden.

{% tabs %}
{% tab Verwendung %}
```sql
is_multi_select: 'true'
```
{% endtab %}
{% endtabs %}

![Ein Beispiel für eine in Braze gerenderte Mehrfachauswahlliste.]({% image_buster /assets/img_archive/sql_variables_productname.png %}){: style="max-width:50%;"}

#### Optionen {#options}

Zum Bereitstellen der Liste auswählbarer Optionen in Form eines Labels und eines Werts. Das Label wird angezeigt und der Wert ist das, wodurch die Variable ersetzt wird, wenn die Option ausgewählt wird. Dies kann nicht eigenständig verwendet werden&#8212;es muss in Kombination mit einer [Liste](#list) verwendet werden.

{% tabs %}
{% tab Verwendung %}
```sql
options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'
```
{% endtab %}
{% endtabs %}

## Braze-spezifische Variablentypen {#braze-specific-variable-types}

### Datumsbereich {#date-range}

Zum Anzeigen eines Kalenders zur Datumsauswahl. Ersetzen Sie `start_date` und `end_date` durch einen Unix-Zeitstempel in Sekunden für ein bestimmtes Datum in UTC, z. B. `1696517353`. Optional können Sie nur ein `start_date` oder `end_date` festlegen, um nur ein einzelnes Datum im Kalender anzuzeigen. Wenn die Labels Ihres `start_date` und `end_date` nicht übereinstimmen, werden sie als zwei separate Daten behandelt, anstatt als Datumsbereich.

{% tabs %}
{% tab Verwendung %}
{% raw %}
```
time > {{start_date.${custom_label}}} AND time < {{end_date.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

Sie können den Datumsbereich auf eine der folgenden Optionen festlegen. Wenn sowohl `start_date` als auch `end_date` verwendet werden und dasselbe Label haben, werden alle Optionen angezeigt. Andernfalls wird nur die angegebene Option angezeigt, wenn nur eine verwendet wird.

| Option | Beschreibung | Erforderliche Werte |
| --- | --- | --- |
| Relativ | Gibt die letzten X Tage an | Erfordert `start_date` |
| Startdatum | Gibt ein Startdatum an | Erfordert `start_date` |
| Enddatum | Gibt ein Enddatum an | Erfordert `end_date` |
| Datumsbereich | Gibt sowohl ein Start- als auch ein Enddatum an | Erfordert sowohl `start_date` als auch `end_date` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Datumsbereich" }

Ihr Liquid wird verwendet, um einen Kalender innerhalb des angegebenen Datumsbereichs anzuzeigen:

![Ein Beispiel für einen in Braze gerenderten Kalender.]({% image_buster /assets/img_archive/query_builder_time_range.png %}){: style="max-width:50%;"}

### Campaigns {#campaigns}

{% tabs local %}
{% tab Eine Campaign %}
Zur Auswahl einer Campaign. Wenn dasselbe Label mit einem Canvas geteilt wird, erscheint im Tab **Variablen** ein Optionsfeld zur Auswahl von entweder Canvas oder Campaign.

{% subtabs %}
{% subtab Verwendung %}
{% raw %}
```sql
campaign_id = '{{campaign.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Mehrere Campaigns %}
Zur Mehrfachauswahl von Campaigns. Wenn dasselbe Label mit einem Canvas geteilt wird, erscheint im Tab **Variablen** ein Optionsfeld zur Auswahl von entweder Canvas oder Campaign.

- **Ersetzungswert:** BSON-IDs der Campaigns

{% subtabs %}
{% subtab Verwendung %}
{% raw %}
```sql
campaign_id IN ({{campaigns.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Kampagnenvarianten %}
Zur Auswahl von Kampagnenvarianten, die zur ausgewählten Campaign gehören. Dies muss in Verbindung mit einer Campaign- oder Campaigns-Variable verwendet werden.

- **Ersetzungswert:** API-IDs der Kampagnenvarianten, kommagetrennte Strings wie `api-id1, api-id2`.

{% subtabs %}
{% subtab Verwendung %}
{% raw %}
```sql
message_variation_api_id IN ({{campaign_variants.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert important %}
Alle Campaign- und Canvas-Variablen müssen dieselben Bezeichner verwenden, um Zustände innerhalb einer einzelnen Gruppe zu synchronisieren.
{% endalert %}

### Canvase {#canvases}

{% tabs local %}
{% tab Ein Canvas %}
Zur Auswahl eines Canvas. Wenn dasselbe Label mit einer Campaign geteilt wird, erscheint im Tab **Variablen** ein Optionsfeld zur Auswahl von entweder Canvas oder Campaign.

- **Ersetzungswert:** BSON-ID des Canvas

{% subtabs %}
{% subtab Verwendung %}
{% raw %}
```sql
canvas_id = '{{canvas.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Mehrere Canvase %}
Zur Auswahl mehrerer Canvase. Wenn dasselbe Label mit einer Campaign geteilt wird, erscheint im Tab **Variablen** ein Optionsfeld zur Auswahl von entweder Canvas oder Campaign.

- **Ersetzungswert:** BSON-IDs der Canvase

{% subtabs %}
{% subtab Verwendung %}
{% raw %}
```sql
canvas_id IN ({{canvases.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Canvas-Varianten %}
Zur Auswahl von Canvas-Varianten, die zu einem ausgewählten Canvas gehören. Dies muss mit einer Canvas- oder Canvase-Variable verwendet werden. Wird auf eine oder mehrere API-IDs der Canvas-Varianten gesetzt, als kommagetrennte Zeichenkette, z. B. `api-id1, api-id2`.

{% subtabs %}
{% subtab Verwendung %}
{% raw %}
```sql
canvas_variation_api_id IN ({{canvas_variants.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Ein Canvas-Schritt %}
Zur Auswahl eines Canvas-Schritts, der zu einem ausgewählten Canvas gehört. Dies muss mit einer Canvas-Variable verwendet werden.

{% subtabs %}
{% subtab Verwendung %}
{% raw %}
```sql
canvas_step_api_id = '{{canvas_step.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Mehrere Canvas-Schritte %}
Zur Auswahl von Canvas-Schritten, die zu ausgewählten Canvase gehören. Dies muss mit einer Canvas- oder Canvase-Variable verwendet werden.

{% subtabs %}
{% subtab Verwendung %}
{% raw %}
```sql
canvas_step_api_id IN ({{canvas_steps.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert important %}
Alle Campaign- und Canvas-Variablen müssen dieselben Bezeichner verwenden, um Zustände innerhalb einer einzelnen Gruppe zu synchronisieren.
{% endalert %}

### Produkte {#products}

`products` wird verwendet, um ein oder mehrere Produkte aus dem Braze-Dashboard auszuwählen.

{% tabs %}
{% tab Verwendung %}
{% raw %}
```sql
({{products.${custom_label}}})
```
{% endraw %}
{% endtab %}

{% tab Beispiel %}
{% raw %}
```sql
SELECT product_name
FROM FULL_GAME_AND_DLC
WHERE product_id IN ({{products.${Games with DLC}}});
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Angepasste Events {#custom-events}

Wählen Sie ein oder mehrere angepasste Events oder Event-Eigenschaften angepasster Events aus einer Liste aus.

{% tabs local %}
{% tab Event %}
`custom_events` wird verwendet, um ein oder mehrere angepasste Events aus dem Braze-Dashboard auszuwählen.

{% subtabs %}
{% subtab Verwendung %}
{% raw %}
```sql
'{{custom_events.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}

{% subtab Beispiel %}
{% raw %}
```sql
SELECT event_name
FROM CUSTOM_EVENTS_TABLE
WHERE event_name IN ({{custom_events.${Purchased Game}}});
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Eigenschaften %}
`custom_event_properties` wird verwendet, um eine oder mehrere Eigenschaften des aktuell ausgewählten angepassten Events auszuwählen. Erfordert eine gesetzte `custom_events`-Variable.

{% subtabs %}
{% subtab Verwendung %}
{% raw %}
```sql
name = '{{custom_event_properties.${property names)}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Workspace {#workspace}

`workspace` wird verwendet, um einen einzelnen Workspace aus dem Braze-Dashboard auszuwählen.

{% tabs %}
{% tab Verwendung %}
{% raw %}
```sql
workspace_id = '{{workspace.${app_group_id}}}'
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Kataloge {#catalogs}

Wählen Sie einen oder mehrere Kataloge oder Katalogfelder aus einer Liste aus.

{% tabs local %}
{% tab Kataloge %}
`catalogs` wird verwendet, um einen oder mehrere Kataloge aus dem Braze-Dashboard auszuwählen.

{% subtabs %}
{% subtab Verwendung %}
{% raw %}
```sql
catalog_id = '{{catalogs.${catalog}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Katalogfelder %}
`catalog_fields` wird verwendet, um ein oder mehrere Felder des aktuell ausgewählten Katalogs festzulegen. Erfordert eine gesetzte `catalogs`-Variable.

{% subtabs %}
{% subtab Verwendung %}
{% raw %}
```sql
field_name = '{{catalog_fields.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Segments {#segments}

Zur Auswahl von Segmenten, bei denen [Analytics-Tracking]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking) aktiviert ist. Wird auf die Segment-Analytics-ID gesetzt, die den in der Spalte `user_segment_membership_ids` gespeicherten IDs in den Tabellen entspricht, in denen diese Spalte verfügbar ist.

{% tabs %}
{% tab Verwendung %}
{% raw %}
```sql
{{segments.${analytics_segments}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Tags {#tags}

Zur Auswahl von Tags für Campaigns und Canvase. Wird auf Campaigns und Canvase mit einfach zitierten, kommagetrennten BSON-IDs gesetzt, die mit den ausgewählten Tags verknüpft sind.

{% tabs %}
{% tab Verwendung %}
{% raw %}
```sql
{{tags.${some tags}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Variablen-Metadaten {#variable-metadata}

Metadaten können an eine Variable angehängt werden, um ihr Verhalten zu ändern, indem die Metadaten mit einem Pipe-Zeichen ( &#124; ) nach dem Variablen-Label angehängt werden. Die Reihenfolge der Metadaten spielt keine Rolle und Sie können beliebig viele anhängen. Außerdem können alle Arten von Metadaten für jede Variable verwendet werden, mit Ausnahme spezieller Metadaten, die für bestimmte Variablen spezifisch sind (dies wird in diesen Fällen angegeben). Die Verwendung aller Metadaten ist optional und dient dazu, das Standardverhalten der Variable zu ändern.

{% tabs %}
{% tab Verwendung %}
{% raw %}
```sql
{{string.${my var}| is_required: 'false' | description: 'My optional string var'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Boolescher Wert {#boolean}

Um festzustellen, ob der Wert einer Variable ausgefüllt ist. Dies ist nützlich für optionale Variablen, bei denen Sie eine Bedingung kurzschließen möchten, wenn der Wert einer Variable nicht ausgefüllt ist. Kann je nach Wert der anderen Variable auf `true` oder `false` gesetzt werden.

{% tabs %}
{% tab Verwendung %}
{% raw %}
```sql
{{string.${type_name_has_no_value} | visible: 'false'}} or {{string.${type_name_has_value} | visible: 'false'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

`type` und `name` beziehen sich auf die referenzierte Variable. Um beispielsweise die folgende optionale Variable kurzzuschließen: {% raw %}`{{campaigns.${messaging}}`{% endraw %}:

{% raw %}
```sql
{{string.${campaigns_messaging_has_no_value}  | visible: 'false'}} OR campaign_id IN ({{campaigns.${messaging} | is_required: 'false'}})
```
{% endraw %}

### Sichtbar {#visible}

Legt fest, ob Variablen sichtbar sind. Alle Variablen sind standardmäßig im Tab **Variablen** sichtbar, wo Sie Werte eingeben können.

Es gibt mehrere spezielle Variablen, deren Wert von einer anderen Variable abhängt, z. B. ob eine andere Variable einen Wert hat. Diese speziellen Variablen sind als nicht sichtbar markiert, damit sie nicht im Tab **Variablen** angezeigt werden.

{% tabs %}
{% tab Verwendung %}
```sql
visible: 'false'
```
{% endtab %}
{% endtabs %}

### Erforderlich {#required}

Legt fest, ob Variablen standardmäßig erforderlich sind. Ein leerer Wert für eine Variable führt in der Regel zu einer fehlerhaften Abfrage.

{% tabs %}
{% tab Verwendung %}
```sql
required: 'false'
```
{% endtab %}
{% endtabs %}

### Reihenfolge {#order}

Zur Auswahl der Position der Variable im Tab **Variablen**.

{% tabs %}
{% tab Verwendung %}
```sql
order: '1'
```
{% endtab %}
{% endtabs %}

### Anführungszeichen einschließen {#include-quotes}

{% tabs local %}
{% tab Einfache Anführungszeichen %}
Zum Umschließen der Werte einer Variable mit einfachen Anführungszeichen.

{% subtabs %}
{% subtab Verwendung %}
```sql
include_quotes: 'true'
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Doppelte Anführungszeichen %}
Zum Umschließen der Werte einer Variable mit doppelten Anführungszeichen.

{% subtabs %}
{% subtab Verwendung %}
```sql
include_double_quotes: 'true'
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Platzhalter {#placeholder}

Zum Festlegen des Platzhaltertexts, der im Eingabefeld der Variable angezeigt wird.

{% tabs %}
{% tab Verwendung %}
```sql
placeholder: 'enter some value'
```
{% endtab %}
{% endtabs %}

### Beschreibung {#description}

Zum Festlegen des Beschreibungstexts, der unter dem Eingabefeld der Variable angezeigt wird.

{% tabs %}
{% tab Verwendung %}
```sql
description: 'some description'
```
{% endtab %}
{% endtabs %}

### Standardwert {#default-value}

Zum Festlegen des Standardwerts für die Variable, wenn kein Wert angegeben wird.

{% tabs %}
{% tab Verwendung %}
```sql
default_value: '5'
```
{% endtab %}
{% endtabs %}

### Label ausblenden {#hide-label}

Zum Ausblenden des Labels der Variable.

{% tabs %}
{% tab Verwendung %}
```sql
hide_label: 'true'
```
{% endtab %}
{% endtabs %}