---
nav_title: mai
page_order: 8
noindex: true
page_type: update
description: "Cet article contient les notes de version de mai 2020."
---
# Mai 2020 {#may-2020}

## Google Tag Manager

Ajout de documentation et d'exemples sur le déploiement et la gestion du SDK Android de Braze à l'aide de [Google Tag Manager]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android).

## Nouvel endpoint d'API pour la mise en liste noire des e-mails {#new-blacklist-email-api-endpoint}

Vous pouvez désormais [mettre en liste noire]({{site.baseurl}}/api/endpoints/email/post_blacklist) des adresses e-mail via l'API de Braze. L'ajout d'une adresse e-mail à la liste noire entraîne le désabonnement de l'utilisateur des e-mails et le marque comme ayant subi un échec d'envoi définitif.

## Changement de clé API pour les endpoints de l'API Braze {#api-key-change-for-braze-api-endpoints}

En mai 2020, Braze a modifié la façon dont les clés API sont lues afin de renforcer la sécurité. Les clés API doivent désormais être transmises dans l'en-tête de la requête. Vous trouverez des exemples sur les pages des endpoints individuels sous la rubrique **Exemple de requête**, ainsi que dans l'**Explication de la clé API**.

Braze continuera à prendre en charge la transmission de `api_key` dans le corps de la requête et les paramètres d'URL, mais cette prise en charge sera abandonnée à terme (date à déterminer). **Mettez à jour vos appels API en conséquence.** Ces changements ont été mis à jour dans [Postman](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro).
{% details API Key Explanation %}
{% tabs %}
{% tab GET Request %}
Cet exemple utilise l'endpoint `/email/hard_bounces`.

**Avant : clé API dans le corps de la requête**
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?api_key={YOUR_REST_API_KEY}&start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@example.com' \
```
**Maintenant : clé API dans l'en-tête**
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@example.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endtab %}
{% tab POST Request %}
Cet exemple utilise l'endpoint `/user/track`.

**Avant : clé API dans le corps de la requête**
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
**Maintenant : clé API dans l'en-tête**
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