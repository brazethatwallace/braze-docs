---
nav_title: Braze アクションクレジットの説明
permalink: "/message_credits_descriptions/"
hidden: true
noindex: true
hide_toc: true
---

# Braze アクションクレジットの説明 {#braze-action-credits-descriptions}

> アクションクレジットは、マルチチャネルメッセージングや高度なAI製品に簡単にアクセスしながら、マーケティング予算を最大限に活用できる柔軟な仕組みを提供します。まずは単一のチャネルやリージョンでエンゲージメントを開始し、ビジネスモデル、顧客基盤、エンゲージメント戦略の進化に合わせて、AIエージェントを含むチャネルミックスをシームレスに拡大できます。

アクションクレジットは、このページに記載されているすべてのチャネルおよび機能に適用できます。

このページで参照される「クレジット比率」とは、指定されたアクションを実行するために必要なアクションクレジットの正確な数として定義されます。

## 目次 {#table-of-contents}

- [メールチャネルの詳細](#email-channel-details)
- [SMS、MMS、RCSチャネルの詳細](#sms-mms-and-rcs-channel-details)
  - [SMSセグメント](#sms-segments)
  - [MMSメッセージ](#mms-messages)
  - [RCSタイプ](#rcs-types)
- [WhatsAppチャネルの詳細](#whatsapp-channel-details)
  - [請求リージョンの内訳](#billing-region-breakdown)
- [エージェントコンソールの詳細](#agent-console-details)
- [その他のチャネルの詳細](#additional-channel-details)
  - [LINE](#line)
  - [KakaoTalk](#kakaotalk)
  - [Content Cards](#content-cards)
  - [バナー](#banners)
  - [オーディエンス同期](#audience-sync)
  - [メッセージアーカイブ](#message-archiving)
  - [Webhook](#webhooks)

## メールチャネルの詳細 {#email-channel-details}

メールクレジットの比率は、Brazeプラットフォームから送信されるメール1,000通単位（CPM）で計算されます。

{% alert note %}
メールチャネルの詳細については、[メールドキュメント]({{site.baseurl}}/user_guide/message_building_by_channel/email)を参照してください。
{% endalert %}

## SMS、MMS、RCSチャネルの詳細 {#sms-mms-and-rcs-channel-details}

SMSおよびMMSのクレジット比率は、Brazeプラットフォームから送信されたセグメント単位で計算されます。RCSのクレジット比率は、Brazeプラットフォームから配信されたBasicおよびRich Mediaタイプ、またはSingleおよびRich Mediaタイプの単位で計算されます。受信と送信の両方のタイプが課金対象となります。

{% alert note %}
これらのチャネルに該当する場合、キャリア料金は別途（後払いで）請求され、アクションクレジットの一部とはみなされません。
{% endalert %}

### SMSセグメント {#sms-segments}

SMS業界では、メッセージをSMSメッセージセグメント単位でカウントします。メッセージセグメントとは、定義された文字数（GSM-7エンコーディングの場合は160文字、UCS-2エンコーディングの場合は67文字）までのグループであり、1回のSMS送信で送られます。GSM-7エンコーディングを使用して161文字のSMSを送信した場合、2つのメッセージセグメントが送信されます。複数のメッセージセグメントを送信すると、追加料金が発生します。

### MMSメッセージ {#mms-messages}

MMSの場合、メッセージの上限は5 MBです（これにはマルチメディアアセットとメッセージ本文のサイズが含まれます）。安全のため、Brazeではマルチメディアアセットを600 KB以下に抑え、メッセージ本文も含めることを推奨しています。

### RCSタイプ {#rcs-types}

RCSはSMSおよびMMSの次世代版です。SMSのようなダイレクトで高エンゲージメントなチャネルの利点を備えつつ、リッチコンテンツ（画像、動画、ドキュメント）、認証済みおよびブランド付き送信、提案された返信やアクションなどのインタラクティブ機能など、現代の消費者が期待するよりリッチな機能を提供します。

{% multi_lang_include pricing/rcs_billing_message_types.md %}

{% alert note %}
BrazeのSMSファミリーの提供内容について詳しくは、[SMSおよびMMSドキュメント]({{site.baseurl}}/user_guide/message_building_by_channel/sms)を参照してください。
{% endalert %}

## WhatsAppチャネルの詳細 {#whatsapp-channel-details}

{% multi_lang_include whatsapp/about_credits.md content="h3" %}

## 請求リージョンの内訳 {#billing-region-breakdown}

### 北米 {#north-america}

米国、カナダ

### その他のアフリカ {#rest-of-africa}

アルジェリア、アンゴラ、ベナン、ボツワナ、ブルキナファソ、ブルンジ、カメルーン、チャド、コンゴ、エリトリア、エチオピア、ガボン、ガンビア、ガーナ、ギニアビサウ、コートジボワール、ケニア、レソト、リベリア、リビア、マダガスカル、マラウイ、マリ、モーリタニア、モロッコ、モザンビーク、ナミビア、ニジェール、ルワンダ、セネガル、シエラレオネ、ソマリア、南スーダン、スーダン、エスワティニ、タンザニア、トーゴ、チュニジア、ウガンダ、ザンビア

### その他のアジア太平洋 {#rest-of-asia-pacific}

アフガニスタン、オーストラリア、バングラデシュ、カンボジア、中国、日本、ラオス、モンゴル、ネパール、ニュージーランド、パプアニューギニア、フィリピン、スリランカ、台湾、タジキスタン、タイ、トルクメニスタン、ウズベキスタン、ベトナム

### その他の中央・東ヨーロッパ {#rest-of-central-eastern-europe}

アルバニア、アルメニア、アゼルバイジャン、ベラルーシ、ブルガリア、クロアチア、チェコ共和国、ジョージア、ギリシャ、ラトビア、リトアニア、マケドニア、モルドバ、セルビア、スロバキア、スロベニア、ウクライナ

### その他のラテンアメリカ {#rest-of-latin-america}

ボリビア、コスタリカ、ドミニカ共和国、エクアドル、エルサルバドル、グアテマラ、ハイチ、ホンジュラス、ジャマイカ、ニカラグア、パナマ、パラグアイ、プエルトリコ、ウルグアイ、ベネズエラ

### その他の中東 {#rest-of-middle-east}

バーレーン、イラク、ヨルダン、クウェート、レバノン、オマーン、イエメン

### その他の西ヨーロッパ {#rest-of-western-europe}

オーストリア、ベルギー、デンマーク、フィンランド、アイルランド、ノルウェー、ポルトガル、スウェーデン、スイス

{% alert note %}
BrazeのWhatsAppサービスの詳細については、[WhatsAppドキュメント]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp)を参照してください。
{% endalert %}

## エージェントコンソールの詳細 {#agent-console-details}

エージェントコンソールのクレジット比率は、Brazeプラットフォームから実行される1,000回の呼び出し（Invocation）単位で計算されます。Invocationは、エージェントがLLMへの呼び出しを開始した際に記録されます。デフォルトでは、契約にはサブスクリプション期間の各期間ごとにプラットフォームエディションで指定された呼び出し回数の割り当てが含まれています。追加の呼び出しについては、注文書に従って課金されます。

{% alert note %}
エージェントコンソールの詳細については、[Brazeエージェントのドキュメント]({{site.baseurl}}/user_guide/brazeai/agents)を参照してください。
{% endalert %}

## チャネルの追加詳細 {#additional-channel-details}

### LINE {#line}

LINEのクレジット比率は、Brazeプラットフォームから送信されたLINEメッセージの増分単位で計算されます。

{% alert note %}
BrazeでのLINEの使用について詳しくは、[LINEドキュメント]({{site.baseurl}}/user_guide/message_building_by_channel/line)を参照してください。
{% endalert %}

### KakaoTalk {#kakaotalk}

KakaoTalkのクレジット比率は、Brazeプラットフォームから送信されたKakaoTalkメッセージの増分単位で計算されます。

{% alert note %}
BrazeでのKakaoTalkの使用について詳しくは、[KakaoTalkドキュメント]({{site.baseurl}}/kakaotalk)を参照してください。
{% endalert %}

### Content Cards {#content-cards}

Content Cardsのクレジット比率は、1日あたりのユニークインプレッション1,000件の増分単位で計算されます。

Brazeは、顧客がBrazeのガイダンスに従ってユニークインプレッションを記録するようにContent Cardsを設定していない場合、送信されたContent Cardsの数に基づいてクレジットを請求する権利を留保します。Content Cardsの最初の送信から6か月以内に、顧客が以下の条件に該当する場合、これが適用されるものとみなされます。
- 500万（5,000,000）件を超えるContent Cardsを送信し、かつ以下のいずれかに該当する場合
    - インプレッションの記録がゼロ（0）件
    - 送信数と1日あたりのユニークインプレッション数の比率が100（100）を超えている

{% alert note %}
Braze Content Cardsについて詳しくは、[Content Cardsドキュメント]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards)を参照してください。
{% endalert %}

### バナー {#banners}

バナーのクレジット比率は、1日あたりのユニークインプレッション1,000件の増分単位で計算されます。

{% alert note %}
Brazeバナーについて詳しくは、[バナードキュメント]({{site.baseurl}}/developer_guide/banner_cards)を参照してください。
{% endalert %}

### Audience Sync {#audience-sync}

Audience Syncのクレジット比率は、合計ユーザー同期1,000件の増分単位で計算されます。デフォルトでは、契約にはサブスクリプション期間の各期間ごとに500万件のユーザー同期が含まれています。追加のユーザー同期は、注文書に従って請求されます。

{% alert note %}
キャンバスのAudience Syncと利用可能なパートナーについて詳しくは、[キャンバスドキュメント]({{site.baseurl}}/partners/canvas_steps)を参照してください。
{% endalert %}

### メッセージアーカイブ {#message-archiving}

メッセージアーカイブのクレジット比率は、プッシュ、メール、SMS/MMSチャネル全体でアーカイブされたメッセージ1,000件の増分単位で計算されます。

{% alert note %}
メッセージアーカイブについて詳しくは、[メッセージアーカイブドキュメント]({{site.baseurl}}/user_guide/data/export_braze_data/message_archiving#message-archiving)を参照してください。
{% endalert %}

### Webhook {#webhooks}

webhookのクレジット比率は、Brazeプラットフォームから正常に送信されたwebhook 1,000件の増分単位で計算されます。デフォルトでは、契約にはサブスクリプション期間の各期間ごとに10万件のwebhookが含まれています。追加のwebhookは、注文書に従って請求されます。

{% multi_lang_include pricing/webhook_failed_requests_billing.md credit_name='Action Credits' %}

{% alert note %}
Braze webhookについて詳しくは、[webhookドキュメント]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks)を参照してください。
{% endalert %}