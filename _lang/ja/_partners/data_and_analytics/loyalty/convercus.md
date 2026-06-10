---
nav_title: Convercus
article_title: Convercus
description: "このリファレンス記事では、BrazeとConvercusのパートナーシップについて説明します。Convercusはロイヤルティおよびクーポンプラットフォームで、リアルタイムのロイヤルティデータでBrazeを強化し、BrazeのCampaignsからConvercusのロイヤルティアクションをトリガーできます。"
page_type: partner
search_tag: Partner
---

# Convercus

> [Convercus](https://www.convercus.com/en)は、SaaS型のロイヤルティおよびクーポンプラットフォームで、オムニチャネルのロイヤルティプログラムやパーソナライズされたクーポンキャンペーンを通じて、ブランドや小売業者の来店頻度、バスケット単価、リピート率の向上を支援します。

*この連携はConvercusによって管理されています。*

## 連携について {#about-the-integration}

BrazeとConvercusの連携は双方向です。ロイヤルティデータはカスタム属性、カスタムイベント、購入としてリアルタイムでBrazeに流れ込み、BrazeのCanvasesやCampaignsはwebhookを通じてConvercusのロイヤルティアクションをトリガーできます。同期されたメンバーティア、ポイント残高、購入、クーポンアクティビティをSegments、Liquid、コネクテッドコンテンツで活用できます。Brazeジャーニーからは、クーポンの割り当て、ポイントの獲得・消費トランザクションの記録、Convercusでのメールサブスクリプション設定の更新も可能です。

Convercusが連携をホストするため、追加のインフラを導入する必要はありません。多くのロイヤルティコネクターがデータを一方向にプッシュするだけなのに対し、Convercusはループを閉じます。Brazeでロイヤルティイベントに反応し、Convercusでアクションを実行し、その結果をBrazeで測定できます。

## ユースケース {#use-cases}

1. **ティアアップのお祝い:** メンバーがConvercusでロイヤルティティアを上がった際に、ウェルカムメッセージ、ティア限定特典、メンバーの新しいティアとポイント残高を含むパーソナライズされたBraze Canvasをトリガーします。
2. **誕生日やマイルストーンボーナス:** Brazeジャーニーから、メンバーの誕生日や記念日にConvercusでボーナスポイントを記録し、新しい残高を確認するお祝いメッセージを送信します。
3. **休眠メンバーの復帰施策:** 非アクティブなメンバーに対して、BrazeがWebhookを通じてConvercusでパーソナライズされたクーポンを割り当て、メール、プッシュ、アプリ内メッセージで配信します。
4. **メッセージ内のリアルタイムポイント残高:** コネクテッドコンテンツを使用してメンバーのリアルタイムポイント残高をBraze Liquidに取り込み、「次の報酬まであとXポイント」のようなケイデンスを実現します。

## 前提条件 {#prerequisites}

開始する前に、以下が必要です。

| 前提条件 | 説明 |
| --- | --- |
| Convercusアカウント | アクティブなConvercusプログラム。まだ顧客でない場合は、Convercusアカウントマネージャーにお問い合わせください。 |
| Braze REST APIキー | `users.track`権限を持つBraze REST APIキー。このキーはBrazeダッシュボードの**設定** > **APIキー**から作成します。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/api/basics/#endpoints)。エンドポイントはお使いのインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

システム間で一貫したユーザー識別子が必要です。Brazeで`external_id`（または選択した識別子タイプ）として使用される値は、Convercusの対応するメンバー識別子と一致する必要があります。一致しない場合、イベントは正しいプロファイルに帰属されません。

## 連携 {#integration}

### ステップ1: Convercus SelfserviceでBrazeを設定する {#step-1-configure-braze-in-convercus-selfservice}

Convercus Selfservice（顧客向け管理UI — Convercusアカウントマネージャーが提供するURLで開きます）で、Brazeに接続するプログラムを開き、**Braze integration card**を使用して以下を行います。

1. 連携フォームに入力してBraze接続を設定します。

   | フィールド | 説明 |
   | --- | --- |
   | `apiKey` | Braze REST APIキー（`users.track`権限付き）。 |
   | `apiEndpoint` | Braze RESTエンドポイント（例: `https://rest.iad-01.braze.com`）。 |
   | 識別子タイプ | `external_id`または`user_alias`。ConvercusメンバーをBrazeユーザープロファイルにマッチングする方法を決定します。 |
   | `defaultOptins` | プログラムのオプトインチャネル（`membershipOptins`から）の複数選択。メールサブスクリプションWebhookでリクエストが`optins`を省略した場合のデフォルトとして使用されます。少なくとも1つが選択されるまで、Braze設定は**未完了**として扱われます。 |
   {: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ1: Convercus SelfserviceでBrazeを設定する" }

2. インバウンドコール用のAPIキーを作成します。プログラムごとの`X-Convercus-Key`認証情報を作成します。生のキーは作成時に一度だけ表示され、`cvc_`がプレフィックスとして付きます（形式: `cvc_<base64url>`）。ステップ2でWebhook CampaignsとコネクテッドコンテンツブロックをBrazeで設定する際に保存してください。キーは同じカードからいつでも取り消すことができ、取り消しは即座に有効になります。

Braze接続を保存すると、Convercusはそのプログラムのロイヤルティイベントを即座にBrazeへストリーミングし始めます。追加のインフラセットアップは不要です。

{% alert note %}
各Convercusプログラムは独立して設定されます。単一のConvercusテナントが異なるプログラムを異なるBrazeワークスペースに接続でき、それぞれ独自のAPIキーを持ちます。
{% endalert %}

### ステップ2: BrazeでWebhookを設定する {#step-2-configure-webhooks-in-braze}

CanvasやCampaignからConvercusアクションをトリガーするには、Convercus連携サービスを呼び出すBraze Webhookアクションを作成します。すべてのリクエストには以下のヘッダーを含める必要があります。

- `X-Convercus-Key: cvc_…` — ステップ1で生成したAPIキー。
- `Content-Type: application/json`

すべてのエンドポイントはベースURL `<SERVICE_HOST>/v1/programs/{programId}` の配下にあります。`<SERVICE_HOST>`をConvercusアカウントマネージャーが提供するホストに、`{programId}`をConvercusプログラムIDに置き換えてください。

| アクション | エンドポイント |
| --- | --- |
| メンバーにクーポンを割り当てる | `POST /campaigns/{couponId}/assign` — `{ "couponCode": "..." }` を返します。 |
| 複数メンバーにクーポンを割り当てる | `POST /campaigns/{couponId}/assign/batch` — 1回のコールで最大500メンバー。ボディはオプションの `valid_from` / `valid_to` を受け付けます。`{ "batchId": "..." }` を返します。 |
| 獲得/消費ポイントを記録する | `POST /members/{accountId}/bookings` — メンバーアカウントに `EARNBOOKING` または `BURNBOOKING` を作成します。`{ "bookingId": "..." }` を返します。 |
| メールサブスクリプション設定を同期する | `POST /subscriptions/email` — メンバーのオプトインを `allowed` または `declined` に設定します。オプトインチャネルはリクエストの `optins` > `defaultOptins` の順で解決されます。`200`（すべて成功）、`207`（部分的 — `succeeded` / `failed` を参照）、または `400`（不明なオプトインまたは未設定）を返します。 |
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

他のアクションも同じパターンに従い、エンドポイントとボディのみが変わります。例えば、ポイント記録は `/members/{accountId}/bookings` に `booking_type`（`EARNBOOKING` または `BURNBOOKING`）、`booking_type_code`、`points`、`reason` を含めてPOSTします。メールサブスクリプションWebhookは `/subscriptions/email` に `account_id` と `status`（`allowed` または `declined`）を含めてPOSTします。

#### エラーレスポンスとリトライ {#error-responses-and-retries}

| ステータス | 意味 |
| --- | --- |
| `200` | 成功。 |
| `207` | マルチステータス — メールサブスクリプションWebhookのみ。一部のメンバーシップが更新され、他が失敗した場合。 |
| `400` | リクエストボディのバリデーションに失敗。 |
| `401` | `X-Convercus-Key`が欠落しているか無効。 |
| `5xx` | 上流のConvercusコールが失敗。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="エラーレスポンスとリトライ" }

{% alert warning %}
5xxレスポンスは**成功を確認せずにリトライするのは安全ではありません**。これらの操作は冪等ではなく、リトライによりクーポンの二重割り当てやポイント記録の二重計上が発生する可能性があります。これらのWebhookではBrazeの5xx自動リトライを無効にするか、最大リトライ回数を非常に低く設定してください。
{% endalert %}

### ステップ3: Brazeでデータを確認する {#step-3-verify-data-in-braze}

1. Convercusでロイヤルティイベントをトリガーします。例えば、ステータスレベルの変更、ポイントトランザクション、クーポンの引き換えなどです。
2. Brazeで対応するユーザーを開き、期待されるカスタム属性、カスタムイベント、または購入がプロファイルに表示されることを確認します。ユーザーは`external_id`（またはステップ1で選択した識別子タイプ）でマッチングされます。
3. 逆方向を確認するには、ステップ2のWebhookの1つを呼び出すBrazeテスト送信を実行し、Convercusでアクションを確認します（クーポンの割り当て、ポイントの記録、またはサブスクリプションの更新）。

## BrazeでConvercusを使用する {#use-convercus-with-braze}

### ステップ1: 同期されたロイヤルティデータでメッセージをパーソナライズする {#step-1-personalize-messages-with-synced-loyalty-data}

連携が稼働すると、Convercusイベントは[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)エンドポイントを通じてBrazeの各ユーザープロファイルに届き、他のネイティブデータと同様に使用できます。

1. ロイヤルティカスタム属性（例: `convercus_status_level`、`convercus_balance`）を**Segments**で使用して、ティア保有者、高残高メンバー、または最近ダウングレードされたユーザーをターゲットにします。
2. カスタムイベント（例: `convercus_status_level_changed`、クーポンおよびメンバーシップイベント）をCanvasの**トリガーステップ**として、またはリエンゲージメントCampaignsのフィルターとして使用します。
3. これらのフィールドを**Liquid**で参照して、メッセージ内パーソナライゼーション（件名、本文、プッシュタイトル）に活用します。
4. Convercusからストリーミングされた`purchase`イベントを使用して、商品対応ジャーニー（補充、カテゴリアップセル、購入後レビューリクエスト）を推進します。

#### カスタム属性 {#custom-attributes}

| 属性 | 説明 |
| --- | --- |
| `convercus_account_id` | メンバーのConvercusアカウントID — Convercusプログラム/Brazeワークスペース内で一意。 |
| `convercus_user_id` | 複数のConvercusプログラムにまたがる基盤となる人物を識別するConvercusユーザーID。 |
| `convercus_partner_id` | このメンバーが登録したConvercusパートナー（加盟店/ブランド）の識別子。コアリションプログラムでのセグメンテーションに有用です。 |
| `convercus_member_role` | ロイヤルティプログラム内でのメンバーの役割。 |
| `convercus_status_level` | メンバーの現在のティアまたはステータスレベル。 |
| `convercus_balance` | メンバーの現在の`points`、`lockedPoints`、`statusPoints`を含むオブジェクト。 |
| `email_subscribe` | Convercusオプトインから導出されたメールサブスクリプション状態（`opted_in`、`subscribed`、または`unsubscribed`）。 |
| `push_subscribe` | Convercusプッシュトークンイベントから導出されたプッシュサブスクリプション状態（`opted_in`または`unsubscribed`）。 |
| 標準プロファイルフィールド | `email`、`phone`、`first_name`、`last_name`、`dob`、`gender`、`home_city`、`country`。 |
| カスタムユーザープロパティ | Convercusユーザーオブジェクトに定義されたカスタムプロパティはすべてBrazeカスタム属性として転送されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="カスタム属性" }

