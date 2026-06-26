---
nav_title: 지원되는 개인화 태그
article_title: 지원되는 Liquid 개인화 태그
page_order: 1
description: "이 참조 문서에서는 지원되는 Liquid 개인화 태그의 전체 목록을 다룹니다."
search_rank: 1
---

# 지원되는 개인화 태그 {#supported-personalization-tags}

> 이 참조 문서에서는 지원되는 Liquid 개인화 태그의 전체 목록을 다룹니다.

## 지원되는 태그 요약 {#summary-of-supported-tags}

편의를 위해 지원되는 개인화 태그의 요약을 제공합니다. 각 태그 유형과 모범 사례에 대한 자세한 내용은 계속 읽어보세요.

{% raw %}

| 개인화 태그 유형 | 태그 |
| -------------  | ---- |
| 표준(기본값) 속성 | `{{${city}}}` <br> `{{${country}}}` <br> `{{${date_of_birth}}}` <br> `{{${email_address}}}` <br> `{{${first_name}}}` <br> `{{${gender}}}` <br> `{{${language}}}` <br> `{{${last_name}}}` <br> `{{${last_used_app_date}}}` <br> `{{${most_recent_app_version}}}` <br> `{{${most_recent_locale}}}` <br> `{{${most_recent_location}}}` <br> `{{${phone_number}}}` <br> `{{${time_zone}}}` <br> `{{${user_id}}}` <br> `{{${braze_id}}}` <br> `{{${random_bucket_number}}}` <br> `{{subscribed_state.${email_global}}}` <br> `{{subscribed_state.${subscription_group_id}}}` |
| 기기 속성 | `{{most_recently_used_device.${carrier}}}` <br> `{{most_recently_used_device.${id}}}` <br> `{{most_recently_used_device.${idfa}}}` <br> `{{most_recently_used_device.${model}}}` <br> `{{most_recently_used_device.${os}}}` <br> `{{most_recently_used_device.${platform}}}` <br> `{{most_recently_used_device.${google_ad_id}}}` <br> `{{most_recently_used_device.${roku_ad_id}}}` <br> `{{most_recently_used_device.${foreground_push_enabled}}}`|
| <a href='/docs/user_guide/channels/email/subscriptions#managing-user-subscriptions'>이메일 목록 속성</a> | `{{${set_user_to_unsubscribed_url}}}` <br>이 태그는 이전의 `{{${unsubscribe_url}}}` 태그를 대체합니다. 이전 태그는 기존에 생성된 이메일에서 여전히 작동하지만, 새로운 태그를 사용하는 것을 권장합니다. <br><br> `{{${set_user_to_one_click_list_unsubscribe}}}` <br> `{{${set_user_to_subscribed_url}}}` <br> `{{${set_user_to_opted_in_url}}}` |
| <a href='/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting#trigger-messages'>SMS 속성</a> | `{{sms.${inbound_message_body}}}` <br> `{{sms.${inbound_media_urls}}}` |
| <a href='/docs/user_guide/channels/whatsapp/message_processing/messaging_users'>WhatsApp 속성</a> | `{{whats_app.${inbound_message_body}}}` <br> `{{whats_app.${inbound_media_urls}}}` <br> `{{whats_app.${inbound_flow_response}}}` <br> `{{whats_app.${inbound_product_id}}}` <br> `{{whats_app.${inbound_catalog_id}}}` <br> `{{whats_app.${inbound_profile_name}}}` |
| Campaign 속성 및 캔버스 단계 속성 | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| Canvas 속성 | `{{canvas.${name}}}` <br> `{{canvas.${api_id}}}` <br> `{{canvas.${variant_name}}}` <br> `{{canvas.${variant_api_id}}}` |
| 카드 속성 | `{{card.${api_id}}}` <br> `{{card.${name}}}` |
| 지오펜싱 이벤트 | `{{event_properties.${geofence_name}}}` <br> `{{event_properties.${geofence_set_name}}}` |
| 이벤트 등록정보 <br> (워크스페이스에 맞게 커스텀됩니다.)| `{{event_properties.${your_custom_event_property}}}` |
| Canvas 컨텍스트 변수 | `{{context.${your_context_variable}}}` |
| 커스텀 속성 <br> (워크스페이스에 맞게 커스텀됩니다.) | `{{custom_attribute.${your_custom_attribute}}}` |
| <a href='/docs/api/objects_filters/trigger_properties_object/'>API 트리거 등록정보</a> | `{{api_trigger_properties.${your_api_trigger_property}}}` |
| Canvas 진입 등록정보 | `{{context.${property_name}}}` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="지원되는 태그 요약" }

{% endraw %}

{% alert note %}
API 트리거 등록정보는 태그당 두 개의 중괄호를 사용해야 합니다: {% raw %}`{{api_trigger_properties.${your_api_trigger_property}}}`. 세 개의 중괄호(예: `{{{...}}}`){% endraw %}는 유효한 Braze 개인화 구문이 아닙니다. [Braze에서 API 트리거 Liquid가 실패하는 이유는 무엇인가요?]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/faq/#why-is-my-api-triggered-liquid-failing-in-braze)를 참조하세요.
{% endalert %}

### 지원되는 속성 {#supported-attributes}

Campaign, 카드, Canvas 속성은 해당하는 메시징 템플릿에서만 지원됩니다. 예를 들어, `dispatch_id`는 이메일, 푸시, SMS, WhatsApp과 같은 메시징 채널의 Liquid에서 지원되지만, 인앱 메시지나 배너에서는 지원되지 않습니다.

자세한 내용은 [소스별 Campaign 및 Canvas 속성]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/campaign_and_canvas_attributes_across_sources/)을 참조하세요.

### Canvas와 Campaign 태그 차이점 {#canvas-and-campaign-tag-differences}

다음 태그의 동작은 Canvas와 Campaign 간에 다릅니다:
{% raw %}
- `dispatch_id` 동작이 다릅니다. Braze는 캔버스 단계를 트리거된 이벤트로 처리하기 때문입니다. "스케줄"된 경우에도 마찬가지입니다(진입 단계는 스케줄할 수 있으므로 제외). 자세한 내용은 [Dispatch ID 동작]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id/)을 참조하세요.
- Canvas에서 `{{campaign.${name}}}` 태그를 사용하면 Canvas 구성요소 이름이 표시됩니다. Campaign에서 이 태그를 사용하면 Campaign 이름이 표시됩니다.
{% endraw %}

#### URL에서의 Campaign 이름 {#campaign-names-in-urls}

{% raw %}
Campaign 및 메시지 배리언트 이름에는 `%`, 공백, `&`와 같이 URL에 안전하지 않은 문자가 포함될 수 있습니다. `{{campaign.${name}}}` 또는 `{{campaign.${message_name}}}`을 `utm_campaign` 매개변수와 같은 링크나 쿼리 문자열에 삽입할 때는 URL이 올바르게 구문 분석되도록 [`url_encode`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/#url-filters) 필터를 적용하세요. 예를 들어:

```liquid
https://example.com/?utm_campaign={{ campaign.${name} | url_encode }}
```
{% endraw %}

## 가장 최근에 사용한 기기 정보 {#most-recently-used-device-information}

모든 플랫폼에서 사용자의 가장 최근 기기에 대해 다음 속성을 템플릿으로 사용할 수 있습니다. 사용자가 애플리케이션을 사용한 적이 없는 경우(예: REST API를 통해 사용자를 가져온 경우), 이 값은 모두 `null`입니다.

{% raw %}

| 태그 | 설명 |
|---|---|
| `{{most_recently_used_device.${browser}}}` | 사용자 기기에서 가장 최근에 사용한 브라우저입니다. 예를 들어 "Chrome"과 "Safari"가 있습니다. |
| `{{most_recently_used_device.${id}}}` | Braze 기기 식별자입니다. iOS에서는 Apple Identifier for Vendor(IDFV) 또는 UUID일 수 있습니다. Android 및 기타 플랫폼에서는 무작위로 생성된 UUID입니다. |
| `{{most_recently_used_device.${carrier}}}` | 가장 최근에 사용한 기기의 통신사입니다(사용 가능한 경우). 예를 들어 "Verizon"과 "Orange"가 있습니다. |
| `{{most_recently_used_device.${ad_tracking_enabled}}}` | 기기에서 광고 추적이 활성화되어 있는지 여부입니다. 부울 값(`true` 또는 `false`)입니다. |
| `{{most_recently_used_device.${idfa}}}` | iOS 기기의 경우, 애플리케이션이 [선택적 IDFA 수집]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection)으로 구성되어 있으면 이 값은 Identifier for Advertising(IDFA)입니다. iOS가 아닌 기기의 경우 이 값은 null입니다. |
| `{{most_recently_used_device.${google_ad_id}}}` | Android 기기의 경우, 애플리케이션이 선택적 Google Play Advertising ID 수집으로 구성되어 있으면 이 값은 Google Play Advertising Identifier입니다. Android가 아닌 기기의 경우 이 값은 null입니다. |
| `{{most_recently_used_device.${roku_ad_id}}}` | Roku 기기의 경우, 애플리케이션이 Braze로 구성되었을 때 수집되는 Roku Advertising Identifier입니다. Roku가 아닌 기기의 경우 이 값은 null입니다. |
| `{{most_recently_used_device.${model}}}` | 기기의 모델명입니다(사용 가능한 경우). 예를 들어 "iPhone 6S", "Nexus 6P", "Firefox"가 있습니다. |
| `{{most_recently_used_device.${os}}}` | 기기의 운영체제입니다(사용 가능한 경우). 예를 들어 "iOS 9.2.1", "Android (Lollipop)", "Windows"가 있습니다. |
| `{{most_recently_used_device.${platform}}}` | 기기의 플랫폼입니다(사용 가능한 경우). 설정된 경우 값은 `ios`, `android`, `kindle`, `android_china`, `web`, `tvos` 중 하나입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="가장 최근에 사용한 기기 정보" }

기기 통신사, 모델명, 운영체제의 범위가 매우 넓기 때문에, 이러한 값에 조건부로 의존하는 Liquid를 철저히 테스트하는 것을 권장합니다. 특정 기기에서 사용할 수 없는 경우 이 값은 `null`입니다.

## 타겟 앱 정보 {#targeted-app-information}

인앱 메시지의 경우, Liquid 내에서 다음 앱 속성을 사용할 수 있습니다. 값은 앱이 메시징을 요청하는 데 사용하는 SDK API 키를 기반으로 합니다.

| 태그 | 설명 |
|------------------|---|
| `{{app.${api_id}}}` | 메시지를 요청하는 앱의 API 키입니다. 예를 들어, 이 키를 `abort_message()` Liquid와 함께 사용하여 TV 플랫폼이나 별도의 SDK API 키를 사용하는 개발 빌드와 같은 특정 앱에 인앱 메시지를 보내지 않도록 할 수 있습니다. |
| `{{app.${name}}}` | 메시지를 요청하는 앱의 이름입니다(Braze 대시보드에서 정의된 대로). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="타겟 앱 정보" }

예를 들어, 이 Liquid 코드는 요청하는 앱이 목록에 있는 두 개의 API 키 중 하나가 아닌 경우 메시지를 중단합니다:

```liquid
{% assign allowed_api_keys = 'sdk_api_key_1,sdk_api_key_2' | split: ',' %}
{% if allowed_api_keys contains {{app.${api_id}}} %}
User is in list of apps
{% else %}
{% abort_message("User not in list of apps") %}
{% endif %}
```

## 타겟 기기 정보 {#targeted-device-information}

푸시 알림, 인앱 메시지, 배너의 경우, 메시지를 수신하는 기기에 대해 다음 속성을 템플릿으로 사용할 수 있습니다. 푸시 알림, 인앱 메시지 또는 배너에는 사용자가 메시지를 읽는 기기의 속성이 포함될 수 있습니다. 이러한 속성은 Content Cards나 이메일에서는 작동하지 않습니다. 이메일의 경우, 메시지는 발송 전에 렌더링되므로 사용자가 이메일을 여는 기기는 그 시점에 알 수 없습니다.

| 태그 | 설명 |
|------------------|---|
| `{{targeted_device.${id}}}` | Braze 기기 식별자입니다. iOS에서는 Apple Identifier for Vendor(IDFV) 또는 UUID일 수 있습니다. Android 및 기타 플랫폼에서는 무작위로 생성된 UUID입니다. 예를 들어, 사용자가 5개의 기기를 가지고 있으면 5개 기기 모두에 대해 발송 시도가 이루어지며, 각각 해당 기기 식별자를 사용합니다. 메시지가 사용자의 가장 최근에 사용한 기기로 발송하도록 구성된 경우, Braze를 통해 식별된 가장 최근에 사용한 기기에 대해 한 번만 발송 시도가 이루어집니다. |
| `{{targeted_device.${carrier}}}` | 가장 최근에 사용한 기기의 통신사입니다(사용 가능한 경우). 예를 들어 "Verizon"과 "Orange"가 있습니다. |
| `{{targeted_device.${idfa}}}` | iOS 기기의 경우, 애플리케이션이 [선택적 IDFA 수집]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection)으로 구성되어 있으면 이 값은 Identifier for Advertising(IDFA)입니다. iOS가 아닌 기기의 경우 이 값은 null입니다. |
| `{{targeted_device.${google_ad_id}}}` | Android 기기의 경우, 애플리케이션이 [선택적 Google Play Advertising ID 수집]으로 구성되어 있으면 이 값은 Google Play Advertising Identifier입니다. Android가 아닌 기기의 경우 이 값은 null입니다. |
| `{{targeted_device.${roku_ad_id}}}` | Roku 기기의 경우, 애플리케이션이 Braze로 구성되었을 때 수집되는 Roku Advertising Identifier입니다. Roku가 아닌 기기의 경우 이 값은 null입니다. |
| `{{targeted_device.${model}}}` | 기기의 모델명입니다(사용 가능한 경우). 예를 들어 "iPhone 6S", "Nexus 6P", "Firefox"가 있습니다. |
| `{{targeted_device.${os}}}` | 기기의 운영체제입니다(사용 가능한 경우). 예를 들어 "iOS 9.2.1", "Android (Lollipop)", "Windows"가 있습니다. |
| `{{targeted_device.${platform}}}` | 기기의 플랫폼입니다(사용 가능한 경우). 설정된 경우 값은 `ios`, `android`, `kindle`, `android_china`, `web`, `tvos` 중 하나입니다. `most_recently_used_device` 개인화 태그도 사용할 수 있습니다. |
| `{{targeted_device.${foreground_push_enabled}}}` | 타겟 기기에서 포그라운드 푸시가 활성화된 경우 이 값은 `true`이고, 그렇지 않으면 `false`입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="타겟 기기 정보" }

{% endraw %}

기기 통신사, 모델명, 운영체제의 범위가 매우 넓기 때문에, 이러한 값에 조건부로 의존하는 로직을 철저히 테스트하는 것을 권장합니다. 특정 기기에서 사용할 수 없는 경우 이 값은 `null`입니다.

또한 푸시 알림의 경우, 푸시 토큰이 API를 통해 가져온 경우와 같은 특정 상황에서 Braze가 푸시 알림에 연결된 기기를 식별하지 못할 수 있으며, 이로 인해 해당 메시지의 값이 `null`이 될 수 있습니다.

![푸시 메시지에서 이름 변수를 사용할 때 기본값으로 "there"를 사용하는 예시.]({% image_buster /assets/img_archive/personalized_firstname_.png %})

### 기본값 대신 조건 로직 사용 {#using-conditional-logic-instead-of-a-default-value}

경우에 따라 기본값을 설정하는 대신 [조건 로직]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic/)을 사용할 수 있습니다. 조건 로직을 사용하면 커스텀 속성의 값에 따라 다른 메시지를 보낼 수 있습니다. 또한 조건 로직을 사용하여 null 또는 빈 속성 값을 가진 고객에게 [메시지를 중단]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/)할 수 있습니다.

#### 사용 사례 {#use-case}

예를 들어, 고객에게 리워드 잔액 알림을 보내고 있다고 가정해 보겠습니다. 기본값을 사용하여 잔액이 낮거나 null인 고객을 적절히 처리하기 어렵습니다.

이 경우 기본값을 설정하는 것보다 더 나은 두 가지 옵션이 있습니다:

1. 잔액이 낮거나 null이거나 빈 고객에 대해 메시지를 중단합니다.

{% raw %}

   ```liquid
   {% if {{custom_attribute.${balance}}} > 0 %}
   Your rewards balance is {{custom_attribute.${balance}}}
   {% else %}
   {% abort_message() %}
   {% endif %}
   ```

{% endraw %}

2. 이러한 고객에게 완전히 다른 메시지를 보냅니다. 예를 들어:

{% raw %}

   ```liquid
   {% if ${first_name} != blank and ${first_name} != null %}
   Hello {{${first_name} | default: 'there'}}, thanks for downloading!
   {% else %}
   Thanks for downloading!
   {% endif %}
   ```

이 사용 사례에서 이름이 빈 값이거나 null인 사용자는 "Thanks for downloading!" 메시지를 받습니다. 실수가 발생했을 때 고객에게 Liquid가 그대로 표시되지 않도록 이름에 [기본값]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values/)을 포함하는 것을 권장합니다.

{% endraw %}

## 변수 태그 {#variable-tags}

`assign` 태그를 사용하여 메시지 작성기에서 변수를 생성할 수 있습니다. 변수에 고유한 이름을 사용하는 것을 권장합니다. 지원되는 개인화 태그와 유사한 이름(예: `language`)으로 변수를 생성하면 메시징 로직에 영향을 줄 수 있습니다.

변수를 생성한 후에는 메시징 로직이나 메시지에서 해당 변수를 참조할 수 있습니다. 이 태그는 [연결된 콘텐츠]({% image_buster /assets/img_archive/personalized_firstname_.png %}) 기능에서 반환된 콘텐츠를 다시 포맷하려는 경우에 유용합니다. Shopify의 [변수 태그](https://docs.shopify.com/themes/liquid/tags/variable-tags) 설명서에서 자세한 내용을 확인할 수 있습니다.

{% alert tip %}
매번 메시지마다 같은 변수를 할당하고 계신가요? `assign` 태그를 반복해서 작성하는 대신, 해당 태그를 콘텐츠 블록으로 저장하고 메시지 상단에 배치할 수 있습니다.

1. [콘텐츠 블록을 생성합니다]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/#create-a-content-block).
2. 콘텐츠 블록에 이름을 지정합니다(공백이나 특수 문자 없이).
3. 페이지 하단에서 **편집**을 선택합니다.
4. `assign` 태그를 입력합니다.

콘텐츠 블록이 메시지 상단에 있는 한, 변수가 메시지에 오브젝트로 삽입될 때마다 선택한 커스텀 속성을 참조합니다.
{% endalert %}

### 사용 사례

고객이 100 리워드 포인트를 적립한 후 리워드 포인트를 상품으로 교환할 수 있도록 허용한다고 가정해 보겠습니다. 따라서 추가 구매를 했을 때 포인트 잔액이 100 이상이 되는 고객에게만 메시지를 보내려고 합니다:

{% raw %}
```liquid
{% assign new_points_balance = {{custom_attribute.${current_rewards_balance} | plus: 50}} %}
{% if new_points_balance >= 100 %}
Make a purchase to bring your rewards points to {{new_points_balance}} and cash in today!
{% else %}
{% abort_message('not enough points') %}
{% endif %}
```
{% endraw %}

## 반복 태그 {#iteration-tags}

{% raw %}
반복 태그를 사용하여 코드 블록을 반복적으로 실행할 수 있습니다. 아래 사용 사례에서는 `for` 태그를 사용합니다.

### 사용 사례

Nike 운동화 세일을 진행 중이고 Nike에 관심을 표현한 고객에게 메시지를 보내려고 한다고 가정해 보겠습니다. 각 고객의 프로필에 조회한 제품 브랜드 배열이 있습니다. 이 배열에는 최대 25개의 제품 브랜드가 포함될 수 있지만, 가장 최근 5개의 제품 조회 중 Nike 제품을 조회한 고객에게만 메시지를 보내려고 합니다.

```liquid
{% for items in {{custom_attribute.${Brands Viewed}}} limit:5 %}
{% if {{items}} contains 'Converse' %}
{% assign converse_viewer = true %}
{% endif %}
{% endfor %}
{% if converse_viewer == true %}
Sale on Converse!
{% else %}
{% abort_message() %}
{% endif %}
```

이 사용 사례에서는 운동화 브랜드 조회 배열의 처음 5개 항목을 확인합니다. 해당 항목 중 하나가 converse이면 `converse_viewer` 변수를 생성하고 true로 설정합니다.

그런 다음 `converse_viewer`가 true일 때 세일 메시지를 보냅니다. 그렇지 않으면 메시지를 중단합니다.

이것은 Braze 메시지 작성기에서 반복 태그를 사용하는 간단한 예시입니다. Shopify의 [반복 태그](https://docs.shopify.com/themes/liquid/tags/iteration-tags) 설명서에서 자세한 정보를 확인할 수 있습니다.

## 구문 태그 {#syntax-tags}

구문 태그를 사용하여 Liquid가 렌더링되는 방식을 제어할 수 있습니다. `echo` 태그를 사용하여 표현식을 반환할 수 있습니다. 이는 중괄호로 표현식을 감싸는 것과 동일하지만, Liquid 태그 내에서 이 태그를 사용할 수 있습니다. 또한 `liquid` 태그를 사용하여 각 태그에 구분자 없이 Liquid 블록을 작성할 수 있습니다. `liquid` 태그를 사용할 때 각 태그는 자체 줄에 있어야 합니다. 자세한 정보와 예시는 Shopify의 [구문 태그](https://shopify.dev/api/liquid/tags#syntax-tags) 설명서를 확인하세요.

[공백 제어](https://shopify.github.io/liquid/basics/whitespace/)를 사용하면 태그 주변의 공백을 제거하여 Liquid 출력의 모양을 더 세밀하게 제어할 수 있습니다.

## HTTP 상태 코드 {#http-personalization}

[연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) 호출의 HTTP 상태를 먼저 로컬 변수로 저장한 다음 `__http_status_code__` 키를 사용하여 활용할 수 있습니다. 예를 들어:

```html
{% connected_content https://example.com/api/endpoint :save connected %}
{% if connected.__http_status_code__ != 200 %}
{% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert note %}
이 키는 엔드포인트가 JSON 오브젝트를 반환하는 경우에만 연결된 콘텐츠 오브젝트에 자동으로 추가됩니다. 엔드포인트가 배열이나 다른 유형을 반환하는 경우, 해당 키는 응답에 자동으로 설정될 수 없습니다.
{% endalert %}

## 언어, 최근 로케일, 시간대에 따라 메시지 보내기 {#send-messages-based-on-language-most-recent-locale-and-time-zone}

경우에 따라 특정 로케일에 맞는 메시지를 보내고 싶을 수 있습니다. 예를 들어, 브라질 포르투갈어는 일반적으로 유럽 포르투갈어와 다릅니다.

### 사용 사례: 최근 로케일에 따라 현지화 {#use-case-localize-based-on-recent-locale}

다음은 가장 최근 로케일을 사용하여 국제화된 메시지를 추가로 현지화하는 방법에 대한 사용 사례입니다.

{% raw %}

```liquid
{% if ${language} == 'en' %}
Message in English
{% elsif  ${language} == 'fr' %}
Message in French
{% elsif  ${language} == 'ja' %}
Message in Japanese
{% elsif  ${language} == 'ko' %}
Message in Korean
{% elsif  ${language} == 'ru' %}
Message in Russian
{% elsif ${most_recent_locale} == 'pt_BR' %}
Message in Brazilian Portuguese
{% elsif ${most_recent_locale} == 'pt_PT' %}
Message in European Portuguese
{% elsif  ${language} == 'pt' %}
Message in default Portuguese
{% else %}
Message in default language
{% endif %}
```

이 사용 사례에서 가장 최근 로케일이 `pt_BR`인 고객은 브라질 포르투갈어로 메시지를 받고, 가장 최근 로케일이 `pt_PT`인 고객은 유럽 포르투갈어로 메시지를 받습니다. 처음 두 조건을 충족하지 않지만 언어가 포르투갈어로 설정된 고객은 기본 포르투갈어 유형으로 설정한 메시지를 받습니다.

### 사용 사례: 시간대별 사용자 타겟팅 {#use-case-target-users-by-time-zone}

시간대별로 사용자를 타겟팅할 수도 있습니다. 예를 들어, EST에 있는 사용자에게는 하나의 메시지를, PST에 있는 사용자에게는 다른 메시지를 보냅니다. 이를 위해 현재 시간을 UTC로 저장하고, 사용자의 현재 시간과 if/else 문을 비교하여 올바른 시간대에 맞는 올바른 메시지를 보냅니다. 사용자에게 적절한 시간에 Campaign을 전달하기 위해 사용자의 현지 시간대로 Campaign을 발송하도록 설정해야 합니다.

다음 사용 사례에서는 오후 2시에서 3시 사이에 전달되는 메시지를 각 시간대별로 특정 메시지와 함께 작성하는 방법을 확인하세요.

```liquid
{% assign hour_in_utc = 'now' | date: '%H' | plus:0 %}
{% if hour_in_utc >= 19 && hour_in_utc < 20 %}
It is between 2:00:00 pm and 2:59:59 pm ET!
{% elsif hour_in_utc >= 22 && hour_in_utc < 23 %}
It is between 2:00:00 pm and 2:59:59 pm PT!
{% else %}
{% abort_message %}
{% endif %}
```

{% endraw %}

## 랜덤 숫자로 메시지 보내기 {#send-messages-with-a-random-number}

{% raw %}
`{% random %}` 태그는 랜덤 숫자를 반환합니다. A/B 스타일 로직, 샘플링 또는 메시지 콘텐츠 변형에 사용할 수 있습니다.

| 태그 | 설명 |
|-------|--------------|
| `{% random %}` | 0과 1 사이의 플로트입니다(0 포함, 1 미포함). |
| `{% random 10 %}` (정수 인수) | 0부터 지정된 정수 미만까지의 정수입니다. 예를 들어, `{% random 10 %}`은 0에서 9까지의 정수를 반환합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="랜덤 숫자로 메시지 보내기" }

{% endraw %}

### 사용 사례: 사용자에게 랜덤 배리언트 보내기 {#use-case-send-users-random-variants}

{% raw %}
```liquid
{% capture roll_str %}{% random %}{% endcapture %}
{% assign roll = roll_str | plus: 0 %}
{% if roll < 0.5 %}
Show variant A
{% else %}
Show variant B
{% endif %}
```
{% endraw %}

## eCommerce 장바구니 태그 {#shopping-cart-tag}

`shopping_cart` 태그는 eCommerce [유기한 장바구니]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/?tab=abandoned%20cart#abandoned-cart) 및 [유기한 결제]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/?tab=abandoned%20checkout#abandoned-checkout) eCommerce Canvas 사용 사례에서 사용자의 장바구니 내용에 접근합니다. `CART_ID`를 실제 장바구니 ID 값(예: {% raw %}`{{context.${cart_id}}}`{% endraw %})으로 교체하세요.

{% raw %}
```liquid
{% shopping_cart CART_ID :abort_if_not_abandoned false %}
```
{% endraw %}

이 예시의 `abort_if_not_abandoned` 매개변수는 `ecommerce.checkout_started` 이벤트와 함께 사용할 때 [유기한 결제]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/?tab=abandoned%20checkout#abandoned-checkout) 사용 사례에만 적용됩니다. 유기한 장바구니 사용 사례에는 적용되지 않습니다. 자세한 내용은 [`abort_if_not_abandoned`]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/?tab=abandoned%20checkout#abort-if-not-abandoned)를 참조하세요.

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags