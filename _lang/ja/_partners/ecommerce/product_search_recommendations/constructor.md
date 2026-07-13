---
nav_title: Constructor
article_title: Constructor
description: "このリファレンス記事では、Braze と Constructor のパートナーシップについて説明します。このパートナーシップにより、Constructor の Offsite Product Discovery を活用して、Braze メッセージでパーソナライズされたおすすめ商品を動的に生成して配信することができます。"
alias: /partners/constructor/
page_type: partner
search_tag: Partner
---

# Constructor

> [Constructor](https://constructor.com/) は、AI と機械学習を利用してパーソナライズされた検索、レコメンデーション、ブラウジング体験をeコマースおよび小売のWebサイトに提供する、検索・商品発見プラットフォームです。

Braze と Constructor の統合により、Constructor の Offsite Product Discovery を使用して、Braze メッセージでパーソナライズされたおすすめ商品を動的に生成して配信することができます。

## ユースケース {#use-cases}

- **放棄カートと注文後のフォローアップ**: ユーザーの行動とカートの内容に基づいて、おすすめ商品を動的に生成し、放棄カートのリマインダーや注文後の提案をパーソナライズして送信します。
- **放棄カートのアイテムと類似した商品のおすすめ**: ユーザーのカートに残されているアイテムに類似した商品を提案し、エンゲージメントの維持と代替品の提供を可能にします。
- **最近閲覧したアイテムのリマインダー**: 最近閲覧したがまだ購入していないアイテムについてユーザーに通知し、購入を完了するよう促します。
- **プロモーションキャンペーン**: 季節的なセールや特別なオファーに向けて、ユーザーの好みに合わせてキュレートされたおすすめ商品を含むパーソナライズされたプロモーションメッセージを配信します。
- **視覚的に類似した商品の提案**: ユーザーが最近閲覧した商品と視覚的に類似したアイテムをおすすめし、ユーザーが好むかもしれない関連オプションを発見できるよう支援します。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|-------------|-------------|
| Constructor のアカウント | このパートナーシップを利用するには、Offsite Discovery サービスが有効化された Constructor アカウントが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

Constructor のオンボーディングチームと協力して、統合プロセスを完了します。Webサイトやその他の関連データソースからの行動データが利用可能であり、おすすめ商品のパーソナライズが可能であることを確認してください。Constructor のオンボーディングチームは、Braze メッセージで使用するために必要な HTML スニペットの設定もサポートします。

## Constructor の Offsite Discovery API URL {#constructors-offsite-discovery-api-url}

Constructor の Offsite Discovery API URL を使用して、商品画像をレンダリングし、ユーザーを適切な商品詳細ページに誘導できます。以下は、エンドポイントの構造の内訳とその使用例です。

### 例 {#example}

```html
<a href="https://offsite-discovery.cnstrc.com/v1/product/url?position=[position]&ui=[ui]&pod_id=[pod_id]&key=[key]&style_id=[style_id]&campaign_id=[campaign_id]" target="_blank">
  <img
    src="https://offsite-discovery.cnstrc.com/v1/product/image?position=[position]&ui=[ui]&pod_id=[pod_id]&key=[key]&style_id=[style_id]&campaign_id=[campaign_id]"
    width="200"
    border="0"
    alt="Shop Now"
  />
</a>
```

### パラメーター {#parameters}

| パラメーター | 説明 |
|-------------|-------------|
| `position` | 提案リスト内の特定のおすすめアイテムのランキングを参照します（例: `position = 2`）。<br>![アイテムの順位ランキング。]({% image_buster /assets/img/constructor/constructor_position.png %}) |
| `ui` | レコメンデーション結果のパーソナライズに不可欠な、ユーザーの識別子を表します。`ui` パラメーターをBrazeで顧客の `external_id` に設定します。省略した場合、Constructor はユーザー固有のレコメンデーションではなく、一般的なレコメンデーションを返します。 |
| `pod_id` | レコメンデーションの戦略とサーチアンダイジングルールを含むポッドの識別子です（例: ベストセラー戦略を持つポッドは、パーソナライズされたベストセラーを生成します）。 |
| `key` | 当該顧客の Constructor インデックスキーです。 |
| `style_id` | 商品カードに表示される画像を決定します。例えば、異なる `style_ids` はそれぞれ異なる商品カード画像を表示します。 |
| `campaign_id` | メールキャンペーンの一意のIDです。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="パラメーター" }

### オプション入力 {#optional-inputs}

| 入力 | 説明 |
|-------------|-------------|
| `item_id` | シードアイテムを表します。代替、補完、バンドルなど、アイテム間ベースの戦略に必要です。例えば、メールの最初のアイテムがシードアイテムであり、後続のアイテムは代替アイテムとなります。 |
| `num_results` | メールに追加する商品の数です。デフォルトは10で、最大100です。例えば、`num_results = 3` は、3つのレコメンデーションが追加されることを意味します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="オプション入力" }