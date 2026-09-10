---
nav_title: Segmenterweiterungen
article_title: Segmenterweiterungen
page_order: 5
page_type: reference
description: "Dieser Artikel zeigt Ihnen, wie Sie eine Segmenterweiterung einrichten und verwenden, um Ihre Segmentierungsmöglichkeiten zu erweitern."
tool: Segments
---

# Segmenterweiterungen {#segment-extensions}

> Segmenterweiterungen ermöglichen es Ihnen, sehr präzise Segmente über einen längeren Zeitraum der Nutzer:innen-Historie zu erstellen. Zum Beispiel können Sie mit Segmenterweiterungen Nutzer:innen ansprechen, die in den letzten sechzehn Monaten ein bestimmtes Produkt gekauft oder einen bestimmten Betrag bei Ihrem Dienst ausgegeben haben. Verfeinern Sie diese Zielgruppe mithilfe von Event-Eigenschaften, um das Targeting noch granularer zu gestalten.

Die Braze-Segmentierung ermöglicht es Ihnen, Nutzer:innen basierend auf angepassten Events oder Kaufverhalten anzusprechen. Segmenterweiterungen erweitern diese Möglichkeit, indem sie auf historische Daten zurückgreifen, die im Kundenprofil gespeichert sind. Mit Segmenterweiterungen können Sie Nutzer:innen identifizieren und erreichen, die ein beliebiges angepasstes Event oder Kauf-Event beliebig oft in den letzten zwei Jahren (730 Tagen) abgeschlossen haben.

## Warum Segmenterweiterungen verwenden? {#why-use-segment-extensions}

Braze Segments bieten Ihnen leistungsstarke Targeting-Tools, um dynamische Gruppen von Nutzer:innen zu erstellen. Für die meisten Anwendungsfälle reicht das aus, um Ihre Zielgruppe effektiv zu erreichen. Segmenterweiterungen sind für fortgeschrittene Anwendungsfälle konzipiert, bei denen Sie Verhaltensdaten von bis zu zwei Jahren analysieren oder komplexe Logik anwenden müssen – ohne Kompromisse bei der Datenspeicherung oder Systemleistung. Sie können [SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)-Abfragen (SQL-Segmenterweiterungen) oder Daten aus Ihrem eigenen [Data Warehouse]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments) nutzen, um Ihre Zielgruppe weiter zu verfeinern.

Beispielsweise findet die standardmäßige Segmentierung von Braze Nutzer:innen, die bestimmte von Ihnen definierte Kriterien erfüllen, wie z. B. die Identifizierung von Nutzer:innen, die kürzlich eines Ihrer Produkte gekauft haben. Segmenterweiterungen ermöglichen es Ihnen, tiefer zu gehen – etwa um Nutzer:innen zu identifizieren, die eine bestimmte Farbe eines bestimmten Produkts mindestens zweimal in einem Zeitraum von 18 bis 24 Monaten gekauft haben. Segmenterweiterungen sind eine Erweiterung, keine Voraussetzung. Wenn Sie fortgeschrittenere Filter oder ein längeres Rückblickfenster benötigen, sind sie ein hervorragendes Werkzeug, das Ihnen hilft und gleichzeitig Ihre Datennutzung optimiert.

{% alert note %}
Standardmäßig stehen pro Workspace zu einem bestimmten Zeitpunkt 50 aktive Segmenterweiterungen zur Verfügung. Wenn Sie dieses Limit erhöhen müssen, wenden Sie sich an Ihren Customer-Success-Manager bei Braze, um Ihren Anwendungsfall zu besprechen.
{% endalert %}

## Erstellen einer Segmenterweiterung {#creating-a-segment-extension}

Um eine Segmenterweiterung zu erstellen, erstellen Sie einen Filter, um ein Segment Ihrer Nutzer:innen anhand von angepassten Event-Eigenschaften einzugrenzen. Beim Erstellen einer Segmenterweiterung legen Sie fest, ob das Segment statisch ist oder in einem festgelegten Intervall dynamisch aktualisiert wird.

### Schritt 1: Zu den Segmenterweiterungen navigieren {#step-1-navigate-to-segment-extensions}

Gehen Sie zu **Audience** > **Segment Extensions**.

Wählen Sie in der Tabelle der Segmenterweiterungen **Create New Extension** und wählen Sie dann Ihre Erstellungsmethode für die Segmenterweiterung:

