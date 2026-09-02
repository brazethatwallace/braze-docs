# 기능 플래그 만들기 {#create-feature-flags}

> 기능 플래그를 사용하면 선택한 사용자에 대해 원격으로 기능을 활성화 또는 비활성화할 수 있습니다. Braze 대시보드 내에서 새 기능 플래그를 만듭니다. 이 기능을 활성화할 사용자의 이름과 `ID`, 타겟 오디언스 및 비율을 입력합니다. 그런 다음, 앱이나 웹사이트의 코드에서 동일한 `ID`를 사용하여 비즈니스 로직의 특정 부분을 조건부로 실행할 수 있습니다. 기능 플래그와 Braze에서 기능 플래그를 사용하는 방법에 대해 자세히 알아보려면 [기능 플래그 정보]({{site.baseurl}}/developer_guide/feature_flags)를 참조하세요.

## 사전 준비 사항 {#prerequisites}

### SDK 버전 {#sdk-version}

기능 플래그를 사용하려면 SDK가 최소 다음 버전 이상으로 업데이트되어 있어야 합니다:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

### Braze 권한 {#braze-permissions}

대시보드에서 기능 플래그를 관리하려면 관리자이거나, 다음 [권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)이 있어야 합니다:

| 권한                                                                    | 수행할 수 있는 작업                           |
|-------------------------------------------------------------------------------|-------------------------------------------|
| **Manage Feature Flags**                                                      | 기능 플래그를 보고, 생성하고, 편집합니다.     |
| **Access Campaigns, Canvases, Cards, Feature Flags, Segments, Media Library** | 사용 가능한 기능 플래그 목록을 확인합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze 권한" }

## 기능 플래그 만들기 {#creating-a-feature-flag}

### 1단계: 새 기능 플래그 만들기 {#step-1-create-a-new-feature-flag}

**메시징** > **Feature Flags**로 이동하여 **기능 플래그 만들기**를 선택합니다.

![기존 기능 플래그를 보여주는 데이터 테이블과 새 기능 플래그를 만드는 방법.]({% image_buster /assets/img/feature_flags/create_ff.png %}){: style="max-width:75%"}

### 2단계: 세부 정보 입력 {#step-2-fill-out-the-details}

**기능 플래그 세부 정보**에서 기능 플래그의 이름, ID, 설명을 입력합니다.

![이름, ID, 설명 및 속성정보를 기능 플래그에 추가할 수 있는 양식.]({% image_buster /assets/img/feature_flags/create_ff_properties.png %}){: style="max-width:75%"}


| 필드        | 설명                                                                |
|--------------|----------------------------------------------------------------------------|
| 이름         | 마케터와 관리자를 위한 사람이 읽을 수 있는 제목입니다.              |
| ID           | 코드에서 이 기능이 [사용자에 대해 활성화되었는지](#enabled) 확인하는 데 사용할 고유 ID입니다. 이 ID는 나중에 변경할 수 없으므로 계속하기 전에 [ID 명명 모범 사례](#naming-conventions)를 검토하세요. |
| 설명  | 기능 플래그에 대한 맥락을 제공하는 선택 사항 설명입니다.   |
| 속성정보   | 기능 플래그를 원격으로 구성하는 선택 사항 속성정보입니다. Canvas 단계 또는 기능 플래그 실험에서 재정의할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="2단계: 세부 정보 입력" }

### 2a단계: 커스텀 속성정보 만들기 {#step-2a-create-custom-properties}

**속성정보**에서 기능이 활성화되었을 때 앱이 Braze SDK를 통해 접근할 수 있는 커스텀 속성정보를 선택적으로 만들 수 있습니다. 각 변수에 문자열, 부울, 이미지, 타임스탬프, JSON 또는 숫자 값을 할당하고 기본값을 설정할 수 있습니다.

{% tabs local %}
{% tab 예시 %}
다음 예시에서 기능 플래그는 나열된 커스텀 속성정보를 사용하여 이커머스 스토어의 품절 배너를 표시합니다:

|속성정보 이름|유형|값|
|--|--|--|
| `banner_height`|`number`|`75`|
| `banner_color`|`string`|`blue`|
| `banner_text`|`string`|`Widgets are out of stock until July 1.`|
|`dismissible`|`boolean`|`false`|
| `homepage_icon`|`image`|`http://s3.amazonaws.com/[bucket_name]/`|
| `account_start`|`timestamp`|`2011-01-01T12:00:00Z`|
| `footer_settings`|`JSON`|`{ "colors": [ "red", "blue", "green" ], "placement": 123 }`|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="2a단계: 커스텀 속성정보 만들기" }

