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

BrazeとConvercusの連携は双方向です。ロイヤルティデータはカスタム属性、カスタムイベント、購入データとしてリアルタイムでBrazeに取り込まれ、Brazeのキャンバスやキャンペーンはwebhookを通じてConvercusのロイヤルティアクションをトリガーできます。同期された会員ティア、ポイント残高、購入履歴、クーポンアクティビティをセグメント、Liquid、Connected Contentで活用できます。Brazeのジャーニーからは、クーポンの割り当て、ポイント取引の記帳・獲得・消費、Convercusでのメール購読設定の更新も行えます。

Convercusが連携をホストするため、追加のインフラを導入する必要はありません。多くのロイヤルティコネクターがデータを一方向にしかプッシュしないのに対し、Convercusはループを閉じます。Brazeでロイヤルティイベントに反応し、Convercusでアクションを実行し、その結果をBrazeで測定できます。

## ユースケース {#use-cases}

* **ティアアップのお祝い：** Convercusでメンバーがロイヤルティティアを昇格した際に、ウェルカムメッセージ、ティア限定の特典、メンバーの新しいティアとポイント残高を含むパーソナライズされたBrazeキャンバスをトリガーします。
* **誕生日やマイルストーンのボーナス：** Brazeジャーニーから、メンバーの誕生日や記念日にConvercusでボーナスポイントを付与し、新しい残高を確認するお祝いメッセージを送信します。
* **休眠メンバーの奪還：** 非アクティブなメンバーに対して、BrazeからWebhookを通じてConvercusでパーソナライズされたクーポンを割り当て、メール、プッシュ、アプリ内メッセージで配信します。
* **メッセージングでのリアルタイムポイント残高：** Connected Contentを使用してメンバーのリアルタイムポイント残高をBraze Liquidに取り込み、「次のリワードまであとXポイント」といったケイデンスに活用します。

## 前提条件 {#prerequisites}

始める前に、以下が必要です。

