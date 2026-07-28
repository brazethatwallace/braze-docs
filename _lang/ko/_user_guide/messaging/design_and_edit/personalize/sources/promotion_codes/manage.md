---
nav_title: 코드 사용
article_title: 프로모션 코드 사용
page_order: 0.2
description: "Campaigns과 Canvases에서 프로모션 코드를 사용하고 사용량을 확인하는 방법을 알아보세요."
---

# 프로모션 코드 사용 {#use-promotion-codes}

> Campaigns과 Canvases에서 프로모션 코드를 사용하고 사용량을 확인하는 방법을 알아보세요.

## 필수 조건 {#prerequisites}

프로모션 코드를 사용하려면 먼저 [프로모션 코드 목록을 생성]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create)해야 합니다.

## 프로모션 코드 사용하기 {#using-promotion-codes}

메시지에 프로모션 코드를 보내려면 [이전에 생성한]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create#create) 프로모션 코드 목록 옆에 있는 **스니펫 복사**를 선택합니다.

![메시지에 붙여넣을 스니펫을 복사하는 옵션.]({% image_buster /assets/img/promocodes/promocode9.png %}){: style="max-width:70%"}

코드 스니펫을 Braze의 메시지 중 하나에 붙여넣은 다음, [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)를 사용하여 목록에서 고유한 프로모션 코드 중 하나를 삽입합니다. 해당 코드는 발송 완료로 표시되어 다른 메시지에서 동일한 코드를 보내지 않습니다.

![독점 혜택과 함께 코드 스니펫이 포함된 예시 메시지 "이번 봄, 독점 혜택으로 자신에게 선물하세요".]({% image_buster /assets/img/promocodes/promocode10.png %}){: style="max-width:70%"}

### 캔버스 단계 간 사용 {#across-canvas-steps}

코드 스니펫이 멀티채널 메시지가 포함된 Campaign이나 Canvas에서 사용되면, 각 사용자는 고유한 코드를 받습니다. 프로모션 코드를 참조하는 여러 단계가 있는 Canvas에서는 사용자가 진입하는 각 단계마다 새로운 코드를 받습니다.

Canvas에서 하나의 프로모션 코드를 할당하고 여러 단계에서 재사용하려면:

1. 첫 번째 단계(사용자 업데이트)에서 프로모션 코드를 커스텀 속성으로 할당합니다.
2. 이후 단계에서 새 코드를 생성하는 대신 Liquid를 사용하여 해당 커스텀 속성을 참조합니다.

사용자가 여러 채널에서 코드를 받을 자격이 있는 경우, 각 채널에서 동일한 코드를 받습니다. 예를 들어, 이메일과 푸시로 메시지를 받는 경우 동일한 코드가 두 채널 모두에 전송됩니다. 보고서에도 단일 코드로 반영됩니다.

{% alert note %}
사용 가능한 프로모션 코드가 없으면, 코드에 의존하는 테스트 또는 라이브 메시지는 발송되지 않습니다.
{% endalert %}

### 인앱 메시지 Campaign {#promotion-codes-iam-campaigns}

[인앱 메시지 Campaign]({{site.baseurl}}/user_guide/channels/in_app_messages)을 생성한 후, 인앱 메시지 본문에 [프로모션 코드 목록 스니펫]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#using-promotion-codes)을 삽입할 수 있습니다. 인앱 메시지의 프로모션 코드는 사용자가 인앱 메시지 표시를 트리거할 때만 차감되어 사용됩니다.

### 테스트 메시지 {#test-messages}

테스트 발송 및 시드 그룹 이메일 발송은 별도 요청이 없는 한 프로모션 코드를 소진합니다. 테스트 발송 및 시드 그룹 이메일 발송 시 프로모션 코드가 사용되지 않도록 이 기능 동작을 업데이트하려면 Braze 계정 매니저에게 문의하세요.

### Currents용 메시지 추가 정보와 함께 사용 {#with-message-extras-for-currents}

{% multi_lang_include partners/shopify.md section='Liquid promotion codes with Currents' %}

