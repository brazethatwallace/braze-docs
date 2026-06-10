---
nav_title: Worthy
article_title: Worthy
description: "이 참조 문서에서는 개인화된 풍부한 인앱 경험을 만들고 Braze를 통해 전달할 수 있는 메시지 개인화 플랫폼인 Worthy와 Braze 간의 파트너십에 대해 설명합니다."
alias: /partners/worthy/
page_type: partner
search_tag: Partner

---

# Worthy

> [Worthy](https://worthy.ai/)와 Braze의 통합을 통해 Worthy의 드래그 앤 드롭 편집기를 사용하여 개인화된 풍부한 인앱 경험을 만들고 Braze를 통해 전달할 수 있습니다. 또한 Worthy는 자동으로 다음을 수행합니다.

_이 통합은 Worthy에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

- 메시징을 위한 연결된 콘텐츠 서버와 보안 API를 생성합니다.
- 분석 및 클릭 추적이 포함된 인앱 메시지를 구성하며, 이는 Braze에 직접 표시됩니다.
- Worthy의 드래그 앤 드롭 편집기를 통해 HTML을 자동으로 내보내어 Braze의 **Custom Code** 인앱 메시지 Campaign에서 사용할 수 있으며, 필요한 API 연결과 구성한 동적 콘텐츠가 포함됩니다.

## 활용 사례 {#use-cases}

- 사용자 온보딩 선택에 기반한 커스텀 환영 경험
- 특별 이벤트 및 프로모션을 위한 인앱 경험
- 앱 동작에 기반한 고객 피드백 및 평점 수집
- 잠재적인 앱 제품 아이디어의 빠른 테스트
- 풍부한 공지사항, 뉴스 및 커뮤니티 업데이트

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| [Worthy](https://worthy.ai/) 계정 | 이 파트너십을 활용하려면 Worthy 계정이 필요합니다. |
| Braze SDK | 풍부한 인앱 메시지를 전송하려면 모바일 애플리케이션에 Braze SDK를 구성해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

### 1단계: Worthy에서 개인화된 메시지 만들기 {#step-1-create-personalized-messaging-in-worthy}

Worthy 대시보드에서 앱으로 이동하여 **Message Creator**를 선택하고, 사용자 참여에 사용할 개인화된 메시지를 만드세요.

### 2단계: Braze Campaign 만들기 {#step-2-create-a-braze-campaign}

Braze에서 [인앱 메시지 Campaign]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/)을 만들고 **메시지 유형**을 **Custom Code**로 설정하세요.

### 3단계: 개인화된 메시지를 Braze에 복사하기 {#step-3-copy-your-personalized-message-into-braze}

Worthy 메시지 크리에이터에서 **내보내기**를 클릭하고 **Braze**를 선택하여 Braze Campaign에서 사용할 개인화된 메시지를 내보내세요. 내보낸 콘텐츠를 Braze Campaign 편집기의 **HTML + Asset Zip** 아래 HTML 텍스트 상자에 붙여넣으세요.

이것으로 완료입니다! Braze Campaign 편집기의 **Test** 탭을 사용하여 개인화된 메시지를 즉시 테스트할 수 있습니다.