---
nav_title: カスタムキーワード処理
article_title: カスタムキーワード処理
page_order: 2
description: "このリファレンス記事では、Brazeが双方向SMS、MMS、RCSメッセージングと自動応答をどのように処理するかについて説明します。キーワードトリガーの仕組み、カスタムキーワードカテゴリ、多言語サポートについても解説しています。"
page_type: reference
channel:
  - SMS
  - MMS
  - RCS

---

# カスタムキーワード処理 {#custom-keyword-handling}

> このリファレンス記事では、Brazeが双方向SMS、MMS、RCSメッセージングと自動応答をどのように処理するかについて説明します。キーワードトリガーの仕組み、カスタムキーワードカテゴリ、多言語サポートについても解説しています。

## 双方向メッセージング（カスタムキーワード応答） {#two-way-messaging-custom-keyword-responses}

双方向メッセージングでは、メッセージを送信し、それに対する応答を処理できます。エンドユーザーがBrazeにキーワードを送信すると、そのユーザーに自動返信が届きます。正しく適用すれば、双方向メッセージングはカスタマーマーケティングにおけるシンプルで即時的かつダイナミックなソリューションとなり、時間とリソースを節約できます。

## キーワードと自動応答の管理 {#managing-keywords-and-auto-responses}

BrazeのSMS、MMS、RCSでは、キーワードトリガーの作成、カスタム応答の設定、複数言語のキーワードセットの定義、カスタムキーワードカテゴリの設定が可能です。

{% alert note %}
Brazeは、オプトアウトキーワードの完全なセット（[デフォルトキーワード]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout/)および[カスタムキーワード]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling/)）を使用して、正確なオプトアウト処理と[ファジーオプトアウト]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/fuzzy_opt_out/)を行います。
{% endalert %}

{% tabs %}
{% tab キーワードトリガーの追加 %}

### キーワードトリガーの追加 {#add-keyword-triggers}

デフォルトのオプトインおよびオプトアウトキーワードに加えて、オプトイン、オプトアウト、ヘルプの応答をトリガーする独自のキーワードを定義することもできます。

独自のキーワードを定義するには、以下の手順に従ってください。

1. Brazeダッシュボードで、**Audience** > **Subscription Group Management**に移動し、**SMS/MMS/RCS**サブスクリプショングループを選択します。
2. **Global Keywords**の下で、キーワードを追加したいキーワードカテゴリの横にある鉛筆アイコンを選択します。![鉛筆アイコンが表示されたオプトインキーワード。]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br>
3. 開いたタブで、このキーワードカテゴリをトリガーするキーワードを追加します。キーワードは大文字と小文字を区別せず、`START`、`YES`、`UNSTOP`などのユニバーサルキーワードは変更できません。![「オプトイン」カテゴリのキーワード編集画面。追加されたキーワードは「START」、「UNSTOP」、「YES」。返信メッセージフィールドには「この番号からのメッセージの配信を停止しました。ヘルプが必要な場合はHELPと返信してください。配信停止するにはSTOPと返信してください。メッセージおよびデータ料金が適用される場合があります。」と表示されています。]({% image_buster /assets/img/sms/keyword_edit2.png %})

キーワードとキーワード応答には以下のルールが適用されます。

| キーワード | キーワード応答 |
| -------- | ----------------- |
| - 有効なUTF-8エンコード文字<br>- カテゴリごとに最大20キーワード<br>- 最大34文字<br>- 最小1文字<br>- スペースを含めることはできない<br>- サブスクリプショングループ全体で大文字小文字を区別せず一意である必要がある | - 空白にはできない<br>- 最大300文字<br>- 有効なUTF-8文字 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="キーワードトリガーの追加" }

{% alert tip %}
これらのキーワードをCampaignsやCanvasesでリターゲティングやメッセージのトリガーにどのように使用できるか知りたい場合は、[ユーザーリターゲティング]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting/)をご覧ください。
{% endalert %}
{% endtab %}

