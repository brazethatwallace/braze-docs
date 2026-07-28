---
nav_title: 동작 및 미디어 URL
article_title: Liquid로 동작 및 미디어 URL 개인화하기
page_order: 2
description: "이 참조 문서에서는 Liquid를 사용하여 동작 및 미디어 URL을 개인화하는 방법을 설명합니다."
---

# Liquid로 동작 및 미디어 URL 개인화하기 {#personalize-action-and-media-urls-with-liquid}

> 버튼, 링크, 이미지, 동영상의 URL에 Liquid 변수를 추가하여 메시지를 수신하는 각 사용자에 맞게 링크 대상과 콘텐츠를 개인화할 수 있습니다.

## 인앱 콘텐츠로 딥링킹하기 {#deep-link-to-in-app-content}

{% alert tip %}
**개발자용:** 커스텀 스킴, 유니버설 링크 및 기타 옵션 중 선택하는 방법(AASA 파일이 필요한 경우, 구현해야 하는 앱 델리게이트 메서드, 문제 디버깅 방법 포함)에 대한 가이드는 [iOS 딥링킹 가이드]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide) 및 [딥링킹 문제 해결]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting)을 참조하세요.
{% endalert %}

### 딥링킹이란? {#what-is-deep-linking}

딥링킹은 네이티브 앱을 실행하고 특정 동작을 수행하거나 특정 콘텐츠를 표시하도록 추가 정보를 제공하는 방법입니다.

딥링킹은 세 가지 부분으로 구성됩니다:

1. 실행할 앱을 식별합니다.
2. 앱에 수행할 동작을 지시합니다.
3. 동작에 필요한 추가 데이터를 제공합니다.

딥링크는 앱의 특정 부분으로 연결되는 커스텀 URI이며, 이 세 가지 부분을 모두 포함합니다. 핵심은 커스텀 스킴을 정의하는 것입니다. `http:`는 거의 모든 사람에게 익숙한 스킴이지만, 스킴은 어떤 단어로든 시작할 수 있습니다. 스킴은 반드시 문자로 시작해야 하지만, 그 이후에는 문자, 숫자, 더하기 기호, 빼기 기호 또는 점을 포함할 수 있습니다. 실질적으로 충돌을 방지하는 중앙 레지스트리가 없으므로, 스킴에 도메인 이름을 포함하는 것이 모범 사례입니다. 예를 들어, `twitter://`는 이전에 Twitter로 알려진 X의 모바일 앱을 실행하는 iOS URI입니다.

딥링크에서 콜론 이후의 모든 내용은 자유 형식 텍스트입니다. 구조와 해석을 정의하는 것은 여러분에게 달려 있지만, 일반적인 관례는 선행 `//`와 쿼리 매개변수(예: `?foo=1&bar=2`)를 포함하여 `http:` URL을 모델로 하는 것입니다. 앞의 예시에서 `twitter://user?screen_name=[id]`는 앱에서 특정 프로필을 실행하는 데 사용됩니다.

{% alert important %}
래퍼 프레임워크(예: Flutter 또는 Cordova)로 구축된 앱의 경우, Braze는 래퍼별 딥링킹 지원을 제공하지 않습니다. 네이티브 iOS 및 Android 레이어에서 딥링크를 구성해야 합니다. Cordova의 경우 [푸시 알림의 딥링킹]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=cordova)을 참조하세요.
{% endalert %}

### UTM 태그 및 Campaign 기여도 {#utm-tags-and-campaign-attribution}

#### UTM 태그란? {#what-is-a-utm-tag}

