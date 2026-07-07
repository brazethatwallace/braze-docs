---
nav_title: プラットフォームの概要
article_title: プラットフォームの概要
page_order: 1
description: "この記事では、Brazeプラットフォームの基本的なパーツと機能について説明します。この記事からのリンクは、Brazeの重要なトピックにつながっています。"
platform:
  - iOS
  - Android
  - Web
  - React Native
  - Flutter
  - Cordova
  - Roku
  - Swift
  - Unity
---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/developer){: style="float:right;width:120px;border:0;" class="noimgborder"}はじめに：プラットフォームの概要 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecompathdeveloper-stylefloatrightwidth120pxborder0-classnoimgbordergetting-started-platform-overview}

> この記事では、Brazeプラットフォームの基本的なパーツと機能について説明します。この記事からのリンクは、Brazeの重要なトピックにつながっています。

{% alert tip %}
これらの記事とあわせて、無料の[開発者ラーニングパス](https://learning.braze.com/path/developer)コースもぜひご覧ください。
{% endalert %}

## Brazeとは {#what-is-braze}

Brazeはカスタマーエンゲージメントプラットフォームです。ユーザーデータを取り込み、ユーザーのアクションや行動を可視化し、それらに基づいてアクションを実行できるようにします。このプラットフォームは主に3つの構成要素から成っています：SDK、ダッシュボード、そしてREST APIです。

Brazeのより一般的な概要を知りたいマーケターの方は、代わりに[マーケター向けの「はじめに」セクション]({{site.baseurl}}/user_guide/get_started)をご覧ください。

![Brazeにはさまざまなレイヤーがあります。全体として、SDK、API、ダッシュボード、およびパートナー連携から構成されています。これらはそれぞれ、データインジェストレイヤー、分類レイヤー、オーケストレーションレイヤー、パーソナライゼーションレイヤー、およびアクションレイヤーの一部を構成します。アクションレイヤーには、プッシュ、アプリ内メッセージ、コネクテッドカタログ、Webhook、SMS、メールなど、さまざまなチャネルがあります。]({% image_buster /assets/img/getting-started/getting-started-vertically-integrated-stack.png %}){: style="max-width:55%;float:right;margin-left:15px;"}

### SDK

[Braze SDK](#integrating-braze)をモバイルアプリケーションおよびWebアプリケーションに統合して、強力なマーケティング、ユーザー管理、および分析ツールを提供できます。

つまり、完全に統合されると、SDKは次を行います。

* ユーザーデータを収集し、統合されたユーザープロファイルに同期します
* セッションデータ、デバイス情報、プッシュトークンを自動的に収集します
* マーケティングエンゲージメントデータとお客様のビジネスに特化したカスタムデータを取得します
* セキュリティを重視した設計で、サードパーティによる侵入テストが実施されています
* 低バッテリーや低速ネットワークのデバイスに最適化されています
* セキュリティを強化するため、サーバー側のJWT署名をサポートします
* システムへの書き込み専用アクセス権を持ちます（ユーザーデータを取得できません）
* プッシュ通知、アプリ内メッセージ、Content Cardsのメッセージングチャネルを強化します

### ダッシュボードのユーザーインターフェイス {#dashboard-user-interface}

ダッシュボードは、Brazeプラットフォームの中心にあるすべてのデータとインタラクションを制御するUIです。マーケターはダッシュボードを使って業務を行い、コンテンツを作成します。開発者はダッシュボードを使い、APIキーやプッシュ通知の認証情報など、アプリを統合するための設定を管理します。

始めたばかりの場合は、チーム管理者がダッシュボードであなた（およびBrazeへのアクセスが必要な他のチームメンバー全員）を[ユーザーとして追加]({{site.baseurl}}/user_guide/administer/personal)する必要があります。

### REST API

Braze APIを使えば、Brazeからデータを大規模に出し入れすることができます。APIを使用して、バックエンド、データウェアハウス、その他のファーストパーティソースおよびサードパーティソースから更新を取り込みます。さらに、APIを使って、Webベースのアプリケーションから直接、セグメンテーション目的のカスタムイベントを追加することもできます。APIを通じてメッセージをトリガーしたり送信したりできるので、テクニカルリソースはキャンペーンの一部として複雑なJSONメタデータを含めることができます。

また、このAPIは、モバイルおよびWeb SDKを経由せず、HTTP経由で直接ユーザーが実行したアクションを記録できるWebサービスも提供します。webhookと組み合わせることで、アプリ体験の内外でユーザーのアクションを追跡し、アクティビティをトリガーできます。[APIガイド]({{site.baseurl}}/api/home)には、利用可能なBraze APIエンドポイントとその用途が記載されています。

Brazeの構成要素については、以下を確認してください：[はじめに：アーキテクチャの概要]({{site.baseurl}}/developer_guide/getting_started/architecture_overview)

## データ分析とアクション {#data-analysis-and-action}

Brazeに保存されたデータは、Brazeの顧客である限り保持され、セグメンテーション、パーソナライゼーション、およびターゲティングに使用できます。これにより、その情報を廃止することを選択するまで、ユーザープロファイルデータ（たとえば、セッションアクティビティや購入）に対して操作を行うことができます。例えば、ストリーミングサービスは、各サブスクライバーがサービス利用開始日から（それが何年も前であっても）視聴したコンテンツを追跡し、そのデータを使用して関連するメッセージングを強化できます。

![Brazeダッシュボードにある「最近の購入者」というセグメントと、「リンダへのおすすめ」というメールが表示された電話画面が並んでいる。]({% image_buster /assets/img/getting-started/getting-started-segment.png %}){: style="max-width:80%"}

### アプリ分析 {#app-analytics}

Brazeダッシュボードは、分析指標と設定したカスタムイベントに基づき、リアルタイムで更新されるグラフを表示します。ABテスト、カスタムレポート、分析、自動インテリジェンスを用いた一貫した測定と最適化は、カスタマーエンゲージメントと差別化を支援します。

### ユーザーセグメンテーション {#user-segmentation}

セグメンテーションを利用することで、アプリ内での行動やユーザー層データなどの強力なフィルターに基づいて、ユーザーのグループを作成できます。また、Brazeでは、希望するアクションがデフォルトでキャプチャされない場合、任意のアプリ内ユーザーアクションを「カスタムイベント」として定義できます。同じことが、「カスタム属性」によるユーザー特性にも当てはまります。ダッシュボード上でユーザーセグメントが作成されると、ユーザーは定義された基準を満たす（または満たさない）ごとにセグメントを出たり入ったりします。例えば、アプリ内でお金を使い、最後にアプリを使ったのが2週間以上前であるすべてのユーザーを含むセグメントを作成できます。

データモデルについては、こちらをご覧ください：[はじめに：分析の概要]({{site.baseurl}}/developer_guide/getting_started/architecture_overview)

## マルチチャネルメッセージング {#multichannel-messaging}

セグメントを定義した後、Brazeのメッセージングツールを使えば、ダイナミックでパーソナライズされた方法でユーザーに働きかけることができます。Brazeはチャネルにとらわれないユーザー中心のデータモデルで設計されています。メッセージングは、アプリやサイトの内部（アプリ内メッセージの送信や、Content Cardsのカルーセルやバナーなどのグラフィック要素）で行われることもあれば、アプリの外部（プッシュ通知やメールの送信など）で行われることもあります。例えば、マーケターは、前のセクションで定義した例のセグメントにプッシュ通知とメールを送ることができます。

![アプリやWebサイトの外でも内でも、あらゆるチャネルでパーソナライズされたメッセージを作成し、トリガーする。]({% image_buster /assets/img/getting-started/messaging-channels.png %}){: style="border:none" }

| チャネル                                                                                              | 説明                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)* | 顧客の作業を中断することなく、高度にターゲットを絞ったダイナミックなアプリ内通知を送信します。 |
| [メール]({{site.baseurl}}/user_guide/channels/email) | リッチテキストエディター、ドラッグ＆ドロップエディター、または既存のHTMLテンプレートをアップロードしてメールを作成し、リッチなHTMLメッセージを送信します。 |
| [アプリ内メッセージ]({{site.baseurl}}/in-app_messages) | Brazeが独自に構築したネイティブユーザーインターフェイスを使用して、控えめなアプリ内通知を送信します。 |
| [プッシュ]({{site.baseurl}}/user_guide/channels/push) | iOS用のApple Push Notification Service（APNs）またはAndroid用のFirebase Cloud Messaging（FCM）を使用して、メッセージングキャンペーンまたはニュースアイテムから自動的にプッシュ通知をトリガーします。 |
| [SMS、MMS、およびRCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs)* | SMS、MMS、またはRCSを使用して、取引通知、プロモーションの共有、リマインダーの送信などを行います。 |
| [Webプッシュ]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web) | ユーザーが現在サイトでアクティブでない場合でも、Webブラウザー通知を送信します。 |
| [Webhook]({{site.baseurl}}/about_webhooks) | webhookを使ってアプリ以外のアクションをトリガーし、他のシステムやアプリケーションにリアルタイムデータを提供します。 |
| [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)* | 広く普及しているピアツーピアメッセージングプラットフォームであるWhatsAppを活用して、ユーザーや顧客と直接つながります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="マルチチャネルメッセージング" }