{% tab 応答の管理 %}

### 応答の管理 {#manage-responses}

特定のキーワードカテゴリにキーワードをテキスト送信したユーザーに送信される応答を管理できます。

1. Brazeダッシュボードで、**Audience** > **Subscription Group Management**に移動し、**SMS/MMS/RCS**サブスクリプショングループを選択します。<br><br>
2. **Global Keywords**の下で、鉛筆アイコンを選択して応答を編集するキーワードカテゴリを選択します。![鉛筆アイコンが表示されたオプトインキーワード。]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br>
3. 開いたタブで応答を編集します。応答を作成する際は、[コンプライアンスを正しく守るための6つのルール]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations/#the-six-rules-to-get-compliance-right)に留意し、キーワードとキーワード応答に適用される以下のルールをお読みください。<br><br>
4. 応答内の静的URLを自動的に短縮するには、**Link Shortening**トグルを選択します。文字カウンターが更新され、短縮URLの予想される長さが表示されます。![「Link Shortening」トグルがオンのときに文字カウンターが更新される様子を示すGIF。]({% image_buster /assets/img/sms/link_shortening.gif %}){: style="max-width:60%;"}

#### 考慮事項 {#considerations}

| キーワード | キーワード応答 |
| -------- | ----------------- |
| - 有効なUTF-8エンコード文字<br>- カテゴリごとに最大20キーワード<br>- 最大34文字<br>- 最小1文字<br>- スペースを含めることはできない<br>- サブスクリプショングループ全体で大文字小文字を区別せず一意である必要がある | - 空白にはできない<br>- 最大300文字<br>- 有効なUTF-8文字 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="考慮事項" }

{% endtab %}
{% endtabs %}

{% alert tip %}
アクションベースのCanvasが受信SMS、MMS、またはRCSメッセージによってトリガーされた場合、Canvasの最初の[メッセージステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/)でSMS、MMS、またはRCSのプロパティを参照できます。
{% endalert %}

## 多言語サポート {#multi-language-support}

特定の国に送信する場合、送信者は現地の言語で受信キーワードと送信返信をサポートする必要がある場合があります。これをサポートするために、Brazeでは言語固有のキーワード設定を作成できます。作成すると、言語固有のキーワード設定はサブスクリプショングループ内のすべての送信番号に適用されます。
![キーワード設定として追加する言語を表示するドロップダウン。]({% image_buster /assets/img/sms/multi-language.png %}){: style="float:right;max-width:50%;margin-left:10px;"}

### 言語固有のキーワードの作成 {#creating-language-specific-keywords}

**Add a Language**を選択し、ターゲット言語を選択するか、ドロップダウン内で言語を検索します。

{% alert important %}
英語以外の言語にはプリセットのキーワードと応答が付属していないため、送信者はマーケティングチームおよび法務チームと協力して、必要なキーワードをこのセットに追加する必要があります。そうしないと、Brazeはそれらの言語のローカライズされた受信メッセージを処理しません。
{% endalert %}

言語を削除する必要がある場合は、右下の**Delete Language**ボタンを選択します。

![「イタリア語」タブが選択されたGlobal Keywordsページ。追加された各言語のタブが表示されています。]({% image_buster /assets/img/sms/multi-language2.png %})

## カスタムキーワードカテゴリ {#custom-keyword-categories}

3つのデフォルトキーワードカテゴリ（オプトイン、オプトアウト、ヘルプ）に加えて、最大25個の独自のキーワードカテゴリを作成できます。これにより、任意のキーワードを識別し、ビジネスに固有の応答を設定できます。カテゴリの例としては「PROMO」や「DISCOUNT」があり、今月実施中のプロモーションに関する応答を促すことができます。

