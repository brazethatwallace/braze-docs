---
nav_title: DailyPlay
article_title: DailyPlay
description: "DailyPlay 브랜드 게임과 리워드를 Braze에 연결하여 게임플레이 데이터를 동기화하고, 오디언스를 세분화하며, 개인화된 Campaign을 트리거하는 방법을 알아보세요."
alias: /partners/dailyplay/
page_type: partner
search_tag: Partner
---

# DailyPlay

> [DailyPlay](https://dailyplay.ai/)는 게임화 플랫폼입니다. 이를 사용하여 인게이지먼트를 심화하고 유지율을 개선하는 개인화된 브랜드 게임과 내장 리워드 시스템을 출시할 수 있습니다.

*이 통합은 DailyPlay에서 유지 관리합니다.*

## 이 통합에 대하여 {#about-this-integration}

Braze와 DailyPlay의 통합을 통해 오디언스 Segments 전반에서 게임과 리워드 성능을 배포하고 추적할 수 있습니다. DailyPlay의 게임 및 리워드 시스템은 Braze의 오케스트레이션 엔진과 연동되어 수동적인 오디언스를 능동적인 참여자로 전환할 수 있습니다.

게임플레이 마일스톤, 리워드 사용 내역, 인게이지먼트 측정기준을 Braze로 전송하여 오디언스 Segments를 구축하고 인게임 행동에 기반한 자동화된 크로스채널 메시징을 트리거할 수 있습니다. 이 통합을 통해 다음을 수행할 수 있습니다:

- **고객 프로필 강화:** 게임플레이 측정기준, 점수, 리워드 상태를 Braze의 고객 프로필로 전달합니다.
- **고급 세분화 활용:** 최고 득점자, 최근 우승자, 리워드 잠금 해제에 가까운 사용자 등 인게임 행동에 기반한 오디언스 Segments를 생성합니다.
- **실시간 Campaign 자동화:** 게임 인터랙션에 기반한 개인화된 크로스채널 메시지(푸시, 이메일, 인앱)를 트리거하여 반복 플레이, 브랜드 로열티, 더 높은 생애주기 가치를 이끌어냅니다.

## 사용 사례 {#use-cases}

- **비활성 고객 재참여:** 비활성 고객을 대상으로 할인 리워드를 받을 수 있는 게임 링크를 전송하세요.
- **제품 및 트렌드 관련 활동:** 신제품, 시즌, 트렌드 또는 이벤트를 소개하는 개인화된 게임을 만들어 보세요.
- **타겟팅된 게임 배포:** Braze 세분화 및 타겟팅과 DailyPlay 개인화를 결합하여 다양한 목표와 성과에 맞는 참여도 높은 게임 콘텐츠를 만들어 보세요.
- **온보딩 및 활성화:** Braze 웰컴 시리즈에 DailyPlay 스크래치 앤 윈 또는 즉시 공개 게임 링크를 삽입하여 첫 구매나 프로필 완성을 유도하세요.
- **유지 및 로열티:** 소비자가 로열티 마일스톤에 도달하거나 Braze에서 추적하는 주요 액션을 수행하면 해당 성과를 축하하고 등급별 리워드를 제공하는 개인화된 DailyPlay 게임을 트리거하세요.
- **고객이탈 방지 및 윈백:** Braze에서 이탈 조짐을 보이는 사용자를 식별한 후 부담 없는 DailyPlay 게임을 전달하여 관심을 다시 끌고 앱이나 사이트로 복귀하도록 유도하세요.

## 전제 조건 {#prerequisites}


| 요구 사항 | 설명 |
| --- | --- |
| DailyPlay 계정 | 이 통합을 사용하려면 DailyPlay 계정이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키가 필요합니다. **설정** > **API 및 식별자** > **API 키**에서 이 키를 생성할 수 있습니다. 자세한 내용은 [API 키]({{site.baseurl}}/api/api_key)를 참조하세요. |
| Braze REST 엔드포인트 | [Braze 인스턴스]({{site.baseurl}}/api/basics#endpoints)의 REST 엔드포인트 URL입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="전제 조건" }

## 통합 {#integration}

### 1단계: 연결 만들기 {#step-1-create-a-connection}

1. [DailyPlay 대시보드](https://app.dailyplay.ai/connections)에서 **Connections** 페이지로 이동하여 **Add Connection**을 선택합니다.

![활성화된 Braze 연결 및 트리거 통계가 나열된 DailyPlay Connections 페이지.]({% image_buster /assets/img/dailyplay/connections_page.png %}){: style="max-width:70%;"}

{: start="2"}
2. **Provider**에서 **Braze**를 선택합니다. 이름, Braze REST API 키, 앱 ID, REST 엔드포인트를 입력한 후 **Create Connection**을 선택합니다.

![Braze가 선택되고 API 키, 앱 ID, REST 엔드포인트에 대한 자격 증명 필드가 표시된 DailyPlay Add Connection 모달.]({% image_buster /assets/img/dailyplay/add_connection.png %}){: style="max-width:60%;"}

### 2단계: 스트림 만들기 {#step-2-create-a-stream}

**Streams** 페이지로 이동하여 새 스트림을 만듭니다.

1. 1단계에서 만든 Braze 연결을 새 스트림에 추가합니다.
2. **Stream Access**, **Play Start**, **Play Complete**, **Prize Redemption** 등 추적할 트리거 이벤트를 구성합니다.
3. 게임을 만들어 스트림에 추가합니다.
4. 해당 스트림의 Braze 통합 코드를 복사합니다.

![Braze 트리거 이벤트와 Braze 이메일 템플릿용 임베드 코드가 표시된 DailyPlay Manage Connections 모달.]({% image_buster /assets/img/dailyplay/manage_connections.png %}){: style="max-width:70%;"}

### 3단계: Braze에서 Campaign 만들기 {#step-3-create-a-campaign-in-braze}

2단계에서 복사한 코드를 Braze의 Campaign에 붙여넣습니다.

사용자가 스트림에서 게임을 플레이하면 DailyPlay가 이벤트를 트리거하고 Braze REST 엔드포인트를 통해 Braze로 전송합니다.

### 4단계: 액션 확인 및 퍼널 확장 {#step-4-inspect-actions-and-expand-your-funnel}

DailyPlay 스트림에서 액션을 완료한 사용자는 Braze 프로필에 커스텀 속성과 커스텀 이벤트를 수신합니다.

사용 사례에 필요한 DailyPlay 커스텀 이벤트 또는 커스텀 속성을 사용하는 [액션 기반]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) 트리거로 [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) 또는 [Canvas]({{site.baseurl}}/user_guide/messaging/canvas)를 만드세요.

## Braze에서 DailyPlay 사용하기 {#use-dailyplay-with-braze}

특정 고객 Segment에 참여하려면, 통합 설정을 완료한 후 다음 단계를 따르세요.

### 1단계: DailyPlay 구성 설정하기 {#step-1-set-up-your-dailyplay-configuration}

이 섹션의 통합 단계에 따라 Braze 연결 및 DailyPlay 스트림을 설정하세요. 통합 코드를 복사합니다.

### 2단계: Braze Campaign 또는 Canvas 만들기 {#step-2-create-a-braze-campaign-or-canvas}

액션 기반 트리거를 사용하여 Campaign 또는 Canvas를 만드세요. 사용 사례에 필요한 DailyPlay 커스텀 이벤트 또는 커스텀 속성을 선택합니다.

[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)을 사용하여 DailyPlay가 메시지 본문에 전송하는 속성을 참조할 수 있습니다.

**커스텀 속성 예시:**

{% raw %}
```liquid
Your score was {{custom_attribute.${dailyplay}.last_game_score}}
```
{% endraw %}

**커스텀 이벤트 예시:**

점 표기법을 사용하여 트리거 이벤트의 속성을 참조합니다:

{% raw %}
```liquid
{{event_properties.${dailyplay_play_complete}.properties.score}}
```
{% endraw %}

## 문제 해결 {#troubleshooting}

추가 설정 안내 및 FAQ는 [DailyPlay Braze 통합 설명서](https://docs.dailyplay.ai/connections/braze/)를 참조하세요.