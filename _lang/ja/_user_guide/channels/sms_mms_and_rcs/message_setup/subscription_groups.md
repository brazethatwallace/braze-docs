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

> サブスクリプショングループは、Brazeを通じてSMS、MMS、RCSメッセージを送信するための基盤です。サブスクリプショングループは、特定の種類のメッセージング目的に使用される[送信エンティティ]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup/)（RCS認証済み送信者、SMSショートコード、SMSロングコード、SMS英数字送信者IDなど）の集合です。たとえば、ブランドがトランザクションSMSとプロモーションSMSの両方を送信する予定がある場合、Brazeダッシュボード内で送信電話番号のプールが別々の2つのサブスクリプショングループを設定する必要があります。

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

## サブスクリプショングループの状態 {#subscription-group-states}

SMSおよびRCSユーザーには、`subscribed`と`unsubscribed`の2つのサブスクリプション状態があります。ユーザーのサブスクリプション状態はサブスクリプショングループレベルに存在し、サブスクリプショングループ間で共有されません。つまり、ユーザーはトランザクションサブスクリプショングループでは`subscribed`であっても、プロモーションサブスクリプショングループでは`unsubscribed`である場合があります。ブランドにとって、この状態の分離により、ユーザーに関連するSMSおよびRCSメッセージを引き続き送信できます。

| 状態 | 定義 |
| --------- | ---------- |
| 購読中 | ユーザーは特定のサブスクリプショングループからSMSおよびRCSを受信するよう購読しています。ユーザーは、BrazeサブスクリプションAPIを通じてサブスクリプション状態を更新するか、オプトインキーワード応答をテキスト送信することで購読できます。ユーザーがSMS、RCS、またはその両方を受信するには、SMSまたはRCSサブスクリプショングループに購読している必要があります。[ダブルオプトイン]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in/)が有効な場合、ユーザーはサブスクリプションステータスが`Subscribed`に更新される前にオプトインの意思を確認する必要があります。 |
| 購読解除 | ユーザーはSMSおよびRCSサブスクリプショングループとそのサブスクリプショングループ内の送信電話番号からのメッセージングを明示的にオプトアウトしています。オプトアウトキーワード応答をテキスト送信するか、[BrazeサブスクリプションAPI]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)を通じてユーザーの購読を解除できます。SMSおよびRCSサブスクリプショングループから購読解除されたユーザーは、そのサブスクリプショングループに属する送信電話番号からSMSまたはRCSを受信しなくなります。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="サブスクリプショングループの状態" }

### ユーザーの状態を設定する {#set-a-users-state}

ユーザープロファイルで電話番号が更新されると、新しい電話番号はそのユーザーのサブスクリプショングループステータスを継承します。電話番号がBrazeに既に存在する番号に更新された場合、その既存の電話番号のサブスクリプションステータスが継承されます。

たとえば、ユーザーAが複数のサブスクリプショングループに購読している電話番号を持っていて、その電話番号がユーザーBに追加された場合、ユーザーBは同じサブスクリプショングループに購読されます。ユーザーが既存のサブスクリプションを継承するのを防ぐには、ユーザーが番号を変更するたびにBraze REST APIを通じて古い番号のサブスクリプショングループをリセットできます。複数のユーザーがこの電話番号を共有している場合、全員が購読解除されます。

ユーザーのサブスクリプショングループの状態を設定するには、以下のいずれかの方法を使用します。

- **REST API:** ユーザープロファイルは、Braze REST APIを使用して[`/subscription/status/set`エンドポイント]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)でプログラム的に設定できます。
- **SDK統合:** ユーザーは、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html)、[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:))、または[Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)の`addToSubscriptionGroup`メソッドを使用して、メールまたはSMSおよびRCSサブスクリプショングループに追加できます。
- **電話番号キャプチャIAMフォーム:** アプリ内メッセージのドラッグ＆ドロップエディターの電話番号キャプチャテンプレートを通じて、ユーザーの電話番号を収集できます。
- **ユーザーのオプトイン/オプトアウト時に自動処理:** ユーザーがデフォルトのオプトインまたはオプトアウト[キーワード]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout/)をテキスト送信すると、Brazeはユーザーのサブスクリプション状態を自動的に設定および更新します。
- **ユーザーインポート:** ユーザーは**Import Users**を通じてメールまたはSMSおよびRCSサブスクリプショングループに追加できます。サブスクリプショングループのステータスを更新する場合、CSVに`subscription_group_id`と`subscription_state`の2つの列が必要です。詳細については、[ユーザーインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/#updating-subscription-group-status)を参照してください。

#### Canvasでユーザーの状態を更新する {#update-a-users-state-in-a-canvas}

キャンバスフローの一部としてユーザーのサブスクリプショングループステータスを更新する場合は、Webhookの代わりに[ユーザーの更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/)ステップを使用してください。ユーザーの更新ステップは、処理が完了するまで待ってからユーザーを次のステップに進めるため、後続のメッセージングステップでは更新されたサブスクリプションステータスが使用されます。

Webhookを使用してサブスクリプショングループを更新すると、ユーザーはWebhookが送信された時点で進行し、サブスクリプション変更の処理が完了した時点ではありません。これにより、フォローアップのSMSステップがユーザーの購読前に実行される競合が発生し、一部のユーザーでメッセージが失敗する可能性があります。Webhookを使用する必要がある場合は、次のメッセージングステップの前に少なくとも1分の遅延ステップを追加してください。

#{% multi_lang_include api/orphaned_subscription_states.md %}

### ユーザーのグループを確認する {#check-a-users-group}

ユーザーのサブスクリプショングループを確認するには、以下のいずれかの方法を使用します。

- **ユーザープロファイル:** 個々のユーザープロファイルは、サイドバーから**ユーザー検索**を選択してBrazeダッシュボードからアクセスできます。ここでは、メールアドレス、電話番号、または外部ユーザーIDでユーザープロファイルを検索できます。ユーザープロファイル内の「エンゲージメント」タブで、ユーザーのSMSおよびRCSサブスクリプショングループを確認できます。
- **REST API:** 個々のユーザープロファイルのサブスクリプショングループは、Braze REST APIを使用して[ユーザーのサブスクリプショングループを一覧表示するエンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/)または[ユーザーのサブスクリプショングループステータスを一覧表示するエンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/)で確認できます。

## サブスクリプショングループでメッセージを送信する {#send-messages-with-a-subscription-group}

Brazeを通じてSMSまたはRCSのCampaignを開始するには、**SMS/MMS/RCSバリアント**ドロップダウンからサブスクリプショングループを選択します。選択すると、オーディエンスフィルターがCampaignまたはCanvasに自動的に追加され、選択したサブスクリプショングループに`subscribed`しているユーザーのみがターゲットオーディエンスに含まれるようになります。

{% alert important %}
国際的な[通信コンプライアンスおよびガイドライン]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations/)に準拠して、Brazeは選択したサブスクリプショングループに購読していないユーザーにSMSまたはRCSを送信しません。
{% endalert %}

![サブスクリプショングループのドロップダウンが開いたSMSコンポーザーで、ユーザーが「Messaging Service A for SMS」をハイライトしている様子。]({% image_buster /assets/img/sms/sms_subgroup_select.png %})

## SMSサブスクリプショングループのベストプラクティス {#sms-subscription-group-best-practices}

メッセージング目的ごと（たとえば、トランザクションとマーケティング）およびワークスペースごとに、別々のSMSサブスクリプショングループを設計してください。複数の国で運用する場合は、現地のコンプライアンスルールをサポートするために地域別にグループを分けることを検討してください。たとえば、ブラジルではプロモーション送信時間帯に制限があります。

## サブスクリプショングループを有効にする {#enable-subscription-groups}

SMS、MMS、またはRCSのサブスクリプショングループを有効にするには、以下を参照してください。

{% tabs local %}
{% tab SMS %}
SMSオンボーディングプロセス中に、Brazeオンボーディングマネージャーがダッシュボードアカウントのサブスクリプショングループを設定します。必要なサブスクリプショングループの数を決定し、適切な送信電話番号をサブスクリプショングループに追加します。サブスクリプショングループの設定にかかる時間は、追加する電話番号の種類によって異なります。たとえば、ショートコードの申請には8〜12週間かかる場合がありますが、ロングコードは1日以内に設定できます。Brazeダッシュボードの設定について質問がある場合は、Brazeの担当者にお問い合わせください。
{% endtab %}

{% tab MMS %}
MMSメッセージを送信するには、サブスクリプショングループ内の少なくとも1つの番号がMMS送信に対応している必要があります。これは、サブスクリプショングループの横にあるタグで示されます。

![サブスクリプショングループのドロップダウンで「Messaging Service A for SMS」がハイライトされている様子。エントリの先頭に「MMS」タグが付いています。]({% image_buster /assets/img/sms/mms_sub_group_tag.png %}){: style="max-width:40%"}
{% endtab %}

{% tab RCS %}
RCSメッセージを送信する前に、サブスクリプショングループ内にRCS認証済み送信者が存在する必要があります。

RCS認証済み送信者を追加するには、2つの方法があります。
- 既存のサブスクリプショングループに追加する
- 新しいRCSサブスクリプショングループを作成する
選択は、関心のあるRCSユースケースに大きく依存します。

統合に応じて、Brazeは既存のSMSサブスクリプショングループにRCS認証済み送信者を追加するか、新しいサブスクリプショングループを設定できます。いずれの場合も、カスタマーサクセスマネージャーがシームレスで効率的なSMSトラフィックのアップグレードをガイドします。
{% endtab %}
{% endtabs %}

## エージェントコンソールで自然言語のオプトアウトを処理する {#handle-natural-language-opt-outs-in-the-agent-console}

包括的なサブスクリプション管理のために、標準キーワードやカスタムキーワード以外のオプトアウト意図（「もうテキストを送らないでください」など）をキャプチャできます。AIエージェントを作成することで、感情分析を使用してこれらのリクエストを自動的に識別し、対応できます。

### セットアップ {#setup}

1. [エージェントコンソール]({{site.baseurl}}/user_guide/brazeai/agents/)で「SMSセンチメント分析エージェント」を作成します。

{% alert tip %}
初期エージェント設定のサポートには[Operator]({{site.baseurl}}/user_guide/brazeai/agents/reference/#canvas-agent-examples)を使用してください。
{% endalert %}

{: start="2"}
2. **その他**のキーワードカテゴリ内で、**SMS受信メッセージを送信**によってトリガーされるアクションベースのCanvasを作成します。
3. Canvasに[エージェントステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step/)を追加して、オプトアウト意図を識別します。
4. リクエストを確認するための後続のSMS[メッセージステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/)を追加します：「SMSの配信停止をご希望のようですので、配信を停止いたします。間違いの場合は、STARTとテキスト送信して再度オプトインしてください。」
5. [ユーザーの更新ステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/#user-update)を追加して、特定のSMSサブスクリプショングループでのユーザーのステータスを「購読解除」に変更します。

{% alert note %}
エージェントコンソールの使用にはメッセージクレジットまたはアクションクレジットが消費されます。
{% endalert %}

## SMSトラフィックをRCSに移行する {#migrate-sms-traffic-to-rcs}

SMSとRCSのサブスクリプショングループが別々にある場合、1ステップのCanvasを使用してユーザーをSMSからRCSに移行できます。

Brazeでは、最初は少数のユーザーにRCSの送信をテストし、時間をかけてより多くのユーザーをRCSサブスクリプショングループに移行することを推奨しています。たとえば、SMSサブスクリプショングループに1,000,000人のユーザーが購読している場合、まずすべてのユーザーを新しいサブスクリプショングループに移行し、次に50,000〜100,000人（5〜10%）の小規模なオーディエンスにセグメントしてRCSメッセージをテストするという方法が考えられます。

### ステップ1: Canvasを作成してエントリスケジュールを設定する {#step-1-create-a-canvas-and-fill-out-the-entry-schedule}

Canvasを作成し、識別しやすい名前を付けます（「SMS-RCSサブスクリプショングループユーザー移行」など）。次に、都合の良いタイミングでスケジュールします。

### ステップ2: オーディエンスを定義する {#step-2-define-your-audience}
{: #step-2-define-your-audience}

以下のいずれかの方法でオーディエンスを定義します。次に、**送信設定**ステップに進み、**購読中またはオプトイン済みのユーザー**を選択します。

| 方法 | 説明 |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **セグメントを作成する** | サブスクリプショングループ内のすべてのユーザーまたはセグメンテーションフィルターを使用したサブセット（ランダムな5〜10%など）を含むセグメントを作成します。セグメントは各送信前に更新され、現在のユーザー群を反映します。 |
| **CampaignまたはCanvasフィルターを適用する** | CampaignまたはCanvasの**ターゲットオーディエンス**ステップでオーディエンスを絞り込みます。ページを離れることなくターゲティングオプションを調整でき、柔軟性が向上します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ2: オーディエンスを定義する" }

### ステップ3: ユーザーの更新ステップを設定する {#step-3-configure-a-user-update-step}

Canvasにユーザーの更新ステップを追加します。ステップ内で**高度なJSONエディター**を開き、以下を入力します（一意のユーザー識別子フィールドには、`braze_id`フィールドの使用を推奨します）。

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

![前述のJSONコードを含む「ユーザーの更新オブジェクト」。]({% image_buster /assets/img/sms/user_update_object.png %})

### ステップ4: Canvasをテストする {#step-4-test-the-canvas}

より広いオーディエンスに送信する前に、[Canvasをテスト]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases/)して期待どおりに動作することを確認することを強く推奨します。

### ステップ5: Canvasを起動する {#step-5-launch-your-canvas}

Canvasのテストが成功したら、ユーザーのサブセットに対して起動しましょう！

ユーザーが正常に移行されたことを確認するには、更新された個々のユーザープロファイルをいくつか確認することを推奨します。**エンゲージメント**タブで**連絡先設定**を探し、スクロールしてユーザーが購読しているサブスクリプショングループを確認します。RCSサブスクリプショングループのトグルがオンになっているはずです。

RCS送信者とサブスクリプショングループの設定については、[RCSの設定]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup/)も参照してください。

## ベストプラクティス {#best-practices}

### 別々のサブスクリプショングループを指定する {#designate-separate-subscription-groups}

- **メッセージングタイプ:** トランザクションやマーケティングなど、メッセージングの種類ごとに個別のサブスクリプショングループを作成します。
- **ワークスペース:** 明確さと整理を維持するために、ワークスペースごとに個別のサブスクリプショングループを作成します。

2つのワークスペースにまたがる4つのサブスクリプショングループの例を考えてみましょう。

- **本番ワークスペース**
  - Marketing - PROD for SMS
  - Transactional - PROD for SMS
- **開発ワークスペース（テスト用）**
  - Marketing - DEV for SMS
  - Transactional - DEV for SMS

### 明確な命名規則を使用する {#use-clear-naming-conventions}

SMSのCampaignを作成する際に正しいグループが選択されるよう、わかりやすく明確なサブスクリプショングループ名を選択してください。

### 国別にグループを分ける {#separate-groups-by-country}

SMS規制は国によって異なります。SMSサブスクリプショングループを国別に分けることを推奨します。これにより、メッセージを送信するすべての地域でコンプライアンス基準を満たすことができます。

各サブスクリプショングループでは、**Geographic Permissions**の下で国の許可リストを設定し、SMS、MMS、RCSが承認された地域にのみ送信されるようにすることもできます。詳細については、[地理的権限]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/geographic_permissions/)を参照してください。

たとえば、ブラジルでは現地時間の午前9時から午後9時以外のマーケティングメッセージの送信が禁止されており、国内には3つのタイムゾーンがあります。これらの規制に準拠するために、ブラジルと米国へのメッセージ送信用に別々のグループを設定することが考えられます。これにより、ブラジルのユーザーが禁止時間帯にマーケティングメッセージを受信することを防ぎます。