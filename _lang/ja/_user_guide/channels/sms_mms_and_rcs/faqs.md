---
nav_title: FAQ
article_title: SMS、MMS、RCS に関する FAQ
page_order: 30
description: "この記事では、SMS、MMS、RCS メッセージングに関するよくある質問に回答します。"
page_type: FAQ
alias: /sms_mms_rcs_faq/
channel:
  - SMS
  - MMS
  - RCS
---

# よくある質問 {#frequently-asked-questions}

> この記事では、SMS、MMS、RCS メッセージングに関するよくある質問に回答します。

## 一般 {#general}

### SMS APIオブジェクトの`app_id`とは何ですか？ {#what-is-an-app_id-in-the-sms-api-object}

アプリ識別子APIキー（`app_id`）は、ワークスペース内の特定のアプリにアクティビティを関連付けるパラメーターです。ワークスペース内のどのアプリとやり取りしているかを指定します。たとえば、iOSアプリ用の`app_id`、Androidアプリ用の`app_id`、Web統合用の`app_id`があります。

SMSの場合、API経由でSMSメッセージを送信する際（`/messages/send`エンドポイントなど）に`app_id`パラメーターが必要です。これは、ワークスペース内のどのアプリがSMSアクティビティまたはAPI呼び出しに関連付けられているかを指定します。SMSメッセージングのために、ワークスペースで設定されたアプリの有効な`app_id`であれば、ユーザーのプロファイルにその特定のアプリがあるかどうかに関係なく使用できます。

`app_id`は、**設定** > **アプリ設定**に移動し、**識別**セクションを見つけることで確認できます。

### 複数のユーザーが同じ電話番号を持っている場合はどうなりますか？ {#what-happens-if-multiple-users-have-the-same-phone-number}

同じ電話番号（SMSが有効）を共有する複数のユーザープロファイルが、受信SMSのイベントによってトリガーされるアクションベースのキャンペーンまたはキャンバスコンポーネントに同時に適格である場合、Brazeはキャンバスコンポーネントレベルでユーザーの重複を排除します。これにより、複数のユーザーが同じ電話番号を共有していても、キャンバスコンポーネントに対して複数のSMSテキストを受信することを防ぎます。

{% alert note %}
Brazeは、スケジュールされたキャンバスでは電話番号による重複排除を行いません。
{% endalert %}

Brazeは以下のフローを使用して受信者プロファイルを決定します。
- どのプロファイルが最も最近SMSを受信したかを確認します（最大7日前まで）。存在する場合、そのユーザーに送信します。
- どちらも7日前までにSMSを受信していない場合、電話番号と一致する「phone」のユーザーエイリアスを持つユーザーに送信します。
- どちらも存在しない場合、利用可能なプロファイルの中からランダムなプロファイルに送信します。

共有電話番号から「START」または「STOP」キーワードを受信した場合、すべてのユーザープロファイルがSMSの購読および有効化、または購読解除されます。これはAPIのステータス変更にも適用されます。たとえば、異なるexternal IDを持つ複数のプロファイルが同じ電話番号を持っている場合、APIを通じた購読グループのステータス変更は、1つのexternal IDのみが指定されていても、その電話番号を持つすべてのプロファイルを更新します。

{% alert important %}
ユーザーをキャンバスに段階的に投入し、各キャンバスコンポーネントに異なるスケジュール時間を設定している場合、同じメールアドレスまたは電話番号を持つユーザーに重複メッセージを送信する可能性があります。
{% endalert %}

不必要に大規模な更新を防ぐため、購読の更新が行われた際に、識別子を共有するユーザープロファイルは最大100件まで更新されます。同じ電話番号を共有するユーザープロファイルが100件を超える場合、すべてのプロファイルが更新されるわけではありません。

### 特定のソースからのSMS購読の急増が見られるのはなぜですか？ {#why-do-i-see-a-spike-in-sms-subscriptions-from-a-specific-source}

