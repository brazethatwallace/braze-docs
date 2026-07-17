---
nav_title: 이탈 사용자
article_title: 이탈 사용자
page_order: 4
page_type: reference
description: "이 문서에서는 Braze Canvas 템플릿을 사용하여 과거 참여 내역을 기반으로 인센티브를 제공하여 사용자를 앱으로 다시 불러오는 방법을 설명합니다."
tool: Canvas
---

# 이탈 사용자 {#lapsed-user}

> 이탈 사용자 템플릿을 사용하여 브랜드가 제공하는 가치를 사용자에게 상기시키고, 과거 참여 내역을 기반으로 한 매력적인 혜택과 인센티브로 복귀를 유도하세요.

이 문서에서는 사용자 라이프사이클의 유지 및 로열티 단계를 위해 설계된 **이탈 사용자** 템플릿의 사용 사례를 안내합니다. 이 과정을 마치면, 프로모션 메시지를 받은 후 앱에서 세션을 시작했는지 여부 등 사용자의 행동에 따라 다양한 프로모션으로 앱 복귀를 유도하는 Canvas를 만들 수 있습니다.

## 필수 조건 {#prerequisites}

이탈 사용자 템플릿을 성공적으로 사용하려면 사용하는 파트너 및 오디언스와 함께 [Braze 오디언스 싱크]({{site.baseurl}}/partners/canvas_audience_sync)를 구성해야 합니다.

## 필요에 맞게 템플릿 조정하기 {#tailoring-the-template-to-your-needs}

영화와 시리즈의 독점 콘텐츠를 제공하는 스트리밍 서비스인 MovieCanon에서 일하고 있다고 가정해 보겠습니다. 이탈 사용자 템플릿을 사용하여 30일 동안 앱을 방문하지 않은 사용자에게 혜택과 프리미엄 콘텐츠를 홍보할 수 있습니다.

Canvas를 만들기 전에 [Braze 오디언스 싱크 to Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync) 통합을 설정하여 Braze의 사용자 데이터를 Google 오디언스에 추가하고 행동 트리거, 세분화 등을 기반으로 광고를 보낼 수 있도록 합니다.

이탈 사용자 템플릿에 접근하려면 새 Canvas를 만들 때 **Use a Canvas template** > **Braze templates**를 선택합니다. 그런 다음 **Lapsing User** 옆에 있는 **Apply Template**을 선택합니다. 이제 템플릿을 필요에 맞게 조정할 수 있습니다.

### 1단계: 세부 정보 설정 {#step-1-set-up-the-details}

Canvas 세부 정보를 목표에 맞게 조정합니다.

1. 템플릿 이름 옆의 **Edit**을 선택합니다.

{:start="2"}
2. Canvas 이름을 업데이트하여 이 Canvas가 프로모션 메시지를 보내고 세션을 시작한 사용자에 대해 오디언스 싱크를 수행한다는 것을 명시합니다.
3. 설명을 업데이트하여 이 Canvas에 혜택과 프로모션이 포함되어 있음을 설명합니다.
4. **Lapsing/Retention** 태그를 추가하여 Canvas 홈 페이지에서 이 Canvas를 필터링할 수 있도록 합니다.

### 2단계: 전환 이벤트 할당 {#step-2-assign-your-conversion-events}

**Primary Conversion Event - A**를 앱(MovieCanon)의 사용자를 타겟팅하도록 업데이트하고, **Primary Conversion Event - B**는 구매 완료 기본값으로 유지합니다.

### 3단계: 진입 스케줄 조정 {#step-3-tailor-the-entry-schedule}

진입 스케줄을 **Scheduled**로 유지하고 기본 시간 기반 옵션을 그대로 두어 Canvas가 매일 이탈 사용자를 확인하도록 합니다.

이 단계에서 두 가지를 조정합니다:

1. 시작 날짜와 시간을 선택합니다.
2. **On a specific date** 종료 파라미터를 선택하고 2개월 후 날짜를 설정합니다. 이 예시에서는 이 Canvas가 끝난 후 시작되는 다른 이탈 사용자 Canvas가 있습니다.

### 4단계: 타겟 오디언스 선택 {#step-4-select-your-target-audience}

