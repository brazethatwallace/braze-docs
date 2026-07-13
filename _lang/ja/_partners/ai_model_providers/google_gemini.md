---
nav_title: Google Gemini
article_title: Google Gemini
description: "この参照記事では、BrazeとGoogle Geminiのパートナーシップについて概説しています。GeminiモデルをBrazeに接続し、カスタムAIエージェントで使用できます。"
alias: /partners/gemini/
page_type: partner
search_tag: Partner

---

# Google Gemini

> [Google Gemini](https://deepmind.google/technologies/gemini/)は、GoogleのAIモデルファミリーで、テキスト、コード、画像にわたる高度な推論を組み合わせ、ブランドがよりスマートでパーソナライズされた体験を提供できるよう支援します。

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

_この連携はGoogleによって管理されています。_

## 連携について {#about-the-integration}

BrazeとGoogle Geminiの連携により、APIキーまたはGoogleアカウントでのサインインを使用してGeminiをBrazeに接続し、カスタムAIエージェントを構築する際にGeminiモデルを使用できます。この連携により、エージェントはパーソナライズされたコピーを生成し、リアルタイムで意思決定を行い、GoogleのGeminiモデルを使用してカタログフィールドを更新できます。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| Google Cloudアカウント | Gemini APIにアクセスできるGoogle Cloudアカウントが必要です。APIキーを使用するか、Googleアカウントに接続してBrazeダッシュボードでGCPプロジェクトを選択することで認証できます。ヘルプについては、管理者または[Google Cloudサポート](https://cloud.google.com/support)にお問い合わせください。 |
| Brazeインスタンス | Brazeインスタンスは、[API概要ページ]({{site.baseurl}}/api/basics#endpoints)またはBrazeオンボーディングマネージャーから確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携 {#integration}

Google GeminiをBrazeに接続するには、以下の手順に従います。

1. Brazeダッシュボードで**パートナー連携** > **テクノロジーパートナー**に移動し、Google Geminiを見つけます。
2. **Authentication Method**で、**API Key**または**Connect Google Account**を選択します。
3. 選択した方法に応じて設定を完了します。
   - **API Key：** **API Type**で、**Gemini API**または**Gemini Enterprise Agent Platform（旧Vertex AI）**を選択します。APIキーを入力します。Gemini Enterprise Agent Platformを選択した場合は、**Project ID**も入力します。**Save**を選択します。
   - **Connect Google Account：** **Connect Google Account**を選択し、次に**Connect Google**を選択してGoogleアカウントでサインインします。ドロップダウンから**GCP Project**を選択します。そのプロジェクトでGemini APIとGemini Enterprise Agent Platformの両方が有効になっている場合は、Brazeが使用する**API Type**を選択します。**Save**を選択します。

{% alert note %}
**Connect Google Account**は、この認証オプションが有効になっているワークスペースでのみ表示されます。
{% endalert %}

保存後、エージェントコンソールで[カスタムエージェントを作成する]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)際にGeminiモデルを選択できます。

連携に関する問題や質問がある場合は、[Google Cloudサポート](https://cloud.google.com/support)にお問い合わせください。