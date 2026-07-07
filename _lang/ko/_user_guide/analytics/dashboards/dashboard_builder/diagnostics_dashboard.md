---
nav_title: 메시징 진단 대시보드
article_title: 메시징 진단 대시보드
description: "이 참조 문서에서는 Campaigns이나 Canvases에서 메시지가 예상대로 발송되지 않은 이유를 파악하는 데 도움이 되는 메시징 진단 대시보드에 대해 설명합니다."
alias: /ccdd/
page_order: 2
toc_headers: h2
---

# 메시징 진단 대시보드 {#messaging-diagnostics-dashboard}

> **메시징 진단** 대시보드는 메시지 발송 결과에 대한 상위 수준의 분석을 제공하여, 메시징 설정에서 트렌드를 파악하고 잠재적인 문제를 진단할 수 있도록 합니다. 이 대시보드를 통해 Campaigns이나 Canvases에서 메시지가 예상대로 발송되지 않은 이유를 파악할 수 있습니다.

{% alert important %}
**메시징 진단** 대시보드는 현재 얼리 액세스 중입니다. 얼리 액세스에 참여하려면 고객 성공 매니저에게 문의하세요.
{% endalert %}

## 주요 개념 {#key-concepts}

### 발송됨과 전달됨 {#sent-and-delivered}

이 대시보드는 Braze가 내부적으로 메시지를 처리한 방식을 보고하며, 메시지의 최종 전달 상태를 보고하는 것이 아니라는 점을 이해하는 것이 중요합니다.

이 대시보드에서 "발송됨"으로 표시된 메시지는 Braze가 해당 메시지를 성공적으로 처리하고 발송했음을 의미합니다. 대부분의 채널에서 이는 Braze가 관련 서드파티 발송 파트너에게 메시지를 전달했음을 의미합니다. 그러나 사용자의 기기에 최종 전달되었음을 보장하지는 않습니다.

Braze가 메시지를 "발송"하면, 최종 전달은 외부 서비스에 따라 달라질 수 있습니다. 각 채널에 대한 다음 예시를 참고하세요.

| 채널 | 최종 전달 예시 |
| --- | --- |
| Content Cards | 카드가 발송되었으며 조회 가능한 상태입니다. |
| 이메일 | Braze가 이메일 서비스 공급자(ESP)에게 메시지를 전달합니다. ESP가 최종 전달을 담당합니다. 예를 들어, 이메일 주소가 유효하지 않거나 받은편지함이 가득 찬 경우 ESP가 "반송"을 보고할 수 있습니다. |
| 인앱 메시지 | 메시지가 사용자에게 표시되었습니다. |
| LINE | 메시지가 발송 파트너에게 성공적으로 전달되었습니다. |
| 푸시 | Braze가 적절한 푸시 알림 서비스(iOS의 경우 Apple Push Notification service, Android의 경우 Firebase Cloud Messaging)에 메시지를 전달합니다. 해당 서비스가 기기로의 최종 알림 전달을 담당합니다. |
| SMS/MMS/RCS | Braze가 SMS 게이트웨이(예: Twilio)에 메시지를 전달합니다. 해당 게이트웨이가 이동통신사로의 최종 전달을 담당합니다. |
| 웹훅 | 웹훅 요청이 성공적으로 이루어졌으며, `2xx` 응답을 반환했습니다. |
| WhatsApp | 메시지가 발송 파트너에게 성공적으로 전달되었습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="발송됨과 전달됨" }

### 데이터 최신성 {#data-freshness}

이 대시보드의 데이터 업데이트 빈도는 시스템 부하에 따라 달라질 수 있습니다. 업데이트 빈도가 보장되지는 않지만, 대부분의 경우 1시간 미만입니다.

## 대시보드 구성 {#configuring-the-dashboard}

진단 대시보드에 접근하려면 **Analytics** > **대시보드 빌더**로 이동하여 Braze가 생성한 대시보드 목록에서 **Messaging Diagnostics**를 선택합니다.

