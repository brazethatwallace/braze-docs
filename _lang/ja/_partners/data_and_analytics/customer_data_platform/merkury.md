---
nav_title: Merkury
article_title: Merkury
description: "このリファレンス記事では、BrazeとアプリのエンタープライズIDプラットフォームであるMerkuryとのパートナーシップについて説明します。`MerkuryID`を活用してBrazeの顧客のサイト訪問者認識率を向上させることができます。"
page_type: partner
search_tag: Partner

---

# Merkury

> [Merkury](https://merkury.merkleinc.com/)は、Merkleのエンタープライズアイデンティティプラットフォームです。ファーストパーティCookieレスアイデンティティ機能により、ブランドが消費者とのエンゲージメント、エクスペリエンス、収益を最大化できるように支援します。`MerkuryID`は、ブランドの既知および未知の顧客と見込み客のレコード、サイトやアプリの訪問履歴、および消費者データを、1つの永続的な個人IDに統合します。

_この統合はMerkuryによって管理されています。_

## 統合について {#about-the-integration}

BrazeとMerkuryの統合により、`MerkuryID`を活用してBrazeの顧客のサイト訪問者認識率を向上させることができます。ブランドのメール購読者である訪問者を認識すると、Merkuryはサブスクライバーのメールアドレスを含むようにBrazeプロファイルを更新します。`MerkuryID`の認識機能の向上により、エンゲージメントとパーソナライゼーションの機会が拡大し、送信されるサイト放棄メールの量と関連収益がすぐに増加します。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| --- | --- |
| Merkleアカウント | このパートナーシップを活用するには、Merkleアカウントが必要です。 |
| MerkleクライアントID | Merkleの担当者からクライアントIDを取得します。 |
| Merkuryタグ | MerkleのMerkuryタグをWebサイトに配置します。 |
| Braze RESTおよびSDKエンドポイント | RESTまたはSDKエンドポイントのURL。エンドポイントはインスタンスの[Braze URL]({{site.baseurl}}/api/basics/#endpoints)に応じて異なります。 |
| Braze REST APIキー | `users.track, users.export.ids, users.export.segment, and segments.list`の権限を持つBraze REST APIキー。<br><br>これは**Brazeダッシュボード > 開発者コンソール > REST APIキー > 新しいAPIキーを作成**で作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

{% alert important %}
BrazeへのMerkuryアイデンティティコネクターのリクエストは、Braze APIレート制限仕様の範囲内で動作します。ご質問がある場合は、BrazeまたはMerkleアカウントマネージャーにお問い合わせください。<br><br>Merkuryは、条件を満たしたセッションの最後に少なくとも1つのリクエストを送信します。
{% endalert %}

## サイドバイサイドのSDK統合 {#side-by-side-sdk-integration}

MerkleのクライアントサイドMerkuryタグを使用してBrazeデバイスをキャプチャし、識別のためにMerkuryアイデンティティコネクターエンドポイントに転送します。

### ステップ1:Braze Web SDKタグを設定する {#step-1-setup-braze-web-sdk-tag}

この統合を使用するには、Webサイトに[Braze Web SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#install-gtm)を導入している必要があります。

### ステップ2:MerkleのMerkuryタグを導入する {#step-2-deploy-merkles-merkury-tag}

WebサイトにMerkuryタグを配置して、MerkuryアイデンティティコネクターをWebサイトで利用できるようにします。Merkleアカウントマネージャーから詳しい手順ガイドが提供されます。

### ステップ3:カスタム属性を作成する {#step-3-create-custom-attributes}

Merkuryアイデンティティコネクターは以下のフィールドに値を入力するため、Brazeで[カスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attributes)として作成する必要があります。

| 属性名 | データタイプ | 説明 |
| --- | --- | --- |
| `hmid` | 文字列 | MerkleのMerkury ID |
| `confidence_score` | 数値 | Merkuryがどの程度の信頼度で識別できたか（1～8、小さいほど良い） |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Step 3: Create custom attributes" }

### ステップ4:Merkleにユーザーメールユニバースを提供する {#step-4-provide-merkle-with-user-email-universe}

Merkleでは、許容されるメールユニバースのセグメンテーションエクスポートを推奨しています。これは、アクティブな許容ユーザーの日次エクスポートでフォローアップできます。

以下のフィールドは必須です：

- `braze_id`
- `external_id`
- メールアドレス

詳細については、Brazeの担当者にお問い合わせください。