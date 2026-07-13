## Braze/APNsのワークフローについて {#understanding-the-brazeapns-workflow}

Appleプッシュ通知サービス（APNs）は、Appleのプラットフォームで実行されているアプリケーションにプッシュ通知を送信するためのインフラです。ユーザーのデバイスに対してプッシュ通知を有効にする方法と、Brazeがユーザーにプッシュ通知を送信する方法の簡略化された構造を以下に示します。

1. プッシュ証明書とプロビジョニングプロファイルを構成します
2. デバイスがAPNsに登録し、Brazeにプッシュトークンを提供します
3. Brazeプッシュキャンペーンを開始します
4. Brazeが無効なトークンを削除します

### ステップ1:プッシュ証明書とプロビジョニングプロファイルの構成 {#step-1-configuring-the-push-certificate-and-provisioning-profile}

アプリの開発では、プッシュ通知を有効にするためにSSL証明書を作成する必要があります。この証明書はアプリのビルドに使用されるプロビジョニングプロファイルに含まれ、Brazeダッシュボードにもアップロードする必要があります。この証明書により、Brazeはあなたに代わってプッシュ通知を送信することが許可されていることをAPNsに伝えることができます。

[プロビジョニングプロファイル](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html)と証明書には、開発と配布の2つのタイプがあります。混乱を避けるために、配布プロファイルと証明書のみを使用することをお勧めします。開発と配布で異なるプロファイルと証明書を使用する場合は、ダッシュボードにアップロードした証明書が現在使用しているプロビジョニングプロファイルと一致していることを確認してください。

{% alert warning %}
プッシュ証明書の環境（開発環境と本番環境）を変更しないでください。プッシュ証明書を間違った環境に変更すると、ユーザーのプッシュトークンが誤って削除され、プッシュで到達できなくなる可能性があります。
{% endalert %}

### ステップ2:デバイスがAPNsに登録し、Brazeにプッシュトークンを提供します {#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens}

ユーザーがアプリを開くと、プッシュ通知を受け入れるように求められます。このプロンプトを受け入れると、APNsはその特定のデバイスのプッシュトークンを生成します。Swift SDKは、デフォルトの[自動フラッシュポリシー]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/fine_network_traffic_control#automatic-request-processing)を使用して、アプリのプッシュトークンを即時かつ非同期に送信します。ユーザーにプッシュトークンが関連付けられると、ダッシュボードの**エンゲージメント**タブのユーザープロファイルに「プッシュ登録済み」と表示され、Brazeキャンペーンからプッシュ通知を受け取る資格が得られます。

{% alert note %}
macOS 13以降、一部のデバイスでは、Xcode 14上で動作するiOS 16シミュレーターでプッシュ通知をテストできます。詳細については、[Xcode 14リリースノート](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes)を参照してください。
{% endalert %}

#### プッシュトークン生成に関する考慮事項 {#considerations-for-push-token-generation}

- ユーザーが別のデバイスにアプリをインストールした場合、別のトークンが作成され、同じ方法で取得されます。
- ユーザーがアプリを再インストールすると、新しいトークンが生成され、Brazeに渡されます。ただし、元のトークンはAPNsとBrazeによって有効なものとして記録される可能性があります。
- ユーザーがアプリをアンインストールしても、Brazeは即座に通知を受け取らず、トークンはAPNsによって無効化されるまで有効なまま表示されます。
- いずれAPNsは古いトークンを廃止します。Brazeはこれについてコントロールも可視性も持っていません。

### ステップ3:Brazeプッシュキャンペーンの開始 {#step-3-launching-a-braze-push-campaign}

プッシュキャンペーンが開始されると、Brazeはメッセージの配信リクエストをAPNsに行います。具体的には、**ユーザーの最新のデバイスに送信**が選択されている場合を除き、現在の有効なプッシュトークンごとにリクエストがAPNsに渡されます。BrazeがAPNsから成功応答を受信した後、ユーザープロファイルに配信成功を記録します。ただし、以下の理由により、ユーザーが実際のメッセージを受信していない可能性があります。
- デバイスの電源が切れている。
- デバイスがインターネット（Wi-Fiまたはモバイルデータ通信）に接続されていない。
- ユーザーが最近アプリをアンインストールした。

