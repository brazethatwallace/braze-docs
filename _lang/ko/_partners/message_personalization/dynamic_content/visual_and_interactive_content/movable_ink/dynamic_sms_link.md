---
nav_title: 동적 단문 메시지 서비스 링크 미리보기
article_title: 동적 단문 메시지 서비스 링크 미리보기
description: "이 참조 문서에서는 Movable Ink의 단문 메시지 서비스 링크 미리보기 기능을 활성화하고 사용하는 방법을 설명합니다."
page_type: partner
search_tag: Partner
---

# 동적 단문 메시지 서비스 링크 미리보기 {#dynamic-sms-link-preview}

> Movable Ink의 동적 단문 메시지 서비스 링크 미리보기를 사용하면 단문 메시지 서비스와 동일한 비용으로 MMS의 몰입감을 활용할 수 있습니다. 이를 통해 Braze와 Movable Ink를 사용하여 비용 효율적이고 개인화된 리치 메시징 경험을 제공할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| Movable Ink 계정 | 이 파트너십을 활용하려면 Movable Ink 계정이 필요합니다. |
| 데이터 소스 | Movable Ink에 데이터 소스를 연결해야 합니다. CSV, 웹사이트 가져오기 또는 API를 통해 연결할 수 있습니다. |
| MMS 발송 기능 | Braze를 통해 MMS가 설정되어 있는지 확인합니다.
| [링크 단축]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening) | 링크 단축이 활성화되어 있는지 확인합니다. |
| 연락처 카드 | 링크 미리보기가 iOS에서 작동하려면 사용자의 휴대폰에 브랜드(발신자)가 연락처로 저장되어 있어야 합니다. 연락처 카드 또는 다른 방법을 통해 저장할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

이 섹션의 각 단계에 따라 iOS 및 Android 운영 체제에서 동적 단문 메시지 서비스 링크를 발송합니다.

### iOS

{% alert important %}
iOS에서 링크 미리보기 이미지를 허용하려면 사용자가 브랜드(발신자)를 연락처로 추가해야 합니다.
{% endalert %}

#### 1단계: 연락처 카드 Campaign 생성 {#step-1-create-a-contact-card-campaign}

사용자가 [연락처 카드]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card) 또는 다른 방법을 통해 브랜드를 연락처로 저장하면 **Tap to Load Preview** 프롬프트와 Movable Ink 링크를 볼 수 있습니다.

![1]{: style="max-width:30%;"}

#### 2단계: Movable Ink 링크 발송 {#step-2-send-movable-ink-links}

1. Movable Ink에서 단문 메시지 서비스 Campaign을 생성하고 클릭률 URL을 생성합니다.
2. Braze 대시보드에서 **Campaigns**로 이동하여 **캠페인 만들기** 드롭다운에서 새 단문 메시지 서비스/MMS Campaign을 설정합니다.
3. 단문 메시지 서비스 Campaign 작성기에서:
    - 구독 그룹을 설정합니다.
    - 메시지를 입력합니다.
    - 메시지 본문의 다른 모든 텍스트 뒤에 Movable Ink 링크를 **마지막으로** 추가합니다. <br><br>![2]{: style="max-width:50%;"}

{% alert tip %}
Liquid 개인화에 대한 내용은 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid)를 참조하세요.
{% endalert %}

{: start="4"}
4. 동적 단문 메시지 서비스 링크 미리보기 Campaign을 테스트하고 시작할 준비가 완료되었습니다.

![3]{: style="max-width:70%;"}

사용자가 링크 미리보기를 로드하면 개인화된 이미지가 렌더링되며, 웹사이트, 앱 또는 랜딩 페이지로 연결할 수 있습니다.

![4]{: style="max-width:30%;"}

### Android (Google 및 Samsung 기기) {#android-google-and-samsung-devices}

Android 사용자는 동적 단문 메시지 서비스 링크 미리보기를 수신하기 위해 브랜드를 연락처로 저장할 필요가 없습니다. 그러나 기기가 링크 미리보기를 자동으로 로드할 수 있도록 저장하는 것을 권장합니다.

![5]{: style="max-width:30%;"}

브랜드를 연락처로 저장하지 않았고 자동 미리보기를 활성화한 사용자는 미리보기 이미지를 로드하기 위해 **Tap to load preview**를 선택해야 합니다.

![6]{: style="max-width:30%;"}

## 고려 사항 {#considerations}

- 메시지에 미리보기 링크를 하나만 포함하세요. 단문 메시지 서비스 본문에 여러 링크가 있으면 콘텐츠가 생성되지 않습니다.
- 미리보기 링크 뒤에 문자를 추가하지 마세요. 추가하면 경험이 중단될 수 있습니다.


[1]: {% image_buster /assets/img/movable_ink/ios_link.png %}
[2]: {% image_buster /assets/img/movable_ink/ios_message.png %}
[3]: {% image_buster /assets/img/movable_ink/ios_test_launch.png %}
[4]: {% image_buster /assets/img/movable_ink/ios_example.png %}
[5]: {% image_buster /assets/img/movable_ink/android_automatic.png %}
[6]: {% image_buster /assets/img/movable_ink/android_tap.png %}