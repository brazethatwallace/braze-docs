---
nav_title: Angepasste Events
article_title: Angepasste Events
page_order: 1
page_type: reference
description: "Dieser Artikel beschreibt angepasste Events und Eigenschaften, Segmentierung, Nutzung, Canvas-Eingangs-Eigenschaften, wo Sie relevante Analytics einsehen können und vieles mehr."
search_rank: 2
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Angepasste Events {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-events}

> Dieser Artikel beschreibt angepasste Events und Eigenschaften, den Event-Verlauf im Nutzerprofil, verwandte Segmentierungsfilter, Canvas-Eingangs-Eigenschaften, relevante Analytics und mehr. Mehr über Braze-Events im Allgemeinen erfahren Sie unter [Events]({{site.baseurl}}/user_guide/data/activation/events/).

Angepasste Events sind Aktionen oder Updates, die von Ihren Nutzer:innen durchgeführt werden. Wenn angepasste Events protokolliert werden, können sie beliebig viele und verschiedene Folgekampagnen auslösen. Mit Hilfe von [Segmentierungsfiltern](#segmentation-filters) können Sie Nutzer:innen dann danach segmentieren, wie kürzlich und wie häufig diese angepassten Events aufgetreten sind. Dadurch eignen sich angepasste Events am besten für das Tracking hochwertiger Nutzer:innen-Interaktionen innerhalb Ihrer Anwendung.

## Anwendungsfälle {#use-cases}

Einige häufige Anwendungsfälle für angepasste Events sind:

- Auslösen einer Campaign oder eines Canvas auf der Grundlage eines angepassten Events mit [aktionsbasierter Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/)
- Segmentierung der Nutzer:innen danach, wie oft sie ein angepasstes Event durchgeführt haben, wann das Event zuletzt aufgetreten ist und Ähnliches
- Nutzung der Dashboard-[Analytics für angepasste Events](#analytics), um eine aggregierte Ansicht darüber zu erhalten, wie oft jedes Event aufgetreten ist
- Zusätzliche Analytics mithilfe von [Funnel]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports/#step-2-select-events-for-funnel-steps)- und [Bindungs]({{site.baseurl}}/user_guide/analytics/reports/retention_reports/)-Berichten gewinnen
- Nutzung von [persistenten Eingangs-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties/), um Metadaten aus Ihrem Kund:innen-Event für die Personalisierung in Ihren Canvas-Schritten zu verwenden
- Generierung anspruchsvollerer Analytics mit [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)
- Einrichten von [Ausstiegskriterien]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria/), um festzulegen, wann Nutzer:innen Ihren Canvas verlassen sollen

## Angepasste Events verwalten {#managing-custom-events}

Sie können angepasste Events im Dashboard verwalten, erstellen oder auf die Blocklist setzen, indem Sie zu **Dateneinstellungen** > **Angepasste Events** navigieren.

Wählen Sie das Menü neben einem angepassten Event für die folgenden Aktionen:

### Auf die Blocklist setzen {#blocklisting}

Sie können einzelne angepasste Events über das Aktionsmenü auf die Blocklist setzen oder bis zu 100 Events gleichzeitig auswählen und in einem Schritt auf die Blocklist setzen.

Wenn Sie ein angepasstes Event blockieren:

- Werden für dieses Event keine zukünftigen Daten mehr erfasst.
- Sind vorhandene Daten nicht verfügbar, es sei denn, das Event wird wieder von der Blocklist entfernt.
- Wird dieses Event nicht in Filtern oder Grafiken angezeigt.

Wenn ein blockiertes angepasstes Event derzeit von Filtern oder Triggern in anderen Bereichen von Braze referenziert wird, erscheint zusätzlich ein Warnhinweis-Modal, das erklärt, dass alle Instanzen der Filter oder Trigger, die darauf verweisen, entfernt und archiviert werden.

Weitere Details zum Blockieren und Löschen angepasster Daten finden Sie unter [Angepasste Daten auf die Blocklist setzen]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data/).

