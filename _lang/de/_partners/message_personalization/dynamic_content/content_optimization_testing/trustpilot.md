---
nav_title: Trustpilot
article_title: Trustpilot
description: "Auf dieser Seite erfahren Sie, wie Sie Trustpilot in Braze integrieren, Einladungen zu Bewertungen versenden und Nachrichten mit Insights aus Produktbewertungen personalisieren können."
alias: /partners/trustpilot/
page_type: partner
search_tag: Partner
---

# Trustpilot

> [Trustpilot](https://www.trustpilot.com/) ist eine Online-Bewertungsplattform, die es Kund:innen ermöglicht, Feedback zu teilen, und die es Ihnen erlaubt, Bewertungen zu verwalten und darauf zu antworten.

Auf dieser Seite finden Sie eine Schritt-für-Schritt-Anleitung für:

* Erstellen von Einladungen zu Bewertungen mit der Trustpilot-API „Create Invitation“
* Personalisierung von Nachrichten mit Produktbewertungen über die Produktbewertungs-API von Trustpilot

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung | Beschreibung |
| --- | --- |
| Ein Trustpilot-Konto | Sie benötigen ein Trustpilot-Konto mit Zugriff auf die API von Trustpilot. |
| Ein Trustpilot-Authentifizierungsschlüssel | Sie müssen einen API-Schlüssel einrichten und ein Access Token / Textbaustein anfordern. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: Trustpilot-API-Zugangsdaten abrufen {#step-1-get-your-trustpilot-api-credentials}

1. [Melden Sie sich bei Trustpilot an](https://app.contentful.com/login) mit Ihren Zugangsdaten.
2. Erstellen oder rufen Sie den API-Schlüssel und das Secret im Trustpilot-Dashboard ab, indem Sie zu **Integrations** > **Developers** > **APIs** navigieren. Wenn Sie noch keinen API-Schlüssel haben, erstellen Sie einen neuen:
   1. Gehen Sie zu **Application Name** > **Create Application**.
   2. Kopieren Sie Ihren API-Schlüssel und Ihr Secret, die zur Authentifizierung Ihrer Connected-Content-Anfragen verwendet werden.

## Trustpilot-Bewertungseinladungen versenden {#sending-trustpilot-review-invitations}

### 1. Schritt: Braze-Webhook-Campaign einrichten {#step-1-set-up-a-braze-webhook-campaign}

Richten Sie eine aktionsbasierte Braze-Webhook-Campaign ein, um die Trustpilot-APIs zu triggern und E-Mail-Bewertungseinladungen an Nutzer:innen zu senden. Sie könnten zum Beispiel eine Einladung zur Bewertung senden, nachdem Nutzer:innen eine Bestellung aufgegeben haben, mit den folgenden Webhook-Details:
   * [Webhook-URL](https://developers.trustpilot.com/invitation-api?_gl=1*1hxojlc*_ga*MjEzMDkzNjQ5NS4xNzMxNjgxOTQ0*_ga_3TEL80JZSG*MTczNjU0MzY0Ny45LjAuMTczNjU0MzY0Ny4wLjAuMA..#create-invitation(s)): `https://invitations-api.trustpilot.com/v1/private/business-units/{businessUnitId}/email-invitations`
   * Methode: POST
   * Fügen Sie die relevanten Kundeninformationen als Schlüssel-Wert-Paare hinzu.

### 2. Schritt: Access Token / Textbaustein abrufen {#step-2-retrieve-the-access-token}

1. Verwenden Sie [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/), um eine Anfrage an den [Authentifizierungs-Endpunkt von Trustpilot](https://documentation-apidocumentation.trustpilot.com/authentication?_gl=1*1hxojlc*_ga*MjEzMDkzNjQ5NS4xNzMxNjgxOTQ0*_ga_3TEL80JZSG*MTczNjU0MzY0Ny45LjAuMTczNjU0MzY0Ny4wLjAuMA..) zu stellen, um das Access Token / Textbaustein abzurufen.
2. Verwenden Sie den Grant-Typ **client_credentials** und geben Sie Ihren API-Schlüssel und Ihr Secret in einen Connected-Content-Tag ein, um ein Token / Textbaustein abzurufen. Die Connected-Content-Anfrage kann in den Anfrage-Header eingegeben werden. Der Connected-Content kann wie folgt aussehen:

{% raw %}

```liquid
{% connected_content
https://api.trustpilot.com/v1/oauth/oauth-business-users-for-applications/accesstoken
:method post
:headers {"Content-Type": "application/x-www-form-urlencoded", "Authorization": "Basic {{'API_KEY:API_SECRET' | base64_encode}}" }
:body grant_type=client_credentials
:save token
:retry
:cache_max_age 3600 %}

{{token.access_token}}

```

{% endraw %}

{: start="3"}
3. Fügen Sie das Access Token / Textbaustein in den Anfrage-Header Ihrer Webhook-Campaign ein.

{% alert tip %}
Ausführlichere Anweisungen finden Sie in der [Dokumentation von Trustpilot](https://support.trustpilot.com/hc/en-us/community/posts/11947443933074-Braze-Trustpilot-Setup-Instructions-for-triggering-API-invites).
{% endalert %}

## Nachrichten mit Insights aus Produktbewertungen personalisieren {#personalizing-messages-with-product-review-insights}

Führen Sie in Ihrer Braze-Campaign einen Connected-Content-Aufruf durch, um Daten vom Trustpilot-Endpunkt [Zusammenfassung der Produktbewertungen abrufen](https://developers.trustpilot.com/product-reviews-api#get-product-reviews-summary) ({% raw %}`https://api.trustpilot.com/v1/product-reviews/business-units/{businessUnitId}`{% endraw %}) anzufordern. Diese Methode ruft Produktbewertungen für bestimmte SKUs aus der Geschäftseinheit ab. Das folgende Beispiel gibt die spezifische Produkt-SKU an und filtert nach Bewertungen mit fünf Sternen.

{% raw %}
```liquid
{% connected_content https://api.trustpilot.com/v1/product-reviews/business-units/66ea0530xxxxxx/reviews?sku={{event_properties.${item_sku}}}&stars=5
   :method get
   :headers {"apikey": "xxxxx"}
   :content_type application/json :save result %}
```
{% endraw %}

![Connected-Content in einer E-Mail mit Liquid, um Informationen abzurufen.]({% image_buster /assets/img/trustpilot_connected_content_example.png %}){:style="max-width:38%;"}

Die Connected-Content-Anfrage gibt die Produktbewertungen zurück.

{% raw %}
```liquid
  {
   "productReviews": [
       {
           "id": "670d5810ba62e6b31de97de9",
           "createdAt": "2024-10-14T17:42:40.286Z",
           "stars": 5,
           "content": "Such a great toy truck, my kids really enjoy it! ",
           "consumer": {
               "id": "6176xxxx",
               "displayName": "Kevin Bob"
           },
           "language": "en",
           "attributeRatings": [],
           "attachments": [],
           "firstCompanyComment": null
       }
   ],
   "links": []
 ```
{% endraw %}

{: start="2"}
2. Verwenden Sie die Liquid-Syntax, um die relevanten Inhalte in Ihre Nachricht einzubinden. Um zum Beispiel den Inhalt der Produktbewertung abzurufen, verwenden Sie den Liquid-Tag {% raw %}`{{result.productReviews[0].content}}`{% endraw %}.

![Personalisierte E-Mail mit einer Bewertung eines Spielzeuglastwagens, den die Nutzer:innen in ihrem Warenkorb gelassen haben.]({% image_buster /assets/img/trustpilot_personalized_email.png %}){:style="max-width:38%;"}