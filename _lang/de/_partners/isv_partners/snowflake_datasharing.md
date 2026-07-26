---
nav_title: Snowflake Datenfreigabe
hidden: true
---

# Snowflake-Integration zur Datenfreigabe {#snowflake-data-sharing-integration}

> Wenn Snowflake Data Share als Integrationsmethode verwendet wird, stellt Braze im Namen der Kund:innen eine Freigabe für Ihre Snowflake-Instanz bereit. Diese Freigabe umfasst automatisch alle Ereignisse zum Nachrichten-Engagement und zum Verhalten der Nutzer:innen.

Freigaben werden pro geschäftskunden bereitgestellt, nachdem die Kund:innen eine Berechtigung für Snowflake Data Share erworben haben. Wenn Kund:innen eine Datenfreigabe anfordern, fügt Braze dem Workspace der Kund:innen eine Freigabe hinzu, und die Kund:innen können die Self-Service-UI verwenden, um die entsprechenden Daten des Partner-Snowflake-Kontos hinzuzufügen.

![Bereitstellung der Snowflake-Datenfreigabe im Braze-Dashboard]({% image_buster /assets/img/snowflake.png %})

Sobald die Freigabe bereitgestellt ist, sind alle Daten sofort innerhalb der Snowflake-Instanz als eingehende Datenfreigabe zugänglich.

![Eingehende Snowflake-Datenfreigabe in der Snowflake-Instanz der Kund:innen]({% image_buster /assets/img/snowflake2.png %})

Innerhalb Ihrer Snowflake-Instanz sehen Sie eine Freigabe pro Region. Jede Tabelle hat eine Spalte, `app_group_id`, die im Grunde ein Mandantenschlüssel für Braze ist. Wenn neue Kund:innen innerhalb derselben Region zu einer Freigabe hinzugefügt werden, erscheinen sie als unterschiedliche `app_group_ids` in den bestehenden Tabellen.

{% alert important %}
Braze hostet derzeit alle Nutzer:innen-Daten in den Snowflake-AWS-Regionen US East-1 und EU-Central (Frankfurt). Obwohl Braze regionsübergreifend teilen kann, ist es für die Kund:innen am kostengünstigsten, wenn die Freigabe mit `US-EAST-1` und/oder `EU-CENTRAL-1` erfolgt.
{% endalert %}

{% alert tip %}
Laden Sie die [Rohtabellenschemata](/docs/assets/download_file/data-sharing-raw-table-schemas.txt) herunter oder verwenden Sie diesen Satz von [Beispiel-Ereignisdaten](https://app.snowflake.com/marketplace/listing/GZT0Z5I4XY0/braze-braze-user-event-demo-dataset), der auf dem Snowflake-Marktplatz verfügbar ist, um sich mit den freigegebenen Ereignissen vertraut zu machen.
{% endalert %}

## Umgang mit doppelten Ereignissen {#handling-duplicate-events}

Duplikate sind zu erwarten, aber alle Ereignisse haben einen eindeutigen Bezeichner, die ID-Spalte. Duplikate können mit `select distinct(id)` entfernt werden.

## Nicht abwärtskompatible versus abwärtskompatible Änderungen {#breaking-versus-non-breaking-changes}

### Abwärtskompatible Änderungen {#non-breaking-changes}

{% multi_lang_include partners/snowflake/non_breaking_changes.md %}

{% alert important %}
Da neue Spalten als abwärtskompatibel gelten, empfiehlt Braze dringend, die gewünschten Spalten in jeder Abfrage explizit aufzuführen, anstatt `SELECT *`-Abfragen zu verwenden. Alternativ können Sie auch Ansichten erstellen, die Spalten explizit benennen, und diese Ansichten dann anstelle der Tabellen direkt abfragen.
{% endalert %}

### Nicht abwärtskompatible Änderungen {#breaking-changes}

{% multi_lang_include partners/snowflake/breaking_changes.md %}

## Wann die Tabellen SNAPSHOTS und CHANGELOGS aktualisiert werden {#when-snapshots-and-changelogs-tables-are-updated}

Die Tabellen SNAPSHOTS und CHANGELOGS verfolgen Änderungen an Campaigns und Canvases. Zu wissen, wann diese Tabellen aktualisiert werden, ist wichtig für die Abfrage der neuesten Nachrichtenvarianten und Canvas-Konfigurationen.

### CHANGELOGS_CAMPAIGN_SHARED

Eine Zeile wird zu `CHANGELOGS_CAMPAIGN_SHARED` hinzugefügt, wenn:
- Die Campaign gestartet wird, ODER
- Eines der folgenden Snapshot-fähigen Felder geändert wird:
  - Name
  - Aktionen (einschließlich Änderungen des Nachrichteninhalts)
  - Conversion-Verhalten

{% alert important %}
Das Speichern oder Aktualisieren des Entwurfs nach dem Start löst nicht automatisch ein Update aus. Das Update wird nur dann getriggert, wenn Sie die Campaign starten oder die Änderungen des Entwurfs nach dem Start auf die aktive Campaign anwenden.
{% endalert %}

### SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED

`SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED` wird von `CHANGELOGS_CAMPAIGN_SHARED` abgeleitet. Diese Tabelle extrahiert und vereinzelt die Aktionsspalte aus `CHANGELOGS_CAMPAIGN_SHARED` in einzelne Datensätze für Nachrichtenvarianten. Sie wird entsprechend aktualisiert, wenn `CHANGELOGS_CAMPAIGN_SHARED` aktualisiert wird.

### CHANGELOGS_CANVAS_SHARED

Eine Zeile wird zu `CHANGELOGS_CANVAS_SHARED` hinzugefügt, wenn:
- Das Canvas gestartet wird, ODER
- Eines der folgenden Snapshot-fähigen Felder geändert wird:
  - Name
  - Conversion-Verhalten
  - Varianten (Prozentsatz, Zuordnungen des ersten Schritts, Variantennamen)

{% alert important %}
Das Speichern oder Aktualisieren des Entwurfs nach dem Start löst nicht automatisch ein Update aus. Das Update wird nur dann getriggert, wenn Sie das Canvas starten oder die nach dem Start vorgenommenen Änderungen am Entwurf auf das aktive Canvas anwenden.
{% endalert %}

### SNAPSHOTS_CANVAS_VARIATION_SHARED

`SNAPSHOTS_CANVAS_VARIATION_SHARED` wird von `CHANGELOGS_CANVAS_SHARED` abgeleitet. Diese Tabelle verwendet das gleiche Extraktionsmuster wie `SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED` und wird entsprechend aktualisiert, wenn `CHANGELOGS_CANVAS_SHARED` aktualisiert wird.

### SNAPSHOTS_CANVAS_STEP_SHARED

Eine Zeile wird zu `SNAPSHOTS_CANVAS_STEP_SHARED` hinzugefügt, wenn:
- Das Canvas gestartet wird, ODER
- Das aktive Canvas aktualisiert wird (Entwurf nach dem Start angewendet), ODER
- Eines der folgenden Snapshot-fähigen Felder geändert wird:
  - Name
  - Aktionen (einschließlich Änderungen des Nachrichteninhalts innerhalb von Nachrichtenvarianten)

{% alert important %}
Das Speichern des Entwurfs nach dem Start löst nicht automatisch ein Update aus. Das Update wird nur dann getriggert, wenn Sie das Canvas starten oder die nach dem Start vorgenommenen Änderungen am Entwurf auf das aktive Canvas anwenden.
{% endalert %}

### SNAPSHOTS_CANVAS_FLOW_STEP_SHARED

Eine Zeile wird zu `SNAPSHOTS_CANVAS_FLOW_STEP_SHARED` hinzugefügt, wenn:
- Das Canvas gestartet wird, ODER
- Das aktive Canvas aktualisiert wird (Entwurf nach dem Start angewendet), ODER
- Eines der folgenden Snapshot-fähigen Felder geändert wird:
  - Name

{% alert important %}
Das Speichern des Entwurfs nach dem Start löst nicht automatisch ein Update aus. Das Update wird nur dann getriggert, wenn Sie das Canvas starten oder die nach dem Start vorgenommenen Änderungen am Entwurf auf das aktive Canvas anwenden.
{% endalert %}

## Einhaltung der Datenschutz-Grundverordnung (DSGVO) {#general-data-protection-regulation-gdpr-compliance}

{% multi_lang_include partners/snowflake_pii_gdpr.md %}