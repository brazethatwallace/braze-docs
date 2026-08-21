---
nav_title: メール設定
article_title: メール設定
page_type: reference
page_order: 2
description: "このリファレンス記事では、送信設定、開封トラッキングピクセル、購読ページおよびフッターなど、Brazeダッシュボードのメール設定について説明します。"
tool: Dashboard
channel: email
alias: /email_preferences/
toc_headers: h2

---

# メール設定 {#email-preferences}

> メール設定では、カスタムフッター、カスタムオプトインおよびオプトアウトページなど、送信メールに関する特定の設定を行うことができます。これらのオプションを送信メールに含めることで、ユーザーにとってスムーズで一貫性のある体験を提供できます。

**メール設定**は、ダッシュボードの**設定** > **ワークスペース設定**にあります。

## 送信設定 {#sending-configuration}

**送信設定**セクションのメール設定は、メールキャンペーンに含まれる詳細を決定します。特に、これらの設定は主に、ユーザーがBrazeからメールを受信したときに表示される内容に関連しています。

### 送信メール設定 {#outbound-email-settings}

メール設定を構成する際、送信メール設定では、Brazeがユーザーにメールを送信するときに使用される名前とメールアドレスを指定します。

ワークスペースに新しいドメインまたはIPプール（送信プロバイダー）を追加する必要がある場合、または利用可能なリストから削除する必要がある場合は、カスタマーサクセスマネージャーにお問い合わせください。

{% tabs local %}
{% tab 表示名アドレス %}

このセクションでは、Brazeがユーザーにメールを送信するときに使用できる名前とメールアドレスを追加できます。表示名とメールアドレスは、メールキャンペーンを作成する際の**送信情報**オプションで利用できます。送信メール設定に加えた更新は、既存の送信に遡って影響しないことに注意してください。

![異なる表示名とドメインのフィールドがある「送信メール設定」セクション。]({% image_buster /assets/img/email_settings/display_name_address.png %})

{% alert note %}
Apple Mailクライアントは、カスタム表示名で`@`記号が使用されている場合、それを認識しません。メールボックスプロバイダーによって表示名アドレスの表示方法が異なるため、メールクライアントによって表示名の表示が異なる場合があります。
{% endalert %}

#### Liquidでパーソナライズする {#personalize-with-liquid}

**差出人表示名**、**ローカルパート**、**ドメイン**フィールドで[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)を使用して、カスタム属性に基づいて送信者名とメールアドレスを動的にテンプレート化することもできます。**ドメイン**フィールドでLiquidを使用するには、メールキャンペーンの**送信情報**オプションに移動し、**差出人表示名+アドレスをカスタマイズ**チェックボックスを選択する必要があります。

![差出人表示名、アドレス、ドメインをカスタマイズするためのフィールドがある送信設定。]({% image_buster /assets/img/email_settings/email_campaign_domain.png %})

たとえば、条件付きロジックを使用して、異なるブランドやリージョンから送信できます。

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

このセクションでメールアドレスを追加すると、メールキャンペーンの返信先アドレスとして選択できるようになります。**デフォルトに設定**を選択して、メールアドレスをデフォルトに設定することもできます。これらのメールアドレスは、メールキャンペーンを作成する際の**送信情報**オプションで利用できます。

![複数の返信先アドレスを入力するフィールドがある「返信先アドレス」セクション。]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

{% alert note %}
Brazeの送信ドメインは受信メールを受け付けません。受信者がBrazeで設定された送信ドメインから送信されたメールに返信すると、その返信は`550 5.7.1 relaying denied`エラーでバウンスされます。返信先アドレスは差出人アドレスと同じドメインを共有する必要はありません。返信を受信する必要がある場合（たとえば、カレンダー招待の確認を収集する場合）は、送信用に設定されておらず、メールを受信するための受信トレイが設定されているサブドメインを使用してください。
{% endalert %}

#### Liquidでパーソナライズする

**返信先アドレス**フィールドで[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)を使用して、カスタム属性に基づいて返信先アドレスを動的にテンプレート化することもできます。たとえば、条件付きロジックを使用して、異なるリージョンや部門に返信を送信できます。

{% raw %}
```liquid
{% if {{custom_attribute.${region}}} == 'US' %}
{% assign address = "us-support@example.com" %}
{% elsif {{custom_attribute.${region}}} == 'EU' %}
{% assign address = "eu-support@example.com" %}
{% else %}
{% assign address = "global-support@example.com" %}{% endif %}{{address}}
```
{% endraw %}

{% alert tip %}
コンテンツブロックを使用して**返信先アドレス**を入力する場合は、最終的にレンダリングされる値が有効なメールアドレスであり、`@`が含まれていることを確認してください。Brazeは設定を保存する際にこれを検証できません。最終的な値は送信時まで確定しないためです。

- コンテンツブロックにローカルパート（`@`の前のテキスト）とドメインが別々に保存されている場合は、フィールドを1つのアドレスとして構築してください（たとえば、{% raw %}`{{content_blocks.${reply_to_local}}}@{{content_blocks.${reply_to_domain}}}`{% endraw %}）。
{% endalert %}

{% endtab %}
{% tab BCCアドレス %}

このセクションでは、Brazeから送信される送信メールメッセージに追加できるBCCアドレスを管理できます。メールメッセージにBCCアドレスを追加すると、ユーザーが受信するメッセージの同一コピーがBCC受信トレイに送信されます。これは、コンプライアンス要件やカスタマーサポートの問題のために、ユーザーに送信したメッセージのコピーを保持するための便利なツールです。BCCメールはメールレポートと分析には含まれません。

BCCアドレスは、Amazon SES、SendGrid、SparkPostで利用できます。BCCアドレスの代替として、アーカイブまたはコンプライアンスの目的でユーザーに送信されたメッセージのコピーを保存するために、[メッセージアーカイブ]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/message_archiving)の使用をお勧めします。

{% multi_lang_include alerts/important_alerts.md alert='BCC address billable emails' %}

アドレスを追加すると、キャンペーンまたはキャンバスステップでメールを作成する際に選択できるようになります。アドレスの横にある**デフォルトに設定**を選択すると、新しいメールキャンペーンまたはキャンバスコンポーネントを起動する際にデフォルトで選択されるように設定されます。メッセージレベルでこれを上書きするには、メッセージを設定する際に**BCCなし**を選択します。

Brazeから送信されるすべてのメールメッセージにBCCアドレスを含める必要がある場合は、**すべてのメールキャンペーンにBCCアドレスを必須にする**トグルを選択できます。これにより、デフォルトアドレスの選択が必要になり、新しいメールキャンペーンまたはキャンバスステップで自動的に選択されます。デフォルトアドレスは、REST APIを通じてトリガーされるすべてのメッセージにも自動的に追加されます。アドレスを含めるために既存のAPIリクエストを変更する必要はありません。

#### ダイナミックBCC {#dynamic-bcc}

ダイナミックBCCを使用すると、BCCアドレスでLiquidを使用できます。この機能は**メール設定**でのみ利用可能で、キャンペーン自体では設定できないことに注意してください。メール受信者ごとに許可されるBCCアドレスは1つのみです。

たとえば、サポートチームからのメールのBCCアドレスとして{% raw %}`{{custom_attribute.${support_agent}}}`{% endraw %}を追加できます。

![Liquidを使用したBCCアドレスが表示されているメール設定タブのBCCアドレスセクション。]({% image_buster /assets/img/email_settings/dynamic_bcc.png %}){: style="max-width:90%;" }

{% endtab %}
{% endtabs %}

## 開封トラッキングピクセル {#open-tracking-pixel}

