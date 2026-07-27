---
nav_title: ランディングページのパーソナライズ
article_title: ランディングページのパーソナライズ
description: "この記事では、ドラッグ＆ドロップエディターを使用してBrazeランディングページをパーソナライズする方法について説明します。"
page_order: 4
---

# ランディングページのパーソナライズ {#personalize-landing-pages}

> ランディングページでLiquidパーソナライゼーションを使用すると、ユーザープロファイルデータに基づいてコンテンツを動的にカスタマイズできます。たとえば、複数の静的ランディングページを管理することなく、さまざまなユーザー属性に基づいて見出しをパーソナライズできます。

{% alert important %}
ランディングページのLiquidパーソナライゼーションは、ランディングページのProティアでのみ利用可能です。現在、[Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)、[多言語]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings)、および[プロモーションコード]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes)は、ランディングページのLiquidパーソナライゼーションではサポートされていません。
{% endalert %}

## Liquidの挿入 {#inserting-liquid}

ドラッグ＆ドロップエディターでは、エディター内およびページやブロックの設定（右側のパネル）の両方でLiquidパーソナライゼーションを挿入できます。Liquidの実装手順については、専用の[Liquidドキュメント]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)をご確認ください。

![Liquidパーソナライゼーションが追加されたランディングページエディター。]({% image_buster /assets/img/landing_pages/lp_liquid_.png %})

## プレビューとテスト {#previewing-and-testing}

エディターでランディングページをプレビューする際、ランダムユーザー、既存ユーザー、またはカスタムユーザーとしてページを表示できます。

ただし、データテーブルまたは**ランディングページの詳細**ページからランディングページをプレビューする場合は、ランダムユーザーとしてのみ表示できます。

## パーソナライゼーションに関する考慮事項 {#personalization-considerations}

パーソナライズされたランディングページで最適なパフォーマンスを維持するために、以下のサイズ制限に注意してください。

- **ランディングページの保存:** サイズが500&nbsp;KBを超えると、ページがサイズ制限を超えたことを示す警告メッセージが表示され、公開できなくなる場合があります。
- **Liquidパーソナライゼーションによるレンダリング:** 合計サイズは1&nbsp;MBを超えてはなりません。超えた場合、Brazeによってページが自動的に非公開になることがあります。

### ランディングページの非公開を防ぐ {#avoid-unpublishing-landing-pages}

ページがこれらのサイズ制限を超えた場合、制限を超え続けると非公開になる可能性があることを通知するメールが届きます。しきい値に達すると、ページは自動的に非公開になり、通知が届きます。

ページがサイズ制限を超えたり、読み込み時間が遅くなったりするのを防ぐために、以下のようなLiquidパーソナライゼーションを使用してください。

- 大規模なデータセットを継続的にループしたり参照したりしない。
- Liquidブロック内で広範な数学的または条件付きロジックに依存しない。

さらに、大きなスクリプト、スタイルシート、base64エンコードされたアセットをランディングページのコードに直接埋め込むことは避けてください。これらのインラインアセットはページサイズ制限にカウントされ、レンダリングを遅くする可能性があります。代わりに、フォント、画像、スタイルシート、スクリプトを[メディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)にアップロードしてください。メディアライブラリから配信されるアセットはBrazeのCDNでホストされるため、Liquidレンダリングの処理対象にならず、ページサイズ制限にもカウントされません。

### 識別済みユーザーと匿名ユーザーにLiquidを使用する {#use-liquid-for-identified-and-anonymous-users}

Liquidを使用すると、識別済みの訪問者と匿名の訪問者の両方に対してランディングページの体験をカスタマイズできます。

- **識別済みユーザー:** Brazeメッセージからランディングページにリンクし、[ランディングページのLiquidタグ]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users#using-landing-page-liquid-tags)を含めます。これにより、ユーザーがBrazeプロファイルに関連付けられ、ページ体験がパーソナライズされます。
- **匿名の訪問者:** ランダムな数値や時間帯に応じた挨拶など、文脈に応じたプロファイルに基づかないコンテンツにLiquidを使用します。

### フォームフィールドの事前入力 {#pre-fill-form-fields}

ランディングページのフォームフィールドがユーザープロファイル属性にマッピングされている場合、リピーターに対してそのフィールドを事前入力できます。これにより、フォームの入力負担が軽減され、既知の訪問者のフォーム完了率が向上します。

フォームフィールドの事前入力を使用するには:

1. ドラッグ＆ドロップエディターでフォームフィールドを選択します。
2. 右側の設定パネルで、フィールドを適切なプロファイル属性にマッピングします。
3. **Pre-fill from user profile** を選択します。

![ユーザープロファイルデータから事前入力するオプションを表示するランディングページのフォームフィールド設定。]({% image_buster /assets/img/landing_pages/pre-fill-checkbox.png %}){: style="max-width:70%;"}

