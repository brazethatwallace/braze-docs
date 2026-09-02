---
nav_title: Angepasste Daten auf die Blocklist setzen
article_title: Angepasste Daten auf die Blocklist setzen
page_order: 3
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie angepasste Events und Attribute in Braze auf die Blocklist setzen und löschen können."
---

# Angepasste Daten auf die Blocklist setzen {#blocklist-custom-data}

> Verwenden Sie die Blocklist, um das Tracking angepasster Daten zu stoppen, die nicht mehr nützlich sind. Verwenden Sie die Löschfunktion, um angepasste Events und Attribute nach dem Blocklisting dauerhaft aus Nutzerprofilen zu entfernen. Informationen zum Vorausfüllen, Verwalten von Eigenschaften und Konfigurieren von Datentypen finden Sie unter [Angepasste Daten verwalten]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data).

## Angepasste Daten auf die Blocklist setzen {#blocklisting-custom-data}

Es kann vorkommen, dass Sie angepasste Attribute, angepasste Events oder Kauf-Events identifizieren, die entweder zu viele Datenpunkte protokollieren, für Ihre Marketingstrategie nicht mehr nützlich sind oder versehentlich aufgezeichnet wurden.

Um zu verhindern, dass diese Daten an Braze gesendet werden, können Sie ein angepasstes Datenobjekt auf die Blocklist setzen, während Ihr Entwicklerteam daran arbeitet, es aus dem Backend Ihrer App oder Website zu entfernen. Durch das Blocklisting wird verhindert, dass ein bestimmtes angepasstes Datenobjekt künftig von Braze aufgezeichnet wird – es wird also nicht mehr angezeigt, wenn Sie nach einem bestimmten Nutzer bzw. einer bestimmten Nutzerin suchen.

### Blocklisting oder Löschen wählen {#choosing-blocklisting-or-deletion}

- **Blocklisting** behält bestehende angepasste Attribute, Events oder Käufe in den Nutzerprofilen bei, aber Braze verarbeitet keine neuen Daten mehr für diese Objekte.
- **Löschen** entfernt diese Daten aus den Nutzerprofilen. Gelöschte angepasste Attribute und Events werden für sieben Tage in den Status **Trashed** verschoben, in dem Sie sie wiederherstellen können. Nach sieben Tagen löscht Braze sie endgültig. Das Löschen stoppt nicht den Eingang neuer Daten – stellen Sie daher sicher, dass Ihr SDK, Ihre API oder Ihre CSV-Importe diese Daten nicht mehr senden, bevor Sie löschen.

Blocklisting überträgt die Blocklist-Informationen an das Gerät jeder Nutzerin und jedes Nutzers und kann datenintensiv sein. Das Blocklisting einer sehr großen Anzahl von Attributen, Events oder Käufen (z. B. mehr als 100) kann die App-Performance beeinträchtigen. Wenn Sie nicht vorhaben, diese Daten weiterhin an Braze zu senden, ist das Löschen oft der bessere Ansatz, nachdem Sie die Integration gestoppt haben.

Unabhängig davon, ob Sie Daten auf die Blocklist setzen oder löschen, werden diese angepassten Attribute, Events und Käufe nicht mehr auf der Seite **Manage Workspace** angezeigt und als Segmentfilter entfernt. Wenn Sie angepasste Daten löschen, entfernt Braze diese Daten auf Nutzerebene aus den Profilen gemäß [Wie das Löschen funktioniert](#how-deletion-works).

Um angepasste Daten auf die Blocklist zu setzen, benötigen Sie die [Nutzerberechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) im folgenden Dropdown für Ihren Workspace.

{% details Nutzerberechtigungen für das Blocklisting angepasster Daten %}

- Campaigns anzeigen
- Campaigns bearbeiten
- Campaigns archivieren
- Canvases anzeigen
- Canvases bearbeiten
- Canvases archivieren
- Frequency-Capping-Regeln anzeigen
- Frequency-Capping-Regeln bearbeiten
- Nachrichtenpriorisierung anzeigen
- Nachrichtenpriorisierung bearbeiten
- Content Blocks anzeigen
- Feature-Flags anzeigen
- Feature-Flags bearbeiten
- Feature-Flags archivieren
- Segmente anzeigen
- Segmente bearbeiten
- IAM-Templates anzeigen
- IAM-Templates bearbeiten
- IAM-Templates archivieren
- E-Mail-Templates anzeigen
- E-Mail-Templates bearbeiten
- E-Mail-Templates archivieren
- Webhook-Templates anzeigen
- Webhook-Templates bearbeiten
- Link-Templates anzeigen
- Link-Templates bearbeiten
- Medienbibliothek-Assets anzeigen
- Medienbibliothek-Assets bearbeiten
- Medienbibliothek-Assets löschen
- Standorte anzeigen
- Standorte bearbeiten
- Standorte archivieren
- Aktionscodes anzeigen
- Aktionscodes bearbeiten
- Aktionscodes exportieren
- Präferenzcenter anzeigen
- Präferenzcenter bearbeiten
- Berichte anzeigen
- Berichte bearbeiten

{% enddetails %}

Daten auf der Blocklist werden nicht vom SDK gesendet, und das Braze-Dashboard verarbeitet keine Daten auf der Blocklist aus anderen Quellen (z. B. der API). Das Blocklisting entfernt jedoch keine Daten aus Nutzerprofilen und reduziert rückwirkend nicht die Anzahl der Datenpunkte, die für dieses angepasste Datenobjekt angefallen sind. Daten auf der Blocklist sind ausgeblendet und können weiterhin für Liquid-Templating verwendet werden.

### Angepasste Attribute, angepasste Events und Produkte auf die Blocklist setzen {#blocklisting-custom-attributes-custom-events-and-products}

{% alert important %}
Wenn ein Event oder Attribut auf die Blocklist gesetzt wird, werden alle Segmente, Campaigns oder Canvases, die dieses Event oder Attribut verwenden, archiviert.
{% endalert %}

Um das Tracking eines bestimmten angepassten Attributs, Events oder Produkts zu stoppen, führen Sie die folgenden Schritte aus:

1. Suchen Sie danach auf den Seiten **Custom Attributes**, **Custom Events** oder **Products**.
2. Wählen Sie das angepasste Attribut, Event oder Produkt aus. Bei angepassten Attributen und Events können Sie bis zu 100 gleichzeitig für das Blocklisting auswählen.
3. Wählen Sie **Blocklist**.

![Mehrere ausgewählte angepasste Attribute, die auf der Seite „Custom Attributes“ auf die Blocklist gesetzt werden.]({% image_buster /assets/img_archive/blocklist_custom_attr.png %})

Sie können bis zu 300 angepasste Attribute und 300 angepasste Events auf die Blocklist setzen. Um das Erfassen bestimmter Geräteattribute zu verhindern, lesen Sie unseren [SDK-Leitfaden]({{site.baseurl}}/developer_guide/getting_started/sdk_overview#blocking-data-collection).

{% alert important %}
Angepasste Attribute oder angepasste Events mit dem Status **Trashed** zählen zum Blocklisting-Limit, bis sie endgültig gelöscht werden.
{% endalert %}

Wenn ein angepasstes Event oder Attribut auf die Blocklist gesetzt wird, gilt Folgendes:

- An Braze gesendete Daten werden nicht verarbeitet, und Events und Attribute auf der Blocklist zählen nicht mehr als Datenpunkte
- Vorhandene Daten sind nicht verfügbar, es sei denn, sie werden reaktiviert
- Events und Attribute auf der Blocklist werden nicht in Filtern oder Diagrammen angezeigt
- Verweise auf Daten der Blocklist in Entwürfen aktiver Canvases werden als ungültige Werte geladen, was zu Fehlern führen kann
- Alles, was das auf der Blocklist stehende Event oder Attribut verwendet, wird archiviert

Um dies zu bewerkstelligen, sendet Braze die Blocklist-Informationen an jedes Gerät. Dies ist wichtig, wenn Sie eine sehr große Anzahl von Events und Attributen auf die Blocklist setzen möchten (Hunderttausende oder Millionen), da es sich um eine datenintensive Operation handelt.

### Überlegungen zum Blocklisting {#considerations-for-blocklisting}

Das Blocklisting einer großen Anzahl von Events und Attributen ist möglich, aber nicht ratsam. Der Grund dafür ist, dass jedes Mal, wenn ein Event ausgeführt oder ein Attribut (potenziell) an Braze gesendet wird, dieses Event oder Attribut gegen die gesamte Blocklist geprüft werden muss.

Bis zu 300 Einträge werden zur Blocklist-Prüfung an das SDK gesendet. Wenn Sie mehr als 300 Einträge auf die Blocklist setzen, werden diese Daten vom SDK gesendet. Wenn Sie das Event oder Attribut künftig nicht mehr benötigen, sollten Sie es bei Ihrem nächsten Release aus Ihrem App-Code entfernen. Änderungen an der Blocklist können einige Minuten benötigen, um propagiert zu werden. Sie können jedes auf der Blocklist stehende Event oder Attribut jederzeit wieder aktivieren.

## Angepasste Daten löschen {#deleting-custom-data}

Beim Erstellen von gezielten Campaigns und Segments stellen Sie möglicherweise fest, dass Sie ein angepasstes Event oder ein angepasstes Attribut nicht mehr benötigen. Wenn Sie beispielsweise ein bestimmtes angepasstes Attribut als Teil einer einmaligen Campaign verwendet haben, können Sie diese Daten nach dem [Sperren](#blocklisting-custom-attributes-custom-events-and-products) löschen und die Verweise darauf aus Ihrer App entfernen. Sie können beliebige Datentypen löschen (z. B. Strings, Zahlen und verschachtelte angepasste Attribute).

{% alert important %}
Sie müssen [Braze-Admin]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#admin) sein, um angepasste Daten zu löschen.
{% endalert %}

Um ein angepasstes Event oder ein angepasstes Attribut zu löschen, gehen Sie wie folgt vor:

1. Gehen Sie zu **Dateneinstellungen** > **Angepasste Attribute** oder **Angepasste Events**, je nachdem, welchen Datentyp Sie löschen möchten.
2. Navigieren Sie zu den angepassten Daten und wählen Sie <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;**Aktionen** > **Sperren** aus.
3. Nachdem Ihre angepassten Daten 7 Tage lang gesperrt waren, wählen Sie <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;**Aktionen** > **Löschen** aus.

### So funktioniert das Löschen {#how-deletion-works}

Wenn Sie angepasste Daten löschen, geschieht Folgendes:

- **Für angepasste Attribute:** Die Attributdaten werden dauerhaft aus dem Profil jedes Nutzers/jeder Nutzerin entfernt.
- **Für angepasste Events:** Die Event-Metadaten werden dauerhaft aus dem Profil jedes Nutzers/jeder Nutzerin entfernt.

Wenn ein Attribut oder Event zum Löschen ausgewählt wird, ändert sich sein Status zu **Papierkorb**. In den nächsten sieben Tagen kann das Attribut oder Event wiederhergestellt werden. Wenn Sie es nach sieben Tagen nicht wiederherstellen, werden die Daten dauerhaft gelöscht. Wenn Sie das Attribut oder Event wiederherstellen, wird es wieder in den gesperrten Zustand versetzt.

Das Löschen verhindert nicht die weitere Aufzeichnung der angepassten Datenobjekte in Nutzerprofilen. Stellen Sie daher sicher, dass die angepassten Daten nicht mehr aufgezeichnet werden, bevor Sie das Event oder Attribut löschen.

### Wichtige Hinweise {#things-to-know}

Beachten Sie beim Löschen angepasster Daten die folgenden Details:

* **Das Löschen ist dauerhaft.** Daten können nicht wiederhergestellt werden.
* Daten werden von der Braze-Plattform und aus Nutzerprofilen entfernt.
* Sie können den Namen des angepassten Attributs oder des angepassten Events nach dem Löschen „wiederverwenden“. Das bedeutet: Wenn Sie bemerken, dass angepasste Daten nach dem Löschen in Braze „wieder auftauchen“, kann dies durch eine Integration verursacht werden, die nicht gestoppt wurde und Daten mit demselben angepassten Datennamen sendet.
* Möglicherweise müssen Sie einen Artikel erneut sperren, wenn Ihr Löschvorgang dazu führt, dass angepasste Daten wieder auftauchen. Der Sperrstatus bleibt nicht erhalten, da die angepassten Daten gelöscht wurden.
* Das Löschen angepasster Daten protokolliert keine [Datenpunkte]({{site.baseurl}}/user_guide/data/infrastructure/data_points) und erzeugt auch keine neuen zu verbrauchenden Datenpunkte.