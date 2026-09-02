> Lernen Sie, wie Sie den Abfrage-Builder verwenden, um Berichte mit Braze-Daten in Snowflake zu erstellen. Der Abfrage-Builder enthält vorgefertigte [SQL-Anfragen-Templates]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates), die Ihnen den Einstieg erleichtern. Sie können aber auch Ihre eigenen angepassten SQL-Anfragen schreiben, um noch mehr Insights zu gewinnen.

## Voraussetzungen {#prerequisites}

Sie benötigen die [Berechtigung „PII anzeigen“]({{site.baseurl}}/user_guide/administer/global/user_management/permissions), um den Abfrage-Builder zu verwenden, da er direkten Zugriff auf bestimmte Kundendaten ermöglicht.

## Verwendung des Abfrage-Builders {#using-the-query-builder}

### Schritt 1: SQL-Anfrage erstellen {#step-1-create-an-sql-query}

Um eine neue Anfrage zu erstellen, gehen Sie zu **Analytics** > **Abfrage-Builder** und wählen Sie **SQL-Anfrage erstellen** aus.

![Die Optionen „Anfrage-Template“ und „SQL-Editor“ im Dropdown „SQL-Anfrage erstellen“.]({% image_buster /assets/img_archive/create_sql_query_button.png %}){: style="max-width:60%;"}

Wenn Sie Inspiration oder Hilfe beim Erstellen Ihrer Anfrage benötigen, wählen Sie **Anfrage-Template** und ein [vorgefertigtes Template]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates). Um mit einer leeren Anfrage zu beginnen, wählen Sie **SQL-Editor** aus.

Ihr Bericht erhält automatisch einen Namen mit dem aktuellen Datum und der aktuellen Uhrzeit. Fahren Sie mit der Maus über den Namen und wählen Sie <i class="fas fa-pencil" alt="Bearbeiten"></i>, um Ihrer SQL-Anfrage einen aussagekräftigen Namen zu geben.

![Ein Beispiel für einen Berichtnamen: „Channel engagement for May 2025“.]({% image_buster /assets/img_archive/report_name_example.png %}){: style="max-width:80%;"}

### Schritt 2: Anfrage erstellen {#step-2-build-your-query}

Beim Erstellen Ihrer Anfrage können Sie sich von KI unterstützen lassen oder die Anfrage selbst schreiben.