Brazeは、ダッシュボードにアップロードされたSSLプッシュ証明書を使用して認証を行い、提供されたプッシュトークンへのプッシュ通知の送信が許可されていることを確認します。デバイスがオンラインの場合、キャンペーンが送信された後すぐに通知が受信されます。なお、Brazeは通知のデフォルトのAPNs[有効期限](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607)を30日に設定しています。

### ステップ4:無効なトークンの削除 {#step-4-removing-invalid-tokens}

[APNs](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1)が、メッセージを送信しようとしたプッシュトークンのいずれかが無効であることを通知した場合、それらのトークンは関連付けられたユーザープロファイルから削除されます。

{% alert note %}
APNsでは、トークンが登録解除されても、最初は成功ステータスを返すのが通常です。APNsはトークンの無効化イベントを即座にレポートしないためです。APNsは、無効なトークンに対する`410`ステータスの返却を意図的に遅延させます。この遅延はランダムなスケジュールで実行され、ユーザーのプライバシー保護とアプリのアンインストール追跡防止を目的としています。APNsが`410`ステータスを返すまで、未登録のトークンへの通知送信を安全に継続できます。
{% endalert %}

## プッシュのエラーログの使用 {#using-the-push-error-logs}

[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab)を使用すると、キャンペーンや送信に関連するメッセージ（特にエラーメッセージ）を確認できます。これにはプッシュ通知エラーも含まれます。このエラーログは、キャンペーンが期待どおりに機能していない理由を特定するのに非常に役立つさまざまな警告を提供します。エラーメッセージをクリックすると、特定のインシデントのトラブルシューティングに役立つ関連ドキュメントにリダイレクトされます。

![エラーが発生した時間、アプリ名、チャネル、エラータイプ、およびエラーメッセージを表示するプッシュエラーログ。]({% image_buster /assets/img_archive/message_activity_log.png %})

ここでよく見かけるエラーとしては、[「プッシュトークンへの未登録送信を受信」](#swift_received-unregistered-sending)など、ユーザー固有の通知があります。

さらに、Brazeは**エンゲージメント**タブのユーザープロファイルにプッシュ通知の変更ログも提供します。この変更ログは、トークンの無効化、プッシュ登録エラー、トークンの新規ユーザーへの移動などのプッシュ登録動作に関するインサイトを提供します。

![Brazeユーザープロファイルのエンゲージメントタブに表示されるプッシュ登録変更ログ。]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

### メッセージアクティビティログのエラー {#message-activity-log-errors}

#### プッシュトークンへの未登録送信を受信 {#received-unregistered-sending}

- メソッド`AppDelegate.braze?.notifications.register(deviceToken:)`からBrazeに送信されているプッシュトークンが有効であることを確認してください。**メッセージアクティビティログ**でプッシュトークンを確認できます。`6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`のような、文字と数字が混在する長い文字列になります。プッシュトークンが異なるように見える場合は、Brazeにプッシュトークンを送信するための[コード]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-4-register-push-tokens-with-braze)を確認してください。
- プッシュプロビジョニングプロファイルがテスト対象の環境と一致することを確認します。ユニバーサル証明書は、開発または本番のAPNs環境のいずれかに送信するようにBrazeダッシュボードで構成できます。本番アプリ用の開発証明書または開発アプリ用の本番証明書は動作しません。
 - Brazeにアップロードしたプッシュトークンが、プッシュトークンの送信元のアプリのビルドに使用したプロビジョニングプロファイルと一致することを確認します。

#### デバイストークンがトピック用ではない {#device-token-not-for-topic}

APNsは、プッシュトークンが認証情報に構成されたトピック（バンドルID）と一致しない場合に`DeviceTokenNotForTopic`（HTTPステータス400）を返します。Brazeは**メッセージアクティビティログ**またはプッシュ配信ログにこれを`DeviceTokenNotForTopic`として表示する場合があります。

不一致を解決するには：

1. アプリの**バンドルID**がBrazeの**アプリバンドルID**（**設定** > **アプリ設定** > **プッシュ通知の設定**）と一致することを確認します。
2. アプリのビルドに使用したプロビジョニングプロファイルに、そのバンドルIDのプッシュ機能が含まれていることを確認します。
3. Brazeにアップロードしたプッシュ認証情報がアプリの環境（開発環境と本番環境）と一致することを確認します。
4. `.p8`キーの場合、Brazeの**チームID**と**キーID**がApple Developerアカウントと一致することを確認します。
5. 認証情報がローテーションまたは失効された場合は、有効な`.p8`キーまたは`.p12`証明書を再アップロードします。

