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

| Spaltenname     | Datentyp     | Beschreibung |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Ihr Braze-Workspace-Bezeichner |
| `APP_ID` | VARCHAR | Die spezifische App innerhalb Ihres Workspace |
| `USER_ID` | VARCHAR | Der eindeutige Braze-Nutzerbezeichner |
| `TIME` | NUMBER | Unix-Zeitstempel (Sekunden) des Profil-Updates |
| `TIME_MS` | NUMBER | Unix-Zeitstempel (Millisekunden) des Profil-Updates |
| `UPDATE_SOURCE` | VARCHAR | Die Quelle des Attribut-Updates (API, SDK, Dashboard usw.) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Wann die Daten zuletzt in Snowflake aktualisiert wurden |
| `EXTERNAL_USER_ID` | VARCHAR | Ihr eigener Nutzerbezeichner (falls gesetzt) |
| `FIRST_NAME` | VARCHAR | Vorname der:des Nutzer:in |
| `LAST_NAME` | VARCHAR | Nachname der:des Nutzer:in |
| `EMAIL_ADDRESS` | VARCHAR | E-Mail-Adresse der:des Nutzer:in |
| `GENDER` | VARCHAR | Geschlecht der:des Nutzer:in |
| `PHONE_NUMBER` | VARCHAR | Telefonnummer der:des Nutzer:in |
| `DOB` | VARCHAR | Geburtsdatum der:des Nutzer:in |
| `TIME_ZONE` | VARCHAR | Zeitzone der:des Nutzer:in |
| `HOME_CITY` | VARCHAR | Wohnort der:des Nutzer:in |
| `COUNTRY` | VARCHAR | Land der:des Nutzer:in |
| `LANGUAGE` | VARCHAR | Sprachpräferenz der:des Nutzer:in |
| `ARCHIVED` | BOOLEAN | Ob das Nutzerprofil archiviert ist |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERDEFAULTATTRIBUTESVIEWSHARED-Schema" }


### `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`-Schema

| Spaltenname     | Datentyp     | Beschreibung |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Ihr Braze-Workspace-Bezeichner |
| `APP_ID` | VARCHAR | Die spezifische App innerhalb Ihres Workspace |
| `USER_ID` | VARCHAR | Der eindeutige Braze-Nutzerbezeichner |
| `EXTERNAL_USER_ID` | VARCHAR | Ihr eigener Nutzerbezeichner (falls gesetzt) |
| `TIME` | NUMBER | Unix-Zeitstempel (Sekunden) des Profil-Updates |
| `TIME_MS` | NUMBER | Unix-Zeitstempel (Millisekunden) des Profil-Updates |
| `UPDATE_SOURCE` | VARCHAR | Die Quelle des Attribut-Updates (API, SDK, Dashboard usw.) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Wann die Daten zuletzt in Snowflake aktualisiert wurden |
| `CUSTOM_ATTRIBUTES` | VARIANT | JSON-Objekt mit allen angepassten Attributen (Schlüssel-Wert-Paare) |
| `ARCHIVED` | BOOLEAN | Ob das Nutzerprofil archiviert ist |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERCUSTOMATTRIBUTESVIEWSHARED-Schema" }

#### Arbeiten mit CUSTOM_ATTRIBUTES {#working-with-custom_attributes}

Die Spalte `CUSTOM_ATTRIBUTES` speichert alle Ihre angepassten Attribute als JSON-Objekt. Sie können auf einzelne Attribute über die JSON-Funktionen von Snowflake zugreifen.

**Beispiel: Bestimmte angepasste Attribute abfragen**

```sql
-- Get users with a specific loyalty tier
SELECT
  USER_ID,
  EXTERNAL_USER_ID,
  CUSTOM_ATTRIBUTES:loyalty_tier::STRING as loyalty_tier,
  CUSTOM_ATTRIBUTES:points::NUMBER as points
FROM USER_CUSTOM_ATTRIBUTES_VIEW_SHARED
WHERE CUSTOM_ATTRIBUTES:loyalty_tier::STRING = 'gold';

-- Get users who made a purchase above a certain amount
SELECT
  USER_ID,
  CUSTOM_ATTRIBUTES:last_purchase_amount::NUMBER as last_purchase_amount
FROM USER_CUSTOM_ATTRIBUTES_VIEW_SHARED
WHERE CUSTOM_ATTRIBUTES:last_purchase_amount::NUMBER > 100;
```

