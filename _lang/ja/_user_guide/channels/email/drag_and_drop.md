---
nav_title: ドラッグ＆ドロップエディター
article_title: ドラッグ＆ドロップでメールを作成する
alias: /dnd/
page_order: 1
description: "この記事では、メールメッセージ用のドラッグ＆ドロップエディターの設定方法と適切な使用方法について説明します。"
channel: email
tool:
- Campaigns
- Canvas
---

# ドラッグ＆ドロップでメールを作成する {#create-an-email-with-drag-and-drop}

> ドラッグ＆ドロップエディターを使用すると、キャンペーンまたはキャンバスのいずれかで、完全にカスタムでパーソナライズされたメールメッセージを作成できます。メール本文の構築にHTMLを使用する必要はありません。

## エディターについて {#about-the-editor}

ドラッグ＆ドロップエディターは、[コンテンツ](#content)と[行](#rows)の2つの主要コンポーネントを使用して、HTMLを追加で使用することなくワークフローを簡素化します。

<table aria-label="エディターについて" style="width: 100%; table-layout: fixed;">
    <caption>コンテンツと行のエディターコンポーネント</caption>
    <thead>
    <tr>
        <th style="width: 50%;">コンテンツ</th>
        <th style="width: 50%;">行</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_content.png %}" alt="メールレイアウトのさまざまな構造的な組み合わせを含む「行」タブ" style="max-width: 100%; height: auto;">
        </td>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_rows.png %}" alt="基本、メディア、高度なブロックを含む「コンテンツ」タブ" style="max-width: 100%; height: auto;">
        </td>
    </tr>
    </tbody>
</table>
{: .reset-td-br-1 aria-label="エディターについて" }

### コンテンツ {#content}

**コンテンツ**には、メッセージで使用できるさまざまな種類のコンテンツを表す一連のタイルが含まれています。これらは基本、メディア、高度の3つのカテゴリに分類されています。

{% tabs %}
{% tab 基本 %}

基本ブロックはメールの基礎です。これらのブロックを使用して、メール本文に以下の要素を追加できます。

- タイトル
- 段落
- リスト
- ボタン
- ディバイダー
- スペーサー

{% endtab %}
{% tab メディア %}

メディアブロックを使用すると、画像、動画、ソーシャルメディアアイコンとリンク、カスタマイズ可能なアイコンなど、さまざまなビジュアルコンテンツを追加できます。

{% endtab %}
{% tab 高度 %}

ドラッグ＆ドロップエディターはこれらのブロックでワークフローを簡素化しますが、高度なブロックを使用してHTMLを挿入したり、メール本文にメニューを追加したりすることもできます。独自のHTMLを使用すると、メッセージのレンダリングに影響を与える可能性があることに注意してください。

{% endtab %}
{% endtabs %}

### 行 {#rows}

**行**は、列を使用してメッセージのセクションの水平方向の構成を定義する構造的な単位です。空の行または[Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)を使用できます。複数の列を使用すると、異なるコンテンツ要素を横に並べて配置できます。これにより、開始時に選択したテンプレートに関係なく、必要なすべての構造要素をメッセージに追加できます。

#### テキストブロック内への画像のネスト {#nesting-images-inside-text-blocks}

ドラッグ＆ドロップエディターでは、段落やその他のテキストブロック内に画像をネストすることはできません。テキストレイアウトの横や内部に画像を配置するには、**行**の列を使用します。たとえば、デスクトップ用にはその行に**モバイルで非表示**を設定した複数列の行を使用し、モバイル用には別のモバイル専用行（必要に応じて**デスクトップで非表示**および**モバイルでスタックしない**を設定）を使用して、小さな画面でも画像とテキストがきれいに並ぶようにします。

#### カードスタイル {#cards-style}

**カードスタイル**は、列間にスペースを追加し、角を丸くすることができる行プロパティです。カードスタイルのフォーマットを使用すると、新しい製品機能、お客様の声、特別オファー、ニュースの更新など、最も重要なコンテンツを目立たせるための視覚的に魅力的なレイアウトを作成できます。

## ドラッグ＆ドロップエディターの使い方 {#using-the-drag-and-drop-editor}

