---
nav_title: Präferenzen für Benachrichtigungen
article_title: Präferenzen für Benachrichtigungen
page_order: 1
page_type: reference
description: "Dieser Referenzartikel behandelt Ihre verfügbaren Optionen zur Überwachung von Messaging und Aktivitäten in Ihrem Unternehmenskonto."

---

# Präferenzen für Benachrichtigungen

> Wenn Sie das Messaging und die Aktivitäten in Ihrem Unternehmenskonto überwachen möchten, können Sie bestimmte Benachrichtigungen einrichten und festlegen, wohin diese gesendet werden sollen.

Auf der Seite **Benachrichtigungseinstellungen** können Sie konfigurieren, wer (wenn überhaupt) Benachrichtigungen über Ihr Unternehmen erhält. Sie können festlegen, wer Benachrichtigungen über die Zustellung von Campaigns oder technische Fehler erhalten soll. Außerdem können Sie Empfänger:innen für den wöchentlichen Analytics-Bericht angeben. Für die meisten Benachrichtigungen unterstützt Braze E-Mail- und Webhook-Kanäle.

![Seite „Benachrichtigungseinstellungen“ im Braze-Dashboard]({% image_buster /assets/img_archive/notification_preferences.png %})

Um auf diese Seite zuzugreifen, gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **Benachrichtigungseinstellungen**.

{% alert tip %}
Sie können auch eine Integration mit Slack einrichten, um Benachrichtigungen zu erhalten. Weitere Informationen finden Sie unter [Nachrichten über eingehende Webhooks senden](https://api.slack.com/incoming-webhooks).
{% endalert %}

## Verfügbare Benachrichtigungen

Die folgende Tabelle beschreibt die verfügbaren Benachrichtigungen und die Kanäle, über die sie zugestellt werden.

{% alert note %}
Wenn Sie den Standardwert **Empfänger:innen** von **Alle Dashboard-Nutzer:innen** löschen und ihn wieder hinzufügen möchten, können Sie ihn manuell in das Dropdown-Feld eingeben.
{% endalert %}

| Benachrichtigung | Beschreibung | Verfügbare Benachrichtigungskanäle |
|--------------|-------------|-----------------|
| API-Nutzungswarnungen | Wenn Sie diese Option auswählen, gelangen Sie zum **API-Nutzungs-Dashboard**, wo Sie dann zum Tab [**API-Nutzungswarnungen**]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts/) navigieren und Warnungen einrichten können, um wichtige API-Anfragevolumen zu überwachen. | E-Mail, Webhook |
| AWS-Zugangsdaten-Fehler | Benachrichtigt Empfänger:innen, wenn Braze beim Versuch, Ihre Amazon-Web-Services-Zugangsdaten für einen Datenexport zu verwenden, einen Fehler erhält. Dies umfasst auch Zugangsdaten-Fehler-Benachrichtigungen für Google Cloud Services und Azure (Microsoft Cloud Services). | E-Mail, Webhook |
| Campaign automatisch gestoppt | Benachrichtigt Empfänger:innen, wenn Braze eine Campaign gestoppt hat. | E-Mail |
| Canvas automatisch gestoppt | Benachrichtigt Empfänger:innen, wenn Braze einen Canvas gestoppt hat. | E-Mail |
| Ablauf von Campaign-Interaktionsdaten | Benachrichtigt Empfänger:innen über jede Campaign, bei der der Ablauf von Campaign-Interaktionsdaten ansteht, zusammen mit Informationen über Segments, Campaigns oder Canvases, die diese in einem Retargeting-Filter referenzieren und in den letzten 30 Tagen zum Senden einer Nachricht verwendet wurden. | E-Mail |
| Campaign/Canvas aktualisiert | Benachrichtigt Empfänger:innen, wenn eine aktive Campaign oder ein aktiver Canvas aktualisiert oder deaktiviert wird, sowie wenn eine inaktive Campaign oder ein inaktiver Canvas reaktiviert wird oder Entwürfe gestartet werden. | E-Mail |
| Campaign-/Canvas-Volumenlimit erreicht | Benachrichtigt Empfänger:innen, wenn eine Campaign oder ein Canvas das Volumenlimit erreicht hat. | E-Mail |
| Ablauf von Canvas-Interaktionsdaten | Benachrichtigt Empfänger:innen über jeden Canvas, bei dem der Ablauf von Canvas-Interaktionsdaten ansteht, zusammen mit Informationen über Segments, Campaigns oder Canvases, die diesen in einem Retargeting-Filter referenzieren und in den letzten 30 Tagen zum Senden einer Nachricht verwendet wurden. | E-Mail |
| Kommentare in Canvases | Benachrichtigt Empfänger:innen, wenn ein Canvas neue Kommentare hat. | E-Mail |
| Connected-Content-Fehler | Benachrichtigt Empfänger:innen, wenn ein Connected-Content-Endpunkt Fehler aufweist. | E-Mail |
| Push-Fehler | Benachrichtigt Empfänger:innen, wenn ein Push-Endpunkt Fehler aufweist. | E-Mail, Webhook |
| Limit für geplante Campaign erreicht | Benachrichtigt Empfänger:innen, wenn das Limit für eine wiederkehrende geplante Campaign erreicht wurde. | E-Mail, Webhook |
| Geplante Campaign hat den Versand abgeschlossen | Benachrichtigt Empfänger:innen, wenn eine geplante Campaign den Versand abgeschlossen hat. | E-Mail, Webhook |
| Webhook-Fehler | Benachrichtigt Empfänger:innen, wenn ein Webhook-Endpunkt Fehler aufweist. | E-Mail |
| Wöchentlicher Analytics-Bericht | Sendet jeden Montag eine Zusammenfassung der Workspace-Aktivitäten der vergangenen Woche an die Empfänger:innen. Empfänger:innen erhalten eine Zusammenfassung für jeden Workspace, dem sie angehören. | E-Mail |
| Tägliche Canvas-/Campaign-Eingangsvolumenlimits | Sendet Benachrichtigungen jedes Mal, wenn ein Sendelimit erreicht wird. | E-Mail |
| Agentenkonsole-Fehler | Benachrichtigt Empfänger:innen, wenn ein [Agentenkonsole-Agent]({{site.baseurl}}/user_guide/brazeai/agents/) sein Ausführungslimit mit der aktuellen Funktionalität erreicht hat oder wenn ein Agent Modelle verwendet, die nicht mehr verfügbar sind. | E-Mail |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
[Gesperrte Nutzer:innen]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users/#suspending-company-users) können weiterhin Benachrichtigungen von Braze erhalten.
{% endalert %}

## Wöchentlicher Analytics-Bericht

Braze sendet optional jeden Montag um 5 Uhr EST einen wöchentlichen Bericht per E-Mail an von Ihnen bestimmte Personen in Ihrem Unternehmen. Sie können die angepassten Events, die im wöchentlichen Bericht enthalten sein sollen, unter **Dateneinstellungen** > **Angepasste Events** auswählen.

Sie können bis zu fünf Events auswählen, die in Ihrem wöchentlichen Bericht enthalten sein sollen:

![Auswahl von Events, die im Analytics-Bericht enthalten sein sollen]({% image_buster /assets/img_archive/company_analytics_report_new.png %})