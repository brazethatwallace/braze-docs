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
| Segment ist größer als erwartet | [Segment ist viel größer als erwartet](#segment-is-much-larger-than-expected) |
| Segmentanzahl stimmt nicht mit Campaign Analytics überein | [*Gesendete Nachrichten* oder *Eindeutige Empfänger:innen* – Abweichung](#message-sent-or-unique-recipients-in-campaign-analytics-doesnt-match-segment-count) |
| Filteroptionen haben sich geändert | [Filteroptionen haben sich geändert](#filter-options-changed) |
| Nutzer:in in falscher App | [Informationen werden für Nutzer:innen anderer Apps angezeigt](#info-displays-for-users-of-other-apps-when-i-filter-for-a-specific-app) |
| War ein:e Nutzer:in zu einem vergangenen Zeitpunkt in diesem Segment? | [Rückwirkende Segmentzugehörigkeit](#retroactive-segment-membership) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Hier starten: Symptom zuordnen" }

## Standardmäßiger Untersuchungspfad {#standard-investigation-path}

Verwenden Sie diesen Workflow, wenn ein:e Nutzer:in in einem Segment sein sollte, es aber nicht ist, oder wenn eine Segmentanzahl falsch aussieht.

1. **Start blockiert:** Wenn Sie einen Fehler wegen Zielgruppenkomplexität oder 10.000-Byte-Filter bei einer Campaign oder einem Canvas sehen, beginnen Sie mit [Fehler](#errors) (CSV-Workaround, Filtervereinfachung).
2. **Nutzervorschau oder Nutzersuche:** Testen Sie eine:n bestimmte:n Nutzer:in gegen Ihre Segmentfilter. Wenn ein:e Nutzer:in einen Teil oder alle Kriterien nicht erfüllt, werden die fehlenden Kriterien zur Fehlerbehebung aufgelistet. Die Schritte finden Sie unter [Segmente testen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments) in „Segment erstellen“.
3. **Exakte Statistiken berechnen:** Wenn die Segmentschätzung 0 Nutzer:innen anzeigt oder falsch erscheint, wählen Sie **Exakte Statistiken berechnen** im Panel **Erreichbare Nutzer:innen**. Speichern Sie Ihr Segment vor der Berechnung. Wenn bereits eine Berechnung läuft, warten Sie, bis sie abgeschlossen ist; veraltete Zahlen können angezeigt werden, bis die neue Berechnung abgeschlossen ist. Weitere Informationen finden Sie unter [Exakte Statistiken berechnen]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#calculating-exact-statistics).
4. **Filterwerte überprüfen:** Achten Sie auf Tippfehler, Datentyp-Abweichungen, veraltete Canvas-Schritt-Referenzen und [negative Filter + OR-Logik](#segment-is-much-larger-than-expected).
5. **Komplexität prüfen:** Wenn der Start blockiert ist, siehe [Zielgruppe ist zu komplex zum Starten](#target-audience-is-too-complex-to-launch).
6. **Support kontaktieren:** Wenn Sie weiterhin blockiert sind, kontaktieren Sie den [Braze-Support]({{site.baseurl}}/braze_support).

## Segment zeigt null Nutzer:innen an {#segment-shows-zero-users}

Die Segmentgröße im Dashboard ist oft eine Schätzung basierend auf einer Stichprobe von Nutzer:innen. Sehr kleine Segmente können einen geschätzten Bereich anzeigen, der 0 einschließt, selbst wenn Nutzer:innen Ihren Filtern entsprechen.

- Wählen Sie **Exakte Statistiken berechnen** im Panel **Erreichbare Nutzer:innen** für eine genaue Zählung. Speichern Sie das Segment zuerst. Weitere Informationen finden Sie unter [Hinweise zu geschätzten Zählungen]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#considerations-for-estimate-counts).
- Wenn die **Nutzervorschau** für ein kleines Segment null Nutzer:innen zurückgibt, bedeutet das nicht unbedingt, dass das Segment leer ist. Führen Sie **Exakte Statistiken berechnen** aus, um dies zu bestätigen. Weitere Informationen finden Sie unter [Nutzervorschau]({{site.baseurl}}/user_guide/audience/segments/segment_data#user-preview).

## Rückwirkende Segmentzugehörigkeit {#retroactive-segment-membership}

Braze speichert keine historische Segmentzugehörigkeit pro Nutzer:in. Sie können nicht nachschlagen, ob ein:e bestimmte:r Nutzer:in zum Zeitpunkt eines vergangenen Versands in einem Segment war.

Um die Zugehörigkeit zu einem bestimmten Zeitpunkt zu erfassen, exportieren Sie Nutzer:innen aus dem Segment im Dashboard oder rufen Sie den Endpunkt [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) auf, bevor Sie eine Campaign oder ein Canvas senden. Weitere Informationen finden Sie unter [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) (Segmentzugehörigkeitsfilter) und [Segmentdaten als CSV exportieren]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv).

## Fehler {#errors}

### Zielgruppe ist zu komplex zum Starten {#target-audience-is-too-complex-to-launch}

Dieser seltene Fehler tritt auf, wenn Ihre Zielgruppe zu viele Regex-Werte, übermäßig lange Regex-Werte, übermäßig detaillierte Filter (z. B. „ist einer von 30.000 Postleitzahlen“) oder zu viele Filter enthält. Dies umfasst alle Filter in einer Campaign- oder Canvas-Zielgruppe, unabhängig davon, ob sich die Filter in den referenzierten Segmenten befinden oder als Filter im Schritt **Zielgruppe** hinzugefügt wurden.

![Fehler für eine Zielgruppe, die den Komplexitätsschwellenwert überschreitet.]({% image_buster /assets/img/segment/target_audience_too_complex_error.png %})

Wenn Sie Segmentfilter zu einer Campaign oder einem Canvas hinzufügen, werden diese Filter in Abfragen in Braze übersetzt (die Zeichenanzahl dieser Abfragen entspricht nicht 1:1 der Anzahl der Zeichen, die ein:e Dashboard-Nutzer:in sieht). Wenn Braze eine Campaign oder ein Canvas sendet, wird eine Abfrage ausgeführt, die alle Filter in der Zielgruppe kombiniert. Wir wenden einen Schwellenwert an, der die Anzahl der Zeichen in der resultierenden Abfrage für eine Zielgruppe begrenzt. Für eine bestimmte Campaign oder ein bestimmtes Canvas summieren wir die Zeichenanzahl über alle referenzierten Segmente hinweg, einschließlich aller zusätzlichen Filter. Für ein bestimmtes Segment summieren wir die Zeichenanzahl über alle Filter und Filterwerte hinweg.

Ihr Dashboard zeigt einen Fehler an, wenn eine Campaign, ein Canvas oder ein Segment den Schwellenwert überschreitet und nicht gestartet werden kann. Wenn Sie diesen Fehler erhalten, vereinfachen Sie Ihre Zielgruppe vor dem erneuten Starten, einschließlich:

- Wenn Ihre Zielgruppe mehrere Segmente referenziert, stellen Sie sicher, dass die Segmente keine Redundanzen aufweisen, z. B. dieselben Filter in mehreren Segmenten.
- Stellen Sie sicher, dass Sie keine veralteten Daten in Segmentfiltern referenzieren. Beispielsweise könnte ein veralteter Filter nach Nutzer:innen suchen, die in der letzten Woche einen bestimmten Canvas-Schritt nicht erhalten haben, obwohl das Canvas seit Monaten gestoppt ist.
- Segmente, die nur Listen von Nutzer-IDs oder E-Mail-Adressen sind (die häufig einen Regex-Filter verwenden), können in einen [CSV-Import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) konvertiert und in einen einzelnen CSV-Filter vereinfacht werden.
- Wenn Sie CDI verwenden, können Sie möglicherweise ein CDI-Segment erstellen, das die Gruppe direkt aus Ihrem Data Warehouse abruft.

Sie können auch den [Support kontaktieren]({{site.baseurl}}/braze_support), um weitere Unterstützung bei der Filteroptimierung zu erhalten.

{% alert note %}
Wir haben im April 2025 begonnen, die Zeichenanzahl zu begrenzen. Campaigns und Canvases, die vor April 2025 gestartet wurden, waren davon ausgenommen, d. h. sie können den Grenzwert weiterhin überschreiten, während neu erstellte Campaigns und Canvases den Grenzwert nicht überschreiten können. Wenn Sie eine ausgenommene Campaign oder ein ausgenommenes Canvas bearbeiten oder klonen, können Sie es nicht starten, bis die Zielgruppe aktualisiert wurde, um unter dem Grenzwert zu liegen.
{% endalert %}

### X aktive oder gestoppte Campaigns oder Canvases überschreiten den Schwellenwert für die Zielgruppenkomplexität {#x-active-or-stopped-campaigns-or-canvases-exceed-the-audience-complexity-threshold}

Dieses Banner wird oben in einer Campaign- oder Canvas-Liste angezeigt, wenn aktive oder gestoppte Campaigns oder Canvases Zielgruppen haben, die den Schwellenwert für die Zielgruppenkomplexität überschreiten. Wählen Sie das Banner aus, um die Liste auf die Campaigns oder Canvases zu filtern, die den Schwellenwert überschreiten, und folgen Sie dann den Schritten zur Fehlerbehebung unter [Zielgruppe ist zu komplex zum Starten](#target-audience-is-too-complex-to-launch).

![Fehlerbanner, das besagt, dass 4 aktive oder gestoppte Canvases den Schwellenwert für die Zielgruppenkomplexität überschreiten.]({% image_buster /assets/img/segment/audience_complexity_threshold_banner.png %})

### Filter überschreitet 10.000 Bytes oder ist zu lang zum Speichern {#filter-exceeds-10000-bytes-or-is-too-long-to-save}

Braze begrenzt einzelne Segmentfilter auf maximal 10.000 Bytes, was 10.000 englischen Zeichen oder 3.333 japanischen Zeichen entspricht. Eine Warnung erscheint, wenn ein einzelner Filter 10.000 Bytes überschreitet, unabhängig davon, ob sich der Filter in einem Segment befindet oder direkt zu einer Campaign oder einem Canvas hinzugefügt wurde.

![Fehlerbanner für einen Filter, dessen Wert 10.000 Zeichen überschreitet.]({% image_buster /assets/img/segment/filter_error.png %})

![Fehler für einen angepassten Attributfilter „menu_item“, dessen Attributwert 10.000 Zeichen überschreitet.]({% image_buster /assets/img/segment/segment_filter_error.png %})

Dieser Fehler tritt sehr selten auf, aber wenn er auftritt, betrifft er typischerweise Regex-Filter, die auf eine Liste von Nutzer-IDs oder E-Mail-Adressen abzielen. In diesem Fall können Sie die folgenden Schritte ausführen, um die Filter in eine CSV-Datei zu konvertieren:

1. Exportieren Sie die Nutzer:innen aus dem betroffenen Segment oder dem spezifischen Regex-Filter.
2. Bereinigen Sie die CSV-Datei nach Bedarf. Sie benötigen entweder die Braze-ID oder die Appboy-ID, aber Sie können alle anderen Spalten entfernen, wenn sie nicht benötigt werden. Wir empfehlen außerdem, Ihre Daten zu überprüfen, um sicherzustellen, dass sie aktuell sind (entfernen Sie beispielsweise Nutzer:innen, die Sie nicht mehr ansprechen möchten).
3. [Importieren]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) Sie die CSV-Datei erneut, wodurch die Nutzer:innen automatisch in einen einzelnen, hocheffizienten CSV-basierten Filter gruppiert werden.

## Nutzerverhalten {#user-behavior}

### Nutzer:in ist nicht mehr in einem Segment {#user-is-no-longer-in-a-segment}

Wenn ein:e Nutzer:in beim Erstellen eines Segments nicht verfügbar ist, haben sich möglicherweise die Nutzerdaten, die die Segmentzugehörigkeit bestimmen, aufgrund eigener Aktivitäten oder anderer Campaigns und Canvases geändert, mit denen sie zuvor interagiert haben. Wenn die erneute Berechtigung aktiviert ist, zeigt das Nutzerprofil die neuesten Daten der empfangenen Campaign an.

Um zu testen, ob ein:e bestimmte:r Nutzer:in heute Ihrem Segment entspricht, verwenden Sie die [Nutzervorschau oder Nutzersuche]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments).

### Informationen werden für Nutzer:innen anderer Apps angezeigt, wenn ich nach einer bestimmten App filtere {#info-displays-for-users-of-other-apps-when-i-filter-for-a-specific-app}

Nutzer:innen können mehrere Apps haben, sodass die Auswahl einer bestimmten App im Abschnitt **Apps Used** der Segmentierungsseite Ergebnisse für Nutzer:innen liefert, die mindestens diese App haben. Der Filter liefert keine Ergebnisse für Nutzer:innen, die ausschließlich diese App haben.

## Filtern {#filtering}

### Filteroptionen haben sich geändert {#filter-options-changed}

Ihre Filteroptionen hängen mit dem Format (Datentyp) zusammen, das Sie für Ihr angepasstes Attribut an Braze übergeben. Um den Datentyp zu überprüfen, den Braze für Ihre angepassten Attribute erkennt, navigieren Sie zu **Dateneinstellungen** > **Angepasste Attribute**.

Wenn sich Ihre Filteroptionen geändert haben, deutet dies darauf hin, dass Ihre Daten in einem anderen Format (Datentyp) als zuvor an Braze übergeben werden. Detaillierte Beschreibungen der verschiedenen Datentypen und ihrer Filteroptionen finden Sie unter [Datentypen für angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types).

Beachten Sie, dass das Ändern des Datentyps eines angepassten Attributs im Dashboard Daten ablehnt, die in einem anderen Format an Braze gesendet werden. Sie können den Datentyp eines angepassten Attributs nicht ändern, solange dieses Attribut in aktiven Campaigns, Canvases oder Segmenten referenziert wird; das Dashboard zeigt einen Fehler an und blockiert die Änderung.

Der Tab **Werte** eines angepassten Attributs zeigt Ergebnisse aus einer Stichprobe von ungefähr 250.000 Nutzer:innen. Verwenden Sie den Tab **Werte** nicht, um zu bestätigen, ob ein bestimmter Attributwert zur Fehlerbehebung existiert. Weitere Informationen finden Sie unter [Tab „Werte“]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#values-tab).

### Segment ist viel größer als erwartet {#segment-is-much-larger-than-expected}

Wenn Ihr Segment trotz restriktiv wirkender Filter viel größer aussieht als erwartet, prüfen Sie, ob Sie negative Filter (`ist nicht`, `ist nicht gleich`, `stimmt nicht mit Regex überein` oder `nicht enthalten`) mit dem **OR**-Operator für dasselbe Attribut mehr als einmal verwenden. Diese Kombination kann Nutzer:innen mit allen Werten für das Attribut ansprechen.

Hinweise dazu, wann Sie **AND** statt **OR** verwenden sollten, finden Sie unter [Wann Sie den OR-Operator vermeiden sollten]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#segmentation-logic-using-and-and-or) in „Segment erstellen“.

## Analytics und Berichterstattung {#analytics-and-reporting}

### *Gesendete Nachrichten* oder *Eindeutige Empfänger:innen* in Campaign Analytics stimmen nicht mit der Segmentanzahl überein {#message-sent-or-unique-recipients-in-campaign-analytics-doesnt-match-segment-count}

Wenn die Anzahl für *Gesendete Nachrichten* oder *Eindeutige Empfänger:innen* in Ihren Campaign Analytics nicht mit der Anzahl der Nutzer:innen im Segmentfilter `Has received message from campaign X` übereinstimmt, kann dies drei mögliche Gründe haben.

1. **Nutzer:innen wurden möglicherweise seit dem Campaign-Start archiviert, verwaist oder gelöscht**<br><br>Nehmen wir beispielsweise an, 1.000 Nutzer:innen erhalten eine Campaign und Sie erstellen am selben Tag einen CSV-Export. Sie sehen 1.000 gemeldete Nutzer:innen. Im Laufe des nächsten Monats werden 50 dieser 1.000 Nutzer:innen gelöscht (z. B. über den Endpunkt `users/delete`). Wenn Sie einen weiteren CSV-Export erstellen, sehen Sie 950 gemeldete Nutzer:innen, während die Anzahl der *Eindeutigen Empfänger:innen* in **Campaign Analytics** weiterhin 1.000 beträgt.<br><br>Mit anderen Worten: Die Metrik *Eindeutige Empfänger:innen* ist ein inkrementierter Zähler, während der Segmentierer und der CSV-Export eine Anzahl der aktuell vorhandenen Nutzer:innen liefern.<br><br>

2. **Die Campaign hat eine erneute Berechtigung eingestellt, sodass Nutzer:innen die Campaign mehrfach betreten können**<br><br>Nehmen wir beispielsweise an, eine E-Mail-Campaign hat die erneute Berechtigung auf null Minuten eingestellt (Nutzer:innen können die Campaign erneut betreten, solange sie die Anforderungen des Zielgruppensegments erfüllen), und die Campaign läuft seit über einem Monat. Die Anzahl der *Gesendeten Nachrichten* in **Campaign Analytics** würde nicht mit der Anzahl im Segment übereinstimmen, da dieses Feld Nachrichten enthält, die an doppelte Nutzer:innen gesendet wurden.<br><br>Das liegt daran, dass Braze eindeutige Nutzer:innen als *Eindeutige tägliche Empfänger:innen* zählt, also die Anzahl der Nutzer:innen, die eine bestimmte Nachricht an einem Tag erhalten haben. Das bedeutet, dass erneut berechtigte Nutzer:innen mehr als einmal als eindeutige:r Empfänger:in gezählt werden, da das Eindeutigkeitsfenster nur einen Tag dauert. Dies kann dazu führen, dass die Anzahl der *Eindeutigen täglichen Empfänger:innen* höher ist als die Anzahl der Nutzerprofile im CSV-Export. Die Nutzerprofile in der CSV-Datei sind wirklich eindeutig.<br><br>

3. **Nutzer:innen, die einen Kanalbezeichner teilen, haben den Filter erfüllt**<br><br>Der Filter `Has received message from campaign X` (und andere „Erhalten“-Filter) kann Nutzer:innen erfassen, die einen Kanalbezeichner wie dasselbe Push-Token oder dieselbe E-Mail-Adresse mit einem anderen Nutzerprofil teilen, das die Nachricht erhalten, geöffnet oder angeklickt hat.

### Nutzer:in ist zwei Apps zugewiesen, obwohl nur in einer App eine Sitzung protokolliert wurde {#user-is-assigned-to-two-apps-despite-logging-a-session-in-only-one-app}

Beim Erstellen eines Segments können Sie Nutzer:innen ansprechen, die [bestimmte Apps verwendet]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#step-3-choose-your-app-or-platform) haben. Ein:e Nutzer:in muss eine Sitzung in einer bestimmten App gehabt haben, um dieser App zugewiesen zu werden. Es gibt jedoch zwei Szenarien, in denen ein:e Nutzer:in einer bestimmten App zugewiesen werden kann, ohne Sitzungen in der App protokolliert zu haben.

Das erste Szenario ist, wenn das Feld `app_id` bei Verwendung des Endpunkts `/users/track` ausgefüllt wird – insbesondere bei Verwendung eines [Event-Objekts]({{site.baseurl}}/api/objects_filters/event_object) oder [Kauf-Objekts]({{site.baseurl}}/api/objects_filters/purchase_object), wie in diesem Beispiel:

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

Das zweite Szenario ist, wenn das Feld `app_id` bei Verwendung des Endpunkts `/users/track` zum Migrieren von Push-Tokens ausgefüllt wird, wie in diesem Beispiel:

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
