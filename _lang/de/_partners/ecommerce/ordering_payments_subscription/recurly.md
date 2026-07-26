---
nav_title: Recurly
article_title: Recurly
description: "Recurly ist die führende Plattform für Abo-Management und Rechnungsstellung für Marken im Direktvertrieb an Verbraucher:innen, die ihre Abos und wiederkehrenden Einnahmen steigern möchten."
alias: /partners/recurly/
page_type: partner
search_tag: partner
---

# Recurly

> [Recurly](https://recurly.com/) ist eine Plattform für Abo-Management und Rechnungsstellung. Die integrierte Plattform von Recurly vereinfacht die Automatisierung des Abo-Lebenszyklus in großem Umfang, indem sie Teams in die Lage versetzt, das Abo-Erlebnis zu verwalten und zu optimieren – vom Testen neuer Pläne, Angebote und Aktionen bis hin zur Verwaltung von Zahlungsarten, Integrationen und Insights.

_Diese Integration wird von Recurly gepflegt._

## Über die Integration {#about-the-integration}

Die Integration zwischen Recurly und Braze vereinfacht den Austausch von Abo-Daten mit Braze und ermöglicht so eine gezielte Kommunikation mit Kund:innen.

- Nutzen Sie Recurly-Abo-Lebenszyklus-Events (z. B. Abo-Verlängerungen, Pausen oder Kündigungen) in Braze, um personalisierte Campaigns und Mitteilungen zu triggern.
- Nutzen Sie Recurly-Abo-Daten (z. B. Abo-Pläne, Add-Ons oder Status), um Unternehmensnutzer:innen, Segmente und Canvases zu erstellen und zu verwalten und kohortenspezifische Campaigns und Mitteilungen durchzuführen.
- Senden Sie Recurly-Daten direkt an Braze, um zusätzliche Messaging-Anwendungsfälle zu ermöglichen und die Entwicklungskosten zu senken.

Weitere Einzelheiten zur Verwendung von Recurly mit Braze finden Sie in den [Recurly Docs](https://docs.recurly.com/docs/braze-integration).

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Recurly-Konto | Sie benötigen ein Elite-[Recurly](https://recurly.com/)-Abo mit aktiviertem Braze-Feature-Flag, um die Vorteile dieser Partnerschaft zu nutzen. Die Aktivierung von Kreditrechnungen in Ihrer Recurly-Plattform ist ebenfalls erforderlich. |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit `users.track`-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. Da Recurly nur den Endpunkt `users.track` verwendet, empfehlen wir, einen Recurly-spezifischen Schlüssel nur mit dieser Berechtigung bereitzustellen. |
| Braze-REST-Endpunkt | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

Bevor Sie beginnen, vergewissern Sie sich, dass Sie sowohl bei Braze als auch bei Recurly ein aktives Konto haben.

### Recurly mit Braze verbinden {#connect-recurly-to-braze}

1. Gehen Sie in Recurly zu **Integrations** > **Braze**. Wenn Sie zum ersten Mal zur Konfigurationsseite für die Braze-Integration in Recurly navigieren, werden Sie von der Schnittstelle aufgefordert, die beiden Systeme miteinander zu verbinden.

2. Geben Sie die folgenden Zugangsdaten an:

- **Instance URL:** Der Braze-REST-Endpunkt der Instanz, für die Sie bereitgestellt werden.
- **API Key (Identifier):** Der Braze-REST-API-Schlüssel, den Recurly beim Senden von Anfragen an Braze verwenden soll.

Denken Sie daran, die URL Ihrer Braze-Instanz zu kopieren. Ihre URL könnte zum Beispiel so aussehen:

```
<https://dashboard-03.braze.com/dashboard/app_usage?locale=en>
```

{:start="3"}
3. Nachdem Sie Ihre Zugangsdaten eingegeben haben, klicken Sie auf **Connect**.

## Verwendung dieser Integration {#using-this-integration}

### Unterstützte Bezeichner {#supported-identifiers}

Recurly verwendet den `account_code` eines Kontos als `external_id` in Braze. Aus diesem Grund sollte der `account_code` Ihrer Recurly-Konten mit der `external_id` Ihrer Braze-Nutzer:innen übereinstimmen.

### Angepasste Events {#custom-events}

Für ein effektives geschäftskunden-Engagement müssen Sie in Braze [angepasste Events konfigurieren]({{site.baseurl}}/user_guide/data/activation/events/custom_events/), um von Recurly getriggerte Events zu empfangen. Stellen Sie sicher, dass Sie jedes Event aus Recurly für eine gründliche Datenintegration einbeziehen. Diese Events können auch in [Braze Analytics]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#analytics) getrackt werden. Einmal konfiguriert, können diese angepassten Events zur Segmentierung von Nutzer:innen oder zur Personalisierung von Nachrichten verwendet werden.

| Angepasstes Braze-Event | Recurly-Event |
| ----------- | ----------- |
| Recurly New Subscription              | Wird getriggert, wenn ein Abo erstellt wird                            |
| Recurly Renewed Subscription          | Wird getriggert, wenn ein Abo verlängert wird                                |
| Recurly Updated Subscription          | Wird getriggert, wenn sich die Attribute eines Abos ändern (Planänderung, Preisänderung oder Mengenänderung) |
| Recurly Canceled Subscription         | Wird getriggert, wenn ein Abo gekündigt wird                           |
| Recurly Reactivated Subscription      | Wird getriggert, wenn ein gekündigtes Abo reaktiviert wird               |
| Recurly Paused Subscription           | Wird getriggert, wenn ein Abo pausiert werden soll                   |
| Recurly Resumed Subscription          | Wird getriggert, wenn ein Abo wieder aufgenommen wird                              |
| Recurly Subscription Expired          | Wird getriggert, wenn ein Abo ausläuft                               |
| Recurly Invoice Created               | Wird getriggert, wenn eine Rechnung erstellt wird                                |
| Recurly Successful Payment            | Wird getriggert, wenn eine Rechnung erfolgreich eingezogen wird                 |
| Recurly Refund Issued                 | Wird getriggert, wenn eine Erstattung ausgestellt wird                                   |
| Recurly Failed Recurring Payment      | Wird getriggert, wenn eine Rechnung für eine Abo-Verlängerung fehlschlägt          |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom events" }

### Batching und Rate-Limiting {#batching-and-rate-limiting}

Da Recurly den Braze-Endpunkt `/users/track` verwendet, unterliegt die Integration den standardmäßigen Braze-Rate-Limits von 50.000 Anfragen pro Minute.

Recurly fasst bestimmte Abo-Lebenszyklus-Events in einzelnen API-Aufrufen an Braze zusammen, um die Anzahl der Anfragen zu reduzieren.

- Recurly bündelt und versendet mehrere gleichzeitig erstellte Abos in einer einzigen Anfrage.
- Recurly fasst mehrere gleichzeitige Verlängerungen für ein Konto in einer einzigen Anfrage zusammen.
- Recurly sendet Abo-Lebenszyklus-Events desselben Modells in einer einzigen Anfrage. Eine neu erstellte Rechnung mit einer Zahlung führt beispielsweise zu einer API-Anfrage, die sowohl das angepasste Event `Recurly Invoice Created` als auch `Recurly Successful Payment` enthält.

Batches werden in Gruppen von bis zu 75 Events auf einmal an Braze gesendet. Wenn zum Beispiel 100 Abos auf einmal erstellt werden, würde Recurly zwei API-Anfragen an Braze stellen. Weitere Informationen finden Sie unter [Batching von User-Track-Anfragen]({{site.baseurl}}/api/api_limits/#batch-user-track).