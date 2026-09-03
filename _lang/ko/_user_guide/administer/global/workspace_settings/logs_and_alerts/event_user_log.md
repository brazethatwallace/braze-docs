---
nav_title: 이벤트 사용자 로그
article_title: 이벤트 사용자 로그
page_order: 1
page_type: reference
description: "이 참조 문서에서는 Braze 통합의 문제를 디버깅하거나 해결하는 데 도움이 되는 이벤트 사용자 로그에 대해 설명합니다."

---

# 이벤트 사용자 로그 {#event-user-log}

> 이벤트 사용자 로그는 Braze 통합에서 발생하는 문제를 분석, 디버깅 또는 해결하는 데 도움을 줍니다. 이 탭에서는 오류 유형, 관련 앱, 발생 시점 등의 세부 정보가 포함된 오류 로그를 확인할 수 있으며, 관련 원시 데이터를 직접 확인할 수 있는 기회도 많습니다.

{% alert tip %}
이 문서 외에도 이벤트 사용자 로그를 사용하여 직접 문제 해결 및 디버깅을 수행하는 방법을 다루는 [품질 보증 및 디버깅 툴](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/) Braze 학습 과정도 확인해 보시기 바랍니다.
{% endalert %}

로그에 액세스하려면 **설정** > **설정 및 테스트** > **이벤트 사용자 로그**로 이동합니다.

로그를 쉽게 찾으려면 다음 기준으로 필터링할 수 있습니다:

* SDK 또는 API
* 앱 이름
* 기간
* 사용자

각 로그는 여러 섹션으로 나뉘며, 다음 항목이 포함될 수 있습니다:

* 기기 속성
* 사용자 속성
* 이벤트
* Campaign 이벤트
* 응답 데이터

**데이터 확장** 아이콘을 선택하면 해당 로그의 원시 JSON 데이터를 확인할 수 있습니다.

![특정 로그 옆에 있는 데이터 확장 아이콘]({% image_buster /assets/img_archive/expand_data.png %})

이벤트 사용자 로그는 기록된 후 30일 동안 대시보드에 보관됩니다.

![이벤트의 원시 로그]({% image_buster /assets/img_archive/rawlogs.png %}){: style="max-width:60%;"}

## 문제 해결 {#troubleshooting}

### 테스트 사용자의 SDK 로그 누락 {#missing-sdk-logs-for-test-users}

내부 그룹에 사용자를 추가했지만 이벤트 사용자 로그에 SDK 로그가 표시되지 않는 경우, 구성 옵션이 누락되었을 수 있습니다. SDK 로그를 캡처하려면 해당 [내부 그룹]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups)의 **내부 그룹 설정**에서 **그룹 멤버의 사용자 이벤트 기록**을 선택해야 합니다.

### 로그 업데이트 지연 {#delay-in-logs-updates}

이 지연은 일반적으로 정상적인 API 처리 로드로 인해 발생합니다.

SDK 메서드를 호출하면 일반적으로 SDK가 해당 이벤트를 로컬에 캐시한 후 10초마다 서버로 플러시합니다. 작업 처리 대기줄이 이벤트를 수집하는 데 해당 시점의 전체 로드에 따라 1초에서 몇 분까지 걸릴 수 있습니다.

이벤트가 가능한 한 빨리 도착하도록 하려면 `requestImmediateDataFlush()` 함수를 호출해 보세요.

### 인앱 메시지 노출 실패 {#in-app-message-impression-failures}

인앱 메시지가 표시되지 않는 경우, 이벤트 사용자 로그에서 관련 SDK 요청의 원시 JSON 데이터를 확장하고 응답에서 `error_code` 필드를 확인하여 원인을 찾을 수 있습니다. `error_code`는 노출이 실패한 구체적인 이유(예: 잘못된 색상 값 또는 렌더링 문제)를 식별합니다. 추가 조사가 필요한 경우 이 오류 코드를 [Braze 지원팀]({{site.baseurl}}/braze_support)에 공유하세요.

### 세션 종료와 세션 시작의 타임스탬프가 유사한 경우 (iOS) {#session-end-and-session-start-have-similar-timestamps-ios}

이벤트 사용자 로그에는 Braze가 세션 종료 알림을 받은 타임스탬프가 표시되며, 이는 다음 세션이 시작되기 밀리초 전입니다. iOS는 앱이 백그라운드에 있을 때 스레드 실행을 적극적으로 중단하기 때문에, 앱이 다시 열릴 때까지 Braze로 데이터를 플러시할 수 없어 세션이 종료되었는지 알 수 없습니다.

세션 종료 시간이 세션 시작보다 몇 초 전으로 표시되지만, 이벤트가 플러시될 때 세션 지속 시간은 별도로 플러시되며 앱이 열려 있던 시간을 정확하게 반영합니다. 따라서 이 동작은 `Median Session Duration` 필터에 영향을 미치지 않습니다.

사용자 세션과 관련하여 Braze를 사용해 다음과 같은 데이터를 모니터링할 수 있습니다:

- 사용자의 세션 횟수
- 사용자가 마지막으로 세션을 시작한 시점
- Campaign을 수신한 후 사용자가 세션을 시작했는지 여부
- 사용자의 중간값 세션 지속 시간

이러한 동작은 세션 종료 이벤트가 다음 세션에서 플러시되는 것에 의해 영향을 받지 않습니다.