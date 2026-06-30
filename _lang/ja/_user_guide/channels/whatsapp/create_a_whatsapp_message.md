---
nav_title: WhatsApp メッセージの作成
article_title: WhatsApp メッセージの作成
page_order: 1
description: "このリファレンス記事では、WhatsApp メッセージの構築と作成に関するステップについて説明します。"
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
search_rank: 1
---

# WhatsApp メッセージの作成 {#create-a-whatsapp-message}

> WhatsApp Campaignsは、顧客に直接リーチし、プログラムによって会話するのに最適です。Liquidやその他のダイナミックなコンテンツを使用して、ユーザーとのパーソナルな体験を作り出し、ブランドとの控えめなユーザー体験を促進・向上させる環境を構築できます。

## 前提条件 {#prerequisites}

WhatsAppメッセージを作成する前に、[WhatsAppの概要]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)から以下を確認し、完了する必要があります。
  - ポリシー、制限、コンテンツルールを確認する
  - WhatsApp接続を設定する
  - メッセージで使用する初期テンプレートをMetaで作成する

## メッセージの作成 {#creating-a-message}

### ステップ 1:メッセージの作成場所を選択する {#step-1-choose-where-to-build-your-message}

{% alert note %}
WhatsAppは言語ごとに異なる[メッセージテンプレート](#template-messages)を作成します。セグメンテーションを使用して適切なテンプレートをユーザーに配信する言語ごとのCampaignを作成するか、Canvasを使用してください。
{% endalert %}

メッセージをCampaignで送信すべきか、Canvasで送信すべきかわからない場合は、Campaignsは単一のターゲットメッセージングに適しており、Canvasesは複数ステップのユーザージャーニーに適しています。

{% tabs %}
{% tab Campaign %}

**ステップ:**

1. **Campaigns**ページに移動し、<i class="fas fa-plus"></i> **キャンペーンを作成**をクリックします。
2. **WhatsApp**を選択するか、複数チャネルをターゲットとするCampaignの場合は**マルチチャネルCampaign**を選択します。
3. Campaignにわかりやすく意味のある名前を付けます。
4. 必要に応じて[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams)と[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)を追加します。
   * タグを使用すると、Campaignsの検索やレポートの作成が容易になります。たとえば、[レポートビルダー]({{site.baseurl}}/user_guide/analytics/reports/report_builder)を使用する際に、特定のタグでフィルタリングできます。
5. Campaignに必要な数のバリアントを追加し、名前を付けます。追加した各バリアントに対して、異なるプラットフォーム、メッセージタイプ、レイアウトを選択できます。このトピックの詳細については、[多変量テストとABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)を参照してください。

{% alert tip %}
Campaign内のすべてのメッセージが類似している、または同じコンテンツを持つ場合は、追加のバリアントを追加する前にメッセージを作成してください。その後、**バリアントを追加**ドロップダウンから**バリアントからコピー**を選択できます。
{% endalert %}

{% endtab %}
{% tab Canvas %}

**ステップ:**

1. Canvasコンポーザーを使用して[Canvasを作成]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)します。
2. Canvasの設定が完了したら、Canvasビルダーでステップを追加します。ステップにわかりやすく意味のある名前を付けます。
3. [ステップスケジュール]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types#schedule-delay)を選択し、必要に応じて遅延を指定します。
4. 必要に応じて、このステップのオーディエンスをフィルタリングします。Segmentsを指定し、追加のフィルターを追加することで、このステップの受信者をさらに絞り込むことができます。オーディエンスオプションは、メッセージ送信時に遅延後にチェックされます。
5. [進行動作]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases)を選択します。
6. メッセージと組み合わせたい他のメッセージングチャネルを選択します。

{% alert tip %}
アクションベースのCanvasが受信WhatsAppメッセージによってトリガーされた場合、次のアクションパスまで、任意のキャンバスステップでWhatsAppプロパティを参照できます。
{% endalert %}

{% endtab %}
{% endtabs %}

### ステップ 2:WhatsAppメッセージを作成する {#step-2-compose-your-whatsapp-message}

