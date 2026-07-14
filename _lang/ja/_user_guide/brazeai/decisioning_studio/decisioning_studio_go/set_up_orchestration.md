---
nav_title: オーケストレーションを設定する
article_title: オーケストレーションを設定する
page_order: 2
description: "BrazeAI Decisioning Studio Goをカスタマーエンゲージメントプラットフォームに接続して、パーソナライズされたコミュニケーションを実現する方法を説明します。"
toc_headers: h2
---

# オーケストレーションを設定する {#set-up-orchestration}

> BrazeAI Decisioning Studio™ Goは、パーソナライズされたコミュニケーションをオーケストレーションするために、カスタマーエンゲージメントプラットフォーム（CEP）に接続する必要があります。この記事では、サポートされている各CEPの統合設定方法を説明します。

## サポートされているCEP {#supported-ceps}

Decisioning Studio Goは、以下のカスタマーエンゲージメントプラットフォームをサポートしています。

| CEP | 統合タイプ | 主要な機能 |
|-----|-----------------|--------------|
| **Braze** | APIトリガーキャンペーン | ネイティブ統合、リアルタイムトリガー |
| **Salesforce Marketing Cloud** | APIイベント付きJourney Builder | SQLクエリのオートメーション、データエクステンション |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="サポートされているCEP" }

以下からCEPを選択して、統合設定を開始しましょう。

{% tabs %}
{% tab Braze %}

## Braze統合を設定する {#set-up-braze-integration}

Decisioning Studio GoをBrazeと統合するには、APIキーを作成し、APIトリガーキャンペーンを設定し、必要な識別子をDecisioning Studio Goポータルに提供します。

### ステップ1: REST APIキーを作成する {#step-1-create-a-rest-api-key}

1. Brazeダッシュボードで、**設定** > **APIと識別子** > **APIキー**に移動します。
2. **APIキーを作成**を選択します。
3. APIキーの名前を入力します。例：「DecisioningStudioGoEmail」
4. 以下のカテゴリに基づいて権限を選択します。
    - **ユーザーデータ：** `users.track`、`users.delete`、`users.export.ids`、`users.export.segment`を選択
    - **メッセージ：** `messages.send`、`messages.schedule.create`、`messages.schedule.update`、`messages.schedule.delete`を選択
    - **キャンペーン：** リストされているすべての権限を選択
    - **キャンバス：** リストされているすべての権限を選択
    - **セグメント：** リストされているすべての権限を選択
    - **テンプレート：** リストされているすべての権限を選択

{: start="5"}
5. **APIキーを作成**を選択します。
6. APIキーをコピーし、BrazeAI Decisioning Studio™ Goポータルに貼り付けます。

### ステップ2: メールの表示名を確認する {#step-2-locate-your-email-display-name}

1. Brazeダッシュボードで、**設定** > **メール設定**に移動します。
2. BrazeAI Decisioning Studio™ Goで使用する表示名を確認します。
3. **差出人の表示名**をコピーし、BrazeAI Decisioning Studio™ Goポータルに**メール表示名**として貼り付けます。
4. 関連するメールアドレスをコピーし、BrazeAI Decisioning Studio™ Goポータルに**送信元メールアドレス**として貼り付けます。このメールアドレスはローカル部分とドメインを組み合わせたものです。

### ステップ3: BrazeのURLとApp IDを見つける {#step-3-find-your-braze-url-and-app-id}

**BrazeのURLを見つけるには：**
1. Brazeダッシュボードに移動します。
2. ブラウザウィンドウで、BrazeのURLは`https://`で始まり`braze.com`で終わります。BrazeのURLの例：`https://dashboard-01.braze.com`

**App ID（APIキー）を見つけるには：**

{% alert note %}
BrazeはアプリID（BrazeダッシュボードではAPIキーと呼ばれます）を提供しており、トラッキング目的で使用できます。例えば、ワークスペース内の特定のアプリにアクティビティを関連付けることができます。アプリIDを使用する場合、BrazeAI Decisioning Studio™ Goは各実験担当者にアプリIDを関連付けることをサポートします。<br><br>アプリIDを使用しない場合は、プレースホルダーとして任意の文字列を入力できます。
{% endalert %}

1. Brazeダッシュボードで、**設定** > **アプリ設定**に移動します。
2. トラッキングしたいアプリに移動します。
3. **APIキー**をコピーし、BrazeAI Decisioning Studio™ Goポータルに貼り付けます。

### ステップ4: APIトリガーキャンペーンを作成する {#step-4-create-an-api-triggered-campaign}

1. Brazeダッシュボードで、**メッセージング** > **キャンペーン**に移動します。
2. **キャンペーンを作成**を選択します。
3. キャンペーンタイプとして、**APIキャンペーン**を選択します。
4. キャンペーン名を入力します。例：「Decisioning Studio Go Email」

![「Decisioning Studio Go Email」という名前のAPIキャンペーン。]({% image_buster /assets/img/decisioning_studio_go/api_campaign_name.png %})

{: start="5"}
5. メッセージングチャネルとして、**メール**を選択します。

![APIキャンペーンのメッセージングチャネルを選択するオプション。]({% image_buster /assets/img/decisioning_studio_go/select_api_campaign.png %})

{: start="6"}
6. **追加オプション**で、**ユーザーがキャンペーンを再度受信できるようにする**チェックボックスを選択します。
7. 再受信資格までの時間として、**1**を入力し、ドロップダウンから**時間**を選択します。

![APIキャンペーンの再受信資格設定が選択された状態。]({% image_buster /assets/img/decisioning_studio_go/additional_options.png %})

{: start="8"}
8. **キャンペーンを保存**を選択します。

### ステップ5: キャンペーンIDとメッセージIDをコピーする {#step-5-copy-your-campaign-and-message-ids}

1. APIキャンペーンで、**キャンペーンID**をコピーします。次に、BrazeAI Decisioning Studio™ Goポータルに移動し、**キャンペーンID**を貼り付けます。

![コピーして貼り付けるメッセージバリエーションIDの例。]({% image_buster /assets/img/decisioning_studio_go/campaign_id.png %})

{: start="2"}
2. **メッセージバリエーションID**をコピーします。次に、BrazeAI Decisioning Studio™ Goポータルに移動し、**メッセージバリエーションID**を貼り付けます。

### ステップ6: テストユーザーIDを確認する {#step-6-locate-a-test-user-id}

統合をテストするには、ユーザーIDが必要です。

ワークスペースで[識別子フィールドレベル暗号化]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption)を使用している場合、`/users/track`エンドポイントで作成する新しいテストユーザーは、暗号化されたワークスペースのメール要件に従う必要があります。`email`フィールドには、小文字に変換したメール値のBase64エンコードされたHMAC-SHA256ハッシュを送信し、`email_encrypted`には設定済みのPII暗号化キーで生成された暗号化メール値を送信してください。

1. Brazeダッシュボードで、**オーディエンス** > **ユーザーを検索**に移動します。
2. 外部ユーザーID、ユーザーエイリアス、メール、電話番号、またはプッシュトークンでユーザーを検索します。
3. 設定で参照するためにユーザーIDをコピーします。

![ユーザーIDでユーザーを検索した際のユーザープロファイルの例。]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## SFMC統合を設定する {#set-up-sfmc-integration}

Decisioning Studio GoをSalesforce Marketing Cloudと統合するには、アプリパッケージを設定し、データクエリオートメーションを作成し、トリガー送信を処理するJourneyを構築します。

### パート1: SFMCアプリパッケージを設定する {#part-1-set-up-an-sfmc-app-package}

1. Marketing Cloudのホームページに移動します。
2. グローバルヘッダーのメニューを開き、**Setup**を選択します。
3. サイドパネルナビゲーションの**Platform Tools**にある**Apps**に移動し、**Installed Packages**を選択します。
4. **New**を選択してアプリパッケージを作成します。
5. アプリパッケージに名前と説明を付けます。

![「Experimenter 1 - Test 5」という名前のアプリパッケージ。]({% image_buster /assets/img/decisioning_studio_go/sfmc_app_package1.png %})

{: start="6"}
6. **Add Component**を選択します。
7. **Component Type**で、**API Integration**を選択します。次に、**Next**を選択します。
8. **Integration Type**で、**Server-to-server**を選択します。次に、**Next**を選択します。
9. アプリパッケージに対してのみ、以下の推奨スコープを選択します。
    - Channels > Email > Read, Write, Send
    - Channels > OTT > Read
    - Channels > Push > Read
    - Channels > SMS > Read
    - Channels > Social > Read
    - Channels > Web > Read
    - Assets > Documents and Images > Read, Write
    - Assets > Saved Content > Read, Write
    - Automation > Automations > Read, Write, Execute
    - Automation > Journeys > Read, Write, Execute, Activate/Stop/Pause/Send/Schedule
    - Contacts > Audiences > Read
    - Contacts > List and Subscribers > Read, Write
    - Cross Cloud Platform > Market Audience > View
    - Cross Cloud Platform > Market Audience Member > View
    - Cross Cloud Platform > Marketing Cloud Connect > Read
    - Data > Data Extensions > Read, Write
    - Data > File Locations > Read
    - Data > Tracking Events > Read, Write
    - Event notifications > Callbacks > Read
    - Event notifications > Subscriptions > Read

{% details 推奨スコープの画像を表示 %}

![Salesforce Marketing Cloudアプリパッケージの推奨スコープ。]({% image_buster /assets/img/decisioning_studio_go/app_package_scopes.png %})

{% enddetails %}

{: start="10"}
10. **Save**を選択します。
11. 以下のフィールドをコピーし、BrazeAI Decisioning Studio™ Goポータルに貼り付けます：**Client Id**、**Client Secret**、**Authentication Base URI**、**REST Base URI**、**SOAP Base URI**。

### パート2: データクエリオートメーションを設定する {#part-2-set-up-a-data-query-automation}

#### ステップ1: 新しいオートメーションを作成する {#step-1-create-a-new-automation}

1. Salesforce Marketing Cloudのホームから、**Journey Builder**に移動し、**Automation Studio**を選択します。

![Journey Builderナビゲーションにあるオートメーションスタジオのオプション。]({% image_buster /assets/img/decisioning_studio_go/query13.png %})

{: start="2"}
2. **New Automation**を選択します。
3. **Schedule**ノードをドラッグ＆ドロップして**Starting Source**とします。

![「Schedule」をJourneyの開始ソースとする。]({% image_buster /assets/img/decisioning_studio_go/query14.png %})

{: start="4"}
4. **Schedule**ノードで、**Configure**を選択します。
5. スケジュールに以下を設定します。
    - **Start Date：** 翌日の日付
    - **Time：** **12:00 AM**
    - **Time Zone：** **(GMT-05:00) Eastern (US & Canada)**
6. **Repeat**で、**Daily**を選択します。
7. このスケジュールを終了しないように設定します。
8. **Done**を選択してスケジュールを保存します。

![2024年1月25日午前0時（米国東部時間）に定義されたスケジュール例。毎日繰り返されます。]({% image_buster /assets/img/decisioning_studio_go/query12.png %})

#### ステップ2: SQLクエリを作成する {#step-2-create-your-sql-queries}

次に、2つのSQLクエリを作成します。サブスクライバークエリとエンゲージメントクエリです。これらのクエリにより、BrazeAI Decisioning Studio™ Goはオーディエンスを構成するデータの取得とエンゲージメントイベントの取り込みが可能になります。

**サブスクライバークエリ：**

1. **SQL Query**をキャンバスにドラッグ＆ドロップします。
2. **Choose**を選択します。
3. **Create New Query Activity**を選択します。
4. クエリに名前と外部キーを付けます。BrazeAI Decisioning Studio™ Goポータルで提供されているサブスクライバークエリ用の推奨名と外部キーを使用することをお勧めします。

![「OFE_Subscribers_query_Test5」と外部キーの例。]({% image_buster /assets/img/decisioning_studio_go/query11.png %})

{: start="5"}
5. **Next**を選択します。
6. BrazeAI Decisioning Studio™ Goポータルで、**Subscriber Query Resources**の下にあるシステムデータSQLクエリを確認します。
7. クエリをテキストボックスにコピーして貼り付け、**Next**を選択します。

![SQL Queryセクションのクエリ例。]({% image_buster /assets/img/decisioning_studio_go/query10.png %})

{: start="8"}
8. BrazeAI Decisioning Studio™ Goポータルの**Resources to use**セクションで、ターゲットデータエクステンションの外部キーを確認します。次に、検索バーに貼り付けて検索します。

