---
nav_title: FAQ
article_title: Snowflake FAQ zur Datenfreigabe
page_order: 50
page_type: FAQ
description: "Dieser Artikel beantwortet häufig gestellte Fragen zur Datenfreigabe in Snowflake."

---

# Häufig gestellte Fragen {#frequently-asked-questions}

## Ist es möglich, PII-Daten über Snowflake Data Sharing zu verschleiern? {#is-it-possible-to-obfuscate-pii-data-via-snowflake-data-sharing}
Nein, das wird derzeit nicht unterstützt.

## Benötige ich Data Sharing für dieselbe Region oder regionsübergreifend? {#do-i-need-data-share-for-the-same-region-or-cross-region}
Verwenden Sie Data Sharing für dieselbe Region in den folgenden Szenarien:
- Ihr Snowflake-Konto befindet sich in US-EAST-1 (AWS) und Ihre Braze-Dashboard-Region ist in den USA.
- Ihre Snowflake-Region ist EU-CENTRAL-1 (AWS) und Ihre Braze-Dashboard-Region ist in der EU.
- Ihre Snowflake-Region ist AP-Northeast-1 (AWS) und Ihre Braze-Dashboard-Region ist in Japan.
- Ihre Snowflake-Region ist AP-Southeast-2 (AWS) und Ihre Braze-Dashboard-Region ist in Australien.
- Ihre Snowflake-Region ist AP-Southeast-3 (AWS) und Ihre Braze-Dashboard-Region ist in Indonesien.

Verwenden Sie andernfalls regionsübergreifendes Data Sharing.

## Was sollte ich mit meinem Data Share tun, wenn ich zu einem neuen Snowflake-Konto wechsle? {#what-should-i-do-with-my-data-share-when-i-switch-to-a-new-snowflake-account}
Sie können den alten Data Share, der mit Ihrem alten Snowflake-Konto verknüpft ist, löschen und dann einen neuen Share für das neue Konto erstellen. Alle historischen Daten sind im neuen Share verfügbar.

## Was passiert, wenn ich meinen Daten-Share auf einen neuen Braze-Workspace umstelle? {#what-happens-if-i-switch-my-data-share-to-a-new-braze-workspace}

Wenn Sie eine bestehende Daten-Share-Integration so umkonfigurieren, dass sie einen anderen Braze-Workspace verwendet, wird möglicherweise folgender Fehler in Snowflake angezeigt, wenn Sie Tabellen abfragen:

> Shared database is no longer available for use. It will need to be re-created if and when the publisher makes it available again.

Um dieses Problem zu beheben, müssen Sie den Share in Snowflake löschen und neu erstellen:

1. Löschen Sie die Datenbank, die mit dem vorherigen Share erstellt wurde.
2. Erstellen Sie die Datenbank erneut gemäß den [Integrationsanweisungen]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake#step-2-create-the-database-in-snowflake).
3. Vergeben Sie alle erforderlichen Zugriffsrechte für die neue Datenbank erneut.
4. Erstellen Sie alle Views (falls zutreffend) neu, die auf die alte Datenbank verwiesen haben.

{% alert note %}
In der neuen Snowflake-Oberfläche finden Sie den Braze-Share unter **Data Products** > **Private Sharing** > **Shared with you**.
{% endalert %}

## Warum sehe ich keine Daten in meinem Data Share? {#why-dont-i-see-data-in-my-data-share}
Möglicherweise haben Sie beim Erstellen Ihres Data Shares die falsche Snowflake-Konto-ID verwendet. Die Konto-ID im Data-Sharing-Dashboard muss mit der Ausgabe von `CURRENT_ACCOUNT()` aus Ihrem Snowflake-Konto übereinstimmen.

Wenn Ihr Share regionsübergreifend ist, sind die Daten möglicherweise nicht sofort verfügbar. Abhängig von Ihrem Datenvolumen kann es einige Stunden dauern, bis die Daten mit Ihrer Region synchronisiert sind.

## Warum erhalte ich einen HIPAA-Compliance-Fehler beim Erstellen einer Datenfreigabe? {#why-am-i-receiving-a-hipaa-compliance-error-when-creating-a-data-share}

Das angegebene Konto ist entweder nicht HIPAA-konform oder verwendet eine [Snowflake Edition](https://docs.snowflake.com/en/user-guide/intro-editions) unterhalb von Business Critical. Ihr Snowflake-Konto muss auf die Business Critical Edition aktualisiert werden, um für die Datenfreigabe HIPAA-konform zu sein. Wenden Sie sich an den Snowflake-Support, um weitere Unterstützung beim Upgrade Ihres Kontos zu erhalten.

## Warum kann ich einen Data Share nach dem Löschen nicht neu erstellen? {#why-cant-i-recreate-a-data-share-after-deleting-one}

Möglicherweise verarbeitet das System noch die Löschung Ihres vorherigen Data Share. Warten Sie einige Minuten, bis der Deprovisionierungsprozess abgeschlossen ist, und versuchen Sie dann erneut, den neuen Data Share zu erstellen.

## Wie oft muss ich `CREATE DATABASE` ausführen, wenn mehrere Workspaces Daten an dasselbe Snowflake-Konto teilen? {#how-many-times-do-i-need-to-run-create-database-when-i-have-multiple-workspaces-sharing-data-to-the-same-snowflake-account}

Sie müssen `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` nur einmal ausführen. Wenn mehrere Datenfreigaben aus verschiedenen Braze-Workspaces an dasselbe Snowflake-Konto geteilt werden, werden sie automatisch in derselben Freigabe zusammengeführt. Nachdem Sie die erste Datenbank erstellt haben, werden Daten aus zusätzlichen Workspaces automatisch zur bestehenden Datenbank hinzugefügt, ohne dass weitere Freigabeanfragen oder Schritte zur Datenbankerstellung erforderlich sind.

Wenn Sie beispielsweise eine Datenfreigabe an Snowflake-Konto 123 aus Workspace A erstellen, akzeptieren Sie die Freigabeanfrage und erstellen eine Datenbank. Wenn Sie später eine Datenfreigabe an dasselbe Snowflake-Konto 123 aus Workspace B erstellen, wird keine neue Freigabeanfrage gesendet – die Daten werden sofort zur bestehenden Freigabe hinzugefügt und sind in der zuvor erstellten Datenbank verfügbar.

## Wenn ich mehrere Workspaces habe, enthält eine einzelne Datenbank Daten aus allen? {#if-i-have-multiple-workspaces-does-a-single-database-contain-data-from-all-of-them}

Ja. Wenn Sie Daten aus mehreren Braze-Workspaces an dasselbe Snowflake-Konto weitergeben, werden alle Daten in einem einzigen Share zusammengeführt und sind in derselben Datenbank verfügbar. Sie können die Daten nach `app_group_id` filtern, um zwischen Workspaces zu unterscheiden.

Als Best Practice sollten Sie Ihre Abfragen immer nach `app_group_id` filtern, um sie zukunftssicher zu machen. So stellen Sie sicher, dass Ihre Dashboards und Berichte korrekt bleiben, wenn Sie in Zukunft weitere Workspaces hinzufügen. Ohne diesen Filter könnten Ihre Metriken unerwartet Daten aus neu hinzugefügten Workspaces enthalten.

## Was ist der empfohlene Ansatz für die Verwaltung von Daten aus mehreren Workspaces in Snowflake? {#what-is-the-recommended-approach-for-managing-data-from-multiple-workspaces-in-snowflake}

Senden Sie alle Braze-Daten in dieselbe Datenbank und filtern Sie nach `app_group_id`, um zwischen Workspaces zu unterscheiden. Dieser Ansatz vereinfacht die Datenverwaltung und gewährleistet ein konsistentes Reporting in Ihrer gesamten Organisation.

## Wie viele Snowflake Data Share Konnektoren benötige ich für mehrere Workspaces? {#how-many-snowflake-data-share-connectors-do-i-need-for-multiple-workspaces}

Die Anzahl der Konnektoren, die Sie benötigen, hängt von Ihrer spezifischen Konfiguration und Ihren Berechtigungen ab. Wenden Sie sich an Ihr Braze-Konto-Team, um mehr darüber zu erfahren, welche Berechtigungen für Ihren Anwendungsfall geeignet sind.

## Welche Möglichkeiten gibt es, Daten verschiedener Workspaces innerhalb desselben Snowflake-Kontos zu isolieren? {#what-options-exist-for-isolating-data-from-different-workspaces-within-the-same-snowflake-account}

Sie können Daten logisch mithilfe der Spalte `app_group_id` isolieren, die angibt, zu welchem Workspace jede Datenzeile gehört. Die gängigsten Ansätze sind:

- **Views (empfohlen):** Erstellen Sie für jeden Workspace eine View, die nach `app_group_id` gefiltert ist. So vermeiden Sie das Duplizieren von Daten und geben jedem Team oder Anwendungsfall dennoch eine saubere, eingegrenzte Sicht auf die Daten seines Workspace.
- **Lokale Tabellenkopien:** Kopieren Sie Daten in separate Tabellen, die nach `app_group_id` gefiltert sind. Da hierbei Daten dupliziert werden, ist der Views-Ansatz in der Regel vorzuziehen.
- **Row Access Policies und Rollen:** Verwenden Sie Snowflake-native Row Access Policies in Kombination mit Rollen, um einzuschränken, welche Zeilen jede Rolle abfragen kann. So bleiben die Daten in einer einzigen Tabelle, während der Zugriff zur Abfragezeit durchgesetzt wird.

Sie konfigurieren diese Optionen innerhalb Ihres Snowflake-Kontos.

## Kann ich ein anderes Snowflake-Konto verwenden, um Daten aus verschiedenen Workspaces zu isolieren? {#can-i-use-a-different-snowflake-account-to-isolate-data-from-different-workspaces}

Ja. Wenn Workspace A an Konto X und Workspace B an Konto Y teilt, erhält jedes Konto einen unabhängigen Share mit separaten Daten. Die meisten Organisationen verwenden jedoch ein einziges Snowflake-Konto für alle Geschäftsdaten. Dieser Ansatz kann daher zusätzlichen operativen Aufwand verursachen. Wägen Sie diesen Kompromiss ab, bevor Sie sich für diese Lösung anstelle der im vorherigen Abschnitt beschriebenen logischen Isolierungsansätze entscheiden.

## Ist die Datenisolierung von Workspaces ein unterstützter Anwendungsfall für Snowflake Data Sharing? {#is-workspace-data-isolation-a-supported-use-case-for-snowflake-data-sharing}

Ja, durch die in den vorherigen Abschnitten beschriebenen Ansätze zur logischen Isolierung. Braze erstellt keine separaten Shares für jeden Workspace, sodass Sie die Isolierung auf Snowflake-Ebene mithilfe von Views, Row Access Policies oder separaten Konten verwalten.