진입 오디언스의 기본 설정을 유지합니다. 이 설정은 30일 이상 앱을 사용하지 않은 사용자를 대상으로 합니다. 또한 사용자가 4주 후에 Canvas에 다시 진입할 수 있도록 기본 진입 제어도 유지합니다. 즉, 사용자가 30일 연속으로 앱을 방문하지 않을 때마다 Canvas에 진입하게 됩니다.

### 5단계: 발송 설정 선택 {#step-5-select-your-send-settings}

대부분의 기본 구독 설정을 유지합니다:

- 메시지 또는 알림 수신에 가입했거나 옵트인한 사용자에게만 발송합니다.
- [최대 게재빈도 설정 규칙]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping)을 적용하여 오디언스가 받는 메시지 수가 과도하지 않도록 합니다. 이 경우 "Lapsing/Retention" 태그가 지정된 Campaign 또는 캔버스 단계를 사용자가 매주 2개까지만 받을 수 있도록 최대 게재빈도를 설정합니다.
- 사용자의 현지 시간 기준 방해금지 시간(오전 12시~오전 8시) 동안에는 메시지를 보내지 않습니다.

변경할 유일한 설정은 방해금지 시간 동안 메시지가 트리거될 때의 처리 방식입니다. 메시지를 취소하는 대신 **Send at next available time**을 선택하여 사용자가 프로모션을 놓치지 않도록 합니다.

### 6단계: Canvas 커스터마이즈 {#step-6-customize-your-canvas}

이제 템플릿 단계를 커스터마이즈하여 Canvas를 구축합니다:

1. 30일 이상 앱을 방문하지 않은 모든 사용자에게 발송할 첫 번째 이메일을 커스터마이즈합니다. 이 사용 사례에서는 오늘 앱을 방문하면 새로운 혜택을 잠금 해제할 수 있다고 알려주는 이메일을 커스터마이즈합니다.

{: start="2"}
2. "Start Session?"이라는 행동 경로 구성요소를 커스터마이즈하여 **Started Session** 경로에 앱을 선택합니다.

{: start="3"}
3. "Sessions?"라는 결정 분할 단계의 기본값을 유지합니다. 이 단계는 ">1 Session" 그룹을 지난 캘린더 일에 앱을 한 번 이상 사용한 사용자로 정의합니다.
4. ">1 Session" 그룹에 해당하는 사용자를 위한 메시지 단계를 커스터마이즈합니다. 이 사용 사례에서는 앱 방문에 감사하고 잠금 해제된 혜택을 강조합니다.
5. 광고 오디언스 업데이트 단계에서 Google 오디언스 싱크가 설정되어 있는지 확인하여, 첫 번째 이메일을 받은 후 여러 세션을 가진 사용자의 사용자 데이터를 업데이트하고 동기화합니다.
6. "A/B Test"라는 [실험 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#experiment-paths) 구성요소의 기본값을 유지합니다. 이 구성요소는 세션이 2회 미만인 사용자에게 두 가지 프로모션(다음 단계에서 커스터마이즈) 중 하나를 무작위로 발송합니다.
7. 실험 경로의 일부로 사용자에게 발송할 두 가지 프로모션을 커스터마이즈합니다. 이 사용 사례에서는 하나를 3개월 구독 20% 할인 프로모션으로, 다른 하나를 1개월 구독 10% 할인 프로모션으로 만듭니다.

![사용자의 세션 수에 따라 분기 경로가 있는 Canvas 단계.]({% image_buster /assets/img/canvas_templates/lapsing_user_8.png %}){: style="max-width:70%;"}

### 7단계: Canvas 테스트 및 시작 {#step-7-test-and-launch-the-canvas}

Canvas를 테스트하고 검토하여 예상대로 작동하는지 확인한 후 **Launch Canvas**를 선택하여 시작합니다. 이제 30일 이상 앱을 방문하지 않았고 메시징 채널에 가입한 사용자에게 복귀를 유도하는 이메일이 발송됩니다!

{% alert tip %}
Canvas를 시작하기 전과 후에 고려해야 할 사항은 [시작 전후 체크리스트]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist#things-to-consider-before-launch)를 확인하세요.
{% endalert %}