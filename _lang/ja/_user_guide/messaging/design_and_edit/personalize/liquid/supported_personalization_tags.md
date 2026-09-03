---
nav_title: サポートされているパーソナライゼーションタグ
article_title: サポートされている Liquid パーソナライゼーションタグ
page_order: 1
description: "このリファレンス記事では、サポートされている Liquid パーソナライゼーションタグの完全なリストを紹介します。"
search_rank: 1
---

# サポートされているパーソナライゼーションタグ {#supported-personalization-tags}

> このリファレンス記事では、サポートされている Liquid パーソナライゼーションタグの完全なリストを紹介します。

## サポートされているタグの概要 {#summary-of-supported-tags}

便宜上、サポートされているパーソナライゼーションタグの概要を以下に示します。各タグの種類とベストプラクティスの詳細については、引き続きお読みください。

{% raw %}

| パーソナライゼーションタグの種類 | タグ |
| -------------  | ---- |
| 標準（デフォルト）属性 | `{{${city}}}` <br> `{{${country}}}` <br> `{{${date_of_birth}}}` <br> `{{${email_address}}}` <br> `{{${first_name}}}` <br> `{{${gender}}}` <br> `{{${language}}}` <br> `{{${last_name}}}` <br> `{{${last_used_app_date}}}` <br> `{{${most_recent_app_version}}}` <br> `{{${most_recent_locale}}}` <br> `{{${most_recent_location}}}` <br> `{{${phone_number}}}` <br> `{{${time_zone}}}` <br> `{{${user_id}}}` <br> `{{${braze_id}}}` <br> `{{${random_bucket_number}}}` <br> `{{subscribed_state.${email_global}}}` <br> `{{subscribed_state.${subscription_group_id}}}` |
| デバイス属性 | `{{most_recently_used_device.${carrier}}}` <br> `{{most_recently_used_device.${id}}}` <br> `{{most_recently_used_device.${idfa}}}` <br> `{{most_recently_used_device.${model}}}` <br> `{{most_recently_used_device.${os}}}` <br> `{{most_recently_used_device.${platform}}}` <br> `{{most_recently_used_device.${google_ad_id}}}` <br> `{{most_recently_used_device.${roku_ad_id}}}` <br> `{{most_recently_used_device.${foreground_push_enabled}}}`|
| <a href='/docs/user_guide/channels/email/subscriptions#changing-email-subscriptions'>メールリスト属性</a> | `{{${set_user_to_unsubscribed_url}}}` <br>このタグは以前の `{{${unsubscribe_url}}}` タグに代わるものです。古いタグは以前に作成されたメールでは引き続き機能しますが、新しいタグの使用を推奨します。 <br><br> `{{${set_user_to_one_click_list_unsubscribe}}}` <br> `{{${set_user_to_subscribed_url}}}` <br> `{{${set_user_to_opted_in_url}}}` |
| <a href='/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting#trigger-messages'>SMS属性</a> | `{{sms.${inbound_message_body}}}` <br> `{{sms.${inbound_media_urls}}}` |
| <a href='/docs/user_guide/channels/whatsapp/message_processing/messaging_users'>WhatsApp属性</a> | `{{whats_app.${inbound_message_body}}}` <br> `{{whats_app.${inbound_media_urls}}}` <br> `{{whats_app.${inbound_flow_response}}}` <br> `{{whats_app.${inbound_product_id}}}` <br> `{{whats_app.${inbound_catalog_id}}}` <br> `{{whats_app.${inbound_profile_name}}}` |
| キャンペーン属性とキャンバスステップ属性 | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| キャンバス属性 | `{{canvas.${name}}}` <br> `{{canvas.${api_id}}}` <br> `{{canvas.${variant_name}}}` <br> `{{canvas.${variant_api_id}}}` |
| カード属性 | `{{card.${api_id}}}` <br> `{{card.${name}}}` |
| ジオフェンスイベント | `{{event_properties.${geofence_name}}}` <br> `{{event_properties.${geofence_set_name}}}` |
| イベントプロパティ <br> （ワークスペースに固有のものです。）| `{{event_properties.${your_custom_event_property}}}` |
| キャンバスコンテキスト変数 | `{{context.${your_context_variable}}}` |
| カスタム属性 <br> （ワークスペースに固有のものです。） | `{{custom_attribute.${your_custom_attribute}}}` |
| <a href='/docs/api/objects_filters/trigger_properties_object'>APIトリガープロパティ</a> | `{{api_trigger_properties.${your_api_trigger_property}}}` |
| キャンバスエントリプロパティ | `{{context.${property_name}}}` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="サポートされているタグの概要" }

