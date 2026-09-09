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
> Multiplied Mediaはソフトウェアツールではなく、マネージドサービスです。Multiplied Mediaチームがコンセプト、デザイン、アニメーション、データ接続、レンダリングを担当します。この連携を使用するには、[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)マージタグを含むメディアURLをキャンペーンまたはキャンバスに挿入します。

_この連携はMultiplied Mediaによって管理されています。_

## この連携について {#about-this-integration}

Multiplied Mediaチームは、最初のコンセプトからローンチまで一貫してサポートします。ブランドに合わせたメディアのデザインとアニメーション制作、データ接続、レンダリングの自動化を行います。新しいソフトウェアを学ぶ必要はありません。

この連携により、Brazeのデータ（顧客属性やセグメント）がMultiplied Mediaに接続されます。Multiplied Mediaは顧客ごとにユニークなメディアアセットをレンダリングし、その顧客の識別子を含むURLでホストします。Brazeメッセージ内でLiquidマージタグを使用してそのURLを参照します。これにより、各顧客が自分専用の画像、GIF、または動画を受け取ります。

この連携は2つのフローをサポートしています：

- **バッチキャンペーン：** CSV、S3、またはAPIでデータを送信します。Multiplied Mediaは送信前にすべてのメディアをレンダリングしてホストします。
- **リアルタイムキャンバスオートメーション：** キャンバス内の[Webhook]({{site.baseurl}}/user_guide/channels/webhooks)ステップが、顧客がそのステップに到達した時点でレンダリングをトリガーします。

## ユースケース {#use-cases}

- **パーソナライズされたキャンペーン:** 新商品の発売、「まとめ」や年間振り返りキャンペーン、季節限定プロモーション、パーソナルデータビジュアライゼーション。
- **常時稼働のオートメーション:** ウェルカムフロー、オンボーディング、マイルストーンのお祝い、奪還メール、カート放棄、配送通知、再入荷アラート、ロイヤルティの更新。
- **オムニチャネルジャーニー:** 1つのコンセプトをあらゆるチャネル向けにレンダリングします。同じ顧客データを、メールのヒーロー画像、プッシュ画像、アプリ内ビジュアル、WhatsApp動画に展開できるため、ジャーニー全体を通じてすべてのタッチポイントで統一されたビジュアルアイデンティティを維持できます。

## 前提条件 {#prerequisites}

Multiplied Mediaのアーキテクチャは、S3またはAPIを介したバッチベースのキャンペーンと、webhookを介したリアルタイムのキャンバスオートメーションをサポートしています。配信前にユニークなメディアアセットを事前生成してホスティングすることで、Multiplied Mediaはメッセージがトリガーされた瞬間に、Liquidタグやカスタム属性を使用してテンプレートにマージできる、シームレスな1対1のビジュアル体験を確実に準備します。

開始する前に、以下の要件を確認してください。

| 要件 | 説明 |
| --- | --- |
| アクティブなMultiplied Mediaエンゲージメント | Multiplied Mediaはマネージドサービスです。Brazeで作業を開始する前に、Multiplied Mediaチームがキャンペーンのスコープを定め、メディアテンプレートをデザイン・構築し、レンダリングを設定します。開始するには、[multiplied.media](https://multiplied.media)にアクセスするか、[hello@multiplied.media](mailto:hello@multiplied.media)にメールしてください。 |
| データソース | CSV、S3、API、またはBraze webhookを使用して顧客データをMultiplied Mediaに接続します。Multiplied Mediaチームがオンボーディング時にこの設定を行います。 |
| 統一識別子 | データには、BrazeとMultiplied Media間で共有される識別子（`external_id`など）が含まれている必要があります。この識別子は各顧客のメディアURLの一部を構成し、BrazeメッセージではLiquidを使用してこれを参照します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## Braze での Multiplied Media の使用 {#use-multiplied-media-with-braze}

Multiplied Media は、パーソナライズされたメディアの設計、構築、レンダリングを行い、データの接続をサポートします。以下のステップは、Braze で行う残りの作業です。

### ステップ1:メディアの準備が完了していることを確認する {#step-1-confirm-your-media-is-ready}

ローンチの前に、Multiplied Media チームがメディアのレンダリング完了（バッチキャンペーン）またはレンダリングエンドポイントの稼働（リアルタイムキャンバスフロー）を確認します。その後、キャンペーンのメディア URL が提供されます。例:

{% raw %}
```
https://cdn.multiplied.media/yourbrand/campaign-name/{{${user_id}}}.gif
```
{% endraw %}

URL パスの識別子は、設定時に合意した統一識別子です。

### ステップ2:キャンペーンまたはキャンバスに URL を挿入する {#step-2-insert-the-url-into-your-campaign-or-canvas}

Multiplied Media の URL（Liquid マージタグを含む）を、チャネルの該当フィールドに貼り付けます。

- **メール:** メールテンプレートの画像ソース。
- **プッシュ通知:** プッシュメッセージの画像フィールド。
- **アプリ内メッセージおよびContent Cards:** メディアフィールド。
- **WhatsApp:** メディアヘッダーフィールド。

リアルタイムキャンバスオートメーションの場合は、メッセージステップの前に Multiplied Media の Webhook ステップ（オンボーディング時に設定）と遅延ノードを追加します。これにより、配信前に各顧客のメディアがレンダリングされます。

### ステップ3:プレビュー、テスト、ローンチ {#step-3-preview-test-and-launch}

Braze のプレビューとテスト送信を使用して、Liquidタグが正しく解決されること、および各テストユーザーに固有のメディアが表示されることを確認します。Multiplied Media チームがローンチ前にテスト送信を一緒にレビューします。

## 考慮事項 {#considerations}

- 各顧客のメディアアセットはユニークです。顧客が接続されたデータソースに存在しない場合、URLはデフォルト（フォールバック）バージョンのメディアを配信します。Multiplied Mediaは、すべてのエンゲージメントの一部としてフォールバックをデザインします。
- Multiplied Mediaは配信前にアセットをレンダリングしてホストします。開封時にレンダリングするわけではありません。メディアは開封時にすぐに読み込まれ、レンダリング時点の顧客データを表示します。送信時点でデータが最新である必要がある場合（たとえば、トリガーされたキャンバスフローなど）は、リアルタイムWebhookステップを使用してください。
- スケジュールされたバッチキャンペーンの場合、すべてのアセットをレンダリングできるよう、送信時刻までにデータがMultiplied Mediaに届いている必要があります。Multiplied Mediaチームが設定時に締め切り時刻について合意します。

## トラブルシューティング {#troubleshooting}

Multiplied Mediaはマネージドサービスであるため、Multiplied Mediaチームが最初のサポート窓口となります。[hello@multiplied.media](mailto:hello@multiplied.media) までお問い合わせください。

ダイナミック画像が表示されない場合は、以下の表を参照してください。

| 問題 | 解決策 |
| --- | --- |
| ダイナミック画像が表示されない | URL内のLiquidタグが、設定時に合意した統一識別子（例：`user_id`とカスタム属性の違い）と一致していることを確認してください。接続されたデータソースに顧客が存在することを確認してください。識別子が解決されてもパーソナライズされたアセットが存在しない場合は、フォールバックメディアが表示されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="トラブルシューティング" }