---
nav_title: ランディングページ
article_title: ランディングページ
page_order: 8
guide_top_header: "ランディングページ"
description: "この記事には、Brazeランディングページの構築とカスタマイズに関するリソースが含まれています。"
alias: /landing_pages/
---

# ランディングページについて {#about-landing-pages}

> Brazeランディングページは、ユーザー獲得とエンゲージメント戦略を推進できるスタンドアロンのWebページです。

ランディングページを使用して、オーディエンスの拡大、ユーザーデータの取得、特別オファーの宣伝、マルチチャネルキャンペーンのサポートを行いましょう。ランディングページのドラッグ＆ドロップブロックのリファレンスについては、[エディターブロック（ランディングページ）]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages)を参照してください。

{% alert note %}
ランディングページとカスタムドメインの利用可否は、Brazeパッケージによって異なります。開始するには、アカウントマネージャーまたはカスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

{% multi_lang_include video.html id="eg4r7agod1" source="wistia" %}

## 前提条件 {#prerequisites}

ランディングページにアクセスし、作成、公開するには、管理者[権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions)、または以下のすべての権限が必要です。

- View Landing Pages
- Edit Landing Page Drafts
- Publish Landing Pages

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## プランティア {#plan-tiers}

公開できるランディングページ数、カスタムドメイン数、使用できる機能は、プランの種類（無料またはPro（増分））によって異なります。

| 機能                                                                                                   | 無料ティア     | Proティア（増分）     |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| 公開済みランディングページ                                                                 | 1社あたり5ページ | 追加20ページ |
| カスタムドメイン          | 1社あたり1ドメイン | 追加5ドメイン |
| [Liquidパーソナライゼーション]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages) | 利用不可 | 利用可能 |
| 事前入力フォームフィールド | 利用不可 | 利用可能 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="プランティア" }

## レート制限 {#rate-limits}

Brazeは、キャッシュされていないランディングページに対して、ワークスペースごとに3秒あたり500リクエスト（約167リクエスト/秒）のレート制限を適用します。この制限は、高トラフィック時のシステムパフォーマンスと信頼性を維持するのに役立ちます。

キャッシュされたランディングページのビューは、この制限にカウントされません。キャッシュがトラフィックに与える影響については、[ランディングページは高トラフィックのシナリオに対応できますか？](#can-landing-pages-handle-high-traffic-scenarios)を参照してください。

## ランディングページへのGoogle Tag Managerの追加 {#adding-google-tag-manager-to-a-landing-page}

ランディングページにGoogle Tag Managerを追加するには、ドラッグ＆ドロップエディターでランディングページに**カスタムコード**ブロックを追加し、Tag Managerのコードをブロックに挿入します。以下の例のように、Tag Managerのコードの前にデータレイヤーを必ず追加してください。

```
<script>
window.dataLayer = window.dataLayer || [];
</script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXX');</script>
<!-- End Google Tag Manager -->
```

Google Tag Managerの実装の詳細については、[Googleのドキュメント](https://developers.google.com/tag-platform/tag-manager/datalayer#installation)を参照してください。

## よくある質問 {#frequently-asked-questions}

### ランディングページの最大サイズは？ {#whats-the-maximum-size-for-landing-pages}

ランディングページのボディサイズは最大500 KBです。

### ランディングページは高トラフィックのシナリオに対応できますか？ {#can-landing-pages-handle-high-traffic-scenarios}

はい。パーソナライズされていないランディングページは、高トラフィックのシナリオに効果的に対応します。ランディングページが最初にリクエストされると、BrazeはCloudflareを通じてキャッシュします。同じリンクへの後続のリクエストはキャッシュから配信されるため、高トラフィック時に役立ちます。このキャッシュは24時間持続し、キャッシュされたページビューは[レート制限](#rate-limits)にカウントされません。

パーソナライズされたランディングページは、Cloudflareキャッシュの有効期間が短く、Brazeへの未キャッシュリクエストがより多く発生します。これらの未キャッシュリクエストは、[レート制限](#rate-limits)で説明されているワークスペースごとのレート制限の対象となります。

パーソナライズされたページのサイズ制限やその他のパフォーマンスガイダンスについては、[パーソナライゼーションに関する考慮事項]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages#personalization-considerations)を参照してください。

### ランディングページを公開するための技術的な要件はありますか？ {#are-there-any-technical-requirements-to-publish-a-landing-page}

いいえ、技術的な要件はありません。

### ランディングページ用のHTMLエディターはありますか？ {#is-there-an-html-editor-for-landing-pages}

はい。ドラッグ＆ドロップエディターの**カスタムコード**ブロックを使用して、HTMLを追加または編集できます。カスタムコードからBraze SDKとインターフェイスするには、[ランディングページ用JavaScriptブリッジ]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge)を参照してください。完全にカスタムのUIをランディングページフォームに接続するには、[カスタムフォームブロックの作成]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks)を参照してください。

### ランディングページでiframeを使用できますか？ {#can-i-use-iframes-on-landing-pages}

はい。ドラッグ＆ドロップエディターで**カスタムコード**ブロックを追加し、埋め込みたいコンテンツのURLを含むiframe要素を追加してください。

埋め込み先のWebサイトがContent Security Policy（CSP）の`frame-ancestors`や`X-Frame-Options`によってフレーミングを制限している場合、ページがiframe内で読み込まれない場合があります。Brazeはこれらの設定を上書きすることはできません。埋め込み先のサイトがランディングページのドメインを許可するよう設定されている必要があります。

### ランディングページ内にWebhookを作成できますか？ {#can-i-create-a-webhook-inside-a-landing-page}

いいえ。ただし、**ランディングページフォームを送信**イベントは、キャンバスやWebhookキャンペーンのトリガーとして機能できます。

- **キャンバス：** **ランディングページフォームを送信**イベントをキャンバスのエントリトリガーとして使用し、Webhookステップを追加します。
- **キャンペーン：** **ランディングページフォームを送信**イベントを使用して、フォーム送信に基づいてトリガーします。

ページがBrazeチャネル（Webサイトや広告など）を通じて送信されていない場合、その人物がすでにBrazeに存在していても、送信時に新しいユーザープロファイルが作成される場合があります。これに対処するには、**ランディングページフォームを送信**でトリガーされるキャンバスを設定し、[`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge)エンドポイントを呼び出すBraze-to-Braze Webhookステップを追加して、新しいプロファイルを既存のプロファイルに統合します。

`landing_page_url` Liquidタグを使用してページを共有する場合、フォーム送信は既存のユーザープロファイルに自動的に紐づけられます。その後、ランディングページで送信されたユーザー属性をLiquidで参照し、後続のテンプレーティングに使用できます。