| 前提条件 | 説明 |
| --- | --- |
| Convercus アカウント | アクティブな Convercus プログラム。まだ顧客でない場合は、Convercus のアカウントマネージャーにお問い合わせください。 |
| Braze REST APIキー | `users.track` 権限を持つ Braze REST APIキー。Braze ダッシュボードの**設定** > **APIキー**からこのキーを作成します。 |
| Braze REST エンドポイント | [REST エンドポイント URL]({{site.baseurl}}/api/basics#endpoints)。エンドポイントは、お使いのインスタンスの Braze URL に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

システム間で一貫したユーザー識別子が必要です。Braze で `external_id`（または選択した識別子タイプ）として使用される値は、Convercus の対応するメンバー識別子と一致している必要があります。一致しない場合、イベントは正しいプロファイルに紐付けられません。

## インテグレーション {#integration}

### ステップ1: Convercus SelfserviceでBrazeを設定する {#step-1-configure-braze-in-convercus-selfservice}

Convercus Selfservice（顧客向けの管理UI。Convercusのアカウントマネージャーが提供するURLから開きます）で、Brazeに接続したいプログラムを開き、**Braze integration カード**を使用して以下を行います。

1. 統合フォームに入力してBraze接続を設定します。

   | フィールド | 説明 |
   | --- | --- |
   | `apiKey` | Braze REST APIキー（`users.track`権限付き）。 |
   | `apiEndpoint` | Braze RESTエンドポイント（例: `https://rest.iad-01.braze.com`）。 |
   | Identifier type | `external_id`または`user_alias`のいずれか。Convercusメンバーをどのようにしてbrazeユーザープロファイルとマッチングするかを決定します。 |
   | `defaultOptins` | プログラムのオプトインチャネル（`membershipOptins`から）の複数選択。メールサブスクリプションWebhookでリクエストに`optins`が含まれていない場合のデフォルトとして使用されます。少なくとも1つが選択されるまで、Braze設定は不完全として扱われます。 |
   {: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ1: Convercus SelfserviceでBrazeを設定する" }

2. インバウンドコール用のAPIキーを作成します。プログラムごとの`X-Convercus-Key`認証情報を作成します。生キーは作成時に一度だけ表示され、`cvc_`のプレフィックスが付きます（形式: `cvc_<base64url>`）。ステップ2でWebhookキャンペーンとConnected Contentブロックを設定する際に、このキーをBrazeに保存してください。キーは同じカードからいつでも取り消すことができ、取り消しは即座に有効になります。

Braze接続を保存すると、ConvercusはそのプログラムのロイヤルティイベントをBrazeへ即座にストリーミングし始めます。追加のインフラ設定は不要です。

{% alert note %}
各Convercusプログラムは独立して設定されます。1つのConvercusテナントで、異なるプログラムをそれぞれ独自のAPIキーで異なるBrazeワークスペースに接続できます。
{% endalert %}

### ステップ2: BrazeでWebhookを設定する {#step-2-configure-webhooks-in-braze}

キャンバスまたはキャンペーンからConvercusアクションをトリガーするには、Convercus統合サービスを呼び出すBraze Webhookアクションを作成します。すべてのリクエストには以下のヘッダーを含める必要があります。

- `X-Convercus-Key: cvc_…` - ステップ1で生成されたAPIキー。
- `Content-Type: application/json`

すべてのエンドポイントはベースURL `<SERVICE_HOST>/v1/programs/{programId}` 配下にあります。`<SERVICE_HOST>`をConvercusのアカウントマネージャーが提供するホストに、`{programId}`をConvercusプログラムIDに置き換えてください。

| アクション | エンドポイント |
| --- | --- |
| メンバーにクーポンを割り当てる | `POST /campaigns/{couponId}/assign` — `{ "couponCode": "..." }` を返します。 |
| 複数メンバーにクーポンを割り当てる | `POST /campaigns/{couponId}/assign/batch` — 1回のコールで最大500メンバー。ボディにはオプションで `valid_from` / `valid_to` を指定可能。`{ "batchId": "..." }` を返します。 |
| ポイントの獲得/消費を記帳する | `POST /members/{accountId}/bookings` — メンバーアカウントに`EARNBOOKING`または`BURNBOOKING`を作成します。`{ "bookingId": "..." }` を返します。 |
| メール購読設定を同期する | `POST /subscriptions/email` — メンバーのオプトインを`allowed`または`declined`に設定します。オプトインチャネルはリクエストの`optins` > `defaultOptins`の順で解決されます。`200`（すべて成功）、`207`（部分的 — `succeeded` / `failed`を参照）、または`400`（不明なオプトインまたは未設定）を返します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ2: BrazeでWebhookを設定する" }

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

その他のアクションも同じパターンに従い、エンドポイントとボディのみが変わります。例えば、ポイント記帳は`/members/{accountId}/bookings`に`booking_type`（`EARNBOOKING`または`BURNBOOKING`）、`booking_type_code`、`points`、`reason`を含めてPOSTします。メール購読Webhookは`/subscriptions/email`に`account_id`と`status`（`allowed`または`declined`）をPOSTします。

#### エラーレスポンスとリトライ {#error-responses-and-retries}

| ステータス | 意味 |
| --- | --- |
| `200` | 成功。 |
| `207` | マルチステータス — メール購読Webhookのみ、一部のメンバーシップが更新され他が失敗した場合。 |
| `400` | リクエストボディのバリデーションに失敗。 |
| `401` | `X-Convercus-Key`が欠落しているか無効です。 |
| `5xx` | 上流のConvercusコールが失敗しました。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="エラーレスポンスとリトライ" }

{% alert warning %}
5xxレスポンスは成功を確認せずにリトライしないでください。これらの操作は冪等ではなく、リトライによりクーポンの二重割り当てやポイント記帳の二重計上が発生する可能性があります。これらのWebhookに対しては、Brazeの5xx自動リトライを無効にするか、最大リトライ回数を非常に低く設定してください。
{% endalert %}

### ステップ3: Brazeでデータを確認する {#step-3-verify-data-in-braze}

1. Convercusでロイヤルティイベントをトリガーします。例えば、ステータスレベルの変更、ポイントトランザクション、またはクーポンの引き換えなどです。
2. Brazeで対応するユーザーを開き、期待されるカスタム属性、カスタムイベント、または購入がプロファイルに表示されていることを確認します。ユーザーは`external_id`（またはステップ1で選択した識別子タイプ）でマッチングされます。
3. 逆方向を確認するには、ステップ2のWebhookの1つを呼び出すBrazeテスト送信を実行し、Convercusでアクション（クーポンの割り当て、ポイントの記帳、または購読の更新）を確認します。

## Braze での Convercus の使用 {#use-convercus-with-braze}

### ステップ1: 同期されたロイヤルティデータでメッセージをパーソナライズする {#step-1-personalize-messages-with-synced-loyalty-data}

連携が有効になると、Convercus のイベントは [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) エンドポイントを通じて Braze の各ユーザープロファイルに届き、他のネイティブデータと同様に使用できます。

1. ロイヤルティのカスタム属性（例: `convercus_status_level`、`convercus_balance`）をセグメントで使用して、ティア保有者、高残高メンバー、または最近ダウングレードされたユーザーをターゲットにします。
2. カスタムイベント（例: `convercus_status_level_changed`、クーポンおよびメンバーシップイベント）をキャンバスの**トリガーステップ**として、またはリエンゲージメントキャンペーンのフィルターとして使用します。
3. これらのフィールドを **Liquid** で参照して、メッセージ内のパーソナライゼーション（件名、本文、プッシュタイトル）に活用します。
4. Convercus からストリーミングされる `purchase` イベントを使用して、商品を意識したジャーニー（補充、カテゴリーアップセル、購入後のレビュー依頼）を推進します。

#### カスタム属性 {#custom-attributes}

| 属性 | 説明 |
| --- | --- |
| `convercus_account_id` | メンバーの Convercus アカウント ID — Convercus プログラム / Braze ワークスペース内で一意です。 |
| `convercus_user_id` | 複数の Convercus プログラムにわたって基盤となる人物を識別する Convercus ユーザー ID です。 |
| `convercus_partner_id` | このメンバーが登録した Convercus パートナー（マーチャント/ブランド）の識別子です。コアリションプログラムでのセグメンテーションに役立ちます。 |
| `convercus_member_role` | ロイヤルティプログラム内でのメンバーの役割です。 |
| `convercus_status_level` | メンバーの現在のティアまたはステータスレベルです。 |
| `convercus_balance` | メンバーの現在の `points`、`lockedPoints`、`statusPoints` を含むオブジェクトです。 |
| `email_subscribe` | Convercus のオプトインから導出されたメール購読ステータス（`opted_in`、`subscribed`、または `unsubscribed`）です。 |
| `push_subscribe` | Convercus のプッシュトークンイベントから導出されたプッシュ購読ステータス（`opted_in` または `unsubscribed`）です。 |
| 標準プロファイルフィールド | `email`、`phone`、`first_name`、`last_name`、`dob`、`gender`、`home_city`、`country` です。 |
| カスタムユーザープロパティ | Convercus ユーザーオブジェクトに定義されたカスタムプロパティは、すべて Braze カスタム属性として転送されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="カスタム属性" }

