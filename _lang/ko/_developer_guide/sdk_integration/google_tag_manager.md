---
nav_title: Google 태그 관리자
article_title: Google Tag Manager와 Braze SDK 사용하기
platform:
  - Android
  - FireOS
  - Swift
page_order: 1.1
description: "런타임 초기화, 지연 초기화 또는 Google Tag Manager와 같은 방법을 사용하여 Braze SDK를 초기화하는 방법을 알아보세요."

---

# Google Tag Manager와 Braze SDK 사용하기 {#google-tag-manager-with-the-braze-sdk}

> [Google Tag Manager(GTM)](https://developers.google.com/tag-platform/tag-manager)를 Braze SDK와 함께 사용하는 방법을 알아보세요. 이를 통해 코드 변경이나 새로운 앱 릴리스 없이 Braze 이벤트 추적 및 사용자 속성 업데이트를 원격으로 제어할 수 있습니다.

{% sdktabs %}
{% sdktab web %}
## 웹용 Google Tag Manager 정보 {#google-tag-manager}

Google Tag Manager(GTM)를 사용하면 프로덕션 코드 릴리스나 엔지니어링 리소스 없이도 웹사이트에 원격으로 태그를 추가, 제거, 편집할 수 있습니다. Braze는 웹 SDK를 위해 다음과 같은 템플릿을 제공합니다:

| 태그 유형 | 사용 사례 |
|--------|--------|
| 초기화 태그 | 이 태그를 사용하면 사이트의 코드를 수정할 필요 없이 [웹 Braze SDK를 통합]({{site.baseurl}}/developer_guide/sdk_integration/?tab=google%20tag%20manager&sdktab=web)할 수 있습니다.|
| 동작 태그 | 이 태그를 사용하면 [Content Cards를 생성]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager)하고, [사용자 속성을 설정]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=google%20tag%20manager&sdktab=web)하고, [데이터 수집을 관리]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?tab=google%20tag%20manager&sdktab=web)할 수 있습니다.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="웹용 Google Tag Manager 정보" }

## Braze 동작 태그의 태그 시퀀싱 {#tag-sequencing-for-braze-action-tags}

커스텀 이벤트 및 기타 Braze 동작 태그는 **Braze Initialization** 태그가 웹 SDK 로드를 완료하기 전에 실행되면 실패할 수 있습니다. Google Tag Manager에서 동작 태그를 열고 **Advanced Settings** > **Tag Sequencing**으로 이동한 다음 **A tag that fires before [this tag] is fired**를 선택하고 Braze Initialization 태그를 선택합니다.

자세한 내용은 [커스텀 이벤트의 태그 시퀀싱 확인]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_tag-sequencing)을 참조하세요.

## GTM으로 구매 기록하기 {#log-purchases-with-gtm}

Braze 동작 태그 및 커스텀 HTML 태그에서 `braze.logPurchase()`를 호출하여 매출을 기록합니다. 레거시 `appboy.logPurchase()` 네임스페이스는 현재 웹 SDK 통합에서 지원되지 않습니다.

## GTM으로 커스텀 이벤트 기록하기 {#logging-custom-events-with-gtm}

GTM에서 **커스텀 HTML** 태그를 사용하여 커스텀 이벤트를 기록할 수 있습니다. 이 방법은 GTM [데이터 레이어](https://developers.google.com/tag-platform/tag-manager/datalayer)를 사용하여 사이트에서 Braze 웹 SDK를 호출하는 GTM 태그로 이벤트 데이터를 전달합니다.

### 1단계: 데이터 레이어에 이벤트 푸시하기 {#step-1-push-the-event-to-the-data-layer}

사이트 코드에서 커스텀 이벤트를 트리거하려는 위치에 이벤트를 데이터 레이어에 푸시합니다. 예를 들어, 버튼 클릭 시 커스텀 이벤트를 기록하려면 다음과 같이 합니다:

```html
<button onclick="dataLayer.push({'event': 'my_custom_event'});">Track Event</button>
```

### 2단계: GTM에서 트리거 만들기 {#step-2-create-a-trigger-in-gtm}

1. GTM 컨테이너에서 **Triggers**로 이동하여 새 트리거를 만듭니다.
2. **Trigger Type**을 **Custom Event**로 설정합니다.
3. **Event Name**을 데이터 레이어에 푸시한 값과 동일하게 설정합니다(예: `my_custom_event`).
4. 트리거가 실행될 시점을 선택합니다(예: **All Custom Events**).

### 3단계: 커스텀 HTML 태그 만들기 {#step-3-create-a-custom-html-tag}

1. GTM에서 **Tags**로 이동하여 새 태그를 만듭니다.
2. **Tag Type**을 **Custom HTML**로 설정합니다.
3. HTML 필드에 다음을 추가합니다:

    ```html
    <script>
    window.braze.logCustomEvent("my_custom_event");
    </script>
    ```

4. **Triggering**에서 2단계에서 만든 트리거를 선택합니다.
5. 컨테이너를 저장하고 게시합니다.

이벤트 속성정보를 포함하려면 두 번째 인수로 전달합니다:

```html
<script>
window.braze.logCustomEvent("my_custom_event", {"property_key": "property_value"});
</script>
```

## Google의 EU 사용자 동의 정책 {#googles-eu-user-consent-policy}

{% alert important %}
Google은 2024년 3월 6일부터 시행되는 [디지털 시장법(DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html)의 변경 사항에 대응하여 [EU 사용자 동의 정책](https://www.google.com/about/company/user-consent-policy/)을 업데이트하고 있습니다. 이 새로운 변경 사항은 광고주가 EEA 및 영국 최종사용자에게 특정 정보를 공개하고 필요한 동의를 얻도록 요구합니다. 자세한 내용은 다음 설명서를 참조하세요.
{% endalert %}

Google의 EU 사용자 동의 정책의 일환으로, 다음 부울 커스텀 속성을 사용자 프로필에 기록해야 합니다:

- `$google_ad_user_data`
- `$google_ad_personalization`

GTM 통합을 통해 이러한 값을 설정하는 경우, 커스텀 속성에는 커스텀 HTML 태그를 만들어야 합니다. 다음은 이러한 값을 문자열이 아닌 부울 데이터 유형으로 기록하는 방법의 예시입니다:

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

자세한 내용은 [Google 오디언스 동기화]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync)를 참조하세요.

{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/google_tag_manager.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/google_tag_manager.md %}
{% endsdktab %}
{% endsdktabs %}

## 문제 해결 {#troubleshooting}

Braze가 초기화되지 않거나 이벤트가 예상대로 표시되지 않는 경우, GTM 컨테이너가 게시되었는지, 트리거 및 태그 실행 순서가 SDK [라이프사이클 및 초기화 전략]({{site.baseurl}}/developer_guide/sdk_integration)과 일치하는지, 테스트 기기가 Braze 엔드포인트를 차단하고 있지 않은지 확인하세요.

초기화 실패의 경우, Braze 태그 또는 커스텀 태그 제공업체가 예상되는 `actionType` 및 파라미터를 수신하는지 확인하세요(이 페이지의 Android, Swift, 웹 탭 참조). GTM에서 실행된 이벤트를 검증하는 동안 상세 로깅을 활성화하려면 해당 탭에서 링크된 플랫폼 통합 가이드에 설명된 대로 플랫폼의 SDK 디버그 로깅을 활성화하세요.