---
nav_title: Narvar
article_title: Narvar
description: "Erfahren Sie, wie Sie Narvar in Braze integrieren können."
alias: /partners/narvar/
page_type: partner
search_tag: Partner
---

# Narvar

> Narvar ist eine Post-Purchase-Plattform, die die Loyalität der Kund:innen durch Sendungsverfolgung, Zustellungsupdates und Retourenmanagement stärkt. Die Integration von Braze und Narvar ermöglicht es Marken, die Benachrichtigungsereignisse von Narvar zu nutzen, um Nachrichten direkt von Braze zu Trigger or triggern or triggern und Kund:innen mit zeitnahen Updates auf dem Laufenden zu halten.

## Voraussetzungen {#prerequisites}

| Anforderung           | Beschreibung                                                                                   |
|-----------------------|-----------------------------------------------------------------------------------------------|
| Narvar-Konto        | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Narvar-Konto.                           |
| Braze-Representational State Transfer-API-Schlüssel    | Ein Braze-Representational State Transfer-API-Schlüssel mit der Berechtigung `messages.send`. Dieser kann im Braze-Dashboard unter **Settings** > **API Keys** erstellt werden.                                            |
| Braze-Representational State Transfer-Endpunkt   | [Ihre Representational State Transfer-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints), die von der URL Ihrer Braze-Instanz abhängt.         |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Unterstützte Features {#supported-features}

| Typ | Unterstützte Features |
|-------|----------|
| Benachrichtigungen | - Delivery Anticipation<br>- Carrier Delay<br>- Delivered Standard |
| Kanäle | Push-Benachrichtigungen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Unterstützte Features" }

{% alert note %}
Wenn Sie an weiteren Benachrichtigungsarten oder Kanälen interessiert sind, wenden Sie sich bitte an Ihren Braze- und Narvar-CSM or Customer-Success-Manager.
{% endalert %}

## Details zur Integration {#integration-details}

Für jedes Benachrichtigungsereignis initiiert Narvar eine Anfrage an den Braze-Endpunkt [`/messaging/send`]({{site.baseurl}}/api/endpoints/messaging/), um eine Push-Nachricht an alle Verbraucher:innen zuzustellen, die ihr Opt-in gegeben haben.

Narvar ist für die Konfiguration der Push-Benachrichtigungs-Payloads für jede Nachricht verantwortlich. Derzeit verfügt Narvar nicht über eine integrierte Design-Schnittstelle für Push-Benachrichtigungen. Das Team von Narvar wird daher mit Ihrem Team zusammenarbeiten, um die Anforderungen an die Payloads zu ermitteln und zu definieren. Diese Payloads können im gleichen Maße angepasst werden wie die, die über Ihr eigenes System gesendet werden, einschließlich der Unterstützung für variable Platzhalter für Inhalte wie z. B. Bestelldaten und Details zu Verbraucher:innen.

## Erste Schritte mit der Braze-Narvar-Integration {#getting-started-with-the-braze-narvar-integration}

1. **Kontaktieren Sie Ihren Narvar-CSM or Customer-Success-Manager**, um Ihr Interesse an der Integration zu bekunden.
2. **Bestimmen Sie Braze-Umgebungen** für Staging und Produktion.
3. **Generieren Sie einen API-Schlüssel** in Braze für die Verwendung durch Narvar.
4. **Erzeugen Sie Campaign-Schlüssel** nach Bedarf in Braze.
5. **Stellen Sie Narvar die API- und Campaign-Schlüssel bereit** – über einen sicheren, einmaligen Link.
6. **Teilen Sie die Details der Push-Benachrichtigungs-Payloads**, um die Einrichtung abzuschließen.