---
nav_title: メールテンプレートの作成
article_title: メールテンプレートの作成
page_order: 0
description: "このリファレンス記事では、メールテンプレートの作成、カスタマイズ、管理方法について説明します。"
tool:
  - Templates
channel:
  - email
alias: "/dnd/email_template/"
search_rank: 1
---

# メールテンプレートの作成 {#create-an-email-template}

> Brazeダッシュボードには、カスタマイズされた目を引くメールを作成し、後でキャンペーンで使用するために保存できるメールテンプレートエディターがあります。独自の[HTMLメールテンプレート]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template)をアップロードすることもできます。

## ステップ1：メールテンプレートエディターに移動する {#step-1-navigate-to-the-email-template-editor}

Brazeダッシュボードで、**コンテンツ** > **メール**に移動します。

## ステップ2: 編集方法を選択する {#step-2-select-your-editing-experience}

編集方法として、**ドラッグ＆ドロップエディター**または **HTMLコードエディター**を選択します。

あらかじめデザインされたBrazeテンプレートから選択したり、新しいテンプレートを作成したり、既存のテンプレート（プレーンまたは[モバイルレスポンシブ]({{site.baseurl}}/releases/2018/may#mobile-responsive-email-templates)）を編集したりすることもできます。

![ドラッグ＆ドロップエディターまたはHTMLエディターの選択オプション、およびBrazeテンプレートからの選択オプションが表示された、企業の春セール用メールテンプレート。]({% image_buster /assets/img/email_templates/template2.png %})

{% alert note %}
既存のカスタムHTMLテンプレートは、ドラッグ＆ドロップエディターを使用して再作成する必要があります。
{% endalert %}

## ステップ3：テンプレートをカスタマイズする {#step-3-customize-your-template}

エディター体験を選択したら、メールテンプレートを自由にカスタマイズできます。HTMLエディターでHTMLを使用してブランディングを作成・再現したり、ドラッグ＆ドロップエディターでさまざまな[クリエイティブな詳細]({{site.baseurl}}/user_guide/channels/email/drag_and_drop)を含めたりできます。

### 購読解除リンクを含める {#include-an-unsubscribe-link}

メールテンプレートをデザインする際、購読解除リンクを含めていない場合、Brazeはメールに追加するよう促します。これは、すべてのマーケティングメールに法律で義務付けられているためです。この購読解除リンクは、Liquidタグ {% raw %}``${email_footer}``{% endraw %} を使用してメールの下部にフッターとして追加するか、テンプレートで[フッターをカスタマイズ]({{site.baseurl}}/user_guide/channels/email/subscriptions#custom-footer)することで追加できます。

## ステップ4: メールエラーの確認 {#step-4-check-for-email-errors}

メールエラーは、メッセージワークフローの「**作成**」タブに表示されます。エラーがある場合、先に進むことができません。「警告」はベストプラクティスに従うためのリマインダーを示します。ビジネスの状況に応じて、これらを無視することもできます。

![サンプルメールのエラーと警告のリスト。]({% image_buster /assets/img/dnd_compose_error.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

エディターで検出されるエラーの一覧は以下のとおりです。

- 正しくないLiquid構文
- [メール本文が400KBを超えている場合。本文は102KB未満にすることを強く推奨します]({{site.baseurl}}/user_guide/channels/email/best_practices)
- 購読解除リンクのないテンプレート
- **本文**または**件名**が空白のメール
- 購読解除リンクのないメール

## ステップ5:メッセージをプレビューしてテストする {#step-5-preview-and-test-your-message}

テンプレートの作成が完了したら、送信前にテストできます。

概要画面の下部にある**プレビューとテスト**を選択します。ここでは、顧客の受信トレイにメールがどのように表示されるかをプレビューできます。**ユーザーとしてプレビュー**を選択すると、ランダムなユーザーとしてメールをプレビューしたり、特定のユーザーを選択したり、カスタムユーザーを作成したりできます。これにより、Connected Contentやパーソナライゼーションの呼び出しが正しく機能しているかどうかをテストできます。

次に、**プレビューリンクをコピー**を使って、ランダムなユーザーに対してメールがどのように見えるかを示す共有可能なプレビューリンクを生成してコピーできます。詳細については、[共有可能なプレビュー]({{site.baseurl}}/user_guide/messaging/governance/shareable_preview)を参照してください。

また、デスクトップ、モバイル、プレーンテキストの各表示を切り替えて、さまざまなコンテキストでメッセージがどのように表示されるかを確認できます。

{% alert tip %}
ダークモードのユーザーにメールがどのように見えるか気になりますか？**プレビューとテスト**セクション内にある**ダークモードプレビュー**トグルを選択してください（ドラッグ＆ドロップエディターのみ）。
{% endalert %}

最終確認の準備ができたら、**テスト送信**を選択し、自分自身またはコンテンツテスターのグループにテストメッセージを送信して、さまざまなデバイスやメールクライアントでメールが正しく表示されることを確認します。

![テスト用に送信されるメールプレビューの例。]({% image_buster /assets/img_archive/newEmailTest.png %})

テンプレートに問題がある場合や変更を加えたい場合は、**メールを編集**を選択してエディターに戻ります。**クラシック**エディターで行った編集は、HTMLエディターやメールプレビューに反映されない場合があります。

## ステップ6:テンプレートを保存する {#step-6-save-your-template}

**テンプレートを保存**を選択して、テンプレートを保存してください。これで、任意のキャンペーンやキャンバスコンポーネントでこのテンプレートを使用する準備が整いました。テンプレートにアクセスするには、テンプレートの作成に使用した編集エクスペリエンスを選択し、利用可能なテンプレートの一覧から選択します。

{% alert note %}
既存のテンプレートに編集を加えた場合、その変更は以前のバージョンのテンプレートを使用して作成されたキャンペーンには反映されません。
{% endalert %}

### テンプレートを管理する {#manage-your-templates}

メールテンプレートは、**テンプレート** > **メールテンプレート**で表示できます。ステータス、タイプ、タグ、作成したユーザーでフィルタリングしたり、テンプレート名で検索したりできます。これらのテンプレートを表示するには、**メールテンプレートを表示**などの関連するユーザー権限が必要です。詳細については、[ユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)を参照してください。

メールテンプレートが増えてきたら、メールテンプレートを[複製]({{site.baseurl}}/user_guide/messaging/templates/managing_templates#duplicating-templates)したり[アーカイブ]({{site.baseurl}}/user_guide/messaging/templates/managing_templates#archiving-templates)したりできます。テンプレートとクリエイティブコンテンツのライブラリの作成と管理については、[テンプレートとメディア]({{site.baseurl}}/user_guide/messaging/templates)で詳しく説明しています。

### APIキャンペーンでテンプレートを使用する {#use-your-templates-in-api-campaigns}

メールをAPIキャンペーンに使用するには、`email_template_id`が必要です。これは、Brazeで作成したメールテンプレートの下部に表示されます。

![メールテンプレートの下部にあるAPI識別子。]({% image_buster /assets/img/email_templates/template5.png %})

### メールテンプレートにコメントする {#comment-on-email-templates}

ドラッグ＆ドロップエディターで、メールテンプレートに対して共同作業やコメントができます。

1. コメントしたいメール本文のコンテンツブロックまたは行を選択します。
2. <i class="fas fa-comment" aria-label="コメント"></i> コメントアイコンを選択します。
3. サイドバーにコメントを入力し、**送信**を選択します。
4. コメントを入力したら、**完了**を選択します。
5. **テンプレートを保存**を選択して、コメントを保存します。

テンプレートが保存されると、未対応のコメントの上にアイコンが表示されます。**解決**を選択して、これらのコメントを解決します。

![「いい感じです」というメールテンプレートのコメント。]({% image_buster /assets/img/email_templates/template_comment.png %})

メールテンプレートに関するよくある質問への回答については、[テンプレートFAQ]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq)をご覧ください。