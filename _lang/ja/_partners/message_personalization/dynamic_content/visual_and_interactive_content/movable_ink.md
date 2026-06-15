---
title: "Movable Ink"
article_title: Movable Ink
alias: "/partners/movable_ink/"
description: "このリファレンス記事では、Braze と Movable Ink のパートナーシップについて説明します。Movable Ink は、顧客に印象づける説得力のある独特なビジュアルエクスペリエンスを作成できる手段をデジタルマーケターに提供するクラウドベースのソフトウェアプラットフォームです。"
page_type: partner
search_tag: Partner

---

# Movable Ink

> [Movable Ink](https://www.movableink.com/) は、顧客に印象づける説得力のある独特なビジュアルエクスペリエンスを作成できる手段をデジタルマーケターに提供するクラウドベースのソフトウェアプラットフォームです。Movable Ink プラットフォームは、キャンペーンに簡単に挿入できる有用なカスタマイズオプションを提供します。

_この統合は Movable Ink によって管理されます。_

## 統合について {#about-the-integration}

ポーリング、カウントダウンタイマー、スクラッチオフなど、Movable Ink の Intelligent Creative 機能を活用して Braze のクリエイティブ機能を拡大します。Movable Ink と Braze の統合により、ダイナミックなデータドリブン型のメッセージへのよりバランスの取れたアプローチを可能にし、重要な事柄に関するリアルタイムの要素をユーザーに提供します。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Movable Ink アカウント | このパートナーシップを活用するには、Movable Ink アカウントが必要です。 |
| データソース | データソースを Movable Ink に接続する必要があります。これは、CSV、Web サイトインポート、または API を使用して実行できます。Braze と Movable Ink の間で統一識別子（`external_id` など）を使用してデータを渡していることを確認してください。
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## ユースケース {#use-cases}

- パーソナライズされた月ごとの要約または年末の要約。
- 直近の既知の動作に基づいて、メール、プッシュ、またはリッチプッシュ通知に使用される画像をダイナミックにパーソナライズします。<br>
	以下に例を示します。
	- リッチプッシュメッセージを使用して、API からデータを取得してイベントのスケジュールを動的に作成します。
	- 大規模なセール（ブラックフライデー、バレンタインデー、祝日セールなど）が近づいているときに、カウントダウンタイマーを使用してユーザーに通知します。
	- プロモーションコードを配信する楽しくインタラクティブな方法として、スクラッチオフ機能を使用します。

## サポートされている Movable Ink の機能 {#supported-movable-ink-capabilities}

Intelligent Creative には、会社ユーザーが利用できる多くのサービスがあります。次のリストに、サポートされている機能を示します。

| Movable Ink の機能 | 機能 | リッチプッシュ通知 | アプリ内メッセージ / Content Cards / メール | 詳細 |
| ---------------------- |---| ---------------------- | -------------------------------- | ------- |
| クリエイティブオプティマイザー | A/B コンテンツの表示 | ✗ | ✔ | |
| 最適化 | ✗ | ✔* | * Branch のディープリンクソリューションを使用する必要があります |
| ターゲティングルール | 日付 | ✔* | ✔ | * プッシュ通知は受信時にキャッシュされ、更新されないため、サポートされますが推奨されません |
| 曜日 | ✔* | ✔ | * プッシュ通知は受信時にキャッシュされ、更新されないため、サポートされますが推奨されません |
| 時刻 | ✔* | ✔ | * プッシュ通知は受信時にキャッシュされ、更新されないため、サポートされますが推奨されません |
| ストーリー/行動アクティビティ | | ✔* | ✔* | * Brazeに使用されるユニークユーザー識別子を、メールサービスプロバイダー (ESP) の識別子にリンクする必要があります |
| アプリ内のディープリンク | | ✔* | ✔* | * 顧客に効率化されたエクスペリエンスを提供するには、Branch で確立されたディープリンクソリューションを使用するか、Movable Ink のクライアントエクスペリエンスチームによる検証済みソリューションを使用します。 |
| アプリ | カウントダウンタイマー | ✔* | ✔ | * プッシュ通知は受信時にキャッシュされ、更新されないため、サポートされますが推奨されません |
| ポーリング | ✗ | ✔* | * 投票後、アプリを離れてモバイルランディングページに遷移します |
| スクラッチオフ | ✔* | ✔* | * クリックすると、スクラッチオフエクスペリエンスのためにアプリを離れます |
| 動画 | ✔* | ✔* | * アニメーション GIF のみ。<br>Android の場合、Braze の実装には [GIF サポート]({{site.baseurl}}/developer_guide/in_app_messages/gifs/?sdktab=android)が必要です |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Supported Movable Ink capabilities" }

## 統合 {#integration}

### ステップ1:Movable Ink のデータソースを作成する {#step-1-create-a-data-source-for-movable-ink}

CSV、Web サイトインポート、または API 統合のいずれかのデータソースを作成する必要があります。

![表示されるさまざまなデータソースオプション:CSV アップロード、Web サイト、または API 統合。]({% image_buster /assets/img/movable_ink/movable_ink1.png %})

{% tabs local %}
{% tab CSV データソース %}
- **CSV データソース**:各行には、少なくとも1つのセグメント列と1つのコンテンツ列が必要です。CSV がアップロードされた後、コンテンツのターゲットとして使用する列を選択します。[CSV ファイルの例]({% image_buster /assets/download_file/movable_ink_CSV.csv %})

![「CSV」をデータソースとして選択したときに表示されるフィールド。]({% image_buster /assets/img/movable_ink/movable_ink2.png %})
{% endtab %}
{% tab Web サイトデータソース %}
- **Web サイトデータソース**:各行には、少なくとも1つのセグメント列と1つのコンテンツ列が必要です。CSV がアップロードされたら、コンテンツのターゲットを設定するために使用する列を選択します。
  - このプロセスでは、以下をマッピングする必要があります。
    - セグメントとして使用されるフィールド
    - クリエイティブで動的にパーソナライズできるデータフィールドとして使用する項目（たとえば、ユーザー属性や名、姓、市区町村などのカスタム属性）

![「Web サイト」をデータソースとして選択したときに表示されるフィールド。]({% image_buster /assets/img/movable_ink/movable_ink3.png %})
{% endtab %}
{% tab API 統合 %}
- **API 統合**:自社の API を使用して、API レスポンスから直接コンテンツを供給します。

![「API 統合」をデータソースとして選択したときに表示されるフィールド]({% image_buster /assets/img/movable_ink/movable_ink4.png %})
{% endtab %}
{% endtabs %}

### ステップ2:Movable Ink プラットフォームでキャンペーンを作成する {#step-2-create-a-campaign-on-the-movable-ink-platform}

Movable Ink のホーム画面から、キャンペーンを作成します。HTML からのメール、画像からのメール、または任意のチャネルで使用できるブロック（プッシュ、アプリ内メッセージ、Content Cards（推奨）など）のいずれかを選択できます。

また、ブロックを通じて利用できるさまざまなコンテンツオプションを確認することもお勧めします。

![新しい Movable Ink キャンペーンを作成するときの Movable Ink プラットフォームの外観。]({% image_buster /assets/img/movable_ink/movable_ink5.png %}){: style="max-width:70%"}

Movable Ink には、テキストや画像などの要素をドラッグ＆ドロップできる簡単なエディターがあります。データソースを入力した場合は、データプロパティを使用して画像をダイナミックに生成できます。また、このフロー内にフォールバックを作成することもできます。これは、キャンペーンが送信され、ユーザーがパーソナライゼーション基準に該当しない場合に使用されます。

![Movable Ink ブロックエディターに表示されるカスタマイズ可能なさまざまな要素。]({% image_buster /assets/img/movable_ink/create_campaign2.png %})

キャンペーンを完了する前に、ダイナミックな画像をプレビューし、クエリパラメーターをテストして、表示時に画像がどのように見えるかを確認してください。完了すると、Braze に挿入できるダイナミック URL が生成されます。

Movable Ink プラットフォームの使用方法の詳細については、[Movable Ink サポートセンター](https://support.movableink.com/)を参照してください。

### ステップ3:Movable Ink コンテンツ URL を取得する {#step-3-obtain-movable-ink-content-url}

Movable Ink のコンテンツを Braze メッセージに含めるには、Movable Ink から提供されたソース URL を確認する必要があります。

ソース URL を取得するには、Movable Ink ダッシュボードでコンテンツを設定し、完了してコンテンツをエクスポートする必要があります。**Finish** ページで、クリエイティブタグからソース URL（`img src`）をコピーします。

![Movable Ink キャンペーンを完了すると表示されるページ。ここにコンテンツ URL が表示されます。]({% image_buster /assets/img/movable_ink/obtain_url.png %}){: style="max-width:80%;"}

次に Braze プラットフォームで、URL を該当するフィールドに貼り付けます。メッセージングチャネルに適したフィールドは、ステップ4に記載されています。最後に、マージタグ（{% raw %}`&mi_u=%%email%%`{% endraw %} など）を対応する Liquid 変数（{% raw %}`&mi_u={{${email_address}}}`{% endraw %} など）に置き換えます。

### ステップ4:Braze エクスペリエンス {#step-4-braze-experience}

{% tabs local %}
{% tab メール %}
Braze プラットフォームで、クリエイティブタグをメール本文に貼り付けます。![]({% image_buster /assets/img/movable_ink/web2.png %}){: style="max-width:90%"}<br><br>

{% endtab %}
{% tab プッシュ通知 %}

1. Braze プラットフォームの場合:
	- Android プッシュ:**Push Icon Image** と **Expanded Notification Image** フィールドに URL を貼り付けます。<br>![]({% image_buster /assets/img/movable_ink/android.png %}){: style="max-width:60%"}<br><br>
	- iOS プッシュ:**Media** リンクフィールドに URL を貼り付け、使用しているファイル形式を示します。<br>![]({% image_buster /assets/img/movable_ink/ios.png %}){: style="max-width:60%"}<br><br>
	- Web プッシュ:**Push Icon Image** と **Large Notification Image** フィールドに URL を貼り付けます。<br>![]({% image_buster /assets/img/movable_ink/web.png %}){: style="max-width:60%"}<br><br>
2. 画像がキャッシュされないようにするため、メッセージの URL の先頭に空の Liquid タグを追加します。<br>{% raw %}`{% if true %}{% endif %}https://movable-ink-image-url-goes-here`{% endraw %}

{% endtab %}
{% tab アプリ内メッセージ %}

1. Braze プラットフォームで、**Rich Notification Media** フィールドに URL を貼り付けます。![]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. キャッシュの防止に役立つ一意の URL を指定します。Movable Ink のリアルタイム画像が機能し、キャッシュの影響を受けないようにするため、Liquid を使用して Movable Ink 画像 URL の末尾にタイムスタンプを付加します。

これを行うには、次の構文を使用します。必要に応じて画像 URL を置き換えてください。
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
このテンプレートは、現在の時刻（秒単位）を取得し、それを Movable Ink 画像タブの末尾に（クエリパラメーターとして）付加し、最終結果を出力します。**Test** タブでプレビューできます&#8212;これにより、コードが評価され、プレビューが表示されます。

**3.** 最後に、セグメントのメンバーシップを再評価します。これを行うには、キャンペーンの **Target Audiences** ステップにある `Re-evaluate audience membership and liquid at send-time` オプションを有効にします。このオプションが利用できない場合は、カスタマーサクセスマネージャーまたは Braze サポートにお問い合わせください。このオプションは、アプリ内メッセージがトリガーされるたびに、一意の URL を指定してキャンペーンを再要求するよう Braze SDKに指示します。

{% endtab %}
{% tab Content Card %}

1. Braze プラットフォームで、**Rich Notification Media** フィールドに URL を貼り付けます。![]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. モバイル:iOS および Android のContent Cardsの画像は、受信時にキャッシュされ、更新されません。
  - 回避策として、キャンペーンを毎日、毎週、または毎月の定期的なメッセージとしてスケジュールし、対応する有効期限を設定します。これにより、Content Cardが再テンプレート化されます。たとえば、1日に1回更新する必要があるContent Cardは、有効期間が1日に設定された毎日のスケジュール送信として設定する必要があります。
3. Content Cardが再テンプレート化されたときに、Movable Ink のリアルタイム画像が機能し、キャッシュの影響を受けないようにするため、Liquid を使用して Movable Ink 画像 URL の末尾にタイムスタンプを付加します。

これを行うには、次の構文を使用します。必要に応じて画像 URL を置き換えてください。
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
このテンプレートは、現在の時刻（秒単位）を取得し、それを Movable Ink 画像タブの末尾に（クエリパラメーターとして）付加し、最終結果を出力します。**Test** タブでプレビューできます。これにより、コードが評価され、プレビューが表示されます。

{% endtab %}
{% endtabs %}

## トラブルシューティング {#troubleshooting}

### ダイナミック画像が正しく表示されませんか？どのチャネルで問題が発生していますか？ {#dynamic-images-not-showing-correctly-what-channel-are-you-experiencing-difficulties-with}
- **プッシュ通知**:Movable Ink 画像 URL の前に空のロジックがあることを確認します。<br>{% raw %}`{% if true %}{% endif %}https://movable-ink-image-url-goes-here`{% endraw %}
- **アプリ内メッセージとContent Cards**:画像 URL がインプレッションごとに一意であることを確認します。このためには、各 URL が異なるものになるように適切な Liquid を追加します。[アプリ内メッセージおよびContent Cardsメッセージの手順]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/movable_ink/#step-4-braze-experience)を参照してください。
- **画像が読み込まれない**:Braze ダッシュボードで、すべての「マージタグ」を対応する Liquid フィールドに必ず置き換えてください。たとえば、{% raw %}`https://mi-msg.com/p/rp/image.png?mi_u=%%email%%`{% endraw %} を {% raw %}`https://mi-msg.com/p/rp/image.png?mi_u={{${email_address}}}`{% endraw %} に置き換えます。

### Android で GIF を表示するときに問題がありますか？ {#having-trouble-showing-gifs-on-android}
- Android では、実装に GIF サポートが必要です。この設定がない場合は、Android の[アプリ内メッセージカスタマイズ]({{site.baseurl}}/developer_guide/in_app_messages/gifs/?sdktab=android)の記事に従ってください。


[1]: https://www.movableink.com/
[datasource]: ({% image_buster /assets/img/movable_ink/movable_ink1.png %})
[1]: ({% image_buster /assets/img/movable_ink/android.png %})
[2]: ({% image_buster /assets/img/movable_ink/ios.png %})
[3]: ({% image_buster /assets/img/movable_ink/web.png %})