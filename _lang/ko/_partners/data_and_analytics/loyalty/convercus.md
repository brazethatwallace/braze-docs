---
nav_title: Convercus
article_title: Convercus
description: "이 참조 문서에서는 Braze와 Convercus 간의 파트너십을 설명합니다. Convercus는 로열티 및 쿠폰 플랫폼으로, 실시간 로열티 데이터로 Braze를 강화하고 Braze Campaigns가 Convercus에서 로열티 동작을 트리거할 수 있도록 합니다."
page_type: partner
search_tag: Partner
---

# Convercus

> [Convercus](https://www.convercus.com/en)는 옴니채널 로열티 프로그램과 개인화된 쿠폰 캠페인을 통해 브랜드와 소매업체가 고객 방문 빈도, 장바구니 가치, 재구매율을 높일 수 있도록 돕는 SaaS 로열티 및 쿠폰 플랫폼입니다.

_이 통합은 Convercus에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Convercus의 통합은 양방향으로 작동합니다. 로열티 데이터는 커스텀 속성, 커스텀 이벤트, 구매 데이터로 실시간으로 Braze에 유입되며, Braze Canvases와 Campaigns는 웹훅을 통해 Convercus에서 로열티 액션을 트리거할 수 있습니다. 동기화된 회원 등급, 포인트 잔액, 구매 내역, 쿠폰 활동을 Segments, Liquid, 연결된 콘텐츠에서 활용할 수 있습니다. Braze 여정에서 쿠폰을 할당하고, 포인트 트랜잭션을 예약·적립·사용하며, Convercus에서 이메일 가입 설정을 업데이트할 수도 있습니다.

Convercus가 통합을 호스팅하므로 추가 인프라를 설치할 필요가 없습니다. 대부분의 로열티 커넥터가 데이터를 한 방향으로만 전송하는 반면, Convercus는 루프를 완성합니다. Braze에서 로열티 이벤트에 반응하고, Convercus에서 액션을 수행한 다음, 그 결과를 다시 Braze에서 측정할 수 있습니다.

## 사용 사례 {#use-cases}

* **등급 상향 축하:** 회원이 Convercus에서 로열티 등급이 올라가면, 환영 메시지, 등급 전용 혜택, 회원의 새로운 등급 및 포인트 잔액이 포함된 개인화된 Braze Canvas를 트리거합니다.
* **생일 및 마일스톤 보너스:** Braze 여정에서 회원의 생일이나 기념일에 Convercus에 보너스 포인트를 적립한 다음, 새로운 잔액을 확인하는 축하 메시지를 보냅니다.
* **이탈 회원 윈백:** 비활성 회원의 경우, Braze가 웹훅을 통해 Convercus에서 개인화된 쿠폰을 할당하고 이메일, 푸시, In-App Messages를 통해 전달합니다.
* **메시지 내 실시간 포인트 잔액:** 연결된 콘텐츠를 사용하여 회원의 실시간 포인트 잔액을 Braze Liquid로 가져와 "다음 리워드까지 X 포인트 남았습니다"와 같은 메시지 흐름을 구성합니다.

## 사전 요구 사항 {#prerequisites}

시작하기 전에 다음이 필요합니다:

| 사전 요구 사항 | 설명 |
| --- | --- |
| Convercus 계정 | 활성 Convercus 프로그램. 아직 고객이 아닌 경우 Convercus 계정 매니저에게 문의하세요. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. Braze 대시보드에서 **설정** > **API 키**로 이동하여 이 키를 생성하세요. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/api/basics#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 다릅니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사전 요구 사항" }

시스템 간에 일관된 사용자 식별자가 필요합니다. Braze에서 `external_id`(또는 선택한 식별자 유형)로 사용되는 값이 Convercus의 해당 회원 식별자와 일치해야 합니다. 그렇지 않으면 이벤트가 올바른 프로필에 귀속되지 않습니다.

## 통합 {#integration}

### 1단계: Convercus Selfservice에서 Braze 구성하기 {#step-1-configure-braze-in-convercus-selfservice}

Convercus Selfservice(고객용 관리 UI—Convercus 계정 매니저가 제공하는 URL로 열 수 있습니다)에서 Braze에 연결하려는 프로그램을 열고 **Braze integration card**를 사용하여 다음을 수행합니다.

1. 통합 양식을 작성하여 Braze 연결을 구성합니다.

   | 필드 | 설명 |
   | --- | --- |
   | `apiKey` | Braze REST API 키(`users.track` 권한 포함). |
   | `apiEndpoint` | Braze REST 엔드포인트(예: `https://rest.iad-01.braze.com`). |
   | 식별자 유형 | `external_id` 또는 `user_alias`. Convercus 회원을 Braze 고객 프로필과 매칭하는 방식을 결정합니다. |
   | `defaultOptins` | 프로그램의 옵트인 채널(`membershipOptins`에서 가져옴)을 다중 선택합니다. 요청에 `optins`가 포함되지 않은 경우 이메일 가입 웹훅의 기본값으로 사용됩니다. 하나 이상 선택될 때까지 Braze 구성은 불완전한 것으로 간주됩니다. |
   {: .reset-td-br-1 .reset-td-br-2 aria-label="1단계: Convercus Selfservice에서 Braze 구성하기" }

2. 인바운드 호출용 API 키를 생성합니다. 프로그램별 `X-Convercus-Key` 자격 증명을 생성합니다. 원시 키는 생성 시 한 번만 표시되며 `cvc_` 접두사가 붙습니다(형식: `cvc_<base64url>`). 2단계에서 웹훅 Campaigns와 연결된 콘텐츠 블록을 구성할 때 Braze에 이 키를 저장합니다. 키는 동일한 카드에서 언제든지 폐기할 수 있으며, 폐기는 즉시 적용됩니다.

Braze 연결을 저장하면 Convercus는 즉시 해당 프로그램의 로열티 이벤트를 Braze로 스트리밍하기 시작합니다. 추가 인프라 설정은 필요하지 않습니다.

{% alert note %}
각 Convercus 프로그램은 독립적으로 구성됩니다. 단일 Convercus 테넌트는 서로 다른 프로그램을 서로 다른 Braze 워크스페이스에 연결할 수 있으며, 각각 고유한 API 키를 사용합니다.
{% endalert %}

### 2단계: Braze에서 웹훅 구성하기 {#step-2-configure-webhooks-in-braze}

Canvas 또는 Campaign에서 Convercus 작업을 트리거하려면, Convercus 통합 서비스를 호출하는 Braze 웹훅 작업을 생성합니다. 모든 요청에는 다음 헤더가 포함되어야 합니다.

- `X-Convercus-Key: cvc_…` - 1단계에서 생성한 API 키.
- `Content-Type: application/json`

모든 엔드포인트는 기본 URL `<SERVICE_HOST>/v1/programs/{programId}` 아래에 있습니다. `<SERVICE_HOST>`를 Convercus 계정 매니저가 제공한 호스트로, `{programId}`를 Convercus 프로그램 ID로 대체합니다.

| 작업 | 엔드포인트 |
| --- | --- |
| 회원에게 쿠폰 할당 | `POST /campaigns/{couponId}/assign` — `{ "couponCode": "..." }`를 반환합니다. |
| 여러 회원에게 쿠폰 할당 | `POST /campaigns/{couponId}/assign/batch` — 한 번의 호출로 최대 500명의 회원 처리 가능. 본문에 선택적으로 `valid_from` / `valid_to`를 포함할 수 있습니다. `{ "batchId": "..." }`를 반환합니다. |
| 적립/차감 포인트 기록 | `POST /members/{accountId}/bookings` — 회원 계정에 `EARNBOOKING` 또는 `BURNBOOKING`을 생성합니다. `{ "bookingId": "..." }`를 반환합니다. |
| 이메일 가입 환경설정 동기화 | `POST /subscriptions/email` — 회원의 옵트인을 `allowed` 또는 `declined`로 설정합니다. 옵트인 채널은 요청 `optins` > `defaultOptins` 순으로 결정됩니다. `200`(모두 성공), `207`(부분 성공 — `succeeded` / `failed` 참조), 또는 `400`(알 수 없는 옵트인 또는 구성되지 않음)을 반환합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="2단계: Braze에서 웹훅 구성하기" }

