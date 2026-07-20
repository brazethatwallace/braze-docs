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

カスタムフッターを作成または編集するには、以下の手順に従ってください。

1. **設定** > **メール設定** > **購読ページおよびフッター**に移動します。
2. **カスタムフッター**セクションに移動し、カスタムフッターをオンにします。
3. **編集**を選択し、**作成**セクションでフッターを編集します。
4. **プレビュー**を選択して、メールフッターが顧客の受信トレイでどのように表示されるかをプレビューします。オプションで**プレビューリンクをコピー**を選択すると、ランダムなユーザーに対してメールがどのように見えるかを示す共有可能なプレビューリンクを生成してコピーできます。リンクは7日間有効で、その後再生成が必要です。
5. テストメッセージを送信します。

![カスタムフッターの例。]({% image_buster /assets/img_archive/custom_footer.png %})

デフォルトのフッターは {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} 属性と物理的な郵送先住所を使用します。このデフォルトを使用する場合は、**プロトコル**で **&#60;other&#62;** を選択してください。

{% alert important %}
CAN-SPAM規制に準拠するため、カスタムフッターには購読解除リンクを含める必要があります。このLiquid属性 {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} または独自のカスタム購読解除URLを使用できます。購読解除リンクなしではカスタムフッターを保存できません。
{% endalert %}

![カスタムフッターに必要なプロトコルとURLの値。]({% image_buster /assets/img_archive/email_unsub_protocol.png %}){: style="max-width:50%;"}

## 購読解除リンクのないフッター {#footers-without-unsubscribe-links}

カスタムフッター {% raw %}`{{${email_footer}}}` を使用しながら `{{${set_user_to_unsubscribed_url}}}`{% endraw %} 購読解除リンクタグを含めないテンプレートを使用する場合は、十分にご注意ください。警告が表示されますが、購読解除リンクの有無にかかわらずメールを送信するかどうかはお客様の判断となります。

メールコンポーザーでの警告は以下のとおりです。

![フッターなしで作成されたメールの例。]({% image_buster /assets/img_archive/no_unsub_link_warning.png %})

キャンペーンコンポーザーでの警告は以下のとおりです。

![フッターなしのキャンペーン作成。]({% image_buster /assets/img_archive/no_footer_test.png %})

### カスタム購読解除リンクの追加 {#adding-a-custom-unsubscribe-link}

カスタム購読解除リンクを追加するには、カスタムフッター内の購読解除リンクを {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} からユーザーIDを含むクエリパラメーター付きの自社Webサイトへのリンクに変更します。例は以下のとおりです。
{% raw %}
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

次に、[`/email/status` エンドポイント]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status)を呼び出して、ユーザーの購読ステータスを更新します。詳細については、[メール購読の変更]({{site.baseurl}}/user_guide/channels/email/subscriptions#changing-email-subscriptions)に関するドキュメントを参照してください。

次に、この新しいリンクを保存します。デフォルトのBraze購読解除タグ {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} はフッターに含める必要があります。つまり、タグをコメント内または非表示の `<div>` タグ内に配置して「隠す」ことで、デフォルトリンクを含める必要があります。

## ベストプラクティス {#best-practices}

カスタムフッターの作成と使用にあたり、以下のベストプラクティスをお勧めします。

### 属性によるパーソナライゼーション {#personalizing-with-attributes}

カスタムフッターを作成する際、Brazeでは[パーソナライゼーション用の属性]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)の使用をお勧めします。デフォルトおよびカスタム属性のフルセットが利用可能ですが、以下は特に便利な属性です。

| 属性 | タグ |
| --------- | --- |
| ユーザーのメールアドレス | {% raw %}`{{${email_address}}}`{% endraw %} |
| ユーザーのカスタム購読解除URL | {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} <br><br>このタグは以前の {% raw %}`{{${unsubscribe_url}}}`{% endraw %} タグに代わるものです。新しい {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} タグの使用をお勧めします。 |
| ユーザーのカスタムオプトインURL | {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} |
| ユーザーのカスタム購読URL | {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}|
| ユーザーのカスタムBrazeユーザー設定センターURL | {% raw %}`{{${preference_center_url}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="属性によるパーソナライゼーション" }

### 購読解除リンクとオプトインリンクの追加 {#including-an-unsubscribe-link-and-opt-in-link}

{% raw  %}
ベストプラクティスとして、Brazeではカスタムフッターに購読解除リンク（``{{${set_user_to_unsubscribed_url}}}`` など）とオプトインリンク（``{{${set_user_to_opted_in_url}}}`` など）の両方を含めることをお勧めします。これにより、ユーザーは購読解除またはオプトインのいずれも行うことができ、ユーザーの一部からオプトインデータを受動的に収集できます。
{% endraw %}

### プレーンテキストメール用のカスタムフッターの設定 {#setting-custom-footers-for-plaintext-emails}

**メール設定**ページの**購読ページおよびフッター**タブから、プレーンテキストメール用のカスタムフッターを設定することもできます。HTMLメール用のカスタムフッターと同じルールに従います。

プレーンテキストフッターを含めない場合、BrazeはHTMLフッターから自動的に作成します。カスタムフッターの設定が完了したら、**保存**を選択してください。

![「カスタムプレーンテキストフッターを設定」オプションが選択されたメール。]({% image_buster /assets/img_archive/custom_footer_save_changes.png %}){: style="max-width:70%" }

## 考慮事項 {#considerations}

### BrazeAI Decisioning Studio™

[BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio)を使用している場合、{% raw %}`{{${email_footer}}}`{% endraw %} は標準的なLiquidタグではないことにご注意ください。Liquidの実行前に前処理されるため、{% raw %}`{{${email_footer}}}`{% endraw %} をコンテキスト変数の値として使用し `:rerender` フラグを呼び出しても、サイレントに失敗します。代わりに、メールフッターには[コンテンツブロック]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks#email-footers)を使用してください。

### リンクテンプレートとUTMパラメーター {#link-templates-and-utm-parameters}

{% raw %}`{{${email_footer}}}`{% endraw %} を使用している場合、カスタムメールフッター内のリンクにはリンクテンプレートが自動的に付加されません。フッターリンクにUTMパラメーターなどのリンクテンプレートが必要な場合は、代わりに[コンテンツブロック]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks#email-footers)を使用するか、カスタムフッター内の特定のリンクにUTMパラメーターを手動で追加してください。