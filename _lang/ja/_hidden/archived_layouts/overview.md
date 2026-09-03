---
nav_title: 概要
page_order: 0
noindex: true
---

# レイアウト例：概要 {#example-layout-overview}

> 概要レイアウトは、ページの上部に特定のナビゲーションオプションを作成し、ユーザーがボタンをクリックしてページの特定の部分やまったく別のページに移動できるようにするのに適しています。

セレクターレイアウトの典型的な例は、[SDK変更ログ]({{site.baseurl}}/developer_guide/changelogs)ページ、または[アプリ内メッセージクリエイティブ詳細ページ]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types)です。

## 必須コンポーネント

1. YAMLの開始および終了の記法。つまり、コンテンツの前に `---`、後に `---` を記述します。
2. 特定のパラメーターコンテンツにはクォーテーションを使用します。（ヘッダーパラメーター、テキストパラメーター、ハイフンやその他の特殊文字を含むコンテンツ。）
3. Glossary Tagsの記法（これらはフィルタータグです）

## 必須パラメータ

|パラメータ | コンテンツタイプ | 詳細 |
|---|---|---|
| `page_order`| 数値 | セクション内でのページの順序です。この順序は左側のナビゲーションに反映されます。 |
| `nav-title`| 英数字 | 左側のナビゲーションに表示されるタイトルです。 |
|`layout`| 英数字 - スペースなし | ドキュメントの[レイアウトセクション](https://github.com/Appboy/braze-docs/tree/develop/_layouts)からレイアウトを選択します。 |
| `guide_top_header`| 英数字 | ページのタイトルを設定します。|
| `guide_top_text`| 英数字 | ページの説明です。ボタンとそのタイトルの直上に表示されます。コンテンツは引用符で囲む必要があります。 |
| `guide_featured_title`| 英数字 | カードのタイトルを設定します。ボタンの直上に表示されます。
| `guide_featured_list`| YAML形式、英数字 | 以下の[ガイドリスト形式](#guide-listing-format)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="必須パラメータ" }

### ガイドリスト形式 {#guide-listing-format}

|パラメータ | コンテンツタイプ | 詳細 |
|---|---|---|
|`name`| 英数字 | ボックスの名前を設定します。 |
| `link`| URLまたはパス | ボックスのリンク先です。完全なURLまたは（内部リンクの場合）`/docs...` を含める必要があります。 |
|`image`| パス | 画像の場所へのリンクです。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ガイドリスト形式" }

フォーマット例：

```yaml
- name: Modal
  link: /docs/user_guide/channels/in_app_messages/message_types/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
```

```yaml
---
nav_title: クリエイティブの詳細
page_order: 4
layout: featured
guide_top_header: "クリエイティブの詳細"
guide_top_text: "アプリ内メッセージでクリエイティブに表現しましょう！ただし、まずいくつかのガイドラインを知っておく必要があります。ルールを破るには、まずルールを知っておかなければなりません！以下の個別のメッセージタイプのクリエイティブ仕様や、グローバルなクリエイティブの詳細をご覧ください。"

guide_featured_title: "メッセージタイプのクリエイティブ仕様"
guide_featured_list:
- name: モーダル
  link: /docs/user_guide/channels/in_app_messages/message_types/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
- name: スライドアップ
  link: /docs/user_guide/channels/in_app_messages/message_types/#slideup
  image: /assets/img/braze_icons/arrow-circle-broken-up.svg
- name: フルスクリーン
  link: /docs/user_guide/channels/in_app_messages/message_types/#full-screen
  image: /assets/img/braze_icons/expand-05.svg
---

# クリエイティブの詳細 {#general}

Brazeのアプリ内メッセージには、グローバルおよび個別のクリエイティブ仕様があります。よりカスタマイズ可能なアプリ内メッセージタイプの詳細については、[カスタマイズ]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/customize/)ページをご覧ください。

{% alert important %}
  これらの詳細は、最新のアプリ内メッセージ世代（第3世代）にのみ適用されます。最新世代のアプリ内メッセージを使用していない場合は、[以前のアプリ内メッセージ世代]({{ site.baseurl }}/help/best_practices/in-app_messages/previous_in-app_message_generations/)のドキュメントをご覧ください。
{% endalert %}