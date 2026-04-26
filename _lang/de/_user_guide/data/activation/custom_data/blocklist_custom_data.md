---
nav_title: Angepasste Daten auf die Blocklist setzen
article_title: Angepasste Daten auf die Blocklist setzen
page_order: 3
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie angepasste Events und Attribute in Braze auf die Blocklist setzen und löschen können."
---

# Angepasste Daten auf die Blocklist setzen {#blocklist-custom-data}

> Verwenden Sie die Blocklist, um das Tracking angepasster Daten zu stoppen, die nicht mehr nützlich sind. Verwenden Sie die Löschfunktion, um angepasste Events und Attribute nach dem Blocklisting dauerhaft aus Nutzerprofilen zu entfernen. Informationen zum Vorausfüllen, Verwalten von Eigenschaften und Konfigurieren von Datentypen finden Sie unter [Angepasste Daten verwalten]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/).

## Angepasste Daten auf die Blocklist setzen {#blocklisting-custom-data}

Gelegentlich identifizieren Sie möglicherweise angepasste Attribute, angepasste Events oder Kauf-Events, die entweder zu viele Datenpunkte protokollieren, für Ihre Marketing-Strategie nicht mehr nützlich sind oder versehentlich erfasst wurden.

Um zu verhindern, dass diese Daten an Braze gesendet werden, können Sie ein angepasstes Datenobjekt auf die Blocklist setzen, während Ihr Entwicklerteam daran arbeitet, es aus dem Backend Ihrer App oder Website zu entfernen. Blocklisting verhindert, dass ein bestimmtes angepasstes Datenobjekt von Braze künftig erfasst wird, d. h. es wird bei der Suche nach einem bestimmten Nutzer bzw. einer bestimmten Nutzerin nicht mehr angezeigt.

Um angepasste Daten auf die Blocklist zu setzen, benötigen Sie die [Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) aus dem folgenden Dropdown für Ihren Workspace.

{% details Berechtigungen für das Blocklisting angepasster Daten %}

{% multi_lang_include deprecations/user_permissions.md %}

- View Campaigns
- Edit Campaigns
- Archive Campaigns
- View Canvases
- Edit Canvases
- Archive Canvases
- View Frequency Capping Rules
- Edit Frequency Capping Rules
- View Message Prioritization
- Edit Message Prioritization
- View Content Blocks
- View Feature Flags
- Edit Feature Flags
- Archive Feature Flags
- View Segments
- Edit Segments
- View IAM Templates
- Edit IAM Templates
- Archive IAM Templates
- View Email Templates
- Edit Email Templates
- Archive Email Templates
- View Webhook Templates
- Edit Webhook Templates
- View Link Templates
- Edit Link Templates
- View Media Library Assets
- Edit Media Library Assets
- Delete Media Library Assets
- View Locations
- Edit Locations
- Archive Locations
- View Promotion Codes
- Edit Promotion Codes
- Export Promotion Codes
- View Preference Centers
- Edit Preference Centers
- View Reports
- Edit Reports

{% enddetails %}

Daten auf der Blocklist werden nicht vom SDK gesendet, und das Braze-Dashboard verarbeitet keine Blocklist-Daten aus anderen Quellen (z. B. der API). Blocklisting entfernt jedoch keine Daten aus Nutzerprofilen und reduziert auch nicht rückwirkend die Anzahl der Datenpunkte, die für dieses angepasste Datenobjekt angefallen sind. Daten auf der Blocklist sind ausgeblendet, können aber weiterhin für Liquid-Templating verwendet werden.

### Angepasste Attribute, angepasste Events und Produkte auf die Blocklist setzen {#blocklisting-custom-attributes-custom-events-and-products}

{% alert important %}
Wenn ein Event oder Attribut auf die Blocklist gesetzt wird, werden alle Segments, Campaigns oder Canvases, die dieses Event oder Attribut verwenden, archiviert.
{% endalert %}

Um das Tracking eines bestimmten angepassten Attributs, Events oder Produkts zu stoppen, gehen Sie wie folgt vor:

1. Suchen Sie es auf den Seiten **Angepasste Attribute**, **Angepasste Events** oder **Produkte**.
2. Wählen Sie das angepasste Attribut, Event oder Produkt aus. Bei angepassten Attributen und Events können Sie bis zu 100 gleichzeitig für die Blocklist auswählen.
3. Wählen Sie **Blocklist**.

![Mehrere ausgewählte angepasste Attribute, die auf der Seite „Angepasste Attribute“ auf die Blocklist gesetzt werden.]({% image_buster /assets/img_archive/blocklist_custom_attr.png %})

Sie können bis zu 300 angepasste Attribute und 300 angepasste Events auf die Blocklist setzen. Um das Erfassen bestimmter Geräteattribute zu verhindern, lesen Sie unseren [SDK-Leitfaden]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection).

{% alert important %}
Angepasste Attribute oder angepasste Events mit dem Status **Trashed** zählen zum Blocklist-Limit, bis sie gelöscht werden.
{% endalert %}

Wenn ein angepasstes Event oder Attribut auf die Blocklist gesetzt wird, gilt Folgendes:

- An Braze gesendete Daten werden nicht verarbeitet, und Events und Attribute auf der Blocklist zählen nicht mehr als Datenpunkte
- Vorhandene Daten sind nicht verfügbar, es sei denn, sie werden reaktiviert
- Events und Attribute auf der Blocklist werden nicht in Filtern oder Diagrammen angezeigt
- Verweise auf Blocklist-Daten in Entwürfen aktiver Canvases werden als ungültige Werte geladen, was zu Fehlern führen kann
- Alles, was das Event oder Attribut auf der Blocklist verwendet, wird archiviert

Um dies zu erreichen, sendet Braze die Blocklist-Informationen an jedes Gerät. Dies ist wichtig, wenn Sie eine große Anzahl von Events und Attributen (Hunderttausende oder Millionen) auf die Blocklist setzen möchten, da dies eine datenintensive Operation wäre.

### Überlegungen zum Blocklisting {#considerations-for-blocklisting}

Das Blocklisting einer großen Anzahl von Events und Attributen ist möglich, aber nicht empfehlenswert. Denn jedes Mal, wenn ein Event ausgeführt oder ein Attribut (potenziell) an Braze gesendet wird, muss dieses Event oder Attribut gegen die gesamte Blocklist geprüft werden.

Bis zu 300 Einträge werden an das SDK für das Blocklisting gesendet. Wenn Sie mehr als 300 Einträge auf die Blocklist setzen, werden diese Daten vom SDK gesendet. Wenn Sie das Event oder Attribut in Zukunft nicht mehr benötigen, sollten Sie es bei Ihrem nächsten Release aus Ihrem App-Code entfernen. Änderungen an der Blocklist können einige Minuten benötigen, um wirksam zu werden. Sie können jedes Event oder Attribut auf der Blocklist jederzeit wieder aktivieren.

## Angepasste Daten löschen {#deleting-custom-data}

Beim Erstellen gezielter Campaigns und Segments stellen Sie möglicherweise fest, dass Sie ein angepasstes Event oder angepasstes Attribut nicht mehr benötigen. Wenn Sie beispielsweise ein bestimmtes angepasstes Attribut als Teil einer einmaligen Campaign verwendet haben, können Sie diese Daten nach dem [Blocklisting](#blocklisting-custom-attributes-custom-events-and-products) löschen und die Verweise darauf aus Ihrer App entfernen. Sie können alle Datentypen löschen (z. B. Strings, Zahlen und verschachtelte angepasste Attribute).

{% alert important %}
Sie müssen [Braze-Admin]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#admin) sein, um angepasste Daten zu löschen.
{% endalert %}

Um ein angepasstes Event oder angepasstes Attribut zu löschen, gehen Sie wie folgt vor:

1. Gehen Sie zu **Dateneinstellungen** > **Angepasste Attribute** oder **Angepasste Events**, je nachdem, welchen Datentyp Sie löschen möchten.
2. Gehen Sie zu den angepassten Daten und wählen Sie <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;**Aktionen** > **Blocklist**.
3. Nachdem Ihre angepassten Daten 7 Tage lang auf der Blocklist waren, wählen Sie <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;**Aktionen** > **Löschen**.

### Wie die Löschung funktioniert {#how-deletion-works}

Wenn Sie angepasste Daten löschen, geschieht Folgendes:

- **Für angepasste Attribute:** Die Attributdaten werden dauerhaft aus dem Profil jeder Nutzerin und jedes Nutzers entfernt.
- **Für angepasste Events:** Die Event-Metadaten werden dauerhaft aus dem Profil jeder Nutzerin und jedes Nutzers entfernt.

Wenn ein Attribut oder Event zur Löschung ausgewählt wird, ändert sich sein Status auf **Trashed**. In den nächsten sieben Tagen ist es möglich, das Attribut oder Event wiederherzustellen. Wenn Sie es nach sieben Tagen nicht wiederherstellen, werden die Daten dauerhaft gelöscht. Wenn Sie das Attribut oder Event wiederherstellen, wird es wieder in den Blocklist-Status versetzt.

Die Löschung verhindert nicht die zusätzliche Erfassung der angepassten Datenobjekte in Nutzerprofilen. Stellen Sie daher sicher, dass die angepassten Daten nicht mehr erfasst werden, bevor Sie das Event oder Attribut löschen.

### Wichtige Hinweise {#things-to-know}

Beachten Sie beim Löschen angepasster Daten die folgenden Details:

* **Die Löschung ist dauerhaft.** Daten können nicht wiederhergestellt werden.
* Daten werden von der Braze-Plattform und aus Nutzerprofilen entfernt.
* Sie können den Namen des angepassten Attributs oder angepassten Events nach der Löschung „wiederverwenden“. Wenn Sie also bemerken, dass angepasste Daten nach der Löschung in Braze „wieder auftauchen“, kann dies durch eine Integration verursacht werden, die nicht gestoppt wurde und Daten mit demselben angepassten Datennamen sendet.
* Möglicherweise müssen Sie einen Eintrag erneut auf die Blocklist setzen, wenn Ihre Löschung dazu führt, dass angepasste Daten wieder auftauchen. Der Blocklist-Status wird nicht beibehalten, da die angepassten Daten gelöscht wurden.
* Das Löschen angepasster Daten protokolliert keine [Datenpunkte]({{site.baseurl}}/user_guide/data/infrastructure/data_points/) und erzeugt auch keine neuen Datenpunkte.