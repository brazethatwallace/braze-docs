---
nav_title: 임베디드 가입
article_title: WhatsApp 임베디드 가입
page_order: 1
description: "이 참조 문서에서는 Braze에서 WhatsApp 임베디드 가입 워크플로에 액세스하는 방법, Meta 가입 전에 준비해야 할 사항, 가입 완료 후 어떤 일이 일어나는지 설명합니다."
page_type: reference
channel:
  - WhatsApp
---

# WhatsApp 임베디드 가입 {#whatsapp-embedded-signup}

> 임베디드 가입을 사용하여 Meta의 호스팅된 가입 플로를 통해 Braze를 WhatsApp Business 계정(WABA)에 연결할 수 있습니다.

WhatsApp 임베디드 가입 워크플로는 Braze 워크스페이스에 처음 [WhatsApp을 통합]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)할 때, 그리고 기존 통합에 [WhatsApp Business 계정 또는 전화번호를 추가]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)할 때 열립니다.

{% alert note %}
Braze 워크스페이스에 [여러 WhatsApp Business 계정]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/multiple_business_accounts)을 추가할 수 있습니다. 그러나 각 특정 WhatsApp Business 계정은 하나의 Braze 워크스페이스에만 추가할 수 있습니다.
{% endalert %}

## 워크플로 액세스 {#accessing-the-workflow}

1. **파트너 통합** > **기술 파트너**로 이동합니다.
2. **WhatsApp**을 검색하고 선택합니다.
3. 사용 사례에 맞는 옵션을 선택합니다:
   - **첫 통합:** **Begin Integration**을 선택합니다.
   - **추가 계정 또는 번호:** **WhatsApp Messaging Integration** 페이지에서 **Add account or number** 또는 **Add WhatsApp Business Account**를 선택합니다.

Meta 임베디드 가입 플로는 어느 진입점에서 시작하든 동일합니다. 구성에 따라 워크스페이스에 **Native Integration** 또는 **BYO Connector - Infobip** 같은 통합 탭이 표시될 수도 있습니다. 시작하기 전에 설정에 맞는 탭을 선택하세요.

## 가입 준비 {#prepare-for-signup}

**통합 시작**을 선택하면 Braze에서 온보딩 창이 열립니다. 각 슬라이드를 검토한 후, **통합 시작**을 다시 선택하여 Meta 임베디드 가입을 시작합니다.

시작하기 전에 다음을 준비하세요:

- **Meta Business Manager 액세스:** 대부분의 회사는 Meta Business Manager를 사용하여 Facebook 페이지, 광고 및 관련 비즈니스 자산을 관리합니다. 액세스 권한이 없는 경우 관리자에게 권한을 부여해 달라고 요청하거나, 가입 중에 Business Manager 계정을 만드세요.
- **전화번호:** [Meta의 WhatsApp 전화번호 요구 사항](https://developers.facebook.com/docs/whatsapp/phone-numbers)을 충족하는 번호를 사용하세요. 가입 중에 문자 메시지 또는 전화 통화로 일회용 인증 코드를 받게 됩니다.

{% alert important %}
초기 임베디드 가입은 통합 경로당 한 번만 완료하게 되므로, 비즈니스 세부 정보를 가능한 한 정확하게 입력하세요.
{% endalert %}

## WhatsApp 임베디드 가입 워크플로 {#whatsapp-embedded-signup-workflow}

Braze가 Meta 임베디드 가입을 실행한 후, 회사의 Business Manager에 액세스할 수 있는 Meta 계정으로 로그인합니다. Meta가 가입 화면을 호스팅하며, Braze는 해당 레이아웃이나 레이블을 제어하지 않습니다.

{% alert note %}
Meta는 사전 통지 없이 임베디드 가입 화면을 변경할 수 있습니다. 워크플로가 이 문서와 다를 경우 Meta의 안내를 따르고 [Meta의 임베디드 가입 설명서](https://developers.facebook.com/docs/whatsapp/embedded-signup/embed-the-flow)를 참조하세요.
{% endalert %}

일반적으로 Meta는 다음 단계를 안내합니다:

1. **로그인 및 권한 부여.** Meta로 인증하고 Braze가 WhatsApp Business 계정에 연결할 수 있도록 허용합니다.
2. **비즈니스 포트폴리오 선택.** WhatsApp Business 계정을 소유할 Business Manager 포트폴리오를 연결합니다. 예상한 포트폴리오가 보이지 않으면 Meta 권한을 확인하세요.
3. **WhatsApp Business 계정 연결 또는 생성.** 새 계정을 생성하거나 사용하지 않는 기존 계정을 선택합니다. 다른 메시징 공급자에 현재 연결된 WhatsApp Business 계정은 선택하지 마세요. 해당 연결은 Braze에서 성공하지 않습니다. [다른 공급자로부터 번호를 마이그레이션]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/migrate_a_phone_number)하려면, 시작하기 전에 Braze 계정 팀에 문의하세요.
4. **비즈니스 및 표시 세부 정보 제공.** Meta가 WhatsApp Business 계정에 대해 요청하는 계정 이름, 표시 이름 및 카테고리를 입력합니다.
5. **전화번호 인증.** WhatsApp 메시징에 사용할 번호를 추가하고 문자 메시지 또는 전화 통화로 인증을 완료합니다.

Meta가 임베디드 가입을 완료하면 제어가 Braze로 돌아옵니다.

## Braze 통합 완료하기 {#complete-the-braze-integration}

임베디드 가입 후 Braze가 자동으로 설정 단계를 실행합니다. **WhatsApp Messaging Integration** 페이지에서 Braze가 다음 작업을 수행하는 동안 **Sign-up flow completed, integration with WhatsApp in progress**와 같은 진행 메시지가 표시될 수 있습니다.

- Meta에서 WhatsApp Business 계정 ID 및 전화번호를 가져옵니다
- WhatsApp Business 계정에 Braze 시스템 사용자를 추가합니다
- 전화번호를 등록하고 웹훅 이벤트를 구독합니다
- 연결된 각 번호에 대해 Braze [구독 그룹]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)을 생성합니다

메시지를 보내기 전에 통합이 완료될 때까지 기다려 주세요. 설정에 실패한 경우, 통합 페이지에서 오류를 확인하고 일반적인 안내는 [WhatsApp 설정]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)을 참조하세요.

## 다음 단계 {#next-steps}

- [WhatsApp 전화번호 획득 또는 마이그레이션]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers)
- [WhatsApp 메시지 만들기]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message)
- [구독 그룹 관리]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)