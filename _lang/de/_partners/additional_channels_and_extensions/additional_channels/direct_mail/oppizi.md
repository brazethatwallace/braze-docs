---
nav_title: Oppizi
article_title: Oppizi
alias: /partners/oppizi/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Oppizi."
page_type: partner
search_tag: Partner
---

# Oppizi

> [Oppizi](https://www.oppizi.com/) ist weltweit führend im Offline-Marketing und bietet Unternehmen eine Lösung aus einer Hand, um messbare, zielgerichtete Direkt-Mailing- und Flyer-Kampagnen durchzuführen.

_Diese Integration wird von Oppizi gepflegt._

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ------------------------------ | ----------------------------------------------------------------------------- |
| Oppizi-Konto | Um diese Integration zu nutzen, benötigen Sie ein aktives Oppizi-Konto. |
| Oppizi-API-Schlüssel | Zu finden in Ihrem Oppizi-Konto unter **Integrations** > **Braze**. |
| Oppizi-Direkt-Mailing-Workflow-ID | Erstellen Sie einen Workflow in Oppizi auf der Seite **Direct Mail Workflow**, um eine ID zu erhalten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

Mit der Oppizi-Integration können Sie:

* **Automatisierte Direkt-Mailing-Postkarten versenden** – mithilfe von Braze-Triggern, die mit den Webhook- und Direkt-Mailing-Workflows von Oppizi verbunden sind.
* **Schwellenwerte, Wellen und Limits konfigurieren** – in den Direkt-Mailing-Workflows von Oppizi, um den Versand Ihrer Kampagnen zu steuern.
* **Professionelle Postkarten entwerfen** – mit dem integrierten Design-Tool von Oppizi. Designkenntnisse sind nicht erforderlich.
* **Die Performance von Kampagnen in Echtzeit verfolgen** – mit dem Dashboard von Oppizi.

## Integration

### 1. Schritt: Generieren Sie Ihren Oppizi-API-Schlüssel {#step-1-generate-your-oppizi-api-key}

Um Ihr Webhook-Template in Braze zu verwenden, müssen Sie zunächst Ihren Oppizi-API-Schlüssel generieren.

1. Melden Sie sich bei Oppizi an.
2. Gehen Sie zu **Integrations** > **Braze**.
3. Generieren Sie Ihren API-Schlüssel.

Von dieser Seite aus können Sie Ihre Schlüssel nach Bedarf verwalten, widerrufen und erstellen.

### 2. Schritt: Erstellen Sie ein Braze-Webhook-Template {#step-2-create-a-braze-webhook-template}

Erstellen Sie als Nächstes ein Webhook-Template für Oppizi in Braze, das Sie in zukünftigen Campaigns oder Canvases verwenden können:

1. Gehen Sie in Braze zu **Content** > **Webhook**.
2. Wählen Sie **Create webhook template**.
3. Geben Sie einen Namen für das Template ein.
4. Füllen Sie in Ihrem Webhook-Template die folgenden Felder aus:

- **Webhook URL:** `https://webhooks.oppizi.com/events`
- **Request Body:** **Raw Text**

Für die Anfragemethode und die Header benötigt Oppizi eine HTTP-Methode sowie die folgenden HTTP-Header, die in das Template aufgenommen werden müssen. Füllen Sie die folgenden Felder aus:

- **HTTP Method:** POST
- **Request Headers:**
  - **Authorization:** `Bearer <oppiziAPIKey>`
  - **Content-Type:** `application/json`

![Ein Beispiel für den Oppizi-Webhook-Header in Braze.]({% image_buster /assets/img/oppizi/oppizi_braze_webhook_headers.png %})

In den **Request Body** müssen Sie das Feld **oppiziWorkflowID** aufnehmen. Diese ID wird bei der Erstellung eines Workflows in Oppizi generiert und wird benötigt, um anzugeben, zu welchem Direkt-Mailing-Workflow Ihre Empfänger:innen hinzugefügt werden sollen. Jeder Direkt-Mailing-Workflow in Oppizi hat eine eindeutige ID. Wenn Sie also ein Oppizi-Webhook-Template in Braze erstellen, stellen Sie sicher, dass Sie die Workflow-ID immer auf die richtige aktualisieren.

{% alert note %}
Überprüfen Sie, ob in Ihrem Braze-Konto die erforderlichen angepassten Attribute für die Postadressen Ihrer Empfänger:innen eingerichtet sind, da diese für den Versand von Direkt-Mailings erforderlich sind.
{% endalert %}

![Ein Beispiel für ein Oppizi-Webhook-Template in Braze.]({% image_buster /assets/img/oppizi/oppizi_braze_webhook_example.png %})

Im Folgenden finden Sie ein Beispiel für einen Anfragetext:

{% raw %}
```json
{
    "event" : "workflow.addRecipient",
    "oppiziWorkflowID" : "<oppiziWorkflowID>",
    "requestType" : "live",
    "recipient" : {
        "recipientID" : "{{${braze_id}}}",
        "firstName" : "{{${first_name}}}",
        "lastName" : "{{${last_name}}}",
        "address1" : "{{custom_attribute.${address1}}}",
        "address2" : "{{custom_attribute.${address2}}}",
        "city" : "{{custom_attribute.${city}}}",
        "country" : "{{${country}}}",
        "zipCode" : "{{custom_attribute.${zipCode}}}",
        "state" : "{{custom_attribute.${state}}}"
    }
}
```
{% endraw %}

### 3. Schritt: Erstellen Sie einen Direkt-Mailing-Workflow in Oppizi {#step-3-create-a-direct-mail-workflow-in-oppizi}

1. Gehen Sie in Oppizi zu **Direct Mail Workflow** > **Create workflow**.
2. Konfigurieren Sie die Workflow-Details, einschließlich Schwellenwerte, Wellen, Postkartenformat und Druckvorlagen.
3. Im Abschnitt „Webhook-Details“ finden Sie einen gebrauchsfertigen Anfragetext, einschließlich Ihrer Workflow-ID, den Sie direkt in Braze einfügen können.

### 4. Schritt: Vorschau und Test Ihrer Anfrage in Braze {#step-4-preview-and-test-your-request-in-braze}

Nachdem Sie Ihren Anfragetext mit der Workflow-ID von Oppizi hinzugefügt haben, führen Sie einen Test durch, um zu überprüfen, ob Ihre Einrichtung wie erwartet funktioniert.

Um den Test durchzuführen, ändern Sie `requestType` im Anfragetext von `live` auf `test`. Beachten Sie, dass dieser Schritt wichtig ist, um zu verhindern, dass Testempfänger:innen zu Ihrer Direkt-Mailing-Zielgruppe hinzugefügt werden.

Nachdem Sie die Tests abgeschlossen haben, ändern Sie `requestType` wieder auf `live` und speichern Sie Ihr Canvas. Jetzt sind Sie bereit, Ihre automatisierten Direkt-Mailing-Kampagnen zu starten.