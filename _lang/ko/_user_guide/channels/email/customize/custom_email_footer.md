---
nav_title: 커스텀 이메일 바닥글
article_title: 커스텀 이메일 바닥글
page_order: 6.5
description: "이 문서에서는 워크스페이스 전체에 커스텀 이메일 바닥글을 설정하는 방법을 설명합니다."
channel:
  - email

---

# 커스텀 이메일 바닥글 {#custom-email-footer}

> {% raw %}`{{${email_footer}}}`{% endraw %} Liquid 속성을 사용하여 모든 이메일에 템플릿으로 사용할 수 있는 워크스페이스 전체 커스텀 이메일 바닥글을 설정할 수 있습니다.

커스텀 이메일 바닥글을 사용하면 사용하는 모든 이메일 템플릿이나 이메일 Campaign에 대해 새 바닥글을 만들 필요가 없습니다. 모든 신규 및 기존 이메일 Campaign에는 커스텀 바닥글에 변경한 내용이 반영됩니다. [CAN-SPAM Act of 2003](https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business) 준수를 위해 이메일에 회사의 실제 주소와 탈퇴 링크를 포함해야 합니다.

{% alert warning %}
커스텀 바닥글이 위에서 언급한 요구 사항을 충족하는지 확인하는 것은 귀하의 책임입니다.
{% endalert %}

## 커스텀 바닥글 만들기 {#create-your-custom-footer}

커스텀 바닥글을 만들거나 편집하려면 다음을 수행합니다:

1. **설정** > **이메일 환경설정** > **가입 페이지 및 바닥글**로 이동합니다.
2. **커스텀 바닥글** 섹션으로 이동하여 커스텀 바닥글을 켭니다.
3. **편집**을 선택한 다음 **작성** 섹션에서 바닥글을 편집합니다.
4. **미리보기**를 선택하면 이메일 바닥글이 고객의 받은편지함에 어떻게 표시되는지 미리 볼 수 있습니다. 선택적으로 **미리보기 링크 복사**를 선택하여 임의의 사용자에게 이메일이 어떻게 표시되는지 보여주는 공유 가능한 미리보기 링크를 생성하고 복사할 수 있습니다. 링크는 7일 동안 유효하며 그 후 다시 생성해야 합니다.
5. 테스트 메시지를 보냅니다.

![커스텀 바닥글의 예시.]({% image_buster /assets/img_archive/custom_footer.png %})

기본 바닥글은 {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} 속성과 실제 우편 주소를 사용합니다. 이 기본값을 사용하는 경우 **프로토콜**에서 **&#60;other&#62;**를 선택해야 합니다.

{% alert important %}
CAN-SPAM 규정을 준수하려면 커스텀 바닥글에 탈퇴 링크를 포함해야 합니다. 이 Liquid 속성 {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} 또는 커스텀 탈퇴 URL을 사용할 수 있습니다. 탈퇴 링크가 없으면 커스텀 바닥글을 저장할 수 없습니다.
{% endalert %}

![커스텀 바닥글에 필요한 프로토콜 및 URL 값.]({% image_buster /assets/img_archive/email_unsub_protocol.png %}){: style="max-width:50%;"}

## 탈퇴 링크가 없는 바닥글 {#footers-without-unsubscribe-links}

커스텀 바닥글 {% raw %}`{{${email_footer}}}` 태그는 있지만 `{{${set_user_to_unsubscribed_url}}}`{% endraw %} 탈퇴 링크 태그가 없는 템플릿을 사용할 때는 매우 주의해야 합니다. 경고가 표시되지만, 탈퇴 링크가 있든 없든 이메일을 보낼지 여부는 사용자의 선택입니다.

다음은 이메일 작성기에서의 경고입니다:

![바닥글 없이 작성된 이메일 예시.]({% image_buster /assets/img_archive/no_unsub_link_warning.png %})

다음은 Campaign 작성기에서의 경고입니다:

![바닥글 없는 Campaign 작성.]({% image_buster /assets/img_archive/no_footer_test.png %})

### 커스텀 탈퇴 링크 추가 {#adding-a-custom-unsubscribe-link}

커스텀 탈퇴 링크를 추가하려면 커스텀 바닥글의 탈퇴 링크를 {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %}에서 사용자 ID를 포함하는 쿼리 매개변수가 있는 자체 웹사이트 링크로 변경할 수 있습니다. 예시는 다음과 같습니다:
{% raw %}
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

다음으로, [`/email/status` 엔드포인트]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status)를 호출하여 사용자의 가입 상태를 업데이트합니다. 자세한 내용은 [이메일 가입 상태 변경]({{site.baseurl}}/user_guide/channels/email/subscriptions#changing-email-subscriptions)에 대한 설명서를 참조하세요.

그런 다음 이 새 링크를 저장합니다. 기본 Braze 탈퇴 태그 {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%}가 바닥글에 있어야 합니다. 즉, 태그를 주석에 넣거나 숨겨진 `<div>` 태그에 배치하여 기본 링크를 "숨기는" 방식으로 포함해야 합니다.

## 모범 사례 {#best-practices}

커스텀 바닥글을 만들고 사용할 때 다음 모범 사례를 권장합니다.

### 속성을 사용한 개인화 {#personalizing-with-attributes}

커스텀 바닥글을 만들 때 Braze는 [개인화를 위한 속성]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)을 사용할 것을 권장합니다. 기본 및 커스텀 속성의 전체 세트를 사용할 수 있지만, 다음은 유용할 수 있는 몇 가지입니다:

| 속성 | 태그 |
| --------- | --- |
| 사용자의 이메일 주소 | {% raw %}`{{${email_address}}}`{% endraw %} |
| 사용자의 커스텀 탈퇴 URL | {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} <br><br>이 태그는 이전의 {% raw %}`{{${unsubscribe_url}}}`{% endraw %} 태그를 대체합니다. 대신 최신 {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} 태그를 사용하는 것을 권장합니다. |
| 사용자의 커스텀 옵트인 URL | {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} |
| 사용자의 커스텀 가입 URL | {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}|
| 사용자의 커스텀 Braze 환경설정 센터 URL | {% raw %}`{{${preference_center_url}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="속성을 사용한 개인화" }

### 탈퇴 링크 및 옵트인 링크 포함 {#including-an-unsubscribe-link-and-opt-in-link}

{% raw  %}
모범 사례로서, Braze는 커스텀 바닥글에 탈퇴 링크(예: ``{{${set_user_to_unsubscribed_url}}}``)와 옵트인 링크(예: ``{{${set_user_to_opted_in_url}}}``)를 모두 포함할 것을 권장합니다. 이렇게 하면 사용자가 탈퇴 또는 옵트인을 할 수 있으며, 일부 사용자의 옵트인 데이터를 수동적으로 수집할 수 있습니다.
{% endraw %}

### 일반 텍스트 이메일용 커스텀 바닥글 설정 {#setting-custom-footers-for-plaintext-emails}

**이메일 환경설정** 페이지의 **가입 페이지 및 바닥글** 탭에서 일반 텍스트 이메일용 커스텀 바닥글을 설정할 수도 있으며, HTML 이메일용 커스텀 바닥글과 동일한 규칙을 따릅니다.

일반 텍스트 바닥글을 포함하지 않으면 Braze가 HTML 바닥글에서 자동으로 생성합니다. 커스텀 바닥글이 만족스러우면 **저장**을 선택합니다.

![커스텀 일반 텍스트 바닥글 설정 옵션이 선택된 이메일.]({% image_buster /assets/img_archive/custom_footer_save_changes.png %}){: style="max-width:70%" }

## 고려 사항 {#considerations}


### BrazeAI Decisioning Studio™

[BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio)를 사용하는 경우, {% raw %}`{{${email_footer}}}`{% endraw %}는 표준 Liquid 태그가 아닙니다. Liquid가 실행되기 전에 사전 처리되므로, {% raw %}`{{${email_footer}}}`{% endraw %}를 컨텍스트 변수 값으로 사용하고 `:rerender` 플래그를 호출하면 자동으로 실패합니다. 대신 이메일 바닥글에 [콘텐츠 블록]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks#email-footers)을 사용하세요.

### 링크 템플릿 및 UTM 매개변수 {#link-templates-and-utm-parameters}

{% raw %}`{{${email_footer}}}`{% endraw %}를 사용할 때 링크 템플릿은 커스텀 이메일 바닥글의 링크에 자동으로 추가되지 않습니다. 바닥글 링크에 UTM 매개변수와 같은 링크 템플릿이 필요한 경우, 대신 [콘텐츠 블록]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks#email-footers)을 사용하거나 커스텀 바닥글의 특정 링크에 UTM 매개변수를 수동으로 추가하세요.