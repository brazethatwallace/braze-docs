---
nav_title: Abfrage-Builder
article_title: Abfrage-Builder
page_order: 4
description: "Dieser Referenzartikel beschreibt, wie Sie mit dem Abfrage-Builder Berichte aus Braze-Daten in Snowflake erstellen."
tool: Reports
alias: /query_builder/
---

# Abfrage-Builder {#query-builder}

> Der Abfrage-Builder erstellt Berichte aus Braze-Daten in Snowflake. Der Abfrage-Builder enthält vorgefertigte SQL-[Abfrage-Templates]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates), die Ihnen den Einstieg erleichtern, oder Sie schreiben eigene SQL-Anfragen, um noch mehr Insights zu gewinnen.

Da der Abfrage-Builder direkten Zugriff auf bestimmte Kundendaten ermöglicht, können Sie ihn nur nutzen, wenn Sie die [Berechtigung]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) „PII anzeigen“ besitzen.

## Verfügbare Datentabellen {#available-data-tables}

Der Abfrage-Builder verwendet dieselben Snowflake-SQL-Tabellen wie [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) und die [Snowflake-Datenfreigabe]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake). Eine vollständige Liste der verfügbaren Tabellen und ihrer Spalten finden Sie in der [SQL-Tabellenreferenz]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables).

## Berichte im Abfrage-Builder ausführen {#running-reports-in-the-query-builder}

So führen Sie einen Bericht im Abfrage-Builder aus:

1. Gehen Sie zu **Analytics** > **Query Builder**.
2. Wählen Sie **Create SQL Query**. Wenn Sie Inspiration oder Hilfe beim Erstellen Ihrer Abfrage benötigen, wählen Sie **Query Template** und wählen Sie eine Vorlage aus der Liste. Andernfalls wählen Sie **SQL Editor**, um direkt zum Editor zu gelangen.
3. Ihr Bericht erhält automatisch einen Namen mit dem aktuellen Datum und der Uhrzeit. Bewegen Sie den Mauszeiger über den Namen und wählen Sie <i class="fas fa-pencil" alt="Bearbeiten"></i>, um Ihrer SQL-Abfrage einen aussagekräftigen Namen zu geben.
4. Schreiben Sie Ihre SQL-Abfrage im Editor oder [lassen Sie sich von KI helfen](#ai-query-builder) über den Tab **AI Query Builder**. Wenn Sie eigenes SQL schreiben, lesen Sie [Eigene SQL-Anfragen schreiben](#custom-sql) für Anforderungen und Ressourcen.
5. Wählen Sie **Run Query**.
6. Speichern Sie Ihre Abfrage.
7. Um eine CSV-Datei Ihres Berichts herunterzuladen, wählen Sie **Export**.

![Abfrage-Builder mit den Ergebnissen der Vorlagenabfrage „Kanal-Engagement und Umsatz der letzten 30 Tage“.]({% image_buster /assets/img_archive/query_builder.png %})

Ergebnisse jedes Berichts können einmal pro Tag generiert werden. Wenn Sie denselben Bericht mehr als einmal an einem Kalendertag ausführen, sehen Sie in beiden Berichten dieselben Ergebnisse.

### Abfrage-Templates {#query-templates}

Greifen Sie auf Abfrage-Templates zu, indem Sie beim Erstellen eines Berichts **Create SQL Query** > **Query Template** wählen.

Eine Liste der verfügbaren Templates finden Sie unter [Abfrage-Templates]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates).

### Datenzeitraum {#data-timeframe}

Abfragen liefern Daten der letzten 60 Tage. Wenn Sie Currents oder die [Snowflake-Datenfreigabe]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake) nutzen, können Sie möglicherweise Daten von bis zu zwei Jahren abfragen – so lange werden Ihre Daten in Snowflake aufbewahrt. Für weitere Details zur erweiterten Datenaufbewahrung wenden Sie sich an Ihren Customer-Success-Manager.

### Zeitzone des Abfrage-Builders {#query-builder-time-zone}

Die Standardzeitzone für Abfragen an unsere Snowflake-Datenbank ist UTC. Daher kann es zu Datenabweichungen zwischen Ihrer Seite **Email Channel Engagement** (die der Zeitzone Ihres Unternehmens folgt) und Ihren Ergebnissen im Abfrage-Builder kommen.

Um die Zeitzone in Ihren Abfrageergebnissen umzurechnen, fügen Sie das folgende SQL zu Ihrer Abfrage hinzu und passen Sie es an die Zeitzone Ihres Unternehmens an:

{% raw %}
```sql
SELECT
DATE_TRUNC(
'day',
CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME))
) AS send_date_sydney,
COUNT(ID) AS emails_sent
USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE
-- Apply the date range in Sydney time as well
CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME)) >= '2025-03-25 00:00:00'
AND CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME)) < '2025-03-29 00:00:00'
AND APP_GROUP_ID = 'your app group ID'
GROUP BY
send_date_sydney
ORDER BY
send_date_sydney;
```
{% endraw %}

