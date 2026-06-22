{% if include.section == "multi-language prerequisites" %}

| Feature | Erforderliche Nutzer:innen-Berechtigungen |
| --- | --- |
| Mehrsprachige Lokalisierungen | Sie benötigen die folgenden Berechtigungen, um mehrsprachige Lokalisierungen zu erstellen und zu verwalten:<br><br> {::nomarkdown} <ul><li>Lokalisierungseinstellungen bearbeiten</li><li>Lokalisierungseinstellungen löschen</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Table" }

{% endif %}

{% if include.section == "Preview" %}

## Vorschau Ihrer Lokalisierungen {#preview-your-locales}

Wählen Sie im Dropdown-Menü **Preview message as user** auf dem Tab **Test** die Option **Custom user** aus und geben Sie verschiedene Sprachen ein, um eine Vorschau der Nachricht anzuzeigen und zu prüfen, ob Ihre Nachricht wie erwartet übersetzt wird.

{% endif %}

{% if include.section == "Frequently Asked Questions" %}

## Häufig gestellte Fragen {#frequently-asked-questions}

#### Kann ich eine Änderung am übersetzten Text in einer meiner Lokalisierungen vornehmen? {#can-i-make-a-change-to-the-translated-copy-in-one-of-my-locales}
Ja. Nehmen Sie zunächst die Bearbeitung in der CSV-Datei vor und laden Sie die Datei dann erneut hoch, um eine Änderung am übersetzten Text vorzunehmen.

#### Lassen sich Übersetzungs-Tags verschachteln? {#can-i-nest-translation-tags}
Nein.

#### Können Übersetzungs-Tags mit HTML-Styling versehen werden? {#can-i-add-html-styling-in-the-translation-tags}
Ja, aber achten Sie darauf, dass das HTML-Styling nicht mit dem Inhalt übersetzt wird.

#### Welche Validierungen oder zusätzlichen Prüfungen führt Braze durch? {#what-validations-or-extra-checks-does-braze-do}

| Szenario                                                                                                                                                 | Validierung in Braze                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| In einer Übersetzungsdatei fehlen die mit der aktuellen Nachricht verbundenen Lokalisierungen.                                                                               | Diese Übersetzungsdatei wird nicht hochgeladen.                                                                       |
| In einer Übersetzungsdatei fehlen Textblöcke, etwa Text innerhalb von Liquid-Übersetzungs-Tags, aus der aktuellen E-Mail-Nachricht.                                | Diese Übersetzungsdatei wird nicht hochgeladen.                                                                       |
| Die Übersetzungsdatei enthält den Standardtext, der nicht mit den Textblöcken der aktuellen E-Mail-Nachricht übereinstimmt.                                          | Diese Übersetzungsdatei wird nicht hochgeladen. Korrigieren Sie den Fehler in der CSV-Datei, bevor Sie den Upload erneut versuchen.               |
| Die Übersetzungsdatei enthält Lokalisierungen, die in den Einstellungen unter **Unterstützung mehrerer Sprachen** nicht vorhanden sind.                                                           | Diese Lokalisierungen werden nicht in Braze gespeichert.                                                                      |
| Die Übersetzungsdatei enthält Textblöcke, die in der aktuellen Nachricht nicht vorhanden sind (z. B. im aktuellen Entwurf zum Zeitpunkt des Hochladens der Übersetzungen). | Textblöcke, die in der aktuellen Nachricht nicht vorhanden sind, werden nicht aus der Übersetzungsdatei in Braze übernommen. |
| Eine Lokalisierung wird aus einer Nachricht entfernt, nachdem sie als Teil der Übersetzungsdatei in die Nachricht hochgeladen wurde.                           | Wenn Sie die Lokalisierung entfernen, werden alle damit verbundenen Übersetzungen in der Nachricht gelöscht.                   |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Welche Validierungen oder zusätzlichen Prüfungen führt Braze durch?" }

{% endif %}