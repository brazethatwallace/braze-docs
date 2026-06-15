---
nav_title: Grouparoo
page_order: 1
description: "この記事では、BrazeとGrouparooのパートナーシップについて説明します。Grouparooは、データウェアハウスのデータを活用してマーケティング、セールス、サポートツールを強化するために使用されるオープンソースのリバースETLツールです。"
page_type: update

---

# Grouparoo

{% alert update %}
Grouparooのサポートは、2022年4月に終了しました。
{% endalert %}

> [Grouparoo](https://www.grouparoo.com/)は、データウェアハウスからマーケティング、セールス、サポートツールにデータを同期するオープンソースのリバースETLツールです。モデル中心のUIにより、技術者でないチームメンバーでもデータ同期の設定やスケジュールを行うことができます。

BrazeとGrouparooの統合により、データウェアハウスのデータをBrazeに同期できます。自動同期スケジュールにより、顧客とのコミュニケーションは常に最新の情報に基づいて行われます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Grouparooのアカウントとプロジェクト | このパートナーシップを利用するには、Grouparooのアカウントとプロジェクトが必要です。<br><br>この統合は、Grouparooが提供する無料のコミュニティエディションおよびエンタープライズソリューションで使用できます。セットアップはGrouparooの設定ユーザーインターフェイスで行います。 |
| Braze REST APIキー | ユーザーとトラックの権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL](https://www.grouparoo.com/)。エンドポイントは、お使いのインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

### ステップ 1:GrouparooでBrazeアプリを作成する {#step-1-create-a-braze-app-in-grouparoo}

Grouparooで、**Apps**に移動し、**Braze**を選択して新しいBrazeアプリを作成します。表示されたモーダルで、Braze APIキーとRESTエンドポイントを入力します。

![]({% image_buster /assets/img/grouparoo/add-app.png %})

### ステップ 2:モデルとデータソースをセットアップする {#step-2-set-up-a-model-and-data-source}

この統合では、次のステップに進む前に、既存のモデルとデータソースをセットアップしておく必要があります。この設定がない場合は、Grouparooのドキュメントにアクセスして、[モデル](https://www.grouparoo.com/docs/config/models)および[データソース](https://www.grouparoo.com/docs/config/sources)の設定方法を確認してください。

### ステップ 3:GrouparooでBrazeの送信先を作成する {#step-3-create-a-braze-destination-in-grouparoo}

#### 同期モードを選択する {#select-sync-mode}

Grouparooで、ナビゲーションバーからモデルを選択します。次に、**Destinations**セクションまでスクロールし、**Add new Destination**をクリックします。

次に、作成した**Braze**アプリを選択し、送信先に名前を付け、以下から希望の同期モードを選択します。
- **Sync**：必要に応じて会社ユーザーを追加、更新、削除します。このオプションでは、新しいレコード、既存レコードの変更、および削除を検索します。
- **Additive**：必要に応じて会社ユーザーを追加・更新しますが、誰も削除しません。このオプションは、Brazeに追加する新規ユーザーと既存の会社ユーザーの変更を検索しますが、削除は追跡しません。
- **Enrich**：Brazeにすでに存在するユーザーのみを更新します。ユーザーの追加や削除は行いません。このオプションは、Brazeの既存ユーザーのみを更新します。

#### プロパティフィールドのマッピング {#property-field-mapping}

次に、Grouparooのプロパティフィールドを Brazeのプロパティフィールドにマッピングする必要があります。

![プロパティマッピングフィールドの例。GrouparooのuserIDはexternal_idにマッピングされるよう設定されています。email、firstName、lastNameは、それぞれ対応する「email」、「first_name」、「last_name」のGrouparooフィールドに設定されています。]({% image_buster /assets/img/grouparoo/mapping.png %}){: style="max-width:80%;"}

Brazeの`external_id`フィールドがソーステーブルの主キーにマッピングされていることを確認してください。ユースケースの必要に応じて、残りのフィールドをマッピングします。

**Send Record Properties**セクション：データのマッピングに使用できるプリセットユーザープロファイルフィールドのリストです。これらのいずれもGrouparooプロパティから同期できます。

**Optional Braze User Profile Fields**セクション：オプションのカスタムBrazeユーザープロファイルフィールドを作成します。**Add New Braze User Profile Field**をクリックすると、Brazeにマッピングできるすべてのプロパティが表示されます。新しく作成するフィールドの名前はGrouparooプロパティと同じになりますが、名前を変更することもできます。

#### Grouparooグループ {#grouparoo-groups}

マッピングに加えて、Grouparooグループを Braze購読グループに追加することもできます。

![Grouparoo送信先設定ウィンドウの「Braze Subscription Groups」で、「High value with recent automotive purchase」Grouparooグループが「High value with recent automotive purchase」Brazeサブスクリプショングループに追加される画面。]({% image_buster /assets/img/grouparoo/lists.png %}){: style="max-width:80%;"}

{% alert important %}
この統合に関する詳細および更新は、[Grouparooのドキュメント](https://www.grouparoo.com/docs/integrations/grouparoo-braze)をご覧ください。
{% endalert %}