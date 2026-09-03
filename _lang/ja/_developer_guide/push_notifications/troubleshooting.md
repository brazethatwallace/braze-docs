---
page_order: 10.9
nav_title: トラブルシューティング
article_title: Braze SDKのプッシュ通知のトラブルシューティング
description: "症状インデックス、標準的な調査パス、プラットフォーム固有のSDKチェックを使用して、プッシュ通知の配信と表示の問題を診断します。"
channel:
  - push notifications
---

# プッシュ通知のトラブルシューティング {#troubleshoot-push-notifications}

> このページでは、デバイス上のプッシュ通知の配信と表示の問題を診断します。ダッシュボード側の配信チェック（購読ステータス、セグメント、キャップ）については、[プッシュ通知のトラブルシューティング]({{site.baseurl}}/user_guide/channels/push/troubleshooting)を参照してください。

デバッグを開始する前に、自分自身を[テストユーザー]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users)として追加し、[テストメッセージの送信]({{site.baseurl}}/developer_guide/push_notifications/sending_test_messages)を確認してください。

## まずはここから：症状を確認する {#start-here-match-your-symptom}

以下の表から該当する動作を見つけて、そのセクションのステップに従ってください。どのセクションが該当するかわからない場合は、[標準的な調査パス](#standard-investigation-path)を使用してください。

| 症状 | 参照先 |
| --- | --- |
| 特定のプラットフォームでプッシュ通知が受信されない | [プラットフォーム固有のトラブルシューティング](#platform-specific-troubleshooting)でSDKタブを選択してください |
| 保存時にLiquidタグ周辺の改行がおかしくなる | [プッシュ通知の改行](#push-linebreaks) |
| ダッシュボードの配信チェック（購読、セグメント、キャップ） | [プッシュ通知のトラブルシューティング]({{site.baseurl}}/user_guide/channels/push/troubleshooting) |
| プッシュ通知からのディープリンクが正しく開かない | [ディープリンクのトラブルシューティング]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting) |
| 一般的なプッシュエラーコード | [一般的なプッシュエラーメッセージ]({{site.baseurl}}/user_guide/channels/push/push_error_codes) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="プッシュSDKの症状" }

## 標準的な調査パス {#standard-investigation-path}

すべてのプッシュ通知のインシデントに対して、このワークフローを使用してください。ステップ1から始めてください。

1. デバイスに有効なプッシュトークンがあり、デバイス設定でプッシュ通知の許可が付与されていることを確認します。
2. ダッシュボードで、テストユーザーがキャンペーンまたはキャンバスの[セグメント]({{site.baseurl}}/user_guide/channels/push/troubleshooting#segment)に一致しており、[コントロールグループ]({{site.baseurl}}/user_guide/channels/push/troubleshooting#control-group-status)に含まれていないことを確認します。
3. テストデバイスに[テストプッシュ]({{site.baseurl}}/developer_guide/push_notifications/sending_test_messages)を送信します。
4. [詳細ログを有効にし]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)、問題を再現して、[SDKタブ](#platform-specific-troubleshooting)でプラットフォーム固有のガイダンスを確認します。
5. 問題が解決しない場合は、詳細ログ、プラットフォーム、SDKバージョン、キャンペーンまたはキャンバスIDを添えて[Brazeサポート]({{site.baseurl}}/braze_support)にお問い合わせください。

## プラットフォーム固有のトラブルシューティング {#platform-specific-troubleshooting}

SDKタブを選択して、プラットフォーム固有の設定と表示の確認を行ってください。

{% sdktabs %}
{% sdktab web %}
## トラブルシューティング {#troubleshooting}

プッシュ通知の設定後に問題が発生した場合は、以下を確認してください。

- Webプッシュ通知には、サイトがHTTPSである必要があります。
- すべてのブラウザーがプッシュメッセージを受信できるわけではありません。ブラウザーで`braze.isPushSupported()`が`true`を返すことを確認してください。
- Firefoxなど一部のブラウザーでは、プッシュ通知に画像が表示されません。ブラウザーサポートの詳細については、[MDNのNotification imageドキュメント](https://developer.mozilla.org/en-US/docs/Web/API/Notification/image)を参照してください。
- ユーザーがサイトのプッシュアクセスを拒否した場合、ブラウザーの設定から拒否ステータスを削除しない限り、再度許可を求めるプロンプトは表示されません。

{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab swift %}
## Braze/APNsワークフローの理解 {#understanding-the-brazeapns-workflow}

Apple Push Notification service（APNs）は、Appleのプラットフォーム上で動作するアプリにプッシュ通知を送信するためのインフラです。ユーザーのデバイスでプッシュ通知が有効になり、Brazeがプッシュ通知を送信する仕組みの概要は以下のとおりです。

{% multi_lang_include developer_guide/push_notifications/push_registration_flow_steps.md %}

### ステップ1：プッシュ証明書とプロビジョニングプロファイルの設定 {#step-1-configuring-the-push-certificate-and-provisioning-profile}

アプリを開発するには、プッシュ通知を有効にするSSL証明書を作成します。この証明書はアプリのビルドに使用されるプロビジョニングプロファイルに含まれ、Brazeダッシュボードにもアップロードする必要があります。この証明書により、Brazeはお客様に代わってプッシュ通知を送信する権限があることをAPNsに通知できます。

[プロビジョニングプロファイル](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html)と証明書には、開発用と配布用の2種類があります。混乱を避けるため、配布用のプロファイルと証明書のみを使用することを推奨します。開発用と配布用で異なるプロファイルと証明書を使用する場合は、ダッシュボードにアップロードした証明書が、現在使用しているプロビジョニングプロファイルと一致していることを確認してください。

{% alert warning %}
プッシュ証明書の環境（開発用と本番用）を変更しないでください。プッシュ証明書を間違った環境に変更すると、ユーザーのプッシュトークンが誤って削除され、プッシュで到達できなくなる可能性があります。
{% endalert %}

### ステップ2：デバイスがAPNsに登録し、Brazeにプッシュトークンを提供する {#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens}

ユーザーがアプリを開くと、プッシュ通知の許可を求めるプロンプトが表示されます。許可された場合、APNsはその特定のデバイスに対してプッシュトークンを生成します。Swift SDKは、デフォルトの[自動フラッシュポリシー]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/advanced_use_cases/fine_network_traffic_control#automatic-request-processing)を使用するアプリについて、プッシュトークンを即座に非同期で送信します。ユーザーに関連付けられたプッシュトークンを取得すると、ダッシュボードのユーザープロファイルの**エンゲージメント**タブで「プッシュ登録済み」と表示され、Brazeキャンペーンからプッシュ通知を受信する資格が得られます。

{% alert note %}
macOS 13以降、特定のデバイスでは、Xcode 14上で動作するiOS 16シミュレーターでプッシュ通知をテストできます。詳細については、[Xcode 14リリースノート](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes)を参照してください。
{% endalert %}

#### プッシュトークン生成に関する考慮事項 {#considerations-for-push-token-generation}

- ユーザーが別のデバイスにアプリをインストールした場合、Brazeは同じ方法で別のトークンを作成しキャプチャします。
- ユーザーがアプリを再インストールした場合、SDKは新しいトークンを生成してBrazeに渡します。ただし、APNsとBrazeは元のトークンを引き続き有効として記録する場合があります。
- ユーザーがアプリをアンインストールした場合、Brazeはすぐに通知を受け取らず、APNsがトークンを無効化するまでトークンは有効として表示されます。
- ある時点で、APNsは古いトークンを無効化します。Brazeはこれを制御したり、可視性を持つことはできません。

### ステップ3：Brazeプッシュキャンペーンの起動 {#step-3-launching-a-braze-push-campaign}

プッシュキャンペーンが起動されると、Brazeはメッセージを配信するためにAPNsにリクエストを送信します。具体的には、**ユーザーの最新のデバイスに送信する**が選択されていない限り、現在有効なプッシュトークンごとにリクエストが渡されます。BrazeがAPNsから成功レスポンスを受信した後、ユーザープロファイルに配信成功が記録されますが、以下の理由を含め、ユーザーが実際にメッセージを受信していない場合があります。
- デバイスの電源がオフになっている。
- デバイスがインターネット（Wi-Fiまたはセルラー）に接続されていない。
- 最近アプリをアンインストールした。

Brazeは、ダッシュボードにアップロードされたSSLプッシュ証明書を使用して認証を行い、提供されたプッシュトークンにプッシュ通知を送信する権限があることを確認します。デバイスがオンラインの場合、キャンペーンの送信後すぐに通知を受信するはずです。Brazeは、通知のデフォルトのAPNs[有効期限](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607)を30日に設定しています。

### ステップ4：無効なトークンの削除 {#step-4-removing-invalid-tokens}

メッセージの送信先のプッシュトークンが無効であることを[APNs](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1)から通知された場合、関連付けられているユーザープロファイルからそれらのトークンを削除します。

{% alert note %}
トークンが未登録になった場合でも、APNsが最初に成功ステータスを返すのは正常な動作です。APNsはトークンの無効化イベントをすぐには報告しません。APNsは、ユーザーのプライバシーを保護し、アプリのアンインストールの追跡を防止するために設計されたランダム化されたスケジュールで、無効なトークンに対する`410`ステータスの返却を意図的に遅延させます。APNsが`410`ステータスを返すまで、未登録のトークンに対して通知を送信し続けても問題ありません。
{% endalert %}

## プッシュエラーログの使用 {#using-the-push-error-logs}

[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab)では、キャンペーンや送信に関連するメッセージ（特にエラーメッセージ）を確認できます。これにはプッシュ通知のエラーも含まれます。このエラーログには、キャンペーンが期待どおりに動作しない理由を特定するのに非常に役立つ様々な警告が表示されます。エラーメッセージを選択すると、特定のインシデントのトラブルシューティングに役立つ関連ドキュメントにリダイレクトされます。

![エラーが発生した時刻、アプリ名、チャネル、エラータイプ、エラーメッセージを表示するプッシュエラーログ。]({% image_buster /assets/img_archive/message_activity_log.png %})

ここで表示される一般的なエラーには、[「未登録の送信先へのプッシュトークン受信」](#swift_received-unregistered-sending)などのユーザー固有の通知が含まれます。

さらに、Brazeはユーザープロファイルの**エンゲージメント**タブにプッシュ変更ログも提供しています。この変更ログは、トークンの無効化、プッシュ登録エラー、トークンが新しいユーザーに移動されたことなど、プッシュ登録の動作に関するインサイトを提供します。

![Brazeのユーザープロファイルのエンゲージメントタブに表示されるプッシュ登録変更ログ。]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

### メッセージアクティビティログのエラー {#message-activity-log-errors}

#### 未登録の送信先へのプッシュトークン受信 {#received-unregistered-sending}

- `AppDelegate.braze?.notifications.register(deviceToken:)`メソッドからBrazeに送信されているプッシュトークンが有効であることを確認してください。**メッセージアクティビティログ**でプッシュトークンを確認できます。`6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`のような、文字と数字が混在した長い文字列のように表示されるはずです。プッシュトークンが異なる場合は、Brazeにプッシュトークンを送信する[コード]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-32-register-push-tokens-with-braze)を確認してください。
- プッシュプロビジョニングプロファイルがテスト中の環境と一致していることを確認してください。ユニバーサル証明書は、Brazeダッシュボードで開発用または本番用のAPNs環境に送信するように設定できます。本番アプリに開発用証明書を使用したり、開発アプリに本番用証明書を使用したりすることはできません。
 - Brazeにアップロードしたプッシュトークンが、プッシュトークンの送信元アプリのビルドに使用したプロビジョニングプロファイルと一致していることを確認してください。

#### デバイストークンがトピックに対応していない {#device-token-not-for-topic}

APNsは、プッシュトークンが認証情報に設定されたトピック（バンドルID）と一致しない場合に`DeviceTokenNotForTopic`（HTTPステータス400）を返します。Brazeはこれを**メッセージアクティビティログ**またはプッシュ配信ログに`DeviceTokenNotForTopic`として表示する場合があります。

この不一致を解決するには、以下の手順を実行してください。

1. アプリの**バンドルID**がBrazeの**App Bundle ID**（**設定** > **アプリの設定** > **プッシュ通知設定**）と一致していることを確認します。
2. アプリのビルドに使用したプロビジョニングプロファイルに、そのバンドルIDのプッシュ機能が含まれていることを確認します。
3. Brazeにアップロードしたプッシュ認証情報がアプリの環境（開発用と本番用）と一致していることを確認します。
4. `.p8`キーの場合、Brazeの**Team ID**と**Key ID**がApple Developerアカウントと一致していることを確認します。
5. 認証情報がローテーションまたは失効された場合は、有効な`.p8`キーまたは`.p12`証明書を再アップロードします。

可能な場合は`.p8`認証キーを使用することを推奨します。認証情報の種類とダッシュボードのステータスインジケーターについては、[.p8認証キーへの移行]({{site.baseurl}}/user_guide/channels/push/troubleshooting#migrate-to-a-p8-authentication-key)を参照してください。

#### BadDeviceTokenがプッシュトークンに送信された {#baddevicetoken-sending-to-push-token}

`BadDeviceToken`はAPNsのエラーコードであり、Brazeから発信されるものではありません。このレスポンスが返される理由は複数考えられ、以下が含まれます。

{% multi_lang_include developer_guide/push_notifications/invalid_push_token_reasons.md %}

## プッシュ登録の問題 {#push-registration-issues}

### プッシュ登録プロンプトが表示されない {#no-push-registration-prompt}

アプリがプッシュ通知の登録プロンプトを表示しない場合、プッシュ登録の統合に問題がある可能性があります。[ドキュメント]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)に従い、プッシュ登録を正しく統合していることを確認してください。また、コードにブレークポイントを設定して、プッシュ登録コードが実行されていることを確認することもできます。

### ダッシュボードに「プッシュ登録済み」のユーザーが表示されない（メッセージ送信前） {#no-push-registered-users-showing-in-the-dashboard-prior-to-sending-messages}

アプリがプッシュ通知を許可するように正しく設定されていることを確認してください。確認すべき一般的な障害ポイントは以下のとおりです。

- アプリがプッシュ通知の許可を求めるプロンプトを表示していることを確認します。通常、このプロンプトはアプリの初回起動時に表示されますが、別の場所に表示するようにプログラムすることもできます。表示されるべき場所に表示されない場合は、アプリのプッシュ機能の基本設定に問題がある可能性があります。
  - [プッシュ通知の統合]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)の手順が正常に完了したことを確認してください。
  - アプリのビルドに使用したプロビジョニングプロファイルにプッシュの権限が含まれていることを確認します。Apple Developerアカウントから利用可能なすべてのプロビジョニングプロファイルを取得していることを確認してください。確認するには、以下の手順を実行します。
    1. Xcodeで、**Preferences > Accounts**（またはキーボードショートカット<kbd>Command</kbd>+<kbd>,</kbd>）に移動します。
    2. 開発者アカウントに使用しているApple IDを選択し、**View Details**をクリックします。
    3. 次のページで**<i class="fas fa-redo-alt"></i> Refresh**をクリックし、利用可能なすべてのプロビジョニングプロファイルを取得していることを確認します。
- アプリで[プッシュ機能を適切に有効化]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-2-enable-push-capabilities)していることを確認してください。
- プッシュプロビジョニングプロファイルがテスト中の環境と一致していることを確認します。ユニバーサル証明書は、Brazeダッシュボードで開発用または本番用のAPNs環境に送信するように設定できます。本番アプリに開発用証明書を使用したり、開発アプリに本番用証明書を使用したりすることはできません。
- コードにブレークポイントを設定して、`registerPushToken`メソッドを呼び出していることを確認してください。
- デバイスを使用してテストしていること（プッシュはシミュレーターでは動作しません）、およびネットワーク接続が良好であることを確認してください。

## プッシュ通知が送信されたがユーザーのデバイスに表示されない {#push-notifications-sent-but-not-displayed-on-users-devices}

### メッセージ送信後に「プッシュ登録済み」のユーザーが無効になる {#push-registered-users-no-longer-enabled-after-sending-messages}

これは、ユーザーのプッシュトークンが無効であることを示している可能性があります。これにはいくつかの原因が考えられます。

#### ダッシュボードとアプリの証明書の不一致 {#dashboard-and-app-certificate-mismatch}

ダッシュボードにアップロードしたプッシュ証明書が、アプリのビルドに使用したプロビジョニングプロファイルのものと一致しない場合、APNsはトークンを拒否します。正しい証明書をアップロードしたことを確認し、別のテスト通知を試す前にアプリで別のセッションを完了してください。

#### アプリがアンインストールされた {#application-was-uninstalled}

ユーザーがアプリをアンインストールした場合、プッシュトークンは無効になり、次回の送信時に削除されます。

#### プロビジョニングプロファイルの再生成 {#regenerating-your-provisioning-profile}

最後の手段として、最初からやり直して完全に新しいプロビジョニングプロファイルを作成することで、複数の環境、プロファイル、アプリを同時に扱う際に生じる設定エラーを解消できます。プッシュ通知の設定には多くの「可動部分」があるため、最初からやり直すのが最善の場合があります。これにより、トラブルシューティングを続ける必要がある場合にも問題を切り分けることができます。

### 「プッシュ登録済み」のユーザーにメッセージが配信されない {#messages-not-delivered-to-push-registered-users}

#### アプリがフォアグラウンドにある {#app-is-foregrounded}

`UserNotifications`フレームワーク経由でプッシュを統合していないiOSバージョンでは、プッシュメッセージの受信時にアプリがフォアグラウンドにある場合、メッセージは表示されません。テストメッセージを送信する前に、テストデバイスでアプリをバックグラウンドにしてください。

#### テスト通知のスケジュールが正しくない {#test-notification-scheduled-incorrectly}

テストメッセージに設定したスケジュールを確認してください。ローカルタイムゾーン配信または[インテリジェントタイミング]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing)に設定されている場合、まだメッセージを受信していない可能性があります（または受信時にアプリがフォアグラウンドにあった可能性があります）。

### テスト対象のアプリでユーザーが「プッシュ登録済み」でない {#user-not-push-registered-for-the-app-being-tested}

テストメッセージを送信しようとしているユーザーのユーザープロファイルを確認してください。**エンゲージメント**タブに「プッシュ可能なアプリ」のリストが表示されるはずです。テストメッセージを送信しようとしているアプリがこのリストに含まれていることを確認してください。ユーザーは、ワークスペース内のいずれかのアプリにプッシュトークンがあれば「プッシュ登録済み」と表示されるため、これは誤検知の可能性があります。

以下は、プッシュ登録に問題がある、またはユーザーのトークンがプッシュ後にAPNsによって無効としてBrazeに返されたことを示しています。

![ユーザーの連絡先設定を表示するユーザープロファイル。プッシュの下に「アプリなし」と表示されている。]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## プッシュクリックが記録されない {#push-clicks-not-logged}

- [プッシュ通知の統合ステップ]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling)に従っていることを確認してください。
- Brazeは、フォアグラウンドでサイレントに受信されたプッシュ通知を処理しません（`UserNotifications`フレームワーク導入前のデフォルトのフォアグラウンドプッシュ動作）。つまり、リンクは開かれず、プッシュクリックも記録されません。アプリがまだ`UserNotifications`フレームワークを統合していない場合、アプリの状態が`UIApplicationStateActive`のときにBrazeはプッシュ通知を処理しません。アプリが[プッシュ処理メソッド]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling)の呼び出しを遅延させないようにしてください。遅延させると、Swift SDKがプッシュ通知をサイレントフォアグラウンドプッシュイベントとして扱い、処理しない場合があります。

