---
nav_title: 概要
page_order: 0
noindex: true
---

# レイアウト例：概要 {#example-layout-overview}

> 概要レイアウトは、ページの上部に特定のナビゲーションオプションを作成し、ユーザーがボタンをクリックしてページの特定の部分やまったく別のページに移動できるようにするのに適しています。

セレクターレイアウトの典型的な例は、[SDK変更ログ]({{site.baseurl}}/developer_guide/changelogs/)ページ、または[アプリ内メッセージクリエイティブ詳細ページ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/)です。

## 必要なコンポーネント {#required-components}

1. YAMLの開始表記と終了表記。つまり、コンテンツの前に---、コンテンツの後に---を記述します。
2. 特定のパラメーターの内容を引用符で囲みます。（ヘッダーパラメーター、テキストパラメーター、ハイフンやその他の特殊文字を含むコンテンツ）
3. 用語集タグの表記（これらはフィルタータグです）

## 必須パラメーター {#required-parameters}

| パラメーター | コンテンツタイプ | 詳細 |
|---|---|---|
| `page_order` | 数値 | セクション内でのページの順序を指定します。この順序は左側のナビゲーションに反映されます。 |
| `nav-title` | 英数字 | 左側のナビゲーションに表示されるタイトルです。 |
| `layout` | 英数字 - スペースなし | ドキュメントの[レイアウトセクション](https://github.com/Appboy/braze-docs/tree/develop/_layouts)からレイアウトを選択します。 |
| `guide_top_header` | 英数字 | ページにタイトルを付けます。|
| `guide_top_text` | 英数字 | ページの説明を記述します。ボタンとそのタイトルの真上に表示されます。内容を引用符で囲む必要があります。 |
| `guide_featured_title` | 英数字 | カードにタイトルを付けます。ボタンの真上に表示されます。
| `guide_featured_list` | YAML追加、英数字 | 下記の[ガイド掲載フォーマット](#guide-listing-format)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="必須パラメーター" }

### ガイド掲載フォーマット {#guide-listing-format}

| パラメーター | コンテンツタイプ | 詳細 |
|---|---|---|
| `name` | 英数字 | ボックスに名前を付けます。 |
| `link` | URLまたはパス | ボックスの移動先へのリンクです。完全なURL、または（内部リンクの場合は）`/docs...` を含める必要があります。 |
| `image` | パス | 画像の場所へのリンクです。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ガイド掲載フォーマット" }

フォーマットの例：

```yaml
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
```

## 例 {#example}

```yaml
---
nav_title: Creative Details
page_order: 4
layout: featured
guide_top_header: "Creative Details"
guide_top_text: "Get creative with our in-app messages! But you should know some of the guidelines, first! After all, you have to know those rules to break them! Check out the individual message type's Creative Specs or the global Creative Details below."

guide_featured_title: "Message Type Creative Specs"
guide_featured_list:
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
- name: Slideup
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#slideup
  image: /assets/img/braze_icons/arrow-circle-broken-up.svg
- name: Full-Screen
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#full-screen
  image: /assets/img/braze_icons/expand-05.svg
---

# Creative Details {#general}

Braze in-app messages have both global and individual creative specifications. For more information on our more customizable in-app message types, go to our [Customize]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/customize/) page.

{% alert important %}
  These details only apply to our most recent in-app message generation (Generation 3). If you are not using our newest generation of in-app messages, check out our [previous in-app message generations]({{ site.baseurl }}/help/best_practices/in-app_messages/previous_in-app_message_generations/) documentation.
{% endalert %}
```
