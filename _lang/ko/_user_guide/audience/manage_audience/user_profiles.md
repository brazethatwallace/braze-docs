---
nav_title: 고객 프로필
article_title: 고객 프로필
page_order: 2
page_type: reference
tool:
  - Dashboard
description: "이 참조 문서에서는 대시보드에서 사용자의 프로필에 액세스하는 방법, 프로필 사용 사례, 각 프로필에 포함된 내용을 설명합니다."

---

# 고객 프로필 {#user-profiles}

> 고객 프로필은 특정 사용자에 대한 정보를 찾는 데 유용한 방법입니다. 사용자와 관련된 모든 영구 데이터는 해당 고객 프로필에 저장됩니다.

## 프로필 접근 {#access-profiles}

사용자의 프로필에 접근하려면 **사용자 검색** 페이지로 이동하여 다음 중 하나로 사용자를 검색합니다:

- 외부 사용자 ID
- Braze ID
- 이메일
- 전화번호
- 푸시 토큰
- "[user_alias]:[alias_name]" 형식의 사용자 별칭(예: "amplitude_id:user_123")

일치하는 결과가 있으면 Braze SDK로 기록한 해당 사용자의 정보를 확인할 수 있습니다. 검색 결과에 여러 고객 프로필이 반환되는 경우 각 프로필을 개별적으로 병합하거나 일괄 사용자 병합을 수행할 수 있습니다. 전체 안내는 [중복 사용자 병합]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users)을 참조하세요.

{% alert note %}
**사용자 검색**은 Segment 또는 Campaign 작성기의 **사용자 조회**와 다릅니다. **사용자 조회**는 특정 사용자가 오디언스와 일치하는지 테스트하며 `external_id` 또는 `braze_id`만 허용합니다. 이 페이지의 **사용자 검색**은 이메일, 전화번호, 푸시 토큰, 사용자 별칭을 지원합니다. 자세한 내용은 [Segment 테스트]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments)를 참조하세요.
{% endalert %}

