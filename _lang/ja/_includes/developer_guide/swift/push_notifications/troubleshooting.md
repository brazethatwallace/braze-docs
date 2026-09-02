## Braze/APNsワークフローの理解 {#understanding-the-brazeapns-workflow}

Apple Push Notification service（APNs）は、Appleのプラットフォーム上で動作するアプリケーションにプッシュ通知を送信するためのインフラです。ここでは、ユーザーのデバイスでプッシュ通知が有効になる仕組みと、Brazeがプッシュ通知を送信する方法を簡略化して説明します。

1. プッシュ証明書とプロビジョニングプロファイルを設定する
2. デバイスがAPNsに登録し、Brazeにプッシュトークンを提供する
3. Brazeのプッシュキャンペーンを起動する
4. Brazeが無効なトークンを削除する

### ステップ1：プッシュ証明書とプロビジョニングプロファイルの設定 {#step-1-configuring-the-push-certificate-and-provisioning-profile}

アプリの開発時に、プッシュ通知を有効にするためのSSL証明書を作成する必要があります。この証明書はアプリのビルドに使用されるプロビジョニングプロファイルに含まれ、Brazeダッシュボードにもアップロードする必要があります。この証明書により、Brazeはお客様に代わってプッシュ通知を送信する許可があることをAPNsに伝えることができます。

[プロビジョニングプロファイル](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html)と証明書には、開発用と配布用の2種類があります。混乱を避けるため、配布用のプロファイルと証明書のみを使用することをお勧めします。開発用と配布用で異なるプロファイルと証明書を使用する場合は、ダッシュボードにアップロードした証明書が現在使用中のプロビジョニングプロファイルと一致していることを確認してください。

{% alert warning %}
プッシュ証明書の環境（開発と本番）を変更しないでください。プッシュ証明書を誤った環境に変更すると、ユーザーのプッシュトークンが誤って削除され、プッシュ通知で到達できなくなる可能性があります。
{% endalert %}

### ステップ2：デバイスがAPNsに登録し、Brazeにプッシュトークンを提供する {#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens}

ユーザーがアプリを開くと、プッシュ通知の受け入れを求めるプロンプトが表示されます。このプロンプトを受け入れると、APNsはその特定のデバイスに対してプッシュトークンを生成します。Swift SDKは、デフォルトの[自動フラッシュポリシー]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/fine_network_traffic_control#automatic-request-processing)を使用しているアプリに対して、プッシュトークンを即座に非同期で送信します。ユーザーに関連付けられたプッシュトークンを取得すると、そのユーザーはダッシュボードのユーザープロファイルの**エンゲージメント**タブに「プッシュ登録済み」と表示され、Brazeキャンペーンからプッシュ通知を受信する資格を得ます。

{% alert note %}
macOS 13以降では、特定のデバイスで、Xcode 14上で動作するiOS 16シミュレーターでプッシュ通知をテストできます。詳細については、[Xcode 14リリースノート](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes)を参照してください。
{% endalert %}

#### プッシュトークン生成に関する考慮事項 {#considerations-for-push-token-generation}

- ユーザーが別のデバイスにアプリをインストールすると、同じ方法で別のトークンが作成されキャプチャされます。
- ユーザーがアプリを再インストールすると、新しいトークンが生成されBrazeに渡されます。ただし、元のトークンはAPNsとBrazeによってまだ有効として記録されている場合があります。
- ユーザーがアプリをアンインストールした場合、Brazeはすぐには通知を受けず、トークンはAPNsによって無効化されるまで有効として表示されます。
- ある時点でAPNsは古いトークンを無効化します。Brazeはこれを制御したり確認したりすることはできません。

### ステップ3：Brazeプッシュキャンペーンの起動 {#step-3-launching-a-braze-push-campaign}

プッシュキャンペーンが起動されると、Brazeはメッセージを配信するためにAPNsにリクエストを行います。具体的には、**ユーザーの最新のデバイスに送信**が選択されていない限り、現在有効な各プッシュトークンに対してリクエストがAPNsに送信されます。BrazeがAPNsから成功レスポンスを受信すると、ユーザープロファイルに配信成功として記録しますが、以下の理由によりユーザーが実際のメッセージを受信していない場合があります。
- デバイスの電源がオフになっている。
- デバイスがインターネット（Wi-Fiまたはセルラー）に接続されていない。
- ユーザーが最近アプリをアンインストールした。

