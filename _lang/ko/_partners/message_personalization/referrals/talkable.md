---
nav_title: Talkable
article_title: Talkable
description: "이 참조 문서에서는 추천 마케팅 플랫폼인 Talkable과 Braze 간의 파트너십에 대해 설명합니다. Talkable은 추천 캠페인에서 수집한 마케팅 이메일 옵트인을 실시간으로 Braze에 동기화합니다."
alias: /partners/talkable/
page_type: partner
search_tag: Partner
---

# Talkable

> [Talkable](https://www.talkable.com/)은 소비자 브랜드가 만족한 고객을 확장 가능한 추천 채널로 전환할 수 있도록 지원합니다. Braze 통합을 통해 Talkable 추천 캠페인에서 수집된 마케팅 이메일 옵트인이 실시간으로 Braze에 전달되므로, 팀은 모든 새로운 추천인과 친구를 환영하고, 세분화하고, 참여시키는 데 필요한 동의, 컨텍스트, 캠페인 데이터를 확보할 수 있습니다.

_이 통합은 Talkable에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Talkable은 Braze가 구동하는 고객 여정에 추천인 주도의 획득을 도입합니다. 이 통합은 Talkable이 수집한 모든 추천 옵트인을 실시간으로 일치하는 Braze 프로필로 이동시켜, 환영 플로우, 추천 여정, 세분화, 라이프사이클 메시징이 신뢰할 수 있는 동의와 추천 컨텍스트를 기반으로 시작될 수 있도록 합니다. 수동 목록 내보내기나 배치 동기화가 필요하지 않습니다.

Talkable은 두 가지 시나리오에서 마케팅 옵트인을 수집합니다:

* **추천인 가입:** 추천인이 Talkable 추천 캠페인에 가입하고 마케팅 이메일 수신에 동의합니다.
* **친구 이메일 게이팅:** 친구가 Talkable의 이메일 게이팅 단계를 완료하고 마케팅 이메일 수신에 옵트인합니다.

두 경우 모두 Talkable은 일치하는 Braze 고객 프로필을 실시간으로 생성하거나 업데이트하고, 사용자의 이메일 구독 상태를 **Opted In**으로 설정합니다.

### 기본 동작 {#default-behavior}

Talkable은 Talkable에서 명시적으로 동의한 사람(캠페인에 가입한 추천인 또는 이메일 게이팅 중 옵트인한 친구)의 개별 옵트인 이벤트에서만 Braze로 데이터를 전송합니다. Talkable은 야간 배치, 전체 동기화 또는 암묵적 프로필 업데이트를 실행하지 않습니다. Talkable은 옵트인하지 않은 프로필을 Braze로 전송하지 않습니다.

## 사용 사례 {#use-cases}

- 추천인이 Talkable 추천 캠페인에 가입하는 순간 Braze 환영 Canvas를 트리거합니다.
- 친구가 옵트인하는 즉시 친구 전용 Canvas와 개인화된 첫 구매 오퍼로 추천받은 친구를 활성화합니다.
- Braze 커스텀 속성으로 전송된 추천인 및 친구 플래그와 캠페인 메타데이터를 사용하여 추천 컨텍스트별로 세분화합니다.
- 규정 준수에 적합한 뉴스레터 발송을 위해 추천 옵트인을 지정된 Braze 구독 그룹으로 라우팅합니다.

## 필수 조건 {#prerequisites}

시작하기 전에 다음이 필요합니다:

| 필수 조건 | 설명 |
| --- | --- |
| Talkable 계정 | 이 파트너십을 활용하려면 최소 하나의 캠페인이 구성된 Talkable 사이트가 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. Braze 대시보드의 **설정** > **API 키**에서 이 키를 생성합니다. 자세한 내용은 [REST API 키 생성]({{site.baseurl}}/api/basics/#creating-rest-api-keys)을 참조하세요. |
| Braze REST 엔드포인트 | Braze REST 엔드포인트 URL(예: `https://rest.iad-01.braze.com`). US(`.com`) 및 EU(`.eu`) Braze 클러스터가 모두 지원됩니다. 자세한 내용은 [REST API 엔드포인트]({{site.baseurl}}/api/basics/#endpoints)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

### 1단계: Talkable에서 Braze 앱 설치 {#step-1-install-the-braze-app-in-talkable}

1. Talkable 관리자에 로그인하고 메뉴를 열어 **All Site Settings** > **App Store**로 이동합니다.
2. **Braze**를 찾아 **Install**을 선택합니다.
3. Braze REST 엔드포인트와 `users.track` 권한이 있는 REST API 키를 입력한 다음 **Save**를 선택합니다.

### 2단계: 이메일 옵트인 동작 구성 {#step-2-configure-the-email-opt-in-action}

1. Talkable Braze 앱에서 **Email opt-in** 동작을 엽니다.
2. (선택 사항) Braze 구독 그룹 식별자를 입력하고, 커스텀 속성을 추가하고, 사용자 별칭을 구성합니다. 자세한 내용은 [Talkable 커스터마이징](#customizing-talkable)을 참조하세요.
3. **Save**를 선택합니다. 라이브 옵트인 이벤트가 동기화되기 전에 테스트 페이로드로 구성을 확인할 수 있도록 동작을 비활성화 상태로 둡니다.

### 3단계: 샘플 페이로드로 테스트 {#step-3-test-with-a-sample-payload}

1. Talkable에서 **Email opt-in** 동작의 **Send sample payload**를 선택하여 Braze에 테스트 요청을 보냅니다.
2. Braze에서 **오디언스** > **사용자 검색**으로 이동하여 테스트 이메일 주소로 검색합니다.
3. 프로필이 존재하고 **Email Subscribe**가 **Opted In**으로 설정되어 있으며, 구성한 커스텀 속성, 구독 그룹 등록 또는 사용자 별칭이 예상대로 표시되는지 확인합니다.

### 4단계: 라이브 트래픽에 대해 동작 활성화 {#step-4-enable-the-action-for-live-traffic}

Braze에서 테스트 프로필이 올바르게 표시되면 Talkable로 돌아가서 **Email opt-in** 동작을 활성화합니다.

이 시점부터 모든 Talkable 옵트인 이벤트가 일치하는 프로필을 실시간으로 Braze에 동기화합니다.

## Braze로 전송되는 기본 사용자 속성 {#default-user-attributes-sent-to-braze}

모든 옵트인 이벤트에서 Talkable은 다음 표준 Braze 사용자 속성으로 일치하는 Braze 고객 프로필을 생성하거나 업데이트합니다. 빈 값은 생략됩니다.

| Braze 속성 | 유형 | 참고 |
| --- | --- | --- |
| `email_subscribe` | 문자열 | 모든 Talkable 옵트인 이벤트에서 **Opted In**으로 설정됩니다. |
| `email` | 문자열 | Braze 프로필을 매칭하는 데 사용되는 기본 식별자입니다. |
| `phone` | 문자열 | 사용자 속성으로만 수집됩니다. Braze는 E.164 형식을 기대하며, Talkable에 저장된 그대로 전송됩니다. |
| `first_name` | 문자열 | 사용자의 이름입니다. |
| `last_name` | 문자열 | 사용자의 성입니다. |
| 구독 그룹 등록 | 해당 없음 | 구독 그룹이 구성된 경우에만 추가됩니다. 사용자는 구독 상태로 등록됩니다. |
| 사용자 별칭 | 해당 없음 | 사용자 별칭이 구성된 경우에만 추가됩니다. 자세한 내용은 [Talkable 커스터마이징](#customizing-talkable)을 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Braze로 전송되는 기본 사용자 속성" }

## Talkable 커스터마이징 {#customizing-talkable}

다음 선택적 커스터마이징을 사용할 수 있습니다. 원하는 조합으로 구성할 수 있으며, 각각 독립적입니다.

### Braze 구독 그룹에 옵트인 등록 {#enroll-opt-ins-in-a-braze-subscription-group}

1. Braze에서 **오디언스** > **구독 그룹 관리**에서 구독 그룹 ID를 복사합니다. 자세한 내용은 [사용자 구독 관리]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/)를 참조하세요.
2. Talkable **Email opt-in** 동작에서 **Subscription group identifier** 필드에 붙여넣습니다.

Talkable은 각 옵트인을 해당 구독 그룹에 구독 상태로 등록하여, 추천 옵트인을 글로벌 구독 대신 해당 그룹으로 범위를 지정합니다. Talkable은 구독만 추가하며, 절대 제거하지 않습니다.

### 커스텀 속성 전송 {#send-custom-attributes}

동작의 페이로드 편집기에 키-값 페어를 추가합니다. 입력한 키가 Braze 고객 프로필의 속성 이름이 됩니다.

값은 Liquid 템플릿으로 처리됩니다. 다음 변수를 사용할 수 있습니다:

{% raw %}
| 변수 | 내용 |
| --- | --- |
| `{{ person }}` | 옵트인한 추천인 또는 친구(`email`, `first_name`, `last_name`, `phone_number`, `username`, `is_advocate`, `custom_properties` 등). |
| `{{ ip }}` | 옵트인이 발생한 IP 주소. |
| `{{ campaign }}` | 원래 Talkable 캠페인(`name`, `type`, `tag_names` 등). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liquid 템플릿 변수" }
{% endraw %}

{% raw %}
예: Braze에서 추천 컨텍스트별로 세분화하려면 `talkable_is_advocate` = `{{ person.is_advocate }}`와 `talkable_campaign_name` = `{{ campaign.name }}`을 추가합니다.
{% endraw %}

### Braze 사용자 별칭으로 사용자 식별 {#identify-users-with-braze-user-aliases}

페이로드 편집기에서 `user_alias.alias_name`(예: {% raw %}`{{ person.username }}`{% endraw %})과 `user_alias.alias_label`(예: `username`)을 추가합니다. 자세한 내용은 [사용자 별칭 오브젝트]({{site.baseurl}}/api/objects_filters/user_alias_object/)를 참조하세요.

두 필드가 모두 있으면 시스템은 이메일 외에 별칭으로도 사용자를 식별하며, 일치하는 항목이 없으면 Braze가 새 별칭 프로필을 생성합니다.

{% alert note %}
두 별칭 필드 모두 필수입니다. `alias_name` 또는 `alias_label` 중 하나만 설정된 경우 Talkable은 사용자 별칭을 전송하지 않으며, 프로필은 이메일로만 매칭됩니다.
{% endalert %}

## Braze에서 사용자 찾기 및 생성 {#find-and-create-users-in-braze}

* 기본적으로 Braze는 이메일 주소로 프로필을 매칭합니다. 일치하는 프로필이 없으면 Braze가 새 프로필을 생성합니다.
* 사용자 별칭이 구성된 경우 Braze는 해당 별칭으로도 매칭하며, 일치하는 항목이 없으면 새 별칭 프로필을 생성합니다.
* 이 통합에서는 외부 ID를 사용하지 않습니다. Talkable 옵트인을 기존 외부 식별 프로필에 연결하려면 해당 프로필의 알려진 별칭과 일치하는 라벨의 사용자 별칭을 구성하세요.

## Braze에서 Talkable 활용 {#use-talkable-with-braze}

### 동기화된 사용자 찾기 {#find-a-synced-user}

**오디언스** > **사용자 검색**으로 이동하여 이메일로 검색하면 Talkable이 생성하거나 업데이트한 프로필을 확인할 수 있습니다.

표준 필드(이메일, 전화번호, 이름, 성)와 구성한 커스텀 속성이 프로필에 표시되며, **Email Subscribe**는 **Opted In**으로 표시됩니다.

### 추천 Segment 구축 {#build-a-referral-segment}

1. **Email Subscribe**가 **Opted In**인 조건으로 필터링된 Segment를 생성합니다.
2. Talkable이 전송하는 커스텀 속성으로 세분화합니다. 예를 들어, 추천인을 타겟팅하려면 `talkable_is_advocate`가 `true`인 조건을, 특정 추천 프로그램을 타겟팅하려면 `talkable_campaign_name`이 해당 캠페인과 같은 조건을 사용합니다.

### 라이프사이클 메시징 트리거 {#trigger-lifecycle-messaging}

1. 실행 기반 전달로 Canvas 또는 Campaign을 구축합니다. 이 통합에서는 다음 Braze 트리거 유형이 작동합니다:
* **구독 상태 업데이트**(예: 이메일 구독이 **Opted In**으로 변경)
* **구독 그룹 상태 업데이트**(구독 그룹이 구성된 경우)
* **커스텀 속성 값 변경**(전송하는 모든 Talkable 커스텀 속성에 대해).
2. 프로필의 Talkable 커스텀 속성(캠페인 이름, 보상 값, 추천인 등)으로 메시지를 개인화합니다.

## 고려 사항 {#considerations}

* **이메일 옵트인만 해당:** 전화번호는 표준 사용자 속성으로 수집되지만, 이 통합은 SMS 구독 상태를 설정하지 않습니다. Talkable은 SMS 옵트인을 동기화하지 않습니다.
* **전화번호 형식:** Braze는 국제(E.164) 형식의 전화번호를 기대합니다.
* **실시간 이벤트 기반 동기화:** Talkable은 옵트인 이벤트당 하나의 요청을 전송합니다(요청당 한 명의 사용자). 배치 처리나 주기적 전체 동기화가 없으며, 볼륨은 추천 옵트인 볼륨에 따릅니다.
* **안정적인 전달:** Braze가 일시적으로 오류를 반환하면 Talkable이 자동으로 재시도합니다. 지속적인 실패 시 사이트 관리자에게 이메일 알림이 전송됩니다.

## 문제 해결 {#troubleshooting}

| 오류 | 가능한 원인 | 해결 방법 |
| --- | --- | --- |
| 401 Unauthorized | REST API 키에 `users.track` 권한이 없거나 엔드포인트가 잘못된 클러스터를 가리키고 있습니다. | `users.track` 권한으로 키를 재발급하고 REST 엔드포인트가 Braze 클러스터와 일치하는지 확인합니다. |
| 설치 시 REST 엔드포인트 거부 | URL이 Braze REST 엔드포인트가 아닙니다. | 클러스터의 REST 엔드포인트를 사용하세요(예: `https://rest.iad-01.braze.com`). 대시보드 URL은 작동하지 않습니다. |
| 프로필이 생성되었지만 구독 그룹에 없음 | 구독 그룹 ID가 구성되지 않았습니다. | **Email opt-in** 동작에 구독 그룹 ID를 입력합니다. |
| 사용자 별칭이 적용되지 않음 | 두 별칭 필드(이름 또는 라벨) 중 하나만 입력되었습니다. | 동작에 별칭 이름과 별칭 라벨 두 필드를 모두 입력합니다. |
| 프로필이 표시되지 않음 | 샘플 요청이 아직 전송되지 않았거나 동작이 비활성화되어 있습니다. | Talkable에서 **Send sample payload**를 선택하고 **Email opt-in** 동작이 활성화되어 있는지 확인합니다. |
| 키 교체 후 요청 전송이 중단됨 | 저장된 API 키가 Braze에서 취소되었거나 교체되었습니다. | Talkable **App Store**에서 Braze 앱을 열고 새 REST API 키를 붙여넣은 다음 **Save**를 선택합니다. **Send sample payload**로 다시 테스트합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="문제 해결" }

Talkable 통합에 대한 자세한 내용은 [Talkable Braze 통합 설명서](https://docs.talkable.com/email_marketing_and_automation/braze/)를 참조하세요. Talkable 고객지원에 문의하려면 [support@talkable.com](mailto:support@talkable.com)으로 이메일을 보내세요.