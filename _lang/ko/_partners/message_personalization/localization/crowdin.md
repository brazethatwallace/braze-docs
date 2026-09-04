---
nav_title: Crowdin
article_title: Crowdin
description: "Crowdin 통합을 사용하여 번역 메모리, 용어집, 기계 번역을 활용해 Campaigns, Canvas 경험, 이메일 템플릿, Content Blocks를 번역할 수 있습니다."
alias: /partners/crowdin/
page_type: partner
search_tag: Partner

---

# Crowdin

> [Crowdin](https://crowdin.com/)은 인공지능 기반 현지화 관리 플랫폼으로, 팀이 소프트웨어, 앱, 마케팅 콘텐츠의 번역을 자동화할 수 있도록 도와줍니다.

Crowdin을 Braze에 연결하여 Campaigns과 Canvas 경험의 번역을 관리할 수 있습니다. 자동 동기화는 기계 번역, 번역 메모리, 용어집과 함께 작동하여 수동 및 자동화 워크플로의 일관성을 유지합니다.

_이 통합은 Crowdin에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

Crowdin은 Braze를 위한 두 가지 앱을 제공합니다: [Braze Campaigns & Canvas](https://store.crowdin.com/braze-content-translation)와 [Braze Email Templates](https://store.crowdin.com/braze-app). 현지화하려는 Braze 기능에 따라 선택하세요. 다음 표에서 두 앱을 비교합니다.

### 적합한 Crowdin 앱 선택하기 {#choose-the-right-crowdin-app}

| 채널 또는 기능 | Braze Campaigns & Canvas | Braze Email Templates |
| --- | --- | --- |
| **Campaigns** | ✅ 지원됨 | ❌ 지원되지 않음 |
| **캔버스 단계** | ✅ 지원됨 | ❌ 지원되지 않음 |
| **이메일 템플릿** | ❌ 지원되지 않음 | ✅ 지원됨 |
| **Content Blocks** | ❌ 지원되지 않음 | ✅ 지원됨 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="적합한 Crowdin 앱 선택하기" }

## 사전 요구 사항 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| **Crowdin 계정** | [Crowdin.com 계정](https://accounts.crowdin.com/register) 또는 [Crowdin Enterprise 계정](https://accounts.crowdin.com/workspace/create)이 필요합니다. |
| **Crowdin 프로젝트** | Braze에 연결하기 전에 Crowdin 또는 Crowdin Enterprise에서 [번역 프로젝트를 생성](https://support.crowdin.com/creating-project/)해야 합니다. |
| **Braze REST API 키** | Campaigns, Canvas, Content Blocks, 커스텀 속성, 이메일 및 템플릿에 대한 권한이 있는 Braze REST API 키가 필요합니다. |
| **Braze REST 엔드포인트** | 사용자의 특정 Braze REST 엔드포인트 URL(예: `https://rest.iad-03.braze.com`)입니다. |
| **Braze 다국어 설정** | Braze 대시보드의 **설정** > **현지화 설정**에서 로캘을 구성해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사전 요구 사항" }

## Braze Campaigns & Canvas 통합 {#braze-campaigns-canvas-integration}

실시간 메시지 내의 콘텐츠를 현지화하려면 [Braze Campaigns & Canvas 앱](https://store.crowdin.com/braze-content-translation)을 사용하여 Campaign 및 Canvas 초안에서 번역 가능한 문자열을 Braze 다국어 지원과 동기화하세요.

비디오 안내는 [Braze Campaigns & Canvas 통합](https://youtu.be/ahG1ET4VRKA)을 참조하세요.

### 1단계: Braze에서 다국어 설정 구성 {#step-1-set-up-multi-language-settings-in-braze}

Crowdin을 연결하기 전에 Braze에서 대상 언어를 추가하세요.

1. Braze에서 **설정** > **현지화 설정**으로 이동합니다.
2. 지원할 언어를 추가합니다.

![설정 아래의 Braze 로케일 페이지로, 로케일 이름, 로케일 키, 로케일 추가가 표시됩니다.]({% image_buster /assets/img/crowdin/braze_locales.png %})

{: start="3"}
3. 각 **로케일 키**(예: `en-US`, `fr-FR`, `es-ES`)를 기록해 두세요. Crowdin에서 언어를 매핑할 때 이 값을 사용합니다.

### 2단계: Crowdin에서 Braze 프로젝트 설정 {#step-2-set-up-the-braze-project-in-crowdin}

1. Crowdin Enterprise 또는 Crowdin.com 계정에서 탐색 메뉴의 **Store**로 이동합니다.
2. **Braze Campaigns & Canvas**를 검색한 다음 **Install**을 선택합니다.

![Braze Campaigns & Canvas가 선택되고 Install이 강조 표시된 Crowdin Store 화면.]({% image_buster /assets/img/crowdin/crowdin_store_campaigns_canvas.png %})

{: start="3"}
3. 이 통합을 사용할 프로젝트를 선택합니다.
4. 통합을 열려면 프로젝트의 **Integrations** > **Braze Campaigns & Canvas**로 이동합니다.

#### Braze를 Crowdin에 연결 {#connecting-braze-to-crowdin}

Braze API 자격 증명으로 연결을 인증합니다:

![REST API 키, REST 엔드포인트, Log in with Braze Campaigns & Canvas가 표시된 Crowdin Braze Campaigns & Canvas 연결 양식.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_login.png %})

- **Braze REST API 키:** Braze에서 **설정** > **API 및 식별자** > **API 키**에서 생성합니다. 이 통합에 필요한 권한(Campaigns, Canvas, Content Blocks, 커스텀 속성)을 부여하세요.
- **Braze REST 엔드포인트:** Braze 인스턴스의 URL을 입력합니다(예: `https://rest.iad-03.braze.com`). 자세한 내용은 [REST API 엔드포인트]({{site.baseurl}}/api/basics#endpoints)를 참조하세요.

![API 키 생성 및 REST 엔드포인트 복사 컨트롤이 표시된 Braze REST API 키 페이지.]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %})

**Log in with Braze Campaigns & Canvas**를 선택합니다.

### 3단계: Crowdin에서 언어 매핑 구성 {#step-3-configure-language-mapping-in-crowdin}

계정을 연결한 후 각 Crowdin 프로젝트 언어를 해당하는 Braze 로케일에 매핑합니다.

1. **Braze Campaigns & Canvas** 통합 대시보드에서 상단 작업 표시줄의 **설정** 기어 아이콘을 선택합니다.

![상단 작업 표시줄에 설정이 표시된 Braze Campaigns & Canvas 통합 화면.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_settings.png %})

{: start="2"}
2. **General Settings** 탭을 엽니다.
3. 로케일 키를 입력합니다. Crowdin에 프로젝트 언어(예: 프랑스어, 이탈리아어)가 나열됩니다. 각 필드에 해당하는 **Braze 로케일 키**를 입력합니다.
   - 예를 들어 Braze에서 이탈리아어에 `it`를 사용하면 Crowdin에서 이탈리아어 옆에 `it`를 입력합니다.
   - 각 항목은 Braze **현지화 설정**에서 해당 로케일의 **로케일 키**와 정확히 일치해야 합니다.

![General Settings 탭의 설정 모달로, 파일 필터 필드와 언어 매핑 행(예: 프랑스어가 fr에 매핑)이 표시됩니다.]({% image_buster /assets/img/crowdin/crowdin_language_mapping_settings.png %})

{: start="4"}
4. **Save**를 선택하여 매핑을 확인합니다.

### 4단계: Braze 메시지에 번역 태그 추가 {#step-4-add-translation-tags-to-your-braze-message}

Crowdin은 Braze가 다국어 메시지에 사용하는 것과 동일한 Liquid **번역 태그**를 읽습니다. 번역하려는 모든 텍스트, 이미지 URL, 링크 URL을 {% raw %}`{% translation your_id_here %}`와 `{% endtranslation %}`{% endraw %}로 감싸세요. 각 블록에는 고유한 `id`(예: `greeting` 또는 `welcome_header`)가 필요합니다.

**예시:**

{% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

HTML, 링크 내의 Liquid 및 기타 패턴은 [로케일 번역]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)과 동일한 규칙을 따르세요(예: 가능한 한 가장 작은 세그먼트를 태그로 감싸고, 링크를 현지화할 때는 언어별 URL 부분만 감싸기).

Crowdin이 콘텐츠를 감지하고 가져올 수 있도록 Braze 메시지를 **초안**으로 저장하세요.

### 5단계: Crowdin에서 번역 관리 {#step-5-manage-translations-in-crowdin}

통합 화면은 두 부분으로 구성됩니다:

- **Braze 패널:** Campaigns와 Canvases가 표시됩니다.
- **Crowdin 패널:** 번역을 위해 이미 동기화된 콘텐츠가 표시됩니다.

![Campaigns 및 로케일 폴더, Sync to Braze, Sync to Crowdin이 표시된 Crowdin 및 Braze Campaigns & Canvas 패널.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_sync_panels.png %})

