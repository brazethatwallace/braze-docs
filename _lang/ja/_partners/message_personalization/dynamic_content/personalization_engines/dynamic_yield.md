---
nav_title: Dynamic Yield
article_title: Dynamic Yield
description: "このリファレンス記事では、BrazeとDynamic Yieldのパートナーシップについて説明します。このパートナーシップにより、Dynamic Yieldのレコメンデーションおよびセグメンテーションエンジンを使用して、Brazeメッセージに埋め込むことができるエクスペリエンスブロックを作成できます。"
alias: /partners/dynamic_yield/
page_type: partner
search_tag: Partner

---

# Dynamic Yield

> Mastercardの子会社である[Dynamic Yield](https://www.dynamicyield.com/)は、パーソナライズされ、最適化され、同期されたデジタルカスタマーエクスペリエンスを提供できるよう、さまざまな業種の企業を支援しています。Dynamic Yieldの[Experience OS](http://www.dynamicyield.com/experience-os)により、マーケター、プロダクトマネージャー、開発者、デジタルチームは、コンテンツ、製品、オファーを各顧客にアルゴリズムでマッチングさせ、収益と顧客ロイヤルティの向上を加速させることができます。

_この統合はDynamic Yieldによって管理されています。_

## 統合について {#about-the-integration}

BrazeとDynamic Yieldのパートナーシップにより、Dynamic Yieldのレコメンデーションおよびセグメンテーションエンジンを使用して、Brazeメッセージに埋め込むことができるエクスペリエンスブロックを作成できます。エクスペリエンスブロックは以下で構成できます。
- **レコメンデーションブロック**: メールの開封時に反映されるユーザーのパーソナライズ済みコンテンツを提供するためのアルゴリズムとフィルタリングを設定します。
- **ダイナミックコンテンツブロック**: ユーザーごとに異なるプロモーションやメッセージをターゲットにします。ターゲティングは、アフィニティまたはオーディエンスのいずれかに基づいて行うことができます。Dynamic Yieldは、メールの開封時にどのパーソナライズ済みエクスペリエンスを提供するかを決定します。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Dynamic Yieldアカウント | このパートナーシップを利用するには、[Dynamic Yield](https://adm.dynamicyield.com/users/sign_in#/r/dashboard)アカウントが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

### ステップ1: エクスペリエンスブロックを作成する {#step-1-create-an-experience-block}

Dynamic Yieldでエクスペリエンスブロックを作成するには、**Email > Experience Emails > Create New** の順に選択します。

次に、**Create Experience Block** を選択して、Brazeメールテンプレートに埋め込むダイナミックコンテンツまたはレコメンデーションブロックをデザインします。<br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield7.png %})

### ステップ2: メッセージの下書きをする {#step-2-draft-your-messaging}

次の画像は、ビルダーでゼロから作成するメールを示しています。<br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield5.png %})

1. 見出しエリアにキャンペーン名、メモ、キャンペーンのラベルを入力します。<br><br>
2. エクスペリエンスブロックを挿入します。エクスペリエンスブロックには、次のものがあります。
  - [レコメンデーション](#configure-a-recommendations-block): 完全にパーソナライズされたレコメンデーションをユーザーに提供するウィジェット。
  - [ダイナミックコンテンツ](#configure-a-dynamic-content-block): さまざまなプロモーションやメッセージを、さまざまなオーディエンスに向けて発信します。<br><br>
3. 設定を更新します:
  - URLパラメータを使用して、分析ソフトウェアでクリックを追跡します（オプション）。必要に応じて、デフォルトの表示にパラメータを追加します。
  - 属性の時間枠として7日間（デフォルト）または1日を選択します。<br><br>
4. 保存して終了します。コードが生成される前であればいつでも、メールのすべての要素を編集できます。コードが生成された後は、[コードに影響を与えない](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZPXB6MH094J1MWS5N86FXH)ものであれば何でも編集できます。

### レコメンデーションブロックを設定する {#configure-a-recommendations-block}

レコメンデーションブロックでは、メールの開封時に反映されるユーザーのパーソナライズ済みコンテンツを提供するためのアルゴリズムとフィルタリングを設定できます。

1. 編集ペインからレコメンデーションブロックをメール本文にドラッグします。<br><br>
2. 希望するアルゴリズム（人気度、ユーザーアフィニティ、類似度など）を選択します。選択されたアルゴリズムに応じて、追加のオプションが表示されます。
  - レコメンデーションが人気度に基づいている場合、閲覧者が開いた異なるメールから同じレコメンデーションが提供されるのを避けるために、結果をシャッフルすることができます。
  - 類似度のような他のアルゴリズムは、コンテキストに依存してレコメンデーションを提供するため、含めるアイテムを選択する必要があります。これらのアイテムはビルダーで追加するか、[埋め込みコードにマージタグを追加して](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#advanced)ダイナミックにすることもできます。たとえば、類似するアイテムを配送確認メールに追加する場合などです。<br><br>
3. ユーザーがすでに購入している製品を除外して、これらの製品をレコメンドしないようにできます。<br><br>
4. [カスタムフィルタールール](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZP4ZWZX1JJ2SH61MB3HVXD)を追加して、特定の製品をスロットに固定したり、製品プロパティに基づいて製品を含めたり除外したりすることができます。たとえば、5ドル未満の製品は表示しない、またはショートパンツカテゴリーの製品だけを表示するなどです。<br><br>
5. 最後に、レコメンデーションブロックのデザインを設定します。これを行うには、アイテムテンプレートを選択し、表示するアイテムの数と行数を設定します。

### ダイナミックコンテンツブロックを設定する {#configure-a-dynamic-content-block}
ダイナミックコンテンツを使用して、ユーザーごとに異なるプロモーションやメッセージをターゲットにします。ターゲティングは、アフィニティまたはオーディエンスのいずれかに基づいて行うことができます。Dynamic Yieldは、メールの開封時にどのパーソナライズ済みエクスペリエンスを提供するかを決定します。

1. ダイナミックコンテンツブロックを編集ペインからメール本文にドラッグします。<br><br>
2. 最初のバリエーションのテンプレートを選択します。デザイン変数とコンテンツ変数を定義できるようになります。完了したらバリエーションを保存します。<br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield3.png %})<br><br>
3. ダイナミックコンテンツペインでオーディエンスを設定します。<br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield4.png %})<br><br>
4. 別のバリエーションを追加して、別の特定のオーディエンスやすべてのユーザーをターゲットにします。必要に応じて繰り返します。<br><br>
5. 上下の矢印を使って、バリエーションの優先順位を設定します。<br><br>
6. 優先順位により、ユーザーが複数のエクスペリエンスの対象である場合に、どのバリエーションを提供するかが決定されます。

### ステップ3: メールをBrazeと統合する {#step-3-integrate-your-email-with-braze}

この統合により、パーソナライズされたレコメンデーションウィジェットとDynamic Yieldを利用したダイナミックコンテンツをBrazeのメールキャンペーンに追加できます。これらのキャンペーンをBrazeのキャンペーンに埋め込むには、Brazeのメールエディターに貼り付ける簡単な埋め込みコードを使用します。

1. エクスペリエンスメールの一覧ページで、ESP統合アイコンをクリックします。<br><br>
2. ユーザーのCUIDとメールIDを挿入するBrazeの関連トークンを入力します。<br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield2_new.png %})

メールに満足したら、次にBrazeに埋め込むコードを生成します。
1. **Experience Emails** で **Generate Code** をクリックします。<br><br>
2. 次に、**Copy to Clipboard** をクリックします。<br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield.png %})<br><br>
3. コードをBrazeのメールキャンペーンに貼り付け、メールキャンペーンのデザイン、テスト、公開を続けます。