可能な場合は`.p8`認証キーを使用することをお勧めします。認証情報のタイプとダッシュボードのステータスインジケーターについては、[.p8認証キーへの移行]({{site.baseurl}}/user_guide/channels/push/troubleshooting#migrate-to-a-p8-authentication-key)を参照してください。

#### プッシュトークンへのBadDeviceToken送信 {#baddevicetoken-sending-to-push-token}

`BadDeviceToken`はAPNsのエラーコードであり、Brazeから発信されたものではありません。この応答が返される理由としては、以下のようなさまざまなものが考えられます。

- アプリが、ダッシュボードにアップロードされた認証情報に対して無効なプッシュトークンを受け取った。
- このワークスペースではプッシュが無効になっていた。
- ユーザーがプッシュをオプトアウトした。
- アプリがアンインストールされた。
- Appleがプッシュトークンを更新したため、古いトークンが無効になった。
- アプリは本番環境用にビルドされているが、Brazeにアップロードされたプッシュ認証情報は開発環境用に設定されている（またはその逆）。

## プッシュ登録に関する問題 {#push-registration-issues}

### プッシュ登録プロンプトが表示されない {#no-push-registration-prompt}

アプリケーションでプッシュ通知の登録を求めるプロンプトが表示されない場合は、プッシュ登録の統合に問題がある可能性があります。[ドキュメント]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)に従い、プッシュ登録が正しく統合されていることを確認してください。コードにブレークポイントを設定して、プッシュ登録コードが実行されていることを確認することもできます。

### ダッシュボードに「プッシュ登録済み」ユーザーが表示されない（メッセージ送信前） {#no-push-registered-users-showing-in-the-dashboard-prior-to-sending-messages}

アプリがプッシュ通知を許可するように正しく構成されていることを確認してください。チェックすべき一般的な障害点は以下のとおりです。

- アプリがプッシュ通知を許可するように求めるプロンプトを表示していることを確認します。通常、このプロンプトはアプリを初めて起動したときに表示されますが、他の場所に表示されるようにプログラムすることもできます。表示されるべき場所に表示されない場合は、アプリのプッシュ機能の基本構成に問題がある可能性があります。
  - [プッシュ統合]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)の手順が正常に完了したことを確認します。
  - アプリのビルドに使用されたプロビジョニングプロファイルにプッシュの権限が含まれていることを確認します。Apple Developerアカウントから利用可能なプロビジョニングプロファイルをすべてプルダウンしていることを確認してください。これを確認するには、以下の手順を実行します。
    1. Xcodeで、**Preferences** > **Accounts**に移動します（またはキーボードショートカット<kbd>Command</kbd>+<kbd>,</kbd>を使用します）。
    2. 開発者アカウントに使用するApple IDを選択し、**View Details**をクリックします。
    3. 次のページで、**<i class="fas fa-redo-alt"></i> Refresh**をクリックし、使用可能なすべてのプロビジョニングプロファイルをプルしていることを確認します。
- アプリで[プッシュ機能が適切に有効化]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-2-enable-push-capabilities)されていることを確認します。
- プッシュプロビジョニングプロファイルがテスト環境と一致することを確認します。ユニバーサル証明書は、開発または本番のAPNs環境のいずれかに送信するようにBrazeダッシュボードで構成できます。本番アプリ用の開発証明書または開発アプリ用の本番証明書は動作しません。
- コードにブレークポイントを設定して、`registerPushToken`メソッドを呼び出していることを確認します。
- デバイスを使ってテストし（プッシュはシミュレーターでは機能しません）、ネットワーク接続が良好であることを確認します。

## プッシュ通知は送信されたがユーザーのデバイスに表示されない {#push-notifications-sent-but-not-displayed-on-users-devices}

### 「プッシュ登録済み」ユーザーがメッセージ送信後に有効でなくなる {#push-registered-users-no-longer-enabled-after-sending-messages}

これは、ユーザーが無効なプッシュトークンを持っていたことを示している可能性があります。これにはいくつかの理由が考えられます。

#### ダッシュボードとアプリ証明書の不一致 {#dashboard-and-app-certificate-mismatch}

ダッシュボードでアップロードしたプッシュ証明書が、アプリのビルドに使用したプロビジョニングプロファイルのものと異なる場合、APNsはトークンを拒否します。別のテスト通知を試みる前に、正しい証明書をアップロードし、アプリで別のセッションを完了していることを確認してください。

