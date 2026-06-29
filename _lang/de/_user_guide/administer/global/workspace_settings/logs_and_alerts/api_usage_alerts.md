---
nav_title: API-Nutzungswarnungen
article_title: API-Nutzungswarnungen
description: "Dieser Artikel bietet eine Übersicht über die API-Nutzungswarnungen, mit denen Sie unerwarteten Datenverkehr proaktiv erkennen können."
page_order: 0
---

# API-Nutzungswarnungen {#api-usage-alerts}

> API-Nutzungswarnungen bieten wichtige Einblicke in Ihre API-Nutzung und ermöglichen es Ihnen, unerwarteten Datenverkehr proaktiv zu erkennen. Durch die Einrichtung dieser Warnungen zum Tracking wichtiger API-Anfragevolumina können Sie Realtime-Benachrichtigungen erhalten und Probleme beheben, bevor sie sich auf Ihre Marketing-Kampagnen auswirken.

## Informationen zu API-Nutzungswarnungen {#about-api-usage-alerts}

Sie können API-Nutzungswarnungen verwenden, um das Volumen der Anfragen für die folgenden Kategorien zu überwachen:

| API-Kategorie | Details |
|--------------|---------|
| REST API-Endpunkte | Verfolgt die Nutzung aller REST API-Aufrufe, die an das Backend von Braze gesendet werden, wie beispielsweise das Versenden von Nachrichten, das Erstellen von Campaigns oder das Exportieren von Nutzer:innen. |
| SDK-API-Anfragen | Verfolgt API-Anfragen, die von Braze-SDKs in Client-Apps gestellt werden, wie beispielsweise das Triggern von In-App-Nachrichten oder die Synchronisierung von Nutzerdaten.<br><br>_*Nur für Kund:innen verfügbar, die „Monatlich aktive:r Nutzer:in – CY 24-25“ erworben haben._ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Informationen zu API-Nutzungswarnungen" }

## Erstellen einer API-Nutzungswarnung {#creating-an-api-usage-alert}

Um eine API-Nutzungswarnung zu erstellen:

1. Gehen Sie zu **Einstellungen** > **APIs und Bezeichner** > **API Usage Alerts** und erstellen Sie eine neue Warnung.
2. Geben Sie einen Namen für Ihre Warnung ein und wählen Sie die REST API-Endpunkte und API-Schlüssel aus, für die Sie benachrichtigt werden möchten.
3. Definieren Sie Ihre Warnungskriterien, indem Sie einen oder mehrere Antwortcodes auswählen und die [Schwellenwerte für Warnungen](#api-usage-alert-thresholds) festlegen.
4. Wenn Sie fertig sind, schalten Sie **Alert enabled** um.
    ![Ein Beispiel für eine API-Nutzungswarnung, die Benachrichtigungen sendet, wenn der Endpunkt „Track users“ innerhalb einer Stunde um 100 Prozent ansteigt.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts1.png %})

## Schwellenwerte für Warnungen {#api-usage-alert-thresholds}

Wenn Sie Ihre Warnungskriterien definieren, können Sie die folgenden Schwellenwerte anpassen:

<table aria-label="Schwellenwerte für Warnungen">
  <caption>Schwellenwerte für Warnungen</caption>
  <thead>
    <tr>
      <th>Feld</th>
      <th>Beschreibung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Schwellenwertbedingung</td>
      <td>
        Definiert die Bedingungen, die zum Schwellenwertvolumen führen, bei dem Sie benachrichtigt werden möchten. Folgende Optionen werden unterstützt:<br><br>
        <ul>
          <li><strong>Increased by</strong> oder <strong>Decreased by</strong>: Vergleicht Anfragen mit dem vorherigen Zeitfenster.</li>
          <li><strong>Increased by percentage</strong> oder <strong>Decreased by percentage</strong>: Vergleicht die prozentuale Änderung der Anfragen mit dem vorherigen Zeitfenster.</li>
          <li><strong>Greater than or equal</strong> oder <strong>less than or equal</strong>: Zählt Anfragen in einem Zeitfenster.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Schwellenwertvolumen</td>
      <td>Wird in Verbindung mit der Schwellenwertbedingung verwendet.</td>
    </tr>
    <tr>
      <td>Innerhalb</td>
      <td>Das Zeitfenster für die Auswertung der Warnung.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schwellenwerte für Warnungen" }

## Einrichten von Warnungsbenachrichtigungen {#setting-up-alert-notifications}

Sie können eine E-Mail-Warnung, eine Webhook-Warnung oder beides einrichten. Webhook-Warnungen können für Anwendungsfälle wie das Senden einer Warnung an externe Plattformen, z. B. einen Slack-Kanal, sehr nützlich sein. Ein Beispiel finden Sie in unserer [Dokumentation]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences/#slack-incoming-webhook-integration) zur Integration von Warnungen mit Slack für unsere Benachrichtigungspräferenzen.

