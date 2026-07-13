---
nav_title: SessionM
article_title: SessionM
description: "이 참조 문서에서는 고객 참여 및 로열티 플랫폼인 Braze와 SessionM 간의 파트너십에 대해 설명합니다."
alias: /partners/sessionm/
page_type: partner
search_tag: Partner
---

# SessionM 로열티 플랫폼 {#sessionm-loyalty-platform}

> [SessionM](https://sessionm.com/)은 Capillary Technologies의 일부로, 마케터가 타겟팅된 아웃리치를 통해 인게이지먼트와 수익성을 높일 수 있도록 캠페인 관리 기능과 로열티 관리 솔루션을 제공하는 고객 참여 및 로열티 플랫폼입니다.

## 필수 조건 {#prerequisites}

| 소스 | 요구 사항 | 설명 |
| --- | --- | --- |
| Braze | Braze REST API 키 | `trigger_send` 권한이 있는 Braze REST API 키입니다. Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze | Braze REST 엔드포인트 | REST 엔드포인트 URL입니다. 엔드포인트는 [인스턴스]({{site.baseurl}}/api/basics#endpoints)의 Braze URL에 따라 달라집니다. |
| Braze 및 SessionM | 일치하는 식별자 | 통합을 사용하려면 SessionM과 Braze 모두 각 플랫폼에서 사용하는 식별자의 기록을 보유하고 있어야 합니다. `user_id`에 대한 참조는 SessionM에서 프로필 생성 시 생성된 SessionM의 사용자 식별자에 해당합니다. |
| SessionM | SessionM 계정 | 이 파트너십을 활용하려면 SessionM 계정이 필요합니다. |
| SessionM | SessionM Core REST 엔드포인트 | 엔드포인트는 인스턴스의 SessionM URL에 따라 달라집니다. SessionM 대시보드의 **Digital Properties**에서 생성할 수 있습니다. |
| SessionM | SessionM Core REST API 키 | 인스턴스 및 Braze 통합과 연결된 SessionM API 키입니다. 이 키는 태그를 포함한 모든 코어 기반 호출에 사용할 수 있습니다. SessionM 대시보드의 **Digital Properties**에서 생성할 수 있습니다. |
| SessionM | SessionM Core REST API 시크릿 | 인스턴스 및 Braze 통합과 연결된 SessionM API 시크릿입니다. 이 키는 태그를 포함한 모든 코어 기반 호출에 사용할 수 있습니다. SessionM 대시보드의 **Digital Properties**에서 생성할 수 있습니다. |
| SessionM | SessionM Connect REST 엔드포인트 | 엔드포인트는 인스턴스의 SessionM URL에 따라 달라집니다. SessionM 기술 계정 매니저 또는 전달 팀에 문의하여 제공받으세요. |
| SessionM | SessionM Connect REST 승인 문자열 | 인스턴스와 연결된 SessionM Connect 기본 승인 문자열입니다. 이 인증 문자열은 get_user_offers를 포함한 모든 연결 기반 호출에 사용할 수 있습니다. SessionM 기술 계정 매니저 또는 전달 팀에 문의하여 제공받으세요. |
| SessionM | SessionM Connect REST 리테일러 ID | 인스턴스와 연결된 특정 고객에 대한 고유 GUID 식별자입니다. SessionM 기술 계정 매니저 또는 전달 팀에 문의하여 제공받으세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="필수 조건" }

## 사용 사례 {#use-cases}

다음 사용 사례는 SessionM과 Braze 통합을 활용하는 몇 가지 방법을 보여줍니다.

- 모든 로열티, 고객 관리 및 메시징 플랫폼의 데이터를 통합하는 세분화를 생성합니다.
- 강력한 세분화를 사용하여 특정 사용자 집합을 오퍼 및 프로모션으로 타겟팅합니다.
- 메시지 발송 시 최신 사용자, 오퍼 및 로열티 정보를 활용합니다.
- 프로모션 및 로열티 활동의 진행 상황과 완료에 대한 상세한 알림을 고객에게 제공합니다.
- 새로운 오퍼가 부여되면 고객에게 알리고 오퍼 세부 정보를 제공합니다.

## SessionM과 Braze 통합 {#integrating-sessionm-with-braze}

### 1단계: Braze에서 Segment 생성 {#step-1-create-a-segment-in-braze}

Braze에서 SessionM 프로모션 및 오퍼로 타겟팅할 사용자 Segment를 생성합니다.

!["커스텀 속성" 필터가 선택된 Segment 빌더.]({% image_buster /assets/img/sessionm/CreateSegment.png %})

### 2단계: Braze Segment를 SessionM으로 가져오기 {#step-2-import-braze-segments-into-sessionm}

#### 옵션 1: SessionM 태그 엔드포인트로 내보내기(권장) {#option-1-export-to-the-sessionm-tag-endpoint-recommended}

먼저 Braze에서 웹훅 Campaign을 생성하고 웹훅 URL을 {% raw %}`{{endpoint_core}}/priv/v1/apps/{{appkey_core}}/users/{{${user_id}}}/tags`{% endraw %}로 설정합니다. Liquid를 사용하여 URL 내에서 `user_id`를 정의합니다.

원시 텍스트 **Request Body**를 사용하여 SessionM의 고객 프로필에 추가할 원하는 태그와 원하는 TTL을 포함하도록 웹훅 본문을 작성합니다. 예를 들면 다음과 같습니다:

 ```
 {
   "tags":[
    "braze_test"
   ],
   "ttl":2592000
}
 ```

![Braze Campaign 트리거 설정을 위한 JSON 페이로드가 포함된 SessionM 웹훅 작성기.]({% image_buster /assets/img/sessionm/SessionMWebhookComposer.png %}){: style="max-width:85%;"}

**Settings** 탭에서 각 요청 헤더 필드에 대한 키-값 페어를 추가합니다:
    - 키 `Content-Type`을 생성하고 해당 값을 `application/json`으로 설정합니다.
    - 키 `Authorization`을 생성하고 해당 값을 `Basic YOUR-ENCODED-STRING-KEY`로 설정합니다. 엔드포인트의 인코딩된 문자열 키는 SessionM 팀에 문의하세요.

![웹훅 설정.]({% image_buster /assets/img/sessionm/SessionMWebhookSettings.png %}){: style="max-width:85%;"}

전달을 스케줄하고, **타겟 오디언스**를 [이전에 생성한](#step-1-create-a-segment-in-braze) Segment로 설정한 다음 Campaign을 시작합니다.

{% alert important %}
이 프로세스는 Postman과 같은 API 클라이언트를 통해 [SessionM 태그 엔드포인트](https://docs.sessionm.com/developer/APIs/Core/Customers/customers_tags.htm#create-or-increment-a-customer-tag)에 직접 요청하여 고객, 태그 이름 및 호출 내 각 사용자의 TTL을 지정하는 방식으로도 수행할 수 있습니다(호출당 단일 사용자).
<br><br>
다음 예시 요청은 cURL을 사용합니다.

{% raw %}
```bash
curl --location -g --request POST '{{endpoint_core}}/priv/v1/apps/{{apikey_core}}/users/{{user_id}}/tags' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic {{base64_encoded_string}}' \
--data-raw '{
"tags":[
"tagname1",
"tagname2"
],
"ttl":20000
}'
```
{% endraw %}
{% endalert %}

#### 옵션 2: CSV 가져오기 {#option-2-csv-import}

Braze 세그먼터를 사용하여 Braze Segment를 내보내고, 태그할 고객, 태그 이름 및 파일 내 각 사용자의 TTL이 포함된 CSV 파일을 SessionM에 제공합니다.

## Braze를 통한 실시간 오퍼 월렛 조회 {#retrieving-real-time-offer-wallet-with-braze}

SessionM과 Braze를 통합하면 연결된 콘텐츠를 사용하여 메시지 발송 시점에 SessionM 사용자 데이터를 실시간으로 가져올 수 있으므로, 만료되었거나 이미 사용된 로열티 오퍼를 고객에게 전달하는 위험을 제거할 수 있습니다.

다음 예시는 연결된 콘텐츠를 사용하여 오퍼 월렛 데이터를 메시지에 템플릿화하는 방법을 보여줍니다. 그러나 연결된 콘텐츠는 SessionM의 모든 Connect 엔드포인트에서 사용할 수 있습니다.

### 1단계: SessionM에서 오퍼 발행 {#step-1-issue-offer-in-sessionm}

SessionM은 구성 가능한 여러 내부 레버를 통해 고객에게 오퍼를 발행합니다. 발행된 후 오퍼는 SessionM에서 "오퍼 월렛"이라고 부르는 상태로 이동합니다.

고객은 필요한 동작을 완료하거나 타겟팅 조건을 충족해야 하며, 그러면 SessionM 내에서 오퍼가 발행됩니다.

그런 다음 SessionM은 발행된 상태로 고객의 월렛에 오퍼를 추가합니다.

### 2단계: SessionM 오퍼 월렛 API 호출 {#step-2-call-sessionm-offer-wallet-api}

SessionM 오퍼가 포함된 Campaign 또는 캔버스 단계에서 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)를 사용하여 [SessionM `get_user_offers` 엔드포인트](https://domains-connecteast1.ent-sessionm.com/offers/swagger/ui/index#!/InfoV232583210323232323232323232323232This32API32allows32for32the32querying32of32information32about32offers32in32a32read45only32fashion4610323232323232323232323232May32be32initiated32by32the32dashboard32or32the32mobile32app4610323232323232323232323232/InfoV2_GetUserOffers/)에 API 호출을 수행합니다.

연결된 콘텐츠 요청에서 사용자의 SessionM `user_id`와 `retailer_id`를 지정하여 고객이 월렛에 보유한 활성 오퍼의 전체 목록을 조회합니다. 이 엔드포인트에 대한 각 요청에는 단일 사용자만 포함할 수 있습니다. 연결된 콘텐츠 호출의 기본 승인 헤더에 사용할 인코딩된 문자열 키는 SessionM 팀에 문의하세요.

요청 본문에서 `culture`의 기본값은 `en-US`이지만, 다국어 SessionM 오퍼를 위해 Liquid를 사용하여 사용자의 언어를 템플릿화할 수 있습니다(예: {% raw %}`"culture":"{{${language}}}"`{% endraw %} 사용).

{% raw %}
```
{% capture postbody %}
{"retailer_id":"YOUR-RETAIL-ID","user_id":"{{${user_id}}}","skip":0,"take":1000,"include_pending_extended_data":false,"culture":"en-US"}
{% endcapture %}

{% connected_content
     {{endpoint_connect}}/offers/api/2.0/offers/get_user_offers
:method post
:headers {
       "Content-Type": "application/json",
       "Authorization": "Basic YOUR-BASE64-ENCODED-KEY"
  }
     :body {{postbody}}
     :save wallet
%}
```
{% endraw %}

### 3단계: Braze 메시징에 오퍼 월렛 채우기 {#step-3-populate-offer-wallet-to-braze-messaging}

엔드포인트에 요청이 이루어지면 SessionM은 발행된 상태의 전체 오퍼 목록과 각 오퍼의 전체 세부 정보를 반환합니다. 다음은 반환된 응답의 예시입니다:

{% raw %}
```
{
    "status": "ok",
    "payload": {
      "user": {
        "opted_in": false,
        "activated": false,
        ...
      },
      "user_id": "00000000-0000-0000-0000-000000000000",
      "user_offers": [
        {
          "offer_id": "1a2b3324-1da6-4e49-b921-afc386dabb60",
          "offer_group_id": "00000000-0000-0000-0000-000000000000",
          "offer_type": "manual_fulfillment",
          ...
        }
      ],
      "total_records": 1,
      "offer_groups": [
        {
          "id": "00000000-0000-0000-0000-000000000000",
          "name": "All Offers",
          "sort_order": 0
        }
      ],
      "offer_categories": [
        {
          "id": "9a82f973-aae6-4e10-839b-7117a852cf9e",
          "name": "All Offers",
          "sort_order": 0
        }
      ],
      "total_points": 1000,
      "available_points": 100
    }
}
```
{% endraw %}

Liquid 점 표기법을 사용하여 메시지에 채울 수 있습니다. 예를 들어, 결과 `offer_id`로 메시지를 개인화하려면 {% raw %}`{{wallet.payload.available_points}}`{% endraw %}를 사용하여 반환 페이로드를 활용할 수 있으며, 이는 `100`을 반환합니다.

{% alert note %}
이것은 개별 API입니다. 500명 이상의 사용자에게 일괄 발송하려는 경우 SessionM 계정 팀에 문의하여 통합에 대량 데이터를 포함하는 방법을 확인하세요.
{% endalert %}

## 트리거 메시징 설정 {#setting-up-triggered-messaging}

SessionM과 Braze 간의 통합을 통해 고객 프로필 데이터, 오퍼 세부 정보 및 포인트 잔액을 메시징에 동적으로 채우고 동작 시점에 실시간으로 고객에게 발송할 수 있습니다.

### 1단계: SessionM 전달 팀이 템플릿 구성 {#step-1-sessionm-delivery-team-configures-templates}

SessionM 전달 팀과 협력하여 트리거 메시징에 사용할 템플릿을 개발합니다. SessionM은 고객 프로필 데이터, 오퍼 세부 정보 및 포인트 잔액을 메시징에 삽입하고 Braze에서 실시간 고객 메시징을 위해 트리거합니다.

SessionM의 모든 템플릿에 포함된 표준 필드는 다음과 같습니다:
- `canvas_id`
- `campaign_id`
- `broadcast flag`
- `customer identifier`
- `email address`

{% alert note %}
`broadcast flag`를 `true`로 설정하면 Braze에서 Campaign 또는 Canvas가 타겟팅하는 전체 Segment에 메시지가 발송됩니다.
{% endalert %}

특정 요구 사항에 따라 추가 필드를 구성할 수 있습니다:

- **오퍼 데이터:** `offer_id`, `offer title`, `user offer id`, `description`, `terms and conditions`, `logo`, `pos discount id`, `expiration date`
- **포인트 보상 데이터:** `point award amount`, `point account name`
- **이벤트 트리거 데이터:** 트리거/발송 웹훅 성과를 활용하는 트리거 이벤트의 모든 데이터
- **캠페인별 데이터:** `campaign runtime`, `campaign_id`, `campaign name`, `campaign custom data`

추가 필드는 메시지를 개인화하기 위해 `trigger_properties`로 Braze에 전송됩니다.

### 2단계: Braze Campaign 또는 Canvas 생성 {#step-2-create-a-braze-campaign-or-canvas}

SessionM에 의해 트리거될 API 트리거 Campaign 또는 Canvas를 Braze에서 생성합니다. `offer_id` 또는 `offer title`과 같은 추가 필드가 구성된 경우, Liquid(예: {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %})를 사용하여 메시징에 개인화된 필드를 추가합니다.

![API 트리거 속성.]({% image_buster /assets/img/sessionm/apiTriggerProperties.png %})

**배신 스케줄** 탭에서 Campaign 또는 Canvas ID를 기록해 두세요. 이 ID는 SessionM 캠페인 **Advanced Settings**에 추가됩니다.

![API 트리거 Campaign.]({% image_buster /assets/img/sessionm/apiTriggerCampaign.png %})

Campaign 또는 Canvas 세부 정보를 완료하고 **시작**을 선택합니다.

### 3단계: SessionM 프로모션 또는 메시징 캠페인 생성 {#step-3-create-a-sessionm-promotional-or-messaging-campaign}

다음으로 SessionM에서 캠페인을 생성합니다.

![SessionM 캠페인 생성.]({% image_buster /assets/img/sessionm/SessionMCampaignCreation.png %})

SessionM 캠페인의 고급 설정을 업데이트하여 `braze_campaign_id` 또는 `braze_canvas_id`가 포함된 다음 JSON 페이로드를 포함합니다.

{% raw %}
```
{
"braze_campaign_id": "{{CAMPAIGN ID}}",
"braze_canvas_id": "{{CANVAS ID}}",
}
```
{% endraw %}

![SessionM 고급 설정.]({% image_buster /assets/img/sessionm/SessionMAdvancedSettings.png %}){: style="max-width:85%;"}

원하는 스케줄 또는 동작에 대한 메시지 트리거를 생성합니다. 그런 다음 **External Message** 메뉴에서 **Braze Messaging Variant**를 **Messaging Variant**로 선택하여 템플릿을 사용합니다.

![SessionM 외부 메시지.]({% image_buster /assets/img/sessionm/SessionMExternalMessage.png %})

이 템플릿은 관련 정적 및 동적 속성을 가져오고 Braze 엔드포인트를 호출합니다.

![SessionM Braze 템플릿.]({% image_buster /assets/img/sessionm/SessionMBrazeTemplate.png %}){: style="max-width:85%;"}