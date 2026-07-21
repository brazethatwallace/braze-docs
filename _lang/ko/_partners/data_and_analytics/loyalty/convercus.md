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

Braze와 Convercus 통합은 양방향입니다. 로열티 데이터는 커스텀 속성, 커스텀 이벤트, 구매로 실시간으로 Braze에 유입되며, Braze Canvases와 Campaigns는 웹훅을 통해 Convercus에서 로열티 동작을 트리거할 수 있습니다. 동기화된 멤버 등급, 포인트 잔액, 구매, 쿠폰 활동을 Segments, Liquid, 연결된 콘텐츠에서 활용하세요. Braze 여정에서 쿠폰을 할당하고, 포인트 적립 및 차감 트랜잭션을 기록하며, Convercus에서 이메일 구독 설정을 업데이트할 수도 있습니다.

Convercus가 통합을 호스팅하므로 추가 인프라를 설치할 필요가 없습니다. 대부분의 로열티 커넥터가 데이터를 한 방향으로만 전송하는 반면, Convercus는 루프를 완성합니다. Braze에서 로열티 이벤트에 반응하고, Convercus에서 동작을 수행한 다음, 결과를 다시 Braze에서 측정할 수 있습니다.

## 사용 사례 {#use-cases}

1. **등급 승급 축하:** 멤버가 Convercus에서 로열티 등급이 올라가면, 환영 메시지, 등급 전용 혜택, 멤버의 새 등급 및 포인트 잔액이 포함된 개인화된 Braze Canvas를 트리거합니다.
2. **생일 및 마일스톤 보너스:** Braze 여정에서 멤버의 생일이나 기념일에 Convercus에 보너스 포인트를 적립한 다음, 새 잔액을 확인하는 축하 메시지를 보냅니다.
3. **이탈 멤버 윈백:** 비활성 멤버의 경우, Braze가 웹훅을 통해 Convercus에서 개인화된 쿠폰을 할당하고 이메일, 푸시, 인앱 메시지를 통해 전달합니다.
4. **메시지 내 실시간 포인트 잔액:** 연결된 콘텐츠를 사용하여 멤버의 실시간 포인트 잔액을 Braze Liquid로 가져와 "다음 보상까지 X 포인트 남았습니다"와 같은 메시지를 구현합니다.

## 필수 조건 {#prerequisites}

시작하기 전에 다음이 필요합니다.

| 필수 조건 | 설명 |
| --- | --- |
| Convercus 계정 | 활성 Convercus 프로그램이 필요합니다. 아직 고객이 아닌 경우 Convercus 계정 매니저에게 문의하세요. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키가 필요합니다. Braze 대시보드에서 **설정** > **API 키**로 이동하여 이 키를 생성하세요. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/api/basics#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

시스템 간에 일관된 사용자 식별자가 필요합니다. Braze에서 `external_id`(또는 선택한 식별자 유형)로 사용되는 값이 Convercus의 해당 멤버 식별자와 일치해야 합니다. 그렇지 않으면 이벤트가 올바른 프로필에 귀속되지 않습니다.

## 통합 {#integration}

### 1단계: Convercus Selfservice에서 Braze 구성 {#step-1-configure-braze-in-convercus-selfservice}

Convercus Selfservice(고객용 관리 UI—Convercus 계정 매니저가 제공하는 URL을 사용하여 열기)에서 Braze에 연결할 프로그램을 열고 **Braze 통합 카드**를 사용하여 다음을 수행합니다.

1. 통합 양식을 작성하여 Braze 연결을 구성합니다.

   | 필드 | 설명 |
   | --- | --- |
   | `apiKey` | Braze REST API 키(`users.track` 권한 포함). |
   | `apiEndpoint` | Braze REST 엔드포인트(예: `https://rest.iad-01.braze.com`). |
   | 식별자 유형 | `external_id` 또는 `user_alias`. Convercus 멤버를 Braze 사용자 프로필에 매칭하는 방법을 결정합니다. |
   | `defaultOptins` | 프로그램의 옵트인 채널(`membershipOptins`에서) 다중 선택. 요청에서 `optins`가 생략된 경우 이메일 구독 웹훅의 기본값으로 사용됩니다. 하나 이상 선택할 때까지 Braze 구성은 **미완료** 상태로 처리됩니다. |
   {: .reset-td-br-1 .reset-td-br-2 aria-label="1단계: Convercus Selfservice에서 Braze 구성" }

