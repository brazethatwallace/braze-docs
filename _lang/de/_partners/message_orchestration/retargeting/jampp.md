---
nav_title: Jampp
article_title: Jampp
alias: /partners/jampp/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Jampp, einer Performance-Marketing-Plattform für die Akquisition und das Retargeting von mobilen Kund:innen."
page_type: partner
search_tag: Partner

---

# Jampp

> [Jampp](https://www.jampp.com/) ist eine Performance-Marketing-Plattform für die Akquisition und das Retargeting von mobilen Kund:innen. Jampp kombiniert Verhaltensdaten mit prädiktiver und programmatischer Technologie, um Einnahmen für Werbetreibende zu generieren, indem persönliche, relevante Anzeigen geschaltet werden, die Verbraucher:innen zum ersten oder häufigeren Kauf inspirieren.

_Diese Integration wird von Jampp gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Jampp ermöglicht es Unternehmensnutzer:innen, Ereignisse über Braze-Webhook-Ereignisse mit Jampp zu synchronisieren. Dadurch können Kund:innen ihren Retargeting-Initiativen innerhalb ihres mobilen Werbe-Ökosystems reichhaltigere Datensätze hinzufügen.

Einige Beispiele, wann Sie Kund:innen mit einer Anzeige retargeten möchten:
- Wenn sich der Status des E-Mail- oder Push-Abos einer Kund:in ändert.
- Wie eine Kund:in mit einer Braze-Messaging-Kampagne interagiert hat.
- Wenn die Kund:in einen bestimmten Geofence getriggert hat.

## Voraussetzungen {#prerequisites}

Diese Integration unterstützt iOS- und Android-Apps.

| Anforderung | Beschreibung |
|---|---|
| Jampp-Konto | Um diese Partnerschaft nutzen zu können, ist ein [Jampp-Konto](https://www.jampp.com/) erforderlich. |
| Android-App-ID | Ihr eindeutiger Braze-Anwendungsbezeichner für Android (z. B. „com.example“). |
| iOS-App-ID | Ihr eindeutiger Braze-Anwendungsbezeichner für iOS (z. B. „012345678“). |
| Aktivierung der IDFA-Erfassung im Braze SDK or Software-Development-Kit | Die IDFA-Erfassung ist im Braze SDK or Software-Development-Kit optional und standardmäßig deaktiviert. |
| Erfassung der Google Advertising ID über ein angepasstes Attribut | Die Erfassung der Google Advertising ID ist für Kund:innen optional und kann als [angepasstes Attribut]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) erfasst werden.
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

### 1. Schritt: Erstellen Sie ein Webhook-Template in Braze {#step-1-create-a-webhook-template-in-braze}

Um ein Jampp-Webhook-Template zu erstellen, das Sie in zukünftigen Campaigns oder Canvase verwenden können, navigieren Sie im Braze-Dashboard zu **Content** > **Webhook**. Wählen Sie dann **Create webhook template** aus.

Wenn Sie eine einmalige Jampp-Webhook-Campaign erstellen oder ein bestehendes Template verwenden möchten, wählen Sie bei der Erstellung einer neuen Campaign **Webhook** in Braze aus.

Füllen Sie in Ihrem neuen Webhook-Template die folgenden Felder aus:
- **Request Body**: Rohtext
- **Webhook-URL**:
{% raw %}
```liquid
{% assign event_name = 'your_jampp_event_name' %}
{% assign android_app_id = 'your_android_app_id' %}
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'{{event_name}}','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

http://tracking.jampp.com/event?kind={{event_name}}&rnd={{rnd}}&app={% if {{most_recently_used_device.${idfa}}} == blank %}{{android_app_id}}{% else %}{{iOS_app_id}}{% endif %}&apple_ifa={{most_recently_used_device.${idfa}}}&google_advertising_id={{custom_attribute.${aaid}}}&user_agent={user-agent}&prtnr=braze

{% if {{most_recently_used_device.${idfa}}} == blank and {{custom_attribute.${aaid}}} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```
{% endraw %}

In der Webhook-URL müssen Sie:
- Den Namen des Ereignisses festlegen. Dieser Name wird in Ihrem Jampp-Dashboard angezeigt.
- Den eindeutigen Anwendungsbezeichner Ihrer App für Android (z. B. „com.example“) und iOS (z. B. „012345678“) übergeben.
- [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid) für das entsprechende angepasste Attribut einfügen, das Sie als Google Advertising ID tracken. Beachten Sie, dass die Google Advertising ID in diesem Beispiel als `aaid` aufgeführt ist, Sie diese jedoch durch den Namen des angepassten Attributs ersetzen müssen, den Ihre Entwickler:innen festgelegt haben.

![Die Webhook-URL und die Nachrichtenvorschau im Braze-Webhook-Builder.]({% image_buster /assets/img/jampp_webhook.png %})

{% alert important %}
Braze erfasst die Geräte-IDFA/AAID nicht automatisch, sodass Sie diese Werte selbst speichern müssen. Beachten Sie, dass Sie möglicherweise die Zustimmung der Nutzer:innen zur Erfassung dieser Daten benötigen.
{% endalert %}

#### Anfrage-Header und Methode {#request-headers-and-method}

Der Jampp-Webhook erfordert eine HTTP-Methode und einen Anfrage-Header.

- **HTTP-Methode**: GET
- **Anfrage-Header**:
  - **Content-Type**: application/json

![Die Anfrage-Header, die HTTP-Methode und die Nachrichtenvorschau im Braze-Webhook-Builder.]({% image_buster /assets/img/jampp_method.png %})

#### Anfragetext {#request-body}

Sie müssen für diesen Webhook keinen Anfragetext definieren.

### 2. Schritt: Vorschau Ihrer Anfrage {#step-2-preview-your-request}

Zeigen Sie eine Vorschau der Nachricht an, um sicherzustellen, dass die Anfrage für verschiedene Nutzer:innen korrekt dargestellt wird. Wir empfehlen, Testanfragen sowohl für Android- als auch für iOS-Nutzer:innen in der Vorschau anzuzeigen und zu versenden. Wenn die Anfrage erfolgreich ist, antwortet die API mit `HTTP 204`.

{% alert important %}
Denken Sie daran, Ihr Template zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Templates finden Sie in der Liste **Gespeicherte Webhook-Templates**, wenn Sie eine neue [Webhook-Campaign]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/) erstellen.
{% endalert %}