예시 — 회원에게 쿠폰 할당:

{% raw %}
```text
POST <SERVICE_HOST>/v1/programs/{programId}/campaigns/{couponId}/assign
X-Convercus-Key: cvc_…
Content-Type: application/json

{
  "account_id": "{{custom_attribute.${convercus_account_id}}}",
  "braze_campaign_id": "{{campaign.${api_id}}}"
}
```
{% endraw %}

다른 작업도 동일한 패턴을 따르며, 엔드포인트와 본문만 변경됩니다. 예를 들어, 포인트 기록은 `/members/{accountId}/bookings`에 `booking_type`(`EARNBOOKING` 또는 `BURNBOOKING`), `booking_type_code`, `points`, `reason`을 포함하여 POST하고, 이메일 가입 웹훅은 `/subscriptions/email`에 `account_id`와 `status`(`allowed` 또는 `declined`)를 포함하여 POST합니다.

#### 오류 응답 및 재시도 {#error-responses-and-retries}

| 상태 | 의미 |
| --- | --- |
| `200` | 성공. |
| `207` | Multi-Status — 이메일 가입 웹훅에서만 해당되며, 일부 멤버십은 업데이트되고 나머지는 실패한 경우입니다. |
| `400` | 요청 본문이 유효성 검사에 실패했습니다. |
| `401` | `X-Convercus-Key`가 누락되었거나 유효하지 않습니다. |
| `5xx` | 업스트림 Convercus 호출이 실패했습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="오류 응답 및 재시도" }

