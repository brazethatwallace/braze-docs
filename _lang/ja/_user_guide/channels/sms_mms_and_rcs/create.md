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
| 送信者の設定 | [送信者の設定]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup)を完了してください。MMSを送信するには、購読グループにMMS対応の電話番号が必要です。RCSを送信するには、[RCSの設定]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup)を完了し、認証済みのRCS送信者を追加してください。 |
| 購読グループ | このメッセージの送信者を含む[購読グループ]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups)を作成してください。 |
| ユーザーの電話番号と同意 | ユーザーの電話番号をインポートし、適切な[SMS、MMS、およびRCSのオプトイン]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins)を収集してください。 |
| キャンペーンまたはキャンバス | 単一のターゲットメッセージにはキャンペーンを、マルチステップのユーザージャーニーにはキャンバスを使用してください。 |
| メッセージまたはアクションクレジット | アカウントに利用可能なクレジットがあることを確認してください。BrazeからのSMS、MMS、およびRCSメッセージの送信にはこれらのクレジットが使用されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMS、MMS、およびRCSメッセージの前提条件" }

## メッセージを作成する {#create-a-message}

### ステップ1：メッセージの作成場所を選択する {#step-1-choose-where-to-build-your-message}

{% tabs %}
{% tab キャンペーン %}

1. **メッセージング** > **キャンペーン**に移動し、**キャンペーンを作成**を選択します。
2. **SMS/MMS/RCS**を選択するか、複数のチャネルをターゲットとするキャンペーンの場合は**マルチチャネルキャンペーン**を選択します。
3. キャンペーンにわかりやすく意味のある名前を付けます。
4. 必要に応じて[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams)と[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)を追加します。
  - タグを使うと、キャンペーンの検索やレポートでの活用が容易になります。
5. キャンペーンのバリアントを追加して名前を付けます。同じキャンペーンにSMS/MMSとRCSのバリアントを含めることができます。詳細については、[多変量テストとABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)を参照してください。

{% alert tip %}
キャンペーンのバリアントが同様のコンテンツを持つ場合は、バリアントを追加する前に最初のメッセージを作成してください。**バリアントを追加**ドロップダウンから**バリアントからコピー**を選択できます。
{% endalert %}

{% endtab %}
{% tab キャンバス %}

{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

### ステップ2：購読グループとメッセージタイプを選択する {#step-2-select-a-subscription-group-and-message-type}

このメッセージの送信者を含む**購読グループ**を選択します。Brazeは選択されたグループを使用して、到達可能なオーディエンスを計算し、送信時の適格性を判断します。

選択した購読グループによって、メッセージ作成画面で利用可能なメッセージタイプが決まります。

| 購読グループのタイプ | 利用可能なメッセージタイプ |
| --- | --- |
| SMSのみ | SMS |
| MMS対応番号を含むSMS | SMSおよびMMS |
| 確認済みRCS送信者を含むRCS対応 | RCSおよびSMS（グループにSMS送信者も含まれている場合）。その送信者がMMS対応の場合はMMSも利用可能。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="購読グループ別の利用可能なメッセージタイプ" }

{% alert tip %}
RCS配信に失敗した場合にSMSフォールバックを送信できるよう、RCS購読グループに少なくとも1つのSMS送信者を追加してください。
{% endalert %}

購読グループが両方のプロトコルをサポートしている場合は、**SMS/MMS**または**RCS**を選択します。RCSの場合は、**テキスト**、**メディア**、または**カード**を選択します。

### ステップ3：メッセージを作成する {#step-3-compose-your-message}

メッセージ作成画面のフィールドと制限は、選択したメッセージタイプによって異なります。

{% tabs local %}
{% tab SMSとMMS %}

#### SMSとMMSのフィールドと設定 {#sms-and-mms-fields-and-settings}

| フィールドまたは設定 | 説明 |
| --- | --- |
| **言語** | 言語固有のコンテンツをメッセージに挿入します。 |
| **メッセージ** | Liquid、Connected Content、絵文字を含む最大1,600文字を入力します。メッセージ作成画面でエンコーディング、文字数、課金対象のSMSセグメント数が推定されます。MMSメッセージは、メッセージ本文なしでメディアのみを含めることができます。 |
| **メディア** | MMS対応の購読グループの場合、メディアライブラリまたはURLからPNG、JPEG、またはGIF画像を1つ追加します。画像の代わりにvCardを追加することもできます。 |
| **リンク短縮** | HTTPおよびHTTPS URLを短縮し、エンゲージメントをトラッキングします。レガシーリンク短縮の場合は、ベーシックまたはアドバンストラッキングを選択します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMSとMMSのフィールドと設定" }

SMSメッセージはGSM-7またはUCS-2エンコーディングを使用し、メッセージセグメントごとに課金されます。1文字の変更でエンコーディングが変わり、課金対象のセグメント数が増加する場合があります。エンコーディングルール、セグメントサイズ、セグメント計算ツールについては、[SMSとRCSの課金計算ツール]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator)を参照してください。

![メッセージコピーと推定文字数・セグメント数を表示するSMSメッセージ作成画面。]({% image_buster /assets/img/sms_campaign_compose.png %})

#### MMSメディア仕様 {#mms-media-specifications}

{% multi_lang_include channels/image_specs.md variable_name='sms and mms' %}

ユーザーがデバイスの連絡先に保存できるビジネス情報を送信するには、[連絡先カード]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card)を参照してください。連絡先カードの送信はMMSとして課金されます。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

MMSの利用可否とレンダリングは受信キャリアに依存します。キャリアがMMSを受信できない場合、プロバイダーを通じてメディアがSMS本文内のリンクに変換されます。Google Voiceの限定的なMMSサポートにより配信が不安定になる可能性があるため、Google Voice番号へのMMS送信は避けてください。

ユーザーがインバウンドメディアを送信すると、BrazeはそのURLを[CurrentsのSMSインバウンドイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events)および{% raw %}`{{sms.${inbound_media_urls}}}`{% endraw %}（Liquid）を通じて公開します。

{% endtab %}
{% tab RCS %}

#### RCSメッセージタイプ {#rcs-message-types}

| メッセージタイプ | フィールドと設定 | 制限と動作 |
| --- | --- | --- |
| **テキスト** | 必須のメッセージ本文、オプションの返信候補またはURL開くアクション、オプションのSMSフォールバック、リンク短縮 | メッセージ本文はSMSサービスプロバイダーに応じて最大1,600文字または3,072文字。最大5つの提案を追加可能。 |
| **メディア** | 必須の画像、動画、ドキュメント、またはオーディオ。オプションのメッセージ本文、提案、SMSフォールバック、リンク短縮 | メッセージ本文はプロバイダーに応じて最大1,600文字または3,072文字で、追加のRCSメッセージとして課金されます。最大5つの提案を追加可能。 |
| **カード** | メディアカードまたはテキストのみのカード、タイトル、説明、ボタン、オプションの提案、オプションのSMSフォールバック | タイトルは最大200文字。説明はプロバイダーに応じて最大1,600文字または2,000文字。1〜4つのボタンを追加可能。テキストのみのカードとカード外の提案が利用可能かどうかはプロバイダーのサポートに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="RCSメッセージタイプ、フィールド、制限" }

提案には、ユーザーのテキスト入力にあらかじめ内容を設定する返信候補と、URL開くアクションがあります。各提案には最大25文字のテキストを追加でき、各URL開くアクションには最大2,048文字のURLを追加できます。

任意のRCSメッセージタイプで、**RCSが失敗した場合にSMSを送信**をオンにして、最大1,600文字のフォールバックメッセージを追加できます。選択した購読グループにはSMS送信者が含まれている必要があります。**カード**メッセージの場合、説明内のリンクはクリック可能ではありません。代わりにURL開くボタンを使用してください。

一部のSMSサービスプロバイダーは、独立した**メディア**メッセージやテキストのみのカードをサポートしていません。メッセージ作成画面にはサポートされているRCSメッセージタイプのみが表示されます。**カード**メッセージの場合、リンク短縮はSMSフォールバック内のリンクにのみ適用されます。

RCSメッセージの課金はメッセージタイプとコンテンツに依存します。ベーシック、リッチ、リッチカードの課金ルールについては、[RCSメッセージの課金]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#rcs-message-billing)を参照してください。

#### RCSメディア仕様 {#rcs-media-specifications}

