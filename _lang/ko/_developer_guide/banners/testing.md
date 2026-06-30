---
nav_title: 테스트 배너
article_title: 테스트 배너
page_order: 2
description: "Campaign을 시작하기 전에 배너 메시지를 테스트하여 모든 미디어, 문구, 개인화 및 커스텀 속성이 올바르게 렌더링되는지 확인하는 방법을 알아보세요."
channel:
  - banners
noindex: true
---

# 테스트 배너 {#test-banners}

> Campaign을 시작하기 전에 배너 메시지를 테스트하여 모든 미디어, 문구, 개인화 및 커스텀 속성이 올바르게 렌더링되는지 확인하는 방법을 알아보세요. 더 자세한 일반 정보는 [배너 소개]({{site.baseurl}}/developer_guide/banners)를 참조하세요.

## 필수 조건 {#prerequisites}

Braze에서 배너 메시지를 테스트하려면 먼저 [Braze에서 배너 Campaign]({{site.baseurl}}/user_guide/channels/banners/create_a_banner)을 생성해야 합니다. 또한 테스트하려는 배치가 이미 [앱 또는 웹사이트에 배치되어 있는지]({{site.baseurl}}/developer_guide/banners/placements) 확인하세요.

[콘텐츠 테스트 그룹]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups) 또는 개별 사용자에게 테스트를 보내려면, 발송 전에 테스트 기기에서 푸시가 활성화되어 있고 테스트 사용자에 대해 유효한 푸시 토큰이 등록되어 있어야 합니다.

## 배너 테스트 {#test-a-banner}

{% multi_lang_include banners/testing.md page="testing" %}