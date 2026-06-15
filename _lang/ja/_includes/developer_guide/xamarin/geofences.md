{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## 前提条件 {#prerequisites}

ジオフェンスの使用を開始するために必要な最小SDKバージョンは以下の通りです：

{% sdk_min_versions xamarin:9.0.0 %}

## ジオフェンスの設定 {#setting-up-geofences}

### ステップ 1: Brazeで有効にする {#step-1-enable-in-braze}

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

---

次に、AndroidまたはiOSのいずれかについて、以下のプラットフォーム固有の手順に従ってください：

{% tabs %}
{% tab Android %}

### ステップ 2: 依存関係を追加する {#step-2-add-dependencies}

プロジェクトに次のNuGetパッケージ参照を追加します：

- `BrazePlatform.BrazeAndroidLocationBinding`

### ステップ 3: AndroidManifest.xmlを更新する {#step-3-update-your-androidmanifestxml}

`AndroidManifest.xml`に以下の権限を追加します：

```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

{% alert important %}
Android 10以降のデバイスでは、アプリがバックグラウンドで動作している間ジオフェンスが機能するために、バックグラウンド位置情報アクセス権限が必要です。
{% endalert %}

### ステップ 4: Brazeの位置情報収集を設定する {#step-4-configure-braze-location-collection}

Brazeの設定で位置情報の収集が有効になっていることを確認してください。自動位置情報収集なしでジオフェンスを有効にしたい場合は、`Braze.xml`に以下を設定します：

`````````xml
<bool name="com_braze_enable_location_collection">true</bool>
<bool name="com_braze_geofences_enabled">true</bool>
```

### ステップ 5: 実行時に位置情報の権限をリクエストする {#step-5-request-location-permissions-at-runtime}

ジオフェンスを登録する前に、ユーザーから位置情報の権限をリクエストする必要があります。C#コードでは、次のパターンを使用します：

`````````csharp
using AndroidX.Core.App;
using AndroidX.Core.Content;

private void RequestLocationPermission()
{
  // ...existing code for checking and requesting permissions...
}

public override void OnRequestPermissionsResult(int requestCode, string[] permissions, Permission[] grantResults)
{
  // ...existing code for handling permission result...
}
```

権限が付与された後、Brazeの位置情報収集を初期化します：

`````````csharp
Braze.GetInstance(this).RequestLocationInitialization();
```

### ステップ 6: ジオフェンスの更新を手動でリクエストする（オプション） {#step-6-manually-request-geofence-updates-optional}

特定のロケーションに対してジオフェンスを手動でリクエストするには：

`````````csharp
Braze.GetInstance(this).RequestGeofences(latitude, longitude);
```

{% alert important %}
ジオフェンスは、SDKによる自動リクエストまたはこのメソッドによる手動リクエストのいずれかで、セッションごとに1回のみリクエストできます。
{% endalert %}
{% endtab %}
{% tab iOS %}

### ステップ 2: 依存関係を追加する

プロジェクトに次のNuGetパッケージ参照を追加します：

- `Braze.iOS.BrazeLocation`

### ステップ 3: Info.plistで位置情報の使用を設定する {#step-3-configure-location-usage-in-infoplist}

`Info.plist`に位置情報サービスの使用説明文字列を追加します：

`````````xml
<key>NSLocationAlwaysAndWhenInUseUsageDescription</key>
<string>This app uses your location to enable geofences and location-based messaging.</string>
<key>NSLocationWhenInUseUsageDescription</key>
<string>This app uses your location to enable geofences and location-based messaging.</string>
```

{% alert important %}
Appleは`NSLocationAlwaysUsageDescription`を廃止しました。iOS 14以降では上記のキーを使用してください。
{% endalert %}

### ステップ 4: Brazeの設定でジオフェンスを有効にする {#step-4-enable-geofences-in-your-braze-configuration}

アプリの起動コード（例：`App.xaml.cs`）で、ジオフェンスを有効にしてBrazeを設定します：

`````````csharp
using BrazeKit;
using BrazeLocation;

var configuration = new BRZConfiguration("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>");
configuration.Location.BrazeLocationProvider = new BrazeLocationProvider();
configuration.Location.AutomaticLocationCollection = true;
configuration.Location.GeofencesEnabled = true;
configuration.Location.AutomaticGeofenceRequests = true;
// ...other configuration...
var braze = new Braze(configuration);
```

### ステップ 5: バックグラウンド位置情報の更新を有効にする（オプション） {#step-5-enable-background-location-updates-optional}

バックグラウンドでジオフェンスを監視するには、`Info.plist`に以下の設定を追加して**Location updates**バックグラウンドモードを有効にします：

`````````xml
<key>UIBackgroundModes</key>
<array>
  <string>location</string>
</array>
```

次に、Brazeの設定で以下を設定します：

`````````csharp
configuration.Location.AllowBackgroundGeofenceUpdates = true;
configuration.Location.DistanceFilter = 8000; // meters
```

{% alert important %}
バッテリーの消耗を防ぐため、`DistanceFilter`をアプリのニーズに合った値に設定してください。
{% endalert %}

### ステップ 6: 位置情報の許可をリクエストする {#step-6-request-location-authorization}

ユーザーから`When In Use`または`Always`の許可をリクエストします：

`````````csharp
using CoreLocation;

var locationManager = new CLLocationManager();
locationManager.RequestWhenInUseAuthorization();
// or
locationManager.RequestAlwaysAuthorization();
```

{% alert important %}
`Always`の許可がない場合、iOSはアプリが使用されていない間、位置情報サービスの実行を制限します。これはオペレーティングシステムによって強制されるものであり、Braze SDKでは回避できません。
{% endalert %}
{% endtab %}
{% endtabs %}