---
nav_title: Census
article_title: Census のコホートインポート
description: "このリファレンス記事では、クラウドウェアハウスのデータを使用してターゲットユーザーセグメントをダイナミックに作成できるデータ統合プラットフォームである Census のコホートインポート機能について説明します。"
page_type: partner
search_tag: Partner

---

# Census のコホートインポート {#census-cohort-import}

> この記事では、ユーザーコホートを [Census](https://www.getcensus.com/) から Braze にインポートする方法について説明します。Census の連携に関する詳細については、[Census のメイン記事]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/census)を参照してください。

## コホートインポート連携 {#cohort-import-integration}

### ステップ1: Braze サービス接続を作成する {#step-1-create-braze-service-connection}

Census プラットフォームで Census を連携するには、**Connections** タブに移動し、**New Destination** を選択して新しい Braze サービス接続を作成します。

表示されるプロンプトで、この接続に名前を付け、Braze エンドポイントURL、Braze REST APIキー、およびデータインポートキーを入力します。データインポートキーはコホートを同期するために必要であり、Braze で**パートナー連携** > **テクノロジーパートナー** > **Census** に移動すると確認できます。

![Braze コホートインポートの認証情報が設定された Census の新しい送信先ダイアログ。]({% image_buster /assets/img/census/add_service.png %}){: style="max-width:60%;"}

### ステップ2: Census の同期を作成する {#step-2-create-a-census-sync}

顧客を Braze に同期するには、同期を作成する必要があります。ここでは、データの同期先と、2つのプラットフォーム間でフィールドをどのようにマッピングするかを定義します。

1. **Syncs** タブに移動し、**New Sync** を選択します。<br><br>
2. コンポーザーで、データウェアハウスからソースデータモデルを選択します。<br><br>
3. モデルの同期先を設定します。送信先として **Braze** を選択し、同期するオブジェクトとして **User & Cohort** を選択します。<br>![「Select a Destination」プロンプトで接続として「Braze」が選択されており、さまざまなオブジェクトが一覧表示されている。]({% image_buster /assets/img/census/census_2.png %}){: style="max-width:80%;"}<br><br>
4. コホートに追加するユーザーを識別する**ソース列**を選択し、**識別子タイプ**として **External User ID** を選択します。<br><br>
5. **Cohort Name** ドロップダウンでコホートを選択するか、コホートを作成するか、またはソース列を選択してコホート名を入力します。<br><br>
6. **When a record is removed from source data** ドロップダウンを使用して、ソースデータセットからユーザーが削除されたときの動作を選択します。たとえば、**Do nothing** や **Remove matching record from cohort** などです。<br><br>
7. 最後に、Census のデータフィールドを対応する Braze フィールドにマッピングします。<br>![Census でのマッピング]({% image_buster /assets/img/census/census_3.png %}){: style="max-width:80%;"}<br><br>
8. 詳細を確認して同期を作成します。

これで同期を実行できます。

同期中にマッピングしたフィールドは、まずユーザーオブジェクトに同期され、Braze に既に存在するデータが更新されます。その後、更新されたユーザーが指定されたコホートに追加されます。

同期後、Census コホートフィルターを使用して Braze セグメントを作成し、今後の Braze キャンペーンやキャンバスに追加してそれらのユーザーをターゲットにできます。

{% alert note %}
Census と Braze の連携を使用する場合、Census は同期のたびに差分（変更データ）のみを Braze に送信します。
{% endalert %}

{% alert important %}
Braze 内に既に存在するユーザーのみがコホートに追加または削除されます。コホートインポートでは Braze に新しいユーザーは作成されません。
{% endalert %}

## ユーザーマッチング {#user-matching}

識別済みユーザーは、`external_id` または `alias` のいずれかで照合できます。匿名ユーザーは `device_id` で照合できます。元々匿名ユーザーとして作成された識別済みユーザーは `device_id` では識別できず、`external_id` または `alias` で識別する必要があります。