{% alert important %}
검색에 전화번호를 사용하면 [`E.164`](https://en.wikipedia.org/wiki/e.164) 형식으로 변환됩니다. 전화번호를 `E.164` 형식으로 변환할 수 없는 사용자(예: 전화번호의 국가 코드 또는 지역 코드가 유효하지 않은 경우)는 전화번호로 검색할 수 없습니다.
{% endalert %}

![검색 결과에 "검색 기준과 일치하는 사용자가 여러 명 있습니다"라는 배너와 이전 및 다음이라는 두 개의 버튼이 표시됩니다.]({% image_buster /assets/img_archive/User_Search_Nonunique.png %}){: style="max-width:60%;"}

## 사용 사례 {#use-cases}

고객 프로필은 사용자의 인게이지먼트 이력, Segment 멤버십, 기기, 운영 체제에 대한 정보를 쉽게 확인할 수 있어 문제 해결 및 테스트에 유용한 리소스입니다.

예를 들어, 사용자가 문제를 보고했는데 어떤 기기와 운영 체제를 사용하고 있는지 확실하지 않은 경우, [개요 탭](#overview-tab)을 사용하여 이 정보를 확인할 수 있습니다(이메일 또는 사용자 ID가 있는 경우). 또한 사용자의 언어를 확인할 수 있는데, 이는 예상대로 작동하지 않는 [다국어 Campaign]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization)을 문제 해결할 때 도움이 될 수 있습니다.

[인게이지먼트 탭](#engagement-tab)을 사용하여 특정 사용자가 Campaign을 수신했는지 확인할 수 있습니다. 또한 해당 사용자가 Campaign을 수신한 경우, 언제 수신했는지도 확인할 수 있습니다. 사용자가 특정 Segment에 속해 있는지, 푸시, 이메일 또는 둘 다에 옵트인했는지도 확인할 수 있습니다. 이 정보는 문제 해결 목적으로 유용합니다. 예를 들어, 사용자가 수신할 것으로 예상했던 Campaign을 수신하지 못하거나, 수신할 것으로 예상하지 않았던 Campaign을 수신한 경우 이 정보를 확인해야 합니다.

## 고객 프로필의 구성 요소 {#elements-of-user-profile}

고객 프로필에는 다섯 가지 주요 섹션이 있습니다.

- **개요:** 사용자에 대한 기본 정보, 세션 데이터, 커스텀 속성, 커스텀 이벤트, 구매 내역, 사용자가 마지막으로 로그인한 최근 기기 정보.
- **인게이지먼트:** 사용자의 연락처 설정, 수신한 Campaigns, Segments, 커뮤니케이션 통계, 설치 경로, 무작위 버킷 번호에 대한 정보.
- **이벤트 기록:** 최근 30일간의 커스텀 이벤트 및 구매 내역으로, 전체 이벤트 속성정보가 JSON으로 표시됩니다.
- **메시징 기록:** 최근 30일간 해당 사용자의 메시징 관련 최근 이벤트.
- **기능 플래그 자격:** 롤아웃, 캔버스 단계, 실험 전반에서 사용자가 현재 자격이 있는 기능 플래그를 확인합니다.

{% tabs %}
{% tab 개요 탭 %}

### 개요 탭 {#overview-tab}

**개요** 탭에는 사용자와 앱 또는 웹사이트와의 상호작용에 대한 기본 정보가 포함되어 있습니다.

| 개요 카테고리 | 포함 내용 |
| --- | --- |
| 프로필 | 성별, 연령대, 위치, 언어, 로캘, 시간대, 생일. |
| 세션 개요 | 세션 횟수, 첫 번째 및 마지막 세션 시점, 어떤 앱에서 발생했는지. |
| 커스텀 속성 | 이 사용자에게 부여된 커스텀 속성과 관련 값(중첩 커스텀 속성 포함). |
| 최근 기기 | 로그인한 기기 수, 각 기기의 세부 정보, 관련 광고 ID(있는 경우). |
| 커스텀 이벤트 | 이 사용자가 수행한 커스텀 이벤트, 수행 횟수, 각 이벤트를 마지막으로 수행한 시점. |
| 구매 | 이 사용자에게 귀속된 생애 매출, 마지막 구매, 총 구매 횟수, 각 구매 목록. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="개요 탭 #overview-tab" }

이 데이터에 대한 자세한 내용은 [SDK 데이터 수집]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection)을 참조하세요.

{% endtab %}
<a id="engagement-tab"></a>
{% tab 인게이지먼트 탭 %}

### 인게이지먼트 탭 {#engagement-tab}

**인게이지먼트** 탭에는 Braze를 사용하여 보낸 메시지와 사용자의 상호작용에 대한 정보가 포함되어 있습니다.

| 인게이지먼트 카테고리 | 포함 내용 |
| --- | --- |
| 연락처 설정 | 이메일, SMS, 푸시의 구독 상태와 이 세 채널에 대해 사용자가 연결된 구독 그룹. 이 섹션에는 푸시 토큰에 대한 변경 기록 정보도 포함됩니다. 구독 및 옵트인 설정 방법에 대한 자세한 내용은 [이메일]({{site.baseurl}}/user_guide/channels/email/subscriptions), [SMS]({{site.baseurl}}/sms_rcs_subscription_groups), [푸시]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states)를 참조하세요. |
| 수신한 Campaigns | **수신한 Campaigns**는 채널별 발송 및 조회 시점을 반영합니다. 대부분의 채널은 Braze가 메시지를 전달 제공업체에 전달할 때 발송을 기록하며, 메시지가 최종적으로 전달되지 않더라도 기록됩니다. **Content Cards**는 다릅니다. 사용자가 앱에서 카드를 조회한 후에만 여기에 표시됩니다. 채널별 분류는 [수신한 Campaigns에 표시되는 시점](#when-campaigns-appear-in-campaigns-received)을 참조하세요. <br><br>메시지가 수신, 열람 또는 클릭되면 Braze는 상호작용을 기록한 프로필과 동일한 채널 식별자를 공유하는 모든 프로필의 데이터를 업데이트합니다(예: 이메일의 경우 동일한 이메일 주소, SMS 또는 WhatsApp의 경우 동일한 전화번호). 메시지를 수신, 열람 또는 클릭한 사람과 식별자를 공유하는 사용자는 원래 해당 Campaign에 포함되지 않았거나 직접 메시지를 받지 않았더라도 이 필터에 매칭될 수 있습니다.<br><br>이 목록은 리타겟팅 및 기록에 표시되는 내용을 결정할 때 [메시징 상호작용 데이터]({{site.baseurl}}/api/data_retention/messaging_interaction_data)(만료 규칙 포함)를 사용합니다.<br><br> 목록에서 Campaign을 선택하여 확인할 수 있습니다. |
| Segments | 이 사용자가 포함된 Segments. 목록에서 Segment를 선택하여 확인할 수 있습니다. |
| 커뮤니케이션 통계 | 각 채널에서 이 사용자가 마지막으로 메시지를 수신한 시점. |
| 설치 경로 | 사용자가 앱을 설치한 방법과 시점에 대한 정보. [사용자 설치 이해]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/install_attribution)에서 자세히 알아보세요. |
| 기타 | 사용자의 [무작위 버킷 번호]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers). |
| 수신한 Canvas 메시지 | 이 사용자가 수신한 Canvas 메시지와 수신 시점. 발송 시점은 **수신한 Campaigns**와 동일한 채널 규칙을 따릅니다. [수신한 Campaigns에 표시되는 시점](#when-campaigns-appear-in-campaigns-received)을 참조하세요.<br><br> 메시지가 수신, 열람 또는 클릭되면 Braze는 상호작용을 기록한 프로필과 동일한 채널 식별자를 공유하는 모든 프로필의 데이터를 업데이트합니다(예: 이메일의 경우 동일한 이메일 주소, SMS 또는 WhatsApp의 경우 동일한 전화번호). 메시지를 수신, 열람 또는 클릭한 사람과 식별자를 공유하는 사용자는 원래 해당 Campaign에 포함되지 않았거나 직접 메시지를 받지 않았더라도 이 필터에 매칭될 수 있습니다.<br><br> 목록에서 메시지를 선택하여 확인할 수 있습니다. |
| 예측 | 이 사용자의 [고객이탈 예측]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn) 및 [이벤트 예측]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events) 점수. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="인게이지먼트 탭" }

