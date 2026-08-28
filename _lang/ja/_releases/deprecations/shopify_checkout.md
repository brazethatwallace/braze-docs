---
nav_title: Shopify checkoutとLiquid
page_order: 7
description: "この記事では、Shopifyのcheckout&#46;liquidの廃止について、Shopify連携への影響と開発者向けのガイダンスを説明します。"
page_type: update

---

# Shopify checkout&#46;liquidの廃止 {#shopify-checkout46liquid-deprecation}

Shopifyはすべてのマーチャントに`checkout.liquid`の廃止と、カスタマイズされたチェックアウト体験を構築するための新しい基盤である[Checkout Extensibility](https://www.shopify.com/enterprise/blog/checkout-extensibility-winter-editions)への移行について通知しました。

Shopifyは`checkout.liquid`を2段階で廃止します:

1. **[2024年8月13日](#phase-one-august-13-2024):** 情報、配送、支払いのページをアップグレードする期限。
2. **[2025年8月28日](#phase-two-august-28-2025):** スクリプトタグと追加スクリプトを使用するアプリを含む、サンキューページと注文ステータスページをアップグレードする期限。

Checkout Extensibilityへのアップグレードに関する一般情報については、[Shopifyのアップグレードガイド](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility)を参照してください。

## 連携への影響 {#impact-to-your-integration}

BrazeとShopifyの連携では、[Shopify ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy)を使用して、ヘッドレスでないサイトにBraze Web SDKを読み込みます。2025年の期限までにすべての顧客をサポートするため、`checkout.liquid`が完全に非推奨となる前に、連携の新バージョンをリリースする予定です。

2024年8月13日に予定されている変更について、開発チームが影響を受けるかどうか、以下の詳細を確認してください。

### フェーズ1：2024年8月13日 {#phase-one-august-13-2024}

デフォルトのBrazeとShopifyの連携では、チェックアウト体験内の情報、配送、および支払いページを使用しません。そのため、デフォルトの連携は影響を受けません。

#### Shopify Plus

Shopify Plusの顧客の場合、情報、配送、または支払いページ用に`checkout.liquid`を変更するカスタムSDKコードスニペットは、この日以降無効になります。たとえば、これらのページからイベントを記録するカスタムコードは機能しなくなります。カスタムSDKコードを使用している場合は、移行に関する[開発者ガイダンス](#developer-guidance)をご覧ください。

#### Shopify Plus以外 {#non-shopify-plus}

Shopify Plus以外の顧客の場合、情報、支払い、および配送ページをカスタマイズする必要がある場合は、[Shopify Plusにアップグレード](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility#eligibility)した上で、[開発者ガイダンス](#developer-guidance)に従ってください。

### フェーズ2：2025年8月28日 {#phase-two-august-28-2025}

Shopifyは、連携で使用されている`checkout.liquid`ページの[ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy)のサポートを非推奨にします。これに対応して、2025年8月の期限に十分先立ってリリースすることを目指し、Shopify連携の新バージョンを積極的に開発しています。Brazeプロダクトチームからの詳細情報にご期待ください。

## 開発者向けガイダンス {#developer-guidance}

このガイダンスは、`checkout.liquid`の情報ページ、配送ページ、または支払いページにカスタムSDKコードスニペットを追加したShopify Plusの顧客に適用されます。これらのカスタマイズを行っていない場合は、このガイダンスを無視できます。

今後、`checkout.liquid`の情報ページ、配送ページ、または支払いページにカスタムSDKコードスニペットを追加できなくなります。代わりに、サンキューページまたは注文ステータスページにカスタムSDKコードスニペットを追加する必要があります。これにより、チェックアウトを完了したユーザーを照合できます。
1. サンキューページと注文ステータスページでBraze Web SDKを読み込みます。
2. ユーザーからメールアドレスを取得します。
3. `setEmail`を呼び出します。

{% raw %}
```java
braze.getUser().setEmail(<email address>);
```
{% endraw %}

{: start="4"}
4. Brazeでメールアドレスに基づいてユーザープロファイルをマージします。

重複するユーザープロファイルが見つかった場合は、[一括マージツール]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users#bulk-merging)を使用してデータの整理を効率化できます。