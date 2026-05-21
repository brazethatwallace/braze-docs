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
| キャンペーンまたはキャンバス ID | GRAVTY®からトリガーする**キャンペーン**または**キャンバス**ワークフローのID。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## ユースケース {#use-cases}

この統合は、以下のBraze機能をサポートします。

- **ユーザーデータ同期（`/users/track`）：** メンバーの属性、イベント、購入をBrazeに同期し、セグメンテーションとパーソナライゼーションに活用します。
- **キャンペーントリガー（`/campaigns/trigger/send`）：** Braze キャンペーンを使用して、ワンタイムまたはトランザクションメッセージをトリガーします。
- **キャンバストリガー（`/canvas/trigger/send`）：** Braze **キャンバス**を使用して、マルチステップジャーニーとライフサイクルメッセージングを開始します。
- **セグメンテーションとパーソナライゼーション：** 同期されたデータからターゲットオーディエンスを構築し、パーソナライズされたコミュニケーションを配信します。

## 統合 {#integration}

GRAVTY®とBrazeの統合はAPIベースであり、GRAVTY®とBraze間のリアルタイムデータ同期とコミュニケーショントリガーを可能にします。

### ステップ 1: BrazeをGRAVTY®に接続する {#step-1-connect-braze-with-gravty}

1. GRAVTY®の**Subscriber Setup**に移動して、外部統合を管理します。
2. **Add New Subscriber**を選択します。
3. 統合プロバイダーとして**Braze**を選択します。
4. 以下を入力します。
   * **API URL**（BrazeのRESTエンドポイント）
   * **API Key**（BrazeのREST APIキー）
5. 設定を保存し、接続がアクティブであることを確認します。

![Brazeが選択され、API URLとAPIキーフィールド、およびアクティブなサブスクライバートグルが表示されたGRAVTY® Add Subscriberフォーム。]({% image_buster /assets/img/lji/braze-subscriber-setup.png %}){: style="max-width:70%;"}

### ステップ 2: イベントトリガーを設定する {#step-2-configure-event-trigger}

GRAVTY®で、メンバーのアクティビティが定義した条件（例：トランザクション、ポイント獲得、ティア変更、プログラム登録）を満たしたときに実行されるイベントを作成します。

1. GRAVTY®の**Events**セクションに移動します。
2. **Create Event**をクリックします。
3. イベント条件を定義します（例：トランザクション作成、ポイント獲得、ティアアップグレード）。
4. イベントがトリガーされるタイミングを決定するルールを設定します。
5. Brazeサブスクライバーをイベントに紐付けて、コミュニケーショントリガーを有効にします。
6. イベント設定を保存します。

以下は、メンバーがプログラムに登録されたときにトリガーされるよう設定されたイベントの例です。

![メンバーのプログラム登録用に設定されたGRAVTY®イベント設定。Brazeがサブスクライバーとして紐付けられています。]({% image_buster /assets/img/lji/event-configuration.png %})

### ステップ 3: テンプレート属性マッピングを設定する {#step-3-configure-template-attribute-mapping}

イベントを設定した後、サブスクライバー設定を完了してデータ同期とコミュニケーショントリガーを有効にします。

1. サブスクライバードロップダウンから、ステップ1で作成した**Brazeサブスクライバー**を選択します。
2. ユースケースに基づいて、適切な**チャネル**（**キャンペーン**または**キャンバス**）を選択します。データ同期のみのシナリオでは、チャネルを未選択のままにできます。
3. 該当する場合、**Template Name**フィールドに対応する**キャンペーン ID**または**キャンバス ID**を入力します。
4. 同期やトリガーベースのメッセージングをサポートするようにコミュニケーションタイプを設定します。

GRAVTY®でフィールドマッピングを設定するには：

1. **Add New Field**をクリックします。
2. ドロップダウンから**GRAVTY®属性**を選択します。
3. データのマッピング先となる対応する**Braze属性名**を入力します。

{% alert important %}
`external_id`をマッピングする必要はありません。GRAVTY®はメンバーID（GRAVTY®内の一意のメンバー識別子）をハッシュ化して内部的に生成し、Brazeはそのハッシュ値をユーザープロファイルの`external_id`として受け取ります。<br><br> 統合を有効にする前に、これが現在Brazeで`external_id`を設定している方法と一致していることを確認してください。Brazeが同じユーザーに対して異なる`external_id`を既に使用している場合は、データを同期する前にLJIと協力して識別子を整合させてください。
{% endalert %}

{: start="4"}
4. 必要に応じてステップ**1〜3**を繰り返し、追加のマッピングを行います。
5. **Save**をクリックして設定を適用します。

![Brazeメンバー同期用の属性マッピング設定。]({% image_buster /assets/img/lji/gravty-attribute-mapping.png %})

{% alert note %}
この統合は、数値（整数、浮動小数点）、文字列、配列、ブール値、オブジェクト、オブジェクトの配列、日付を含むすべてのBrazeカスタム属性データタイプをサポートします。
{% endalert %}

### ステップ 4: 統合をテストする {#step-4-test-the-integration}

GRAVTY®でサンプルイベントをトリガーして、同期、コミュニケーショントリガー、および統合全体が期待どおりに動作していることを確認します。

* メンバーデータがBrazeに同期され、メンバープロファイルに反映されます。

![設定されたフィールドマッピングに基づいてデータフィールドが入力されたBrazeメンバープロファイル。]({% image_buster /assets/img/lji/braze-member-profile.png %})

* 設定されたキャンペーンまたはキャンバスに基づいてコミュニケーションがトリガーされます。

![Brazeからトリガーされたメールの例。]({% image_buster /assets/img/lji/braze-email-example.png %})

## サポート {#support}

統合サポートまたはトラブルシューティングについては、LJI（[support@lji.io](mailto:support@lji.io)）にお問い合わせください。