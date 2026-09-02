---
nav_title: Multiplied Media
article_title: Multiplied Media
description: "Erfahren Sie, wie Sie Multiplied Media mit Braze verwenden, um personalisierte Bilder, GIFs und Videos per E-Mail, Push-Benachrichtigungen, In-App-Nachrichten, Content Cards und WhatsApp zu versenden."
alias: /partners/multiplied_media/
page_type: partner
search_tag: Partner
---

# Multiplied Media

> [Multiplied Media](https://multiplied.media) ist ein Kreativ- und Automatisierungsstudio, das Ihre CRM or Customer-Relationship-Management [-System] (CRM)-Daten nutzt, um personalisierte Bilder, GIFs und Videos zu erstellen – ein einzigartiges Asset für jede:n Kund:in. Die Integration von Multiplied Media und Braze ermöglicht es Ihnen, diese Medien per E-Mail, Push-Benachrichtigungen, In-App-Nachrichten, Content Cards und WhatsApp zu versenden.
>
> Multiplied Media ist ein Managed Service, kein Software-Tool. Das Multiplied-Media-Team übernimmt Konzept, Design, Animation, Datenanbindung und Rendering. Um diese Integration zu nutzen, fügen Sie eine Medien-URL mit einem [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)-Merge-Tag in Ihre Campaign oder Ihr Canvas ein.

_Diese Integration wird von Multiplied Media betreut._

## Über diese Integration {#about-this-integration}

Das Team von Multiplied Media arbeitet mit Ihnen vom ersten Konzept bis zum Launch zusammen. Sie entwerfen und animieren Medien für Ihre Marke, verknüpfen Ihre Daten und automatisieren das Rendering. Sie müssen keine neue Software erlernen.

Die Integration verbindet Ihre Braze-Daten – Kundenattribute und Segments – mit Multiplied Media. Multiplied Media rendert für jede:n Kund:in ein individuelles Medien-Asset und hostet es unter einer URL, die den Bezeichner der jeweiligen Person enthält. Sie referenzieren diese URL in Ihrer Braze-Nachricht mit einem Liquid-Merge-Tag. Jede:r Kund:in sieht dann das eigene Bild, GIF oder Video.

Die Integration unterstützt zwei Abläufe:

- **Batch-Campaigns:** Senden Sie Daten per CSV, S3 oder API. Multiplied Media rendert und hostet alle Medien vor dem Versand.
- **Realtime-Canvas-Automatisierungen:** Ein [Webhook]({{site.baseurl}}/user_guide/channels/webhooks)-Schritt in Ihrem Canvas triggert das Rendering, wenn ein:e Kund:in diesen Schritt erreicht.

## Anwendungsfälle {#use-cases}

- **Personalisierte Campaigns:** Produkteinführungen, „Wrapped“- und Jahresrückblick-Campaigns, saisonale Aktionen und personalisierte Datenvisualisierungen.
- **Always-on-Automatisierungen:** Willkommensflows, Onboarding, Meilenstein-Feiern, Rückgewinnungs-E-Mails, Warenkorb-Abbruch, Versandbenachrichtigungen, Wieder-verfügbar-Benachrichtigungen und Kundenbindungs-Updates.
- **Omnichannel-Journeys:** Ein Konzept, umgesetzt für jeden Kanal. Dieselben Kundendaten können zu einem E-Mail-Hero-Image, einem Push-Bild, einem In-App-Visual und einem WhatsApp-Video werden – so behält eine Journey über jeden Touchpoint hinweg eine einheitliche visuelle Identität.

## Voraussetzungen {#prerequisites}

Die Architektur von Multiplied Media unterstützt batch-basierte Campaigns über S3 oder API sowie Realtime-Canvas-Automatisierung über Webhooks. Durch die Vorab-Generierung und das Hosting einzigartiger Medien-Assets vor der Zustellung stellt Multiplied Media sicher, dass nahtlose 1:1-visuelle Erlebnisse bereitstehen, um sie mit Liquid-Tags oder angepassten Attributen in Ihre Templates einzufügen, sobald Ihre Nachricht getriggert wird.

Bevor Sie beginnen, stellen Sie sicher, dass Sie über Folgendes verfügen:

| Voraussetzung | Beschreibung |
| --- | --- |
| Aktives Multiplied-Media-Engagement | Multiplied Media ist ein Managed Service. Bevor Sie in Braze beginnen, definiert das Multiplied-Media-Team den Umfang Ihrer Campaign, gestaltet und erstellt Ihre Medien-Templates und richtet das Rendering ein. Um zu starten, besuchen Sie [multiplied.media](https://multiplied.media) oder senden Sie eine E-Mail an [hello@multiplied.media](mailto:hello@multiplied.media). |
| Datenquelle | Verbinden Sie Ihre Kundendaten mit Multiplied Media per CSV, S3, API oder Braze-Webhooks. Das Multiplied-Media-Team richtet dies während des Onboardings gemeinsam mit Ihnen ein. |
| Vereinheitlichender Bezeichner | Ihre Daten müssen einen Bezeichner enthalten, der zwischen Braze und Multiplied Media geteilt wird, z. B. `external_id`. Dieser Bezeichner bildet einen Teil der Medien-URL jeder Kund:in, und Ihre Braze-Nachricht referenziert ihn mit Liquid. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Multiplied Media mit Braze verwenden {#use-multiplied-media-with-braze}

Multiplied Media entwirft, erstellt und rendert Ihre personalisierten Medien und hilft Ihnen, Ihre Daten zu verknüpfen. Die folgenden Schritte beschreiben, was in Braze noch zu tun ist.

### Schritt 1: Bestätigen Sie, dass Ihre Medien bereit sind {#step-1-confirm-your-media-is-ready}

Vor dem Start bestätigt das Multiplied-Media-Team, dass Ihre Medien gerendert (Batch-Campaigns) oder dass Ihr Rendering-Endpunkt live ist (Realtime-Canvas-Flows). Anschließend erhalten Sie die Medien-URL Ihrer Campaign. Zum Beispiel:

{% raw %}
```
https://cdn.multiplied.media/yourbrand/campaign-name/{{${user_id}}}.gif
```
{% endraw %}

Der Bezeichner im URL-Pfad ist der gemeinsame Bezeichner, der bei der Einrichtung vereinbart wurde.

### Schritt 2: URL in Ihre Campaign oder Ihren Canvas einfügen {#step-2-insert-the-url-into-your-campaign-or-canvas}

Fügen Sie die Multiplied-Media-URL – mit dem Liquid-Merge-Tag – in das Feld für Ihren Kanal ein:

- **E-Mail:** Die Bildquelle in Ihrem E-Mail-Template.
- **Push-Benachrichtigungen:** Das Bildfeld Ihrer Push-Nachricht.
- **In-App-Nachrichten und Content Cards:** Das Medienfeld.
- **WhatsApp:** Das Medien-Header-Feld.

Für Realtime-Canvas-Automatisierungen fügen Sie den Multiplied-Media-Webhook-Schritt (der während des Onboardings mit Ihnen eingerichtet wurde) zusammen mit einem Delay-Knoten vor Ihrem Nachrichtenschritt hinzu. So wird sichergestellt, dass die Medien für jede Kund:in vor der Zustellung gerendert werden.

### Schritt 3: Vorschau, Test und Start {#step-3-preview-test-and-launch}

Verwenden Sie Braze-Vorschauen und Testversendungen, um zu bestätigen, dass der Liquid-Tag korrekt aufgelöst wird und dass jede:r Testnutzer:in ihre bzw. seine eigenen Medien sieht. Das Multiplied-Media-Team prüft die Testversendungen gemeinsam mit Ihnen vor dem Start.

## Hinweise {#considerations}

- Jedes Medien-Asset ist für jede:n Kund:in einzigartig. Wenn ein:e Kund:in nicht in der verbundenen Datenquelle vorhanden ist, wird über die URL eine Standard-Version (Fallback) des Mediums bereitgestellt. Multiplied Media gestaltet den Fallback als Teil jedes Engagements.
- Multiplied Media rendert und hostet Assets vor der Zustellung – sie werden nicht zum Öffnungszeitpunkt gerendert. Das Medium wird beim Öffnen sofort geladen und zeigt die Kundendaten zum Zeitpunkt des Renderings an. Wenn die Daten zum Sendezeitpunkt aktuell sein müssen – beispielsweise in getriggerten Canvas-Flows – verwenden Sie den Realtime-Webhook-Schritt.
- Bei geplanten Batch-Campaigns müssen Ihre Daten Multiplied Media vor dem Sendezeitpunkt erreichen, damit alle Assets gerendert werden können. Ihr Multiplied-Media-Team vereinbart den Stichtag während des Setups mit Ihnen.

## Fehlerbehebung {#troubleshooting}

Multiplied Media ist ein Managed Service, daher ist Ihr Multiplied-Media-Team Ihre erste Anlaufstelle für Support. Kontaktieren Sie das Team unter [hello@multiplied.media](mailto:hello@multiplied.media).

Wenn Ihr dynamisches Bild nicht angezeigt wird, finden Sie in der folgenden Tabelle mögliche Lösungen.

| Problem | Lösung |
| --- | --- |
| Dynamisches Bild wird nicht angezeigt | Bestätigen Sie, dass der Liquid-Tag in der URL mit dem bei der Einrichtung vereinbarten einheitlichen Bezeichner übereinstimmt (z. B. `user_id` im Vergleich zu einem angepassten Attribut). Bestätigen Sie, dass die Kund:in in der verbundenen Datenquelle existiert. Wenn der Bezeichner aufgelöst wird, aber kein personalisiertes Asset vorhanden ist, wird das Fallback-Medium angezeigt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fehlerbehebung" }