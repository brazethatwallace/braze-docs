---
nav_title: Optimizely
article_title: Optimizely
page_order: 2
description: "このリファレンス記事では、Brazeの顧客セグメント、イベント、およびCurrentsイベントをOptimizely Data Platformに同期できる、BrazeとOptimizelyのパートナーシップについて説明します。"
alias: /partners/optimizely/
page_type: partner
search_tag: Partner
---

# Optimizely

> [Optimizely](https://www.optimizely.com/) は、デジタル製品やマーケティングキャンペーンのための実験やコンテンツ管理ツールを提供する、主要なデジタルエクスペリエンスプラットフォームです。

BrazeとOptimizelyの統合は双方向の統合であり、以下のことが可能です。

{% multi_lang_include partners/ab_testing/optimizely_integration_bullets.md %}

## 前提条件 {#prerequisites}

| 要件                     | 説明 |
|----------------------------------|-------------|
| Optimizely Data Platformアカウント | このパートナーシップを利用するには、Optimizely Data Platform（ODP）アカウントが必要です。 |
| Braze REST APIキー               | 次の権限を持つBraze REST APIキー：`users.track`、`users.export.segments`、`segments.list`、`campaigns.trigger.send`、`canvas.trigger.send`。 |
| Currents                         | Optimizelyにデータをエクスポートするには、アカウントにBraze Currentsが設定されている必要があります。 |
| Optimizely URLとトークン         | Optimizelyダッシュボードに移動し、取り込みURLとトークンをコピーすることで取得できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携 {#integration}

### ステップ1：連携を設定する {#step-1-configure-the-integration}

1. Optimizely Data Platform（ODP）の**App Directory**で、**Braze**アプリを選択し、**Install App**を選択します。
2. **Settings**タブに移動します。**Authorization**セクションで、以下を行います。
    1. Braze **REST APIキー**を入力します。
    2. Brazeの**インスタンスURL**を選択します。
    2. **Verify API Key**を選択します。
3. Brazeで、**[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents)**に移動します。
4. **Create New Current** > **Custom Currents Export**を選択します。
5. ODPで提供されたエンドポイントとトークンを使用してCurrentを設定します。これは、BrazeのイベントをODPに同期するために必要です。

![Optimizelyの認証設定。]({% image_buster /assets/img/optimizely/image1_authorization.png %})

{:start="6"}
6. ODPで、**セグメント**セクションを展開し、**セグメント to Sync**リストから特定のセグメントを選択するか、**Import All Customers**を選択してすべてのセグメントを同期します。
7. BrazeとODPの間で必要な[追加のフィールドマッピング](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/29918568615949-Integrate-Braze%23h_01J6Z1P53JVDBFZ758Q78CK1QB&sa=D&source=editors&ust=1733948158380300&usg=AOvVaw3WSAND5ie3LCVuSxUlLanR)を追加します。
8. **Save**を選択します。

![OptimizelyのBrazeセグメント同期。]({% image_buster /assets/img/optimizely/image2_syncsegment.png %})

{% alert tip %}
Brazeの顧客プロファイルをインポートするには、セグメントを選択する必要があります。セグメントを選択しない場合、連携によって顧客プロファイルはインポートされません。
{% endalert %}

### ステップ2：データフィールドをマッピングする {#step-2-map-data-fields}

この連携には、BrazeとODP間のデフォルトのデータフィールドマッピングがあります。たとえば、Brazeの**Email**フィールドは、ODPの**Last Seen Email**フィールドにマッピングされています。

![OptimizelyとBrazeのセグメントマッピングフィールド。]({% image_buster /assets/img/optimizely/image3_emailmapfield.png %})

#### 追加フィールドのマッピング（オプション） {#map-additional-fields-optional}

BrazeにODPへマッピングしたい追加のデータフィールドがある場合、ODPで以下を行います。

1. アプリの**セグメント**セクションで、**Braze User Data Fields**ドロップダウンリストからBrazeフィールドを選択します。
2. **ODP Customer Fields**ドロップダウンリストからODPフィールドを選択します。
3. **Save Field Map**を選択します。

![OptimizelyのBrazeセグメントフィールドマッピングの保存]({% image_buster /assets/img/optimizely/image4_mapfields.png %})

#### 不要なフィールドマッピングの削除（オプション） {#delete-non-required-field-mappings-optional}

不要なデータフィールドマッピングを削除することもできます。ODPで以下を行います。

1. アプリの**セグメント**セクションで、**Field Map**ドロップダウンリストから削除したいフィールドマッピングを選択します。
2. **Delete Field Map**を選択します。

![OptimizelyのBrazeセグメントフィールドマッピングの削除]({% image_buster /assets/img/optimizely/image5_deletephonefield.png %})

### ステップ3：Optimizely Data Platform（ODP）からBrazeにデータを同期する {#step-3-sync-data-from-optimizely-data-platform-odp-to-braze}

連携を設定した後、ODPでアクティベーションを設定して、ODPの顧客データをBrazeに同期できます。

1. **Activation** > **Engage**に移動し、**Create New キャンペーン**を選択します。
2. **Behavioral**を選択して、自動化された定期的な同期を設定します。
3. **Create From Scratch**を選択し、Brazeに同期するデータを表すアクティベーション名を入力します（例：**Braze Data Sync**）。
4. **Enrollment**セクションで、セグメントに一致する顧客のデータを同期するか、イベントをトリガーする顧客のデータを同期できます（ODPが顧客のメール開封を検知した場合など）。
   - **セグメントに一致する顧客：** 目的のセグメントを選択し、**Next**を選択します。<br><br>![Optimizelyのセグメント選択]({% image_buster /assets/img/optimizely/image6_segment.png %})
   - **イベントをトリガーする顧客：** **Filter**ドロップダウンリストを展開し、このBrazeへのデータ同期のトリガーとして使用するODPイベントを選択します。次に、**Automation Rules**を展開し、必要に応じて調整します。<br><br>![Optimizelyのトリガーイベント]({% image_buster /assets/img/optimizely/image7_trigger.png %})
5. **Touchpoints**を展開し、**Touchpoint 1**の編集を選択してから、**Braze**を選択します。
6. **Targeting**セクションを展開し、**Target Identifier**を選択します。
7. **Configure**セクションの**Add Users To**で、以下のオプションのいずれかを選択します。
    - **キャンペーン：** Brazeの特定のキャンペーンに顧客を追加します。このオプションを選択した後、Brazeのキャンペーンを選択する必要があります。
    - **キャンバス：** Brazeの特定のキャンバスに顧客を追加します。このオプションを選択した後、Brazeのキャンバスを選択する必要があります。
    - **Profile Update Only：** Brazeの顧客プロファイルのみを更新します。
8. （オプション）Brazeに同期する**追加フィールドの数**を選択します（最大20）。
    次に、各追加フィールドのドロップダウンリストと入力フィールドで以下を選択します。
    - 各**Field #**ドロップダウンリストで、入力したいBrazeフィールドを選択します。
    - 対応する各**Field # Value**に、選択したBrazeフィールドに送信するODPフィールドを入力します。たとえば、**Field #**ドロップダウンリストから**Company Name**を選択した場合、対応する**Field # Value**に`{{customer.company_name}}`と入力します。
9. **Save**を選択し、パンくずリストでアクティベーション名を選択します。
10. 登録で**セグメントに一致する顧客**を選択した場合は、**Touchpoints**セクションで**Select start time and schedule**を選択します。
11. 以下の設定を完了します。
    - **Recurring or Continuous：** **Recurring**を選択します。
    - **Start Date：** Brazeにデータを送信する日付を入力します。
    - **End：** デフォルトは**Never**です。特定の日付でBrazeデータ同期を終了したい場合は、ここで設定します。
    - **Repeats：** **Daily**に設定します。
    - **Repeat Every：** **1 day**に設定します。
    - **Timing：** Brazeにデータを送信する時刻を入力します。
    - **Time Zone：** このデータを送信するタイムゾーンを選択します。
12. **Apply**、**Save**、**Go Live**の順に選択します。指定した開始日時（またはトリガーイベントの発生時）に同期が開始されます。

## トラブルシューティング {#troubleshooting}

### イベントの検査 {#inspect-events}

ODP から Braze にデータが正しく同期されているかを確認するには、ODP でイベントを検査します。

1. ODP で、**Account Settings** > **Event Inspector** に移動します。
2. **Start Inspector** を選択します。
3. インスペクターでデータが利用可能になると、**Refresh** の横に数字が表示されます。選択してデータを表示します。
4. ODP と Braze がやり取りする生データが表示されます。**View Details** を選択すると、その生データのフォーマット済みバージョンが表示されます。
5. Braze から ODP に送信されるデータフィールドは `_braze` で始まります。

### アクティビティログの確認 {#check-activity-logs}

各データ同期は [ODP アクティビティログ](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/4407268804365-Use-the-Activity-Log&sa=D&source=editors&ust=1733948158385124&usg=AOvVaw2tMOxzcTKfL0-oYLT4IMpP)にも記録されます。

1. **Account Settings** > **Activity Log** に移動します。
2. カテゴリーを **braze** でフィルターします。
3. **View Details** を選択すると、一致件数を含むログ詳細のフォーマット済みビューが表示されます。