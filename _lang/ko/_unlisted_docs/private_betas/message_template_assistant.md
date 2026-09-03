---
nav_title: HTML 이메일 템플릿
article_title: HTML 이메일 템플릿 생성
permalink: "/template_assistant/"
description: "이 참조 문서에서는 Operator를 사용하여 HTML 이메일 템플릿을 생성하는 방법, 작동 방식 및 예시 프롬프트를 다룹니다."
page_type: reference
---

# HTML 이메일 템플릿 생성 {#generate-html-email-templates}

> Operator를 사용하여 HTML 이메일 템플릿을 생성하고 반복 개선할 수 있습니다. 필요한 템플릿을 자연어로 설명하면, Operator가 브랜드 가이드라인과 글로벌 스타일 설정을 활용하여 템플릿을 구축하거나 수정합니다.

{% alert important %}
Operator를 사용한 HTML 이메일 템플릿 생성은 얼리 액세스 단계입니다. 이 얼리 액세스에 참여하려면 Braze 계정 매니저에게 문의하세요.

이 기능은 HTML 편집기의 이메일 채널에서만 지원되며, 드래그 앤 드롭이나 AMP 등 다른 편집기에서는 지원되지 않습니다.
{% endalert %}

{% multi_lang_include brazeai/generative_ai/unification_note.md %}

## 접근 방법 {#how-to-access}

HTML 이메일 템플릿 편집기에서 **Generate** 사이드바 그룹에 **Template** 옵션이 포함되어 있습니다. 이 옵션을 선택하면 브랜드에 맞는 HTML 이메일 템플릿을 생성하거나 반복 작업할 수 있습니다. Operator는 [브랜드 가이드라인]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines)을 적용하여 결과물이 브랜드의 보이스와 스타일에 맞도록 합니다.

## 작동 방식 {#how-it-works}

Operator는 [브랜드 가이드라인]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines)과 [글로벌 스타일 설정]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings)을 사용하여 메시지 콘텐츠와 스타일을 브랜드에 맞게 조정합니다.

예를 들어, 글로벌 스타일 설정이 구성되어 있으면 Operator가 브랜드의 색상과 스타일을 반영합니다. Braze에 브랜드 가이드라인이 정의되어 있는 경우, Operator는 이를 참조하여 브랜드의 톤과 개성에 맞는 카피를 작성합니다.

또한 Operator는 모바일 응답형에 맞게 템플릿을 반복적으로 개선합니다.

## 예시 프롬프트 {#example-prompts}

{% include copy_block.html content="히어로 이미지와 두 개의 기능 블록이 포함된 제품 출시용 응답형 HTML 이메일 템플릿을 만들어 주세요." %}

{% include copy_block.html content="브랜드 가이드라인에 맞는 깔끔한 단일 열 뉴스레터 템플릿을 만들어 주세요." %}

{% include copy_block.html content="이메일 하단에 피드백 설문조사를 추가해 주세요" %}

{% include copy_block.html content="폰트를 [폰트명]으로 변경하고 단락의 폰트 크기를 [숫자]로 변경해 주세요" %}

{% include copy_block.html content="모든 이미지에 둥근 모서리를 적용해 주세요" %}

{% include copy_block.html content="이미지와 콜 투 액션이 포함된 섹션을 하나 더 추가해 주세요" %}