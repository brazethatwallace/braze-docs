---
nav_title: Status
article_title: Status
page_order: 6
description: "Erfahren Sie mehr über Status für Campaigns und Canvase und wie Sie diese im Dashboard verwenden können."
tool:
    - Campaigns
    - Canvas
---

# Campaign- und Canvas-Status {#campaign-and-canvas-statuses}

> Erfahren Sie mehr über Status für Campaigns und Canvase und wie Sie diese im Dashboard verwenden können.

## Nach Status filtern {#filtering-by-status}

Um Ihre Campaigns oder Canvase nach Status zu filtern, wählen Sie **All Statuses** aus und wählen Sie dann einen Status.

![Das Dropdown-Menü „All Statuses“ im Braze-Dashboard.]({% image_buster /assets/img/messaging_fundamentals/filter-by-status.png %}){: style="max-width:70%;"}

## Status ändern {#changing-the-status}

Um den Status einer Campaign oder eines Canvas zu ändern, wählen Sie das Menü <i class="fas fa-ellipsis-vertical"></i> aus und wählen Sie dann einen Status.

![Eine Liste von Canvases im Braze-Dashboard, mit geöffnetem Menü für eines der Canvases.]({% image_buster /assets/img/messaging_fundamentals/change-status.png %})

## Verfügbare Status {#available-statuses}

Dies sind die verfügbaren Status für Campaigns und Canvase:

