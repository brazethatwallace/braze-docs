# SQL-Segmenterweiterungen {#sql-segment-extensions}

> Sie können eine Segmenterweiterung mithilfe von Snowflake-SQL-Abfragen von [Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)-Daten erstellen. SQL kann Ihnen helfen, neue Segmentierungs-Anwendungsfälle zu erschließen, da es die Flexibilität bietet, die Beziehungen zwischen Daten auf eine Weise zu beschreiben, die mit anderen Segmentierungs-Features nicht möglich ist.
>
> Wie bei Standard-Segmenterweiterungen können Sie in Ihrer SQL-Segmenterweiterung Ereignisse aus den letzten zwei Jahren (730 Tage) abfragen. Im Gegensatz zu Standard-Segmenterweiterungen [verbrauchen SQL-Segmenterweiterungen Credits](#credits).

## Voraussetzungen {#prerequisites}

Da über dieses Feature auf PII-Daten zugegriffen werden kann, benötigen Sie PII-Berechtigungen, um SQL-Segmentabfragen auszuführen.

## Erstellen einer Segmenterweiterung {#creating-a-segment-extension}

### Schritt 1: Editor auswählen {#step-1-choose-an-editor}

Bei der Erstellung Ihrer SQL-Segmenterweiterung stehen Ihnen zwei Arten von SQL-Editoren zur Auswahl: der SQL-Editor und der inkrementelle SQL-Editor.

- **Vollständige Aktualisierung:** Bei jeder Aktualisierung Ihres Segments fragt Braze alle verfügbaren Daten ab, um Ihr Segment zu aktualisieren. Dies verbraucht mehr Credits als inkrementelle Aktualisierungen. Erweiterungen mit vollständiger Aktualisierung können die Mitgliedschaft täglich automatisch neu generieren, können jedoch nicht mit inkrementeller Aktualisierung aktualisiert werden.
- **Inkrementelle Aktualisierung:** Die inkrementelle Aktualisierung ist eine kostengünstigere Möglichkeit, Ihre Abfrage einzurichten, obwohl die Einrichtung einige zusätzliche [Schritte](#step-2-write-your-sql) erfordert. Wenn Sie diese zusätzlichen Schritte bei der Erstellung Ihres Segments durchführen können, lohnt es sich, diese Option zu wählen, da Ihre Abfrage weniger Credits verbraucht.
- **KI-SQL-Generator:** Der KI-SQL-Generator ermöglicht es Ihnen, eine Eingabeaufforderung in natürlicher Sprache zu schreiben und sie in eine SQL-Abfrage für Ihr Segment umzuwandeln. Dies ist ein schneller Weg, um loszulegen, ohne das SQL selbst schreiben zu müssen.

{% alert tip %}
Sie können für alle SQL-Segments, die in einem der beiden SQL-Editoren erstellt wurden, eine manuelle vollständige Aktualisierung durchführen.
{% endalert %}

{% tabs local %}
{% tab Vollständige Aktualisierung %}

So erstellen Sie eine SQL-Segmenterweiterung mit vollständiger Aktualisierung:

1. Gehen Sie zu **Zielgruppe** > **Segmenterweiterungen**.
2. Wählen Sie **Neue Erweiterung erstellen** und dann **Vollständige Aktualisierung**.<br><br>
   ![Modal „Neue Erweiterung erstellen“ mit den Optionen „Vollständige Aktualisierung“ und „Inkrementelle Aktualisierung“.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. Fügen Sie einen Namen für Ihre Segmenterweiterung hinzu und geben Sie Ihr SQL ein. Anforderungen und Ressourcen finden Sie in [Schritt 2](#step-2-write-your-sql).<br><br>
   ![SQL-Editor mit einer Beispiel-SQL-Segmenterweiterung.]({% image_buster /assets/img_archive/sql_segments_editor.png %}){: style="max-width:60%" }<br><br>
4. Speichern Sie Ihre Segmenterweiterung.

{% endtab %}
{% tab Inkrementelle Aktualisierung %}

So erstellen Sie eine SQL-Segmenterweiterung mit inkrementeller Aktualisierung:

1. Gehen Sie zu **Zielgruppe** > **Segmenterweiterungen**.
2. Wählen Sie **Neue Erweiterung erstellen** und dann **Inkrementelle Aktualisierung**.<br><br>
   ![Modal „Neue Erweiterung erstellen“ mit den Optionen „Vollständige Aktualisierung“ und „Inkrementelle Aktualisierung“.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. Fügen Sie einen Namen für Ihre Segmenterweiterung hinzu und geben Sie Ihr SQL ein. Anforderungen und Ressourcen finden Sie im Abschnitt [SQL schreiben](#writing-sql).<br><br>
   ![SQL-Editor mit einer Beispiel für eine inkrementelle SQL-Segmenterweiterung.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:60%" }<br><br>
4. Aktivieren Sie bei Bedarf **Erweiterung täglich regenerieren**.<br><br>
   ![Kontrollkästchen zum täglichen Regenerieren der Erweiterung.]({% image_buster /assets/img_archive/sql_segments_regenerate.png %}){: style="max-width:60%" }<br><br>
   Wenn diese Option aktiviert ist, aktualisiert Braze die Segmentmitgliedschaft automatisch jeden Tag. Das bedeutet, dass Braze jeden Tag um Mitternacht in der Zeitzone Ihres Unternehmens (mit einer möglichen Verzögerung von einer Stunde) nach neuen Nutzer:innen in Ihrem Segment sucht und diese automatisch hinzufügt. Wenn eine Segmenterweiterung 7 Tage lang nicht verwendet wurde, pausiert Braze die tägliche Regenerierung automatisch. Eine nicht verwendete Segmenterweiterung ist eine, die nicht Teil einer Campaign oder eines Canvas ist (die Campaign oder das Canvas muss nicht aktiv sein, damit die Erweiterung als „verwendet“ gilt).<br><br>
5. Speichern Sie Ihre Segmenterweiterung.

{% endtab %}

{% tab KI-SQL-Generator %}

{% alert note %}
Der KI-SQL-Generator ist derzeit als Beta-Feature verfügbar. Kontaktieren Sie Ihren Customer-Success-Manager, wenn Sie an dieser Beta-Phase teilnehmen möchten.
{% endalert %}

Der KI-SQL-Generator nutzt [GPT](https://openai.com/gpt-4), unterstützt von OpenAI, um SQL für Ihr SQL-Segment zu empfehlen.

![KI-SQL-Generator mit der Eingabeaufforderung „Nutzer:innen, die im letzten Monat eine Benachrichtigung erhalten haben“]({% image_buster /assets/img/ai_sql_generator.png %}){: style="max-width:70%;"}

So verwenden Sie den KI-SQL-Generator:

1. Wählen Sie **KI-SQL-Generator starten**, nachdem Sie ein [SQL-Segment]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) mit vollständiger oder inkrementeller Aktualisierung erstellt haben.
2. Geben Sie Ihre Eingabeaufforderung ein und wählen Sie **Generieren**, um Ihre Eingabeaufforderung in SQL umzuwandeln.
3. Überprüfen Sie das generierte SQL, um sicherzustellen, dass es korrekt aussieht, und speichern Sie dann Ihr Segment.

#### Beispiel-Eingabeaufforderungen {#example-prompts}

- Nutzer:innen, die im letzten Monat eine E-Mail erhalten haben
- Nutzer:innen, die im letzten Jahr weniger als fünf Käufe getätigt haben

#### Tipps {#tips}

- Machen Sie sich mit den verfügbaren [Snowflake-Datentabellen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables) vertraut. Wenn Sie nach Daten fragen, die in diesen Tabellen nicht vorhanden sind, kann ChatGPT eine fiktive Tabelle erfinden.
- Machen Sie sich mit den [SQL-Schreibregeln]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments?tab=sql%20editor#writing-sql) für dieses Feature vertraut. Die Nichtbeachtung dieser Regeln führt zu einem Fehler. Beispielsweise muss Ihr SQL-Code die Spalte `user_id` auswählen. Beginnen Sie Ihre Eingabeaufforderung mit „Nutzer:innen, die“, um dies zu erleichtern.
- Sie können bis zu 20 Eingabeaufforderungen pro Minute mit dem KI-SQL-Generator senden.

##{% multi_lang_include brazeai/generative_ai/policy.md %}

{% endtab %}
{% endtabs %}

{% alert note %}
SQL-Abfragen, die länger als 20 Minuten dauern, werden aufgrund einer Zeitüberschreitung abgebrochen.
{% endalert %}

Wenn die Erweiterung die Verarbeitung abgeschlossen hat, können Sie [ein Segment erstellen]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension#step-5-use-your-extension-in-a-segment), das Ihre Segmenterweiterung nutzt, und dieses neue Segment mit Ihren Campaigns und Canvases ansprechen.

### Schritt 2: SQL schreiben {#step-2-write-your-sql}

Ihre SQL-Abfrage sollte mit der [Snowflake-Syntax](https://docs.snowflake.com/en/sql-reference.html) geschrieben werden. Konsultieren Sie die [Tabellenreferenz]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables) für eine vollständige Liste der verfügbaren Tabellen und Spalten.

{% alert important %}
Beachten Sie, dass die abfragbaren Tabellen nur Ereignisdaten enthalten. Wenn Sie Nutzerattribute abfragen möchten, sollten Sie Ihr SQL-Segment mit angepassten Attributfiltern aus dem [klassischen Segmenter]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) kombinieren.
{% endalert %}

{% tabs %}
{% tab SQL-Editor %}

Ihr SQL muss zusätzlich die folgenden Regeln einhalten:

- Schreiben Sie eine einzelne SQL-Anweisung. Fügen Sie keine Semikolons ein.
- Ihr SQL darf nur eine Spalte auswählen: die Spalte `user_id`. Das bedeutet, Ihr SQL muss Folgendes enthalten:

```sql
SELECT DISTINCT user_id FROM "INSERT TABLE NAME"
```

- Es ist nicht möglich, nach Nutzer:innen mit null Ereignissen zu suchen. Das bedeutet, dass jede Abfrage nach Nutzer:innen, die ein Ereignis weniger als X Mal ausgeführt haben, diesen Workaround erfordert:
   1. Schreiben Sie eine Abfrage, die Nutzer:innen auswählt, die das Ereignis MEHR als X Mal ausgeführt haben.
   2. Wenn Sie Ihre Segmenterweiterung in Ihrem Segment referenzieren, wählen Sie `doesn't include`, um das Ergebnis umzukehren.

#### Zusätzliche Regeln {#additional-rules}

Zusätzlich muss Ihre Standard-SQL-Abfrage die folgenden Regeln einhalten:

- Sie können keine `DECLARE`-Anweisungen verwenden.
{% endtab %}
{% tab Inkrementeller SQL-Editor %}

Alle Abfragen mit inkrementeller Aktualisierung bestehen aus zwei Teilen: einer Abfrage und Schema-Details.

1. Schreiben Sie im Editor eine Abfrage, die `user_id`s aus Ihrer gewünschten Tabelle auswählt.
2. Fügen Sie Schema-Details hinzu, indem Sie einen **Operator**, eine **Anzahl** und einen **Zeitraum** aus den Feldern oben im Editor auswählen. Die Abfrage prüft, ob die Summe der Aggregationsspalte die Bedingung erfüllt, die Sie mit diesen Feldern festgelegt haben. Dies funktioniert ähnlich wie der Workflow zum Erstellen klassischer Segmenterweiterungen.<br><br>
   - **Operator:** Geben Sie an, ob das Ereignis mehr als, weniger als oder gleich einer bestimmten Anzahl von Vorkommen stattgefunden hat.<br>
   ![Operator-Feld mit ausgewähltem „Mehr als“.]({% image_buster /assets/img_archive/sql_segments_operator.png %})<br><br>
   - **Anzahl:** Wie oft Sie das Ereignis in Bezug auf den Operator auswerten möchten.<br>
   ![Anzahl-Feld mit eingegebenem „5“.]({% image_buster /assets/img_archive/sql_segments_times.png %})<br><br>
   - **Zeitraum:** Anzahl der Tage von 1 bis 730, in denen Sie nach Instanzen des Ereignisses suchen möchten. Dieser Zeitraum bezieht sich auf vergangene Tage relativ zum aktuellen Tag. Das folgende Beispiel zeigt die Abfrage nach Nutzer:innen, die das Ereignis mehr als 5 Mal in den letzten 365 Tagen ausgeführt haben.<br>
   ![Zeitraum-Feld mit eingegebenem „365“.]({% image_buster /assets/img_archive/sql_segments_period.png %})

Im folgenden Beispiel würde das resultierende Segment Nutzer:innen enthalten, die das Ereignis `favorited` in den letzten 30 Tagen nach einem bestimmten Datum mehr als 3 Mal ausgeführt haben.

![SQL-Editor mit einer Beispiel für eine inkrementelle SQL-Segmenterweiterung.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:65%" }

![SQL-Vorschau einer inkrementellen SQL-Segmenterweiterung.]({% image_buster /assets/img_archive/sql_segments_incremental_preview.png %}){: style="max-width:85%" }

{% alert tip %}
Die inkrementelle Aktualisierung berücksichtigt verspätete Ereignisse – Ereignisse, die nach dem täglichen Aktualisierungsfenster eintreffen, wie z. B. SDK-Ereignisse, die zum Zeitpunkt ihrer Erfassung nicht gesendet wurden. Wenn das Segment aktualisiert wird, verarbeitet Braze die Daten der Tage, zu denen diese verspäteten Ereignisse gehören, erneut.
{% endalert %}

#### Wie die inkrementelle Aktualisierung Nutzer:innen über die Zeit verfolgt {#how-incremental-refresh-tracks-users-over-time}

Wenn Sie die inkrementelle Aktualisierung verwenden, speichert Braze tägliche Zählungen für jede:n Nutzer:in in einer internen Zähltabelle, sodass Ihr Segment über den gesamten Zeitraum ausgewertet werden kann, ohne jeden Tag alle historischen Daten erneut abzufragen.

**Was gespeichert wird:** Braze pflegt eine Zähltabelle (ähnlich einer Segment-Kohortentabelle), die tägliche Nutzerqualifikationszählungen im Format `(date, user_id, count)` akkumuliert. Diese Tabelle bewahrt historische Daten außerhalb des zweitägigen rollierenden Aktualisierungsfensters auf.

**Was bei jeder Aktualisierung passiert:** Wenn eine inkrementelle Aktualisierung ausgeführt wird, löscht Braze nur die Datensätze innerhalb des zweitägigen rollierenden Aktualisierungsfensters aus der Zähltabelle. Anschließend wird Ihre SQL-Abfrage mit aktualisierten Zeitparametern (unter Verwendung von `$start_date`) erneut ausgeführt, um frische Zeilen für diese Daten einzufügen. Historische Zeilen außerhalb des zweitägigen rollierenden Aktualisierungsfensters bleiben in der Zähltabelle intakt.

**Wie Braze entscheidet, wer im Segment ist:** Braze wertet Ihre Segmentmitgliedschaftskriterien gegen die gesamte akkumulierte Zähltabelle aus, nicht nur gegen die letzte zweitägige rollierende Aktualisierungs-Nutzlast. Das bedeutet, dass Nutzer:innen, die sich vor mehr als zwei Tagen qualifiziert haben, im Segment bleiben, es sei denn, die aggregierten Zählungen erfüllen Ihre Kriterien nicht mehr.

**SQL schreiben, das zuverlässig aktualisiert:** Beim Schreiben von SQL für die inkrementelle Aktualisierung sollten Sie Abfragemuster vermeiden, die bei teilweisen Aktualisierungen inkonsistente Ergebnisse liefern könnten. Beispielsweise können gefensterte Aggregationen wie `MAX(time)`, die von Daten über `$start_date`-Grenzen hinweg abhängen, den Zeilenstatus unerwartet ändern, wenn nur eine Teilmenge der Daten neu berechnet wird. Strukturieren Sie Ihre Abfragen so, dass die Ausgabe jedes Tages nur von Ereignissen dieses Tages abhängt. So werden konsistente Ergebnisse gewährleistet, unabhängig davon, ob die Abfrage 2 oder 730 Tage an Daten verarbeitet.

#### Zusätzliche Regeln

Zusätzlich muss Ihre Abfrage mit inkrementeller Aktualisierung die folgenden Regeln einhalten:

- Schreiben Sie eine einzelne SQL-Anweisung. Fügen Sie keine Semikolons ein.
- Ihr inkrementelles SQL-Segment kann nur auf ein Ereignis verweisen. Ihre Dropdowns für Datum und Anzahl gelten für dieses Ereignis.
- Ihr SQL muss den Alias `$date()` enthalten (z. B. `$date(time)`), `user_id` und eine `COUNT()`-Aggregation auswählen, nach Datum und `user_id` gruppieren und mit `$start_date` auf Ihrer Zeitspalte filtern (z. B. `time > $start_date`). Das Speichern von SQL ohne `$date()` oder diese Felder gibt einen Fehler zurück.
- Sie können keine `DECLARE`-Anweisungen verwenden.
{% endtab %}
{% endtabs %}

{% alert note %}
Wenn Sie ein SQL-Segment erstellen, das die Tabelle `CATALOGS_ITEMS_SHARED` verwendet, müssen Sie eine Katalog-ID angeben. Zum Beispiel:

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

### Schritt 3: Abfrage in der Vorschau anzeigen {#step-3-preview-the-query}

Vor dem Speichern können Sie eine Vorschau Ihrer Abfrage ausführen. Abfragevorschauen sind automatisch auf 100 Zeilen begrenzt und haben eine Zeitüberschreitung nach 60 Sekunden. Die Anforderung der Spalte `user_id` gilt nicht bei der Ausführung einer Vorschau.

Für inkrementelle SQL-Segmenterweiterungen enthält die Vorschau nicht die zusätzlichen Kriterien aus Ihren Feldern für Operator, Anzahl und Zeitraum.

### Schritt 4: Bestimmen, ob SQL invertiert werden muss {#step-4-determine-if-you-need-to-invert-sql}

Als Nächstes bestimmen Sie, ob Sie SQL invertieren müssen. Obwohl es nicht möglich ist, direkt nach Nutzer:innen mit null Ereignissen zu suchen, können Sie **SQL invertieren** verwenden, um diese Nutzer:innen anzusprechen.

{% alert note %}
Standardmäßig ist **SQL invertieren** nicht aktiviert. Wenn Sie jedoch den KI-SQL-Generator verwenden, um eine SQL-Anweisung zu generieren, die negiert werden muss, könnte ChatGPT eine Ausgabe liefern, die dieses Feature automatisch aktiviert.
{% endalert %}

Um beispielsweise Nutzer:innen mit weniger als drei Käufen anzusprechen, schreiben Sie zunächst eine Abfrage, die Nutzer:innen mit drei oder mehr Käufen auswählt. Wählen Sie dann **SQL invertieren**, um Nutzer:innen mit weniger als drei Käufen (einschließlich solcher mit null Käufen) anzusprechen.

{% alert important %}
Sofern Sie nicht gezielt Nutzer:innen mit null Ereignissen ansprechen möchten, müssen Sie SQL nicht invertieren. Wenn **SQL invertieren** ausgewählt ist, bestätigen Sie, dass das Feature benötigt wird und das Segment Ihrer gewünschten Zielgruppe entspricht. Wenn eine Abfrage beispielsweise Nutzer:innen mit mindestens einem Ereignis anspricht, werden bei Invertierung nur Nutzer:innen mit null Ereignissen angesprochen.
{% endalert %}

![Segmenterweiterung mit dem Namen „1–4 E-Mails in den letzten 30 Tagen geklickt“ mit aktivierter Option zum Invertieren von SQL.]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:90%;"}

## Aktualisierung der Segmentzugehörigkeit {#refreshing-segment-membership}

Um die Segmentzugehörigkeit einer mit SQL erstellten Segmenterweiterung zu aktualisieren, öffnen Sie die Segmenterweiterung und wählen Sie **Aktualisieren** aus.

{% alert tip %}
Wenn Sie ein Segment erstellt haben, bei dem Sie erwarten, dass Nutzer:innen regelmäßig ein- und austreten, aktualisieren Sie die verwendete Segmenterweiterung manuell, bevor Sie dieses Segment in einer Campaign oder einem Canvas ansprechen.
{% endalert %}

## Verwalten Ihrer Segmenterweiterungen {#managing-your-segment-extensions}

Auf der Seite **Segmenterweiterungen** werden mit SQL generierte Segmente durch <i class="fas fa-code" alt="SQL-Segmenterweiterung"></i> neben ihrem Namen gekennzeichnet.

Wählen Sie eine SQL-Segmenterweiterung aus, um anzuzeigen, wo die Erweiterung verwendet wird, die Erweiterung zu archivieren oder die [Segmentzugehörigkeit manuell zu aktualisieren](#refreshing-segment-membership).

![Bereich „Messaging-Nutzung“ des SQL-Editors, der zeigt, wo das SQL-Segment verwendet wird.]({% image_buster /assets/img_archive/sql_segments_usage.png %}){: style="max-width:70%;"}

### Aktualisierungseinstellungen festlegen {#designating-refresh-settings}

{% multi_lang_include audience/segments.md section='Refresh settings' %}

## Snowflake-Credits {#credits}

Jeder Braze Workspace verfügt über 5 Snowflake-Credits pro Monat. Wenn Sie mehr Credits benötigen, wenden Sie sich an Ihren Account Manager:in. Credits werden immer dann verbraucht, wenn Sie die Mitgliedschaft eines SQL-Segments aktualisieren oder speichern und aktualisieren. Credits werden nicht verbraucht, wenn Sie Vorschauen innerhalb eines SQL-Segments ausführen oder eine klassische Segmenterweiterung speichern oder aktualisieren.

{% alert note %}
Snowflake-Credits werden nicht zwischen Features geteilt. So sind beispielsweise Credits für SQL-Segmenterweiterungen und den Abfrage-Builder unabhängig voneinander.
{% endalert %}

Der Credit-Verbrauch hängt von der Laufzeit Ihrer SQL-Anfrage ab. Je länger die Laufzeit ist, desto mehr Credits kostet eine Abfrage. Die Laufzeit kann je nach Komplexität und Umfang Ihrer Abfragen im Laufe der Zeit variieren. Je komplexer und häufiger Sie Abfragen durchführen, desto größer ist Ihre Ressourcenzuweisung und desto schneller wird Ihre Laufzeit.

Um Credits zu sparen, sollten Sie eine Vorschau Ihrer Abfrage anzeigen, um sicherzustellen, dass sie korrekt ist, bevor Sie die SQL-Segmenterweiterung speichern.

Ihre Credits werden am ersten eines jeden Monats um 12 Uhr UTC auf 5 zurückgesetzt. Sie können Ihren Credit-Verbrauch im Laufe des Monats im Panel für die Credit-Nutzung überwachen. Klicken Sie auf der Seite **Segmenterweiterungen** auf <i class="fa-solid fa-chart-column"></i> **View SQL Credit Usage**.

![Panel für die SQL-Credit-Nutzung auf der Seite „SQL-Segmenterweiterungen“]({% image_buster /assets/img_archive/sql_segments_credits.png %}){: style="max-width:60%"}

Wenn Ihre Credits null erreichen, geschieht Folgendes:

- Alle SQL-Segmenterweiterungen, die für automatische Aktualisierung eingerichtet sind, werden nicht mehr aktualisiert, was sich auf die Mitgliedschaft in diesen Segmenten und auf alle Campaigns oder Canvases auswirkt, die auf diese Segmente abzielen.
- Sie können neue SQL-Segmenterweiterungen nur noch für den Rest des Monats als Entwurf speichern.

Alle Unternehmensnutzer:innen, die ein SQL-Segment erstellt haben, und Ihre Unternehmensadministrator:innen erhalten eine Benachrichtigungs-E-Mail, wenn Sie 50 %, 80 % und 100 % Ihrer Credits verbraucht haben. Nachdem Ihre Credits zu Beginn des nächsten Monats zurückgesetzt wurden, können Sie weitere SQL-Segmente erstellen, und die automatischen Aktualisierungen werden wieder aufgenommen.

Wenn Sie mehr SQL-Segment-Credits oder zusätzliche Segmenterweiterungen erwerben möchten, wenden Sie sich bitte an Ihren Account Manager:in.