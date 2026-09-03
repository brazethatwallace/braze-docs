---
nav_title: API-Nutzungswarnungen
article_title: API-Nutzungswarnungen
description: "Dieser Artikel bietet eine Übersicht über die API-Nutzungswarnungen, mit denen Sie unerwarteten Datenverkehr proaktiv erkennen können."
page_order: 0
---

# API-Nutzungswarnungen {#api-usage-alerts}

> API-Nutzungswarnungen bieten wichtige Einblicke in Ihre API-Nutzung und ermöglichen es Ihnen, unerwarteten Datenverkehr proaktiv zu erkennen. Durch die Einrichtung dieser Warnungen zum Tracking wichtiger API-Anfragevolumina können Sie Realtime-Benachrichtigungen erhalten und Probleme beheben, bevor sie sich auf Ihre Marketing-Kampagnen auswirken.

## Informationen zu API-Nutzungswarnungen {#about-api-usage-alerts}

Sie können API-Nutzungswarnungen verwenden, um Anfragevolumen für die folgenden Kategorien zu überwachen:

| API-Kategorie | Details |
|--------------|---------|
| REST API-Endpunkte | Verfolgt die Nutzung aller REST API-Aufrufe an das Braze-Backend, wie z. B. das Senden von Nachrichten, das Erstellen von Campaigns oder das Exportieren von Nutzer:innen. |
| SDK-API-Anfragen | Verfolgt API-Anfragen, die von Braze SDKs in Client-Apps gestellt werden, wie z. B. das Triggern von In-App-Nachrichten oder das Synchronisieren von Nutzerdaten.<br><br>_*Nur für Kund:innen verfügbar, die „Monthly Active Users – CY 24-25“ erworben haben._ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Informationen zu API-Nutzungswarnungen" }

## Erstellen einer API-Nutzungswarnung {#creating-an-api-usage-alert}

So erstellen Sie eine API-Nutzungswarnung:

1. Navigieren Sie zu **Einstellungen** > **APIs und Bezeichner** > **API-Nutzungswarnungen** und erstellen Sie dann eine neue Warnung.
2. Geben Sie einen Namen für Ihre Warnung ein und wählen Sie die REST API-Endpunkte und API-Schlüssel aus, für die Sie benachrichtigt werden möchten.
3. Definieren Sie Ihre Warnungskriterien, indem Sie einen oder mehrere Antwortcodes auswählen und die [Warnungsschwellenwerte](#api-usage-alert-thresholds) festlegen.
4. Wenn Sie fertig sind, schalten Sie **Alert enabled** um.
    ![Ein Beispiel für eine API-Nutzungswarnung, die Benachrichtigungen sendet, wenn der Track-Users-Endpunkt innerhalb einer Stunde um 100 Prozent ansteigt.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts1.png %})

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

## Benachrichtigungen für Warnmeldungen einrichten {#setting-up-alert-notifications}

Sie können eine E-Mail-Benachrichtigung, eine Webhook-Benachrichtigung oder beides einrichten. Webhook-Benachrichtigungen können für Anwendungsfälle wie das Senden einer Warnmeldung an externe Plattformen, z. B. einen Slack-Kanal, sehr nützlich sein. Ein Beispiel finden Sie in unserer [Dokumentation]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences) zur Integration von Warnmeldungen mit Slack für unsere Benachrichtigungseinstellungen.

![Eine E-Mail wird an die ausgewählte E-Mail-Adresse gesendet, wenn die Kriterien für die Warnmeldung erreicht sind.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts2.png %})

### Beispiel-Payload {#payload}

Das Folgende ist ein Beispiel-Payload für den Body eines API-Nutzungswarnungs-Webhooks.

```json
{
  "text": "Your My First API Usage Alert alert has triggered. Please note that this alert is reset every 8 hours, and only one notification will be sent per reset period. You can view your alert and usage here: <link>.",
  "data": {
    "alert_name": "My First API Usage Alert",
    "alert_type": "API Usage Alert",
    "app_group_name": "My Workspace",
    "alert_criteria": {
      "response_codes": "201, 202 and 203",
      "threshold_condition": "increase by",
      "threshold_volume": "50%",
      "within": "1 hour"
    },
    "timeframe_start": "2025-03-20 15:35:00",
    "timeframe_end": "2025-03-20 16:35:00",
    "volume": 1500,
    "previous_timeframe_start": "2025-03-20 14:35:00",
    "previous_timeframe_end": "2025-03-20 15:35:00",
    "previous_volume": 1000
  }
}
```

{% alert note %}
Die Felder `previous_timeframe_start`, `previous_timeframe_end` und `previous_volume` sind optional und erscheinen nur, wenn die Warnmeldung eine vergleichende Schwellenwertbedingung (`increase by`, `decrease by`) verwendet. Bei Warnmeldungen mit `greater than or equal` oder `less than or equal` werden diese Felder weggelassen.
{% endalert %}

#### Details zu den Payload-Feldern {#payload-field-details}

