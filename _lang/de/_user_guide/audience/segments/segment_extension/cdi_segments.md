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

> Mit der [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) (CDI) von Braze können Sie eine direkte Verbindung von Ihrem Data Warehouse oder Dateispeichersystem zu Braze einrichten, um relevante Nutzer:innen- oder Katalogdaten regelmäßig zu synchronisieren.

{% alert warning %}
CDI-Segmenterweiterungen fragen Ihr Data Warehouse direkt ab, sodass Ihnen alle Kosten entstehen, die mit der Ausführung dieser Abfragen in Ihrem Data Warehouse verbunden sind. CDI-Segmenterweiterungen verbrauchen keine [SQL-Segment-Credits]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments#credits), zählen nicht zu Ihrem Segmenterweiterungs-Limit und protokollieren keine Datenpunkte.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um Ihre Data-Warehouse-Daten für die Segmentierung in Ihrem Braze-Workspace zu nutzen, müssen Sie eine [verbundene Quelle]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources) erstellen und dann ein CDI-Segment in Ihren [Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension) anlegen. CDI-Segmenterweiterungen ermöglichen es Ihnen, SQL zu schreiben, das Ihr eigenes Data Warehouse direkt abfragt, indem es Daten nutzt, die über Ihre CDI-Verbindungen bereitgestellt werden, und eine Gruppe von Nutzer:innen zu erstellen, die innerhalb von Braze angesprochen werden können.

## Erstellen eines CDI-Segments {#creating-a-cdi-segment}

### Schritt 1: Quelle einrichten {#step-1-set-up-your-source}

Bevor Sie Ihre erste CDI-Segmenterweiterung erstellen, richten Sie eine neue verbundene Quelle mit Ihrem Data Warehouse ein, indem Sie die Schritte unter [Verbundene Quellen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources) befolgen.

### Schritt 2: Segment erstellen {#step-2-create-a-segment}

1. Gehen Sie zu **Zielgruppe** > **Segmenterweiterungen** und wählen Sie **Neue Erweiterung erstellen**.
2. Wählen Sie im Menü **Erstellungsmethode für Segmenterweiterung auswählen** die Option **Vollständige Aktualisierung (einschließlich CDI-Segmente)**.

![Das Menü „Erstellungsmethode für Segmenterweiterung auswählen“ mit den verfügbaren Erstellungsoptionen.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:60%;"}

{: start="3"}
3. Wählen Sie im Menü **Datenquelle für diese Segmenterweiterung auswählen** die Option **CDI-Datentabellen**. Dieses Menü wird nur angezeigt, nachdem Sie mindestens eine [verbundene Quelle]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources) eingerichtet haben.

![Das Menü „Datenquelle für diese Segmenterweiterung auswählen“ mit der Option „CDI-Datentabellen“.]({% image_buster /assets/img/segment/cdi_data_tables.png %}){: style="max-width:60%;"}

{: start="4"}
4. Wählen Sie eine Verbindung aus und schreiben Sie dann Ihre Abfrage. Jede Verbindung verfügt über einen bestimmten Satz von Datentabellen. Ihr Entwicklungsteam kann Ihre Verbindungen und Datentabellen während der CDI-Einrichtung konfigurieren.
5. Sehen Sie sich die verfügbaren Datentabellen an, einschließlich ihres Schemas und etwaiger Beschreibungen, indem Sie **Quellen-Explorer** auswählen.

![Der Quellen-Explorer mit den verfügbaren Datentabellen, einschließlich ihres Schemas und etwaiger Beschreibungen.]({% image_buster /assets/img/segment/connection_schema_with_descriptions.png %}){: style="max-width:100%;"}

{: start="6"}
6. Schreiben Sie die SQL-Abfrage für Ihr Segment mithilfe der [Braze-SQL-Syntax]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments#step-2-write-your-sql). Beachten Sie, dass alle CDI-Segmenterweiterungen `external_user_id` als ausgewählte Spalte verwenden müssen und Ihre `external_user_id` mit der in Braze für Nutzer:innen festgelegten übereinstimmen sollte.<br><br>
Wenn Ihre Abfrageergebnisse Nutzer:innen enthalten, die in Braze nicht existieren, werden diese ignoriert. Braze erstellt keine neuen Nutzer:innen auf Grundlage der Ausgabe Ihrer CDI-Segmenterweiterung.

{% alert important %}
`external_user_id` muss ein String-Wert sein. Wenn Ihre Quell-ID als Zahl gespeichert ist (zum Beispiel `client_id` als Integer), [wandeln Sie sie in Ihrem SQL in einen String um](https://www.w3schools.com/sql/func_sqlserver_cast.asp), damit sie mit dem `external_id`-Typ in Braze übereinstimmt.
{% endalert %}

{: start="7"}
7. [Verwenden Sie diese Segmenterweiterung]({{site.baseurl}}/user_guide/audience/segments/segment_extension#step-6-use-your-extension-in-a-segment) innerhalb eines Braze-Segments, um eine Campaign oder ein Canvas an diese Zielgruppe zu senden.

{% alert tip %}
Informationen dazu, wie Sie Ihre Segmenterweiterungen in der Vorschau anzeigen, verwalten und automatische Mitgliedschaftsaktualisierungen ausführen können, finden Sie unter [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments).
{% endalert %}

## Überlegungen {#considerations}

- Eine Segmenterweiterung kann nur auf Daten aus einer einzelnen Verbindung verweisen, nicht aus mehreren.
- Eine Segmenterweiterung kann eine der folgenden Datenquellen verwenden: CDI-Daten oder Braze Snowflake (Currents)-Daten. Sie können innerhalb einer Segmenterweiterung keine Datenquellen mischen, aber Sie können mehrere Segmenterweiterungen erstellen und diese innerhalb eines Segments gemeinsam referenzieren.

## Fehlerbehebung {#troubleshooting}

- Ihre Abfrage kann ein Timeout erreichen, wenn sie die maximale Laufzeit überschreitet, die für jede Verbindungssynchronisierung auf der Seite **Cloud Data Ingestion** festgelegt ist. Die maximal zulässige Laufzeit beträgt 60 Minuten.
- Stellen Sie sicher, dass Ihr SQL mit der entsprechenden Syntax für Ihr Data Warehouse geschrieben ist.