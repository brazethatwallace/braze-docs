---
nav_title: Crowdin
article_title: Crowdin
description: "Crowdinの統合を使用して、翻訳メモリ、用語集、機械翻訳を活用しながら、キャンペーン、キャンバスエクスペリエンス、メールテンプレート、Content Blocksを翻訳できます。"
alias: /partners/crowdin/
page_type: partner
search_tag: Partner

---

# Crowdin

> [Crowdin](https://crowdin.com/)は、AI駆動のローカライゼーション管理プラットフォームであり、ソフトウェア、アプリ、マーケティングコンテンツの翻訳を自動化するのに役立ちます。

CrowdinをBrazeに接続して、キャンペーンやキャンバスエクスペリエンスの翻訳を管理できます。自動同期は機械翻訳、翻訳メモリ、用語集と連携するため、人手による翻訳ワークフローと自動化されたワークフローの一貫性が保たれます。

_この統合はCrowdinによって管理されています。_

## 連携について {#about-the-integration}

Crowdinは、Brazeと連携する2つのアプリを提供しています：[Braze キャンペーン & キャンバス](https://store.crowdin.com/braze-content-translation) と [Braze Email Templates](https://store.crowdin.com/braze-app)。ローカライズするBrazeの機能に応じて選択してください。以下の表で両者を比較しています。

### 適切なCrowdinアプリの選択 {#choose-the-right-crowdin-app}

| チャネルまたは機能 | Braze キャンペーン & キャンバス | Braze Email Templates |
| --- | --- | --- |
| **キャンペーン** | ✅ サポート対象 | ❌ サポート対象外 |
| **キャンバスステップ** | ✅ サポート対象 | ❌ サポート対象外 |
| **メールテンプレート** | ❌ サポート対象外 | ✅ サポート対象 |
| **Content Blocks** | ❌ サポート対象外 | ✅ サポート対象 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="適切なCrowdinアプリの選択" }

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| --- | --- |
| **Crowdinアカウント** | [Crowdin.comアカウント](https://accounts.crowdin.com/register)または[Crowdin Enterpriseアカウント](https://accounts.crowdin.com/workspace/create)が必要です。 |
| **Crowdinプロジェクト** | Brazeに接続する前に、CrowdinまたはCrowdin Enterpriseで[翻訳プロジェクトを作成](https://support.crowdin.com/creating-project/)してください。 |
| **Braze REST APIキー** | キャンペーン、キャンバス、Content Blocks、カスタム属性、メール、テンプレートの権限を持つBraze REST APIキー。 |
| **Braze RESTエンドポイント** | お客様固有のBraze RESTエンドポイントURL（例：`https://rest.iad-03.braze.com`）。 |
| **Braze多言語設定** | Brazeダッシュボードの**設定** > **ローカライゼーション設定**でロケールが設定されている必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## BrazeキャンペーンとキャンバスのCrowdin連携 {#braze-campaigns-canvas-integration}

ライブメッセージ内のコンテンツをローカライズする場合は、[Braze キャンペーン & キャンバス アプリ](https://store.crowdin.com/braze-content-translation)を使用して、キャンペーンとキャンバスの下書きから翻訳可能な文字列をBrazeの多言語サポートと同期できます。

動画によるウォークスルーについては、[Braze キャンペーン & キャンバス integration](https://youtu.be/ahG1ET4VRKA)をご覧ください。

### ステップ1:Brazeで多言語設定をセットアップする {#step-1-set-up-multi-language-settings-in-braze}

Crowdinを接続する前に、Brazeでターゲット言語を追加します。

1. Brazeで、**設定** > **ローカライゼーション設定**に移動します。
2. サポートする予定の言語を追加します。

![ロケール名、ロケールキー、ロケールの追加が表示されているBrazeの設定内のロケールページ。]({% image_buster /assets/img/crowdin/braze_locales.png %})

{: start="3"}
3. 各**ロケールキー**（例：`en-US`、`fr-FR`、`es-ES`）を確認します。これらの値は、Crowdinで言語をマッピングする際に使用します。

### ステップ2:CrowdinでBrazeプロジェクトをセットアップする {#step-2-set-up-the-braze-project-in-crowdin}

1. Crowdin EnterpriseまたはCrowdin.comアカウントで、ナビゲーションメニューの**Store**に移動します。
2. **Braze キャンペーン & キャンバス**を検索し、**Install**を選択します。

![Braze キャンペーン & キャンバスが選択され、InstallがハイライトされているCrowdin Store。]({% image_buster /assets/img/crowdin/crowdin_store_campaigns_canvas.png %})

{: start="3"}
3. この連携を使用するプロジェクトを選択します。
4. 連携を開くには、プロジェクトの**Integrations** > **Braze キャンペーン & キャンバス**に移動します。

#### BrazeをCrowdinに接続する {#connecting-braze-to-crowdin}

Braze APIの認証情報を使用して接続を認可します。

![REST APIキー、RESTエンドポイント、Log in with Braze キャンペーン & キャンバスが表示されているCrowdinのBraze キャンペーン & キャンバス接続フォーム。]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_login.png %})

- **Braze REST APIキー：** Brazeの**設定** > **APIと識別子** > **APIキー**で作成します。この連携に必要な権限（キャンペーン、キャンバス、Content Blocks、カスタム属性）を付与します。
- **Braze RESTエンドポイント：** Brazeインスタンスの URL を入力します（例：`https://rest.iad-03.braze.com`）。詳細については、[REST APIエンドポイント]({{site.baseurl}}/api/basics#endpoints)を参照してください。

![APIキーの作成とRESTエンドポイントのコピーコントロールが表示されているBraze REST APIキーページ。]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %})

**Log in with Braze キャンペーン & キャンバス**を選択します。

### ステップ3:Crowdinで言語マッピングを設定する {#step-3-configure-language-mapping-in-crowdin}

アカウントを接続したら、Crowdinの各プロジェクト言語を対応するBrazeロケールにマッピングします。

1. **Braze キャンペーン & キャンバス**連携ダッシュボードで、上部アクションバーの**設定**歯車アイコンを選択します。

![上部アクションバーに設定が表示されているBraze キャンペーン & キャンバス連携画面。]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_settings.png %})

{: start="2"}
2. **General Settings**タブを開きます。
3. ロケールキーを入力します。Crowdinにはプロジェクト言語（例：フランス語、イタリア語）が一覧表示されます。各フィールドに、対応する**Brazeロケールキー**を入力します。
   - 例えば、Brazeでイタリア語に`it`を使用している場合、Crowdinのイタリア語の横に`it`と入力します。
   - 各エントリは、Brazeの**ローカライゼーション設定**のそのロケールの**ロケールキー**と正確に一致する必要があります。

![General Settingsタブの設定モーダル。ファイルフィルターフィールドと言語マッピング行（例：フランス語がfrにマッピング）が表示されています。]({% image_buster /assets/img/crowdin/crowdin_language_mapping_settings.png %})

{: start="4"}
4. **Save**を選択してマッピングを確定します。

### ステップ4:Brazeメッセージに翻訳タグを追加する {#step-4-add-translation-tags-to-your-braze-message}

Crowdinは、Brazeが多言語メッセージに使用するのと同じLiquid**翻訳タグ**を読み取ります。翻訳したいテキスト、画像URL、またはリンクURLの周囲に{% raw %}`{% translation your_id_here %}`と`{% endtranslation %}`{% endraw %}を追加します。各ブロックには一意の`id`が必要です（例：`greeting`や`welcome_header`）。

**例：**

{% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

HTML、リンク内のLiquid、およびその他のパターンについては、[ロケールの翻訳]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)と同じルールに従ってください（例：タグはできるだけ小さなセグメントを囲み、リンクをローカライズする際は言語固有の部分のみをラップします）。

Crowdinがコンテンツを検出してプルできるようにするには、Brazeメッセージを**下書き**として保存してください。

### ステップ5:Crowdinで翻訳を管理する {#step-5-manage-translations-in-crowdin}

連携画面には2つのパネルがあります。

- **Brazeパネル：** キャンペーンとキャンバス。
- **Crowdinパネル：** 翻訳用に同期済みのコンテンツ。

![キャンペーンとロケールのフォルダー、Sync to Braze、Sync to Crowdinが表示されているCrowdinとBraze キャンペーン & キャンバスのパネル。]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_sync_panels.png %})

#### コンテンツを同期する {#syncing-content}

1. **Braze**パネルで、翻訳するキャンペーンまたはキャンバスのチェックボックスを選択します。
2. **Sync to Crowdin**を選択します。
3. 同期が完了すると、**Crowdin**パネルにファイルが表示されます。翻訳者はCrowdinエディターで文字列を開くことができます。