대시보드를 실행하고 데이터를 확인하려면:

1. 대시보드 보고서의 소스로 **Campaigns** 또는 **Canvases**를 선택합니다.
2. 하나 이상의 Campaign 또는 Canvas를 선택합니다.
3. **Run Dashboard**를 선택하여 선택한 필터에 대한 데이터를 로드합니다.

![2025년 5월 25일부터 5월 31일까지의 웰컴 시리즈 Campaign에 대한 Campaign 및 Canvas 진단 예시.]({% image_buster /assets/img/messaging_diagnostics_dashboard_details_log.png %}){: style="max-width:45%;"} ![2025년 5월 25일부터 5월 31일까지의 웰컴 시리즈 Campaign에 대한 그래프 호버 시 Campaign 및 Canvas 진단 예시.]({% image_buster /assets/img/messaging_diagnostics_dashboard_drawer_expanded.png %}){: style="max-width:45%;"}

## 데이터 해석 {#interpreting-the-data}

{% alert note %}
대시보드는 최근 7일간의 데이터만 표시합니다. 모든 타임스탬프는 워크스페이스의 시간대로 표시됩니다.
{% endalert %}

### 요약 타일 {#summary-tiles}

페이지 상단에는 선택한 기간에 대한 주요 요약 타일이 있으며, 다음을 보여줍니다:

- **발송됨:** Braze가 성공적으로 처리하고 발송한 메시지의 총 수입니다.
  - **이메일, SMS/MMS/RCS, WhatsApp, LINE, 푸시:** 메시지가 발송 파트너에게 성공적으로 전달되었습니다.
  - **웹훅:** 웹훅 요청이 성공적으로 이루어졌으며, `2xx` 응답을 반환했습니다.
  - **Content Cards:** 카드가 발송되었으며 조회 가능한 상태입니다.
  - **인앱 메시지:** 메시지가 사용자에게 표시되었습니다.
- **미발송:** 중단된 메시지의 총 수입니다. 여기에는 Canvas에 진입하지 않았거나, 단계 실패를 경험했거나, 종료 이벤트를 수행하면서 종료 기준을 충족하여 Canvas를 종료한 Canvas 오디언스 멤버가 포함됩니다.

### 시간별 메시지 결과 {#message-outcomes-over-time}

이 시계열 차트는 메시지가 중단되었거나 사용자가 Canvas에서 제외된 이유를 시간별로 분석하여 보여줍니다. 이 차트의 결과 레이블은 정규화된 대시보드 레이블이며, 원시 이벤트 페이로드 값이 아닙니다. 이 차트에는 발송 수가 표시되지 않습니다.

### 메시지 결과 상세 로그 {#message-outcomes-granular-log}

대시보드에는 선택한 필터와 기간에 대한 개별 메시지 결과의 상세 테이블이 표시됩니다. 이 테이블을 사용하여 타임스탬프, 사용자 ID, 캔버스 단계, 결과, 세부 정보, 채널 등 특정 레코드를 검토할 수 있습니다.

테이블을 필터링하여 특정 레코드에 집중할 수 있습니다:

- **결과별 필터링:** 결과 필터에서 결과를 선택하여 해당 결과가 있는 행만 표시합니다(예: `Frequency capped` 또는 `User not eligible for channel`).
- **사용자 ID로 검색:** 검색 필드에 사용자 ID를 입력하여 해당 사용자의 행을 표시합니다.

두 필터를 모두 적용하면, 테이블은 선택한 결과와 입력한 사용자 ID 모두에 일치하는 행을 반환합니다.

테이블에서 행을 선택하면 세부 정보 패널이 열립니다. 세부 정보 패널은 해당 결과에 대한 추가 컨텍스트를 제공하며, Ask Operator가 근본 원인을 해결하는 데 도움이 되는 수정 가이드를 제공합니다.

