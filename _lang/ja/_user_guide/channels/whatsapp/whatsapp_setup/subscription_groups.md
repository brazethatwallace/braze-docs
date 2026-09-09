---
nav_title: "サブスクリプショングループ"
article_title: "サブスクリプショングループ"
page_order: 4
description: "この記事では、WhatsApp購読グループ、提供される購読状態、および購読グループの設定方法について説明します。"
page_type: reference
alias: /whatsapp_subscription_groups/
channel:
  - WhatsApp


---

# WhatsApp購読グループ {#whatsapp-subscription-groups}

> WhatsApp購読グループは、**テクノロジーパートナーポータル**を通じてWhatsAppをアプリと統合する際に作成されます。購読グループのクロスチャネルの概要については、[購読グループ]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups)を参照してください。

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

## WhatsApp購読状態 {#whatsapp-subscription-states}
{: #whatsapp-subscription-states}

WhatsApp購読状態の定義とMetaのオプトイン要件との関連については、[購読ステータス]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#whatsapp)を参照してください。

### ユーザーのWhatsApp購読グループの設定 {#setting-users-whatsapp-subscription-groups}

- **REST API:** [`/subscription/status/set`エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)を使用して、Braze REST APIでユーザープロファイルをプログラムで設定できます。
- **Web SDK:** `addToSubscriptionGroup`メソッドを使用して、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html)、[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:))、または[Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)でメール、SMS、またはWhatsApp購読グループにユーザーを追加できます。
- **ユーザーインポート**: **ユーザーをインポート**を使用して、メールまたはSMS購読グループにユーザーを追加できます。購読グループのステータスを更新する場合、CSVに`subscription_group_id`と`subscription_state`の2つの列が必要です。詳細については、[ユーザーインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)を参照してください。

### ユーザーのWhatsApp購読グループの確認 {#checking-a-users-whatsapp-subscription-group}

- **ユーザープロファイル:** Brazeダッシュボードの**オーディエンス** > **ユーザー検索**から、個々のユーザープロファイルにアクセスできます。ここでは、メールアドレス、電話番号、または外部ユーザーIDでユーザープロファイルを検索できます。ユーザープロファイル内の**エンゲージメント**タブで、ユーザーのWhatsApp購読グループとそのステータスを確認できます。

- **REST API:** [ユーザーの購読グループ一覧エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups)または[ユーザーの購読グループステータス一覧エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status)を使用して、Braze REST APIで個々のユーザープロファイルの購読グループを確認できます。

## 購読グループのアーカイブ {#archive-subscription-groups}

WhatsApp購読グループの使用を停止する必要がある場合は、アーカイブして非アクティブとしてマークできます。

購読グループをアーカイブすると非アクティブとしてマークされますが、ワークスペースからは削除されません。WhatsAppの電話番号または購読グループを完全に削除する必要がある場合は、まず購読グループマネージャーで購読グループをアーカイブしてから、Brazeサポートに削除をリクエストする必要があります。

購読グループをアーカイブするには：

1. **オーディエンス** > **購読グループ管理**に移動します。
2. アーカイブするWhatsApp購読グループを見つけます。
3. 購読グループのステータスにカーソルを合わせ、<i class="fa-solid fa-box-archive" aria-label="アーカイブ"></i> **アーカイブ**を選択します。

## WhatsAppのオプトインおよびオプトアウトプロセス {#whatsapp-opt-in-and-opt-out-process}

WhatsAppの購読ステータス、オプトイン要件、オプトアウトの動作の概要については、[購読ステータス]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#whatsapp)を参照してください。

現在、ユーザーは[SMS](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal)、Webサイト、WhatsAppスレッド、電話、または対面など、さまざまな方法でWhatsAppメッセージングを購読し、[オプトインおよびオプトアウト]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs)できます。オプトインは必須である点にご注意ください。

オプトインキーワードは現在WhatsAppチャネルではサポートされていないため、ユーザーリストの管理はお客様ご自身で行う必要があります。WhatsAppはオプトインとレート制限に対して遡及的なアプローチを取っており、ユーザーが報告やブロックを始めると、レート制限が引き下げられます。

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