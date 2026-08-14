---
nav_title: "オプトインとオプトアウト"
article_title: "オプトインとオプトアウト"
description: "このリファレンス記事では、WhatsAppのさまざまなオプトインおよびオプトアウト方法について説明します。"
page_type: partner
search_tag: Partner
page_order: 5
channel:
  - WhatsApp
---

# オプトインとオプトアウト {#opt-in-and-opt-out}

> WhatsAppのオプトインとオプトアウトの処理は非常に重要です。WhatsAppは[電話番号の品質評価](https://www.facebook.com/business/help/896873687365001)を監視しており、評価が低いとメッセージ送信数の上限が引き下げられる可能性があります。<br><br>高品質な評価を維持する方法の1つは、ユーザーがビジネスをブロックしたり報告したりすることを防ぐことです。これは、[高品質なメッセージング](https://developers.facebook.com/docs/whatsapp/messaging-limits#quality-rating-and-messaging-limits)（ユーザーにとって価値のある内容など）を提供し、メッセージの頻度を管理し、顧客が今後のコミュニケーションの受信をオプトアウトできるようにすることで実現できます。<br><br>WhatsAppの購読ステータスに関するクロスチャネルの概要については、[購読ステータス]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#whatsapp)を参照してください。このページでは、オプトインとオプトアウトの設定方法、および「regex」と「is」修飾子の違いについて説明します。

オプトインは、外部ソースまたはBrazeの方法（SMSやアプリ内メッセージ、ブラウザ内メッセージなど）から取得できます。オプトアウトは、Brazeで設定したキーワードやWhatsAppマーケティングボタンを使用して処理できます。オプトインとオプトアウトの設定に関するガイダンスについては、以下の方法を参照してください。

## オプトイン方法 {#opt-in-methods}
- [Braze外部のオプトイン方法](#external-to-braze-opt-in-methods)
  - [外部で構築したオプトインリスト](#externally-built-opt-in-list)
  - [カスタマーサポートWhatsAppチャネルでのアウトバウンドメッセージ](#outbound-message-in-customer-support-whatsapp-channel)
  - [インバウンドWhatsAppメッセージ](#inbound-whatsapp-message)
- [Brazeを活用したオプトイン方法](#braze-powered-opt-in-methods)

### オプトアウト方法 {#opt-out-methods}
- [一般的なオプトアウトキーワード](#general-opt-out-keywords)
- [マーケティングオプトアウトの選択](#marketing-opt-out-selection)

## Braze WhatsAppチャネルのオプトイン設定 {#set-up-opt-ins-for-your-braze-whatsapp-channel}

WhatsAppのオプトインについては、[WhatsAppの要件](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)に準拠する必要があります。また、Brazeに以下の情報を提供する必要があります。
- すべてのユーザーの`external_id`、[電話番号]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers)、および更新された購読ステータス。これは、[SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/)を使用するか、[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を通じて電話番号と購読ステータスを更新することで実行できます。

WhatsAppの受信メッセージによって、ユーザーがWhatsApp購読グループに自動的に購読されることはありません。[ユーザー更新ステップ](#user-update-step)、[Webhook](#webhook-campaign-to-trigger-a-second-whatsapp-campaign)、またはAPI呼び出しを使用して、購読ステータスを明示的に更新する必要があります。

Metaでは、オプトインのコピーに以下を求めています。

- あなたのビジネスからメッセージを受信することにオプトインしていることを明確に記載すること
- ビジネス名を含めること（「メッセージをお送りします」などの一般的な表現ではなく）
- 適用される現地の法律に準拠すること

{% alert note %}
Brazeは`/users/track`エンドポイントの改善をリリースし、購読ステータスの更新が可能になりました。詳細は[購読グループ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status)をご覧ください。ただし、[`/v2/subscription/status/set`エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2)を使用してオプトインプロトコルをすでに作成している場合は、引き続きそちらを使用できます。
{% endalert %}

### Braze外部のオプトイン方法 {#external-to-braze-opt-in-methods}

アプリまたはWebサイト（アカウント登録、チェックアウトページ、アカウント設定、クレジットカード端末）からBrazeへ。

メールやテキストメッセージのマーケティング同意をすでに取得している場所に、WhatsApp用の追加セクションを含めてください。ユーザーがオプトインした後、`external_id`、[電話番号]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers)、および更新された購読ステータスが必要です。これを行うには、Brazeのインストール方法に応じて、[`/subscription/status/set`エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)を活用するか、[SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/)を使用します。

#### 外部で構築されたオプトインリスト {#externally-built-opt-in-list}

以前WhatsAppを使用していた場合、WhatsAppの要件に従ってオプトイン済みのユーザーリストをすでに構築している可能性があります。その場合は、CSVをアップロードするか、[以下の情報]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)を使用してAPIでBrazeにインポートします。

#### カスタマーサポートWhatsAppチャネルでのアウトバウンドメッセージ {#outbound-message-in-customer-support-whatsapp-channel}

カスタマーサポートチャネルで、解決済みの問題に対するフォローアップとして、マーケティングメッセージの受信にオプトインするかどうかを尋ねる自動メッセージを送信します。ここでの機能は、選択したカスタマーサポートツールの機能の可用性と、ユーザー情報の保存場所に依存します。

1. WhatsApp Businessの電話番号から[メッセージリンク](https://business.facebook.com/business/help/890732351439459?ref=search_new_0)を提供します。
2. 顧客がオプトインを示すために「はい」と返信する[クイック返信アクション]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies)を提供します。
3. カスタムキーワードトリガーを設定します。
4. これらのアイデアのいずれかについて、おそらく以下のパスで完了する必要があります。
	- [`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を呼び出してユーザーを更新または作成する
	- [`/subscription/status/set`エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)を活用するか、[SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/)を使用する

#### WhatsApp受信メッセージ {#inbound-whatsapp-message}

顧客にWhatsApp番号への受信メッセージを送信してもらいます。

新しいチャネルで確認メッセージをユーザーに受信させたいかどうかに応じて、キャンバスまたはキャンペーンとして設定できます。

1. 受信メッセージのアクションベースの配信トリガーを使用してキャンペーンを作成します。
2. Webhookキャンペーンを作成します。Webhookの例については、[購読グループ]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs#step-2-update-the-users-profile)を参照してください。

{% alert tip %}
[WhatsAppマネージャー](https://business.facebook.com/wa/manage/phone-numbers/)の**Phone Number** > **Message Links**から、WhatsAppチャネルに参加するためのURLまたはQRコードを作成できます。<br>![WhatsApp QRコードコンポーザー。]({% image_buster /assets/img/whatsapp/whatsapp115.png %}){: style="max-width:55%;"}
{% endalert %}

### Brazeを活用したオプトイン方法 {#braze-powered-opt-in-methods}

#### SMSメッセージ {#sms-message}

キャンバスで、以下のいずれかの方法を使用して、WhatsAppメッセージの受信にオプトインするかどうかを顧客に尋ねるキャンペーンを設定します。
- 顧客セグメント：米国外の購読済みマーケティンググループ
- カスタムキーワードトリガーの設定

ユーザープロファイルの購読ステータスの更新については、[購読グループ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status)を参照してください。

#### アプリ内メッセージまたはブラウザ内メッセージ {#in-app-or-in-browser-message}

WhatsAppの利用にオプトインするよう顧客に促すアプリ内メッセージまたはブラウザ内ポップアップを作成します。

[HTMLアプリ内メッセージ](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal)と[JavaScriptブリッジ]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge)を使用して、Braze SDKとインターフェイスします。WhatsApp購読グループIDを必ず使用してください。

#### 電話番号キャプチャフォーム {#phone-number-capture-form}

アプリ内メッセージのドラッグ＆ドロップエディターで[電話番号キャプチャフォーム]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/phone_number_capture)テンプレートを使用して、ユーザーの電話番号を収集し、WhatsApp購読グループを拡大します。

## Braze WhatsApp チャネルのオプトアウトを設定する {#set-up-opt-outs-for-your-braze-whatsapp-channel}

### WhatsApp の「お知らせとキャンペーン」トグル {#whatsapp-offers-and-announcements-toggle}

WhatsApp では、アプリの設定に「お知らせとキャンペーン」トグルがあり、ユーザーはマーケティングメッセージをオプトアウトできます。このトグルは Braze の購読グループとは独立して動作します。

- **Braze の購読グループ**は、Braze インテグレーション（API、ユーザー設定センター、またはSDK）を通じて管理され、メッセージングの対象となるユーザーを制御します。
- **WhatsApp のネイティブトグル**は Meta によって制御され、Braze の外部であるプラットフォームレベルで適用されます。

これら2つのレイヤーは、設計上自動的に同期されません。ユーザーが WhatsApp で「お知らせとキャンペーン」トグルをオフにすると、Braze の購読ステータスが「Subscribed」と表示されていても、Meta がプラットフォームレベルでマーケティングメッセージの配信をブロックします。ユーザーの設定は配信時点で尊重されます。

{% alert note %}
Braze は送信が試行され Meta がエラーを返すまでオプトアウトシグナルを受信しないため、Braze の購読数には、メッセージが試行されるまで WhatsApp トグルを通じてオプトアウトしたユーザーが反映されない場合があります。つまり、このフィードバックループが発生するまで、リーチの推定値がわずかに過大になる可能性があります。
{% endalert %}

### 一般的なオプトアウトキーワード {#general-opt-out-keywords}

特定の単語をメッセージとして送信したユーザーが今後のメッセージングをオプトアウトできるキャンペーンまたはキャンバスを設定できます。キャンバスは、オプトアウトが正常に完了したことを確認するフォローアップメッセージを含めることができるため、特に有効です。

#### ステップ1:「受信 WhatsApp メッセージ」をトリガーとするキャンバスを作成する {#step-1-create-a-canvas-with-a-trigger-of-inbound-whatsapp-message}

![WhatsApp 受信メッセージを送信したユーザーがエントリするアクションベースのキャンバスエントリステップ。]({% image_buster /assets/img/whatsapp/whatsapp116.png %}){: style="max-width:85%;"}

キーワードトリガーを選択する際は、「Stop」や「No Message」などの単語を含めてください。この方法を選択する場合は、顧客にオプトアウト用の単語を確実に伝えてください。たとえば、最初のオプトインを受信した後、「これらのメッセージをオプトアウトするには、いつでも「Stop」とメッセージしてください。」のようなフォローアップ応答を含めます。

![メッセージ本文が「STOP」または「NO MESSAGE」の WhatsApp 受信メッセージを送信するメッセージステップ。]({% image_buster /assets/img/whatsapp/whatsapp117.png %}){: style="max-width:85%;"}

#### ステップ2:ユーザーのプロファイルを更新する {#step-2-update-the-users-profile}

[購読グループ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status)に記載されているいずれかの方法を使用して、ユーザーのプロファイルを更新します。

### マーケティングオプトアウトの選択 {#marketing-opt-out-selection}

WhatsApp メッセージテンプレートクリエーターでは、「マーケティングオプトアウト」オプションを含めることができます。このオプションを含める場合は、必ず購読グループの変更を行う後続ステップを持つキャンバスでテンプレートを使用してください。

1. 「マーケティングオプトアウト」クイック返信を含むメッセージテンプレートを作成します。<br>![フッターオプションに「マーケティングオプトアウト」が表示されたメッセージテンプレート]({% image_buster /assets/img/whatsapp/whatsapp121.png %})<br><br>![マーケティングオプトアウトボタンを設定するセクション。]({% image_buster /assets/img/whatsapp/whatsapp122.png %})<br><br>
2. このメッセージテンプレートを使用するキャンバスを作成します。<br><br>
3. 前述の例と同じ手順に従いますが、トリガーテキストは「STOP PROMOTIONS」を使用します。<br><br>
4. [購読グループ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status)に記載されているいずれかの方法を使用して、ユーザーの購読ステータスを更新します。

## オプトインとオプトアウトのワークフローを設定する {#set-up-opt-in-and-opt-out-workflows}

WhatsAppの「START」と「STOP」キーワード応答ワークフローは、以下の2つの方法で設定できます。

- [ユーザー更新ステップ](#user-update-step)
- [2つ目のWhatsAppキャンペーンをトリガーするWebhookキャンペーン](#webhook-campaign-to-trigger-a-second-whatsapp-campaign)

### ユーザー更新ステップ {#user-update-step}

[ユーザー更新ステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)を使用すると、ユーザーが購読グループの電話番号にキーワードを送信した際に、そのユーザーの電話番号をWhatsApp購読グループに追加できます。

ユーザー更新ステップでは、電話番号が購読グループに追加される前にユーザーがキャンバスの次のステップに進むことがないため、競合を回避できます。また、他の方法と比べて設定ステップが少ないため、Brazeでは一般的にこの方法を推奨しています。

1. アクションベースのステップ「**WhatsApp受信メッセージを送信**」を使用してキャンバスを作成します。「**メッセージ本文が**」を選択し、「**次と一致する**」に「START」と入力します。

{% alert important %}
「STOP」メッセージの場合は、オプトアウトを確認するメッセージステップとユーザー更新ステップの順序を逆にしてください。そうしないと、ユーザーが先に購読グループからオプトアウトされ、確認メッセージを受信する資格がなくなります。
{% endalert %}

![メッセージ本文が「START」のWhatsAppメッセージステップ。]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:80%;"}

{: start="2"}
2. キャンバスで「**ユーザー更新を設定**」ステップを作成し、「**アクション**」で「**高度なJSONエディター**」を選択します。<br><br>![アクションが「高度なJSONエディター」のユーザー更新ステップ。]({% image_buster /assets/img/whatsapp/user_update.png %})<br><br>
3. 以下のJSONペイロードを「**ユーザー更新オブジェクト**」に入力し、`XXXXXXXXXXX`を購読グループIDに置き換えます。

{% raw %}
```json
{
    "attributes": [
        {
            "subscription_groups": [
                {
                    "subscription_group_id": "XXXXXXXXXXX",
                    "subscription_state": "subscribed"
                }
            ]
        }
    ]
}
```
{% endraw %}

{: start="4"}
4. 後続のWhatsAppメッセージステップを追加します。<br><br>![キャンバス内のユーザー更新ステップ。]({% image_buster /assets/img/whatsapp/message_step.png %}){: style="max-width:25%;"}

#### 考慮事項 {#considerations}

Brazeは[ユーザー更新ステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)のリクエストをバッチ処理するため、更新の完了速度にばらつきが生じる場合があります。購読更新後すぐに確認メッセージを送信する必要がある時間的に重要なオプトインフローでは、ユーザー更新ステップの代わりに[Webhookメソッド](#webhook-campaign-to-trigger-a-second-whatsapp-campaign)を使用してください。

### 2つ目のWhatsAppキャンペーンをトリガーするWebhookキャンペーン {#webhook-campaign-to-trigger-a-second-whatsapp-campaign}

Webhookキャンペーンを使用すると、ユーザーが購読グループの電話番号にキーワードを送信した際に、そのユーザーの電話番号をWhatsApp購読グループに追加した後、2つ目のキャンペーンへのエントリをトリガーできます。

{% alert important %}
STOPメッセージにこの方法を使用する必要はありません。確認メッセージはユーザーが購読グループから削除される前に送信されるため、他の2つのステップのいずれかを使用できます。
{% endalert %}

1. アクションベースのステップ「**WhatsApp受信メッセージを送信**」を使用してキャンペーンまたはキャンバスを作成します。「**メッセージ本文が**」を選択し、「**次と一致する**」に「START」と入力します。

![メッセージ本文が「START」のWhatsAppメッセージステップ。]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:85%;"}

{: start="2"}
2. キャンペーンまたはキャンバスでWebhookメッセージステップを作成し、「**リクエスト本文**」を「**Raw Text**」に変更します。

![Webhookのメッセージステップ。]({% image_buster /assets/img/whatsapp/webhook_step.png %}){: style="max-width:85%;"}

{: start="3"}
3. 「**Webhook URL**」に顧客の[エンドポイントURL]({{site.baseurl}}/api/basics)を入力し、その後にエンドポイントリンク`campaigns/trigger/send`を続けます。例：`https://dashboard-02.braze.eu/campaigns/trigger/send`。

![「Webhookを作成」セクションのWebhook URLフィールド。]({% image_buster /assets/img/whatsapp/campaigns_webhook_url.png %}){: style="max-width:70%;"}

{: start="4"}
4. Raw Textに以下のJSONペイロードを入力し、`XXXXXXXXXXX`を購読グループIDに置き換えます。2つ目のキャンペーンを作成した後に`campaign_id`を置き換える必要があります。

{% raw %}
```json
{
    "campaign_id": "XXXXXXXXXXX",
    "recipients": [
        {
            "external_user_id": "{{${user_id}}}",
            "attributes": {
                "subscription_groups": [
                    {
                        "subscription_group_id": "XXXXXXXXXXX",
                        "subscription_state": "subscribed"
                    }
                ]
            }
        }
    ]
}
```
{% endraw %}

{: start="5"}
5. WhatsAppキャンペーン（2つ目のキャンペーン）を作成し、トリガーをAPIに設定します。この`campaign_id`を最初のキャンペーンのJSONペイロードにコピーしてください。

#### 考慮事項

- キャンバスAPIトリガーのJSONペイロード内からの属性更新はまだサポートされていないため、WhatsApp応答メッセージ用のWhatsAppキャンペーンのみをトリガーできます（ステップ2のとおり）。
- WhatsAppテンプレートは、応答メッセージとして送信するには承認が必要です。これは、クイック応答では受信メッセージトリガーが同じキャンペーンまたはキャンバス内にある必要があるためです。[ユーザー更新ステップ](#user-update-step)を使用する場合は、Metaの承認なしでクイック応答メッセージを送信できます。

## 「regex」と「is」修飾子の違いについて {#understanding-the-difference-between-regex-and-is-modifiers}

この表では、修飾子の動作を示すために、トリガーワードの例として `STOP` を使用しています。

| 修飾子 | トリガーワード | アクション |
| --- | --- | --- |
| `Is` | `STOP` | 大文字小文字に関係なく、「stop」という単語全体の使用をキャッチします。たとえば、「stop」はキャッチしますが、「please stop」はキャッチしません。 |
| `Matches regex` | `STOP` | 大文字小文字が完全に一致する「STOP」の使用をキャッチします。たとえば、「STOP」や「PLEASE STOP」はキャッチしますが、「stop」はキャッチしません。 |
| `Matches regex` | `(?i)STOP(?-i)` | 大文字小文字に関係なく、「STOP」の使用をキャッチします。たとえば、「stop」、「please stop」、「never stop sending me messages」をキャッチします。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="「regex」と「is」修飾子の違いについて" }