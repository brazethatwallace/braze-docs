---
nav_title: CDI-Segmenterweiterungen
article_title: CDI-Segmenterweiterungen
page_order: 0
page_type: reference
alias: /cdi_segment_extensions/
tool:
- Segments
description: "Dieser Artikel erklärt, wie CDI-Segmenterweiterungen die Cloud-Datenaufnahme nutzen, um Ihr Data Warehouse abzufragen und Zielgruppen in Braze zu definieren."

---

# CDI-Segmenterweiterungen {#cdi-segment-extensions}

> Mit der [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/) (CDI) von Braze können Sie eine direkte Verbindung von Ihrem Data Warehouse oder Dateispeichersystem zu Braze einrichten, um relevante Nutzer:innen- oder Katalogdaten regelmäßig zu synchronisieren.

{% alert warning %}
CDI-Segmenterweiterungen fragen Ihr Data Warehouse direkt ab, sodass Ihnen alle Kosten entstehen, die mit der Ausführung dieser Abfragen in Ihrem Data Warehouse verbunden sind. CDI-Segmenterweiterungen verbrauchen keine [SQL-Segment-Credits]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/#monitoring-your-sql-segments-usage), zählen nicht zu Ihrem Segmenterweiterungs-Limit und protokollieren keine Datenpunkte.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um Ihre Data-Warehouse-Daten für die Segmentierung in Ihrem Braze-Workspace zu nutzen, müssen Sie eine [verbundene Quelle]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources/) erstellen und dann ein CDI-Segment in Ihren [Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/) anlegen. CDI-Segmenterweiterungen ermöglichen es Ihnen, SQL zu schreiben, das Ihr eigenes Data Warehouse direkt abfragt, indem es Daten nutzt, die über Ihre CDI-Verbindungen verfügbar gemacht werden, und eine Gruppe von Nutzer:innen zu erstellen, die innerhalb von Braze angesprochen werden kann.

## Ein CDI-Segment erstellen {#creating-a-cdi-segment}

### 1. Schritt: Quelle einrichten {#step-1-set-up-your-source}

Bevor Sie Ihre erste CDI-Segmenterweiterung erstellen, richten Sie eine neue verbundene Quelle mit Ihrem Data Warehouse ein, indem Sie den Schritten unter [Verbundene Quellen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources/) folgen.

### 2. Schritt: Segment erstellen {#step-2-create-a-segment}

Erstellen Sie zunächst eine neue [Segmenterweiterung]({{site.baseurl}}/user_guide/audience/segments/segment_extension/) und wählen Sie dann **Full refresh** aus.

![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:60%;"}

Wählen Sie als Datenquelle **CDI Data Tables** aus.

![]({% image_buster /assets/img/segment/cdi_data_tables.png %}){: style="max-width:60%;"}

Im Rahmen Ihrer CDI-Einrichtung können Sie aus verschiedenen Verbindungen auswählen, die in CDI-Segmenterweiterungen verwendet werden sollen. Jede Verbindung verfügt über einen bestimmten Satz von Datentabellen. Ihr Entwicklungsteam kann Ihre Verbindungen und Datentabellen während der CDI-Einrichtung konfigurieren.

Um die verfügbaren Datentabellen einschließlich ihres Schemas und etwaiger Beschreibungen anzuzeigen, wählen Sie **Reference** aus. Wenn Sie bereit sind, wählen Sie eine Verbindung aus.

![]({% image_buster /assets/img/segment/connection_schema_with_descriptions.png %}){: style="max-width:100%;"}

Schreiben Sie als Nächstes das SQL für Ihr Segment unter Verwendung der [Braze-SQL-Syntax]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/#writing-sql).

Beachten Sie, dass alle CDI-Segmenterweiterungen `external_user_id` als ausgewählte Spalte verwenden müssen und Ihre `external_user_id` mit der in Braze für Nutzer:innen festgelegten übereinstimmen sollte.

{% alert important %}
`external_user_id` muss ein **String**-Wert sein. Wenn Ihre Quell-ID als Zahl gespeichert ist (zum Beispiel `client_id` als Integer), [wandeln Sie sie in Ihrem SQL in einen String um](https://www.w3schools.com/sql/func_sqlserver_cast.asp), damit sie dem `external_id`-Typ in Braze entspricht.
{% endalert %}

Wenn Ihre Abfrageergebnisse Nutzer:innen enthalten, die in Braze nicht existieren, werden diese ignoriert. Braze erstellt keine neuen Nutzer:innen basierend auf der Ausgabe Ihrer CDI-Segmenterweiterung.

{% alert tip %}
Um zu erfahren, wie Sie Ihre Segmenterweiterungen in der Vorschau anzeigen, verwalten und automatische Mitgliedschaftsaktualisierungen ausführen können, lesen Sie [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/).
{% endalert %}

Schließlich können Sie [diese Segmenterweiterung verwenden]({{site.baseurl}}/user_guide/audience/segments/segment_extension/#step-5-use-your-extension-in-a-segment), um innerhalb eines Braze-Segments eine Campaign oder ein Canvas an diese Zielgruppe zu senden.

## Hinweise {#considerations}

- Eine Segmenterweiterung kann nur auf Daten aus einer einzigen Verbindung verweisen, nicht aus mehreren.
- Eine Segmenterweiterung kann eine der folgenden Datenquellen verwenden: CDI-Daten oder Braze-Snowflake-Daten (Currents). Sie können Datenquellen innerhalb einer Segmenterweiterung nicht mischen, aber Sie können mehrere Segmenterweiterungen erstellen, die innerhalb eines Segments gemeinsam referenziert werden.

## Fehlerbehebung {#troubleshooting}

- Ihre Abfrage kann ein Timeout erreichen, wenn sie Ihre maximale Laufzeit überschreitet, die für jede Verbindungssynchronisierung auf der Seite **Cloud Data Ingestion** festgelegt wird. Die maximal zulässige Laufzeit beträgt 60 Minuten.
- Stellen Sie sicher, dass Ihr SQL mit der passenden Syntax für Ihr Data Warehouse geschrieben ist.