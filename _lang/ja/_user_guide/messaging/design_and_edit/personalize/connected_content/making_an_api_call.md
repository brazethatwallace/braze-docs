---
nav_title: Connected Contentの呼び出しを行う
article_title: Connected Content APIの呼び出しを行う
page_order: 0
description: "このリファレンス記事では、Connected Content APIの呼び出し方法、役立つ例、高度なConnected Contentのユースケースについて説明します。"
search_rank: 2
---

# [![Braze Learningコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"} Connected Content APIの呼び出しを行う {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomconnected-content-stylefloatrightwidth120pxborder0-classnoimgbordermake-a-connected-content-api-call}

> Connected Contentを使用すると、APIでアクセス可能な情報をユーザーに送信するメッセージに直接挿入できます。Webサーバーから直接、または公開されているAPIからコンテンツを取得できます。<br><br>このページでは、Connected Content APIの呼び出し方法、高度なConnected Contentのユースケース、エラー処理などについて説明します。

## Connected Contentの呼び出し量について {#understanding-connected-content-call-volume}

{% alert important %}
1回の送信は1回のConnected Contentの呼び出しと等しくありません。Brazeはメッセージ送信とConnected Contentリクエストの間の1:1の比率を保証しません。システムは、呼び出し回数を最小限に抑えることよりも、正しいメッセージのレンダリングと配信を優先するように設計されています。エンドポイントは、受信者数や送信メッセージ数よりも多くのリクエストを処理できるように構築する必要があります。
{% endalert %}

Brazeは、受信者1人あたり同じConnected Content APIの呼び出しを複数回行う場合があります。一般的な理由は以下のとおりです。

- **複数パートのメール：** 1通のメールで、HTML本文、プレーンテキスト本文、Accelerated Mobile Pages（AMP）バージョン（存在する場合）のそれぞれに対して個別のレンダリングパスがトリガーされることがあります。各パスでそのパートのConnected Contentがトリガーされるため、1人の受信者が複数の同一または類似の呼び出しを生成する可能性があります。
- **バリデーションとリトライ：** メッセージペイロードは、バリデーション、リトライロジック、その他の内部目的のために、受信者1人あたり複数回レンダリングされることがあります。
- **チャネルの動作：** Connected Contentはメッセージがレンダリングされるときに実行されます。アプリ内メッセージの場合、メッセージはインプレッション時にレンダリングされます。

ログで送信数や受信者数よりも多くのConnected Contentの呼び出しが確認される場合、その動作は想定どおりです。負荷の軽減とスケーリングの計画については、[大量エンドポイントのベストプラクティス](#best-practices-for-high-volume-endpoints)を参照してください。

## Connected Contentコールを送信する {#send-a-connected-content-call}

Connected Contentコールを送信するには、{% raw %}`{% connected_content %}`{% endraw %} タグを使用します。このタグでは、`:save` を使用して変数を割り当てまたは宣言できます。これらの変数の要素は、後でメッセージ内で [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) を使って参照できます。

### APIコールの内訳 {#break-down-the-api-call}

次の例では、Sunrise-Sunset APIを使用して、今日の日の出時刻をメッセージに含めています。

{% raw %}
```
{% connected_content https://api.sunrise-sunset.org/v2?lat=40.7128&lng=-74.0060&date=today :save result %}
Hi there, today's sunrise in NYC is at {{result.sunrise}}.
```
{% endraw %}

各部分の役割は次のとおりです。

| コンポーネント | 役割 |
| --- | --- |
| `connected_content` タグ | メッセージのレンダリング中にHTTPリクエストを行うようBrazeに指示します。 |
| `https://api.sunrise-sunset.org/v2` | Brazeが呼び出すAPIエンドポイントです。 |
| `lat=40.7128&lng=-74.0060` | ニューヨーク市の座標を指定するクエリパラメーターです。 |
| `date=today` | その座標における当日のデータをリクエストします。 |
| `:save result` | APIレスポンスを `result` というローカル変数に保存します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="APIコールの内訳" }

