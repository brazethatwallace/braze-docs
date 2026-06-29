---
nav_title: BYO WhatsApp 커넥터
article_title: Bring Your Own WhatsApp 커넥터
page_order: 2
description: "이 참조 문서에서는 Bring Your Own WhatsApp 커넥터를 설정하는 단계별 안내를 제공합니다. 이 커넥터를 통해 Braze가 Infobip WhatsApp Business Manager에 액세스할 수 있습니다."
page_type: reference
channel:
  - WhatsApp
---

# Bring Your Own WhatsApp 커넥터 {#bring-your-own-whatsapp-connector}

> Bring Your Own(BYO) WhatsApp 커넥터는 Braze와 Infobip 간의 파트너십을 제공하며, Braze가 Infobip WhatsApp Business Manager(WABA)에 액세스할 수 있도록 합니다. 이를 통해 Braze에서 세분화, 개인화, Campaign 오케스트레이션을 활용하면서 메시징 비용은 Infobip과 직접 관리하고 결제할 수 있습니다. Braze는 아웃바운드 메시지, 인바운드 메시지 처리, WhatsApp 플로우, 분석 등 WhatsApp 채널이 제공하는 모든 기존 기능을 유지합니다.

## 요구 사항 {#requirements}

| 요구 사항 | 설명 |
| --- | --- |
| Infobip 계정 | BYO WhatsApp 커넥터를 사용하려면 Infobip 계정이 필요합니다. |
| 메시지 또는 액션 크레딧 | WhatsApp 메시지를 보낼 때 Braze 액션 크레딧이 소비됩니다. |
| WhatsApp 요구 사항 | 모든 [WhatsApp 요구 사항]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/#prerequisites)을 완료하세요. |
| 전화번호 | 편의를 위해 [Infobip을 통해 전화번호를 취득](https://www.infobip.com/docs/numbers/getting-started)하는 것을 권장합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="요구 사항" }

## 설정 {#set-up}

BYO WhatsApp 커넥터를 설정하기 전에, WhatsApp Business 계정의 이전 발송이 Infobip을 통해 이루어지지 않았는지 확인하세요.

### 지원되는 사례 {#supported-cases}

- WhatsApp Business 계정과 전화번호가 이전에 파트너에 연결된 적이 없는 경우
- WhatsApp Business 계정이 네이티브 통합을 통해 Braze에 직접 연결된 경우
    - [WhatsApp 전화번호 마이그레이션]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/migrate_a_phone_number/)의 단계를 따라 전화번호를 한 번에 하나씩 새 WhatsApp Business 계정으로 마이그레이션하세요.
- WhatsApp Business 계정이 Braze 및 Infobip이 아닌 다른 솔루션 제공업체에 연결된 경우
    - [WhatsApp 전화번호 마이그레이션]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/migrate_a_phone_number/)의 단계를 따라 전화번호를 한 번에 하나씩 새 WhatsApp Business 계정으로 마이그레이션하세요.

## 1단계: Infobip 계정 정보 가져오기 {#step-1}

1. Infobip에서 WhatsApp Business 계정에 사용할 계정을 확인합니다.
2. **Developer Tools** > **API Keys**로 이동하여 **Create API Key**를 선택합니다.

![생성일 "16/12/2025", 만료일 "16/12/36"이 표시된 "Create API key" 페이지.]({% image_buster /assets/img/whatsapp/byo_connector/create_api_key.png %})

{: start="3"}
3. "Braze - My Workspace Name - My WABA Name"과 같이 의미 있는 이름을 키에 지정합니다.
4. 토큰 만료 문제를 방지하기 위해 만료 날짜를 먼 미래로 설정합니다.
    - 만료 날짜 전에 새 API 키를 생성하고 WABA를 다시 연결해야 한다는 점을 기록해 두세요.
5. 다음 스코프를 선택합니다:
- `Message:send`
- `Whatsapp:manage`
- `Whatsapp:message:send`
- `Account-management:manage`
- `Subscriptions:manage`
- `Metrics:manage`
6. 키를 생성한 후 API 키를 복사합니다.
    - 키는 생성 후 제한된 시간 동안만 복사할 수 있습니다. 향후 다른 WhatsApp Business 계정을 연결해야 하는 경우 이 단계를 반복하여 새 키를 생성할 수 있습니다.

