---
nav_title: 多言語メッセージ
article_title: 多言語メッセージ
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "この記事では、メッセージでロケールを使用する方法について説明します。"
---

# 多言語メッセージ {#multi-language-messages}

> ワークスペースにロケールを追加すると、1つのプッシュ、メール、バナー、アプリ内メッセージ、またはContent Blockで、異なる言語のユーザーをターゲットにできます。

## 前提条件 {#prerequisites}

多言語メッセージの設定と使用方法の概要については、以下の動画をご覧ください。

{% multi_lang_include video.html id="whfstwrel5" source="wistia" %}

{% tabs %}
{% tab 多言語ロケール %}

{% multi_lang_include messaging/localization/locales.md section='multi-language prerequisites' %}

{% endtab %}
{% tab メッセージタイプ %}

| 機能 | 必要なユーザー権限 |
| --- | --- |
| メッセージ&nbsp;タイプ | CampaignsおよびCanvasesにロケールと翻訳を追加するには、以下の権限が必要です。<br><br> <ul><li>Edit Campaigns</li><li>Edit Canvases</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件"}

{% endtab %}
{% tab テンプレート %}

| 機能 | 必要なユーザー権限 |
| --- | --- |
| テンプレート | ロケールと翻訳を追加するテンプレートタイプに応じて、以下の権限が必要です。<br><br> <ul><li>Edit Email Templates</li><li>Edit IAM Templates</li><li>Edit Content Block Templates</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

{% endtab %}
{% endtabs %}

## ロケールの使用 {#use-locales}

### ステップ1:ロケールを設定する {#step-1-set-up-locales}

メッセージに翻訳を追加する前に、まず[サポートするロケールを作成]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings)する必要があります。ロケールは、メッセージングで利用可能な言語（およびオプションで地域）のバリアントを定義します。

### ステップ2:翻訳するコンテンツをマークする {#step-2-mark-content-for-translation}

翻訳したいテキストをLiquid翻訳タグ {% raw %}`{% translation your_id_here %}`と`{% endtranslation %}`{% endraw %} で囲み、タグIDを割り当てます。翻訳タグIDはメッセージ内で一意である必要があります。テキストを明確に説明するセマンティックなID名の使用を検討してください（例: {% raw %}`{% translation header %}`{% endraw %}）。

翻訳用にマークされたメッセージの例: {% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

{% alert tip %}
翻訳したいテキストをハイライトし、キーボードショートカット **Cmd + Alt + L**（macOS）または **Ctrl + Alt + L**（Windows）を使用して翻訳タグで囲みます。<br><br> このショートカットは、メールおよびContent Blocksのドラッグ＆ドロップエディターを除く、多言語メッセージングをサポートするすべてのチャネルで使用できます。これらのエディターでは、左サイドバーの**パーソナライゼーションを追加**ボタンを使用して翻訳タグを追加してください。
{% endalert %}

#### URLのローカライズ {#localize-urls}

コンテンツを翻訳する際、URLにはリンク切れを防ぐための特別な処理が必要です。

##### 標準（静的）URL {#standard-static-urls}

静的URLはエディターで手動入力します（例: `https://example.com`）。以下の推奨事項もご確認ください。

| 推奨事項 | 理由 |
| --- | --- |
| プロトコル（`https://`）は翻訳タグの外に置いてください。ドメインとパスのみを囲みます（例: `example.com/en`）。 | 翻訳者が特殊文字を誤って変更または削除し、リンク切れの原因となる可能性があります。 |
| クエリパラメーター（例: `?utm_source=promo`）は翻訳タグ内に含めないでください。 | 翻訳者が特殊文字を誤って変更または削除し、リンク切れの原因となる可能性があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="標準（静的）URL" }

両方の推奨事項に従った標準URLの例:

{% raw %}
```
<a href="https://{% translation id_1 %}example.shop.com{% endtranslation %}">Visit our store</a>
```
{% endraw %}

##### Liquidで生成されるURL {#liquid-generated-urls}

URLがLiquidで生成される場合（例: {% raw %}`{% landing_page_url %}`{% endraw %}）、以下を推奨します。

| 推奨事項 | 理由 |
| --- | --- |
| Liquidで生成されるURLは、ローカライズが必要な場合のみ翻訳タグで囲んでください。 | Liquid構文は正しくレンダリングするために慎重に保持する必要があります。 |
| クエリパラメーター（例: `?utm_source=promo`）は翻訳タグ内に含めないでください。 | 翻訳者が特殊文字を誤って変更または削除し、リンク切れの原因となる可能性があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liquidで生成されるURL" }

