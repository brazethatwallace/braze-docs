---
nav_title: Google Tag Manager
article_title: Google Tag ManagerとBraze SDK
platform:
  - Android
  - FireOS
  - Swift
page_order: 1.1
description: "ランタイム初期化、遅延初期化、Google Tag Managerなどの方法を使用してBraze SDKを初期化する方法について説明します。"

---

# Google Tag ManagerとBraze SDK {#google-tag-manager-with-the-braze-sdk}

> [Google Tag Manager（GTM）](https://developers.google.com/tag-platform/tag-manager)をBraze SDKと連携することで、コード変更やアプリの新バージョンリリースを必要とせずに、Brazeのイベントトラッキングやユーザー属性の更新をリモートでコントロールできます。

{% sdktabs %}
{% sdktab web %}
## Google Tag Manager for Webについて {#google-tag-manager}

Google Tag Manager（GTM）を使えば、プロダクションコードのリリースやエンジニアリングリソースを必要とせずに、Webサイトのタグをリモートで追加、削除、編集できます。BrazeはWeb SDK用に以下のテンプレートを提供しています。

| タグの種類 | ユースケース |
|--------|--------|
| 初期化タグ | このタグにより、サイトのコードを変更することなく、[Web Braze SDKを統合する]({{site.baseurl}}/developer_guide/sdk_integration/?tab=google%20tag%20manager&sdktab=web)ことができます。|
| アクションタグ | このタグで[Content Cardsの作成]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager)、[ユーザー属性の設定]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=google%20tag%20manager&sdktab=web)、[データ収集の管理]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?tab=google%20tag%20manager&sdktab=web)ができます。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Google Tag Manager for Webについて" }

## Brazeアクションタグのタグシーケンス {#tag-sequencing-for-braze-action-tags}

カスタムイベントやその他のBrazeアクションタグは、**Braze Initialization**タグがWeb SDKの読み込みを完了する前に発火すると失敗することがあります。Google Tag Managerでアクションタグを開き、**Advanced Settings** > **Tag Sequencing**に移動して、**A tag that fires before [this tag] is fired**を選択し、Braze Initializationタグを選択してください。

詳細については、[カスタムイベントのタグシーケンスの検証]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_tag-sequencing)を参照してください。

## GTMで購入を記録する {#log-purchases-with-gtm}

BrazeアクションタグおよびCustom HTMLタグで `braze.logPurchase()` を呼び出して収益を記録します。レガシーの `appboy.logPurchase()` 名前空間は、現在のWeb SDK統合ではサポートされていません。

## GTMでカスタムイベントを記録する {#logging-custom-events-with-gtm}

GTMの**Custom HTML**タグを使用してカスタムイベントを記録できます。このアプローチでは、GTMの[データレイヤー](https://developers.google.com/tag-platform/tag-manager/datalayer)を使用して、サイトからGTMタグにイベントデータを渡し、Braze Web SDKを呼び出します。

### ステップ1：データレイヤーにイベントをプッシュする {#step-1-push-the-event-to-the-data-layer}

サイトのコードで、カスタムイベントをトリガーしたい場所でデータレイヤーにイベントをプッシュします。たとえば、ボタンがクリックされたときにカスタムイベントを記録するには、次のようにします。

```html
<button onclick="dataLayer.push({'event': 'my_custom_event'});">Track Event</button>
```

### ステップ2：GTMでトリガーを作成する {#step-2-create-a-trigger-in-gtm}

1. GTMコンテナで、**Triggers**に移動し、新しいトリガーを作成します。
2. **Trigger Type**を**Custom Event**に設定します。
3. **Event Name**を、データレイヤーにプッシュした値と同じ値（たとえば `my_custom_event`）に設定します。
4. トリガーを発火するタイミングを選択します（たとえば**All Custom Events**）。

### ステップ3：Custom HTMLタグを作成する {#step-3-create-a-custom-html-tag}

1. GTMで、**Tags**に移動し、新しいタグを作成します。
2. **Tag Type**を**Custom HTML**に設定します。
3. HTMLフィールドに、以下を追加します。

    ```html
    <script>
    window.braze.logCustomEvent("my_custom_event");
    </script>
    ```

4. **Triggering**で、ステップ2で作成したトリガーを選択します。
5. コンテナを保存して公開します。

イベントプロパティを含めるには、2番目の引数として渡します。

```html
<script>
window.braze.logCustomEvent("my_custom_event", {"property_key": "property_value"});
</script>
```

## GoogleのEUユーザー同意ポリシー {#googles-eu-user-consent-policy}

{% alert important %}
Googleは、2024年3月6日に発効した[デジタル市場法（DMA）](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html)の変更に対応して、[EUユーザー同意ポリシー](https://www.google.com/about/company/user-consent-policy/)を更新しています。この新しい変更により、広告主はEEAおよび英国のエンドユーザーに特定の情報を開示し、必要な同意を取得することが求められます。詳細については、以下のドキュメントを確認してください。
{% endalert %}

GoogleのEUユーザー同意ポリシーの一環として、以下のブール型カスタム属性をユーザープロファイルに記録する必要があります。

- `$google_ad_user_data`
- `$google_ad_personalization`

GTM統合を介してこれらを設定する場合、カスタム属性にはCustom HTMLタグの作成が必要です。以下は、これらの値をブールデータ型（文字列ではなく）として記録する方法の例です。

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

詳細については、[Googleへのオーディエンス同期]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync)を参照してください。

{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/google_tag_manager.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/google_tag_manager.md %}
{% endsdktab %}
{% endsdktabs %}

## トラブルシューティング {#troubleshooting}

Brazeが初期化されない場合やイベントが期待どおりに表示されない場合は、GTMコンテナが公開されていること、トリガーとタグの発火順序がSDKの[ライフサイクルおよび初期化戦略]({{site.baseurl}}/developer_guide/sdk_integration)と一致していること、テストデバイスがBrazeエンドポイントをブロックしていないことを確認してください。

初期化の失敗については、Brazeタグまたはカスタムタグプロバイダーが期待される `actionType` とパラメーターを受信しているかを確認してください（このページのAndroid、Swift、Webの各タブを参照）。GTMから発火されたイベントを検証する際に詳細なログを取得するには、各タブからリンクされているプラットフォーム統合ガイドの説明に従って、プラットフォームのSDKデバッグログを有効にしてください。