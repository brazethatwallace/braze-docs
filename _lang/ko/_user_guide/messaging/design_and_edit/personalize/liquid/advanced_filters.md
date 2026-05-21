---
nav_title: 고급 필터
article_title: 고급 Liquid 필터
page_order: 4
description: "이 참조 문서에서는 고급 필터, 예시, 그리고 Campaign에서 활용하는 방법을 설명합니다."

---

# 고급 필터 {#advanced-filters}

> 이 참조 문서에서는 Liquid의 고급 필터와 사용 방법에 대한 개요를 제공합니다.

## 인코딩 필터 {#encoding-filters}

{% raw %}
| 필터 이름 | 필터 설명 | 입력 예시 | 출력 예시 |
|---|---|---|---|
| `md5` | md5로 인코딩된 문자열을 반환합니다 | `{{'hey' | md5}}` | 6057f13c496ecf7fd777ceb9e79ae285 |
| `sha1` | sha1으로 인코딩된 문자열을 반환합니다 | `{{'hey' | sha1}}` | 7f550a9f4c44173a37664d938f1355f0f92a47a7 |
| `sha2` | sha2(256비트, SHA-256이라고도 함)로 인코딩된 문자열을 반환합니다 | `{{'hey' | sha2}}` | fa690b82061edfd2852629aeba8a8977b57e40fcb77d1a7a28b26cba62591204 |
| `base64` | base64로 인코딩된 문자열을 반환합니다 | `{{'blah' | base64_encode}}` | YmxhaA== |
| `hmac_sha1_hex` (이전 `hmac_sha1`) | hmac-sha1 서명을 16진수 문자열로 인코딩하여 반환합니다 | `{{'hey' | hmac_sha1_hex: 'secret_key'}}` | 2a3969bed25bfeefb00aca4063eb9590b4df8f0e |
| `hmac_sha1_base64` | hmac-sha1 서명을 base64 문자열로 인코딩하여 반환합니다 | `{{'hey' | hmac_sha1_base64: 'secret_key'}}` | KjlpvtJb/u+wCspAY+uVkLTfjw4= |
| `hmac_sha256_hex` | hmac-sha256 서명을 16진수 문자열로 인코딩하여 반환합니다 | `{{'hey' | hmac_sha256_hex: 'secret_key'}}` | 8df897f8da3d7992fe57c8dbc6f27578cfbf2dcc4d0fbb4000b8c924841d508e |
| `hmac_sha256_base64` | hmac-sha256 서명을 base64 문자열로 인코딩하여 반환합니다 | `{{'hey' | hmac_sha256_base64: 'secret_key'}}` | jfiX+No9eZL+V8jbxvJ1eM+/LcxND7tAALjJJIQdUI4= |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Encoding filters" }

## URL 필터 {#url-filters}

| 필터 이름 | 필터 설명 | 입력 예시 | 출력 예시 |
|---|---|---|---|
| `url_escape` | URL에서 허용되지 않는 문자열 내 모든 문자를 식별하고 이스케이프된 형태로 대체합니다 | `{{'hey<>hi' | url_escape}}` | hey%3C%3Ehi |
| `url_param_escape` | URL에서 허용되지 않는 문자열 내 모든 문자를 앰퍼샌드(&)를 포함하여 이스케이프된 형태로 대체합니다 | `{{'hey<&>hi' | url_param_escape}}` | hey%3C%26%3Ehi |
| `url_encode` | URL에 적합한 형태로 문자열을 인코딩합니다 | `{{ 'google search' | url_encode }}` | google+search |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="URL filters" }

{% endraw %}
{% alert tip %}
`assign` 태그를 HTML과 결합하면 여러 하이퍼링크를 만들 때 시간과 노력을 절약할 수 있습니다.
{% raw %}
```
{% assign url = "https://www.examplelink.com" %}
<a href='{{url}}'>Shop the collection</a>
```
{% endraw %}
{% endalert %}
{% raw %}

## 등록정보 접근자 필터 {#property-accessor-filter}

| 필터 이름 | 필터 설명 |
| --- | --- |
| `property_accessor` | 해시와 해시 키를 받아 해당 키에 있는 값을 반환합니다 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Property accessor filter" }

**해시 예시:** `{"a" => 42, "b" => 0}`
**입력 예시:** `{{hash | property_accessor: 'a'}}`
**출력 예시:** `42`

또한 등록정보 접근자 필터를 사용하면 커스텀 속성을 해시 키로 템플릿화하여 특정 해시 값에 접근할 수 있습니다.

{% endraw %}

{% alert note %}
Braze의 Liquid에서는 해시를 변수(예: 표현식)로 인스턴스화할 수 있는 방법이 없습니다.
{% endalert %}

{% raw %}

## 숫자 서식 필터 {#number-formatting-filters}

| 필터 이름 | 필터 설명 | 입력 예시 | 출력 예시 |
|---|---|---|---|
| `number_with_delimiter` | 숫자에 쉼표를 추가하여 서식을 지정합니다 | `{{ 123456 | number_with_delimiter }}` | 123,456 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Number formatting filters" }

## JSON 이스케이프 / 문자열 이스케이프 필터 {#json-escape-or-string-escape-filter}

| 필터 이름 | 필터 설명 |
|---|---|
| `json_escape` | 문자열 내 특수 문자(예: 큰따옴표 `""` 및 백슬래시 '\')를 이스케이프합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="JSON escape or string escape filter" }

이 필터는 JSON 사전에서 문자열을 개인화할 때 항상 사용해야 하며, 특히 웹훅에 유용합니다.

## JSON 서식 필터 {#json-formatting-filters}

| 필터 이름 | 필터 설명 |
|---|---|
| `json_parse` | JSON 문자열을 오브젝트나 배열과 같은 해당 데이터 구조로 변환합니다. |
| `as_json_string` | 오브젝트나 배열과 같은 데이터 구조를 해당 JSON 문자열로 변환합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="JSON-formatting filters" }

{% endraw %}

{% details json_parse 입력 및 출력 예시 %}

### 입력 {#input}

{% raw %}
```liquid
{% assign my_data_string = '[{"id":"1","store_name":"demo-store"}]'  %}
{% assign my_data = my_data_string | json_parse %}
```

### 출력 {#output}

```liquid
{% for item in my_data %}
Item ID: {{ item.id }}
Item Name: {{ item.store_name }}
{% endfor %}
```
{% endraw %}

{% enddetails %}

{% details as_json_string 입력 및 출력 예시 %}

### 입력

{% raw %}
```liquid
{% assign my_data_string = '[{"id":"1","store_name":"demo-store"}]'  %}
{% assign my_data = my_data_string | json_parse %}
{% assign json_string = my_data | as_json_string %}
```

### 출력

```liquid
{{json_string}}
```
{% endraw %}
{% enddetails %}

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[37]:#accounting-for-null-attribute-values