メールメッセージをキャンペーンで送信すべきかキャンバスで送信すべきか迷っていますか？キャンペーンは単一のターゲットメッセージングに適しており、キャンバスはマルチステップのユーザージャーニーに適しています。

{% alert note %}
キャンペーンまたはキャンバスからドラッグ＆ドロップメールを**テンプレート** > **メールテンプレート**にメールテンプレートとして直接保存することはできません。まず**テンプレート**で作成するか、[キャンペーンまたはキャンバス内で作成したドラッグ＆ドロップメールをテンプレートとして保存できますか？]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/faq#can-i-save-my-drag-and-drop-email-as-a-template-after-i-build-it-within-my-campaign-or-canvas)を参照して、ドラッグ＆ドロップテンプレートを再作成するか、**ファイルをダウンロード**でHTMLをエクスポートしてください。
{% endalert %}

メッセージの作成場所を選択したら、ドラッグ＆ドロップメールの作成手順を見ていきましょう。

### ステップ1:テンプレートを選択する {#step-1-select-your-template}

編集体験としてドラッグ＆ドロップエディターを選択した後、以下のいずれかを選択できます。

- 空白のテンプレートから始める。
- Brazeのドラッグ＆ドロップメールテンプレートを使用する。
- 保存済みのドラッグ＆ドロップメールテンプレートを使用する。

{% alert note %}
既存のカスタムHTMLテンプレートやサードパーティが作成したテンプレートを使用するには、**コンテンツ** > **メール**に移動し、編集体験として**ドラッグ＆ドロップエディター**を選択してテンプレートを再作成する必要があります。
{% endalert %}

すべてのテンプレートには**テンプレート**セクションからもアクセスできます。

テンプレートを選択すると、**メールバリアント**にメールの概要が表示され、送信情報とメール本文が確認できます。

次に、**メール本文を編集**を選択して、ドラッグ＆ドロップエディターでメールの構造をデザインします。

![メール本文の例が表示された「メールバリアント」セクション。]({% image_buster /assets/img/dnd/dnd_emailvariant.png %})

### ステップ2:メールを作成する {#step-2-build-your-email}

