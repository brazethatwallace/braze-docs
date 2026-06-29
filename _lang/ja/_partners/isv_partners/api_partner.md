---
nav_title: APIパートナー連携
alias: /api_partner_integration/
hidden: true
---

# APIパートナー連携 {#api-partner-integration}

> `User-エージェント` ヘッダーの構文など、パートナーAPI連携の要件について説明します。

{% alert important %}
以前は、パートナーがAPIリクエストのパートナーフィールドに自社名を追加する必要がありました。この形式は現在サポートされておらず、`User-エージェント` ヘッダーが必須となっています。
{% endalert %}

## ユーザーエージェント {#user-agents}

トラフィックのソースを明確に識別する `User-エージェント` ヘッダーを含める必要があります。これにより、共有顧客はBrazeのAPI使用状況レポートでパートナーのトラフィックを確認でき、Brazeのエンジニアはベストプラクティスに従っていない連携を特定できます。一般的に、すべてのトラフィックに対して単一のユーザーエージェントのみを使用してください。

### 構文 {#syntax}

`User-エージェント` ヘッダーは以下の形式（[RFC 7231](https://datatracker.ietf.org/doc/html/rfc7231#page-46) 標準と同様）に従う必要があります。

```bash
User-Agent: partner-OrganizationName
```

以下を置き換えてください。

| プレースホルダー | 説明 |
|-------------|-------------|
| `OrganizationName` | Pascalケースでフォーマットされた組織名。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Syntax" }

### 例 {#examples}

たとえば、Snowflakeのクラウドデータ取り込みの場合、以下が正しいユーザーエージェントです。

`````````bash
User-Agent: partner-Snowflake
```

一方、以下はトラフィックのソースを明確に識別できないため、正しくありません。

`````````bash
User-Agent: axios/1.4.0
```
