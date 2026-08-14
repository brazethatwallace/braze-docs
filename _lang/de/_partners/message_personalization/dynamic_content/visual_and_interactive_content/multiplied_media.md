---
nav_title: Multiplied Media
article_title: Multiplied Media
description: "Erfahren Sie, wie Sie Multiplied Media mit Braze verwenden, um personalisierte Bilder, GIFs und Videos per E-Mail, Push-Benachrichtigungen, In-App-Nachrichten, Content Cards und WhatsApp zu versenden."
alias: /partners/multiplied_media/
page_type: partner
search_tag: Partner
---

# Multiplied Media

> [Multiplied Media](https://multiplied.media) ist ein Kreativ- und Automatisierungsstudio, das Ihre CRM-Daten nutzt, um personalisierte Bilder, GIFs und Videos zu erstellen – ein einzigartiges Asset für jede:n Kund:in. Die Integration von Multiplied Media und Braze ermöglicht es Ihnen, diese Medien per E-Mail, Push-Benachrichtigungen, In-App-Nachrichten, Content Cards und WhatsApp zu versenden.
>
> Multiplied Media ist ein Managed Service, kein Software-Tool. Das Multiplied-Media-Team übernimmt Konzept, Design, Animation, Datenanbindung und Rendering. Um diese Integration zu nutzen, fügen Sie eine Medien-URL mit einem [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid)-Merge-Tag in Ihre Campaign oder Ihr Canvas ein.

_Diese Integration wird von Multiplied Media betreut._

## Über diese Integration {#about-this-integration}

Das Multiplied-Media-Team arbeitet mit Ihnen vom ersten Konzept bis zum Launch. Es gestaltet und animiert Medien für Ihre Marke, verbindet Ihre Daten und automatisiert das Rendering. Sie müssen keine neue Software erlernen.

Die Integration verbindet Ihre Braze-Daten – Kundenattribute und Segmente – mit Multiplied Media. Multiplied Media rendert ein einzigartiges Medien-Asset für jede:n Kund:in und hostet es unter einer URL, die den Bezeichner dieser Person enthält. Sie referenzieren diese URL in Ihrer Braze-Nachricht mit einem Liquid-Merge-Tag. Jede:r Kund:in sieht dann das eigene Bild, GIF oder Video.

Die Integration unterstützt zwei Abläufe:

- **Batch-Campaigns:** Senden Sie Daten per CSV, S3 oder API. Multiplied Media rendert und hostet alle Medien vor dem Versand.
- **Realtime-Canvas-Automatisierungen:** Ein [Webhook]({{site.baseurl}}/user_guide/channels/webhooks)-Schritt in Ihrem Canvas löst das Rendering aus, wenn ein:e Kund:in diesen Schritt erreicht.

## Anwendungsfälle {#use-cases}

- **Personalisierte Campaigns:** Produktlaunches, „Wrapped“- und Jahresrückblick-Campaigns, saisonale Aktionen und persönliche Datenvisualisierungen.
- **Always-on-Automatisierungen:** Willkommensflows, Onboarding, Meilenstein-Feiern, Rückgewinnungs-E-Mails, Warenkorb-Abbruch, Versandbenachrichtigungen, Wieder-verfügbar-Hinweise und Kundenbindungs-Updates.
- **Omnichannel-Journeys:** Ein Konzept, gerendert für jeden Kanal. Dieselben Kundendaten können zu einem E-Mail-Hero-Image, einem Push-Bild, einem In-App-Visual und einem WhatsApp-Video werden – so behält eine Journey über jeden Touchpoint hinweg eine einheitliche visuelle Identität.

## Voraussetzungen {#prerequisites}

Die Multiplied-Media-Architektur unterstützt Batch-basierte Campaigns über S3 oder API sowie Realtime-Canvas-Automatisierungen über Webhooks. Durch das Vorab-Generieren und Hosten einzigartiger Medien-Assets vor der Zustellung stellt Multiplied Media sicher, dass nahtlose 1:1-visuelle Erlebnisse bereitstehen, um mit Liquid-Tags oder angepassten Attributen in Ihre Templates eingebunden zu werden, sobald Ihre Nachricht ausgelöst wird.

Stellen Sie vor dem Start sicher, dass Folgendes vorhanden ist:

| Voraussetzung | Beschreibung |
| --- | --- |
| Aktives Multiplied-Media-Engagement | Multiplied Media ist ein Managed Service. Bevor Sie in Braze beginnen, definiert das Multiplied-Media-Team den Umfang Ihrer Campaign, gestaltet und erstellt Ihre Medien-Templates und richtet das Rendering ein. Besuchen Sie zum Einstieg [multiplied.media](https://multiplied.media) oder schreiben Sie an [hello@multiplied.media](mailto:hello@multiplied.media). |
| Datenquelle | Verbinden Sie Ihre Kundendaten per CSV, S3, API oder Braze-Webhooks mit Multiplied Media. Das Multiplied-Media-Team richtet dies während des Onboardings gemeinsam mit Ihnen ein. |
| Gemeinsamer Bezeichner | Ihre Daten müssen einen Bezeichner enthalten, der zwischen Braze und Multiplied Media geteilt wird, z. B. `external_id`. Dieser Bezeichner ist Teil der Medien-URL jeder Person, und Ihre Braze-Nachricht referenziert ihn mit Liquid. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Multiplied Media mit Braze verwenden {#use-multiplied-media-with-braze}

Multiplied Media gestaltet, erstellt und rendert Ihre personalisierten Medien und hilft Ihnen bei der Datenanbindung. Die folgenden Schritte beschreiben, was in Braze noch zu tun ist.

### Schritt 1: Bestätigen Sie, dass Ihre Medien bereit sind {#step-1-confirm-your-media-is-ready}

Vor dem Launch bestätigt das Multiplied-Media-Team, dass Ihre Medien gerendert sind (Batch-Campaigns) oder dass Ihr Rendering-Endpunkt live ist (Realtime-Canvas-Flows). Anschließend stellt es Ihnen die Medien-URL Ihrer Campaign bereit. Zum Beispiel:

{% raw %}
```
https://cdn.multiplied.media/yourbrand/campaign-name/{{${user_id}}}.gif
```
{% endraw %}

Der Bezeichner im URL-Pfad ist der gemeinsame Bezeichner, der beim Setup vereinbart wurde.

### Schritt 2: URL in Ihre Campaign oder Ihr Canvas einfügen {#step-2-insert-the-url-into-your-campaign-or-canvas}

Fügen Sie die Multiplied-Media-URL – mit dem Liquid-Merge-Tag – in das entsprechende Feld Ihres Kanals ein:

- **E-Mail:** Die Bildquelle in Ihrem E-Mail-Template.
- **Push-Benachrichtigungen:** Das Bildfeld Ihrer Push-Nachricht.
- **In-App-Nachrichten und Content Cards:** Das Medienfeld.
- **WhatsApp:** Das Medien-Header-Feld.

Für Realtime-Canvas-Automatisierungen fügen Sie den Multiplied-Media-Webhook-Schritt (der während des Onboardings mit Ihnen eingerichtet wird) zusammen mit einem Delay-Node vor Ihrem Nachrichtenschritt hinzu. So wird sichergestellt, dass die Medien für jede:n Kund:in vor der Zustellung gerendert werden.

### Schritt 3: Vorschau anzeigen, testen und starten {#step-3-preview-test-and-launch}

Nutzen Sie Braze-Vorschauen und Testversendungen, um zu bestätigen, dass der Liquid-Tag aufgelöst wird und jede:r Testnutzer:in die eigenen Medien sieht. Das Multiplied-Media-Team prüft die Testversendungen gemeinsam mit Ihnen vor dem Launch.

## Hinweise {#considerations}

- Das Medien-Asset jeder Person ist einzigartig. Wenn ein:e Kund:in nicht in der verbundenen Datenquelle vorhanden ist, liefert die URL stattdessen eine Standard-Version (Fallback) der Medien. Multiplied Media gestaltet den Fallback als Teil jedes Engagements.
- Multiplied Media rendert und hostet Assets vor der Zustellung; es rendert sie nicht zum Öffnungszeitpunkt. Die Medien laden sofort beim Öffnen und zeigen die Kundendaten zum Zeitpunkt des Renderings. Wenn die Daten zum Sendezeitpunkt aktuell sein müssen – beispielsweise in getriggerten Canvas-Flows – verwenden Sie den Realtime-Webhook-Schritt.
- Bei geplanten Batch-Campaigns müssen Ihre Daten vor dem Sendezeitpunkt bei Multiplied Media eingehen, damit alle Assets gerendert werden können. Ihr Multiplied-Media-Team vereinbart den Stichtag während des Setups mit Ihnen.

## Fehlerbehebung {#troubleshooting}

Multiplied Media ist ein Managed Service, daher ist Ihr Multiplied-Media-Team Ihre erste Anlaufstelle für Support. Kontaktieren Sie es unter [hello@multiplied.media](mailto:hello@multiplied.media).

Ziehen Sie die folgende Tabelle heran, wenn Ihr dynamisches Bild nicht angezeigt wird.

| Problem | Lösung |
| --- | --- |
| Dynamisches Bild wird nicht angezeigt | Bestätigen Sie, dass der Liquid-Tag in der URL mit dem beim Setup vereinbarten gemeinsamen Bezeichner übereinstimmt (z. B. `user_id` im Vergleich zu einem angepassten Attribut). Bestätigen Sie, dass die Person in der verbundenen Datenquelle vorhanden ist. Wenn der Bezeichner aufgelöst wird, aber kein personalisiertes Asset existiert, wird das Fallback-Medium angezeigt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fehlerbehebung" }