[![Braze Learning コース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

メール開封トラッキングピクセルは、目に見えない1 x 1&nbsp;pxの画像で、メールのHTMLに自動的に挿入されます。このピクセルにより、Brazeはユーザーがメールを開封したかどうかを検出できます。ユーザーのメールクライアントがトラッキングピクセルにリクエストを送信すると、そのリクエストにはIPアドレス、ユーザーエージェント、タイムスタンプなどの情報が含まれる場合があります。メールの開封情報は非常に有用で、対応する開封率を把握することで効果的なマーケティング戦略を判断するのに役立ちます。

### 配置 {#placement}

Brazeのデフォルトの動作では、トラッキングピクセルはメールの下部、通常は`<body>`タグ内に追加されます。大多数のユーザーにとって、これがピクセルを配置する理想的な場所です。

ピクセルは視覚的な変化をできるだけ少なくするようにスタイル設定されていますが、意図しない視覚的な変化はメールの下部で最も目立ちにくくなります。これはSendGridやSparkPostなどのメールプロバイダーでもデフォルトの設定です。

予期しない動作を減らすために、Liquidは`<html>`タグ内に配置してください。ネストされたタグや重複するドキュメントレベルのタグは、メールの解析方法やピクセルの配置場所を変更し、開封トラッキングやレイアウトに影響を与える可能性があります。詳細については、[Liquidの使用]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid)を参照してください。

### 配置の更新 {#update-the-placement}

Brazeは現在、メールサービスプロバイダー (ESP) のデフォルトの開封トラッキングピクセルの位置（メールの`<body>`内の最後のタグ）をオーバーライドして、`<body>`内の最初のタグに移動することをサポートしています。

![SendGrid、SparkPost、またはAmazon SES用の移動オプションが表示された「開封トラッキングピクセル」セクション]({% image_buster /assets/img/open_pixel.png %}){: style="max-width:80%;" }

位置を変更するには：

1. Brazeで、**設定** > **ワークスペース設定** > **メール設定**に移動します。
2. 以下のオプションから選択します：**Move for SendGrid**、**Move for SparkPost**、または**Move for Amazon SES**
3. **保存**を選択します。

保存すると、Brazeはすべての HTMLメールの上部に開封トラッキングピクセルを配置するための特別な指示をメールサービスプロバイダー (ESP) に送信します。

{% alert important %}
SSLを有効にすると、トラッキングピクセルのURLがHTTPではなくHTTPSでラップされます。SSLが正しく設定されていない場合、トラッキングピクセルの有効性に影響を与える可能性があります。
{% endalert %}

{% alert important %}
クリックトラッキングは、`http://`または`https://`で始まるリンクにのみ適用されます。`mailto:`リンク（例：`mailto:support@example.com`）はトラッキング用に書き換えられません。
{% endalert %}

## List-Unsubscribeヘッダー {#list-unsubscribe}

{% alert note %}
2026年6月15日以降、ワンクリックlist-unsubscribeヘッダーが特定の購読グループにスコープされるように設定されている場合、Brazeはメールにmailtoヘッダーを含めなくなります。list-unsubscribeヘッダーを通じて購読解除したユーザーは、グローバルではなく、その特定の購読グループからのみ購読解除されます。
{% endalert %}

list-unsubscribeヘッダーを使用すると、受信者はメッセージ本文ではなく、メールボックスUI内の**購読解除**ボタンを表示することで、マーケティングメールから簡単に購読解除できます。

テスト送信には通常、list-unsubscribeヘッダーは含まれません。ライブヘッダーが表示されるかどうかはメールボックスプロバイダーによって決定され、レピュテーションに基づきます。送信者のレピュテーションが高いほど、通常は表示される可能性が高くなります。

![メッセージ本文の外側にlist-unsubscribeが表示される、メッセージの横に購読解除オプションがあるメールクライアントのメールボックスUI。]({% image_buster /assets/img_archive/list_unsub_img1.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

受信者が**購読解除**を選択すると、メールボックスプロバイダーはメールヘッダーで定義された送信先に購読解除リクエストを送信します。

list-unsubscribeを有効にすることは、配信到達性のベストプラクティスであり、主要なメールボックスプロバイダーの一部では必須要件です。これにより、エンドユーザーは不要なメッセージから安全に自分自身を削除できるようになります。メールクライアントでスパムボタンを押す代わりにこの方法を使用することで、送信レピュテーションとメール配信到達性への悪影響を防ぐことができます。

[Gmailでサブスクリプションを管理する](https://support.google.com/mail/answer/15621070?sjid=2292320204527911296-NC)場合、Gmailはメッセージ本文から購読解除リンクを取得することもできますが、ヘッダーにlist-unsubscribeが存在する場合はそちらを優先します。

### list-unsubscribeヘッダーをオフにするとGmailの購読解除ボタンは削除されますか？ {#does-turning-off-the-list-unsubscribe-header-remove-the-gmail-unsubscribe-button}

いいえ。Brazeのlist-unsubscribeヘッダー設定をオフにすると、Brazeが送信するメッセージから`List-Unsubscribe`ヘッダーが削除されますが、GmailがメールボックスUIに**購読解除**オプションを表示するかどうかは制御しません。前のセクションで述べたとおり、Gmailはメッセージ本文内のリンクから購読解除オプションを表示したり、他のプロバイダーロジックを使用したりする場合があります。生メッセージにヘッダーが表示されるかどうかと、Gmailが受信者に購読解除オプションを表示するかどうかは別の問題です。詳細については、[GmailのEmail Sender Guidelines FAQ](https://support.google.com/a/answer/14229414)を参照してください。

### メールボックスプロバイダーのサポート {#mailbox-provider-support}

以下の表は、「mailto:」ヘッダー、list-unsubscribe URL、およびワンクリック購読解除（[RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)）に対するメールボックスプロバイダーのサポートをまとめたものです。

| List-Unsubscribeヘッダー | Mailto:ヘッダー | List-Unsubscribe URL | ワンクリック購読解除（RFC 8058） |
| ----- | --- | --- | --- |
| Gmail | サポート対象* | サポート対象 | サポート対象 |
| Gmailモバイル | サポート対象外 | サポート対象外 | サポート対象外 |
| Apple Mail | サポート対象 | サポート対象外 | サポート対象外 |
| Outlook.com | サポート対象 | サポート対象外 | サポート対象外 |
| Yahoo! Mail | サポート対象* | サポート対象外 | サポート対象 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="メールボックスプロバイダーのサポート" }

_*YahooとGmailは最終的に「mailto:」ヘッダーを廃止し、ワンクリックのみをサポートする予定です。_

ヘッダーの表示は最終的にメールボックスプロバイダーによって決定されます。Gmailで受信者の生の（テキスト）メールにlist-unsubscribeヘッダーが含まれているかどうかを確認するには、以下の手順を実行します。

1. メールで**メッセージのソースを表示**を選択します。これにより、メールの生バージョンとそのヘッダーが新しいタブで開きます。
2. 「List-Unsubscribe」を検索します。ワンクリック購読解除の場合、多くのプロバイダーは「List-Unsubscribe-Post」ヘッダーも含めます。ワンクリックが利用可能であると想定される場合は、生メッセージに両方が表示されることを確認してください。

ヘッダーがメールの生バージョンに含まれているが表示されていない場合、メールボックスプロバイダーが購読解除オプションを表示しないと判断したことを意味し、メールボックスプロバイダーがヘッダーを表示しない理由についてはこれ以上のインサイトはありません。list-unsubscribeヘッダーの表示は最終的にレピュテーションに基づきます。ほとんどの場合、メールボックスプロバイダーでの送信者レピュテーションが高いほど、list-unsubscribeヘッダーが表示される可能性が高くなります。

### ワークスペースでのメール購読解除ヘッダー {#email-unsubscribe-header-in-workspaces}

![送信先として「購読中またはオプトインしたユーザー」を選択する画面。]({% image_buster /assets/img/email_settings/email_unsub_header_workspaces.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

メール購読解除ヘッダー機能がオンになっている場合、この設定は会社レベルではなく、ワークスペース全体に適用されます。キャンペーンおよびキャンバスビルダーの**ターゲットオーディエンス**ステップで、購読中またはオプトインしたユーザー、またはオプトインしたユーザーに送信するように設定されたキャンペーンおよびキャンバスに追加されます。

「ワークスペースのデフォルト」を使用する場合、Brazeはトランザクションとみなされるキャンペーン（「購読解除ユーザーを含むすべてのユーザーに送信」に設定されたもの）にはワンクリック購読解除ヘッダーを追加しません。これを上書きして、購読解除ユーザーに送信する際にワンクリック購読解除ヘッダーを追加するには、メッセージレベルのワンクリックlist-unsubscribe設定で**すべてのメールからグローバルに購読解除**を選択できます。

### デフォルトのlist-unsubscribeヘッダー {#default-list-unsubscribe-header}

{% alert important %}
Gmailは、2024年6月1日以降、すべての送信商用・プロモーションメッセージに対してワンクリック購読解除を実装することを送信者に求めています。詳細については、[Gmailの送信者ガイドライン](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe)および[GmailのEmail Sender Guidelines FAQ](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages)を参照してください。Yahooは要件更新のタイムラインを2024年初頭と発表しました。詳細については、[More Secure, Less Spam: Enforcing Email Standards for a Better Experience](https://blog.postmaster.yahooinc.com/)を参照してください。
{% endalert %}

Brazeの購読解除機能を使用して購読解除を直接処理するには、**購読中またはオプトインしたユーザーに送信されるメールにワンクリックlist-unsubscribe（mailtoおよびHTTP）メールヘッダーを含める**を選択し、標準のBraze URLおよびmail-toとして**Brazeデフォルト**を選択します。

![購読中またはオプトインしたユーザーに送信されるメールにlist-unsubscribeヘッダーを自動的に含めるオプション。]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %})

Brazeは以下のバージョンのlist-unsubscribeヘッダーをサポートしています。

| List-Unsubscribeバージョン | 説明 |
| ----- | --- |
| ワンクリック（RFC 8058） | ワンクリックで受信者がメールからオプトアウトするための簡単な方法を提供します。これはYahooとGmailが大量送信者に対して求める要件です。 |
| List-Unsubscribe URLまたはHTTPS | 受信者に購読解除できるWebページへのリンクを提供します。 |
| Mailto | 受信者からブランドに送信される購読解除リクエストメッセージの送信先としてメールアドレスを指定します。<br><br> _mailto list-unsubscribeリクエストを処理するには、そのような購読解除リクエストに、購読解除するエンドユーザーのBrazeに保存されているメールアドレスが含まれている必要があります。これは、エンドユーザーが購読解除するメールの「差出人アドレス」、エンコードされた件名、またはエンドユーザーが受信したメールのエンコードされた本文から提供される場合があります。非常に限られたケースでは、一部の受信トレイプロバイダーが[RFC 2368](https://datatracker.ietf.org/doc/html/rfc2368)プロトコルに準拠しておらず、メールアドレスが正しく渡されないことがあります。これにより、Brazeで購読解除リクエストを処理できない場合があります。_ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="デフォルトのlist-unsubscribeヘッダー" }

Brazeが[デフォルトのlist-unsubscribeヘッダー](#default-list-unsubscribe-header)のいずれかの方法でユーザーからlist-unsubscribeリクエストを受信すると、このユーザーのグローバルメール購読状態が購読解除に設定されます。一致するものがない場合、Brazeはこのリクエストを処理しません。

### ワンクリック購読解除 {#one-click-unsubscribe}

list-unsubscribeヘッダーのワンクリック購読解除（[RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)）を使用すると、受信者がメールからオプトアウトするための簡単な方法を提供することに重点を置いています。

### メッセージレベルのワンクリックlist-unsubscribe {#message-level-one-click-list-unsubscribe}

メッセージレベルのワンクリックlist-unsubscribe設定は、ワークスペースに設定されたメール購読解除ヘッダー機能を上書きします。以下の用途で、キャンペーンまたはキャンバスステップごとにワンクリック購読解除の動作を適用します。

- 1つのワークスペース内で複数のブランド/リストをサポートするために、特定の購読グループに対してBrazeワンクリック購読解除を追加する
- デフォルトのBraze購読解除とカスタムURLを切り替える
- カスタムのワンクリック購読解除URLを追加する
- このメッセージでワンクリック購読解除を省略する

{% alert note %}
メッセージレベルのワンクリックlist-unsubscribe設定は、ドラッグ＆ドロップエディターおよび更新されたHTMLエディターを使用する場合にのみ利用できます。以前のHTMLエディターを使用している場合は、この機能を使用するために更新されたHTMLエディターに切り替えてください。
{% endalert %}

メールエディターで、**送信設定** > **送信情報**に移動します。以下のオプションから選択します。

- **ワークスペースのデフォルトを使用**：**メール設定**で設定された**メール購読解除ヘッダー**設定を使用します。この設定への変更はすべてのメッセージに適用されます。
- **すべてのメールからグローバルに購読解除**：Brazeデフォルトのワンクリック購読解除ヘッダーを使用します。購読解除ボタンをクリックしたユーザーのグローバルメール購読状態が「購読解除」に設定されます。
- **特定の購読グループから購読解除**：指定された購読グループを使用します。Brazeは、購読解除ボタンをクリックしたユーザーを選択された購読グループから購読解除します。
    - 購読グループを選択する場合、**ターゲットオーディエンス**で**購読グループ**フィルターを追加して、この特定のグループに購読しているユーザーのみをターゲットにします。ワンクリック購読解除用に選択された購読グループは、ターゲットにしている購読グループと一致する必要があります。購読グループに不一致がある場合、すでに購読解除している購読グループから購読解除しようとしているユーザーに送信するリスクがあります。

{% alert important %}
**特定の購読グループから購読解除**設定は、ワンクリックlist-unsubscribeヘッダーにのみ適用されます。mailto list-unsubscribeヘッダーは、このオプションを選択しても影響を受けません。つまり、この方法で購読解除した受信者は、特定の購読グループからの購読解除ではなく、グローバル購読解除として記録されます。この設定を選択する際にmailto list-unsubscribeヘッダーがユーザーをグローバルに購読解除しないようにするには、[サポート]({{site.baseurl}}/support_contact)にお問い合わせください。
{% endalert %}

- **カスタム**：購読解除を直接処理するためのカスタムワンクリック購読解除URLを追加します。
- **購読解除を除外**

{% alert important %}
ワンクリック購読解除またはその他の購読解除メカニズムの除外は、パスワードリセット、領収書、確認メールなどのトランザクションメッセージングにのみ行うべきです。
{% endalert %}

この設定を調整すると、このメールのワンクリックlist-unsubscribeのデフォルト動作が上書きされます。

![ワークスペースのデフォルトやカスタムURLなど、メッセージレベルのワンクリックlist-unsubscribeオプションがあるメールエディターの送信設定。]({% image_buster /assets/img/email_settings/one_click_list_unsubscribe_message_level.png %}){: style="max-width:70%;"}

#### 要件 {#requirements}

独自のカスタム購読解除機能を使用してメールを送信する場合、設定するワンクリック購読解除URLがRFC 8058に準拠していることを確認するために、以下の要件を満たす必要があります。

* URLは購読解除POSTリクエストを処理できる必要があります。
* URLは`https://`で始まる必要があります。
* URLはHTTPSリダイレクトまたはボディを返してはなりません。ランディングページやその他のタイプのWebページに移動するワンクリック購読解除リンクはRFC 8058に準拠しません。
* POSTリクエストはCookieを設定してはなりません。

**カスタムlist-unsubscribeヘッダー**を選択して、独自に設定したワンクリック購読解除エンドポイントとオプションの「mailto:」を追加します。Brazeはカスタムlist-unsubscribeヘッダーをサポートするためにURLの入力を必要とします。これは、ワンクリック購読解除HTTPがYahooとGmailの大量送信者に対する要件であるためです。

![ワンクリック購読解除URLとオプションのmailtoのカスタムlist-unsubscribeヘッダーフィールドがあるメール設定。]({% image_buster /assets/img/email_settings/email_unsubscribe_header_custom.png %}){: style="max-width:80%;"}

## メール件名への追記 {#append-email-subject-lines}

トグルを使用して、テストメールおよびシードメールの件名に「[TEST]」と「[SEED]」を含めます。これにより、テストとして送信されたメールキャンペーンを識別しやすくなります。

![テストメールおよびシードメールの件名にTESTおよびSEEDプレフィックスを追加するワークスペースのメール設定トグル。]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;"}

## 新規メールのデフォルトでのインラインCSS {#inline-css-on-new-emails-by-default}

CSSインライン化は、メールおよび新規メールのCSSスタイルを自動的にインライン化する手法です。一部のメールクライアントでは、メールの表示が改善される場合があります。

この設定を変更しても、既存のメールメッセージやテンプレートには影響しません。メッセージやテンプレートの作成中にいつでもこのデフォルトを上書きできます。詳細については、[CSSインライン化]({{site.baseurl}}/user_guide/channels/email/html_editor/css_inline)を参照してください。

## ユーザーのメールアドレス変更時に再購読する {#resubscribe-users-when-their-email-changes}

ユーザーがメールアドレスを変更した際に、自動的に再購読させることができます。たとえば、以前購読解除したワークスペースユーザーがメールアドレスをBrazeの購読解除リストに含まれていないアドレスに変更した場合、そのユーザーは自動的に再購読されます。

![ユーザーのメールアドレス変更時に自動的に再購読するワークスペース設定。]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## 購読ページとフッター {#subscription-pages-and-footers}

{% tabs local %}
{% tab カスタムフッター %}

商用メールの場合、[CAN-SPAM法](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003)により、すべての商用メールに購読解除オプションを含めることが義務付けられています。カスタムフッター設定を使用すると、メールのオプトアウトフッターをカスタマイズしながら、CAN-SPAM法に準拠し続けることができます。準拠を維持するには、このワークスペースのキャンペーンの一部として送信されるすべてのメールにカスタムフッターを追加する必要があります。

メールメッセージングのカスタムフッターを作成する際は、以下の要件に注意してください。
- 購読解除URLと物理的な郵送先住所を含める必要があります。
- 100 KB未満にする必要があります。

![CAN-SPAM準拠のための購読解除リンクと郵送先住所フィールドを含むカスタムメールフッターエディター。]({% image_buster /assets/img/email_settings/custom_footer.png %})

カスタムフッターのLiquidテンプレートについては、[カスタムフッター]({{site.baseurl}}/user_guide/channels/email/subscriptions#changing-email-subscriptions)を参照してください。

{% endtab %}
{% tab カスタム購読解除ページ %}

Brazeでは、独自のHTMLを使用して**カスタム購読解除ページ**を設定できます。このページは、ユーザーがメールの下部から購読解除を選択した後に表示されます。このページは750 KB未満にする必要があります。

![ユーザーがメールの購読を解除した後に表示されるページのカスタム購読解除ページHTMLエディターとプレビュー。]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

{% multi_lang_include email/external_font_domains.md page_type='unsubscribe' %}

{% endtab %}
{% tab カスタムオプトインページ %}

独自のHTMLを使用してカスタムオプトインページを作成できます。これをメールに含めることは、ユーザーライフサイクル全体を通じてブランディングとメッセージの一貫性を維持したい場合に特に有益です。このページは750 KB未満にする必要があります。

![ブランド化されたメール購読確認用のカスタムオプトインページHTMLエディターとプレビュー。]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

{% multi_lang_include email/external_font_domains.md page_type='opt-in' %}

{% endtab %}
{% endtabs %}

{% alert tip %}
購読ページまたはフッターの**プレビュー**セクションで、**プレビューリンクをコピー**を選択すると、ランダムなユーザーに対してメールフッター、購読解除ページ、またはオプトインページがどのように表示されるかを示す共有可能なプレビューリンクを生成してコピーできます。詳細については、[共有可能なプレビュー]({{site.baseurl}}/user_guide/messaging/governance/shareable_preview)を参照してください。
{% endalert %}

## よくある質問 {#frequently-asked-questions}

### ワンクリック購読解除

{% details ワンクリック購読解除URL（list-unsubscribeヘッダー経由）をユーザー設定センターにリンクできますか？ %}
いいえ、それはRFC 8058に準拠しないため、YahooおよびGmailのワンクリック購読解除要件に準拠できません。
{% enddetails %}

{% details ユーザー設定センターを作成する際に「メール本文に購読解除リンクが含まれていません」というエラーメッセージが表示されるのはなぜですか？ %}
ユーザー設定センターは購読解除リンクとはみなされません。CAN-SPAMに準拠するためには、メール受信者がすべての商用メールから購読解除できるオプションが必要です。
{% enddetails %}

{% details ワンクリック購読解除設定を有効にした後、過去のメールキャンペーンやキャンバスを編集する必要がありますか？ %}
メッセージレベルのワンクリックlist-unsubscribe設定のユースケースがない場合、**メール設定**で設定がオンになっていれば、特に必要なアクションはありません。Brazeは、すべての送信マーケティングおよびプロモーションメッセージにワンクリック購読解除ヘッダーを自動的に追加します。ただし、メッセージごとにワンクリック購読解除の動作を設定する必要がある場合は、以前のメールキャンペーンやキャンバスステップを適宜更新する必要があります。
{% enddetails %}

{% details 元のメッセージまたは生データでlist-unsubscribeおよびワンクリック購読解除ヘッダーを確認できますが、GmailやYahooで購読解除ボタンが表示されないのはなぜですか？ %}
GmailとYahooは、list-unsubscribeまたはワンクリック購読解除ヘッダーを表示するかどうかを最終的に決定します。新しい送信者や送信者レピュテーションが低い送信者の場合、購読解除ボタンが表示されないことがあります。
{% enddetails %}

{% details カスタムワンクリック購読解除ヘッダーはLiquidをサポートしていますか？ %}
はい、Liquidと条件付きロジックがサポートされており、ヘッダーにダイナミックなワンクリック購読解除URLを設定できます。
{% enddetails %}

{% alert tip %}
条件付きロジックを追加する場合、URLに空白を追加する出力値を避けてください。Brazeはこれらの空白を削除しません。
{% endalert %}

### メッセージレベルのワンクリックlist-unsubscribe

{% details ワンクリック用のメールヘッダーを手動で追加し、メール購読解除ヘッダーがオンになっている場合、どのような動作が期待されますか？ %}
ワンクリックlist-unsubscribe用に追加されたメールヘッダーは、このキャンペーンの今後のすべての送信に適用されます。
{% enddetails %}

{% details キャンペーンを開始するために、メッセージバリアント間で購読グループが一致する必要があるのはなぜですか？ %}
ABテストを含むキャンペーンでは、Brazeはユーザーにバリアントの1つをランダムに送信します。同じキャンペーンに2つの異なる購読グループが設定されている場合（バリアントAが購読グループAに設定され、バリアントBが購読グループBに設定されている場合）、購読グループBのみに購読しているユーザーがバリアントBを受信することを保証できません。ユーザーがすでにオプトアウトした購読グループから購読解除するシナリオが発生する可能性があります。
{% enddetails %}

{% details メール設定でメール購読解除ヘッダー設定がオフになっていますが、キャンペーンの送信情報ではワンクリックlist-unsubscribe設定が「ワークスペースのデフォルトを使用」に設定されています。これはバグですか？ %}
いいえ。ワークスペース設定がオフで、メッセージ設定が**ワークスペースのデフォルトを使用**に設定されている場合、Brazeは**メール設定**で構成された内容に従います。つまり、キャンペーンにワンクリック購読解除ヘッダーは追加されません。
{% enddetails %}

{% details 購読グループがアーカイブされた場合はどうなりますか？送信済みメールのワンクリック購読解除が機能しなくなりますか？ %}
ワンクリック用の**送信情報**で参照されている購読グループがアーカイブされた場合でも、Brazeはワンクリックからの購読解除を引き続き処理します。購読グループはダッシュボード上（セグメントフィルター、ユーザープロファイル、および類似のエリア）には表示されなくなります。
{% enddetails %}

{% details ワンクリック購読解除設定はメールテンプレートで利用できますか？ %}
いいえ、現在メールテンプレートにこの機能を追加する予定はありません。これらのテンプレートは送信ドメインに割り当てられていないためです。{% multi_lang_include product_feedback_cta.md context="gap" feature="per-domain sending for email templates" %}
{% enddetails %}

{% details この機能は、カスタムオプションに追加されたワンクリック購読解除URLが有効かどうかを確認しますか？ %}
いいえ、Brazeダッシュボードではリンクの確認や検証は行いません。開始前にURLを適切にテストしてください。
{% enddetails %}