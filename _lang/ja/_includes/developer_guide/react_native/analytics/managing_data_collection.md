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

デバイス上にローカルに保存されたすべてのBraze SDKデータを削除するには、`wipeData`メソッドを使用します。このメソッドを呼び出すと、SDKは無効になり、`enableSDK`で再度有効にする必要があります。

```javascript
Braze.wipeData();
```

## データのフラッシュ {#flushing-data}

保留中のデータをBrazeサーバーに即座にフラッシュするには、`requestImmediateDataFlush`を使用します。

```javascript
Braze.requestImmediateDataFlush();
```

## 広告トラッキングの有効化設定 {#setting-ad-tracking-enabled}

Brazeにこのデバイスで広告トラッキングが有効かどうかを通知するには、`setAdTrackingEnabled`メソッドを使用します。SDKはこのデータを自動的に収集しません。

```javascript
Braze.setAdTrackingEnabled(true, "GOOGLE_ADVERTISING_ID");
```

2番目のパラメーターはGoogle Advertising IDで、Androidでのみ使用されます。

## トラッキングプロパティ許可リストの更新（iOSのみ） {#updating-the-tracking-property-allow-list-ios-only}

トラッキング対象として宣言するデータタイプのリストを更新するには、`updateTrackingPropertyAllowList`を使用します。Androidではこの操作は何も行いません。

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

詳細については、[プライバシーマニフェスト]({{site.baseurl}}/developer_guide/analytics/managing_data_collection?sdktab=swift#swift_privacy-manifest)を参照してください。

## ログアウトとプッシュ登録解除 {#logout-and-unregister-push}

この機能はReact Native SDKではまだサポートされていません。