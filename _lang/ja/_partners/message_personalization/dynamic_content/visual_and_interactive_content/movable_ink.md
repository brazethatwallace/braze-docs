---
title: "Movable Ink"
article_title: Movable Ink
alias: "/partners/movable_ink/"
description: "このリファレンス記事では、BrazeとMovable Inkのパートナーシップについて説明します。Movable Inkは、顧客に印象づける説得力のある独特なビジュアルエクスペリエンスを作成できる手段をデジタルマーケターに提供するクラウドベースのソフトウェアプラットフォームです。"
page_type: partner
search_tag: Partner

---

# Movable Ink

> [Movable Ink](https://www.movableink.com/)は、顧客に印象づける説得力のある独特なビジュアルエクスペリエンスを作成できる手段をデジタルマーケターに提供するクラウドベースのソフトウェアプラットフォームです。Movable Inkプラットフォームは、キャンペーンに簡単に挿入できる有用なカスタマイズオプションを提供します。

_この統合はMovable Inkによって管理されます。_

## 統合について {#about-the-integration}

ポーリング、カウントダウンタイマー、スクラッチオフなど、Movable InkのIntelligent Creative機能を活用してBrazeのクリエイティブ機能を拡大します。Movable InkとBrazeの統合により、ダイナミックなデータドリブン型のメッセージへのよりバランスの取れたアプローチを可能にし、重要な事柄に関するリアルタイムの要素をユーザーに提供します。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Movable Inkアカウント | このパートナーシップを活用するには、Movable Inkアカウントが必要です。 |
| データソース | データソースをMovable Inkに接続する必要があります。これは、CSV、Webサイトインポート、またはAPIを使用して実行できます。BrazeとMovable Inkの間で統一識別子（`external_id`など）を使用してデータを渡していることを確認してください。
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## ユースケース {#use-cases}

- パーソナライズされた月ごとの要約または年末の要約。
- 直近の既知の行動に基づいて、メール、プッシュ、またはリッチプッシュ通知に使用される画像をダイナミックにパーソナライズします。<br>
	以下に例を示します。
	- リッチプッシュメッセージを使用して、APIからデータを取得してイベントのスケジュールを動的に作成します。
	- 大規模なセール（ブラックフライデー、バレンタインデー、祝日セールなど）が近づいているときに、カウントダウンタイマーを使用してユーザーに通知します。
	- プロモーションコードを配信する楽しくインタラクティブな方法として、スクラッチオフ機能を使用します。

## サポートされているMovable Inkの機能 {#supported-movable-ink-capabilities}

Intelligent Creativeには、会社ユーザーが利用できる多くのサービスがあります。次のリストに、サポートされている機能を示します。

| Movable Inkの機能 | 機能 | リッチプッシュ通知 | アプリ内メッセージ / Content Cards / メール | 詳細 |
| ---------------------- |---| ---------------------- | -------------------------------- | ------- |
| クリエイティブオプティマイザー | A/Bコンテンツの表示 | ✗ | ✔ | |
| 最適化 | ✗ | ✔* | * Branchのディープリンクソリューションを使用する必要があります |
| ターゲティングルール | 日付 | ✔* | ✔ | * プッシュ通知は受信時にキャッシュされ、更新されないため、サポートされますが推奨されません |
| 曜日 | ✔* | ✔ | * プッシュ通知は受信時にキャッシュされ、更新されないため、サポートされますが推奨されません |
| 時刻 | ✔* | ✔ | * プッシュ通知は受信時にキャッシュされ、更新されないため、サポートされますが推奨されません |
| ストーリー/行動アクティビティ | | ✔* | ✔* | * Brazeに使用されるユニークユーザー識別子を、メールサービスプロバイダー (ESP) の識別子にリンクする必要があります |
| アプリ内のディープリンク | | ✔* | ✔* | * 顧客に効率化されたエクスペリエンスを提供するには、Branchで確立されたディープリンクソリューションを使用するか、Movable Inkのクライアントエクスペリエンスチームによる検証済みソリューションを使用します。 |
| アプリ | カウントダウンタイマー | ✔* | ✔ | * プッシュ通知は受信時にキャッシュされ、更新されないため、サポートされますが推奨されません |
| ポーリング | ✗ | ✔* | * 投票後、アプリを離れてモバイルランディングページに遷移します |
| スクラッチオフ | ✔* | ✔* | * クリックすると、スクラッチオフエクスペリエンスのためにアプリを離れます |
| 動画 | ✔* | ✔* | * アニメーションGIFのみ。<br>Androidの場合、Brazeの実装には[GIFサポート]({{site.baseurl}}/developer_guide/in_app_messages/gifs/?sdktab=android)が必要です |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Supported Movable Ink capabilities" }

## 統合 {#integration}

### ステップ1:Movable Inkのデータソースを作成する {#step-1-create-a-data-source-for-movable-ink}

CSVアップロード、Webサイトインポート、またはAPI統合のいずれかのデータソースを作成する必要があります。

![表示されるさまざまなデータソースオプション:CSVアップロード、Webサイト、またはAPI統合。]({% image_buster /assets/img/movable_ink/movable_ink1.png %})

{% tabs local %}
{% tab CSVデータソース %}
- **CSVデータソース**:各行には、少なくとも1つのセグメント列と1つのコンテンツ列が必要です。CSVがアップロードされた後、コンテンツのターゲットとして使用する列を選択します。[CSVファイルの例]({% image_buster /assets/download_file/movable_ink_CSV.csv %})

![「CSV」をデータソースとして選択したときに表示されるフィールド。]({% image_buster /assets/img/movable_ink/movable_ink2.png %})
{% endtab %}
{% tab Webサイトデータソース %}
- **Webサイトデータソース**:各行には、少なくとも1つのセグメント列と1つのコンテンツ列が必要です。CSVがアップロードされたら、コンテンツのターゲットを設定するために使用する列を選択します。
  - このプロセスでは、以下をマッピングする必要があります。
    - セグメントとして使用されるフィールド
    - クリエイティブで動的にパーソナライズできるデータフィールドとして使用する項目（たとえば、ユーザー属性や名、姓、市区町村などのカスタム属性）

![「Webサイト」をデータソースとして選択したときに表示されるフィールド。]({% image_buster /assets/img/movable_ink/movable_ink3.png %})
{% endtab %}
{% tab API統合 %}
- **API統合**:自社のAPIを使用して、APIレスポンスから直接コンテンツを供給します。

![「API統合」をデータソースとして選択したときに表示されるフィールド]({% image_buster /assets/img/movable_ink/movable_ink4.png %})
{% endtab %}
{% endtabs %}

### ステップ2:Movable Inkプラットフォームでキャンペーンを作成する {#step-2-create-a-campaign-on-the-movable-ink-platform}

Movable Inkのホーム画面から、キャンペーンを作成します。HTMLからのメール、画像からのメール、または任意のチャネルで使用できるブロック（プッシュ、アプリ内メッセージ、Content Cards（推奨）など）のいずれかを選択できます。

また、ブロックを通じて利用できるさまざまなコンテンツオプションを確認することもお勧めします。

![新しいMovable Inkキャンペーンを作成するときのMovable Inkプラットフォームの外観。]({% image_buster /assets/img/movable_ink/movable_ink5.png %}){: style="max-width:70%"}

Movable Inkには、テキストや画像などの要素をドラッグ＆ドロップできる簡単なエディターがあります。データソースを入力した場合は、データプロパティを使用して画像をダイナミックに生成できます。また、このフロー内にフォールバックを作成することもできます。これは、キャンペーンが送信され、ユーザーがパーソナライゼーション基準に該当しない場合に使用されます。

![Movable Inkブロックエディターに表示されるカスタマイズ可能なさまざまな要素。]({% image_buster /assets/img/movable_ink/create_campaign2.png %})

キャンペーンを完了する前に、ダイナミックな画像をプレビューし、クエリパラメーターをテストして、表示時に画像がどのように見えるかを確認してください。完了すると、Brazeに挿入できるダイナミックURLが生成されます。

Movable Inkプラットフォームの使用方法の詳細については、[Movable Inkサポートセンター](https://support.movableink.com/)を参照してください。

### ステップ3:Movable InkコンテンツURLを取得する {#step-3-obtain-movable-ink-content-url}

Movable InkのコンテンツをBrazeメッセージに含めるには、Movable Inkから提供されたソースURLを確認する必要があります。

ソースURLを取得するには、Movable Inkダッシュボードでコンテンツを設定し、完了してコンテンツをエクスポートする必要があります。**Finish**ページで、クリエイティブタグからソースURL（`img src`）をコピーします。

![Movable Inkキャンペーンを完了すると表示されるページ。ここにコンテンツURLが表示されます。]({% image_buster /assets/img/movable_ink/obtain_url.png %}){: style="max-width:80%;"}

次にBrazeプラットフォームで、URLを該当するフィールドに貼り付けます。メッセージングチャネルに適したフィールドは、ステップ4に記載されています。最後に、マージタグ（{% raw %}`&mi_u=%%email%%`{% endraw %}など）を対応するLiquid変数（{% raw %}`&mi_u={{${email_address}}}`{% endraw %}など）に置き換えます。

### ステップ4:Brazeエクスペリエンス {#step-4-braze-experience}

{% tabs local %}
{% tab メール %}
Brazeプラットフォームで、クリエイティブタグをメール本文に貼り付けます。![Movable Inkクリエイティブタグがメッセージ本文に挿入されたBrazeメールコンポーザー。]({% image_buster /assets/img/movable_ink/web2.png %}){: style="max-width:90%"}<br><br>

{% endtab %}
{% tab プッシュ通知 %}

1. Brazeプラットフォームの場合:
	- Androidプッシュ:**Push Icon Image**と**Expanded Notification Image**フィールドにURLを貼り付けます。<br>![Movable InkコンテンツのURL画像フィールドが表示されたBraze Androidプッシュ設定。]({% image_buster /assets/img/movable_ink/android.png %}){: style="max-width:60%"}<br><br>
	- iOSプッシュ:**Media**リンクフィールドにURLを貼り付け、使用しているファイル形式を示します。<br>![Movable Ink URLが入力されたBraze iOSプッシュコンポーザーのメディアフィールド。]({% image_buster /assets/img/movable_ink/ios.png %}){: style="max-width:60%"}<br><br>
	- Webプッシュ:**Push Icon Image**と**Large Notification Image**フィールドにURLを貼り付けます。<br>![プッシュアイコンと大きな画像のURLフィールドが表示されたBraze Webプッシュエディター。]({% image_buster /assets/img/movable_ink/web.png %}){: style="max-width:60%"}<br><br>
2. 画像がキャッシュされないようにするため、メッセージのURLの先頭に空のLiquidタグを追加します。<br>{% raw %}`{% if true %}{% endif %}https://movable-ink-image-url-goes-here`{% endraw %}

{% endtab %}
{% tab アプリ内メッセージ %}

1. Brazeプラットフォームで、**Rich Notification Media**フィールドにURLを貼り付けます。![Movable Ink画像URLが入力されたBrazeリッチ通知メディアフィールド。]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. キャッシュの防止に役立つ一意のURLを指定します。Movable Inkのリアルタイム画像が機能し、キャッシュの影響を受けないようにするため、Liquidを使用してMovable Ink画像URLの末尾にタイムスタンプを付加します。

これを行うには、次の構文を使用します。必要に応じて画像URLを置き換えてください。
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
このテンプレートは、現在の時刻（秒単位）を取得し、それをMovable Ink画像タブの末尾に（クエリパラメーターとして）付加し、最終結果を出力します。**Test**タブでプレビューできます&#8212;これにより、コードが評価され、プレビューが表示されます。

**3.** 最後に、セグメントのメンバーシップを再評価します。これを行うには、キャンペーンの**ターゲットオーディエンス**ステップにある`Re-evaluate audience membership and liquid at send-time`オプションを有効にします。このオプションが利用できない場合は、カスタマーサクセスマネージャーまたはBrazeサポートにお問い合わせください。このオプションは、アプリ内メッセージがトリガーされるたびに、一意のURLを指定してキャンペーンを再要求するようBraze SDKに指示します。

{% endtab %}
{% tab Content Card %}

1. Brazeプラットフォームで、**Rich Notification Media**フィールドにURLを貼り付けます。![Movable Ink画像URLが入力されたBraze Content Cardメディアフィールド。]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. モバイル:iOSおよびAndroidのContent Cardsの画像は、受信時にキャッシュされ、更新されません。
  - 回避策として、キャンペーンを毎日、毎週、または毎月の定期的なメッセージとしてスケジュールし、対応する有効期限を設定します。これにより、Content Cardが再テンプレート化されます。たとえば、1日に1回更新する必要があるContent Cardは、有効期間が1日に設定された毎日のスケジュール送信として設定する必要があります。
3. Content Cardが再テンプレート化されたときに、Movable Inkのリアルタイム画像が機能し、キャッシュの影響を受けないようにするため、Liquidを使用してMovable Ink画像URLの末尾にタイムスタンプを付加します。

これを行うには、次の構文を使用します。必要に応じて画像URLを置き換えてください。
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
このテンプレートは、現在の時刻（秒単位）を取得し、それをMovable Ink画像タブの末尾に（クエリパラメーターとして）付加し、最終結果を出力します。**Test**タブでプレビューできます。これにより、コードが評価され、プレビューが表示されます。

{% endtab %}
{% endtabs %}

## トラブルシューティング {#troubleshooting}

### ダイナミック画像が正しく表示されませんか？どのチャネルで問題が発生していますか？ {#dynamic-images-not-showing-correctly-what-channel-are-you-experiencing-difficulties-with}
- **プッシュ通知**:Movable Ink画像URLの前に空のロジックがあることを確認します。<br>{% raw %}`{% if true %}{% endif %}https://movable-ink-image-url-goes-here`{% endraw %}
- **アプリ内メッセージとContent Cards**:画像URLがインプレッションごとに一意であることを確認します。このためには、各URLが異なるものになるように適切なLiquidを追加します。[アプリ内メッセージおよびContent Cardsメッセージの手順]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/movable_ink#step-4-braze-experience)を参照してください。
- **画像が読み込まれない**:Brazeダッシュボードで、すべての「マージタグ」を対応するLiquidフィールドに必ず置き換えてください。たとえば、{% raw %}`https://mi-msg.com/p/rp/image.png?mi_u=%%email%%`{% endraw %}を{% raw %}`https://mi-msg.com/p/rp/image.png?mi_u={{${email_address}}}`{% endraw %}に置き換えます。

### AndroidでGIFを表示するときに問題がありますか？ {#having-trouble-showing-gifs-on-android}
- Androidでは、実装にGIFサポートが必要です。この設定がない場合は、Androidの[アプリ内メッセージカスタマイズ]({{site.baseurl}}/developer_guide/in_app_messages/gifs/?sdktab=android)の記事に従ってください。


[1]: https://www.movableink.com/
[datasource]: ({% image_buster /assets/img/movable_ink/movable_ink1.png %})
[1]: ({% image_buster /assets/img/movable_ink/android.png %})
[2]: ({% image_buster /assets/img/movable_ink/ios.png %})
[3]: ({% image_buster /assets/img/movable_ink/web.png %})