| Feld | Typ | Beschreibung |
|------|-----|-------------|
| `text` | String | Lesbare Warnmeldung. |
| `data.alert_name` | String | Name der Warnmeldung. |
| `data.alert_type` | String | Typ der Warnmeldung (immer `"API Usage Alert"`). |
| `data.app_group_name` | String | Workspace-Name. |
| `data.alert_criteria.response_codes` | String | Für die Warnmeldung ausgewählte Antwortcodes. Gibt `"all response codes"` zurück, wenn keiner ausgewählt ist, einen einzelnen Code wie `"201"` oder mehrere Codes wie `"201, 202 and 203"`. |
| `data.alert_criteria.threshold_condition` | String | Bedingungstyp: `"increase by"`, `"decrease by"`, `"greater than or equal"` oder `"less than or equal"`. |
| `data.alert_criteria.threshold_volume` | String oder Zahl | Schwellenwert. Wenn die Bedingung einen Prozentwert verwendet, ist dies ein String mit `%` am Ende (z. B. `"50%"`). Wenn die Bedingung einen numerischen Wert verwendet, ist dies eine Zahl (z. B. `50`). |
| `data.alert_criteria.within` | String | Zeitfenster für die Auswertung der Warnmeldung (z. B. `"1 day"`). |
| `data.timeframe_start` | String | Beginn des Warnmeldungszeitraums im UTC-Format `YYYY-MM-DD HH:MM:SS`. |
| `data.timeframe_end` | String | Ende des Warnmeldungszeitraums im UTC-Format `YYYY-MM-DD HH:MM:SS`. |
| `data.volume` | Zahl | Anfragevolumen während des Warnmeldungszeitraums. |
| `data.previous_timeframe_start` | String | (Optional) Beginn des vorherigen Zeitraums. Nur bei vergleichenden Schwellenwertbedingungen vorhanden. |
| `data.previous_timeframe_end` | String | (Optional) Ende des vorherigen Zeitraums. Nur bei vergleichenden Schwellenwertbedingungen vorhanden. |
| `data.previous_volume` | Zahl | (Optional) Anfragevolumen während des vorherigen Zeitraums. Nur bei vergleichenden Schwellenwertbedingungen vorhanden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Details zu den Payload-Feldern" }

### Beispielwarnmeldungen {#example-alerts}

Hier sind einige Möglichkeiten, wie Sie Ihre API-Nutzungswarnungskonfigurationen einrichten können, um in den folgenden Szenarien benachrichtigt zu werden.

{% tabs local %}
{% tab API-Gesundheit %}
Sie können Warnmeldungen einrichten, um den allgemeinen Zustand Ihrer API zu überwachen. Zum Beispiel können Sie diese Warnmeldungen einrichten, wenn API-Fehler drastisch ansteigen, z. B. um 20 % gegenüber der vorherigen Stunde.

| Endpunkt | API-Schlüssel | Antwortcode | Schwellenwertbedingung | Schwellenwert | Innerhalb |
| --- | --- | --- | --- | --- | --- |
| Alle Endpunkte | Alle API-Schlüssel | `4XX` und `5XX` | Um 10 % gestiegen | 10 | 1 Stunde |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Beispielwarnmeldungen" }
{% endtab %}

{% tab Endpunkt-Rate-Limit %}
Lassen Sie sich benachrichtigen, wenn Ihr Workspace das Rate-Limit für den Endpunkt `/users/track` erreicht. Sie können diese Konfiguration auch auf andere Braze-Endpunkte anwenden.

| Endpunkt | API-Schlüssel | Antwortcode | Schwellenwertbedingung | Schwellenwert | Innerhalb |
| --- | --- | --- | --- | --- | --- |
| `/users/track` | Alle API-Schlüssel | `429` | Größer als oder gleich | 100 | 1 Stunde |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Beispielwarnmeldungen" }
{% endtab %}

{% tab API-getriggerte Campaigns %}
Diese Warnmeldungskonfiguration benachrichtigt Sie, wenn Fehler bei API-getriggerten Campaigns und Canvases auftreten, von denen einige eine hohe Priorität haben können.

| Endpunkt | API-Schlüssel | Antwortcode | Schwellenwertbedingung | Schwellenwert | Innerhalb |
| --- | --- | --- | --- | --- | --- |
| {::nomarkdown}<ul><li><code>/campaigns/trigger/send</code></li><li><code>/canvas/trigger/send</code></li><li><code>/messages/send</code></li></ul>{:/} | Alle API-Schlüssel | `4XX` und `5XX` | Größer als oder gleich | 1 | 1 Stunde |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Beispielwarnmeldungen" }
{% endtab %}

{% tab Partnerintegrationen %}
Verwenden Sie die folgende Warnmeldungskonfiguration, um benachrichtigt zu werden, wenn eine Partnerintegration aufhört, Daten an Braze zu senden.

| Endpunkt | API-Schlüssel | Antwortcode | Schwellenwertbedingung | Schwellenwert | Innerhalb |
| --- | --- | --- | --- | --- | --- |
| Alle Endpunkte | Der für Ihre Partnerintegration verwendete API-Schlüssel | Alle Antwortcodes | Kleiner als oder gleich | 0 | 1 Tag |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Beispielwarnmeldungen" }
{% endtab %}
{% endtabs %}

## Überlegungen {#considerations}

- Jede aktive Warnung sendet nur alle 8 Stunden eine E-Mail- oder Webhook-Benachrichtigung. Dies soll verhindern, dass eine einzelne Warnung zu viele Benachrichtigungen auslöst. Wenn Ihre Warnung Sie zu früh benachrichtigt, sollten Sie die Warnungskriterien bearbeiten, um sie besser an Ihren Anwendungsfall anzupassen.
- Sie können bis zu 10 Warnungen pro Workspace haben.