### Beschreibungen hinzufügen {#adding-descriptions}

Sie können einem angepassten Event nach der Erstellung eine Beschreibung hinzufügen, wenn Sie die [Nutzerberechtigung]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) `Manage Events, Attributes, Purchases` haben. Wählen Sie **Beschreibung bearbeiten** für das angepasste Event und geben Sie ein, was Sie möchten, z. B. eine Notiz für Ihr Team.

### Tags hinzufügen {#adding-tags}

Sie können einem angepassten Event nach der Erstellung Tags hinzufügen, wenn Sie die [Nutzerberechtigung]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) „Manage Events, Attributes, Purchases“ haben. Die Tags können dann verwendet werden, um die Liste der Events zu filtern.

### Daten exportieren {#exporting-data}

Um die Liste der angepassten Events als CSV-Datei zu exportieren, wählen Sie oben auf der Seite **Alle exportieren**. Die CSV-Datei wird generiert und ein Download-Link wird Ihnen per E-Mail zugesendet.

{% alert note %}
Es gibt keine feste Dashboard-Obergrenze für die Anzahl unterschiedlicher **angepasster Events** oder **angepasster Attribute**, die Sie in einem Profil definieren oder speichern können. Die praktischen Grenzen hängen von der Datenstruktur, dem Aufnahmevolumen und der Workspace-Performance ab. Wenn Sie einen sehr großen Katalog von Events oder Attributen tracken möchten, arbeiten Sie mit Ihrem Braze-Account-Team an der Modellierung und Datenhygiene (z. B. [Blocklisting]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data/) ungenutzter Daten).
{% endalert %}

## Nutzungsberichte anzeigen {#viewing-usage-reports}

Der Nutzungsbericht listet alle Canvases, Campaigns und Segmente auf, die ein bestimmtes angepasstes Event verwenden. Diese Liste enthält keine Liquid-Verwendungen.

Sie können bis zu 100 Nutzungsberichte gleichzeitig anzeigen, indem Sie die Kontrollkästchen neben den jeweiligen angepassten Events aktivieren und dann **Nutzungsbericht anzeigen** auswählen.

## Angepasste Events protokollieren {#logging-custom-events}

Angepasste Events erfordern eine zusätzliche Einrichtung. In der folgenden Liste finden Sie die Dokumentation für jede Plattform mit Informationen zu den Methoden, die zum Protokollieren angepasster Events verwendet werden, und wie Sie Eigenschaften und Mengen zu Ihren angepassten Events hinzufügen können.

{% details Dokumentation nach Plattform aufklappen %}

