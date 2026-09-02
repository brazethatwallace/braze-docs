---
nav_title: トラブルシューティング
article_title: iOSのプッシュ通知のトラブルシューティング
platform: iOS
page_order: 30
description: "このリファレンス記事では、iOSのプッシュ実装に関する潜在的なトラブルシューティングトピックについて説明します。"
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# トラブルシューティング {#push-troubleshooting}

## Braze/APNsワークフローについて {#understanding-the-brazeapns-workflow}

Apple Push Notification service（APNs）は、iOSおよびOS Xアプリケーションへのプッシュ通知送信を行うAppleのインフラです。ここでは、ユーザーのデバイスでプッシュ通知がどのように有効になり、Brazeがどのようにプッシュ通知を送信できるかについて、簡略化した構造を説明します。

{% multi_lang_include developer_guide/push_notifications/push_registration_flow_steps.md %}

### ステップ1：プッシュ証明書とプロビジョニングプロファイルの設定 {#step-1-configuring-the-push-certificate-and-provisioning-profile}

アプリを開発する際に、プッシュ通知を有効にするためのSSL証明書を作成します。この証明書はアプリのビルドに使用されるプロビジョニングプロファイルに含まれ、Brazeダッシュボードにもアップロードする必要があります。この証明書により、Brazeはお客様に代わってプッシュ通知を送信する権限があることをAPNsに伝えることができます。

[プロビジョニングプロファイル](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html)と証明書には、開発用と配布用の2種類があります。混乱を避けるため、配布用のプロファイルと証明書のみを使用することをお勧めします。開発用と配布用で異なるプロファイルと証明書を使用する場合は、ダッシュボードにアップロードされた証明書が現在使用しているプロビジョニングプロファイルと一致していることを確認してください。

{% alert warning %}
プッシュ証明書の環境（開発用と本番用）を変更しないでください。プッシュ証明書を誤った環境に変更すると、ユーザーのプッシュトークンが誤って削除され、プッシュ通知で連絡できなくなる可能性があります。
{% endalert %}

#### ステップ2：デバイスがAPNsに登録し、Brazeにプッシュトークンを提供する {#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens}

ユーザーがアプリを開くと、プッシュ通知を受け入れるよう求められます。このプロンプトを受け入れると、APNsはその特定のデバイスのプッシュトークンを生成します。iOS SDKは、デフォルトの[自動フラッシュポリシー]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/advanced_use_cases/fine_network_traffic_control#automatic-request-processing)を使用するアプリについて、プッシュトークンを即座に非同期で送信します。ユーザーに関連付けられたプッシュトークンが取得されると、そのユーザーはダッシュボードのユーザープロファイルの**エンゲージメント**タブに「プッシュ登録済み」と表示され、Brazeキャンペーンからプッシュ通知を受信する資格が付与されます。

{% alert note %}
Xcode 14以降では、iOSシミュレーターでリモートプッシュ通知をテストできます。
{% endalert %}

#### ステップ3：Brazeプッシュキャンペーンの開始 {#step-3-launching-a-braze-push-campaign}

プッシュキャンペーンが開始されると、Brazeはメッセージを配信するためにAPNsにリクエストを送信します。Brazeは、ダッシュボードにアップロードされたSSLプッシュ証明書を使用して、提供されたプッシュトークンにプッシュ通知を送信する権限があることを認証および検証します。デバイスがオンラインの場合、キャンペーンが送信された直後に通知を受信するはずです。Brazeは、通知のデフォルトのAPNs[有効期限](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607)を30日に設定していることにご注意ください。

#### ステップ4：無効なトークンの削除 {#step-4-removing-invalid-tokens}

メッセージの送信を試みたプッシュトークンのいずれかが無効であると[APNs](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1)から通知された場合、それらのトークンは関連付けられていたユーザープロファイルから削除されます。

## プッシュエラーログの活用 {#utilizing-the-push-error-logs}

Brazeは、**メッセージアクティビティログ**でプッシュ通知エラーのログを提供しています。このエラーログには、キャンペーンが期待どおりに動作しない原因を特定するのに非常に役立つさまざまな警告が含まれています。エラーメッセージを選択すると、特定のインシデントのトラブルシューティングに役立つ関連ドキュメントにリダイレクトされます。

