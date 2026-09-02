---
nav_title: DailyPlay
article_title: DailyPlay
description: "DailyPlayのブランドゲームと報酬をBrazeに接続し、ゲームプレイデータの同期、オーディエンスのセグメンテーション、パーソナライズされたキャンペーンのトリガーを行う方法を説明します。"
alias: /partners/dailyplay/
page_type: partner
search_tag: Partner
---

# DailyPlay

> [DailyPlay](https://dailyplay.ai/)はゲーミフィケーションプラットフォームです。パーソナライズされたブランドゲームや組み込みの報酬システムを立ち上げ、エンゲージメントを深め、リテンションを向上させることができます。

*このインテグレーションはDailyPlayによって管理されています。*

## この連携について {#about-this-integration}

BrazeとDailyPlayの連携により、オーディエンスセグメント全体でゲームや報酬パフォーマンスのデプロイとトラッキングが可能になります。DailyPlayのゲームと報酬システムは、Brazeのオーケストレーションエンジンと連携することで、受動的なオーディエンスを能動的な参加者に変えることができます。

ゲームプレイのマイルストーン、報酬の引き換え、エンゲージメント指標をBrazeに送信し、オーディエンスセグメントを構築したり、ゲーム内の行動に基づいて自動化されたクロスチャネルメッセージングをトリガーしたりできます。この連携により、以下のことが可能になります。

- **ユーザープロファイルの充実化：** ゲームプレイの指標、スコア、報酬ステータスをBrazeのユーザープロファイルに渡します。
- **高度なセグメンテーションの実現：** トップスコアラー、最近の勝者、報酬のアンロックに近いユーザーなど、ゲーム内の行動に基づいてオーディエンスセグメントを作成します。
- **リアルタイムキャンペーンの自動化：** ゲームのインタラクションに基づいてパーソナライズされたクロスチャネルメッセージ（プッシュ、メール、アプリ内）をトリガーし、リピートプレイ、ブランドロイヤルティ、および生涯価値の向上を促進します。

## ユースケース {#use-cases}

- **離脱した顧客の再エンゲージメント：** 非アクティブな顧客に、割引報酬が当たるチャンスのあるゲームへのリンクを送信します。
- **商品やトレンドに関連するアクティビティ：** 新商品や季節のイベント、トレンド、キャンペーンイベントを紹介するパーソナライズされたゲームを作成します。
- **ターゲットを絞ったゲームの展開：** Brazeのセグメンテーションとターゲティングを DailyPlay のパーソナライゼーションと組み合わせることで、さまざまな目的や成果に向けた魅力的なゲームコンテンツを作成します。
- **オンボーディングとアクティベーション：** Brazeのウェルカムシリーズに DailyPlay のスクラッチ＆ウィンやインスタントリビールゲームのリンクを埋め込み、初回購入やプロフィール入力を促進します。
- **リテンションとロイヤルティ：** 消費者がロイヤルティのマイルストーンに到達したり、Brazeでトラッキングされているキーアクションを実行した際に、その達成を祝い、ティア別の報酬をアンロックするパーソナライズされた DailyPlay ゲームをトリガーします。
- **解約防止と奪還：** Brazeで離脱傾向にあるユーザーを特定し、低負荷の DailyPlay ゲームを配信して注意を引き戻し、アプリやサイトへの再訪を促します。

## 前提条件 {#prerequisites}


| 要件 | 説明 |
| --- | --- |
| DailyPlayアカウント | このインテグレーションを使用するには、DailyPlayアカウントが必要です。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。このキーはBrazeの**設定** > **APIと識別子** > **APIキー**で作成します。詳細については、[APIキー]({{site.baseurl}}/api/basics)を参照してください。 |
| Braze RESTエンドポイント | [お客様のBrazeインスタンス]({{site.baseurl}}/api/basics#endpoints)のRESTエンドポイントURL。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

### ステップ1：接続を作成する {#step-1-create-a-connection}

1. [DailyPlayダッシュボード](https://app.dailyplay.ai/connections)で、**Connections**ページに移動し、**Add Connection**を選択します。

![アクティブなBraze接続とトリガー統計を一覧表示するDailyPlayのConnectionsページ。]({% image_buster /assets/img/dailyplay/connections_page.png %}){: style="max-width:70%;"}

{: start="2"}
2. **Provider**で**Braze**を選択します。名前、Braze REST APIキー、App ID、RESTエンドポイントを入力し、**Create Connection**を選択します。

![Brazeが選択され、APIキー、App ID、RESTエンドポイントの認証情報フィールドが表示されたDailyPlayのAdd Connectionモーダル。]({% image_buster /assets/img/dailyplay/add_connection.png %}){: style="max-width:60%;"}

### ステップ2：ストリームを作成する {#step-2-create-a-stream}

**Streams**ページに移動し、新しいストリームを作成します。

1. ステップ1で作成したBraze接続を新しいストリームに追加します。
2. **Stream Access**、**Play Start**、**Play Complete**、**Prize Redemption**など、トラッキングするトリガーイベントを設定します。
3. ゲームを作成し、ストリームに追加します。
4. ストリーム用のBraze統合コードをコピーします。

![Brazeトリガーイベントとメールテンプレート用の埋め込みコードが表示されたDailyPlayのManage Connectionsモーダル。]({% image_buster /assets/img/dailyplay/manage_connections.png %}){: style="max-width:70%;"}

### ステップ3：Brazeでキャンペーンを作成する {#step-3-create-a-campaign-in-braze}

ステップ2のコードをBrazeのキャンペーンに貼り付けます。

ユーザーがストリーム内でゲームをプレイすると、DailyPlayはイベントをトリガーし、Braze RESTエンドポイントを通じてBrazeに送信します。

### ステップ4：アクションを確認してファネルを拡張する {#step-4-inspect-actions-and-expand-your-funnel}

DailyPlayストリームでアクションを完了したユーザーは、Brazeプロファイルにカスタム属性とカスタムイベントを受け取ります。

ユースケースに必要なDailyPlayのカスタムイベントまたはカスタム属性を使用する[アクションベース]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)トリガーを設定した[キャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns)または[キャンバス]({{site.baseurl}}/user_guide/messaging/canvas)を作成します。

## BrazeでDailyPlayを使用する {#use-dailyplay-with-braze}

特定の顧客セグメントにエンゲージするには、インテグレーションの設定が完了した後に以下のステップに従ってください。

### ステップ1：DailyPlayの設定を行う {#step-1-set-up-your-dailyplay-configuration}

このセクションのインテグレーション手順に従って、Braze接続とDailyPlayストリームを設定します。インテグレーションコードをコピーしてください。

### ステップ2：Brazeキャンペーンまたはキャンバスを作成する {#step-2-create-a-braze-campaign-or-canvas}

アクションベースのトリガーを使用してキャンペーンまたはキャンバスを作成します。ユースケースに必要なDailyPlayのカスタムイベントまたはカスタム属性を選択してください。

[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)を使用して、DailyPlayが送信するプロパティをメッセージコピー内で参照できます。

**カスタム属性の例：**

{% raw %}
```liquid
Your score was {{custom_attribute.${dailyplay}.last_game_score}}
```
{% endraw %}

**カスタムイベントの例：**

ドット表記を使用して、トリガーイベントのプロパティを参照します。

{% raw %}
```liquid
{{event_properties.${dailyplay_play_complete}.properties.score}}
```
{% endraw %}

## トラブルシューティング {#troubleshooting}

追加のセットアップガイダンスやFAQについては、[DailyPlay Braze統合ドキュメント](https://docs.dailyplay.ai/connections/braze/)を参照してください。