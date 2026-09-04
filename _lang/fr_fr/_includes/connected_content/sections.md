{% if include.section == "default behavior" %}

Par défaut, le contenu connecté définit un en-tête `Content-Type` sur la requête HTTP GET qu'il effectue à `application/json` avec `Accept: */*`. Si vous avez besoin d'un autre type de contenu, spécifiez-le explicitement en ajoutant `:content_type your/content-type` à l'étiquette. Braze définira alors l'en-tête Content-Type et l'en-tête Accept selon le type que vous spécifiez.

{% raw %}
```js
{% connected_content https://api.sunrise-sunset.org/v2?lat=40.7128&lng=-74.0060&date=today :content_type application/json %}
```
{% endraw %}

{% endif %}

{% if include.section == "http post" %}

Par défaut, le contenu connecté effectue une requête HTTP GET vers l'URL spécifiée. Pour effectuer une requête POST à la place, spécifiez `:method post`.

Vous pouvez également fournir un payload POST en spécifiant `:body` suivi d'une chaîne de caractères de requête au format `key1=value1&key2=value2&...` ou d'une référence à des valeurs capturées. Le Content-Type par défaut est `application/x-www-form-urlencoded`. Si vous spécifiez `:content_type application/json` et fournissez un corps encodé en URL tel que `key1=value1&key2=value2`, Braze encodera automatiquement le corps en JSON avant l'envoi.

Par défaut, le contenu connecté ne met pas non plus en cache les appels POST. Vous pouvez modifier ce comportement en ajoutant `:cache_max_age` à l'appel POST du contenu connecté.

{% tabs %}
{% tab Content-Type par défaut %}

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 %}
```
{% endraw %}

{% endtab %}
{% tab Content-Type Application/JSON %}

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 :content_type application/json %}
```
{% endraw %}

{% endtab %}
{% endtabs %}


{% endif %}