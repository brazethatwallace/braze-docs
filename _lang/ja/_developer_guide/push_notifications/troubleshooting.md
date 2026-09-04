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

以下の表から発生している動作を見つけて、該当セクションのステップに従ってください。どのセクションが該当するかわからない場合は、[標準的な調査パス](#standard-investigation-path)を使用してください。

| 症状 | 参照先 |
| --- | --- |
| 特定のプラットフォームでプッシュ通知を受信しない | [プラットフォーム固有のトラブルシューティング](#platform-specific-troubleshooting)でSDKタブを選択してください |
| 保存時にLiquidタグ周辺の改行がおかしくなる | [プッシュ通知の改行](#push-linebreaks) |
| ダッシュボードの配信チェック（購読、セグメント、上限） | [プッシュ通知のトラブルシューティング]({{site.baseurl}}/user_guide/channels/push/troubleshooting) |
| プッシュ通知からのディープリンクが正しく開かない | [ディープリンクのトラブルシューティング]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting) |
| 一般的なプッシュエラーコード | [一般的なプッシュエラーメッセージ]({{site.baseurl}}/user_guide/channels/push/push_error_codes) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="プッシュSDKの症状" }

## 標準的な調査パス {#standard-investigation-path}

すべてのプッシュ通知インシデントに対して、このワークフローを使用してください。ステップ1から始めてください。

1. デバイスに有効なプッシュトークンがあり、デバイス設定でプッシュ権限が付与されていることを確認します。
2. ダッシュボードで、テストユーザーがキャンペーンまたはキャンバスの[セグメント]({{site.baseurl}}/user_guide/channels/push/troubleshooting#segment)に一致しており、[コントロールグループ]({{site.baseurl}}/user_guide/channels/push/troubleshooting#control-group-status)に含まれていないことを確認します。
3. テストデバイスに[テストプッシュ]({{site.baseurl}}/developer_guide/push_notifications/sending_test_messages)を送信します。
4. [詳細ログを有効にし]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)、問題を再現して、[SDKタブ](#platform-specific-troubleshooting)のプラットフォーム固有のガイダンスを確認します。
5. 問題が解決しない場合は、詳細ログ、プラットフォーム、SDKバージョン、キャンペーンまたはキャンバスIDを添えて[Brazeサポート]({{site.baseurl}}/user_guide/administer/personal/braze_support)にお問い合わせください。

## プッシュクリックが記録されない {#push-clicks-not-logged}

- [プッシュ通知の統合ステップ]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling)に従っていることを確認してください。
- Brazeは、フォアグラウンドでサイレントに受信されたプッシュ通知を処理しません（`UserNotifications`フレームワーク導入前のデフォルトのフォアグラウンドプッシュ動作）。つまり、リンクは開かれず、プッシュクリックも記録されません。アプリがまだ`UserNotifications`フレームワークを統合していない場合、アプリの状態が`UIApplicationStateActive`のときにBrazeはプッシュ通知を処理しません。アプリが[プッシュ処理メソッド]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling)の呼び出しを遅延させないようにしてください。遅延させると、Swift SDKがプッシュ通知をサイレントフォアグラウンドプッシュイベントとして扱い、処理しない場合があります。

## プッシュ通知の改行 {#push-linebreaks}

Liquidタグを使用してプッシュ通知を作成する場合、Liquidタグに隣接する改行はメッセージ送信前に自動的に削除されます。[プッシュ通知コンポーザー]({{site.baseurl}}/user_guide/channels/push/create_a_push_message)では、編集中にメッセージが読みやすいようにこれらの改行が再追加されます。メッセージを保存する際にLiquidタグの前後に改行が表示される場合、これは想定どおりの動作です。