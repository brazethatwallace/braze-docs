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

> 自信を持ってキャンペーンやキャンバスをローンチしましょう！Brazeの主要なメッセージング[チャネル]({{site.baseurl}}/user_guide/channels)に関する最終チェックリストや「注意点」を参照してください。

{% alert note %}
送信前に参照できるリソースの広範なリストを提供していますが、各チャネルには製品の進化に伴い増え続ける個別のニュアンスがあります。以下に記載されたチェック項目は参考となる提案であり、送信前にキャンペーンや大量送信を十分にテストすることをお勧めします。
{% endalert %}

## 一般的な情報 {#general}

### チェックすべき事項 {#things-to-check}
- [**APIレート制限**](https://braze.com/resources/articles/whats-rate-limiting): ワークスペースのBraze API [レート制限]({{site.baseurl}}/api/api_limits)を確認して、エラーを回避してください。レート制限の引き上げを検討している場合（すでにリクエストをバッチ処理している場合）は、カスタマーサクセスマネージャーにご連絡ください。このプロセスにはリードタイムが必要ですので、計画的に進めてください。
- [**必要なフリークエンシーキャップのオーバーライド**]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping): トランザクションメッセージのように、フリークエンシーキャップに達している場合でも常にユーザーに届けたいキャンペーンがあります（例: 配送通知）。特定のキャンペーンでフリークエンシーキャップルールをオーバーライドしたい場合は、Brazeダッシュボードでそのキャンペーンの配信スケジュール設定時にフリークエンシーキャップをオフに切り替えることで設定できます。

### 知っておくべきこと {#things-to-know}
- [**グローバルコントロールグループ**]({{site.baseurl}}/user_guide/audience/global_control_group): グローバルコントロールグループを使用している場合、一定の割合のユーザーはキャンペーンやキャンバスを受信しません。（[除外設定]({{site.baseurl}}/user_guide/audience/global_control_group#step-3-assign-exclusion-settings)で例外を作成できます。）これらのユーザーのリストを確認するには、CSVまたは[API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group)でエクスポートしてください。
- [**キャンバスのレート制限**]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping): キャンバスでは、レート制限は個々のステップではなくキャンバス全体に適用されます。例えば、複数のステップがあるキャンバスに1分あたり10,000メッセージのレート制限を設定した場合、最初のステップで上限に達するため、依然として10,000メッセージに制限されます。
- **フリークエンシーキャップ**:
  - フリークエンシーキャップルールは、プッシュ、メール、SMS、webhookに適用されますが、アプリ内メッセージやContent Cardsには適用されません。
  - グローバルフリークエンシーキャップはユーザーのタイムゾーンに基づいてスケジュールされ、24時間単位ではなくカレンダー日で計算されます。例えば、1日1回以下のキャンペーン送信というフリークエンシーキャップルールを設定した場合、ユーザーはローカルタイムゾーンの午後11時にメッセージを受信しても、1時間後に別のメッセージを受信する資格があります。

{% alert tip %}
キャンバスやキャンペーンのトラブルシューティングでさらにサポートが必要な場合は、問題発生から30日以内にBrazeサポートにご連絡ください。診断ログは直近30日分のみ保持されています。
{% endalert %}

## バナー {#banners}

### 確認すべきこと
- **バナーのサイズ:** 固定サイズの要素を使用してバナーを構築し、エディターでテストしてください。
- **優先度:** 複数のバナーを公開する場合、各バナーの表示優先度を手動で設定できます。

### 知っておくべきこと
- **Liquidパーソナライゼーション:** Liquidパーソナライゼーションはリフレッシュリクエストごとに更新されます。
- **プレースメントとバナーの比率:** 各バナープレースメントは、ワークスペース内で最大25件のメッセージに使用できます。
- **クリックとインプレッション:** バナーのクリックとインプレッションはSDKで自動的にトラッキングされます。
- **制限事項:** 現在、以下の機能はサポートされていません：キャンバス統合、APIトリガーおよびアクションベースのキャンペーン、Connected Content、プロモーションコード、[`:rerender` タグ]({{site.baseurl}}/user_guide/data/activation/catalogs/use#using-liquid)を使用した `catalog_items`。
- **テスト:** テスト用バナーを表示するには、使用するデバイスがフォアグラウンドプッシュ通知を受信できる必要があります。
- **カスタムHTML:** カスタムHTMLを使用してリンクやボタンなどのクリックアクションを定義する場合、[JavaScriptブリッジ]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge)を活用してクリックを記録してください。クリックアクションは、ドラッグ＆ドロップエディターのビルド済みコンポーネントを使用した場合にのみ自動で記録されます。
- **プレースメントのリクエスト:** 1回のリフレッシュリクエストで最大10件のプレースメントがSDKに返されます。各プレースメントには、ユーザーが対象となる最も優先度の高いバナーが含まれます。

