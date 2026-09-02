---
nav_title: Contentsquare
article_title: Contentsquare
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Contentsquare, einer Analytics-Plattform für digitale Erlebnisse, die es Ihnen erlaubt, die Relevanz und die Konversionsraten Ihrer Campaigns zu verbessern, indem Sie Nachrichten auf der Grundlage der digitalen Erlebnisse Ihrer Kund:innen ausrichten."
alias: /partners/contentsquare/
page_type: partner
search_tag: Partner

---

# Contentsquare

> [Contentsquare](https://contentsquare.com/) ist eine Analytics-Plattform für digitale Erlebnisse, die ein noch nie dagewesenes Verständnis für das Kundenerlebnis ermöglicht.

_Diese Integration wird von Contentsquare gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Contentsquare ermöglicht es Ihnen, Live-Signale (Betrug, Frustrationssignale usw.) als angepasste Events in Braze zu senden. Nutzen Sie die Insights von Contentsquare, um die Relevanz Ihrer Campaigns und die Konversionsraten zu verbessern, indem Sie Nachrichten auf der Grundlage der digitalen Erlebnisse und der Körpersprache Ihrer Kund:innen gezielt einsetzen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Contentsquare-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Contentsquare-Konto. |
| Braze Representational State Transfer-API-Schlüssel | Ein Braze Representational State Transfer-API-Schlüssel mit `users.track`-Berechtigungen. Um einen neuen Schlüssel im Braze-Dashboard zu erstellen, gehen Sie zu **Settings** > **API Keys**. |
| Braze REST-Endpunkt | [Ihre REST-Endpunkt-URL]({% image_buster /assets/img/contentsquare_custom_events.png %}). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

Einige häufige Anwendungsfälle für Braze und Contentsquare sind:
- Hyper-Personalisierung von Nachrichten auf der Grundlage der Kundenabsicht, indem Daten über Kundenerlebnisse in Braze eingebunden werden.
- Retargeting von Kund:innen auf der Grundlage ihres digitalen Verhaltens, ihres Zögerns, ihrer Frustration und ihrer Absicht.
- Identifizieren Sie schlechte Erfahrungen innerhalb von Contentsquare und gewinnen Sie Kund:innen mit gezielten Nachrichten und Angeboten zur Bindung zurück.
- Gewinnen Sie gefährdete Kund:innen zurück, indem Sie relevantere und einfühlsamere Nachrichten zur richtigen Zeit und am richtigen Ort versenden.

## Integration

Um Contentsquare in Braze zu integrieren, müssen Sie die Installation einer „Live Signals“-Integration aus dem Contentsquare-Integrationskatalog anfragen:

1. Klicken Sie in Contentsquare im Menü **Settings** auf **Console**. Dadurch werden Sie zu dem Projekt weitergeleitet, an dem Sie gerade arbeiten.
2. Gehen Sie auf der Seite **Projects** auf den Tab **Integrations** und klicken Sie auf den Button **+ Add integration**.
3. Suchen Sie im Integrationskatalog die Integration **Live Signals** und klicken Sie auf **Add**. Das Contentsquare-Team wird sich dann mit Ihnen in Verbindung setzen, um das Code-Snippet so zu konfigurieren, dass es Live-Signale an Braze sendet.
4. Contentsquare wird nun Ihre Integration bearbeiten. Der Indikatortext wird aktualisiert, nachdem die Integration abgeschlossen ist.

Weitere Informationen finden Sie unter [Anfrage für die Integration von Contentsquare](https://uxanalyser.zendesk.com/hc/en-gb/articles/4405613239186).

## Verwendung dieser Integration {#using-this-integration}

Sobald die Integration abgeschlossen ist, stehen Ihnen angepasste Events von Contentsquare zur Verwendung in Ihren Campaigns und Canvase zur Verfügung. Sie können unter **Data Settings** > **Custom Events** überprüfen, welche Events an Braze gesendet werden.

![Contentsquare-Live-Signals-Daten im Braze-Tab „Angepasste Events“]({% image_buster /assets/img/contentsquare_custom_events.png %})