#### 翻訳をBrazeに戻す {#returning-translations-to-braze}

1. Crowdinで翻訳が100%完了したら、**Integrations**タブに戻ります。
2. **Crowdin**パネルで完了したコンテンツを選択します。
3. **Sync to Braze**を選択します。これにより、翻訳された文字列がBrazeキャンペーンの対応する言語バリアントにプッシュされます。

### ステップ6:Brazeで多言語ユーザーとしてメッセージをプレビューする {#step-6-preview-the-message-as-a-multi-language-user-in-braze}

連携を確認するには：

1. **Brazeメッセージ作成画面**でキャンペーンを開きます。
2. **テスト**タブに移動します。
3. **ユーザーとしてメッセージをプレビュー**を選択します。
4. 翻訳済みロケールのいずれかに一致する`language`属性を持つユーザープロファイルを検索します。
5. コンテンツがソース言語から翻訳済みバージョンに切り替わることを確認します。

## Braze メールテンプレート連携 {#braze-email-templates-integration}

テンプレートレベルでメールをローカライズする場合は、[Braze メールテンプレートアプリ](https://store.crowdin.com/braze-app)を使用して、Braze メディアライブラリから HTML を同期します。

動画のウォークスルーについては、[Braze メールテンプレート連携](https://youtu.be/g0YMKW3jEjk)をご覧ください。

### ステップ1:アプリをインストールする {#step-1-install-the-app}

1. Crowdin プロジェクトで、**Store** タブに移動します。
2. **Braze Email Templates** を検索し、**Install** を選択します。

![Braze Email Templates が選択され、Install がハイライトされている Crowdin Store。]({% image_buster /assets/img/crowdin/crowdin_store_email_templates.png %})

{: start="3"}
3. この連携を使用するプロジェクトを選択します。
4. 連携を開くには、プロジェクトの **Integrations** > **Braze Email Templates** に移動します。

### ステップ2:Braze に接続する {#step-2-connect-to-braze}

Braze API 認証情報を使用して接続を認証します。

![REST APIキー、RESTエンドポイント、および Log in with Braze Email Templates が表示された Crowdin Braze メールテンプレート接続フォーム。]({% image_buster /assets/img/crowdin/crowdin_email_templates_login.png %}){: style="max-width:85%;"}

1. **Braze REST APIキー:** `templates.email` と `content_blocks`（読み取りおよび書き込み）を付与します。Braze の **設定** > **API と識別子** > **APIキー** でキーを作成します。

![Create API Key と REST エンドポイントのコピーコントロールが表示された Braze REST APIキーページ。]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %})

{: start="2"}
2. **Braze REST エンドポイント**には、インスタンス固有の URL を使用します（例: `https://rest.iad-03.braze.com`）。
3. **Log in with Braze Email Templates** を選択します。

### ステップ3:翻訳用コンテンツを同期する {#step-3-sync-content-for-translation}

連携画面には Braze ライブラリが表示されます。

- **Braze パネル:** 同期可能な**メールテンプレート**と **Content Blocks**。
- **Crowdin パネル:** 翻訳中のコンテンツ。

1. **Braze** パネルで、ローカライズするテンプレートまたはブロックの横にあるチェックボックスを選択します。
2. **Sync to Crowdin** を選択します。
3. Crowdin が HTML ソースを取得します。翻訳者は Crowdin エディターでライブ **WYSIWYG プレビュー**を使用して作業するため、レイアウトが維持されます。

![ローカライズされたメール HTML と翻訳可能な文字列が表示された Crowdin エディタープレビュータブ。]({% image_buster /assets/img/crowdin/crowdin_editor_wysiwyg_preview.png %}){: style="max-width:85%;"}

### ステップ4:翻訳済みテンプレートを配信する {#step-4-deliver-translated-templates}

翻訳が100%完了した場合:

1. **Crowdin** パネルで完了したファイルを選択します。
2. **Sync to Braze** を選択します。
3. Crowdin が Braze メディアライブラリにこれらのアセットのローカライズ版を自動的に作成します（例: `Template_Name_fr`）。

![メールテンプレートと Content Blocks が一覧表示され、Sync to Braze と Sync to Crowdin が表示された Crowdin と Braze メールテンプレートパネル。]({% image_buster /assets/img/crowdin/crowdin_email_templates_sync_panels.png %})