---
nav_title: ユーザープロファイル
article_title: ユーザープロファイル
page_order: 2
page_type: reference
tool:
  - Dashboard
description: "このリファレンス記事では、ダッシュボードでユーザーのプロファイルにアクセスする方法、プロファイルのユースケース、各プロファイルに含まれる内容について説明します。"

---

# ユーザープロファイル {#user-profiles}

> ユーザープロファイルは、特定のユーザーに関する情報を確認するのに最適な方法です。ユーザーに関連するすべての永続データは、そのユーザーのプロファイルに保存されます。

## プロファイルへのアクセス {#access-profiles}

ユーザーのプロファイルにアクセスするには、**Search Users**ページに移動し、以下のいずれかでユーザーを検索します。

- 外部ユーザー ID
- Braze ID
- メール
- 電話番号
- プッシュトークン
- "[user_alias]:[alias_name]" 形式のユーザーエイリアス（例: "amplitude_id:user_123"）

一致するものが見つかった場合、Braze SDKで記録したそのユーザーの情報を表示できます。検索結果に複数のユーザープロファイルが返された場合は、各プロファイルを個別にマージするか、一括ユーザーマージを実行できます。詳しい手順については、[重複ユーザーのマージ]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/)を参照してください。

{% alert note %}
**Search Users**はセグメントやCampaignコンポーザーの**User Lookup**とは異なります。**User Lookup**は特定のユーザーがオーディエンスに一致するかどうかをテストするもので、`external_id`または`braze_id`のみを受け付けます。このページの**Search Users**はメール、電話番号、プッシュトークン、ユーザーエイリアスにも対応しています。詳細については、[セグメントのテスト]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/#testing-segments)を参照してください。
{% endalert %}

