---
nav_title: "Anwendungsfall: Einen Braze-zu-Braze-Webhook erstellen"
article_title: "Anwendungsfall: Einen Braze-zu-Braze-Webhook erstellen"
page_order: 2
channel:
  - webhooks
description: "Dieser Referenzartikel behandelt, wann Sie die Nutzeraktualisierung im Vergleich zu Braze-zu-Braze-Webhooks verwenden sollten und wie Sie einen Braze-zu-Braze-Webhook erstellen."

---

# Einen Braze-zu-Braze-Webhook erstellen {#create-a-braze-to-braze-webhook}

> Braze-zu-Braze-Webhooks ermöglichen es Ihnen, die [Braze REST API]({{site.baseurl}}/api/basics) innerhalb von Braze über einen [Webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) in einer [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) oder einem [Canvas]({{site.baseurl}}/user_guide/messaging/canvas) aufzurufen. Verwenden Sie dies für Orchestrierungsaufgaben wie das Triggern eines [API-getriggerten Canvas]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases). Zum Aktualisieren von [Nutzerattributen]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), [angepassten Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events) oder [Käufen]({{site.baseurl}}/user_guide/data/activation/events/purchase_events) aus Canvas heraus verwenden Sie stattdessen die [Nutzeraktualisierung]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update). Sie ist für Änderungen am Nutzerprofil konzipiert und verarbeitet Updates effizienter.

Um das Beste aus diesem Artikel herauszuholen, sollten Sie mit der [Funktionsweise von Webhooks]({{site.baseurl}}/user_guide/channels/webhooks) und dem [Erstellen eines Webhooks]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) in Braze vertraut sein.

## „An Ziel senden“ zum Triggern eines weiteren Canvas verwenden {#use-send-to-destination-for-triggering-another-canvas}

Um einen zweiten Canvas aus einem Canvas heraus zu triggern, verwenden Sie [An Ziel senden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination) anstelle eines Braze-zu-Braze-Webhooks. Diese Canvas-Komponente wurde speziell für die Verknüpfung von Canvas-Journeys entwickelt und bietet eine einfachere, effizientere Möglichkeit, Nutzer:innen von einem Canvas in einen anderen zu senden.

„An Ziel senden“ prüft Nutzer:innen anhand der Entry- und Zielgruppenkriterien des Ziel-Canvas, wenn sie den Schritt erreichen, ohne dass eine Webhook-Konfiguration oder API-Schlüssel erforderlich sind. Nutzer:innen, die die Kriterien erfüllen, treten in den Ziel-Canvas ein und können ihre Journey im Quell-Canvas fortsetzen, wenn weitere Schritte folgen.

{% alert tip %}
Fügen Sie [An Ziel senden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination) zu Ihrem Canvas hinzu, um Nutzer:innen ohne Konfiguration von Webhooks oder API-Aufrufen in eine andere Canvas-Journey zu senden.
{% endalert %}

## Nutzeraktualisierung für Nutzerdatenänderungen verwenden {#use-user-update-for-user-data-changes}

Um Nutzerprofile innerhalb eines Canvas zu aktualisieren – einschließlich der Änderung [angepasster Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), der Aufzeichnung [angepasster Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events) oder der Aufzeichnung von [Käufen]({{site.baseurl}}/user_guide/data/activation/events/purchase_events) – verwenden Sie die [Nutzeraktualisierung]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) anstelle eines Braze-zu-Braze-Webhooks.

Die Nutzeraktualisierung fasst mehrere Änderungen zusammen und sendet sie in Batches, was schneller ist als Webhooks. Sie ist einfacher einzurichten als ein Webhook und unterstützt komplexe Updates über den [erweiterten JSON-Composer]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#advanced-json-editor). Um beispielsweise zu zählen, wie oft Nutzer:innen eine Nachricht gesehen haben, verwenden Sie die [Inkrementieren-und-Dekrementieren-Funktion]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#increasing-and-decreasing-values) der Nutzeraktualisierung anstelle eines Braze-zu-Braze-Webhooks.

{% alert tip %}
Fügen Sie die [Nutzeraktualisierung]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) zu Ihrem Canvas hinzu, um Attribute, Events und Käufe von Nutzer:innen mithilfe eines JSON-Composers zu aktualisieren.
{% endalert %}

## Wann Sie einen Braze-zu-Braze-Webhook verwenden sollten {#when-to-use-a-braze-to-braze-webhook}

Die Nutzeraktualisierung kann nahezu alle Aufgaben eines Braze-zu-Braze-Webhooks für die Aktualisierung von Nutzerprofilen übernehmen. Für komplexe Updates, die über einfache angepasste Attribute hinausgehen, können Sie den [erweiterten JSON-Composer]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#advanced-json-editor) verwenden.

„An Ziel senden“ bietet eine einfachere Möglichkeit, einen zweiten Canvas aus einem Canvas heraus zu triggern, ohne eine Webhook-Konfiguration zu benötigen.

Sie können einen Braze-zu-Braze-Webhook verwenden, wenn Sie die [REST API]({{site.baseurl}}/api/basics) von Braze innerhalb von Braze für Szenarien aufrufen müssen, für die es keine dedizierte Canvas-Komponente gibt. Häufige Beispiele sind:

- Triggern einer [API-getriggerten Campaign]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) aus einem Canvas heraus
- Aufrufen anderer [Messaging-Endpunkte]({{site.baseurl}}/api/endpoints/messaging) für Orchestrierungsmuster, bei denen ein Workflow in Braze eine API aufrufen muss, für die es keine dedizierte Canvas-Komponente gibt

