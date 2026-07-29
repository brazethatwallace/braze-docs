{% if include.section == "default behavior" %}

Por padrão, o Conteúdo Conectado definirá um cabeçalho `Content-Type` em uma solicitação HTTP GET para `application/json` com `Accept: */*`. Se você precisar de outro tipo de conteúdo, especifique-o explicitamente adicionando `:content_type your/content-type` à tag. A Braze definirá então tanto o cabeçalho Content-Type quanto o cabeçalho Accept para o tipo que você especificar.

{% raw %}
```js
{% connected_content https://api.sunrise-sunset.org/v2?lat=40.7128&lng=-74.0060&date=today :content_type application/json %}
```
{% endraw %}

{% endif %}

{% if include.section == "http post" %}

Por padrão, o Conteúdo Conectado faz uma solicitação HTTP GET para a URL especificada. Para fazer uma solicitação POST, especifique `:method post`.

Opcionalmente, você pode fornecer um corpo POST especificando `:body` seguido por uma string de consulta no formato `key1=value1&key2=value2&...` ou uma referência a valores capturados. O Content-Type padrão é `application/x-www-form-urlencoded`. Se você especificar `:content_type application/json` e fornecer um corpo codificado em formulário, como `key1=value1&key2=value2`, a Braze codificará automaticamente o corpo em JSON antes de enviar.

O Conteúdo Conectado também não armazena em cache chamadas POST por padrão. Você pode atualizar esse comportamento adicionando `:cache_max_age` à chamada POST do Conteúdo Conectado.

{% tabs %}
{% tab Tipo de conteúdo padrão %}

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 %}
```
{% endraw %}

{% endtab %}
{% tab Tipo de conteúdo Application/JSON %}

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 :content_type application/json %}
```
{% endraw %}

{% endtab %}
{% endtabs %}


{% endif %}