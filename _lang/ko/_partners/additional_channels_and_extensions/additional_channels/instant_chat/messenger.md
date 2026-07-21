---
nav_title: 메신저
article_title: Facebook 메신저
alias: /partners/messenger/
description: "이 참조 문서에서는 세계에서 가장 인기 있는 인스턴트 메시징 플랫폼 중 하나인 Facebook 메신저와 Braze 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# Facebook 메신저 {#facebook-messenger}

> [Facebook 메신저](https://developers.facebook.com/docs/messenger-platform/)는 세계에서 가장 인기 있는 인스턴트 메시징 플랫폼 중 하나로, 약 10억 명의 월간 활성 사용자가 이용하고 있습니다. 이 플랫폼을 통해 브랜드는 매력적인 챗봇을 만들어 고객과 지능적이고 자동화된 방식으로 상호작용할 수 있습니다.

Braze와 Facebook 통합은 Braze 웹훅, 세분화, 개인화 및 트리거 기능을 활용하여 메신저 플랫폼 API를 통해 Facebook 메신저에서 사용자에게 메시지를 보냅니다. 커스텀 Facebook 메신저 웹훅 템플릿은 플랫폼의 **콘텐츠** > **웹훅**에서 제공됩니다.

Facebook 메신저 플랫폼은 "기존 거래를 지원하거나, 기타 고객 지원 조치를 제공하거나, 사용자가 요청한 콘텐츠를 전달하는 비홍보성 메시지"를 위한 것입니다. 자세한 내용은 [Facebook 플랫폼 가이드라인](https://developers.facebook.com/docs/messenger-platform) 및 [허용되는 사용 사례 예시](https://developers.facebook.com/docs/messenger-platform/app-review#examples_acceptable)를 참조하세요.

## 필수 조건 {#prerequisites}

통합을 진행하기 전에 다음 사항을 확인하세요:

- Facebook은 메신저 플랫폼을 마케팅 메시지 전송에 사용하는 것을 허용하지 않습니다.
- 페이지에서 메시지를 보내려면 사용자의 명시적인 동의가 필요합니다.
- Facebook 앱의 테스트 사용자가 아닌 사용자에게 메시지를 보내려면 앱이 Facebook의 [앱 검토](https://developers.facebook.com/docs/messenger-platform/app-review)를 통과해야 합니다.<br><br>

| 요구 사항 | Origin | 접근 | 설명 |
| --- | --- | --- | --- |
| Facebook 메신저 페이지 | Facebook | [https://www.facebook.com/pages/create](https://www.facebook.com/pages/create) | Facebook 페이지는 봇의 ID로 사용됩니다. 사용자가 앱과 채팅할 때 페이지 이름과 프로필 사진이 표시됩니다. |
| Facebook 메신저 앱 | Facebook | [https://developers.facebook.com/apps](https://developers.facebook.com/apps) | Facebook 앱에는 액세스 토큰을 포함한 메신저 봇의 설정이 포함되어 있습니다. |
| 앱 봇 검토 및 승인 | Facebook | [https://developers.facebook.com/docs/messenger-platform/app-review](https://developers.facebook.com/docs/messenger-platform/app-review) | 봇을 공개적으로 출시할 준비가 되면 Facebook에 검토 및 승인을 위해 제출해야 합니다. 이 검토 과정을 통해 메신저 봇이 정책을 준수하고 예상대로 작동하는지 확인한 후 메신저의 모든 사용자에게 제공합니다. |
| 페이지 범위 ID(PSID) | Facebook | [https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages) | Facebook 메신저에서 메시지를 보내려면 사용자의 PSID가 필요합니다. 사용자가 메신저를 통해 앱과 상호작용하면 Facebook이 PSID를 생성합니다. 이 PSID는 문자열 커스텀 속성으로 Braze에 전송할 수 있습니다. |
| 페이지 액세스 토큰 | Facebook | [https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token](https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token) | 이 액세스 토큰은 사용자 액세스 토큰과 유사하지만, Facebook 페이지에 속한 데이터를 읽고, 쓰고, 수정하는 API에 대한 권한을 제공합니다. 페이지 액세스 토큰을 얻으려면 먼저 사용자 액세스 토큰을 얻고 `manage_pagespermission`을 요청해야 합니다. 사용자 액세스 토큰을 얻은 후 Graph API를 통해 페이지 액세스 토큰을 가져옵니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="필수 조건" }

## 통합 {#integration}

다음은 Braze Facebook 메신저 웹훅을 설정하는 방법을 보여줍니다.
봇 설정에 추가 도움이 필요한 경우, 전체 메신저 봇 튜토리얼과 예제 코드를 [Braze GitHub 리포지토리](https://github.com/Appboy/appboy-fb-messenger-bot)에서 확인할 수 있습니다!

### 1단계: PSID 수집 {#step-1-collect-your-psids}

Facebook 메신저에서 메시지를 보내려면 사용자의 페이지별 ID(PSID)를 수집하여 사용자를 식별하고 일관되게 상호작용해야 합니다. PSID는 사용자의 Facebook ID와 동일하지 않습니다. Facebook은 고객에게 메시지를 보내거나 고객이 메시지를 보낼 때마다 이 식별자를 생성합니다.

PSID는 Facebook이 제공하는 다양한 [진입점](https://developers.facebook.com/docs/messenger-platform/discovery)을 사용하여 찾을 수 있습니다. 사용자가 앱에 메시지를 보내거나 대화에서 버튼을 탭하거나 메시지를 보내는 등의 동작을 수행하면, 해당 PSID가 웹훅 이벤트의 `sender.id` 속성에 포함되어 봇이 동작을 수행한 사용자를 식별할 수 있습니다.

```
{
  "sender":{
    "id":"<PSID>"
  },
  "recipient":{
    "id":"<PAGE_ID>"
  },
  "timestamp":1458692752478,
  "message":{
    "mid":"mid.1457764197618:41d102a3e1ae206a38",
    "text":"hello, world!",
    "quick_reply": {
      "payload": "<DEVELOPER_DEFINED_PAYLOAD>"
    }
  }
}
```

메시지를 보낼 때마다 해당 PSID가 요청의 `recipient.id` 속성에 포함되어 메시지를 받을 사용자를 식별합니다.

### 2단계: 커스텀 속성으로 Braze에 전송 {#step-2-send-to-braze-as-a-custom-attribute}

PSID를 수신하고 있다고 확인되면, 개발자와 협력하여 PSID를 [커스텀 속성]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes#custom-attributes)으로 Braze에 전송하세요. PSID는 [API 호출](https://developers.facebook.com/documentation/business-messaging/messenger-platform/send-messages)을 통해 접근할 수 있는 문자열입니다.

### 3단계: 웹훅 템플릿 설정 {#step-3-set-up-your-webhook-template}

Facebook 메신저 웹훅 템플릿을 생성하려면 다음을 수행합니다.

1. **콘텐츠** > **웹훅**으로 이동하여 **웹훅 템플릿 생성**을 선택합니다.
2. **템플릿** > **Braze 템플릿**을 선택합니다.
3. "Facebook Messenger" 템플릿을 찾아 선택합니다.
4. **템플릿 선택**을 선택합니다.

1. 템플릿 이름을 입력하고 필요에 따라 Teams와 태그를 추가합니다.
2. 메시지를 입력하거나 [Facebook에서 제공하는 메시지 템플릿](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages)에서 선택합니다. 메시지 [유형](https://developers.facebook.com/docs/messenger-platform/send-messages#message_types) 또는 [태그](https://developers.facebook.com/docs/messenger-platform/send-messages/message-tags)를 선택할 수도 있습니다.
3. PSID를 커스텀 속성으로 포함합니다. **Request Body** 상자 모서리에 있는 파란색과 흰색 **+** 버튼을 사용하여 수행할 수 있습니다.
3. 웹훅 URL에서 `FACEBOOK_PAGE_ACCESS_TOKEN`을 실제 토큰으로 교체하여 페이지 액세스 토큰을 추가합니다.

#### 웹훅 미리보기 및 테스트 {#previewing-and-testing-your-webhook}

메시지를 보내기 전에 웹훅을 테스트하세요. 메신저 ID가 Braze에 저장되어 있는지 확인하고(또는 찾아서 커스텀 사용자로 테스트), 미리보기를 사용하여 테스트 메시지를 전송합니다.

![기존 사용자에게 메시지를 전송하여 미리 볼 수 있는 Facebook 메신저 웹훅 템플릿의 테스트 탭.]({% image_buster /assets/img_archive/fbm-test.png %})

메시지를 성공적으로 수신했다면 전달 설정을 구성할 수 있습니다.

## 이 통합 사용하기 {#using-this-integration}

설정이 완료되면 이 통합을 사용하여 Facebook 메신저 사용자를 타겟팅합니다. 사용자의 전화번호를 사용하여 메시지를 보내지 않고 메신저 메시지를 반복적으로 보낼 계획이라면, 메신저 ID가 커스텀 속성으로 존재하는 모든 사용자에 대해 [Segment를 생성]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#creating-a-segment)하고 [분석 추적]({{site.baseurl}}/user_guide/audience/segments/segment_data)을 활성화하여 시간 경과에 따른 메신저 구독률을 추적해야 합니다.

![Segment 필터 "messenger_id"가 "비어 있지 않음"으로 설정됨.]({% image_buster /assets/img_archive/fbm-segmentation.png %})

메신저 구독자를 위한 특정 Segment를 생성하지 않기로 선택한 경우, 오류를 방지하기 위해 메신저 ID가 존재하는지에 대한 필터를 포함해야 합니다.

다른 세분화를 사용하여 메신저 Campaign을 타겟팅할 수도 있으며, 나머지 Campaign 생성 프로세스는 다른 Campaign과 동일합니다.