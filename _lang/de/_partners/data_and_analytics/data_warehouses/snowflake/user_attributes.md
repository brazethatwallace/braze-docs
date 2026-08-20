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

In seltenen Fällen können die Werte von Standard- und angepassten Attributen in den Snowflake-Views auf dieser Seite von dem abweichen, was Sie im Nutzerprofil im Braze-Dashboard sehen.

Beispielsweise kann ein Attribut in Snowflake als `NULL` erscheinen, während das Dashboard einen Wert für diese:n Nutzer:in anzeigt.

Wenn Sie weitverbreitete Abweichungen feststellen, wenden Sie sich an Ihre:n Customer-Success-Manager:in oder den Braze-Support.

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
      <td>Snapshots von Nutzerprofilen</td>
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
      <td>Snapshots von Nutzerprofilen</td>
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

## Snapshots von Nutzerprofilen {#user-profile-snapshots}

Diese Views bieten periodische Snapshots von Nutzerprofilattributen. Die Daten haben eine Verzögerung von bis zu 12 Stunden, was sie für Abfragen nützlich macht, die keine Realtime-Aktualisierungen erfordern.

 - `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`
 - `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`

### Verwendung {#usage}

* Bietet einen Snapshot von Nutzerattributen mit einer Verzögerung von bis zu **12 Stunden**.
* Eignet sich gut für Abfragen, die keine Realtime-Genauigkeit erfordern.
* Schnellere Abfrageausführung, insbesondere beim Filtern nach anderen Attributen als `USER_ID`.
* **Einschränkung:** Die Daten sind nicht in Echtzeit aktuell.

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`-Schema

| Spaltenname     | Datentyp     | Beschreibung |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Ihr Braze-Workspace-Bezeichner |
| `APP_ID` | VARCHAR | Die spezifische App innerhalb Ihres Workspace |
| `USER_ID` | VARCHAR | Der eindeutige Braze-Nutzerbezeichner |
| `TIME` | NUMBER | Unix-Zeitstempel (Sekunden) der Profilaktualisierung |
| `TIME_MS` | NUMBER | Unix-Zeitstempel (Millisekunden) der Profilaktualisierung |
| `UPDATE_SOURCE` | VARCHAR | Die Quelle der Attributaktualisierung (API, SDK, Dashboard usw.) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Wann die Daten zuletzt in Snowflake aktualisiert wurden |
| `EXTERNAL_USER_ID` | VARCHAR | Ihr eigener Nutzerbezeichner (falls festgelegt) |
| `FIRST_NAME` | VARCHAR | Vorname der Nutzerin bzw. des Nutzers |
| `LAST_NAME` | VARCHAR | Nachname der Nutzerin bzw. des Nutzers |
| `EMAIL_ADDRESS` | VARCHAR | E-Mail-Adresse der Nutzerin bzw. des Nutzers |
| `GENDER` | VARCHAR | Geschlecht der Nutzerin bzw. des Nutzers |
| `PHONE_NUMBER` | VARCHAR | Telefonnummer der Nutzerin bzw. des Nutzers |
| `DOB` | VARCHAR | Geburtsdatum der Nutzerin bzw. des Nutzers |
| `TIME_ZONE` | VARCHAR | Zeitzone der Nutzerin bzw. des Nutzers |
| `HOME_CITY` | VARCHAR | Heimatort der Nutzerin bzw. des Nutzers |
| `COUNTRY` | VARCHAR | Land der Nutzerin bzw. des Nutzers |
| `LANGUAGE` | VARCHAR | Sprachpräferenz der Nutzerin bzw. des Nutzers |
| `ARCHIVED` | BOOLEAN | Ob das Nutzerprofil archiviert ist |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERDEFAULTATTRIBUTESVIEWSHARED-Schema" }


### `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`-Schema

| Spaltenname     | Datentyp     | Beschreibung |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Ihr Braze-Workspace-Bezeichner |
| `APP_ID` | VARCHAR | Die spezifische App innerhalb Ihres Workspace |
| `USER_ID` | VARCHAR | Der eindeutige Braze-Nutzerbezeichner |
| `EXTERNAL_USER_ID` | VARCHAR | Ihr eigener Nutzerbezeichner (falls festgelegt) |
| `TIME` | NUMBER | Unix-Zeitstempel (Sekunden) der Profilaktualisierung |
| `TIME_MS` | NUMBER | Unix-Zeitstempel (Millisekunden) der Profilaktualisierung |
| `UPDATE_SOURCE` | VARCHAR | Die Quelle der Attributaktualisierung (API, SDK, Dashboard usw.) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Wann die Daten zuletzt in Snowflake aktualisiert wurden |
| `CUSTOM_ATTRIBUTES` | VARIANT | JSON-Objekt mit allen angepassten Attributen (Schlüssel-Wert-Paare) |
| `ARCHIVED` | BOOLEAN | Ob das Nutzerprofil archiviert ist |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERCUSTOMATTRIBUTESVIEWSHARED-Schema" }

#### Arbeiten mit CUSTOM_ATTRIBUTES {#working-with-custom_attributes}

Die Spalte `CUSTOM_ATTRIBUTES` speichert alle Ihre angepassten Attribute als JSON-Objekt. Sie können auf einzelne Attribute über die JSON-Funktionen von Snowflake zugreifen.

**Beispiel: Abfrage bestimmter angepasster Attribute**

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

**Beispiel: Analyse von Daten angepasster Attribute**

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

## Realtime-Nutzerprofilansichten {#real-time-user-profile-views}

Diese Ansichten bieten nahezu Realtime-Aktualisierungen von Nutzerprofilattributen, wobei die Daten nach einer Aktualisierung in Braze um bis zu 10 Minuten verzögert sein können.

  - `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`
  - `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`

### Verwendung

* Bietet aktuelle Nutzerattribute mit minimaler Verzögerung (~10 Minuten).
* Nützlich für Realtime-Analysen und Szenarien, in denen aktuelle Daten erforderlich sind.
* **Überlegungen zur Performance:**
    * Abfragen für einzelne Nutzer:innen sind schneller (unter einer Minute bei Verwendung eines großen Warehouse).
    * Abfragen ohne USER_ID-Filter erfordern eine Aggregation über alle Nutzer:innen, was zu deutlich längeren Ausführungszeiten führt.
    * Abfragen auf einem großen Datensatz (z. B. über 100 Millionen Nutzer:innen) können viele Minuten dauern.

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`-Schema