{% alert note %}
Brazeワークスペース内では、メンバーは`convercus_account_id`で一意に識別されます。`convercus_user_id`は複数のConvercusプログラムにまたがる基盤となる人物を識別し、クロスプログラム分析のために提供されます。Braze内でのセグメンテーションには`convercus_account_id`を使用してください。
{% endalert %}

**`email_subscribe`のマッピング**

| Convercusの状態 | Brazeの`email_subscribe` |
| --- | --- |
| `email consent`または`newsletter`の`allowedOptins`エントリ | `opted_in` |
| それらのチャネルの`declinedOptIns`エントリ（かつallowedエントリなし） | `unsubscribed` |
| いずれの記録もなし | `subscribed`（Brazeのニュートラルデフォルト） |
{: .reset-td-br-1 .reset-td-br-2 aria-label="email_subscribeのマッピング" }

#### カスタムイベント {#custom-events}

| イベント | トリガー条件 |
| --- | --- |
| `convercus_account_created` | Convercusで新しいアカウントが作成された場合。 |
| `convercus_membership_added` | 既存のアカウントがロイヤルティプログラムに参加した場合。 |
| `convercus_membership_created` | 新しいメンバーシップが作成された場合。 |
| `convercus_membership_changed` | メンバーシップのデータが変更された場合。 |
| `convercus_membership_optins_changed` | メンバーのオプトイン設定が変更された場合。 |
| `convercus_membership_terminated` | メンバーシップが終了した場合。 |
| `convercus_status_level_changed` | メンバーのティアまたはステータスレベルが変更された場合。 |
| `convercus_balance_changed` | メンバーのポイント残高が変更された場合。 |
| `convercus_account_transaction` | ロイヤルティトランザクションがレーティングされた場合。 |
| `convercus_coupon_assigned` | メンバーにクーポンが割り当てられた場合。 |
| `convercus_coupon_redeemed` | メンバーがクーポンを引き換えた場合。 |
| `convercus_user_logged_in` | メンバーがConvercus搭載のサーフェスにサインインした場合。 |
| `convercus_user_logged_out` | メンバーがサインアウトした場合。 |
| `convercus_user_created` | 新しいユーザーが作成された場合。 |
| `convercus_user_changed` | ユーザーのプロファイルデータが変更された場合。 |
| `convercus_push_token_created` | メンバーのプッシュトークンが登録された場合。 |
| `convercus_push_token_deleted` | プッシュトークンが削除された場合。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="カスタムイベント" }

