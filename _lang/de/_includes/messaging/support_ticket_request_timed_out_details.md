- **Bildschirmaufnahme:** Eine Aufnahme der Schritte, die Sie vor dem Auftreten des Fehlers durchgeführt haben, einschließlich aller Seitenwechsel.
- **Zeitstempel und Zeitzone:** Der genaue Zeitpunkt, zu dem der Fehler aufgetreten ist, und Ihre Zeitzone.
- **Browser und Version:** Der Browser, den Sie verwenden (zum Beispiel Chrome 120, Safari 17), und ob Sie versucht haben, den Fehler in einem anderen Browser zu reproduzieren.
{% if include.context == 'Canvas' -%}
- **Schritte zur Reproduktion:** Eine klare Beschreibung der Aktionen, die den Fehler Trigger or triggern or triggern, einschließlich aller spezifischen Canvas-Schritte oder Konfigurationen, die beteiligt sind.
{% elsif include.context == 'campaign' -%}
- **Schritte zur Reproduktion:** Eine klare Beschreibung der Aktionen, die den Fehler Trigger or triggern or triggern, einschließlich aller spezifischen Campaign- oder Canvas-Einstellungen, die beteiligt sind.
{% endif -%}
- **Netzwerkprotokolle (optional):** Öffnen Sie die Entwicklertools Ihres Browsers (Tab **Network**), reproduzieren Sie den Fehler und exportieren Sie das Netzwerkprotokoll als HTTP-Archive-Datei (HAR). Dies hilft dem Support-Team festzustellen, welcher API-Aufruf ein Timeout verursacht.