---
nav_title: Optimizely
article_title: Optimizely
page_order: 2
description: "このリファレンス記事では、Braze と Optimizely のパートナーシップについて説明します。Brazeの顧客セグメント、イベント、および Currentsイベントを Optimizely Data Platform に同期できます。"
alias: /partners/optimizely/
page_type: partner
search_tag: Partner
---

# Optimizely

> [Optimizely](https://www.optimizely.com/) は、デジタル製品やマーケティングキャンペーンのための実験やコンテンツ管理ツールを提供する、主要なデジタルエクスペリエンスプラットフォームです。

Braze と Optimizely の統合は双方向の統合であり、以下のことが可能です。

- Brazeの顧客セグメントとイベントをOptimizely Data Platform (ODP) に毎晩同期して、Optimizely の顧客プロファイル、レポート、およびセグメンテーションを強化します。
- Braze Currentsイベントを Braze から Optimizely のレポートツールに送信します。
- ODP の顧客データとイベントを Braze に同期して、Brazeの顧客データを強化し、ODP の顧客イベントに基づいて Braze メッセージングをトリガーします。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|----------------------------------|-------------|
| Optimizely Data Platform アカウント | このパートナーシップを活用するには、Optimizely Data Platform (ODP) アカウントが必要です。 |
| Braze REST APIキー | 以下の権限を持つ Braze REST APIキー: `users.track`、`users.export.segments`、`segments.list`、`campaigns.trigger.send`、および `canvas.trigger.send`。 |
| Currents | データを Optimizely にエクスポートするには、アカウントに Braze Currentsを設定する必要があります。 |
| Optimizely の URL とトークン | Optimizely ダッシュボードに移動し、取り込み URL とトークンをコピーすることで取得できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

### ステップ 1: 統合を設定する {#step-1-configure-the-integration}

1. Optimizely Data Platform (ODP) の **App Directory** で、**Braze** アプリを選択し、**Install App** を選択します。
2. **Settings** タブに移動します。**Authorization** セクションで、以下を実行します。
    1. Braze **REST APIキー**を入力します。
    2. Braze **Instance URL** を選択します。
    2. **Verify API Key** を選択します。
3. Brazeで、**[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/)** に移動します。
4. **Create New Current** > **Custom Currents Export** の順に選択します。
5. ODP で提供されるエンドポイントとトークンを使用して Current を設定します。これは、BrazeイベントをODP に同期するために必要です。

![Optimizely の認証設定画面。]({% image_buster /assets/img/optimizely/image1_authorization.png %})

{:start="6"}
6. ODP で、**セグメント** セクションを展開し、**セグメント to Sync** リストから特定のセグメントを選択するか、**Import All Customers** を選択してすべてのセグメントを同期します。
7. Braze と ODP の間で必要な[追加フィールドマッピング](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/29918568615949-Integrate-Braze%23h_01J6Z1P53JVDBFZ758Q78CK1QB&sa=D&source=editors&ust=1733948158380300&usg=AOvVaw3WSAND5ie3LCVuSxUlLanR)を追加します。
8. **Save** を選択します。

![Optimizely と Brazeのセグメント同期画面。]({% image_buster /assets/img/optimizely/image2_syncsegment.png %})

{% alert tip %}
Brazeの顧客プロファイルをインポートするには、セグメントを選択する必要があります。セグメントを選択しない場合、統合で顧客プロファイルはインポートされません。
{% endalert %}

### ステップ 2: データフィールドをマッピングする {#step-2-map-data-fields}

統合には、Braze と ODP 間のデフォルトのデータフィールドマッピングがあります。たとえば、Brazeの **Email** フィールドは、ODP の **Last Seen Email** フィールドにマッピングされます。

![Optimizely と Brazeのセグメントマッピングフィールド画面。]({% image_buster /assets/img/optimizely/image3_emailmapfield.png %})

#### 追加フィールドのマッピング（オプション） {#map-additional-fields-optional}

ODP にマッピングする追加のデータフィールドが Braze にある場合は、ODP で以下の手順を実行します。

1. アプリの **セグメント** セクションで、**Braze User Data Fields** ドロップダウンリストから Braze フィールドを選択します。
2. **ODP Customer Fields** ドロップダウンリストから ODP フィールドを選択します。
3. **Save Field Map** を選択します。

![Optimizely と Brazeのセグメントフィールドマッピング保存画面]({% image_buster /assets/img/optimizely/image4_mapfields.png %})

#### 不要なフィールドマッピングの削除（オプション） {#delete-non-required-field-mappings-optional}

不要なデータフィールドマッピングを削除することもできます。ODP で次の手順を実行します。

1. アプリの **セグメント** セクションで、**Field Map** ドロップダウンリストから削除するフィールドマッピングを選択します。
2. **Delete Field Map** を選択します。

![Optimizely と Brazeのセグメントフィールドマッピング削除画面]({% image_buster /assets/img/optimizely/image5_deletephonefield.png %})

### ステップ 3: Optimizely Data Platform (ODP) から Braze へデータを同期する {#step-3-sync-data-from-optimizely-data-platform-odp-to-braze}

統合を設定した後、ODP でアクティベーションを設定して、ODP の顧客データを Braze に同期できます。

1. **Activation** > **Engage** に進み、**Create New キャンペーン** を選択します。
2. **Behavioral** を選択して、自動定期同期を設定します。
3. **Create From Scratch** を選択し、Brazeに同期するデータを表すアクティベーションの名前を入力します（**Braze Data Sync** など）。
4. **Enrollment** セクションでは、セグメントに一致する顧客のデータを同期したり、イベントをトリガーする顧客のデータを同期したりできます（ODP が顧客のメール開封を登録した場合など）。
   - **セグメントに一致する顧客:** 必要なセグメントを選択し、**Next** を選択します。<br><br>![Optimizelyのセグメント選択画面]({% image_buster /assets/img/optimizely/image6_segment.png %})
   - **イベントをトリガーする顧客:** **Filter** ドロップダウンリストを展開し、Brazeへのこのデータ同期のトリガーとして使用する ODP イベントを選択します。次に、**Automation Rules** を展開し、必要に応じて調整します。<br><br>![Optimizely トリガーイベント設定画面]({% image_buster /assets/img/optimizely/image7_trigger.png %})
5. **Touchpoints** を展開し、**Touchpoint 1** の編集を選択して、**Braze** を選択します。
6. **Targeting** セクションを展開し、**Target Identifier** を選択します。
7. **Configure** セクションで、**Add Users To** に次のオプションのいずれかを選択します。
    - **キャンペーン:** Brazeで特定のキャンペーンに顧客を追加します。このオプションを選択した後、Braze キャンペーンを選択する必要があります。
    - **キャンバス:** Brazeで特定のキャンバスに顧客を追加します。このオプションを選択した後、Braze キャンバスを選択する必要があります。
    - **Profile Update Only:** Brazeの顧客プロファイルのみを更新します。
8. （オプション）Brazeに同期する**追加フィールド数**を選択します（最大20）。
    次に、追加フィールドのドロップダウンリストと入力フィールドごとに、以下を選択します。
    - 各 **Field #** ドロップダウンリストで、入力する Braze フィールドを選択します。
    - 対応する **Field # Value** ごとに、選択した Braze フィールドに送信する ODP フィールドを入力します。たとえば、**Field #** ドロップダウンリストで **Company Name** を選択した場合は、対応する **Field # Value** に `{{customer.company_name}}` と入力します。
9. **Save** を選択し、パンくずリストのアクティベーション名を選択します。
10. 登録に **Customers that match a segment** を選択した場合は、**Touchpoints** セクションで **Select start time and schedule** を選択します。
11. 次の設定を行います。
    - **Recurring or Continuous:** **Recurring** を選択します。
    - **Start Date:** データを Braze に送信する日付を入力します。
    - **End:** デフォルトは **Never** です。特定の日付に Braze データの同期を終了する場合は、ここで設定します。
    - **Repeats:** **Daily** に設定します。
    - **Repeat Every:** **1 day** に設定します。
    - **Timing:** データを Braze に送信する時刻を入力します。
    - **Time Zone:** このデータを送信するタイムゾーンを選択します。
12. **Apply**、**Save**、**Go Live** を選択します。同期は、指定した開始日時（またはトリガーイベントの発生時）に開始されます。

## トラブルシューティング {#troubleshooting}

### イベントの検査 {#inspect-events}

データが ODP から Braze に正しく同期されていることを確認するために、ODP でイベントを検査できます。

1. ODP で、**Account Settings** > **Event Inspector** に移動します。
2. **Start Inspector** を選択します。
3. インスペクターでデータが利用可能な場合、**Refresh** の横に数字が表示されます。選択するとデータを表示できます。
4. ODP と Braze が相互に送信する生データが表示されます。**View Details** を選択すると、その生データのフォーマットされたバージョンが表示されます。
5. Braze から ODP に返されるデータフィールドは、`_braze` で始まります。

### アクティビティログの確認 {#check-activity-logs}

各データ同期は、[ODP アクティビティログ](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/4407268804365-Use-the-Activity-Log&sa=D&source=editors&ust=1733948158385124&usg=AOvVaw2tMOxzcTKfL0-oYLT4IMpP)にも記録されます。

1. **Account Settings** > **Activity Log** に移動します。
2. **braze** でカテゴリをフィルタリングします。
3. **View Details** を選択すると、一致数を含むログの詳細がフォーマットされた形式で表示されます。