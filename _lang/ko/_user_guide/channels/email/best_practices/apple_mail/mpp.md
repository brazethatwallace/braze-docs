---
nav_title: Apple Mail 개인정보 보호
article_title: iOS 15용 Apple Mail 개인정보 보호
page_order: 1
description: "이 참조 문서에서는 Apple Mail 개인정보 보호 업데이트, 영향을 받는 대상, 그리고 이 기능에 대비하기 위한 다음 단계를 다룹니다."
channel:
  - email

---

# Apple Mail 개인정보 보호

> 이 문서에서는 Apple의 MPP(Mail Privacy Protection), 영향을 받는 대상, 그리고 이메일 전달 가능성 측정기준에 미치는 영향에 대비하는 방법을 다룹니다.

## Apple의 Mail Privacy Protection 업데이트란 무엇인가요?

Apple의 MPP(Mail Privacy Protection)는 2021년 9월 중순에 출시된 iOS 15, iPadOS 15, macOS Monterey, watchOS 8의 Apple Mail 앱 사용자에게 제공되는 개인정보 보호 업데이트입니다. MPP에 옵트인한 사용자(대부분의 사용자가 옵트인할 것으로 예상됨)의 경우, 이메일이 프록시 서버를 통해 미리 로드되고 이미지가 캐싱되어 [오픈 추적]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/#changing-location-of-tracking-pixel)과 같은 측정기준에 추적 픽셀을 활용하는 기능이 제한됩니다.

브랜드는 MPP로 인해 이메일 전달 가능성 측정기준과 관련된 문제, 그리고 이러한 측정기준을 기반으로 트리거되는 기존 캠페인 및 캔버스에 문제가 발생할 수 있음을 예상해야 합니다. 이메일 전달 가능성에 미치는 영향을 이해하려면 [이메일 보고]({{site.baseurl}}/user_guide/channels/email/reporting/)를 참조하세요.

### 영향을 받는 대상은 누구인가요?

다음 기기에서 기본 Apple Mail 앱을 사용하는 모든 수신자가 해당됩니다:

- iOS 15
- iPadOS 15
- macOS Monterey
- watchOS 8

이는 이메일 서비스(Gmail, Outlook, Yahoo, AOL 등)에 관계없이 Apple Mail 앱에 메일 계정을 연결하고 보안 기능에 옵트인한 모든 사용자에게 적용됩니다. 이 영향은 Apple/iCloud/me.com 이메일 주소로 메일을 수신하는 가입자에게만 국한되지 않습니다.

{% alert important %}
이러한 이메일 전달 가능성 업데이트는 중요하지만, MPP가 이메일과 전달 가능성을 관리하는 기본 규칙을 근본적으로 변경하는 것은 아닙니다. 대신, 성공을 측정하는 기준과 앞으로 사용할 수 있는 이메일 도구 및 기능에 영향을 미칩니다.
{% endalert %}

## MPP에 어떻게 대비해야 하나요?

MPP와 이메일 마케팅 및 전반적인 고객 참여 활동에 미칠 잠재적 영향에 대한 대응을 이제 막 고려하기 시작한 브랜드에게는 시간이 매우 중요합니다. 다음 사항을 권장합니다:

- MPP가 마케팅 활동에 미치는 위험을 평가하세요
- Braze 플랫폼에서의 자동화 조정, 전달 가능성 모범 사례 강화, 성과를 측정하기 위한 보다 광범위한 측정기준 개발을 포함하는 MPP 대응 계획을 수립하세요
- 가능한 한 빨리 해당 대응 계획을 실행하세요

Apple의 Mail Privacy Protection에 대비하는 방법에 대한 자세한 개요는 [블로그 게시물](https://www.braze.com/resources/articles/apple-mail-privacy-protection-how-to-prepare)을 확인하세요.