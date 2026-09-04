---
nav_title: ローカライゼーション設定
article_title: ローカライゼーション設定
alias: "/multi_language_support/"
page_order: 4
description: "この記事では、Brazeダッシュボードの多言語設定の概要と、メッセージングでロケールを使用する方法について説明します。"
---

# ローカライゼーション設定 {#localization-settings}

> 多言語機能を使用すると、[翻訳タグ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)を使用して、単一のメッセージ内で異なる言語やロケーションのユーザーをターゲットにできます。

## 前提条件 {#prerequisites}

{% multi_lang_include messaging/localization/locales.md section='multi-language prerequisites' %}

## ロケールを追加する {#add-a-locale}

1. **設定** > **ローカライゼーション設定**に移動します。
2. **ロケールを追加**を選択し、**デフォルトのロケール**または**カスタム属性**を選択します。
3. ロケールの名前を入力します。
4. [アクセシビリティ用の言語を選択します]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#language-settings-and-accessibility)。この設定により、スクリーンリーダーなどの支援技術がテキストを正しく読み上げることができます。
5. 選択したロケールオプションに対応するユーザー属性を選択します。ロケールを設定する際は、デフォルトのユーザー属性またはカスタム属性から言語を選択できます。両方から選択することはできません。

{% tabs %}
{% tab Default locale %}

**デフォルトのロケール**の場合、ドロップダウンを使用して、追加する言語、およびオプションで言語に関連付ける国を選択します。

![言語と国を指定する「ロケールを追加 - デフォルト言語と国」というウィンドウ。]({% image_buster /assets/img/multi-language_support/default_option.png %})

{% endtab %}
{% tab カスタム属性 %}

**カスタム属性**の場合、ドロップダウンを使用して関連付けるカスタム属性を選択し、テキストフィールドに値を入力します。

![カスタム属性とその値を指定する「ロケールを追加 - カスタム属性」というウィンドウ。]({% image_buster /assets/img/multi-language_support/custom_attributes_option.png %})

{% endtab %}
{% endtabs %}

{: start="6"}
6. **ロケールを追加**を選択します。

メッセージでこれらのロケールを使用する手順については、[ロケールの使用]({{site.baseurl}}/locales_in_messages)を参照してください。

## 考慮事項 {#considerations}

- 単一のロケールで最大2つのカスタム属性、または最大2つのデフォルトユーザー属性言語を選択できます。いずれの場合も、2つ目の属性はオプションです。
- CSVファイルの翻訳値を編集する際は、ファイル内のデフォルト値を変更しないでください。
- アップロードしたファイルのロケールキーは、多言語設定のロケールキーと一致する必要があります。
- `device_locale`を`zh_CN`（中国本土で使用される簡体字中国語）に更新するには、プロジェクトに`zh_CN`ローカライゼーションファイルを追加する必要があります。iOSはネイティブで`zh-Hans`を使用するためです。

### サポートと優先順位 {#support-and-prioritization}

- ユーザーがカスタム属性で定義されたロケールとデフォルトのユーザー属性で定義されたロケールの両方に一致する場合、カスタム属性のロケールが優先されます。
- カスタム属性はテキスト（文字列）値の完全一致をサポートしています。
- カスタム属性が削除されたり、その型が変更されたりすると、ユーザーはそのロケールに該当しなくなり、該当するロケールの優先順位リストの次のロケールに移行するか、デフォルトのマーケティング翻訳を受け取ります。
- ロケールが無効な場合（カスタム属性が変更または削除された場合）、エラーは**多言語サポート**ページに表示されます。

## よくある質問 {#frequently-asked-questions}

### ロケールはいくつ追加できますか？ {#how-many-locales-can-i-add}

最大200のロケールを追加できます。

### 翻訳ファイルはBrazeのどこに保存されますか？ {#where-are-the-translation-files-stored-in-braze}

翻訳ファイルはキャンペーンレベルで保存されるため、各メッセージバリアントに翻訳をアップロードする必要があります。翻訳はContent Blocksにも保存できます。ブロックがメッセージに追加されると、その翻訳が自動的に含まれます。

### ロケール名は特定のパターンやフォーマットに従う必要がありますか？ {#does-the-locale-name-have-to-follow-a-specific-pattern-or-format}

いいえ。お好みの命名規則を使用できます。ロケール名はエディターでロケールを選択する際に使用され、翻訳IDを含むダウンロードファイルの見出しにも表示されます。