---
nav_title: メール設定
article_title: メール設定
page_type: reference
page_order: 2
description: "このリファレンス記事では、送信設定、開封トラッキングピクセル、購読ページおよびフッターなど、Brazeダッシュボードのメール設定について説明します。"
tool: Dashboard
channel: email
toc_headers: h2

---

# メール設定 {#email-preferences}

> メール設定では、カスタムフッター、カスタムオプトインおよびオプトアウトページなど、送信メールに関する特定の設定を行うことができます。これらのオプションを送信メールに含めることで、ユーザーにとってスムーズで一貫性のある体験を提供できます。

**メール設定**は、ダッシュボードの**設定**にあります。

## 送信設定 {#sending-configuration}

**送信設定**セクションのメール設定は、メールキャンペーンに含まれる詳細を決定します。特に、これらの設定は主に、ユーザーがBrazeからメールを受信したときに表示される内容に関連しています。

### 送信メール設定 {#outbound-email-settings}

メール設定を構成する際、送信メール設定では、Brazeがユーザーにメールを送信するときに使用される名前とメールアドレスを指定します。

{% tabs local %}
{% tab 表示名アドレス %}

このセクションでは、Brazeがユーザーにメールを送信するときに使用できる名前とメールアドレスを追加できます。表示名とメールアドレスは、メールキャンペーンを作成する際の**送信情報**オプションで利用できます。送信メール設定の更新は、既存の送信に遡って適用されないことに注意してください。

![さまざまな表示名とドメインのフィールドがある「送信メール設定」セクション。]({% image_buster /assets/img/email_settings/display_name_address.png %})

#### Liquidによるパーソナライズ {#personalize-with-liquid}

**差出人表示名**、**ローカルパート**、**ドメイン**フィールドで[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/)を使用して、カスタム属性に基づいて送信者名とメールアドレスを動的にテンプレート化することもできます。**ドメイン**フィールドでLiquidを使用するには、メールキャンペーンの**送信情報**オプションに移動し、**差出人表示名 + アドレスをカスタマイズ**チェックボックスを選択する必要があります。

![差出人表示名、アドレス、ドメインをカスタマイズするためのフィールドがある送信設定。]({% image_buster /assets/img/email_settings/email_campaign_domain.png %})

たとえば、条件ロジックを使用して、異なるブランドやリージョンから送信できます。

{% raw %}
```liquid
{% if ${language} == 'en' %}
English Display Name
{% elsif ${language} == 'de' %}
German Display Name
{% else %}
Default to English Display Name
{% endif %}
```
{% endraw %}

{% endtab %}
{% tab 返信先アドレス %}

このセクションでメールアドレスを追加すると、メールキャンペーンの返信先アドレスとして選択できるようになります。**Make Default**を選択して、メールアドレスをデフォルトに設定することもできます。これらのメールアドレスは、メールキャンペーンを作成する際の**送信情報**オプションで利用できます。

![複数の返信先アドレスを入力するフィールドがある「返信先アドレス」セクション。]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

#### Liquidによるパーソナライズ

**返信先アドレス**フィールドで[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/)を使用して、カスタム属性に基づいて返信先アドレスを動的にテンプレート化することもできます。たとえば、条件ロジックを使用して、異なるリージョンや部門に返信を送信できます。

{% raw %}
```liquid
{% if {{custom_attribute.${region}}} == 'US' %}
{% assign address = "us-support@company.com" %}
{% elsif {{custom_attribute.${region}}} == 'EU' %}
{% assign address = "eu-support@company.com" %}
{% else %}
{% assign address = "global-support@company.com" %}{% endif %}{{address}}
```
{% endraw %}

{% endtab %}
{% tab BCCアドレス %}

このセクションでは、Brazeから送信される送信メールメッセージに追加できるBCCアドレスを管理できます。メールメッセージにBCCアドレスを追加すると、ユーザーが受信するメッセージの同一コピーがBCC受信トレイに送信されます。これは、コンプライアンス要件やカスタマーサポートの問題に対応するために、ユーザーに送信したメッセージのコピーを保持するのに便利なツールです。BCCメールはメールレポートや分析には含まれません。

