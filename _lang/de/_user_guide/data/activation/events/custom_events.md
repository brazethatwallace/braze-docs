---
nav_title: Angepasste Events
article_title: Angepasste Events
page_order: 1
page_type: reference
description: "Dieser Artikel beschreibt angepasste Events und Eigenschaften, Segmentierung, Nutzung, Canvas-Eingangs-Eigenschaften, wo Sie relevante Analytics einsehen können und mehr."
search_rank: 2
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Angepasste Events

> Dieser Artikel beschreibt angepasste Events und Eigenschaften, zugehörige Segmentierungsfilter, Canvas-Eingangs-Eigenschaften, relevante Analytics und mehr. Um mehr über Braze Events im Allgemeinen zu erfahren, lesen Sie [Events]({{site.baseurl}}/user_guide/data/activation/events/).

Angepasste Events sind Aktionen, die von Ihren Nutzer:innen durchgeführt werden, oder Updates über diese. Wenn angepasste Events protokolliert werden, können sie eine beliebige Anzahl und Art von Folgekampagnen triggern. Sie können dann [Segmentierungsfilter](#segmentation-filters) verwenden, um Nutzer:innen danach zu segmentieren, wie kürzlich und wie häufig diese angepassten Events aufgetreten sind. Damit eignen sich angepasste Events besonders gut für das Tracking von hochwertigen Nutzerinteraktionen innerhalb Ihrer Anwendung.

## Anwendungsfälle

Einige gängige Anwendungsfälle für angepasste Events sind:

- Triggern einer Kampagne oder eines Canvas basierend auf einem angepassten Event mithilfe der [aktionsbasierten Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/)
- Segmentierung von Nutzer:innen danach, wie oft sie ein angepasstes Event durchgeführt haben, wann das Event zuletzt aufgetreten ist und Ähnliches
- Nutzung der Dashboard-[Analytics für angepasste Events](#analytics), um eine aggregierte Ansicht darüber zu erhalten, wie oft jedes Event aufgetreten ist
- Zusätzliche Analytics mithilfe von [Funnel]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports#step-2-select-events-for-funnel-steps)- und [Bindungs]({{site.baseurl}}/user_guide/analytics/reports/retention_reports/)-Berichten gewinnen
- Nutzung von [persistenten Eingangs-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties/), um Metadaten aus Ihrem Kund:innen-Event für die Personalisierung in Ihren Canvas-Schritten zu verwenden
- Generierung anspruchsvollerer Analytics mit [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)
- Einrichten von [Ausstiegskriterien]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria/), um festzulegen, wann Nutzer:innen Ihren Canvas verlassen sollen

## Angepasste Events verwalten

Sie können angepasste Events im Dashboard verwalten, erstellen oder auf die Blocklist setzen, indem Sie zu **Dateneinstellungen** > **Angepasste Events** navigieren.

Wählen Sie das Menü neben einem angepassten Event für die folgenden Aktionen:

### Auf die Blocklist setzen

Sie können einzelne angepasste Events über das Aktionsmenü auf die Blocklist setzen oder bis zu 100 Events gleichzeitig auswählen und in einem Schritt auf die Blocklist setzen.

Wenn Sie ein angepasstes Event blockieren:

- Werden für dieses Event keine zukünftigen Daten mehr erfasst.
- Sind vorhandene Daten nicht verfügbar, es sei denn, das Event wird wieder von der Blocklist entfernt.
- Wird dieses Event nicht in Filtern oder Grafiken angezeigt.

Wenn ein blockiertes angepasstes Event derzeit von Filtern oder Triggern in anderen Bereichen von Braze referenziert wird, erscheint zusätzlich ein Warnhinweis-Modal, das erklärt, dass alle Instanzen der Filter oder Trigger, die darauf verweisen, entfernt und archiviert werden.

Weitere Details zum Blockieren und Löschen angepasster Daten finden Sie unter [Angepasste Daten auf die Blocklist setzen]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data/).

### Als personenbezogene Daten (PII) markieren

Administrator:innen können auf dieser Seite auch angepasste Events erstellen und als PII markieren. Diese Events sind nur für Administrator:innen und Dashboard-Nutzer:innen mit der Berechtigung „Angepasste Attribute anzeigen, die als PII markiert sind" sichtbar.

### Beschreibungen hinzufügen

Sie können einem angepassten Event nach der Erstellung eine Beschreibung hinzufügen, wenn Sie die [Nutzerberechtigung]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) `Manage Events, Attributes, Purchases` haben. Wählen Sie **Beschreibung bearbeiten** für das angepasste Event und geben Sie ein, was Sie möchten, z. B. eine Notiz für Ihr Team.

