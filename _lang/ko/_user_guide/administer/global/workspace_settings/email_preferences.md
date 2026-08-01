---
nav_title: 이메일 환경설정
article_title: 이메일 환경설정
page_type: reference
page_order: 2
description: "이 참조 문서에서는 발송 구성, 열람 추적 픽셀, 가입 페이지 및 바닥글 등 Braze 대시보드의 이메일 환경설정에 대해 다룹니다."
tool: Dashboard
channel: email
alias: /email_preferences/
toc_headers: h2

---

# 이메일 환경설정 {#email-preferences}

> 이메일 환경설정은 커스텀 바닥글, 커스텀 옵트인 및 옵트아웃 페이지 등 특정 발신 이메일 설정을 구성하는 곳입니다. 이러한 옵션을 발신 이메일에 포함하면 사용자에게 매끄럽고 일관된 경험을 제공할 수 있습니다.

**이메일 환경설정**은 대시보드의 **설정**에서 찾을 수 있습니다.

## 발송 구성 {#sending-configuration}

**발송 구성** 섹션의 이메일 설정은 이메일 Campaign에 포함되는 세부 정보를 결정합니다. 특히 이 설정은 사용자가 Braze에서 보낸 이메일을 수신할 때 표시되는 내용과 주로 관련됩니다.

### 발신 이메일 설정 {#outbound-email-settings}

이메일 설정을 구성할 때, 발신 이메일 설정은 Braze가 사용자에게 이메일을 보낼 때 사용되는 이름과 이메일 주소를 식별합니다.

워크스페이스에 새 도메인이나 IP 풀(발송 공급자)을 추가하거나 사용 가능한 목록에서 제거해야 하는 경우, 고객 성공 매니저에게 문의하세요.

{% tabs local %}
{% tab 표시 이름 주소 %}

이 섹션에서는 Braze가 사용자에게 이메일을 보낼 때 사용할 수 있는 이름과 이메일 주소를 추가할 수 있습니다. 표시 이름과 이메일 주소는 이메일 Campaign을 작성할 때 **발송 정보** 옵션에서 사용할 수 있습니다. 발신 이메일 설정에 대한 업데이트는 기존 발송에 소급 적용되지 않습니다.

![다양한 표시 이름과 도메인 필드가 있는 발신 이메일 설정 섹션.]({% image_buster /assets/img/email_settings/display_name_address.png %})

{% alert note %}
Apple Mail 클라이언트는 커스텀 표시 이름에 `@` 기호가 사용된 경우 이를 인식하지 못합니다. 메일함 공급자마다 사용자에게 표시 이름 주소를 표시하는 방식이 다르므로, 이메일 클라이언트에 따라 표시 이름이 다르게 나타날 수 있습니다.
{% endalert %}

#### Liquid으로 개인화 {#personalize-with-liquid}

**발신 표시 이름**, **로컬 파트**, **도메인** 필드에서 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)을 사용하여 커스텀 속성을 기반으로 발신자 이름과 이메일 주소를 동적으로 템플릿화할 수도 있습니다. **도메인** 필드에서 Liquid을 사용하려면 이메일 Campaign의 **발송 정보** 옵션으로 이동하여 **발신 표시 이름 + 주소 커스터마이즈** 체크박스를 선택해야 합니다.

![발신 표시 이름, 주소, 도메인을 커스터마이즈하기 위한 필드가 있는 발송 설정.]({% image_buster /assets/img/email_settings/email_campaign_domain.png %})

예를 들어, 조건 로직을 사용하여 다른 브랜드나 지역에서 발송할 수 있습니다:

{% raw %}
```liquid
{% if ${language} == 'en' %}
English Display Name
{% elsif ${language} == 'de' %}
German Display Name
{% else %}
Default to English Display Name
{% endif %}
```
{% endraw %}

{% endtab %}
{% tab 회신 주소 %}

이 섹션에서 이메일 주소를 추가하면 이메일 Campaign의 회신 주소로 선택할 수 있습니다. **기본값으로 설정**을 선택하여 이메일 주소를 기본 주소로 설정할 수도 있습니다. 이러한 이메일 주소는 이메일 Campaign을 작성할 때 **발송 정보** 옵션에서 사용할 수 있습니다.

![여러 회신 주소를 입력할 수 있는 필드가 있는 회신 주소 섹션.]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

{% alert note %}
Braze 발송 도메인은 수신 이메일을 수락하지 않습니다. 수신자가 Braze에서 구성한 발송 도메인으로 보낸 이메일에 회신하면, `550 5.7.1 relaying denied` 오류와 함께 회신이 반송됩니다. 회신 주소는 발신 주소와 동일한 도메인을 공유할 필요가 없습니다. 회신을 수신해야 하는 경우(예: 캘린더 초대 확인 수집), 발송용으로 구성되지 않았으며 메일을 수신할 수 있는 받은편지함이 설정된 하위 도메인을 사용하세요.
{% endalert %}

#### Liquid으로 개인화

**회신 주소** 필드에서 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)을 사용하여 커스텀 속성을 기반으로 회신 주소를 동적으로 템플릿화할 수도 있습니다. 예를 들어, 조건 로직을 사용하여 다른 지역이나 부서로 회신을 보낼 수 있습니다:

{% raw %}
```liquid
{% if {{custom_attribute.${region}}} == 'US' %}
{% assign address = "us-support@example.com" %}
{% elsif {{custom_attribute.${region}}} == 'EU' %}
{% assign address = "eu-support@example.com" %}
{% else %}
{% assign address = "global-support@example.com" %}{% endif %}{{address}}
```
{% endraw %}

{% endtab %}
{% tab BCC 주소 %}

이 섹션에서는 Braze에서 발송되는 아웃바운드 이메일 메시지에 추가할 수 있는 BCC 주소를 관리할 수 있습니다. 이메일 메시지에 BCC 주소를 추가하면 사용자가 수신하는 메시지의 동일한 사본이 BCC 받은편지함으로 전송됩니다. 이는 규정 준수 요구 사항이나 고객 지원 문제를 위해 사용자에게 보낸 메시지의 사본을 보관하는 데 유용한 도구입니다. BCC 이메일은 이메일 보고 및 분석에 포함되지 않습니다.

BCC 주소는 Amazon SES, SendGrid, SparkPost에서 사용할 수 있습니다. BCC 주소의 대안으로, 보관 또는 규정 준수 목적으로 사용자에게 보낸 메시지의 사본을 저장하려면 [메시지 아카이빙]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/message_archiving)을 사용하는 것을 권장합니다.

{% multi_lang_include alerts/important_alerts.md alert='BCC address billable emails' %}

주소를 추가하면 Campaign 또는 캔버스 단계에서 이메일을 작성할 때 해당 주소를 선택할 수 있습니다. 주소 옆의 **기본값으로 설정**을 선택하면 새 이메일 Campaign 또는 Canvas 구성 요소를 시작할 때 기본적으로 이 주소가 선택됩니다. 메시지 수준에서 이를 재정의하려면 메시지를 설정할 때 **BCC 없음**을 선택하면 됩니다.

Braze에서 발송되는 모든 이메일 메시지에 BCC 주소를 포함해야 하는 경우, **모든 이메일 Campaign에 BCC 주소 필수** 토글을 선택할 수 있습니다. 이 경우 기본 주소를 선택해야 하며, 새 이메일 Campaign 또는 캔버스 단계에서 자동으로 선택됩니다. 기본 주소는 REST API를 통해 트리거되는 모든 메시지에도 자동으로 추가됩니다. 주소를 포함하기 위해 기존 API 요청을 변경할 필요는 없습니다.

#### 동적 BCC {#dynamic-bcc}

동적 BCC를 사용하면 BCC 주소에 Liquid을 사용할 수 있습니다. 이 기능은 **이메일 환경설정**에서만 사용할 수 있으며 Campaign 자체에서는 설정할 수 없습니다. 이메일 수신자당 하나의 BCC 주소만 허용됩니다.

예를 들어, 지원팀의 이메일에 대한 BCC 주소로 {% raw %}`{{custom_attribute.${support_agent}}}`{% endraw %}를 추가할 수 있습니다.

![Liquid을 사용하는 BCC 주소가 있는 이메일 설정 탭의 BCC 주소 섹션.]({% image_buster /assets/img/email_settings/dynamic_bcc.png %}){: style="max-width:90%;" }

{% endtab %}
{% endtabs %}

## 열람 추적 픽셀 {#open-tracking-pixel}

[![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

이메일 열람 추적 픽셀은 보이지 않는 1 x 1&nbsp;px 이미지로, 이메일 HTML에 자동으로 삽입됩니다. 이 픽셀은 Braze가 사용자가 이메일을 열었는지 감지하는 데 도움을 줍니다. 사용자의 이메일 클라이언트가 추적 픽셀에 요청을 보내면, 해당 요청에는 IP 주소, 사용자 에이전트, 타임스탬프 등의 정보가 포함될 수 있습니다. 이메일 열람 정보는 해당 열람율을 파악하여 효과적인 마케팅 전략을 결정하는 데 매우 유용합니다.

### 배치 {#placement}

Braze의 기본 동작은 이메일 하단, 일반적으로 `<body>` 태그 안에 추적 픽셀을 추가하는 것입니다. 대부분의 사용자에게 이 위치가 픽셀을 배치하기에 가장 이상적인 곳입니다.

픽셀은 이미 시각적 변화를 최소화하도록 스타일이 적용되어 있지만, 의도하지 않은 시각적 변화가 발생하더라도 이메일 하단에서 가장 눈에 띄지 않습니다. 이는 SendGrid 및 SparkPost와 같은 이메일 공급자의 기본 설정이기도 합니다.

예기치 않은 동작을 줄이려면 Liquid를 `<html>` 태그 안에 유지하세요. 중첩되거나 중복된 문서 수준 태그는 이메일이 파싱되는 방식과 픽셀이 배치되는 위치를 변경하여 열람 추적 및 레이아웃에 영향을 줄 수 있습니다. 자세한 내용은 [Liquid 사용하기]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid)를 참조하세요.

### 배치 업데이트 {#update-the-placement}

Braze는 현재 ESP의 기본 열람 추적 픽셀 위치(이메일 `<body>`의 마지막 태그)를 `<body>`의 첫 번째 태그로 이동하도록 재정의하는 기능을 지원합니다.

![SendGrid, SparkPost 또는 Amazon SES에 대한 이동 옵션이 있는 열람 추적 픽셀 섹션]({% image_buster /assets/img/open_pixel.png %}){: style="max-width:80%;" }

위치를 변경하려면:

1. Braze에서 **설정** > **이메일 환경설정**으로 이동합니다.
2. 다음 옵션 중 하나를 선택합니다: **Move for SendGrid**, **Move for SparkPost** 또는 **Move for Amazon SES**
3. **저장**을 선택합니다.

저장하면 Braze가 ESP에 특별한 지침을 전송하여 모든 HTML 이메일의 상단에 열람 추적 픽셀을 배치합니다.

{% alert important %}
SSL을 활성화하면 추적 픽셀의 URL이 HTTP 대신 HTTPS로 래핑됩니다. SSL이 잘못 구성된 경우 추적 픽셀의 효과에 영향을 줄 수 있습니다.
{% endalert %}

{% alert important %}
클릭 추적은 `http://` 또는 `https://`로 시작하는 링크에만 적용됩니다. `mailto:` 링크(예: `mailto:support@example.com`)는 추적을 위해 재작성되지 않습니다.
{% endalert %}

## 목록 탈퇴 헤더 {#list-unsubscribe}

{% alert note %}
2026년 6월 15일부터 원클릭 목록 탈퇴 헤더가 특정 구독 그룹으로 범위가 지정되도록 구성된 경우, Braze는 더 이상 이메일에 mailto 헤더를 포함하지 않습니다. 목록 탈퇴 헤더를 통해 탈퇴하는 사용자는 전체가 아닌 해당 특정 구독 그룹에서만 탈퇴됩니다.
{% endalert %}

목록 탈퇴 헤더를 사용하면 수신자가 메시지 본문이 아닌 메일함 UI 내에 **Unsubscribe** 버튼을 표시하여 마케팅 이메일에서 쉽게 탈퇴할 수 있습니다.

테스트 발송에는 일반적으로 목록 탈퇴 헤더가 포함되지 않습니다. 실제 헤더가 표시되는지 여부는 메일함 공급자에 따라 다르며 평판 기반입니다. 발송자 평판이 높을수록 일반적으로 가시성이 향상됩니다.

![메시지 본문 외부에 목록 탈퇴가 표시되는 이메일 클라이언트 메일함 UI에서 메시지 옆에 Unsubscribe 옵션이 있는 화면.]({% image_buster /assets/img_archive/list_unsub_img1.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

수신자가 **Unsubscribe**를 선택하면 메일함 공급자가 이메일 헤더에 정의된 대상으로 탈퇴 요청을 보냅니다.

목록 탈퇴를 활성화하는 것은 전달 가능성 모범 사례이며 주요 메일함 공급자의 요구 사항입니다. 이는 최종사용자가 이메일 클라이언트에서 스팸 버튼을 누르는 대신 원치 않는 메시지에서 안전하게 자신을 제거하도록 권장하며, 후자는 발송자 평판과 이메일 전달 가능성에 해롭습니다.

[Gmail에서 구독을 관리](https://support.google.com/mail/answer/15621070?sjid=2292320204527911296-NC)할 때, Gmail은 메시지 본문에서 탈퇴 링크를 가져올 수도 있지만, 헤더에 목록 탈퇴가 있는 경우 이를 우선시합니다.

### 목록 탈퇴 헤더를 끄면 Gmail의 탈퇴 버튼이 제거되나요? {#does-turning-off-the-list-unsubscribe-header-remove-the-gmail-unsubscribe-button}

아니요. Braze 목록 탈퇴 헤더 설정을 끄면 Braze가 보내는 메시지에서 `List-Unsubscribe` 헤더가 제거되지만, Gmail이 메일함 UI에 **Unsubscribe** 옵션을 표시하는지 여부는 제어하지 않습니다. 이전 섹션에서 언급한 바와 같이, Gmail은 메시지 본문의 링크에서 탈퇴 옵션을 표시하거나 다른 공급자 로직을 사용할 수 있습니다. 원본 메시지에 헤더가 나타나는지 여부는 Gmail이 수신자에게 탈퇴 옵션을 표시하는지 여부와 별개입니다. 자세한 내용은 [Gmail 이메일 발신자 가이드라인 FAQ](https://support.google.com/a/answer/14229414)를 참조하세요.

### 메일함 공급자 지원 {#mailbox-provider-support}

다음 표는 "mailto:" 헤더, 목록 탈퇴 URL, 원클릭 탈퇴([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058))에 대한 메일함 공급자 지원을 요약합니다.

| 목록 탈퇴 헤더 | Mailto: 헤더 | 목록 탈퇴 URL | 원클릭 탈퇴 (RFC 8058) |
| ----- | --- | --- | --- |
| Gmail | 지원됨* | 지원됨 | 지원됨 |
| Gmail 모바일 | 지원되지 않음 | 지원되지 않음 | 지원되지 않음 |
| Apple Mail | 지원됨 | 지원되지 않음 | 지원되지 않음 |
| Outlook.com | 지원됨 | 지원되지 않음 | 지원되지 않음 |
| Yahoo! Mail | 지원됨* | 지원되지 않음 | 지원됨 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="메일함 공급자 지원" }

_*Yahoo와 Gmail은 결국 "mailto:" 헤더를 지원 중단하고 원클릭만 지원할 예정입니다._

헤더 표시 여부는 궁극적으로 메일함 공급자가 결정합니다. Gmail에서 수신자의 원본(텍스트) 이메일에 목록 탈퇴 헤더가 포함되어 있는지 확인하려면 다음을 수행하세요:

1. 이메일에서 **Show Original**을 선택합니다. 이메일의 원본 버전과 헤더가 포함된 새 탭이 열립니다.
2. "List-Unsubscribe"를 검색합니다. 원클릭 탈퇴의 경우, 많은 공급자가 "List-Unsubscribe-Post" 헤더도 포함합니다. 원클릭이 사용 가능할 것으로 예상되는 경우 원본 메시지에 두 헤더가 모두 나타나는지 확인하세요.

헤더가 이메일의 원본 버전에 있지만 표시되지 않는 경우, 메일함 공급자가 탈퇴 옵션을 표시하지 않기로 결정한 것이며, 메일함 공급자가 헤더를 표시하지 않는 이유에 대한 추가 인사이트는 없습니다. 목록 탈퇴 헤더의 표시는 궁극적으로 평판 기반입니다. 대부분의 경우 메일함 공급자에 대한 발송자 평판이 좋을수록 목록 탈퇴 헤더가 나타날 가능성이 높습니다.

### 워크스페이스의 이메일 탈퇴 헤더 {#email-unsubscribe-header-in-workspaces}

![발송 대상으로 가입했거나 옵트인한 사용자를 선택하는 화면.]({% image_buster /assets/img/email_settings/email_unsub_header_workspaces.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

이메일 탈퇴 헤더 기능이 켜져 있으면 이 설정은 회사 수준이 아닌 전체 워크스페이스에 적용됩니다. Campaign 및 Canvas 빌더의 **타겟 오디언스** 단계에서 가입했거나 옵트인한 사용자, 또는 옵트인한 사용자에게 발송하도록 설정된 Campaigns 및 Canvases에 추가됩니다.

"워크스페이스 기본값"을 사용할 때, Braze는 트랜잭션으로 간주되는 Campaign, 즉 "탈퇴한 사용자를 포함한 모든 사용자에게 발송"으로 구성된 Campaign에는 원클릭 탈퇴 헤더를 추가하지 않습니다. 이를 재정의하고 탈퇴한 사용자에게 발송할 때 원클릭 탈퇴 헤더를 추가하려면 메시지 수준 원클릭 목록 탈퇴 설정에서 **Unsubscribe globally from all emails**를 선택할 수 있습니다.

### 기본 목록 탈퇴 헤더 {#default-list-unsubscribe-header}

{% alert important %}
Gmail은 2024년 6월 1일부터 모든 발신 상업 및 프로모션 메시지에 대해 발신자가 원클릭 탈퇴를 구현하도록 요구할 예정입니다. 자세한 내용은 [Gmail 발신자 가이드라인](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe) 및 [Gmail 이메일 발신자 가이드라인 FAQ](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages)를 참조하세요. Yahoo는 요구 사항 업데이트에 대해 2024년 초 일정을 발표했습니다. 자세한 내용은 [더 안전하고 스팸이 적은: 더 나은 경험을 위한 이메일 표준 시행](https://blog.postmaster.yahooinc.com/)을 참조하세요.
{% endalert %}

Braze 탈퇴 기능을 사용하여 탈퇴를 직접 처리하려면 **Include a one-click list-unsubscribe (mailto and HTTP) email header for emails sent to subscribed or opted-in users**를 선택하고 표준 Braze URL 및 mail-to로 **Braze default**를 선택합니다.

![가입했거나 옵트인한 사용자에게 보내는 이메일에 목록 탈퇴 헤더를 자동으로 포함하는 옵션.]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %})

Braze는 다음 버전의 목록 탈퇴 헤더를 지원합니다:

| 목록 탈퇴 버전 | 설명 |
| ----- | --- |
| 원클릭 (RFC 8058) | 수신자가 한 번의 클릭으로 이메일을 옵트아웃할 수 있는 간단한 방법을 제공합니다. 이는 대량 발신자에 대한 Yahoo 및 Gmail의 요구 사항입니다. |
| 목록 탈퇴 URL 또는 HTTPS | 수신자에게 탈퇴할 수 있는 웹 페이지로 이동하는 링크를 제공합니다. |
| Mailto | 탈퇴 요청 메시지가 수신자로부터 브랜드로 전송될 대상으로 이메일 주소를 지정합니다. <br><br> _mailto 목록 탈퇴 요청을 처리하려면, 해당 탈퇴 요청에 탈퇴하는 최종사용자에 대해 Braze에 저장된 이메일 주소가 포함되어야 합니다. 이는 최종사용자가 탈퇴하는 이메일의 "보낸 사람 주소", 인코딩된 제목, 또는 최종사용자가 수신한 이메일의 인코딩된 본문에서 제공될 수 있습니다. 매우 제한된 경우에 일부 받은편지함 공급자가 [RFC 2368](https://datatracker.ietf.org/doc/html/rfc2368) 프로토콜을 준수하지 않아 이메일 주소가 올바르게 전달되지 않을 수 있습니다. 이로 인해 Braze에서 탈퇴 요청을 처리할 수 없게 될 수 있습니다._ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="기본 목록 탈퇴 헤더" }

Braze가 [기본 목록 탈퇴 헤더](#default-list-unsubscribe-header) 방법 중 하나를 통해 사용자로부터 목록 탈퇴 요청을 수신하면, 이 사용자의 글로벌 이메일 구독 상태가 탈퇴로 설정됩니다. 일치하는 항목이 없으면 Braze는 이 요청을 처리하지 않습니다.

### 원클릭 탈퇴 {#one-click-unsubscribe}

목록 탈퇴 헤더에 원클릭 탈퇴([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058))를 사용하면 수신자가 이메일을 쉽게 옵트아웃할 수 있는 방법을 제공하는 데 중점을 둡니다.

### 메시지 수준 원클릭 목록 탈퇴 {#message-level-one-click-list-unsubscribe}

메시지 수준 원클릭 목록 탈퇴 설정은 워크스페이스에 설정된 이메일 탈퇴 헤더 기능을 재정의합니다. 다음 용도로 Campaign 또는 캔버스 단계별로 원클릭 탈퇴 동작을 적용합니다:

- 하나의 워크스페이스 내에서 여러 브랜드/목록을 지원하기 위해 특정 구독 그룹에 대한 Braze 원클릭 탈퇴 추가
- 기본 Braze 탈퇴 또는 커스텀 URL 간 전환
- 커스텀 원클릭 탈퇴 URL 추가
- 이 메시지에서 원클릭 탈퇴 생략

{% alert note %}
메시지 수준 원클릭 목록 탈퇴 설정은 드래그 앤 드롭 편집기와 업데이트된 HTML 편집기를 사용할 때만 사용할 수 있습니다. 이전 HTML 편집기를 사용하는 경우 이 기능을 사용하려면 업데이트된 HTML 편집기로 전환하세요.
{% endalert %}

이메일 편집기에서 **Sending Settings** > **Sending Info**로 이동합니다. 다음 옵션 중에서 선택합니다:

- **Use workspace default**: **이메일 환경설정**에 설정된 **Email Unsubscribe Header** 설정을 사용합니다. 이 설정에 대한 변경 사항은 모든 메시지에 적용됩니다.
- **Unsubscribe globally from all emails**: Braze 기본 원클릭 탈퇴 헤더를 사용합니다. 탈퇴 버튼을 클릭한 사용자의 글로벌 이메일 구독 상태가 "Unsubscribed"로 설정됩니다.
- **Unsubscribe from specific subscription group**: 지정된 구독 그룹을 사용합니다. Braze는 탈퇴 버튼을 클릭한 사용자를 선택한 구독 그룹에서 탈퇴시킵니다.
    - 구독 그룹을 선택할 때 **타겟 오디언스**에서 **구독 그룹** 필터를 추가하여 이 특정 그룹에 가입한 사용자만 타겟팅합니다. 원클릭 탈퇴에 선택한 구독 그룹은 타겟팅하는 구독 그룹과 일치해야 합니다. 구독 그룹이 일치하지 않으면 이미 탈퇴한 구독 그룹에서 탈퇴하려는 사용자에게 발송할 위험이 있습니다.

{% alert important %}
**Unsubscribe from specific subscription group** 설정은 원클릭 목록 탈퇴 헤더에만 적용됩니다. mailto 목록 탈퇴 헤더는 이 옵션을 선택해도 영향을 받지 않습니다. 즉, 이 방법을 사용하여 탈퇴하는 수신자는 특정 구독 그룹이 아닌 글로벌 탈퇴를 기록합니다. 이 설정을 선택할 때 mailto 목록 탈퇴 헤더가 사용자를 전체 탈퇴시키지 않도록 하려면 [고객지원]({{site.baseurl}}/support_contact)에 문의하세요.
{% endalert %}

- **Custom**: 탈퇴를 직접 처리할 수 있도록 커스텀 원클릭 탈퇴 URL을 추가합니다.
- **Exclude unsubscribe**

{% alert important %}
원클릭 탈퇴 또는 모든 탈퇴 메커니즘을 제외하는 것은 비밀번호 재설정, 영수증, 확인 이메일과 같은 트랜잭션 메시징에만 해당합니다.
{% endalert %}

이 설정을 조정하면 이 이메일의 원클릭 목록 탈퇴에 대한 기본 동작이 재정의됩니다.

![워크스페이스 기본값 및 커스텀 URL을 포함한 메시지 수준 원클릭 목록 탈퇴 옵션이 있는 이메일 편집기의 발송 설정.]({% image_buster /assets/img/email_settings/one_click_list_unsubscribe_message_level.png %}){: style="max-width:70%;"}

#### 요구 사항 {#requirements}

자체 커스텀 탈퇴 기능을 사용하여 이메일을 보내는 경우, 설정한 원클릭 탈퇴 URL이 RFC 8058을 준수하도록 다음 요구 사항을 충족해야 합니다:

* URL은 탈퇴 POST 요청을 처리할 수 있어야 합니다.
* URL은 `https://`로 시작해야 합니다.
* URL은 HTTPS 리디렉션이나 본문을 반환해서는 안 됩니다. 랜딩 페이지나 다른 유형의 웹 페이지로 이동하는 원클릭 탈퇴 링크는 RFC 8058을 준수하지 않습니다.
* POST 요청은 쿠키를 설정해서는 안 됩니다.

**Custom list-unsubscribe header**를 선택하여 자체 구성된 원클릭 탈퇴 엔드포인트와 선택적 "mailto:"를 추가합니다. Braze는 원클릭 탈퇴 HTTP가 대량 발신자에 대한 Yahoo 및 Gmail의 요구 사항이므로 커스텀 목록 탈퇴 헤더를 지원하기 위해 URL 입력이 필요합니다.

![원클릭 탈퇴 URL 및 선택적 mailto를 위한 커스텀 목록 탈퇴 헤더 필드가 있는 이메일 환경설정.]({% image_buster /assets/img/email_settings/email_unsubscribe_header_custom.png %}){: style="max-width:80%;"}

## 이메일 제목란에 접두사 추가 {#append-email-subject-lines}

토글을 사용하여 테스트 및 시드 이메일 제목란에 "[TEST]" 및 "[SEED]"를 포함할 수 있습니다. 이를 통해 테스트로 발송된 이메일 Campaign을 쉽게 식별할 수 있습니다.

![테스트 및 시드 이메일 제목란에 TEST와 SEED 접두사를 추가하는 워크스페이스 이메일 환경설정 토글.]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;"}

## 새 이메일에 대한 기본 인라인 CSS {#inline-css-on-new-emails-by-default}

CSS 인라이닝은 이메일 및 새 이메일의 CSS 스타일을 자동으로 인라인 처리하는 기술입니다. 일부 이메일 클라이언트에서는 이 기능을 통해 이메일 렌더링이 개선될 수 있습니다.

이 설정을 변경해도 기존 이메일 메시지나 템플릿에는 영향을 미치지 않습니다. 메시지나 템플릿을 작성하는 동안 언제든지 이 기본값을 재정의할 수 있습니다. 자세한 내용은 [CSS 인라이닝]({{site.baseurl}}/user_guide/channels/email/html_editor/css_inline)을 참조하세요.

## 이메일 변경 시 사용자 재구독 {#resubscribe-users-when-their-email-changes}

사용자가 이메일 주소를 변경할 때 자동으로 재구독되도록 설정할 수 있습니다. 예를 들어, 이전에 구독을 취소한 워크스페이스 사용자가 Braze의 구독 취소 목록에 없는 이메일 주소로 변경하면 자동으로 재구독됩니다.

![이메일 주소 변경 시 사용자를 자동으로 재구독하는 워크스페이스 설정.]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## 구독 페이지 및 푸터 {#subscription-pages-and-footers}

{% tabs local %}
{% tab 커스텀 푸터 %}

상업용 이메일의 경우, [CAN-SPAM법](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003)에 따라 모든 상업용 이메일에 구독 취소 옵션을 포함해야 합니다. 커스텀 푸터 설정을 사용하면 이메일 옵트아웃 푸터를 맞춤 설정하면서도 CAN-SPAM 규정을 준수할 수 있습니다. 규정을 준수하려면 이 워크스페이스의 Campaigns 일부로 발송되는 모든 이메일에 커스텀 푸터를 추가해야 합니다.

이메일 메시징용 커스텀 푸터를 만들 때 다음 요구 사항에 유의하세요:
- 구독 취소 URL과 실제 우편 주소를 포함해야 합니다.
- 100KB 미만이어야 합니다.

![CAN-SPAM 규정 준수를 위한 구독 취소 링크 및 우편 주소 필드가 포함된 커스텀 이메일 푸터 편집기.]({% image_buster /assets/img/email_settings/custom_footer.png %})

커스텀 푸터 Liquid 템플릿에 대한 자세한 내용은 [커스텀 푸터]({{site.baseurl}}/user_guide/channels/email/subscriptions#changing-email-subscriptions)를 참조하세요.

{% endtab %}
{% tab 커스텀 구독 취소 페이지 %}

Braze에서는 자체 HTML을 사용하여 **커스텀 구독 취소 페이지**를 설정할 수 있습니다. 이 페이지는 사용자가 이메일 하단에서 구독 취소를 선택한 후에 표시됩니다. 이 페이지는 750KB 미만이어야 합니다.

![사용자가 이메일 구독을 취소한 후 표시되는 페이지의 커스텀 구독 취소 페이지 HTML 편집기 및 미리보기.]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

{% multi_lang_include email/external_font_domains.md page_type='unsubscribe' %}

{% endtab %}
{% tab 커스텀 옵트인 페이지 %}

자체 HTML을 사용하여 커스텀 옵트인 페이지를 만들 수 있습니다. 이메일에 이 페이지를 포함하면 사용자 라이프사이클 전반에 걸쳐 브랜딩과 메시지의 일관성을 유지하는 데 특히 유용합니다. 이 페이지는 750KB 미만이어야 합니다.

![브랜드 이메일 구독 확인을 위한 커스텀 옵트인 페이지 HTML 편집기 및 미리보기.]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

{% multi_lang_include email/external_font_domains.md page_type='opt-in' %}

{% endtab %}
{% endtabs %}

{% alert tip %}
구독 페이지 또는 푸터의 **미리보기** 섹션에서 **미리보기 링크 복사**를 선택하면 임의의 사용자에게 이메일 푸터, 구독 취소 페이지 또는 옵트인 페이지가 어떻게 보이는지 확인할 수 있는 공유 가능한 미리보기 링크를 생성하고 복사할 수 있습니다. 자세한 내용은 [공유 가능한 미리보기]({{site.baseurl}}/user_guide/messaging/governance/shareable_preview)를 참조하세요.
{% endalert %}

## 자주 묻는 질문 {#frequently-asked-questions}

### 원클릭 수신 거부

{% details 원클릭 수신 거부 URL(list-unsubscribe 헤더를 통한)을 환경설정 센터에 연결할 수 있나요? %}
아니요, 이는 RFC 8058을 준수하지 않으므로 Yahoo 및 Gmail의 원클릭 수신 거부 요구 사항을 충족하지 못합니다.
{% enddetails %}

{% details 환경설정 센터를 작성할 때 "이메일 본문에 수신 거부 링크가 포함되어 있지 않습니다"라는 오류 메시지가 표시되는 이유는 무엇인가요? %}
환경설정 센터는 수신 거부 링크로 간주되지 않습니다. CAN-SPAM을 준수하려면 이메일 수신자에게 모든 상업용 이메일의 수신을 거부할 수 있는 옵션을 제공해야 합니다.
{% enddetails %}

{% details 원클릭 수신 거부 설정을 활성화한 후 이전 이메일 Campaigns 및 Canvases를 수정해야 하나요? %}
메시지 수준의 원클릭 list-unsubscribe 설정에 해당하는 사용 사례가 없다면, **이메일 환경설정**에서 설정이 켜져 있는 한 별도의 조치가 필요하지 않습니다. Braze는 모든 발신 마케팅 및 프로모션 메시지에 원클릭 수신 거부 헤더를 자동으로 추가합니다. 그러나 메시지별로 원클릭 수신 거부 동작을 구성해야 하는 경우에는 이전 이메일 Campaigns 및 캔버스 단계를 적절히 업데이트해야 합니다.
{% enddetails %}

{% details 원본 메시지 또는 원시 데이터에서 list-unsubscribe 및 원클릭 수신 거부 헤더를 확인할 수 있는데, Gmail이나 Yahoo에서 수신 거부 버튼이 표시되지 않는 이유는 무엇인가요? %}
Gmail과 Yahoo는 list-unsubscribe 또는 원클릭 수신 거부 헤더를 표시할지 여부를 최종적으로 결정합니다. 신규 발송자이거나 발송자 평판이 낮은 발송자의 경우, 수신 거부 버튼이 표시되지 않을 수 있습니다.
{% enddetails %}

{% details 커스텀 원클릭 수신 거부 헤더는 Liquid를 지원하나요? %}
네, Liquid 및 조건 로직이 지원되어 헤더에 동적 원클릭 수신 거부 URL을 사용할 수 있습니다.
{% enddetails %}

{% alert tip %}
조건 로직을 추가할 때 URL에 공백을 추가하는 출력 값이 생기지 않도록 주의하세요. Braze는 이러한 공백을 제거하지 않습니다.
{% endalert %}

### 메시지 수준 원클릭 list-unsubscribe

{% details 원클릭 이메일 헤더를 수동으로 추가하고 이메일 수신 거부 헤더가 켜져 있는 경우, 예상되는 동작은 무엇인가요? %}
원클릭 list-unsubscribe를 위해 추가된 이메일 헤더는 이 Campaign의 모든 향후 발송에 적용됩니다.
{% enddetails %}

{% details 발송하려면 메시지 배리언트 간에 구독 그룹이 일치해야 하는 이유는 무엇인가요? %}
A/B 테스트가 포함된 Campaign의 경우, Braze는 사용자에게 배리언트 중 하나를 무작위로 발송합니다. 동일한 Campaign에 두 개의 서로 다른 구독 그룹이 설정되어 있으면(배리언트 A는 구독 그룹 A로 설정, 배리언트 B는 구독 그룹 B로 설정), 구독 그룹 B에만 가입한 사용자가 배리언트 B를 수신한다고 보장할 수 없습니다. 사용자가 이미 옵트아웃한 구독 그룹에서 수신 거부하는 시나리오가 발생할 수 있습니다.
{% enddetails %}

{% details 이메일 환경설정에서 이메일 수신 거부 헤더 설정이 꺼져 있지만, Campaign의 발송 정보에서 원클릭 list-unsubscribe 설정이 "워크스페이스 기본값 사용"으로 되어 있습니다. 이것은 버그인가요? %}
아니요. 워크스페이스 설정이 꺼져 있고 메시지 설정이 **워크스페이스 기본값 사용**으로 설정되어 있으면, Braze는 **이메일 환경설정**에서 구성된 내용을 따릅니다. 즉, 해당 Campaign에 원클릭 수신 거부 헤더를 추가하지 않습니다.
{% enddetails %}

{% details 구독 그룹이 보관되면 어떻게 되나요? 발송된 이메일의 원클릭 수신 거부가 중단되나요? %}
원클릭을 위해 **발송 정보**에서 참조된 구독 그룹이 보관되더라도, Braze는 원클릭을 통한 수신 거부를 계속 처리합니다. 해당 구독 그룹은 대시보드(Segment 필터, 고객 프로필 및 유사 영역)에 더 이상 표시되지 않습니다.
{% enddetails %}

{% details 원클릭 수신 거부 설정을 이메일 템플릿에서 사용할 수 있나요? %}
아니요, 현재 이메일 템플릿에 이 기능을 추가할 계획은 없습니다. 이러한 템플릿은 발송 도메인에 할당되지 않기 때문입니다. {% multi_lang_include product_feedback_cta.md context="gap" feature="per-domain sending for email templates" %}
{% enddetails %}

{% details 이 기능은 커스텀 옵션에 추가된 원클릭 수신 거부 URL이 유효한지 확인하나요? %}
아니요, Braze 대시보드에서 링크를 확인하거나 검증하지 않습니다. 발송 전에 URL을 적절히 테스트하세요.
{% enddetails %}