---
nav_title: 프로모션 코드
article_title: 프로모션 코드
page_order: 5
toc_headers: h2
alias: "/promotion_codes/"
description: "프로모션 코드 목록에 대해 알아보고, 캠페인과 캔버스에 추가하는 방법을 확인하세요."
---

# 프로모션 코드 {#promotion-codes}

> 프로모션 코드 목록에 대해 알아보고, 캠페인과 캔버스에 추가하는 방법을 확인하세요.

## 프로모션 코드 정보 {#about-promotion-codes}

프로모션 코드를 사용하면 메시지에 고유하고 시간이 제한된 값을 삽입하여 전환을 유도할 수 있습니다. 각 목록에는 최대 2천만 개의 코드를 보관할 수 있으며, 각 코드는 만료되기 전 최대 6개월 동안 유효합니다.

Braze가 프로모션 코드가 포함된 메시지를 발송할 때, 코드는 메시지가 발송되기 전에 차감됩니다. 코드가 일관되고 고유하며 재사용되지 않도록 하기 위해 다음 사항을 유의하세요:

- 발송에 실패한 메시지도 코드를 소비합니다.
- 멀티채널 발송에서는 동일한 코드가 모든 채널에 적용됩니다.
- 조건부 Liquid를 사용할 경우, 하나의 분기만 표시되더라도 참조된 모든 목록에서 코드가 차감됩니다.
- Canvas 단계에 진입하거나 재진입하면 새로운 코드가 소비됩니다.

동일한 목록에서 여러 스니펫을 하나의 메시지에 배치하면, Braze는 모든 스니펫에 동일한 코드를 적용합니다. 코드가 부족해지는 것을 방지하려면, 사용 예상량보다 더 많은 코드를 업로드하는 것을 권장합니다.

{% tabs local %}
{% tab 예시 %}
프로모션 코드를 우체국의 쿠폰이라고 생각해 보세요. 직원이 편지에 쿠폰을 한 장 꺼내 붙이면, 편지가 도착하지 않더라도 그 쿠폰은 사라집니다.

예를 들어, 다음 조건부 Liquid에서 각 사용자는 하나의 분기만 보지만, 두 목록(`vip-deal`과 `regular-deal`) 모두에서 코드가 차감됩니다:

{% raw %}
```liquid
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert important %}
프로모션 코드는 인앱 메시지 Campaign에서 얼리 액세스 기능으로 사용할 수 있지만, Canvas의 인앱 메시지에서는 발송할 수 없습니다.
{% endalert %}

## 다음 단계 {#next-steps}

다음 단계를 찾고 계신가요? 여기에서 시작하세요:

{% article_tiles %}
- name: 프로모션 코드 목록 생성
  link: /docs/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create
- name: 프로모션 코드 사용
  link: /docs/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#using-promotion-codes
- name: 프로모션 코드 사용량 확인
  link: /docs/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#viewing-promotion-code-usage
{% endarticle_tiles %}

## 자주 묻는 질문 {#frequently-asked-questions}

### 프로모션 코드에 사용할 수 있는 메시징 채널은 무엇인가요? {#which-messaging-channels-can-i-use-with-promotion-codes}

프로모션 코드는 이메일, 모바일 푸시, 웹 푸시, Content Cards, 웹훅, 단문 메시지 서비스, WhatsApp에서 지원됩니다. In-App Messages Campaign에서는 얼리 액세스 기능으로 프로모션 코드를 지원합니다. Braze 트랜잭션 이메일 Campaign과 Canvas의 인앱 메시지에서는 프로모션 코드를 지원하지 않습니다.

### 테스트 및 시드 그룹 발송도 사용량에 포함되나요? {#do-test-and-seed-sends-count-towards-usage}

기본적으로 테스트 발송과 시드 그룹 이메일 발송은 사용자당, 테스트 발송당 프로모션 코드를 사용합니다. 다만 테스트 중 프로모션 코드를 사용하지 않도록 동작을 변경하려면 Braze 계정 매니저에게 문의하실 수 있습니다.

### 여러 메시징 채널에서 동일한 프로모션 코드 스니펫을 사용하면 어떻게 되나요? {#what-happens-when-multiple-messaging-channels-use-the-same-promotion-code-snippet}

특정 사용자가 여러 채널을 통해 코드를 받을 자격이 있는 경우, 각 채널에서 동일한 코드를 받습니다. 수신한 채널 수와 관계없이 프로모션 코드는 하나만 사용됩니다.

### 하나의 메시지에서 동일한 프로모션 코드 목록을 참조하는 여러 Liquid 스니펫을 사용할 수 있나요? {#can-i-use-multiple-liquid-snippets-to-reference-the-same-promotion-code-list-in-one-message}

네. Braze는 메시지 내 해당 스니펫의 모든 인스턴스에 동일한 프로모션 코드를 적용하여 사용자가 하나의 고유한 코드만 받도록 합니다.

### 프로모션 코드 목록이 만료되거나 비어 있으면 어떻게 되나요? {#what-happens-when-a-promotion-code-list-is-expired-or-empty}

만료된 코드는 6개월 후 삭제됩니다.

메시지에 비어 있거나 만료된 목록의 프로모션 코드가 포함되어야 했다면, 해당 메시지는 취소됩니다.

메시지에 프로모션 코드를 조건부로 삽입하는 Liquid 로직이 포함된 경우, 프로모션 코드가 포함되어야 하는 경우에만 메시지가 취소됩니다. 프로모션 코드가 포함되지 않아야 하는 경우에는 메시지가 정상적으로 발송됩니다.

### 잘못된 프로모션 코드를 업로드한 경우 업데이트할 수 있나요? {#if-i-uploaded-the-wrong-promotion-codes-can-i-update-them}

잘못된 코드를 업로드한 경우, 다음 두 가지 방법으로 해결할 수 있습니다:

- **전체 목록 폐기:** 현재 목록을 모든 Campaign, Canvases 또는 템플릿에서 사용 중단합니다. 그런 다음 올바른 코드를 새 목록에 업로드하고 모든 메시지를 새 목록을 사용하도록 전환합니다.
- **잘못된 코드 소진:** 잘못된 목록의 코드를 플레이스홀더 사용자에게 보내는 Campaign을 생성하여 잘못된 코드가 모두 소진될 때까지 발송합니다. 그 후 잘못된 코드를 제외하고 올바른 코드를 동일한 목록에 다시 업로드합니다.

목록 업데이트에 대한 일반적인 안내는 [프로모션 코드 목록 업데이트]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create#updating-a-promotion-code-list)를 참조하세요.

### Braze는 어떤 사용자가 어떤 프로모션 코드를 받았거나 사용했는지 추적하나요? {#does-braze-track-which-users-received-or-redeemed-which-promotion-codes}

메시지에서 프로모션 코드를 사용하면 Braze는 해당 코드를 소비됨으로 표시하여 다시 발송되지 않도록 하고, 목록의 잔여 수량을 업데이트합니다. Braze는 발송된 코드의 보고서를 유지하거나, 각 코드를 받은 특정 사용자를 추적하거나, 코드가 사용(리딤)되었는지 여부를 추적하지 않습니다.

코드를 사용자와 연결하거나 사용 이력을 직접 추적해야 하는 경우 다음 방법을 사용할 수 있습니다:

- 사용자 업데이트 단계를 통해 프로모션 코드를 고객 프로필에 저장합니다. 자세한 내용은 [프로모션 코드를 고객 프로필에 저장하기]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#save-to-profile)를 참조하세요.
- `message_extras` Liquid 태그를 사용하여 프로모션 코드 값을 Currents로 전송합니다. 자세한 내용은 [프로모션 코드 정보를 Currents로 전송하기]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras#sending-promotion-code-information-to-currents)를 참조하세요.

### 프로모션 코드를 사용자 프로필에 저장하여 이후 메시지에서 사용할 수 있나요? {#can-i-save-a-promotion-code-to-a-users-profile-for-future-messages}

네. 사용자 업데이트 단계를 통해 프로모션 코드를 고객 프로필에 저장할 수 있습니다. 자세한 내용은 [프로모션 코드를 고객 프로필에 저장하기]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#save-to-profile)를 참조하세요.