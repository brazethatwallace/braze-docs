---
nav_title: Convercus
article_title: Convercus
description: "このリファレンス記事では、BrazeとConvercusのパートナーシップについて説明します。Convercusはロイヤルティおよびクーポンプラットフォームで、リアルタイムのロイヤルティデータでBrazeを強化し、Brazeのキャンペーンから Convercusのロイヤルティアクションをトリガーできます。"
page_type: partner
search_tag: Partner
---

# Convercus

> [Convercus](https://www.convercus.com/en)は、SaaS型のロイヤルティおよびクーポンプラットフォームで、オムニチャネルのロイヤルティプログラムやパーソナライズされたクーポンキャンペーンを通じて、ブランドや小売業者の来店頻度、バスケット単価、リピート率の向上を支援します。

_この連携はConvercusによって管理されています。_

## 連携について {#about-the-integration}

BrazeとConvercusの連携は双方向です。ロイヤルティデータはカスタム属性、カスタムイベント、購入データとしてリアルタイムでBrazeに流れ込み、Brazeのキャンバスやキャンペーンはwebhookを通じてConvercusのロイヤルティアクションをトリガーできます。同期された会員ティア、ポイント残高、購入履歴、クーポンアクティビティをセグメント、Liquid、Connected Contentで活用できます。Brazeのジャーニーからは、クーポンの割り当て、ポイントトランザクションの記帳・獲得・消費、Convercusでのメール購読設定の更新も可能です。

Convercusが連携をホストするため、追加のインフラをインストールする必要はありません。多くのロイヤルティコネクターがデータを一方向にプッシュするだけなのに対し、Convercusはループを閉じます。Brazeでロイヤルティイベントに反応し、Convercusでアクションを実行し、その結果をBrazeで測定できます。

## ユースケース {#use-cases}

* **ティアアップのお祝い:** Convercusでメンバーがロイヤルティティアを昇格した際に、ウェルカムメッセージ、ティア限定特典、メンバーの新しいティアとポイント残高を含むパーソナライズされたBrazeキャンバスをトリガーします。
* **誕生日やマイルストーンのボーナス:** Brazeジャーニーから、メンバーの誕生日や記念日にConvercusでボーナスポイントを付与し、新しい残高を確認するお祝いメッセージを送信します。
* **休眠メンバーの奪還:** 非アクティブなメンバーに対して、BrazeからWebhookを通じてConvercusでパーソナライズされたクーポンを割り当て、メール、プッシュ、アプリ内メッセージで配信します。
* **メッセージングでのリアルタイムポイント残高:** Connected Contentを使用してメンバーのリアルタイムポイント残高をBraze Liquidに取り込み、「次のリワードまであとXポイント」のようなケイデンスを実現します。

## 前提条件 {#prerequisites}

始める前に、以下が必要です。

| 前提条件 | 説明 |
| --- | --- |
| Convercus アカウント | アクティブな Convercus プログラム。まだ顧客でない場合は、Convercus のアカウントマネージャーにお問い合わせください。 |
| Braze REST APIキー | `users.track` 権限を持つ Braze REST APIキー。Braze ダッシュボードの**設定** > **API キー**からこのキーを作成します。 |
| Braze REST エンドポイント | [REST エンドポイント URL]({{site.baseurl}}/api/basics#endpoints)。エンドポイントは、お使いのインスタンスの Braze URL によって異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

システム間で一貫したユーザー識別子が必要です。Braze で `external_id`（または選択した識別子タイプ）として使用される値は、Convercus の対応するメンバー識別子と一致する必要があります。一致しない場合、イベントは正しいプロファイルに紐付けられません。

## 統合 {#integration}

### ステップ1：Convercus Selfservice で Braze を設定する {#step-1-configure-braze-in-convercus-selfservice}

Convercus Selfservice（顧客向け管理 UI — Convercus のアカウントマネージャーから提供される URL で開きます）で、Braze に接続するプログラムを開き、**Braze integration card** を使用して以下を行います。

1. 統合フォームに入力して Braze 接続を設定します。

   | フィールド | 説明 |
   | --- | --- |
   | `apiKey` | Braze REST APIキー（`users.track` 権限付き）。 |
   | `apiEndpoint` | Braze REST エンドポイント。例: `https://rest.iad-01.braze.com`。 |
   | Identifier type | `external_id` または `user_alias`。Convercus メンバーを Braze ユーザープロファイルにどのようにマッチングするかを決定します。 |
   | `defaultOptins` | プログラムのオプトインチャネル（`membershipOptins` から）の複数選択。メールサブスクリプション Webhook でリクエストに `optins` が含まれない場合のデフォルトとして使用されます。少なくとも1つが選択されるまで、Braze 設定は不完全として扱われます。 |
   {: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ1：Convercus Selfservice で Braze を設定する" }

2. インバウンドコール用の API キーを作成します。プログラムごとの `X-Convercus-Key` 認証情報を作成します。生のキーは作成時に一度だけ表示され、`cvc_` がプレフィックスとして付きます（形式: `cvc_<base64url>`）。ステップ2で Webhook キャンペーンと Connected Content ブロックを設定する際に、このキーを Braze に保存してください。キーは同じカードからいつでも取り消すことができ、取り消しは即座に有効になります。

Braze 接続を保存すると、Convercus はそのプログラムのロイヤルティイベントを直ちに Braze へストリーミングし始めます。追加のインフラ設定は不要です。

{% alert note %}
各 Convercus プログラムは独立して設定されます。1つの Convercus テナントで、異なるプログラムを異なる Braze ワークスペースに接続でき、それぞれ独自の API キーを持ちます。
{% endalert %}

### ステップ2：Braze で Webhook を設定する {#step-2-configure-webhooks-in-braze}

キャンバスやキャンペーンから Convercus アクションをトリガーするには、Convercus 統合サービスを呼び出す Braze Webhook アクションを作成します。すべてのリクエストには以下のヘッダーを含める必要があります。

- `X-Convercus-Key: cvc_…` - ステップ1で生成した API キー。
- `Content-Type: application/json`

すべてのエンドポイントはベース URL `<SERVICE_HOST>/v1/programs/{programId}` 配下にあります。`<SERVICE_HOST>` を Convercus のアカウントマネージャーから提供されたホストに、`{programId}` を Convercus プログラム ID に置き換えてください。

| アクション | エンドポイント |
| --- | --- |
| メンバーにクーポンを割り当てる | `POST /campaigns/{couponId}/assign` — `{ "couponCode": "..." }` を返します。 |
| 複数のメンバーにクーポンを割り当てる | `POST /campaigns/{couponId}/assign/batch` — 1回のコールで最大500メンバー。ボディにはオプションの `valid_from` / `valid_to` を指定できます。`{ "batchId": "..." }` を返します。 |
| ポイントの獲得/消費を記録する | `POST /members/{accountId}/bookings` — メンバーアカウントに `EARNBOOKING` または `BURNBOOKING` を作成します。`{ "bookingId": "..." }` を返します。 |
| メール購読設定を同期する | `POST /subscriptions/email` — メンバーのオプトインを `allowed` または `declined` に設定します。オプトインチャネルはリクエストの `optins` > `defaultOptins` の順で解決されます。`200`（すべて成功）、`207`（部分的 — `succeeded` / `failed` を参照）、または `400`（不明なオプトインまたは未設定）を返します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ2：Braze で Webhook を設定する" }

例 — メンバーにクーポンを割り当てる:

{% raw %}
```text
POST <SERVICE_HOST>/v1/programs/{programId}/campaigns/{couponId}/assign
X-Convercus-Key: cvc_…
Content-Type: application/json

{
  "account_id": "{{custom_attribute.${convercus_account_id}}}",
  "braze_campaign_id": "{{campaign.${api_id}}}"
}
```
{% endraw %}

他のアクションも同じパターンに従い、エンドポイントとボディのみが変わります。例えば、ポイント記録は `/members/{accountId}/bookings` に `booking_type`（`EARNBOOKING` または `BURNBOOKING`）、`booking_type_code`、`points`、`reason` を含めて POST します。メール購読 Webhook は `/subscriptions/email` に `account_id` と `status`（`allowed` または `declined`）を含めて POST します。

#### エラーレスポンスとリトライ {#error-responses-and-retries}

| ステータス | 意味 |
| --- | --- |
| `200` | 成功。 |
| `207` | Multi-Status — メール購読 Webhook のみ。一部のメンバーシップが更新され、他が失敗した場合。 |
| `400` | リクエストボディのバリデーションに失敗しました。 |
| `401` | `X-Convercus-Key` が欠落しているか無効です。 |
| `5xx` | アップストリームの Convercus コールが失敗しました。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="エラーレスポンスとリトライ" }

{% alert warning %}
5xx レスポンスは、成功を確認せずにリトライするのは安全ではありません。これらの操作はべき等ではなく、リトライによりクーポンの二重割り当てやポイント記録の二重計上が発生する可能性があります。これらの Webhook では Braze の 5xx 自動リトライを無効にするか、最大リトライ回数を非常に低く設定してください。
{% endalert %}

### ステップ3：Braze でデータを検証する {#step-3-verify-data-in-braze}

1. Convercus でロイヤルティイベントをトリガーします。例えば、ステータスレベルの変更、ポイントトランザクション、クーポンの引き換えなどです。
2. Braze で該当するユーザーを開き、期待されるカスタム属性、カスタムイベント、または購入がプロファイルに表示されることを確認します。ユーザーは `external_id`（またはステップ1で選択した識別子タイプ）でマッチングされます。
3. 逆方向を検証するには、ステップ2の Webhook のいずれかを呼び出す Braze テスト送信を実行し、Convercus でアクション（クーポンの割り当て、ポイントの記録、または購読の更新）を確認します。

## Braze での Convercus の使用 {#use-convercus-with-braze}

### ステップ1: 同期されたロイヤルティデータでメッセージをパーソナライズする {#step-1-personalize-messages-with-synced-loyalty-data}

インテグレーションが稼働すると、Convercus のイベントは [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) エンドポイントを通じて Braze の各ユーザープロファイルに届き、他のネイティブデータと同様に使用できます。

1. ロイヤルティのカスタム属性（例: `convercus_status_level`、`convercus_balance`）をセグメントで使用して、ティア保有者、高残高メンバー、または最近ダウングレードされたユーザーをターゲットにします。
2. カスタムイベント（例: `convercus_status_level_changed`、クーポンおよびメンバーシップイベント）をキャンバスの**トリガーステップ**として、またはリエンゲージメントキャンペーンのフィルターとして使用します。
3. これらのフィールドを **Liquid** で参照して、メッセージ内のパーソナライゼーション（件名、本文、プッシュタイトル）に活用します。
4. Convercus からストリーミングされた `purchase` イベントを使用して、商品に基づいたジャーニー（補充、カテゴリアップセル、購入後レビューリクエスト）を推進します。

#### カスタム属性 {#custom-attributes}

| 属性 | 説明 |
| --- | --- |
| `convercus_account_id` | メンバーの Convercus アカウント ID — Convercus プログラム / Braze ワークスペース内で一意です。 |
| `convercus_user_id` | 複数の Convercus プログラムにまたがる基盤となる人物を識別する Convercus ユーザー ID です。 |
| `convercus_partner_id` | このメンバーが登録した Convercus パートナー（加盟店/ブランド）の識別子です。コアリションプログラムでのセグメンテーションに役立ちます。 |
| `convercus_member_role` | ロイヤルティプログラム内でのメンバーの役割です。 |
| `convercus_status_level` | メンバーの現在のティアまたはステータスレベルです。 |
| `convercus_balance` | メンバーの現在の `points`、`lockedPoints`、`statusPoints` を含むオブジェクトです。 |
| `email_subscribe` | Convercus のオプトインから導出されたメール購読状態（`opted_in`、`subscribed`、または `unsubscribed`）です。 |
| `push_subscribe` | Convercus のプッシュトークンイベントから導出されたプッシュ購読状態（`opted_in` または `unsubscribed`）です。 |
| 標準プロファイルフィールド | `email`、`phone`、`first_name`、`last_name`、`dob`、`gender`、`home_city`、`country`。 |
| カスタムユーザープロパティ | Convercus ユーザーオブジェクトに定義されたカスタムプロパティは、Braze のカスタム属性として転送されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="カスタム属性" }

{% alert note %}
Braze ワークスペース内では、メンバーは `convercus_account_id` によって一意に識別されます。`convercus_user_id` は複数の Convercus プログラムにまたがる基盤となる人物を識別し、クロスプログラム分析のために提供されます。Braze 内でのセグメンテーションには `convercus_account_id` を使用してください。
{% endalert %}

**`email_subscribe` のマッピング**

| Convercus の状態 | Braze の `email_subscribe` |
| --- | --- |
| `email consent` または `newsletter` の `allowedOptins` エントリ | `opted_in` |
| それらのチャネルの `declinedOptIns` エントリ（許可エントリなし） | `unsubscribed` |
| いずれの記録もなし | `subscribed`（Braze のニュートラルなデフォルト） |
{: .reset-td-br-1 .reset-td-br-2 aria-label="カスタム属性" }

#### カスタムイベント {#custom-events}

| イベント | トリガー条件 |
| --- | --- |
| `convercus_account_created` | Convercus で新しいアカウントが作成されたとき。 |
| `convercus_membership_added` | 既存のアカウントがロイヤルティプログラムに参加したとき。 |
| `convercus_membership_created` | 新しいメンバーシップが作成されたとき。 |
| `convercus_membership_changed` | メンバーシップのデータが変更されたとき。 |
| `convercus_membership_optins_changed` | メンバーのオプトイン設定が変更されたとき。 |
| `convercus_membership_terminated` | メンバーシップが終了したとき。 |
| `convercus_status_level_changed` | メンバーのティアまたはステータスレベルが変更されたとき。 |
| `convercus_balance_changed` | メンバーのポイント残高が変更されたとき。 |
| `convercus_account_transaction` | ロイヤルティトランザクションが評価されたとき。 |
| `convercus_coupon_assigned` | メンバーにクーポンが割り当てられたとき。 |
| `convercus_coupon_redeemed` | メンバーがクーポンを利用したとき。 |
| `convercus_user_logged_in` | メンバーが Convercus を利用したサーフェスにサインインしたとき。 |
| `convercus_user_logged_out` | メンバーがサインアウトしたとき。 |
| `convercus_user_created` | 新しいユーザーが作成されたとき。 |
| `convercus_user_changed` | ユーザーのプロファイルデータが変更されたとき。 |
| `convercus_push_token_created` | メンバーのプッシュトークンが登録されたとき。 |
| `convercus_push_token_deleted` | プッシュトークンが削除されたとき。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="カスタムイベント" }