{% endraw %}

{% alert note %}
APIトリガープロパティでは、タグごとに2つの波括弧を使用する必要があります: {% raw %}`{{api_trigger_properties.${your_api_trigger_property}}}`。3つの波括弧（例: `{{{...}}}`）{% endraw %}は有効なBrazeパーソナライゼーション構文ではありません。[APIトリガーのLiquidがBrazeで失敗するのはなぜですか？]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/faq#why-is-my-api-triggered-liquid-failing-in-braze)を参照してください。
{% endalert %}

### サポートされている属性 {#supported-attributes}

キャンペーン、カード、キャンバスの属性は、対応するメッセージングテンプレートでのみサポートされています。例えば、`dispatch_id`はメール、プッシュ、SMS、WhatsAppなどのメッセージングチャネルのLiquidでサポートされていますが、アプリ内メッセージやバナーではサポートされていません。

詳細については、[ソース間のキャンペーンとキャンバスの属性]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/campaign_and_canvas_attributes_across_sources)を参照してください。

### キャンバスとキャンペーンのタグの違い {#canvas-and-campaign-tag-differences}

以下のタグの動作は、キャンバスとキャンペーンで異なります:
{% raw %}
- `dispatch_id`の動作が異なるのは、Brazeがキャンバスステップをトリガーイベントとして扱うためです（エントリステップを除く。エントリステップはスケジュール可能です）。詳細については、[ディスパッチIDの動作]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id)を参照してください。
- `{{campaign.${name}}}` タグをキャンバスで使用すると、キャンバスコンポーネント名が表示されます。このタグをキャンペーンで使用すると、キャンペーン名が表示されます。
{% endraw %}

#### URL内のキャンペーン名 {#campaign-names-in-urls}

{% raw %}
キャンペーン名やメッセージバリアント名には、`%`、スペース、`&`など、URLセーフでない文字が含まれる場合があります。`{{campaign.${name}}}` や `{{campaign.${message_name}}}` をリンクやクエリ文字列（`utm_campaign` パラメーターなど）に挿入する場合は、URLが正しく解析されるように [`url_encode`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters#url-filters) フィルターを適用してください。例:

```liquid
https://example.com/?utm_campaign={{ campaign.${name} | url_encode }}
```
{% endraw %}

## 最近使用されたデバイス情報 {#most-recently-used-device-information}

すべてのプラットフォームにわたるユーザーの最新デバイスについて、以下の属性をテンプレート化できます。ユーザーがアプリケーションを使用していない場合（たとえば、REST APIを介してユーザーをインポートした場合）、これらの値はすべて`null`になります。

{% raw %}

| タグ | 説明 |
|---|---|
|`{{most_recently_used_device.${browser}}}` | ユーザーのデバイスで最近使用されたブラウザ。例として「Chrome」や「Safari」があります。 |
|`{{most_recently_used_device.${id}}}` | Brazeデバイス識別子。iOSでは、Apple Identifier for Vendor（IDFV）またはUUIDになります。Androidやその他のプラットフォームでは、ランダムに生成されたUUIDです。 |
| `{{most_recently_used_device.${carrier}}}` | 最近使用されたデバイスの電話サービスキャリア（利用可能な場合）。例として「Verizon」や「Orange」があります。 |
| `{{most_recently_used_device.${ad_tracking_enabled}}}` | デバイスで広告トラッキングが有効かどうか。これはブール値（`true`または`false`）です。 |
| `{{most_recently_used_device.${idfa}}}` | iOSデバイスの場合、アプリケーションがオプションの[IDFAコレクション]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection)で構成されていれば、この値はIdentifier for Advertising（IDFA）になります。iOS以外のデバイスでは、この値はnullです。 |
| `{{most_recently_used_device.${google_ad_id}}}` | Androidデバイスの場合、アプリケーションがオプションのGoogle Play広告ID収集で構成されていれば、この値はGoogle Play広告識別子になります。Android以外のデバイスでは、この値はnullです。 |
| `{{most_recently_used_device.${roku_ad_id}}}` | Rokuデバイスの場合、アプリケーションがBrazeで構成されている際に収集されるRoku広告識別子がこの値になります。Roku以外のデバイスでは、この値はnullです。 |
| `{{most_recently_used_device.${model}}}` | デバイスのモデル名（利用可能な場合）。例として「iPhone 6S」、「Nexus 6P」、「Firefox」があります。 |
| `{{most_recently_used_device.${os}}}` | デバイスのオペレーティングシステム（利用可能な場合）。例として「iOS 9.2.1」、「Android (Lollipop)」、「Windows」があります。 |
| `{{most_recently_used_device.${platform}}}` | デバイスのプラットフォーム（利用可能な場合）。設定されている場合、値は`ios`、`android`、`kindle`、`android_china`、`web`、`tvos`のいずれかです。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="最近使用されたデバイス情報" }

デバイスキャリア、モデル名、オペレーティングシステムは非常に多岐にわたるため、これらの値に条件付きで依存するLiquidは十分にテストすることをお勧めします。特定のデバイスで利用できない場合、これらの値は`null`になります。

## ターゲットアプリ情報 {#targeted-app-information}

アプリ内メッセージでは、Liquid内で以下のアプリ属性を使用できます。値は、アプリがメッセージングをリクエストする際に使用するSDK APIキーに基づいています。

|タグ | 説明 |
|------------------|---|
| `{{app.${api_id}}}` | メッセージをリクエストしているアプリのAPIキー。たとえば、このキーを`abort_message()` Liquidと組み合わせて使用し、TVプラットフォームや別のSDK APIキーを使用する開発ビルドなど、特定のアプリへのアプリ内メッセージの送信を回避できます。|
| `{{app.${name}}}` | メッセージをリクエストしているアプリの名前（Brazeダッシュボードで定義されたもの）。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ターゲットアプリ情報" }

たとえば、以下のLiquidコードは、リクエストしているアプリがリスト内の2つのAPIキーのいずれでもない場合にメッセージを中止します。

```liquid
{% assign allowed_api_keys = 'sdk_api_key_1,sdk_api_key_2' | split: ',' %}
{% if allowed_api_keys contains {{app.${api_id}}} %}
User is in list of apps
{% else %}
{% abort_message("User not in list of apps") %}
{% endif %}
```

## ターゲットデバイス情報 {#targeted-device-information}

プッシュ通知、アプリ内メッセージ、およびBannersでは、メッセージを受信するデバイスの以下の属性をテンプレートに含めることができます。プッシュ通知、アプリ内メッセージ、またはBannerには、ユーザーがメッセージを閲覧するデバイスの属性を含めることができます。これらの属性はContent Cardsやメールでは機能しません。メールの場合、メッセージは送信前にレンダリングされるため、ユーザーがメールを開封するデバイスはその時点では不明です。

|タグ | 説明 |
|------------------|---|
| `{{targeted_device.${id}}}` | Brazeのデバイス識別子です。iOSの場合、Apple Identifier for Vendor（IDFV）またはUUIDになります。Androidやその他のプラットフォームでは、ランダムに生成されたUUIDです。例えば、ユーザーが5台のデバイスを持っている場合、5台すべてのデバイスに対して送信が試行され、それぞれ対応するデバイス識別子が使用されます。メッセージがユーザーの最後に使用したデバイスに送信するよう設定されている場合、Brazeで特定された最後に使用したデバイスに対して1回のみ送信が試行されます。 |
| `{{targeted_device.${carrier}}}` | 最後に使用したデバイスの電話サービスキャリア（利用可能な場合）。例として「Verizon」や「Orange」があります。 |
| `{{targeted_device.${idfa}}}` | iOSデバイスの場合、アプリケーションが[オプションのIDFA収集]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection)で設定されていれば、この値はIdentifier for Advertising（IDFA）になります。iOS以外のデバイスでは、この値はnullです。 |
| `{{targeted_device.${google_ad_id}}}` | Androidデバイスの場合、アプリケーションが[オプションのGoogle Play広告ID収集]で設定されていれば、この値はGoogle Play Advertising Identifierになります。Android以外のデバイスでは、この値はnullです。 |
| `{{targeted_device.${roku_ad_id}}}` | Rokuデバイスの場合、アプリケーションがBrazeで設定されている際に収集されるRoku Advertising Identifierがこの値になります。Roku以外のデバイスでは、この値はnullです。 |
| `{{targeted_device.${model}}}` | デバイスのモデル名（利用可能な場合）。例として「iPhone 6S」、「Nexus 6P」、「Firefox」があります。 |
| `{{targeted_device.${os}}}` | デバイスのオペレーティングシステム（利用可能な場合）。例として「iOS 9.2.1」、「Android (Lollipop)」、「Windows」があります。 |
| `{{targeted_device.${platform}}}` | デバイスのプラットフォーム（利用可能な場合）。設定されている場合、値は`ios`、`android`、`kindle`、`android_china`、`web`、または`tvos`のいずれかです。`most_recently_used_device`パーソナライゼーションタグも使用できます。 |
| `{{targeted_device.${foreground_push_enabled}}}` | ターゲットデバイスでフォアグラウンドプッシュが有効な場合、この値は`true`になり、それ以外の場合は`false`になります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ターゲットデバイス情報" }

{% endraw %}

デバイスキャリア、モデル名、オペレーティングシステムは非常に多岐にわたるため、これらの値に条件付きで依存するロジックは十分にテストすることをお勧めします。これらの値は、特定のデバイスで利用できない場合は`null`になります。

さらに、プッシュ通知の場合、プッシュトークンがAPIを通じてインポートされた場合など、特定の状況下ではBrazeがプッシュ通知に紐づくデバイスを識別できないことがあり、その結果、それらのメッセージの値が`null`になることがあります。

![プッシュメッセージで名変数を使用する際にデフォルト値「there」を使用する例。]({% image_buster /assets/img_archive/personalized_firstname_.png %})

### デフォルト値の代わりに条件付きロジックを使用する {#using-conditional-logic-instead-of-a-default-value}

状況によっては、デフォルト値を設定する代わりに[条件付きロジック]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic)を使用することもできます。条件付きロジックを使用すると、カスタム属性の値に基づいて異なるメッセージを送信できます。さらに、条件付きロジックを使用して、nullまたは空白の属性値を持つ顧客へのメッセージを[中止]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)することもできます。

#### ユースケース {#use-case}

例えば、顧客に報酬残高の通知を送信するとします。デフォルト値を使用して、残高が少ない顧客やnullの残高を持つ顧客に適切に対応する良い方法はありません。

この場合、デフォルト値を設定するよりも適切な2つのオプションがあります。

1. 残高が少ない、null、または空白の顧客に対してメッセージを中止する。

{% raw %}

   ```liquid
   {% if {{custom_attribute.${balance}}} > 0 %}
   Your rewards balance is {{custom_attribute.${balance}}}
   {% else %}
   {% abort_message() %}
   {% endif %}
   ```

{% endraw %}

2. これらの顧客にまったく異なるメッセージを送信する。例えば：

{% raw %}

   ```liquid
   {% if ${first_name} != blank and ${first_name} != null %}
   Hello {{${first_name} | default: 'there'}}, thanks for downloading!
   {% else %}
   Thanks for downloading!
   {% endif %}
   ```

このユースケースでは、名が空白またはnullのユーザーには「Thanks for downloading」というメッセージが届きます。ミスが発生した場合に顧客にLiquidが表示されないよう、名に[デフォルト値]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values)を含めるようにしてください。

{% endraw %}

## 変数タグ {#variable-tags}

`assign`タグを使用して、メッセージ作成画面で変数を作成できます。変数には一意の名前を使用することをお勧めします。サポートされているパーソナライゼーションタグ（`language`など）と類似した名前で変数を作成すると、メッセージングロジックに影響を与える可能性があります。

変数を作成した後、メッセージングロジックやメッセージ内でその変数を参照できます。このタグは、[Connected Content]({% image_buster /assets/img_archive/personalized_firstname_.png %})機能から返されるコンテンツを再フォーマットしたい場合に便利です。詳細については、Shopifyのドキュメントの[変数タグ](https://docs.shopify.com/themes/liquid/tags/variable-tags)を参照してください。

{% alert important %}
`assign`タグ内でシングルクォートで囲まれた文字列は、リテラル文字列として扱われます。シングルクォート内のLiquidパーソナライゼーションタグは展開されません。例：

{% raw %}
```liquid
{% assign name_intro = 'My name is {{${first_name}}}' %}
{{ name_intro }}
```
{% endraw %}

この場合、ユーザーの名ではなく、リテラルテキスト{% raw %}`My name is {{${first_name}}}`{% endraw %}がそのまま出力されます。

パーソナライゼーションを含めるには、変数を使用するか、[`append`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters#string-filters)フィルターで文字列を連結してください。パーソナライゼーションを使用したURLテンプレートについては、[リンクテンプレート]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template)を参照してください。
{% endalert %}

{% alert tip %}
毎回のメッセージで同じ変数を割り当てていませんか？`assign`タグを何度も書く代わりに、そのタグをコンテンツブロックとして保存し、メッセージの先頭に配置できます。

1. [コンテンツブロックを作成します]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks#create-a-content-block)。
2. コンテンツブロックに名前を付けます（スペースや特殊文字は使用しないでください）。
3. ページ下部の**編集**を選択します。
4. `assign`タグを入力します。

コンテンツブロックがメッセージの先頭にある限り、変数がオブジェクトとしてメッセージに挿入されるたびに、選択したカスタム属性を参照します。
{% endalert %}

### ユースケース

顧客が報酬ポイントを100ポイント貯めた後に、そのポイントを賞品と交換できるようにしているとします。この場合、追加購入を行った場合にポイント残高が100以上になる顧客にのみメッセージを送信したいとします：

{% raw %}
```liquid
{% assign new_points_balance = {{custom_attribute.${current_rewards_balance} | plus: 50}} %}
{% if new_points_balance >= 100 %}
Make a purchase to bring your rewards points to {{new_points_balance}} and cash in today!
{% else %}
{% abort_message('not enough points') %}
{% endif %}
```
{% endraw %}

## 反復タグ {#iteration-tags}

{% raw %}
反復タグは、コードブロックを繰り返し実行するために使用できます。以下のユースケースでは、`for` タグを取り上げます。

### ユースケース

Nike のスニーカーのセールを実施しており、Nike に興味を示した顧客にメッセージを送りたいとします。各顧客のプロファイルには、閲覧した商品ブランドの配列があります。この配列には最大25の商品ブランドが含まれる可能性がありますが、直近5件の商品閲覧のうち Nike の商品を閲覧した顧客にのみメッセージを送りたいとします。

```liquid
{% for items in {{custom_attribute.${Brands Viewed}}} limit:5 %}
{% if {{items}} contains 'Converse' %}
{% assign converse_viewer = true %}
{% endif %}
{% endfor %}
{% if converse_viewer == true %}
Sale on Converse!
{% else %}
{% abort_message() %}
{% endif %}
```

このユースケースでは、閲覧されたスニーカーブランドの配列の最初の5つの項目を確認します。それらの項目のいずれかが Converse であれば、`converse_viewer` 変数を作成し、true に設定します。

次に、`converse_viewer` が true の場合にセールメッセージを送信します。それ以外の場合は、メッセージを中止します。

これは、Brazeのメッセージ作成画面で反復タグを使用する方法の簡単な例です。詳細については、Shopify のドキュメントの[反復タグ](https://docs.shopify.com/themes/liquid/tags/iteration-tags)を参照してください。

## 構文タグ {#syntax-tags}

構文タグを使用して、Liquidのレンダリング方法を制御できます。`echo`タグを使用して式を返すことができます。これは式を中括弧で囲むのと同じですが、このタグはLiquidタグ内で使用できます。また、`liquid`タグを使用すると、各タグにデリミターを付けずにLiquidのブロックを記述できます。`liquid`タグを使用する場合、各タグはそれぞれ独立した行に記述する必要があります。詳細と例については、Shopifyの[構文タグ](https://shopify.dev/api/liquid/tags#syntax-tags)に関するドキュメントを参照してください。

[空白制御](https://shopify.github.io/liquid/basics/whitespace/)を使用すると、タグの周囲の空白を削除でき、Liquidの出力の見た目をさらに細かく制御できます。

## HTTPステータスコード {#http-personalization}

[Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)呼び出しのHTTPステータスを利用するには、まずローカル変数として保存し、次に `__http_status_code__` キーを使用します。例えば：

```html
{% connected_content https://example.com/api/endpoint :save connected %}
{% if connected.__http_status_code__ != 200 %}
{% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert note %}
このキーは、エンドポイントがJSONオブジェクトを返す場合にのみ、Connected Contentオブジェクトに自動的に追加されます。エンドポイントが配列やその他の型を返す場合、そのキーはレスポンスに自動的に設定できません。
{% endalert %}

## 言語、最新のロケール、タイムゾーンに基づいてメッセージを送信する {#send-messages-based-on-language-most-recent-locale-and-time-zone}

状況によっては、特定のロケールに固有のメッセージを送信したい場合があります。たとえば、ブラジルポルトガル語は通常、ヨーロッパポルトガル語とは異なります。

### ユースケース: 最新のロケールに基づいてローカライズする {#use-case-localize-based-on-recent-locale}

最新のロケールを使用して、国際化されたメッセージをさらにローカライズする方法のユースケースを以下に示します。

{% raw %}

```liquid
{% if ${language} == 'en' %}
Message in English
{% elsif  ${language} == 'fr' %}
Message in French
{% elsif  ${language} == 'ja' %}
Message in Japanese
{% elsif  ${language} == 'ko' %}
Message in Korean
{% elsif  ${language} == 'ru' %}
Message in Russian
{% elsif ${most_recent_locale} == 'pt_BR' %}
Message in Brazilian Portuguese
{% elsif ${most_recent_locale} == 'pt_PT' %}
Message in European Portuguese
{% elsif  ${language} == 'pt' %}
Message in default Portuguese
{% else %}
Message in default language
{% endif %}
```

このユースケースでは、最新のロケールが `pt_BR` の顧客にはブラジルポルトガル語のメッセージが送信され、最新のロケールが `pt_PT` の顧客にはヨーロッパポルトガル語のメッセージが送信されます。最初の2つの条件を満たさないが、言語がポルトガル語に設定されている顧客には、デフォルトのポルトガル語タイプとして設定したメッセージが送信されます。

### ユースケース: タイムゾーンでユーザーをターゲットにする {#use-case-target-users-by-time-zone}

タイムゾーンでユーザーをターゲットにすることもできます。たとえば、EST にいるユーザーには1つのメッセージを送信し、PST にいるユーザーには別のメッセージを送信します。これを行うには、現在の時刻を UTC で保存し、if/else ステートメントをユーザーの現在の時刻と比較して、適切なタイムゾーンに適切なメッセージを送信します。ユーザーのローカルタイムゾーンでキャンペーンを送信するように設定し、適切なタイミングでキャンペーンを届けるようにしてください。

以下のユースケースでは、午後2時から午後3時の間に配信されるメッセージを、各タイムゾーンに固有のメッセージとして記述する方法を示しています。

```liquid
{% assign hour_in_utc = 'now' | date: '%H' | plus:0 %}
{% if hour_in_utc >= 19 && hour_in_utc < 20 %}
It is between 2:00:00 pm and 2:59:59 pm ET!
{% elsif hour_in_utc >= 22 && hour_in_utc < 23 %}
It is between 2:00:00 pm and 2:59:59 pm PT!
{% else %}
{% abort_message %}
{% endif %}
```

{% endraw %}

## ランダムな数値を使ってメッセージを送信する {#send-messages-with-a-random-number}

{% raw %}
`{% random %}` タグはランダムな数値を返します。A/Bスタイルのロジック、サンプリング、またはメッセージコンテンツのバリエーションに使用できます。

| タグ | 説明 |
|-------|--------------|
| `{% random %}` | 0以上1未満の浮動小数点数（0を含み、1を含まない）。 |
| `{% random 10 %}`（整数引数） | 0以上、指定した整数未満の整数。たとえば、`{% random 10 %}` は0から9の整数を返します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ランダムな数値を使ってメッセージを送信する" }

{% endraw %}

### ユースケース: ユーザーにランダムなバリアントを送信する {#use-case-send-users-random-variants}

{% raw %}
```liquid
{% capture roll_str %}{% random %}{% endcapture %}
{% assign roll = roll_str | plus: 0 %}
{% if roll < 0.5 %}
Show variant A
{% else %}
Show variant B
{% endif %}
```
{% endraw %}

## eコマースショッピングカートタグ {#shopping-cart-tag}

`shopping_cart` タグは、eコマースの[カート放棄]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases?tab=abandoned%20cart#abandoned-cart)および[チェックアウト放棄]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases?tab=abandoned%20checkout#abandoned-checkout)のキャンバスユースケースで、ユーザーのカート内容にアクセスします。`CART_ID` を実際のカートID値（{% raw %}`{{context.${cart_id}}}`{% endraw %} など）に置き換えてください。

{% raw %}
```liquid
{% shopping_cart CART_ID :abort_if_not_abandoned false %}
```
{% endraw %}

この例の `abort_if_not_abandoned` パラメーターは、`ecommerce.checkout_started` イベントと併用する[チェックアウト放棄]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases?tab=abandoned%20checkout#abandoned-checkout)のユースケースにのみ適用されます。カート放棄のユースケースには適用されません。詳細については、[`abort_if_not_abandoned`]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases?tab=abandoned%20checkout#abort-if-not-abandoned) を参照してください。

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags