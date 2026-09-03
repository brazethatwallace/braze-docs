---
nav_title: アンインストール追跡
article_title: Braze SDKを通じてアンインストールを追跡する
page_order: 3.5
description: "Braze SDKによるアンインストール追跡の設定方法について説明します。"

---

# アンインストール追跡 {#track-uninstalls}

> Braze SDKを通じてアンインストール追跡を設定する方法について説明します。一般的な情報については、[ユーザーガイド：アンインストール追跡]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking)を参照してください。

{% sdktabs %}
{% sdktab android %}
## アンインストール追跡の設定 {#setting-up-uninstall-tracking}

### ステップ 1: FCMの設定 {#step-1-set-up-fcm}

Android Braze SDKは、Firebase Cloud Messaging（FCM）を使用してサイレントプッシュ通知を送信し、アンインストール追跡分析を収集します。まだの場合は、プッシュ通知のためにFirebase Cloud Messaging APIを[設定]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android#android_setting-up-push-notifications)するか、[移行]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)してください。

### ステップ 2: 手動でアンインストール追跡を検出する（オプション） {#step-2-manually-detect-uninstall-tracking-optional}

デフォルトでは、Android Braze SDKはアンインストール追跡に関連するサイレントプッシュ通知を自動的に検出し、無視します。ただし、[`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html)メソッドを使用して手動でアンインストール追跡を検出することもできます。

{% alert important %}
アンインストール追跡用のサイレント通知はBrazeのプッシュコールバックには転送されないため、このメソッドを使用できるのは、プッシュ通知をBrazeに渡す前だけです。
{% endalert %}

### ステップ 3: 自動サーバーpingを削除する {#step-3-remove-automatic-server-pings}

サイレントプッシュ通知はアプリを起動させ、アプリがまだ実行中でなければ`Application`コンポーネントをインスタンス化します。そのため、カスタム[`Application`](https://developer.android.com/reference/android/app/Application)サブクラスがある場合は、[`Application.onCreate()`](https://developer.android.com/reference/android/app/Application#onCreate())ライフサイクルメソッド中に自動的にサーバーにpingを送るロジックをすべて削除してください。

### ステップ 4: アンインストール追跡を有効にする {#step-4-enable-uninstall-tracking}

最後に、Brazeでアンインストール追跡を有効にします。完全なチュートリアルについては、[アンインストール追跡を有効にする]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking#turning-on-uninstall-tracking)を参照してください。

{% alert important %}
アンインストールの追跡は不正確な場合があります。Brazeに表示される指標は、遅れたり不正確であったりする可能性があります。
{% endalert %}

{% endsdktab %}

{% sdktab swift %}
## アンインストール追跡の設定

### ステップ 1: バックグラウンドプッシュを有効にする {#step-1-enable-background-push}

Xcodeプロジェクトで、**Capabilities**に移動し、**Background Modes**が有効になっていることを確認します。詳しくは、[サイレントプッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift)を参照してください。

### ステップ 2: 内部プッシュ通知を無視する {#step-2-ignore-internal-push-notifications}

Swift Braze SDKは、バックグラウンドプッシュ通知を使用してアンインストール追跡分析を収集します。プッシュ通知が送信されたときにアプリが不要なアクションを起こさないようにするには、[内部プッシュ通知が無視される]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications)ようにする必要があります。

### ステップ 3: テストプッシュを送信する（オプション） {#step-3-send-a-test-push-optional}

次に、Brazeのダッシュボードからテスト用のプッシュ通知を自分に送信します（ユーザープロファイルは更新されないのでご安心ください）。

1. **メッセージング** > **キャンペーン**に進み、関連プラットフォームを使ってプッシュ通知キャンペーンを作成します。
2. **設定** > **アプリ設定**に進み、`true`値を持つ`appboy_uninstall_tracking`キーを追加し、**コンテンツ利用可能フラグを追加**にチェックを入れます。
3. **プレビュー**ページを使用して、テスト用のアンインストール追跡プッシュを自分に送信します。
4. アプリがプッシュ通知を受信したときに、不要な自動アクションを行わないことを確認します。

{% alert note %}
バッジ番号はテストプッシュ通知と一緒に送信されますが、実際のアンインストール追跡プッシュではバッジ番号は送信されません。
{% endalert %}

### ステップ 4: アンインストール追跡を有効にする

最後に、Brazeでアンインストール追跡を有効にします。完全なチュートリアルについては、[アンインストール追跡を有効にする]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking#turning-on-uninstall-tracking)を参照してください。

{% alert important %}
アンインストールの追跡は不正確な場合があります。Brazeに表示される指標は、遅れたり不正確であったりする可能性があります。
{% endalert %}

{% endsdktab %}
{% endsdktabs %}