{% alert tip %}
추가할 수 있는 속성정보의 수에는 제한이 없습니다. 다만 기능 플래그의 속성정보는 총 10,000자로 제한됩니다.
{% endalert %}
{% endtab %}
{% endtabs %}

### 4단계: 타겟 Segments 선택 {#step-4-choose-segments-to-target}

기능 플래그를 출시하기 전에 타겟으로 할 사용자 [Segment]({{site.baseurl}}/user_guide/audience/segments)를 선택해야 합니다. 새로 만든 플래그에서 **규칙 추가**를 선택한 다음 필터 그룹 및 Segment 드롭다운 메뉴를 사용하여 타겟 오디언스에서 사용자를 필터링합니다. 여러 필터를 추가하여 오디언스를 더 좁힐 수 있습니다.

![Segments 및 필터를 추가할 수 있는 출시 트래픽이라고 표시된 텍스트 상자.]({% image_buster /assets/img/feature_flags/segmentation_ff.png %}){: style="max-width:75%;"}

### 5단계: 출시 트래픽 설정 {#rollout}

기본적으로 기능 플래그는 항상 비활성 상태이므로 기능 릴리스 날짜와 전체 사용자 활성화를 분리할 수 있습니다. 출시를 시작하려면 **출시 트래픽** 섹션의 텍스트 상자에 백분율을 입력합니다. 선택한 Segment에서 이 새 기능을 받을 무작위 사용자의 비율이 결정됩니다.

{% alert important %}
새 기능을 실제로 출시할 준비가 될 때까지 출시 트래픽을 0%보다 높게 설정하지 마세요. 대시보드에서 기능 플래그를 처음 정의할 때 이 설정을 0%로 유지하세요.
{% endalert %}

{% alert important %}
단일 규칙만으로 또는 단일 오디언스에 플래그를 출시하려면, 세분화 기준과 출시 비율을 선택하여 첫 번째 규칙을 추가합니다. 마지막으로 **Everyone Else** 규칙이 꺼져 있는지 확인하고 플래그를 저장합니다.
{% endalert %}

## 다중 규칙 기능 플래그 롤아웃 {#multi-rule-feature-flag-rollouts}

다중 규칙 기능 플래그 롤아웃을 사용하면 사용자를 평가하기 위한 규칙 시퀀스를 정의할 수 있어 정밀한 세분화와 통제된 기능 릴리스가 가능합니다. 이 방법은 다양한 오디언스에게 동일한 기능을 배포할 때 이상적입니다.

### 평가 순서 {#evaluation-order}

기능 플래그 규칙은 나열된 순서대로 위에서 아래로 평가됩니다. 사용자는 자신이 충족하는 첫 번째 규칙에 해당됩니다. 어떤 규칙에도 해당하지 않는 사용자는 기본 "Everyone Else" 규칙에 의해 자격이 결정됩니다.

### 사용자 자격 조건 {#user-qualification}

- 사용자가 첫 번째 규칙의 기준을 충족하면 즉시 기능 플래그를 받을 자격이 생깁니다.
- 사용자가 첫 번째 규칙에 해당하지 않으면 두 번째 규칙으로 평가되며, 이후 순서대로 계속됩니다.

순차적 평가는 사용자가 규칙에 해당하거나 목록 하단의 "Everyone Else" 규칙에 도달할 때까지 계속됩니다.

### "Everyone Else" 규칙 {#everyone-else-rule}

"Everyone Else" 규칙은 기본값 역할을 합니다. 사용자가 앞선 규칙 중 어디에도 해당하지 않는 경우, 기능 플래그 자격은 "Everyone Else" 규칙의 토글 설정에 의해 결정됩니다. 예를 들어, "Everyone Else" 규칙이 기본 상태에서 "Off"로 토글되어 있으면, 다른 규칙의 기준을 충족하지 않는 사용자는 세션 시작 시 기능 플래그를 받지 못합니다.

### 규칙 순서 변경 {#re-ordering-rules}

기본적으로 규칙은 생성된 순서대로 정렬되지만, 대시보드에서 드래그 앤 드롭으로 순서를 변경할 수 있습니다.

![기능 플래그에 규칙을 추가하는 방법을 보여주는 이미지.]({% image_buster /assets/img/feature_flags/add_rule.png %}){: style="max-width:80%;"}

![여러 규칙과 Everyone Else 규칙이 추가된 기능 플래그 요약을 보여주는 이미지.]({% image_buster /assets/img/feature_flags/mr_rules_overview.png %}){: style="max-width:80%;"}

### 다중 규칙 기능 플래그 사용 사례 {#multi-rule-feature-flag-use-cases}

#### 결제 페이지 점진적 릴리스 {#gradually-release-a-checkout-page}

이커머스 브랜드에서 일하면서 안정성을 확보하기 위해 다양한 지역에 걸쳐 새로운 결제 페이지를 롤아웃하려 한다고 가정해 보겠습니다. 다중 규칙 기능 플래그를 사용하면 다음과 같이 설정할 수 있습니다:

- **규칙 1:** 미국 Segment를 100%로 설정합니다.
- **규칙 2:** 브라질 사용자의 50%로 Segment를 설정하여, 모든 사용자가 한 번에 플로우를 받지 않도록 합니다.
- **규칙 3(Everyone Else):** 나머지 모든 사용자에 대해 "Everyone Else" 규칙을 켜고 15%로 설정하여, 일부 사용자가 새로운 플로우로 결제할 수 있도록 합니다.

#### 내부 테스터를 먼저 도달시키기 {#reach-internal-testers-first}

새 제품을 릴리스할 때 내부 테스터가 항상 기능 플래그를 받도록 하려는 제품 매니저라고 가정해 보겠습니다. 내부 테스터 Segment를 첫 번째 규칙에 추가하고 100%로 설정하면, 모든 기능 롤아웃에서 내부 테스터가 자격을 갖추게 됩니다.

## 기능 플래그에 "활성화됨" 필드 사용 {#enabled}

기능 플래그를 정의한 후, 특정 사용자에게 활성화되어 있는지 확인하도록 앱이나 사이트를 구성하세요. 활성화되면 사용 사례에 따라 특정 동작을 설정하거나 기능 플래그의 변수 속성정보를 참조하게 됩니다. Braze SDK는 기능 플래그의 상태와 해당 속성정보를 앱으로 가져오는 getter 메서드를 제공합니다.

세션 시작 시 기능 플래그가 자동으로 새로고침되므로 시작 시 최신 버전의 기능을 표시할 수 있습니다. SDK는 이러한 값을 캐시하여 오프라인 상태에서도 사용할 수 있도록 합니다.

{% alert note %}
[기능 플래그 노출 횟수](#impressions)를 기록해야 합니다.
{% endalert %}

앱에 새로운 유형의 고객 프로필을 배포한다고 가정합니다. `ID`를 `expanded_user_profile`로 설정할 수 있습니다. 그런 다음, 앱에서 이 새 고객 프로필을 특정 사용자에게 표시해야 하는지 확인합니다. 예를 들어:

{% tabs %}
{% tab Web %}

```javascript
const featureFlag = braze.getFeatureFlag("expanded_user_profile");
if (featureFlag?.enabled) {
  console.log(`expanded_user_profile is enabled`);
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "expanded_user_profile")
if featureFlag?.enabled == true {
  print("expanded_user_profile is enabled")
} else {
  print("expanded_user_profile is not enabled")
}
```
{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}
```java
FeatureFlag featureFlag = braze.getFeatureFlag("expanded_user_profile");
if (featureFlag != null && featureFlag.getEnabled()) {
  Log.i(TAG, "expanded_user_profile is enabled");
} else {
  Log.i(TAG, "expanded_user_profile is not enabled");
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("expanded_user_profile")
if (featureFlag?.enabled == true) {
  Log.i(TAG, "expanded_user_profile is enabled.")
} else {
  Log.i(TAG, "expanded_user_profile is not enabled.")
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
const featureFlag = await Braze.getFeatureFlag("expanded_user_profile");
if (featureFlag?.enabled) {
  console.log(`expanded_user_profile is enabled`);
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```

{% endtab %}
{% tab Unity %}
```csharp
var featureFlag = Appboy.AppboyBinding.GetFeatureFlag("expanded_user_profile");
if (featureFlag != null && featureFlag.Enabled) {
  Console.WriteLine("expanded_user_profile is enabled");
} else {
  Console.WriteLine("expanded_user_profile is not enabled");
}
```
{% endtab %}

{% tab Cordova %}
```javascript
const featureFlag = await BrazePlugin.getFeatureFlag("expanded_user_profile");
if (featureFlag?.enabled) {
  console.log(`expanded_user_profile is enabled`);
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```
{% endtab %}
{% tab Flutter %}
```dart
BrazeFeatureFlag? featureFlag = await braze.getFeatureFlagByID("expanded_user_profile");
if (featureFlag?.enabled == true) {
  print("expanded_user_profile is enabled");
} else {
  print("expanded_user_profile is not enabled");
}
```
{% endtab %}

{% tab Roku %}
```brightscript
featureFlag = m.braze.getFeatureFlag("expanded_user_profile")
if featureFlag <> invalid and featureFlag.enabled
  print "expanded_user_profile is enabled"
else
  print "expanded_user_profile is not enabled"
end if
```
{% endtab %}
{% endtabs %}

### 기능 플래그 노출 횟수 기록 {#impressions}

사용자가 새 기능과 상호 작용할 기회가 있었을 때 또는 기능이 비활성화되었을 때 상호 작용__할 수__ 있었던 경우(A/B 테스트 대조군의 경우) 기능 플래그 노출 횟수를 추적합니다. 기능 플래그 노출은 세션당 한 번만 기록됩니다.

일반적으로 앱에서 기능 플래그를 참조하는 위치 바로 아래에 이 코드 줄을 넣으면 됩니다:

{% tabs %}
{% tab Web %}

```javascript
braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Swift %}

```swift
braze.featureFlags.logFeatureFlagImpression(id: "expanded_user_profile")
```

{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

```java
braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
braze.logFeatureFlagImpression("expanded_user_profile")
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
Braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Unity %}

```csharp
Appboy.AppboyBinding.LogFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Cordova %}
```javascript
BrazePlugin.logFeatureFlagImpression("expanded_user_profile");
```
{% endtab %}
{% tab Flutter %}
```dart
braze.logFeatureFlagImpression("expanded_user_profile");
```
{% endtab %}
{% tab Roku %}
```brightscript
m.Braze.logFeatureFlagImpression("expanded_user_profile");
```
{% endtab %}
{% endtabs %}

### 속성정보에 액세스 {#accessing-properties}

기능 플래그의 속성정보에 액세스하려면 대시보드에서 정의한 유형에 따라 다음 메서드 중 하나를 사용합니다.

제공한 키에 대해 해당 유형의 속성정보가 없으면 이러한 메서드는 `null`을 반환합니다.

{% tabs %}
{% tab Web %}

```javascript
// Returns the Feature Flag instance
const featureFlag = braze.getFeatureFlag("expanded_user_profile");

// Returns the String property
const stringProperty = featureFlag.getStringProperty("color");

// Returns the boolean property
const booleanProperty = featureFlag.getBooleanProperty("expanded");

// Returns the number property
const numberProperty = featureFlag.getNumberProperty("height");

// Returns the Unix UTC millisecond timestamp property as a number
const timestampProperty = featureFlag.getTimestampProperty("account_start");

// Returns the image property as a String of the image URL
const imageProperty = featureFlag.getImageProperty("homepage_icon");

// Returns the JSON object property as a FeatureFlagJsonPropertyValue
const jsonProperty = featureFlag.getJsonProperty("footer_settings");
```

{% endtab %}
{% tab Swift %}

```swift
// Returns the Feature Flag instance
let featureFlag: FeatureFlag = braze.featureFlags.featureFlag(id: "expanded_user_profile")

// Returns the string property
let stringProperty: String? = featureFlag.stringProperty(key: "color")

// Returns the boolean property
let booleanProperty: Bool? = featureFlag.boolProperty(key: "expanded")

// Returns the number property as a double
let numberProperty: Double? = featureFlag.numberProperty(key: "height")

// Returns the Unix UTC millisecond timestamp property as an integer
let timestampProperty: Int? = featureFlag.timestampProperty(key: "account_start")

// Returns the image property as a String of the image URL
let imageProperty: String? = featureFlag.imageProperty(key: "homepage_icon")

// Returns the JSON object property as a [String: Any] dictionary
let jsonObjectProperty: [String: Any]? = featureFlag.jsonObjectProperty(key: "footer_settings")
```

{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

```java
// Returns the Feature Flag instance
FeatureFlag featureFlag = braze.getFeatureFlag("expanded_user_profile");

// Returns the String property
String stringProperty = featureFlag.getStringProperty("color");

// Returns the boolean property
Boolean booleanProperty = featureFlag.getBooleanProperty("expanded");

// Returns the number property
Number numberProperty = featureFlag.getNumberProperty("height");

// Returns the Unix UTC millisecond timestamp property as a long
Long timestampProperty = featureFlag.getTimestampProperty("account_start");

// Returns the image property as a String of the image URL
String imageProperty = featureFlag.getImageProperty("homepage_icon");

// Returns the JSON object property as a JSONObject
JSONObject jsonObjectProperty = featureFlag.getJSONProperty("footer_settings");
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
// Returns the Feature Flag instance
val featureFlag = braze.getFeatureFlag("expanded_user_profile")

// Returns the String property
val stringProperty: String? = featureFlag.getStringProperty("color")

// Returns the boolean property
val booleanProperty: Boolean? = featureFlag.getBooleanProperty("expanded")

// Returns the number property
val numberProperty: Number? = featureFlag.getNumberProperty("height")

// Returns the Unix UTC millisecond timestamp property as a long
val timestampProperty: Long? = featureFlag.getTimestampProperty("account_start")

// Returns the image property as a String of the image URL
val imageProperty: String?  = featureFlag.getImageProperty("homepage_icon")

// Returns the JSON object property as a JSONObject
val jsonObjectProperty: JSONObject? = featureFlag.getJSONProperty("footer_settings")
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
// Returns the String property
const stringProperty = await Braze.getFeatureFlagStringProperty("expanded_user_profile", "color");

// Returns the boolean property
const booleanProperty = await Braze.getFeatureFlagBooleanProperty("expanded_user_profile", "expanded");

// Returns the number property
const numberProperty = await Braze.getFeatureFlagNumberProperty("expanded_user_profile", "height");

// Returns the Unix UTC millisecond timestamp property as a number
const timestampProperty = await Braze.getFeatureFlagTimestampProperty("expanded_user_profile", "account_start");

// Returns the image property as a String of the image URL
const imageProperty = await Braze.getFeatureFlagImageProperty("expanded_user_profile", "homepage_icon");

// Returns the JSON object property as an object
const jsonObjectProperty = await Braze.getFeatureFlagJSONProperty("expanded_user_profile", "footer_settings");
```

{% endtab %}
{% tab Unity %}

```csharp
// Returns the Feature Flag instance
var featureFlag = Appboy.AppboyBinding.GetFeatureFlag("expanded_user_profile");

// Returns the String property
var stringProperty = featureFlag.GetStringProperty("color");

// Returns the boolean property
var booleanProperty = featureFlag.GetBooleanProperty("expanded");

// Returns the number property as an integer
var integerProperty = featureFlag.GetIntegerProperty("height");

// Returns the number property as a double
var doubleProperty = featureFlag.GetDoubleProperty("height");

// Returns the Unix UTC millisecond timestamp property as a long
var timestampProperty = featureFlag.GetTimestampProperty("account_start");

// Returns the image property as a String of the image URL
var imageProperty = featureFlag.GetImageProperty("homepage_icon");

// Returns the JSON object property as a JSONObject
var jsonObjectProperty = featureFlag.GetJSONProperty("footer_settings");
```

{% endtab %}
{% tab Cordova %}

```javascript
// Returns the String property
const stringProperty = await BrazePlugin.getFeatureFlagStringProperty("expanded_user_profile", "color");

// Returns the boolean property
const booleanProperty = await BrazePlugin.getFeatureFlagBooleanProperty("expanded_user_profile", "expanded");

// Returns the number property
const numberProperty = await BrazePlugin.getFeatureFlagNumberProperty("expanded_user_profile", "height");

// Returns the Unix UTC millisecond timestamp property as a number
const timestampProperty = await BrazePlugin.getFeatureFlagTimestampProperty("expanded_user_profile", "account_start");

// Returns the image property as a String of the image URL
const imageProperty = await BrazePlugin.getFeatureFlagImageProperty("expanded_user_profile", "homepage_icon");

// Returns the JSON object property as an object
const jsonObjectProperty = await BrazePlugin.getFeatureFlagJSONProperty("expanded_user_profile", "footer_settings");
```

{% endtab %}
{% tab Flutter %}

```dart
// Returns the Feature Flag instance
BrazeFeatureFlag featureFlag = await braze.getFeatureFlagByID("expanded_user_profile");

// Returns the String property
var stringProperty = featureFlag.getStringProperty("color");

// Returns the boolean property
var booleanProperty = featureFlag.getBooleanProperty("expanded");

// Returns the number property
var numberProperty = featureFlag.getNumberProperty("height");

// Returns the Unix UTC millisecond timestamp property as an integer
var timestampProperty = featureFlag.getTimestampProperty("account_start");

// Returns the image property as a String of the image URL
var imageProperty = featureFlag.getImageProperty("homepage_icon");

// Returns the JSON object property as a Map<String, dynamic> collection
var jsonObjectProperty = featureFlag.getJSONProperty("footer_settings");
```

{% endtab %}
{% tab Roku %}

```brightscript
' Returns the String property
color = featureFlag.getStringProperty("color")

' Returns the boolean property
expanded = featureFlag.getBooleanProperty("expanded")

' Returns the number property
height = featureFlag.getNumberProperty("height")

' Returns the Unix UTC millisecond timestamp property
account_start = featureFlag.getTimestampProperty("account_start")

' Returns the image property as a String of the image URL
homepage_icon = featureFlag.getImageProperty("homepage_icon")

