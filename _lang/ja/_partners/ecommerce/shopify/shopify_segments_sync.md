---
nav_title: Shopify セグメントの同期
article_title: Shopify セグメントの同期
alias: /shopify_segments_sync/
page_order: 8
description: "このリファレンス記事では、統一されたオーディエンス管理とターゲティングのために、Shopifyセグメントをコホートとして Braze に同期する方法について説明します。"
---

# Shopify セグメントの同期 {#shopify-segments-sync}

> Shopifyセグメントの同期は、Shopifyストアの機能をBrazeに拡張し、マーケティングチームがShopifyに存在するより豊富なユーザーデータ（標準のBraze Shopify連携ではキャプチャされないシグナルを含む）に直接アクセスできるようにします。Shopifyセグメントをコホートとして同期することで、両プラットフォーム間でオーディエンス定義を統一し、Shopifyでターゲティングする場合でもBrazeキャンペーンを通じてリーチする場合でも、一貫性のある連携されたユーザー体験を提供できます。

{% alert important %}
Shopifyセグメントの同期は現在ベータ版です。アクセスをリクエストするには、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| --- | --- |
| Braze Shopify連携 | Braze ShopifyアプリがShopifyストアにインストールされ、Brazeワークスペースに接続されている必要があります。設定手順については、[Shopify標準連携の設定]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration)または[Shopifyカスタム連携の設定]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration)を参照してください。 |
| Shopifyユーザー権限 | セグメント同期を開始するShopifyユーザーは、ユーザーデータをエクスポートするための**エクスポート**権限を持っている必要があります。Shopifyの権限の詳細については、[Shopifyのストア権限に関するドキュメント](https://help.shopify.com/en/manual/your-account/users/roles/permissions/store-permissions#customers-permissions)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 仕組み {#how-it-works}

Shopifyセグメント同期は2つのフェーズで動作します。

1. **初期バックフィル:** セグメントを初めて同期すると、Brazeは現在のすべてのメンバーをバックフィルし、Brazeに対応するコホートを作成します。バックフィルは非同期で実行されるため、完了までに少し時間がかかる場合があります。
2. **継続的な同期:** 初期バックフィルの後、BrazeはShopify webhookにもサブスクライブするため、メンバーシップはほぼリアルタイムで同期された状態を維持します。

| Webhookトピック | Brazeでの効果 |
| --- | --- |
| `customer.joined_segment` | ユーザーが対応するBrazeコホートに追加されます。 |
| `customer.left_segment` | ユーザーが対応するBrazeコホートから削除されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Webhookトピック" }

同期が失敗した場合、アクション拡張モーダルにエラーバナーが表示され、何が起こったか、およびどのように対処すればよいかが説明されます。一部のエラーでは**同期を再試行**アクションが提供されます。その他のエラーでは、管理者による対応または設定の変更が必要です。

## データインポート連携 {#data-import-integration}

### ステップ1:同期するShopifyセグメントを選択する {#step-1-select-a-shopify-segment-to-sync}

Shopifyで、**Customers** > **セグメント** に移動し、Brazeに同期するセグメントを選択します。注文履歴、商品購入、顧客タグ、生涯支出額、メタフィールドに基づくセグメントなど、Shopifyのネイティブセグメンテーションを使用して構築されたあらゆるセグメントを同期できます。

![Shopifyセグメントの一覧が表示されたセグメントパネル。]({% image_buster /assets/img/shopify/shopify_segments.png %})

### ステップ2:同期を開始する {#step-2-initiate-the-sync}

1. Shopifyのセグメント詳細ページで、**Use segment** ドロップダウンを開き、**Braze セグメント Sync** を選択します。

![「Use segment」ドロップダウンに「Braze セグメント Sync」オプションが表示されたセグメント詳細ページ。]({% image_buster /assets/img/shopify/braze_segment_sync.png %})

{: start="2"}
2. Brazeアクション拡張モーダルが開き、セグメント名とオーディエンスサイズが表示されます。**Sync with Braze** を選択してインポートを開始します。

![Brazeと同期するボタンが表示されたモーダル。]({% image_buster /assets/img/shopify/sync_with_braze.png %}){:style="max-width:70%;"}

{: start="3"}
3. モーダルが同期中の状態に遷移し、Brazeがメンバーをインポートしている間、進行状況バナーが表示されます。

![同期が進行中であることを示すモーダル。]({% image_buster /assets/img/shopify/sync_in_progress.png %}){:style="max-width:70%;"}

{: start="4"}
4. **Close** を選択します。同期はバックグラウンドで続行されます。モーダルを閉じても同期は停止しません。

同期が完了したかどうかを確認するには、モーダルを閉じてから再度開きます。同期が完了すると、モーダルに成功バナーが表示されます。

![同期がアクティブであることを確認するモーダル。]({% image_buster /assets/img/shopify/braze_sync_active.png %}){:style="max-width:70%;"}

### ステップ3:コホートメンバーシップフィルターを使用してBrazeセグメントを作成する {#step-3-create-a-braze-segment-with-the-cohort-membership-filter}

Brazeで、**Audience** > **セグメント** に移動し、新しいセグメントを作成します。**Add Filter** で **Cohort Membership** フィルターを選択し、ドロップダウンから同期済みのShopifyセグメントを選択します。保存後、キャンペーンやキャンバスでユーザーをターゲティングする際にこのBrazeセグメントを参照できます。

![「Shopify Cohorts」フィルターが表示されたセグメントビルダー。]({% image_buster /assets/img/shopify/segment_builder_cohort_import.png %})

## セグメントの再同期 {#re-syncing-a-segment}

セグメントが同期された後、同じアクション拡張機能からいつでもコホートメンバーシップを更新できます。

1. Shopifyで、同期済みのセグメントを開き、**Use segment** > **Braze セグメント Sync** を選択します。
2. モーダルで、**Sync now** を選択します。
3. 確認ダイアログで、**Sync now** を選択して再同期を開始します。

再同期は追加方式です。現在のShopifyセグメントに一致するユーザーはコホートに追加されますが、一致しなくなったユーザーはコホートに残ります。

## Shopifyのセグメント更新 {#segment-updates-in-shopify}

### セグメントの名前変更 {#renaming-a-segment}

Shopifyセグメントの名前を変更すると、Brazeは対応するコホートの表示名を自動的に更新します。再同期は必要ありません。

### セグメント条件の変更 {#changing-segment-criteria}

Shopifyセグメントの条件を変更しても、自動的には反映されません。新たに条件に一致するユーザーを取得するには、アクション拡張機能からセグメントを再同期してください。条件に一致しなくなったユーザーは、再同期ではメンバーが削除されないため、コホートに残ります。詳細については、[セグメントの再同期](#re-syncing-a-segment)を参照してください。

## ユーザーマッチング {#user-matching}

Shopifyセグメントから同期されたユーザーは、Braze Shopify統合の一部として設定される `shopify_customer_id` エイリアスを使用して、Brazeユーザープロファイルとマッチングされます。一致するBrazeユーザープロファイルがないユーザーは、同期時にスキップされます。

Shopify統合がユーザーを識別しエイリアスを設定する方法の詳細については、[Shopifyデータ機能]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features)を参照してください。

Brazeは、同期されたユーザーを、プロファイルの作成方法に関係なく、既存のBrazeユーザープロファイルとマッチングします。これには、Shopifyの履歴バックフィル、独自のデータプラットフォーム（Snowflakeやその他のデータウェアハウスなど）、または直接のAPIインポートによって作成されたプロファイルが含まれます。コホートがShopifyセグメントよりも小さい場合、一部のセグメントメンバーにはまだ一致するBrazeプロファイルがないことを意味します。マッチカバレッジを向上させるには、同期前にお好みの方法でBrazeユーザープロファイルを作成してください。

## 制限事項 {#limitations}

- **一方向の同期。** セグメントメンバーシップは Shopify から Braze への一方向のみです。Braze で直接行ったコホートメンバーシップの変更は Shopify に反映されません。
- **プロファイルの作成は行われません。** Braze のユーザープロファイルが既に存在する Shopify の顧客のみがコホートに追加されます。
- **同期の取り消しはできません。** Shopify セグメントが同期されると、取り消すことはできません。
- **再同期ではメンバーの追加のみが行われます。** セグメントを再同期すると、新たに一致するユーザーがコホートに追加されますが、Shopify セグメントに含まれなくなったユーザーは削除されません。