---
nav_title: Braze Pilot
page_order: 10.5
layout: dev_guide
guide_top_header: "Braze Pilot"
guide_top_text: "Braze Pilotは、Brazeダッシュボードとシームレスに接続するように設計されたモバイルアプリです。これにより、アプリにCampaignsやCanvasesを配信でき、自分のスマートフォン上でBrazeのメッセージを実際に体験できます。Braze Pilotには、さまざまな業界を代表する架空ブランド向けのアプリシミュレーションのライブラリーが含まれており、顧客の視点からメッセージングがどのように見えるかを体験できます。"
description: "Brazeダッシュボードからスマートフォンにメッセージを送信するさまざまな方法をご確認ください。"

guide_featured_title: "セクションの記事"
guide_featured_list:
  - name: Braze Pilotを始める
    link: /docs/user_guide/get_started/braze_pilot/getting_started
    image: /assets/img/braze_icons/brush-02.svg
  - name: データ辞書
    link: /docs/user_guide/get_started/braze_pilot/data_dictionary
    image: /assets/img/braze_icons/book-closed.svg
  - name: ナビゲーションディープリンク
    link: /docs/user_guide/get_started/braze_pilot/deep_links
    image: /assets/img/braze_icons/link-03.svg

---

## Pilotアプリのシミュレーション {#pilot-app-simulations}

Braze Pilotの中核は、アプリシミュレーションのライブラリーです。各アプリは業界特化型の架空ブランドをリアルにシミュレートしたもので、豊富なイベントや属性を記録する仕組みを備えています。これにより、Brazeの一般的なユースケースを実現する無限の可能性が生まれます。

{% tabs local %}
{% tab Fitness %}

### Steppington

Steppingtonは、ワークアウトや運動目標、そしてSteppington+プレミアムサービスを備えたフィットネスアプリです。[Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)を表示する複数の場所を提供し、[フィーチャーフラグ]({{site.baseurl}}/developer_guide/feature_flags)で表示可能なセクションを備え、さらに豊富なカスタムイベントロギングのライブラリーにより、この業界におけるさまざまなカスタマージャーニーを可視化できます。

![Steppingtonのホームページには、マラソントレーニング、ヨガ、サイクリング、ウェイトトレーニングのアイコンがあります。]({% image_buster /assets/img/braze_pilot/steppington_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab eCommerce %}

### PantsLabyrinth

PantsLabyrinthは、パンツを販売するeコマースアプリです（ご想像の通り！）。PantsLabyrinthアプリには、ショッピングカートの決済機能、フィーチャーフラグで有効化できるオプションのウィッシュリスト機能、そして英国の友人たちとユーモアを楽しむ機会が数多く含まれています。

![PantsLabyrinthの商品ページで、ジーンズをカートに追加するオプションがあります。]({% image_buster /assets/img/braze_pilot/pantslabyrinth_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab Streaming %}

### MovieCanon

MovieCanonは、コンテンツエンゲージメントに関するBrazeの一般的なユースケースを説明するために最適に設計されたストリーミングサービスです。

![さまざまなスリラー映画が視聴できるMovieCanonアプリ。]({% image_buster /assets/img/braze_pilot/moviecanon_app.png %}){:style="max-width:50%"}

{% endtab %}
{% endtabs %}

## PilotがBrazeダッシュボードと接続する仕組み {#how-pilot-connects-with-your-braze-dashboard}

Braze SDKは、アプリやWebサイトに統合されると、ユーザーからデータを収集するコードパッケージです。Pilotをダッシュボードに接続すると、スマートフォン上のPilotアプリとBraze SDK間の接続が初期化されます。さらに、ダッシュボードのAPIキー識別子をPilotに提供することで、Brazeインスタンスとの固有の接続が確立されます。

![Pilotセットアップの最初のステップ。]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

PilotがBrazeダッシュボードに接続された後、アプリ内のBraze SDKは、自社のアプリやWebサイトにSDKを統合した場合と同様に機能します。つまり、Brazeは以下を行います。

- Pilotでのユーザーアクティビティデータを保存します。これにはアプリ内の架空ブランド固有のカスタムデータも含まれます。
- セッションデータ、デバイス情報、プッシュトークンを自動的に収集します。
- SDK統合が必要なプッシュ通知、In-App Messages、Content Cardsのメッセージングチャネルを動作させます。

Braze SDKの詳細については、[統合]({{site.baseurl}}/user_guide/get_started/integrations)をご確認ください。

![Brazeのカスタマーエンゲージメントスタックは、データ取り込み、分類、オーケストレーション、パーソナライゼーション、アクションのための統合、API、SDKを含み、顧客との双方向フィードバックループを実現するメッセージングチャネルを備えています。]({% image_buster /assets/img/braze_pilot/braze_sdk_diagram.png %}){:style="max-width:70%"}

## Brazeのユーザープロファイル {#user-profiles-in-braze}

Brazeに送信されるすべてのデータは、アプリやWebサイトの特定のユーザーに紐づくユーザープロファイルに保存されます。PilotをBrazeダッシュボードに接続すると、BrazeはPilotのユーザーであるあなたに関するデータの記録を開始します。この接続を通じて作成されるユーザーには、匿名ユーザーと識別済みユーザーの2種類があります。

### 匿名 {#anonymous}

この接続ステータスは、まだログインしていないアプリやWebサイトのゲストの体験を表しています。Pilotを匿名ユーザーとして初期化すると、Brazeは[匿名ユーザープロファイル]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users)を作成し、そのプロファイルにアクティビティデータを記録します。匿名ユーザーもCampaignsのターゲットにすることはできますが、Brazeダッシュボードで直接そのユーザープロファイルを検索することはできません。

### 識別済み {#identified}

この接続ステータスは、Brazeがあなたに割り当てられた一意の識別子（external IDと呼ばれる）を通じて、あなたのユーザープロファイルを認識していることを意味します。ダッシュボードの**ユーザー検索**ページでこのexternal IDを検索すれば、ユーザープロファイルを見つけることができます。そこには、アプリ内でのアクティビティに基づいてPilotから記録されたすべてのユーザー属性とイベントが保存されています。Brazeダッシュボードで**Audience** > **ユーザー検索**に移動し、Pilotの**external ID**を入力してプロファイルを開き、属性とイベントを確認します。

### 接続タイプ {#connection-type}

接続の種類を確認するには、Pilotアプリの右上にある接続ステータス表示を確認してください。

{% tabs local %}
{% tab 匿名ユーザー %}

**匿名**は、匿名ユーザーとしてデータを記録していることを示します。ステータス領域には**匿名**ラベル（マスクやシークレットモード風のアイコンなど）が表示されます。

{% endtab %}
{% tab 識別済みユーザー %}

識別済みユーザーとしてデータを記録している場合、ステータス領域には**識別済みユーザー**とexternal IDが表示されます。

{% endtab %}
{% tab 未接続 %}

**未接続**は、まだBraze SDKとPilotの接続を初期化していないことを示します。ステータス領域では、PilotがまだBrazeワークスペースに接続されていないことが示されます。

{% endtab %}
{% endtabs %}

## CampaignsとCanvases {#campaigns-and-canvases}

CampaignsとCanvasesは、ユーザーにメッセージを送信する手段です。

- Campaignsは、さまざまなチャネルにわたって特定のオーディエンスセグメントに送信する単一のメッセージに最適です。
- Canvasesは、複数のチャネルにわたってパーソナライズされたカスタマージャーニーを自動化およびオーケストレーションできる高度なワークフローです。Canvas内では、分岐ロジック、遅延、決定ポイント、コンバージョンイベントを設定して、一連のインタラクションを通じて顧客を導くことができます。Canvasesは、異なるタッチポイント間で一貫性のあるシームレスなコミュニケーションを確保し、カスタマーエンゲージメントとコンバージョンの可能性を高めます。

## サポートされているメッセージングチャネル {#supported-messaging-channels}

Braze Pilotは現在、[アプリ内メッセージ]({{site.baseurl}}/in-app_messages)をサポートしています。アプリ内メッセージはアプリ内に表示され、ユーザーが積極的にエンゲージメントを行っている最中にタイムリーなメッセージを届けます。

![MovieCanonアプリのアプリ内メッセージ「MovieCanonを楽しんでいますか？友達を紹介しよう！」と表示され、紹介メールを送るためのメールアドレス入力欄があります。]({% image_buster /assets/img/braze_pilot/moviecanon_iam.png %}){:style="max-width:40%"}