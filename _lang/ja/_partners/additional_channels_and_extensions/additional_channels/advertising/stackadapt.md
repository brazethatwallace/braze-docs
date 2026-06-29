---
nav_title: StackAdapt
article_title: StackAdapt
description: "このリファレンス記事では、BrazeとStackAdaptのパートナーシップについて説明します。"
alias: /partners/stackadapt/
page_type: partner
search_tag: Partner
---

# StackAdapt

> [StackAdapt](https://www.stackadapt.com/)は、ターゲットを絞ったパフォーマンス重視の広告を配信するためにデジタルマーケターが使用する、AIを活用した業界トップのマーケティングプラットフォームです。

_この統合はStackAdaptによって管理されています。_

BrazeとStackAdaptの統合により、ユーザープロファイルデータをBrazeからStackAdapt Data Hubに同期できます。2つのプラットフォームを接続することで、顧客の統一されたビューを作成し、ファーストパーティデータを活用して広告パフォーマンスを向上させることができます。

## ユースケース {#use-cases}

- **離脱ユーザーの再エンゲージメント：** Brazeのメールマーケティングリストから配信停止したユーザーを特定し、StackAdaptのプログラマティック広告でターゲティングして、別のチャネルを通じて再エンゲージメントを図ります。
- **マルチチャネル体験の構築：** ユーザーのジャーニーをメール以外にも拡張します。例えば、ユーザーがBrazeのメールキャンペーンをクリックした場合、StackAdaptを使って補完的なプログラマティック広告を表示し、メッセージを強化してさらなるアクションを促すことができます。
- **大規模なパーソナライゼーション：**「市区町村」や「言語」といったBrazeの詳細なデータポイントを活用し、関連性の高い、ローカライズされた、言語固有の広告やメールを配信します。
- **オーディエンスへの理解を深める：** プロファイル属性を同期することで、StackAdaptでよりリッチなオーディエンスセグメントを作成し、より正確なターゲティングとパーソナライズされた広告体験を実現できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ------------------- |
| **StackAdaptアカウント** | Data Hub統合を管理する権限を持つアクティブなStackAdaptアカウントが必要です。 |
| **Braze REST APIキー** | 以下の権限を持つBraze REST APIキー：<br>- users.export.ids<br>- users.export.segment<br>- email.unsubscribe<br>- email.hard_bounces<br>- messages.schedule_broadcasts<br>- campaigns.list<br>- campaigns.details<br>- canvas.list<br>- canvas.details<br>- segments.list<br>- segments.details<br>- purchases.product_list<br>- events.list<br>- feed.list<br>- feed.details<br>- templates.email.info<br>- templates.email.list<br>- subscription.status.get<br>- subscription.groups.get<br><br>これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| **Braze RESTエンドポイント** | [RESTエンドポイントURL]({{site.baseurl}}/api/basics/#endpoints)。エンドポイントはインスタンスのBraze URLに応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 仕組み {#how-it-works}

StackAdapt Data Hubは、ユーザープロファイル属性を取得するためにBrazeアカウントに直接接続します。これにより、StackAdapt内でBrazeの顧客データを直接活用し、高度なオーディエンスセグメンテーションとアクティベーションを行うことができます。

### データフロー {#data-flow}

1. StackAdaptは、提供されたAPI認証情報を使用してBrazeインスタンスへのセキュアな接続を開始します。
2. StackAdaptはユーザープロファイルデータを取得します。具体的には、選択してマッピングしたプロパティが取得されます。
3. データは正規化されてStackAdapt Data Hubに取り込まれ、セグメンテーションやCampaignsでの利用が可能になります。
4. この統合により、スケジュールされたデータ同期（例：毎日）が可能になり、StackAdaptのオーディエンスをBrazeの最新プロファイルデータで常に最新の状態に保つことができます。

## 同期されるフィールド {#fields-synced}

StackAdaptは、以下を含む（ただしこれらに限定されない）さまざまなBrazeプロファイルフィールドを同期できます。

{% tabs local %}
{% tab Standard attributes %}
- メール
- 生年月日
- 名
- 姓
- 電話番号
- 市区町村
- 国
- 性別
- タイムゾーン
- 作成日時
- External ID
- 言語

{% endtab %}
{% tab Custom attributes %}
アプリやビジネスに固有の属性で、特定のビジネスニーズに基づいて定義されます。

{% endtab %}
{% tab Attribution data %}
- アトリビューション広告
- アトリビューション広告グループ
- アトリビューションCampaign
- アトリビューションソース

{% endtab %}
{% tab Subscription status %}
- メールサブスクリプションステータス
- プッシュサブスクリプションステータス

マーケティングコミュニケーションに対するユーザーの同意（例：メールサブスクリプションステータス）を反映するBrazeのフィールドを正確にマッピングすることは、広告活動がユーザーの設定やプライバシー規制に準拠するために非常に重要です。

{% endtab %}
{% endtabs %}

## 統合のセットアップ {#setting-up-the-integration}

以下のステップに従って、Brazeユーザープロファイルをインポートします。

1. StackAdaptアカウントにログインします。
2. ナビゲーションメニューで**Data Hub**を選択します。
3. **Import Profiles**を選択し、利用可能な統合のリストから**Braze**を選択します。
4. プロンプトが表示されたら、Braze API認証情報を入力します。
- **Braze REST APIキー：** Brazeの**設定** > **APIキー**にあります。セキュリティのベストプラクティスとして、StackAdapt統合用に専用のAPIキーを作成することを推奨します。
- **Brazeアプリキー：** Brazeの**設定** > **APIキー**または**Manage Apps**にあります。
- **Braze RESTエンドポイントURL：** BrazeインスタンスのベースURL（例：`https://rest.iad-01.braze.com`）。
5. **Connect**を選択して認証情報を確認します。

![StackAdaptでのBraze接続設定。]({% image_buster /assets/img/stackadapt/stackadapt_braze_connection_settings.png %})

{: start="6"}
6. 接続を選択し、StackAdaptの広告主を選択します。
7. **Property Mappings**を設定します。StackAdaptが提案するデフォルトマッピングと事前に選択されたプロパティを確認します。
8. （オプション）追加のプロパティをインポートしたい場合は、それぞれのチェックボックスをチェックして選択し、PIIを含むかどうかとデータタイプを指定します。

![StackAdaptでのBrazeプロパティマッピング。]({% image_buster /assets/img/stackadapt/stackadapt_mappings.png %})

{: start="9"}
9. プロファイルを**リスト**に追加するか、新規作成してプロファイルをグループ化およびセグメント化します。
10. **Activate Integration**を選択して、最初のデータ同期を開始します。

## 考慮事項 {#considerations}

- **カスタムイベントとプロパティのインポート：** この機能はまだサポートされていません。
- **データの遅延：** すべてのユーザープロファイルデータのインポートには最大24時間かかる場合があります。
- **同意管理：** Brazeにおけるデータ収集の慣行がプライバシー規制に準拠していること、および顧客データを広告目的で使用するために必要な同意を得ていることを確認してください。StackAdaptは、ソースシステムから渡される同意ステータスに依存しています。
- **属性の一貫性：** データの有効性を最大化するために、StackAdaptに同期する前に、Brazeでの属性の命名方法と入力方法の一貫性を維持してください。