![エラーが発生した時刻、アプリ名、チャネル、エラータイプ、エラーメッセージを表示するプッシュエラーログ。]({% image_buster /assets/img_archive/message_activity_log.png %})

ここで表示される一般的なエラーには、[「Received Unregistered Sending to Push Token」](#received-unregistered-sending)などのユーザー固有の通知があります。

さらに、Brazeはユーザープロファイルの**エンゲージメント**タブでプッシュの変更ログも提供しています。この変更ログは、トークンの無効化、プッシュ登録エラー、トークンが新しいユーザーに移動された場合など、プッシュ登録の動作に関するインサイトを提供します。

![アニメーション付きContent Cardの例。]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

## プッシュ通知の登録に関する問題 {#push-registration-issues}

アプリケーションのプッシュ通知登録ロジックに検証を追加するには、[プッシュユニットテスト]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests)を実装してください。

### プッシュ通知の登録プロンプトが表示されない {#no-push-registration-prompt}

アプリケーションがプッシュ通知の登録を促すプロンプトを表示しない場合、プッシュ通知の登録統合に問題がある可能性があります。[ドキュメント]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration)に従い、プッシュ通知の登録が正しく統合されていることを確認してください。コード内にブレークポイントを設定して、プッシュ通知の登録コードが実行されていることを確認することもできます。

#### ダッシュボードに「プッシュ通知登録済み」のユーザーが表示されない {#no-push-registered-users-showing-in-the-dashboard}

- アプリがプッシュ通知を許可するよう求めるプロンプトを表示していることを確認してください。通常、このプロンプトはアプリの初回起動時に表示されますが、別の場所で表示されるようにプログラムすることもできます。表示されるべき場所で表示されない場合は、アプリのプッシュ通知機能の基本的な設定に問題がある可能性があります。
  - [プッシュ通知の統合]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration)の手順が正常に完了していることを確認してください。
  - アプリのビルドに使用されたプロビジョニングプロファイルにプッシュ通知の権限が含まれていることを確認してください。Apple開発者アカウントから利用可能なすべてのプロビジョニングプロファイルを取得していることを確認してください。以下の手順で確認できます：
    1. Xcodeで、**Preferences > Accounts** に移動します（またはキーボードショートカット <kbd>Command</kbd>+<kbd>,</kbd> を使用します）。
    2. 開発者アカウントに使用するApple IDを選択し、**View Details** をクリックします。
    3. 次のページで **<i class="fas fa-redo-alt"></i> Refresh** をクリックし、利用可能なすべてのプロビジョニングプロファイルを取得していることを確認します。
- アプリで[プッシュ通知機能が適切に有効化されている]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration#step-2-enable-push-capabilities)ことを確認してください。
- プッシュ通知のプロビジョニングプロファイルが、テスト中の環境と一致していることを確認してください。ユニバーサル証明書はBrazeダッシュボードで開発用またはプロダクション用のAPNs環境のいずれかに送信するよう設定できます。プロダクション用アプリに開発用証明書を使用したり、開発用アプリにプロダクション用証明書を使用したりすると、正しく動作しません。
- コード内にブレークポイントを設定して、`registerPushToken`メソッドが呼び出されていることを確認してください。
- 実機を使用していること（シミュレーターではプッシュ通知は動作しません）、および良好なネットワーク接続があることを確認してください。

## デバイスがプッシュ通知を受信しない {#devices-not-receiving-push-notifications}

### プッシュ通知の送信後にユーザーが「プッシュ登録済み」でなくなる {#users-no-longer-push-registered-after-sending-a-push-notification}

これは、ユーザーのプッシュトークンが無効であることを示している可能性があります。これはいくつかの理由で発生する可能性があります。

#### ダッシュボードとアプリの証明書の不一致 {#dashboard-and-app-certificate-mismatch}

ダッシュボードにアップロードしたプッシュ証明書が、アプリのビルドに使用したプロビジョニングプロファイルのものと異なる場合、APNsはトークンを拒否します。正しい証明書をアップロードしたことを確認し、別のテスト通知を試行する前にアプリで別のセッションを完了してください。

##### アンインストール {#uninstalls}

ユーザーがアプリケーションをアンインストールした場合、プッシュトークンは無効となり、次の送信時に削除されます。

