---
nav_title: 이메일
article_title: 이메일
page_order: 3
page_type: landing
description: "Braze에서 드래그 앤 드롭 및 HTML 편집기, 구독 관리 등을 활용하여 맞춤화되고 개인화된 이메일 Campaign을 만들어 보세요."
channel:
  - email
search_rank: 2
---

# 이메일 {#email}

> Braze의 이메일을 사용하면 Campaigns 또는 Canvases에서 맞춤화되고 개인화된 이메일 메시지를 만들어 앱이나 웹사이트 외부의 사용자에게 도달할 수 있습니다. 이 허브에서는 이메일 설정, 드래그 앤 드롭 및 HTML 편집기, 구독 관리, 템플릿, 테스트 등을 다루므로 규정을 준수하면서 브랜드에 맞는 이메일 프로그램을 시작할 수 있습니다. Braze 이메일 템플릿이나 커스텀 HTML을 사용하여 브랜드 톤과 레이아웃에 맞게 이메일을 구성하세요. 새 발송 도메인을 설정하는 경우 [이메일 설정]({{site.baseurl}}/user_guide/channels/email/email_setup)부터 시작하세요. 이메일 Campaign 예시는 Braze [사례 연구](https://www.braze.com/customers/)를 참조하세요.

## 사전 준비 사항 {#prerequisites}

Braze로 이메일을 발송하려면 먼저 전용 IP, 도메인, 이메일 인증, IP 워밍을 구성해야 합니다. 전체 설정 과정은 [이메일 설정]({{site.baseurl}}/user_guide/channels/email/email_setup)을 참조하세요.

## 이메일 커스텀하기 {#customize-your-emails}

다양한 방법으로 이메일 메시징을 커스텀할 수 있습니다:

- [Braze 이메일 템플릿]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template)
- [커스텀 HTML 템플릿]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template)
- [편집기 블록(이메일)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email)
- [사용자 구독]({{site.baseurl}}/user_guide/channels/email/subscriptions)
- [구독 그룹]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups)

## 이메일 테스트 {#test-your-emails}

[시드 그룹]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups)은 품질 보증을 위해 이메일 Campaign의 사본을 내부 사용자에게 자동으로 발송합니다. 시드 이메일은 제목란 앞에 `[SEED]`가 추가되어 쉽게 식별할 수 있습니다.

## 사용 사례 {#use-cases}

| 사용 사례 | 설명 |
| --- | --- |
| 재참여 | 앱을 설치하지 않은 사용자를 포함하여, 앱 외부에서 사용자에게 도달할 수 있습니다. |
| 온보딩 | 신규 사용자의 온보딩을 지원하고 푸시 알림 활성화나 소셜 네트워크에서의 앱 공유를 유도합니다. |
| 리치 메시지 | 풍부하고 동적인 HTML 메시지를 전달할 수 있습니다. |
| 멀티미디어 콘텐츠 | 비디오, 이미지 등 사용자의 참여를 유도하는 멀티미디어 콘텐츠를 손쉽게 배치할 수 있습니다. |
| 뉴스레터 | 월간 또는 주간 뉴스레터를 편리하게 발송하여 사용자 인게이지먼트를 유지할 수 있습니다. |
| 트랜잭션 | 최근 구매에 대해 사용자에게 알리고, [트랜잭션 이메일]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email)을 통해 중요한 제품 및 배송 정보를 전달합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사용 사례" }

## 이메일 서비스 {#email-services}

이메일 프로그램에 대한 추가 지원이 필요한 경우, Braze는 추가 비용으로 정기 및 일회성 서비스를 제공합니다. 자세한 내용은 Braze 계정 매니저에게 문의하세요.

### 이메일 전달 가능성 서비스 {#email-deliverability-services}

Braze는 두 가지 등급의 정기 이메일 지원을 제공합니다:
1. 디럭스
2. 스탠다드

이러한 서비스에는 다음이 포함될 수 있습니다:

- 타겟팅, 발송 주기 및 메시징 전략에 대한 검토를 포함한 과거 및 현재 이메일 발송 관행 감사
- 이메일 전달 가능성 전문가가 작성한 허용 목록 구성 및 맞춤형 IP 워밍 계획
  - 첫 달 동안 정기 체크인 통화(디럭스는 주 3회, 스탠다드는 주 1회)
- 전달 가능성 전문가와의 정기 통화(디럭스는 월 2회, 스탠다드는 월 1회)를 통해 다음을 제공합니다:
  - 도메인별 전달 가능성 성능 모니터링
  - 데이터 및 확립된 모범 사례를 활용하여 이메일 프로그램 성능 및 결과 개선을 위한 권장 사항
- 차단 목록 등록과 같은 전달 가능성 문제를 초래하는 이벤트에 대한 위기 대응 완화 및 해결

## 자주 묻는 질문 {#frequently-asked-questions}

### Braze에서 이메일 발송을 어떻게 설정하나요? {#how-do-i-set-up-email-sending-in-braze}

첫 번째 발송 전에 전용 IP, 도메인, 인증, IP 워밍을 구성해야 합니다. 전체 체크리스트는 [이메일 설정]({{site.baseurl}}/user_guide/channels/email/email_setup)을 참조하세요.

### 사용자 구독과 구독 그룹의 차이점은 무엇인가요? {#what-is-the-difference-between-user-subscriptions-and-subscription-groups}

사용자 구독은 채널에 대한 글로벌 옵트인 상태를 제어합니다(예: 이메일 구독 또는 탈퇴). 구독 그룹은 사용자가 해당 채널 내에서 특정 메시지 카테고리를 선택할 수 있도록 해줍니다. 자세한 내용은 [사용자 구독]({{site.baseurl}}/user_guide/channels/email/subscriptions) 및 [구독 그룹]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups)을 참조하세요.

### Campaign을 발송하기 전에 이메일을 어떻게 테스트할 수 있나요? {#how-can-i-test-an-email-before-i-send-a-campaign}

[시드 그룹]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups)을 사용하여 내부 검토자에게 미리보기 사본을 발송하고 다양한 클라이언트에서 렌더링을 확인하세요.

## 다음 단계 {#next-steps}

{% article_tiles %}
- name: 이메일 설정
  link: /docs/user_guide/channels/email/email_setup
- name: 드래그 앤 드롭 편집기로 이메일 만들기
  link: /docs/user_guide/channels/email/drag_and_drop
- name: HTML 편집기로 이메일 만들기
  link: /docs/user_guide/channels/email/html_editor
{% endarticle_tiles %}