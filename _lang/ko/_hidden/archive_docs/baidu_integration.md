---
nav_title: Baidu 통합
article_title: Android용 Baidu 푸시 알림 통합
platform: Android
permalink: /baidu_integration/
description: "이 문서에서는 Baidu Android 통합을 설정하는 방법을 설명합니다."
hidden: true
---
# Baidu 통합 {#baidu-integration}
{% alert warning %}
Braze Baidu 푸시 통합은 2022년 3월 24일부로 지원이 중단되었습니다.

* **2022년 3월 24일:** Braze 대시보드에서 새로운 Baidu 앱을 생성할 수 없습니다.
* **2022년 9월 15일:** 새로운 Baidu 푸시 메시지를 생성할 수 없습니다. 기존 메시지와 데이터 수집에는 영향이 없습니다.
* **2023년 1월 15일:** Braze는 더 이상 Baidu 앱에서 메시지를 전송하거나 데이터를 수집하지 않습니다.
{% endalert %}

Braze는 [Baidu Cloud Push]({% image_buster /assets/img_archive/baidu_app_console.png %})를 사용하여 Android 기기에 푸시 알림을 보낼 수 있습니다. Baidu Cloud Push를 사용하더라도 Baidu 앱 스토어를 통해 앱을 배포할 필요는 없습니다.

## 1단계: Baidu 계정 생성 {#step-1-create-a-baidu-account}

Baidu 계정을 생성하려면 [Baidu 포털](https://www.baidu.com/)을 방문하고 **登录**(로그인)을 클릭하여 로그인하거나 새 계정을 만들 수 있는 대화 상자를 표시합니다.

![]({% image_buster /assets/img_archive/baidu_portal.png %})

새 계정을 만들려면 로그인 대화 상자 하단에서 **立即注册**(새 계정)을 클릭합니다.

![]({% image_buster /assets/img_archive/baidu_login_dialog.png %}){: style="max-width:70%;"}

계정 생성 페이지에 사용자 이름, 전화번호 및 비밀번호를 입력합니다. 다음으로 인증 코드 받기 버튼을 클릭합니다. Baidu에서 인증 코드가 포함된 SMS 메시지를 받게 됩니다. 마지막으로 라이선스 계약에 동의하고 **注册**(계정 생성)을 클릭하여 등록합니다. 이 설정 단계가 실패하면 이 [로그인 문서](https://www.adchina.io/how-to-open-a-baidu-account-outside-china/)에 설명된 대로 Baidu Cloud 로그인을 통해 등록해 보세요.

![Baidu 가입 페이지]({% image_buster /assets/img_archive/baidu_signup.png %}){: style="max-width:80%;"}

## 2단계: Baidu 개발자로 등록 {#step-2-register-as-a-baidu-developer}

다음으로 Baidu 개발자로 등록해야 합니다. 먼저 [Baidu 개발자 포털](http://developer.baidu.com/)을 방문하고 **注册**(새 개발자 계정 만들기)를 선택하여 등록을 시작합니다.

![]({% image_buster /assets/img_archive/baidu_dev_portal.png %})

등록 페이지에서 계정 유형(个人은 개인용, 公司는 비즈니스용)과 개발자 유형(개발자가 미리 선택되어 있으며 대부분의 경우 올바름)을 선택합니다. 이름, 약력 및 국가 코드를 괄호 안에 포함한 전화번호를 입력합니다(예: (1)xxxxxxxxxx). **发送验证码**(인증 코드 전송)를 클릭하고 다음 줄에 인증 코드를 입력합니다. 다음 두 필드인 개발자 웹사이트와 개발자 로고는 선택 사항입니다. 라이선스 계약에 동의하고 **提交**(제출)를 클릭하여 제출합니다. 이제 Baidu 개발자 계정이 생성되었습니다.

![]({% image_buster /assets/img_archive/baidu_dev_reg.png %})

## 3단계: Baidu에 애플리케이션 등록 {#step-3-register-your-application-with-baidu}

Baidu에 애플리케이션을 등록하려면 [Baidu 프로젝트 포털](http://developer.baidu.com/console#app/project)을 방문하고 **创建工程**(프로젝트 만들기)을 클릭합니다.

![]({% image_buster /assets/img_archive/baidu_project.png %})

다음 페이지에서 애플리케이션 이름을 입력합니다. 다음 두 개의 체크박스는 추가 Baidu 서비스를 활성화하기 위한 것입니다. 대부분의 경우 비워 두어야 합니다.

![]({% image_buster /assets/img_archive/baidu_app_name.png %})

애플리케이션을 설정하면 API 키를 포함한 앱 정보가 표시되는 콘솔로 이동합니다. 다음으로 사이드바에서 **云推送**(클라우드 푸시)로 이동합니다. 다음 페이지에서 **推送设置**(푸시 설정)를 클릭합니다.

![]({% image_buster /assets/img_archive/baidu_app_console.png %})

![]({% image_buster /assets/img_archive/baidu_continue.png %})

다음 페이지에서 앱 패키지 이름(예: `com.braze.sample`)을 입력하고 메시지를 캐시할지 여부와 캐시할 경우 기간(시간 단위)을 지정합니다. 이는 Baidu가 오프라인 사용자에게 메시지를 보내려고 시도하는 기간을 나타냅니다. **保存设置**(설정 저장)를 클릭하여 저장합니다.

![]({% image_buster /assets/img_archive/baidu_configure_cloud.png %})

## 4단계: 애플리케이션에 Baidu 추가 {#step-4-add-baidu-to-your-application}

[Baidu 푸시 SDK 포털](http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk)을 방문하여 최신 Baidu Cloud Push Android SDK를 다운로드합니다.

![]({% image_buster /assets/img_archive/baidu_sdk.png %})

SDK 내부에는 푸시 서비스 jar 및 플랫폼별 네이티브 라이브러리가 있습니다. 이를 프로젝트에 통합합니다. 앱이 현재 Baidu에서 지원하는 최신 SDK 버전을 대상으로 하는지 확인하세요. 이 설명서는 Baidu Cloud Push Android SDK 버전 `4.6.2.38`에 해당합니다.

애플리케이션의 `AndroidManifest.xml`에 다음 필수 Baidu 권한을 추가합니다.

```xml
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
    <uses-permission android:name="android.permission.WRITE_SETTINGS" />
    <uses-permission android:name="android.permission.VIBRATE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.DISABLE_KEYGUARD" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
```

Baidu의 라이브러리에는 수신 푸시 메시지를 처리하는 브로드캐스트 수신기가 포함되어 있습니다. 애플리케이션의 `AndroidManifest.xml`에서 `<application>` 요소 내에 내부 Baidu 수신기를 선언합니다.

```xml
  <!-- 用于接收系统消息以保证 PushService 正常运行 -->
      <receiver
        android:name="com.baidu.android.pushservice.PushServiceReceiver"
        android:process=":bdservice_v1">
        <intent-filter>
          <action android:name="android.intent.action.BOOT_COMPLETED"/>
          <action android:name="android.net.conn.CONNECTIVITY_CHANGE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.SHOW"/>
          <action android:name="com.baidu.android.pushservice.action.media.CLICK"/>
        </intent-filter>
      </receiver>
      <!-- Push 服务接收客户端发送的各种请求-->
      <!-- 注意:RegistrationReceiver 在 2.1.1 及之前版本有拼写失误,为 RegistratonReceiver ,用 新版本 SDK 时请更改为如下代码-->
      <receiver
        android:name="com.baidu.android.pushservice.RegistrationReceiver"
        android:process=":bdservice_v1">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.METHOD"/>
          <action android:name="com.baidu.android.pushservice.action.BIND_SYNC"/>
        </intent-filter>
        <intent-filter>
          <action android:name="android.intent.action.PACKAGE_REMOVED"/>
          <data android:scheme="package"/>
        </intent-filter>
      </receiver>
      <!-- Push 服务 -->
      <!-- 注意:在 4.0 (包含)之后的版本需加上如下所示的 intent-filter action -->
      <service
        android:name="com.baidu.android.pushservice.PushService"
        android:exported="true"
        android:process=":bdservice_v1">
        <intent-filter >
          <action android:name="com.baidu.android.pushservice.action.PUSH_SERVICE"/>
        </intent-filter>
      </service>
```

또한 수신 푸시 메시지와 알림을 수신하는 브로드캐스트 수신기를 만들어야 합니다. 애플리케이션의 `AndroidManifest.xml`에서 `<application>` 요소 내에 수신기를 선언합니다. 이 수신기는 `com.baidu.android.pushservice.PushMessageReceiver`를 확장하고 Baidu 푸시 서비스로부터 이벤트 업데이트를 수신하는 메서드를 구현해야 합니다.

```xml
      <receiver android:name=".MyPushMessageReceiver">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.MESSAGE"/>
          <action android:name="com.baidu.android.pushservice.action.RECEIVE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.CLICK"/>
        </intent-filter>
      </receiver>
```

메인 액티비티의 `onCreate()` 메서드에 다음 줄을 추가하여 애플리케이션을 Baidu에 등록하고 수신 푸시 메시지를 수신하기 시작합니다. "Your-API-Key"를 프로젝트의 Baidu API 키로 교체하세요.

```
PushManager.startWork(getApplicationContext(), PushConstants.LOGIN_TYPE_API_KEY, "Your-API-Key");
```

마지막으로 Braze에 사용자를 등록해야 합니다. 이 단계에서 생성한 Baidu 브로드캐스트 수신기의 `onBind()` 메서드에서 `Braze.registerAppboyPushMessages(channelId)`를 사용하여 `channelId`를 Braze에 전송합니다.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).setRegisteredPushToken(channelId);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).setRegisteredPushToken(channelId)
```

{% endtab %}
{% endtabs %}

## 5단계: 푸시 열람 등록 {#step-5-registering-push-opens}

Baidu는 JSON 형식으로 푸시 메시지에 추가 키-값 페어를 보내는 것을 지원합니다. 사용자가 수신된 푸시 메시지를 클릭할 때마다 브로드캐스트 수신기의 `public void onNotificationClicked(Context context, String title, String description, String customContentString)` 메서드가 호출됩니다. 매개변수 `customContentString`에는 JSON 형식의 추가 항목이 포함되어 있습니다. Braze에서 보낸 모든 메시지에는 다음 두 가지 키-값 페어가 포함됩니다.

  ```json
  {
    "source": "Appboy",
    "cid": "your-campaign-Id"
  }
  ```

`onNotificationClicked`가 Baidu 수신기에서 호출될 때마다 수신기는 `customContentString`을 포함하는 [Intent](http://developer.android.com/reference/android/content/Intent.html)를 애플리케이션에 전송해야 합니다. 애플리케이션은 `customContentString`을 사용하여 클릭을 Braze에 기록합니다.

다음 샘플 코드는 `customContentString`을 Braze에 전달하고 클릭을 기록합니다.

{% tabs %}
{% tab JAVA %}

  ```java
  String customContentString = intent.getStringExtra(ChinaPushMessageReceiver.NOTIFICATION_CLICKED_KEY);
  BrazeNotificationUtils.logBaiduNotificationClick(mApplicationContext, customContentString);
  ```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val customContentString = intent.getStringExtra(ChinaPushMessageReceiver.NOTIFICATION_CLICKED_KEY)
BrazeNotificationUtils.logBaiduNotificationClick(context, customContentString)
```

{% endtab %}
{% endtabs %}

## 6단계: 추가 항목 {#step-6-extras}

Braze에서 사용하는 예약 키 외에도 매개변수 `customContentString`에는 사용자가 정의한 모든 커스텀 키-값 페어가 포함됩니다. 키-값 페어를 추출하려면 `customContentString`을 JSONObject로 감싸고 추가 항목을 검색합니다.

{% tabs %}
{% tab JAVA %}

```java
try {
  JSONObject myExtras = new JSONObject(customContentString);
  String myValue = myExtras.optString("my_key", null);
} catch (Exception e) {
  Log.e(TAG, "Caught an exception processing customContentString");
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
try {
  val myExtras = JSONObject(customContentString)
  val myValue = myExtras.optString("my_key", null)
} catch (e: Exception) {
  Log.e(TAG, "Caught an exception processing customContentString", e)
}
```

{% endtab %}
{% endtabs %}

## 7단계: Baidu 키 설정 {#step-7-set-up-baidu-keys}

Baidu API 키와 Baidu 비밀 키를 Braze 대시보드에 입력해야 합니다. 두 키 모두 Baidu 애플리케이션 콘솔에서 확인할 수 있습니다.

**설정 관리** 페이지에서 Android China 앱을 선택하고 푸시 알림 섹션에 Baidu API 키와 Baidu 비밀 키를 입력합니다.

![]({% image_buster /assets/img_archive/baidu_api_key.png %} "APIKey"){: style="max-width:80%;"}

## 추가 리소스 {#additional-resources}

- [Baidu 포털](https://www.baidu.com/)
- [Baidu 개발자 포털](http://developer.baidu.com/)
- [Baidu 프로젝트 포털](http://developer.baidu.com/console#app/project)
- [Baidu 푸시 SDK 포털](http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk)
- [Baidu 통합 설명서](http://developer.baidu.com/wiki/index.php?title=docs/frontia/guide-android/overview)