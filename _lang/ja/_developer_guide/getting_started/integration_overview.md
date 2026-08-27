---
nav_title: 統合の概要
article_title: 統合の概要
page_order: 2
description: "この記事では、オンボーディングプロセスの基本的な概要を説明します。"
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

# [![Braze Learningコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/sdk-integration-basics){: style="float:right;width:120px;border:0;" class="noimgborder"}はじめに：統合の概要 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomsdk-integration-basics-stylefloatrightwidth120pxborder0-classnoimgbordergetting-started-integration-overview}

> この記事では、オンボーディングプロセスの基本的な概要を説明します。

![発見、統合、品質保証、保守という4つの円のベン図。中心に「価値実現までの時間」が配置されています。]({% image_buster /assets/img/getting-started/getting-started-integrate-flower.png %}){: style="max-width:50%;float:right;margin-left:15px;border:none;"}

技術リソースとして、Brazeを技術スタックに統合することでチームを強化できます。オンボーディングは大きく4つのステップに分けられます。
* [発見と計画](#discovery)：チームと協力してスコープを調整し、データとキャンペーンの構造を計画し、適切なワークスペース構造を作成します。
* [統合](#integration)：SDKとAPIを統合し、メッセージングチャネルを有効にし、データのインポートとエクスポートを設定することで計画を実行します。
* [品質保証](#qa)：Brazeプラットフォームとアプリまたはサイト間のデータとメッセージングのループが期待通りに機能していることを確認します。
* [メンテナンス](#maintenance)：Brazeをマーケティングチームに引き渡した後も、すべてがスムーズに実行されるよう引き続き確認します。

<br>
{% alert tip %}
すべての組織には固有のニーズがあることを認識しており、Brazeはお客様の特定の要件に合わせてカスタマイズできる多様なオプションに対応するよう構築されています。統合にかかる時間はユースケースによって異なります。
{% endalert %}

## 発見と計画 {#discovery}

このフェーズでは、チームと協力してオンボーディングタスクの範囲を設定し、すべての関係者が共通の目標に向けて足並みを揃えていることを確認します。

チームはユースケースのエンドツーエンドの計画を行い、すべてが期待通りに構築でき、そのために適切なデータが利用できることを確認します。このフェーズには、プロジェクトリード、CRMリード、フロントエンドとバックエンドの開発、プロダクトオーナー、マーケターが含まれます。

発見と計画のフェーズには、平均して約6週間かかります。エンジニアリングリードはこのフェーズで週に2〜4時間を費やすことが予想されます。製品に携わる開発者は、発見と計画のフェーズで週に10〜20時間をBrazeに費やすことが予想されます。

{% alert tip %}
御社のオンボーディング期間中、Brazeは技術概要セッションを開催します。エンジニアにはこれらのセッションに参加することを強くお勧めします。技術概要セッションでは、プラットフォームアーキテクチャのスケーラビリティについて話し合ったり、同規模の企業が同様のユースケースで過去にどのように成功したかという実践的な事例を見たりする機会が得られます。
{% endalert %}

![メール、ショッピングカート、画像、ジオロケーションなど、さまざまなチャネルのアイコン。]({% image_buster /assets/img/getting-started/data-graphic-2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

### キャンペーン計画 {#campaign-planning}

CRMチームは、近い将来に立ち上げるメッセージングのユースケースを計画します。これには以下が含まれます。
* [チャネル]({{site.baseurl}}/user_guide/channels)（例：プッシュ通知やアプリ内メッセージ）
* [配信方法]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)（例：スケジュール配信やアクションベースの配信）
* [ターゲットオーディエンス]({{site.baseurl}}/user_guide/audience/segments)
* [成功指標]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)

例えば、新規顧客向けキャンペーンは、昨日最初のセッションを記録した顧客のセグメントに毎日午前10時にメールを送信するものです。コンバージョンイベント（成功指標）はセッションの記録です。

<br>
{% alert important %}
キャンペーン計画のステップが完了するまで、統合を開始することはできません。このステップでは、統合フェーズで構成する必要があるBrazeの構成要素を決定します。
{% endalert %}

### データ要件の作成 {#creating-data-requirements}

次に、CRMチームは計画したキャンペーンを実施するために必要なデータを定義し、データ要件を作成します。

名前、メール、生年月日、国など、多くの一般的なユーザー属性は、Braze SDKが統合された後に自動的にトラッキングされます。その他のタイプのデータはカスタムデータとして定義する必要があります。

開発者として、チームと協力してトラッキングする価値のある追加のカスタムデータを定義します。カスタムデータは、ユーザー群がどのように分類され、セグメント化されるかに影響します。成長スタック全体でイベント分類法を設定し、データがBrazeに出入りする際にシステムとの互換性を確保するよう構造化します。

{% alert tip %}
ツール間でデータの命名法を統一してください。例えば、データウェアハウスは「期間限定オファーの購入」を特定の方法で記録する場合があります。このフォーマットに合わせてBrazeのカスタムイベントが必要かどうかを決める必要があります。
{% endalert %}

[自動収集されたデータとカスタムデータ]({{site.baseurl}}/developer_guide/analytics)の詳細を参照してください。

### カスタマイズの計画 {#customizations-planning}

マーケターに、希望するカスタマイズについて相談してください。例えば、デフォルトのBraze Content Cardsを実装しますか？ブランドガイドラインに合うようにルック＆フィールを少し調整しますか？コンポーネントのためにまったく新しいUIを開発し、Brazeにその分析をトラッキングさせますか？カスタマイズのレベルが異なれば、必要なスコープのレベルも異なります。

### ダッシュボードへのアクセス {#getting-dashboard-access}

Brazeダッシュボードは、ウェブUIインターフェイスです。マーケターはダッシュボードを使って仕事をし、コンテンツを作成します。開発者はダッシュボードを使い、APIキーやプッシュ通知の認証情報など、アプリを統合するための設定を管理します。

チーム管理者は、ダッシュボードであなた（およびBrazeへのアクセスが必要な他のチームメンバー全員）をユーザーとして追加する必要があります。

### ワークスペースとAPIキー {#workspaces-and-api-keys}

チーム管理者はまた、さまざまな[ワークスペース]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces)を作成します。ワークスペースは、ユーザー、セグメント、APIキーなどのデータを1つの場所にグループ化します。ベストプラクティスとして、同じアプリやよく似たアプリの異なるバージョンのみを1つのワークスペースにまとめることをお勧めします。

重要なのは、ワークスペースが複数のプラットフォーム（iOSやAndroidなど）用のAPIキーを提供することです。SDKデータを特定のワークスペースに関連付けるには、対応するAPIキーを使用します。ワークスペースに移動して、各アプリのAPIキーにアクセスしてください。各APIキーがスコープした作業を実行するための正しい権限を持っていることを確認してください。詳細は[APIプロビジョニングの記事]({{site.baseurl}}/api/basics#rest-api-key-permissions)を参照してください。

Web実装が複数のルートドメインにまたがる場合は、1つのアプリを使用するか、別々のアプリとAPIキーを使用するかを決定する際に、[Braze Web SDKのマルチドメイン統合]({{site.baseurl}}/developer_guide/platforms/web/multi_domain_integration)を参照してください。

{% alert important %}
開発用と本番用で異なる環境を設定することが重要です。テスト環境を設定することで、オンボーディングやQAで実際にお金を使うことを防ぐことができます。テスト環境を作成するには、テスト用ワークスペースをセットアップし、本番用ワークスペースにテストデータを入力しないように、必ずそのAPIキーを使用してください。
{% endalert %}

## 統合 {#integration}

![データソースからユーザーデバイスへの情報の流れを表す抽象的なピラミッド図形。]({% image_buster /assets/img/getting-started/data-graphic.png %}){: style="max-width:45%;float:right;margin-left:15px;"}

BrazeはiOSアプリ、Androidアプリ、Webアプリなどをサポートしています。また、React NativeやUnityのようなクロスプラットフォームのラッパーSDKを使用することもできます。通常、顧客は1〜6週間で統合を完了します。多くの顧客は、技術スキルの幅と帯域幅にもよりますが、たった1人のエンジニアでBrazeを統合しています。これは具体的な統合の範囲と、チームがBrazeプロジェクトに費やす時間に完全に依存します。

以下に精通した開発者が必要です。
* アプリやサイトのネイティブレイヤーでの作業
* REST APIにアクセスするプロセスの作成
* 統合テスト
* JSON Webトークン認証
* 一般的なデータ管理スキル
* DNSレコードの設定

### CDP統合パートナー {#cdp-integration-partners}

多くの顧客は、Brazeのオンボーディングを、統合パートナーとして顧客データプラットフォーム（CDP）とも統合する機会として利用しています。Brazeはデータのトラッキングと分析を提供し、CDPは追加のデータルーティングとオーケストレーションを提供できます。Brazeは、[mParticle]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle)や[セグメント]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment)など多くのCDPとシームレスに統合できます。

CDPとサイドバイサイドの統合を行う場合は、CDPのSDKからの呼び出しをBraze SDKにマッピングします。基本的に、以下を実行します。
* 識別呼び出しを`changeUser`（[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html)、[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)/)、[web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)）にマッピングし、属性を設定します。
* データフラッシュ呼び出しを`requestImmediateDataFlush`（[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-immediate-data-flush.html?query=abstract%20fun%20requestImmediateDataFlush())、[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/requestimmediatedataflush())、[web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestimmediatedataflush)）にマッピングします。
* カスタムイベントや購入を記録します。

選択したプラットフォームによっては、Braze SDKと選択したCDP間の統合例を利用できる場合があります。詳細は[CDPテクノロジーパートナーのリスト]({{site.baseurl}}/partners/data_and_analytics)を参照してください。

### Braze SDKの統合 {#braze-sdk-integration}

Braze SDKは2つの重要な機能を提供します。ユーザーデータを収集し統合されたユーザープロファイルに同期することと、プッシュ通知、アプリ内メッセージ、Content Cardsなどのメッセージングチャネルを強化することです。

{% alert tip %}
Braze SDKをアプリやサイトと完全に統合すると、完全に実現されたレベルの高度なマーケティングが可能になります。Braze SDKの統合を延期すると、ドキュメントに記載されている機能の一部が利用できなくなります。
{% endalert %}

{% alert note %}
セキュリティを強化するため、[SDK認証]({{site.baseurl}}/developer_guide/sdk_integration/authentication)を有効にして不正なSDKリクエストを防ぐことができます。この機能は、Web、iOS、Android、React Native、Flutter、Unity、Cordova、.NET MAUI（Xamarin）、Expoを含むすべての主要プラットフォームで利用できます。
{% endalert %}

SDKの実装では、以下を行います。

* サポートしたいプラットフォームごとにSDK統合コードを記述します。
* 各プラットフォームのメッセージングチャネルを有効にし、Braze SDKがメール、SMS、プッシュ通知、その他のチャネルにわたる顧客とのインタラクションのデータをトラッキングするようにします。
* 予定されているUIコンポーネントのカスタマイズ（例：カスタムContent Cards）を作成します。完全にカスタム化されたコンテンツの場合、SDKの自動データ収集では新しいコンポーネントを認識できないため、分析のログを記録する必要があります。この実装はデフォルトのコンポーネントをパターンとして利用できます。

### Braze APIの使用 {#using-the-braze-api}

Brazeを使用している間、さまざまな場面でさまざまなタスクにREST APIを使用します。Braze APIは次のような用途に役立ちます。

1. 過去のデータをインポートする。
2. Brazeではトリガーされない継続的な更新。例えば、アプリにログインせずにユーザープロファイルがVIPにアップグレードされる場合、APIはこの情報をBrazeに伝える必要があります。

[Braze API]({{site.baseurl}}/api/basics)を使い始めましょう。

{% alert important %}
APIを使用する際は、リクエストをバッチ処理し、デルタ値のみを送信するようにしてください。Brazeは送信されたすべての属性を書き直します。カスタム属性の値が変更されていない場合は更新しないでください。
{% endalert %}

### 製品分析の設定 {#setting-up-product-analytics}

Brazeはデータがすべてです。Brazeのデータはユーザープロファイルに保存されます。

データポイントとは、マーケターにとって適切なデータを確実に取得するための仕組みであり、単に「どんな」データでも集めればいいというものではありません。[データポイント]({{site.baseurl}}/user_guide/data/infrastructure/data_points)について理解を深めてください。

### レガシーユーザーデータの移行 {#migrating-legacy-user-data}

Brazeの[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を使用して、Brazeの外部で記録された履歴データを移行できます。よくインポートされるデータの例としては、プッシュトークンや過去の購入履歴などがあります。このエンドポイントは、単発のインポートや定期的なバッチ更新に使用できます。

また、ダッシュボードに一度だけ[CSVをアップロード]({{site.baseurl}}/user_guide/audience/manage_audience/import_users)することで、ユーザーをインポートし、顧客の属性値を更新することもできます。CSVのアップロードはマーケターにとって便利ですが、REST APIを使えばより柔軟に対応できます。

### セッショントラッキングの設定 {#setting-up-session-tracking}

Braze SDKは「セッション開始」と「セッション終了」のデータポイントを生成します。また、Braze SDKは定期的にデータをフラッシュします。セッショントラッキングのデフォルト値（いずれもカスタマイズ可能）については、以下のリンクを参照してください（[Android]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=android)、[iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=swift)、[web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=web)）。

### カスタムイベント、属性、購入イベントのトラッキング {#tracking-custom-events-attributes-and-purchase-events}

カスタムイベント、ユーザー属性、購入イベントなど、計画したデータスキーマを設定するためにチームと調整してください。[カスタムデータスキーム]({{site.baseurl}}/user_guide/data/activation/events/custom_events)はダッシュボードを使用して入力され、SDK統合中に実装したものと完全に一致しなければなりません。

{% alert tip %}
ユーザーID（Brazeでは`external_id`と呼ばれます）は、既知のすべてのユーザーに対して設定する必要があります。これらは不変であるべきで、ユーザーがアプリを開いたときにアクセスできるようにし、デバイスやプラットフォームを超えてユーザーをトラッキングできるようにします。ベストプラクティスについては、[ユーザーライフサイクル]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)の記事を参照してください。
{% endalert %}

### その他のツール {#other-tools}

ユースケースによっては、他にも設定が必要なツールがある場合があります。例えば、ユーザーストーリーを実現するために[ジオフェンス]({{site.baseurl}}/user_guide/audience/locations_and_geofences)のようなツールを設定する必要がある場合があります。重要な統合ステップを完了した後にこれらの追加ツールを設定できる顧客が最も成功していることがわかっています。

## 品質保証 {#qa}
統合を実行する際には、設定したすべてが期待通りに機能していることを確認するため、品質保証を行います。このQAは、データインジェストとメッセージチャネルの2つに大別されます。

{% alert important %}
QAを始める前に、本番環境とテスト環境がセットアップされていることを確認してください。
{% endalert %}

| **QAデータインジェスト**  | **QAメッセージング**                                              |
|---------------------------|---------------------------------------------------------------|
| データのインジェスト、保存、エクスポートの方法について品質保証を行います。 | メッセージがユーザーに正しく送信され、すべてが適切に表示されることを確認します。 |
| データが正しく保存されていることを確認するためにテストを実行します。 | ユーザーのセグメントを作成します。 |
| セッションデータがBraze内の意図したワークスペースに正しく帰属していることを確認します。 | キャンペーンとキャンバスを正常に起動します。 |
| セッションの開始と終了が記録されていることを確認します。 | 正しいキャンペーンが正しいユーザーセグメントに表示されていることを確認します。 |
| ユーザー属性情報がユーザープロファイルに対して正しく記録されていることを確認します。 | プッシュトークンが正しく登録されていることを確認します。 |
| ユーザープロファイルに対してカスタムデータが正しく記録されていることをテストします。 | プッシュトークンが正しく削除されていることを確認します。 |
| 匿名ユーザープロファイルを作成します。 | プッシュキャンペーンがデバイスに正しく送信され、エンゲージメントが記録されているかテストします。 |
| `changeUser()` メソッドが呼び出されたときに、匿名ユーザープロファイルが既知のユーザープロファイルになることを確認します。 | アプリ内メッセージが配信され、指標が記録されることをテストします。 |
|                           | Content Cardsが配信され、指標が記録されていることをテストします。 |
|                           | Connected Contentを活用します（例：AccuWeather）。 |
|                           | すべてのメッセージチャネルの統合が正しく連携していることを確認します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="品質保証" }

{% alert note %}
SDK統合のQAを行う際、[SDKデバッガー]({{site.baseurl}}/developer_guide/sdk_integration/debugging)を使用すれば、アプリの冗長ロギングをオンにすることなく問題のトラブルシューティングを行うことができます。
{% endalert %}

### Brazeをマーケターに引き継ぐ {#passing-braze-off-to-marketers}

プラットフォームやサイトを統合したら、マーケティングチームを関与させてプラットフォームの所有権を引き渡しましょう。このプロセスは企業によって異なりますが、以下のようなものが含まれる場合があります。

* 複雑な[Liquidロジック]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)を構成する
* [メールのIPウォームアップ]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming)を支援する
* 他の利害関係者にトラッキングされるデータの種類を理解させる

### 未来のために開発する {#develop-for-the-future}

コードベースを受け継いだが、最初の開発者が何を考えていたのかまったく分からなかったことはありませんか？さらに悪いことに、コードを書いて完全に理解したのに、1年後にそのコードに戻ってきたときにまったく不可解に感じたことはありませんか？

Brazeのオンボーディング時には、データ、ユーザープロファイル、対象となる統合と対象外の統合、カスタマイズの動作方法などに関して下した決断の積み重ねが新鮮に感じられ、それゆえに明白なものとなります。チームがBrazeを拡張したいとき、または他の技術リソースがBrazeプロジェクトに割り当てられたとき、この情報は不明瞭になります。

技術概要セッションで学んだ情報を定着させるためのリソースを作成してください。このリソースは、チームに加わる新しい開発者をオンボードする時間を短縮するのに役立ちます（あるいは、現在のBraze実装を拡張する必要があるときに自分自身へのリマインダーとして役立ちます）。

## メンテナンス {#maintenance}

マーケターに引き継がれた後も、メンテナンスのためのリソースとしての役割を果たし続けます。Braze SDKに影響を与える可能性のあるiOSとAndroidのアップデートに注意を払い、サードパーティベンダーが最新であることを確認してください。

Brazeの[GitHub](https://github.com/braze-inc/)を通じて、Brazeプラットフォームへの更新を追跡します。時折、緊急アップデートやバグフィックスに関するメールがBrazeから管理者に直接届くこともあります。

## SDKレート制限 {#sdk-rate-limits}

### Monthly Active Users CY 24-25、Universal MAU、Web MAU、Mobile MAU {#monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau}

Monthly Active Users CY 24-25、Universal MAU、Web MAU、Mobile MAUを購入されたお客様に対して、Brazeは当社SDKが使用するAPIリクエスト（セッション、ユーザー属性、イベント、その他のユーザープロファイルデータの更新）にサーバー側のレート制限を適用しています。これはプラットフォームの安定性を確保し、高速で信頼性の高いサービスを維持するためです。

* 時間あたりのレート制限は、アカウントで予想されるSDKトラフィックに基づいて設定されます。これは、購入された月間アクティブユーザー（MAU）数、業界、季節性、その他の要因に対応する場合があります。時間あたりのレート制限に達すると、Brazeは次の1時間までリクエストをスロットルします。
* レート制限されたすべてのリクエストは、SDKにより自動的にリトライされます。
* SDKリクエストは、実装で収集されるカスタムデータの量に相関します。時間あたりのレート制限に常に近づいている、または達している場合は、以下を検討してください。
    * SDK統合を見直して、過剰なデータ収集を削減する。
    * マーケティングのユースケースに不可欠でないカスタムデータをブロックリストに追加する。
* バーストレート制限は、非常に短い期間（つまり数秒以内）に大量のリクエストが到着した場合に適用される短期間のレート制限です。バースト制限が発生した場合、対応は不要で、SDKがすぐにリトライします。
* 定常レート制限は、バーストウィンドウよりも長いローリングウィンドウ（たとえば数分間）にわたる持続的なリクエスト量を制御し、バーストレート制限と時間あたりのレート制限の間で進行中のトラフィックを平滑化します。

### レート制限の確認 {#finding-your-rate-limits}

予想されるSDKスループットに基づく現在の制限を確認するには、**設定** > **APIと識別子** > **APIとSDKの制限**に移動します。

過去の使用状況については、**設定** > **APIと識別子** > **APIとSDKダッシュボード**に移動します。

### より高いレート制限のリクエスト {#requesting-higher-rate-limits}

Brazeのレート制限の引き上げが必要な場合は、Brazeサポートまたはカスタマーサクセスマネージャーに連絡し、以下の詳細を含めてください。

* 一時的な引き上げが必要か、恒久的な引き上げが必要か。
* 引き上げが必要な理由。
* 影響を受けるエンドポイントと環境。
* おおよそのトラフィック量とタイムライン（開始日、期間、ピーク時間を含む）。
* コールをバッチ処理したり、トラフィックを時間的に分散させることが可能か。

リクエストを送信後、Brazeが内容を確認し、結果をお知らせします。

### 変更とサポート {#changes-and-support}

Brazeは、システムの安定性を保護するため、またはアカウントのデータスループットの増加に対応するために、レート制限を変更する場合があります。レート制限とそのビジネスへの影響に関するご質問やご懸念については、Brazeサポートまたはカスタマーサクセスマネージャーにお問い合わせください。