---
article_title: Workspace-Rate-Limits
description: "Erfahren Sie, wie Sie Workspace-Rate-Limits festlegen, um zu steuern, wie das gesamte API-Rate-Limit Ihres Unternehmens auf einzelne Workspaces verteilt wird. So verhindern Sie, dass eine einzelne Integration oder ein Team zu viele Anfragen an einen bestimmten Endpunkt sendet."
permalink: /workspace_rate_limits/
---

# Workspace-Rate-Limits

> Erfahren Sie, wie Sie Workspace-Rate-Limits festlegen, um zu steuern, wie das gesamte API-Rate-Limit Ihres Unternehmens auf einzelne Workspaces verteilt wird. So verhindern Sie, dass eine einzelne Integration oder ein Team zu viele Anfragen an einen bestimmten Endpunkt sendet.

## Voraussetzungen {#prerequisites}

Workspace-Rate-Limits sind nur für Braze-Verträge ohne Datenpunkte verfügbar. Außerdem benötigen Sie [Admin-Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin), um Rate-Limits zu verwalten.

## Über Workspace-Rate-Limits {#about-workspace-rate-limits}

Standardmäßig werden Rate-Limits auf Unternehmensebene über alle Ihre Workspaces hinweg geteilt.

Mit Workspace-Rate-Limits können Sie eine maximale Anzahl von API-Anfragen festlegen, die ein Workspace an einen bestimmten Ingestion-Endpunkt senden kann, z. B. `/users/track` oder SDK-Daten. Sie können Rate-Limits auch auf eine Gruppe von Workspaces anwenden, sodass das Limit von allen Workspaces in dieser Gruppe gemeinsam genutzt wird.

Wenn Ihr `/users/track`-Endpunkt beispielsweise ein Rate-Limit auf Unternehmensebene von 500.000 Anfragen pro Stunde hat, könnten Sie die folgenden Workspace-Rate-Limits festlegen:

- Ein Rate-Limit von 10.000 Anfragen pro Stunde für _Workspace 1_
- Ein gemeinsames Rate-Limit von 200.000 Anfragen pro Stunde für _Workspace 2_ und _Workspace 3_
- Kein Rate-Limit für _Workspace 4_, sodass das Standard-Rate-Limit auf Unternehmensebene verwendet wird

## Workspace-Rate-Limits verwalten {#managing-workspace-rate-limits}

### Ein Limit zuweisen {#assigning-a-limit}

Um ein neues Rate-Limit für einen oder mehrere Workspaces zuzuweisen, gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **Workspace-Rate-Limits** und wählen Sie dann **Rate-Limits zuweisen**.

![Die Seite „Workspace-Rate-Limits“ im Braze-Dashboard.]({% image_buster /assets/unlisted_docs/img/workspace_rate_limits/settings.png %}){: style="max-width:85%;"}

Wählen Sie als Nächstes einen Endpunkt und einen oder mehrere Workspaces aus und geben Sie dann Ihr Rate-Limit ein. Das Limit kann eine beliebige ganze Zahl sein, die größer als 1.000 ist und Ihr Rate-Limit auf Unternehmensebene nicht überschreitet.

Wenn Sie fertig sind, wählen Sie **Rate-Limit aktualisieren**.

![Das Popup-Fenster „Rate-Limit“ mit Optionen zur Auswahl eines Endpunkts, von Workspaces und eines Rate-Limits.]({% image_buster /assets/unlisted_docs/img/workspace_rate_limits/update_rate_limit.png %}){: style="max-width:45%;"}

{% alert note %}
Wenn Sie mehr als einen Workspace auswählen, wird das Rate-Limit von dieser Gruppe von Workspaces gemeinsam genutzt.
{% endalert %}

### Ein Limit bearbeiten {#editing-a-limit}

Um ein bestehendes Workspace-Rate-Limit zu bearbeiten, gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **Workspace-Rate-Limits** und wählen Sie dann die <i class="fas fa-ellipsis-vertical" aria-label="Vertikale Auslassungspunkte"></i> vertikale Auslassungspunkte und dann **Bearbeiten**. Ihr neues Rate-Limit kann innerhalb weniger Minuten wirksam werden.

### Ein Limit zurücksetzen {#resetting-a-limit}

Um ein bestehendes Rate-Limit zurückzusetzen, sodass es auf Ihr Rate-Limit auf Unternehmensebene zurückgesetzt wird, gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **Workspace-Rate-Limits** und wählen Sie dann die <i class="fas fa-ellipsis-vertical" aria-label="Vertikale Auslassungspunkte"></i> vertikale Auslassungspunkte und dann **Zurücksetzen**.

## Nutzung überwachen {#monitoring-usage}

### Antwort-Header {#response-headers}

Standardmäßig enthalten alle Ingestion-Antworten die folgenden Header, die Ihr reguläres Rate-Limit auf Unternehmensebene widerspiegeln.

Wir empfehlen, diese Header in Ihrer Integrationslogik zu verwenden, um Rate-Limits effektiv zu verwalten. Sie können beispielsweise das Anfragevolumen reduzieren, wenn Sie sich diesen Limits nähern, und den `Retry-After`-Header verwenden, um zu bestimmen, wann ein erneuter Versuch gestartet werden soll.

| Header-Name | Beschreibung |
| ----- | ----- |
| `X-RateLimit-Limit` | Die maximale Anzahl zulässiger Anfragen im aktuellen Rate-Limit-Fenster. |
| `X-RateLimit-Remaining` | Die Anzahl der verbleibenden Anfragen im aktuellen Fenster. |
| `X-RateLimit-Reset` | Wann das aktuelle Rate-Limit-Fenster zurückgesetzt wird (UTC-Epochensekunden). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Fehlercodes {#error-codes}

Wenn ein Workspace-Rate-Limit erreicht wird, gibt Ihre Anfrage einen `429`-Antwortcode zurück und die Header enthalten einen `Retry-After`-Wert. Dieser gibt die Anzahl der Sekunden bis zum Zurücksetzen des Rate-Limits an.

Der `Retry-After`-Wert gibt die Anzahl der Sekunden bis zum Beginn der nächsten Stunde an, wenn das Workspace-Rate-Limit zurückgesetzt wird.

### API-Nutzungs-Dashboard {#api-usage-dashboard}

Um das Anfragevolumen, Antwortcodes und das Ingestion-Verhalten über Workspaces hinweg zu überwachen, können Sie auch das [API-Nutzungs-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_dashboard/) verwenden.

Sie können das Dashboard filtern, um `429 Workspace Rate Limited` oder `429 Company Rate Limited` anzuzeigen, sodass Sie schnell erkennen können, ob eine Anfrage durch das Unternehmens- oder Workspace-Rate-Limit begrenzt wurde.