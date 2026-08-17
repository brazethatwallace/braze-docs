---
nav_title: FAQ
article_title: 이메일 FAQ
page_order: 30
description: "이 페이지에서는 이메일 메시징에 대해 자주 묻는 질문에 대한 답변을 제공합니다."
channel: email

---

# 자주 묻는 질문 {#frequently-asked-questions}

> 이 문서에서는 이메일에 대해 자주 묻는 질문에 대한 답변을 제공합니다.

## 이메일이 발송될 때 여러 프로필이 동일한 이메일 주소를 가지고 있으면 어떻게 되나요? {#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address}

일치하는 이메일 주소를 가진 여러 사용자가 Campaign을 수신할 Segment에 포함되어 있는 경우, 발송 시점에 해당 이메일 주소를 가진 단일 사용자 프로필이 선택됩니다. 이렇게 하면 이메일이 한 번만 발송되고 중복이 제거되어 동일한 이메일 주소로 여러 번 도달하지 않습니다.

**고유 이메일 주소:** Braze는 프로필 간에 고유한 이메일 주소를 강제하지 않습니다. 이메일 주소와 프로필 간의 일대일 관계에 의존하는 경우, 사용자를 생성할 때 내부적으로 중복을 모니터링하세요.

**Liquid 이전 중복 제거:** Braze가 하나의 디스패치 내에서 이메일 주소별로 중복을 제거하는 발송(예: 동일한 주소를 가진 여러 Segment 멤버가 함께 처리되는 예약된 Campaigns)의 경우, 해당 중복 제거는 해당 주소를 대표하도록 선택된 프로필에 대해 Liquid가 실행되기 전에 발생합니다. 해당 프로필에 대해 Liquid가 중단되면(예: [`abort_message()`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) 사용 시), 해당 주소는 해당 디스패치에서 메시지를 수신하지 않습니다. 이는 중복 제거로 이미 건너뛴 프로필도 포함됩니다. 트리거 발송은 동일한 디스패치 내 주소 중복 제거를 적용하지 않습니다. 주소를 공유하는 여러 프로필이 하나의 배치에서 모두 자격을 유지할 수 있으므로, 이 중단 동작은 동일한 방식으로 적용되지 않습니다(다음 단락 참조).

여러 프로필이 이메일 주소를 공유하고 하나의 프로필이 구독을 취소하면, Braze는 해당 주소를 가진 다른 프로필(최대 100개)을 동일한 구독 상태로 업데이트합니다. 이는 구독 취소 및 글로벌 구독 상태와 개별 구독 그룹 상태 등의 기타 변경 사항에 적용됩니다.

**시드 그룹:** [시드 그룹]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups)이 있는 Campaigns의 경우, 여러 프로필이 주소를 공유할 때 Braze는 기본 전달을 위해 하나의 프로필을 선택합니다. 해당 기본 수신자는 동일한 주소를 가진 다른 프로필이 시드 그룹에 있더라도 시드 그룹에 포함되지 않을 수 있습니다.

다음 시나리오에서는 사용자가 이메일을 두 번 수신한 것처럼 보일 수 있습니다:

- **시드 목록 또는 테스트 수신자:** 시드 주소와 내부 테스트 수신자는 메인 오디언스 외에 추가로 발송을 수신할 수 있으며, 받은편지함이 프로필과 시드 항목 모두에 일치하는 경우 중복처럼 보일 수 있습니다.
- **Campaign 또는 Canvas 생성 중 오류 발생:** 사용자가 동일한 발송을 두 번 수신하지 않을 수 있지만, 동일한 제목란을 가진 두 개의 별도 이메일을 수신할 수 있습니다. Campaign 또는 Canvas가 복제된 경우, 이미지나 제목란 등의 이메일 구성 세부 사항을 확인하세요. 또한 체인지로그를 참조하여 Campaign 또는 Canvas가 출시 후 수정되었는지 확인할 수 있습니다. 중복은 사용자가 수신했을 때 원본과 동일한 제목란을 공유할 수 있습니다.
- **여러 사용자 프로필에 이메일 전달이 설정된 경우:** 사용자가 특정 앱에서 여러 계정을 가지고 있지만 하나의 계정이 메일을 전달하는 경우, 사용자는 받은편지함당 한 번 Campaign을 수신합니다. 메시지가 전달되는 받은편지함에서는 메일이 두 번 나타날 수 있습니다. 일부 공급자만 이메일이 다른 계정에서 전달되었는지 표시합니다.
- **수신자의 이메일 구성:** 일부 클라이언트는 받은편지함을 병합합니다("통합 받은편지함"). 동일한 Campaign이 하나의 받은편지함을 공유하는 여러 계정을 대상으로 하는 경우, 실제로 두 개의 별개 프로필에 메시지가 전송되었지만 한 사람이 Campaign을 두 번 받은 것처럼 보일 수 있습니다. 수신자는 여러 계정이 하나의 받은편지함에 결합되어 있는지 확인할 수 있습니다.

이 중복 제거는 대상 사용자가 동일한 디스패치에 있을 때 적용됩니다. 재자격은 이메일 주소가 아닌 프로필별로 평가됩니다.

이메일 Campaign 및 Canvas 단계 재자격은 받은편지함이 아닌 각 사용자의 프로필을 사용하므로, 해당 로직이 충족되는 동안 여러 프로필이 별도의 발송에 자격을 얻을 수 있습니다. 트리거와 결합하면, 주소 수준에서 단일 비자격 기간을 준수하려고 해도 동일한 받은편지함에 둘 이상의 메시지가 전달될 수 있습니다. 트리거 Campaigns(API 트리거 Campaigns 제외) 및 Canvases는 일치하는 이메일 주소를 가진 서로 다른 프로필이 서로 다른 시간에 트리거를 충족할 때 하나의 주소로 두 번 발송할 수도 있습니다. 예를 들어 사용자 A와 사용자 B가 `johndoe@example.com`을 공유하지만 서로 다른 시간대에 있고 전달이 현지 시간대를 사용하는 경우입니다.

사용자는 Canvas 진입 시 이메일별로 중복 제거되지 않으므로, 사용량 제한조치가 적용된 진입으로 인해 약간 다른 시간에 진행되는 경우 Canvas의 첫 번째 단계 이후에는 중복 제거되지 않을 수 있습니다. 특정 이메일 주소와 연결된 사용자가 이메일을 열거나 클릭하면, 해당 이메일 주소를 공유하는 모든 사용자 프로필이 Campaign을 열거나 클릭한 것으로 표시됩니다.

### 예외: API 트리거 Campaigns {#exception-api-triggered-campaigns}

API 트리거 Campaigns는 오디언스가 정의된 위치에 따라 중복을 제거하거나 중복 발송합니다. 여러 전달을 수신하려면 중복 이메일이 API 호출에서 별도의 `user_ids`를 사용하여 개별적으로 타겟팅되어야 합니다. API 트리거 Campaigns에 대한 세 가지 가능한 시나리오는 다음과 같습니다:

