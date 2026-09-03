---
nav_title: 커런츠 설정
article_title: 커런츠 설정
page_order: 1
page_type: tutorial
description: "이 사용 방법 문서는 Braze 커런츠를 통합하고 구성하는 과정을 안내합니다."
tool: Currents
search_rank: 8
---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/currents-the-basics-2/){: style="float:right;width:120px;border:0;" class="noimgborder"}커런츠 설정 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomcurrents-the-basics-2-stylefloatrightwidth120pxborder0-classnoimgborderset-up-currents}

> 이 페이지는 Braze 커런츠를 통합하고 구성하는 일반적인 프로세스를 설명합니다.

{% alert important %}
Currents는 특정 Braze 패키지에 포함되어 있습니다. 질문이 있거나 접근 권한을 얻고 싶으시면 Braze 담당자에게 문의하세요.
{% endalert %}

## 문제 해결 {#troubleshooting}

### 새 Currents 통합을 추가할 수 없음 {#cannot-add-a-new-currents-integration}

새 통합을 추가할 때 "You do not have any remaining Currents integrations"라는 메시지가 표시되거나, 새 Currents 커넥터를 추가하는 버튼이 회색으로 비활성화되어 있는 경우, 일반적인 원인은 다음과 같습니다:

- 이 워크스페이스에 대해 Currents 이용 권한이 구매되지 않았습니다.
- Currents 이용 권한이 회사 내 다른 워크스페이스에서 사용 가능합니다.

이 문제를 해결하려면 회사 내 다른 워크스페이스를 확인하세요. 다른 워크스페이스에서 사용 가능한 Currents 이용 권한이 표시될 수 있습니다. 이용 권한을 요청하거나 구성을 조정해야 하는 경우, Braze 계정 매니저에게 문의하세요.

### 추가 이벤트 추적을 활성화할 수 없음 {#cannot-enable-additional-event-tracking}

커넥터를 생성하거나 편집할 수는 있지만 선택 사항인 추적 스위치 중 하나를 활성화할 수 없는 경우, 해당 이벤트 카테고리에 대한 이용 권한 한도에 도달했을 수 있습니다.

- **Track Customer Behavior and User Events**를 사용하려면 **고객 행동 이벤트** 이용 권한이 필요합니다.
- **Track user profiles and attributes**를 사용하려면 **User Profiles and Attributes** 이용 권한이 필요합니다.

추가 이용 권한이 필요하거나 구성 조정에 도움이 필요한 경우, Braze 계정 매니저에게 문의하세요.

## 요구 사항 {#requirements}

Currents를 파트너와 함께 사용하려면 동일한 기본 파라미터와 연결 방법이 필요합니다.

각 파트너는 Braze가 데이터 파일을 작성하고 전송할 수 있는 권한을 요구하며, Braze는 해당 파일을 작성할 위치, 특히 버킷 이름이나 키를 요청합니다.

다음 요구 사항은 대부분의 파트너와 통합하기 위한 기본적이고 최소한의 요구 사항입니다. 일부 파트너는 추가 파라미터를 요구할 수 있으며, 이러한 기본 요구 사항과 관련된 세부 사항과 함께 해당 [파트너 설명서]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners)에 나열되어 있습니다.

| 요구 사항 | Origin | 액세스 | 설명
|---|---|---|---|
| 파트너 계정 | 해당 파트너와 계정을 준비하거나 Braze 계정 매니저에게 문의하여 추천을 받으세요. | 해당 파트너의 사이트를 확인하거나 파트너에게 연락하여 가입하세요. | 회사 계정을 통해 해당 데이터에 액세스할 수 없는 경우, Braze는 파트너에게 데이터를 전송하지 않습니다.
| 파트너 API 키 또는 토큰 | 일반적으로 파트너의 대시보드에서 확인할 수 있습니다. | 복사하여 지정된 Braze 필드에 붙여넣으세요. | Braze는 해당 파트너의 통합 페이지에 이를 위한 지정 필드를 제공합니다. 데이터를 전송할 위치를 매핑하는 데 필요합니다. **파트너 키 또는 토큰을 항상 최신 상태로 유지하세요. 자격 증명이 유효하지 않으면 커넥터가 비활성화되고 이벤트가 삭제될 수 있습니다.**
| 인증 코드/키, 비밀 키, 인증서 파일 | 해당 파트너 계정 담당자에게 문의하세요. 파트너의 대시보드에서도 확인할 수 있습니다. | 키를 복사하여 지정된 Braze 필드에 붙여넣으세요. `.json` 또는 기타 인증서 파일을 생성하여 Braze의 적절한 위치에 업로드하세요. | Braze는 해당 파트너의 통합 페이지에 이를 위한 지정 필드를 제공합니다. 이를 통해 Braze에 자격 증명이 부여되고 파트너 계정에 파일을 작성할 수 있는 권한이 주어집니다. **인증 세부 정보를 항상 최신 상태로 유지하는 것이 중요합니다. 자격 증명이 유효하지 않으면 커넥터가 비활성화되고 이벤트가 삭제될 수 있습니다.**
| 버킷, 폴더 경로 | 일부 파트너는 버킷별로 데이터를 구성하고 정렬합니다. 파트너의 대시보드에서 확인할 수 있습니다. | 필요한 경우, 버킷 이름이나 파일 경로를 정확히 복사하여 Braze의 지정된 공간에 붙여넣으세요. | 일부 파트너에서만 필요하지만, 필요할 때 정확하게 입력하는 것이 중요합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요구 사항" }

