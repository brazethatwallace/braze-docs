---
nav_title: 購読ステータス
article_title: 購読ステータス
page_order: 0
page_type: reference
description: "Brazeがメール、LINE、SMS、RCS、WhatsAppの購読ステータスをどのように追跡し、ステータスがメッセージ配信をどのように制御するかについて説明します。"

---

# 購読ステータス {#subscription-status}

> Brazeがメッセージングチャネル全体で購読ステータスをどのように追跡するか、グローバルステータスと購読グループステータスがどのように連携するか、チャネル固有のルールがどこで適用されるかについて説明します。

購読ステータスは、ユーザーがチャネルでメッセージを受信する資格があるかどうかをBrazeに伝えます。ステータスはキャンペーンやキャンバスのターゲティング、セグメントフィルター、およびBrazeが配信を試みるかどうかを制御できます。

## Brazeにおける購読ステータスの仕組み {#how-subscription-status-works-in-braze}

Brazeは2つのレベルで購読ステータスを追跡します。

| レベル | 制御する内容 | チャネル |
| ----- | ---------------- | -------- |
| グローバル購読状態 | ユーザーがそのチャネルでメッセージを受信できるかどうか | メール、プッシュ |
| 購読グループステータス | ユーザーがチャネル内の特定のグループにオプトインしているかどうか | メール、SMS、MMS、RCS、WhatsApp、LINE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Brazeにおける購読ステータスの仕組み" }

グローバル状態と購読グループステータスは連携して機能します。メールの場合、グローバルで購読解除されたユーザーは、購読グループに登録されていてもメールを受信しません。SMS、RCS、WhatsApp、LINEの場合、ユーザーはそのグループからメッセージを受信するために、関連する購読グループに登録されている必要があります。

ユーザープロファイルの**エンゲージメント** > **連絡先設定**、REST API、SDK、CSVインポート、ユーザー設定センター、チャネル固有のオプトインフローを通じて、購読ステータスを表示および更新できます。Brazeは購読状態の変更をデータポイントとしてカウントしません。

{% alert note %}
購読グループは、チャネル内で詳細なオプトインを追加します（例：プロモーション用とトランザクション用のSMS）。グローバルメール状態と購読グループのメンバーシップは、誰にリーチ可能かを決定する際に連携して機能します。
{% endalert %}

## メール {#email}

Brazeにはメール用の3つのグローバル購読状態があります。これらの状態は、購読済みまたはオプトイン済みのオーディエンスをターゲットにしたメッセージをユーザーが受信するかどうかを制御します。例えば、`unsubscribed`状態のユーザーは、`subscribed`または`opted-in`のユーザーをターゲットにしたメッセージを受信しません。

| 状態 | 定義 |
| ----- | ---------- |
| オプトイン済み | ユーザーがメールの受信を明示的に確認しました。Brazeは、メール送信の同意を得るために明示的なオプトインプロセスを推奨しています。 |
| 購読済み | ユーザーは購読解除も明示的なオプトインもしていません。これはユーザープロファイルが作成されたときのデフォルトの購読状態です。 |
| 購読解除済み | ユーザーがメールの購読を明示的に解除しました。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="メールの購読状態" }

### メール固有の動作 {#email-specific-behavior}

- **購読解除とスパム報告：** Brazeは、[カスタムフッター]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer)を通じて購読解除したユーザーを自動的に購読解除します。ユーザーがメールをスパムとしてマークした場合、Brazeはトランザクションメール（**購読解除済みユーザーを含むすべてのユーザーに送信**で送信されたメッセージ）のみを送信します。
- **ハードバウンス：** メールアドレスがハードバウンスした場合、Brazeはユーザーの購読状態を自動的に`unsubscribed`に設定しません。Brazeはアドレスを無効としてマークし、ユーザーがメールアドレスを更新するまで送信を停止します。
- **共有メールアドレス：** ユーザーのグローバルメール購読状態が変更されると、Brazeはその状態を同じメールアドレスを共有する他のプロファイルに伝播します（変更ごとに最大100プロファイル）。
- **メールアドレスの更新：** ユーザーがメールアドレスを更新すると、購読状態は`subscribed`に設定されます。ただし、更新されたアドレスが別のプロファイルに既に存在する場合、ユーザーはそのプロファイルの状態を継承します。

購読状態の更新、ステータスの確認、ユーザー設定センター、キャンペーンターゲティングについては、[メール購読]({{site.baseurl}}/user_guide/channels/email/subscriptions)を参照してください。

## LINE {#line}

LINEの購読ステータスについては、LINEが信頼できる情報源です。ユーザープロファイルに`native_line_id`があっても、そのユーザーがLINEチャネルをフォローしていない限り、BrazeはLINEメッセージを配信しません。

LINEの購読ステータスは`external_id`ではなく`native_line_id`で追跡されます。複数のプロファイルが同じ`native_line_id`を共有している場合、同じLINE購読ステータスを継承します。

| 状態 | 定義 |
| ----- | ---------- |
| 購読済み | ユーザーがLINEアプリ内からLINEチャネルをフォローしました。 |
| 購読解除済み | ユーザーがLINEチャネルをフォローしていないか、明示的にフォロー解除しました。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINEの購読状態" }

### 購読同期ツール {#subscription-sync-tool}

LINEチャネルの統合が成功すると、Brazeは既存のBrazeプロファイルをLINEフォロワーデータと整合させるための購読同期ツールをデプロイします。

- チャネルをフォローしている`native_line_id`を持つプロファイルは`subscribed`に更新されます。
- 一致するBrazeプロファイルがないフォロワーには、`native_line_id`、`line_id`ユーザーエイリアス、および`subscribed`ステータスを持つ匿名プロファイルが作成されます。

統合中にLINE購読グループの状態を手動で設定することはできません。LINEがステータスを制御し、Brazeがそれを同期します。

### フォローおよびフォロー解除イベントの更新 {#follow-and-unfollow-event-updates}

Brazeが統合チャネルのLINE Webhookイベントを受信した場合：

- **フォロー：** 一致する`native_line_id`を持つすべてのプロファイルが`subscribed`に設定されます。プロファイルが存在しない場合、Brazeは[匿名ユーザーを作成]({{site.baseurl}}/user_guide/channels/line/message_users/user_management)します。
- **フォロー解除：** 一致する`native_line_id`を持つすべてのプロファイルが`unsubscribed`に設定されます。

設定手順、ユーザー照合、ユースケースについては、[LINE設定]({{site.baseurl}}/user_guide/channels/line/line_setup#user-setup)および[LINE購読グループ]({{site.baseurl}}/user_guide/channels/line/message_users/subscription_groups)を参照してください。

## SMSとRCS {#sms-and-rcs}

SMSとRCSは、個別のグローバルチャネル状態ではなく、購読グループステータスを使用します。ユーザーはトランザクショングループに`subscribed`であると同時に、プロモーショングループから`unsubscribed`であることが可能です。

| 状態 | 定義 |
| ----- | ---------- |
| 購読済み | ユーザーは、Braze購読APIやオプトインキーワード、またはその他のサポートされている方法を通じて、特定の購読グループからSMSおよびRCSを受信するよう購読しています。[ダブルオプトイン]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in)が有効な場合、ユーザーはステータスが`Subscribed`に更新される前にオプトインを確認する必要があります。 |
| 購読解除済み | ユーザーがオプトアウトキーワードのテキスト送信または[Braze購読API]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)を通じて、その購読グループからオプトアウトしました。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMSとRCSの購読状態" }

### SMSとRCS固有の動作 {#sms-and-rcs-specific-behavior}

- **電話番号の継承：** 電話番号がプロファイルに追加または更新されると、その番号はプロファイルまたはその番号を既に使用している既存のプロファイルから購読グループステータスを継承します。
- **キーワード処理：** ユーザーはデフォルトまたはカスタムの[キーワード]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout)をテキスト送信することでオプトインまたはオプトアウトできます。Brazeは購読状態を自動的に更新します。
- **コンプライアンス：** Brazeは、選択された購読グループに登録されていないユーザーにSMSまたはRCSを送信しません。

設定、送信、購読グループの管理については、[SMS、MMS、RCS購読グループ]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups)を参照してください。

## WhatsApp {#whatsapp}

WhatsAppも購読グループステータスを使用します。Metaはマーケティングメッセージを送信する前に、明示的な[オプトイン同意](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)を要求しています。

| 状態 | 定義 |
| ----- | ---------- |
| 購読済み | ユーザーがオプトインフローまたはBraze購読APIを通じて、ビジネスからのWhatsAppメッセージの受信を明示的に確認しました。 |
| 購読解除済み | ユーザーがオプトインしていないか、オプトインが取り消されました。購読解除済みのユーザーは、その購読グループの電話番号からメッセージを受信しません。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="WhatsAppの購読状態" }

### オプトイン要件 {#opt-in-requirements}

WhatsAppでユーザーにメッセージを送信するには、各ユーザーの`external_id`、[電話番号]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers)、および更新された購読ステータスをBrazeに提供してください。Webサイト、アプリ、SMS、アプリ内メッセージ、インバウンドWhatsAppスレッド、または他の場所で既にオプトインしたユーザーのCSVインポートを通じてオプトインを収集します。

### オプトアウト方法 {#opt-out-methods}

ユーザーは以下の方法でオプトアウトできます。

- **インバウンドキーワードワークフロー：** オプトアウトキーワード（例：「STOP」）によってトリガーされるキャンバスまたはキャンペーンで、購読ステータスを更新するフォローアップステップを含みます。
- **マーケティングオプトアウトクイックリプライ：** Metaのマーケティングオプトアウトボタンを含むメッセージテンプレートで、キャンバス内の購読グループ更新ステップと組み合わせます。
- **ブロックと報告：** ユーザーがビジネスをブロックした場合、以降のメッセージは配信されず課金もされませんが、Brazeの購読ステータスは更新されません。ユーザーの報告も購読ステータスを変更しません。

### WhatsAppの「お知らせとキャンペーン」トグル {#whatsapp-offers-and-announcements-toggle}

WhatsAppネイティブの**お知らせとキャンペーン**トグルは、Brazeの購読グループとは別のものです。ユーザーがWhatsAppでこれをオフにすると、Brazeが`subscribed`と表示していても、Metaがマーケティング配信をブロックします。2つのレイヤーは自動的に同期されません。

ステップバイステップのオプトインおよびオプトアウトワークフローについては、[WhatsAppのオプトインとオプトアウト]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs)および[WhatsApp購読グループ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)を参照してください。

## 購読ステータスによるセグメントとターゲティング {#segment-and-target-by-subscription-status}

セグメントビルダーの購読ステータスフィルターを使用して、チャネルごとにオーディエンスをターゲットまたは抑制できます。例えば、**メール購読ステータス**、**プッシュ購読ステータス**、**購読グループ**フィルターがあります。

キャンペーンやキャンバスを作成する際、**送信設定**と**ターゲットオーディエンス**オプションを使用して、特定の購読ステータス（購読済みやオプトイン済みなど）のユーザーにのみ送信できます。メールとプッシュのフィルター定義については、[セグメンテーションフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)を参照してください。