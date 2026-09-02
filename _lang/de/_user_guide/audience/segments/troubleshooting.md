---
nav_title: Fehlerbehebung
article_title: Fehlerbehebung für Segmente
page_order: 9
page_type: reference
tool:
  - Segments
description: "Dieser Referenzartikel behandelt die Fehlerbehebung für Segmentfehler, Nutzereignung, Filterprobleme und Analytics-Abweichungen. Filterdefinitionen finden Sie unter Segmentierungsfilter. Informationen zu Segmentgrößenschätzungen und exakten Zählungen finden Sie unter Segmentgröße messen."
---

# Fehlerbehebung für Segmente {#troubleshoot-segments}

> Ordnen Sie Ihr Symptom in der folgenden Liste zu, um den richtigen Abschnitt zu finden. Diese Seite behandelt Startfehler, Nutzereignung, Filterprobleme und Analytics-Abweichungen. Filterdefinitionen finden Sie unter [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters). Informationen zu Segmentgrößenschätzungen, exakten Zählungen und historischen Mitgliedschaftsdiagrammen finden Sie unter [Segmentgröße messen]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size).

## Hier starten: Symptom zuordnen {#start-here-match-your-symptom}

| Symptom | Gehe zu |
|---------|-------|
| Zielgruppe ist zu komplex | [Zielgruppe ist zu komplex zum Starten](#target-audience-is-too-complex-to-launch) |
| Filter lässt sich nicht speichern | [Filter überschreitet 10.000 Bytes](#filter-exceeds-10000-bytes-or-is-too-long-to-save) |
| Segment hat keine Nutzer:innen | [Segment zeigt null Nutzer:innen an](#segment-shows-zero-users) |
| Nutzer:in nicht im Segment | [Standardmäßiger Untersuchungspfad](#standard-investigation-path) |
| Segment ist größer als erwartet | [Segment ist deutlich größer als erwartet](#segment-is-much-larger-than-expected) |
| Segment-Anzahl stimmt nicht mit Campaign-Analytics überein | [Abweichung bei *Gesendete Nachrichten* oder *Eindeutige Empfänger:innen*](#message-sent-or-unique-recipients-in-campaign-analytics-doesnt-match-segment-count) |
| Filteroptionen haben sich geändert | [Filteroptionen haben sich geändert](#filter-options-changed) |
| Verschachteltes angepasstes Attribut nicht als Filter verfügbar | [Verschachteltes angepasstes Attribut nicht als Filteroption verfügbar](#nested-custom-attribute-not-available-as-a-filter-option) |
| Nutzer:in in falscher App | [Informationen werden für Nutzer:innen anderer Apps angezeigt](#info-displays-for-users-of-other-apps-when-i-filter-for-a-specific-app) |
| War eine:r Nutzer:in zu einem früheren Zeitpunkt in diesem Segment? | [Rückwirkende Segment-Zugehörigkeit](#retroactive-segment-membership) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Hier starten: Symptom zuordnen" }

## Standardmäßiger Untersuchungspfad {#standard-investigation-path}

Verwenden Sie diesen Workflow, wenn eine:r Nutzer:in in einem Segment sein sollte, aber nicht enthalten ist, oder wenn die Segment-Anzahl falsch aussieht.

1. **Start blockiert:** Wenn bei einer Campaign oder einem Canvas ein Fehler zur Zielgruppenkomplexität oder ein 10.000-Byte-Filterfehler angezeigt wird, beginnen Sie mit [Fehler](#errors) (CSV-Workaround, Filter-Vereinfachung).
2. **Nutzer:innen-Vorschau oder Nutzer:innen-Suche:** Testen Sie eine:n bestimmte:n Nutzer:in anhand Ihrer Segment-Filter. Wenn eine:r Nutzer:in einen Teil der Kriterien oder alle Kriterien nicht erfüllt, werden die fehlenden Kriterien zur Fehlerbehebung aufgelistet. Schritte finden Sie unter [Segments testen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments) in „Segment erstellen“.
3. **Exakte Statistiken berechnen:** Wenn die Segment-Schätzung 0 Nutzer:innen anzeigt oder falsch erscheint, wählen Sie **Exakte Statistiken berechnen** im Panel **Erreichbare Nutzer:innen** aus. Speichern Sie Ihr Segment vor der Berechnung. Wenn bereits eine Berechnung läuft, warten Sie, bis sie abgeschlossen ist; veraltete Zahlen werden möglicherweise angezeigt, bis die neue Berechnung abgeschlossen ist. Einzelheiten finden Sie unter [Exakte Statistiken berechnen]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#calculating-exact-statistics).
4. **Filterwerte prüfen:** Achten Sie auf Tippfehler, Datentyp-Inkompatibilitäten, veraltete Canvas-Schritt-Referenzen und [negativer Filter + ODER-Logik](#segment-is-much-larger-than-expected).
5. **Komplexität prüfen:** Wenn der Start blockiert ist, siehe [Zielgruppe ist zu komplex für den Start](#target-audience-is-too-complex-to-launch).
6. **Support kontaktieren:** Wenn Sie weiterhin blockiert sind, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support).

## Segment zeigt null Nutzer:innen an {#segment-shows-zero-users}

Die Segmentgröße im Dashboard basiert häufig auf einer Schätzung anhand einer Stichprobe von Nutzer:innen. Sehr kleine Segmente können einen geschätzten Bereich anzeigen, der 0 einschließt, selbst wenn Nutzer:innen Ihren Filtern entsprechen.

- Wählen Sie **Exakte Statistiken berechnen** im Panel **Erreichbare Nutzer:innen** aus, um eine genaue Anzahl zu erhalten. Speichern Sie das Segment zuerst. Weitere Informationen finden Sie unter [Hinweise zu Schätzwerten]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#considerations-for-estimate-counts).
- Wenn die **Nutzervorschau** bei einem kleinen Segment null Nutzer:innen zurückgibt, bedeutet das nicht zwangsläufig, dass das Segment leer ist. Führen Sie **Exakte Statistiken berechnen** aus, um dies zu bestätigen. Weitere Informationen finden Sie unter [Nutzervorschau]({{site.baseurl}}/user_guide/audience/segments/segment_data#user-preview).

## Rückwirkende Segmentzugehörigkeit {#retroactive-segment-membership}

Braze speichert keine historische Segmentzugehörigkeit pro Nutzer:in. Sie können nicht nachschlagen, ob eine:r bestimmte:r Nutzer:in zu einem vergangenen Sendezeitpunkt in einem Segment war.

Um die Zugehörigkeit zu einem bestimmten Zeitpunkt festzuhalten, exportieren Sie Nutzer:innen aus dem Segment im Dashboard oder rufen Sie den Endpunkt [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) auf, bevor Sie eine Campaign oder ein Canvas senden. Weitere Informationen finden Sie unter [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) (Filter für Segmentzugehörigkeit) und [Segmentdaten als CSV exportieren]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv).

## Fehler {#errors}

### Zielgruppe ist zu komplex zum Starten {#target-audience-is-too-complex-to-launch}

Dieser seltene Fehler tritt auf, wenn Ihre Zielgruppe zu viele Regex-Werte, übermäßig lange Regex-Werte, übermäßig detaillierte Filter (z. B. „ist einer von 30.000 Postleitzahlen“) oder zu viele Filter enthält. Dies umfasst alle Filter in einer Campaign- oder Canvas-Zielgruppe, unabhängig davon, ob sich die Filter innerhalb der referenzierten Segmente befinden oder als Filter im Schritt **Target Audience** hinzugefügt wurden.

![Fehler für eine Zielgruppe, die den Komplexitätsschwellenwert überschreitet.]({% image_buster /assets/img/segment/target_audience_too_complex_error.png %})

Wenn Sie Segment-Filter zu einer Campaign oder einem Canvas hinzufügen, werden diese Filter in Abfragen in Braze übersetzt (die Zeichenanzahl dieser Abfragen entspricht nicht 1:1 der Zeichenanzahl, die Nutzer:innen im Dashboard sehen). Wenn Braze eine Campaign oder ein Canvas sendet, wird eine Abfrage ausgeführt, die alle Filter der Zielgruppe kombiniert. Wir wenden einen Schwellenwert an, der die Anzahl der Zeichen in der resultierenden Abfrage für eine Zielgruppe begrenzt. Für eine bestimmte Campaign oder ein bestimmtes Canvas wird die Zeichenanzahl über alle referenzierten Segmente hinweg summiert, einschließlich aller zusätzlichen Filter. Für ein bestimmtes Segment wird die Zeichenanzahl über alle Filter und Filterwerte hinweg summiert.

Ihr Dashboard zeigt einen Fehler an, wenn eine Campaign, ein Canvas oder ein Segment den Schwellenwert überschreitet und nicht gestartet werden kann. Wenn Sie diesen Fehler erhalten, vereinfachen Sie Ihre Zielgruppe vor dem erneuten Starten, einschließlich:

- Wenn Ihre Zielgruppe mehrere Segmente referenziert, stellen Sie sicher, dass die Segmente keine Redundanzen aufweisen, z. B. dieselben Filter in mehreren Segmenten.
- Stellen Sie sicher, dass Sie in Segment-Filtern nicht auf veraltete Daten verweisen. Beispielsweise könnte ein veralteter Filter nach Nutzer:innen suchen, die in der letzten Woche einen bestimmten Canvas-Schritt nicht erhalten haben, obwohl das Canvas seit Monaten gestoppt ist.
- Segmente, die nur Listen von Nutzer-IDs oder E-Mail-Adressen sind (die oft einen Regex-Filter verwenden), können in einen [CSV-Import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) umgewandelt und zu einem einzelnen CSV-Filter vereinfacht werden.
- Wenn Sie CDI verwenden, können Sie möglicherweise ein CDI-Segment erstellen, das die Gruppe direkt aus Ihrem Data Warehouse abruft.

Sie können auch den [Support kontaktieren]({{site.baseurl}}/user_guide/administer/personal/braze_support), um weitere Unterstützung bei der Filter-Optimierung zu erhalten.

{% alert note %}
Wir haben im April 2025 begonnen, Zeichenanzahlen zu begrenzen. Campaigns und Canvases, die vor April 2025 gestartet wurden, waren davon ausgenommen, d. h. sie können den Grenzwert weiterhin überschreiten, während neu erstellte Campaigns und Canvases den Grenzwert nicht überschreiten können. Wenn Sie eine ausgenommene Campaign oder ein ausgenommenes Canvas bearbeiten oder Klon, können Sie es nicht starten, bis die Zielgruppe so aktualisiert wurde, dass sie unter dem Grenzwert liegt.
{% endalert %}

### X aktive oder gestoppte Campaigns oder Canvases überschreiten den Schwellenwert für die Zielgruppenkomplexität {#x-active-or-stopped-campaigns-or-canvases-exceed-the-audience-complexity-threshold}

Dieses Banner wird oben in einer Campaign- oder Canvas-Liste angezeigt, wenn aktive oder gestoppte Campaigns oder Canvases Zielgruppen haben, die den Schwellenwert für die Zielgruppenkomplexität überschreiten. Wählen Sie das Banner aus, um die Liste auf die Campaigns oder Canvases zu filtern, die den Schwellenwert überschreiten, und befolgen Sie dann die Schritte zur Fehlerbehebung unter [Zielgruppe ist zu komplex zum Starten](#target-audience-is-too-complex-to-launch).

![Fehlerbanner mit dem Hinweis, dass 4 aktive oder gestoppte Canvases den Schwellenwert für die Zielgruppenkomplexität überschreiten.]({% image_buster /assets/img/segment/audience_complexity_threshold_banner.png %})

### Filter überschreitet 10.000 Bytes oder ist zu lang zum Speichern {#filter-exceeds-10000-bytes-or-is-too-long-to-save}

Braze begrenzt einzelne Segment-Filter auf maximal 10.000 Bytes, was 10.000 englischen Zeichen oder 3.333 japanischen Zeichen entspricht. Eine Warnung wird angezeigt, wenn ein einzelner Filter 10.000 Bytes überschreitet, unabhängig davon, ob sich der Filter innerhalb eines Segments befindet oder direkt zu einer Campaign oder einem Canvas hinzugefügt wurde.

![Fehlerbanner für einen Filter, dessen Wert 10.000 Zeichen überschreitet.]({% image_buster /assets/img/segment/filter_error.png %})

![Fehler für einen Filter mit angepasstem Attribut „menu_item“, dessen Attributwert 10.000 Zeichen überschreitet.]({% image_buster /assets/img/segment/segment_filter_error.png %})

Dieser Fehler tritt sehr selten auf, aber wenn er auftritt, betrifft er typischerweise Regex-Filter, die eine Liste von Nutzer-IDs oder E-Mail-Adressen als Ziel haben. In diesem Fall können Sie die folgenden Schritte befolgen, um die Filter in eine CSV-Datei umzuwandeln:

1. Exportieren Sie die Nutzer:innen aus dem betroffenen Segment oder dem spezifischen Regex-Filter.
2. Bereinigen Sie die CSV-Datei nach Bedarf. Sie benötigen entweder die Braze-ID oder die Appboy-ID, aber Sie können alle anderen Spalten entfernen, wenn sie nicht benötigt werden. Wir empfehlen außerdem, Ihre Daten zu überprüfen, um sicherzustellen, dass sie aktuell sind (entfernen Sie beispielsweise Nutzer:innen, die Sie nicht mehr ansprechen möchten).
3. [Importieren]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) Sie die CSV-Datei erneut, wodurch die Nutzer:innen automatisch in einen einzelnen, hocheffizienten CSV-basierten Filter gruppiert werden.

## Nutzer:innenverhalten {#user-behavior}

### Nutzer:in ist nicht mehr in einem Segment {#user-is-no-longer-in-a-segment}

Wenn eine:r Nutzer:in beim Erstellen eines Segments nicht verfügbar ist, haben sich möglicherweise die Nutzerdaten, die die Segment-Zugehörigkeit bestimmen, durch eigene Aktivitäten oder andere Campaigns und Canvases geändert, mit denen sie zuvor interagiert haben. Wenn die erneute Berechtigung aktiviert ist, zeigt das Kundenprofil die aktuellsten Daten der empfangenen Campaign an.

Um zu testen, ob eine:r bestimmte:r Nutzer:in heute Ihrem Segment entspricht, verwenden Sie die [Nutzer:innenvorschau oder Nutzer:innensuche]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments).

### Informationen zu Nutzer:innen anderer Apps werden angezeigt, wenn ich nach einer bestimmten App filtere {#info-displays-for-users-of-other-apps-when-i-filter-for-a-specific-app}

Nutzer:innen können mehrere Apps verwenden. Wenn Sie eine bestimmte App im Bereich **Apps Used** der Segmentierungsseite auswählen, werden Ergebnisse für Nutzer:innen angezeigt, die mindestens diese App haben. Der Filter liefert keine Ergebnisse für Nutzer:innen, die ausschließlich diese App verwenden.

## Filtern {#filtering}

### Filteroptionen haben sich geändert {#filter-options-changed}

Ihre Filteroptionen hängen mit dem Format (Datentyp) zusammen, das Sie für Ihre angepassten Attribute an Braze übergeben. Um den Datentyp zu überprüfen, den Braze für Ihre angepassten Attribute erkennt, navigieren Sie zu **Dateneinstellungen** > **Angepasste Attribute**.

Wenn sich Ihre Filteroptionen geändert haben, deutet dies darauf hin, dass Ihre Daten in einem anderen Format (Datentyp) als zuvor an Braze übergeben werden. Ausführliche Beschreibungen der verschiedenen Datentypen und ihrer Filteroptionen finden Sie unter [Datentypen für angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types).

Beachten Sie, dass eine Änderung des Datentyps eines angepassten Attributs im Dashboard dazu führt, dass Daten, die in einem anderen Format an Braze gesendet werden, abgelehnt werden. Sie können den Datentyp eines angepassten Attributs nicht ändern, solange dieses Attribut in aktiven Campaigns, Canvases oder Segments referenziert wird. Das Dashboard zeigt einen Fehler an und blockiert die Änderung.

Der Tab **Werte** eines angepassten Attributs zeigt Ergebnisse aus einer Stichprobe von etwa 250.000 Nutzer:innen. Verwenden Sie den Tab **Werte** nicht, um zur Fehlerbehebung zu prüfen, ob ein bestimmter Attributwert vorhanden ist. Weitere Informationen finden Sie unter [Tab „Werte“]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#values-tab).

### Verschachteltes angepasstes Attribut ist nicht als Filteroption verfügbar {#nested-custom-attribute-not-available-as-a-filter-option}

Wenn Ihr verschachteltes angepasstes Attribut beim Erstellen eines Segments nicht als Filteroption angezeigt wird, generieren Sie zuerst dessen Schema. Navigieren Sie zu **Dateneinstellungen** > **Angepasste Attribute**, suchen Sie das Attribut und wählen Sie **Schema generieren** aus. Sobald das Schema generiert wurde, steht das Attribut im Segment-Filter-Dropdown zur Verfügung. Weitere Informationen finden Sie unter [Schema mit dem verschachtelten Objekt-Explorer generieren]({{site.baseurl}}/user_guide/audience/segments/segment_with_nested_custom_attributes#generate-schema).

### Segment ist viel größer als erwartet {#segment-is-much-larger-than-expected}

Wenn Ihr Segment trotz restriktiv wirkender Filter viel größer aussieht als erwartet, prüfen Sie, ob Sie negative Filter (`ist nicht`, `ist nicht gleich`, `stimmt nicht mit Regex überein` oder `nicht enthalten`) mit dem **ODER**-Operator für dasselbe Attribut mehrfach verwenden. Diese Kombination kann dazu führen, dass Nutzer:innen mit allen Werten für das Attribut in die Zielgruppe aufgenommen werden.

Hinweise dazu, wann Sie **UND** anstelle von **ODER** verwenden sollten, finden Sie unter [Wann der ODER-Operator vermieden werden sollte]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#segmentation-logic-using-and-and-or) im Abschnitt „Segment erstellen“.

## Analytics und Reporting {#analytics-and-reporting}

### *Gesendete Nachrichten* oder *Eindeutige Empfänger:innen* in Campaign Analytics stimmen nicht mit der Segmentanzahl überein {#message-sent-or-unique-recipients-in-campaign-analytics-doesnt-match-segment-count}

Wenn die Anzahl der *gesendeten Nachrichten* oder *eindeutigen Empfänger:innen* in Ihren Campaign Analytics nicht mit der Anzahl der Nutzer:innen im Segmentfilter `Has received message from campaign X` übereinstimmt, kann das drei mögliche Gründe haben.

1. **Nutzer:innen wurden seit dem Campaign-Start möglicherweise archiviert, verwaist oder gelöscht**<br><br>Angenommen, 1.000 Nutzer:innen erhalten eine Campaign und Sie erstellen am selben Tag einen CSV-Export. Sie sehen 1.000 Nutzer:innen im Bericht. Im nächsten Monat werden 50 dieser 1.000 Nutzer:innen gelöscht (zum Beispiel über den Endpunkt `users/delete`). Wenn Sie einen weiteren CSV-Export erstellen, sehen Sie 950 Nutzer:innen im Bericht, während die Anzahl der *eindeutigen Empfänger:innen* in **Campaign Analytics** weiterhin 1.000 beträgt.<br><br>Mit anderen Worten: Die Metrik *Eindeutige Empfänger:innen* ist ein inkrementeller Zähler, während der Segmentierer und der CSV-Export die Anzahl der aktuell vorhandenen Nutzer:innen liefern.<br><br>

2. **Für die Campaign ist eine erneute Berechtigung eingestellt, sodass Nutzer:innen die Campaign mehrfach durchlaufen können**<br><br>Angenommen, eine E-Mail-Campaign hat die erneute Berechtigung auf null Minuten eingestellt (Nutzer:innen können die Campaign erneut durchlaufen, solange sie die Zielgruppen-Segment-Anforderungen erfüllen) und die Campaign läuft seit über einem Monat. Die Anzahl der *gesendeten Nachrichten* in **Campaign Analytics** würde nicht mit der Anzahl im Segment übereinstimmen, da dieses Feld auch Nachrichten enthält, die an doppelte Nutzer:innen gesendet wurden.<br><br>Das liegt daran, dass Braze eindeutige Nutzer:innen als *Eindeutige tägliche Empfänger:innen* zählt, also die Anzahl der Nutzer:innen, die eine bestimmte Nachricht an einem Tag erhalten haben. Das bedeutet, dass erneut berechtigte Nutzer:innen mehr als einmal als eindeutige:r Empfänger:in gezählt werden, da das „Eindeutigkeits“-Fenster nur einen Tag umfasst. Dies kann dazu führen, dass die Anzahl der *eindeutigen täglichen Empfänger:innen* höher ist als die Anzahl der Nutzerprofile im CSV-Export. Die Nutzerprofile in der CSV-Datei sind tatsächlich eindeutig.<br><br>

3. **Nutzer:innen, die einen Kanalbezeichner teilen, haben den Filter erfüllt**<br><br>Der Filter `Has received message from campaign X` (und andere „Empfangen“-Filter) kann Nutzer:innen zuordnen, die einen Kanalbezeichner teilen – zum Beispiel dasselbe Push-Token / Textbaustein oder dieselbe E-Mail-Adresse – mit einem anderen Kundenprofil, das die Nachricht empfangen, geöffnet oder angeklickt hat.

### Nutzer:in wird zwei Apps zugeordnet, obwohl nur in einer App eine Sitzung protokolliert wurde {#user-is-assigned-to-two-apps-despite-logging-a-session-in-only-one-app}

Beim Erstellen eines Segments können Sie Nutzer:innen ansprechen, die [bestimmte Apps genutzt haben]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#step-3-choose-your-app-or-platform). Eine:r Nutzer:in muss eine Sitzung in einer bestimmten App gehabt haben, um dieser App zugeordnet zu werden. Es gibt jedoch zwei Szenarien, in denen eine:r Nutzer:in einer bestimmten App zugeordnet werden kann, ohne dort Sitzungen protokolliert zu haben.

Das erste Szenario ist, wenn das Feld `app_id` bei der Verwendung des Endpunkts `/users/track` befüllt wird – insbesondere bei der Verwendung eines [Event-Objekts]({{site.baseurl}}/api/objects_filters/event_object) oder [Kauf-Objekts]({{site.baseurl}}/api/objects_filters/purchase_object), wie in diesem Beispiel:

```json
{
    "events": [
    {
      "external_id": "john_doe123",
      "app_id": "my_web_app_id",
      "name": "Custom Event",
      "time": "2025-08-17T19:20:30+1:00"
    }
  ]
}
```

Das zweite Szenario ist, wenn das Feld `app_id` bei der Verwendung des Endpunkts `/users/track` zum Migrieren von Push-Tokens befüllt wird, wie in diesem Beispiel:

```json
{
"app_group_id": "{YOUR_APP_GROUP_ID}",
"attributes": [
{
      "push_token_import": false,
      "external_id": "external_id1",
      "country": "US",
      "language": "en",
      "{YOUR_CUSTOM_ATTRIBUTE}": "{YOUR_VALUE}",
      "push_tokens": [
        {"app_id": "{APP_ID_OF_OS}", "token": "{PUSH_TOKEN_STRING}"}
      ]
  }
]
}
```
