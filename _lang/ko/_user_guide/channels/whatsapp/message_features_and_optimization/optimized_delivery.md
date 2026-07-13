---
nav_title: 최적화된 전달
article_title: 최적화된 전달을 사용한 WhatsApp 메시지
page_order: 1
description: "이 참조 문서에서는 최적화된 전달을 사용하여 WhatsApp 메시지를 구축하고 생성하는 단계를 다룹니다."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
---

# 최적화된 전달을 사용한 WhatsApp 메시지 {#whatsapp-messages-with-optimized-delivery}

> 동적이고 참여 기반의 전달을 통해 WhatsApp에서 더 많은 적합한 사용자에게 도달하여 전달 가능성과 참여를 높이세요.

최적화된 전달을 사용한 WhatsApp 메시지는 Meta의 [WhatsApp용 마케팅 메시지 API](https://developers.facebook.com/docs/whatsapp/marketing-messages-api-for-whatsapp)(WhatsApp용 MM API)를 사용하여 발송되며, 동적이고 참여 기반의 전달을 제공합니다. 이는 참여도가 높은 메시지(예: 읽히고 클릭될 가능성이 높은 메시지)가 해당 메시지에 참여할 가능성이 높은 더 많은 사용자에게 도달할 수 있음을 의미합니다. WhatsApp은 메시지가 기대되고, 관련성이 있으며, 시의적절하여 읽히고 클릭될 가능성이 높은 경우 해당 메시지를 높은 참여도로 간주합니다.

브랜드는 Cloud API와 비교하여 WhatsApp용 MM API를 통해 동등하거나 더 높은 전달 가능성을 기대할 수 있습니다. Meta에 따르면, 인도에서 높은 참여도의 마케팅 메시지는 Cloud API 대비 최대 9% 더 많은 메시지가 전달되었습니다. WhatsApp용 MM API는 여전히 100% 전달 가능성을 보장하지 않는다는 점에 유의하세요.

## 지역별 가용성 {#regional-availability}

최적화된 전달의 가용성과 최적화 기능은 비즈니스 전화번호와 사용자의 지역에 따라 달라집니다. 자세한 내용은 [기능의 지리적 가용성](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/get-started#geographic-availability-of-features)을 참조하세요.

## 최적화된 전달 설정 {#setting-up-optimized-delivery}

1. Braze에서 **파트너 통합** > **기술 파트너** > **WhatsApp**으로 이동합니다.
2. **최적화된 전달로 발송 최적화** 섹션에서 **설정 업그레이드**를 선택하여 [임베디드 가입 워크플로]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup)를 트리거합니다.

![최적화된 전달로 발송을 최적화하는 옵션이 있는 WhatsApp 메시지 통합 섹션.]({% image_buster /assets/img/whatsapp/whatsapp_messaging_integration.png %})

{: start="3"}
3. 최적화된 전달이 활성화되면 **WhatsApp 비즈니스 계정 관리**의 계정 세부 정보에 최적화된 전달 상태가 표시됩니다.

![활성 번호 상태를 가진 구독 그룹이 나열된 WhatsApp 비즈니스 계정 관리 섹션.]({% image_buster /assets/img/whatsapp/optimized_delivery_message.png %})

또는 WhatsApp 매니저에서 직접 최적화된 전달을 활성화한 다음 Braze에서 발송을 시작할 수 있습니다.

### 설정 문제 해결 {#troubleshooting-your-setup}

- **일반 오류:** 업그레이드 중 문제가 발생하면 이 오류 배너가 표시되며 [고객지원에 문의]({{site.baseurl}}/braze_support)하도록 안내합니다.
- **부적격 오류:** Meta에 의해 제한된 경우 다음 오류 배너가 표시됩니다: "하나 이상의 WhatsApp 비즈니스 계정이 Meta에 의해 제한되었습니다. 업그레이드하려면 계정이 양호한 상태여야 합니다." 이 문제가 해결될 때까지 해제할 수 없습니다.

## Campaigns 및 Canvases에서 최적화된 전달 사용 {#using-optimized-delivery-in-campaigns-and-canvases}

최적화된 전달은 **마케팅 메시지**에 사용해야 합니다. Braze는 **유틸리티, 인증, 서비스 및 응답 메시지**에 대해 최적화된 전달 옵션을 자동으로 제거하며, 이러한 메시지는 기본 설정인 Cloud API를 통해 계속 발송되어야 합니다.

### 전달 방법 선택 {#selecting-the-delivery-method}

1. Campaign 또는 Canvas 메시지 단계의 Braze WhatsApp 작성기에서 **설정** 탭으로 이동합니다.
2. **전달 방법** 섹션에서 WhatsApp 비즈니스 계정(WABA)이 활성화된 경우 **최적화된 전달(권장)** 체크박스가 기본적으로 선택되어 있습니다. 해당 특정 메시지에 최적화된 전달을 사용하지 않으려면 체크박스를 해제하세요.
- 최적화된 전달을 선택했지만 사용할 수 없는 경우, 메시지는 자동으로 Cloud API 방법으로 대체됩니다.

![최적화된 전달을 선택하는 체크박스가 있는 미리보기 탭이 포함된 메시지 작성기.]({% image_buster /assets/img/whatsapp/delivery_method_settings.png %})

### 다른 Braze 채널에서 사용자 리타겟팅 {#retargeting-users-on-other-braze-channels}

WhatsApp용 MM API는 100% 전달 가능성을 제공하지 않으므로, 메시지를 받지 못한 사용자를 다른 채널에서 리타겟팅하는 방법을 이해하는 것이 중요합니다.

사용자를 리타겟팅하려면 특정 메시지를 받지 못한 사용자의 Segment를 구축하는 것을 권장합니다. 이를 위해 오류 코드 `131049`로 필터링하세요. 이 코드는 WhatsApp의 사용자별 마케팅 템플릿 제한 적용으로 인해 마케팅 템플릿 메시지가 발송되지 않았음을 나타냅니다. Braze 커런츠 또는 SQL 세그먼트 확장을 사용하여 이를 수행할 수 있습니다:

- **Braze 커런츠:** Braze 커런츠를 사용하여 메시지 실패 이벤트를 내보냅니다. 그런 다음 이 데이터를 사용하여 고객 프로필의 커스텀 속성(예: `whatsapp_failed_last_msg: true`)을 업데이트하고, 이를 리타겟팅 Campaign의 필터로 사용할 수 있습니다.
- **SQL 세그먼트 확장:** 이 기능에 액세스할 수 있는 경우, SQL을 사용하여 메시지 실패 로그를 쿼리하고 해당 사용자의 Segment를 생성한 다음, 다른 채널에서 해당 Segment를 타겟팅할 수 있습니다.