### Abfrageverlauf {#query-history}

Der Abschnitt **Query history** im Abfrage-Builder zeigt Ihre zuvor ausgeführten Abfragen an, damit Sie Ihre Arbeit nachverfolgen und wiederverwenden können. Der Abfrageverlauf wird sieben Tage lang aufbewahrt, d. h. Abfragen, die älter als sieben Tage sind, werden automatisch entfernt.

Wenn Sie die Abfragenutzung über längere Zeiträume prüfen oder Aufzeichnungen über sieben Tage hinaus aufbewahren müssen, empfehlen wir, wichtige Abfrageergebnisse zu exportieren oder zu speichern, bevor sie ablaufen.

## SQL mit dem KI-Abfrage-Builder generieren {#ai-query-builder}

Der KI-Abfrage-Builder nutzt [GPT](https://openai.com/gpt-4), betrieben von OpenAI, um SQL für Ihre Abfrage vorzuschlagen.

![Der SQL-KI-Abfrage-Builder.]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

So generieren Sie SQL mit dem KI-Abfrage-Builder:

1. Nachdem Sie einen Bericht im Abfrage-Builder erstellt haben, wählen Sie den Tab **AI Query Builder**.
2. Geben Sie Ihren Prompt ein oder wählen Sie einen Beispiel-Prompt und wählen Sie **Generate**, um Ihren Prompt in SQL zu übersetzen.
3. Überprüfen Sie das generierte SQL, um sicherzustellen, dass es korrekt aussieht, und wählen Sie dann **Insert into Editor**.

### Tipps {#tips}

- Machen Sie sich mit den verfügbaren Tabellen und Spalten in der [SQL-Tabellenreferenz]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables) vertraut. Wenn Sie nach Daten fragen, die in diesen Tabellen nicht existieren, kann ChatGPT eine fiktive Tabelle erfinden.
- Machen Sie sich mit den [SQL-Schreibregeln]({{site.baseurl}}/user_guide/analytics/reports/query_builder#custom-sql) für dieses Feature vertraut. Die Nichteinhaltung dieser Regeln führt zu einem Fehler.
- Sie können mit dem KI-Abfrage-Builder bis zu 20 Prompts pro Minute senden.

#{% multi_lang_include brazeai/generative_ai/policy.md %}

## Eigene SQL-Anfragen schreiben {#custom-sql}

Schreiben Sie Ihre SQL-Abfrage mit der [Snowflake-Syntax](https://docs.snowflake.com/en/sql-reference). In der [Tabellenreferenz]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables) finden Sie eine vollständige Liste der Tabellen und Spalten, die abgefragt werden können.

So zeigen Sie Tabellendetails im Abfrage-Builder an:

1. Öffnen Sie auf der Seite **Query Builder** das Panel **Reference** und wählen Sie **Available Data Tables**, um die verfügbaren Datentabellen und ihre Namen anzuzeigen.
3. Wählen Sie <i class="fas fa-chevron-down" alt=""></i> **See Details**, um die Tabellenbeschreibung und Informationen zu den Tabellenspalten wie Datentypen anzuzeigen.
4. Um den Tabellennamen in Ihr SQL einzufügen, wählen Sie <i class="fas fa-copy" title="Tabellennamen in den SQL-Editor kopieren"></i> **Copy table name to SQL editor**.

Um von Braze bereitgestellte vorgefertigte Abfragen zu verwenden, wählen Sie **Query Template** beim Erstellen eines Berichts im Abfrage-Builder.

Wenn Sie Ihre Abfrage auf einen bestimmten Zeitraum beschränken, werden Ergebnisse schneller generiert. Das folgende Beispiel zeigt eine Abfrage, die die Anzahl der Käufe und den generierten Umsatz der letzten Stunde abruft.

```sql
SELECT COUNT(*) as Purchases, SUM(price) as Revenue
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('hour', -1, date_trunc('day',CURRENT_DATE()));
```

Diese Abfrage ruft die Anzahl der E-Mail-Versendungen im letzten Monat ab:

```sql
SELECT COUNT(*) as Sends
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('month', -1, date_trunc('day',CURRENT_DATE()));
```

Wenn Sie nach `CANVAS_ID`, `CANVAS_VARIATION_API_ID` oder `CAMPAIGN_ID` abfragen, werden die zugehörigen Namensspalten automatisch in die Ergebnistabelle aufgenommen. Sie müssen sie nicht in die `SELECT`-Abfrage selbst einschließen.

| ID-Name | Zugehörige Namensspalte |
| --- | --- |
| `CANVAS_ID` | Canvas Name |
| `CANVAS_VARIATION_API_ID` | Canvas Variant Name |
| `CAMPAIGN_ID` | Campaign Name |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eigene SQL-Anfragen schreiben" }

Diese Abfrage ruft alle drei IDs und ihre zugehörigen Namensspalten mit maximal 100 Zeilen ab:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
LIMIT 100
```

### Kampagnenvarianten-Name automatisch befüllen {#automatically-populate-the-campaign-variant-name}

Wenn der Kampagnenvarianten-Name automatisch befüllt werden soll, fügen Sie den Spaltennamen `MESSAGE_VARIATION_API_ID` in Ihre Abfrage ein, wie in diesem Beispiel:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID, MESSAGE_VARIATION_API_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
LIMIT 100
```

### Fehlerbehebung {#troubleshooting}

Ihre Abfrage kann aus folgenden Gründen fehlschlagen:

- Syntaxfehler in Ihrer SQL-Abfrage
- Verarbeitungs-Timeout (nach 6 Minuten)
    - Berichte, deren Ausführung länger als 6 Minuten dauert, werden abgebrochen.
    - Wenn ein Bericht ein Timeout hat, versuchen Sie, den Zeitraum der abgefragten Daten einzuschränken oder einen spezifischeren Datensatz abzufragen.

## Variablen verwenden {#using-variables}

Verwenden Sie Variablen, um vordefinierte Variablentypen in SQL zu nutzen und Werte zu referenzieren, ohne den Wert manuell kopieren zu müssen. Anstatt beispielsweise die ID einer Campaign manuell in den SQL-Editor zu kopieren, können Sie {% raw %}`{{campaign.${My campaign}}}`{% endraw %} verwenden, um eine Campaign direkt aus einem Dropdown im Tab **Variables** auszuwählen.

Nachdem eine Variable erstellt wurde, erscheint sie im Tab **Variables** Ihres Abfrage-Builder-Berichts. Vorteile der Verwendung von SQL-Variablen:

- Sparen Sie Zeit, indem Sie eine Campaign-Variable erstellen, aus der Sie beim Erstellen Ihres Berichts auswählen können, anstatt Campaign-IDs einzufügen.
- Tauschen Sie Werte aus, indem Sie Variablen hinzufügen, mit denen Sie den Bericht für leicht unterschiedliche Anwendungsfälle in der Zukunft wiederverwenden können (z. B. ein anderes angepasstes Event).
- Reduzieren Sie Nutzer:innenfehler beim Bearbeiten Ihres SQL, indem Sie den Bearbeitungsaufwand für jeden Bericht verringern. Teammitglieder, die sich mit SQL besser auskennen, können Berichte erstellen, die weniger technisch versierte Teammitglieder dann nutzen können.

### Richtlinien {#guidelines}

Variablen müssen der folgenden Liquid-Syntax entsprechen: {% raw %}`{{ type.${name}}}`{% endraw %}, wobei `type` einer der akzeptierten Typen sein muss und `name` frei wählbar ist. Die Bezeichnungen dieser Variablen entsprechen standardmäßig dem Variablennamen.

Standardmäßig sind alle Variablen Pflichtfelder (und Ihr Bericht wird nicht ausgeführt, wenn keine Variablenwerte ausgewählt sind), mit Ausnahme des Datumsbereichs, der standardmäßig die letzten 30 Tage umfasst, wenn kein Wert angegeben wird.

### Variablentypen {#variable-types}

Die folgenden Variablentypen werden akzeptiert:

- [Zahl](#number)
- [Datumsbereich](#date-range)
- [Messaging](#messaging)
- [Produkte](#products)
- [Angepasste Events](#custom-events)
- [Eigenschaften angepasster Events](#custom-event-properties)
- [Workspace](#workspace)
- [Kataloge](#catalogs)
- [Katalogfelder](#catalog-fields)
- [Optionen](#options)
- [Segments](#segments)
- [String](#string)
- [Tags](#tags)

#### Zahl {#number}

- **Ersetzungswert:** Der angegebene Wert, z. B. `5.5`
- **Verwendungsbeispiel:** {% raw %}`some_number_column < {{number.${some name}}}`{% endraw %}

#### Datumsbereich {#date-range}

Wenn Sie sowohl `start_date` als auch `end_date` verwenden, müssen sie denselben Namen haben, damit Sie sie als Datumsbereich nutzen können.

##### Beispielwerte {#example-values}

Der Datumsbereichstyp kann relativ, Startdatum, Enddatum oder Datumsbereich sein.

Alle vier Typen werden angezeigt, wenn sowohl `start_date` als auch `end_date` mit demselben Namen verwendet werden. Wenn nur einer verwendet wird, werden nur die relevanten Typen angezeigt.

| Datumsbereichstyp | Beschreibung | Erforderliche Werte |
| --- | --- | --- |
| Relativ | Gibt die letzten X Tage an | Erfordert `start_date` |
| Startdatum | Gibt ein Startdatum an | Erfordert `start_date` |
| Enddatum | Gibt ein Enddatum an | Erfordert `end_date` |
| Datumsbereich | Gibt sowohl ein Start- als auch ein Enddatum an | Erfordert sowohl `start_date` als auch `end_date` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Beispielwerte" }

- **Ersetzungswert:** Ersetzt `start_date` und `end_date` durch einen Unix-Zeitstempel in Sekunden für ein angegebenes Datum in UTC, z. B. `1696517353`.
- **Verwendungsbeispiel:** Für alle Variablen – relativ, Startdatum, Enddatum und Datumsbereich:
    - {% raw %}`time > {{start_date.${some name}}} AND time < {{end_date.${some name}}}` {% endraw %}
        - Sie können entweder `start_date` oder `end_date` verwenden, wenn Sie keinen Datumsbereich benötigen.

#### Messaging {#messaging}

Alle Messaging-Variablen müssen denselben Bezeichner teilen, wenn Sie ihren Zustand in einer Gruppe verknüpfen möchten.

##### Canvas

Zur Auswahl eines Canvas. Wenn derselbe Name wie bei einer Campaign verwendet wird, erscheint im Tab **Variables** ein Optionsfeld zur Auswahl von entweder Canvas oder Campaign.

- **Ersetzungswert:** Canvas-BSON-ID
- **Verwendungsbeispiel:** {% raw %}`canvas_id = '{{canvas.${some name}}}'`{% endraw %}

##### Canvases

Zur Auswahl mehrerer Canvases. Wenn derselbe Name wie bei einer Campaign verwendet wird, erscheint im Tab **Variables** ein Optionsfeld zur Auswahl von entweder Canvas oder Campaign.

- **Ersetzungswert:** Canvases-BSON-IDs
- **Verwendungsbeispiel:** {% raw %}`canvas_id IN ({{canvases.${some name}}})`{% endraw %}

##### Campaign

Zur Auswahl einer Campaign. Wenn derselbe Name wie bei einem Canvas verwendet wird, erscheint im Tab **Variables** ein Optionsfeld zur Auswahl von entweder Canvas oder Campaign.

- **Ersetzungswert:** Campaign-BSON-ID
- **Verwendungsbeispiel:** {% raw %}`campaign_id = '{{campaign.${some name}}}'`{% endraw %}

##### Campaigns

Zur Mehrfachauswahl von Campaigns. Wenn derselbe Name wie bei einem Canvas verwendet wird, erscheint im Tab **Variables** ein Optionsfeld zur Auswahl von entweder Canvas oder Campaign.

- **Ersetzungswert:** Campaigns-BSON-IDs
- **Verwendungsbeispiel:** {% raw %}`campaign_id IN ({{campaigns.${some name}}})`{% endraw %}

##### Kampagnenvarianten {#campaign-variants}

Zur Auswahl von Kampagnenvarianten, die zur ausgewählten Campaign gehören. Muss in Verbindung mit einer Campaign- oder Campaigns-Variable verwendet werden.

- **Ersetzungswert:** API-IDs der Kampagnenvarianten, durch Kommas getrennte Strings wie `api-id1, api-id2`.
- **Verwendungsbeispiel:** {% raw %}`message_variation_api_id IN ({{campaign_variants.${some name}}})`{% endraw %}

##### Canvas-Varianten {#canvas-variants}

Zur Auswahl von Canvas-Varianten, die zu einem gewählten Canvas gehören. Muss mit einer Canvas- oder Canvases-Variable verwendet werden.

- **Ersetzungswert:** API-IDs der Canvas-Varianten, durch Kommas getrennte Strings wie `api-id1, api-id2`.
- **Verwendungsbeispiel:** {% raw %}`canvas_variation_api_id IN ({{canvas_variants.${some name}}})`{% endraw %}

##### Canvas-Schritt {#canvas-step}

Zur Auswahl eines Canvas-Schritts, der zu einem gewählten Canvas gehört. Muss mit einer Canvas-Variable verwendet werden.

- **Ersetzungswert:** API-ID des Canvas-Schritts
- **Verwendungsbeispiel:** {% raw %}`canvas_step_api_id = '{{canvas_step.${some name}}}'`{% endraw %}

##### Canvas-Schritte {#canvas-steps}

Zur Auswahl von Canvas-Schritten, die zu gewählten Canvases gehören. Muss mit einer Canvas- oder Canvases-Variable verwendet werden.

- **Ersetzungswert:** API-IDs der Canvas-Schritte
- **Verwendungsbeispiel:** {% raw %}`canvas_step_api_id IN ({{canvas_steps.${some name}}})`{% endraw %}