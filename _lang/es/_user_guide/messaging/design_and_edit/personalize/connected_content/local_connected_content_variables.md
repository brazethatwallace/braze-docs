---
nav_title: Variables locales de Contenido conectado
article_title: Variables locales de Contenido conectado
page_order: 1
description: "Este artículo de referencia explica cómo usar y almacenar variables locales de Contenido conectado."
search_rank: 1
---

# Variables locales de Contenido conectado {#local-connected-content-variables}

> Esta página ofrece un resumen de las variables locales de Contenido conectado y cómo usarlas y almacenarlas.

Braze realiza una solicitud GET estándar en el momento del envío al punto de conexión especificado dentro de la etiqueta `connected_content`. Si el punto de conexión devuelve JSON, se analiza automáticamente y se almacena en una variable llamada `connected`. Si el punto de conexión devuelve texto, se insertará directamente en el mensaje en lugar de la etiqueta `connected_content`.

Si quieres guardar tu respuesta en una variable, se recomienda devolver objetos JSON. Y si quieres que la respuesta de Contenido conectado reemplace la etiqueta con el texto, asegúrate de que la respuesta no sea JSON válido (según la definición de [json.org](http://www.json.org)).

También puedes especificar `:save your_variable_name` después de la URL para guardar los datos con otro nombre. Por ejemplo, la siguiente etiqueta `connected_content` almacenará la respuesta en una variable local llamada `localweather` (puedes guardar múltiples variables JSON de `connected_content`):

{% raw %}
```js
{% connected_content https://www.metaweather.com/api/location/2459115/ :save localweather %}
```
{% endraw %}

Metaweather es una API meteorológica gratuita que utiliza un "Where-on-Earth ID" para devolver el clima de una zona. Usa este código solo con fines de prueba y aprendizaje.

Solo se puede acceder a la variable almacenada dentro del campo que contiene la solicitud `connected_content`. Por ejemplo, si quieres usar la variable `localweather` tanto en el campo del mensaje como en el del título, debes hacer la solicitud `connected_content` en ambos campos.

Las solicitudes GET generalmente se almacenan en caché de forma predeterminada, con algunas excepciones (como URLs que incluyen atributos de usuario de alta cardinalidad, `:no_cache` o cuerpos de respuesta mayores de 1 MB). Cuando solicitudes GET idénticas aparecen en más de un campo, Braze reutiliza la respuesta almacenada en caché en lugar de llamar al punto de conexión de nuevo. Para más detalles sobre el comportamiento de la caché, consulta [Almacenamiento en caché de respuestas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses/).

Las llamadas de Contenido conectado realizadas a través de HTTP POST no se almacenan en caché de forma predeterminada. Para almacenar en caché las respuestas POST, añade `:cache_max_age` a la etiqueta. Consulta [Configuración predeterminada de caché]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses/#default-cache-settings).

## Análisis de JSON {#json-parsing}

Contenido conectado interpretará cualquier resultado con formato JSON como una variable local cuando especifiques `:save`. Por ejemplo, un punto de conexión de Contenido conectado relacionado con el clima devuelve el siguiente objeto JSON, que almacenas en una variable local `localweather` especificando `:save localweather`.
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

Puedes comprobar si está lloviendo o no haciendo referencia a `{{localweather.consolidated_weather[0].weather_state_name}}`, que si se usa con este objeto devolvería `Clear`. Si también quieres personalizar con el nombre de la ubicación resultante, `{{localweather.title}}` devuelve `New York`.
{% endraw %}

La siguiente imagen ilustra el tipo de resaltado de sintaxis que deberías ver en el dashboard si estás configurando las cosas correctamente. También muestra cómo podrías aprovechar la solicitud de ejemplo de `connected_content`.

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

Si la API respondiera con {%raw%}`{{localweather.consolidated_weather[0].weather_state_name}}`{%endraw%} devolviendo `Rain`, el usuario recibiría entonces esta notificación push.

![Notificación push con el mensaje "It's raining! Grab an umbrella!"]({% image_buster /assets/img_archive/connected_weather_push2.png %} "Connected Content Push Usage Example"){:style="max-width:50%" }

{% multi_lang_include connected_content.md section='default behavior' %}

## HTTP POST

{% multi_lang_include connected_content.md section='http post' %}

### Proporcionar un cuerpo JSON {#providing-json-body}

Si quieres proporcionar tu propio cuerpo JSON, puedes escribirlo en línea si no hay espacios. Si tu cuerpo tiene espacios, deberías usar una sentencia assign o capture. Es decir, cualquiera de estas tres opciones es aceptable:

{% raw %}
##### En línea: no se permiten espacios {#inline-spaces-not-allowed}

```js
{% connected_content https://example.com/api/endpoint :method post :body {"foo":"bar","baz":"{{1|plus:1}}"} :content_type application/json %}
```

##### Cuerpo en una sentencia capture: se permiten espacios {#body-in-a-capture-statement-spaces-allowed}

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
##### Cuerpo en una sentencia assign: se permiten espacios {#body-in-an-assign-statement-spaces-allowed}

```js
{% assign postbody = '{"foo":"bar", "baz": "2"}' %}
{% connected_content https://example.com/api/endpoint :method post :body {{postbody}} :content_type application/json %}
```
{% endraw %}

## Códigos de estado HTTP {#http-status-codes}

Puedes utilizar el estado HTTP de una llamada de Contenido conectado guardándolo primero como una variable local y luego usando la clave `__http_status_code__`. Por ejemplo:

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :save result %}
{% if result.__http_status_code__ != 200 %}
  {% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert important %}
Esta clave solo se añadirá automáticamente al objeto de Contenido conectado si el punto de conexión devuelve un objeto JSON válido y una respuesta `2XX`. Si el punto de conexión devuelve un array u otro tipo, esa clave no se puede establecer automáticamente en la respuesta.
{% endalert %}


[16]: [success@braze.com](mailto:success@braze.com)