#### 購入 {#purchases}

タイプ`EARNTRANSACTION`（顧客の支出から獲得したポイント）のConvercusトランザクションは、Brazeに[購入]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#purchase-object-specification)として報告され、Brazeの収益分析、RFMセグメンテーション、予測機能でカウントされます。トランザクションIDを商品識別子として、トランザクション金額と通貨を価格と通貨として使用します。

タイプ`PAYWITHPOINTSTRANSACTION`（ポイント消費）のトランザクションは購入として報告**されません**。`convercus_account_transaction`カスタムイベントとして流れるため、セグメンテーションに引き続き利用できます。獲得トランザクションの取り消しやキャンセルは、マイナス価格の購入として報告され、Brazeの収益をConvercusと整合させます。

### ステップ2: コネクテッドコンテンツでリアルタイムのロイヤルティデータを取得する {#step-2-fetch-live-loyalty-data-with-connected-content}

送信時に最新でなければならない値（現在のポイント残高、アクティブなクーポン、最新のティア）については、最後に同期された属性に頼るのではなく、[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)を使用してBrazeからConvercusを呼び出します。両方のエンドポイントはWebhookと同じベースURL配下にあり、`X-Convercus-Key`ヘッダーが必要です。

| データ | エンドポイント | 返却値 |
| --- | --- | --- |
| メンバープロファイル | `GET /members/{accountId}/profile` | `member_id`、`first_name`、`last_name`、`email`、`tier_name`、`tier_id`、`points_balance`、`enrollment_date`。 |
| メンバークーポン | `GET /members/{accountId}/coupons` | アクティブで引き換え可能なクーポンのリスト（ステータス、値、有効期間、タイトル、説明）。`?lang=<code>`（例: `?lang=de`）を追加して`title`/`description`をローカライズできます。デフォルトは`en`です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ2: コネクテッドコンテンツでリアルタイムのロイヤルティデータを取得する" }