#### 購入 {#purchases}

タイプ `EARNTRANSACTION`（顧客の支出から獲得したポイント）の Convercus トランザクションは、Braze に[購入]({{site.baseurl}}/api/objects_filters/purchase_object)として報告され、Braze の収益分析、RFM セグメンテーション、予測機能でカウントされます。トランザクション ID を商品識別子として、トランザクション金額と通貨を価格と通貨として使用します。

タイプ `PAYWITHPOINTSTRANSACTION`（ポイント消費）のトランザクションは購入として報告**されません**。これらは `convercus_account_transaction` カスタムイベントとして流れるため、セグメンテーションに引き続き利用できます。獲得トランザクションの取り消しやキャンセルは、マイナス価格の購入として報告され、Braze の収益を Convercus と整合させます。

### ステップ2: Connected Content でリアルタイムのロイヤルティデータを取得する {#step-2-fetch-live-loyalty-data-with-connected-content}

送信時に最新である必要がある値（現在のポイント残高、有効なクーポン、最新のティアなど）については、最後に同期された属性に頼るのではなく、[Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) を使用して Braze から Convercus を呼び出します。両方のエンドポイントは Webhook と同じベース URL の下にあり、`X-Convercus-Key` ヘッダーが必要です。

| データ | エンドポイント | 返却内容 |
| --- | --- | --- |
| メンバープロファイル | `GET /members/{accountId}/profile` | `member_id`、`first_name`、`last_name`、`email`、`tier_name`、`tier_id`、`points_balance`、`enrollment_date`。 |
| メンバークーポン | `GET /members/{accountId}/coupons` | 有効で利用可能なクーポンのリスト（ステータス、値、有効期間、タイトル、説明）。`?lang=<code>`（例: `?lang=de`）を追加すると `title`/`description` がローカライズされます。デフォルトは `en` です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ2: Connected Content でリアルタイムのロイヤルティデータを取得する" }

