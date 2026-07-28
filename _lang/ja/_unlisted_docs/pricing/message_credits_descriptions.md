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
  - [課金リージョンの内訳](#billing-region-breakdown)
- [エージェントコンソールの詳細](#agent-console-details)
- [その他のチャネルの詳細](#additional-channel-details)
  - [LINE](#line)
  - [KakaoTalk](#kakaotalk)
  - [Content Cards](#content-cards)
  - [バナー](#banners)
  - [Audience Sync](#audience-sync)
  - [メッセージのアーカイブ](#message-archiving)
  - [Webhook](#webhooks)

## メールチャネルの詳細 {#email-channel-details}

メールのクレジット比率は、Brazeプラットフォームから送信されるメール1,000通単位（CPM）で計算されます。

{% alert note %}
メールチャネルの詳細については、[メールドキュメント]({{site.baseurl}}/user_guide/message_building_by_channel/email)を参照してください。
{% endalert %}

## SMS、MMS、RCSチャネルの詳細 {#sms-mms-and-rcs-channel-details}

SMSおよびMMSのクレジット比率は、Brazeプラットフォームから送信されるセグメント単位で計算されます。RCSのクレジット比率は、Brazeプラットフォームから配信されるBasicおよびRich Mediaタイプ、またはSingleおよびRich Mediaタイプの単位で計算されます。受信および送信の両方のタイプが課金対象となります。

{% alert note %}
これらのチャネルにおいて、該当する場合、キャリア料金は別途（後払いで）請求され、アクションクレジットの一部とはみなされません。
{% endalert %}

### SMSセグメント {#sms-segments}

SMS業界では、メッセージをSMSメッセージセグメント単位でカウントします。メッセージセグメントとは、定義された文字数（GSM-7エンコーディングの場合は160文字、UCS-2エンコーディングの場合は67文字）までの文字グループであり、1回のSMS送信で送られます。GSM-7エンコーディングで161文字のSMSを送信した場合、2つのメッセージセグメントが送信されます。複数のメッセージセグメントを送信すると、追加料金が発生します。

### MMSメッセージ {#mms-messages}

MMSの場合、メッセージの上限は5 MBです（マルチメディアアセットとメッセージ本文のサイズを含みます）。安全のため、Brazeではマルチメディアアセットを600 KB以下に抑え、メッセージ本文も含めることを推奨しています。

### RCSタイプ {#rcs-types}

RCSはSMSおよびMMSの次世代版です。SMSのようなダイレクトで高エンゲージメントなチャネルのメリットを備えつつ、リッチコンテンツ（画像、動画、文書）、認証済みおよびブランド付き送信、候補返信やアクションなどのインタラクティブ機能など、現代の消費者が期待するより豊富な機能を提供します。

- RCSの課金は、2つの異なるメッセージタイプに基づいています（米国向けの区分あり）：
    - **Basic RCS：** テキストのみ、最大160文字
    - **Single RCS：** リッチコンテンツを含むメッセージ、または160文字を超えるテキストのみのメッセージ
    - **Rich RCS（米国のみ）：** テキストのみ、限定的なサジェスチョン/ボタン（quickReply、dialPhone、webviewなしのopenURL）を含む場合あり、160 UTF-8バイト単位でセグメント化
    - **Rich Media RCS（米国のみ）：** メディアを含むメッセージ、またはよりリッチなサジェスチョン/ボタン（webview、ロケーション、カレンダーなど）を含むテキスト、1メッセージとしてカウント

{% alert note %}
SMSファミリーの提供内容の詳細については、[SMSおよびMMSドキュメント]({{site.baseurl}}/user_guide/message_building_by_channel/sms)を参照してください。
{% endalert %}

## WhatsAppチャネルの詳細 {#whatsapp-channel-details}

{% multi_lang_include whatsapp/about_credits.md content="h3" %}

## 課金リージョンの内訳 {#billing-region-breakdown}

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
WhatsAppの提供内容の詳細については、[WhatsAppドキュメント]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp)を参照してください。
{% endalert %}

## エージェントコンソールの詳細 {#agent-console-details}

エージェントコンソールのクレジット比率は、Brazeプラットフォームから実行される呼び出し（Invocation）1,000回単位で計算されます。呼び出しは、エージェントがLLMへのコールを開始した際に記録されます。デフォルトでは、契約にはサブスクリプション期間の各期間ごとに、プラットフォームエディションで指定された呼び出し回数の割り当てが含まれています。追加の呼び出しは、注文書に従って課金されます。

{% alert note %}
エージェントコンソールの詳細については、[Brazeエージェントドキュメント]({{site.baseurl}}/user_guide/brazeai/agents)を参照してください。
{% endalert %}

## その他のチャネルの詳細 {#additional-channel-details}

### LINE {#line}

LINEのクレジット比率は、Brazeプラットフォームから送信されるLINEメッセージ単位で計算されます。

{% alert note %}
BrazeでのLINEの使用方法の詳細については、[LINEドキュメント]({{site.baseurl}}/user_guide/message_building_by_channel/line)を参照してください。
{% endalert %}

### KakaoTalk {#kakaotalk}

KakaoTalkのクレジット比率は、Brazeプラットフォームから送信されるKakaoTalkメッセージ単位で計算されます。

{% alert note %}
BrazeでのKakaoTalkの使用方法の詳細については、[KakaoTalkドキュメント]({{site.baseurl}}/kakaotalk)を参照してください。
{% endalert %}

### Content Cards {#content-cards}

Content Cardsのクレジット比率は、1日あたりのユニークインプレッション1,000回単位で計算されます。

Brazeは、顧客がBrazeのガイダンスに従ってユニークインプレッションを記録するようにContent Cardsを設定していない場合、送信されたContent Cardsの数に基づいてクレジットを課金する権利を留保します。これは、Content Cardsの初回送信から6か月以内に、顧客が以下の条件を満たした場合に適用されます：
- Content Cardsを500万通以上送信し、かつ以下のいずれかに該当する場合
    - インプレッションの記録がゼロ（0）
    - 送信数と1日あたりのユニークインプレッション数の比率が100を超える

{% alert note %}
Braze Content Cardsの詳細については、[Content Cardsドキュメント]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards)を参照してください。
{% endalert %}

### バナー {#banners}

バナーのクレジット比率は、1日あたりのユニークインプレッション1,000回単位で計算されます。

{% alert note %}
Brazeバナーの詳細については、[バナードキュメント]({{site.baseurl}}/developer_guide/banner_cards)を参照してください。
{% endalert %}

### Audience Sync {#audience-sync}

Audience Syncのクレジット比率は、合計ユーザー同期1,000回単位で計算されます。デフォルトでは、契約にはサブスクリプション期間の各期間ごとに500万回のユーザー同期が含まれています。追加のユーザー同期は、注文書に従って課金されます。

{% alert note %}
キャンバスのAudience Syncと利用可能なパートナーの詳細については、[キャンバスドキュメント]({{site.baseurl}}/partners/canvas_steps)を参照してください。
{% endalert %}

### メッセージのアーカイブ {#message-archiving}

メッセージのアーカイブのクレジット比率は、プッシュ、メール、SMS/MMSチャネル全体でアーカイブされたメッセージ1,000通単位で計算されます。

{% alert note %}
メッセージのアーカイブの詳細については、[メッセージアーカイブドキュメント]({{site.baseurl}}/user_guide/data/export_braze_data/message_archiving#message-archiving)を参照してください。
{% endalert %}

### Webhook {#webhooks}

Webhookのクレジット比率は、Brazeプラットフォームから送信されるwebhook 1,000回単位で計算されます。デフォルトでは、契約にはサブスクリプション期間の各期間ごとに10万回のwebhookが含まれています。追加のwebhookは、注文書に従って課金されます。

{% alert note %}
Braze Webhookの詳細については、[webhookドキュメント]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks)を参照してください。
{% endalert %}