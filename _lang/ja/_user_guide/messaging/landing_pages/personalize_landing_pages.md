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

### フォームフィールドの事前入力 {#pre-fill-form-fields}

ランディングページのフォームフィールドがユーザープロファイル属性にマッピングされている場合、リピーターに対してそのフィールドを事前入力できます。これにより、フォーム入力の手間が軽減され、既知の訪問者のフォーム完了率が向上します。

フォームフィールドの事前入力を使用するには：

1. ドラッグ＆ドロップエディターでフォームフィールドを選択します。
2. 右側の設定パネルで、フィールドを適切なプロファイル属性にマッピングします。
3. **Pre-fill from user profile**を選択します。

![ユーザープロファイルデータから事前入力するオプションが表示されたランディングページのフォームフィールド設定。]({% image_buster /assets/img/landing_pages/pre-fill-checkbox.png %}){: style="max-width:70%;"}

事前入力は[識別済みユーザー](#use-liquid-for-identified-and-anonymous-users)に対してのみ機能します。匿名の訪問者の場合、フォームフィールドはデフォルトの状態を維持します。

- **入力フィールド：** プレースホルダーテキストが表示されます。
- **チェックボックス、ラジオボタン、および類似のコントロール：** ユーザーが操作するまで未選択のままです。

## カスタムコードによる外部データの取得 {#fetching-external-data-with-custom-code}

**Custom Code**ブロックを使用して、外部エンドポイントからデータを取得し、ランディングページに表示できます。このアプローチではクライアント側（ユーザーのブラウザ）でリクエストを行うため、サーバー側のレンダリング遅延なしにページが素早く読み込まれます。

{% alert warning %}
外部データを取得する場合、実装のセキュリティはお客様の責任となります。API呼び出しで使用される外部識別子はUUIDであるか、同等に安全な命名スキームを使用する必要があります。[ユーザーIDの命名に関するベストプラクティス]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#naming-best-practices)を参照してください。
{% endalert %}

### ユースケース {#use-case}

このパターンは、Brazeに保存されていないユーザー固有のデータを表示する必要がある場合に便利です。例としては、リアルタイムの在庫情報、パーソナライズされたおすすめ、または組織が別のシステムで管理しているその他のデータなどがあります。

### 実装例 {#example-implementation}

この例では、外部APIからユーザーデータを取得する方法を示します。APIエンドポイントをご自身の安全なエンドポイントに置き換え、安全な識別子を使用してください。

{% raw %}
```html
<script>
window.onload = () => {
  // Use Liquid to template the user's external ID
  const userId = "{{${user_id}}}";

  const loadUserData = async () => {
    try {
      // Replace with your own secure API endpoint
      const response = await fetch(`https://your-api.example.com/user/${userId}`);

      if (!response.ok) {
        throw new Error('Failed to load data');
      }

      const data = await response.json();

      // Update the page with the fetched data
      document.querySelector("#user-data").textContent = JSON.stringify(data, null, 2);
      document.querySelector("#user-name").textContent = data.name || "User";
    } catch (error) {
      // Handle errors gracefully
      document.querySelector("#user-data").textContent = "Unable to load data at this time.";
    }
  };

  loadUserData();
};
</script>

<!-- Display area for fetched data -->
<p>Welcome, <span id="user-name">Loading...</span></p>
<pre id="user-data">Loading your information...</pre>
```
{% endraw %}

### 考慮事項 {#considerations}

ランディングページで外部データを取得する際は、以下の点にご注意ください。

- **読み込み状態：** エンドポイントが応答するまで、ユーザーにはプレースホルダーテキストが表示されます。ローディングインジケーターやスケルトンスクリーンの追加を検討してください。
- **エラーハンドリング：** エンドポイントが失敗したり応答が遅い場合、ページが壊れて見える可能性があります。適切なエラーメッセージとフォールバックを実装してください。
- **パフォーマンス：** ページはすぐに読み込まれますが、データは外部リクエストの完了後に表示されます。最適なユーザー体験のために、APIレスポンスを高速に保ってください。
- **セキュリティ：** APIエンドポイントが識別子を検証し、ユーザーが閲覧を許可されたデータのみを返すようにしてください。不正利用を防ぐためにレート制限を実装してください。安全な識別子の選択に関するガイダンスについては、[ユーザーIDの命名に関するベストプラクティス]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#naming-best-practices)を参照してください。

## フォールバックページ {#fallback-pages}

ユーザーが非公開になったページにアクセスしようとすると、ページが現在読み込めないことを示すメッセージが表示されます。ページが非公開になる理由には以下が含まれます。

- 複雑または壊れたLiquidにより、レンダリング時間が長くなる
- ユーザーのネットワークの問題
- ランディングページの最大サイズ制限の超過