{% endtab %}
<a id="event-history-tab"></a>
{% tab 이벤트 기록 탭 %}

### 이벤트 기록 탭 {#event-history-tab}

{% alert note %}
**이벤트 기록** 탭을 보려면 **Search Users**, **View User Event Properties**, **View PII** [권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)이 필요합니다. 이벤트 속성정보에 개인 데이터가 포함될 수 있기 때문입니다.
{% endalert %}

**이벤트 기록** 탭에는 사용자가 기록한 커스텀 이벤트와 구매 내역이 표시됩니다. 이벤트 데이터가 올바르게 수신되고 있는지 확인하고, 데이터 내보내기나 외부 도구 없이 대시보드에서 직접 사용자 수준의 문제를 해결하는 데 사용할 수 있습니다.

| 이벤트 기록 카테고리 | 포함 내용 |
| --- | --- |
| 이벤트 목록 | 최근 30일간의 커스텀 이벤트 및 구매(최대 100개), 최신순으로 정렬. |
| 이벤트 유형 | 해당 행이 **커스텀 이벤트**인지 **구매**인지 여부. |
| 타임스탬프 | 이벤트가 기록된 시점. |
| 이벤트 이름 | 커스텀 이벤트 또는 구매의 이름. |
| 이벤트 속성정보 | 이벤트의 전체 이벤트 속성정보로, JSON으로 표시됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="이벤트 기록 탭" }

{% endtab %}
{% endtabs %}

### 수신한 Campaigns에 표시되는 시점 {#when-campaigns-appear-in-campaigns-received}

일반적으로 Braze는 메시지 발송을 시도한 후 **수신한 Campaigns**에 해당 Campaign을 표시합니다. 발송이 기록되기 위해 사용자의 기기나 받은편지함에 실제로 전달될 필요는 없습니다. **수신한 Canvas 메시지**도 각 Canvas 메시지 유형에 대해 동일한 채널별 규칙을 따릅니다.

{% alert tip %}
타임스탬프가 상대적 형식(예: "6일 전")으로 표시되는 경우, 마우스를 올리면 정확한 날짜와 시간을 확인할 수 있습니다.
{% endalert %}

- **이메일:** Braze는 메시지가 이메일 서비스 공급자(ESP)에 전달될 때 발송을 기록합니다. 전달 이후에는 Liquid 로직, 사용량 제한, 또는 사용자가 도달 불가로 표시되어 메시지가 중단되지 않습니다. 이후 이벤트는 보통 전달 또는 반송입니다.
- **푸시:** Braze는 메시지가 푸시 제공업체(예: Apple Push Notification service(APNs) 또는 Firebase Cloud Messaging(FCM))에 전달될 때 발송을 기록합니다. 제공업체는 보통 즉시 전달을 시도하며, 기기를 사용할 수 없는 경우(예: 오프라인) 메시지가 만료될 때까지 재시도할 수 있습니다.
- **인앱 메시지:** Braze는 Campaign이 시작될 때 발송을 기록합니다.
- **Content Cards:** Braze가 _발송_ 이벤트를 기록하는 시점은 전달 유형과 **카드 생성** 설정에 따라 달라집니다. 콘텐츠 카드 Campaign은 사용자가 앱에서 카드를 조회한 후에만 고객 프로필의 **수신한 Campaigns**에 표시됩니다. 전체 분류는 Content Cards 리포팅 문서의 [발송이 기록되는 시점]({{site.baseurl}}/user_guide/channels/content_cards/reporting#when-sends-are-logged) 및 [수신한 Campaigns 및 리타겟팅 필터]({{site.baseurl}}/user_guide/channels/content_cards/reporting#campaigns-received-and-retargeting-filters)를 참조하세요.
- **SMS, WhatsApp, 웹훅:** Braze는 메시지가 해당 채널의 전달 경로(예: SMS 또는 WhatsApp 제공업체, 또는 웹훅 엔드포인트)에 진입할 때 발송을 기록합니다.

{% alert note %}
이 설명은 **수신한 Campaigns**에 대해 발송이 기록되는 시점을 다룹니다. 메시지가 제공업체에 도달하기 전에 중단할 수 있는 [메시지 중단]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)과는 별개입니다.
{% endalert %}

