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

いいえ、Brazeではこの機能を提供していません。これは、メールの大多数がモバイルデバイスや最新のメールクライアントで開封されるようになっており、画像やコンテンツが問題なくレンダリングされるためです。

**回避策：** 同じ結果を実現するには、メールのコンテンツを外部のランディングページ（自社のWebサイトなど）にホストし、メール本文の編集時に**リンク**ツールを使用してメールキャンペーンからリンクすることができます。

### メールテンプレートにカスタム配信停止リンクを作成するにはどうすればよいですか？ {#how-do-i-create-a-custom-unsubscribe-link-for-my-email-templates}

配信停止ページにはリダイレクトオプションがあります。

カスタムフッターの配信停止リンクを {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} から、ユーザーIDを含むクエリパラメーター付きの自社Webサイトへのリンクに変更できます。例：
{% raw %}
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

次に、[`/email/status` エンドポイント]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status)を呼び出して、ユーザーのサブスクリプションステータスを更新できます。詳細については、[メールサブスクリプションの変更]({{site.baseurl}}/user_guide/channels/email/subscriptions#changing-email-subscriptions)に関するドキュメントを参照してください。

この新しいリンクを保存するには、デフォルトのBraze配信停止タグ {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} がフッターに含まれている必要があります。つまり、タグをコメント内または非表示の `<div>` タグ内に配置して「隠す」ことで、デフォルトリンクを含める必要があります。

- **コメント内のタグの例：** `<!-- ${set_user_to_unsubscribed_url} -->`
- **非表示の `<div>` タグ内のコメントの例：** {%raw%}`<div style="display:none;max-height:0px;overflow:hidden;">${set_user_to_unsubscribed_url}</div>`{%endraw%}

### 現在キャンペーンで使用されているメールテンプレートを編集するとどうなりますか？ {#what-happens-if-i-edit-an-email-template-that-is-currently-being-used-in-a-campaign}

既存のテンプレートに加えた編集は、そのテンプレートの以前のバージョンを使用して作成されたキャンペーンには反映されません。REST API本文でテンプレートを使用するAPIキャンペーンの場合、Brazeは送信時にテンプレートの最新バージョンを使用します。

## リンクテンプレート {#link-templates}

### メールに複数のリンクテンプレートをアップロードできますか？ {#can-i-upload-multiple-link-templates-to-my-email}

はい、メールメッセージに必要な数だけテンプレートを挿入できます。ベストプラクティスとして、ほとんどのブラウザがリンクを短縮またはカットするため、リンクが2,000文字を超えないようにメールをテストすることをお勧めします。

### すべてのタグが適用された状態でリンクをプレビューするにはどうすればよいですか？ {#how-do-i-preview-my-links-with-all-of-the-tags-applied}

リンクをプレビューする方法はいくつかあります。[リンクテンプレート]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template)を適用した後、自分宛てに[テストメール]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages)を送信して、すべてのリンクを確認できます。

新しいタブのプレビューペインからリンクを開いて確認することもできます。また、プレビューペインでリンクにカーソルを合わせると、ブラウザの下部にリンクが表示されます。

### リンクテンプレートはLiquidとどのように連携しますか？ {#how-does-link-templating-work-with-liquid}

リンクテンプレートは、Liquidの展開が行われる前に各URLに展開・追加されます。URLの一部がLiquidスニペットで生成される場合、リンクテンプレートが正しく展開されるように、URLのベースとクエスチョンマーク（?）をハードコードすることをお勧めします。

Liquidにクエスチョンマーク（?）を追加しないでください。リンクテンプレートが最初にクエスチョンマーク（?）を追加し、その後Liquidの展開プロセスで2つ目のクエスチョンマーク（?）が追加されてしまいます。

## リンクエイリアス {#link-aliasing}

### リンクエイリアスを有効にすると、Content Blocksとリンクテンプレートにどのような影響がありますか？ {#how-will-enabling-link-aliasing-impact-my-content-blocks-and-link-templates}

新しく作成されるすべてのContent Blocksには、会社レベルの機能であるため、ワークスペース全体でリンクエイリアスが適用されます。

既存のContent Blocksは、リンクエイリアスが有効になっても変更されません。既存のリンクテンプレートも変更されませんが、メッセージ内の既存のリンクテンプレートセクションは削除されます。詳細については、[Content Blocksでのリンクエイリアス]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing#link-aliasing-in-content-blocks)を参照してください。

### HTMLアンカータグ内でLiquidの条件ロジックを完全に使用できますか？ {#can-i-use-liquid-conditional-logic-entirely-within-an-html-anchor-tag}

いいえ、Brazeのリンクエイリアスは HTMLを正しく認識できません。

このようなロジックがHTMLの解析を必要とする機能（プリヘッダーやリンクテンプレートなど）と併用される場合、HTMLをスキャンするために使用されるライブラリがアンカータグを変更し、適切な `href` がテンプレート化されなくなる可能性があります。このライブラリはLiquidコードを認識しないため、HTMLが無効であると判断します。

代わりに、各段階で完全なアンカータグを含むLiquidロジックを使用してください。これにより、ロジックに有効なHTMLの複数のインスタンスが含まれるため、HTMLの解析に干渉しません。また、変数を割り当ててから適切なアンカータグにテンプレート化することで、ロジックを簡素化することもできます。