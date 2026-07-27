---
nav_title: 기능 인지도 및 새 앱 버전
article_title: 기능 인지도 및 새 앱 버전
page_order: 9
page_type: reference
description: "이 참조 문서에서는 새로운 기능이나 버전을 출시할 때 사용자에게 정보를 제공하고 기대감을 높이는 방법을 설명합니다."
tool: Campaigns

---

# 기능 인지도 및 새 앱 버전 {#feature-awareness-and-new-app-version}

> 이 참조 문서에서는 Braze 플랫폼을 사용하여 고객에게 앱의 새로운 기능과 버전에 대한 최신 정보를 제공하는 방법을 다룹니다.

앱을 지속적으로 업데이트하고 개선하기 위해 많은 노력을 기울이고 있으며, 사용자가 이러한 흥미로운 새 기능과 새 앱 버전을 경험하기를 원합니다. 사용자가 아직 사용하지 않은 새로운 기능에 대해 알리고, 앱을 탐색하여 제공하는 모든 것을 최대한 활용하도록 유도하는 방법을 알아보세요.

기능 인지도 Campaign은 앱의 기능을 계속 개선하면서 사용자가 앱에 지속적으로 참여하도록 유도하는 좋은 방법입니다. 사용자에게 최신 정보를 제공하면 활성 상태를 유지하고, 평점을 높이며, 사용자 인게이지먼트를 보장하는 데 도움이 됩니다.

## 최신 앱 버전으로 필터링 {#filtering-by-most-recent-app-versions}

Braze SDK는 사용자의 최신 앱 버전을 자동으로 추적합니다. 이러한 버전은 필터와 Segments에서 사용하여 어떤 사용자가 메시지나 Campaign을 수신해야 하는지 결정할 수 있습니다.

![Campaign 구축 워크플로의 타겟 사용자 단계에 있는 타겟팅 옵션 패널. 추가 필터 섹션에 다음 필터가 포함되어 있습니다: "Android Stopwatch(Android)의 최신 앱 버전 번호가 3.7.0(134.0.0.0) 미만".]({% image_buster /assets/img_archive/new_app_version.png %}){: style="max-width:90%;"}

{% alert note %}
현재 앱 버전이 채워지는 데 시간이 걸릴 수 있습니다. 고객 프로필의 앱 버전은 SDK가 정보를 캡처할 때 업데이트되며, 이는 사용자가 앱을 열 때에 의존합니다. 사용자가 앱을 열지 않으면 현재 버전이 업데이트되지 않습니다. <br><br> 이러한 필터는 소급 적용되지 않습니다. 현재 및 향후 버전에 대해 "초과" 또는 "같음"을 사용하는 것이 좋지만, 과거 버전 필터를 사용하면 예상치 못한 동작이 발생할 수 있습니다.
{% endalert %}

### 앱 버전 번호 {#app-version-number}

**앱 버전 번호** 필터를 사용하여 앱의 버전 및 빌드 번호별로 사용자를 세분화할 수 있습니다.

이 필터는 다양한 앱 버전을 타겟팅하기 위한 숫자 비교를 지원합니다. 예를 들어, 앱 버전 "1.2.3" "미만", "초과", "같음"인 사용자를 타겟팅할 수 있으며, 이는 앱 업그레이드가 필요한 새 기능을 홍보하는 데 유용할 수 있습니다.

이 새로운 필터는 이전의 각 버전을 명시적으로 나열하거나 정규표현식을 사용해야 했던 레거시 "앱 버전 이름" 필터를 대체할 수 있습니다.

**작동 방식**

* 앱의 앱 버전에서 전송된 `major.minor.patch` 버전의 각 부분이 정수로 비교됩니다
* 주 번호가 같으면 부 번호가 비교되는 식으로 진행됩니다.

**중요 사항**

