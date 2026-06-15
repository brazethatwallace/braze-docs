---
nav_title: Anthropic
article_title: Anthropic
description: "このリファレンス記事では、BrazeとAnthropicのパートナーシップについて説明しています。このパートナーシップにより、ClaudeモデルをBrazeに接続してカスタムAIエージェントで使用できます。"
alias: /partners/anthropic/
page_type: partner
search_tag: Partner

---

# Anthropic

> [Anthropic](https://www.anthropic.com/)は、AIの安全性と研究に取り組む会社で、幅広い言語タスクに対して有用で、正直で、安全な次世代AIアシスタントであるClaudeを開発しています。

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

_この統合はAnthropicによって管理されています。_

## 統合について {#about-the-integration}

BrazeとAnthropicの統合により、Anthropic APIキーをBrazeに接続して、カスタムAIエージェントを構築する際にClaudeモデルを使用できます。この統合により、エージェントはパーソナライズ済みのコピーを生成したり、リアルタイムで意思決定を行ったり、AnthropicのClaudeモデルを使用してカタログフィールドを更新したりできます。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| APIキーを持つAnthropicアカウント | APIキーを持つAnthropicアカウントが必要です。ヘルプについては、管理者または[Anthropicサポート](https://support.anthropic.com/)にお問い合わせください。 |
| Brazeインスタンス | Brazeインスタンスは、[API概要ページ]({{site.baseurl}}/api/basics/#endpoints)またはBrazeオンボーディングマネージャーから確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

Anthropic APIキーをBrazeに接続するには、以下の手順に従います。

1. Brazeダッシュボードで**パートナー連携** > **テクノロジーパートナー**に移動し、Anthropicを見つけます。
2. AnthropicのAPIキーを入力します。
3. **保存**を選択します。

保存後、エージェントコンソールで[カスタムエージェントを作成する]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)際にClaudeモデルを選択できます。

統合に関する問題や質問がある場合は、[Anthropicサポート](https://support.anthropic.com/)にお問い合わせください。