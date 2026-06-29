---
nav_title: Variáveis locais de Conteúdo conectado
article_title: Variáveis locais de Conteúdo conectado
page_order: 1
description: "Este artigo de referência aborda como usar e armazenar variáveis locais de Conteúdo conectado."
search_rank: 1
---

# Variáveis locais de Conteúdo conectado {#local-connected-content-variables}

> Esta página oferece uma visão geral das variáveis locais de Conteúdo conectado e como usá-las e armazená-las.

A Braze faz uma requisição GET padrão no momento do envio para o endpoint especificado na tag `connected_content`. Se o endpoint retornar JSON, ele será automaticamente analisado e armazenado em uma variável chamada `connected`. Se o endpoint retornar texto, ele será inserido diretamente na mensagem no lugar da tag `connected_content`.

Se você quiser salvar a resposta em uma variável, é recomendável retornar objetos JSON. E se você quiser que a resposta do Conteúdo conectado substitua a tag pelo texto, certifique-se de que a resposta não seja um JSON válido (conforme definido por [json.org](http://www.json.org))

Você também pode especificar `:save nome_da_sua_variavel` após a URL para salvar os dados com outro nome. Por exemplo, a seguinte tag `connected_content` armazenará a resposta em uma variável local chamada `localweather` (você pode salvar múltiplas variáveis JSON de `connected_content`):

{% raw %}
```js
{% connected_content https://www.metaweather.com/api/location/2459115/ :save localweather %}
```
{% endraw %}

Metaweather é uma API gratuita de clima que usa um "Where-on-Earth ID" para retornar o clima de uma área. Use este código apenas para fins de teste e aprendizado.

A variável armazenada só pode ser acessada dentro do campo que contém a requisição `connected_content`. Por exemplo, se você quiser usar a variável `localweather` tanto no campo de mensagem quanto no campo de título, faça a requisição `connected_content` em ambos os campos.

Requisições GET geralmente são armazenadas em cache por padrão, com algumas exceções (como URLs que incluem atributos de usuário de alta cardinalidade, `:no_cache` ou corpos de resposta maiores que 1 MB). Quando requisições GET idênticas aparecem em mais de um campo, a Braze reutiliza a resposta em cache em vez de chamar o endpoint novamente. Para detalhes sobre o comportamento de cache, consulte [Respostas em cache]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses/).

Chamadas de Conteúdo conectado feitas via HTTP POST não são armazenadas em cache por padrão. Para armazenar respostas POST em cache, adicione `:cache_max_age` à tag. Consulte [Configurações padrão de cache]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses/#default-cache-settings).

## Análise de JSON {#json-parsing}

O Conteúdo conectado interpretará qualquer resultado formatado em JSON como uma variável local quando você especificar `:save`. Por exemplo, um endpoint de Conteúdo conectado relacionado ao clima retorna o seguinte objeto JSON, que você armazena em uma variável local `localweather` especificando `:save localweather`.
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

Você pode verificar se está chovendo ou não referenciando `{{localweather.consolidated_weather[0].weather_state_name}}`, que, se usado neste objeto, retornaria `Clear`. Se você também quiser personalizar com o nome do local resultante, `{{localweather.title}}` retorna `New York`.
{% endraw %}

A imagem a seguir ilustra o tipo de destaque de sintaxe que você deve ver no dashboard se estiver configurando tudo corretamente. Ela também demonstra como você pode aproveitar o exemplo de requisição `connected_content`!

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

Se a API respondesse com {%raw%}`{{localweather.consolidated_weather[0].weather_state_name}}`{%endraw%} retornando `Rain`, o usuário receberia esta notificação por push.

![Notificação por push com a mensagem "It's raining! Grab an umbrella!"]({% image_buster /assets/img_archive/connected_weather_push2.png %} "Connected Content Push Usage Example"){:style="max-width:50%" }

{% multi_lang_include connected_content/sections.md section='default behavior' %}

## HTTP POST

{% multi_lang_include connected_content/sections.md section='http post' %}

### Fornecendo um corpo JSON {#providing-json-body}

Se você quiser fornecer seu próprio corpo JSON, pode escrevê-lo inline se não houver espaços. Se o corpo tiver espaços, você deve usar uma instrução assign ou capture. Ou seja, qualquer uma dessas três opções é aceitável:

{% raw %}
##### Inline: espaços não permitidos {#inline-spaces-not-allowed}

```js
{% connected_content https://example.com/api/endpoint :method post :body {"foo":"bar","baz":"{{1|plus:1}}"} :content_type application/json %}
```

##### Corpo em uma instrução capture: espaços permitidos {#body-in-a-capture-statement-spaces-allowed}

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
##### Corpo em uma instrução assign: espaços permitidos {#body-in-an-assign-statement-spaces-allowed}

```js
{% assign postbody = '{"foo":"bar", "baz": "2"}' %}
{% connected_content https://example.com/api/endpoint :method post :body {{postbody}} :content_type application/json %}
```
{% endraw %}

## Códigos de status HTTP {#http-status-codes}

Você pode utilizar o status HTTP de uma chamada de Conteúdo conectado salvando-o primeiro como uma variável local e depois usando a chave `__http_status_code__`. Por exemplo:

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :save result %}
{% if result.__http_status_code__ != 200 %}
  {% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert important %}
Esta chave só será adicionada automaticamente ao objeto de Conteúdo conectado se o endpoint retornar um objeto JSON válido e uma resposta `2XX`. Se o endpoint retornar um array ou outro tipo, essa chave não poderá ser definida automaticamente na resposta.
{% endalert %}


[16]: [success@braze.com](mailto:success@braze.com)