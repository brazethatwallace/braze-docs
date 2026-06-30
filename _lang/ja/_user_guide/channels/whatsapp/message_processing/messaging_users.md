---
nav_title: "ユーザーメッセージ"
article_title: "WhatsApp ユーザーメッセージ"
description: "このリファレンス記事では、Brazeがユーザーメッセージをどのように処理するかについて説明します。"
page_type: reference
channel:
  - WhatsApp
page_order: 5.1
alias: /whatsapp_quick_replies/

---

# ユーザーメッセージ {#user-messages}

> WhatsAppは双方向のコミュニケーションチャネルです。ブランドからユーザーにメッセージを送信できるだけでなく、テンプレート化されたCampaignsやCanvasesを使用して会話に参加することもできます。WhatsAppのクイック返信、リストメッセージ、トリガーワードなど、さまざまな方法があります。クイック返信やリストメッセージのコールトゥアクション（CTA）は、WhatsAppメッセージングへのユーザーエンゲージメントを促進する優れた方法です。

## アクションベースのトリガー {#action-based-triggers}

CampaignsとCanvasesはどちらも、受信WhatsAppメッセージ（ユーザーがWhatsAppにメッセージを送信すること）から開始、分岐、およびジャーニー途中の変更を行うことができます（トリガーワードなど）。

トリガーワードがユーザーから期待する内容と一致していることを確認してください。

**注意事項:**
- 設定時にトリガーワードの各文字を大文字にする必要があります。Brazeでは、ユーザーが送信する受信トリガーワードを大文字にする必要はありません。たとえば、「jOin2023」とメッセージを送信しても、CanvasまたはCampaignがトリガーされます。
- エントリスケジュールのアクションベーストリガーにトリガーワードが指定されていない場合、CampaignまたはCanvasはすべての受信WhatsAppメッセージに対して実行されます。これには、アクティブなCampaignsやCanvasesで一致するフレーズを持つメッセージも含まれ、その場合ユーザーは2つのWhatsAppメッセージを受信します。

{% tabs %}
{% tab Campaign %}

![アクションベースのCampaignスケジューリングオプション。]({% image_buster /assets/img/whatsapp/whatsapp27.png %})

{% endtab %}
{% tab Canvas %}

![アクションベースのCanvasスケジューリングオプション。]({% image_buster /assets/img/whatsapp/whatsapp25.png %})

{% endtab %}
{% endtabs %}

## 認識されない応答 {#unrecognized-responses}

インタラクティブなCanvasesに認識されない応答のオプションを含めることをお勧めします。これにより、利用可能なプロンプトをユーザーに理解させ、チャネルに対する期待値を設定できます。期待値の管理は、ライブエージェントチャットを備えたWhatsAppチャネルがある場合に特に役立ちます。
- アクションステップで、カスタムフィルターフレーズのアクショングループを作成した後、「WhatsAppメッセージを送信」の追加アクショングループを追加しますが、**メッセージ本文の条件はチェックしないでください**。これにより、「else」句と同様に、認識されないすべてのユーザー応答がキャッチされます。
- このチャネルは有人対応ではないことをユーザーに通知し、必要に応じてサポートチャネルに誘導するWhatsAppメッセージでフォローアップすることをお勧めします。

## クイック返信 {#quick-replies}

![電話画面にコールトゥアクションボタンが表示され、クリックされたボタンのテキストが返信されることを示しています。]({% image_buster /assets/img/whatsapp/whatsapp11.png %}){: style="float:right;max-width:25%;margin-left:15px;border: 0;"}

クイック返信は、会話内でクリック可能なボタンオプションとして表示されますが、ユーザーがテキストで返信したかのように動作します。Brazeはこれらを受信メッセージとして処理し、クリックされたボタンに基づいて設定された応答を返すことができます。ユーザーからの応答を作成およびフィルタリングする際に、「受信WhatsAppメッセージアクション」ステップを使用してください。

![テキストと3つのコールトゥアクションボタンを表示するWhatsAppメッセージ。]({% image_buster /assets/img/whatsapp/whatsapp13.png %}){: style="max-width:50%;"}

### Canvasでクイック返信エクスペリエンスを設定する {#configure-the-quick-reply-experience-in-canvas}

#### ステップ 1: CTAを構築する {#step-1-build-out-ctas}

