---
nav_title: WhatsAppメッセージの作成
article_title: WhatsAppメッセージの作成
page_order: 1
description: "このリファレンス記事では、WhatsAppメッセージの作成方法と、WhatsApp固有のフィールド、設定、メッセージの動作について説明します。"
page_type: reference
tool:
  - Campaigns
  - Canvas
channel:
  - WhatsApp
search_rank: 1
---

# WhatsAppメッセージの作成 {#create-a-whatsapp-message}

> WhatsAppキャンペーンを使用して、顧客に直接リーチできます。Liquidやその他のダイナミックなコンテンツを使用して各メッセージをパーソナライズし、一貫したブランド体験を提供しましょう。

## 前提条件 {#prerequisites}

始める前に、以下を準備してください。

| 要件 | 説明 |
| --- | --- |
| キャンペーンまたはキャンバス | WhatsAppメッセージを作成する前に、[キャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns)または[キャンバス]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)を設定してください。 |
| WhatsAppチャネルの設定 | [WhatsApp設定フロー]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)を完了してください。ポリシーの確認、接続の設定、送信インフラの構成が含まれます。 |
| 承認済みテンプレート | ビジネス主導の送信には、Metaでテンプレートを作成し、承認を受けてください。詳しくは[WhatsApp設定のステップ3]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup#step-3-create-whatsapp-templates)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="WhatsAppメッセージの前提条件" }

## メッセージタイプ {#message-type}

WhatsAppはBrazeで2種類のメッセージタイプをサポートしています。

- **テンプレートメッセージ：** ビジネス主導の会話に使用します。テンプレートは送信前にMetaで承認を受ける必要があります。
- **応答メッセージ：** アクティブな24時間の会話時間枠内で、ユーザーからの受信メッセージに返信するために使用します。

## 購読グループ {#subscription-group}

WhatsAppメッセージのバリアントまたはキャンバスのメッセージステップごとにWhatsApp購読グループを選択します。購読グループによって、使用する送信者設定と、メッセージの受信対象となるユーザーが決まります。

## テンプレートメッセージの言語 {#languages-for-template-messages}

承認済みの各テンプレートは特定の言語に紐付けられています。複数のテンプレート言語をサポートする必要がある場合は、個別のバリアントまたはキャンバスステップを設定してください。

右から左に読む言語でコピーを追加する場合は、[右から左に読むメッセージの作成]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)を参照してください。

## メッセージの作成 {#step-2-compose-your-whatsapp-message}

メッセージ作成画面でWhatsAppコンテンツを作成します。WhatsApp固有の設定オプションについては、以下のフィールドリファレンスを使用してください。

| フィールドまたは設定 | 制御内容 | 備考 |
| --- | --- | --- |
| **購読グループ** | WhatsAppの送信者とメッセージの対象オーディエンス。 | 関連する送信電話番号は**テスト**タブのアラートに表示されます。 |
| **メッセージタイプ** | バリアントがテンプレートメッセージまたは応答メッセージを送信するかどうか。 | ビジネス主導の送信にはテンプレートが必要です。応答メッセージにはアクティブな会話時間枠が必要です。 |
| **テンプレート**（テンプレートメッセージ） | メッセージの送信に使用される承認済みのMetaテンプレート。 | メッセージ作成画面の無効化されたフィールドは承認済みテンプレートに基づいており、Metaで変更して再承認を受ける必要があります。 |
| **言語**（テンプレートメッセージ） | バリアントまたはステップに選択されたテンプレート言語。 | 受信者に正しくマッチさせるために、言語ごとにキャンペーンバリアントまたはキャンバスステップを作成してください。 |
| **変数**（テンプレートメッセージ） | テンプレート変数のプレースホルダーに挿入される値。 | 二重中括弧内にLiquidまたはプレーンテキストを使用します。プロファイルデータが欠落している場合に送信が失敗しないよう、Liquidにはデフォルト値を含めてください。 |
| **ダイナミックリンク** | パーソナライズされたコールトゥアクションURL。 | MetaではCTA URLの末尾に変数を配置する必要があります。 |
| **ダイナミック画像** | テンプレートメッセージまたは応答メッセージで使用されるメディアURLまたはメディアライブラリの画像。 | ダイナミック画像はURL内でLiquidとConnected Contentをサポートします。 |
| **応答レイアウト**（応答メッセージ） | 応答コンテンツのフォーマット。 | サポートされるレイアウトは、クイック返信、テキストメッセージ、メディアメッセージ、コールトゥアクションボタン、リストメッセージ、フローメッセージ、Meta Product Messages、カルーセルです。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="WhatsApp固有のフィールドと設定" }

{% tabs %}
{% tab テンプレートメッセージ %}

### テンプレートメッセージ {#template-messages}

[承認済みのWhatsAppテンプレートメッセージ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup#step-3-create-whatsapp-templates)を使用して、WhatsAppでの会話を開始します。テンプレートの承認はMetaが行い、最大24時間かかる場合があります。テンプレートのコピーを編集する場合は、Metaで更新し、再度承認を申請してください。

キャンペーンまたはキャンバスの作成画面を離れずに新しいテンプレートを作成して送信するには、**新しいテンプレートを作成**を選択します。カテゴリ、タイプ、および完全なビルドプロセスについては、[WhatsAppテンプレートビルダー]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder)を参照してください。

