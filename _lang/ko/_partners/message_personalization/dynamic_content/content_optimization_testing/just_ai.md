---
nav_title: JustAI
article_title: JustAI
description: "이 참조 문서에서는 Braze와 JustAI 간의 파트너십에 대해 설명합니다. JustAI는 AI 기반 SaaS 비즈니스 플랫폼으로, 기존 Campaign의 개인화된 버전을 생성하고 시간이 지남에 따라 제목란, 크리에이티브 콘텐츠 및 HTML 이메일 레이아웃을 최적화합니다."
alias: ["/partners/just_ai/", "/partners/just_words/"]
page_type: partner
---

# JustAI 통합 가이드 {#justai-integration-guide}

> [JustAI](https://www.getjust.ai/)는 라이프사이클 마케팅 채널에서 대규모로 메시징을 초개인화하여, 수백 가지 변형을 동적으로 테스트하고 성과가 낮은 콘텐츠를 자동으로 갱신할 수 있도록 지원합니다.

JustAI를 Braze [연결된 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)와 함께 사용하여 기존 Braze Campaigns 및 Canvases를 개인화하면, JustAI가 Braze 커런츠를 활용하여 콘텐츠를 동적으로 최적화합니다. 직접 관리할 필요가 없습니다.

## 이점은 무엇인가요? {#what-are-the-benefits}

통합이 완료되면 JustAI 플랫폼을 활용하여 다음을 수행할 수 있습니다:

- 실시간 실험 결과 확인
- 동적으로 카피 편집
- 성과 인사이트 확인

{% alert note %}
질문이 있으신가요? JustAI의 [예약 페이지](https://www.getjust.ai/book-demo) 또는 공유 Slack 채널을 통해 문의하세요.
{% endalert %}

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| JustAI 계정 | 이 파트너십을 활용하려면 [JustAI](https://www.getjust.ai/) 계정이 필요합니다. JustAI 계정이 없는 경우 [30분 온보딩 통화를 예약](https://www.getjust.ai/book-demo)하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## JustAI와 Braze 통합하기 {#integrating-justai-with-braze}

### 1단계: JustAI 템플릿 생성 {#step-1-create-a-justai-template}

1. JustAI 콘솔로 이동하여 [새 템플릿을 생성](https://console.getjust.ai/new)합니다.
2. 문자, 숫자, 밑줄만 사용하여 기억하기 쉬운 ID를 선택합니다.
3. 기본 Campaign 세부 정보를 입력합니다.
4. AI를 사용하여 개인화된 변형을 생성합니다.

![JustAI 템플릿 생성 플랫폼.]({% image_buster /assets/img/just_words/creation_interface.png %}){: style="max-width:80%;"}

### 2단계: JustAI API 키 생성 {#step-2-create-a-justai-api-key}

1. **Org Settings** > **API Keys** > **Generate API Key**로 이동합니다.
2. API 키를 복사하여 안전한 위치에 저장합니다.

![JustAI API 키 양식.]({% image_buster /assets/img/just_words/api_key_form.png %}){: style="max-width:80%;"}

### 3단계: Braze 콘텐츠에서 JustAI 사용 {#step-3-use-justai-in-your-braze-content}

JustAI는 연결된 콘텐츠를 사용하여 Canvases 및 Campaigns와 함께 작동합니다. Canvas를 생성하는 경우, 각 이메일 단계는 고유한 JustAI 템플릿에 대응해야 합니다.

#### 3.1단계: A/B 테스트 설정 {#step-31-set-up-your-ab-test}

{% tabs %}
{% tab Canvas %}

1. Canvas에서 **배리언트 추가** > **배리언트 추가**를 선택하여 원하는 수의 배리언트를 만들고, 각 배리언트에 단계(예: 이메일 메시지 단계)를 추가합니다.
2. 원하는 대로 오디언스 트래픽을 분할합니다. 예를 들어, 두 개의 배리언트가 있는 경우 각각 50%를 할당할 수 있습니다. 또는 두 개의 배리언트에 각각 40%, 대조군에 20%를 할당할 수도 있습니다. Canvas A/B 테스트에 대한 자세한 내용은 [Canvas 생성하기]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)를 참조하세요.
3. 연결된 콘텐츠와 함께 사용하려는 메시지 단계의 작성기에서, JustAI 콘솔의 연결된 콘텐츠 스니펫을 붙여넣습니다. 다음은 스니펫 예시입니다.

{% raw %}
```liquid
{% connected_content https://worker.getjust.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

![Braze A/B 테스트 Canvas 설정.]({% image_buster /assets/img/just_words/braze_canvas.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Campaign %}

1. Campaign의 **메시지 작성** 단계에서 두 개의 배리언트를 생성합니다.
2. **타겟 오디언스** 단계에서 **A/B Testing** 섹션으로 이동하여 각 배리언트(및 선택적 대조군)를 수신할 사용자 비율을 수정합니다. 최적화 옵션을 선택하여 테스트를 추가로 커스터마이즈할 수 있습니다. Campaign A/B 테스트에 대한 자세한 내용은 [다변량 및 A/B 테스트 생성하기]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/)를 참조하세요.
3. 메시지 작성기에서 JustAI 콘솔의 연결된 콘텐츠 스니펫을 붙여넣습니다. 다음 Liquid 스니펫은 이에 대한 예시입니다.

{% raw %}
```liquid
{% connected_content https://worker.getjust.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

{% endtab %}
{% endtabs %}

#### 3.2단계: 커스텀 속성으로 개인화 추가(선택 사항) {#step-32-add-personalization-with-custom-attributes-optional}

커스텀 속성(예: `industry`)으로 메시지를 개인화하려면 다음 Liquid 형식을 사용합니다:

{% raw %}
```liquid
{% connected_content https://worker.getjust.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}&attrs.industry={{ custom_attribute.industry }}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

`industry` 커스텀 속성은 {% raw %}`&attrs.industry={{ custom_attribute.industry }}`{% endraw %}로 표시됩니다.

![HTML 메시지 작성기에서의 Braze Liquid 로직.]({% image_buster /assets/img/just_words/just_words_personalization.png %}){: style="max-width:80%;"}

### 4단계: 이메일 미리보기 {#step-4-preview-the-email}

Braze에서 이메일을 미리보기하여 개인화된 콘텐츠가 올바르게 렌더링되는지 확인하세요.

![JustAI 이메일에 대한 Braze 메시지 미리보기.]({% image_buster /assets/img/just_words/just_words_preview.png %}){: style="max-width:80%;"}

### 5단계: Braze 커런츠 설정 {#step-5-set-up-braze-currents}

Braze 커런츠를 사용하면 시간이 지남에 따라 성과 추적 및 최적화가 가능합니다.

1. Braze에서 **파트너 통합** > **데이터 내보내기**로 이동합니다.
2. **Create New Test Current**를 선택한 다음 **Test Amazon S3 Data Export**를 선택합니다.

!["Create New Test Current" 드롭다운에 "Test Amazon S3 Data Export" 옵션이 표시됨.]({% image_buster /assets/img/just_words/test_amazon_s3.png %}){: style="max-width:80%;"}

{: start="3" }
3. 온보딩 시 JustAI에서 제공한 S3 Access ID, AWS Secret Access Key, 버킷 이름 및 폴더를 입력합니다.

![AWS 비밀 액세스 키에 대한 "자격 증명" 섹션.]({% image_buster /assets/img/just_words/aws_secret_access_key.png %}){: style="max-width:80%;"}

{: start="4" }
4. 발송, 오픈, 클릭, 탈퇴, 전환 등 추적할 이벤트를 선택합니다.

![선택할 이벤트가 있는 "메시지 참여 이벤트" 섹션.]({% image_buster /assets/img/just_words/message_engagement_events.png %}){: style="max-width:80%;"}

{: start="5" }
5. Braze 커런츠를 시작합니다.

모든 설정이 완료되었습니다! 이제 Braze 연결된 콘텐츠와 함께 JustAI를 사용할 수 있습니다.