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

BrazeとShopifyの連携は、[Shopify ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy)を使用して、ヘッドレスでないサイトにBraze Web SDKを読み込みます。`checkout.liquid`が完全に廃止される前にすべての顧客をサポートするため、2025年の期限前に新しいバージョンの連携をリリースする予定です。

2024年8月13日に予定されている変更については、以下の詳細を確認して、開発チームが影響を受けるかどうかをご確認ください。

### フェーズ1: 2024年8月13日 {#phase-one-august-13-2024}

デフォルトのBrazeとShopifyの連携は、チェックアウト体験内の情報、配送、および支払いページを使用しません。そのため、デフォルトの連携は影響を受けません。

#### Shopify Plus

Shopify Plusの顧客の場合、情報、配送、または支払いページの`checkout.liquid`を変更するカスタムSDKコードスニペットは、この日以降無効になります。例えば、これらのページからイベントを記録するカスタムコードは機能しなくなります。カスタムSDKコードがある場合は、移行のための[開発者ガイダンス](#developer-guidance)をご覧ください。

#### 非Shopify Plus {#non-shopify-plus}

Shopify Plus以外の顧客の場合、情報、支払い、および配送ページをカスタマイズする必要がある場合は、[Shopify Plusにアップグレードする必要があります](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility#eligibility)。その後、[開発者ガイダンス](#developer-guidance)に従ってください。

### フェーズ2: 2025年8月28日 {#phase-two-august-28-2025}

Shopifyは、連携で使用されている`checkout.liquid`ページでの[ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy)のサポートを廃止します。これを受けて、2025年8月の期限よりも十分前にリリースする予定のShopify連携の新バージョンを積極的に構築しています。Braze製品チームからの詳細情報をお待ちください。

## 開発者ガイダンス {#developer-guidance}

このガイダンスは、`checkout.liquid`の情報、配送、または支払いページにカスタムSDKコードスニペットを追加したShopify Plusの顧客に適用されます。これらのカスタマイズを行っていない場合は、このガイダンスを無視してかまいません。

`checkout.liquid`では、情報、配送、または支払いページにカスタムSDKコードスニペットを追加できなくなります。代わりに、カスタムSDKコードスニペットをサンキューページまたは注文ステータスページに追加する必要があります。これにより、チェックアウトを完了したユーザーを照合できます。
1. サンキューページと注文ステータスページでBraze Web SDKを読み込みます。
2. ユーザーからメールアドレスを取得します。
3. `setEmail`を呼び出します。

{% raw %}
```java
braze.getUser().setEmail(<email address>);
```
{% endraw %}

{: start="4"}
4. Brazeで、ユーザープロファイルをメールアドレスでマージします。

重複するユーザープロファイルが発生した場合は、データを効率化するために[一括マージツール]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging)を使用できます。