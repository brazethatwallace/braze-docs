---
nav_title: 푸시 알림
article_title: Windows 유니버설용 푸시 알림
platform: Windows Universal
page_order: 1
description: "이 문서에서는 Windows 유니버설 플랫폼에 대한 푸시 알림 통합 지침에 대해 설명합니다."
channel: push
hidden: true
---

# 푸시 알림 통합 {#push-notification-integration}
{% multi_lang_include archive/windows_deprecation.md %}

![Windows 유니버설 푸시 예제입니다.]({% image_buster /assets/img_archive/windows_uni_push_sample.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

푸시 알림은 중요한 업데이트가 발생하면 사용자 화면에 표시되는 앱 외 알림입니다. 푸시 알림은 사용자에게 시의적절하고 관련성 높은 콘텐츠를 제공하거나 앱에 다시 참여하도록 유도할 수 있는 유용한 방법입니다.

추가 모범 사례는 [설명서]({{site.baseurl}}/user_guide/channels/push/best_practices/)를 참조하세요.

## 1단계: 푸시를 위한 애플리케이션 구성 {#step-1-configure-your-application-for-push}

`Package.appxmanifest` 파일에 다음 설정이 구성되어 있는지 확인합니다:

**Application** 탭에서 `Toast Capable`이 `YES`로 설정되어 있는지 확인합니다.

## 2단계: Braze 대시보드 구성 {#step-2-configure-the-braze-dashboard}

1. [SID 및 클라이언트 시크릿 찾기](http://msdn.microsoft.com/en-us/library/windows/apps/hh465407.aspx)
2. Braze 대시보드의 **Settings** 페이지에서 설정에 SID와 클라이언트 시크릿을 추가합니다.<br>![]({% image_buster /assets/img_archive/windows_sid.png %} "Windows SID dashboard")

## 3단계: 백그라운드 오픈 로깅 업데이트 {#step-3-update-for-background-open-logging}

`OnLaunched` 메서드에서 `OpenSession`을 호출한 후 다음 코드 스니펫을 추가합니다.

```
string campaignId = e.Arguments.Split(new[] { "_ab_pn_cid" }, StringSplitOptions.None)[0];
if (!string.IsNullOrEmpty(campaignId))
{
Appboy.SharedInstance.PushManager.LogPushNotificationOpened(campaignId);
}
```

## 4단계: 이벤트 핸들러 만들기 {#step-4-creating-event-handlers}

푸시가 수신되고 활성화(사용자가 클릭)될 때 발생하는 이벤트를 수신하려면 이벤트 핸들러를 만들어 `PushManager` 이벤트에 추가합니다:

- `Appboy.SharedInstance.PushManager.PushReceivedEvent += YourPushReceivedEventHandler;`
- `Appboy.SharedInstance.PushManager.ToastActivatedEvent += YourToastActivatedEventHandler;`

이벤트 핸들러의 서명은 다음과 같아야 합니다:

- `void YourPushReceivedEventHandler(PushNotificationChannel sender, AppboyPushNotificationReceivedEventArgs args);`
- `void YourToastActivatedEventHandler(ToastNotification sender, AppboyToastActivatedEventArgs args);`

## 5단계: 푸시에서 앱으로 딥링킹 {#step-5-deep-linking-from-push-into-your-app}

### 1부: 앱용 딥링크 만들기 {#part-1-creating-deep-links-for-your-app}

딥링크는 애플리케이션 외부의 사용자를 애플리케이션의 특정 화면이나 페이지로 바로 이동시키는 데 사용됩니다. 일반적으로 운영체제에 URL 체계(예: myapp://mypage)를 등록하고 해당 체계를 처리하도록 애플리케이션을 등록한 다음, OS가 해당 형식의 URL을 열도록 요청하면 애플리케이션으로 제어권을 이전합니다.

WNS 딥링크 지원은 사용자를 전송할 위치에 대한 데이터와 함께 애플리케이션을 실행하므로 이와 다릅니다. WNS 푸시가 생성되면 푸시를 클릭하고 애플리케이션이 열릴 때 애플리케이션의 `OnLaunched`로 전달되는 실행 문자열이 포함될 수 있습니다. 이 실행 문자열은 이미 Campaign 추적에 사용되고 있으며, 사용자가 앱이 실행될 때 구문 분석하여 사용자를 탐색하는 데 사용할 수 있는 자체 데이터를 추가할 수 있는 기능을 제공합니다.

대시보드 또는 REST API에서 추가 실행 문자열을 지정하는 경우, 생성하는 실행 문자열의 끝에 "abextras=" 키 뒤에 추가됩니다. 따라서 실행 문자열의 예는 `ab_cn_id=_trackingid_abextras=page=settings`와 같으며, 여기서 추가 실행 문자열 매개변수에 `page=settings`를 지정하면 이를 구문 분석하여 사용자를 설정 페이지로 안내할 수 있습니다.

### 2부: 대시보드를 통한 딥링킹 {#part-2-deep-linking-through-the-dashboard}

푸시 알림 설정의 "Additional Launch String Configuration" 필드에서 실행 문자열에 추가할 문자열을 지정합니다.

![]({% image_buster /assets/img_archive/windows_deep_link_click_action.png %} "Deep Link Click Action")

### 3부: REST API를 통한 딥링킹 {#part-3-deep-linking-through-the-rest-api}

Braze에서는 REST API를 통해 딥링크를 전송할 수도 있습니다. [Windows 유니버설 푸시 오브젝트]({{site.baseurl}}/api/objects_filters/)는 선택 사항인 `extra_launch_string` 매개변수를 허용합니다.