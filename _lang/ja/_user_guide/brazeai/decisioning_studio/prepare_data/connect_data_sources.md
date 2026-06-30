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

## サポートされている統合パターン {#supported-integration-patterns}

Decisioning Studioは、顧客データを接続するための複数の統合パターンをサポートしています。

| 統合パターン | 最適な用途 | セットアップの複雑さ |
|---------------------|----------|------------------|
| **Brazeデータプラットフォーム** | すでにBrazeを使用している顧客 | 低 |
| **Brazeクラウドデータ取り込み（CDI）** | 外部データウェアハウスの接続 | 中 |
| **クラウドストレージ（GCS、AWS、Azure）** | 他のプラットフォームからの直接データエクスポート | 中 |
| **CEP統合** | SFMC、Klaviyoデータエクステンション | 中 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="サポートされている統合パターン" }

## 顧客データタイプ {#customer-data-types}

以下の顧客データアセットは、エージェントがより効果的にパーソナライズするのに役立ちます。

| データタイプ | 説明 | 例 |
|-----------|-------------|----------|
| **顧客プロファイル** | 静的でゆっくり変化する属性 | 顧客歴年数、地域、獲得チャネル、満足度、ライフタイムバリュー推定値 |
| **顧客行動** | アクティビティとエンゲージメントパターン | アカウントログイン、デバイスタイプ、カスタマーサービスのインタラクション、製品使用状況 |
| **取引履歴** | 購入とコンバージョンデータ | 購入した製品、取引金額、支払い方法、購入チャネル |
| **マーケティングエンゲージメント** | コミュニケーションへの反応 | メールの開封/クリック、SMSエンゲージメント、Webおよびモバイルアクティビティ、調査への回答 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="顧客データタイプ" }

{% alert tip %}
エージェントが顧客について持つ情報が多いほど、パフォーマンスが向上します。ビジネスにとって特に重要なインサイトに関するデータを含めることを検討してください（例えば、AIがロイヤルティ顧客をどのように異なる扱いにするかを確認したい場合は、ロイヤルティステータスが顧客データに含まれていることを確認してください）。
{% endalert %}

## プラットフォーム別のデータ接続 {#connect-data-by-platform}

{% tabs %}
{% tab Braze %}

### Brazeを通じて顧客データを送信する {#send-customer-data-through-braze}

BrazeAI Decisioning Studioは、すでにBrazeデータプラットフォームに送信しているすべてのデータを使用できます。

Decisioning Studioに使用したい顧客データが、現在ユーザープロファイルやカスタム属性に保存されていない場合、推奨されるアプローチは[Brazeクラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を使用して他のソースからデータを取り込むことです。

CDIは以下との直接統合をサポートしています：

- Snowflake
- Redshift
- BigQuery
- Databricks
- Microsoft Fabric
- AWS S3

サポートされているソースの完全なリストについては、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を参照してください。

Brazeデータプラットフォームに送信しているデータに満足したら、AI Decisioning Servicesチームに連絡して、ユーザープロファイルまたはカスタム属性のどのフィールドをAI意思決定に使用すべきかを相談してください。

このプロセスを効率化するために、Decisioning Studioで使用すべき顧客の行動を最もよく表すと思われるBrazeユーザープロファイル属性のリストを作成してください（[利用可能なフィールドのリスト]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment#fields-to-export)を参照）。サービスチームは、AI意思決定に最も適切なフィールドを決定するためのディスカバリーセッションの実施もサポートできます。

データを送信するその他のオプションには以下があります：

- SDKを介してBrazeカスタムイベントを送信する
- RESTエンドポイント（[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)）を使用してイベントを送信する

これらのパターンはより多くのエンジニアリング作業が必要ですが、現在のBraze設定によっては好ましい場合があります。詳細については、AI Decisioning Servicesチームにお問い合わせください。

{% endtab %}
{% tab SFMC %}

### SFMCを通じて顧客データを送信する {#send-customer-data-through-sfmc}

Salesforce Marketing Cloudとの統合の場合：

1. 顧客データ用のSFMCデータエクステンションを設定します
2. Decisioning Studioが必要とする適切な権限を持つAPI統合用のSFMCインストール済みパッケージを設定します
3. Decisioning Studioは利用可能な最新の増分データから取得するため、データエクステンションが毎日更新されることを確認します

エクステンションIDとAPIキーをAI Decisioning Servicesチームに提供してください。チームが顧客データの取り込みにおける次のステップをサポートします。

{% endtab %}
{% tab Klaviyo %}

### Klaviyoを通じて顧客データを送信する {#send-customer-data-through-klaviyo}

Klaviyoとの統合の場合：

1. 顧客プロファイルデータがKlaviyoプロファイルで利用可能であることを確認します
2. プロファイルへのフルアクセス権を持つプライベートAPIキーを生成します
3. APIキーをAI Decisioning Servicesチームに提供します

APIキーの設定の詳細については、[Klaviyoドキュメント](https://help.klaviyo.com/hc/en-us/articles/115005237908)を参照してください。

{% endtab %}
{% tab Cloud Storage %}

### その他のクラウドソリューション（Google Cloud Storage、Azure、AWS） {#other-cloud-solutions-google-cloud-storage-azure-aws}

顧客データが現在Braze、SFMC、またはKlaviyoに保存されていない場合、次善のステップは、Brazeが管理するGoogle Cloud Storageバケットへの自動エクスポートを設定することです。AWSまたはAzureへのエクスポートもサポートできます（ただしGCSが推奨されます）。これらのプラットフォームの場合、それぞれのクラウドプラットフォーム内の内部クラウドストレージにエクスポートし、Brazeがそのデータを取得できるようにします。

これが実現可能かどうかを判断するには、お使いのマーテクプラットフォームのドキュメントを参照してください。例えば：

- mParticleは[Google Cloud Storageとのネイティブ統合](https://www.mparticle.com/integration/google-cloud-storage/)を提供しています
- [Twilio セグメント](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [トレジャーデータ](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

これが実現可能な場合、Decisioning Studio専用に分離された顧客データエクスポート用のGCSバケットを提供できます。

{% endtab %}
{% endtabs %}

## ベストプラクティス {#best-practices}

- **わかりやすいカラム名：** 顧客データには明確でわかりやすいカラム名を付ける必要があります。理想的には、データディクショナリを提供してください。
- **増分更新：** 毎日の顧客履歴全体のスナップショットよりも、増分ファイルが推奨されます
- **一貫した識別子：** 各レコードには、すべてのデータアセットで一貫したユニークな顧客識別子が含まれている必要があります
- **タイムスタンプを含める：** 正確なアトリビューションとエージェントのトレーニングのために、レコードには関連するタイムスタンプが必要です

## カスタム統合 {#custom-integrations}

その他のオプションや完全にカスタムのデータパイプラインも可能です。これらには、チームからの追加のサービス作業またはエンジニアリング作業が必要になる場合があります。何が実現可能で最適かを判断するには、AI Decisioning Servicesチームと協力してください。

{% alert important %}
このガイドでは、最も一般的な統合パターンについて説明しています。情報セキュリティチームがすべての接続ポイントを審査する必要があり、ソリューションコンサルタントが実装に関するアドバイスを提供します。
{% endalert %}

## 次のステップ {#next-steps}

データソースを接続した後、オーケストレーションの設定に進みます：

- [オーケストレーションを設定する]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/orchestration_setup)