![선택된 행과 세부 정보 패널 접근이 가능한 메시징 진단 상세 결과 로그.]({% image_buster /assets/img/messaging_diagnostics_dashboard_details_log.png %}){: style="max-width:45%;"} ![결과 컨텍스트와 수정 가이드가 포함된 메시징 진단 세부 정보 패널 확장 화면.]({% image_buster /assets/img/messaging_diagnostics_dashboard_drawer_expanded.png %}){: style="max-width:45%;"}

{% alert note %}
채널 필터는 특정 메시징 채널에 연결된 결과에 적용됩니다. 일부 결과는 채널에 구애받지 않으므로, 채널 필터를 적용하더라도 집계 보기에 여전히 나타날 수 있습니다.
{% endalert %}

### 중단 결과 {#abort-outcomes}

다음 정의는 대시보드에 표시되는 중단 결과를 설명합니다. 결과는 조사하려는 항목을 쉽게 찾을 수 있도록 카테고리별로 그룹화되어 있습니다.

{% alert note %}
메시징 진단의 중단 결과는 사람이 읽을 수 있는 대시보드 레이블입니다. [Currents 메시지 인게이지먼트 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)에서는 `abort_type` 및 `abort_log`와 같은 필드로 중단 정보가 표현됩니다. 이러한 데이터셋은 서로 다른 표현 방식과 처리 경로를 가지므로, Currents와 메시징 진단 간에 수치나 명칭이 다를 수 있습니다.
{% endalert %}

#### 콘텐츠 및 렌더링 {#content-and-rendering}

| 중단 결과 | 설명 |
| ---- | ---- |
| Content Card 만료됨 | 사용자가 보기 전에 Content Card가 만료되었습니다. |
| Content Card 유효하지 않음 | Content Card에 오류가 있어 사용자에게 발송되지 않았습니다. 일반적인 이유는 다음과 같습니다: {::nomarkdown}<ul><li> 최대 크기 초과(2 KB) </li><li> 만료 날짜가 유효하지 않음 </li><li> 메시지에 유효하지 않은 문자가 포함됨 </li></ul>{:/} |
| 연결된 콘텐츠 실패 | Braze가 메시지를 발송하려 했지만, 최대 재시도 횟수(기본값 5회) 이후 연결된 콘텐츠가 실패했습니다. **참고:** 이 수치는 최대 재시도 횟수에 도달하여 중단된 메시지 수를 나타내며, 실패한 연결된 콘텐츠 요청의 총 수가 아닙니다. |
| 인앱 메시지 렌더링 시간 초과 | 여러 번의 재시도 후에도 Liquid를 렌더링할 수 없어 시간이 초과되었습니다. |
| Liquid 중단 | [abort_message]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) Liquid 태그가 호출되어 발송이 취소되었습니다. |
| Liquid 렌더링 시간 초과 | Liquid 템플릿을 렌더링하는 데 너무 오래 걸렸습니다. 배너, 인앱 메시지, 이메일에서 가장 많이 발생합니다. |
| Liquid 구문 오류 | Liquid 템플릿에 파싱 오류가 있어 메시지가 취소되었습니다. |
| 미디어 URL 실패 | Braze가 메시지의 미디어 URL을 처리할 수 없었습니다. URL이 차단되었거나, 유효하지 않거나, 시간이 초과되었거나, 유효하지 않은 HTTP 상태를 반환했거나, SSL 유효성 검사에 실패한 경우에 발생할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="콘텐츠 및 렌더링" }

#### Campaign 및 Canvas 상태 {#campaign-and-canvas-state}

