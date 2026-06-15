> Lernen Sie, wie Sie den Abfrage-Builder verwenden, um Berichte mit Braze-Daten in Snowflake zu erstellen. Der Abfrage-Builder enthält vorgefertigte [SQL-Anfragen-Templates]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/), die Ihnen den Einstieg erleichtern. Sie können aber auch Ihre eigenen angepassten SQL-Anfragen schreiben, um noch mehr Insights zu gewinnen.

## Voraussetzungen {#prerequisites}

Sie benötigen die [Berechtigung „PII anzeigen“]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/), um den Abfrage-Builder zu verwenden, da er direkten Zugriff auf einige Kundendaten erlaubt.

## Verwenden des Abfrage-Builders {#using-the-query-builder}

### 1. Schritt: Erstellen Sie eine SQL-Anfrage {#step-1-create-an-sql-query}

Um eine neue Anfrage zu erstellen, gehen Sie zu **Analytics** > **Query Builder** und wählen Sie dann **Create SQL Query**.

![Die Optionen „Query Template“ und „SQL Editor“ im Dropdown-Menü „Create SQL Query“.]({% image_buster /assets/img_archive/create_sql_query_button.png %}){: style="max-width:60%;"}

Wenn Sie Inspiration oder Hilfe bei der Gestaltung Ihrer Anfrage benötigen, wählen Sie **Query Template** und wählen Sie ein [vorgefertigtes Template]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) aus. Um mit einer leeren Anfrage zu beginnen, wählen Sie **SQL Editor**.

Ihr Bericht erhält automatisch einen Namen mit dem aktuellen Datum und der Uhrzeit. Bewegen Sie den Mauszeiger über den Namen und wählen Sie <i class="fas fa-pencil" alt="Bearbeiten"></i>, um Ihrer SQL-Anfrage einen aussagekräftigen Namen zu geben.

![Ein Beispielbericht mit dem Namen „Channel engagement for May 2025“.]({% image_buster /assets/img_archive/report_name_example.png %}){: style="max-width:80%;"}

### 2. Schritt: Erstellen Sie Ihre Anfrage {#step-2-build-your-query}

Bei der Erstellung Ihrer Anfrage können Sie sich von der KI helfen lassen oder sie selbst erstellen.

{% tabs local %}
{% tab Using BrazeAI %}
Der KI-Abfrage-Builder nutzt [GPT](https://openai.com/gpt-4) von OpenAI, um SQL für Ihre Anfrage zu empfehlen. So generieren Sie SQL mit dem KI-Abfrage-Builder:

1. Wenn Sie einen Bericht im Abfrage-Builder erstellt haben, wählen Sie den Tab **AI Query Builder**.
2. Geben Sie Ihren Prompt ein oder wählen Sie einen Beispielprompt aus und wählen Sie **Generate**, um Ihren Prompt in SQL zu übersetzen.
3. Überprüfen Sie das generierte SQL auf Richtigkeit und wählen Sie dann **Insert into Editor**.

![Der SQL-KI-Abfrage-Builder.]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

#### Tipps {#tips}

- Machen Sie sich mit den verfügbaren [Snowflake-Datentabellen]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) vertraut. Wenn Sie nach Daten fragen, die in diesen Tabellen nicht vorhanden sind, kann es passieren, dass ChatGPT eine fiktive Tabelle erfindet.
- Machen Sie sich mit den [SQL-Schreibregeln]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/#custom-sql) für dieses Feature vertraut. Die Nichtbeachtung dieser Regeln führt zu einem Fehler.
- Sie können bis zu 20 Prompts pro Minute mit dem KI-Abfrage-Builder senden.

##{% multi_lang_include brazeai/generative_ai/policy.md %}
{% endtab %}