ドラッグ＆ドロップの編集体験は、**送信設定**、**コンテンツ**、**プレビューとテスト**の3つのセクションに分かれています。メール本文の作成は**コンテンツ**セクションで行います。メールを作成する前に、メール作成体験をガイドする主要なコンポーネントを理解しておくことが重要です。確認が必要な場合は、[エディターについて](#about-the-editor)を参照してください。

準備ができたら、ドラッグ＆ドロップのコンテンツブロックを使ってメールを作成しましょう。

1. **行**パネルを選択します。行のレイアウト設定をメインエディターにドラッグ＆ドロップします。これによりメールコンテンツのレイアウトが設定されます。
- 新しいレイアウト設定は、既存のセクションの上部または下部にドラッグする必要があります。
- 行のレイアウト設定を選択すると、行の背景色、画像、カスタム列サイズをさらにカスタマイズするための**行のプロパティ**設定が表示されます。
2. **コンテンツ**パネルを選択します。コンテンツタイルを行コンポーネントにドラッグ＆ドロップします。
- **コンテンツ**タイルをメインエディターに直接ドラッグすることもできます。タイル用の行が自動的に作成されます。
- タイルを選択し、**コンテンツプロパティ**と**ブロックオプション**のフィールドを調整することで、タイルをさらに細かく設定できます。文字間隔、パディング、行の高さなどの編集が含まれます。

ドラッグ＆ドロップメールをさらにカスタマイズする方法については、[その他のカスタマイズ](#other-customizations)を確認してください。

メールを作成しながら、デスクトップビューとモバイルビューを切り替えてプレビューし、ユーザー群にメールメッセージがどのように表示されるか確認できます。これによりコンテンツのレスポンシブ対応を確認し、必要に応じて調整できます。

{% alert tip %}
優れたコピーの作成にお困りですか？[AIコピーライティングアシスタント]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy)をお試しください。商品名や説明を入力すると、AIがメッセージングに使用できる、人間が書いたようなマーケティングコピーを生成します。

![ドラッグ＆ドロップエディターのコンテンツパネルでスタイル設定の横にあるコピーライターボタン。]({% image_buster /assets/img/ai_copywriter/ai_copywriter_dnd.png %})
{% endalert %}

### ステップ3:送信情報を追加する {#step-3-add-your-sending-information}

メールメッセージのデザインと作成が完了したら、**送信設定**セクションで送信情報を追加します。

{% multi_lang_include email/sending_info_steps.md %}

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

右側のパネルのプレビューに、追加した送信情報が表示されます。この情報は、**設定** > **メール設定** > **送信設定**に移動して更新することもできます。

#### メール添付ファイルを追加する {#add-email-attachments}

**送信設定** > **詳細設定**で、以下の方法でメール添付ファイルを追加できます。

{% multi_lang_include email/attachment_upload_options.md %}

具体的なベストプラクティスについては、[メールガイドライン]({{site.baseurl}}/user_guide/channels/email/best_practices/email_guidelines)を参照してください。

#### メールヘッダーをパーソナライズする（詳細設定） {#personalize-your-email-header-advanced}

**送信設定**では、メールヘッダーやメールエクストラにパーソナライゼーションを追加でき、他のメールサービスプロバイダーに追加データを送信できます。受信者の名前を含めるなど、メールヘッダーをパーソナライズすることで、メールが開封される可能性を高めることもできます。

{% alert note %}
詳細設定機能はキャンペーンまたはキャンバスコンポーザーに表示されます。詳細設定機能では、インラインCSSの設定を変更したり、ヘッダーや追加のキーと値のペアを入力したりできます（設定されている場合）。
{% endalert %}

### ステップ4:メールをテストする {#step-4-test-your-email}

送信情報を追加したら、いよいよメールのテストを行います。

{% alert tip %}
メールがエディターとプレビューまたはテスト送信で異なって見える場合は、すべてのタグが閉じられているか、画像属性に値が設定されているか、背景画像の端がぼやけていないかを確認してください。
{% endalert %}

**プレビューとテスト**セクションに移動します。ここでは、ユーザーとしてメールをプレビューしたり、テストメッセージを送信したりするオプションがあります。このセクションには[Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision)も含まれており、さまざまなモバイルクライアントやWebクライアントでメールが正しくレンダリングされることを確認できます。

{% alert tip %}
プレビューパネルの**ダークモードプレビュー**トグルを使って、ダークモードでメール本文を表示し、必要に応じてメールを調整することもできます。
{% endalert %}

実際のエディター、Inbox Vision、実際のテストメールで同じメールの3つの異なるバージョンを確認できるため、すべてのプラットフォームで詳細を揃えることが重要です。

#### プレビューとテスト送信 {#preview-and-test-send}

**ユーザーとしてプレビュー**タブでは、以下のユーザータイプを選択してメッセージをプレビューできます。

- **ランダムユーザー：** Brazeがデータベースからランダムにユーザーを選択し、そのユーザーの属性やイベント情報に基づいてメールをプレビューします。
- **ユーザーを選択：** メールアドレスまたはexternal IDに基づいて特定のユーザーを選択できます。そのユーザーの属性とイベント情報に基づいてメールがプレビューされます。
- **カスタムユーザー：** ユーザーをカスタマイズできます。Brazeは利用可能なすべての属性とイベントの入力欄を提供します。プレビューメールに表示したい情報を入力できます。

{% alert note %}
ランダムユーザーはセグメンテーション条件に含まれている場合もいない場合もあります。セグメンテーションは後から選択するため、この時点でBrazeはターゲットオーディエンスを認識していません。
{% endalert %}

**プレビューリンクをコピー**を選択して、ランダムユーザーに対してメールがどのように表示されるかを示す共有可能なプレビューリンクを生成してコピーすることもできます。詳細については、[共有可能なプレビュー]({{site.baseurl}}/user_guide/messaging/governance/shareable_preview)を参照してください。

![「プレビューリンクをコピー」ボタンと生成されたリンクをコピーするボタンが表示されたメールプレビュー。]({% image_buster /assets/img/dnd_email_link_preview.png %})

#### Inbox Visionを使用する {#use-inbox-vision}

Inbox Visionでは、メールクライアントやモバイルデバイスの視点からメールキャンペーンを確認できます。Inbox Visionを使ってメールメッセージをテストするには、**プレビューとテスト**セクションで**Inbox Vision**を選択し、**Inbox Visionを実行**を選択します。

メールメッセージの細部をテストして確認することが重要です。たとえば、メールメッセージの背景画像が、画像間に白い線や切れ目を生じさせたり、Windows Outlookなどのクライアントが背景画像を表示しなかったりする場合があります。Inbox Visionを使用すると、クライアント間のこれらの不一致を特定できます。このような場合は、フォールバックの背景色を設定して、画像が期待どおりにレンダリングされるようにしてください。

詳細については、[テストメッセージの送信]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=email)を参照してください。