| Spaltenname     | Datentyp     | Beschreibung |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Ihr Braze-Workspace-Bezeichner |
| `APP_ID` | VARCHAR | Die spezifische App innerhalb Ihres Workspace |
| `USER_ID` | VARCHAR | Der eindeutige Braze-Nutzerbezeichner |
| `TIME` | NUMBER | Unix-Zeitstempel (Sekunden) der Profilaktualisierung |
| `TIME_MS` | NUMBER | Unix-Zeitstempel (Millisekunden) der Profilaktualisierung |
| `UPDATE_SOURCE` | VARCHAR | Die Quelle der Attributaktualisierung (API, SDK, Dashboard usw.) |
| `ARCHIVED` | BOOLEAN | Ob das Nutzerprofil archiviert ist |
| `SF_UPDATED_AT` | TIMESTAMP_LTZ | Wann die Daten zuletzt in Snowflake aktualisiert wurden |
| `EXTERNAL_USER_ID` | VARCHAR | Ihr eigener Nutzerbezeichner (falls festgelegt) |
| `FIRST_NAME` | VARCHAR | Vorname der/des Nutzer:in |
| `LAST_NAME` | VARCHAR | Nachname der/des Nutzer:in |
| `EMAIL_ADDRESS` | VARCHAR | E-Mail-Adresse der/des Nutzer:in |
| `GENDER` | VARCHAR | Geschlecht der/des Nutzer:in |
| `PHONE_NUMBER` | VARCHAR | Telefonnummer der/des Nutzer:in |
| `DOB` | VARCHAR | Geburtsdatum der/des Nutzer:in |
| `HOME_CITY` | VARCHAR | Wohnort der/des Nutzer:in |
| `COUNTRY` | VARCHAR | Land der/des Nutzer:in |
| `LANGUAGE` | VARCHAR | Sprachpräferenz der/des Nutzer:in |
| `TIME_ZONE` | VARCHAR | Zeitzone der/des Nutzer:in |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schema für USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED" }

### `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`-Schema

{% include partners/snowflake_user_attributes_custom_view_schemas.md schema="latest" %}

## Historische Änderungsprotokolle {#historical-change-logs}

Diese Ansichten speichern historische Änderungsprotokolle von Nutzerattributen und erfassen Änderungen mit einer 12-Stunden-Granularität.

- `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`
- `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`

### Verwendung

* Bietet eine Aufzeichnung historischer Änderungen an Nutzerattributen für einen rollierenden Zeitraum von 6 Monaten.
* Daten werden alle 12 Stunden als Snapshot erfasst, was bedeutet, dass mehrere Aktualisierungen in diesem Zeitfenster zu einem einzigen Datensatz zusammengefasst werden. Einzelne Änderungen innerhalb dieses Zeitraums werden nicht separat aufbewahrt.
* `EFF_DT` und `END_DT` markieren den Beginn und das Ende eines Attributzustands der Nutzer:innen.

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`-Schema

| Spaltenname     | Datentyp     | Beschreibung |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Ihr Braze-Workspace-Bezeichner |
| `USER_ID` | VARCHAR | Der eindeutige Braze-Nutzerbezeichner |
| `APP_ID` | VARCHAR | Die spezifische App innerhalb Ihres Workspace |
| `TIME` | NUMBER | Unix-Zeitstempel (Sekunden) der Profilaktualisierung |
| `TIME_MS` | NUMBER | Unix-Zeitstempel (Millisekunden) der Profilaktualisierung |
| `UPDATE_SOURCE` | VARCHAR | Die Quelle der Attributaktualisierung (API, SDK, Dashboard usw.) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Wann die Daten zuletzt in Snowflake aktualisiert wurden |
| `EXTERNAL_USER_ID` | VARCHAR | Ihr eigener Nutzerbezeichner (falls festgelegt) |
| `FIRST_NAME` | VARCHAR | Vorname der Nutzer:innen |
| `LAST_NAME` | VARCHAR | Nachname der Nutzer:innen |
| `EMAIL_ADDRESS` | VARCHAR | E-Mail-Adresse der Nutzer:innen |
| `GENDER` | VARCHAR | Geschlecht der Nutzer:innen |
| `PHONE_NUMBER` | VARCHAR | Telefonnummer der Nutzer:innen |
| `DOB` | VARCHAR | Geburtsdatum der Nutzer:innen |
| `TIME_ZONE` | VARCHAR | Zeitzone der Nutzer:innen |
| `HOME_CITY` | VARCHAR | Wohnort der Nutzer:innen |
| `COUNTRY` | VARCHAR | Land der Nutzer:innen |
| `LANGUAGE` | VARCHAR | Sprachpräferenz der Nutzer:innen |
| `EFF_DT` | TIMESTAMP_NTZ | Gültigkeitsdatum: wann dieser Attributzustand begann |
| `END_DT` | TIMESTAMP_NTZ | Enddatum: wann dieser Attributzustand endete (NULL für den aktuellen Zustand) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERDEFAULTATTRIBUTESHISTORYVIEWSHARED-Schema" }

### `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`-Schema

{% include partners/snowflake_user_attributes_custom_view_schemas.md schema="history" %}

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

### Hochwertige Kund:innen identifizieren {#finding-high-value-customers}

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

### Empfohlene Abfragenutzung {#recommended-query-usage}

| Anwendungsfall                                          | Empfohlene Views                                   | Hinweise                                                              |
|--------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------|
| **Allgemeine Abfragen**, die keine aktuellen Updates erfordern | `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` und `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`               | Schnelle Ausführung, mit Daten, die bis zu 12 Stunden alt sein können.                          |
| Abfragen, die die **neuesten Nutzerattribute** erfordern       | `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` und `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` | Bietet nahezu Realtime-Updates, kann aber bei großen Datensätzen langsamer sein. |
| **Historisches Tracking** von Attributänderungen           | `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` und `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`      | Speichert Attributänderungen mit einer Granularität von 12 Stunden.                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Empfohlene Abfragenutzung" }

### Performance-Überlegungen {#performance-considerations}

* Abfragen auf `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` oder `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` sollten bei großen Datensätzen (~1 Milliarde Nutzer:innen) auf einem großen Warehouse in unter 10 Sekunden zurückkehren.
* Abfragen auf `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` oder `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED ` für einzelne Nutzer:innen werden in unter einer Minute zurückgegeben, skalieren aber ohne `USER_ID`-Filterung schlecht.
* Abfragen über mehr als 100 Millionen Nutzer:innen in `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` oder `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` können aufgrund der Aggregation pro Nutzer:in mehrere Minuten dauern.