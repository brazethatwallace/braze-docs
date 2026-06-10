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

> ドラッグ＆ドロップエディターを使用すると、CampaignまたはCanvasのいずれかで、完全にカスタムでパーソナライズされたメールメッセージを作成できます。メール本文の構築にHTMLを使用する必要はありません。

## エディターについて {#about-the-editor}

ドラッグ＆ドロップエディターは、[コンテンツ](#content)と[行](#rows)の2つの主要コンポーネントを使用してワークフローを簡素化します。HTMLを追加で使用する必要はありません。

<table aria-label="エディターについて" style="width: 100%; table-layout: fixed;">
    <caption>コンテンツと行のエディターコンポーネント</caption>
    <tr>
        <th style="width: 50%;">コンテンツ</th>
        <th style="width: 50%;">行</th>
    </tr>
    <tr>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_content.png %}" alt="メールレイアウト用のさまざまな構造の組み合わせを含む「行」タブ。" style="max-width: 100%; height: auto;">
        </td>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_rows.png %}" alt="基本ブロック、メディア、詳細設定を含む「コンテンツ」タブ。" style="max-width: 100%; height: auto;">
        </td>
    </tr>
</table>
{: .reset-td-br-1 aria-label="エディターについて" }

### コンテンツ {#content}

**コンテンツ**には、メッセージで使用できるさまざまな種類のコンテンツを表すタイルが含まれています。これらは基本、メディア、詳細設定の3つのカテゴリに分類されています。

{% tabs %}
{% tab 基本 %}

基本ブロックはメールの基盤です。これらのブロックを使用して、メール本文に以下の要素を追加できます。

- タイトル
- 段落
- リスト
- ボタン
- 区切り線
- スペーサー

{% endtab %}
{% tab メディア %}

メディアブロックを使用すると、画像、動画、ソーシャルメディアアイコンとリンク、カスタマイズ可能なアイコンなど、さまざまなビジュアルコンテンツを追加できます。

{% endtab %}
{% tab 詳細設定 %}

ドラッグ＆ドロップエディターはこれらのブロックでワークフローを簡素化しますが、詳細設定ブロックを使用してHTMLを挿入したり、メール本文にメニューを追加したりすることもできます。独自のHTMLを使用すると、メッセージのレンダリングに影響を与える場合があることに注意してください。

{% endtab %}
{% endtabs %}

### 行 {#rows}

**行**は、列を使用してメッセージのセクションの水平方向の構成を定義する構造単位です。空の行または[Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/)を使用できます。複数の列を使用すると、異なるコンテンツ要素を横に並べて配置できます。これにより、開始時に選択したテンプレートに関係なく、メッセージに必要なすべての構造要素を追加できます。

#### テキストブロック内への画像のネスト {#nesting-images-inside-text-blocks}

ドラッグ＆ドロップエディターでは、段落やその他のテキストブロック内に画像をネストすることはできません。テキストレイアウトの横や中に画像を配置するには、**行**の列を使用します。たとえば、デスクトップ用にはその行に**モバイルで非表示**を設定した複数列の行を使用し、モバイル用には別途モバイル専用の行（**デスクトップで非表示**と**モバイルでスタックしない**を必要に応じて設定）を使用することで、小さな画面でも画像とテキストがきれいに配置されます。

#### カードスタイル {#cards-style}

**カードスタイル**は、列間にスペースを追加し、角を丸くできる行プロパティです。カードスタイルのフォーマットを使用すると、新製品の機能、お客様の声、特別オファー、ニュース更新など、最も重要なコンテンツを強調するための、より視覚的に魅力的なレイアウトを作成できます。

## ドラッグ＆ドロップエディターの使用 {#using-the-drag-and-drop-editor}

メールメッセージをCampaignで送信するかCanvasで送信するか迷っていますか？Campaignは単一のターゲットメッセージングに適しており、Canvasはマルチステップのユーザージャーニーに適しています。

