---
nav_title: Multiplied Media
article_title: Multiplied Media
description: "Multiplied MediaをBrazeと連携して、メール、プッシュ通知、アプリ内メッセージ、Content Cards、WhatsAppを通じてパーソナライズされた画像、GIF、動画を送信する方法を説明します。"
alias: /partners/multiplied_media/
page_type: partner
search_tag: Partner
---

# Multiplied Media

> [Multiplied Media](https://multiplied.media)は、CRMデータを活用して、パーソナライズされた画像、GIF、動画（顧客ごとにユニークなアセット）を作成するクリエイティブ＆オートメーションスタジオです。Multiplied MediaとBrazeの連携により、メール、プッシュ通知、アプリ内メッセージ、Content Cards、WhatsAppを通じてこれらのメディアを送信できます。
>
> Multiplied Mediaはソフトウェアツールではなく、マネージドサービスです。Multiplied Mediaチームがコンセプト、デザイン、アニメーション、データ接続、レンダリングを担当します。この連携を使用するには、[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid)マージタグを含むメディアURLをキャンペーンまたはキャンバスに挿入します。

_この連携はMultiplied Mediaによって管理されています。_

## この連携について {#about-this-integration}

Multiplied Mediaチームは、最初のコンセプトからローンチまで一緒に取り組みます。ブランド向けのメディアをデザイン・アニメーション化し、データを接続し、レンダリングを自動化します。新しいソフトウェアを学ぶ必要はありません。

この連携は、Brazeのデータ（顧客属性やセグメント）をMultiplied Mediaに接続します。Multiplied Mediaは顧客ごとにユニークなメディアアセットをレンダリングし、その顧客の識別子を含むURLでホストします。Brazeメッセージ内でLiquidマージタグを使用してそのURLを参照します。これにより、各顧客が自分専用の画像、GIF、または動画を見ることができます。

この連携は2つのフローをサポートしています：

- **バッチキャンペーン：** CSV、S3、またはAPIでデータを送信します。Multiplied Mediaが送信前にすべてのメディアをレンダリングしてホストします。
- **リアルタイムキャンバスオートメーション：** キャンバス内の[Webhook]({{site.baseurl}}/user_guide/channels/webhooks)ステップが、顧客がそのステップに到達した時点でレンダリングをトリガーします。

## ユースケース {#use-cases}

- **パーソナライズされたキャンペーン：** 製品ローンチ、「まとめ」や年間レビューキャンペーン、季節のプロモーション、個人データのビジュアライゼーション。
- **常時稼働オートメーション：** ウェルカムフロー、オンボーディング、マイルストーンのお祝い、奪還メール、カート放棄、配送通知、再入荷アラート、ロイヤルティの更新。
- **オムニチャネルジャーニー：** 1つのコンセプトをすべてのチャネル向けにレンダリング。同じ顧客データから、メールのヒーロー画像、プッシュ画像、アプリ内ビジュアル、WhatsApp動画を作成できるため、ジャーニー全体で一貫したビジュアルアイデンティティを維持できます。

## 前提条件 {#prerequisites}

Multiplied Mediaのアーキテクチャは、S3またはAPIによるバッチベースのキャンペーンと、webhookによるリアルタイムキャンバスオートメーションをサポートしています。配信前にユニークなメディアアセットを事前生成してホストすることで、Multiplied Mediaはメッセージがトリガーされた瞬間にLiquidタグやカスタム属性でテンプレートにマージできる、シームレスな1対1のビジュアル体験を保証します。

開始する前に、以下の要件を確認してください：

| 要件 | 説明 |
| --- | --- |
| アクティブなMultiplied Mediaの契約 | Multiplied Mediaはマネージドサービスです。Brazeでの作業を開始する前に、Multiplied Mediaチームがキャンペーンのスコープを定め、メディアテンプレートをデザイン・構築し、レンダリングを設定します。開始するには、[multiplied.media](https://multiplied.media)にアクセスするか、[hello@multiplied.media](mailto:hello@multiplied.media)にメールしてください。 |
| データソース | CSV、S3、API、またはBraze webhookで顧客データをMultiplied Mediaに接続します。Multiplied Mediaチームがオンボーディング中にこの設定を行います。 |
| 統一識別子 | データには、BrazeとMultiplied Media間で共有される識別子（`external_id`など）が含まれている必要があります。この識別子は各顧客のメディアURLの一部を構成し、BrazeメッセージではLiquidで参照します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## BrazeでMultiplied Mediaを使用する {#use-multiplied-media-with-braze}

Multiplied Mediaがパーソナライズされたメディアのデザイン、構築、レンダリングを行い、データ接続をサポートします。以下のステップは、Brazeで行う残りの作業です。

### ステップ1：メディアの準備完了を確認する {#step-1-confirm-your-media-is-ready}

ローンチ前に、Multiplied Mediaチームがメディアのレンダリング完了（バッチキャンペーンの場合）またはレンダリングエンドポイントの稼働（リアルタイムキャンバスフローの場合）を確認します。その後、キャンペーンのメディアURLが提供されます。例：

{% raw %}
```
https://cdn.multiplied.media/yourbrand/campaign-name/{{${user_id}}}.gif
```
{% endraw %}

URLパス内の識別子は、設定時に合意した統一識別子です。

### ステップ2：キャンペーンまたはキャンバスにURLを挿入する {#step-2-insert-the-url-into-your-campaign-or-canvas}

Liquidマージタグを含むMultiplied MediaのURLを、チャネルに応じたフィールドに貼り付けます：

- **メール：** メールテンプレートの画像ソース。
- **プッシュ通知：** プッシュメッセージの画像フィールド。
- **アプリ内メッセージとContent Cards：** メディアフィールド。
- **WhatsApp：** メディアヘッダーフィールド。

リアルタイムキャンバスオートメーションの場合は、メッセージステップの前にMultiplied MediaのWebhookステップ（オンボーディング中に設定）と遅延ノードを追加します。これにより、配信前に各顧客のメディアがレンダリングされます。

### ステップ3：プレビュー、テスト、ローンチ {#step-3-preview-test-and-launch}

Brazeのプレビューとテスト送信を使用して、Liquidタグが正しく解決され、各テストユーザーが自分専用のメディアを表示できることを確認します。Multiplied Mediaチームがローンチ前にテスト送信を一緒にレビューします。

## 考慮事項 {#considerations}

- 各顧客のメディアアセットはユニークです。顧客が接続されたデータソースに存在しない場合、URLはメディアのデフォルト（フォールバック）バージョンを配信します。Multiplied Mediaはすべての契約の一環としてフォールバックをデザインします。
- Multiplied Mediaは配信前にアセットをレンダリングしてホストします。開封時にレンダリングするわけではありません。メディアは開封時に即座に読み込まれ、レンダリング時点の顧客データを表示します。送信時点でデータが最新である必要がある場合（例：トリガーされたキャンバスフロー）は、リアルタイムWebhookステップを使用してください。
- スケジュールされたバッチキャンペーンの場合、すべてのアセットをレンダリングできるよう、送信時刻前にデータがMultiplied Mediaに届いている必要があります。Multiplied Mediaチームが設定時に締め切り時刻を合意します。

## トラブルシューティング {#troubleshooting}

Multiplied Mediaはマネージドサービスのため、Multiplied Mediaチームが最初のサポート窓口となります。[hello@multiplied.media](mailto:hello@multiplied.media)までお問い合わせください。

ダイナミック画像が表示されない場合は、以下の表を参照してください。

| 問題 | 解決方法 |
| --- | --- |
| ダイナミック画像が表示されない | URL内のLiquidタグが、設定時に合意した統一識別子と一致していることを確認してください（例：`user_id`とカスタム属性の違い）。顧客が接続されたデータソースに存在することを確認してください。識別子が解決されてもパーソナライズされたアセットが存在しない場合は、フォールバックメディアが表示されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="トラブルシューティング" }