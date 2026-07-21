---
nav_title: データを接続する
article_title: データを接続する
page_order: 1
description: "BrazeAI Decisioning Studio Goが、カスタマーエンゲージメントプラットフォームを通じて顧客データに接続する方法を学びます。"
---

# データを接続する {#connect-data-sources}

> BrazeAI Decisioning Studio™ Goは、カスタマーエンゲージメントプラットフォーム（CEP）を通じて顧客データに接続します。この記事では、どのようなデータが使用され、接続がどのように機能するかについて説明します。

## Goが顧客データにアクセスする方法 {#how-go-accesses-customer-data}

さまざまなソースとの直接的なデータ統合をサポートするDecisioning Studio Proとは異なり、Decisioning Studio GoはCEPを介して顧客データにアクセスします。これは以下を意味します：

- **オーディエンスデータ**は、CEP（BrazeまたはSalesforce Marketing Cloud）で定義されたセグメントまたはリストから直接取得され、特定の事前定義された属性のみを含めることができます（1Pデータは含まれません）
- **エンゲージメントデータ**（開封、クリック、送信）は、自動クエリまたはCEPとのネイティブ統合を通じて取得されます
- CEPで設定する内容以外に、**追加のデータパイプライン設定は不要**です

## サポートされている統合パターン {#supported-integration-patterns}

Decisioning Studio Goは、データアクセスにおいて以下のCEPをサポートしています：

| CEP | オーディエンスソース | エンゲージメントデータ |
|-----|-----------------|-----------------|
| **Braze** | セグメント | Braze Currentsエクスポート |
| **Salesforce Marketing Cloud** | データエクステンション | SQLクエリオートメーション |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="サポートされている統合パターン" }

## CEP別のデータ要件 {#data-requirements-by-cep}

{% tabs %}
{% tab Braze %}

### Brazeのデータ要件 {#braze-data-requirements}

Brazeとの統合において、Decisioning Studio Goには以下が必要です：

1. **Braze Currents：** Braze Currentsを有効にし、エンゲージメントデータをDecisioning Studio Goにエクスポートするよう設定する必要があります。これにより、エージェントは顧客の反応から学習できるようになります。

2. **セグメントアクセス：** 作成するAPIキーには、ターゲットオーディエンスを定義するセグメントにアクセスする権限が必要です。

3. **ユーザープロファイルデータ：** エージェントに考慮させたいユーザープロファイル属性やカスタム属性は、すべてBraze APIを通じてアクセス可能である必要があります。

{% alert important %}
比較対象とするキャンペーン（通常運用のキャンペーンを含む）のデータが、Braze Currentsのエクスポートに含まれていることを確認してください。
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

### SFMCのデータ要件 {#sfmc-data-requirements}

Salesforce Marketing Cloudとの統合において、Decisioning Studio Goには以下が必要です：

1. **データエクステンション：** オーディエンスは、Decisioning Studio Goがアクセス可能なデータエクステンションで定義されている必要があります。SubscriberKeyをプライマリユーザー識別子として使用してください。
2. **トラッキングイベントへのアクセス：** インストール済みアプリパッケージがエンドツーエンドの自動設定をサポートしている限り、追加の設定は不要です。

データエクステンションとSQLクエリは、[Decisioning Studio Goエージェントの設定]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup)の一部として構成されます。

{% endtab %}
{% endtabs %}

## ベストプラクティス {#best-practices}

- **データを最新の状態に保つ：** オーディエンスのセグメントと顧客データを定期的に（最低でも毎日）更新し、エージェントが常に最新の情報で動作できるようにしてください。
- **関連する属性を含める：** どの顧客特性がメッセージの効果に影響を与えるかを考えてみてください。デモグラフィック、エンゲージメント履歴、購買行動、ライフサイクルステージはすべて貴重なシグナルです。

## 次のステップ {#next-steps}

Goがデータに接続する仕組みを理解したところで、Brazeダッシュボードでエージェントを設定しましょう：

- [Decisioning Studio Goエージェントを設定する]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup)