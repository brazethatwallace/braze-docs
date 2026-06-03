# ユーザー IDを設定する {#setting-user-ids}

> このリファレンス記事では、Android または FireOS アプリでユーザー IDを設定する方法、推奨されるユーザー IDの命名規則、およびいくつかのベストプラクティスについて説明します。

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

## 推奨されるユーザー IDの命名規則 {#suggested-user-id-naming-convention}

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

### ユーザー IDの割り当て {#assigning-a-user-id}

ユーザー IDを設定するために、ユーザーが識別された直後（一般的にはログイン後）に以下の呼び出しを行う必要があります。

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING);
```

{% endtab %}
{% tab KOTLIN %}

`````````kotlin
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING)
```

{% endtab %}
{% endtabs %}

{% alert warning %}
**ユーザーがログアウトするときに `changeUser()` を呼び出さないでください。`changeUser()` は、ユーザーがアプリケーションにログインするときにのみ呼び出す必要があります。**`changeUser()` を静的なデフォルト値に設定すると、ユーザーが再度ログインするまで、すべてのユーザーアクティビティがそのデフォルトの「ユーザー」に関連付けられます。
{% endalert %}

また、ユーザーがログアウトするときにユーザー IDを変更**しない**ことをお勧めします。変更すると、以前にログインしたユーザーを再エンゲージメントキャンペーンでターゲットにできなくなるためです。同じデバイスに複数のユーザーが存在することが予想されるものの、アプリがログアウト状態の間にそのうちの1ユーザーのみをターゲットにしたい場合は、ログアウト中にターゲットにするユーザー IDを個別に追跡し、アプリのログアウトプロセスの中でそのユーザー IDに切り替えることをお勧めします。

詳細については、[`changeUser`のドキュメント](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html)を参照してください。

### ユーザー変更イベントのサブスクライブ {#subscribing-to-user-change-events}

[`subscribeToChangeUserEvents`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-change-user-events.html)を使用して、アプリが `changeUser()` でユーザーを変更したときにロジックを実行します。このメソッドはAndroid SDK 40.0.0以降で利用できます。

サブスクライバーのコールバックは、`changeUser()` を通じてユーザーが変更されたときに実行され、`BrazeUserChangeEvent` を受け取ります。`BrazeUserChangeEvent` は、現在のユーザーが変更されたとき、またはSDKが初期化された直後に発火します。SDKは、遷移が発生していない場合でも、同じユーザーに対して複数のイベントを発火することがあります。

{% tabs %}
{% tab JAVA %}

`````````java
Braze.getInstance(context).subscribeToChangeUserEvents(new IEventSubscriber<BrazeUserChangeEvent>() {
  @Override
  public void trigger(BrazeUserChangeEvent event) {
    // Add your app logic for user changes, such as refreshing user-scoped state.
  }
});
```

{% endtab %}
{% tab KOTLIN %}

`````````kotlin
Braze.getInstance(context).subscribeToChangeUserEvents { event ->
  // Add your app logic for user changes, such as refreshing user-scoped state.
}
```

{% endtab %}
{% endtabs %}

## ユーザー ID 統合のベストプラクティスとメモ {#user-id-integration-best-practices-and-notes}

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## ユーザーのエイリアシング {#aliasing-users}

{% multi_lang_include archive/setting_user_ids/aliasing.md platform="Android" %}