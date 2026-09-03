---
nav_title: Connected Contentの呼び出しを行う
article_title: Connected Content APIの呼び出しを行う
page_order: 0
description: "このリファレンス記事では、Connected Content APIの呼び出し方法、役立つ例、高度なConnected Contentのユースケースについて説明します。"
search_rank: 2
toc_headers: h2
---

# [![Braze Learningコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"}Connected Content APIの呼び出しを行う {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomconnected-content-stylefloatrightwidth120pxborder0-classnoimgbordermake-a-connected-content-api-call}

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

## Connected Content コールを送信する {#send-a-connected-content-call}

Connected Content コールを送信するには、{% raw %}`{% connected_content %}`{% endraw %} タグを使用します。このタグでは、`:save` を使用して変数を割り当てたり宣言したりできます。これらの変数の要素は、後でメッセージ内で [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) を使って参照できます。

### API コールの内訳 {#break-down-the-api-call}

次の例では、Sunrise-Sunset API を使用して、今日の日の出時刻をメッセージに含めています。

{% raw %}
```
{% connected_content https://api.sunrise-sunset.org/v2?lat=40.7128&lng=-74.0060&date=today :save result %}
Hi there, today's sunrise in NYC is at {{result.sunrise}}.
```
{% endraw %}

各部分の役割は次のとおりです。

| コンポーネント | 役割 |
| --- | --- |
| `connected_content` タグ | メッセージのレンダリング時に HTTP リクエストを行うよう Braze に指示します。 |
| `https://api.sunrise-sunset.org/v2` | Braze が呼び出す API エンドポイントです。 |
| `lat=40.7128&lng=-74.0060` | ニューヨーク市の座標を指定するクエリパラメーターです。 |
| `date=today` | その座標における当日のデータをリクエストします。 |
| `:save result` | API レスポンスを `result` という名前のローカル変数に保存します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="API コールの内訳" }

### Sunrise-Sunset API レスポンスの仕組み {#how-the-sunrise-sunset-api-response-works}

このエンドポイントは、`sunrise`、`sunset`、`tzid` などのトップレベルフィールドを含む JSON を返します。時刻はデフォルトでその場所のタイムゾーンで返されます（この例ではニューヨーク時間）。

たとえば、レスポンスの形式は次のようになります。

```json
{
  "date": "2026-07-23",
  "tzid": "America/New_York",
  "sunrise": "2026-07-23T05:42:11-04:00",
  "sunset": "2026-07-23T20:21:32-04:00"
}
```

### API レスポンスを Liquid にマッピングする {#map-the-api-response-to-liquid}

レスポンスは `result` として保存されるため、そのオブジェクトから各フィールドを直接参照できます。

{% raw %}
```liquid
{{result.sunrise}}
{{result.sunset}}
{{result.tzid}}
```
{% endraw %}

Connected Content から JSON を保存する場合は、常にこのパターンを使用します。

1. `:save` で API レスポンスを保存します。
2. JSON レスポンスから必要なフィールドを見つけます。
3. Liquid で `saved_variable.field_name` として参照します。

### 変数を追加する {#add-variables}

Connected Content リクエストを行う際に、URL 文字列の変数としてユーザープロファイル属性を含めることもできます。

たとえば、ユーザーのメールアドレスと ID に基づいてコンテンツを返す Web サービスがあるとします。アットマーク（@）などの特殊文字を含む属性を渡す場合は、次のメールアドレス属性の例に示すように、Liquid フィルター `url_param_escape` を使用して、URL で許可されていない文字を URL に適した形式のエスケープバージョンに置き換えてください。

{% raw %}
```
Hi, here are some articles that you might find interesting:

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```
{% endraw %}
{% alert note %}
属性値は、Braze の Liquid 構文で正しく動作するために、`${}` で囲む必要があります。
{% endalert %}

Connected Content リクエストでは、GET リクエストと POST リクエストのみがサポートされています。

## エラー処理 {#error-handling}

URL が利用できず 404 ページに到達した場合、Braze はその箇所に空の文字列をレンダリングします。URL が HTTP 500 または 502 ページに到達した場合、URL はリトライロジックで失敗します。