両方の推奨事項に従ったLiquid生成URLの例:

{% raw %}
```
<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}">View details</a>
```
{% endraw %}

{% alert important %}
[メールリンクトラッキング](#email-link-tracking)（リンクエイリアスまたはリンクテンプレート）を使用している場合、URLを翻訳タグで囲む際に追加の設定が必要です。
{% endalert %}

#### HTML属性と構造 {#html-attributes-and-structure}

翻訳タグで囲むのは、人間が読むテキストのみにしてください。HTML属性（`class`、`style`、`id`など）やその他の構造コードを囲むことは避けてください。HTML属性はレイアウト、スタイル、機能を制御します。翻訳タグで囲むと、ローカライズ版のメッセージでフォーマットやスタイルが崩れる可能性があります。

正しく囲まれたテキスト:

{% raw %}
```
<p class="headline" style="color: red;">
  {% translation id_1 %}Welcome to our sale{% endtranslation %}
</p>
```
{% endraw %}

{% details 正しくない囲み方 %}

このテキストは**正しくない**囲み方です:

{% raw %}
```
{% translation id_1 %}
<p class="headline" style="color: red;">
  Welcome to our sale
</p>
{% endtranslation %}
```
{% endraw %}

{% enddetails %}

### ステップ3:メッセージにロケールを追加する {#step-3-add-locales-to-your-message}

メッセージに翻訳タグを追加した後、エディターで**言語を管理**を選択し（メールおよびContent Blocksのドラッグ＆ドロップエディターでは**言語**）、翻訳を追加するロケールを少なくとも1つ選択します。

![デフォルトロケールまたはカスタム属性を選択するオプションを含むロケール追加ドロップダウン。]({% image_buster /assets/img/multi-language_support/select_locale_type.png %}){: style="max-width:70%;"}

#### 翻訳を含むContent Blocks {#content-blocks-containing-translation}

メッセージに翻訳が保存済みのContent Blocksが含まれている場合、それらの翻訳を再アップロードする必要はありません。保存された翻訳は、Content Blockがメッセージに追加されると自動的に適用されます。

**言語を管理**モーダルでは、翻訳が保存されたContent Blocksが、サポートするロケールとともにリストに表示されます。これにより、新しい翻訳を追加する前に、メッセージのどの部分がすでにローカライズされているかを確認できます。

![翻訳が保存されたContent Blocksのリストを含む「言語を管理」セクション。]({% image_buster /assets/img/multi-language_support/content_blocks_translations.png %}){: style="max-width:70%;"}

{% alert important %}
各Content Blockに、メッセージに追加したすべてのロケールの翻訳が含まれていることを確認してください。Content Blockに追加したロケールの翻訳がない場合、そのロケールのユーザーには元の言語で表示されます。
{% endalert %}

### ステップ4:翻訳を追加する {#step-4-add-translations}

ロケールを選択した後、以下のいずれかの方法でメッセージに翻訳を追加します。

![CSVによるアップロードまたは翻訳パートナーへの接続による翻訳追加オプションを含む「翻訳を追加」タブ。]({% image_buster /assets/img/multi-language_support/add_translations.png %}){: style="max-width:70%;"}

{% tabs %}
{% tab CSVテンプレートをアップロード %}

**テンプレートをダウンロード**を選択して、選択した翻訳IDとロケールのマトリクスを含むCSVをダウンロードします。各ロケールの翻訳を入力してください。完成したファイルをアップロードすると、翻訳がメッセージに適用されます。

{% alert important %}
英語以外の文字の表示問題を防ぐため、翻訳CSVにExcelを使用しないでください。
{% endalert %}

![タイトル、オファーテキスト、オファー金額、CTAの翻訳タグを含むCSV。]({% image_buster /assets/img/multi-language_support/csv_template_example.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab 翻訳APIを使用 %}

パートナー翻訳APIを使用して、CampaignsおよびCanvasesの翻訳を管理・更新します。これは、外部システムでローカライゼーションを行っている場合や、翻訳パートナーと直接接続したい場合に便利です。

Canvasesで翻訳エンドポイントを使用するには、以下のパラメーターを含めてください。
  - `workflow_id`
  - `step_id`
  - `message_variation_id`

{% alert note %}
Canvasの起動後に作成されたキャンバスステップで翻訳APIを使用する場合、APIに渡す`message_variation_id`は空またはブランクになります。
{% endalert %}

{% endtab %}
{% endtabs %}

### ステップ5:翻訳をプレビューする {#step-5-preview-translations}

メッセージをプレビューするには、**ユーザーとしてプレビュー**ドロップダウンから**多言語ユーザー**オプションを選択します。これにより、異なるロケール定義を切り替えて、メッセージのすべての翻訳をプレビューできます。

![ロケールプレビュー]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

## 翻訳の管理 {#manage-translations}

### キャンバスステップまたはCampaignsの複製と翻訳 {#duplicate-canvas-steps-or-campaigns-and-translations}

キャンバスステップ、Campaign、またはバリアントを複製すると、翻訳も含まれます。これはワークスペース間のコピーでも同様で、コピー先のワークスペースにロケールが定義されている場合に適用されます。CanvasまたはCampaignに変更を加える際は、翻訳を確認し、必要に応じて更新してください。

### Content Blocksに翻訳を保存する {#save-translations-in-content-blocks}

Content Blocksは、メッセージと同じ方法で多言語をサポートします。Content Blocksを作成または編集する際に、コンテンツに翻訳タグを付け、ロケールを追加し、CSVまたは[翻訳API]({{site.baseurl}}/api/endpoints/translations)を使用して翻訳をアップロードできます。

保存された翻訳はContent Blockに関連付けられたままです。ブロックがメッセージに追加されると、その翻訳が自動的に含まれます。

### 右から左に書くメッセージ {#right-to-left-messages}

右から左に書く言語（アラビア語など）の翻訳ファイルを入力する際は、翻訳を`span`で囲んで適切にフォーマットされるようにしてください。

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

### メールリンクトラッキング {#email-link-tracking}

メールCampaignsでは、Brazeは各URLにトラッキング情報（クエリパラメーター）を追加してリンクを追跡します。この動作は[リンクエイリアス]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing)と[リンクテンプレート]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template)の両方をサポートしています。

URLが翻訳タグで囲まれている場合、Brazeはトラッキング情報を追加する場所を判断できない場合があります。これが正しく機能するようにするには、URLの末尾にトラッキングを追加する場所を示す特殊文字を含める必要があります。

URLは2つの特殊文字を使用してこの動作を制御します。
  - `?`はまだトラッキングがないURLにトラッキングを追加します。
  - `&`はURLにすでに`?`が含まれている場合に追加のトラッキングを追加します。URLには`?`を1つだけ含めることができます。

| URL | `?`を含む | 説明 | 例 |
| --- | --- | --- | --- |
| 標準URL | いいえ | URLにまだ`?`が含まれていない場合、閉じ翻訳タグの後に`?`を追加します。 | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?">Shop Now</a>```{% endraw %} |
| 標準URL | はい | URLにすでに`?`が含まれている場合、URLの末尾（閉じ翻訳タグの後）に`&`を使用します。 | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?ref=4&">Shop Now</a>```{% endraw %} |
| Liquid生成 | いいえ | 生成されたURLにまだ`?`が含まれていない場合、閉じ翻訳タグの後に`?`を使用します。 | {% raw %}```<a href="{% translation id_1 %}{{ product_url }}{% endtranslation %}?">Shop Now</a>``` {% endraw %} |
| Liquid生成 | はい | 生成されたURLにすでに`?`が含まれている場合、閉じ翻訳タグの後に`&`を使用します。 | {% raw %}```<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}&">Shop Now</a>```{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="メールリンクトラッキング" }

### 言語設定とアクセシビリティ {#language-settings-and-accessibility}

まず[アクセシビリティ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility)の[アクセシビリティ言語]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#accessibility-language)を参照して、WCAGのコンテキスト、チャネルとエディターの動作（ランディングページを含む）、およびメッセージレベルの**アクセシビリティ**設定をご確認ください。

**多言語メッセージ**を使用する場合、ローカライズされた送信が適切な言語を宣言するように、アクセシビリティ言語を各ロケールに合わせてください。

#### アクセシビリティ言語の設定 {#configuring-the-accessibility-language}

アクセシビリティ言語は2つのレベルで設定できます。

##### メッセージレベル {#message-level}

メッセージレベルでは、メッセージ設定の**アクセシビリティ**セクションでアクセシビリティ言語を設定します。言語の選択、Liquidの使用、チャネルごとの制限については、[アクセシビリティ言語]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#accessibility-language)を参照してください。

##### ロケールレベル {#locale-level}

多言語メッセージの場合、**ローカライゼーション設定**で各ロケールにアクセシビリティ言語を設定します。**アクセシビリティ**セクションで {% raw %}`{{accessibility_language}}`{% endraw %} を使用すると、ドキュメントまたはカードの言語がそれらのロケール値にマッピングされます。

