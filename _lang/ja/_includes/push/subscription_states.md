## プッシュサブスクリプションの状態 {#push-sub-states}

Brazeの「プッシュサブスクリプションの状態」は、プッシュ通知の受信に対する**ユーザー**のグローバルな設定を識別します。サブスクリプションの状態はユーザーベースであるため、個々のアプリに固有のものではありません。サブスクリプションの状態は、プッシュ通知のターゲットにするユーザーを決定する際に役立つフラグとなります。

{% alert note %}
ユーザーのプッシュサブスクリプションの状態は、ユーザーのすべてのデバイスを含むユーザープロファイル全体に適用されます。
{% endalert %}

以下のサブスクリプション状態オプションがあります：`Subscribed`、`Opted-In`、および `Unsubscribed`。

デフォルトでは、ユーザーがプッシュ通知でメッセージを受け取るには、プッシュサブスクリプション状態が `Subscribed` または `Opted-In` のいずれかであり、かつフォアグラウンドプッシュが有効になっている必要があります。メッセージの作成時に、必要に応じてこの設定をオーバーライドできます。

| オプトイン状態 | 説明 |
|---|---|
| `Subscribed` | Brazeでユーザープロファイルが作成されたときのデフォルトのプッシュサブスクリプション状態。 |
| `Opted-In` | ユーザーがプッシュ通知を受け取ることを明示的に希望しました。ユーザーがOSレベルのプッシュプロンプトを承認した場合、Brazeは自動的にそのユーザーのオプトイン状態を `Opted-In` に変更します。<br><br>Android 12またはそれ以前のユーザーには適用されません。|
| `Unsubscribed` | ユーザーがアプリケーションやブランドが提供するその他の方法で、プッシュ配信を明示的に解除しました。デフォルトでは、Brazeのプッシュ Campaignsは、プッシュ通知に対して `Subscribed` または `Opted-in` のユーザーのみを対象とします。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push subscription states #push-sub-states" }

{% alert important %}
Brazeがユーザーのプッシュサブスクリプションの状態を自動的に `Unsubscribed` に変更することはありません。ユーザーのプッシュサブスクリプション状態が `Unsubscribed` の場合、そのユーザーのセグメンテーションにおける `Foreground Push Enabled` フィルターは `false` になることを覚えておいてください。
{% endalert %}

### プッシュサブスクリプションの状態の更新 {#update-push-subscription-state}

ユーザーのプッシュサブスクリプション状態を更新する以下の方法を確認してください。

#### 自動オプトイン（デフォルト） {#automatic-opt-in-default}

Brazeはデフォルトで、ユーザーが初めてアプリのプッシュ通知を承認したときに、ユーザーのプッシュサブスクリプション状態を `Opted-In` に設定します。また、ユーザーがシステム設定でプッシュ権限を無効にした後、再度有効にした場合にも同様の処理を行います。

{% tabs local %}
{% tab android %}
このデフォルトの動作を無効にするには、Android Studioプロジェクトの `braze.xml` ファイルに次のプロパティを追加します。

```xml
<bool name="com_braze_optin_when_push_authorized">false</bool>
```
{% endtab %}

{% tab swift %}
[Braze Swift SDKバージョン7.5.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0)以降では、Xcodeプロジェクトの `AppDelegate.swift` ファイルに `optInWhenPushAuthorized` の設定を追加することで、この動作を無効にしたり、さらにカスタマイズしたりすることができます。

```swift
configuration.optInWhenPushAuthorized = false // disables the default behavior

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% endtabs %}

#### SDKの統合 {#sdk-integration}

[Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype)、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html)、または[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/set(pushnotificationsubscriptionstate:))で `setPushNotificationSubscriptionType` メソッドを使用して、Braze SDKでユーザーのサブスクリプション状態を更新できます。例えば、このメソッドを使って、ユーザーが手動でプッシュ通知を有効または無効にできる設定ページをアプリ内に作成することができます。

#### REST API

ユーザーのサブスクリプション状態を更新するには、Braze REST APIの[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を使用して、ユーザーの [`push_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object/) 属性を更新します。

### プッシュサブスクリプションの状態の確認 {#checking-push-subscription-state}

![John Doeのユーザープロファイルで、プッシュサブスクリプションの状態が購読中に設定されている。]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Brazeでは、以下のいずれかの方法でユーザーのプッシュサブスクリプション状態を確認できます。

* **ユーザープロファイル：** Brazeダッシュボードの[**ユーザー検索**]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/)ページから、個々のユーザープロファイルにアクセスできます。（メールアドレス、電話番号、または外部ユーザーIDを使用して）ユーザーのプロファイルを見つけた後、**Engagement**タブを選択してユーザーのサブスクリプション状態を表示し、手動で調整することができます。
* **REST APIでのエクスポート：** [Segmentごとのユーザー]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)または[識別子ごとのユーザー]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)エンドポイントを使用して、個々のユーザープロファイルをJSON形式でエクスポートできます。Brazeは、デバイスごとのプッシュ有効化情報を含むプッシュトークンオブジェクトを返します。