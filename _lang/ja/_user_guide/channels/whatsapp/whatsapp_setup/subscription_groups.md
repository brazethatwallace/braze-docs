---
nav_title: "サブスクリプショングループ"
article_title: "サブスクリプショングループ"
page_order: 4
description: "この記事では、WhatsAppサブスクリプショングループ、提供されるサブスクリプション状態、およびサブスクリプショングループの設定方法について説明します。"
page_type: reference
alias: /whatsapp_subscription_groups/
channel:
  - WhatsApp

---

# WhatsAppサブスクリプショングループ {#whatsapp-subscription-groups}

> WhatsAppサブスクリプショングループは、**テクノロジーパートナーポータル**を通じてWhatsAppをアプリと統合する際に作成されます。

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

## WhatsAppサブスクリプション状態 {#whatsapp-subscription-states}

WhatsAppユーザーには、`subscribed`と`unsubscribed`の2つのサブスクリプション状態があります。

| 状態 | 定義 |
| --- | --- |
| 購読中 | ユーザーが特定の会社からWhatsAppメッセージを受信することを明示的に確認しています。ユーザーは、BrazeサブスクリプションAPIを通じてサブスクリプション状態を更新するか、WhatsAppのガイドラインに従ってオプトイン戦略を展開することで購読できます。 |
| 購読解除 | ユーザーがオプトインの同意を明示的に与えていないか、オプトインステータスが明示的に削除されています。<br><br>WhatsAppサブスクリプショングループから購読解除されたユーザーは、そのサブスクリプショングループに属する送信電話番号からのWhatsAppメッセージを受信しなくなります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="WhatsAppサブスクリプション状態" }

### ユーザーのWhatsAppサブスクリプショングループの設定 {#setting-users-whatsapp-subscription-groups}

- **REST API：** ユーザープロファイルは、Braze REST APIを使用して[`/subscription/status/set`エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)でプログラム的に設定できます。
- **Web SDK：** ユーザーは、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html)、[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:))、または[Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)の`addToSubscriptionGroup`メソッドを使用して、メール、SMS、またはWhatsAppサブスクリプショングループに追加できます。
- **ユーザーインポート：** ユーザーは、**ユーザーをインポートする**を通じてメールまたはSMSサブスクリプショングループに追加できます。サブスクリプショングループのステータスを更新する場合、CSVに`subscription_group_id`と`subscription_state`の2つの列が必要です。詳細については、[ユーザーインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)を参照してください。

### ユーザーのWhatsAppサブスクリプショングループの確認 {#checking-a-users-whatsapp-subscription-group}

- **ユーザープロファイル：** 個々のユーザープロファイルは、Brazeダッシュボードから**オーディエンス** > **ユーザーを検索**でアクセスできます。ここでは、メールアドレス、電話番号、または外部ユーザーIDでユーザープロファイルを検索できます。ユーザープロファイル内の**エンゲージメント**タブで、ユーザーのWhatsAppサブスクリプショングループとそのステータスを確認できます。

- **REST API：** 個々のユーザープロファイルのサブスクリプショングループは、Braze REST APIを使用して[ユーザーの購読グループを一覧表示するエンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups)または[ユーザーの購読グループステータスを一覧表示するエンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status)で確認できます。

## サブスクリプショングループのアーカイブ {#archive-subscription-groups}

WhatsAppサブスクリプショングループの使用を停止する必要がある場合、アーカイブして非アクティブとしてマークできます。

サブスクリプショングループをアーカイブすると、非アクティブとしてマークされますが、ワークスペースからは削除されません。WhatsApp電話番号またはサブスクリプショングループを完全に削除する必要がある場合は、Brazeサポートに削除をリクエストする前に、まず購読グループ管理でサブスクリプショングループをアーカイブする必要があります。

サブスクリプショングループをアーカイブするには：

1. **オーディエンス** > **購読グループ管理**に移動します。
2. アーカイブするWhatsAppサブスクリプショングループを見つけます。
3. サブスクリプショングループのステータスにカーソルを合わせ、<i class="fa-solid fa-box-archive"></i> **アーカイブ**を選択します。

## WhatsAppのオプトインとオプトアウトのプロセス {#whatsapp-opt-in-and-opt-out-process}

現在、ユーザーは[SMS](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal)、Webサイト、WhatsAppスレッド、電話、対面など、さまざまな方法でWhatsAppメッセージングの購読や[オプトインとオプトアウト]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs)を行うことができます。オプトインは必須であることにご注意ください。

現在、WhatsAppチャネルではオプトインキーワードはサポートされていないため、ユーザーリストの管理はお客様自身で行う必要があります。WhatsAppはオプトインとレート制限に対して遡及的なアプローチを取っており、ユーザーが報告やブロックを開始すると、レート制限が引き下げられます。

## WhatsAppキャンバスへのユーザーのサブスクリプションステータスの更新 {#update-subscription-status}

使用するオプトインおよびオプトアウトの方法に関係なく、以下のいずれかの更新方法でユーザープロファイルのサブスクリプションステータスを更新できます。

- 以下の例のように、REST APIを通じてサブスクリプションステータスを更新する[Braze間Webhook]({{site.baseurl}}/user_guide/channels/webhooks/use_case_create_a_braze_to_braze_webhook#considerations)を作成します。

![POSTメソッドを使用したメッセージを含むWebhookコンポーザー。]({% image_buster /assets/img/whatsapp/whatsapp118.png %}){: style="max-width:90%;"}

競合を避けるため、Webhook後のフォローアップメッセージングは、最初のキャンバスの結果（ユーザーがキャンバスバリエーションに入り、WhatsAppサブスクリプショングループに属しているなど）によってトリガーされる2番目のキャンバスに含める必要があります。

- 高度なJSONエディターを使用して、以下のテンプレートでユーザープロファイルを更新します。

	```json
	{
	  "attributes": [
	  {
	  	"subscription_groups": [{
	  	  "subscription_group_id": "subscription_group_identifier_1",
	  	  "subscription_state": "unsubscribed"
	  	   },
	  	   {
	  	     "subscription_group_id": "subscription_group_identifier_2",
	  	     "subscription_state": "subscribed"
	  	     },
	  	     {
	  	       "subscription_group_id": "subscription_group_identifier_3",
	  	       "subscription_state": "subscribed"
	  	    }
	  	  ]
	  	}
	  ]
	}
	```

![高度なJSONエディターステップを含むユーザー更新ステップ。]({% image_buster /assets/img/whatsapp/whatsapp_json_editor.png %}){: style="max-width:90%;"}

{% alert note %}
ユーザーのサブスクリプションステータスの更新には最大60秒かかる場合があります。
{% endalert %}