メッセージ作成画面は最大1,000文字のメディアURLを受け付けます。利用可能なフォーマットと最大ファイルサイズはSMSサービスプロバイダーに依存します。

| ファイルタイプ | 仕様 |
| --- | --- |
| すべて | プロバイダーに応じて最大ファイルサイズは16&nbsp;MBまたは100&nbsp;MB。 |
| 画像 | JPEG、JPG、GIF、PNG |
| 動画 | H263、M4V、MP4、MPEG、MPEG-4、WEBM |
| ドキュメント | PDF。**メディア**メッセージでは利用可能ですが、メディアカードでは利用できません。 |
| オーディオ | AAC、MP3、MPEG、MP4、3GPP、OGG。プロバイダーのサポートにより異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="RCSメディア仕様" }

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% endtab %}
{% endtabs %}

#### パーソナライゼーション {#personalization}

[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)、[Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)、絵文字、言語固有のコンテンツを使用してメッセージをパーソナライズします。データが不完全なプロファイルに空白のコンテンツが送信されないよう、Liquidパーソナライゼーションにデフォルト値を含めてください。

プロンプトからメッセージコピーを作成するには、オペレーターの[コピーを生成]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy)を使用します。

右から左に書く言語については、[右から左のメッセージの作成]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)を参照してください。

#### 会話型メッセージワークフローを作成する（RCS） {#create-conversational-message-workflows-rcs}

会話型メッセージワークフローを使用すると、ユーザーに動的に応答し、双方向のメッセージング体験を構築できます。ワークフローを構築するには、キャンバスを作成し、返信候補と[アクションパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)を組み合わせて、ユーザーが選択した返信に基づいてワークフローを誘導します。

1. キャンバスビルダーで、複数の返信候補を含むRCSメッセージステップを作成します。

![返信候補を含むRCSメッセージ作成画面。]({% image_buster /assets/img/rcs/suggested_replies.png %})

{: start="2"}
2. そのメッセージを、各返信候補に対応するアクショングループを持つアクションパスに接続します。
3. 各アクショングループで以下を設定します。
   - トリガーとして**SMSインバウンドメッセージを送信**を選択します。
   - メッセージ本文を対応する返信候補と同じ内容に設定します。

![3つのアクショングループ（各返信候補に1つ）で構成されたアクションパスステップ。]({% image_buster /assets/img/rcs/quick_reply.png %})

{: start="4"}
4. 各アクショングループをRCSメッセージステップに接続し、関連する返信候補に基づいたコンテンツを追加します。
5. フォローアップメッセージに返信候補を追加して、会話型ワークフローを続けます。
6. ワークフローが完成するまでステップ2〜4を繰り返します。

![2つのアクションパスを含む会話型ワークフローを表示するキャンバス。]({% image_buster /assets/img/rcs/full_conversational_workflow.png %})

### ステップ4：リンク短縮を設定する {#step-4-configure-link-shortening}

**リンク短縮**をオンにして、HTTPおよびHTTPS URLを短縮し、SMS、MMS、およびサポートされているRCSリンクのクリックをトラッキングします。ワークスペースで利用可能なバージョンに応じて、ベーシックまたはアドバンストラッキングを選択するか、統合リンク短縮を使用します。

アドバンストラッキングでは、セグメンテーションとリターゲティングのためのユーザーレベルのクリックデータが追加されます。統合リンク短縮では、SMSとRCSの短縮リンクを1つのパーソナライズされたフォーマットに統合します。サポートされているURL、Liquidの動作、テスト要件、カスタムドメイン、リターゲティングについては、[リンク短縮]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening)を参照してください。

Brazeはメッセージ内で最大25件のリンクを短縮します。4,000文字を超えるURLは短縮できず、送信時にメッセージが失敗します。

### ステップ5：メッセージをプレビューしてテストする {#step-5-preview-and-test-your-message}

**テスト**タブに移動して、ユーザーとしてメッセージをプレビューするか、[コンテンツテストグループ]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups)または個別のユーザーにテストSMS、MMS、またはRCSメッセージを送信します。

{% alert tip %}
[SMSセグメント計算ツール]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator)を使用して、メッセージに含まれるセグメント数を推定できます。
{% endalert %}

![メッセージ作成画面のテストタブからのSMSコピーのプレビュー。プロファイルセクションでは名フィールドが「James」に設定されています。プレビューセクションでは、SMSに「Hi James, we appreciate your support!」と表示されています。]({% image_buster /assets/img/sms_campaign_test.png %})

MMSの場合、メディアがメッセージ本文の前後どちらに表示されるかは受信側の電話によって決まります。

{% alert note %}
RCSのレンダリングはユーザーのオペレーティングシステム、デバイスメーカー、キャリア、メッセージングアプリ（例：Google MessagesやApple Messages）によって制御されるため、メッセージの表示は異なる場合があります。Brazeで表示されるプレビューは、エンドユーザーが受信するものと正確に一致しない場合があります。可能な限り実機で最終的なレンダリングを確認してください。iOSデバイスでのRCSレンダリングの詳細については、[RCSメッセージがiOSデバイスで正確にレンダリングされないのはなぜですか？]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#why-doesnt-my-rcs-message-render-accurately-on-ios-devices)を参照してください。リッチカード内のGIFについては、[RCSリッチカード内のGIFがiOSで静止画として表示されるのはなぜですか？]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#why-do-gifs-in-rcs-rich-cards-appear-static-on-ios)を参照してください。
{% endalert %}

詳細については、[テストメッセージを送信する]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=sms%2Fmms%20and%20rcs)を参照してください。

### ステップ6：キャンペーンまたはキャンバスの残りの部分を構築する {#step-6-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab キャンペーン %}

#### 配信スケジュールまたはトリガーを選択する {#choose-a-delivery-schedule-or-trigger}

スケジュールされた時間に、またはアクションやAPIトリガーに応じてメッセージを配信します。スケジュールとトリガーのオプションについては、[キャンペーンのスケジュール]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)を参照してください。

[再適格性]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility)や[フリークエンシーキャップ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping)などの配信コントロールを設定します。アクションベース配信の場合は、キャンペーンの期間と[サイレント時間]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)を設定します。

#### ターゲットユーザーを選択する {#choose-users-to-target}

セグメントとフィルターを選択して[ユーザーをターゲット]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)します。Brazeはメッセージ送信前に正確なセグメントメンバーシップを計算します。

選択した購読グループにより、購読済みユーザーがフィルタリングされます。SMSおよびMMSの受信者には有効な電話番号も必要です。RCSの受信者にはRCS対応デバイスとキャリア接続が必要です。RCS配信に失敗した場合に適格なユーザーに到達するには、SMSフォールバックを使用してください。

{% multi_lang_include audience/target_audiences.md %}

クリックおよびインタラクションターゲティングについては、[ユーザーリターゲティング]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting)を参照してください。

#### コンバージョンイベントを選択する {#choose-conversion-events}

[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)を使用して、ユーザーがキャンペーンを受信した後のアクションを測定します。最大30日間のコンバージョンウィンドウを設定します。

{% endtab %}
{% tab キャンバス %}

キャンバスの残りのセクションを完成させます。エントリスケジュール、オーディエンス設定、送信コントロールについては、[キャンバスを作成する]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)を参照してください。

{% endtab %}
{% endtabs %}

### ステップ7：確認してデプロイする {#step-7-review-and-deploy}

キャンペーンまたはキャンバスの構築が完了したら、詳細を確認し、送信前にメッセージをテストしてください。

ローンチ後は、[SMS、MMS、およびRCSレポート]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting)を使用してメッセージのパフォーマンスを確認します。

## 注意事項 {#things-to-know}

- SMSはメッセージセグメントごとに課金され、MMSは独自のレートで、RCSはメッセージタイプごとに課金されます。送信前に[SMSおよびRCS請求計算ツール]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator)を確認してください。
- MMSは1つの画像またはvCardをサポートしています。キャリアのサポートにより、受信者がメディアを受信するか画像リンクを受信するかが決まります。
- RCSの機能と制限はSMSサービスプロバイダーによって異なります。メッセージ作成画面には、選択した購読グループで利用可能なオプションのみが表示されます。
- RCSの**メディア**メッセージで、事前に録音したボイスメールをオーディオとして送信できます。
- レンダリングやインタラクションの動作は、デバイス、キャリア、オペレーティングシステム、メッセージングアプリによって異なります。