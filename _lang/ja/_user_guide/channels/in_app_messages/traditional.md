---
nav_title: 従来のエディター
article_title: 従来のエディターでアプリ内メッセージを作成する
page_order: 2
description: "このリファレンス記事では、キャンペーンまたはキャンバスを使用してBrazeプラットフォームでアプリ内メッセージを作成する方法について説明します。"
channel:
  - in-app messages
tool:
  - キャンペーン
search_rank: 4.8
toc_headers: h2
---

# 従来のエディターでアプリ内メッセージを作成する {#create-an-in-app-message-with-the-traditional-editor}

> Brazeプラットフォームでは、キャンペーン、キャンバス、またはAPIキャンペーンとしてアプリ内メッセージやブラウザ内メッセージを作成できます。便利な[アプリ内メッセージ準備ガイド]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices)を使用して、事前にメッセージを計画し、すべての素材を準備しておくことを強くお勧めします。

## ステップ 1:メッセージの作成場所を選択する {#create-new-campaign-in-app}

メッセージをキャンペーンとキャンバスのどちらで送信すべきかわからない場合は、キャンペーンは単一のターゲットメッセージングに適しており、キャンバスはマルチステップのユーザージャーニーに適しています。

{% tabs %}
{% tab キャンペーン %}

1. **メッセージング** > **キャンペーン**に移動し、**キャンペーンを作成**を選択します。
2. **アプリ内メッセージ**を選択します。アプリ内メッセージはマルチチャネルキャンペーンでは利用できないことに注意してください。
3. キャンペーンにわかりやすく意味のある名前を付けます。
4. 必要に応じて[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams)と[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)を追加します。
   * タグを使用すると、キャンペーンを見つけやすくなり、レポートを作成しやすくなります。たとえば、[レポートビルダー]({{site.baseurl}}/user_guide/analytics/reports/report_builder)を使用する場合、特定のタグでフィルタリングできます。
5. キャンペーンに必要な数のバリアントを追加して名前を付けます。追加したバリアントごとに、異なるプラットフォーム、メッセージタイプ、レイアウトを選択できます。このトピックの詳細については、[多変量テストとABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)を参照してください。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似している場合や同じコンテンツを持つ場合は、追加のバリアントを追加する前にメッセージを作成してください。その後、**バリアントを追加**ドロップダウンから**バリアントからコピー**を選択できます。
{% endalert %}

{% endtab %}
{% tab キャンバス %}

1. キャンバスコンポーザーを使用して[キャンバスを作成]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)します。
2. キャンバスを設定したら、キャンバスビルダーでステップを追加します。ステップにわかりやすく意味のある名前を付けます。
3. [ステップスケジュール]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types#schedule-delay)を選択し、必要に応じて遅延を指定します。アプリ内メッセージを含むステップはアクションベースにできないことに注意してください。
4. 必要に応じて、このステップのオーディエンスをフィルタリングします。セグメントを指定し、追加のフィルターを追加することで、このステップの受信者をさらに絞り込むことができます。オーディエンスオプションは、遅延後のメッセージ送信時にチェックされます。
5. [進行動作]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases)を選択します。
6. メッセージと組み合わせたい他のメッセージングチャネルを選択します。

{% alert important %}
1つのステップに複数のアプリ内メッセージバリアントを含めることはできません。
{% endalert %}

キャンバス固有の詳細情報については、[キャンバスのアプリ内メッセージ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#messages-in-canvas)を参照してください。

{% endtab %}
{% endtabs %}

## ステップ 2:配信プラットフォームを指定する {#step-2-specify-delivery-platforms}

まず、メッセージを受信するプラットフォームを選択します。この選択を使用して、キャンペーンの配信を特定のアプリセットに制限します。たとえば、モバイルアプリのダウンロードを促すブラウザ内メッセージに**Web Browsers**を選択して、すでにアプリを取得した後にメッセージを受信しないようにすることができます。プラットフォームの選択はバリアントごとに固有であるため、プラットフォームごとのメッセージエンゲージメントをテストすることもできます。

| プラットフォーム | メッセージ配信 |
|---------------------------------|------------------------------|
| Mobile Apps | iOS、Android、Vega SDK |
| Web Browsers | Web SDK |
| Mobile AppsとWeb Browsersの両方 | iOS、Android、Vega、Web SDK |
{: .reset-td-br-1 .reset-td-br-2 aria-label="配信プラットフォームの指定" }

## ステップ 3:メッセージタイプを指定する {#step-3-specify-your-message-types}

送信プラットフォームを選択したら、それに関連するメッセージタイプ、レイアウト、その他のオプションを参照します。これらの各メッセージの期待される動作と外観の詳細については、[メッセージタイプ]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types)ページを参照するか、以下の表のリンクされたメッセージタイプをクリックしてください。

