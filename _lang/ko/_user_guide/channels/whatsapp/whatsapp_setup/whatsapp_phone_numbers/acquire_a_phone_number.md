---
nav_title: "번호 획득"
article_title: "WhatsApp 전화번호 획득"
page_order: 1
description: "이 참조 문서에서는 Twilio 및 Infobip에서 전화번호를 획득하는 방법을 다룹니다."
page_type: reference
channel:
  - WhatsApp
---

# WhatsApp 전화번호 획득 {#acquire-a-whatsapp-phone-number}

> WhatsApp 메시징 채널을 사용하려면 WhatsApp의 [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) 또는 [On-Premises API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers) 요구 사항을 충족하는 전화번호가 필요합니다.

Braze에서 번호를 프로비저닝하지 않으므로 직접 전화번호를 획득해야 합니다. 비즈니스 전화 제공업체를 통해 SIM 카드가 포함된 실물 전화기를 구매하거나, 파트너인 Twilio 또는 Infobip을 사용할 수 있습니다. **Braze를 통해서는 이 작업을 수행할 수 없으므로 Twilio 또는 Infobip 계정을 직접 보유하고 있어야 합니다.**

## WhatsApp API 요구 사항 {#whatsapp-api-requirements}

전화번호는 다음 WhatsApp API 요구 사항을 충족해야 합니다:

- 비즈니스에서 소유한 번호
- 국가 코드 및 지역 코드가 있는 번호(유선 전화 및 휴대전화 번호 등)
- 음성 통화 또는 SMS 수신이 가능한 번호
- 계정 설정 중 접근 가능한 번호(인증 코드 수신용)
- 짧은 코드가 아닌 번호
- WhatsApp Business Platform에서 이전에 사용되지 않은 번호
- 개인 WhatsApp 계정에 연결되지 않은 번호

## Twilio 전화번호 획득 {#acquiring-a-twilio-phone-number}

### 1단계: Twilio 콘솔 또는 API에서 전화번호 구매 {#step-1-buy-a-phone-number-from-the-twilio-console-or-api}

1. Twilio 콘솔에서 **Develop** > **Phone Numbers** > **Manage** > **Buy a number**로 이동합니다. 이 옵션이 보이지 않으면 **Explore Products**를 선택하고 **Super Networks**까지 스크롤한 다음 **Phone Number** > **Buy a number**를 선택합니다. <br><br>![Twilio 콘솔에서 'Develop' 탭이 열려 있고 'Buy a number' 옵션이 표시된 화면.]({% image_buster /assets/img/whatsapp/develop_buy_number.png %}){: style="max-width:20%;"}<br><br>

2. 원하는 지역 코드 또는 지역(있는 경우)을 입력합니다. 번호를 찾은 다음 **Buy**를 선택합니다. <br><br> ![나열된 전화번호를 구매하는 버튼.]({% image_buster /assets/img/whatsapp/buy.png %})<br><br>

3. 전화번호를 구매한 후 **Active Numbers**로 이동하여 방금 구매한 전화번호를 선택합니다. <br><br>![구매한 전화번호가 표시된 'Active Numbers' 화면.]({% image_buster /assets/img/whatsapp/active_numbers.png %}){: style="max-width:70%;"}<br><br>

### 2단계: 전화번호 구성 {#step-2-configure-your-phone-number}

이메일로 인증 코드를 수신할 수 있도록 Twilio 전화번호를 구성합니다. **Twilio 콘솔에서 전화번호를 WhatsApp에 연결하지 마세요.**

{% alert warning %}
Twilio 콘솔에서 전화번호를 WhatsApp에 연결하지 마세요. 연결하면 해당 번호가 Twilio의 WhatsApp Business Account에 등록되어 임베디드 가입 워크플로를 통해 Braze에 연결할 수 없게 됩니다.
{% endalert %}

1. Twilio 콘솔에서 [Active Numbers 페이지](https://www.twilio.com/console/phone-numbers/incoming)로 이동하여 구매한 전화번호를 선택합니다.
2. **Voice Configuration** 섹션으로 이동하여 **Configure with** 드롭다운에서 **Webhook, TwiML Bin, Function, Studio Flow, Proxy Service**를 선택합니다.
3. **A call comes in** 행에서 **Webhook**을 선택하고 URL을 `https://twimlets.com/voicemail?Email=YOUR_EMAIL_ADDRESS`로 설정합니다. `YOUR_EMAIL_ADDRESS`를 본인의 이메일 주소로 바꿉니다.

### 3단계: 임베디드 가입 워크플로 완료 {#step-3-complete-the-embedded-sign-up-workflow}

1. Twilio 구성이 완료되면 Braze 대시보드 > **기술 파트너** > **WhatsApp**으로 이동하여 **Begin integration** 또는 **Add WhatsApp Business Account** 중 표시되는 옵션을 선택하여 [임베디드 가입 워크플로]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup)를 시작합니다.<br><br>**Add a phone number for WhatsApp** 단계에서 전화번호 인증 방법으로 **Phone call**을 선택합니다. <br><br>![문자 메시지 또는 전화 통화를 통해 전화번호를 인증하는 옵션이 있는 섹션.]({% image_buster /assets/img/whatsapp/verify.png %}){: style="max-width:50%;"}<br><br>

2. 인증 코드가 이메일 받은편지함으로 전송될 때까지 몇 분 기다린 후 인증 코드를 입력하고 설정을 완료합니다.

## Infobip 전화번호 획득 {#acquiring-an-infobip-phone-number}

1. Infobip 콘솔에서 **Channels and Numbers**로 이동하여 **Numbers**를 선택합니다.<br><br>![Infobip의 'Channels and Numbers' 섹션 아래에 'Numbers'가 나열된 화면.]({% image_buster /assets/img/whatsapp/infoblip_numbers.png %}){: style="max-width:30%;"}<br><br>

2. **Buy Number** > 메시지를 보내려는 국가 > **SMS**를 선택합니다.<br><br>![번호를 구매하는 버튼.]({% image_buster /assets/img/whatsapp/infoblip_buy.png %})<br><br>

3. 선택한 국가에 따라 추가 등록 절차를 완료해야 할 수 있습니다(예: 미국 전화번호의 경우 10DLC 또는 수신자 부담 옵션 선택). 사용 가능한 옵션을 선택하세요.<br><br>![번호 유형을 선택하는 페이지: 10DLC 또는 수신자 부담.]({% image_buster /assets/img/whatsapp/infoblip_10dlc.png %}){: style="max-width:70%;"}<br><br>

4. 사용 가능한 제안을 선택한 다음 나머지 단계를 진행하고 요청이 처리될 때까지 기다립니다. **Numbers** > **My Request**로 이동하여 상태를 확인할 수 있습니다. <br><br>![수수료 및 커버리지 정보가 포함된 제안.]({% image_buster /assets/img/whatsapp/infoblip_offer.png %}){: style="max-width:70%;"}<br><br>

5. 선택한 국가에 따라 Infobip 팀이 등록 세부 정보(예: 미국의 10DLC)에 대해 연락할 때까지 기다립니다.<br><br>

6. Infobip에서 전화번호가 준비되면 Braze 대시보드 > **기술 파트너** > **WhatsApp**으로 이동하여 **Begin integration** 또는 **Add WhatsApp Business Account** 중 표시되는 옵션을 선택하여 [임베디드 가입 워크플로]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup)를 시작합니다.<br><br> **Add a phone number for WhatsApp** 단계에서 전화번호 인증 방법으로 **Text message**를 선택합니다.<br><br>![문자 메시지 또는 전화 통화를 통해 전화번호를 인증하는 옵션이 있는 섹션.]({% image_buster /assets/img/whatsapp/infoblip_verify.png %})<br><br>

7. Infobip 고객 포털의 [analyze logs](https://www.infobip.com/docs/analyze/analyze-logs)에서 인증 코드를 확인합니다. 표시되기까지 몇 분이 걸릴 수 있습니다. 인증 코드를 입력하고 설정을 완료합니다.