![検索バーに貼り付けられた外部キー]({% image_buster /assets/img/decisioning_studio_go/query9.png %})

{: start="9"}
9. 検索した外部キーに一致するデータエクステンションを選択します。ターゲットデータエクステンション名は、BrazeAI Decisioning Studio™ Goポータルでも参照用に提供されています。サブスクライバークエリの**Data Extension**は、`BASE_AUDIENCE_DATA`サフィックスで終わるはずです。

![外部キーの例に一致するデータエクステンション名。]({% image_buster /assets/img/decisioning_studio_go/query8.png %})

{: start="10"}
10. **Overwrite**を選択し、次に**Next**を選択します。

**エンゲージメントクエリ：**

1. **SQL Query**をキャンバスにドラッグ＆ドロップします。

![「SQL Query」がJourneyのアクティビティとして追加された状態。]({% image_buster /assets/img/decisioning_studio_go/query7.png %})

{: start="2"}
2. **Choose**を選択します。
3. **Create New Query Activity**を選択します。
4. クエリに名前と外部キーを付けます。BrazeAI Decisioning Studio™ Goポータルで提供されているエンゲージメントクエリ用の推奨名と外部キーを使用することをお勧めします。

![「OFE_Engagement_query」と外部キーの例。]({% image_buster /assets/img/decisioning_studio_go/query6.png %})

{: start="5"}
5. **Next**を選択します。
6. BrazeAI Decisioning Studio™ Goポータルで、**Engagement Query Resources**の下にあるシステムデータSQLクエリを確認します。
7. クエリをテキストボックスにコピーして貼り付け、**Next**を選択します。

![SQL Queryセクションのクエリ例。]({% image_buster /assets/img/decisioning_studio_go/query5.png %})

{: start="8"}
8. BrazeAI Decisioning Studio™ Goポータルで指定されたエンゲージメントクエリのターゲットデータエクステンションを確認し、選択します。

{% alert tip %}
ターゲットデータエクステンション名は、BrazeAI Decisioning Studio™ Goポータルでも参照用に提供されています。エンゲージメントクエリのターゲットデータエクステンションを確認していることを確認してください。エンゲージメントクエリの**Data Extension**は、ENGAGEMENT_DATAサフィックスで終わるはずです。
{% endalert %}

{: start="9"}
9. **Overwrite**を選択し、次に**Next**を選択します。

![外部キーの例に一致するデータエクステンション名。]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

#### ステップ3: オートメーションを実行する {#step-3-run-the-automation}

1. オートメーションに名前を付け、**Save**を選択します。

![オートメーションの例「OFE_Experimenter_Test5_Automation」。]({% image_buster /assets/img/decisioning_studio_go/query3.png %})

{: start="2"}
2. 次に、**Run Once**を選択して、すべてが期待通りに動作していることを確認します。
3. 両方のクエリを選択し、**Run**を選択します。

![実行するSQLクエリアクティビティの選択リストを持つ「OFE_Experimenter_Test5_Automation」オートメーション。]({% image_buster /assets/img/decisioning_studio_go/query2.png %})

{: start="4"}
4. **Run Now**を選択します。

![選択されたSQLクエリアクティビティ。]({% image_buster /assets/img/decisioning_studio_go/query1.png %})

これで、オートメーションが正常に動作しているか確認できます。オートメーションが期待通りに動作しない場合は、Brazeサポートに連絡して追加の支援を受けてください。

### パート3: SFMC Journeyを作成する {#part-3-create-your-sfmc-journey}

#### ステップ1: Journeyを設定する {#step-1-set-up-the-journey}

1. Salesforce Marketing Cloudで、**Journey Builder** > **Journey Builder**に移動します。
2. **Create New Journey**を選択します。
3. Journeyタイプとして**Multi-Step Journey**を選択し、**Create**を選択します。

![API Eventエントリソースが条件分岐ノードと複数のメールノードに接続されている。]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

#### ステップ2: Journeyを構築する {#step-2-build-the-journey}

**エントリソースを作成する：**

1. エントリソースとして、**API Event**をJourney Builderにドラッグします。

![「API Event」がエントリソースとして選択された状態。]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

{: start="2"}
2. **API Event**で、**Create an event**を選択します。

![API Eventの「create an event」オプション。]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3. **Select Data Extension**を選択します。BrazeAI Decisioning Studio™ Goがレコメンデーションを書き込むデータエクステンションを確認し、選択します。
4. **Summary**を選択して変更を保存します。
5. **Done**を選択してAPIイベントを保存します。

![APIイベントのサマリー。]({% image_buster /assets/img/decisioning_studio_go/journey4.png %}){: style="max-width:80%;"}

**条件分岐を追加する：**

1. **API Entry Event**の後に**Decision Split**をドラッグ＆ドロップします。
2. **Decision Split**の詳細で、最初のパスの**Edit**を選択します。

![「Edit」ボタンがあるDecision Splitの詳細。]({% image_buster /assets/img/decisioning_studio_go/journey5.png %})

{: start="3"}
3. レコメンデーションデータエクステンションから渡されるテンプレートIDを使用するように**Decision Split**を更新します。**Journey Data**の下にある適切なフィールドを確認します。

![Decision Splitのパス1にあるJourney Dataセクション。]({% image_buster /assets/img/decisioning_studio_go/journey6.png %})

{: start="4"}
4. エントリイベントを選択し、目的のテンプレートIDフィールドを確認して、ワークスペースにドラッグします。

![含めるメールテンプレートID。]({% image_buster /assets/img/decisioning_studio_go/journey7.png %})

{: start="5"}
5. 最初のメールテンプレートのテンプレートIDを入力し、**Done**を選択します。
6. **Summary**を選択してこのパスを保存します。
7. 各メールテンプレートにパスを追加し、上記のステップ4〜6を繰り返してフィルター条件を設定します。テンプレートIDが各テンプレートのID値と一致するようにしてください。
8. **Done**を選択して**Decision Split**ノードを保存します。

![各メールテンプレートIDに対応するDecision Splitの2つのパス。]({% image_buster /assets/img/decisioning_studio_go/journey10.png %}){: style="max-width:65%;"}

**各Decision Splitにメールを追加する：**

1. **Decision Split**の各パスに**Email**ノードをドラッグします。
2. **Email**を選択し、各パスに適用すべき適切なテンプレートを選択します（つまり、ID値を持つテンプレートがDecision Splitのロジックと一致する必要があります）。

![Journeyに追加されたメールノード。]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

#### ステップ3: Journeyを有効化する {#step-3-activate-the-journey}

Journeyを設定したら、有効化して以下の詳細をBrazeAI Decisioning Studio™ Goチームと共有します。

* Journey ID
* Journey名
* APIイベント定義キー
* レコメンデーションデータエクステンション外部キー

{% alert note %}
BrazeAI Decisioning Studio™ Goポータルには、サブスクライバーとエンゲージメントデータを1日1回エクスポートするためにプロビジョニングされたSFMCオートメーションが表示されます。このオートメーションをSFMCで開く場合は、必ず一時停止を解除してライブ状態に戻してください。
{% endalert %}

1. BrazeAI Decisioning Studio™ Goポータルで、**Journey名**をコピーします。
2. 次に、Salesforce Marketing Cloud Journey Builderで、Journey名を検索バーに貼り付けます。
3. Journey名を選択します。なお、Journeyは現在下書きステータスです。
4. **Validate**を選択します。

![有効化する完成したJourney。]({% image_buster /assets/img/decisioning_studio_go/activate3.png %})

{: start="5"}
5. 検証結果を確認し、**Activate**を選択します。

![Validation Rulesセクションに記載されたレコメンデーション。]({% image_buster /assets/img/decisioning_studio_go/activate1.png %}){: style="max-width:60%;"}

{: start="6"}
6. **Activate Journey**のサマリーで、もう一度**Activate**を選択します。

![Journeyのサマリー。]({% image_buster /assets/img/decisioning_studio_go/activate2.png %}){: style="max-width:85%;"}

これで設定は完了です。BrazeAI Decisioning Studio™ Goを通じて送信をトリガーできるようになりました。

{% endtab %}
{% endtabs %}

## 次のステップ {#next-steps}

オーケストレーションの設定が完了したら、次にエージェントの設計に進みましょう。

- [エージェントを設計する]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/design_your_agent)