---
nav_title: Antavo
article_title: Antavo Loyalty Cloud
description: "このリファレンス記事では、Braze と Antavo のパートナーシップについて説明します。Antavo は、購入への報酬にとどまらない次世代ロイヤルティプログラムです。"
alias: /partners/antavo/
page_type: partner
search_tag: Partner
---

# Antavo Loyalty Cloud

> [Antavo](https://antavo.com/) は、包括的なロイヤルティプログラムを構築し、ブランド愛を育み、顧客行動を変えるエンタープライズグレードのSaaSロイヤルティテクノロジープロバイダーです。

_この統合はAntavoによって管理されています。_

## 統合について {#about-the-integration}

AntavoとBrazeの統合により、ロイヤルティプログラム関連データを使用してパーソナライズされたCampaignを構築し、カスタマーエクスペリエンスを向上させることができます。Antavoは2つのプラットフォーム間のロイヤルティデータ同期をサポートしています。これはAntavoからBrazeへの一方向データ同期のみです。この統合は`external_id` Brazeフィールドをサポートしており、Antavoはこのフィールドを使用してロイヤルティ会員IDを同期します。

## 前提条件 {#prerequisites}

| 必要条件          | 説明                                                                                                                                                                   |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------  |
| Antavoアカウント       | このパートナーシップを利用するには、Brazeとの統合を有効にした[Antavo](https://antavo.com/)アカウントが必要です。                                                |
| Braze REST APIキー   | `users.track`、`events.list`、`events.data_series`、`events.get`の権限を持つBraze REST APIキー。<br><br>これは、Brazeダッシュボードの**設定** > **APIキー**で作成できます。  |
| Braze RESTエンドポイント  | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントはインスタンスのBraze URLに依存します。                |
| Brazeアプリ識別子 | アプリ識別子キー。<br><br>Brazeダッシュボードでこのキーを確認するには、**設定** > **APIキー**に移動し、**Identification**セクションを確認してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

### ステップ 1: AntavoでBrazeに接続する {#step-1-connect-braze-in-antavo}

Antavoで**Modules** > **Braze**に移動し、**Configure**をクリックします。AntavoのBraze統合設定ページに初めてアクセスすると、2つのシステムを接続するよう求められます。

以下の認証情報を入力します。

- **Instance URL:** プロビジョニング先のインスタンスのBraze RESTエンドポイント。
- **API Token (Identifier):** AntavoがBrazeにリクエストを送信する際に使用するBraze REST APIキー。
- **App Identifier:** Brazeアプリ識別子。

認証情報を入力したら、**Connect**をクリックします。

![Instance URL、API Token、App Identifierが表示されているAntavoのConnect Braze画面。]({% image_buster /assets/img/antavo/connect_braze.png %})

### ステップ 2: フィールドマッピングを設定する {#step-2-configure-field-mapping}

接続が確立されると、Antavoの**Sync Fields**ページに自動的にリダイレクトされ、2つのシステム間のフィールド同期を設定できます。このページには**Modules** > **Braze**からいつでもアクセスできます。

Antavoでフィールドマッピングを設定するには:

1. **Add new field** <i class="fas fa-plus" alt=""></i>をクリックします。
2. ドロップダウンフィールドを使用して、Brazeに同期するAntavoの**Loyalty field**を選択します。
3. データの取り込み先となるBrazeの対応するカスタム属性を表す**Remote field**を入力します。

{% alert note %}
カスタム属性のリストは、Brazeの**データ設定** > **カスタム属性**で確認できます。入力したフィールドがBrazeで定義されていない場合、最初の同期で新しいフィールドが自動的に生成されます。
{% endalert %}

{:start="4"}
4. フィールドの組み合わせを追加するには、ステップ1〜3を繰り返します。
5. 同期データのリストからフィールドを削除するには、行の末尾にある<i class="fa-solid fa-rectangle-xmark" title="削除"></i>をクリックします。
6. **Save**をクリックします。

Antavoで設定されたフィールドのいずれかの値が変更されると、その単一の値の同期がトリガーされるだけでなく、フィールドマッピングに追加されたすべてのフィールドがリクエストに含まれます。

![AntavoのSync Fieldsページ。]({% image_buster /assets/img/antavo/data_field_mapping.png %})

{% alert important %}
データポイント使用量を最小限に抑えるため、Braze内でアクションを起こすフィールドのみをマッピングすることを推奨します。
{% endalert %}

#### サポートされるデータタイプ {#supported-data-types}

この統合では、Brazeのすべてのカスタム属性[データタイプ]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage)（数値（整数、浮動小数点）、文字列、配列、ブール値、オブジェクト、オブジェクト配列、日付）がサポートされています。

![さまざまなカスタム属性を示すBrazeプロファイル。]({% image_buster /assets/img/antavo/braze_profile.png %})

データフィールドは、設定されたフィールドマッピングに基づいて入力されます。

## トリガー {#triggers}

フィールドマッピングの設定に加え、Antavoの[ワークフロー](https://antavo.atlassian.net/wiki/spaces/AUM/pages/581402629)ツールに組み込まれた機能により、統合はさらなる機能を提供します。すべてのBrazeカスタム属性[データタイプ]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage)とカスタムイベントプロパティ[データタイプ]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#event-property-data-types)も、ワークフローを介して同期できます。

### ロイヤルティデータを随時同期する {#synchronizing-loyalty-data-occasionally}

データがAntavoのロイヤルティフィールドに格納されていない場合、またはデータがマッピングされたフィールドリストに追加されていない場合は、このオプションを使用します。要求されたデータの同期は、設定されたワークフロー条件が満たされたときにトリガーされます。

[最後の購入に関連するロイヤルティデータ](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Sync-data-related-to-the-customer%E2%80%99s-last-purchase)の同期を設定する方法については、ステップバイステップガイドを参照してください。

### ロイヤルティプログラムのイベントを同期する {#synchronizing-loyalty-program-events}

Antavoから同期されたイベントを使用して、アクションベースのBraze Canvasesにロイヤルティメンバーをエントリーさせます。この統合は、Brazeにカスタムイベントとして表示されるあらゆるAntavoイベント（購入イベントを含む）を同期できます。

[ロイヤルティプログラム登録イベント](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!)の同期および[ロイヤルティプログラム特典獲得イベント](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!)の同期の設定方法については、ステップバイステップガイドを参照してください。