---
nav_title: OpenAI
article_title: OpenAI
description: "このリファレンス記事では、BrazeとOpenAIのパートナーシップについて説明しています。OpenAIモデルをBrazeに接続し、カスタムAIエージェントで使用できます。"
alias: /partners/openai/
page_type: partner
search_tag: Partner

---

# OpenAI

> [OpenAI](https://openai.com/)は、GPTのような高度なAIモデルを開発しており、自然言語の理解と生成を可能にすることで、ブランドが有意義な顧客インタラクションを構築・拡張できるようにしています。

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

_この連携はOpenAIによって管理されています。_

## 連携について {#about-the-integration}

BrazeとOpenAIの連携により、OpenAIのAPIキーをBrazeに接続して、カスタムAIエージェントを構築する際にOpenAIモデルを使用できます。この連携により、エージェントはパーソナライズ済みコピーの生成、リアルタイムの意思決定、OpenAIの大規模言語モデルを使用したカタログフィールドの更新が可能になります。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| APIキーを持つOpenAIアカウント | APIキーを持つOpenAIアカウントが必要です。問題や質問がある場合は、管理者または[OpenAIサポート](https://help.openai.com/)にお問い合わせください。 |
| Brazeインスタンス | Brazeインスタンスは、[API概要ページ]({{site.baseurl}}/api/basics/#endpoints)またはBrazeオンボーディングマネージャーから確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携 {#integration}

OpenAIのAPIキーをBrazeに接続するには：

1. Brazeダッシュボードで**パートナー連携** > **テクノロジーパートナー**に移動し、OpenAIを見つけます。
2. OpenAIのAPIキーを入力します。
3. **保存**を選択します。

保存後、エージェントコンソールで[カスタムエージェントを作成する]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)際にOpenAIモデルを選択できます。

連携に関する問題や質問がある場合は、[OpenAIサポート](https://help.openai.com/)にお問い合わせください。