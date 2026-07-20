---
nav_title: "GET: 제품 ID 내보내기"
article_title: "GET: 제품 ID 내보내기"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "이 문서에서는 제품 ID 내보내기 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 제품 ID 내보내기 {#export-product-ids}
{% apimethod get %}
/purchases/product_list
{% endapimethod %}

> 이 엔드포인트를 사용하여 페이지가 매겨진 제품 ID 목록을 반환합니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#dff4ed40-81f5-451d-9d44-accc0e932285{% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `purchases.product_list` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key-permissions)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `page` | 선택 사항 | 문자열 | 보고 싶은 제품 목록 페이지입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요청 매개변수" }

## 요청 예시 {#example-request}

{% raw %}
```
https://rest.iad-01.braze.com/purchases/product_list?page=1
```
{% endraw %}

## 응답 {#response}

```json
{
  "products": [
    "product_name" (string), the name of the product
  ],
  "message": "success"
}
```

{% endapi %}

{% alert tip %}
CSV 및 API 내보내기에 대한 도움이 필요하면 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)을 참조하세요.
{% endalert %}