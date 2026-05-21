---
nav_title: "사용자 전화번호"
article_title: WhatsApp 사용자 전화번호
page_order: 3
description: "이 참조 문서에서는 WhatsApp 전화번호 형식, 전화번호 가져오기 방법, WhatsApp 구독 그룹에 사용자를 추가하는 방법을 다룹니다."
page_type: reference
channel:
  - WhatsApp

---

# 사용자 전화번호 {#user-phone-numbers}

> 이 문서에서는 사용자 또는 고객의 전화번호와 관련된 다양한 주제를 다룹니다.

전화번호는 고객 프로필에 현지 형식으로 표시되지만, 번호를 가져올 때 사용하는 형식(`(724) 123 4567`)과는 다릅니다.

## 전화번호 가져오기 {#importing-phone-numbers}

[CSV 업로드]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/#csv) 또는 [API를 통해]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) 전화번호를 가져와서 사용자를 생성할 수 있습니다.

### 형식 {#formatting}

미국 이외의 번호는 "+"와 국가 코드를 포함한 [`E.164`](https://en.wikipedia.org/wiki/e.164) 형식으로 가져오는 것이 중요합니다. 이 형식으로 제공되지 않은 전화번호는 미국 번호로 해석됩니다.

전화번호가 E.164 형식으로 변환되었지만 유효성 검사를 통과하지 못하면, Braze는 해당 번호로 WhatsApp 메시지를 보낼 수 없습니다. 형식을 지정할 수 없는 전화번호를 가진 사용자는 WhatsApp을 포함하는 캔버스 단계에서 자동으로 이탈합니다.

모든 미국 번호는 유효한 지역 코드를 포함한 유효한 10자리 전화번호여야 합니다. `+`와 국가 코드 없이 입력할 수 있으며, Braze는 유효한 10자리 전화번호를 모두 미국 번호로 가정하고 매핑합니다.

모든 국제 번호는 `+`로 시작하고, 그 뒤에 국가 코드와 전화번호가 와야 합니다. (예: `+442071838750`)

![]({% image_buster /assets/img/sms/e164.png %}){: style="max-width:50%;border: 0;"}

그러나 국가 코드나 지역 코드가 다른 여러 지역으로 발송하는 경우 정확성을 보장하기 위해, 미국 기반 전화번호에도 `E.164` 형식을 사용하는 것이 권장됩니다.

다음 표에서 현지 번호 형식과 범용 `E.164` 형식의 차이를 확인할 수 있습니다:

| 국가 | 현지 형식 | 국가 코드 | `E.164` |
|---|---|---|---|
| 미국 | `4155552671` | 1 | `+14155552671` |
| 영국 | `02071838750` | 44 | `+442071838750` |
| 브라질 | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Formatting" }

### WhatsApp 구독 그룹에 사용자 추가 {#adding-users-to-whatsapp-a-subscription-group}

고객이 WhatsApp 메시지를 수신하려면 유효한 전화번호가 있어야 하며 구독 그룹에 옵트인되어 있어야 합니다. 자세한 내용은 [WhatsApp 구독 그룹]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups/)을 참조하세요.


### 동일한 전화번호를 가진 다중 사용자 {#multiple-users-with-the-same-phone-number}

단일 Campaign 또는 캔버스 단계의 Segment 내에서 여러 사용자가 동일한 전화번호를 가지고 있는 경우, Braze는 발송을 중복 제거하여 해당 전화번호로 하나의 메시지만 발송합니다.