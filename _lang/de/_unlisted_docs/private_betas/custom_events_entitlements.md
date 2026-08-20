---
article_title: Angepasste Events
permalink: "/custom_events_entitlements/"
hidden: true
---

# [![Braze-Lernkurs]({% image_buster /assets/unlisted_docs/img/logos/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Angepasste Events {#braze-learning-course-image_buster-assetsunlisted_docsimglogosbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-events}

> Dieser Artikel beschreibt angepasste Events und Eigenschaften, zugehörige Segmentierungsfilter, Canvas-Entry-Eigenschaften, relevante Analytics und mehr. Um mehr über Braze-Events im Allgemeinen zu erfahren, lesen Sie [Events]({{site.baseurl}}/user_guide/data/custom_data/events).

Angepasste Events sind Aktionen, die von Ihren Nutzer:innen durchgeführt werden, oder Updates über diese. Wenn angepasste Events protokolliert werden, können sie eine beliebige Anzahl und Art von Folgekampagnen auslösen. Sie können dann [Segmentierungsfilter](#segmentation-filters) verwenden, um Nutzer:innen danach zu segmentieren, wie kürzlich und wie häufig diese angepassten Events aufgetreten sind. Damit eignen sich angepasste Events am besten für das Tracking von hochwertigen Nutzerinteraktionen innerhalb Ihrer Anwendung.

## Anwendungsfälle {#use-cases}

Einige gängige Anwendungsfälle für angepasste Events sind:

{% multi_lang_include data_activation/custom_event_use_cases.md %}

## Berechtigungen {#entitlements}

Berechtigungen bestimmen Ihre Kapazität für angepasste Events, die die Anzahl der verschiedenen Event-Namen erfasst, die Sie definieren. Pro Workspace können Sie bis zu 2.000 angepasste Events verwenden. Wenn Sie Ihre Kapazität erhöhen müssen, wenden Sie sich an Ihren Braze Account Manager für weitere Informationen.

Wenn sich Ihr Workspace der maximalen Anzahl angepasster Events nähert, erhalten Sie Benachrichtigungen im Dashboard und per E-Mail, damit Sie den Überblick behalten.

Auch nach Erreichen der Kapazitätsgrenze können bestehende angepasste Events weiterhin empfangen werden. Sie können jedoch keine neuen angepassten Events erstellen. Daten, die für angepasste Events empfangen werden, die noch nicht existieren, werden nicht verarbeitet.

## Angepasste Events verwalten {#managing-custom-events}

Sie können angepasste Events im Dashboard verwalten, erstellen oder auf die Blockliste setzen, indem Sie zu **Dateneinstellungen** > **Angepasste Events** navigieren.

Wählen Sie das Menü neben einem angepassten Event für die folgenden Aktionen aus:

### Auf die Blockliste setzen {#blocklisting}

Sie können einzelne angepasste Events über das Aktionsmenü auf die Blockliste setzen oder bis zu 100 Events gleichzeitig auswählen und in einem Schritt auf die Blockliste setzen.

Wenn Sie ein angepasstes Event blockieren:

{% multi_lang_include data_activation/custom_event_block_effects.md %}

Wenn ein blockiertes angepasstes Event derzeit von Filtern oder Triggern in anderen Bereichen von Braze referenziert wird, erscheint zusätzlich ein Warnhinweis-Modal, das erklärt, dass alle Instanzen der Filter oder Trigger, die darauf verweisen, entfernt und archiviert werden.

### Beschreibungen hinzufügen {#adding-descriptions}

Sie können einem angepassten Event nach der Erstellung eine Beschreibung hinzufügen, wenn Sie über die [Nutzerberechtigung]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions) `Manage Events, Attributes, Purchases` verfügen. Wählen Sie **Beschreibung bearbeiten** für das angepasste Event aus und geben Sie ein, was Sie möchten, z. B. eine Notiz für Ihr Team.

## Tags hinzufügen {#adding-tags}

Sie können Tags zu einem angepassten Event hinzufügen, nachdem es erstellt wurde, sofern Sie über die Nutzerberechtigung „Events, Attribute und Käufe verwalten“ verfügen ([Nutzerberechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions)). Die Tags können dann verwendet werden, um die Liste der Events zu filtern.

### Nutzungsberichte anzeigen {#viewing-usage-reports}

Der Nutzungsbericht listet alle Canvases, Campaigns und Segmente auf, die ein bestimmtes angepasstes Event verwenden. Die Liste enthält keine Verwendungen von Liquid.

Sie können bis zu 100 Nutzungsberichte gleichzeitig anzeigen, indem Sie die Kontrollkästchen für mehrere angepasste Events aktivieren und dann **Nutzungsbericht anzeigen** auswählen.

## Daten exportieren {#exporting-data}

Um die Liste der angepassten Events als CSV-Datei zu exportieren, wählen Sie den Button **Export all** oben auf der Seite. Die CSV-Datei wird generiert, und ein Download-Link wird Ihnen per E-Mail zugesendet.

## Angepasste Events protokollieren {#logging-custom-events}

Angepasste Events erfordern eine zusätzliche Einrichtung. In den folgenden plattformspezifischen Dokumentationslinks finden Sie die Methoden zum Protokollieren angepasster Events sowie zum Hinzufügen von Eigenschaften und Mengen.

{% details Dokumentation nach Plattform aufklappen %}

- [Android und FireOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
- [Internet]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events/?sdktab=unity)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=roku)

{% enddetails %}

## Speicherung angepasster Events {#custom-event-storage}

Alle auf dem **Nutzerprofil** gespeicherten Daten, einschließlich Metadaten angepasster Events (erstes oder letztes Vorkommen, Gesamtanzahl und X in Y über 30 Tage), werden unbegrenzt aufbewahrt, solange jedes Profil [aktiv]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival#active-users) ist.

## Segmentierungsfilter {#segmentation-filters}

Die folgende Tabelle zeigt die verfügbaren Filter zur Segmentierung von Nutzer:innen nach angepassten Events.

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen |
| ---------------------| --------------- | ------------- |
| Prüfen, ob das angepasste Event **mehr als X Mal** aufgetreten ist | **MORE THAN** | **NUMBER** |
| Prüfen, ob das angepasste Event **weniger als X Mal** aufgetreten ist | **LESS THAN** | **NUMBER** |
| Prüfen, ob das angepasste Event **genau X Mal** aufgetreten ist | **EXACTLY** | **NUMBER** |
| Prüfen, ob das angepasste Event zuletzt **nach dem Datum X** aufgetreten ist | **AFTER** | **TIME** |
| Prüfen, ob das angepasste Event zuletzt **vor dem Datum X** aufgetreten ist | **BEFORE** | **TIME** |
| Prüfen, ob das angepasste Event zuletzt **vor mehr als X Tagen** aufgetreten ist | **MORE THAN** | **NUMBER OF DAYS AGO** (positive Zahl) |
| Prüfen, ob das angepasste Event zuletzt **vor weniger als X Tagen** aufgetreten ist | **LESS THAN** | **NUMBER OF DAYS AGO** (positive Zahl) |
| Prüfen, ob das angepasste Event **mehr als X (Max = 50) Mal** aufgetreten ist | **MORE THAN** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** |
| Prüfen, ob das angepasste Event **weniger als X (Max = 50) Mal** aufgetreten ist | **LESS THAN** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** |
| Prüfen, ob das angepasste Event **genau X (Max = 50) Mal** aufgetreten ist | **EXACTLY** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Analytics

Braze erfasst die Anzahl der Vorkommen angepasster Events und den Zeitpunkt der letzten Ausführung durch jede:n Nutzer:in für die Segmentierung. Informationen zur Berichtseinrichtung, zu Filtern und Exportoptionen finden Sie unter [Bericht zu angepassten Events]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report).

Auf der Seite **Bericht zu angepassten Events** können Sie aggregiert sehen, wie oft jedes angepasste Event auftritt. Die grauen Linien, die über die Zeitreihe gelegt werden, zeigen an, wann zuletzt eine Campaign gesendet wurde, was nützlich ist, um zu sehen, wie Ihre Campaigns die Aktivität angepasster Events beeinflusst haben.

![Diagramm der Anzahl angepasster Events auf der Seite „Angepasste Events“ im Dashboard mit Trends für ein angepasstes Event][8]

Sie können auch **Filter** verwenden, um Ihre angepassten Events nach Stunde, monatlich aktiven Nutzer:innen (MAU), Segmenten oder KPI-Formeln aufzuschlüsseln.

{% alert tip %}
[Inkrementieren Sie angepasste Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#integers), um einen Zähler für eine Nutzeraktion ähnlich einem angepassten Event zu führen. Sie können jedoch keine Daten angepasster Attribute in einer Zeitreihe anzeigen. Nutzeraktionen, die nicht in einer Zeitreihe analysiert werden müssen, sollten mit dieser Methode erfasst werden.
{% endalert %}

### Warum Analytics für angepasste Events nicht angezeigt werden {#why-custom-events-analytics-arent-showing}

Segmente, die mit Daten angepasster Events erstellt wurden, können keine früheren historischen Daten aus der Zeit vor ihrer Erstellung anzeigen.

## Angepasste Event-Eigenschaften {#custom-event-properties}

Angepasste Event-Eigenschaften sind angepasste Event-Metadaten oder Attribute, die ein bestimmtes Vorkommen eines Events beschreiben. Diese Eigenschaften können verwendet werden, um Trigger-Bedingungen weiter zu qualifizieren, die Personalisierung im Messaging zu verbessern, Konversionen zu tracken und anspruchsvollere Analytics durch den Export von Rohdaten zu generieren.

Angepasste Event-Eigenschaften werden nicht im Braze-Profil gespeichert und verbrauchen daher keine Datenpunkte (siehe [Datenpunkte](#data-points) für Ausnahmen).

{% alert important %}
Jedes angepasste Event oder jeder Kauf kann bis zu 256 verschiedene angepasste Event-Eigenschaften haben. Wenn ein angepasstes Event oder ein Kauf mit mehr als 256 Eigenschaften protokolliert wird, werden nur die ersten 256 erfasst und stehen zur Verfügung.
{% endalert %}

### Erwartetes Format {#expected-format}

Die Eigenschaftswerte sollten ein Objekt sein, bei dem die Schlüssel die Eigenschaftsnamen und die Werte die Eigenschaftswerte sind. Eigenschaftsnamen müssen nicht-leere Strings mit maximal 255 Zeichen sein, ohne führende Dollarzeichen (`$`).

Eigenschaftswerte können einen der folgenden Datentypen haben:

| Datentyp | Beschreibung |
| --- | --- |
| Zahlen | Als [Ganzzahlen](https://en.wikipedia.org/wiki/Integer) oder [Gleitkommazahlen](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Boolesche Werte | Wert `true` oder `false`. |
| Datumsangaben | Formatiert als Strings im [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)- oder `yyyy-MM-dd'T'HH:mm:ss:SSSZ`-Format. Nicht unterstützt innerhalb von Arrays. |
| Strings | 255 Zeichen oder weniger. |
| Arrays | Arrays können keine Datumsangaben enthalten. |
| Objekte | Objekte werden als Strings aufgenommen. |
| Verschachtelte Objekte | Objekte, die sich innerhalb anderer Objekte befinden. Weitere Informationen finden Sie im Abschnitt [Verschachtelte Objekte](#nested-objects) in diesem Artikel.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Event-Eigenschaftsobjekte, die Array- oder Objektwerte enthalten, können eine Event-Eigenschafts-Payload von bis zu 100&nbsp;KB haben.

Sie können den Datentyp Ihrer angepassten Event-Eigenschaft ändern, sollten sich aber der Auswirkungen bewusst sein, die das [Ändern von Datentypen]({{site.baseurl}}/help/help_articles/data/change_custom_data_type) nach der Datenerfassung hat.

### Angepasste Event-Eigenschaften verwenden {#using-custom-event-properties}

Angepasste Event-Eigenschaften können verwendet werden, um Campaign-Trigger zu qualifizieren, Konversionen zu tracken und Messaging zu personalisieren.

#### Nachrichten triggern {#trigger-messages}

Verwenden Sie angepasste Event-Eigenschaften, um Ihre Zielgruppe für eine bestimmte Campaign oder ein Canvas weiter einzugrenzen. Wenn Sie beispielsweise eine E-Commerce-Anwendung haben und eine Nachricht an Nutzer:innen senden möchten, wenn diese ihren Warenkorb abbrechen, können Sie eine angepasste Event-Eigenschaft `cart value` hinzufügen, um Ihre Zielgruppe zu verbessern und eine stärkere Campaign-Personalisierung zu ermöglichen.

![Filter für angepasste Event-Eigenschaften für einen Warenkorb-Abbruch. Zwei Filter werden mit einem UND-Operator kombiniert, um diese Campaign an Nutzer:innen zu senden, die ihren Warenkorb mit einem Warenkorbwert zwischen 100 und 200 Dollar abgebrochen haben][16]

Verschachtelte angepasste Event-Eigenschaften werden auch bei der [aktionsbasierten Zustellung][19] unterstützt.

![Filter für angepasste Event-Eigenschaften für einen Warenkorb-Abbruch. Ein Filter ist ausgewählt, wenn ein Artikel im Warenkorb einen Preis von mehr als 100 Dollar hat.][20]

#### Nachrichten personalisieren {#personalize-messages}

Sie können angepasste Event-Eigenschaften auch zur Personalisierung innerhalb des Messaging-Templates verwenden. Jede Campaign, die [aktionsbasierte Zustellung][19] mit einem Trigger-Event verwendet, kann angepasste Event-Eigenschaften dieses Events für die Messaging-Personalisierung nutzen.

Wenn Sie beispielsweise eine Gaming-App haben und eine Nachricht an Nutzer:innen senden möchten, die ein Level abgeschlossen haben, könnten Sie Ihre Nachricht mit einer Eigenschaft für die Zeit, die Nutzer:innen zum Abschließen dieses Levels benötigt haben, weiter personalisieren. In diesem Beispiel wird die Nachricht für drei verschiedene Segmente mithilfe von [bedingter Logik][18] personalisiert. Die angepasste Event-Eigenschaft namens `time_spent` kann in die Nachricht eingefügt werden, indem Sie ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}`` aufrufen.

{% raw %}
```liquid
{% if {{event_properties.${time_spent}}} < 600 %}
Incredible work, hero! Are you ready to test your skills against other powerful heroes? Visit the Arena for real-time battles with top players from around the globe.
{% elsif {{event_properties.${time_spent}}} < 1800 %}
Great job, hero! Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Well done, hero! Talk to villagers for tips on how to beat levels faster and unlock more rewards.
{% endif %}
```
{% endraw %}

{% alert warning %}
Wenn Nutzer:innen keine Internetverbindung haben, werden getriggerte In-App-Nachrichten mit vorlagenbasierten angepassten Event-Eigenschaften (z. B. {% raw %}``{{event_properties.${time_spent}}}``{% endraw %}) fehlschlagen und nicht angezeigt.
{% endalert %}

Eine vollständige Liste der Liquid-Tags, die dazu führen, dass In-App-Nachrichten als vorlagenbasierte In-App-Nachrichten zugestellt werden, finden Sie unter [Häufig gestellte Fragen]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/faq/#what-are-templated-in-app-messages/).

##### Hinweise zu Filtern {#considerations-with-filters}

- **API-Aufrufe:** Wenn Sie API-Aufrufe tätigen und den Filter „ist leer“ verwenden, wird eine angepasste Event-Eigenschaft als „leer“ betrachtet, wenn sie aus dem Aufruf ausgeschlossen wird. Wenn Sie beispielsweise `"event_property": ""` einschließen, werden Ihre Nutzer:innen als „nicht leer“ betrachtet.
- **Ganzzahlen:** Wenn Sie nach einer numerischen angepassten Event-Eigenschaft filtern und die Zahl sehr groß ist, verwenden Sie nicht den Filter „genau“. Wenn eine Zahl zu groß ist, wird sie möglicherweise ab einer bestimmten Länge gerundet, sodass Ihr Filter nicht wie erwartet funktioniert.

#### Segmentierung {#segmentation}

Verwenden Sie die Event-Eigenschafts-Segmentierung, um Nutzer:innen basierend auf durchgeführten angepassten Events und den mit diesen Events verknüpften Eigenschaften anzusprechen. Dies erweitert Ihre Filteroptionen bei der Segmentierung nach Käufen und angepassten Events.

Event-Eigenschaften für angepasste Events werden in Echtzeit für jedes Segment aktualisiert, das sie verwendet. Sie können Eigenschaften verwalten, indem Sie zu **Dateneinstellungen** > **Angepasste Events** gehen und **Eigenschaften verwalten** für das zugehörige angepasste Event auswählen. Angepasste Event-Eigenschaften, die in bestimmten Segment-Filtern verwendet werden, haben einen maximalen Rückblickzeitraum von 30 Tagen.

##### Event-Eigenschaften für die Segmentierung hinzufügen {#adding-event-properties-for-segmentation}

Sie benötigen die [Nutzerberechtigung]({{site.baseurl}}/user_guide/data/data_points#viewing-data-point-usage) „Manage Custom Event Property Segmentation“, um Segmente basierend auf der Aktualität und Häufigkeit von Event-Eigenschaften zu erstellen.

Standardmäßig können Sie 20 segmentierbare Event-Eigenschaften pro Workspace haben. Wenden Sie sich an Ihren Braze Account Manager, um dieses Limit zu erhöhen.

Um Event-Eigenschaften für die Segmentierung hinzuzufügen, gehen Sie wie folgt vor:

1. Gehen Sie zu Ihrem angepassten Event und wählen Sie **Eigenschaften verwalten**.
2. Wählen Sie den Schalter **Segmentierung aktivieren**, um die Event-Eigenschaft für die Segmentierung hinzuzufügen. Beim Segmentieren stehen Ihnen dann zusätzliche Filteroptionen zur Verfügung.

Die Event-Eigenschafts-Segmentierungsfilter umfassen:

{% multi_lang_include data_activation/custom_event_property_filters.md %}

![Eine Filtergruppe mit „hat ‚Warenkorb-Abbruch' mit Eigenschaft ‚Anzahl der Artikel' und Wert ‚2' ‚mehr als' ‚1' Mal in den letzten ‚30' Kalendertagen.“][3]

Daten werden erst für eine bestimmte Event-Eigenschaft protokolliert, nachdem sie von Ihrem Customer-Success-Manager aktiviert wurde, und Event-Eigenschaften sind erst ab diesem Datum verfügbar.

##### Datenpunkte {#data-points}

In Bezug auf die Abo-Nutzung werden angepasste Event-Eigenschaften, die für die Segmentierung mit den folgenden Filtern aktiviert sind, jeweils als separate Datenpunkte gezählt – zusätzlich zu dem Datenpunkt, der durch das angepasste Event selbst gezählt wird:

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### Canvas-Entry-Eigenschaften und Event-Eigenschaften {#canvas-entry-properties-and-event-properties}

Sie können `canvas_entry_properties` und `event_properties` in Ihren Canvas-User-Journeys verwenden. Weitere Informationen und Beispiele finden Sie unter [Canvas-Entry-Eigenschaften und Event-Eigenschaften]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties).

{% tabs local %}
{% tab Canvas-Entry-Eigenschaften %}

[Canvas-Entry-Eigenschaften]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object) sind die Eigenschaften, die Sie für Canvases zuordnen, die aktionsbasiert oder API-getriggert sind. Beachten Sie, dass das `canvas_entry_properties`-Objekt eine maximale Größenbeschränkung von 50 KB hat.

{% alert note %}
Speziell für In-App-Nachrichtenkanäle kann `canvas_entry_properties` nur in Canvas Flow und im ursprünglichen Canvas-Editor referenziert werden, wenn Sie persistente Entry-Eigenschaften im ursprünglichen Editor als Teil des vorherigen Early Access aktiviert haben.
{% endalert %}

Für Canvas-Flow-Messaging kann `canvas_entry_properties` in jedem Nachrichtenschritt mit diesem Liquid-Format verwendet werden: ``{% raw %} canvas_entry_properties.${property_name} {% endraw %}``. Beachten Sie, dass die Events angepasste Events oder Kauf-Events sein müssen, um auf diese Weise verwendet zu werden.

#### Anwendungsfall {#use-case}

{% raw %}
Nehmen wir an, ein Einzelhandelsgeschäft, RetailApp, hat die folgende Anfrage: `"canvas_entry_properties" : {"product_name" : "shoes", "product_price" : 79.99}`. RetailApp kann den Produktnamen (shoes) mit dem Liquid `{{canvas_entry_properties.${product_name}}}` in eine Nachricht einfügen.
{% endraw %}

RetailApp kann auch bestimmte Nachrichten für verschiedene `product_name`-Eigenschaften in einem Canvas triggern, das Nutzer:innen anspricht, nachdem sie ein Kauf-Event ausgelöst haben. Beispielsweise können sie unterschiedliche Nachrichten an Nutzer:innen senden, die Schuhe gekauft haben, und an Nutzer:innen, die etwas anderes gekauft haben, indem sie das folgende Liquid in einen Nachrichtenschritt einfügen.

{% raw %}
```markdown
{% if  {{canvas_entry_properties.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
{% endraw %}

{% details Für den ursprünglichen Canvas-Editor erweitern %}

Seit dem 28. Februar 2023 können Sie keine Canvases mehr mit dem ursprünglichen Editor erstellen oder duplizieren. Dieser Abschnitt dient nur als Referenz.

Für Canvases, die mit dem ursprünglichen Editor erstellt wurden, kann `canvas_entry_properties` nur im ersten vollständigen Schritt eines Canvas referenziert werden.

{% enddetails %}
{% endtab %}

{% tab Event-Eigenschaften %}

{% alert important %}
Sie können `event_properties` nicht im ersten Nachrichtenschritt verwenden. Stattdessen müssen Sie `canvas_entry_properties` verwenden oder einen Aktionspfade-Schritt mit dem entsprechenden Event **vor** dem Nachrichtenschritt hinzufügen, der `event_properties` enthält.
{% endalert %}

Event-Eigenschaften beziehen sich auf die Eigenschaften, die Sie für angepasste Events und Käufe festlegen. Diese `event_properties` können in Campaigns mit aktionsbasierter Zustellung und in Canvases verwendet werden.

In Canvas Flow können angepasste Event- und Kauf-Event-Eigenschaften in Liquid in jedem Nachrichtenschritt verwendet werden, der auf einen Aktionspfade-Schritt folgt. Stellen Sie sicher, dass Sie {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} verwenden, wenn Sie auf diese `event_properties` verweisen. Diese Events müssen angepasste Events oder Kauf-Events sein, um auf diese Weise in der Nachrichtenkomponente verwendet zu werden.

Im ersten Nachrichtenschritt nach einem Aktionspfad können Sie `event_properties` verwenden, die sich auf das in diesem Aktionspfad referenzierte Event beziehen. Diese `event_properties` können nur verwendet werden, wenn Nutzer:innen die Aktion tatsächlich durchgeführt haben (und nicht in die Gruppe „Alle anderen“ gegangen sind). Zwischen diesem Aktionspfad und dem Nachrichtenschritt können andere Schritte (die kein weiterer Aktionspfade- oder Nachrichtenschritt sind) liegen.

{% details Für den ursprünglichen Canvas-Editor erweitern %}

Seit dem 28. Februar 2023 können Sie keine Canvases mehr mit dem ursprünglichen Editor erstellen oder duplizieren. Dieser Abschnitt dient nur als Referenz.

Für den ursprünglichen Canvas-Editor können `event_properties` nicht in geplanten vollständigen Schritten verwendet werden. Sie können `event_properties` jedoch im ersten vollständigen Schritt eines aktionsbasierten Canvas verwenden, auch wenn der vollständige Schritt geplant ist.

{% enddetails %}

{% endtab %}
{% endtabs %}

### Verschachtelte Objekte {#nested-objects}

Sie können verschachtelte Objekte (Objekte innerhalb eines anderen Objekts) verwenden, um verschachtelte JSON-Daten als Eigenschaften von angepassten Events und Käufen zu senden. Diese verschachtelten Daten können für die Vorlagen-Personalisierung in Nachrichten, das Triggern von Nachrichtenversendungen und die Segmentierung von Nutzer:innen verwendet werden.

Weitere Informationen finden Sie auf unserer speziellen Seite zu [Verschachtelten Objekten]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects).

## Speicherung angepasster Event-Eigenschaften {#custom-event-property-storage}

Angepasste Event-Eigenschaften helfen Ihnen, die Targeting-Präzision zu erhöhen und Nachrichten noch persönlicher zu gestalten. Angepasste Event-Eigenschaften können in Braze sowohl kurz- als auch langfristig gespeichert werden.

Sie können auf zwei Arten basierend auf den Werten von Event-Eigenschaften segmentieren:

1. **Innerhalb von 30 Tagen:** Braze-Supportmitarbeiter:innen können die Segmentierung nach Event-Eigenschaften basierend auf der Häufigkeit und Aktualität bestimmter Event-Eigenschaftswerte innerhalb von Braze Segments aktivieren. Wenn Sie Event-Eigenschaften innerhalb von Segments nutzen möchten, wenden Sie sich an Ihren Braze Account Executive oder Customer-Success-Manager. Diese Option wirkt sich auf die Datennutzung aus.<br><br>
2. **Innerhalb und über 30 Tage hinaus:** Um sowohl die kurz- als auch die langfristige Segmentierung nach Event-Eigenschaften abzudecken, können Sie [Segmenterweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension) verwenden. Dieses Feature segmentiert Nutzer:innen basierend auf angepassten Events und Event-Eigenschaften, die innerhalb der letzten zwei Jahre erfasst wurden. Diese Option wirkt sich nicht auf die Datennutzung aus.

Wenden Sie sich an Ihren Braze Customer-Success-Manager, um Empfehlungen zum besten Ansatz für Ihre spezifischen Anforderungen zu erhalten.

[1]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_object1.png %}
[2]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_object2.png %}
[3]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_object3.png %}
[4]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_event_properties_segmentation.png %}
[5]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_event_properties_personalization.png %}
[6]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/schema_generation_example.png %}
[8]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/custom_event_analytics_example.png %} "custom_event_analytics_example.png"
[16]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/customEventProperties.png %} "customEventProperties.png"
[18]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[19]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/
[20]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/customEventPropertiesNested.png %} "customEventPropertiesNested.png"