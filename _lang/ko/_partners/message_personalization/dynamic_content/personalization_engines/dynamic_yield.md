---
nav_title: Dynamic Yield
article_title: Dynamic Yield
description: "이 참조 문서에서는 Braze와 Dynamic Yield 간의 파트너십에 대해 설명합니다. 이번 파트너십을 통해 Dynamic Yield의 추천 및 세분화 엔진을 사용하여 Braze 메시지에 삽입할 수 있는 경험 블록을 만들 수 있습니다."
alias: /partners/dynamic_yield/
page_type: partner
search_tag: Partner

---

# Dynamic Yield

> Mastercard 계열사인 [Dynamic Yield](https://www.dynamicyield.com/)는 다양한 산업의 기업이 개인화되고, 최적화되며, 동기화된 디지털 고객 경험을 제공할 수 있도록 지원합니다. Dynamic Yield의 [Experience OS](http://www.dynamicyield.com/experience-os)를 통해 마케터, 제품 매니저, 개발자, 디지털 팀은 알고리즘을 활용하여 각 고객에게 맞는 콘텐츠, 제품, 오퍼를 매칭하여 매출과 고객 로열티를 가속화할 수 있습니다.

_이 통합은 Dynamic Yield에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Dynamic Yield의 파트너십을 통해 Dynamic Yield의 추천 및 세분화 엔진을 사용하여 Braze 메시지에 삽입할 수 있는 Experience Block을 만들 수 있습니다. Experience Block은 다음으로 구성할 수 있습니다:
{% multi_lang_include partners/message_personalization/dynamic_yield_experience_blocks.md %}

## 전제 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Dynamic Yield 계정 | 이 파트너십을 활용하려면 [Dynamic Yield](https://adm.dynamicyield.com/users/sign_in#/r/dashboard) 계정이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="전제 조건" }

## 통합 {#integration}

### 1단계: Experience Block 만들기 {#step-1-create-an-experience-block}

Dynamic Yield에서 Experience Block을 만들려면 **Email > Experience Emails > Create New**로 이동합니다.

그런 다음 **Create Experience Block**을 선택하여 Braze 이메일 템플릿에 삽입할 동적 콘텐츠 또는 추천 블록을 디자인합니다.<br>![Create Experience Block이 선택된 Dynamic Yield Experience Emails 페이지.]({% image_buster /assets/img/dynamic_yield/dynamic_yield7.png %})

### 2단계: 메시지 작성하기 {#step-2-draft-your-messaging}

다음 이미지는 작성기에서 처음부터 만든 이메일을 보여줍니다.<br>![초안 경험 이메일 레이아웃이 표시된 Dynamic Yield 이메일 작성기.]({% image_buster /assets/img/dynamic_yield/dynamic_yield5.png %})

1. 헤딩 영역에 Campaign 이름, 메모, 레이블을 입력합니다.<br><br>
2. Experience Block을 삽입합니다. 이 블록에는 다음이 포함됩니다:
  - [추천](#configure-a-recommendations-block): 사용자에게 완전히 개인화된 추천을 제공하는 위젯입니다.
  - [동적 콘텐츠](#configure-a-dynamic-content-block): 다양한 오디언스에게 서로 다른 프로모션과 메시지를 타겟팅합니다.<br><br>
3. 설정을 업데이트합니다:
  - URL 파라미터를 사용하여 분석 소프트웨어 내에서 클릭을 추적합니다(선택 사항). 필요에 따라 기본 표시에 파라미터를 추가합니다.
  - 속성 기간을 7일(기본값) 또는 1일 중에서 선택합니다.<br><br>
4. 저장하고 종료합니다. 코드가 생성되기 전에는 언제든지 이메일의 모든 요소를 편집할 수 있습니다. 코드가 생성된 후에는 [코드에 영향을 주지 않는 항목](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZPXB6MH094J1MWS5N86FXH)만 편집할 수 있습니다.

### 추천 블록 구성하기 {#configure-a-recommendations-block}

추천 블록을 사용하면 알고리즘과 필터링을 설정하여 이메일이 열릴 때 전파되는 사용자의 개인화된 콘텐츠를 소싱할 수 있습니다.

1. 편집 창에서 추천 블록을 이메일 본문으로 드래그합니다.<br><br>
2. 원하는 알고리즘(인기도, 사용자 친밀도, 유사성 등)을 선택합니다. 선택한 알고리즘에 따라 추가 옵션이 표시됩니다:
  - 추천이 인기도를 기반으로 하는 경우, 결과를 셔플하여 열람자가 여는 다른 이메일에서 동일한 추천이 제공되는 것을 방지할 수 있습니다.
  - 유사성과 같은 다른 알고리즘은 추천을 제공하기 위해 컨텍스트에 의존하므로 포함할 항목을 선택해야 합니다. 이러한 항목은 작성기에서 추가하거나 [임베드 코드에 병합 태그를 추가](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#advanced)하여 동적으로 만들 수 있습니다. 예를 들어, 배송 확인 이메일에 유사한 항목을 추가할 수 있습니다.<br><br>
3. 사용자가 이미 구매한 제품을 제외하여 해당 제품이 추천되지 않도록 할 수 있습니다.<br><br>
4. [커스텀 필터 규칙](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZP4ZWZX1JJ2SH61MB3HVXD)을 추가하여 특정 제품을 슬롯에 고정하거나, 제품 속성별로 제품을 포함 또는 제외할 수 있습니다. 예를 들어, $5 미만의 제품을 표시하지 않거나 반바지 카테고리의 제품만 표시할 수 있습니다.<br><br>
5. 마지막으로 추천 블록 디자인을 구성합니다. 이를 위해 항목 템플릿을 선택하고, 표시할 항목 수와 행 수를 설정합니다.

### 동적 콘텐츠 블록 구성하기 {#configure-a-dynamic-content-block}
동적 콘텐츠를 사용하여 다양한 사용자에게 서로 다른 프로모션과 메시지를 타겟팅합니다. 타겟팅은 친밀도 또는 오디언스를 기반으로 할 수 있습니다. Dynamic Yield는 이메일이 열릴 때 어떤 개인화된 경험을 제공할지 결정합니다.

1. 편집 창에서 동적 콘텐츠 블록을 이메일 본문으로 드래그합니다.<br><br>
2. 첫 번째 변형에 대한 템플릿을 선택합니다. 이제 디자인 및 콘텐츠 변수를 정의할 수 있습니다. 완료되면 변형을 저장합니다.<br>![Dynamic Yield 동적 콘텐츠 변형 템플릿 편집기.]({% image_buster /assets/img/dynamic_yield/dynamic_yield3.png %})<br><br>
3. 동적 콘텐츠 창에서 오디언스를 설정합니다.<br>![동적 콘텐츠 변형에 대한 Dynamic Yield 오디언스 타겟팅 설정.]({% image_buster /assets/img/dynamic_yield/dynamic_yield4.png %})<br><br>
4. 다른 특정 오디언스 또는 모든 사용자를 타겟팅하기 위해 다른 변형을 추가합니다. 필요에 따라 반복합니다.<br><br>
5. 위아래 화살표를 사용하여 변형의 우선순위를 설정합니다.<br><br>
6. 우선순위는 사용자가 둘 이상의 경험에 적합한 경우 어떤 변형이 제공되는지를 결정합니다.

### 3단계: Braze와 이메일 통합하기 {#step-3-integrate-your-email-with-braze}

이 통합을 통해 Dynamic Yield가 제공하는 개인화된 추천 위젯과 동적 콘텐츠를 Braze 이메일 Campaign에 추가할 수 있습니다. 이러한 Campaign을 Braze Campaign에 임베드하는 것은 Braze 이메일 편집기에 붙여넣는 간단한 임베드 코드로 수행됩니다.

1. Experience Email 목록 페이지에서 ESP 통합 아이콘을 클릭합니다.<br><br>
2. 사용자의 CUID와 이메일 ID를 삽입하는 Braze의 관련 토큰을 입력합니다.<br>![Braze 사용자 토큰 필드가 있는 Dynamic Yield ESP 통합 모달.]({% image_buster /assets/img/dynamic_yield/dynamic_yield2_new.png %})

이메일에 만족하면 다음 단계는 Braze에 임베드할 코드를 생성하는 것입니다.
1. **Experience Emails**에서 **Generate Code**를 클릭합니다.<br><br>
2. 그런 다음 **Copy to Clipboard**를 클릭합니다.<br>![Copy to Clipboard 작업이 있는 Dynamic Yield 생성된 임베드 코드 패널.]({% image_buster /assets/img/dynamic_yield/dynamic_yield.png %})<br><br>
3. Braze 이메일 Campaign에 코드를 붙여넣은 다음, 이메일 Campaign을 계속 디자인하고 테스트하고 게시합니다.