### Sunrise-Sunset APIレスポンスの仕組み {#how-the-sunrise-sunset-api-response-works}

このエンドポイントは、`sunrise`、`sunset`、`tzid` などのトップレベルフィールドを含むJSONを返します。時刻はデフォルトでその場所のタイムゾーンで返されます（この例ではニューヨーク時間）。

たとえば、レスポンスの形式は次のようになります。

```json
{
  "date": "2026-07-23",
  "tzid": "America/New_York",
  "sunrise": "2026-07-23T05:42:11-04:00",
  "sunset": "2026-07-23T20:21:32-04:00"
}
```

### APIレスポンスをLiquidにマッピングする {#map-the-api-response-to-liquid}

レスポンスは `result` として保存されるため、そのオブジェクトから各フィールドを直接参照できます。

{% raw %}
```liquid
{{result.sunrise}}
{{result.sunset}}
{{result.tzid}}
```
{% endraw %}

Connected ContentからJSONを保存する場合は、常にこのパターンを使用してください。

1. `:save` でAPIレスポンスを保存します。
2. JSONレスポンス内で必要なフィールドを見つけます。
3. Liquidで `saved_variable.field_name` として参照します。

### 変数を追加する {#add-variables}

Connected Contentリクエストを行う際に、URL文字列内の変数としてユーザープロファイル属性を含めることもできます。

たとえば、ユーザーのメールアドレスとIDに基づいてコンテンツを返すWebサービスがあるとします。アットマーク（@）などの特殊文字を含む属性を渡す場合は、次のメールアドレス属性の例に示すように、Liquidフィルター `url_param_escape` を使用して、URLで許可されていない文字をURLフレンドリーなエスケープバージョンに置き換えてください。

{% raw %}
```
Hi, here are some articles that you might find interesting:

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```
{% endraw %}
{% alert note %}
属性値は、Braze版のLiquid構文内で正しく動作するために `${}` で囲む必要があります。
{% endalert %}

Connected ContentリクエストはGETおよびPOSTリクエストのみをサポートしています。

## エラーハンドリング {#error-handling}

URLが利用できず404ページに到達した場合、Brazeはその場所に空の文字列をレンダリングします。URLがHTTP 500または502ページに到達した場合、URLはリトライロジックで失敗します。

エンドポイントがJSONを返す場合、`connected`の値がnullかどうかを確認し、[条件付きでメッセージを中止する]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content)ことで検出できます。Brazeはポート80（HTTP）および443（HTTPS）で通信するURLのみを許可します。

### 異常ホスト検出 {#unhealthy-host-detection}

Connected Contentは、ターゲットホストが著しい遅延や過負荷の高い発生率を経験し、タイムアウト、リクエスト過多、またはBrazeがターゲットエンドポイントと正常に通信できないその他の結果が生じた場合に検出する異常ホスト検出メカニズムを採用しています。これは、ターゲットホストの問題を引き起こしている可能性のある不要な負荷を軽減するためのセーフガードとして機能します。また、Brazeインフラの安定化と高速なメッセージング速度の維持にも役立ちます。

ターゲットホストが著しい遅延や過負荷の高い発生率を経験した場合、Brazeはターゲットホストへのリクエストを1分間一時的に停止し、代わりに失敗を示すレスポンスをシミュレートします。1分後、Brazeは少数のリクエストを使用してホストの健全性を確認し、ホストが健全であることが確認された場合はフルスピードでリクエストを再開します。ホストがまだ異常な場合、Brazeはさらに1分間待ってから再試行します。

ターゲットホストへのリクエストが異常ホスト検出器によって停止された場合、Brazeはエラーレスポンスコードを受信したかのようにメッセージのレンダリングを続行し、Liquidロジックに従います。これらのConnected Contentリクエストが異常ホスト検出器によって停止された際にリトライされるようにしたい場合は、`:retry`オプションを使用してください。`:retry`オプションの詳細については、[Connected Contentのリトライ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries)を参照してください。

異常ホスト検出が問題を引き起こしていると思われる場合は、[Brazeサポート]({{site.baseurl}}/support_contact)にお問い合わせください。

