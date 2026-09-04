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

SMSの場合、API経由でSMSメッセージを送信する際（`/messages/send`エンドポイントなど）に`app_id`パラメーターが必要です。これは、ワークスペース内のどのアプリがSMSアクティビティまたはAPI呼び出しに関連付けられているかを指定します。SMSメッセージングのために、ユーザーのプロファイルにその特定のアプリがあるかどうかに関係なく、ワークスペースで設定された任意の有効な`app_id`を使用できます。

`app_id`は、**設定** > **アプリ設定**に移動し、**識別**セクションを見つけることで確認できます。

### 複数のユーザーが同じ電話番号を持っている場合はどうなりますか？ {#what-happens-if-multiple-users-have-the-same-phone-number}

同じ電話番号（SMSが有効）を共有する複数のユーザープロファイルが、受信SMSのイベントによってトリガーされるアクションベースのキャンペーンまたはキャンバスコンポーネントに同時に該当する場合、Brazeはキャンバスコンポーネントレベルでユーザーの重複排除を行います。これにより、複数のユーザーが同じ電話番号を共有していても、キャンバスコンポーネントに対して複数のSMSテキストを受信することが防止されます。

{% alert note %}
Brazeは、スケジュールされたキャンバスでは電話番号による重複排除を行いません。
{% endalert %}

Brazeは、受信者プロファイルを決定するために以下のフローを使用します。
- 最も最近SMSを受信したプロファイルを確認します（最大7日前まで）。存在する場合、そのユーザーに送信します。
- どちらも最大7日前までにSMSを受信していない場合、電話番号と一致する「phone」というユーザーエイリアスを持つユーザーに送信します。
- どちらも存在しない場合、利用可能なプロファイルの中からランダムなプロファイルに送信します。

共有電話番号から「START」または「STOP」キーワードを受信した場合、すべてのユーザープロファイルがSMSの購読および有効化、または購読解除されます。これはAPIのステータス変更にも適用されます。たとえば、異なるexternal IDを持つ複数のプロファイルが同じ電話番号を持っている場合、APIを通じた購読グループのステータス変更は、1つのexternal IDのみが指定されていても、その電話番号を持つすべてのプロファイルを更新します。

{% alert important %}
ユーザーをキャンバスに段階的に投入し、各キャンバスコンポーネントのスケジュール時間が異なる場合、同じメールアドレスまたは電話番号を持つユーザーに重複メッセージが送信される可能性があります。
{% endalert %}

不必要に大規模な更新を防ぐため、購読の更新が行われる際、Brazeは識別子を共有するユーザープロファイルを最大100件まで更新します。同じ電話番号を共有するユーザープロファイルが100件を超える場合、すべてのプロファイルが更新されるわけではありません。

### 特定のソースからのSMS購読が急増するのはなぜですか？ {#why-do-i-see-a-spike-in-sms-subscriptions-from-a-specific-source}

