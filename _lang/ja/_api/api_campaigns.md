---
nav_title: APIキャンペーン
article_title: APIキャンペーン
page_order: 5
description: "このリファレンス記事では、API呼び出しに含めるcampaign_idの生成方法と、そのキャンペーンの設定方法について説明します。"
page_type: reference
tool: Campaigns
---

# APIキャンペーン {#api-campaigns}

> このリファレンス記事では、API呼び出しに含める`campaign_id`の生成方法と、そのキャンペーンの設定方法について説明します。

APIキャンペーンは通常、トランザクションメッセージングに使用されます。APIキャンペーン（[APIトリガーキャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery)ではない）を作成する場合、Brazeダッシュボードは`campaign_id`を生成するためだけに使用され、キャンペーンレポートの分析を追跡できます。また、キャンペーン内の各バリアントごとに異なるメッセージバリエーションIDを生成することもできます。

次に、その情報を以下の内容とともに開発チームに送信し、APIリクエストで使用します。
- キャンペーンコピー
- オーディエンスメンバーシップ
- アセット

キャンペーンが開始された後、結果をダッシュボードで確認できます。APIキャンペーンはBrazeの[メッセージングAPI]({{site.baseurl}}/api/endpoints/messaging)を使用します。これらのAPIは、ダッシュボードを通じて完全に作成されたキャンペーンと同じ詳細なレポートおよびリターゲティングオプションを備えています。

{% alert warning %}
APIキャンペーンは通常トランザクション型であるため、グローバルコントロールグループに属するユーザーも含め、すべてのユーザーがAPIキャンペーンの対象となります。デフォルトでは、これらの送信に[ワンクリックリスト購読解除]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings#list-unsubscribe)ヘッダーは追加されません。APIキャンペーンにワンクリックリスト購読解除ヘッダーを追加するには、[APIキャンペーンにワンクリックリスト購読解除を追加する](#add-one-click-list-unsubscribe-to-api-campaigns)を参照してください。すべてのAPIキャンペーンにワンクリックリスト購読解除ヘッダーを追加する場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

## 新しいキャンペーンを作成する {#create-a-new-campaign}

**メッセージング** > **キャンペーン**に移動し、**キャンペーンを作成**を選択してから、**APIキャンペーン**を選択します。これで、APIキャンペーンの設定に進むことができます。

[APIトリガーキャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery)はAPIキャンペーンとは異なります。

## キャンペーンを設定する {#configure-your-campaign}

キャンペーンを設定するには、以下のステップを実行します。

1. メッセージ送信後にキャンペーンページで結果を見つけられるよう、わかりやすいタイトルを追加します。
2. **メッセージを追加**を選択し、APIキャンペーンに含めるメッセージタイプを追加します。これにより、`campaign_id` と、含めるチャネルごとに異なるメッセージバリアントIDが生成されます。
3. 必要に応じて、特定のアクションやキャンペーン目標に対するユーザーのコンバージョンを追跡するためのコンバージョンイベントを追加できます。
4. **キャンペーンを保存**を選択して、APIキャンペーンを開始します。

## API呼び出し {#api-calls}

APIキャンペーンを保存した後、APIリクエストに以下を含めてください。

- 生成された`campaign_id`フィールドを、[メッセージ送信エンドポイント]({{site.baseurl}}/api/endpoints/messaging)に記載されている箇所でAPIリクエストに含めます。
- キャンペーンに含まれる各プラットフォームの[メッセージオブジェクト]({{site.baseurl}}/api/objects_filters#messaging-objects)。メッセージオブジェクトには、メッセージバリアントIDを指定します。これにより、統計がそのバリアントの下で収集・表示されるようになります。サポートされているメッセージオブジェクトは、Android、Content Cards、メール、iOS、Kindle、SMS/MMS、Webプッシュ、Webhookです。

## APIキャンペーンにワンクリックリスト配信停止を追加する {#add-one-click-list-unsubscribe-to-api-campaigns}

{% raw %}
デフォルトでは、BrazeはAPIキャンペーンにワンクリックリスト配信停止ヘッダーを追加しません。APIリクエストのメールヘッダーフィールドに`{{${set_user_to_one_click_list_unsubscribe}}}`Liquidタグを含めることで、個々のAPIキャンペーン送信にこのヘッダーを追加できます。
{% endraw %}

ワンクリックリスト配信停止の[RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)に準拠するには、APIリクエストに`List-Unsubscribe`ヘッダーと`List-Unsubscribe-Post`ヘッダーの両方を含めてください。

{% raw %}
```json
{
  "external_user_ids": ["user_id"],
  "messages": {
    "email": {
      "app_id": "your_app_id",
      "subject": "Your Subject",
      "from": "Sender Name <sender@example.com>",
      "body": "<p>Email body content</p>",
      "headers": {
        "List-Unsubscribe": "<{{${set_user_to_one_click_list_unsubscribe}}}>",
        "List-Unsubscribe-Post": "List-Unsubscribe=One-Click"
      }
    }
  }
}
```
{% endraw %}

{% alert note %}
これらのヘッダーを含めても、メールクライアントが購読解除ボタンを表示することが保証されるわけではありません。メールクライアントは、送信者のレピュテーションやメッセージの内容などの要素に基づいて、購読解除オプションを表示するかどうかを判断します。
{% endalert %}

### メール添付ファイルを追加する {#add-email-attachments}

APIキャンペーンのメールに添付ファイルを追加するには、[メールオブジェクト]({{site.baseurl}}/api/objects_filters/messaging/email_object)に`attachments`配列を含めます。メールオブジェクトに`email_template_id`を指定することで、ドラッグ＆ドロップエディターまたはHTMLエディターで作成したメールテンプレートを参照し、API呼び出しを通じて添付ファイルを追加できます。

添付ファイルの詳細、サイズ制限、およびベストプラクティスについては、[添付ファイル付きメールオブジェクトの例]({{site.baseurl}}/api/objects_filters/messaging/email_object#example-email-object-with-attachment)を参照してください。