{% alert important %}
電話番号で検索する場合、番号は[`E.164`](https://en.wikipedia.org/wiki/e.164)形式に変換されます。電話番号を`E.164`形式に変換できないユーザー（例えば、国コードや市外局番が無効な場合）は、電話番号で検索できません。
{% endalert %}

![「複数のユーザーが検索条件に一致しました」というバナーと、「前へ」「次へ」の2つのボタンが表示された検索結果。]({% image_buster /assets/img_archive/User_Search_Nonunique.png %}){: style="max-width:60%;"}

## ユースケース {#use-cases}

ユーザープロファイルは、ユーザーのエンゲージメント履歴、セグメントメンバーシップ、デバイス、オペレーティングシステムに関する情報に簡単にアクセスできるため、トラブルシューティングやテストに最適なリソースです。

例えば、ユーザーが問題を報告し、使用しているデバイスやオペレーティングシステムが不明な場合、[概要タブ](#overview-tab)を使用してこの情報を確認できます（メールアドレスまたはユーザーIDがわかっている場合）。また、ユーザーの言語を確認することもでき、期待どおりに動作しなかった[多言語Campaign]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/)のトラブルシューティングに役立ちます。

[エンゲージメントタブ](#engagement-tab)を使用して、特定のユーザーがCampaignを受信したかどうかを確認できます。さらに、そのユーザーがCampaignを受信した場合、いつ受信したかを確認できます。また、ユーザーが特定のセグメントに含まれているかどうか、プッシュ、メール、またはその両方にオプトインしているかどうかも確認できます。この情報はトラブルシューティングに役立ちます。例えば、ユーザーが受信するはずのCampaignを受信しなかった場合や、受信するはずでないCampaignを受信した場合に、この情報を確認する必要があります。

## ユーザープロファイルの要素 {#elements-of-user-profile}

ユーザープロファイルには4つの主要セクションがあります。

- **概要:** ユーザーに関する基本情報、セッションデータ、カスタム属性、カスタムイベント、購入、およびユーザーが最後にログインしたデバイス。
- **エンゲージメント:** ユーザーの連絡先設定、受信したCampaign、セグメント、コミュニケーション統計、インストールアトリビューション、ランダムバケット番号に関する情報。
- **メッセージ履歴:** 過去30日間のこのユーザーに関する最近のメッセージング関連イベント。
- **フィーチャーフラグの適格性:** ロールアウト、キャンバスステップ、実験全体で、ユーザーが現在どのフィーチャーフラグに適格であるかを検証します。

### 概要タブ {#overview-tab}

**概要**タブには、ユーザーに関する基本情報と、アプリまたはWebサイトとのインタラクションが表示されます。

| 概要カテゴリ | 内容 |
| --- | --- |
| プロファイル | 性別、年齢層、ロケーション、言語、ロケール、タイムゾーン、誕生日。 |
| セッション概要 | セッション数、最初と最後のセッションの日時、およびどのアプリで行われたか。 |
| カスタム属性 | このユーザーに紐づけられているカスタム属性とその値（階層化カスタム属性を含む）。 |
| 最近のデバイス | ログインしたデバイスの数、各デバイスの詳細、および関連する広告ID（ある場合）。 |
| カスタムイベント | このユーザーが実行したカスタムイベント、実行回数、および各イベントの最終実行日時。 |
| 購入 | このユーザーに紐づけられた生涯収益、最後の購入、購入総数、および各購入のリスト。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="概要タブ" }

このデータの詳細については、[SDKデータ収集]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection/)を参照してください。

![ユーザープロファイルの概要タブ。]({% image_buster /assets/img_archive/user_profile2.png %})

### エンゲージメントタブ {#engagement-tab}

**エンゲージメント**タブには、Brazeを使用して送信したメッセージに対するユーザーのインタラクションに関する情報が表示されます。

| エンゲージメントカテゴリ | 内容 |
| --- | --- |
| 連絡先設定 | メール、SMS、プッシュのサブスクリプションステータス、およびこれら3つのチャネルでこのユーザーが関連付けられている購読グループ。このセクションには、プッシュトークンの変更ログ情報も含まれます。サブスクリプションとオプトインの設定方法については、[メール]({{site.baseurl}}/user_guide/channels/email/subscriptions/)、[SMS]({{site.baseurl}}/sms_rcs_subscription_groups/)、[プッシュ]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states/)を参照してください。 |
| 受信したCampaign | **受信したCampaign**は、チャネル固有の送信および表示タイミングを反映します。ほとんどのチャネルでは、Brazeが配信プロバイダーにメッセージを渡した時点で送信が記録されます（メッセージが最終的に配信されなかった場合でも同様です）。**Content Cards**は異なります。Campaignがここに表示されるのは、ユーザーがアプリ内でカードを表示した後のみです。チャネルごとの詳細については、[受信したCampaignにCampaignが表示されるタイミング](#when-campaigns-appear-in-campaigns-received)を参照してください。<br><br>メッセージが受信、開封、またはクリックされると、Brazeはインタラクションを記録したプロファイルと同じチャネル識別子（例えば、メールの場合は同じメールアドレス、SMSやWhatsAppの場合は同じ電話番号）を共有するすべてのプロファイルのデータを更新します。識別子を共有するユーザーは、元々Campaignの対象でなかった場合や、メッセージが直接送信されなかった場合でも、このフィルターに一致する可能性があります。<br><br>これらのリストは、リターゲティングと履歴に表示される内容を決定する際に、[メッセージングインタラクションデータ]({{site.baseurl}}/api/data_retention/messaging_interaction_data/)（有効期限ルールを含む）を使用します。<br><br>リストからCampaignを選択して表示します。 |
| セグメント | このユーザーが含まれているセグメント。リストからセグメントを選択して表示します。 |
| コミュニケーション統計 | このユーザーが各チャネルから最後にメッセージを受信した日時。 |
| インストールアトリビューション | ユーザーがアプリをインストールした方法と時期に関する情報。詳しくは[ユーザーインストールの理解]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/install_attribution/)を参照してください。 |
| その他 | ユーザーの[ランダムバケット番号]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/)。 |
| 受信したCanvasメッセージ | このユーザーが受信したCanvasメッセージとその受信日時。送信タイミングは**受信したCampaign**と同じチャネルルールに従います。[受信したCampaignにCampaignが表示されるタイミング](#when-campaigns-appear-in-campaigns-received)を参照してください。<br><br>メッセージが受信、開封、またはクリックされると、Brazeはインタラクションを記録したプロファイルと同じチャネル識別子（例えば、メールの場合は同じメールアドレス、SMSやWhatsAppの場合は同じ電話番号）を共有するすべてのプロファイルのデータを更新します。識別子を共有するユーザーは、元々Campaignの対象でなかった場合や、メッセージが直接送信されなかった場合でも、このフィルターに一致する可能性があります。<br><br>リストからメッセージを選択して表示します。 |
| 予測 | このユーザーの[チャーン予測]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/)および[イベント予測]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/)スコア。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="エンゲージメントタブ" }

