---
nav_title: Dynamic Yield
article_title: Dynamic Yield
description: "このリファレンス記事では、BrazeとDynamic Yieldのパートナーシップについて説明します。このパートナーシップにより、Dynamic Yieldのレコメンデーションおよびセグメンテーションエンジンを使用して、Brazeメッセージに埋め込むことができるエクスペリエンスブロックを作成できます。"
alias: /partners/dynamic_yield/
page_type: partner
search_tag: Partner

---

# Dynamic Yield

> Mastercardの子会社である[Dynamic Yield](https://www.dynamicyield.com/)は、パーソナライズされ、最適化され、同期されたデジタル顧客体験を提供できるよう、さまざまな業種の企業を支援しています。Dynamic Yieldの[Experience OS](http://www.dynamicyield.com/experience-os)により、マーケター、プロダクトマネージャー、開発者、デジタルチームは、コンテンツ、製品、オファーを各顧客にアルゴリズムでマッチングさせ、収益と顧客ロイヤルティの向上を加速させることができます。

_この統合はDynamic Yieldによって管理されています。_

## 統合について {#about-the-integration}

BrazeとDynamic Yieldのパートナーシップにより、Dynamic Yieldのレコメンデーションおよびセグメンテーションエンジンを使用して、Brazeメッセージに埋め込むことができるエクスペリエンスブロックを作成できます。エクスペリエンスブロックは以下で構成できます:
{% multi_lang_include partners/message_personalization/dynamic_yield_experience_blocks.md %}

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| ----------- | ----------- |
| Dynamic Yieldアカウント | このパートナーシップを利用するには、[Dynamic Yield](https://adm.dynamicyield.com/users/sign_in#/r/dashboard)アカウントが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携 {#integration}

### ステップ1：エクスペリエンスブロックを作成する {#step-1-create-an-experience-block}

Dynamic Yieldでエクスペリエンスブロックを作成するには、**Email > Experience Emails > Create New** に移動します。

次に、**Create Experience Block** を選択して、Brazeメールテンプレートに埋め込むダイナミックコンテンツまたはレコメンデーションブロックを設計します。<br>![「Create Experience Block」が選択されたDynamic Yieldのエクスペリエンスメールページ。]({% image_buster /assets/img/dynamic_yield/dynamic_yield7.png %})

### ステップ2：メッセージングの下書きを作成する {#step-2-draft-your-messaging}

以下の画像は、ビルダーでゼロから作成したメールを示しています。<br>![下書きのエクスペリエンスメールレイアウトが表示されたDynamic Yieldメールビルダー。]({% image_buster /assets/img/dynamic_yield/dynamic_yield5.png %})

1. ヘッダーエリアにキャンペーン名、メモ、キャンペーンのラベルを入力します。<br><br>
2. エクスペリエンスブロックを挿入します。これらのブロックには以下が含まれます：
  - [レコメンデーション](#configure-a-recommendations-block)：完全にパーソナライズされたレコメンデーションをユーザーに提供するウィジェットです。
  - [ダイナミックコンテンツ](#configure-a-dynamic-content-block)：異なるオーディエンスに異なるプロモーションやメッセージをターゲティングします。<br><br>
3. 設定を更新します：
  - 分析ソフトウェアでクリックを追跡するためにURLパラメーターを使用します（オプション）。必要に応じてデフォルト表示にパラメーターを追加します。
  - 属性ウィンドウを7日間（デフォルト）または1日間のいずれかで選択します。<br><br>
4. 保存して終了します。コードが生成される前であれば、いつでもメールのすべての要素を編集できます。コードが生成された後は、[コードに影響しない要素](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZPXB6MH094J1MWS5N86FXH)のみ編集できます。

### レコメンデーションブロックを設定する {#configure-a-recommendations-block}

レコメンデーションブロックを使用すると、アルゴリズムとフィルタリングを設定して、メールが開封されたときに表示されるユーザーのパーソナライズされたコンテンツをソースできます。

1. 編集ペインからレコメンデーションブロックをメール本文にドラッグします。<br><br>
2. 希望するアルゴリズム（人気度、ユーザーアフィニティ、類似性など）を選択します。選択したアルゴリズムに応じて、追加オプションが表示されます：
  - レコメンデーションが人気度に基づいている場合、閲覧者が開封する異なるメールから同じレコメンデーションが配信されるのを避けるために、結果をシャッフルできます。
  - 類似性などの他のアルゴリズムは、レコメンデーションを配信するためにコンテキストに依存し、含めるアイテムを選択する必要があります。これらのアイテムはビルダーで追加するか、[埋め込みコードにマージタグを追加](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#advanced)してダイナミックにすることができます。たとえば、出荷確認メールに類似アイテムを追加できます。<br><br>
3. ユーザーがすでに購入した商品を除外して、それらの商品をレコメンドしないようにできます。<br><br>
4. [カスタムフィルタールール](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZP4ZWZX1JJ2SH61MB3HVXD)を追加して、特定の商品をスロットに固定したり、商品プロパティで商品を含めたり除外したりできます。たとえば、5ドル未満の商品を表示しない、またはショーツカテゴリの商品のみを表示するなどです。<br><br>
5. 最後に、レコメンデーションブロックのデザインを設定します。これを行うには、アイテムテンプレートを選択し、表示するアイテム数と行数を設定します。

### ダイナミックコンテンツブロックを設定する {#configure-a-dynamic-content-block}
ダイナミックコンテンツを使用して、異なるユーザーに異なるプロモーションやメッセージをターゲティングします。ターゲティングはアフィニティまたはオーディエンスのいずれかに基づくことができます。Dynamic Yieldは、メールが開封されたときにどのパーソナライズされたエクスペリエンスを配信するかを決定します。

1. 編集ペインからダイナミックコンテンツブロックをメール本文にドラッグします。<br><br>
2. 最初のバリエーションのテンプレートを選択します。デザインとコンテンツの変数を定義できます。完了したらバリエーションを保存します。<br>![Dynamic Yieldのダイナミックコンテンツバリエーションテンプレートエディター。]({% image_buster /assets/img/dynamic_yield/dynamic_yield3.png %})<br><br>
3. ダイナミックコンテンツペインでオーディエンスを設定します。<br>![ダイナミックコンテンツバリエーションのDynamic Yieldオーディエンスターゲティング設定。]({% image_buster /assets/img/dynamic_yield/dynamic_yield4.png %})<br><br>
4. 別の特定のオーディエンスまたはすべてのユーザーをターゲットにする別のバリエーションを追加します。必要に応じて繰り返します。<br><br>
5. 上下の矢印を使用してバリエーションの優先順位を設定します。<br><br>
6. 優先順位は、ユーザーが複数のエクスペリエンスの対象となる場合に、どのバリエーションが配信されるかを決定します。

### ステップ3：メールをBrazeと連携する {#step-3-integrate-your-email-with-braze}

この連携により、Dynamic Yieldを活用したパーソナライズされたレコメンデーションウィジェットやダイナミックコンテンツを、Brazeのメールキャンペーンに追加できます。これらのキャンペーンをBrazeキャンペーンに埋め込むには、Brazeメールエディターに貼り付けるシンプルな埋め込みコードを使用します。

1. エクスペリエンスメールリストページでESP連携アイコンをクリックします。<br><br>
2. ユーザーのCUIDとメールIDを挿入するBrazeの関連トークンを入力します。<br>![Brazeユーザートークンフィールドが表示されたDynamic YieldのESP連携モーダル。]({% image_buster /assets/img/dynamic_yield/dynamic_yield2_new.png %})

メールに満足したら、次のステップはBrazeに埋め込むコードを生成することです。
1. **Experience Emails** で、**Generate Code** をクリックします。<br><br>
2. 次に、**Copy to Clipboard** をクリックします。<br>![「Copy to Clipboard」アクションが表示されたDynamic Yieldの生成された埋め込みコードパネル。]({% image_buster /assets/img/dynamic_yield/dynamic_yield.png %})<br><br>
3. コードをBrazeのメールキャンペーンに貼り付け、メールキャンペーンのデザイン、テスト、公開を続行します。