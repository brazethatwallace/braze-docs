---
nav_title: Currentsの Zeotap
article_title: Currentsの Zeotap
description: "このリファレンス記事では、Braze CurrentsとZeotapのパートナーシップについて概説します。Zeotapは、アイデンティティ解決、インサイト、データ強化を提供して、モバイルオーディエンスを発見、理解できるようにする次世代の顧客データプラットフォームです。"
page_type: partner
tool: Currents
search_tag: Partner
---

# Currentsの Zeotap {#zeotap-for-currents}

> [Zeotap](https://zeotap.com/) は、アイデンティティ解決、インサイト、データ強化を提供して、モバイルオーディエンスを発見、理解できるようにする次世代の顧客データプラットフォームです。

BrazeとZeotapの統合により、Zeotapの顧客SegmentsをBrazeのユーザープロファイルに同期することで、Campaignsの規模とリーチを拡大できます。[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)を使用すると、データをZeotapに接続し、グローススタック全体で実用的なデータにすることもできます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| --- | --- |
| Zeotapアカウント | このパートナーシップを活用するには、[Zeotapアカウント](https://zeotap.com/)が必要です。 |
| Currents | Zeotapにデータをエクスポートするには、アカウントに[Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 実装 {#implementation}

### ステップ 1: Currentsソースを作成する {#step-1-create-a-currents-source}

1. Zeotapで、**Integrate** の下の **Sources** に移動します。
2. **Create Source** を選択します。
3. カテゴリーとして **Customer Engagement Channels** を選択します。<br><br>![「Customer Engagement Channels」など、さまざまなカテゴリーを一覧表示する「Create Source」ウィンドウ。]({% image_buster /assets/img/zeotap/cec.png %}){: style="max-width:70%;"}<br><br>
4. データソースとして **Braze** を選択します。
5. ソース名を入力します。
6. 地域を選択します。<br><br>![地域とデータエンティティを選択するためのオプションがあるウィンドウ。]({% image_buster /assets/img/zeotap/select_region.png %}){: style="max-width:70%;"}<br><br>
7. **Create Source** を選択します。
8. **Implementation Details** タブに移動し、**API URL** と **Write Key** をメモします。<br><br>![API URLとWrite Keyを含むBraze Currentsの実装詳細。]({% image_buster /assets/img/zeotap/implementation_details.png %})

### ステップ 2: Currentsでデータストリーミングを設定する {#step-2-configure-data-streaming-in-currents}

1. Brazeで、**パートナー連携** > **データのエクスポート** に移動します。
2. **Create New Current** と **Custom Currents Export** を選択します。<br><br>![「Custom Currents Export」を含むドロップダウンが表示された「Create New Current」ボタン。]({% image_buster /assets/img/zeotap/custom_currents_export.png %}){: style="max-width:60%;"}<br><br>
3. 統合名と、統合でエラーが発生した場合に連絡を受けるメールアドレスを入力します。
4. **Credentials** の下に、[ステップ 1](#step-1-create-a-currents-source)でメモした次の情報を入力します。
- API URLを **Endpoint** として入力
- Write Keyを **Bearer Token** として入力<br><br>![統合の詳細および認証情報を入力するセクション。]({% image_buster /assets/img/zeotap/credentials.png %})<br><br>
5. Zeotapに送信するメッセージエンゲージメントイベントを選択します。<br><br>![メッセージエンゲージメントイベントを選択するセクションがある「General Settings」タブ。]({% image_buster /assets/img/zeotap/message_engagement_events.png %})
6. **Launch Current** を選択して変更を保存し、Zeotapへのイベント送信を開始します。

{% alert important %}
Currentsコネクターは匿名ユーザー（`external_id`を持たないユーザー）をサポートしていません。
{% endalert %}