Für Nutzeraktualisierungen innerhalb von Canvas verwenden Sie die [Nutzeraktualisierung]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update). Zum Triggern eines weiteren Canvas verwenden Sie [An Ziel senden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination).

## Voraussetzungen {#prerequisites}

Um einen Braze-zu-Braze-Webhook zu erstellen, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key) mit Berechtigungen für den Endpunkt, den Sie erreichen möchten. Um beispielsweise einen API-getriggerten Canvas zu triggern, benötigen Sie einen API-Schlüssel mit der Berechtigung `canvas.trigger.send`.

## Ihren Braze-zu-Braze-Webhook einrichten {#setting-up-your-braze-to-braze-webhook}

Der allgemeine Workflow zum Erstellen eines Braze-zu-Braze-Webhooks umfasst die folgenden Schritte:

1. [Erstellen Sie einen Webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) als Campaign oder Canvas-Komponente.
2. Wählen Sie **Blank Template**.
3. Geben Sie im Tab **Verfassen** die **Webhook-URL** und den **Request Body** für Ihren API-Anwendungsfall an.
4. Geben Sie im Tab **Einstellungen** Ihre **HTTP-Methode** und **Anfrage-Header** gemäß den Anforderungen des Endpunkts an.
5. Konfigurieren Sie alle weiteren Zustellungseinstellungen (z. B. Triggern durch ein angepasstes Event) und erstellen Sie den Rest Ihrer Campaign oder Ihres Canvas.

## Einen zweiten Canvas aus einem initialen Canvas triggern {#trigger-a-second-canvas-from-an-initial-canvas}

In diesem Anwendungsfall erstellen Sie zwei Canvases und verwenden einen Braze-zu-Braze-Webhook, um den zweiten Canvas aus dem ersten zu triggern. Dies funktioniert wie ein Entry-Trigger, wenn Nutzer:innen einen bestimmten Punkt in einem anderen Canvas erreichen.

1. Beginnen Sie mit der Erstellung Ihres zweiten Canvas – dem Canvas, der von Ihrem initialen Canvas getriggert werden soll.
2. Wählen Sie als Canvas-**Entry-Zeitplan** die Option **API-Triggered**.
3. Notieren Sie sich Ihre **Canvas-ID**. Sie benötigen diese in einem späteren Schritt.
4. Erstellen Sie die weiteren Schritte Ihres zweiten Canvas und speichern Sie den Canvas.
5. Erstellen Sie abschließend Ihren ersten Canvas. Suchen Sie den Schritt, an dem Sie den zweiten Canvas triggern möchten, und erstellen Sie einen neuen Schritt mit einem Webhook.

Beachten Sie beim Konfigurieren Ihres Webhooks Folgendes:

- **Webhook-URL:** Ihre [REST-Endpunkt-URL]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) gefolgt von `/canvas/trigger/send`. Für die Instanz `US-06` wäre die URL beispielsweise `https://rest.iad-06.braze.com/canvas/trigger/send`.
- **Request Body:** Raw Text

### Anfrage-Header und Methode {#request-headers-and-method}

Braze erfordert einen HTTP-Header für die Autorisierung, der Ihren API-Schlüssel enthält, sowie einen weiteren, der Ihren Content-Typ deklariert.

- **Anfrage-Header:**
  - **Authorization:** `Bearer YOUR_API_KEY`
  - **Content-Type:** `application/json`
- **HTTP-Methode:** `POST`

Ersetzen Sie `YOUR_API_KEY` durch einen Braze-API-Schlüssel mit `canvas.trigger.send`-Berechtigungen. Sie können einen API-Schlüssel im Braze-Dashboard erstellen, indem Sie zu **Einstellungen** > **API-Schlüssel** navigieren.

![Anfrage-Header für den Webhook mit den Feldern „Authorization“ und „Content-Type“ im Braze-Dashboard.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Anfrage-Body {#request-body}

Fügen Sie Ihre `/canvas/trigger/send`-Anfrage in das Textfeld ein. Weitere Details finden Sie unter [Canvas-Nachrichten über API-getriggerte Zustellung senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases). Das Folgende ist ein Beispiel für den Anfrage-Body dieses Endpunkts, wobei `your_canvas_id` die Canvas-ID Ihres zweiten Canvas ist:

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

Wenn Nutzer:innen diesen Webhook-Schritt im ersten Canvas erreichen, triggert Braze den zweiten Canvas für diese Nutzer:innen über die API.

## Hinweise {#considerations}

- **Nutzeraktualisierungen:** Zum Aktualisieren von Nutzerprofilen aus Canvas heraus (Attribute, Events, Käufe) verwenden Sie die [Nutzeraktualisierung]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) anstelle von Braze-zu-Braze-Webhooks für bessere Effizienz und Kosteneffektivität.
- Braze-zu-Braze-Webhooks unterliegen den [Rate-Limits]({{site.baseurl}}/api/api_limits) der Endpunkte.
- Aktualisierungen am Nutzerprofil verbrauchen [Datenpunkte]({{site.baseurl}}/user_guide/data/infrastructure/data_points), die auf Ihren Gesamtverbrauch angerechnet werden, während das Triggern einer weiteren Nachricht über die Messaging-Endpunkte dies nicht tut.
- Um [anonyme Nutzer:innen]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#anonymous-user-profiles) anzusprechen, verwenden Sie `braze_id` anstelle von `external_id` im Anfrage-Body Ihres Webhooks.
- Sie können Ihren Braze-zu-Braze-Webhook als [Webhook-Template]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates) zur Wiederverwendung speichern.
- Sie können das [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) einsehen, um Webhook-Fehler anzuzeigen und zu beheben.