### Tags hinzufügen

Sie können einem angepassten Event nach der Erstellung Tags hinzufügen, wenn Sie die [Nutzerberechtigung]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) „Manage Events, Attributes, Purchases" haben. Die Tags können dann verwendet werden, um die Liste der Events zu filtern.

### Daten exportieren

Um die Liste der angepassten Events als CSV-Datei zu exportieren, wählen Sie oben auf der Seite **Alle exportieren**. Die CSV-Datei wird generiert und ein Download-Link wird Ihnen per E-Mail zugesendet.

## Nutzungsberichte anzeigen

Der Nutzungsbericht listet alle Canvases, Kampagnen und Segmente auf, die ein bestimmtes angepasstes Event verwenden. Diese Liste enthält keine Liquid-Verwendungen.

Sie können bis zu 100 Nutzungsberichte gleichzeitig anzeigen, indem Sie die Kontrollkästchen neben den jeweiligen angepassten Events aktivieren und dann **Nutzungsbericht anzeigen** auswählen.

## Angepasste Events protokollieren

Angepasste Events erfordern eine zusätzliche Einrichtung. In der folgenden Liste finden Sie die Dokumentation für jede Plattform mit Informationen zu den Methoden, die zum Protokollieren angepasster Events verwendet werden, und wie Sie Eigenschaften und Mengen zu Ihren angepassten Events hinzufügen können.

{% details Dokumentation nach Plattform aufklappen %}

- [Android und FireOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
- [Internet]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=unity)
- [.NET MAUI (ehemals Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=roku)

{% enddetails %}

## Speicherung angepasster Events

Alle im **Nutzerprofil** gespeicherten Daten, einschließlich Metadaten angepasster Events (erstes oder letztes Vorkommen, Gesamtanzahl und X in Y über 30 Tage), werden unbegrenzt aufbewahrt, solange jedes Profil [aktiv]({{site.baseurl}}/user_archival#active-users) ist.

## Segmentierungsfilter

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

Braze erfasst die Anzahl der Vorkommen angepasster Events und den Zeitpunkt, zu dem sie zuletzt von den einzelnen Nutzer:innen durchgeführt wurden, für die Segmentierung. Sie können diese Analytics einsehen, indem Sie zu **Analytics** > **Bericht zu angepassten Events** navigieren.

Auf der Seite **Bericht zu angepassten Events** im Dashboard können Sie in aggregierter Form sehen, wie oft jedes angepasste Event auftritt. Die grauen Linien, die über die Zeitreihe gelegt werden, zeigen an, wann zuletzt eine Kampagne gesendet wurde – das ist nützlich, um zu sehen, wie Ihre Kampagnen die Aktivität angepasster Events beeinflusst haben.

![Grafik der Anzahl angepasster Events auf der Seite „Angepasste Events" im Dashboard, die Trends für ein angepasstes Event zeigt]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

Sie können auch **Filter** verwenden, um Ihre angepassten Events nach Stunde, monatlich aktiven Nutzer:innen (MAU), Segmenten oder KPI-Formeln aufzuschlüsseln.

![Filter für die Grafik angepasster Events]({% image_buster /assets/img/custom_events_report_filters.png %}){: style="max-width:40%;"}

{% alert tip %}
[Inkrementieren Sie angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#integers), um einen Zähler für eine Nutzeraktion ähnlich einem angepassten Event zu führen. Allerdings können Sie Daten angepasster Attribute nicht in einer Zeitreihe anzeigen. Nutzeraktionen, die nicht in einer Zeitreihe analysiert werden müssen, sollten mit dieser Methode erfasst werden.
{% endalert %}

### Warum Analytics für angepasste Events nicht angezeigt werden

Segmente, die mit Daten angepasster Events erstellt wurden, können keine früheren historischen Daten aus der Zeit vor ihrer Erstellung anzeigen.

## Eigenschaften angepasster Events

Eigenschaften angepasster Events sind Metadaten oder Attribute angepasster Events, die ein bestimmtes Vorkommen eines Events beschreiben. Diese Eigenschaften können verwendet werden, um Trigger-Bedingungen weiter zu qualifizieren, die Personalisierung im Messaging zu erhöhen, Conversions zu tracken und anspruchsvollere Analytics durch den Rohdatenexport zu generieren.

Um mehr zu erfahren, lesen Sie [Eigenschaften angepasster Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties/).