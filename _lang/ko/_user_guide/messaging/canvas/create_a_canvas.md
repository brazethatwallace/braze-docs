---
nav_title: Canvas 만들기
article_title: Canvas 만들기
page_order: 1
description: "Canvas를 만들고 시작하는 방법을 알아보세요. 기본 설정, 진입 스케줄, 타겟 오디언스, 발송 설정, 여정 구축 등을 다룹니다."
tool: Canvas
search_rank: 1
---

# Canvas 만들기 {#create-a-canvas}

> 이 참조 문서에서는 Canvas를 만들고, 관리하고, 테스트하는 데 필요한 단계를 다룹니다. 이 가이드를 따르거나 [Canvas Braze 학습 과정](https://learning.braze.com/quick-overview-canvas-setup)을 확인하세요. [Braze 캔버스 템플릿]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates)에서 시작하여 설정 시간을 단축할 수도 있습니다. 자세한 내용은 [캔버스 템플릿]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates)을 참조하세요. 자연어 설명으로 Canvas 초안을 작성하려면 [Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#canvases)에 요청하세요.

{% details 기존 Canvas 편집기 세부 정보 펼치기 %}
더 이상 기존 Canvas 환경을 사용하여 Canvases를 만들거나 복제할 수 없습니다. Braze는 최신 편집기로 [Canvases를 복제]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases)할 것을 권장합니다.
{% enddetails %}

## 1단계: 새 Canvas 설정하기 {#step-1-set-up-a-new-canvas}

먼저 **메시징** > **Canvas**로 이동한 다음 **Canvas 만들기**를 선택합니다.

Canvas 빌더가 Canvas 설정 과정을 단계별로 안내합니다. 이름 지정부터 전환 이벤트 설정, 고객 여정으로 대상 사용자를 유입하는 것까지 모든 과정을 포함합니다. 아래 각 탭을 선택하여 각 빌더 단계에서 조정할 수 있는 설정을 확인하세요.

{% tabs local %}
  {% tab 기본 사항 %}
    여기에서 Canvas의 기본 사항을 설정합니다:
    - Canvas 이름 지정
    - Teams 추가
    - 태그 추가
    - 전환 이벤트 할당 및 이벤트 유형과 기한 선택

    [기본 사항 단계](#step-11-start-with-your-canvas-basics)에서 자세히 알아보세요.
  {% endtab %}
  {% tab 진입 스케줄 %}
    여기에서 사용자가 Canvas에 진입하는 방법과 시기를 결정합니다:
    - 예약 전달: 시간 기반 Canvas 진입 방식입니다
    - 실행 기반 전달: 사용자가 정의된 동작을 수행한 후 Canvas에 진입합니다
    - API 트리거: API 요청을 사용하여 사용자를 Canvas에 진입시킵니다

    [진입 스케줄 단계](#step-12-determine-your-canvas-entry-schedule)에서 자세히 알아보세요.
  {% endtab %}
  {% tab 타겟 오디언스 %}
    여기에서 타겟 오디언스를 선택합니다:
    - Segments와 필터를 추가하여 오디언스 생성
    - Canvas 재진입 및 진입 제한 세부 조정
    - 타겟 오디언스 요약 확인

    [타겟 오디언스 단계](#step-13-set-your-target-entry-audience)에서 자세히 알아보세요.
  {% endtab %}
  {% tab 전송 설정 %}
    여기에서 Canvas 전송 설정을 선택합니다:
    - 구독 설정 선택
    - Canvas 메시지에 대한 전송 사용량 제한 설정
    - 방해금지 시간 활성화 및 설정

    [전송 설정 단계](#step-14-select-your-send-settings)에서 자세히 알아보세요.
  {% endtab %}
  {% tab Canvas 빌드 %}
    여기에서 Canvas를 빌드합니다.

    Canvas 빌더를 사용하여 [Canvas를 빌드하는 방법](#step-2-build-your-canvas)을 알아보세요.
  {% endtab %}
  {% tab 요약 %}
    여기에서 Canvas 세부 정보의 요약을 확인할 수 있습니다. [Canvas 승인 워크플로]({{site.baseurl}}/user_guide/messaging/governance/approvals)가 활성화되어 있는 경우, 출시 전에 나열된 Canvas 세부 정보를 승인할 수 있습니다.

  {% endtab %}
{% endtabs %}

### 1.1단계: Canvas 기본 사항으로 시작하기 {#step-11-start-with-your-canvas-basics}

여기에서 Canvas의 이름을 지정하고, [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams)를 할당하고, [태그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)를 만들거나 추가합니다. Canvas에 대한 전환 이벤트도 할당할 수 있습니다.

{% alert tip %}
Canvas에 태그를 지정하면 쉽게 찾고 보고서를 작성할 수 있습니다. 예를 들어, [보고서 빌더]({{site.baseurl}}/user_guide/analytics/reports/report_builder)를 사용할 때 특정 태그로 필터링할 수 있습니다.
{% endalert %}

![Canvas 이름, 설명, 위치 및 태그 필드가 있는 Canvas 세부 정보 페이지.]({% image_buster /assets/img/canvas_details.png %}){: style="max-width:70%;"}

#### 전환 이벤트 선택하기 {#choose-conversion-events}

전환 이벤트 유형을 선택한 다음 기록할 전환을 선택합니다. 이러한 [전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)는 Canvas의 효율성을 측정합니다.

![3일 전환 기한 이내에 구매를 완료한 사용자의 대화를 기록하기 위한 구매 완료 전환 이벤트 유형이 포함된 주요 전환 이벤트 A.]({% image_buster /assets/img/add_canvas_conversions.png %})

Canvas에 여러 배리언트 또는 대조군이 있는 경우, Braze는 이 전환 이벤트를 사용하여 이 전환 목표를 달성하기 위한 최적의 배리에이션을 결정합니다. 동일한 로직을 사용하여 여러 전환 이벤트를 만들 수 있습니다.

### 1.2단계: Canvas 진입 스케줄 결정하기 {#step-12-determine-your-canvas-entry-schedule}

사용자가 Canvas에 진입할 수 있는 세 가지 방법 중 하나를 선택할 수 있습니다.

#### 진입 스케줄 유형 {#entry-schedule-types}

{% tabs local %}
{% tab 예약 전달 %}
예약 전달을 사용하면 Campaign을 스케줄하는 것과 유사하게 사용자가 시간 스케줄에 따라 진입합니다. Canvas가 출시되자마자 사용자를 등록하거나, 미래의 특정 시점에 여정에 진입시키거나, 반복 기준(매일, 매주 또는 매월)으로 진입시킬 수 있습니다.

월별 반복 스케줄을 선택한 경우 일부 월에는 선택한 날짜가 없을 수 있습니다. 예를 들어, Canvas를 매월 31일에 전송하도록 설정했다고 가정해 보겠습니다. 이 경우 Braze는 4월 31일이 존재하지 않으므로 4월 30일처럼 해당 월의 마지막 날에 전송합니다.

이 예시에서 시간 기반 옵션에 따라 사용자는 2025년 11월 14일부터 2025년 12월 31일까지 매주 화요일 현지 시간대 오후 12시에 이 Canvas에 진입합니다.

![유형이 '예약'으로 설정된 '진입 스케줄' 페이지. 선택에 따라 빈도, 시작 시간, 반복, 요일 등의 시간 기반 옵션이 표시됩니다.]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})

현지 시간대 전달을 사용하면 Braze는 진입 자격을 두 번 평가합니다: 첫 번째로 스케줄된 날짜의 사모아 시간(UTC+13)에, 두 번째로 사용자의 현지 시간에 평가합니다. 사용자가 Canvas에 진입하려면 두 검사 모두 통과해야 합니다. 진입 필터가 상대적 시간 범위(예: "2일 이상 전")를 사용하는 경우, 첫 번째 검사 시점에 24시간이 경과하지 않아 사용자가 하루 늦게 진입할 수 있습니다. 이를 방지하려면 최소 2일 이상의 더 넓은 시간 범위를 사용하세요. 자세한 내용은 [Braze는 현지 시간대 전달을 위해 언제 사용자를 평가하나요?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#when-does-braze-evaluate-users-for-local-time-zone-delivery)를 참조하세요.
{% endtab %}
{% tab 실행 기반 전달 %}
실행 기반 전달을 사용하면 사용자가 앱 열기, 구매, 커스텀 이벤트 트리거 등 특정 동작을 수행할 때 Canvas에 진입하고 메시지를 수신하기 시작합니다.

**진입 오디언스** 창에서 재자격 규칙 및 최대 게재빈도 설정을 포함한 Canvas 동작의 다른 측면을 제어할 수 있습니다. 실행 기반 전달은 인앱 메시지가 있는 Canvas 구성요소에는 사용할 수 없습니다.

![실행 기반 전달의 예시. 사용자는 2025년 6월 10일 오후 1:30부터 시작되는 진입 기간 동안 구매를 완료하면 Canvas에 진입합니다.]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

{% alert note %}
**Canvas 단계와 상호작용**은 Canvases의 실행 기반 진입 트리거로 사용할 수 없습니다. Campaign의 트리거로만 사용할 수 있습니다. 하나의 Canvas에서 다른 Canvas를 트리거하려면 [대상으로 전송]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination) Canvas 구성요소를 사용하거나 `/canvas/trigger/send` 엔드포인트를 호출하는 [Braze 간 웹훅]({{site.baseurl}}/user_guide/channels/webhooks/use_case_create_a_braze_to_braze_webhook#trigger-a-second-canvas-from-an-initial-canvas)을 만드세요.
{% endalert %}

{% alert important %}
실행 기반 Canvas가 예상보다 일찍 메시지를 전송하는 경우, 커스텀 이벤트 타임스탬프가 소급된 시간이 아닌 현재 시간으로 전송되었는지 확인하세요. 예를 들어, 실행 기반 Canvas에 사용자가 커스텀 이벤트를 수행한 후 3시간의 지연이 있는 경우, Braze는 커스텀 이벤트와 함께 전송된 타임스탬프를 사용하여 해당 지연을 평가합니다. 타임스탬프가 3시간 이상 소급된 경우, Braze는 지연이 이미 경과한 것으로 처리하여 메시지를 즉시 전송합니다.
{% endalert %}
{% endtab %}
{% tab API 트리거 전달 %}
API 트리거 전달을 사용하면 API를 통해 [`/canvas/trigger/send` 엔드포인트]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)를 사용하여 사용자가 추가된 후 Canvas에 진입하고 메시지를 수신하기 시작합니다. 대시보드에서 이 작업을 수행하는 예시 cURL 요청을 찾을 수 있으며, [컨텍스트 객체]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)를 사용하여 선택적 [`context`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)를 할당할 수도 있습니다.

![Canvas ID와 cURL 요청 예시가 포함된 API 트리거 전달의 예시.]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

API 트리거 전달에 다음 엔드포인트를 사용할 수 있습니다:
- [POST: API 트리거 전달을 통한 Canvas 메시지 전송]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)
- [POST: API 트리거 Canvases 스케줄]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases)
- [POST: 스케줄된 API 트리거 Canvases 업데이트]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases)
{% endtab %}
{% endtabs %}

전달 방법을 선택한 후 사용 사례에 맞게 설정을 조정하고, 타겟 오디언스 설정으로 계속 진행합니다.

{% details 기존 편집기를 사용하는 Canvases의 중복 제거 동작 %}
재자격 기간이 Canvas의 최대 기간보다 짧으면 사용자가 재진입하여 하나 이상의 구성요소 메시지를 수신할 수 있습니다. 사용자의 재진입이 이전 진입과 동일한 구성요소에 도달하는 경우, Braze는 해당 구성요소의 메시지를 중복 제거합니다.

사용자가 Canvas에 재진입하여 이전 진입과 동일한 구성요소에 도달하고 각 진입에 대해 인앱 메시지를 받을 자격이 있는 경우, 사용자는 세션을 두 번 다시 열면 메시지를 두 번 받게 됩니다(인앱 메시지 우선순위에 따라 다름).
{% enddetails %}

### 1.3단계: 타겟 진입 오디언스 설정하기 {#step-13-set-your-target-entry-audience}

**타겟 오디언스** 단계에서 정의한 기준에 맞는 사용자만 여정에 진입할 수 있으며, 이는 Braze가 사용자가 Canvas 여정에 진입하기 **전에** 먼저 타겟 오디언스의 자격을 평가한다는 의미입니다. 예를 들어, 신규 사용자를 타겟팅하려면 앱을 처음 사용한 지 1주일 미만인 사용자 Segment를 선택할 수 있습니다.

{% alert important %}
여러 앱이 있는 워크스페이스에서 Canvas 진입 오디언스 자격(Segments 및 필터 포함)은 사용자가 Canvas에 진입할 때만 평가되며, 개별 메시지 단계에서는 평가되지 않습니다. 워크스페이스에 여러 앱이 있고 메시지 단계가 특정 앱의 사용자만 타겟팅하도록 해야 하는 경우, 각 메시지 단계에서 다음 방법 중 하나를 사용하세요:
- 메시지 단계의 [전달 유효성 검사]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations)에서 **메시지 전송 시 오디언스 유효성 검사**를 활성화하고 앱별 Segments 또는 필터를 추가합니다.
- Liquid를 사용하여 전송 시점에 타겟 기기 또는 앱을 확인합니다.

이러한 보호 조치가 없으면 하나의 앱에서 여정에 자격을 얻은 사용자가 워크스페이스의 다른 앱도 사용하는 경우 다른 앱용 메시지를 받을 수 있습니다.
{% endalert %}

**진입 제어**에서 Canvas가 실행되도록 스케줄될 때마다 사용자 수를 제한할 수 있습니다. API 트리거 기반 및 실행 기반 Canvases의 경우 이 제한은 매 UTC 시간에 적용됩니다.

{% multi_lang_include alerts/warning_alerts.md alert='Canvas race condition audience trigger' %}

#### 오디언스 테스트하기 {#testing-your-audience}

타겟 오디언스에 Segments와 필터를 추가한 후 [사용자를 검색]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)하여 오디언스 기준에 맞는지 확인함으로써 오디언스가 예상대로 설정되었는지 테스트할 수 있습니다.

![외부 사용자 ID 또는 Braze ID로 검색할 수 있는 '사용자 검색' 필드.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### 진입 제어 선택하기 {#selecting-entry-controls}

진입 제어는 사용자가 Canvas에 재진입할 수 있는지 여부를 결정합니다. 진입 스케줄 유형에 따라 선택한 주기로 이 Canvas에 잠재적으로 진입하는 사용자 수를 제한할 수도 있습니다:

- **예약:** Canvas의 수명 기간 또는 Canvas가 스케줄될 때마다
- **실행 기반:** 시간별, 일별 또는 Canvas의 수명 기간
- **API 트리거:** 시간별, 일별 또는 Canvas의 수명 기간

예를 들어, 예약된 Canvas가 있고 **진입 수 제한**을 선택한 후 **최대 진입** 필드를 500,000명으로 설정하고 **Canvas가 스케줄될 때마다**를 제한 주기로 설정하면, Canvas는 스케줄된 전송당 500,000명의 사용자에게만 전송합니다.

!['사용자가 Canvas에 재진입할 수 있음' 및 '진입 수 제한' 체크박스가 표시된 '진입 제어' 페이지.]({% image_buster /assets/img_archive/entry_controls.png %})

{% alert tip %}
Braze는 IP 워밍에 **Canvas가 스케줄될 때마다**를 선택하지 않는 것을 권장합니다. 이렇게 하면 전송량이 증가할 수 있습니다.
{% endalert %}

#### 종료 기준 설정하기 {#setting-exit-criteria}

[종료 기준]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria)을 설정하여 Canvas에서 종료할 사용자를 결정합니다. 사용자가 예외 이벤트를 수행하거나 Segments 및 필터에 일치하면 추가 메시지를 받지 않습니다.

#### 대상 집단 계산하기 {#calculating-target-population}

**대상 집단** 섹션에서 선택한 Segments 및 추가 필터 등 오디언스 요약과 메시징 채널별 도달 가능한 사용자 수 분석을 확인할 수 있습니다. 기본 추정치 대신 타겟 오디언스에서 도달 가능한 정확한 사용자 수를 계산하려면 [정확한 통계 계산]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#calculating-exact-statistics)을 선택합니다.

참고 사항:

- 정확한 통계를 계산하는 데 몇 분이 걸릴 수 있습니다. 이 기능은 Segment 수준에서만 정확한 통계를 계산하며, 필터 또는 필터 그룹 수준에서는 계산하지 않습니다.
- 정확한 통계가 로딩되는 동안 반올림된 추정치가 표시될 수 있습니다. 정확한 수치는 로딩이 완료되면 **도달 가능한 사용자** 섹션에 나타납니다. **추가 통계 보기**를 선택하여 상세 분석을 확인할 수 있습니다.
- 대규모 Segments의 경우 정확한 통계를 계산할 때도 약간의 변동이 있는 것은 정상입니다. 이 기능의 정확도는 99.999% 이상입니다.

타겟 사용자의 평균 수명 매출 등 추가 통계를 보려면 **추가 통계 보기**를 선택합니다.

![정확한 통계 계산 옵션이 있는 대상 집단 분석.]({% image_buster /assets/img_archive/canvas_exact_stats.png %})

#### 타겟 오디언스 수와 도달 가능한 사용자 수가 다를 수 있는 이유 {#why-the-target-audience-count-could-differ-from-the-reachable-users-count}

{% multi_lang_include audience/segments.md section='Differing audience size' %}

### 1.4단계: 전송 설정 선택하기 {#step-14-select-your-send-settings}

**전송 설정**을 선택하여 구독 설정을 편집하고, 사용량 제한조치를 활성화하고, [방해금지 시간]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)을 활성화합니다. [사용량 제한조치]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-rate-limiting) 또는 [최대 게재빈도 설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping)을 활성화하면 사용자에게 가해지는 마케팅 압력을 완화하고 과도한 메시징을 방지할 수 있습니다.

이메일 및 푸시 채널을 타겟팅하는 Canvases의 경우, 명시적으로 옵트인한 사용자만 메시지를 수신하도록 Canvas를 제한할 수 있습니다(가입 또는 탈퇴 사용자 제외). 예를 들어, 옵트인 상태가 다른 세 명의 사용자가 있다고 가정해 보겠습니다:

{% multi_lang_include messaging/intelligent_channel_user_examples.md %}

이렇게 하려면 **구독 설정**을 "옵트인한 사용자에게만" 이 Canvas를 전송하도록 설정합니다. 이 옵션을 선택하면 옵트인한 사용자만 이메일을 수신하고, Braze는 기본적으로 푸시가 활성화된 사용자에게만 푸시를 전송합니다.

이러한 구독 설정은 단계별로 적용되며, 진입 오디언스에는 영향을 미치지 않습니다. 따라서 이 설정은 각 Canvas 단계를 수신할 사용자의 자격을 평가하는 데 사용됩니다.

{% alert important %}
이 구성을 사용하는 경우 **타겟 오디언스** 단계에 오디언스를 단일 채널로 제한하는 필터를 포함하지 마세요(예: `Foreground Push Enabled = True` 또는 `Email Subscription = Opted-In`).
{% endalert %}

Canvas에 [방해금지 시간]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)(메시지가 전송되지 않는 시간)을 지정할 수 있습니다. **전송 설정**에서 **방해금지 시간 활성화**를 선택합니다. 그런 다음 사용자의 현지 시간대에서 방해금지 시간을 선택하고, 메시지를 중단할지 아니면 다음 가능한 시간에 전송할지 선택합니다.

**다음 가능한 시간에 전송**을 선택하면 방해금지 시간이 메시지를 억제하고 방해금지 시간 이후 다음 가능한 시간에 전송합니다. 예를 들어, 방해금지 시간이 사용자의 현지 시간 기준 오전 11시 30분부터 오후 2시 30분까지 메시지 전송을 방지하도록 설정되어 있고, 사용자가 오전 11시 35분에 메시지 단계에 진입한다고 가정해 보겠습니다. 이 시간은 방해금지 시간 이내이므로 메시지가 아직 전송되지 않으며, 사용자는 방해금지 시간 이후인 오후 2시 30분에 메시지 단계를 수신합니다.

![방해금지 시간 활성화 체크박스가 표시된 '방해금지 시간' 페이지. 활성화되면 시작 시간, 종료 시간 및 대체 동작을 설정할 수 있습니다.]({% image_buster /assets/img/quiet_hours.png %})

## 2단계: Canvas 작성하기 {#step-2-build-your-canvas}

{% alert tip %}
[BRAZE 캔버스 템플릿]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates)을 사용하여 Canvas 작성 시간을 절약하고 프로세스를 간소화하세요! 사전 제작된 템플릿 라이브러리를 둘러보고 사용 사례에 맞는 템플릿을 찾아 특정 요구에 맞게 커스터마이즈할 수 있습니다. 자세한 내용은 [Canvas 템플릿]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates)을 참조하세요.
{% endalert %}

### 2.1단계: 배리언트 추가 {#step-21-add-a-variant}

!["배리언트 추가" 옵션이 있는 컨텍스트 메뉴를 표시하도록 "배리언트 추가" 버튼이 선택된 화면.]({% image_buster /assets/img_archive/canvas_add_variant.gif %}){: style="float:right;max-width:40%;margin-left:15px;"}

**배리언트 추가**를 선택한 다음 Canvas에 새 배리언트를 추가합니다. 배리언트는 사용자가 따라가는 여정을 나타내며, 여러 단계와 분기를 포함할 수 있습니다.

<i class="fas fa-plus-circle"></i> 플러스 버튼을 선택하여 추가 배리언트를 추가할 수 있습니다. 새 배리언트를 추가하면 사용자가 각 배리언트에 어떻게 배분될지 조정할 수 있어, 다양한 인게이지먼트 전략의 효과를 교차 비교하고 분석할 수 있습니다.

![BRAZE 캔버스에 두 개의 예시 배리언트가 있는 화면.]({% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %})

{% alert tip %}
기본적으로 Canvas 배리언트 할당은 사용자 ID와 Canvas ID의 결정론적 해시에 의해 결정되며([무작위 버킷 번호]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers)가 아님), 배리언트 배분 비율이 변경되지 않는 한 특정 사용자는 재진입 시 항상 동일한 배리언트에 할당됩니다. 출시 후 배리언트 배분을 조정하면 Canvas에 재진입할 때 사용자가 다른 배리언트에 할당될 수 있습니다. <br><br>배분 비율이 변경되어도 고정된 할당이 필요한 경우, 단일 Canvas 배리언트를 사용하고 [오디언스 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) 단계로 사용자를 라우팅하세요. 여정의 시작 부분에서 [사용자 업데이트]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) 단계를 사용하여 커스텀 속성에 무작위 숫자를 저장한 다음, 오디언스 경로에서 해당 속성으로 필터링합니다.

