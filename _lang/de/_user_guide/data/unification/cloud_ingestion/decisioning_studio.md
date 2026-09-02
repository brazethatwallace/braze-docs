---
nav_title: Decisioning-Studio-Daten synchronisieren
article_title: "BrazeAI Decisioning Studio-Daten synchronisieren"
description: "Erfahren Sie, wie Sie Data-Warehouse-Tabellen mithilfe der Cloud-Datenaufnahme mit BrazeAI Decisioning Studio synchronisieren."
page_order: 6.5
page_type: reference
toc_headers: h2
---

# BrazeAI Decisioning Studio-Daten synchronisieren {#sync-brazeai-decisioning-studio-data}

> Diese Seite beschreibt, wie Sie Daten aus Ihrem Data Warehouse mithilfe der Cloud-Datenaufnahme (CDI) direkt mit BrazeAI Decisioning Studio™ synchronisieren.

Mit dem Decisioning-Studio-Ziel von CDI können Warehouse-Daten direkt mit BrazeAI Decisioning Studio synchronisiert werden. Daten aus diesen Synchronisierungen werden Decisioning Studio zur Aktivierung bereitgestellt, Ihre Nutzerprofile und Braze-Workspaces bleiben dabei unverändert.

{% alert important %}
Dieses Feature befindet sich im Early Access. Wenden Sie sich an Ihren CSM or Customer-Success-Manager or Customer-Success-Manager:in oder Account Manager:in, um Zugang zu erhalten.
{% endalert %}

## Funktionsweise {#how-it-works}

Wenn Sie eine Synchronisierung erstellen, wählen Sie Decisioning Studio als Ziel und schreiben eine SQL-Abfrage, die die zu synchronisierenden Daten zurückgibt. CDI führt diese Abfrage nach dem von Ihnen festgelegten Zeitplan aus und liefert die Ergebnisse als Decisioning-Studio-Asset. Jede Synchronisierung wird einem einzelnen Asset zugeordnet, sodass Sie nicht mehr als eine Synchronisierung auf dasselbe Asset verweisen können.

Im Gegensatz zu Synchronisierungen mit der Braze Data Platform ordnen Decisioning-Studio-Synchronisierungen Ihre Daten nicht Nutzerprofilen, Ereignissen oder Katalogen zu.

Informationen zu weiteren Möglichkeiten, Daten für Decisioning Studio verfügbar zu machen, finden Sie unter [Daten verbinden]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/connect_data_sources).

## Voraussetzungen {#prerequisites}

- Zugang zu Braze und BrazeAI Decisioning Studio.
- Eine aktive Cloud-Datenaufnahme-Data-Warehouse-Quelle. Falls Sie noch keine eingerichtet haben, siehe [Data-Warehouse-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).
- Die Tabelle oder View, die Sie synchronisieren möchten.
- Eine Spalte (oder mehrere Spalten) in dieser Tabelle als Primärschlüssel sowie eine Zeitstempel-Spalte, die CDI für die inkrementelle Synchronisierung verwenden kann.

## Eine Decisioning-Studio-Synchronisierung erstellen {#create-a-decisioning-studio-sync}

### Schritt 1: Synchronisierung erstellen und Ziel auswählen {#step-1-create-the-sync-and-select-the-destination}

1. Gehen Sie zu **Data Settings** > **Cloud Data Ingestion** > **Syncs**.
2. Wählen Sie **Create data sync**.
3. Geben Sie einen **Integration Name** ein und wählen Sie dann Ihre Quelle unter **Data sources** aus.
4. Setzen Sie unter **Destination** die **Data destination** auf **BrazeAI Decisioning Studio™**.
5. Wählen Sie unter **Data category** den **Decisioning Studio data**-Typ, der am besten zu Ihrer Tabelle passt. Wählen Sie zwischen **Kundenprofil or Kundenprofil or Nutzerprofil or Kundenprofil or Nutzerprofil**, **Message engagement events**, **Conversion events** oder **Other**. Dies taggt die Daten für Decisioning Studio und ändert nicht, wie CDI Ihre Zeilen verarbeitet.

### Schritt 2: SQL-Abfrage schreiben {#step-2-write-your-sql-query}

Schreiben Sie im Schritt **Data definition** eine SQL-Abfrage, die die Daten aus der Tabelle oder View zurückgibt, die Sie synchronisieren möchten. Das Abfrageergebnis wird zum Schema Ihrer Synchronisierung.

Sie können den Source Explorer verwenden, um verfügbare Tabellen und Views zu durchsuchen, oder den KI or künstliche Intelligenz-SQL-Generator nutzen, um Hilfe beim Schreiben Ihrer Abfrage zu erhalten.

Ihre Abfrage muss eine `UPDATED_AT`-Spalte zurückgeben, da CDI `UPDATED_AT` für die inkrementelle Synchronisierung und Änderungsverfolgung verwendet. Bei jedem Synchronisierungslauf synchronisiert CDI nur Zeilen, bei denen `UPDATED_AT` nach dem zuletzt synchronisierten Wert liegt. Falls die von Ihnen identifizierte Zeitstempel-Spalte nicht bereits `UPDATED_AT` heißt, können Sie sie in Ihrer Abfrage mit einem Alias versehen:

```sql
SELECT *, LAST_MODIFIED AS UPDATED_AT FROM my_table
```