' Returns the JSON object property
footer_settings = featureFlag.getJSONProperty("footer_settings")
```

{% endtab %}
{% endtabs %}

### 모든 기능 플래그 목록 가져오기 {#get-list-of-flags}

{% tabs %}
{% tab Web %}

```javascript
const features = getAllFeatureFlags();
for(const feature of features) {
  console.log(`Feature: ${feature.id}`, feature.enabled);
}
```

{% endtab %}
{% tab Swift %}

```swift
let features = braze.featureFlags.featureFlags
for let feature in features {
  print("Feature: \(feature.id)", feature.enabled)
}
```

{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

```java
List<FeatureFlag> features = braze.getAllFeatureFlags();
for (FeatureFlag feature: features) {
  Log.i(TAG, "Feature: ", feature.getId(), feature.getEnabled());
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
val featureFlags = braze.getAllFeatureFlags()
featureFlags.forEach { feature ->
  Log.i(TAG, "Feature: ${feature.id} ${feature.enabled}")
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
const features = await Braze.getAllFeatureFlags();
for(const feature of features) {
  console.log(`Feature: ${feature.id}`, feature.enabled);
}
```

{% endtab %}
{% tab Unity %}

```csharp
List<FeatureFlag> features = Appboy.AppboyBinding.GetAllFeatureFlags();
foreach (FeatureFlag feature in features) {
  Console.WriteLine("Feature: {0} - enabled: {1}", feature.ID, feature.Enabled);
}
```

{% endtab %}
{% tab Cordova %}
```javascript
const features = await BrazePlugin.getAllFeatureFlags();
for(const feature of features) {
  console.log(`Feature: ${feature.id}`, feature.enabled);
}
```
{% endtab %}
{% tab Flutter %}
```dart
List<BrazeFeatureFlag> featureFlags = await braze.getAllFeatureFlags();
featureFlags.forEach((feature) {
  print("Feature: ${feature.id} ${feature.enabled}");
});
```
{% endtab %}
{% tab Roku %}
```brightscript
features = m.braze.getAllFeatureFlags()
for each feature in features
      print "Feature: " + feature.id + " enabled: " + feature.enabled.toStr()
end for
```
{% endtab %}
{% endtabs %}

### 기능 플래그 새로고침 {#refreshing}

세션 도중에 현재 사용자의 기능 플래그를 새로고침하여 Braze에서 최신 값을 가져올 수 있습니다.

{% alert tip %}
세션이 시작되면 새로고침이 자동으로 수행됩니다. 새로고침은 결제 페이지를 로드하기 전과 같이 중요한 사용자 동작 전이나 기능 플래그가 참조될 것을 알고 있는 경우에만 필요합니다.
{% endalert %}

{% tabs %}
{% tab Web %}

```javascript
braze.refreshFeatureFlags(() => {
  console.log(`Feature flags have been refreshed.`);
}, () => {
  console.log(`Failed to refresh feature flags.`);
});
```

{% endtab %}
{% tab Swift %}

```swift
braze.featureFlags.requestRefresh { result in
  switch result {
  case .success(let features):
    print("Feature flags have been refreshed:", features)
  case .failure(let error):
    print("Failed to refresh feature flags:", error)
  }
}
```

{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

```java
braze.refreshFeatureFlags();
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
braze.refreshFeatureFlags()
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
Braze.refreshFeatureFlags();
```

{% endtab %}
{% tab Unity %}

```csharp
Appboy.AppboyBinding.RefreshFeatureFlags();
```

{% endtab %}
{% tab Cordova %}
```javascript
BrazePlugin.refreshFeatureFlags();
```
{% endtab %}
{% tab Flutter %}
```dart
braze.refreshFeatureFlags();
```
{% endtab %}
{% tab Roku %}
```brightscript
m.Braze.refreshFeatureFlags()
```
{% endtab %}
{% endtabs %}

### 변경 사항 수신 대기 {#updates}

SDK가 기능 플래그를 새로고침할 때 앱을 수신 대기하고 업데이트하도록 Braze SDK를 구성할 수 있습니다.

사용자가 더 이상 기능을 사용할 자격이 없는 경우 앱을 업데이트하려는 때에 유용합니다. 예를 들어, 기능의 활성화 여부 또는 속성정보 값 중 하나를 기반으로 앱에서 일부 상태를 설정하는 경우가 이에 해당합니다.

{% tabs %}
{% tab Web %}

```javascript
// Register an event listener
const subscriptionId = braze.subscribeToFeatureFlagsUpdates((features) => {
  console.log(`Features were updated`, features);
});
// Unregister this event listener
braze.removeSubscription(subscriptionId);
```

{% endtab %}
{% tab Swift %}

```swift
// Create the feature flags subscription
// - You must keep a strong reference to the subscription to keep it active
let subscription = braze.featureFlags.subscribeToUpdates { features in
  print("Feature flags were updated:", features)
}
// Cancel the subscription
subscription.cancel()
```

{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

```java
braze.subscribeToFeatureFlagsUpdates(event -> {
  Log.i(TAG, "Feature flags were updated.");
  for (FeatureFlag feature: event.getFeatureFlags()) {
    Log.i(TAG, "Feature: ", feature.getId(), feature.getEnabled());
  }
});
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
braze.subscribeToFeatureFlagsUpdates() { event ->
  Log.i(TAG, "Feature flags were updated.")
  event.featureFlags.forEach { feature ->
    Log.i(TAG, "Feature: ${feature.id}")
  }
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
// Register an event listener
Braze.addListener(braze.Events.FEATURE_FLAGS_UPDATED, (featureFlags) => {
  console.log(`featureFlagUpdates`, JSON.stringify(featureFlags));
});
```

{% endtab %}
{% tab Unity %}

변경 사항을 수신 대기하려면 **Braze 구성** > **기능 플래그**에서 **게임 오브젝트 이름** 및 **콜백 메서드 이름** 값을 애플리케이션의 해당 값으로 설정합니다.

{% endtab %}
{% tab Cordova %}
```javascript
// Register an event listener
BrazePlugin.subscribeToFeatureFlagUpdates((featureFlags) => {
    console.log(`featureFlagUpdates`, JSON.stringify(featureFlags));
});
```
{% endtab %}
{% tab Flutter %}

앱의 Dart 코드에서 다음 샘플 코드를 사용합니다:

```dart
// Create stream subscription
StreamSubscription featureFlagsStreamSubscription;

featureFlagsStreamSubscription = braze.subscribeToFeatureFlags((featureFlags) {
  print("Feature flags were updated");
});

// Cancel stream subscription
featureFlagsStreamSubscription.cancel();
```

{% subtabs %}
{% subtab Flutter SDK 18.0.0+ %}

기능 플래그 데이터는 Android 및 iOS 네이티브 레이어 모두에서 자동으로 전달됩니다. 추가 설정이 필요하지 않습니다.

{% endsubtab %}
{% subtab Flutter SDK 17.1.0 이하 %}

Flutter SDK 17.1.0 이하를 사용하는 경우, iOS 네이티브 레이어에서의 기능 플래그 데이터 전달에는 수동 설정이 필요합니다. 애플리케이션에 `BrazePlugin.processFeatureFlags(featureFlags)`를 호출하는 `featureFlags.subscribeToUpdates` 콜백이 포함되어 있을 수 있습니다. Flutter SDK 18.0.0으로 마이그레이션하려면 `BrazePlugin.processFeatureFlags(_:)` 호출을 제거하세요. 데이터 전달이 이제 자동으로 처리됩니다.

예시는 Braze Flutter SDK 샘플 애플리케이션의 [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift)를 참조하세요.

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% tab Roku %}
```brightscript
' Define a function called `onFeatureFlagChanges` to be called when feature flags are refreshed
m.BrazeTask.ObserveField("BrazeFeatureFlags", "onFeatureFlagChanges")
```
{% endtab %}

{% tab React Hook %}
```typescript
import { useEffect, useState } from "react";
import {
  FeatureFlag,
  getFeatureFlag,
  removeSubscription,
  subscribeToFeatureFlagsUpdates,
} from "@braze/web-sdk";

export const useFeatureFlag = (id: string): FeatureFlag => {
  const [featureFlag, setFeatureFlag] = useState<FeatureFlag>(
    getFeatureFlag(id)
  );

  useEffect(() => {
    const listener = subscribeToFeatureFlagsUpdates(() => {
      setFeatureFlag(getFeatureFlag(id));
    });
    return () => {
      removeSubscription(listener);
    };
  }, [id]);

  return featureFlag;
};
```
{% endtab %}
{% endtabs %}

## 사용자 자격 확인 {#checking-user-eligibility}

Braze에서 사용자가 어떤 기능 플래그에 대해 자격이 있는지 확인하려면 **오디언스** > **사용자 검색**으로 이동한 다음 사용자를 검색하고 선택합니다.

**기능 플래그 자격** 탭에서 플랫폼, 애플리케이션 또는 기기별로 자격이 있는 기능 플래그 목록을 필터링할 수 있습니다. 또한 기능 플래그 옆에 있는 <i class="fa-solid fa-eye" aria-label="미리보기"></i>를 선택하여 사용자에게 반환될 페이로드를 미리 볼 수 있습니다.

![사용자가 자격이 있는 기능 플래그 테이블을 보여주는 이미지.]({% image_buster /assets/img/feature_flags/eligibility.png %}){: style="max-width:85%;"}

## 체인지로그 보기 {#viewing-the-changelog}

기능 플래그의 체인지로그를 보려면 기능 플래그를 열고 **Changelog**를 선택합니다.

![기능 플래그의 "편집" 페이지에서 "Changelog" 버튼이 강조 표시된 모습.]({% image_buster /assets/img/feature_flags/changelog/open_changelog.png %}){: style="max-width:60%;"}

여기에서 변경이 발생한 시점, 변경한 사람, 해당 카테고리 등을 확인할 수 있습니다.

![선택한 기능 플래그의 체인지로그.]({% image_buster /assets/img/feature_flags/changelog/changelog.png %}){: style="max-width:90%;"}

## 기능 플래그로 세분화 {#segmentation}

Braze는 현재 어떤 사용자가 기능 플래그를 활성화했는지 자동으로 추적합니다. [**기능 플래그** 필터]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#feature-flags)를 사용하여 Segment 또는 타겟 메시징을 생성할 수 있습니다. Segment 필터링에 대한 자세한 내용은 [Segment 생성]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)을 참조하세요.

![필터 검색창에 "기능 플래그"가 입력된 필터 섹션.]({% image_buster /assets/img/feature_flags/feature-flags-filter-name.png %}){: style="max-width:75%;"}

{% alert note %}
재귀 Segment를 방지하기 위해 다른 기능 플래그를 참조하는 Segment를 생성할 수 없습니다.
{% endalert %}

## 모범 사례 {#best-practices}

### 롤아웃을 Canvases나 실험과 결합하지 마세요 {#dont-combine-rollouts-with-canvases-or-experiments}

사용자가 서로 다른 진입점에 의해 활성화되거나 비활성화되는 것을 방지하려면, 롤아웃 슬라이더를 0보다 큰 값으로 설정하거나 Canvas 또는 실험에서 기능 플래그를 활성화해야 합니다. 모범 사례로, Canvas 또는 실험에서 기능 플래그를 사용할 계획이라면 롤아웃 비율을 0으로 유지하세요.

### 명명 규칙 {#naming-conventions}

코드를 명확하고 일관성 있게 유지하려면 기능 플래그 ID의 이름을 지정할 때 다음 형식을 사용하는 것을 고려하세요:

```plaintext
BEHAVIOR_PRODUCT_FEATURE
```

각 항목을 다음과 같이 대체합니다:

| 입력 안내 | 설명 |
|-------------|---------------------------------------------------------------------------------------------------------------------------|
| `BEHAVIOR`  | 기능의 동작입니다. 코드에서 동작이 기본적으로 비활성화되어 있는지 확인하고, 기능 플래그 이름에 `disabled`와 같은 문구를 사용하지 마세요. |
| `PRODUCT`   | 기능이 속한 제품입니다.                                                                                       |
| `FEATURE`    | 기능의 이름입니다.                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="명명 규칙" }

다음은 `show`가 동작, `animation_profile`이 제품, `driver`가 기능인 기능 플래그 예시입니다:

```plaintext
show_animation_profile_driver
```

### 미리 계획하기 {#planning-ahead}

항상 안전하게 진행하세요. 끄기 스위치가 필요할 수 있는 새로운 기능을 고려할 때, 기능 플래그와 함께 새 코드를 릴리스하고 필요하지 않은 것이 새 앱 업데이트가 필요하다는 것을 나중에 깨닫는 것보다 낫습니다.

### 설명을 자세히 작성하세요 {#be-descriptive}

기능 플래그에 설명을 추가하세요. Braze에서 선택 필드이지만, 사용 가능한 기능 플래그를 탐색할 때 다른 사람들이 가질 수 있는 질문에 답하는 데 도움이 될 수 있습니다.

- 이 플래그의 활성화 및 동작을 담당하는 사람의 연락처 정보
- 이 플래그를 비활성화해야 하는 시기
- 이 플래그가 제어하는 새로운 기능에 대한 설명서 또는 메모 링크
- 기능 사용 방법에 대한 종속성 또는 참고 사항

### 오래된 기능 플래그 정리하기 {#clean-up-old-feature-flags}

누구나 필요 이상으로 오랫동안 100% 롤아웃 상태로 기능을 방치한 경험이 있습니다.

코드(및 Braze 대시보드)를 깔끔하게 유지하려면, 모든 사용자가 업그레이드를 완료하고 기능을 비활성화할 필요가 더 이상 없는 경우 코드베이스에서 영구 기능 플래그를 제거하세요. 이렇게 하면 개발 환경의 복잡성을 줄이는 데 도움이 될 뿐만 아니라, 기능 플래그 목록도 깔끔하게 유지됩니다.