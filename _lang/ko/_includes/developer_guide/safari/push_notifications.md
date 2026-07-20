{% multi_lang_include developer_guide/prerequisites/web.md %} 웹 SDK에 대한 [푸시 알림 설정]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)도 필요합니다. iOS 및 iPadOS 사용자에게는 [Safari v16.4](https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes) 이상을 사용하는 경우에만 푸시 알림을 보낼 수 있습니다.

## 모바일용 Safari 푸시 설정하기 {#setting-up-safari-push-for-mobile}

### 1단계: 매니페스트 파일 만들기 {#manifest}

[웹 애플리케이션 매니페스트](https://developer.mozilla.org/en-US/docs/Web/Manifest)는 웹사이트가 사용자의 홈 화면에 설치될 때 표시되는 방식을 제어하는 JSON 파일입니다.

예를 들어 [앱 스위처](https://support.apple.com/en-us/HT202070)에서 사용하는 배경 테마 색상과 아이콘, 네이티브 앱처럼 전체 화면으로 렌더링할지, 앱을 가로 또는 세로 모드로 열지 여부를 설정할 수 있습니다.

웹사이트의 루트 디렉터리에 다음과 같은 필수 필드를 사용하여 `manifest.json` 파일을 새로 만듭니다.

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

### 2단계: 매니페스트 파일 링크 {#manifest-link}

웹사이트의 `<head>` 요소에 매니페스트 파일이 호스팅되는 위치를 가리키는 다음 `<link>` 태그를 추가합니다.

```html
<link rel="manifest" href="/manifest.json" />
```

### 3단계: 서비스 워커 추가 {#service-worker}

[웹 푸시 통합 가이드]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration#step-1-configure-your-sites-service-worker)에 설명된 대로 웹사이트에 Braze 서비스 워커 라이브러리를 가져오는 서비스 워커 파일이 있어야 합니다.

### 4단계: 홈 화면에 추가 {#add-to-homescreen}

인기 있는 브라우저(예: Safari, Chrome, FireFox 및 Edge)는 모두 최신 버전에서 웹 푸시 알림을 지원합니다. iOS 또는 iPadOS에서 푸시 권한을 요청하려면 **공유하기** > **홈 화면에 추가**를 선택하여 사용자의 홈 화면에 웹사이트를 추가해야 합니다. [홈 화면에 추가](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc)를 통해 사용자는 웹사이트를 북마크하고 아이콘을 소중한 홈 화면 공간에 추가할 수 있습니다.

![웹사이트를 북마크하고 홈 화면에 저장하는 옵션을 보여주는 iPhone]({% image_buster /assets/img/push_implementation_guide/add-to-homescreen.png %}){: style="max-width:40%"}

### 5단계: 네이티브 푸시 프롬프트 표시 {#push-prompt}
앱이 홈 화면에 추가된 후 사용자가 버튼 클릭 등의 작업을 수행할 때 푸시 권한을 요청할 수 있습니다. [`requestPushPermission`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestpushpermission) 메서드를 사용하거나 [노코드 푸시 프라이머 인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages)를 사용하여 수행할 수 있습니다.

{% alert note %}
프롬프트를 수락하거나 거부한 후에는 프롬프트를 다시 표시하려면 웹사이트를 홈 화면에서 삭제하고 다시 설치해야 합니다.
{% endalert %}

![알림을 '허용' 또는 '허용 안 함'으로 설정할지 묻는 푸시 프롬프트]({% image_buster /assets/img/push_implementation_guide/safari-mobile-push-prompt.png %}){: style="max-width:40%"}

예를 들어 다음과 같습니다.

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

다음으로 [테스트 메시지]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages)를 보내 통합을 검증합니다. 통합이 완료되면 [노코드 푸시 프라이머 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages)를 사용하여 푸시 옵트인율을 최적화할 수 있습니다.