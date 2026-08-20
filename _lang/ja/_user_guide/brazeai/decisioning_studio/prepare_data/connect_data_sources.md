---
nav_title: データを接続する
article_title: データを接続する
page_order: 6
description: "パーソナライズされたAI意思決定のために、顧客データソースをBrazeAI Decisioning Studioに接続する方法を学びます。"
---

# データを接続する {#connect-your-data}

> BrazeAI Decisioning Studio™のエージェントは、効果的な意思決定を行うために、顧客コンテキストを十分に理解する必要があります。この記事では、顧客データソースをDecisioning Studioに接続する方法について説明します。

{% alert tip %}
AI Decisioning Servicesチームが、最適なパフォーマンスのためのデータ接続の設定をサポートします。
{% endalert %}

## サポートされている連携パターン {#supported-integration-patterns}

Decisioning Studioは、顧客データを接続するための複数の連携パターンをサポートしています。

| 連携パターン | 最適な用途 | セットアップの複雑さ |
|---------------------|----------|------------------|
| **Braze Data Platform** | すでにBrazeを利用している顧客 | 低 |
| **Braze Cloud Data Ingestion (CDI)** | 外部データウェアハウスとの接続 | 中 |
| **Cloud Storage (GCS、AWS、Azure)** | 他のプラットフォームからの直接データエクスポート | 中 |
| **CEP連携** | SFMC、Klaviyoデータエクステンション | 中 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="サポートされている連携パターン" }

## 顧客データの種類 {#customer-data-types}

以下の顧客データアセットは、エージェントがより効果的にパーソナライズを行うのに役立ちます。

| データの種類 | 説明 | 例 |
|-----------|-------------|----------|
| **顧客プロファイル** | 静的でゆっくり変化する属性 | 顧客歴（年数）、地域、獲得チャネル、満足度、推定生涯価値 |
| **顧客行動** | アクティビティとエンゲージメントのパターン | アカウントログイン、デバイスタイプ、カスタマーサービスとのやり取り、製品の利用状況 |
| **取引履歴** | 購入とコンバージョンのデータ | 購入した製品、取引金額、支払い方法、購入チャネル |
| **マーケティングエンゲージメント** | コミュニケーションへの反応 | メールの開封/クリック、SMSエンゲージメント、Webおよびモバイルのアクティビティ、調査への回答 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="顧客データの種類" }

{% alert tip %}
エージェントが顧客について持つ情報が多いほど、パフォーマンスが向上します。ビジネスにとって特に重要なインサイトに関するデータを含めることを検討してください（たとえば、AIがロイヤルティ顧客をどのように異なる扱いにするかを確認したい場合は、ロイヤルティステータスを顧客データに含めるようにしてください）。
{% endalert %}

## プラットフォーム別のデータ接続 {#connect-data-by-platform}

{% tabs %}
{% tab Braze %}

### Brazeを通じて顧客データを送信する {#send-customer-data-through-braze}

BrazeAI Decisioning Studioは、Brazeデータプラットフォームにすでに送信しているすべてのデータを使用できます。

ユーザープロファイルやカスタム属性にない顧客データについては、[Brazeクラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を使用して取り込む方法が2つあります。

- Brazeデータプラットフォームに取り込む。データウェアハウスのデータをBrazeユーザープロファイル、カスタム属性、またはイベントに同期します。セグメンテーションやメッセージングのためにBrazeでもデータを利用したい場合に選択してください。Snowflake、Redshift、BigQuery、Databricks、Microsoft Fabric、AWS S3、Google Cloud Storageに対応しています。
- Decisioning Studioに直接送信する（早期アクセス）。データウェアハウスのデータを、Brazeユーザープロファイルやカスタム属性に追加せずに、Decisioning Studioに直接同期します。Decisioning Studioで使用したいが、Brazeの他の場所では必要ないデータに適しています。このオプションは早期アクセス中です。設定方法については、[クラウドデータ取り込み：Decisioning Studioデータの同期]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/decisioning_studio)を参照してください。

Brazeデータプラットフォームに送信するデータに問題がなければ、AI意思決定サービスチームに連絡して、ユーザープロファイルやカスタム属性のどのフィールドをAI意思決定に使用すべきかを相談してください。

