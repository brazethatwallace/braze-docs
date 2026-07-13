---
nav_title: Datadog
article_title: Datadog
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Datadog, einem Observability-Dienst für Cloud-basierte Anwendungen, der die Überwachung von Servern, Datenbanken, Tools und Diensten über eine SaaS-basierte Analytics-Plattform ermöglicht."
alias: /partners/datadog/
page_type: partner
search_tag: Partner


---

# Datadog

> [Datadog](https://www.datadoghq.com/) ist ein Observability-Dienst für Anwendungen im Cloud-Maßstab, der die Überwachung von Servern, Datenbanken, Tools und Diensten über eine SaaS-basierte Analytics-Plattform ermöglicht.

Die Integration von Braze und Datadog ermöglicht es Kund:innen, Braze-Daten in Datadog zu erfassen und Warnmeldungen zu den gesendeten Daten zu erstellen. Sie können beispielsweise eine Überwachung und einen Alarm einrichten, wenn Ihre wöchentliche Newsletter-Campaign ein ungewöhnlich niedriges Nachrichtenvolumen versendet oder wenn ein Canvas-Schritt, der normalerweise nur wenige Nachrichten pro Tag versendet, plötzlich Tausende versendet.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Datadog-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, ist ein Datadog-Konto erforderlich. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### Schritt 1: Datadog-Schlüssel generieren {#step-1-generate-datadog-key}

In Datadog müssen Sie einen [API-Schlüssel](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys) erstellen. Um einen API-Schlüssel hinzuzufügen, navigieren Sie zu **Organization Settings** > **API Keys** > **New Key**.

### Schritt 2: Schlüssel zu Braze hinzufügen {#step-2-add-key-to-braze}

Navigieren Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologie-Partner** und suchen Sie dann nach **Datadog**. Geben Sie auf der Datadog-Partnerseite den Datadog-API-Schlüssel an. Dadurch wird eine Verbindung hergestellt, die es Braze erlaubt, Daten an Datadog zu senden.

## Braze-Ereignisse {#braze-events}

Nach der Integration der Verbindung sendet Braze die folgenden Ereignisse an Datadog:

- `braze.messaging.sent` – Die Anzahl der Sendungen

Jedes dieser Ereignisse enthält Metadaten in Form von Datadog-Tags, die Ihnen Informationen wie die folgenden liefern:

- `app_group_id`
- `app_group_name`
- `campaign_id` / `campaign_name` (falls verfügbar)
- `canvas_id` / `canvas_name` / `canvas_step_id` / `canvas_step_name` (falls verfügbar)

Diese Ereignisse und Tags können auf der Datadog-Seite **Metrics Explorer** überwacht werden. Diese Metriken werden als [Verteilungen](https://docs.datadoghq.com/metrics/distributions/) an Datadog protokolliert. Aufgrund der Natur der Metriken und der Ungenauigkeit der Aggregationen und Rollups von Datadog unternimmt Braze keine erneuten Versuche bei vorübergehenden Netzwerkfehlern oder anderen Datadog-API-Fehlern, die während der Übertragung auftreten können. Das bedeutet, dass die Zählungen dieser Metriken geringfügig von den Zählungen im Braze-Dashboard und/oder über Currents abweichen können.

![Datadog Metrics Explorer mit Braze-Ereignismetriken und Tags.]({% image_buster /assets/img/datadog.png %})