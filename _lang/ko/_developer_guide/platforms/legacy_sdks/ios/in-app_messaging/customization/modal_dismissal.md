---
nav_title: 모달 해제
article_title: iOS용 인앱 메시지 모달 해제
platform: iOS
page_order: 29
description: "이 참조 문서에서는 iOS 애플리케이션의 인앱 메시징 모달 해제를 다룹니다."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 바깥쪽 탭으로 모달 닫기 {#dismiss-modal-on-outside-tap}

기본값은 `NO`입니다. 사용자가 인앱 메시지 외부를 탭할 때 모달 인앱 메시지를 해제할지 여부를 결정합니다.

외부 탭 해제를 활성화하려면 `Info.plist` 파일에 `Braze`라는 사전을 추가합니다. 다음 코드 스니펫과 같이 `Braze` 사전 내에 `DismissModalOnOutsideTap` 부울 하위 항목을 추가하고 값을 `YES`로 설정합니다. Braze iOS SDK v4.0.2 이전 버전에서는 `Braze` 대신 `Appboy` 사전 키를 사용해야 합니다.

```
<key>Braze</key>
<dict>
  <key>DismissModalOnOutsideTap</key>
  <boolean>YES</boolean>
</dict>
```

런타임에 `appboyOptions`에서 `ABKEnableDismissModalOnOutsideTapKey`를 `YES`로 설정하여 이 기능을 활성화할 수도 있습니다.

| `DismissModalOnOutsideTap` | 설명 |
|----------|-------------|
| `YES`       | 외부를 탭하면 모달 인앱 메시지가 해제됩니다.     |
| `NO`        | 기본값으로, 외부를 탭해도 모달 인앱 메시지는 해제되지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Dismiss modal on outside tap" }