まず、メッセージテンプレート内の[WhatsAppメッセージテンプレートマネージャー](https://business.facebook.com/wa/manage/message-templates/)でクイック返信CTAを構築します。

![CTAボタンの作成方法を示すWhatsAppメッセージテンプレートマネージャーUI。ボタンタイプ（カスタム）とボタンテキストを指定します。]({% image_buster /assets/img/whatsapp/whatsapp12.png %}){: style="max-width:80%;"}

テンプレートがWhatsAppに送信され承認されたら、Braze内でCanvasを構築するために使用できます。

{% alert tip %}
メッセージテンプレートの承認を受ける前にCanvasを構築できます。
{% endalert %}

#### ステップ 2: Canvasを構築する {#step-2-build-your-canvas}

次に、作成したテンプレートを含むメッセージステップを持つCanvasを構築します。

![クイック返信テンプレートが入力されたWhatsAppステップメッセージ作成画面。]({% image_buster /assets/img/whatsapp/whatsapp14.png %})

メッセージステップに続くアクションステップを作成します。このアクションステップで、クイック返信オプションごとに1つのグループを作成します。

![評価アクションが「WhatsApp受信メッセージを送信」であるCanvas。]({% image_buster /assets/img/whatsapp/whatsapp15.png %})

各クイック返信オプショングループについて、一致させるボタンと同じ正確なテキストを指定します。キーワードは大文字で入力する必要があることに注意してください。

![特定のメッセージ本文が受信されたときに送信するように設定された「WhatsApp受信メッセージを送信」アクションを持つキャンバスステップ。]({% image_buster /assets/img/whatsapp/whatsapp16.png %})

クイック返信ではなくテキストでメッセージに応答するユーザーに対してデフォルトの応答を設定したい場合は、一致するメッセージ本文のない追加グループを作成します。

この時点から、通常どおりCanvasの構築を続けてください。

### 応答 {#responses}

各応答に対して返信メッセージを設定することをお勧めします。クイック返信の範囲外の応答（事前に決められたプロンプトではなく一般的なメッセージで応答する顧客など）に対するキャッチオールオプションを用意することをお勧めします。たとえば、「申し訳ございませんが、応答を認識できませんでした。サポートに関する問題については、<サポートチャネル>にメッセージをお送りください。」

![各コールトゥアクションボタンの応答を示す構築済みのCanvas。]({% image_buster /assets/img/whatsapp/whatsapp18.png %})

応答としてのメッセージ、ユーザープロファイルの更新、Braze間のwebhookなど、Braze Canvasが提供する後続のアクションを使用できることに注意してください。

## リストメッセージ {#list-messages}

リストメッセージは、クリック可能なオプションのリストを含む本文メッセージとして表示されます。各リストには複数のセクションを含めることができ、各リストには最大10行を含めることができます。

![さまざまなファッションスタイルの行を含むWhatsAppリストメッセージの例。]({% image_buster /assets/img/whatsapp/list_message_example.png %}){: style="max-width:40%;"}

### Canvasでリストメッセージエクスペリエンスを設定する {#configure-the-list-message-experience-in-canvas}

#### ステップ 1: アクションベースのCanvasesを作成または編集する {#step-1-create-or-edit-an-existing-action-based-canvases}

WhatsAppリストメッセージは、ユーザーメッセージへの応答として送信する必要があるため、アクションベースのCanvasesにのみ追加できます。

#### ステップ 2: WhatsAppメッセージステップを作成する {#step-2-create-a-whatsapp-message-step}

WhatsApp[メッセージステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)を追加し、応答メッセージレイアウトとして**リストメッセージ**を選択します。

![「リストメッセージ」を含む、作成可能なさまざまなタイプのWhatsApp応答メッセージの選択可能なコレクション。]({% image_buster /assets/img/whatsapp/list_message_option.png %}){: style="max-width:70%;"}

ユーザーがリストを表示するために選択する**リストボタン**名を追加します。次に、**リストコンテンツ**のフィールドを使用してリストを作成します。

- **セクション:** リストアイテムをグループ化して整理するために、最大10のセクションを追加します。たとえば、衣料品小売業者は、季節のスタイル（春、夏、秋、冬など）や衣料品アイテム（トップス、ボトムス、シューズなど）でセクションを整理できます。
- **行:** すべてのセクションにわたって、最大10行（リストアイテム）を追加します。
- **行の説明（オプション）:** すべての行（リストアイテム）にオプションの説明を追加します。

![2つのセクション、複数の行、および行の説明が入力された「リストコンテンツ」セクション。]({% image_buster /assets/img/whatsapp/list_content.png %}){: style="max-width:60%;"}

セクションと行の順序を変更するには、名前の横にあるアイコンを選択してドラッグします。

![リストセクションを新しい位置にドラッグしている様子。]({% image_buster /assets/img/whatsapp/drag_list_order.png %}){: style="max-width:60%;"}

Canvasコンポーザーに戻り、メッセージステップの後に各リスト応答のグループを持つ[アクションパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)を追加します。各グループで以下を行います。

1. **受信WhatsAppサブスクリプショングループを送信**のトリガーを追加し、該当するWhatsAppサブスクリプショングループを選択します。
2. **メッセージ本文の条件**チェックボックスをオンにします。
3. 1つの行（リストアイテム）のコンテンツを指定します。

![さまざまな衣料品スタイルのグループを持つアクションパスのコンポーザー。]({% image_buster /assets/img/whatsapp/action_path_list_message.png %})

Canvasの構築を続けてください。

### 長い説明のアクションパスを作成する {#creating-actions-paths-for-long-descriptions}

行の説明がある場合は、**正規表現に一致**を使用して行を指定する必要があります。たとえば、「お気に入りのアンクルブーツの上に履ける新しいスタイル」という説明の行を指定したい場合、「ankle boots」で[正規表現]({{site.baseurl}}/user_guide/audience/segments/regex)を使用できます。

![「ankle boots」を含む応答メッセージをキャプチャするための「正規表現に一致」フィルターを使用したWhatsAppトリガー。]({% image_buster /assets/img/whatsapp/regex_list_message.png %})

## 考慮事項 {#considerations}

### 応答メッセージのタイミング要件 {#timing-requirements-for-response-messages}

応答メッセージは、ユーザーのメッセージを受信してから24時間以内に送信する必要があります。成功するエクスペリエンスの構築を支援するために、Brazeはメッセージロジックをチェックして、応答メッセージのブロックを解除する上流の受信ユーザーメッセージがあることを確認します。

以下のイベントが応答メッセージのブロックを解除します。

- 受信メッセージ
  - トリガー**WhatsApp受信メッセージを送信**を持つ[アクションパス]({{site.baseurl}}/action_paths)または[アクションベースのエントリ]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)。

