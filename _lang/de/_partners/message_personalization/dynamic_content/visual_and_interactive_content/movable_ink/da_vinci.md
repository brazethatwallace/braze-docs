---
title: "Movable Ink Da Vinci"
article_title: Movable Ink Da Vinci
alias: "/partners/movable_ink_da_vinci/"
description: "Die Integration von Braze und Movable Ink Da Vinci ermöglicht es Marken, hochgradig personalisiertes Messaging zu liefern, indem sie die KI or künstliche Intelligenz-gesteuerte Content-Decisioning-Engine von Da Vinci nutzen. Da Vinci kuratiert die relevantesten Inhalte für jede Nutzer:in und stellt die Nachrichten nahtlos über Braze bereit."
page_type: partner
search_tag: Partner

---

# Movable Ink Da Vinci

> Die Integration von Braze und Movable Ink [Da Vinci](https://movableink.com/da-vinci) ermöglicht es Marken, hochgradig personalisiertes Messaging zu liefern, indem sie die KI or künstliche Intelligenz-gesteuerte Content-Decisioning-Engine von Da Vinci nutzen. Da Vinci kuratiert die relevantesten Inhalte für jede Nutzer:in und stellt die Nachrichten nahtlos über Braze bereit.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|------------|-------------|
| Movable Ink Da Vinci | Sie benötigen ein Movable Ink Da Vinci-Konto, um die Vorteile dieser Partnerschaft zu nutzen. |
| Braze-Currents – Nachrichten-Engagement-Events | Ein benutzerdefinierter Braze-Currents-Export ist erforderlich, um Daten über Nachrichten-Engagement-Events an Movable Ink zu senden. |
| Braze Representational State Transfer-API-Schlüssel | Sie benötigen einen Braze Representational State Transfer-API-Schlüssel mit den Berechtigungen `messages.send`, `sends.id.create` und `campaigns.details`. Dieser kann im Braze-Dashboard unter **Settings** > **API Keys** erstellt werden. <br><br>Weitere Anweisungen zur Einrichtung erhalten Sie direkt von Ihrem Movable Ink Team. Lesen Sie den Abschnitt [Integration](#integration). |
| Da Vinci App-Instanz in Braze | Erstellen Sie eine eigene Da Vinci App-Instanz in Braze. Eine neue App können Sie im Braze-Dashboard erstellen, indem Sie zu **Settings** > **App Settings** > **+ Add App** gehen. Nennen Sie die App „**Movable Ink - Da Vinci**“ und wählen Sie eine beliebige Plattform aus (eine Plattformauswahl ist erforderlich, aber der Typ hat keinen Einfluss auf die Funktionalität). Erfahren Sie mehr darüber, [wie Sie eine neue App hinzufügen können]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/#step-3-add-your-app-instances). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration {#integration}

Um mit der Integration zu beginnen, wenden Sie sich bitte an Ihr Movable Ink Team, das Sie dabei unterstützt. Movable Ink wird Ihnen entsprechende Anweisungen für den Zugang und die Einrichtung geben. Sie müssen Movable Ink eine Reihe von Braze-API-Zugangsdaten zur Verfügung stellen, damit Da Vinci E-Mail-Deployments über die Messaging-API von Braze versenden kann.

Wenn die Verbindung hergestellt ist, wird Movable Ink:

- Mit dem Client und Braze zusammenarbeiten, um das Da Vinci-Konto der Marke einzurichten und erfolgreich mit Braze einzusetzen.
- Markenspezifische Konfigurationen erfassen, die auf Ihre Messaging-Anwendungsfälle abgestimmt sind.
- Umfassende Tests und Qualitätssicherungsmaßnahmen durchführen, um sicherzustellen, dass E-Mails wie vorgesehen zugestellt werden und alle Performance- und Betriebsstandards erfüllen.