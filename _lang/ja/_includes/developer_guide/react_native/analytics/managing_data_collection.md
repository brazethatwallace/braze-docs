{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## データトラッキングを無効にする {#disabling-data-tracking}

データ収集を無効にするには、`disableSDK`メソッドを使用します。このメソッドを呼び出すと、Braze SDKはBrazeサーバーへのデータ送信を停止します。

```javascript
Braze.disableSDK();
```

## データトラッキングを再開する {#resuming-data-tracking}

データ収集を無効にした後に再開するには、`enableSDK`メソッドを使用します。

```javascript
Braze.enableSDK();
```

## ローカルに保存されたデータを消去する {#wiping-data}

デバイスに保存されたすべてのBraze SDKデータを削除するには、`wipeData`メソッドを使用します。このメソッドを呼び出すと、SDKは無効になり、`enableSDK`で再度有効にする必要があります。

```javascript
Braze.wipeData();
```

## データのフラッシュ {#flushing-data}

保留中のデータをBrazeサーバーに即座にフラッシュするには、`requestImmediateDataFlush`を使用します。

```javascript
Braze.requestImmediateDataFlush();
```

## 広告トラッキングの有効化を設定する {#setting-ad-tracking-enabled}

このデバイスで広告トラッキングが有効かどうかをBrazeに通知するには、`setAdTrackingEnabled`メソッドを使用します。SDKはこのデータを自動的に収集しません。

```javascript
Braze.setAdTrackingEnabled(true, "GOOGLE_ADVERTISING_ID");
```

2番目のパラメーターはGoogle Advertising IDで、Androidでのみ使用されます。

## トラッキングプロパティ許可リストの更新（iOSのみ） {#updating-the-tracking-property-allow-list-ios-only}

トラッキングとして宣言されたデータタイプのリストを更新するには、`updateTrackingPropertyAllowList`を使用します。これはAndroidでは何も実行されません。

```javascript
Braze.updateTrackingPropertyAllowList({
  adding: [Braze.TrackingProperty.EMAIL, Braze.TrackingProperty.FIRST_NAME],
  removing: [],
  addingCustomEvents: ["my_custom_event"],
  removingCustomEvents: [],
  addingCustomAttributes: ["my_custom_attribute"],
  removingCustomAttributes: []
});
```

詳細については、[プライバシーマニフェスト]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest)を参照してください。

## ログアウトとプッシュ登録解除 {#logout-and-unregister-push}

この機能はReact Native SDKではまだサポートされていません。