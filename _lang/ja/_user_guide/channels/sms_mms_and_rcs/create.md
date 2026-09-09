---
nav_title: メッセージを作成する
article_title: SMS、MMS、またはRCSメッセージを作成する
page_order: 1
description: "SMS、MMS、またはRCSメッセージを作成し、チャネル固有のメッセージタイプ、フィールド、リンク短縮、配信設定、および動作を構成します。"
page_type: reference
alias: /create_sms_mms_rcs_message/
tool:
  - Campaigns
  - Canvas
channel:
  - SMS
  - MMS
  - RCS
search_rank: 1
---

# SMS、MMS、またはRCSメッセージを作成する {#create-an-sms-mms-or-rcs-message}

> キャンペーンやキャンバスで、パーソナライズされたSMS、MMS、およびRich Communication Services（RCS）メッセージを作成できます。選択した購読グループによって、利用可能なメッセージタイプと送信者が決まります。

## 前提条件 {#prerequisites}

始める前に、以下の要件を満たしていることを確認してください。

| 要件 | 説明 |
| --- | --- |
| 送信者設定 | [送信者設定]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup)を完了します。MMSを送信するには、購読グループにMMS対応の電話番号が必要です。RCSを送信するには、[RCS設定]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup)を完了し、認証済みのRCS送信者を追加します。 |
| 購読グループ | このメッセージの送信者を含む[購読グループ]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups)を作成します。 |
| ユーザーの電話番号と同意 | ユーザーの電話番号をインポートし、適切な[SMS、MMS、RCSのオプトイン]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins)を収集します。 |
| キャンペーンまたはキャンバス | 単一のターゲットメッセージにはキャンペーンを、複数ステップのユーザージャーニーにはキャンバスを使用します。 |
| メッセージまたはアクションクレジット | アカウントにクレジットが利用可能であることを確認します。BrazeからのSMS、MMS、RCSメッセージの送信にはこれらのクレジットが使用されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMS、MMS、RCSメッセージの前提条件" }

## メッセージを作成する {#create-a-message}

### ステップ1：メッセージの作成場所を選択する {#step-1-choose-where-to-build-your-message}

{% tabs %}
{% tab キャンペーン %}

1. **メッセージング** > **キャンペーン**に移動し、**キャンペーンを作成**を選択します。
2. **SMS/MMS/RCS**を選択するか、複数のチャネルを対象とするキャンペーンの場合は**マルチチャネルキャンペーン**を選択します。
3. キャンペーンにわかりやすく意味のある名前を付けます。
4. 必要に応じて[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams)と[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)を追加します。
  - タグを使用すると、キャンペーンの検索やレポートでの活用が容易になります。
5. キャンペーンのバリアントを追加して名前を付けます。同じキャンペーンにSMS/MMSとRCSのバリアントを含めることができます。詳細については、[多変量テストとABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)を参照してください。

{% alert tip %}
キャンペーンのバリアントが似た内容の場合は、最初のメッセージを作成してからバリアントを追加してください。**バリアントを追加**ドロップダウンから**バリアントからコピー**を選択できます。
{% endalert %}

{% endtab %}
{% tab キャンバス %}

{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

### ステップ2：購読グループとメッセージタイプを選択する {#step-2-select-a-subscription-group-and-message-type}

このメッセージの送信元を含む**購読グループ**を選択します。Brazeは選択されたグループを使用して、到達可能なオーディエンスの計算と送信時の適格性の判定を行います。

選択した購読グループによって、メッセージ作成画面で利用可能なメッセージタイプが決まります。

| 購読グループタイプ | 利用可能なメッセージタイプ |
| --- | --- |
| SMSのみ | SMS |
| MMS対応番号付きSMS | SMSおよびMMS |
| 認証済みRCS送信者を含むRCS対応 | RCS、およびグループにSMS送信者も含まれている場合はSMS。その送信者がMMS対応の場合はMMSも利用可能。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="購読グループ別の利用可能なメッセージタイプ" }

{% alert tip %}
RCS配信が失敗した場合にSMSフォールバックを送信できるよう、RCS購読グループには少なくとも1つのSMS送信者を追加してください。
{% endalert %}

購読グループが両方のプロトコルをサポートしている場合は、**SMS/MMS**または**RCS**を選択します。RCSの場合は、**テキスト**、**メディア**、または**カード**を選択します。

### ステップ3：メッセージを作成する {#step-3-compose-your-message}

メッセージ作成画面のフィールドと制限は、選択したメッセージタイプによって異なります。

{% tabs local %}
{% tab SMSおよびMMS %}

#### SMSおよびMMSのフィールドと設定 {#sms-and-mms-fields-and-settings}

| フィールドまたは設定 | 説明 |
| --- | --- |
| **言語** | メッセージに言語固有のコンテンツを挿入します。 |
| **メッセージ** | Liquid、Connected Content、絵文字を含めて最大1,600文字を入力します。メッセージ作成画面はエンコーディング、文字数、課金対象のSMSセグメント数を推定します。MMSメッセージにはメッセージ本文なしでメディアを含めることができます。 |
| **メディア** | MMS対応の購読グループの場合、メディアライブラリまたはURLからPNG、JPEG、またはGIF画像を1つ追加します。画像の代わりにvCardを追加することもできます。 |
| **リンク短縮** | HTTPおよびHTTPS URLを短縮し、エンゲージメントを追跡します。レガシーリンク短縮の場合は、基本トラッキングまたは高度なトラッキングを選択します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMSおよびMMSのフィールドと設定" }

SMSメッセージはGSM-7またはUCS-2エンコーディングを使用し、メッセージセグメント単位で課金されます。1文字の変更でエンコーディングが変わり、課金対象のセグメント数が増える場合があります。エンコーディングルール、セグメントサイズ、セグメント計算ツールについては、[SMSおよびRCS課金計算ツール]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator)を参照してください。

![メッセージの本文と推定文字数・セグメント数を表示するSMSメッセージ作成画面。]({% image_buster /assets/img/sms_campaign_compose.png %})

#### MMSメディア仕様 {#mms-media-specifications}

{% multi_lang_include channels/image_specs.md variable_name='sms and mms' %}

ユーザーがデバイスの連絡先に保存できるビジネス詳細を送信するには、[連絡先カード]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card)を参照してください。連絡先カードの送信はMMSとして課金されます。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

MMSの利用可能性とレンダリングは受信側のキャリアによって異なります。キャリアがMMSを受信できない場合、プロバイダーを通じてメディアはSMS本文内のリンクに変換されます。Google Voice番号へのMMSの送信は、MMS サポートが限定的で配信が不安定になる可能性があるため、避けてください。

ユーザーがインバウンドメディアを送信した場合、BrazeはそのURLを[Currents SMSインバウンドイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events)およびLiquidの{% raw %}`{{sms.${inbound_media_urls}}}`{% endraw %}で公開します。

{% endtab %}
{% tab RCS %}

#### RCSメッセージタイプ {#rcs-message-types}