{% alert note %}
ドラッグ＆ドロップメールをCampaignまたはCanvasから直接**テンプレート** > **メールテンプレート**にメールテンプレートとして保存することはできません。まず**テンプレート**で構築するか、[CampaignまたはCanvas内で構築した後にドラッグ＆ドロップメールをテンプレートとして保存できますか？]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/faq/#can-i-save-my-drag-and-drop-email-as-a-template-after-i-build-it-within-my-campaign-or-canvas)を参照して、ドラッグ＆ドロップテンプレートの再作成や**ファイルをダウンロード**でHTMLをエクスポートする方法をご確認ください。
{% endalert %}

メッセージの作成場所を選択したら、ドラッグ＆ドロップメールを作成する手順を見ていきましょう。

### ステップ 1: テンプレートを選択する {#step-1-select-your-template}

編集エクスペリエンスとしてドラッグ＆ドロップエディターを選択した後、以下を選択できます。

- 空白のテンプレートから開始する。
- 事前にデザインされたBrazeのドラッグ＆ドロップメールテンプレートを使用する。
- 保存済みのドラッグ＆ドロップメールテンプレートを使用する。

{% alert note %}
既存のカスタムHTMLテンプレートやサードパーティが作成したテンプレートを使用するには、**コンテンツ** > **メール**に移動し、編集エクスペリエンスとして**ドラッグ＆ドロップエディター**を選択してテンプレートを再作成する必要があります。
{% endalert %}

すべてのテンプレートには**テンプレート**セクションからもアクセスできます。

テンプレートを選択すると、**メールバリアント**の下にメールの概要が表示されます。これには送信情報とメール本文が含まれます。

次に、**メール本文を編集**を選択して、ドラッグ＆ドロップエディターでメール構造のデザインを開始します。

![メール本文の例を含む「メールバリアント」セクション。]({% image_buster /assets/img/dnd/dnd_emailvariant.png %})

### ステップ 2: メールを構築する {#step-2-build-your-email}