ドラッグ＆ドロップエディターを使ってメールメッセージをデザインおよび作成した後は、キャンペーンまたはキャンバスの残りの部分を引き続き[作成]({{site.baseurl}}/user_guide/channels/email/html_editor#step-4-build-the-remainder-of-your-campaign-or-canvas)してください。

{% details 更新されたHTMLエンジンについて %}
ドラッグ＆ドロップエディターからHTMLを生成する基盤エンジンが最適化および更新され、HTMLファイルの圧縮とレンダリングに関する改善がもたらされました。

エクスポートされるHTMLデータの平均フットプリントサイズが削減され、読み込みとレンダリングの高速化、モバイルでのクリッピングの削減、帯域幅消費の削減につながっています。

HTMLレンダリングは、条件付きコメントとCSSメディアクエリの数を最小化する以下の更新に基づいて改善されました。その結果、HTMLファイルはより小さく、より効率的にコーディングされています。
- `<div>`要素ベースのデザインから標準的な`<table aria-label="Inbox Visionを使用する">`フォーマットのコードベースへの移行
  <caption>Inbox Visionを使用する</caption>
- [エディターブロック（メール）]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email)が簡潔に再コーディングされました
- 最終的なHTMLコードがタグ間の空白を除去して圧縮されます
- 透明なディバイダーは自動的にコンテンツのパディングに変換されます
{% enddetails %}

## その他のカスタマイズ {#other-customizations}

ドラッグ＆ドロップメールの作成を続ける中で、これらのクリエイティブな詳細を組み合わせて使用することで、各メール本文をさらにカスタマイズし、オーディエンスの注目と関心を引くことができます。

{% alert tip %}
[グローバルスタイル設定]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings)を使用して、ドラッグ＆ドロップエディターのカスタムテーマを作成できます。
{% endalert %}

### 自動幅画像 {#auto-width-images}

メールに追加された画像は、自動的に**自動幅**に設定されます。この設定を調整するには、**自動幅**をオフに切り替え、必要に応じて幅のパーセンテージを調整してください。

![ドラッグ＆ドロップエディターの「コンテンツ」タブにある自動幅オプション。]({% image_buster /assets/img/dnd/dnd1.png %})

### カラーレイヤリング {#color-layering}

カラーレイヤリングを使用すると、メールの背景色、コンテンツエリア、さまざまなコンテンツコンポーネントの色を変更できます。色の順序は手前から奥に向かって、コンテンツコンポーネントの色、コンテンツエリアの背景色、背景色となります。

![ドラッグ＆ドロップエディターでのカラーレイヤリングの例。]({% image_buster /assets/img/dnd/dnd2.png %})

### コンテンツのパディング {#content-padding}