コネクテッドコンテンツのエンドポイントは、予期される失敗時に常にHTTP 200を返すため、Liquidテンプレートで`error`フィールドに基づいて分岐できます。

| レスポンス | 意味 |
| --- | --- |
| `200` + ペイロード | 成功。 |
| `200 { "error": "member_not_found" }` | このプログラムにアカウントが存在しません。 |
| `200 { "error": "internal_error" }` | 上流または予期しない障害。 |
| `401` | `X-Convercus-Key`が欠落しているか無効（Liquidではなく連携設定時に対処してください）。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="コネクテッドコンテンツのレスポンス" }

例 — メンバーのロイヤルティステータス（ティア、ポイント、アクティブオファー）をレンダリングする:

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

コネクテッドコンテンツは常に条件分岐でラップしてください（`member.error`と空の`coupons`をチェック）。一時的なルックアップ失敗が壊れたメッセージを送信しないようにします。プロファイルはキャッシュし（`cache_max_age 300`）、クーポンはキャッシュしないでください（`cache_max_age 0`）。クーポンのステータスは送信間で変わる可能性があるためです。

## 考慮事項 {#considerations}

- **レイテンシ:** ConvercusからBrazeへのイベントはKafkaを通じて伝播し、通常の負荷では数秒でBrazeに到達します。
- **Brazeレート制限:** 連携は`429`レスポンスに対してエクスポネンシャルバックオフでBrazeの`x-ratelimit-retry-after`ヘッダーを尊重しながら自動的にリトライします。
- **コネクテッドコンテンツのキャッシュ:** Brazeはデフォルトでコネクテッドコンテンツのレスポンスを数分間キャッシュします。送信時に正確でなければならない値（ポイント残高など）については、コネクテッドコンテンツコールでキャッシュウィンドウを短縮またはバイパスしてください。
- **プログラムごとに1つの設定:** 各ロイヤルティプログラムは単一のBrazeワークスペースにマッピングされます。2つ目のワークスペースを接続するには、別のプログラムで設定してください。
- **オブザーバビリティ:** プログラムごとのAPIコール統計とエラー履歴（双方向）は90日間保持され、SelfserviceのBraze integration cardから確認できます。

## トラブルシューティング {#troubleshooting}

- **イベントがBrazeに表示されない:** ステップ1で選択した識別子として使用されている値が、Brazeのユーザーの`external_id`（または選択した識別子タイプ）と一致していることを確認してください。識別子の不一致により、イベントが誤ったプロファイルに帰属されるか、ドロップされます。
- **Webhookが`401`を返す:** `X-Convercus-Key`ヘッダーが欠落しているか、`cvc_…` APIキーが取り消されています。Selfserviceでキーを再生成し、BrazeのWebhookアクションを更新してください。
- **Webhookが`400`を返す:** リクエストに`Content-Type: application/json`が欠落しているか、ペイロードがドキュメント化されたスキーマと一致していません。メールサブスクリプションWebhookの場合、`400`はリクエストされたオプトインがプログラムに認識されていないか、設定されていないことも意味します。
- **詳細なデバッグ:** SelfserviceのBraze integration cardでプログラムごとのAPIコール統計とエラー履歴を確認するか、Convercusの担当者にお問い合わせください。