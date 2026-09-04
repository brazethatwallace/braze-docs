---
nav_title: Mai
page_order: 8
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für Mai 2020."
---
# Mai 2020 {#may-2020}

## Google Tag Manager

Dokumentation und Beispiele für die Bereitstellung und Verwaltung des Android SDK von Braze mit [Google Tag Manager]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android) hinzugefügt.

## Neuer API-Endpunkt zum Sperren von E-Mail-Adressen {#new-blacklist-email-api-endpoint}

Sie können jetzt E-Mail-Adressen über die Braze API [sperren]({{site.baseurl}}/api/endpoints/email/post_blacklist). Wenn Sie eine E-Mail-Adresse sperren, wird die betreffende Nutzer:in von E-Mails abgemeldet und als Hard Bounce markiert.

## Änderung der API-Schlüssel für Braze-API-Endpunkte {#api-key-change-for-braze-api-endpoints}

Ab Mai 2020 hat Braze die Art und Weise geändert, wie API-Schlüssel gelesen werden, um die Sicherheit zu erhöhen. API-Schlüssel sollten jetzt als Anfrage-Header übergeben werden. Beispiele finden Sie auf den einzelnen Endpunktseiten unter **Example Request** sowie in der **API Key Explanation**.

Braze unterstützt weiterhin die Übergabe des `api_key` über den Body der Anfrage und die URL-Parameter, dies wird jedoch irgendwann eingestellt (TBD). **Aktualisieren Sie Ihre API-Aufrufe entsprechend.** Diese Änderungen wurden in [Postman](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro) aktualisiert.
{% details API Key Explanation %}
{% tabs %}
{% tab GET Request %}
Dieses Beispiel verwendet den Endpunkt `/email/hard_bounces`.

**Vorher: API-Schlüssel im Body der Anfrage**
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?api_key={YOUR_REST_API_KEY}&start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@example.com' \
```
**Jetzt: API-Schlüssel im Header**
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@example.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endtab %}
{% tab POST Request %}
Dieses Beispiel verwendet den Endpunkt `/user/track`.

**Vorher: API-Schlüssel im Body der Anfrage**
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--data-raw '{
	"api_key": YOUR-API-KEY-HERE ,
	"attributes": [
 	{
 	  "external_id":"user_id",
      "string_attribute": "sherman",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": ["banana", "apple"]
    }
    ]
}'
```
**Jetzt: API-Schlüssel im Header**
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
	"attributes": [
 	{
	  "external_id":"user_id",
      "string_attribute": "sherman",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": ["banana", "apple"]
    }
    ]
}'
```
{% endtab %}
{% endtabs %}
{% enddetails %}