{% alert warning %}
5xx 응답은 성공 여부를 확인하지 않고 재시도하면 안전하지 않습니다. 이 작업들은 멱등성이 보장되지 않으며, 재시도 시 쿠폰이 이중 할당되거나 포인트가 이중 적립될 수 있습니다. 이 웹훅에 대해 Braze의 5xx 자동 재시도를 비활성화하거나, 최대 재시도 횟수를 매우 낮게 설정하세요.
{% endalert %}

### 3단계: Braze에서 데이터 확인하기 {#step-3-verify-data-in-braze}

1. Convercus에서 로열티 이벤트를 트리거합니다. 예를 들어 상태 레벨 변경, 포인트 트랜잭션 또는 쿠폰 사용 등이 있습니다.
2. Braze에서 해당 사용자를 열고 예상되는 커스텀 속성, 커스텀 이벤트 또는 구매가 프로필에 나타나는지 확인합니다. 사용자는 `external_id`(또는 1단계에서 선택한 식별자 유형)로 매칭됩니다.
3. 반대 방향을 확인하려면, 2단계의 웹훅 중 하나를 호출하는 Braze 테스트 전송을 실행하고 Convercus에서 해당 작업(쿠폰 할당, 포인트 기록 또는 가입 업데이트)을 확인합니다.

## Braze에서 Convercus 사용하기 {#use-convercus-with-braze}

### 1단계: 동기화된 로열티 데이터로 메시지 개인화하기 {#step-1-personalize-messages-with-synced-loyalty-data}

통합이 활성화되면, Convercus 이벤트는 [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) 엔드포인트를 통해 Braze의 각 고객 프로필에 전달되며, 다른 기본 데이터와 동일하게 사용할 수 있습니다.

