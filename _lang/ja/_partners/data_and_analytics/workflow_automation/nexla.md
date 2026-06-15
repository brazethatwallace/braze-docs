---
nav_title: Nexla
article_title: Nexla
description: "このリファレンス記事では、Braze と Nexla のパートナーシップについて説明します。Nexla は統合データ運用プラットフォームであり、Braze Currentsをご利用のお客様はデータレイクデータを抽出、変換し、カスタムフォーマットで他の場所にデータを読み込むことができます。"
alias: /partners/nexla/
page_type: partner
search_tag: Partner

---

# Nexla

> [Nexla](https://www.nexla.com) は統合データ運用分野のリーダーであり、2021年の Gartner Cool Vendor に選出されています。Nexla プラットフォームは、スケーラブルなデータフローを作成するためのツールを提供し、ビジネスチームとデータチームにガバナンスの効いたデータオペレーション、コラボレーション、アジリティを提供します。データを扱うチームは、ノーコード／ローコードの統一されたエクスペリエンスで、あらゆるユースケースのデータを統合、変換、プロビジョニング、監視することができます。

BrazeとNexlaの統合により、[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/)を利用しているお客様は、Nexlaを活用してデータレイクデータを抽出、変換し、カスタムフォーマットで他の場所に読み込むことができ、エコシステム全体でデータに簡単にアクセスできるようになります。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Nexla アカウント | このパートナーシップを活用するには、[Nexla アカウント](https://www.nexla.com/get-demo)が必要です。 |
| Braze REST APIキー | `users.track` 権限を持つ Braze REST APIキー。<br><br> これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze REST エンドポイント  | REST エンドポイントのURL。エンドポイントは、[インスタンスのBraze URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)によって異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}

Nexlaのデータ・アズ・ア・プロダクトである [Nexsets](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information) を使用すると、メタデータを管理することなく、あらゆるフォーマットのデータを扱うことができます。BrazeとのデータフローをNexlaで設定すると、コード不要のツールが数分で利用可能になります。データフローが送信先に設定されると、Nexlaはフローを監視し、任意のデータ量にスケーリングします。

## 統合 {#integration}

### ステップ 1: Nexla アカウントを作成する {#step-1-create-a-nexla-account}

まだ Nexla アカウントをお持ちでない場合は、Nexlaの[Webサイト](https://www.nexla.com)から無料デモとトライアルをリクエストしてください。次に [www.dataops.nexla.io](https://www.dataops.nexla.io) にログオンし、新しい認証情報でサインオンします。

### ステップ 2: ソースを追加する {#step-2-add-your-source}

#### Brazeをデータソースとする場合 {#if-braze-is-your-data-source}
1. Nexla プラットフォームで、左ツールバーの**Flows** > **Create a New Flow**を選択します。
2. **Create New Source**をクリックし、Braze コネクターを選択して、**Next**をクリックします。
3. **Add a New Credential**を選択し、認証情報に名前を付け、Braze APIキーとRESTエンドポイントを追加して、**Save**をクリックします。
4. 最後にデータを選択して**Save**をクリックします。

Nexlaはソースから利用可能なデータを検索し、変換または送信先への送信に使用する [Nexset](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information) を生成します。

#### Brazeが送信先の場合 {#if-braze-is-your-destination}

[Nexlaへのソースの接続](https://nexla.zendesk.com/hc/en-us/sections/115001685927-Create-a-Data-Source)については、Nexlaのドキュメントを参照してください。

### ステップ 3: トランスフォーム（オプション） {#step-3-transform-optional}

データに対してカスタム[変換](https://nexla.zendesk.com/hc/en-us/sections/115001686007-Transformations)を実行したい場合、またはNexlaのビルド済みコネクターを使用したい場合は、データセットの**Transform**ボタンをクリックしてTransform Builderに入ります。Transform Builderの使用に関するガイダンスは[Nexlaのドキュメント](https://nexla.zendesk.com/hc/en-us/articles/360000590468-How-to-Transform-your-Data)を参照してください。

### ステップ 4: 送信先に送信する {#step-4-send-to-destination}

送信先にデータを送信するには、データセットの**Send to Destination**矢印をクリックし、Nexlaの送信先コネクターまたはBraze（ソースが異なる場合）を選択します。認証情報を入力し、送信先オプションを設定して、**Save**をクリックします。データは即座に、指定したフォーマットで選択した送信先に流れ始めます。

## この統合の使用方法 {#using-this-integration}

フローがセットアップされれば、追加の操作は必要ありません。Nexlaはソースデータの変更をすべて処理し、新しいデータへのスケーリングを行い、トリアージのためにスキーマの変更やエラーを通知します。変換、ソース、または送信先を変更する場合は、該当するオプションをクリックして変更を行ってください。Nexlaがフローを即時に更新します。