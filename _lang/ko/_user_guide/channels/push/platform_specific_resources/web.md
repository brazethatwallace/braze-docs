---
nav_title: "웹 푸시"
article_title: 웹 푸시 알림
page_order: 8.5
page_type: reference
description: "이 참조 페이지에서는 웹 푸시 알림에 대해 간략히 설명하고, 웹 푸시 알림을 생성하는 데 필요한 단계로 연결합니다."
platform: Web
channel:
  - push

---

# 웹 푸시 {#web-push}

> Braze의 웹 푸시 알림에 대해 알아보고, 직접 만들기 위한 리소스를 확인하세요.

웹 푸시는 웹 애플리케이션 사용자와 소통할 수 있는 또 다른 훌륭한 방법입니다. [지원되는 브라우저](#supported-browsers)에서 웹사이트를 방문하는 고객은 웹 페이지가 로드되어 있는지 여부에 관계없이 웹 애플리케이션에서 웹 푸시를 수신하도록 옵트인할 수 있습니다.

## 필수 조건 {#prerequisites}

Braze를 사용하여 푸시 메시지를 생성하고 전송하려면 먼저 개발자와 협력하여 웹사이트에 푸시를 통합해야 합니다. 자세한 단계는 [웹 푸시 통합 가이드]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web)를 참조하세요.

### 푸시 권한 {#push-permission}

모든 브랜드는 자사 웹사이트에 웹 푸시 알림을 통합하고 사용할 수 있습니다. 알림은 웹 브라우저가 열려 있는 한 현재 및 이전 웹 방문자 모두에게 도달할 수 있지만, 기존 모바일 앱 푸시와 마찬가지로 방문자가 [알림 수신에 옵트인]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#push-permission)해야 합니다.

{% alert tip %}
인브라우저 메시지를 사용하여 사용자에게 웹 푸시 옵트인을 유도하는 것을 고려해 보세요. 이를 [푸시 프라이머]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)라고도 합니다.
{% endalert %}

## 개요 {#overview}

웹 푸시 알림은 긴급하고 실행 가능한 업데이트를 전달하여 빠른 전환을 유도합니다. 웹 푸시를 사용하면 다음을 수행할 수 있습니다:

- 가격 인하와 같이 중요한 데이터가 변경될 때 즉시 메시지를 트리거
- 명확한 실행 버튼으로 사용자를 웹사이트로 다시 유도
- 제품 및 고객 정보로 푸시를 개인화하여 메시지의 관련성 향상

웹 푸시는 휴대폰의 앱 푸시 알림과 동일한 방식으로 작동합니다. 웹 푸시 작성에 대한 자세한 내용은 [푸시 알림 만들기]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#create-a-push-message)를 확인하세요.

![노트북과 휴대폰에 동일한 푸시 메시지가 표시된 웹 푸시 예시.]({% image_buster /assets/img_archive/Macbook_Push.png %}){: style="border:none"}

## 잠재적 사용 사례 {#potential-use-cases}

다음은 일반적인 웹 푸시 메시지 사용 사례의 예시입니다.

| 사용 사례 | 설명 |
| --- | --- |
| 무료 평가판 | 웹사이트의 신규 방문자에게 무료 평가판 가입을 유도합니다. 사용자에게 여러분의 특별한 점을 경험할 기회를 제공하면 유료 고객으로 전환될 가능성이 높아집니다. |
| 앱 다운로드 | 웹 사용자를 모바일 앱으로 유도하여 제품에서 더 많은 가치를 얻을 수 있도록 합니다. 현재 참여 패턴을 기반으로 앱의 이점을 강조하는 개인화를 활용하는 것을 고려해 보세요. |
| 할인 및 세일 | 시간에 민감한 이벤트와 프로모션에 대한 고객 인지도를 높입니다. 웹 푸시를 포함한 여러 채널을 통해 메시지를 전달하여 브랜드 프로모션에 대한 인지도를 높이세요. |
| 장바구니 유기 | 거래를 완료하지 않은 사용자에게 자동 리마인더를 보내 결제 흐름으로 다시 유도합니다. <br><br>Braze의 연구에 따르면 웹 푸시는 수신자가 다시 돌아와 구매를 완료하도록 하는 데 이메일보다 53% 더 효과적이고, 모바일 푸시보다 23% 더 큰 영향력을 가집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="잠재적 사용 사례" }

## 지원되는 브라우저 {#supported-browsers}

다음 브라우저는 웹 푸시 알림을 지원합니다.

{% multi_lang_include alerts/important_alerts.md alert='Web push private browsing' %}

- Chrome(및 Android 모바일용 Chrome)
- Safari(버전 16 이상)
- Firefox(및 Android 모바일용 Firefox)
- Opera
- Edge

푸시 프로토콜 표준 및 브라우저 지원에 대한 자세한 내용은 브라우저별 리소스를 참조하세요:

- [Safari(데스크탑)](https://developer.apple.com/notifications/safari-push-notifications/)
- [Safari(모바일)]({{site.baseurl}}/developer_guide/push_notifications?sdktab=safari)
- [Mozilla Firefox](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility)
- [Microsoft Edge](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/push)

## 410 (Gone) 및 유효하지 않은 웹 푸시 엔드포인트 {#410-gone-and-invalid-web-push-endpoints}

브라우저와 푸시 서비스는 웹 푸시 구독이 더 이상 수락되지 않을 때 **410 Gone**(또는 유사한 "엔드포인트가 유효하지 않음" 오류)을 반환할 수 있습니다. 일반적인 원인은 다음과 같습니다:

- 사용자가 브라우저 또는 OS 설정에서 사이트에 대한 알림을 비활성화한 경우.
- 동일한 브라우저 프로필에서 다른 사용자 프로필이 구독하여 엔드포인트가 새 가입자로 교체된 경우.
- 오랜 기간 참여 없이 구독이 만료된 경우—사용자가 다시 옵트인하면 다음 세션에서 새로운 구독이 생성됩니다.

사용자가 알림을 다시 활성화한 후, 사이트의 일반적인 웹 푸시 등록 흐름을 다시 트리거하여 Braze가 새 구독 엔드포인트를 저장하도록 합니다.