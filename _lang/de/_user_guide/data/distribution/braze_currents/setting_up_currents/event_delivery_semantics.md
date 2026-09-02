---
nav_title: Semantik der Zustellung von Events
article_title: Semantik der Zustellung von Events
page_order: 2
page_type: reference
description: "In diesem Referenzartikel wird erläutert und definiert, wie Currents die von uns an Data Warehouse-Speicherpartner gesendeten Flat-File-Event-Daten verwaltet."
tool: Currents

---

# Semantik der Zustellung von Events {#event-delivery-semantics}

> Auf dieser Seite wird beschrieben und definiert, wie Currents die Flat-File-Event-Daten verwaltet, die wir an Data Warehouse-Speicherpartner senden.

„Currents für Datenspeicher“ ist ein kontinuierlicher Datenstrom von unserer Plattform zu einem Speicher-Bucket auf einer unserer Data Warehouse-[Partnerverbindungen]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners). Currents schreibt Avro-Dateien in regelmäßigen Abständen in Ihren Speicher-Bucket, sodass Sie die Event-Daten mit Ihrem eigenen Business-Intelligence-Toolset (BI) verarbeiten und analysieren können.

{% alert important %}
Dieser Inhalt **gilt nur für die Flat-File-Event-Daten, die wir an Data Warehouse-Speicherpartner (Google Cloud Storage, Amazon S3 und Microsoft Azure Blob Storage) senden**. <br><br>Inhalte, die für andere Partner gelten, finden Sie in unserer Liste der [verfügbaren Partner]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) und auf den jeweiligen Seiten.
{% endalert %}

## Test-Events {#test-events}

Wenn Sie eine Currents-Integration einrichten, klicken Sie auf **Test-Events senden**, um die Verbindung mit Ihrem Speicher-Bucket zu überprüfen. Diese Test-Events bestätigen, dass Ihre Integration Daten korrekt empfangen und verarbeiten kann.

{% alert important %}
**Datenformat von Test-Events:** Test-Events enthalten Platzhalterwerte, die den korrekten Datentypen für jedes Feld entsprechen, jedoch keine realistischen oder genauen Daten enthalten. Beispielsweise kann ein `timezone`-Feld einen UUID-ähnlichen String anstelle eines gültigen Zeitzonen-Bezeichners (wie „America/Chicago“) enthalten, und andere Felder wie `campaign_name` und `ip_pool` können ebenfalls Platzhalterwerte anstelle tatsächlicher Daten enthalten.<br>

Dies ist das erwartete Verhalten. Test-Events dienen in erster Linie zum Testen der Verbindung und des Integrations-Setups, nicht zur Validierung der Datengenauigkeit. Um echte Events mit genauen Daten zu sehen, verwenden Sie eine Test-Currents-Integration, um tatsächliche Event-Daten durch Ihre Pipeline zu senden.
{% endalert %}

## „At-least-once“-Zustellung {#at-least-once-delivery}

Als Hochdurchsatzsystem bietet Currents eine „At-least-once“-Zustellung von Events, was bedeutet, dass gelegentlich doppelte Events in Ihren Speicher-Bucket geschrieben werden können. Dies kann passieren, wenn Events aus unserer Warteschlange aus irgendeinem Grund erneut verarbeitet werden.

Wenn Ihre Anwendungsfälle eine „Exactly-once“-Zustellung erfordern, können Sie das eindeutige Bezeichnerfeld, das mit jedem Event gesendet wird (`id`), zur Deduplizierung von Events verwenden. Da die Datei unserer Kontrolle entgeht, sobald sie in Ihren Speicher-Bucket geschrieben wird, können wir keine Deduplizierung von unserer Seite garantieren.

## Zeitstempel {#timestamps}

Alle von Currents exportierten Zeitstempel werden in der UTC-Zeitzone gesendet. Für einige Events, bei denen es verfügbar ist, wird auch ein Zeitzonen-Feld mitgeliefert, das die Ortszeit der Nutzer:innen zum Zeitpunkt des Events im IANA-Format (Internet Assigned Numbers Authority) enthält.

### Latenz {#latency}

Events, die über SDK or Software-Development-Kit oder API an Braze gesendet werden, können einen Zeitstempel aus der Vergangenheit enthalten. Das häufigste Beispiel ist, wenn SDK or Software-Development-Kit-Daten in eine Warteschlange gestellt werden, etwa wenn keine mobile Konnektivität besteht. In diesem Fall spiegelt der Event-Zeitstempel wider, wann das Event generiert wurde. Das bedeutet, dass ein gewisser Prozentsatz der Events eine hohe Latenz aufweisen wird.

## Apache-Avro-Format {#apache-avro-format}