| 중단 결과 | 설명 |
| ---- | ---- |
| 지연 단계 실패 | [지연 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step#personalized-delays)가 실패하여 사용자가 Canvas를 종료했습니다. 이 실패는 다음과 같은 경우에 발생할 수 있습니다: {::nomarkdown}<ul><li> 개인화된 지연 단계에 제공된 변수가 비어 있거나 유효하지 않은 유형인 경우 </li><li> 지연이 Canvas 내에서 허용되는 최대 기간을 초과한 경우</li></ul>{:/} |
| 예외 또는 종료 이벤트 | 사용자가 이전에 메시지를 받을 자격이 있었지만, {::nomarkdown}<ul><li> 액션 기반 Campaign에 대한 <a href="/docs/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#step-3-select-exception-events">예외 이벤트</a> 를 수행하여 메시지가 중단되었거나, </li><li> Canvas <a href="/docs/user_guide/messaging/canvas/create_a_canvas#setting-exit-criteria">종료 기준</a> 을 충족하여 여정 중간에 제외되었습니다.</li></ul>{:/} |
| 비활성 Campaign | 메시지가 전송 중인 상태에서 Campaign이 중지되어 중단되었습니다. |
| 비활성 Canvas | 사용자가 여정에 진입하기 전에 Canvas가 중지되었습니다. |
| 비활성 캔버스 단계 | Canvas에서 다음과 같은 경우에 발생할 수 있습니다: {::nomarkdown}<ul><li> 캔버스 단계가 삭제된 경우 </li> <li>Canvas가 중지되어 모든 단계가 비활성화된 경우 </li></ul>{:/} |
| 볼륨 제한 | Campaign이 설정된 볼륨 제한에 도달하여 발송이 취소되었습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campaign 및 Canvas 상태" }

#### 사용량 제한 및 타이밍 {#rate-limiting-and-timing}

| 중단 결과 | 설명 |
| ---- | ---- |
| 최대 게재빈도 설정 적용됨 | 워크스페이스의 [최대 게재빈도 설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping) 규칙에 따라 사용자가 이미 허용된 최대 메시지 수를 수신하여 발송이 취소되었습니다. |
| 방해금지 시간 중단 | Campaign 또는 캔버스 단계에 대해 방해금지 시간이 활성화되어 있으며 대체 옵션이 **Abort message**로 설정되어 있습니다. 사용자가 방해금지 시간 중에 Campaign을 트리거하거나 Canvas 메시지 단계에 진입하여 메시지가 중단되었습니다. 그러나 이로 인해 사용자가 Canvas에서 종료되지는 않습니다. |
| 72시간 초과 사용량 제한 | [전달 속도 사용량 제한]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting)으로 인해 메시지가 72시간 이상 조절되어 발송이 중단되었습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사용량 제한 및 타이밍" }

#### 사용자 자격 및 프로필 {#user-eligibility-and-profile}

| 중단 결과 | 설명 |
| ---- | ---- |
| 중복 사용자 식별자 | 일치하는 식별자(예: 외부 ID, 이메일 주소, 전화번호)를 가진 여러 사용자가 이 메시지를 받을 자격이 있었습니다. 동일한 사용자에게 중복 발송을 방지하기 위해 이 메시지가 중단되었습니다. |
| 메시지 단계 사전 검사 실패 | Braze는 Canvas 메시지 단계의 전체 전달 유효성 검사 전에 오디언스 자격, 재자격, 채널 자격에 대한 기본 사전 검사를 먼저 실행합니다. 이 결과는 사용자 또는 메시지가 해당 검사 중 하나에 실패하여 해당 단계에서 메시지가 중단되었음을 의미합니다. |
| 트리거된 메시지 사전 검사 실패 | Braze는 이 트리거에서 발송할 메시지를 생성하기 전에 오디언스 자격, 재자격, 채널 자격에 대한 기본 사전 검사를 먼저 실행합니다. 이 결과는 사용자 또는 메시지가 해당 검사 중 하나에 실패하여 메시지가 중단되었음을 의미합니다. |
| 사용자가 더 이상 자격이 없음 | 사용자가 처음에는 타겟 오디언스에 포함되어 있었지만, Braze가 메시지를 발송하거나 사용자를 Canvas에 진입시키기 전에 오디언스 기준에 더 이상 일치하지 않게 되었습니다. 사용자가 처음 오디언스 기준을 충족한 시점과 오디언스에서 벗어난 시점 사이의 시간 차이는 다음과 같은 지연으로 인해 발생할 수 있습니다: {::nomarkdown}<ul><li>Intelligent Timing</li><li>방해금지 시간</li><li>현지 시간</li><li>전달 속도 사용량 제한(Canvas 진입에는 적용되지 않음)</li><li>메시징 파이프라인 지연</li></ul>{:/} |
| 단계에 대한 사용자 자격 없음 | 사용자가 메시지 단계에 대해 설정된 [전달 유효성 검사]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations)를 충족하지 못했거나 [억제 목록]({{site.baseurl}}/user_guide/audience/suppression_lists)에 포함되어 있었습니다. **전달 유효성 검사** 설정에 따라 사용자가 Canvas를 종료했거나 다음 단계로 진행했을 수 있습니다. |
| 사용자 재자격 없음 | 사용자가 메시지를 받거나 Canvas에 진입할 자격이 있었지만, 재자격 또는 재진입 설정으로 인해 발송이 취소되었습니다. 이는 사용자가 이미 Campaign을 수신했거나 Canvas에 최근에 진입한 경우, 동일한 Campaign에 대한 다른 발송이 이미 해당 사용자에 대해 진행 중인 경우, 또는 재자격이나 재진입이 비활성화된 경우에 발생할 수 있습니다. |
| 고객 프로필을 찾을 수 없음 | 사용자가 존재한 적이 없거나 Braze에 더 이상 존재하지 않습니다. 일반적인 경우는 다음과 같습니다: {::nomarkdown}<ul><li> API 메시징을 사용하여 사용자를 타겟팅했지만, Braze에 존재한 적이 없는 경우. </li><li>메시지가 발송되거나 캔버스 단계가 실행되기 전에 사용자가 삭제된 경우. </li><li>메시지가 발송되기 전에 사용자가 다른 프로필과 병합된 경우.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사용자 자격 및 프로필" }

#### 채널 및 전달 {#channel-and-delivery}