[UTM(Urchin Traffic Manager) 태그](https://support.google.com/analytics/answer/10917952?sjid=14344007686729081565-NC#zippy=%2Cin-this-article)를 사용하면 링크에 캠페인 기여도 세부 정보를 직접 포함할 수 있습니다. UTM 태그는 Google Analytics에서 캠페인 기여도 데이터를 수집하는 데 사용되며, 다음 속성을 추적하는 데 사용할 수 있습니다:

- `utm_source`: 트래픽 소스의 식별자(예: `my_app`)
- `utm_medium`: 캠페인 매체(예: `newsfeed`)
- `utm_campaign`: 캠페인의 식별자(예: `spring_2016_campaign`)
- `utm_term`: 사용자를 앱이나 웹사이트로 유도한 유료 검색어의 식별자(예: `pizza`)
- `utm_content`: 사용자가 클릭한 특정 링크 또는 콘텐츠의 식별자(예: `toplink` 또는 `android_iam_button2`)

UTM 태그는 일반 HTTP(웹) 링크와 딥링크 모두에 삽입할 수 있으며, Google Analytics를 통해 추적할 수 있습니다.

##### UTM 태그 계산 {#utm-tag-calculations}

Braze는 Campaign 또는 캔버스 단계의 모든 링크에 대해 _총 클릭 수_를 보고하며, 여기에는 UTM 태그가 없는 링크도 포함될 수 있습니다. 이는 Google Analytics 캠페인 추적 링크에서 캠페인 성과 또는 보고서 빌더에 표시되는 _총 클릭 수_와 다른(종종 더 낮은) 결과를 볼 수 있음을 의미합니다.

#### Braze에서 UTM 태그 사용하기 {#using-utm-tags-with-braze}

일반 HTTP(웹) 링크에 UTM 태그를 사용하려는 경우(예: 이메일 캠페인의 캠페인 기여도를 위해) 조직에서 이미 Google Analytics를 사용하고 있다면, [Google의 URL 빌더](https://ga-dev-tools.google/ga4/campaign-url-builder/)를 사용하여 UTM 링크를 생성할 수 있습니다. 이러한 링크는 다른 링크와 마찬가지로 Braze 캠페인 카피에 쉽게 삽입할 수 있습니다.

앱의 딥링크에 UTM 태그를 사용하려면 앱에 관련 [Google Analytics SDK](https://developers.google.com/analytics/devguides/collection/)가 통합되어 있고 딥링크를 처리하도록 올바르게 구성되어 있어야 합니다. 이에 대해 확실하지 않은 경우 개발자에게 확인하세요.

Analytics SDK가 통합되고 구성된 후, Braze 캠페인의 딥링크에 UTM 태그를 사용할 수 있습니다. 캠페인에 UTM 태그를 설정하려면 대상 URL 또는 딥링크에 필요한 UTM 태그를 포함하세요. 다음 예시는 푸시 알림과 인앱 메시지에서 UTM 태그를 사용하는 방법을 보여줍니다.

##### UTM 태그로 푸시 열람 및 인앱 메시지 클릭 기여도 추적 {#attribute-push-opens-and-in-app-message-clicks-with-utm-tags}

{% tabs %}
{% tab 푸시 열람 %}

푸시 알림의 딥링크에 UTM 태그를 포함하려면, 푸시 메시지의 클릭 시 동작을 딥링크로 설정한 다음 딥링크 주소를 작성하고 다음과 같은 방식으로 원하는 UTM 태그를 포함하세요:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=push&utm_campaign=spring2016giftcards&utm_content=ios_deeplink
```

![UTM 태그를 사용한 푸시 열람 및 인앱 메시지 클릭 기여도 추적 관련 스크린샷.]({% image_buster /assets/img_archive/push_utm_tags.png %})

{% endtab %}
{% tab 인앱 메시지 클릭 %}

인앱 메시지의 딥링크에 UTM 태그를 포함하려면 다음을 사용하세요:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=iam&utm_campaign=spring2021giftcards&utm_content=web_link
```

![UTM 태그를 사용한 푸시 열람 및 인앱 메시지 클릭 기여도 추적 관련 스크린샷.]({% image_buster /assets/img_archive/iam_utm_tags.png %})

{% endtab %}
{% endtabs %}

## URL에서 Liquid 개인화 사용하기 {#use-liquid-personalization-in-urls}

Braze 작성기에서 직접 URL을 동적으로 구성할 수 있으므로, URL에 동적 UTM 매개변수를 추가하거나 사용자에게 고유한 링크를 보낼 수 있습니다(예: 사용자를 유기한 장바구니로 안내하거나 재입고된 특정 제품으로 안내).

### 지원되는 Liquid 개인화 태그로 URL 생성하기 {#create-a-url-with-supported-liquid-personalization-tags}

[지원되는 Liquid 개인화 태그]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)를 사용하여 URL을 동적으로 생성할 수 있습니다.

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

커스텀 정의된 Liquid 변수의 단축도 지원합니다. 다음 예시를 참조하세요:

### Liquid 변수를 사용하여 URL 생성하기 {#create-a-url-using-liquid-variables}

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Liquid 변수로 렌더링된 URL 단축하기 {#shorten-urls-rendered-by-liquid-variables}

**지원 채널:** KakaoTalk, LINE, SMS, RCS, WhatsApp

API 트리거 속성에 포함된 URL을 포함하여 Liquid로 렌더링된 URL을 단축합니다. 예를 들어, {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %}가 유효한 URL을 나타내는 경우, 메시지를 보내기 전에 해당 URL을 단축하고 추적합니다.

### `/messages/send` 엔드포인트에서 URL 단축하기 {#shorten-urls-in-messagessend-endpoint}

[`/messages/send` 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)를 통한 API 전용 메시지에도 링크 단축이 활성화됩니다. 전체 요청 매개변수 목록은 [요청 매개변수]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters)를 참조하세요.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `link_shortening_enabled` | 예 | 부울 | 링크 단축을 활성화하려면 `link_shortening_enabled`를 `true`로 설정하세요. 추적을 사용하려면 `campaign_id`와 `message_variation_id`가 있어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="/messages/send 엔드포인트에서 URL 단축하기" }