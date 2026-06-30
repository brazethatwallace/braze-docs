---
nav_title: "Gmail 프로모션 탭"
article_title: "Gmail 프로모션 탭"
page_order: 8
description: "이 참조 문서에서는 Braze를 사용하여 이메일 캠페인에서 Gmail 모바일 프로모션 카드를 구축하는 방법을 다룹니다."
channel:
  - email
toc_headers: h2
---

# Gmail 프로모션 탭 {#gmail-promotions-tab}

> [Gmail 모바일 프로모션 탭](https://developers.google.com/gmail/promotab/)을 사용하면 마케터가 제목란이나 프리헤더 정보만이 아닌 "카드"의 주석을 통해 더 많은 정보를 전달할 수 있습니다. Braze에는 이메일 캠페인에서 카드를 구축하는 데 도움이 되는 내장 도구가 있습니다.

## 필수 조건 {#prerequisites}

먼저, 도메인과 하위 도메인을 Google의 프로모션 탭 아웃리치 팀 <a href="mailto:p-promo-outreach@google.com">p-promo-outreach@google.com</a> 에 전달하여 Gmail의 허용 목록에 추가하세요. 이를 통해 Gmail 프로모션 탭의 제품 캐러셀과 같은 풍부한 이미지를 보여주는 모든 기능을 사용할 수 있습니다.

## Braze로 카드 만들기 {#build-the-card-with-braze}

다음 단계를 따라 이메일 캠페인을 위한 Gmail 프로모션 카드를 구축하세요. 편집기에서 **콘텐츠** 섹션을 벗어나면 **Gmail 프로모션** 탭의 필드와 정보가 초기화됩니다. 프로모션 카드의 설정을 완료하고 생성된 HTML을 복사하여 HTML 코드를 잃지 않도록 하세요.

### 1단계: 이메일 캠페인 만들기 {#step-1-create-an-email-campaign}

먼저, [이메일 캠페인을 만들고]({{site.baseurl}}/user_guide/channels/email/html_editor) 편집 환경으로 **HTML 코드 편집기**를 선택하세요.

### 2단계: Gmail 프로모션 카드에 세부 정보 추가 {#step-2-add-details-to-gmail-promotion-card}

다음으로, HTML 편집기의 **콘텐츠** 섹션으로 이동하여 **Gmail 프로모션** 탭을 선택하세요. **기본 정보** 아래의 필드를 작성한 후 **HTML 코드 생성**을 선택하세요. 이렇게 하면 **HTML 코드를 `<Head>`에 복사하여 붙여넣기** 섹션 아래에 Gmail 프로모 탭 카드의 스크립트가 생성됩니다.

![카드를 구축하는 방법의 예시.]({% image_buster /assets/img/create-gmail-promo.png %})

### 3단계: Gmail 프로모션 카드 커스터마이즈 {#step-3-customize-your-gmail-promotion-card}

Gmail 프로모션 카드에 할인 제안, 딜 카드, 프로모션 카드 또는 모든 옵션을 포함할지 선택하세요.

{% tabs %}
{% tab 할인 제안 %}

할인 제안을 설정하면 할인의 유효 날짜를 지정할 수 있습니다.

1. **Discount Offer** 토글을 선택하세요.
2. **Offer**에 할인에 대한 간단한 요약을 입력하세요. 예: "20% off".
3. **Code**에 사용자가 결제 시 적용해야 하는 프로모션 코드를 추가하세요.
4. 그런 다음, 할인 제안의 시작 날짜와 시간을 선택하세요.
5. 할인 제안이 특정 시간에 종료되어야 하는지 또는 종료되지 않아야 하는지 결정하세요.

![할인 제안의 제안 값, 코드, 시작 날짜 및 시간을 지정하는 옵션.]({% image_buster /assets/img/gmail_promo_discount_details.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab 딜 카드 %}

딜 카드를 사용하면 이메일 본문 상단에 주요 딜 정보를 직접 제공할 수 있습니다. 이를 통해 수신자가 제안 세부 정보를 빠르게 파악하고 조치를 취할 수 있습니다. 예를 들어, 딜 카드를 사용하여 한정 기간 제안을 홍보하고 사용자가 이메일 내에서 세부 정보를 찾아야 하는 번거로움을 줄일 수 있습니다.

1. **Deal Card** 토글을 선택하세요.
2. **Offer**에 할인에 대한 간단한 요약을 입력하세요. 예: "20% off all shoes".
3. (선택 사항) **Code**에 사용자가 결제 시 적용해야 하는 프로모션 코드를 추가하세요.
4. 다음 URL 중 하나 이상을 입력하세요.
-  **Offer Page URL:** 특정 제안 랜딩 페이지의 URL입니다. "Shop now"(또는 유사한) 버튼이 생성됩니다. 딜 카드에 이 URL을 제공하는 것을 권장합니다.
- **Merchant Homepage URL:** 메인 홈페이지의 URL입니다. 특정 제안 페이지 URL을 사용할 수 없는 경우에만 이 필드를 사용하세요.
5. (선택 사항) 제안의 시작 날짜를 추가하세요.
6. 제안이 특정 시간에 종료되어야 하는지 또는 종료되지 않아야 하는지 결정하세요.

![딜 카드의 제안 값, 코드, 시작 날짜 및 시간을 지정하는 옵션.]({% image_buster /assets/img/gmail_promo_deal_cards.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab 프로모션 카드 %}

제품 캐러셀의 프로모션 카드는 제안에 이미지를 제공하는 데 유용합니다. 제품 캐러셀의 변수를 커스터마이즈하고 최대 10개의 이미지 미리보기를 포함할 수 있으며, 각 이미지는 고유해야 합니다.

1. **Promotion Cards** 토글을 선택하세요.
2. **Add promotion card**를 선택하세요. 제품 캐러셀의 각 이미지는 고유한 URL을 가져야 하며 동일한 종횡비(4:5, 1:1, 1.91:1)를 사용해야 합니다.
3. 이미지 URL을 포함하세요.
4. **Target URL**에 프로모션 링크를 추가하세요.

{% alert tip %}
제품 이미지를 미디어 라이브러리에 업로드한 다음 URL을 복사하여 적절한 필드에 붙여넣는 것을 권장합니다. 정적 이미지 형식(PNG 및 JPEG)만 허용됩니다. 일부 이미지 형식(GIF)은 업로드되지만 예상대로 표시되지 않습니다.
{% endalert %}

{: start="5"}
5. 헤드라인, 통화, 가격 및 할인 값을 추가하여 프로모션 카드를 커스터마이즈하세요.

| 커스터마이즈 가능한 등록정보 | 설명 |
|---|---|
| 헤드라인 | (선택 사항) 프로모션에 대한 한두 문장의 설명입니다. 미리보기 이미지 아래에 표시됩니다. |
| 통화 | (선택 사항) 가격의 통화입니다. |
| 가격 | 프로모션의 가격입니다. |
| 할인 값 | 원래 가격에서 할인된 금액입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="3단계: Gmail 프로모션 카드 커스터마이즈" }

![Motto라는 회사의 제품 캐러셀 예시로, 이메일 제목이 "베스트셀러 양말 세일 중"이며 양말 이미지 3개와 할인 가격이 표시되어 있습니다.]({% image_buster /assets/img_archive/product_carousel.png %}){: style="max-width:40%;"}

{% endtab %}
{% endtabs %}

### 4단계: HTML 코드 생성 및 붙여넣기 {#step-4-generate-and-paste-html-code}

Gmail 프로모션 카드를 구축한 후 **Generate HTML code**를 선택하세요. 스크립트를 복사하여 이메일 HTML의 `<head>` 요소에 붙여넣으세요.

{% alert tip %}
드래그 앤 드롭 편집기의 경우, 생성된 HTML 코드를 **Sending Settings** 아래의 [커스텀 헤드 태그]({{site.baseurl}}/user_guide/channels/email/drag_and_drop#custom-head-tags) 섹션에 복사하여 붙여넣으세요.
{% endalert %}

{% alert warning %}
프로모션 스크립트는 이메일이 Gmail 프로모션 탭에 도착한 경우에만 표시됩니다. 현재 Gmail은 알고리즘을 사용하여 이메일이 어디에 도착할지 결정합니다. 그러나 사용자가 이메일을 프로모션으로 표시하면 Gmail의 알고리즘이 무시되고 이후 이메일이 자동으로 프로모션 탭에 도착합니다.
{% endalert %}

### 5단계: Gmail의 미리보기 도구로 테스트 {#step-5-test-using-gmails-preview-tool}

소량 발송에 대한 주석을 테스트하려면 먼저 Gmail의 [미리보기 도구](https://developers.google.com/workspace/gmail/promotab/preview)를 사용하여 주석을 검증해야 합니다. 이 단계를 건너뛰면 제품 캐러셀과 단일 이미지 미리보기가 더 많은 발송량에서만 트리거됩니다.

## Gmail 카드 측정 {#measure-gmail-cards}

Gmail은 이러한 카드에 대한 분석을 반환하지 않으며, Braze와 같은 이메일 서비스 공급자(ESP)는 헤더 섹션의 링크(프로모션 카드 및 제품 캐러셀 포함)에 자체 링크 추적을 삽입할 수 없습니다. 그러나 설정 중에 URL에 UTM 매개변수 또는 고유 코드를 추가할 수 있습니다. 이러한 매개변수를 사용하면 추적이 ESP가 삽입하는 것이 아니라 URL 자체의 일부이므로 자체 웹사이트 분석 또는 전환 추적을 사용하여 참여를 추적할 수 있습니다. 이러한 링크에 대해서는 ESP 수준의 클릭 추적을 사용할 수 없습니다.

### 이미지 활용 {#incorporate-images}

Gmail은 이메일 메시지와 관련된 강력한 이미지를 사용할 때 더 나은 결과를 보였습니다. Gmail은 이 공간이 이메일 마케팅에 필수적인 시각적 언어를 미리보기에 가져오도록 설계되었으므로 텍스트만 사용하는 디자인을 권장하지 않습니다. 텍스트가 잘린 이미지를 사용하거나 여러 Campaign에서 이미지를 반복 사용하지 마세요.

### 제안 설명 {#describe-offers}

Gmail은 "1+1 무료 또는 모든 반바지와 셔츠 할인"과 같은 문장이나 구문을 사용하는 것을 권장하지 않습니다. 이러한 문구는 잘릴 수 있고, 더 이상 시선을 끌지 못하며, 제목란과 경쟁하게 됩니다. 이 공간은 메시징으로 고객의 참여를 유도하는 데만 사용해야 하므로 "지금 이 이메일을 열어보세요" 또는 "여기를 클릭하여 할인 받기"와 같은 문구는 피하세요. 제목란을 반복하지 않는 것이 가장 좋습니다.

## 모범 사례 {#best-practices}

일반적으로 [Gmail의 프로모션 탭 모범 사례](https://developers.google.com/gmail/promotab/best-practices)를 따르세요.

카드를 구축할 때 다음 질문을 고려하세요:

- 주석 스크립트가 유효한가요? [Google로 미리보기](https://developers.google.com/workspace/gmail/promotab/preview)하세요.
- Gmail에서 **Show original**을 하면 원시 메시지에 스크립트가 표시되나요?
- 메일이 **Promotions**에 도착하나요? 카드는 프로모션 탭에서만 적용됩니다.
- 데스크탑과 모바일에서 테스트했나요?

{% alert tip %}
스크립트에서 Liquid을 지원하지만, 오류를 방지하기 위해 철저히 테스트하는 것을 권장합니다.
{% endalert %}

### 주석 미리보기 {#preview-your-annotation}

[미리보기 도구](https://developers.google.com/workspace/gmail/promotab/preview)를 사용하여 주석을 미리보기하세요. 주석은 이메일이 상당수의 수신자에게 발송되어야만 렌더링되므로 테스트 이메일을 자신에게 보내는 것은 주석 확인에 적합하지 않습니다. 최종 이메일(이미지 URL 포함)을 최소 100명의 Gmail 수신자에게 발송하세요.

주석이 포함된 이메일을 보내는 데 Google Workspace를 사용하지 마세요. 허용 목록에 등록된 이메일 도메인만 사용하여 대규모 수신자 그룹에 주석을 보내세요.

### 이미지 가이드라인 준수 {#adhere-to-image-guidelines}

이미지가 다음 가이드라인을 준수하는지 확인하세요:
- 고품질 및 고해상도 이미지를 사용하세요.
- 모든 주석 이미지는 동일한 종횡비를 사용합니다. 지원되는 종횡비: 4:5, 1:1, 1.91:1.
- 올바른 이미지 크기를 사용하세요. 최소 256x256, 최대 4096x4096 픽셀입니다.

Gmail은 다음을 피할 것을 권장합니다:
- 이미지에 텍스트를 과도하게 사용하는 것
- 아이콘만 있는 이미지를 사용하는 것
- 둥근 마스크가 있는 이미지를 사용하는 것
- 개인화된 이미지 URL을 사용하는 것

### DMARC에 등록 {#register-with-dmarc}

주석이 올바르게 렌더링되려면 제출된 도메인이 DMARC에 등록되어 있고 모든 정책이 활성화되어 있는지 확인하세요.

## 자주 묻는 질문 {#frequently-asked-questions}

### 발신자 로고를 어떻게 추가하나요? {#how-do-i-add-a-sender-logo}

[Google 주석](https://developers.google.com/workspace/gmail/promotab/overview)을 사용하여 Gmail 앱에서 로고와 프로모션 카드를 추가하세요. 렌더링은 Braze가 아닌 Gmail에 의해 제어됩니다.

### 프로모션 메시지가 최종 사용자의 받은편지함에 프로모션 카드나 제품 캐러셀을 표시하지 않는 이유는 무엇인가요? {#why-is-my-promotional-message-not-displaying-the-promotion-card-or-product-carousel-in-the-end-users-inbox}

Gmail 프로모션 탭에 제품 캐러셀이 표시되는지 여부를 결정하는 많은 요인이 있습니다.

주석의 모든 이미지는 여전히 품질 필터를 통과해야 합니다. 제품 캐러셀이 채워지려면 주석의 모든 이미지가 권장 이미지 종횡비여야 하고 고품질, 고해상도의 클로즈업 제품 이미지여야 합니다. 이미지에는 텍스트가 거의 또는 전혀 포함되지 않아야 합니다. 품질 필터는 부적절한 콘텐츠도 필터링하므로 이미지는 가족, 사용자 및 아동에게 적합해야 합니다.

또한 Gmail은 사용자의 Gmail 프로모션 탭에 표시되는 제품 캐러셀 수에 밀도 제한을 두고 있습니다. 예를 들어, 사용자가 프로모션 이메일에 제품 캐러셀을 사용하는 많은 브랜드를 구독하면 Gmail은 결국 표시되는 제품 캐러셀 수에 제한을 둡니다.

Google의 개인정보 보호 및 안전 규정으로 인해 주석이 포함된 이메일은 주석이 작동하려면 광범위하게 발송되어야 합니다. Campaign을 시작하고 Google의 시스템이 "대량 발송"으로 감지할 수 있도록 최소 100명의 수신자에게 발송하는 것이 권장됩니다. 이미지 URL은 수신자마다 다를 수 없습니다.

### 프로모션 카드나 제품 캐러셀의 클릭은 어떻게 추적되나요? {#how-are-clicks-on-a-promotion-card-or-product-carousel-tracked}

Braze 또는 다른 ESP는 헤더 섹션의 링크에 링크 추적을 삽입할 수 없습니다. 이는 프로모션 카드나 제품 캐러셀에서 클릭을 추적할 수 없음을 의미합니다.

### 제품 캐러셀을 받은 사용자 수를 확인할 수 있는 방법이 있나요? {#is-there-a-way-to-see-how-many-users-received-a-product-carousel}

Gmail이 카드를 언제 누구에게 표시할지 결정하므로 모든 수신자가 제품 캐러셀을 볼 것이라는 보장은 없습니다.

### Gmail 프로모션 탭에서 주석이 보이지 않는 이유는 무엇인가요? {#why-dont-i-see-annotations-in-my-gmail-promotions-tab}

주석은 Google Workspace에서 지원되지 않습니다. 주석을 미리보려면 Gmail로 개인 이메일 주소를 만들 수 있습니다.

주석은 **Primary** 탭이나 Gmail 모바일 앱의 다른 탭에서는 렌더링되지 않습니다. 사용자가 이메일을 연 후에는 주석이 표시되지 않으며, `DiscountOffer` 주석 유형을 사용하고 시간과 날짜가 이미 만료된 경우에도 표시되지 않습니다.

{% alert tip %}
더 많은 문제 해결 방법은 [Google의 이메일 프로모션 문제 해결 가이드](https://developers.google.com/workspace/gmail/promotab/troubleshooting)를 참조하세요.
{% endalert %}