{% alert note %}
Braze ワークスペース内では、メンバーは `convercus_account_id` によって一意に識別されます。`convercus_user_id` は複数の Convercus プログラムにわたる基盤となる人物を識別するもので、クロスプログラム分析のために提供されています。Braze 内でのセグメンテーションには `convercus_account_id` を使用してください。
{% endalert %}

**`email_subscribe` のマッピング**

| Convercus の状態 | Braze の `email_subscribe` |
| --- | --- |
| `email consent` または `newsletter` の `allowedOptins` エントリ | `opted_in` |
| これらのチャネルの `declinedOptIns` エントリ（許可エントリなし） | `unsubscribed` |
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
| `convercus_coupon_redeemed` | メンバーがクーポンを引き換えたとき。 |
| `convercus_user_logged_in` | メンバーが Convercus 連携のサーフェスにサインインしたとき。 |
| `convercus_user_logged_out` | メンバーがサインアウトしたとき。 |
| `convercus_user_created` | 新しいユーザーが作成されたとき。 |
| `convercus_user_changed` | ユーザーのプロファイルデータが変更されたとき。 |
| `convercus_push_token_created` | メンバーのプッシュトークンが登録されたとき。 |
| `convercus_push_token_deleted` | プッシュトークンが削除されたとき。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="カスタムイベント" }

#### 購入 {#purchases}

タイプが `EARNTRANSACTION`（顧客の支出から獲得したポイント）の Convercus トランザクションは、[購入]({{site.baseurl}}/api/objects_filters/purchase_object)として Braze に報告され、Braze の収益分析、RFM セグメンテーション、予測機能でカウントされます。トランザクション ID が商品識別子として、トランザクション金額と通貨が価格と通貨として使用されます。

タイプが `PAYWITHPOINTSTRANSACTION`（ポイント消費）のトランザクションは購入としては報告**されません**。これらは `convercus_account_transaction` カスタムイベントとしてフローし、セグメンテーションに引き続き利用できます。獲得トランザクションの取り消しおよびキャンセルは、マイナス価格の購入として報告され、Braze の収益が Convercus と整合します。