| メッセージタイプ | フィールドと設定 | 制限と動作 |
| --- | --- | --- |
| **テキスト** | 必須のメッセージ本文、オプションの候補返信またはURLを開くアクション、オプションのSMSフォールバック、リンク短縮 | メッセージ本文にはSMSサービスプロバイダーに応じて最大1,600文字または3,072文字を含めることができます。候補は最大5つまで追加できます。 |
| **メディア** | 必須の画像、動画、ドキュメント、またはオーディオ、オプションのメッセージ本文、オプションの候補、SMSフォールバック、リンク短縮 | メッセージ本文にはプロバイダーに応じて最大1,600文字または3,072文字を含めることができ、追加のRCSメッセージとして課金されます。候補は最大5つまで追加できます。すべてのプロバイダーが独立した**メディア**メッセージをサポートしているわけではありません（例：Twilio）。 |
| **カード** | メディアカードまたはテキストのみのカード、タイトル、説明、ボタン、オプションの候補、オプションのSMSフォールバック | タイトルは最大200文字です。説明はプロバイダーに応じて最大1,600文字または2,000文字です。ボタンは1〜4つまで追加できます。レイアウトとフィールドの利用可能性については、[カードメッセージのプロバイダーサポート](#provider-support-for-card-messages)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="RCSメッセージタイプ、フィールド、および制限" }

#### カードレイアウト {#card-layouts}

RCSの**カード**メッセージは、メディア、テキスト、ボタンを1つのユニットにまとめます。メッセージ作成画面でレイアウトを選択します。

| カードレイアウト | 必須フィールド | オプションフィールド |
| --- | --- | --- |
| **テキストのみ** | タイトル、説明、少なくとも1つのカードボタン | 追加のカードボタン最大3つ、カード外の候補（サポートされている場合）、SMSフォールバック |
| **メディア** | 画像、GIF、または動画、少なくとも1つのカードボタン | タイトル、説明、追加のカードボタン最大3つ、カード外の候補（サポートされている場合）、SMSフォールバック |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="RCSカードレイアウト" }

カードのタイトル、説明、メディア、ボタンをパーソナライズするにはLiquidを使用します。タイトルや説明にプレーンテキストとして入力されたURLはクリックできません。代わりに**URLを開く**カードボタンを追加してください。

候補には、ユーザーのテキスト入力をあらかじめ入力する候補返信と、URLを開くアクションがあります。各候補には最大25文字のテキスト、各URLを開くアクションには最大2,048文字のURLを追加できます。**RCSが失敗した場合にSMSを送信**をオンにすると、RCS配信が失敗した場合に最大1,600文字のフォールバックメッセージが追加されます。選択した購読グループにはSMS送信者が含まれている必要があります。リンク短縮はSMSフォールバック本文内のリンクにのみ適用され、カードボタンのURLには適用されません。

RCSメッセージの課金はメッセージタイプとコンテンツによって異なります。基本、リッチ、リッチカードの課金ルールについては、[RCSメッセージの課金]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#rcs-message-billing)を参照してください。

#### カードメッセージのプロバイダーサポート {#provider-support-for-card-messages}

RCSメッセージタイプとカードオプションの利用可能性は、SMSサービスプロバイダーによって異なります。メッセージ作成画面にはサポートされているタイプとフィールドのみが表示されます。

| 機能 | Infobip | Twilio |
| --- | --- | --- |
| 独立した**メディア**メッセージタイプ | サポートあり | サポートなし |
| テキストのみのカードレイアウト | サポートあり | サポートなし |
| メディアカードレイアウト | サポートあり | サポートあり |
| カード外の候補 | サポートあり | サポートなし |
| カードボタン | サポートあり（1〜4） | サポートあり（1〜4） |
| 説明文字数制限 | 最大2,000文字 | 最大1,600文字 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="RCSカードメッセージのプロバイダーサポート" }

#### RCSメディア仕様 {#rcs-media-specifications}

メッセージ作成画面では最大1,000文字のメディアURLを受け付けます。利用可能な形式と最大ファイルサイズはSMSサービスプロバイダーによって異なります。

| ファイルタイプ | 仕様 |
| --- | --- |
| すべて | プロバイダーに応じて最大ファイルサイズは16&nbsp;MBまたは100&nbsp;MBです。 |
| 画像 | JPEG、JPG、GIF、PNG |
| 動画 | H263、M4V、MP4、MPEG、MPEG-4、WEBM |
| ドキュメント | PDF。**メディア**メッセージで利用可能ですが、メディアカードでは利用できません。 |
| オーディオ | AAC、MP3、MPEG、MP4、3GPP、OGG。プロバイダーのサポートは異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="RCSメディア仕様" }

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% endtab %}
{% endtabs %}

#### パーソナライゼーション {#personalization}

[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)、[Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)、絵文字、言語固有のコンテンツを使用してメッセージをパーソナライズします。データが不完全なプロファイルに空のコンテンツが表示されないように、Liquidパーソナライゼーションにはデフォルト値を設定してください。

プロンプトからメッセージコピーを作成するには、Operatorの[コピーを生成]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy)を使用します。

右から左に書く言語については、[右から左へのメッセージの作成]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)を参照してください。

#### 会話型メッセージワークフローの作成（RCS） {#create-conversational-message-workflows-rcs}

会話型メッセージワークフローを使用すると、ユーザーにダイナミックに応答し、双方向のメッセージング体験を構築できます。ワークフローを作成するには、キャンバスを作成し、候補返信と[アクションパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)を組み合わせて、ユーザーが選択した返信に基づいてワークフローを誘導します。

1. キャンバスビルダーで、複数の候補返信を含むRCSメッセージステップを作成します。

![候補返信を含むRCSメッセージ作成画面。]({% image_buster /assets/img/rcs/suggested_replies.png %})

{: start="2"}
2. そのメッセージを、各候補返信に対応するアクショングループを持つアクションパスに接続します。
3. 各アクショングループで以下を設定します。
   - トリガーとして**SMSインバウンドメッセージを送信**を選択します。
   - メッセージ本文を対応する候補返信と同じ内容に設定します。

![3つのアクショングループが設定されたアクションパスステップ。各アクショングループは候補返信に対応しています。]({% image_buster /assets/img/rcs/quick_reply.png %})

{: start="4"}
4. 各アクショングループをRCSメッセージステップに接続し、対応する候補返信に基づいたコンテンツを追加します。
5. フォローアップメッセージに候補返信を追加して、会話型ワークフローを続けます。
6. ワークフローが完成するまでステップ2〜4を繰り返します。

![2つのアクションパスを含む会話型ワークフローを示すキャンバス。]({% image_buster /assets/img/rcs/full_conversational_workflow.png %})

### ステップ4：リンク短縮を設定する {#step-4-configure-link-shortening}

**リンク短縮**をオンにして、HTTPおよびHTTPS URLを短縮し、SMS、MMS、およびサポートされているRCSリンクのクリックを追跡します。ワークスペースで利用可能なバージョンに応じて、基本トラッキングまたは高度なトラッキングを選択するか、統合リンク短縮を使用します。

高度なトラッキングは、セグメンテーションとリターゲティングのためにユーザーレベルのクリックデータを追加します。統合リンク短縮は、SMSとRCSの短縮リンクを1つのパーソナライズされた形式にまとめます。サポートされるURL、Liquidの動作、テスト要件、カスタムドメイン、リターゲティングについては、[リンク短縮]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening)を参照してください。

Brazeは1つのメッセージで最大25個のリンクを短縮します。4,000文字を超えるURLは短縮できず、送信時にメッセージが失敗する原因となります。

### ステップ5：メッセージをプレビューしてテストする {#step-5-preview-and-test-your-message}

**テスト**タブに移動して、ユーザーとしてメッセージをプレビューするか、[コンテンツテストグループ]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups)または個々のユーザーにテストSMS、MMS、またはRCSメッセージを送信します。

{% alert tip %}
[SMSセグメント計算ツール]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator)を使用して、メッセージに含まれるセグメント数を推定できます。
{% endalert %}

![メッセージ作成画面のテストタブからのSMSコピーのプレビュー。プロファイルセクションでは名フィールドが「James」に設定されています。プレビューセクションでは、SMSに「Hi James, we appreciate your support!」と表示されています。]({% image_buster /assets/img/sms_campaign_test.png %})

MMSの場合、メディアがメッセージ本文の前に表示されるか後に表示されるかは、受信側の電話によって決まります。

{% alert note %}
RCSのレンダリングはユーザーのオペレーティングシステム、デバイスメーカー、キャリア、メッセージングアプリ（例：Google MessagesとApple Messages）によって制御されるため、メッセージの外観は異なる場合があります。Brazeに表示されるプレビューは、エンドユーザーが受信するものと正確に一致しない場合があります。可能な限り実際のデバイスで最終的なレンダリングを確認してください。iOSデバイスでのRCSレンダリングの詳細については、[iOSデバイスでRCSメッセージが正確にレンダリングされないのはなぜですか？]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#why-doesnt-my-rcs-message-render-accurately-on-ios-devices)を参照してください。リッチカードでのGIFについては、[iOSでRCSリッチカードのGIFが静止画で表示されるのはなぜですか？]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#why-do-gifs-in-rcs-rich-cards-appear-static-on-ios)を参照してください。
{% endalert %}

詳細については、[テストメッセージの送信]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=sms%2Fmms%20and%20rcs)を参照してください。

### ステップ6：キャンペーンまたはキャンバスの残りの部分を作成する {#step-6-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab キャンペーン %}

#### 配信スケジュールまたはトリガーを選択する {#choose-a-delivery-schedule-or-trigger}

スケジュールされた時間、またはアクションやAPIトリガーに応答してメッセージを配信します。スケジュールとトリガーのオプションについては、[キャンペーンのスケジュール設定]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)を参照してください。

[再適格性]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility)や[フリークエンシーキャップ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping)などの配信コントロールを設定します。アクションベースの配信の場合は、キャンペーンの期間と[サイレント時間]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)を設定します。

#### ターゲットユーザーを選択する {#choose-users-to-target}

セグメントとフィルターを選択して[ユーザーをターゲット]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)します。Brazeはメッセージ送信前にセグメントメンバーシップを正確に計算します。

選択した購読グループは、購読済みのユーザーでフィルタリングします。SMSおよびMMSの受信者には有効な電話番号も必要です。RCSの受信者にはRCS対応のデバイスとキャリア接続が必要です。RCS配信が失敗した場合に適格なユーザーに到達するには、SMSフォールバックを使用してください。

{% multi_lang_include audience/target_audiences.md %}

クリックおよびインタラクションのターゲティングについては、[ユーザーリターゲティング]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting)を参照してください。

#### コンバージョンイベントを選択する {#choose-conversion-events}

ユーザーがキャンペーンを受信した後のアクションを測定するには、[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)を使用します。コンバージョンウィンドウは最大30日間に設定できます。

{% endtab %}
{% tab キャンバス %}

キャンバスの残りのセクションを完成させます。エントリスケジュール、オーディエンス設定、送信コントロールについては、[キャンバスを作成する]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)を参照してください。

{% endtab %}
{% endtabs %}

### ステップ7：レビューしてデプロイする {#step-7-review-and-deploy}

キャンペーンまたはキャンバスの作成が完了したら、詳細をレビューし、送信前にメッセージをテストしてください。

ローンチ後は、[SMS、MMS、RCSレポート]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting)を使用してメッセージのパフォーマンスを確認します。

## 知っておくべきこと {#things-to-know}

- SMSはメッセージセグメントごとに課金され、MMSは独自のレートで課金され、RCSはメッセージタイプごとに課金されます。送信前に[SMSおよびRCS請求計算ツール]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator)を確認してください。
- MMSは1つの画像またはvCardをサポートしています。キャリアのサポート状況により、受信者がメディアを受信するか画像リンクを受信するかが決まります。
- RCSの機能と制限はSMSサービスプロバイダーによって異なります。メッセージ作成画面には、選択した購読グループで利用可能なオプションのみが表示されます。
- 事前に録音したボイスメールを、RCSの**メディア**メッセージとして音声で送信できます。
- 表示や操作の動作は、デバイス、キャリア、オペレーティングシステム、メッセージングアプリによって異なります。