![ドラッグ＆ドロップエディターのブロックオプション。]({% image_buster /assets/img/dnd/dnd3.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

パディングを調整するには、下にスクロールして**ブロックオプション**を選択し、**その他のオプション**を選択します。パディングを細かく調整して、メールの見た目を最適にできます。

### コンテンツの背景 {#content-background}

行の構成に背景画像を追加して、メールキャンペーンにより多くのデザインとビジュアルコンテンツを組み込むことができます。

### 言語属性 {#language-attribute}

**設定**タブに移動して希望の言語を選択することで、言語属性を設定できます。メッセージが動的な言語値を持つユーザーを対象としている場合は、ユーザー属性 {%raw%} `{{${language}}}` {%endraw%} をターゲットにすることもできます。

![メールの「言語」値の設定。]({% image_buster /assets/img/dnd/language_setting_dnd.png %}){: style="max-width:70%;"}

### パーソナライゼーション {#personalization}

![ドラッグ＆ドロップエディターでパーソナライゼーションを追加するオプション。]({% image_buster /assets/img/dnd/dnd4.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

ドラッグ＆ドロップメールエディターでは基本的なLiquidがサポートされています。メールにパーソナライゼーションを追加するには：

1. **コンテンツ**セクションの下にある**パーソナライゼーション**を選択します。
2. パーソナライゼーションのタイプを選択します。デフォルト（標準）属性、デバイス属性、カスタム属性などがあります。
3. 追加する属性を検索します。
4. 生成されたLiquidスニペットをコピーし、メール本文に貼り付けます。

Liquidパーソナライゼーションは、画像ブロックおよびボタンのリンクタイプフィールドではサポートされていません。

#### ダイナミック画像 {#dynamic-images}

メールメッセージングにダイナミック画像を含めるには、画像ソース属性に[Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)または[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)を含めることができます。たとえば、静的な画像の代わりに、画像URLとして {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %} を挿入して、画像にユーザーの名を含めることができます。これにより、各ユーザーに合わせてメールをパーソナライズできます。

{% alert important %}
画像URLは`https://`で始まる必要があります。`http://`を使用するとアプリがクラッシュします。
{% endalert %}

### テキストの方向 {#text-direction}

メッセージを作成する際に、それぞれの**テキストの方向**ボタンを選択して、左から右または右から左にテキストの方向を切り替えることができます。アラビア語やヘブライ語などの言語でメッセージを作成する場合に、このオプションを使用できます。

![メールのドラッグ＆ドロップエディターのメニュー。テキストの配置を右から左、左から右に切り替えるボタンがあります。]({% image_buster /assets/img/dnd/dnd_template1.png %}){: style="max-width:50%;"}

右から左のメッセージの最終的な外観は、サービスプロバイダーのレンダリング方法に大きく依存します。右から左のメッセージをできるだけ正確に表示するためのベストプラクティスについては、[右から左のメッセージの作成]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)を参照してください。

### HTML

#### リンクへのHTML属性 {#html-attributes-to-links}

![リンクの属性「clicktracking」がオフに設定されている「属性」セクション。]({% image_buster /assets/img/dnd_custom_attributes.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

ドラッグ＆ドロップエディターでリンク、ボタン、画像、動画を使用する場合、**コンテンツ**セクションの**属性**の下にある**新しい属性を追加**を選択して、メール内のHTMLタグに追加情報を付加できます。これは、メッセージのパーソナライゼーション、セグメンテーション、スタイリングに特に役立ちます。

一般的なユースケースとして、Brazeを通じて送信する際に特定のリンクのクリックトラッキングを無効にすることがあります。これは2つの方法で行えます：

- **リンクモジュールの属性を使用する場合：** リンク要素（ボタンやリンクモジュールなど）を選択し、**属性**の下にある**新しい属性を追加**を使用して追加します：
  - SendGridの場合、名前に`clicktracking`、値に`off`を使用します。
  - SparkPostの場合、名前に`data-msys-clicktrack`、値に`0`を使用します。
- **HTMLブロックを使用する場合：** HTMLブロックを挿入し、アンカータグコードにクリックトラッキング属性を直接含めます：
  - SendGridの場合、`<a href="your-url" clicktracking="off">Link text</a>`を使用します。
  - SparkPostの場合、`<a href="your-url" data-msys-clicktrack="0">Link text</a>`を使用します。

もう1つの一般的なユースケースは、特定のリンクをユニバーサルリンクとしてフラグ付けすることです。ユニバーサルリンクは、アプリにリダイレクトするリンクで、ユーザーに統合された体験を提供します。

* **SendGrid：** `universal = "true"`
* **SparkPost：** `data-msys-sublink = "open-in-app"`（[カスタムサブパス](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#custom-link-sub-paths)の設定が必要です）

ユニバーサルリンクを設定するには、[ユニバーサルリンクとApp Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links)を参照してください。

また、[Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking)や[AppsFlyer]({{site.baseurl}}/partners/message_orchestration/deeplinking/appsflyer/appsflyer#integrate-appsflyer-with-braze-for-deep-linking)などのアトリビューションパートナーと統合して、ユニバーサルリンクを管理することもできます。

最後に、メッセージをアクセシブルにするための定義済み属性が利用可能です。詳しくは、[Brazeでアクセシブルなメッセージを作成する]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility)の記事（[メールクライアントが代替テキストを表示する方法]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#how-email-clients-display-alt-text)を含む）をご覧ください。

#### カスタムheadタグ {#custom-head-tags}

`<head>`タグを使用して、メールメッセージにCSSとメタデータを追加できます。たとえば、これらのタグを使用してスタイルシートやファビコンを追加できます。`<head>`タグではLiquidがサポートされています。

`<head>`タグの外に追加されたものは、メール内の`<body>`タグの後に追加されます。つまり、追加されたコンテンツはメールに表示されます。

##### タグごとに許可されるタグと属性 {#allowed-tags-and-attributes-by-tag}

| タグ名 | 説明 | 例 |
| --- | --- | --- |
| `base` | メッセージ内のすべての相対URLの基本URLを指定します。 | `<base href="https://example.com" target="_blank">` |
| `link` | メッセージと外部リソースの関係を定義します。 | `<link href="styles.css" rel="stylesheet" type="text/css">` |
| `meta` | ページの説明やキーワードなどのメタデータを提供します。 | `<meta name="description" content="Free Web tutorials">` |
| `style` | 内部CSSスタイルを埋め込みます。 | `<style type="text/css" media="screen">body { font-size: 16px; }</style>` |
| `title` | ブラウザのタブに表示されるドキュメントのタイトルを設定します。 | `<title>StyleRyde</title>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="タグごとに許可されるタグと属性" }

| タグ | 属性 | 説明 | 例 |
| --- | --- | --- | --- |
| `base` | `href` | 相対URLに使用する基本URL。 | ```<base href="https://braze.com">``` |
| `base` | `target` | すべてのハイパーリンクとフォームのデフォルトターゲット。 | ```<base target="_blank">``` |
| `link` | `href` | 外部リソースへのURL。 | ```<link href="style.css">``` |
| `link` | `rel` | 現在のメッセージとリンクされたメッセージの関係を定義します。 | ```<link rel="stylesheet">``` |
| `link` | `type` | リンクされたリソースのタイプ。 | ```<link type="text/css">``` |
| `link` | `sizes` | アイコンのサイズを指定します。 | ```<link rel="icon" sizes="32x32" href="favicon-32.png">``` |
| `link` | `media` | スタイルが適用されるメディアまたはデバイスを指定します。 | ```<link rel="stylesheet" media="screen" href="style.css">``` |
| `meta` | `name` | ブラウザのタブに表示されるドキュメントのタイトルを設定します。 | ```<meta name="viewport" content="width=device-width, initial-scale=1">``` |
| `meta` | `content` | ブラウザのタブに表示されるドキュメントのタイトルを設定します。 | ```<meta name="description" content="Page about our newest products">``` |
| `meta` | `charset` | 文字エンコーディングを宣言します。 | ```<meta charset="UTF-8">``` |
| `meta` | `property` | ブラウザのタブに表示されるドキュメントのタイトルを設定します。 | ```<meta property="og:title" content="Website title">``` |
| `style` | `type` | スタイルコンテンツのMIMEタイプ。 | {% raw %}```<style type="text/css">p { color: red; }</style>```{% endraw %} |
| `style` | `media` | スタイルが適用されるメディアまたはデバイスを指定します。 | ```<style media="print">body { font-size: 12pt; }</style>``` |
| `title` | 属性なし | `title`タグは属性を受け付けません。 | ```<title>Kitchenerie</title>``` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="タグごとに許可されるタグと属性" }

{% alert note %}
リンク名は最大63バイトで、制限を超えると自動的に切り捨てられます。
{% endalert %}