ドラッグ＆ドロップの編集エクスペリエンスは、**送信設定**、**コンテンツ**、**プレビューとテスト**の3つのセクションに分かれています。メール本文構築の要となるのは**コンテンツ**セクションです。メールを構築する前に、メール構築エクスペリエンスをガイドする主要コンポーネントを理解することが重要です。確認が必要な場合は、[エディターについて](#about-the-editor)を参照してください。

準備ができたら、ドラッグ＆ドロップのコンテンツブロックを使用してメールを構築します。

1. **行**パネルを選択します。行の設定をメインエディターにドラッグ＆ドロップします。これにより、メールコンテンツのレイアウトがマッピングされます。
- 新しい設定は、既存のセクションの上部または下部にドラッグする必要があることに注意してください。
- 行の設定を選択すると、行のバックグラウンドカラー、画像、カスタム列サイズをさらにカスタマイズするための**行プロパティ**設定が表示されます。
2. **コンテンツ**パネルを選択します。目的のコンテンツタイルを行コンポーネントにドラッグ＆ドロップします。
- **コンテンツ**タイルをメインエディターに直接ドラッグすることもできます。これにより、タイル用の行が作成されます。
- タイルを選択し、**コンテンツプロパティ**と**ブロックオプション**のフィールドを調整することで、タイルをさらに細かく調整できます。これには、文字間隔、パディング、行の高さなどの編集が含まれます。

ドラッグ＆ドロップメールをさらにカスタマイズする他の方法については、[その他のカスタマイズ](#other-customizations)を確認してください。

メールを構築する際に、デスクトップビューとモバイルビューを切り替えて、ユーザーグループに対してメールメッセージングがどのように表示されるかをプレビューできます。これにより、コンテンツがレスポンシブであることを確認し、途中で必要な調整を行うことができます。

{% alert tip %}
素晴らしいコピーの作成にお困りですか？[AIコピーライティングアシスタント]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/)を使用してみてください。製品名または説明を入力すると、AIがメッセージングで使用できる人間のようなマーケティングコピーを生成します。

![ドラッグ＆ドロップエディターのコンテンツパネルのスタイル設定の横にあるコピーライターボタン。]({% image_buster /assets/img/ai_copywriter/ai_copywriter_dnd.png %})
{% endalert %}

### ステップ 3: 送信情報を追加する {#step-3-add-your-sending-information}

メールメッセージのデザインと構築が完了したら、**送信設定**セクションで送信情報を追加します。

1. **送信情報**の下で、**差出人表示名 + アドレス**としてメールを選択します。**差出人表示名 + アドレスをカスタマイズ**を選択してカスタマイズすることもできます。
2. **返信先アドレス**としてメールを選択します。**返信先アドレスをカスタマイズ**を選択してカスタマイズすることもできます。
3. 次に、**BCCアドレス**としてメールを選択して、このアドレスにメールが表示されるようにします。
4. メールに件名を追加します。オプションで、プリヘッダーとプリヘッダー後の空白も追加できます。

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

右側のパネルのプレビューに、追加した送信情報が表示されます。この情報は、**設定** > **メール設定** > **送信設定**に移動して更新することもできます。

#### メール添付ファイルの追加 {#add-email-attachments}

**送信設定** > **詳細設定**で、以下の方法でメール添付ファイルを追加できます。

- **ファイルをアップロード:** コンピューターからファイルを直接ドラッグ＆ドロップまたは参照してアップロードします。Brazeはアップロード前にファイルタイプとサイズ（デフォルトで最大2&nbsp;MB）を検証し、ファイルはメディアライブラリにアップロードされます。2&nbsp;MBの制限を超えるファイルはアップロードできません。
- **メディアライブラリを使用:** [メディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/)に既に保存されているアセットを参照して選択します。PDF、Wordドキュメント、Excelファイル、PowerPointプレゼンテーションがすべてサポートされています。
- **URLから追加:** ファイルを指すURLを入力し、表示ファイル名を指定します。Brazeはメール作成中に任意のURLのサイズを調べることができないため、ファイルサイズは送信時に適用されます。このフィールドではLiquidはサポートされていないことに注意してください。

考慮すべき具体的なベストプラクティスについては、[メールガイドライン]({{site.baseurl}}/user_guide/channels/email/best_practices/email_guidelines/)を参照してください。

#### メールヘッダーのパーソナライズ（詳細設定） {#personalize-your-email-header-advanced}

**送信設定**の下で、メールヘッダーとメールエクストラのパーソナライゼーションを追加できます。これにより、他のメールサービスプロバイダーに追加データを送信できます。受信者の名前を含めるなど、メールヘッダーをパーソナライズすることで、メールが開封される可能性を高めることもできます。

{% alert note %}
詳細設定機能は、CampaignまたはCanvasコンポーザーに表示されます。詳細設定機能では、インラインCSS設定を変更したり、ヘッダーまたは追加のキーと値のペアを入力したりできます（設定されている場合）。
{% endalert %}

### ステップ 4: メールをテストする {#step-4-test-your-email}

送信情報を追加したら、いよいよメールをテストします。

{% alert tip %}
エディターでの表示がプレビューやテスト送信と異なる場合は、すべてのタグが閉じられていること、画像属性に値があること、バックグラウンド画像の端がぼやけていないことを確認してください。
{% endalert %}

**プレビューとテスト**セクションに移動します。ここでは、ユーザーとしてメールをプレビューするか、テストメッセージを送信するオプションがあります。このセクションには[Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision/)も含まれており、さまざまなモバイルおよびWebクライアントでメールが正しくレンダリングされていることを確認できます。

{% alert tip %}
プレビューパネルの**ダークモードプレビュー**トグルを使用して、ダークモードでメール本文を表示し、必要に応じてメールを調整することもできます。
{% endalert %}

実際のエディター、Inbox Vision、実際のテストメールの3つの異なるバージョンで同じメールを表示できるため、すべてのプラットフォームで詳細を揃えることが重要です。

#### プレビューとテスト送信 {#preview-and-test-send}

**ユーザーとしてプレビュー**タブの下で、以下のユーザータイプを選択してメッセージをプレビューできます。

- **ランダムユーザー:** Brazeがデータベースからランダムにユーザーを選択し、そのユーザーの属性またはイベント情報に基づいてメールをプレビューします。
- **ユーザーを選択:** メールアドレスまたはexternal IDに基づいて特定のユーザーを選択できます。そのユーザーの属性とイベント情報に基づいてメールがプレビューされます。
- **カスタムユーザー:** ユーザーをカスタマイズできます。Brazeは利用可能なすべての属性とイベントの入力欄を提供します。プレビューメールで確認したい情報を入力できます。

{% alert note %}
ランダムユーザーは、セグメンテーション基準に含まれている場合もいない場合もあります。セグメンテーションは後で選択されるため、この時点ではBrazeはターゲットオーディエンスを認識していません。
{% endalert %}

**プレビューリンクをコピー**を選択して、ランダムユーザーに対してメールがどのように表示されるかを示す共有可能なプレビューリンクを生成してコピーすることもできます。リンクは7日間有効で、その後再生成する必要があります。

メールテンプレートに加えた編集は、以前に生成されたリンクには反映されないことに注意してください。編集を確認するには、新しいリンクプレビューを生成する必要があります。

![「プレビューリンクをコピー」ボタンと生成されたリンクをコピーするメールプレビュー。]({% image_buster /assets/img/dnd_email_link_preview.png %})

#### Inbox Visionを使用する {#use-inbox-vision}

Inbox Visionを使用すると、メールクライアントやモバイルデバイスの視点からメールCampaignを表示できます。Inbox Visionを使用してメールメッセージをテストするには、**プレビューとテスト**セクションで**Inbox Vision**を選択し、**Inbox Visionを実行**を選択します。

メールメッセージの細部をテストして確認することが重要です。たとえば、メールメッセージングのバックグラウンド画像は、画像間に白い線や途切れが表示されることがあります。また、Windows Outlookなどのクライアントではバックグラウンド画像が表示されない場合があります。Inbox Visionを使用すると、クライアント間のこれらの不一致を特定できます。このシナリオでは、フォールバックのバックグラウンドカラーを設定して、これらの画像が期待どおりにレンダリングされるようにします。

詳細については、[テストメッセージの送信]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=email)を参照してください。

