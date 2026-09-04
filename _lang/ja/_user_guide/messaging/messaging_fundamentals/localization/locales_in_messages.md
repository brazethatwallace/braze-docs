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
| メッセージタイプ | キャンペーンやキャンバスにロケールと翻訳を追加するには、以下の権限が必要です。<br><br> {::nomarkdown} <ul><li>Edit キャンペーン</li><li>Edit キャンバス</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件"}

{% endtab %}
{% tab テンプレート %}

| 機能 | 必要なユーザー権限 |
| --- | --- |
| テンプレート | ロケールと翻訳を追加するテンプレートタイプに応じて、以下の権限が必要です。<br><br> {::nomarkdown} <ul><li>Edit Email Templates</li><li>Edit IAM Templates</li><li>Edit Webhook Templates</li><li>Edit Content Block Templates</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

{% endtab %}
{% endtabs %}

## ロケールを使用する {#use-locales}

### ステップ1：ロケールを設定する {#step-1-set-up-locales}

メッセージに翻訳を追加する前に、まず[サポートしたいロケールを作成する]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings)必要があります。ロケールは、メッセージングで利用可能な言語（およびオプションで地域）のバリアントを定義します。

### ステップ2：翻訳するコンテンツをマークする {#step-2-mark-content-for-translation}

翻訳したいテキストを Liquid 翻訳タグ {% raw %}`{% translation your_id_here %}` と `{% endtranslation %}`{% endraw %} で囲み、タグ ID を割り当てます。翻訳タグ ID はメッセージ内で一意である必要があります。テキストを明確に説明するセマンティックな ID 名（{% raw %}`{% translation header %}`{% endraw %} など）の使用を検討してください。メッセージに Content Blocks が含まれている場合は、一意性の適用方法について[翻訳を含む Content Blocks](#content-blocks-containing-translation) を参照してください。

翻訳用にマークされたメッセージの例は次のとおりです：{% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

{% alert tip %}
翻訳したいテキストをハイライトし、キーボードショートカット **Cmd + Alt + L**（macOS）または **Ctrl + Alt + L**（Windows）を使用して翻訳タグで囲みます。<br><br>このショートカットは、メールおよび Content Blocks のドラッグ＆ドロップエディターを除く、多言語メッセージングをサポートするすべてのチャネルで機能します。これらのエディターでは、**パーソナライゼーションを追加**ボタンを使用して翻訳タグを追加してください。
{% endalert %}

#### URL をローカライズする {#localize-urls}

コンテンツを翻訳する際、URL はリンク切れを防ぐために特別な処理が必要です。

##### 標準（静的）URL {#standard-static-urls}

静的 URL はエディターで手動入力します（例：`https://example.com`）。以下も推奨します：

| 推奨事項 | 理由 |
| --- | --- |
| プロトコル（`https://`）は翻訳タグの外に置きます。ドメインとパスのみ（例：`example.com/en`）を囲みます。 | 翻訳者が特殊文字を誤って変更または削除し、リンク切れが発生する可能性があります。 |
| クエリパラメーター（例：`?utm_source=promo`）を翻訳タグ内に含めないでください。 | 翻訳者が特殊文字を誤って変更または削除し、リンク切れが発生する可能性があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="標準（静的）URL" }

両方の推奨事項に従った標準 URL は次のとおりです：

{% raw %}
```
<a href="https://{% translation id_1 %}example.shop.com{% endtranslation %}">Visit our store</a>
```
{% endraw %}

##### Liquid 生成 URL {#liquid-generated-urls}

URL が Liquid で生成される場合（例：{% raw %}`{% landing_page_url %}`{% endraw %}）、以下を推奨します：

| 推奨事項 | 理由 |
| --- | --- |
| Liquid 生成 URL を翻訳タグで囲むのは、ローカライズが必要な場合のみにしてください。 | Liquid 構文が正しくレンダリングされるようにするには、慎重に保持する必要があります。 |
| クエリパラメーター（例：`?utm_source=promo`）を翻訳タグ内に含めないでください。 | 翻訳者が特殊文字を誤って変更または削除し、リンク切れが発生する可能性があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liquid 生成 URL" }

両方の推奨事項に従った Liquid 生成 URL は次のとおりです：

{% raw %}
```
<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}">View details</a>
```
{% endraw %}

{% alert important %}
[メールリンクトラッキング](#email-link-tracking)（リンクエイリアスまたはリンクテンプレート）を使用している場合、URL を翻訳タグで囲む際に追加の設定が必要です。
{% endalert %}

#### HTML 属性と構造 {#html-attributes-and-structure}

翻訳タグで囲むのは、人間が読むテキストのみにしてください。HTML 属性（`class`、`style`、`id` など）やその他の構造コードは囲まないでください。HTML 属性はレイアウト、スタイリング、機能を制御します。翻訳タグで囲むと、ローカライズされたバージョンのメッセージでフォーマットやスタイルが崩れる可能性があります。

以下は正しく囲まれたテキストです：

{% raw %}
```
<p class="headline" style="color: red;">
  {% translation id_1 %}Welcome to our sale{% endtranslation %}
</p>
```
{% endraw %}

{% details 正しく囲まれていないテキスト %}

以下のテキストは**正しく囲まれていません**：

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

メッセージに翻訳タグを追加した後、エディターで**言語を管理**を選択し（メールおよび Content Blocks のドラッグ＆ドロップエディターでは**言語**）、翻訳を追加する少なくとも1つのロケールを選択します。

![デフォルトのロケールまたはカスタム属性を選択するオプションを含むロケール追加ドロップダウン。]({% image_buster /assets/img/multi-language_support/select_locale_type.png %}){: style="max-width:70%;"}

#### 翻訳を含む Content Blocks {#content-blocks-containing-translation}

翻訳タグを持つ Content Blocks は、ブロックに独自の保存済み翻訳があるかどうかによって動作が異なります：

| Content Block の状態 | 翻訳の管理場所 |
| --- | --- |
| 翻訳タグはあるが、ロケールや保存済み翻訳がない | 親メッセージの**言語を管理** CSV |
| ロケールと保存済み翻訳を含む翻訳タグ | Content Block 独自の CSV または翻訳 API |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Block の翻訳状態" }

##### 保存済み翻訳を持つ Content Blocks {#content-blocks-with-saved-translations}

メッセージに翻訳が既に保存されている Content Blocks が含まれている場合、それらの翻訳を再アップロードする必要はありません。保存済みの翻訳は、Content Block がメッセージに追加される際に自動的に適用されます。これらのブロックは独自のタグ ID を保持し、親メッセージに対して一意である必要はありません。ブロック自体に翻訳を保存する方法については、[Content Blocks に翻訳を保存する](#save-translations-in-content-blocks)を参照してください。

**言語を管理**モーダルでは、保存済みの翻訳を持つ Content Blocks がサポートするロケールとともにリストに表示されます。これにより、新しい翻訳を追加する前に、メッセージのどの部分が既にローカライズされているかを確認できます。

![保存済み翻訳を持つ Content Blocks のリストを含む言語を管理セクション。]({% image_buster /assets/img/multi-language_support/content_blocks_translations.png %}){: style="max-width:70%;"}

{% alert important %}
各 Content Block に、メッセージに追加されたすべてのロケールの翻訳が含まれていることを確認してください。追加したロケールのいずれかの翻訳が Content Block に欠けている場合、そのロケールのユーザーには元の言語で表示されます。
{% endalert %}

##### 翻訳タグのみを持つ Content Blocks {#content-blocks-with-translation-tags-only}

Content Block に翻訳タグはあるがロケールや保存済みの翻訳がない場合、そのタグは親メッセージ内で未翻訳のソースコンテンツとして扱われます。親の**言語を管理**エクスポートにはそれらのタグが含まれ、親の CSV でその翻訳を提供する必要があります。それらのタグは、親メッセージ内の他のタグに対して一意である必要があります。

未翻訳の Content Block を別のメッセージで再利用する場合、その2番目のメッセージでもブロックのタグの翻訳を提供する必要があります。Content Block を使用するすべてのメッセージで翻訳を提供する手間を省くには、Content Block 自体にロケールと翻訳を直接追加してください。

### ステップ4：翻訳を追加する {#step-4-add-translations}

ロケールを選択した後、以下のいずれかの方法でメッセージに翻訳を追加します：

![CSV でアップロードするか翻訳パートナーに接続するオプションを含む翻訳追加タブ。]({% image_buster /assets/img/multi-language_support/add_translations.png %}){: style="max-width:70%;"}

{% tabs %}
{% tab CSV テンプレートをアップロード %}

**テンプレートをダウンロード**を選択して、選択した翻訳 ID とロケールのマトリクスを含む CSV をダウンロードします。

{% alert important %}
英語以外の文字の表示問題を防ぐため、翻訳 CSV に Excel を使用しないでください。
{% endalert %}

テンプレートに入力する際は、各ロケールのテキストコンテンツのみを翻訳してください。ダウンロードしたテンプレートに HTML タグが含まれている場合は、それらを変更せず、タグ内のテキストのみを翻訳してください。

例えば、テンプレートに以下が含まれている場合：

```
<p style="margin:0;margin-bottom:0">A charming bakery dedicated to crafting artisanal breads.</p>
```

テキスト `A charming bakery dedicated to crafting artisanal breads.` のみを翻訳し、HTML タグ `<p style="margin:0;margin-bottom:0">` と `</p>` はそのままにしてください。

その後、完成したファイルをアップロードすると、翻訳がメッセージに適用されます。

![タイトル、オファーテキスト、オファー金額、CTA の翻訳タグを含む CSV。]({% image_buster /assets/img/multi-language_support/csv_template_example.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab 翻訳 API を使用 %}

パートナー翻訳 API を使用して、キャンペーン、キャンバス、Content Blocks、メールテンプレート、Webhook テンプレートの翻訳を管理および更新します。これは、ローカライゼーションに外部システムを使用している場合や、翻訳パートナーと直接接続したい場合に便利です。

キャンバスで翻訳エンドポイントを使用するには、以下のパラメーターを含めてください：
  - `workflow_id`
  - `step_id`
  - `message_variation_id`

{% alert note %}
キャンバスのローンチ後に作成されたキャンバスステップで翻訳 API を使用する場合、API に渡す `message_variation_id` は空またはブランクになります。
{% endalert %}

{% endtab %}
{% endtabs %}

### ステップ5：翻訳をプレビューする {#step-5-preview-translations}

メッセージをプレビューするには、**ユーザーとしてプレビュー**ドロップダウンから**多言語ユーザー**オプションを選択します。これにより、異なるロケール定義を切り替えて、メッセージのすべての翻訳をプレビューできます。

![ロケールプレビュー]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

## 翻訳の管理 {#manage-translations}

### キャンバスステップまたはキャンペーンの複製と翻訳 {#duplicate-canvas-steps-or-campaigns-and-translations}

キャンバスステップ、キャンペーン、またはバリアントを複製すると、翻訳も含まれます。ワークスペース間のコピーでも同様で、コピー先のワークスペースにロケールが定義されている場合に限ります。キャンバスやキャンペーンに変更を加える際は、翻訳を確認して適宜更新してください。

### Content Blocksに翻訳を保存する {#save-translations-in-content-blocks}

Content Blocksは、メッセージと同様に多言語対応をサポートしています。Content Blocksを作成または編集する際に、翻訳用のコンテンツにタグを付けたり、ロケールを追加したり、CSVまたは[翻訳API]({{site.baseurl}}/api/endpoints/translations)を使用して翻訳をアップロードしたりできます。

保存された翻訳はContent Blocksに関連付けられたままになります。ブロックをメッセージに追加すると、その翻訳も自動的に含まれます。

### 右から左に書く言語のメッセージ {#right-to-left-messages}

右から左に書く言語（アラビア語など）の翻訳ファイルに入力する際は、正しくフォーマットされるように翻訳を`span`で囲みます。

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

### メールのリンクトラッキング {#email-link-tracking}

メールキャンペーンでは、Brazeは各URLにトラッキング情報（クエリパラメーター）を追加することでリンクを追跡します。この動作は、[リンクエイリアス]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing)と[リンクテンプレート]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template)の両方をサポートしています。

URLが翻訳タグで囲まれている場合、Brazeはこのトラッキング情報を追加する場所を特定できないことがあります。これが正しく機能するようにするには、URLの末尾にトラッキングの追加場所を示す特殊文字を含める必要があります。

URLは、この動作を制御するために2つの特殊文字を使用します。
  - `?` はまだトラッキングがないURLにトラッキングを追加します。
  - `&` はURLに既に`?`がある場合に追加のトラッキングを加えます。URLに含められる`?`は1つだけです。

| URL | `?`を含む&nbsp;か | 説明 | 例 |
| --- | --- | --- | --- |
| 標準URL | いいえ | URLにまだ`?`が含まれていない場合、閉じ翻訳タグの後に`?`を追加します。 | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?">Shop Now</a>```{% endraw %} |
| 標準URL | はい | URLに既に`?`が含まれている場合、URLの末尾（閉じ翻訳タグの後）に`&`を使用します。 | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?ref=4&">Shop Now</a>```{% endraw %} |
| Liquid生成 | いいえ | 生成されたURLにまだ`?`が含まれていない場合、閉じ翻訳タグの後に`?`を使用します。 | {% raw %}```<a href="{% translation id_1 %}{{ product_url }}{% endtranslation %}?">Shop Now</a>``` {% endraw %} |
| Liquid生成 | はい | 生成されたURLに既に`?`が含まれている場合、閉じ翻訳タグの後に`&`を使用します。 | {% raw %}```<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}&">Shop Now</a>```{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="メールのリンクトラッキング" }

### 言語設定とアクセシビリティ {#language-settings-and-accessibility}

WCAGのコンテキスト、チャネルとエディターの動作（ランディングページを含む）、およびメッセージレベルの**アクセシビリティ**設定については、[アクセシビリティ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility)の[アクセシビリティ言語]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#accessibility-language)から始めてください。

**多言語メッセージ**を使用する場合は、ローカライズされた送信で適切な言語が宣言されるよう、アクセシビリティ言語を各ロケールに合わせてください。

#### アクセシビリティ言語の設定 {#configuring-the-accessibility-language}

アクセシビリティ言語は2つのレベルで設定できます。

##### メッセージレベル {#message-level}

メッセージレベルでは、メッセージ設定の**アクセシビリティ**セクションでアクセシビリティ言語を設定します。言語の選択、Liquidの使用、チャネルごとの制限については、[アクセシビリティ言語]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#accessibility-language)を参照してください。

##### ロケールレベル {#locale-level}

多言語メッセージの場合、**ローカライゼーション設定**で各ロケールのアクセシビリティ言語を設定します。**アクセシビリティ**セクションで{% raw %}`{{accessibility_language}}`{% endraw %}を使用すると、ドキュメントやカードの言語がこれらのロケール値にマッピングされます。

このトークンが新しいメッセージでデフォルトで表示されるかどうかは、チャネルとエディターによって異なります。たとえば、アプリ内メッセージやバナーはランディングページやドラッグ＆ドロップメールとは異なる動作をします。詳細については、[アクセシビリティ言語]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#accessibility-language)を参照してください。

## よくある質問 {#frequently-asked-questions}

### 翻訳タグの制限はどのようなものですか？ {#what-are-the-limits-for-translation-tags}

翻訳タグを使用する場合、以下の制限が適用されます。

- 各メッセージには最大200個の翻訳タグを設定できます。
- 各デフォルトテキスト（翻訳タグ間のコンテンツ）は最大2,000文字です。
- ロケールごとの翻訳は最大409,600バイト（約409.6&nbsp;KB）です。

### 多言語メールテンプレートをダウンロードするときにエラーが発生するのはなぜですか？ {#why-am-i-receiving-an-error-when-downloading-multi-language-email-templates}

多言語メールテンプレートのダウンロード時にエラーが発生する場合、翻訳タグがHTML属性やCSSスタイリングをラップしており、Brazeがメール本文を処理する方法と競合している可能性があります。

BrazeはHTML本文とプレーンテキスト本文を同じメッセージの別々のコンポーネントとして扱います。翻訳タグに`href`参照やCSSスタイリングが含まれていると、タグの競合が発生し、テンプレートが正しくダウンロードできなくなることがあります。

これを解決するには：
- `href`参照やCSSスタイリングを翻訳タグから除外してください。
- [HTML属性と構造](#html-attributes-and-structure)で説明されているように、人間が読めるテキストコンテンツのみを翻訳タグでラップしてください。
- URLについては、[URLのローカライズ](#localize-urls)のガイダンスに従ってください。

#### ロケールの1つで翻訳済みコピーを変更できますか？ {#can-i-make-a-change-to-the-translated-copy-in-one-of-my-locales}

はい。まずCSVで編集を行い、その後ファイルを再度アップロードして翻訳済みコピーを変更してください。

### Brazeは翻訳を提供しますか？ {#does-braze-provide-translations}

いいえ。CSVをアップロードするか、翻訳APIを使用して、[独自の翻訳を提供する](#step-4-add-translations)必要があります。

### 翻訳タグをネストできますか？ {#can-i-nest-translation-tags}

いいえ。

#### HTMLメッセージ全体を翻訳タグでラップできますか？ {#can-i-wrap-entire-html-messages-in-a-translation-tag}

いいえ。ベストプラクティスとして、人間が読めるテキストやローカライズが必要なコンテンツのみをラップしてください。これにより、壊れたフォーマット、リンク、またはその他の非テキスト要素を防ぐことができます。

さらに、正確な翻訳を作成し、パフォーマンスやサイズの制限を回避するために、意味的に関連するより小さなテキスト単位でラップすることを検討してください。

#### ロケールの1つで翻訳済みコピーを変更できますか？

はい。CSVを使用している場合は、まずファイルで編集を行い、その後再度アップロードして翻訳済みコピーを変更してください。[翻訳API]({{site.baseurl}}/api/endpoints/translations)を使用している場合は、更新エンドポイントを使用して変更を行ってください。

#### Brazeはどのようなバリデーションや追加チェックを行いますか？ {#what-validations-or-extra-checks-does-braze-do}

| シナリオ | Brazeでのバリデーション |
| --- | --- |
| メッセージに、異なるテキストにマッピングされた2つ以上の一致する翻訳IDが含まれている。 | この翻訳ファイルはダウンロードされません。 |
| 翻訳ファイルに1つ以上の翻訳タグIDが欠落している。 | この翻訳ファイルはアップロードされません。 |
| 翻訳ファイルにメッセージに存在しないロケールが含まれている。 | この翻訳ファイルはアップロードされません。 |
| 翻訳テンプレートをダウンロードする前に、翻訳タグをメッセージに追加する必要がある。 | この翻訳ファイルはダウンロードされません。 |
| アップロードしたファイルに含まれる翻訳タグがメッセージに存在しない。 | 余分な翻訳はメッセージに保存されません。 |
| {% raw %}メッセージに1つ以上の壊れたLiquidタグが含まれている。開始タグには`{% translation your_id_here %}`を使用し、翻訳タグは`{% endtranslation %}`で閉じてください。{% endraw %} | この翻訳ファイルはダウンロードされません。 |
| 翻訳ファイルにメッセージ内のテキストと一致しないデフォルトテキストが含まれている。 | 翻訳は追加されますが、元のメッセージテキストは更新されません。 |
| メッセージ内の1つ以上のロケールが設定で削除され、存在しなくなった。 | すでに追加された翻訳はメッセージ内に存在し続けます。メッセージから削除された場合、翻訳は失われます。 |
| 翻訳タグに完全なURLまたはLiquidで生成されたURLが含まれている。 | URLを含む翻訳タグは、リンク切れやリンクトラッキングの問題が発生した場合に備えて識別されます。 |
| 翻訳タグにクエリパラメーターが含まれている。 | クエリパラメーターを含む翻訳タグは、リンク切れやリンクトラッキングの問題が発生した場合に備えて識別されます。 |
| 翻訳タグにHTML属性や構造が含まれている。 | HTML属性や構造を含む翻訳タグは、スタイルやフォーマットの問題が発生した場合に備えて識別されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Brazeはどのようなバリデーションや追加チェックを行いますか？" }