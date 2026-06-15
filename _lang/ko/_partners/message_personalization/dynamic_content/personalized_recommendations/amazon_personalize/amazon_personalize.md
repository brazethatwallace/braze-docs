---
nav_title: Amazon Personalize
article_title: Amazon Personalize
alias: "/partners/amazon_personalize_overview/"
description: "이 참조 문서에서는 Braze와 Amazon Personalize 간의 참조 아키텍처 및 통합에 대해 설명합니다. 이 참조 문서를 통해 Amazon Personalize가 제공하는 사용 사례, 작동하는 데이터, 서비스 구성 방법, 그리고 Braze와의 통합 방법을 이해할 수 있습니다."
page_type: partner
search_tag: Partner
---

# Amazon Personalize
<!--
{% multi_lang_include video.html id="xFZ3HMleYYE" align="right" %}
-->
> [Amazon Personalize](https://aws.amazon.com/personalize/)는 하루 종일 작동하는 나만의 Amazon 머신 러닝 추천 시스템과 같습니다. 20년 이상의 추천 경험을 바탕으로, Amazon Personalize는 실시간 개인화된 제품 및 콘텐츠 추천과 타겟 마케팅 프로모션을 통해 고객 참여를 향상시킬 수 있도록 지원합니다.

_이 통합은 Amazon Personalize에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

머신 러닝과 사용자가 정의하는 알고리즘을 활용하여, Amazon Personalize는 웹사이트와 애플리케이션에 고품질 추천을 출력하는 모델을 학습시키는 데 도움을 줄 수 있습니다. 이러한 모델을 통해 사용자의 과거 행동을 기반으로 추천 목록을 생성하고, 관련성에 따라 항목을 정렬하며, 유사성을 기반으로 다른 항목을 추천할 수 있습니다. Amazon Personalize API에서 가져온 목록은 Braze 연결된 콘텐츠에서 사용하여 개인화된 Braze 추천 캠페인을 실행할 수 있습니다. Amazon Personalize와 통합하면 고객은 모델 학습에 사용되는 매개변수를 제어하고 알고리즘 출력을 최적화하는 선택적 비즈니스 목표를 정의할 수 있는 자유를 얻게 됩니다.

이 참조 문서를 통해 Amazon Personalize가 제공하는 사용 사례, 작동하는 데이터, 서비스 구성 방법, 그리고 Braze와의 통합 방법을 이해할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| Amazon Web Service 계정 | 이 파트너십을 활용하려면 AWS 계정이 필요합니다. AWS 계정이 있으면 Amazon Personalize 콘솔, AWS 명령줄 인터페이스(AWS CLI) 또는 AWS SDK를 통해 Amazon Personalize에 액세스할 수 있습니다. |
| 정의된 사용 사례 | 모델을 생성하기 전에 이 통합의 사용 사례를 결정해야 합니다. 일반적인 사용 사례는 다음 목록을 참조하세요. |
| 데이터셋 | Amazon Personalize 추천 모델에는 상호작용, 사용자, 항목의 세 가지 유형의 데이터셋이 필요합니다. 각 데이터셋의 요구 사항은 다음 세부 정보를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

{% tabs %}
{% tab 사용 사례 %}

**사용 사례**

모델을 생성하기 전에 이 통합의 사용 사례를 결정해야 합니다. 일반적인 사용 사례는 다음과 같습니다:
- 사용자의 이전 상호작용을 기반으로 항목을 추천하여 진정한 개인화된 경험을 제공합니다.
- 각 사용자에게 맞춤화된 항목 목록 또는 검색 결과를 제공하여 사용자와의 관련성에 따라 항목을 표시함으로써 참여를 높입니다.
- 유사한 항목에 대한 추천을 찾아 사용자가 새로운 것을 발견할 수 있도록 돕습니다.

다음 가이드에서는 사용자 개인화 추천 레시피에 초점을 맞추겠습니다.

{% endtab %}
{% tab 데이터셋 %}

**데이터셋**

Amazon Personalize 추천 모델을 시작하려면 세 가지 유형의 데이터셋이 필요합니다:

- 상호작용
  - 사용자와 항목 간의 과거 상호작용을 저장합니다
  - `USER_ID`, `ITEM_ID`, `EVENT_TYPE` 및 `TIMESTAMP` 값이 필요하며, 선택적으로 이벤트에 대한 메타데이터를 허용합니다
- 사용자
  - 사용자에 대한 메타데이터를 저장합니다
  - `USER_ID` 값과 성별, 나이, 로열티 멤버십 등 최소 하나의 메타데이터 필드(문자열 또는 숫자)가 필요합니다
- 항목
  - 항목에 대한 메타데이터를 저장합니다
  - `ITEM_ID`와 항목을 설명하는 최소 하나의 메타데이터 필드(텍스트, 범주형 또는 숫자)가 필요합니다

사용자 추천 레시피의 경우, 최소 25명의 고유 사용자로부터 각각 최소 2회 이상의 상호작용이 포함된 최소 1000개의 상호작용 데이터 포인트가 있는 상호작용 데이터셋을 제공해야 합니다. 이러한 데이터셋은 S3에 저장된 CSV 파일을 사용하여 대량으로 업로드하거나 API를 통해 점진적으로 업로드할 수 있습니다.

{% endtab %}
{% endtabs %}

## 모델 생성 {#creating-models}

### 1단계: 학습 {#step-1-training}

데이터셋을 가져온 후 솔루션을 생성할 수 있습니다. 솔루션은 Amazon Personalize [레시피](https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html)(알고리즘) 중 하나를 사용하여 모델을 학습시킵니다. 이 경우 `USER_PERSONALIZATION` 레시피를 사용합니다. 솔루션을 학습시키면 모델의 성능 측정기준을 기반으로 평가할 수 있는 솔루션 버전(학습된 모델)이 생성됩니다.

Amazon Personalize에서는 모델이 학습에 사용하는 하이퍼파라미터를 조정할 수 있습니다. 예를 들어:
- Amazon Personalize 콘솔에 있는 "사용자 기록 길이 백분위수" 매개변수를 사용하면 학습에 포함할 사용자 기록의 백분위수를 조정할 수 있습니다:<br><br>![최소 최대 사용자 프로필 설정]({% image_buster /assets/img/amazon_personalize/min_and_max_user_percentile.png %})
  - `min_user_history_length_percentile`: 기록 길이가 매우 짧은 사용자 비율을 제외하므로 인기 항목을 제거하고 보다 심층적인 기본 패턴을 기반으로 추천을 구축하는 데 도움이 될 수 있습니다.
  - `max_user_history_length_percentile`: 기록 길이가 매우 긴 사용자를 학습에 포함할 비율을 조정합니다.

숨겨진 차원의 수는 복잡한 데이터셋에서 더 복잡한 패턴을 감지하는 데 도움이 되며, 시간 역전파 기법(BPTT)은 높은 가치의 행동으로 이어진 일련의 이벤트 이후 초기 이벤트에 대한 보상을 조정합니다.

또한 Amazon Personalize는 서로 다른 값으로 여러 버전의 솔루션을 동시에 실행하여 자동 하이퍼파라미터 튜닝을 제공합니다. 튜닝을 사용하려면 솔루션을 생성할 때 **Perform HPO**를 켜세요.

### 2단계: 평가 및 비교 {#step-2-evaluate-and-compare}

솔루션 학습이 완료되면 이를 평가하고 다른 버전과 비교할 준비가 됩니다. 각 솔루션 버전은 계산된 측정기준을 표시합니다. 사용 가능한 측정기준에는 다음이 포함됩니다:

- **정규화 할인 누적 이득:** 추천된 항목 순서를 실제 항목 목록과 비교하고 목록에서의 위치에 해당하는 가중치를 각 항목에 부여합니다
- **정밀도 @k:** 올바르게 추천된 항목 수를 전체 추천 항목 수로 나눈 값으로, `k`는 항목 수입니다
- **평균 역순위:** 첫 번째, 가장 높은 순위의 추천에 초점을 맞추고 첫 번째 일치하는 추천이 나타나기 전에 몇 개의 추천 항목이 표시되는지 계산합니다
- **커버리지:** 고유 추천 항목의 비율을 데이터셋의 전체 고유 항목 수에 대한 비율로 나타냅니다

## 추천 가져오기 {#getting-recommendations}

만족스러운 솔루션 버전을 생성했다면 이제 추천을 활용할 차례입니다. 추천에 액세스하는 방법은 두 가지가 있습니다:

1. 실시간 캠페인<br>캠페인은 정의된 최소 트랜잭션 처리량을 가진 배포된 솔루션 버전입니다. 트랜잭션은 추천 출력을 가져오기 위한 단일 API 호출이며, 최소값이 1인 TPS(초당 트랜잭션)로 정의됩니다. 캠페인은 부하가 증가하면 리소스를 확장하지만 최소값 아래로 떨어지지는 않습니다. 콘솔, AWS CLI 또는 코드에서 AWS SDK를 통해 추천을 쿼리할 수 있습니다.<br><br>
2. 배치 작업<br>배치 작업은 추천을 S3 버킷으로 내보냅니다. 작업은 추천을 내보내려는 사용자 ID 목록이 포함된 JSON 파일을 입력으로 받습니다. 그런 다음 올바른 권한과 출력 대상을 지정하면 작업을 실행할 준비가 됩니다. 런타임은 데이터셋의 크기와 추천 목록 길이에 따라 달라집니다.

### 필터 {#filters}

필터를 사용하면 항목의 ID, 이벤트 유형 또는 메타데이터를 기반으로 항목을 제외하여 추천 출력을 조정할 수 있습니다. 나이나 로열티 멤버십 상태와 같은 메타데이터를 기반으로 사용자를 필터링할 수도 있습니다. 필터는 사용자가 이미 상호작용한 항목을 추천하지 않도록 방지하는 데 유용할 수 있습니다.

## Braze와 결과 통합 {#integrating-results-with-braze}

생성된 모델과 추천 캠페인을 통해 Content Cards와 연결된 콘텐츠를 사용하여 사용자를 위한 Braze 캠페인을 실행할 준비가 되었습니다.
Braze 캠페인을 실행하기 전에 API를 통해 이러한 추천을 제공할 수 있는 서비스를 생성해야 합니다. [워크숍 문서의 3단계]({{site.baseurl}}/partners/amazon_personalize_workshop/#step-3-send-personalized-emails-from-braze)를 따라 AWS 서비스를 사용하여 서비스를 배포할 수 있습니다. 추천을 제공하는 자체 독립 백엔드 서비스를 배포할 수도 있습니다.

### Content Cards 캠페인 사용 사례 {#content-card-campaign-use-case}

목록에서 첫 번째 추천 항목으로 Content Cards 캠페인을 실행해 보겠습니다.<br><br>
다음 예제에서는 `user_id` 매개변수를 사용하여
`GET http://<service-endpoint.com>/recommendations?user_id=user123` 엔드포인트를 쿼리하며, 이는 추천 항목 목록을 반환합니다:

```json
[
  {
    "id": "abc123",
    "url": "http://productpage.com/product/abc123",
    "name": "First Item",
    "price": 39.99,
    "image": "http://pp.cdn.com/abvh3321pjb1j"
  },
  {
    "id": "xyz987",
    "url": "http://productpage.com/product/xyz987",
    "name": "Great Item",
    "price": 19.99,
    "image": "http://pp.cdn.com/234bjl1gioj1b2b"
  },
  ...
]
```

Braze 대시보드에서 새 [Content Cards 캠페인]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/)을 생성합니다. 메시지 텍스트 필드에서 연결된 콘텐츠 Liquid 블록을 생성하여 API를 쿼리하고 응답을 `recommendations` 변수에 저장합니다:

{% raw %}

```liquid
{% connected_content https:/<service-endpoint.com>/recommendations?user_id={{${user_id}}} :save recommendations %}
```

그런 다음 결과 배열의 첫 번째 항목을 참조하여 사용자에게 콘텐츠를 표시할 수 있습니다:

```liquid
This seems like a great fit for you:
{% recommendations[0].name %}
{% recommendations[0].price %}
```

{% endraw %}

제목, 이미지를 포함하고 URL을 연결하면 완성된 Content Cards는 다음과 같습니다:

![메시지 본문과 '이미지 추가' 필드에 연결된 콘텐츠가 추가된 캠페인의 이미지입니다. 이 이미지는 사용자를 추천 URL로 연결하는 '웹 URL로 리디렉션' 필드에 추가된 연결된 콘텐츠 로직도 보여줍니다.]({% image_buster /assets/img/amazon_personalize/content-card-campaign.png %})