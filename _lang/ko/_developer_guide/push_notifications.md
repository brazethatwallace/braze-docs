---
nav_title: 푸시 알림
article_title: "Braze SDK용 푸시 알림"
page_order: 2.3
description: "이 랜딩 페이지에서는 푸시 알림에 관한 모든 것을 확인할 수 있습니다."
---

# 푸시 알림 {#push-notifications}

> [푸시 알림]({{site.baseurl}}/user_guide/channels/push/)을 사용하면 중요한 이벤트가 발생할 때 앱에서 알림을 보낼 수 있습니다. 전달할 새 인스턴트 메시지, 송출할 뉴스 속보 알림 또는 오프라인으로 시청할 수 있도록 다운로드할 준비가 된 사용자가 좋아하는 TV 프로그램의 최신 에피소드가 있을 때 푸시 알림을 전송할 수 있습니다. 또한 애플리케이션이 필요할 때만 실행되므로 백그라운드 가져오기보다 더 효율적입니다.

{% alert note %}
**웹 URL로 리디렉션**과 **앱 내에서 웹 URL 열기**가 선택되지 않았는데도 링크가 앱 내에서 열리는 경우, 앱이 해당 URL을 직접 처리하고 있을 수 있습니다(예: iOS의 유니버설 링크 또는 Android의 앱 링크). 브라우저에서 링크를 열려면, 사용자가 알림을 탭할 때 앱이 해당 URL을 시스템 브라우저로 위임하는지 확인하거나, 클릭 동작이 Braze 대시보드 설정과 일치하도록 앱의 URL 처리 방식을 조정하세요. 클릭 동작 및 URL 처리 구성 방법은 해당 플랫폼의 푸시 설명서를 참조하세요.
{% endalert %}

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/push_notifications.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/push_notifications.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/push_notifications.md %}
{% endsdktab %}

{% sdktab android tv %}
{% multi_lang_include developer_guide/android_tv/push_notifications.md %}
{% endsdktab %}

{% sdktab cordova %}
{% multi_lang_include developer_guide/cordova/push_notifications.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/push_notifications.md %}
{% endsdktab %}

{% sdktab huawei %}
{% multi_lang_include developer_guide/huawei/push_notifications.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/push_notifications.md %}
{% endsdktab %}

{% sdktab safari %}
{% multi_lang_include developer_guide/safari/push_notifications.md %}
{% endsdktab %}

{% sdktab unity %}
{% multi_lang_include developer_guide/unity/push_notifications.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin)%}
{% multi_lang_include developer_guide/xamarin/push_notifications.md %}
{% endsdktab %}
{% endsdktabs %}