**Beispiel: Daten angepasster Attribute analysieren**

```sql
-- Count users by subscription status
SELECT
  CUSTOM_ATTRIBUTES:subscription_status::STRING as subscription_status,
  COUNT(*) as user_count
FROM USER_CUSTOM_ATTRIBUTES_VIEW_SHARED
GROUP BY CUSTOM_ATTRIBUTES:subscription_status::STRING;

-- Find average order value by customer segment
SELECT
  CUSTOM_ATTRIBUTES:customer_segment::STRING as segment,
  AVG(CUSTOM_ATTRIBUTES:lifetime_value::NUMBER) as avg_lifetime_value
FROM USER_CUSTOM_ATTRIBUTES_VIEW_SHARED
WHERE CUSTOM_ATTRIBUTES:customer_segment IS NOT NULL
GROUP BY CUSTOM_ATTRIBUTES:customer_segment::STRING;
```

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

| Spaltenname     | Datentyp     | Beschreibung |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Ihr Braze-Workspace-Bezeichner |
| `APP_ID` | VARCHAR | Die spezifische App innerhalb Ihres Workspace |
| `USER_ID` | VARCHAR | Der eindeutige Braze-Nutzerbezeichner |
| `TIME` | NUMBER | Unix-Zeitstempel (Sekunden) des Profil-Updates |
| `TIME_MS` | NUMBER | Unix-Zeitstempel (Millisekunden) des Profil-Updates |
| `UPDATE_SOURCE` | VARCHAR | Die Quelle des Attribut-Updates (API, SDK, Dashboard usw.) |
| `ARCHIVED` | BOOLEAN | Ob das Nutzerprofil archiviert ist |
| `SF_UPDATED_AT` | TIMESTAMP_LTZ | Wann die Daten zuletzt in Snowflake aktualisiert wurden |
| `EXTERNAL_USER_ID` | VARCHAR | Ihr eigener Nutzerbezeichner (falls gesetzt) |
| `FIRST_NAME` | VARCHAR | Vorname der:des Nutzer:in |
| `LAST_NAME` | VARCHAR | Nachname der:des Nutzer:in |
| `EMAIL_ADDRESS` | VARCHAR | E-Mail-Adresse der:des Nutzer:in |
| `GENDER` | VARCHAR | Geschlecht der:des Nutzer:in |
| `PHONE_NUMBER` | VARCHAR | Telefonnummer der:des Nutzer:in |
| `DOB` | VARCHAR | Geburtsdatum der:des Nutzer:in |
| `HOME_CITY` | VARCHAR | Wohnort der:des Nutzer:in |
| `COUNTRY` | VARCHAR | Land der:des Nutzer:in |
| `LANGUAGE` | VARCHAR | Sprachpräferenz der:des Nutzer:in |
| `TIME_ZONE` | VARCHAR | Zeitzone der:des Nutzer:in |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERLATESTSTATEDEFAULTATTRIBUTESVIEWSHARED-Schema" }

### `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`-Schema

| Spaltenname     | Datentyp     | Beschreibung |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Ihr Braze-Workspace-Bezeichner |
| `USER_ID` | VARCHAR | Der eindeutige Braze-Nutzerbezeichner |
| `EXTERNAL_USER_ID` | VARCHAR | Ihr eigener Nutzerbezeichner (falls gesetzt) |
| `TIME` | NUMBER | Unix-Zeitstempel (Sekunden) des Profil-Updates |
| `TIME_MS` | NUMBER | Unix-Zeitstempel (Millisekunden) des Profil-Updates |
| `UPDATE_SOURCE` | VARCHAR | Die Quelle des Attribut-Updates (API, SDK, Dashboard usw.) |
| `ARCHIVED` | BOOLEAN | Ob das Nutzerprofil archiviert ist |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Wann die Daten zuletzt in Snowflake aktualisiert wurden |
| `APP_ID` | VARCHAR | Die spezifische App innerhalb Ihres Workspace |
| `CUSTOM_ATTRIBUTES` | OBJECT | JSON-Objekt mit allen angepassten Attributen (Schlüssel-Wert-Paare) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERLATESTSTATECUSTOMATTRIBUTEVIEWSHARED-Schema" }

{% alert note %}
Diese Ansicht verwendet den Typ `OBJECT` für `CUSTOM_ATTRIBUTES` anstelle von `VARIANT`. Verwenden Sie dieselbe JSON-Zugriffssyntax (`:attribute_name::TYPE`), um einzelne Attribute abzufragen.
{% endalert %}

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

| Spaltenname     | Datentyp     | Beschreibung |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Ihr Braze-Workspace-Bezeichner |
| `USER_ID` | VARCHAR | Der eindeutige Braze-Nutzerbezeichner |
| `APP_ID` | VARCHAR | Die spezifische App innerhalb Ihres Workspace |
| `TIME` | NUMBER | Unix-Zeitstempel (Sekunden) des Profil-Updates |
| `TIME_MS` | NUMBER | Unix-Zeitstempel (Millisekunden) des Profil-Updates |
| `UPDATE_SOURCE` | VARCHAR | Die Quelle des Attribut-Updates (API, SDK, Dashboard usw.) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Wann die Daten zuletzt in Snowflake aktualisiert wurden |
| `EXTERNAL_USER_ID` | VARCHAR | Ihr eigener Nutzerbezeichner (falls gesetzt) |
| `FIRST_NAME` | VARCHAR | Vorname der:des Nutzer:in |
| `LAST_NAME` | VARCHAR | Nachname der:des Nutzer:in |
| `EMAIL_ADDRESS` | VARCHAR | E-Mail-Adresse der:des Nutzer:in |
| `GENDER` | VARCHAR | Geschlecht der:des Nutzer:in |
| `PHONE_NUMBER` | VARCHAR | Telefonnummer der:des Nutzer:in |
| `DOB` | VARCHAR | Geburtsdatum der:des Nutzer:in |
| `TIME_ZONE` | VARCHAR | Zeitzone der:des Nutzer:in |
| `HOME_CITY` | VARCHAR | Wohnort der:des Nutzer:in |
| `COUNTRY` | VARCHAR | Land der:des Nutzer:in |
| `LANGUAGE` | VARCHAR | Sprachpräferenz der:des Nutzer:in |
| `EFF_DT` | TIMESTAMP_NTZ | Gültigkeitsdatum: Wann dieser Attribut-Status begann |
| `END_DT` | TIMESTAMP_NTZ | Enddatum: Wann dieser Attribut-Status endete (NULL für den aktuellen Status) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERDEFAULTATTRIBUTESHISTORYVIEWSHARED-Schema" }

### `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`-Schema

| Spaltenname     | Datentyp     | Beschreibung |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Ihr Braze-Workspace-Bezeichner |
| `USER_ID` | VARCHAR | Der eindeutige Braze-Nutzerbezeichner |
| `APP_ID` | VARCHAR | Die spezifische App innerhalb Ihres Workspace |
| `EXTERNAL_USER_ID` | VARCHAR | Ihr eigener Nutzerbezeichner (falls gesetzt) |
| `TIME` | NUMBER | Unix-Zeitstempel (Sekunden) des Profil-Updates |
| `TIME_MS` | NUMBER | Unix-Zeitstempel (Millisekunden) des Profil-Updates |
| `UPDATE_SOURCE` | VARCHAR | Die Quelle des Attribut-Updates (API, SDK, Dashboard usw.) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Wann die Daten zuletzt in Snowflake aktualisiert wurden |
| `CUSTOM_ATTRIBUTES` | VARIANT | JSON-Objekt mit allen angepassten Attributen (Schlüssel-Wert-Paare) |
| `ARCHIVED` | BOOLEAN | Ob das Nutzerprofil archiviert ist |
| `EFF_DT` | TIMESTAMP_NTZ | Gültigkeitsdatum: Wann dieser Attribut-Status begann |
| `END_DT` | TIMESTAMP_NTZ | Enddatum: Wann dieser Attribut-Status endete (NULL für den aktuellen Status) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERCUSTOMATTRIBUTESHISTORYVIEWSHARED-Schema" }