- **시나리오 1: 대상 Segment의 중복 이메일:** 동일한 이메일이 API 트리거 Campaign의 대시보드 오디언스 필터에 그룹화된 여러 사용자 프로필에 나타나는 경우, 프로필 중 하나만 이메일을 수신합니다.
- **시나리오 2: 수신자 객체 내 서로 다른 `user_ids`의 중복 이메일:** 동일한 이메일이 `recipients` 객체에서 참조하는 여러 `external_user_id` 값 내에 나타나는 경우, 이메일이 두 번 발송됩니다.
- **시나리오 3: 수신자 객체 내 중복 `user_ids`로 인한 중복 이메일:** 동일한 사용자 프로필을 두 번 추가하려고 하면, 프로필 중 하나만 이메일을 수신합니다.

{% alert important %}
API 호출을 통해 API Campaign을 발송하고(API 트리거 Campaigns 제외) Segment 오디언스에 동일한 이메일 주소를 가진 여러 사용자가 지정된 경우, 호출에 나열된 횟수만큼 해당 주소로 발송됩니다. 이는 API 호출이 의도적으로 구성된 것으로 간주되기 때문입니다.
{% endalert %}

#### 중복 이메일 주소를 사용한 A/B 테스트 {#ab-testing-with-duplicate-email-addresses}

여러 프로필이 동일한 이메일 주소를 공유할 수 있는 경우 이메일에 대한 [다변량 및 A/B 테스트]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing)를 피하세요. 배리언트는 프로필별로 할당되므로 동일한 받은편지함에 둘 이상의 메시지가 전달될 수 있습니다. 해당 상황에서 테스트해야 하는 경우, **Winning Variant** 단계를 [현지 시간대 전달]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#local-time-zone-campaigns)과 결합하여 우승자 선택을 지연시키는 방식으로 사용하지 마세요. 이러한 옵션을 함께 사용하면 중복 발송 가능성이 높아질 수 있습니다.

#### Canvas와 중복 이메일 주소 {#canvas-and-duplicate-email-addresses}

Canvas 여정의 경우, 중복 이메일 주소가 한 번 발송을 수신하는지 또는 둘 이상을 수신하는지는 진입 배칭, 단계 타이밍 및 기타 요인에 따라 달라질 수 있습니다. 여정에 대해 검증할 때까지 동작을 정의되지 않은 것으로 취급하세요. 가능한 경우 중복 프로필을 병합하거나 통합하세요. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="deterministic deduplication for duplicate email addresses in Canvas" %}

### 사용자의 이메일 주소가 다른 사용자가 공유하는 주소로 변경되면 구독 상태는 어떻게 되나요? {#what-happens-to-the-subscription-state-when-a-users-email-address-changes-to-one-shared-by-another-user}

사용자 A의 이메일 주소를 기존 사용자 B가 공유하는 다른 이메일 주소로 설정하거나 업데이트하면, **사용자가 이메일을 업데이트할 때 재구독** 설정이 켜져 있지 않는 한 사용자 A는 사용자 B에서 이미 존재하는 구독 상태를 상속합니다.

### 발신 이메일 설정에 대한 업데이트가 소급 적용되나요? {#will-updates-to-my-outbound-email-settings-apply-retroactively}

아니요. 발신 이메일 설정에 대한 업데이트는 기존 발송에 소급 적용되지 않습니다. 예를 들어, 이메일 설정에서 기본 표시 이름을 변경해도 활성 Campaigns 또는 Canvases의 기존 기본 표시 이름이 자동으로 대체되지 않습니다.

### "좋은" 이메일 전달률이란 무엇인가요? {#what-is-a-good-email-delivery-rate}

일반적으로 "마법의 숫자"는 반송률이 3%를 넘지 않으면서 메시지의 약 98%가 전달되는 것입니다. 메시지의 98% 미만이 전달되면 보통 우려할 만한 이유가 있습니다.

그러나 98% 이상의 전달률에서도 전달 가능성 문제가 있을 수 있습니다. 예를 들어, 모든 반송이 단일 도메인에서 발생하는 경우 해당 공급자와의 평판 문제에 대한 명확한 신호입니다.

또한 메시지가 전달되지만 스팸 폴더에 들어갈 수 있으며, 이는 잠재적으로 심각한 평판 문제를 나타냅니다. 전달되는 메시지 수뿐만 아니라 열람율과 클릭률도 모니터링하여 사용자가 실제로 받은편지함에서 메시지를 보고 있는지 확인하는 것이 중요합니다. 공급자는 보통 모든 스팸 인스턴스를 보고하지 않으므로, 1%의 스팸률도 우려의 원인이 될 수 있으며 추가 분석이 필요합니다.

마지막으로, 비즈니스와 발송하는 이메일 유형도 전달에 영향을 미칠 수 있습니다. 예를 들어, 주로 [트랜잭션 이메일]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign)을 발송하는 사람은 많은 마케팅 메시지를 발송하는 사람보다 더 나은 비율을 기대할 수 있습니다.

### 이메일 전달 측정기준이 왜 100%에 맞지 않나요? {#why-are-my-email-delivery-metrics-not-adding-up-to-100}

이메일 전달 측정기준(전달, 반송, 스팸률)은 소프트 바운스 후 최대 72시간의 재시도 기간 후에도 전달되지 않은 이메일로 인해 100%에 맞지 않을 수 있습니다.

소프트 바운스는 "사서함 가득 참", "서버 일시적으로 사용 불가" 등과 같은 일시적 또는 과도적 문제로 인해 반송되는 이메일입니다. 소프트 바운스된 이메일이 72시간 후에도 전달되지 않으면, 이 이메일은 Campaign 전달 측정기준에 포함되지 않습니다.

### 이메일 피드백 루프란 무엇인가요? {#what-is-an-email-feedback-loop}

