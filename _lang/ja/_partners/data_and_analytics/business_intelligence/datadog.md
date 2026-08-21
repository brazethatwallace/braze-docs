---
nav_title: Datadog
article_title: Datadog
description: "このリファレンス記事では、BrazeとDatadogのパートナーシップについて説明します。Datadogはクラウドスケールのアプリケーション向けオブザーバビリティサービスであり、SaaSベースのデータ分析プラットフォームを通じてサーバー、データベース、ツール、サービスの監視を提供します。"
alias: /partners/datadog/
page_type: partner
search_tag: Partner


---

# Datadog

> [Datadog](https://www.datadoghq.com/) は、クラウドスケールのアプリケーション向けオブザーバビリティサービスであり、SaaSベースのデータ分析プラットフォームを通じてサーバー、データベース、ツール、サービスの監視を提供します。

BrazeとDatadogの連携により、顧客はDatadogでBrazeデータを収集し、送信するデータに関するアラートを作成できます。たとえば、毎週のニュースレターキャンペーンで送信されるメッセージの量が異常に少ない場合や、通常は1日に数通しか送信しないキャンバスステップが数千通を送信し始めた場合に、モニターとアラートを設定できます。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| Datadog アカウント | このパートナーシップを利用するには、Datadog アカウントが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携 {#integration}

### ステップ1：Datadogキーを生成する {#step-1-generate-datadog-key}

Datadogで[APIキー](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys)を作成する必要があります。APIキーを追加するには、**Organization Settings** > **API Keys** > **New Key** に移動します。

### ステップ2：Brazeにキーを追加する {#step-2-add-key-to-braze}

Brazeダッシュボードで、**パートナー連携** > **テクノロジーパートナー** に移動し、**Datadog** を検索します。Datadogパートナーページで、Datadog APIキーを入力します。これにより、BrazeがDatadogにデータを送信するための接続が作成されます。

## Brazeイベント {#braze-events}

連携が完了すると、BrazeはDatadogに以下のイベントを送信します。

- `braze.messaging.sent` - 送信数のカウント

これらの各イベントには、Datadogタグの形式でメタデータが含まれており、以下のような情報を提供します。

- `app_group_id`
- `app_group_name`
- `campaign_id` / `campaign_name`（利用可能な場合）
- `canvas_id` / `canvas_name` / `canvas_step_id` / `canvas_step_name`（利用可能な場合）

これらのイベントとタグは、Datadogの**Metrics Explorer**ページで監視できます。これらのメトリクスはDataDogに[ディストリビューション](https://docs.datadoghq.com/metrics/distributions/)として記録されます。メトリクスの性質およびDataDogの集計やロールアップの不正確さを考慮し、Brazeは送信中に発生する可能性のある断続的なネットワークエラーやその他のDataDog APIエラーに対してリトライを行いません。そのため、これらのメトリクスのカウントは、BrazeダッシュボードやCurrentsで確認できるカウントとわずかに異なる場合があります。

![Brazeイベントメトリクスとタグを表示するDatadog Metrics Explorer。]({% image_buster /assets/img/datadog.png %})

## トラブルシューティング {#troubleshooting}

### Datadog で `braze.messaging.sent` メトリクスが表示されないのはなぜですか？ {#why-are-brazemessagingsent-metrics-missing-in-datadog}

Braze を Datadog に接続したにもかかわらず、Metrics Explorer に `braze.messaging.sent` が表示されない場合は、Braze で選択した **Datadog サイト**が Datadog 組織のサイト URL と一致していることを確認してください。利用可能なサイトは以下のとおりです。

- `datadoghq.com`（デフォルト）
- `us3.datadoghq.com`
- `us5.datadoghq.com`
- `datadoghq.eu`
- `ddog-gov.com`
- `ap1.datadoghq.com`

サイトが一致していないと、検索先のワークスペースにメトリクスが表示されないことがあります。Braze ダッシュボードで、**パートナー連携** > **テクノロジーパートナー** > **Datadog** に移動し、サイトが Datadog アカウント URL のサブドメインと一致していることを確認してください。

**Datadog サイト**フィールドは接続後にロックされます。変更するには、連携を切断してから正しいサイトで再接続してください。

サイトを修正した後、メトリクスが表示されるまで新しい送信アクティビティが発生するのをお待ちください。過去のデータはバックフィルされません。