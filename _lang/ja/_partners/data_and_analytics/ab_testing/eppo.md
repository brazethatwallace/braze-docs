---
nav_title: Eppo
article_title: Eppo
description: "EppoとBrazeの統合方法について説明します。"
alias: /partners/eppo/
page_type: partner
search_tag: Partner
---

# Eppo

> [Eppo](https://www.geteppo.com/) は、チームがABテストを実行し、大規模に機能を管理し、データドリブン型の意思決定にAI駆動のインサイトを活用できるようにする次世代の実験プラットフォームです。

*この統合は、Eppoによって管理されています。*

BrazeとEppoの統合により、BrazeでABテストを設定し、Eppoで結果を分析することで、インサイトを明らかにし、メッセージパフォーマンスを収益やリテンションなどの長期的なビジネス指標に結びつけることができます。

## 前提条件 {#prerequisites}

| 要件                        | 説明                                                                         |
|------------------------------------|-------------------------------------------------------------------------------------|
| Eppo アカウント                       | このパートナーシップを活用するには、Eppo アカウントが必要です。                   |
| Currents または Snowflake データ共有 | Eppo が実験データを分析するには、Currents または Snowflake データ共有が必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## インテグレーション {#integration}

### ステップ1：Braze で Currents または Snowflake データ共有を設定する {#step-1-configure-currents-or-snowflake-data-sharing-in-braze}

Eppo はデータウェアハウス内で直接実験を分析します。このインテグレーションを有効にするには、Eppo に接続されているデータウェアハウスで Braze のメッセージエンゲージメントデータが利用可能である必要があります。Currents を使用して Braze からキャンペーンデータをエクスポートするか、[Snowflake データ共有]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)を使用して Snowflake インスタンス内の Braze データにアクセスできます。

### ステップ2：Braze のキャンペーンまたはキャンバスで実験を設定する {#step-2-set-up-your-experiment-in-a-braze-campaign-or-canvas}

キャンペーンやキャンバスでネイティブの AB テスト機能を使用できます。詳しくは、[多変量テストと AB テスト]({{site.baseurl}}/user_guide/messaging/ab_testing)を参照してください。

### ステップ3：Eppo で Braze の実験を測定するための設定を行う {#step-3-set-up-eppo-to-measure-braze-experiments}

Eppo で Braze データを使用して実験を実行するには、Braze からエクスポートされたユーザーレベルのメッセージイベントデータに基づいて、データウェアハウスに[割り当てテーブル](https://docs.geteppo.com/data-management/definitions/assignment-sql/)を作成します。キャンバスとキャンペーンの実験では異なるメタデータに依存するため、それぞれ別のテーブルを作成することを推奨します。

{% tabs local %}
{% tab キャンバス実験 %}
キャンバス実験の場合、割り当ては以下のいずれかで作成できます：

- キャンバスのエントリレベル（`users.canvas.Entry`）
- またはキャンバスの実験ステップ（`users.canvas.experimentstep.SplitEntry`）

これらの場合、`canvas_name`、`experiment_step_id`、`canvas_variation_name`、`experiment_split_id` などのフィールドを使用して、実験名とバリエーションを定義します。

{% endtab %}

{% tab キャンペーン実験 %}
キャンペーン実験の場合、送信イベント（プッシュ、メール、SMS など）を使用して、ユーザーが実験に参加したタイミングを判定します。`campaign_name`、`message_variation_name`、`time` を使用して割り当てテーブルにデータを格納します。

{% endtab %}
{% endtabs %}

メッセージ固有の指標（クリックや開封など）を追跡するには、ユーザー IDとキャンペーンまたはキャンバス名を結合した `combined_id` を作成して、**セカンダリエンティティ**を含めます。この `combined_id` は、指標を正しい実験およびバリエーションに関連付けるために、ファクトテーブルでも使用されます。

Eppo はこれらの割り当てテーブルとファクトテーブルを使用して結果を分析します。今後の実験設定を標準化するために、Eppo で**プロトコル**を設定することを推奨します。詳しくは、[Eppo のドキュメント](https://docs.geteppo.com/guides/marketing/integrating-with-braze/)を参照してください。

## サポート {#support}

Braze Currentsの設定、Snowflakeデータ共有、または多変量キャンペーンの設定に関するご質問は、Brazeのカスタマーサクセスマネージャーにお問い合わせください。

Brazeの実験を測定するためのEppoの設定に関するサポートについては、Eppoサポートチームにお問い合わせください。