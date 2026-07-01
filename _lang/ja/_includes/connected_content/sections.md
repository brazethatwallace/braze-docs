{% if include.section == "default behavior" %}

コネクテッドコンテンツはデフォルトで、GET HTTPリクエストの`Content-Type`ヘッダーを`Accept: */*`付きの`application/json`に設定します。別のコンテンツタイプが必要な場合は、タグに`:content_type your/content-type`を追加して明示的に指定してください。Brazeは、指定したタイプにContent-TypeヘッダーとAcceptヘッダーの両方を設定します。

{% raw %}
```js
{% connected_content http://numbersapi.com/random/trivia :content_type application/json %}
```
{% endraw %}

{% endif %}

{% if include.section == "http post" %}

デフォルトでは、コネクテッドコンテンツは指定されたURLにHTTP GETリクエストを送信します。代わりにPOSTリクエストを行うには、`:method post`を指定します。

オプションで`:body`の後に`key1=value1&key2=value2&...`形式のクエリ文字列またはキャプチャされた値への参照を指定することで、POSTボディを提供できます。Content-Typeのデフォルトは`application/x-www-form-urlencoded`です。`:content_type application/json`を指定し、`key1=value1&key2=value2`のようなフォームURLエンコードされたボディを提供すると、Brazeは送信前に自動的にボディをJSONエンコードします。

また、コネクテッドコンテンツはデフォルトではPOST呼び出しをキャッシュしません。コネクテッドコンテンツのPOST呼び出しに`:cache_max_age`を追加することで、この動作を更新できます。

{% tabs %}
{% tab Default content-type %}

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 %}
```
{% endraw %}

{% endtab %}
{% tab Application/JSON Content-Type %}

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 :content_type application/json %}
```
{% endraw %}

{% endtab %}
{% endtabs %}


{% endif %}