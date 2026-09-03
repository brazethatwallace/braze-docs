---
nav_title: 多言語メッセージ
article_title: 多言語メッセージ
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "この記事では、メッセージでロケールを使用する方法について説明します。"
---

# 多言語メッセージ {#multi-language-messages}

> ワークスペースにロケールを追加すると、1つのプッシュ、メール、Webhook、バナー、アプリ内メッセージ、またはコンテンツブロックで、異なる言語のユーザーをターゲットにできます。

## 前提条件 {#prerequisites}

{% tabs %}
{% tab 多言語ロケール %}

{% multi_lang_include messaging/localization/locales.md section='multi-language prerequisites' %}

{% endtab %}
{% tab メッセージタイプ %}

| 機能 | 必要なユーザー権限 |
| --- | --- |
| メッセージ&nbsp;タイプ | キャンペーンやキャンバスにロケールと翻訳を追加するには、以下の権限が必要です。<br><br> {::nomarkdown} <ul><li>Edit キャンペーン</li><li>Edit キャンバス</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件"}

{% endtab %}
{% tab テンプレート %}

| 機能 | 必要なユーザー権限 |
| --- | --- |
| テンプレート | ロケールと翻訳を追加したいテンプレートタイプに応じて、以下の権限が必要です。<br><br> {::nomarkdown} <ul><li>Edit Email Templates</li><li>Edit IAM Templates</li><li>Edit Webhook Templates</li><li>Edit Content Block Templates</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

{% endtab %}
{% endtabs %}

## ロケールの使用 {#use-locales}

### ステップ1：ロケールを設定する {#step-1-set-up-locales}

メッセージに翻訳を追加する前に、まず[サポートしたいロケールを作成]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings)する必要があります。ロケールは、メッセージングに使用できる言語（およびオプションで地域）のバリアントを定義します。

### ステップ2：翻訳対象のコンテンツをマークする {#step-2-mark-content-for-translation}

翻訳したいテキストをLiquid翻訳タグ{% raw %}`{% translation your_id_here %}`と`{% endtranslation %}`{% endraw %}で囲み、タグIDを割り当てます。翻訳タグIDはメッセージ内で一意である必要があります。テキストをわかりやすく説明するセマンティックなID名の使用を検討してください（{% raw %}`{% translation header %}`{% endraw %}など）。

翻訳用にマークされたメッセージの例：{% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

{% alert tip %}
翻訳したいテキストをハイライトし、キーボードショートカット**Cmd + Alt + L**（macOS）または**Ctrl + Alt + L**（Windows）を使用して翻訳タグで囲みます。<br><br>このショートカットは、メールおよびContent Blocksのドラッグ＆ドロップエディターを除く、多言語メッセージングをサポートするすべてのチャネルで機能します。これらのエディターでは、**パーソナライゼーションを追加**ボタンを使用して翻訳タグを追加してください。
{% endalert %}

#### URLのローカライズ {#localize-urls}

コンテンツを翻訳する際、URLはリンク切れを防ぐために特別な処理が必要です。

##### 標準（静的）URL {#standard-static-urls}

静的URLはエディターに手動で入力します（例：`https://example.com`）。以下の点も推奨されます。

| 推奨事項 | 理由 |
| --- | --- |
| プロトコル（`https://`）は翻訳タグの外に保持してください。ドメインとパスのみを囲みます（例：`example.com/en`）。 | 翻訳者が誤って特殊文字を変更または削除し、リンク切れが発生する可能性があります。 |
| クエリパラメーター（例：`?utm_source=promo`）は翻訳タグの中に含めないでください。 | 翻訳者が誤って特殊文字を変更または削除し、リンク切れが発生する可能性があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="標準（静的）URL" }

両方の推奨事項に従った標準URLの例：

{% raw %}
```
<a href="https://{% translation id_1 %}example.shop.com{% endtranslation %}">Visit our store</a>
```
{% endraw %}

##### Liquid生成URL {#liquid-generated-urls}

URLがLiquidで生成される場合（例：{% raw %}`{% landing_page_url %}`{% endraw %}）、以下の点を推奨します。

| 推奨事項 | 理由 |
| --- | --- |
| Liquid生成URLは、ローカライズが必要な場合にのみ翻訳タグで囲んでください。 | Liquid構文は正しくレンダリングするために慎重に保持する必要があります。 |
| クエリパラメーター（例：`?utm_source=promo`）は翻訳タグの中に含めないでください。 | 翻訳者が誤って特殊文字を変更または削除し、リンク切れが発生する可能性があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liquid生成URL" }

両方の推奨事項に従ったLiquid生成URLの例：

{% raw %}
```
<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}">View details</a>
```
{% endraw %}

{% alert important %}
[メールリンクトラッキング](#email-link-tracking)（リンクエイリアスまたはリンクテンプレート）を使用している場合、URLが翻訳タグで囲まれているときは追加の設定が必要です。
{% endalert %}

#### HTML属性と構造 {#html-attributes-and-structure}

翻訳タグで囲むのは、人間が読めるテキストのみにしてください。HTML属性（`class`、`style`、`id`など）やその他の構造コードは囲まないようにしてください。HTML属性はレイアウト、スタイリング、機能を制御します。翻訳タグで囲むと、メッセージのローカライズ版でフォーマットやスタイルが壊れる可能性があります。

正しく囲まれたテキスト：

{% raw %}
```
<p class="headline" style="color: red;">
  {% translation id_1 %}Welcome to our sale{% endtranslation %}
</p>
```
{% endraw %}

{% details 誤って囲まれたテキスト %}

このテキストは**誤って**囲まれています：

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

### ステップ3：メッセージにロケールを追加する {#step-3-add-locales-to-your-message}

メッセージに翻訳タグを追加した後、エディターで**言語を管理**を選択し（メールおよびContent Blocksのドラッグ＆ドロップエディターでは**言語**）、翻訳を追加するロケールを少なくとも1つ選択します。

![デフォルトロケールまたはカスタム属性を選択するオプションがあるロケール追加のドロップダウン。]({% image_buster /assets/img/multi-language_support/select_locale_type.png %}){: style="max-width:70%;"}

#### 翻訳を含むContent Blocks {#content-blocks-containing-translation}

メッセージに既に翻訳が保存されたContent Blocksが含まれている場合、それらの翻訳を再アップロードする必要はありません。保存された翻訳は、Content Blocksがメッセージに追加されると自動的に適用されます。

**言語を管理**モーダルでは、保存された翻訳を持つContent Blocksが、サポートするロケールとともにリストに表示されます。これにより、新しい翻訳を追加する前に、メッセージのどの部分が既にローカライズされているかを確認できます。

![保存された翻訳を持つContent Blocksのリストが表示された「言語を管理」セクション。]({% image_buster /assets/img/multi-language_support/content_blocks_translations.png %}){: style="max-width:70%;"}

{% alert important %}
各Content Blocksに、メッセージに追加されたすべてのロケールの翻訳が含まれていることを確認してください。Content Blocksに追加したロケールの翻訳がない場合、そのロケールのユーザーには元の言語で表示されます。
{% endalert %}

### ステップ4：翻訳を追加する {#step-4-add-translations}

ロケールを選択した後、以下のいずれかの方法でメッセージに翻訳を追加します。

![CSVによるアップロードまたは翻訳パートナーへの接続で翻訳を追加するオプションがある「翻訳を追加」タブ。]({% image_buster /assets/img/multi-language_support/add_translations.png %}){: style="max-width:70%;"}

{% tabs %}
{% tab CSVテンプレートのアップロード %}

**テンプレートをダウンロード**を選択して、選択した翻訳IDとロケールのマトリックスを含むCSVをダウンロードします。

{% alert important %}
英語以外の文字の表示の問題を防ぐため、翻訳CSVにExcelを使用しないでください。
{% endalert %}

テンプレートに記入する際は、各ロケールのテキストコンテンツのみを翻訳してください。ダウンロードしたテンプレートにHTMLタグが含まれている場合は、それらを変更せず、タグ内のテキストのみを翻訳してください。

例えば、テンプレートに以下が含まれている場合：

```
<p style="margin:0;margin-bottom:0">A charming bakery dedicated to crafting artisanal breads.</p>
```

テキスト`A charming bakery dedicated to crafting artisanal breads.`のみを翻訳し、HTMLタグ`<p style="margin:0;margin-bottom:0">`と`</p>`はそのままにしてください。

その後、完成したファイルをアップロードすると、翻訳がメッセージに適用されます。

![タイトル、オファーテキスト、オファー金額、CTAの翻訳タグを含むCSV。]({% image_buster /assets/img/multi-language_support/csv_template_example.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab 翻訳APIの使用 %}

パートナー翻訳APIを使用して、キャンペーン、キャンバス、Content Blocks、メールテンプレート、Webhookテンプレートの翻訳を管理・更新できます。これは、外部システムでローカライゼーションを行っている場合や、翻訳パートナーと直接接続したい場合に便利です。

キャンバスで翻訳エンドポイントを使用するには、以下のパラメーターを含めてください：
  - `workflow_id`
  - `step_id`
  - `message_variation_id`

{% alert note %}
キャンバスの起動後に作成されたキャンバスステップで翻訳APIを使用する場合、APIに渡す`message_variation_id`は空またはブランクになります。
{% endalert %}

{% endtab %}
{% endtabs %}

### ステップ5：翻訳をプレビューする {#step-5-preview-translations}

メッセージをプレビューするには、**ユーザーとしてプレビュー**ドロップダウンから**多言語ユーザー**オプションを選択します。これにより、異なるロケール定義を切り替えて、メッセージのすべての翻訳をプレビューできます。

![ロケールプレビュー]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

## 翻訳の管理 {#manage-translations}

### キャンバスステップまたはキャンペーンの複製と翻訳 {#duplicate-canvas-steps-or-campaigns-and-translations}

キャンバスステップ、キャンペーン、またはバリアントを複製すると、翻訳も含まれます。ワークスペース間のコピーでも同様ですが、コピー先のワークスペースでロケールが定義されている必要があります。キャンバスやキャンペーンを変更する際は、翻訳を確認し、必要に応じて更新してください。

### Content Blocksに翻訳を保存する {#save-translations-in-content-blocks}

Content Blocksはメッセージと同じ方法で多言語をサポートしています。Content Blocksを作成または編集する際、翻訳対象のコンテンツにタグを付け、ロケールを追加し、CSVまたは[翻訳API]({{site.baseurl}}/api/endpoints/translations)を使用して翻訳をアップロードできます。

保存された翻訳はContent Blocksに関連付けられたままになります。ブロックがメッセージに追加されると、その翻訳も自動的に含まれます。

### 右から左に書く言語のメッセージ {#right-to-left-messages}

右から左に書く言語（アラビア語など）の翻訳ファイルを入力する際は、翻訳を`span`で囲み、適切にフォーマットされるようにしてください。

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

### メールのリンクトラッキング {#email-link-tracking}

メールキャンペーンでは、Brazeは各URLにトラッキング情報（クエリパラメーター）を追加してリンクをトラッキングします。この動作は[リンクエイリアス]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing)と[リンクテンプレート]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template)の両方をサポートしています。

URLが翻訳タグで囲まれている場合、Brazeはトラッキング情報を追加する場所を判断できないことがあります。これが正しく動作するようにするには、トラッキングを追加すべき場所を示す特殊文字をURLの末尾に含める必要があります。

URLでは、この動作を制御するために2つの特殊文字を使用します。
  - `?` はまだトラッキングがないURLにトラッキングを追加します。
  - `&` はURLにすでに`?`が含まれている場合に追加のトラッキングを追加します。URLに含めることができる`?`は1つだけです。

| URL | `?`を含む&nbsp; | 説明 | 例 |
| --- | --- | --- | --- |
| 標準URL | いいえ | URLにまだ`?`が含まれていない場合は、閉じ翻訳タグの後に`?`を追加します。 | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?">Shop Now</a>```{% endraw %} |
| 標準URL | はい | URLにすでに`?`が含まれている場合は、URLの末尾（閉じ翻訳タグの後）に`&`を使用します。 | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?ref=4&">Shop Now</a>```{% endraw %} |
| Liquid生成 | いいえ | 生成されたURLにまだ`?`が含まれていない場合は、閉じ翻訳タグの後に`?`を使用します。 | {% raw %}```<a href="{% translation id_1 %}{{ product_url }}{% endtranslation %}?">Shop Now</a>``` {% endraw %} |
| Liquid生成 | はい | 生成されたURLにすでに`?`が含まれている場合は、閉じ翻訳タグの後に`&`を使用します。 | {% raw %}```<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}&">Shop Now</a>```{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="メールのリンクトラッキング" }

### 言語設定とアクセシビリティ {#language-settings-and-accessibility}

WCAGのコンテキスト、チャネルとエディターの動作（ランディングページを含む）、およびメッセージレベルの**アクセシビリティ**設定については、[アクセシビリティ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility)の[アクセシビリティ言語]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#accessibility-language)から始めてください。

**多言語メッセージ**を使用する場合は、ローカライズされた送信が適切な言語を宣言するように、アクセシビリティ言語を各ロケールに合わせてください。

#### アクセシビリティ言語の設定 {#configuring-the-accessibility-language}

アクセシビリティ言語は2つのレベルで設定できます。

##### メッセージレベル {#message-level}

メッセージレベルでは、メッセージ設定の**アクセシビリティ**セクションでアクセシビリティ言語を設定します。言語の選択、Liquidの使用、チャネルごとの制限については、[アクセシビリティ言語]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#accessibility-language)を参照してください。

##### ロケールレベル {#locale-level}

多言語メッセージの場合、**ローカライゼーション設定**で各ロケールのアクセシビリティ言語を設定します。**アクセシビリティ**セクションで {% raw %}`{{accessibility_language}}`{% endraw %} を使用すると、ドキュメントまたはカードの言語がそれらのロケール値にマッピングされます。

新しいメッセージでそのトークンがデフォルトで表示されるかどうかは、チャネルとエディターによって異なります。たとえば、アプリ内メッセージやバナーは、ランディングページやドラッグ＆ドロップメールとは動作が異なります。詳細については、[アクセシビリティ言語]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#accessibility-language)を参照してください。

## よくある質問 {#frequently-asked-questions}

### 翻訳タグの制限は何ですか？ {#what-are-the-limits-for-translation-tags}

翻訳タグを使用する場合、以下の制限が適用されます。

- 各メッセージには最大200個の翻訳タグを含めることができます。
- 各デフォルトテキスト（翻訳タグ間のコンテンツ）は最大2,000文字です。
- ロケールごとの翻訳は最大409,600バイト（約409.6&nbsp;KB）です。

### 多言語メールテンプレートのダウンロード時にエラーが発生するのはなぜですか？ {#why-am-i-receiving-an-error-when-downloading-multi-language-email-templates}

多言語メールテンプレートのダウンロード時にエラーが発生する場合、翻訳タグがHTML属性やCSSスタイリングをラップしており、Brazeがメール本文を処理する方法と競合している可能性があります。

BrazeはHTML本文とプレーンテキスト本文を同じメッセージの別々のコンポーネントとして扱います。翻訳タグに`href`参照やCSSスタイリングが含まれていると、タグの競合が発生し、テンプレートが正しくダウンロードできなくなることがあります。

