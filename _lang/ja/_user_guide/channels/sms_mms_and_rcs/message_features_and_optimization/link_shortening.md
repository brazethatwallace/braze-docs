---
nav_title: リンク短縮
article_title: リンク短縮
page_order: 1
description: "この参照記事では、SMSメッセージでリンク短縮を有効にする方法と、よくある質問について説明しています。"
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS
---

# リンク短縮 {#link-shortening}

> このページでは、SMSおよびRCSメッセージでリンク短縮を有効にする方法、短縮リンクのテスト、短縮リンクでのカスタムドメインの使用などについて説明します。

{% alert important %}
Brazeは[統合リンク短縮]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening?sdktab=unified)を段階的にロールアウトしています。これにより、すべてのSMSおよびRCSの短縮リンクが単一のパーソナライズされたリンク形式（例：`brz.ai/abcdefgh`）に統合されます。
{% endalert %}

{% sdktabs %}
{% sdktab Legacy %}

リンク短縮とクリックトラッキングを使用すると、SMSまたはRCSメッセージに含まれるURLを自動的に短縮し、クリックスルー率の分析を収集できます。これにより、ユーザーがキャンペーンにどのようにエンゲージしているかを理解するための追加のエンゲージメント指標が提供されます。

リンク短縮とクリックトラッキングは、キャンペーンとキャンバスの両方で[メッセージバリアントレベル]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#step-1-create-your-campaign)で有効にできます。

{% multi_lang_include channels/sms/rcs_link_shortening_note.md %}

URLの長さは、有効にしたトラッキングの種類によって決まります。
- **基本トラッキング**は、キャンペーンレベルのクリックトラッキングを有効にします。静的URLの長さは20文字で、パーソナライズされたURLの長さは25文字です。
- **高度なトラッキング**は、キャンペーンレベルおよびユーザーレベルのクリックトラッキングを有効にし、クリックに依存するセグメンテーションおよびリターゲティング機能の使用を可能にします。クリックは、Currentsを通じて送信される[SMSクリックイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)も生成します。高度なトラッキングを使用した静的URLの長さは27〜28文字で、URLをクリックしたユーザーのセグメントを作成できます。パーソナライズされたURLの長さは32〜33文字です。

リンクは、共有ショートドメイン（`brz.ai`）またはカスタムリンク短縮ドメインを使用して短縮されます。URLの例は次のようになります：`https://brz.ai/8jshX`（基本、静的）または`https://brz.ai/p/8jshX/2dj8d`（高度、パーソナライズ）。詳細については、[テスト](#legacy_testing)を参照してください。

`http://`または`https://`で始まる静的URLはすべて短縮されます。静的な短縮URLは、作成日から1年間有効です。Liquidパーソナライゼーションを含む短縮URLは2か月間有効です。

{% alert note %}
Brazeの短縮リンクには常に`https://`プロトコルが含まれており、別のプロトコルを使用するように設定することはできません。
{% endalert %}

## リンク短縮の使用 {#using-link-shortening}

リンク短縮を使用するには、メッセージ作成画面のリンク短縮トグルがオンになっていることを確認してください。次に、基本トラッキングまたは高度なトラッキングのいずれかを選択します。

![リンク短縮のトグルがあるメッセージ作成画面。]({% image_buster /assets/img/link_shortening/legacy/temp_shortening1.png %})

Brazeは`http://`または`https://`で始まるURLのみを認識します。URLが認識されると、**プレビュー**セクションがプレースホルダーURLで更新されます。Brazeは短縮後のURLの長さを推定しますが、より正確な推定のためにテストユーザーを選択してメッセージを下書きとして保存するよう警告が表示されます。

![「メッセージ」ボックスに長いURLがあり、プレビューに生成された短縮リンクが表示されたメッセージ作成画面。]({% image_buster /assets/img/link_shortening/legacy/temp_shortening3.png %})

{% alert note %}
BrazeAI<sup>TM</sup>の[インテリジェントチャネルフィルター]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel)を使用し、SMSおよびRCSチャネルを選択可能にしたい場合は、高度なトラッキングでリンク短縮を有効にしてください。
{% endalert %}

### UTMパラメーターの追加 {#adding-utm-parameters}

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## URLでのLiquidパーソナライゼーション {#liquid-personalization-in-urls}

Brazeの作成画面内でURLを動的に構築できるため、URLにダイナミックなUTMパラメーターを追加したり、ユーザーにユニークなリンクを送信したりできます（放棄カートへの誘導や、再入荷した特定の商品への誘導など）。

### サポートされているLiquidパーソナライゼーションタグを使用したURLの作成 {#create-a-url-with-supported-liquid-personalization-tags}

URLは、[サポートされているLiquidパーソナライゼーションタグ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)を使用して動的に生成できます。

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Brazeは、以下の例のようなカスタム定義のLiquid変数の短縮もサポートしています。

### Liquid変数を使用したURLの作成 {#create-a-url-using-liquid-variables}

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Liquid変数によってレンダリングされたURLの短縮 {#shorten-urls-rendered-by-liquid-variables}

**サポートされているチャネル：** KakaoTalk、LINE、SMS、RCS、WhatsApp

Brazeは、APIトリガープロパティに含まれるものも含め、LiquidによってレンダリングされたURLを短縮します。たとえば、{% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %}が有効なURLを表す場合、Brazeはメッセージを送信する前にそのURLを短縮してトラッキングします。

### `/messages/send`エンドポイントでのURLの短縮 {#shorten-urls-in-messagessend-endpoint}

リンク短縮は、[`/messages/send`エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)を通じたAPIのみのメッセージでも有効になります。基本トラッキングまたは高度なトラッキングも有効にするには、`link_shortening_enabled`または`user_click_tracking_enabled`リクエストパラメーターを使用します。

| パラメーター | 必須 | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
| `link_shortening_enabled` | オプション | Boolean | リンク短縮とキャンペーンレベルのクリックトラッキングを有効にするには、`link_shortening_enabled`を`true`に設定します。トラッキングを使用するには、`campaign_id`と`message_variation_id`が必要です。|
| `user_click_tracking_enabled` | オプション | Boolean | リンク短縮、キャンペーンレベルおよびユーザーレベルのクリックトラッキングを有効にするには、`user_click_tracking_enabled`を`true`に設定します。トラッキングデータを使用して、URLをクリックしたユーザーのセグメントを作成できます。<br><br>このパラメーターを使用するには、`link_shortening_enabled`が`true`であり、`campaign_id`と`message_variation_id`が必要です。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="/messages/sendエンドポイントでのURLの短縮" }

リクエストパラメーターの完全なリストについては、[リクエストパラメーター]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters)を参照してください。

## テスト {#testing}

キャンペーンまたはキャンバスを開始する前に、まずメッセージをプレビューしてテストすることがベストプラクティスです。これを行うには、**テスト**タブに移動して、[コンテンツテストグループ]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups)または個々のユーザーにSMSまたはRCSメッセージをプレビューして送信します。

このプレビューは、関連するパーソナライゼーションと短縮URLで更新されます。文字数と[課金対象セグメント]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator)も、レンダリングされたパーソナライゼーションと短縮URLを反映して更新されます。

テストメッセージを送信する前にキャンペーンまたはキャンバスを保存して、メッセージで送信される短縮URLの表現を受け取るようにしてください。テスト送信前にキャンペーンまたはキャンバスが保存されていない場合、テスト送信にはプレースホルダーURLが含まれます。

「短縮SMSリンクをクリック」フィルターにキャンバスが表示されるようにするには、ショートリンクを含むキャンバスステップでも高度なトラッキングを有効にする必要があります。これにより、ユーザーレベルのクリックトラッキングが可能になります。ショートリンクが基本トラッキングで設定されている場合、SMSショートリンクのクリックイベントをフィルタリングするオプションは利用できません。クリックされた短縮SMSリンクに依存するキャンバスエントリまたはアクションパスを設定する場合も、同じ高度なトラッキング要件が適用されます。

{% alert important %}
アクティブなキャンバス内で下書きが作成された場合、短縮URLは生成されません。実際の短縮URLは、キャンバスの下書きがアクティブになったときに生成されます。
{% endalert %}

![テスト受信者を選択するフィールドがあるメッセージの「テスト」タブ。]({% image_buster /assets/img/link_shortening/legacy/temp_shortening2.png %})

{% alert note %}
Liquidパーソナライゼーションと短縮URLは、ユーザーが選択された後に**テスト**タブでテンプレート化されます。正確な文字数を取得するために、ユーザーが選択されていることを確認してください。
{% endalert %}

## クリックトラッキング {#click-tracking}

リンク短縮が有効になっている場合、**SMS/MMS/RCSパフォーマンス**テーブルには、バリアントごとのクリックイベント数と関連するクリック率を示す**合計クリック数**という列が含まれます。指標の詳細については、[メッセージパフォーマンス]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting)を参照してください。

![SMSおよびMMSのパフォーマンス指標テーブル。]({% image_buster /assets/img/link_shortening/shortening4.png %})

**過去のパフォーマンス**テーブルと**SMS/MMS/RCSパフォーマンス**テーブルにも**合計クリック数**のオプションがあり、クリックイベントの日次時系列が表示されます。クリックはリダイレクト時（ユーザーがリンクにアクセスした場合など）にインクリメントされ、ユーザーごとに複数回インクリメントされる場合があります。

## ユーザーのリターゲティング {#retargeting-users}

リターゲティングのガイダンスについては、[リターゲティング]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting#filter-by-advanced-tracking-links)を参照してください。

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### URLをクリックした個々のユーザーを把握できますか？ {#do-i-know-which-individual-users-are-clicking-on-a-url}

はい。**高度なトラッキング**が有効になっている場合、[SMSリターゲティングフィルター]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting)またはCurrentsによって送信されるSMSクリックイベント（`users.messages.sms.ShortLinkClick`）を活用して、URLをクリックしたユーザーをリターゲティングできます。

### リンク短縮はディープリンクやユニバーサルリンクで機能しますか？ {#does-link-shortening-work-with-deep-links-or-universal-links}

リンク短縮はディープリンクでは機能しません。代わりに、BranchやAppsFlyerなどのサードパーティプロバイダーのユニバーサルリンクを短縮できますが、ユーザーは短時間のリダイレクトや「ちらつき」効果を経験する場合があります。これは、短縮リンクがアプリの起動をサポートするユニバーサルリンクに解決される前に、まずWebを経由するためです。さらに、Brazeはユニバーサルリンクの短縮時に発生する可能性のある問題（アトリビューションの破損や予期しないリダイレクトなど）のトラブルシューティングを行うことができません。

{% alert note %}
ユニバーサルリンクでリンク短縮を実装する前に、ユーザーエクスペリエンスをテストして、期待どおりであることを確認してください。
{% endalert %}

### `send_ids`はSMSクリックイベントに関連付けられていますか？ {#are-send_ids-associated-with-sms-click-events}

いいえ。ただし、高度なトラッキングが有効になっている場合、[クエリビルダー]({{site.baseurl}}/query_builder)を使用して、以下のクエリでCurrentsデータをクエリすることにより、一般的に`send_ids`をクリックイベントに関連付けることができます。

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL;
```


{% endsdktab %}
{% sdktab Unified %}

{% multi_lang_include channels/sms/unified_link_shortening.md %}

{% endsdktab %}
{% endsdktabs %}