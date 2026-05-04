---
nav_title: FAQ
article_title: Snowflake FAQ zur Datenfreigabe
page_order: 50
page_type: FAQ
description: "Dieser Artikel beantwortet häufig gestellte Fragen zur Datenfreigabe in Snowflake."

---

# Häufig gestellte Fragen {#frequently-asked-questions}

### Ist es möglich, PII-Daten über die Snowflake-Datenfreigabe zu verschleiern? {#is-it-possible-to-obfuscate-pii-data-via-snowflake-data-sharing}
Nein, das wird derzeit nicht unterstützt.

### Benötige ich eine Datenfreigabe für dieselbe Region oder regionsübergreifend? {#do-i-need-data-share-for-the-same-region-or-cross-region}
Verwenden Sie die Datenfreigabe für dieselbe Region in den folgenden Szenarien:
- Ihr Snowflake-Konto befindet sich in US-EAST-1 (AWS) und Ihre Braze-Dashboard-Region ist in den USA.
- Ihre Snowflake-Region liegt in EU-CENTRAL-1 (AWS) und Ihre Braze-Dashboard-Region liegt in der EU.
- Ihre Snowflake-Region befindet sich in AP-Northeast-1 (AWS) und Ihre Braze-Dashboard-Region ist in Japan.
- Ihre Snowflake-Region befindet sich in AP-Southeast-2 (AWS) und Ihre Braze-Dashboard-Region ist in Australien.
- Ihre Snowflake-Region befindet sich in AP-Southeast-3 (AWS) und Ihre Braze-Dashboard-Region ist in Indonesien.

Andernfalls nutzen Sie die regionsübergreifende Datenfreigabe.

### Was soll ich mit meiner Datenfreigabe machen, wenn ich zu einem neuen Snowflake-Konto wechsle? {#what-should-i-do-with-my-data-share-when-i-switch-to-a-new-snowflake-account}
Sie können die alte Datenfreigabe, die mit Ihrem alten Snowflake-Konto verbunden ist, löschen und dann eine neue Freigabe für das neue Konto erstellen. Alle historischen Daten werden in der neuen Freigabe verfügbar sein.

### Warum sehe ich keine Daten in meiner Datenfreigabe? {#why-dont-i-see-data-in-my-data-share}
Sie haben bei der Erstellung Ihrer Datenfreigabe möglicherweise die falsche Snowflake-Konto-ID verwendet. Die Konto-ID auf dem Dashboard für die Datenfreigabe muss mit der Ausgabe von `CURRENT_ACCOUNT()` von Ihrem Snowflake-Konto übereinstimmen.

Wenn Ihre Freigabe regionsübergreifend ist, sind die Daten möglicherweise nicht sofort verfügbar. Je nach Datenvolumen kann es einige Stunden dauern, bis die Daten mit Ihrer Region synchronisiert sind.

### Warum erhalte ich eine Fehlermeldung zur Einhaltung des US-Gesetzes zum Schutz medizinischer Daten (HIPAA), wenn ich eine Datenfreigabe erstelle? {#why-am-i-receiving-a-hipaa-compliance-error-when-creating-a-data-share}

Das angegebene Konto entspricht entweder nicht dem US-Gesetz zum Schutz medizinischer Daten (HIPAA) oder verfügt über eine [Snowflake-Edition](https://docs.snowflake.com/en/user-guide/intro-editions) unterhalb von Business Critical. Ihr Snowflake-Konto muss auf die Business Critical Edition upgegradet werden, damit die Datenfreigabe dem US-Gesetz zum Schutz medizinischer Daten (HIPAA) entspricht. Wenden Sie sich an den Snowflake-Support, wenn Sie weitere Unterstützung beim Upgraden Ihres Kontos benötigen.

### Warum kann ich eine Datenfreigabe nicht neu erstellen, nachdem ich sie gelöscht habe? {#why-cant-i-recreate-a-data-share-after-deleting-one}

Es kann sein, dass das System die Löschung Ihrer vorherigen Datenfreigabe noch verarbeitet. Warten Sie einige Minuten, bis die Deprovisionierung abgeschlossen ist, und versuchen Sie dann erneut, die neue Datenfreigabe zu erstellen.

### Wie oft muss ich `CREATE DATABASE` ausführen, wenn ich mehrere Workspaces habe, die Daten für dasselbe Snowflake-Konto freigeben? {#how-many-times-do-i-need-to-run-create-database-when-i-have-multiple-workspaces-sharing-data-to-the-same-snowflake-account}

Sie müssen `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` nur einmal ausführen. Wenn mehrere Datenfreigaben aus verschiedenen Braze-Workspaces für dasselbe Snowflake-Konto freigegeben werden, werden sie automatisch in derselben Freigabe zusammengefasst. Nachdem Sie die erste Datenbank erstellt haben, werden Daten aus zusätzlichen Workspaces automatisch zur bestehenden Datenbank hinzugefügt, ohne dass zusätzliche Freigabeanfragen oder Schritte zur Datenbankerstellung erforderlich sind.

Wenn Sie beispielsweise eine Datenfreigabe für Snowflake-Konto 123 von Workspace A aus erstellen, akzeptieren Sie die Freigabeanfrage und erstellen eine Datenbank. Wenn Sie später eine Datenfreigabe für dasselbe Snowflake-Konto 123 von Workspace B aus erstellen, wird keine neue Freigabeanfrage gesendet – die Daten werden sofort zur bestehenden Freigabe hinzugefügt und sind in der zuvor erstellten Datenbank verfügbar.

### Wenn ich mehrere Workspaces habe, enthält dann eine einzige Datenbank die Daten aller dieser Workspaces? {#if-i-have-multiple-workspaces-does-a-single-database-contain-data-from-all-of-them}

Ja. Wenn Sie Daten aus mehreren Braze-Workspaces für dasselbe Snowflake-Konto freigeben, werden alle Daten in einer einzigen Freigabe zusammengefasst und sind in derselben Datenbank verfügbar. Sie können die Daten nach `app_group_id` filtern, um zwischen Workspaces zu unterscheiden.

Filtern Sie in Ihren Abfragen am besten immer nach `app_group_id`, um sie zukunftssicher zu machen. Dadurch wird sichergestellt, dass Ihre Dashboards und Berichte korrekt bleiben, wenn Sie in Zukunft weitere Workspaces hinzufügen. Ohne diesen Filter enthalten Ihre Metriken möglicherweise unerwartet Daten aus neu hinzugefügten Workspaces.

### Welche Vorgehensweise wird für die Verwaltung von Daten aus mehreren Workspaces in Snowflake empfohlen? {#what-is-the-recommended-approach-for-managing-data-from-multiple-workspaces-in-snowflake}

Senden Sie alle Braze-Daten in dieselbe Datenbank und filtern Sie nach `app_group_id`, um zwischen Workspaces zu unterscheiden. Dieser Ansatz vereinfacht die Datenverwaltung und gewährleistet eine konsistente Berichterstattung in Ihrem Unternehmen.

### Wie viele Snowflake-Datenfreigabe-Konnektoren benötige ich für mehrere Workspaces? {#how-many-snowflake-data-share-connectors-do-i-need-for-multiple-workspaces}

Die Anzahl der Konnektoren, die Sie benötigen, hängt von Ihrer spezifischen Konfiguration und Ihren Berechtigungen ab. Kontaktieren Sie Ihr Braze-Konto-Team, um mehr darüber zu erfahren, welche Berechtigungen für Ihren Anwendungsfall geeignet sind.

### Welche Optionen gibt es, um Daten aus verschiedenen Workspaces innerhalb desselben Snowflake-Kontos zu isolieren? {#what-options-exist-for-isolating-data-from-different-workspaces-within-the-same-snowflake-account}

Sie können die Daten logisch mithilfe der Spalte `app_group_id` isolieren, die angibt, zu welchem Workspace jede Datenzeile gehört. Die gängigsten Ansätze sind:

- **Views (empfohlen):** Erstellen Sie für jeden Workspace einen View, der nach `app_group_id` gefiltert ist. Dadurch werden Daten nicht dupliziert, während jedes Team oder jeder Anwendungsfall dennoch eine saubere, eingegrenzte Sicht auf die Workspace-Daten erhält.
- **Lokale Tabellenkopien:** Kopieren Sie Daten in separate Tabellen, die nach `app_group_id` gefiltert sind. Da hierbei Daten dupliziert werden, ist der Views-Ansatz in der Regel vorzuziehen.
- **Row-Access-Policies und Rollen:** Verwenden Sie Snowflake-native Row-Access-Policies in Kombination mit Rollen, um einzuschränken, welche Zeilen jede Rolle abfragen kann. Dadurch bleiben die Daten in einer einzigen Tabelle, während der Zugriff zur Abfragezeit durchgesetzt wird.

Sie konfigurieren diese Optionen innerhalb Ihres Snowflake-Kontos.

### Kann ich ein anderes Snowflake-Konto verwenden, um Daten aus verschiedenen Workspaces zu isolieren? {#can-i-use-a-different-snowflake-account-to-isolate-data-from-different-workspaces}

Ja. Wenn Workspace A Daten an Konto X und Workspace B Daten an Konto Y freigibt, erhält jedes Konto eine unabhängige Freigabe mit separaten Daten. Die meisten Unternehmen verwenden jedoch ein einziges Snowflake-Konto für alle Geschäftsdaten. Dieser Ansatz kann daher zusätzlichen operativen Aufwand verursachen. Wägen Sie diesen Kompromiss ab, bevor Sie sich für diese Lösung anstelle der in den vorherigen Abschnitten beschriebenen logischen Isolierungsansätze entscheiden.

### Ist die Isolierung von Workspace-Daten ein unterstützter Anwendungsfall für die Snowflake-Datenfreigabe? {#is-workspace-data-isolation-a-supported-use-case-for-snowflake-data-sharing}

Ja, über die in den vorherigen Abschnitten beschriebenen logischen Isolierungsansätze. Braze erstellt keine separaten Freigaben für jeden Workspace, sodass Sie die Isolierung auf Snowflake-Ebene mithilfe von Views, Row-Access-Policies oder separaten Konten verwalten.