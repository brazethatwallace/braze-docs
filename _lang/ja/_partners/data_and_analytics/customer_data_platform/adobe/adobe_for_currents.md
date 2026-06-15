---
nav_title: Currentsの Adobe
article_title: Currentsの Adobe
alias: /partners/adobe_for_currents/
description: "このリファレンス記事では、Braze Currentsと Adobe のパートナーシップについて説明します。Adobe は顧客データプラットフォームであり、ブランドはリアルタイムで Adobe データ（カスタム属性とセグメント）をBrazeに接続してマッピングできます。"
page_type: partner
tool: Currents
search_tag: Partner
---

# Currentsの Adobe {#adobe-for-currents}

> [Adobe](https://www.adobe.com/) は、ブランドが自身の Adobe データ（カスタム属性とセグメント）をリアルタイムでBrazeに接続してマッピングできる顧客データプラットフォームです。

BrazeとAdobe の統合により、2つのシステム間の情報の流れをシームレスにコントロールできます。[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)を使用すると、データをAdobe に接続し、グローススタック全体で実用的なデータにすることもできます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Currents | Adobe にデータを再度エクスポートするには、アカウントに [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) を設定する必要があります。 |
| Adobe Experience Platform アカウント | このパートナーシップを活用するには、[Adobe Experience Platform アカウント](https://experience.adobe.com/#/platform/home)が必要です。 |
| コネクタの作成権限 | この統合を使用するには、ストリーミングソース接続を作成する権限が必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

### ステップ 1:Adobe で XDM スキーマを作成する {#step-1-create-an-xdm-schema-in-adobe}

1. Adobe Experience Platform で、**Schemas** > **Create schema** > **Experience Event** > **Next** の順に選択します。<br><br>![「Braze Currents Walk-Through」というスキーマの Adobe Schemas ページ。]({% image_buster /assets/img/adobe/currents_sources.png %})<br><br>
2. スキーマの名前と説明を入力します。
3. **Composition** パネルで、スキーマ属性を設定します。
- **Field groups** で、**Add** を選択し、**Braze Currents User Event** フィールドグループを追加します。
- **Save** を選択します。

スキーマの詳細については、[スキーマの作成](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/create-schema-ui)に関する Adobe のドキュメントを参照してください。

### ステップ 2:Brazeを Adobe Experience Platform に接続する {#step-2-connect-braze-to-the-adobe-experience-platform}

1. Adobe Experience Platform で、**Sources** > **Catalog** > **Marketing automation** に移動します。
2. Braze Currentsの **Add data** を選択します。
3. [Braze Currents サンプルファイル](https://github.com/Appboy/currents-examples/blob/master/sample-data/Adobe/adobe_examples.json)をアップロードします。<br><br>![Adobe の「データの追加」ページ。]({% image_buster /assets/img/adobe/currents_add_data.png %})<br><br>
4. ファイルがアップロードされたら、データセットとマッピング先のスキーマに関する情報など、データフローの詳細を指定します。
    - Braze Currents ソースを初めて接続する場合は、新しいデータセットを作成し、[ステップ 1](#step-1-create-an-xdm-schema-in-adobe) で作成したスキーマを使用するようにします。
    - 初めてでない場合は、Braze スキーマを参照する既存のデータセットを使用します。
5. データのマッピングを設定し、問題を解決します。
    - スキーマのルートレベルで、`id` のマッピングを `to _braze.appID` から `_id` に変更します。
    - `properties.is_amp` が `_braze.messaging.email.isAMP` にマッピングされていることを確認します。
    - `time` と `timestamp` のマッピングを削除し、追加アイコン > **Add calculated field** を選択して、**time * 1000** と入力します。**Save** を選択します。
    - 新しいソースフィールドの横にある **Map target field** を選択し、スキーマのルートレベルの **timestamp** にマッピングします。<br><br>![マッピングを含む Adobe の「データの追加」ページ。]({% image_buster /assets/img/adobe/currents_mapping.png %})<br><br>
6. **Validate** を選択して、問題が解決されたことを確認します。

{% alert important %}
Brazeのタイムスタンプは秒単位で表されます。Adobe Experience Platform でタイムスタンプを正確に反映するには、計算フィールドがミリ秒単位である必要があります。秒をミリ秒に変換するには、**time * 1000** の計算を使用します。
{% endalert %}

{: start="7"}
7. **Next** を選択し、データフローの詳細を確認してから、**Finish** を選択します。<br><br>![マッピングエラーのない Adobe の「データの追加」ページ。]({% image_buster /assets/img/adobe/currents_no_errors.png %})

### ステップ 3:認証情報を収集する {#step-3-gather-credentials}

次の認証情報を収集してBrazeに入力すると、BrazeがAdobe Experience Platform にデータを送信できるようになります。

| フィールド         | 説明                          |
|---------------|-------------------------------------|
| Client ID     | Adobe Experience Platform ソースに関連付けられたクライアント ID。 |
| Client Secret | Adobe Experience Platform ソースに関連付けられたクライアントシークレット。 |
| Tenant ID     | Adobe Experience Platform ソースに関連付けられたテナント ID。 |
| Sandbox Name  | Adobe Experience Platform ソースに関連付けられたサンドボックス。   |
| Dataflow ID   | Adobe Experience Platform ソースに関連付けられたデータフロー ID。   |
| Streaming Endpoint  | Adobe Experience Platform ソースに関連付けられたストリーミングエンドポイント。Brazeはこれを自動的にバッチストリーミングエンドポイントに変換します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3: Gather credentials" }

### ステップ 4:データソースにデータをストリーミングするようCurrentsを設定する {#step-4-configure-currents-to-stream-data-to-your-data-source}

1. Brazeで、**パートナー連携** > **データのエクスポート** に移動し、**Create New Current** を選択します。
2. 次の情報を入力します。
    - コネクタの名前
    - コネクタに関する通知の連絡先情報
    - [ステップ 3](#step-3-gather-credentials) の認証情報
3. 受信するイベントを選択します。
4. 必要に応じて、フィールドの除外または変換を設定します。
5. **Launch Current** を選択します。