新しいメッセージでそのトークンがデフォルトで表示されるかどうかは、チャネルとエディターによって異なります。たとえば、アプリ内メッセージやバナーは、ランディングページやドラッグ＆ドロップメールとは動作が異なります。詳細については、[アクセシビリティ言語]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#accessibility-language)を参照してください。

## よくある質問 {#frequently-asked-questions}

### 翻訳タグの制限は何ですか？ {#what-are-the-limits-for-translation-tags}

翻訳タグを使用する場合、以下の制限が適用されます。

- 各メッセージには最大200個の翻訳タグを使用できます。
- 各デフォルトテキスト（翻訳タグ間のコンテンツ）は最大2,000文字です。
- ロケールごとの翻訳は最大409,600バイト（約409.6&nbsp;KB）です。

#### ロケールの1つで翻訳済みコピーを変更できますか？ {#can-i-make-a-change-to-the-translated-copy-in-one-of-my-locales}

はい。まずCSVで編集を行い、ファイルを再度アップロードして翻訳済みコピーを変更します。

### Brazeは翻訳を提供しますか？ {#does-braze-provide-translations}

いいえ。CSVのアップロードまたは翻訳APIを使用して、[ご自身で翻訳を提供](#step-4-add-translations)する必要があります。

### 翻訳タグをネストできますか？ {#can-i-nest-translation-tags}

いいえ。

#### HTMLメッセージ全体を翻訳タグで囲むことはできますか？ {#can-i-wrap-entire-html-messages-in-a-translation-tag}

いいえ。ベストプラクティスとして、人間が読むテキストまたはローカライズが必要なコンテンツのみを囲むべきです。これにより、フォーマット、リンク、その他の非テキスト要素の破損を防ぐことができます。

また、正確な翻訳を作成し、パフォーマンスやサイズの制限を回避するために、意味的に関連する小さなテキスト単位で囲むことを検討してください。

#### ロケールの1つで翻訳済みコピーを変更できますか？

はい。CSVを使用している場合は、まずファイルで編集を行い、再度アップロードして翻訳済みコピーを変更します。[翻訳API]({{site.baseurl}}/api/endpoints/translations)を使用している場合は、更新エンドポイントを使用して変更を行います。

#### Brazeはどのような検証や追加チェックを行いますか？ {#what-validations-or-extra-checks-does-braze-do}

| シナリオ | Brazeでの検証 |
| --- | --- |
| メッセージに、異なるテキストにマッピングされた2つ以上の一致する翻訳IDが含まれている。 | この翻訳ファイルはダウンロードされません。 |
| 翻訳ファイルに1つ以上の翻訳タグIDが欠けている。 | この翻訳ファイルはアップロードされません。 |
| 翻訳ファイルにメッセージに存在しないロケールが含まれている。 | この翻訳ファイルはアップロードされません。 |
| 翻訳テンプレートをダウンロードする前に、メッセージに翻訳タグを追加する必要がある。 | この翻訳ファイルはダウンロードされません。 |
| アップロードしたファイルに含まれる翻訳タグがメッセージに存在しない。 | 余分な翻訳はメッセージに保存されません。 |
| {% raw %}メッセージに1つ以上の壊れたLiquidタグが含まれている。開始タグには`{% translation your_id_here %}`を使用し、翻訳タグは`{% endtranslation %}`で閉じてください。{% endraw %} | この翻訳ファイルはダウンロードされません。 |
| 翻訳ファイルにメッセージ内のテキストと一致しないデフォルトテキストが含まれている。 | 翻訳は追加されますが、元のメッセージテキストは更新されません。 |
| メッセージ内の1つ以上のロケールが設定で削除され、存在しなくなった。 | すでに追加された翻訳はメッセージ内に引き続き存在します。メッセージから削除すると、翻訳は失われます。 |
| 翻訳タグに完全なURLまたはLiquid生成URLが含まれている。 | リンク切れやリンクトラッキングの問題が発生する可能性があるため、URLを含む翻訳タグが識別されます。 |
| 翻訳タグにクエリパラメーターが含まれている。 | リンク切れやリンクトラッキングの問題が発生する可能性があるため、クエリパラメーターを含む翻訳タグが識別されます。 |
| 翻訳タグにHTML属性または構造が含まれている。 | スタイルやフォーマットの問題が発生する可能性があるため、HTML属性または構造を含む翻訳タグが識別されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Brazeはどのような検証や追加チェックを行いますか？" }