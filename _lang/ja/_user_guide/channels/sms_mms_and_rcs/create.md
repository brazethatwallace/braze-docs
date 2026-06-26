---
nav_title: メッセージを作成する
article_title: SMS、MMS、またはRCSメッセージを作成する
page_order: 1
description: "この記事では、BrazeでSMS、MMS、またはRCSメッセージを作成して送信する方法について説明します。"
page_type: reference
alias: /create_sms_mms_rcs_message/
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS
search_rank: 1
---

# SMS、MMS、またはRCSメッセージを作成する {#create-an-sms-mms-or-rcs-message}

> SMS、MMS、およびRCSのCampaignsは、顧客に直接リーチし、プログラムで会話するのに最適です。Liquidやその他のダイナミックコンテンツを使用して、ユーザーとのパーソナルな体験を作り出し、ブランドとの控えめなユーザー体験を促進・向上させる環境を構築できます。

## ステップ1:メッセージの作成場所を選択する {#step-1-choose-where-to-build-your-message}

メッセージをCampaignで送信するか、Canvasで送信するか迷っていますか？Campaignsは単一のターゲットメッセージングに適しており、Canvasesは複数ステップのユーザージャーニーに適しています。

{% tabs %}
{% tab Campaign %}

1. **メッセージング** > **Campaigns**に移動し、**キャンペーンを作成**を選択します。
2. **SMS/MMS/RCS**を選択するか、複数チャネルをターゲットとするCampaignsの場合は**マルチチャネル**を選択します。
3. Campaignにわかりやすく意味のある名前を付けます。
4. 必要に応じて[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams)と[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)を追加します。
   * タグを使用すると、Campaignsを見つけやすくなり、レポートを作成しやすくなります。たとえば、[レポートビルダー]({{site.baseurl}}/user_guide/analytics/reports/report_builder)を使用する際に、特定のタグでフィルタリングできます。
5. Campaignに必要な数のバリアントを追加して名前を付けます。追加したバリアントごとに、異なるプラットフォーム、メッセージタイプ、レイアウトを選択できます。このトピックの詳細については、[多変量テストとABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)を参照してください。
   * Brazeでは、単一のCampaign内にSMSとRCSの両方のバリアントを含めることができるため、それぞれのパフォーマンスを比較できます。

{% alert tip %}
Campaign内のすべてのメッセージが類似している、または同じコンテンツを持つ場合は、追加のバリアントを追加する前にメッセージを作成してください。その後、**バリアントを追加**ドロップダウンから**バリアントからコピー**を選択できます。
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. Canvasコンポーザーを使用して[Canvasを作成]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)します。
2. Canvasを設定したら、Canvasビルダーで**SMS/MMS/RCS**メッセージステップを追加します。
3. ステップにわかりやすく意味のある名前を付けます。
4. [ステップスケジュール]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types#schedule-delay)を選択し、必要に応じて遅延を指定します。
5. 必要に応じて、このステップのオーディエンスをフィルタリングします。Segmentsを指定し、追加のフィルターを追加することで、このステップの受信者をさらに絞り込むことができます。オーディエンスオプションは、メッセージが送信される時点で遅延後にチェックされます。
6. [進行動作]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases)を選択します。
7. メッセージと組み合わせたい他のメッセージングチャネルを選択します。

{% endtab %}
{% endtabs %}

## ステップ2:サブスクリプショングループを選択する {#step-2-select-a-subscription-group}

適切なユーザーにメッセージを送信するために、[サブスクリプショングループ]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups)を選択します。サブスクリプショングループを選択すると、Brazeは自動的にセグメンテーションフィルターを追加し、購読中のユーザーのみがCampaignを受信するようにします。

選択したサブスクリプショングループによって、コンポーザーで利用可能なメッセージタイプが決まります。

| サブスクリプショングループタイプ | 利用可能なメッセージタイプ |
| --- | --- |
| SMSのみ | SMS |
| MMS対応番号を含むSMS | SMSおよびMMS |
| RCS対応（RCS認証済み送信者あり） | SMS、MMS（有効な場合）、およびRCS |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ2:サブスクリプショングループを選択する" }

{% alert tip %}
Brazeは、RCS送信者を含むすべてのサブスクリプショングループに、フォールバック用のSMSコードを少なくとも1つ含めることを強く推奨します。これにより、RCSメッセージの配信に失敗した場合（たとえば、デバイスの非互換性やキャリアカバレッジの不完全さなど）でも、SMSを通じてメッセージがユーザーに届くようになります。
{% endalert %}

サブスクリプショングループを選択したら、作成するメッセージタイプを選択します。サブスクリプショングループが複数のタイプをサポートしている場合、それらを選択するオプションが表示されます。

![RCSまたはSMS/MMSメッセージタイプから選択するオプション。]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

## ステップ3:メッセージを作成する {#step-3-compose-your-message}

作成体験は、選択したメッセージタイプによって異なります。メッセージタイプのタブを選択してください。

{% tabs local %}
{% tab SMS %}

言語やパーソナライゼーション（Liquid、コネクテッドコンテンツ、絵文字）を必要に応じて使用してメッセージを作成します。超過料金の可能性を減らすために、メッセージコピーの制限を遵守してください。

{% alert important %}
先に進む前に、[SMSメッセージセグメントとコピー制限]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator)のガイドラインをお読みください。SMSメッセージセグメントは、電話キャリアがテキストメッセージを測定するために使用する文字バッチです。メッセージはメッセージセグメントごとに課金されるため、メッセージがどのように分割されるかのニュアンスを理解しておくことをお勧めします。
{% endalert %}

![BrazeのSMSコンポーザー。メッセージは「Hi first_name, we appreciate your support! Why not stop by one of our stores and show them this SMS for an exclusive discount? Reply STOP to stop receiving messages from us.」]({% image_buster /assets/img/sms_campaign_compose.png %})

### 連絡先カードを追加する {#adding-a-contact-card}

SMSメッセージに連絡先カードを追加して、顧客がビジネスや連絡先情報をデバイスの連絡先に追加できるようにすることができます。会社名、電話番号、住所、メール、小さな写真などのプロパティを割り当てることができます。詳細については、[連絡先カード]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card)を参照してください。

{% endtab %}
{% tab MMS %}

MMSメッセージを送信するには、サブスクリプショングループにMMS対応の電話番号が少なくとも1つ必要です。これは、コンポーザーでサブスクリプショングループの横に**MMS**タグが表示されることで確認できます。

メッセージ本文を入力し、[メディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)からPNG、JPEG、またはGIF画像をアップロードするか、画像URLを指定します。メッセージごとにサポートされる画像は1つのみです。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

![MMSメッセージを作成するための作成タブ。]({% image_buster /assets/img/sms/mms_composer.png %}){: style="max-width:80%;"}

### 画像の仕様 {#image-specifications}

| プロパティ | 推奨 |
| --- | --- |
| サイズ | 最大600&nbsp;KB |
| ファイルタイプ | PNG、JPEG、GIF |
{: .reset-td-br-1 .reset-td-br-2 aria-label="画像の仕様" }

### 連絡先カード {#contact-cards}

画像の代わりに[連絡先カード]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card)（vCard）を含めることもできます。

### キャリアの動作 {#carrier-behavior}

MMSメッセージは、テキストのみのSMSとは異なるレートで課金されます。すべてのキャリアがMMSを受け入れられるわけではありません。その場合、MMSはユーザーが選択できる画像リンクに自動的に変換されます。

{% alert note %}
Google Voice番号へのMMS送信は避けてください。Google VoiceのMMSサポートは限定的であり、メッセージ配信が不安定になります。
{% endalert %}

### 受信MMSとパーソナライゼーション {#inbound-mms-and-personalization}

顧客がメディアを含む受信メッセージを送信すると、Brazeは[Currents SMS受信イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events)およびLiquidで{% raw %}`{{sms.${inbound_media_urls}}}`{% endraw %}としてメディアを公開します（たとえば、リターゲティングやフォローアップメッセージで使用）。CanvasでのSMS受信プロパティの使用の詳細については、[メッセージステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)を参照してください。

{% endtab %}
{% tab RCS %}

RCSテキストまたはメディアメッセージの作成方法については、このクイックウォークスルーをご覧ください。

{% multi_lang_include video.html id="3y0iiqqygw" source="wistia" %}

**テキスト**または**メディア**メッセージタイプを選択します。

![テキストまたはメディアメッセージタイプから選択するオプション。]({% image_buster /assets/img/rcs/rcs_text_media.png %}){: style="max-width:65%;"}

{% subtabs %}
{% subtab テキスト %}

RCSテキストメッセージは、テキストをメディアとして重視します。メッセージがリッチ要素なしで160文字以内の場合、基本RCSメッセージとして課金されます。160文字を超えるか、リッチ要素を使用する場合、文字制限3,072のリッチ（シングル）RCSメッセージとして課金されます。

**機能:**

- すべてのSMS機能が含まれ、URLクリックトラッキングの高度なトラッキングが利用可能です。
- **候補返信**: ユーザーが選択してテキスト入力に事前入力できる候補応答を含むボタンです。
- **候補アクション**: ユーザーのデバイスでアクションを開始するボタンです。Brazeは現在、ユーザーをWebページまたはその他のURL識別されたロケーションにリダイレクトするOpenURL候補アクションをサポートしています。

![トレンドファッションスタイルを宣伝するRCSメッセージの3つの候補アクション。]({% image_buster /assets/img/rcs/rcs_suggested_actions.gif %}){: style="max-width:70%;"}

**考慮事項:**

- AndroidとiOSでは表示が異なる場合があります。Androidはリッチメッセージテキスト全体を表示しますが、iOSは3行目以降を切り詰めます。
- メッセージごとに最大5つのボタンを追加できます。これらは候補アクションまたは候補返信のいずれかです。
- 長いテキストブロックや多くのボタンは受信者を圧倒する可能性があります。可能な限りシンプルさを重視してください。
- 場合によっては、長いテキストのみのメッセージをSMSよりもRCSで送信する方がコスト効率が良いことがあります。長いSMSメッセージは複数の課金対象セグメントに分割されますが、RCSメッセージはメッセージごとに課金されるためです。

{% endsubtab %}
{% subtab メディア %}

RCSメディアメッセージでは、SMSでは不可能な魅力的なメディアフォーマット（画像、動画、ドキュメントファイルなど）を使用できます。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

**機能:**

- テキスト、候補返信、候補アクションなど、テキストメッセージタイプで利用可能なすべてをサポートします。
- [メディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)からアップロードされた画像ファイル（JPEG、PNG）。
- メッセージコンポーザーでURLにより追加された動画ファイル（MP4、MPEG、MV4）。
- メッセージコンポーザーでURLにより追加されたドキュメントファイル（PDF）。

![メディアファイルをアップロードするオプションを含むRCSコンポーザー。]({% image_buster /assets/img/rcs/rcs_media_type.png %})

**ファイルの仕様:**

| ファイルタイプ | 仕様 |
| --- | --- |
| すべて | ファイルサイズは100 MBまで。ファイルURLは最大2,048文字。 |
| 画像 | サポートされるフォーマット: JPG、JPEG、GIF |
| 動画 | サポートされるフォーマット: H263、M4V、MP4、MPEG-4、MPEG、WEBM |
| ドキュメント | サポートされるフォーマット: PDF |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ファイルの仕様" }

**考慮事項:**

RCSメッセージの受信体験は、キャリアカバレッジ、モバイルデバイスのハードウェア、オペレーティングシステムによって異なる場合があります。RCSはAndroidデバイスとより自然に統合され、デバイスによって異なる速度と品質で体験がレンダリングされる場合があります。

{% endsubtab %}
{% endsubtabs %}

言語やパーソナライゼーション（[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)、[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)、絵文字）を必要に応じて使用してメッセージを作成します。超過料金の可能性を減らすために、メッセージコピーの制限を遵守してください。

{% alert important %}
先に進む前に、上記の[RCSメッセージタイプのガイドライン](#step-3-compose-your-message)をお読みください。RCSメッセージは[メッセージごとに課金]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator)されるため、各タイプに含められる内容を理解しておくことをお勧めします。
{% endalert %}

{% endtab %}
{% endtabs %}

### ヒント {#tips}

#### Liquidの使用 {#using-liquid}

{% raw %}
Liquidを使用する予定がある場合は、選択したパーソナライゼーションにデフォルト値を含めるようにしてください。ユーザーのプロファイルが不完全な場合に、名前の代わりに空白のプレースホルダー`Hi, !`や意味不明な文が表示されないようにするためです。
{% endraw %}

#### AIコピーの生成 {#generating-ai-copy}

[AIコピーライティングアシスタント]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy)を試してみてください。製品名や説明を入力すると、AIがメッセージングで使用できる人間らしいマーケティングコピーを生成します。

![SMSコンポーザーのメッセージフィールドにある「AIコピーライターを起動」ボタン。]({% image_buster /assets/img/ai_copywriter/ai_copywriter_sms.png %}){: style="max-width:60%"}

#### 右から左へのメッセージの作成 {#creating-right-to-left-messages}

右から左へのメッセージの最終的な外観は、サービスプロバイダーがどのようにレンダリングするかに大きく依存します。右から左へのメッセージをできるだけ正確に表示するためのベストプラクティスについては、[右から左へのメッセージの作成]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)を参照してください。

#### 会話型メッセージワークフローの作成（RCS） {#create-conversational-message-workflows-rcs}

会話型メッセージワークフローでは、ユーザーに動的に応答し、双方向のメッセージング体験を作成できます。ワークフローを構築するには、Canvasを作成し、候補返信と[アクションパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)を組み合わせて、ユーザーが選択した返信に基づいてワークフローを誘導します。

1. Canvasビルダーで、複数の候補返信を含むRCSメッセージステップを作成します。

![候補返信を含むRCSメッセージコンポーザー。]({% image_buster /assets/img/rcs/suggested_replies.png %})

{: start="2"}
2. そのメッセージを、各候補返信に対応するアクショングループを持つアクションパスに接続します。
3. 各アクショングループについて:
   - トリガーとして**SMS受信メッセージを送信**を選択します。
   - メッセージ本文を、対応する候補返信と同じに設定します。

![3つのアクショングループ（各候補返信に1つずつ）で構成されたアクションパスステップ。]({% image_buster /assets/img/rcs/quick_reply.png %})

{: start="4"}
4. 各アクショングループをRCSメッセージステップに接続し、関連する候補返信に基づいたコンテンツを追加します。
5. フォローアップメッセージに候補返信を追加して、会話型ワークフローを続けます。
6. ワークフローが完了するまで、ステップ2〜4を繰り返します。

![2つのアクションパスを含む会話型ワークフローを示すCanvas。]({% image_buster /assets/img/rcs/full_conversational_workflow.png %})

## ステップ4:メッセージをプレビューしてテストする {#step-4-preview-and-test-your-message}

Brazeでは、送信前にメッセージをプレビューしてテストすることを常に推奨しています。**テスト**タブに切り替えて、[コンテンツテストグループ]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups)または個々のユーザーにテストSMS、MMS、またはRCSメッセージを送信するか、Braze内でユーザーとしてメッセージを直接プレビューします。

{% alert tip %}
SMSがいくつのセグメントに分割されるかをテストしたい場合は、[SMSセグメント計算ツール]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator)でコピーの長さをテストしてください。
{% endalert %}

![コンポーザーのテストタブからSMSコピーをプレビュー。プロファイルセクションでは、名フィールドが「James」に設定されています。プレビューセクションでは、SMSに「Hi James, we appreciate your support!」と表示されています。]({% image_buster /assets/img/sms_campaign_test.png %})

{% alert note %}
MMSの場合、アセット（画像とメッセージ本文）の順序はカスタマイズできません。順序は、メッセージを受信する電話に依存します。
{% endalert %}

{% alert note %}
RCSのレンダリングはユーザーのオペレーティングシステム、デバイスメーカー、キャリア、メッセージングアプリ（たとえば、Google MessagesとApple Messages）によって制御されるため、メッセージの外観は異なる場合があります。Brazeに表示されるプレビューは、エンドユーザーが受信するものと正確に一致しない場合があります。可能な限り、実際のデバイスで最終的なレンダリングを検証してください。iOSデバイスでのRCSレンダリングの詳細については、[RCSメッセージがiOSデバイスで正確にレンダリングされないのはなぜですか？]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#why-doesnt-my-rcs-message-render-accurately-on-ios-devices)を参照してください。
{% endalert %}

詳細については、[テストメッセージの送信]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=sms%2Fmms%20and%20rcs)を参照してください。

## ステップ5:CampaignまたはCanvasの残りを構築する {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

次に、Campaignの残りを構築します。メッセージを構築するためのツールの最適な使用方法の詳細については、以下のセクションを参照してください。

### 配信スケジュールまたはトリガーを選択する {#choose-delivery-schedule-or-trigger}

メッセージは、スケジュールされた時間、アクション、またはAPIトリガーに基づいて配信できます。詳細については、[Campaignのスケジュール設定]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)を参照してください。

アクションベースの配信の場合、Campaignの期間と[サイレント時間]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)も設定できます。

このステップでは、ユーザーがCampaignを[再受信可能]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#campaigns)にすることや、[フリークエンシーキャップ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#frequency-capping)ルールを有効にするなどの配信コントロールも指定できます。

### ターゲットユーザーを選択する {#choose-users-to-target}

次に、Segmentsまたはフィルターを選択してオーディエンスを絞り込み、[ユーザーをターゲット]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)します。サブスクリプショングループはすでに選択されているはずで、これによりユーザーが希望するコミュニケーションのレベルやカテゴリで絞り込まれます。

{% multi_lang_include target_audiences.md %}

Segmentsからより大きなオーディエンスを選択し、オプションのフィルターでそのSegmentをさらに絞り込みます。おおよそのSegment人口のプレビューが自動的に表示されます。正確なSegmentメンバーシップは、メッセージが送信される前に常に計算されることに注意してください。

{% alert tip %}
リターゲティングに興味がありますか？詳細については、[ユーザーリターゲティング]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting)を参照してください。
{% endalert %}

### コンバージョンイベントを選択する {#choose-conversion-events}

Brazeでは、Campaignを受信した後にユーザーが特定のアクション（[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)）を実行する頻度を追跡できます。ユーザーが指定されたアクションを実行した場合にコンバージョンがカウントされる最大30日間の時間枠を設定するオプションがあります。

コンバージョンイベントは、Campaignの成功を測定するのに役立ちます。たとえば:

- ジオターゲティングを使用して、ユーザーの購入を最終目標とするメッセージをトリガーする場合、コンバージョンイベントを`Purchase`に設定します。
- ユーザーをアプリに誘導しようとしている場合、コンバージョンイベントを`Starts Session`に設定します。

特定のユースケースに基づいて、カスタムコンバージョンイベントを設定することもできます。

{% endtab %}
{% tab Canvas %}

まだ完了していない場合は、Canvasコンポーネントの残りのセクションを完了してください。Canvasの残りの構築方法、多変量テストとインテリジェントセレクションの実装などの詳細については、Canvasドキュメントの[Canvasを構築する]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-3-build-your-canvas)ステップを参照してください。

{% endtab %}
{% endtabs %}

## ステップ6:確認してデプロイする {#step-6-review-and-deploy}

CampaignまたはCanvasの最後の構築が完了したら、詳細を確認し、テストしてから送信してください。

次に、[SMS、MMS、およびRCSレポート]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting)を確認して、Campaignsの結果にアクセスする方法を学びましょう。

## よくある質問 {#frequently-asked-questions}

### RCSで事前録音のボイスメールを送信できますか？ {#can-i-send-pre-recorded-voicemails-with-rcs}

はい、メディアメッセージを使用してオーディオファイルをサポートできます。