ユースケースに応じて、WhatsApp[テンプレートメッセージ](#template-messages)または応答メッセージのどちらを作成するかを選択します。ビジネスが開始する会話はすべて承認済みテンプレートから開始する必要がありますが、応答メッセージは24時間の時間枠内でユーザーからの受信メッセージへの返信に使用できます。

![メッセージバリアントセクションでは、サブスクリプショングループと2つのメッセージタイプ（WhatsAppテンプレートメッセージと応答メッセージ）のいずれかを選択できます。]({% image_buster /assets/img/whatsapp/whatsapp_message_variants.png %}){: style="max-width:80%;"}

{% tabs %}
{% tab テンプレートメッセージ %}

[承認済みWhatsAppテンプレートメッセージ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup#step-3-create-whatsapp-templates
)を使用して、WhatsAppでユーザーとの会話を開始できます。これらのメッセージは事前にWhatsAppにコンテンツ承認のために送信され、承認には最大24時間かかる場合があります。コピーに加えた編集は、WhatsAppで編集して再送信する必要があります。

無効なテキストフィールド（グレーでハイライト表示）は、承認済みWhatsAppテンプレートの一部であるため編集できません。無効なテキストを更新するには、テンプレートを編集して再承認を受ける必要があります。

#### 言語 {#languages}

各テンプレートには割り当てられた言語があるため、ユーザーマッチングを正しく設定するには、言語ごとにCampaignまたはキャンバスステップを作成する必要があります。たとえば、インドネシア語と英語が割り当てられたテンプレートを使用するCanvasを構築する場合、インドネシア語テンプレート用のキャンバスステップと英語テンプレート用のキャンバスステップを作成する必要があります。

![テンプレートのリスト。メッセージのプレビュー、割り当てられた言語、承認ステータスが表示されています。]({% image_buster /assets/img/whatsapp/whatsapp_templates.png %}){: style="max-width:80%;"}

右から左に書く言語でコピーを追加する場合、右から左のメッセージの最終的な表示はサービスプロバイダーのレンダリング方法に大きく依存することに注意してください。右から左のメッセージをできるだけ正確に表示するためのベストプラクティスについては、[右から左のメッセージの作成]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)を参照してください。

#### 変数 {#variables}

Meta Business ManagerでWhatsAppテンプレートを作成する際に変数を追加した場合、それらの変数はメッセージ作成画面で空白スペースとして表示されます。これらの空白スペースをLiquidまたはプレーンテキストに置き換えてください。プレーンテキストを使用するには、二重中括弧で囲んだ「ここにテキスト」の形式を使用します。テンプレートの作成時に画像を含めることを選択した場合、メディアライブラリから画像をアップロードまたは追加するか、画像URLを参照できます。可能な限り、一貫性と信頼性を確保するために、メディアライブラリに直接画像をアップロードすることをお勧めします。

無効なテキストフィールド（グレーでハイライト表示）は、承認済みWhatsAppテンプレートの一部であるため編集できないことに注意してください。無効なテキストを更新する場合は、テンプレートを編集して再承認を受ける必要があります。

{% alert tip %}
{% raw %}
Liquidを使用する予定がある場合は、選択したパーソナライゼーションにデフォルト値を含めるようにしてください。受信者のユーザープロファイルが不完全な場合でも、メッセージを受信できるようになります。Liquid変数が欠落しているメッセージはWhatsAppから送信されません。
{% endraw %}
{% endalert %}

![パーソナライゼーション追加ツール。属性「first_name」とデフォルト値「you」が設定されています。]({% image_buster /assets/img/whatsapp/whatsapp7.png %}){: style="max-width:80%;"}

### ダイナミックリンク {#dynamic-links}

コールトゥアクションURLには変数を含めることができますが、Metaでは`{% raw %}https://example.com/{{variable}}{% endraw %}`のようにURLの末尾に配置する必要があります。変数はBrazeでLiquidに置き換えることができます。リンクはテンプレートの一部として本文テキストに含めることもできます。これらのリンクはどちらも[クリックトラッキング]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/click_tracking)を使用して短縮およびトラッキングできます。

