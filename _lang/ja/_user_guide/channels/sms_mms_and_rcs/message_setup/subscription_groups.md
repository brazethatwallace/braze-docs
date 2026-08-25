---
nav_title: "サブスクリプショングループ"
article_title: SMSおよびRCSサブスクリプショングループ
page_order: 4
description: "このリファレンス記事では、SMS、MMS、RCSチャネルのサブスクリプショングループ、サブスクリプション状態、およびサブスクリプショングループの設定プロセスについて説明します。"
page_type: reference
alias: /sms_rcs_subscription_groups/
channel:
  - SMS
  - MMS
  - RCS

---

# SMS、MMS、RCSサブスクリプショングループ {#sms-mms-and-rcs-subscription-groups}

> サブスクリプショングループは、Brazeを通じてSMS、MMS、RCSメッセージを送信するための基盤です。サブスクリプショングループは、特定のメッセージング目的（たとえばトランザクションとプロモーション）に使用される[送信エンティティ]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup)（RCS認証済み送信者、SMSショートコード、SMSロングコード、SMS英数字送信者IDなど）の集合です。サブスクリプショングループのクロスチャネルの概要については、[サブスクリプショングループ]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups)を参照してください。

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

## 購読グループの状態 {#subscription-group-states}

SMSおよびRCSユーザーには、`subscribed`と`unsubscribed`の2つの購読状態があります。ユーザーの購読状態は購読グループレベルに存在し、購読グループ間で共有されません。つまり、ユーザーはトランザクション購読グループでは`subscribed`でありながら、プロモーション購読グループでは`unsubscribed`である可能性があります。ブランドにとって、この状態の分離により、ユーザーに関連性のあるSMSおよびRCSメッセージを引き続き送信できます。

| 状態 | 定義 |
| --------- | ---------- |
| 購読中 | ユーザーは特定の購読グループからSMSおよびRCSを受信するよう購読しています。ユーザーは、BrazeサブスクリプションAPIを通じて購読状態を更新するか、オプトインキーワードの応答をテキスト送信することで購読できます。SMSまたはRCS、あるいはその両方を受信するには、ユーザーがSMSまたはRCS購読グループに購読している必要があります。[ダブルオプトイン]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in)が有効な場合、ユーザーは購読ステータスが`Subscribed`に更新される前にオプトインの意思を確認する必要があります。 |
| 購読解除 | ユーザーがSMSおよびRCS購読グループと、その購読グループ内の送信電話番号からのメッセージングを明示的にオプトアウトしました。オプトアウトキーワードの応答をテキスト送信するか、[Brazeサブスクリプション API]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)を通じて購読解除できます。SMSおよびRCS購読グループから購読解除されたユーザーは、その購読グループに属する送信電話番号からのSMSまたはRCSを受信しなくなります。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="購読グループの状態" }

### ユーザーの状態を設定する {#set-a-users-state}

ユーザープロファイルで電話番号が更新されると、新しい電話番号はユーザーの購読グループステータスを引き継ぎます。電話番号がBrazeにすでに存在する番号に更新された場合、その既存の電話番号の購読ステータスが引き継がれます。

たとえば、ユーザーAが複数の購読グループに購読中の電話番号を持っていて、その電話番号がユーザーBに追加された場合、ユーザーBは同じ購読グループに購読されます。ユーザーが既存の購読を引き継ぐのを防ぐには、ユーザーが番号を変更するたびにBraze REST APIを通じて古い番号の購読グループをリセットできます。複数のユーザーがこの電話番号を共有している場合、全員が購読解除されます。

ユーザーの購読グループの状態を設定するには、以下のいずれかの方法を使用します。

- **REST API:** [`/subscription/status/set`エンドポイント]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)を使用して、Braze REST APIでプログラム的にユーザープロファイルを設定します。各リクエストには1〜25の購読グループを含めることができます。
- **SDK統合:** `addToSubscriptionGroup`および`removeFromSubscriptionGroup`を使用して、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html)、[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:))、または[Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)でメールまたはSMSおよびRCS購読グループにユーザーを追加または削除できます。SDKメソッドは、キーワードやREST APIで処理される規制上のオプトイン/オプトアウトフローを置き換えるものではありません。
- **電話番号キャプチャIAMフォーム:** アプリ内メッセージのドラッグ＆ドロップエディターの電話番号キャプチャテンプレートを使用して、ユーザーの電話番号を収集できます。
- **ユーザーのオプトイン/オプトアウト時に自動処理:** ユーザーがデフォルトのオプトインまたはオプトアウト[キーワード]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout)をテキスト送信すると、Brazeがユーザーの購読状態を自動的に設定・更新します。
- **ユーザーインポート:** **Import Users**を使用して、メールまたはSMSおよびRCS購読グループにユーザーを追加できます。購読グループのステータスを更新する場合、CSVに`subscription_group_id`と`subscription_state`の2つの列が必要です。詳細については、[ユーザーインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)を参照してください。
- **Brazeダッシュボード:** サイドバーから**User Search**を選択し、ユーザーのプロファイルを開き、**Engagement**タブの**Contact Settings**でSMSまたはRCS購読グループを更新します。
- **Cloud Data Ingestion (CDI):** 同期される行に`subscription_group_id`と`subscription_state`を含めます。[Cloud Data Ingestionテーブル設定]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup)を参照してください。
- **ユーザー更新ステップ:** キャンバスの[ユーザー更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)ステップで購読ステータスを更新します。タイミングに関する注意事項については、[キャンバスでユーザーの状態を更新する](#update-a-users-state-in-a-canvas)を参照してください。

#### キャンバスでユーザーの状態を更新する {#update-a-users-state-in-a-canvas}

キャンバスフローの一部としてユーザーの購読グループステータスを更新する場合、Webhookの代わりに[ユーザー更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)ステップを使用してください。ユーザー更新ステップは、処理が完了するまで待機してからユーザーを次のステップに進めるため、後続のメッセージングステップでは更新された購読ステータスが使用されます。

Webhookを使用して購読グループを更新すると、購読の変更処理が完了する前に、Webhookが送信された時点でユーザーが先に進みます。これにより、フォローアップのSMSステップがユーザーの購読前に実行され、一部のユーザーでメッセージが失敗するという競合が発生する可能性があります。Webhookを使用する必要がある場合は、次のメッセージングステップの前に少なくとも1分の遅延ステップを追加してください。

{% multi_lang_include api/orphaned_subscription_states.md %}

### ユーザーのグループを確認する {#check-a-users-group}

ユーザーの購読グループを確認するには、以下のいずれかの方法を使用します。

- **ユーザープロファイル:** サイドバーから**User Search**を選択して、Brazeダッシュボードから個々のユーザープロファイルにアクセスできます。メールアドレス、電話番号、または外部ユーザーIDでユーザープロファイルを検索できます。ユーザープロファイル内のEngagementタブで、ユーザーのSMSおよびRCS購読グループを表示できます。
- **REST API:** Braze REST APIの[ユーザーの購読グループを一覧表示エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups)または[ユーザーの購読グループステータスを一覧表示エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status)を使用して、個々のユーザープロファイルの購読グループを表示できます。

## 購読グループを使用したメッセージ送信 {#send-messages-with-a-subscription-group}

BrazeでSMSまたはRCSキャンペーンを送信するには、**SMS/MMS/RCSバリアント**ドロップダウンから購読グループを選択します。選択すると、オーディエンスフィルターがキャンペーンまたはキャンバスに自動的に追加され、選択した購読グループに`subscribed`しているユーザーのみがターゲットオーディエンスに含まれるようになります。

ユーザーがキャンペーンまたはキャンバスからメッセージを受信するには、選択した購読グループに購読している必要があります。それ以外は有効なユーザーへの送信が失敗する場合は、[ユーザーの状態を設定する](#set-a-users-state)のメソッドを使用して、ユーザーが購読していることを確認してください。ダブルオプトインの要件については、[購読グループの状態](#subscription-group-states)を参照してください。

{% alert important %}
国際的な[通信コンプライアンスおよびガイドライン]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)に準拠し、Brazeは選択した購読グループに購読していないユーザーにSMSまたはRCSを送信しません。
{% endalert %}

![購読グループドロップダウンが開かれたSMSコンポーザー。「Messaging Service A for SMS」がユーザーによりハイライトされている。]({% image_buster /assets/img/sms/sms_subgroup_select.png %})

## SMS購読グループのベストプラクティス {#sms-subscription-group-best-practices}

メッセージングの目的ごと（例：トランザクションとマーケティング）、およびワークスペースごとに、個別のSMS購読グループを設計してください。複数の国で運用する場合は、各地域のコンプライアンスルールに対応するために、地域ごとに個別のグループを検討してください。例えば、ブラジルではプロモーション送信の時間帯に関する制限があります。

## 購読グループの有効化 {#enable-subscription-groups}

SMS、MMS、またはRCSの購読グループを有効にするには、以下を参照してください。

{% tabs local %}
{% tab SMS %}
SMSのオンボーディングプロセスにおいて、Brazeのオンボーディングマネージャーがダッシュボードアカウントの購読グループを設定します。必要な購読グループの数を決定し、適切な送信用電話番号を購読グループに追加する作業を一緒に行います。購読グループの設定にかかる時間は、追加する電話番号の種類によって異なります。たとえば、ショートコードの申請は8〜12週間かかることがありますが、ロングコードは1日以内に設定できます。Brazeダッシュボードの設定についてご不明な点がある場合は、Brazeの担当者にお問い合わせください。
{% endtab %}

{% tab MMS %}
MMSメッセージを送信するには、購読グループ内の少なくとも1つの番号がMMS送信に対応している必要があります。これは、購読グループの横にあるタグで示されます。

![購読グループのドロップダウン。「Messaging Service A for SMS」がハイライトされている。エントリの先頭に「MMS」タグが付いている。]({% image_buster /assets/img/sms/mms_sub_group_tag.png %}){: style="max-width:40%"}
{% endtab %}

{% tab RCS %}
RCSメッセージを送信するには、購読グループ内にRCS認証済みの送信者が存在している必要があります。

RCS認証済みの送信者を追加するには、2つの方法があります。
- 既存の購読グループに追加する
- 新しいRCS購読グループを作成する
どちらを選択するかは、関心のあるRCSのユースケースによって大きく異なります。

統合方法に応じて、BrazeはRCS認証済みの送信者を既存のSMS購読グループに追加するか、新しい購読グループを設定します。いずれの場合も、カスタマーサクセスマネージャーがシームレスで効率的なSMSトラフィックのアップグレードをご案内します。
{% endtab %}
{% endtabs %}

## エージェントコンソールで自然言語のオプトアウトを処理する {#handle-natural-language-opt-outs-in-the-agent-console}

包括的な購読管理のために、標準キーワードやカスタムキーワード以外のオプトアウト意思（「テキストを送らないでください」など）をキャプチャできます。AIエージェントを作成することで、感情分析を使用してこれらのリクエストを自動的に識別し、対応できます。

### セットアップ {#setup}

1. [エージェントコンソール]({{site.baseurl}}/user_guide/brazeai/agents)で、「SMS感情分析エージェント」を作成します。

{% alert tip %}
初期エージェント設定のアシストには、[オペレーター]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator)を使用してください。
{% endalert %}

{: start="2"}
2. **Send an SMS inbound message**によってトリガーされるアクションベースのキャンバスを、**Other**キーワードカテゴリ内に作成します。
3. キャンバスに[エージェントステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step)を追加して、オプトアウトの意思を識別します。
4. リクエストを確認するための後続のSMS[メッセージステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)を追加します：「SMSの購読解除をご希望のようですので、購読解除の処理を行います。誤りの場合は、STARTとテキストを送信して再度オプトインしてください。」
5. [ユーザー更新ステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)を追加して、特定のSMS購読グループにおけるユーザーのステータスを「Unsubscribed」に変更します。

{% alert note %}
エージェントコンソールの使用には、メッセージクレジットまたはアクションクレジットを消費します。
{% endalert %}

## SMSトラフィックをRCSに移行する {#migrate-sms-traffic-to-rcs}

SMSとRCSで別々の購読グループがある場合、1ステップのキャンバスを使用してユーザーをSMSからRCSに移行できます。

Brazeでは、最初は少量のユーザーにRCSを送信してテストし、時間をかけてRCS購読グループに移行するユーザーを増やすことを推奨しています。たとえば、SMS購読グループに1,000,000人のユーザーが購読している場合、まずすべてのユーザーを新しい購読グループに移行し、次に50,000～100,000人（5～10%）の小規模なオーディエンスにセグメントして、RCSメッセージをテストするという方法が考えられます。

### ステップ1：キャンバスを作成してエントリスケジュールを設定する {#step-1-create-a-canvas-and-fill-out-the-entry-schedule}

キャンバスを作成し、識別しやすい名前を付けます（「SMS-RCS購読グループユーザー移行」など）。次に、都合の良いタイミングでキャンペーンをスケジュールします。

### ステップ2：オーディエンスを定義する {#step-2-define-your-audience}
{: #step-2-define-your-audience}

以下のいずれかの方法でオーディエンスを定義します。次に、**送信設定**ステップに移動し、**購読中またはオプトイン済みのユーザー**を選択します。

| 方法                          | 説明                                                                                                                                                                                                 |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **セグメントを作成する**         | 購読グループ内のすべてのユーザー、またはセグメンテーションフィルター（ランダムな5～10%など）を使用したサブセットを含むセグメントを作成します。セグメントは各送信前に更新され、現在のユーザー群を反映します。        |
| **キャンペーンまたはキャンバスフィルターを適用する** | キャンペーンまたはキャンバスの**ターゲットオーディエンス**ステップでオーディエンスを絞り込みます。ページを離れることなくターゲティングオプションを調整でき、柔軟に対応できます。                                         |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ2：オーディエンスを定義する" }

### ステップ3：ユーザー更新ステップを設定する {#step-3-configure-a-user-update-step}

キャンバスにユーザー更新ステップを追加します。ステップ内で**Advanced JSON Editor**を開き、以下を入力します（一意のユーザー識別子フィールドには、`braze_id`フィールドの使用を推奨します）。

{% raw %}
```json
{
  "attributes": [
    {
      "braze_id": "{{${braze_id}}}",
      "subscription_groups": [
        {
          "subscription_group_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}
```
{% endraw %}

{% alert important %}
`use_double_opt_in_logic`を使用する場合、購読状態を更新するにはユーザープロファイルがすでに存在している必要があります。提供された識別子に関連付けられたユーザープロファイルがない場合、購読状態は更新されません。
{% endalert %}

![前述のJSONコードが含まれるユーザー更新オブジェクト。]({% image_buster /assets/img/sms/user_update_object.png %})

### ステップ4：キャンバスをテストする {#step-4-test-the-canvas}

より広いオーディエンスに送信する前に、[キャンバスをテスト]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases)して期待どおりに動作することを確認することを強く推奨します。

### ステップ5：キャンバスを開始する {#step-5-launch-your-canvas}

キャンバスのテストが成功したら、ユーザーのサブセットに対してキャンバスを開始しましょう！

ユーザーが正常に移行されたことを確認するには、更新されたいくつかの個別のユーザープロファイルをチェックすることを推奨します。**エンゲージメント**タブで**連絡先設定**を探し、スクロールしてユーザーが購読している購読グループを確認します。RCS購読グループのトグルがオンになっているはずです。

RCS送信者と購読グループの設定については、[RCSの設定]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup)も参照してください。

## ベストプラクティス {#best-practices}

### 購読グループを分けて設定する {#designate-separate-subscription-groups}

- **メッセージングタイプ：** トランザクションやマーケティングなど、メッセージングの種類ごとに異なる購読グループを作成します。
- **ワークスペース：** 明確性と整理性を維持するために、各ワークスペースごとに個別の購読グループを作成します。

以下は、2つのワークスペースにまたがる4つの購読グループの例です。

- **本番ワークスペース**
  - Marketing - PROD for SMS
  - Transactional - PROD for SMS
- **開発ワークスペース（テスト用）**
  - Marketing - DEV for SMS
  - Transactional - DEV for SMS

### わかりやすい命名規則を使用する {#use-clear-naming-conventions}

SMSキャンペーンを作成する際に正しいグループが選択されるよう、説明的でわかりやすい購読グループ名を選びます。

### 国ごとにグループを分ける {#separate-groups-by-country}

SMSの規制は国によって異なります。SMS購読グループを国ごとに分けることをお勧めします。これにより、メッセージを送信するすべての地域でコンプライアンス基準を満たすことができます。

各購読グループでは、**Geographic Permissions**の下で国の許可リストを設定して、SMS、MMS、RCSが承認された地域にのみ送信されるようにすることもできます。詳細については、[地理的権限]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/geographic_permissions)を参照してください。

たとえば、ブラジルでは現地時間の午前9時から午後9時以外の時間帯にマーケティングメッセージを送信することが禁止されており、同国は3つのタイムゾーンにまたがっています。これらの規制に準拠するために、ブラジルと米国宛てのメッセージ送信用に別々のグループを設定することが考えられます。これにより、ブラジルのユーザーが禁止時間帯にマーケティングメッセージを受信することを防止できます。