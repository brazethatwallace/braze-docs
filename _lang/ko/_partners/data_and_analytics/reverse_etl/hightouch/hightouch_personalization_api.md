---
nav_title: Hightouch Personalization API
article_title: Hightouch Personalization API
description: "이 참조 문서에서는 Braze와 Hightouch의 Personalization API 간의 통합에 대해 설명합니다. Personalization API는 클라우드 데이터 웨어하우스 내의 모든 데이터셋을 기반으로 저지연 데이터 API를 호스팅하는 관리형 서비스입니다. 이 참조 문서에서는 Hightouch Personalization API가 해결하는 사용 사례, 작동하는 데이터, 구성 방법, 그리고 Braze와 통합하는 방법을 다룹니다."
page_type: partner
search_tag: Partner
---

# Hightouch Personalization API

> Hightouch의 [Personalization API](https://hightouch.com/docs/destinations/personalization-api)는 클라우드 데이터 웨어하우스 내의 모든 데이터셋을 기반으로 저지연 데이터 API를 호스팅할 수 있는 관리형 서비스입니다.

![데이터 웨어하우스에서 Hightouch를 거쳐 모바일 앱, 웹 경험, 동적 이메일로의 데이터 흐름을 보여주는 Hightouch Personalization API 아키텍처 다이어그램.]({% image_buster /assets/img/hightouch/cohort7.png %})

Braze와 Hightouch 통합을 사용하면 [Braze 연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)와 함께 API를 활용하여 발송 시점에 최신 고객 또는 오브젝트 데이터를 Campaign 또는 Canvases로 가져올 수 있습니다.

Hightouch의 Personalization API는 Braze 구성 내에서 사용할 수 있는 REST 엔드포인트를 제공합니다. 구체적으로, Braze 연결된 콘텐츠 기능을 사용하여 Personalization API에 GET 요청을 보내 특정 식별자와 관련된 모든 정보를 검색할 수 있습니다. 이 API를 통해 노출되는 데이터는 고객, 제품 또는 기타 오브젝트 데이터를 나타낼 수 있습니다.

![Snowflake, BigQuery, Redshift에서 Hightouch Personalization API를 거쳐 Braze 연결된 콘텐츠로의 데이터 흐름을 보여주는 다이어그램.]({% image_buster /assets/img/hightouch/cohort6.png %})

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| Personalization API가 활성화된 [Hightouch 계정](https://app.hightouch.com/login) | 이 파트너십을 활용하려면 Hightouch [비즈니스 티어 계정](https://hightouch.com/pricing)이 필요합니다. |
| 정의된 사용 사례 | API를 설정하기 전에 이 통합의 사용 사례를 결정해야 합니다. 일반적인 사용 사례는 아래 목록을 참조하세요. |
| 클라우드 데이터 웨어하우스 또는 기타 소스에 저장된 데이터 | Hightouch는 [25개 이상의 데이터 소스](https://hightouch.com/integrations)와 통합됩니다. |
| Hightouch API 키 | **Hightouch > Settings > API keys > Add API key**에서 생성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

{% tabs %}
{% tab 사용 사례 %}

### 사용 사례 {#use-cases}

시작하기 전에 Personalization API를 어떻게 사용할지 정확히 계획하는 것이 좋습니다.

일반적인 사용 사례는 다음과 같습니다:
- **제품 추천**: 이메일 템플릿, Campaigns 또는 인앱 경험에 개인화된 제품 추천을 간편하게 삽입
- **개인화된 마케팅 캠페인 강화**: 동적 제품 추천으로 마케팅 터치포인트를 풍부하게 만들기
- **인앱 또는 웹 개인화 제공**: 예를 들어, 맞춤형 검색 결과, 코호트 기반 가격 책정 및 메시징, 문서 추천 또는 가장 가까운 매장 위치
- **금융 또는 의료 데이터 기반 추천**: 금융 데이터에는 엄격한 요구 사항이 있으며, Hightouch는 [엄격한 데이터 보안 정책](https://hightouch.com/docs/security/overview#compliance)을 통해 이를 충족합니다. Hightouch를 사용하면 세분화 기준에 사용된 기본 속성을 노출하지 않고도 금융 또는 의료 데이터를 기반으로 고객 Segments를 생성할 수 있습니다.

{% endtab %}
{% tab 데이터셋 %}

### 데이터셋 {#datasets}

Personalization API는 웨어하우스에서 선택한 데이터의 캐시 역할을 하므로, 추천 데이터가 이미 웨어하우스에 저장되어 있어야 합니다. 필요한 경우 Hightouch를 사용하여 템플릿에 따라 데이터를 변환할 수 있습니다. 이러한 유형의 데이터에는 다음이 포함됩니다:
- 지리적 지역, 나이 또는 기타 인구통계 정보와 같은 사용자 메타데이터
- 과거 구매, 페이지 조회, 클릭 등을 포함한 사용자 행동 또는 이벤트

{% endtab %}
{% endtabs %}

## 통합 {#integration}

### 1단계: Hightouch에 데이터 소스 연결 {#step-1-connect-data-source-to-hightouch}

Hightouch [소스](https://hightouch.com/docs/getting-started/concepts#sources)는 조직의 비즈니스 데이터가 저장된 곳입니다. 이 경우 사용자 데이터가 저장된 곳이 됩니다.
1. Hightouch에서 **Sources Overview > Add Source**로 이동합니다. 데이터 웨어하우스를 소스로 선택합니다.<br><br>
2. 관련 자격 증명을 입력합니다. 이는 소스에 따라 다릅니다.

자세한 내용은 관련 소스 [설명서](https://hightouch.com/docs)를 참조하세요.

### 2단계: 데이터 모델링 {#step-2-model-data}

Hightouch 모델은 소스에서 가져올 데이터를 정의합니다. 새 모델을 설정하려면 다음 단계를 따르세요:

1. Hightouch에서 [**Models overview**](https://app.hightouch.com/models) > **Add model**로 이동하고, 방금 연결한 소스를 선택합니다.<br><br>
2. 다음으로, [모델링 방법](https://hightouch.com/docs/models/creating-models)을 선택합니다. 모든 정보가 하나의 테이블에 조인되어야 하므로 시각적 테이블 선택기를 사용하여 테이블을 정의할 수 있습니다. 또는 SQL을 작성하여 원하는 열만 포함하거나, 기존 dbt 모델, Looker Looks 또는 Sigma 워크북을 활용할 수도 있습니다.<br><br>
3. 계속하기 전에 모델을 미리보기하여 원하는 데이터를 쿼리하고 있는지 확인합니다. 기본적으로 Braze는 미리보기를 처음 100개 레코드로 제한합니다. 데이터를 검증한 후 **Continue**를 클릭합니다.<br><br>
4. 모델 이름을 지정합니다. 예를 들어, "User recommendations"로 지정합니다.<br><br>
5. 마지막으로, 기본 키를 선택하고 **Finish**를 클릭합니다. 기본 키는 고유 식별자가 있는 열이어야 합니다. 이 필드는 특정 사용자의 추천을 검색하기 위해 Personalization API를 호출할 때 사용하는 필드이기도 합니다.

### 3단계: Personalization API 구성 {#step-3-configure-personalization-api}

API가 요청을 수신할 수 있도록 준비하는 데는 두 가지 단계가 있습니다:
- 인프라에 가장 가까운 리전에서 Personalization API 활성화
- 어떤 모델이 Hightouch 관리형 캐시에 구체화되어야 하는지 정의하는 동기화 생성

다음 지침에 따라 두 가지를 모두 완료하세요:

1. Hightouch에서 [**Destinations**](https://app.hightouch.com/destinations)로 이동하고, 생성된 Hightouch Personalization API를 선택합니다. 이 대상이 활성화되어 있지 않은 경우 [Hightouch 고객지원](mailto:friends@hightouch.com)에 문의하세요.<br><br>
2. 다음으로, 적절한 리전을 선택합니다. 인프라에 가장 가까운 리전을 선택하면 응답 시간이 단축됩니다. 인프라에 가까운 리전이 보이지 않는 경우 [Hightouch 고객지원](mailto:friends@hightouch.com)에 문의하세요.<br><br>
3. [**Syncs** 개요 페이지](https://app.hightouch.com/syncs)로 이동하고 **Add sync** 버튼을 클릭합니다. 다음으로, 관련 모델과 이전에 설정한 대상을 선택합니다.<br><br>
4. 영숫자 컬렉션 이름을 입력합니다. 컬렉션은 개념적으로 데이터베이스 테이블과 유사합니다. 각 컬렉션은 고객 또는 인보이스와 같은 특정 데이터 유형을 나타내야 합니다. 컬렉션 이름은 영숫자여야 하며 Personalization API 엔드포인트의 일부가 됩니다.<br><br>
5. 다음으로, 모델에서 어떤 열이 레코드 조회의 기본 인덱스 역할을 해야 하는지 지정합니다. 이 필드는 컬렉션의 각 레코드를 고유하게 식별해야 하며, 일반적으로 모델의 기본 키와 동일합니다. Personalization API는 여러 인덱스에 대한 조회를 지원합니다. 예를 들어, `user_id`, `anonymous_id` 또는 `email_address`를 사용하여 고객 프로필을 검색할 수 있습니다. 여러 인덱스를 활성화하려면 [Hightouch 고객지원](mailto:friends@hightouch.com)에 문의하세요.<br><br>
6. 필드 매퍼를 사용하여 모델에서 어떤 열이 API 응답 페이로드에 포함되어야 하는지 지정합니다. 이러한 필드의 이름을 변경하고 고급 매퍼를 사용하여 Liquid 템플릿 언어로 변환을 적용할 수 있습니다.<br><br>
7. 사용 사례에 적합한 [삭제 동작](https://www.hightouch.com/docs/destinations/personalization-api#delete-behavior)을 선택합니다.<br><br>
8. 마지막으로, **Continue**를 클릭한 다음 [동기화 스케줄](https://hightouch.com/docs/syncs/schedule-sync-ui)을 선택합니다.

이제 Hightouch가 웨어하우스의 데이터를 관리형 데이터베이스에 동기화하고 Personalization API를 통해 노출합니다.

### 4단계: Braze 연결된 콘텐츠를 통해 Personalization API 호출 {#step-4-call-personalization-api-through-braze-connected-content}

Personalization API 인스턴스를 설정한 후에는 Braze 연결된 콘텐츠 엔드포인트로 사용할 수 있습니다.

API는 `https://personalization.{region}.hightouch.com`에서 접근할 수 있습니다. 예를 들어, `https://personalization.us-west-2.hightouch.com`입니다.

정보는 이 엔드포인트 `/v1/collections/:collection_name/records/:index_key/:index_value`를 사용하여 이용할 수 있습니다.

예를 들어, Campaign 또는 Canvas에 다음 스니펫을 포함할 수 있습니다:

{% raw %}

```liquid
{% connected_content
     https://personalization.us-west-2.hightouch.com/v1/collections/customer/records/id/12345
     :method get
     :headers {
       "Authorization": "Bearer {{YOUR-API-KEY}}"
  }
     :content_type application/json
     :save customer
%}
```
{% endraw %}

Liquid 템플릿을 사용하여 JSON 페이로드에서 반환된 속성을 참조하고 메시징에 활용할 수 있습니다.

아래 예시 페이로드의 경우:

```json
{
    "user_id": 12345,
    "full_name": "Alex Smith",
    "lifetime_value": 1492.18,
    "churn_risk": 0.04,
    "90_day_summary": {
        "num_songs_listened": 813,
        "top_genres": [
            "house",
            "techno",
            "ambient"
        ],
        "top_artists": [
            "deadmau5",
            "Marsh",
            "Enamour"
        ]
    },
    "recommendations": {
        "concerts": [
            {
                "artist": "Aphex Twin",
                "location": "San Francisco, CA",
                "event_date": "2023-01-31"
            },
            {
                "artist": "Sultan + Shepard",
                "location": "San Francisco, CA",
                "event_date": "2023-02-25"
            }
        ],
        "upcoming_album_release": {
            "title": "Universal Language",
            "artist": "Alex Lee",
            "label": "Anjunadeep",
            "release_date": "2023-04-28"
        }
    }
}
```

다음 Liquid 참조는 이 예시 데이터를 반환합니다:

| Liquid 템플릿 | 반환 예시 |
| --- | --- |
| {% raw %}`{{artists.recommendations.concerts[0].artist}}`{% endraw %} | Aphex Twin |
| {% raw %}`{{artists.recommendations.concerts[0].location}}`{% endraw %} | San Francisco, CA |
| {% raw %}`{{artists.recommendations.upcoming_album_release.title}}`{% endraw %} | Universal Language |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze 연결된 콘텐츠를 통해 Personalization API 호출" }

## 문제 해결 {#troubleshooting}

질문이 있는 경우 [Hightouch 고객지원](mailto:friends@hightouch.com)에 문의하여 도움을 받으세요.