### ダイナミック画像 {#dynamic-images}

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% endtab %}
{% tab 応答メッセージ %}

応答メッセージを使用して、ユーザーからの受信メッセージに返信できます。これらのメッセージは、作成体験中にBrazeのアプリ内で構築され、いつでも編集できます。Liquidを使用して、応答メッセージの言語を適切なユーザーに合わせることができます。

使用できる応答メッセージのレイアウトは5つあります。
- クイック返信
- テキストメッセージ
- メディアメッセージ
- コールトゥアクションボタン
- リストメッセージ

![新規ユーザーにディスカウントコードで歓迎する返信メッセージの応答メッセージコンポーザー。]({% image_buster /assets/img/whatsapp/whatsapp_response_messages.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### ステップ 3:メッセージをプレビューしてテストする {#step-3-preview-and-test-your-message}

Brazeでは、メッセージを送信する前に必ずプレビューとテストを行うことをお勧めします。**テスト**タブに切り替えて、[コンテンツテストグループ]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups)または個々のユーザーにテストWhatsAppメッセージを送信するか、Braze内でユーザーとしてメッセージを直接プレビューします。

![カスタムユーザーMaxのプレビューメッセージ。]({% image_buster /assets/img/whatsapp/whatsapp8.png %}){: style="max-width:80%;"}

{% alert note %}
応答メッセージ（テストメッセージを含む）を送信するには、会話ウィンドウが必要です。会話ウィンドウを開始するには、このメッセージに使用しているサブスクリプショングループに関連付けられた電話番号にWhatsAppメッセージを送信してください。関連付けられた電話番号は、**テスト**タブのアラートに記載されています。
{% endalert %}

![会話ウィンドウを開くためにWhatsAppメッセージを送信し、その後テストユーザーにメッセージを送信するよう案内するアラート。]({% image_buster /assets/img/whatsapp/whatsapp_test_phone_number.png %}){: style="max-width:70%;"}

詳細については、[テストメッセージの送信]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=whatsapp)を参照してください。

### ステップ 4:テスト送信結果を確認する {#step-4-view-test-send-results}

テストWhatsAppメッセージを送信した後、メッセージ作成画面で詳細な配信レポートを直接確認できます。これにより、メッセージが意図した受信者に届いたことを確認し、起動前に失敗のトラブルシューティングを行うことができます。

**テスト結果を表示**ボタンは、現在のCampaignまたはキャンバスステップのテスト送信データが利用可能な場合に表示されます。選択すると結果パネルが開きます。

結果パネルには、メッセージが受信者に届くまでに通過した各ステージが表示されます。
- **Braze:** Brazeがメッセージを正常に処理してディスパッチしたかどうか
- **Meta:** Metaがメッセージの配信を受け入れたかどうか
- **ユーザーデバイス:** メッセージが受信者のデバイスに配信されたかどうか

各ステージには現在のステータスが表示されます。ステージが失敗した場合、パネルには発生したエラーと解決方法のガイダンスが表示されます。結果は、同じCampaignまたはCanvasを閉じて再度開いても保持されます。

![2件の成功したテスト送信と1件の失敗したテスト送信を示すテスト結果パネル。]({% image_buster /assets/img/whatsapp/whatsapp_test_results.png %}){: style="max-width:80%;"}

#### リトライと過去の試行 {#retries-and-past-attempts}

テスト送信が失敗した場合、Brazeは最大24時間自動的に配信をリトライします。結果パネルには2つのタブが表示されます。

- **最新:** リトライが発生するとリアルタイムで更新される、最新の配信試行
- **過去の試行:** 以前のリトライ実行の履歴。各ステージのステータスと発生したエラーが表示されます

最終結果が確定すると（配信成功、リトライ回数の上限到達、またはリトライでは解決できない失敗）、タブはそれぞれ**結果**と**リトライ履歴**に名前が変わります。

{% alert note %}
リトライは最大24時間続く可能性があるため、送信失敗直後に最終結果が表示されない場合があります。
{% endalert %}