### 受信したCampaignにCampaignが表示されるタイミング {#when-campaigns-appear-in-campaigns-received}

一般的に、Brazeはメッセージの送信を試みた後に**受信したCampaign**にCampaignを表示します。送信が記録されるために、ユーザーのデバイスや受信トレイへの配信は必要ありません。**受信したCanvasメッセージ**も、各Canvasメッセージタイプに対して同じチャネル固有のルールに従います。

- **メール:** Brazeは、メッセージがメールサービスプロバイダー（ESP）に引き渡された時点で送信を記録します。その引き渡し後、Liquidロジック、レート制限、またはユーザーが到達不能としてマークされたことによるメッセージの中止は行われません。次のイベントは通常、配信またはバウンスです。
- **プッシュ:** Brazeは、メッセージがプッシュプロバイダー（例えば、Apple Push Notification service（APNs）やFirebase Cloud Messaging（FCM））に引き渡された時点で送信を記録します。プロバイダーは通常、即座に配信を試みます。デバイスが利用できない場合（例えば、オフラインの場合）、プロバイダーはメッセージの有効期限が切れるまで再試行する場合があります。
- **アプリ内メッセージ:** Brazeは、Campaignが起動された時点で送信を記録します。
- **Content Cards:** Brazeが*送信済み*イベントを記録するタイミングは、配信タイプと**カード作成**設定によって異なります。Content Cards Campaignがユーザープロファイルの**受信したCampaign**に表示されるのは、ユーザーがアプリ内でカードを表示した後のみです。詳細については、Content Cardsレポートの記事の[送信が記録されるタイミング]({{site.baseurl}}/user_guide/channels/content_cards/reporting/#when-sends-are-logged)および[受信したCampaignとリターゲティングフィルター]({{site.baseurl}}/user_guide/channels/content_cards/reporting/#campaigns-received-and-retargeting-filters)を参照してください。
- **SMS、WhatsApp、webhook:** Brazeは、メッセージがそのチャネルの配信パス（例えば、SMSまたはWhatsAppプロバイダー、またはwebhookエンドポイント）に入った時点で送信を記録します。

{% alert note %}
これらの説明は、**受信したCampaign**に対して送信が記録されるタイミングについてのものです。プロバイダーに到達する前にメッセージを停止できる[メッセージの中止]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/)とは別のものです。
{% endalert %}

![連絡先設定とコミュニケーション統計が表示されたユーザープロファイルのエンゲージメントタブ。]({% image_buster /assets/img_archive/profiles_engagement_tab.png %})

### メッセージ履歴タブ {#messaging-history-tab}

ユーザープロファイルの**メッセージ履歴**タブには、過去30日間の個々のユーザーに関する最近のメッセージング関連イベント（約40件）が表示されます。これらのイベントには、ユーザーに送信されたメッセージ、受信したメッセージ、インタラクションしたメッセージなどが含まれます。