##### プロビジョニングプロファイルの再生成 {#regenerating-your-provisioning-profile}

最後の手段として、最初からやり直して完全に新しいプロビジョニングプロファイルを作成すると、複数の環境、プロファイル、アプリを同時に扱うことで発生する設定エラーを解消できます。iOSアプリのプッシュ通知を設定するには多くの「可動部分」があるため、最初からやり直すのが最善の場合があります。これは、トラブルシューティングを続ける必要がある場合に問題を切り分けるのにも役立ちます。

#### プッシュ通知の送信後もユーザーが「プッシュ登録済み」のままになっている {#users-still-push-registered-after-sending-a-push-notification}

##### アプリがフォアグラウンドにある {#app-is-foregrounded}

`UserNotifications`フレームワーク経由のプッシュを統合していないiOSバージョンでは、プッシュメッセージの受信時にアプリがフォアグラウンドにある場合、通知は表示されません。テストメッセージを送信する前に、テストデバイスでアプリをバックグラウンドにしてください。

##### テスト通知のスケジュールが正しくない {#test-notification-scheduled-incorrectly}

テストメッセージに設定したスケジュールを確認してください。ローカルタイムゾーン配信または[インテリジェントタイミング]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing)に設定されている場合、まだメッセージを受信していないだけかもしれません（または受信時にアプリがフォアグラウンドにあった可能性があります）。

#### テスト対象のアプリにユーザーが「プッシュ登録済み」でない {#user-not-push-registered-for-the-app-being-tested}

テストメッセージの送信先ユーザーのユーザープロファイルを確認してください。**エンゲージメント**タブに「プッシュ可能なアプリ」のリストがあるはずです。テストメッセージを送信しようとしているアプリがこのリストに含まれていることを確認してください。ユーザーはワークスペース内のいずれかのアプリのプッシュトークンを持っていれば「プッシュ登録済み」と表示されるため、偽陽性の可能性があります。

以下は、プッシュ登録に問題がある、またはプッシュ送信後にユーザーのトークンがAPNsによって無効としてBrazeに返されたことを示しています。

![ユーザーの連絡先設定を表示するユーザープロファイル。ここで、プッシュがどのアプリに登録されているかを確認できます。]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## プッシュメッセージが送信されない {#push-messages-not-sending}

送信されないプッシュ通知のトラブルシューティングについては、[プッシュ通知のトラブルシューティング]({{site.baseurl}}/user_guide/channels/push/troubleshooting)を参照してください。

## メッセージアクティビティログのエラー {#message-activity-log-errors}

### プッシュトークンへの未登録送信を受信 {#received-unregistered-sending}

- メソッド`[[Appboy sharedInstance] registerPushToken:]`からBrazeに送信されるプッシュトークンが有効であることを確認してください。**メッセージアクティビティログ**でプッシュトークンを確認できます。`6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`のような、英数字が混在する長い文字列のように表示されるはずです。プッシュトークンの表示が異なる場合は、Brazeにプッシュトークンを送信する[コード]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration#step-4-register-push-tokens-with-braze)を確認してください。
- プッシュプロビジョニングプロファイルがテスト中の環境と一致していることを確認してください。ユニバーサル証明書は、Brazeダッシュボードで開発用または本番用のAPNs環境のいずれかに送信するように設定できます。本番アプリに開発用証明書を使用したり、開発アプリに本番用証明書を使用したりすると動作しません。
 - Brazeにアップロードしたプッシュトークンが、そのプッシュトークンの送信元アプリのビルドに使用したプロビジョニングプロファイルと一致していることを確認してください。

#### トピックに対応しないデバイストークン {#device-token-not-for-topic}

このエラーは、アプリのプッシュ証明書とバンドルIDが一致していないことを示しています。Brazeにアップロードしたプッシュ証明書が、プッシュトークンの送信元アプリのビルドに使用したプロビジョニングプロファイルと一致しているか確認してください。

#### プッシュトークンへの送信でBadDeviceToken {#baddevicetoken-sending-to-push-token}

`BadDeviceToken`はAPNsのエラーコードであり、Brazeから発生したものではありません。このレスポンスが返される理由は複数考えられ、以下が含まれます：

{% multi_lang_include developer_guide/push_notifications/invalid_push_token_reasons.md %}