使用するメッセージタイプを決定する際は、メッセージが占めるスペースの量と、ユーザーエクスペリエンスにどの程度の中断を与えるかを考慮してください。

- **スライドアップ**メッセージは最も控えめで、コンテンツをブロックせずにさりげなく表示されます。
- **モーダル**メッセージは中間的な位置づけで、画面全体を占有せずに注目を集めるのに十分な存在感があります。
- **フルスクリーン**メッセージは最も注目を集め、重要なお知らせやプロモーションに最適です。

コンテンツが複雑になるほど、より多くのスペースが必要になり、ユーザーのフローを中断する可能性が高くなります。

### メッセージタイプ {#message-types}

これらのアプリ内メッセージは、モバイルアプリとウェブアプリケーションの両方で使用できます。

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table aria-label="メッセージタイプ" class="tg">
  <caption>メッセージタイプ</caption>
<thead>
  <tr>
    <th>メッセージタイプ</th>
    <th>タイプの説明</th>
    <th>利用可能なレイアウト</th>
    <th>その他のオプション</th>
    <th>推奨される使用方法</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/fullscreen'>フルスクリーン</a></td>
    <td>メッセージブロックで画面全体を覆うメッセージです。</td>
    <td>
      <ul>
      <li>画像とテキスト</li>
      <li>画像のみ</li>
      </ul>
    </td>
    <td>デバイスの向きの強制（縦向きまたは横向き）</td>
    <td>大きくて大胆に！最も重要なキャンペーン、重要な通知、大規模なプロモーションなど、ユーザーにコンテンツを確実に見てもらいたい場合に使用します。<br><br>モバイルデバイスでは、デバイスの向きがメッセージの向きと一致しない場合、縦向きおよび横向きのメッセージは表示されないことに注意してください。</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/modal'>モーダル</a></td>
    <td>画面オーバーレイとメッセージブロックで画面全体を覆うメッセージです。</td>
    <td>
      <ul>
      <li>テキスト（オプションの画像付き）</li>
      <li>画像のみ</li>
      </ul>
    </td>
    <td>N/A</td>
    <td>バランスの取れた選択肢です。新機能の試用やプロモーションの活用を促すなど、ユーザーの注目を集める明確な方法が必要な場合に使用します。</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/slideup'>スライドアップ</a></td>
    <td>画面の残りの部分をブロックせずに、指定された場所にスライドして表示されるメッセージです。</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>控えめで、画面の占有面積が最も少ないです。新機能、お知らせ、Cookieの使用など、小さな情報をユーザーに通知する場合に使用します。<br></td>
  </tr>
</tbody>
</table>

### 高度なメッセージタイプ {#advanced-message-types}

これらのアプリ内メッセージは、ニーズに合わせてカスタマイズできます。

<table aria-label="高度なメッセージタイプ" class="tg">
  <caption>高度なメッセージタイプ</caption>
<thead>
  <tr>
    <th>メッセージタイプ</th>
    <th>タイプの説明</th>
    <th>利用可能なレイアウト</th>
    <th>要件</th>
    <th>推奨される使用方法</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/customize#custom-html-messages'>カスタムHTMLメッセージ</a></td>
    <td>カスタムコード（HTML、CSS、JavaScript）で定義されたとおりに動作するカスタムメッセージです。</td>
    <td>N/A</td>
    <td>アプリ内メッセージを機能させるには、<span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span>初期化オプションを<code>true</code>に設定する必要があります。</td>
    <td>IAMのすべての利点を活かしつつ、追加機能が必要な場合や、外観を「ブランドに合わせた」ものにしたい場合に適しています。メッセージのあらゆる細部（フォント、色、形、サイズ、ボタンなど）を変更できます。<br><br>ユースケースの例としては、アプリのフィードバックの依頼、メールキャプチャフォーム、ページ分割されたメッセージなどがあります。</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/customize#email-capture-form'>メールキャプチャフォーム</a></td>
    <td>通常、閲覧者のメールアドレスをキャプチャするために使用されます。</td>
    <td>N/A</td>
    <td>アプリ内メッセージを機能させるには、<span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span>初期化オプションを<code>true</code>に設定する必要があります。</td>
    <td>ユーザーにメールアドレスの送信を促す場合に使用します。</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/customize#web-modal-css'>CSS付きウェブモーダル</a></td>
    <td>カスタマイズ可能なCSSを持つウェブ用モーダルメッセージです。</td>
    <td>
      <ul>
      <li>テキスト（オプションの画像付き）</li>
      <li>画像のみ</li>
      </ul>
    </td>
    <td>CSS付きウェブモーダルはWeb SDK固有のもので、<b>Web Browsers</b>を選択した後にのみ使用できます。</td>
    <td>カスタムCSSをアップロードまたは記述して、美しく全体的にカスタムスタイルのメッセージングを作成したい場合に使用します。</td>
  </tr>
</tbody>
</table>

{% alert important %}
Brazeがコードに閉じるボタンまたは却下ボタンが含まれていないことを検出した場合、追加するようリクエストします。便宜上、コードにコピー＆ペーストできるスニペットを用意しています：<br><br>`<a href= "appboy://close">X</a>`
{% endalert %}

## ステップ 4:アプリ内メッセージを作成する {#step-4-compose-your-in-app-message}

**作成**タブでは、メッセージのコンテンツと動作のすべての側面を編集できます。

![新規顧客を歓迎し、ユーザープロファイルの設定を促すブランドのアプリ内メッセージの例。]({% image_buster /assets/img_archive/iam_compose.png %}){: style="max-width:85%" }

**作成**タブの内容は、前のステップで選択したメッセージオプションによって異なりますが、以下のオプションのいずれかが含まれる場合があります。

### 言語 {#language}

**Add Languages**を選択し、提供されたリストから希望の言語を選択します。これにより、メッセージに[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#conditional-logic)が挿入されます。コンテンツを記述する前に言語を選択して、Liquid内の適切な場所にテキストを入力できるようにすることをお勧めします。[利用可能な言語の完全なリスト]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization#languages-supported)を参照してください。

### 画像 {#image}

メッセージタイプに応じて、**Upload Image**、**Pick a Badge**、または**Font Awesome**を使用できます。画像をアップロードするには、**Add Image**を選択するか、画像URLを入力します。**Add Image**を選択すると**メディアライブラリ**が開き、以前にアップロードした画像を選択するか、新しい画像を追加できます。各メッセージタイプとプラットフォームには、それぞれ推奨される比率と要件があります。画像を発注または作成する前に、それらを確認してください。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

### ヘッダーと本文 {#header-and-body}

好きなことを書きましょう！完全にカスタムなコピー（多くの場合カスタムHTML機能付き）を含め、[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid)やその他のパーソナライゼーションタイプのオプションを使用できます。メッセージを素早く伝え、顧客にクリックしてもらえるほど効果的です。明確で簡潔なヘッダーとメッセージコンテンツをお勧めします。

一部のメッセージタイプではヘッダーが不要なため、ヘッダーの入力を求められません。

#### ヒント {#tips}

##### AIコピーの生成 {#generating-ai-copy}

素晴らしいコピーの作成にお困りですか？[AIコピーライティングアシスタント]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy)を使用してみてください。製品名または説明を入力すると、AIがメッセージングに使用できる人間のようなマーケティングコピーを生成します。

![アプリ内メッセージコンポーザーのメッセージフィールドにある「AIコピーライターを起動」ボタン。]({% image_buster /assets/img/ai_copywriter/ai_copywriter_iam.png %}){: style="max-width:60%"}

##### 右から左のメッセージの作成 {#creating-right-to-left-messages}

アラビア語やヘブライ語などの右から左のメッセージの作成にお困りですか？ベストプラクティスについては、[右から左のメッセージの作成]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)を参照してください。

### ボタンテキスト {#buttons}

メッセージタイプで利用可能な場合、本文テキストの下に最大2つのボタンを表示できます。カスタムボタンテキストと色を作成および編集できます。メールキャプチャフォーム内に利用規約リンクを追加することもできます。

ボタンを1つだけ使用する場合、追加のボタン用のスペースを残す代わりに、メッセージの下部にある利用可能なスペースを占めるように自動的に調整されます。

