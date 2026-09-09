---
nav_title: "Anwendungsfall: Einen Braze-zu-Braze-Webhook erstellen"
article_title: "Anwendungsfall: Einen Braze-zu-Braze-Webhook erstellen"
page_order: 2
channel:
  - webhooks
description: "Dieser Referenzartikel behandelt, wann Sie die Nutzeraktualisierung im Vergleich zu Braze-zu-Braze-Webhooks verwenden sollten und wie Sie einen Braze-zu-Braze-Webhook erstellen."
---

# Einen Braze-zu-Braze-Webhook erstellen {#create-a-braze-to-braze-webhook}

> Braze-zu-Braze-Webhooks ermöglichen es Ihnen, die [Braze REST API]({{site.baseurl}}/api/basics) innerhalb von Braze über einen [Webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) in einer [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) oder einem [Canvas]({{site.baseurl}}/user_guide/messaging/canvas) aufzurufen. Verwenden Sie dies für Orchestrierungsaufgaben wie das Triggern eines [API-getriggerten Canvas]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases). Zum Aktualisieren von [Nutzerattributen]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), [angepassten Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events) oder [Käufen]({{site.baseurl}}/user_guide/data/activation/events/purchase_events) aus Canvas heraus verwenden Sie stattdessen die [Nutzeraktualisierung]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update). Sie ist für Änderungen am Kundenprofil konzipiert und verarbeitet Updates effizienter.

Um das Beste aus diesem Artikel herauszuholen, sollten Sie mit der [Funktionsweise von Webhooks]({{site.baseurl}}/user_guide/channels/webhooks) und dem [Erstellen eines Webhooks]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) in Braze vertraut sein.

## „An Ziel senden“ verwenden, um einen weiteren Canvas auszulösen {#use-send-to-destination-for-triggering-another-canvas}

Um einen zweiten Canvas aus einem Canvas heraus auszulösen, verwenden Sie [An Ziel senden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination) anstelle eines Braze-zu-Braze-Webhooks. Dieser Canvas-Schritt wurde speziell dafür entwickelt, Canvas-Journeys miteinander zu verbinden, und bietet eine einfachere, effizientere Möglichkeit, Nutzer:innen von einem Canvas in einen anderen zu senden.

„An Ziel senden“ prüft die Nutzer:innen anhand der Eintritts- und Zielgruppenkriterien des Ziel-Canvas, wenn sie den Schritt erreichen – ohne dass eine Webhook-Konfiguration oder API-Schlüssel erforderlich sind. Nutzer:innen, die die Kriterien erfüllen, treten in den Ziel-Canvas ein und können ihre Journey im Quell-Canvas fortsetzen, falls weitere Schritte folgen.

{% alert tip %}
Fügen Sie [An Ziel senden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination) zu Ihrem Canvas hinzu, um Nutzer:innen ohne Konfiguration von Webhooks oder API-Aufrufen in eine andere Canvas-Journey zu senden.
{% endalert %}

## User Update für Änderungen an Nutzerdaten verwenden {#use-user-update-for-user-data-changes}

Um Nutzerprofile innerhalb eines Canvas zu aktualisieren – einschließlich der Änderung [angepasster Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), der Erfassung [angepasster Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events) oder der Erfassung von [Käufen]({{site.baseurl}}/user_guide/data/activation/events/purchase_events) – verwenden Sie [User Update]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) anstelle eines Braze-zu-Braze-Webhooks.

User Update fasst mehrere Änderungen zusammen und sendet sie in Batches, was schneller ist als Webhooks. Die Einrichtung ist einfacher als bei einem Webhook und unterstützt komplexe Aktualisierungen über den [Advanced JSON Composer]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#advanced-json-editor). Um beispielsweise zu zählen, wie oft eine Nutzer:in eine Nachricht gesehen hat, verwenden Sie das [Inkrementierungs- und Dekrementierungs-Feature]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#increasing-and-decreasing-values) von User Update anstelle eines Braze-zu-Braze-Webhooks.

{% alert tip %}
Fügen Sie [User Update]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) zu Ihrem Canvas hinzu, um Attribute, Events und Käufe von Nutzer:innen mithilfe eines JSON Composers zu aktualisieren.
{% endalert %}

## Wann ein Braze-zu-Braze-Webhook verwendet werden sollte {#when-to-use-a-braze-to-braze-webhook}

User Update kann fast alle Aufgaben übernehmen, die ein Braze-zu-Braze-Webhook für die Aktualisierung von Nutzerprofilen bietet. Für komplexe Aktualisierungen, die über einfache angepasste Attribute hinausgehen, können Sie den [erweiterten JSON-Composer]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#advanced-json-editor) verwenden.

Send to Destination bietet eine einfachere Möglichkeit, einen zweiten Canvas innerhalb eines Canvas auszulösen, ohne eine Webhook-Konfiguration vornehmen zu müssen.

Sie können einen Braze-zu-Braze-Webhook verwenden, wenn Sie die Braze [REST API]({{site.baseurl}}/api/basics) innerhalb von Braze für Szenarien aufrufen müssen, für die es keinen dedizierten Canvas-Schritt gibt. Gängige Beispiele sind:

- Auslösen einer [API-getriggerten Campaign]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) aus einem Canvas
- Aufrufen anderer [Messaging-Endpunkte]({{site.baseurl}}/api/endpoints/messaging) für Orchestrierungsmuster, bei denen ein Workflow in Braze eine API aufrufen muss, für die es keinen dedizierten Canvas-Schritt gibt

Für Nutzeraktualisierungen innerhalb eines Canvas verwenden Sie [User Update]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update). Um einen weiteren Canvas auszulösen, verwenden Sie [Send to Destination]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination).

## Voraussetzungen {#prerequisites}

Um einen Braze-zu-Braze-Webhook zu erstellen, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics) mit Berechtigungen für den Endpunkt, den Sie erreichen möchten. Um beispielsweise ein API-getriggertes Canvas auszulösen, benötigen Sie einen API-Schlüssel mit der Berechtigung `canvas.trigger.send`.

## Einrichten Ihres Braze-zu-Braze-Webhooks {#setting-up-your-braze-to-braze-webhook}

Der allgemeine Workflow zum Erstellen eines Braze-zu-Braze-Webhooks umfasst die folgenden Schritte:

1. [Erstellen Sie einen Webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) als Campaign oder Canvas-Komponente.
2. Wählen Sie **Leeres Template** aus.
3. Geben Sie im Tab **Erstellen** die **Webhook-URL** und den **Anfrage-Body** für Ihren API-Anwendungsfall an.
4. Geben Sie im Tab **Einstellungen** die **HTTP-Methode** und die **Anfrage-Header** an, wie vom Endpunkt gefordert.
5. Konfigurieren Sie alle weiteren Zustellungseinstellungen (z. B. das Triggern durch ein angepasstes Event) und erstellen Sie den Rest Ihrer Campaign oder Ihres Canvas.

## Ein zweites Canvas über ein erstes Canvas triggern {#trigger-a-second-canvas-from-an-initial-canvas}

In diesem Anwendungsfall erstellen Sie zwei Canvases und verwenden einen Braze-zu-Braze-Webhook, um das zweite Canvas über das erste zu triggern. Dies funktioniert wie ein Entry-Trigger, wenn eine Nutzer:in einen bestimmten Punkt in einem anderen Canvas erreicht.

{% alert note %}
Der Trigger **Interact with Canvas-Schritt** ist nur für Campaigns verfügbar, nicht für aktionsbasierte Canvas-Eintritte. Wenn Sie ein Canvas auf Basis einer Nutzer:in triggern müssen, die einen bestimmten Schritt in einem anderen Canvas erreicht, verwenden Sie diesen Braze-zu-Braze-Webhook-Ansatz oder die Canvas-Komponente [Send to Destination]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination).
{% endalert %}

