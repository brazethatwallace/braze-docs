Wenn Sie zwei angepasste Dateneinträge mit demselben sichtbaren Namen sehen, enthält möglicherweise ein Eintrag ein unsichtbares führendes oder nachgestelltes Leerzeichen.

So beheben Sie dieses Problem:

1. Gehen Sie zu **Dateneinstellungen** > **Angepasste Attribute** oder **Angepasste Events** und suchen Sie die beiden Einträge, die denselben Namen zu haben scheinen.
2. Überprüfen Sie, ob ein Name versteckte Leerzeichen enthält:
    1. Führen Sie einen Rechtsklick auf jeden Namen aus und wählen Sie **Untersuchen** aus.
    2. Überprüfen Sie den HTML-Textwert in den Entwicklertools Ihres Browsers.
    3. Vergleichen Sie die Werte (zum Beispiel `email` gegenüber ` email`).
    4. Bei Bedarf lesen Sie [Seiten und Stile mit Chrome DevTools untersuchen und bearbeiten](https://developer.chrome.com/docs/devtools/inspect-mode).
3. Entscheiden Sie, welcher Name als Ihr kanonischer Schlüssel beibehalten werden soll, und standardisieren Sie auf genau diese Schreibweise und Groß-/Kleinschreibung.
4. Wenn ein Eintrag führende oder nachgestellte Leerzeichen enthält und direkt im Dashboard erstellt wurde, verwenden Sie diesen Eintrag nicht mehr und wechseln Sie zum kanonischen Schlüssel:
    - Aktualisieren Sie alle Dashboard-Workflows, CSV-Importe und internen Runbooks, um den kanonischen Schlüssel zu verwenden.
    - Setzen Sie den fehlerhaften Eintrag auf die [Blocklist für angepasste Daten]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data), wenn Sie bereit sind, ihn außer Betrieb zu nehmen.
5. Überprüfen Sie Ihre Ingestion-Pfade:
    - API- und SDK-Payloads entfernen führende und nachgestellte Leerzeichen automatisch.
    - Im Dashboard erstellte Namen werden nicht automatisch gekürzt, daher sind manuelle Eingabe und Governance erforderlich.