## 고객 프로필에 프로모션 코드 저장 {#save-to-profile}

후속 메시지에서 동일한 프로모션 코드를 참조하려면, 해당 코드를 고객 프로필에 커스텀 속성으로 저장해야 합니다. 이는 메시지 단계 바로 앞에 있는 [사용자 업데이트 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)를 통해 할인 코드를 "Promo Code"와 같은 커스텀 속성에 할당하여 수행할 수 있습니다.

먼저, 사용자 업데이트 단계의 각 필드에 다음을 선택합니다:

- **속성 이름:** Promo Code
- **동작:** 업데이트
- **키 값:** 프로모션 코드의 Liquid 코드 스니펫(예: {% raw %}`{% promotion('spring25') %}`{% endraw %})

다음으로, 메시지에 커스텀 속성(이 예시에서는 {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %})을 추가합니다. 할인 코드가 템플릿으로 삽입됩니다.

## 프로모션 코드 사용량 확인 {#viewing-promotion-code-usage}

**프로모션 코드** 페이지의 프로모션 코드 목록에서 **잔여** 열을 통해 남은 코드 수를 확인할 수 있습니다.

![미사용 코드가 있는 프로모션 코드 예시.]({% image_buster /assets/img/promocodes/promocode11.png %})

이 코드 수는 기존 프로모션 코드 목록 페이지를 다시 방문할 때도 확인할 수 있습니다. 미사용 코드를 CSV 파일로 내보낼 수도 있습니다.

![992개의 잔여 코드가 있는 "Black Friday Sale"이라는 프로모션 코드.]({% image_buster /assets/img/promocodes/promocode12.png %}){: style="max-width:70%"}

## 멀티채널 및 단일 채널 발송 {#multichannel-and-single-channel-sends}

멀티채널 및 단일 발송 Campaigns과 Canvases의 경우, 메시지의 Liquid에서 참조된 모든 프로모션 코드는 메시지가 발송되기 **전에** 차감되어 다음 사항이 보장됩니다:

- 멀티채널 메시지에서 채널 간에 동일한 프로모션 코드가 사용됩니다.
- 메시지가 실패하거나 중단되는 경우 추가 프로모션 코드가 사용되지 않습니다.

사용자가 하나의 메시지에서 Liquid 조건 로직 태그로 분기되는 두 개의 프로모션 코드 목록을 참조하는 경우, 사용자가 어떤 조건 흐름을 따르든 모든 프로모션 코드가 차감됩니다.

사용자가 새 캔버스 단계에 진입하거나 Canvas에 재진입하여 해당 사용자에게 보내는 메시지에 프로모션 코드 Liquid 스니펫이 다시 적용되면, 새로운 프로모션 코드가 사용됩니다.

### 예시 {#example}

다음 예시에서는 프로모션 코드 목록 `vip-deal`과 `regular-deal`이 모두 차감됩니다. Liquid는 다음과 같습니다:

{% raw %}
```
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %}
```
{% endraw %}

Braze는 예상 사용량보다 더 많은 프로모션 코드를 업로드할 것을 권장합니다. 프로모션 코드 목록이 만료되거나 프로모션 코드가 소진되면, 이후 메시지는 중단됩니다.

{% alert tip %}
**Braze에서 프로모션 코드가 소진되는 방식에 대한 비유입니다.** <br><br>메시지를 보내는 것이 우체국에서 편지를 보내는 것과 같다고 상상해 보세요. 편지를 직원에게 건네면, 직원은 편지에 쿠폰이 포함되어야 한다는 것을 확인합니다. 직원은 쿠폰 더미에서 첫 번째 쿠폰을 꺼내 봉투에 넣습니다. 직원이 편지를 보내지만, 어떤 이유로 편지가 배달 중 분실됩니다(쿠폰도 함께 분실됩니다). <br><br>이 시나리오에서 Braze는 우체국 직원이고, 프로모션 코드는 쿠폰입니다. 프로모션 코드 더미에서 꺼낸 후에는 웹훅 결과와 관계없이 되돌릴 수 없습니다.
{% endalert %}