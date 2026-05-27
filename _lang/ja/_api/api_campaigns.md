---
nav_title: APIキャンペーン
article_title: API キャンペーン
page_order: 5
description: "このリファレンス記事では、API呼び出しに含めるcampaign_idの生成方法と、そのキャンペーンの設定方法について説明します。"
page_type: reference
tool: Campaigns

---
# APIキャンペーン {#api-campaigns}

> このリファレンス記事では、API呼び出しに含める`campaign_id`の生成方法とそのキャンペーンの設定方法について説明します。

APIキャンペーンは通常、トランザクションメッセージングに使用されます。APIキャンペーン（[APIトリガーキャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery/)ではない）を作成する場合、Brazeダッシュボードは`campaign_id`を生成するためだけに使用され、キャンペーンレポートの分析を追跡できます。また、キャンペーン内の各バリアントごとに異なるメッセージバリエーションIDを生成することもできます。

次に、その情報を以下の内容とともに開発チームに送信し、APIリクエストで使用します。
- キャンペーンコピー
- オーディエンスメンバーシップ
- アセット

キャンペーンが開始された後、結果をダッシュボードで確認できます。APIキャンペーンはBrazeの[メッセージングAPI]({{site.baseurl}}/api/endpoints/messaging/)を使用します。これらのAPIは、ダッシュボードを通じて完全に作成されたキャンペーンと同じ詳細なレポートおよびリターゲティングオプションを備えています。

{% alert warning %}
APIキャンペーンは通常トランザクション型であるため、グローバルコントロールグループに属するユーザーも含め、すべてのユーザーがAPIキャンペーンの対象となります。これらの送信には[ワンクリックリスト配信停止]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#list-unsubscribe)ヘッダーが追加されません。すべてのAPIキャンペーンにワンクリックリスト配信停止ヘッダーを追加する場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

## 新しいキャンペーンを作成する {#create-a-new-campaign}

**メッセージング** > **キャンペーン**に移動して**キャンペーンを作成**を選択し、**API キャンペーン**を選択します。これで、APIキャンペーンの設定に進むことができます。

[APIトリガーキャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery/)は、APIキャンペーンとは異なります。

## キャンペーンを設定する {#configure-your-campaign}

キャンペーンを設定するには、次のステップを実行します。

1. メッセージを送信した後にキャンペーンページで結果を見つけられるように、わかりやすいタイトルを追加します。
2. **Add Message**をクリックして、APIキャンペーンに含めるメッセージタイプを追加します。これにより、`campaign_id`とメッセージバリエーションIDが生成されます。メッセージバリエーションIDは含める各チャネルごとに異なります。
3. オプションとして、特定のアクションやキャンペーン目標に対するユーザーのコンバージョンを追跡するために、コンバージョンイベントを追加できます。
4. **Save キャンペーン**をクリックすると、APIキャンペーンを開始する準備が整います。

## API呼び出し {#api-calls}

APIキャンペーンを保存したら、APIリクエストに次の内容を含めます。
- [メッセージ送信エンドポイント]({{site.baseurl}}/api/endpoints/messaging/#send-endpoints)に記載されている箇所に、生成された`campaign_id`フィールドを含めます。
- キャンペーンに含まれる各プラットフォームの[メッセージオブジェクト]({{site.baseurl}}/api/objects_filters/#messaging-objects)。メッセージオブジェクトにメッセージバリエーションIDを指定します。これにより、統計が収集され、そのバリアントの下に表示されるようになります。次のメッセージオブジェクトがサポートされています：Android、Content Cards、メール、iOS、Kindle、SMS/MMS、Webプッシュ、Webhook。