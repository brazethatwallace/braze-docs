---
nav_title: Segments verwalten
article_title: Segments verwalten
page_order: 2
page_type: tutorial
tool: Segments
description: "Dieser Artikel beschreibt die Aktionen, die Sie zur Verwaltung Ihrer Segments durchführen können, wie das Filtern einer Segment-Liste, das Erstellen von Segments und das Bearbeiten von Segments."

---

# Segments verwalten {#manage-segments}

> Im Abschnitt „Segments“ können Sie eine umfassende Liste Ihrer vorhandenen Segments anzeigen, neue Segments erstellen und bestehende Segments bearbeiten. Sie können die Segment-Liste verfeinern, indem Sie verschiedene Filter und Spalten auswählen, sodass nur die für Sie relevantesten Informationen angezeigt werden.

![Der Abschnitt „Segments“ mit einer Liste aktiver Segments.]({% image_buster /assets/img/segment/segments_page.png %})

## Ihre Ansicht anpassen {#customizing-your-view}

Passen Sie Ihre Ansicht der Segment-Liste an, indem Sie Filter verwenden und die anzuzeigenden Spalten ändern. Wenn Sie den Abschnitt **Segments** verlassen und zurückkehren, wird die Liste auf die Standardansicht zurückgesetzt und alle zuvor ausgewählten Filter werden gelöscht.

### Statusfilter {#status-filter}

Sie können die Liste eingrenzen, um nur aktive oder archivierte Segments anzuzeigen. Jedes nicht archivierte Segment gilt als aktiv.

### Filter {#filters}

Sortieren Sie die Segments in der Liste, indem Sie die folgenden Filter anpassen:
- **Last Edited By:** Die Person, die die Segments zuletzt bearbeitet hat
- **Last Edited:** Zeitraum, in dem die Segments zuletzt bearbeitet wurden
- **Estimated Size:** Ungefähre Spanne, wie viele Nutzer:innen sich in den Segments befinden
- **Tags:** Tags, die den Segments zugeordnet sind
- **Teams:** Teams, die den Segments zugeordnet sind
- **Advanced Tracking Segments Only:** Zeigt nur die Segments an, bei denen [Analytics-Tracking]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking) aktiviert ist.

### Spalten {#columns}

Dies sind die Informationsspalten, die Sie für die Anzeige in der Segment-Liste auswählen können:
- **Filters:** Anzahl der Filter im Segment
- **Last edited:** Datum, an dem das Segment zuletzt bearbeitet wurde
- **Last edited by:** Die Person, die das Segment zuletzt bearbeitet hat
- **Tags:** Tags, die dem Segment zugeordnet sind
- **Teams:** Teams, die dem Segment zugeordnet sind
- **Estimated size:** Geschätzte Anzahl der Nutzer:innen im Segment
- **Canvases:** Anzahl der Canvases, die das Segment verwenden
- **Campaigns:** Anzahl der Campaigns, die das Segment verwenden

### Nur markierte anzeigen {#show-starred-only}

Durch Auswahl von **Show Starred Only** wird Ihre Ansicht auf die Segments eingegrenzt, die von Ihnen mit einem Stern markiert wurden.

## Messaging-Nutzung eines Segments anzeigen {#messaging-use}

Gehen Sie zum Abschnitt **Messaging Use** eines Segments, um eine Übersicht darüber zu erhalten, wo das Segment verwendet wird, z. B. in anderen Segments, Campaigns und Canvases.

{% alert note %}
Um Schleifen durch gegenseitige Segment-Referenzen zu vermeiden, können Segments, die den Filter **Segment Membership** verwenden, nicht von anderen Segments referenziert werden. Weitere Informationen finden Sie unter [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).
{% endalert %}

## Bestimmte Segments verwalten {#managing-specific-segments}

![Das Bearbeitungsmenü für ein Segment mit den Optionen „Edit“, „Duplicate“, „Archive“ und „Add to starred“.]({% image_buster /assets/img/segment/segments_page_edit_menu.png %}){: style="float:right;max-width:25%;"}