1. 로열티 커스텀 속성(예: `convercus_status_level`, `convercus_balance`)을 **Segments**에서 사용하여 특정 등급 보유자, 높은 잔액 회원 또는 최근 등급 하락 사용자를 타겟팅합니다.
2. 커스텀 이벤트(예: `convercus_status_level_changed`, 쿠폰 및 멤버십 이벤트)를 Canvas의 **트리거 단계**로 사용하거나 재참여 캠페인의 필터로 사용합니다.
3. 인메시지 개인화(제목란, 본문 카피, 푸시 제목)를 위해 **Liquid**에서 이러한 필드를 참조합니다.
4. Convercus에서 스트리밍되는 `purchase` 이벤트를 사용하여 제품 기반 여정(보충, 카테고리 업셀, 구매 후 리뷰 요청)을 구동합니다.

#### 커스텀 속성 {#custom-attributes}

| 속성 | 설명 |
| --- | --- |
| `convercus_account_id` | 회원의 Convercus 계정 ID로, Convercus 프로그램/Braze 워크스페이스 내에서 고유합니다. |
| `convercus_user_id` | 여러 Convercus 프로그램에 걸쳐 기본 사용자를 식별하는 Convercus 사용자 ID입니다. |
| `convercus_partner_id` | 해당 회원이 등록한 Convercus 파트너(가맹점/브랜드)의 식별자입니다. 제휴 프로그램에서 세분화에 유용합니다. |
| `convercus_member_role` | 로열티 프로그램 내에서 회원의 역할입니다. |
| `convercus_status_level` | 회원의 현재 등급 또는 상태 레벨입니다. |
| `convercus_balance` | 회원의 현재 `points`, `lockedPoints`, `statusPoints`를 포함하는 객체입니다. |
| `email_subscribe` | Convercus 옵트인에서 파생된 이메일 가입 상태(`opted_in`, `subscribed`, 또는 `unsubscribed`)입니다. |
| `push_subscribe` | Convercus 푸시 토큰 이벤트에서 파생된 푸시 가입 상태(`opted_in` 또는 `unsubscribed`)입니다. |
| 표준 프로필 필드 | `email`, `phone`, `first_name`, `last_name`, `dob`, `gender`, `home_city`, `country`. |
| 커스텀 사용자 속성 | Convercus 사용자 객체에 정의된 모든 커스텀 속성은 Braze 커스텀 속성으로 전달됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="커스텀 속성" }

{% alert note %}
Braze 워크스페이스 내에서 회원은 `convercus_account_id`로 고유하게 식별됩니다. `convercus_user_id`는 여러 Convercus 프로그램에 걸쳐 기본 사용자를 식별하며 프로그램 간 분석을 위해 제공됩니다. Braze 내 세분화에는 `convercus_account_id`를 사용하세요.
{% endalert %}

**`email_subscribe` 매핑**

| Convercus 상태 | Braze `email_subscribe` |
| --- | --- |
| `email consent` 또는 `newsletter`에 대한 `allowedOptins` 항목 | `opted_in` |
| 해당 채널에 대한 `declinedOptIns` 항목(허용된 항목 없음) | `unsubscribed` |
| 어느 쪽에도 기록 없음 | `subscribed` (Braze의 중립 기본값) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="커스텀 속성" }

#### 커스텀 이벤트 {#custom-events}

| 이벤트 | 트리거 시점 |
| --- | --- |
| `convercus_account_created` | Convercus에서 새 계정이 생성될 때 |
| `convercus_membership_added` | 기존 계정이 로열티 프로그램에 가입할 때 |
| `convercus_membership_created` | 새 멤버십이 생성될 때 |
| `convercus_membership_changed` | 멤버십의 데이터가 변경될 때 |
| `convercus_membership_optins_changed` | 회원의 옵트인 설정이 변경될 때 |
| `convercus_membership_terminated` | 멤버십이 종료될 때 |
| `convercus_status_level_changed` | 회원의 등급 또는 상태 레벨이 변경될 때 |
| `convercus_balance_changed` | 회원의 포인트 잔액이 변경될 때 |
| `convercus_account_transaction` | 로열티 트랜잭션이 정산될 때 |
| `convercus_coupon_assigned` | 쿠폰이 회원에게 할당될 때 |
| `convercus_coupon_redeemed` | 회원이 쿠폰을 사용할 때 |
| `convercus_user_logged_in` | 회원이 Convercus 기반 서비스에 로그인할 때 |
| `convercus_user_logged_out` | 회원이 로그아웃할 때 |
| `convercus_user_created` | 새 사용자가 생성될 때 |
| `convercus_user_changed` | 사용자의 프로필 데이터가 변경될 때 |
| `convercus_push_token_created` | 회원에 대한 푸시 토큰이 등록될 때 |
| `convercus_push_token_deleted` | 푸시 토큰이 삭제될 때 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="커스텀 이벤트" }

