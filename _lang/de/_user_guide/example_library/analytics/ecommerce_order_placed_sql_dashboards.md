---
nav_title: SQL-Dashboards für aufgegebene Bestellungen
article_title: Berichte zu E-Commerce-Order-Placed-Events im Dashboard Builder
page_order: 1
page_type: reference
description: "Verwenden Sie Query Builder SQL für ecommerce.order_placed-Events, um Umsatz- und Bestell-Tiles im Dashboard Builder für E-Commerce-Berichte zu erstellen."
tool: Reports
---

# Berichte zu E-Commerce-Order-Placed-Events im Dashboard Builder {#report-on-ecommerce-order-placed-events-in-dashboard-builder}

> Erstellen Sie angepasste Umsatz- und Bestell-Charts aus empfohlenen `ecommerce.order_placed`-Events, indem Sie SQL-Anfragen im Query Builder speichern und die Ergebnisse im Dashboard Builder visualisieren.

## Über dieses Beispiel {#about-this-example}

Flash und Thread, eine fiktive Einzelhandelsmarke für Bekleidung, erfasst Bestellungen mit [empfohlenen E-Commerce-Events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events). Das Marketing-Team möchte täglichen Umsatz, den durchschnittlichen Bestellwert (AOV) und das Bestellvolumen in einem einzigen Dashboard sehen – nicht nur die vorgefertigte Last-Touch-Attribution-Ansicht.

Dieses Muster verwendet den Query Builder, um `ecommerce.order_placed` aus den gemeinsam genutzten Snowflake-Event-Tabellen abzufragen, und fügt die gespeicherte Anfrage dann als **Custom Queries**-Tile im Dashboard Builder hinzu. Sie können den Workflow für zusätzliche Metriken wiederholen (neue vs. wiederkehrende Käufer:innen, Produktkategorien oder Umsatz auf Segment-Ebene).

Verwenden Sie dieses Vorgehen, wenn die integrierten E-Commerce-Dashboards Ihren Metrik-Mix nicht abdecken. Für Last-Touch-attributierten Umsatz siehe stattdessen das Dashboard [Revenue - Last Touch Attribution]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder#revenue---last-touch-attribution).

## Hinweise {#considerations}

- **Event-Implementierung:** `ecommerce.order_placed` muss implementiert sein und `total_value` (sowie Produktdaten bei Bedarf) senden, bevor Anfragen Daten zurückgeben. Wenn Sie den [Shopify-Konnektor]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector) verwenden, sind empfohlene Events möglicherweise bereits verfügbar.
- **Query-Builder-Zugriff:** Sie benötigen die Nutzer:innenberechtigung „View PII“ ([Nutzer:innenverwaltung]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)), um den Query Builder zu verwenden.
- **Datenaufbewahrung:** Der Query Builder gibt standardmäßig Daten der letzten 60 Tage zurück. Mit [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake) können Sie bis zu zwei Jahre aufbewahrte Daten abfragen. Siehe [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder).
- **Timeouts:** Anfragen, die länger als sechs Minuten laufen, werden abgebrochen. Schränken Sie den Datumsbereich ein, filtern Sie nach `TIME` oder reduzieren Sie die Zielgruppengröße, wenn ein Bericht fehlschlägt. Event-Tabellen sind nach `TIME` geclustert; filtern Sie bevorzugt nach dem Zeitpunkt des Events.
- **Umsatzfeld:** Die Beispielabfragen summieren `total_value` aus den Event-`properties`. Der standardisierte E-Commerce-Umsatz von Braze in Produktberichten leitet sich häufig aus `price` und `quantity` jedes Produkts ab. Stimmen Sie `total_value` mit Ihren Produktpositionen ab oder passen Sie das SQL an Ihr Schema an.
- **Spaltenbezeichnungen:** Setzen Sie Anzeige-Spaltennamen in doppelte Anführungszeichen (zum Beispiel `"Date"`, `"Total Revenue"`), damit der Dashboard Builder lesbare Achsen- und Tabellenüberschriften anzeigt.
- **Testen:** Das SQL in diesem Artikel dient als Beispiel. Validieren Sie Anfragen in Ihrem Workspace, bevor Sie Dashboards breit teilen.

## Einrichtung {#setup}

### Schritt 1: SQL-Anfrage für den täglichen Umsatz erstellen {#step-1-create-a-sql-query-for-daily-revenue}

