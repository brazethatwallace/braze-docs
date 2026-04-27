---
nav_title: GRAVTY®
article_title: GRAVTY® Loyalty Platform
description: "この記事では、BrazeとGRAVTY®のパートナーシップについて説明します。GRAVTY®はエンタープライズグレードのロイヤルティプラットフォームであり、ブランドがデータドリブン型のロイヤルティプログラムを設計、管理、スケーリングし、カスタマーエンゲージメントとリテンションを強化できるようにします。"
alias: /partners/lji/
page_type: partner
search_tag: Partner
---

# GRAVTY® Loyalty Platform

> [GRAVTY®](https://www.lji.io/)は、Loyalty Juggernaut Inc.（LJI）が提供するエンタープライズグレードのロイヤルティプラットフォームです。小売、旅行、レストラン（クイックサービスレストランを含む）、金融サービスなどのブランドが次世代プログラムを設計、管理、スケーリングし、パーソナライズされたデータドリブン型の体験を通じてエンゲージメント、リテンション、顧客生涯価値の測定可能な成長を促進できるようにします。

柔軟なAPIファーストアーキテクチャ上に構築されたGRAVTY®は、リアルタイムの獲得と消費、パートナーエコシステム管理、チャネル間の統合をサポートします。チームはプログラムをより迅速に起動し、反復改善を行い、ロイヤルティ体験を大規模に提供できます。

_この統合はLJIによって管理されています。_

## 統合について {#about-the-integration}

BrazeとGRAVTY®の統合は、両プラットフォーム間でロイヤルティデータとメッセージングトリガーを接続します。GRAVTY®はユーザーデータを属性、イベント、購入としてBrazeに送信します。Brazeはそのデータを保存し、SMS、メール、プッシュ通知などのチャネルを通じてメッセージを配信します。同期されたデータをセグメンテーション、パーソナライゼーション、トリガーに使用します。

## 前提条件 {#prerequisites}

開始する前に、以下が必要です。

| 要件 | 説明 |
| :--- | :--- |
| GRAVTY®アカウント | 統合の設定とイベントサブスクリプションの管理権限を持つGRAVTY®アカウント。 |
| Brazeアカウント | APIアクセスが有効になっているアクティブなBrazeアカウント。 |
| Braze REST APIキー | `campaigns.trigger.send`、`canvas.trigger.send`、`users.track`の権限を持つREST APIキー。<br><br> このキーはBrazeダッシュボードの**設定** > **APIキー**から作成します。 |
| Braze APIエンドポイント | BrazeのRESTエンドポイント（例：`https://rest.fra-01.braze.eu`）。詳細については、[Brazeインスタンスとエンドポイント]({{site.baseurl}}/api/basics/#endpoints)を参照してください。 |
| CampaignまたはCanvas ID | GRAVTY®からトリガーする**Campaigns**または**Canvas**ワークフローのID。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## ユースケース {#use-cases}

この統合は、以下のBraze機能をサポートします。

- **ユーザーデータ同期（`/users/track`）：** メンバーの属性、イベント、購入をBrazeに同期し、セグメンテーションとパーソナライゼーションに活用します。
- **Campaignトリガー（`/campaigns/trigger/send`）：** Braze Campaignsを使用して、ワンタイムまたはトランザクションメッセージをトリガーします。
- **Canvasトリガー（`/canvas/trigger/send`）：** Braze **Canvas**を使用して、マルチステップジャーニーとライフサイクルメッセージングを開始します。
- **セグメンテーションとパーソナライゼーション：** 同期されたデータからターゲットオーディエンスを構築し、パーソナライズされたコミュニケーションを配信します。

## 統合 {#integration}

GRAVTY®とBrazeの統合はAPIベースです。リアルタイムのデータ同期とコミュニケーショントリガーをサポートします。

![GRAVTY®がBraze APIにデータとトリガーを送信し、SMS、メール、プッシュ、WhatsAppにメッセージを配信するフロー図。]({% image_buster /assets/img/lji/braze-gravty-integration.png %})

### ステップ 1: BrazeをGRAVTY®に接続する {#step-1-connect-braze-with-gravty}

1. GRAVTY®の**Subscriber Setup**に移動して、外部統合を管理します。
2. **Add New Subscriber**を選択します。
3. 統合プロバイダーとして**Braze**を選択します。
4. 以下を入力します。
   * **API URL**（BrazeのRESTエンドポイント）
   * **API Key**（BrazeのREST APIキー）
5. 設定を保存し、接続がアクティブであることを確認します。

![Brazeが選択され、API URLとAPIキーフィールド、およびアクティブなサブスクライバートグルが表示されたGRAVTY® Add Subscriberフォーム。]({% image_buster /assets/img/lji/braze-subscriber-setup.png %}){: style="max-width:70%;"}

### ステップ 2: テンプレート属性マッピングを設定する {#step-2-configure-template-attribute-mapping}

Brazeサブスクライバーを保存すると、GRAVTY®は**Template Attribute Mapping**ページを開きます。これを使用してフィールドをBrazeにマッピングします。

1. **Add New Field**を選択します。
2. リストから**GRAVTY®属性**を選択します。
3. 値がBrazeに表示される**Braze属性名**（カスタム属性）を入力します。

{% alert important %}
`external_id`をマッピングする必要はありません。GRAVTY®はメンバーIDをハッシュ化して内部的に生成し、Brazeはそのハッシュ値をユーザープロファイルの`external_id`として受け取ります。<br><br> 統合を有効にする前に、これが現在Brazeで`external_id`を設定している方法と一致していることを確認してください。Brazeが同じユーザーに対して異なる`external_id`を既に使用している場合は、データを同期する前にLJIと協力して識別子を整合させてください。
{% endalert %}

{: start="4"}
4. ステップ1〜3を繰り返して、さらにマッピングを追加します。
5. **Save**を選択します。

![テンプレート設定、同期設定、およびBraze用のエンティティ、GRAVTY®属性、テンプレート属性フィールドをマッピングするテーブルが表示されたGRAVTY® Subscription Setupページ。]({% image_buster /assets/img/lji/gravty-attribute-mapping.png %})

{% alert note %}
この統合は、数値（整数、浮動小数点）、文字列、配列、ブール値、オブジェクト、オブジェクトの配列、日付を含むBrazeカスタム属性データタイプをサポートします。
{% endalert %}

### ステップ 3: 統合をテストする {#step-3-test-the-integration}

GRAVTY®でサンプルイベントをトリガーして、同期、コミュニケーショントリガー、エンドツーエンドのフローを確認します。

![GRAVTY®マッピングから入力されたプロファイル、カスタム属性（ティア、日付、国、市区町村）、カスタムイベントが表示されたBrazeユーザープロファイル概要。]({% image_buster /assets/img/lji/braze-member-profile.png %})

## サポート {#support}

統合サポートまたはトラブルシューティングについては、LJI（[support@lji.io](mailto:support@lji.io)）にお問い合わせください。