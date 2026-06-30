---
nav_title: REST API
article_title: REST API
page_order: 1
description: "연결된 콘텐츠를 사용하여 REST API에서 메시지로 데이터를 가져와 실시간 개인화를 수행하는 방법을 알아봅니다."
---

# REST API {#rest-api}

> [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)를 사용하여 발송 시점에 외부 REST API에서 메시지로 직접 데이터를 가져올 수 있습니다. 이를 통해 자체 서버, 서드파티 서비스 또는 공개적으로 접근 가능한 API 엔드포인트의 실시간 정보로 메시지를 개인화할 수 있습니다.

## 작동 방식 {#how-it-works}

{% raw %}
연결된 콘텐츠는 지정한 URL로 HTTP 요청을 보낸 다음 응답을 저장하여 Liquid로 참조할 수 있도록 합니다. 메시지에 `{% connected_content %}` 태그를 추가하면 메시지가 발송될 때 Braze가 엔드포인트를 호출합니다.

```liquid
{% connected_content https://api.example.com/user/{{${user_id}}}/recommendations :save recs %}
We think you'll love {{recs.top_pick}}!
```
{% endraw %}

연결된 콘텐츠는 GET 및 POST 요청을 지원합니다. Braze는 서버가 2초 이내에 응답하도록 요구하므로, 엔드포인트를 낮은 지연 시간에 맞게 설계하세요.

## 일반적인 활용 사례 {#common-use-cases}

| 활용 사례 | 설명 |
| --- | --- |
| 제품 추천 | 추천 엔진에서 개인화된 제품 추천을 가져옵니다 |
| 실시간 가격 또는 재고 | 발송 시점의 현재 가격 또는 재고 수준을 표시합니다 |
| 날씨 기반 콘텐츠 | 현지 날씨 데이터를 가져와 메시징을 맞춤화합니다 |
| 로열티 포인트 잔액 | 최신 리워드 또는 계정 잔액을 표시합니다 |
| 콘텐츠 피드 | 최신 블로그 게시물, 문서 또는 뉴스 항목을 삽입합니다 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="일반적인 활용 사례" }

## 인증 {#authentication}

Braze는 연결된 콘텐츠 요청에 대해 기본 인증, 토큰 인증 및 OAuth를 지원합니다. Braze 대시보드의 **설정** > **연결된 콘텐츠**에서 자격 증명을 안전하게 저장하고 API 호출에서 참조할 수 있습니다.

자세한 내용은 [연결된 콘텐츠 API 호출하기]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#authentication-types)를 참조하세요.

## 오류 처리 {#error-handling}

엔드포인트가 오류를 반환하거나 시간이 초과되면, Braze는 연결된 콘텐츠 응답 대신 빈 문자열을 렌더링합니다. 저장된 변수가 null인지 확인하여 실패를 감지하고, 조건부로 메시지를 중단하거나 대체 콘텐츠를 표시할 수 있습니다.

자세한 내용은 [연결된 콘텐츠 중단하기]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content)를 참조하세요.

## 성능 고려 사항 {#performance-considerations}

Braze는 대량으로 메시지를 전달하므로, 서버가 수천 개의 동시 연결을 처리할 수 있어야 합니다. 적절한 경우 캐싱을 사용하고 메시지에 사용량 제한을 설정하여 외부 엔드포인트에 과부하가 걸리지 않도록 하세요.

연결된 콘텐츠에 대한 전체 참조는 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)를 확인하세요.