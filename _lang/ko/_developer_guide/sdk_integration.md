---
nav_title: SDK 통합
article_title: Braze SDK 통합
description: "Braze SDK를 통합하는 방법을 알아보세요."
page_order: 2.0
---

# ![Braze 로고]({% image_buster /assets/Braze_Primary_Icon_BLACK.svg %}){: style="float:right;width:120px;border:0;" class="noimgborder"}Braze SDK 통합 {#braze-logo-image_buster-assetsbraze_primary_icon_blacksvg-stylefloatrightwidth120pxborder0-classnoimgborderintegrate-the-braze-sdk}

> Braze SDK를 통합하는 방법을 알아보세요. 각 SDK는 자체 공개 GitHub 리포지토리에서 호스팅되며, Braze 기능을 테스트하거나 자체 애플리케이션과 함께 구현하는 데 사용할 수 있는 완전히 빌드 가능한 샘플 앱이 포함되어 있습니다. 자세히 알아보려면 [참조, 리포지토리 및 샘플 앱]({{site.baseurl}}/developer_guide/references)을 확인하세요. SDK에 대한 보다 일반적인 정보는 [시작하기: 통합 개요]({{site.baseurl}}/developer_guide/getting_started/integration_overview)를 참조하세요.

미러링된 SDK README 콘텐츠는 [리포지토리 가이드]({{site.baseurl}}/developer_guide/sdk_repository_guides)를 참조하세요.

{% alert tip %}
SDK를 통합한 후에는 [SDK 인증]({{site.baseurl}}/developer_guide/sdk_integration/authentication)을 활성화하여 무단 SDK 요청을 방지함으로써 추가적인 보안 계층을 적용할 수 있습니다. SDK 인증은 웹, Android, Swift, React Native, Flutter, Unity, Cordova, .NET MAUI(Xamarin) 및 Expo에서 사용할 수 있습니다.
{% endalert %}

{% alert note %}
SDK 초기화가 HTTPS 인증서 신뢰 오류(예: `Trust anchor for certification path not found`가 포함된 `SSLHandshakeException`)로 실패하는 경우, [SDK 인증서 신뢰 오류 문제 해결]({{site.baseurl}}/developer_guide/sdk_integration/troubleshooting_certificate_errors)을 참조하세요.
{% endalert %}

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/sdk_integration.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/sdk_integration.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/sdk_integration.md %}
{% endsdktab %}

{% sdktab cordova %}
{% multi_lang_include developer_guide/cordova/sdk_integration.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/sdk_integration.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/sdk_integration.md %}
{% endsdktab %}

{% sdktab roku %}
## Roku SDK 통합 {#integrating-the-roku-sdk}

### 1단계: 파일 추가 {#step-1-add-files}

Braze SDK 파일은 [Braze Roku SDK 리포지토리](https://github.com/braze-inc/braze-roku-sdk)의 `sdk_files` 디렉토리에서 찾을 수 있습니다.

1. 앱의 `source` 디렉토리에 `BrazeSDK.brs`를 추가합니다.
2. 앱의 `components` 디렉토리에 `BrazeTask.brs`와 `BrazeTask.xml`을 추가합니다.

### 2단계: 참조 추가 {#step-2-add-references}

다음 `script` 요소를 사용하여 메인 씬에 `BrazeSDK.brs`에 대한 참조를 추가합니다:

```
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

### 3단계: 구성 {#step-3-configure}

`main.brs` 내에서 글로벌 노드에 Braze 구성을 설정합니다:

```brightscript
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = {YOUR_API_KEY}
' example endpoint: "https://sdk.iad-01.braze.com/"
config[config_fields.ENDPOINT] = {YOUR_ENDPOINT}
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

[SDK 엔드포인트]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints)와 API 키는 Braze 대시보드에서 확인할 수 있습니다.

### 4단계: Braze 초기화 {#step-4-initialize-braze}

Braze 인스턴스를 초기화합니다:

```brightscript
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## 선택적 구성 {#optional-configurations}

### 로깅 {#logging}

Braze 통합을 디버깅하려면 Roku 디버그 콘솔에서 Braze 로그를 확인할 수 있습니다. 자세한 내용은 Roku 개발자의 [코드 디버깅](https://developer.roku.com/docs/developer-program/debugging/debugging-channels.md)을 참조하세요.

{% endsdktab %}

{% sdktab unity %}
{% multi_lang_include developer_guide/unity/sdk_integration.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
{% multi_lang_include developer_guide/xamarin/sdk_integration.md %}
{% endsdktab %}

{% sdktab chatgpt apps %}
{% multi_lang_include developer_guide/chatgpt_apps/sdk_integration.md %}
{% endsdktab %}

{% sdktab vega %}
{% multi_lang_include developer_guide/vega/sdk_integration.md %}
{% endsdktab %}
{% endsdktabs %}

{% alert note %}
SDK 통합에 대한 QA를 수행하는 동안 [SDK 디버거]({{site.baseurl}}/developer_guide/sdk_integration/debugging)를 사용하면 앱에서 상세 로깅을 활성화하지 않고도 문제를 해결할 수 있습니다.
{% endalert %}