이메일 피드백 루프(FBL)를 통해 발신자는 높은 불만 건수를 받는 Campaigns를 식별하여 평판을 모니터링할 수 있습니다. Gmail 피드백 루프를 구현하는 단계는 [Google의 피드백 루프](https://support.google.com/a/answer/6254652) 문서를 참조하세요.

### 열람 추적 픽셀이란 무엇인가요? {#what-are-open-tracking-pixels}

[열람 추적 픽셀]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#update-the-placement)은 발신자의 이메일 클릭 추적 도메인을 활용하여 이메일 열람 이벤트를 추적합니다. 이 픽셀은 이메일의 HTML에 추가되는 이미지 태그입니다. 가장 일반적으로 body 태그 내의 마지막 HTML 요소입니다. 사용자가 이메일을 로드하면, 브랜드 추적 도메인에서 이미지를 채우기 위한 요청이 이루어지며, 이를 통해 열람 이벤트가 기록됩니다.

### 일반 텍스트로 렌더링된 이메일의 열람을 추적할 수 있나요? {#can-i-track-opens-for-emails-rendered-in-plain-text}

아니요. Braze는 이메일의 HTML에 포함된 [열람 추적 픽셀]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#open-tracking-pixel)을 사용하여 이메일 열람을 추적합니다. 수신자의 이메일 클라이언트가 이메일을 로드하면 이 이미지를 요청하고, Braze가 열람 이벤트를 기록합니다.

일반 텍스트 이메일은 이미지를 포함할 수 없으므로 열람 추적 픽셀이 포함되지 않아 일반 텍스트로 렌더링된 이메일의 열람을 추적할 수 없습니다. 하이퍼링크는 일반 텍스트에서도 기능하므로 클릭은 여전히 추적할 수 있습니다.

이는 예상되는 동작입니다. 열람율 정확도를 위해 이메일을 HTML로 디자인하고, 수신자가 일반 텍스트 버전을 볼 때 열람이 집계되지 않는다는 점을 인지하세요.

### 수신자가 이메일을 전달할 때 이메일 추적은 어떻게 작동하나요? {#how-does-email-tracking-work-when-recipients-forward-emails}

수신자가 이메일을 전달하면, 전달된 이메일에는 원본과 동일한 열람 추적 픽셀과 클릭 추적 링크가 포함됩니다. 이는 다음을 의미합니다:

- 원래 Campaign 오디언스에 포함되지 않은 사람이 전달된 이메일을 수신하고 열면, Braze가 열람 이벤트를 기록합니다.
- 전달된 이메일의 링크를 클릭하면, Braze가 클릭 이벤트를 기록합니다.
- 이러한 이벤트는 전달된 이메일을 수신한 사람이 아닌 원래 수신자의 프로필에 귀속됩니다. 추적 픽셀과 링크가 원래 수신자에게 연결되어 있기 때문입니다.

Braze는 원래 수신자의 열람 및 클릭과 전달된 사본을 수신한 사람의 열람 및 클릭을 구분할 수 없습니다. 이는 이메일 추적 픽셀의 표준 동작이며 모든 이메일 서비스 공급자에 영향을 미칩니다.

이메일 측정기준을 분석할 때, 전달 활동이 열람 및 클릭 수에 기여할 수 있다는 점을 인지하세요. 비정상적으로 높은 참여율이나 동일한 프로필에서 시간이 지남에 따라 반복되는 활동을 발견하면, 전달이 요인일 수 있습니다.

### 이메일 Campaign 또는 Canvas가 중지되면 어떻게 되나요? {#what-happens-when-an-email-campaign-or-canvas-is-stopped}

사용자는 Canvas에 진입하는 것이 방지되며, 추가 메시지는 발송되지 않습니다.

이메일 Campaigns 및 Canvases의 경우, 중지 버튼은 발송을 즉시 중지하지 않습니다. 발송 요청이 전송되면, 사용자에게 전달되는 것을 중지할 수 없으며, 이는 약간의 지연 후에 발생할 수 있습니다.

Campaign 또는 Canvas가 중지된 후에는 Braze가 추가 요청을 보내지 않지만, ESP가 이미 진행 중인 요청을 처리하는 동안 분석이 여전히 증가할 수 있습니다.

### 이메일 분석에서 _총 클릭 수_가 _총 열람 수_보다 많은 이유는 무엇인가요? {#why-am-i-seeing-more-_total-clicks_-than-_total-opens_-in-my-email-analytics}

_총 열람 수_는 사용자가 이메일을 열어본 횟수이고, _총 클릭 수_는 링크 클릭을 포함한 모든 유형의 클릭을 포함하여 사용자가 전달된 이메일 내에서 클릭한 횟수입니다. 다음과 같은 이유로 열람보다 클릭이 더 많을 수 있습니다:

- 사용자가 한 번의 열람 내에서 이메일 본문을 여러 번 클릭합니다.
- 사용자가 휴대폰의 미리보기 창에서 일부 이메일 링크를 클릭합니다. 이 경우 Braze는 이 이메일을 클릭된 것으로 기록하지만 열린 것으로는 기록하지 않습니다.
- 사용자가 이전에 미리 본 이메일을 다시 엽니다.

### 클릭 수가 클릭한 사용자의 Segment보다 높은 이유는 무엇인가요? {#why-are-my-click-counts-higher-than-my-segment-of-users-who-clicked}

Campaign 분석은 총 클릭 이벤트 수를 보여주고, Segments는 해당 클릭을 수행한 고유 사용자 수를 반환합니다. 각 사용자가 여러 번 클릭할 수 있으므로, 분석의 총 클릭 수는 Segment를 생성할 때 클릭한 사용자 수보다 높은 경우가 많습니다.

예를 들어, 100명의 사용자가 각각 링크를 3번 클릭하면, Campaign 분석은 300개의 총 클릭을 표시하지만, 해당 Campaign에 대해 "이메일 클릭"으로 필터링된 Segment는 100명의 사용자를 반환합니다.

### 이메일 열람 및 클릭이 0으로 표시되는 이유는 무엇인가요? {#why-am-i-seeing-zero-email-opens-and-clicks}

추적 도메인의 구성 오류가 있는 경우 이메일 열람이나 클릭이 표시되지 않을 수 있습니다. 이는 다음과 같은 이유 때문일 수 있습니다:
- 추적 URL이 `https` 대신 `http`인 SSL 문제가 있습니다.
- 열람 이벤트, 클릭 이벤트 또는 둘 다에서 사용자 에이전트 문자열이 채워지지 않는 CDN 문제가 있습니다.

### 비정상적인 이메일 열람 또는 클릭 동작이 보이는 이유는 무엇인가요? {#why-am-i-seeing-unusual-email-open-or-click-behavior}

이메일 열람 또는 클릭 측정기준에서 예상치 못한 패턴을 발견하는 경우(예: 단일 사용자가 모든 링크를 즉시 클릭하는 것처럼 보이거나, 열람이 예상대로 등록되지 않는 경우), 다음과 같은 일반적인 원인을 검토하세요:

#### 이메일 클리핑으로 추적 픽셀이 제거됨 {#email-clipping-removes-the-tracking-pixel}

수신자의 이메일 공급자(예: 약 102KB를 초과하는 메시지를 클리핑하는 Gmail)에 의해 이메일이 클리핑되면, 이메일 하단의 콘텐츠가 잘릴 수 있습니다. 열람 추적 픽셀은 일반적으로 이메일 하단에 삽입되므로, 클리핑으로 인해 열람 추적이 작동하지 않을 수 있습니다.

**식별 방법:** 이메일 하단에 "전체 메시지 보기" 또는 유사한 링크가 표시되는지 확인하세요. [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision)을 사용하여 전체 스크롤 가능한 이메일을 미리 보고 메시지가 클리핑되고 있는지 확인할 수 있습니다.

**해결 방법:** Braze에서 추적 픽셀을 이메일 하단 대신 상단에 배치하도록 구성할 수 있습니다. 추적 픽셀을 이동하면 일부 이메일 클라이언트가 HTML을 렌더링하는 방식에 영향을 줄 수 있으므로, 이 변경 후 Inbox Vision에서 이메일을 테스트하세요. 수신자가 이미지를 비활성화한 경우, 픽셀 배치에 관계없이 열람을 추적할 수 없습니다.

#### 추적 픽셀로 인해 이메일 상단에 흰색 간격이 발생함 {#tracking-pixel-causes-white-gap-at-top-of-email}

열람 추적 픽셀이 이메일 상단에 위치하면, 특히 모바일 기기에서 이메일 본문 상단에 눈에 보이는 흰색 선이나 간격이 나타날 수 있습니다.

**식별 방법:** Braze에서 **설정** > **이메일 환경설정**으로 이동하여 **열람 추적 픽셀** 섹션을 선택하세요. 발송 공급자에 대해 **SendGrid용 이동**, **SparkPost용 이동** 또는 **Amazon SES용 이동**이 활성화되어 있으면, 픽셀이 이메일 HTML 상단에 위치합니다. 렌더링된 이메일 상단에 흰색 간격이나 선이 보이면, 이 설정이 원인일 수 있습니다.

**해결 방법:** 발송 공급자의 **열람 추적 픽셀** 섹션에서 해당 **SendGrid용 이동**, **SparkPost용 이동** 또는 **Amazon SES용 이동** 토글을 끄세요. 추적 픽셀은 보통 이메일 하단에서 덜 눈에 띕니다. 배치를 변경한 후 [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision)에서 이메일을 테스트하세요. 자세한 내용은 [배치 업데이트]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#update-the-placement)를 참조하세요.

#### 지연된 통계 또는 열람 없는 클릭 {#delayed-stats-or-clicks-without-opens}

열람 추적은 수신자가 이미지가 활성화된 상태에서 이메일을 로드하는 것에 의존합니다. 일부 경우, 다음과 같은 이유로 통계가 지연되거나 해당 열람 없이 클릭이 기록될 수 있습니다:

- 수신자가 완전히 열지 않고 미리보기 창에서 이메일을 본 다음, 미리보기에서 직접 링크를 클릭합니다.
- 이메일 클라이언트가 수신자가 링크와 상호작용한 후에야 이미지(따라서 추적 픽셀)를 로드합니다.

#### 보안 소프트웨어가 링크 클릭을 시뮬레이션함 {#security-software-simulates-link-clicks}

일부 기업 이메일 보안 도구(예: Barracuda, Proofpoint 및 유사 서비스)는 메시지의 모든 링크를 자동으로 클릭하여 안전한지 확인함으로써 수신 이메일을 스캔합니다. 이로 인해 발송 후 몇 초 내에 클릭 이벤트가 나타날 수 있으며, 종종 이메일의 모든 링크가 빠르게 연속으로 클릭됩니다.

이 동작은 기관 이메일 도메인(예: 고등학교, 대학교, 기업 환경)에서 더 일반적이며, 발송 도메인이 추적 도메인과 크게 다를 때 더 가능성이 높습니다. [커스텀 브랜드 추적 도메인]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences)을 설정하면 이러한 자동 클릭의 빈도를 줄일 수 있습니다.

