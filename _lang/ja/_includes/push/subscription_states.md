## プッシュサブスクリプションの状態 {#push-sub-states}

Brazeの「プッシュサブスクリプションの状態」は、プッシュ通知の受信に対する**ユーザー**のグローバルな設定を識別します。サブスクリプションの状態はユーザーベースであるため、個々のアプリに固有のものではありません。サブスクリプションの状態は、プッシュ通知のターゲットにするユーザーを決定する際に役立つフラグとなります。

{% alert note %}
ユーザーのプッシュサブスクリプションの状態は、ユーザーのすべてのデバイスを含むユーザープロファイル全体に適用されます。
{% endalert %}

以下のサブスクリプション状態オプションがあります：`Subscribed`、`Opted-In`、および`Unsubscribed`。

デフォルトでは、ユーザーがプッシュ通知でメッセージを受け取るには、プッシュサブスクリプション状態が`Subscribed`または`Opted-In`のいずれかであり、かつフォアグラウンドプッシュが有効になっている必要があります。メッセージの作成時に、必要に応じてこの設定をオーバーライドできます。

| オプトイン状態 | 説明 |
|---|---|
| `Subscribed` | Brazeでユーザープロファイルが作成されたときのデフォルトのプッシュサブスクリプション状態。 |
| `Opted-In` | ユーザーがプッシュ通知を受け取ることを明示的に希望しました。ユーザーがOSレベルのプッシュプロンプトを承認した場合、Brazeは自動的にそのユーザーのオプトイン状態を`Opted-In`に変更します。<br><br>Android 12またはそれ以前のユーザーには適用されません。|
| `Unsubscribed` | ユーザーがアプリケーションやブランドが提供するその他の方法で、プッシュ配信を明示的に購読解除しました。デフォルトでは、Brazeのプッシュキャンペーンは、プッシュ通知に対して`Subscribed`または`Opted-in`のユーザーのみを対象とします。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="プッシュサブスクリプションの状態 #push-sub-states" }

{% alert important %}
Brazeがユーザーのプッシュサブスクリプションの状態を自動的に`Unsubscribed`に変更することはありません。ユーザーのプッシュサブスクリプション状態が`Unsubscribed`の場合、そのユーザーのセグメンテーションにおける`Foreground Push Enabled`フィルターは`false`になることを覚えておいてください。
{% endalert %}

### プッシュ登録と到達可能なユーザー {#push-registration-and-reachable-users}

プッシュサブスクリプションの状態はユーザーの設定を反映しますが、ダッシュボードでプッシュの**到達可能**としてカウントされるかどうかは、[プッシュ登録]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle)にも依存します。つまり、プロファイルに有効なフォアグラウンドプッシュトークンが存在する必要があります。Brazeがチャネルレベルのカウントを計算する方法については、[セグメントサイズの測定]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size)を参照してください。

- **プッシュキャンペーンとキャンバス：** プッシュ登録されていないユーザーは、プッシュサブスクリプション状態が`Subscribed`または`Opted-In`であっても、オーディエンス統計のAndroidプッシュまたはiOSプッシュの**到達可能なユーザー**には含まれません。
- **その他のチャネル：** 同じユーザーでも、対象となる他のチャネル（メールやアプリ内メッセージなど）では到達可能としてカウントされる場合があります。
- **セグメント：** セグメントのメンバーシップはフィルターに従います。プッシュ登録のないユーザーも、フィルターで除外されない限り（例：**Foreground Push Enabled**）、セグメントに残ります。セグメントの合計メンバーシップは、プッシュ固有の**到達可能なユーザー**行に表示されるユーザー数の合計よりも多くなる場合があります。

ユーザープロファイルのプッシュサブスクリプション状態が`Subscribed`であっても、プッシュトークンが割り当てられていない場合があります。そのようなユーザーは、Brazeが有効なトークンを記録するまで、AndroidプッシュまたはiOSプッシュの**到達可能なユーザー**にはカウントされません。

フィルターの定義については、[セグメンテーションフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)を参照してください。

### プッシュサブスクリプションの状態の更新 {#update-push-subscription-state}

ユーザーのプッシュサブスクリプション状態を更新する以下の方法を確認してください。

#### 自動オプトイン（デフォルト） {#automatic-opt-in-default}

Brazeはデフォルトで、ユーザーが初めてアプリのプッシュ通知を承認したときに、ユーザーのプッシュサブスクリプション状態を`Opted-In`に設定します。また、ユーザーがシステム設定でプッシュ権限を無効にした後、再度有効にした場合にも同様の処理を行います。

{% tabs local %}
{% tab android %}
このデフォルトの動作を無効にするには、Android Studioプロジェクトの`braze.xml`ファイルに次のプロパティを追加します。

```xml
<bool name="com_braze_optin_when_push_authorized">false</bool>
```
{% endtab %}

