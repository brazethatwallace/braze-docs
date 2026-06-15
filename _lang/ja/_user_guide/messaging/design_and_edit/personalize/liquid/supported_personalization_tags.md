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
| 標準 (デフォルト) 属性 | `{{${city}}}` <br> `{{${country}}}` <br> `{{${date_of_birth}}}` <br> `{{${email_address}}}` <br> `{{${first_name}}}` <br> `{{${gender}}}` <br> `{{${language}}}` <br> `{{${last_name}}}` <br> `{{${last_used_app_date}}}` <br> `{{${most_recent_app_version}}}` <br> `{{${most_recent_locale}}}` <br> `{{${most_recent_location}}}` <br> `{{${phone_number}}}` <br> `{{${time_zone}}}` <br> `{{${user_id}}}` <br> `{{${braze_id}}}` <br> `{{${random_bucket_number}}}` <br> `{{subscribed_state.${email_global}}}` <br> `{{subscribed_state.${subscription_group_id}}}` |
| デバイス属性 | `{{most_recently_used_device.${carrier}}}` <br> `{{most_recently_used_device.${id}}}` <br> `{{most_recently_used_device.${idfa}}}` <br> `{{most_recently_used_device.${model}}}` <br> `{{most_recently_used_device.${os}}}` <br> `{{most_recently_used_device.${platform}}}` <br> `{{most_recently_used_device.${google_ad_id}}}` <br> `{{most_recently_used_device.${roku_ad_id}}}` <br> `{{most_recently_used_device.${foreground_push_enabled}}}`|
| <a href='/docs/user_guide/channels/email/subscriptions#managing-user-subscriptions'>メールリスト属性</a> | `{{${set_user_to_unsubscribed_url}}}` <br>このタグは以前の `{{${unsubscribe_url}}}` タグに代わるものです。以前のタグは過去に作成されたメールでは引き続き機能しますが、新しいタグの使用を推奨します。<br><br> `{{${set_user_to_one_click_list_unsubscribe}}}` <br> `{{${set_user_to_subscribed_url}}}` <br> `{{${set_user_to_opted_in_url}}}` |
| <a href='/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting#trigger-messages'>SMS 属性</a> | `{{sms.${inbound_message_body}}}` <br> `{{sms.${inbound_media_urls}}}` |
| <a href='/docs/user_guide/channels/whatsapp/message_processing/messaging_users'>WhatsApp 属性</a> | `{{whats_app.${inbound_message_body}}}` <br> `{{whats_app.${inbound_media_urls}}}` <br> `{{whats_app.${inbound_flow_response}}}` <br> `{{whats_app.${inbound_product_id}}}` <br> `{{whats_app.${inbound_catalog_id}}}` <br> `{{whats_app.${inbound_profile_name}}}` |
| Campaign属性とキャンバスステップ属性 | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| Canvas属性 | `{{canvas.${name}}}` <br> `{{canvas.${api_id}}}` <br> `{{canvas.${variant_name}}}` <br> `{{canvas.${variant_api_id}}}` |
| カード属性 | `{{card.${api_id}}}` <br> `{{card.${name}}}` |
| ジオフェンスイベント | `{{event_properties.${geofence_name}}}` <br> `{{event_properties.${geofence_set_name}}}` |
| イベントプロパティ <br> (ワークスペースに固有のものです。)| `{{event_properties.${your_custom_event_property}}}` |
| Canvasコンテキスト変数 | `{{context.${your_context_variable}}}` |
| カスタム属性 <br> (ワークスペースに固有のものです。) | `{{custom_attribute.${your_custom_attribute}}}` |
| <a href='/docs/api/objects_filters/trigger_properties_object/'>API トリガープロパティ</a> | `{{api_trigger_properties.${your_api_trigger_property}}}` |
| Canvasエントリプロパティ | `{{context.${property_name}}}` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Summary of supported tags" }

{% endraw %}

### サポートされている属性 {#supported-attributes}

Campaign、カード、Canvasの属性は、対応するメッセージングテンプレートでのみサポートされています（例えば、`dispatch_id` はアプリ内メッセージCampaignでは使用できません）。

詳細については、[ソース別のCampaignおよびCanvas属性]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/campaign_and_canvas_attributes_across_sources/)を参照してください。

### CanvasとCampaignのタグの違い {#canvas-and-campaign-tag-differences}

以下のタグの動作は、CanvasとCampaignで異なります。
{% raw %}
- `dispatch_id` の動作が異なるのは、Brazeがキャンバスステップを（「スケジュール済み」であっても）トリガーイベントとして扱うためです（スケジュール可能なエントリステップを除く）。詳細については、[ディスパッチ ID の動作]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id/)を参照してください。
- Canvasで `{{campaign.${name}}}` タグを使用すると、Canvasコンポーネント名が表示されます。Campaignでこのタグを使用すると、Campaign名が表示されます。
{% endraw %}

#### URL 内のCampaign名 {#campaign-names-in-urls}
{: #campaign-names-in-urls}

{% raw %}
Campaignおよびメッセージバリアント名には、`%`、スペース、`&` など、URLセーフでない文字が含まれる場合があります。`{{campaign.${name}}}` または `{{campaign.${message_name}}}` をリンクやクエリ文字列（`utm_campaign` パラメーターなど）に挿入する場合は、URLが正しく解析されるように [`url_encode`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/#url-filters) フィルターを適用してください。例えば：

```liquid
https://example.com/?utm_campaign={{ campaign.${name} | url_encode }}
```
{% endraw %}

## 最近使用したデバイスの情報 {#most-recently-used-device-information}

すべてのプラットフォームにわたって、ユーザーの最新デバイスの以下の属性をテンプレート化できます。ユーザーがアプリケーションを使用したことがない場合（例えば、REST API経由でユーザーをインポートした場合）、これらの値はすべて `null` になります。

{% raw %}

| タグ | 説明 |
|---|---|
|`{{most_recently_used_device.${browser}}}` | ユーザーのデバイスで最近使用されたブラウザです。例として「Chrome」や「Safari」があります。|
|`{{most_recently_used_device.${id}}}` | Brazeデバイス識別子です。iOSでは、Apple Identifier for Vendor (IDFV) または UUID になります。Androidやその他のプラットフォームでは、ランダムに生成された UUID です。|
| `{{most_recently_used_device.${carrier}}}` | 最近使用されたデバイスの電話サービスキャリアです（利用可能な場合）。例として「Verizon」や「Orange」があります。|
| `{{most_recently_used_device.${ad_tracking_enabled}}}` | デバイスで広告トラッキングが有効かどうかを示します。ブール値（`true` または `false`）です。|
| `{{most_recently_used_device.${idfa}}}` | iOSデバイスの場合、アプリケーションがオプションの [IDFA 収集]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/)で設定されていれば、この値は Identifier for Advertising (IDFA) になります。iOS以外のデバイスでは、この値は null です。|
| `{{most_recently_used_device.${google_ad_id}}}` | Androidデバイスの場合、アプリケーションがオプションの Google Play 広告 ID 収集で設定されていれば、この値は Google Play Advertising Identifier になります。Android以外のデバイスでは、この値は null です。|
| `{{most_recently_used_device.${roku_ad_id}}}` | Rokuデバイスの場合、アプリケーションがBrazeで設定されているときに収集される Roku Advertising Identifier がこの値になります。Roku以外のデバイスでは、この値は null です。|
| `{{most_recently_used_device.${model}}}` | デバイスのモデル名です（利用可能な場合）。例として「iPhone 6S」、「Nexus 6P」、「Firefox」があります。|
| `{{most_recently_used_device.${os}}}` | デバイスのオペレーティングシステムです（利用可能な場合）。例として「iOS 9.2.1」、「Android (Lollipop)」、「Windows」があります。|
| `{{most_recently_used_device.${platform}}}` | デバイスのプラットフォームです（利用可能な場合）。設定されている場合、値は `ios`、`android`、`kindle`、`android_china`、`web`、`tvos` のいずれかです。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Most recently used device information" }

デバイスキャリア、モデル名、オペレーティングシステムは非常に多岐にわたるため、これらの値に条件付きで依存する Liquid は十分にテストすることを推奨します。特定のデバイスで利用できない場合、これらの値は `null` になります。

## ターゲットアプリの情報 {#targeted-app-information}

アプリ内メッセージでは、Liquid 内で以下のアプリ属性を使用できます。値は、アプリがメッセージングをリクエストする際に使用するSDK APIキーに基づいています。

| タグ | 説明 |
|------------------|---|
| `{{app.${api_id}}}` | メッセージをリクエストしているアプリのAPIキーです。例えば、このキーを `abort_message()` Liquid と組み合わせて使用し、TVプラットフォームや別のSDK APIキーを使用する開発ビルドなど、特定のアプリへのアプリ内メッセージの送信を回避できます。|
| `{{app.${name}}}` | メッセージをリクエストしているアプリの名前です（Brazeダッシュボードで定義されたもの）。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Targeted app information" }

例えば、以下の Liquid コードは、リクエストしているアプリがリスト内の 2 つのAPIキーのいずれでもない場合にメッセージを中止します。

```liquid
{% assign allowed_api_keys = 'sdk_api_key_1,sdk_api_key_2' | split: ',' %}
{% if allowed_api_keys contains {{app.${api_id}}} %}
User is in list of apps
{% else %}
{% abort_message("User not in list of apps") %}
{% endif %}
```

## ターゲットデバイスの情報 {#targeted-device-information}

プッシュ通知、アプリ内メッセージ、バナーでは、メッセージを受信するデバイスの以下の属性をテンプレート化できます。プッシュ通知、アプリ内メッセージ、またはバナーには、ユーザーがメッセージを読むデバイスの属性を含めることができます。これらの属性はContent Cardsやメールでは機能しません。メールの場合、メッセージは送信前にレンダリングされるため、ユーザーがメールを開くデバイスはその時点では不明です。

| タグ | 説明 |
|------------------|---|
| `{{targeted_device.${id}}}` | Brazeデバイス識別子です。iOSでは、Apple Identifier for Vendor (IDFV) または UUID になります。Androidやその他のプラットフォームでは、ランダムに生成された UUID です。例えば、ユーザーが 5 台のデバイスを持っている場合、5 台すべてのデバイスに対して送信が試行され、それぞれ対応するデバイス識別子が使用されます。メッセージがユーザーの最近使用したデバイスに送信するよう設定されている場合、Brazeで特定された最近使用したデバイスに対して 1 回のみ送信が試行されます。|
| `{{targeted_device.${carrier}}}` | 最近使用されたデバイスの電話サービスキャリアです（利用可能な場合）。例として「Verizon」や「Orange」があります。|
| `{{targeted_device.${idfa}}}` | iOSデバイスの場合、アプリケーションがオプションの [IDFA 収集]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/)で設定されていれば、この値は Identifier for Advertising (IDFA) になります。iOS以外のデバイスでは、この値は null です。|
| `{{targeted_device.${google_ad_id}}}` | Androidデバイスの場合、アプリケーションがオプションの [Google Play 広告 ID 収集]で設定されていれば、この値は Google Play Advertising Identifier になります。Android以外のデバイスでは、この値は null です。|
| `{{targeted_device.${roku_ad_id}}}` | Rokuデバイスの場合、アプリケーションがBrazeで設定されているときに収集される Roku Advertising Identifier がこの値になります。Roku以外のデバイスでは、この値は null です。|
| `{{targeted_device.${model}}}` | デバイスのモデル名です（利用可能な場合）。例として「iPhone 6S」、「Nexus 6P」、「Firefox」があります。|
| `{{targeted_device.${os}}}` | デバイスのオペレーティングシステムです（利用可能な場合）。例として「iOS 9.2.1」、「Android (Lollipop)」、「Windows」があります。|
| `{{targeted_device.${platform}}}` | デバイスのプラットフォームです（利用可能な場合）。設定されている場合、値は `ios`、`android`、`kindle`、`android_china`、`web`、`tvos` のいずれかです。`most_recently_used_device` パーソナライゼーションタグも使用できます。|
| `{{targeted_device.${foreground_push_enabled}}}` | ターゲットデバイスでフォアグラウンドプッシュが有効な場合、この値は `true` になり、それ以外の場合は `false` になります。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Targeted device information" }

{% endraw %}

デバイスキャリア、モデル名、オペレーティングシステムは非常に多岐にわたるため、これらの値に条件付きで依存するロジックは十分にテストすることを推奨します。特定のデバイスで利用できない場合、これらの値は `null` になります。

さらに、プッシュ通知の場合、プッシュトークンがAPI経由でインポートされた場合など、特定の状況下ではBrazeがプッシュ通知に関連付けられたデバイスを識別できないことがあり、その結果、それらのメッセージの値が `null` になります。

![プッシュメッセージで名変数を使用する際にデフォルト値として「there」を使用する例。]({% image_buster /assets/img_archive/personalized_firstname_.png %})

### デフォルト値の代わりに条件付きロジックを使用する {#using-conditional-logic-instead-of-a-default-value}

状況によっては、デフォルト値を設定する代わりに[条件付きロジック]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic/)を使用することもできます。条件付きロジックを使用すると、カスタム属性の値に基づいて異なるメッセージを送信できます。さらに、条件付きロジックを使用して、null または空白の属性値を持つ顧客への[メッセージを中止]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/)することもできます。

#### ユースケース {#use-case}

例えば、顧客に報酬残高通知を送信するとします。デフォルト値を使用して、残高が少ない顧客や null の顧客に適切に対応する良い方法はありません。

この場合、デフォルト値を設定するよりも適切な 2 つのオプションがあります。

1. 残高が少ない、null、または空白の顧客に対してメッセージを中止します。

{% raw %}

   ```liquid
   {% if {{custom_attribute.${balance}}} > 0 %}
   Your rewards balance is {{custom_attribute.${balance}}}
   {% else %}
   {% abort_message() %}
   {% endif %}
   ```

{% endraw %}

2. これらの顧客にまったく異なるメッセージを送信します。例えば：

{% raw %}

   ```liquid
   {% if ${first_name} != blank and ${first_name} != null %}
   Hello {{${first_name} | default: 'there'}}, thanks for downloading!
   {% else %}
   Thanks for downloading!
   {% endif %}
   ```

このユースケースでは、名が空白または null のユーザーには「Thanks for downloading!」というメッセージが届きます。ミスが発生した場合に顧客に Liquid が表示されないよう、名に[デフォルト値]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values/)を含めることを推奨します。

{% endraw %}

## 変数タグ {#variable-tags}

`assign` タグを使用して、メッセージ作成画面で変数を作成できます。変数にはユニークな名前を使用することを推奨します。サポートされているパーソナライゼーションタグ（`language` など）と類似した名前の変数を作成すると、メッセージングロジックに影響を与える可能性があります。

変数を作成した後、メッセージングロジックやメッセージ内でその変数を参照できます。このタグは、[コネクテッドコンテンツ]({% image_buster /assets/img_archive/personalized_firstname_.png %})機能から返されるコンテンツを再フォーマットしたい場合に便利です。詳細については、Shopifyのドキュメントの[変数タグ](https://docs.shopify.com/themes/liquid/tags/variable-tags)を参照してください。

{% alert tip %}
毎回のメッセージで同じ変数を割り当てていませんか？`assign` タグを何度も書く代わりに、そのタグをコンテンツブロックとして保存し、メッセージの先頭に配置できます。

1. [コンテンツブロックを作成]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/#create-a-content-block)します。
2. コンテンツブロックに名前を付けます（スペースや特殊文字は使用しないでください）。
3. ページ下部の**編集**を選択します。
4. `assign` タグを入力します。

コンテンツブロックがメッセージの先頭にある限り、変数がオブジェクトとしてメッセージに挿入されるたびに、選択したカスタム属性を参照します。
{% endalert %}

### ユースケース

顧客が報酬ポイントを 100 ポイント貯めた後にポイントを賞品に交換できるとします。そのため、追加購入を行った場合にポイント残高が 100 以上になる顧客にのみメッセージを送信したいとします。

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
反復タグを使用して、コードブロックを繰り返し実行できます。以下のユースケースでは `for` タグを使用しています。

### ユースケース

Nike のスニーカーのセールを開催しており、Nike に興味を示した顧客にメッセージを送信したいとします。各顧客のプロファイルには、閲覧した製品ブランドの配列があります。この配列には最大 25 の製品ブランドが含まれる可能性がありますが、直近 5 回の製品閲覧のうち Nike の製品を閲覧した顧客にのみメッセージを送信したいとします。

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

このユースケースでは、閲覧したスニーカーブランドの配列の最初の 5 つのアイテムを確認します。そのうちの 1 つが Converse であれば、`converse_viewer` 変数を作成して true に設定します。

次に、`converse_viewer` が true の場合にセールメッセージを送信します。それ以外の場合はメッセージを中止します。

これは、Brazeのメッセージ作成画面で反復タグを使用する方法の簡単な例です。詳細については、Shopifyのドキュメントの[反復タグ](https://docs.shopify.com/themes/liquid/tags/iteration-tags)を参照してください。

## 構文タグ {#syntax-tags}

構文タグを使用して、Liquid のレンダリング方法を制御できます。`echo` タグを使用して式を返すことができます。これは式を波括弧で囲むのと同じですが、Liquid タグ内でこのタグを使用できます。また、`liquid` タグを使用して、各タグにデリミタを付けずに Liquid のブロックを記述できます。`liquid` タグを使用する場合、各タグは独自の行に記述する必要があります。詳細と例については、Shopifyのドキュメントの[構文タグ](https://shopify.dev/api/liquid/tags#syntax-tags)を参照してください。

[空白制御](https://shopify.github.io/liquid/basics/whitespace/)を使用すると、タグの周囲の空白を削除でき、Liquid の出力の見た目をさらに制御できます。

## HTTP ステータスコード {#http-personalization}

[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)呼び出しの HTTP ステータスを利用するには、まずローカル変数として保存し、次に `__http_status_code__` キーを使用します。例えば：

```html
{% connected_content https://example.com/api/endpoint :save connected %}
{% if connected.__http_status_code__ != 200 %}
{% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert note %}
このキーは、エンドポイントが JSON オブジェクトを返す場合にのみ、コネクテッドコンテンツオブジェクトに自動的に追加されます。エンドポイントが配列やその他の型を返す場合、そのキーはレスポンスに自動的に設定できません。
{% endalert %}

## 言語、最新ロケール、タイムゾーンに基づいたメッセージ送信 {#send-messages-based-on-language-most-recent-locale-and-time-zone}

状況によっては、特定のロケールに固有のメッセージを送信したい場合があります。例えば、ブラジルポルトガル語は通常、ヨーロッパポルトガル語とは異なります。

### ユースケース：最新ロケールに基づくローカライズ {#use-case-localize-based-on-recent-locale}

最新ロケールを使用して、国際化されたメッセージをさらにローカライズする方法のユースケースを紹介します。

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

このユースケースでは、最新ロケールが `pt_BR` の顧客にはブラジルポルトガル語のメッセージが届き、最新ロケールが `pt_PT` の顧客にはヨーロッパポルトガル語のメッセージが届きます。最初の 2 つの条件に該当しないが、言語がポルトガル語に設定されている顧客には、デフォルトのポルトガル語タイプとして設定したメッセージが届きます。

### ユースケース：タイムゾーンによるユーザーのターゲティング {#use-case-target-users-by-time-zone}

タイムゾーンによってユーザーをターゲティングすることもできます。例えば、EST にいるユーザーには 1 つのメッセージを送信し、PST にいるユーザーには別のメッセージを送信します。これを行うには、現在の時刻を UTC で保存し、if/else 文をユーザーの現在の時刻と比較して、適切なタイムゾーンに適切なメッセージを送信します。ユーザーのローカルタイムゾーンで送信するようCampaignを設定し、適切な時間にCampaignが届くようにする必要があります。

以下のユースケースでは、午後 2 時から午後 3 時の間に配信されるメッセージを、各タイムゾーン向けの特定のメッセージで記述する方法を示します。

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

## ランダムな数値を使用したメッセージ送信 {#send-messages-with-a-random-number}

{% raw %}
`{% random %}` タグはランダムな数値を返します。A/B テストスタイルのロジック、サンプリング、またはメッセージコンテンツのバリエーションに使用できます。

| タグ | 説明 |
|-------|--------------|
| `{% random %}` | 0 から 1 の間の浮動小数点数（0 を含み、1 を含まない）です。|
| `{% random 10 %}` (整数引数) | 0 から指定した整数未満までの整数です。例えば、`{% random 10 %}` は 0 から 9 の整数を返します。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Send messages with a random number" }

{% endraw %}

### ユースケース：ユーザーにランダムなバリアントを送信する {#use-case-send-users-random-variants}

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

`shopping_cart` タグは、eコマースの[カート放棄]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/?tab=abandoned%20cart#abandoned-cart)および[チェックアウト放棄]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/?tab=abandoned%20checkout#abandoned-checkout)のCanvasユースケースで、ユーザーのカート内容にアクセスします。`CART_ID` を実際のカート ID 値（{% raw %}`{{context.${cart_id}}}`{% endraw %} など）に置き換えてください。

{% raw %}
```liquid
{% shopping_cart CART_ID :abort_if_not_abandoned false %}
```
{% endraw %}

この例の `abort_if_not_abandoned` パラメーターは、`ecommerce.checkout_started` イベントと併用する[チェックアウト放棄]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/?tab=abandoned%20checkout#abandoned-checkout)のユースケースにのみ適用されます。カート放棄のユースケースには適用されません。詳細については、[`abort_if_not_abandoned`]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/?tab=abandoned%20checkout#abort-if-not-abandoned) を参照してください。

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags