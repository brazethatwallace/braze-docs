---
nav_title: ローカルコネクテッドコンテンツ変数
article_title: ローカルコネクテッドコンテンツ変数
page_order: 1
description: "このリファレンス記事では、ローカルコネクテッドコンテンツ変数の使用方法と保存方法について説明します。"
search_rank: 1
---

# ローカルコネクテッドコンテンツ変数

> このページでは、ローカルコネクテッドコンテンツ変数の概要と、その使用方法および保存方法について説明します。

Braze は送信時に `connected_content` タグ内で指定されたエンドポイントに対して標準的な GET リクエストを行います。エンドポイントが JSON を返す場合、自動的に解析され、`connected` という変数に格納されます。エンドポイントがテキストを返す場合、`connected_content` タグの代わりにメッセージに直接挿入されます。

応答を変数に保存したい場合は、JSON オブジェクトを返すことをお勧めします。コネクテッドコンテンツの応答でタグをテキストに置き換えたい場合は、応答が有効な JSON（[json.org](http://www.json.org) で定義されているもの）でないことを確認してください。

URL の後に `:save your_variable_name` を指定して、データを別の名前で保存することもできます。たとえば、次の `connected_content` タグは応答を `localweather` というローカル変数に保存します（複数の `connected_content` JSON 変数を保存できます）。

{% raw %}
```js
{% connected_content https://www.metaweather.com/api/location/2459115/ :save localweather %}
```
{% endraw %}

Metaweather は「Where-on-Earth ID」を使用してエリアの天気を返す無料の天気 API です。このコードはテストと学習目的でのみ使用してください。

>  保存された変数は、`connected_content` リクエストを含むフィールド内でのみアクセスできます。たとえば、メッセージフィールドとタイトルフィールドの両方で `localweather` 変数を使用したい場合は、両方のフィールド内で `connected_content` リクエストを行う必要があります。リクエストが同一の場合、Braze は送信先サーバーに 2 回目のリクエストを行う代わりに、キャッシュされた結果を使用します。ただし、HTTP POST 経由で行われたコネクテッドコンテンツの呼び出しはデフォルトではキャッシュされず、送信先サーバーに 2 回目のリクエストを行います。POST 呼び出しにキャッシュを追加したい場合は、[`cache_max_age`](#configurable-caching) オプションを参照してください。

## JSON の解析

コネクテッドコンテンツは、`:save` を指定すると、JSON 形式の結果をローカル変数として解釈します。たとえば、天気関連のコネクテッドコンテンツエンドポイントが次の JSON オブジェクトを返し、`:save localweather` を指定してローカル変数 `localweather` に格納します。
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

`{{localweather.consolidated_weather[0].weather_state_name}}` を参照することで、雨が降っているかどうかをテストできます。このオブジェクトで使用した場合、`Clear` が返されます。結果のロケーション名でパーソナライズしたい場合は、`{{localweather.title}}` で `New York` が返されます。
{% endraw %}

次の画像は、正しく設定されている場合にダッシュボードで表示されるシンタックスハイライトの種類を示しています。また、`connected_content` リクエストの例をどのように活用できるかも示しています。

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

API が {%raw%}`{{localweather.consolidated_weather[0].weather_state_name}}`{%endraw%} で `Rain` を返した場合、ユーザーは次のプッシュ通知を受け取ります。

![「It's raining! Grab an umbrella!」というメッセージのプッシュ通知]({% image_buster /assets/img_archive/connected_weather_push2.png %} "Connected Content Push Usage Example"){:style="max-width:50%" }

{% multi_lang_include connected_content.md section='default behavior' %}

## HTTP POST

{% multi_lang_include connected_content.md section='http post' %}

### JSON ボディの提供

独自の JSON ボディを提供したい場合、スペースがなければインラインで記述できます。ボディにスペースがある場合は、assign または capture ステートメントを使用する必要があります。つまり、以下の 3 つのいずれも使用できます。

{% raw %}
##### インライン: スペースは使用不可

```js
{% connected_content https://example.com/api/endpoint :method post :body {"foo":"bar","baz":"{{1|plus:1}}"} :content_type application/json %}
```

##### capture ステートメント内のボディ: スペース使用可

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
##### assign ステートメント内のボディ: スペース使用可

```js
{% assign postbody = '{"foo":"bar", "baz": "2"}' %}
{% connected_content https://example.com/api/endpoint :method post :body {{postbody}} :content_type application/json %}
```
{% endraw %}

## HTTP ステータスコード

コネクテッドコンテンツの呼び出しから HTTP ステータスを利用するには、まずローカル変数として保存し、次に `__http_status_code__` キーを使用します。例:

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :save result %}
{% if result.__http_status_code__ != 200 %}
  {% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert important %}
このキーは、エンドポイントが有効な JSON オブジェクトと `2XX` 応答を返す場合にのみ、コネクテッドコンテンツオブジェクトに自動的に追加されます。エンドポイントが配列やその他の型を返す場合、このキーは応答に自動的に設定できません。
{% endalert %}


[16]: [success@braze.com](mailto:success@braze.com)