このプロセスを効率化するために、Decisioning Studioで使用すべき顧客の行動を最もよく表すと思われるBrazeユーザープロファイル属性のリストを作成してください（[エクスポート可能なフィールドの一覧]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment#fields-to-export)を参照）。サービスチームは、AI意思決定に最も適切なフィールドを決定するためのディスカバリーセッションの実施もサポートできます。

データを送信するその他のオプションには、以下があります。

- SDKを通じてBrazeカスタムイベントを送信する
- RESTエンドポイント（[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)）を使用してイベントを送信する

これらのパターンはより多くの開発工数が必要ですが、現在のBraze構成によっては望ましい場合があります。詳しくはAI意思決定サービスチームにお問い合わせください。

{% endtab %}
{% tab SFMC %}

### SFMCを通じて顧客データを送信する {#send-customer-data-through-sfmc}

Salesforce Marketing Cloudとの連携の場合：

1. 顧客データ用のSFMCデータエクステンションを設定します
2. Decisioning Studioが必要とする適切な権限を持つAPI連携用のSFMCインストール済みパッケージを設定します
3. Decisioning Studioは利用可能な最新の増分データから取得するため、データエクステンションが毎日更新されるようにしてください

エクステンションIDとAPIキーをAI意思決定サービスチームに提供してください。顧客データの取り込みに関する次のステップをサポートします。

{% endtab %}
{% tab Klaviyo %}

### Klaviyoを通じて顧客データを送信する {#send-customer-data-through-klaviyo}

Klaviyoとの連携の場合：

1. 顧客プロファイルデータがKlaviyoプロファイルで利用可能であることを確認します
2. プロファイルへのフルアクセス権を持つプライベートAPIキーを生成します
3. APIキーをAI意思決定サービスチームに提供します

APIキーの設定の詳細については、[Klaviyoのドキュメント](https://help.klaviyo.com/hc/en-us/articles/115005237908)を参照してください。

{% endtab %}
{% tab Cloud Storage %}

### その他のクラウドソリューション（Google Cloud Storage、Azure、AWS） {#other-cloud-solutions-google-cloud-storage-azure-aws}

顧客データが現在Braze、SFMC、またはKlaviyoに保存されていない場合、次善のステップとして、Brazeが管理するGoogle Cloud Storageバケットへの自動エクスポートを設定します。AWSやAzureへのエクスポートもサポートできます（ただしGCSが推奨されます）。これらのプラットフォームの場合、各クラウドプラットフォームの内部クラウドストレージにエクスポートし、Brazeがそのデータを取得できるようにします。

これが実現可能かどうかを判断するには、お使いのマーテクプラットフォームのドキュメントを参照してください。例：

- mParticleは[Google Cloud Storageとのネイティブ連携](https://www.mparticle.com/integration/google-cloud-storage/)を提供しています
- [Twilio セグメント](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [トレジャーデータ](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

これが実現可能な場合、Decisioning Studio専用に分離された顧客データエクスポート用のGCSバケットを提供できます。

{% endtab %}
{% endtabs %}

## ベストプラクティス {#best-practices}

- **わかりやすいカラム名:** 顧客データには、明確でわかりやすいカラム名を付ける必要があります。理想的には、データディクショナリを提供してください。
- **増分更新:** 毎日の顧客履歴全体のスナップショットよりも、増分ファイルが望ましいです。
- **一貫した識別子:** 各レコードには、すべてのデータアセットで一貫した一意の顧客識別子を含める必要があります。
- **タイムスタンプの付与:** 正確なアトリビューションとエージェントのトレーニングのために、レコードには関連するタイムスタンプを含める必要があります。

## カスタムインテグレーション {#custom-integrations}

その他のオプションや完全にカスタムのデータパイプラインも利用可能です。これらには、追加のサービス作業やチームからの開発作業が必要になる場合があります。何が実現可能で最適かを判断するには、AI意思決定サービスチームと連携してください。

{% alert important %}
このガイドでは、最も一般的なインテグレーションパターンについて説明します。情報セキュリティ部門がすべての接続ポイントを審査する必要があり、ソリューションコンサルタントが実装に関するアドバイスを提供します。
{% endalert %}

## 次のステップ {#next-steps}

データソースを接続した後、オーケストレーションの設定に進みます。

- [オーケストレーションの設定]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/orchestration_setup)