Die Braze-Currents-Datenspeicher-Integrationen geben Daten im `.avro`-Format aus. Wir haben [Apache Avro](https://avro.apache.org/) gewählt, weil es ein flexibles Datenformat ist, das nativ Schema-Evolution unterstützt und von einer Vielzahl von Datenprodukten unterstützt wird:

- Avro wird von nahezu jedem großen Data Warehouse unterstützt.
- Falls Sie Ihre Daten in S3 belassen möchten, komprimiert Avro besser als CSV und JSON, sodass Sie weniger für Speicher bezahlen und potenziell weniger CPU zum Parsen der Daten benötigen.
- Avro erfordert Schemas beim Schreiben oder Lesen von Daten. Schemas können im Laufe der Zeit weiterentwickelt werden, um das Hinzufügen von Feldern zu handhaben, ohne dass etwas kaputtgeht.

Currents erstellt für jeden Event-Typ eine Datei im folgenden Format:

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>/event_type=<event-type>/date=<date>/version=<currents_version>/<environment>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>+<partition>+<offset>.avro
```

{% alert tip %}
Sie können den Code wegen der Scrollleiste nicht sehen? Erfahren Sie [auf der Startseite des Braze-Benutzerhandbuchs]({{site.baseurl}}/user_guide), wie Sie das beheben können.
{% endalert %}

Beispielsweise kann ein Pfad für ein Push-Sende-Event so aussehen:

```
currents-export/dataexport.prod-01.S3.integration.69cadaaed2d51b7c75b1a3e5/event_type=users.messages.pushnotification.Send/date=2025-04-01-17/version=6/us-01/dataexport.prod-01.S3.integration.69cadaaed2d51b7c75b1a3e5+0+123456.avro
```

Das Pfadsegment `version` ist ein einfacher ganzzahliger Currents-Versionswert, z. B. `version=6`.

| Dateinamensegment | Definition |
|---|---|
| `<your-bucket-prefix>` | Das für diese Currents-Integration festgelegte Präfix. |
| `<cluster-identifier>` | Für den internen Gebrauch durch Braze. Ist ein String wie „prod-01“, „prod-02“, „prod-03“ oder „prod-04“. Alle Dateien haben denselben Cluster-Bezeichner. |
| `<connection-type-identifier>` | Der Bezeichner für den Verbindungstyp. Optionen sind „S3“, „AzureBlob“ oder „GCS“. |
| `<integration-id>` | Die eindeutige ID für diese Currents-Integration. |
| `<event-type>` | Der Typ des Events in der Datei. |
| `<date>` | Die Stunde, in der Events in unserem System zur Verarbeitung in der UTC-Zeitzone in die Warteschlange gestellt werden. Format: JJJJ-MM-TT-HH. |
| `version=<currents_version>` | Die Currents-Version für den Pipeline-Pfad. Dieser Wert ist eine einfache Ganzzahl wie `6`. |
| `<environment>` | Für den internen Gebrauch durch Braze. |
| `<partition>` | Für den internen Gebrauch durch Braze. Ganzzahl. |
| `<offset>` | Für den internen Gebrauch durch Braze. Ganzzahl. Beachten Sie, dass verschiedene Dateien, die innerhalb derselben Stunde gesendet werden, einen unterschiedlichen `<offset>`-Parameter haben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Apache-Avro-Format" }

{% alert tip %}
Dateibenennungskonventionen können sich ändern. Braze empfiehlt, alle Schlüssel in Ihrem Bucket zu durchsuchen, die das Präfix &lt;your-bucket-prefix&gt; haben.
{% endalert %}

### Avro-Schreibschwellenwert {#avro-write-threshold}

Unter normalen Umständen schreibt Braze alle 5 Minuten oder alle 15.000 Events Datendateien in Ihren Speicher-Bucket – je nachdem, was zuerst eintritt. Bei hoher Last können wir größere Datendateien mit bis zu 100.000 Events pro Datei schreiben.

{% alert important %}
Currents schreibt niemals leere Dateien.
{% endalert %}

### Avro-Schema-Änderungen {#avro-schema-changes}

Von Zeit zu Zeit kann Braze Änderungen am Avro-Schema vornehmen, wenn Felder hinzugefügt, geändert oder entfernt werden. Für unsere Zwecke gibt es hier zwei Arten von Änderungen: nicht-brechende und brechende. Alle Schema-Änderungen werden in Currents-Releases gebündelt, und jedes Release erhöht das Segment `version=<currents_version>` im Speicherpfad (z. B. von `version=6` auf `version=7`). Currents-Events, die in Azure Blob Storage, Google Cloud Storage und Amazon S3 geschrieben werden, verwenden das folgende Pfadformat:

```
<your-bucket-prefix>/<currents-integration-id>/event_type=<event-type>/date=<date>/version=<currents_version>/<environment>/<avro-file>
```

#### Nicht-brechende Änderungen {#non-breaking-changes}

Wenn ein Feld zum Avro-Schema hinzugefügt wird, betrachten wir dies als nicht-brechende Änderung. Hinzugefügte Felder sind immer „optionale“ Avro-Felder (z. B. mit einem Standardwert von `null`), sodass sie gemäß der [Avro-Schema-Auflösungsspezifikation](http://avro.apache.org/docs/current/spec.html#schema+resolution) mit älteren Schemas „übereinstimmen“. Diese Ergänzungen sollten bestehende ETL or Extract, Transform, Load-Prozesse (ETL or Extract, Transform, Load or Extract, Transform, Load) nicht beeinträchtigen, da das Feld einfach ignoriert wird, bis es zu Ihrem ETL or Extract, Transform, Load-Prozess hinzugefügt wird.

{% alert important %}
Wir empfehlen, dass Ihr ETL or Extract, Transform, Load-Setup explizit die zu verarbeitenden Felder angibt, um zu vermeiden, dass der Ablauf beim Hinzufügen neuer Felder unterbrochen wird.
{% endalert %}

#### Brechende Änderungen {#breaking-changes}

Wenn ein Feld aus dem Avro-Schema entfernt oder darin geändert wird, betrachten wir dies als brechende Änderung. Brechende Änderungen können Anpassungen an bestehenden ETL or Extract, Transform, Load-Prozessen erfordern, da Felder, die zuvor verwendet wurden, möglicherweise nicht mehr wie erwartet aufgezeichnet werden.

Alle brechenden Änderungen werden vor dem Release im Voraus kommuniziert.

Eine vollständige Änderungshistorie nach Version finden Sie im [Currents-Changelog]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs).