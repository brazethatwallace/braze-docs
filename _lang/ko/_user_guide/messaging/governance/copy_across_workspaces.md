---
nav_title: 워크스페이스 간 복사
article_title: 워크스페이스 간 복사
page_order: 3
alias: "/copying_to_workspaces/"
page_type: reference
description: "이 참조 문서에서는 Campaign과 Canvases를 다른 워크스페이스로 복사하는 방법에 대한 개요를 제공합니다."
tool:
    - Campaigns
    - Canvas
---

# 워크스페이스 간 Campaign 및 Canvases 복사 {#copy-campaigns-and-canvases-across-workspaces}

> 워크스페이스 간 Campaign 복사를 사용하면 다른 워크스페이스에 있는 Campaign의 사본으로 시작하여 메시지 작성을 빠르게 시작할 수 있습니다. 이 페이지에서는 Campaign을 다른 워크스페이스로 복사하는 방법과 복사되는 항목 및 복사되지 않는 항목을 설명합니다.

Campaign 또는 Canvas를 다른 워크스페이스로 복사하면 편집하고 시작할 때까지 초안 상태로 유지되므로, 성공적인 메시징 전략을 유지하고 이를 기반으로 발전시킬 수 있습니다.

{% tabs local %}
{% tab campaigns %}

{% alert important %}
워크스페이스 간 Campaign 복사는 일반적으로 사용할 수 있습니다. Content Cards에 대한 채널 지원은 현재 제공되지 않습니다.
{% endalert %}

SMS, 인앱 메시지, 푸시 알림, 이메일, 웹훅 등 지원되는 채널에 대해 워크스페이스 간 Campaign을 복사할 수 있습니다. 이메일 템플릿, 기능 플래그, Content Blocks도 복사할 수 있습니다. 지원되지 않는 채널이 포함된 멀티채널 캠페인은 다른 워크스페이스로 복사할 수 없습니다.

Campaign을 다른 워크스페이스로 복사하려면:

1. 선택한 Campaign 옆의 <i class="fas fa-cog"></i> 톱니바퀴 아이콘을 선택합니다.
2. **워크스페이스에 복사**를 선택합니다.
3. 복사 후 Campaign을 검토하고 테스트하여 모든 필드가 올바르게 작동하는지 확인합니다.

{% endtab %}
{% tab canvas %}

{% alert important %}
워크스페이스 간 Canvases 복사는 일반적으로 사용할 수 있습니다. LINE, Content Cards, WhatsApp 채널은 현재 지원되지 않습니다.
{% endalert %}

이메일, 인앱 메시지, 푸시, 웹훅, SMS 등 지원되는 채널에 대해 워크스페이스 간 Canvases를 복사할 수 있습니다.

Canvas를 다른 워크스페이스로 복사하려면:

1. 선택한 Canvas 옆의 <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;메뉴를 선택합니다.
2. **워크스페이스에 복사**를 선택합니다.
3. 복사 후 Canvas를 검토하고 테스트하여 모든 필드가 올바르게 작동하는지 확인합니다.

오디언스 동기화 단계가 포함된 Canvas를 복사할 때 설정은 대상 워크스페이스로 복사되지 않지만, 여정의 단계는 복사됩니다.

{% endtab %}
{% endtabs %}

## 워크스페이스 간 복사되는 항목 {#whats-copied-across-workspaces}

다음은 워크스페이스 간에 복사되는 항목과 생략되는 항목의 전체 목록이 아닙니다. 모범 사례로서 Campaign 및 Canvas 세부 정보를 확인하고 테스트하여 메시지가 예상대로 작동하는지 확인하세요.

### 세부 정보 {#details}

{% tabs local %}
{% tab campaigns %}

| 복사됨 | 생략됨 |
|---|---|
| 설명 | 지역 |
| 유형 | 태그 |
| 동작(중첩) | Segments 및 필터 |
| 전환 동작(중첩) | [승인]({{site.baseurl}}/user_guide/messaging/governance/approvals/) |
| 방해 금지 시간 구성 | 트리거 스케줄 |
| 최대 게재빈도 설정 구성 | Campaign 요약 |
| 수신자 구독 상태 |  |
| 반복 스케줄 |  |
| 트랜잭션 여부 |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Details" }

{% endtab %}
{% tab canvas %}

| 복사됨 | 생략됨 |
|---|---|
| 설명 | 지역 |
| 유형 | 태그 |
| 동작(중첩) | Segments 및 필터 |
| 전환 동작(중첩) | [승인]({{site.baseurl}}/user_guide/messaging/governance/approvals/) |
| 방해 금지 시간 구성 | 트리거 스케줄 |
| 최대 게재빈도 설정 구성 | Canvas 요약 |
| 수신자 구독 상태 |  |
| 반복 스케줄 | 종료 기준 |
| 트랜잭션 여부 |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Details" }

캔버스 단계의 필터 기준(예: [결정 분할]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/) 단계)은 대상 워크스페이스로 복사되지 않습니다. 복사 후 해당 필터를 다시 구성하세요.

{% endtab %}
{% endtabs %}

### 전환 동작 {#conversion-behaviors}

{% tabs local %}
{% tab campaigns %}

| 복사됨 | 생략됨 |
|---|---|
| 유형 동작 | 워크스페이스 ID |
| Campaign 상호작용 | Campaign ID |
| 커스텀 이벤트 이름 |  |
| 제품 이름 |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conversion behaviors" }

{% endtab %}
{% tab canvas %}

| 복사됨 | 생략됨 |
|---|---|
| 유형 동작 | 워크스페이스 ID |
| Canvas 상호작용 | Canvas ID |
| 커스텀 이벤트 이름 |  |
| 제품 이름 |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conversion behaviors" }

{% endtab %}
{% endtabs %}

### 동작 {#actions}

{% tabs local %}
{% tab campaigns %}

| 복사됨 | 생략됨 |
|---|---|
| 유형 동작 | 워크스페이스 ID |
| Campaign 상호작용 | Campaign ID |
| 커스텀 이벤트 이름 |  |
| 제품 이름 |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Actions" }

{% endtab %}
{% tab canvas %}

| 복사됨 | 생략됨 |
|---|---|
| 유형 동작 | 워크스페이스 ID |
| Canvas 상호작용 | Canvas ID |
| 커스텀 이벤트 이름 |  |
| 제품 이름 |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Actions" }

{% endtab %}
{% endtabs %}

### 메시지 변형 {#message-variations}

{% tabs local %}
{% tab campaigns %}

| 복사됨 | 생략됨 |
|---|---|
| 발송 비율 | API ID |
| 유형 |  시드 그룹 ID |
|  |  링크 템플릿 ID |
|  |  내부 사용자 그룹 ID |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Message variations" }

{% endtab %}
{% tab canvas %}

| 복사됨 | 생략됨 |
|---|---|
| 발송 비율 | API ID |
| 유형 |  시드 그룹 ID |
|  |  링크 템플릿 ID |
|  |  내부 사용자 그룹 ID |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Message variations" }

{% endtab %}
{% endtabs %}


### 이메일 메시지 변형 {#email-message-variation}

{% tabs local %}
{% tab campaigns %}

| 복사됨 | 생략됨 |
|---|---|
| 이메일 본문 | 발신 주소 |
| 메시지 추가 항목 |  회신 대상 |
| 제목 |  BCC |
| 제목줄 |  링크 템플릿 |
|  |  링크 별칭 지정 |
|  | 번역 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email message variation" }

{% endtab %}
{% tab canvas %}

| 복사됨 | 생략됨 |
|---|---|
| 이메일 본문 | 발신 주소 |
| 메시지 추가 항목 |  회신 대상 |
| 제목 |  BCC |
| 제목줄 |  링크 템플릿 |
|  |  링크 별칭 지정 |
|  | 번역 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email message variation" }

{% endtab %}
{% endtabs %}

### 이메일 본문 {#email-body}

{% tabs local %}
{% tab campaigns %}

| 복사됨 | 생략됨 |
|---|---|
| 일반 텍스트 | 링크 별칭 지정 |
| HTML 및 드래그 앤 드롭 콘텐츠 | 번역 |
| 프리헤더 |  |
| 인라인 CSS |  |
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email body" }

{% endtab %}
{% tab canvas %}

| 복사됨 | 생략됨 |
|---|---|
| 일반 텍스트 | 링크 별칭 지정 |
| HTML 및 드래그 앤 드롭 콘텐츠 | 번역 |
| 프리헤더 |  |
| 인라인 CSS |  |
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email body" }

{% endtab %}
{% endtabs %}

### 이메일 템플릿 {#email-templates}

{% tabs local %}
{% tab campaigns %}

| 복사됨 | 생략됨 |
|---|---|
| 이메일 본문 | API ID |
| 설명 | 이미지 ID |
| 제목줄 | 지역 |
| 헤더 | 태그 |
| | 번역 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email templates" }

{% endtab %}
{% tab canvas %}

| 복사됨 | 생략됨 |
|---|---|
| 이메일 본문 | API ID |
| 설명 | 이미지 ID |
| 제목줄 | 지역 |
| 헤더 | 태그 |
| | 번역 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email templates" }

{% endtab %}
{% endtabs %}

### Content Blocks

{% tabs local %}
{% tab campaigns %}

| 복사됨 | 생략됨 |
|---|---|
| 이름 | 링크 별칭 지정 |
| 설명 | API 키 |
| 콘텐츠 | 지역 |
| HTML 및 드래그 앤 드롭 콘텐츠 | 태그 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Blocks" }

{% endtab %}
{% tab canvas %}

| 복사됨 | 생략됨 |
|---|---|
| 이름 | 링크 별칭 지정 |
| 설명 | API 키 |
| 콘텐츠 | 지역 |
| HTML 및 드래그 앤 드롭 콘텐츠 | 태그 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Blocks" }

{% endtab %}
{% endtabs %}

### SMS 메시지 변형 {#sms-message-variation}

{% tabs local %}
{% tab campaigns %}

| 복사됨 | 생략됨 |
|---|---|
| 본문 | 메시징 서비스 |
| 링크 단축 | VCF 미디어 항목 |
| 클릭 추적 |  |
| 미디어 항목 |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMS message variation" }

{% endtab %}
{% tab canvas %}

| 복사됨 | 생략됨 |
|---|---|
| 본문 | 메시징 서비스 |
| 링크 단축 | VCF 미디어 항목 |
| 클릭 추적 |  |
| 미디어 항목 |  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMS message variation" }

{% endtab %}
{% endtabs %}

## Liquid가 포함된 메시지 복사 {#copying-messages-that-contain-liquid}

메시지 본문 내의 Liquid 참조는 대상 워크스페이스로 복사되지만, 참조가 예상대로 작동하지 않을 수 있습니다. 즉, 워크스페이스 A의 Canvas를 워크스페이스 B로 복사하면 워크스페이스 B에서 Liquid 참조를 포함한 워크스페이스 A의 세부 정보를 참조할 수 없습니다. 예를 들어, 트리거 동작, 오디언스 필터, [결정 분할]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/) 필터 기준과 같은 필드는 복사되지 않습니다.

워크스페이스 간 Campaign 및 Canvases를 복사할 때 종속성이 있는 다음 Liquid 참조를 추적하세요:

- 카탈로그 항목 태그
- 연결된 콘텐츠 태그
- Content Blocks
- 커스텀 속성
- 환경설정 센터
- 제품 추천
- 구독 상태 태그
- 바우처 및 프로모션 태그

## 피처 플래그가 포함된 메시지 복사 {#copying-messages-with-feature-flags}

피처 플래그 Campaign과 피처 플래그 단계가 포함된 Canvas를 워크스페이스 간에 복사하려면, 대상 워크스페이스에 원본 Campaign에서 참조하는 피처 플래그 또는 원본 Canvas에서 참조하는 피처 플래그 단계와 일치하는 ID로 구성된 [피처 플래그 실험]({{site.baseurl}}/developer_guide/feature_flags/experiments/)이 있어야 합니다.

대상 워크스페이스에 존재하지 않는 피처 플래그 ID가 포함된 피처 플래그 단계가 있는 Campaign 또는 Canvas를 복사하면, 피처 플래그 단계는 복사되지만 그 내용은 복사되지 않습니다.

## Content Blocks가 포함된 메시지 복사 {#copying-messages-with-content-blocks}

워크스페이스 간 Campaign을 복사할 때 Content Blocks는 복사되지 않습니다. 그러나 동일한 이름의 블록이 대상 워크스페이스에 존재하면 해당 Content Block을 참조할 수 있습니다. 또는 Campaign 시작 시 오류를 방지하기 위해 대상 워크스페이스에 Content Block(또는 이러한 Liquid 참조)을 생성할 수 있습니다.

Content Block을 참조하는 Canvases의 경우, Content Block을 먼저 대상 워크스페이스에 복사해야 합니다.