![Eine E-Mail wird an die ausgewählte E-Mail-Adresse gesendet, wenn die Kriterien für die Warnung erreicht werden.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts2.png %})

### Beispiel-Payload {#payload}

Das Folgende ist ein Beispiel-Payload für den Body eines API-Nutzungswarnungs-Webhooks.

```json
{
  "data": {
    "alert_name": "My First API Usage Alert",
    "alert_type": "API Usage Alert",
    "alert_criteria": {
    	"response_codes": ["201", "202", "203"],
    	"threshold_condition": "Increased by %",
    	"threshold_volume": 50,
    	"within": "1 day"
    },
    "timeframe_start": "2025-03-20T15:35:00Z",
    "timeframe_end": "2025-03-20T16:35:00Z",
    "volume": 1500,
    "previous_timeframe_start": "2025-03-20T14:35:00Z",
    "previous_timeframe_end": "2025-03-20T15:35:00Z",
    "previous_volume": 1000
  },
  "text": "Your My First API Usage Alert alert has triggered. You can view your alert and usage here: <link>. Note that this alert will reset in 1 day, as each alert will only send one notification per 8 hours."
}
```

### Beispielwarnungen {#example-alerts}

Hier sind einige Möglichkeiten, wie Sie Ihre API-Nutzungswarnungen konfigurieren können, um in den folgenden Szenarien benachrichtigt zu werden.

{% tabs local %}
{% tab API-Zustand %}
Sie können Warnungen einrichten, um den allgemeinen Zustand Ihrer API zu überwachen. Zum Beispiel können Sie diese Warnungen einrichten, wenn API-Fehler drastisch ansteigen, z. B. um 20 % gegenüber der vorherigen Stunde.

| Endpunkt | API-Schlüssel | Antwortcode | Schwellenwertbedingung | Schwellenwertvolumen | Innerhalb |
| --- | --- | --- | --- | --- | --- |
| Alle Endpunkte | Alle API-Schlüssel | `4XX` und `5XX` | Increased by 10 % | 10 | 1 Stunde |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Beispielwarnungen" }
{% endtab %}

{% tab Endpunkt-Rate-Limit %}
Lassen Sie sich benachrichtigen, wenn Ihr Workspace das Rate-Limit für den Endpunkt `/users/track` erreicht. Sie können diese Konfiguration auch für andere Braze-Endpunkte anwenden.

| Endpunkt | API-Schlüssel | Antwortcode | Schwellenwertbedingung | Schwellenwertvolumen | Innerhalb |
| --- | --- | --- | --- | --- | --- |
| `/users/track` | Alle API-Schlüssel | `429` | Greater than or equal | 100 | 1 Stunde |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Beispielwarnungen" }
{% endtab %}

{% tab API-getriggerte Campaigns %}
Diese Warnungskonfiguration benachrichtigt Sie, wenn Fehler bei API-getriggerten Campaigns und Canvases auftreten, von denen einige möglicherweise eine hohe Priorität haben.

| Endpunkt | API-Schlüssel | Antwortcode | Schwellenwertbedingung | Schwellenwertvolumen | Innerhalb |
| --- | --- | --- | --- | --- | --- |
| {::nomarkdown}<ul><li><code>/campaigns/trigger/send</code></li><li><code>/canvas/trigger/send</code></li><li><code>/messages/send</code></li></ul>{:/} | Alle API-Schlüssel | `4XX` und `5XX` | Greater than or equal | 1 | 1 Stunde |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Beispielwarnungen" }
{% endtab %}

{% tab Partnerintegrationen %}
Verwenden Sie die folgende Warnungskonfiguration, um benachrichtigt zu werden, wenn eine Partnerintegration keine Daten mehr an Braze sendet.

| Endpunkt | API-Schlüssel | Antwortcode | Schwellenwertbedingung | Schwellenwertvolumen | Innerhalb |
| --- | --- | --- | --- | --- | --- |
| Alle Endpunkte | Der API-Schlüssel, der für Ihre Partnerintegration verwendet wird | Alle Antwortcodes | Less than or equal | 0 | 1 Tag |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Beispielwarnungen" }
{% endtab %}
{% endtabs %}

## Hinweise {#considerations}

- Jede aktive Warnung sendet nur alle 8 Stunden eine E-Mail- oder Webhook-Benachrichtigung. Dies dient dazu, zu viele Benachrichtigungen von einer einzelnen Warnung zu vermeiden. Wenn Ihre Warnung Sie zu früh benachrichtigt, sollten Sie die Warnungskriterien bearbeiten, um sie besser an Ihren Anwendungsfall anzupassen.
- Sie können bis zu 10 Warnungen pro Workspace einrichten.