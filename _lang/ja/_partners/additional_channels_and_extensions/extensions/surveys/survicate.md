---
nav_title: Survicate
article_title: Survicate
description: "このリファレンス記事では、BrazeとSurvicateのパートナーシップについて説明します。Survicateは、複数のチャネルやカスタマージャーニー全体を通じて、顧客インサイトの収集、分析、活用を支援するカスタマーフィードバックプラットフォームです。"
alias: /partners/survicate/
page_type: partner
search_tag: Partner

---

# Survicate

> [Survicate](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter)は、複数のチャネルとカスタマージャーニー全体を通じて顧客インサイトを収集、分析、活用するカスタマーフィードバックプラットフォームです。[クイックデモを見る](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter)

_この統合はSurvicateによって管理されています。_

## 統合について {#about-the-integration}

SurvicateとBrazeのネイティブ統合を使用して、メール、アプリ内、モバイル、またはWebアンケートの回答をBrazeの顧客プロファイルと同期できます。アンケートの回答は、カスタム属性またはイベントとしてBrazeユーザープロファイルと自動的に同期されます。リアルタイムのフィードバックインサイトにより、顧客データとともにフィードバックを簡単に追跡・分析し、ターゲットフォローアップやハイパーパーソナライズされたセグメントを作成できます。

## ユースケース {#use-cases}

BrazeとSurvicateは、さまざまなフィードバックのユースケースをカバーするために連携し、アクション可能なユーザーインサイトの収集とカスタマーエクスペリエンスの向上を支援します。

