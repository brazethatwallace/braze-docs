---
nav_title: Copy Pastd
article_title: Copy Pastd
alias: /partners/copy_pastd/
description: "このリファレンス記事では、BrazeとCopy Pastdのパートナーシップについて説明します。Copy Pastdは、Liquid対応のContent Blocksやテンプレートをドラッグアンドドロップで作成し、Brazeワークスペースに直接プッシュできるメールビルダーです。"
page_type: partner
search_tag: Partner
---

# Copy Pastd

> [Copy Pastd](https://copypastd.com/) Building Blocksは、Liquid対応のContent Blocksやフルテンプレートをドラッグアンドドロップで作成し、Brazeワークスペースに直接プッシュできるメールビルダーです。一度デザインすれば、Brazeに同期して、Campaigns、Canvases、トリガーフローで同じコンポーネントを再利用でき、毎回HTMLを再構築する必要がありません。

_このインテグレーションはCopy Pastdによって管理されています。_

## インテグレーションについて {#about-the-integration}

BrazeとCopy Pastdのインテグレーションにより、Building Blocks（クリーンなLiquid、Content Blockの参照、およびCampaignやCanvasにそのまま組み込めるテンプレートを含むBrazeネイティブの出力を生成するホスト型メールビルダー）でメールを構築できます。

再利用可能なブロックからメールを組み立て、ワンクリックでBrazeにプッシュし、同じブランドスタイル、コンポーネント、ダイナミックコンテンツがすべての送信で一貫してレンダリングされることを確認できます。その結果、手動コーディングのテンプレートが減り、メールの作成と送信にかかる時間が短縮され、変更時にすべての場所で更新される一元化されたライブラリーが実現します。

## 前提条件 {#prerequisites}

このインテグレーションを使用するには、以下が必要です。

| 要件 | 説明 |
| ----------- | ----------- |
| Copy Pastdアカウント | Building Blocksを使用するために必要です。[copypastd.com](https://copypastd.com)でサインアップしてください。各顧客にはワークスペース、スタイルシートライブラリー、5つのビルダーシート、ブロックライブラリーが提供されます。 |
| メールテンプレート用のBraze REST APIキー | `templates.email.create`、`templates.email.update`、`templates.email.list`の権限を持つAPIキー。<br><br>Brazeダッシュボードの**Settings** > **API Keys**からキーを作成してください。 |
| Content Blocks用のBraze REST APIキー | `content_blocks.create`、`content_blocks.update`、`content_blocks.info`、`content_blocks.list`の権限を持つAPIキー。<br><br>Brazeダッシュボードの**Settings** > **API Keys**からキーを作成してください。 |
| カタログ用のBraze REST APIキー（オプション） | `catalogs.get`、`catalogs.get_item`、`catalogs.get_selections`への読み取りアクセス権を持つAPIキー。ブロックをBrazeカタログにバインドする予定がある場合にのみ必要です。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントはインスタンスのBraze URLに依存します。Building Blocksは、選択したクラスターに基づいてエンドポイントを自動的に選択します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## ユースケース {#use-cases}

* **大規模なブランド一貫性のあるオーサリング。** Building Blocksのスタイルシートをすべてのテンプレートに適用すると、カラー、フォント、ボタンスタイル、パディングスケールが数百通のメールで同一にレンダリングされます。ブランドが変更された場合、スタイルシートを一度更新して再同期するだけで、すべてのメールに一括で更新を展開できます。
* **コネクテッドコンテンツとカタログバインドの製品テンプレート。** メールブロックのフィールドをビルダー内から[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)エンドポイントや[Brazeカタログ]({{site.baseurl}}/user_guide/data/activation/catalogs/)に直接バインドできます。新製品のドロップ、シーズンコレクション、コンテンツの更新に同じテンプレートを再利用でき、Liquidに触れる必要がありません。
* **非技術系マーケター向けのセルフサービスメール制作。** Liquidのパーソナライゼーションやロジックを含む承認済みブロックからフルメールを作成し、HTMLやLiquidの記述や品質保証のための開発者サポートなしにBrazeにプッシュしてレビューできます。
* **ワンクリックで更新できる一元化されたヘッダーとフッター。** Building Blocksビルダーでヘッダーまたはフッターを一度作成し、Brazeにプッシュします。それを参照するすべてのテンプレートが同期されるため、ロゴの差し替え、法的文言の変更、新しいソーシャルリンクの追加は、Building Blocks内で一度更新するだけで、Braze内のすべてのメールに反映されます。
* **すべてのメールにわたる一元化されたコンテンツ。** ヒーロー、フッター、プロモカードをBuilding Blocksのスマートブロックとして一度作成します。更新して同期すると、それを参照するBraze内のすべてのメールが次回送信時に変更を反映します。ウェルカムフロー、週刊ニュースレター、トリガージャーニーが、各Campaignを編集することなく常に最新の状態を維持します。
* **コントリビューター向けのロックされたテンプレート。** テンプレートを作成し、選択したフィールドをロックしてから、他のチームをコントリビューターインターフェイスに招待して、ユーザー向けツールへのアクセスを付与せずに独自のメールを作成できるようにします。

## インテグレーション {#integration}

### ステップ 1: Building BlocksをBrazeに接続する {#step-1-connect-building-blocks-to-braze}

{% alert note %}
Building BlocksのBrazeへの接続は一度だけのセットアップです。認証情報が検証されると、Building Blocksはすべての将来の同期とテンプレートプッシュのために認証情報を保存します。
{% endalert %}

1. [blocks.copypastd.com](https://blocks.copypastd.com)でBuilding Blocksにログインするか、[copypastd.com](https://copypastd.com)で**Login**を選択します。
2. ダッシュボードから**Set up your Braze connection**を選択します。（このピルは初回ログイン時から完了するまで管理者に表示されます。**Team Settings** > **Connect** > **Braze API Keys**からもアクセスできます。）
3. ドロップダウンからBrazeクラスターを選択します。対応するRESTエンドポイントが自動的に入力されます。
4. テンプレートAPIキー、Content Blocks APIキー、および（オプションで）カタログAPIキーを該当するフィールドに貼り付けます。
5. **Validate and save**を選択します。Building BlocksがBrazeを呼び出してキーが機能し、権限スコープが正しいことを確認します。不足がある場合、インラインエラーでどのスコープが間違っているかが表示されます。

### ステップ 2: ライブラリーをBrazeに同期する {#step-2-sync-your-library-to-braze}

1. キーが検証された後、セットアップモーダルで**Sync now**を選択します。（**Settings** > **Connect** > **Braze** > **Sync library**からいつでも再同期できます。）<br> Building BlocksがスタイルシートとブロックをBraze Content BlocksとしてBrazeワークスペースにプッシュします。Brazeでは`CP_`（ブロックの場合、例：`CP_Hero_1`）または`cp_`（スタイルシートの場合、例：`cp_default_style`）のプレフィックスが付いた名前で表示されます。
2. 同期が完了したら、ビルダーから**Push to Braze**を使用して個別のテンプレートをプッシュできます。

## Building Blocksのカスタマイズ {#customize-building-blocks}

### ステップ 1: スタイルシートを設定する {#step-1-set-up-your-stylesheet}

1. Building Blocksで、**Settings** > **Build** > **Stylesheets**に移動します。
2. デフォルトのスタイルシートを編集するか、新しいスタイルシートを作成します。カラーパレット（24色の名前付きカラー）、フォント（Google Fonts対応）、ボタンスタイル、リンクスタイル、角丸、パディングスケールを設定します。
3. **Save**を選択します。Building Blocksがこのスタイルシートを使用するすべてのブロックのLiquidを再生成します。
4. **Sync now**を選択して、更新されたスタイルをBrazeワークスペースにプッシュします。

### ステップ 2: コネクテッドコンテンツエンドポイントを有効にする（オプション） {#step-2-enable-connected-content-endpoints-optional}

1. Building Blocksで、**Settings** > **Connect** > **Connected Content endpoints**に移動します。
2. エンドポイントURLを追加し、名前を付けて保存します。Building Blocksは標準のJSONシェイプに加えて、Google Sheetsのレスポンスシェイプもサポートしています。
3. ビルダーで、**Personalize**パネルからテキスト、画像、またはリンクフィールドをコネクテッドコンテンツ変数にバインドします。エクスポート時に正しい{% raw %}`{% connected_content %}`{% endraw %} Liquidが生成されます。

### ステップ 3: Brazeカタログにバインドする（オプション） {#step-3-bind-to-braze-catalogs-optional}

1. Building Blocksで、**Settings** > **Connect** > **Catalogs**に移動します。Building BlocksがカタログAPIキーを使用してカタログリストを読み取ります。
2. 互換性のあるブロック（例：製品グリッド）を開きます。
3. カタログとセレクションを選択し、ブロックフィールドをカタログアイテムの属性にマッピングします。
4. テンプレートをプッシュします。Building Blocksが正しい{% raw %}`{% catalog_items %}`{% endraw %}および{% raw %}`{% catalog_selection_items %}`{% endraw %} Liquidを出力し、Brazeが送信時に解決します。

### ステップ 4: Brazeカスタム属性を追加する（オプション） {#step-4-add-your-braze-custom-attributes-optional}

Building BlocksにはデフォルトのBrazeユーザー属性（`first_name`、`email`、`country`など）が含まれています。独自のカスタム属性にブロックをバインドするには、Building Blocksに一度インポートすると、すべての**Personalize**ドロップダウンで利用可能になります。

1. Building Blocksで、**Team Settings** > **Connect** > **Custom Attributes**に移動します。
2. 以下のいずれかの方法でカスタム属性をインポートします。
* **一括インポート（推奨）。** Brazeで**Data Settings** > **Custom Attributes**に移動し、**Export**（右上）を選択します。Building BlocksにCSVをアップロードします。
* **属性を1つずつ追加。** 属性名（例：`loyalty_tier`）を入力し、**Add**を選択します。この方法は、いくつかの属性のみを追加する場合や、Brazeエクスポート間に新しい属性を追加する場合に便利です。

保存後、カスタム属性がビルダーの**Personalize**ドロップダウンにデフォルトと並んで表示されます。挿入すると、エクスポート時に正しい{% raw %}`{{custom_attribute.${name}}}`{% endraw %} Liquidがレンダリングされるため、Brazeが送信時に受信者ごとに値を解決します。

## インテグレーションの使用 {#use-the-integration}

### ステップ 1: テンプレートをBrazeにプッシュする {#step-1-push-a-template-to-braze}

1. Building Blocksビルダーで任意のメールを開きます。
2. **Push to Braze**（右上）を選択します。
3. ワークスペースを選択して確認します。Building BlocksがレンダリングされたLiquidを含むメールテンプレートをBrazeに作成します。

テンプレートはBrazeの**Templates & Media** > **Email Templates**に、メール設定で選択したメール名と日付に基づいて名前が付けられて表示されます。

### ステップ 2: CampaignまたはCanvasでテンプレートを使用する {#step-2-use-the-template-in-a-campaign-or-canvas}

1. Brazeで新しいメールCampaignまたはCanvasステップを作成します。
2. **Templates**を選択し、Building Blocksがプッシュしたテンプレートを選択します。

テンプレートにはすべてのBuilding Blocksの参照（スタイルシート、Content Blocks）がライブの{% raw %}`{{content_blocks.${...}}}`{% endraw %} Liquidとして含まれているため、Building Blocksでの更新はテンプレートを再インポートせずに反映されます。

### ステップ 3: コンテンツを一元的に更新する {#step-3-update-content-centrally}

1. Building Blocksで、該当するブロックまたはスタイルシートを編集します。
2. **Sync**を選択して、更新されたContent BlockをBrazeにプッシュします。

それを参照するBraze内のすべてのメール（エバーグリーン、トリガー、ウェルカムフロー）が次回送信時に新しいバージョンを反映します。各Campaignを編集する必要はありません。

### ステップ 4: コンテンツプールを構築する {#step-4-build-content-pools}

コンテンツプールは、メールが静的コピーを含む代わりに参照するコンテンツ行のテーブルです。Building Blocksでプールを更新すると、それを使用するBraze内のすべてのメールが次回送信時に新しいコンテンツを配信します。コンテンツプールは、週刊ニュースレター、ウェルカムフロー、ウィンバックシーケンス、シーズンCampaigns、購入後ジャーニーなど、同じコンテンツを多くのメールで常に最新に保つ必要がある場所で使用します。

1. Building Blocksで、プライマリナビゲーションの**Content**を選択します。
2. **New Pool**を選択します。保持する内容を説明する名前を入力します（例：Weekly Offers、Product Catalog、News Articles）。
3. プールが供給するブロックタイプを選択します（例：Hero、Grid、Card）。これにより、各行で使用可能なフィールドが設定されます。
4. 行を追加します。各行は1つのコンテンツです。フィールド（見出し、画像、CTAテキスト、CTAリンクなど）を入力します。
5. 行をドラッグして上下に移動し、優先順位を設定します。各行をアクティブまたは非アクティブに切り替え、オプションで開始日と終了日を設定します。送信時に、日付が有効な最も優先度の高いアクティブな行が選択されます。
6. **Save**をクリックします。スマートブロックがこのプールを参照できるようになります。

### ステップ 5: スマートブロックを使用してメールにプールコンテンツをレンダリングする {#step-5-use-smart-blocks-to-render-pool-content-in-your-emails}

スマートブロックは、静的コンテンツを保持する代わりに1つ以上のコンテンツプールを参照するビルダーキャンバス上のブロックです。送信時に、Brazeが最も優先度が高く、アクティブで、日付が有効なプール行をレンダリングします。エクスポートされたLiquidがその処理を行います。追加のBrazeセットアップは不要です。

1. Building Blocksで、スマートブロックをキャンバスにドラッグします（対応するプールがある任意のブロックタイプ）。
2. プロパティパネルで、カスケードエディターを開きます。
3. 優先順位に従って1つ以上のコンテンツプールを追加します。これがウォーターフォールです。アクティブで日付が有効な行を持つ最初のプールがレンダリングされます。ライブなものがない場合、スマートブロックは次のプール、さらに次のプールにフォールスルーします。一般的なパターンは「フラッシュセール > 週間オファー > エバーグリーンお気に入り」で、常に何かが用意されています。
4. テンプレートをBrazeにプッシュします。エクスポートされたLiquidにはフルカスケードが含まれているため、Brazeが送信ごとにプールの優先度と日付を評価します。

以降は、メールではなくプールを更新します。トリガーフロー、エバーグリーンニュースレター、シーズンCampaignsはすべて、プールが最新である限り最新の状態を維持します。

アップロードしたBuilding BlocksテンプレートはBrazeの**Templates & Media** > **Email Templates**にあります。同期されたスタイルシートとブロックは**Templates & Media** > **Content Blocks**に表示されます。

## 考慮事項 {#considerations}

- **Building Blocksチームスペースごとに1つのBrazeインスタンス。** 各Building Blocksチームは単一のBrazeインスタンスに接続します。複数のワークスペース（別々のブランド、リージョン、環境）を運用している顧客は、同じチームに追加でき、ブロックの共有が可能になります。
- **APIキーの権限は個別にスコープされます。** テンプレートキーとContent Blocksキーは分離されています。キーに必要なスコープが不足している場合、検証がすぐに失敗するため、Brazeでどの権限を追加すべきかが正確にわかります。
- **Content Block名は名前空間化されています。** Building Blocksは`CP_`（ブロック）および`cp_`（スタイルシート）のプレフィックスを付けてContent Blocksをプッシュし、Brazeで直接作成されたContent Blocksとの衝突を回避します。
- **スタイルシートの編集はすべてのメールを更新します。** スタイルシートはすべてのテンプレートが参照する単一のBraze Content Blockとしてレンダリングされます。Building Blocksでの変更は、スケジュール済みのものを含め、それを使用するBraze内のすべてのメールを更新します。同期前にドラフトテンプレートでスタイルシートの変更をテストしてください。
- **カタログバインドは読み取り専用です。** Building BlocksはバインディングUIを表示するためにカタログを読み取ります。Brazeカタログへの書き込みは行いません。すべてのカタログ管理は引き続きBrazeダッシュボードで行います。
- **レート制限とリトライ。** すべてのアウトバウンドリクエストはBrazeのレート制限を遵守し、エクスポネンシャルバックオフ、ジッター、Retry-Afterの処理を行います。パートナーアトリビューションのために、すべての呼び出しで`User-Agent: partner-CopyPastd`ヘッダーが送信されます。
- **ユーザーデータは送信されません。** Building Blocksはコンテンツオーサリングツールです。ユーザー属性、イベント、購入、またはセグメントデータをBrazeにプッシュせず、Brazeデータポイントを消費しません。

## トラブルシューティング {#troubleshooting}

- **APIキーの検証が失敗する。** 各キーが前提条件に記載されている正確な権限を持っていることを確認してください。テンプレートとContent Blocksのスコープは個別にチェックされます。Brazeでキーを再生成した場合、新しい値をBuilding Blocksに貼り付けて再検証してください。
- **RESTエンドポイントの不一致。** テンプレートキーとContent Blocksキーは同じBrazeワークスペースのものである必要があり、RESTエンドポイントはクラスターと一致する必要があります。Building Blocksのドロップダウンがこれを自動設定するため、検証が失敗した場合はクラスターの選択を確認してください。
- **Push to Brazeがエラーを返す。** **Settings** > **Build** > **Activity log**を開いて、最後の同期試行とBrazeが返したレスポンスを確認してください。ほとんどの失敗は権限関連（スコープの不足）またはクォータ関連（レート制限、自動リトライ）です。
- **Content BlockがBrazeで更新されない。** **Settings** > **Connect** > **Braze** > **Sync library**から手動再同期をトリガーしてください。Building Blocksはコンペアアンドスワップを実行するため、変更されていないブロックはスキップされます。
- **テンプレートがBrazeにまだ存在しないContent Blockを参照している。** **Sync library**を使用して依存関係（スタイルシート、スマートブロック）を先にプッシュしてから、テンプレートをプッシュしてください。
- **その他すべての問題。** Copy Pastd（[help@copypastd.com](mailto:help@copypastd.com)）にお問い合わせください。チーム名と失敗したアクションの時刻を含めていただくと、Copy Pastdが対応するアクティビティログを確認できます。