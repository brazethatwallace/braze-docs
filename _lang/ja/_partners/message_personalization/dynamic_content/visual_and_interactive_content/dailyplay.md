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

## このインテグレーションについて {#about-this-integration}

BrazeとDailyPlayのインテグレーションにより、オーディエンスセグメント全体でゲームと報酬のパフォーマンスをデプロイおよびトラッキングできます。DailyPlayのゲームと報酬システムはBrazeのオーケストレーションエンジンと連携し、受動的なオーディエンスをアクティブな参加者に変えることができます。

ゲームプレイのマイルストーン、報酬の引き換え、エンゲージメント指標をBrazeに送信して、オーディエンスセグメントを構築し、ゲーム内の行動に基づいた自動クロスチャネルメッセージングをトリガーできます。このインテグレーションにより、以下のことが可能になります。

- **ユーザープロファイルの強化:** ゲームプレイ指標、スコア、報酬ステータスをBrazeのユーザープロファイルに渡します。
- **高度なセグメンテーションの実現:** トップスコアラー、最近の勝者、報酬のアンロックに近いユーザーなど、ゲーム内の行動に基づいたオーディエンスセグメントを作成します。
- **リアルタイムキャンペーンの自動化:** ゲームインタラクションに基づいてパーソナライズされたクロスチャネルメッセージ（プッシュ、メール、アプリ内）をトリガーし、リピートプレイ、ブランドロイヤルティ、生涯価値の向上を促進します。

## ユースケース {#use-cases}

- **離脱した顧客の再エンゲージメント:** 非アクティブな顧客に、割引報酬を獲得するチャンスのあるゲームへのリンクを送信します。
- **製品やトレンドに関するアクティビティ:** 新製品やホリデーシーズン、トレンド、イベントを紹介するパーソナライズされたゲームを作成します。
- **ターゲットゲームのデプロイ:** BrazeのセグメンテーションとターゲティングをDailyPlayのパーソナライゼーションと組み合わせ、さまざまな目的や成果に向けた魅力的なゲームコンテンツを作成します。
- **オンボーディングとアクティベーション:** Brazeのウェルカムシリーズに、DailyPlayのスクラッチ＆ウィンやインスタントリビールゲームのリンクを埋め込み、初回購入やプロファイル完了を促進します。
- **リテンションとロイヤルティ:** 消費者がロイヤルティマイルストーンに到達したり、Brazeでトラッキングされている重要なアクションを実行した場合、その達成を祝い、ティア固有の報酬をアンロックするパーソナライズされたDailyPlayゲームをトリガーします。
- **チャーン防止と奪還:** Brazeで離脱しつつあるユーザーを特定し、低負荷のDailyPlayゲームを配信して注意を引き戻し、アプリやサイトへの再訪を促します。

## 前提条件 {#prerequisites}


| 要件 | 説明 |
| --- | --- |
| DailyPlayアカウント | このインテグレーションを使用するにはDailyPlayアカウントが必要です。 |
| Braze REST APIキー | `users.track`権限を持つBraze REST APIキー。このキーはBrazeの**設定** > **APIと識別子** > **APIキー**で作成します。詳細については、[APIキー]({{site.baseurl}}/api/api_key)を参照してください。 |
| Braze RESTエンドポイント | [Brazeインスタンス]({{site.baseurl}}/api/basics#endpoints)のRESTエンドポイントURL。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## インテグレーション {#integration}

### ステップ1: 接続を作成する {#step-1-create-a-connection}

1. [DailyPlayダッシュボード](https://app.dailyplay.ai/connections)で**Connections**ページに移動し、**Add Connection**を選択します。

![アクティブなBraze接続とトリガー統計を一覧表示するDailyPlayのConnectionsページ。]({% image_buster /assets/img/dailyplay/connections_page.png %}){: style="max-width:70%;"}

{: start="2"}
2. **Provider**で**Braze**を選択します。名前、Braze REST APIキー、App ID、RESTエンドポイントを入力し、**Create Connection**を選択します。

![Brazeが選択され、APIキー、App ID、RESTエンドポイントの認証情報フィールドが表示されたDailyPlayのAdd Connectionモーダル。]({% image_buster /assets/img/dailyplay/add_connection.png %}){: style="max-width:60%;"}

### ステップ2: ストリームを作成する {#step-2-create-a-stream}

**Streams**ページに移動し、新しいストリームを作成します。

1. ステップ1で作成したBraze接続を新しいストリームに追加します。
2. **Stream Access**、**Play Start**、**Play Complete**、**Prize Redemption**など、トラッキングするトリガーイベントを設定します。
3. ゲームを作成してストリームに追加します。
4. ストリームのBrazeインテグレーションコードをコピーします。

![Brazeのトリガーイベントとメールテンプレート用の埋め込みコードが表示されたDailyPlayのManage Connectionsモーダル。]({% image_buster /assets/img/dailyplay/manage_connections.png %}){: style="max-width:70%;"}

### ステップ3: Brazeでキャンペーンを作成する {#step-3-create-a-campaign-in-braze}

ステップ2のコードをBrazeのキャンペーンに貼り付けます。

ユーザーがストリーム内のゲームをプレイすると、DailyPlayはイベントをトリガーし、Braze RESTエンドポイントを通じてBrazeに送信します。

### ステップ4: アクションを確認してファネルを拡張する {#step-4-inspect-actions-and-expand-your-funnel}

DailyPlayストリームでアクションを完了したユーザーは、Brazeプロファイルにカスタム属性とカスタムイベントを受け取ります。

ユースケースに必要なDailyPlayカスタムイベントまたはカスタム属性を使用する[アクションベース]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)トリガーで[キャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns)または[キャンバス]({{site.baseurl}}/user_guide/messaging/canvas)を作成します。

## DailyPlayをBrazeで使用する {#use-dailyplay-with-braze}

特定の顧客セグメントをエンゲージするには、インテグレーションのセットアップ完了後に以下のステップに従ってください。

### ステップ1: DailyPlayの設定をセットアップする {#step-1-set-up-your-dailyplay-configuration}

このセクションのインテグレーションステップに従って、Braze接続とDailyPlayストリームをセットアップします。インテグレーションコードをコピーします。

### ステップ2: Brazeのキャンペーンまたはキャンバスを作成する {#step-2-create-a-braze-campaign-or-canvas}

アクションベーストリガーを使用してキャンペーンまたはキャンバスを作成します。ユースケースに必要なDailyPlayカスタムイベントまたはカスタム属性を選択します。

[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid)を使用して、DailyPlayが送信するプロパティをメッセージコピーで参照できます。

**カスタム属性の例:**

{% raw %}
```liquid
Your score was {{custom_attribute.${dailyplay}.last_game_score}}
```
{% endraw %}

**カスタムイベントの例:**

ドット記法を使用して、トリガーイベントのプロパティを参照します。

{% raw %}
```liquid
{{event_properties.${dailyplay_play_complete}.properties.score}}
```
{% endraw %}

## トラブルシューティング {#troubleshooting}

追加のセットアップガイダンスとFAQについては、[DailyPlay Brazeインテグレーションドキュメント](https://docs.dailyplay.ai/connections/braze/)を参照してください。