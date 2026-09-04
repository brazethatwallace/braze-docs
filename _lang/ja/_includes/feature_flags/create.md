# フィーチャーフラグを作成する {#create-feature-flags}

> フィーチャーフラグを使用すると、選択したユーザーに対してリモートで機能を有効または無効にすることができます。Brazeダッシュボードで新しいフィーチャーフラグを作成します。名前と`ID`、ターゲットオーディエンス、およびこの機能を有効にするユーザーの割合を指定します。その後、アプリまたはWebサイトのコードで同じ`ID`を使用して、ビジネスロジックの特定の部分を条件付きで実行できます。フィーチャーフラグおよびBrazeでの使用方法の詳細については、[フィーチャーフラグについて]({{site.baseurl}}/developer_guide/feature_flags)を参照してください。

## 前提条件 {#prerequisites}

### SDKバージョン {#sdk-version}

フィーチャーフラグを使用するには、SDKが少なくとも以下の最小バージョンに更新されていることを確認してください。

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

### Brazeの権限 {#braze-permissions}

ダッシュボードでフィーチャーフラグを管理するには、管理者であるか、以下の[権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)を持っている必要があります。

| 権限                                                                    | できること                           |
|-------------------------------------------------------------------------------|-------------------------------------------|
| **Manage Feature Flags**                                                      | フィーチャーフラグの表示、作成、編集。     |
| **Access キャンペーン, キャンバス, Cards, Feature Flags, セグメント, Media Library** | 利用可能なフィーチャーフラグのリストの表示。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Brazeの権限" }

## フィーチャーフラグの作成 {#creating-a-feature-flag}

### ステップ1：新しいフィーチャーフラグを作成する {#step-1-create-a-new-feature-flag}

**メッセージング** > **フィーチャーフラグ**に移動し、**フィーチャーフラグを作成**を選択します。

![既存のフィーチャーフラグと新しいフィーチャーフラグの作成方法を示すデータテーブル。]({% image_buster /assets/img/feature_flags/create_ff.png %}){: style="max-width:75%"}

### ステップ2：詳細を入力する {#step-2-fill-out-the-details}

**フィーチャーフラグの詳細**で、フィーチャーフラグの名前、ID、説明を入力します。

![フィーチャーフラグに名前、ID、説明、プロパティを追加できるフォーム。]({% image_buster /assets/img/feature_flags/create_ff_properties.png %}){: style="max-width:75%"}


| フィールド  | 説明                                                                       |
|--------------|----------------------------------------------------------------------------|
| 名前         | マーケターや管理者向けの、人間が読めるタイトルです。              |
| ID           | この機能がユーザーに対して[有効](#enabled)かどうかをコードで確認するために使用する一意のIDです。このIDは後から変更できないため、続行する前に[IDの命名ベストプラクティス](#naming-conventions)を確認してください。 |
| 説明         | フィーチャーフラグに関するコンテキストを提供するオプションの説明です。   |
| プロパティ   | フィーチャーフラグをリモートで設定するオプションのプロパティです。キャンバスステップやフィーチャーフラグの実験で上書きできます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ2：詳細を入力する" }

### ステップ2a：カスタムプロパティを作成する {#step-2a-create-custom-properties}

**プロパティ**で、機能が有効な場合にBraze SDKを通じてアプリがアクセスできるカスタムプロパティをオプションで作成できます。各変数には文字列、ブール値、画像、タイムスタンプ、JSON、または数値を割り当てることができ、デフォルト値を設定することもできます。

{% tabs local %}
{% tab 例 %}
次の例では、フィーチャーフラグがカスタムプロパティを使用してeコマースストアの在庫切れバナーを表示しています。

|プロパティ名|タイプ|値|
|--|--|--|
| `banner_height`|`number`|`75`|
| `banner_color`|`string`|`blue`|
| `banner_text`|`string`|`Widgets are out of stock until July 1.`|
|`dismissible`|`boolean`|`false`|
| `homepage_icon`|`image`|`http://s3.amazonaws.com/[bucket_name]/`|
| `account_start`|`timestamp`|`2011-01-01T12:00:00Z`|
| `footer_settings`|`JSON`|`{ "colors": [ "red", "blue", "green" ], "placement": 123 }`|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ2a：カスタムプロパティを作成する" }

{% alert tip %}
追加できるプロパティの数に制限はありません。ただし、フィーチャーフラグのプロパティは合計10,000文字に制限されています。
{% endalert %}
{% endtab %}
{% endtabs %}

### ステップ4：ターゲットとなるセグメントを選択する {#step-4-choose-segments-to-target}

フィーチャーフラグをロールアウトする前に、ターゲットとするユーザーの[セグメント]({{site.baseurl}}/user_guide/audience/segments)を選択する必要があります。新しく作成したフラグで**ルールを追加**を選択し、フィルターグループとセグメントのドロップダウンメニューを使用して、ターゲットオーディエンスからユーザーをフィルタリングします。複数のフィルターを追加して、オーディエンスをさらに絞り込むことができます。

![セグメントとフィルターを追加できるロールアウトトラフィックというラベルのテキストボックス。]({% image_buster /assets/img/feature_flags/segmentation_ff.png %}){: style="max-width:75%;"}

### ステップ5：ロールアウトトラフィックを設定する {#rollout}

デフォルトでは、フィーチャーフラグは常に無効であり、機能リリースの日付をユーザーの全体的なアクティベーションから分離できます。ロールアウトを開始するには、**ロールアウトトラフィック**セクションでテキストボックスにパーセンテージを入力します。これにより、選択したセグメント内のランダムなユーザーの中から、この新機能を受け取るユーザーのパーセンテージが選択されます。

{% alert important %}
新機能を公開する準備ができるまで、ロールアウトトラフィックを0%より大きく設定しないでください。ダッシュボードでフィーチャーフラグを最初に定義する際は、この設定を0%のままにしてください。
{% endalert %}

{% alert important %}
1つのルールのみで、または単一のオーディエンスにフラグをロールアウトするには、セグメンテーション基準とロールアウトパーセンテージを選択して最初のルールを追加します。最後に、**Everyone Else**ルールがオフに切り替えられていることを確認し、フラグを保存します。
{% endalert %}

## マルチルールフィーチャーフラグロールアウト {#multi-rule-feature-flag-rollouts}

マルチルールフィーチャーフラグロールアウトを使用すると、ユーザーを評価するための一連のルールを定義でき、正確なセグメンテーションと制御されたフィーチャーリリースが可能になります。この方法は、同じフィーチャーを多様なオーディエンスにデプロイする場合に最適です。

### 評価順序 {#evaluation-order}

フィーチャーフラグのルールは、リストに表示されている順番で上から下に評価されます。ユーザーは、最初に一致したルールに適用されます。どのルールにも一致しない場合、そのユーザーの適格性はデフォルトの「Everyone Else」ルールによって決定されます。

### ユーザーの適格性判定 {#user-qualification}

- ユーザーが最初のルールの条件を満たした場合、そのユーザーはすぐにフィーチャーフラグを受け取る対象となります。
- ユーザーが最初のルールに該当しない場合、2番目のルールに対して評価され、以降同様に続きます。

この順次評価は、ユーザーがいずれかのルールに該当するか、リストの最下部にある「Everyone Else」ルールに到達するまで続きます。

### 「Everyone Else」ルール {#everyone-else-rule}

「Everyone Else」ルールはデフォルトとして機能します。ユーザーがそれ以前のどのルールにも該当しない場合、フィーチャーフラグの適格性は「Everyone Else」ルールのトグル設定によって決定されます。たとえば、「Everyone Else」ルールがデフォルト状態で「Off」にトグルされている場合、他のルールの条件を満たさないユーザーはセッション開始時にフィーチャーフラグを受け取りません。

### ルールの並べ替え {#re-ordering-rules}

デフォルトでは、ルールは作成された順序で並べられますが、ダッシュボードでドラッグ＆ドロップして並べ替えることができます。

![フィーチャーフラグにルールを追加する画面。]({% image_buster /assets/img/feature_flags/add_rule.png %}){: style="max-width:80%;"}

![複数のルールとEveryone Elseルールが追加されたフィーチャーフラグのサマリー画面。]({% image_buster /assets/img/feature_flags/mr_rules_overview.png %}){: style="max-width:80%;"}

### マルチルールフィーチャーフラグのユースケース {#multi-rule-feature-flag-use-cases}

#### チェックアウトページを段階的にリリースする {#gradually-release-a-checkout-page}

eコマースブランドで働いていて、安定性を確保しながら異なる地域に新しいチェックアウトページをロールアウトしたいとします。マルチルールフィーチャーフラグを使用して、以下のように設定できます。

- **ルール1：** 米国セグメントを100%に設定します。
- **ルール2：** ブラジルのユーザーの50%にセグメントを設定し、全員が一度にフローを受け取らないようにします。
- **ルール3（Everyone Else）：** その他すべてのユーザーに対して、「Everyone Else」ルールをオンにトグルし、15%に設定します。これにより、すべてのユーザーの一部が新しいフローでチェックアウトできます。

#### 社内テスターに最初にリーチする {#reach-internal-testers-first}

プロダクトマネージャーとして、新製品をリリースする際に社内テスターが常にフィーチャーフラグを受け取るようにしたいとします。社内テスターのセグメントを最初のルールに追加し、100%に設定することで、すべてのフィーチャーロールアウトで社内テスターが対象となります。

## フィーチャーフラグの「enabled」フィールドの使用 {#enabled}

フィーチャーフラグを定義したら、アプリやサイトを設定して、特定のユーザーに対してそのフィーチャーフラグが有効かどうかを確認するようにします。有効になったら、ユースケースに応じて何らかのアクションを設定するか、フィーチャーフラグの変数プロパティを参照します。Braze SDKは、フィーチャーフラグのステータスとそのプロパティをアプリに取り込むためのゲッターメソッドを提供します。

フィーチャーフラグはセッション開始時に自動的に更新されるため、起動時に機能の最新バージョンを表示できます。SDKはこれらの値をキャッシュし、オフラインの状態でも使用できるようにします。

{% alert note %}
[フィーチャーフラグのインプレッション](#impressions)を必ず記録してください。
{% endalert %}

たとえば、アプリに新しいタイプのユーザープロファイルをロールアウトするとします。`ID`を`expanded_user_profile`に設定します。次に、この新しいユーザープロファイルを特定のユーザーに表示するかどうかをアプリで確認します。以下に例を示します。

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

### フィーチャーフラグのインプレッションをログに記録する {#impressions}

ユーザーが新しい機能を操作する機会があった場合、または機能が無効になっている場合（A/Bテストのコントロールグループの場合）にユーザーが操作した__可能性がある__場合は、フィーチャーフラグのインプレッションを追跡します。フィーチャーフラグのインプレッションは、1セッションにつき1回のみ記録されます。

通常、このコード行は、アプリ内でフィーチャーフラグを参照する場所の直下に置くことができます。

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

### プロパティにアクセスする {#accessing-properties}

フィーチャーフラグのプロパティにアクセスするには、ダッシュボードで定義したタイプに応じて、以下のメソッドのいずれかを使用します。

指定したキーに対応する型のプロパティが存在しない場合、これらのメソッドは`null`を返します。

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

### すべてのフィーチャーフラグのリストを取得する {#get-list-of-flags}

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

### フィーチャーフラグを更新する {#refreshing}

セッションの途中で現在のユーザーのフィーチャーフラグを更新して、Brazeから最新の値を取得できます。

{% alert tip %}
更新はセッション開始時に自動的に行われます。更新が必要なのは、チェックアウトページの読み込み前や、フィーチャーフラグが参照されることがわかっている場合など、重要なユーザーアクションの前だけです。
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

### 変更をリッスンする {#updates}

SDKがフィーチャーフラグを更新するときにアプリをリッスンして更新するようにBraze SDKを構成できます。

これは、ユーザーがある機能を利用できなくなった場合にアプリを更新したい場合に便利です。たとえば、ある機能が有効かどうか、またはそのプロパティ値の1つに基づいて、アプリの状態を設定する場合です。

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

変更をリッスンするには、**Braze Configuration** > **Feature Flags**の**Game Object Name**と**Callback Method Name**の値を、アプリケーションの対応する値に設定します。

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

アプリのDartコードでは、以下のサンプルコードを使用します。

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
{% subtab Flutter SDK 18.0.0以降 %}

フィーチャーフラグのデータは、AndroidとiOSの両方のネイティブレイヤーから自動的に転送されます。追加のセットアップは不要です。

{% endsubtab %}
{% subtab Flutter SDK 17.1.0以前 %}

Flutter SDK 17.1.0以前を使用している場合、iOSネイティブレイヤーからのフィーチャーフラグデータの転送には手動セットアップが必要です。アプリケーションには、`BrazePlugin.processFeatureFlags(featureFlags)`を呼び出す`featureFlags.subscribeToUpdates`コールバックが含まれている可能性があります。Flutter SDK 18.0.0に移行するには、`BrazePlugin.processFeatureFlags(_:)`の呼び出しを削除してください。データ転送は自動的に処理されるようになりました。

例については、Braze Flutter SDKサンプルアプリケーションの[AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift)を参照してください。

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

## ユーザーの適格性を確認する {#checking-user-eligibility}

Brazeでユーザーがどのフィーチャーフラグに適格であるかを確認するには、**オーディエンス** > **ユーザー検索**に移動し、ユーザーを検索して選択します。

**フィーチャーフラグの適格性**タブでは、適格なフィーチャーフラグのリストをプラットフォーム、アプリケーション、またはデバイスでフィルタリングできます。また、フィーチャーフラグの横にある<i class="fa-solid fa-eye" aria-label="プレビュー"></i>を選択すると、ユーザーに返されるペイロードをプレビューすることもできます。

![ユーザーが適格なフィーチャーフラグのテーブルを表示する画面。]({% image_buster /assets/img/feature_flags/eligibility.png %}){: style="max-width:85%;"}

## 変更履歴の表示 {#viewing-the-changelog}

フィーチャーフラグの変更履歴を表示するには、フィーチャーフラグを開き、**変更履歴**を選択します。

![フィーチャーフラグの「編集」ページ。「変更履歴」ボタンがハイライトされています。]({% image_buster /assets/img/feature_flags/changelog/open_changelog.png %}){: style="max-width:60%;"}

ここでは、変更が行われた日時、変更を行ったユーザー、変更が属するカテゴリーなどを確認できます。

![選択したフィーチャーフラグの変更履歴。]({% image_buster /assets/img/feature_flags/changelog/changelog.png %}){: style="max-width:90%;"}

## フィーチャーフラグでセグメント化する {#segmentation}

Brazeは、現在フィーチャーフラグが有効になっているユーザーを自動的に追跡します。[**フィーチャーフラグ**フィルター]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#feature-flags)を使ってセグメントまたはターゲットメッセージングを作成できます。セグメントでのフィルタリングの詳細については、[セグメントの作成]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)を参照してください。

![「フィルター」セクションで、フィルター検索バーに「フィーチャーフラグ」と入力した状態。]({% image_buster /assets/img/feature_flags/feature-flags-filter-name.png %}){: style="max-width:75%;"}

{% alert note %}
再帰的なセグメントを防ぐため、他のフィーチャーフラグを参照するセグメントを作成することはできません。
{% endalert %}

## ベストプラクティス {#best-practices}

### ロールアウトをキャンバスや実験と組み合わせない {#dont-combine-rollouts-with-canvases-or-experiments}

ユーザーが異なるエントリポイントによって有効化・無効化されることを防ぐため、ロールアウトスライダーをゼロより大きい値に設定するか、キャンバスまたは実験でフィーチャーフラグを有効にするかのどちらかにしてください。ベストプラクティスとして、キャンバスや実験でフィーチャーフラグを使用する予定がある場合は、ロールアウトの割合をゼロのままにしてください。

### 命名規則 {#naming-conventions}

コードを明確で一貫性のあるものに保つため、フィーチャーフラグIDの命名には以下の形式を検討してください。

```plaintext
BEHAVIOR_PRODUCT_FEATURE
```

以下を置き換えてください。

| プレースホルダー | 説明 |
|-------------|---------------------------------------------------------------------------------------------------------------------------|
| `BEHAVIOR`  | フィーチャーの動作です。コード内では、デフォルトで動作が無効になるようにし、フィーチャーフラグ名に`disabled`のようなフレーズを使用しないようにしてください。 |
| `PRODUCT`   | フィーチャーが属するプロダクトです。 |
| `FEATURE`    | フィーチャーの名前です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="命名規則" }

以下は、`show`が動作、`animation_profile`がプロダクト、`driver`がフィーチャーであるフィーチャーフラグの例です。

```plaintext
show_animation_profile_driver
```

### 事前に計画する {#planning-ahead}

常に安全策を取ってください。オフスイッチが必要になる可能性のある新機能を検討する際は、フィーチャーフラグ付きで新しいコードをリリースして結局不要だったという方が、新しいアプリのアップデートが必要だと後から気づくよりもはるかに良い選択です。

### 説明的にする {#be-descriptive}

フィーチャーフラグに説明を追加してください。Brazeではオプションのフィールドですが、利用可能なフィーチャーフラグを確認する際に他の人が抱く疑問に答えるのに役立ちます。

- このフラグの有効化と動作の責任者の連絡先
- このフラグを無効にすべきタイミング
- このフラグが制御する新機能に関するドキュメントやメモへのリンク
- 依存関係やフィーチャーの使用方法に関する注意事項

### 古いフィーチャーフラグを整理する {#clean-up-old-feature-flags}

100%のロールアウトのまま必要以上に長くフィーチャーを残してしまうことは誰にでもあります。

コード（およびBrazeダッシュボード）をクリーンに保つため、すべてのユーザーがアップグレードし、フィーチャーを無効にするオプションが不要になったら、コードベースから恒久的なフィーチャーフラグを削除してください。これにより、開発環境の複雑さが軽減されるだけでなく、フィーチャーフラグのリストも整理された状態に保たれます。