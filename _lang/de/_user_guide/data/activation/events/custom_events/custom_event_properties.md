---
nav_title: Angepasste Event-Eigenschaften
article_title: Angepasste Event-Eigenschaften
page_order: 0
page_type: reference
description: "Dieser Artikel beschreibt angepasste Event-Eigenschaften, ihr erwartetes Format, wie Sie sie verwenden können und die Speicherung angepasster Event-Eigenschaften."
---

# Angepasste Event-Eigenschaften {#custom-event-properties}

> Dieser Artikel beschreibt angepasste Event-Eigenschaften, ihr erwartetes Format, wie Sie sie für Messaging und Segmentierung verwenden können und die Speicherung angepasster Event-Eigenschaften.

Angepasste Event-Eigenschaften sind Metadaten oder Attribute eines angepassten Events, die ein bestimmtes Vorkommen eines Events beschreiben. Diese Eigenschaften können verwendet werden, um Trigger-Bedingungen weiter zu qualifizieren, die Personalisierung im Messaging zu erhöhen, Conversions zu tracken und durch den Export von Rohdaten anspruchsvollere Analytics zu erstellen.

Angepasste Event-Eigenschaften werden nicht im Braze-Profil gespeichert und verbrauchen daher keine Datenpunkte (siehe [Datenpunkte](#data-points) für Ausnahmen).

{% alert important %}
Jedes angepasste Event oder jeder Kauf kann bis zu 256 verschiedene angepasste Event-Eigenschaften haben. Wenn ein angepasstes Event oder ein Kauf mit mehr als 256 Eigenschaften protokolliert wird, werden nur die ersten 256 erfasst und stehen zur Verfügung.
{% endalert %}

## Erwartetes Format {#expected-format}

Eigenschaftswerte müssen ein Objekt sein: Schlüssel sind die Eigenschaftsnamen (nicht-leere Strings, 255 Zeichen oder weniger, kein führendes `$`), und Werte sind die Eigenschaftswerte. Informationen zu unterstützten Datentypen, Formatanforderungen und Payload-Limits finden Sie unter [Datentypen]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#event-property-data-types).

Sie können den Datentyp Ihrer angepassten Event-Eigenschaft ändern, sollten sich aber der Auswirkungen bewusst sein, die das [Ändern von Datentypen]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#changing-custom-attribute-or-event-data-type) nach der Datenerfassung mit sich bringt.

### Reservierte Schlüssel {#reserved-keys}

Sie können keine reservierten Schlüssel als Event-Eigenschaftsnamen verwenden. Die Verwendung eines reservierten Schlüssels im `properties`-Objekt gibt den Fehler „Invalid 'properties' field“ zurück.

| Eigenschaft | Reservierter Schlüssel |
| --- | --- |
| Angepasste Events | `time` und `event_name` |
| Kauf-Events | `time`, `product_id`, `quantity`, `event_name`, `price`, `currency` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Reservierte Schlüssel" }

## Angepasste Event-Eigenschaften verwenden {#using-custom-event-properties}

Angepasste Event-Eigenschaften können verwendet werden, um Campaign-Trigger zu qualifizieren, Konversionen zu verfolgen und Nachrichten zu personalisieren.

### Nachrichten triggern {#trigger-messages}

Verwenden Sie angepasste Event-Eigenschaften, um Ihre Zielgruppe für eine bestimmte Campaign oder ein Canvas weiter einzugrenzen. Wenn Sie beispielsweise eine E-Commerce-Anwendung haben und eine Nachricht an Nutzer:innen senden möchten, die ihren Warenkorb abgebrochen haben, können Sie eine angepasste Event-Eigenschaft `price` hinzufügen, um Ihre Zielgruppe zu verbessern und eine stärkere Campaign-Personalisierung zu ermöglichen.

![Filter für angepasste Event-Eigenschaften bei einem Warenkorb-Abbruch. Zwei Filter werden mit einem UND-Operator kombiniert, um diese Campaign an Nutzer:innen zu senden, die ihren Warenkorb mit einem Preis zwischen 100 und 200 Dollar abgebrochen haben.]({% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png"){: style="max-width:70%;"}

Verschachtelte angepasste Event-Eigenschaften werden auch bei der [aktionsbasierten Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) unterstützt.

![Filter für angepasste Event-Eigenschaften bei einem Warenkorb-Abbruch. Ein Filter ist ausgewählt, wenn ein Artikel im Warenkorb einen Preis von mehr als 100 Dollar hat.]({% image_buster /assets/img_archive/customEventPropertiesNested.png %} "customEventPropertiesNested.png"){: style="max-width:70%;"}

### Nachrichten personalisieren {#personalize-messages}

Sie können angepasste Event-Eigenschaften auch für die Personalisierung innerhalb des Messaging-Templates verwenden. Jede Campaign, die [aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) mit einem Trigger-Event verwendet, kann angepasste Event-Eigenschaften dieses Events für die Messaging-Personalisierung nutzen.

#### Hinweise zu Filtern {#considerations-with-filters}

- **API-Aufrufe:** Wenn Sie API-Aufrufe durchführen und den Filter „ist leer“ verwenden, wird eine angepasste Event-Eigenschaft als „leer“ betrachtet, wenn sie im Aufruf nicht enthalten ist. Wenn Sie beispielsweise `"event_property": ""` einschließen, werden Ihre Nutzer:innen als „nicht leer“ betrachtet.
- **Ganzzahlen:** Wenn Sie nach einer numerischen angepassten Event-Eigenschaft filtern und die Zahl sehr groß ist, verwenden Sie nicht den Filter „genau“. Wenn eine Zahl zu groß ist, wird sie möglicherweise ab einer bestimmten Länge gerundet, sodass Ihr Filter nicht wie erwartet funktioniert.

#### Typumwandlung für Vergleiche {#type-coercion-for-comparisons}

Wenn Sie Event-Eigenschaften in bedingten Liquid-Anweisungen verwenden, kann der Fehler `Liquid error: comparison of String with 0 failed` auftreten, wenn Sie eine ganzzahlige Event-Eigenschaft mit Operatoren wie „größer als“, „kleiner als“ oder „gleich“ vergleichen. Dies geschieht, weil Liquid die Eigenschaft standardmäßig als String behandelt.

Um dies zu beheben, verwenden Sie den Filter `plus: 0`, um die Eigenschaft vor dem Vergleich in eine Zahl umzuwandeln:

{% raw %}
```liquid
{% assign time_spent = {{event_properties.${time_spent}}} | plus: 0 %}
{% if time_spent >= 100 %}
  Great job completing the level quickly!
{% endif %}
```
{% endraw %}

Wenn Sie beispielsweise eine Gaming-App haben und eine Nachricht an Nutzer:innen senden möchten, die ein Level abgeschlossen haben, könnten Sie Ihre Nachricht mit einer Eigenschaft für die Zeit, die Nutzer:innen zum Abschließen des Levels benötigt haben, weiter personalisieren.

Die folgende Nachricht ist für drei verschiedene Segmente mithilfe von [bedingter Logik]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic) personalisiert. Die angepasste Event-Eigenschaft `time_spent` kann in die Nachricht eingebunden werden, indem ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}`` aufgerufen wird.

{% raw %}
```liquid
{% assign time_spent = {{event_properties.${time_spent}}} | plus: 0 %}
{% if time_spent < 600 %}
Incredible work, hero! Are you ready to test your skills against other powerful heroes? Visit the Arena for real-time battles with top players from around the globe.
{% elsif time_spent < 1800 %}
Great job, hero! Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Well done, hero! Talk to villagers for tips on how to beat levels faster and unlock more rewards.
{% endif %}
```
{% endraw %}

{% alert warning %}
Wenn Nutzer:innen keine Internetverbindung haben, schlagen getriggerte In-App-Nachrichten mit vorlagenbasierten angepassten Event-Eigenschaften (z. B. {% raw %}``{{event_properties.${time_spent}}}``{% endraw %}) fehl und werden nicht angezeigt.
{% endalert %}

Eine vollständige Liste der Liquid-Tags, die dazu führen, dass In-App-Nachrichten als vorlagenbasierte In-App-Nachrichten zugestellt werden, finden Sie unter [Häufig gestellte Fragen]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages).

#### Canvas {#canvas}

In Canvas dienen `context` und `event_properties` unterschiedlichen Zwecken:

- **`context`**: Eigenschaften des Events oder API-Aufrufs, der den Canvas-Eintritt ausgelöst hat. Verwenden Sie `context` in jedem Nachrichtenschritt, einschließlich des ersten.
- **`event_properties`**: Eigenschaften eines angepassten Events oder Kaufs, der während der Journey stattfindet. Verwenden Sie sie nur im ersten Nachrichtenschritt nach einem [Aktionspfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)-Schritt – nicht auf dem „Alle anderen“-Pfad und nicht in späteren Nachrichtenschritten.

{% alert important %}
Verwenden Sie im ersten Nachrichtenschritt eines Canvas `context` anstelle von `event_properties`, oder fügen Sie einen Aktionspfade-Schritt vor dem Nachrichtenschritt hinzu. Ausnahme: Bei In-App-Nachrichten können Sie `event_properties` im ersten Nachrichtenschritt verwenden, wenn dieses Event der Canvas-Entry-Trigger ist.
{% endalert %}

Weitere Informationen finden Sie unter [Context und Event-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) und [Canvas-Entry-Eigenschaften und Event-Eigenschaften](#canvas-entry-properties-and-event-properties).

### Segmentierung {#segmentation}

Verwenden Sie die Event-Eigenschafts-Segmentierung, um Nutzer:innen basierend auf durchgeführten angepassten Events und den mit diesen Events verknüpften Eigenschaften anzusprechen. Dies erweitert Ihre Filteroptionen bei der Segmentierung nach Käufen und angepassten Events.

Event-Eigenschaften für angepasste Events werden in Realtime für jedes Segment aktualisiert, das sie verwendet. Sie können Eigenschaften verwalten, indem Sie zu **Dateneinstellungen** > **Angepasste Events** gehen und **Eigenschaften verwalten** für das zugehörige angepasste Event auswählen. Angepasste Event-Eigenschaften, die in bestimmten Segment-Filtern verwendet werden, haben einen maximalen Rückblickzeitraum von 30 Tagen.

#### Event-Eigenschaften für die Segmentierung hinzufügen {#adding-event-properties-for-segmentation}

Sie benötigen die Nutzer:innenberechtigung „Edit Custom Event Property Segmentation“ ([Nutzer:innenberechtigung]({{site.baseurl}}/user_guide/data/infrastructure/data_points#viewing-data-point-usage)), um Segmente basierend auf der Aktualität und Häufigkeit von Event-Eigenschaften zu erstellen.

Standardmäßig können Sie 20 segmentierbare Event-Eigenschaften pro Workspace haben. Wenden Sie sich an Ihren Braze Account Manager, um dieses Limit zu erhöhen.

Um Event-Eigenschaften für die Segmentierung hinzuzufügen, gehen Sie wie folgt vor:

1. Gehen Sie zu Ihrem angepassten Event und wählen Sie **Eigenschaften verwalten**.
2. Wählen Sie den Schalter **Segmentierung aktivieren**, um die Event-Eigenschaft für die Segmentierung hinzuzufügen. Beim Segmentieren stehen Ihnen dann zusätzliche Filteroptionen zur Verfügung.

Die Filter für die Event-Eigenschafts-Segmentierung umfassen:

{% multi_lang_include data_activation/custom_event_property_filters.md %}

![Eine Filtergruppe mit „Warenkorb-Abbruch“ mit der Eigenschaft „Anzahl der Artikel“ und dem Wert 2, mehr als 1 Mal in den letzten 30 Kalendertagen.]({% image_buster /assets/img/nested_object3.png %})

Daten werden erst protokolliert, nachdem Sie eine bestimmte Event-Eigenschaft aktiviert haben, und Event-Eigenschaften sind erst ab diesem Datum verfügbar.

#### Datenpunkte {#data-points}

In Bezug auf die Abo-Nutzung werden angepasste Event-Eigenschaften, die für die Segmentierung mit den folgenden Filtern aktiviert sind, jeweils als separate Datenpunkte gezählt – zusätzlich zu dem Datenpunkt, der durch das angepasste Event selbst gezählt wird:

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### Canvas-Entry-Eigenschaften und Event-Eigenschaften {#canvas-entry-properties-and-event-properties}

{% multi_lang_include canvas/entry_event_properties.md %}

### Verschachtelte Objekte {#nested-objects}

Sie können verschachtelte Objekte (Objekte innerhalb eines anderen Objekts) verwenden, um verschachtelte JSON-Daten als Eigenschaften von angepassten Events und Käufen zu senden. Diese verschachtelten Daten können für die Vorlagenerstellung personalisierter Informationen in Nachrichten, das Triggern von Nachrichtenversendungen und die Segmentierung von Nutzer:innen verwendet werden.

Weitere Informationen finden Sie auf unserer speziellen Seite zu [Verschachtelte Objekte]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects).

## Speicherung angepasster Event-Eigenschaften {#custom-event-property-storage}

Angepasste Event-Eigenschaften helfen Ihnen, die Targeting-Präzision zu erhöhen und Nachrichten noch persönlicher zu gestalten. Angepasste Event-Eigenschaften können in Braze sowohl kurz- als auch langfristig gespeichert werden.

Sie können auf zwei Arten basierend auf den Werten von Event-Eigenschaften segmentieren:

1. **Innerhalb von 30 Tagen:** Sie können die Segmentierung nach Event-Eigenschaften basierend auf der Häufigkeit und Aktualität bestimmter Event-Eigenschaftswerte innerhalb von Braze-Segments verwenden. Diese Option wirkt sich auf die Datennutzung aus.<br><br>
2. **Innerhalb und über 30 Tage hinaus:** Um sowohl die kurz- als auch die langfristige Segmentierung nach Event-Eigenschaften abzudecken, können Sie [Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension) verwenden. Dieses Feature segmentiert Nutzer:innen basierend auf angepassten Events und Event-Eigenschaften, die innerhalb der letzten zwei Jahre erfasst wurden. Diese Option wirkt sich nicht auf die Datennutzung aus.

Wenden Sie sich an Ihren Customer-Success-Manager bei Braze, um Empfehlungen zum besten Ansatz für Ihre spezifischen Anforderungen zu erhalten.