Weitere Informationen dazu, wie `UPDATED_AT` die inkrementelle Synchronisierung steuert – einschließlich dessen, was passiert, wenn Sie den Wert zurücksetzen – finden Sie unter [Die UPDATED_AT-Spalte verstehen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices#understanding-the-updated_at-column).

{% alert note %}
Es werden nur einzelne, schreibgeschützte Abfragen unterstützt, einschließlich `JOIN`-Klauseln. CDI führt schreibgeschützte Abfragen aus und ändert Ihre zugrunde liegenden Tabellen nicht.
{% endalert %}

### Schritt 3: Abfrage in der Vorschau anzeigen und validieren {#step-3-preview-and-validate-your-query}

Wählen Sie **Preview and validate**, um Ihre Abfrage auszuführen. Der Abschnitt **Query preview (first 10 rows)** zeigt die ersten 10 Zeilen, die von Ihrer Quelle zurückgegeben werden, zusammen mit dem erkannten Datentyp jeder Spalte, sodass Sie die Korrektheit der Daten bestätigen können, bevor Sie fortfahren.

### Schritt 4: Primärschlüssel auswählen {#step-4-select-a-primary-key}

Jede Decisioning-Studio-Synchronisierung benötigt einen Primär- oder zusammengesetzten Schlüssel – eine oder mehrere Spalten, die jede Zeile eindeutig identifizieren. Öffnen Sie nach erfolgreicher Validierung das Dropdown **Primary key** und wählen Sie eine Spalte als Primärschlüssel aus. Die Auswahl mehrerer Spalten bildet einen zusammengesetzten Schlüssel.

{% alert tip %}
Ein guter Primärschlüssel ist für jede Zeile eindeutig, niemals leer und über Synchronisierungsläufe hinweg stabil. Vermeiden Sie Werte, die zur Abfragezeit generiert werden, wie `UUID()` oder `CURRENT_TIMESTAMP`, da diese zu doppelten oder fehlenden Zeilen führen können.
{% endalert %}

### Schritt 5: Benachrichtigungen und Zeitplan festlegen und Synchronisierung erstellen {#step-5-set-notifications-schedule-and-create-the-sync}

1. Geben Sie im Schritt **Notifications** eine oder mehrere **Contact Email(s)** ein, um Benachrichtigungen über Synchronisierungsfehler zu erhalten. Sie können auch **Row Error**- und **Sync success**-Benachrichtigungen aktivieren.
2. Aktivieren Sie im Schritt **Schedule** die Option **Recurring sync**, um die Synchronisierung automatisch nach einem Zeitplan auszuführen. Bei deaktiviertem **Recurring sync** wird die Synchronisierung nur ausgeführt, wenn Sie sie auslösen – entweder manuell über das Dashboard oder über den Endpunkt [Synchronisierung Trigger or triggern or triggern]({{site.baseurl}}/api/endpoints/cdi/post_job_sync).
3. Überprüfen Sie die **Summary** und erstellen Sie dann die Synchronisierung.

## Eine Synchronisierung bearbeiten {#editing-a-sync}

Wenn Sie eine bestehende Synchronisierung bearbeiten, erfordert jede Änderung an Ihrer SQL-Abfrage eine erneute Validierung, bevor Sie speichern können. Primär- und zusammengesetzte Schlüssel können nicht geändert werden und müssen weiterhin zurückgegeben werden.

Gültige Änderungen werden beim nächsten Synchronisierungslauf wirksam.

## Umgang mit Schemaänderungen {#handling-schema-changes}

CDI behandelt Schemaänderungen an der Quelle additiv. Bei jedem Synchronisierungslauf vergleicht CDI Ihr Quellschema mit dem bestehenden Decisioning-Studio-Asset und fügt neue Spalten hinzu, während die bereits vorhandenen erhalten bleiben.

| Änderung in Ihrer Quelltabelle | Synchronisierungsverhalten |
|---|---|
| Eine neue Spalte wird hinzugefügt | CDI fügt die Spalte dem Decisioning-Studio-Asset hinzu. Zeilen, die vor dem Vorhandensein der Spalte geliefert wurden, zeigen `null` für diese Spalte an. |
| Eine Spalte wird entfernt | CDI aktualisiert diese Spalte nicht mehr, aber die Spalte und ihre vorhandenen Daten bleiben im Asset erhalten. Die anderen Spalten werden weiterhin synchronisiert. |
| Eine Spalte wird umbenannt | Wird als entfernte Spalte plus neue Spalte behandelt. Die ursprüngliche Spalte bleibt im Asset erhalten, und die neue Spalte wird hinzugefügt. |
| Der Datentyp einer Spalte ändert sich | CDI konvertiert Werte, wo dies möglich ist. Zeilen, die nicht konvertiert werden können, werden als Zeilenfehler in den Laufdetails der Synchronisierung gemeldet. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Umgang mit Schemaänderungen" }

Wenn CDI eine Schemaänderung erkennt, wird diese in den Laufdetails der Synchronisierung und auf der Seite zur Bearbeitung der Synchronisierung angezeigt, und Ihre Benachrichtigungskontakte erhalten eine E-Mail-Benachrichtigung. Um zu ändern, welche Spalten geliefert werden, Update or aktualisieren or aktualisieren Sie Ihre SQL-Abfrage und validieren Sie erneut.