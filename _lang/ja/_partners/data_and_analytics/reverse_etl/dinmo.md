---
nav_title: DinMo
article_title: DinMo
description: "このリファレンス記事では、BrazeとDinMoのパートナーシップについて説明します。DinMoはコンポーザブル顧客データプラットフォームで、リバースETLを使用してデータウェアハウスのデータをBrazeに同期します。"
alias: /partners/dinmo/
page_type: partner
search_tag: Partner

---

# DinMo

> [DinMo](https://www.dinmo.com/)は、リバースETL（Extract, Transform, Load）を通じてクラウドデータウェアハウスをBrazeに接続するコンポーザブル顧客データプラットフォーム（CDP）です。マーケティングチームは、データウェアハウスのデータからオーディエンスセグメントを構築し、ユーザー属性やイベントをBrazeに同期し、CSVアップロードや開発サポートなしで購読ステータスを最新の状態に保つことができます。

_この統合はDinMoによって管理されています。_

BrazeとDinMoの統合は、Braze REST APIを通じてデータウェアハウスからBrazeにセグメントとデータモデルをプッシュします。DinMoでBrazeの送信先を接続すると、アクティベーションによってモデルまたはセグメントからBrazeにデータが送信されます。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| --- | --- |
| DinMo アカウント | このパートナーシップを活用するには、送信先を作成する権限を持つ [DinMo アカウント](https://www.dinmo.com/)が必要です。 |
| Braze REST APIキー | 使用予定の送信先サービスに必要な[権限](#api-key-permissions)を持つ Braze REST APIキー。これは Braze ダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze REST エンドポイント | REST エンドポイント URL。エンドポイントは、Braze インスタンスの [API エンドポイント]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints)に応じて異なります。 |
| Braze ダッシュボード URL | お使いのインスタンスの Braze ダッシュボード URL（例: `https://dashboard.iad-01.braze.com`）。詳細については、[利用可能なSDKエンドポイント]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)を参照してください。 |
| データウェアハウスとデータモデル | インテグレーションを開始する前に、DinMo でデータウェアハウスを接続し、Braze に同期するデータのモデルまたはセグメントを定義してください。詳細については、[DinMo Braze インテグレーションガイド](https://docs.dinmo.io/integrations/destination-platforms/braze)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}

この連携により、以下のことが可能です。

* データウェアハウスのユーザー属性をBrazeに同期し、キャンペーンやキャンバスをパーソナライズできます。
* データウェアハウスのデータからカスタムイベントや購入イベントをBrazeに送信し、行動ベースのターゲティングに活用できます。
* Brazeの購読グループメンバーシップを、DinMoで定義されたオーディエンスセグメントと整合させることができます。
* DinMoのセグメントをBrazeのユーザー属性としてエクスポートし、それらの属性からBrazeのセグメントを構築できます。

## APIキーの権限 {#api-key-permissions}

使用する送信先サービスに基づいて、Braze REST APIキーに以下の権限を付与してください。

| 権限 | 必要な用途 |
| --- | --- |
| `users.track` | ユーザー属性の同期、トラックイベントの送信、送信先接続の検証 |
| `users.export.ids` | 一括操作のためのユーザーIDのエクスポート |
| `users.alias.update` | ユーザーエイリアスの更新 |
| `subscription.status.set` | 購読ステータスの同期 |
| `users.delete` | ミラー同期モードのみ（その他の送信先サービスではオプション） |
{: .reset-td-br-1 .reset-td-br-2 aria-label="APIキーの権限" }

## インテグレーション {#integration}

### ステップ1：DinMoでBrazeの送信先を設定する {#step-1-configure-the-braze-destination-in-dinmo}

1. DinMoで、サイドナビゲーションの**送信先**に移動します。
2. **新しい送信先を追加** > **新しいプラットフォームを接続** > **Braze**を選択します。
3. 接続フォームに以下の情報を入力します：
   * **プラットフォーム名**：例：`Braze – Your Company`
   * **REST API URL**：インスタンスのRESTエンドポイント（例：`https://rest.eu-01.braze.com`）
   * **ダッシュボードURL**：インスタンスのダッシュボードURL（例：`https://dashboard.eu-01.braze.com`）
   * **APIキー**：Brazeからコピーしたキー
4. **接続**を選択して認証情報を検証します。

{% alert note %}
REST API URLとダッシュボードURLの両方を指定する必要があります。REST API URLの末尾にスラッシュを含めないでください。
{% endalert %}

### ステップ2：接続を確認する {#step-2-verify-the-connection}

送信先を保存すると、DinMoはテスト呼び出し（例：`users.track`）を実行し、APIキーとエンドポイントが正常に機能するか確認します。

検証に失敗した場合は、以下を確認してください：

* REST API URLが正しく、末尾にスラッシュが含まれていないこと。
* APIキーが有効で、必要な権限が付与されていること。
* Brazeワークスペースで IP 許可リストを使用している場合、DinMoのIPアドレスが含まれていること。

## サポートされている送信先サービス {#supported-destination-services}

DinMoの各送信先サービスは、同じ一般的なワークフローに従います。Brazeの送信先を作成し、DinMoモデルまたはセグメントを構築し、アクティベーションを作成してBrazeにデータを送信します。ステップバイステップのアクティベーションガイダンスについては、[DinMo Braze送信先サービス](https://docs.dinmo.io/integrations/destination-platforms/braze)を参照してください。

以下の送信先サービスが利用可能です。

| 送信先サービス | 説明 |
| --- | --- |
| [ユーザー属性の同期](https://docs.dinmo.io/integrations/destination-platforms/braze/synchronize-users-attributes) | Brazeのユーザープロファイル属性を更新し、オプションで新しいユーザーを挿入します。 |
| [トラックイベントの送信](https://docs.dinmo.io/integrations/destination-platforms/braze/send-track-events) | カスタムイベントおよび購入イベントをBrazeに送信します。 |
| [購読ステータスの同期](https://docs.dinmo.io/integrations/destination-platforms/braze/synchronize-subscription-statuses) | DinMoセグメントのメンバーシップに基づいて、Brazeの購読グループでユーザーを購読または購読解除します。 |
| [ユーザーリストのエクスポート](https://docs.dinmo.io/integrations/destination-platforms/braze/export-user-lists) | セグメントメンバーシップをBrazeユーザー属性に同期し、Brazeのセグメンテーションで使用します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="サポートされている送信先サービス" }

### ユーザー属性の同期 {#synchronize-user-attributes}

この送信先サービスを使用して、既存のBrazeユーザープロファイルの属性を更新し、オプションで新しいユーザーを挿入します。

アクティベーションを実行すると、以下のようになります。

* 挿入モードを有効にすると、モデル内の新しいユーザーがBrazeに作成されます（UPSERTの動作）。
* 前回のアクティベーション以降に変更された属性値がBrazeで更新されます。

挿入モードを有効にしない場合、DinMoはBrazeにすでに存在し、一致するexternal IDを持つユーザーのみを更新します。

アクティベーションの設定時に、ユーザーの[external ID]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web)またはBraze IDに対応するDinMoモデルのフィールドをマッピングします。各DinMoフィールドをBrazeの正確な属性名にマッピングします。属性がBrazeに存在しない場合、DinMoがその属性を作成します。

ユーザー属性アクティベーションでは、以下の同期モードが利用可能です。

| 同期モード | 説明 |
| --- | --- |
| UPDATE | Brazeにすでに存在するユーザーの変更されたレコードを更新します。レコードの挿入や削除は行いません。 |
| UPSERT | 新しいレコードを挿入し、変更されたレコードを更新します。レコードの削除は行いません。 |
| MIRROR | Brazeのレコードを挿入、更新、削除してソースをミラーリングします。削除操作にはコネクタのサポートが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユーザー属性の同期モード" }

{% alert warning %}
ミラー同期モードは、DinMoソースに存在しなくなったレコードをBrazeから完全に削除します。ミラーモードは、データウェアハウスが信頼できる唯一の情報源であり、削除が意図的である場合にのみ使用してください。本番環境でミラー同期を実行する前に、削除ルールを検証してください。
{% endalert %}

### トラックイベントの送信 {#send-track-events}

この送信先サービスを使用して、DinMoイベントモデルまたはセグメントからBrazeにカスタムイベントまたは購入イベントを送信します。Brazeはタイプごとに異なるAPIを使用するため、DinMoはカスタムイベントと購入を別の送信先サービスとして扱います。

モデル内の各レコードは、単一のイベントタイプ（例: `Purchase`）を表します。DinMoは各アクティベーション実行時に新しいイベントのみを送信し、以前に送信したイベントを更新することはありません。

アクティベーションの設定時に、以下を行います。

1. Brazeに表示されるべきイベント名を正確に指定します。イベントが存在しない場合、DinMoがそのイベントを作成します。
2. 必須フィールドをマッピングします。
   * **イベント時刻**: イベントが発生したタイムスタンプ
   * **External ID**: イベントに関連付けられたユーザーのexternal ID
3. オプションのイベントプロパティをBrazeの属性名にマッピングします。
4. 新しいイベントがBrazeに送信される頻度のスケジュールを設定します。

### 購読ステータスの同期 {#synchronize-subscription-statuses}

この送信先サービスを使用して、Brazeの購読グループをDinMoセグメントまたはモデルと同期させます。

このサービスを有効化する前に、以下を行います。

1. Brazeでターゲットの購読グループ（SMSまたはメール）を作成します。
2. その購読グループに属するべきユーザーを含むDinMoモデルまたはセグメントを構築します。

アクティベーションの設定時に、Brazeの正確な購読グループIDを入力します。複数の購読グループを同期するには、グループごとに1つのアクティベーションを作成します。

アクティベーションが実行されると、以下のようになります。

* ユーザーがすでにBrazeに存在する場合、DinMoセグメントに参加したユーザーはターゲットの購読グループに購読済みとしてマークされます。
* DinMoセグメントから離脱したユーザーは、購読グループから購読解除としてマークされます。

DinMoは、セグメントに一度も含まれなかったユーザーを変更せず、この送信先サービスで新しいBrazeユーザーを作成することもありません。

### ユーザーリストのエクスポート {#export-user-lists}

この送信先サービスを使用して、DinMoセグメントをBrazeユーザー属性として表現します。Brazeの制限により、DinMoはBrazeリストを直接作成しません。代わりに、セグメント内のユーザーにはユーザー属性を`true`に設定し、セグメントから離脱したユーザーには`false`に設定します。

アクティベーションの設定時に、オーディエンス名を指定します。DinMoはこの名前をBraze属性として使用します（スペースはアンダースコアに置き換えられます）。同じ名前の属性がBrazeにまだ存在しないことを確認してください。ユーザーのexternal IDに対応するDinMoフィールドをマッピングします。

アクティベーションの実行後、同期された属性が`true`に等しいユーザーをフィルタリングするBrazeセグメントを作成します。

既存のBrazeユーザーと一致するexternal IDを持つユーザーのみが更新されます。この送信先サービスでは新しいユーザーは作成されません。