{% alert note %}
このタブのデータは、ユーザーがマージされた後は更新されません。また、API経由で送信されたメッセージに関連するイベント（例えば、[`/messages/send`エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#creating-new-users-with-api-sends)）は、それらの送信でCampaign IDが指定されていない場合、このタブに表示されません。
{% endalert %}

![ユーザーが受信したCampaignとCanvasを表示するメッセージ履歴タブ。]({% image_buster /assets/img_archive/profiles_messaging_history_tab.png %})

#### イベントの表示と理解 {#viewing-and-understanding-events}

**メッセージ履歴**テーブルの各イベントについて、メッセージングチャネル、イベントタイプ、イベント発生のタイムスタンプ、関連するCampaignまたはCanvasメッセージ、およびユーザーのデバイスデータを確認できます。特定のイベントでフィルタリングするには、**Filters**をクリックしてリストからイベントを選択します。

##### メッセージエンゲージメントイベント {#message-engagement-events}

以下のメッセージエンゲージメントイベントは、メール、SMS、プッシュ、アプリ内メッセージ、Content Cards、webhookで利用できます。特定のイベントのトラッキング方法の詳細については、[メッセージエンゲージメントイベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)を参照してください。

| チャネル | 利用可能なエンゲージメントイベント |
| --- | --- |
| メール | バウンス<br>クリック<br>遅延イベント<br>配信<br>スパムとしてマーク<br>開封（[メール開封イベントに関する注意](#note-on-email-open-event)を参照）<br>送信<br>ソフトバウンス<br>配信停止 |
| SMS | キャリア送信<br>配信<br>配信失敗<br>受信<br>拒否<br>送信 |
| プッシュ | バウンス<br>影響を受けた開封<br>iOSフォアグラウンド<br>開封<br>送信 |
| アプリ内メッセージ | クリック<br>インプレッション |
| Content Cards | クリック<br>却下<br>インプレッション<br>送信 |
| Webhook | 送信 |
| WhatsApp | 中止<br>配信<br>失敗<br>フリークエンシーキャップ<br>受信<br>既読<br>送信 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="メッセージエンゲージメントイベント" }

##### メッセージ中止イベント {#message-abort-events}

メッセージ中止イベントは、ユーザーに送信されたメッセージが[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/)または[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content/#aborting-messages)の条件ロジック、またはLiquidレンダリングのタイムアウトにより中止された場合に発生します。

中止イベントは以下のチャネルで利用できます。

- メール
- SMS
- プッシュ
- Webhook

中止イベントは現在、アプリ内メッセージおよびContent Cardsでは利用できません。

##### フリークエンシーキャップイベント {#frequency-cap-events}

フリークエンシーキャップイベントは、ユーザーがメッセージの受信対象となったものの、[フリークエンシーキャップ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#frequency-capping)設定により実際にはメッセージを受信しなかった場合に発生します。フリークエンシーキャップの設定は、**Settings** > **Frequency Capping Rules**からカスタマイズできます。

##### 空白の送信先 {#blank-destinations}

一部のメッセージ送信は、メッセージ履歴で送信先が空白（「—」で表示）で表示される場合があります。これは、Content Cardsやwebhookなどの一部のチャネルでは、メッセージ送信時にデバイスデータを収集しないためです。

Content Cardsの送信は、カードが表示可能になった時点で記録されます。Content Cardsは複数のデバイスで表示できるため、送信時にデバイスデータは記録されません。代わりに、この情報はインプレッション時（カードが実際に表示された時点）に記録されます。Webhookはシステムエンドポイント（デバイスではなく）に送信されるため、デバイスデータは該当しません。

#### メール開封イベントに関する注意 {#note-on-email-open-event}

メール開封のトラッキングは、Brazeを含むあらゆるツールでエラーが発生しやすいものです。さまざまなメールクライアントが提供するプライバシー保護機能により、画像の自動読み込みがブロックされたり、サーバー上で事前に読み込まれたりするため、メール開封イベントは偽陽性と偽陰性の両方の影響を受けやすくなっています。

メール開封の統計は、異なる件名の効果を比較するなど、集計レベルでは有用ですが、個々のユーザーの個々の開封イベントが意味のあるものであると想定すべきではありません。

#### メッセージ履歴タブで特定のフィールドが空白なのはなぜですか？ {#why-are-certain-fields-blank-in-the-message-history-tab}

以下のシナリオでは、ユーザーの**メッセージ履歴**タブで一部のフィールドが表示されない場合があります。

- **Message Sent**のデータが欠落しているイベントは、そのCampaignにメッセージバリエーションがないことを示しています。
- **Campaign/Canvas**と**Message Sent**のデータが欠落しているイベントは、このメッセージが`campaign_id`と`message_variation_id`を指定していないAPI Campaign（APIトリガーCampaignではない）から送信されたことを示しています。これらのフィールドはオプションであり、リクエストボディから省略される場合があります。これらのフィールドが指定されている場合、その情報はメッセージ履歴ログに反映されます。
   - 特定のメッセージがメッセージ履歴に表示されないが、**Campaigns Received**ログに表示される場合、そのユーザーは現在のユーザーとして識別される前にCampaignを受信した可能性があります。既存のプロファイルが孤立した場合、**Campaigns Received**ログは転送されますが、メッセージ履歴は転送されません。
- **Campaign/Canvas**のデータが欠落している場合、手動テストが送信された可能性があります。手動テストは**メッセージ履歴**タブに記録されますが、送信されたCampaignまたはCanvasは記録されません。
- ユーザーがシードグループやその他の内部テストオーディエンスに含まれている場合、**メッセージ履歴**には本番送信と比較してCampaignやCanvasのメタデータが限定的に表示される場合があります。

## 関連記事 {#related-articles}

- [ユーザープロファイルのライフサイクル]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/)
- [POST: 識別子によるユーザープロファイルのエクスポート]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)
- [POST: ユーザーの削除]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)