---
nav_title: Merkury
article_title: Merkury
description: "このリファレンス記事では、BrazeとアプリのエンタープライズIDプラットフォームであるMerkuryとのパートナーシップについて説明します。`MerkuryID`を活用してBrazeの顧客のサイト訪問者認識率を向上させることができます。"
page_type: partner
search_tag: Partner
---

# Merkury

> [Merkury](https://merkury.merkleinc.com/)は、MerkleのエンタープライズIDプラットフォームです。ファーストパーティのCookieレスID機能により、ブランドが消費者とのエンゲージメント、エクスペリエンス、収益を最大化できるよう支援します。`MerkuryID`は、ブランドの既知および未知の顧客・見込み客のレコード、サイトやアプリの訪問履歴、および消費者データを、1つの永続的な個人IDに統合します。

_この統合はMerkuryによって管理されています。_

## 統合について {#about-the-integration}

BrazeとMerkuryの統合により、`MerkuryID`を活用してBraze顧客のサイト訪問者認識率を向上させることができます。ブランドのメール購読者である訪問者を認識すると、MerkuryはBrazeプロファイルを更新し、購読者のメールアドレスを追加します。`MerkuryID`の認識機能の向上により、エンゲージメントとパーソナライゼーションの機会が広がり、サイト離脱メールの送信数と関連する収益が即座に増加します。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| --- | --- |
| Merkleアカウント | このパートナーシップを利用するには、Merkleアカウントが必要です。 |
| MerkleクライアントID | Merkleの担当者からクライアントIDを取得してください。 |
| Merkuryタグ | MerkleのMerkuryタグをWebサイトに設置してください。 |
| Braze REST APIおよびSDKエンドポイント | RESTまたはSDKエンドポイントのURL。エンドポイントは[お使いのインスタンスのBraze URL]({{site.baseurl}}/api/basics#endpoints)によって異なります。 |
| Braze REST APIキー | `users.track, users.export.ids, users.export.segment, and segments.list` の権限を持つBraze REST APIキー。<br><br>これは、**Brazeダッシュボード > 開発者コンソール > REST APIキー > 新しいAPIキーを作成**から作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

{% alert important %}
BrazeへのMerkury IDコネクタリクエストは、BrazeのAPIレート制限仕様の範囲内で動作します。ご質問がある場合は、Brazeまたは担当のMerkleアカウントマネージャーにお問い合わせください。<br><br>Merkuryは、認定されたセッションの終了時に少なくとも1つのリクエストを送信します。
{% endalert %}

## サイドバイサイドSDK連携 {#side-by-side-sdk-integration}

MerkleのクライアントサイドMerkuryタグを使用してBrazeデバイスをキャプチャし、識別のためにMerkury IDコネクターエンドポイントに転送します。

### ステップ1：Braze Web SDKタグの設定 {#step-1-setup-braze-web-sdk-tag}

この連携を使用するには、Webサイトに[Braze Web SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-gtm)がデプロイされている必要があります。

### ステップ2：MerkleのMerkuryタグをデプロイする {#step-2-deploy-merkles-merkury-tag}

WebサイトにMerkuryタグをデプロイして、Merkury IDコネクターをWebサイトで利用できるようにします。Merkleのアカウントマネージャーが詳細な手順ガイドを提供します。

### ステップ3：カスタム属性を作成する {#step-3-create-custom-attributes}

Merkury IDコネクターは以下のフィールドを設定します。これらをBrazeで[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)として作成する必要があります。

| 属性名 | データ型 | 説明 |
| --- | --- | --- |
| `hmid` | String | MerkleのMerkury ID |
| `confidence_score` | Number | Merkuryが識別できた確信度（1〜8、低いほど良い） |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ3：カスタム属性を作成する" }

### ステップ4：Merkleにユーザーのメールユニバースを提供する {#step-4-provide-merkle-with-user-email-universe}

Merkleは、許可されたメールユニバースのセグメンテーションエクスポートを推奨しています。その後、許可されたアクティブユーザーの日次エクスポートを行うこともできます。

以下のフィールドが必須です：

- `braze_id`
- `external_id`
- メールアドレス

詳細については、Brazeの担当者にお問い合わせください。