ドラッグ＆ドロップエディターを使用してメールメッセージをデザインおよび作成した後、CampaignまたはCanvasの残りの部分の[構築]({{site.baseurl}}/user_guide/channels/email/html_editor/#step-4-build-the-remainder-of-your-campaign-or-canvas)を続けます。

{% details 更新されたHTMLエンジンについて %}
ドラッグ＆ドロップエディターからHTMLを生成する基盤エンジンが最適化および更新され、HTMLファイルの圧縮とレンダリングに関する改善がもたらされました。

エクスポートされるHTMLデータの平均フットプリントサイズが削減され、読み込みとレンダリングの高速化、モバイルでのクリッピングの削減、帯域幅消費の削減につながりました。

HTMLレンダリングは、条件付きコメントとCSSメディアクエリの数を最小限に抑える以下の更新に基づいて改善されました。その結果、HTMLファイルはより小さく、より効率的にコーディングされています。
- `<div>` 要素ベースのデザインから標準的な `<table aria-label="Inbox Visionを使用する">` フォーマットのコードベースへの移行
  <caption>Inbox Visionを使用する</caption>
- [エディターブロック（メール）]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=email)が簡潔さのために再コーディングされました
- 最終的なHTMLコードはタグ間の空白を削除するために圧縮されます
- 透明な区切り線はコンテンツパディングに自動的に変換されます
{% enddetails %}

## その他のカスタマイズ {#other-customizations}

ドラッグ＆ドロップメールの構築を続ける中で、これらのクリエイティブな詳細を組み合わせて使用することで、各メール本文をさらにカスタマイズし、オーディエンスの注目と関心を引くことができます。

{% alert tip %}
[グローバルスタイル設定]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings/)を使用して、ドラッグ＆ドロップエディターのカスタムテーマを作成できます。
{% endalert %}

### 自動幅画像 {#auto-width-images}

メールに追加された画像は、自動的に**自動幅**に設定されます。この設定を調整するには、**自動幅**をオフに切り替え、必要に応じて幅のパーセンテージを調整します。

![ドラッグ＆ドロップエディターのコンテンツタブの自動幅オプション。]({% image_buster /assets/img/dnd/dnd1.png %})

### カラーレイヤリング {#color-layering}

カラーレイヤリングを使用すると、メールのバックグラウンド、コンテンツエリア、およびさまざまなコンテンツコンポーネントの色を変更できます。前面から背面への色の順序は、コンテンツコンポーネントの色、コンテンツエリアのバックグラウンドカラー、バックグラウンドカラーです。

![ドラッグ＆ドロップエディターでのカラーレイヤリングの例。]({% image_buster /assets/img/dnd/dnd2.png %})

### コンテンツパディング {#content-padding}

![ドラッグ＆ドロップエディターのブロックオプション。]({% image_buster /assets/img/dnd/dnd3.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

パディングを調整するには、**ブロックオプション**までスクロールし、**その他のオプション**を選択します。パディングを微調整して、メールの見た目を完璧に仕上げることができます。

### コンテンツバックグラウンド {#content-background}

行の設定にバックグラウンド画像を追加して、メールキャンペーンにより多くのデザインとビジュアルコンテンツを組み込むことができます。

### 言語属性 {#language-attribute}

**設定**タブに移動し、目的の言語を選択することで、言語属性を設定できます。メッセージがダイナミックな言語値を持つユーザーを対象としている場合は、ユーザー属性{%raw%}`{{${language}}}`{%endraw%}をターゲットにすることもできます。

![メールの「言語」値を設定する画面。]({% image_buster /assets/img/dnd/language_setting_dnd.png %}){: style="max-width:70%;"}

### パーソナライゼーション {#personalization}

![ドラッグ＆ドロップエディターのパーソナライゼーション追加オプション。]({% image_buster /assets/img/dnd/dnd4.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

ドラッグ＆ドロップメールエディターでは基本的なLiquidがサポートされています。メールにパーソナライゼーションを追加するには：

1. **コンテンツ**セクションの下にある**パーソナライゼーション**を選択します。
2. パーソナライゼーションタイプを選択します。これには、デフォルト（標準）属性、デバイス属性、カスタム属性などが含まれます。
3. 追加する属性を検索します。
4. 生成されたLiquidスニペットをコピーして、メール本文に貼り付けます。

Liquidパーソナライゼーションは、画像ブロックとボタンリンクタイプのフィールドではサポートされていません。

#### ダイナミック画像 {#dynamic-images}

画像ソース属性に[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/#about-connected-content)または[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/)を含めることで、メールメッセージングにダイナミック画像を含めることができます。たとえば、静的な画像の代わりに、画像URLとして{% raw %}`https://example.com/images/?imageBanner={{first_name}}`{% endraw %}を挿入して、画像にユーザーの名を含めることができます。これにより、各ユーザーに合わせてメールをパーソナライズできます。

{% alert important %}
画像URLは`https://`で始まる必要があります。`http://`を使用するとアプリがクラッシュします。
{% endalert %}

### テキスト方向 {#text-direction}

メッセージを作成する際に、それぞれの**テキスト方向**ボタンを選択して、左から右と右から左のテキスト方向を切り替えることができます。アラビア語やヘブライ語などの言語でメッセージを作成する場合に、このオプションを使用できます。

![右から左と左から右のテキスト配置を切り替えるボタンを含むメールドラッグ＆ドロップエディターメニュー。]({% image_buster /assets/img/dnd/dnd_template1.png %}){: style="max-width:50%;"}

右から左のメッセージの最終的な外観は、サービスプロバイダーがどのようにレンダリングするかに大きく依存します。右から左のメッセージをできるだけ正確に表示するためのベストプラクティスについては、[右から左のメッセージの作成]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages/)を参照してください。

### HTML

#### リンクへのHTML属性 {#html-attributes-to-links}

![リンクの属性「clicktracking」がオフになっている「属性」セクション。]({% image_buster /assets/img/dnd_custom_attributes.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

ドラッグ＆ドロップエディターでリンク、ボタン、画像、動画を使用する場合、**コンテンツ**セクションの**属性**の下にある**新しい属性を追加**を選択して、メール内のHTMLタグに追加情報を付加できます。これは、メッセージのパーソナライゼーション、セグメンテーション、スタイリングに特に役立ちます。

一般的なユースケースは、Braze経由で送信する際にクリックトラッキングを無効にするために、アンカータグに属性を挿入することです。

* **SendGrid:** `clicktracking = "off"`
* **SparkPost:** `data-msys-clicktrack = "0"`

もう1つの一般的なユースケースは、特定のリンクをユニバーサルリンクとしてフラグ付けすることです。ユニバーサルリンクは、アプリにリダイレクトするリンクで、ユーザーに統合されたエクスペリエンスを提供します。

* **SendGrid:** `universal = "true"`
* **SparkPost:** `data-msys-sublink = "open-in-app"`（[カスタムサブパス](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#custom-link-sub-paths)を設定する必要があります）

ユニバーサルリンクを設定するには、[ユニバーサルリンクとApp Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links/)を参照してください。

または、[Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/)や[AppsFlyer]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/appsflyer/#email-deep-linking-and-click-tracking)などのアトリビューションパートナーと統合して、ユニバーサルリンクを管理することもできます。

最後に、メッセージをアクセシブルにするための定義済み属性が利用可能です。詳細については、[Brazeでアクセシブルなメッセージを構築する]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility/)の記事を参照してください。

#### カスタムheadタグ {#custom-head-tags}

`<head>` タグを使用して、メールメッセージにCSSとメタデータを追加します。たとえば、これらのタグを使用してスタイルシートやファビコンを追加できます。`<head>` タグではLiquidがサポートされています。

`<head>` タグの外側に追加されたものは、メール内の `<body>` タグの後に追加されます。つまり、追加されたコンテンツはメールに表示されます。

##### 許可されるタグとタグごとの属性 {#allowed-tags-and-attributes-by-tag}

| タグ名 | 説明 | 例 |
| --- | --- | --- |
| `base` | メッセージ内のすべての相対URLのベースURLを指定します。 | `<base href="https://example.com" target="_blank">` |
| `link`| メッセージと外部リソース間の関係を定義します。 | `<link href="styles.css" rel="stylesheet" type="text/css">` |
| `meta` | ページの説明やキーワードなどのメタデータを提供します。 | `<meta name="description" content="Free Web tutorials">` |
| `style` | 内部CSSスタイルを埋め込みます。 | `<style type="text/css" media="screen">body { font-size: 16px; }</style>` |
| `title` | ブラウザタブに表示されるドキュメントのタイトルを設定します。 | `<title>StyleRyde</title>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="許可されるタグとタグごとの属性" }

| タグ | 属性 | 説明 | 例 |
| --- | --- | --- | --- |
| `base` | `href` | 相対URLに使用するベースURL。 | ```<base href="https://braze.com">``` |
| `base` | `target`| すべてのハイパーリンクとフォームのデフォルトターゲット。 | ```<base target="_blank">``` |
| `link` | `href` | 外部リソースへのURL。 | ```<link href="style.css">``` |
| `link` | `rel` | 現在のメッセージとリンクされたメッセージ間の関係を定義します。 | ```<link rel="stylesheet">``` |
| `link` | `type` | リンクされたリソースのタイプ。 | ```<link type="text/css">``` |
| `link` | `sizes` | アイコンのサイズを指定します。 | ```<link rel="icon" sizes="32x32" href="favicon-32.png">``` |
| `link` | `media` | スタイルが適用されるメディアまたはデバイスを指定します。 | ```<link rel="stylesheet" media="screen" href="style.css">``` |
| `meta` | `name` | ブラウザタブに表示されるドキュメントのタイトルを設定します。 | ```<meta name="viewport" content="width=device-width, initial-scale=1">``` |
| `meta` | `content` | ブラウザタブに表示されるドキュメントのタイトルを設定します。 | ```<meta name="description" content="Page about our newest products">``` |
| `meta` | `charset` | 文字エンコーディングを宣言します。 | ```<meta charset="UTF-8">``` |
| `meta` | `property` | ブラウザタブに表示されるドキュメントのタイトルを設定します。 | ```<meta property="og:title" content="Website title">``` |
| `style` | `type` | スタイルコンテンツのMIMEタイプ。 | {% raw %}```<style type="text/css">p { color: red; }</style>```{% endraw %} |
| `style` | `media` | スタイルが適用されるメディアまたはデバイスを指定します。 | ```<style media="print">body { font-size: 12pt; }</style>``` |
| `title` | 属性なし | `title` タグは属性を受け付けません。 | ```<title>Kitchenerie</title>``` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="許可されるタグとタグごとの属性" }

{% alert note %}
リンク名は最大63バイトで、制限を超えると自動的に切り捨てられます。
{% endalert %}