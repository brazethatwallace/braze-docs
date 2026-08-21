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

ランディングページにアクセス、作成、公開するには、管理者の[権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions)、または以下のすべての権限が必要です。

- View Landing Pages
- Edit Landing Page Drafts
- Publish Landing Pages

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## プランティア {#plan-tiers}

公開できるランディングページの数、カスタムドメインの数、および使用できる機能は、プランタイプ（無料またはPro（増分））によって異なります。

| 機能                                                                                                   | 無料ティア     | Proティア（増分）     |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| 公開済みランディングページ                                                                 | 1社あたり5ページ | 追加20ページ |
| カスタムドメイン          | 1社あたり1ドメイン | 追加5ドメイン |
| [Liquidパーソナライゼーション]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages) | 利用不可 | 利用可能 |
| 事前入力フォームフィールド | 利用不可 | 利用可能 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="プランティア" }

## ランディングページへのGoogle Tag Managerの追加 {#adding-google-tag-manager-to-a-landing-page}

ランディングページにGoogle Tag Managerを追加するには、ドラッグ＆ドロップエディターでランディングページに**カスタムコード**ブロックを追加し、そのブロックにTag Managerのコードを挿入します。以下の例のように、Tag Managerのコードの前にデータレイヤーを追加してください。

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

### ランディングページの最大サイズはどのくらいですか？ {#whats-the-maximum-size-for-landing-pages}

ランディングページのボディサイズは最大500 KBです。

### ランディングページは高トラフィックのシナリオに対応できますか？ {#can-landing-pages-handle-high-traffic-scenarios}

はい、パーソナライズされていないランディングページは高トラフィックのシナリオに効果的に対応できます。パーソナライズされていないランディングページが最初にリクエストされると、BrazeはCloudflareを通じてキャッシュします。つまり、同じリンクへの後続のリクエストはすべてキャッシュから提供されるため、大量のリクエストでもパフォーマンスが低下しません。このキャッシュは24時間持続し、キャッシュされたページビューはレート制限にカウントされません。

パーソナライズされたランディングページ（Liquidパーソナライゼーションを使用）の場合、キャッシュされていないリクエストにレート制限が適用されます。最適なパフォーマンスを維持するには、[パーソナライゼーションに関する考慮事項]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages#personalization-considerations)を参照してください。

### ランディングページを公開するための技術的な要件はありますか？ {#are-there-any-technical-requirements-to-publish-a-landing-page}

いいえ、技術的な要件はありません。

### ランディングページ用のHTMLエディターはありますか？ {#is-there-an-html-editor-for-landing-pages}

はい。ドラッグ＆ドロップエディターの**カスタムコード**ブロックを使用して、HTMLを追加または編集できます。カスタムコードからBraze SDKとインターフェイスするには、[ランディングページ用JavaScriptブリッジ]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge)を参照してください。完全にカスタムのUIをランディングページフォームに接続するには、[カスタムフォームブロックの作成]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks)を参照してください。

### ランディングページでiframeを使用できますか？ {#can-i-use-iframes-on-landing-pages}

はい。ドラッグ＆ドロップエディターで**カスタムコード**ブロックを追加し、埋め込みたいコンテンツのURLを含むiframe要素を追加してください。

埋め込み先のWebサイトがContent Security Policy（CSP）の`frame-ancestors`や`X-Frame-Options`によってフレーミングを制限している場合、iframe内でページが読み込まれないことがあります。Brazeはこれらの設定を上書きできません。埋め込み先のサイトがランディングページのドメインを許可するように設定されている必要があります。

### ランディングページ内にWebhookを作成できますか？ {#can-i-create-a-webhook-inside-a-landing-page}

いいえ。ただし、**Submitted a Landing Page form**イベントは、キャンバスやWebhookキャンペーンのトリガーとして機能できます。

- **キャンバス：** **Submitted a Landing Page form**イベントをキャンバスのエントリトリガーとして使用し、Webhookステップを追加します。
- **キャンペーン：** **Submitted a Landing Page form**イベントを使用して、フォーム送信に基づいてトリガーします。

ページがBrazeチャネルを通じて送信されていない場合（Webサイトや広告経由など）、送信時に新しいユーザープロファイルが作成される可能性があります。そのユーザーがすでにBrazeに存在している場合でも同様です。これに対処するには、**Submitted a Landing Page form**でトリガーされるキャンバスを設定し、[`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge)エンドポイントを呼び出すBraze-to-Braze Webhookステップを追加して、新しいプロファイルを既存のプロファイルに統合します。

`landing_page_url` Liquidタグを使用してページを共有する場合、フォーム送信は自動的に既存のユーザープロファイルに紐づけられます。その後、ランディングページで送信されたユーザー属性をLiquidを通じて参照し、後続のテンプレーティングに使用できます。