# SQL-Segmenterweiterungen {#sql-segment-extensions}

> Sie können eine Segmenterweiterung mithilfe von Snowflake-SQL-Abfragen von [Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)-Daten erstellen. SQL kann Ihnen helfen, neue Segmentierungs-Anwendungsfälle zu erschließen, da es die Flexibilität bietet, die Beziehungen zwischen Daten auf eine Weise zu beschreiben, die mit anderen Segmentierungs-Features nicht möglich ist.
>
> Wie bei Standard-Segmenterweiterungen können Sie in Ihrer SQL-Segmenterweiterung Events aus den letzten zwei Jahren (730 Tage) abfragen. Im Gegensatz zu Standard-Segmenterweiterungen [verbrauchen SQL-Segmenterweiterungen Credits](#credits).

## Voraussetzungen {#prerequisites}

Da es möglich ist, über dieses Feature auf PII-Daten zuzugreifen, müssen Sie über PII-Berechtigungen verfügen, um SQL-Segmentabfragen durchzuführen.

## Erstellen einer Segmenterweiterung {#creating-a-segment-extension}

### 1. Schritt: Wählen Sie einen Editor {#step-1-choose-an-editor}

Bei der Erstellung Ihrer SQL-Segmenterweiterung können Sie zwischen zwei Arten von SQL-Editoren wählen: dem SQL-Editor und dem inkrementellen SQL-Editor.

- **Vollständige Aktualisierung:** Jedes Mal, wenn Ihr Segment aktualisiert wird, fragt Braze alle verfügbaren Daten ab, um Ihr Segment zu aktualisieren, was mehr Credits verbraucht als inkrementelle Aktualisierungen. Erweiterungen mit vollständiger Aktualisierung können die Mitgliedschaft automatisch täglich erneuern, können aber nicht mit inkrementeller Aktualisierung aktualisiert werden.
- **Inkrementelle Aktualisierung:** Die inkrementelle Aktualisierung stellt eine kosteneffizientere Methode zur Einrichtung Ihrer Abfrage dar, erfordert jedoch einige zusätzliche [Schritte](#step-2-write-your-sql). Wenn Sie diese zusätzlichen Schritte beim Erstellen Ihres Segments ausführen können, empfiehlt es sich, diese Option zu wählen, da Ihre Abfrage dann mit weniger Credits ausgeführt wird.
- **KI-SQL-Generator:** Mit dem KI-SQL-Generator können Sie einen Prompt in einfacher Sprache schreiben und ihn in eine SQL-Abfrage für Ihr Segment umwandeln. So können Sie schnell loslegen, ohne selbst SQL schreiben zu müssen.

{% alert tip %}
Sie können alle SQL-Segmente, die in einem der beiden SQL-Editoren erstellt wurden, manuell vollständig aktualisieren.
{% endalert %}

{% tabs local %}
{% tab Full refresh %}

So erstellen Sie eine SQL-Segmenterweiterung mit vollständiger Aktualisierung:

1. Gehen Sie zu **Zielgruppe** > **Segmenterweiterungen**.
2. Wählen Sie **Neu erstellen** und dann **Vollständige Aktualisierung**.<br><br>
   ![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. Fügen Sie einen Namen für Ihre Segmenterweiterung hinzu und geben Sie Ihr SQL ein. Anforderungen und Ressourcen finden Sie in [Schritt 2](#step-2-write-your-sql).<br><br>
   ![SQL-Editor, der ein Beispiel für eine SQL-Segmenterweiterung anzeigt.]({% image_buster /assets/img_archive/sql_segments_editor.png %}){: style="max-width:60%" }<br><br>
4. Speichern Sie Ihre Segmenterweiterung.

{% endtab %}
{% tab Incremental refresh %}

So erstellen Sie eine SQL-Segmenterweiterung mit inkrementeller Aktualisierung:

1. Gehen Sie zu **Zielgruppe** > **Segmenterweiterungen**.
2. Wählen Sie **Neu erstellen** und dann **Inkrementelle Aktualisierung**.<br><br>
   ![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. Fügen Sie einen Namen für Ihre Segmenterweiterung hinzu und geben Sie Ihr SQL ein. Anforderungen und Ressourcen finden Sie im Abschnitt [SQL schreiben](#writing-sql).<br><br>
   ![SQL-Editor, der ein Beispiel für eine inkrementelle SQL-Segmenterweiterung anzeigt.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:60%" }<br><br>
4. Falls gewünscht, wählen Sie **Regenerate Extension Daily**.<br><br>
   ![Kontrollkästchen, um die Erweiterung täglich neu zu generieren.]({% image_buster /assets/img_archive/sql_segments_regenerate.png %}){: style="max-width:60%" }<br><br>
   Wenn Sie diese Option auswählen, aktualisiert Braze die Segmentmitgliedschaft jeden Tag automatisch. Das bedeutet, dass Braze jeden Tag um Mitternacht in der Zeitzone Ihres Unternehmens (mit einer möglichen Verzögerung von einer Stunde) nach neuen Nutzer:innen in Ihrem Segment sucht und diese automatisch zu Ihrem Segment hinzufügt. Wenn eine Segmenterweiterung 7 Tage lang nicht verwendet wurde, pausiert Braze automatisch die tägliche Regeneration. Eine ungenutzte Segmenterweiterung ist eine, die nicht Teil einer Campaign oder eines Canvas ist (die Campaign oder das Canvas muss nicht aktiv sein, damit die Erweiterung als „genutzt“ gilt).<br><br>
5. Speichern Sie Ihre Segmenterweiterung.

{% endtab %}

{% tab AI SQL Generator %}

{% alert note %}
Der KI-SQL-Generator ist derzeit als Beta-Feature verfügbar. Wenden Sie sich an Ihren Customer-Success-Manager, wenn Sie an der Teilnahme an diesem Betatest interessiert sind.
{% endalert %}

Der KI-SQL-Generator nutzt [GPT](https://openai.com/gpt-4), powered by OpenAI, um SQL-Empfehlungen für Ihr SQL-Segment zu geben.

![KI-SQL-Generator mit dem Prompt „Nutzer:innen, die im letzten Monat eine Benachrichtigung erhalten haben“]({% image_buster /assets/img/ai_sql_generator.png %}){: style="max-width:70%;"}

Um den KI-SQL-Generator zu verwenden, gehen Sie wie folgt vor:

1. Wählen Sie **Launch AI SQL Generator**, nachdem Sie ein [SQL-Segment]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) mit vollständiger oder inkrementeller Aktualisierung erstellt haben.
2. Geben Sie Ihren Prompt ein und wählen Sie **Generate**, um ihn in SQL zu übersetzen.
3. Überprüfen Sie das generierte SQL, um sicherzustellen, dass es korrekt aussieht, und speichern Sie dann Ihr Segment.

#### Beispiel-Prompts {#example-prompts}

- Nutzer:innen, die im letzten Monat eine E-Mail erhalten haben
- Nutzer:innen, die im letzten Jahr weniger als fünf Käufe getätigt haben

#### Tipps {#tips}

- Machen Sie sich mit den verfügbaren [Snowflake-Datentabellen]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) vertraut. Wenn Sie nach Daten fragen, die in diesen Tabellen nicht vorhanden sind, kann es sein, dass ChatGPT eine fiktive Tabelle erstellt.
- Machen Sie sich mit den [SQL-Schreibregeln]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments?tab=sql%20editor#writing-sql) für dieses Feature vertraut. Die Nichtbeachtung dieser Regeln führt zu einem Fehler. Zum Beispiel muss Ihr SQL-Code die Spalte `user_id` auswählen. Beginnen Sie Ihren Prompt mit „Nutzer:innen, die“, um bessere Ergebnisse zu erzielen.
- Mit dem KI-SQL-Generator können Sie bis zu 20 Prompts pro Minute senden.

##{% multi_lang_include brazeai/generative_ai/policy.md %}

{% endtab %}
{% endtabs %}

{% alert note %}
SQL-Anfragen, die länger als 20 Minuten dauern, werden abgebrochen.
{% endalert %}

Wenn die Verarbeitung der Erweiterung abgeschlossen ist, können Sie mit Ihrer Segmenterweiterung [ein Segment erstellen]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#step-5-use-your-extension-in-a-segment) und dieses neue Segment mit Ihren Campaigns und Canvases ansprechen.

### 2. Schritt: Schreiben Sie Ihr SQL {#step-2-write-your-sql}

Ihre SQL-Abfrage sollte in [Snowflake-Syntax](https://docs.snowflake.com/en/sql-reference.html) geschrieben sein. In der [Tabellenreferenz]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) finden Sie eine vollständige Liste der Tabellen und Spalten, die abgefragt werden können.

{% alert important %}
Beachten Sie, dass die zur Abfrage verfügbaren Tabellen nur Event-Daten enthalten. Wenn Sie nach Nutzerattributen suchen möchten, sollten Sie Ihr SQL-Segment mit angepassten Attributfiltern aus dem [klassischen Segmentierer]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) kombinieren.
{% endalert %}

{% tabs %}
{% tab SQL Editor %}

Ihr SQL muss zusätzlich die folgenden Regeln einhalten:

- Schreiben Sie eine einzelne SQL-Anweisung. Fügen Sie keine Semikolons ein.
- Ihr SQL darf nur eine Spalte auswählen: die Spalte `user_id`. Das bedeutet, dass Ihr SQL Folgendes enthalten muss:

```sql
SELECT DISTINCT user_id FROM "INSERT TABLE NAME"
```

- Es ist nicht möglich, Nutzer:innen mit null Events abzufragen. Das bedeutet, dass jede Abfrage nach Nutzer:innen, die ein Event weniger als X-mal durchgeführt haben, diesen Workaround befolgen muss:
   1. Schreiben Sie eine Abfrage, um Nutzer:innen auszuwählen, die das Event MEHR als X-mal durchgeführt haben.
   2. Wenn Sie Ihre Segmenterweiterung in Ihrem Segment referenzieren, wählen Sie `doesn't include`, um das Ergebnis zu invertieren.

#### Zusätzliche Regeln {#additional-rules}

Außerdem muss Ihre Standard-SQL-Abfrage die folgenden Regeln einhalten:

- Sie können keine `DECLARE`-Anweisungen verwenden.
{% endtab %}
{% tab Incremental SQL Editor %}

Alle inkrementellen Aktualisierungsabfragen bestehen aus zwei Teilen: einer Abfrage und Schemadetails.

1. Schreiben Sie im Editor eine Abfrage, die `user_id`s aus der gewünschten Tabelle auswählt.
2. Fügen Sie Schemadetails hinzu, indem Sie einen **Operator**, die **Anzahl der Male** und den **Zeitraum** aus den Feldern oberhalb des Editors auswählen. Die Abfrage prüft, ob die Summe der Aggregatspalte eine bestimmte Bedingung erfüllt, die durch die Platzhalter {% raw %}`{{operator}}` und `{{number of times}}`{% endraw %} angegeben ist. Dies funktioniert ähnlich wie der Arbeitsablauf zur Erstellung klassischer Segmenterweiterungen.<br><br>
   - **Operator:** Geben Sie an, ob das Event mehr als, weniger als oder gleich einer Anzahl von Vorkommen stattgefunden hat.<br>
   ![Operator-Feld mit der Auswahl „Mehr als“.]({% image_buster /assets/img_archive/sql_segments_operator.png %})<br><br>
   - **Anzahl der Male:** Wie oft Sie das Event in Bezug auf den Operator auswerten möchten.<br>
   ![Feld „Anzahl der Male“ mit der Eingabe „5“.]({% image_buster /assets/img_archive/sql_segments_times.png %})<br><br>
   - **Zeitraum:** Anzahl der Tage von 1 bis 730, in denen Sie Instanzen des Events überprüfen möchten. Dieser Zeitraum bezieht sich auf vergangene Tage relativ zum aktuellen Tag. Das folgende Beispiel zeigt die Abfrage nach Nutzer:innen, die das Event in den letzten 365 Tagen mehr als 5 Mal durchgeführt haben.<br>
   ![Zeitraum-Feld mit der Eingabe „365“.]({% image_buster /assets/img_archive/sql_segments_period.png %})

Im folgenden Beispiel würde das resultierende Segment Nutzer:innen enthalten, die das Event `favorited` mehr als 3 Mal in den letzten 30 Tagen nach einem bestimmten Datum durchgeführt haben.

![SQL-Editor, der ein Beispiel für eine inkrementelle SQL-Segmenterweiterung anzeigt.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:65%" }

![SQL-Vorschau einer inkrementellen SQL-Segmenterweiterung.]({% image_buster /assets/img_archive/sql_segments_incremental_preview.png %}){: style="max-width:85%" }

{% alert tip %}
Segmente mit inkrementeller Aktualisierung berücksichtigen späte Events, d. h. Events, die mehr als 2 Tage zurückliegen (z. B. SDK-Events, die zum Zeitpunkt ihrer Erfassung noch nicht gesendet wurden).
{% endalert %}

#### Zusätzliche Regeln

Außerdem muss Ihre Abfrage zur inkrementellen Aktualisierung die folgenden Regeln einhalten:

- Schreiben Sie eine einzelne SQL-Anweisung. Fügen Sie keine Semikolons ein.
- Ihr inkrementelles SQL-Segment kann sich nur auf ein einziges Event beziehen. Ihre Dropdowns für Datum und Anzahl beziehen sich auf das von Ihnen gewählte Event.
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

### 3. Schritt: Vorschau der Abfrage {#step-3-preview-the-query}

Vor dem Speichern können Sie eine Vorschau Ihrer Abfrage ausführen. Abfragevorschauen sind automatisch auf 100 Zeilen begrenzt und werden nach 60 Sekunden abgebrochen. Die Anforderung der Spalte `user_id` gilt nicht, wenn Sie eine Vorschau ausführen.

Bei inkrementellen SQL-Segmenterweiterungen enthält die Vorschau nicht die zusätzlichen Kriterien aus Ihren Feldern für Operator, Anzahl der Male und Zeitraum.

### 4. Schritt: Prüfen Sie, ob Sie SQL invertieren müssen {#step-4-determine-if-you-need-to-invert-sql}

Als Nächstes sollten Sie feststellen, ob Sie SQL invertieren müssen. Es ist zwar nicht möglich, direkt nach Nutzer:innen mit null Events zu suchen, jedoch können Sie **Invert SQL** verwenden, um diese Nutzer:innen anzusprechen.

{% alert note %}
Standardmäßig ist **Invert SQL** nicht aktiviert. Wenn Sie jedoch den KI-SQL-Generator verwenden, um eine SQL-Anweisung zu generieren, die negiert werden muss, könnte ChatGPT eine Ausgabe zurückgeben, die dieses Feature automatisch aktiviert.
{% endalert %}

Um beispielsweise Nutzer:innen anzusprechen, die weniger als drei Käufe getätigt haben, erstellen Sie zunächst eine Abfrage, um Nutzer:innen auszuwählen, die drei oder mehr Käufe getätigt haben. Wählen Sie anschließend **Invert SQL**, um Nutzer:innen mit weniger als drei Käufen (einschließlich derjenigen mit null Käufen) anzusprechen.

{% alert important %}
Sofern Sie nicht gezielt Nutzer:innen mit null Events ansprechen möchten, ist es nicht erforderlich, SQL zu invertieren. Wenn **Invert SQL** ausgewählt ist, vergewissern Sie sich, dass das Feature erforderlich ist und dass das Segment Ihrer gewünschten Zielgruppe entspricht. Wenn eine Abfrage beispielsweise auf Nutzer:innen mit mindestens einem Event abzielt, wird sie bei einer Invertierung nur auf Nutzer:innen mit null Events angewendet.
{% endalert %}

![Segmenterweiterung mit dem Namen „1–4 E-Mails in den letzten 30 Tagen angeklickt“ mit der Option „SQL invertieren“ ausgewählt.]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:90%;"}

## Segmentmitgliedschaft aktualisieren {#refreshing-segment-membership}

Um die Segmentmitgliedschaft einer mit SQL erstellten Segmenterweiterung zu aktualisieren, öffnen Sie die Segmenterweiterung und wählen Sie **Refresh**.

{% alert tip %}
Wenn Sie ein Segment erstellt haben, bei dem Sie erwarten, dass Nutzer:innen regelmäßig ein- und austreten, aktualisieren Sie die verwendete Segmenterweiterung manuell, bevor Sie dieses Segment in einer Campaign oder einem Canvas ansprechen.
{% endalert %}

## Verwalten Ihrer Segmenterweiterungen {#managing-your-segment-extensions}

Auf der Seite **Segmenterweiterungen** sind Segmente, die mit SQL generiert wurden, mit <i class="fas fa-code" alt="SQL-Segmenterweiterung"></i> neben ihrem Namen gekennzeichnet.

Wählen Sie eine SQL-Segmenterweiterung aus, um zu sehen, wo die Erweiterung verwendet wird, die Erweiterung zu archivieren oder die [Segmentmitgliedschaft manuell zu aktualisieren](#refreshing-segment-membership).

![Der Abschnitt „Messaging-Verwendung“ des SQL-Editors zeigt an, wo das SQL-Segment verwendet wird.]({% image_buster /assets/img_archive/sql_segments_usage.png %}){: style="max-width:70%;"}

### Festlegen der Aktualisierungseinstellungen {#designating-refresh-settings}

{% multi_lang_include segments.md section='Refresh settings' %}

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