**식별 방법:** 클릭 이벤트의 IP 주소(Currents 데이터에서 확인 가능)를 검색 엔진에서 조회하세요. IP가 알려진 보안 공급자(예: Barracuda Networks)와 연관되어 있으면, 클릭은 자동화된 것일 가능성이 높습니다. 여러 자동 클릭에서 일관된 User-Agent 헤더를 볼 수도 있습니다.

보안 스캔이 이메일 측정기준에 미치는 영향에 대한 추가 컨텍스트는 [클릭률 증가 처리]({{site.baseurl}}/user_guide/channels/email/reporting)를 참조하세요.

### 서버 클릭을 트리거할 수 있는 잠재적 위험은 무엇인가요? {#what-are-the-potential-risks-of-triggering-server-clicks}

지나치게 긴 메시지나 너무 많은 느낌표와 같은 이메일 메시지의 특정 요소는 이메일 보안 응답을 트리거할 수 있습니다. 이러한 응답은 리포팅과 IP 평판에 영향을 미치고 사용자가 구독을 취소하게 만들 수 있습니다.

이러한 응답을 처리하는 모범 사례는 [클릭률 증가 처리]({{site.baseurl}}/user_guide/channels/email/reporting)를 참조하세요.

### Braze가 "탈퇴" 측정기준에 포함되는 구독 취소 링크를 추적할 수 있나요? {#can-braze-track-unsubscribe-links-counted-toward-the-unsubscribe-metric}

Braze는 이메일 내에서 다음 Liquid가 사용되는 경우 구독 취소 링크를 추적합니다: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}

### 구독 취소 링크의 클릭 수와 다른 구독 취소 수가 표시되는 이유는 무엇인가요? {#why-am-i-seeing-a-different-number-of-unsubscribes-than-clicks-on-my-unsubscribe-link}

이메일 본문의 구독 취소 링크를 클릭한 사용자보다 _구독 취소_ 수가 더 많은 경우, [**List-unsubscribe**]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#list-unsubscribe)가 그 차이를 설명하는 경우가 많습니다. List-unsubscribe는 이메일 헤더에 있는 추가 구독 취소 경로입니다(메시지 본문의 링크가 아님). 사용자가 이 방법으로 구독을 취소하면, _구독 취소_에 포함되지만 본문의 추적된 구독 취소 URL에 대한 클릭으로는 집계되지 않습니다.

본문 구독 취소 링크의 총 클릭 수가 _구독 취소_ 수보다 많은 경우, 사용자가 링크를 두 번 이상 클릭했을 수 있습니다. 예를 들어, 구독을 취소하고, 다시 구독한 다음, 다시 구독을 취소하면, 이메일 분석에서 클릭 분석에 여러 클릭이 기록될 수 있습니다.

사용자가 구독 취소 링크를 두 번 클릭하면(예: 구독 취소, 다시 구독, 다시 구독 취소), 이메일 분석에서 두 번으로 집계됩니다.

### 이메일에 "브라우저에서 이 이메일 보기" 링크를 추가할 수 있나요? {#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails}

아니요. Braze는 이 기능을 제공하지 않습니다. 이는 이메일의 대다수가 모바일 기기와 최신 이메일 클라이언트에서 열리며, 이미지와 콘텐츠를 문제없이 렌더링하기 때문입니다.

**해결 방법:** 동일한 결과를 얻으려면, 이메일의 콘텐츠를 외부 랜딩 페이지(예: 웹사이트)에 호스팅한 다음, 이메일 본문을 편집할 때 **링크** 도구를 사용하여 구축 중인 이메일 Campaign에서 링크할 수 있습니다.

### Braze가 일반 텍스트 URL이나 "www." 텍스트를 자동으로 링크로 변환하나요? {#does-braze-automatically-turn-plain-text-urls-or-www-text-into-links}

아니요. Braze는 메시지를 스캔하여 `www.`로 시작하거나 URL처럼 보이는 일반 텍스트를 하이퍼링크로 변환하지 않습니다. HTML 앵커 태그(`<a href="...">`)로 정의한 링크만 Braze의 일반 렌더링 및 링크 기능을 통해 처리됩니다.

수신자가 일반 텍스트가 클릭 가능한 링크로 표시되는 것을 보는 경우, 해당 동작은 보통 이메일 클라이언트(예: Gmail, Outlook 또는 Apple Mail)에서 발생합니다. 많은 클라이언트가 메시지가 전달된 후 URL과 유사한 문자열을 감지하여 수신자의 기기에서 링크로 변환합니다. Braze는 해당 동작을 제어하지 않으며 수신자를 위해 끌 수 없습니다.

예측 가능한 링크 외관, 추적 및 스타일링을 위해 일반 텍스트 URL 대신 명시적 `<a href>` 태그를 사용하세요.