## プッシュ配信後の問題 {#issues-after-push-delivery}

アプリケーションのプッシュ処理の検証を追加するには、[プッシュユニットテスト]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests)を実装してください。

### プッシュクリックが記録されない {#push-clicks-not-logged}

- iOS 10でのみ発生している場合は、[iOS 10]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration#step-5-enable-push-handling)のプッシュ統合ステップに従っていることを確認してください。
- Brazeは、フォアグラウンドでサイレントに受信されたプッシュ通知を処理しません（例：`UserNotifications`フレームワーク導入前のデフォルトのフォアグラウンドプッシュ動作）。これは、リンクが開かれず、プッシュクリックも記録されないことを意味します。アプリケーションがまだ`UserNotifications`フレームワークを統合していない場合、Brazeはアプリケーションの状態が`UIApplicationStateActive`のときにプッシュ通知を処理しません。アプリが[プッシュ処理メソッド]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration#step-5-enable-push-handling)の呼び出しを遅延させていないことを確認してください。遅延させると、iOS SDKがプッシュ通知をサイレントフォアグラウンドプッシュイベントとして扱い、処理しない場合があります。

#### プッシュクリックからのWebリンクが開かない {#web-links-from-push-clicks-not-opening}

iOS 9以降では、Webビューで開くリンクはATSに準拠している必要があります。WebリンクがHTTPSを使用していることを確認してください。詳しくは、[ATSコンプライアンス]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/advanced_use_cases/linking#app-transport-security-ats)の記事を参照してください。

#### プッシュクリックからのディープリンクが開かない {#deep-links-from-push-clicks-not-opening}

ディープリンクを処理するコードの大部分は、プッシュの開封も処理します。まず、プッシュの開封が記録されていることを確認してください。記録されていない場合は、[その問題を修正](#push-clicks-not-logged)してください（修正によりリンク処理の問題も解決することが多いです）。

開封が記録されている場合は、ディープリンク全般の問題か、ディープリンクのプッシュクリック処理の問題かを確認します。これを確認するには、アプリ内メッセージのクリックからディープリンクが機能するかテストしてください。

#### 直接開封がほとんどまたはまったくない {#few-or-no-direct-opens}

少なくとも1人のユーザーがiOSプッシュ通知を開封しているにもかかわらず、Brazeに*直接開封*がほとんどまたはまったく記録されていない場合、[SDK統合]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview)に問題がある可能性があります。*直接開封*はテスト送信やサイレントプッシュ通知では記録されないことに注意してください。

- メッセージが[サイレントプッシュ通知]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications#sending-silent-push-notifications)として送信されていないことを確認してください。サイレントと見なされないためには、タイトルまたは本文にテキストが必要です。
- [プッシュ統合ガイド]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration)の以下のステップを再確認してください：
   - [プッシュの登録]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration#step-3-register-for-push-notifications)：アプリの起動ごとに（できれば`application:didFinishLaunchingWithOptions:`内で）、ステップ3のコードを実行する必要があります。`UNUserNotificationCenter.current()`のデリゲートプロパティは、`UNUserNotificationCenterDelegate`を実装し、`(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:`メソッドを含むオブジェクトに割り当てる必要があります。
   - [プッシュ処理の有効化]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration#step-5-enable-push-handling)：`(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:`メソッドが実装されていることを確認してください。

### Push Stories の画像クリックが動作しない {#push-story-image-clicks-do-nothing}

このセクションはObjective-C SDKのPush Stories統合に適用されます。SWIFT SDKの`BrazePushStory`モジュールを使用している場合は、`UNNotificationExtensionUserInteractionEnabled`を`YES`に設定してください。[Push Stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories/?sdktab=swift)を参照してください。

Push Storiesの画像をタップしても期待するアクションが開かない場合は、Notification Content Extensionの`Info.plist`を開き、[Push Storiesの設定]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/push_story)のキーと一致しているか確認してください：

- `UNNotificationExtensionCategory` = `ab_cat_push_story_v2`
- `UNNotificationExtensionDefaultContentHidden` = `YES`
- `UNNotificationExtensionInitialContentSizeRatio` = `0.65`

そのplistに`UNNotificationExtensionUserInteractionEnabled`がある場合は、削除してください。Objective-CのPush Stories設定にはそのキーは含まれていません。