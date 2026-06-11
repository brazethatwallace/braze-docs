---
nav_title: Smartling
article_title: Smartling
description: "이 참조 문서에서는 Braze와 현지화를 위한 클라우드 기반 소프트웨어인 Smartling 간의 파트너십을 설명합니다. Braze 커넥터는 HTML 이메일 템플릿, Content Blocks, Canvases 및 Campaign 이메일 메시지의 번역을 지원합니다."
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> [Smartling](https://www.smartling.com/)은 웹사이트, 애플리케이션 및 고객 경험의 번역을 자동화하려는 고객을 위한 엔드투엔드 클라우드 번역 관리 소프트웨어입니다.

_이 통합은 Smartling에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

Braze 커넥터는 Campaigns와 Canvases(이메일, 푸시, 인앱 메시지 및 배너), 이메일 템플릿 및 Content Blocks의 메시지 번역을 지원합니다. 각 채널 또는 기능에 대해 지원되는 편집기 유형을 알아보려면 다음 표를 참조하세요.

| 채널/기능 | 기존 편집기(예: HTML) | 드래그 앤 드롭 편집기 |
| --------------- | ----------------------------- | -------------------- |
| [이메일]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email) | ✅ | ✅ |
| [IAM]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message) | ✅ | ✅ |
| [푸시]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push) | ✅ | 해당 없음 |
| 이메일 템플릿 | ✅ | ✅ |
| 배너 | 해당 없음 | ✅ |
| Content Blocks | ✅ | ✅ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="About the integration" }


## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Smartling 계정 | 이 파트너십을 이용하려면 [Smartling 계정](https://dashboard.smartling.com/)이 필요합니다. |
| Smartling 번역 프로젝트 | Braze 계정을 Smartling에 연결하려면 먼저 로그인하고 [번역 프로젝트를 생성](https://help.smartling.com/hc/en-us/articles/115003074093)해야 합니다. |
| Braze REST API 키 | 다음 권한이 있는 Braze REST API 키: <br>- campaigns.translations.get<br>- campaigns.translations.update<br>- campaigns.list<br>- campaigns.details<br>- canvas.translations.get<br>- canvas.translations.update<br>- campaigns.details<br>- templates.email.create<br>- templates.email.update<br>- templates.email.list<br>- templates.email.info<br>- templates.translations.get<br>- templates.translations.update<br>- content_blocks.info<br>- content_blocks.list<br>- content_blocks.create<br>- content_blocks.update<br><br> Braze 대시보드의 **설정 > API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/api/basics/#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
| Braze 다중 언어 설정 | [Braze에서 다중 언어 설정 완료]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 {#integration}

### 1단계: Braze에서 다중 언어 설정 구성하기 {#step-1-set-up-multi-language-settings-in-braze}

Braze에서 로캘을 설정하려면 [Braze의 다중 언어 설정 안내]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites)를 참조하세요.

### 2단계: Smartling TMS에서 Braze 프로젝트 설정하기 {#step-2-set-up-the-braze-project-in-smartling-tms}

커넥터 구성에 대한 자세한 내용은 [Smartling 설명서](https://help.smartling.com/hc/en-us/articles/13248549217435)를 참조하세요.

### Braze를 Smartling에 연결하기 {#connecting-braze-to-smartling}

1. [Smartling 계정](https://dashboard.smartling.com/)에서 [Braze 커넥터](https://help.smartling.com/hc/en-us/articles/115003074093) 프로젝트 유형을 생성합니다.

![Smartling에서의 Braze 연결.]({% image_buster /assets/img/smartling/image1_Connecting_Braze_to_Smartling.png %})

{: start="2"}
2. 이 프로젝트에서 **Settings** > **Braze Settings** > **Connect to Braze**를 선택합니다.
3. API URL 및 API 키와 같은 필수 필드를 작성합니다. 테스트 연결이 성공하면 연결을 저장합니다. 테스트가 실패하면 올바른 API URL과 API 키를 입력했는지 확인하세요.

![Smartling API 설정에서의 Braze 연결.]({% image_buster /assets/img/smartling/image2_API.png %})

{: start="4"}
4. 프로젝트 언어를 추가합니다.

![Smartling 프로젝트 언어에서의 Braze 연결.]({% image_buster /assets/img/smartling/image3_project_languages.png %})

{: start="5"}
5. Braze 설정에서 **Target Language (Braze)** 열의 값이 Braze 다중 언어 설정에서 구성된 로캘과 일치하는지 확인합니다. 로캘 명명 규칙이 정확히 일치해야 합니다.

![Smartling 언어 확인에서의 Braze 연결.]({% image_buster /assets/img/smartling/image4_language_confirmation.png %})

### 3단계: Braze 메시지에 번역 태그 추가하기 {#step-3-add-translation-tags-to-your-braze-message}

메시지에 번역 태그를 추가하는 방법은 [Braze의 안내]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/?tab%3Dhtml%2520editor#prerequisites)를 참조하세요:

- [이메일]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email)
- [푸시]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push)
- [인앱 메시지]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message)

