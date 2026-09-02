---
nav_title: Workspace-Zeitzonen
article_title: Workspace-Zeitzonen
alias: /workspace_time_zones/
page_order: 3
description: "Dieser Referenzartikel beschreibt, wie Sie verschiedene Zeitzonen für Ihre Braze-Workspaces konfigurieren können, um Teams, die an verschiedenen geografischen Standorten tätig sind, mehr Kontrolle über den Zeitplan für Campaigns und Canvase zu ermöglichen."
toc_headers: h2
---

# Workspace-Zeitzonen {#workspace-time-zones}

> Mit Workspace-Zeitzonen können Administratoren spezifische Zeitzonen für einzelne Workspaces festlegen. Dadurch werden geplante Campaigns und Canvase (die weder die Ortszeit noch intelligentes Timing verwenden) entsprechend der für den Workspace festgelegten Zeitzone versendet und nicht entsprechend der übergeordneten Zeitzone des Unternehmens.

{% alert important %}
Workspace-Zeitzonen für den Nachrichtenversand werden schrittweise eingeführt. Möglicherweise sehen Sie diese Einstellungen noch nicht in Ihrem Dashboard.
{% endalert %}

Standardmäßig übernimmt ein neuer Workspace die für Ihr Unternehmen festgelegte Zeitzone. Administratoren können diese Standardeinstellung für einen oder mehrere Workspaces mit Workspace-Zeitzonen überschreiben. Wenn für einen Workspace eine Zeitzone festgelegt wird, referenzieren geplante Campaigns und Canvase innerhalb dieses Workspaces für ihre Versandzeiten diese neue Zeitzone.

Wenn beispielsweise die Zeitzone eines Workspaces auf PST eingestellt ist und eine Campaign innerhalb dieses Workspaces für den Versand um 15:00 Uhr PST im Zeitplan steht, wird sie um 15:00 Uhr PST zugestellt. Dies gilt auch dann, wenn die Zeitzone Ihres Unternehmens abweicht (z. B. EST, wo 15:00 Uhr PST 18:00 Uhr EST entspricht).

## Workspace-Zeitzonen verwalten {#manage-workspace-time-zones}

Wenn Sie Administrator:in sind, können Sie Workspace-Zeitzonen aufrufen und verwalten, indem Sie zu **Einstellungen** > **Administratoreinstellungen** > **Workspace-Zeitzonen** navigieren.

Hier können Sie eine Liste aller Ihrer Workspaces, deren eingestellte Zeitzone und den Zeitpunkt der letzten Bearbeitung der Zeitzone einsehen. Verwenden Sie die Suchleiste, um bestimmte Workspaces nach Namen zu finden.

### Eine Zeitzone festlegen {#setting-a-time-zone}

{% alert note %}
Es kann einige Minuten dauern, bis Zeitzonen-Aktualisierungen wirksam werden.
{% endalert %}

{% tabs %}
{% tab Einzelner Workspace %}
1. Suchen Sie den gewünschten Workspace in der Liste.
2. Wählen Sie das Symbol **Bearbeiten** neben dem Workspace-Namen aus.

![Seite „Workspace-Zeitzonen“ mit dem Symbol „Bearbeiten“ neben einem Workspace-Namen.]({% image_buster /assets/img/workspaces/time_zones/single_edit_icon.png %})

{: start="3"}
3. Wählen Sie im Dropdown-Menü die gewünschte Zeitzone für diesen Workspace aus.
4. Wählen Sie **Speichern** aus.

{% endtab %}
{% tab Mehrere Workspaces %}

Sie können eine bestimmte Zeitzone auf mehrere Workspaces gleichzeitig anwenden, indem Sie wie folgt vorgehen:

1. Aktivieren Sie die Kontrollkästchen neben allen Workspaces, die Sie Update or aktualisieren or aktualisieren möchten.
2. Wählen Sie **Zeitzone bearbeiten** aus.
3. Wählen Sie im Dropdown-Menü eine Zeitzone aus, die auf alle ausgewählten Workspaces angewendet werden soll.

![Seite „Workspace-Zeitzonen“ mit mehreren ausgewählten Workspaces und geöffnetem Dropdown „Zeitzone bearbeiten“.]({% image_buster /assets/img/workspaces/time_zones/bulk_edit_workspace_time_zone.png %})

{: start="4"}
4. Wählen Sie **Speichern** aus.

{% endtab %}
{% endtabs %}

## Auswirkungen auf Campaigns und Canvase {#impact-on-campaigns-and-canvases}