{% tab On My Own %}
Schreiben Sie Ihre SQL-Anfrage mit der [Snowflake-Syntax](https://docs.snowflake.com/en/sql-reference). In der [Tabellenreferenz]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) finden Sie eine vollständige Liste der Tabellen und Spalten, die abgefragt werden können.

Um Tabellendetails im Abfrage-Builder anzuzeigen:

1. Öffnen Sie auf der Seite **Query Builder** das Panel **Reference** und wählen Sie **Available Data Tables**, um die verfügbaren Datentabellen und ihre Namen anzuzeigen.
3. Wählen Sie <i class="fas fa-chevron-down" alt=""></i> **See Details**, um die Tabellenbeschreibung und Informationen über die Tabellenspalten, wie z. B. Datentypen, anzuzeigen.
4. Um den Tabellennamen in Ihr SQL einzufügen, wählen Sie <i class="fas fa-copy" title="Copy table name to SQL editor"></i>.

Wenn Sie Ihre Anfrage auf einen bestimmten Zeitraum beschränken, können Sie schneller Ergebnisse erzielen. Hier eine Beispielabfrage, die die Anzahl der Käufe und den in der letzten Stunde erzielten Umsatz ermittelt.

```sql
SELECT COUNT(*) as Purchases, SUM(price) as Revenue
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('hour', -1, date_trunc('day',CURRENT_DATE()));
```

Diese Anfrage ruft die Anzahl der E-Mail-Sendungen im letzten Monat ab:

```sql
SELECT COUNT(*) as Sends
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('month', -1, date_trunc('day',CURRENT_DATE()));
```

Wenn Sie nach `CANVAS_ID`, `CANVAS_VARIATION_API_ID` oder `CAMPAIGN_ID` abfragen, werden die zugehörigen Namensspalten automatisch in die Ergebnistabelle aufgenommen. Sie müssen sie nicht in die `SELECT`-Anfrage selbst aufnehmen.

| ID-Name | Zugehörige Namensspalte |
| --- | --- |
| `CANVAS_ID` | Canvas Name |
| `CANVAS_VARIATION_API_ID` | Canvas Variant Name |
| `CAMPAIGN_ID` | Campaign Name |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tips" }

Diese Anfrage ruft alle drei IDs und ihre zugehörigen Namensspalten mit maximal 100 Zeilen ab:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
LIMIT 100
```

#### Fehlerbehebung {#troubleshooting}

Ihre Anfrage kann aus einem der folgenden Gründe fehlschlagen:

- Syntaxfehler in Ihrer SQL-Anfrage
- Zeitüberschreitung bei der Verarbeitung (nach 6 Minuten)
    - Bei Berichten, deren Ausführung länger als 6 Minuten dauert, tritt ein Timeout ein.
    - Versuchen Sie in diesem Fall, den Zeitraum Ihrer Datenabfrage zu verkürzen oder einen spezifischeren Datensatz abzufragen.
{% endtab %}
{% endtabs %}

### 3. Schritt: Generieren Sie Ihren Bericht {#step-3-generate-your-report}

Wenn Sie mit der Erstellung Ihrer Anfrage fertig sind, wählen Sie **Run Query**. Wenn keine Fehler oder [Zeitüberschreitungen](#report-timeouts) auftreten, wird aus der Anfrage eine CSV-Datei erstellt.

Um den CSV-Bericht herunterzuladen, wählen Sie **Export**.

![Der Abfrage-Builder zeigt die Ergebnisse für die Template-Anfrage „Channel engagement and revenue for the last 30 days“.]({% image_buster /assets/img_archive/query_builder.png %})

{% alert important %}
Jeder Bericht kann nur einmal pro Tag Ergebnisse liefern. Wenn Sie denselben Bericht mehrmals an einem Kalendertag ausführen, sehen Sie in jedem Bericht dieselben Ergebnisse.
{% endalert %}

## Zeitüberschreitungen bei Berichten {#report-timeouts}

Bei Berichten, deren Ausführung länger als sechs Minuten dauert, tritt ein Timeout ein. Wenn dies die erste Anfrage seit längerer Zeit ist, kann die Verarbeitung etwas länger dauern und die Wahrscheinlichkeit eines Timeouts ist daher höher. Versuchen Sie in diesem Fall, den Bericht erneut auszuführen.

Wenn Ihr Bericht auch nach mehreren Versuchen weiterhin ein Timeout verursacht, [kontaktieren Sie den Support]({{site.baseurl}}/help/support/#braze-support).

## Abbruchgründe abfragen {#querying-abort-reasons}

Sie können die Spalte `ABORT_TYPE` in jeder `USERS_MESSAGES_*_ABORT_SHARED`-Tabelle abfragen, um zu analysieren, warum Nachrichten nicht gesendet wurden. Das Feld `ABORT_TYPE` enthält einen String-Wert, der den spezifischen Grund für den Abbruch beschreibt, und das zugehörige Feld `ABORT_LOG` enthält zusätzliche Details (z. B. die Frequency-Capping-Regel, die getriggert wurde).

Um beispielsweise E-Mail-Abbrüche nach Typ in den letzten 30 Tagen zu zählen:

```sql
SELECT ABORT_TYPE, COUNT(*) as abort_count
FROM USERS_MESSAGES_EMAIL_ABORT_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('day', -30, CURRENT_DATE())
GROUP BY ABORT_TYPE
ORDER BY abort_count DESC
```

Die vollständige Liste der `ABORT_TYPE`-Werte und ihrer Beschreibungen finden Sie unter [Abbruchtypen]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/#abort-types).

## Daten und Ergebnisse {#data-and-results}

Alle Anfragen beziehen sich auf die Daten der letzten 60 Tage. Wenn Sie Ihre Ergebnisse exportieren, werden nur bis zu 1.000 Zeilen enthalten sein. Für Berichte, die größere Datenmengen erfordern, können Sie Tools wie [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) oder den [Export-API-Endpunkt]({{site.baseurl}}/api/endpoints/export/) verwenden.

## Snowflake Credits

Jedem Unternehmen stehen 5 Snowflake Credits pro Monat zur Verfügung, die auf alle Workspaces aufgeteilt werden. Ein kleiner Teil eines Snowflake Credits wird immer dann verbraucht, wenn Sie eine Anfrage ausführen oder eine Vorschau einer Tabelle anzeigen.

{% alert note %}
Snowflake Credits werden nicht zwischen Features geteilt. So sind zum Beispiel Credits für SQL-Segmenterweiterungen und den Abfrage-Builder unabhängig voneinander.
{% endalert %}

Der Verbrauch hängt von der Laufzeit Ihrer SQL-Anfrage ab. Je länger die Laufzeit, desto mehr Snowflake Credits werden verbraucht. Die Laufzeit kann sich je nach Komplexität und Umfang Ihrer Anfragen unterscheiden. Je komplexere und häufigere Anfragen Sie ausführen, desto mehr Ressourcen werden Ihnen zugewiesen und desto schneller wird die Laufzeit.

Credits werden beim Schreiben, Bearbeiten oder Speichern von Berichten im Braze SQL-Editor nicht verbraucht. Ihr Guthaben wird am ersten eines jeden Monats um 12 Uhr UTC auf 5 zurückgesetzt. Sie können den Verbrauch Ihres monatlichen Guthabens oben auf der Seite des Abfrage-Builders einsehen.

![Der Abfrage-Builder zeigt das im laufenden Monat verbrauchte Guthaben an.]({% image_buster /assets/img_archive/query_builder_credits.png %}){: style="max-width:60%;"}

Wenn Sie Ihr Guthaben aufgebraucht haben, können Sie keine Anfragen mehr ausführen, aber weiterhin SQL-Berichte erstellen, bearbeiten und speichern. Wenn Sie weitere Abfrage-Builder-Credits erwerben möchten, wenden Sie sich bitte an Ihren Account Manager.