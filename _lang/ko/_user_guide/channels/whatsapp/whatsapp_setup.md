---
nav_title: "설정"
article_title: "WhatsApp 설정"
alias: /partners/whatsapp/
description: "이 문서에서는 필수 조건 및 권장 다음 단계를 포함하여 Braze WhatsApp 채널을 설정하는 방법을 다룹니다."
page_type: partner
search_tag: Partner
page_order: 0
channel:
  - WhatsApp
search_rank: 2
---

# WhatsApp 설정 {#whatsapp-setup}

> [WhatsApp](https://www.whatsapp.com/) 비즈니스 메시징은 전 세계적으로 사용되는 인기 있는 P2P 메시징 플랫폼으로, 비즈니스를 위한 대화 기반 메시징을 제공합니다.

## 필수 조건 {#prerequisites}

통합을 진행하기 전에 다음 사항을 확인하세요:

- **옵트인 정책:** WhatsApp은 비즈니스가 메시징에 대해 고객의 옵트인을 받도록 요구합니다.
- **WhatsApp 콘텐츠 규칙:** WhatsApp에는 준수해야 하는 여러 [콘텐츠 규칙](https://www.whatsapp.com/legal/commerce-policy?l=en)이 있습니다.
- **규정 준수:** 모든 해당 Braze 및 Meta 설명서와 해당되는 [Meta 정책](https://www.whatsapp.com/legal/?lang=en)을 준수하세요.
- **24시간 대화 제한:** 비즈니스가 초기 템플릿 메시지를 보내거나 사용자가 메시지를 보낸 후, 양측이 서로 메시지를 주고받을 수 있는 24시간 기간이 시작됩니다.
- **대화 시작:** 사용자는 언제든지 대화를 시작할 수 있습니다. 비즈니스는 승인된 메시지 템플릿을 통해서만 대화를 시작할 수 있습니다.
<br><br>

| 요구 사항 | 설명 |
| ---| --- |
| Meta Business Manager 계정 | 이 메시징 채널을 활용하려면 Meta Business 계정이 필요합니다. |
| WhatsApp Business 계정 | 이 메시징 채널을 활용하려면 WhatsApp Business 계정이 필요합니다. |
| WhatsApp 전화번호 | 메시징 채널을 사용하려면 WhatsApp의 [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) 또는 [On-Premises API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers) 요구 사항을 충족하는 전화번호를 확보해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

### 1단계: WhatsApp 메신저를 Braze에 연결하기 {#step-1-connect-whatsapp-messenger-to-braze}

Braze에서 **파트너 통합** > **기술 파트너**로 이동하여 **WhatsApp**을 검색합니다.

WhatsApp 파트너 페이지에서 **Begin Integration**을 선택합니다.

![통합을 시작하는 버튼이 있는 WhatsApp 파트너 페이지.]({% image_buster /assets/img/whatsapp/whatsapp1.png %}){: style="max-width:70%;"}

열린 창에서 **Begin Integration** 버튼이 나타날 때까지 **Next**를 선택합니다. 버튼을 선택하여 통합 프로세스를 시작합니다.

![Braze를 WhatsApp에 연결하기 위한 안내.]({% image_buster /assets/img/whatsapp/instructions.png %}){: style="max-width:50%;"}

### 2단계: WhatsApp 설정 {#step-2-whatsapp-setup}

다음으로 Braze 설정 워크플로가 표시됩니다. 단계별 안내는 [WhatsApp 임베디드 가입]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup)을 참조하세요.

이 흐름에서 다음을 수행합니다:
1. Meta 및 WhatsApp Business 계정을 생성하거나 선택합니다. [WhatsApp 표시 이름 가이드라인](https://www.facebook.com/business/help/757569725593362)을 반드시 검토하세요. <br><br>회사에 이미 하나 이상의 기존 Meta Business 계정이 있을 가능성이 높습니다. 그런 경우 WhatsApp Business 계정을 포함시킬 계정을 선택하세요. WhatsApp에 대한 사용자 권한 및 비즈니스 인증은 Meta Business 계정에서 중앙 집중식으로 관리됩니다.<br><br>
2. WhatsApp Business 프로필을 생성합니다.
3. WhatsApp Business 번호를 인증합니다.<br><br>

설정이 완료되면 사용자를 위한 전용 WhatsApp 구독 그룹이 생성됩니다.

### 3단계: WhatsApp 템플릿 생성하기 {#step-3-create-whatsapp-templates}

승인된 WhatsApp 메시지 템플릿만 고객과의 대화를 시작하는 데 사용할 수 있습니다. WhatsApp 템플릿은 [Meta Business Manager](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343)에서 구축할 수 있습니다. Braze에서 지원하는 WhatsApp 메시징 기능 목록은 [지원되는 WhatsApp 기능]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#supported-whatsapp-features)을 확인하세요.

1. **[템플릿 매니저](https://business.facebook.com/wa/manage/message-templates)로 이동하기**<br>
Meta Business Manager에서 **Account Tools** 아래의 **Message Templates**를 선택합니다.
다음으로 **Create Templates**를 선택합니다.<br><br>![메시지 템플릿 목록이 있는 WhatsApp Manager.]({% image_buster /assets/img/whatsapp/whatsapp2.png %}){: style="max-width:100%;"}<br><br>
2. **메시지 설정**<br>
새 메시지 템플릿 작성기에서 메시지 카테고리를 선택하고, 템플릿 이름을 지정하고, 지원할 언어를 선택합니다. 나중에 언어를 삭제하거나 추가할 수 있습니다.<br><br>
	사용 가능한 메시지 템플릿 카테고리는 다음과 같습니다:
	- 마케팅: 인지도와 참여를 높이기 위해 프로모션 제안, 제품 공지 등을 전송합니다
	- 유틸리티: 중요한 정보를 공유하기 위해 계정 업데이트, 주문 업데이트, 알림 등을 전송합니다
	- 인증: 고객이 계정에 접근할 수 있도록 코드를 전송합니다<br><br>
	![마케팅, 유틸리티, 인증 카테고리가 있는 메시지 템플릿 작성기.]({% image_buster /assets/img/whatsapp/whatsapp3.png %}){: style="max-width:100%;"}<br><br>
3. **템플릿 편집하기**<br>
다음으로 메시지 템플릿을 생성합니다. <br><br>텍스트 또는 미디어 헤더, 텍스트 본문, 메시지 푸터, 버튼을 제공할 수 있습니다. 동영상 및 문서 헤더는 현재 사용할 수 없으며, 헤더는 텍스트 또는 이미지 유형이어야 합니다. 추가하는 미디어는 검토 프로세스를 위한 예시로 사용되며 템플릿 메시지에 **포함되지 않습니다**. 미디어는 Braze에서 추가해야 합니다. 메시지 미리보기가 패널에 표시됩니다. <br><br>Meta는 Liquid를 지원하지 않지만, 나중에 Braze에서 Liquid 변수로 대체할 수 있는 변수를 템플릿에 추가할 수 있습니다. 이를 위해 **+ Add variable** 버튼을 선택하세요.<br><br>![템플릿 작성기.]({% image_buster /assets/img/whatsapp/whatsapp4.png %}){: style="max-width:100%;"}

템플릿을 완성한 후 **Submit**을 누르세요.

#### 템플릿 승인 시간 {#template-approval-time}

메시지 템플릿의 승인 상태는 Meta Business Manager의 **Message Template** 페이지에서 확인하거나, Braze에서 Campaign 또는 Canvas를 생성할 때 확인할 수 있습니다. 또한 알림 권한 설정에 따라 WhatsApp 팀으로부터 이메일로 알림을 받을 수 있습니다.

{% alert note %}
승인된 템플릿은 원하는 만큼 많은 Campaign 및 Canvas에서 사용할 수 있습니다. 또한 원하는 만큼 많은 옵트인 사용자에게 전송할 수 있습니다. 이는 템플릿의 품질이 저하되지 않는 한 유효합니다.
{% endalert %}

### 4단계: WhatsApp Campaign 생성하기 {#step-4-create-a-whatsapp-campaign}

WhatsApp 템플릿이 승인되면 대시보드로 이동하여 [WhatsApp Canvas 또는 Campaign]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message)을 구축할 수 있습니다.

{% alert note %}
WhatsApp Business 계정이 생성된 후 Meta가 초기 메시징 한도를 결정합니다. 자세한 내용은 [처리량]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup/10dlc#throughput)을 확인하세요.
{% endalert %}

## 다음 단계 {#next-steps}

통합을 완료한 후 다음 두 가지 Meta 프로세스를 완료하는 것을 권장합니다:
- [비즈니스 인증](https://www.facebook.com/business/help/2058515294227817?id=180505742745347)
	- 기존 Meta Business Manager를 사용한 적이 있다면 이미 비즈니스 인증이 완료되어 있을 수 있습니다.
- [공식 비즈니스 계정](https://www.facebook.com/business/help/604726921052590?ref=search_new_0)

또한 [사용자 전화번호]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers)에 대해 읽어보고, [조직에서 메시지 템플릿](https://www.facebook.com/business/help/2169003770027706?id=2190812977867143)을 생성하는 데 접근이 필요한 사용자를 추가하는 것을 권장합니다.

### WhatsApp Cloud API 로컬 스토리지 {#whatsapp-cloud-api-local-storage}

Braze는 WhatsApp의 [Cloud API 로컬 스토리지](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/local-storage?content_id=ka6F9gESPqhQpm5)를 지원합니다. 이를 활성화하려면 Braze 고객지원 매니저에게 문의하세요.