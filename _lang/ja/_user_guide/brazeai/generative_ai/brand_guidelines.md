---
nav_title: ブランド・ガイドライン
article_title: AIが生成するブランド・ガイドライン
page_order: 2.2
description: "このリファレンス記事では、AIコピーライティングアシスタントのブランドガイドラインについて説明します。この機能を使用すると、AIコピーライティングアシスタントが生成するコピーのスタイルを、ブランドのボイスやスタイルに合わせて調整できます。"
---

# BrazeAIでブランド・ガイドラインを生成する {#generate-brand-guidelines-with-brazeai}

> カスタマイズされたブランドガイドラインで、AIが生成するコピーのスタイルをブランドのボイスやパーソナリティに合わせて調整できます。

## ブランドガイドラインの生成 {#steps}

AIコピーライティングアシスタントでブランドガイドラインを作成するには、次のステップに従います。[ブランド・ガイドライン]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/)の設定ページでブランドガイドラインを作成することもできます。

### ステップ1:ブランドガイドラインの作成 {#step-1-create-a-brand-guideline}

1. メッセージ作成画面で <i class="fa-solid fa-wand-magic-sparkles" title="AIコピーライター"></i> **AIコピーライター**を見つけて選択し、[AIコピーライティングアシスタントを開きます]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/#access)。
2. **Apply brand guideline**を選択し、次に**Create a brand guideline**を選択します。

![「Apply brand guidelines」のドロップダウンが展開され、「Create a brand guideline」ボタンがフォーカスされている状態。]({% image_buster /assets/img/ai_copywriter/create_brand_guideline_button.png %}){:style="max-width:75%"}

{: start="3"}

3. このガイドラインの名前を入力します。これは、前の選択画面で表示されるラベルになります。
4. **When will you use these brand guidelines?** には、同僚（そして将来のあなた）がこのガイドラインを使用するコンテキストを理解できるように詳細を追加します。
5. これを現在のワークスペースのデフォルトのブランドガイドラインにしたい場合は、**Use as default brand guideline**をチェックします。

![ブランドガイドライン作成画面。]({% image_buster /assets/img/ai_copywriter/manual_brand_guidelines.png %} "Brand Guidelines")

### ステップ2:ブランドのパーソナリティの説明 {#step-2-describe-your-brand-personality}

**Brand personality**では、自社ブランドをユニークなものにしている要素について考えます。自社ブランドを定義する特徴、価値観、ボイス、およびあらゆる原型を含めます。以下に、考慮すべきいくつかの特徴を示します。

| **特徴** | **定義** | **例** |
|--------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| レピュテーション | 自社ブランドが市場でどのように認知されたいか。 | 自社は業界で最も信頼性が高く、顧客重視のブランドとして知られています。 |
| パーソナリティの特徴 | 自社ブランドの特徴を表す、人間に例えた特徴。 | 自社ブランドはフレンドリーで親しみやすく、常に明るいです。 |
| 価値観 | 自社ブランドのアクションや意思決定の指針となるコアバリュー。 | 自社は、持続可能性、透明性、そしてコミュニティを大切にしています。 |
| 差別化 | 自社ブランドを競合他社から際立たせる独自の資質。 | 自社は、極上のパーソナライズされた顧客サービスを提供することで、傑出した存在になっています。 |
| ブランドボイス | 自社ブランドが使用するコミュニケーションのトーンとスタイル。 | 自社のボイスはカジュアルでありながら情報量が豊富で、堅苦しくならずに明確さを確保しています。 |
| ブランドアーキタイプ | 自社ブランドのペルソナを表すアーキタイプ（ヒーロー、クリエイターなど）。 | 自社は「探検家」のアーキタイプを体現し、常に新しい挑戦と冒険を求めています。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ2:ブランドのパーソナリティの説明" }

### ステップ3:避けるべき言葉の定義（オプション） {#step-3-define-language-that-should-be-avoided-optional}

**Exclusions**には、自社ブランドにふさわしくない言葉やスタイルを列挙します。例えば、「皮肉」「否定的な態度」「慇懃無礼」なトーンを避けたい場合に指定します。

### ステップ4:ガイドラインのテスト {#step-4-test-your-guidelines}

ガイドラインをテストして、そのパフォーマンスを確認します。**Test your guidelines**を展開し、コピー例を生成して、必要に応じて調整します。

![メール件名用の春のセールプロモーションでブランドガイドラインをテストしている様子。]({% image_buster /assets/img/ai_copywriter/test_brand_guidelines.png %})

### ステップ5:ガイドラインの保存 {#step-5-save-your-guidelines}

ガイドラインに満足したら、**Save brand guideline**を選択します。新しいガイドラインは、今後使用できるようにワークスペースに保存されます。

{% alert important %}
コピーの言語に関係なく出力言語を変更できますが、BrazeもOpenAIも翻訳の品質を保証しません。翻訳を使用する前に、必ずテストと検証を行ってください。
{% endalert %}

## 既存のガイドラインを編集する {#editing-existing-guidelines}

既存のブランドガイドラインを編集するには、次の手順に従います。

1. AIコピーライティングアシスタントを開きます。
2. 変更するブランドガイドラインを適用します。フィールドの近くにボタンが表示されます。
3. **Edit guideline**を選択します。

{% multi_lang_include brazeai/generative_ai/policy.md %}