{% details 단계 보기 %}

1. 무작위 숫자를 저장할 **숫자** 커스텀 속성을 생성합니다. `lottery_number` 또는 `random_assignment`처럼 찾기 쉬운 이름을 지정합니다. 대시보드에서 **데이터 설정** > **커스텀 속성**으로 이동합니다.<br><br>
2. 단일 Canvas 배리언트를 사용합니다(또는 각 배리언트에 동일한 사용자 업데이트 단계를 추가합니다). 여정 시작 부분에 [사용자 업데이트]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) 단계를 추가합니다. 이 단계는 사용자가 오디언스 경로 단계에 도달하기 전에 무작위 숫자를 생성하고 저장합니다.<br><br>
3. 사용자 업데이트 단계에서 [고급 JSON 편집기]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#advanced-json-editor)를 선택합니다. {% raw %}{% random %}{% endraw %} 태그를 사용하여 숫자를 생성합니다. 자세한 내용은 [무작위 숫자가 포함된 메시지 보내기]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#send-messages-with-a-random-number)를 참조하세요. 예를 들어, {% raw %}`{% random 10 %}`{% endraw %}은 0부터 9까지의 정수를 반환합니다. 1단계의 커스텀 속성을 다음과 같은 JSON으로 설정합니다:<br><br>{% raw %}
```json
{% if {{custom_attribute.${lottery_number}}} == blank %}
{% capture lottery_number_str %}{% random 10 %}{% endcapture %}
{
  "attributes": [
    {
      "lottery_number": {{ lottery_number_str | plus: 0 }}
    }
  ]
}
{% endif %}
```
{% endraw %}
<br><br>
{% raw %}`{% if %}`{% endraw %} 블록은 속성이 비어 있을 때만 숫자를 설정하므로, 사용자가 Canvas에 재진입할 때도 동일한 할당을 유지합니다.<br><br>

{: start="4"}
4. 사용자 업데이트 단계 뒤에 [오디언스 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) 단계를 추가합니다. 각 오디언스 그룹에서 배리언트 배분 비율 대신 커스텀 속성 기반 필터를 추가합니다.<br><br>예를 들어, {% raw %}`{% random 10 %}`{% endraw %}을 사용한 경우, 한 그룹은 `lottery_number`가 **4 미만**, 다른 그룹은 **3 초과 7 미만**, 세 번째 그룹은 **6 초과 10 미만**으로 설정할 수 있습니다.

{% enddetails %}
{% endalert %}

### 2.2단계: Canvas 단계 추가 {#step-22-add-canvas-steps}

**구성요소** 사이드바에서 구성요소를 드래그 앤 드롭하여 Canvas 워크플로에 추가 단계를 추가할 수 있습니다. 또는 <i class="fas fa-plus-circle"></i> 플러스 버튼을 선택하여 팝오버 메뉴로 구성요소를 추가할 수도 있습니다.

{% alert tip %}
단계를 더 추가하기 시작하면 확대/축소 수준을 전환하여 세부 사항에 집중하거나 전체 사용자 여정을 살펴볼 수 있습니다. <kbd>Shift</kbd> + <kbd>+</kbd>로 확대하거나 <kbd>Shift</kbd> + <kbd>-</kbd>로 축소할 수 있습니다.
{% endalert %}

![BRAZE 캔버스에 지연 단계를 추가하는 구성요소 검색 창.]({% image_buster /assets/img_archive/add_components_flow.png %}){: style="max-width:80%;"}

{% alert important %}
Canvas에 최대 200개의 단계를 추가할 수 있습니다. Canvas가 200단계를 초과하면 로딩 문제가 발생할 수 있습니다.
{% endalert %}

#### 최대 기간 {#maximum-duration}

Canvas 여정의 단계가 늘어나면 최대 기간은 사용자가 이 Canvas를 완료하는 데 소요될 수 있는 최장 시간입니다. 이는 가장 긴 경로에 대해 각 배리언트의 각 단계 지연 시간과 트리거 기간을 합산하여 계산됩니다. 예를 들어, Canvas에 3일 지연이 있는 지연 단계와 메시지 단계가 있으면 Canvas의 최대 기간은 3일입니다.

#### 단계 편집하기 {#editing-a-step}

