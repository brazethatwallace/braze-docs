{% if include.section == "default behavior" %}

De manera predeterminada, el contenido conectado establecerá un encabezado `Content-Type` en una solicitud GET HTTP que realice a `application/json` con `Accept: */*`. Si necesitas otro tipo de contenido, especifícalo explícitamente añadiendo `:content_type your/content-type` a la etiqueta. Braze establecerá entonces tanto el encabezado Content-Type como el Accept en el tipo que especifiques.

{% raw %}
```js
{% connected_content https://api.sunrise-sunset.org/v2?lat=40.7128&lng=-74.0060&date=today :content_type application/json %}
```
{% endraw %}

{% endif %}

{% if include.section == "http post" %}

De manera predeterminada, el contenido conectado realiza una solicitud HTTP GET a la URL especificada. Para realizar una solicitud POST en su lugar, especifica `:method post`.

Opcionalmente, puedes proporcionar un cuerpo POST especificando `:body` seguido de una cadena de consulta con el formato `key1=value1&key2=value2&...` o una referencia a los valores capturados. El tipo de contenido se establece de manera predeterminada en `application/x-www-form-urlencoded`. Si especificas `:content_type application/json` y proporcionas un cuerpo con codificación URL de formulario como `key1=value1&key2=value2`, Braze codificará automáticamente el cuerpo en JSON antes de enviarlo.

El contenido conectado tampoco almacena en caché las llamadas POST de forma predeterminada. Puedes actualizar este comportamiento añadiendo `:cache_max_age` a la llamada POST de contenido conectado.

{% tabs %}
{% tab Tipo de contenido predeterminado %}

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 %}
```
{% endraw %}

{% endtab %}
{% tab Tipo de contenido Application/JSON %}

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 :content_type application/json %}
```
{% endraw %}

{% endtab %}
{% endtabs %}


{% endif %}