## Häufige Anwendungsfälle {#common-use-cases}

### Nutzersegmente erstellen {#building-user-segments}

```sql
-- Find active users in a specific city who haven't received an email recently
SELECT
  d.EXTERNAL_USER_ID,
  d.EMAIL_ADDRESS,
  d.HOME_CITY,
  c.CUSTOM_ATTRIBUTES:last_email_sent::TIMESTAMP as last_email_sent
FROM USER_DEFAULT_ATTRIBUTES_VIEW_SHARED d
JOIN USER_CUSTOM_ATTRIBUTES_VIEW_SHARED c
  ON d.USER_ID = c.USER_ID
WHERE d.HOME_CITY = 'New York'
  AND d.EMAIL_ADDRESS IS NOT NULL
  AND (c.CUSTOM_ATTRIBUTES:last_email_sent::TIMESTAMP < DATEADD(day, -30, CURRENT_TIMESTAMP())
       OR c.CUSTOM_ATTRIBUTES:last_email_sent IS NULL);
```

### Nutzerverhalten im Zeitverlauf analysieren {#analyzing-user-behavior-over-time}

```sql
-- Track how a user's loyalty tier changed over the past 6 months
SELECT
  USER_ID,
  CUSTOM_ATTRIBUTES:loyalty_tier::STRING as loyalty_tier,
  EFF_DT,
  END_DT
FROM USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED
WHERE USER_ID = 'user_123'
  AND EFF_DT >= DATEADD(month, -6, CURRENT_TIMESTAMP())
ORDER BY EFF_DT DESC;
```

### Standard- und angepasste Attribute kombinieren {#combining-default-and-custom-attributes}

```sql
-- Get a complete user profile with both default and custom attributes
SELECT
  d.EXTERNAL_USER_ID,
  d.FIRST_NAME,
  d.LAST_NAME,
  d.EMAIL_ADDRESS,
  d.COUNTRY,
  c.CUSTOM_ATTRIBUTES:subscription_status::STRING as subscription_status,
  c.CUSTOM_ATTRIBUTES:lifetime_value::NUMBER as lifetime_value,
  c.CUSTOM_ATTRIBUTES:last_purchase_date::DATE as last_purchase_date
FROM USER_DEFAULT_ATTRIBUTES_VIEW_SHARED d
LEFT JOIN USER_CUSTOM_ATTRIBUTES_VIEW_SHARED c
  ON d.USER_ID = c.USER_ID
WHERE d.EXTERNAL_USER_ID = 'customer_456';
```

### Hochwertige Kund:innen finden {#finding-high-value-customers}

```sql
-- Identify users with high lifetime value who are at risk of churning
SELECT
  d.EXTERNAL_USER_ID,
  d.EMAIL_ADDRESS,
  c.CUSTOM_ATTRIBUTES:lifetime_value::NUMBER as lifetime_value,
  c.CUSTOM_ATTRIBUTES:days_since_last_purchase::NUMBER as days_since_last_purchase
FROM USER_DEFAULT_ATTRIBUTES_VIEW_SHARED d
JOIN USER_CUSTOM_ATTRIBUTES_VIEW_SHARED c
  ON d.USER_ID = c.USER_ID
WHERE c.CUSTOM_ATTRIBUTES:lifetime_value::NUMBER > 1000
  AND c.CUSTOM_ATTRIBUTES:days_since_last_purchase::NUMBER > 90
ORDER BY c.CUSTOM_ATTRIBUTES:lifetime_value::NUMBER DESC;
```

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
* Abfragen auf `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` oder `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` für einzelne Nutzer:innen kommen in unter einer Minute zurück, skalieren aber schlecht ohne `USER_ID`-Filterung.
* Abfragen bei über 100 Millionen Nutzer:innen auf `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` oder `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` können aufgrund der Aggregation pro Nutzer:in mehrere Minuten dauern.