---
nav_title: HTMLエディター
article_title: カスタムHTMLでメールを作成する
page_order: 2
description: "このリファレンス記事では、Brazeプラットフォームを使用してメールを作成する方法について説明します。メッセージの作成、コンテンツのプレビュー、キャンペーンやキャンバスのスケジュール設定に関するベストプラクティスも含まれています。"
tool:
  - Campaigns
channel:
  - email
search_rank: 1
---

# カスタムHTMLでメールを作成する {#create-an-email-with-custom-html}

> メールメッセージは、ユーザーが望むタイミングでコンテンツを届けるのに最適です。また、アプリをアンインストールしたユーザーを再エンゲージするための優れたツールでもあります。カスタマイズされたメールメッセージを送信することで、ユーザー体験が向上し、アプリから最大限の価値を引き出す手助けになります。

メールキャンペーンの例については、[ケーススタディ](https://www.braze.com/customers)をご覧ください。

{% alert tip %}
メールキャンペーンを初めて作成する場合は、以下のBraze Learningコースを確認することを強くお勧めします。<br><br>
- [メールのオプトインと権限](https://learning.braze.com/messaging-channels-email)
- [プロジェクト：基本的なメールマーケティングプログラムを構築する](https://learning.braze.com/project-build-a-basic-email-marketing-program)
{% endalert %}

## ステップ1:メッセージの作成場所を選択する {#step-1-choose-where-to-build-your-message}

シンプルな単一メッセージにはキャンペーンを使用します。複数ステップのユーザージャーニーにはキャンバスを使用します。

{% tabs %}
{% tab キャンペーン %}

1. **メッセージング** > **キャンペーン**に移動し、**キャンペーンを作成**を選択します。
2. **メール**を選択するか、複数チャネルを対象とするキャンペーンの場合は**マルチチャネル**を選択します。
3. キャンペーンにわかりやすく意味のある名前を付けます。
4. 必要に応じて[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams)と[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)を追加します。
   * タグを使うと、キャンペーンの検索やレポートの作成が容易になります。たとえば、[レポートビルダー]({{site.baseurl}}/user_guide/analytics/reports/report_builder)を使用する際に、特定のタグでフィルタリングできます。
5. キャンペーンに必要な数のバリアントを追加して名前を付けます。このトピックの詳細については、[多変量テストとABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)を参照してください。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似している、または同じコンテンツを持つ場合は、追加のバリアントを追加する前にメッセージを作成してください。その後、**バリアントを追加**ドロップダウンから**バリアントからコピー**を選択できます。
{% endalert %}
{% endtab %}
{% tab キャンバス %}

1. キャンバスコンポーザーを使用して[キャンバスを作成]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)します。
2. キャンバスの設定が完了したら、キャンバスビルダーでステップを追加します。ステップにわかりやすく意味のある名前を付けます。
3. [ステップスケジュール]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types)を選択し、必要に応じて遅延を指定します。
4. 必要に応じて、このステップのオーディエンスをフィルタリングします。セグメントを指定し、追加のフィルターを追加することで、このステップの受信者をさらに絞り込むことができます。オーディエンスオプションは、遅延後のメッセージ送信時にチェックされます。
5. [進行動作]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases)を選択します。
6. メッセージと組み合わせたい他のメッセージングチャネルを選択します。
{% endtab %}
{% endtabs %}

{% alert tip %}
カスタムHTMLを構築する予定で、デバイスのダークモードがオンの状態でGmailモバイルアプリの背景の一貫性を保つ必要がある場合は、[Gmailモバイルアプリとダークモードの背景色](#gmail-dark-mode)を参照してください。
{% endalert %}

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='email html editor' %}

## ステップ2:編集エクスペリエンスを選択する {#step-2-choose-your-template-and-compose-your-email}

Brazeでは、メールキャンペーンを作成する際に2つの編集エクスペリエンスを提供しています。[ドラッグ＆ドロップエディター]({{site.baseurl}}/dnd)と標準HTMLエディターです。お好みの編集エクスペリエンスに対応するタイルを選択してください。

![メール編集エクスペリエンスとして、ドラッグ＆ドロップエディター、HTMLエディター、またはテンプレートから選択する画面。]({% image_buster /assets/img_archive/choose_email_creation.png %}){: style="max-width:75%" }

次に、既存の[メールテンプレート]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template)を選択するか、ファイルから[テンプレートをアップロード]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template)するか（HTMLエディターのみ）、空白のテンプレートを使用できます。

