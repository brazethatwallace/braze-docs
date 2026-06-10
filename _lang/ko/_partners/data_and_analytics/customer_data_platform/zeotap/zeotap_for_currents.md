---
nav_title: Zeotap for Currents
article_title: Zeotap for Currents
description: "이 참조 문서에서는 Braze Currents와 Zeotap 간의 파트너십에 대해 설명합니다. Zeotap은 ID 확인, 인사이트, 데이터 보강을 제공하여 모바일 오디언스를 발견하고 이해할 수 있도록 돕는 차세대 고객 데이터 플랫폼입니다."
page_type: partner
tool: Currents
search_tag: Partner
---

# Zeotap for Currents

> [Zeotap](https://zeotap.com/)은 ID 확인, 인사이트, 데이터 보강을 제공하여 모바일 오디언스를 발견하고 이해할 수 있도록 돕는 차세대 고객 데이터 플랫폼입니다.

Braze와 Zeotap 통합을 사용하면 Zeotap 고객 세그먼트를 Braze 고객 프로필에 동기화하여 Campaign의 규모와 도달 범위를 확장할 수 있습니다. [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)를 사용하면 데이터를 Zeotap에 연결하여 전체 성장 스택에서 활용할 수도 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| Zeotap 계정 | 이 파트너십을 활용하려면 [Zeotap 계정](https://zeotap.com/)이 필요합니다. |
| Currents | 데이터를 Zeotap으로 다시 내보내려면 계정에 [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)가 설정되어 있어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 구현 {#implementation}

### 1단계: Currents 소스 생성 {#step-1-create-a-currents-source}

1. Zeotap에서 **Integrate** 아래의 **Sources**로 이동합니다.
2. **Create Source**를 선택합니다.
3. 카테고리로 **Customer Engagement Channels**를 선택합니다.<br><br>!["Customer Engagement Channels"를 포함한 다양한 카테고리가 나열된 "Create Source" 창]({% image_buster /assets/img/zeotap/cec.png %}){: style="max-width:70%;"}<br><br>
4. 데이터 소스로 **Braze**를 선택합니다.
5. 소스 이름을 입력합니다.
6. 지역을 선택합니다.<br><br>![지역 및 데이터 엔티티를 선택할 수 있는 옵션이 있는 창]({% image_buster /assets/img/zeotap/select_region.png %}){: style="max-width:70%;"}<br><br>
7. **Create Source**를 선택합니다.
8. **Implementation Details** 탭으로 이동하여 **API URL**과 **Write Key**를 메모합니다.<br><br>![API URL과 Write Key가 포함된 Braze Currents 구현 세부 정보]({% image_buster /assets/img/zeotap/implementation_details.png %})

### 2단계: Currents에서 데이터 스트리밍 구성 {#step-2-configure-data-streaming-in-currents}

1. Braze에서 **파트너 통합** > **데이터 내보내기**로 이동합니다.
2. **Create New Current**을 선택한 다음 **Custom Currents Export**를 선택합니다.<br><br>!["Custom Currents Export"가 포함된 드롭다운이 있는 "Create New Current" 버튼]({% image_buster /assets/img/zeotap/custom_currents_export.png %}){: style="max-width:60%;"}<br><br>
3. 통합 이름과 통합에서 오류가 발생할 경우 연락받을 이메일을 입력합니다.
4. **Credentials** 아래에 [1단계](#step-1-create-a-currents-source)에서 메모한 다음 정보를 입력합니다:
- API URL을 **Endpoint**로 입력
- Write Key를 **Bearer Token**으로 입력<br><br>![통합 세부 정보 및 자격 증명을 입력하는 섹션]({% image_buster /assets/img/zeotap/credentials.png %})<br><br>
5. Zeotap으로 전송할 메시지 참여 이벤트를 선택합니다.<br><br>![메시지 참여 이벤트를 선택할 수 있는 섹션이 있는 "General Settings" 탭]({% image_buster /assets/img/zeotap/message_engagement_events.png %})
6. **Launch Current**을 선택하여 변경 사항을 저장하고 Zeotap으로 이벤트 전송을 시작합니다.

{% alert important %}
Currents 커넥터는 익명 사용자(`external_id`가 없는 사용자)를 지원하지 않습니다.
{% endalert %}