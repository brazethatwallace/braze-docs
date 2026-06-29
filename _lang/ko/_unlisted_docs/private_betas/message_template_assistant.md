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

{% multi_lang_include brazeai/generative_ai/access_html_template.md %}

## 작동 방식 {#how-it-works}

Operator는 [브랜드 가이드라인]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/)과 [글로벌 스타일 설정]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings/)을 사용하여 메시지 콘텐츠와 스타일을 브랜드에 맞게 조정합니다.

예를 들어, 글로벌 스타일 설정이 구성되어 있으면 Operator가 브랜드의 색상과 스타일을 반영합니다. Braze에서 브랜드 가이드라인을 정의한 경우, Operator는 이를 참조하여 브랜드의 톤과 개성에 맞는 카피를 작성합니다.

Operator는 모바일 반응형에 맞게 템플릿을 반복 개선합니다.

## 예시 프롬프트 {#example-prompts}

{% include copy_block.html content="Build a responsive HTML email template for a product launch with a hero image and two feature blocks." %}

{% include copy_block.html content="Create a clean, single-column newsletter template that matches our brand guidelines." %}

{% include copy_block.html content="Add a feedback survey at the bottom of the email" %}

{% include copy_block.html content="Change font to [font name] and font size of the paragraph to size [number]" %}

{% include copy_block.html content="Make all the images have rounded corners" %}

{% include copy_block.html content="Add another section with an image and a call-to-action" %}