### 이메일 링크의 `target` 속성을 제어할 수 있나요? {#can-i-control-the-target-attribute-on-email-links}

이메일 HTML의 링크에 `target` 속성(예: `target="_blank"` 또는 `target="_top"`)을 설정할 수 있지만, 대부분의 이메일 클라이언트는 이 속성을 무시하거나 재정의합니다. 예를 들어, Gmail은 지정한 것에 관계없이 사실상 `_blank`와 유사한 동작을 강제합니다.

이메일 클라이언트 동작이 다양하므로, 링크가 열리는 방식을 제어하기 위해 `target` 속성에 의존해서는 안 됩니다. 어떤 이메일 클라이언트가 `target` 속성을 지원하는지에 대한 자세한 내용은 [caniemail.com](https://www.caniemail.com/features/html-target/)을 참조하세요.

### 이메일 보안 소프트웨어에 의해 사용자가 자동으로 구독 취소되는 이유는 무엇인가요? {#why-are-my-users-being-auto-unsubscribed-by-email-security-software}

일부 기업 이메일 보안 도구(예: Barracuda, Proofpoint 및 유사 서비스)는 구독 취소 링크를 포함하여 수신 이메일의 모든 URL을 사전 가져오기하거나 스캔합니다. 보안 도구가 원클릭 list-unsubscribe 링크를 따라갈 때 의도하지 않은 구독 취소가 발생할 수 있습니다.

이를 완화하려면:

- **수신자에게 발송 도메인을 허용 목록에 추가하도록 권장하세요:** 영향을 받는 수신자의 IT 팀과 협력하여 발송 도메인과 Braze 추적 도메인을 이메일 보안 허용 목록에 추가하세요.
- **환경설정 센터를 사용하세요:** 직접 구독 취소 링크 대신, 구독 취소 작업을 확인하기 위해 사용자 상호작용이 필요한 [환경설정 센터]({{site.baseurl}}/user_guide/channels/email/subscriptions)를 사용하세요. 보안 스캐너는 일반적으로 다단계 양식을 완료하지 않습니다.
- **구독 취소 로그를 검토하세요:** Currents 구독 취소 이벤트 데이터에서 `User-Agent` 헤더와 IP 주소를 확인하여 자동 스캔과 일치하는 패턴(예: 여러 구독 취소에서 일관된 `User-Agent` 헤더)을 식별하세요.

서버 측 스캔이 이메일 측정기준에 미치는 영향에 대한 자세한 내용은 [클릭률 증가 처리]({{site.baseurl}}/user_guide/channels/email/reporting)를 참조하세요.

### 머신 열람율이 예상치 못하게 변경된 이유는 무엇인가요? {#why-has-my-machine-open-rate-changed-unexpectedly}

[머신 열람]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens)은 Apple Mail Privacy Protection(MPP)과 같은 이메일 보안 기능에 의해 트리거되며, 사용자가 실제로 이메일을 열지 않아도 이메일 콘텐츠(추적 픽셀 포함)를 사전 로드합니다. 머신 열람율은 다음에 따라 변동할 수 있습니다:

- Apple Mail 또는 기타 개인정보 보호 기능이 활성화된 이메일 클라이언트를 사용하는 오디언스 비율의 변화.
- 이메일 공급자의 개인정보 보호 기능 또는 봇 감지 동작의 업데이트.
- 오디언스 세분화 또는 타겟팅의 변경.

머신 열람 비율은 실제 참여의 신뢰할 수 있는 측정 수단이 아닙니다. 이메일 성능에 대한 보다 정확한 보기를 위해 *기타 열람*(비머신 열람)과 *고유 클릭*에 집중하세요. [이메일 성능 대시보드]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance)를 사용하여 시간에 따라 이러한 측정기준을 비교할 수도 있습니다.

### Gmail에서 딥링크가 작동하지 않는 이유는 무엇인가요? {#why-are-my-deep-links-not-working-in-gmail}

Gmail은 이메일 메시지에서 모든 비HTTP/HTTPS 링크를 제거합니다. 딥링크가 커스텀 스킴(예: `myapp://path/to/content`)을 사용하는 경우, Gmail이 이를 제거하고 Gmail에서 이메일을 읽는 수신자에게 링크가 작동하지 않습니다. 이는 Braze의 제한이 아닌 Gmail의 제한입니다.

이를 해결하려면:

