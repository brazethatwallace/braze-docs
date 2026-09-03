## トラブルシューティング {#troubleshooting}

### プッシュ通知をタップしてもアプリが開かない {#tapping-push-notification-doesnt-open-the-app}

Androidでは、プッシュ通知をタップしたときにアプリが自動的にフォアグラウンドに表示され、ディープリンクが開かれるかどうかは、ネイティブの`com_braze_handle_push_deep_links_automatically`フラグによって制御されます。このフラグのデフォルト値は`false`です。

デフォルトの`false`の場合：

- ネイティブSDKは引き続き`BRAZE_PUSH_CLICKED`ブロードキャストを送信し、Dartの`push_opened`リスナーも期待どおりに起動します。
- ネイティブSDKは`startActivity()`を呼び出さないため、アプリはフォアグラウンドに表示されず、ディープリンクも自動的にたどられません。

これら2つの動作が発生している症状と一致する場合、フラグの設定が原因である可能性が高いです。
確認するには、デバイスログで`BrazePushReceiver`が`com.braze.action.BRAZE_PUSH_CLICKED`を処理しているエントリを探し、続いてFlutterログに`push_opened`イベントが記録されているにもかかわらず、対応するアプリの起動がないことを確認してください。

これを修正するには、`braze.xml`で`com_braze_handle_push_deep_links_automatically`を`true`に設定します。

```xml
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

詳細については、Flutterプッシュ通知ガイドの[ディープリンクの追加（Android）]({{site.baseurl}}/developer_guide/push_notifications#flutter_step-4-add-deep-links-android)を参照してください。

### その他のプッシュ配信および登録の問題 {#other-push-delivery-and-registration-issues}

Braze Flutter SDK for AndroidはネイティブのBraze Android SDKの上に構築されているため、その他のプッシュ配信、登録、ログに関する問題（送信者IDの不一致、Google Play Servicesの欠落、`BrazeFirebaseMessagingService`が登録されていないなど）のほとんどはFlutterアプリにも該当します。詳細については、[ネイティブAndroidトラブルシューティングガイド]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)を参照してください。