{% alert important %}
파트너 키, 파트너 토큰 및 인증 세부 정보를 항상 최신 상태로 유지하는 것이 중요합니다. 커넥터의 자격 증명이 만료되면 커넥터가 이벤트 전송을 중지합니다. 이 상태가 **5일** 이상 지속되면 커넥터의 이벤트가 삭제되고 데이터가 영구적으로 손실됩니다.
{% endalert %}

## Currents 설정하기 {#setting-up-currents}

### 1단계: 파트너 선택하기 {#step-1-choose-your-partner}

Braze Currents를 사용하면 플랫 파일을 이용한 데이터 스토리지를 통해 통합하거나, 지정된 엔드포인트로 배치된 JSON 페이로드를 보내 행동 분석 및 고객 데이터 파트너와 통합할 수 있습니다.

통합을 시작하기 전에 어떤 통합이 목적에 가장 적합한지 결정하는 것이 좋습니다. 예를 들어, 이미 mParticle과 Segment를 사용하고 있으며 Braze 데이터를 해당 서비스로 스트리밍하고 싶다면 배치된 JSON 페이로드를 사용하는 것이 좋습니다. 데이터를 직접 다루거나 더 복잡한 데이터 분석 시스템이 있는 경우에는 데이터 스토리지를 사용하는 것이 좋습니다([Braze도 이 방법을 사용합니다]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents)!).

### 2단계: Currents 열기 {#step-2-open-currents}

시작하려면 **파트너 통합** > **Currents**로 이동합니다. Currents 통합 관리 페이지로 이동합니다.

![Braze 대시보드의 Currents 페이지]({% image_buster /assets/img_archive/currents-main-page.png %})

### 3단계: 파트너 추가하기 {#step-3-add-your-partner}

화면 상단의 드롭다운을 선택하여 파트너(Currents 커넥터라고도 함)를 추가합니다.

각 파트너마다 서로 다른 구성 단계가 필요합니다. 각 통합을 활성화하려면 [사용 가능한 파트너]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) 목록을 참조하고 해당 페이지의 안내를 따르세요.

{% multi_lang_include currents/contact_email_notifications.md %}

### 4단계: 이벤트 구성하기 {#step-4-configure-your-events}

사용 가능한 옵션에서 체크하여 해당 파트너에게 전달할 이벤트를 선택합니다. 이러한 이벤트 목록은 [고객 행동 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) 및 [메시지 인게이지먼트 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) 라이브러리에서 확인할 수 있습니다.

![내보내기를 위해 파트너 이벤트가 선택된 Currents 구성 페이지]({% image_buster /assets/img/current4.png %})

필요한 경우 [이벤트 전달 의미론]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics) 문서에서 이벤트에 대해 자세히 알아볼 수 있습니다.

### 5단계: 필드 변환 설정하기 {#step-5-set-up-field-transformations}

Currents 필드 변환을 사용하여 문자열 필드를 제거하거나 해싱할 수 있습니다.

- **제거:** 문자열 필드를 `[REDACTED]`로 대체합니다. 파트너가 누락되거나 비어 있는 필드가 있는 이벤트를 거부하는 경우에 유용합니다.
- **해싱:** 문자열 필드에 SHA-256 해싱 알고리즘을 적용합니다.

이러한 변환 중 하나에 필드를 선택하면 해당 필드가 나타나는 모든 이벤트에 해당 변환이 적용됩니다. 예를 들어, `email_address`를 해싱 대상으로 선택하면 이메일 전송, 이메일 열람, 이메일 반송 및 구독 그룹 상태 변경 이벤트에서 `email_address` 필드가 해싱됩니다.

![필드 변환 추가하기]({% image_buster /assets/img/current3.png %})

### 6단계: 통합 테스트하기 {#step-6-test-your-integration}

{% alert important %}
Currents는 900&nbsp;KB보다 큰 과도하게 큰 페이로드를 가진 이벤트를 삭제합니다.
{% endalert %}

테스트하기 전에 [GitHub의 Currents 샘플 데이터](https://github.com/Appboy/currents-examples)를 확인해 보는 것이 좋습니다. 테스트할 준비가 되면 다음 섹션에서 옵션을 선택합니다.

#### 테스트 이벤트 전송 {#sending-test-events}

통합을 테스트하려면 **Send Test Events**를 선택하여 선택한 각 이벤트 유형에서 하나의 이벤트를 이 Currents로 전송할 수 있습니다. 각 이벤트 유형에 대한 자세한 내용은 [고객 행동 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) 및 [메시지 인게이지먼트 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) 라이브러리를 참조하세요.

![Braze 대시보드의 Currents 테스트 페이지]({% image_buster /assets/img/currents/current_test_events.png %}){: style="max-width:70%;"}

#### Currents 커넥터 테스트 {#testing-currents-connectors}

테스트 Currents 커넥터는 다양한 대상을 테스트하고 시도해 볼 수 있는 기존 커넥터의 무료 버전입니다. 테스트 Currents의 특징:

- 워크스페이스당 최대 10개의 테스트 Currents 커넥터
- 고정된 24시간 기간 동안 최대 1,500개 이벤트(총합 기준)이며, 매일 자정(UTC)에 초기화됩니다. 이 이벤트 총량은 대시보드에서 매시간 업데이트됩니다.

테스트 Currents 커넥터가 전송 한도에 도달하면 다음 날(자정 UTC)까지 이벤트를 전송하지 않습니다.

테스트 Currents 커넥터를 업그레이드하려면 대시보드에서 통합을 편집하고 **Upgrade Test Integration**을 선택합니다.

## Currents 업데이트하기 {#updating-currents}

{% multi_lang_include currents/updating_currents.md %}

## IP 허용 목록 {#ip-allowlisting}

Braze는 아래 나열된 IP에서 Currents 데이터를 전송합니다:

{% multi_lang_include administer/data_centers.md datacenters='ips' %}