#### 콘텐츠 동기화 {#syncing-content}

1. **Braze** 패널에서 번역할 Campaign 또는 Canvas의 체크박스를 선택합니다.
2. **Sync to Crowdin**을 선택합니다.
3. 동기화가 완료되면 **Crowdin** 패널에 파일이 나타납니다. 번역자가 Crowdin 에디터에서 문자열을 열 수 있습니다.

#### Braze로 번역 반환 {#returning-translations-to-braze}

1. Crowdin에서 번역이 100% 완료되면 **Integrations** 탭으로 돌아갑니다.
2. **Crowdin** 패널에서 완료된 콘텐츠를 선택합니다.
3. **Sync to Braze**를 선택합니다. 이렇게 하면 번역된 문자열이 Braze Campaign의 해당 언어 배리언트에 푸시됩니다.

### 6단계: Braze에서 다국어 사용자로 메시지 미리보기 {#step-6-preview-the-message-as-a-multi-language-user-in-braze}

통합을 확인하려면 다음을 수행합니다:

1. **Braze 메시지 작성기**에서 Campaign을 엽니다.
2. **테스트** 탭으로 이동합니다.
3. **사용자로 메시지 미리보기**를 선택합니다.
4. 번역된 로케일 중 하나와 일치하는 `language` 속성을 가진 고객 프로필을 검색합니다.
5. 콘텐츠가 원본 언어에서 번역된 버전으로 전환되는지 확인합니다.

