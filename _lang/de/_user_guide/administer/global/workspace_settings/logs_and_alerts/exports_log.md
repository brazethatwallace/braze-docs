---
nav_title: Exportprotokoll
article_title: Exportprotokoll
page_order: 2
page_type: reference
description: "Auf dieser Seite finden Sie das Exportprotokoll, mit dem Sie den Status von Exportaufträgen einsehen und laufende Exporte abbrechen können."
---

# Exportprotokoll {#exports-log}

> Auf der Seite **Exportprotokoll** können Sie den Status von Exportaufträgen einsehen und laufende Exporte direkt von der Braze-Plattform aus abbrechen. Das Exportprotokoll unterstützt Segment- und [Unterdrückungslisten]({{site.baseurl}}/user_guide/audience/suppression_lists)-Exporte, die über das Dashboard oder die [Nutzerexport-API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) gestartet wurden.

Sie finden das Exportprotokoll unter **Einstellungen** > **Einrichtung und Tests** > **Exportprotokoll**.

## Was das Exportprotokoll anzeigt {#what-the-exports-log-shows}

Das Exportprotokoll listet Exportaufträge für den aktuellen Workspace auf. Jede Zeile stellt einen Exportversuch dar und enthält den Namen des Segments oder der Unterdrückungsliste, die Exportquelle, den Status und Zeitstempel.

| Spalte | Beschreibung |
|--------|-------------|
| Export-ID | Eindeutiger Bezeichner für den Exportauftrag. Wählen Sie diese ID aus, um Exportdetails zu öffnen oder das Protokoll zu teilen. |
| Segmentname | Name des exportierten Segments oder der Unterdrückungsliste. |
| Segmenttyp | Gibt an, ob der Export für ein **Segment** oder eine **Unterdrückungsliste** erfolgt. |
| Quelle | Wo der Export ausgelöst wurde: **Dashboard** (CSV-Export über die UI) oder **API** (Nutzer:innen-Export-API). |
| Status | Aktueller Zustand des Exportauftrags. Siehe [Exportstatus](#export-statuses). |
| Gestartet um | Zeitpunkt, zu dem der Exportauftrag begonnen hat. |
| Beendet um | Zeitpunkt, zu dem der Exportauftrag abgeschlossen wurde, fehlgeschlagen ist oder abgebrochen wurde. Leer, solange der Auftrag noch läuft. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Spalten des Exportprotokolls" }

## Exportstatus {#export-statuses}

| Status | Beschreibung |
|--------|-------------|
| In Progress | Der Exportauftrag wird ausgeführt. |
| Complete | Der Export wurde erfolgreich abgeschlossen. |
| Failed | Der Export wurde nicht abgeschlossen. |
| Cancelled | Der Export wurde vor dem Abschluss abgebrochen. |
| Cancelling | Eine Abbruchanfrage wird verarbeitet. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exportstatus" }

Sie können nur Exporte mit dem Status **In Progress** abbrechen. Wenn ein Export nicht mehr ausgeführt wird, ist die Abbrechen-Aktion nicht verfügbar.

## Exportdetails {#export-details}

Wählen Sie eine **Export-ID** aus, um zusätzliche Details für diesen Auftrag anzuzeigen, darunter:

| Feld | Beschreibung |
|-------|-------------|
| Ziel | Wohin exportierte Dateien zugestellt werden (z. B. ein Cloud-Speicherpfad, falls zutreffend). |
| Exportierte Felder | Nutzerprofilfelder, die im Export enthalten sind. |
| Selbst gehostet | Ob der Export eine vom Kunden gehostete Zustellung verwendet. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Felder der Exportdetails" }

Auf der Seite mit den Exportdetails können Sie einen laufenden Export abbrechen oder einen Link zum Protokolleintrag teilen.

## Verwandte Export-Workflows {#related-export-workflows}

| Exporttyp | So starten Sie | Dokumentation |
|-------------|--------------|---------------|
| Segment-CSV-Export | **Audience** > **Segments** > Segment auswählen > **User Data** > **CSV Export** | [Segmentdaten als CSV exportieren]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv) |
| Export der Unterdrückungsliste | **Audience** > **Suppression Lists** | [Unterdrückungslisten]({{site.baseurl}}/user_guide/audience/suppression_lists) |
| API-Segment-Export | `POST /users/export/segment` | [POST: Kundenprofil or Nutzerprofil nach Segment exportieren]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Verwandte Export-Workflows" }

## Abbrechen eines ausstehenden Exports {#cancelling-a-pending-export}

Sie können ausstehende Exporte direkt auf der Seite **Exports Log** abbrechen, indem Sie das Menü <i class="fas fa-ellipsis-vertical"></i> und dann **Cancel Export** auswählen, oder indem Sie die **Export ID** auswählen und dann auf der Seite des Exports **Cancel Export** auswählen.

## Ein bestimmtes Export-Log teilen {#sharing-a-specific-export-log}

Teilen Sie ein Export-Log, indem Sie die **Export-ID** auswählen und dann **Share Log** auswählen.