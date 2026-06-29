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

| 必要条件 | 説明 |
|---|---|
| Eppoアカウント | このパートナーシップを利用するには、Eppoアカウントが必要です。 |
| CurrentsまたはSnowflakeデータ共有 | Eppoが実験データを分析するには、CurrentsまたはSnowflakeデータ共有が必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

### ステップ 1:BrazeでCurrentsまたはSnowflakeデータ共有を設定する {#step-1-configure-currents-or-snowflake-data-sharing-in-braze}

Eppoはデータウェアハウスで直接実験を分析します。統合を有効にするには、Brazeのメッセージエンゲージメントデータが、Eppoに接続されたデータウェアハウスで利用可能である必要があります。Currentsを使用してBrazeからCampaignデータをエクスポートしたり、[Snowflakeデータ共有]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)を使用してSnowflakeインスタンスでBrazeデータにアクセスしたりできます。

### ステップ 2:BrazeのCampaignまたはCanvasで実験を設定する {#step-2-set-up-your-experiment-in-a-braze-campaign-or-canvas}

CampaignsやCanvasesでネイティブのABテスト機能を使用できます。詳しくは、[多変量テストとABテスト]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#what-are-multivariate-and-ab-testing)を参照してください。

### ステップ 3:Eppoを設定してBrazeの実験を測定する {#step-3-set-up-eppo-to-measure-braze-experiments}

EppoでBrazeデータを使用して実験を実行するには、Brazeからエクスポートされたユーザーレベルのメッセージイベントデータに基づいて、データウェアハウスに[割り当てテーブル](https://docs.geteppo.com/data-management/definitions/assignment-sql/)を作成します。CanvasとCampaignの実験は異なるメタデータに依存しているため、別々のテーブルを使用することを推奨します。

{% tabs local %}
{% tab Canvas実験 %}
Canvasの実験では、割り当ては以下のいずれかで作成できます。

- Canvasエントリレベル（`users.canvas.Entry`）
- Canvas実験ステップ（`users.canvas.experimentstep.SplitEntry`）

このようなケースでは、`canvas_name`、`experiment_step_id`、`canvas_variation_name`、`experiment_split_id`のようなフィールドが、実験名とバリエーションを定義するために使用されます。

{% endtab %}

{% tab Campaign実験 %}
Campaignの実験では、送信イベント（プッシュ、メール、SMSなど）を使って、ユーザーがいつ実験に参加したかを判断します。`campaign_name`、`message_variation_name`、および`time`は、割り当てテーブルに入力するために使用されます。

{% endtab %}
{% endtabs %}

メッセージ固有の指標（クリック数や開封など）をトラッキングするには、ユーザーIDとCampaign名またはCanvas名を結合した`combined_id`を作成することによって**セカンダリエンティティ**を含めます。この`combined_id`は、ファクトテーブルでも使用され、指標を正しい実験とバリエーションに合わせます。

Eppoは、これらの割り当てとファクトテーブルを使用して結果を分析します。Eppoで**プロトコル**を設定して、将来の実験セットアップを標準化することをお勧めします。詳細については、[Eppoのドキュメント](https://docs.geteppo.com/guides/marketing/integrating-with-braze/)を参照してください。

## サポート {#support}

Braze Currentsの設定、Snowflakeデータ共有、または多変量Campaignsの設定については、Brazeカスタマーサクセスマネージャーにお問い合わせください。

Brazeの実験を測定するためのEppoの設定に関するサポートについては、Eppoサポートチームにお問い合わせください。