{% tab swift %}
iOSでは、新規インストール時のプッシュサブスクリプション状態は通常 **`Subscribed`** です。ユーザーが通知を許可すると、自動オプトインが有効な場合、Brazeは状態を **`Opted-In`** に設定します。ユーザーが**Don't Allow**を選択し、後からiOSの設定でプッシュを有効にした場合、状態は設定を変更した瞬間ではなく、ユーザーがセッションを記録した後に更新されます。

[Braze Swift SDKバージョン7.5.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0)以降では、Xcodeプロジェクトの`AppDelegate.swift`ファイルに`optInWhenPushAuthorized`の設定を追加することで、この動作を無効にしたり、さらにカスタマイズしたりすることができます。

```swift
configuration.optInWhenPushAuthorized = false // disables the default behavior

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% endtabs %}

#### SDKの統合 {#sdk-integration}

[Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype)、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html)、または[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/set(pushnotificationsubscriptionstate:))で`setPushNotificationSubscriptionType`メソッドを使用して、Braze SDKでユーザーのサブスクリプション状態を更新できます。例えば、このメソッドを使って、ユーザーが手動でプッシュ通知を有効または無効にできる設定ページをアプリ内に作成することができます。

#### REST API

ユーザーのサブスクリプション状態を更新するには、Braze REST APIの[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を使用して、ユーザーの[`push_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object)属性を更新します。

### プッシュ有効化とプッシュサブスクリプション状態の違い {#differences-between-push-enablement-and-push-subscription-status}

プッシュ有効化とは、ユーザーが特定のデバイスでOSまたはブラウザレベルの通知受信許可を付与しているかどうかを指します。プッシュサブスクリプション状態は、Brazeレベルの設定であり、プロファイル全体でプッシュを受信するためのユーザーのグローバルな設定を表します。

自動オプトインが有効（デフォルト）の場合、ユーザーがアプリのプッシュ通知を承認するか、システム設定でプッシュ権限を再度有効にすると（例えば、iOS、Android 13以降、およびサポートされているWebブラウザ）、Brazeはユーザーのプッシュサブスクリプション状態を`Opted-In`に更新します。それ以外の場合、SDKメソッドまたはREST API呼び出しを使用して明示的に変更するまで、ユーザーのプッシュサブスクリプション状態は`Subscribed`のままです。

Brazeは、ユーザーがOS、ブラウザ、またはアプリレベルで通知をオプトアウトした場合でも、ユーザーのプッシュサブスクリプション状態を自動的に`Unsubscribed`に変更することはありません。ユーザーのプッシュサブスクリプション状態を更新するには、Brazeで更新する必要があります。例えば、ユーザーがアプリ内のユーザー設定センターからプッシュを無効にした場合、Brazeでプッシュサブスクリプション状態を`Unsubscribed`に更新してください。Brazeはユーザー設定センターに基づいてユーザープロファイルを自動的に更新しません。サブスクリプション状態をユーザーのアプリ内設定と一致させるには、SDK（iOSまたはAndroid）またはREST APIを使用して適切なメソッドを呼び出してください。詳細については、[プッシュサブスクリプションの状態の更新]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#update-push-subscription-state)を参照してください。

### インポートされたプッシュトークン（iOS） {#imported-push-tokens-ios}

[iOSプッシュトークンをインポート]({{site.baseurl}}/api/objects_filters/user_attributes_object#push-token-import)する際に`push_token_import`を使用すると、ユーザーのプッシュサブスクリプション状態は通常 **`Subscribed`** となり、Braze統合アプリでセッションを記録するまでその状態が維持されます。最初のセッション後、[自動オプトイン](#automatic-opt-in-default)が適用される場合（例えば、ユーザーがiOSでプッシュを承認し、`optInWhenPushAuthorized`が有効な場合）、Brazeは状態を **`Opted-In`** に更新することがあります。

インポート後、およびユーザーの最初のアプリ内セッション後に、ユーザープロファイルの**連絡先設定**を確認して、期待される状態になっていることを確認してください。

### プッシュサブスクリプションの状態の確認 {#checking-push-subscription-state}

![John Doeのユーザープロファイルで、プッシュサブスクリプションの状態が「Subscribed」に設定されている。]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Brazeでは、以下のいずれかの方法でユーザーのプッシュサブスクリプション状態を確認できます。

* **ユーザープロファイル：** Brazeダッシュボードの[**ユーザー検索**]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles)ページから、個々のユーザープロファイルにアクセスできます。（メールアドレス、電話番号、または外部ユーザーIDを使用して）ユーザーのプロファイルを見つけた後、**エンゲージメント**タブを選択してユーザーのサブスクリプション状態を表示し、手動で調整することができます。
* **REST APIでのエクスポート：** [セグメントごとのユーザー]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)または[識別子ごとのユーザー]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)エンドポイントを使用して、個々のユーザープロファイルをJSON形式でエクスポートできます。Brazeは、デバイスごとのプッシュ有効化情報を含むプッシュトークンオブジェクトを返します。