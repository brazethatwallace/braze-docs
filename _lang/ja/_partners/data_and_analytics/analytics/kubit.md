---
nav_title: Kubit
article_title: Kubit
description: "このリファレンス記事では、BrazeとKubitのパートナーシップについて説明します。Kubitは、製品インサイトを即座に提供するノーコードのセルフサービス分析プラットフォームであり、KubitユーザーコホートをインポートしてBrazeメッセージングでターゲットにすることができます。"
alias: /partners/kubit/
page_type: partner
search_tag: Partner

---

# Kubit

> [Kubit](https://kubit.ai/)は、製品インサイトを即座に提供するノーコードのセルフサービス分析プラットフォームです。

BrazeとKubitの統合により、[Kubitユーザーコホートをインポート]({{site.baseurl}}/partners/data_and_analytics/cohort_import/kubit)し、Brazeメッセージングでターゲットにすることができます。さらに、[Snowflakeセキュアデータ共有]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)を使用することで、Brazeの生のキャンペーンおよびインプレッションデータをKubitの製品分析と統合し、これらのキャンペーンの効果をリアルタイムで測定できます。このアプローチにより、開発の作業を必要とすることなく、ユーザーのライフサイクル全体に関するインサイトを得ることができます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Kubitエンタープライズアカウント | このパートナーシップを利用するには、Kubitエンタープライズアカウントが必要です。 |
| ユーザーIDの一致 | KubitとBrazeの顧客データは、2つのプラットフォーム間でユーザーIDが一致している必要があります。これには匿名UUIDも含まれます。BrazeがどのようにユーザーIDを設定するかについては、[ドキュメント]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=android)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## KubitでBrazeデータを分析する {#analyzing-braze-data-in-kubit}

[Snowflakeセキュアデータ共有]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)を活用して、Brazeの生のキャンペーンおよびインプレッションデータをKubitと共有し、Kubitのセルフサービス分析に組み込むことで、ユーザーのライフサイクルの全体像を把握できます。

参考として、Kubit分析に組み込むことが可能なすべての[Brazeフィールド](/docs/assets/download_file/data-sharing-raw-table-schemas.txt)をこちらで確認できます。このステップの詳細は顧客ごとに大きく異なり、特別な設定が必要です。詳しくは、Kubitアカウントマネージャーまたは[support@kubit.ai](mailto:support@kubit.ai)までお問い合わせください。