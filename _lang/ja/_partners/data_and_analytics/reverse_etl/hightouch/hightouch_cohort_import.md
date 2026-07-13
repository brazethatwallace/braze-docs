---
nav_title: Hightouch コホートインポート
article_title: Hightouch コホートインポート
description: "このリファレンス記事では、Hightouchのコホートインポート機能について説明します。Hightouchは、ウェアハウスの顧客データをビジネスツールに同期するプラットフォームです。"
page_type: partner
search_tag: Partner

---
# Hightouch コホートインポート {#hightouch-cohort-import}

> この記事では、[Hightouch](https://hightouch.io) からBrazeにユーザーコホートをインポートする方法について説明します。これにより、ウェアハウス内にのみ存在する可能性のあるデータに基づいてターゲットを絞ったキャンペーンを送信できます。Hightouchの連携やその他の機能の詳細については、メインの[Hightouchの記事]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/hightouch)を参照してください。

## データインポート連携 {#data-import-integration}

### ステップ1:Brazeデータインポートキーを取得する {#step-1-get-the-braze-data-import-key}
Brazeで、**パートナー連携** > **テクノロジーパートナー**に移動し、**Hightouch**を選択します。

ここで、RESTエンドポイントを確認し、Brazeデータインポートキーを生成します。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にできます。<br><br>![RESTエンドポイントとデータインポートキーのコントロールが表示されたBraze Hightouchテクノロジーパートナーページ。]({% image_buster /assets/img/hightouch/data_import_key.png %}){: style="max-width:90%;"}

### ステップ2:HightouchでBrazeコホートを宛先として追加する {#step-2-add-braze-cohorts-as-a-destination-in-hightouch}
Hightouchワークスペースの**Destination**ページに移動し、**Braze Cohorts**を検索して、**Continue**をクリックします。そこから、RESTエンドポイントとデータインポートキーを入力し、**Continue**をクリックします。<br><br>![認証情報フィールドが表示されたHightouch Braze Cohorts宛先設定画面。]({% image_buster /assets/img/hightouch/cohort1.png %}){: style="max-width:90%;"}

### ステップ3:モデル（またはオーディエンス）をBrazeコホートに同期する {#step-3-sync-a-model-or-audience-into-braze-cohorts}
Hightouchで、作成した[モデル](https://hightouch.io/docs/getting-started/create-your-first-sync/#create-a-model)または[オーディエンス](https://hightouch.io/docs/audiences/usage/)を使用して、新しい同期を作成します。次に、前のステップで作成したBrazeコホート宛先を選択します。最後に、Brazeコホート宛先設定で、照合する識別子を選択し、Hightouchで新しいBrazeコホートを作成するか、既存のコホートを更新するかを決定します。<br><br>![マッチ識別子とコホートオプションが表示されたHightouch Brazeコホート同期設定画面。]({% image_buster /assets/img/hightouch/cohort2.png %}){: style="max-width:90%;"}

{% alert important %}
Braze内に既に存在するユーザーのみがコホートに追加または削除されます。コホートインポートではBrazeに新しいユーザーは作成されません。
{% endalert %}

### ステップ4:HightouchカスタムオーディエンスからBrazeセグメントを作成する {#step-4-create-a-braze-segment-from-the-hightouch-custom-audience}
Brazeで**セグメント**に移動し、新しいセグメントを作成して、フィルターとして**Hightouch Cohorts**を選択します。ここから、含めたいHightouchコホートを選択できます。Hightouchコホートセグメントを作成したら、キャンペーンまたはキャンバスを作成するときにオーディエンスフィルターとして選択できます。<br><br>![Hightouch Cohortsフィルターを使用したBrazeセグメントビルダー。]({% image_buster /assets/img/hightouch/cohort3.png %}){: style="max-width:90%;"}

### この連携を使用する {#using-this-integration}
Hightouchセグメントを使用するには、Brazeキャンペーンまたはキャンバスを作成し、ターゲットオーディエンスとしてセグメントを選択します。<br><br>![Hightouchベースのセグメントが選択されたBrazeオーディエンスターゲティングステップ。]({% image_buster /assets/img/hightouch/cohort4.png %}){: style="max-width:90%;"}

## ユーザーマッチング {#user-matching}

識別済みユーザーは、`external_id`または`alias`のいずれかで照合できます。匿名ユーザーは`device_id`で照合できます。もともと匿名ユーザーとして作成された識別済みユーザーは、`device_id`では識別できず、`external_id`または`alias`で識別する必要があります。