購読数の予想外に大きな増加が見られる場合、特にCurrentsを通じて[`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)エンドポイントからのデータを確認している場合、これはユーザープロファイルの重複が原因である可能性があります。

`/subscription/status/set`エンドポイントに電話番号のみ（`external_id`なし）でリクエストが行われた場合、Brazeはその電話番号を共有するすべてのユーザープロファイルを更新します。ワークスペースに重複プロファイルがある場合、実際には1つの電話番号のみが変更されたにもかかわらず、購読ステータスを更新したユーザー数が膨らみます。

Currentsからデータを取得する際に購読データをより正確に分析するには、すべての購読ステータス変更イベントをカウントするのではなく、一意の電話番号をカウントするようにクエリを更新してください。

### 共有ショートコードとは何ですか？ {#what-are-shared-short-codes}

共有ショートコードでは、どのビジネスや組織が送信したかに関係なく、すべてのテキストメッセージが消費者のモバイルデバイスに同じ5〜6桁の電話番号から届きます。共有ショートコードは比較的低コストですぐに利用できますが、ビジネス専用のショートコードを持つことはできません。

このアプローチのデメリットには以下が含まれます。

- 顧客が、あなたと共有ショートコードを持つ別のビジネスのメッセージをオプトアウトした場合、あなたのメッセージもオプトアウトされます。
- 1つのビジネスがルールに違反した場合、すべてのビジネスのメッセージが停止されます。
- セキュリティの問題

## 請求と料金 {#billing-and-pricing}

### SMSの請求はどのように行われますか？ {#how-will-i-be-billed-for-sms}

ショートコードとロングコードの料金に加えて、Brazeはさまざまな国向けにSMSメッセージの割り当てを提供しています。つまり、お客様と協力して、さまざまな国向けに一定数のメッセージセグメントを設定し、それを使用してSMSキャンペーンを送信します。請求は、国ごとに送信されたメッセージセグメント数に基づいて行われます。メッセージセグメントの計算方法の詳細については、[メッセージセグメントとコピー制限]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator)ガイドを参照してください。上限に近づいている場合は、アカウントマネージャーから連絡があり、関連するレポートを提供して最新情報をお届けします。超過料金に関するその他のご質問については、Brazeの担当者にお問い合わせください。

### MMSとSMSの料金は異なりますか？ {#does-mms-and-sms-pricing-differ}

MMSとSMSはコストが異なり、ボリュームに基づいて別々に課金されます。料金情報については、Brazeオンボーディングチームにお問い合わせください。

### 超過料金を回避するにはどうすればよいですか？ {#how-can-i-avoid-overages}

超過料金が一切発生しないことを保証することはできませんが、割り当て上限を超える可能性を減らすために、以下の予防策を講じることができます。

- SMSの文字数に注意してください。意図せず複数のセグメントを送信すると、超過料金が発生する可能性があります。詳細については、[セグメントの内訳]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator)を参照してください。
- LiquidやConnected Contentを考慮して、SMSの文字数を慎重に計算してください。ダッシュボードのBraze SMSコンポーザーは、これらの機能の使用を推定したり考慮したりしません。
- メッセージが使用するエンコーディングの種類を考慮してください。メッセージがGSM-7エンコーディングを使用している場合、通常1メッセージセグメントあたり160文字と見積もることができます（GSM-7拡張テーブルの文字を使用する場合はそれより少なくなります）。メッセージが[UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set)エンコーディングを使用している場合、通常1メッセージセグメントあたり67文字と見積もることができます。
- テスト、テスト、そしてテストです！特にLiquidやConnected Contentを使用する場合は、送信前に必ずSMSメッセージをテストしてください。

### 固定電話にメッセージが送信された場合、SMS送信数にカウントされますか？ {#if-a-message-is-sent-to-a-landline-will-the-message-still-count-toward-my-sms-send-count}

米国、カナダ、英国の場合：
- SMSが固定電話に送信された場合、**未配信**としてマークされます。請求の動作はSMSサービスプロバイダーによって異なります。Twilioの場合、配信の試行に対しても課金されるため、メッセージログで**送信済み**、**配信済み**、または**未配信**としてマークされたメッセージは請求対象となります。
- 英国では、一部のキャリアがSMSをボイスメールに変換してメッセージを配信します。

その他の国の場合：
- Twilioの場合、エラーが返され、試行されたSMSメッセージに対しては課金されません。

### メッセージが160文字（GSM-7）または67文字（UCS-2）未満なのに、追加のメッセージセグメントが課金される可能性があるとBrazeダッシュボードで警告が表示されるのはなぜですか？ {#why-is-the-braze-dashboard-warning-me-i-may-be-charged-for-additional-message-segments-when-my-message-is-under-160-gsm-7-or-67-ucs-2-characters}

メッセージにLiquidパーソナライゼーションが含まれている場合、追加のメッセージセグメントが課金される可能性があります。コンテンツブロックのテンプレート処理は、メッセージの送信準備が整うまで行われません。コンテンツブロックを含むSMSを編集する際、Brazeはコンテンツブロックの内容を把握できませんが、おおよその見積もりを提供します。テストペインを使用してメッセージをプレビューし、期待される内容をより正確に把握することをお勧めします。

## 送信と配信性 {#sending-and-deliverability}

### SMSにリンクを含めることはできますか？ {#can-you-include-links-in-an-sms}

SMSキャンペーンには任意のリンクを含めることができます。ただし、いくつかの注意点があります。

- リンクはSMSの160文字制限の大部分を占める可能性があります。リンクとテキストを含めると、1通ではなく2通のSMSメッセージになる場合があります。
- 企業はリンクの文字数への影響を抑えるためにリンク短縮サービスを使用することがよくあります。ただし、短縮リンクをロングコードで送信すると、キャリアがリンクリダイレクトを疑い、メッセージをブロックまたは拒否する可能性があります。
- [ショートコード]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup)を使用することが、リンクを含める際に最も信頼性の高い番号タイプです。

Brazeには独自のリンク短縮機能もあり、リンクを自動的に短縮し、クリックスルー分析を提供します。詳細については、[リンク短縮]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening)を参照してください。

### SMSメッセージの送信速度をレート制限する必要がありますか？ {#do-you-need-to-rate-limit-how-fast-you-send-sms-messages}

デフォルトの同時実行レートとスループットでは、ショートコードあたり1時間に約360,000メッセージを送信できます。追加のスループットには追加のショートコードが必要です。

### SMSのURLをどのように許可リストに登録しますか？ {#how-do-you-allowlist-urls-for-sms}

特定の国（スウェーデンや北欧諸国など）のユーザーにURLを含むSMSメッセージを送信する前に、これらのURLをキャリアに登録する必要があります。Brazeカスタマーサービスマネージャーにお問い合わせください。このプロセスには約5日かかります。

### SMSのスパム検出を回避するためのベストプラクティスは何ですか？ {#what-are-the-best-sending-practices-to-avoid-spam-detection-for-sms}

1. オプトインとオプトアウトの手順が明確であることを確認してください。
2. あなた（ブランド）が顧客との関係を持っていることを確認してください。
3. コンテンツがその関係性と、ユーザーが受信をオプトインした内容に関連していることを確認してください。

スパム検出の回避に関する詳細なガイドラインについては、[SMSの法律と規制に関するガイドライン]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)をご覧ください。

### 絵文字は何文字を使用しますか？ {#how-many-characters-does-an-emoji-use}

絵文字は扱いが難しい場合があります。すべての絵文字に標準的な文字数があるわけではないためです。絵文字が文字数制限を超え、Brazeコンポーザーでは1通のメッセージとして表示されているにもかかわらず、SMSが複数のメッセージに分割されるリスクがあります。メッセージのテストでは、[セグメント計算ツール]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator)を使用して、メッセージが分割されるかどうかをより正確に確認できます。

## 購読グループとオプトイン/オプトアウト {#subscription-groups-and-opt-inopt-out}

### SMSの選択的オプトインのロジックを作成して、ユーザーを適切な購読グループに配置するにはどうすればよいですか？ {#how-do-you-create-logic-for-selective-opt-ins-to-sms-so-users-are-in-the-right-subscription-group}

カスタムキーワードはカスタムイベントとして記録されるため、顧客がテキスト送信できるキーワードに基づいてセグメントを作成します。たとえば、ユーザーがVIPメッセージにはSMSオプトインしているがアラートにはオプトインしていない場合、VIPセグメントとアラートセグメントを作成し、ユーザーを適切なセグメントに割り当てることができます。

### ユーザーがショートコードに「Stop」とテキスト送信した場合、購読グループから購読解除されますか？ {#if-a-user-texts-stop-to-our-short-code-are-they-unsubscribed-from-the-subscription-group}

ユーザープロファイルではどのように表示されますか？購読グループは**連絡先設定**の下で購読解除として表示され、購読と購読解除のカスタムイベントが記録されます。

### ユーザーがオプトアウトしている状態でショートコードやロングコードにキーワードを送信した場合、Brazeで設定したそのキーワードへの応答を受信しますか？ {#if-a-user-is-opted-out-and-sends-a-keyword-to-our-short-and-long-code-do-they-receive-the-response-we-configured-for-that-keyword-in-braze}

ユーザーがオプトアウトしている状態で[デフォルトキーワードカテゴリ]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout)のキーワードを送信した場合、そのキーワードに対する応答を受信します。ユーザーがオプトアウトしている状態で[カスタムキーワード]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling)を送信した場合、そのキーワードに対する応答は受信しません。

### SMSイベントプロパティは文中のキーワードをキャプチャしますか？ {#will-sms-event-properties-capture-keywords-in-a-sentence}

文中のキーワードを認識させるには（たとえば「please stop texting me」）、メッセージ内でLiquidステートメントを使用して特定の単語を認識させる必要があります。イベントプロパティには256文字の制限がありますが、それ以外に文字数制限はありません。

## テスト {#testing}

### テストテキストメッセージは制限にカウントされますか？ {#do-test-text-messages-count-toward-limits}

はい、カウントされます。メッセージのテスト時にはこの点に注意してください。

### ユーザーがSMSテストメッセージを受信するには、SMS購読グループに属している必要がありますか？ {#does-a-user-need-to-be-part-of-an-sms-subscription-group-to-receive-sms-test-messages}

はい、必要です。ユーザーは有効な電話番号を持ち、テスト送信に使用するSMS購読グループに属し、SMSの**Geographic Permissions**で少なくとも1つの国が選択されている必要があります。

### ユーザープロファイルにエイリアスが存在するかどうかを確認する方法はありますか？ {#is-there-a-way-to-see-if-an-alias-exists-on-a-user-profile}

エイリアスはユーザープロファイルには表示されません。エイリアスが設定されていることを確認するには、[ユーザーデータのエクスポート]({{site.baseurl}}/api/endpoints/export)エンドポイントを使用する必要があります。

## MMS

### MMSを送信する場合、Currentsデータに変更はありますか？ {#are-there-any-changes-to-currents-data-when-sending-an-mms}

いいえ、MMSメッセージを送信する場合も同じレベルのインサイトが提供されます。

### MMSの画像とメッセージ本文の配信順序を制御できますか？ {#can-i-control-the-order-in-which-the-image-and-message-body-of-an-mms-are-delivered}

Brazeは、MMSメッセージにメッセージ本文と画像の両方が含まれている場合の表示順序を制御できません。これは以下を含むがこれに限定されないいくつかの要因に依存します。

- メッセージを受信するキャリア
- メッセージを受信するデバイス
- メッセージの全体的なサイズ

### MMSには別途オンボーディングプロセスが必要ですか？ {#does-mms-require-a-separate-onboarding-process}

いいえ。MMSは現在、SMSオンボーディングプロセスに含まれています。すでにオンボーディングを完了した既存のお客様は、以下のステップを完了した後にMMSキャンペーンの送信を開始できます。

1. MMSを購入します。
2. Brazeオンボーディングチームに連絡して、MMS機能の有効化をリクエストします。これによりMMSが有効になり、SMS/MMSサブスクリプショングループが作成または更新されます。

次に、BrazeオンボーディングチームがショートコードとロングコードがMMSに対して有効になっていることを確認します（米国とカナダ）。また、MMS用に追加または有効化された現在の番号を表示するようにサブスクリプショングループを更新します。これらのステップが完了すると、ネイティブのSMSコンポーザーからすぐにMMSメッセージを送信できます。

### 機能が有効になっているのに、ダッシュボードでMMSが見つからないのはなぜですか？ {#why-cant-i-find-mms-on-my-dashboard-even-though-the-feature-is-enabled}

MMSは、サブスクリプショングループが「MMS有効」と見なされた場合にのみBrazeダッシュボードに表示されます。これは、SMS/MMSメッセージのコンポーザーでサブスクリプショングループを選択する際のMMSタグに反映されます。つまり、サブスクリプショングループ内の少なくとも1つの番号がMMSメッセージを送信できる必要があります。

さらに、特定の状況では、元々MMSが有効になっていなかったショートコードの有効化をTwilioが再承認する必要がある場合があります。この承認プロセスには数週間かかる可能性があります。

## RCS

### iOSデバイスでRCSメッセージが正確にレンダリングされないのはなぜですか？ {#why-doesnt-my-rcs-message-render-accurately-on-ios-devices}

RCSメッセージは、オペレーティングシステムやメッセージングアプリによってiOSデバイスでの表示が異なる場合があります。iOSデバイスでは、以下の動作が発生する可能性があります。

- 同じ会話スレッド内の異なるRCSメッセージからのサジェストアクションがグループ化され、誤った順序で表示される場合があります。
- リッチカードボタンおよびリッチカード外のサジェストアクションが、リッチカードボタンやサジェストアクションをタップした後も表示されたままになる場合があります。

{% alert note %}
Brazeは作成したRCSペイロードを送信しますが、サジェストアクションの順序、グループ化、非表示はメッセージングクライアントが制御します。送信前に、特にサジェストアクションやサジェスト返信を使用するリッチカードを含むRCSメッセージを、AndroidとiOSの両方のデバイスでテストしてください。
{% endalert %}

### RCSで事前録音のボイスメールを送信できますか？ {#can-i-send-pre-recorded-voicemails-with-rcs}

はい、メディアメッセージを使用してオーディオファイルをサポートできます。

### REST APIのSMSオプトインがSMS/MMS/RCSパフォーマンスの**合計オプトイン数**と一致しないのはなぜですか？ {#why-do-rest-api-sms-opt-ins-not-match-total-opt-ins-on-smsmmsrcs-performance}

[SMS/MMS/RCSパフォーマンス]({{site.baseurl}}/user_guide/analytics/dashboards)ダッシュボードの**合計オプトイン数**と**合計オプトアウト数**は、受信SMSキーワード処理によるサブスクリプション変更をカウントします（たとえば、ユーザーがショートコードにオプトインキーワードをテキスト送信した場合）。REST API、ダッシュボード、またはその他のソースを通じて行われたすべてのサブスクリプション更新が含まれるわけではありません。

ソース別のオプトインとオプトアウトを分析するには、`USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED`で[クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder)を使用し、`STATE_CHANGE_SOURCE`でフィルタリングします（たとえば、**Rest API**と**Inbound Message**の比較）。