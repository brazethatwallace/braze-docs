---
nav_title: Yotpo
article_title: Yotpo
alias: /partners/yotpo/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Yotpo, einer führenden E-Commerce-Marketing-Plattform, die Tausenden von zukunftsorientierten Marken hilft, das Wachstum im Direktvertrieb an Verbraucher:innen zu beschleunigen."
page_type: partner
search_tag: Partner
---

# Yotpo

> [Yotpo](https://www.yotpo.com/), die führende E-Commerce-Marketing-Plattform, hilft Tausenden von zukunftsorientierten Marken, das Wachstum im Direktvertrieb an Verbraucher:innen zu beschleunigen. Yotpos Einzelplattform-Ansatz integriert datengestützte Lösungen für Bewertungen, Loyalität, SMS-Marketing und vieles mehr und versetzt Marken in die Lage, intelligentere Kundenerlebnisse mit höherer Conversion-Rate zu schaffen.

_Diese Integration wird von Yotpo gepflegt._

## Über die Integration {#about-the-integration}

Mit der Integration von Braze und Yotpo können Sie in E-Mails und anderen Kommunikationskanälen innerhalb von Braze dynamisch Sternebewertungen, Top-Rezensionen und visuelle, von Nutzer:innen erstellte Inhalte (UGC) zu Produkten abrufen und anzeigen. Sie können auch Daten zur Kundentreue in E-Mails und andere Kommunikationsmethoden einbeziehen, um eine personalisierte Interaktion zu schaffen, die den Umsatz und die Loyalität steigert.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Yotpo-Konto | Ein Yotpo-Konto ist erforderlich, um die Vorteile dieser Partnerschaft zu nutzen. |
| Yotpo-Bewertungen-API-Schlüssel | Diese API wird im Connected-Content-Code-Snippet implementiert.<br><br>Weitere Informationen finden Sie unter [Finden Sie Ihren Yotpo-App-Schlüssel und geheimen Schlüssel](https://support.yotpo.com/en/article/finding-your-yotpo-app-key-and-secret-key). |
| Yotpo-Loyalitäts-API-Schlüssel | Dieser API-Schlüssel und der weltweit eindeutige Bezeichner (GUID) werden im Connected-Content-Code-Snippet implementiert.<br><br>Weitere Informationen finden Sie unter [Finden Sie Ihren Treue- und Empfehlungs-API-Schlüssel und GUID](https://support.yotpo.com/en/article/finding-your-loyalty-referrals-api-key-and-guid)|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

Bevor Sie fortfahren, vergewissern Sie sich, dass die Yotpo-Produkt-ID mit der `product_id` übereinstimmt, die dynamisch von Braze abgerufen wird. Dies ist ein Pflichtfeld, damit die Integration funktioniert.

Um Ihre Yotpo-Produkt-ID zu finden, führen Sie die folgenden Schritte aus:

1. Gehen Sie auf die Website Ihres Shops.
2. Öffnen Sie die Produktseite.
3. Rechtsklicken Sie und wählen Sie **Untersuchen** aus.
4. Drücken Sie <kbd>Strg</kbd> + <kbd>F</kbd> und suchen Sie im Code nach `yotpo-main`. Die Variable `data-product ID` und ihr Wert erscheinen im Yotpo-Div.

![Untersuchen und nach „yotpo-main“ suchen, um die Variable „data-product ID“ zu finden]({% image_buster /assets/img/yotpo/image1.png %})

## Integration

Um Yotpo und Braze zu integrieren, führen Sie die folgenden Schritte durch:

1. Gehen Sie zu Ihrem Braze-Dashboard.
2. Klicken Sie auf der Seite **Campaigns** auf **Create Campaign** und wählen Sie **Email** aus.
3. Wählen Sie Ihr bevorzugtes Template aus.
4. Klicken Sie auf **Edit email body** und fügen Sie das entsprechende [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)-Snippet für Ihren Anwendungsfall hinzu:
    - [Sternebewertung und Anzahl der Bewertungen eines Produkts anzeigen](#star-review-count)
    - [Eine aktuelle 5-Sterne-Bewertung für ein Produkt anzeigen](#five-star-review)
    - [Visuellen UGC nach Produkt anzeigen](#visual-ugc)
    - [Treueguthaben einer geschäftskunden in einer E-Mail anzeigen](#loyalty-balance)

### Sternebewertung und Anzahl der Bewertungen eines Produkts anzeigen {#star-review-count}

Verwenden Sie dieses Snippet, um die öffentliche Durchschnittsbewertung und die Gesamtanzahl der Bewertungen für ein Produkt anzuzeigen, das in der E-Mail enthalten ist:

{% raw %}
```liquid
{% connected_content https://api.yotpo.com/products/<YOTPO-API-KEY>/{{event_properties.${product_id}}}/bottomline :save result %}

{% if {{result.response.bottomline.average_score}} != 0 %}

The average rating for this product is:

{{result.response.bottomline.average_score}}/5, based on {{result.response.bottomline.total_reviews}} reviews.

{% else %}
{% endif %}
```
{% endraw %}

Ersetzen Sie `<YOTPO-API-KEY>` durch Ihren Yotpo-Bewertungen-API-Schlüssel. Die `product_id` wird dynamisch von Braze bezogen. Damit die Integration funktioniert, muss die `product_id` in Braze mit der Produkt-ID in Yotpo übereinstimmen (in der Regel die übergeordnete E-Commerce-Produkt-ID).

![YOTPO-API-KEY durch Ihren Yotpo-Bewertungen-API-Schlüssel ersetzen]({% image_buster /assets/img/yotpo/image2.png %})

### Eine aktuelle 5-Sterne-Bewertung für ein Produkt anzeigen {#five-star-review}

Verwenden Sie dieses Snippet, um eine Top-Rezension (veröffentlicht) für ein bestimmtes Produkt anzuzeigen, das in der E-Mail enthalten ist:

{% raw %}
```liquid
{% connected_content https://api.yotpo.com/v1/widget/<YOTPO-API-KEY>/products/{{event_properties.${product_id}}}/reviews.json?per_page=50&star=5&sort=votes_up :save result %}

{% if {{result.response.reviews[0].score}} == 5 %}

Recent 5 Star Review for this product:

{{result.response.reviews[0].content}}

{% else %}
{% endif %}
```
{% endraw %}

Ersetzen Sie `<YOTPO-API-KEY>` durch Ihren Yotpo-Bewertungen-API-Schlüssel. Die `product_id` wird dynamisch von Braze bezogen. Damit die Integration funktioniert, muss die `product_id` in Braze mit der Produkt-ID in Yotpo übereinstimmen (in der Regel die übergeordnete E-Commerce-Produkt-ID).

So sieht das Snippet in Ihrem E-Mail-Editor aus:

![Beispiel für einen E-Mail-Editor mit einem Snippet für aktuelle 5-Sterne-Bewertungen]({% image_buster /assets/img/yotpo/image3.png %})

### Visuellen UGC nach Produkt anzeigen {#visual-ugc}

Verwenden Sie dieses Snippet, um getaggte und veröffentlichte Yotpo-Bilder abzurufen und sie anstelle des Stockbildes oder als zusätzliche Galerie in Ihre E-Mails einzufügen:

{% raw %}
```liquid

{% connected_content https://api.yotpo.com/v1/widget/<YOTPO-API-KEY>/albums/product/{{event_properties.${product_id}}}?per_page=1 :save result %}

{% if {{result.response.images[0].tagged_products[0].image_url}} != null %}

The Visual content of the product:

<img src="{{result.response.images[0].tagged_products[0].image_url}}" border="0" width="200" height="200" alt="" />

{% else %}

Image return NULL

{% endif %}
```
{% endraw %}

Ersetzen Sie `<YOTPO-API-KEY>` durch Ihren Yotpo-Bewertungen-API-Schlüssel. Die `product_id` wird dynamisch von Braze bezogen. Damit die Integration funktioniert, muss die `product_id` in Braze mit der Produkt-ID in Yotpo übereinstimmen (in der Regel die übergeordnete E-Commerce-Produkt-ID).

Das Snippet sieht dann etwa so aus:

![Beispiel für einen E-Mail-Editor mit einem Snippet von Bildern, die in Yotpo veröffentlicht wurden]({% image_buster /assets/img/yotpo/image4.png %})

### Treueguthaben einer geschäftskunden in einer E-Mail anzeigen {#loyalty-balance}

Verwenden Sie dieses Snippet, um den Treuepunkte-Kontostand einer geschäftskunden abzurufen und in Ihrem E-Mail-Messaging zu verwenden:

{% raw %}
```liquid
{% connected_content

https://loyalty.yotpo.com/api/v2/customers?customer_email=**{{${email_address}}}**
:method get
:headers {
    "x-guid": "<YOTPO-LOYALTY-GUID>",
    "x-api-key": "<YOTPO-LOYALTY-API-KEY>"
        }
:content_type application/json
:save publication
%}

You have {{publication.points_balance}} points

Only {{publication.vip_tier_upgrade_requirements.points_needed}} more points to become part of our VIP Tier!
```
{% endraw %}

Ersetzen Sie `<YOTPO-LOYALTY-GUID>` und `<YOTPO-LOYALTY-API-KEY>` durch Ihre Yotpo-Loyalitäts-Zugangsdaten. Die `email_address` wird dynamisch von Braze bezogen. Damit die Integration funktioniert, muss die E-Mail die E-Mail-Adresse der geschäftskunden sein, die die E-Mail erhält.

Das Snippet sieht dann etwa so aus:

![Beispiel für einen E-Mail-Editor mit einem Snippet des Treueguthabens einer Kund:in]({% image_buster /assets/img/yotpo/image5.png %})

## Häufig gestellte Fragen {#faq}

### Was ist, wenn ich keine 5-Sterne-Bewertung habe? {#what-if-i-dont-have-a-5-star-review}

Wenn Sie keine 5-Sterne-Bewertungen haben (z. B. wenn die Antwort des Endpunkts NULL für die 5-Sterne-Bewertung zurückgibt), wird kein Inhalt angezeigt.

### Was ist, wenn ich kein Bild für ein Produkt veröffentlicht habe? {#what-if-i-dont-have-an-image-published-for-a-product}

Wenn Sie keine Bilder für ein Produkt haben (z. B. wenn die Antwort des Endpunkts NULL für das Produktbild zurückgibt), wird kein Inhalt angezeigt.

### Kann ich das Aussehen anpassen oder andere Datenfelder von Yotpo beziehen? {#can-i-customize-the-look-and-feel-or-pull-other-data-fields-from-yotpo}

Ja! Weitere Datenpunkte und Anpassungsmöglichkeiten finden Sie unter [Einen API-Aufruf tätigen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/). Möglicherweise benötigen Sie dazu die Hilfe einer Entwickler:in.

{% alert note %}
Yotpo unterstützt keine angepassten Anforderungen, die über das hinausgehen, was in diesem Leitfaden beschrieben ist.
{% endalert %}