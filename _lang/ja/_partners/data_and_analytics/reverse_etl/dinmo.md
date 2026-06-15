---
nav_title: DinMo
article_title: DinMo
description: "このリファレンス記事では、BrazeとDinMoのパートナーシップについて説明します。DinMoはコンポーザブル顧客データプラットフォームで、リバースETLを使用してデータウェアハウスのデータをBrazeに同期します。"
alias: /partners/dinmo/
page_type: partner
search_tag: Partner

---

# DinMo

> [DinMo](https://www.dinmo.com/)は、リバースETL（Extract, Transform, Load）を通じてクラウドデータウェアハウスをBrazeに接続するコンポーザブル顧客データプラットフォーム（CDP）です。マーケティングチームは、データウェアハウスのデータからオーディエンスSegmentsを構築し、ユーザー属性やイベントをBrazeに同期し、CSVアップロードやエンジニアリングサポートなしでサブスクリプションステータスを最新の状態に保つことができます。

*この統合はDinMoによって管理されています。*

BrazeとDinMoの統合は、Braze REST APIを通じてデータウェアハウスからBrazeにSegmentsとデータモデルをプッシュします。DinMoでBrazeの送信先を接続すると、アクティベーションによってモデルまたはSegmentsからBrazeにデータが送信されます。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| --- | --- |
| DinMoアカウント | このパートナーシップを利用するには、送信先を作成する権限を持つ[DinMoアカウント](https://www.dinmo.com/)が必要です。 |
| Braze REST APIキー | 使用する送信先サービスに必要な[権限](#api-key-permissions)を持つBraze REST APIキー。これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | RESTエンドポイントURL。エンドポイントは[インスタンスのBraze URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)に依存します。 |
| BrazeダッシュボードURL | インスタンスのBrazeダッシュボードURL（例: `https://dashboard.iad-01.braze.com`）。詳細については、[利用可能なSDKエンドポイント]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)を参照してください。 |
| データウェアハウスとデータモデル | 統合を開始する前に、DinMoでデータウェアハウスを接続し、Brazeに同期するデータのモデルまたはSegmentを定義してください。詳細については、[DinMo Braze統合ガイド](https://docs.dinmo.io/integrations/destination-platforms/braze)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}

この統合により、以下のことが可能になります。

* データウェアハウスからBrazeにユーザー属性を同期し、CampaignsやCanvasesをパーソナライズする。
* データウェアハウスのデータからカスタムイベントや購入イベントをBrazeに送信し、行動ターゲティングに活用する。
* DinMoで定義されたオーディエンスSegmentsに合わせて、Brazeのサブスクリプショングループメンバーシップを整合させる。
* DinMoのSegmentsをBrazeユーザー属性としてエクスポートし、それらの属性からBrazeのSegmentsを構築する。

## APIキーの権限 {#api-key-permissions}

使用する送信先サービスに基づいて、Braze REST APIキーに以下の権限を付与してください。

| 権限 | 必要な場面 |
| --- | --- |
| `users.track` | ユーザー属性の同期、トラックイベントの送信、送信先接続の検証 |
| `users.export.ids` | 一括操作のためのユーザーIDエクスポート |
| `users.alias.update` | ユーザーエイリアスの更新 |
| `subscription.status.set` | サブスクリプションステータスの同期 |
| `users.delete` | ミラー同期モードのみ（その他の送信先サービスではオプション） |
{: .reset-td-br-1 .reset-td-br-2 aria-label="APIキーの権限" }

## 統合 {#integration}

### ステップ 1: DinMoでBrazeの送信先を設定する {#step-1-configure-the-braze-destination-in-dinmo}

1. DinMoで、サイドナビゲーションの**Destinations**に移動します。
2. **Add a new destination** > **Connect a new platform** > **Braze**を選択します。
3. 接続フォームに以下の詳細を入力します。
   * **Platform Name**: 例: `Braze – Your Company`
   * **REST API URL**: インスタンスのRESTエンドポイント（例: `https://rest.eu-01.braze.com`）
   * **Dashboard URL**: インスタンスのダッシュボードURL（例: `https://dashboard.eu-01.braze.com`）
   * **API Key**: Brazeからコピーしたキー
4. **Connect**を選択して認証情報を検証します。

{% alert note %}
REST API URLとダッシュボードURLの両方を指定する必要があります。REST API URLの末尾にスラッシュを含めないでください。
{% endalert %}

### ステップ 2: 接続を確認する {#step-2-verify-the-connection}

送信先を保存すると、DinMoはテストコール（例: `users.track`）を実行して、APIキーとエンドポイントが正常に動作することを確認します。

検証に失敗した場合は、以下を確認してください。

* REST API URLが正しく、末尾にスラッシュがないこと。
* APIキーが有効で、必要な権限を持っていること。
* BrazeワークスペースがIP許可リストを使用している場合、DinMoのIPアドレスが含まれていること。

## サポートされている送信先サービス {#supported-destination-services}

DinMoの各送信先サービスは同じ一般的なワークフローに従います。Brazeの送信先を作成し、DinMoのモデルまたはSegmentを構築し、Brazeにデータを送信するアクティベーションを作成します。ステップバイステップのアクティベーションガイダンスについては、[DinMo Braze送信先サービス](https://docs.dinmo.io/integrations/destination-platforms/braze)を参照してください。

以下の送信先サービスが利用可能です。

| 送信先サービス | 説明 |
| --- | --- |
| [ユーザー属性の同期](https://docs.dinmo.io/integrations/destination-platforms/braze/synchronize-users-attributes) | Brazeのユーザープロファイル属性を更新し、オプションで新しいユーザーを挿入します。 |
| [トラックイベントの送信](https://docs.dinmo.io/integrations/destination-platforms/braze/send-track-events) | カスタムイベントと購入イベントをBrazeに送信します。 |
| [サブスクリプションステータスの同期](https://docs.dinmo.io/integrations/destination-platforms/braze/synchronize-subscription-statuses) | DinMoのSegmentメンバーシップに基づいて、Brazeのサブスクリプショングループでユーザーを購読または購読解除します。 |
| [ユーザーリストのエクスポート](https://docs.dinmo.io/integrations/destination-platforms/braze/export-user-lists) | Segmentメンバーシップをbrazeユーザー属性に同期し、Brazeのセグメンテーションで使用します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="サポートされている送信先サービス" }

### ユーザー属性の同期 {#synchronize-user-attributes}

この送信先サービスを使用して、既存のBrazeユーザープロファイルの属性を更新し、オプションで新しいユーザーを挿入します。

アクティベーションを実行すると:

* 挿入モードを有効にした場合、モデル内の新しいユーザーがBrazeに作成されます（UPSERTの動作）。
* 前回のアクティベーション以降に変更された属性値がBrazeで更新されます。

挿入モードを有効にしない場合、DinMoはBrazeに既に存在し、一致するexternal IDを持つユーザーのみを更新します。

アクティベーションのセットアップ中に、DinMoモデル内のユーザーの[external ID]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/)またはBraze IDに対応するフィールドをマッピングします。各DinMoフィールドをBrazeの正確な属性名にマッピングしてください。属性がBrazeに存在しない場合、DinMoが作成します。

ユーザー属性アクティベーションでは、以下の同期モードが利用可能です。

| 同期モード | 説明 |
| --- | --- |
| UPDATE | Brazeに既に存在するユーザーの変更されたレコードを更新します。レコードの挿入や削除は行いません。 |
| UPSERT | 新しいレコードを挿入し、変更されたレコードを更新します。レコードの削除は行いません。 |
| MIRROR | Brazeのレコードをソースと一致するように挿入、更新、削除します。削除操作にはコネクタのサポートが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユーザー属性の同期モード" }

{% alert warning %}
ミラー同期モードは、DinMoソースに存在しなくなったレコードをBrazeから永久に削除します。データウェアハウスが唯一の信頼できるソースであり、削除が意図的な場合にのみミラーモードを使用してください。本番環境でミラー同期を実行する前に、削除ルールを検証してください。
{% endalert %}

### トラックイベントの送信 {#send-track-events}

この送信先サービスを使用して、DinMoのイベントモデルまたはSegmentからBrazeにカスタムイベントまたは購入イベントを送信します。DinMoはカスタムイベントと購入を別々の送信先サービスとして扱います。これは、Brazeが各タイプに異なるAPIを使用するためです。

モデル内の各レコードは単一のイベントタイプ（例: `Purchase`）を表します。DinMoは各アクティベーション実行時に新しいイベントのみを送信し、以前に送信されたイベントは更新しません。

アクティベーションのセットアップ中:

1. Brazeに表示されるべきイベント名を正確に指定します。イベントが存在しない場合、DinMoが作成します。
2. 必須フィールドをマッピングします。
   * **Event time**: イベントが発生したタイムスタンプ
   * **External ID**: イベントに関連付けられたユーザーのexternal ID
3. オプションのイベントプロパティをBrazeの属性名にマッピングします。
4. 新しいイベントがBrazeに送信される頻度のスケジュールを設定します。

### サブスクリプションステータスの同期 {#synchronize-subscription-statuses}

この送信先サービスを使用して、BrazeのサブスクリプショングループをDinMoのSegmentまたはモデルと整合させます。

このサービスをアクティベートする前に:

1. Brazeでターゲットのサブスクリプショングループ（SMSまたはメール）を作成します。
2. そのサブスクリプショングループに所属すべきユーザーを含むDinMoモデルまたはSegmentを構築します。

アクティベーションのセットアップ中に、Brazeの正確なサブスクリプショングループIDを入力します。複数のサブスクリプショングループを同期するには、グループごとに1つのアクティベーションを作成してください。

アクティベーションが実行されると:

* ユーザーがBrazeに既に存在する場合、DinMoのSegmentに参加したユーザーはターゲットのサブスクリプショングループで購読中としてマークされます。
* DinMoのSegmentから離脱したユーザーは、サブスクリプショングループで購読解除としてマークされます。

DinMoは、Segmentに一度も含まれなかったユーザーを変更せず、この送信先サービスでは新しいBrazeユーザーを作成しません。

### ユーザーリストのエクスポート {#export-user-lists}

この送信先サービスを使用して、DinMoのSegmentをBrazeユーザー属性として表現します。Brazeの制限により、DinMoはBrazeリストを直接作成しません。代わりに、Segment内のユーザーのユーザー属性を`true`に設定し、Segmentから離脱したユーザーの属性を`false`に設定します。

アクティベーションのセットアップ中に、オーディエンス名を指定します。DinMoはこの名前をBraze属性として使用します（スペースはアンダースコアに置き換えられます）。同じ名前の属性がBrazeに既に存在しないことを確認してください。ユーザーのexternal IDに対応するDinMoフィールドをマッピングします。

アクティベーションの実行後、同期された属性が`true`に等しいユーザーをフィルタリングするBrazeのSegmentを作成してください。

既存のBrazeユーザーと一致するexternal IDを持つユーザーのみが更新されます。この送信先サービスでは新しいユーザーは作成されません。