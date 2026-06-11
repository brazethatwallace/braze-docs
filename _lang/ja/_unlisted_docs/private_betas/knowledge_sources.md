---
nav_title: ナレッジソース
article_title: ナレッジソース
permalink: "/knowledge_sources/"
description: "このリファレンス記事では、BrazeAIエージェント用のナレッジソースの作成と管理方法について説明します。"
page_type: reference
---

# ナレッジソース {#knowledge-sources}

> ナレッジソースは、AIエージェントがカタログデータを解釈し、目標を達成するために適切な情報を取得するのに役立ちます。

{% alert important %}
エージェントコンソールのナレッジソースは現在、早期アクセス段階です。この早期アクセスへの参加にご興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。
{% endalert %}

## 仕組み {#how-it-works}

ナレッジソースはエージェントコンテキストの一種です。AIエージェントは、カタログをエージェントの指示で直接参照する場合よりも、ナレッジソースを参照することでカタログからより正確にデータを取得できます。

たとえば、ユーザーのお気に入りの料理（カスタム属性）に基づいて、ニューヨーク市のレストランをおすすめするエージェントを構築するとします。このエージェントは「nyc_restaurants」カタログのナレッジソースを参照します。ナレッジソースを作成する際、エージェントが必要とするフィールド（レストラン名、ロケーション、料理の種類など）のみを含め、おすすめに関係のない他のカタログ列は除外します。

エージェントの指示には、その役割と制約が明確に記述されています：

{% raw %}
```
You are a restaurant recommendation agent. Use your knowledge to help find restaurants for the user. Only include filters in your knowledge source query. Don't ask any followup questions. The user's favorite cuisine is {{custom_attribute.${favorite_cuisine}}}
```
{% endraw %}

ユーザーのお気に入りの料理がピザの場合、エージェントはナレッジソースに基づいて次のような応答を返すことができます：

```
Here are some pizza recommendations for you:
- Dale's Pizza (Greenwich Village, Manhattan): Dale's Pizza invites you to savor the taste of authentic New York. Nestled in the heart of Manhattan, this iconic pizzeria offers a warm and inviting atmosphere perfect for any occasion.
- Pizza Palace (Carroll Gardens, Brooklyn): Pizza Palace is a highly-rated culinary gem renowned for its exquisite pizza. This inviting spot offers a warm and modern dining experience.
```

## ナレッジソースを作成する {#create-a-knowledge-source}

ナレッジソースを作成するには：

1. **エージェントコンソール** > **ナレッジソース**に移動します。
2. **ナレッジソースを追加**を選択します。ドロップダウンで**カタログ**を選択します。
3. ドロップダウンからカタログを選択します。
4. カタログフィールドを確認し、エージェントのユースケースに該当しないフィールドの選択を解除します。取得や生成に役立たないカタログフィールドは除外し、エージェントが必要とするフィールドのみにナレッジソースを限定することをお勧めします。
5. （オプション）ナレッジソースの内容を説明する説明を追加します。
6. **ナレッジソースを追加**を選択します。

すべてのカタログフィールドを含めると、不要なコンテキストが追加され、出力品質が低下する可能性があります。ユースケースに関連しないフィールドの選択を解除することで、エージェントが重要なデータに集中できるようになります。

![カタログ「nyc_restaurants」を参照するナレッジソース「nyc_restaurants」。]({% image_buster /assets/unlisted_docs/img/knowledge_sources/knowledge_source_example.png %}){: style="max-width:80%;"}

エージェントの構築中にナレッジソースを作成することもできます。エージェントの**指示**セクションに移動し、**ナレッジを追加** > **ナレッジソースを作成**を選択します。

## AIエージェントでナレッジソースを使用する {#use-a-knowledge-source-in-your-ai-agent}

ナレッジソースは**ナレッジソース**セクションから管理できます。ここでは、どのナレッジソースがアクティブか、最後に同期された日時などの詳細を確認できます。ナレッジソースの名前は、ソースとして使用されるカタログの名前と一致します。

AIエージェントでナレッジソースを使用するには：

1. エージェントの**指示**セクションに移動します。
2. **+ エージェントコンテキスト** > **ナレッジを追加**を選択します。
3. ドロップダウンからナレッジソースを選択します。

これで、エージェントはナレッジソースを参照し、関連するカタログデータを取得できるようになります。

## よくある質問 {#frequently-asked-questions}

### ナレッジソースはどのように機能しますか？ {#how-do-knowledge-sources-work}

カタログをナレッジソースに変換することで、Brazeエージェントがカタログ内の単語やフレーズの真の意味を理解できるようになり、エージェントがより効果的に意味のあるデータを見つけて、より良い出力を生成できるようになります。

### ナレッジソースはいつ作成すべきですか？ {#when-should-i-create-a-knowledge-source}

カタログをコンテキストとして使用できるカスタムエージェント（Canvasエージェントまたはカタログエージェント）を設定する場合に、ナレッジソースを作成します。ナレッジソースの使用は、既存の方法と比較して、カタログをコンテキストとして添付するより優れた方法です。

### エージェントにナレッジソースをコンテキストとして付与した場合、元のカタログもコンテキストとして割り当てる必要がありますか？ {#if-an-agent-has-been-given-a-knowledge-source-as-context-do-i-also-need-to-assign-the-original-catalog-as-context}

いいえ。ナレッジソースはエージェントコンテキストとしてカタログに置き換わるため、両方を添付する必要はありません。ナレッジソースを作成する際は、エージェントが必要とするカタログフィールドのみを含めてください。

### ナレッジソースの有効性をどのように評価すべきですか？ {#how-should-i-evaluate-the-efficacy-of-knowledge-source}

通常のカタログを参照している既存のエージェントを複製し、同等のナレッジソースを参照するように切り替えます。エージェントコンソールでいくつかのテスト呼び出しを実行して精度を確認し、その後、既存のエージェントがデプロイされている場所で置き換えるか、古いエージェントと新しいエージェントをABテスト（Experiment Pathステップを使用）してパフォーマンスへの影響を把握することを検討してください。