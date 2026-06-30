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

Die Braze-Segmentierung ermöglicht es Ihnen, Nutzer:innen basierend auf angepassten Events oder Kaufverhalten anzusprechen. Segmenterweiterungen erweitern diese Möglichkeit, indem sie auf historische Daten zurückgreifen, die im Nutzerprofil gespeichert sind. Mit Segmenterweiterungen können Sie Nutzer:innen identifizieren und erreichen, die ein beliebiges angepasstes Event oder Kauf-Event beliebig oft in den letzten zwei Jahren (730 Tagen) abgeschlossen haben.

## Warum Segmenterweiterungen verwenden? {#why-use-segment-extensions}

Braze Segments bieten Ihnen leistungsstarke Targeting-Tools, um dynamische Nutzer:innen-Gruppen zu erstellen. Für die meisten Anwendungsfälle reicht dies aus, um Ihre Zielgruppe effektiv zu erreichen. Segmenterweiterungen sind für fortgeschrittene Anwendungsfälle konzipiert, bei denen Sie Verhaltensweisen von bis zu zwei Jahren analysieren oder komplexe Logik anwenden müssen – ohne die Datenaufbewahrung oder Systemleistung zu beeinträchtigen. Sie können [SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)-Abfragen (SQL-Segmenterweiterungen) oder Daten aus Ihrem eigenen [Data Warehouse]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments) verwenden, um Ihre Zielgruppe weiter zu verfeinern.

Zum Beispiel findet die Standard-Segmentierung von Braze Nutzer:innen, die bestimmte von Ihnen definierte Kriterien erfüllen, wie etwa die Identifizierung von Nutzer:innen, die kürzlich eines Ihrer Produkte gekauft haben. Segmenterweiterungen ermöglichen es Ihnen, tiefer zu gehen – etwa Nutzer:innen zu identifizieren, die eine bestimmte Farbe eines bestimmten Produkts mindestens zweimal zwischen 18 und 24 Monaten gekauft haben. Segmenterweiterungen sind eine Erweiterung, keine Voraussetzung. Wenn Sie fortgeschrittenere Filter oder ein längeres Rückblickfenster benötigen, sind sie ein großartiges Werkzeug, das Ihnen hilft und gleichzeitig Ihre Datennutzung optimiert.

{% alert note %}
Es gibt ein Standardkontingent von 25 aktiven Segmenterweiterungen pro Workspace zu einem bestimmten Zeitpunkt. Wenn Sie dieses Limit erhöhen müssen, wenden Sie sich an Ihren Braze Customer-Success-Manager, um Ihren Anwendungsfall zu besprechen.
{% endalert %}

## Eine Segmenterweiterung erstellen {#creating-a-segment-extension}

Um eine Segmenterweiterung zu erstellen, erstellen Sie einen Filter, um ein Segment Ihrer Nutzer:innen basierend auf angepassten Event-Eigenschaften zu verfeinern. Beim Erstellen einer Segmenterweiterung wählen Sie, ob das Segment statisch sein oder in einem festgelegten Intervall dynamisch aktualisiert werden soll.

### 1. Schritt: Zu Segmenterweiterungen navigieren {#step-1-navigate-to-segment-extensions}

Gehen Sie zu **Audience** > **Segment Extensions**.

Wählen Sie in der Segmenterweiterungen-Tabelle **Create New Extension** und dann Ihre gewünschte Erstellungsmethode für die Segmenterweiterung:

- **Simple extension:** Erstellen Sie eine Segmenterweiterung, die sich auf ein einzelnes Event konzentriert, mithilfe eines geführten Formulars. Am besten geeignet, wenn Sie kein SQL verwenden möchten.
- **Start with a template:** Erstellen Sie ein SQL-Segment mit einem anpassbaren Template unter Verwendung von Snowflake-Daten.
- **Incremental refresh:** Schreiben Sie ein Snowflake-SQL-Segment, das automatisch die Daten der letzten 2 Tage aktualisiert, oder aktualisieren Sie bei Bedarf manuell. Am besten geeignet, um Genauigkeit und Kosteneffizienz in Einklang zu bringen.
- **Full refresh:** Schreiben Sie ein SQL-Segment mit Snowflake-Daten oder einer beliebigen [CDI-verbundenen Quelle]({{site.baseurl}}/cdi_segment_extensions), das die gesamte Zielgruppe bei manueller Aktualisierung neu berechnet. Am besten geeignet, wenn Sie eine vollständige, aktuelle Ansicht Ihrer Zielgruppe benötigen.

![Tabelle mit verschiedenen Erstellungsmethoden für Segmenterweiterungen zur Auswahl.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%"}

Wenn Sie eine Methode auswählen, die SQL verwendet, lesen Sie [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) für weitere Informationen. Wenn Sie **Simple extension** auswählen, fahren Sie mit Schritt 2 fort.

#### SQL-Credit-Verbrauch {#sql-credit-usage}

Die folgenden Segmenterweiterungstypen verbrauchen SQL-Credits:

- SQL-Segmenterweiterungen (sowohl inkrementelle als auch vollständige Aktualisierung)
- Katalogsegmente
- CDI-Segmente
    - Credits werden in Ihrem eigenen Data Warehouse verbraucht

### 2. Schritt: Ihre Segmenterweiterung benennen {#step-2-name-your-segment-extension}

Benennen Sie Ihre Segmenterweiterung, indem Sie die Art der Nutzer:innen beschreiben, die Sie filtern möchten. So stellen Sie sicher, dass diese Erweiterung leicht und korrekt gefunden werden kann, wenn Sie sie als Filter in Ihrem Segment anwenden.

![Segmenterweiterung mit dem Namen „Online Shoppers Extension - 90 Days“.]({% image_buster /assets/img/segment/segment_extension2.png %})

### 3. Schritt: Ihre Kriterien auswählen {#step-3-choose-your-criteria}

Wählen Sie zwischen Kauf-, Nachrichten-Engagement-, empfohlenen E-Commerce-Event- oder angepassten Event-Kriterien für das Targeting. Nachdem Sie die gewünschten Event-Typ-Kriterien ausgewählt haben, wählen Sie, welchen gekauften Artikel, welche Nachrichteninteraktion, welches empfohlene E-Commerce-Event oder welches angepasste Event Sie für Ihre Nutzer:innen-Liste ansprechen möchten. Wählen Sie dann, wie oft (mehr als, weniger als oder gleich) die Nutzer:innen das Event abgeschlossen haben müssen, und den Zeitraum – speziell für Segmenterweiterungen können Sie bis zu 730 Tage (2 Jahre) zurückblicken.

Segmentierung basierend auf Event-Daten von mehr als 730 Tagen kann mit anderen Filtern unter **Segments** durchgeführt werden. Bei der Auswahl Ihres Zeitraums können Sie einen relativen Datumsbereich angeben, um die letzten X Tage auszuwählen, ein Startdatum, ein Enddatum oder einen genauen Datumsbereich (Datum A bis Datum B).

![Segmentierungskriterien für Nutzer:innen, die ein angepasstes Event mehr als 2 Mal im Datumsbereich vom 1. März 2025 bis 31. März 2025 durchgeführt haben.]({% image_buster /assets/img/segment/segment_extension1.png %})

Wenn Sie eine Segmenterweiterung mit einem empfohlenen E-Commerce-Event erstellen, wählen Sie zunächst **eCommerce Recommended Event** als Kriterium und dann ein Event aus dem Dropdown-Menü.

![Ein Kriterium für ein empfohlenes E-Commerce-Event mit einem Dropdown-Menü der verfügbaren empfohlenen Events.]({% image_buster /assets/img/segment/ecommerce_recommended_event_criterion.png %})

#### Event-Eigenschafts-Segmentierung {#event-property-segmentation}

Um die Targeting-Präzision zu erhöhen, aktivieren Sie das Kontrollkästchen **Add Property Filters**. Damit können Sie basierend auf den spezifischen Eigenschaften Ihres Kaufs oder angepassten Events filtern. Wir unterstützen Event-Eigenschafts-Segmentierung basierend auf String-, numerischen, booleschen und Zeitobjekten.

Für String-Eigenschaften können Sie mehrere Werte gleichzeitig eingeben. Im folgenden Beispiel sucht dieser Filter nach Nutzer:innen mit einem Status, der einem der folgenden Werte entspricht: Gold, Silber oder Bronze.

![Segmentierung basierend auf String-Eigenschaften.]({% image_buster /assets/img/segment/property5.png %})

![Segmentierung basierend auf numerischen Eigenschaften.]({% image_buster /assets/img/segment/property2.png %})

![Segmentierung basierend auf booleschen Eigenschaften.]({% image_buster /assets/img/segment/property3.png %})

![Segmentierung basierend auf Datums-/Zeitobjekten.]({% image_buster /assets/img/segment/property4.png %})

Wenn Sie empfohlene E-Commerce-Events verwenden und eine Event-Eigenschaft hinzufügen, wird das Eigenschafts-Dropdown automatisch mit den für dieses spezifische empfohlene E-Commerce-Event verfügbaren Eigenschaften befüllt.

![Segmenterweiterungs-Details mit einem Dropdown-Menü der verfügbaren Eigenschaften.]({% image_buster /assets/img/segment/ecommerce_recommended_event_properties.png %})

Wir unterstützen auch Segmentierung basierend auf [verschachtelten Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects). Wählen Sie im Vergleichs-Dropdown den Vergleich aus, der zum Datentyp Ihrer verschachtelten Eigenschaft passt. Sie können dieselbe Syntax für verschachtelte Event-Eigenschaften verwenden, um verschachtelte Eigenschaften für alle empfohlenen E-Commerce-Events hinzuzufügen, die verschachtelte Eigenschaften enthalten. Informationen zu den verschiedenen verfügbaren verschachtelten Eigenschaften finden Sie unter [Typen empfohlener E-Commerce-Events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events#types-of-ecommerce-recommended-events). Um das erforderliche Schema für den Eigenschaftsnamen Ihrer Segmenterweiterung zu generieren, folgen Sie den Schritten unter [Verschachtelte Objekte in angepassten Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects).

![Segmentierung basierend auf verschachtelten Event-Eigenschaften.]({% image_buster /assets/img/segment/nested_segment_extensions.png %})

Segmenterweiterungen basieren auf der Langzeitspeicherung von Event-Eigenschaften und haben kein zeitgestempeltes Eigenschaftsspeicherlimit. Sie können auf Event-Eigenschaften zurückblicken, die in den letzten zwei Jahren erfasst wurden. Die Verwendung von Event-Eigenschaften innerhalb von Segmenterweiterungen hat keinen Einfluss auf den Datenpunkt-Verbrauch.

{% alert note %}
Sie benötigen keine Segmenterweiterungen, um Event-Eigenschaften oder verschachtelte angepasste Attribute in Ihrem Segment zu verwenden. Segmenterweiterungen erweitern lediglich das historische Fenster, das zur Erstellung eines Standard-Segments verwendet wird. Sie können ein Realtime-Standard-[Segment]({{site.baseurl}}/user_guide/audience/segments) erstellen, das Event-Eigenschaften der letzten 30 Tage oder verschachtelte angepasste Attribute verwendet. Ebenso können Sie [Ihre Nachricht planen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery), um in Realtime basierend auf einer Event-Eigenschaft ausgelöst zu werden – keine Segmenterweiterung erforderlich.
{% endalert %}

### 4. Schritt: Aktualisierungseinstellungen festlegen (optional) {#step-4-designate-refresh-settings-optional}

{% multi_lang_include audience/segments.md section='Refresh settings' %}

### 5. Schritt: Ihre Segmenterweiterung speichern {#step-5-save-your-segment-extension}

Nachdem Sie **Save** ausgewählt haben, beginnt Ihre Segmenterweiterung mit der Verarbeitung. Die Dauer der Generierung Ihrer Segmenterweiterung hängt davon ab, wie viele Nutzer:innen Sie haben, wie viele angepasste Events oder Kauf-Events Sie erfassen und wie viele Tage Sie in der Historie zurückblicken.

Während Ihre Segmenterweiterung verarbeitet wird, sehen Sie eine kleine Animation neben dem Namen der Segmenterweiterung und das Wort „Processing“ in der Spalte **Last Processed** in der Segmenterweiterungsliste. Beachten Sie, dass Sie eine Segmenterweiterung nicht bearbeiten können, während sie verarbeitet wird.

![Seite „Segment Extensions“ mit zwei aktiven Erweiterungen.]({% image_buster /assets/img/segment/segment_extension5.png %})

Wenn eine Segmenterweiterung verarbeitet wird, verwendet Braze weiterhin die Versionshistorie des Standard-Segments von vor Beginn der Verarbeitung für Zielgruppen-Segmentierungszwecke. Die Verarbeitung findet jedes Mal statt, wenn ein Speichern oder Aktualisieren erfolgt, und umfasst das Abfragen und Aktualisieren von Nutzerprofilen – mit anderen Worten, die Mitgliedschaft Ihres Standard-Segments wird nicht sofort aktualisiert. Das bedeutet, dass wir nicht garantieren können, dass Nutzer:innen in die Segmenterweiterung aufgenommen werden, wenn ihre Aktion nicht vor Beginn der Aktualisierungsverarbeitung durchgeführt wurde. Umgekehrt werden Nutzer:innen, die vor der Aktualisierung in der Segmenterweiterung waren und die Kriterien nicht mehr erfüllen, weiterhin Ihrem Standard-Segment zugeordnet, bis der Aktualisierungsprozess abgeschlossen ist und die Änderungen angewendet werden.

### 6. Schritt: Ihre Erweiterung in einem Segment verwenden {#step-6-use-your-extension-in-a-segment}

Nachdem Sie eine Segmenterweiterung erstellt haben, können Sie sie als Filter verwenden, wenn Sie ein Segment erstellen oder eine Zielgruppe für eine Campaign oder ein Canvas definieren. Wählen Sie zunächst **Braze Segment Extension** aus der Filterliste im Abschnitt **User Attributes**.

![Abschnitt „Filters“ mit einem Filter-Dropdown, das „Braze Segment Extensions“ anzeigt.]({% image_buster /assets/img/segment/segment_extension7.png %})

Wählen Sie aus der Braze-Segmenterweiterungs-Filterliste die Segmenterweiterung aus, die Sie in dieses Segment einschließen oder ausschließen möchten.

![Ein „Braze Segment Extensions“-Filter, der ein Segment „1 email click in the last 56 days“ einschließt.]({% image_buster /assets/img/segment/segment_extension6.png %})

Um die Kriterien der Segmenterweiterung anzuzeigen, wählen Sie **View Extension Details**, um die Details in einem neuen Fenster anzuzeigen.

![Erweiterung für „1 email click in the last 56 days“.]({% image_buster /assets/img/segment/segment_extension8.png %}){: style="max-width:70%;"}

Jetzt können Sie wie gewohnt mit dem [Erstellen Ihres Segments]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) fortfahren.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Kann ich eine Segmenterweiterung erstellen, die mehrere angepasste Events verwendet? {#can-i-create-a-segment-extension-that-uses-multiple-custom-events}

Ja. Sie können mehrere Events hinzufügen oder mehrere Snowflake-Tabellen referenzieren, wenn Sie [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) verwenden.

Bei Verwendung von **Simple extension**-Segmenterweiterungen können Sie ein angepasstes Event, ein Kauf-Event oder eine Kanalinteraktion auswählen. Sie können jedoch mehrere Segmenterweiterungen mit AND oder OR kombinieren, wenn Sie das Standard-Segment erstellen.

### Kann ich Segmenterweiterungen archivieren, wenn sie in einer aktiven Campaign existieren? {#can-i-archive-segment-extensions-if-they-exist-in-an-active-campaign}

Nein. Bevor Sie eine Segmenterweiterung archivieren können, müssen Sie sie aus allen aktiven Nachrichten entfernen.

### Kann ich Arrays in Segmenterweiterungen verwenden? {#can-i-use-arrays-in-segment-extensions}

Ja. Um Arrays zu verwenden, hängen Sie eckige Klammern (`[]`) an Ihren Eigenschaftsnamen an. Wenn Ihre Eigenschaft `location_code` ist, würden Sie `location_code[]` eingeben.

Braze verwendet `[]`, um Arrays zu durchlaufen und zu prüfen, ob ein Element im durchlaufenen Array mit der Event-Eigenschaft übereinstimmt. Zum Beispiel könnten Sie eine Segmenterweiterung von Nutzer:innen erstellen, die mindestens einem Wert einer Array-Eigenschaft entsprechen.

### Wie berechnet Braze den Zeitraum für einen relativen Zeitraum von „letzte __ Tage“? {#how-does-braze-calculate-the-time-period-for-a-relative-time-period-of-last-__-days}

Wenn Segmenterweiterungen den relativen Zeitraum („letzte X Tage“) berechnen, wird die Startzeit auf Mitternacht UTC gesetzt. Zum Beispiel wird bei einer Segmenterweiterung, die am 16.09.2024 um 21:00 UTC aktualisiert wird und 10 Tage angibt, die Startzeit auf den 06.09.2024 um 00:00 UTC gesetzt, nicht auf den 06.09.2024 um 21:00 UTC.

Sie können jedoch die Zeitzonen angeben, indem Sie SQL-Segmente verwenden, um Nutzer:innen zu identifizieren, die das angepasste Event vor 10 Tagen basierend auf Mitternacht in der Unternehmenszeit durchgeführt haben, oder Nutzer:innen, die das Event vor 10 Tagen basierend auf der aktuellen Uhrzeit durchgeführt haben.