---
nav_title: APIトリガーおよびアクションベースのキャンペーン
article_title: APIトリガーおよびアクションベースのキャンペーンのテスト
page_order: 2
page_type: reference
description: "このリファレンス記事では、APIトリガーおよびアクションベースのキャンペーンのテスト方法について説明します。"

---

# APIトリガーおよびアクションベースのキャンペーン {#api-triggered-and-action-based-campaigns}

> キャンペーンを設定する際は、起動前にメッセージをテストすることが常にベストプラクティスです。このリファレンス記事では、APIリクエストやペイロードの検査、配信ログの確認を可能にするテストユーザーSegmentの作成方法について説明します。

## ステップ 1: テストユーザーSegmentを作成する {#step-1-create-a-test-user-segment}

APIまたはカスタムイベントによるキャンペーンのトリガーをテストする唯一の方法は、キャンペーンを本番環境にプッシュすることです。新しいキャンペーンを展開する際は、配信のトリガーをテストするときにキャンペーンにテストユーザーSegmentを追加することを強くお勧めします。これにより安全策が確保され、キャンペーンが誤って送信された場合でも、内部ユーザーにのみ送信されます。

1. **テストユーザーをインポートする**<br>テストユーザーは、CSVまたは[Postman]({{site.baseurl}}/api/postman_collection)を使用した単発のバッチリクエストでBrazeにインポートできます。これらのユーザーをインポートする際は、テストグループSegmentの構築に使用できるカスタム属性（`internal_test_user: true` など）をプロファイルに設定することをお勧めします。<br><br>
2. **テストユーザーをBraze認定テストユーザーとして追加する**<br>ダッシュボードで[テストユーザーをBraze認定テストユーザーとしてマークする]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups)と、各ユーザーの詳細なログにアクセスでき、APIリクエストやそのペイロードの検査、および配信ログの確認が可能になります。これらのログは、エンドユーザーへのキャンペーン配信に問題がなかったかどうかを判断するのに役立ちます。<br><br>
3. **Segmentを作成する**<br>テストユーザーSegmentを作成するには、`internal_test_user` カスタム属性が `true` に設定されたユーザーのSegmentを作成します。このSegmentは、キャンペーンが本番環境に移行した際に削除できます。

## ステップ 2: テスト送信を行う {#step-2-testing-sends}

次に、Brazeダッシュボードからテスト送信を行うか、Inbox Vision（メールのみ）を使用して、キャンペーンがまだ下書きモードの間にレイアウトがどのように表示されるかを確認できます。その後、キャンペーンをテストユーザーSegmentに送信して、期待どおりに動作しているかを確認します。キャンペーンがAPIトリガーであるかアクションベースであるかに関わらず、Postmanを使用してBraze APIに単発のリクエストを送信し、キャンペーンをトリガーしてください。

## ステップ 3: Brazeのログを使用して受信結果を検査する {#step-3-use-braze-logging-to-inspect-inbound-results}

Brazeのログを使用して、トリガー、送信、およびイベントの問題をトラブルシューティングします。
- [イベントユーザーログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log)では、APIトリガーリクエストの生のペイロード、キャンペーンをトリガーするカスタムイベント、および関連するトリガーやイベントプロパティを確認できます。
- [メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)では、エラーが記録され、特定のメッセージが配信されなかった理由を把握するのに役立ちます。

## ステップ 4: テストSegmentを削除してキャンペーンを展開する {#step-4-remove-the-test-segment-and-roll-out-the-campaign}

メッセージが正しくトリガーおよびレンダリングされ、クリックされたすべてのリンクが登録されたことを確認したら、Segmentを削除してキャンペーンを更新できます。テストユーザーの少数のインプレッションが含まれないようにキャンペーンを最初からやり直したい場合は、キャンペーンを複製し、テストユーザーSegmentなしで再開できます。