![연락처 설정과 커뮤니케이션 통계를 표시하는 고객 프로필의 인게이지먼트 탭.]({% image_buster /assets/img_archive/profiles_engagement_tab.png %})

### 메시징 기록 탭 {#messaging-history-tab}

고객 프로필의 **메시지 기록** 탭에는 최근 30일간 개별 사용자의 메시징 관련 최근 이벤트(약 40개)가 표시됩니다. 이 이벤트에는 사용자에게 발송된 메시지, 수신한 메시지, 상호작용한 메시지 등이 포함됩니다.

이 탭의 데이터는 사용자가 병합된 후에는 업데이트되지 않습니다. 또한 API를 통해 발송된 메시지(예: [`/messages/send` 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#creating-new-users-with-api-sends))와 관련된 이벤트는 해당 발송에 Campaign ID가 지정되지 않은 경우 이 탭에 표시되지 않습니다.

{% alert important %}
RCS 이벤트는 현재 **메시징 기록** 탭에서 지원되지 않습니다.
{% endalert %}

![사용자가 수신한 Campaigns와 Canvases를 보여주는 메시징 기록 탭.]({% image_buster /assets/img_archive/profiles_messaging_history_tab.png %})

#### 이벤트 보기 및 이해 {#viewing-and-understanding-events}

**메시징 기록** 테이블의 각 이벤트에 대해 메시징 채널, 이벤트 유형, 이벤트 발생 타임스탬프, 관련 Campaign 또는 Canvas 메시지, 사용자의 기기 데이터를 확인할 수 있습니다. 특정 이벤트를 필터링하려면 **필터**를 클릭하고 목록에서 이벤트를 선택합니다.

##### 메시지 인게이지먼트 이벤트 {#message-engagement-events}

다음 메시지 인게이지먼트 이벤트는 이메일, SMS, 푸시, 인앱 메시지, Content Cards, 웹훅에서 사용할 수 있습니다. 특정 이벤트가 추적되는 방식에 대한 자세한 내용은 [메시지 인게이지먼트 이벤트 용어집]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)을 참조하세요.

| 채널 | 사용 가능한 인게이지먼트 이벤트 |
| --- | --- |
| 이메일 | 반송<br>클릭<br>지연 이벤트<br>전달<br>스팸 신고<br>열람 ([이메일 열람 이벤트에 대한 참고 사항](#note-on-email-open-event) 참조)<br>발송<br>소프트 반송<br>탈퇴 |
| SMS | 통신사 발송<br>전달<br>전달 실패<br>인바운드 수신<br>거부<br>발송 |
| 푸시 | 반송<br>영향받은 열람<br>iOS 포그라운드<br>열람<br>발송 |
| 인앱 메시지 | 클릭<br>노출 |
| Content Cards | 클릭<br>닫기<br>노출<br>발송 |
| 웹훅 | 발송 |
| WhatsApp | 중단<br>전달<br>실패<br>최대 게재빈도 제한<br>인바운드 수신<br>읽음<br>발송 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="메시지 인게이지먼트 이벤트" }

##### 메시지 중단 이벤트 {#message-abort-events}

메시지 중단 이벤트는 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) 또는 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content)의 조건 로직으로 인해, 또는 Liquid 렌더링 시간 초과로 인해 사용자에게 보낸 메시지가 중단되었을 때 발생합니다.

중단 이벤트는 다음 채널에서 사용할 수 있습니다:

- 이메일
- SMS
- 푸시
- 웹훅

중단 이벤트는 현재 인앱 메시지와 Content Cards에서는 사용할 수 없습니다.

##### 최대 게재빈도 제한 이벤트 {#frequency-cap-events}

