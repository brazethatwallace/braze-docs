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
- 비즈니스 전화번호의 2단계 인증이 꺼져 있어야 합니다. WhatsApp Business 계정을 소유하고 있는 경우 WhatsApp Manager에서 해당 번호의 2단계 인증을 끌 수 있습니다. 그렇지 않은 경우 솔루션 제공업체에 요청하여 꺼야 합니다.

WhatsApp 전화번호 마이그레이션에 대한 자세한 내용은 Meta의 [Embedded Signup을 통한 WhatsApp Business 계정 간 전화번호 마이그레이션](https://developers.facebook.com/docs/whatsapp/business-management-api/guides/migrate-phone-to-different-waba/) 설명서를 참조하세요.

## WhatsApp 전화번호 마이그레이션하기 {#migrating-your-whatsapp-phone-number}

1. WhatsApp Manager에서 전화번호와 연결된 WhatsApp Business 계정(WABA)을 선택한 다음 **Account tools** > **Phone numbers**로 이동합니다.
2. **Turn off two-step verification**을 선택하고 이어지는 단계를 완료합니다.<br><br>![WhatsApp Business Manager의 "Phone numbers" 페이지가 열려 있는 화면.]({% image_buster /assets/img/whatsapp/waba_manager.png %}){: style="max-width:80%;"} <br><br> 다른 WhatsApp Business 그룹으로 전화번호를 마이그레이션하는 경우 Meta의 Embedded Signup에서 표시 이름이 일치해야 할 수 있으므로, **Phone Numbers** 페이지에서 기존 표시 이름을 메모해 두세요. 다음 단계에서 해당 이름을 입력하게 됩니다.<br><br>![WhatsApp Business Manager의 Phone Numbers 페이지에 전화번호 옆에 "Braze"라는 표시 이름이 나열되어 있는 화면.]({% image_buster /assets/img/whatsapp/phone_numbers.png %}){: style="max-width:80%;"}<br><br>
3. Meta의 Embedded Signup 워크플로를 끝까지 완료합니다.