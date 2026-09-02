---
nav_title: Punchh
article_title: Punchh
page_order: 1
description: "이 참조 문서에서는 로열티 및 인게이지먼트 플랫폼인 Punchh와 Braze 간의 파트너십에 대해 설명합니다. 두 플랫폼 간에 데이터를 동기화할 수 있으며, Braze에 게시된 데이터는 세분화에 사용할 수 있고, Braze에서 설정한 웹훅 템플릿을 통해 사용자 데이터를 Punchh로 다시 동기화할 수 있습니다."
page_type: partner
search_tag: Partner
---

# Punchh

> [Punchh](https://punchh.com/)는 브랜드가 매장 내 및 디지털 방식으로 옴니채널 고객 로열티 프로그램을 제공할 수 있도록 하는 업계 최고의 로열티 및 인게이지먼트 플랫폼입니다.

_이 통합은 Punchh에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

Braze와 Punchh 통합을 통해 두 플랫폼 간에 기프팅 및 로열티 목적의 데이터를 동기화할 수 있습니다. Braze에 게시된 데이터는 세분화에 활용할 수 있으며, Braze 웹훅을 통해 사용자 데이터를 다시 Punchh로 동기화할 수 있습니다.

## 이점은 무엇인가요? {#what-are-the-benefits}

- Punchh의 로열티 데이터를 Braze로 실시간으로 수집합니다.
- Braze의 강력한 오디언스 데이터를 활용하고 레이어링하여 의미 있고 동적인 크로스채널 경험(앱, 모바일, 웹, 이메일, SMS)을 제공합니다.
  - 고객이 이메일을 열었나요? 고객이 매장 근처에서 앱을 열었나요?
- Braze를 통해 전송되는 트랜잭션 이메일의 디자인과 느낌을 표준화합니다.
- A/B 테스트와 최적화를 진행하면서 여정을 생성합니다.

## 전제 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Punchh 계정 | 이 파트너십을 활용하려면 활성화된 Punchh 계정이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키가 필요합니다. <br><br> 이 키는 Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/api/basics#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="전제 조건" }

## 그 밖에 알아야 할 사항 {#what-else-should-i-know}

### 통합 전 확인 사항 {#before-integrating}

- Braze 통합을 활용할 때는 두 개의 Campaign이 필요합니다. 하나는 Punchh에서, 다른 하나는 Braze에서 설정합니다. 예를 들어, 오퍼가 첨부된 Campaign을 보내는 경우, 선물 Campaign은 Punchh 내에서 구성하고 알림은 Braze에서 발송할 수 있습니다.
- 게스트는 이미 Punchh와 Braze에 존재해야 합니다. Punchh는 로열티 게스트가 아닌 고객을 자동으로 필터링합니다.

### 중요 참고 사항 {#important-things-to-note}

- Punchh는 기본 사용자 속성을 Braze로 전송하는 기능을 비활성화할 수 있는 옵션을 추가했습니다. 이를 통해 고객이 데이터 포인트 초과량을 발생시키지 않도록 할 수 있습니다. 이 설정은 어댑터 설정 시 구성됩니다.
- 반복 Campaign에서 커스텀 Segments를 사용하는 경우, Campaign이 실행될 때마다 ID가 변경되므로 Campaign ID 대신 Campaign 이름을 사용해야 합니다.
- 각 Punchh 선물 Campaign 내에서 사용할 수 있는 커뮤니케이션 채널에는 리치 메시지, 푸시 알림, SMS, 이메일이 포함됩니다.
- Braze에서 Punchh 커스텀 Segment로 사용자를 전송한 후에는 해당 사용자를 제거할 수 없습니다. 기존 커스텀 Segment에는 새로운 게스트만 추가할 수 있습니다. 기존 Punchh 커스텀 Segment에서 게스트를 제거해야 하는 경우, Braze에서 새로운 웹훅 Campaign을 생성하여 사용자를 새 Punchh 커스텀 Segment로 전송해야 합니다.

## 통합 {#integration}

Punchh는 Braze 고객이 다음 Punchh API 엔드포인트를 사용하여 Punchh 플랫폼에 외부 ID를 추가할 수 있도록 여러 엔드포인트를 제공합니다. 외부 ID가 추가된 후, Punchh에서 어댑터를 생성하고 Braze 자격 증명을 제공한 다음 동기화할 이벤트를 선택합니다. 그런 다음 Punchh Segment ID를 사용하여 Canvas 여정에서 고객 동기화를 트리거하는 Punchh 웹훅을 구축할 수 있습니다.

Punchh `user_id`와 Braze `external_id`가 통합이 올바르게 동기화되려면 두 플랫폼 모두에서 사용할 수 있어야 합니다.
- Punchh에서 Braze로 전송되는 이벤트에는 Braze `external_id`가 식별자로 포함됩니다. Punchh가 `external_source_id`를 사용하도록 구성된 경우, 해당 값이 Braze `external_id`로 설정됩니다. 그렇지 않으면 통합에서 기본적으로 Punchh `user_id`가 Braze `external_id`로 설정됩니다.
- Braze에서 Punchh로 웹훅을 보내려면 Punchh `user_id`가 Braze 사용자 프로필에서 사용 가능해야 합니다. Punchh `user_id`가 Braze `external_id`로 사용되지 않는 경우, 커스텀 속성 "punchh_user_id"로 설정해야 합니다.

### 1단계: 외부 ID 수집 엔드포인트 설정 (선택 사항) {#step-1-set-up-external-id-ingestion-endpoints-optional}

Braze의 외부 ID는 다음 엔드포인트를 사용하여 신규 및 기존 Punchh 사용자에게 추가할 수 있습니다.

{% alert important %}
`external_source` 및 `external_source_id` 필드 값은 Punchh에서 고유해야 하며 기존 프로필과 연결되지 않아야 합니다.
{% endalert %}

1. 신규 Punchh 사용자<br>
`external_source` 및 `external_source_id` 필드를 사용하여 Punchh 가입 엔드포인트로 Punchh에서 신규 사용자를 생성합니다. Punchh는 다음 가입 엔드포인트 중 하나를 통해 사용자 프로필과 함께 외부 식별자를 전송할 수 있습니다:
- [모바일 가입 API](https://developers.punchh.com/docs/dev-portal-mobile/2e67abf6f8e12-sign-up-register)
- [SSO 가입 API](https://developers.punchh.com/docs/dev-portal-online-ordering/58f18dfdd2a3d-signup-with-email-and-password)<br><br>
2. 기존 Punchh 사용자 <br>
기존 Punchh 사용자에 대해 `external_source_id`를 업데이트합니다. Punchh는 사용자 API 업데이트 엔드포인트를 통해 프로필에 외부 식별자를 추가할 수 있습니다:
- [모바일 사용자 업데이트](https://developers.punchh.com/docs/dev-portal-mobile/c9b928e35a6f3-update-user-profile)
- [SSO 사용자 업데이트](https://developers.punchh.com/docs/dev-portal-online-ordering/eef4eef6c97a0-update-user-information)
- [대시보드 사용자 업데이트](https://developers.punchh.com/docs/dev-portal-platform-functions/6351feaf591aa-update-a-user)
<br><br>
{% tabs local %}
{% tab 사용자 가입 API 예제 %}
이 예제에서는 가입 시 사용자 프로필과 함께 외부 식별자를 전송할 수 있습니다. `external_source`를 "customer_id"로, `external_source_id`를 "111111111111111111"로 문자열 데이터 유형으로 전송합니다.

```bash
curl --location --request POST 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Accept-Timezone: Etc/UTC' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--data-raw '{
    "client":"CLIENT",
    "user" : {
      "email": "test@example.com",
      "password": "PASSWORD",
      "first_name":"FIRST_NAME",
      "last_name":"LAST_NAME",
      "terms_and_conditions":"true",
      "anniversary":"2014-02-02",
      "zip_code":"94497",
      "birthday":"2004-02-02",
      "external_source":"customer_id",
      "external_source_id":"111111111111111111"
      }
}'
```
{% endtab %}
{% tab 사용자 업데이트 API 예제 %}
이 예제에서는 사용자 프로필의 외부 식별자를 업데이트할 수 있습니다. `external_source`를 "customer_id"로, `external_source_id`를 "111111111111111111"로 문자열 데이터 유형으로 전송합니다.

```bash
curl --location --request PUT 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Authorization: Bearer ACCESS_TOKEN' \
--data-raw '{
    "client":"CLIENT",
    "user": {
        "external_source":"customer_id",
        "external_source_id":"111111111111111111"
    }
}'
```
{% endtab %}
{% endtabs %}

{% alert note %}
**플랫폼 구성:** Punchh에서 외부 식별자를 활성화하려면 Punchh 대시보드에서 **Cockpit** > **Dashboard** > **External User Identifier**로 이동합니다.
{% endalert %}

### 2단계: Punchh에서 Braze 어댑터 설정 {#step-2-braze-adapter-setup-in-punchh}

#### 동기화 가능한 이벤트 {#available-events-to-sync}

1. **게스트:** 가입, 게스트 프로필 업데이트, 비활성화 또는 삭제 시 트리거됩니다.
2. **로열티 체크인:** 로열티 트랜잭션 또는 영수증 바코드 스캔을 통한 적립 시 트리거됩니다.
3. **기프트 체크인:** Campaign에서 포인트가 지급될 때 트리거됩니다.
4. **사용:** 리워드 사용 시 트리거되며, Punchh 쿠폰은 제외됩니다. 쿠폰은 발급 및 사용을 포함하여 별도의 쿠폰 이벤트로 전송됩니다.
5. **리워드:** Campaigns, 활동, 포인트를 리워드로 전환, 또는 관리자 지급을 통해 리워드가 지급될 때 트리거됩니다.
6. **트랜잭션 알림:** Punchh 시스템 내에서 사용자에 대한 트랜잭션 활동이 발생할 때 트리거됩니다(예: 포인트 만료).
7. **마케팅 알림:** 관련 사용자 Segment에 대한 Punchh의 다양한 Campaign 설정에 따라 트리거됩니다.

{% alert note %}
이러한 동기화 가능한 이벤트의 샘플 페이로드에 대한 내용은 Punchh 설명서를 참조하세요.
{% endalert %}

이 어댑터를 설정하려면 Punchh 구현 매니저와 협력하세요.

Braze와 Punchh 통합을 설정하려면 다음을 수행합니다:

1. Punchh 대시보드에서 **Cockpit** > **Dashboard** > **Major Features** > **Enable Webhook Management**로 이동하여 **Enable Webhook Management**를 토글합니다.<br><br>
2. 다음으로, **Settings** > **Webhooks 매니저** > **Configurations** > **Show Adapters Tab**으로 이동하여 **Show Adapters Tab**을 토글하여 어댑터를 활성화합니다.<br><br>
3. **Settings** 탭에서 **Webhooks Manager**로 이동하고, **Adapters** 탭을 선택한 다음 **Create Adapter**를 클릭합니다. <br><br>![Create Adapter가 선택된 Punchh Webhooks Manager Adapters 탭]({% image_buster /assets/img/punchh/punchh1.png %})<br><br>
4. 어댑터 이름, 설명 및 관리자 이메일을 입력합니다. 어댑터로 **Braze**를 선택하고 Braze REST API 엔드포인트와 Braze API 키를 제공합니다.<br><br>
5. 다음으로, 활성화할 동기화 가능한 이벤트를 선택합니다. 이벤트 목록은 [동기화 가능한 이벤트](#available-events-to-sync)에서 확인할 수 있습니다.<br><br>![Braze 동기화를 위한 선택 가능한 이벤트가 표시된 Punchh 어댑터 설정]({% image_buster /assets/img/punchh/punchh3.png %})<br><br>
6. **Submit**을 클릭하여 웹훅을 활성화합니다.

## Braze에서 Punchh 웹훅 생성 {#create-punchh-webhook-in-braze}

Braze는 Punchh 커스텀 Segments를 활용하는 웹훅을 통해 사용자를 Punchh Segment에 추가할 수 있습니다.

1. Punchh에서 커스텀 Segment를 생성하고 다음 예시와 같이 Punchh Segment 대시보드 URL에 있는 `custom_segment_id`를 기록합니다. 클래식 또는 베타 Segment 빌더 모두 사용할 수 있습니다. 다만, 클래식은 향후 지원이 중단될 예정이므로 베타를 사용하는 것이 좋습니다.<br><br>Punchh 플랫폼에서 **Guest** > **Segment** > **Custom List** > **New Custom List**로 이동합니다.<br><br>![URL에 커스텀 Segment ID가 표시된 Punchh 커스텀 Segment 대시보드.]({% image_buster /assets/img/punchh/update1.png %})<br><br>

2. Punchh의 사용자를 커스텀 Segment에 추가하는 엔드포인트를 웹훅 URL로 사용하여 Braze에서 웹훅 Campaign을 생성합니다. 여기에서 URL에서 가져온 `custom_segment_id`와 `user_id`를 키-값 페어로 제공할 수 있습니다.<br><br>![Punchh 엔드포인트와 키-값 페이로드 필드가 포함된 Braze 웹훅 작성기.]({% image_buster /assets/img/punchh/punchh4.png %})<br><br>

3. 이 웹훅은 단일 Campaign으로 설정하거나 Canvas 내의 단계로 설정할 수 있습니다. 또는, 이 특정 Punchh Segment에 사용자를 추가하는 웹훅이 여러 Campaigns 또는 Canvases에서 사용될 경우 [템플릿]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates)으로 설정할 수 있습니다.<br><br>
웹훅 내의 `user_id` 키는 Punchh 사용자 ID에 매핑됩니다. 이 식별자는 사용자를 Punchh 커스텀 Segment에 추가하기 위해 Braze에서 생성하는 모든 웹훅에 추가해야 합니다. `punch_user_id` 커스텀 속성은 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid#pre-formatted-variables)를 사용하여 `user_id` 키의 값으로 동적으로 채울 수 있습니다. 템플릿 텍스트 필드 도구 모음의 파란색 "플러스" 아이콘을 사용하여 `punchh_user_id` 커스텀 속성 변수를 삽입할 수 있습니다.<br><br>![Punchh 사용자 ID Liquid 변수가 삽입된 Braze 웹훅 페이로드 필드.]({% image_buster /assets/img/punchh/update3.png %}){: style="max-width:65%;"}<br><br>![punchh_user_id 커스텀 속성이 표시된 Braze 개인화 선택기.]({% image_buster /assets/img/punchh/update4.png %}){: style="max-width:65%;"}<br><br>

4. 웹훅이 저장되면 사용자를 동기화하는 데 사용할 수 있습니다. 예를 들어, 이 Braze 웹훅 Campaign이 실행되면 136명의 게스트가 Punchh 커스텀 Segment에 추가됩니다.<br><br>![Braze와 Punchh 통합으로 저장된 웹훅을 사용하여 사용자를 동기화하는 예시.]({% image_buster /assets/img/punchh/punchh6.png %})

Braze에서 웹훅이 사용되는 방법에 대한 자세한 내용은 [웹훅 생성]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook)을 참조하세요.

## 사용 사례 캠페인 {#use-case-campaigns}

### Campaign 및 Canvas 구성 {#campaign-and-canvas-configuration}

#### 트리거 {#triggering}

리워드 이벤트나 게스트 이벤트와 같은 Punchh 이벤트가 Braze로 전송될 때 트리거되는 Braze 메시징 사용 사례는 [액션 기반 캠페인]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) 또는 관련 Punchh 이벤트에 의해 트리거되는 Canvases로 생성할 수 있습니다.

트리거를 추가하면 Braze에서 생성된 이벤트 목록이 표시됩니다. Campaign 또는 Canvas를 트리거하여 해당 이벤트를 기록한 사용자에게 전송할 이벤트를 선택하세요.

![액션 기반 캠페인에 대해 Punchh 이벤트가 선택된 Braze 트리거 구성 화면.]({% image_buster /assets/img/punchh/update5.png %})

트리거 이벤트를 더욱 세분화하기 위해 속성 필터를 추가할 수 있습니다. 예를 들어, 고객이 승인된 이벤트 속성이 `true`인 "checkins_gift" 이벤트를 트리거할 때만 메시지가 트리거되도록 설정할 수 있습니다. 이것은 모든 사용 사례에 적용되지 않을 수 있는 선택적 기능입니다.

#### 세분화 {#segmentation}

많은 경우, Punchh 이벤트에 의해 트리거되는 Braze Campaign 및 Canvases는 "모든 사용자" 오디언스로 설정할 수 있습니다. 이는 이러한 이벤트를 트리거하는 사용자의 세분화가 Punchh 내에서 결정되기 때문입니다. 그러나 이벤트에 의해 트리거되는 Braze 메시징을 수신할 사용자 오디언스를 더욱 세분화하려는 고객은 Campaign 작성기의 **타겟 오디언스** 섹션 또는 Canvas 작성기의 **진입 오디언스**에서 추가 필터와 Segments를 추가하여 이를 수행할 수 있습니다.

### 사용 사례 {#use-cases}

{% tabs local %}
{% tab 가입 %}
#### 가입 캠페인 {#sign-up-campaign}

오퍼가 첨부된 가입 캠페인에 Braze 구성을 활용할 때, Punchh 내에서 가입 기프팅 캠페인을 구성하고 Braze에서 웰컴 메시지를 설정해야 합니다.

Punchh는 가입 캠페인에 실행 지연을 추가하여 Braze가 먼저 게스트 이벤트를 기반으로 웰컴 메시지를 트리거할 수 있도록 권장합니다. 사용자에게 기프트를 받았다는 후속 메시지를 보내려면 리워드 이벤트를 기반으로 이를 트리거할 수 있습니다.

가입 캠페인의 경우 모든 가입자를 Segment로 사용할 수 있으므로 커스텀 Braze Segment는 필요하지 않습니다.

Punchh 구성 요건:
- 캠페인: 가입
- Segment: 모든 가입자
- 리워드: 고객 선택
필요한 이벤트:
- 리워드 이벤트
- 게스트 이벤트
고려 사항:
- 실행 지연, 게스트에게 5~10분 지연을 추가하는 것을 권장합니다

![사용자 Segment가 Punchh에서 구성되고 게스트가 로열티 프로그램에 가입합니다. 이후 게스트 이벤트가 트리거되면 Braze 메시징 캠페인이 트리거됩니다. 다음으로 10분 후 Punchh 가입 기프팅 캠페인이 트리거되어 리워드 이벤트와 선택적 후속 메시지가 발송됩니다.]({% image_buster /assets/img/punchh/usecase3.png %})
{% endtab %}

{% tab Braze 웰컴 %}
#### Braze 웰컴 캠페인 {#braze-welcome-campaign}

새 사용자가 가입하면, Punchh가 Braze에 게스트 이벤트를 전송하여 사용자를 생성하고 커스텀 속성 `signup_channel`을 전송합니다. 이를 사용하여 Braze 웰컴 캠페인을 트리거할 수 있습니다.

Braze 웰컴 캠페인을 설정하려면 다음 단계를 따르세요:

1. Braze에서 액션 기반 캠페인을 생성합니다.
2. 트리거로 **커스텀 속성 값 변경**을 선택하고 커스텀 속성 `signup_channel`을 **모든 새 값**으로 설정합니다.
3. 캠페인 생성을 계속한 후 준비가 되면 전송하세요!

{% endtab %}
{% tab 대량 오퍼 %}
#### 대량 오퍼 캠페인 {#mass-offer-campaign}

기프팅을 위한 대량 오퍼 캠페인을 활용할 때, Punchh 내에서 대량 오퍼 캠페인을 구성하고 Braze에서 메시징 캠페인을 설정해야 합니다.

캠페인에 Braze Segment를 사용하거나 Punchh 플랫폼에서 게스트에게 기프팅하기 전에 Braze에서 커뮤니케이션을 보내려면, Punchh 기프팅 캠페인에 [커스텀 Punchh Segment]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh#step-3-create-punchh-webhook-in-braze)가 필요합니다.

이 오퍼를 받을 사용자 Segment를 Braze에서 생성하는 것은 Punchh 내에서 사용할 수 없는 속성을 사용할 때만 권장됩니다. 그렇지 않으면 Punchh 세분화를 사용할 수 있으며, Braze 메시징 캠페인은 사용자가 리워드를 받을 때(Punchh에 의해 트리거되는 리워드 이벤트) 트리거되는 액션 기반 캠페인으로 생성됩니다.

Punchh 구성 요건:
- 캠페인: 대량 오퍼
- Segment: 커스텀 목록 또는 고객 선택
- 리워드: 고객 선택

**세분화 및 기프팅에 Punchh를 사용하고 메시징에 Braze를 사용하는 경우:**<br>
예를 들어, Punchh 내에서 구성 가능한 Segment에 $2 할인 리워드가 Braze를 통해 메시지와 함께 전송됩니다.<br>
![사용자 Segment를 Punchh에서 구성할 수 있으며, 사용자는 Punchh 대량 오퍼 캠페인을 통해 기프트를 받습니다. 다음으로 리워드 이벤트가 트리거되고 Braze 메시징 캠페인이 트리거됩니다.]({% image_buster /assets/img/punchh/usecase6.png %}){: style="max-width:80%;"}

**Braze 세분화 및 메시징을 사용하고 기프팅에 Punchh를 사용하는 경우:**<br>
예를 들어, Punchh에서 사용할 수 없는 속성을 가진 Segment에 $2 할인 리워드와 메시지가 전송됩니다.<br>
![사용자 Segment를 Braze에서 구성한 후 Braze-to-Braze Segment에서 메시지를 보낼 수 있습니다. 다음으로 Segment 및 사용자 ID가 포함된 Braze 웹훅을 통해 사용자가 Punchh 커스텀 Segment로 전송됩니다. 이후 사용자는 커스텀 Segment가 적용된 Punchh 대량 오퍼 캠페인을 통해 기프트를 받습니다. 이후 리워드 이벤트가 트리거됩니다.]({% image_buster /assets/img/punchh/usecase5.png %}){: style="max-width:80%;"}

**Braze 세분화를 사용하고 기프팅 또는 메시징, 또는 둘 다에 Punchh를 사용하는 경우:**<br>
예를 들어, Punchh에서 사용할 수 없는 속성을 가진 Segment에 $2 할인 리워드가 전송되지만 메시징이 필요하지 않거나, Punchh를 통해 메시지를 보낼 수 있습니다(모든 게스트가 Punchh에 존재해야 합니다).<br>
![사용자 Segment를 Braze에서 구성한 후 Segment 및 사용자 ID가 포함된 Braze 웹훅을 통해 사용자가 Punchh 커스텀 Segment로 전송됩니다. 이후 사용자는 커스텀 Segment가 적용된 Punchh 대량 오퍼 캠페인을 통해 기프트를 받습니다. 이후 리워드 이벤트가 트리거됩니다.]({% image_buster /assets/img/punchh/usecase4.png %})

{% endtab %}
{% tab 반복 대량 오퍼 %}
#### 반복 대량 오퍼 캠페인 {#recurring-mass-offer-campaign}

기프팅을 위한 반복 대량 오퍼 캠페인을 활용할 때, Punchh 내에서 대량 오퍼 캠페인을 구성하고 Braze에서 메시징 캠페인을 설정해야 합니다. 고객이 Braze 세분화를 사용하려면(Punchh 내에서 사용할 수 없는 속성을 활용하는 경우에만 권장) Punchh 커스텀 Segment가 필요합니다. 그렇지 않으면 Punchh 세분화를 사용할 수 있으며, Braze 메시징 캠페인은 리워드 이벤트를 기반으로 트리거됩니다.

Punchh 구성 요건:
- 캠페인: 반복 대량 오퍼
- Segment: 커스텀 목록 또는 고객 선택
- 리워드: 고객 선택
고려 사항:
- 캠페인 ID와 캠페인 이름은 이벤트의 이벤트 속성으로 Braze에 전송됩니다. 캠페인을 수신하는 오디언스를 추가로 필터링하기 위해 Braze에서 Punchh 캠페인 식별자를 사용하려면, 캠페인 ID가 매일 변경되므로 캠페인 이름을 사용해야 합니다.

{% endtab %}
{% tab 체크인 후 오퍼(알림 포함) %}
#### 알림이 포함된 체크인 후 오퍼 캠페인 {#post-check-in-offer-campaign-with-notification}

체크인 후 오퍼 캠페인을 활용할 때, Braze가 기프팅에 대한 알림을 보내고, 게스트가 체크인하면 Punchh 체크인 후 캠페인에서 기프트를 받게 됩니다. 따라서 Punchh 내에서 체크인 후 오퍼 캠페인을 구성하고 Braze에서 메시징 캠페인을 설정해야 합니다(고객에게 캠페인을 알리는 경우).

Punchh 구성 요건:
- 캠페인: 체크인 후 오퍼
- Segment: 커스텀 목록
- 리워드: 고객 선택

예를 들어, Punchh에서 사용할 수 없는 속성을 가진 Segment에 이번 주말 방문 시 더블 포인트를 알리는 이메일을 보냅니다. Punchh는 조건에 부합하는 체크인 후 해당 Segment에 포인트를 기프팅하고, Braze에서 선택적 메시지를 전송합니다.

![사용자 Segment가 Braze에서 구성되고 Braze 체크인 후 캠페인에서 메시지가 전송됩니다. 다음으로 조건에 부합하는 사용자가 Segment 및 사용자 ID가 포함된 Braze 웹훅을 통해 Punchh 커스텀 Segment로 전송됩니다. 마지막으로 커스텀 Segment의 조건에 부합하는 사용자가 체크인하고 체크인 후 캠페인을 통해 기프트와 선택적 메시지를 받습니다.]({% image_buster /assets/img/punchh/update7.png %})

{% endtab %}
{% tab 체크인 후 오퍼(알림 미포함) %}
#### 알림이 없는 체크인 후 오퍼 캠페인 {#post-check-in-offer-campaign-without-notification}

고객에게 먼저 알리지 않는 체크인 후 오퍼 캠페인을 활용할 때, 캠페인은 기프팅(선택적 메시징)을 수행하고 Braze 내에서 알림을 트리거합니다. 따라서 Punchh 내에서 체크인 후 오퍼 캠페인을 구성해야 하지만, 커스텀 목록은 필요하지 않습니다. 대신 Punchh 내에서 원하는 Segment를 선택할 수 있습니다.

Punchh 구성 요건:
- 캠페인: 체크인 후 오퍼
- Segment: 고객 선택
- 리워드: 고객 선택

예를 들어, Punchh에서 사용 가능한 Segment에 방문에 감사하고 다음 방문 시 $2 할인 리워드를 제공하는 서프라이즈 앤 딜라이트 Braze 캠페인이 전송됩니다.

![조건에 부합하는 사용자 Segment를 Punchh 내에서 구성할 수 있으며, 조건에 부합하는 사용자가 체크인하고 Punchh 체크인 후 캠페인을 통해 기프트를 받습니다. 이후 리워드 이벤트가 트리거되고 리워드를 알리는 리콜 메시지가 Braze에서 전송됩니다.]({% image_buster /assets/img/punchh/usecase2.png %})

{% endtab %}
{% tab 기념일 %}
#### 기념일 캠페인 {#anniversary-campaign}

기념일 캠페인을 활용할 때, 사용자는 먼저 Punchh 캠페인에서 기념일 기프트를 받게 됩니다. 이 기프팅(리워드 이벤트)은 사용자에게 기프팅을 알리는 Braze 내 메시징 캠페인을 트리거합니다. 따라서 커스텀 목록은 필요하지 않습니다. 대신 Punchh 내에서 Segment와 기념일 설정을 선택할 수 있습니다.

Punchh 구성 요건:
- 캠페인: 기념일 캠페인
- Segment: 고객 선택
- 리워드: 고객 선택
고려 사항:
- 가입 월 기프팅
- 유효 기간(생일 리워드의 유효 기간은 얼마인가?)
- 반복 캠페인, 스케줄 필요

![Punchh 내에서 선택적 Segment를 생성할 수 있으며, 조건에 부합하는 사용자가 Punchh 기념일 캠페인을 통해 리워드를 받습니다. 이후 리워드 이벤트가 트리거되고 리워드를 알리는 리콜 메시지가 Braze에서 전송됩니다.]({% image_buster /assets/img/punchh/usecase1.png %})

{% endtab %}
{% tab 리콜 %}
#### 리콜 캠페인 {#recall-campaign}

비활성 사용자를 타겟팅할 때 리콜 캠페인을 사용할 수 있습니다. 고객은 Punchh 내에서 Segment와 캠페인을 생성하되 메시징에는 Braze를 사용할 수 있습니다.

Braze에서 생성된 세분화를 사용하려면, 비활성을 기반으로 한 [커스텀 Punchh Segment]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh#step-3-create-punchh-webhook-in-braze)를 반복 대량 오퍼 캠페인에 연결할 수 있습니다.

Punchh 구성 요건:
- 캠페인: 리콜 캠페인
- Segment: 고객 선택
- 리워드: 고객 선택
고려 사항:
- 캠페인은 스케줄에 따라 실행됩니다

![Punchh 내에서 선택적 Segment를 생성할 수 있으며, 조건에 부합하는 사용자가 Punchh 리콜 캠페인을 통해 리워드를 받습니다. 이후 리워드 이벤트가 트리거되고 리워드를 알리는 리콜 메시지가 Braze에서 전송됩니다.]({% image_buster /assets/img/punchh/usecase.png %})

{% endtab %}
{% endtabs %}