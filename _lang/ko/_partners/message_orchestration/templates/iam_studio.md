---
nav_title: IAM Studio
article_title: IAM Studio
description: "이 참조 문서에서는 개인화된 풍부한 인앱 경험을 만들고 Braze를 통해 전달할 수 있는 메시지 개인화 플랫폼인 IAM Studio와 Braze 간의 파트너십에 대해 설명합니다."
alias: /partners/iam_studio/
page_type: partner
search_tag: Partner

---

# IAM Studio

> [IAM Studio](https://www.inappmessage.com)는 개인화된 풍부한 인앱 경험을 만들고 Braze를 통해 전달할 수 있는 노코드 메시지 개인화 플랫폼입니다.

_이 통합은 IAM Studio에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 IAM Studio 통합을 사용하면 커스터마이즈 가능한 인앱 메시지 템플릿을 Braze 인앱 메시지에 쉽게 삽입할 수 있으며, 이미지 교체, 텍스트 수정, 딥링크 설정, 커스텀 속성 및 이벤트 설정을 제공합니다. IAM Studio를 사용하면 메시지 제작 시간을 줄이고 콘텐츠 기획에 더 많은 시간을 할애할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| IAM Studio 계정 | 이 파트너십을 활용하려면 [IAM Studio 계정](https://www.inappmessage.com/register)이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 사용 사례 {#use-cases}

- 상품 구매 유도
- 사용자 정보 수집
- 회원 가입 증대
- 쿠폰 발행 안내

## 통합 {#integration}

### 1단계: 템플릿 선택 {#step-1-choose-a-template}

인앱 메시지 템플릿 갤러리에서 사용하려는 인앱 메시지 템플릿을 선택하세요.

![IAM Studio 템플릿 갤러리는 '캐러셀 슬라이드 모달', '간단한 아이콘 모달', '모달 전체 이미지' 등 다양한 템플릿을 보여줍니다.]({% image_buster /assets/img/iam_studio/iam_template_gallery.png %})

### 2단계: 템플릿 커스터마이즈 {#step-2-customize-the-template}

먼저 콘텐츠에 맞게 이미지, 텍스트, 버튼을 커스터마이즈합니다. 이미지와 버튼에 **Deeplink**를 연결해야 합니다.

{% tabs local %}
{% tab 이미지 %}
![이미지를 커스터마이즈하는 옵션을 보여주는 IAM Studio UI. 이러한 옵션에는 이미지, 이미지 반경, 이미지 어둡게 하기 등이 있습니다.]({% image_buster /assets/img/iam_studio/iam_customize_image.png %})
{% endtab %}
{% tab 텍스트 %}
![메시지의 제목과 부제목을 커스터마이즈하는 옵션을 보여주는 IAM Studio UI. 이러한 옵션에는 텍스트, 서식 및 글꼴이 포함됩니다.]({% image_buster /assets/img/iam_studio/iam_customize_text.png %})
{% endtab %}
{% tab 버튼 %}
![메인, 왼쪽 및 오른쪽 버튼을 커스터마이즈하는 옵션을 보여주는 IAM Studio UI. 이러한 옵션에는 색상, 딥링크, 텍스트 및 서식이 포함됩니다.]({% image_buster /assets/img/iam_studio/iam_customize_button.png %})
{% endtab %}
{% endtabs %}

다음으로, 커스텀 글꼴을 추가하고 Liquid 태그를 사용하여 개인화된 인앱 메시지를 만듭니다. 로깅 및 추적을 활성화하려면 **Log data and track user behavior**를 선택합니다.

{% tabs local %}
{% tab 글꼴 %}
![Liquid를 추가하는 옵션을 보여주는 IAM Studio UI. 이러한 옵션에는 개인화된 문장을 만드는 것이 포함됩니다.]({% image_buster /assets/img/iam_studio/iam_custom_font.png %})
{% endtab %}
{% tab Liquid %}
![이벤트/속성 로깅을 커스터마이즈하는 옵션을 보여주는 IAM Studio UI. 이러한 옵션에는 해당 사용자 행동 로그가 포함됩니다.]({% image_buster /assets/img/iam_studio/iam_liquid.png %})
{% endtab %}
{% tab 로깅 및 추적 %}
![글꼴을 커스터마이즈하는 옵션을 보여주는 IAM Studio UI. 이러한 옵션에는 사용자가 글꼴 스타일을 커스터마이즈할 수 있는 옵션이 포함됩니다.]({% image_buster /assets/img/iam_studio/iam_tracking_logging.png  %})
{% endtab %}
{% endtabs %}

### 3단계: 템플릿 내보내기 {#step-3-export-the-template}

모든 편집이 완료되면 **Export**를 클릭하여 템플릿을 내보냅니다. 내보내기 후 인앱 메시지 HTML 코드가 생성됩니다. **Copy code** 버튼을 클릭하여 이 코드를 복사합니다.

![생성된 인앱 메시지 HTML과 코드 복사 작업이 표시된 IAM Studio 내보내기 대화 상자.]({% image_buster /assets/img/iam_studio/export_iam_code.png %}){: style="max-width:45%;"}

### 4단계: Braze에서 코드 사용 {#step-4-use-code-in-braze}

Braze로 이동하여 인앱 메시지에서 커스텀 코드를 **HTML Input** 상자에 붙여넣습니다. 메시지가 올바르게 표시되는지 테스트하여 확인하세요.

![IAM Studio HTML이 HTML Input 상자에 붙여넣어진 Braze 인앱 메시지 Campaign 편집기.]({% image_buster /assets/img/iam_studio/braze_campaign_editor.png %}){: style="max-width:85%;"}