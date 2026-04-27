---
nav_title: 커스텀 이벤트 추적하기
article_title: Windows 유니버설용 커스텀 이벤트 추적
platform: Windows Universal
page_order: 2
description: "이 참조 문서에서는 Windows Universal 플랫폼에서 커스텀 이벤트를 추적하는 방법에 대해 설명합니다."
hidden: true
---

# 커스텀 이벤트 추적하기 {#track-custom-events}
{% multi_lang_include archive/windows_deprecation.md %}

Braze에서 커스텀 이벤트를 기록하여 앱의 사용 패턴에 대해 자세히 알아보고 대시보드에서 사용자의 행동에 따라 세그먼트를 구성할 수 있습니다. 또한 [이벤트 이름 지정 규칙]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions/)을 숙지하는 것이 좋습니다.

모든 이벤트는 IAppboy에서 노출되는 등록정보인 `EventLogger`를 사용하여 기록됩니다. `EventLogger`에 대한 참조를 얻으려면 `Appboy.SharedInstance.EventLogger`를 호출하세요. 다음 메서드를 사용하여 중요한 사용자 행동 및 커스텀 이벤트를 추적할 수 있습니다.

```csharp
bool LogCustomEvent(string YOUR_EVENT_NAME)
```
