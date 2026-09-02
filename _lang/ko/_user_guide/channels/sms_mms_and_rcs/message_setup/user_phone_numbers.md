---
nav_title: "사용자 전화번호"
article_title: 단문 메시지 서비스 사용자 전화번호
page_order: 3
description: "이 참조 문서에서는 단문 메시지 서비스 전화번호 형식, 전화번호 가져오기, 단문 메시지 서비스 구독 그룹에 사용자를 추가하는 방법을 다룹니다."
page_type: reference
alias: /user_phone_numbers/
channel:
  - SMS
  - MMS
  - RCS
---

# 사용자 전화번호 {#user-phone-numbers}

> 이 문서에서는 사용자 또는 고객의 전화번호와 관련된 다양한 주제를 다룹니다. 자체 번호에 대한 정보를 찾고 있다면 [발신 전화번호]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup) 문서를 참조하세요.

## 권장 형식 {#recommended-format}

국가 코드나 지역 코드가 다른 여러 지역으로 발송하는 경우 정확성을 보장하기 위해, 미국 기반 전화번호에도 [`E.164`](https://en.wikipedia.org/wiki/e.164) 형식으로 전화번호를 가져오는 것을 권장합니다.

- **미국 번호:** 모든 미국 번호는 유효한 지역 코드를 포함한 유효한 10자리 전화번호여야 합니다. 10자리 전화번호에 `+`와 국가 코드가 누락된 경우 Braze는 이를 미국 번호로 매핑합니다. 푸에르토리코 전화번호는 미국 스타일의 지역 코드를 사용한 10자리 형식이지만 여전히 `+`와 국가 코드가 필요합니다.
- **국제 번호:** 모든 국제 번호는 `+`로 시작하고, 그 뒤에 국가 코드와 전화번호가 와야 합니다. 예: `+442071838750`.

![유효한 E.164 국제 전화번호 예시.]({% image_buster /assets/img/sms/e164.png %}){: style="max-width:50%;border: 0;"}

다음은 현지 형식과 `E.164` 형식의 차이를 보여주는 몇 가지 예시입니다:

| 국가 | 현지 형식 | 국가 코드 | `E.164` |
|---|---|---|---|
| 미국 | `4155552671` | 1 | `+14155552671` |
| 영국 | `2071838750` | 44 | `+442071838750` |
| 브라질 | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="권장 형식" }

## 전화번호 가져오기 {#import-phone-numbers}

전화번호를 가져올 때는 [권장 형식](#recommended-format)을 따르는 것이 중요합니다. 전화번호를 가져오려면 다음 방법 중 하나를 사용하세요:

- [Braze에 CSV 업로드]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)
- [`/users/track` 엔드포인트 사용]({{site.baseurl}}/api/endpoints/user_data/post_user_track)

{% alert important %}
사용자 전화번호는 Braze에서 숫자 문자열로 표시됩니다. 선행 {% raw %}`+`{% endraw %} 이외에 숫자가 아닌 문자(예: `,`, `-`, `(`)가 포함된 번호를 가져오면, Braze에서 렌더링할 때 해당 문자가 제거됩니다. 예를 들어 `+1 (724) 123-4567`을 가져오면 `+17241234567`로 표시됩니다.
{% endalert %}

## 전화번호 유효성 검사 {#phone-number-validation}

Braze는 Google의 [libphonenumber](https://github.com/google/libphonenumber) 라이브러리를 사용하여 전화번호의 유효성을 검사합니다. 새로운 휴대폰 번호 접두사가 도입되면, 업스트림 라이브러리가 업데이트될 때 해당 지원이 추가됩니다. Braze는 유효한 접두사의 별도 목록을 관리하지 않습니다.

### 유효하지 않은 전화번호 처리 {#handling-invalid-phone-numbers}

전화번호가 유효하지 않은 것으로 판단되면, Braze는 해당 사용자의 전화번호를 유효하지 않음으로 표시하고 해당 전화번호로 더 이상 커뮤니케이션을 보내지 않습니다. 유효하지 않은 전화번호는 고객 프로필의 **인게이지먼트 탭**에 표시됩니다.

![Braze에서 유효하지 않은 전화번호에 대한 오류 메시지 예시.]({% image_buster /assets/img/sms/invalid_banner.png %}){: style="max-width:50%;border: 0;"}

전화번호가 유효하지 않은 것으로 간주되는 이유는 다음과 같습니다:

- **공급자 오류**: 단문 메시지 서비스 및 RCS 공급자로부터 영구적인 오류가 수신되었습니다. 이는 제공된 전화번호의 형식이 잘못되었거나 단문 메시지 서비스 또는 RCS 메시지를 영구적으로 수신할 수 없음을 나타냅니다.
- **비활성화**: 모바일 가입자가 서비스를 해지하고 이동통신사에서 번호를 해제하여 전화번호가 비활성화되었습니다(이후 재활용되어 새 사용자에게 할당될 수 있습니다). 비활성화된 전화번호는 해당 번호로 단문 메시지 서비스 또는 RCS 메시지를 보내지 않은 경우에도 유효하지 않음으로 표시될 수 있습니다.

이러한 유효하지 않은 전화번호는 [단문 메시지 서비스 및 RCS 엔드포인트]({{site.baseurl}}/api/endpoints/sms)를 사용하여 관리할 수 있습니다.

{% alert note %}
여러 고객 프로필이 동일한 전화번호를 가지고 있고 해당 전화번호가 유효하지 않음으로 표시된 경우, 해당 번호를 가진 모든 기존 고객 프로필이 유효하지 않음으로 표시됩니다. 새로 생성된 고객 프로필은 처음에 유효하지 않음으로 표시되지 않습니다.
{% endalert %}

[Segment 생성]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#step-4-add-filters-to-your-segment) 시 유효하지 않은 전화번호를 가진 사용자를 포함하거나 제외할 수도 있습니다.

## 세분화에서 거부된 단문 메시지 서비스 발송 제외하기 {#exclude-rejected-sms-sends-from-segmentation}

{% alert important %}
단문 메시지 서비스 거부는 Braze 계약 및 단문 메시지 서비스 공급자에 따라 단문 메시지 서비스 할당량에 포함될 수 있습니다. 과금 성과에 대해서는 [리포팅]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting)을 참조하세요.
{% endalert %}

거부된 단문 메시지 서비스 발송이 있는 사용자를 Segment에서 제외하려면 [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)을 사용하여 다음을 수행합니다:

1. **오디언스** > **세그먼트 확장**으로 이동합니다.
2. **새 확장 생성** > **전체 새로고침** 또는 **증분 새로고침**을 선택합니다.
3. 단문 메시지 서비스 거부가 있는 사용자를 식별하는 SQL 쿼리를 작성합니다. 예를 들어, `USERS_MESSAGES_SMS_REJECTION_SHARED` 이벤트를 쿼리하여 단문 메시지 서비스 거부를 수신한 사용자를 찾을 수 있습니다.
4. 세그먼트 확장을 저장합니다.
5. 단문 메시지 서비스 Segment를 생성할 때, 이 세그먼트 확장에 포함된 사용자를 제외하는 필터를 추가합니다.

## 단문 메시지 서비스 및 RCS 구독 그룹에 사용자 추가 {#add-users-to-sms-and-rcs-subscription-groups}

사용자가 단문 메시지 서비스 또는 RCS 메시지를 수신하려면 유효한 전화번호가 있어야 하며 구독 그룹에 옵트인되어 있어야 합니다. 구독 그룹은 운영 중인 단문 메시지 서비스 또는 RCS 프로그램에 연결됩니다(반드시 [단문 메시지 서비스, MMS 및 RCS에 대한 법적 요구사항]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)을 준수하고 각 고객에 대한 동의를 기록해야 합니다). 자세한 내용은 [단문 메시지 서비스 및 RCS 구독 그룹]({{site.baseurl}}/sms_rcs_subscription_groups)을 참조하세요.

## 서드파티 소싱 및 검증 {#third-party-sourcing-and-verification}

Braze는 서드파티 도구를 활용하여 유효하지 않은 번호를 확인합니다. Braze는 이러한 서비스의 중단이나 잘못된 정보에 대해 책임을 지지 않습니다. 따라서 이 도구를 유효하지 않은 번호를 검증하기 위한 유일한 컴플라이언스 수단으로 사용해서는 안 됩니다.

## 전화번호 수집 {#phone-number-capture}

인앱 메시지를 통해 전화번호를 수집하려면 [단문 메시지 서비스, RCS 및 WhatsApp 가입 양식]({{site.baseurl}}/phone_number_capture)을 참조하세요.