HTMLエディターを使用していて、デバイスがダークモードの場合にGmailモバイルアプリで背景色の一貫性を保つ必要がある場合は、[Gmailモバイルアプリとダークモードの背景色](#gmail-dark-mode)を参照してください。

{% alert tip %}
メールキャンペーンごとに1つの編集エクスペリエンスを選択することをお勧めします。たとえば、1つのメールキャンペーン内で**HTML Classic**または**Block editor**のいずれかを選択し、エディター間を切り替えないようにしてください。
{% endalert %}

## ステップ3:メールを作成する {#step-3-compose-your-email}

テンプレートを選択すると、メールの概要が表示され、フルスクリーンエディターに直接移動してメールを作成したり、送信情報を変更したり、配信性やコンプライアンスに関する警告を確認したりできます。作成中は、HTML、クラシック、プレーンテキスト、[AMP]({{site.baseurl}}/user_guide/channels/email/customize/amp_for_email)タブを切り替えることができます。

![「HTMLから再生成」ボタン。]({% image_buster /assets/img_archive/regenerate_from_html.png %}){: style="max-width:30%;float:right;margin-left:15px;border:none;" }

Brazeは、プレーンテキストバージョンへの編集が検出されるまで、HTMLバージョンからプレーンテキストバージョンを自動的に更新します。Brazeが編集を検出すると、意図的な変更が行われたと判断し、プレーンテキストの更新を停止します。自動同期を復元するには、**プレーンテキスト**に移動して**HTMLから再生成**を選択します（プレーンテキストが同期していない場合にのみ表示されます）。

{% alert tip %}
正確なプレビューでメールにモーションを追加するには、JavaScriptの代わりにGIFを使用してください。ほとんどの受信トレイはJavaScriptをサポートしていません。
{% endalert %}


{% alert important %}
Brazeは、属性として参照されるHTMLイベントハンドラーを自動的に削除します。これによりHTMLが変更されるため、完了後にメールを再確認してください。[HTMLハンドラー](https://www.w3schools.com/tags/ref_eventattributes.asp)の詳細をご覧ください。
{% endalert %}

{% alert tip %}
素晴らしいコピーの作成にお困りですか？[AIコピーライティングアシスタント]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy)をお試しください。製品名や説明を入力すると、AIがメッセージングに使用できる人間らしいマーケティングコピーを生成します。

![メールコンポーザーの本文タブにある「AIコピーライターを起動」ボタン。]({% image_buster /assets/img/ai_copywriter/ai_copywriter_email.png %}){: style="max-width:80%"}
{% endalert %}

アラビア語やヘブライ語などの右から左に書く言語のメッセージ作成にお困りですか？ベストプラクティスについては、[右から左に書くメッセージの作成]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)を参照してください。

### Gmailモバイルアプリとダークモード {#gmail-dark-mode}

Gmailモバイルアプリ（AndroidおよびiOS）は、デバイスがダークモードの場合に背景色を反転させることがあります。これにより、メールの背景が画像の端や特定のブランドカラーと一致する必要があるレイアウトが崩れる可能性があります。

これを回避するには、安定した背景が必要なテーブルセルで、`background-color`の代わりに単色のCSS `linear-gradient`を使用します。Gmailは、フラットな背景色よりもこの処理を反転させる可能性が低くなります。

たとえば、セルに白い背景を維持するには、以下を使用します。

```html
<td style="background-image: linear-gradient(#ffffff, #ffffff);">
```

`#ffffff`を目的の色に置き換えてください。

{% alert note %}
このアプローチは`<table aria-label="Gmail mobile app and dark mode #gmail-dark-mode">`要素単体には確実に適用されないため、テーブルだけでなくセルにグラデーションを設定してください。
  <caption>Gmailモバイルアプリとダークモード</caption>
{% endalert %}

グラデーション構文の詳細については、[W3SchoolsのCSSグラデーション](https://www.w3schools.com/css/css3_gradients.asp)を参照してください。

### ステップ3.1:送信情報を追加する {#step-31-add-your-sending-information}

メールメッセージのデザインと構築が完了したら、**送信設定**で送信情報を追加します。

1. **送信情報**で、**差出人表示名 + アドレス**としてメールを選択します。**差出人表示名 + アドレスをカスタマイズ**を選択してカスタマイズすることもできます。
2. **返信先アドレス**としてメールを選択します。**返信先アドレスをカスタマイズ**を選択してカスタマイズすることもできます。
3. 次に、**BCCアドレス**としてメールを選択し、このアドレスにメールが表示されるようにします。
4. メールに件名を追加します。オプションで、プリヘッダーも追加できます。プリヘッダーの後に空白を追加するには、**プリヘッダーの後に空白を追加**チェックボックスを選択します。

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

右側のパネルのプレビューに、追加した送信情報が表示されます。この情報は、**設定** > **メール設定** > **送信設定**に移動して更新することもできます。

#### 詳細設定 {#advanced}

**送信設定** > **詳細設定**で、**インラインCSS**をオンにすると、最も幅広いクライアントサポートが得られます。メッセージがクリップされたり、画像が行の高さに引き伸ばされたりする場合は、インラインCSSを一時的に**オフ**にしてみてください。一部のテンプレートはインライン化なしの方がうまく動作します。

メールヘッダーやメールエクストラのパーソナライゼーションを追加して、他のメールサービスプロバイダーに追加データを送信することもできます。

##### メールの添付ファイル {#email-attachments}

以下の方法でメールに添付ファイルを追加することもできます。

- **ファイルをアップロード：** コンピューターからファイルをドラッグ＆ドロップするか、参照して直接アップロードします。Brazeはアップロード前にファイルの種類とサイズ（デフォルトで最大2&nbsp;MB）を検証し、ファイルはメディアライブラリにアップロードされます。2&nbsp;MBの制限を超えるファイルはアップロードできません。
- **メディアライブラリを使用：** [メディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)に既に保存されているアセットを参照して選択します。PDF、Word文書、Excelファイル、PowerPointプレゼンテーションがすべてサポートされています。
- **URLから追加：** ファイルを指すURLを入力し、表示ファイル名を指定します。Brazeはメール作成中に任意のURLのサイズを調べることができないため、ファイルサイズは送信時に適用されます。このフィールドではLiquidはサポートされていません。

具体的なベストプラクティスについては、[メールガイドライン]({{site.baseurl}}/user_guide/channels/email/best_practices/email_guidelines)を参照してください。

##### メールヘッダー {#email-headers}

メールヘッダーを追加するには、**新しいヘッダーを追加**を選択します。メールヘッダーには、送信されるメールに関する情報が含まれています。これらの[キーと値のペア]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs)には、通常、送信者、受信者、認証プロトコル、ルーティング情報が含まれます。Brazeは、メールが受信トレイプロバイダーに到達するために必要なRFC準拠のヘッダー情報を自動的に追加します。

Brazeでは、高度なユースケースに必要な追加のメールヘッダーを柔軟に追加できます。Brazeプラットフォームが送信時に上書きする予約フィールドがいくつかあります。

以下のキーの使用は避けてください。

<style>
#reserved-fields td {
    word-break: break-word;
    width: 33%;
}
</style>

<table aria-label="メールヘッダー" id="reserved-fields">
  <caption>メールヘッダー</caption>
<thead>
  <tr>
    <th>予約フィールド</th>
    <th></th>
    <th></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>BCC</td>
    <td>dkim-signature</td>
    <td>Reply-To</td>
  </tr>
  <tr>
    <td>CC</td>
    <td>From</td>
    <td>Subject</td>
  </tr>
  <tr>
    <td>Content-Transfer-Encoding</td>
    <td>MIME-Version</td>
    <td>To</td>
  </tr>
  <tr>
    <td>Content-Type</td>
    <td>Received</td>
    <td>x-sg-eid</td>
  </tr>
  <tr>
    <td>DKIM-Signature</td>
    <td>received</td>
    <td>x-sg-id</td>
  </tr>
</tbody>
</table>

##### メールエクストラの追加 {#adding-email-extras}

メールエクストラを使用すると、他のメールサービスプロバイダーに追加データを送信できます。これは高度なユースケースにのみ適用されるため、会社でこの設定が既に行われている場合にのみメールエクストラを使用してください。

メールエクストラを追加するには、**送信情報**に移動して**新しいエクストラを追加**を選択します。

{% alert warning %}
追加されたキーと値のペアの合計は1 KBを超えてはなりません。超えた場合、メッセージは中止されます。
{% endalert %}

メールエクストラの値はCurrentsやSnowflakeには公開されません。追加のメタデータやダイナミックな値をCurrentsやSnowflakeに送信する場合は、代わりに[`message_extras`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras)を使用してください。

### ステップ3.2:メッセージをプレビューしてテストする {#step-3b-preview-and-test-your-message}

メールの作成が完了したら、送信前にテストします。概要画面の下部から**プレビューとテスト**を選択します。

ここでは、顧客の受信トレイでメールがどのように表示されるかをプレビューできます。**ユーザーとしてプレビュー**を選択すると、ランダムなユーザーとしてメールをプレビューしたり、特定のユーザーを選択したり、カスタムユーザーを作成したりできます。これにより、Connected Contentやパーソナライゼーションの呼び出しが正しく機能しているかテストできます。

次に、**プレビューリンクをコピー**を使用して、ランダムなユーザーに対してメールがどのように表示されるかを示す共有可能なプレビューリンクを生成してコピーできます。リンクは7日間有効で、その後再生成が必要です。

デスクトップ、モバイル、プレーンテキストのビューを切り替えて、さまざまなコンテキストでメッセージがどのように表示されるかを確認することもできます。

{% alert tip %}
ダークモードユーザーにメールがどのように見えるか気になりますか？**プレビューとテスト**セクションにある**ダークモードプレビュー**トグルを選択してください（ドラッグ＆ドロップエディターのみ）。HTMLエディターを使用している場合でも、[Gmailモバイルアプリとダークモード](#gmail-dark-mode)でGmailモバイルのダークモードレンダリングに対応できます。
{% endalert %}

最終確認の準備ができたら、**テスト送信**を選択し、自分自身またはテスターグループにテストメッセージを送信して、デバイスやクライアント間でメールが正しく表示されることを確認します。

![メール作成時のテスト送信オプションとメールプレビューの例。]({% image_buster /assets/img_archive/newEmailTest.png %})

メールに問題がある場合や変更を加えたい場合は、**メールを編集**を選択してエディターに戻ります。

{% alert tip %}
プレビューテキストをサポートするメールクライアントは、利用可能なプレビューテキストスペースを埋めるのに十分な文字数を常に取得します。しかし、これによりプレビューテキストが不完全になったり、最適化されていない状態になることがあります。
<br><br>これを回避するには、目的のプレビューテキストの後に空白を作成して、メールクライアントが他の邪魔なテキストや文字をエンベロープコンテンツに取り込まないようにします。**送信設定**セクションで、**プリヘッダーの後に空白を追加**チェックボックスを選択すると、自動的に空白が追加されます。<br><br>または、より細かい制御が必要な場合は、表示したいプレビューテキストの後にゼロ幅非結合子（`&zwnj;`）とノーブレークスペース（`&nbsp;`）のチェーンを手動で追加できます。<br><br>プリヘッダーセクションのプレビューテキストの末尾に追加すると、HTMLエディター用の以下のコードで目的の空白が追加されます。<br><br>

```html
<div style="display: none; max-height: 0px; overflow: hidden;">&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;</div>
```

ドラッグ＆ドロップエディターの場合は、**送信設定**セクションのプリヘッダーに`<div>`フォーマットなしでゼロ幅非結合子（`&zwnj;`）のみを直接追加してください。
{% endalert %}

{% alert note %}
Apple Mailアプリでは、HTMLメール内の画像リンクがクリック可能であるためには`https://` URLを使用する必要があります。Apple Mailの受信者からのクリックが想定される場合は、アンカータグで囲まれた画像にセキュアリンクを使用してください。
{% endalert %}

### ステップ3.3:メールエラーを確認する {#step-33-check-for-email-errors}

送信前に、エディターが一般的な問題をフラグします。

- 差出人表示名とヘッダーが一緒に設定されていない
- 無効な差出人アドレスまたは返信先アドレス
- 重複するヘッダーキー
- Liquid構文エラー
- 完全な`<!DOCTYPE html>`を含むContent Blocks
- メール本文が400&nbsp;KBを超えている
  - クリッピングを避けるため、[102&nbsp;KB未満]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips#email-size)を目指してください。
- 空の本文または件名
- 購読解除リンクがない
- 差出人ドメインが許可リストに登録されていない（送信が大幅にスロットリングされます）

## ステップ4:キャンペーンまたはキャンバスの残りを構築する {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab キャンペーン %}
次に、キャンペーンの残りの部分を構築します。Brazeのツールを使用してメールキャンペーンを構築する方法の詳細については、以下のセクションを参照してください。

### 配信スケジュールまたはトリガーを選択する {#choose-delivery-schedule-or-trigger}

スケジュールされた時間、アクション、またはAPIトリガーに基づいてメールを配信します。詳細については、[キャンペーンのスケジュール設定]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)を参照してください。

{% alert note %}
APIトリガーキャンペーンの場合、トリガーアクションが**キャンペーンとのインタラクション**に設定されている場合、インタラクションとして**受信**オプションを選択すると、Brazeが選択したキャンペーンを送信済みとしてマークした時点で新しいキャンペーンがトリガーされます。これは、そのメッセージがバウンスしたり配信に失敗した場合でも同様です。
{% endalert %}

キャンペーンの期間を設定したり、[サイレント時間]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)を指定したり、[フリークエンシーキャップ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping)ルールを設定したりすることもできます。

### ターゲットユーザーを選択する {#choose-users-to-target}

次に、セグメントやフィルターを選択して[ユーザーをターゲット]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)します。Brazeは、メールでリーチ可能なユーザー数を含むセグメント人口のライブプレビューを表示します。正確なセグメントメンバーシップは送信直前に計算されます。

{% multi_lang_include audience/target_audiences.md %}

特定の[購読ステータス]({{site.baseurl}}/user_guide/channels/email/subscriptions)を持つユーザー（購読中でメールにオプトインしているユーザーなど）にのみキャンペーンを送信することもできます。

オプションで、セグメント内の指定された数のユーザーに配信を制限したり、キャンペーンの繰り返し時にユーザーが同じメッセージを2回受信できるようにしたりすることもできます。

{% alert note %}
新しいメールキャンペーンを作成する場合、コントロールグループはデフォルトで20%に設定されており、キャンペーンの必要に応じて調整または削除できます。
{% endalert %}

#### メールとプッシュのマルチチャネルキャンペーン {#multichannel-campaigns-with-email-and-push}

メールとプッシュの両方のチャネルをターゲットとするマルチチャネルキャンペーンでは、明示的にオプトインしたユーザーのみがメッセージを受信するようにキャンペーンを制限したい場合があります（購読中または購読解除のユーザーを除外）。たとえば、異なるオプトインステータスを持つ3人のユーザーがいるとします。

- **ユーザーA**はメールを購読中で、プッシュが有効です。このユーザーはメールを受信しませんが、プッシュを受信します。
- **ユーザーB**はメールにオプトインしていますが、プッシュは有効ではありません。このユーザーはメールを受信しますが、プッシュは受信しません。
- **ユーザーC**はメールにオプトインしており、プッシュも有効です。このユーザーはメールとプッシュの両方を受信します。

これを行うには、**オーディエンスの概要**で、このキャンペーンを「オプトインしたユーザーのみ」に送信するように選択します。このオプションにより、オプトインしたユーザーのみがメールを受信し、Brazeはデフォルトでプッシュが有効なユーザーにのみプッシュを送信します。

{% alert important %}
この設定では、**ターゲットオーディエンス**ステップにオーディエンスを単一チャネルに制限するフィルター（たとえば、`Foreground Push Enabled = True`や`Email Subscription = Opted-In`）を含めないでください。
{% endalert %}

### コンバージョンイベントを選択する {#choose-conversion-events}

Brazeでは、キャンペーンを受信した後にユーザーが特定のアクション（[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)）を実行する頻度を追跡できます。以下のアクションのいずれかをコンバージョンイベントとして指定できます。

- アプリを開く
- 購入する（一般的な購入または特定のアイテム）
- 特定のカスタムイベントを実行する
- メールを開封する

ユーザーが指定されたアクションを実行した場合にBrazeがコンバージョンをカウントする最大30日間の時間枠を設定できます。Brazeは開封とクリックを自動的に追跡しますが、[インテリジェントセレクション]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection)を使用するために、コンバージョンイベントを開封またはクリックに設定することもできます。
{% endtab %}

{% tab キャンバス %}
まだ完了していない場合は、キャンバスコンポーネントの残りのセクションを完了してください。キャンバスの残りの構築方法、多変量テストとインテリジェントセレクションの実装などの詳細については、キャンバスドキュメントの[キャンバスを構築する]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas)ステップを参照してください。
{% endtab %}
{% endtabs %}

## ステップ5:確認してデプロイする {#step-5-review-and-deploy}

最後のセクションでは、設計したキャンペーンの概要が表示されます。関連するすべての詳細を確認し、**キャンペーンを起動**を選択します。

メールキャンペーンの結果にアクセスする方法については、[メールレポート]({{site.baseurl}}/user_guide/channels/email/reporting)をご覧ください。