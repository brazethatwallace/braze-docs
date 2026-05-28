---
nav_title: ActionIQ
article_title: ActionIQ
description: "このリファレンス記事では、BrazeとActionIQの統合について説明します。ActionIQはマーケター、アナリスト、技術者のためのエンタープライズ顧客データプラットフォームです。この統合により、ブランドはActionIQのデータをBrazeに直接同期し、マッピングすることができます。"
alias: /partners/actioniq/
page_type: partner
search_tag: ActionIQ
---

# ActionIQ

> [ActionIQ](https://www.actioniq.com/) は、マーケターがカスタマーエクスペリエンスのあらゆる場所でデータを簡単かつ安全に活用できる方法を提供する、エンタープライズブランド向けの顧客データプラットフォームです。ActionIQ独自のコンポーザブルアーキテクチャにより、データは現在ある場所に安全に保持され、マーケティングチームは必要なツールだけを使用できます。

_この統合はActionIQによって管理されています。_

## 統合について {#about-the-integration}

BrazeとActionIQの統合により、ブランドはActionIQデータを直接Brazeに同期してマッピングできます。これにより、幅広い顧客データ全体に基づく卓越したカスタマーエクスペリエンスの提供が可能になります。利用可能な統合を使用することで、ユーザーは以下を実行できます。

- Brazeのユーザープロファイルを、オーディエンスのメンバーシップ情報とActionIQから直接得られる属性で更新する
- ActionIQで追跡されたイベントをリアルタイムでBrazeに転送し、パーソナライズされたターゲットキャンペーンをトリガーする
- APIトリガーのキャンペーンを、ActionIQジャーニーのタッチポイントから直接Brazeで配信する

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| ActionIQアカウント | この統合を利用するには、ActionIQアカウントが必要です。 |
| Braze REST APIキー | それぞれの統合に必要な権限を備えたBraze REST APIキー。詳細については、それぞれの要件セクションを参照してください。<br><br>このキーは、Brazeダッシュボードの**Settings** > **API Keys**から作成できます。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、お使いのインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integrations}

### オーディエンスメンバーシップ {#audience-membership}

この統合は、Brazeプロファイルがセグメントに属しているかどうかを示すカスタム属性を作成することで、ActionIQのオーディエンスメンバーシップをBrazeに同期するために使用されます。各ActionIQオーディエンスは、固有のブール値カスタム属性に対応します。

作成されるカスタム属性の標準的な命名規則は次のとおりです: `AIQ_<Audience ID>_<Split ID>`

これらのユーザーのセグメントを作成するには、以下の手順を実行します。
1. Brazeで**セグメント**に移動します。
2. 新しいセグメントを作成します。
3. フィルターとして**Custom Attributes**を選択します。
4. ここから、ActionIQカスタム属性を選択します。
5. セグメントを作成した後、キャンペーンまたはキャンバスを作成する際にオーディエンスフィルターとして選択できます。

さらに、この統合は、Brazeユーザープロファイルのカスタムまたは標準属性項目を、ActionIQの属性値で更新します。

#### 要件 {#requirements}

`users.track`と`user.export.ids`の権限を持つBraze REST APIキーが必要です。これは、Brazeダッシュボードの**Settings** > **API Keys**で作成できます。

ActionIQで、REST APIキーとBraze RESTエンドポイントを指定して、Braze接続を設定します。

Brazeプラットフォームで消費者とマッチングするためには、アクティベーション設定に次の識別子が含まれている必要があります。
- `braze_id`
- `external_id`

### イベント {#events}

ActionIQプラットフォームは、ストリーミングインジェストサービスを通じてイベント情報を受信するように設定できます。この統合オプションは、これらのイベントをBrazeに転送し、マーケターがオーケストレーションやマーケティングキャンペーンのトリガーに使用できるようにします。イベント統合は、イベントペイロード内のプロパティの一部として、追加のActionIQ属性を送信できます。

#### 要件

`users.track`と`user.export.ids`の権限を持つBraze REST APIキーが必要です。これは、Brazeダッシュボードの**Settings** > **API Keys**で作成できます。

イベント統合は以下の情報をBrazeに送信します。
- イベント名
- 消費者識別子（`braze_id`または`external_id`）
- タイムスタンプ
- イベントプロパティ（エクスポート設定の追加属性により取り込まれます）

### トリガーキャンペーン {#triggered-campaigns}

この統合は、ActionIQのセグメント内のすべてのユーザーに対してBrazeでキャンペーンをトリガーします。キャンペーンのコピー、多変量テスト、再適格性ルールを設定した後に、Brazeのキャンペーン IDをエクスポート設定に追加すると、ActionIQジャーニーのどのタッチポイントからでもトリガーすることができます。

オプションで、エクスポートに他のActionIQ属性を含めてキャンペーンコピーに入力できます。これらは`trigger_properties`オブジェクトとともに送信されます。

#### 要件

`campaigns.trigger.send`と`campaigns.list`の権限を持つBraze REST APIキーが必要です。これは、Brazeダッシュボードの**Settings** > **API Keys**で作成できます。

BrazeへのActionIQエクスポートでは、以下の値を送信する必要があります。
- 消費者識別子（`braze_id`または`external_id`）
- キャンペーン ID