無効化されたテキストフィールド（グレーでハイライト表示）は、承認済みWhatsAppテンプレートの一部であるため編集できません。無効化されたテキストを更新するには、テンプレートを編集して再承認を受ける必要があります。

#### コンテンツフィールド {#content-fields}

変数、ダイナミックリンク、ダイナミック画像の定義については、フィールドリファレンステーブルを使用してください。このセクションでは、テンプレート固有の動作と例について説明します。

![メッセージのプレビュー、割り当てられた言語、承認ステータスを含むテンプレートの一覧。]({% image_buster /assets/img/whatsapp/whatsapp_templates.png %}){: style="max-width:80%;"}

{% alert tip %}
Liquidを使用する場合は、パーソナライゼーションフィールドにデフォルト値を含めてください。パーソナライゼーション値が欠落しているメッセージはWhatsAppによって送信されません。
{% endalert %}

![属性「first_name」とデフォルト値「you」が設定されたパーソナライゼーション追加ツール。]({% image_buster /assets/img/whatsapp/whatsapp7.png %}){: style="max-width:80%;"}

### ダイナミック画像 {#dynamic-images}

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% endtab %}
{% tab 応答メッセージ %}

### 応答メッセージ {#response-messages}

応答メッセージを使用して、アクティブな24時間の会話時間枠内にユーザーからの受信メッセージに返信します。これらのメッセージはBrazeで作成され、いつでも編集できます。

応答メッセージは以下のレイアウトをサポートしています。
- クイック返信
- テキストメッセージ
- メディアメッセージ
- コールトゥアクションボタン
- リストメッセージ
- フローメッセージ
- Meta Product Messages
- カルーセル

