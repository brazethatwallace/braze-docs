---
nav_title: Octolis
article_title: Octolis
description: "このリファレンス記事では、BrazeとOctolisのパートナーシップについて説明します。Octolisはデータアクティベーションプラットフォームであり、データをBrazeに統合できます。"
alias: /partners/octolis/
page_type: partner
search_tag: Octolis

---

# Octolis

> [Octolis](http://octolis.com)は、強力なデータアクティベーションプラットフォーム（またはヘッドレス顧客データプラットフォーム）です。自分が所有するデータベースの上に位置し、ビジネスツールでデータを統合、準備、スコア化、同期するための簡単な方法を提供します。

_この統合はOctolisによって管理されています。_

## 統合について {#about-the-integration}

BrazeとOctolisの統合は、生データソースとBrazeの間のミドルウェアとして機能し、オンラインとオフラインのさまざまなソースからデータを取得して統合できます。
1. Eショップ、CRM、POSシステムなどのソースからデータを統合・結合します。
2. 正規化とスコア化を行います。
3. 計算されたフィールドとイベントをBrazeにリアルタイムで同期します。

![Octolisのデータソース、処理、およびBrazeへの同期フローを示すアーキテクチャ図。]({% image_buster /assets/img/Octolis/Braze_scheme.png %})

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Octolisアカウント | このパートナーシップを活用するには、Octolisアカウントが必要です。 |
| Braze REST APIキー | [**users.track**]({{site.baseurl}}/api/endpoints/user_data/post_user_track)権限を持つBraze REST APIキー。<br><br>これは、Brazeダッシュボードの**設定** > **APIキー**で作成できます。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints)。エンドポイントは、インスタンスのBraze URLに依存します。 |
| Brazeアプリキー | アプリ識別子キー。これは、**Brazeダッシュボード > 設定の管理 > APIキー**で確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

統合を開始する前に、接続、ソース、オーディエンス、および同期に関する以下のセクションを参照してください。

詳細については、Octolisの[Getting started](https://help.octolis.com/)セクションを参照してください。

### ステップ1:Octolisをデータソースに接続する {#step-1-connect-octolis-to-your-data-sources}

Brazeにデータを送信するには、少なくとも1つの[オーディエンス](https://help.octolis.com/audiences/create-a-no-code-audience)を作成しておく必要があります。オーディエンスは、複数のデータソースを結合し、準備ステップを適用し、計算されたフィールドを追加します。

これらのオーディエンスは、さまざまなデータソースに基づいて作成する必要があります。ソースとして次のいずれかを使用できます。
- Salesforceオブジェクト（取引先責任者、取引先など）
- Zendeskオブジェクト（チケット）
- SFTP内のファイル（一部の連絡先を含むCSVファイル、イベントを含むJSONファイルなど）
- データベースのテーブル/ビュー
- いずれかのシステムから、webhookやAPI呼び出しを通じてレコードが送信されます。

### ステップ2:Brazeを送信先として追加する {#step-2-add-braze-as-a-destination}

次に、Brazeを新しい送信先として設定するには、メイン画面の現在の送信先の上にある**+ Add more**を選択し、利用可能なビジネスツールから**Braze**を選択します。

![利用可能なビジネスツールからBrazeが選択されたOctolisの送信先選択画面。]({% image_buster /assets/img/Octolis/Braze_screen2.png %})

選択したら、以下を入力します。

- Braze APIキー：これは、Brazeダッシュボードの**設定** > **APIキー**で作成できます。
- 時間枠：Octolisは指定された期間にわたってレート制限を適用します。
- リクエスト量：この時間枠内に実行できるリクエストの数です。
- カスタム属性：ここで、Brazeに送信する新しいフィールド、その形式（文字列、整数、浮動小数点数）を指定し、いずれかを同期に必須にする場合は**Required for syncs**にチェックを入れます。

![APIキー、レート制限、カスタム属性のOctolis Braze送信先設定フィールド。]({% image_buster /assets/img/Octolis/Braze_screen3.png %})

設定が完了すると、ホーム画面で新しい送信先としてBrazeが表示されます。

### ステップ3:新しい同期を作成する {#step-3-create-a-new-sync}

メニューから**Syncs**をクリックし、アクションバーの**Add sync**を選択します。以前に作成したオーディエンスから、使用するオーディエンスを選択します。
次に、送信先として**Braze**を選択し、データの送信先エンティティを選択します。

![オーディエンスとBraze送信先の選択が表示されたOctolisの同期作成画面。]({% image_buster /assets/img/Octolis/Braze_screen4.png %})

### ステップ4:出力設定を行う {#step-4-set-output-settings}

デフォルトでは、送信するすべての属性がBrazeにより作成されますが、同期するフィールドのリストを文書に記録しておく必要があります。

![Brazeのフィールドマッピングと同期スケジュールのOctolis出力設定画面。]({% image_buster /assets/img/Octolis/Braze_screen5.png %}){: style="max-width:75%;"}

設定フィールドの具体的な定義を次に示します。

| フィールド | 説明 |
| --- | --- |
| オーディエンスの同期先は？ | レコードを作成または更新するBrazeエンティティです。 |
| レコードを識別するために使用されるフィールドは？ | レコードがすでにBrazeに存在する場合に、Octolisがレコードを識別するために使用するフィールドです。 |
| 各レコードの送信頻度は？ | デフォルトでは、すべての統合（API、データベース、FTP）で同期は増分同期になります。つまり、最後の更新以降の新しい値のみが更新されます。必要に応じて、定期的にテーブル全体を送信することもできます。開始時に、Octolisは完全なテーブルを送信します。 |
| 同期するフィールドはどれですか？ | OctolisからBrazeへのフィールドマッピングです。利用可能なすべてのフィールドのリストがドロップダウンメニューに表示されます。計算フィールドをBrazeに送信するには、まずBrazeエンティティ内に対応する列を作成しておく必要があります。 |
| オーディエンスをいつ同期しますか？ | Brazeへのデータの送信方法：手動、リアルタイム、またはプログラムによる送信のいずれかです。 |
| レコードの同期タイミングは？ | 作成：オプトインの場合、Brazeテーブルがマスターのままであることが重要です。フィールドの更新時にOctolisが同期をトリガーしないようにします。<br><br>更新：一方で、たとえば名フィールドの場合、顧客が新しいエントリを入力するたびにBrazeテーブルのフィールドを更新できるようにすることがあります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ4:出力設定を行う" }

## 複数キーの重複排除 {#multi-keys-deduplication}

重複排除は、複数のソース、特にオンラインおよびオフラインのソースのデータを照合する場合に大きな課題となります。Octolisの高度なノーコードモジュールにより、[重複排除](https://help.octolis.com/resources/faq/what-is-deduplication-and-how-does-it-work)に複数のキーを使用できます。このモジュールは各マスターテーブルで使用できるため、各エンティティにロジックを適合させることができます。