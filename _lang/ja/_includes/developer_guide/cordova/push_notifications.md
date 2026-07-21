{% multi_lang_include developer_guide/prerequisites/cordova.md %} SDKを統合すると、基本的なプッシュ通知機能はデフォルトで有効になります。[リッチプッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=cordova)と[Push Stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories/?sdktab=cordova)を使用するには、それぞれ個別に設定する必要があります。iOSのプッシュ通知を利用するには、有効なプッシュ証明書もアップロードする必要があります。

{% alert warning %}
Cordovaプラグインを追加、削除、または更新するたびに、CordovaはiOSアプリのXcodeプロジェクト内のPodfileを上書きします。つまり、Cordovaプラグインを変更するたびに、これらの機能を再度設定する必要があります。
{% endalert %}

## プッシュディープリンクを有効にする {#enabling-push-deep-linking}

デフォルトでは、Braze Cordova SDKはプッシュ通知からのディープリンクを自動的に処理しません。プッシュディープリンクを有効にするには、[ディープリンク]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=cordova)の設定ステップに従ってください。
これらの設定やその他のプッシュ設定オプションの詳細については、[オプションの設定]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional)を参照してください。

## 基本プッシュ通知を無効にする（iOSのみ） {#disabling-basic-push-notifications-ios-only}

iOS用のBraze Cordova SDKを統合すると、基本的なプッシュ通知機能がデフォルトで有効になります。iOSアプリでこの機能を無効にするには、`config.xml`ファイルに以下を追加してください。詳細については、[オプションの設定]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional)を参照してください。

```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="NO" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
