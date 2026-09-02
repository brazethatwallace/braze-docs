---
nav_title: Datadog
article_title: Datadog
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Datadog, einem Observability-Dienst für Cloud-basierte Anwendungen, der die Überwachung von Servern, Datenbanken, Tools und Diensten über eine SaaS or Software-as-a-Service-basierte Analytics-Plattform ermöglicht."
alias: /partners/datadog/
page_type: partner
search_tag: Partner


---

# Datadog

> [Datadog](https://www.datadoghq.com/) ist ein Observability-Dienst für Anwendungen im Cloud-Maßstab, der die Überwachung von Servern, Datenbanken, Tools und Diensten über eine SaaS or Software-as-a-Service-basierte Analytics-Plattform ermöglicht.

Die Integration von Braze und Datadog ermöglicht es Kund:innen, Braze-Daten in Datadog zu erfassen und Warnmeldungen zu den gesendeten Daten zu erstellen. Sie können beispielsweise eine Überwachung und einen Alarm einrichten, wenn Ihre wöchentliche Newsletter-Campaign ein ungewöhnlich niedriges Nachrichtenvolumen versendet oder wenn ein Canvas-Schritt, der normalerweise nur wenige Nachrichten pro Tag versendet, plötzlich Tausende versendet.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Datadog-Konto | Ein Datadog-Konto ist erforderlich, um diese Partnerschaft nutzen zu können. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### Schritt 1: Datadog-Schlüssel generieren {#step-1-generate-datadog-key}

In Datadog müssen Sie einen [API-Schlüssel](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys) erstellen. Um einen API-Schlüssel hinzuzufügen, navigieren Sie zu **Organization Settings** > **API Keys** > **New Key**.

### Schritt 2: Schlüssel zu Braze hinzufügen {#step-2-add-key-to-braze}

Navigieren Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologie-Partner** und suchen Sie dann nach **Datadog**. Geben Sie auf der Datadog-Partnerseite den Datadog-API-Schlüssel an. Dadurch wird eine Verbindung hergestellt, die es Braze erlaubt, Daten an Datadog zu senden.

## Braze-Ereignisse {#braze-events}

Nachdem die Verbindung integriert ist, sendet Braze die folgenden Ereignisse an Datadog:

- `braze.messaging.sent` – Die Anzahl der Sendungen

Jedes dieser Ereignisse enthält Metadaten in Form von Datadog-Tags, die Ihnen Informationen wie die folgenden liefern:

- `app_group_id`
- `app_group_name`
- `campaign_id` / `campaign_name` (falls verfügbar)
- `canvas_id` / `canvas_name` / `canvas_step_id` / `canvas_step_name` (falls verfügbar)

Diese Ereignisse und Tags können auf der Datadog-Seite **Metrics Explorer** überwacht werden. Diese Metriken werden als [Distributions](https://docs.datadoghq.com/metrics/distributions/) in DataDog protokolliert. Aufgrund der Natur von Metriken und der Ungenauigkeit der Aggregationen und Rollups von DataDog unternimmt Braze keine Wiederholungsversuche bei vorübergehenden Netzwerkfehlern oder anderen DataDog-API-Fehlern, die während der Übertragung auftreten können. Das bedeutet, dass diese Metrikzähler geringfügig von den im Braze-Dashboard und/oder über Currents angezeigten Werten abweichen können.

![Datadog Metrics Explorer mit Braze-Ereignismetriken und Tags.]({% image_buster /assets/img/datadog.png %})

## Fehlerbehebung {#troubleshooting}

### Warum fehlen `braze.messaging.sent`-Metriken in Datadog? {#why-are-brazemessagingsent-metrics-missing-in-datadog}

Wenn Sie Braze mit Datadog verbunden haben, aber `braze.messaging.sent` im Metrics Explorer nicht sehen, überprüfen Sie, ob die in Braze ausgewählte **Datadog-Site** mit der Site-URL Ihrer Datadog-Organisation übereinstimmt. Verfügbare Sites sind:

- `datadoghq.com` (Standard)
- `us3.datadoghq.com`
- `us5.datadoghq.com`
- `datadoghq.eu`
- `ddog-gov.com`
- `ap1.datadoghq.com`

Eine nicht übereinstimmende Site kann dazu führen, dass Metriken im Workspace, in dem Sie suchen, nicht angezeigt werden. Gehen Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologie-Partner** > **Datadog** und überprüfen Sie, ob die Site mit der Subdomain in Ihrer Datadog-Konto-URL übereinstimmt.

Das Feld **Datadog-Site** ist nach dem Verbinden gesperrt. Um es zu ändern, trennen Sie die Integration und verbinden Sie sich erneut mit der korrekten Site.

Nachdem Sie die Site korrigiert haben, warten Sie auf neue Sendeaktivität, bevor Metriken erscheinen. Historische Daten werden nicht nachträglich aufgefüllt.