{% alert note %}
Connected Contentに使用する特定のURLを許可リストに追加できます。この機能にアクセスするには、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

{% alert tip %}
一般的なエラーコードの詳細については、[WebhookとConnected Contentリクエストのトラブルシューティング]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#unhealthy-host-detection)を参照してください。
{% endalert %}

### レート制限（429）と異常ホスト検出の違い {#rate-limits-429-versus-unhealthy-host-detection}

以下は異なるメカニズムです：

- **429 Too Many Requests：** エンドポイント（または上流のサービス）がこのレスポンスを返しています。これは、サーバーまたはミドルウェアがトラフィックを拒否していることを意味し、多くの場合、独自のレート制限があるためです。BrazeはConnected Contentに個別のレート制限を適用しません。Connected Contentのリクエスト量は、[メッセージ配信速度のレート制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting)に直接比例してスケールします。メッセージは受信者ごとに複数回レンダリングされる可能性があるため（例：メールのHTML、プレーンテキスト、AMP）、Connected Contentリクエストの数はそのレート制限を超える場合があります。設定した1分あたりのメッセージ数以下になるとは想定しないでください。429が発生する場合は、予想されるリクエスト量を処理できるようにエンドポイントまたはミドルウェアをスケールするか、キャンペーンまたはキャンバスの[配信速度のレート制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting)を下げて、1分あたりに送信されるメッセージ（およびConnected Content呼び出し）を減らしてください。
- **異常ホスト検出：** 1分間のウィンドウ内で高い発生率と量の*失敗*が発生した後にトリガーされるBraze側のセーフガードです。失敗カウントには`408`、`429`、`502`、`503`、`504`、`529`のステータスコードが含まれます。トリガーされると、Brazeはそのホストへのリクエストを一時的に停止し、失敗レスポンスをシミュレートします。これはお客様独自のレート制限とは独立しています。検出しきい値と詳細については、[WebhookとConnected Contentリクエストのトラブルシューティング]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#unhealthy-host-detection)を参照してください。異常ホスト検出のトリガーを回避するには、[Connected Content呼び出し量の理解](#understanding-connected-content-call-volume)および[大量エンドポイントのベストプラクティス](#best-practices-for-high-volume-endpoints)で説明されている呼び出し量をエンドポイントが処理できるようにしてください。

## 効率的なパフォーマンスの確保 {#allowing-for-efficient-performance}

Brazeは非常に高速にメッセージを配信するため、コンテンツの取得時にオーバーロードしないよう、サーバーが数千の同時接続を処理できることを確認してください。パブリックAPIを使用する場合は、APIプロバイダーが設定しているレート制限に違反しないことを確認してください。Brazeはパフォーマンス上の理由から、サーバーのレスポンス時間が2秒未満であることを要求しています。サーバーのレスポンスに2秒以上かかる場合、コンテンツは挿入されません。

エンドポイントのキャパシティ計画と呼び出し量の削減については、[大量エンドポイントのベストプラクティス](#best-practices-for-high-volume-endpoints)を参照してください。

## 知っておくべきこと {#things-to-know}

- Brazeは API コールに対して課金せず、所定のデータポイント使用量にもカウントされません。
- Connected Contentのレスポンスには1 MBの制限があります。
- Connected Contentはメッセージがレンダリングされるときに実行されます。アプリ内メッセージの場合、メッセージはインプレッション時にレンダリングされます。
- Connected Contentコールはリダイレクトに従いません。

### Connected Contentコールの処理方法 {#how-connected-content-calls-are-processed}

単一のメッセージテンプレート内のConnected ContentコールはLiquidレンダリング中に順次（上から下へ）実行されます。つまり、下流のコールは上流のコールで設定された変数を参照できます。この例では、最初のコールがユーザーデータを取得し、2番目のコールがそのデータを使用してプリファレンスを取得します。

{% raw %}
```liquid
{% connected_content https://api.example.com/user :save user_data %}
{% connected_content https://api.example.com/preferences?user_id={{user_data.id}} :save preferences %}
```
{% endraw %}

### グローバル送信とリクエストボリューム {#global-sending-and-request-volume}

Connected Contentコールは単一のメッセージ内では順次実行されますが、メッセージはキャンペーンやキャンバス全体で並列に送信されます。大量送信では、ピーク送信期間中にエンドポイントに対して大量のリクエストトラフィックが発生する可能性があります。そのトラフィックの管理とスロットリング（ワークスペースのメッセージングレート制限、配信速度のレート制限、キャッシュを含む）については、[大量エンドポイントのベストプラクティス](#best-practices-for-high-volume-endpoints)を参照してください。

## 大量送信エンドポイントのベストプラクティス {#best-practices-for-high-volume-endpoints}

メッセージでConnected Contentを使用し、大量に送信する場合は、受信者数や送信数を超えるリクエストが発生することを想定して計画してください。

- **ピーク負荷を見積もる:** エンドポイントやミドルウェアのサイジングには、保守的な倍率を使用してください。Connected Contentのリクエストは、受信者数やメッセージ送信数を超える場合があります。たとえば、メールの場合、1人の受信者に対して複数の呼び出し（HTML、プレーンテキスト、AMP）が発生する可能性があるため、受信者数 × 2 または × 3 が保守的な見積もりとしてよく使用されます。
- **適切な場合はキャッシュを使用する:** GETリクエストはデフォルトでキャッシュされます。POSTリクエストの場合、レスポンスが一定期間再利用できるとき（たとえば、リクエストごとに変わらないトークンやコンテンツなど）は `:cache_max_age` を追加してください。[レスポンスのキャッシュ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses)および次のセクションの[POSTキャッシュに関するFAQ](#what-is-caching-behavior)を参照してください。
- **メッセージのレート制限を設定する:** [ワークスペースのメッセージングレート制限]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits)およびキャンペーンやキャンバスの[配信速度レート制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting)は、Connected Contentのリクエスト量を間接的に制限します。Braze自体はConnected Contentをレート制限しません。Connected Contentのリクエストはメッセージと1:1ではないため、これらは完全な制御ではなくプロキシです。エンドポイントが処理できる範囲内にメッセージ（およびConnected Content）の量を抑えるために使用してください。
- **冪等性とリトライを考慮して設計する:** Brazeは1人の受信者に対してエンドポイントを複数回呼び出す場合があります。エンドポイントが重複リクエストを受けても、不正な副作用なく処理できることを確認してください。

## 認証タイプ {#authentication-types}

### ベーシック認証の使用 {#using-basic-authentication}

URLにベーシック認証が必要な場合、BrazeはAPI呼び出しで使用するベーシック認証の認証情報を保存できます。既存のベーシック認証の認証情報を管理したり、新しい認証情報を追加したりするには、**設定** > **Connected Content** に移動します。

![Brazeダッシュボードの Connected Content 設定。]({% image_buster /assets/img/connected_content/basic_auth_mgmt.png %})

新しい認証情報を追加するには、**認証情報を追加** > **ベーシック認証**を選択します。

![ベーシック認証またはトークン認証を使用するオプションが表示された「認証情報を追加」ドロップダウン。]({% image_buster /assets/img/connected_content/add_credential_button.png %}){: style="max-width:60%"}

認証情報に名前を付け、ユーザー名とパスワードを入力します。

![名前、ユーザー名、パスワードを入力するオプションが表示された「新しい認証情報を作成」ウィンドウ。]({% image_buster /assets/img/connected_content/basic_auth_token.png %}){: style="max-width:60%"}

その後、トークンの名前を参照することで、API呼び出しでこのベーシック認証の認証情報を使用できます。

{% raw %}
```
Hi there, here is some fun trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
認証情報を削除すると、その認証情報を使用しようとするすべてのConnected Content呼び出しが中止されることに注意してください。
{% endalert %}

保存された認証情報は、Brazeがメッセージをレンダリングする際に{% raw %}`{% connected_content %}`{% endraw %}リクエストに適用されます。[Webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#authentication-and-connected-content-credentials)ステップで設定されたプライマリHTTPリクエストには適用されません。その呼び出しのシークレットを取得する必要がある場合は、リクエストヘッダーまたはWebhookのヘッダーやボディフィールド内の{% raw %}`{% connected_content %}`{% endraw %}タグを使用してください。

### トークン認証の使用 {#using-token-authentication}

Braze Connected Contentを使用する際、特定のAPIではユーザー名とパスワードの代わりにトークンが必要になる場合があります。Brazeは、トークン認証のヘッダー値を保持する認証情報も保存できます。

トークン値を保持する認証情報を追加するには、**認証情報を追加** > **トークン認証**を選択します。次に、API呼び出しヘッダーのキーと値のペアと許可ドメインを追加します。

![トークン認証の詳細が表示されたトークン「token_credential_abc」の例。]({% image_buster /assets/img/connected_content/token_auth.png %}){: style="max-width:60%"}

その後、認証情報名を参照することで、API呼び出しでこの認証情報を使用できます。

{% raw %}
```
{% assign campaign_name="New Year Sale" %}
{% connected_content
     https://api.endpoint.com/your_path
     :method post
     :auth_credentials token_credential_abc
     :body campaign={{campaign_name}}&customer={{${user_id}}}&channel=Braze
     :content_type application/json
     :save publication
%}
```
{% endraw %}

### Open Authentication（OAuth）の使用 {#use-open-authentication-oauth}

一部のAPI設定では、アクセスしたいAPIエンドポイントの認証に使用できるアクセストークンの取得が必要です。

#### ステップ1:アクセストークンを取得する {#step-1-retrieve-the-access-token}

以下の例は、アクセストークンを取得してローカル変数に保存する方法を示しています。保存されたトークンは、後続のAPI呼び出しの認証に使用できます。`:cache_max_age`パラメーターを追加して、アクセストークンの有効期間に合わせることで、送信Connected Content呼び出しの数を削減できます。詳細については、[設定可能なキャッシュ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses)を参照してください。

{% raw %}
```
{% connected_content
     https://your_API_access_token_endpoint_here/
     :method post
     :auth_credentials access_token_credential_abc
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE"
     }
     :cache_max_age 900
     :save token_response
%}
```
{% endraw %}

{% alert note %}
トークンエンドポイントが`application/x-www-form-urlencoded`を期待し、認証情報を`:body`で渡す場合、パラメーター値の特殊文字をURLエンコードしてください。たとえば、スラッシュ（`/`）は`%2F`に、プラス記号（`+`）は`%2B`になります。エンコードされていない特殊文字があると、OAuthトークンリクエストが失敗する可能性があります。
{% endalert %}

#### ステップ2:取得したアクセストークンを使用してAPIを認可する {#step-2-authorize-the-api-using-the-retrieved-access-token}

トークンが保存されると、後続のConnected Content呼び出しにダイナミックにテンプレート化して、リクエストを認可できます。

{% raw %}
```
{% connected_content
     https://your_API_endpoint_here/
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE",
       "Authorization": "{{token_response}}"
     }
     :body key1=value1&key2=value2
     :save response
%}
```
{% endraw %}

### 認証情報の編集 {#editing-credentials}

認証タイプの認証情報名を編集できます。

- ベーシック認証の場合、ユーザー名とパスワードを更新できます。以前に入力したパスワードは表示されないことに注意してください。
- トークン認証の場合、ヘッダーのキーと値のペアと許可ドメインを更新できます。以前に設定したヘッダー値は表示されないことに注意してください。

## Connected Content IP許可リスト {#connected-content-ip-allowlisting}

Connected Contentを使用したメッセージがBrazeから送信されると、Brazeサーバーは自動的に顧客またはサードパーティのサーバーにネットワークリクエストを送信してデータを取得します。IP許可リストを使用すると、Connected Contentリクエストが実際にBrazeから送信されていることを確認でき、セキュリティの層を追加できます。

Brazeは以下のIP範囲からConnected Contentリクエストを送信します。リストに記載された範囲は、許可リストにオプトインされたすべてのAPIキーに自動的かつ動的に追加されます。

Brazeには、すべてのサービスに使用される予約済みのIPセットがあり、特定の時点ですべてがアクティブであるとは限りません。これは、必要に応じて、顧客に影響を与えることなく、Brazeが別のデータセンターから送信したりメンテナンスを行ったりできるように設計されています。BrazeはConnected Contentリクエストを行う際に、以下にリストされたIPの1つ、サブセット、またはすべてを使用する場合があります。

Connected Contentリクエストが一貫して`403 Forbidden`を返し、認証が正しく設定されている場合は、リクエストを受信するサーバーでこれらのIPを許可リストに追加してください。`403`は権限不足や無効な認証情報を示す場合もあるため、ネットワーク設定と認証設定の両方を確認してください。Webhookに関する具体的なガイダンスについては、[403 ForbiddenとIP許可リスト]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#403-forbidden-and-ip-allowlisting)を参照してください。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### `User-Agent`ヘッダー {#user-agent-header}

Brazeは、すべてのConnected ContentおよびWebhookリクエストに以下のような`User-Agent`ヘッダーを含めます。

```text
Braze Sender 75e404755ae1270441f07eb238f0faf25e44dfdc
```

{% alert tip %}
ハッシュ値は定期的に変更されることに注意してください。`User-Agent`でトラフィックをフィルタリングしている場合は、`Braze Sender`で始まるすべての値を許可してください。
{% endalert %}

## トラブルシューティング {#troubleshooting}

Connected Contentの呼び出しが正しくレンダリングされない、またはまったくレンダリングされない場合は、以下の点を確認してください。

- **Connected Contentの呼び出しが行われたことを確認する：**[メッセージング履歴タブ]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab)で呼び出しが行われたかどうかを確認できます。また、単一のConnected Contentリクエストをテスト送信することもできます。
- **PostmanまたはCURLリクエストで理想的なリクエストが成功するか検証する：**リクエストが機能してレスポンスが返される場合は、リクエストの詳細（ヘッダーを含む）を比較してください。ヘッダーがダブルクォーテーション付きのキーと値のペアでキャプチャされていることを確認してください。
- **認証が正しく処理されていることを検証する：**`:basic_auth`/`:auth_credentials`オプションが使用されており、Connected Contentの認証がConnected Contentのワークスペース設定に追加されていることを確認してください。Connected Content URLには、認証以外のヘッダーの入力が必要な場合があります。
- **データが期待される形式であることを検証する：**レスポンスボディについて、Brazeは有効なJSONをLiquidオブジェクトに解析します。それ以外の場合、レスポンスはプレーンテキスト（HTMLを含む）として扱われます。`:content_type`オプションはリクエストの送信時の`Content-Type`および`Accept`ヘッダーを設定しますが、レスポンスの解析には影響しません。リクエストの`:body`について、JSONにスペースが含まれている場合は、[JSONボディの提供]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/local_connected_content_variables#providing-json-body)セクションのガイダンスに従ってください。
- **データが正しく解析されたことを確認する：**Liquidが期待されるフィールドを正しく参照しているか確認してください。ネストされたJSONの場合は、{% raw %}`{{sampleresult.data[0].sample_field}}`{% endraw %}を使用して目的のネストされたフィールドを指定します。{% raw %}`RESPONSE:{{sampleresult.data}}`{% endraw %}で期待される結果を出力して、ネストされたJSONプロパティを確認できます。
- **レスポンスステータスコードを確認する：**レスポンスステータスコードは`2XX`コードである必要があります。Connected Contentには、コードが`2XX`でない場合にレスポンスを処理する方法がありません。

[Webhook.site](https://webhook.site/)を使用して、Connected Contentの呼び出しのトラブルシューティングや、呼び出しで送信されるリクエストヘッダー、リクエストボディ、その他の情報に関する問題を診断することもできます。

1. Connected Content呼び出しのURLを、サイトで生成された一意のURLに切り替えます。
2. キャンペーンまたはキャンバスステップをプレビューしてテストし、このWebサイトにリクエストが届くことを確認します。

また、Liquidタグにエンドポイントが期待するパラメーター（例：`:method`、`:headers`、`:content_type`、`:body`、必要に応じて`:basic_auth`）が含まれていることを確認できます。保存されたJSONオブジェクト内のHTTPステータスコードキーに依存している場合、エンドポイントはJSONオブジェクトと`2XX`ステータスを返す必要があります。

ホストからのエラー率が高い場合は、[異常なホストの検出]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors#unhealthy-host-detection)および[Connected Content呼び出しボリュームの理解](#understanding-connected-content-call-volume)を確認してください。

## よくある質問 {#frequently-asked-questions}

### Connected Content の呼び出しがユーザー数や送信数より多いのはなぜですか？ {#why-are-there-more-connected-content-calls-than-users-or-sends}

Braze は、メッセージペイロードをレンダリングするために、受信者1人あたり同じ Connected Content API 呼び出しを複数回行う場合があります。メッセージペイロードは、バリデーション、リトライロジック、その他の内部目的のために、受信者1人あたり複数回レンダリングされることがあります。ただし、メッセージに実際に反映される Connected Content 呼び出しは1回のみです。

リトライロジックが呼び出しで使用されていない場合でも、Connected Content API 呼び出しが受信者1人あたり複数回行われることは想定される動作です。Connected Content を含むメッセージにレート制限を設定するか、メッセージ送信ごとに複数の Connected Content 呼び出しが行われることを考慮した想定ボリュームに対応できるようサーバーを構成することをお勧めします。

詳細と軽減策については、[Connected Content の呼び出しボリュームについて](#understanding-connected-content-call-volume)および[大量エンドポイントのベストプラクティス](#best-practices-for-high-volume-endpoints)を参照してください。

### Connected Content でレート制限はどのように機能しますか？ {#how-does-rate-limiting-work-with-connected-content}

Connected Content には独自のレート制限はありません。代わりに、レート制限はメッセージ送信レートに基づきます。送信されるメッセージ数よりも Connected Content 呼び出しが多い場合は、メッセージングのレート制限を、意図する Connected Content のレート制限よりも高く設定することをお勧めします。

### キャッシュの動作はどのようになっていますか？ {#what-is-caching-behavior}

GET リクエストはデフォルトでキャッシュされます（[レスポンスのキャッシュ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses)を参照）。**POST リクエストはデフォルトではキャッシュされません**が、Connected Content 呼び出しに `:cache_max_age` を追加することでキャッシュを有効にできます。これにより、同じ POST（たとえばトークンやコンテンツのリクエスト）がキャッシュウィンドウ内で繰り返し行われる場合に、エンドポイントの負荷を軽減できます。

{% raw %}
```liquid
{% connected_content https://api.example.com/token :method post :body grant_type=client_credentials :cache_max_age 900 :save token %}
```
{% endraw %}

キャッシュは重複する Connected Content 呼び出しの削減に役立ちますが、ユーザーあたり1回の呼び出しになることが保証されるわけではありません。キャッシュの持続時間は5分から4時間の間です。詳細については、[レスポンスのキャッシュ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses)を参照してください。

### Connected Content のデフォルトの HTTP 動作は何ですか？ {#what-is-the-connected-content-http-default-behavior}

{% multi_lang_include connected_content/sections.md section='default behavior' %}

{% multi_lang_include connected_content/sections.md section='http post' %}

### 同じ Connected Content 呼び出しを複数の場所で使用するとどうなりますか？ {#what-happens-if-i-use-the-same-connected-content-call-in-multiple-places}

各 Connected Content タグは、複数のタグが同じ URL とパラメーターを使用している場合でも、個別に評価されます。URL とキャッシュ設定が許可する場合、同一のリクエストは新しいアウトバウンドリクエストをトリガーする代わりにキャッシュから提供されることがあります（詳細については[レスポンスのキャッシュ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/caching_responses)を参照してください）。