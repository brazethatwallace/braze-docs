---
nav_title: Angepasste Events
article_title: Angepasste Events
page_order: 1
page_type: reference
description: "Dieser Artikel beschreibt angepasste Events und Eigenschaften, Segmentierung, Nutzung, Canvas-Entry-Eigenschaften, wo Sie relevante Analytics einsehen können und vieles mehr."
search_rank: 2
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Angepasste Events {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-events}

> Dieser Artikel beschreibt angepasste Events und Eigenschaften, den Event-Verlauf im Kundenprofil or Nutzerprofil, verwandte Segmentierungsfilter, Canvas-Entry-Eigenschaften, relevante Analytics und mehr. Mehr über Braze-Events im Allgemeinen erfahren Sie unter [Events]({{site.baseurl}}/user_guide/data/activation/events).

Angepasste Events sind Aktionen oder Updates, die von Ihren Nutzer:innen durchgeführt werden. Wenn angepasste Events protokolliert werden, können sie beliebig viele und verschiedene Folgekampagnen auslösen. Mit Hilfe von [Segmentierungsfiltern](#segmentation-filters) können Sie Nutzer:innen dann danach segmentieren, wie kürzlich und wie häufig diese angepassten Events aufgetreten sind. Dadurch eignen sich angepasste Events am besten für das Tracking hochwertiger Nutzer:innen-Interaktionen innerhalb Ihrer Anwendung.

## Anwendungsfälle {#use-cases}

Einige häufige Anwendungsfälle für angepasste Events sind:

{% multi_lang_include data_activation/custom_event_use_cases.md %}

## Verwalten angepasster Events {#managing-custom-events}

Sie können angepasste Events im Dashboard verwalten, erstellen oder auf die Blockliste setzen, indem Sie zu **Dateneinstellungen** > **Angepasste Events** navigieren.

### Fehlerbehebung bei doppelten angepassten Attributen oder Events {#troubleshooting-duplicate-custom-attributes-or-events}

{% multi_lang_include data_activation/troubleshooting_duplicate_custom_data_entries.md %}

Wählen Sie das Menü neben einem angepassten Event aus, um die folgenden Aktionen auszuführen:

### Auf die Blockliste setzen {#blocklisting}

Sie können einzelne angepasste Events über das Aktionsmenü auf die Blockliste setzen oder bis zu 100 Events gleichzeitig auswählen und in einem Schritt auf die Blockliste setzen.

Wenn Sie ein angepasstes Event blockieren:

{% multi_lang_include data_activation/custom_event_block_effects.md %}

Wenn ein blockiertes angepasstes Event derzeit von Filtern oder Trigger or triggern or triggern in anderen Bereichen von Braze referenziert wird, erscheint zusätzlich ein Warndialog, der erklärt, dass alle Instanzen der Filter oder Trigger or triggern, die darauf verweisen, entfernt und archiviert werden.

Weitere Details zum Blocklisting und Löschen angepasster Daten finden Sie unter [Angepasste Daten auf die Blockliste setzen]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data).

### Beschreibungen hinzufügen {#adding-descriptions}

Sie können einem angepassten Event nach der Erstellung eine Beschreibung hinzufügen, wenn Sie über die [Nutzerberechtigung]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) `Manage Events, Attributes, Purchases` verfügen. Wählen Sie **Beschreibung bearbeiten** für das angepasste Event aus und geben Sie einen beliebigen Text ein, zum Beispiel eine Notiz für Ihr Team.

### Tags hinzufügen {#adding-tags}

Sie können einem angepassten Event nach der Erstellung Tags hinzufügen, wenn Sie über die [Nutzerberechtigung]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) „Manage Events, Attributes, Purchases“ verfügen. Die Tags können dann verwendet werden, um die Liste der Events zu filtern.

### Daten exportieren {#exporting-data}

Um die Liste der angepassten Events als CSV-Datei zu exportieren, wählen Sie oben auf der Seite **Alle exportieren** aus. Die CSV-Datei wird generiert, und ein Download-Link wird Ihnen per E-Mail zugesendet.

{% alert note %}
Es gibt keine feste Dashboard-Obergrenze für die Anzahl unterschiedlicher **angepasster Events** oder **angepasster Attribute**, die Sie in einem Profil definieren oder speichern können. Die praktischen Grenzen hängen von der Datenstruktur, dem Ingestion-Volumen und der Workspace-Performance ab. Wenn Sie einen sehr großen Katalog von Events oder Attributen tracken möchten, arbeiten Sie mit Ihrem Braze-Account-Team an Modellierung und Datenpflege (zum Beispiel [Blocklisting]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data) ungenutzter Daten).
{% endalert %}

## Nutzungsberichte anzeigen {#viewing-usage-reports}

Der Nutzungsbericht listet alle Canvase, Campaigns und Segments auf, die ein bestimmtes angepasstes Event verwenden. Diese Liste enthält keine Verwendungen von Liquid.

Sie können bis zu 100 Nutzungsberichte gleichzeitig anzeigen, indem Sie die Kontrollkästchen neben den entsprechenden angepassten Events aktivieren und dann **Nutzungsbericht anzeigen** auswählen.

## Angepasste Events protokollieren {#logging-custom-events}

Angepasste Events erfordern eine zusätzliche Einrichtung. In der folgenden Plattform-Dokumentation finden Sie die Methoden zur Protokollierung angepasster Events und erfahren, wie Sie Ihren angepassten Events Eigenschaften und Mengen hinzufügen können.

{% details Dokumentation nach Plattform anzeigen %}

- [Android und FireOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift)
- [Internet]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/analytics#custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=unity)
- [.NET MAUI (ehemals Xamarin)]({{site.baseurl}}/developer_guide/analytics?sdktab=xamarin#custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=roku)

{% enddetails %}

## Speicherung angepasster Events {#custom-event-storage}

Alle im **Kundenprofil or Nutzerprofil** gespeicherten Daten, einschließlich Metadaten angepasster Events (erstes oder letztes Vorkommen, Gesamtanzahl und X in Y über 30 Tage), werden unbegrenzt aufbewahrt, solange jedes Profil <a href="/docs/user_archival#active-users">aktiv</a> ist.

## Event-Verlauf von Nutzer:innen anzeigen {#view-a-users-event-history}

Verwenden Sie den Tab **Event-Verlauf** im Profil von Nutzer:innen, um deren kürzliche angepasste Events und Käufe einzusehen. So können Sie bestätigen, dass Ihre Integration Events korrekt protokolliert, und Probleme auf Nutzerebene direkt im Dashboard beheben.

So zeigen Sie den Event-Verlauf von Nutzer:innen an:

1. Gehen Sie zu **Zielgruppe** > **Nutzer:innen suchen** und wählen Sie dann Nutzer:innen aus, um deren Profil zu öffnen.
2. Wählen Sie den Tab **Event-Verlauf** aus.

Der Tab listet die angepassten Events und Käufe der Nutzer:innen der letzten 30 Tage auf, bis zu den 100 neuesten Events, sortiert von neuesten zu ältesten.

Jedes Event enthält:

- **Event-Typ:** Ob es sich um ein angepasstes Event oder einen Kauf handelt.
- **Event-Name:** Der Event-Name, wie er protokolliert wurde.
- **Zeit:** Wann das Event aufgetreten ist.
- **Eigenschaften:** Die vollständigen Event-Eigenschaften für dieses Vorkommen, dargestellt als JSON.

Häufige Anwendungsfälle sind:

- Überprüfen, ob Ihre SDK or Software-Development-Kit- oder API-Integration während der Entwicklung oder nach einem Release Events wie erwartet sendet.
- Fehlerbehebung, warum Nutzer:innen eine event-getriggerte Campaign oder ein Canvas betreten haben oder nicht.
- Untersuchung eines Support-Problems für bestimmte Nutzer:innen, ohne einen Datenexport einrichten zu müssen.

{% alert note %}
Das Anzeigen des Tabs **Event-Verlauf** erfordert die Nutzerberechtigungen **Nutzer:innen suchen**, **PII anzeigen** und **Event-Eigenschaften von Nutzer:innen anzeigen**, da Event-Eigenschaften personenbezogene Daten enthalten können. Weitere Informationen finden Sie unter [Nutzerberechtigungen im Unternehmen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).
{% endalert %}

## Segmentierungsfilter {#segmentation-filters}

Die folgende Tabelle zeigt die Filter, die für die Segmentierung von Nutzer:innen nach angepassten Events verfügbar sind.

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen |
| ---------------------| --------------- | ------------- |
| Prüfen, ob das angepasste Event **mehr als X-mal** aufgetreten ist | **MEHR ALS** | **ANZAHL** |
| Prüfen, ob das angepasste Event **weniger als X-mal** aufgetreten ist | **WENIGER ALS** | **ANZAHL** |
| Prüfen, ob das angepasste Event **genau X-mal** aufgetreten ist | **GENAU** | **ANZAHL** |
| Prüfen, ob das angepasste Event zuletzt **nach dem Datum X** aufgetreten ist | **NACH** | **ZEIT** |
| Prüfen, ob das angepasste Event zuletzt **vor dem Datum X** aufgetreten ist | **VOR** | **ZEIT** |
| Prüfen, ob das angepasste Event zuletzt **vor mehr als X Tagen** aufgetreten ist | **MEHR ALS** | **ANZAHL DER TAGE HER** (positive Zahl) |
| Prüfen, ob das angepasste Event zuletzt **vor weniger als X Tagen** aufgetreten ist | **WENIGER ALS** | **ANZAHL DER TAGE HER** (positive Zahl) |
| Prüfen, ob das angepasste Event **mehr als X-mal (Max = 50)** aufgetreten ist | **MEHR ALS** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** |
| Prüfen, ob das angepasste Event **weniger als X-mal (Max = 50)** aufgetreten ist | **WENIGER ALS** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** |
| Prüfen, ob das angepasste Event **genau X-mal (Max = 50)** aufgetreten ist | **GENAU** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Segmentierungsfilter" }

## Analytics

Braze erfasst, wie oft angepasste Events aufgetreten sind und wann sie zuletzt von den einzelnen Nutzer:innen ausgeführt wurden, um sie für die Segmentierung zu verwenden. Informationen zur Einrichtung von Berichten, Filtern und Exportoptionen finden Sie unter [Bericht über angepasste Events]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report).

Auf der Seite **Custom Events Report** können Sie in aggregierter Form sehen, wie oft jedes angepasste Event auftritt. Die grauen Linien, die über die Zeitreihe gelegt werden, zeigen an, wann zuletzt eine Campaign gesendet wurde. Dies ist nützlich, um zu sehen, wie Ihre Campaigns die Aktivität angepasster Events beeinflusst haben.

![Diagramm der Anzahl angepasster Events auf der Seite „Custom Events“ im Dashboard mit Trends für ein angepasstes Event]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

Sie können auch **Filter** verwenden, um Ihre angepassten Events nach Stunde, monatlich aktiven Nutzer:innen (MAU or monatlich aktive:r Nutzer:in), Segments oder KPI or Leistungskennzahl or Leistungskennzahlen-Formeln aufzuschlüsseln.

![Filter für das Diagramm angepasster Events]({% image_buster /assets/img/custom_events_report_filters.png %}){: style="max-width:40%;"}

{% alert tip %}
[Inkrementieren Sie angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types), um einen Zähler für eine Nutzeraktion ähnlich einem angepassten Event zu führen. Allerdings können Sie Daten angepasster Attribute nicht in einer Zeitreihe anzeigen. Nutzeraktionen, die nicht in einer Zeitreihe analysiert werden müssen, sollten mit dieser Methode erfasst werden.
{% endalert %}

### Warum Analytics angepasster Events nicht angezeigt werden {#why-custom-events-analytics-arent-showing}

Segments, die mit Daten angepasster Events erstellt wurden, können keine früheren historischen Daten aus der Zeit vor ihrer Erstellung anzeigen.

## Angepasste Event-Eigenschaften {#custom-event-properties}

Angepasste Event-Eigenschaften sind Metadaten oder Attribute eines angepassten Events, die ein bestimmtes Vorkommen eines Events beschreiben. Diese Eigenschaften können verwendet werden, um Trigger or triggern-Bedingungen weiter zu qualifizieren, die Personalisierung im Messaging zu erhöhen, Conversions zu tracken und durch den Export von Rohdaten anspruchsvollere Analytics zu erstellen.

Weitere Informationen finden Sie unter [Angepasste Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties).