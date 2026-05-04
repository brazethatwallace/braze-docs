---
nav_title: ランディングページのパーソナライズ
article_title: ランディングページのパーソナライズ
description: "この記事では、ドラッグ＆ドロップエディターを使用してBrazeランディングページをパーソナライズする方法について説明します。"
page_order: 4
---

# ランディングページのパーソナライズ {#personalize-landing-pages}

> ランディングページでLiquidパーソナライゼーションを使用すると、ユーザープロファイルデータに基づいてコンテンツを動的にカスタマイズできます。たとえば、複数の静的ランディングページを管理することなく、さまざまなユーザー属性に基づいて見出しをパーソナライズできます。

{% alert important %}
ランディングページのLiquidパーソナライゼーションは、ランディングページのProティアでのみ利用可能です。現在、[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)、[多言語]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings/)、および[プロモーションコード]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/)は、ランディングページのLiquidパーソナライゼーションではサポートされていません。
{% endalert %}

## Liquidの挿入 {#inserting-liquid}

ドラッグ＆ドロップエディターでは、エディター内および右側パネルのページまたはブロック設定の両方でLiquidパーソナライゼーションを挿入できます。Liquidの実装手順については、専用の[Liquidドキュメント]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic/#using-liquid)をご確認ください。

![Liquidパーソナライゼーションが追加されたランディングページエディター。]({% image_buster /assets/img/landing_pages/lp_liquid_.png %})

## プレビューとテスト {#previewing-and-testing}

エディターでランディングページをプレビューする際、ランダムユーザー、既存ユーザー、またはカスタムユーザーとしてページを表示できます。

ただし、データテーブルまたは**ランディングページの詳細**ページからランディングページをプレビューする場合は、ランダムユーザーとしてのみ表示できます。

## パーソナライゼーションに関する考慮事項 {#personalization-considerations}

パーソナライズされたランディングページで最適なパフォーマンスを維持するために、以下のサイズ制限にご注意ください。

- **ランディングページの保存：** サイズが500&nbsp;KBを超えると、ページがサイズ制限を超えたことを示す警告メッセージが表示される場合があり、公開できなくなる可能性があります。
- **Liquidパーソナライゼーションによるレンダリング：** 合計サイズは1&nbsp;MBを超えてはなりません。超えた場合、Brazeによってページが自動的に非公開になる可能性があります。

### ランディングページの非公開を回避する {#avoid-unpublishing-landing-pages}

ページがこれらのサイズ制限を超えた場合、制限を超え続けると非公開になる可能性があることを通知するメールが届きます。しきい値に達すると、ページは自動的に非公開になり、通知が届きます。

ページがサイズ制限を超えたり、読み込み時間が遅くなったりするのを防ぐために、以下のようなLiquidパーソナライゼーションを使用してください。

- 大規模なデータセットを継続的にループしたり参照したりしないこと。
- Liquidブロック内で広範な数学的処理や条件ロジックに依存しないこと。

さらに、大きなスクリプト、スタイルシート、base64エンコードされたアセットをランディングページのコードに直接埋め込むことは避けてください。これらのインラインアセットはページサイズ制限にカウントされ、レンダリングを遅くする可能性があります。代わりに、フォント、画像、スタイルシート、スクリプトを[メディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/)にアップロードしてください。メディアライブラリから配信されるアセットはBrazeのCDNでホストされるため、Liquidレンダリングの処理対象にならず、ページサイズ制限にカウントされません。

### 識別済みユーザーと匿名ユーザーに対するLiquidの使用 {#use-liquid-for-identified-and-anonymous-users}

Liquidは、識別済みの訪問者と匿名の訪問者の両方に対してランディングページの体験をカスタマイズできます。

- **識別済みユーザー：** Brazeメッセージからランディングページにリンクし、[ランディングページのLiquidタグ]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users/#using-landing-page-liquid-tags)を含めます。これにより、ユーザーがBrazeプロファイルに関連付けられ、ページ体験がパーソナライズされます。
- **匿名の訪問者：** ランダムな数値や時間帯に応じた挨拶など、文脈に応じたプロファイルに基づかないコンテンツにLiquidを使用します。

## フォールバックページ {#fallback-pages}

ユーザーが非公開になったページにアクセスしようとすると、ページが現在読み込めないことを示すメッセージが表示されます。ページが非公開になる理由には以下が含まれます。

- 複雑または壊れたLiquidにより、レンダリング時間が長くなる
- ユーザーのネットワークの問題
- ランディングページの最大サイズ制限の超過