## ディープリンクが動作しない {#deep-links-not-working}

プッシュ、メール、サードパーティプロバイダー（Branchなど）を含むすべてのチャネルにわたるユニバーサルリンク、カスタムスキームの包括的なトラブルシューティングについては、[ディープリンクのトラブルシューティング]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting)を参照してください。

### プッシュクリックからのWebリンクが開かない {#web-links-from-push-clicks-not-opening}

プッシュ通知内のリンクは、Webビューで開くためにATSに準拠している必要があります。WebリンクがHTTPSを使用していることを確認してください。詳細については、[ATSコンプライアンス]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/advanced_use_cases/linking#app-transport-security-ats)を参照してください。

### プッシュクリックからのディープリンクが開かない {#deep-links-from-push-clicks-not-opening}

ディープリンクを処理するコードの大部分は、プッシュの開封も処理します。まず、プッシュの開封が記録されていることを確認してください。記録されていない場合は、その問題を修正してください（修正することでリンク処理も修正されることがよくあります）。

開封が記録されている場合は、問題がディープリンク全般にあるのか、ディープリンクのプッシュクリック処理にあるのかを確認します。これを確認するには、アプリ内メッセージのクリックからディープリンクが機能するかどうかをテストしてください。

### Push Storyの画像タップが反応しない {#push-story-image-taps-do-nothing}

