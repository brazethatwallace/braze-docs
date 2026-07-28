---
nav_title: actionable.me
article_title: actionable.me
description: "このリファレンス記事では、Brazeとactionable.meのパートナーシップについて説明します。actionable.meは、Brazeへの投資を今すぐ最大限に引き出すことができる専用ソフトウェアおよびプロセスです。"
alias: /partners/actionableme/
page_type: partner
search_tag: Partner

---

# actionable.me

> [actionable.me](https://actionable.me)は、データおよびCRMエージェンシーであるMassive Rocketのチームによって開発された、CRMプログラムを実行するための標準化および自動化されたアプローチです。Brazeの顧客に、迅速かつ一貫性があり予測可能な方法で価値を実現するためのツールとプロセスを提供します。

_この統合はactionable.meによって管理されています。_

## 統合について {#about-the-integration}

Brazeとactionable.meの統合により、Brazeの利用状況の進捗を監視するサービスをデプロイできます。ツールとプロセスを組み合わせることで、CRMのパフォーマンスが迅速にベンチマークされ、新しい機会が特定され、パフォーマンスの向上に関するおすすめが提供されます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| --- | --- |
| actionable.meアカウント | このパートナーシップを活用するには、actionable.meアカウントが必要です。 |
| Braze REST APIキー | 次のセクションに記載されている権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**設定** > **API キー**から作成できます。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、お使いのインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

Brazeとactionable.meを統合するには、actionable.meプラットフォームを設定し、Braze APIキーをBrazeで作成してactionable.meダッシュボードで設定する必要があります。

### ステップ1:Braze APIキーを作成する {#step-1-create-your-braze-api-key}

Brazeで**設定** > **API キー**に移動します。**API キーを作成**を選択し、以下の権限が追加されていることを確認します。

- `campaigns.list`
- `campaigns.data_series`
- `campaigns.details`
- `sends.data_series`
- `segments.list`
- `segments.data_series`
- `segments.details`
- `events.list`
- `canvas.list`
- `canvas.data_series`
- `canvas.details`
- `canvas.data_summary`
- `kpi.mau.data_series`
- `kpi.dau.data_series`
- `kpi.new_users.data_series`
- `kpi.uninstalls.data_series`

### ステップ2:actionable.meチームに情報を提供する {#step-2-provide-information-to-the-actionableme-team}

統合を完了するには、REST APIキーと[RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)をactionable.meオペレーションチームに提供する必要があります。actionable.meが接続を確立し、セットアップ完了後に連絡を取り、インサイトの共有を開始します。

![actionable.meオペレーションチームが設定するactionable.meの「プラットフォームの追加」ページ。]({% image_buster /assets/img/actionableme/image2.png %})

## トラブルシューティング {#troubleshooting}

その他のサポートについては、actionable.meまたはMassive Rocketチーム（[info@massiverocket.com](mailto:info@massiverocket.com)）にお問い合わせください。