{% alert important %}
Informieren Sie relevante Teams und Stakeholder in jedem Workspace über Zeitzonenänderungen, um Verwirrung bei Campaign-Zeitplänen zu vermeiden.
{% endalert %}

- **Campaigns und Canvase mit Ortszeit und intelligentem Timing:** Campaigns und Canvase, die die Ortszeit der Nutzer:innen oder [intelligentes Timing]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#option-3-intelligent-timing) für die Zustellung verwenden, funktionieren weiterhin wie bisher und sind von Workspace-Zeitzonen nicht betroffen.
- **Geplante Campaigns und Canvase:** Alle geplanten Campaigns oder Canvase, die nicht die Ortszeit der Nutzer:innen oder intelligentes Timing für die Zustellung verwenden, werden basierend auf der ausgewählten Zeitzone des Workspace versendet.
- **Campaigns, die vor einer Zeitzonenänderung geplant wurden:** Wenn Sie eine Campaign oder ein Canvas vor der Änderung der Workspace-Zeitzone geplant haben, behält Braze die ursprüngliche Sendezeit bei und plant sie nicht neu. Wenn beispielsweise eine Campaign für den Versand um 19:00 Uhr PST eingestellt ist und die Workspace-Zeitzone auf EST geändert wird, wird die Campaign weiterhin um 19:00 Uhr PST gesendet (was nun 22:00 Uhr EST entspricht). Das System referenziert weiterhin die ursprüngliche Zeit, interpretiert sie jedoch durch die neue Workspace-Zeitzone.

## Auswirkungen auf datumsbasierte Zielgruppenfilter {#impact-on-date-based-audience-filters}

Wenn die Zeitzone eines Workspace aktualisiert wird, werden Zielgruppenfilter, die ausschließlich datumsbasierte Kriterien verwenden (bei denen keine bestimmte Uhrzeit angegeben ist), anhand der Grenzen der neuen Zeitzone neu ausgewertet.

Bei Filtern wie „Letztes angepasstes Event X nach“ verwendet Braze die Workspace-Zeitzone, um den Beginn und das Ende des Kalendertags zu bestimmen. Eine Änderung dieser Einstellung verschiebt den Stichtag um 23:59 Uhr für das jeweilige Datum.

### Beispiel {#example}

Ein Workspace aktualisiert seine Zeitzone von Eastern Time (EST) auf Pacific Time (PST).

- **Bisheriger Stichtag:** 23:59 Uhr EST
- **Neuer Stichtag:** 23:59 Uhr PST (was 2:59 Uhr EST am folgenden Tag entspricht)

Nach dieser Änderung wird ein:e Nutzer:in, der/die das angepasste Event am 6. März 2026 um 22:00 Uhr PST ausführt (was 1:00 Uhr EST am 7. März 2026 entspricht), nun in die Zielgruppe aufgenommen, da das Event innerhalb der PST-Kalendergrenze für dieses Datum lag.

## Auswirkungen auf Performance-Daten {#impact-on-performance-data}

Die Aktualisierung der Zeitzone Ihres Workspace beeinflusst, wie Performance-Daten in Ihrem Dashboard aggregiert und angezeigt werden. Da Analytics für Daten wie *täglich aktive Nutzer:innen* (täglich aktive:r Nutzer:in; täglich aktiv) auf die Workspace-Zeitzone angewiesen sind, um den Beginn und das Ende eines 24-Stunden-Tages zu definieren, verschiebt eine Änderung dieser Einstellung die entsprechenden Berichtszeiträume.

Wenn Sie die Zeitzone ändern, können Schwankungen oder „Verschiebungen“ in Ihren historischen Daten auftreten. Dies geschieht, weil sich das Zeitfenster von 0:00 Uhr bis 23:59 Uhr relativ zu UTC verschoben hat.

Betrachten Sie das folgende Beispiel für einen Workspace, dessen Zeitzone von UTC auf PST (UTC-8) umgestellt wird:

- **Vor der Änderung:** Ein „Tag“ für die Berichterstattung wird von 0:00 Uhr UTC bis 23:59 Uhr UTC gemessen.
- **Nach der Änderung:** Ein „Tag“ für die Berichterstattung wird nun von 0:00 Uhr PST bis 23:59 Uhr PST gemessen.

Infolgedessen wäre ein Ereignis, das am 1. Januar um 1:00 Uhr UTC stattfand, zuvor der Statistik des 1. Januars zugerechnet worden. Nach der Umstellung auf PST würde dasselbe Ereignis (das am 31. Dezember um 17:00 Uhr PST stattfand) im aktualisierten Bericht den Metriken des Vortags zugeordnet.