| 중단 결과 | 설명 |
| ---- | ---- |
| 파트너 전달 시간 초과 | Braze가 24시간 동안 전달 파트너에게 이 메시지를 발송하려 했지만, 파트너가 전체 기간 동안 일시적 오류를 반환했습니다. |
| 푸시 자격 증명 유효하지 않음 | 이 앱의 [푸시 자격 증명]({{site.baseurl}}/user_guide/channels/push/faqs#valid-push-token)이 누락되었거나 유효하지 않아 발송이 취소되었습니다. **앱 설정**에서 자격 증명을 업데이트하세요. |
| 구독 그룹 실패 | 구독 그룹 또는 메시징 서비스 구성 문제로 인해 메시지를 발송할 수 없었습니다. 일반적인 이유로는 SMS 또는 WhatsApp의 발송 번호 누락, 또는 구성된 메시징 서비스에서 MMS가 지원되지 않는 경우가 있습니다. |
| 채널에 대한 사용자 자격 없음 | 사용자가 선택한 채널에서 이 메시지를 받을 자격이 없습니다. 일반적인 이유로는 채널 식별자 누락 또는 유효하지 않음, 유효한 푸시 토큰 없음, 구독 상태 제한, 지원되지 않는 채널 기능, 또는 전화 기반 채널의 차단된 국가 등이 있습니다. |
| 웹훅 실패 | 웹훅이 실패한 응답 코드(비`2xx`)를 수신했습니다. 자세한 내용은 [메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log#dev-console-troubleshooting)를 참조하세요. 60시간이 지난 로그는 정리되어 더 이상 접근할 수 없으며, 웹훅 오류는 시간당 최대 20개의 로그까지 샘플링됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="채널 및 전달" }

## 자주 묻는 질문 {#frequently-asked-questions}

### "사전 검사" 실패란 무엇인가요? {#what-does-a-pre-check-failure-mean}

"사전 검사"란 파이프라인 단계(예: 메시지 트리거 또는 Canvas 메시지 단계 발송)의 맨 처음에 실행되는 고속 번들 유효성 검사를 의미합니다. 최대 속도를 위해 설계된 조기 종료라고 생각하면 됩니다. 사용자 프로필의 모든 세부 사항을 검증하는 것과 같은 별도의 리소스 집약적 검사를 여러 번 실행하는 대신, Braze는 여러 기본 유효성 검사를 하나의 "첫 번째 패스"로 번들링합니다.

사용자가 이 단일 번들 검사에 실패하면 즉시 제외됩니다. 이 번들 접근 방식을 통해 Braze는 대량의 메시지를 고속으로 처리할 수 있으며, 각 메시지의 처리 지연 시간을 줄여 Campaigns과 Canvases의 더 빠르고 안정적인 성능에 기여할 수 있습니다.

### "기타" 중단 결과는 무엇을 의미하나요? {#what-does-an-other-abort-outcome-mean}

이는 기존 대시보드 카테고리에 해당하지 않는 중단입니다. "기타"로 표시된 중단 비율이 높은 경우, 추가 지원을 위해 [Braze 고객지원]({{site.baseurl}}/braze_support)에 문의하세요.

### _미발송_과 _발송됨_의 합이 예상 오디언스 크기보다 낮은 이유는 무엇인가요? {#why-is-the-sum-of-_not-sent_-and-_sent_-lower-than-my-expected-audience-size}

이는 여러 가지 이유로 발생할 수 있습니다:

- **오디언스 기준:** Campaign이나 Canvas가 시작되었을 때 예상보다 적은 수의 사용자가 오디언스 기준을 충족했을 수 있습니다(예: Segment에 포함되지 않았거나 필요한 속성이 없는 경우).
- **처리 진행 중:** 메시지가 아직 활발히 처리 중일 수 있습니다. 사용자가 아직 Canvas의 이전 단계에 있어 메시지 단계에 도달하지 않았을 수 있습니다.
- **데이터 최신성:** 대시보드 데이터는 약 15분마다 업데이트되지만, 이는 보장되지 않습니다. 이 Campaign이나 Canvas의 최신 데이터가 아직 대시보드에 반영되지 않았을 수 있습니다.
- **엣지 케이스:** 현재 이 대시보드에서 포착되지 않는 엣지 케이스가 발생했을 가능성이 적지만 있습니다. 이 경우가 의심되면 [Braze 고객지원]({{site.baseurl}}/user_guide/administer/personal/braze_support)에 문의하세요.

### _미발송_과 _발송됨_의 합이 Campaign 및 Canvas의 오디언스보다 큰 이유는 무엇인가요? {#why-is-the-sum-of-_not-sent_-and-_sent_-greater-than-the-audience-for-a-campaign-and-canvas}

이는 다음과 같은 이유로 발생할 수 있습니다:

- **다중 채널 메시지:** Campaign이나 캔버스 단계가 여러 채널(예: SMS 및 이메일)로 발송하도록 구성되었습니다. 한 명의 사용자가 한 채널(예: 이메일)에서는 "발송됨" 결과를, 다른 채널(예: "채널에 대한 사용자 자격 없음")에서는 "중단" 결과를 받을 수 있습니다. 이 경우 해당 사용자는 차트에서 두 번 계산됩니다: 한 번은 "발송됨"으로, 한 번은 "중단"으로.
  - **예시:** 100명의 사용자에게 iOS와 Android를 모두 타겟팅하는 푸시 Campaign을 발송합니다. 사용자가 iOS 기기만 가지고 있는 경우, iOS 푸시를 수신("발송됨")하지만 Android 푸시에 대해서도 중단이 트리거됩니다("채널에 대한 사용자 자격 없음").
- **다중 메시지 단계(Canvas만 해당):** Canvas의 특정 경로에 둘 이상의 메시지 단계가 있을 수 있습니다. 이 대시보드는 모든 결과를 집계하므로, 선택한 기간 내에 여러 메시지 단계를 통과한 경우 한 명의 사용자가 여러 번 계산될 수 있습니다.
- **테스트 메시지:** 테스트 발송(대시보드에서 계산됨)으로 인해 총 수가 오디언스 크기보다 높아질 수 있습니다.