![トリガー「WhatsApp受信メッセージを送信」を持つアクションベースのエントリステップ。]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message_trigger.png %})

- [APIトリガーエントリ]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery)
- 受信製品メッセージ
  - [`ecommerce.cart_updated`]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events#types-of-ecommerce-recommended-events?tab=ecommerce.cart_updated)イベント

![実行されたカスタムイベント`ecommerce.cart_updated`のトリガーを持つアクションパス。]({% image_buster /assets/img/whatsapp/ecommerce_cart_updated.png %})

### カスタム時間属性によるフィルタリング {#filtering-by-a-custom-time-attribute}

アクションベースのWhatsApp CampaignまたはCanvasのオーディエンスがカスタム時間属性の相対的な時間枠内（たとえば、現在から次の24時間の間）に依存している場合は、[時間]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes#time)で説明されているように2つのフィルターを組み合わせてください。

### 受信メディアの保存とURLの有効期限 {#inbound-media-storage-and-url-expiration}

ユーザーがメディア（画像、オーディオファイル、ドキュメントなど）を含むWhatsAppメッセージを送信した場合、Brazeはそのメディアをメッセージ受信時から30日間Amazon S3に保存します。

ただし、そのメディアのURLを参照する`inbound_media_urls` Liquidフィールドは、Brazeが受信メッセージを受け取った時点から7日間有効です。URLは受信時に一度生成され、再生成されないため、フィールドにアクセスするタイミングに関係なく7日間の有効期間が適用されます。2つの制限のうち短い方が適用されるため、実際には`inbound_media_urls`は最大7日間有効として扱う必要があります。

{% alert note %}
`inbound_media_urls`の値を後で使用するためにユーザーカスタム属性に保存する場合は、この7日間の有効期限に注意してください。有効期限が切れた後にURLにアクセスしようとすると、リンク切れになります。
{% endalert %}