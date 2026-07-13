---
nav_title: Zapier
article_title: Zapier
alias: /partners/zapier/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Zapier, einem Internet-Automatisierungstool, das es Ihnen erlaubt, Daten zwischen Web-Apps auszutauschen und diese Informationen zur Automatisierung von Aktionen zu nutzen."
page_type: partner
search_tag: Partner

---
# Zapier-Integration

> [Zapier](https://zapier.com/) ist ein Internet-Tool für die Automatisierung, das es Ihnen erlaubt, Daten zwischen Web-Apps auszutauschen und diese Informationen dann zur Automatisierung von Aktionen zu verwenden.

Die Partnerschaft zwischen Braze und Zapier nutzt die Braze API und die Braze-[Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook#creating-a-webhook), um sich mit Drittanbieter-Anwendungen zu verbinden – wie Google Workplace, Slack, Salesforce, WordPress usw. – und verschiedene Aktionen zu automatisieren.

## Voraussetzungen {#prerequisites}

| Anforderungen | Beschreibung |
|---|---|
| Zapier-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Zapier-Konto. |
| Braze-REST-Endpunkt | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics#api-definitions) ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Im folgenden Zapier-Beispiel senden wir Informationen von WordPress an Braze über einen POST-Webhook. Diese Informationen können dann zur Erstellung eines Braze-Canvas verwendet werden.

### Schritt 1: Erstellen Sie einen Zapier-Trigger {#step-1-create-a-zapier-trigger}

In der Terminologie von Zapier ist ein „Zap“ ein automatisierter Workflow, der Ihre Apps und Dienste miteinander verbindet. Der erste Teil eines Zaps besteht darin, einen Trigger zu bestimmen. Nachdem Ihr Zap aktiviert wurde, führt Zapier automatisch die entsprechenden Aktionen aus, sobald Ihr Trigger erkannt wird.

Anhand unseres WordPress-Beispiels richten wir in der Zapier-Plattform unseren Zap so ein, dass er triggert, wenn ein neuer WordPress-Beitrag hinzugefügt wird, und wählen als **Post Status** und **Post Type** die Optionen **Published** und **Posts** aus.

![Wählen Sie in der Zapier-Plattform innerhalb eines Zaps den Trigger aus: „neuer Kommentar“, „beliebiger Webhook“ oder „neuer Beitrag“. In diesem Beispiel ist „neuer Beitrag“ ausgewählt.][5]

![Konfigurieren Sie in der Zapier-Plattform innerhalb eines Zaps den Trigger, indem Sie den gewünschten Beitragsstatus und Beitragstyp auswählen. In diesem Beispiel sind „Published“ und „Posts“ ausgewählt.][6]

### Schritt 2: Einen Aktions-Webhook hinzufügen {#step-2-add-an-action-webhook}

Definieren Sie als Nächstes die Zap-Aktion. Wenn Ihr Zap aktiviert ist und Ihr Trigger erkannt wird, wird die Aktion automatisch ausgeführt.

Um unser Beispiel fortzusetzen, möchten wir eine POST-Anfrage als JSON an einen Braze-Endpunkt senden. Wählen Sie dazu unter **Apps** die Option **Webhooks** aus.

![Zapier-Apps-Schritt mit ausgewählter Webhooks-Option für die Aktion.]({% image_buster /assets/img_archive/zapier3.png %})

### Schritt 3: Braze-POST einrichten {#step-3-set-up-braze-post}

Wenn Sie Ihren Webhook einrichten, verwenden Sie die folgenden Einstellungen und geben Sie Ihren Braze-REST-Endpunkt in der Webhook-URL an. Wenn Sie fertig sind, wählen Sie **Publish**.

- **Method**: POST
- **Webhook URL**: `https://rest.iad-01.braze.com/canvas/trigger/send`
- **Data Pass-Through**: False
- **Unflatten**: No
- **Anfrage-Header**:
  - **Content-Type**: application/json
  - **Authorization**: Bearer YOUR-API-KEY
- **Data**:

```json
{
  "canvas_id": "your_canvas_identifier",
  "recipients": [
    {
      "external_user_id": "external_user_identifier",
      "context":{
        "string_property": "Your example string",
        "example_integer_property": 1
      }
    }
  ]
}
```

![Zapier-Webhook-Konfiguration mit Braze-Endpunkt, Headern und Payload-Feldern.]({% image_buster /assets/img/zapier.png %}){: style="max-width:70%;"}

### Schritt 4: Erstellen Sie eine Braze-Campaign {#step-4-create-a-braze-campaign}

Sobald Sie Ihren Zap erfolgreich eingerichtet haben, können Sie Ihre Braze-Campaigns oder Canvases mit WordPress-Daten anpassen, indem Sie die Informationen in Ihren Nachrichten mit Liquid formatieren.

## Zapier mit dem Endpunkt `/users/track` verwenden {#using-zapier-with-the-userstrack-endpoint}

Um Daten an den Braze-Endpunkt [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) zu senden (zum Beispiel bei Verwendung eines Triggers wie **New or Updated Spreadsheet Row** in Google Sheets), verwenden Sie **Webhooks by Zapier** mit einer **Custom Request** – verwenden Sie nicht die Standard-Aktion **POST**. Die Standard-POST-Aktion formatiert die Anfrage auf eine Weise, die nicht mit dem Endpunkt `/users/track` kompatibel ist.

1. Wählen Sie in Zapier Ihren Trigger aus (zum Beispiel **New or Updated Spreadsheet Row** in Google Sheets).
2. Wählen Sie als Aktion **Webhooks by Zapier** und dann **Custom Request** (nicht POST).
3. Setzen Sie **Method** auf POST, geben Sie Ihre Braze-REST-Endpunkt-URL ein (zum Beispiel `https://rest.iad-01.braze.com/users/track`) und formatieren Sie den Anfrage-Body mit doppelten Anführungszeichen um jedes Element, wie Sie es in Postman oder einem API-Aufruf tun würden. Ordnen Sie Felder aus Ihrem Trigger (zum Beispiel Tabellenspalten) den entsprechenden Stellen im JSON-Body zu.
4. Fügen Sie die erforderlichen Header hinzu:
   - **Content-Type**: `application/json`
   - **Authorization**: `Bearer YOUR-REST-API-KEY` (verwenden Sie Ihren Braze-REST-API-Schlüssel ohne Klammern oder Anführungszeichen)
5. Testen Sie den Schritt und aktivieren Sie Ihren Zap.

[5]: {% image_buster /assets/img_archive/zapier1.png %}
[6]: {% image_buster /assets/img_archive/zapier2.png %}