---
nav_title: 웹훅 템플릿
article_title: 웹훅 템플릿
page_order: 5
tool:
  - Templates
channel:
  - webhooks
description: "Braze 플랫폼에서 나중에 사용할 웹훅 템플릿을 생성하고 커스터마이즈하는 방법을 알아보세요."

---

# 웹훅 템플릿 생성 {#create-a-webhook-template}

> 웹훅을 구축하고 커스터마이즈하면서, 나중에 Braze 플랫폼에서 사용할 웹훅 템플릿을 생성하고 활용할 수 있습니다. 이를 통해 다양한 Campaign에서 일관되게 여러 웹훅을 구축할 수 있습니다.

## 1단계: 웹훅 템플릿 편집기로 이동 {#step-1-go-to-the-webhook-template-editor}

Braze 대시보드에서 **콘텐츠** > **웹훅**으로 이동합니다.

![미리 디자인된 웹훅 템플릿과 저장된 웹훅 템플릿이 있는 '웹훅 템플릿' 페이지.]({% image_buster /assets/img_archive/webhook_template_campaign.png %})

## 2단계: 템플릿 선택 {#step-2-choose-your-template}

여기에서 새 템플릿을 생성하거나, 미리 디자인된 웹훅 템플릿 중 하나를 사용하거나, 기존 템플릿을 편집할 수 있습니다.

예를 들어, [LINE]({{site.baseurl}}/user_guide/channels/line/)을 메시징 채널로 사용하는 경우, **LINE Carousel** 또는 **LINE Image**의 미리 디자인된 템플릿을 사용하여 여러 웹훅을 설정할 수 있습니다.

## 3단계: 템플릿 세부 정보 입력 {#step-3-fill-out-template-details}

1. 웹훅 템플릿에 고유한 이름을 지정합니다.
2. (선택 사항) 이 템플릿의 사용 목적을 설명하는 템플릿 설명을 추가합니다.
3. 필요에 따라 [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) 및 [태그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/)를 추가하여 템플릿을 쉽게 찾고 필터링할 수 있도록 합니다.

## 4단계: 템플릿 구축 {#step-4-build-your-template}

1. 웹훅 URL을 입력합니다.
2. HTTP 메서드를 선택합니다.
3. 요청 본문을 추가합니다. **JSON 키/값 쌍** 또는 **원시 텍스트**를 사용할 수 있습니다.
4. (선택 사항) 요청 헤더를 추가합니다. 웹훅 대상에 따라 필요할 수 있습니다.

![웹훅 템플릿 생성 시 '작성' 탭. 사용 가능한 필드는 웹훅 URL, HTTP 메서드, 요청 본문, 요청 헤더입니다. 언어를 추가할 수도 있습니다.]({% image_buster /assets/img_archive/Webhook_template_test.png %}){: style="max-width:90%"}

## 5단계: 템플릿 테스트 {#step-5-test-your-template}

사용자에게 발송하기 전에 웹훅이 어떻게 보이는지 확인하려면 **테스트** 탭을 사용하여 테스트 웹훅을 발송할 수 있습니다. 여기에서 랜덤 사용자, 기존 사용자 또는 커스텀 사용자로 메시지를 미리보기할 수 있습니다.

## 6단계: 템플릿 저장 {#step-6-save-your-template}

**템플릿 저장**을 선택하여 템플릿을 저장하세요. 이제 원하는 Campaign에서 이 템플릿을 사용할 준비가 되었습니다.

{% alert note %}
기존 템플릿에 대한 수정 사항은 해당 템플릿의 이전 버전을 사용하여 생성된 Campaign에는 반영되지 않습니다.
{% endalert %}

## 템플릿 관리 {#managing-your-templates}

웹훅 템플릿을 [복제 및 아카이브]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/)하여 템플릿 목록을 더 효과적으로 정리하고 관리할 수 있습니다.