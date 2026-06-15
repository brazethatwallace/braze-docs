---
nav_title: Dynamics 365 Customer Insights
article_title: Dynamics 365 Customer Insights
description: "このリファレンス記事では、Brazeと Dynamics 365 Customer Insightsのパートナーシップについて説明します。Dynamics 365 Customer Insightsは業界をリードするエンタープライズ顧客データプラットフォームであり、顧客セグメントをBrazeにエクスポートしてキャンペーンやキャンバスで使用できます。"
alias: /partners/dynamics_365_customer_insights/
page_type: partner
search_tag: Partner
---

# Dynamics 365 Customer Insights

> [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) は、顧客の360度ビューでパーソナライズされたカスタマーエクスペリエンスを提供する、エンタープライズ向けの主要な顧客データプラットフォームです。

_この統合は、Dynamics 365 Customer Insightsによって管理されています。_

## 統合について {#about-the-integration}

BrazeとDynamics 365 Customer Insightsの統合により、顧客セグメントをBrazeにエクスポートしてキャンペーンやキャンバスで使用できるようになります。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Dynamics 365 Customer Insightsアカウント | このパートナーシップを活用するには、[Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) アカウントが必要です。必要なプラグインにアクセスするためにDynamics 365 Customer Insightsアカウント内で接続を表示および編集するには、管理者としてのアクセスが必要です。 |
| Braze REST APIキー | `users.track` と `users.export.segment` の権限を持つBraze REST APIキーが必要です。<br><br> これは、Brazeダッシュボードの**Settings** > **API Keys**で作成できます。 |
| プロファイル識別子の一致 | エクスポートされたセグメントの統合済み顧客プロファイルには、メールアドレスを表すフィールドとBrazeの `external_id` が含まれます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合 {#integration}

### ステップ 1: Brazeの接続を設定する {#step-1-set-up-braze-connection}

Customer Insightsで**Admin** > **Connections**に移動します。次に、**Add connections**を選択し、**Braze**を選択して接続を設定します。

1. **Display name**フィールドで、接続にわかりやすい名前を付けます。
2. この接続を使用できるユーザーを選択します。このフィールドを空白にすると、デフォルトはAdministratorsになります。詳細については、[共同作成者がエクスポートに接続を使用できるようにする](https://docs.microsoft.com/en-us/dynamics365/customer-insights/connections#allow-contributors-to-use-a-connection-for-exports)を参照してください。
3. Braze APIキーとRESTエンドポイントを `rest.iad-03.braze.com` の形式で入力します。
4. **I agree**を選択して、データとプライバシーの遵守を確認します。
5. **Connect**を選択して、Brazeへの接続を初期化します。
6. **Add yourself as export user**を選択し、Customer Insightsの認証情報を入力します。
7. **Save**を選択して接続を完了します。

### ステップ 2: Braze セグメントを作成する {#step-2-create-a-braze-segment}

1. Brazeで、**Audience** > **セグメント**に移動します。
2. Dynamics 365 Customer Insightsを介してMicrosoftに更新させたいユーザーのセグメントを作成します。
3. セグメントの**API 識別子**を取得します。

### ステップ 3: エクスポートを設定する {#step-3-configure-an-export}

このタイプの接続にアクセスできる場合は、このエクスポートを設定できます。詳細については、[エクスポートの概要](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#set-up-a-new-export)を参照してください。

1. Customer Insightsで**Data** > **Exports**に移動します。新しいエクスポートを作成するには、**Add destination**を選択します。
2. **Connection for export**フィールドで、Brazeセクションの接続を選択します。このセクション名が表示されない場合は、このタイプの接続は利用できません。
3. BrazeでセグメントのセグメントAPI識別子を指定します。
4. **Data matching**セクションの**Email**フィールドで、顧客のメールアドレスを表すフィールドを選択します。次に、**Braze Customer ID**フィールドで、顧客のBraze IDを表すフィールドを選択します。また、データマッチング用の追加のオプションフィールドを選択することもできます。
  a. Brazeで `external_id` をCustomer InsightsのBraze顧客IDフィールドにマップすると、エクスポート時にBrazeで既存のレコードが更新されます。
  b. Brazeのレコードの `external_id` を表さない別のIDフィールド、または空のフィールドをマップすると、エクスポート時に新しいレコードがBrazeで作成されます。
5. 最後に、エクスポートするセグメントを選択して、**Save**を選択します。

エクスポートを保存しても、すぐにエクスポートが実行されるわけではありません。このエクスポートは、[スケジュールされた更新](https://docs.microsoft.com/en-us/dynamics365/customer-insights/system#schedule-tab)ごとに実行されます。[オンデマンドでデータをエクスポートする](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#run-exports-on-demand)こともできます。


### この統合を使用する {#using-this-integration}

セグメントが正常にBrazeにエクスポートされたら、ユーザープロファイルでカスタム属性として確認できます。カスタム属性には、エクスポート接続の設定時に入力されたBrazeセグメントAPI識別子が名前として設定されます。例: `"セグメント_API_Identifier": "0000-0000-0000"`

Brazeでこれらのユーザーのセグメントを作成するには、**セグメント**に移動して、新しいセグメントを作成し、フィルターとして**Custom Attributes**を選択します。ここから、Dynamics 365と同期したカスタム属性を選択できます。セグメントを作成した後、キャンペーンまたはキャンバスを作成する際に、オーディエンスフィルターとして選択できます。

{% alert note %}
この統合の詳細については、Microsoftの[Braze統合の記事](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-braze)を参照してください。
{% endalert %}