これを解決するには：
- `href`参照やCSSスタイリングを翻訳タグから除外してください。
- [HTML属性と構造](#html-attributes-and-structure)で説明されているように、人が読めるテキストコンテンツのみを翻訳タグでラップしてください。
- URLについては、[URLのローカライズ](#localize-urls)のガイダンスに従ってください。

#### ロケールの1つで翻訳済みコピーを変更できますか？ {#can-i-make-a-change-to-the-translated-copy-in-one-of-my-locales}

はい。まずCSVで編集を行い、その後ファイルを再度アップロードして翻訳済みコピーを変更してください。

### Brazeは翻訳を提供していますか？ {#does-braze-provide-translations}

いいえ。CSVをアップロードするか、翻訳APIを使用して、[独自の翻訳を提供する](#step-4-add-translations)必要があります。

### 翻訳タグをネストできますか？ {#can-i-nest-translation-tags}

いいえ。

#### HTMLメッセージ全体を翻訳タグでラップできますか？ {#can-i-wrap-entire-html-messages-in-a-translation-tag}

いいえ。ベストプラクティスとして、人が読めるテキストやローカライズが必要なコンテンツのみをラップしてください。これにより、フォーマットの崩れ、リンクの破損、その他のテキスト以外の要素の問題を防ぐことができます。

さらに、正確な翻訳を作成し、パフォーマンスやサイズの制限を回避するために、意味的に関連する小さなテキストの単位でラップすることを検討してください。

#### ロケールの1つで翻訳済みコピーを変更できますか？

はい。CSVを使用している場合は、まずファイルで編集を行い、その後再度アップロードして翻訳済みコピーを変更してください。[翻訳API]({{site.baseurl}}/api/endpoints/translations)を使用している場合は、更新エンドポイントを使用して変更を行ってください。

#### Brazeはどのようなバリデーションや追加チェックを行いますか？ {#what-validations-or-extra-checks-does-braze-do}

| シナリオ | Brazeでのバリデーション |
| --- | --- |
| メッセージに、異なるテキストにマッピングされる2つ以上の一致する翻訳IDが含まれている。 | この翻訳ファイルはダウンロードされません。 |
| 翻訳ファイルに1つ以上の翻訳タグIDが不足している。 | この翻訳ファイルはアップロードされません。 |
| 翻訳ファイルにメッセージに存在しないロケールが含まれている。 | この翻訳ファイルはアップロードされません。 |
| 翻訳テンプレートをダウンロードする前に、翻訳タグをメッセージに追加する必要がある。 | この翻訳ファイルはダウンロードされません。 |
| アップロードしたファイルに含まれる翻訳タグがメッセージに存在しない。 | 余分な翻訳はメッセージに保存されません。 |
| {% raw %}メッセージに1つ以上の壊れたLiquidタグが含まれている。開始タグには`{% translation your_id_here %}`を使用し、翻訳タグは`{% endtranslation %}`で閉じてください。{% endraw %} | この翻訳ファイルはダウンロードされません。 |
| 翻訳ファイルにメッセージ内のテキストと一致しないデフォルトテキストが含まれている。 | 翻訳は追加されますが、元のメッセージテキストは更新されません。 |
| メッセージ内の1つ以上のロケールが設定から削除され、存在しなくなっている。 | 既に追加された翻訳はメッセージ内に存在し続けます。メッセージから削除された場合、翻訳は失われます。 |
| 翻訳タグに完全なURLまたはLiquidで生成されたURLが含まれている。 | リンク切れやリンクトラッキングの問題が発生する可能性があるため、URLを含む翻訳タグが検出されます。 |
| 翻訳タグにクエリパラメーターが含まれている。 | リンク切れやリンクトラッキングの問題が発生する可能性があるため、クエリパラメーターを含む翻訳タグが検出されます。 |
| 翻訳タグにHTML属性や構造が含まれている。 | スタイルやフォーマットの問題が発生する可能性があるため、HTML属性や構造を含む翻訳タグが検出されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Brazeはどのようなバリデーションや追加チェックを行いますか？" }