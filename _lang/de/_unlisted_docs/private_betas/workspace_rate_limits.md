---
article_title: Workspace-Rate-Limits
description: "Erfahren Sie, wie Sie Workspace-Rate-Limits festlegen, um zu steuern, wie das gesamte API-Rate-Limit Ihres Unternehmens auf einzelne Workspaces verteilt wird. So verhindern Sie, dass eine einzelne Integration oder ein Team zu viele Anfragen an einen bestimmten Endpunkt sendet."
permalink: /workspace_rate_limits/
---

# Workspace-Rate-Limits

> Erfahren Sie, wie Sie Workspace-Rate-Limits festlegen, um zu steuern, wie das gesamte API-Rate-Limit Ihres Unternehmens auf einzelne Workspaces verteilt wird. So verhindern Sie, dass eine einzelne Integration oder ein Team zu viele Anfragen an einen bestimmten Endpunkt sendet.

## Voraussetzungen {#prerequisites}

Workspace-Rate-Limits sind nur für Braze-Verträge ohne Datenpunkte verfügbar. Außerdem benötigen Sie [Administratorberechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions), um Rate-Limits zu verwalten.

## Über Workspace-Rate-Limits {#about-workspace-rate-limits}

Standardmäßig werden Rate-Limits auf Unternehmensebene über alle Ihre Workspaces hinweg geteilt.

Mit Workspace-Rate-Limits können Sie eine maximale Anzahl von API-Anfragen festlegen, die ein Workspace an einen bestimmten Ingestion-Endpunkt senden kann, z. B. `/users/track` oder SDK or Software-Development-Kit-Daten. Sie können Rate-Limits auch auf eine Gruppe von Workspaces anwenden, d. h. das Limit wird von allen Workspaces in dieser Gruppe gemeinsam genutzt.

Wenn Ihr `/users/track`-Endpunkt beispielsweise ein Rate-Limit auf Unternehmensebene von 500.000 Anfragen pro Stunde hat, könnten Sie die folgenden Workspace-Rate-Limits festlegen:

- Ein Rate-Limit von 10.000 Anfragen pro Stunde, angewendet auf _Workspace 1_
- Ein gemeinsames Rate-Limit von 200.000 Anfragen pro Stunde, angewendet auf _Workspace 2_ und _Workspace 3_
- Kein Rate-Limit für _Workspace 4_, d. h. es wird das standardmäßige Rate-Limit auf Unternehmensebene verwendet

## Workspace-Rate-Limits verwalten {#managing-workspace-rate-limits}

### Ein Limit zuweisen {#assigning-a-limit}

Um ein neues Rate-Limit für einen oder mehrere Workspaces zuzuweisen, gehen Sie zu **Einstellungen** > **Administratoreinstellungen** > **Workspace-Rate-Limits** und wählen Sie dann **Rate-Limits zuweisen** aus.

![Die Seite „Workspace-Rate-Limits“ im Braze-Dashboard.]({% image_buster /assets/unlisted_docs/img/workspace_rate_limits/settings.png %}){: style="max-width:85%;"}

Wählen Sie anschließend einen Endpunkt und einen oder mehrere Workspaces aus und geben Sie dann Ihr Rate-Limit ein. Das Limit kann eine beliebige ganze Zahl sein, die größer als 1.000 ist und Ihr unternehmensweites Rate-Limit nicht überschreitet.

Wenn Sie fertig sind, wählen Sie **Rate-Limit Update or aktualisieren or aktualisieren** aus.

![Das Popup-Fenster „Rate-Limit“ mit Optionen zur Auswahl eines Endpunkts, von Workspaces und eines Rate-Limits.]({% image_buster /assets/unlisted_docs/img/workspace_rate_limits/update_rate_limit.png %}){: style="max-width:45%;"}

{% alert note %}
Wenn Sie mehr als einen Workspace auswählen, wird das Rate-Limit auf diese Gruppe von Workspaces aufgeteilt.
{% endalert %}

### Ein Limit bearbeiten {#editing-a-limit}

Um ein bestehendes Workspace-Rate-Limit zu bearbeiten, gehen Sie zu **Einstellungen** > **Administratoreinstellungen** > **Workspace-Rate-Limits** und wählen Sie dann die <i class="fas fa-ellipsis-vertical" aria-label="Vertikale Auslassungspunkte"></i> vertikale Ellipse aus und wählen Sie **Bearbeiten**. Ihr neues Rate-Limit kann innerhalb weniger Minuten wirksam werden.

### Ein Limit zurücksetzen {#resetting-a-limit}

Um ein bestehendes Rate-Limit zurückzusetzen, sodass es auf Ihr unternehmensweites Rate-Limit zurückgesetzt wird, gehen Sie zu **Einstellungen** > **Administratoreinstellungen** > **Workspace-Rate-Limits** und wählen Sie dann die <i class="fas fa-ellipsis-vertical" aria-label="Vertikale Auslassungspunkte"></i> vertikale Ellipse aus und wählen Sie **Zurücksetzen**.

## Nutzung überwachen {#monitoring-usage}

### Antwort-Header {#response-headers}

Standardmäßig enthalten alle Ingestion-Antworten die folgenden Header, die Ihr festes unternehmensweites Rate-Limit widerspiegeln.

Wir empfehlen, diese Header in Ihrer Integrationslogik zu verwenden, um Rate-Limits effektiv zu verwalten. Beispielsweise können Sie das Anfragevolumen reduzieren, wenn Sie sich diesen Limits nähern, und den `Retry-After`-Header verwenden, um zu bestimmen, wann ein erneuter Versuch erfolgen sollte.

| Header-Name | Beschreibung |
| ----- | ----- |
| `X-RateLimit-Limit` | Die maximale Anzahl von Anfragen, die im aktuellen Rate-Limit-Fenster zulässig sind. |
| `X-RateLimit-Remaining` | Die Anzahl der verbleibenden Anfragen im aktuellen Fenster. |
| `X-RateLimit-Reset` | Zeitpunkt, zu dem das aktuelle Rate-Limit-Fenster zurückgesetzt wird (UTC-Epochensekunden). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Fehlercodes {#error-codes}

Wenn ein Workspace-Rate-Limit erreicht wird, gibt Ihre Anfrage den Antwortcode `429` zurück, und die Header enthalten einen `Retry-After`-Wert. Dieser gibt die Anzahl der Sekunden bis zum Zurücksetzen des Rate-Limits an.

Der `Retry-After`-Wert gibt die Anzahl der Sekunden bis zum Beginn der nächsten Stunde an, zu der das Workspace-Rate-Limit zurückgesetzt wird.

### API-Nutzungs-Dashboard {#api-usage-dashboard}

Um das Anfragevolumen, Antwortcodes und das Ingestion-Verhalten über alle Workspaces hinweg zu überwachen, können Sie auch das [API-Nutzungs-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/api_usage) verwenden.

Sie können das Dashboard so filtern, dass `429 Workspace Rate Limited` oder `429 Company Rate Limited` angezeigt wird, sodass Sie schnell erkennen können, ob eine Anfrage durch das unternehmensweite oder das Workspace-Rate-Limit begrenzt wurde.