BrazeはダッシュボードにアップロードされたSSLプッシュ証明書を使用して認証し、提供されたプッシュトークンにプッシュ通知を送信する許可があることを確認します。デバイスがオンラインの場合、キャンペーンの送信後すぐに通知を受信するはずです。なお、BrazeはAPNsの通知のデフォルトの[有効期限](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607)を30日に設定しています。

### ステップ4：無効なトークンの削除 {#step-4-removing-invalid-tokens}

メッセージの送信を試みたプッシュトークンのいずれかが無効であると[APNs](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1)から通知された場合、それらのトークンは関連付けられていたユーザープロファイルから削除されます。

{% alert note %}
トークンが未登録になった場合でも、APNsが最初に成功ステータスを返すのは正常な動作です。APNsはトークンの無効化イベントを即座に報告しません。APNsは、ユーザーのプライバシーを保護し、アプリのアンインストールの追跡を防止するために設計されたランダムなスケジュールで、無効なトークンに対する`410`ステータスの返却を意図的に遅延させます。APNsが`410`ステータスを返すまで、未登録のトークンに対して通知の送信を安全に続けることができます。
{% endalert %}

## プッシュエラーログの使用 {#using-the-push-error-logs}

[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)では、キャンペーンや送信に関連するメッセージ（特にエラーメッセージ）を確認できます。プッシュ通知のエラーも含まれます。このエラーログには、キャンペーンが期待どおりに動作しない理由を特定するのに非常に役立つさまざまな警告が表示されます。エラーメッセージをクリックすると、特定のインシデントのトラブルシューティングに役立つ関連ドキュメントにリダイレクトされます。

![エラーが発生した時刻、アプリ名、チャネル、エラータイプ、エラーメッセージを表示するプッシュエラーログ。]({% image_buster /assets/img_archive/message_activity_log.png %})

ここで表示される一般的なエラーには、[「Received Unregistered Sending to Push Token」](#swift_received-unregistered-sending)などのユーザー固有の通知があります。

さらに、Brazeはユーザープロファイルの**エンゲージメント**タブにプッシュ変更ログも提供しています。この変更ログでは、トークンの無効化、プッシュ登録エラー、トークンが新しいユーザーに移動されたことなど、プッシュ登録の動作に関するインサイトを確認できます。

![プッシュ登録の変更ログを表示するBrazeユーザープロファイルのエンゲージメントタブ。]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

### メッセージアクティビティログのエラー {#message-activity-log-errors}

#### 未登録のプッシュトークンへの送信を受信 {#received-unregistered-sending}

- `AppDelegate.braze?.notifications.register(deviceToken:)` メソッドからBrazeに送信されるプッシュトークンが有効であることを確認してください。**メッセージアクティビティログ**でプッシュトークンを確認できます。`6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6` のような、文字と数字が混在した長い文字列のように見えるはずです。プッシュトークンが異なる形式の場合は、Brazeにプッシュトークンを送信するための[コード]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-4-register-push-tokens-with-braze)を確認してください。
- プッシュプロビジョニングプロファイルがテスト中の環境と一致していることを確認してください。ユニバーサル証明書は、Brazeダッシュボードで開発用または本番用のAPNs環境のいずれかに送信するよう構成できます。本番アプリに開発用証明書を使用したり、開発用アプリに本番用証明書を使用したりすると動作しません。
 - Brazeにアップロードしたプッシュトークンが、プッシュトークンの送信元アプリのビルドに使用したプロビジョニングプロファイルと一致していることを確認してください。

#### デバイストークンがトピックに一致しない {#device-token-not-for-topic}

APNsは、プッシュトークンが認証情報に構成されたトピック（バンドルID）と一致しない場合、`DeviceTokenNotForTopic`（HTTPステータス400）を返します。Brazeは**メッセージアクティビティログ**またはプッシュ配信ログにこれを `DeviceTokenNotForTopic` として表示する場合があります。

不一致を解決するには：

1. アプリの**バンドルID**がBrazeの**App Bundle ID**（**設定** > **アプリ設定** > **プッシュ通知設定**）と一致していることを確認します。
2. アプリのビルドに使用したプロビジョニングプロファイルに、そのバンドルIDのプッシュ機能が含まれていることを確認します。
3. Brazeにアップロードしたプッシュ認証情報がアプリの環境（開発用と本番用）と一致していることを確認します。
4. `.p8` キーの場合、Brazeの**Team ID**と**Key ID**がApple Developerアカウントと一致していることを確認します。
5. 認証情報がローテーションまたは取り消された場合は、有効な `.p8` キーまたは `.p12` 証明書を再アップロードします。

可能な場合は `.p8` 認証キーを使用してください。認証情報の種類とダッシュボードのステータスインジケーターについては、[.p8 認証キーへの移行]({{site.baseurl}}/user_guide/channels/push/troubleshooting#migrate-to-a-p8-authentication-key)を参照してください。

#### プッシュトークンへの送信でBadDeviceTokenが発生 {#baddevicetoken-sending-to-push-token}

`BadDeviceToken` はAPNsのエラーコードであり、Brazeから発生するものではありません。このレスポンスが返される理由として、以下のようなものが考えられます：

- ダッシュボードにアップロードされた認証情報に対して無効なプッシュトークンをアプリが受信した。
- このワークスペースでプッシュが無効になっていた。
- ユーザーがプッシュをオプトアウトした。
- アプリがアンインストールされた。
- Appleがプッシュトークンを更新し、古いトークンが無効になった。
- アプリは本番環境用にビルドされたが、Brazeにアップロードされたプッシュ認証情報は開発環境用に設定されていた（またはその逆）。

## プッシュ登録の問題 {#push-registration-issues}

### プッシュ登録のプロンプトが表示されない {#no-push-registration-prompt}

アプリがプッシュ通知の登録を促すプロンプトを表示しない場合、プッシュ登録の統合に問題がある可能性があります。[ドキュメント]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)に従い、プッシュ登録が正しく統合されていることを確認してください。また、コード内にブレークポイントを設定して、プッシュ登録コードが実行されていることを確認することもできます。

### ダッシュボードに「プッシュ登録済み」のユーザーが表示されない（メッセージ送信前） {#no-push-registered-users-showing-in-the-dashboard-prior-to-sending-messages}

アプリがプッシュ通知を許可するように正しく構成されていることを確認してください。よくある問題点は以下のとおりです。

- アプリがプッシュ通知の許可を求めるプロンプトを表示しているか確認してください。通常、このプロンプトはアプリの初回起動時に表示されますが、別のタイミングで表示されるようプログラムすることもできます。表示されるべき場所で表示されない場合、アプリのプッシュ機能の基本構成に問題がある可能性があります。
  - [プッシュ統合]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)の手順が正常に完了していることを確認してください。
  - アプリのビルドに使用したプロビジョニングプロファイルにプッシュの権限が含まれていることを確認してください。Apple開発者アカウントから利用可能なすべてのプロビジョニングプロファイルを取得していることを確認してください。確認するには、以下の手順を実行してください。
    1. Xcodeで、**Preferences > Accounts**に移動します（またはキーボードショートカット<kbd>Command</kbd>+<kbd>,</kbd>を使用します）。
    2. 開発者アカウントに使用しているApple IDを選択し、**View Details**をクリックします。
    3. 次のページで、**<i class="fas fa-redo-alt"></i> Refresh**をクリックし、利用可能なすべてのプロビジョニングプロファイルを取得していることを確認します。
- アプリで[プッシュ機能が正しく有効化]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-2-enable-push-capabilities)されていることを確認してください。
- プッシュのプロビジョニングプロファイルがテスト中の環境と一致していることを確認してください。ユニバーサル証明書は、Brazeダッシュボードで開発用または本番用のAPNs環境のいずれかに送信するよう構成できます。本番アプリに開発用証明書を使用したり、開発アプリに本番用証明書を使用したりしても機能しません。
- コード内にブレークポイントを設定して、`registerPushToken`メソッドが呼び出されていることを確認してください。
- デバイスを使用してテストしていること（シミュレーターではプッシュは機能しません）、およびネットワーク接続が良好であることを確認してください。

## プッシュ通知が送信されたがユーザーのデバイスに表示されない {#push-notifications-sent-but-not-displayed-on-users-devices}

### メッセージ送信後に「プッシュ登録済み」ユーザーが無効になる {#push-registered-users-no-longer-enabled-after-sending-messages}

これは、ユーザーのプッシュトークンが無効であったことを示している可能性があります。これにはいくつかの原因が考えられます。

#### ダッシュボードとアプリの証明書の不一致 {#dashboard-and-app-certificate-mismatch}

ダッシュボードにアップロードしたプッシュ証明書が、アプリのビルドに使用されたプロビジョニングプロファイル内の証明書と一致しない場合、APNsはトークンを拒否します。正しい証明書をアップロードしたことを確認し、再度テスト通知を送信する前にアプリで別のセッションを完了してください。

#### アプリがアンインストールされた {#application-was-uninstalled}

ユーザーがアプリをアンインストールした場合、そのプッシュトークンは無効となり、次回の送信時に削除されます。

#### プロビジョニングプロファイルの再生成 {#regenerating-your-provisioning-profile}

最後の手段として、最初からやり直して新しいプロビジョニングプロファイルを作成することで、複数の環境、プロファイル、アプリを同時に使用する際に生じる設定エラーを解消できる場合があります。プッシュ通知の設定には多くの「可動部分」があるため、最初からやり直すのが最善である場合があります。これは、引き続きトラブルシューティングが必要な場合に問題を切り分けるのにも役立ちます。

### 「プッシュ登録済み」ユーザーにメッセージが配信されない {#messages-not-delivered-to-push-registered-users}

#### アプリがフォアグラウンドにある {#app-is-foregrounded}

`UserNotifications`フレームワーク経由でプッシュを統合していないiOSバージョンでは、プッシュメッセージの受信時にアプリがフォアグラウンドにある場合、メッセージは表示されません。テストメッセージを送信する前に、テストデバイスでアプリをバックグラウンドに移行してください。

#### テスト通知のスケジュールが正しくない {#test-notification-scheduled-incorrectly}

テストメッセージに設定したスケジュールを確認してください。ローカルタイムゾーン配信または[インテリジェントタイミング]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing)に設定されている場合、まだメッセージを受信していない（または受信時にアプリがフォアグラウンドにあった）可能性があります。

### テスト対象のアプリでユーザーが「プッシュ登録済み」ではない {#user-not-push-registered-for-the-app-being-tested}

テストメッセージを送信しようとしているユーザーのユーザープロファイルを確認してください。**エンゲージメント**タブに「プッシュ可能なアプリ」のリストが表示されるはずです。テストメッセージを送信しようとしているアプリがこのリストに含まれていることを確認してください。ユーザーは、ワークスペース内のいずれかのアプリのプッシュトークンを持っている場合に「プッシュ登録済み」と表示されるため、これは偽陽性である可能性があります。

以下の表示は、プッシュ登録に問題があるか、プッシュ送信後にAPNsによってユーザーのトークンが無効としてBrazeに返されたことを示しています。

![ユーザーの連絡先設定を表示するユーザープロファイル。プッシュの下に「アプリなし」と表示されている。]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## プッシュクリックが記録されない {#push-clicks-not-logged}

- [プッシュ統合のステップ]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-5-enable-push-handling)に従っていることを確認します。
- Brazeでは、フォアグラウンドでサイレント受信したプッシュ通知（`UserNotifications`フレームワーク以前のデフォルトのフォアグラウンドプッシュ動作）は処理されません。つまり、リンクは開かれず、プッシュクリックも記録されません。アプリケーションが`UserNotifications`フレームワークをまだ統合していない場合、アプリケーション状態が`UIApplicationStateActive`のときにBrazeはプッシュ通知を処理しません。アプリで[プッシュ処理メソッド]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-5-enable-push-handling)の呼び出しが遅延しないようにしてください。遅延すると、Swift SDKはプッシュ通知をサイレントフォアグラウンドプッシュイベントとして扱い、処理しない場合があります。

## ディープリンクが機能しない {#deep-links-not-working}

すべてのチャネル（ユニバーサルリンク、カスタムスキーム、メール、Branchなどのサードパーティプロバイダーを含む）にわたる包括的なトラブルシューティングについては、[ディープリンクのトラブルシューティング]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting)を参照してください。

### プッシュクリックからのWebリンクが開かない {#web-links-from-push-clicks-not-opening}

プッシュ通知のリンクをWebビューで開くには、ATSに準拠している必要があります。WebリンクがHTTPSを使用していることを確認してください。詳細については、[ATSコンプライアンス]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking#app-transport-security-ats)を参照してください。

### プッシュクリックからのディープリンクが開かない {#deep-links-from-push-clicks-not-opening}

ディープリンクを処理するコードのほとんどは、プッシュの開封処理も行います。まず、プッシュの開封が記録されていることを確認してください。記録されていない場合は、その問題を修正してください（多くの場合、この修正でリンクの処理も修正されます）。

開封が記録されている場合は、ディープリンク全般の問題なのか、ディープリンクのプッシュクリック処理の問題なのかを確認してください。これを確認するには、アプリ内メッセージのクリックからディープリンクが機能するかテストしてください。