최대 게재빈도 제한 이벤트는 사용자가 메시지를 수신할 자격이 있지만 [최대 게재빈도 설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping) 때문에 실제로 수신하지 못할 때 발생합니다. **설정** > **최대 게재빈도 규칙**에서 최대 게재빈도 설정을 커스터마이즈할 수 있습니다.

##### 빈 대상 {#blank-destinations}

일부 메시지 발송은 메시징 기록에 빈 대상("—"으로 표시)으로 나타날 수 있습니다. 이는 Content Cards 및 웹훅과 같은 일부 채널이 메시지 발송 시 기기 데이터를 수집하지 않기 때문입니다.

Content Cards 발송은 카드를 조회할 수 있게 되었을 때 기록됩니다. Content Cards는 여러 기기에서 조회할 수 있으므로 발송 시 기기 데이터가 기록되지 않습니다. 대신 이 정보는 노출 시(카드가 실제로 조회될 때) 기록됩니다. 웹훅은 시스템 엔드포인트(기기가 아닌)로 전송되므로 기기 데이터가 해당되지 않습니다.

#### 이메일 열람 이벤트에 대한 참고 사항 {#note-on-email-open-event}

이메일 열람 추적은 Braze를 포함한 모든 도구에서 오류가 발생하기 쉽습니다. 다양한 이메일 클라이언트가 제공하는 개인정보 보호 기능으로 인해 이미지의 자동 로딩을 차단하거나 서버에서 사전에 로딩하는 경우가 있어, 이메일 열람 이벤트는 거짓 양성과 거짓 음성 모두에 취약합니다.

이메일 열람 통계는 집계 수준에서 유용할 수 있지만(예: 다른 제목란의 효과 비교), 개별 사용자의 개별 열람 이벤트가 의미 있다고 가정해서는 안 됩니다.

#### 메시지 기록 탭에서 특정 필드가 비어 있는 이유는? {#why-are-certain-fields-blank-in-the-message-history-tab}

다음 시나리오에서 사용자의 **메시지 기록** 탭에 일부 필드가 없을 수 있습니다:

- **메시지 발송** 데이터가 누락된 이벤트는 해당 Campaign에 메시지 변형이 없음을 나타냅니다.
- **Campaign/Canvas** 및 **메시지 발송** 데이터가 누락된 이벤트는 `campaign_id`와 `message_variation_id`를 지정하지 않은 API Campaign(API 트리거 Campaign이 아닌)에서 보낸 메시지임을 나타냅니다. 이 필드는 선택 사항이며 요청 본문에서 생략될 수 있습니다. 이 필드가 지정되면 해당 정보가 메시지 기록 로그에 채워집니다.
   - 특정 메시지가 메시징 기록에는 없지만 **수신한 Campaigns** 로그에 나타나는 경우, 해당 사용자가 현재 사용자로 식별되기 전에 Campaign을 수신했을 가능성이 높습니다. 기존 프로필이 분리된 경우 **수신한 Campaigns** 로그는 이전되지만 메시징 기록은 이전되지 않습니다.
- **Campaign/Canvas** 데이터가 누락된 경우 수동 테스트가 발송되었을 수 있습니다. 수동 테스트는 **메시징 기록** 탭에 기록되지만, 발송된 Campaign 또는 Canvas는 기록되지 않습니다.
- 사용자가 시드 그룹이나 기타 내부 테스트 오디언스에 속한 경우, **메시징 기록**에 프로덕션 발송에 비해 제한된 Campaign 또는 Canvas 메타데이터가 표시될 수 있습니다.

## 데이터 크기 제약 조건 {#data-size-constraints}

Braze는 사용자 프로필의 전체 크기에 대한 총 용량 제한을 적용하지 않습니다. 그러나 사용자와 관련된 특정 데이터 유형에는 정의된 크기 용량이 있습니다.

### 커스텀 속성 배열 {#custom-attribute-arrays}

커스텀 속성 배열(객체 배열 포함)의 용량은 100KB입니다. 이 용량을 초과하는 배열을 전송하면 커스텀 속성이 처리되지 않습니다. API는 성공 응답(201)을 반환하지만, 배열이 고객 프로필에 표시되지 않으며 해당 속성의 기존 데이터도 업데이트되지 않습니다.

배열이 이 용량에 근접하는 경우, 전체 크기가 100KB 이내로 유지되도록 채우는 객체 수를 제한하는 것을 고려하세요.

커스텀 속성에 대한 자세한 내용은 [커스텀 속성 데이터 유형]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types)을 참조하세요.

## 관련 문서 {#related-articles}

- [사용자 프로필 수명주기]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)
- [POST: 식별자로 고객 프로필 내보내기]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [POST: 사용자 삭제]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)