- **Universal Links(iOS) 또는 App Links(Android)를 사용하세요.** 이들은 앱이 설치된 경우 앱을 열고 그렇지 않으면 웹 페이지로 폴백하는 표준 `https://` URL을 사용합니다. 설정 지침은 [Universal Links 및 App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links)를 참조하세요.
- **딥링킹 공급자를 사용하세요.** [Branch](https://www.branch.io/)와 같은 서비스는 Gmail을 포함한 이메일 클라이언트와 호환되는 HTTP 형식의 딥링크를 생성합니다.
- **리디렉트 엔드포인트를 설정하세요.** 서버에 앱의 커스텀 스킴 URL로 리디렉트하는 `https://` 엔드포인트를 호스팅하세요. 이메일 클라이언트는 `https://` 링크를 보존하고, 리디렉트가 앱 열기를 처리합니다.

### *고유 열람* 측정기준에 *머신 열람*이 포함되나요? {#does-the-unique-opens-metric-include-machine-opens}

네. *고유 열람*에는 *머신 열람*이 포함됩니다. **Campaign 분석** 보기와 **보고서 빌더**에서 두 측정기준을 모두 확인할 수 있습니다.

이것이 **전환 대시보드** 기여도에 미치는 영향에 대해서는 전환 대시보드 페이지의 [문제 해결]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#troubleshooting)에서 [이메일 열람 합계가 Campaign 분석과 일치하지 않는 이유는 무엇인가요?]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#why-dont-email-open-totals-match-campaign-analytics)를 참조하세요.

### 이메일 전달량이 발송량과 일치하지 않는 이유는 무엇인가요? {#why-does-my-email-delivery-volume-not-match-my-send-volume}

이메일이 발송된 후, 수신자의 받은편지함이 전달 시점을 결정합니다. 사서함 가득 참, 특정 IP에서의 ESP 스로틀링 등의 이유로 메시지가 몇 시간 또는 며칠 동안 지연될 수 있습니다.

지연된 메시지가 발송일과 다른 달력 날짜에 전달되면, 동일한 날짜 범위에서 _전달_이 _발송_을 초과할 수 있습니다. 많은 지연이 하루에 집중되면, 해당 범위에서 _발송_이 _전달_을 초과할 수 있습니다.

### 이메일에 이미 구독 취소 링크가 있는데 구독 취소 링크를 포함하라는 경고가 표시되는 이유는 무엇인가요? {#why-am-i-seeing-a-warning-to-include-an-unsubscribe-link-when-my-email-already-has-one}

이 경고는 구독 취소 링크가 없었던 Campaign에서 복제된 Campaigns에서 지속될 수 있습니다. 이를 해결하려면:

- HTML 이메일의 경우, **일반 텍스트** 탭으로 이동한 다음 **HTML에서 재생성**을 선택하세요.
- 복제 후, 배리언트를 복제한 다음 원본 배리언트를 제거하세요. 원본 배리언트를 **선택하지 마세요**. 그렇지 않으면 경고가 이어질 수 있습니다.

### 사용자가 수신하지 말아야 할 이메일을 수신한 이유는 무엇인가요? {#why-did-a-user-receive-an-email-they-shouldnt-have}

Braze가 구성된 대로 동작했더라도 전달이 잘못된 것처럼 보일 수 있습니다. 다음을 확인하세요:

- 하나의 받은편지함을 공유하는 **중복 프로필**([이메일이 발송될 때 여러 프로필이 동일한 이메일 주소를 가지고 있으면 어떻게 되나요?](#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address) 참조).
- 오디언스에 포함되거나 CC/BCC로 발송에 포함된 **시드 목록, 테스트 수신자 또는 내부 주소**.
- **Segment 또는 Canvas 타이밍:** Braze가 자격을 평가할 때 사용자가 오디언스 또는 Canvas 단계에 일치했지만, 메시지를 읽기 전에 속성 또는 구독 상태가 변경되었습니다.
- **구독 그룹:** 글로벌 구독 상태가 달리 제안하더라도 사용자가 메시지가 타겟팅한 그룹에 옵트인 상태를 유지했습니다.
- 세분화 후 변경 사항이 적용될 것으로 예상하기 전에 사용자를 업데이트한 **API 또는 파일 가져오기**.

[메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), Campaign 또는 Canvas 체인지로그, Segment 정의를 검토하세요. 발송을 여전히 조정할 수 없는 경우, 사용자 식별자, `dispatch_id`(가능한 경우) 및 타임스탬프와 함께 Braze 지원팀에 문의하세요.

### 사용자가 이메일 메시지를 수신하지 못한 이유는 무엇인가요? {#why-hasnt-a-user-received-my-email-message}

사용자가 수신할 것으로 예상한 이메일을 수신하지 못하는 데는 다음과 같은 여러 이유가 있습니다:

- 이메일을 수신할 자격이 없었습니다.
- 이메일 주소가 유효하지 않거나 존재하지 않습니다.
- 메시지를 놓치거나 삭제했을 수 있습니다.
- 메시지가 스팸 폴더에 있을 수 있습니다.

{% alert tip %}
Braze의 전달 이벤트는 이메일이 사서함 공급자의 서버에 의해 수락되었음을 의미합니다. 그러나 이것이 메시지가 사용자의 받은편지함에 나타나는 것을 보장하지는 않습니다. 사서함 공급자는 메시지를 스팸으로 라우팅하거나, 드문 경우 메시지 표시를 조용히 방지할 수 있습니다.
{% endalert %}

다음 표를 사용하여 원인을 좁혀보세요.

#### 이메일이 발송되지 않음 {#the-email-wasnt-sent}

| 가능한 원인 | 확인 사항 |
|---|---|
| 사용자가 Campaign 또는 Canvas에 대한 자격이 없었습니다 | **Target Audiences**(Campaigns의 경우) 또는 **Target Audience**(Canvas의 경우) [설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)을 확인하여 사용자가 발송 시점에 모든 오디언스 필터, Segment 기준 및 전달 규칙을 충족했는지 확인하세요. |
| 메시지가 중단되었습니다 | [메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)에서 Liquid 오류 또는 필수 필드 누락과 같은 중단 이유를 확인하세요. |
| 사용자의 이메일 주소가 유효하지 않거나 누락되었습니다 | **사용자 검색**에서 사용자의 프로필을 확인하여 발송 시점에 유효한 이메일 주소가 파일에 있었는지 확인하세요. |
| 사용자의 이메일 주소가 이전에 하드 바운스되었습니다 | 하드 바운스는 이메일 주소를 유효하지 않은 것으로 표시하고 해당 주소로의 향후 발송을 방지합니다. 마찬가지로, 수신자가 이메일을 스팸으로 표시하면, Braze는 표준 Campaigns가 아닌 트랜잭션 이메일만 해당 사용자에게 발송합니다. 사용자 프로필의 **참여** 탭을 확인하세요. 자세한 내용은 [구독 취소된 이메일 주소]({{site.baseurl}}/user_guide/channels/email/subscriptions#unsubscribed-email-addresses) 및 [반송 및 유효하지 않은 이메일]({{site.baseurl}}/user_guide/channels/email/subscriptions#bounces-and-invalid-emails)을 참조하세요. |
| 사용자가 이메일 구독을 취소했습니다 | **참여** 탭의 **연락처 설정**에서 사용자의 구독 상태를 확인하세요. Braze는 구독을 취소한 사용자에게 이메일을 발송하지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="이메일이 발송되지 않은 원인" }

#### 이메일이 발송되었지만 받은편지함에 도착하지 않음 {#the-email-was-sent-but-didnt-arrive-in-their-inbox}

| 가능한 원인 | 확인 사항 |
|---|---|
| 사서함 공급자(MBP)에 연결할 수 없었습니다 | 일시적인 문제로 이메일이 수신자의 MBP에 도달하지 못했습니다. 이는 일반적으로 재시도를 통해 자체적으로 해결됩니다. 이메일 서비스 공급자는 최대 72시간 동안 소프트 바운스를 재시도합니다. |
| MBP가 이메일을 반송했습니다 | 수신자의 메일 서버가 이메일을 거부했습니다. [메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)에서 반송 세부 정보를 검토하세요. |
| MBP가 이메일을 조용히 삭제했습니다 | MBP가 이메일을 수락했지만 사용자에게 표시하지 않았고 반송도 반환하지 않았습니다. 이는 Braze의 통제 범위 밖이며 Braze 로그에서 감지할 수 없습니다. |
| 이메일이 스팸 폴더로 이동했습니다 | MBP가 메시지를 스팸으로 식별하여 사용자의 스팸 또는 정크 폴더로 라우팅했습니다. 사용자에게 스팸 폴더를 확인하도록 요청하세요. |
| 수신자에게 커스텀 메일 필터링이 있습니다 | 사용자 또는 IT 관리자가 수신 메시지를 필터링, 리디렉트 또는 삭제하는 사서함 규칙을 구성했을 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="이메일이 받은편지함에 없는 원인" }

### 반송 목록에서 이메일 주소를 제거하려면 어떻게 하나요? {#how-can-i-remove-an-email-address-from-the-bounce-list}

유효한 이메일 주소가 Braze에서 유효하지 않은 것으로 표시되는 경우(일반적으로 이메일 서비스 공급자의 하드 바운스 후), [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces) 엔드포인트를 사용하세요. 이렇게 하면 Braze 반송 목록과 이메일 공급자가 유지하는 반송 목록에서 주소가 제거됩니다. 그러면 Braze가 해당 주소로의 발송을 재개합니다.

주소가 하드 바운스가 아닌 스팸으로 표시된 경우, 대신 [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam) 엔드포인트를 사용하세요.

자세한 내용은 [반송 및 유효하지 않은 이메일]({{site.baseurl}}/user_guide/channels/email/subscriptions#bounces-and-invalid-emails) 및 [반송 또는 스팸 목록에서 이메일 주소 제거]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps#remove-an-email-address-from-your-bounce-or-spam-list)를 참조하세요.

### 이메일 전달 가능성 문제를 해결하려면 어떻게 하나요? {#how-do-i-troubleshoot-email-deliverability-issues}

이메일이 지연, 연기 또는 반송되는 경우, [메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)에서 반송 및 연기 세부 정보를 검토한 다음, 전달 체인에서 문제가 발생하는 위치를 식별하세요. 일반적인 전달 가능성 문제는 네 가지 범주로 나뉩니다:

#### ESP 사용량 제한 응답 읽기 {#reading-esp-rate-limit-responses}

이메일 서비스 공급자(ESP)(예: Amazon SES, SparkPost 또는 SendGrid)는 메시지를 수락하거나 연기할 때 SMTP 응답 코드를 반환합니다. 사용량 제한 응답은 일반적으로 일시적 실패를 나타내는 4xx 코드를 사용합니다:

- **421:** 서비스 일시적으로 사용 불가, 높은 볼륨, 연결 제한 또는 서버 리소스 제약으로 인한 경우가 많습니다. 메시지는 대기열에 남아 있으며 ESP가 자동으로 전달을 재시도합니다.
- **429:** API 사용량 제한 초과. 허용된 시간 창 내에 너무 많은 요청을 보냈습니다.
- **450 / 451:** 볼륨 또는 연결로 인한 일시적 연기. 수신 서버가 속도를 줄이도록 요청하고 있습니다.

[메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) 또는 ESP 대시보드에서 이러한 코드를 볼 때, 영향을 받는 도메인으로의 발송량을 줄이고 점진적으로 더 긴 재시도 간격을 사용하세요. 사용량 제한이 적용된 상태에서 전체 볼륨으로 계속 발송하면 일시적 연기가 영구적 거부로 확대될 수 있습니다.

#### 사서함 공급자 사용량 제한 {#mailbox-provider-rate-limits}

사서함 공급자는 Braze의 발송 제어와 별도로 수신 메일에 대한 자체 사용량 제한을 적용합니다. 이러한 제한은 엄격할 수 있으며 직접 제어할 수 없습니다:

- Virgin Media / NTL(영국): `421 4.1.1 MXIN503 Hourly ratelimit for your IP exceeded` 오류를 트리거하는 시간별 사용량 제한을 사용합니다. 이러한 제한은 저볼륨 발신자에게도 영향을 미칠 수 있습니다. 해당 IP를 공유하는 모든 발신자에 대해 IP 수준에서 적용됩니다.
- Gmail, Yahoo, iCloud, Microsoft: 각 공급자는 발신자 평판, 볼륨 및 참여 패턴에 기반한 독자적인 스로틀링 임계값을 가지고 있습니다.

공급자별 사용량 제한이 발생하면, 더 긴 기간에 걸쳐 발송을 배치하거나 사서함 공급자별로 세분화하여 볼륨을 더 점진적으로 분산하는 것을 고려하세요. 수신자 목록에서 하나의 공급자에 집중되어 있는지 확인하세요. 대부분의 수신자가 하나의 도메인을 사용하는 경우, 전달을 분산하세요.

#### 바이러스 백신 스캔으로 인한 기업 이메일 지연 {#corporate-email-delays-from-antivirus-scanning}

비즈니스 이메일 주소는 전달 전에 메시지를 스캔하는 기업 보안 게이트웨이를 통과하는 경우가 많습니다. 이로 인해 특히 다음과 같은 메시지의 경우 이메일이 15~20분 이상 지연될 수 있습니다:

- 대용량 첨부 파일
- 익숙하지 않은 도메인으로의 링크
- 피싱 패턴과 유사한 콘텐츠

이러한 지연은 보안 시스템이 격리된 샌드박스 환경에서 행동 분석을 위해 메시지를 대기열에 넣기 때문에 발생합니다. 대량의 메일이 동시에 도착하면, 메시지가 분석을 위해 대기열에 들어가고 지연이 더 길어집니다. 이는 기업 이메일 보안의 정상적인 동작이며 우회할 수 있는 것이 아닙니다. 기업 수신자에게 시간에 민감한 메시지를 보낼 때, 커뮤니케이션 타임라인에 이 처리 시간을 고려하세요.

#### Google 421 4.7.28 사용량 제한 오류 문제 해결 {#troubleshooting-google-421-4728-rate-limit-errors}

Gmail은 IP 주소, 발송 IP 범위, SPF 도메인, DKIM 도메인 또는 URL 도메인에서 비정상적인 비율의 원치 않는 이메일을 감지하면 `421-4.7.28` 오류를 반환합니다. 이는 영구적 차단이 아닌 일시적 스로틀이지만, 발송 볼륨, 속도 또는 평판이 Gmail의 현재 기대치를 충족하지 못한다는 신호입니다.

이 오류를 수신하면:

1. 24~48시간 동안 비필수 발송을 즉시 중지하세요. 스로틀이 적용된 상태에서 계속 발송하면 문제가 확대되어 영구적 550 거부로 이어질 수 있습니다.
2. SPF, DKIM 및 DMARC가 올바르게 구성되어 있고 From: 헤더가 인증과 일치하는지 확인하세요.
3. [Google Postmaster Tools](https://postmaster.google.com/)와 Braze [전달 가능성 센터]({{site.baseurl}}/user_guide/analytics/dashboards/deliverability_center)(Google Postmaster 연결 후)에서 도메인의 준수 상태와 스팸 불만율을 확인하세요. 사용자 보고 스팸률은 0.1% 미만이어야 합니다(하드 상한은 0.3%).
4. 중지 후, 가장 참여도가 높은 수신자에게만 이전 볼륨의 10~20%로 발송을 재개하세요. 추가 4xx 오류가 발생하지 않는 경우에만 몇 주에 걸쳐 천천히 볼륨을 늘리세요.

추가 지침은 [Google의 대량 이메일 발신자 가이드라인](https://support.google.com/mail/answer/81126)을 참조하세요.

### Outlook에서 이미지를 최적화하려면 어떻게 하나요? {#how-can-i-optimize-images-in-outlook}

Outlook은 표준 브라우저 렌더링 대신 Microsoft Word 렌더링을 사용하는 경우가 많아 이미지가 잘못 렌더링되거나 이미지 주위에 테두리가 추가될 수 있습니다. 이 동일한 클라이언트별 렌더링은 다양한 이메일 클라이언트에서 [대체 텍스트가 표시되는 방식]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#how-email-clients-display-alt-text)에도 영향을 미칩니다.

Outlook에서 이미지가 예상 너비보다 크게 표시되는 경우, 이미지에 다음 CSS를 추가하세요:

```css
max-width: 100%;
```

예시:

```html
<img src="your-image.png" style="max-width: 100%;" alt="Description">
```

조건부 주석을 사용하여 Outlook 데스크톱에서 콘텐츠를 숨길 수도 있습니다:

```html
<!--[if !mso]><!-- -->
<span>Content hidden in Outlook desktop</span>
<!--<![endif]-->
```

### 이메일 메시지에 SVG 또는 WebP 이미지를 사용할 수 있나요? {#can-i-use-svg-or-webp-images-in-my-email-messages}

SVG 이미지는 이메일 클라이언트 간의 제한된 지원으로 인해 이메일에 권장되지 않습니다. Gmail 및 기타 여러 주요 이메일 공급자는 SVG 이미지를 렌더링하지 않으므로, 수신자에게 깨지거나 누락된 이미지가 표시될 수 있습니다. WebP도 클라이언트 간에 일관되게 지원되지 않습니다.

대신, 이미지가 안정적으로 렌더링되도록 PNG 또는 JPEG와 같이 널리 지원되는 형식을 사용하세요.

### 이메일에 비디오를 삽입할 수 있나요? {#can-i-embed-videos-in-emails}

삽입된 비디오는 Gmail, Outlook, Yahoo와 같은 많은 인기 이메일 클라이언트에서 기본적으로 지원되지 않습니다. 따라서 삽입된 비디오 요소가 의도한 대로 표시되지 않거나 전혀 나타나지 않을 수 있습니다. 또한 이메일에 비디오를 직접 삽입하면 이메일 크기가 크게 증가하여 메시지가 스팸으로 표시될 가능성이 높아집니다.

대신, 비디오 플레이어에서 비디오처럼 보이는 GIF 또는 정적 이미지를 만든 다음, 해당 이미지를 비디오에 링크할 수 있습니다. 사용자가 이미지를 클릭하면, 웹사이트 또는 비디오 플랫폼에 호스팅된 비디오로 이동합니다. Braze는 지원되는 이메일 클라이언트에서 자동 재생되는 최적화된 비디오 콘텐츠를 제공하는 [Playable]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/playable)과의 통합도 지원합니다.

### 메시지 작성기의 한 부분에서 할당된 Liquid 변수를 다른 부분에서 사용할 수 있나요? {#can-liquid-variables-assigned-in-one-part-of-the-message-composer-be-used-in-another}

아니요. 이메일의 각 부분(제목, 본문, 헤더, 버튼 등)은 별도로 생성되므로, 한 필드에서 할당된 Liquid는 다른 필드에서 사용할 수 없습니다. 필요한 각 필드에서 변수를 할당하세요.

### 이메일 템플릿이 없습니다. 어디에 있나요? {#my-email-template-is-missing-where-is-it}

먼저, 템플릿을 볼 수 있는 [사용자 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)이 있는지 확인하세요. 저장된 이메일 템플릿을 보려면 **콘텐츠** > **이메일**로 이동하세요. 상태 및 유형(HTML 또는 드래그 앤 드롭)별로 템플릿을 필터링할 수 있습니다.

### 릴레이 또는 마스킹된 이메일에 대해 도메인을 등록해야 하나요? {#do-i-need-to-register-domains-for-relay-or-masked-emails}

[Apple의 Private Email Relay]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/email_private_relay_apple_SSO)는 반송을 방지하기 위해 Apple Developer Portal에 발송 도메인을 등록해야 합니다. Google Shielded Email은 수동 도메인 등록이나 허용 목록 프로세스가 필요하지 않습니다.


### 이메일 제목란이나 프리헤더에 하이퍼링크를 추가할 수 있나요? {#can-i-add-hyperlinks-in-email-subject-lines-or-preheaders}

아니요. 이메일 제목란에 하이퍼링크를 추가하는 것은 사서함 공급자에서 지원되지 않습니다. 일부 사서함 공급자는 제목란을 자동으로 스캔하여 실제 주소, 날짜 또는 시간을 클릭 가능한 링크로 변환하지만, 이는 수신자의 기기에서 자동으로 발생하며 Braze(또는 모든 ESP)의 통제 범위 밖입니다.

마찬가지로, 프리헤더 내에 하이퍼링크를 추가하는 것은 이메일 업계 전반에서 지원되지 않습니다.

제목란이나 프리헤더 영역에서 클릭 가능한 콘텐츠와 유사한 기능이 필요한 경우, [Gmail 프로모션]({{site.baseurl}}/user_guide/channels/email/html_editor/gmail_promotions_tab)을 사용하여 Gmail 사용자를 위한 이메일에 인터랙티브 주석을 추가하는 것을 고려하세요.

### 반송 이유 `unable to get mx info` 또는 `failed to get IPs from PTR record`는 무엇을 의미하나요? {#what-does-the-bounce-reason-unable-to-get-mx-info-or-failed-to-get-ips-from-ptr-record-mean}

[메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)에서 다음과 유사한 반송 이유는 Braze 메시지 구성이 아닌 수신 도메인의 메일 설정(주소의 `@` 뒤 도메인)을 확인하는 데 문제가 있음을 나타냅니다:

일반적인 원인은 다음과 같습니다:

- 해당 도메인에 대한 **MX 레코드**가 누락, 잘못되었거나 연결할 수 없음
- 수신 인프라에서 예상하는 **PTR(역방향 DNS)** 검사에 실패하거나 확인되지 않는 인바운드 메일 호스트 이름
- 이메일 주소의 유효하지 않거나 잘못 입력된 도메인

**다음 단계:**

- 주소와 도메인 철자를 확인하세요.
- 주소가 올바른 경우, 해당 도메인의 사서함 소유자 또는 IT 팀에 문의하세요.
- DNS 공급자와 함께 메일 서버의 PTR 레코드를 포함한 MX 및 관련 DNS 레코드를 감사하도록 요청하세요.

다른 수신자는 보통 영향을 받지 않습니다. 소프트 바운스가 리포팅에 나타나는 방식에 대해서는 [소프트 바운스]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary#soft-bounce)를 참조하세요.

### Braze에서 자신에게 이메일을 보낼 때 스팸 알림이 표시되는 이유는 무엇인가요? {#why-do-i-get-a-spam-alert-when-sending-an-email-from-braze-to-myself}

Braze에서 자신의 이메일 주소로 테스트 이메일을 보내고 스팸 경고 또는 피싱 알림(예: "발송 도메인이 회사 도메인과 유사하지만 인식할 수 없습니다")이 표시되는 경우, 이는 Braze 설정의 오류가 아닌 일반적인 피싱 방지 보안 기능입니다.

이 알림은 일반적으로 이메일의 발송 도메인이 수신자 도메인과 일치할 때(예: 둘 다 `@yourcompany.com`인 경우) 나타납니다. 이메일 보안 시스템은 사기꾼이 수신자의 회사 도메인과 유사한 도메인을 스푸핑하는 경우가 많기 때문에 이를 플래그합니다.

이메일이 올바르게 구성되었는지 확인하려면:

1. 이메일 클라이언트에서 원본 메시지(원시 이메일 헤더)를 확인하세요.
2. SPF, DKIM 및 DMARC 인증이 모두 통과하는지 확인하세요.
3. 세 가지 모두 통과하면, Braze 이메일 발송이 올바르게 구성된 것입니다.

이 알림이 나타나지 않도록 하려면:

IT 팀에 회사의 이메일 보안 서비스 또는 메일 게이트웨이에서 Braze 발송 도메인과 IP 주소를 허용 목록에 추가하도록 요청하세요. 이렇게 하면 보안 시스템이 Braze 발송 인프라에서 오는 이메일을 신뢰하도록 합니다.