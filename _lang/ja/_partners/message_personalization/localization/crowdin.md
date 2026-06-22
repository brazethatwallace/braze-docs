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

## 統合について {#about-the-integration}

CrowdinはBraze向けに2つのアプリを提供しています：[Braze キャンペーン & キャンバス](https://store.crowdin.com/braze-content-translation)と[Braze Email Templates](https://store.crowdin.com/braze-app)です。ローカライズするBrazeの機能に応じて選択してください。以下の表で比較できます。

### 適切なCrowdinアプリの選択 {#choose-the-right-crowdin-app}

| チャネルまたは機能 | Braze キャンペーン & キャンバス | Braze Email Templates |
| --- | --- | --- |
| **キャンペーン** | ✅ 対応 | ❌ 非対応 |
| **キャンバスステップ** | ✅ 対応 | ❌ 非対応 |
| **メールテンプレート** | ❌ 非対応 | ✅ 対応 |
| **Content Blocks** | ❌ 非対応 | ✅ 対応 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="適切なCrowdinアプリの選択" }

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| --- | --- |
| **Crowdinアカウント** | [Crowdin.comアカウント](https://accounts.crowdin.com/register)または[Crowdin Enterpriseアカウント](https://accounts.crowdin.com/workspace/create)が必要です。 |
| **Crowdinプロジェクト** | Brazeを接続する前に、CrowdinまたはCrowdin Enterpriseで[翻訳プロジェクトを作成](https://support.crowdin.com/creating-project/)してください。 |
| **Braze REST APIキー** | キャンペーン、キャンバス、Content Blocks、カスタム属性、メール、テンプレートの権限を持つBraze REST APIキー。 |
| **Braze RESTエンドポイント** | お使いのBraze RESTエンドポイントURL（例：`https://rest.iad-03.braze.com`）。 |
| **Braze多言語設定** | Brazeダッシュボードの**設定** > **ローカライゼーション設定**でロケールを設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## Braze キャンペーン & キャンバス統合 {#braze-campaigns-canvas-integration}

ライブメッセージ内のコンテンツをローカライズする場合は、[Braze キャンペーン & キャンバスアプリ](https://store.crowdin.com/braze-content-translation)を使用して、キャンペーンやキャンバスの下書きから翻訳可能な文字列をBrazeの多言語サポートと同期します。

動画によるウォークスルーについては、[Braze キャンペーン & キャンバス integration](https://youtu.be/ahG1ET4VRKA)をご覧ください。

### ステップ 1:Brazeで多言語設定を行う {#step-1-set-up-multi-language-settings-in-braze}

Crowdinを接続する前に、Brazeでターゲット言語を追加します。

1. Brazeで、**設定** > **ローカライゼーション設定**に移動します。
2. サポートする予定の言語を追加します。

![Brazeの設定配下のロケールページ。ロケール名、ロケールキー、ロケールの追加が表示されています。]({% image_buster /assets/img/crowdin/braze_locales.png %})

{: start="3"}
3. 各**ロケールキー**（例：`en-US`、`fr-FR`、`es-ES`）をメモしてください。Crowdinで言語をマッピングする際にこれらの値を使用します。

### ステップ 2:CrowdinでBrazeプロジェクトを設定する {#step-2-set-up-the-braze-project-in-crowdin}

1. Crowdin EnterpriseまたはCrowdin.comアカウントで、左側メニューの**Store**に移動します。
2. **Braze キャンペーン & キャンバス**を検索し、**Install**を選択します。

![Crowdin StoreでBraze キャンペーン & キャンバスが選択され、Installがハイライトされている画面。]({% image_buster /assets/img/crowdin/crowdin_store_campaigns_canvas.png %})

{: start="3"}
3. この統合を使用するプロジェクトを選択します。
4. 統合を開くには、プロジェクトの**Integrations** > **Braze キャンペーン & キャンバス**に移動します。

#### BrazeをCrowdinに接続する {#connecting-braze-to-crowdin}

Braze API認証情報を使用して接続を認可します：

![CrowdinのBraze キャンペーン & キャンバス接続フォーム。REST APIキー、RESTエンドポイント、Log in with Braze キャンペーン & キャンバスが表示されています。]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_login.png %})

- **Braze REST APIキー：** Brazeの**設定** > **APIキー** > **APIキー**で作成します。この統合に必要な権限（キャンペーン、キャンバス、Content Blocks、カスタム属性）を付与してください。
- **Braze RESTエンドポイント：** お使いのBrazeインスタンスのURLを入力します（例：`https://rest.iad-03.braze.com`）。詳細については、[REST APIエンドポイント]({{site.baseurl}}/api/basics/#endpoints)を参照してください。

![Braze REST APIキーページ。APIキーの作成とRESTエンドポイントのコピーコントロールが表示されています。]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %})

**Log in with Braze キャンペーン & キャンバス**を選択します。

### ステップ 3:Crowdinで言語マッピングを設定する {#step-3-configure-language-mapping-in-crowdin}

アカウントを接続したら、Crowdinプロジェクトの各言語を対応するBrazeロケールにマッピングします。

1. **Braze キャンペーン & キャンバス**統合ダッシュボードで、右上の**Settings**歯車アイコンを選択します。

![Braze キャンペーン & キャンバス統合画面。上部のアクションバーにSettingsが表示されています。]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_settings.png %})

{: start="2"}
2. **General Settings**タブを開きます。
3. ロケールキーを入力します。Crowdinにはプロジェクトの言語（例：French、Italian）が一覧表示されます。各フィールドに、対応する**Brazeロケールキー**を入力します。
   - 例えば、Brazeでイタリア語に`it`を使用している場合、CrowdinのItalianの横に`it`と入力します。
   - 各エントリは、Brazeの**ローカライゼーション設定**にあるそのロケールの**ロケールキー**と正確に一致する必要があります。

![SettingsモーダルのGeneral Settingsタブ。ファイルフィルターフィールドと言語マッピング行（例：Frenchがfrにマッピング）が表示されています。]({% image_buster /assets/img/crowdin/crowdin_language_mapping_settings.png %})

{: start="4"}
4. **Save**を選択してマッピングを確定します。

### ステップ 4:Brazeメッセージに翻訳タグを追加する {#step-4-add-translation-tags-to-your-braze-message}

Crowdinは、Brazeが多言語メッセージに使用するのと同じLiquid**翻訳タグ**を読み取ります。翻訳したいテキスト、画像URL、リンクURLのすべてを {% raw %}`{% translation your_id_here %}`と`{% endtranslation %}`{% endraw %} で囲みます。各ブロックには一意の`id`（例：`greeting`や`welcome_header`）が必要です。

**例：**

{% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

HTML、リンク内のLiquid、その他のパターンについては、[ロケールの翻訳]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/)と同じルールに従ってください（例：タグはできるだけ小さなセグメントの周りに配置し、リンクをローカライズする際は言語固有の部分のみを囲みます）。

Crowdinがコンテンツを検出して取得できるように、Brazeメッセージを**下書き**として保存してください。

### ステップ 5:Crowdinで翻訳を管理する {#step-5-manage-translations-in-crowdin}

統合画面には2つの側面があります：

- **右側（Braze）：** キャンペーンとキャンバス。
- **左側（Crowdin）：** 翻訳用に同期済みのコンテンツ。

![CrowdinとBraze キャンペーン & キャンバスパネル。キャンペーンとロケールのフォルダーSync to Braze、Sync to Crowdinが表示されています。]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_sync_panels.png %})

#### コンテンツの同期 {#syncing-content}

1. **Braze（右側）**で、翻訳するキャンペーンまたはキャンバスのチェックボックスを選択します。
2. **Sync to Crowdin**を選択します。
3. 同期が完了すると、ファイルが**Crowdin（左側）**に表示されます。翻訳者はCrowdinエディターで文字列を開くことができます。

#### 翻訳をBrazeに戻す {#returning-translations-to-braze}

1. Crowdinで翻訳が100%完了したら、**Integrations**タブに戻ります。
2. **Crowdin（左側）**で完了したコンテンツを選択します。
3. **Sync to Braze**を選択します。これにより、翻訳された文字列がBraze キャンペーンの対応する言語バリアントにプッシュされます。

### ステップ 6:Brazeで多言語ユーザーとしてメッセージをプレビューする {#step-6-preview-the-message-as-a-multi-language-user-in-braze}

統合を確認するには：

1. **Brazeメッセージ作成画面**でキャンペーンを開きます。
2. **テスト**タブに移動します。
3. **ユーザーとしてメッセージをプレビュー**を選択します。
4. 翻訳済みロケールのいずれかに一致する`language`属性を持つユーザープロファイルを検索します。
5. コンテンツがソース言語から翻訳版に切り替わることを確認します。

## Braze Email Templates統合 {#braze-email-templates-integration}

テンプレートレベルでメールをローカライズする場合は、[Braze Email Templatesアプリ](https://store.crowdin.com/braze-app)を使用して、Brazeメディアライブラリから HTMLを同期します。

動画によるウォークスルーについては、[Braze Email Templates integration](https://youtu.be/g0YMKW3jEjk)をご覧ください。

### ステップ 1:アプリをインストールする {#step-1-install-the-app}

1. Crowdinプロジェクトで、**Store**タブに移動します。
2. **Braze Email Templates**を検索し、**Install**を選択します。

![Crowdin StoreでBraze Email Templatesが選択され、Installがハイライトされている画面。]({% image_buster /assets/img/crowdin/crowdin_store_email_templates.png %})

{: start="3"}
3. この統合を使用するプロジェクトを選択します。
4. 統合を開くには、プロジェクトの**Integrations** > **Braze Email Templates**に移動します。

### ステップ 2:Brazeに接続する {#step-2-connect-to-braze}

Braze API認証情報を使用して接続を認可します：

![CrowdinのBraze Email Templates接続フォーム。REST APIキー、RESTエンドポイント、Log in with Braze Email Templatesが表示されています。]({% image_buster /assets/img/crowdin/crowdin_email_templates_login.png %}){: style="max-width:85%;"}

1. **Braze REST APIキー：** `templates.email`と`content_blocks`（読み取りおよび書き込み）の権限を付与します。Brazeの**設定** > **APIキー** > **APIキー**でキーを作成します。

![Braze REST APIキーページ。APIキーの作成とRESTエンドポイントのコピーコントロールが表示されています。]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %})

{: start="2"}
2. **Braze RESTエンドポイント**には、インスタンス固有のURLを使用します（例：`https://rest.iad-03.braze.com`）。
3. **Log in with Braze Email Templates**を選択します。

### ステップ 3:翻訳用にコンテンツを同期する {#step-3-sync-content-for-translation}

統合画面にはBrazeライブラリが表示されます：

- **右側（Braze）：** 同期可能な**メールテンプレート**と**Content Blocks**。
- **左側（Crowdin）：** 翻訳中のコンテンツ。

1. **Braze（右側）**で、ローカライズしたいテンプレートまたはブロックの横にあるチェックボックスを選択します。
2. **Sync to Crowdin**を選択します。
3. CrowdinがHTMLソースを取得します。翻訳者はライブ**WYSIWYGプレビュー**付きのCrowdinエディターで作業できるため、レイアウトが維持されます。

![Crowdinエディターのプレビュータブ。ローカライズされたメールHTMLと翻訳可能な文字列が表示されています。]({% image_buster /assets/img/crowdin/crowdin_editor_wysiwyg_preview.png %}){: style="max-width:85%;"}

### ステップ 4:翻訳済みテンプレートを配信する {#step-4-deliver-translated-templates}

翻訳が100%完了したら：

1. **Crowdin（左側）**で完了したファイルを選択します。
2. **Sync to Braze**を選択します。
3. CrowdinがBrazeメディアライブラリにこれらのアセットのローカライズ版を自動的に作成します（例：`Template_Name_fr`）。

![CrowdinとBraze Email Templatesパネル。メールテンプレートとContent Blocksが一覧表示され、Sync to BrazeとSync to Crowdinが表示されています。]({% image_buster /assets/img/crowdin/crowdin_email_templates_sync_panels.png %})