## Content Cards

### 確認すべきこと
- **Content Cardsのサイズ**: Content Cardsのメッセージフィールドは、圧縮前のサイズで2&nbsp;KBに制限されています。これは、タイトル、メッセージ、画像URL、リンクテキスト、リンクURL、キーと値のペアの各フィールドのバイトサイズの合計で計算されます。このサイズを超えるメッセージは送信されません。これには画像自体のサイズは含まれず、画像URLの長さのみが対象です。
- **送信後のコピー更新**: カードが送信された後、同じカードのコピーを更新することはできません。このシナリオへの対処方法については、[送信済みカードの更新]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#updating-launched-cards)を参照してください。

### 知っておくべきこと
- **アクティブなContent Cardsキャンペーンの上限**: アクティブなContent Cardsキャンペーンは最大500件まで設定できます。このカウントには、いずれかの[カード作成]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card)オプションで送信されたContent Cardsが含まれます。
- [**レポート用語**]({{site.baseurl}}/user_guide/channels/content_cards/reporting): 合計インプレッション数、ユニークインプレッション数、ユニーク受信者数などの用語を確認してください。定義が混乱を招く場合があります。
- **Content Cardsのリフレッシュ**: デフォルトでは、Brazeはセッション開始時の同期、フィードの下スワイプ（モバイル）、および最後のリフレッシュから1分以上経過した場合のカードビュー表示時にContent Cardsリクエストをリフレッシュします。
- **Content Cardsのキャッシュ**: Content Cardsのキャッシュオプションについては、[Android/FireOS]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style)および[Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#getcachedcontentcards)のドキュメントを参照してください。
- **フリークエンシーキャップ**: フリークエンシーキャップはContent Cardsには適用されません。
- **インプレッション**: インプレッションは通常、カードが表示されたときにログに記録されます。例えば、Content Cardsでいっぱいの受信トレイがある場合、ユーザーが特定のContent カードまでスクロールするまでインプレッションはログに記録されません。Web、Android、iOSプラットフォーム間にはいくつかのニュアンスがあります。
- **SDKセッションとカード作成**: SDKセッションのないユーザーに対しては、セグメントの条件を満たしていてもContent Cardsは作成されません。ただし、ユーザーがすでにAndroidセッションを持っている場合、iOS固有のクリックアクションを持つContent Cardsは作成され、ユーザーはiOSでセッションを持った後にそれらのContent Cardsを表示できます。カードが作成されるタイミングの詳細については、[カード作成]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card)を参照してください。

## メール {#email}

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

### 確認すべきこと
- **顧客の同意**: 最初のメールを送信する前に、まず顧客から許可を得ることが重要です。詳細については、[同意とアドレスの収集]({{site.baseurl}}/user_guide/channels/email/email_setup/consent_and_address_collection)および[Braze利用規約](https://www.braze.com/company/legal/aup)を参照してください。
- **想定される送信量**: 単一IPで1日あたり200万通のメールが一般的な推奨量ですが、その送信量が[適切にウォームアップ]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming)されていることが前提です。
  - これよりも多い送信量を継続的に送信する予定がある場合、プロバイダーによるメール受信のスロットリングを避け、ソフトバウンスの増加、配信率の低下、IPレピュテーションの低下を防ぐために、IPプールにまとめた複数のIPアドレスの使用を検討してください。
  - より短い時間枠で送信したい場合は、各プロバイダーがメールを受け入れる速度を調査し、送信元として適切なIPの数を判断することをお勧めします。

### 知っておくべきこと
- **送信量に影響する要因**: IPの送信可能量を決定する要因には、以下のようなものがあります。
  - メールボックス: 大規模なメールプロバイダーは、単一IPから1日あたり数百万通を処理できる可能性がありますが、小規模な地域のメールボックスプロバイダーやインフラの小さいプロバイダーでは、その量を処理できない場合があります。
  - 送信者レピュテーション: 送信者がその送信量までランプアップしており、送信先の各メールボックスやドメインで十分な送信者レピュテーションを持っている場合、単一IPからより多くの量を1日あたり送信できる可能性があります。
- **ベストプラクティス**: Brazeの[メールのベストプラクティス]({{site.baseurl}}/user_guide/channels/email/best_practices)を確認し、配信サービスについて詳しく知りたい場合はBrazeアカウントチームにお問い合わせください。

## アプリ内メッセージ {#in-app-messages}

### 知っておくべきこと
- **アプリ内メッセージのトリガー**:セッション開始時に、SDKは対象となるすべてのアプリ内メッセージをトリガーとともにデバイスに送信するようリクエストします。そのため、ユーザーがセッション中にイベントを実行すると、アプリ内メッセージを迅速かつ確実に受け取ることができます。
- **送信とインプレッション**:アプリ内メッセージでは、「送信」の概念は他の利用可能なチャネルとは異なります。アプリ内メッセージを表示するには、ユーザーがセッションを開始し、対象オーディエンスに含まれ、トリガーを実行する必要があります。このため、より明確な指標として「インプレッション」を追跡しています。
- **トリガー**:デフォルトでは、アプリ内メッセージはSDKによって記録されたイベントでトリガーされます。サーバー送信イベントでアプリ内メッセージをトリガーしたい場合は、[iOS]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=swift)および[Android]({{site.baseurl}}/developer_guide/in_app_messages/customization?sdktab=android)のガイドを参照してください。
- [キャンバスのアプリ内メッセージ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas#advancement-behavior):これらのメッセージは、キャンバスコンポーネント内のスケジュールされたメッセージがユーザーに送信された後、ユーザーがアプリを初めて開いた時（セッション開始でトリガー）に表示されます。
- **Connected Content呼び出し**:Connected Contentを使用すると、メッセージにダイナミックなコンテンツを送信できます。アプリ内メッセージなどのチャネルでメッセージを送信する場合、ユーザーのデバイスへの同時接続が増加する可能性があります（メッセージはバッチではなく1件ずつ送信されます）。これを管理するために、メッセージに[レート制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping)を設定することをお勧めします。

## プッシュ {#push}

### 確認事項
- [**オプトイン/購読済みおよびプッシュ有効**]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states): ユーザーがBrazeからプッシュメッセージを受信するには、購読ステータスがオプトイン（iOS）または購読済み（Android）であり、`Push Enabled = True` である必要があります。Android 13では、プッシュ通知を送信するアプリをユーザーが管理する方法に大きな変更が導入されています。Braze [Android 13 SDKアップグレードガイド]({{site.baseurl}}/developer_guide/platforms/android/android_13)は、新しいAndroid 13ベータ版がリリースされるたびに更新されます。

### 知っておくべきこと
- **Webプッシュ**: Braze [Web SDKの設定]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web)が完了している場合は、Webプッシュを活用してユーザーのエンゲージメントを高めることを検討してください。Webプッシュは、スマートフォンのアプリプッシュ通知と同じように機能します。Webプッシュの作成について詳しくは、[プッシュ通知の作成]({{site.baseurl}}/user_guide/channels/push/create_a_push_message)をご覧ください。
- **単一アプリのターゲティング**: 単一アプリとそのユーザーをターゲティングするには、[セグメンテーションの違い]({{site.baseurl}}/user_guide/get_started/workspaces)を確認してください。

## SMS

### 確認すべきこと
- **割り当てとスループット**: 現在アカウントに紐づいているSMS割り当て（ショートコード、ロングコードなど）と、[それによって提供されるスループット]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup)を把握し、希望する時間内に送信するのに十分なスループットがあることを確認してください。
- **SMSコピーからのセグメント推定**: [SMSセグメント計算ツール]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator)でSMSコピーをテストしてください。SMSセグメント数はスループット能力と合わせて考慮する必要があります。（オーディエンス × SMSセグメント = 必要なスループット）。[超過料金の回避]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs)についてはSMS FAQを参照してください。
- **SMSの法律と規制**: [SMSの法律、規制、不正利用防止]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)を確認し、すべての適用法に準拠してSMSサービスを使用していることを確認してください。送信前に法律顧問の助言を求めることをお勧めします。

### 知っておくべきこと
- **SMSメッセージのデフォルト**: SMSメッセージは通常、送信者プール内のショートコードからデフォルトで送信されます。
- **英数字送信者ID**: 英数字送信者IDを使用すると、双方向メッセージングは機能しなくなります。現在は一方向のみです。
- **米国でのスループットの更新**: 米国では[A2P 10DLC登録](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US)によりスループットが変更されています。トラフィックの混雑やキャリアの問題など、実際の配信率に影響を与える複数の要因があるため、送信速度のSLAを契約上保証していないことにご注意ください。
- **購読グループ**: BrazeでSMSキャンペーンをローンチするには、購読グループを選択する必要があります。また、国際的な[通信コンプライアンスおよびガイドライン]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)を遵守するため、Brazeは[選択された購読グループに登録]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#check-a-users-group)していないユーザーにSMSを送信することはありません。

## WhatsApp

### 知っておくべきこと

- [**ベストプラクティス**]({{site.baseurl}}/user_guide/channels/whatsapp/best_practices): WhatsAppのベストプラクティスに関する推奨事項を確認してください。