Push Storyの画像をタップしても何も起こらない場合は、Notification Content Extensionの`Info.plist`を開き、`UNNotificationExtensionUserInteractionEnabled`が`YES`に設定されていることを確認してください。Swift SDKの`BrazePushStory`モジュールは、エクステンションがタップを受信できるようにするためにこのキーを必要とします。[Push Stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories/?sdktab=swift)を参照してください。

{% endsdktab %}

{% sdktab fireos %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
## トラブルシューティング

### タスクスイッチャーからアプリを閉じた後にプッシュが表示されない {#push-doesnt-appear-after-app-is-closed-from-task-switcher}

タスクスイッチャーからアプリを閉じた後にプッシュ通知が表示されなくなった場合、アプリがDebugモードで動作している可能性があります。.NET MAUIはDebugモードでスキャフォールディングを追加するため、プロセスが終了した後にアプリがプッシュを受信できなくなります。アプリをReleaseモードで実行すると、タスクスイッチャーからアプリを閉じた後でもプッシュが表示されるはずです。

### カスタム通知ファクトリが正しく設定されていない {#custom-notification-factory-not-being-set-correctly}

カスタム通知ファクトリ（およびすべてのデリゲート）は、C#とJava間で正しく動作するために[`Java.Lang.Object`](https://developer.xamarin.com/api/type/Android.Runtime.IJavaObject/)を継承する必要があります。詳細については、Javaインターフェイスの実装に関する[Xamarin](https://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/working_with_jni/#Implementing_Interfaces)を参照してください。

{% endsdktab %}
{% endsdktabs %}

## プッシュ通知の改行 {#push-linebreaks}

Liquidタグを使用してプッシュ通知を作成する場合、Liquidタグに隣接する改行はメッセージ送信前に自動的に削除されます。[プッシュ通知コンポーザー]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message)では、編集中にメッセージが読みやすいようにこれらの改行が再追加されます。メッセージを保存する際にLiquidタグの前後に改行が表示される場合、これは想定どおりの動作です。