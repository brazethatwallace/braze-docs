---
nav_title: Iterate
article_title: Iterate
alias: /partners/iterate/
description: "このリファレンス記事では、BrazeとIterateのパートナーシップについて説明します。アンケートを活用して顧客データを充実させ、さらなるインサイトを追加できます。"
page_type: partner
search_tag: Partner

---

# Iterate

> [Iterate](https://iteratehq.com) は、顧客から学ぶためのアンケートやフィードバックツールを提供し、ブランドに合ったユーザーフレンドリーなリサーチ体験を実現します。

_この統合はIterateによって管理されています。_

## 統合について {#about-the-integration}

IterateとBrazeの統合により、製品やキャンペーン内でIterateアンケートをネイティブかつシームレスに配信できます。アンケートの回答はBrazeでカスタムユーザー属性として記録できるため、ユーザーの全体像を把握したり、強力な新しいオーディエンスやセグメントを作成したりできます。

アプリやWebサイトにBraze SDKをインストールすれば、Brazeで利用可能なセグメンテーションやターゲティングツールを使用して、任意のトリガーやカスタムセグメントに基づき、オーディエンスの特定の部分にアプリ内メッセージでアンケートを配信できます。Iterateのアンケートは、メールキャンペーンに直接埋め込むことも、プッシュやその他のキャンペーンタイプにリンクとして組み込むこともできます。

## 前提条件 {#prerequisites}

| 要件 | 提供元 |
|---|---|
| Iterateアカウント | このパートナーシップを活用するには、[Iterateアカウント](https://iteratehq.com)が必要です。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。Brazeアプリ内メッセージでアンケートを送信するには、`kpi.mau.data_series` 権限も必要です。<br><br> これは、Brazeダッシュボードの**設定** > **API キー**から作成できます。|
| Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントはインスタンスの[Braze URL]({{site.baseurl}}/api/basics/#endpoints)に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース {#use-cases}

Iterateを使用すると、ほぼすべてのタイプのデータを収集できます。個人情報（名前、年齢、メール）、パフォーマンスデータ（NPS、顧客満足度、星評価）、好み（好みのデバイス、好みのコミュニケーション頻度）、性格（好きな本、犬派か猫派か）など多岐にわたります。質問の内容、収集するデータの種類、作成するオーディエンスはすべてお客様が決定します。

## 統合 {#integration}

### はじめに：BrazeとIterateを接続する {#getting-started-connect-braze-with-iterate}

Iterateアカウントにログインし、**会社の設定**ページでBraze RESTエンドポイントとREST APIキーを追加します。

### アンケートをアプリ内メッセージとして配信する {#deliver-surveys-as-an-in-app-message}

#### ステップ1：アンケートを作成する {#step-1-create-your-survey}

アンケートを作成する前に、Iterateの設定で**Enable in-app message surveys**トグルをオンにします。

次に、Iterateで新しいアンケートを作成し、関連するアンケートの質問を追加します。適切であれば、アンケートの前に表示されるプロンプトメッセージを含めることもできます。アンケートのタイプとして**Send via Braze In-App Message**を選択します。

アンケートが完了したら、**Publish**タブで**Copy and paste your embed code**の下にあるコードスニペットをコピーします。

#### ステップ2：アンケートを共有する {#step-2-share-your-survey}

Brazeで新しいアプリ内メッセージングキャンペーンを作成し、メッセージングタイプとして**Custom Code**を選択し、コードスニペットをメッセージに貼り付けます。次に、クリック時のメッセージ動作として**Wait for User to Dismiss**を選択します。

他のアプリ内メッセージングキャンペーンと同様にキャンペーンの設定を続け、配信方法を選択し、オーディエンスをターゲットに設定します。

### メールまたはプッシュでアンケートを配信する {#deliver-surveys-through-email-or-push}

#### ステップ1：アンケートを作成する

Iterateで新しいメールアンケートまたはリンクアンケートを作成し、関連するアンケートの質問を追加します。質問を作成し、デザインをカスタマイズしたら、**Send survey > Integrations > Braze**を選択します。

すると、Brazeに回答を送信するための設定オプションが表示されます。そのアンケートの回答をBrazeに送信できるようにするため、統合をオンに切り替えます。

#### ステップ2：アンケートを共有する

アンケートは2通りの方法で共有できます。最初の質問をメッセージに埋め込む方法と、Iterateプラットフォーム上のアンケートへの直接リンクを含める方法です。

![Iterateのリンクオプション]({% image_buster /assets/img/iterate.png %})

- **コードを埋め込む**
  - **Send survey**タブのBraze統合セクションにある**Email embed code**の下のコードスニペットをコピーします。BrazeメールのHTMLに、アンケートの冒頭を表示したい場所にコードを挿入します。
  - アンケートの質問の表示に問題がある場合や、形式が正しくない場合は、メッセージ作成画面の**Sending Info**タブに移動して**Inline CSS**のチェックを外します。
- **リンクを含める**
  - **Send survey**タブのBraze統合セクションにある**Survey Link**の下のリンクをコピーします。リンクに含まれるLiquid {% raw %}`?user_braze_id={{${braze_id}}}`{% endraw %} は、送信時にユーザーごとに自動的に置き換えられることに注意してください。

### 次のステップ：フォローアップキャンペーンを作成する {#next-steps-build-follow-up-campaigns}

ユーザーが回答すると、プロファイルにリアルタイムでデータが反映されます。このデータを使用して、ユーザーをセグメント化し、パーソナライズされたフォローアップキャンペーンを送信できます。例えば、「Do you enjoy our products?」という質問を送信した場合、カスタムユーザー属性 `Do you enjoy our products?` を持ち「Yes」または「No」と回答したユーザーのセグメントを作成し、これらのユーザーをターゲットにできます。

## Brazeカスタムイベント {#braze-custom-events}

ユーザーがアンケートの質問に回答すると、IterateはBraze内で `survey-question-response` という名前のカスタムイベントをトリガーします。カスタムイベントにより、任意の数やタイプのフォローアップキャンペーンをトリガーできます。

## ユーザー属性名をカスタマイズする {#customize-user-attribute-names}

デフォルトでは、質問に対して作成されるユーザー属性はプロンプトと同じです。
場合によっては、これをカスタマイズしたいこともあります。そのためには、**Create your Survey**ステップの**Customize user attribute names**ドロップダウンをクリックし、使用するカスタム名を入力します。