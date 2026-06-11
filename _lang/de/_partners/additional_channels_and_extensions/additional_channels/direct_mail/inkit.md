---
nav_title: Inkit
article_title: Inkit
alias: /partners/inkit/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Inkit, die es Ihnen ermöglicht, Zeit und Aufwand zu sparen, indem Sie Ihre Direkt-Mailing-Campaigns automatisieren und Offline-Kund:innen wieder online bringen."
page_type: partner
search_tag: Partner

---

# Inkit

> [Inkit](https://www.inkit.com) und Braze ermöglichen es Unternehmen, Dokumente sicher zu erstellen und zu verteilen – sowohl digital als auch per Direkt-Mailing.

_Diese Integration wird von Inkit gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Inkit erlaubt es Ihnen, mit Braze-Webhooks Dokumente zu erstellen und diese direkt an Braze-Nutzer:innen zu versenden.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| Inkit-Konto | Um diese Partnerschaft zu nutzen, benötigen Sie ein [Inkit-Konto](https://www.inkit.com/). |
| Inkit API-Schlüssel<br><br>`<INKIT_API_TOKEN>` | Dieser Schlüssel befindet sich auf Ihrem [Inkit Dashboard](https://app.inkit.io/#/account/integrations) unter dem Tab **Development** und ermöglicht es Ihnen, Ihre Braze- und Inkit-Konten zu verbinden. |
| Inkit Template-ID<br><br>`<INKIT_TEMPLATE_ID>` | Nachdem Sie ein Template erstellt haben, können Sie die Template-ID aus dem Tab **Templates** kopieren, um sie in Ihrem Template in Braze zu verwenden.<br><br>Sie könnten zum Beispiel in der Inkit-Umgebung ein Template namens `invoice_template` mit der Template-ID `tmpl_3bDScFl9cwr3OAVR1RSdEC` erstellen. |
| HTTP-Header | Der HTTP-Header ist Teil der API-Anfrage, die Sie von Braze an Inkit senden. Darin enthalten ist Ihr Inkit API-Schlüssel zur Authentifizierung und Autorisierung von Aufrufen der Inkit API. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: Ein Inkit-Template erstellen {#step-1-create-an-inkit-template}

Erstellen Sie auf der Inkit-Plattform ein Template, das Sie in Ihrer Braze-Campaign in HTML, Word, PowerPoint, Excel oder PDF verwenden können. Lesen Sie die [Inkit-Dokumentation](https://docs.inkit.com/docs/create-a-template), um mehr zu erfahren.

### 2. Schritt: Ihr Braze-Webhook-Template erstellen {#step-2-create-your-braze-webhook-template}

Um ein Inkit-Webhook-Template zu erstellen, das Sie in zukünftigen Campaigns oder Canvases verwenden können, navigieren Sie auf der Braze-Plattform zu **Content** > **Webhook**. Wählen Sie dann **Create webhook template** aus.

Wenn Sie eine einmalige Inkit-Webhook-Campaign erstellen oder ein bestehendes Template verwenden möchten, wählen Sie bei der Erstellung einer neuen Campaign **Webhook** in Braze aus.

![Eine Auswahl der verfügbaren vorgefertigten Webhook-Templates im Tab „Webhook-Templates“ im Bereich „Templates und Medien“.]({% image_buster /assets/img/inkit-webhook-template.png %})

Sobald Sie das Inkit-Webhook-Template ausgewählt haben, sollten Sie Folgendes sehen:
- **Webhook-URL**: Leer
- **Anfragetext**: Rohtext

[Erstellen](https://docs.inkit.com/docs/set-up-a-webhook-to-an-event) Sie im Feld „Webhook-URL“ eine Inkit-Webhook-URL und geben Sie diese ein.

![Anfragetext-Code und Webhook-URL im Tab „Verfassen“ des Braze-Webhook-Builders.]({% image_buster /assets/img/inkit-integration.png %})

#### Anfrage-Header und Methode {#request-headers-and-method}

Inkit benötigt einen `HTTP Header` für die Autorisierung, einschließlich Ihres Inkit API-Schlüssels, der in Base64 kodiert ist. Das Folgende ist bereits als Schlüssel-Wert-Paar im Template enthalten, aber im Tab **Einstellungen** müssen Sie `<INKIT_API_TOKEN>` durch Ihren Inkit API-Schlüssel ersetzen.

{% raw %}
- **HTTP-Methode**: POST
- **Anfrage-Header**:
  - **Authorization**: Basic `{{ '<INKIT_API_TOKEN>' | base64_encode }}`
  - **Content-Type**: application/json
{% endraw %}

#### Anfragetext {#request-body}

Vergewissern Sie sich, dass Ihr Liquid die richtigen angepassten Attribute enthält, die mit den folgenden erforderlichen und optionalen Feldern verknüpft sind. Sie können auch angepasste Datenfelder zu jeder Anfrage hinzufügen.

```json
{% raw %}{
  "api_token": "<INKIT_API_TOKEN>",
  "template_id": "<INKIT_TEMPLATE_ID>",
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "email": "{{${email_address}}}",
  "company": "{{custom_attribute.${company_name}}}",
  "phone" : "{{${phone_number}}}",
  "address_line_1": "{{custom_attribute.${address}}}",
  "address_line_2": "{{custom_attribute.${address2}}}",
  "address_city": "{{${city}}}",
  "address_state": "{{custom_attribute.${state}}}",
  "address_zip": "{{custom_attribute.${zip}}}",
  "address_country": "{{${country}}}",
  "source" : "Braze"
}{% endraw %}
```

### 3. Schritt: Vorschau Ihrer Anfrage {#step-3-preview-your-request}

Ihr Rohtext wird automatisch hervorgehoben, wenn es sich um einen passenden Braze-Tag handelt. `street`, `unit`, `state` und `zip` müssen als [angepasste Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attributes) eingerichtet werden, um diesen Webhook zu senden.

Eine Vorschau Ihrer Anfrage finden Sie im Panel **Vorschau**. Alternativ können Sie zum Tab **Test** navigieren, wo Sie zufällige Nutzer:innen oder bestehende Nutzer:innen auswählen oder eigene Daten anpassen können, um Ihren Webhook zu testen.

{% alert important %}
Denken Sie daran, Ihr Template zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Templates finden Sie in der Liste **Gespeicherte Webhook-Templates**, wenn Sie eine neue [Webhook-Campaign]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/) erstellen.
{% endalert %}