2. 인바운드 호출용 API 키를 생성합니다. 프로그램별 `X-Convercus-Key` 자격 증명을 생성합니다. 원시 키는 생성 시 한 번만 표시되며 `cvc_` 접두사가 붙습니다(형식: `cvc_<base64url>`). 2단계에서 웹훅 Campaigns와 연결된 콘텐츠 블록을 구성할 때 Braze에 저장하세요. 키는 동일한 카드에서 언제든지 취소할 수 있으며, 취소는 즉시 적용됩니다.

Braze 연결을 저장하면 Convercus가 해당 프로그램의 로열티 이벤트를 즉시 Braze로 스트리밍하기 시작합니다. 추가 인프라 설정은 필요하지 않습니다.

{% alert note %}
각 Convercus 프로그램은 독립적으로 구성됩니다. 단일 Convercus 테넌트는 서로 다른 프로그램을 서로 다른 Braze 워크스페이스에 연결할 수 있으며, 각각 고유한 API 키를 사용합니다.
{% endalert %}

### 2단계: Braze에서 웹훅 구성 {#step-2-configure-webhooks-in-braze}

Canvas 또는 Campaign에서 Convercus 동작을 트리거하려면 Convercus 통합 서비스를 호출하는 Braze 웹훅 동작을 생성합니다. 모든 요청에는 다음 헤더가 포함되어야 합니다.

- `X-Convercus-Key: cvc_…` - 1단계에서 생성한 API 키.
- `Content-Type: application/json`

모든 엔드포인트는 기본 URL `<SERVICE_HOST>/v1/programs/{programId}` 아래에 있습니다. `<SERVICE_HOST>`를 Convercus 계정 매니저가 제공한 호스트로, `{programId}`를 Convercus 프로그램 ID로 바꾸세요.

| 동작 | 엔드포인트 |
| --- | --- |
| 멤버에게 쿠폰 할당 | `POST /campaigns/{couponId}/assign` — `{ "couponCode": "..." }`를 반환합니다. |
| 여러 멤버에게 쿠폰 할당 | `POST /campaigns/{couponId}/assign/batch` — 한 번의 호출로 최대 500명의 멤버; 본문에 선택적 `valid_from` / `valid_to`를 허용합니다. `{ "batchId": "..." }`를 반환합니다. |
| 포인트 적립/차감 기록 | `POST /members/{accountId}/bookings` — 멤버 계정에 `EARNBOOKING` 또는 `BURNBOOKING`을 생성합니다. `{ "bookingId": "..." }`를 반환합니다. |
| 이메일 구독 설정 동기화 | `POST /subscriptions/email` — 멤버의 옵트인을 `allowed` 또는 `declined`로 설정합니다. 옵트인 채널은 요청 `optins` > `defaultOptins` 순으로 결정됩니다. `200`(모두 성공), `207`(부분 — `succeeded` / `failed` 참조), 또는 `400`(알 수 없는 옵트인 또는 구성되지 않음)을 반환합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="2단계: Braze에서 웹훅 구성" }

예시 — 멤버에게 쿠폰 할당:

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

다른 동작도 동일한 패턴을 따르며, 엔드포인트와 본문만 변경됩니다. 예를 들어, 포인트 기록은 `/members/{accountId}/bookings`에 `booking_type`(`EARNBOOKING` 또는 `BURNBOOKING`), `booking_type_code`, `points`, `reason`과 함께 전송하고, 이메일 구독 웹훅은 `/subscriptions/email`에 `account_id`와 `status`(`allowed` 또는 `declined`)를 전송합니다.

#### 오류 응답 및 재시도 {#error-responses-and-retries}

| 상태 | 의미 |
| --- | --- |
| `200` | 성공. |
| `207` | Multi-Status — 이메일 구독 웹훅에서만 해당되며, 일부 멤버십은 업데이트되고 다른 멤버십은 실패한 경우입니다. |
| `400` | 요청 본문 유효성 검사 실패. |
| `401` | `X-Convercus-Key`가 누락되었거나 유효하지 않습니다. |
| `5xx` | 업스트림 Convercus 호출 실패. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="오류 응답 및 재시도" }