![新規ユーザーにディスカウントコードで歓迎する応答メッセージのメッセージ作成画面。]({% image_buster /assets/img/whatsapp/whatsapp_response_messages.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

## WhatsAppテスト送信結果 {#step-4-view-test-send-results}

WhatsAppのテストメッセージを送信した後、メッセージ作成画面で詳細な配信レポートを直接確認できます。これにより、メッセージが意図した受信者に届いたことを確認し、ローンチ前に失敗のトラブルシューティングを行うことができます。

**テスト結果を表示**ボタンは、現在のキャンペーンまたはキャンバスステップでテスト送信データが利用可能な場合に表示されます。選択すると結果パネルが開きます。

結果パネルには、メッセージが受信者に届くまでに通過した各ステージが表示されます。
- **Braze：** Brazeがメッセージの処理と送信に成功したかどうか
- **Meta：** Metaがメッセージの配信を受け付けたかどうか
- **ユーザーデバイス：** メッセージが受信者のデバイスに配信されたかどうか

各ステージには現在のステータスが表示されます。ステージが失敗した場合、パネルには発生したエラーと解決方法に関するガイダンスが表示されます。同じキャンペーンまたはキャンバスを閉じて再度開いても、結果は保持されます。

![2件の成功したテスト送信と1件の失敗したテスト送信を表示するテスト結果パネル。]({% image_buster /assets/img/whatsapp/whatsapp_test_results.png %}){: style="max-width:80%;"}

### リトライと過去の試行 {#retries-and-past-attempts}

テスト送信が失敗した場合、Brazeは最大24時間にわたって自動的に配信をリトライします。結果パネルには2つのタブが表示されます。

- **最新：** リトライが発生するたびにリアルタイムで更新される、最新の配信試行
- **過去の試行：** 過去のリトライ履歴。各リトライのステージステータスと発生したエラーが表示されます

最終結果が確定すると（配信成功、リトライ回数の上限到達、またはリトライでは解決できない失敗）、タブはそれぞれ**結果**と**リトライ履歴**に名前が変わります。

{% alert note %}
リトライは最大24時間継続する可能性があるため、送信失敗の直後に最終結果が表示されない場合があります。
{% endalert %}

### 失敗のトラブルシューティング {#troubleshoot-failures}

ステージに失敗が表示された場合、パネルにはエラーと推奨される次のステップが表示されます。テスト送信が失敗する一般的な理由には以下が含まれます。

- メッセージテンプレートがMetaで一時停止されているか、まだ承認されていない
- 受信者の電話番号がレート制限されている
- メッセージ内のLiquid変数が、選択したテストユーザーに対して正しく入力されていない

問題が解決しない場合は、Meta Businessマネージャーでテンプレートのステータスを確認するか、テスト受信者にBrazeで必要なユーザー属性が設定されているかを確認してください。

## 知っておくべきこと {#supported-whatsapp-features}

### アウトバウンドメッセージ {#outbound-messages}

Brazeを通じて送信するアウトバウンドWhatsAppメッセージでは、以下の機能がサポートされています。

| 機能 | 詳細 | 最大サイズ | サポートされるフォーマット |
| ------- | ------- | ------------- | ---------------------- |
| ヘッダーテキスト | 文字列と変数パラメーターがサポートされています。 | — | — |
| 本文テキスト | 文字列と変数パラメーターがサポートされています。 | — | — |
| フッターテキスト | 文字列と変数パラメーターがサポートされています。 | — | — |
| CTAリンク | さまざまなコールトゥアクション（CTA）タイプがサポートされています。詳細については、[コールトゥアクションタイプ](#ctas)を参照してください。 | — | — |
| 画像 | 本文テキスト内に画像を埋め込むことができます。画像は8ビットで、RGBまたはRGBAカラーモデルを使用する必要があります。 | 5 MB未満 | `.png`、`.jpg`、`.jpeg` |
| ドキュメント | 本文テキスト内にドキュメントを埋め込むことができます。ファイルはURL経由でホストされている必要があります。 | 100 MB未満 | `.txt`、`.xls`、`.xlsx`、`.doc`、`.docx`、`.ppt`、`.pttx`、`.pdf` |
| 動画 | 本文テキスト内に動画を埋め込むことができます。ファイルはURL経由または[Brazeメディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)でホストされている必要があります。 | 16 MB未満 | `.3gp`、`.mp4` |
| オーディオ | オーディオは応答メッセージングでのみサポートされています。ファイルはURL経由でホストされている必要があります。 | 16 MB未満 | `.aac`、`.amr`、`.mp3`、`.mp4`、`.ogg` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="アウトバウンドメッセージ" }

{% multi_lang_include alerts/important_alerts.md alert='Meta MP4 video issue' %}

### インバウンドメッセージ {#inbound-messages}

Brazeを通じて受信するインバウンドWhatsAppメッセージでは、以下の機能がサポートされています。

| 機能 | 詳細 | サポートされるフォーマット |
| ------- | ------- | ------------------ |
| 本文テキスト | 標準の文字列のみがサポートされています。 | — |
| 画像 | 画像は8ビットで、RGBまたはRGBAカラーモデルを使用する必要があります。ファイルは5 MB未満である必要があります。 | `.jpg`、`.png` |
| オーディオ | Opusコーデックでエンコードされたoggファイルのみがサポートされています。その他のoggフォーマットはサポートされていません。 | `.aac`、`.mp4`、`.mpeg`、`.amr`、`.ogg (Opusのみ)` |
| ドキュメント | メッセージの添付ファイルを通じてドキュメントがサポートされています。 | `.txt`、`.pdf`、`.ppt`、`.doc`、`.xls`、`.docx`、`.pptx`、`.xlsx` |
| 動画 | H.264動画コーデックとAACオーディオコーデックのみがサポートされています。動画には単一のオーディオストリームが含まれるか、オーディオストリームが含まれない必要があります。 | `.mp4`、`.3gp` |
| CTAリンク | さまざまなコールトゥアクション（CTA）タイプがサポートされています。詳細については、[コールトゥアクションタイプ](#ctas)を参照してください。 | — |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="インバウンドメッセージ" }

### コールトゥアクションタイプ {#ctas}

Brazeを通じて送信するWhatsAppメッセージでは、以下のコールトゥアクションタイプがサポートされています。

| CTAタイプ | 詳細 |
| ----------- |---------------- |
| Webサイトにアクセス | ボタンは最大1つです（変数パラメーターを含む）。 |
| 電話番号に発信 | メッセージテンプレートでのみ利用可能です。<br>ボタンは最大1つです。 |
| カスタムクイック返信ボタン | ボタンは最大3つです。 |
| マーケティングオプトアウトボタン | デフォルトでは、購読ステータスは自動的に更新されません。詳細なウォークスルーについては、[オプトインとオプトアウト]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs#marketing-opt-out-selection)を参照してください。 |
| クーポンコードメッセージテンプレート | メッセージテンプレートでのみ利用可能です。<br>他のメッセージテンプレートと同様に開いて編集でき、LiquidおよびBrazeプロモーションコードと互換性があります。 |
| CTA応答メッセージ | コールトゥアクションボタンを含む応答メッセージを作成します。 |
| [リスト応答メッセージ]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#list-messages) | ユーザーが選択できる最大10個のオプションのリストを含む応答メッセージを作成します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="コールトゥアクションタイプ #ctas" }

## 次のステップ {#next-steps}

WhatsAppメッセージの作成後、送信の構築と検証を続けます。

{% article_tiles %}
- name: キャンバスを作成する
  link: /docs/user_guide/messaging/canvas/create_a_canvas
- name: キャンペーンをスケジュールする
  link: /docs/user_guide/messaging/campaigns/schedule_your_campaign
- name: ユーザーをターゲットにする
  link: /docs/user_guide/messaging/messaging_fundamentals/target_users
- name: コンバージョンイベント
  link: /docs/user_guide/messaging/messaging_fundamentals/conversion_events
- name: テストメッセージを送信する
  link: /docs/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=whatsapp
- name: WhatsAppレポート
  link: /docs/user_guide/channels/whatsapp/reporting
{% endarticle_tiles %}