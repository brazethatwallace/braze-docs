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

| 必要条件 | 説明 |
|---|---|
| Datadogアカウント | このパートナーシップを利用するには、Datadogアカウントが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携 {#integration}

### ステップ1:Datadogキーを生成する {#step-1-generate-datadog-key}

Datadogで[APIキー](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys)を作成する必要があります。APIキーを追加するには、**Organization Settings** > **API Keys** > **New Key** に移動します。

### ステップ2:Brazeにキーを追加する {#step-2-add-key-to-braze}

Brazeダッシュボードで**パートナー連携** > **テクノロジーパートナー**に移動し、**Datadog**を検索します。Datadogパートナーページで Datadog APIキーを入力します。これにより、BrazeがDatadogにデータを送信するための接続が作成されます。

## Brazeイベント {#braze-events}

接続が統合されると、Brazeは以下のイベントをDatadogに送信します。

- `braze.messaging.sent` — 送信数

これらの各イベントにはDatadogタグの形式でメタデータが付与され、以下のような情報を確認できます。

- `app_group_id`
- `app_group_name`
- `campaign_id` / `campaign_name`（利用可能な場合）
- `canvas_id` / `canvas_name` / `canvas_step_id` / `canvas_step_name`（利用可能な場合）

これらのイベントとタグは、Datadogの**Metrics Explorer**ページで監視できます。これらの指標はDataDogに[ディストリビューション](https://docs.datadoghq.com/metrics/distributions/)として記録されます。指標の性質とDataDogの集約およびロールアップの不正確さを考慮し、Brazeでは送信中に発生する可能性のある断続的なネットワークエラーやその他のDataDog APIエラーに対して再試行を行いません。そのため、これらの指標の数値は、BrazeダッシュボードやCurrentsで表示される数値と若干異なる場合があります。

![Brazeイベントの指標とタグを表示するDatadog Metrics Explorer。]({% image_buster /assets/img/datadog.png %})