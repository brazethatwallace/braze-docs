---
nav_title: 프로모션 코드
article_title: 프로모션 코드
page_order: 5
toc_headers: h2
alias: "/promotion_codes/"
description: "프로모션 코드 목록에 대해 알아보고, 캠페인과 캔버스에 추가하는 방법을 확인하세요."
---

# 프로모션 코드

> 프로모션 코드 목록에 대해 알아보고, 캠페인과 캔버스에 추가하는 방법을 확인하세요.

## 프로모션 코드 소개

프로모션 코드를 사용하면 메시지에 고유하고 시간 제한이 있는 값을 삽입하여 전환을 유도할 수 있습니다. 각 목록에는 최대 2,000만 개의 코드를 저장할 수 있으며, 모든 코드는 만료되기 전까지 최대 6개월 동안 유효합니다.

Braze가 프로모션 코드가 포함된 메시지를 발송할 때, 메시지가 전송되기 전에 코드가 차감됩니다. 코드의 일관성, 고유성, 재사용 방지를 위해 다음 사항을 참고하세요:

- 메시지 전송에 실패하더라도 코드는 소비됩니다.
- 멀티채널 발송 시, 동일한 코드가 모든 채널에 적용됩니다.
- 조건부 Liquid를 사용하는 경우, 하나의 분기만 표시되더라도 참조된 모든 목록에서 코드가 차감됩니다.
- 캔버스 단계에 진입하거나 재진입하면 새로운 코드가 소비됩니다.

하나의 메시지에 동일한 목록의 스니펫을 여러 개 배치하면, Braze는 모든 스니펫에 동일한 코드를 적용합니다. 코드가 부족해지는 것을 방지하려면, 예상 사용량보다 더 많은 코드를 업로드하는 것을 권장합니다.

{% tabs local %}
{% tab 예시 %}
프로모션 코드를 우체국의 쿠폰이라고 생각해 보세요. 직원이 편지에 넣을 쿠폰을 더미에서 꺼내면, 편지가 도착하지 않더라도 그 쿠폰은 사라집니다.

예를 들어, 다음 조건부 Liquid에서는 각 사용자가 하나의 분기만 보더라도 두 목록(`vip-deal`과 `regular-deal`) 모두에서 코드가 차감됩니다:

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
프로모션 코드는 캔버스의 인앱 메시지에서는 발송할 수 없습니다.
{% endalert %}

## 다음 단계

다음 단계를 찾고 계신가요? 여기서 시작하세요:

- [프로모션 코드 목록 생성]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create/)
- [프로모션 코드 사용]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage/#using-promotion-codes)
- [프로모션 코드 사용량 확인]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage/#viewing-promotion-code-usage)

## 자주 묻는 질문

### 프로모션 코드와 함께 사용할 수 있는 메시징 채널은 무엇인가요?

프로모션 코드는 현재 이메일, 모바일 푸시, 웹 푸시, 콘텐츠 카드, 웹훅, SMS, WhatsApp에서 지원됩니다. Braze 트랜잭션 이메일 캠페인과 인앱 메시지는 현재 프로모션 코드를 지원하지 않습니다.

### 테스트 및 시드 발송도 사용량에 포함되나요?

기본적으로 테스트 발송과 시드 그룹 이메일 발송은 사용자당, 테스트 발송당 프로모션 코드를 사용합니다. 그러나 Braze 계정 매니저에게 연락하여 테스트 중에 프로모션 코드를 사용하지 않도록 이 동작을 업데이트할 수 있습니다.

### 여러 메시징 채널이 동일한 프로모션 코드 스니펫을 사용하면 어떻게 되나요?

특정 사용자가 여러 채널을 통해 코드를 받을 자격이 있는 경우, 각 채널을 통해 동일한 코드를 받게 됩니다. 수신한 채널 수에 관계없이 하나의 프로모션 코드만 사용됩니다.

### 하나의 메시지에서 동일한 프로모션 코드 목록을 참조하는 여러 Liquid 스니펫을 사용할 수 있나요?

네. Braze는 메시지 내 해당 스니펫의 모든 인스턴스에 동일한 프로모션 코드를 적용하여, 사용자가 하나의 고유 코드만 받도록 합니다.

### 프로모션 코드 목록이 만료되거나 비어 있으면 어떻게 되나요?

만료된 코드는 6개월 후에 삭제됩니다.

메시지에 비어 있거나 만료된 목록의 프로모션 코드가 포함되어야 했다면, 해당 메시지는 취소됩니다.

메시지에 프로모션 코드를 조건부로 삽입하는 Liquid 로직이 포함된 경우, 프로모션 코드가 포함되어야 하는 경우에만 메시지가 취소됩니다. 프로모션 코드가 포함되지 않아야 하는 경우에는 메시지가 정상적으로 발송됩니다.

### 잘못된 프로모션 코드를 업로드한 경우 업데이트할 수 있나요?

네. 전체 목록을 폐기하거나 플레이스홀더를 사용하여 목록을 삭제하면 해결할 수 있습니다. 자세한 내용은 [프로모션 코드 목록 업데이트]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create/#updating-a-promotion-code-list)를 참조하세요.

### 향후 메시지를 위해 프로모션 코드를 고객 프로필에 저장할 수 있나요?

네. 사용자 업데이트 단계를 통해 프로모션 코드를 고객 프로필에 저장할 수 있습니다. 자세한 내용은 [고객 프로필에 프로모션 코드 저장]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage/#save-to-profile)을 참조하세요.