{% if include.section == "default behavior" %}

기본적으로 연결된 콘텐츠는 GET HTTP 요청에 `Content-Type` 헤더를 `application/json`으로, `Accept: */*`로 설정합니다. 다른 콘텐츠 유형이 필요한 경우 태그에 `:content_type your/content-type`을 추가하여 명시적으로 지정하세요. 그러면 Braze는 Content-Type 헤더와 Accept 헤더를 모두 지정한 유형으로 설정합니다.

{% raw %}
```js
{% connected_content http://numbersapi.com/random/trivia :content_type application/json %}
```
{% endraw %}

{% endif %}

{% if include.section == "http post" %}

기본적으로 연결된 콘텐츠는 지정된 URL에 HTTP GET 요청을 보냅니다. 대신 POST 요청을 보내려면 `:method post`를 지정하세요.

선택적으로 `:body` 뒤에 `key1=value1&key2=value2&...` 형식의 쿼리 문자열 또는 캡처된 값에 대한 참조를 지정하여 POST 본문을 제공할 수 있습니다. Content-Type의 기본값은 `application/x-www-form-urlencoded`입니다. `:content_type application/json`을 지정하고 `key1=value1&key2=value2`와 같이 form-urlencoded 본문을 제공하면, Braze는 전송 전에 자동으로 본문을 JSON 인코딩합니다.

연결된 콘텐츠는 기본적으로 POST 호출도 캐시하지 않습니다. 이 동작은 연결된 콘텐츠 POST 호출에 `:cache_max_age`를 추가하여 변경할 수 있습니다.

{% tabs %}
{% tab 기본 content-type %}

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