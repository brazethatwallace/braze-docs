---
nav_title: SmarterSends
article_title: SmarterSends
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und SmarterSends, einer benutzerfreundlichen Schnittstelle, die für Nicht-Marketer entwickelt wurde, um markenkonforme E-Mail-Campaigns zu erstellen, zu planen und bereitzustellen."
alias: /partners/smartersends/
page_type: partner
search_tag: Partner
---

# SmarterSends

> [SmarterSends](https://smartersends.com) ermöglicht Personalisierung durch Marketing-Campaigns, die Unternehmen erstellen, zeitlich planen und einsetzen können, um die Einhaltung von Marken- und Rechtsvorschriften durchzusetzen und dabei die Kontrolle über die verwendeten Inhalte und Daten zu behalten.

_Diese Integration wird von SmarterSends gepflegt._

## Über die Integration {#about-the-integration}

Die Partnerschaft zwischen Braze und SmarterSends ermöglicht es Ihnen, die Leistungsfähigkeit von Braze mit den hyperlokalisierten Inhalten Ihrer verteilten Nutzer:innen zu kombinieren, um Ihre Marketing-Campaigns zu optimieren.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| SmarterSends-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [SmarterSends-Konto](https://smartersends.com). |
| Braze Representational State Transfer-API-Schlüssel | Ein Braze Representational State Transfer-API-Schlüssel mit diesen Berechtigungen: {::nomarkdown}<ul><li><code>users.track</code></li><li><code>users.export.ids</code></li><li><code>messages.schedule.create</code></li><li><code>messages.schedule.Update or aktualisieren</code></li> <li><code>messages.schedule.delete</code></li><li><code>sends.id.create</code></li><li><code>segments.list</code></li><li><code>segments.data_series</code></li><li><code>segments.details</code></li><li><code>sends.data_series</code></li></ul>{:/} Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. Für zusätzliche Sicherheit setzen Sie die IP-Adresse von SmarterSends auf die Allowlist (verfügbar in Ihrer Instanz). |
| Braze Representational State Transfer-Endpunkt | [Ihre Representational State Transfer-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Braze API-Campaign-ID | Die [Braze API-Campaign-ID]({{site.baseurl}}/api/api_campaigns/) ist der eindeutige Bezeichner für alle Campaigns, die über SmarterSends gesendet werden. Diese kann im Braze-Dashboard unter **Messaging** > **Campaigns** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

Mit der Integration von Braze und SmarterSends können Sie die Vorteile des verteilten Marketings nutzen, indem Sie Marketing-Campaigns über mehrere Kanäle und Standorte hinweg erstellen und durchführen. Diese Vorteile umfassen:

1. **Erhöhte Reichweite:** Nutzen Sie mehrere Kanäle und Standorte, um eine breitere Zielgruppe zu erreichen und Kund:innen an verschiedenen Standorten anzusprechen, was zu einer erhöhten Markenpräsenz führt.
2. **Gezieltes Messaging:** Maßgeschneidertes Messaging über verschiedene Kanäle und Standorte hinweg, um bei der lokalen Zielgruppe Anklang zu finden und die Kommunikation und das Engagement mit Kund:innen effektiver zu gestalten.
3. **Verbesserte Markenkonsistenz:** Das Messaging und Image Ihrer Marke über alle Kanäle und Standorte hinweg abzustimmen, ist wichtig für den Aufbau einer starken und wiedererkennbaren Marke.
4. **Bessere Insights:** Das Sammeln von Daten aus verschiedenen Kanälen und Standorten liefert wertvolle Insights über das Kundenverhalten und die Präferenzen, die zur Verfeinerung von Marketing-Strategien und -Taktiken sowohl auf lokaler als auch auf globaler Ebene genutzt werden können.
5. **Gesteigerte Effizienz:** Die Stärken verschiedener Kanäle und Standorte nutzen, was zu einer effizienteren Nutzung von Ressourcen führen kann, während gleichzeitig die gewünschten Marketingziele erreicht werden.

## Integration

### 1. Schritt: Einen Representational State Transfer-API-Schlüssel erstellen {#step-1-create-a-rest-api-key}

1. Gehen Sie in Braze zu **Einstellungen** > **API-Schlüssel** und klicken Sie auf **Neuen API-Schlüssel erstellen**.
2. Geben Sie einen Namen für den API-Schlüssel ein.
3. Wählen Sie die folgenden Berechtigungen für diesen Schlüssel aus, damit SmarterSends mit Ihrem Braze Workspace interagieren kann.
- `users.track`
- `users.export.ids`
- `messages.schedule.create`
- `messages.schedule.update`
- `messages.schedule.delete`
- `sends.id.create`
- `segments.list`
- `segments.data_series`
- `segments.details`
- `sends.data_series`
4. Fügen Sie die SmarterSends-IP-Adresse zum Abschnitt **Whitelist IPs** hinzu.
5. Klicken Sie auf **API-Schlüssel speichern**.
6. Kopieren Sie den API-Schlüssel mit den entsprechenden Berechtigungen und fügen Sie ihn in die Einstellungen des **Braze E-Mail-Anbieters** in SmarterSends ein.

### 2. Schritt: Eine Anwendungs-ID erstellen oder kopieren {#step-2-create-or-copy-an-application-id}

1. Gehen Sie in Ihrem Braze Workspace zu **Einstellungen** > **App Settings**.
2. Richten Sie eine neue App ein oder verwenden Sie die Anwendungs-ID einer bestehenden App in Ihrem Workspace. Beachten Sie, dass die Anwendungs-ID als **API Key** gekennzeichnet ist.
3. Kopieren Sie diese ID und fügen Sie sie in das Feld **App ID** in SmarterSends ein.

### 3. Schritt: Eine API-Campaign erstellen {#step-3-create-an-api-campaign}

Eine API-Campaign ermöglicht das Tracking von Metriken für alle SmarterSends-Mails innerhalb von Braze und erlaubt es SmarterSends, diese API-basierten Campaigns zu Trigger or triggern or triggern.

1. Erstellen Sie in Braze eine [API-Campaign]({{site.baseurl}}/api/api_campaigns/#create-a-new-campaign).
2. Klicken Sie auf **Email** unter **Select Message Channel**, um einen Messaging-Kanal hinzuzufügen und mit dem Tracking von Metriken zu beginnen.
3. Kopieren Sie dann die Campaign-ID aus Braze und fügen Sie sie in das Feld **Campaign ID** in SmarterSends ein.
4. Kopieren Sie die Nachrichtenvarianten-ID aus Braze und fügen Sie sie in das Feld **Message Variant ID** in SmarterSends ein. Dies ist die Standard-Nachrichten-ID, die verwendet wird, wenn Sie nicht für jede Gruppe in SmarterSends eine eigene Nachrichten-ID erstellen möchten.
5. Fügen Sie für jede Gruppe, die Sie in SmarterSends erstellen, eine Nachrichtenvariante zu Ihrer API-Campaign in Braze hinzu. Kopieren Sie dann die Nachrichtenvarianten-ID in die Nachrichtenvarianten-ID der Gruppe in SmarterSends.

{% alert tip %}
Erstellen Sie für jede Gruppe, die Sie in SmarterSends anlegen, eine Nachrichtenvarianten-ID, um die Metriken für die Sendungen jeder Gruppe separat in Ihrem Braze Workspace anzuzeigen. Dies kann hilfreich sein, um beim Erstellen von Berichten in Braze gruppenübergreifende Trends zu erkennen.
{% endalert %}

## Anpassung {#customization}

Jede SmarterSends-Instanz lässt sich vollständig an die Farben Ihres Markenlogos und Ihren angepassten Domain-Namen anpassen, wodurch eine vertraute Umgebung geschaffen wird. Darüber hinaus können Sie zur weiteren Personalisierung die Attribute und angepassten Attribute definieren, um Nutzer:innen in Campaigns auf der Grundlage der Segmente innerhalb Ihres Braze Workspace anzusprechen.