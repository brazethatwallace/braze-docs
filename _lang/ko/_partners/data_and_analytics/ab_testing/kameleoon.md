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

## 필수 조건 {#prerequisites}

시작하기 전에 다음이 필요합니다:

| 요구 사항 | 설명 |
| --- | --- |
| Kameleoon 계정 | 이 파트너십을 이용하려면 Kameleoon 계정이 필요합니다.|
| Braze 계정 | 웹페이지에 [Braze Web SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)가 통합된 활성 Braze 계정이 필요합니다. 또한 이벤트 속성정보 세분화를 활성화해야 합니다. 요청하려면 [고려 사항](#considerations)을 참조하세요.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 활용 사례 {#use-cases}

Kameleoon은 실험 및 개인화 Campaign(캠페인)에 참여하는 사용자를 식별하기 위해 커스텀 이벤트를 Braze에 전송하여 보다 정확한 타겟팅과 개인화된 메시징을 가능하게 합니다.

## Kameleoon 통합하기 {#integrating-kameleoon}

이 통합은 Kameleoon의 engine.js를 통해 JavaScript 트래커로 실행됩니다. Kameleoon 플랫폼 내에서 빠르게 활성화할 수 있습니다.

### 1단계: Kameleoon 통합 페이지로 이동하기 {#step-1-go-to-the-kameleoon-integrations-page}

Kameleoon 앱의 사이드바에서 **Admin**을 선택한 다음 **Integrations**를 선택합니다.

![Kameleoon 플랫폼의 관리자 패널.]({% image_buster /assets/img/kameleoon/img_1.png %}){: style="max-width:70%;"}

### 2단계: Braze 도구 설치하기 {#step-2-install-the-braze-tool}

기본적으로 Braze 도구는 설치되어 있지 않습니다. Braze 아이콘을 찾은 다음 **Install the tool**을 선택합니다. ![아래쪽을 가리키는 화살표가 있는 회색 사각형.]({% image_buster /assets/img/kameleoon/img_2.png %})

Braze 도구를 활성화할 프로젝트를 선택하면 Kameleoon 데이터가 Braze에 올바르게 보고됩니다.

![Kameleoon의 Braze 도구 아이콘.]({% image_buster /assets/img/kameleoon/img_3.png %})

도구를 구성한 후 **Validate**를 선택하면 구성 패널이 닫힙니다. 그러면 도구가 구성된 프로젝트 수와 함께 Braze 도구 아이콘 옆에 **ON** 토글이 표시됩니다.

![Kameleoon에서 Braze 도구가 "On"으로 토글된 모습.]({% image_buster /assets/img/kameleoon/img_4.png %})

{% alert important %}
이 기능은 베타 버전입니다. [Kameleoon 베타 프로그램](https://help.kameleoon.com/account-and-team-management/join-beta-program/)에 가입하여 이 통합 기능을 사용해 보세요.
{% endalert %}

### 3단계: Braze와 Kameleoon 캠페인 연계하기 {#step-3-associate-braze-with-kameleoon-campaigns}

#### 그래픽/코드 편집기에서 {#in-the-graphiccode-editor}

실험을 완료하려면 **Integrations** 단계를 선택하여 추적 도구로 Braze를 구성한 다음 **Braze**를 선택합니다.

![Kameleoon의 통합 대시보드에 활성 통합인 Braze를 포함하여 사용 가능한 모든 통합이 표시됩니다.]({% image_buster /assets/img/kameleoon/img_5.png %})

Braze는 라이브 시작 전 요약에 언급됩니다. Kameleoon은 자동으로 데이터를 Braze로 전송하며, Braze에서 바로 분석 및 세분화에 사용할 수 있습니다.

##### 개인화 생성 {#personalization-creation}

**Personalization Creation** 페이지에서 리포팅 도구 중 Braze를 선택하여 리포팅을 개인화할 수 있습니다.

![보고 도구 섹션에 Braze가 선택된 상태에서 Heap, Mixpanel, Clarity와 같은 통합이 표시됩니다.]({% image_buster /assets/img/kameleoon/img_6.png %})

##### 피처 플래그 생성 {#feature-flag-creation}

**Integrations** 섹션의 피처 플래그 환경에서 통합을 설정합니다. 활성화하려는 환경에 맞게 활성화하세요.

![Kameleoon의 피처 플래그 페이지와 사용 가능한 통합. 각 파트너에 대해 "Delivery rules"와 "Feature experiments"라는 두 가지 스위치가 있습니다.]({% image_buster /assets/img/kameleoon/img_7.png %})

##### 결과 페이지 {#results-page}

실험의 보고 도구로 Braze를 설정한 후에는 **Experiment configuration** 메뉴의 Kameleoon 결과 페이지에서 이를 선택(또는 선택 해제)할 수 있습니다.

{% alert note %}
이 통합은 [하이브리드 구현](https://developers.braze-presentation.preview.kameleoon.net/core-concepts/hybrid-experimentation?language=en#sending-exposure-events-to-third-party-analytics)이 필요하며 웹 SDK와만 호환됩니다.
{% endalert %}

![Kameleoon의 결과 페이지 측면 패널.]({% image_buster /assets/img/kameleoon/img_8.png %}){: style="max-width:50%;" }

실험과 관련된 보고 도구가 표시됩니다. **Edit**를 선택하여 이 선택 항목을 편집합니다.

### 4단계: Braze에서 Kameleoon 데이터 분석 및 활용하기 {#step-4-analyze-and-leverage-your-kameleoon-data-in-braze}

통합이 설정되면 Kameleoon은 **Experiment name**, **Experiment ID**, **Variation name**, **Variation ID**와 같은 속성정보가 포함된 `kameleoon_exposure`라는 커스텀 이벤트를 Braze에 전송합니다.

![Braze의 커스텀 이벤트 사용자 로그로, Kameleoon에서 Braze가 수신한 이벤트의 페이로드 예시를 보여줍니다.]({% image_buster /assets/img/kameleoon/img_9.png %})

그런 다음 커스텀 이벤트에서 이 데이터를 확인하고, 커스텀 이벤트 보고서를 생성하여 Kameleoon 캠페인 노출을 식별하고, 이벤트 속성정보를 기반으로 세분화를 활성화할 수 있습니다. [행동 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/#action-groups), [행동 기반 트리거]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/)를 통해 후속 또는 연결된 Campaigns 및 Canvases를 만들거나 [Segments]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/)를 생성할 때 커스텀 이벤트를 사용할 수 있습니다.

또한 이러한 이벤트는 [Currents 커스텀 이벤트 오브젝트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)를 통해 액세스할 수 있어 종합적인 보고 및 분석이 가능합니다.

## 고려 사항 {#considerations}

### 이벤트 속성정보 세분화 요청하기 {#request-event-property-segmentation}

이벤트 속성정보 세분화를 사용하려면 먼저 Braze에서 활성화해야 합니다. 다음 템플릿을 사용하여 Braze 고객 성공 매니저 또는 고객지원 팀에 연락하여 액세스를 요청하세요.

   <table aria-label="Request event property segmentation">
     <caption>Request event property segmentation</caption>
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
   {: .reset-td-br-1 .reset-td-br-2 aria-label="Request event property segmentation" }

### Braze 데이터 포인트 {#braze-data-points}

세분화를 위해 활성화된 이벤트 속성정보를 포함하여 Kameleoon에서 Braze로 전송된 커스텀 이벤트는 Braze 인스턴스에 데이터 포인트를 기록합니다.