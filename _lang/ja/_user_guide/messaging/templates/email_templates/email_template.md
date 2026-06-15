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

> Brazeダッシュボードには、カスタマイズされた目を引くメールを作成し、後でCampaignsで使用するために保存できるメールテンプレートエディターがあります。独自の[HTMLメールテンプレート]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template/)をアップロードすることもできます。

## ステップ 1:メールテンプレートエディターに移動する {#step-1-navigate-to-the-email-template-editor}

Brazeダッシュボードで、**コンテンツ** > **メール**に移動します。

## ステップ 2:編集エクスペリエンスを選択する {#step-2-select-your-editing-experience}

編集エクスペリエンスとして、**ドラッグ＆ドロップエディター**または**HTMLコードエディター**を選択します。

また、あらかじめデザインされたBrazeテンプレートから選択したり、新しいテンプレートを作成したり、既存のテンプレート（プレーンまたは[モバイルレスポンシブ]({{site.baseurl}}/help/release_notes/2018/may/#mobile-responsive-email-templates)）を編集したりすることもできます。

![ドラッグ＆ドロップエディターまたはHTMLエディターを選択するオプション、またはBrazeテンプレートから選択するオプションが表示された、企業のスプリングセール用メールテンプレート。]({% image_buster /assets/img/email_templates/template2.png %})

{% alert note %}
既存のカスタムHTMLテンプレートは、ドラッグ＆ドロップエディターを使用して再作成する必要があります。
{% endalert %}

## ステップ 3:テンプレートをカスタマイズする {#step-3-customize-your-template}

エディターエクスペリエンスを選択したら、メールテンプレートを自由にカスタマイズできます。HTMLエディターでHTMLを使用してブランディングを作成・再現したり、ドラッグ＆ドロップエディターでさまざまな[クリエイティブの詳細]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/#creative-details)を含めたりできます。

### 配信停止リンクを含める {#include-an-unsubscribe-link}

メールテンプレートをデザインする際、配信停止リンクを含めない場合、Brazeはメールに追加するよう促します。これは、すべてのマーケティングメールで法律上必要とされるためです。Liquidタグ {% raw %}``${email_footer}``{% endraw %} を使用してメールの下部にフッターとしてこの配信停止リンクを追加するか、テンプレートで[フッターをカスタマイズ]({{site.baseurl}}/user_guide/channels/email/subscriptions/#custom-footer)できます。

## ステップ 4:メールエラーを確認する {#step-4-check-for-email-errors}

メールエラーは、メッセージワークフローの**作成**タブに表示されます。エラーがあると先に進めません。「警告」は、ベストプラクティスに従うためのリマインダーを示します。ビジネスの状況に応じて、無視することもできます。

![サンプルメールのエラーと警告のリスト。]({% image_buster /assets/img/dnd_compose_error.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

エディターで検出されるエラーのリストは以下のとおりです。

- 不正なLiquid構文
- [400KBを超えるメール本文。本文は102KB未満にすることを強く推奨します]({{site.baseurl}}/user_guide/channels/email/best_practices/)
- 配信停止リンクのないテンプレート
- **本文**または**件名**が空白のメール
- 配信停止リンクのないメール

## ステップ 5:メッセージをプレビューしてテストする {#step-5-preview-and-test-your-message}

テンプレートの作成が完了したら、送信前にテストできます。

概要画面の下部で、**Preview and Test**を選択します。ここでは、顧客の受信トレイでメールがどのように表示されるかをプレビューできます。**Preview as User**を選択すると、ランダムなユーザーとしてメールをプレビューしたり、特定のユーザーを選択したり、カスタムユーザーを作成したりできます。これにより、コネクテッドコンテンツやパーソナライゼーションの呼び出しが正しく機能しているかテストできます。

また、**Copy preview link**を選択して、ランダムなユーザーに対してメールがどのように見えるかを示す共有可能なプレビューリンクを生成してコピーできます。リンクは7日間有効で、その後再生成が必要です。

デスクトップ、モバイル、プレーンテキストのビューを切り替えて、さまざまなコンテキストでメッセージがどのように表示されるかを確認することもできます。

{% alert tip %}
ダークモードのユーザーにメールがどのように見えるか気になりますか？**Preview and Test**セクション（ドラッグ＆ドロップエディターのみ）にある**Dark Mode Preview**トグルを選択してください。
{% endalert %}

最終確認の準備ができたら、**Test Send**を選択し、自分自身またはコンテンツテスターのグループにテストメッセージを送信して、さまざまなデバイスやメールクライアントでメールが正しく表示されることを確認します。

![テスト用に送信されるメールプレビューの例。]({% image_buster /assets/img_archive/newEmailTest.png %})

テンプレートに問題がある場合や変更を加えたい場合は、**Edit Email**を選択してエディターに戻ります。**Classic**エディターで行った編集は、HTMLエディターやメールプレビューに反映されない場合があることにご注意ください。

## ステップ 6:テンプレートを保存する {#step-6-save-your-template}

**Save Template**を選択して、テンプレートを必ず保存してください。これで、任意のCampaignまたはCanvasコンポーネントでこのテンプレートを使用する準備が整いました。テンプレートにアクセスするには、作成時に使用した編集エクスペリエンスを選択し、利用可能なテンプレートのリストから選択します。

{% alert note %}
既存のテンプレートに編集を加えた場合、以前のバージョンのテンプレートを使用して作成されたCampaignsにはその変更は反映されません。
{% endalert %}

### テンプレートを管理する {#manage-your-templates}

メールテンプレートは、**テンプレート** > **メールテンプレート**で表示でき、ステータス、タイプ、タグ、作成者でフィルタリングしたり、テンプレート名で検索したりできます。これらのテンプレートを表示するには、**View Email Templates**などの関連するユーザー権限が必要です。詳細については、[ユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/)を参照してください。

メールテンプレートを増やしていくにつれて、メールテンプレートを[複製]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/#duplicate-templates)したり[アーカイブ]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/#archive-templates)したりできます。テンプレートとクリエイティブコンテンツのライブラリーの作成と管理について詳しくは、[テンプレートとメディア]({{site.baseurl}}/user_guide/messaging/templates/)をご覧ください。

### APIキャンペーンでテンプレートを使用する {#use-your-templates-in-api-campaigns}

APIキャンペーンでメールを使用するには、`email_template_id`が必要です。これは、Brazeで作成されたメールテンプレートの下部に記載されています。

![メールテンプレートの下部にあるAPI識別子。]({% image_buster /assets/img/email_templates/template5.png %})

### メールテンプレートにコメントする {#comment-on-email-templates}

ドラッグ＆ドロップエディターで、メールテンプレートに対して共同作業やコメントができます。

1. コメントしたいメール本文のコンテンツブロックまたは行を選択します。
2. <i class="fas fa-comment"></i> コメントアイコンを選択します。
3. サイドバーにコメントを入力し、**Submit**を選択します。
4. コメントを入力したら、**Done**を選択します。
5. **Save Template**を選択してコメントを保存します。

テンプレートが保存されると、未対応のコメントの上にアイコンが表示されます。**Resolve**を選択して、これらのコメントを解決します。

![「Looks good to me」と書かれたメールテンプレートのコメント。]({% image_buster /assets/img/email_templates/template_comment.png %})

メールテンプレートに関するよくある質問への回答については、[テンプレートFAQ]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq/)をご確認ください。