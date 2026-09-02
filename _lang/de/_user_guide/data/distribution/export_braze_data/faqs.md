---
nav_title: FAQ
article_title: FAQ zum Exportieren
page_order: 7
page_type: FAQ
description: "Dieser Artikel behandelt einige häufig gestellte Fragen zu API- und CSV-Exporten."

---

# Häufig gestellte Fragen {#frequently-asked-questions}

> Auf dieser Seite finden Sie Antworten auf einige häufig gestellte Fragen zu API- und CSV-Exporten.

## Können bestimmte Exporte in Ihrem S3-Bucket erscheinen und andere nicht? {#can-you-make-certain-exports-appear-in-your-s3-bucket-and-others-not}

Nein. Wenn Sie S3-Zugangsdaten angegeben haben, werden alle Ihre Exporte in Ihrem S3-Bucket angezeigt. Wenn keine Zugangsdaten angegeben wurden, werden alle Exporte in einem S3-Bucket von Braze angezeigt.

## Muss ich S3-Zugangsdaten zu Braze hinzufügen, um Daten zu exportieren? {#do-i-have-to-add-s3-credentials-to-braze-to-export-data}

Nein. Wenn Sie keine S3-Zugangsdaten hinzufügen, werden Ihre Exporte in einem S3-Bucket angezeigt, der Braze gehört.

## Was passiert, wenn Sie S3-Zugangsdaten im Dashboard einrichten, aber nicht „Dies zum Standardziel für den Datenexport machen“ auswählen? {#what-happens-if-you-set-up-s3-credentials-in-the-dashboard-but-dont-select-make-this-the-default-data-export-destination}

Das Kontrollkästchen **Make this the default data export destination** hat Einfluss darauf, ob die Exporte an S3 oder Azure gehen, vorausgesetzt, Sie haben Zugangsdaten für beide hinzugefügt.

## Beeinflusst das Standardziel für den Datenexport Braze-Currents? {#does-the-default-data-export-destination-affect-braze-currents}

Nein. Currents verwendet einen eigenen Konnektor und eigene Speichereinstellungen. Die Auswahl eines Standardziels für CSV- und API-gesteuerte Exporte ändert nicht, wohin Currents-Daten geschrieben werden.

## Warum habe ich beim Exportieren von Nutzerprofilen in S3 mehrere Dateien erhalten? {#why-did-i-receive-multiple-files-when-exporting-user-profiles-to-s3}

Dies ist das erwartete Verhalten für Workspaces mit vielen Nutzer:innen. Braze teilt Ihren Export in mehrere Dateien auf, basierend auf der Anzahl der Nutzer:innen in Ihrem Workspace. In der Regel wird eine Datei pro 5.000 Nutzer:innen ausgegeben. Beachten Sie, dass Sie auch dann mehrere Dateien erhalten können, wenn Sie ein kleines Segment innerhalb eines großen Workspace exportieren.

## Warum sehe ich Duplikate, wenn ich Nutzer:innen über die Representational State Transfer API nach Segmenten exportiere? {#why-do-i-see-duplicates-when-i-export-users-by-segment-through-rest-api}

Dies ist ein sehr seltenes Vorkommen, das durch die zugrunde liegende Architektur des Datenbankanbieters verursacht wird. Duplikate werden jede Woche bereinigt; in den meisten Wochen werden jedoch keine Duplikate entfernt.

## Wie öffne ich CSV-Berichte in Excel? {#how-do-i-open-csv-reports-in-excel}

CSV-Dateien werden in der Regel standardmäßig automatisch in Excel geöffnet, aber das ist nicht immer der Fall. In den Artikeln zur Fehlerbehebung für [Windows](https://support.microsoft.com/en-us/windows/change-which-programs-windows-7-uses-by-default-62fd162f-8c82-0436-806f-c60d69dcf495) und [Apple](https://support.apple.com/guide/mac-help/choose-an-app-to-open-a-file-on-mac-mh35597/mac) finden Sie Schritte, um Excel als Standardprogramm festzulegen.

Um eine CSV-Datei in XLSX oder XLS umzuwandeln oder die Kommas zwischen den Datenwerten zu entfernen, lesen Sie [diese Anleitung zum Importieren von CSV-Dateien in Excel](https://www.ablebits.com/office-addins-blog/convert-csv-excel/#import-csv-wizard).

Wenn Sie feststellen, dass führende Nullen in Nutzer-IDs in Ihrem CSV-Export entfernt werden, liegt das daran, dass Excel die Zahlen in einer CSV-Datei als Daten statt als Text behandelt. Um dieses Problem zu beheben, verwenden Sie den [Excel-Textimport-Assistenten](https://www.ablebits.com/office-addins-blog/converting-csv-excel-issues/#leading-zeros).