* Android 앱에는 사람이 읽을 수 있는 [`versionName`](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName)과 내부 [`versionCode`](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode())가 모두 있습니다. 앱 버전 번호 필터는 앱 스토어 출시마다 증가가 보장되는 `versionCode`를 사용합니다.
* 앱의 `versionName`과 `versionCode`가 동기화되지 않으면 혼란이 발생할 수 있으며, 특히 두 필드 모두 Braze 대시보드에서 확인할 수 있기 때문에 더욱 그렇습니다. 모범 사례로, 앱의 `versionName`과 `versionCode`가 함께 증가하는지 확인하세요.
* 사람이 읽을 수 있는 `versionName` 필드로 필터링해야 하는 경우(드문 경우), 앱 버전 이름 필터를 사용하세요.

#### SDK 요구 사항 {#sdk-requirements}

이 필터의 값은 Braze Android SDK v3.6.0+ 및 iOS SDK v3.21.0+부터 수집됩니다. 이 필터에 SDK 요구 사항이 있지만, 이 기능을 사용하여 앱의 더 낮은(이전) 버전을 사용하는 사용자도 타겟팅할 수 있습니다!

Android의 경우, 이 버전 번호는 앱의 [Package Long Version Code](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode())를 기반으로 합니다.

iOS의 경우, 이 버전 번호는 앱의 [Short Version String](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring)을 기반으로 합니다.

{% alert tip %}
이 필터는 사용자가 지원되는 Braze SDK 버전으로 앱을 업그레이드한 후에 값이 채워집니다. 그때까지는 필터를 선택해도 버전이 표시되지 않습니다.
{% endalert %}

#### 사용 사례 {#use-case}

다음 시나리오에서는 이 필터를 지원하는 Braze SDK로 앱 버전 `2.0.0`에서 처음 업그레이드했다고 가정합니다.

Braze가 앱 버전 2.0.0의 데이터를 수신하면, 이전 또는 이후 버전의 사용자를 타겟팅할 수 있습니다.

| 필터  | 사용자의 앱 버전  | 결과 |
| :------------- | :----------- | :--------- |
| 2.0.0 미만 | 1.0.0 | Braze SDK가 "앱 버전 번호" 필터를 지원하지 않았더라도 사용자가 Segment에 포함됩니다. |
| 2.0.0 초과 | 2.5.1 | 해당 사용자와 향후 모든 설치가 Segment에 포함됩니다. |
| 2.0.0 초과 | 1.9.9 | 사용자가 Segment에 포함되지 않습니다. |
| 2.0.0 이하 | 3.0.1 | 사용자가 Segment에 포함되지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="사용 사례" }

### 앱 버전 이름 {#app-version-name}

"앱 버전 이름" 필터를 사용하여 앱의 사용자 대상 "빌드 이름"별로 사용자를 세분화할 수 있습니다.

이 필터는 "같음", "다음이 아님", 정규표현식 매칭을 지원합니다. 예를 들어, 앱 버전이 "1.2.3-test-build"가 아닌 사용자를 타겟팅할 수 있습니다.

Android의 경우, 이 버전 이름은 앱의 [Package Version Name](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName)을 기반으로 합니다. iOS의 경우, 이 버전 이름은 앱의 [Short Version String](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring)을 기반으로 합니다.

### 기능을 사용하지 않은 경우 {#have-not-used-feature}

새 앱 버전을 출시하고 새로운 기능을 도입할 때, 사용자가 새로운 콘텐츠를 인지하지 못할 수 있습니다. 기능 인지도 Campaign을 실행하면 사용자에게 새로운 기능이나 한 번도 사용하지 않은 기능에 대해 알릴 수 있는 좋은 방법입니다. 이를 위해 앱 내에서 특정 동작을 완료한 적이 없는 사용자에게 할당되는 [커스텀 속성]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)을 생성하거나, 특정 동작을 추적하는 [커스텀 이벤트]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)를 사용해야 합니다. 이 속성(또는 이벤트)을 사용하여 Campaign을 보낼 사용자를 세분화할 수 있습니다.

{% alert tip %}
오디언스의 특정 부분을 리타겟팅하고 싶으신가요? [리타겟팅 Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns)를 확인하여 사용자의 이전 행동을 활용해 Campaign을 리타겟하는 방법을 알아보세요.
{% endalert %}