エンドポイントが JSON を返す場合、`connected` の値が null かどうかを確認し、[条件付きでメッセージを中止する]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content)ことで検出できます。Braze はポート 80 (HTTP) および 443 (HTTPS) で通信する URL のみを許可します。

### 異常ホスト検出 {#unhealthy-host-detection}

Connected Content は、ターゲットホストが著しい低速化や過負荷の高い発生率を経験し、タイムアウト、過剰なリクエスト、または Braze がターゲットエンドポイントとの通信を正常に行えないその他の結果が生じた場合に検出する、異常ホスト検出メカニズムを採用しています。これは、ターゲットホストの問題の原因となっている可能性のある不要な負荷を軽減するためのセーフガードとして機能します。また、Braze インフラの安定化とメッセージング速度の維持にも役立ちます。

ターゲットホストが著しい低速化や過負荷の高い発生率を経験した場合、Braze はターゲットホストへのリクエストを一時的に 1 分間停止し、代わりに失敗を示すレスポンスをシミュレートします。1 分後、Braze は少数のリクエストを使用してホストの正常性をプローブし、ホストが正常であることが確認された場合、フルスピードでリクエストを再開します。ホストがまだ異常な場合、Braze はさらに 1 分待ってから再試行します。

異常ホスト検出器によってターゲットホストへのリクエストが停止された場合、Braze はエラーレスポンスコードを受信した場合と同様に、メッセージのレンダリングと Liquid ロジックの実行を続行します。異常ホスト検出器によって停止された Connected Content リクエストを確実にリトライしたい場合は、`:retry` オプションを使用してください。`:retry` オプションの詳細については、[Connected Content のリトライ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries)を参照してください。

異常ホスト検出が問題を引き起こしていると思われる場合は、[Braze サポート]({{site.baseurl}}/support_contact)にお問い合わせください。

{% alert note %}
Connected Content に使用する特定の URL を許可リストに追加できます。この機能を利用するには、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

{% alert tip %}
一般的なエラーコードの詳細については、[Webhook と Connected Content リクエストのトラブルシューティング]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#unhealthy-host-detection)を参照してください。
{% endalert %}

### レート制限 (429) と異常ホスト検出の違い {#rate-limits-429-versus-unhealthy-host-detection}

以下は異なるメカニズムです。

- **429 Too Many Requests:** エンドポイント（または上流のサービス）がこのレスポンスを返しています。これは、サーバーまたはミドルウェアが独自のレート制限を持っていることが多いため、トラフィックを拒否していることを意味します。Braze は Connected Content に個別のレート制限を適用しません。Connected Content のリクエスト量は、[メッセージ配信速度のレート制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting)に直接比例します。メッセージは受信者ごとに複数回レンダリングされる可能性があるため（例えば、メールの HTML、プレーンテキスト、AMP）、Connected Content リクエストの数はそのレート制限を超える場合があります。設定した1分あたりのメッセージ数以下になるとは想定しないでください。429 エラーが発生する場合は、予想されるリクエスト量を処理できるようにエンドポイントまたはミドルウェアをスケールするか、キャンペーンまたはキャンバスの[配信速度のレート制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting)を下げて、1分あたりに送信されるメッセージ（つまり Connected Content 呼び出し）の数を減らしてください。
- **異常ホスト検出:** 1 分間のウィンドウ内で高い発生率と量の*失敗*が発生した後にトリガーされる、Braze 側のセーフガードです。失敗カウントには `408`、`429`、`502`、`503`、`504`、`529` のステータスコードが含まれます。トリガーされると、Braze はそのホストへのリクエストを一時的に停止し、失敗レスポンスをシミュレートします。これはお客様独自のレート制限とは独立しています。検出しきい値と詳細については、[Webhook と Connected Content リクエストのトラブルシューティング]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#unhealthy-host-detection)を参照してください。異常ホスト検出のトリガーを回避するには、[Connected Content の呼び出し量を理解する](#understanding-connected-content-call-volume)および[大量エンドポイントのベストプラクティス](#best-practices-for-high-volume-endpoints)で説明されている呼び出し量をエンドポイントが処理できることを確認してください。

## 効率的なパフォーマンスの確保 {#allowing-for-efficient-performance}

Brazeは非常に高速にメッセージを配信するため、コンテンツの取得時にオーバーロードしないよう、サーバーが数千の同時接続を処理できることを確認してください。パブリックAPIを使用する場合は、APIプロバイダーが設定しているレート制限に違反しないことを確認してください。Brazeはパフォーマンス上の理由から、サーバーのレスポンス時間が2秒未満であることを要求しています。サーバーのレスポンスに2秒以上かかる場合、コンテンツは挿入されません。

エンドポイントのキャパシティ計画と呼び出し量の削減については、[大量エンドポイントのベストプラクティス](#best-practices-for-high-volume-endpoints)を参照してください。

## 知っておくべきこと {#things-to-know}

- Brazeは API コールに対して課金せず、所定のデータポイント使用量にもカウントされません。
- Connected Contentのレスポンスには1 MBの制限があります。
- Connected Contentはメッセージがレンダリングされるときに実行されます。アプリ内メッセージの場合、メッセージはインプレッション時にレンダリングされます。
- Connected Contentコールはリダイレクトに従いません。`2xx` レスポンスのみが成功として扱われます。エンドポイントが`3xx`リダイレクト（例: `301`や`302`）を返す場合、Brazeはリダイレクト先の最終URLに従いません。症状やトラブルシューティング手順については、[エンドポイントがリダイレクトを返すとConnected Contentが失敗するのはなぜですか？](#why-does-connected-content-fail-when-my-endpoint-returns-a-redirect-301-or-302)を参照してください。

### Connected Contentコールの処理方法 {#how-connected-content-calls-are-processed}

単一のメッセージテンプレート内のConnected Contentコールは、Liquidレンダリング中に順番に（上から下へ）実行されます。つまり、下流のコールは上流のコールで設定された変数を参照できます。この例では、最初のコールがユーザーデータを取得し、2番目のコールがそのデータを使用してプリファレンスを取得します。

{% raw %}
```liquid
{% connected_content https://api.example.com/user :save user_data %}
{% connected_content https://api.example.com/preferences?user_id={{user_data.id}} :save preferences %}
```
{% endraw %}

### グローバル送信とリクエストボリューム {#global-sending-and-request-volume}

Connected Contentコールは単一メッセージ内では順番に実行されますが、メッセージはキャンペーンやキャンバス全体で並列に送信されます。大量送信では、ピーク送信期間中にエンドポイントに対して大量のリクエストトラフィックが発生する可能性があります。このトラフィックの管理とスロットリング（ワークスペースのメッセージングレート制限、配信速度のレート制限、キャッシュなど）については、[大量エンドポイントのベストプラクティス](#best-practices-for-high-volume-endpoints)を参照してください。

## 大量送信エンドポイントのベストプラクティス {#best-practices-for-high-volume-endpoints}

メッセージでConnected Contentを使用し、大量に送信する場合は、受信者数や送信数を超えるリクエストを想定して計画してください。

- **ピーク負荷を見積もる:** エンドポイントやミドルウェアのサイジングには、控えめな倍率を使用してください。Connected Contentのリクエストは、受信者数やメッセージ送信数を超えることがあります。たとえばメールの場合、1人の受信者に対して複数の呼び出し（HTML、プレーンテキスト、AMP）が発生する可能性があるため、受信者数 × 2 または × 3 が控えめな見積もりとしてよく使用されます。
- **適切な場合はキャッシュを使用する:** GETリクエストはデフォルトでキャッシュされます。POSTリクエストの場合は、レスポンスが一定期間再利用できる場合（たとえば、リクエストごとに変わらないトークンやコンテンツ）に `:cache_max_age` を追加してください。[レスポンスのキャッシュ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses)および次のセクションの[POSTキャッシュに関するFAQ](#what-is-caching-behavior)を参照してください。
- **メッセージのレート制限を設定する:** [ワークスペースのメッセージングレート制限]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits)およびキャンペーンやキャンバスの[配信速度のレート制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting)は、Connected Contentのリクエスト量を間接的に制限します。Braze自体がConnected Contentをレート制限することはありません。Connected Contentのリクエストはメッセージと1対1ではないため、これらは近似的な手段であり、完全なものではありません。エンドポイントが処理できる範囲内にメッセージ（ひいてはConnected Content）のボリュームを抑えるために活用してください。
- **冪等性とリトライを考慮した設計にする:** Brazeは1人の受信者に対してエンドポイントを複数回呼び出す場合があります。エンドポイントが重複リクエストを受けても、不正な副作用なく処理できるようにしてください。

## 認証タイプ {#authentication-types}

### ベーシック認証の使用 {#using-basic-authentication}

URL にベーシック認証が必要な場合、Braze は API 呼び出しで使用するベーシック認証の認証情報を保存できます。既存のベーシック認証の認証情報を管理したり、新しい認証情報を追加したりするには、**設定** > **Connected Content** に移動します。

![Braze ダッシュボードの Connected Content 設定。]({% image_buster /assets/img/connected_content/basic_auth_mgmt.png %})

新しい認証情報を追加するには、**認証情報を追加** > **ベーシック認証**を選択します。

![ベーシック認証またはトークン認証を使用するオプションがある「認証情報を追加」ドロップダウン。]({% image_buster /assets/img/connected_content/add_credential_button.png %}){: style="max-width:60%"}

認証情報に名前を付け、ユーザー名とパスワードを入力します。

![名前、ユーザー名、パスワードを入力するオプションがある「新しい認証情報を作成」ウィンドウ。]({% image_buster /assets/img/connected_content/basic_auth_token.png %}){: style="max-width:60%"}

その後、トークンの名前を参照することで、API 呼び出しでこのベーシック認証の認証情報を使用できます。

{% raw %}
```
Hi there, here is some fun trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
認証情報を削除する場合、その認証情報を使用しようとする Connected Content 呼び出しはすべて中止されることに注意してください。
{% endalert %}

保存された認証情報は、Braze がメッセージをレンダリングする際に {% raw %}`{% connected_content %}`{% endraw %} リクエストに適用されます。[Webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#authentication-and-connected-content-credentials) ステップで設定されたプライマリ HTTP リクエストには適用されません。その呼び出しのためにシークレットを取得する必要がある場合は、リクエストヘッダーを使用するか、Webhook のヘッダーまたはボディフィールド内に {% raw %}`{% connected_content %}`{% endraw %} タグを使用してください。

### トークン認証の使用 {#using-token-authentication}

Braze の Connected Content を使用する際、一部の API ではユーザー名とパスワードの代わりにトークンが必要になる場合があります。Braze はトークン認証のヘッダー値を保持する認証情報も保存できます。

トークン値を保持する認証情報を追加するには、**認証情報を追加** > **トークン認証**を選択します。次に、API 呼び出しヘッダーのキーと値のペアと許可されたドメインを追加します。

![トークン認証の詳細を含むトークン「token_credential_abc」の例。]({% image_buster /assets/img/connected_content/token_auth.png %}){: style="max-width:60%"}

その後、認証情報名を参照することで、API 呼び出しでこの認証情報を使用できます。

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

一部の API 設定では、アクセスしたい API エンドポイントの認証に使用できるアクセストークンの取得が必要です。

#### ステップ 1: アクセストークンを取得する {#step-1-retrieve-the-access-token}

次の例は、アクセストークンを取得してローカル変数に保存し、後続の API 呼び出しの認証に使用する方法を示しています。`:cache_max_age` パラメーターを追加して、アクセストークンの有効期間に合わせ、アウトバウンドの Connected Content 呼び出し数を削減できます。詳細については、[設定可能なキャッシュ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses)を参照してください。

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
トークンエンドポイントが `application/x-www-form-urlencoded` を期待し、認証情報を `:body` で渡す場合、パラメーター値の特殊文字を URL エンコードしてください。たとえば、スラッシュ（`/`）は `%2F` に、プラス記号（`+`）は `%2B` になります。エンコードされていない特殊文字があると、OAuth トークンリクエストが失敗する場合があります。
{% endalert %}

#### ステップ 2: 取得したアクセストークンを使用して API を認可する {#step-2-authorize-the-api-using-the-retrieved-access-token}

トークンが保存されたら、後続の Connected Content 呼び出しに動的にテンプレート化してリクエストを認可できます。

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

- ベーシック認証の場合、ユーザー名とパスワードを更新できます。以前に入力したパスワードは表示されませんのでご注意ください。
- トークン認証の場合、ヘッダーのキーと値のペアと許可されたドメインを更新できます。以前に設定されたヘッダー値は表示されませんのでご注意ください。

## Connected Content IPアローリスティング {#connected-content-ip-allowlisting}

Connected Contentを使用するメッセージがBrazeから送信されると、Brazeサーバーは自動的に顧客またはサードパーティのサーバーにネットワークリクエストを行い、データを取得します。IPアローリスティングを使用すると、Connected Contentリクエストが実際にBrazeから送信されていることを確認でき、セキュリティの層を追加できます。

BrazeはConnected Contentリクエストを以下のIP範囲から送信します。リストされた範囲は、アローリスティングにオプトインされたAPIキーに自動的かつ動的に追加されます。

Brazeには、すべてのサービスに使用される予約済みのIPセットがあり、特定の時点ですべてがアクティブであるとは限りません。これは、必要に応じて、Brazeが顧客に影響を与えることなく、別のデータセンターから送信したりメンテナンスを行ったりできるように設計されています。BrazeはConnected Contentリクエストを行う際に、以下にリストされたIPの1つ、一部、またはすべてを使用する場合があります。

Connected Contentリクエストが一貫して `403 Forbidden` を返し、認証が正しく設定されている場合は、リクエストを受信するサーバーでこれらのIPをアローリストに追加してください。`403` は権限不足や無効な認証情報を示す場合もあるため、ネットワークと認証の両方の設定を確認してください。Webhook固有のガイダンスについては、[403 ForbiddenとIPアローリスティング]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#403-forbidden-and-ip-allowlisting)を参照してください。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### Amazon S3でのIPアローリスティングの使用 {#using-ip-allowlisting-with-amazon-s3}

Connected Contentを使用してAmazon S3からファイルを取得する場合、BrazeのIPアドレスからの非認証HTTP `GET` リクエストを許可するようにバケットを設定します。

1. **IP条件付きのバケットポリシーを追加する:** `Principal: "*"` と、インスタンスの[BrazeのIP範囲](#connected-content-ip-allowlisting)を使用する `IpAddress` 条件を指定して、バケットオブジェクトに `s3:GetObject` を付与します。個々のオブジェクトにパブリック読み取りACLを設定する必要はありません。

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*",
      "Condition": {
        "IpAddress": {
          "aws:SourceIp": ["{YOUR_BRAZE_IP_RANGE}"]
        }
      }
    }
  ]
}
```

`{YOUR_BRAZE_IP_RANGE}` を[Connected Content IPアローリスティング](#connected-content-ip-allowlisting)にリストされているインスタンスのBrazeのIP範囲に置き換えます。`aws:SourceIp` 配列に個別の値として1つ以上の範囲を追加できます。

{: start="2"}
2. **S3ブロックパブリックアクセス設定を確認する:** `Principal: "*"` を使用するバケットポリシーは、IP条件が設定されていても、AWSによってパブリックアクセスとして扱われます。ACLベースのパブリックアクセスをブロックしたまま、バケットポリシーベースのパブリックアクセスを許可する必要がある場合があります。

3. **Connected ContentタグでS3オブジェクトURLを使用する:** 標準のS3 URLでオブジェクトを参照します（例：`https://your-bucket.s3.amazonaws.com/path/to/object.json`）。

バケットポリシーと条件キーの詳細については、[AWSドキュメント](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html)を参照してください。

## 送信リクエストヘッダー {#outgoing-request-headers}

{% multi_lang_include connected_content/outgoing_request_headers.md %}

Webhookリクエストでは、`User-Agent` ヘッダーを設定していない場合、`Braze Sender` で始まる `User-Agent` も送信されます。

## トラブルシューティング {#troubleshooting}

Connected Contentの呼び出しが正しくレンダリングされない、またはまったくレンダリングされない場合は、以下の項目を確認してください。

- **ライブリクエストとレスポンスを検査する:** **プレビューとテスト**の[Connected Contentデバッガー]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/debugger)を使用します。
- **Connected Contentの呼び出しが行われたことを確認する:** [メッセージング履歴タブ]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab)で呼び出しが行われたかどうかを確認できます。単一のConnected Contentリクエストをテスト送信することもできます。
- **PostmanまたはCURLリクエストで想定どおりのリクエストが成功するか検証する:** リクエストが機能してレスポンスが返される場合は、リクエストの詳細（ヘッダーを含む）を比較してください。ヘッダーがダブルクォーテーション付きのキーと値のペアでキャプチャされていることを確認してください。
- **認証が正しく処理されていることを検証する:** `:basic_auth`/`:auth_credentials`オプションが使用されており、Connected Contentの認証がConnected Contentワークスペース設定に追加されていることを確認してください。Connected Content URLには認証以外のヘッダーが必要な場合があり、それらを入力する必要があります。
- **データが期待される形式であることを検証する:** レスポンスボディについて、Brazeは有効なJSONをLiquidオブジェクトにパースします。それ以外の場合、レスポンスはプレーンテキスト（HTMLを含む）として扱われます。`:content_type`オプションはリクエストの送信`Content-Type`および`Accept`ヘッダーを設定しますが、レスポンスのパースには影響しません。リクエストの`:body`について、JSONにスペースが含まれている場合は、[JSONボディの提供]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/local_connected_content_variables#providing-json-body)セクションのガイダンスに従ってください。
- **データが正しくパースされたことを確認する:** Liquidが期待されるフィールドを正しく参照しているか確認してください。ネストされたJSONの場合は、{% raw %}`{{sampleresult.data[0].sample_field}}`{% endraw %}を使用して目的のネストされたフィールドを指定します。ネストされたJSONプロパティは、{% raw %}`RESPONSE:{{sampleresult.data}}`{% endraw %}で期待される結果を出力することで確認できます。
- **レスポンスステータスコードを確認する:** レスポンスステータスコードは`2XX`コードである必要があります。Connected Contentでは、コードが`2XX`でない場合にレスポンスを利用する方法はありません。

**プレビューとテスト**でプレビューを生成し、**詳細を表示**を選択して[Connected Contentデバッガー]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/debugger)を開きます。デバッガーには、Connected Contentタグからのヘッダーが一覧表示されます。Brazeが送信リクエストに追加するヘッダーについては、[送信リクエストヘッダー](#outgoing-request-headers)を参照してください。

また、Liquidタグにエンドポイントが期待するパラメーター（例: `:method`、`:headers`、`:content_type`、`:body`、必要に応じて`:basic_auth`）が含まれていることも確認できます。保存されたJSONオブジェクトのHTTPステータスコードキーに依存している場合、エンドポイントはJSONオブジェクトと`2XX`ステータスを返す必要があります。

ホストからのエラーレートが高い場合は、[異常ホスト検出]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content)および[Connected Contentの呼び出しボリューム](#understanding-connected-content-call-volume)を確認してください。

### メールPOSTリクエストでのアンパサンドエンコーディング {#ampersand-encoding-in-email-post-requests}

メールメッセージでは、HTMLパースにより{% raw %}`{% capture %}`{% endraw %}ブロック内のアンパサンド（`&`）が自動的に`&amp;`に変換されます。`application/x-www-form-urlencoded`のPOSTリクエストでは、これによりリクエストがパラメーター名に`amp;`プレフィックスを付けて送信される（例: `amp;username`）ため、API呼び出しが失敗する可能性があります。

この問題を回避するには、`replace`フィルターを使用して、ボディを`:body`に渡す前に`amp;`プレフィックスを削除します。

{% raw %}
```liquid
{% capture body_with_amps %}
grant_type=client_credentials&username=test&password=test
{% endcapture %}
{% connected_content https://api.example.com/token
   :method post
   :body {{body_with_amps | replace: "amp;", ""}}
   :content_type application/x-www-form-urlencoded
   :save token
%}
```
{% endraw %}

## よくある質問 {#frequently-asked-questions}

### エンドポイントがリダイレクト（301 または 302）を返すと Connected Content が失敗するのはなぜですか？ {#why-does-connected-content-fail-when-my-endpoint-returns-a-redirect-301-or-302}

リダイレクトにより、Connected Content がプレビューや送信時に空白で表示されたり、メッセージアクティビティログに HTTP ステータスコード `301` または `302` のエラーが記録されたりすることがあります。Postman やその他のクライアントはリダイレクトを自動的にフォローすることが多いため、Postman では動作する URL が Braze では失敗することがあります。

エンドポイントを設定して、Braze が呼び出す URL でレスポンスボディを含む `2xx` レスポンス（通常は `200`）を返すようにしてください。その URL 自体がリダイレクトを返す場合は、最終的なリダイレクト先 URL に置き換えてください。

コンテンツが空白で表示される場合の関連チェックについては、[Connected Content がレスポンスボディを返さない]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#connected-content-returns-no-response-body)を参照してください。

### Connected Content の呼び出しがユーザー数や送信数よりも多いのはなぜですか？ {#why-are-there-more-connected-content-calls-than-users-or-sends}

Braze は、メッセージペイロードをレンダリングするために、受信者1人あたり同じ Connected Content API 呼び出しを複数回行うことがあります。メッセージペイロードは、バリデーション、リトライロジック、その他の内部目的のために、受信者1人あたり複数回レンダリングされることがあります。ただし、Connected Content の呼び出しのうちメッセージに反映されるのは1回のみです。

リトライロジックが呼び出しで使用されていない場合でも、Connected Content API 呼び出しが受信者1人あたり複数回行われることは想定される動作です。Connected Content を含むメッセージにレート制限を設定するか、メッセージ送信あたり複数回の Connected Content 呼び出しが行われることを考慮した予想ボリュームを処理できるようサーバーを構成することをお勧めします。

詳細と軽減策については、[Connected Content の呼び出しボリュームについて](#understanding-connected-content-call-volume)と[大量トラフィックのエンドポイントに関するベストプラクティス](#best-practices-for-high-volume-endpoints)を参照してください。

### Connected Content でレート制限はどのように機能しますか？ {#how-does-rate-limiting-work-with-connected-content}

Connected Content には独自のレート制限はありません。代わりに、レート制限はメッセージ送信レートに基づいています。送信されるメッセージよりも Connected Content の呼び出しが多い場合は、メッセージングのレート制限を意図する Connected Content のレート制限よりも高く設定することをお勧めします。

### キャッシュの動作はどうなっていますか？ {#what-is-caching-behavior}

GET リクエストはデフォルトでキャッシュされます（[レスポンスのキャッシュ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses)を参照）。**POST リクエストはデフォルトではキャッシュされません**が、Connected Content の呼び出しに `:cache_max_age` を追加することでキャッシュを有効にできます。これにより、同じ POST（例えばトークンやコンテンツのリクエスト）がキャッシュウィンドウ内で繰り返し行われる場合のエンドポイント負荷を軽減できます。

{% raw %}
```liquid
{% connected_content https://api.example.com/token :method post :body grant_type=client_credentials :cache_max_age 900 :save token %}
```
{% endraw %}

キャッシュは重複する Connected Content の呼び出しを削減するのに役立ちますが、ユーザーあたり1回の呼び出しになることが保証されるわけではありません。キャッシュの期間は5分から4時間です。詳細については、[レスポンスのキャッシュ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses)を参照してください。

### Connected Content の HTTP デフォルト動作は何ですか？ {#what-is-the-connected-content-http-default-behavior}

{% multi_lang_include connected_content/sections.md section='default behavior' %}

{% multi_lang_include connected_content/sections.md section='http post' %}

### 同じ Connected Content の呼び出しを複数の場所で使用するとどうなりますか？ {#what-happens-if-i-use-the-same-connected-content-call-in-multiple-places}

各 Connected Content タグは、複数のタグが同じ URL とパラメーターを使用している場合でも個別に評価されます。URL とキャッシュ設定が許可する場合、同一のリクエストは新しいアウトバウンドリクエストをトリガーするのではなくキャッシュから提供されることがあります（詳細は[レスポンスのキャッシュ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses)を参照してください）。