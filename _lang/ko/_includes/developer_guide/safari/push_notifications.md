{% multi_lang_include developer_guide/prerequisites/web.md %} 웹 SDK에 대한 [푸시 알림 설정]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)도 필요합니다. iOS 및 iPadOS 사용자에게는 [Safari v16.4](https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes) 이상을 사용하는 경우에만 푸시 알림을 보낼 수 있습니다.

## Safari 모바일 푸시 설정하기 {#setting-up-safari-push-for-mobile}

### 1단계: 매니페스트 파일 만들기 {#manifest}

[웹 애플리케이션 매니페스트](https://developer.mozilla.org/en-US/docs/Web/Manifest)는 웹사이트가 사용자의 홈 화면에 설치될 때 어떻게 표시되는지를 제어하는 JSON 파일입니다.

예를 들어, [앱 전환기](https://support.apple.com/en-us/HT202070)에서 사용할 배경 테마 색상과 아이콘을 설정하거나, 네이티브 앱처럼 전체 화면으로 렌더링할지 여부, 앱을 가로 모드로 열지 세로 모드로 열지 등을 지정할 수 있습니다.

웹사이트의 루트 디렉토리에 다음 필수 필드를 포함하여 새로운 `manifest.json` 파일을 생성합니다.

```json
{
  "name": "your app name",
  "short_name": "your app name",
  "display": "fullscreen",
  "icons": [{
    "src": "favicon.ico",
    "sizes": "128x128",
  }]
}
```

지원되는 전체 필드 목록은 [MDN의 웹 앱 매니페스트 설명서](https://developer.mozilla.org/en-US/docs/Web/Manifest)에서 확인할 수 있습니다.

### 2단계: 매니페스트 파일 연결하기 {#manifest-link}

매니페스트 파일이 호스팅되는 위치를 가리키는 다음 `<link>` 태그를 웹사이트의 `<head>` 요소에 추가합니다.

```html
<link rel="manifest" href="/manifest.json" />
```

### 3단계: 서비스 워커 추가하기 {#service-worker}

[웹 푸시 통합 가이드]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration#step-1-configure-your-sites-service-worker)에 설명된 대로 Braze 서비스 워커 라이브러리를 가져오는 서비스 워커 파일이 웹사이트에 있어야 합니다.

### 4단계: 홈 화면에 추가하기 {#add-to-homescreen}

주요 브라우저(Safari, Chrome, Firefox, Edge 등)는 최신 버전에서 웹 푸시 알림을 지원합니다. iOS 또는 iPadOS에서 푸시 권한을 요청하려면 **공유** > **홈 화면에 추가**를 선택하여 웹사이트를 사용자의 홈 화면에 추가해야 합니다. [홈 화면에 추가](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc) 기능을 사용하면 사용자가 웹사이트를 북마크하여 홈 화면에 아이콘을 추가할 수 있습니다.

![웹사이트를 북마크하고 홈 화면에 저장하는 옵션을 보여주는 iPhone]({% image_buster /assets/img/push_implementation_guide/add-to-homescreen.png %}){: style="max-width:40%"}

### 5단계: 네이티브 푸시 프롬프트 표시하기 {#push-prompt}
앱이 홈 화면에 추가된 후, 사용자가 특정 동작(예: 버튼 클릭)을 수행할 때 푸시 권한을 요청할 수 있습니다. 이 작업은 [`requestPushPermission`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestpushpermission) 메서드를 사용하거나, [노코드 푸시 프라이머 인앱 메시지]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)를 통해 수행할 수 있습니다.

{% alert note %}
프롬프트를 수락하거나 거부한 후에 다시 프롬프트를 표시하려면 홈 화면에서 웹사이트를 삭제한 후 다시 설치해야 합니다.
{% endalert %}

![알림에 대해 '허용' 또는 '허용 안 함'을 선택할 수 있는 푸시 프롬프트]({% image_buster /assets/img/push_implementation_guide/safari-mobile-push-prompt.png %}){: style="max-width:40%"}

예시:

```typescript
import { requestPushPermission } from "@braze/web-sdk";

button.onclick = function(){
    requestPushPermission(() => {
        console.log(`User accepted push prompt`);
    }, (temporary) => {
        console.log(`User ${temporary ? "temporarily dismissed" : "permanently denied"} push prompt`);
    });
};
```

## 다음 단계 {#next-steps}

다음으로, 통합을 검증하기 위해 [테스트 메시지]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages)를 자신에게 보내보세요. 통합이 완료되면, [노코드 푸시 프라이머 메시지]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)를 사용하여 푸시 옵트인 비율을 최적화할 수 있습니다.