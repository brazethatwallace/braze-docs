---
nav_title: Variables locales de Contenu connecté
article_title: Variables locales de Contenu connecté
page_order: 1
description: "Cet article de référence explique comment utiliser et stocker les variables locales de Contenu connecté."
search_rank: 1
---

# Variables locales de Contenu connecté {#local-connected-content-variables}

> Cette page offre un aperçu des variables locales de Contenu connecté et explique comment les utiliser et les stocker.

Braze effectue une requête GET standard au moment de l'envoi vers l'endpoint spécifié dans la balise `connected_content`. Si l'endpoint renvoie du JSON, celui-ci est automatiquement analysé et stocké dans une variable appelée `connected`. Si l'endpoint renvoie du texte, celui-ci sera directement inséré dans le message à la place de la balise `connected_content`.

Si vous souhaitez enregistrer votre réponse dans une variable, il est recommandé de renvoyer des objets JSON. Et si vous souhaitez que la réponse du Contenu connecté remplace la balise par le texte, assurez-vous que la réponse n'est pas du JSON valide (tel que défini par [json.org](http://www.json.org)).

Vous pouvez également spécifier `:save your_variable_name` après l'URL pour enregistrer les données sous un autre nom. Par exemple, la balise `connected_content` suivante stockera la réponse dans une variable locale appelée `localweather` (vous pouvez enregistrer plusieurs variables JSON `connected_content`) :

{% raw %}
```js
{% connected_content https://www.metaweather.com/api/location/2459115/ :save localweather %}
```
{% endraw %}

Metaweather est une API météo gratuite qui utilise un identifiant « Where-on-Earth ID » pour renvoyer la météo d'une zone. Utilisez ce code uniquement à des fins de test et d'apprentissage.

La variable stockée n'est accessible que dans le champ qui contient la requête `connected_content`. Par exemple, si vous souhaitez utiliser la variable `localweather` à la fois dans le champ du message et dans le champ du titre, vous devez effectuer la requête `connected_content` dans les deux champs.

Les requêtes GET sont généralement mises en cache par défaut, avec quelques exceptions (comme les URL contenant des attributs utilisateur à haute cardinalité, `:no_cache`, ou les corps de réponse supérieurs à 1 Mo). Lorsque des requêtes GET identiques apparaissent dans plusieurs champs, Braze réutilise la réponse mise en cache au lieu d'appeler à nouveau l'endpoint. Pour plus de détails sur le comportement de mise en cache, consultez [Mise en cache des réponses]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses).

Les appels de Contenu connecté effectués via HTTP POST ne sont pas mis en cache par défaut. Pour mettre en cache les réponses POST, ajoutez `:cache_max_age` à la balise. Consultez [Paramètres de cache par défaut]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses#default-cache-settings).

## Analyse du JSON {#json-parsing}

Le Contenu connecté interprète tout résultat au format JSON dans une variable locale lorsque vous spécifiez `:save`. Par exemple, un endpoint de Contenu connecté lié à la météo renvoie l'objet JSON suivant, que vous stockez dans une variable locale `localweather` en spécifiant `:save localweather`.
{% raw %}

```js
{
  "consolidated_weather": [
    {
      "id": 5.8143475362693e+15,
      "weather_state_name": "Clear",
      "weather_state_abbr": "c",
      "wind_direction_compass": "WSW",
      "created": "2017-06-12T14:14:46.268110Z",
      "applicable_date": "2017-06-12",
      "min_temp": 22.511666666667,
      "max_temp": 31.963333333333,
      "the_temp": 27.803333333333,
      "wind_speed": 6.8884690250312,
      "wind_direction": 251.62921994166,
      "air_pressure": 1021.335,
      "humidity": 50,
      "visibility": 14.945530601288,
      "predictability": 68
    },
    .
    .
    .
    "title": "New York",
    "location_type": "City",
    "woeid": 2459115,
    "latt_long": "40.71455,-74.007118",
    "timezone": "US\/Eastern"
  }
```

Vous pouvez vérifier s'il pleut ou non en référençant `{{localweather.consolidated_weather[0].weather_state_name}}`, qui, utilisé sur cet objet, renverrait `Clear`. Si vous souhaitez également personnaliser avec le nom de l'emplacement résultant, `{{localweather.title}}` renvoie `New York`.
{% endraw %}

L'image suivante illustre le type de coloration syntaxique que vous devriez voir dans le tableau de bord si vous avez correctement configuré les choses. Elle montre également comment vous pourriez exploiter l'exemple de requête `connected_content` !

{% raw %}
```liquid
{% connected_content https://www.metaweather.com/api/location/search/?query={{custom_attribute.${customCity}}} :save locationjson %}
{% connected_content https://www.metaweather.com/api/location/{{locationjson[0].woeid}}/ :save localweather %}

{% if {{localweather.consolidated_weather[0].weather_state_name}} == 'Rain' %}
It's raining! Grab an umbrella!
{% elsif {{localweather.consolidated_weather[0].weather_state_name}} == 'Clouds' %}
No sunscreen needed :)
{% else %}
Enjoy the weather!
{% endif %}
```
{% endraw %}

Si l'API répondait avec {%raw%}`{{localweather.consolidated_weather[0].weather_state_name}}`{%endraw%} renvoyant `Rain`, l'utilisateur recevrait alors cette notification push.

![Notification push avec le message « It's raining! Grab an umbrella! »]({% image_buster /assets/img_archive/connected_weather_push2.png %} "Connected Content Push Usage Example"){:style="max-width:50%" }

{% multi_lang_include connected_content/sections.md section='default behavior' %}

## HTTP POST

{% multi_lang_include connected_content/sections.md section='http post' %}

### Fournir un payload JSON {#providing-json-body}

Si vous souhaitez fournir votre propre payload JSON, vous pouvez l'écrire en ligne s'il ne contient pas d'espaces. Si votre payload contient des espaces, vous devez utiliser une instruction assign ou capture. Autrement dit, les trois approches suivantes sont acceptables :

{% raw %}
##### En ligne : espaces non autorisés {#inline-spaces-not-allowed}

```js
{% connected_content https://example.com/api/endpoint :method post :body {"foo":"bar","baz":"{{1|plus:1}}"} :content_type application/json %}
```

##### Corps dans une instruction capture : espaces autorisés {#body-in-a-capture-statement-spaces-allowed}

```js
{% capture postbody %}
{"foo": "bar", "baz": "{{ 1 | plus: 1 }}"}
{% endcapture %}
{% connected_content https://example.com/api/endpoint :method post :body {{postbody}} :content_type application/json %}
```
{% endraw %}

{% raw %}
```js
{% capture postbody %}
{
"ids":[ca_57832,ca_75869],"include":{"attributes":{"withKey":["daily_deals"]}}
}
{% endcapture %}

{% connected_content
    https://example.com/api/endpoint
    :method post
    :headers {
      "Content-Type": "application/json"
  }
  :body {{postbody}}
  :save result
%}
```
{% endraw %}

{% raw %}
##### Corps dans une instruction assign : espaces autorisés {#body-in-an-assign-statement-spaces-allowed}

```js
{% assign postbody = '{"foo":"bar", "baz": "2"}' %}
{% connected_content https://example.com/api/endpoint :method post :body {{postbody}} :content_type application/json %}
```
{% endraw %}

## Codes de statut HTTP {#http-status-codes}

Vous pouvez utiliser le statut HTTP d'un appel de Contenu connecté en l'enregistrant d'abord en tant que variable locale, puis en utilisant la clé `__http_status_code__`. Par exemple :

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :save result %}
{% if result.__http_status_code__ != 200 %}
  {% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert important %}
Cette clé ne sera automatiquement ajoutée à l'objet de Contenu connecté que si l'endpoint renvoie un objet JSON valide et une réponse `2XX`. Si l'endpoint renvoie un tableau ou un autre type, cette clé ne pourra pas être automatiquement définie dans la réponse.
{% endalert %}


[16]: [success@braze.com](mailto:success@braze.com)