![6개의 스코프가 추가된 "Braze Example API Key".]({% image_buster /assets/img/whatsapp/byo_connector/api_key.png %})

{: start="7"}
7. 계정 API 기본 URL을 복사합니다.

![API 기본 URL이 강조 표시된 "API keys" 페이지.]({% image_buster /assets/img/whatsapp/byo_connector/api_base_url.png %})

## 2단계: 임베디드 가입 시작 {#step-2-start-the-embedded-signup}

1. Braze에서 **파트너 통합** > **기술 파트너** > **WhatsApp**으로 이동합니다.
2. **BYO Connector - Infobip** 탭을 선택합니다.

![WhatsApp 기술 파트너 페이지.]({% image_buster /assets/img/whatsapp/byo_connector/byo_tab_tech_parners.png %})

{: start="3"}
3. [1단계](#step-1)에서 가져온 API 키와 기본 URL을 입력합니다.
4. **연결**을 선택합니다.
5. 다음 사항을 고려하여 [임베디드 가입 워크플로우]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup/#whatsapp-embedded-signup-workflow)를 진행합니다:
- 다른 Business Solution Provider가 사용하는 것과 동일한 비즈니스 포트폴리오를 선택할 수 없습니다.
- 다른 Business Solution Provider가 사용하는 전화번호를 선택할 수 없습니다.
- 기존 WABA를 선택하지 말고 새 WABA를 생성해야 합니다.

{% alert note %}
인증 코드를 받으려면 Infobip 대시보드 > **Analyze** > **Logs**로 이동하여 인바운드 SMS 메시지에서 코드를 확인하세요.
{% endalert %}

![인증 코드가 포함된 인바운드 SMS 메시지를 보여주는 메시지 로그.]({% image_buster /assets/img/whatsapp/byo_connector/verification_code.png %})

설정을 완료하면 전화번호가 WhatsApp Business 그룹 아래에 구독 그룹으로 나열됩니다. WhatsApp Business 그룹에는 연결된 Infobip 계정 이름과 API 기본 URL이 포함됩니다. 네이티브 통합을 통해 연결된 계정에는 Infobip 계정 이름이 표시되지 않습니다.

{% alert note %}
각 WhatsApp Business 계정을 단일 Infobip 계정에 연결하세요. 추가 전화번호 또는 구독 그룹을 연결할 때마다, WhatsApp Business 계정이 이미 Infobip 계정에 연결되어 있는 경우 기존 계정의 API 자격 증명을 다시 입력해야 합니다.
{% endalert %}

## 3단계: 메시지 발송 {#step-3-sending-messages}

다음을 포함하여 네이티브 통합 발송 프로세스를 따르세요:
- [구독 그룹에 사용자 구독]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups/)
- [WhatsApp 메시지 생성]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/)

## 설정 문제 해결 {#troubleshooting-setup}

### WhatsApp Business 계정 ID를 가져올 수 없음 {#couldnt-retrieve-whatsapp-business-account-id}

WhatsApp Business 계정이 다른 Braze 워크스페이스에 연결되어 있지 않은지 확인하세요.

### WhatsApp Business 계정 ID를 Infobip과 공유할 수 없음 {#couldnt-share-whatsapp-business-account-id-with-infobip}

1. WhatsApp Business 계정이 Braze 또는 다른 파트너에 연결되어 있지 않은지 확인하세요.
2. WhatsApp Business 계정의 전화번호가 다른 Infobip 계정에 연결되어 있지 않은지 확인하세요. 가져온 번호의 경우 Infobip에서 해당 번호를 찾아 **Cancel number**를 선택할 수 있습니다.

## 고려 사항 {#considerations}

Braze의 모든 기존 기능이 지원되지만, 다음 사용 사례는 현재 지원되지 않습니다.

| 사용 사례 | 이유 |
| --- | --- |
| Braze와 Infobip에서 인바운드 메시지 처리 | 이는 두 시스템 중 하나에 의해 트리거되는 로직 체인을 방지하여, 중복되고 잠재적으로 모순되는 메시지 스레드가 생성되는 것을 막기 위함입니다. |
| Braze와 Infobip에서 메시지 발송 | Braze에 연결된 WhatsApp Business 계정의 경우, 모든 발송은 Braze에서 시작됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="고려 사항" }