- 受信トレイから回答できる埋め込み型アンケートで、アンケートの回答率を向上させます。
- Brazeアプリ内メッセージを通じて、カスタマージャーニーの重要な段階でインサイトを収集します。
- Survicateに保存されたフィードバックを使用して、Brazeでよりスマートなセグメントを作成します。
- 顧客のフィードバックに基づいてフォローアップキャンペーンを自動化します。
- 顧客インサイトを活用して、パーソナライズされたワークフローをトリガーします。
- 自動翻訳されたアンケートで、より多くのオーディエンスにアプローチします。
- 誰かがアンケートに回答すると、Brazeコンタクトプロファイルにイベントを送信します。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Survicateアカウント | この統合を有効にするにはSurvicateアカウントが必要です。 |
| Braze REST APIキー | `users.track`権限を持つBraze REST APIキー。<br><br>これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、お使いのインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合の主な特徴 {#key-features-of-the-integration}

SurvicateとBrazeの統合はリアルタイムのデータ同期を提供するため、Survicateアンケートの最新情報をBrazeですぐに利用できます。アンケートの回答に基づいて、このデータを使用してタイムリーでパーソナライズされたアクションを実行できます。

- **アンケートの回答をカスタムユーザー属性としてBrazeに送信する**：アンケートの回答データでBrazeユーザープロファイルを充実させます。
- **Brazeでカスタムイベントをトリガーする**：アンケートの回答に基づいたイベントを使用して、特定のグループをターゲットにしたり、フォローアップキャンペーンを開始したりします。
- **詳細なセグメントを構築する**：Survicateアンケートのデータを使用してBraze セグメントを作成し、アウトリーチをさらにパーソナライズします。

## 統合 {#integration}

### Survicateでアンケートを作成する {#creating-your-surveys-in-survicate}

#### アンケートをメールに埋め込むか、共有可能なリンクアンケートを作成する {#embed-your-survey-in-an-email-or-create-a-shareable-link-survey}

1.  Survicateで**+ Create new survey**をクリックし、作成方法（テンプレート、AIアンケート作成、または独自の質問の追加）を選択し、メールまたは共有リンクのアンケートタイプを選択します：
![アンケート作成画面でBrazeが選択されている。]({% image_buster /assets/img/survicate/survicate_1.gif %})

{: start="2"}
2. アンケートのConfigureタブで、回答者を識別するツールとして**Braze**を選択します：
![アンケートのConfigureタブでBrazeが選択されている。]({% image_buster /assets/img/survicate/survicate_2.png %})

{: start="3"}
3. アンケートを設定したら、Shareタブでメールアンケートの送信方法を決定します。2つのオプションがあります：**アンケートをリンクとして**送信するか、**最初の質問をメールに埋め込んで**回答者がメールからすぐにアンケートに回答できるようにします。

{% details アンケートリンクオプション %}

1. **Copy survey link**ボタンからアンケートへのリンクを取得します：

![Copy survey linkボタンからアンケートへのリンクを取得する。]({% image_buster /assets/img/survicate/survicate_3.png %})

{: start="2"}
2. BrazeメールのCTAボタンやハイパーリンクの背後にアンケートリンクを配置します。

![BrazeメールのCTAボタンやハイパーリンクの背後にアンケートリンクを配置する。]({% image_buster /assets/img/survicate/survicate_4.png %})

{% enddetails %}

{% details メール埋め込みオプション %}

最初の質問をメール本文に直接表示し、メールからアンケートを開始します。その後、回答者は残りのアンケートに回答するためのランディングページにリダイレクトされます。

1. **Get email code**をクリックし、**Copy the HTML code**をクリックします：

![メールコードを取得する]({% image_buster /assets/img/survicate/survicate_5.gif %})

{: start="2"}
2. アンケートに使用するBraze キャンペーンに移動し、**Edit email body**をクリックして、テンプレートにHTMLブロックを追加します：

![HTMLブロックコードを取得する]({% image_buster /assets/img/survicate/survicate_6.png %})

{: start="3"}
3. コードをSurvicateアンケートからコピーしたものに置き換えます。すると、アンケートの最初の質問がテンプレートに表示されます：

![Survicateアンケートからコピーしたコードに置き換える]({% image_buster /assets/img/survicate/survicate_7.png %})

{: start="4"}
4. メールをスケジュールし、ターゲットグループを選択すれば、キャンペーンは送信準備完了です。

{% enddetails %}

### Brazeアプリ内メッセージアンケート {#braze-in-app-message-survey}

1. **+ Create new survey**をクリックし、作成方法（テンプレート、AIアンケート作成、または独自の質問の追加）を選択し、プラットフォーム内アンケートとBraze In-App Messageのアンケートタイプを選択します：

![+ Create new surveyをクリックし、作成方法を選択する]({% image_buster /assets/img/survicate/survicate_8.gif %})

{: start="2"}
2. Brazeアカウントに移動し、**メッセージング** > **キャンペーン** > **Create キャンペーン** > **In-App Message**の順に選択して、Brazeアプリ内メッセージアンケートを起動します：
![Brazeアプリ内メッセージアンケートを起動する]({% image_buster /assets/img/survicate/survicate_9.gif %})

### 従来のエディターでBrazeアプリ内メッセージアンケートを起動する {#launch-your-braze-in-app-messenger-survey-via-the-traditional-editor}

1. 従来のエディターを使用している場合は、メッセージタイプで**Custom code**を選択します：

![Custom codeを選択する]({% image_buster /assets/img/survicate/survicate_10.gif %})

{: start="2"}
2. 次に、アンケートのLaunchタブにあるコードをHTMLフィールドに貼り付けます：

![アンケートのLaunchタブからHTMLフィールドにコードを貼り付ける]({% image_buster /assets/img/survicate/survicate_11.gif %})

{% alert note %}
Brazeはデフォルトで、アプリのバックグラウンドがブロックされている間、アプリ内メッセージをiframeで表示します。Survicateのアンケートが表示されている間にアプリとのインタラクションを許可するには、以下が必要です：<br><br>

- Survicate-Brazeスニペットに`opts.useBrazeIframeClipper = true`を追加します。
- Brazeを初期化し、`initBrazeBridge`関数を使用するファイルに`@survicate/braze-bridge-npm` [パッケージ](https://www.npmjs.com/package/@survicate/braze-bridge-npm)をインストールします。

サンプルスニペットとReactの実装は[Survicateの開発者サイト](https://developers.survicate.com/javascript/installation/#braze)にあります。
{% endalert %}

{: start="3"}
3. Braze キャンペーンで、ターゲットと割り当てのステップを設定します。完了したら、キャンペーンを起動する準備が整います。確認ステップでは、キャンペーンの見た目を確認できます。アンケートは、上記のようにSurvicateパネルで指定された場所にWebサイト上に表示されます。

### Braze統合を有効にする {#enabling-the-braze-integration}

1. Braze統合を有効にするには、**Integrations**に移動し、「Braze」を検索して選択します。

![Brazeを選択する]({% image_buster /assets/img/survicate/survicate_12.gif %})

{: start="2"}
2. **Connect**をクリックして認証を設定します。

3. BrazeアカウントのワークスペースAPIキーとBrazeインスタンスURLを入力します：

![BrazeアカウントのワークスペースAPIキーとBrazeインスタンスURLを入力する]({% image_buster /assets/img/survicate/survicate_13.png %})

{% alert important %}
SurvicateをBrazeに接続するには、Braze APIキーに`users.track`権限が必要です。
{% endalert %}

### アンケートをBrazeに接続する {#connecting-your-surveys-to-braze}

Braze統合が接続されたので、各アンケートに個別の設定を行うことができます。アンケートに移動し、**Connect**タブを選択し、利用可能な統合のリストから**Braze**を選択します。

![アンケートに移動し、Connectタブを選択し、Brazeを選択する]({% image_buster /assets/img/survicate/survicate_14.png %})

### 回答をカスタム属性としてBrazeに送信する {#sending-responses-to-braze-as-custom-attributes}

アンケートの回答をカスタム属性としてBrazeに流入するように設定し、収集データでBrazeユーザープロファイルを充実させます。

1. Braze統合の設定タブで、**Update fields**セクションを見つけます。

![Update fieldsセクションを選択する]({% image_buster /assets/img/survicate/survicate_15.png %})

{: start="2"}
2. フィールドを更新したい質問を選択します。Brazeユーザープロファイルがデータで溢れるのを避けるため、選択した質問のみに回答を送信できます。

![フィールドを更新したい質問を選択する]({% image_buster /assets/img/survicate/survicate_16.png %})

{% alert note %}
このBraze統合では、ランキングとマトリックスの質問はサポートされていません。
{% endalert %}

{: start="3"}
3. 更新したいカスタム属性の名前を**User**フィールドの下に追加します：

![更新したいカスタム属性の名前をUserフィールドの下に追加する]({% image_buster /assets/img/survicate/survicate_17.png %})

デフォルトでは、Survicateはアンケートの回答内容を属性値として送信します。ラベルを短くしたり、データ構造に合わせて変更するには、**Edit mapping**をクリックしてこれらの値を変更できます：

![属性値としてのアンケート回答]({% image_buster /assets/img/survicate/survicate_18.png %})

![これらの値を変更するにはEdit mappingをクリックする]({% image_buster /assets/img/survicate/survicate_19.png %})

{% alert note %}
NPSの場合、SurvicateはNPS®の質問の回答グループに基づいてマッピングされた値を送信します。ただし、数値を受信したい場合は、「Send Answers as 0-10 values」をオンに切り替えることができます。
{% endalert %}

![Survicateは回答グループに基づいてマッピングされた値を送信する]({% image_buster /assets/img/survicate/survicate_20.png %})

{: start="4"}
4. **+ Add new**をクリックし、同じステップを適用することで、さらに多くの質問を統合に接続します。

![より多くの質問を統合に接続する]({% image_buster /assets/img/survicate/survicate_21.png %})

### Brazeコンタクトのプロファイルにイベントを送信する {#sending-events-to-braze-contacts-profiles}

これまでの設定とは別に、回答者がアンケートの質問に回答するたびに、Survicateは`survicate-question-answered`というカスタムイベントをBrazeに送信できます。
Survicateパネルの「Send responses as custom attributes」で、すべての質問に対してイベントを送信するか、「Update fields」タブで選択した質問に対してイベントを送信するか、またはまったく送信しないかを選択できます：

![すべての質問に対してイベントを送信するかどうかを選択できる]({% image_buster /assets/img/survicate/survicate_22.png %})

イベントの送信を選択した場合、ユーザープロファイルでSurvicateアンケートに何回回答したか、最後に回答したのはいつかを確認できます：

![回答状況]({% image_buster /assets/img/survicate/survicate_23.png %})

イベントには、質問に対する回答と、アンケート、質問、回答者に関する情報を含むイベントプロパティが含まれます。このイベントを使用してセグメントを作成できます。例えば、特定の日付以降や特定の回数アンケートに回答したユーザーのセグメントを作成できます：

![イベントには回答を含むイベントプロパティが含まれる]({% image_buster /assets/img/survicate/survicate_24.png %})

このデータは、Brazeでキャンペーンを作成する際にも使用できます。

![このデータはBrazeでキャンペーンを作成する際にも使用できる]({% image_buster /assets/img/survicate/survicate_25.png %})

### 統合をテストする {#test-the-integration}

アンケートの準備と統合設定が完了したら、作成した属性、タグ、新規コンタクト設定の横にある**Test Integration**ボタンをクリックして、Survicateを離れることなくテストできます。SurvicateはBrazeアカウントにテストコンタクト（`braze-test@survicate.com`）を作成します。コンタクトのプロファイルには、設定に従って更新されたフィールドが含まれます。

![Test Integrationボタンをクリックする]({% image_buster /assets/img/survicate/survicate_26.png %})

Brazeでは、Survicateダミーコンタクトのマッピングされたフィールドのサンプルデータを確認できます：

![Survicateダミーコンタクトのマッピングされたフィールドのサンプルデータ]({% image_buster /assets/img/survicate/survicate_27.png %})

### アンケート結果を分析する {#analyzing-your-survey-results}

Brazeアンケートで回答を収集したら、回答者が共有したフィードバックやインサイトを確認しましょう。Survicateを使えば、結果、統計、傾向を簡単に確認し、さらなるアクションにつなげることができます。

### Survicateでのフィードバック {#feedback-in-survicate}

アンケートの回答収集が開始されると、アンケートのAnalyzeタブにすぐに回答が表示されます。

![Analyzeタブの回答]({% image_buster /assets/img/survicate/survicate_28.png %})

Analyzeタブでは、統計および経時データを含む全体的な結果が表示されるほか、各アンケート提出の詳細を調べるための個別の回答も表示されます。

### Brazeでのフィードバック {#feedback-in-braze}

アンケートの回答でユーザーフィールドを更新したり、回答をカスタムイベントとして送信したりすると、リアルタイムで同期されたアンケートデータを確認できます。Brazeで、アンケートに回答した特定のコンタクトにアクセスします。コンタクトのメインビューには、回答ベースのデータとイベントの両方が表示されます。

![アンケートデータはリアルタイムで同期される]({% image_buster /assets/img/survicate/survicate_29.png %})