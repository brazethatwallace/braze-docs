## 사전 요구 사항 {#prerequisites}

{% tabs local %}
{% tab iOS %}
Flutter iOS 앱에서 딥링킹을 구현하기 전에, `Info.plist` 파일에서 URL 스킴을 구성해야 합니다. 자세한 내용은 [iOS 딥링킹]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift#url-schemes)을 참조하세요.
{% endtab %}

{% tab Android %}
Flutter Android의 경우, Dart 레이어에서 딥링크를 처리하고 있다면 추가적인 네이티브 설정이 필요하지 않습니다. 이 문서에 나와 있는 최소한의 구현만으로 대부분의 Flutter 앱에 충분합니다.

{% alert warning %}
Braze의 네이티브 `com_braze_handle_push_deep_links_automatically` 플래그는 Android에서 기본적으로 `false`로 설정되어 있습니다. `braze.xml`에서 이 값을 `true`로 설정하지 않으면, 사용자가 푸시 알림을 탭해도 `push_opened` 이벤트가 Dart 리스너에 전달되더라도 앱이 자동으로 포그라운드로 전환되거나 딥링크 대상으로 라우팅되지 않습니다. 자세한 내용은 [딥링크 추가 (Android)]({{site.baseurl}}/developer_guide/push_notifications#flutter_step-4-add-deep-links-android)를 참조하세요.
{% endalert %}

고급 네이티브 레이어 링크 처리(예: 커스텀 `IBrazeDeeplinkHandler` 구현)가 필요한 경우, [Android 딥링킹]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=android)을 참조하세요.
{% endtab %}
{% endtabs %}

## 딥링킹 구현 {#implementing-deep-linking}

### 1단계: Flutter 내장 처리 설정 {#step-1-set-up-flutters-built-in-handling}

{% tabs %}
{% tab iOS %}
1. Xcode 프로젝트에서 `Info.plist` 파일을 엽니다.
2. 새 키-값 페어를 추가합니다.
3. 키를 `FlutterDeepLinkingEnabled`로 설정합니다.
4. 타입을 `Boolean`으로 설정합니다.
5. 값을 `YES`로 설정합니다.
    ![추가된 키-값 페어가 포함된 예제 프로젝트의 Info.plist 파일]({% image_buster /assets/img/flutter/flutter-ios-deep-link-info-plist.png %} "Xcode Project Info.plist File")
{% endtab %}

{% tab Android %}
1. Android Studio 프로젝트에서 `AndroidManifest.xml` 파일을 엽니다.
2. `activity` 태그에서 `.MainActivity`를 찾습니다.
3. `activity` 태그 내에 다음 `meta-data` 태그를 추가합니다:
    ```xml
    <meta-data android:name="flutter_deeplinking_enabled" android:value="true" />
    ```
{% endtab %}
{% endtabs %}

### 2단계: Dart 레이어로 데이터 전달 (선택 사항) {#step-2-forward-data-to-the-dart-layer-optional}

사용자를 앱의 특정 위치로 보내거나 특정 함수를 호출하는 등 복잡한 사용 사례에 대해 네이티브, 퍼스트파티 또는 서드파티 링크 처리를 사용할 수 있습니다.

#### 예시: 알림 대화 상자로 딥링킹 {#example-deep-linking-to-an-alert-dialog}

{% alert note %}
다음 예시는 추가 패키지에 의존하지 않지만, [`go_router`](https://pub.dev/packages/go_router)와 같은 네이티브, 퍼스트파티 또는 서드파티 패키지를 구현하는 데 유사한 접근 방식을 사용할 수 있습니다. 추가 Dart 코드가 필요할 수 있습니다.
{% endalert %}

먼저, 네이티브 레이어에서 메서드 채널을 사용하여 딥링크의 URL 문자열 데이터를 Dart 레이어로 전달합니다.

{% tabs %}
{% tab iOS %}
```swift
extension AppDelegate {

  // Delegate method for handling custom scheme links.
  override func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    forwardURL(url)
    return true
  }

  // Delegate method for handling universal links.
  override func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
    guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
        let url = userActivity.webpageURL else {
      return false
    }
    forwardURL(url)
    return true
  }

  private func forwardURL(_ url: URL) {
    guard let controller: FlutterViewController = window?.rootViewController as? FlutterViewController else { return }
    let deepLinkChannel = FlutterMethodChannel(name: "deepLinkChannel", binaryMessenger: controller.binaryMessenger)
    deepLinkChannel.invokeMethod("receiveDeepLink", arguments: url.absoluteString)
  }

}
```
{% endtab %}

{% tab Android %}
```kotlin
class MainActivity : FlutterActivity() {

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    handleDeepLink(intent)
  }

  override fun onNewIntent(intent: Intent) {
      super.onNewIntent(intent)
    handleDeepLink(intent)
  }

  private fun handleDeepLink(intent: Intent) {
    val binaryMessenger = flutterEngine?.dartExecutor?.binaryMessenger
    if (intent?.action == Intent.ACTION_VIEW && binaryMessenger != null) {
      MethodChannel(binaryMessenger, "deepLinkChannel")
        .invokeMethod("receivedDeepLink", intent?.data.toString())
    }
  }

}
```
{% endtab %}
{% endtabs %}

다음으로, Dart 레이어에서 콜백 함수를 사용하여 이전에 전송된 URL 문자열 데이터를 활용해 알림 대화 상자를 표시합니다.

```dart
MethodChannel('deepLinkChannel').setMethodCallHandler((call) async {
  deepLinkAlert(call.arguments, context);
});

void deepLinkAlert(String link, BuildContext context) {
  showDialog(
    context: context,
    builder: (BuildContext context) {
      return AlertDialog(
        title: Text("Deep Link Alert"),
        content: Text("Opened with deep link: $link"),
        actions: <Widget>[
          TextButton(
            child: Text("Close"),
            onPressed: () {
              Navigator.of(context).pop();
            },
          ),
        ],
      );
    },
  );
}
```
