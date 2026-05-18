---
nav_title: Eagle Eye
article_title: Eagle Eye
description: Eagle Eye를 Braze와 통합하는 방법을 알아보세요.
alias: /partners/eagle_eye/
page_type: partner
search_tag: Partner
---

# Eagle Eye

> [Eagle Eye](https://eagleeye.com/)는 리테일, 여행 및 호스피탈리티 브랜드가 실시간, 옴니채널, 개인화된 소비자 마케팅 활동을 대규모로 지원하여 최종 고객의 로열티를 확보할 수 있도록 하는 선도적인 SaaS 및 AI 기술 회사입니다.

_이 통합은 Eagle Eye에서 유지 관리합니다._

## 개요 {#overview}

Eagle Eye Connect는 Braze와 AIR 간의 양방향 통합으로, 브랜드가 로열티 및 프로모션 데이터를 Braze에서 직접 활성화할 수 있도록 합니다. 클라이언트는 AIR에서 오디언스에 진입하는 소비자에게 보상을 발급할 수 있습니다. 이를 통해 마케터는 포인트 잔액, 프로모션, 보상 활동 등의 실시간 데이터를 사용하여 고객 참여를 개인화할 수 있습니다.

## 활용 사례 {#use-cases}

- 포인트 임계값이나 보상 획득과 같은 로열티 이벤트를 기반으로 Braze Campaign을 트리거합니다.
- 실시간 로열티 데이터로 Braze 고객 프로필을 강화하여 더욱 개인화된 타겟팅을 가능하게 합니다.
- 보상 사용과 연계된 캠페인 효과를 추적하고 보고합니다.
- 사용자가 Braze에서 Campaign에 진입할 때 AIR에서 보상을 발급합니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|--------------------------|-------------|
| Eagle Eye AIR 계정 | 이 파트너십을 활용하려면 활성 Eagle Eye AIR 계정이 필요합니다. 시작하려면 [partnerships@eagleeye.com](mailto:partnerships@eagleeye.com)으로 Eagle Eye 파트너십 팀에 문의하세요. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br>Braze 대시보드의 **설정 > API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL](https://www.braze.com/docs/api/basics/#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 아웃바운드 vs. 인바운드 {#outbound-vs-inbound}

다음 표는 Braze와 Eagle Eye AIR 간에 지원되는 두 가지 유형의 통합을 설명합니다. Eagle Eye Connect는 AIR과 Braze와 같은 파트너 시스템 간의 데이터 교환을 가능하게 하는 미들웨어입니다. 자세한 내용은 [Eagle Eye의 Braze 설명서](https://developer.eagleeye.com/docs/braze)를 참조하세요.

{% tabs local %}
{% tab 아웃바운드 %}
<table aria-label="Outbound vs. inbound">
  <caption>Outbound vs. inbound</caption>
  <thead>
    <tr>
      <th>방향</th>
      <th>시작 주체</th>
      <th>데이터 흐름</th>
      <th>목적</th>
      <th>예시</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Eagle Eye → Braze</td>
      <td>Eagle Eye</td>
      <td>Braze API로</td>
      <td>
        커스텀 이벤트를 통해 로열티 데이터를 커스텀 속성으로 Braze 고객 프로필에 전송합니다. Braze 내에서 수집된 데이터는 다음과 같이 사용할 수 있습니다:
        <ul>
          <li>사용자 세그먼트 분류, Campaign 트리거</li>
          <li>메시지 개인화</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>로열티 포인트 또는 등급 상태를 Braze로 전송 (<code>ee_loyalty.points.current</code>, <code>ee_loyalty.tier.tierId</code>)</li>
          <li>사용자가 쿠폰을 수신하거나 사용할 때 프로필 업데이트</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Outbound vs. inbound" }
{% endtab %}

{% tab 인바운드 %}
<table aria-label="Outbound vs. inbound">
  <caption>Outbound vs. inbound</caption>
  <thead>
    <tr>
      <th>방향</th>
      <th>시작 주체</th>
      <th>데이터 흐름</th>
      <th>목적</th>
      <th>예시</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Braze → Eagle Eye</td>
      <td>Braze</td>
      <td>웹훅을 통해 Eagle Eye API로</td>
      <td>
        소비자가 어떤 소스에서든 Braze의 오디언스에 진입하면, Braze는 EE Connect로 웹훅을 트리거하여 EE가 보상(쿠폰 또는 포인트)을 발급할 수 있도록 합니다.<br><br>
        AIR에서 동작이 완료되면, Braze는 AIR로부터 아웃바운드 이벤트를 수신합니다.
      </td>
      <td>
        <ul>
          <li>로열티 프로그램 가입 시 소비자에게 보상(쿠폰 또는 포인트)이 발급됩니다</li>
          <li>배송 지연이 발생한 소비자에게 보상이 발급됩니다</li>
          <li>생일 보상</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Outbound vs. inbound" }
{% endtab %}
{% endtabs %}

{% alert tip %}
커스텀 속성 또는 이벤트로 Braze에 전송할 수 있는 커스텀 데이터에 대해 자세히 알아보려면 [Eagle Eye의 Braze 설명서](https://developer.eagleeye.com/docs/braze#data-model)를 참조하세요.
{% endalert %}

## 통합 개요 {#integration-overview}

현재 인바운드 및 아웃바운드 커넥터는 Eagle Eye 팀의 직접 지원을 통해 API로만 설정할 수 있습니다. 하지만 AIR 대시보드 내 셀프 서비스 옵션이 곧 제공될 예정입니다!

Eagle Eye 팀과 협력하여 다음 단계를 완료하게 됩니다:

### 1단계: 구성 세부 정보 제공 {#step-1-provide-configuration-details}

먼저 다음 세부 정보를 Eagle Eye 팀에 제공합니다:

| 제공 항목 | 설명 |
|------------------------|-------------|
| Braze API 자격 증명 | Braze REST 엔드포인트, 앱 식별자 및 API 키를 Eagle Eye 담당자에게 안전하게 공유합니다. |
| 식별자 매칭 | AIR과 Braze에서 공통으로 사용되는 프로필 업데이트용 기본 사용자 식별자(예: 외부 ID 또는 이메일)를 결정하고 공유합니다. |
| 인증 키 | 각 인바운드 및 아웃바운드 커넥터에 대한 비밀 인증 키를 결정하고 공유합니다. |
| 통화 코드 | 금전적 구매 금액을 표시하기 위한 3자리 통화 코드를 공유합니다(예: USD). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 1: Provide configuration details" }

### 2단계: Eagle Eye Connect 구성 {#step-2-configure-eagle-eye-connect}

Eagle Eye 팀이 제공된 세부 정보와 함께 고유한 AIR API 자격 증명 및 커넥터용 아웃바운드 이벤트를 사용하여 Eagle Eye Connect를 구성합니다.

### 3단계: AIR에서 소셜 행동 동작 구성 {#step-3-configure-social-behavioral-actions-in-air}

다음으로, 포인트 또는 쿠폰을 발급하기 위한 고유한 동작 참조가 포함된 하나 이상의 소셜 행동 동작을 AIR에서 설정합니다.

### 4단계: Braze 구성 {#step-4-configure-braze}

Braze에서 다음을 완료합니다:

- AIR에서 보상을 발급하기 위한 Campaign을 Braze에서 설정합니다
- AIR 이벤트가 수신될 때 소비자에게 보낼 커뮤니케이션을 설정합니다

### 5단계: 통합 테스트 {#step-5-test-your-integration}

AIR에서 API 호출을 수행하고 이벤트 데이터가 Braze 워크스페이스로 유입되는 것을 확인합니다. AIR에서 수신된 데이터를 검증하고 속성이 예상대로 업데이트되는지 확인합니다.

또한 사용자를 오디언스에 추가하고 AIR에서 보상이 발급되는지 확인합니다.

### 6단계: 프로덕션 출시 {#step-6-launch-to-production}

테스트가 성공적으로 완료되면, 통합을 라이브로 전환하여 Braze로 데이터를 지속적으로 전송할 수 있습니다. AIR과 Braze의 프로덕션 환경에도 동일한 구성 단계가 필요합니다.

Eagle Eye 고객 성공 매니저에게 연락하여 리소스를 할당받고 EE Connect를 설정하세요.

## 고객지원 {#support}

통합 지원 또는 문제 해결이 필요한 경우 Eagle Eye 지원 팀([support@eagleeye.com](mailto:support@eagleeye.com))에 문의하세요.