사용자 여정의 단계를 편집하고 싶으신가요? Canvas 워크플로에 따른 편집 방법을 확인하세요!

Canvas 워크플로의 모든 단계는 해당 구성요소를 선택하여 편집할 수 있습니다. 예를 들어, 워크플로의 첫 번째 단계인 [지연]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) 구성요소를 특정 날짜로 편집하고 싶다고 가정해 보겠습니다. 해당 단계를 선택하여 설정을 확인하고 지연을 3월 1일로 조정합니다. 이렇게 하면 3월 1일에 사용자가 Canvas의 다음 단계로 이동합니다.

![지연이 "특정 날짜까지"로 설정된 예시 "지연" 단계.]({% image_buster /assets/img_archive/edit_delay_flow.png %})

또는 [작업 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) 단계의 **액션 설정**을 빠르게 편집하고 조정하여 사용자를 일정 기간 동안 유지할 수 있습니다. 이를 통해 평가 기간 동안의 행동을 기반으로 다음 경로의 우선순위를 지정합니다.

![Canvas의 두 번째 단계인 "액션 설정"으로, 평가 기간이 1일로 설정되어 있는 화면.]({% image_buster /assets/img_archive/action_paths_flow.png %})

Canvas의 경량 구성요소는 간편한 편집 환경을 제공하므로, Canvas의 세부 사항 조정이 더 쉬워집니다.

#### Canvas의 메시지 {#messages-in-canvas}

Canvas 구성요소의 메시지를 편집하여 특정 단계에서 전송할 메시지를 제어할 수 있습니다. Canvas는 이메일, 모바일 및 웹 푸시 메시지, 그리고 다른 시스템과 통합하기 위한 웹훅을 전송할 수 있습니다. Campaigns와 마찬가지로 특정 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) 템플릿을 사용하여 메시지를 개인화할 수 있습니다.

{% alert tip %}
Canvas 구성요소 이름을 메시지 및 링크 템플릿에 포함할 수 있다는 것을 알고 계셨나요?<br>
`campaign.${name}` Liquid 태그를 Canvas에서 사용하여 현재 Canvas 구성요소 이름을 표시할 수 있습니다.
{% endalert %}

메시지 구성요소는 사용자에게 전송되는 메시지를 관리합니다. **메시징 채널**을 선택하고 **전달 설정**을 조정하여 Canvas 메시징을 최적화할 수 있습니다. 이 구성요소에 대한 자세한 내용은 [메시지]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)를 확인하세요.

![메시징 채널이 선택되어 Android 푸시, Content Cards, 이메일 등 사용 가능한 메시징 채널 목록을 표시하는 "메시지 설정" 단계.]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

Canvas 구성요소 구성을 완료한 후 **완료**를 선택합니다.

{% tabs local %}
{% tab Canvas 진입 속성정보 %}

[`context` 객체]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)는 Canvas 생성의 **진입 스케줄** 단계에서 구성되며, 사용자를 Canvas에 진입시키는 트리거를 나타냅니다. 이 속성정보를 통해 API 트리거 Canvases의 진입 페이로드 속성정보에도 접근할 수 있습니다. `context` 객체는 최대 50KB까지 가능합니다.

Canvas 진입 시 생성된 이러한 속성정보를 참조하려면 다음 Liquid를 사용합니다: {% raw %} ``context.${property_name}`` {% endraw %}. 이벤트는 이 방식으로 사용하려면 커스텀 이벤트 또는 구매 이벤트여야 합니다.

{% raw %}
예를 들어, 다음 요청을 살펴보겠습니다: `"context" : {"product_name" : "shoes", "product_price" : 79.99}`. 이 Liquid ``{{context.${product_name}}}``를 사용하여 메시지에 "shoes"라는 단어를 추가할 수 있습니다.
{% endraw %}

{% endtab %}

{% tab 이벤트 속성정보 %}
이벤트 속성정보는 커스텀 이벤트 및 구매에 설정하는 속성정보입니다. 이러한 `event_properties`는 실행 기반 전달을 사용하는 Campaigns와 Canvases에서 사용할 수 있습니다.

Canvas에서 커스텀 이벤트 및 구매 이벤트 속성정보는 작업 경로 단계 뒤에 오는 모든 메시지 단계의 Liquid에서 사용할 수 있습니다. 이러한 `event_properties`를 참조하려면 다음 Liquid를 사용합니다: {% raw %} ``{{event_properties.${property_name}}}`` {% endraw %}. 이벤트는 메시지 구성요소에서 이 방식으로 사용하려면 커스텀 이벤트 또는 구매 이벤트여야 합니다.

