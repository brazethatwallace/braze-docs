{% alert important %}
React Native SDKでは、ジオフェンスは**iOSとAndroidの両方**でサポートされています。`requestLocationInitialization`メソッドはAndroid専用であり、iOSでは不要です。`requestGeofences`メソッドは両方のプラットフォームで利用できます。デフォルトでは、SDKはロケーションが利用可能な場合にジオフェンスを自動的にリクエストし監視できます。この自動設定を利用するか、`requestGeofences`を呼び出して手動でリクエストすることができます。
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## ジオフェンスの設定 {#setting-up-geofences}

### ステップ 1:Brazeで有効にする {#step-1-enable-in-braze}

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### ステップ 2:ネイティブAndroidセットアップを完了する {#step-2-complete-native-android-setup}

React Native SDKはネイティブのBraze Android SDKを使用するため、プロジェクトのネイティブAndroidジオフェンスセットアップを完了する必要があります。これらのステップに相当するiOS版は、ネイティブSwift SDKジオフェンスガイド（[ステップ2.2から3.1]({{site.baseurl}}/developer_guide/geofences/?sdktab=swift#swift_step-21-add-the-brazelocation-module)）で説明されています。ステップ2.1（BrazeLocationモジュールの追加）はReact Nativeでは不要です。BrazeLocationはBraze React Native SDKに既に暗黙的に含まれているためです。

1. **`build.gradle`を更新する：** `android-sdk-location`とGoogle Play Servicesのロケーションを追加します。[Androidジオフェンス]({{site.baseurl}}/developer_guide/geofences/?sdktab=android)を参照してください。
2. **マニフェストを更新する：** ロケーション権限とBrazeブートレシーバーを追加します。[Androidジオフェンス]({{site.baseurl}}/developer_guide/geofences/?sdktab=android)を参照してください。
3. **Brazeのロケーション収集を有効にする：** `braze.xml`ファイルを更新します。[Androidジオフェンス]({{site.baseurl}}/developer_guide/geofences/?sdktab=android)を参照してください。

### ステップ 3:ネイティブiOSセットアップを完了する {#step-3-complete-native-ios-setup}

React Native SDKはネイティブのBraze iOS SDKを使用するため、プロジェクトのネイティブiOSジオフェンスセットアップを完了するには、ネイティブSwift SDKの手順に従い、ステップ2.2から開始します。具体的には、`Info.plist`をロケーション使用説明で更新し（ステップ2.2）、`automaticGeofenceRequests = true`を含むBraze設定でジオフェンスを有効にし（ステップ3）、オプションでバックグラウンドレポートを有効にします（ステップ3.1）。ステップ2.1（BrazeLocationモジュールの追加）は不要です。BrazeLocationはBraze React Native SDKに既に暗黙的に含まれています。[iOSジオフェンス、ステップ2.2から3.1]({{site.baseurl}}/developer_guide/geofences/?sdktab=swift#swift_step-21-add-the-brazelocation-module)を参照してください。

### ステップ 4:JavaScriptからジオフェンスをリクエストする {#step-4-request-geofences-from-javascript}

**Androidの場合：** ユーザーがロケーション権限を付与した後、`requestLocationInitialization()`を呼び出してBrazeのロケーション機能を初期化し、Brazeサーバーからジオフェンスをリクエストします。このメソッドはiOSではサポートされておらず、iOSでは不要です。

**iOSの場合：** 対応する方法は、ネイティブのSwiftまたはObjective-CのBraze設定で`automaticGeofenceRequests`設定を有効にすることです（ステップ3を参照）。これが有効になると、SDKはロケーションが利用可能な場合に自動的にジオフェンスをリクエストし監視します。`requestLocationInitialization`に相当するJavaScript呼び出しは不要です。

```javascript
import Braze from '@braze/react-native-sdk';

// Android only: call this after the user grants location permission
Braze.requestLocationInitialization();
```

### ステップ 5:ジオフェンスを手動でリクエストする（オプション） {#step-5-manually-request-geofences-optional}

iOSとAndroidの両方で、`requestGeofences`を使用して特定のGPS座標に対するジオフェンスの更新を手動でリクエストできます。デフォルトでは、Brazeは自動的にデバイスのロケーションを取得し、ジオフェンスをリクエストします。代わりに手動で座標を指定するには：

1. 自動ジオフェンスリクエストを無効にします。Androidでは、`braze.xml`で`com_braze_automatic_geofence_requests_enabled`を`false`に設定します。iOSでは、Brazeの設定で`automaticGeofenceRequests`を`false`に設定します。
2. 指定した緯度と経度で`requestGeofences`を呼び出します：

`````````javascript
import Braze from '@braze/react-native-sdk';

Braze.requestGeofences(33.078947, -116.601356);
```

{% alert important %}
ジオフェンスは、SDKによる自動リクエストまたはこのメソッドによる手動リクエストのいずれかで、セッションごとに一度だけリクエストできます。
{% endalert %}