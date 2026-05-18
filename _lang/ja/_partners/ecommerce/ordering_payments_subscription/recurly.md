---
nav_title: Recurly
article_title: Recurly
description: "Recurlyは、サブスクリプションと定期収益の拡大を目指すDirect-to-Consumerブランド向けの、業界をリードするサブスクリプション管理および請求プラットフォームです。"
alias: /partners/recurly/
page_type: partner
search_tag: partner
---

# Recurly

> [Recurly](https://recurly.com/)はサブスクリプション管理および請求プラットフォームです。Recurly統合プラットフォームは、サブスクリプションライフサイクルのオートメーションを大規模に簡素化し、チームがサブスクライバーの体験（新しいプラン、オファー、プロモーションのテストから、決済方法、統合、インサイトの管理まで）を管理および最適化できるようにします。

_この統合はRecurlyによって管理されています。_

## 統合について {#about-the-integration}

RecurlyとBrazeの統合により、サブスクリプションデータをBrazeと共有するプロセスが簡素化され、顧客とのターゲットを絞ったコミュニケーションが可能になります。

- BrazeでRecurlyのサブスクリプションライフサイクルイベント（サブスクリプションの更新、一時停止、キャンセルなど）を活用して、パーソナライズされたキャンペーンやコミュニケーションをトリガーします。
- Recurlyのサブスクリプションデータ（サブスクリプションプラン、アドオン、ステータスなど）を活用して、会社ユーザー、セグメント、キャンバスを作成・管理し、コホート固有のキャンペーンやコミュニケーションを実施します。
- RecurlyデータをBrazeに直接送信することで、追加のメッセージングユースケースを可能にし、開発のオーバーヘッドコストを削減します。

BrazeでのRecurlyの使用に関する詳細については、[Recurlyドキュメント](https://docs.recurly.com/docs/braze-integration)をご覧ください。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Recurlyアカウント | このパートナーシップを活用するには、Brazeフィーチャーフラグが有効になっているエリート[Recurly](https://recurly.com/)サブスクリプションプランが必要です。Recurlyプラットフォームでクレジット請求書の有効化も必要です。|
| Braze REST APIキー | `users.track`権限を持つBraze REST APIキー。<br><br>これは、Brazeダッシュボードの**設定** > **APIキー**で作成できます。Recurlyは`users.track`エンドポイントのみを使用するため、この権限のみを持つRecurly専用のキーをプロビジョニングすることを推奨します。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、インスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

開始する前に、BrazeとRecurlyの両方でアクティブなアカウントを持っていることを確認してください。

### RecurlyをBrazeに接続する {#connect-recurly-to-braze}

1. Recurlyで**Integrations** > **Braze**に移動します。RecurlyのBraze統合設定ページに初めてアクセスすると、インターフェイスが2つのシステムを接続するよう促します。

2. 以下の認証情報を入力します。

- **Instance URL:** プロビジョニングされたインスタンスのBraze RESTエンドポイント。
- **API Key (Identifier):** RecurlyがBrazeにリクエストを送信する際に使用するBraze REST APIキー。

BrazeインスタンスのURLをコピーすることを忘れないでください。例えば、URLは次のようになります：

```
<https://dashboard-03.braze.com/dashboard/app_usage?locale=en>
```

{:start="3"}
3. 認証情報を入力したら、**Connect**をクリックします。

## この統合を使用する {#using-this-integration}

### サポートされている識別子 {#supported-identifiers}

Recurlyはアカウントの`account_code`をBrazeの`external_id`として使用します。このため、Recurlyアカウントの`account_code`は、Brazeユーザーの`external_id`に対応している必要があります。

### カスタムイベント {#custom-events}

効果的なカスタマーエンゲージメントのために、Recurlyによってトリガーされるイベントを受信するためにBrazeで[カスタムイベントを設定]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)する必要があります。データ統合を徹底するために、Recurlyの各イベントを含めるようにしてください。これらのイベントは[Braze分析]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#analytics)内でも追跡できます。設定後、これらのカスタムイベントを使用してユーザーをセグメント化したり、メッセージングをパーソナライズしたりできます。

| Brazeカスタムイベント | Recurlyイベント |
| ----------- | ----------- |
| Recurly New Subscription              | サブスクリプションが作成されたときにトリガーされます                            |
| Recurly Renewed Subscription          | サブスクリプションが更新されたときにトリガーされます                                |
| Recurly Updated Subscription          | サブスクリプションの属性が変更されたときにトリガーされます（プランの変更、価格の変更、または数量の変更） |
| Recurly Canceled Subscription         | サブスクリプションがキャンセルされたときにトリガーされます                           |
| Recurly Reactivated Subscription      | キャンセルされたサブスクリプションが再アクティブ化されたときにトリガーされます               |
| Recurly Paused Subscription           | サブスクリプションが一時停止に設定されたときにトリガーされます                   |
| Recurly Resumed Subscription          | サブスクリプションが再開されたときにトリガーされます                              |
| Recurly Subscription Expired          | サブスクリプションの有効期限が切れたときにトリガーされます                               |
| Recurly Invoice Created               | 請求書が作成されたときにトリガーされます                                |
| Recurly Successful Payment            | 請求書が正常に回収されたときにトリガーされます                 |
| Recurly Refund Issued                 | 返金が行われたときにトリガーされます                                   |
| Recurly Failed Recurring Payment      | サブスクリプション更新の請求書が失敗したときにトリガーされます          |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom events" }

### バッチ処理とレート制限 {#batching-and-rate-limiting}

RecurlyはBrazeの`/users/track`エンドポイントを使用しているため、この統合は標準的なBrazeレート制限（1分あたり50,000件のリクエスト）の対象となります。

Recurlyは、特定のサブスクリプションライフサイクルイベントをBrazeへの単一のAPI呼び出しにバッチ処理し、リクエスト数を削減します。

- Recurlyは、同時に作成された複数のサブスクリプションをバッチ処理し、1つのリクエストとして送信します。
- Recurlyは、アカウントの複数の同時更新を1つのリクエストにまとめます。
- Recurlyは同じモデルのサブスクリプションライフサイクルイベントを単一のリクエストで送信します。例えば、支払いを伴う新規請求書の作成は、`Recurly Invoice Created`と`Recurly Successful Payment`のカスタムイベントを含む1つのAPIリクエストになります。

バッチは一度に最大75個のイベントのグループでBrazeに送信されます。例えば、100件のサブスクリプションが一度に作成された場合、RecurlyはBrazeに対して2回のAPIリクエストを行います。詳細については、[ユーザートラックリクエストのバッチ処理]({{site.baseurl}}/api/api_limits/#batch-user-track)を参照してください。