Connected Content エンドポイントは、予期されるエラーの場合でも常に HTTP 200 を返すため、Liquid テンプレートで `error` フィールドに基づいて分岐できます。

| レスポンス | 意味 |
| --- | --- |
| `200` + ペイロード | 成功。 |
| `200 { "error": "member_not_found" }` | このプログラムにアカウントが存在しません。 |
| `200 { "error": "internal_error" }` | アップストリームまたは予期しないエラーです。 |
| `401` | `X-Convercus-Key` が欠落しているか無効です（Liquid ではなくインテグレーション時に対処してください）。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ2: Connected Content でリアルタイムのロイヤルティデータを取得する" }

例 — メンバーのロイヤルティステータス（ティア、ポイント、有効なオファー）をレンダリングする:

{% raw %}
```liquid
{% connected_content
  https://<SERVICE_HOST>/v1/programs/{programId}/members/{{custom_attribute.${convercus_account_id}}}/profile
  :headers { "X-Convercus-Key": "cvc_…" }
  :content_type application/json
  :cache_max_age 300
  :retry
  :save member
%}

{% connected_content
  https://<SERVICE_HOST>/v1/programs/{programId}/members/{{custom_attribute.${convercus_account_id}}}/coupons?lang=en
  :headers { "X-Convercus-Key": "cvc_…" }
  :content_type application/json
  :cache_max_age 0
  :retry
  :save coupon_data
%}

{% unless member.error %}
  <h2>Your Loyalty Status</h2>
  <p>Hi {{member.first_name}}, you're a <strong>{{member.tier_name}}</strong> member.</p>
  <p>Points balance: <strong>{{member.points_balance}}</strong></p>

  {% if coupon_data.coupons.size > 0 %}
    <h3>Your Active Offers</h3>
    {% for coupon in coupon_data.coupons %}
      <p><strong>{{coupon.title}}</strong> — valid until {{coupon.valid_to}}</p>
    {% endfor %}
  {% endif %}
{% endunless %}
```
{% endraw %}

