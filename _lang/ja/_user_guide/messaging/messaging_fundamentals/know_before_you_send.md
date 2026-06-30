---
nav_title: "送信前に知っておくべきこと"
article_title: "送信前に知っておくべきこと"
description: "ローンチ前ガイドを確認した後、Content Cards、メール、アプリ内メッセージ、プッシュ、SMSに関する最終チェックリストや「注意点」を参照してください。"
alias: /know_before_send/
page_order: 7
tool:
    - Campaigns
    - Canvas
---

# 送信前に知っておくべきこと: チャネル {#know-before-you-send-channels}

> 自信を持ってCampaignsやCanvasesをローンチしましょう！Brazeの主要なメッセージング[チャネル]({{site.baseurl}}/user_guide/channels)に関する最終チェックリストや「注意点」を参照してください。

{% alert note %}
送信前に参照できるリソースの広範なリストを提供していますが、各チャネルには製品の進化に伴い増え続ける個別のニュアンスがあります。以下に記載されたチェック項目は参考となる提案であり、送信前にCampaignsや大量送信を十分にテストすることをお勧めします。
{% endalert %}

## 一般 {#general}

### 確認すべきこと {#things-to-check}
- [**APIレート制限**](https://braze.com/resources/articles/whats-rate-limiting): ワークスペースのBraze API[レート制限]({{site.baseurl}}/api/api_limits)を確認し、エラーを回避してください。レート制限の引き上げを希望する場合（すでにリクエストをバッチ処理している場合）は、カスタマーサクセスマネージャーにお問い合わせください。このプロセスにはリードタイムが必要なため、計画的に進めてください。
- [**必要なフリークエンシーキャップの上書き**]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping): トランザクションメッセージなど、フリークエンシーキャップに達していてもユーザーに必ず届けたいCampaignsがあります（例：配送通知）。特定のCampaignでフリークエンシーキャップルールを上書きしたい場合は、BrazeダッシュボードでそのCampaignの配信スケジュール設定時にフリークエンシーキャップをオフに切り替えることで設定できます。

### 知っておくべきこと {#things-to-know}
- [**グローバルコントロールグループ**]({{site.baseurl}}/user_guide/audience/global_control_group): グローバルコントロールグループを使用している場合、一定の割合のユーザーはCampaignsやCanvasesを受信しません。（[除外設定]({{site.baseurl}}/user_guide/audience/global_control_group#step-3-assign-exclusion-settings)で例外を作成できます。）これらのユーザーのリストを確認するには、CSVまたは[API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group)でエクスポートしてください。
- [**Canvasレート制限**]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping): Canvasでは、レート制限は個々のステップではなくCanvas全体に適用されます。例えば、複数のステップを持つCanvasに1分あたり10,000メッセージのレート制限を設定した場合、最初のステップで制限に達するため、依然として10,000メッセージに制限されます。
- **フリークエンシーキャップ**:
  - フリークエンシーキャップルールはプッシュ、メール、SMS、webhookに適用されますが、アプリ内メッセージやContent Cardsには適用されません。
  - グローバルフリークエンシーキャップはユーザーのタイムゾーンに基づいてスケジュールされ、24時間単位ではなくカレンダー日で計算されます。例えば、1日1回以下のCampaign送信というフリークエンシーキャップルールを設定した場合、ユーザーはローカルタイムゾーンの午後11時にメッセージを受信し、1時間後に別のメッセージを受信する資格を得る可能性があります。

{% alert tip %}
CanvasやCampaignのトラブルシューティングについてさらにサポートが必要な場合は、問題発生から30日以内にBrazeサポートにお問い合わせください。直近30日分の診断ログのみ保持しています。
{% endalert %}

## バナー {#banners}

### 確認すべきこと
- **バナーのサイズ:** 固定サイズの要素を使用してバナーを構築し、エディターでテストしてください。
- **優先度:** 複数のバナーをローンチする場合、各バナーの表示優先度を手動で設定できます。

