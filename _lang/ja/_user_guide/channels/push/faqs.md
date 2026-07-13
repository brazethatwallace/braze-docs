---
nav_title: FAQ
article_title: FAQ
page_order: 30
description: "この記事では、プッシュキャンペーンの設定時に最もよく寄せられる質問について説明します。"
page_type: FAQ
channel:
  - Push
---

# よくある質問 {#frequently-asked-questions}

> この記事では、プッシュチャネルに関するよくある質問への回答を提供します。

## プッシュ通知が遅延することがあるのはなぜですか？ {#why-are-push-notifications-sometimes-delayed}

配信は通常、3つの段階を経ます。Brazeの**処理**（セグメンテーション、スケジューリング、プロバイダーへの引き渡し）、Brazeから**APNsまたはFCM**への転送、プロバイダーから**デバイス**への配信です。遅延はどの段階でも発生する可能性があります。Brazeはプロバイダーやデバイスのキューを可視化できません。デバイス側のタイミングを絞り込む必要がある場合は、クライアントで[詳細ログ]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs)を使用してください。

## 1つのデバイスに複数のユーザーがログインするとどうなりますか？ {#what-happens-when-multiple-users-log-into-a-single-device}

ユーザーがデバイスまたはWebサイトからログアウトしても、別のユーザーがログインするまでプッシュで到達可能な状態が続きます。別のユーザーがログインした時点で、プッシュトークンは新しいユーザーに再割り当てされます。これは、各デバイスがアプリまたはWebサイトごとに1つのアクティブなプッシュサブスクリプションしか持てないためです。

プッシュトークンが再割り当てされると、その変更はユーザープロファイルの**プッシュ変更ログ**に反映されます。ユーザープロファイルの**エンゲージメント**タブに移動すると確認できます。

![「連絡先設定」セクションの「プッシュ変更ログ」。]({% image_buster /assets/img/push_changelog_faq.png %}){: style="max-width:50%;"}

## テストプッシュを送信すると、すべてのデバイスに届きますか？ {#when-i-send-a-test-push-does-it-go-to-all-of-my-devices}

はい。テストプッシュは、選択したユーザープロファイルに関連付けられたプッシュ有効なすべてのデバイスに送信されます。同じユーザーで複数のスマートフォンやタブレットにログインしている場合、有効なプッシュトークンを持つ各デバイスが通知を受信します。

テストプッシュを1つのデバイスにのみ送信するには、テスト前にユーザープロファイルから他のデバイスのプッシュトークンを削除します。または、[`/messages/send`エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)で送信する場合は、`apple_push`または`android_push`オブジェクトで`send_to_most_recent_device_only`を`true`に設定すると、最も最近アクティブだったデバイスのみがプッシュを受信します。

## 「ペイロードが無効なためプッシュの送信エラー」とはどういう意味ですか？ {#what-does-error-sending-push-because-the-payload-was-invalid-mean}

このメッセージは、無効なペイロード（例：空のペイロードやサイズが大きすぎるペイロード）が原因で、APNsがプッシュリクエストを拒否したことを示しています。

詳細と次のステップについては、[一般的なプッシュエラーメッセージ]({{site.baseurl}}/user_guide/channels/push/push_error_codes)を参照してください。

## オプトインしたユーザーにプッシュトークンがないのはなぜですか？ {#why-doesnt-an-opted-in-user-have-a-push-token}

これは、同じデバイスを使用した別のユーザーにプッシュトークンが再割り当てされた場合に発生することがあります。

1. 該当するユーザーのプロファイルの**エンゲージメント**タブにある**プッシュ変更ログ**に移動します。
2. プッシュトークンが別のユーザーに移動されたというメッセージを探します。
3. プッシュトークンをコピーしてユーザー検索バーに貼り付けます。
4. プッシュトークンがまだ存在する場合、そのデバイスで最も最近ログインしたユーザーに移動します。

プッシュトークンを元のユーザーに再割り当てしたい場合：

1. プッシュトークンが欠落しているプロファイルに元のユーザーをログインさせます。
2. 新しいプッシュ送信をトリガーします。デバイスレベルでプッシュが有効になっている場合、トークンがそのアカウントに戻されます。

## 下書きキャンペーンのテスト時に「モバイルアプリ内でWeb URLを開く」が常にアプリを開くのはなぜですか？ {#why-does-open-web-url-inside-mobile-app-always-open-the-app-when-im-testing-a-draft-campaign}

キャンペーンがまだ**下書き**ステータスの場合、テストプッシュを送信して通知をタップすると、**モバイルアプリ内でWeb URLを開く**オプションが選択されているかどうかに関係なく、常にアプリが最初に開きます。キャンペーンが**ライブ**の場合、クリック時の動作は設定どおりに機能します。