### ステップ2: Connected Content でライブロイヤルティデータを取得する {#step-2-fetch-live-loyalty-data-with-connected-content}

送信時に最新である必要がある値（現在のポイント残高、有効なクーポン、最新のティア）については、最後に同期された属性に頼るのではなく、[Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) を使用して Braze から Convercus を呼び出します。両方のエンドポイントは Webhook と同じベース URL の配下にあり、`X-Convercus-Key` ヘッダーが必要です。

| データ | エンドポイント | 返却内容 |
| --- | --- | --- |
| メンバープロファイル | `GET /members/{accountId}/profile` | `member_id`、`first_name`、`last_name`、`email`、`tier_name`、`tier_id`、`points_balance`、`enrollment_date`。 |
| メンバークーポン | `GET /members/{accountId}/coupons` | 有効で引き換え可能なクーポンのリスト（ステータス、値、有効期間、タイトル、説明）。`?lang=<code>`（例: `?lang=de`）を追加すると `title`/`description` がローカライズされます。デフォルトは `en` です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ2: Connected Content でライブロイヤルティデータを取得する" }

Connected Content エンドポイントは、想定されるエラーでは常に HTTP 200 を返すため、Liquid テンプレートで `error` フィールドに基づいて分岐できます。

| レスポンス | 意味 |
| --- | --- |
| `200` + ペイロード | 成功。 |
| `200 { "error": "member_not_found" }` | このプログラムにアカウントが存在しません。 |
| `200 { "error": "internal_error" }` | アップストリームまたは予期しないエラー。 |
| `401` | `X-Convercus-Key` が欠落しているか無効です（Liquid ではなく連携時に対処してください）。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ2: Connected Content でライブロイヤルティデータを取得する" }

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

Connected Content は必ず条件分岐でラップしてください（`member.error` と空の `coupons` をチェック）。一時的なルックアップ失敗によって壊れたメッセージが送信されることを防ぎます。プロファイルはキャッシュし（`cache_max_age 300`）、クーポンはキャッシュしないでください（`cache_max_age 0`）。クーポンのステータスは送信間で変わる可能性があるためです。

## 考慮事項 {#considerations}

- **レイテンシー:** Convercus から Braze へのイベントは Kafka を経由して伝達され、通常の負荷状態では数秒で Braze に到達します。
- **Braze のレート制限:** このインテグレーションは `429` レスポンスに対して自動的にリトライを行い、Braze の `x-ratelimit-retry-after` ヘッダーに従い指数バックオフを適用します。
- **Connected Content のキャッシュ:** Braze はデフォルトで Connected Content のレスポンスを数分間キャッシュします。送信時に正確な値が必要な場合（ポイント残高など）は、Connected Content の呼び出しでキャッシュウィンドウを短縮するかバイパスしてください。
- **プログラムごとに1つの設定:** 各ロイヤルティプログラムは1つの Braze ワークスペースにマッピングされます。2つ目のワークスペースを接続するには、別のプログラムで設定を行ってください。
- **オブザーバビリティ:** プログラムごとの API コール統計とエラー履歴（双方向）は90日間保持され、Selfservice の Braze インテグレーションカードから確認できます。

## トラブルシューティング {#troubleshooting}

- **イベントがBrazeに表示されない:** 識別子として使用した値（ステップ1で選択したもの）が、Brazeのユーザーの`external_id`（または選択した識別子タイプ）と一致していることを確認してください。識別子が一致していない場合、イベントが誤ったプロファイルに紐付けられたり、ドロップされたりする原因になります。
- **Webhookが`401`を返す:** `X-Convercus-Key`ヘッダーが欠落しているか、`cvc_…` APIキーが失効しています。Selfserviceでキーを再生成し、BrazeのWebhookアクションを更新してください。
- **Webhookが`400`を返す:** リクエストに`Content-Type: application/json`が含まれていないか、ペイロードがドキュメントに記載されたスキーマと一致していません。メール購読Webhookの場合、`400`はリクエストされたオプトインがプログラムで認識されていないか、設定されていないことも意味します。
- **より詳細なデバッグ:** Selfserviceのブレイズ連携カードでプログラムごとのAPI呼び出し統計とエラー履歴を確認するか、Convercusの担当者にお問い合わせください。