---
nav_title: Meta Direct Billing
article_title: Meta Direct Billing
page_order: 7
description: "이 참조 문서에서는 Braze 또는 파트너 크레딧 라인 대신 자체 직불카드 또는 신용카드로 WhatsApp 메시징 비용을 지불할 수 있도록 Meta Direct Billing을 설정하는 방법을 다룹니다."
page_type: reference
channel:
  - WhatsApp
alias: /whatsapp_meta_direct_billing/
hidden: true
noindex: true
---

# Meta Direct Billing {#meta-direct-billing}

> Meta Direct Billing을 사용하면 Braze 또는 파트너 크레딧 라인을 통하지 않고 자체 직불카드 또는 신용카드로 WhatsApp 메시징 비용을 직접 지불할 수 있습니다.

## 전제 조건 {#prerequisites}

Meta Direct Billing을 설정하기 전에 다음 사항을 확인하세요.

| 요구 사항 | 설명 |
| --- | --- |
| Braze 워크스페이스 접근 권한 | 임베디드 가입 플로우를 시작하려면 Braze에서 **파트너 통합** > **기술 파트너**에 접근할 수 있어야 합니다. |
| Meta Business 매니저 계정 | 결제는 Meta Business 매니저의 **결제 및 결제 수단**에서 구성합니다. |
| 직불카드 또는 신용카드 | 설정을 완료하려면 유효한 카드가 필요합니다. 일부 계정에서는 월별 청구서 발행이 옵션으로 표시될 수 있지만, 보장되지는 않습니다. |
| 완전한 비즈니스 정보 | 비즈니스 이름, 주소, 통화가 정확하게 입력되어 있어야 합니다. Meta는 메시징을 활성화하기 전에 이 정보를 검토합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="전제 조건" }

## 설정 {#setup}

### 1단계: Meta Direct Billing 선택 {#step-1-select-meta-direct-billing}

1. Braze에서 **파트너 통합** > **기술 파트너**로 이동한 후 **WhatsApp**을 검색하고 **WhatsApp Messaging Integration** 페이지를 엽니다.
2. **Meta Direct Billing** 탭을 선택합니다. 이는 결제 관계가 Braze 또는 Infobip 결제 라인을 통하지 않고 Meta와 직접 이루어진다는 의미이므로, 나중에 변경하려고 하기보다 계속 진행하기 전에 반드시 이 탭을 선택하는 것이 중요합니다.
3. **WhatsApp Business Account 또는 전화번호 추가** 아래에서 **계정 또는 번호 추가**를 선택합니다. 이렇게 하면 Meta의 임베디드 가입이 시작되어 Meta에 로그인하고, 비즈니스 포트폴리오를 선택하고, WhatsApp Business Account(WABA)를 생성 또는 선택하고, 전화번호를 인증할 수 있습니다.

### 2단계: 결제 및 결제 수단으로 이동 {#step-2-go-to-billing-payments}

Meta의 임베디드 가입을 완료한 후 다음 중 하나를 수행합니다.

- **결제 수단 추가**를 선택하면 Meta Business 매니저로 이동합니다.
- Meta Business 매니저에서 **결제 및 결제 수단** > **계정**으로 이동한 후 WABA를 선택합니다.

### 3단계: 결제 수단 추가 {#step-3-add-a-payment-method}

1. **결제 수단 추가**를 선택합니다.
2. 열리는 창에서 **비즈니스 위치 및 통화**(예: **Canada, US Dollars USD**)를 확인합니다. 이것이 청구 통화를 결정합니다. 변경이 필요한 경우 **편집**을 선택합니다.
3. **결제 수단 선택** 아래에 기존 크레딧 라인이 표시될 수 있습니다. 이 크레딧 라인은 사용할 수 없으므로 선택하지 마세요. 자세한 내용은 [결제 라인 제한 사항](#billing-line-restrictions)을 참조하세요.

![직불카드 또는 신용카드가 선택되어 있고 기존 Infobip 및 Braze 크레딧 라인은 선택되지 않은 결제 수단 선택 창.]({% image_buster /assets/img/whatsapp/payment_methods.png %}){: style="max-width:40%;"}

{: start="4"}
4. **결제 수단 추가** 아래에서 **직불카드 또는 신용카드**를 선택한 다음 **다음**을 선택합니다.
5. 카드 정보를 입력한 다음 **저장**을 선택합니다.
6. 카드가 **결제 수단** 아래에 **기본값**으로 표시되며, 마스킹된 카드 번호와 만료일이 나타납니다.

{% alert note %}
결제 수단을 추가한 후 설정 창을 닫아도 전화번호 연결이 해제되지 않습니다. 연결된 번호는 유지됩니다.
{% endalert %}

### 4단계: 비즈니스 정보 확인 {#step-4-confirm-your-business-information}

Meta는 메시징을 활성화하기 전에 비즈니스 이름, 주소, 통화를 검토합니다. 불완전하거나 부정확한 비즈니스 정보는 메시지 전송 실패 또는 잘못된 비즈니스 정보 오류를 초래할 수 있습니다.

## 결제 라인 제한 사항 {#billing-line-restrictions}

결제 수단 목록에 표시되는 크레딧 라인(예: "Infobip Limited" 또는 "BRAZE INC.")은 해당 특정 비즈니스가 소유한 것이며 사용자의 것이 아닙니다. 계정이 연결된 방식 때문에 표시되지만 선택할 수 없습니다.

## Meta 리소스 {#meta-resources}

- [Meta Business 도움말 센터: 결제 및 결제 수단](https://business.facebook.com/business/help/535561817791563)
- [Meta Business 도움말 센터: 결제 수단 추가](https://www.facebook.com/business/help/832746984379005)