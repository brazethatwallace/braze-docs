---
nav_title: 채널
article_title: 채널
page_order: 5
layout: dev_guide
guide_top_header: "채널"
guide_top_text: "적절한 시간에 적절한 채널을 통해 사용자에게 도달하세요. 인앱 메시지, Content Cards, 배너와 같은 제품 내 채널이나 푸시, 이메일, SMS, WhatsApp과 같은 제품 외 채널 중에서 선택하세요."

page_type: landing
description: "Braze의 제품 내 및 제품 외 메시징 채널을 통해 사용자에게 도달하세요."

guide_featured_title: "제품 내 채널"
guide_featured_list:
  - name: 인앱 메시지
    link: /docs/user_guide/channels/in_app_messages
    image: /assets/img/braze_icons/phone-02.svg
  - name: Content Cards
    link: /docs/user_guide/channels/content_cards
    image: /assets/img/braze_icons/sticker-square.svg
  - name: 배너
    link: /docs/user_guide/channels/banners
    image: /assets/img/braze_icons/layout-top.svg

guide_menu_title: "제품 외 채널"
guide_menu_list:
  - name: 이메일
    link: /docs/user_guide/channels/email
    image: /assets/img/braze_icons/mail-01.svg
  - name: 트랜잭션 이메일
    link: /docs/user_guide/channels/transactional_email
    image: /assets/img/braze_icons/bank-note-02.svg
  - name: 랜딩 페이지
    link: /docs/user_guide/messaging/landing_pages
    image: /assets/img/braze_icons/file-02.svg
  - name: LINE
    link: /docs/user_guide/channels/line
    image: /assets/img/braze_icons/message-chat-circle.svg
  - name: 라이브 알림
    link: /docs/developer_guide/live_notifications
    image: /assets/img/braze_icons/phone-02.svg
  - name: 푸시
    link: /docs/user_guide/channels/push
    image: /assets/img/braze_icons/marker-pin-05.svg
  - name: "SMS, MMS, RCS"
    link: /docs/user_guide/channels/sms_mms_and_rcs
    image: /assets/img/braze_icons/message-text-circle-01.svg
  - name: 웹훅
    link: /docs/user_guide/channels/webhooks
    image: /assets/img/braze_icons/brackets.svg
  - name: WhatsApp
    link: /docs/user_guide/channels/whatsapp
    image: /assets/img/braze_icons/whatsapp.svg
---

## 메시지 채널 선택하기 {#choosing-a-message-channel}

Campaigns와 Canvases에 가장 적합한 메시지 채널을 결정할 때는 항상 메시지의 콘텐츠와 긴급성을 고려하세요.

- **콘텐츠**는 메시지가 시각적으로 얼마나 매력적인지를 나타냅니다. 멀티미디어 및 기타 자산을 추가하여 콘텐츠를 더욱 풍부하게 만들 수 있습니다.
- **긴급성**은 메시지가 사용자에게 얼마나 빠르게 알림을 전달하고 주의를 끌 수 있는지를 나타내는 척도입니다. 사용자가 즉시 확인할 수 있는 알림은 긴급성이 높고, 사용자가 앱에 로그인해야 확인할 수 있는 메시지는 긴급성이 낮습니다.

Braze 메시징 매트릭스는 **콘텐츠 복잡도**와 **전달 긴급성**을 매핑하여 채널 선택을 간소화합니다. 이 두 가지 요소의 균형을 맞추면 메시지가 방해가 아닌 공감을 이끌어낼 수 있습니다.

![모바일/웹 푸시는 단순한 콘텐츠, 높은 긴급성; 이메일은 풍부한 콘텐츠, 높은 긴급성; 인앱/브라우저 메시지는 단순한 콘텐츠, 낮은 긴급성; Content Cards는 낮은 긴급성, 풍부한 콘텐츠]({% image_buster /assets/img_archive/messaging_matrix.png %})

이 매트릭스는 핵심 채널을 강조하지만 유연하게 적용할 수 있습니다. 예를 들어 SMS와 WhatsApp은 높은 긴급성의 도구이면서 멀티미디어 형식을 활용하면 풍부한 콘텐츠로 확장할 수 있습니다. 이 매트릭스를 활용하는 방법에 대해 자세히 알아보려면 [크로스채널 메시징](https://learning.braze.com/cross-channel-messaging)에 대한 Braze 학습 과정을 확인하세요.

## 접근성 리소스 {#accessibility-resources}

Braze를 사용하여 각 채널에서 접근성 높은 메시징 캠페인을 만들 수 있습니다. 엔지니어와 협력하여 구현 시 접근성 표준을 충족하는지 확인하세요. 추가 가이드가 필요하다면 다음을 권장합니다:

- [접근성 높은 메시징 기초](https://learning.braze.com/accessible-messaging-foundations): 이 Braze 학습 과정에서 브랜드 커뮤니케이션에 적용되는 기본적인 접근성 원칙을 배울 수 있습니다.
- [접근성 높은 메시지 구축하기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility): Braze 내에서 직접 대체 텍스트를 추가하고 보조 기술을 위한 콘텐츠를 구조화하는 방법을 알아보세요.

Braze의 접근성 또는 Braze에서 발송된 메시지에 대한 피드백이 있으시면 언제든지 알려주세요. 글로벌 헤더의 **고객지원** 메뉴를 열고 **피드백 공유**를 선택하여 의견을 보내주세요.