| Status | Beschreibung |
| --- | --- |
| Aktiv | Aktive Campaigns und Canvase befinden sich im Versandprozess. Standardmäßig werden aktive Campaigns und Canvase auf den jeweiligen Seiten angezeigt. |
| Entwurf | Entwürfe von Campaigns und Canvase sind gespeichert, aber noch nicht gestartet. Um die Bearbeitung fortzusetzen und den Versand zu starten, können Sie den Entwurf auswählen, indem Sie im Braze-Dashboard zu **Messaging** gehen und **Canvas** oder **Campaigns** auswählen. |
| Archiviert | Archivierte Campaigns und Canvase sind Nachrichten, die nicht mehr versendet werden. Diese Campaigns und Canvase werden auch aus den Statistikdiagrammen auf den Seiten [**Startseite**]({{site.baseurl}}/user_guide/analytics/dashboards/home) und [**Umsatz**]({{site.baseurl}}/user_guide/analytics/reports/revenue_report) entfernt. |
| Gestoppt | Gestoppte Campaigns und Canvase sind pausiert, können aber weiterhin bearbeitet werden. Um ein Canvas fortzusetzen, gehen Sie zum Schritt **Zusammenfassung** im Canvas-Builder und wählen Sie **Canvas fortsetzen**. Für Campaigns wählen Sie das Menü <i class="fas fa-ellipsis-vertical" aria-label="Weitere Optionen"></i> und dann **Fortsetzen**. Weitere Informationen finden Sie unter [Verhalten gestoppter Canvase](#stopped-canvas-behavior). |
| Inaktiv | Wenn ein Campaign oder Canvas keine Nachrichten mehr versendet, weist Braze einen Inaktiv-Status zu, um die Sortierung und Verwaltung Ihrer Liste von Campaigns und Canvase zu erleichtern. Sie können einsehen, welche Campaigns oder Canvase automatisch gestoppt werden und das zugehörige Stoppdatum. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Verfügbare Status" }

### Verhalten gestoppter Canvase {#stopped-canvas-behavior}

Wenn ein Canvas gestoppt wird, geschieht Folgendes:

- **Geplante Nachrichten:** Ihre geplanten Nachrichten werden nicht gesendet, unabhängig davon, wo sich Nutzer:innen im Canvas befinden. Dies gilt auch für Nutzer:innen, die aufgrund von Rate-Limiting in der Warteschlange standen.
- **E-Mail-Versand:** Der E-Mail-Versand wird möglicherweise nicht sofort gestoppt, da Ihr E-Mail-Anbieter (E-Mail-Anbieter or ESP) Ihre bestehenden Anfragen möglicherweise weiterhin verarbeitet.
- **Verzögerungsschritte:** Nutzer:innen in einem [Verzögerungsschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) verbleiben dort wie gewohnt, verlassen das Canvas jedoch, wenn der festgelegte Zeitraum endet.
- **Entwurfsänderungen:** Alle Entwurfsänderungen am Canvas werden verworfen, wenn das Canvas gestoppt wird.

#### Wenn Sie ein Canvas fortsetzen {#when-you-resume-a-canvas}

Um das Canvas fortzusetzen, gehen Sie zum Schritt **Zusammenfassung** im Canvas-Builder und wählen Sie **Canvas fortsetzen**. Wenn Sie ein Canvas fortsetzen, setzen Nutzer:innen ihre Journey an der Stelle fort, an der sie aufgehört haben:

- Nutzer:innen in Verzögerungsschritten: Nutzer:innen, die sich in einem Verzögerungsschritt befanden, als das Canvas gestoppt wurde, warten weiterhin auf die verbleibende Verzögerungszeit. Wenn sich beispielsweise Nutzer:innen 2 Stunden in einer 24-Stunden-Verzögerung befanden, als das Canvas für 3 Tage gestoppt wurde, warten sie nach der Wiederaufnahme des Canvas noch 22 weitere Stunden, bevor sie fortfahren.
- Nutzer:innen, die auf Nachrichten warten: Alle geplanten Nachrichten, die beim Stoppen des Canvas ausstanden, werden bei der Wiederaufnahme wie geplant gesendet – sofern der geplante Zeitpunkt noch nicht verstrichen ist.
- Nutzer:innen, die das Canvas verlassen haben: Nutzer:innen, die das Canvas während der Stoppphase verlassen haben (z. B. Nutzer:innen, die sich in Verzögerungsschritten befanden und das Ende ihrer Verzögerung erreicht haben), treten dem Canvas bei der Wiederaufnahme nicht erneut bei.

#### Verhalten bei Ortszeit {#local-time-zone-behavior}

Wenn Ihr Canvas so konfiguriert ist, dass **Nutzer:innen in ihrer Ortszeit in dieses Canvas eintreten**, beachten Sie beim Stoppen und Fortsetzen Folgendes:

- Entry-Fenster: Wenn Sie das Canvas fortsetzen, treten Nutzer:innen basierend auf ihrer Ortszeit wie ursprünglich konfiguriert ein. Braze bewertet die Entry-Berechtigung weiterhin gemäß der Zeitzone jeder Nutzerin und jedes Nutzers.
- Verpasste Entry-Fenster: Wenn das Canvas während eines geplanten Entry-Fensters für Nutzer:innen in bestimmten Zeitzonen gestoppt wurde, treten diese Nutzer:innen bei der Wiederaufnahme des Canvas nicht rückwirkend ein. Die Entry-Bewertung wird ab diesem Zeitpunkt fortgesetzt.

#### Häufige Szenarien {#common-scenarios}

**Szenario 1: Fehler im Nachrichteninhalt**
Sie starten ein Canvas, bemerken aber einen Tippfehler in einer der Nachrichten. Stoppen Sie das Canvas, bearbeiten Sie die Nachricht im Entwurfsmodus und setzen Sie es dann fort. Nutzer:innen, die die Nachricht noch nicht erhalten haben, erhalten die korrigierte Version. Nutzer:innen, die sie bereits erhalten haben, erhalten sie nicht erneut.

**Szenario 2: Targeting-Problem**
Sie stellen fest, dass das Canvas das falsche Segment anspricht. Stoppen Sie das Canvas sofort, um zu verhindern, dass weitere Nutzer:innen eintreten. Alle Nutzer:innen, die sich derzeit in Verzögerungsschritten befinden, verlassen das Canvas, wenn ihre Verzögerungszeit endet. Sie können dann ein neues Canvas mit dem korrekten Targeting erstellen.

**Szenario 3: Szenario mit verlängerter Verzögerung**
Sie haben ein Canvas mit einem siebentägigen Verzögerungsschritt. Sie stoppen das Canvas nach drei Tagen. Nutzer:innen, die sich im Verzögerungsschritt befanden, warten weiter, aber wenn ihre Verzögerungszeit endet, während das Canvas noch gestoppt ist, verlassen sie das Canvas. Wenn Sie das Canvas vor Ablauf ihrer Verzögerung fortsetzen, setzen sie ihre Journey fort.

## Best Practices {#best-practices}

### Nachrichten nach Status überwachen {#monitor-your-messages-by-status}

Sie können Ihre Nachrichten nach Status überwachen, um die Performance-Details zu überprüfen. Wenn Sie beispielsweise eine Reihe aktiver Campaigns haben, können Sie die Performance jeder Campaign anhand ihrer Engagement-Metriken bewerten und bei Bedarf Anpassungen vornehmen. Wenn Sie stattdessen einige gestoppte Canvase haben, können Sie überlegen, ob diese für das Messaging fortgesetzt oder vollständig archiviert werden sollten.

{% alert tip %}
Suchen Sie nach weiteren Möglichkeiten, organisiert zu bleiben? Fügen Sie [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) und [Tags]({{site.baseurl}}/user_guide/messaging/governance/tags) hinzu, um mehr Kontext auf einen Blick zu bieten.
{% endalert %}

### Aktive Nachrichten überprüfen {#audit-your-active-messages}

Durch regelmäßige Überprüfungen Ihrer aktiven Campaigns und Canvase können Sie die Relevanz und Performance bewerten und veraltete Campaigns und Canvase entfernen oder Update or aktualisieren or aktualisieren, um Ihr Messaging aktuell zu halten.