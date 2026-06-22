---
nav_title: "Attribute des Nutzerprofils"
article_title: Attributansichten für Nutzer:innen in Snowflake
page_order: 10
page_type: partner
search_tag: Partner
toc_headers: h2
---

# Attribute des Nutzerprofils {#user-profile-attributes}

> Diese Seite dient als Referenz für die Standard- und angepassten Attributansichten in Snowflake. Es gibt drei Ansichten für Standardattribute und drei Ansichten für angepasste Attribute, die jeweils für einen bestimmten Anwendungsfall mit eigenen Performance-Überlegungen konzipiert wurden.

## Datenparität mit dem Dashboard {#data-parity-with-the-dashboard}

In seltenen Fällen stimmen die Werte von Standard- und angepassten Attributen in den Snowflake-Ansichten auf dieser Seite möglicherweise nicht mit dem überein, was Sie im Nutzerprofil im Braze-Dashboard sehen.

Beispielsweise kann ein Attribut in Snowflake als `NULL` erscheinen, während das Dashboard einen Wert für diese:n Nutzer:in anzeigt.

Wenn Sie weitverbreitete Abweichungen feststellen, wenden Sie sich an Ihren Customer-Success-Manager oder den Braze Support.

## Verfügbare Ansichten {#available-views}

<table aria-label="Verfügbare Ansichten">
  <caption>Verfügbare Ansichten</caption>
  <thead>
    <tr>
      <th>Typ</th>
      <th>Ansicht</th>
      <th>Beschreibung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Standardattribut</td>
      <td><code>USER_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Schnappschüsse von Nutzerprofilen</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Realtime-Nutzerprofile</td>
    </tr>
    <tr>
      <td><code>USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>Historische Änderungsprotokolle</td>
    </tr>
    <tr>
      <td rowspan="3">Angepasstes Attribut</td>
      <td><code>USER_CUSTOM_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Schnappschüsse von Nutzerprofilen</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED</code></td>
      <td>Realtime-Nutzerprofile</td>
    </tr>
    <tr>
      <td><code>USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>Historische Änderungsprotokolle</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Verfügbare Ansichten" }

## Schnappschüsse von Nutzerprofilen {#user-profile-snapshots}

Diese Ansichten bieten regelmäßige Schnappschüsse der Attribute des Nutzerprofils. Die Daten werden um bis zu 12 Stunden verzögert, was sie für Abfragen nützlich macht, die keine Realtime-Updates erfordern.

 - `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`
 - `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`

### Verwendung {#usage}

* Liefert eine Momentaufnahme der Attribute von Nutzer:innen mit einer **Verzögerung von bis zu 12 Stunden**.
* Gute Performance bei Abfragen, die keine Realtime-Genauigkeit erfordern.
* Schnellere Abfrageausführung, insbesondere beim Filtern nach anderen Attributen als `USER_ID`.
* **Einschränkung:** Die Daten sind nicht in Realtime auf dem neuesten Stand.

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`-Schema

| Spaltenname     | Datentyp     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_USER_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL_ADDRESS` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE_NUMBER` | VARCHAR |
| `DOB` | VARCHAR |
| `TIMEZONE` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
| `ARCHIVED` | BOOLEAN |
{: .reset-td-br-1 .reset-td-br-2 aria-label="USERDEFAULTATTRIBUTESVIEWSHARED-Schema" }


### `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`-Schema

| Spaltenname     | Datentyp     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `EXTERNAL_USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `CUSTOM_ATTRIBUTES` | VARIANT |
| `ARCHIVED` | BOOLEAN |
{: .reset-td-br-1 .reset-td-br-2 aria-label="USERCUSTOMATTRIBUTESVIEWSHARED-Schema" }

## Realtime-Ansichten des Nutzerprofils {#real-time-user-profile-views}

Diese Ansichten bieten nahezu Realtime-Updates der Attribute des Nutzerprofils, wobei die Daten bis zu 10 Minuten nach einem Update in Braze verzögert werden.

  - `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`
  - `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`

### Verwendung

* Liefert aktuelle Attribute der Nutzer:innen mit minimaler Verzögerung (~10 Minuten).
* Nützlich für Realtime-Analysen und Szenarien, in denen aktuelle Daten benötigt werden.
* **Performance-Überlegungen:**
    * Abfragen zu einzelnen Nutzer:innen sind schneller (unter einer Minute bei einem großen Warehouse).
    * Abfragen ohne USER_ID-Filter erfordern eine Aggregation über alle Nutzer:innen, was zu deutlich längeren Ausführungszeiten führt.
    * Abfragen eines großen Datensatzes (z. B. über 100 Millionen Nutzer:innen) können viele Minuten dauern.

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`-Schema

| Spaltenname     | Datentyp     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `ARCHIVED` | BOOLEAN |
| `SF_UPDATED_AT` | TIMESTAMP_LTZ |
| `EXTERNAL_USER_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL_ADDRESS` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE_NUMBER` | VARCHAR |
| `DOB` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
| `TIMEZONE` | VARCHAR |
{: .reset-td-br-1 .reset-td-br-2 aria-label="USERLATESTSTATEDEFAULTATTRIBUTESVIEWSHARED-Schema" }

### `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`-Schema

| Spaltenname     | Datentyp     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `EXTERNAL_USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `ARCHIVED` | BOOLEAN |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `APP_ID` | VARCHAR |
| `CUSTOM_ATTRIBUTES` | OBJECT |
{: .reset-td-br-1 .reset-td-br-2 aria-label="USERLATESTSTATECUSTOMATTRIBUTEVIEWSHARED-Schema" }

## Historische Änderungsprotokolle {#historical-change-logs}

Diese Ansichten speichern historische Änderungsprotokolle von Nutzerattributen, wobei Änderungen mit einer Granularität von 12 Stunden erfasst werden.

- `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`
- `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`

### Verwendung

* Bietet eine Aufzeichnung historischer Änderungen an Nutzerattributen für einen rollierenden Zeitraum von 6 Monaten.
* Die Daten werden alle 12 Stunden in einem Snapshot festgehalten, d. h. mehrere Updates in diesem Fenster werden zu einem einzigen Datensatz zusammengefasst. Einzelne Änderungen innerhalb dieses Zeitraums werden nicht separat gespeichert.
* `EFF_DT` und `END_DT` markieren den Beginn und das Ende des Attribut-Status einer:eines Nutzer:in.

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`-Schema

| Spaltenname     | Datentyp     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_USER_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL_ADDRESS` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE_NUMBER` | VARCHAR |
| `DOB` | VARCHAR |
| `TIMEZONE` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
| `EFF_DT` | TIMESTAMP_NTZ |
| `END_DT` | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="USERDEFAULTATTRIBUTESHISTORYVIEWSHARED-Schema" }

### `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`-Schema

| Spaltenname     | Datentyp     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `EXTERNAL_USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `CUSTOM_ATTRIBUTES` | VARIANT |
| `ARCHIVED` | BOOLEAN |
| `EFF_DT` | TIMESTAMP_NTZ |
| `END_DT` | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="USERCUSTOMATTRIBUTESHISTORYVIEWSHARED-Schema" }

## Best Practices

### Empfohlene Abfrageverwendung {#recommended-query-usage}

| Anwendungsfall                                               | Empfohlene Ansichten                                   | Anmerkungen                                                                 |
|--------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------|
| **Allgemeine Abfragen**, die keine aktuellen Updates erfordern | `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` und `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`               | Schnelle Ausführung, mit Daten, die bis zu 12 Stunden alt sind.                          |
| Abfragen, die die **neuesten Attribute der Nutzer:innen** erfordern       | `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` und `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` | Bietet Updates nahezu in Realtime, kann aber bei großen Datenmengen langsamer sein. |
| **Historisches Tracking** von Attributänderungen           | `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` und `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`      | Speichert Attributänderungen mit einer Granularität von 12 Stunden.                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Empfohlene Abfrageverwendung" }

### Performance-Überlegungen {#performance-considerations}

* Abfragen auf `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` oder `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` sollten bei großen Datensätzen (~1 Milliarde Nutzer:innen) in einem großen Warehouse in unter 10 Sekunden zurückkommen.
* Abfragen auf `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` oder `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED ` für einzelne Nutzer:innen kommen in unter einer Minute zurück, skalieren aber schlecht ohne `USER_ID`-Filterung.
* Abfragen bei über 100 Millionen Nutzer:innen auf `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` oder `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` können aufgrund der Aggregation pro Nutzer:in mehrere Minuten dauern.