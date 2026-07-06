---
nav_title: NiftyImages
article_title: NiftyImages
description: "NiftyImagesをBrazeに接続して、パーソナライズされたダイナミックなビジュアルを作成し、コンタクトプロパティを同期し、アセットを再利用可能なContent Blocksとして公開する方法を説明します。"
alias: /partners/niftyimages/
page_type: partner
search_tag: Partner
---

# NiftyImages

> [NiftyImages](https://niftyimages.com)は、Brazeの顧客がメール、モバイル、アプリ内メッセージング向けにパーソナライズされたリアルタイムのビジュアルコンテンツを作成できるようにします。ライブの顧客データ、製品データ、ビジネスデータをダイナミックな画像やコンテンツに接続することで、ブランドはカウントダウンタイマー、パーソナライズされたおすすめ、ローカライズされたメッセージング、在庫更新、プロモーションオファーなど、エンゲージメントとコンバージョンを促進するタイムリーで関連性の高い体験を提供できます。

_この統合はNiftyImagesによって管理されています。_

## 統合について {#about-the-integration}

BrazeのNiftyImages統合を使用すると、Brazeのコンタクトデータを使用してパーソナライズされたダイナミックなビジュアルを作成できます。チームはパーソナライズされた画像、カウントダウンタイマー、地図、カレンダー、ロイヤルティビジュアルなどのアセットを構築し、再利用可能なBraze [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)として公開して、キャンペーンやキャンバス全体で使用できます。これにより、時間を節約し、エラーを減らし、パーソナライズされたコンテンツ管理を簡素化できます。

## ユースケース {#use-cases}

NiftyImagesを使用すると、以下のことができます。

- **画像をパーソナライズする：**各顧客の名前、ロイヤルティステータス、報酬残高、ロケーション、製品の好み、メンバーシップティア、アカウント詳細、その他のBrazeコンタクトプロパティを含む画像を作成します。
- **カウントダウンタイマーを追加する：**セール、製品ドロップ、イベント、期間限定オファー、予約、オンボーディング期限、パーソナライズされた有効期限のリアルタイムカウントダウンタイマーを追加します。
- **ダイナミックな地図を表示する：**顧客のロケーションデータまたはBrazeコンタクトプロパティに基づいて、最寄りの店舗、イベント会場、サービスエリア、ディーラー、クラブ、支店、ピックアップ場所を表示します。
- **カレンダーを表示する：**パーソナライズされた日付、イベント、予約、更新期間、キャンペーンの瞬間、顧客のマイルストーンをキャンペーンビジュアル内に直接表示します。
- **ライブ投票を実行する：**キャンペーンにインタラクティブな投票を追加し、顧客が投票した後にリアルタイムで更新される結果を表示します。
- **スクラッチオフを作成する：**パーソナライズされた報酬、割引、オファー、画像、またはメッセージを明らかにするゲーミフィケーションされたスクラッチオフ体験を作成します。
- **ロイヤルティデータを可視化する：**顧客データをプログレスバー、アカウントサマリー、ロイヤルティビジュアル、チャート、グラフに変換し、各受信者にパーソナライズします。
- **ルールベースのコンテンツを適用する：**時間、ロケーション、デバイス、顧客データ、オーディエンスセグメント、またはキャンペーンロジックに基づいて異なるビジュアルを表示します。
- **ダイナミックコンテンツを再利用する：**完成したNiftyImagesアセットをBraze Content Blocksに公開し、チームがマーケティングメール、テンプレート、キャンペーン、共有ブランドアセット全体で再利用できるようにします。

## 前提条件 {#prerequisites}

開始する前に、以下を確認してください。

| 要件 | 説明 |
| ------------ | ----------- |
| NiftyImagesアカウント | パーソナライズされた画像、タイマー、地図、カレンダー、スクラッチオフ、チャート、その他のダイナミックビジュアルを作成・管理するには、[NiftyImagesアカウント](https://niftyimages.com/Signup)が必要です。 |
| Brazeアカウント | Brazeのキャンペーン、キャンバス、メールテンプレート、メッセージングチャネル内でNiftyImagesを使用するには、Brazeアカウントが必要です。 |
| Braze REST APIキー | `custom_attributes.get`および`content_blocks.create`権限を持つBraze REST APIキー。<br><br>これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/api/basics#endpoints)。エンドポイントは、お使いのインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

NiftyImagesでBrazeアカウントを接続して、コンタクトプロパティを同期し、アセットをBraze Content Blocksに公開します。

### ステップ1：NiftyImagesで統合を開く {#step-1-open-integrations-in-niftyimages}

1. NiftyImagesで、**Settings** > **Integrations**に移動します。
2. **Braze**を選択します。
3. **Connect Braze**を選択します。

### ステップ2：Braze REST APIキーを作成する {#step-2-create-your-braze-rest-api-key}

1. Brazeで、**設定** > **APIキー**に移動します。
2. NiftyImages統合用のREST APIキーを作成または選択します。
3. **Custom Attributes**で、`custom_attributes.get`を選択します。
4. **Content Blocks**で、`content_blocks.create`を選択します。
5. APIキーを保存し、REST APIキーと[RESTエンドポイント]({{site.baseurl}}/api/basics#endpoints)をコピーします。

### ステップ3：NiftyImagesでBrazeアカウントを接続する {#step-3-connect-your-braze-account-in-niftyimages}

1. NiftyImagesのBraze統合画面に戻ります。
2. Braze REST APIキーを貼り付けます。
3. Braze RESTエンドポイントを入力します。
4. 接続を確認します。
5. **Connected Braze accounts**にBrazeアカウントが**Active**または**Connected**ステータスで表示されることを確認します。

必要に応じて複数のBrazeアカウントを接続できます。これは、代理店、マルチブランドチーム、または複数のBrazeインスタンスを管理する組織に便利です。

## NiftyImagesでアセットをカスタマイズする {#customize-assets-in-niftyimages}

Brazeを接続した後、コンタクト変数同期とContent Block公開を使用して、パーソナライズされたビジュアルを管理します。

### コンタクト変数同期を使用する {#use-contact-variable-sync}

コンタクト変数同期を使用すると、マージタグを手動で入力したり再作成したりすることなく、既存のBrazeコンタクトプロパティをNiftyImages内で直接使用できます。

1. パーソナライズされた画像またはその他のNiftyImagesアセットを作成または編集します。
2. マージタグまたはパーソナライゼーションピッカーを開きます。
3. **Pick from connected integrations**を選択し、使用するBrazeプロパティを選択します。
4. それらの値をテキスト、画像、タイマー、地図、チャート、カレンダー、またはダイナミックコンテンツレイヤーに追加します。
5. 画像を保存します。

Braze変数を使用する保存済み画像には、NiftyImages画像URLにそれらのパーソナライゼーション値が自動的に含まれます。

### Braze Content Blocksに公開する {#publish-to-braze-content-blocks}

1. NiftyImagesアセットを完成させます。
2. **Send to Braze**を選択します。

## BrazeでNiftyImagesを使用する {#use-niftyimages-in-braze}

公開されたContent Blocksを、Brazeのメールテンプレート、キャンペーン、キャンバスで使用します。

### NiftyImagesアセットをBrazeメールに追加する {#add-a-niftyimages-asset-to-a-braze-email}

1. Brazeでメールテンプレート、キャンペーン、またはキャンバスのメールメッセージを開きます。
2. メッセージエディターで、パーソナライゼーションメニューを開き、パーソナライゼーションタイプとして**Content Blocks**を選択します。
3. NiftyImagesから公開したNiftyImages Content Blockを選択します。

### NiftyImagesアセットをBraze全体で再利用する {#reuse-niftyimages-assets-across-braze}

1. 公開されたContent Blockをマーケティングメール、メールテンプレート、キャンペーン、共有ブランドアセット、自動化フロー全体で使用します。
2. NiftyImagesアセットがダイナミック変数を使用している場合、Brazeはメッセージとチャネルに基づいてコンタクト値を渡します。
3. クリエイティブの変更が必要な場合は、NiftyImagesでソースアセットを更新します。

### Brazeアカウントを切断する {#disconnect-a-braze-account}

1. NiftyImagesで**Settings** > **Integrations**に戻ります。
2. Braze接続ページを開きます。
3. 削除するアカウントの削除または切断アイコンを選択します。
4. 切断を確認します。

## 考慮事項 {#considerations}

- **REST API権限：**Braze REST APIキーには、コンタクトプロパティ同期用の`custom_attributes.get`と、アセットをBraze Content Blocksに公開するための`content_blocks.create`が含まれている必要があります。
- **コンタクトプロパティの利用可能性：**接続されたBrazeアカウントで利用可能なコンタクトプロパティのみがNiftyImagesに同期できます。
- **フォールバック値：**パーソナライズされたビジュアルを構築する際にフォールバック値を使用して、コンタクトプロパティが欠落している場合でもすべての顧客に洗練された画像が表示されるようにしてください。
- **再利用可能なContent Blocks：**Braze Content Blocksに公開することで、チームは手動のHTMLコピー＆ペーストを回避し、マージタグエラーを減らし、キャンペーンやテンプレート全体でアセットを再利用できます。
- **複数のBrazeアカウント：**NiftyImagesは複数の接続されたBrazeアカウントをサポートしており、代理店、マルチブランドチーム、複数のBrazeインスタンスを管理するチームに便利です。
- **テスト：**キャンペーンまたはキャンバスを起動する前に、サンプルの顧客プロファイルで最終的なBrazeメッセージをテストしてください。

## トラブルシューティング {#troubleshooting}

NiftyImages統合で問題が発生した場合は、以下の表を参照してください。

| 問題 | 解決方法 |
| ----- | ---------- |
| Brazeアカウントが接続されない | REST APIキーが有効であること、RESTエンドポイントが正しいこと、キーに必要な権限が含まれていることを確認してください。 |
| BrazeコンタクトプロパティがNiftyImagesに表示されない | APIキーに`custom_attributes.get`が含まれていることを確認してください。次に、NiftyImages内でBraze接続を更新してください。 |
| アセットがBraze Content Blocksに公開されない | APIキーに`content_blocks.create`が含まれていること、接続されたBrazeアカウントがContent Blockの作成を許可していることを確認してください。 |
| パーソナライゼーションが正しく表示されない | 選択したBrazeコンタクトプロパティにテストユーザーの値が含まれていることを確認してください。必要に応じてNiftyImagesでフォールバック値を追加してください。 |
| 画像がBrazeでレンダリングされない | NiftyImagesアセットが保存済み、アクティブ、正しく公開されていることを確認してください。意図したチャネルで画像を確認するために、Brazeテストメッセージを送信してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="トラブルシューティング" }