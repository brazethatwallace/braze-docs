---
nav_title: Lokalise
article_title: Lokalise
description: "この参考記事では、Brazeとアジャイルチーム向け翻訳管理サービスLokaliseのパートナーシップについて説明します。"
alias: /partners/lokalise/
page_type: partner
search_tag: Partner

---

# Lokalise

> [Lokalise](https://lokalise.com)は、アジャイルチーム向けの翻訳管理サービスです。

_この統合はLokaliseによって管理されています。_

## 統合について {#about-the-integration}

Lokaliseは、Brazeとの統合オプションを2つ提供しています。

- **多言語統合（推奨）**：Brazeの[多言語コンポジションAPI]({{site.baseurl}}/api/endpoints/translations/)を使用して、LokaliseとBraze間の直接的な双方向同期を提供します。この統合は、Campaigns、Canvases、メールテンプレートのローカライズされたメッセージバリアントに対応しており、プッシュ、メール、In-App Messagesの起動前および起動後のワークフローをサポートしています。
- **コネクテッドコンテンツ統合（レガシー）**：Brazeのコネクテッドコンテンツを使用して、ユーザーの言語設定に基づいて翻訳されたコンテンツを挿入します。

この記事では、両方の統合のセットアップについて説明します。

## 多言語統合（推奨） {#multi-language-integration-recommended}

多言語統合は、Brazeの多言語コンポジションAPIを使用して、Lokalise内で多言語Brazeコンテンツを管理するための効率的で自動化された方法を提供します。

### 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Lokaliseアカウント | このパートナーシップを活用するには、Lokaliseアカウントが必要です。 |
| Lokalise翻訳プロジェクト | **Marketing and support**タイプでLokaliseプロジェクトを作成し、**Content integration**として**Braze**を選択します。 |
| Braze多言語設定 | Brazeワークスペースで[多言語サポート]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings/)が有効になっている必要があります。 |
| Braze REST APIキー | Campaigns、Canvases、メールテンプレートの読み取りおよび更新権限を持つBraze REST APIキー。Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Brazeサーバーリージョン | お使いの[Brazeサーバーリージョン]({{site.baseurl}}/api/basics/#endpoints)（例：US-01、EU-01）。Brazeダッシュボードで確認できます。 |
| Brazeコンテンツ内の翻訳タグ | メッセージでは、翻訳可能なコンテンツを識別するために[翻訳タグ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/)を使用する必要があります。翻訳可能な各ブロックを、一意のIDを持つ{% raw %}`{% translation ID %}...{% endtranslation %}`{% endraw %}タグで囲みます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

### セットアップと使用方法 {#setup-and-usage}

Lokaliseでの Braze多言語統合の接続、コンテンツのインポート、翻訳、およびBrazeへの翻訳のエクスポートに関する詳細な手順については、[LokaliseのBraze統合ドキュメント](https://docs.lokalise.com/en/articles/13654162-braze)を参照してください。

この統合は以下をサポートしています：
- LokaliseとBraze間の直接的な双方向同期（手動のファイル処理不要）
- Campaigns、Canvases、メールテンプレートのローカライズされたメッセージバリアント
- 起動前および起動後の翻訳ワークフロー

{% alert note %}
Brazeで多言語用に設定され、翻訳タグで囲まれたコンテンツのみがLokaliseへのインポートに利用できます。翻訳が正しく同期されるためには、BrazeとLokaliseの両方で言語コードが正確に一致している必要があります。
{% endalert %}

## コネクテッドコンテンツ統合（レガシー） {#connected-content-integration-legacy}

レガシー統合は、Brazeのコネクテッドコンテンツを使用して、ユーザーの言語設定に基づいて翻訳されたコンテンツを挿入します。

### 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Lokaliseアカウント | このパートナーシップを活用するには、Lokaliseアカウントが必要です。 |
| Lokalise翻訳プロジェクト | **Software Localization**プロジェクトタイプでLokaliseプロジェクトを作成します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

### 新しいLokaliseプロジェクトを作成する {#create-a-new-lokalise-project}

新しい翻訳プロジェクトを作成するには、Lokaliseにログインして**New Project**を選択します。次に、プロジェクトに名前を付け、**Base Language**（翻訳元の言語）を選択し、1つ以上の**Target Languages**を追加し、**Software Localization**プロジェクトタイプを選択します。準備ができたら、**Proceed**をクリックします。

### 統合 {#integration}

Lokaliseで、Brazeで定義したコネクテッドコンテンツ変数ごとに翻訳キーを作成します。翻訳の準備ができたら、言語ごとに1つのJSONファイルを生成し、コネクテッドコンテンツを提供するURLに公開できます。

#### ステップ1：ユーザー言語を設定する {#step-1-configure-user-languages}

まだ設定していない場合は、Brazeダッシュボードを開いて**Users > User Import**に移動します。ここでユーザーをインポートできます。インポート用のCSVファイルを準備する際には、ユーザーの言語を記載した言語カラムを必ず含めてください。この言語フィールドは、後で翻訳を表示するときに使用されます。

{% alert important %}
使用する言語コードは、BrazeとLokaliseの両方で一致している必要があります。
{% endalert %}

#### ステップ2：Lokaliseで翻訳を準備する {#step-2-prepare-your-translations-on-lokalise}

次に、Lokaliseで翻訳を準備するには、Brazeのコネクテッドコンテンツ変数で使用しているのと同じ名前の翻訳キーを手動で作成する必要があります。

例えば、シンプルな翻訳キー`description`を作成してみましょう：
1. Lokaliseプロジェクトを開いて**Add Key**をクリックし、**Key**フィールドに「description」と入力します。
2. **Base Language Value**フィールドに「Demo description」と入力します。
3. **Platforms**のドロップダウンに「Web」を追加します。
4. 準備ができたら、**Save**をクリックします。

![]({% image_buster /assets/img/lokalise/1_add_key.png %}){: style="max-width:60%"}

プロジェクトエディターに翻訳キーが表示されます：

![]({% image_buster /assets/img/lokalise/2_translation_key_added.png %}){: style="max-width:90%"}

##### 既知の問題 {#known-issues}

- キーは**Web**プラットフォームに割り当てられている必要があります。
- ピリオド（`.`）や`_on`文字列を含むキーの使用は避けてください。たとえば、`this.is.the.key`の代わりに`this_is_the_key`を使用し、`join_us_on_instagram`の代わりに`join_us_instagram`を使用してください。

#### ステップ3：LokaliseでBrazeアプリを設定する {#step-3-configure-the-braze-app-on-lokalise}

Lokaliseプロジェクトを開いて**Apps**をクリックします。ここでBrazeアプリを検索してインストールします。以下の画面が表示されます：

![Lokalise上のBraze設定。プロジェクトIDと翻訳ファイルのURLが記載されています。]({% image_buster /assets/img/lokalise/3_lokalise_braze_app.png %})

**Translation File URL**では、Lokaliseがプロジェクト内のキーのすべての翻訳を含むJSONファイルを公開します。プロジェクトにあるターゲット言語の数だけ翻訳ファイルのURLが得られます。そのため、翻訳ファイルのURLは2つの部分で構成されています：

1. URLパスの最初の部分はすべての言語に共通です。
2. URL末尾のJSONファイル名は、言語コードに基づいています。

翻訳ファイルのURLは、Braze Campaignを設定する際に必要となるURLです。JSONファイルのコンテンツを更新するには**Refresh**をクリックします。URLは変更されないため、Brazeでコネクテッドコンテンツ呼び出しを変更する必要はありません。

##### テストURL {#test-url}

このURLをテストするには、URLをコピーし、{% raw %}`{{${language}}}`{% endraw %}を言語コード（たとえば`en`）に置き換えて、ブラウザでこのURLを開きます。キーと翻訳を含むJSONファイルが表示されます：

![]({% image_buster /assets/img/lokalise/4_testing_json_lokalise.png %})

#### ステップ4：Braze Campaignで翻訳を使用する {#step-4-use-translations-in-braze-campaign}

##### コネクテッドコンテンツ呼び出しを挿入する {#insert-connected-content-call}

準備ができたら、Brazeに戻り、既存のCampaignを開くか、新しいCampaignを作成します。この例では、サンプルコンテンツで新しいメールCampaignを作成します。**Edit Email Body**をクリックします。

翻訳を挿入するには、ドキュメントの最上部または翻訳が必要な最初の位置の直前に、HTML内にコネクテッドコンテンツリクエストを追加する必要があります。これは、以下のマークアップを挿入することで実現できます：

{% raw %}
`{% connected_content https://exports.live.lokalise.cloud/braze/123abc/456xyz/{{${language}}}.json :save translations %}`
{% endraw %}

`https://exports.live.lokalise.cloud/...` URLを、前のステップで取得した翻訳ファイルのURLに置き換えます。

{% raw %}

- `{{${language}}}`は、「この位置にユーザーの言語を挿入する」という意味です。あるいは、言語コードをハードコードすることもできます。たとえば、`en.json`のようにします。
  - 各ユーザーに適切な翻訳JSONファイルが取得されるようにするには、`{{${language}}}`プロファイル属性か、ユーザーの言語を保持する別の同様のカスタム属性を翻訳ファイルURLの末尾に配置する必要があります（たとえば、`/{{${language}}}.json`）。これらの属性に保持される値は、翻訳されたJSONファイルのそれぞれのプレフィックスと一致しなければなりません。これにより、各ユーザーに対して正しい翻訳ファイルが返されるようになります。
- `:save translations`により、JSONコンテンツがtranslations変数に保存されます。

##### 翻訳を表示する {#display-translations}

translations変数を使用して、必要な翻訳をキーで表示します。

たとえば、`description`キーを表示するには`{{ translations.description }}`を使用します。

{% endraw %}
![]({% image_buster /assets/img/lokalise/6_integration_usage_sample.png %})

最後に、メールテンプレートを保存し、プレビューします。翻訳が表示されるはずです。

## よくある質問 {#frequently-asked-questions}

### 誤ってLokaliseからキーを削除した場合はどうなりますか？ {#what-happens-if-i-accidentally-delete-a-key-from-lokalise}

Brazeの対応する文字列には翻訳が表示されなくなります。

### `en`ロケールを持っているが、Lokaliseで`en-US`で上書きした場合、Brazeは`en-US`として読み込みますか？ {#if-i-have-an-en-locale-but-override-it-with-en-us-on-lokalise-will-braze-read-it-as-en-us}

いいえ、ロケールのISOコードはBrazeとLokaliseで一致している必要があります。

### Lokaliseコンテンツを接続するときに`:rerender`フラグを使用できますか？ {#can-we-use-the-rerender-flag-when-connecting-lokalise-content}

はい、使用できます。このフラグの追加方法については、Brazeのドキュメントを参照してください。

### Lokaliseで翻訳ファイルを更新した後、Brazeで翻訳内容に変更が反映されないのはなぜですか？ {#after-refreshing-the-translation-file-on-lokalise-why-cant-i-see-any-changes-in-the-translated-content-on-braze}

Brazeでは翻訳コンテンツがキャッシュされ、その更新には数分かかることがあります。Campaignをテストしていて、翻訳の結果をすぐに確認する必要がある場合は、このリファレンス記事で説明されているように`:cache_max_age`パラメーターを使用できます。