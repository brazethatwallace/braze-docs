---
nav_title: FAQ
article_title: メールテンプレートとリンクテンプレートのFAQ
page_order: 10

page_type: FAQ
description: "このページでは、メールテンプレートとリンクテンプレートに関するよくある質問について説明します。"
tool:
  - Templates
channel: email

---

# よくある質問 {#frequently-asked-questions}

> このページでは、メールテンプレートとリンクテンプレートに関するよくある質問への回答を提供します。

## メールテンプレート {#email-templates}

### メールに「ブラウザでこのメールを表示」リンクを追加できますか？ {#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails}

いいえ、Brazeではこの機能を提供していません。これは、メールの大多数がモバイルデバイスや最新のメールクライアントで開封されており、画像やコンテンツが問題なくレンダリングされるためです。

**回避策：** 同じ結果を実現するには、メールのコンテンツを外部のランディングページ（自社のWebサイトなど）にホストし、メール本文の編集時に**リンク**ツールを使用して、作成中のメールキャンペーンからリンクすることができます。

### メールテンプレートにカスタム購読解除リンクを作成するにはどうすればよいですか？ {#how-do-i-create-a-custom-unsubscribe-link-for-my-email-templates}

購読解除ページにはリダイレクトオプションがあります。

カスタムフッターの購読解除リンクを {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} から、ユーザー IDを含むクエリパラメーター付きの自社Webサイトへのリンクに変更できます。例は以下の通りです：
{% raw %}
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

次に、[`/email/status` エンドポイント]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status)を呼び出して、ユーザーの購読ステータスを更新できます。詳細については、[メール購読の変更]({{site.baseurl}}/user_guide/channels/email/subscriptions#changing-email-subscriptions)に関するドキュメントを参照してください。

この新しいリンクを保存するには、デフォルトのBraze購読解除タグ {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} がフッターに含まれている必要があります。つまり、タグをコメント内または非表示の `<div>` タグ内に配置して「隠す」ことで、デフォルトリンクを含める必要があります。

- **コメント内のタグの例：** タグをコメント内に配置する例：`<!-- ${set_user_to_unsubscribed_url} -->`
- **非表示の `<div>` タグ内のコメントの例：** {%raw%}`<div style="display:none;max-height:0px;overflow:hidden;">${set_user_to_unsubscribed_url}</div>`{%endraw%}

### 現在キャンペーンで使用されているメールテンプレートを編集するとどうなりますか？ {#what-happens-if-i-edit-an-email-template-that-is-currently-being-used-in-a-campaign}

既存のテンプレートに加えた編集は、そのテンプレートの以前のバージョンを使用して作成されたキャンペーンには反映されません。REST API本文でテンプレートを使用するAPIキャンペーンの場合、Brazeは送信時にテンプレートの最新バージョンを使用します。

## リンクテンプレート {#link-templates}

### メールに複数のリンクテンプレートをアップロードできますか？ {#can-i-upload-multiple-link-templates-to-my-email}

はい、メールメッセージに必要な数だけテンプレートを挿入できます。ベストプラクティスとして、リンクが2,000文字を超えないようにメールをテストしてください。ほとんどのブラウザではリンクが短縮またはカットされます。

### すべてのタグが適用された状態でリンクをプレビューするにはどうすればよいですか？ {#how-do-i-preview-my-links-with-all-of-the-tags-applied}

リンクをプレビューする方法はいくつかあります。[リンクテンプレート]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template)を適用した後、自分宛てに[テストメール]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages)を送信して、すべてのリンクを確認できます。

新しいタブのプレビューペインからリンクを開いて確認することもできます。また、プレビューペインでリンクにカーソルを合わせると、ブラウザの下部にリンクが表示されます。

### リンクテンプレートはLiquidとどのように連携しますか？ {#how-does-link-templating-work-with-liquid}

リンクテンプレートは、Liquidの展開が行われる前に各URLに展開・追加されます。URLの一部がLiquidスニペットを使用して生成される場合、リンクテンプレートが正しく展開されるように、URLのベースとクエスチョンマーク（?）をハードコードすることをお勧めします。

Liquidにクエスチョンマーク（?）を追加しないでください。リンクテンプレートが最初にクエスチョンマーク（?）を追加し、その後Liquidの展開プロセスで2つ目のクエスチョンマーク（?）が追加されてしまいます。

#### ハードコードされたURLとカスタム属性 {#hardcoded-urls-versus-custom-attributes}

HTMLエディターでハードコードされたURL（例：`https://braze.com?12345`）を使用する場合、Brazeは`?`がすでに存在することを検出し、自動的に`&`を使用してリンクテンプレートのパラメーターを追加します。ただし、`?`を含むURLが格納されたカスタム属性（例：{% raw %}`{{custom_attribute.${my_url}}}`{% endraw %}、ここで`my_url`は`https://braze.com?12345`）を使用する場合、Brazeはカスタム属性の値に`?`がすでに存在するかどうかを確認しません。この場合、リンクテンプレートはパラメーターの前にもう1つの`?`を追加し、`https://braze.com?12345?utm_source=...`のようなURLになります。

クエリパラメーターを含む可能性のあるカスタム属性を使用する際にこの問題を回避するには、カスタム属性の値にクエリパラメーターが含まれているかどうかに基づいて、カスタム属性の後に`?`または`&`をハードコードしてください。例えば、カスタム属性に常に`?`が含まれている場合は、{% raw %}`{{custom_attribute.${my_url}}}&`{% endraw %}を使用して、リンクテンプレートがパラメーターを正しく追加するようにしてください。

## リンクエイリアス {#link-aliasing}

### リンクエイリアスを有効にすると、Content Blocksやリンクテンプレートにどのような影響がありますか？ {#how-will-enabling-link-aliasing-impact-my-content-blocks-and-link-templates}

新しく作成されるすべてのContent Blocksには、リンクエイリアスがワークスペース全体に適用されます。これは企業レベルの機能であるためです。

リンクエイリアスを有効にしても、既存のContent Blocksは変更されません。既存のリンクテンプレートも変更されませんが、メッセージ内の既存のリンクテンプレートセクションは削除されます。詳細については、[Content Blocksでのリンクエイリアス]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing#link-aliasing-in-content-blocks)を参照してください。

### HTMLアンカータグ内でLiquidの条件ロジックを完全に使用できますか？ {#can-i-use-liquid-conditional-logic-entirely-within-an-html-anchor-tag}

いいえ、BrazeのリンクエイリアスはHTMLを正しく認識できません。

このようなロジックが、HTMLの解析を必要とする機能（プリヘッダーやリンクテンプレートなど）と併用された場合、HTMLをスキャンするために使用されるライブラリがアンカータグを変更し、適切な`href`がテンプレート化されなくなる可能性があります。このライブラリはLiquidコードを認識しないため、HTMLが無効であると判断します。

代わりに、各段階で完全なアンカータグを含むLiquidロジックを使用してください。このロジックには有効なHTMLの複数のインスタンスが含まれるため、HTMLの解析に干渉しません。また、変数を割り当ててから適切なアンカータグにテンプレート化することで、ロジックを簡素化することもできます。