## Braze 이메일 템플릿 통합 {#braze-email-templates-integration}

템플릿 수준에서 이메일을 현지화하는 경우, [Braze 이메일 템플릿 앱](https://store.crowdin.com/braze-app)을 사용하여 Braze 미디어 라이브러리에서 HTML을 동기화할 수 있습니다.

비디오 안내는 [Braze 이메일 템플릿 통합](https://youtu.be/g0YMKW3jEjk)을 참조하세요.

### 1단계: 앱 설치 {#step-1-install-the-app}

1. Crowdin 프로젝트에서 **Store** 탭으로 이동합니다.
2. **Braze Email Templates**를 검색하고 **Install**을 선택합니다.

![Braze 이메일 템플릿이 선택되고 Install이 강조 표시된 Crowdin Store.]({% image_buster /assets/img/crowdin/crowdin_store_email_templates.png %})

{: start="3"}
3. 이 통합을 사용할 프로젝트(또는 여러 프로젝트)를 선택합니다.
4. 통합을 열려면 프로젝트의 **Integrations** > **Braze Email Templates**로 이동합니다.

### 2단계: Braze에 연결 {#step-2-connect-to-braze}

Braze API 자격 증명으로 연결을 인증합니다:

![REST API 키, REST 엔드포인트, Braze 이메일 템플릿으로 로그인이 표시된 Crowdin Braze 이메일 템플릿 연결 양식.]({% image_buster /assets/img/crowdin/crowdin_email_templates_login.png %}){: style="max-width:85%;"}

1. **Braze REST API 키:** `templates.email` 및 `content_blocks`(읽기 및 쓰기) 권한을 부여합니다. Braze에서 **Settings** > **APIs and Identifiers** > **API Keys**로 이동하여 키를 생성합니다.

![Create API Key 버튼과 REST 엔드포인트 복사 컨트롤이 있는 Braze REST API Keys 페이지.]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %})

{: start="2"}
2. **Braze REST 엔드포인트**에는 인스턴스별 URL(예: `https://rest.iad-03.braze.com`)을 사용합니다.
3. **Log in with Braze Email Templates**를 선택합니다.

### 3단계: 번역할 콘텐츠 동기화 {#step-3-sync-content-for-translation}

통합 화면에 Braze 라이브러리가 표시됩니다:

- **Braze 패널:** 동기화할 수 있는 **이메일 템플릿** 및 **Content Blocks**.
- **Crowdin 패널:** 번역 중인 콘텐츠.

1. **Braze** 패널에서 현지화할 템플릿 또는 블록 옆의 체크박스를 선택합니다.
2. **Sync to Crowdin**을 선택합니다.
3. Crowdin이 HTML 소스를 가져옵니다. 번역자는 Crowdin 에디터에서 실시간 **WYSIWYG 미리보기**를 통해 레이아웃을 유지하면서 작업할 수 있습니다.

![현지화된 이메일 HTML과 번역 가능한 문자열이 표시된 Crowdin 에디터 미리보기 탭.]({% image_buster /assets/img/crowdin/crowdin_editor_wysiwyg_preview.png %}){: style="max-width:85%;"}

### 4단계: 번역된 템플릿 전달 {#step-4-deliver-translated-templates}

번역이 100% 완료되면:

1. **Crowdin** 패널에서 완료된 파일을 선택합니다.
2. **Sync to Braze**를 선택합니다.
3. Crowdin이 Braze 미디어 라이브러리에 이러한 에셋의 현지화된 버전을 자동으로 생성합니다(예: `Template_Name_fr`).

![이메일 템플릿과 Content Blocks가 나열된 Crowdin 및 Braze 이메일 템플릿 패널, Sync to Braze와 Sync to Crowdin 표시.]({% image_buster /assets/img/crowdin/crowdin_email_templates_sync_panels.png %})