---
nav_title: Apple MPP
article_title: iOS 15용 Apple 메일 개인정보 보호
page_order: 1
description: "이 참조 문서에서는 Apple 메일 개인정보 보호 업데이트와 이 업데이트의 영향을 받는 대상, 그리고 이 기능에 대비하기 위한 몇 가지 다음 단계에 대해 설명합니다."
channel:
  - email

---

# Apple의 메일 개인정보 보호 {#apples-mail-privacy-protection}

> 이 문서에서는 Apple의 메일 개인정보 보호(MPP), 영향을 받는 대상, 그리고 이메일 전달 가능성 측정기준에 미치는 영향에 대비하는 방법을 다룹니다.

## Apple의 메일 개인정보 보호 업데이트란 무엇인가요? {#what-is-apples-mail-privacy-protection-update}

Apple의 메일 개인정보 보호(MPP)는 2021년 9월 중순에 출시된 iOS 15, iPadOS 15, macOS Monterey 및 watchOS 8의 Apple Mail 앱 사용자가 사용할 수 있는 개인정보 보호 업데이트입니다. MPP에 옵트인하는 사용자(대부분의 사용자가 그렇게 할 것으로 예상)의 경우, 이메일이 프록시 서버를 통해 미리 로드되고 이미지가 캐싱되어 [열람 추적]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#update-the-placement)과 같은 측정기준에 추적 픽셀을 활용하는 기능이 제한됩니다.

브랜드는 MPP로 인해 이메일 전달 가능성 측정기준과 관련된 문제, 그리고 이러한 측정기준을 기반으로 트리거되는 기존 Campaign 및 Canvases에 문제가 발생할 수 있음을 예상해야 합니다. 이메일 전달 가능성에 미치는 영향을 이해하려면 [이메일 보고]({{site.baseurl}}/user_guide/channels/email/reporting)를 참조하세요.

### 누구에게 영향을 미치나요? {#who-will-this-affect}

다음 기기에서 기본 Apple Mail 앱을 사용하는 모든 수신자가 해당됩니다:

- iOS 15
- iPadOS 15
- macOS Monterey
- watchOS 8

이는 이메일 서비스(Gmail, Outlook, Yahoo, AOL 등)에 관계없이 Apple Mail 앱에 메일 계정을 연결하고 보안 기능을 사용하도록 설정한 모든 사용자에게 적용됩니다. 이 영향은 Apple/iCloud/me.com 이메일 주소로 메일을 수신하는 구독자에게만 국한되지 않습니다.

{% alert important %}
이러한 이메일 전달 가능성에 대한 업데이트는 중요하지만, MPP가 이메일과 전달 가능성에 적용되는 규칙을 근본적으로 변경하지는 않습니다. 대신, 성공을 벤치마킹하는 방법과 앞으로 사용할 수 있는 이메일 도구 및 기능에 영향을 미칠 것입니다.
{% endalert %}

## MPP에 대비하는 방법 {#how-to-prepare-for-mpp}

이제 막 MPP에 대응하는 방법과 이메일 마케팅 및 전반적인 고객 참여 활동에 미치는 잠재적 영향에 대해 고민하기 시작한 브랜드에게는 시간이 매우 중요합니다. 다음 사항을 수행하는 것을 권장합니다:

- MPP가 마케팅 활동에 미치는 위험을 평가하세요
- Braze 플랫폼의 자동화 조정을 다루고, 전달 가능성 모범 사례를 강화하며, 성능을 측정하기 위한 광범위한 측정기준을 개발하는 MPP 대응 계획을 수립하세요
- 가능한 한 빨리 해당 대응 계획을 실행하세요

Apple의 메일 개인정보 보호에 대비하는 방법에 대한 자세한 개요는 [블로그 게시물](https://www.braze.com/resources/articles/apple-mail-privacy-protection-how-to-prepare)을 확인하세요.