{% tabs local %}
{% tab Mit BrazeAI %}
Der KI-Abfrage-Builder nutzt [GPT](https://openai.com/gpt-4), bereitgestellt von OpenAI, um SQL für Ihre Anfrage vorzuschlagen. So generieren Sie SQL mit dem KI-Abfrage-Builder:

1. Nachdem Sie einen Bericht im Abfrage-Builder erstellt haben, wählen Sie den Tab **KI-Abfrage-Builder** aus.
2. Geben Sie Ihren Prompt ein oder wählen Sie einen Beispielprompt aus und klicken Sie auf **Generieren**, um Ihren Prompt in SQL zu übersetzen.
3. Überprüfen Sie das generierte SQL, um sicherzustellen, dass es korrekt aussieht, und wählen Sie dann **In Editor einfügen** aus.

![Der SQL-KI-Abfrage-Builder.]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

#### Tipps {#tips}

- Machen Sie sich mit den verfügbaren [Snowflake-Datentabellen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables) vertraut. Wenn Sie nach Daten fragen, die in diesen Tabellen nicht vorhanden sind, kann es passieren, dass ChatGPT eine fiktive Tabelle erfindet.
- Machen Sie sich mit den [SQL-Schreibregeln]({{site.baseurl}}/user_guide/data_and_analytics/query_builder#custom-sql) für dieses Feature vertraut. Die Nichtbeachtung dieser Regeln führt zu einem Fehler.
- Sie können mit dem KI-Abfrage-Builder bis zu 20 Prompts pro Minute senden.

##{% multi_lang_include brazeai/generative_ai/policy.md %}
{% endtab %}

{% tab Eigene Erstellung %}
Schreiben Sie Ihre SQL-Anfrage mit der [Snowflake-Syntax](https://docs.snowflake.com/en/sql-reference). In der [Tabellenreferenz]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables) finden Sie eine vollständige Liste aller verfügbaren Tabellen und Spalten, die abgefragt werden können.

So zeigen Sie Tabellendetails im Abfrage-Builder an:

1. Öffnen Sie auf der Seite **Abfrage-Builder** das **Referenz**-Panel und wählen Sie **Verfügbare Datentabellen** aus, um die verfügbaren Datentabellen und ihre Namen anzuzeigen.
3. Wählen Sie <i class="fas fa-chevron-down" alt=""></i> **Details anzeigen** aus, um die Tabellenbeschreibung und Informationen zu den Tabellenspalten wie Datentypen anzuzeigen.
4. Um den Tabellennamen in Ihr SQL einzufügen, wählen Sie <i class="fas fa-copy" title="Tabellennamen in den SQL-Editor kopieren"></i>.

Wenn Sie Ihre Anfrage auf einen bestimmten Zeitraum beschränken, werden die Ergebnisse schneller generiert. Das folgende Beispiel zeigt eine Anfrage, die die Anzahl der Käufe und den generierten Umsatz der letzten Stunde abruft.

```sql
SELECT COUNT(*) as Purchases, SUM(price) as Revenue
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('hour', -1, date_trunc('day',CURRENT_DATE()));
```

Diese Anfrage ruft die Anzahl der E-Mail-Sends im letzten Monat ab:

```sql
SELECT COUNT(*) as Sends
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('month', -1, date_trunc('day',CURRENT_DATE()));
```

Wenn Sie nach `CANVAS_ID`, `CANVAS_VARIATION_API_ID` oder `CAMPAIGN_ID` abfragen, werden die zugehörigen Namensspalten automatisch in die Ergebnistabelle aufgenommen. Sie müssen sie nicht in die `SELECT`-Anfrage selbst einschließen.

| ID-Name | Zugehörige Namensspalte |
| --- | --- |
| `CANVAS_ID` | Canvas Name |
| `CANVAS_VARIATION_API_ID` | Canvas-Variante Name |
| `CAMPAIGN_ID` | Campaign Name |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipps" }

Diese Anfrage ruft alle drei IDs und ihre zugehörigen Namensspalten mit maximal 100 Zeilen ab:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
LIMIT 100
```

#### Fehlerbehebung {#troubleshooting}

Ihre Anfrage kann aus folgenden Gründen fehlschlagen:

- Syntaxfehler in Ihrer SQL-Anfrage
- Zeitüberschreitung bei der Verarbeitung (nach 6 Minuten)
    - Berichte, deren Ausführung länger als 6 Minuten dauert, werden wegen Zeitüberschreitung abgebrochen.
    - Wenn bei einem Bericht eine Zeitüberschreitung auftritt, versuchen Sie, den Zeitraum einzuschränken, in dem Sie Daten abfragen, oder fragen Sie einen spezifischeren Datensatz ab.
{% endtab %}
{% endtabs %}

### Schritt 3: Bericht generieren {#step-3-generate-your-report}

Wenn Sie Ihre Anfrage fertig erstellt haben, wählen Sie **Anfrage ausführen** aus. Wenn keine Fehler oder [Berichts-Zeitüberschreitungen](#report-timeouts) auftreten, wird aus der Anfrage eine CSV-Datei generiert.

Um den CSV-Bericht herunterzuladen, wählen Sie **Exportieren** aus.

![Der Abfrage-Builder mit den Ergebnissen für die Template-Anfrage „Channel engagement and revenue for the last 30 days“.]({% image_buster /assets/img_archive/query_builder.png %})

{% alert important %}
Jeder Bericht kann nur einmal pro Tag Ergebnisse generieren. Wenn Sie denselben Bericht mehrmals an einem Kalendertag ausführen, sehen Sie in jedem Bericht dieselben Ergebnisse.
{% endalert %}

## Zeitüberschreitung bei Berichten {#report-timeouts}

Berichte, deren Ausführung länger als sechs Minuten dauert, werden aufgrund einer Zeitüberschreitung abgebrochen. Wenn Sie zum ersten Mal seit Längerem eine Anfrage ausführen, kann die Verarbeitung länger dauern und die Wahrscheinlichkeit einer Zeitüberschreitung ist höher. Versuchen Sie in diesem Fall, den Bericht erneut auszuführen.

Wenn bei Ihrem Bericht nach mehreren Versuchen weiterhin eine Zeitüberschreitung auftritt, [wenden Sie sich an den Support]({{site.baseurl}}/help/support#braze-support).

## Abbruchgründe abfragen {#querying-abort-reasons}

Sie können die Spalte `ABORT_TYPE` in jeder `USERS_MESSAGES_*_ABORT_SHARED`-Tabelle abfragen, um zu analysieren, warum Nachrichten nicht gesendet wurden. Das Feld `ABORT_TYPE` enthält einen String-Wert, der den spezifischen Grund für den Abbruch beschreibt, und das zugehörige Feld `ABORT_LOG` enthält zusätzliche Details (z. B. die Frequency-Capping-Regel, die ausgelöst wurde).

Um beispielsweise E-Mail-Abbrüche nach Typ in den letzten 30 Tagen zu zählen:

```sql
SELECT ABORT_TYPE, COUNT(*) as abort_count
FROM USERS_MESSAGES_EMAIL_ABORT_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('day', -30, CURRENT_DATE())
GROUP BY ABORT_TYPE
ORDER BY abort_count DESC
```

Die vollständige Liste der `ABORT_TYPE`-Werte und deren Beschreibungen finden Sie unter [Abbruchtypen]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables#abort-types).

## Daten und Ergebnisse {#data-and-results}

Alle Anfragen liefern Daten aus den letzten 60 Tagen. Wenn Sie Ihre Ergebnisse exportieren, enthält der Export nur bis zu 1.000 Zeilen. Für Berichte, die größere Datenmengen erfordern, können Sie Tools wie [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) oder den [Export-API-Endpunkt]({{site.baseurl}}/api/endpoints/export) verwenden.

## Snowflake-Credits

Jedes Unternehmen verfügt über 5 Snowflake-Credits pro Monat, die über alle Workspaces hinweg geteilt werden. Ein kleiner Teil eines Snowflake-Credits wird jedes Mal verbraucht, wenn Sie eine Anfrage ausführen oder eine Tabellenvorschau anzeigen.

{% alert note %}
Snowflake-Credits werden nicht zwischen Features geteilt. Zum Beispiel sind Credits für Segmenterweiterungen und den Abfrage-Builder unabhängig voneinander.
{% endalert %}

Der Credit-Verbrauch korreliert mit der Laufzeit Ihrer SQL-Anfrage. Je länger die Laufzeit, desto höher ist der Anteil eines Snowflake-Credits, den eine Anfrage kostet. Die Laufzeit kann je nach Komplexität und Größe Ihrer Anfragen variieren. Je komplexer und häufiger Ihre Anfragen sind, desto größer wird Ihre Ressourcenzuweisung und desto schneller wird Ihre Laufzeit.

Credits werden nicht verbraucht, wenn Sie Berichte im Braze SQL-Editor schreiben, bearbeiten oder speichern. Ihre Credits werden am Ersten jedes Monats um 00:00 Uhr UTC auf 5 zurückgesetzt. Sie können Ihren monatlichen Credit-Verbrauch oben auf der Seite des Abfrage-Builders überwachen.

![Abfrage-Builder mit der Anzeige der im aktuellen Monat verbrauchten Credits.]({% image_buster /assets/img_archive/query_builder_credits.png %}){: style="max-width:60%;"}

Wenn Sie das Credit-Limit erreicht haben, können Sie keine Anfragen mehr ausführen, aber Sie können SQL-Berichte erstellen, bearbeiten und speichern. Wenn Sie weitere Credits für den Abfrage-Builder erwerben möchten, wenden Sie sich bitte an Ihren Account Manager.