#### 失敗のトラブルシューティング {#troubleshoot-failures}

ステージが失敗を示している場合、パネルにはエラーと推奨される次のステップが表示されます。テスト送信が失敗する一般的な理由には以下があります。

- メッセージテンプレートがMetaで一時停止されているか、まだ承認されていない
- 受信者の電話番号がレート制限されている
- メッセージ内のLiquid変数が選択したテストユーザーに対して入力されなかった

問題が解決しない場合は、Meta Business Managerでテンプレートのステータスを確認するか、テスト受信者がBrazeで必要なユーザー属性を設定しているかを確認してください。

### ステップ 5:CampaignまたはCanvasの残りの部分を構築する {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

次に、Campaignの残りの部分を構築します。WhatsAppメッセージを構築するためのツールの最適な使用方法の詳細については、以下のセクションを参照してください。

#### 配信スケジュールまたはトリガーを選択する {#choose-a-delivery-schedule-or-trigger}

WhatsAppメッセージは、スケジュールされた時間、アクション、またはAPIトリガーに基づいて配信できます。詳細については、[Campaignのスケジュール設定]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)を参照してください。

アクションベースの配信では、Campaignの期間と[サイレント時間]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)を設定することもできます。

このステップでは、ユーザーがCampaignを[再受信可能]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#campaigns)にすることや、[フリークエンシーキャップ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#frequency-capping)ルールを有効にするなどの配信コントロールを指定することもできます。

#### ターゲットユーザーを選択する {#choose-users-to-target}

次に、Segmentsまたはフィルターを選択してオーディエンスを絞り込み、[ユーザーをターゲット]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)する必要があります。サブスクリプショングループはすでに選択されているはずで、これによりユーザーが希望するコミュニケーションのレベルやカテゴリで絞り込まれます。このステップでは、Segmentsからより大きなオーディエンスを選択し、フィルターを使用してそのセグメントをさらに絞り込みます。おおよそのセグメント人口のスナップショットが自動的に表示されます。正確なセグメントメンバーシップは、メッセージ送信前に常に計算されることに注意してください。

{% multi_lang_include audience/target_audiences.md %}

#### コンバージョンイベントを選択する {#choose-conversion-events}

Brazeでは、Campaignを受信した後にユーザーが特定のアクション（[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)）を実行する頻度をトラッキングできます。ユーザーが指定されたアクションを実行した場合にコンバージョンがカウントされる最大30日間の時間枠を設定できます。

特定のユースケースに基づいてカスタムコンバージョンイベントを設定することもできます。クリエイティブに考え、このCampaignの成功をどのように測定したいかを検討してください。

{% endtab %}

{% tab Canvas %}

まだ完了していない場合は、Canvasコンポーネントの残りのセクションを完了してください。Canvasの残りの構築方法、多変量テストとインテリジェントセレクションの実装方法などの詳細については、Canvasドキュメントの[Canvasの構築]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message)ステップを参照してください。

会話ウィンドウは受信メッセージごとに24時間しか持続しないため、Brazeは受信メッセージと応答メッセージの間に24時間を超える遅延がないことを確認します。

{% endtab %}
{% endtabs %}

### ステップ 5:確認とデプロイ {#step-5-review-and-deploy}

CampaignまたはCanvasの最後の構築が完了したら、詳細を確認し、テストしてから送信してください。

次に、[WhatsAppレポート]({{site.baseurl}}/user_guide/channels/whatsapp/reporting)を確認して、WhatsApp Campaignsの結果にアクセスする方法を学びましょう。

## サポートされているWhatsApp機能 {#supported-whatsapp-features}

### 送信メッセージ {#outbound-messages}

Brazeを通じて送信するWhatsApp送信メッセージでは、以下の機能がサポートされています。

