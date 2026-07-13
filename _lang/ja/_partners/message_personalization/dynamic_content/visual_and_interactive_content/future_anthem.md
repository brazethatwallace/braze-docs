---
nav_title: Future Anthem
article_title: Future Anthem
description: "この参考記事では、スポーツベッティングおよびiGamingパーソナライゼーション向けのリアルタイムAIプラットフォームであるFuture AnthemとBrazeのパートナーシップについて説明します。"
alias: /partners/future_anthem/
page_type: partner
search_tag: Partner
---

# Future Anthem

> [Future Anthem](https://www.futureanthem.com/)のリアルタイムAIプラットフォームは、スポーツ、カジノ、ビンゴ、宝くじにわたるパーソナライゼーションを実現します。Brazeの顧客は、好きなゲーム、好きなチーム、エンゲージメントスコア、次のベットのレコメンデーション、予想される次のベットなど、業界特有の属性でプレイヤープロファイルを強化できます。
>
> リアルタイム体験、ダイナミックオーディエンス、コンテンツレコメンデーションを通じて提供されるすべての属性は、ライブのプレイヤー行動に基づいて構築されるため、Brazeの顧客はその瞬間にアクションを起こすことができます。

_この統合はFuture Anthemによって管理されています。_

{% alert important %}
この機能は現在早期アクセス段階です。開始するには、Future Anthemカスタマーサクセスチームにお問い合わせください。
{% endalert %}

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Future Anthemアカウント | Future Anthemアカウントが必要です。 |
| Braze REST APIキー | [`users.track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)の権限を持つBraze REST APIキー。これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | インスタンスに一致するBraze [RESTエンドポイント]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)（例: `rest.iad-01.com`）。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## ユースケース {#use-cases}

この統合により、以下のことが可能になります。

- エンゲージメントスコアが高いプレイヤーを特定し、限定プロモーションやVIP特典などのパーソナライズされたオファーでターゲットにします。
- プレイヤーがすでに好きなゲームに基づいて、類似のゲームを提案します。

## 統合 {#integration}

Future Anthemカスタマーサクセスチームが統合の設定をサポートします。Future Anthemカスタマーサクセスの担当者にご連絡いただければ、Brazeに送信する最も関連性の高い属性を特定するお手伝いをいたします。

| Future Anthemの属性例 | Brazeの属性例 |
| ----------------------------------- | --------------------------- |
| ![プレイヤーのプロファイル属性を表示するFuture Anthemダッシュボード。]({% image_buster /assets/img/future_anthem/future_anthem_example_attributes.png %}) | ![Future Anthemから同期されたカスタムオブジェクト属性を表示するBrazeユーザープロファイル。]({% image_buster /assets/img/future_anthem/braze_example_attributes.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Integration" }

## Brazeカスタム属性 {#braze-custom-attributes}

以下は利用可能なBrazeカスタム属性です。詳細については、[Future Anthem: Getting Started](https://knowledge.futureanthem.com/getting-started)を参照してください。

{% tabs local %}
{% tab ベットレコメンデーション %}

| サブカテゴリー | 例（JSON） | データタイプ |
| ----------- | ---------------- | --------- |
| ユーザー設定 | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}` | オブジェクト |
| シングルベットのレコメンデーション | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}` | オブジェクト |
| アキュムレーターベットのレコメンデーション（イベントラベル） | `{"Bet_1": "Haaland goal vs. Manchester United", "Bet_2": "Liverpool vs. Everton"}` | オブジェクト |
| アキュムレーターベットのレコメンデーション（数値オッズ） | `{"Bet_1": 1.5, "Bet_2": 2}` | オブジェクト |
| ベットビルダーのベットレコメンデーション | `{"Sport":"American Football", "Competition":"NFL", "Event":"Seahawks@Giants", "Market":"MoneyLine", "Selection":"Seahawks"}` | オブジェクト |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze custom attributes" }

{% endtab %}
{% tab ボーナスレコメンデーション %}

| サブカテゴリー | 例 | データタイプ |
| ----------- | ------- | --------- |
| NGR（純ゲーム収益、生涯） | 2232 | 数値 |
| NGR14（純ゲーム収益、直近14日間のアクティビティ） | 42 | 数値 |
| プレイヤー収益性スコア | 130 | 数値 |
| エンゲージメントスコア | 0.78 | 数値 |
| 解約リスクスコア | 0.02 | 数値 |
| 次回ベット予定日 | 2024-08-29 | 時刻 |
| ベット＆ゲットボーナス値レコメンデーション | 20 | 数値 |
| その他のボーナス値レコメンデーション | 0 | 数値 |
| 将来のCLTV | 3126 | 数値 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze custom attributes" }

{% endtab %}
{% tab ゲームレコメンデーション %}

| サブカテゴリー | 例 | データタイプ |
| ----------- | ------- | --------- |
| あなたにおすすめ | Fluffy Favourites, Fishin' Frenzy, Big Bass Bonanza, Rainbow Gold, Wild West | 配列 |
| お気に入りのゲーム | Fishin' Frenzy | 配列 |
| おすすめ新作ゲーム | Sticky Bees, Beware the Deep Megaways, Gold Party, The Flintstones | 配列 |
| あなたのようなプレイヤーがプレイ中（協調フィルタリング） | Gold Blitz, Big Bass Splash, Rick and Morty, Book of Dead, Gates of Olympus, Luck O' the Irish | 配列 |
| あなたがプレイしたから（ゲームの類似性） | Fluffy Favourites 2, Luck O' the Irish Express, Gold Cash, Aztec Treasure Hunt, Stars Bonanza | 配列 |
| 次のおすすめ（ゲームシーケンス） | Fishin' Frenzy The Big Catch, Big Banker, 9 Masks of Fire, Super Lion, Fishin' Bigger Pots of Gold | 配列 |
| 人気ゲーム | Temple of Iris, Fishin' Frenzy, Fishing Reward, Crazy Time, Fluffy Favourites | 配列 |
| トレンドゲーム | Pig Banker, Hyper Gold, Pyramid King, Gold Cash | 配列 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze custom attributes" }

{% endtab %}

{% tab プレイヤークラスター %}

| サブカテゴリー | 例 | データタイプ |
| ----------- | ------- | --------- |
| プレイヤーが属するクラスターを表示 | High Value Game Diverse | 文字列 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze custom attributes" }

{% endtab %}

{% tab プレイヤーサステイン（プレイヤーの潜在リスク） %}

| サブカテゴリー | 例 | データタイプ |
| ----------- | ------- | --------- |
| リスクスコア | 0.5 | 数値 |
| リスクのあるプレイヤー | True | ブール値 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze custom attributes" }

{% endtab %}
{% endtabs %}