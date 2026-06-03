---
nav_title: Airbyte
article_title: Airbyte
description: "このリファレンス記事では、BrazeとAirbyteの統合について説明します。Airbyteはデータウェアハウス、データレイク、データベースにデータを統合するのに役立つオープンソースのデータ統合エンジンであり、AirbyteからBrazeにリアルタイムのイベントを転送します。"
alias: /partners/airbyte/
page_type: partner
search_tag: Airbyte

---

# Airbyte

> [Airbyte](https://airbyte.com/) は、データウェアハウス、データレイク、データベースにデータを統合するのに役立つオープンソースのデータ統合エンジンです。

_この統合はAirbyteによって管理されています。_

## 統合について {#about-the-integration}

BrazeとAirbyteの統合により、ユーザーはすべてのアプリケーションとデータベースを中央のデータウェアハウスに接続することで、Brazeデータを収集・分析するためのデータパイプラインを作成できます。中央のデータウェアハウスにデータが収集されると、データチームは好みのビジネスインテリジェンスツールを使用して、Brazeデータを効率的に調査できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Airbyte Cloudアカウント | この統合を利用するには、[Airbyte Cloud](https://cloud.airbyte.io/workspaces)アカウントが必要です。 |
| Braze REST APIキー | すべての権限を持つBraze REST APIキー。<br><br> これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | エンドポイントは、お使いのインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

1. Airbyte Cloudアカウントで、**Sources** > **+ New Source** > **Set up the Source** に移動します。
2. ソース名として「Braze」を入力し、ソースのドロップダウンから**Braze**を選択します。
3. エンドポイントURL、Braze REST APIキー、および開始日を入力します。**Set up Source** をクリックします。

### サポートされる同期モード {#supported-sync-modes}

AirbyteのBrazeソースコネクターは、以下の[同期モード](https://docs.airbyte.com/cloud/core-concepts#connection-sync-modes)をサポートしています。
- **フルリフレッシュ | 上書き**: ソースからすべてのレコードを同期し、送信先のデータを上書きして置き換えます。
- **増分同期 | 追加**: ソースから新しいレコードを同期し、データを削除せずに送信先に追加します。

### サポートされるストリーム {#supported-streams}

- [`campaigns`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f3b0b3ef-04fb-4a31-8570-e6ad88dacb18)
- [`campaigns_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c07b5ebd-0246-471e-b154-416d63ae28a1)
- [`canvases`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e6c150d7-fceb-4b10-91e2-a9ca4d5806d1)
- [`canvases_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0fd61e93-7edf-4d87-a8dc-052420aefb73)
- [`events`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#93ecd8a5-305d-4b72-ae33-2d74983255c1)
- [`events_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bd1ab63-d1a5-4301-8d17-246cf24a178c)
- [`kpi_daily_new_users`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#07756c39-cfa0-40a0-8101-03f8791cec01)
- [`kpi_daily_active_users`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#90a64560-65aa-4f71-a8ef-1edf49321986)
- [`kpi_daily_app_uninstalls`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#59c4d592-3e77-42f8-8ff1-d5d250acbeae)
- [`cards`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9fa7a3bc-4a02-4de2-bc4c-8f111750665e)
- [`cards_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9cdc3b1e-641e-4d62-b9e8-42d04ee9d4d8)
- [`segments`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1349e6f4-3ce7-4e60-b3e9-951c99c0993f)
- [`segments_analytics`](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#62d9d142-cdec-4aea-a287-c13efea7415e)

{% alert note %}
レート制限はストリームによって異なります。詳しくは[レート制限テーブル]({{site.baseurl}}/api/api_limits/#rate-limits-by-request-type)を参照してください。
{% endalert %}