| 機能 | 詳細 | 最大サイズ | サポートされる形式 |
| ------- | ------- | ------------- | ---------------------- |
| ヘッダーテキスト | 文字列と変数パラメーターがサポートされています。 | — | —
| 本文テキスト | 文字列と変数パラメーターがサポートされています。 | — | — |
| フッターテキスト | 文字列と変数パラメーターがサポートされています。 | — | — |
| CTAリンク | さまざまなコールトゥアクション（CTA）タイプがサポートされています。詳細については、[コールトゥアクションタイプ](#ctas)を参照してください。 | — | — |
| 画像 | 画像は本文テキスト内に埋め込むことができます。8ビットで、RGBまたはRGBAカラーモデルを使用する必要があります。 | < 5 MB | `.png`、`.jpg`、`.jpeg` |
| ドキュメント | ドキュメントは本文テキスト内に埋め込むことができます。ファイルはURL経由でホストされている必要があります。 | < 100 MB | `.txt`、`.xls`、`.xlsx`、`.doc`、`.docx`、`.ppt`、`.pttx`、`.pdf` |
| 動画 | 動画は本文テキスト内に埋め込むことができます。ファイルはURL経由または[Brazeメディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)でホストされている必要があります。 | < 16 MB | `.3gp`、`.mp4` |
| オーディオ | オーディオは応答メッセージングでのみサポートされています。ファイルはURL経由でホストされている必要があります。 | < 16 MB | `.aac`、`.amr`、`.mp3`、`.mp4`、`.ogg` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="送信メッセージ" }

{% multi_lang_include alerts/important_alerts.md alert='Meta MP4 video issue' %}

### 受信メッセージ {#inbound-messages}

Brazeを通じて受信するWhatsApp受信メッセージでは、以下の機能がサポートされています。

| 機能 | 詳細 | サポートされる形式 |
| ------- | ------- | ------------------ |
| 本文テキスト | 標準の文字列のみがサポートされています。 | — |
| 画像 | 画像は8ビットで、RGBまたはRGBAカラーモデルを使用する必要があります。ファイルは5 MB未満である必要があります。 | `.jpg`、`.png` |
| オーディオ | OpusコーデックでエンコードされたOggファイルのみがサポートされています。その他のOgg形式はサポートされていません。 | `.aac`、`.mp4`、`.mpeg`、`.amr`、`.ogg (Opus only)` |
| ドキュメント | ドキュメントはメッセージ添付ファイルを通じてサポートされています。 | `.txt`、`.pdf`、`.ppt`、`.doc`、`.xls`、`.docx`、`.pptx`、`.xlsx` |
| 動画 | H.264ビデオコーデックとAACオーディオコーデックのみがサポートされています。動画は単一のオーディオストリームを持つか、オーディオストリームを持たない必要があります。 | `.mp4`、`.3gp` |
| CTAリンク | さまざまなコールトゥアクション（CTA）タイプがサポートされています。詳細については、[コールトゥアクションタイプ](#ctas)を参照してください。 | — |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="受信メッセージ" }

### コールトゥアクションタイプ {#ctas}

Brazeを通じて送信するWhatsAppメッセージでは、以下のコールトゥアクションタイプがサポートされています。

| CTAタイプ | 詳細 |
| ----------- |---------------- |
| Webサイトにアクセス | ボタンは最大1つ（変数パラメーターを含む）。 |
| 電話番号に発信 | メッセージテンプレートでのみ利用可能。<br>ボタンは最大1つ。 |
| カスタムクイック返信ボタン | ボタンは最大3つ。 |
| マーケティングオプトアウトボタン | デフォルトでは、サブスクリプションステータスは自動的に更新されません。完全なウォークスルーについては、[オプトインとオプトアウト]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs#marketing-opt-out-selection)を参照してください。 |
| クーポンコードメッセージテンプレート | メッセージテンプレートでのみ利用可能。<br>他のメッセージテンプレートと同様に開いて編集でき、LiquidおよびBrazeプロモーションコードと互換性があります。 |
| CTA応答メッセージ | コールトゥアクションボタンを含む応答メッセージを作成します。 |
| [リスト応答メッセージ]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#list-messages) | ユーザーが選択できる最大10個のオプションのリストを含む応答メッセージを作成します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="コールトゥアクションタイプ" }