事前入力は[識別済みユーザー](#use-liquid-for-identified-and-anonymous-users)に対してのみ機能します。匿名の訪問者の場合、フォームフィールドはデフォルトの状態を維持します。

- **入力フィールド:** プレースホルダーテキストが表示されます。
- **チェックボックス、ラジオボタン、および類似のコントロール:** ユーザーが操作するまで未選択のままです。

{% alert warning %}
ユーザーがランディングページのリンク（メール、SMS、またはその他のメッセージから）を別の人に転送した場合、受信者には元のユーザー向けに事前入力されたデータが表示されます。これは、購読解除リンクやユーザー設定センターのリンクに適用されるのと同じセキュリティ上の考慮事項です。事前入力するデータの機密性と、この機能を使用する際のオーディエンスの共有行動を考慮してください。
{% endalert %}

## カスタムコードを使用した外部データの取得 {#fetching-external-data-with-custom-code}

**カスタムコード**ブロックを使用して、外部エンドポイントからデータを取得し、ランディングページに表示できます。このアプローチではクライアント側（ユーザーのブラウザ）でリクエストを行うため、サーバーサイドレンダリングの遅延なくページが素早く読み込まれます。

{% alert warning %}
外部データを取得する際は、実装のセキュリティについてはお客様の責任となります。API呼び出しで使用される外部識別子はUUIDまたは同等にセキュアな命名スキームを使用する必要があります。詳しくは[ユーザーIDの命名に関するベストプラクティス]({{site.baseurl}}/developer_guide/analytics/setting_user_ids#naming-best-practices)を参照してください。
{% endalert %}

### ユースケース {#use-case}

このパターンは、Brazeに保存されていないユーザー固有のデータを表示する必要がある場合に便利です。例としては、リアルタイムの在庫情報、パーソナライズされたレコメンデーション、または組織が別のシステムで管理しているその他のデータなどがあります。

### 実装例 {#example-implementation}

この例では、外部APIからユーザーデータを取得する方法を示しています。APIエンドポイントをご自身のセキュアなエンドポイントに置き換え、セキュアな識別子を使用してください。

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

ランディングページで外部データを取得する際は、以下の点を考慮してください。

- **読み込み状態:** エンドポイントが応答するまで、ユーザーにはプレースホルダーテキストが表示されます。読み込みインジケーターやスケルトンスクリーンの追加を検討してください。
- **エラーハンドリング:** エンドポイントが失敗したり応答が遅い場合、ページが壊れているように見えることがあります。適切なエラーメッセージとフォールバックを実装してください。
- **パフォーマンス:** ページはすぐに読み込まれますが、データは外部リクエストの完了後に表示されます。最良のユーザー体験のために、APIレスポンスを高速に保ってください。
- **セキュリティ:** APIエンドポイントが識別子を検証し、ユーザーが閲覧を許可されたデータのみを返すようにしてください。不正利用を防ぐためにレート制限を実装してください。セキュアな識別子の選択に関するガイダンスについては、[ユーザーIDの命名に関するベストプラクティス]({{site.baseurl}}/developer_guide/analytics/setting_user_ids#naming-best-practices)を参照してください。

{% alert warning %}
Liquidでパーソナライズされたランディングページでは、BrazeはランディングページのHTML内のどこに{% raw %}`{{`{% endraw %}および{% raw %}`{%`{% endraw %}デリミタが出現しても処理します。これにはJavaScript文字列、コメント、正規表現の内部も含まれます。これはページ全体に適用されますが、**カスタムコード**ブロックがこれらのシーケンスを意図せず含む可能性が最も高い場所です。

これらのシーケンスが対応する閉じタグなしに出現した場合（例：{% raw %}`/* version {{ 2.0 */`{% endraw %}）、Brazeはそれらを開いたLiquidタグとして扱います。ページ上の他の有効なLiquidタグがレンダリングされなくなったり、同じブロック内の他の場所でLiquidレンダリングが壊れたりする可能性があります。深刻な場合、壊れたLiquidによりページの公開ができなくなったり、非公開になったりすることがあります（[フォールバックページ](#fallback-pages)を参照）。

これを回避するには、Liquid以外のコンテキストから{% raw %}`{{`{% endraw %}および{% raw %}`{%`{% endraw %}をエスケープまたは削除するか、JavaScriptでシーケンスを分割してください（例：{% raw %}`'{' + '{'`{% endraw %}）。Liquidはスクリプトの実行前にサーバーサイドで処理されます。また、Liquid以外の大きなセクションを{% raw %}`&#123;% raw %&#125;...&#123;% endraw %&#125;`{% endraw %}タグで囲むこともできます。
{% endalert %}

## フォールバックページ {#fallback-pages}

ユーザーが非公開になったページにアクセスしようとすると、現在ページを読み込めないことを示すメッセージが表示されます。ページが非公開になる理由には、以下のようなものがあります。

- 複雑または不正なLiquidにより、レンダリング時間が長くなる場合
- ユーザーのネットワークの問題
- ランディングページの最大サイズ制限を超えた場合