---
nav_title: 購入記録
article_title: Windows Universal向け購入記録
platform: Windows Universal
page_order: 4
description: "このリファレンス記事では、Windows Universalプラットフォームでの購入記録方法について説明します。"
hidden: true
---

# 購入記録 {#log-purchases}
{% multi_lang_include archive/windows_deprecation.md %}

アプリ内での購入を記録して、売上を経時的にトラッキングしたり、売上源を横断してトラッキングしたりできます。また、ユーザーをLTVでセグメント化することもできます。

Brazeは複数の通貨での購入に対応しています。米ドル以外の通貨でレポートする購入は、レポートされた日付の為替レートに基づいて米ドル単位でダッシュボードに表示されます。

実装する前に、カスタムイベント、カスタム属性、購入イベントによって提供されるセグメンテーションオプションの例を[ベストプラクティス]({{site.baseurl}}/developer_guide/analytics#best-practices)の記事で確認してください。また、[イベント命名規則]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions)についてもよく理解しておくことをお勧めします。

この機能を使用するには、アプリ内購入が正常に完了した後でこのメソッド呼び出しを追加します。

購入は`EventLogger`を使用してログに記録されます。これはIAppboyで公開されているプロパティです。`EventLogger`への参照を取得するには、`Appboy.SharedInstance.EventLogger`を呼び出します。

```csharp
bool LogPurchase(string productId, string currencyCode, decimal price)
```

## 注文レベルでの購入記録 {#log-purchases-at-the-order-level}
商品レベルではなく注文レベルで購入を記録する場合は、注文名または注文カテゴリを`product_id`として使用できます。詳細については、[購入オブジェクトの仕様]({{site.baseurl}}/api/objects_filters/purchase_object#naming-conventions)を参照してください。

## REST API

REST APIを使用して購入を記録することもできます。詳細については、[ユーザーAPI]({{site.baseurl}}/api/endpoints/user_data)のドキュメントを参照してください。