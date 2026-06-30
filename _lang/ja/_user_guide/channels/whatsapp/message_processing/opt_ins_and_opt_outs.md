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

> WhatsAppのオプトインとオプトアウトの処理は非常に重要です。WhatsAppは[電話番号の品質評価](https://www.facebook.com/business/help/896873687365001)を監視しており、評価が低いとメッセージ送信数の上限が引き下げられる可能性があります。<br><br>高品質な評価を維持する方法の1つは、ユーザーがビジネスをブロックしたり報告したりすることを防ぐことです。これは、[高品質なメッセージング](https://developers.facebook.com/docs/whatsapp/messaging-limits#quality-rating-and-messaging-limits)（ユーザーにとって価値のある内容など）を提供し、メッセージの頻度を管理し、顧客が今後のコミュニケーションの受信をオプトアウトできるようにすることで実現できます。<br><br>このページでは、オプトインとオプトアウトの設定方法、および「regex」と「is」修飾子の違いについて説明します。

オプトインは、外部ソースまたはBrazeの方法（SMSやアプリ内メッセージ、ブラウザ内メッセージなど）から取得できます。オプトアウトは、Brazeで設定したキーワードやWhatsAppマーケティングボタンを使用して処理できます。オプトインとオプトアウトの設定に関するガイダンスについては、以下の方法を参照してください。

## オプトイン方法 {#opt-in-methods}
- [Braze外部のオプトイン方法](#external-to-braze-opt-in-methods)
  - [外部で構築されたオプトインリスト](#externally-built-opt-in-list)
  - [カスタマーサポートWhatsAppチャネルでのアウトバウンドメッセージ](#outbound-message-in-customer-support-whatsapp-channel)
  - [インバウンドWhatsAppメッセージ](#inbound-whatsapp-message)
- [Brazeを活用したオプトイン方法](#braze-powered-opt-in-methods)

### オプトアウト方法 {#opt-out-methods}
- [一般的なオプトアウトキーワード](#general-opt-out-keywords)
- [マーケティングオプトアウトの選択](#marketing-opt-out-selection)

## BrazeのWhatsAppチャネルのオプトインを設定する {#set-up-opt-ins-for-your-braze-whatsapp-channel}

WhatsAppのオプトインについては、[WhatsAppの要件](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)に準拠する必要があります。また、Brazeに以下の情報を提供する必要があります。
- すべてのユーザーの`external_id`、[電話番号]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers)、および更新されたサブスクリプションステータス。これは、[SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/)を使用するか、[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を通じて電話番号とサブスクリプションステータスを更新することで実行できます。

{% alert note %}
Brazeは`/users/track`エンドポイントの改善をリリースし、サブスクリプションステータスの更新が可能になりました。詳細は[購読グループ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status)で確認できます。ただし、[`/v2/subscription/status/set`エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2)を使用してオプトインプロトコルをすでに作成している場合は、引き続きそちらを使用できます。
{% endalert %}

### Braze外部のオプトイン方法 {#external-to-braze-opt-in-methods}

アプリまたはWebサイト（アカウント登録、チェックアウトページ、アカウント設定、クレジットカード端末）からBrazeへ。

メールやテキストメッセージのマーケティング同意をすでに取得している場合は、WhatsApp用の追加セクションを含めてください。ユーザーがオプトインした後、`external_id`、[電話番号]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers)、および更新されたサブスクリプションステータスが必要です。これを行うには、Brazeのインストール方法に応じて、[`/subscription/status/set`エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)を活用するか、[SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/)を使用します。

#### 外部で構築されたオプトインリスト {#externally-built-opt-in-list}

以前WhatsAppを使用していた場合、WhatsAppの要件に従ってオプトイン済みのユーザーリストをすでに構築している可能性があります。その場合は、CSVをアップロードするか、[以下の情報]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#csv)を使用してAPIでBrazeにインポートしてください。

#### カスタマーサポートWhatsAppチャネルでのアウトバウンドメッセージ {#outbound-message-in-customer-support-whatsapp-channel}

カスタマーサポートチャネルで、解決済みの問題に対するフォローアップとして、マーケティングメッセージのオプトインを希望するかどうかを尋ねる自動メッセージを送信します。ここでの機能は、選択したカスタマーサポートツールの機能の可用性と、ユーザー情報の保存場所に依存します。

1. WhatsApp Businessの電話番号から[メッセージリンク](https://business.facebook.com/business/help/890732351439459?ref=search_new_0)を提供します。
2. 顧客が「はい」と返信してオプトインを示す[クイック返信アクション]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies)を提供します。
3. カスタムキーワードトリガーを設定します。
4. これらのアイデアのいずれかについて、おそらく以下の方法でパスを完了する必要があります。
	- [`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を呼び出してユーザーを更新または作成する
	- [`/subscription/status/set`エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)を活用するか、[SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/)を使用する

#### インバウンドWhatsAppメッセージ {#inbound-whatsapp-message}

顧客にWhatsApp番号へインバウンドメッセージを送信してもらいます。

これは、新しいチャネルで確認メッセージをユーザーに受信させたいかどうかに応じて、キャンバスまたはキャンペーンとして設定できます。

1. インバウンドメッセージのアクションベースの配信トリガーを持つキャンペーンを作成します。
2. Webhook キャンペーンを作成します。Webhookの例については、[購読グループ]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs#update-subscription-status)を参照してください。

{% alert tip %}
[WhatsAppマネージャー](https://business.facebook.com/wa/manage/phone-numbers/)の**Phone Number** > **Message Links**から、WhatsAppチャネルに参加するためのURLまたはQRコードを作成できます。<br>![WhatsApp QRコードコンポーザー。]({% image_buster /assets/img/whatsapp/whatsapp115.png %}){: style="max-width:55%;"}
{% endalert %}

### Brazeを活用したオプトイン方法 {#braze-powered-opt-in-methods}

#### SMSメッセージ {#sms-message}

キャンバスで、以下のいずれかの方法を使用して、WhatsAppメッセージの受信をオプトインするかどうかを顧客に尋ねるキャンペーンを設定します。
- 顧客セグメント：米国外の購読済みマーケティンググループ
- カスタムキーワードトリガーの設定

ユーザープロファイルのサブスクリプションステータスの更新については、[購読グループ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status)を参照してください。

#### アプリ内またはブラウザ内メッセージ {#in-app-or-in-browser-message}

WhatsAppの利用をオプトインするよう顧客に促すアプリ内メッセージまたはブラウザ内ポップアップを作成します。

Braze SDKとインターフェイスするために、[JavaScript「ブリッジ」]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge)を使用した[HTMLアプリ内メッセージ](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal)を使用します。WhatsAppサブスクリプショングループIDを必ず使用してください。

#### 電話番号キャプチャフォーム {#phone-number-capture-form}

アプリ内メッセージのドラッグ＆ドロップエディターで[電話番号キャプチャフォーム]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/phone_number_capture)テンプレートを使用して、ユーザーの電話番号を収集し、WhatsAppサブスクリプショングループを拡大します。

## BrazeのWhatsAppチャネルのオプトアウトを設定する {#set-up-opt-outs-for-your-braze-whatsapp-channel}

### WhatsApp「お知らせとキャンペーン」トグル {#whatsapp-offers-and-announcements-toggle}

WhatsAppは、アプリ設定内に「お知らせとキャンペーン」トグルを提供しており、ユーザーがマーケティングメッセージをオプトアウトできるようにしています。このトグルはBrazeのサブスクリプショングループとは独立して動作します。

- **Brazeのサブスクリプショングループ**は、Brazeの統合（API、ユーザー設定センター、またはSDK）を通じて管理され、メッセージングのターゲットとなるユーザーを制御します。
- **WhatsAppのネイティブトグル**は、Metaによって制御され、Brazeの外部でプラットフォームレベルで適用されます。

これら2つのレイヤーは設計上、自動的に同期されません。ユーザーがWhatsAppで「お知らせとキャンペーン」トグルをオフにすると、Metaはプラットフォームレベルでマーケティングメッセージの配信をブロックします。これは、ユーザーのBrazeサブスクリプションステータスが「購読中」と表示されている場合でも同様です。ユーザーの設定は配信時点で尊重されます。

{% alert note %}
Brazeは送信が試行されてMetaがエラーを返すまでオプトアウトシグナルを受信しないため、Brazeのサブスクリプション数には、メッセージが試行されるまでWhatsAppトグルでオプトアウトしたユーザーが反映されない場合があります。これは、そのフィードバックループが発生するまで、リーチの推定値がわずかに過大になる可能性があることを意味します。
{% endalert %}

### 一般的なオプトアウトキーワード {#general-opt-out-keywords}

特定の単語をメッセージとして送信したユーザーが今後のメッセージングをオプトアウトできるキャンペーンまたはキャンバスを設定できます。キャンバスは、オプトアウトの成功を確認するフォローアップメッセージを含めることができるため、特に有益です。

#### ステップ1：「インバウンドWhatsAppメッセージ」トリガーでキャンバスを作成する {#step-1-create-a-canvas-with-a-trigger-of-inbound-whatsapp-message}

![WhatsAppインバウンドメッセージを送信したユーザーがエントリするアクションベースのキャンバスエントリステップ。]({% image_buster /assets/img/whatsapp/whatsapp116.png %}){: style="max-width:85%;"}

キーワードトリガーを選択する際は、「Stop」や「No Message」などの単語を含めてください。この方法を選択する場合は、顧客がオプトアウトの単語を知っていることを確認してください。例えば、最初のオプトインを受信した後、「これらのメッセージをオプトアウトするには、いつでも「Stop」とメッセージしてください。」のようなフォローアップ応答を含めます。

![メッセージ本文が「STOP」または「NO MESSAGE」であるWhatsAppインバウンドメッセージを送信するメッセージステップ。]({% image_buster /assets/img/whatsapp/whatsapp117.png %}){: style="max-width:85%;"}

#### ステップ2：ユーザーのプロファイルを更新する {#step-2-update-the-users-profile}

[購読グループ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status)で説明されている方法のいずれかを使用して、ユーザーのプロファイルを更新します。

### マーケティングオプトアウトの選択 {#marketing-opt-out-selection}

WhatsAppメッセージテンプレートクリエーター内で、「マーケティングオプトアウト」オプションを含めることができます。これを含める場合は、テンプレートがサブスクリプショングループの変更のための後続ステップを持つキャンバスで使用されていることを確認してください。

1. 「マーケティングオプトアウト」クイック返信を含むメッセージテンプレートを作成します。<br>![「マーケティングオプトアウト」のフッターオプションを持つメッセージテンプレート。]({% image_buster /assets/img/whatsapp/whatsapp121.png %})<br><br>![マーケティングオプトアウトボタンを設定するセクション。]({% image_buster /assets/img/whatsapp/whatsapp122.png %})<br><br>
2. このメッセージテンプレートを使用するキャンバスを作成します。<br><br>
3. 前述の例と同じ手順に従いますが、トリガーテキストは「STOP PROMOTIONS」を使用します。<br><br>
4. [購読グループ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status)で説明されている方法のいずれかを使用して、ユーザーのサブスクリプションステータスを更新します。

## オプトインとオプトアウトのワークフローを設定する {#set-up-opt-in-and-opt-out-workflows}

以下の2つの方法で、WhatsAppの「START」と「STOP」キーワード応答ワークフローを設定できます。

- [ユーザーの更新ステップ](#user-update-step)
- [2番目のWhatsApp キャンペーンをトリガーするwebhook キャンペーン](#webhook-campaign-to-trigger-a-second-whatsapp-campaign)

### ユーザーの更新ステップ {#user-update-step}

[ユーザーの更新ステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)は、ユーザーがサブスクリプショングループの電話番号にキーワードを送信した際に、ユーザーの電話番号をWhatsAppサブスクリプショングループに追加できます。

ユーザーの更新ステップは、ユーザーの電話番号がサブスクリプショングループに追加される前にキャンバスの次のステップに進むことがないため、競合を回避できます。また、他の方法よりも設定手順が少ないため、Brazeでは一般的にこの方法を推奨しています。

1. アクションベースのステップ**Send a WhatsApp Inbound Message**でキャンバスを作成します。**Where the message body**を選択し、**Is**に「START」と入力します。

{% alert important %}
「STOP」メッセージの場合は、オプトアウトを確認するメッセージステップとユーザーの更新ステップの順序を逆にしてください。そうしないと、ユーザーが最初にサブスクリプショングループからオプトアウトされ、確認メッセージを受信する資格がなくなります。
{% endalert %}

![メッセージ本文が「START」であるWhatsAppメッセージステップ。]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:80%;"}

{: start="2"}
2. キャンバスで、**Set Up User Update**ステップを作成し、**Action**で**Advanced JSON Editor**を選択します。<br><br>![「Advanced JSON Editor」のアクションを持つユーザーの更新ステップ。]({% image_buster /assets/img/whatsapp/user_update.png %})<br><br>
3. 以下のJSONペイロードで**User Update object**を入力し、`XXXXXXXXXXX`をサブスクリプショングループIDに置き換えます。

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
4. 後続のWhatsAppメッセージステップを追加します。<br><br>![キャンバス内のユーザーの更新ステップ。]({% image_buster /assets/img/whatsapp/message_step.png %}){: style="max-width:25%;"}

#### 考慮事項 {#considerations}

Brazeは[ユーザーの更新ステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)のリクエストをバッチ処理するため、更新の完了速度は変動する可能性があります。

### 2番目のWhatsApp キャンペーンをトリガーするwebhook キャンペーン {#webhook-campaign-to-trigger-a-second-whatsapp-campaign}

Webhook キャンペーンは、ユーザーがサブスクリプショングループの電話番号にキーワードを送信した際に、ユーザーの電話番号をWhatsAppサブスクリプショングループに追加した後、2番目のキャンペーンへのエントリをトリガーできます。

{% alert important %}
STOPメッセージにはこの方法を使用する必要はありません。確認メッセージはユーザーがサブスクリプショングループから削除される前に送信されるため、他の2つのステップのいずれかを使用できます。
{% endalert %}

1. アクションベースのステップ**Send a WhatsApp Inbound Message**でキャンペーンまたはキャンバスを作成します。**Where the message body**を選択し、**Is**に「START」と入力します。

![メッセージ本文が「START」であるWhatsAppメッセージステップ。]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:85%;"}

{: start="2"}
2. キャンペーンまたはキャンバスで、Webhookメッセージステップを作成し、**Request Body**を**Raw Text**に変更します。

![Webhookのメッセージステップ。]({% image_buster /assets/img/whatsapp/webhook_step.png %}){: style="max-width:85%;"}

{: start="3"}
3. **Webhook URL**に顧客の[エンドポイントURL]({{site.baseurl}}/api/basics)を入力し、その後にエンドポイントリンク`campaigns/trigger/send`を続けます。例えば、`https://dashboard-02.braze.eu/campaigns/trigger/send`のようになります。

![「Compose Webhook」セクションの下にあるWebhook URLフィールド。]({% image_buster /assets/img/whatsapp/campaigns_webhook_url.png %}){: style="max-width:70%;"}

{: start="4"}
4. Raw Textに以下のJSONペイロードを入力し、`XXXXXXXXXXX`をサブスクリプショングループIDに置き換えます。2番目のキャンペーンを作成した後に`campaign_id`を置き換える必要があります。

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
5. WhatsApp キャンペーン（2番目のキャンペーン）を作成し、トリガーをAPIに設定します。この`campaign_id`を最初のキャンペーンのJSONペイロードにコピーしてください。

#### 考慮事項

- キャンバス APIトリガーのJSONペイロード内からの属性更新はまだサポートされていないため、WhatsApp応答メッセージ用のWhatsApp キャンペーンのみをトリガーできます（ステップ2のように）。
- WhatsAppテンプレートは、応答メッセージとして送信するために承認されている必要があります。これは、クイック応答ではインバウンドメッセージトリガーが同じキャンペーンまたはキャンバス内にある必要があるためです。[ユーザーの更新ステップ](#user-update-step)を使用する場合は、Metaの承認なしにクイック応答メッセージを送信できます。

## 「regex」と「is」修飾子の違いを理解する {#understanding-the-difference-between-regex-and-is-modifiers}

この表では、修飾子の動作を示すために、トリガーワードの例として`STOP`を使用しています。

| 修飾子 | トリガーワード | アクション |
| --- | --- | --- |
| `Is` | `STOP` | 大文字小文字に関係なく、「stop」の完全一致の単語をキャッチします。例えば、「stop」はキャッチしますが、「please stop」はキャッチしません。 |
| `Matches regex` | `STOP` | 正確にその大文字小文字での「STOP」の使用をキャッチします。例えば、「STOP」と「PLEASE STOP」はキャッチしますが、「stop」はキャッチしません。 |
| `Matches regex` | `(?i)STOP(?-i)` | 大文字小文字に関係なく、「STOP」の使用をキャッチします。例えば、「stop」、「please stop」、「never stop sending me messages」をキャッチします。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" aria-label="「regex」と「is」修飾子の違いを理解する" }