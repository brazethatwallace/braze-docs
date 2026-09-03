---
nav_title: Datenaufnahme-Optionen vergleichen
article_title: Persistente und Zero-Copy-Datenaufnahme-Optionen vergleichen
page_order: 1
page_type: reference
description: "Vergleichen Sie Standard-CDI-Syncs, CDI Segments, CDI Canvas-Trigger und die /users/track-API, um zu entscheiden, wie Warehouse- oder Anwendungsdaten Braze-Profile, Segmente und Canvases erreichen."
---

# Persistente und Zero-Copy-Datenaufnahme-Optionen vergleichen {#compare-persistent-and-zero-copy-data-ingestion-options}

> Entscheiden Sie, wie Daten aus Ihrem Warehouse oder Ihren Anwendungen Braze erreichen – ob sie auf Nutzerprofile kopiert, direkt für die Segmentierung abgefragt oder vorübergehend an einen Canvas übergeben werden – bevor Sie Ihre Datenaufnahme-Pipelines entwerfen.

## Über dieses Beispiel {#about-this-example}

MovieCanon ist ein fiktiver Film-Streaming-Dienst. Kund:innen-, Ticket- und Aufrufdaten werden zentral in einem Warehouse gespeichert. Das Datenteam muss entscheiden, wie Braze für drei gängige Anforderungen mit Daten versorgt wird:

- **Profildaten:** Treueprogramm-Stufe, Lifetime-Value und Präferenzattribute für Genre oder Format, die auf Braze-Nutzerprofilen persistent gespeichert werden.
- **Zielgruppenbildung:** SQL-gesteuerte Segmente aus Warehouse-Tabellen, ohne jede Spalte nach Braze zu kopieren.
- **Getriggerte Nachrichten:** Warehouse-Zeilen, die einen Canvas-Eintritt mit zeilenspezifischer Personalisierung auslösen sollen, die nicht auf dem Profil gespeichert werden muss.

Braze bietet vier primäre Datenaufnahme-Pfade. Standard-Cloud Data Ingestion (CDI)-Syncs und die [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)-API speichern Daten persistent auf Profilen. CDI Segments (Connected Sources) und CDI Canvas-Trigger sind Zero-Copy-Optionen: Warehouse-Daten bleiben in Ihrem Warehouse und werden nicht auf Braze-Nutzerprofile geschrieben.

Nutzen Sie diesen Vergleich, wenn Sie Architektur planen, Durchsatz dimensionieren oder Trade-offs gegenüber Engineering- und Marketing-Stakeholdern erläutern. Er ersetzt nicht die Integrations-Setup-Anleitungen für die einzelnen Optionen.

## Hinweise {#considerations}

- Cloud Data Ingestion ist ein übergeordnetes Feature. Standard-CDI-Syncs kopieren Daten auf Braze-Profile (ähnlich wie `/users/track`). CDI Segments und CDI Canvas-Trigger lassen Warehouse-Daten an Ort und Stelle, ohne sie auf Braze-Nutzerprofile zu schreiben.
- Wiederkehrende CDI-Syncs können alle 15 Minuten bis einmal im Monat ausgeführt werden. Wenn Sie eine höhere Kadenz als 15 Minuten benötigen, wenden Sie sich an Ihren Customer-Success-Manager oder verwenden Sie die REST-API-Datenaufnahme. Siehe [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).
- CDI Canvas-Trigger teilen sich das Rate-Limit von [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) mit anderem Traffic an diesen Endpunkt. `/users/track` hat eigene Limits und Batching-Regeln. Standardlimits können erhöht werden. Gehen Sie zu **Einstellungen** > **APIs und Bezeichner** > **API-Limits** und lesen Sie [API-Rate-Limits]({{site.baseurl}}/api/api_limits).
- Connected Sources und CDI-Segmenterweiterungen führen Abfragen in Ihrem Warehouse aus. Sie tragen die Warehouse-Compute-Kosten; Braze protokolliert für diese Abfragen keine Datenpunkte. Siehe [Connected Sources]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources).

## Einrichtung {#setup}

### Schritt 1: Anwendungsfall einem Datenaufnahme-Pfad zuordnen {#step-1-map-your-use-case-to-an-ingestion-path}

Ordnen Sie Ihr Ziel dem empfohlenen Datenaufnahme-Pfad zu und prüfen Sie, ob dieser Pfad auf Braze-Profile schreibt.

| Ihr Ziel | Empfohlener Pfad | Schreibt auf Profile? |
| --- | --- | --- |
| Attribute, Ereignisse, Käufe oder Katalogartikel aus dem Warehouse persistent speichern | Standard-CDI-Sync | Ja (Daten werden auf Braze-Profile oder in Kataloge kopiert) |
| Zielgruppen aus Warehouse-SQL erstellen, ohne Quelltabellen nach Braze zu kopieren | CDI Segments (Connected Sources) | Nein (nur Zugehörigkeit) |
| Nutzer:innen mit Warehouse-Zeilenkontext in einen Canvas eintreten lassen, der nicht auf dem Profil persistent gespeichert werden soll | CDI Canvas-Trigger | Nein (transiente Canvas-Kontexteigenschaften) |
| Daten aus Apps, Servern oder Streaming-Pipelines nahezu in Realtime senden | [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) (oder SDKs) | Ja (Daten werden persistent auf Profilen gespeichert) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Anwendungsfall einem Datenaufnahme-Pfad zuordnen" }

### Schritt 2: Persistenz, Latenz und Durchsatz vergleichen {#step-2-compare-persistence-latency-and-throughput}

Vergleichen Sie, wie jeder Pfad Datenresidenz, Latenz, Durchsatz und Nutzererstellung handhabt.

| Dimension | Standard-CDI-Sync | CDI Segments | CDI Canvas-Trigger | `/users/track` |
| --- | --- | --- | --- | --- |
| Was es tut | Geplantes Lesen einer Warehouse-Tabelle; schreibt Attribute, Ereignisse, Käufe, Nutzerlöschungen oder Kataloge | Braze fragt Ihr Warehouse für SQL-Segmenterweiterungen ab | Warehouse-Zeilen triggern den Canvas-Eintritt mit Zeilenkontext als Canvas-Kontexteigenschaften | Apps, Server oder Streaming-Pipelines schreiben Attribute, Ereignisse und Käufe auf Profile |
| Datenresidenz | Kopiert und persistent auf Braze-Profilen gespeichert | Verbleibt in Ihrem Warehouse; nichts wird auf Profile geschrieben | Canvas-Kontexteigenschaften sind transient; nicht persistent auf Profilen gespeichert | Kopiert und persistent auf Braze-Profilen gespeichert |
| Typische Latenz | Nicht in Realtime; minimale Sync-Kadenz von 15 Minuten (Warehouse-Aktualität gilt ebenfalls) | Nicht in Realtime; Aktualisierung nach Ihrem Segmenterweiterungszeitplan (Zugehörigkeit aktualisiert sich nicht bei jeder Warehouse-Änderung) | Nicht in Realtime; begrenzt durch den Sync-Zeitplan (mindestens 15 Minuten) | Nahezu in Realtime (asynchrone Verarbeitung) |
| Durchsatz-Hinweise | Vollständiges Abfrageergebnis pro Sync; Braze batcht intern zu `/users/track`, `/users/delete` oder Katalog-Endpunkten | Abfrage-Laufzeitlimit von 60 Minuten pro Connected Source; kein Per-Request-Objektlimit | Teilt das `/canvas/trigger/send`-Rate-Limit; ca. 3,75 Millionen Canvas-Eintritte pro Stunde pro Sync-Lauf | Bis zu 75 kombinierte Objekte pro Anfrage; siehe [API-Rate-Limits]({{site.baseurl}}/api/api_limits) |
| Batch-Größe | Kein Per-Objekt-Limit auf CDI-Seite für Warehouse-Lesevorgänge | N/A (Abfrageergebnis definiert die Zugehörigkeit) | Ein Canvas-Eintritt pro Warehouse-Zeile pro Sync-Lauf | 75 Attribute, Ereignisse und Käufe kombiniert pro Anfrage (Standard) |
| Nutzererstellung | Ja, sofern nicht „nur vorhandene aktualisieren“ gesetzt ist | Nein (unbekannte Nutzer:innen im Abfrageergebnis werden ignoriert) | Nein (nur vorhandene Braze-Nutzer:innen) | Ja, sofern `_update_existing_only` nicht auf „true“ gesetzt ist |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Persistenz, Latenz und Durchsatz vergleichen" }