{% alert warning %}
5xx 응답은 **성공 여부를 확인하지 않고 재시도하면 안전하지 않습니다**—이러한 작업은 멱등성이 없으며, 재시도 시 쿠폰이 이중 할당되거나 포인트가 이중 적립될 수 있습니다. 이러한 웹훅에 대해 Braze의 5xx 자동 재시도를 비활성화하거나 최대 재시도 횟수를 매우 낮게 설정하세요.
{% endalert %}

### 3단계: Braze에서 데이터 확인 {#step-3-verify-data-in-braze}

1. Convercus에서 로열티 이벤트를 트리거합니다. 예를 들어, 상태 등급 변경, 포인트 트랜잭션, 쿠폰 사용 등이 있습니다.
2. Braze에서 해당 사용자를 열고 예상되는 커스텀 속성, 커스텀 이벤트 또는 구매가 프로필에 표시되는지 확인합니다. 사용자는 `external_id`(또는 1단계에서 선택한 식별자 유형)로 매칭됩니다.
3. 반대 방향을 확인하려면 2단계의 웹훅 중 하나를 호출하는 Braze 테스트 전송을 실행하고 Convercus에서 동작(쿠폰 할당, 포인트 기록 또는 구독 업데이트)을 확인합니다.

## Braze에서 Convercus 활용하기 {#use-convercus-with-braze}

### 1단계: 동기화된 로열티 데이터로 메시지 개인화 {#step-1-personalize-messages-with-synced-loyalty-data}

통합이 활성화되면 Convercus 이벤트가 [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) 엔드포인트를 통해 Braze의 각 사용자 프로필에 도착하며, 다른 네이티브 데이터와 동일하게 사용할 수 있습니다.

1. 로열티 커스텀 속성(예: `convercus_status_level`, `convercus_balance`)을 **Segments**에서 사용하여 등급 보유자, 높은 잔액 멤버 또는 최근 등급이 하락한 사용자를 타겟팅합니다.
2. 커스텀 이벤트(예: `convercus_status_level_changed`, 쿠폰 및 멤버십 이벤트)를 Canvas의 **트리거 단계**로 사용하거나 재참여 Campaigns의 필터로 사용합니다.
3. 이러한 필드를 **Liquid**에서 참조하여 인메시지 개인화(제목란, 본문, 푸시 제목)에 활용합니다.
4. Convercus에서 스트리밍된 `purchase` 이벤트를 사용하여 제품 인식 여정(보충, 카테고리 업셀, 구매 후 리뷰 요청)을 구동합니다.

#### 커스텀 속성 {#custom-attributes}

| 속성 | 설명 |
| --- | --- |
| `convercus_account_id` | 멤버의 Convercus 계정 ID — Convercus 프로그램/Braze 워크스페이스 내에서 고유합니다. |
| `convercus_user_id` | 여러 Convercus 프로그램에 걸쳐 기본 사용자를 식별하는 Convercus 사용자 ID입니다. |
| `convercus_partner_id` | 이 멤버가 등록한 Convercus 파트너(가맹점/브랜드)의 식별자입니다. 제휴 프로그램에서 세분화에 유용합니다. |
| `convercus_member_role` | 로열티 프로그램 내 멤버의 역할입니다. |
| `convercus_status_level` | 멤버의 현재 등급 또는 상태 레벨입니다. |
| `convercus_balance` | 멤버의 현재 `points`, `lockedPoints`, `statusPoints`가 포함된 오브젝트입니다. |
| `email_subscribe` | Convercus 옵트인에서 파생된 이메일 구독 상태(`opted_in`, `subscribed` 또는 `unsubscribed`). |
| `push_subscribe` | Convercus 푸시 토큰 이벤트에서 파생된 푸시 구독 상태(`opted_in` 또는 `unsubscribed`). |
| 표준 프로필 필드 | `email`, `phone`, `first_name`, `last_name`, `dob`, `gender`, `home_city`, `country`. |
| 커스텀 사용자 속성 | Convercus 사용자 오브젝트에 정의된 모든 커스텀 속성은 Braze 커스텀 속성으로 전달됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="커스텀 속성" }

{% alert note %}
Braze 워크스페이스 내에서 멤버는 `convercus_account_id`로 고유하게 식별됩니다. `convercus_user_id`는 여러 Convercus 프로그램에 걸쳐 기본 사용자를 식별하며 크로스 프로그램 분석을 위해 제공됩니다. Braze 내 세분화에는 `convercus_account_id`를 사용하세요.
{% endalert %}

**`email_subscribe` 매핑**

| Convercus 상태 | Braze `email_subscribe` |
| --- | --- |
| `email consent` 또는 `newsletter`에 대한 `allowedOptins` 항목 | `opted_in` |
| 해당 채널에 대한 `declinedOptIns` 항목(허용 항목 없음) | `unsubscribed` |
| 어느 쪽에도 기록 없음 | `subscribed`(Braze의 중립 기본값) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="email_subscribe 매핑" }

#### 커스텀 이벤트 {#custom-events}

| 이벤트 | 트리거 시점 |
| --- | --- |
| `convercus_account_created` | Convercus에서 새 계정이 생성될 때. |
| `convercus_membership_added` | 기존 계정이 로열티 프로그램에 가입할 때. |
| `convercus_membership_created` | 새 멤버십이 생성될 때. |
| `convercus_membership_changed` | 멤버십 데이터가 변경될 때. |
| `convercus_membership_optins_changed` | 멤버의 옵트인 설정이 변경될 때. |
| `convercus_membership_terminated` | 멤버십이 종료될 때. |
| `convercus_status_level_changed` | 멤버의 등급 또는 상태 레벨이 변경될 때. |
| `convercus_balance_changed` | 멤버의 포인트 잔액이 변경될 때. |
| `convercus_account_transaction` | 로열티 트랜잭션이 평가될 때. |
| `convercus_coupon_assigned` | 멤버에게 쿠폰이 할당될 때. |
| `convercus_coupon_redeemed` | 멤버가 쿠폰을 사용할 때. |
| `convercus_user_logged_in` | 멤버가 Convercus 기반 서비스에 로그인할 때. |
| `convercus_user_logged_out` | 멤버가 로그아웃할 때. |
| `convercus_user_created` | 새 사용자가 생성될 때. |
| `convercus_user_changed` | 사용자의 프로필 데이터가 변경될 때. |
| `convercus_push_token_created` | 멤버에 대해 푸시 토큰이 등록될 때. |
| `convercus_push_token_deleted` | 푸시 토큰이 제거될 때. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="커스텀 이벤트" }

#### 구매 {#purchases}

`EARNTRANSACTION` 유형의 Convercus 트랜잭션(고객 지출로 적립된 포인트)은 Braze에 [구매]({{site.baseurl}}/api/objects_filters/purchase_object)로 보고되며, 트랜잭션 ID를 제품 식별자로, 트랜잭션 금액과 통화를 가격과 통화로 사용하여 Braze 매출 분석, RFM 세분화, 예측 기능에 반영됩니다.

`PAYWITHPOINTSTRANSACTION` 유형의 트랜잭션(포인트 차감)은 구매로 보고되지 **않습니다**—이러한 트랜잭션은 `convercus_account_transaction` 커스텀 이벤트로 전달되어 세분화에 활용할 수 있습니다. 적립 트랜잭션의 취소 및 환불은 음수 가격의 구매로 보고되어 Braze 매출이 Convercus와 일치하도록 유지됩니다.

### 2단계: 연결된 콘텐츠로 실시간 로열티 데이터 가져오기 {#step-2-fetch-live-loyalty-data-with-connected-content}

전송 시점에 최신이어야 하는 값(현재 포인트 잔액, 활성 쿠폰, 최신 등급)의 경우, 가장 최근에 동기화된 속성에 의존하는 대신 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)를 사용하여 Braze에서 Convercus를 호출합니다. 두 엔드포인트 모두 웹훅과 동일한 기본 URL 아래에 있으며 `X-Convercus-Key` 헤더가 필요합니다.