Um ein bestimmtes Segment zu verwalten, bewegen Sie den Mauszeiger darüber und wählen Sie das Menüsymbol am Ende der Zeile, um die folgenden Optionen anzuzeigen:
- **Edit:** Bearbeiten Sie die Filter in Ihrem Segment.
- **Duplicate:** Erstellen Sie eine Kopie Ihres Segments.
- **Archive:** Archivieren Sie das Segment. Beachten Sie, dass dadurch auch alle Campaigns oder Canvases archiviert werden, die dieses Segment verwenden.
- **Add to starred:** Markieren Sie das Segment mit einem Stern, sodass Sie schnell darauf zugreifen können, indem Sie im Segment-Abschnitt das Kontrollkästchen „Nur markierte anzeigen“ aktivieren.

Sie können auch Massenaktionen durchführen – insbesondere Massenarchivierung und Massen-Tagging – indem Sie die Kontrollkästchen neben mehreren Segment-Namen aktivieren.

{% alert tip %}
Wenn Sie einen maschinenlesbaren Export der vorhandenen Segments im Workspace benötigen (nicht nur die aktuelle Tabellenansicht), verwenden Sie den [Endpunkt „Segment-Liste exportieren“]({{site.baseurl}}/api/endpoints/export/segments/get_segment) und blättern Sie durch die Ergebnisse. Um archivierte Segments zu überprüfen, sehen Sie diese separat im **Segments**-Dashboard mithilfe des Statusfilters ein.
{% endalert %}

![Mehrere ausgewählte Segments mit „CRM“ als ausgewähltem Wert im Dropdown-Feld „Tag As“.]({% image_buster /assets/img/segment/segments_bulk_action.png %}){: style="max-width:45%;"}

### Änderungen seit der letzten Ansicht {#changes-since-last-viewed}

Die Anzahl der Aktualisierungen an den Segments durch andere Mitglieder Ihres Teams wird durch die Metrik *Changes Since Last Viewed* auf der Segment-Übersichtsseite erfasst. Wählen Sie **Changes Since Last Viewed**, um ein Changelog der Aktualisierungen an Name, Beschreibung und Zielgruppe des Segments anzuzeigen. Für jede Aktualisierung können Sie sehen, wer sie durchgeführt hat und wann. Sie können dieses Changelog verwenden, um Änderungen an Ihrem Segment zu überprüfen.

## Nach Segments suchen {#searching-for-segments}

Suchen Sie nach Segment-Namen, indem Sie Begriffe in das Suchfeld eingeben.

Alle in dieses Feld eingegebenen Begriffe und Zeichenfolgen werden durchsucht. Wenn Sie beispielsweise nach „test segment 1“ suchen, werden Segments zurückgegeben, die „test“, „segment“ oder „1“ irgendwo in ihrem Namen enthalten. Um nach einer exakten Zeichenfolge zu suchen, setzen Sie Ihren Suchbegriff in Anführungszeichen. Die Suche nach [„test segment 1“] gibt alle Segments zurück, die die exakte Phrase „test segment 1“ in ihrem Namen enthalten.

![Die Suchergebnisse für die Eingabe von „all users“ in das Suchfeld umfassen „All Users (Test)“, „All Users“, „All Users 15“.]({% image_buster /assets/img/segment/segments_search.png %})

### Segments in Canvases {#segments-in-canvases}

Um alle Segment-Referenzen zu durchsuchen, einschließlich derer in anderen Segments, Campaigns oder Canvases, gehen Sie zum Abschnitt [Messaging-Nutzung](#messaging-use) eines Segments. Der Filter **Target segment** auf der **Canvas**-Seite durchsucht nur Canvas-Zielgruppen-Segments.

![Der Filter „Target segment“ auf der Canvas-Seite.]({% image_buster /assets/img/segment/target_segment.png %}){: style="max-width:45%;"}