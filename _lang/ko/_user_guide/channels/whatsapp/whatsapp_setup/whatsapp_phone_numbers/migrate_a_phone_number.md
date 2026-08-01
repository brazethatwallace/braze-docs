---
nav_title: "번호 마이그레이션"
article_title: "WhatsApp 전화번호 마이그레이션"
page_order: 2
description: "이 참조 문서에서는 WhatsApp 전화번호를 마이그레이션하는 방법을 다룹니다."
page_type: reference
channel:
  - WhatsApp
---

# WhatsApp 전화번호 마이그레이션 {#migrate-a-whatsapp-phone-number}

> Meta의 Embedded Signup을 사용하여 WhatsApp Business 계정 간에 WhatsApp 전화번호를 마이그레이션할 수 있습니다.

## 필수 조건 {#prerequisites}

전화번호가 마이그레이션 대상이 되려면 Meta의 요구 사항을 충족해야 합니다.

- Meta Business 계정이 인증되어 있어야 합니다.
- 기존 WhatsApp Business 계정이 승인되어 있어야 합니다.
- 기존 WhatsApp Business 계정의 **Payment Settings**에 유효한 결제 수단이 등록되어 있어야 합니다.
- 비즈니스 전화번호의 2단계 인증이 꺼져 있어야 합니다. WhatsApp Business 계정을 소유하고 있는 경우 WhatsApp 매니저에서 해당 번호의 2단계 인증을 끌 수 있습니다. 그렇지 않은 경우 솔루션 제공업체에 요청하여 꺼야 합니다.

WhatsApp 전화번호 마이그레이션에 대한 자세한 내용은 Meta의 [Embedded Signup을 통한 WhatsApp Business 계정 간 전화번호 마이그레이션](https://developers.facebook.com/docs/whatsapp/business-management-api/guides/migrate-phone-to-different-waba/) 설명서를 참조하세요.

## WhatsApp Business 계정 간 마이그레이션 {#migrate-between-whatsapp-business-accounts}

1. WhatsApp 매니저에서 전화번호와 연결된 WhatsApp Business 계정(WABA)을 선택한 다음 **Account tools** > **Phone numbers**로 이동합니다.
2. **Turn off two-step verification**을 선택하고 이어지는 단계를 완료합니다.<br><br>![WhatsApp Business 매니저의 "Phone numbers" 페이지가 열려 있는 화면.]({% image_buster /assets/img/whatsapp/waba_manager.png %}){: style="max-width:80%;"} <br><br> 다른 WhatsApp Business 그룹으로 전화번호를 마이그레이션하는 경우 Meta의 Embedded Signup에서 표시 이름이 일치해야 할 수 있으므로, **Phone Numbers** 페이지에서 기존 표시 이름을 메모해 두세요. 다음 단계에서 해당 이름을 입력하게 됩니다.<br><br>![WhatsApp Business 매니저의 Phone Numbers 페이지에 전화번호 옆에 "Braze"라는 표시 이름이 나열되어 있는 화면.]({% image_buster /assets/img/whatsapp/phone_numbers.png %}){: style="max-width:80%;"}<br><br>
3. Meta의 Embedded Signup 워크플로를 끝까지 완료합니다.

## 다른 비즈니스 솔루션 제공업체(BSP)에서 마이그레이션 {#migrate-from-another-business-solution-provider}

WhatsApp 전화번호가 다른 BSP에 등록되어 있는 경우, Braze에서 해당 번호로 메시지를 보내려면 먼저 Braze에 연결된 WhatsApp Business 계정으로 번호를 마이그레이션해야 합니다.

### 마이그레이션 전 확인 사항 {#before-you-migrate}

- 전화번호는 한 번에 하나의 BSP에서만 활성화할 수 있습니다. 마이그레이션하면 발송이 Braze로 이전되며, 기존 BSP는 해당 번호에 대한 접근 권한을 잃게 됩니다.
- 현재 제공업체와의 계약 및 청구 사항을 검토하세요. 메시지 기록과 템플릿은 자동으로 이전되지 않을 수 있습니다.
- Meta의 요구 사항에 따라 해당 번호의 2단계 인증을 꺼야 합니다.
- 지원용과 마케팅용 번호를 별도로 사용해야 하는 경우, WhatsApp FAQ의 [통합, 데이터 및 리포팅]({{site.baseurl}}/user_guide/channels/whatsapp/faq#integrations-data-and-reporting)을 참조하세요.

### 마이그레이션 경로 {#migration-paths}

| 현재 설정 | 권장 경로 |
|---|---|
| 다른 BSP에 등록된 번호를 Braze로 완전히 이전 | [Embedded Signup]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup)을 통해 신규 또는 기존 Braze WABA로 마이그레이션 |
| Braze 네이티브 통합에 등록된 번호를 Infobip 청구로 이전 | [BYO WhatsApp 커넥터]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/byo_connector) (Infobip 전용) |
| 마케팅은 Braze, 지원은 다른 WABA 사용 | 별도의 WABA와 전화번호를 유지합니다. [WhatsApp FAQ]({{site.baseurl}}/user_guide/channels/whatsapp/faq#integrations-data-and-reporting) 및 [WhatsApp과 외부 시스템]({{site.baseurl}}/user_guide/channels/whatsapp/use_cases/whatsapp_and_external_systems)을 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="마이그레이션 경로" }

## 개발 및 프로덕션 워크스페이스 {#development-and-production-workspaces}

Braze는 가능한 경우 개발용과 프로덕션용으로 별도의 WhatsApp Business 계정을 사용할 것을 권장합니다.

- 프로덕션 전화번호를 샌드박스 또는 개발 워크스페이스에 바인딩하지 마세요.
- 통합 테스트에는 전용 테스트 WABA와 전화번호를 사용하세요.
- 템플릿 승인은 WABA 단위로 적용됩니다. 발송하는 워크스페이스에 연결된 WABA에서 템플릿을 승인하세요.