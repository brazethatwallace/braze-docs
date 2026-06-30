---
nav_title: クリックトラッキング
article_title: クリックトラッキング
page_order: 2
description: "このリファレンス記事では、WhatsAppメッセージでクリックトラッキングを有効にする方法、短縮リンクのテスト、トラッキングリンクでのカスタムドメインの使用などについて説明します。"
page_type: reference
alias: "/whatsapp_click_tracking/"
tool:
  - キャンペーン
channel:
  - WhatsApp
---

# クリックトラッキング {#click-tracking}

> このページでは、WhatsAppメッセージでクリックトラッキングを有効にする方法、短縮リンクのテスト、トラッキングリンクでのカスタムドメインの使用などについて説明します。

クリックトラッキングを使用すると、WhatsAppメッセージ内のリンクを誰かがタップしたタイミングを測定でき、どのコンテンツがエンゲージメントを促進しているかを明確に把握できます。BrazeはURLを短縮し、バックグラウンドでトラッキングを追加し、クリックイベントが発生するとログに記録します。

クリックトラッキングは、応答メッセージとテンプレートメッセージの両方で有効にできます。ボタンや本文テキスト内のリンクで機能し、パーソナライズ済みURLやカスタムドメインにも対応しています。有効にすると、WhatsAppパフォーマンスレポートにクリックデータが表示され、誰が何をクリックしたかに基づいてユーザーをセグメント化できます。

{% alert note %}
クリックトラッキングはディープリンクでは機能しません。BranchやAppsFlyerなどのプロバイダーからのユニバーサルリンクを短縮することはできますが、その際に発生する可能性のある問題（アトリビューションの破損やリダイレクトの発生など）についてBrazeはトラブルシューティングできません。
{% endalert %}

## 仕組み {#how-it-works}

### 応答メッセージ {#response-messages}

応答メッセージのクリックトラッキングを設定するには：
1. WebサイトURLを含むコールトゥアクション（CTA）ボタン付きの応答メッセージを作成します。
2. インターフェイスの指定されたボタンをクリックして、クリックトラッキングを有効にします。

リンクはBrazeドメイン、またはサブスクリプショングループに指定されたカスタムドメインに短縮され、ユーザーごとにパーソナライズされます。

`http://` または `https://` で始まる静的URLはすべて短縮されます。Liquidパーソナライゼーション（ユーザーレベルのトラッキングターゲティングなど）を含む短縮URLは、2か月間有効です。

![コンテンツ本文とボタンを含むWhatsAppメッセージ作成画面。]({% image_buster /assets/img/whatsapp/click_tracking/message_composer.png %})

### テンプレートメッセージ {#template-messages}

テンプレートメッセージのクリックトラッキングを有効にするには、Brazeの**WhatsAppテンプレートビルダー**を使用することをお勧めします。この方法では、URLフォーマットの要件が自動的に処理されるため、WhatsApp Business Managerで手動設定する必要はありません。

WhatsApp Business Managerで直接テンプレートを作成する場合は、[WhatsApp Business Managerからのクリックトラッキング設定](#configuring-click-tracking-from-whatsapp-business-manager)を参照してください。

#### テンプレートビルダーを使用する {#use-the-template-builder}

テンプレートビルダーでテンプレートを作成する場合、クリックトラッキングは**設定**タブで設定します。

##### ステップ 1: クリックトラッキングを有効にする {#step-1-enable-click-tracking}

テンプレートビルダーで**設定**タブに移動します。**リンクオプション**で、**クリックトラッキング**チェックボックスを選択します。有効にすると、テンプレート内のすべてのリンク（メッセージ本文とCTA Webサイトボタンの両方）が短縮されてトラッキングされます。

![テンプレートビルダーの設定タブ。リンクオプションセクションにクリックトラッキングチェックボックスが有効になっており、カスタムドメインドロップダウンが表示されています。]({% image_buster /assets/img/whatsapp/click_tracking/template_builder_settings.png %})

##### ステップ 2: カスタムドメインを選択する（オプション） {#step-2-select-a-custom-domain-optional}

**カスタムドメイン**で、短縮リンクに使用するドメインを選択します。ドロップダウンには、ワークスペースに設定されているすべてのカスタムトラッキングドメインが表示されます。選択しない場合、Brazeはデフォルトの `brz.ai` ドメインを使用します。

ドメインを追加または変更するには、**購読グループ管理**を選択します。

{% alert important %}
テンプレートがMetaに承認申請として送信された後は、トラッキングドメインを変更できません。送信前に正しいドメインを選択していることを確認してください。
{% endalert %}

##### ステップ 3: 送信先URLを追加する {#step-3-add-your-destination-urls}

**作成**タブに戻り、メッセージコンテンツを追加します。

- **CTA Webサイトボタンの場合：** **クリックトラッキングURL**フィールドに送信先URLを入力します。Brazeは送信先URLを保存し、トラッキングドメインと変数プレースホルダー{% raw %}（例：`https://brz.ai/{{1}}`）{% endraw %}を使用してボタンのWebサイトURLを自動的にフォーマットします。このプレースホルダーがMetaに送信されます。送信時に、Brazeは各ユーザーの完全なトラッキングURLを生成し、変数を入力します。
- **本文テキストリンクの場合：** 本文に直接URLを入力します。

各ボタンのトラッキングURLフォーマットは、**WebサイトURL**フィールドのすぐ下でプレビューできます（例：`https://brz.ai/XXXXXXXX`）。

![コールトゥアクションボタンセクション。Visit websiteボタンのWebサイトURLがトラッキングフォーマットで事前入力されており、送信先用のクリックトラッキングURLフィールドが表示されています。]({% image_buster /assets/img/whatsapp/click_tracking/template_builder_compose.png %}){: style="max-width:70%;"}

##### 送信後に送信先URLを更新する {#update-destination-urls-after-submission}

テンプレートがMetaに送信された後、トラッキングドメインはロックされますが、送信先URLはいつでも編集可能です。リンクの送信先を更新するには、そのボタンの**クリックトラッキングURL**フィールドを編集します。トラッキングURLフォーマットは変わりません。Brazeは送信時にユーザーを新しい送信先にリダイレクトします。

#### WhatsApp Business Managerからクリックトラッキングを設定する {#configure-click-tracking-from-whatsapp-business-manager}

テンプレートビルダーではなくWhatsApp Business Managerでテンプレートを作成する場合は、Brazeでテンプレートを使用する際にクリックトラッキングが正しく機能するように、以下の手順に従ってください。

##### ステップ 1: WhatsApp Business Managerでクリックトラッキング対応テンプレートを作成する {#step-1-build-a-click-tracking-supported-template-in-whatsapp-business-manager}

1. WhatsApp Business Managerで、カスタムドメインまたは `brz.ai` のいずれかのベースURLを作成します。
2. テンプレートに含まれるリンクがクリックトラッキングと互換性があることを確認します。
3. Brazeでキャンペーンとして設定した後は、テンプレート変数を変更しないでください。ダウンストリームの変更は反映できません。
4. CTAボタンリンクの場合、**Dynamic**を選択し、ベースURL（`brz.ai` またはカスタムドメイン）を入力します。

![コールトゥアクションを作成するセクション。]({% image_buster /assets/img/whatsapp/click_tracking/create_cta.png %}){: style="max-width:70%;"}

{: start="5"}
5. 本文テキスト内のリンクの場合、WhatsApp Business Managerでテンプレートを作成する際に、トラッキングしたい本文内のリンクに挿入されたスペースを削除します。

![コールトゥアクションのコンテンツ本文を入力するテキストボックス。]({% image_buster /assets/img/whatsapp/click_tracking/cta_textbox.png %}){: style="max-width:70%;"}

##### ステップ 2: Brazeでテンプレートを完成させる {#step-2-complete-your-template-in-braze}

作成時に、Brazeは本文テキストとCTAボタンの両方で、サポート可能なURLドメインを持つテンプレートを自動的に検出します。ステータスはテンプレートの下部に表示されます。

![クリックトラッキングのアクティブステータスを示すリンクステータスセクション。]({% image_buster /assets/img/whatsapp/click_tracking/link_status.png %}){: style="max-width:70%;"}

- **サポートされているリンク：** 一致するベースURLで送信されたリンクは、クリックトラッキングが有効になります。
- **部分的にサポートされているリンク：** テンプレート内の一部のリンクが完全なURLとして送信された場合、それらのリンクにはクリックトラッキングが**適用されません**。
- **サポートされていないリンク：** 承認済みベースURLのないリンクには、クリックトラッキング機能が**ありません**。

`brz.ai` またはカスタムドメインと一致するベースURLを持つリンクには、送信先URLを指定する必要があります。

![ボタン名、WebサイトURL、クリックトラッキングURLのフィールドを含むボタンセクション。]({% image_buster /assets/img/whatsapp/click_tracking/buttons.png %}){: style="max-width:70%;"}

{% alert important %}
**API経由でのテンプレートメッセージ送信**：WhatsAppクリックトラッキング（`brz.ai` またはカスタムトラッキングドメインとメッセージ作成画面の**クリックトラッキングURL**フィールドを使用）は、[`/messages/send` エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)を通じてWhatsAppテンプレートメッセージを送信する場合はサポートされていません。

API経由でテンプレートメッセージを送信する場合、CTA URL変数（`button_variables` を使用）を入力できますが、BrazeはAPIリクエストフローでクリックトラッキングURLやリダイレクトリンクを生成しません。クリックトラッキングを使用するには、BrazeダッシュボードからまたはBraze キャンペーントリガー経由でテンプレートを送信してください。
{% endalert %}

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

## URL内のLiquidパーソナライゼーション {#liquid-personalization-in-urls}

Braze作成画面内で直接URLをダイナミックに構築でき、URLにダイナミックなUTMパラメータを追加したり、ユーザーにユニークなリンクを送信したりできます（放棄カートや再入荷した特定の製品にユーザーを誘導するなど）。
URLは、サポートされているLiquidパーソナライゼーションタグを使用してダイナミックに生成できます。

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

以下の例のように、カスタム定義のLiquid変数の短縮もサポートしています：

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Liquid変数でレンダリングされたURLの短縮 {#shorten-urls-rendered-by-liquid-variables}

BrazeはLiquidでレンダリングされたURL（APIトリガープロパティに含まれるものも含む）を短縮します。例えば、{% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %}が有効なURLを表す場合、WhatsAppメッセージを送信する前にそのURLを短縮してトラッキングします。

## テスト {#testing}

キャンペーンまたはキャンバスを起動する前に、まずメッセージをプレビューしてテストすることがベストプラクティスです。これを行うには、**テスト**タブに移動して、コンテンツテストグループまたは個々のユーザーにWhatsAppをプレビューして送信します。

このプレビューは、関連するパーソナライゼーションと短縮URLで更新されます。

{% alert important %}
アクティブなキャンバス内で下書きが作成された場合、短縮URLは生成されません。実際の短縮URLは、キャンバスの下書きがアクティブになったときに生成されます。
{% endalert %}

## レポート {#reporting}

クリックトラッキングが有効になっている場合、またはサポートされているテンプレートで使用されている場合、WhatsAppパフォーマンステーブルには、バリアントごとのクリックイベント数と関連するクリック率を示す**Total Clicks**列が含まれます。WhatsApp指標の詳細については、[WhatsAppメッセージパフォーマンス]({{site.baseurl}}/user_guide/channels/whatsapp/reporting)を参照してください。

![WhatsAppメッセージのキャンバスステップ。]({% image_buster /assets/img/whatsapp/click_tracking/canvas_step.png %}){: style="max-width:30%;"}

クリックデータは分析ダッシュボードに自動的にレポートされます。

![WhatsAppメッセージパフォーマンステーブル。]({% image_buster /assets/img/whatsapp/click_tracking/message_performance.png %})

## ユーザーのリターゲティング {#retargeting-users}

`Clicked/Opened Step` フィルターと `clicked tracked WhatsApp link` インタラクションを使用して、リンクとのインタラクションに基づいてユーザーをセグメント化できます。

![「clicked tracked WhatsApp link」フィルターを含むフィルターグループ。]({% image_buster /assets/img/whatsapp/click_tracking/filter_group.png %})

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### URLをクリックした個々のユーザーを特定できますか？ {#do-i-know-which-individual-users-are-clicking-on-a-url}

はい。クリックトラッキングが有効になっている場合（またはテンプレート設定に基づいて有効になっている場合）、WhatsAppリターゲティングフィルターまたはCurrentsから送信されるWhatsAppクリックイベント（`users.messages.whatsapp.Click`）を活用して、URLをクリックしたユーザーをリターゲティングできます。

### WhatsAppデバイスでのプレビューはクリックとしてカウントされますか？ {#do-previews-on-the-whatsapp-device-count-as-clicks}

いいえ、WhatsAppメッセージのクリック率には影響しません。