これらのカスタムキーワードは「常時オン」の状態で動作します。つまり、メッセージサービスに購読しているユーザーは、いつでもキーワードをテキスト送信して応答を受け取ることができます。この動作に加えて、ユーザーのライフサイクルの[特定の時点](#lifecycle-specific-keywords)でのみ送信できる特定のキーワードを定義するオプションもあります。

![「Promo」カテゴリのキーワード。ユーザーが「YO」とテキスト送信すると、プロモコード付きのメッセージを受信します。]({% image_buster /assets/img/sms/sms_custom_keyword.png %})

### カスタムカテゴリの作成 {#creating-a-custom-category}

カスタムキーワードカテゴリを作成するには、以下の手順に従ってください。

1. 適切なサブスクリプショングループを編集します。
2. **Add custom keyword**を選択します。![新しいキーワードを追加するフィールド。]({% image_buster /assets/img/sms/sms_custom_step.png %}){: style="max-width:90%;"}
3. キーワードカテゴリ名を入力し、ユーザーが返信メッセージを受け取るためにテキスト送信できるキーワードを定義します。

このキーワードカテゴリが作成されると、CampaignsやCanvasesで[フィルターおよびトリガー]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting/)として利用できるようになります。

カスタムキーワードカテゴリで作成されたキーワードは、新しいキーワード作成のすべてのルールとバリデーションに準拠します。

### ライフサイクル固有のキーワード {#lifecycle-specific-keywords}

ライフサイクル中の特定の時点（例えば、最初のオンボーディング中）で顧客が特定のキーワードを送信して応答を受け取ることを制限したいユースケースがある場合は、CampaignまたはCanvasでトリガー**サブスクリプショングループ内のキーワードカテゴリOTHERへの受信SMS送信**を使用し、ユーザーが特定の時点で送信できるキーワードを定義できます。

このトリガーは、メッセージの「一致する」または「一致しない」比較、および正規表現の「マッチする」または「マッチしない」ルールを使用して、特定の受信メッセージのフィルタリングをサポートし、ユーザーの入力を検証します。

#### Canvas

![アクションベースのキャンバスステップ。トリガーはサブスクリプショングループ「Messaging Service」のキーワードカテゴリ「Other」への受信SMSの送信で、メッセージ本文が正規表現「キャレット記号skip」にマッチします。]({% image_buster /assets/img/sms/canvas_trigger.png %}){: style="max-width:90%;"}

#### Campaign

![アクションベースのCampaign。トリガーはサブスクリプショングループ「Marketing Message Service A」のキーワードカテゴリ「Other」への受信SMSの送信で、メッセージ本文が「Keyword1」または「Keyword2」であるか、「Keyword A」ではない場合です。]({% image_buster /assets/img/sms/campaign_trigger.png %}){: style="max-width:90%;"}

### 不明なキーワードへの対応 {#dealing-with-unknown-keywords}

購読中のユーザーが定義済みのキーワードに一致しないテキストを送信した場合の自動応答を設定することを強くお勧めします（**OTHER**キーワードカテゴリで処理されます）。

デフォルトの返信（例えば「申し訳ありません。そのキーワードは認識できませんでした。」）を送信するには、以下の手順に従ってください。

1. [SMSキャンペーン]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/)を作成します。
2. **ターゲットオーディエンス**で、**すべてのユーザー**を選択します（トリガーによってメッセージを受信するユーザーは制限されます）。
3. **スケジュール**で、**アクションベースの配信**を選択します。
4. トリガーを、適切なサブスクリプショングループの**キーワードカテゴリOTHER内への受信SMS送信**に設定します。
5. **Messaging**ステップで、ユーザーに受信させたい応答本文を入力します。

Brazeが**不明な**電話番号（プロファイルが存在する前）からの受信メッセージをどのように処理するかについては、[不明な電話番号の処理]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/unknown_phone_numbers/)をご覧ください。

{% alert tip %}
これらのキーワードとキーワードカテゴリをCampaignsやCanvasesでリターゲティングやメッセージのトリガーにどのように使用できるか知りたい場合は、[ユーザーリターゲティング]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting/)をご覧ください。
{% endalert %}