1. Gehen Sie zu **Analytics** > **Query Builder**.
2. Wählen Sie **Create SQL Query** und dann **SQL Editor**.
3. Benennen Sie die Anfrage (zum Beispiel `Flash Thread — daily eCommerce revenue`).
4. Fügen Sie die folgende Anfrage ein und passen Sie sie an, um den Gesamtumsatz pro Kalendertag der letzten 60 Tage zu erhalten:

{% raw %}
```sql
SELECT
  DATE_TRUNC('day', TO_TIMESTAMP_NTZ(TIME))::DATE AS "Date",
  SUM(PARSE_JSON(PROPERTIES):total_value::NUMBER(18, 2)) AS "Total Revenue"
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED
WHERE NAME = 'ecommerce.order_placed'
  AND TO_TIMESTAMP_NTZ(TIME) >= DATEADD(day, -60, CURRENT_TIMESTAMP())
  AND TO_TIMESTAMP_NTZ(TIME) <= CURRENT_TIMESTAMP()
GROUP BY 1
ORDER BY 1;
```
{% endraw %}

{:start="5"}
5. Wählen Sie **Run Query** und dann **Save**.

Details zur Einrichtung des Query Builders finden Sie unter [Berichte im Query Builder ausführen]({{site.baseurl}}/user_guide/analytics/reports/query_builder#running-reports-in-the-query-builder).

### Schritt 2: Anfrage als Dashboard-Builder-Tile hinzufügen {#step-2-add-the-query-to-a-dashboard-builder-tile}

1. Gehen Sie zu **Analytics** > **Dashboard Builder**.
2. Wählen Sie **Create Dashboard** (oder öffnen Sie ein bestehendes Dashboard).
3. Wählen Sie als Datenquelle **Custom Queries**.
4. Wählen Sie **+ Add Tile** und dann die in Schritt 1 gespeicherte Anfrage.
5. Wählen Sie das Stiftsymbol, um das Tile zu bearbeiten:
   - Setzen Sie den Chart-Typ auf **Line graph**.
   - Setzen Sie die **X-Achse** auf `Date`.
   - Setzen Sie die **Y-Achse** auf `Total Revenue`.
6. Passen Sie die Größe des Tiles nach Bedarf an und wählen Sie **Save**.
7. Wählen Sie **View Dashboard** > **Run Dashboard**.

Die Dashboard-Erstellung kann einige Minuten dauern. Siehe [Ein angepasstes Dashboard erstellen]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder#creating-a-custom-dashboard).

### Schritt 3: Zusätzliche _Order Placed_-Metriken hinzufügen (optional) {#step-3-add-additional-_order-placed_-metrics-optional}

Erstellen Sie separate gespeicherte Anfragen und fügen Sie jede als eigenes Tile hinzu (bis zu 10 Tiles pro Dashboard).

#### Durchschnittlicher Bestellwert und Bestellanzahl pro Tag {#average-order-value-and-order-count-per-day}

{% raw %}
```sql
SELECT
  DATE_TRUNC('day', TO_TIMESTAMP_NTZ(TIME))::DATE AS "Date",
  AVG(PARSE_JSON(PROPERTIES):total_value::NUMBER(18, 2)) AS "Average Order Value",
  COUNT(*) AS "No. of Orders"
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED
WHERE NAME = 'ecommerce.order_placed'
  AND TO_TIMESTAMP_NTZ(TIME) >= DATEADD(day, -60, CURRENT_TIMESTAMP())
  AND TO_TIMESTAMP_NTZ(TIME) <= CURRENT_TIMESTAMP()
GROUP BY 1
ORDER BY 1;
```
{% endraw %}

Verwenden Sie ein Linien- oder Balkendiagramm mit `Date` auf der X-Achse und beiden Metriken auf der Y-Achse (deaktivieren Sie Spalten, die Sie nicht anzeigen möchten).

#### Neue vs. wiederkehrende Käufer:innen pro Tag {#new-versus-returning-purchasers-per-day}

Dieses Muster vergleicht den ersten `ecommerce.order_placed`-Tag jeder Nutzer:in mit späteren Kauftagen. Es ist am genauesten, wenn Ihr Query-Builder-Fenster den gesamten Berichtszeitraum abdeckt (zum Beispiel das standardmäßige 60-Tage-Fenster).

{% raw %}
```sql
WITH order_days AS (
  SELECT DISTINCT
    USER_ID,
    DATE_TRUNC('day', TO_TIMESTAMP_NTZ(TIME))::DATE AS purchase_day
  FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED
  WHERE NAME = 'ecommerce.order_placed'
),
first_purchase AS (
  SELECT
    USER_ID,
    MIN(purchase_day) AS first_day
  FROM order_days
  GROUP BY USER_ID
),
per_day_purchasers AS (
  SELECT DISTINCT
    USER_ID,
    purchase_day
  FROM order_days
)
SELECT
  p.purchase_day AS "Date",
  COUNT(DISTINCT CASE
    WHEN f.first_day = p.purchase_day THEN p.USER_ID
  END) AS "New Purchasers",
  COUNT(DISTINCT CASE
    WHEN f.first_day < p.purchase_day THEN p.USER_ID
  END) AS "Returning Purchasers"
FROM per_day_purchasers AS p
INNER JOIN first_purchase AS f
  ON p.USER_ID = f.USER_ID
GROUP BY 1
ORDER BY 1;
```
{% endraw %}

#### Produktkategorie aus Bestellpositionen {#product-category-from-order-line-items}

Entfalten Sie das `products`-Array und filtern Sie nach Ihrem Kategoriefeld. Ersetzen Sie `metadata.category`, wenn Sie einen anderen Produkt-Metadaten-Schlüssel verwenden.

{% raw %}
```sql
SELECT
  f.value:metadata:category::STRING AS "Product Category",
  COUNT(*) AS "Line Items"
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED,
  LATERAL FLATTEN(INPUT => PARSE_JSON(PROPERTIES):products) f
WHERE NAME = 'ecommerce.order_placed'
  AND f.value:metadata:category::STRING IS NOT NULL
  AND TRIM(f.value:metadata:category::STRING) != ''
  AND LOWER(TRIM(f.value:metadata:category::STRING)) != 'undefined'
GROUP BY 1
ORDER BY 2 DESC;
```
{% endraw %}

#### Käufe und Umsatz nach Segment (Segment-Analytics) {#purchases-and-revenue-by-segment-segment-analytics}

Dies erfordert [Segment-Analytics-Tracking]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking) für die Segmente, über die Sie berichten. Verwenden Sie [SQL-Variablen]({{site.baseurl}}/user_guide/analytics/reports/query_builder/sql_variables) für Datumsauswahlen.

{% raw %}
```sql
WITH event_conversions AS (
  SELECT
    user_id,
    time,
    TRY_CAST(GET_PATH(PARSE_JSON(PROPERTIES), 'total_value')::string AS FLOAT) AS price,
    id AS purchase_event_id,
    f.value::string AS user_segment_membership_id
  FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED,
    LATERAL FLATTEN(input => user_segment_membership_ids) AS f
  WHERE NAME = 'ecommerce.order_placed'
    AND time > {{start_date.${Start Date}}}
    AND time < {{end_date.${End Date}}}
)
SELECT
  user_segment_membership_id AS "Segment Analytics Id",
  COUNT(DISTINCT purchase_event_id) AS "Total Purchases",
  ROUND(SUM(price), 2) AS "Total Revenue"
FROM event_conversions
GROUP BY 1
ORDER BY 3 DESC;
```
{% endraw %}

### Weitere integrierte E-Commerce-Berichte {#other-built-in-ecommerce-reporting}

| Bericht | Verwendung |
| --- | --- |
| [Revenue - Last Touch Attribution]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder#revenue---last-touch-attribution) | Last-Touch-attributierter Umsatz nach Campaign oder Canvas |
| [Bericht zu angepassten Events]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report) | Event-Volumen und -Häufigkeit für empfohlene Events |
| Campaign- oder Canvas-Konversionen | `ecommerce.order_placed` ist das primäre Konversions-Event |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Weitere integrierte E-Commerce-Berichte" }

## Verwandte Artikel {#related-articles}

- [Empfohlene E-Commerce-Events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events)
- [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder)
- [SQL-Variablen im Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder/sql_variables)
- [Dashboard Builder]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder)
- [Revenue - Last Touch Attribution]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder#revenue---last-touch-attribution)
- [SQL-Tabellenreferenz]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#USERS_BEHAVIORS_CUSTOMEVENT_SHARED)
- [Segment-Analytics-Tracking]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking)