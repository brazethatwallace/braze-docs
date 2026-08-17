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

> SMS、MMS、およびRCSキャンペーンは、顧客に直接リーチし、プログラムで会話するのに最適です。Liquidやその他のダイナミックコンテンツを使用して、ユーザーとのパーソナルな体験を作り出し、ブランドとの控えめなユーザー体験を促進・向上させる環境を構築できます。

## ステップ 1:メッセージの作成場所を選択する {#step-1-choose-where-to-build-your-message}

メッセージをキャンペーンとキャンバスのどちらで送信すべきかわからない場合、キャンペーンは単一のターゲットメッセージングに適しており、キャンバスはマルチステップのユーザージャーニーに適しています。

{% tabs %}
{% tab キャンペーン %}

1. **メッセージング** > **キャンペーン**に移動し、**キャンペーンを作成**を選択します。
2. **SMS/MMS/RCS**を選択するか、複数のチャネルをターゲットとするキャンペーンの場合は**マルチチャネル**を選択します。
3. キャンペーンにわかりやすく意味のある名前を付けます。
4. 必要に応じて[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams)と[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)を追加します。
   * タグを使用すると、キャンペーンを見つけやすくなり、レポートを作成しやすくなります。たとえば、[レポートビルダー]({{site.baseurl}}/user_guide/analytics/reports/report_builder)を使用する際に、特定のタグでフィルタリングできます。
5. キャンペーンに必要な数のバリアントを追加して名前を付けます。追加したバリアントごとに、異なるプラットフォーム、メッセージタイプ、レイアウトを選択できます。このトピックの詳細については、[多変量テストとABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)を参照してください。
   * Brazeでは、1つのキャンペーン内にSMSとRCSの両方のバリアントを含めることができるため、それぞれのパフォーマンスを比較できます。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似している、または同じコンテンツを持つ場合は、追加のバリアントを追加する前にメッセージを作成してください。その後、**バリアントを追加**ドロップダウンから**バリアントからコピー**を選択できます。
{% endalert %}

{% endtab %}
{% tab キャンバス %}

1. キャンバスコンポーザーを使用して[キャンバスを作成]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)します。
2. キャンバスの設定が完了したら、キャンバスビルダーで**SMS/MMS/RCS**メッセージステップを追加します。
3. ステップにわかりやすく意味のある名前を付けます。
4. [ステップスケジュール]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types)を選択し、必要に応じて遅延を指定します。
5. 必要に応じて、このステップのオーディエンスをフィルタリングします。セグメントを指定し、追加のフィルターを追加することで、このステップの受信者をさらに絞り込むことができます。オーディエンスオプションは、メッセージが送信される時点で遅延後にチェックされます。
6. [昇格動作]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases)を選択します。
7. メッセージと組み合わせたい他のメッセージングチャネルを選択します。

{% endtab %}
{% endtabs %}

## ステップ 2: 購読グループを選択する {#step-2-select-a-subscription-group}

[購読グループ]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups)を選択して、適切なユーザーにメッセージを送信していることを確認します。購読グループを選択すると、Brazeは自動的にセグメンテーションフィルターを追加し、購読済みのユーザーのみがキャンペーンを受信するようにします。

選択した購読グループによって、メッセージ作成画面で利用可能なメッセージタイプが決まります。

| 購読グループタイプ | 利用可能なメッセージタイプ |
| --- | --- |
| SMSのみ | SMS |
| MMS対応番号付きSMS | SMSおよびMMS |
| RCS対応（RCS認証済み送信者付き） | SMS、MMS（有効な場合）、およびRCS |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 2: 購読グループを選択する" }

{% alert tip %}
Brazeは、RCS送信者を含むすべての購読グループに、フォールバック用のSMSコードを少なくとも1つ含めることを強く推奨します。これにより、RCSメッセージの配信に失敗した場合（デバイスの非互換性やキャリアカバレッジの不完全さなど）でも、SMSを通じてメッセージがユーザーに届くようになります。
{% endalert %}

購読グループを選択したら、作成するメッセージタイプを選びます。購読グループが複数のタイプをサポートしている場合、それらの中から選択するオプションが表示されます。

![RCSまたはSMS/MMSメッセージタイプから選択するオプション。]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

## ステップ 3: メッセージを作成する {#step-3-compose-your-message}

メッセージの作成画面は、選択したメッセージタイプによって異なります。メッセージタイプに応じたタブを選択してください。

{% tabs local %}
{% tab SMS %}

言語やパーソナライゼーション（Liquid、Connected Content、絵文字）を必要に応じて使用してメッセージを作成します。超過料金が発生する可能性を減らすために、メッセージのコピー制限を遵守してください。

{% alert important %}
先に進む前に、[SMSメッセージセグメントとコピー制限]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator)のガイドラインをお読みください。SMSメッセージセグメントとは、携帯キャリアがテキストメッセージを測定するために使用する文字のバッチです。メッセージはメッセージセグメントごとに課金されるため、メッセージがどのように分割されるかのニュアンスを理解しておくことをお勧めします。
{% endalert %}

![BrazeのSMS作成画面。メッセージには「Hi first_name, we appreciate your support! Why not stop by one of our stores and show them this SMS for an exclusive discount? Reply STOP to stop receiving messages from us.」と表示されています。]({% image_buster /assets/img/sms_campaign_compose.png %})

### 連絡先カードの追加 {#adding-a-contact-card}

SMSメッセージに連絡先カードを追加して、顧客がビジネスや連絡先情報をデバイスの連絡先に保存できるようにすることができます。会社名、電話番号、住所、メール、小さな写真などのプロパティを割り当てることができます。詳細については、[連絡先カード]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card)を参照してください。

{% endtab %}
{% tab MMS %}

MMSメッセージを送信するには、購読グループに少なくとも1つのMMS対応電話番号が必要です。これは、作成画面の購読グループの横にある**MMS**タグで示されます。

メッセージ本文を入力し、[メディアライブラリー]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)からPNG、JPEG、またはGIF画像をアップロードするか、画像URLを指定します。1メッセージにつき画像は1つのみサポートされています。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

![MMSメッセージを作成するための作成タブ。]({% image_buster /assets/img/sms/mms_composer.png %}){: style="max-width:80%;"}

### 画像の仕様 {#image-specifications}

{% multi_lang_include channels/image_specs.md variable_name='sms and mms' %}

### 連絡先カード {#contact-cards}

画像の代わりに[連絡先カード]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card)（vCard）を含めることもできます。

### キャリアの動作 {#carrier-behavior}

MMSメッセージは、テキストのみのSMSとは異なるレートで課金されます。すべてのキャリアがMMSを受け入れられるわけではありません。その場合、MMSはユーザーが選択できる画像リンクに自動的に変換されます。

{% alert note %}
Google Voice番号へのMMS送信は避けてください。Google VoiceのMMSサポートは限定的であり、メッセージ配信が不安定になります。
{% endalert %}

### 受信MMSとパーソナライゼーション {#inbound-mms-and-personalization}

顧客がメディアを含む受信メッセージを送信すると、Brazeは[CurrentsのSMS受信イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events)およびLiquidで{% raw %}`{{sms.${inbound_media_urls}}}`{% endraw %}としてメディアを公開します（例：リターゲティングやフォローアップメッセージで使用）。キャンバスで受信SMSプロパティを使用する方法の詳細については、[メッセージステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)を参照してください。

{% endtab %}
{% tab RCS %}

RCSテキストまたはメディアメッセージの作成方法については、こちらの簡単なウォークスルーをご覧ください。

{% multi_lang_include video.html id="3y0iiqqygw" source="wistia" %}

**テキスト**または**メディア**メッセージタイプから選択します。

![テキストまたはメディアメッセージタイプを選択するオプション。]({% image_buster /assets/img/rcs/rcs_text_media.png %}){: style="max-width:65%;"}

{% subtabs %}
{% subtab テキスト %}

RCSテキストメッセージは、テキストを媒体として重視します。メッセージがリッチ要素なしで160文字以内の場合、基本RCSメッセージとして課金されます。160文字を超えるか、リッチ要素を使用する場合は、文字数制限3,072文字のリッチ（シングル）RCSメッセージとして課金されます。

**機能：**

- すべてのSMS機能が含まれ、URLクリックトラッキングの高度なトラッキングが利用可能です。
- **候補返信**: ユーザーが選択してテキスト入力に事前入力できる候補の応答を含むボタンです。
- **候補アクション**: ユーザーのデバイスでアクションを開始するボタンです。Brazeは現在、ユーザーをWebページやその他のURLで識別される場所にリダイレクトするOpenURL候補アクションをサポートしています。

![トレンドファッションスタイルを宣伝するRCSメッセージの3つの候補アクション。]({% image_buster /assets/img/rcs/rcs_suggested_actions.gif %}){: style="max-width:70%;"}

**考慮事項：**

- AndroidとiOSでは表示が異なる場合があります。Androidはリッチメッセージのテキスト全体を表示しますが、iOSは3行目以降を省略します。
- 1メッセージにつき最大5つのボタンを追加できます。候補アクションまたは候補返信のいずれかを使用できます。
- 長いテキストブロックや多数のボタンは受信者を圧倒する可能性があります。可能な限りシンプルにしてください。
- 場合によっては、SMSよりもRCSで長いテキストのみのメッセージを送信する方がコスト効率が良いことがあります。長いSMSメッセージは複数の課金対象セグメントに分割されますが、RCSメッセージはメッセージ単位で課金されるためです。

{% endsubtab %}
{% subtab メディア %}

RCSメディアメッセージでは、SMSでは不可能な魅力的なメディア形式（画像、動画、ドキュメントファイルなど）を使用できます。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

**機能：**

- テキスト、候補返信、候補アクションなど、テキストメッセージタイプで利用可能なすべての機能をサポートします。
- [メディアライブラリー]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)からアップロードされた画像ファイル（JPEG、PNG）。
- メッセージ作成画面でURLにより追加された動画ファイル（MP4、MPEG、MV4）。
- メッセージ作成画面でURLにより追加されたドキュメントファイル（PDF）。
- メッセージ作成画面でURLにより追加されたオーディオファイル（例：事前録音されたボイスメール）。

![メディアファイルをアップロードするオプションを備えたRCS作成画面。]({% image_buster /assets/img/rcs/rcs_media_type.png %})

**ファイルの仕様：**

| ファイルタイプ | 仕様 |
| --- | --- |
| すべて | ファイルサイズは100 MBまで。ファイルURLは最大2,048文字です。 |
| 画像 | サポートされる形式：JPG、JPEG、GIF |
| 動画 | サポートされる形式：H263、M4V、MP4、MPEG-4、MPEG、WEBM |
| ドキュメント | サポートされる形式：PDF |
| オーディオ | サポートされる形式：AAC、MP3、MPEG、MP4、3GPP、OGG（SMSサービスプロバイダーにより異なります） |
{: .reset-td-br-1 .reset-td-br-2 aria-label="受信MMSとパーソナライゼーション" }

**考慮事項：**

RCSメッセージの受信体験は、キャリアのカバレッジ、モバイルデバイスのハードウェア、およびオペレーティングシステムによって異なる場合があります。RCSはAndroidデバイスとより自然に統合され、デバイスによって異なる速度と品質で体験がレンダリングされる場合があります。

{% endsubtab %}
{% endsubtabs %}

言語やパーソナライゼーション（[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)、[Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)、絵文字）を必要に応じて使用してメッセージを作成します。超過料金が発生する可能性を減らすために、メッセージのコピー制限を遵守してください。

{% alert important %}
先に進む前に、このセクションの前半にある[RCSメッセージタイプのガイドライン](#step-3-compose-your-message)をお読みください。RCSメッセージは[メッセージ単位で課金]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator)されるため、各タイプに含められる内容を理解しておくことをお勧めします。
{% endalert %}

{% endtab %}
{% endtabs %}

### ヒント {#tips}

#### Liquidの使用 {#using-liquid}

{% raw %}
Liquidを使用する予定がある場合は、選択したパーソナライゼーションにデフォルト値を含めるようにしてください。ユーザーのプロファイルが不完全な場合に、名前の代わりに空白のプレースホルダー `Hi, !` や意味の通らない文が表示されることを防ぐためです。
{% endraw %}

#### AIコピーの生成 {#generating-ai-copy}

[AIコピーライティングアシスタント]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy)を試してみてください。商品名や説明を入力すると、AIがメッセージングに使用できる人間らしいマーケティングコピーを生成します。

![SMS作成画面のメッセージフィールドにある「AIコピーライターを起動」ボタン。]({% image_buster /assets/img/ai_copywriter/ai_copywriter_sms.png %}){: style="max-width:60%"}

#### 右から左へのメッセージの作成 {#creating-right-to-left-messages}

右から左へのメッセージの最終的な表示は、サービスプロバイダーがどのようにレンダリングするかに大きく依存します。できるだけ正確に表示される右から左へのメッセージを作成するためのベストプラクティスについては、[右から左へのメッセージの作成]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)を参照してください。

#### 会話型メッセージワークフローの作成（RCS） {#create-conversational-message-workflows-rcs}

会話型メッセージワークフローでは、ユーザーに動的に応答し、双方向のメッセージング体験を作成できます。ワークフローを構築するには、キャンバスを作成し、候補返信と[アクションパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)を組み合わせて、ユーザーが選択した返信に基づいてワークフローを誘導します。

1. キャンバスビルダーで、複数の候補返信を含むRCSメッセージステップを作成します。

![候補返信を含むRCSメッセージ作成画面。]({% image_buster /assets/img/rcs/suggested_replies.png %})

{: start="2"}
2. そのメッセージを、各候補返信に対応するアクショングループを持つアクションパスに接続します。
3. 各アクショングループについて：
   - トリガーとして**SMS受信メッセージを送信**を選択します。
   - メッセージ本文を、対応する候補返信と同じに設定します。

![3つのアクショングループ（各候補返信に1つずつ）で構成されたアクションパスステップ。]({% image_buster /assets/img/rcs/quick_reply.png %})

{: start="4"}
4. 各アクショングループをRCSメッセージステップに接続し、関連する候補返信に基づいたコンテンツを追加します。
5. フォローアップメッセージに候補返信を追加して、会話型ワークフローを続けます。
6. ワークフローが完成するまで、ステップ2〜4を繰り返します。

![2つのアクションパスを含む会話型ワークフローを示すキャンバス。]({% image_buster /assets/img/rcs/full_conversational_workflow.png %})

## ステップ 4:メッセージをプレビューしてテストする {#step-4-preview-and-test-your-message}

Brazeでは、メッセージを送信する前に必ずプレビューとテストを行うことを推奨しています。**テスト**タブに切り替えて、[コンテンツテストグループ]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups)または個々のユーザーにテストSMS、MMS、またはRCSメッセージを送信するか、Braze内でユーザーとしてメッセージを直接プレビューします。

{% alert tip %}
SMSがいくつのセグメントに分割されるかをテストしたい場合は、[SMSセグメント計算ツール]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator)でコピーの長さをテストしてください。
{% endalert %}

![メッセージ作成画面のテストタブからSMSコピーをプレビューしている画面。プロファイルセクションでは、名フィールドが「James」に設定されています。プレビューセクションでは、SMSに「Hi James, we appreciate your support!」と表示されています。]({% image_buster /assets/img/sms_campaign_test.png %})

{% alert note %}
MMSの場合、アセット（画像とメッセージ本文）の順序はカスタマイズできません。順序はメッセージを受信する電話に依存します。
{% endalert %}

{% alert note %}
RCSのレンダリングはユーザーのオペレーティングシステム、デバイスメーカー、キャリア、およびメッセージングアプリ（例：Google Messages vs. Apple Messages）によって制御されるため、メッセージの表示は異なる場合があります。Brazeに表示されるプレビューは、エンドユーザーが受信するものと正確に一致しない場合があります。可能な限り実際のデバイスで最終的なレンダリングを検証してください。iOSデバイスでのRCSレンダリングの詳細については、[RCSメッセージがiOSデバイスで正確にレンダリングされないのはなぜですか？]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#why-doesnt-my-rcs-message-render-accurately-on-ios-devices)を参照してください。
{% endalert %}

詳細については、[テストメッセージの送信]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=sms%2Fmms%20and%20rcs)を参照してください。

## ステップ5：キャンペーンまたはキャンバスの残りの部分を構築する {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab キャンペーン %}

次に、キャンペーンの残りの部分を構築します。メッセージを構築するためのツールの最適な使用方法について、以下のセクションを参照してください。

### 配信スケジュールまたはトリガーを選択する {#choose-delivery-schedule-or-trigger}

メッセージは、スケジュールされた時間、アクション、またはAPIトリガーに基づいて配信できます。詳細については、[キャンペーンのスケジュール設定]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)を参照してください。

アクションベースの配信では、キャンペーンの期間と[サイレント時間]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)を設定することもできます。

このステップでは、ユーザーがキャンペーンを[再度受け取れる]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility)ようにしたり、[フリークエンシーキャップ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping)ルールを有効にしたりするなど、配信コントロールを指定することもできます。

### ターゲットユーザーを選択する {#choose-users-to-target}

次に、セグメントまたはフィルターを選択してオーディエンスを絞り込み、[ユーザーをターゲット]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)にします。購読グループはすでに選択されているはずです。これにより、ユーザーが希望するコミュニケーションのレベルやカテゴリーで絞り込まれます。

{% multi_lang_include audience/target_audiences.md %}

セグメントからより大きなオーディエンスを選択し、オプションのフィルターでそのセグメントをさらに絞り込みます。おおよそのセグメント人口のプレビューが自動的に表示されます。正確なセグメントメンバーシップは、メッセージが送信される前に常に計算されることに留意してください。

{% alert tip %}
リターゲティングに興味がありますか？詳細については、[ユーザーリターゲティング]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting)を参照してください。
{% endalert %}

### コンバージョンイベントを選択する {#choose-conversion-events}

Brazeでは、キャンペーンを受信した後にユーザーが特定のアクション（[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)）を実行する頻度をトラッキングできます。ユーザーが指定されたアクションを実行した場合にコンバージョンがカウントされる最大30日間のウィンドウを設定するオプションがあります。

コンバージョンイベントは、キャンペーンの成功を測定するのに役立ちます。例：

- ジオターゲティングを使用して、ユーザーが購入するという最終目標を持つメッセージをトリガーする場合、コンバージョンイベントを`Purchase`に設定します。
- ユーザーをアプリに誘導しようとしている場合、コンバージョンイベントを`Starts Session`に設定します。

特定のユースケースに基づいてカスタムコンバージョンイベントを設定することもできます。

{% endtab %}
{% tab キャンバス %}

まだ完了していない場合は、キャンバスコンポーネントの残りのセクションを完了してください。キャンバスの残りの部分の構築方法、多変量テストやインテリジェントセレクションの実装方法などの詳細については、キャンバスドキュメントの[キャンバスを構築する]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas)ステップを参照してください。

{% endtab %}
{% endtabs %}

## ステップ 6:確認してデプロイする {#step-6-review-and-deploy}

キャンペーンまたはキャンバスの最後の構築が完了したら、詳細を確認し、テストしてから送信します。

次に、[SMS、MMS、RCSレポート]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting)を参照して、キャンペーンの結果にアクセスする方法を確認してください。

## よくある質問 {#frequently-asked-questions}

### RCSで事前録音のボイスメールを送信できますか？ {#can-i-send-pre-recorded-voicemails-with-rcs}

はい、メディアメッセージを使用してオーディオファイルをサポートできます。