購読数が予想外に大幅に増加した場合、特にCurrentsを通じて[`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)エンドポイントのデータを確認する際に、重複したユーザープロファイルが原因である可能性があります。

`/subscription/status/set`エンドポイントに電話番号のみ（`external_id`なし）でリクエストが行われた場合、Brazeはその電話番号を共有するすべてのユーザープロファイルを更新します。ワークスペースに重複プロファイルがある場合、実際には1つの電話番号のみが変更されたにもかかわらず、購読ステータスを更新したユーザーの数が膨らみます。

Currentsからデータを取得する際に購読データをより正確に分析するには、すべての購読ステータス変更イベントをカウントするのではなく、一意の電話番号をカウントするようにクエリを更新してください。

### 共有ショートコードとは何ですか？ {#what-are-shared-short-codes}

共有ショートコードでは、どの企業や組織がメッセージを送信したかに関係なく、すべてのテキストメッセージが同じ5〜6桁の電話番号から消費者のモバイルデバイスに届きます。共有ショートコードは比較的低コストですぐに利用できますが、企業が専用のショートコードを持てないことを意味します。

このアプローチにはいくつかのデメリットがあります。

- 顧客が、あなたと共有ショートコードを持つ別の企業のメッセージをオプトアウトした場合、あなたのメッセージもオプトアウトされます。
- 1つの企業がルールに違反した場合、すべての企業のメッセージが停止されます。
- セキュリティの問題

## 請求と料金 {#billing-and-pricing}

### SMSはどのように請求されますか？ {#how-will-i-be-billed-for-sms}

ショートコードやロングコードの料金に加えて、Brazeはさまざまな国向けにSMSメッセージの割り当てを提供しています。つまり、お客様と協力してさまざまな国のメッセージセグメント数を設定し、その割り当て内でSMSキャンペーンを送信していただきます。請求は、国ごとに送信されたメッセージセグメント数に基づいて行われます。メッセージセグメントの計算方法の詳細については、[メッセージセグメントとコピー制限]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator)ガイドを参照してください。割り当ての上限に近づいている場合は、アカウントマネージャーから関連レポートとともにご連絡いたします。超過料金に関するその他のご質問については、Brazeの担当者にお問い合わせください。

### MMSとSMSの料金は異なりますか？ {#does-mms-and-sms-pricing-differ}

MMSとSMSはコストが異なり、ボリュームに基づいて個別に請求されます。料金情報については、Brazeオンボーディングチームにお問い合わせください。

### 超過料金を避けるにはどうすればよいですか？ {#how-can-i-avoid-overages}

超過料金が一切発生しないことは保証できませんが、割り当て制限を超える可能性を減らすために以下の予防策に従うことができます。

- SMSの文字数に注意してください。意図せず1つ以上のセグメントを送信すると、超過料金が発生する可能性があります。詳細については、[セグメントの内訳]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator)を参照してください。
- LiquidやConnected Contentを考慮してSMSの文字数を慎重に計算してください。ダッシュボードのBraze SMSコンポーザーでは、これらの機能の使用量を見積もったり考慮したりすることはできません。
- メッセージで使用するエンコーディングの種類を考慮してください。メッセージがGSM-7エンコーディングを使用する場合、通常メッセージセグメントあたり160文字と見積もることができます（GSM-7拡張テーブルの文字を使用する場合はより少なくなります）。メッセージが[UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set)エンコーディングを使用する場合、通常メッセージセグメントあたり67文字と見積もることができます。
- テスト、テスト、そしてテスト！特にLiquidやConnected Contentを使用する場合は、送信前に必ずSMSメッセージをテストしてください。

### 固定電話にメッセージが送信された場合、SMS送信数にカウントされますか？ {#if-a-message-is-sent-to-a-landline-will-the-message-still-count-toward-my-sms-send-count}

米国、カナダ、英国の場合：
- SMSが固定電話に送信された場合、**未配信**としてマークされます。請求の動作はSMSサービスプロバイダーによって異なります。Twilioの場合、配信の試行にも課金されるため、メッセージログで**送信済み**、**配信済み**、または**未配信**としてマークされたメッセージが請求対象となります。
- 英国では、一部のキャリアがSMSをボイスメールに変換してメッセージを配信します。

その他の国の場合：
- Twilioの場合、エラーがスローされ、試行されたSMSメッセージに対して請求されません。

### メッセージが160文字（GSM-7）または67文字（UCS-2）未満なのに、追加のメッセージセグメントが請求される可能性があるとBrazeダッシュボードが警告するのはなぜですか？ {#why-is-the-braze-dashboard-warning-me-i-may-be-charged-for-additional-message-segments-when-my-message-is-under-160-gsm-7-or-67-ucs-2-characters}

メッセージにLiquidパーソナライゼーションが含まれている場合、追加のメッセージセグメントが請求される可能性があります。コンテンツブロックのテンプレート処理は、メッセージが送信準備される時点まで行われません。コンテンツブロックを含むSMSを編集しているとき、Brazeはコンテンツブロックの内容を把握できませんが、おおよその見積もりを提供します。テストペインを使用してメッセージをプレビューし、期待される結果をより正確に把握することをお勧めします。

## 送信とデリバラビリティ {#sending-and-deliverability}

### SMSにリンクを含めることはできますか？ {#can-you-include-links-in-an-sms}

任意のSMSキャンペーンにリンクを含めることができます。ただし、いくつかの注意点があります。

- リンクはSMSの160文字制限の大部分を占める場合があります。リンクとテキストを含めると、1通ではなく2通のSMSメッセージになることがあります。
- 企業はリンクの文字数への影響を抑えるためにリンク短縮サービスを使用することがよくあります。ただし、短縮リンクをロングコードで送信すると、キャリアがリンクリダイレクトを疑わしいと判断し、メッセージをブロックまたは拒否する可能性があります。
- [ショートコード]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup)を使用することが、リンクを含める上で最も信頼性の高い番号タイプです。

Brazeには独自のリンク短縮機能もあり、リンクを自動的に短縮し、クリックスルー分析を提供します。詳細については、[リンク短縮]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening)を参照してください。

### SMSメッセージの送信速度をレート制限する必要がありますか？ {#do-you-need-to-rate-limit-how-fast-you-send-sms-messages}

デフォルトの同時実行レートとスループットでは、ショートコードごとに1時間あたり約360,000メッセージの送信が可能です。追加のスループットが必要な場合は、追加のショートコードが必要です。

### SMSのURLをどのように許可リストに登録しますか？ {#how-do-you-allowlist-urls-for-sms}

特定の国（スウェーデンや北欧諸国など）のユーザーにURLを含むSMSメッセージを送信する前に、これらのURLをキャリアに登録する必要があります。Brazeカスタマーサービスマネージャーにお問い合わせください。このプロセスには約5日かかります。

### SMSのスパム検出を避けるためのベストプラクティスは何ですか？ {#what-are-the-best-sending-practices-to-avoid-spam-detection-for-sms}

1. オプトインとオプトアウトの手順が明確であることを確認してください。
2. あなた（ブランド）が顧客と関係を持っていることを確認してください。
3. コンテンツがその関係およびユーザーが受信をオプトインした内容に関連していることを確認してください。

スパム検出を避けるためのガイドラインの詳細については、[SMSの法律と規制に関するガイドライン]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)をご覧ください。

### 絵文字は何文字を使用しますか？ {#how-many-characters-does-an-emoji-use}

絵文字は扱いが難しい場合があります。すべての絵文字で標準の文字数が決まっているわけではありません。絵文字が文字数制限を超え、Brazeコンポーザーでは1通のメッセージとして表示されているにもかかわらず、SMSが複数のメッセージに分割されるリスクがあります。メッセージをテストする際に、[セグメント計算ツール]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator)を使用して、メッセージが分割されるかどうかをより正確に確認できます。

## 購読グループとオプトイン/オプトアウト {#subscription-groups-and-opt-inopt-out}

### ユーザーが適切な購読グループに入るように、SMSの選択的オプトインのロジックを作成するにはどうすればよいですか？ {#how-do-you-create-logic-for-selective-opt-ins-to-sms-so-users-are-in-the-right-subscription-group}

カスタムキーワードはカスタムイベントとして記録されるため、顧客がテキストで送信できるキーワードに基づいてセグメントを作成します。たとえば、ユーザーがVIPメッセージにはSMSオプトインしているがアラートにはオプトインしていない場合、VIPセグメントとアラートセグメントを作成し、ユーザーを適切なセグメントに割り当てることができます。

### ユーザーがショートコードに「Stop」とテキスト送信した場合、購読グループから購読解除されますか？ {#if-a-user-texts-stop-to-our-short-code-are-they-unsubscribed-from-the-subscription-group}

ユーザープロファイルではどのように表示されますか？購読グループは**連絡先設定**で購読解除として表示され、購読と購読解除のカスタムイベントが記録されます。

### ユーザーがオプトアウト済みで、ショートコードやロングコードにキーワードを送信した場合、Brazeで設定したそのキーワードの応答は受信されますか？ {#if-a-user-is-opted-out-and-sends-a-keyword-to-our-short-and-long-code-do-they-receive-the-response-we-configured-for-that-keyword-in-braze}

ユーザーがオプトアウト済みで[デフォルトのキーワードカテゴリ]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout)のキーワードを送信した場合、そのキーワードの応答を受信します。ユーザーがオプトアウト済みで[カスタムキーワード]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling)を送信した場合、そのキーワードの応答は受信しません。

### SMSイベントプロパティは文中のキーワードをキャプチャしますか？ {#will-sms-event-properties-capture-keywords-in-a-sentence}

文中のキーワードを認識させるには（たとえば「please stop texting me」）、メッセージ内でLiquidステートメントを使用して特定の単語を認識させる必要があります。イベントプロパティには256文字の制限がありますが、それ以外に文字数制限はありません。

## テスト {#testing}

### テストテキストメッセージは制限にカウントされますか？ {#do-test-text-messages-count-toward-limits}

はい、カウントされます。メッセージのテスト時にはこの点に注意してください。

### SMS テストメッセージを受信するには、ユーザーが SMS 購読グループに属している必要がありますか？ {#does-a-user-need-to-be-part-of-an-sms-subscription-group-to-receive-sms-test-messages}

はい、必要です。ユーザーは有効な電話番号を持ち、テスト送信に使用する SMS 購読グループに属しており、SMS の**地理的権限**で少なくとも1つの国が選択されている必要があります。

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
2. Brazeオンボーディングチームに連絡して、MMS機能の有効化をリクエストします。これによりMMSが有効になり、SMS/MMS購読グループが作成または更新されます。

次に、BrazeオンボーディングチームがショートコードとロングコードがMMSに対して有効になっていることを確認します（米国とカナダ）。また、MMS用に追加または有効化された現在の番号を表示するように購読グループを更新します。これらのステップが完了すると、ネイティブのSMSコンポーザーからすぐにMMSメッセージを送信できます。

### 機能が有効になっているのに、ダッシュボードでMMSが見つからないのはなぜですか？ {#why-cant-i-find-mms-on-my-dashboard-even-though-the-feature-is-enabled}

MMSは、購読グループが「MMS有効」と見なされた場合にのみBrazeダッシュボードに表示されます。これは、SMS/MMSメッセージのコンポーザーで購読グループを選択する際のMMSタグに反映されます。つまり、購読グループ内の少なくとも1つの番号がMMSメッセージを送信できる必要があります。

さらに、特定の状況では、元々MMSが有効になっていなかったショートコードの有効化をTwilioが再承認する必要がある場合があります。この承認プロセスには数週間かかる可能性があります。

### 画像付きのMMSが送信に失敗するのはなぜですか？ {#why-does-my-mms-with-an-image-fail-to-send}

一部のSMSプロバイダーは、画像URLの`Content-Type`ヘッダーを検証します。画像付きのMMSが中止される場合は、ホストされている画像URLが`image/png`またはその他のサポートされている画像タイプを返すことを確認してください（例：`curl -I <image-url>`を使用）。正しい`Content-Type`を提供するBrazeメディアライブラリまたはCDNにアセットを再ホストしてください。

### MMSで連絡先カードの画像が表示されないのはなぜですか？ {#why-doesnt-my-contact-card-image-appear-in-an-mms}

MMSの連絡先カード写真は、連絡先カードファイルが受信者のデバイスで取得できない画像URLを参照している場合、レンダリングに失敗することがあります。電話で連絡先カードを作成し、ファイルをエクスポートして、MMSメッセージで使用するためにメディアライブラリにアップロードしてください。

## RCS

### iOSデバイスでRCSメッセージが正確にレンダリングされないのはなぜですか？ {#why-doesnt-my-rcs-message-render-accurately-on-ios-devices}

RCSメッセージは、オペレーティングシステムやメッセージングアプリによってiOSデバイスでの表示が異なる場合があります。iOSデバイスでは、以下の動作が発生する可能性があります。

- 同じ会話スレッド内の異なるRCSメッセージからのサジェストアクションがグループ化され、誤った順序で表示される場合があります。
- リッチカードボタンおよびリッチカード外のサジェストアクションが、リッチカードボタンやサジェストアクションをタップした後も表示されたままになる場合があります。
- リッチカード内のGIFが静止画像として表示されます。詳細については、[RCSリッチカード内のGIFがiOSで静止画として表示されるのはなぜですか？](#why-do-gifs-in-rcs-rich-cards-appear-static-on-ios)を参照してください。

{% alert note %}
Brazeは作成したRCSペイロードを送信しますが、サジェストアクションの順序、グループ化、非表示はメッセージングクライアントが制御します。送信前に、特にサジェストアクションやサジェスト返信を使用するリッチカードを含むRCSメッセージを、AndroidとiOSの両方のデバイスでテストしてください。
{% endalert %}

### RCSリッチカード内のGIFがiOSで静止画として表示されるのはなぜですか？ {#why-do-gifs-in-rcs-rich-cards-appear-static-on-ios}

iOSでは、RCSリッチカード内のGIFは静止画像（最初のフレーム）として表示されます。Androidでは、期待どおりにアニメーション再生されます。

この動作はiOSのメッセージングクライアントが制御しています。BrazeのプレビューではGIFがアニメーション再生される場合があります。配信されたメッセージの見え方を確認するには、iOSデバイスにテストメッセージを送信してください。

iOSにアニメーションコンテンツを送信するには：

- RCSの**メディア**メッセージを使用して、GIFをファイルとして送信します
- リッチカードで動画を使用します

### RCSで事前録音のボイスメールを送信できますか？ {#can-i-send-pre-recorded-voicemails-with-rcs}

はい、メディアメッセージを使用してオーディオファイルをサポートできます。

### REST APIのSMSオプトインがSMS/MMS/RCSパフォーマンスの**合計オプトイン数**と一致しないのはなぜですか？ {#why-do-rest-api-sms-opt-ins-not-match-total-opt-ins-on-smsmmsrcs-performance}

[SMS/MMS/RCSパフォーマンス]({{site.baseurl}}/user_guide/analytics/dashboards)ダッシュボードの**合計オプトイン数**と**合計オプトアウト数**は、受信SMSキーワード処理によるサブスクリプション変更をカウントします（たとえば、ユーザーがショートコードにオプトインキーワードをテキスト送信した場合）。REST API、ダッシュボード、またはその他のソースを通じて行われたすべてのサブスクリプション更新が含まれるわけではありません。

ソース別のオプトインとオプトアウトを分析するには、`USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED`で[クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder)を使用し、`STATE_CHANGE_SOURCE`でフィルタリングします（たとえば、**Rest API**と**Inbound Message**の比較）。