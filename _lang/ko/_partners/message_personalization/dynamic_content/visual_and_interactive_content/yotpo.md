---
nav_title: Yotpo
article_title: Yotpo
alias: /partners/yotpo/
description: "이 참조 문서에서는 수천 개의 혁신적인 브랜드가 소비자 직접 판매(D2C) 성장을 가속화할 수 있도록 돕는 선도적인 이커머스 마케팅 플랫폼인 Yotpo와 Braze 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner
---

# Yotpo

> [Yotpo](https://www.yotpo.com/)는 선도적인 이커머스 마케팅 플랫폼으로, 수천 개의 혁신적인 브랜드가 소비자 직접 판매(D2C) 성장을 가속화할 수 있도록 돕습니다. Yotpo의 단일 플랫폼 접근 방식은 리뷰, 로열티, SMS 마케팅 등을 위한 데이터 중심 솔루션을 통합하여 브랜드가 더 스마트하고 전환율이 높은 고객 경험을 만들 수 있도록 지원합니다.

_이 통합은 Yotpo에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Yotpo 통합을 사용하면 Braze 내 이메일 및 기타 커뮤니케이션 채널에서 제품의 별점, 상위 리뷰, 시각적 사용자 생성 콘텐츠(UGC)를 동적으로 가져와 표시할 수 있습니다. 또한 이메일 및 기타 커뮤니케이션 방법에 고객 수준의 로열티 데이터를 포함하여 보다 개인화된 상호작용을 만들고, 매출과 로열티를 높일 수 있습니다.

## 필수 조건 {#prerequisites}

| 필수 조건 | 설명 |
| ----------- | ----------- |
| Yotpo 계정 | 이 파트너십을 활용하려면 Yotpo 계정이 필요합니다. |
| Yotpo 리뷰 API 키 | 이 API는 연결된 콘텐츠 코드 스니펫 내에서 구현됩니다.<br><br>자세한 내용은 [Yotpo 앱 키 및 시크릿 키 찾기](https://support.yotpo.com/en/article/finding-your-yotpo-app-key-and-secret-key)를 참조하세요. |
| Yotpo 로열티 API 키 | 이 API 키와 글로벌 고유 식별자(GUID)는 연결된 콘텐츠 코드 스니펫 내에서 구현됩니다.<br><br>자세한 내용은 [로열티 및 추천 API 키와 GUID 찾기](https://support.yotpo.com/en/article/finding-your-loyalty-referrals-api-key-and-guid)를 참조하세요.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

계속하기 전에 Yotpo 제품 ID가 Braze에서 동적으로 가져올 `product_id`와 동일한지 확인하세요. 이는 통합이 작동하기 위한 필수 사항입니다.

Yotpo 제품 ID를 찾으려면 다음 단계를 수행하세요:

1. 스토어 웹사이트로 이동합니다.
2. 제품 페이지를 엽니다.
3. 마우스 오른쪽 버튼을 클릭하고 **검사**를 선택합니다.
4. <kbd>Control</kbd> + <kbd>F</kbd>를 누르고 코드에서 `yotpo-main`을 검색합니다. `data-product ID` 변수와 해당 값이 Yotpo div에 표시됩니다.

![yotpo-main을 검사하고 검색하여 data-product ID 변수 찾기]({% image_buster /assets/img/yotpo/image1.png %})

## 통합 {#integration}

Yotpo와 Braze를 통합하려면 다음 단계를 수행하세요:

1. Braze 대시보드로 이동합니다.
2. **Campaigns** 페이지에서 **캠페인 생성**을 클릭하고 **Email**을 선택합니다.
3. 원하는 템플릿을 선택합니다.
4. **Edit email body**를 클릭하고 사용 사례에 맞는 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) 스니펫을 추가합니다:
    - [제품의 별점 및 리뷰 수 표시](#star-review-count)
    - [제품의 최근 5점 별점 리뷰 표시](#five-star-review)
    - [제품별 시각적 UGC 표시](#visual-ugc)
    - [이메일에 고객 로열티 잔액 표시](#loyalty-balance)

### 제품의 별점 및 리뷰 수 표시 {#star-review-count}

이 스니펫을 사용하여 이메일에 포함된 제품의 공개 평균 점수와 총 리뷰 수를 제공합니다:

{% raw %}
```liquid
{% connected_content https://api.yotpo.com/products/<YOTPO-API-KEY>/{{event_properties.${product_id}}}/bottomline :save result %}

{% if {{result.response.bottomline.average_score}} != 0 %}

The average rating for this product is:

{{result.response.bottomline.average_score}}/5, based on {{result.response.bottomline.total_reviews}} reviews.

{% else %}
{% endif %}
```
{% endraw %}

`<YOTPO-API-KEY>`를 Yotpo 리뷰 API 키로 교체하세요. `product_id`는 Braze에서 동적으로 가져옵니다. 통합이 작동하려면 Braze의 `product_id`가 Yotpo의 제품 ID(일반적으로 이커머스 상위 제품 ID)와 일치해야 합니다.

![YOTPO-API-KEY를 Yotpo 리뷰 API 키로 교체]({% image_buster /assets/img/yotpo/image2.png %})

### 제품의 최근 5점 별점 리뷰 표시 {#five-star-review}

이 스니펫을 사용하여 이메일에 포함된 특정 제품의 상위(게시된) 리뷰를 제공합니다:

{% raw %}
```liquid
{% connected_content https://api.yotpo.com/v1/widget/<YOTPO-API-KEY>/products/{{event_properties.${product_id}}}/reviews.json?per_page=50&star=5&sort=votes_up :save result %}

{% if {{result.response.reviews[0].score}} == 5 %}

Recent 5 Star Review for this product:

{{result.response.reviews[0].content}}

{% else %}
{% endif %}
```
{% endraw %}

`<YOTPO-API-KEY>`를 Yotpo 리뷰 API 키로 교체하세요. `product_id`는 Braze에서 동적으로 가져옵니다. 통합이 작동하려면 Braze의 `product_id`가 Yotpo의 제품 ID(일반적으로 이커머스 상위 제품 ID)와 일치해야 합니다.

이메일 편집기에서 스니펫은 다음과 같이 표시됩니다:

![최근 별 5개 리뷰에 대한 스니펫을 표시하는 이메일 편집기 예시]({% image_buster /assets/img/yotpo/image3.png %})

### 제품별 시각적 UGC 표시 {#visual-ugc}

이 스니펫을 사용하여 태그가 지정되고 게시된 Yotpo 이미지를 가져와 기본 이미지 대신 또는 추가 갤러리로 이메일에 추가합니다:

{% raw %}
```liquid

{% connected_content https://api.yotpo.com/v1/widget/<YOTPO-API-KEY>/albums/product/{{event_properties.${product_id}}}?per_page=1 :save result %}

{% if {{result.response.images[0].tagged_products[0].image_url}} != null %}

The Visual content of the product:

<img src="{{result.response.images[0].tagged_products[0].image_url}}" border="0" width="200" height="200" alt="" />

{% else %}

Image return NULL

{% endif %}
```
{% endraw %}

`<YOTPO-API-KEY>`를 Yotpo 리뷰 API 키로 교체하세요. `product_id`는 Braze에서 동적으로 가져옵니다. 통합이 작동하려면 Braze의 `product_id`가 Yotpo의 제품 ID(일반적으로 이커머스 상위 제품 ID)와 일치해야 합니다.

스니펫은 다음과 비슷하게 표시됩니다:

![Yotpo에 게시된 이미지 스니펫을 보여주는 이메일 편집기 예시]({% image_buster /assets/img/yotpo/image4.png %})

### 이메일에 고객 로열티 잔액 표시 {#loyalty-balance}

이 스니펫을 사용하여 고객의 로열티 포인트 잔액을 가져와 이메일 메시징에 활용합니다:

{% raw %}
```liquid
{% connected_content

https://loyalty.yotpo.com/api/v2/customers?customer_email=**{{${email_address}}}**
:method get
:headers {
    "x-guid": "<YOTPO-LOYALTY-GUID>",
    "x-api-key": "<YOTPO-LOYALTY-API-KEY>"
        }
:content_type application/json
:save publication
%}

You have {{publication.points_balance}} points

Only {{publication.vip_tier_upgrade_requirements.points_needed}} more points to become part of our VIP Tier!
```
{% endraw %}

`<YOTPO-LOYALTY-GUID>`와 `<YOTPO-LOYALTY-API-KEY>`를 Yotpo 로열티 자격 증명으로 교체하세요. `email_address`는 Braze에서 동적으로 가져옵니다. 통합이 작동하려면 이메일이 이메일을 수신하는 고객의 이메일 주소여야 합니다.

스니펫은 다음과 비슷하게 표시됩니다:

![고객 로열티 잔액 스니펫을 보여주는 이메일 편집기 예시]({% image_buster /assets/img/yotpo/image5.png %})

## 자주 묻는 질문 {#faq}

### 5점 별점 리뷰가 없으면 어떻게 되나요? {#what-if-i-dont-have-a-5-star-review}

5점 별점 리뷰가 없는 경우(예: 엔드포인트 응답이 5점 별점 리뷰에 대해 NULL을 반환하는 경우) 콘텐츠가 표시되지 않습니다.

### 제품에 게시된 이미지가 없으면 어떻게 되나요? {#what-if-i-dont-have-an-image-published-for-a-product}

제품에 이미지가 없는 경우(예: 엔드포인트 응답이 제품 이미지에 대해 NULL을 반환하는 경우) 콘텐츠가 표시되지 않습니다.

### 디자인을 커스터마이즈하거나 Yotpo에서 다른 데이터 필드를 가져올 수 있나요? {#can-i-customize-the-look-and-feel-or-pull-other-data-fields-from-yotpo}

네! 사용 가능한 다른 데이터 포인트와 커스터마이즈 옵션을 알아보려면 [API 호출하기]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/)를 참조하세요. 이를 위해 프론트엔드 개발자의 도움이 필요할 수 있습니다.

{% alert note %}
Yotpo는 이 가이드에 설명된 것 이상의 커스텀 요구 사항을 지원하지 않습니다.
{% endalert %}