### Schritt 3: Schema- und Bezeichner-Anforderungen vergleichen {#step-3-compare-schema-and-identifier-requirements}

Vergleichen Sie erforderliche Spalten und unterstützte Bezeichner für jeden Pfad. Konfigurieren Sie einen Datentyp pro Standard-CDI-Sync (z. B. Attribute in einer Integration und Ereignisse in einer anderen).

| Dimension | Standard-CDI-Sync | CDI Segments | CDI Canvas-Trigger | `/users/track` |
| --- | --- | --- | --- | --- |
| Erforderliche Spalten / Struktur | Nutzerbezeichner + `UPDATED_AT` + `PAYLOAD` (JSON) pro Zeile | SQL muss nur `external_user_id` ausgeben | Bezeichner + `UPDATED_AT` + `PROPERTIES` (JSON; `{}` verwenden, wenn leer) | Standard-`/users/track`-Anfragetext |
| Unterstützte Bezeichner | `external_id`, Nutzer-Alias, `braze_id`, E-Mail oder Telefon | Nur `external_user_id` (String) | Nur `external_id` oder Nutzer-Alias | `external_id`, Nutzer-Alias, `braze_id`, E-Mail oder Telefon |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Schema- und Bezeichner-Anforderungen vergleichen" }

### Schritt 4: Den gewählten Pfad implementieren {#step-4-implement-the-path-you-selected}

- **Standard-CDI-Sync:** Erstellen Sie eine Warehouse-Tabelle oder -View und folgen Sie dann [Cloud Data Ingestion-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations) und [Tabelleneinrichtung]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup).
- **CDI Segments:** Fügen Sie eine [Connected Source]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources) hinzu und erstellen Sie dann eine [CDI-Segmenterweiterung]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments).
- **CDI Canvas-Trigger:** Richten Sie eine Quelltabelle mit `PROPERTIES` ein, erstellen und starten Sie einen Ziel-Canvas und erstellen Sie dann einen Sync gemäß [Zero-Copy-Personalisierung mit CDI]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync).
- **`/users/track`:** Senden Sie Anfragen aus Ihrer Anwendung oder Middleware. Formatieren Sie Payloads gemäß [POST: Nutzer:innen erstellen und aktualisieren]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

Für MovieCanon ist ein gängiges Muster: Standard-CDI-Syncs für nächtliche Profilanreicherung, CDI Segments für reine Warehouse-Zielgruppenregeln, Canvas-Trigger für Ticketstatus- oder Aufruf-Journeys mit Zeilenkontext und `/users/track` für Realtime-App-Ereignisse.

## Verwandte Artikel {#related-articles}

- [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)
- [Connected Sources]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources)
- [Zero-Copy-Personalisierung mit CDI]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync)
- [CDI-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments)
- [Tabelleneinrichtung für Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup)
- [POST: Nutzer:innen erstellen und aktualisieren]({{site.baseurl}}/api/endpoints/user_data/post_user_track)
- [API-Rate-Limits]({{site.baseurl}}/api/api_limits)