- **Simple extension:** Erstellen Sie eine Segmenterweiterung, die sich auf ein einzelnes Event konzentriert, indem Sie ein geführtes Formular verwenden. Am besten geeignet, wenn Sie kein SQL verwenden möchten.
- **Start with a template:** Erstellen Sie ein SQL-Segment mit einem anpassbaren Template unter Verwendung von Snowflake-Daten.
- **Incremental refresh:** Schreiben Sie ein Snowflake-SQL-Segment, das automatisch die Daten der letzten 2 Tage aktualisiert, oder aktualisieren Sie bei Bedarf manuell. Am besten geeignet, um Genauigkeit und Kosteneffizienz auszubalancieren.
- **Full refresh:** Schreiben Sie ein SQL-Segment mit Snowflake-Daten oder einer beliebigen [CDI-verbundenen Quelle]({{site.baseurl}}/cdi_segment_extensions), das die gesamte Zielgruppe bei manueller Aktualisierung neu berechnet. Am besten geeignet, wenn Sie eine vollständige, aktuelle Ansicht Ihrer Zielgruppe benötigen.

![Tabelle mit verschiedenen Erstellungsmethoden für Segmenterweiterungen zur Auswahl.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%"}

Wenn Sie eine Methode auswählen, die SQL verwendet, lesen Sie [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) für weitere Informationen. Wenn Sie **Simple extension** auswählen, fahren Sie mit Schritt 2 fort.

#### Verbrauch von SQL-Credits {#sql-credit-usage}

Die folgenden Typen von Segmenterweiterungen verbrauchen SQL-Credits:

- SQL-Segmenterweiterungen (sowohl inkrementelle als auch vollständige Aktualisierung)
- Katalogsegmente
- CDI-Segmente
    - Credits werden in Ihrem eigenen Data Warehouse verbraucht

### Schritt 2: Segmenterweiterung benennen {#step-2-name-your-segment-extension}

Benennen Sie Ihre Segmenterweiterung, indem Sie den Typ der Nutzer:innen beschreiben, die Sie filtern möchten. Dies hilft anderen, die Erweiterung korrekt zu finden und anzuwenden.

![Segmenterweiterung mit dem Namen „Online Shoppers Extension - 90 Days“.]({% image_buster /assets/img/segment/segment_extension2.png %})

### Schritt 3: Kriterien auswählen {#step-3-choose-your-criteria}

Wählen Sie zwischen Kauf-, Nachrichteninteraktions-, empfohlenen E-Commerce-Event- oder angepassten Event-Kriterien für das Targeting. Nachdem Sie die gewünschten Event-Typ-Kriterien ausgewählt haben, wählen Sie, welchen gekauften Artikel, welche Nachrichteninteraktion, welches empfohlene E-Commerce-Event oder welches angepasste Event Sie für Ihre Nutzer:innenliste verwenden möchten. Legen Sie dann fest, wie oft (mehr als, weniger als oder gleich) die Nutzer:innen das Event abgeschlossen haben müssten, und den Zeitraum – speziell für Segmenterweiterungen können Sie bis zu 730 Tage (2 Jahre) zurückblicken.

Eine Segmentierung auf Basis von Event-Daten, die älter als 730 Tage sind, kann mit anderen Filtern unter **Segments** durchgeführt werden. Bei der Auswahl Ihres Zeitraums können Sie einen relativen Datumsbereich angeben, um die letzten X Tage auszuwählen, ein Startdatum, ein Enddatum oder einen genauen Datumsbereich (Datum A bis Datum B).

![Segmentierungskriterien für Nutzer:innen, die ein angepasstes Event mehr als 2 Mal im Datumsbereich vom 1. März 2025 bis zum 31. März 2025 durchgeführt haben.]({% image_buster /assets/img/segment/segment_extension1.png %})

Wenn Sie eine Segmenterweiterung mit einem empfohlenen E-Commerce-Event erstellen, wählen Sie zunächst **eCommerce Recommended Event** als Kriterium und dann ein Event aus dem Dropdown.

![Ein Kriterium für ein empfohlenes E-Commerce-Event mit einem Dropdown der verfügbaren empfohlenen Events.]({% image_buster /assets/img/segment/ecommerce_recommended_event_criterion.png %})

#### Segmentierung nach Event-Eigenschaften {#event-property-segmentation}

Um die Targeting-Präzision zu erhöhen, aktivieren Sie das Kontrollkästchen **Add Property Filters**. Dadurch können Sie anhand der spezifischen Eigenschaften Ihres Kaufs oder angepassten Events filtern. Wir unterstützen die Segmentierung nach Event-Eigenschaften basierend auf String-, numerischen, booleschen und Zeit-Objekten.

##### Eigenschafts-Datentypen {#property-data-types}

Bei String-Eigenschaften können Sie mehrere Werte gleichzeitig eingeben. Im folgenden Beispiel sucht dieser Filter nach Nutzer:innen mit einer Hunderasse, die einer von sechs bestimmten Hunderassen entspricht.

![Segmentierung basierend auf String-Eigenschaften.]({% image_buster /assets/img/segment/property5.png %})

##### Eigenschaften empfohlener E-Commerce-Events {#ecommerce-recommended-event-properties}

Wenn Sie eine Event-Eigenschaft für ein empfohlenes E-Commerce-Event hinzufügen, wird das Eigenschafts-Dropdown automatisch mit den für dieses Event verfügbaren Eigenschaften befüllt.

Segmenterweiterungen unterstützen nur Event-Eigenschaften in der dokumentierten Allowlist für jedes empfohlene E-Commerce-Event. Angepasste Top-Level-Eigenschaften, die Sie über die API oder das SDK senden, sind für Eigenschaftsfilter von Erweiterungen nicht gültig – auch dann nicht, wenn diese Eigenschaften in Ihren Event-Daten erscheinen. Die Verwendung einer nicht in der Allowlist aufgeführten Top-Level-Eigenschaft verhindert das Speichern oder Dearchivieren der Erweiterung.

Wenn Sie nach nicht standardmäßigen Eigenschaften filtern müssen, verschachteln Sie diese unter `metadata`, wenn Sie das Event protokollieren (zum Beispiel `metadata.color` statt `color`). Informationen zu unterstützten Eigenschaften finden Sie unter [Event-Schemata]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#event-schemas) und [Typen empfohlener E-Commerce-Events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events).

![Details der Segmenterweiterung mit einem Dropdown der verfügbaren Eigenschaften.]({% image_buster /assets/img/segment/ecommerce_recommended_event_properties.png %})

##### Verschachtelte Event-Eigenschaften {#nested-event-properties}

Wir unterstützen auch die Segmentierung basierend auf [verschachtelten Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects). Wählen Sie im Vergleichs-Dropdown den Vergleich aus, der zum Datentyp Ihrer verschachtelten Eigenschaft passt. Sie können dieselbe Syntax für verschachtelte Event-Eigenschaften verwenden, um verschachtelte Eigenschaften für alle empfohlenen E-Commerce-Events hinzuzufügen, die verschachtelte Eigenschaften enthalten.

Informationen zu den verschiedenen verfügbaren verschachtelten Eigenschaften finden Sie unter [Typen empfohlener E-Commerce-Events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events). Um das erforderliche Schema für den Eigenschaftsnamen Ihrer Segmenterweiterung zu generieren, folgen Sie den Schritten unter [Verschachtelte Objekte in angepassten Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects).

![Segmentierung basierend auf verschachtelten Event-Eigenschaften.]({% image_buster /assets/img/segment/nested_segment_extensions.png %})

##### Rückblickzeitraum und Datenpunkte {#lookback-window-and-data-points}

Segmenterweiterungen basieren auf der Langzeitspeicherung von Event-Eigenschaften und haben keine zeitgestempelte Speicherbegrenzung für Eigenschaften. Sie können auf Event-Eigenschaften zurückblicken, die innerhalb der letzten zwei Jahre erfasst wurden. Die Verwendung von Event-Eigenschaften innerhalb von Segmenterweiterungen wirkt sich nicht auf die Datenpunkt-Nutzung aus.

{% alert note %}
Sie benötigen keine Segmenterweiterungen, um Event-Eigenschaften oder verschachtelte angepasste Attribute in Ihrem Segment zu verwenden. Segmenterweiterungen erweitern lediglich das historische Zeitfenster, das zur Erstellung eines Standard-Segments verwendet wird. Sie können ein Standard-[Segment]({{site.baseurl}}/user_guide/audience/segments) in Realtime erstellen, das Event-Eigenschaften der letzten 30 Tage oder verschachtelte angepasste Attribute verwendet. Ebenso können Sie [Ihre Nachricht planen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery), damit sie in Realtime basierend auf einer Event-Eigenschaft ausgelöst wird – keine Segmenterweiterung erforderlich.
{% endalert %}

### Schritt 4: Aktualisierungseinstellungen festlegen (optional) {#step-4-designate-refresh-settings-optional}

{% multi_lang_include audience/segments.md section='Refresh settings' %}

### Schritt 5: Segmenterweiterung speichern {#step-5-save-your-segment-extension}

Nachdem Sie **Save** ausgewählt haben, beginnt Ihre Segmenterweiterung mit der Verarbeitung. Die Dauer der Erstellung Ihrer Segmenterweiterung hängt davon ab, wie viele Nutzer:innen Sie haben, wie viele angepasste Events oder Kauf-Events Sie erfassen und wie viele Tage Sie in der Historie zurückblicken.

Während Ihre Segmenterweiterung verarbeitet wird, sehen Sie eine kleine Animation neben dem Namen der Segmenterweiterung und **Processing** in der Spalte **Status** in der Liste der Segmenterweiterungen. Beachten Sie, dass Sie eine Segmenterweiterung während der Verarbeitung nicht bearbeiten können.

![Seite „Segment Extensions“ mit zwei aktiven Erweiterungen.]({% image_buster /assets/img/segment/segment_extension5.png %})

Wenn eine Segmenterweiterung verarbeitet wird, verwendet Braze weiterhin die Versionshistorie des Standard-Segments von vor Beginn der Verarbeitung für die Zielgruppensegmentierung. Die Verarbeitung findet jedes Mal statt, wenn ein Speichern oder Aktualisieren erfolgt, und umfasst das Abfragen und Aktualisieren von Nutzerprofilen – mit anderen Worten, die Mitgliedschaft Ihres Standard-Segments wird nicht sofort aktualisiert. Das bedeutet, dass wir nicht garantieren können, dass eine Nutzer:in in die Segmenterweiterung aufgenommen wird, sobald eine bestimmte Aktualisierung abgeschlossen ist, es sei denn, die Aktion der Nutzer:in wurde vor Beginn der Aktualisierungsverarbeitung durchgeführt. Umgekehrt bleiben Nutzer:innen, die vor der Aktualisierung in der Segmenterweiterung waren und die Kriterien nicht mehr erfüllen, so lange in Ihrem Standard-Segment, bis der Aktualisierungsprozess abgeschlossen ist und die Änderungen angewendet werden.

#### Status der Segmenterweiterungen {#segment-extension-statuses}

Auf der Seite **Segment Extensions** zeigt jede Erweiterung einen **Status** und einen **Last Processed**-Zeitstempel an. Nachdem Sie eine Erweiterung gespeichert oder aktualisiert haben, verwenden Sie diese Spalten, um zu bestätigen, ob die Verarbeitung erfolgreich abgeschlossen wurde.

| Status | Beschreibung |
|---|---|
| Active | Die Erweiterung wurde erfolgreich verarbeitet und steht für die Segmentierung zur Verfügung. **Last Processed** zeigt an, wann die letzte Aktualisierung abgeschlossen wurde. |
| Draft | Die Erweiterung ist gespeichert, wurde aber noch nicht aktiviert. |
| Archived | Die Erweiterung ist archiviert und steht für die Segmentierung nicht zur Verfügung. |
| Refresh disabled | Wiederkehrende Zielgruppen-Updates sind deaktiviert. |
| Processing | Braze verarbeitet einen Speicher- oder Aktualisierungsvorgang. Die Spalte **Status** zeigt **Processing**, eine kleine Animation erscheint neben dem Erweiterungsnamen, und Sie können die Erweiterung nicht bearbeiten, bis die Verarbeitung abgeschlossen ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Status der Segmenterweiterungen" }

Wenn die Verarbeitung nicht erfolgreich abgeschlossen wird, erscheint ein Fehlersymbol neben dem Erweiterungsnamen, obwohl die Spalte **Status** möglicherweise noch **Active** anzeigt. Fahren Sie mit dem Mauszeiger über das Symbol, um den Fehlergrund zu sehen. Wenn Sie einen Fehler erhalten, aber glauben, dass die Erweiterung die Verarbeitung hätte abschließen müssen, versuchen Sie zunächst, die Erweiterung zu aktualisieren – der Status kann veraltet sein.

### Schritt 6: Erweiterung in einem Segment verwenden {#step-6-use-your-extension-in-a-segment}

Nachdem Sie eine Segmenterweiterung erstellt haben, können Sie sie als Filter verwenden, wenn Sie ein Segment erstellen oder eine Zielgruppe für eine Campaign oder ein Canvas definieren. Wählen Sie zunächst **Braze Segment Extension** aus der Filterliste im Abschnitt **User Attributes**.

![Abschnitt „Filters“ mit einem Filter-Dropdown, das „Braze Segment Extensions“ zeigt.]({% image_buster /assets/img/segment/segment_extension7.png %})

Wählen Sie aus der Filterliste der Braze-Segmenterweiterung die Segmenterweiterung aus, die Sie in dieses Segment einschließen oder davon ausschließen möchten.

![Ein Filter „Braze Segment Extensions“, der ein Segment „1 email click in the last 56 days“ enthält.]({% image_buster /assets/img/segment/segment_extension6.png %})

Um die Kriterien der Segmenterweiterung anzuzeigen, wählen Sie **View Extension Details**, um die Details in einem neuen Fenster anzuzeigen.

![Erweiterung für „1 email click in the last 56 days“.]({% image_buster /assets/img/segment/segment_extension8.png %}){: style="max-width:70%;"}

Jetzt können Sie wie gewohnt mit dem [Erstellen Ihres Segments]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) fortfahren.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Kann ich eine Segmenterweiterung erstellen, die mehrere angepasste Events verwendet? {#can-i-create-a-segment-extension-that-uses-multiple-custom-events}

Ja. Sie können mehrere Events hinzufügen oder auf mehrere Snowflake-Tabellen verweisen, wenn Sie [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) verwenden.

Bei der Verwendung von **Einfachen Erweiterungs**-Segmenterweiterungen können Sie ein angepasstes Event, ein Kauf-Event oder eine Kanalinteraktion auswählen. Sie können jedoch beim Erstellen des Standard-Segments mehrere Segmenterweiterungen mit UND oder ODER kombinieren.

### Kann ich Segmenterweiterungen archivieren, wenn sie in einer aktiven Campaign verwendet werden? {#can-i-archive-segment-extensions-if-they-exist-in-an-active-campaign}

Nein. Bevor Sie eine Segmenterweiterung archivieren können, müssen Sie sie aus allen aktiven Messaging-Aktivitäten entfernen.

### Kann ich Arrays in Segmenterweiterungen verwenden? {#can-i-use-arrays-in-segment-extensions}

Ja. Um Arrays zu verwenden, hängen Sie eckige Klammern (`[]`) an Ihren Eigenschaftsnamen an. Wenn Ihre Eigenschaft `location_code` lautet, würden Sie `location_code[]` eingeben.

Braze verwendet `[]`, um Arrays zu durchlaufen und zu prüfen, ob ein Element im durchlaufenen Array mit der Event-Eigenschaft übereinstimmt. So könnten Sie beispielsweise eine Segmenterweiterung von Nutzer:innen erstellen, die mindestens einem Wert einer Array-Eigenschaft entsprechen.

### Wie berechnet Braze den Zeitraum für einen relativen Zeitraum von „letzte __ Tage“? {#how-does-braze-calculate-the-time-period-for-a-relative-time-period-of-last-__-days}

Wenn Segmenterweiterungen den relativen Zeitraum („letzte X Tage“) berechnen, wird die Startzeit auf Mitternacht UTC gesetzt. Beispielsweise wird bei einer Segmenterweiterung, die am 16.09.2024 um 21:00 UTC aktualisiert wird und 10 Tage angibt, die Startzeit auf den 06.09.2024 00:00 UTC gesetzt, nicht auf den 06.09.2024 21:00 UTC.

Sie können jedoch die Zeitzonen festlegen, indem Sie SQL-Segmente verwenden, um Nutzer:innen zu identifizieren, die das angepasste Event vor 10 Tagen basierend auf Mitternacht in der Unternehmenszeit ausgeführt haben, oder Nutzer:innen, die das Event vor 10 Tagen basierend auf der aktuellen Zeit ausgeführt haben.