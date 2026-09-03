---
nav_title: Copy Pastd
article_title: Copy Pastd
alias: /partners/copy_pastd/
description: "このリファレンス記事では、BrazeとCopy Pastdのパートナーシップについて説明します。Copy Pastdは、Liquid対応のContent Blocksやテンプレートをドラッグ＆ドロップで作成し、Brazeワークスペースに直接プッシュできるメールビルダーです。"
page_type: partner
search_tag: Partner
---

# Copy Pastd

> [Copy Pastd](https://copypastd.com/) が提供するBuilding Blocksは、Liquid対応のContent Blocksやフルテンプレートをドラッグ＆ドロップで作成し、Brazeワークスペースに直接プッシュできるメールビルダーです。一度デザインすれば、Brazeに同期して、キャンペーン、キャンバス、トリガーフローで同じコンポーネントを再利用でき、毎回HTMLを再構築する必要がありません。

*このインテグレーションはCopy Pastdによって管理されています。*

## 統合について {#about-the-integration}

BrazeとCopy Pastdの統合により、Building Blocks（ホスト型メールビルダー）でメールを構築できます。Building Blocksは、クリーンなLiquid、Content Blocksの参照、テンプレートを含むBrazeネイティブの出力を生成し、変換なしで任意のキャンペーンやキャンバスにそのまま組み込むことができます。

再利用可能なブロックからメールを組み立て、ワンクリックでBrazeにプッシュし、同じブランドスタイル、コンポーネント、ダイナミックなコンテンツがすべての送信で一貫してレンダリングされることを確認できます。その結果、手動でコーディングするテンプレートが減り、メールの作成と送信にかかる時間が短縮され、変更時にすべての場所で更新される一元化されたライブラリが実現します。

## 前提条件 {#prerequisites}

この連携を使用するには、以下が必要です。

| 要件 | 説明 |
| ----------- | ----------- |
| Copy Pastd アカウント | Building Blocks を使用するために必要です。[copypastd.com](https://copypastd.com) でサインアップしてください。各顧客にはワークスペース、スタイルシートライブラリ、5つのビルダーシート、およびブロックライブラリが提供されます。 |
| メールテンプレート用 Braze REST APIキー | `templates.email.create`、`templates.email.update`、`templates.email.list` の権限を持つAPIキー。<br><br>Brazeダッシュボードの**設定** > **APIキー**からキーを作成してください。 |
| Content Blocks用 Braze REST APIキー | `content_blocks.create`、`content_blocks.update`、`content_blocks.info`、`content_blocks.list` の権限を持つAPIキー。<br><br>Brazeダッシュボードの**設定** > **APIキー**からキーを作成してください。 |
| カタログ用 Braze REST APIキー（オプション） | `catalogs.get`、`catalogs.get_item`、`catalogs.get_selections` への読み取りアクセス権を持つAPIキー。ブロックをBrazeカタログにバインドする予定がある場合にのみ必要です。 |
| Braze REST エンドポイント | [REST エンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints)。エンドポイントはお使いのインスタンスのBraze URLによって異なります。Building Blocks は、選択したクラスターに基づいてエンドポイントを自動的に選択します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}

* **ブランドの一貫性を保ちながら大規模にコンテンツを作成。** Building Blocksのスタイルシートをすべてのテンプレートに適用すると、カラー、フォント、ボタンスタイル、パディングの表示が数百通のメールにわたって統一されます。ブランドが変更された場合は、スタイルシートを一度更新して再同期するだけで、すべてのメールに一括で変更を反映できます。
* **Connected Contentとカタログ連携のプロダクトテンプレート。** メールブロックのフィールドを、ビルダー内から直接[Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)エンドポイントや[Brazeカタログ]({{site.baseurl}}/user_guide/data/activation/catalogs)にバインドできます。新商品の発売、季節のコレクション、コンテンツの更新に同じテンプレートを再利用でき、Liquidを編集する必要はありません。
* **技術知識がないマーケターでもセルフサービスでメール制作が可能。** 承認済みのブロックからLiquidのパーソナライゼーションやロジックを含む完全なメールを作成し、開発者にHTMLやLiquidの記述やレビューを依頼することなく、Brazeにプッシュしてレビューに回せます。
* **共通のヘッダーとフッターをワンクリックで更新。** Building Blocksビルダーでヘッダーやフッターを一度作成し、Brazeにプッシュします。それを参照するすべてのテンプレートが同期されるため、ロゴの差し替え、法的文言の変更、新しいソーシャルリンクの追加も、Building Blocks内で一度更新するだけで、Braze内のすべてのメールに反映されます。
* **すべてのメールにわたるコンテンツの一元管理。** ヒーロー、フッター、プロモカードをBuilding Blocksのスマートブロックとして一度作成します。更新して同期すれば、それを参照しているBraze内のすべてのメールが次回送信時に変更を反映します。ウェルカムフロー、週刊ニュースレター、トリガーされたジャーニーも、各キャンペーンを個別に編集することなく常に最新の状態を保てます。
* **コントリビューター向けにロックされたテンプレートでセルフサービスを実現。** テンプレートを作成し、選択したフィールドをロックした上で、他のチームをコントリビューターインターフェイスに招待すれば、ユーザー向けツールへのアクセス権を付与することなく、各チームが独自のメールを作成できます。

## 連携 {#integration}

### ステップ1：Building BlocksをBrazeに接続する {#step-1-connect-building-blocks-to-braze}

{% alert note %}
Building BlocksとBrazeの接続は一度だけの設定です。認証情報が検証されると、Building Blocksはその認証情報を保存し、以降のすべての同期やテンプレートのプッシュに使用します。
{% endalert %}

1. [blocks.copypastd.com](https://blocks.copypastd.com) でBuilding Blocksにログインするか、[copypastd.com](https://copypastd.com) で**ログイン**を選択します。
2. ダッシュボードから、**Set up your Braze connection**を選択します。（このピルは管理者の初回ログイン時に表示され、設定が完了するまで表示されます。**Team Settings** > **Connect** > **Braze API Keys**からもこのページにアクセスできます。）
3. ドロップダウンからBrazeクラスターを選択します。対応するRESTエンドポイントが自動的に入力されます。
4. テンプレートAPIキー、Content Blocks APIキー、および（任意で）カタログAPIキーをそれぞれのフィールドに貼り付けます。
5. **Validate and save**を選択します。Building BlocksがBrazeを呼び出してキーが正しく機能し、権限スコープが正しいことを確認します。不足がある場合は、インラインエラーでどのスコープに問題があるかが表示されます。

### ステップ2：ライブラリをBrazeに同期する {#step-2-sync-your-library-to-braze}

1. キーが検証されたら、設定モーダルで**Sync now**を選択します。（**Settings** > **Connect** > **Braze** > **Sync library**からいつでも再同期できます。）<br> Building Blocksがスタイルシートとブロックを、Braze Content BlocksとしてBrazeワークスペースにプッシュします。Brazeでは`CP_`（例：`CP_Hero_1`）またはスタイルシートの場合は`cp_`（例：`cp_default_style`）のプレフィックスが付いた名前で表示されます。
2. 同期が完了したら、ビルダーから**Push to Braze**を使用して個別のテンプレートをプッシュできます。

## Building Blocksのカスタマイズ {#customize-building-blocks}

### ステップ1：スタイルシートを設定する {#step-1-set-up-your-stylesheet}

1. Building Blocksで、**設定** > **ビルド** > **スタイルシート**に移動します。
2. デフォルトのスタイルシートを編集するか、新しいスタイルシートを作成します。カラーパレット（24色の名前付きカラー）、フォント（Google Fonts対応）、ボタンスタイル、リンクスタイル、角丸、パディングスケールを設定します。
3. **保存**を選択します。Building Blocksは、このスタイルシートを使用するすべてのブロックのLiquidを再生成します。
4. **今すぐ同期**を選択して、更新されたスタイルをBrazeワークスペースにプッシュします。

### ステップ2：Connected Contentエンドポイントを有効にする（オプション） {#step-2-enable-connected-content-endpoints-optional}

1. Building Blocksで、**設定** > **接続** > **Connected Contentエンドポイント**に移動します。
2. エンドポイントURLを追加し、名前を付けて保存します。Building Blocksは、標準のJSON形式に加えて、Google Sheetsのレスポンス形式もサポートしています。
3. ビルダーで、**パーソナライズ**パネルからConnected Content変数にテキスト、画像、またはリンクフィールドをバインドします。エクスポート時に正しい{% raw %}`{% connected_content %}`{% endraw %} Liquidが生成されます。

### ステップ3：Brazeカタログにバインドする（オプション） {#step-3-bind-to-braze-catalogs-optional}

1. Building Blocksで、**設定** > **接続** > **カタログ**に移動します。Building Blocksは、カタログAPIキーを使用してカタログリストを読み取ります。
2. 互換性のあるブロック（例：商品グリッド）を開きます。
3. カタログとセレクションを選択し、ブロックフィールドをカタログアイテムの属性にマッピングします。
4. テンプレートをプッシュします。Building Blocksは、Brazeが送信時に解決するための正しい{% raw %}`{% catalog_items %}`{% endraw %}および{% raw %}`{% catalog_selection_items %}`{% endraw %} Liquidを出力します。

### ステップ4：Brazeカスタム属性を追加する（オプション） {#step-4-add-your-braze-custom-attributes-optional}

Building Blocksには、デフォルトのBrazeユーザー属性（`first_name`、`email`、`country`など）が付属しています。ブロックを独自のカスタム属性にバインドするには、Building Blocksに一度インポートすると、すべての**パーソナライズ**ドロップダウンで利用可能になります。

1. Building Blocksで、**チーム設定** > **接続** > **カスタム属性**に移動します。
2. 以下のいずれかの方法でカスタム属性をインポートします：
* **一括インポート（推奨）。** Brazeで、**データ設定** > **カスタム属性**に移動し、**エクスポート**を選択します。Building BlocksにCSVをアップロードします。
* **属性を1つずつ追加。** 属性名（例：`loyalty_tier`）を入力し、**追加**を選択します。この方法は、いくつかの属性のみを追加する場合や、Brazeエクスポート間に新しい属性を追加したい場合に便利です。

保存すると、カスタム属性がビルダーの**パーソナライズ**ドロップダウンにデフォルトと並んで表示されます。属性を挿入すると、エクスポート時に正しい{% raw %}`{{custom_attribute.${name}}}`{% endraw %} Liquidがレンダリングされるため、Brazeは送信時に受信者ごとに値を解決します。

## 連携の使用 {#use-the-integration}

### ステップ1: テンプレートをBrazeにプッシュする {#step-1-push-a-template-to-braze}

1. Building Blocksビルダーで任意のメールを開きます。
2. アクションバーで**Push to Braze**を選択します。
3. ワークスペースを選択して確認します。Building Blocksが、レンダリングされたLiquidを含むメールテンプレートをBrazeに作成します。

テンプレートはBrazeの**Templates & Media** > **Email Templates**に表示され、メール設定で選択したメール名と日付に基づいて命名されます。

### ステップ2: キャンペーンまたはキャンバスでテンプレートを使用する {#step-2-use-the-template-in-a-campaign-or-canvas}

1. Brazeで、新しいメールキャンペーンまたはキャンバスステップを作成します。
2. **Templates**を選択し、Building Blocksからプッシュされたテンプレートを選択します。

テンプレートには、Building Blocksのすべての参照（スタイルシート、Content Blocks）がライブの{% raw %}`{{content_blocks.${...}}}`{% endraw %} Liquidとして含まれているため、Building Blocksでの更新はテンプレートを再インポートすることなく反映されます。

### ステップ3: コンテンツを一元的に更新する {#step-3-update-content-centrally}

1. Building Blocksで、該当するブロックまたはスタイルシートを編集します。
2. **Sync**を選択して、更新されたコンテンツブロックをBrazeにプッシュします。

それを参照しているBraze内のすべてのメール（エバーグリーン、トリガー、ウェルカムフロー）は、次回送信時に新しいバージョンを取得します。各キャンペーンを個別に編集する必要はありません。

### ステップ4: コンテンツプールを構築する {#step-4-build-content-pools}

コンテンツプールは、メールが静的なコピーを含む代わりに参照するコンテンツ行のテーブルです。Building Blocksでプールを更新すると、それを使用しているBraze内のすべてのメールが次回送信時に新しいコンテンツを配信します。コンテンツプールは、週刊ニュースレター、ウェルカムフロー、奪還シーケンス、季節キャンペーン、購入後ジャーニーなど、同じコンテンツを多くのメールにわたって最新の状態に保つ必要がある場所で使用します。

1. Building Blocksで、プライマリナビゲーションの**Content**を選択します。
2. **New Pool**を選択します。プールの内容を説明する名前を入力します（例: Weekly Offers、Product Catalog、News Articles）。
3. プールが供給するブロックタイプを選択します（例: Hero、Grid、Card）。これにより、各行で使用可能なフィールドが設定されます。
4. 行を追加します。各行は1つのコンテンツです。フィールド（見出し、画像、CTAテキスト、CTAリンクなど）を入力します。
5. 行をドラッグして上下に移動し、優先順位を設定します。各行をアクティブまたは非アクティブに切り替え、オプションの開始日と終了日を設定します。送信時に、日付が有効な最も優先度の高いアクティブな行が選択されます。
6. **Save**をクリックします。スマートブロックがこのプールを参照できるようになります。

### ステップ5: スマートブロックを使用してメールにプールコンテンツをレンダリングする {#step-5-use-smart-blocks-to-render-pool-content-in-your-emails}

スマートブロックは、静的なコンテンツを保持する代わりに1つ以上のコンテンツプールを参照するビルダーキャンバス上のブロックです。送信時に、Brazeは最も優先度が高く、アクティブで、日付が有効なプール行をレンダリングします。エクスポートされたLiquidがその処理を行います。Braze側での追加設定は不要です。

1. Building Blocksで、スマートブロックをキャンバスにドラッグします（一致するプールを持つ任意のブロックタイプ）。
2. プロパティパネルで、カスケードエディターを開きます。
3. 1つ以上のコンテンツプールを優先順位に従って追加します。これがウォーターフォールです。アクティブで日付が有効な行を持つ最初のプールがレンダリングされます。ライブなものがない場合、スマートブロックは次のプール、さらにその次のプールへとフォールスルーします。一般的なパターンは「Flash Sale > Weekly Offers > Evergreen Favorites」で、常に何かが用意されている状態になります。
4. テンプレートをBrazeにプッシュします。エクスポートされたLiquidには完全なカスケードが含まれているため、Brazeは送信ごとにプールの優先度と日付を評価します。

これ以降は、メールではなくプールを更新します。トリガーフロー、エバーグリーンニュースレター、季節キャンペーンはすべて、プールが最新である限り最新の状態を維持します。

アップロードしたBuilding BlocksテンプレートはBrazeの**Templates & Media** > **Email Templates**にあります。同期されたスタイルシートとブロックは**Templates & Media** > **Content Blocks**に表示されます。

## 考慮事項 {#considerations}

- **Building Blocksのチームスペースごとに1つのBrazeインスタンス。** 各Building Blocksチームは1つのBrazeインスタンスに接続します。複数のワークスペース（異なるブランド、地域、環境）を運用している顧客は、それらを同じチームに追加でき、ブロックの共有が可能になります。
- **APIキーの権限は個別にスコープされます。** テンプレートキーとContent Blocksキーは分離されています。キーに必要なスコープが不足している場合、バリデーションは即座に失敗するため、Brazeでどの権限を追加すべきか正確に把握できます。
- **Content Blocks名は名前空間で管理されます。** Building Blocksは、Brazeで直接作成されたContent Blocksとの衝突を避けるため、`CP_`（ブロック）および`cp_`（スタイルシート）プレフィックスを付けてContent Blocksをプッシュします。
- **スタイルシートの編集はすべてのメールに反映されます。** スタイルシートは、すべてのテンプレートから参照される単一のBraze Content Blockとしてレンダリングされます。Building Blocksでの変更は、すでにスケジュールされたものを含め、それを使用しているBraze内のすべてのメールを更新します。同期する前に、下書きテンプレートでスタイルシートの変更をテストしてください。
- **カタログバインディングは読み取り専用です。** Building BlocksはバインディングUIにデータを表示するためにカタログを読み取ります。Brazeカタログへの書き込みは行いません。カタログの管理はすべて引き続きBrazeダッシュボードで行います。
- **レート制限とリトライ。** すべてのアウトバウンドリクエストはBrazeのレート制限を遵守し、指数バックオフ、ジッター、およびRetry-Afterの処理を行います。パートナーアトリビューションのため、すべてのリクエストに`User-Agent: partner-CopyPastd`ヘッダーが送信されます。
- **ユーザーデータは送信されません。** Building Blocksはコンテンツオーサリングツールです。ユーザー属性、イベント、購入、セグメントデータをBrazeにプッシュすることはなく、Brazeのデータポイントを消費することもありません。

## トラブルシューティング {#troubleshooting}

- **APIキーの検証が失敗する。** 各キーが「前提条件」に記載されている正確な権限を持っているか確認してください。テンプレートとContent Blocksのスコープは個別にチェックされます。Brazeでキーを再生成した場合は、新しい値をBuilding Blocksに貼り付けて再検証してください。
- **RESTエンドポイントの不一致。** テンプレートとContent Blocksのキーは同じBrazeワークスペースのものである必要があり、RESTエンドポイントはクラスターと一致している必要があります。Building Blocksのドロップダウンが自動的に設定しますので、検証が失敗した場合はクラスターの選択を確認してください。
- **Brazeへのプッシュがエラーを返す。** **Settings** > **Build** > **Activity log** を開いて、最後の同期試行とBrazeが返したレスポンスを確認してください。ほとんどの失敗は権限関連（スコープの不足）またはクォータ関連（レート制限、自動的にリトライされます）です。
- **コンテンツブロックがBrazeで更新されない。** **Settings** > **Connect** > **Braze** > **Sync library** から手動再同期をトリガーしてください。Building Blocksはcompare-and-swapを実行するため、変更のないブロックはスキップされます。
- **テンプレートが、Brazeにまだ存在しないコンテンツブロックを参照している。** まず **Sync library** を使用して依存関係（スタイルシート、スマートブロック）をプッシュしてから、テンプレートをプッシュしてください。
- **その他すべての問題について。** Copy Pastd（[help@copypastd.com](mailto:help@copypastd.com)）にお問い合わせください。チーム名と失敗したアクションの時刻を記載していただくと、Copy Pastdが該当するアクティビティログを確認できます。