#### アプリケーションがアンインストールされた {#application-was-uninstalled}

ユーザーがアプリケーションをアンインストールした場合、プッシュトークンは無効となり、次回の送信時に削除されます。

#### プロビジョニングプロファイルの再生成 {#regenerating-your-provisioning-profile}

最後の手段として、最初からやり直してまったく新しいプロビジョニングプロファイルを作成すると、複数の環境、プロファイル、およびアプリを同時に操作することによって発生する構成エラーを解消できます。プッシュ通知の設定には多くの「動く部分」があるため、最初からやり直した方がよい場合もあります。また、トラブルシューティングを続ける必要がある場合は、問題を切り分けるのにも役立ちます。

### 「プッシュ登録済み」ユーザーにメッセージが配信されない {#messages-not-delivered-to-push-registered-users}

#### アプリがフォアグラウンドにある {#app-is-foregrounded}

`UserNotifications`フレームワークを介してプッシュを統合していないiOSバージョンでは、プッシュメッセージの受信時にアプリがフォアグラウンドにある場合、そのメッセージは表示されません。テストメッセージを送信する前に、テストデバイスでアプリをバックグラウンドにする必要があります。

#### テスト通知のスケジュールが正しくない {#test-notification-scheduled-incorrectly}

テストメッセージに設定したスケジュールを確認します。ローカルタイムゾーン配信または[インテリジェントタイミング]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing)に設定されている場合、メッセージがまだ受信されていない（または受信時にアプリがフォアグラウンドにあった）だけかもしれません。

### テスト対象のアプリに対してユーザーが「プッシュ登録」されていない {#user-not-push-registered-for-the-app-being-tested}

テストメッセージを送信しようとしている相手のユーザープロファイルを確認します。**エンゲージメント**タブの下に「プッシュ可能なアプリ」のリストがあるはずです。テストメッセージを送信しようとしているアプリがこのリストにあることを確認します。ユーザーがワークスペース内の任意のアプリのプッシュトークンを持っている場合は「プッシュ登録済み」と表示されるため、誤検知の可能性があります。

以下は、プッシュ登録に問題があるか、プッシュ後にユーザーのトークンがAPNsによって無効としてBrazeに返されたことを示しています。

![ユーザーの連絡先設定を表示するユーザープロファイル。プッシュの下に「アプリなし」が表示されています。]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## プッシュクリックが記録されない {#push-clicks-not-logged}

- [プッシュ統合のステップ]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-5-enable-push-handling)に従っていることを確認します。
- Brazeでは、フォアグラウンドでサイレント受信したプッシュ通知（`UserNotifications`フレームワーク以前のデフォルトのフォアグラウンドプッシュ動作）は処理されません。つまり、リンクは開かれず、プッシュクリックも記録されません。アプリケーションが`UserNotifications`フレームワークをまだ統合していない場合、アプリケーション状態が`UIApplicationStateActive`のときにBrazeはプッシュ通知を処理しません。アプリで[プッシュ処理メソッド]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-5-enable-push-handling)の呼び出しが遅延しないようにしてください。遅延すると、Swift SDKはプッシュ通知をサイレントフォアグラウンドプッシュイベントとして扱い、処理しない場合があります。

## ディープリンクが機能しない {#deep-links-not-working}

ユニバーサルリンク、カスタムスキーム、メール、Branchのようなサードパーティプロバイダーを含む、全チャネルにわたる包括的なトラブルシューティングについては、[ディープリンクのトラブルシューティング]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting)を参照してください。

### プッシュクリックからのWebリンクが開かない {#web-links-from-push-clicks-not-opening}

プッシュ通知のリンクは、Webビューで開くにはATS準拠である必要があります。WebリンクがHTTPSを使用していることを確認してください。詳細については、[ATSコンプライアンス]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking#app-transport-security-ats)を参照してください。

### プッシュクリックからのディープリンクが開かない {#deep-links-from-push-clicks-not-opening}

ディープリンクを扱うコードのほとんどはプッシュ通知の開封も扱います。まず、プッシュ通知の開封がログに記録されていることを確認します。記録されていない場合は、その問題を修正してください（修正するとリンク処理も直ることが多いです）。

開封が記録されている場合は、ディープリンク全般の問題なのか、ディープリンクのプッシュクリック処理の問題なのかを確認してください。そのためには、アプリ内メッセージクリックからのディープリンクが機能するかテストします。