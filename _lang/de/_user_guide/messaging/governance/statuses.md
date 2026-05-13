---
nav_title: Status
article_title: Status
page_order: 5
description: "Erfahren Sie mehr über Status für Campaigns und Canvases und wie Sie diese im Dashboard verwenden können."
tool:
    - Campaigns
    - Canvas
---

# Campaign- und Canvas-Status {#campaign-and-canvas-statuses}

> Erfahren Sie mehr über Status für Campaigns und Canvases und wie Sie diese im Dashboard verwenden können.

## Nach Status filtern {#filtering-by-status}

Um Ihre Campaigns oder Canvases nach Status zu filtern, wählen Sie **Alle Status** und dann einen Status aus.

![Das Dropdown-Menü „Alle Status“ im Braze-Dashboard.]({% image_buster /assets/img/messaging_fundamentals/filter-by-status.png %}){: style="max-width:70%;"}

## Status ändern {#changing-the-status}

Um den Status einer Campaign oder eines Canvas zu ändern, wählen Sie das Menü <i class="fas fa-ellipsis-vertical"></i> und dann einen Status aus.

![Eine Liste von Canvases im Braze-Dashboard, wobei das Menü für eines der Canvases geöffnet ist.]({% image_buster /assets/img/messaging_fundamentals/change-status.png %})

## Verfügbare Status {#available-statuses}

Dies sind die verfügbaren Status für Campaigns und Canvases:

| Status | Beschreibung |
| --- | --- |
| Aktiv | Aktive Campaigns und Canvases befinden sich im Versandprozess. Standardmäßig werden Ihnen aktive Campaigns und Canvases auf den jeweiligen Seiten angezeigt. |
| Entwurf | Entwürfe von Campaigns und Canvases sind gespeichert, aber noch nicht gestartet. Um die Bearbeitung fortzusetzen und den Versand zu starten, können Sie den Entwurf auswählen, indem Sie im Braze-Dashboard zu **Messaging** gehen und **Canvas** oder **Campaigns** auswählen. |
| Archiviert | Archivierte Campaigns und Canvases sind Nachrichten, die nicht mehr versendet werden. Diese Campaigns und Canvases werden auch aus den Statistikdiagrammen auf den Seiten [**Startseite**]({{site.baseurl}}/user_guide/analytics/dashboards/home/) und [**Umsatz**]({{site.baseurl}}/user_guide/analytics/reports/revenue_report/) entfernt. |
| Gestoppt | Gestoppte Campaigns und Canvases sind pausiert, können aber weiterhin bearbeitet werden. Um ein Canvas fortzusetzen, gehen Sie zum Schritt **Summary** des Canvas-Builders und wählen Sie **Resume Canvas**. Für Campaigns wählen Sie das Menü <i class="fas fa-ellipsis-vertical"></i> und dann **Resume**. Weitere Informationen finden Sie unter [Verhalten gestoppter Canvases](#stopped-canvas-behavior). |
| Inaktiv | Wenn eine Campaign oder ein Canvas keine Nachrichten mehr versendet, weist Braze einen inaktiven Status zu, um Ihnen bei der Sortierung und Verwaltung Ihrer Liste von Campaigns und Canvases zu helfen. Sie können einsehen, welche Campaigns oder Canvases automatisch gestoppt werden und das zugehörige Stoppdatum. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Verfügbare Status" }

### Verhalten gestoppter Canvases {#stopped-canvas-behavior}

Wenn ein Canvas gestoppt wird, geschieht Folgendes:

- **Geplante Nachrichten:** Ihre geplanten Nachrichten werden nicht gesendet, unabhängig davon, wo sich Nutzer:innen im Canvas befinden. Dies gilt auch für Nutzer:innen, die aufgrund von Rate-Limiting in der Warteschlange standen.
- **E-Mail-Versand:** Der E-Mail-Versand wird möglicherweise nicht sofort gestoppt, da Ihr E-Mail-Anbieter (ESP) Ihre bestehenden Anfragen möglicherweise weiterhin verarbeitet.
- **Verzögerungsschritte:** Nutzer:innen in einem [Verzögerungsschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step/) verbleiben dort wie gewohnt, verlassen das Canvas jedoch, wenn der festgelegte Zeitraum endet.
- **Entwurfsänderungen:** Alle Entwurfsänderungen am Canvas werden verworfen, wenn das Canvas gestoppt wird.

Um das Canvas fortzusetzen, gehen Sie zum Schritt **Summary** des Canvas-Builders und wählen Sie **Resume Canvas**. Bei der Reaktivierung werden alle zuvor gestoppten Nachrichten wie geplant gesendet&#8212;sofern der geplante Zeitpunkt noch nicht verstrichen ist.

## Best Practices {#best-practices}

### Nachrichten nach Status überwachen {#monitor-your-messages-by-status}

Sie können Ihre Nachrichten nach Status überwachen, um die Performance-Details zu überprüfen. Wenn Sie beispielsweise eine Reihe aktiver Campaigns haben, können Sie die Performance jeder Campaign anhand ihrer Engagement-Metriken bewerten und bei Bedarf Anpassungen vornehmen. Wenn Sie stattdessen einige gestoppte Canvases haben, können Sie überlegen, ob diese für den Nachrichtenversand fortgesetzt oder vollständig archiviert werden sollten.

{% alert tip %}
Suchen Sie nach weiteren Möglichkeiten, organisiert zu bleiben? Fügen Sie [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) und [Tags]({{site.baseurl}}/user_guide/messaging/governance/tags/) hinzu, um mehr Kontext auf einen Blick zu erhalten.
{% endalert %}

### Aktive Nachrichten überprüfen {#audit-your-active-messages}

Durch regelmäßige Überprüfungen Ihrer aktiven Campaigns und Canvases können Sie die Relevanz und Performance bewerten und veraltete Campaigns und Canvases entfernen oder aktualisieren, um Ihr Messaging aktuell zu halten.