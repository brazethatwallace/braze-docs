## Cordova SDKを統合する {#integrating-the-cordova-sdk}

### 前提条件 {#prerequisites}

始める前に、お使いの環境が[最新のBraze Cordova SDKバージョン](https://github.com/braze-inc/braze-cordova-sdk?tab=readme-ov-file#minimum-version-requirements)でサポートされていることを確認してください。

### ステップ 1: SDKをプロジェクトに追加する {#step-1-add-the-sdk-to-your-project}

{% alert warning %}
Braze Cordova SDKは、以下の方法でのみ追加してください。他の方法でインストールしようとすると、セキュリティ侵害につながる恐れがあります。
{% endalert %}

Cordova 6以降をお使いの場合は、GitHubから直接SDKを追加できます。または、[GitHubリポジトリ](https://github.com/braze-inc/braze-cordova-sdk)のZIPをダウンロードして、SDKを手動で追加することもできます。

{% tabs local %}
{% tab ジオフェンス無効 %}
ロケーション収集とジオフェンスを使用する予定がない場合は、GitHubの`master`ブランチを使用してください。

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master
```
{% endtab %}

{% tab ジオフェンス有効 %}
ロケーション収集とジオフェンスを使用する予定がある場合は、GitHubの`geofence-branch`を使用してください。

`````````bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```
{% endtab %}
{% endtabs %}

{% alert tip %}
このステップを繰り返すことで、いつでも`master`と`geofence-branch`を切り替えることができます。
{% endalert %}

### ステップ 2: プロジェクトを構成する {#step-2-configure-your-project}

次に、プロジェクトの`config.xml`ファイル内の`platform`要素に以下の設定を追加します。

{% tabs %}
{% tab ios %}
`````````xml
<preference name="com.braze.ios_api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.ios_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}

{% tab android %}
`````````xml
<preference name="com.braze.android_api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.android_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}
{% endtabs %}

以下の値を置き換えてください。

| 値 | 説明 |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `BRAZE_API_KEY` | お使いの[Braze REST APIキー]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys)。 |
| `CUSTOM_API_ENDPOINT` | カスタムAPIエンドポイント。このエンドポイントは、Brazeインスタンスデータをダッシュボードの正しいアプリグループにルーティングするために使用されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2: Configure your project" }

`config.xml`ファイルの`platform`要素は以下のようになります。

{% tabs %}
{% tab ios %}
`````````xml
<platform name="ios">
    <preference name="com.braze.ios_api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.ios_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}

{% tab android %}
`````````xml
<platform name="android">
    <preference name="com.braze.android_api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.android_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}
{% endtabs %}

## プラットフォーム固有の構文 {#platform-specific-syntax}

以下のセクションでは、iOSまたはAndroidでCordovaを使用する場合のプラットフォーム固有の構文について説明します。

### 整数 {#integers}

{% tabs %}
{% tab ios %}
整数の設定は、以下の例のように文字列表現として読み取られます。

`````````xml
<platform name="ios">
    <preference name="com.braze.ios_flush_interval_seconds" value="10" />
    <preference name="com.braze.ios_session_timeout" value="5" />
</platform>
```
{% endtab %}

{% tab android %}
Cordova 8.0.0以降のフレームワークによる設定の処理方法に従い、整数のみの設定（送信者IDなど）は、以下の例のように先頭に`str_`を付加した文字列に設定する必要があります。

`````````xml
<platform name="android">
    <preference name="com.braze.android_fcm_sender_id" value="str_64422926741" />
    <preference name="com.braze.android_default_session_timeout" value="str_10" />
</platform>
```
{% endtab %}
{% endtabs %}

### ブール値 {#booleans}

{% tabs %}
{% tab ios %}
ブール値の設定は、以下の例のように`YES`および`NO`キーワードを文字列表現としてSDKによって読み取られます。

`````````xml
<platform name="ios">
    <preference name="com.braze.should_opt_in_when_push_authorized" value="YES" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
{% endtab %}

{% tab android %}
ブール値の設定は、以下の例のように`true`および`false`キーワードを文字列表現としてSDKによって読み取られます。

`````````xml
<platform name="android">
    <preference name="com.braze.should_opt_in_when_push_authorized" value="true" />
    <preference name="com.braze.is_session_start_based_timeout_enabled" value="false" />
</platform>
```
{% endtab %}
{% endtabs %}

## オプション設定 {#optional}

以下の設定をプロジェクトの`config.xml`ファイルの`platform`要素に追加できます。

{% tabs %}
{% tab ios %}
| 方法 | 説明 |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ios_api_key` | アプリケーションのAPIキーを設定します。 |
| `ios_api_endpoint` | アプリケーションの[SDKエンドポイント]({{site.baseurl}}/api/basics/#endpoints)を設定します。 |
| `ios_disable_automatic_push_registration` | 自動プッシュ登録を無効にするかどうかを設定します。 |
| `ios_disable_automatic_push_handling` | 自動プッシュ処理を無効にするかどうかを設定します。 |
| `ios_enable_idfa_automatic_collection` | Braze SDKがIDFA情報を自動的に収集するかどうかを設定します。詳細については、[BrazeのIDFAメソッドのドキュメント](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/)を参照してください。 |
| `enable_location_collection` | 自動ロケーション収集を有効にするかどうかを設定します（ユーザーが許可した場合）。`geofence-branch` |
| `geofences_enabled` | ジオフェンスを有効にするかどうかを設定します。 |
| `ios_session_timeout` | アプリケーションのBrazeセッションタイムアウトを秒単位で設定します。デフォルトは10秒です。 |
| `sdk_authentication_enabled` | [SDK認証]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication/#sdk-authentication)機能を有効にするかどうかを設定します。 |
| `display_foreground_push_notifications` | アプリケーションがフォアグラウンドにある間、プッシュ通知を表示するかどうかを設定します。 |
| `ios_disable_un_authorization_option_provisional` | `UNAuthorizationOptionProvisional`を無効にするかどうかを設定します。 |
| `trigger_action_minimum_time_interval_seconds` | トリガー間の最小時間間隔を秒単位で設定します。デフォルトは30秒です。 |
| `ios_push_app_group` | iOSプッシュ拡張機能のアプリグループIDを設定します。 |
| `ios_forward_universal_links` | SDKがユニバーサルリンクを自動的に認識し、システムメソッドに転送するかどうかを設定します。iOSでプッシュ通知からのディープリンクを機能させるために必要です。デフォルトは無効です。 |
| `ios_log_level` | `Braze.Configuration.Logger`の最小ログレベルを設定します。 |
| `ios_use_uuid_as_device_id` | ランダムに生成されたUUIDをデバイスIDとして使用するかどうかを設定します。 |
| `ios_flush_interval_seconds` | 自動データフラッシュの間隔を秒単位で設定します。デフォルトは10秒です。 |
| `ios_use_automatic_request_policy` | `Braze.Configuration.Api`のリクエストポリシーを自動にするか手動にするかを設定します。 |
| `should_opt_in_when_push_authorized` | プッシュ権限が承認された際に、ユーザーの通知サブスクリプション状態を自動的に`optedIn`に設定するかどうかを指定します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Optional configurations #optional" }

{% alert tip %}
詳細については、[GitHub: Braze iOS Cordovaプラグイン](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/ios/BrazePlugin.m)を参照してください。
{% endalert %}
{% endtab %}

{% tab android %}
| 方法 | 説明 |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `android_api_key` | アプリケーションのAPIキーを設定します。 |
| `android_api_endpoint` | アプリケーションの[SDKエンドポイント]({{site.baseurl}}/api/basics/#endpoints)を設定します。 |
| `android_small_notification_icon` | 通知の小さなアイコンを設定します。 |
| `android_large_notification_icon` | 通知の大きなアイコンを設定します。 |
| `android_notification_accent_color` | 通知のアクセントカラーを16進数表記で設定します。 |
| `android_default_session_timeout` | アプリケーションのBrazeセッションタイムアウトを秒単位で設定します。デフォルトは10秒です。 |
| `android_handle_push_deep_links_automatically` | Braze SDKがプッシュディープリンクを自動的に処理するかどうかを設定します。Androidでプッシュ通知からのディープリンクを機能させるために必要です。デフォルトは無効です。 |
| `android_log_level` | アプリケーションのログレベルを設定します。デフォルトのログレベルは4で、最小限の情報をログに記録します。デバッグ用の詳細ログを有効にするには、ログレベル2を使用してください。 |
| `firebase_cloud_messaging_registration_enabled` | プッシュ通知にFirebase Cloud Messagingを使用するかどうかを設定します。 |
| `android_fcm_sender_id` | Firebase Cloud Messagingの送信者IDを設定します。 |
| `enable_location_collection` | 自動ロケーション収集を有効にするかどうかを設定します（ユーザーが許可した場合）。 |
| `geofences_enabled` | ジオフェンスを有効にするかどうかを設定します。 |
| `android_disable_auto_session_tracking` | Android Cordovaプラグインによるセッションの自動トラッキングを無効にします。詳細については、[自動セッショントラッキングの無効化](#cordova_disable-automatic-session-tracking)を参照してください。 |
| `sdk_authentication_enabled` | [SDK認証]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication/#sdk-authentication)機能を有効にするかどうかを設定します。 |
| `trigger_action_minimum_time_interval_seconds` | トリガー間の最小時間間隔を秒単位で設定します。デフォルトは30秒です。 |
| `is_session_start_based_timeout_enabled` | セッションタイムアウトの動作を、セッション開始イベントに基づくかセッション終了イベントに基づくかを設定します。 |
| `default_notification_channel_name` | Brazeのデフォルト`NotificationChannel`で`NotificationChannel.getName`を通じてユーザーに表示される名前を設定します。 |
| `default_notification_channel_description` | Brazeのデフォルト`NotificationChannel`で`NotificationChannel.getDescription`を通じてユーザーに表示される説明を設定します。 |
| `does_push_story_dismiss_on_click` | Push Storiesがクリックされた際に自動的に非表示になるかどうかを設定します。 |
| `is_fallback_firebase_messaging_service_enabled` | フォールバック用のFirebase Cloud Messagingサービスの使用を有効にするかどうかを設定します。 |
| `fallback_firebase_messaging_service_classpath` | フォールバック用のFirebase Cloud Messagingサービスのクラスパスを設定します。 |
| `is_content_cards_unread_visual_indicator_enabled` | Content Cardsの未読視覚インジケーターバーを有効にするかどうかを設定します。 |
| `is_firebase_messaging_service_on_new_token_registration_enabled` | Braze SDKが`com.google.firebase.messaging.FirebaseMessagingService.onNewToken`でトークンを自動的に登録するかどうかを設定します。 |
| `is_push_deep_link_back_stack_activity_enabled` | プッシュのディープリンクを自動的にたどる際に、Brazeがバックスタックにアクティビティを追加するかどうかを設定します。 |
| `push_deep_link_back_stack_activity_class_name` | プッシュのディープリンクを自動的にたどる際に、Brazeがバックスタックに追加するアクティビティを設定します。 |
| `should_opt_in_when_push_authorized` | プッシュが許可された際に、Brazeがユーザーを自動的にオプトインするかどうかを設定します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Optional configurations #optional" }

{% alert tip %}
詳細については、[GitHub: Braze Android Cordovaプラグイン](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/android/BrazePlugin.kt)を参照してください。
{% endalert %}
{% endtab %}
{% endtabs %}

以下は、追加設定を含む`config.xml`ファイルの例です。

{% tabs %}
{% tab ios %}
`````````xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="NO"/"YES" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO"/"YES" />
    <preference name="com.braze.ios_enable_idfa_automatic_collection" value="YES"/"NO" />
    <preference name="com.braze.enable_location_collection" value="NO"/"YES" />
    <preference name="com.braze.geofences_enabled" value="NO"/"YES" />
    <preference name="com.braze.ios_session_timeout" value="5" />
    <preference name="com.braze.sdk_authentication_enabled" value="YES"/"NO" />
    <preference name="com.braze.display_foreground_push_notifications" value="YES"/"NO" />
    <preference name="com.braze.ios_disable_un_authorization_option_provisional" value="NO"/"YES" />
    <preference name="com.braze.trigger_action_minimum_time_interval_seconds" value="30" />
    <preference name="com.braze.ios_push_app_group" value="PUSH_APP_GROUP_ID" />
    <preference name="com.braze.ios_forward_universal_links" value="YES"/"NO" />
    <preference name="com.braze.ios_log_level" value="2" />
    <preference name="com.braze.ios_use_uuid_as_device_id" value="YES"/"NO" />
    <preference name="com.braze.ios_flush_interval_seconds" value="10" />
    <preference name="com.braze.ios_use_automatic_request_policy" value="YES"/"NO" />
    <preference name="com.braze.should_opt_in_when_push_authorized" value="YES"/"NO" />
</platform>
```
{% endtab %}

{% tab android %}
`````````xml
<platform name="android">
    <preference name="com.braze.android_small_notification_icon" value="RESOURCE_ENTRY_NAME_FOR_ICON_DRAWABLE" />
    <preference name="com.braze.android_large_notification_icon" value="RESOURCE_ENTRY_NAME_FOR_ICON_DRAWABLE" />
    <preference name="com.braze.android_notification_accent_color" value="str_ACCENT_COLOR_INTEGER" />
    <preference name="com.braze.android_default_session_timeout" value="str_SESSION_TIMEOUT_INTEGER" />
    <preference name="com.braze.android_handle_push_deep_links_automatically" value="true"/"false" />
    <preference name="com.braze.android_log_level" value="str_LOG_LEVEL_INTEGER" />
    <preference name="com.braze.firebase_cloud_messaging_registration_enabled" value="true"/"false" />
    <preference name="com.braze.android_fcm_sender_id" value="str_YOUR_FCM_SENDER_ID" />
    <preference name="com.braze.enable_location_collection" value="true"/"false" />
    <preference name="com.braze.geofences_enabled" value="true"/"false" />
    <preference name="com.braze.android_disable_auto_session_tracking" value="true"/"false" />
    <preference name="com.braze.sdk_authentication_enabled" value="true"/"false" />
    <preference name="com.braze.trigger_action_minimum_time_interval_seconds" value="str_MINIMUM_INTERVAL_INTEGER" />
    <preference name="com.braze.is_session_start_based_timeout_enabled" value="false"/"true" />
    <preference name="com.braze.default_notification_channel_name" value="DEFAULT_NAME" />
    <preference name="com.braze.default_notification_channel_description" value="DEFAULT_DESCRIPTION" />
    <preference name="com.braze.does_push_story_dismiss_on_click" value="true"/"false" />
    <preference name="com.braze.is_fallback_firebase_messaging_service_enabled" value="true"/"false" />
    <preference name="com.braze.fallback_firebase_messaging_service_classpath" value="FALLBACK_FIREBASE_MESSAGING_CLASSPATH" />
    <preference name="com.braze.is_content_cards_unread_visual_indicator_enabled" value="true"/"false" />
    <preference name="com.braze.is_firebase_messaging_service_on_new_token_registration_enabled" value="true"/"false" />
    <preference name="com.braze.is_push_deep_link_back_stack_activity_enabled" value="true"/"false" />
    <preference name="com.braze.push_deep_link_back_stack_activity_class_name" value="DEEPLINK_BACKSTACK_ACTIVITY_CLASS_NAME" />
    <preference name="com.braze.should_opt_in_when_push_authorized" value="true"/"false" />
</platform>
```
{% endtab %}
{% endtabs %}

## 自動セッショントラッキングを無効にする（Androidのみ） {#disable-automatic-session-tracking}

デフォルトでは、Android Cordovaプラグインは自動的にセッションをトラッキングします。自動セッショントラッキングを無効にするには、プロジェクトの`config.xml`ファイル内の`platform`要素に以下の設定を追加してください。

`````````xml
<platform name="android">
    <preference name="com.braze.android_disable_auto_session_tracking" value="true" />
</platform>
```

セッショントラッキングを再開するには、`BrazePlugin.startSessionTracking()`を呼び出してください。次回の`Activity.onStart()`以降に開始されたセッションのみがトラッキングされることに注意してください。