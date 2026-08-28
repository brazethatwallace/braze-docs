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

始める前に、以下の準備が整っていることを確認してください。

| 要件 | 説明 |
| --- | --- |
| 送信者設定 | [送信者設定]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup)を完了します。MMSを送信するには、購読グループにMMS対応の電話番号が必要です。RCSを送信するには、[RCS設定]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup)を完了し、認証済みのRCS送信者を追加してください。 |
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
2. **SMS/MMS/RCS**を選択するか、複数のチャネルをターゲットとするキャンペーンの場合は**マルチチャネルキャンペーン**を選択します。
3. キャンペーンにわかりやすく意味のある名前を付けます。
4. 必要に応じて[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams)と[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)を追加します。
  - タグを使用すると、キャンペーンの検索やレポートでの活用が容易になります。
5. キャンペーンのバリアントを追加して名前を付けます。同じキャンペーンにSMS/MMSとRCSのバリアントを含めることができます。詳細については、[多変量テストとABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)を参照してください。

{% alert tip %}
キャンペーンのバリアントに類似したコンテンツが含まれる場合は、バリアントを追加する前に最初のメッセージを作成してください。その後、**バリアントを追加**ドロップダウンから**バリアントからコピー**を選択できます。
{% endalert %}

{% endtab %}
{% tab キャンバス %}

{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

### ステップ2：購読グループとメッセージタイプを選択する {#step-2-select-a-subscription-group-and-message-type}

このメッセージの送信者を含む**購読グループ**を選択します。Brazeは選択されたグループを使用して、到達可能なオーディエンスの計算と送信時の適格性を判定します。

選択した購読グループにより、メッセージ作成画面で利用可能なメッセージタイプが決まります。

| 購読グループのタイプ | 利用可能なメッセージタイプ |
| --- | --- |
| SMSのみ | SMS |
| MMS対応番号を含むSMS | SMSおよびMMS |
| 認証済みRCS送信者によるRCS対応 | RCS、およびグループにSMS送信者も含まれている場合はSMS。その送信者がMMS対応の場合はMMSも利用可能。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="購読グループ別の利用可能なメッセージタイプ" }

{% alert tip %}
RCS配信が失敗した場合にSMSフォールバックを送信できるよう、RCS購読グループに少なくとも1つのSMS送信者を追加してください。
{% endalert %}

購読グループが両方のプロトコルをサポートしている場合は、**SMS/MMS**または**RCS**を選択します。RCSの場合は、**テキスト**、**メディア**、または**カード**を選択します。

### ステップ3：メッセージを作成する {#step-3-compose-your-message}

メッセージ作成画面のフィールドと制限は、選択したメッセージタイプによって異なります。

{% tabs local %}
{% tab SMSとMMS %}

#### SMSとMMSのフィールドと設定 {#sms-and-mms-fields-and-settings}

| フィールドまたは設定 | 説明 |
| --- | --- |
| **言語** | メッセージに言語固有のコンテンツを挿入します。 |
| **メッセージ** | Liquid、Connected Content、絵文字を含めて最大1,600文字を入力します。メッセージ作成画面はエンコーディング、文字数、課金対象のSMSセグメント数を推定します。MMSメッセージにはメッセージ本文なしでメディアを含めることができます。 |
| **メディア** | MMS対応の購読グループの場合、メディアライブラリまたはURLからPNG、JPEG、GIF画像を1つ追加します。画像の代わりにvCardを追加することもできます。 |
| **リンク短縮** | HTTPおよびHTTPSのURLを短縮し、エンゲージメントをトラッキングします。レガシーリンク短縮の場合は、基本または高度なトラッキングを選択します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMSとMMSのフィールドと設定" }

SMSメッセージはGSM-7またはUCS-2エンコーディングを使用し、メッセージセグメントごとに課金されます。1文字でもエンコーディングが変わり、課金対象のセグメント数が増加する可能性があります。エンコーディングルール、セグメントサイズ、セグメント計算機については、[SMSおよびRCS課金計算機]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator)を参照してください。

![メッセージコピーとその推定文字数およびセグメント数を表示するSMSメッセージ作成画面。]({% image_buster /assets/img/sms_campaign_compose.png %})

#### MMSメディア仕様 {#mms-media-specifications}

{% multi_lang_include channels/image_specs.md variable_name='sms and mms' %}

ユーザーがデバイスの連絡先に保存できるビジネス情報を送信するには、[連絡先カード]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card)を参照してください。連絡先カードの送信はMMSとして課金されます。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

MMSの可用性とレンダリングは受信キャリアに依存します。キャリアがMMSを受け入れられない場合、メディアはプロバイダーによってSMS本文内のリンクに変換されます。Google Voice番号へのMMS送信は、MMSサポートが限定的であるため配信が不安定になる可能性があるので避けてください。

ユーザーが受信メディアを送信すると、BrazeはそのURLを[Currents SMSインバウンドイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events)および{% raw %}`{{sms.${inbound_media_urls}}}`{% endraw %}（Liquid内）で公開します。

{% endtab %}
{% tab RCS %}

#### RCSメッセージタイプ {#rcs-message-types}

| メッセージタイプ | フィールドと設定 | 制限と動作 |
| --- | --- | --- |
| **テキスト** | 必須のメッセージ本文、オプションの候補返信またはURL開くアクション、オプションのSMSフォールバック、リンク短縮 | メッセージ本文にはSMSサービスプロバイダーに応じて最大1,600文字または3,072文字を含めることができます。最大5つの候補を追加できます。 |
| **メディア** | 必須の画像、動画、ドキュメント、または音声、オプションのメッセージ本文、オプションの候補、SMSフォールバック、リンク短縮 | メッセージ本文にはプロバイダーに応じて最大1,600文字または3,072文字を含めることができ、追加のRCSメッセージとして課金されます。最大5つの候補を追加できます。 |
| **カード** | メディアカードまたはテキストのみのカード、タイトル、説明、ボタン、オプションの候補、オプションのSMSフォールバック | タイトルは最大200文字です。説明はプロバイダーに応じて最大1,600文字または2,000文字です。1～4個のボタンを追加できます。テキストのみのカードおよびカード外の候補が利用可能かどうかはプロバイダーのサポートによります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="RCSメッセージタイプ、フィールド、制限" }

候補には、ユーザーのテキスト入力を事前設定する候補返信と、URL開くアクションがあります。各候補に最大25文字のテキスト、各URL開くアクションに最大2,048文字のURLを追加できます。

任意のRCSメッセージタイプで、**RCSが失敗した場合にSMSを送信**をオンにすると、最大1,600文字のフォールバックメッセージを追加できます。選択した購読グループにはSMS送信者が含まれている必要があります。**カード**メッセージの場合、説明内のリンクはクリックできないため、代わりにURL開くボタンを使用してください。

一部のSMSサービスプロバイダーは、単独の**メディア**メッセージやテキストのみのカードをサポートしていません。メッセージ作成画面には、サポートされているRCSメッセージタイプのみが表示されます。**カード**メッセージの場合、リンク短縮はSMSフォールバック内のリンクにのみ適用されます。

RCSメッセージの課金はメッセージタイプとコンテンツに依存します。基本、リッチ、リッチカードの課金ルールについては、[RCSメッセージ課金]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#rcs-message-billing)を参照してください。

#### RCSメディア仕様 {#rcs-media-specifications}

メッセージ作成画面では最大1,000文字のメディアURLを受け付けます。利用可能なフォーマットと最大ファイルサイズはSMSサービスプロバイダーに依存します。

| ファイルタイプ | 仕様 |
| --- | --- |
| すべて | 最大ファイルサイズはプロバイダーに応じて16&nbsp;MBまたは100&nbsp;MBです。 |
| 画像 | JPEG、JPG、GIF、PNG |
| 動画 | H263、M4V、MP4、MPEG、MPEG-4、WEBM |
| ドキュメント | PDF。**メディア**メッセージで利用可能ですが、メディアカードでは利用できません。 |
| 音声 | AAC、MP3、MPEG、MP4、3GPP、OGG。プロバイダーのサポートは異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="RCSメディア仕様" }

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% endtab %}
{% endtabs %}

#### パーソナライゼーション {#personalization}

[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)、[Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)、絵文字、言語固有のコンテンツを使用してメッセージをパーソナライズします。データが不完全なプロファイルが空のコンテンツを受け取らないよう、Liquidパーソナライゼーションにデフォルト値を含めてください。

プロンプトからメッセージコピーを作成するには、オペレーターの[コピーを生成]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy)を使用します。

右から左に記述される言語については、[右から左へのメッセージの作成]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)を参照してください。

#### 会話型メッセージワークフローの作成（RCS） {#create-conversational-message-workflows-rcs}

会話型メッセージワークフローを使用すると、ユーザーにダイナミックに応答し、双方向のメッセージング体験を作り出すことができます。ワークフローを構築するには、キャンバスを作成し、候補返信と[アクションパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)を組み合わせて、ユーザーが選択した返信に基づいてワークフローを分岐させます。

1. キャンバスビルダーで、複数の候補返信を含むRCSメッセージステップを作成します。

![候補返信を含むRCSメッセージ作成画面。]({% image_buster /assets/img/rcs/suggested_replies.png %})

{: start="2"}
2. そのメッセージを、各候補返信に対応するアクショングループを持つアクションパスに接続します。
3. 各アクショングループで以下を行います。
   - トリガーとして**SMSインバウンドメッセージを送信**を選択します。
   - メッセージ本文を対応する候補返信と同じに設定します。

![3つのアクショングループ（各候補返信に1つずつ）が設定されたアクションパスステップ。]({% image_buster /assets/img/rcs/quick_reply.png %})

{: start="4"}
4. 各アクショングループをRCSメッセージステップに接続し、関連する候補返信に基づいたコンテンツを追加します。
5. フォローアップメッセージに候補返信を追加して、会話型ワークフローを継続します。
6. ワークフローが完成するまで、ステップ2～4を繰り返します。

![2つのアクションパスを持つ会話型ワークフローを表示するキャンバス。]({% image_buster /assets/img/rcs/full_conversational_workflow.png %})

### ステップ4：リンク短縮を設定する {#step-4-configure-link-shortening}

**リンク短縮**をオンにすると、HTTPおよびHTTPSのURLを短縮し、SMS、MMS、サポートされているRCSリンクのクリックをトラッキングできます。ワークスペースで利用可能なバージョンに応じて、基本または高度なトラッキングを選択するか、統合リンク短縮を使用します。

高度なトラッキングにより、セグメンテーションやリターゲティング用のユーザーレベルのクリックデータが追加されます。統合リンク短縮は、SMSとRCSの短縮リンクを1つのパーソナライズされた形式に統合します。サポートされているURL、Liquidの動作、テスト要件、カスタムドメイン、リターゲティングについては、[リンク短縮]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening)を参照してください。

Brazeは1つのメッセージで最大25個のリンクを短縮します。4,000文字を超えるURLは短縮できず、送信時にメッセージが失敗する原因となります。

### ステップ5：メッセージをプレビューしてテストする {#step-5-preview-and-test-your-message}

**テスト**タブに移動して、ユーザーとしてメッセージをプレビューするか、[コンテンツテストグループ]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups)または個別のユーザーにテストSMS、MMS、またはRCSメッセージを送信します。

{% alert tip %}
[SMSセグメント計算機]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator)を使用して、メッセージに含まれるセグメント数を推定します。
{% endalert %}

![メッセージ作成画面のテストタブからSMSコピーをプレビュー。プロファイルセクションの名フィールドは「James」に設定されています。プレビューセクションでは、SMSに「Hi James, we appreciate your support!」と表示されています。]({% image_buster /assets/img/sms_campaign_test.png %})

MMSの場合、メディアがメッセージ本文の前に表示されるか後に表示されるかは受信側の電話によって決まります。

RCSの場合、オペレーティングシステム、デバイスメーカー、キャリア、メッセージングアプリがレンダリングを制御します。Brazeのプレビューは受信したメッセージと異なる場合があるため、実機でテストしてください。詳細については、[iOSデバイスでRCSメッセージが正確にレンダリングされないのはなぜですか？]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#why-doesnt-my-rcs-message-render-accurately-on-ios-devices)を参照してください。

詳細については、[テストメッセージを送信する]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=sms%2Fmms%20and%20rcs)を参照してください。

### ステップ6：キャンペーンまたはキャンバスの残りを構築する {#step-6-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab キャンペーン %}

#### 配信スケジュールまたはトリガーを選択する {#choose-a-delivery-schedule-or-trigger}

スケジュールされた時間にメッセージを配信するか、アクションまたはAPIトリガーに応じて配信します。スケジューリングとトリガーのオプションについては、[キャンペーンのスケジュール]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)を参照してください。

[再適格性]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility)や[フリークエンシーキャップ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping)などの配信コントロールを設定します。アクションベースの配信の場合は、キャンペーンの期間と[静寂時間]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)を設定します。

#### ターゲットユーザーを選択する {#choose-users-to-target}

セグメントとフィルターを選択して[ユーザーをターゲット]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)します。Brazeはメッセージ送信前に正確なセグメントメンバーシップを計算します。

選択した購読グループは購読済みユーザーでフィルタリングされます。SMSおよびMMSの受信者には有効な電話番号も必要です。RCSの受信者にはRCS対応のデバイスとキャリア接続が必要です。RCS配信が失敗した場合に適格なユーザーに到達するには、SMSフォールバックを使用してください。

{% multi_lang_include audience/target_audiences.md %}

クリックおよびインタラクションターゲティングについては、[ユーザーリターゲティング]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting)を参照してください。

#### コンバージョンイベントを選択する {#choose-conversion-events}

[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)を使用して、ユーザーがキャンペーンを受信した後のアクションを測定します。コンバージョンウィンドウは最大30日間に設定できます。

{% endtab %}
{% tab キャンバス %}

キャンバスの残りのセクションを完成させます。エントリスケジュール、オーディエンス設定、送信コントロールについては、[キャンバスを作成する]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)を参照してください。

{% endtab %}
{% endtabs %}

### ステップ7：レビューしてデプロイする {#step-7-review-and-deploy}

キャンペーンまたはキャンバスの構築が完了したら、詳細を確認し、送信前にメッセージをテストしてください。

ローンチ後は、[SMS、MMS、RCSレポート]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting)を使用してメッセージのパフォーマンスを確認します。

## 知っておくべきこと {#things-to-know}

- SMSはメッセージセグメント単位で課金され、MMSは独自の料金が適用され、RCSはメッセージタイプごとに課金されます。送信前に[SMSおよびRCS請求計算ツール]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator)を確認してください。
- MMSは1つの画像またはvCardをサポートします。受信者がメディアを受信するか画像リンクを受信するかは、キャリアのサポート状況によって異なります。
- RCSの機能と制限はSMSサービスプロバイダーによって異なります。メッセージ作成画面には、選択した購読グループで利用可能なオプションのみが表示されます。
- RCSの**メディア**メッセージで、事前に録音したボイスメールを音声として送信できます。
- レンダリングやインタラクションの動作は、デバイス、キャリア、オペレーティングシステム、メッセージングアプリによって異なります。