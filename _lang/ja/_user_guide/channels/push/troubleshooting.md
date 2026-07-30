---
nav_title: トラブルシューティング
article_title: プッシュ通知のトラブルシューティング
page_order: 5
page_type: reference
description: "症状インデックスと標準的な調査パスを使用して、プッシュ通知の配信、クリック動作、認証情報の問題を診断します。"
channel: push
---

# プッシュ通知のトラブルシューティング {#troubleshoot-push}

> このページでは、プッシュ通知の配信、クリック動作、認証情報の問題をトラブルシューティングします。SDKに固有の設定については、[Braze SDKのプッシュ通知のトラブルシューティング]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting)を参照してください。エラーコードについては、[一般的なプッシュエラーメッセージ]({{site.baseurl}}/user_guide/channels/push/push_error_codes)を参照してください。

## まずはここから：症状を確認する {#start-here-match-your-symptom}

| 症状 | 参照先 |
| --- | --- |
| ユーザーがプッシュ通知を受信しなかった | [プッシュ通知が届かない](#missing-push-notifications) |
| プッシュ通知が遅れて届く | [プッシュ通知の遅延](#delayed-push-notifications) |
| プッシュ送信が予想より遅い | [プッシュ通知の送信が予想より遅い](#push-notifications-are-sending-slower-than-expected) |
| `MismatchSenderID` エラー（Android） | [エラー：MismatchSenderID](#error-mismatch-sender-id) |
| プッシュをタップしてもアプリが開かない | [プッシュ通知をクリックしてもアプリが開かない](#clicking-a-push-notification-does-not-open-the-app) |
| プッシュリンクがブラウザーではなくアプリで開く | [プッシュクリックが予期せずアプリ内で開く](#push-clicks-unexpectedly-open-in-app) |
| Webプッシュの権限または配信の問題 | [Webプッシュ通知が期待どおりに動作しない](#web-push-notifications-are-not-behaving-as-expected) |
| `.p12` から `.p8` への移行が必要（iOS） | [.p8認証キーへの移行](#migrate-to-a-p8-authentication-key) |
| ログに特定のプッシュエラーコードがある | [プッシュエラーメッセージ](#push-error-messages) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="プッシュの症状" }

## 標準的な調査パス {#standard-investigation-path}

ユーザーまたはテストデバイスがプッシュを受信しなかった場合は、このワークフローを使用してください。ステップ1から始めてください。

1. ユーザーがプッシュ購読済みまたはオプトイン済みであり、プロファイルの**エンゲージメント**タブに有効なプッシュトークンがあることを確認します。
2. 送信時にユーザーがキャンペーンまたはキャンバスのターゲットオーディエンスに含まれていることを確認します（セグメントはリアルタイムで更新されます）。
3. キャンペーンまたはキャンバスのグローバルフリークエンシーキャップ、レート制限、コントロールグループの割り当てを確認します。
4. デバイスに対して正しいプッシュタイプを使用していることを確認します（例：Android、iOS、またはKindle）。
5. 内部テストの場合、テスターがデバイス上の正しいアプリにログインしていることを確認します。
6. それでも配信に失敗する場合は、[よくあるプッシュエラーメッセージ]({{site.baseurl}}/user_guide/channels/push/push_error_codes)を確認するか、キャンペーンまたはキャンバスのID、ユーザーID、タイムゾーン付きのタイムスタンプを添えて[Brazeサポート]({{site.baseurl}}/braze_support)にお問い合わせください。

## プッシュ通知が届かない {#missing-push-notifications}

**症状：** ユーザーが期待されるプッシュ通知を受信しなかった。

プッシュ通知が期待どおりに届かない場合は、以下の項目を順に確認してください。

- [プッシュサブスクリプションステータス](#push-subscription-status)
- [セグメント](#segment)
- [プッシュ通知キャップ](#push-notification-caps)
- [レート制限](#rate-limits)
- [コントロールグループのステータス](#control-group-status)
- [有効なプッシュトークン](#valid-push-token)
- [プッシュ通知の種類](#push-notification-type)
- [現在のアプリ](#current-app)

### プッシュサブスクリプションステータス {#push-subscription-status}

プッシュ通知は、購読中またはオプトインしたユーザーにのみ送信できます。**ユーザープロファイル**で[エンゲージメント]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#engagement-tab)タブを開き、テスト対象のワークスペースでプッシュ通知に登録されていることを確認してください。複数のアプリに登録している場合は、**Push Registered For**に一覧表示されます。

![プッシュ登録済みアプリの一覧]({% image_buster /assets/img_archive/trouble1.png %})

Brazeのエクスポートエンドポイントを使用してユーザープロファイルをエクスポートすることもできます。

- [識別子によるユーザー]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [セグメントによるユーザー]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

いずれのエンドポイントも、デバイスごとのプッシュ有効化情報を含むプッシュトークンオブジェクトを返します。

### セグメント {#segment}

ターゲットにしているセグメントに自分が含まれていることを確認してください（ライブキャンペーンの場合、テストではない場合）。**ユーザープロファイル**には、ユーザーが現在含まれているセグメントの一覧が表示されます。セグメントメンバーシップはリアルタイムで更新されます。

![セグメントの一覧]({% image_buster /assets/img_archive/trouble2.png %})

セグメントを作成する際に**ユーザー検索**を使用して、ユーザーがそのセグメントに含まれていることを確認することもできます。**ユーザー検索**は`external_id`または`braze_id`のみを受け付けます。メールアドレスや電話番号は使用できません。メール、電話番号、プッシュトークン、またはユーザーエイリアスで検索するには、[**ユーザーを検索**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles)を参照してください。

![検索フィールドを含むユーザー検索セクション]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

### プッシュ通知キャップ {#push-notification-caps}

グローバルフリークエンシーキャップを確認してください。ワークスペースにグローバルフリークエンシーキャップが設定されており、指定された期間のプッシュ通知キャップにすでに達しているため、プッシュ通知を受信できなかった可能性があります。

キャンペーンの**分析**ページで、フリークエンシーキャップのバナーを確認し、過去30日間にキャンペーンを受信しなかったユーザーのおおよその数を確認してください。個別の送信を調査するには、[メッセージング診断ダッシュボード]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard)を使用し、**フリークエンシーキャップ**でフィルタリングしてください。ルールの確認や変更については、[グローバルフリークエンシーキャップ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#freq-cap-feat-over)を参照してください。

![キャンペーンの詳細]({% image_buster /assets/img_archive/trouble3.png %})

### レート制限 {#rate-limits}

キャンペーンまたはキャンバスにレート制限が設定されている場合、その制限を超えたためにメッセージを受信できなくなっている可能性があります。詳細については、[レート制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-rate-limiting)を参照してください。

### コントロールグループのステータス {#control-group-status}

単一チャネルのキャンペーンまたはコントロールグループを含むキャンバスの場合、コントロールグループに入っている可能性があります。

  1. [バリアント配分]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#step-4-choose-a-segment-and-distribute-your-users-across-variants)を確認して、コントロールグループがあるかどうかを確認します。
  2. コントロールグループがある場合は、[キャンペーンコントロールグループ内]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns#in-campaign-control-group)でフィルタリングするセグメントを作成し、[セグメントをエクスポート]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv#segment-csv-export-details)して、自分のユーザーIDがリストに含まれているかどうかを確認します。

### 有効なプッシュトークン {#valid-push-token}

プッシュトークンは、送信者が特定のデバイスにプッシュ通知を送信するために使用する識別子です。有効なプッシュトークンがなければ、Brazeはそのデバイスにプッシュ通知を送信できません。

Brazeはユーザープロファイルごとに最大20台のデバイスを保存します。21台目のデバイスが登録されると、最も古いデバイスが削除されます（先入れ先出し、FIFO）。SDKで[`changeUser()`]({{site.baseurl}}/developer_guide/analytics/setting_user_ids)を呼び出すと、現在のデバイスがプロファイルに再登録されます。

### プッシュ通知の種類 {#push-notification-type}

ターゲットにしているデバイスまたはプラットフォームに合ったプッシュの種類を使用してください。たとえば、Fire TVをターゲットにする場合は、Androidプッシュキャンペーンではなく、Kindleプッシュ通知を使用します。Androidデバイスの場合は、iOSプッシュキャンペーンではなく、Androidプッシュ通知を使用します。

プラットフォーム固有のトラブルシューティングワークフローについては、以下を参照してください。

- [Appleプッシュ通知のトラブルシューティング]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)
- [Firebase Cloud Messagingのトラブルシューティング]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)

### 現在のアプリ {#current-app}

内部ユーザーでプッシュをテストする場合、プッシュ通知を受信させたいユーザーが正しいアプリにサインインしていることを確認してください。そうでない場合、プッシュ通知を受信しなかったり、セグメンテーションに基づいて予期しないプッシュ通知を受信したりする可能性があります。

{% alert note %}
Androidで画像付きのプッシュメッセージを送信する場合、FCMが画像を破棄し、プッシュメッセージにテキストのみを表示することがあります。この問題は通常、サーバー接続の問題が原因です。
{% endalert %}

## エラー：MismatchSenderID {#error-mismatch-sender-id}

**症状：** Androidプッシュが`MismatchSenderID`エラーで失敗します。

MismatchSenderIDは、Firebase Cloud Messaging（FCM）での認証失敗を示します。FirebaseのSender IDとFCM APIキーが正しいことを確認してください。

正しいFirebaseサーバーキーを見つけて置き換えるには：

1. アプリのFirebaseコンソールに移動します。
2. **Project Overview**で、**Project Settings**を選択します。
3. **Cloud Messaging**タブで、APIキーとともに表示されているSender IDがBrazeのもの（**設定** > **アプリ設定** > **Cloud Messaging API Key**）と一致していることを確認します。

{% alert warning %}
Brazeダッシュボードでは、Sender IDを変更しないでください。変更すると、既存のプッシュ登録が無効になります。Sender IDが一致しない場合は、一致するSender IDを持つFirebaseプロジェクトを見つける必要があります。
{% endalert %}

4. **Project credentials**の下にある**Server Key**をコピーします。
5. Brazeで、**設定** > **アプリ設定**に移動し、アプリを選択して、サーバーキーを**Cloud Messaging API Key**フィールドに貼り付けます（古いキーを置き換えます）。
6. **Save**を選択します。
7. 確認するには、APIキーを変更する前と後に、アプリを開かずにデバイスにテストプッシュを送信します。これにより、新しいプッシュ登録ID（プッシュトークン）を生成しなくても、ユーザーが引き続きプッシュ通知を受信できることを確認できます。

## トラブルシューティングシナリオ {#troubleshooting-scenarios}

### プッシュ通知の遅延 {#delayed-push-notifications}

**症状:** プッシュ通知が予想より遅れて届きます。

プッシュ通知が遅延する原因として、以下が考えられます。

- デバイスのデータ接続が弱い
- アプリ内のカスタムコードがBrazeのプッシュ通知を抑制している
- デバイスの設定でのプッシュ通知に関するユーザーの設定
- キャンペーンまたはキャンバスで作成されたプッシュのメッセージ優先度
- プッシュサービスプロバイダー（FCMおよびAPNs）のトラフィック遅延や問題

### プッシュ通知の送信が予想より遅い {#push-notifications-are-sending-slower-than-expected}

**症状:** キャンペーンまたはキャンバスのプッシュ送信が、完了するまでに予想以上の時間がかかります。

プッシュ通知の設定が以下のベストプラクティスに従っていることを確認してください。

- プッシュ有効ステータスを考慮せずに大規模なオーディエンスに送信している場合、送信速度が遅くなる可能性があります。代わりに、プッシュ有効なユーザーのみに送信してオーディエンスのサイズを縮小することを検討してください。
- 可能であれば、即時送信ではなく、事前にキャンペーンをスケジュールするようにしてください。
- キャンバスで多数のユーザーにプッシュ通知をターゲティングしている場合、キャンバス内の後続のメッセージステップは、ユーザーに即時送信するキャンペーンとは異なる処理時間を要することが予想されます。この場合、キャンバスの最初の「ステップ」はユーザーが特定のユーザージャーニーに適格かどうかを確認することであるため、通常キャンペーンの方がキャンバスよりも先に送信を完了します。

## プッシュ通知をタップしてもアプリが開かない {#clicking-a-push-notification-does-not-open-the-app}

**症状：** プッシュ通知をタップしても、アプリが開かない、または設定どおりに遷移しない。

プッシュ通知をタップしてもアプリが開かない場合は、プラットフォームに応じて以下を確認してください。

### Android

1. **クリック時の動作を確認する：** キャンペーンがクリック時にアプリを開くように設定されていることを確認します。
2. **ディープリンクの処理を確認する：** `braze.xml` ファイルで、`com_braze_handle_push_deep_links_automatically` が `true` に設定されているか `false` に設定されているかを確認します。
   - `true` に設定されている場合、Braze SDKがディープリンクを直接処理し、アプリは期待どおりに開きます。
   - `false` に設定されている場合、アプリにはプッシュの受信および開封インテントをリッスンして処理するブロードキャストレシーバーが必要です。このレシーバーが正しく実装されていることを確認してください。
3. **詳細ログを収集する：** [詳細ログを有効にし]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)、問題を再現して、ログと `braze.xml` および `AndroidManifest.xml` をBrazeサポートに提供してください。

### iOS

1. **クリック時の動作を確認する：** キャンペーンがクリック時にアプリを開くように設定されていることを確認します。
2. **プッシュの統合を確認する：** プッシュからアプリへのディープリンクは、Brazeの[標準プッシュ統合]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift)によって自動的に処理されます。カスタムデリゲートの処理を含め、統合が正しく実装されていることを確認してください。
3. **詳細ログを収集する：** [詳細ログを有効にし]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)、問題を再現して、ログをBrazeサポートに提供してください。

## プッシュのクリックが予期せずアプリ内で開く {#push-clicks-unexpectedly-open-in-app}

**症状:** プッシュ通知内のリンクが、デバイスのWebブラウザではなくアプリ内で開きます。

プッシュ通知内のリンクがWebブラウザではなく予期せずアプリ内で開く問題が発生している場合、キャンペーンの設定またはSDKの実装に問題がある可能性があります。以下の手順を参照してください。

### クリック時の動作を確認する {#verify-on-click-behavior}

キャンペーンまたはキャンバスステップで、**モバイルアプリ内でWeb URLを開く**が選択されていないことを再確認してください。選択されている場合は、選択を解除して再起動してください。

クリック時の動作「Web URLを開く」のデフォルトの動作はSDKバージョンによって異なります。SDKバージョンiOS 2.29.0およびAndroid 2.0.0以降では、このオプションはデフォルトで選択されており、Web URLはアプリ内のWebビューで開きます。これらのバージョンより前では、このオプションはデフォルトで選択解除されており、Web URLはデバイスのデフォルトWebブラウザで開きます。

これが問題でない場合は、プッシュの実装に問題がある可能性があります。

### プッシュ統合を再確認する {#double-check-push-integration}

プッシュ通知内のリンクが予期せずアプリ内で開く場合、プッシュ通知の統合またはカスタマイズ設定に問題がある可能性があります。以下の手順でトラブルシューティングを行ってください。

1. **プッシュデリゲートの実装を確認する:** Brazeプッシュデリゲートが正しく実装されていることを確認します。詳細な手順については、お使いの[プラットフォーム]({{site.baseurl}}/developer_guide/home)のプッシュ通知統合ガイドを参照してください。
2. **カスタムリンク処理を確認する:** アプリにすべての`https://`リンクに対するカスタム処理が含まれていないか確認します。カスタム設定がデフォルトの動作を上書きしている可能性があります。開発チームと協力して、必要に応じてこれらの設定を確認・調整してください。
3. **iOSプッシュ登録を確認する:** iOSの場合、[APNsへのプッシュ通知の登録]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-1-register-for-push-notifications-with-apns)に関するプッシュ統合ガイドのステップ1を再確認してください。デリゲートオブジェクトがアプリの起動完了前に同期的に割り当てられていることを確認します。このステップは`application:didFinishLaunchingWithOptions:`メソッドで完了する必要があります。
4. **統合をテストする:** 調整を行った後、iOSとAndroidの両方のデバイスでプッシュ通知の動作をテストし、問題が解決されたことを確認してください。

### アプリがバックグラウンドで実行中のディープリンク（iOS） {#deep-links-with-app-still-running-in-the-background-ios}

アプリが実行されていないとき、またはリンクを直接使用したときにはディープリンクが機能するが、アプリがすでにバックグラウンドで実行されているときには機能しない場合、アプリがリンクを処理する方法に問題がある可能性があります。メソッドスウィズリングを使用するサードパーティライブラリを使用していないか確認してください。スウィズリングはディープリンクの実装に問題を引き起こす可能性があるため、オフにすることをお勧めします。

## .p8認証キーへの移行 {#migrate-to-a-p8-authentication-key}

**症状：** iOSプッシュ認証情報をレガシー証明書から`.p8`キーに移行する必要がある、または認証情報の変更後にプッシュ配信が失敗した。

Appleの`.p8`認証キーは、BrazeでのAPNsプッシュに必要なアプローチです。レガシーの証明書ファイルタイプとは異なり、`.p8`キーは有効期限がなく、単一のキーですべてのアプリをサポートするため、年次の証明書更新が不要になり、プッシュ配信の失敗リスクが軽減されます。

現在`.p12`または`.pem`証明書を使用している場合は、できるだけ早く`.p8`キーに移行してください。`.p8`キーの作成とアップロードの手順については、[APNsプッシュ証明書のアップロード]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift)を参照してください。Appleの開発者アカウントから`.p8`キーを生成する方法については、[認証トークンを使用したAPNsとの通信](https://developer.apple.com/help/account/capabilities/communicate-with-apns-using-authentication-tokens/)を参照してください。

### .p8キーと.p12証明書の比較 {#p8-keys-versus-p12-certificates}

以下の表で、認証情報の種類、有効期限、およびダッシュボードでの表示を比較できます。

| 認証情報 | 有効期限 | ダッシュボードのステータスインジケーター |
| --- | --- | --- |
| `.p8`認証キー | 有効期限なし | 緑色のステータスインジケーターなし（これは想定どおりです） |
| `.p12`プッシュ証明書 | 毎年有効期限切れ | 証明書が有効な場合は緑色のインジケーター |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label=".p8キーと.p12証明書の比較" }

`.p12`証明書を`.p8`キーに置き換える（または新しい認証情報をアップロードする）と、Brazeが変更を処理する間、プッシュ配信が一時的に停止する場合があります。可能であれば、メンテナンスウィンドウ中に更新を計画してください。

**設定** > **アプリ設定** > **プッシュ通知の設定**で、**App Bundle ID**、**Team ID**、および**Key ID**（`.p8`キーの場合）がApple Developerアカウントの値と一致していることを確認してください。複数のBrazeワークスペースで、iOSアプリの**バンドルID**が同一であれば、同じAppleプッシュ認証情報を使用できます。認証情報の環境（開発と本番）は、アプリのビルド方法と一致する必要があります。

[Braze Swift SDK 10.0.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/10.0.0)以降のアプリでは、[動的APNsゲートウェイ管理]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift#dynamic-apns-gateway-management)を使用して、トークンを正しいAPNs環境に自動的にルーティングできます。

## Webプッシュ通知が期待どおりに動作しない {#web-push-notifications-are-not-behaving-as-expected}

**症状：** ブラウザーのプッシュ通知が表示されない、またはサイトの権限が固まっているように見えます。

ブラウザーでプッシュ通知に問題が発生している場合は、サイトの通知権限をリセットし、サイトのストレージをクリアする必要がある場合があります。以下の手順を参考にしてください。

{% tabs %}
{% tab Chrome %}

### デスクトップでChromeをリセットする {#reset-chrome-on-desktop}

1. Chromeブラウザーで URL の横にある **View Site Information** スライダーアイコンを選択します。
2. **Notifications** の下で、**Reset permission** を選択します。
3. Chrome DevToolsを開きます。オペレーティングシステムごとの関連するショートカットは以下のとおりです。

<style>
table {
    max-width: 50%;
}
</style>

| OS      | キーボードショートカット                                                  |
| ------- | ------------------------------------------------------------------- |
| Mac      | `Fn` + `F12`<br>`Ctrl` + `Shift` + `I` |
| Windows | `F12`<br>`Ctrl` + `Shift` + `I` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="デスクトップでChromeをリセットする" }

{:start="4"}
4. DevToolsで、**Application** タブに移動します。
5. サイドバーで **Storage** を選択します。
6. **Clear site data** を選択します。
7. Chromeが更新された設定を適用するためにページの再読み込みを求めます。**Reload** を選択します。

プッシュ権限がリセットされました。サイトの新しいタブを開いて試してみてください。

### AndroidでChromeをリセットする {#reset-chrome-on-android}

サイトからの通知がAndroidの通知ドロワーに表示されている場合：

1. プッシュ通知から <i class="fas fa-cog" title="設定"></i> **Settings** を選択し、**Site settings** を選択します。
2. **Site settings** から、**Clear & Reset** をタップします。

サイトからの通知が開いていない場合：

1. AndroidでChromeを開きます。
2. <i class="fas fa-ellipsis-vertical"></i> メニューをタップします。
3. **Settings** > **Site Settings** > **Notifications** に移動します。
4. 通知が **Ask before sending (recommended)** に設定されていることを確認します。
5. リストからサイトを見つけます。
6. エントリを選択し、**Clear and Reset** をタップします。

プッシュ権限がリセットされました。サイトの新しいタブを開いて試してみてください。

{% endtab %}
{% tab Firefox %}

### デスクトップでFirefoxをリセットする {#reset-firefox-on-desktop}

1. サイトのURLの横にある <i class="fa-solid fa-circle-info" alt="情報アイコン"></i> または <i class="fas fa-lock" alt="ロックアイコン"></i> を選択します。
2. **Permissions** の下で、**Receive Notifications** の横にある <i class="fa-solid fa-circle-xmark" title="この権限をクリアして再度確認する"></i> **Clear permission** を選択して通知権限をクリアします。
3. 同じメニューで、**Clear Cookies and Site Data** を選択します。
4. 選択を確認するダイアログで、**OK** を選択します。

プッシュ権限がリセットされました。サイトの新しいタブを開いて試してみてください。

### AndroidでFirefoxをリセットする {#reset-firefox-on-android}

Androidでプッシュ権限をリセットするには、Mozilla Supportの[Clear your browsing history and other personal data](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser)を参照してください。

{% endtab %}
{% tab Safari %}

### macOSでSafariをリセットする {#reset-safari-on-macos}

{% alert note %}
これらの手順はmacOS専用です。AppleはWindows上のSafariではWebプッシュをサポートしていません。
{% endalert %}

1. Safariを開きます。
2. [Macのメニューバー](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac)から、**Safari** > **Settings** > **Websites** > **Notifications** に移動します。
3. リストからサイトを選択します。
4. **Remove** を選択して、サイトの通知権限を削除します。
5. 次に、**Privacy** > **Manage Website Data** に移動します。
6. リストからサイトを選択します。
7. **Remove** を選択するか、すべてのサイトデータを削除するには **Remove All** を選択します。
8. **Done** を選択します。

プッシュ権限がリセットされました。サイトの新しいタブを開いて試してみてください。

{% endtab %}
{% endtabs %}

## プッシュ開封指標 {#push-open-metrics}

Brazeは、ユーザーが通知をタップしてアプリがセッションを開始したときに直接開封を記録します。アプリを開かずにリッチプッシュ通知を展開しても、直接開封は記録されません。

ユーザーがプッシュ通知を受信した後、通知をタップせずにアプリを開いた場合、Brazeは代わりに影響を受けた開封を記録することがあります。定義とレポートについては、[影響を受けた開封]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens)を参照してください。

## プッシュエラーメッセージ {#push-error-messages}

**症状：** 特定のプッシュエラーコード（例：`DEVICE_UNREGISTERED`、`Unregistered`、`NotRegistered`）が表示されます。

一般的なプッシュエラーコード（`DEVICE_UNREGISTERED`、`NotRegistered`、`Unregistered`など）の定義については、[一般的なプッシュエラーメッセージ]({{site.baseurl}}/user_guide/channels/push/push_error_codes)を参照してください。

FCMが`DEVICE_UNREGISTERED`や`NotRegistered`などのエラーを返した場合、Brazeは通常、影響を受けたプッシュトークンをユーザープロファイルから削除します。この削除は、アプリがアンインストールされたか、トークンが無効になったことを示す場合が多いです。アンインストール追跡キャンペーンは、同じトークン削除ロジックを大規模に使用します。