1. Erstellen Sie zunächst Ihr zweites Canvas – das Canvas, das durch Ihr erstes Canvas getriggert werden soll.
2. Wählen Sie für den **Entry Schedule** des Canvas **API-Triggered** aus.
3. Notieren Sie sich Ihre **Canvas ID**. Sie benötigen diese in einem späteren Schritt.
4. Erstellen Sie die weiteren Schritte Ihres zweiten Canvas und speichern Sie es anschließend.
5. Erstellen Sie zuletzt Ihr erstes Canvas. Suchen Sie den Schritt, an dem Sie das zweite Canvas triggern möchten, und erstellen Sie einen neuen Schritt mit einem Webhook.

Beachten Sie beim Konfigurieren Ihres Webhooks die folgenden Hinweise:

- **Webhook-URL:** Ihre [REST-Endpunkt-URL]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints), gefolgt von `/canvas/trigger/send`. Für die Instanz `US-06` wäre die URL beispielsweise `https://rest.iad-06.braze.com/canvas/trigger/send`.
- **Anfrage-Body:** Raw Text

### Anfrage-Header und Methode {#request-headers-and-method}

Braze erfordert einen HTTP-Header zur Autorisierung, der Ihren API-Schlüssel enthält, sowie einen weiteren, der den Content-Typ deklariert.

- **Anfrage-Header:**
  - **Authorization:** `Bearer YOUR_API_KEY`
  - **Content-Type:** `application/json`
- **HTTP-Methode:** `POST`

Ersetzen Sie `YOUR_API_KEY` durch einen Braze-API-Schlüssel, der über `canvas.trigger.send`-Berechtigungen verfügt. Sie können einen API-Schlüssel im Braze-Dashboard erstellen, indem Sie zu **Einstellungen** > **API-Schlüssel** navigieren.

![Anfrage-Header für den Webhook mit den Feldern „Authorization“ und „Content-Type“ im Braze-Dashboard.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Anfrage-Body {#request-body}

Fügen Sie Ihre `/canvas/trigger/send`-Anfrage in das Textfeld ein. Weitere Einzelheiten finden Sie unter [Canvas-Nachrichten über API-getriggerte Zustellung senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases). Das Folgende ist ein Beispiel für den Anfrage-Body dieses Endpunkts, wobei `your_canvas_id` die Canvas ID Ihres zweiten Canvas ist:

{% raw %}
```json
{
  "canvas_id": "your_canvas_id",
  "recipients": [
    {
      "external_user_id": "{{${user_id}}}"
    }
  ]
}
```
{% endraw %}

Wenn eine Nutzer:in diesen Webhook-Schritt im ersten Canvas erreicht, triggert Braze das zweite Canvas für diese Nutzer:in über die API.

## Überlegungen {#considerations}

- **Nutzer:innen-Aktualisierungen:** Für die Aktualisierung von Nutzerprofilen aus Canvas heraus (Attribute, Events, Käufe) verwenden Sie [User Update]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) anstelle von Braze-zu-Braze-Webhooks, da dies effizienter und kostengünstiger ist.
- Braze-zu-Braze-Webhooks unterliegen den [Rate-Limits]({{site.baseurl}}/api/api_limits) für Endpunkte.
- Aktualisierungen des Nutzerprofils verursachen [Datenpunkte]({{site.baseurl}}/user_guide/data/infrastructure/data_points), die auf Ihren Gesamtverbrauch angerechnet werden, während das Triggern einer weiteren Nachricht über die Messaging-Endpunkte dies nicht tut.
- Um [anonyme Nutzer:innen]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#anonymous-user-profiles) anzusprechen, verwenden Sie `braze_id` anstelle von `external_id` im Anfrage-Body Ihres Webhooks.
- Sie können Ihren Braze-zu-Braze-Webhook als [Webhook-Template]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates) zur Wiederverwendung speichern.
- Sie können das [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) einsehen, um Webhook-Fehler anzuzeigen und zu beheben.