#### プライマリボタンの選択 {#choosing-a-primary-button}

これらのボタンを独自の色でフォーマットする場合は、より望ましい結果にはButton 2を使用することをお勧めします。

つまり、ユーザーに一方のボタンをもう一方よりも多くクリックしてもらいたい場合は、右側に配置してください。右側のボタンは、特にメッセージの他の部分とやや対照的な色や目立つ色を持っている場合、クリックされる可能性が高いことが多いです。これは、左側のボタンがメッセージとより視覚的に溶け込んでいる場合にのみ強調されます。

![アプリ内メッセージのプライマリボタンとセカンダリボタン]({% image_buster /assets/img/primary-secondary-buttons.png %})

### クリック時の動作 {#button-actions}

顧客がアプリ内メッセージのボタンをクリックすると、以下のアクションが利用可能です。

| アクション | 説明 |
|---|---|
| ウェブURLにリダイレクト | ネイティブでないウェブページを開きます。 |
| [アプリへのディープリンク]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content) | アプリ内の既存の画面にディープリンクします。 |
| メッセージを閉じる | 現在アクティブなメッセージを閉じます。 |
| カスタムイベントを記録 | トリガーする[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events)を選択します。別のアプリ内メッセージの表示や追加のメッセージングのトリガーに使用できます。 |
| カスタム属性を記録 | 現在のユーザーに設定する[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)を選択します。 |
| プッシュ許可をリクエスト | ネイティブのプッシュ許可を表示します。[プッシュプライミング]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)の詳細と、プッシュのためのユーザー準備の[ベストプラクティス]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#best-practices)をお読みください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="クリック時の動作" }

注意：__プッシュ許可をリクエスト__、__カスタムイベントを記録__、__カスタム属性を記録__オプションには、以下のSDK最小バージョンが必要です。

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

### iOSデバイスオプション {#ios-device-options}

必要に応じて、アプリ内メッセージをiOSデバイスのみに送信するように制限できます。これを行うには、**Change**をクリックし、**Only send to iOS devices**を選択します。

### メッセージの閉じ方 {#message-close}

以下のオプションから選択します：

- **自動的に却下：**メッセージが画面に表示される秒数を選択します。
- **ユーザーのスワイプまたはタッチを待つ：**却下または閉じるオプションが必要です。

### スライドアップの位置 {#slide-up-position}

この設定はスライドアップメッセージタイプにのみ適用されます。スライドアップを**From Bottom of App Screen**から表示するか、**From Top of App Screen**から表示するかを選択します。

### HTMLとアセット {#html-and-assets}

この設定はカスタムコードメッセージタイプにのみ適用されます。利用可能なスペースにHTMLをコピー＆ペーストし、ZIPファイルを使用してアセットをアップロードします。

### メールキャプチャ入力プレースホルダー {#email-capture-input-placeholder}

この設定はメールキャプチャフォームメッセージタイプにのみ適用されます。メール入力フィールドのプレースホルダーテキストとして表示されるカスタムコピーを入力します。デフォルトは「Enter your email address」です。

## ステップ 5:アプリ内メッセージのスタイルを設定する {#step-5-style-your-in-app-message}

**スタイル**タブでは、メッセージのすべての視覚的側面を調整できます。画像やバッジをアップロードするか、事前にデザインされたバッジアイコンを選択します。パレットから選択するか、16進数、RGB、またはHSBコードを入力して、ヘッダーと本文テキスト、ボタン、背景の色を変更します。

**スタイル**タブの内容は、前のステップで選択したメッセージオプションによって異なりますが、以下のオプションのいずれかが含まれる場合があります。

| フォーマット | 入力 | 説明 |
|---|---|---|
| [カラープロファイル]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/in_app_message_template#reusable-color-profiles) | アプリ内メッセージテンプレートギャラリーから適用します。 | **Apply Template**を選択し、ギャラリーから選択します。次に、**Save**を選択します。 |
| テキスト配置 | 左、中央、または右。 | 新しいBraze SDKバージョンでのみ利用可能です。 |
| ヘッダー | 16進数カラーコード。 | 希望の16進数カラーが表示されます。色の不透明度も選択できます。 |
| テキスト | 16進数カラーコード。 | 希望の16進数カラーが表示されます。色の不透明度も選択できます。 |
| ボタン | 16進数カラーコード。 | 希望の16進数カラーが表示されます。色の不透明度も選択できます。メッセージの閉じるボタンの背景、および各ボタンの背景、テキスト、ボーダーの色を選択できます。 |
| ボタンボーダー | 16進数カラーコード。 | 新機能！プライマリボタンとセカンダリボタンを互いに区別できるようになります。対照的な色でボタンをアウトラインすることをお勧めします。 |
| 背景色 | 16進数カラーコード。 | 希望の16進数カラーが表示されます。色の不透明度も選択できます。これはメッセージ全体の背景で、テキスト本文の背後にはっきりと表示されます。 |
| 画面オーバーレイ | 16進数カラーコード。 | 希望の16進数カラーが表示されます。色の不透明度も選択できます。新しいBraze SDKバージョンでのみ利用可能です。これはメッセージ全体の周りのフレームです。 |
| シェブロンまたはその他のメッセージ閉じオプション | 16進数カラーコード。 | 希望の16進数カラーが表示されます。色の不透明度も選択できます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="アプリ内メッセージのスタイル設定" }

送信前に必ずメッセージを[プレビューしてテスト]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message)してください。

{% alert important %}
一部のアプリ内メッセージタイプには、カスタムHTML（またはCSS、JavaScript）とアセットをZIPファイルでアップロードする以外のスタイル設定オプションがありません。[CSS付きウェブモーダル]({{site.baseurl}}/user_guide/channels/in_app_messages/customize#web-modal-css)では、カスタムCSSをアップロードまたは記述して、美しく全体的にカスタムスタイルのメッセージングを作成できます。
{% endalert %}

## ステップ 6:追加設定を構成する（オプション） {#step-6-configure-additional-settings-optional}

### キーと値のペア {#key-value-pairs}

[キーと値のペア]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs)を追加して、ユーザーデバイスに追加のカスタムフィールドを送信できます。

## ステップ 7:キャンペーンまたはキャンバスの残りの部分を構築する {#step-7-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab キャンペーン %}

キャンペーンの残りの部分を構築します。アプリ内メッセージを構築するためのツールの最適な使用方法については、以下のセクションを参照してください。

### トリガーを選択する {#choose-a-trigger}

メッセージをトリガーするアクション、およびキャンペーンまたはキャンバスの開始時間と終了時間を選択します。

{% alert important %}
カスタムイベントに基づいてアプリ内メッセージをトリガーする場合、そのカスタムイベントはSDKを使用して送信する必要があることに注意してください。
{% endalert %}

![トリガーアクションが「セッション開始」に設定されたアクションベースのキャンペーン。]({% image_buster /assets/img_archive/in_app_schedule.png %}){: style="max-width:80%"}

アプリ内メッセージの配信は、完全に以下のアクショントリガーに基づいています。

- 購入を行う
- アプリ/ウェブページを開く
- カスタムイベントを実行する（SDKを使用して送信されたイベントでのみ機能します）
- 特定のプッシュメッセージを開く
- 各ユーザーのローカルタイムに合わせて、特定の時間にキャンペーンを自動的にスケジュールして送信します。
- メッセージは、毎日、毎週（オプションで特定の曜日）、または毎月の繰り返しに設定することもできます。

開始日時を選択する必要がありますが、終了日はオプションです。終了日を設定すると、指定された日時以降にその特定のアプリ内メッセージがデバイスに表示されなくなります。

[サーバーサイドイベントトリガー]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=web)と[ローカルアプリ内メッセージ配信]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery#local-in-app-messages)については、開発者ドキュメントを参照してください。

#### オンラインとオフラインのトリガー {#online-versus-offline-triggering}

アプリ内メッセージは、メッセージとトリガーをユーザーのデバイスに送信することで機能します。アプリ内メッセージがデバイスに届くと、トリガー条件が満たされるまで表示を待ちます。アプリ内メッセージがすでにユーザーのデバイスにキャッシュされている場合、Brazeへの接続がなくてもオフラインでアプリ内メッセージをトリガーできます（たとえば、機内モードの場合）。

{% alert important %}
アプリ内メッセージが停止された後も、メッセージが停止される前にセッションを開始し、その後トリガーイベントを実行したユーザーには引き続きメッセージが表示される場合があります。これらのユーザーは、キャンペーンが停止された後でもユニークインプレッションとしてカウントされます。
{% endalert %}

### 優先度を選択する {#choose-a-priority}

最後に、アプリ内メッセージがトリガーされるアクションを選択した後、優先度も設定する必要があります。同じアクションで2つのメッセージがトリガーされた場合、優先度の高いメッセージが優先度の低いメッセージよりも先にユーザーのデバイスに表示されるようにスケジュールされます。

以下のメッセージ優先度から選択できます。

- 高優先度（他のメッセージより先に表示）
- 中優先度（デフォルト）
- 低優先度（他のメッセージの後に表示）

トリガーメッセージの優先度の高、中、低オプションはバケットであるため、複数のメッセージが同じ選択された優先度を持つことがあります。同じ優先度を共有する複数のメッセージがある場合、最も最近作成または割り当てられたメッセージが優先され、最初に表示されます。

- **デフォルト優先度バケット：**2つのキャンペーンが同じトリガーを共有し、デフォルト（中）優先度を使用している場合、最後に作成されたキャンペーンがトリガーを受け取ります。
- **特定の優先度バケット：**複数のキャンペーンが同じトリガーを共有し、特定の優先度バケットに割り当てられている場合、そのバケットに最も最近割り当てられたキャンペーンがトリガーを受け取ります。

これらのバケット内で優先度を設定するには、**正確な優先度を設定**をクリックし、キャンペーンをドラッグ＆ドロップして正しい優先度に並べ替えることができます。

![アプリ内メッセージのキャンペーンとキャンバスの優先度設定の例。]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: style="max-width:70%"}

### ターゲットユーザーを選択する {#choose-users-to-target}

次に、セグメントまたはフィルターを選択してオーディエンスを絞り込み、[ユーザーをターゲット]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)する必要があります。おおよそのセグメント人口のスナップショットが自動的に表示されます。正確なセグメントメンバーシップは、メッセージが送信される前に常に計算されることに注意してください。

{% alert note %}
アプリ内メッセージステップに遅延がある場合、セグメントメンバーシップは遅延後に評価されます。ユーザーが対象の場合、アプリ内メッセージは次の利用可能なセッションで同期されます。
{% endalert %}

#### キャンペーンの適格性とLiquidの再評価 {#re-evaluate-campaign-eligibility-and-liquid}

一部のシナリオでは、アプリ内メッセージの表示をトリガーする際にユーザーの適格性を再評価したい場合があります。例としては、頻繁に変更されるカスタム属性をターゲットにするキャンペーンや、直前のプロファイル変更を反映すべきメッセージなどがあります。

![「表示前にキャンペーンの適格性を再評価する」のチェックボックスが選択されている状態。]({% image_buster /assets/img_archive/re-evaluate-iam-membership.png %}){:style="max-width:60%"}

**Re-evaluate campaign eligibility before displaying**を選択すると、送信前にユーザーがこのメッセージの対象であることを確認するために、Brazeへの追加リクエストが行われます。さらに、メッセージが表示される前に、[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)変数や[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)がその時点でテンプレート化されます。

これにより、期限切れまたはアーカイブされたキャンペーン内のユーザーにアプリ内メッセージが送信されることを防ぎます。ユーザーの適格性を再評価しない場合、メッセージはSDK内にあり、ユーザーがトリガーするのを待っているため、キャンペーンが期限切れまたはアーカイブされた後でもユーザーはアプリ内メッセージを受信します。

{% alert note %}
このオプションを有効にすると、追加の適格性とテンプレートリクエストにより、ユーザーがアプリ内メッセージをトリガーしてからメッセージが表示されるまでにわずかな遅延（100ms未満）が発生します。
<br><br>
ユーザーがオフラインの場合や、適格性とLiquidの再評価が不要な場合は、このオプションを使用しないでください。
{% endalert %}

#### REST APIで追加されたデータをメッセージで使用する {#use-data-added-by-rest-api-in-a-message}

同じセッション内で[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)が追加したユーザーデータは、そのユーザーのアプリ内メッセージで使用できる場合があります。たとえば、ユーザーがトリガーを待っているアプリ内メッセージのオーディエンスに含まれており、セッションを開始し、同じセッション内でREST APIがプロファイルを更新した場合、**Re-evaluate campaign eligibility before displaying**が選択されていれば、その新しいデータがアプリ内メッセージに表示される可能性があります。Brazeはレンダリングの時間までアプリ内メッセージをテンプレート化しません。

1つのトリガーがBrazeにデータを送信し、同時にアプリ内メッセージを発火する場合、スケジュールされた遅延があっても、メッセージはその新しく更新されたプロファイルデータを使用できません。代わりに、データを送信するトリガーとアプリ内メッセージをトリガーするトリガーの2つの別々のトリガーを使用してください。

### コンバージョンイベントを選択する {#choose-conversion-events}

Brazeでは、キャンペーンを受信した後にユーザーが特定のアクション（[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)）を実行する頻度を追跡できます。ユーザーが指定されたアクションを実行した場合にコンバージョンがカウントされる最大30日間の時間枠を設定するオプションがあります。

{% endtab %}
{% tab キャンバス %}

まだ完了していない場合は、キャンバスコンポーネントの残りのセクションを完了してください。キャンバスの残りの部分の構築方法、多変量テストとインテリジェントセレクションの実装などの詳細については、キャンバスドキュメントの[キャンバスを構築する]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-3-build-your-canvas)ステップを参照してください。

キャンバス固有のアプリ内メッセージオプションについては、[キャンバスのアプリ内メッセージ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#messages-in-canvas)を参照してください。

{% endtab %}
{% endtabs %}

## ステップ 8:確認してデプロイする {#step-8-review-and-deploy}

キャンペーンまたはキャンバスの最後の部分の構築が完了したら、詳細を確認し、[テスト]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message)してから送信してください！

次に、[アプリ内メッセージレポート]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting)を確認して、メッセージングキャンペーンの結果にアクセスする方法を学びましょう。

## 知っておくべきこと {#things-to-know}

### アクティブなアプリ内メッセージキャンペーンの制限 {#active-in-app-message-campaign-limits}

Brazeは信頼性と速度を重視しています。必要なデータのみをBrazeに送信し、ブランドに価値を提供しなくなったキャンペーンはオフにすることをお勧めします。

アクティブな状態のままでメッセージを送信していない、または不要になったアクションベースのアプリ内メッセージキャンペーンを処理すると、お客様および他のお客様に対するBrazeサービスの全体的なパフォーマンスが低下します。これらの大量のアイドルキャンペーンを処理するために必要な追加時間により、アプリ内メッセージがエンドユーザーのデバイスに表示されるまでの時間が長くなり、エンドユーザーのエクスペリエンスに影響を与えます。

{% alert important %}
メッセージ配信の速度を最適化し、タイムアウトを防ぐために、ワークスペースごとに最大200のアクティブなアクションベースのアプリ内メッセージキャンペーンを持つことができます。これはキャンバスには適用されません。
{% endalert %}

200のカウントには、まだ終了時間に達していないアクティブなアプリ内メッセージキャンペーンと、終了時間が設定されていないものが含まれます。終了時間を過ぎたアクティブなアプリ内メッセージキャンペーンはカウントされません。Brazeの平均的な顧客は、同時にアクティブなキャンペーンが合計26件であるため、この制限が影響する可能性は低いです。

### ローカルタイム配信の評価 {#local-time-delivery-evaluation}

アプリ内メッセージキャンペーンがユーザーのローカルタイムゾーンを使用してスケジュールされている場合、キャンペーンの開始時間と終了時間の評価はデバイス自体で処理されます。

アプリ内メッセージキャンペーンは通常、アプリセッションの開始時またはリフレッシュ時にユーザーのデバイスにプッシュされます。その時点で：

1. SDKは、ユーザーがトリガーベースのアプリ内メッセージの対象かどうかを評価します。
2. デバイスは、ユーザーのトリガーイベントがキャンペーンの開始時間と終了時間（ユーザーのローカルタイムゾーンで定義）の範囲内で発生したかどうかを確認します。
3. 両方の条件が満たされた場合、アプリ内メッセージは表示の対象となります。

#### 考慮事項 {#considerations}

- ユーザーがアプリ内メッセージの配信直後にイベント（ボタンタップなど）をトリガーした場合、すべての適格性基準がまだ満たされていると仮定して、メッセージは次のセッションリフレッシュまで表示されない場合があります。
- 他のチャネルタイプと同様に、アプリ内メッセージキャンペーンは理想的には24〜48時間前に開始する必要があります。このバッファにより、ユーザーが適格性を満たし、メッセージが評価および表示されるためのセッションを開始するのに十分な時間が確保されます。