**アプリ内**オプションなしで**Web URLを開く**を選択した場合、リンクはデバイスのデフォルトブラウザで直接開きます。**モバイルアプリ内でWeb URLを開く**を選択した場合、リンクはアプリ内Webビューで開きます。

## iOSプッシュ証明書の「Send to Production」と「Send to Development」の違いは何ですか？ {#what-is-the-difference-between-send-to-production-and-send-to-development-for-ios-push-certificates}

BrazeでAppleプッシュ証明書を追加する際、**Send to Production**と**Send to Development**のオプションは、Brazeがプッシュ通知を配信するために使用するAPNs（Apple Push Notification service）ゲートウェイを決定します。

- **Send to Development：** Xcodeで開発モードでビルドされ、開発プロビジョニングプロファイルで署名されたアプリの場合に選択します。プッシュ通知はAppleの開発（サンドボックス）ゲートウェイを通じてルーティングされます。
- **Send to Production：** AppleのTestFlight、App Store、またはエンタープライズ配布を通じて配布されるアプリの場合に選択します。プッシュ通知はAppleの本番ゲートウェイを通じてルーティングされます。

間違ったオプションを選択すると、プッシュトークンの種類がゲートウェイと一致しないため、プッシュ通知がサイレントに失敗します。通常、TestFlightまたはApp Storeを通じて配布されるアプリは**Send to Production**を使用する必要があります。

## 「Foreground Push Enabled」フィルターと「Background or Foreground Push Enabled」フィルターの違いは何ですか？ {#what-is-the-difference-between-the-foreground-push-enabled-and-background-or-foreground-push-enabled-filters}

これらのセグメンテーションフィルターは、異なる条件をチェックします。

| フィルター | チェック内容 | ユースケース |
|--------|---------------|----------|
| **Foreground Push Enabled** | ユーザーが有効なフォアグラウンドプッシュトークンを持ち、**かつ**プッシュサブスクリプション状態が`Opted-In`または`Subscribed`である。 | 可視プッシュ通知を受信できるユーザーをターゲットにします。 |
| **Background or Foreground Push Enabled** | ユーザーがいずれかのプッシュトークン（フォアグラウンドまたはバックグラウンド）を持ち、**かつ**プッシュサブスクリプション状態が`Opted-In`または`Subscribed`である。これには、可視プッシュ通知を無効にしているがバックグラウンドプッシュトークンを保持しているユーザーも含まれます。 | [アンインストール追跡]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking)、[サイレントプッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/silent)、およびジオフェンシングに使用されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="「Foreground Push Enabled」フィルターと「Background or Foreground Push Enabled」フィルターの違い" }

ユーザーは`Foreground Push Enabled`でなくても`Background or Foreground Push Enabled`になることがあります。これは、ユーザーがデバイス設定で可視プッシュ通知を無効にしているが、アプリがバックグラウンドプッシュトークンを保持している場合に発生します。詳細については、[プッシュユーザーとサブスクリプション]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#foreground-push-enabled)を参照してください。

## Brazeはプッシュメッセージがいつ正常に送信されたかをどのように判断しますか？ {#how-does-braze-determine-when-a-push-message-is-sent-successfully}

メッセージは、プッシュサービスプロバイダーによって受信された時点で送信済みとして記録されます。これは、ユーザーがメッセージを受信または閲覧したことを必ずしも意味するものではありません。

iOSの場合、プッシュサービスプロバイダーはApple Push Notification Service（APNs）であり、Androidの場合は通常Firebase Cloud Messaging（FCM）です。プッシュサービスプロバイダーは即座に成功または失敗を返します。失敗にはバウンスやネットワーク障害による再試行が含まれる場合があります。

成功メッセージが返された場合、送信はBrazeによって記録され、その後プッシュサービスがデバイスへの配信を試みます。デバイスにすぐに到達できない場合、サービスはBrazeで設定された有効期限オプション（Androidの場合は**TTL**、iOSの場合は**有効期限**）まで再試行します。メッセージがタイムアウトした場合、プッシュサービスはプッシュを破棄しますが、バウンスとはみなされません。

- アクションベースの配信プッシュキャンペーンの場合、メッセージ送信はユーザーがキャンペーンをトリガーするアクションを実行した時点で記録されます。
- スケジュールされたキャンペーンの場合、送信時間はメッセージがキューに入れられ、プッシュサービスプロバイダーに渡された時間です。
- どちらの配信タイプでも、ユーザーがまだプッシュを閲覧または受信していなくても、メッセージはBrazeおよびユーザープロファイルの**受信したキャンペーン**で「送信済み」としてマークされます。

ダッシュボードのプッシュの「配信」指標は、ページ読み込み時に送信数からバウンス数を差し引いた値として計算されます。