- [Android und FireOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=unity)
- [.NET MAUI (ehemals Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=roku)

{% enddetails %}

## Speicherung angepasster Events {#custom-event-storage}

Alle im **Nutzerprofil** gespeicherten Daten, einschließlich Metadaten angepasster Events (erstes oder letztes Vorkommen, Gesamtanzahl und X in Y über 30 Tage), werden unbegrenzt aufbewahrt, solange jedes Profil [aktiv]({{site.baseurl}}/user_archival/#active-users) ist.

## Event-Verlauf einer Nutzer:in anzeigen {#view-a-users-event-history}

{% alert important %}
Der Event-Verlauf befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Braze Account Manager, wenn Sie an einer Teilnahme interessiert sind.
{% endalert %}

Verwenden Sie den Tab **Event-Verlauf** im Profil einer Nutzer:in, um die letzten angepassten Events und Käufe dieser Nutzer:in einzusehen. So können Sie bestätigen, dass Ihre Integration Events korrekt protokolliert, und Probleme auf Nutzer:innen-Ebene direkt im Dashboard beheben.

So zeigen Sie den Event-Verlauf einer Nutzer:in an:

1. Gehen Sie zu **Zielgruppe** > **Nutzer:innen suchen** und wählen Sie eine Nutzer:in aus, um deren Profil zu öffnen.
2. Wählen Sie den Tab **Event-Verlauf**.

Der Tab listet die angepassten Events und Käufe der Nutzer:in aus den letzten 30 Tagen auf, bis zu den 100 neuesten Events, sortiert von neuesten zu ältesten.

Jedes Event enthält:

- **Event-Typ:** Ob es sich um ein angepasstes Event oder einen Kauf handelt.
- **Event-Name:** Der Event-Name, wie er protokolliert wurde.
- **Zeitpunkt:** Wann das Event aufgetreten ist.
- **Eigenschaften:** Die vollständigen Event-Eigenschaften für dieses Vorkommen, dargestellt als JSON.

Häufige Anwendungsfälle sind:

- Überprüfung, ob Ihre SDK- oder API-Integration Events wie erwartet sendet – während der Entwicklung oder nach einem Release.
- Fehlerbehebung, warum eine Nutzer:in eine Event-getriggerte Campaign oder einen Canvas betreten hat oder nicht.
- Untersuchung eines Support-Falls für eine bestimmte Nutzer:in, ohne einen Datenexport einrichten zu müssen.

{% alert note %}
Zum Anzeigen des Tabs **Event-Verlauf** sind sowohl die Nutzerberechtigungen **Nutzer:innen suchen** als auch **PII anzeigen** erforderlich, da Event-Eigenschaften personenbezogene Daten enthalten können. Weitere Informationen finden Sie unter [Nutzerberechtigungen im Unternehmen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/).
{% endalert %}

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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Segmentierungsfilter" }

## Analytics {#analytics}

Braze erfasst die Anzahl der Vorkommen angepasster Events und den Zeitpunkt, zu dem sie zuletzt von den einzelnen Nutzer:innen durchgeführt wurden, für die Segmentierung. Sie können diese Analytics einsehen, indem Sie zu **Analytics** > **Bericht zu angepassten Events** navigieren.

Auf der Seite **Bericht zu angepassten Events** im Dashboard können Sie in aggregierter Form sehen, wie oft jedes angepasste Event auftritt. Die grauen Linien, die über die Zeitreihe gelegt werden, zeigen an, wann zuletzt eine Campaign gesendet wurde – das ist nützlich, um zu sehen, wie Ihre Campaigns die Aktivität angepasster Events beeinflusst haben.

![Grafik der Anzahl angepasster Events auf der Seite „Angepasste Events“ im Dashboard, die Trends für ein angepasstes Event zeigt]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

Sie können auch **Filter** verwenden, um Ihre angepassten Events nach Stunde, monatlich aktiven Nutzer:innen (MAU), Segmenten oder KPI-Formeln aufzuschlüsseln.

![Filter für die Grafik angepasster Events]({% image_buster /assets/img/custom_events_report_filters.png %}){: style="max-width:40%;"}

{% alert tip %}
[Inkrementieren Sie angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#integers), um einen Zähler für eine Nutzeraktion ähnlich einem angepassten Event zu führen. Allerdings können Sie Daten angepasster Attribute nicht in einer Zeitreihe anzeigen. Nutzeraktionen, die nicht in einer Zeitreihe analysiert werden müssen, sollten mit dieser Methode erfasst werden.
{% endalert %}

### Warum Analytics für angepasste Events nicht angezeigt werden {#why-custom-events-analytics-arent-showing}

Segmente, die mit Daten angepasster Events erstellt wurden, können keine früheren historischen Daten aus der Zeit vor ihrer Erstellung anzeigen.

## Angepasste Event-Eigenschaften {#custom-event-properties}

Angepasste Event-Eigenschaften sind Metadaten oder Attribute eines angepassten Events, die ein bestimmtes Vorkommen eines Events beschreiben. Diese Eigenschaften können verwendet werden, um Trigger-Bedingungen weiter zu qualifizieren, die Personalisierung im Messaging zu erhöhen, Conversions zu tracken und anspruchsvollere Analytics durch den Rohdatenexport zu generieren.

Um mehr zu erfahren, lesen Sie [Angepasste Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties/).