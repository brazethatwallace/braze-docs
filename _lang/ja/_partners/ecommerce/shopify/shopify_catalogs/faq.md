---
nav_title: FAQ
article_title: Shopify商品同期 FAQ
page_order: 0
page_type: FAQ
description: "このページでは、Shopify商品をBrazeカタログに同期する際のよくある質問への回答を提供します。"
---

# よくある質問 {#frequently-asked-questions}

> このページでは、[Shopify商品同期]({{site.baseurl}}/shopify_catalogs/)に関するよくある質問への回答を提供します。

## カタログと同期の動作 {#catalog-and-sync-behavior}

### BrazeでShopifyカタログを直接編集できますか？ {#can-i-edit-my-shopify-catalog-directly-in-braze}

いいえ。Shopifyカタログは、Brazeでは読み取り専用です。手動で編集しても、次回の同期で上書きされる可能性があります。商品の更新はすべてShopifyで直接行ってください。

### Shopifyカタログを削除するにはどうすればよいですか？ {#how-do-i-delete-my-shopify-catalog}

Shopifyカタログを削除するには、Shopifyパートナーページから同期を無効にしてください。**カタログ**ページからカタログを直接削除しないでください。無効にすると、同期されたすべてのタグ、コレクション、メタフィールドデータを含むカタログ全体が削除されます。無効にする前に、このカタログを参照しているキャンペーンやキャンバスを更新または一時停止してください。商品の詳細が欠落したメッセージが送信される可能性があります。

### Shopifyで以前同期した商品や商品フィールドを削除するとどうなりますか？ {#what-happens-if-i-delete-a-previously-synced-product-or-product-field-in-shopify}

Brazeは削除を検出すると、Shopifyカタログから商品またはフィールドを自動的に削除します。ただし、削除された商品やフィールドを参照しているキャンペーン、キャンバス、またはセグメントは正常に動作しなくなります。Shopifyで商品やフィールドを削除する前に、Brazeで使用されていないことを確認してください。

### カタログID（商品識別子）を変更するにはどうすればよいですか？ {#how-do-i-change-my-catalog-id-product-identifier}

カタログIDを変更するには、まず同期を無効にし、アクティブなメッセージがこのカタログデータを参照していないことを確認してください。その後、初期同期を再実行し、希望する識別子を選択してください。

### 同期するタグ、コレクション、またはメタフィールドを変更すると、アクティブなキャンペーンに影響しますか？ {#will-changing-my-synced-tags-collections-or-metafields-affect-active-campaigns}

はい。同期の選択を変更すると、それらを参照しているアクティブなキャンペーン、キャンバス、または[カタログセレクション]({{site.baseurl}}/catalog_selections/)に影響する可能性があります。変更を行う前に、アクティブなコンテンツが更新されていることを確認してください。

### 初期同期にはどのくらい時間がかかりますか？ {#how-long-does-the-initial-sync-take}

同期時間は、ストア内の商品とバリアントの数によって異なります。初期同期は商品をバッチで取得するため、すべての商品タグ、メタフィールド、コレクションの関連付けが表示されるまでに時間がかかる場合があります。同期ステータスはShopifyパートナーページで確認してください。

## 設定と制限 {#configuration-and-limits}

### タグ、コレクション、またはメタフィールドはいくつまで同期できますか？ {#how-many-tags-collections-or-metafields-can-i-sync}

設定ごとにそれぞれ最大20個まで同期できます。

- 商品タグ：最大20個
- コレクション：最大20個
- 商品メタフィールド：最大20個

### 商品が250を超えるコレクションに属している場合はどうなりますか？ {#what-if-a-product-belongs-to-more-than-250-collections}

Shopifyでは商品が250を超えるコレクションに属することが可能ですが、Brazeは商品ごとに最初の250件のコレクション関連付けのみを取得できます。選択したコレクションが最初に取得される250件の範囲外にある場合、その関連付けはShopifyカタログに反映されません。コレクションの関連付けが欠落していることに気づいた場合は、カスタマーサクセスマネージャーにお問い合わせください。

### 設定モーダルにすべてのコレクションが表示されないのはなぜですか？ {#why-dont-i-see-all-my-collections-in-the-configuration-modal}

設定モーダルには、最近更新されたコレクションのうち最大5,000件が表示されます。ストアがこの制限を超えている場合、古いコレクションは表示されないことがあります。上位5,000件の範囲外にある以前選択したコレクションは、引き続き選択内容に表示されます。

### 1つのカタログセレクションでタグとコレクションの両方でフィルタリングできますか？ {#can-i-filter-by-both-tags-and-collections-in-a-single-catalog-selection}

いいえ。カタログセレクションは、セレクションフィルターごとに1つの配列フィールドのみをサポートしています。同じセレクション内でタグとコレクションを組み合わせることはできません。タグとコレクションの両方の条件に基づいてユーザーをターゲットにする必要がある場合は、代わりにSQLクエリを使用した[セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)を使用してください。

### カタログセレクションの制限は何ですか？ {#what-are-the-catalog-selection-limits}

カタログセレクションには、標準のカタログセレクションと同じ制限が適用されます。アイテムの制限、フィルターの制約、ティアベースのストレージ上限の詳細については、[カタログセレクション]({{site.baseurl}}/catalog_selections/)を参照してください。

## メタフィールドとトラブルシューティング {#metafields-and-troubleshooting}

### 一部のメタフィールドタイプが表示されないのはなぜですか？ {#why-are-some-of-my-metafield-types-not-showing-up}

設定モーダルには、サポートされているメタフィールドタイプのみが表示されます。現在サポートされていないタイプは、`dimension`、`json`、`link`、`money`、`rating`、`rich_text_field`、`volume`、`weight`です。サポートされているタイプと完全なリストについては、Shopify商品同期ページの[Shopify商品メタフィールド]({{site.baseurl}}/shopify_catalogs/#shopify-product-metafields)を参照してください。

### 「Duplicate Metafield Column Name」エラーが発生しました。どうすればよいですか？ {#i-got-a-duplicate-metafield-column-name-error-what-do-i-do}

選択したメタフィールドのうち2つ以上が、カタログ内で同じカラム名を生成しようとしています。競合するメタフィールドの1つを選択解除するか、Shopifyでメタフィールドキーの名前を変更して、それぞれがユニークなカラム名にマッピングされるようにしてください。その後、設定を再保存してください。

### タグの読み込みに予想以上に時間がかかるのはなぜですか？ {#why-are-my-tags-taking-longer-than-expected-to-load}

タグは、設定モーダルを開いたときにShopifyから直接取得されます。ストアに大量の商品やタグがある場合、読み込みに時間がかかることがあります。これは想定される動作であり、同期のパフォーマンスには影響しません。読み込みが常にタイムアウトする場合は、Shopifyストアのタグの総数を減らすか、サポートにお問い合わせください。

## ストレージ {#storage}

### 追加の商品データを同期すると、カタログストレージに影響しますか？ {#will-syncing-additional-product-data-affect-my-catalog-storage}

はい。タグ、メタフィールド、コレクションを同期すると、カタログストレージの使用量が増加します。無料カタログティアには100 MBのストレージ制限があります。同期が制限を超えると、Brazeは同期を停止し、商品の更新が反映されなくなります。必要に応じて、アカウントマネージャーに連絡してティアをアップグレードしてください。