| 데이터 | 엔드포인트 | 반환값 |
| --- | --- | --- |
| 멤버 프로필 | `GET /members/{accountId}/profile` | `member_id`, `first_name`, `last_name`, `email`, `tier_name`, `tier_id`, `points_balance`, `enrollment_date`. |
| 멤버 쿠폰 | `GET /members/{accountId}/coupons` | 활성 상태의 사용 가능한 쿠폰 목록(상태, 값, 유효 기간, 제목, 설명). `?lang=<code>`(예: `?lang=de`)를 추가하여 `title`/`description`을 현지화할 수 있으며, 기본값은 `en`입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="2단계: 연결된 콘텐츠로 실시간 로열티 데이터 가져오기" }

연결된 콘텐츠 엔드포인트는 예상된 실패 시에도 항상 HTTP 200을 반환하므로 Liquid 템플릿에서 `error` 필드를 기준으로 분기할 수 있습니다.

| 응답 | 의미 |
| --- | --- |
| `200` + 페이로드 | 성공. |
| `200 { "error": "member_not_found" }` | 이 프로그램에 해당 계정이 존재하지 않습니다. |
| `200 { "error": "internal_error" }` | 업스트림 또는 예기치 않은 오류. |
| `401` | `X-Convercus-Key`가 누락되었거나 유효하지 않습니다(Liquid가 아닌 통합 시점에 처리). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="연결된 콘텐츠 응답" }

예시 — 멤버의 로열티 상태(등급, 포인트, 활성 오퍼) 렌더링:

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

연결된 콘텐츠는 항상 조건문으로 감싸세요(`member.error` 및 빈 `coupons` 확인). 일시적인 조회 실패가 깨진 메시지를 전송하지 않도록 합니다. 프로필은 캐시하되(`cache_max_age 300`), 쿠폰은 캐시하지 마세요(`cache_max_age 0`). 쿠폰 상태는 전송 사이에 변경될 수 있기 때문입니다.

## 고려 사항 {#considerations}

- **지연 시간:** Convercus에서 Braze로의 이벤트는 Kafka를 통해 전파되며 정상 부하에서 수 초 내에 Braze에 도달합니다.
- **Braze 사용량 제한:** 통합은 `429` 응답 시 Braze의 `x-ratelimit-retry-after` 헤더를 준수하며 지수 백오프로 자동 재시도합니다.
- **연결된 콘텐츠 캐싱:** Braze는 기본적으로 연결된 콘텐츠 응답을 몇 분간 캐시합니다. 전송 시점에 정확해야 하는 값(예: 포인트 잔액)의 경우, 연결된 콘텐츠 호출에서 캐시 기간을 줄이거나 우회하세요.
- **프로그램당 하나의 구성:** 각 로열티 프로그램은 단일 Braze 워크스페이스에 매핑됩니다. 두 번째 워크스페이스를 연결하려면 별도의 프로그램에서 구성하세요.
- **관측 가능성:** 프로그램별 API 호출 통계 및 오류 이력(양방향)은 90일간 보관되며 Selfservice의 Braze 통합 카드에서 확인할 수 있습니다.

## 문제 해결 {#troubleshooting}

- **이벤트가 Braze에 표시되지 않는 경우:** 식별자로 사용된 값(1단계에서 선택)이 Braze의 사용자 `external_id`(또는 선택한 식별자 유형)와 일치하는지 확인하세요. 식별자가 일치하지 않으면 이벤트가 잘못된 프로필에 귀속되거나 누락됩니다.
- **웹훅이 `401`을 반환하는 경우:** `X-Convercus-Key` 헤더가 누락되었거나 `cvc_…` API 키가 취소되었습니다. Selfservice에서 키를 재생성하고 Braze의 웹훅 동작을 업데이트하세요.
- **웹훅이 `400`을 반환하는 경우:** 요청에 `Content-Type: application/json`이 누락되었거나 페이로드가 문서화된 스키마와 일치하지 않습니다. 이메일 구독 웹훅의 경우, `400`은 요청된 옵트인이 프로그램에 알려지지 않았거나 구성되지 않았음을 의미하기도 합니다.
- **심층 디버깅:** Selfservice의 Braze 통합 카드에서 프로그램별 API 호출 통계 및 오류 이력을 검토하거나 Convercus 담당자에게 문의하세요.