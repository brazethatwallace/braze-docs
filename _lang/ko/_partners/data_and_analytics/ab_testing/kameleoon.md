---
nav_title: Kameleoon
article_title: Kameleoon
description: "Kameleoon과 Braze를 통합하는 방법 알아보기"
alias: /partners/kameleoon/
page_type: partner
search_tag: Partner
---

# Kameleoon

>[Kameleoon](https://www.kameleoon.com)은 하나의 통합 플랫폼에서 실험, AI 기반 개인화 및 기능 관리 기능을 갖춘 최적화 솔루션입니다.

## 사전 요구 사항 {#prerequisites}

시작하기 전에 다음이 필요합니다:

| 요구 사항 | 설명 |
| --- | --- |
| Kameleoon 계정 | 이 파트너십을 활용하려면 Kameleoon 계정이 필요합니다.|
| Braze 계정 | 웹페이지에 [Braze 웹 SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)가 통합된 활성 Braze 계정이 필요합니다. 또한 이벤트 속성정보 세분화가 활성화되어 있어야 합니다. 요청하려면 [고려 사항](#considerations)을 참조하세요.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="사전 요구 사항" }

## 사용 사례 {#use-cases}

Kameleoon은 실험 및 개인화 Campaign에 참여하는 사용자를 식별하기 위해 Braze에 커스텀 이벤트를 전송하여, 보다 정밀한 타겟팅과 개인화된 메시징을 가능하게 합니다.

## Kameleoon 연동하기 {#integrating-kameleoon}

이 연동은 Kameleoon의 engine.js를 통해 JavaScript 트래커로 실행됩니다. Kameleoon 플랫폼 내에서 활성화할 수 있습니다.

### 1단계: Kameleoon 연동 페이지로 이동 {#step-1-go-to-the-kameleoon-integrations-page}

Kameleoon 앱에서 사이드바의 **Admin**을 선택한 다음 **Integrations**를 선택합니다.

![Kameleoon 플랫폼의 Admin 패널.]({% image_buster /assets/img/kameleoon/img_1.png %}){: style="max-width:70%;"}

### 2단계: Braze 도구 설치 {#step-2-install-the-braze-tool}

기본적으로 Braze 도구는 설치되어 있지 않습니다. Braze 아이콘을 찾은 다음 **Install the tool**을 선택합니다. ![아래쪽 화살표가 있는 회색 사각형.]({% image_buster /assets/img/kameleoon/img_2.png %})

Braze 도구를 활성화할 프로젝트를 선택하여 Kameleoon 데이터가 Braze로 올바르게 보고되도록 합니다.

![Kameleoon의 Braze 도구 아이콘.]({% image_buster /assets/img/kameleoon/img_3.png %})

도구 설정을 완료한 후 **Validate**를 선택하면 설정 패널이 닫힙니다. Braze 도구 아이콘 옆에 **ON** 토글이 나타나며, 도구가 설정된 프로젝트 수가 함께 표시됩니다.

![Kameleoon에서 'On'으로 토글된 Braze 도구.]({% image_buster /assets/img/kameleoon/img_4.png %})

### 3단계: Braze를 Kameleoon Campaign에 연결 {#step-3-associate-braze-with-kameleoon-campaigns}

#### 그래픽/코드 에디터에서 {#in-the-graphiccode-editor}

실험을 완료하려면 **Integrations** 단계를 선택하여 Braze를 추적 도구로 설정한 다음 **Braze**를 선택합니다.

![사용 가능한 모든 연동을 보여주는 Kameleoon의 Integrations 대시보드, 활성 연동인 Braze 포함.]({% image_buster /assets/img/kameleoon/img_5.png %})

라이브 전 요약에 Braze가 표시됩니다. Kameleoon이 자동으로 데이터를 Braze로 전송하며, Braze에서 직접 분석 및 세분화에 활용할 수 있습니다.

##### 개인화 생성 {#personalization-creation}

**Personalization Creation** 페이지에서 리포팅 도구 중 Braze를 선택하여 리포팅을 개인화할 수 있습니다.

![Heap, Mixpanel, Clarity 등의 연동을 보여주는 리포팅 도구 섹션, Braze가 선택된 상태.]({% image_buster /assets/img/kameleoon/img_6.png %})

##### 피처 플래그 생성 {#feature-flag-creation}

피처 플래그 환경의 **Integrations** 섹션에서 연동을 설정합니다. 활성화하려는 환경에서 이를 활성화합니다.

![사용 가능한 연동이 있는 Kameleoon의 Feature Flag 페이지. 각 파트너에 대해 'Delivery rules'와 'Feature experiments' 두 개의 스위치가 있습니다.]({% image_buster /assets/img/kameleoon/img_7.png %})

##### 결과 페이지 {#results-page}

Braze가 실험의 리포팅 도구로 설정된 후, Kameleoon 결과 페이지의 **Experiment configuration** 메뉴에서 이를 선택하거나 선택 해제할 수 있습니다.

{% alert note %}
이 연동은 [하이브리드 구현](https://developers.braze-presentation.preview.kameleoon.net/core-concepts/hybrid-experimentation?language=en#sending-exposure-events-to-third-party-analytics)이 필요하며 웹 SDK에서만 호환됩니다.
{% endalert %}

![Kameleoon 결과 페이지의 사이드 패널.]({% image_buster /assets/img/kameleoon/img_8.png %}){: style="max-width:50%;" }

실험에 연결된 리포팅 도구가 표시됩니다. 이 선택을 편집하려면 **Edit**를 선택합니다.

### 4단계: Braze에서 Kameleoon 데이터 분석 및 활용 {#step-4-analyze-and-leverage-your-kameleoon-data-in-braze}

연동이 설정되면 Kameleoon은 **Experiment name**, **Experiment ID**, **Variation name**, **Variation ID** 등의 속성정보를 포함한 `kameleoon_exposure`라는 커스텀 이벤트를 Braze로 전송합니다.

![Kameleoon에서 Braze로 수신된 이벤트의 예시 페이로드를 보여주는 Braze의 커스텀 이벤트 사용자 로그.]({% image_buster /assets/img/kameleoon/img_9.png %})

그런 다음 커스텀 이벤트에서 이 데이터를 확인하고, 커스텀 이벤트 보고서를 생성하여 Kameleoon Campaign 노출을 식별하며, 이벤트 속성정보를 기반으로 세분화를 활성화할 수 있습니다. [행동 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths#action-groups), [액션 기반 트리거]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) 또는 [Segments 생성]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)을 통해 후속 또는 연결된 Campaigns 및 Canvases를 생성할 때 커스텀 이벤트를 사용할 수 있습니다.

또한 이러한 이벤트는 [Currents 커스텀 이벤트 오브젝트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)를 통해 접근할 수 있어 포괄적인 리포팅과 분석이 가능합니다.

## 고려 사항 {#considerations}

### 이벤트 속성정보 세분화 요청 {#request-event-property-segmentation}

이벤트 속성정보 세분화를 사용하려면 먼저 Braze에서 해당 기능을 활성화해야 합니다. 아래 템플릿을 사용하여 Braze 고객 성공 매니저 또는 지원팀에 액세스를 요청하세요.

   <table aria-label="이벤트 속성정보 세분화 요청">
     <caption>이벤트 속성정보 세분화 요청</caption>
   <thead>
      <tr>
         <th>필드</th>
         <th>세부 정보</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td><strong>제목</strong></td>
         <td>Request to Enable Event Property Segmentation for Kameleoon Integration</td>
      </tr>
      <tr>
         <td><strong>본문</strong></td>
         <td>
         Hello Braze Team,<br><br>
         We would like to enable event property segmentation for events sent from our Kameleoon&lt;&gt;Braze integration. Here are the details:<br><br>
         - <strong>Event Name:</strong> Kameleoon<br>
         - <strong>Event Properties:</strong> <code>kameleoon_campaign_name</code>, <code>kameleoon_variation_name</code><br><br>
         Please confirm once the properties have been enabled in our account.<br><br>
         Thank you.
         </td>
      </tr>
   </tbody>
   </table>
   {: .reset-td-br-1 .reset-td-br-2 aria-label="이벤트 속성정보 세분화 요청" }

### Braze 데이터 포인트 {#braze-data-points}

Kameleoon에서 Braze로 전송되는 커스텀 이벤트는&#8212;세분화를 위해 활성화된 이벤트 속성정보를 포함하여&#8212;Braze 인스턴스에서 데이터 포인트를 기록합니다.