<sup>*アドオン機能として利用できます。*</sup>

### カスタマイズ可能なコンポーネント {#customizable-components}

{% gallery %}
{{site.baseurl}}/assets/img/getting-started/crawl-example.png <br> すべてのBrazeコンポーネントは、アクセシブルで、適応性があり、カスタマイズできるように作られています。Brazeを使い始めるには、デフォルトの `BrazeUI` コンポーネントを使用し、ブランドのニーズやユースケースに合わせてカスタマイズします。
{{site.baseurl}}/assets/img/getting-started/walk-example.png <br> デフォルトのオプションを超えるために、カスタムコードを書いて、メッセージチャネルのルック＆フィールをよりブランドに近いものに更新できます。これには、コンポーネントのフォントタイプ、フォントサイズ、色の変更も含まれます。マーケターは、Brazeダッシュボードで直接、オーディエンス、コンテンツ、クリック行動、有効期限をコントロールできます。
{{site.baseurl}}/assets/img/getting-started/run-example.png <br> また、完全にカスタムのコンポーネントを作成して、メッセージングの外観、動作、および他のメッセージングチャネルとの連携方法（プッシュ通知に基づいてContent Cardsをトリガーするなど）をコントロールすることもできます。BrazeにはSDKメソッドが用意されており、Brazeダッシュボードでインプレッション数、クリック数、閉じた回数などの指標を記録できます。各メッセージングチャネルには、これを容易にするための分析記事があります。
{% endgallery %}

<br>
<br>

## Brazeを統合する {#integrating-braze}

Brazeは迅速な統合のために設計されています。顧客ベース全体での平均的な価値実現までの期間は6週間です。統合プロセスに関する詳細は、[はじめに：統合の概要]({{site.baseurl}}/developer_guide/getting_started/integration_overview)を参照してください。

## ブックマークすべきリソース {#resources-to-bookmark}

テクニカルリソースとして、Brazeの肝心な部分の多くに携わることになります。ドキュメント以外でブックマークしておくとよいリソースを以下に紹介します。今後、Brazeの用語について質問がある場合は、[用語集]({{site.baseurl}}/user_guide/get_started/terms_to_know)を手元に置いておくとよいでしょう。

| リソース | 学べる内容 |
|---|---|
| [SDKのデバッグ]({{site.baseurl}}/developer_guide/sdk_integration/debugging) | 統合をトラブルシューティングする際には、SDKデバッグツールが役に立ちます。必ず手元に置いておきましょう。 |
| [Braze Public GitHub](https://github.com/braze-inc/) | 統合に関する詳細な情報とサンプルコードについては、GitHubリポジトリを参照してください。 |
| [Android SDK GitHubリポジトリ](https://github.com/braze-inc/braze-android-sdk/) | Android SDKのGitHubリポジトリです。 |
| [Android SDKリファレンス](https://appboy.github.io/appboy-android-sdk/kdoc/index.html) | Android SDKのクラスドキュメントです。 |
| [iOS（Swift）SDK GitHubリポジトリ](https://github.com/braze-inc/braze-swift-sdk) | Swift SDKのGitHubリポジトリです。 |
| [iOS（Swift）SDKリファレンス](https://braze-inc.github.io/braze-swift-sdk/) | iOS SDKのクラスドキュメントです。 |
| [Web SDK GitHubリポジトリ](https://github.com/braze-inc/braze-web-sdk) | Web SDKのGitHubリポジトリです。 |
| [Web SDKリファレンス](https://js.appboycdn.com/web-sdk/5.0/doc/modules/braze.html) | iOS SDKのクラスドキュメントです。 |
| [SDK変更ログ]({{site.baseurl}}/developer_guide/changelogs) | Brazeは、重要な問題や主要なOS更新のリリースに加えて、予測可能な毎月のリリースを提供しています。 |
| [Braze API Postman Collection](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest) | Postman Collectionはこちらからダウンロードできます。  |
| [Braze System Status Monitor](https://braze.statuspage.io/) | ステータスページは、インシデントや障害が発生するたびに更新されます。アラートをサブスクライブするには、このページにアクセスしてください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ブックマークすべきリソース" }