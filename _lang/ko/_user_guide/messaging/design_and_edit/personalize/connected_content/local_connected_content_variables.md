---
nav_title: 로컬 연결된 콘텐츠 변수
article_title: 로컬 연결된 콘텐츠 변수
page_order: 1
description: "이 참조 문서에서는 로컬 연결된 콘텐츠 변수를 사용하고 저장하는 방법을 다룹니다."
search_rank: 1
---

# 로컬 연결된 콘텐츠 변수 {#local-connected-content-variables}

> 이 페이지에서는 로컬 연결된 콘텐츠 변수의 개요와 이를 사용하고 저장하는 방법을 설명합니다.

Braze는 `connected_content` 태그 내에 지정된 엔드포인트로 전송 시점에 표준 GET 요청을 보냅니다. 엔드포인트가 JSON을 반환하면 자동으로 구문 분석되어 `connected`라는 변수에 저장됩니다. 엔드포인트가 텍스트를 반환하면 `connected_content` 태그 위치에 메시지로 직접 삽입됩니다.

응답을 변수에 저장하려면 JSON 오브젝트를 반환하는 것이 좋습니다. 연결된 콘텐츠의 응답이 태그를 텍스트로 대체하도록 하려면 응답이 유효한 JSON이 아닌지 확인하세요([json.org](http://www.json.org)에서 정의한 기준).

URL 뒤에 `:save your_variable_name`을 지정하여 데이터를 다른 이름으로 저장할 수도 있습니다. 예를 들어, 다음 `connected_content` 태그는 응답을 `localweather`라는 로컬 변수에 저장합니다(여러 `connected_content` JSON 변수를 저장할 수 있습니다):

{% raw %}
```js
{% connected_content https://www.metaweather.com/api/location/2459115/ :save localweather %}
```
{% endraw %}

Metaweather는 "Where-on-Earth ID"를 사용하여 해당 지역의 날씨를 반환하는 무료 날씨 API입니다. 이 코드는 테스트 및 학습 목적으로만 사용하세요.

저장된 변수는 `connected_content` 요청이 포함된 필드 내에서만 접근할 수 있습니다. 예를 들어, `localweather` 변수를 메시지와 제목 필드 모두에서 사용하려면 두 필드 모두에서 `connected_content` 요청을 해야 합니다.

GET 요청은 일반적으로 기본적으로 캐시되지만, 몇 가지 예외가 있습니다(높은 카디널리티의 사용자 속성을 포함하는 URL, `:no_cache`, 또는 1MB보다 큰 응답 본문 등). 동일한 GET 요청이 둘 이상의 필드에 나타나면 Braze는 엔드포인트를 다시 호출하는 대신 캐시된 응답을 재사용합니다. 캐시 동작에 대한 자세한 내용은 [응답 캐싱]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses/)을 참조하세요.

HTTP POST를 통한 연결된 콘텐츠 호출은 기본적으로 캐시되지 않습니다. POST 응답을 캐시하려면 태그에 `:cache_max_age`를 추가하세요. [기본 캐시 설정]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses/#default-cache-settings)을 참조하세요.

## JSON 구문 분석 {#json-parsing}

연결된 콘텐츠는 `:save`를 지정하면 JSON 형식의 결과를 로컬 변수로 해석합니다. 예를 들어, 날씨 관련 연결된 콘텐츠 엔드포인트가 다음 JSON 오브젝트를 반환하고, `:save localweather`를 지정하여 로컬 변수 `localweather`에 저장합니다.
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

`{{localweather.consolidated_weather[0].weather_state_name}}`을 참조하여 비가 오는지 여부를 테스트할 수 있으며, 이 오브젝트에서 사용하면 `Clear`를 반환합니다. 결과 위치 이름으로도 개인화하려면 `{{localweather.title}}`이 `New York`을 반환합니다.
{% endraw %}

다음 이미지는 올바르게 설정했을 때 대시보드에서 볼 수 있는 구문 강조 유형을 보여줍니다. 또한 예시 `connected_content` 요청을 활용하는 방법도 보여줍니다!

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

API가 {%raw%}`{{localweather.consolidated_weather[0].weather_state_name}}`{%endraw%}에서 `Rain`을 반환하면 사용자는 다음 푸시 알림을 받게 됩니다.

![메시지가 "It's raining! Grab an umbrella!"인 푸시 알림]({% image_buster /assets/img_archive/connected_weather_push2.png %} "Connected Content Push Usage Example"){:style="max-width:50%" }

{% multi_lang_include connected_content.md section='default behavior' %}

## HTTP POST

{% multi_lang_include connected_content.md section='http post' %}

### JSON 본문 제공 {#providing-json-body}

자체 JSON 본문을 제공하려면 공백이 없는 경우 인라인으로 작성할 수 있습니다. 본문에 공백이 있는 경우 assign 또는 capture 문을 사용해야 합니다. 즉, 다음 세 가지 모두 허용됩니다:

{% raw %}
##### 인라인: 공백 불허 {#inline-spaces-not-allowed}

```js
{% connected_content https://example.com/api/endpoint :method post :body {"foo":"bar","baz":"{{1|plus:1}}"} :content_type application/json %}
```

##### capture 문의 본문: 공백 허용 {#body-in-a-capture-statement-spaces-allowed}

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
##### assign 문의 본문: 공백 허용 {#body-in-an-assign-statement-spaces-allowed}

```js
{% assign postbody = '{"foo":"bar", "baz": "2"}' %}
{% connected_content https://example.com/api/endpoint :method post :body {{postbody}} :content_type application/json %}
```
{% endraw %}

## HTTP 상태 코드 {#http-status-codes}

연결된 콘텐츠 호출의 HTTP 상태를 먼저 로컬 변수로 저장한 다음 `__http_status_code__` 키를 사용하여 활용할 수 있습니다. 예를 들어:

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :save result %}
{% if result.__http_status_code__ != 200 %}
  {% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert important %}
이 키는 엔드포인트가 유효한 JSON 오브젝트와 `2XX` 응답을 반환하는 경우에만 연결된 콘텐츠 오브젝트에 자동으로 추가됩니다. 엔드포인트가 배열이나 다른 유형을 반환하는 경우 해당 키는 응답에 자동으로 설정될 수 없습니다.
{% endalert %}


[16]: [success@braze.com](mailto:success@braze.com)