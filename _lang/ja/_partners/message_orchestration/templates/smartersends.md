---
nav_title: SmarterSends
article_title: SmarterSends
description: "このリファレンス記事では、BrazeとSmarterSendsのパートナーシップについて説明します。SmarterSendsは、マーケター以外のユーザーでもブランドに準拠したメールキャンペーンを作成、スケジュール、展開できるように設計された使いやすいインターフェイスです。"
alias: /partners/smartersends/
page_type: partner
search_tag: Partner
---

# SmarterSends

> [SmarterSends](https://smartersends.com)は、企業が作成、スケジュール、展開できるマーケティングキャンペーンでパーソナライゼーションを推進し、使用するコンテンツやデータをコントロールしながら、ブランドおよび法的コンプライアンスを強化します。

_この統合はSmarterSendsによって管理されています。_

## 統合について {#about-the-integration}

BrazeとSmarterSendsのパートナーシップにより、Brazeの機能と、分散ユーザーが所有するハイパーローカライズされたコンテンツを組み合わせて、マーケティングキャンペーンを強化できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| --- | --- |
| SmarterSendsアカウント | このパートナーシップを活用するには、[SmarterSendsアカウント](https://smartersends.com)が必要です。 |
| Braze REST APIキー | 以下の権限を持つBraze REST APIキー: {::nomarkdown}<ul><li><code>users.track</code></li><li><code>users.export.ids</code></li><li><code>messages.schedule.create</code></li><li><code>messages.schedule.update</code></li> <li><code>messages.schedule.delete</code></li><li><code>sends.id.create</code></li><li><code>segments.list</code></li><li><code>segments.data_series</code></li><li><code>segments.details</code></li><li><code>sends.data_series</code></li></ul>{:/} これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。セキュリティを強化するために、SmarterSendsのIPアドレス（インスタンスで確認可能）を許可リストに追加してください。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、インスタンスのBraze URLに依存します。 |
| Braze APIキャンペーンID | [Braze APIキャンペーンID]({{site.baseurl}}/api/api_campaigns/)は、SmarterSendsを介して送信されるすべてのキャンペーンの一意の識別子です。これはBrazeダッシュボードの**Messaging** > **キャンペーン**で作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}

BrazeとSmarterSendsの統合により、複数のチャネルやロケーションにまたがるマーケティングキャンペーンを作成・実行することで、分散型マーケティングを活用できます。これには次のようなメリットがあります。

1. **リーチの拡大:** 複数のチャネルやロケーションを利用して、より幅広いオーディエンスにリーチし、さまざまな場所にいる顧客をターゲットにすることで、ブランドの露出を増やします。
2. **ターゲットを絞ったメッセージング:** 顧客とのより効果的なコミュニケーションとエンゲージメントを実現するため、地域のオーディエンスに響くよう、チャネルやロケーションを超えてメッセージングを調整します。
3. **ブランドの一貫性の向上:** ブランドのメッセージとイメージをすべてのチャネルとロケーションで統一します。これは、強力で認識しやすいブランドを構築するうえで重要です。
4. **より優れたインサイト:** さまざまなチャネルやロケーションからデータを収集し、顧客の行動や嗜好に関する貴重なインサイトを提供します。このインサイトは、ローカルレベルとグローバルレベルの両方でマーケティング戦略や戦術を洗練させるために活用できます。
5. **効率性の向上:** 異なるチャネルやロケーションの強みを活用することで、マーケティング目標を達成しながら、リソースをより効率的に活用できます。

## 統合 {#integration}

### ステップ1:REST APIキーを作成する {#step-1-create-a-rest-api-key}

1. Brazeで、**設定** > **APIキー**に移動し、**新規APIキーを作成**をクリックします。
2. APIキーの名前を入力します。
3. SmarterSendsがBrazeワークスペースとやり取りできるように、このキーに以下の権限を選択します。
- `users.track`
- `users.export.ids`
- `messages.schedule.create`
- `messages.schedule.update`
- `messages.schedule.delete`
- `sends.id.create`
- `segments.list`
- `segments.data_series`
- `segments.details`
- `sends.data_series`
4. SmarterSendsのIPアドレスを**Whitelist IPs**セクションに追加します。
5. **Save API Key**をクリックします。
6. 適切な権限を持つAPIキーをコピーして、SmarterSendsの**Braze Email Service Provider**設定に貼り付けます。

### ステップ2:アプリケーションIDを作成またはコピーする {#step-2-create-or-copy-an-application-id}

1. Brazeワークスペースで、**設定** > **アプリ設定**に移動します。
2. 新しいアプリをセットアップするか、ワークスペース内の既存のアプリケーションのアプリケーションIDを使用します。アプリケーションIDには**API Key**というラベルが付いていることに注意してください。
3. このIDをコピーしてSmarterSendsの**App ID**フィールドに貼り付けます。

### ステップ3:APIキャンペーンを作成する {#step-3-create-an-api-campaign}

APIキャンペーンにより、Braze内のすべてのSmarterSendsメールの指標をトラッキングし、SmarterSendsがこれらのAPIベースのキャンペーンをトリガーできるようになります。

1. Brazeで[APIキャンペーンを作成]({{site.baseurl}}/api/api_campaigns/#create-a-new-campaign)します。
2. **Select Message Channel**の下にある**Email**をクリックし、指標のトラッキングを開始するメッセージングチャネルを追加します。
3. 次に、BrazeのキャンペーンIDをコピーしてSmarterSendsの**キャンペーン ID**フィールドに貼り付けます。
4. BrazeのメッセージバリアントIDをコピーしてSmarterSendsの**Message Variant ID**フィールドに貼り付けます。SmarterSendsでグループごとにメッセージIDを作成しない場合、これがデフォルトのメッセージIDとして使用されます。
5. SmarterSendsで作成したグループごとに、BrazeのAPIキャンペーンにメッセージバリアントを追加します。次に、メッセージバリアントIDをSmarterSendsのグループのメッセージバリアントIDにコピーします。

{% alert tip %}
SmarterSendsで作成したグループごとにメッセージバリアントIDを作成すると、Brazeワークスペースで各グループの送信指標を個別に表示できます。これは、Brazeでレポートを作成する際に、グループ間の傾向を特定するのに役立ちます。
{% endalert %}

## カスタマイズ {#customization}

SmarterSendsの各インスタンスは、ブランドのロゴカラーやカスタムドメイン名で完全にカスタマイズ可能で、親しみやすい環境を作ることができます。さらに、パーソナライゼーションを進めるために、Brazeワークスペース内のセグメントに基づいて、キャンペーンでユーザーをターゲットにする属性やカスタム属性を定義できます。