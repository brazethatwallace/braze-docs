---
nav_title: カスタムメールフッター
article_title: カスタムメールフッター
page_order: 6.5
description: "この記事では、ワークスペース全体のカスタムメールフッターを設定する方法について説明します。"
channel:
  - email

---

# カスタムメールフッター {#custom-email-footer}

> ワークスペース全体のカスタムメールフッターを設定し、{% raw %}`{{${email_footer}}}`{% endraw %} Liquid属性を使用してすべてのメールにテンプレートとして適用できます。

カスタムメールフッターを使用すると、メールテンプレートやメールキャンペーンごとに新しいフッターを作成する必要がなくなります。新規および既存のすべてのメールキャンペーンに、カスタムフッターへの変更が反映されます。[CAN-SPAM Act of 2003](https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business) に準拠するには、メールに会社の物理的な住所と購読解除リンクを含める必要があることにご注意ください。

{% alert warning %}
カスタムフッターが上記の要件を満たしていることを確認するのは、お客様の責任です。
{% endalert %}

## カスタムフッターの作成 {#create-your-custom-footer}

カスタムフッターを作成または編集するには、以下の手順に従います。

1. **設定** > **メール設定** > **購読ページとフッター**に移動します。
2. **カスタムフッター**セクションに移動し、カスタムフッターをオンにします。
3. **編集**を選択し、**作成**セクションでフッターを編集します。
4. **プレビュー**を選択して、メールフッターが顧客の受信トレイでどのように表示されるかをプレビューします。オプションで**プレビューリンクをコピー**を選択すると、ランダムなユーザーに対してメールがどのように表示されるかを示す共有可能なプレビューリンクを生成してコピーできます。詳細については、[共有可能なプレビュー]({{site.baseurl}}/user_guide/messaging/governance/shareable_preview)を参照してください。
5. テストメッセージを送信します。

![カスタムフッターの例。]({% image_buster /assets/img_archive/custom_footer.png %})

デフォルトのフッターでは、{% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} 属性と物理的な郵送先住所が使用されます。このデフォルトを使用する場合は、**プロトコル**で **&#60;other&#62;** を選択してください。

{% alert important %}
CAN-SPAM規制に準拠するため、カスタムフッターには購読解除リンクを含める必要があります。このLiquid属性 {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} を使用するか、独自のカスタム購読解除URLを使用できます。購読解除リンクがないカスタムフッターは保存できません。
{% endalert %}

![カスタムフッターに必要なプロトコルとURLの値。]({% image_buster /assets/img_archive/email_unsub_protocol.png %}){: style="max-width:50%;"}

## 購読解除リンクのないフッター {#footers-without-unsubscribe-links}

カスタムフッター {% raw %}`{{${email_footer}}}`{% endraw %} を使用しながら、購読解除リンクタグ `{{${set_user_to_unsubscribed_url}}}` を含めない場合は十分に注意してください。警告が表示されますが、購読解除リンクの有無にかかわらずメールを送信するかどうかはお客様の判断です。

メールコンポーザーでの警告の例を以下に示します。

![フッターなしで作成されたメールの例。]({% image_buster /assets/img_archive/no_unsub_link_warning.png %})

キャンペーンコンポーザーでの警告の例を以下に示します。

![フッターなしのキャンペーン作成。]({% image_buster /assets/img_archive/no_footer_test.png %})

### カスタム購読解除リンクの追加 {#adding-a-custom-unsubscribe-link}

カスタム購読解除リンクを追加するには、カスタムフッター内の購読解除リンクを {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} から、ユーザー IDをクエリパラメーターに含む自社Webサイトへのリンクに変更します。例を以下に示します。
{% raw %}
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

次に、[`/email/status` エンドポイント]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status)を呼び出して、ユーザーの購読ステータスを更新します。詳細については、[メール購読の変更]({{site.baseurl}}/user_guide/channels/email/subscriptions#changing-email-subscriptions)に関するドキュメントを参照してください。

その後、この新しいリンクを保存します。デフォルトのBraze購読解除タグ {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} はフッターに含める必要があります。つまり、デフォルトリンクをコメント内または非表示の `<div>` タグ内に配置して「隠す」ことで含める必要があります。

## ベストプラクティス {#best-practices}

カスタムフッターを作成・使用する際には、以下のベストプラクティスをお勧めします。

### 属性を使ったパーソナライゼーション {#personalizing-with-attributes}

カスタムフッターを作成する際、Brazeでは[パーソナライゼーション用の属性]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)の使用をお勧めします。デフォルトおよびカスタム属性のフルセットが利用可能ですが、特に便利なものをいくつかご紹介します。

| 属性 | タグ |
| --------- | --- |
| ユーザーのメールアドレス | {% raw %}`{{${email_address}}}`{% endraw %} |
| ユーザーのカスタム購読解除URL | {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} <br><br>このタグは以前の{% raw %}`{{${unsubscribe_url}}}`{% endraw %}タグに代わるものです。新しい{% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %}タグの使用をお勧めします。 |
| ユーザーのカスタムオプトインURL | {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} |
| ユーザーのカスタム購読URL | {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}|
| ユーザーのカスタムBrazeユーザー設定センターURL | {% raw %}`{{${preference_center_url}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="属性を使ったパーソナライゼーション" }

### 購読解除リンクとオプトインリンクを含める {#including-an-unsubscribe-link-and-opt-in-link}

{% raw  %}
ベストプラクティスとして、Brazeではカスタムフッターに購読解除リンク（``{{${set_user_to_unsubscribed_url}}}``など）とオプトインリンク（``{{${set_user_to_opted_in_url}}}``など）の両方を含めることをお勧めします。これにより、ユーザーは購読解除やオプトインが可能になり、一部のユーザーからオプトインデータを受動的に収集できます。
{% endraw %}

### プレーンテキストメール用のカスタムフッターを設定する {#setting-custom-footers-for-plaintext-emails}

**メール設定**ページの**購読ページとフッター**タブから、プレーンテキストメール用のカスタムフッターを設定することもできます。HTMLメール用のカスタムフッターと同じルールに従います。

プレーンテキストフッターを含めない場合、BrazeはHTMLフッターから自動的にフッターを生成します。カスタムフッターの内容に問題がなければ、**保存**を選択してください。

![「カスタムプレーンテキストフッターを設定」オプションが選択されたメール。]({% image_buster /assets/img_archive/custom_footer_save_changes.png %}){: style="max-width:70%" }

## 注意事項 {#considerations}


### BrazeAI Decisioning Studio™

[BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio)を使用している場合、{% raw %}`{{${email_footer}}}`{% endraw %}は標準的なLiquidタグではないことに注意してください。これはLiquidの実行前に前処理されるため、{% raw %}`{{${email_footer}}}`{% endraw %}をコンテキスト変数の値として使用し、`:rerender`フラグを呼び出してもサイレントに失敗します。代わりに、メールフッターには[コンテンツブロック]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks#email-footers)を使用してください。

### リンクテンプレートとUTMパラメーター {#link-templates-and-utm-parameters}

{% raw %}`{{${email_footer}}}`{% endraw %}を使用している場合、カスタムメールフッター内のリンクにリンクテンプレートは自動的に追加されません。フッターリンクにUTMパラメーターなどのリンクテンプレートが必要な場合は、代わりに[コンテンツブロック]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks#email-footers)を使用するか、カスタムフッター内の特定のリンクにUTMパラメーターを手動で追加してください。