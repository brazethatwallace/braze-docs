---
nav_title: "사용자 전화번호"
article_title: SMS 사용자 전화번호
page_order: 3
description: "이 참조 문서에서는 SMS 전화번호 형식, 전화번호 가져오기, SMS 구독 그룹에 사용자를 추가하는 방법을 다룹니다."
page_type: reference
alias: /user_phone_numbers/
channel:
  - SMS
  - MMS
  - RCS
---

# 사용자 전화번호 {#user-phone-numbers}

> 이 문서에서는 사용자 또는 고객의 전화번호와 관련된 다양한 주제를 다룹니다. 자체 번호에 대한 정보를 찾고 있다면 [발신 전화번호]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup/) 문서를 참조하세요.

## 권장 형식 {#recommended-format}

국가 코드나 지역 코드가 다른 여러 지역으로 발송하는 경우 정확성을 보장하기 위해 [`E.164`](https://en.wikipedia.org/wiki/e.164) 형식으로 전화번호를 가져오는 것을 권장합니다&#8212;미국 기반 전화번호도 마찬가지입니다.

- **미국 번호:** 모든 미국 번호는 유효한 지역 코드를 포함한 10자리 전화번호여야 합니다. 10자리 전화번호에 `+`와 국가 코드가 누락된 경우, Braze는 이를 미국 번호로 매핑합니다.
- **국제 번호:** 모든 국제 번호는 `+`로 시작하고, 그 뒤에 국가 코드와 전화번호가 이어져야 합니다. 예를 들어, `+442071838750`입니다.

![유효한 E.164 국제 전화번호 예시.]({% image_buster /assets/img/sms/e164.png %}){: style="max-width:50%;border: 0;"}

다음은 현지 형식과 `E.164` 형식의 차이를 보여주는 몇 가지 예시입니다:

| 국가 | 현지 형식 | 국가 코드 | `E.164` |
|---|---|---|---|
| 미국 | `4155552671` | 1 | `+14155552671` |
| 영국 | `2071838750` | 44 | `+442071838750` |
| 브라질 | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Recommended format" }

## 전화번호 가져오기 {#import-phone-numbers}

전화번호를 가져올 때는 [권장 형식](#recommended-format)을 따르는 것이 중요합니다. 전화번호를 가져오려면 다음 방법 중 하나를 사용하세요:

- [Braze에 CSV 업로드]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/#csv)
- [`/users/track` 엔드포인트 사용]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)

{% alert important %}
사용자 전화번호는 Braze에서 숫자 문자열로 표시됩니다. 선행 {% raw %}`+`{% endraw %} 이외에 숫자가 아닌 문자(예: `,`, `-`, `(`)가 포함된 번호를 가져오면, Braze에서 렌더링될 때 숫자가 아닌 문자가 제거됩니다. 예를 들어, `+1 (724) 123-4567`을 가져오면 `+17241234567`로 표시됩니다.
{% endalert %}

## 전화번호 유효성 검사 {#phone-number-validation}

Braze는 전화번호 유효성 검사를 위해 Google의 [libphonenumber](https://github.com/google/libphonenumber) 라이브러리를 사용합니다. 새로운 모바일 번호 접두사가 도입되면, 업스트림 라이브러리가 업데이트됨에 따라 지원이 추가됩니다. Braze는 유효한 접두사의 별도 목록을 관리하지 않습니다.

### 유효하지 않은 전화번호 처리 {#handling-invalid-phone-numbers}

전화번호가 유효하지 않은 것으로 판단되면, Braze는 해당 사용자의 전화번호를 유효하지 않음으로 표시하고 해당 전화번호로 추가 커뮤니케이션을 발송하지 않습니다. 유효하지 않은 전화번호는 고객 프로필의 **Engagement Tab**에 표시됩니다.

![Braze에서 유효하지 않은 전화번호에 대한 오류 메시지 예시.]({% image_buster /assets/img/sms/invalid_banner.png %}){: style="max-width:50%;border: 0;"}

전화번호가 유효하지 않은 것으로 간주되는 이유는 다음과 같습니다:

- **공급자 오류**: SMS 및 RCS 공급자로부터 영구적인 오류가 수신되었습니다. 이는 제공된 전화번호의 형식이 잘못되었거나 SMS 또는 RCS 메시지를 영구적으로 수신할 수 없음을 나타냅니다.
- **비활성화**: 모바일 가입자가 서비스를 해지하고 통신사에서 번호를 해제하여 전화번호가 비활성화되었습니다(결국 재활용되어 새 사용자에게 할당될 수 있습니다). 해당 전화번호로 SMS 또는 RCS 메시지를 발송하지 않았더라도 비활성화된 전화번호는 유효하지 않음으로 표시될 수 있습니다.

이러한 유효하지 않은 전화번호는 [SMS 및 RCS 엔드포인트]({{site.baseurl}}/api/endpoints/sms/)를 사용하여 관리할 수 있습니다.

{% alert note %}
여러 고객 프로필이 동일한 전화번호를 가지고 있고 해당 전화번호가 유효하지 않음으로 표시되면, 해당 번호를 가진 모든 기존 고객 프로필이 유효하지 않음으로 표시됩니다. 새로 생성된 고객 프로필은 처음에 유효하지 않음으로 표시되지 않습니다.
{% endalert %}

[Segment 생성]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/#step-4-add-filters-to-your-segment) 시 유효하지 않은 전화번호를 가진 사용자를 포함하거나 제외할 수도 있습니다.

## 거부된 SMS 발송을 세분화에서 제외 {#exclude-rejected-sms-sends-from-segmentation}

{% alert important %}
SMS 거부는 SMS 할당량에 포함되어 청구됩니다.
{% endalert %}

거부된 SMS 발송이 있는 사용자를 Segment에서 제외하려면 [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/)을 사용하여 다음을 수행하세요:

1. **오디언스** > **세그먼트 확장**으로 이동합니다.
2. **Create New Extension** > **Full refresh** 또는 **Incremental refresh**를 선택합니다.
3. SMS 거부가 있는 사용자를 식별하는 SQL 쿼리를 작성합니다. 예를 들어, `USERS_MESSAGES_SMS_REJECTION_SHARED` 이벤트를 쿼리하여 SMS 거부를 수신한 사용자를 찾을 수 있습니다.
4. 세그먼트 확장을 저장합니다.
5. SMS Segment를 생성할 때, 이 세그먼트 확장에 포함된 사용자를 제외하는 필터를 추가합니다.

## SMS 및 RCS 구독 그룹에 사용자 추가 {#add-users-to-sms-and-rcs-subscription-groups}

사용자가 SMS 또는 RCS 메시지를 수신하려면 유효한 전화번호가 있어야 하며 구독 그룹에 옵트인해야 합니다. 구독 그룹은 운영 중인 SMS 또는 RCS 프로그램에 연결됩니다([SMS, MMS 및 RCS에 대한 법적 요구 사항]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations/)을 준수하고 각 고객에 대한 동의를 기록했는지 확인하세요). 자세한 내용은 [SMS 및 RCS 구독 그룹]({{site.baseurl}}/sms_rcs_subscription_groups/)을 참조하세요.

## 서드파티 소싱 및 검증 {#third-party-sourcing-and-verification}

Braze는 유효하지 않은 번호를 소싱하기 위해 서드파티 도구에 의존합니다. Braze는 이러한 서비스의 중단이나 잘못된 정보에 대해 책임지지 않습니다. 따라서 이 도구를 유효하지 않은 번호를 검증하기 위한 유일한 규정 준수 방법으로 사용해서는 안 됩니다.

## 전화번호 수집 {#phone-number-capture}

인앱 메시지를 통해 전화번호를 수집하려면 [전화번호 수집]({{site.baseurl}}/phone_number_capture/)을 참조하세요.