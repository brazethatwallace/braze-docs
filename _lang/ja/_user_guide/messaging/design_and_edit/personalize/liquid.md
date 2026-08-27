---
nav_title: Liquidリファレンス
article_title: Liquidリファレンス
page_order: 3
layout: dev_guide
alias: /liquid/
search_rank: 3
guide_top_header: "Liquidリファレンス"
guide_top_text: "Liquidは、Shopifyが作成したオープンソースのテンプレート言語で、Brazeではダイナミックなパーソナライゼーションを実現するために使用されています。全員に同じ静的メッセージを送信する代わりに、Liquidを使えば各受信者のプロファイルデータ、行動、言語に基づいてコンテンツが変化するテンプレートを作成できます。このセクションの記事では、サポートされているタグ、フィルター、条件ロジック、デフォルト値、一般的なパーソナライゼーションパターンについて説明します。"
description: "このランディングページでは、サポートされているパーソナライゼーションタグ、フィルター、デフォルト値の設定など、Liquidに関するすべてを網羅しています。"

guide_featured_title: "セクション記事"
guide_featured_list:
- name: Liquidの使用
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid
  image: /assets/img/braze_icons/beaker-02.svg
- name: サポートされているパーソナライゼーションタグ
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags
  image: /assets/img/braze_icons/tag-01.svg
- name: オペレーター
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/operators
  image: /assets/img/braze_icons/code-02.svg
- name: フィルター
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/filters
  image: /assets/img/braze_icons/flag-02.svg
- name: 高度なフィルター
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters
  image: /assets/img/braze_icons/settings-01.svg
- name: デフォルト値を設定する
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values
  image: /assets/img/braze_icons/table.svg
- name: 条件付きメッセージングロジック
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic
  image: /assets/img/braze_icons/columns-01.svg
- name: メッセージの中止
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages
  image: /assets/img/braze_icons/refresh-ccw-01.svg
- name: Liquidユースケースライブラリ
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases
  image: /assets/img/braze_icons/list.svg
- name: チュートリアル
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/tutorials
  image: /assets/img/braze_icons/book-open-01.svg
- name: よくある質問
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/faq
  image: /assets/img/braze_icons/annotation-question.svg

---

## Liquidについて {#about-liquid}

Liquidは、メッセージとユーザーデータの間の橋渡し役として機能します。メッセージを送信すると、BrazeはテキストをスキャンしてLiquid構文を探します。Liquidが見つかると、その特定のユーザーに関連するデータを取得し、メッセージが送信される前にコードを実際の値に置き換えます。

たとえば、整数データ型であるカスタム属性をユーザープロファイルから取得し、その値を最も近い整数に丸めることができます。Liquidの構文と使用方法の詳細については、[**サポートされているパーソナライゼーションタグ**]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)を参照してください。

Liquidテンプレート言語は、オブジェクト、タグ、フィルターの使用をサポートしています。

- [**オブジェクト**]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)を使用すると、パーソナライズされた属性をメッセージに挿入できます。
- [**タグ**]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)を使用すると、メッセージングにデータを挿入し、特定の条件が満たされた場合にメッセージを送信する条件付きロジックを使用できます。たとえば、タグを使用して「if」文などのインテリジェントなロジックをキャンペーンに含めることができます。
- [**フィルター**]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters)を使用すると、パーソナライズされた属性やダイナミックなコンテンツを再フォーマットできます。たとえば、[`date`フィルター]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters#date-filter)を使用して、*2016-09-07 08:43:50 UTC*のようなタイムスタンプを、*2016年9月7日*のような日付に変換できます。

{% alert warning %}
Brazeは現在、ShopifyのLiquidを100%サポートしているわけではなく、ドキュメントで概説しようとした特定の部分のみをサポートしています。エラーやサポートされていないLiquidの使用リスクを軽減するため、送信前にLiquidを使用したすべてのメッセージをテストすることを強くお勧めします。
{% endalert %}

### Liquid 5のサポート {#liquid-5-support}

Brazeは、**ShopifyのLiquid 5**までをサポートしています。Liquidの実装は、構文パーソナライゼーションタグタイプとホワイトスペース制御をサポートしています。特定のタグの詳細については、[構文タグ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#syntax-tags)を参照してください。

以下の新しい配列フィルターおよび数学フィルターが、メッセージングの構築時にLiquidで使用できます。
- `at_least`
- `at_most`
- `compact`
- `concat`
- `sort_natural`
- `where`

定義については、[フィルター]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters)を参照してください。

## 知っておくべき用語 {#terms-to-know}

これらの用語は、Brazeのサポートレベルに基づいて[**Shopifyのドキュメント**](https://shopify.github.io/liquid/basics/introduction/)から再解釈されたものです。

{% raw %}

| 用語 | 定義 | 例 |
|---|---|---|
| Liquid | Shopifyが開発し、Rubyで記述された、広く使われている顧客向けのテンプレート言語で、ダイナミックなコンテンツの読み込みと取得に使用されます。 | `{{${first_name}}}`は、ユーザーの名をメッセージに挿入します。 |
| オブジェクト | 変数とその目的の変数名の位置を示す表記で、メッセージ内のどこにコンテンツを表示するかをLiquidに指示します。 | `{{${city}}}`は、ユーザーの市区町村をメッセージに挿入します。 |
| 条件ロジックタグ | ロジックを作成し、メッセージコンテンツのフローを制御するために使用されます。Brazeでは、条件ロジックタグは、特定の事前定義された基準に基づいてメッセージの例外やバリエーションを作成するために使用されます。 | ```{% if ${language} == 'en' %}```は、ユーザーが言語として「英語」を設定している場合に、メッセージを指定された方法でトリガーします。 |
| フィルター | Liquidオブジェクトの出力を変更、絞り込み、または再フォーマットするために使用されます。数学的演算の作成によく使用されます。 | ```{{"Big Sale" | upcase}}```は、「Big Sale」という文字をメッセージ内で「BIG SALE」と表示します。 |
| 演算子 | メッセージ内で依存関係や条件を作成するために使用され、ユーザーが受け取るメッセージに影響を与えます。 | `{% custom_attribute.${Total_Revenue} > 0%}`がタグ付けされたメッセージで、ユーザーが定義された条件を満たす場合、そのメッセージを受信します。満たさない場合は、設定内容に応じて、別の指定されたメッセージを受信する（または受信しない）ことになります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="知っておくべき用語" }

{% endraw %}

<br>