다음은 번역 태그가 포함된 HTML 이메일 Campaign의 예입니다.

![번역 태그가 포함된 Braze 이메일.]({% image_buster /assets/img/smartling/image5_translation_tags.png %})

로캘을 선택하려면 먼저 메시지를 초안으로 저장해야 합니다.

### 4단계: Smartling에서 번역 관리하기 {#step-4-manage-translations-in-smartling}

커넥터를 연결하고 설정한 후 Smartling 프로젝트의 Braze 탭에서 Braze 콘텐츠를 찾을 수 있습니다. 자세한 내용은 [Smartling 설명서](https://help.smartling.com/hc/en-us/articles/13248577069979)를 참조하세요.

Smartling은 다음과 같은 고급 기능을 제공하여 콘텐츠를 검색하고 선택할 수 있습니다:
- 키워드 검색
- Braze 콘텐츠 유형
- Braze 태그 지정

1. 이 예제에서는 [3단계](#step-3-add-translation-tags-to-your-braze-message)에서 새해 프로모션 이메일 Campaign을 만들었습니다.

![번역 태그가 포함된 Braze 이메일.]({% image_buster /assets/img/smartling/image6_ny_promotion.png %})

{: start="2"}
2. 번역하려는 Campaign을 찾은 후 폴더를 선택하고 배리언트를 선택한 다음 **Request Translation**을 선택합니다.

![번역 요청하기.]({% image_buster /assets/img/smartling/image7_request_translation.png %})

{: start="3"}
3. 번역을 위한 새 작업을 만듭니다.

![번역을 위한 새 작업 만들기.]({% image_buster /assets/img/smartling/image8_request_translation.png %})

{: start="4"}
4. 작업이 승인된 후 CAT 도구에서 각 번역을 편집합니다.

![번역 CAT 도구.]({% image_buster /assets/img/smartling/image9_translation_job.png %})

{: start="5"}
5. 번역이 완료되면 번역을 저장하고 Braze에 제출합니다.

![Braze에 번역 제출하기.]({% image_buster /assets/img/smartling/image10_translations.png %})

### 5단계: Braze에서 다중 언어 사용자로 메시지 미리보기 {#step-5-preview-the-message-as-a-multi-language-user-in-braze}

Braze에서 다중 언어 사용자로 Campaign을 미리 보고 번역이 올바르게 적용되었는지 확인합니다.

![다중 언어 사용자 미리보기.]({% image_buster /assets/img/smartling/image11_preview.png %})

## 자주 묻는 질문 {#frequently-asked-questions}

### 드래그 앤 드롭 편집기에서 번역 태그가 지원되나요? {#are-translation-tags-supported-for-the-drag-and-drop-editor}

드래그 앤 드롭 편집기(이메일, 콘텐츠 블록, 인앱 메시지)의 경우 번역 태그를 Liquid 태그로 수동 추가해야 합니다.

### Liquid 태그 내의 텍스트는 어떻게 번역하나요? {#how-do-you-translate-text-within-a-liquid-tag}

Smartling은 Liquid 태그를 인식하여 컴포저에서 편집할 수 없는 변수로 만듭니다. 기본값 텍스트나 join과 같은 필터 등 Liquid 태그 내의 다른 텍스트도 Smartling에서 편집할 수 없게 됩니다. 하지만 Smartling에서 Liquid 태그를 제거한 후 번역된 기본값 텍스트로 Liquid 태그를 다시 생성할 수 있습니다. 번역을 저장할 때 경고가 표시됩니다.