BCCアドレスはAmazon SES、SendGrid、SparkPostで利用できます。BCCアドレスの代替として、アーカイブやコンプライアンスの目的でユーザーに送信されたメッセージのコピーを保存するために、[メッセージアーカイブ]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/message_archiving/)の使用をお勧めします。

{% multi_lang_include alerts/important_alerts.md alert='BCC address billable emails' %}

アドレスを追加すると、Campaignsまたはキャンバスステップでメールを作成する際に選択できるようになります。アドレスの横にある**Make Default**を選択すると、新しいメールキャンペーンまたはCanvasコンポーネントを起動する際にデフォルトで選択されるアドレスを設定できます。メッセージレベルでこれを上書きするには、メッセージの設定時に**No BCC**を選択します。

Brazeから送信されるすべてのメールメッセージにBCCアドレスを含めることを必須にする場合は、**Require a BCC address for all your email campaigns**トグルを選択できます。これにより、デフォルトアドレスの選択が必要になり、新しいメールキャンペーンまたはキャンバスステップに自動的に選択されます。デフォルトアドレスは、REST API経由でトリガーされるすべてのメッセージにも自動的に追加されます。アドレスを含めるために既存のAPIリクエストを変更する必要はありません。

#### ダイナミックBCC {#dynamic-bcc}

ダイナミックBCCを使用すると、BCCアドレスでLiquidを使用できます。この機能は**メール設定**でのみ利用可能で、キャンペーン自体では設定できないことに注意してください。メール受信者ごとに許可されるBCCアドレスは1つのみです。

たとえば、サポートチームからのメールのBCCアドレスとして{% raw %}`{{custom_attribute.${support_agent}}}`{% endraw %}を追加できます。

![Liquidを使用したBCCアドレスがあるメール設定タブのBCCアドレスセクション。]({% image_buster /assets/img/email_settings/dynamic_bcc.png %}){: style="max-width:90%;" }

{% endtab %}
{% endtabs %}

## 開封トラッキングピクセル {#open-tracking-pixel}

[![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

メール開封トラッキングピクセルは、目に見えない1 x 1&nbsp;pxの画像で、メールHTMLに自動的に挿入されます。このピクセルにより、Brazeはユーザーがメールを開封したかどうかを検出できます。ユーザーのメールクライアントがトラッキングピクセルにリクエストを送信すると、そのリクエストにはIPアドレス、ユーザーエージェント、タイムスタンプなどの情報が含まれることがあります。メール開封情報は非常に有用で、対応する開封率を把握することで効果的なマーケティング戦略を判断するのに役立ちます。

### 配置 {#placement}

Brazeのデフォルトの動作では、トラッキングピクセルはメールの下部、通常は`<body>`タグ内に追加されます。大多数のユーザーにとって、これがピクセルを配置する理想的な場所です。

ピクセルは視覚的な変化をできるだけ少なくするようにスタイル設定されていますが、意図しない視覚的な変化はメールの下部で最も目立ちにくくなります。これはSendGridやSparkPostなどのメールプロバイダーのデフォルトでもあります。

予期しない動作を減らすために、Liquidは`<html>`タグ内に配置してください。ネストされたタグや重複するドキュメントレベルのタグは、メールの解析方法やピクセルの配置場所を変更し、開封トラッキングやレイアウトに影響を与える可能性があります。詳細については、[Liquidの使用]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/)を参照してください。

### 配置の更新 {#update-the-placement}

Brazeは現在、メールサービスプロバイダー（ESP）のデフォルトの開封トラッキングピクセル位置（メールの`<body>`の最後のタグ）を上書きして、`<body>`の最初のタグに移動することをサポートしています。

![SendGrid、SparkPost、またはAmazon SESに対して移動するオプションがある「開封トラッキングピクセル」セクション。]({% image_buster /assets/img/open_pixel.png %}){: style="max-width:80%;" }

位置を変更するには：

1. Brazeで、**設定** > **メール設定**に移動します。
2. 以下のオプションから選択します：**Move for SendGrid**、**Move for SparkPost**、または**Move for Amazon SES**
3. **保存**を選択します。

保存すると、BrazeはすべてのHTMLメールの上部に開封トラッキングピクセルを配置するための特別な指示をESPに送信します。

{% alert important %}
SSLを有効にすると、トラッキングピクセルのURLがHTTPではなくHTTPSでラップされます。SSLが正しく設定されていない場合、トラッキングピクセルの有効性に影響を与える可能性があります。
{% endalert %}

{% alert important %}
クリックトラッキングは、`http://`または`https://`で始まるリンクにのみ適用されます。`mailto:`リンク（例：`mailto:support@example.com`）はトラッキング用に書き換えられません。
{% endalert %}

## List-Unsubscribeヘッダー {#list-unsubscribe}

{% alert note %}
2024年2月15日以降、新しい会社ではlist-unsubscribeヘッダー（ワンクリック配信停止付き）がデフォルトで有効になっています。
{% endalert %}

list-unsubscribeヘッダーを使用すると、受信者はメッセージ本文ではなく、メールボックスUI内の**Unsubscribe**ボタンを表示することで、マーケティングメールから簡単に配信停止できます。

テスト送信には通常、list-unsubscribeヘッダーは**含まれません**。ライブヘッダーが表示されるかどうかはメールボックスプロバイダーによって決定され、レピュテーションに基づきます。送信者のレピュテーションが高いほど、通常は表示される可能性が高くなります。

![メッセージ本文の外側にlist-unsubscribeが表示される、メッセージの横にUnsubscribeオプションがあるメールクライアントのメールボックスUI。]({% image_buster /assets/img_archive/list_unsub_img1.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

受信者が**Unsubscribe**を選択すると、メールボックスプロバイダーはメールヘッダーで定義された送信先に配信停止リクエストを送信します。

list-unsubscribeを有効にすることは、配信到達性のベストプラクティスであり、主要なメールボックスプロバイダーの一部では必須要件です。これにより、エンドユーザーは不要なメッセージから安全に自分自身を削除できるようになります。メールクライアントでスパムボタンを押す代わりにこの方法を使用することで、送信レピュテーションとメール配信到達性への悪影響を防ぐことができます。

[Gmailでサブスクリプションを管理する](https://support.google.com/mail/answer/15621070?sjid=2292320204527911296-NC)場合、Gmailはメッセージ本文から配信停止リンクを取得することもできますが、ヘッダーにlist-unsubscribeが存在する場合はそちらを優先します。

### list-unsubscribeヘッダーをオフにするとGmailの配信停止ボタンは削除されますか？ {#does-turning-off-the-list-unsubscribe-header-remove-the-gmail-unsubscribe-button}

いいえ。Brazeのlist-unsubscribeヘッダー設定をオフにすると、Brazeが送信するメッセージから`List-Unsubscribe`ヘッダーが削除されますが、GmailがメールボックスUIに**Unsubscribe**オプションを表示するかどうかは制御しません。上記のとおり、Gmailはメッセージ本文内のリンクから配信停止オプションを表示したり、他のプロバイダーロジックを使用したりする場合があります。生メッセージにヘッダーが表示されるかどうかと、Gmailが受信者に配信停止オプションを表示するかどうかは別の問題です。詳細については、[GmailのメールSender Guidelines FAQ](https://support.google.com/a/answer/14229414)を参照してください。

### メールボックスプロバイダーのサポート {#mailbox-provider-support}

以下の表は、「mailto:」ヘッダー、list-unsubscribe URL、およびワンクリック配信停止（[RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)）に対するメールボックスプロバイダーのサポートをまとめたものです。

| List-Unsubscribeヘッダー | Mailto:ヘッダー | List-Unsubscribe URL | ワンクリック配信停止（RFC 8058） |
| ----- | --- | --- | --- |
| Gmail | サポート対象* | サポート対象 | サポート対象 |
| Gmailモバイル | サポート対象外 | サポート対象外 | サポート対象外 |
| Apple Mail | サポート対象 | サポート対象外 | サポート対象外 |
| Outlook.com | サポート対象 | サポート対象外 | サポート対象外 |
| Yahoo! Mail | サポート対象* | サポート対象外 | サポート対象 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="メールボックスプロバイダーのサポート" }

_*YahooとGmailは最終的に「mailto:」ヘッダーを廃止し、ワンクリックのみをサポートする予定です。_

ヘッダーの表示は最終的にメールボックスプロバイダーによって決定されます。Gmailで受信者の生の（テキスト）メールにlist-unsubscribeヘッダーが含まれているかどうかを確認するには、以下の手順を実行します。

1. メールで**Show Original**を選択します。これにより、メールの生バージョンとそのヘッダーが新しいタブで開きます。
2. 「List-Unsubscribe」を検索します。ワンクリック配信停止の場合、多くのプロバイダーは「List-Unsubscribe-Post」ヘッダーも含めます。ワンクリックが利用可能であると想定される場合は、生メッセージに両方が表示されることを確認してください。

ヘッダーがメールの生バージョンに含まれているが表示されていない場合、メールボックスプロバイダーが配信停止オプションを表示しないと判断したことを意味し、メールボックスプロバイダーがヘッダーを表示しない理由についてはこれ以上のインサイトはありません。list-unsubscribeヘッダーの表示は最終的にレピュテーションに基づきます。ほとんどの場合、メールボックスプロバイダーでの送信者レピュテーションが高いほど、list-unsubscribeヘッダーが表示される可能性が高くなります。

### ワークスペースでのメール配信停止ヘッダー {#email-unsubscribe-header-in-workspaces}

![送信先として「購読中またはオプトインしたユーザー」を選択する画面。]({% image_buster /assets/img/email_settings/email_unsub_header_workspaces.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

メール配信停止ヘッダー機能がオンになっている場合、この設定は会社レベルではなく、ワークスペース全体に適用されます。CampaignsおよびCanvasesビルダーの**ターゲットオーディエンス**ステップで、購読中またはオプトインしたユーザー、またはオプトインしたユーザーに送信するように設定されたCampaignsおよびCanvasesに追加されます。

「ワークスペースのデフォルト」を使用する場合、Brazeはトランザクションとみなされるキャンペーン（「配信停止ユーザーを含むすべてのユーザーに送信」に設定されたもの）にはワンクリック配信停止ヘッダーを追加しません。これを上書きして、配信停止ユーザーに送信する際にワンクリック配信停止ヘッダーを追加するには、メッセージレベルのワンクリックlist-unsubscribe設定で**Unsubscribe globally from all emails**を選択できます。

### デフォルトのlist-unsubscribeヘッダー {#default-list-unsubscribe-header}

{% alert important %}
Gmailは、2024年6月1日以降、すべての送信商用・プロモーションメッセージに対してワンクリック配信停止を実装することを送信者に求めています。詳細については、[Gmailの送信者ガイドライン](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe)および[GmailのメールSender Guidelines FAQ](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages)を参照してください。Yahooは要件更新のタイムラインを2024年初頭と発表しました。詳細については、[More Secure, Less Spam: Enforcing Email Standards for a Better Experience](https://blog.postmaster.yahooinc.com/)を参照してください。
{% endalert %}

Brazeの配信停止機能を使用して配信停止を直接処理するには、**Include a one-click list-unsubscribe (mailto and HTTP) email header for emails sent to subscribed or opted-in users**を選択し、標準のBraze URLおよびmail-toとして**Braze default**を選択します。

![購読中またはオプトインしたユーザーに送信されるメールにlist-unsubscribeヘッダーを自動的に含めるオプション。]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %})

Brazeは以下のバージョンのlist-unsubscribeヘッダーをサポートしています。

| List-Unsubscribeバージョン | 説明 |
| ----- | --- |
| ワンクリック（RFC 8058） | ワンクリックで受信者がメールからオプトアウトするための簡単な方法を提供します。これはYahooとGmailが大量送信者に対して求める要件です。 |
| List-Unsubscribe URLまたはHTTPS | 受信者に配信停止できるWebページへのリンクを提供します。 |
| Mailto | 受信者からブランドに送信される配信停止リクエストメッセージの送信先としてメールアドレスを指定します。<br><br> _mailto list-unsubscribeリクエストを処理するには、そのような配信停止リクエストに、配信停止するエンドユーザーのBrazeに保存されているメールアドレスが含まれている必要があります。これは、エンドユーザーが配信停止するメールの「差出人アドレス」、エンコードされた件名、またはエンドユーザーが受信したメールのエンコードされた本文から提供される場合があります。非常に限られたケースでは、一部の受信トレイプロバイダーが[RFC 2368](https://datatracker.ietf.org/doc/html/rfc2368)プロトコルに準拠しておらず、メールアドレスが正しく渡されないことがあります。これにより、Brazeで配信停止リクエストを処理できない場合があります。_ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="デフォルトのlist-unsubscribeヘッダー" }

Brazeが上記のいずれかの方法でユーザーからlist-unsubscribeリクエストを受信すると、このユーザーのグローバルメールサブスクリプション状態が配信停止に設定されます。一致するものがない場合、Brazeはこのリクエストを処理しません。

### ワンクリック配信停止 {#one-click-unsubscribe}

list-unsubscribeヘッダーのワンクリック配信停止（[RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)）を使用すると、受信者がメールからオプトアウトするための簡単な方法を提供することに重点を置いています。

### メッセージレベルのワンクリックlist-unsubscribe {#message-level-one-click-list-unsubscribe}

メッセージレベルのワンクリックlist-unsubscribe設定は、ワークスペースに設定されたメール配信停止ヘッダー機能を上書きします。以下の用途で、Campaignまたはキャンバスステップごとにワンクリック配信停止の動作を適用します。

- 1つのワークスペース内で複数のブランド/リストをサポートするために、特定のサブスクリプショングループに対してBrazeワンクリック配信停止を追加する
- デフォルトのBraze配信停止とカスタムURLを切り替える
- カスタムのワンクリック配信停止URLを追加する
- このメッセージでワンクリック配信停止を省略する

{% alert note %}
メッセージレベルのワンクリックlist-unsubscribe設定は、ドラッグ＆ドロップエディターおよび更新されたHTMLエディターを使用する場合にのみ利用できます。以前のHTMLエディターを使用している場合は、この機能を使用するために更新されたHTMLエディターに切り替えてください。
{% endalert %}

メールエディターで、**Sending Settings** > **Sending Info**に移動します。以下のオプションから選択します。

- **Use workspace default**：**メール設定**で設定された**メール配信停止ヘッダー**設定を使用します。この設定への変更はすべてのメッセージに適用されます。
- **Unsubscribe globally from all emails**：Brazeデフォルトのワンクリック配信停止ヘッダーを使用します。配信停止ボタンをクリックしたユーザーのグローバルメールサブスクリプション状態が「配信停止」に設定されます。
- **Unsubscribe from specific subscription group**：指定されたサブスクリプショングループを使用します。Brazeは、配信停止ボタンをクリックしたユーザーを選択されたサブスクリプショングループから配信停止します。
    - サブスクリプショングループを選択する場合、**Target Audiences**で**Subscription Group**フィルターを追加して、この特定のグループに購読しているユーザーのみをターゲットにします。ワンクリック配信停止用に選択されたサブスクリプショングループは、ターゲットにしているサブスクリプショングループと一致する必要があります。サブスクリプショングループに不一致がある場合、すでに配信停止しているサブスクリプショングループから配信停止しようとしているユーザーに送信するリスクがあります。

{% alert important %}
**Unsubscribe from specific subscription group**設定は、ワンクリックlist-unsubscribeヘッダーにのみ適用されます。mailto list-unsubscribeヘッダーは、このオプションを選択しても影響を受けません。つまり、この方法で配信停止した受信者は、特定のサブスクリプショングループからの配信停止ではなく、グローバル配信停止として記録されます。この設定を選択する際にmailto list-unsubscribeヘッダーがユーザーをグローバルに配信停止しないようにするには、[サポート]({{site.baseurl}}/support_contact/)にお問い合わせください。
{% endalert %}

- **Custom**：配信停止を直接処理するためのカスタムワンクリック配信停止URLを追加します。
- **Exclude unsubscribe**

{% alert important %}
ワンクリック配信停止またはその他の配信停止メカニズムの除外は、パスワードリセット、領収書、確認メールなどのトランザクションメッセージングにのみ行うべきです。
{% endalert %}

この設定を調整すると、このメールのワンクリックlist-unsubscribeのデフォルト動作が上書きされます。

![ワークスペースのデフォルトやカスタムURLなど、メッセージレベルのワンクリックlist-unsubscribeオプションがあるメールエディターの送信設定。]({% image_buster /assets/img/email_settings/one_click_list_unsubscribe_message_level.png %}){: style="max-width:70%;"}

#### 要件 {#requirements}

独自のカスタム配信停止機能を使用してメールを送信する場合、設定するワンクリック配信停止URLがRFC 8058に準拠していることを確認するために、以下の要件を満たす必要があります。

* URLは配信停止POSTリクエストを処理できる必要があります。
* URLは`https://`で始まる必要があります。
* URLはHTTPSリダイレクトまたはボディを返してはなりません。ランディングページやその他のタイプのWebページに移動するワンクリック配信停止リンクはRFC 8058に準拠しません。
* POSTリクエストはCookieを設定してはなりません。

**Custom list-unsubscribe header**を選択して、独自に設定したワンクリック配信停止エンドポイントとオプションの「mailto:」を追加します。Brazeはカスタムlist-unsubscribeヘッダーをサポートするためにURLの入力を必要とします。これは、ワンクリック配信停止HTTPがYahooとGmailの大量送信者に対する要件であるためです。

![ワンクリック配信停止URLとオプションのmailtoのカスタムlist-unsubscribeヘッダーフィールドがあるメール設定。]({% image_buster /assets/img/email_settings/email_unsubscribe_header_custom.png %}){: style="max-width:80%;"}

## メール件名行への追加 {#append-email-subject-lines}

トグルを使用して、テストおよびシードメールの件名行に「[TEST]」および「[SEED]」を含めます。これにより、テストとして送信されたメールキャンペーンを識別するのに役立ちます。

![テストおよびシードメールの件名行にTESTおよびSEEDプレフィックスを追加するワークスペースのメール設定トグル。]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;"}

## 新規メールでのデフォルトCSSインライン化 {#inline-css-on-new-emails-by-default}

CSSインライン化は、メールおよび新規メールのCSSスタイルを自動的にインライン化する技術です。一部のメールクライアントでは、メールのレンダリングが改善される場合があります。

この設定を変更しても、既存のメールメッセージやテンプレートには影響しません。メッセージやテンプレートの作成中にいつでもこのデフォルトを上書きできます。詳細については、[CSSインライン化]({{site.baseurl}}/user_guide/channels/email/html_editor/css_inline/)を参照してください。

## メールアドレス変更時のユーザー再購読 {#resubscribe-users-when-their-email-changes}

ユーザーがメールアドレスを変更した際に、自動的に再購読させることができます。たとえば、以前に配信停止したワークスペースユーザーがメールアドレスをBrazeの配信停止リストにないアドレスに変更した場合、自動的に再購読されます。

![メールアドレスが変更された際にユーザーを自動的に再購読するワークスペース設定。]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## 購読ページおよびフッター {#subscription-pages-and-footers}

{% tabs local %}
{% tab カスタムフッター %}

商用メールの場合、[CAN-SPAM法](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003)では、すべての商用メールに配信停止オプションを含めることが義務付けられています。カスタムフッター設定を使用すると、CAN-SPAMに準拠しながら、メールのオプトアウトフッターをカスタマイズできます。準拠を維持するために、このワークスペースのCampaignsの一部として送信されるすべてのメールにカスタムフッターを追加する必要があります。

メールメッセージングのカスタムフッターを作成する際の以下の要件に注意してください。
- 配信停止URLと物理的な郵送先住所を含める必要があります。
- 100 KB未満である必要があります。

![CAN-SPAM準拠のための配信停止リンクと郵送先住所フィールドがあるカスタムメールフッターエディター。]({% image_buster /assets/img/email_settings/custom_footer.png %})

カスタムフッターのLiquidテンプレートについて詳しくは、[カスタムフッター]({{site.baseurl}}/user_guide/channels/email/subscriptions/#changing-email-subscriptions)を参照してください。

{% endtab %}
{% tab カスタム購読解除ページ %}

Brazeでは、独自のHTMLを使用して**カスタム購読解除ページ**を設定できます。このページは、ユーザーがメールの下部から配信停止を選択した後に表示されます。このページは750 KB未満である必要があることに注意してください。

![ユーザーがメールから配信停止した後に表示されるページのカスタム購読解除ページHTMLエディターとプレビュー。]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

メールリスト管理のベストプラクティスについて詳しくは、[メールサブスクリプションの管理]({{site.baseurl}}/user_guide/channels/email/faq/#unsubscribed-email-addresses)を参照してください。

{% endtab %}
{% tab カスタムオプトインページ %}

独自のHTMLを使用してカスタムオプトインページを作成できます。これをメールに含めることは、ユーザーライフサイクル全体を通じてブランディングとメッセージの一貫性を維持したい場合に特に有益です。このページは750 KB未満である必要があることに注意してください。

![ブランド化されたメール購読確認のためのカスタムオプトインページHTMLエディターとプレビュー。]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

メールリスト管理のベストプラクティスについて詳しくは、[メールサブスクリプションの管理]({{site.baseurl}}/user_guide/channels/email/faq/#unsubscribed-email-addresses)を参照してください。

{% endtab %}
{% endtabs %}

{% alert tip %}
購読ページまたはフッターの**プレビュー**セクションで、**プレビューリンクをコピー**を選択すると、ランダムなユーザーに対してメールフッター、購読解除ページ、またはオプトインページがどのように表示されるかを示す共有可能なプレビューリンクを生成してコピーできます。リンクは7日間有効で、その後再生成する必要があります。
{% endalert %}

## よくある質問 {#frequently-asked-questions}

### ワンクリック配信停止

{% details ワンクリック配信停止URL（list-unsubscribeヘッダー経由）をユーザー設定センターにリンクできますか？ %}
いいえ、それはRFC 8058に準拠しないため、YahooとGmailのワンクリック配信停止要件に準拠しません。
{% enddetails %}

{% details ユーザー設定センターを作成する際に「メール本文に配信停止リンクが含まれていません」というエラーメッセージが表示されるのはなぜですか？ %}
ユーザー設定センターは配信停止リンクとはみなされません。CAN-SPAMに準拠するために、メール受信者はすべての商用メールから配信停止するオプションを持つ必要があります。
{% enddetails %}

{% details ワンクリック配信停止設定を有効にした後、過去のメールキャンペーンやCanvasesを編集する必要がありますか？ %}
メッセージレベルのワンクリックlist-unsubscribe設定のユースケースがない場合、**メール設定**で設定がオンになっている限り、必要なアクションはありません。Brazeはすべての送信マーケティングおよびプロモーションメッセージにワンクリック配信停止ヘッダーを自動的に追加します。ただし、メッセージレベルでワンクリック配信停止の動作を設定する必要がある場合は、以前のメールキャンペーンおよびキャンバスステップを適宜更新する必要があります。
{% enddetails %}

{% details 元のメッセージまたは生データでlist-unsubscribeおよびワンクリック配信停止ヘッダーを確認できますが、GmailやYahooで配信停止ボタンが表示されないのはなぜですか？ %}
GmailとYahooは最終的にlist-unsubscribeまたはワンクリック配信停止ヘッダーを表示するかどうかを決定します。新しい送信者や送信者レピュテーションが低い送信者の場合、配信停止ボタンが表示されないことがあります。
{% enddetails %}

{% details カスタムワンクリック配信停止ヘッダーはLiquidをサポートしていますか？ %}
はい、Liquidと条件ロジックがサポートされており、ヘッダーのダイナミックなワンクリック配信停止URLを使用できます。
{% enddetails %}

{% alert tip %}
条件ロジックを追加する場合、URLに空白を追加する出力値を避けてください。Brazeはこれらの空白を削除しません。
{% endalert %}

### メッセージレベルのワンクリックlist-unsubscribe

{% details ワンクリック用のメールヘッダーを手動で追加し、メール配信停止ヘッダーがオンになっている場合、期待される動作は何ですか？ %}
ワンクリックlist-unsubscribe用に追加されたメールヘッダーは、このCampaignの今後のすべての送信に適用されます。
{% enddetails %}

{% details 起動するためにメッセージバリアント間でサブスクリプショングループが一致する必要があるのはなぜですか？ %}
ABテストを含むCampaignの場合、Brazeはユーザーにバリアントの1つをランダムに送信します。同じCampaignに2つの異なるサブスクリプショングループが設定されている場合（バリアントAがサブスクリプショングループAに設定され、バリアントBがサブスクリプショングループBに設定されている場合）、サブスクリプショングループBのみに購読しているユーザーがバリアントBを受信することを保証できません。ユーザーがすでにオプトアウトしたサブスクリプショングループから配信停止するシナリオが発生する可能性があります。
{% enddetails %}

{% details メール設定でメール配信停止ヘッダー設定がオフになっていますが、キャンペーンの送信情報ではワンクリックlist-unsubscribe設定が「ワークスペースのデフォルトを使用」に設定されています。これはバグですか？ %}
いいえ。ワークスペース設定がオフで、メッセージ設定が**Use workspace default**に設定されている場合、Brazeは**メール設定**で構成された内容に従います。つまり、Campaignにワンクリック配信停止ヘッダーは追加されません。
{% enddetails %}

{% details サブスクリプショングループがアーカイブされた場合はどうなりますか？送信済みメールのワンクリック配信停止が壊れますか？ %}
ワンクリック用の**Sending Info**で参照されているサブスクリプショングループがアーカイブされた場合でも、Brazeはワンクリックからの配信停止を引き続き処理します。サブスクリプショングループはダッシュボード上（Segmentフィルター、ユーザープロファイルなどの領域）には表示されなくなります。
{% enddetails %}

{% details ワンクリック配信停止設定はメールテンプレートで利用できますか？ %}
いいえ、現在メールテンプレートにこの機能を追加する予定はありません。これらのテンプレートは送信ドメインに割り当てられていないためです。メールテンプレートでのこの機能に興味がある場合は、[製品フィードバック]({{site.baseurl}}/user_guide/administer/personal/product_portal/)を送信してください。
{% enddetails %}

{% details この機能は、カスタムオプションに追加されたワンクリック配信停止URLが有効かどうかをチェックしますか？ %}
いいえ、Brazeダッシュボードではリンクのチェックや検証は行いません。起動前にURLを適切にテストしてください。
{% enddetails %}