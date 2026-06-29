---
nav_title: Remerge
article_title: Remerge
alias: /partners/remerge/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Remerge, einer speziell für Retargeting in großem Maßstab entwickelten App, die Ihnen Tools zur effizienten Segmentierung von App-Zielgruppen und zum Retargeting von Nutzer:innen an die Hand gibt."
page_type: partner
search_tag: Partner

---

# Remerge

> [Remerge](https://www.remerge.io/) wurde speziell für das Retargeting von Apps in großem Umfang entwickelt und gibt Ihnen Tools an die Hand, mit denen Sie App-Zielgruppen effizient segmentieren und Nutzer:innen erneut ansprechen können.

_Diese Integration wird von Remerge gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Remerge hilft Ihnen, robuste, kanalübergreifende Lebenszyklus-Marketingkampagnen zu entwickeln, indem Nutzerdaten über Webhook-Ereignisse an Remerge gesendet werden, um das Retargeting von Nutzer:innen über deren mobile Demand-Side-Plattform zu unterstützen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Remerge-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, ist ein Remerge-Konto erforderlich. |
| Remerge-Webhook-Schlüssel | Dieser Schlüssel wird von Remerge bereitgestellt. |
| Android-App-ID | Ihr eindeutiger Braze-Anwendungsbezeichner für Android (z. B. „com.example“). |
| iOS-App-ID | Ihr eindeutiger Braze-Anwendungsbezeichner für iOS (z. B. „012345678“). |
| IDFA-Erfassung im Braze SDK aktivieren | Die IDFA-Erfassung ist im Braze SDK optional und standardmäßig deaktiviert. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

### 1. Schritt: Erstellen Sie Ihr Braze-Webhook-Template {#step-1-create-your-braze-webhook-template}

Um ein Remerge-Webhook-Template für zukünftige Campaigns oder Canvases zu erstellen, navigieren Sie in der Braze-Plattform zu **Content** > **Webhook**. Wählen Sie dann **Create webhook template** aus.


Wenn Sie eine einmalige Remerge-Webhook-Campaign erstellen oder ein bestehendes Template verwenden möchten, wählen Sie bei der Erstellung einer neuen Campaign **Webhook** in Braze aus.

Füllen Sie in Ihrem neuen Webhook-Template die folgenden Felder aus:
- **Request Body**: Raw Text
- **Webhook URL**:
{% raw %}
```liquid
{% assign event_name = 'your_remerge_event_name' %}
{% assign android_app_id = 'your_android_app_id' %}
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'event_name','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

https://remerge.events/event?partner=braze&app_id=\{% if most_recently_used_device.${idfa} == blank %}android_app_id{% else %}iOS_app_id{% endif %}&key=1cs3p12k&ts='now' | date: '%s' }}&{% if {{most_recently_used_device.${idfa} == blank%}aaid=custom_attribute.${aaid}{% else %}idfa=most_recently_used_device.${idfa{%endif%}&event=event_name&non_app_event=true&data=json | url_param_escape

{% if most_recently_used_device.${idfa} == blank and custom_attribute.${aaid} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```
{% endraw %}

In der Webhook-URL müssen Sie:
- Die `https://remerge.events/event`-API verwenden, um Ihre Webhook-Ereignisse zu senden.
- Den Ereignisnamen festlegen. Dieser Name erscheint in Ihrem [remerge.io](https://www.remerge.io/)-Dashboard.
- Den eindeutigen Anwendungsbezeichner Ihrer App für Android (z. B. „com.example“) und iOS (z. B. „012345678“) an Remerge übergeben.
- Einen Schlüssel definieren; Remerge wird diesen bereitstellen.

![Die Webhook-URL und die Nachrichtenvorschau im Braze-Webhook-Builder.]({% image_buster /assets/img_archive/webhook_remerge_preview.png %})

{% alert important %}
Braze erfasst die Geräte-IDFA/AAID nicht automatisch, sodass Sie diese Werte selbst speichern müssen. Beachten Sie, dass Sie möglicherweise die Zustimmung der Nutzer:innen zur Erfassung dieser Daten benötigen.
{% endalert %}

#### Anfrage-Header und Methode {#request-headers-and-method}

Der Remerge-Webhook erfordert eine HTTP-Methode und einen Anfrage-Header.

- **HTTP Method**: GET
- **Request Headers**:
  - **Content-Type**: application/json

![Die Anfrage-Header, die HTTP-Methode und die Nachrichtenvorschau im Braze-Webhook-Builder.]({% image_buster /assets/img_archive/httpmethod_remerge.png %})

#### Anfragetext {#request-body}

Sie müssen für diesen Webhook keinen Anfragetext definieren.

## 2. Schritt: Vorschau Ihrer Anfrage {#step-2-preview-your-request}

Zeigen Sie eine Vorschau der Nachricht an, um sicherzustellen, dass die Anfrage für verschiedene Nutzer:innen korrekt dargestellt wird. Wir empfehlen, Vorschauen anzuzeigen und Testanfragen sowohl für Android- als auch für iOS-Nutzer:innen zu senden. Wenn die Anfrage erfolgreich ist, antwortet die API mit `HTTP 204`.

{% alert important %}
Denken Sie daran, Ihr Template zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Templates finden Sie in der Liste **Gespeicherte Webhook-Templates**, wenn Sie eine neue [Webhook-Campaign]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/) erstellen.
{% endalert %}