작업 경로 뒤 첫 번째 메시지 단계에서 해당 작업 경로에서 참조한 이벤트와 관련된 `event_properties`를 사용할 수 있습니다. 이 작업 경로 단계와 메시지 단계 사이에 다른 단계(작업 경로 또는 메시지 단계가 아닌)가 있을 수 있습니다. 메시지 단계가 작업 경로 단계의 모든 사용자 경로가 아닌 특정 경로로 추적될 수 있는 경우에만 `event_properties`에 접근할 수 있습니다.

{% endtab %}
{% endtabs %}

### 2.3단계: 연결 편집 {#step-23-edit-connections}

단계 간 연결을 이동하려면 두 구성요소를 연결하는 화살표를 선택한 후 다른 구성요소를 선택합니다. 연결을 제거하려면 화살표를 선택한 후 Canvas 작성기 하단의 **연결 취소**를 선택합니다.

단일 배리언트에 동일한 오디언스와 전송 시간을 가진 여러 분기가 있는 경우, Braze는 해당 분기 간 균등 분배를 보장하지 않습니다. 배분이 먼저 생성된 분기에 편향될 수 있습니다. 균등 분배를 위해서는 각 분기에 [무작위 버킷 번호]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) 필터를 사용하세요. 자세한 내용은 [하나의 배리언트에 여러 분기가 있는 Canvas에서 오디언스와 전송 시간이 동일한 경우 어떻게 되나요?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches)를 참조하세요.

## 3단계: 대조군 추가 {#step-3-add-a-control-group}

<i class="fas fa-plus-circle"></i> 플러스 버튼을 선택하여 새 배리언트를 추가하면 Canvas에 대조군을 추가할 수 있습니다.

Braze는 대조군에 배치된 사용자의 전환을 추적하지만, 해당 사용자에게는 메시지가 전송되지 않습니다. 정확한 테스트를 유지하기 위해 전환 이벤트 선택 화면에 표시된 것과 동일한 기간 동안 배리언트와 대조군의 전환 수를 추적합니다.

**배리언트 이름** 헤더를 더블 클릭하여 메시지 간 배분 비율을 조정할 수 있습니다.

이 예시에서는 Canvas가 두 개의 배리언트로 나뉘어 있습니다. 배리언트 1에는 사용자의 70%가 배정됩니다. 두 번째 배리언트는 나머지 30%의 사용자로 구성된 대조군입니다.

![BRAZE 캔버스의 배리언트 예시로, 70%가 '배리언트 1'로 이동하여 첫 번째 단계에서 1일 지연 후 두 번째 단계에서 메시지를 보냅니다. 나머지 30%는 후속 단계가 없는 '대조군'으로 이동합니다.]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

### BrazeAI로 캔버스 배리언트 최적화 {#optimize-canvas-variants-with-brazeai}

여러 최상위 배리언트가 있는 Canvas의 경우, **BrazeAI<sup>TM</sup>로 최적화**를 켜면 각 배리언트에 진입하는 사용자 비율이 자동으로 조정됩니다. BrazeAI<sup>TM</sup>는 배리언트 성능을 분석하여 기대 전환 수를 극대화합니다.

최소 두 개의 배리언트와 하나의 전환 이벤트를 추가합니다. 그런 다음 배리언트 비율을 선택하여 **배리언트 배분 편집**을 열고 **BrazeAI<sup>TM</sup>로 최적화**를 켭니다.

초기 전환 마감 이후, BrazeAI<sup>TM</sup>는 12시간마다 성능을 검토하고 전환을 가장 많이 유도하는 배리언트로 더 많은 사용자를 이동시킵니다. 최적화에서 확실한 우승자를 식별하면 이후 모든 적격 사용자가 해당 배리언트에 진입합니다.

이 최적화는 새로운 사용자가 자주 진입하는 Canvases에서 가장 효과적입니다.

## 4단계: 저장 및 실행 {#step-4-save-and-launch}

Canvas 생성이 완료되면 **Launch Canvas**를 선택하여 Canvas를 저장하고 실행합니다. Canvas를 실행한 후에는 **Canvas Details** 페이지에서 여정에 대한 분석이 수집되는 것을 확인할 수 있습니다.

나중에 다시 돌아와야 하는 경우 Canvas를 초안으로 저장할 수도 있습니다.

![Braze의 Canvas 예시.]({% image_buster /assets/img_archive/Canvas_Analytics.png %})

{% alert tip %}
실행 후 Canvas를 편집해야 하나요? 걱정 마세요! 자세한 내용은 [실행 후 Canvases 편집]({{site.baseurl}}/post-launch_edits)을 참조하세요.
{% endalert %}