Connected Content は常に条件分岐でラップしてください（`member.error` と空の `coupons` をチェック）。これにより、一時的なルックアップ失敗が壊れたメッセージを送信することを防ぎます。プロファイルはキャッシュし（`cache_max_age 300`）、クーポンはキャッシュしないでください（`cache_max_age 0`）。クーポンのステータスは送信間で変わる可能性があるためです。

## 考慮事項 {#considerations}

- **レイテンシ:** Convercus から Braze へのイベントは Kafka を経由して伝播し、通常の負荷であれば数秒で Braze に到達します。
- **Braze のレート制限:** このインテグレーションは `429` レスポンスに対して自動的にリトライし、Braze の `x-ratelimit-retry-after` ヘッダーに従って指数バックオフを行います。
- **Connected Content のキャッシュ:** Braze はデフォルトで Connected Content のレスポンスを数分間キャッシュします。送信時に正確な値が必要な場合（ポイント残高など）は、Connected Content の呼び出しでキャッシュウィンドウを短縮するかバイパスしてください。
- **プログラムごとに1つの設定:** 各ロイヤルティプログラムは1つの Braze ワークスペースにマッピングされます。2つ目のワークスペースを接続するには、別のプログラムで設定してください。
- **オブザーバビリティ:** プログラムごとの API 呼び出し統計とエラー履歴（双方向）は90日間保持され、Selfservice の Braze インテグレーションカードから確認できます。

## トラブルシューティング {#troubleshooting}

- **イベントがBrazeに表示されない:** 識別子として使用した値（ステップ1で選択）が、Brazeのユーザーの`external_id`（または選択した識別子タイプ）と一致していることを確認してください。識別子が一致しない場合、イベントが誤ったプロファイルに紐付けられたり、ドロップされたりします。
- **Webhookが`401`を返す:** `X-Convercus-Key`ヘッダーが欠落しているか、`cvc_…` APIキーが失効しています。Selfserviceでキーを再生成し、BrazeのWebhookアクションを更新してください。
- **Webhookが`400`を返す:** リクエストに`Content-Type: application/json`が含まれていないか、ペイロードがドキュメントに記載されたスキーマと一致していません。メール購読Webhookの場合、`400`はリクエストされたオプトインがプログラムに認識されていないか、設定されていないことも意味します。
- **詳細なデバッグ:** SelfserviceのBrazeインテグレーションカードで、プログラムごとのAPI呼び出し統計とエラー履歴を確認するか、Convercusの担当者にお問い合わせください。