#### 구매 {#purchases}

`EARNTRANSACTION` 유형(고객 지출로 적립된 포인트)의 Convercus 트랜잭션은 Braze에 [구매]({{site.baseurl}}/api/objects_filters/purchase_object)로 보고되며, 트랜잭션 ID를 제품 식별자로, 트랜잭션 금액과 통화를 가격과 통화로 사용하여 Braze 매출 분석, RFM 세분화 및 예측 기능에 반영됩니다.

`PAYWITHPOINTSTRANSACTION` 유형(포인트 소진)의 트랜잭션은 구매로 보고되지 **않으며**, `convercus_account_transaction` 커스텀 이벤트로 전달되어 세분화에 활용할 수 있습니다. 적립 트랜잭션의 취소 및 환불은 음수 가격 구매로 보고되어 Braze 매출이 Convercus와 일치하도록 유지됩니다.

### 2단계: 연결된 콘텐츠로 실시간 로열티 데이터 가져오기 {#step-2-fetch-live-loyalty-data-with-connected-content}

발송 시점에 최신이어야 하는 값(현재 포인트 잔액, 활성 쿠폰, 최신 등급)의 경우, 가장 최근 동기화된 속성에 의존하는 대신 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)를 사용하여 Braze에서 Convercus를 호출합니다. 두 엔드포인트 모두 웹훅과 동일한 기본 URL 아래에 위치하며, `X-Convercus-Key` 헤더가 필요합니다.

| 데이터 | 엔드포인트 | 반환 값 |
| --- | --- | --- |
| 회원 프로필 | `GET /members/{accountId}/profile` | `member_id`, `first_name`, `last_name`, `email`, `tier_name`, `tier_id`, `points_balance`, `enrollment_date`. |
| 회원 쿠폰 | `GET /members/{accountId}/coupons` | 활성화되어 사용 가능한 쿠폰 목록(상태, 값, 유효 기간, 제목, 설명). `?lang=<code>`를 추가하여(예: `?lang=de`) `title`/`description`을 현지화할 수 있으며, 기본값은 `en`입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="2단계: 연결된 콘텐츠로 실시간 로열티 데이터 가져오기" }

연결된 콘텐츠 엔드포인트는 예상된 실패 시에도 항상 HTTP 200을 반환하므로, Liquid 템플릿에서 `error` 필드를 기준으로 분기할 수 있습니다.

| 응답 | 의미 |
| --- | --- |
| `200` + 페이로드 | 성공 |
| `200 { "error": "member_not_found" }` | 해당 프로그램에 계정이 존재하지 않습니다. |
| `200 { "error": "internal_error" }` | 업스트림 또는 예상치 못한 오류입니다. |
| `401` | `X-Convercus-Key`가 누락되었거나 유효하지 않습니다(Liquid가 아닌 통합 시점에 처리). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="2단계: 연결된 콘텐츠로 실시간 로열티 데이터 가져오기" }

예시 — 회원의 로열티 상태(등급, 포인트, 활성 오퍼)를 렌더링합니다:

{% raw %}
```liquid
{% connected_content
  https://<SERVICE_HOST>/v1/programs/{programId}/members/{{custom_attribute.${convercus_account_id}}}/profile
  :headers { "X-Convercus-Key": "cvc_…" }
  :content_type application/json
  :cache_max_age 300
  :retry
  :save member
%}

{% connected_content
  https://<SERVICE_HOST>/v1/programs/{programId}/members/{{custom_attribute.${convercus_account_id}}}/coupons?lang=en
  :headers { "X-Convercus-Key": "cvc_…" }
  :content_type application/json
  :cache_max_age 0
  :retry
  :save coupon_data
%}

{% unless member.error %}
  <h2>Your Loyalty Status</h2>
  <p>Hi {{member.first_name}}, you're a <strong>{{member.tier_name}}</strong> member.</p>
  <p>Points balance: <strong>{{member.points_balance}}</strong></p>

  {% if coupon_data.coupons.size > 0 %}
    <h3>Your Active Offers</h3>
    {% for coupon in coupon_data.coupons %}
      <p><strong>{{coupon.title}}</strong> — valid until {{coupon.valid_to}}</p>
    {% endfor %}
  {% endif %}
{% endunless %}
```
{% endraw %}

연결된 콘텐츠는 항상 조건문으로 감싸서(`member.error` 및 비어 있는 `coupons` 확인) 일시적인 조회 실패가 깨진 메시지를 발송하지 않도록 합니다. 프로필은 캐시하되(`cache_max_age 300`), 쿠폰 상태는 발송 간에 변경될 수 있으므로 캐시하지 마세요(`cache_max_age 0`).

## 고려 사항 {#considerations}

- **지연 시간:** Convercus에서 Braze로의 이벤트는 Kafka를 통해 전파되며, 정상 부하 상태에서 몇 초 내에 Braze에 도달합니다.
- **Braze 사용량 제한:** 통합은 `429` 응답 시 자동으로 재시도하며, Braze의 `x-ratelimit-retry-after` 헤더를 준수하여 지수 백오프를 적용합니다.
- **연결된 콘텐츠 캐싱:** Braze는 기본적으로 연결된 콘텐츠 응답을 몇 분간 캐시합니다. 발송 시점에 정확한 값이 필요한 경우(예: 포인트 잔액), 연결된 콘텐츠 호출에서 캐시 기간을 줄이거나 우회하세요.
- **프로그램당 하나의 구성:** 각 로열티 프로그램은 하나의 Braze 워크스페이스에 매핑됩니다. 두 번째 워크스페이스를 연결하려면 별도의 프로그램에서 구성하세요.
- **관찰 가능성:** 프로그램별 API 호출 통계 및 오류 이력(양방향)은 90일간 보관되며, Selfservice의 Braze 통합 카드에서 확인할 수 있습니다.

## 문제 해결 {#troubleshooting}

- **이벤트가 Braze에 표시되지 않는 경우:** 식별자로 사용한 값(1단계에서 선택)이 Braze에서 해당 사용자의 `external_id`(또는 선택한 식별자 유형)와 일치하는지 확인합니다. 식별자가 일치하지 않으면 이벤트가 잘못된 프로필에 귀속되거나 누락될 수 있습니다.
- **웹훅이 `401`을 반환하는 경우:** `X-Convercus-Key` 헤더가 누락되었거나 `cvc_…` API 키가 해지되었습니다. Selfservice에서 키를 재생성하고 Braze에서 웹훅 액션을 업데이트하세요.
- **웹훅이 `400`을 반환하는 경우:** 요청에 `Content-Type: application/json`이 누락되었거나 페이로드가 문서화된 스키마와 일치하지 않습니다. 이메일 구독 웹훅의 경우, `400`은 요청된 옵트인이 프로그램에서 인식되지 않거나 구성되어 있지 않음을 의미하기도 합니다.
- **심층 디버깅:** Selfservice의 Braze 통합 카드에서 프로그램별 API 호출 통계 및 오류 이력을 확인하거나, Convercus 담당자에게 문의하세요.