# SQL-Segmenterweiterungen {#sql-segment-extensions}

> Sie können eine Segmenterweiterung mithilfe von Snowflake-SQL-Abfragen von [Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)-Daten erstellen. SQL kann Ihnen helfen, neue Segmentierungs-Anwendungsfälle zu erschließen, da es die Flexibilität bietet, die Beziehungen zwischen Daten auf eine Weise zu beschreiben, die mit anderen Segmentierungs-Features nicht möglich ist.
>
> Wie bei Standard-Segmenterweiterungen können Sie in Ihrer SQL-Segmenterweiterung Ereignisse aus den letzten zwei Jahren (730 Tage) abfragen. Im Gegensatz zu Standard-Segmenterweiterungen [verbrauchen SQL-Segmenterweiterungen Credits](#credits).

## Voraussetzungen {#prerequisites}

Da über dieses Feature auf PII-Daten zugegriffen werden kann, benötigen Sie PII-Berechtigungen, um SQL-Segment-Anfragen auszuführen.

## Erstellen einer Segmenterweiterung {#creating-a-segment-extension}

### Schritt 1: Editor auswählen {#step-1-choose-an-editor}

Bei der Erstellung Ihrer SQL-Segmenterweiterung stehen zwei Arten von SQL-Editoren zur Auswahl: der SQL-Editor und der inkrementelle SQL-Editor.

- **Vollständige Aktualisierung:** Bei jeder Aktualisierung Ihres Segments fragt Braze alle verfügbaren Daten ab, um Ihr Segment zu aktualisieren, was mehr Credits verbraucht als inkrementelle Aktualisierungen. Erweiterungen mit vollständiger Aktualisierung können die Mitgliedschaft täglich automatisch regenerieren, können jedoch nicht mit inkrementeller Aktualisierung aufgefrischt werden.
- **Inkrementelle Aktualisierung:** Die inkrementelle Aktualisierung ist eine kostengünstigere Methode, Ihre Abfrage einzurichten, obwohl die Einrichtung einige zusätzliche [Schritte](#step-2-write-your-sql) umfasst. Wenn Sie diese zusätzlichen Schritte bei der Erstellung Ihres Segments durchführen können, lohnt es sich, diese Option zu wählen, da Ihre Abfrage mit weniger Credits ausgeführt wird.
- **KI-SQL-Generator:** Der KI-SQL-Generator ermöglicht es Ihnen, einen Prompt in natürlicher Sprache zu verfassen und diesen in eine SQL-Abfrage für Ihr Segment umzuwandeln. Es ist eine schnelle Möglichkeit, loszulegen, ohne selbst SQL schreiben zu müssen.

{% alert tip %}
Sie können bei allen in beiden SQL-Editoren erstellten SQL-Segments eine manuelle vollständige Aktualisierung durchführen.
{% endalert %}

{% tabs local %}
{% tab Vollständige Aktualisierung %}

So erstellen Sie eine SQL-Segmenterweiterung mit vollständiger Aktualisierung:

1. Gehen Sie zu **Zielgruppe** > **Segmenterweiterungen**.
2. Wählen Sie **Neue Erweiterung erstellen** und dann **Vollständige Aktualisierung**.<br><br>
   ![Dialog „Neue Erweiterung erstellen“ mit den Optionen „Vollständige Aktualisierung“ und „Inkrementelle Aktualisierung“.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. Geben Sie einen Namen für Ihre Segmenterweiterung ein und fügen Sie Ihr SQL ein. Weitere Anforderungen und Ressourcen finden Sie unter [Schritt 2](#step-2-write-your-sql).<br><br>
   ![SQL-Editor mit einer beispielhaften SQL-Segmenterweiterung.]({% image_buster /assets/img_archive/sql_segments_editor.png %}){: style="max-width:60%" }<br><br>
4. Speichern Sie Ihre Segmenterweiterung.

{% endtab %}
{% tab Inkrementelle Aktualisierung %}

So erstellen Sie eine SQL-Segmenterweiterung mit inkrementeller Aktualisierung:

1. Gehen Sie zu **Zielgruppe** > **Segmenterweiterungen**.
2. Wählen Sie **Neue Erweiterung erstellen** und dann **Inkrementelle Aktualisierung**.<br><br>
   ![Dialog „Neue Erweiterung erstellen“ mit den Optionen „Vollständige Aktualisierung“ und „Inkrementelle Aktualisierung“.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. Geben Sie einen Namen für Ihre Segmenterweiterung ein und fügen Sie Ihr SQL ein. Weitere Anforderungen und Ressourcen finden Sie im Abschnitt [SQL schreiben](#writing-sql).<br><br>
   ![SQL-Editor mit einer beispielhaften inkrementellen SQL-Segmenterweiterung.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:60%" }<br><br>
4. Aktivieren Sie bei Bedarf **Erweiterung täglich regenerieren**.<br><br>
   ![Kontrollkästchen zur täglichen Regenerierung der Erweiterung.]({% image_buster /assets/img_archive/sql_segments_regenerate.png %}){: style="max-width:60%" }<br><br>
   Wenn diese Option aktiviert ist, aktualisiert Braze die Segmentmitgliedschaft automatisch jeden Tag. Das bedeutet, dass Braze jeden Tag um Mitternacht in der Zeitzone Ihres Unternehmens (mit einer möglichen Verzögerung von einer Stunde) prüft, ob neue Nutzer:innen in Ihrem Segment vorhanden sind, und diese automatisch hinzufügt. Wenn eine Segmenterweiterung 7 Tage lang nicht verwendet wurde, pausiert Braze die tägliche Regenerierung automatisch. Eine nicht verwendete Segmenterweiterung ist eine, die nicht Teil einer Campaign oder eines Canvas ist (die Campaign oder der Canvas muss nicht aktiv sein, damit die Erweiterung als „verwendet“ gilt).<br><br>
5. Speichern Sie Ihre Segmenterweiterung.

{% endtab %}

{% tab KI-SQL-Generator %}

{% alert note %}
Der KI-SQL-Generator ist derzeit als Beta-Feature verfügbar. Wenden Sie sich an Ihren Customer-Success-Manager, wenn Sie an diesem Beta-Test teilnehmen möchten.
{% endalert %}

Der KI-SQL-Generator nutzt [GPT](https://openai.com/gpt-4), unterstützt durch OpenAI, um SQL für Ihr SQL-Segment zu empfehlen.

![KI-SQL-Generator mit dem Prompt „Users that received a notification last month“]({% image_buster /assets/img/ai_sql_generator.png %}){: style="max-width:70%;"}

So verwenden Sie den KI-SQL-Generator:

1. Wählen Sie **KI-SQL-Generator starten**, nachdem Sie ein [SQL-Segment]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) mit vollständiger oder inkrementeller Aktualisierung erstellt haben.
2. Geben Sie Ihren Prompt ein und wählen Sie **Generieren**, um Ihren Prompt in SQL umzuwandeln.
3. Überprüfen Sie das generierte SQL, um sicherzustellen, dass es korrekt aussieht, und speichern Sie dann Ihr Segment.

#### Beispiel-Prompts {#example-prompts}

- Nutzer:innen, die im letzten Monat eine E-Mail erhalten haben
- Nutzer:innen, die im letzten Jahr weniger als fünf Käufe getätigt haben

#### Tipps {#tips}

- Machen Sie sich mit den verfügbaren [Snowflake-Datentabellen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables) vertraut. Wenn Sie nach Daten fragen, die in diesen Tabellen nicht vorhanden sind, kann ChatGPT eine fiktive Tabelle erstellen.
- Machen Sie sich mit den [SQL-Schreibregeln]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments?tab=sql%20editor#writing-sql) für dieses Feature vertraut. Ein Nichtbeachten dieser Regeln führt zu einem Fehler. Ihr SQL-Code muss beispielsweise die Spalte `user_id` auswählen. Es kann helfen, Ihren Prompt mit „users who“ zu beginnen.
- Sie können bis zu 20 Prompts pro Minute mit dem KI-SQL-Generator senden.

##{% multi_lang_include brazeai/generative_ai/policy.md %}

{% endtab %}
{% endtabs %}

{% alert note %}
SQL-Abfragen, deren Ausführung länger als 20 Minuten dauert, werden aufgrund einer Zeitüberschreitung abgebrochen.
{% endalert %}

Wenn die Verarbeitung der Erweiterung abgeschlossen ist, können Sie [ein Segment erstellen]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension#step-5-use-your-extension-in-a-segment), das Ihre Segmenterweiterung verwendet, und dieses neue Segment mit Ihren Campaigns und Canvases ansprechen.

### Schritt 2: SQL schreiben {#step-2-write-your-sql}

Ihre SQL-Abfrage sollte mit [Snowflake-Syntax](https://docs.snowflake.com/en/sql-reference.html) geschrieben werden. In der [Tabellenreferenz]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables) finden Sie eine vollständige Liste der Tabellen und Spalten, die abgefragt werden können.

{% alert important %}
Beachten Sie, dass die abfragbaren Tabellen nur Ereignisdaten enthalten. Wenn Sie Nutzerattribute abfragen möchten, sollten Sie Ihr SQL-Segment mit Filtern für angepasste Attribute aus dem [klassischen Segmentierer]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) kombinieren.
{% endalert %}

{% tabs %}
{% tab SQL-Editor %}

Ihr SQL muss zusätzlich folgende Regeln einhalten:

- Schreiben Sie eine einzelne SQL-Anweisung. Verwenden Sie keine Semikolons.
- Ihr SQL darf nur eine Spalte auswählen: die Spalte `user_id`. Das bedeutet, Ihr SQL muss Folgendes enthalten:

```sql
SELECT DISTINCT user_id FROM "INSERT TABLE NAME"
```

- Es ist nicht möglich, nach Nutzer:innen zu suchen, die null Ereignisse haben. Das bedeutet, dass jede Abfrage nach Nutzer:innen, die ein Ereignis weniger als X Mal ausgeführt haben, folgenden Workaround erfordert:
   1. Schreiben Sie eine Abfrage, die Nutzer:innen auswählt, die das Ereignis MEHR als X Mal haben.
   2. Wenn Sie Ihre Segmenterweiterung in Ihrem Segment referenzieren, wählen Sie `doesn't include`, um das Ergebnis umzukehren.

#### Zusätzliche Regeln {#additional-rules}

Darüber hinaus muss Ihre Standard-SQL-Abfrage folgende Regeln einhalten:

- Sie können keine `DECLARE`-Anweisungen verwenden.
{% endtab %}
{% tab Inkrementeller SQL-Editor %}

Alle Abfragen mit inkrementeller Aktualisierung bestehen aus zwei Teilen: einer Abfrage und Schemadetails.

1. Schreiben Sie im Editor eine Abfrage, die `user_id`s aus der gewünschten Tabelle auswählt.
2. Fügen Sie Schemadetails hinzu, indem Sie einen **Operator**, eine **Anzahl** und einen **Zeitraum** aus den Feldern oben im Editor auswählen. Die Abfrage prüft, ob die Summe der Aggregationsspalte eine bestimmte Bedingung erfüllt, die durch die Platzhalter {% raw %}`{{operator}}` und `{{number of times}}`{% endraw %} festgelegt wird. Dies funktioniert ähnlich wie der Workflow zur Erstellung klassischer Segmenterweiterungen.<br><br>
   - **Operator:** Geben Sie an, ob das Ereignis mehr als, weniger als oder gleich einer bestimmten Anzahl von Vorkommen stattgefunden hat.<br>
   ![Operator-Feld mit ausgewählter Option „More than“.]({% image_buster /assets/img_archive/sql_segments_operator.png %})<br><br>
   - **Anzahl:** Wie oft Sie das Ereignis in Bezug auf den Operator auswerten möchten.<br>
   ![Feld „Anzahl“ mit dem Wert „5“.]({% image_buster /assets/img_archive/sql_segments_times.png %})<br><br>
   - **Zeitraum:** Anzahl der Tage von 1 bis 730, in denen Sie Vorkommen des Ereignisses prüfen möchten. Dieser Zeitraum bezieht sich auf vergangene Tage relativ zum aktuellen Tag. Das folgende Beispiel zeigt eine Abfrage nach Nutzer:innen, die das Ereignis in den letzten 365 Tagen mehr als 5 Mal ausgeführt haben.<br>
   ![Feld „Zeitraum“ mit dem Wert „365“.]({% image_buster /assets/img_archive/sql_segments_period.png %})

Im folgenden Beispiel würde das resultierende Segment Nutzer:innen enthalten, die das Ereignis `favorited` in den letzten 30 Tagen mehr als 3 Mal nach einem bestimmten Datum ausgeführt haben.

![SQL-Editor mit einer beispielhaften inkrementellen SQL-Segmenterweiterung.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:65%" }

![SQL-Vorschau einer inkrementellen SQL-Segmenterweiterung.]({% image_buster /assets/img_archive/sql_segments_incremental_preview.png %}){: style="max-width:85%" }

{% alert tip %}
Segmente mit inkrementeller Aktualisierung berücksichtigen verspätete Ereignisse, also Ereignisse, die vor mehr als 2 Tagen stattfanden (beispielsweise SDK-Ereignisse, die zum Zeitpunkt der Erfassung nicht gesendet wurden).
{% endalert %}

#### Zusätzliche Regeln

Darüber hinaus muss Ihre Abfrage mit inkrementeller Aktualisierung folgende Regeln einhalten:

- Schreiben Sie eine einzelne SQL-Anweisung. Verwenden Sie keine Semikolons.
- Ihr inkrementelles SQL-Segment kann sich nur auf ein einzelnes Ereignis beziehen. Ihre Dropdowns für Datum und Anzahl beziehen sich auf das von Ihnen gewählte Ereignis.
- Ihr SQL muss die folgenden Spalten enthalten: `user_id`, `$start_date` und eine Aggregationsfunktion (wie `COUNT`). Jedes SQL, das ohne diese drei Felder gespeichert wird, führt zu einem Fehler.
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

### Schritt 3: Vorschau der Abfrage anzeigen {#step-3-preview-the-query}

Bevor Sie speichern, können Sie eine Vorschau Ihrer Abfrage ausführen. Abfragevorschauen sind automatisch auf 100 Zeilen begrenzt und haben eine Zeitüberschreitung nach 60 Sekunden. Die Anforderung der `user_id`-Spalte gilt beim Ausführen einer Vorschau nicht.

Für inkrementelle SQL-Segmenterweiterungen enthält die Vorschau nicht die zusätzlichen Kriterien aus Ihren Operator-, Anzahl- und Zeitraumfeldern.

### Schritt 4: Bestimmen, ob SQL invertiert werden muss {#step-4-determine-if-you-need-to-invert-sql}

Bestimmen Sie als Nächstes, ob Sie SQL invertieren müssen. Obwohl es nicht möglich ist, direkt nach Nutzer:innen mit null Ereignissen zu suchen, können Sie **SQL invertieren** verwenden, um diese Nutzer:innen anzusprechen.

{% alert note %}
Standardmäßig ist **SQL invertieren** nicht aktiviert. Wenn Sie jedoch den KI-SQL-Generator verwenden, um eine SQL-Anweisung zu generieren, die negiert werden muss, kann ChatGPT eine Ausgabe zurückgeben, die dieses Feature automatisch aktiviert.
{% endalert %}

Um beispielsweise Nutzer:innen mit weniger als drei Käufen anzusprechen, schreiben Sie zunächst eine Abfrage, die Nutzer:innen mit drei oder mehr Käufen auswählt. Wählen Sie dann **SQL invertieren**, um Nutzer:innen mit weniger als drei Käufen (einschließlich derjenigen mit null Käufen) anzusprechen.

{% alert important %}
Sofern Sie nicht gezielt Nutzer:innen mit null Ereignissen ansprechen möchten, müssen Sie SQL nicht invertieren. Wenn **SQL invertieren** ausgewählt ist, bestätigen Sie, dass das Feature benötigt wird und dass das Segment Ihrer gewünschten Zielgruppe entspricht. Wenn eine Abfrage beispielsweise Nutzer:innen mit mindestens einem Ereignis anspricht, werden bei Invertierung nur Nutzer:innen mit null Ereignissen angesprochen.
{% endalert %}

![Segmenterweiterung mit dem Namen „Clicked 1-4 emails in the last 30 days“ mit aktivierter Option „SQL invertieren“.]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:90%;"}

## Aktualisierung der Segmentzugehörigkeit {#refreshing-segment-membership}

Um die Segmentzugehörigkeit einer Segmenterweiterung zu aktualisieren, die mit SQL erstellt wurde, öffnen Sie die Segmenterweiterung und wählen Sie **Aktualisieren** aus.

{% alert tip %}
Wenn Sie ein Segment erstellt haben, in das Nutzer:innen voraussichtlich regelmäßig eintreten und wieder austreten, aktualisieren Sie die verwendete Segmenterweiterung manuell, bevor Sie dieses Segment in einer Campaign oder einem Canvas als Zielgruppe verwenden.
{% endalert %}

## Verwalten Ihrer Segmenterweiterungen {#managing-your-segment-extensions}

Auf der Seite **Segmenterweiterungen** werden Segments, die mit SQL generiert wurden, mit <i class="fas fa-code" alt="SQL-Segmenterweiterung"></i> neben ihrem Namen gekennzeichnet.

Wählen Sie eine SQL-Segmenterweiterung aus, um anzuzeigen, wo die Erweiterung verwendet wird, die Erweiterung zu archivieren oder die [Segment-Mitgliedschaft manuell zu aktualisieren](#refreshing-segment-membership).

![Abschnitt „Messaging-Nutzung“ des SQL-Editors, der zeigt, wo das SQL-Segment verwendet wird.]({% image_buster /assets/img_archive/sql_segments_usage.png %}){: style="max-width:70%;"}

### Aktualisierungseinstellungen festlegen {#designating-refresh-settings}

{% multi_lang_include audience/segments.md section='Refresh settings' %}

## Snowflake-Credits {#credits}

Jeder Braze Workspace verfügt über 5 Snowflake-Credits pro Monat. Wenn Sie mehr Credits benötigen, wenden Sie sich an Ihren Account Manager. Credits werden immer dann verbraucht, wenn Sie die Mitgliedschaft eines SQL-Segments aktualisieren oder speichern und aktualisieren. Credits werden nicht verbraucht, wenn Sie Vorschauen innerhalb eines SQL-Segments ausführen oder eine klassische Segmenterweiterung speichern oder aktualisieren.

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

Wenn Sie mehr SQL-Segment-Credits oder zusätzliche Segmenterweiterungen erwerben möchten, wenden Sie sich bitte an Ihren Account Manager.