### 知っておくべきこと
- **Liquidパーソナライゼーション:** Liquidパーソナライゼーションはリフレッシュリクエストごとに更新されます。
- **プレースメントとバナーの比率:** 各バナープレースメントは、ワークスペース内で最大25件のメッセージに使用できます。
- **クリック数とインプレッション:** バナーのクリック数とインプレッションはSDKで自動的にトラッキングされます。
- **制限事項:** 現在、以下の機能はサポートされていません：Canvas統合、APIトリガーおよびアクションベースのCampaigns、コネクテッドコンテンツ、プロモーションコード、[`:rerender`タグ]({{site.baseurl}}/user_guide/data/activation/catalogs/use#using-liquid)を使用した`catalog_items`。
- **テスト:** テストバナーを表示するには、使用するデバイスがフォアグラウンドプッシュ通知を受信できる必要があります。
- **カスタムHTML:** カスタムHTMLを使用してリンクやボタンなどのクリックアクションを定義する場合は、[JSブリッジ]({{site.baseurl}}/user_guide/channels/in_app_messages/customize#javascript-bridge)を活用してクリックをログに記録してください。クリックアクションは、ドラッグ＆ドロップエディターの組み込みコンポーネントを使用した場合にのみ自動的にログに記録されます。
- **プレースメントのリクエスト:** 1回のリフレッシュリクエストで最大10件のプレースメントをSDKに返すことができます。各プレースメントには、ユーザーが対象となる最も優先度の高いバナーが含まれます。

## Content Cards

### 確認すべきこと
- **Content Cardsのサイズ**: Content Cardsのメッセージフィールドは、圧縮前のサイズで2&nbsp;KBに制限されています。これは、タイトル、メッセージ、画像URL、リンクテキスト、リンクURL、キーと値のペアの各フィールドのバイトサイズの合計で計算されます。このサイズを超えるメッセージは送信されません。これには画像自体のサイズは含まれず、画像URLの長さのみが対象です。
- **送信後のコピー更新**: カードが送信された後、同じカードのコピーを更新することはできません。このシナリオへの対処方法については、[送信済みカードの更新]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#updating-sent-cards)を参照してください。

### 知っておくべきこと
- **アクティブなContent Cards Campaignsの上限**: アクティブなContent Cards Campaignsは最大500件まで設定できます。このカウントには、いずれかの[カード作成]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#card-creation)オプションで送信されたContent Cardsが含まれます。
- [**レポート用語**]({{site.baseurl}}/user_guide/channels/content_cards/reporting): 合計インプレッション数、ユニークインプレッション数、ユニーク受信者数などの用語を確認してください。定義が混乱を招く場合があります。
- **Content Cardsのリフレッシュ**: デフォルトでは、Brazeはセッション開始時の同期、フィードの下スワイプ（モバイル）、および最後のリフレッシュから1分以上経過した場合のカードビュー表示時にContent Cardsリクエストをリフレッシュします。
- **Content Cardsのキャッシュ**: Content Cardsのキャッシュオプションについては、[Android/FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization/custom_styling#customizing-card-rendering-for-android)および[Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#getcachedcontentcards)のドキュメントを参照してください。
- **フリークエンシーキャップ**: フリークエンシーキャップはContent Cardsには適用されません。
- **インプレッション**: インプレッションは通常、カードが表示されたときにログに記録されます。例えば、Content Cardsでいっぱいの受信トレイがある場合、ユーザーが特定のContent Cardまでスクロールするまでインプレッションはログに記録されません。Web、Android、iOSプラットフォーム間にはいくつかのニュアンスがあります。
- **SDKセッションとカード作成**: SDKセッションのないユーザーに対しては、Segmentの条件を満たしていてもContent Cardsは作成されません。ただし、ユーザーがすでにAndroidセッションを持っている場合、iOS固有のクリックアクションを持つContent Cardsは作成され、ユーザーはiOSでセッションを持った後にそれらのContent Cardsを表示できます。カードが作成されるタイミングの詳細については、[カード作成]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#card-creation)を参照してください。

## メール {#email}

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

### 確認すべきこと
- **顧客の同意**: 最初のメールを送信する前に、まず顧客から許可を得ることが重要です。詳細については、[同意とアドレスの収集]({{site.baseurl}}/user_guide/channels/email/email_setup/consent_and_address_collection)および[Braze利用規約](https://www.braze.com/company/legal/aup)を参照してください。
- **想定される送信量**: 単一IPで1日あたり200万通のメールが一般的な推奨値です（その送信量が適切に[ウォームアップ]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming#ip-warming)されている場合）。
  - これを超える送信量を継続的に計画している場合、プロバイダーがメールの受信をスロットリングし、ソフトバウンスの増加、配信率の低下、IP評判の低下を招くことを避けるため、IPプールにバンドルされた複数のIPアドレスの使用を検討してください。
  - より短い時間枠での送信を検討している場合は、異なるプロバイダーがメールを受け入れる速度を調査し、送信に適切なIP数を判断することをお勧めします。

### 知っておくべきこと
- **送信量に影響する要因**: IPの送信可能量を決定する要因には以下が含まれます：
  - メールボックス：大手メールプロバイダーは単一IPから1日あたり数百万通を処理できる可能性がありますが、小規模な地域のメールボックスプロバイダーやインフラが小さいプロバイダーはその量を処理できない場合があります。
  - 送信者の評判：送信者がその送信量まで段階的に増加させ、送信先の各メールボックスやドメインで十分な送信者評判を持っている場合、単一IPからより大量の送信が可能になる場合があります。
- **ベストプラクティス**: Brazeの[メールベストプラクティス]({{site.baseurl}}/user_guide/channels/email/best_practices)を確認し、配信性サービスについて詳しく知りたい場合はBrazeアカウントチームにお問い合わせください。

## アプリ内メッセージ {#in-app-messages}

### 知っておくべきこと
- **アプリ内メッセージのトリガー**: セッション開始時に、SDKは対象となるすべてのアプリ内メッセージとそのトリガーをデバイスに送信するようリクエストします。そのため、セッション中にイベントを実行すると、アプリ内メッセージを迅速かつ確実に受信できます。
- **送信数とインプレッション**: アプリ内メッセージの場合、「送信」の概念は他の利用可能なチャネルとは異なります。アプリ内メッセージを表示するには、ユーザーがセッションを開始し、対象オーディエンスに含まれ、トリガーを実行する必要があります。このため、より明確な「インプレッション」をトラッキングしています。
- **トリガー**: デフォルトでは、アプリ内メッセージはSDKによってログに記録されたイベントによってトリガーされます。サーバー送信イベントによってアプリ内メッセージをトリガーしたい場合は、[iOS]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=swift)および[Android]({{site.baseurl}}/developer_guide/in_app_messages/customization?sdktab=android)のガイドを参照してください。
- [Canvasアプリ内メッセージ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas#advancement-behavior-options): これらのメッセージは、Canvasコンポーネントでスケジュールされたメッセージがユーザーに送信された後、ユーザーが初めてアプリを開いたとき（セッション開始によってトリガー）に表示されます。
- **コネクテッドコンテンツの呼び出し**: コネクテッドコンテンツを使用すると、メッセージにダイナミックなコンテンツを送信できます。アプリ内メッセージなどのチャネルでメッセージを送信する場合、ユーザーのデバイスへの同時接続が増加する可能性があります（メッセージはバッチではなく1つずつ送信されます）。これを管理するために、メッセージに[レート制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping)を設定することをお勧めします。

## プッシュ {#push}

### 確認すべきこと
- [**オプトイン/購読中とプッシュ有効**]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states): ユーザーがBrazeからプッシュメッセージを受信するには、サブスクリプションステータスがオプトイン（iOS）または購読中（Android）であり、`Push Enabled = True`である必要があります。Android 13では、プッシュ通知を送信するアプリの管理方法に大きな変更が導入されています。Brazeの[Android 13 SDKアップグレードガイド]({{site.baseurl}}/developer_guide/platforms/android/android_13)は、新しいAndroid 13ベータ版がリリースされるたびに更新されます。

### 知っておくべきこと
- **Webプッシュ**: Brazeの[Web SDKセットアップ]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web)が完了している場合は、Webプッシュを活用してユーザーをエンゲージすることを検討してください。Webプッシュは、スマートフォンのアプリプッシュ通知と同じように動作します。Webプッシュの作成方法の詳細については、[プッシュ通知の作成]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#creating-a-push-message)を参照してください。
- **単一アプリのターゲティング**: 単一アプリとそのユーザーをターゲティングするための[セグメンテーションの違い]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration#targeting-a-singular-app)を確認してください。

## SMS

### 確認すべきこと
- **割り当てとスループット**: 現在アカウントに紐づいているSMS割り当て（ショートコード、ロングコードなど）と、[それによって提供されるスループット]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup)を把握し、希望する時間内に送信するのに十分なスループットがあることを確認してください。
- **SMSコピーからのセグメント推定**: [SMSセグメント計算ツール]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator)でSMSコピーをテストしてください。SMSセグメント数はスループット能力と合わせて考慮する必要があります。（オーディエンス × SMSセグメント = 必要なスループット）。[超過料金の回避]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs)についてはSMS FAQを参照してください。
- **SMSの法律と規制**: [SMSの法律、規制、不正利用防止]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)を確認し、すべての適用法に準拠してSMSサービスを使用していることを確認してください。送信前に法律顧問の助言を求めることをお勧めします。

### 知っておくべきこと
- **SMSメッセージのデフォルト**: SMSメッセージは通常、送信者プール内のショートコードからデフォルトで送信されます。
- **英数字送信者ID**: 英数字送信者IDを使用すると、双方向メッセージングは機能しなくなります。現在は一方向のみです。
- **米国でのスループットの更新**: 米国では[A2P 10DLC登録](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US)によりスループットが変更されています。トラフィックの混雑やキャリアの問題など、実際の配信率に影響を与える複数の要因があるため、送信速度のSLAを契約上保証していないことにご注意ください。
- **サブスクリプショングループ**: BrazeでSMS Campaignをローンチするには、サブスクリプショングループを選択する必要があります。また、国際的な[通信コンプライアンスおよびガイドライン]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)を遵守するため、Brazeは[選択されたサブスクリプショングループに登録]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#how-to-check-a-users-sms-subscription-group)していないユーザーにSMSを送信することはありません。

## WhatsApp

### 知っておくべきこと

- [**ベストプラクティス**]({{site.baseurl}}/user_guide/channels/whatsapp/best_practices): WhatsAppのベストプラクティスに関する推奨事項を確認してください。