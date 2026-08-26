Brazeは、送信されるConnected Contentリクエストに以下のヘッダーを追加します。ほとんどのヘッダーは、タグ内でまだ指定されていない場合にのみ設定されます。`:headers`、認証情報、またはタグオプションで指定したヘッダーは、指定した通りに送信されます。

| ヘッダー | Brazeが設定するタイミング |
| --- | --- |
| `User-Agent` | まだ設定されていない場合、Brazeは`Braze Sender <version>`を送信します。バージョン文字列は変更される場合があります。`User-Agent`でトラフィックをフィルタリングする場合は、`Braze Sender`で始まるすべての値を許可してください。一貫した値を送信するには、`:headers`で`User-Agent`を設定してください。 |
| `X-Braze-Sender-Version` | 常にConnected Contentの送信元バージョンに設定されます。 |
| `Accept-Encoding` | まだ設定されていない場合、Brazeは`gzip`を送信します。 |
| `Authorization` | URLにユーザー名とパスワード（`user:pass@host`）が含まれている場合、Brazeはその認証情報から導出されたBasic `Authorization`ヘッダーを追加します。明示的な`Authorization`ヘッダーはこれを上書きします。URLに認証情報を含めるのではなく、[`:basic_auth`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#using-basic-authentication)または`:headers`の使用をお勧めします。 |
| `Host` | `Host`ヘッダーを設定しない限り、リクエストURLのホスト名です（例：`https://www.example.com/abc/123`の場合は`www.example.com`）。 |
| `Content-Length` | ボディが存在する場合のリクエストボディのバイト単位のサイズです。 |
| `BrazeToBraze` | Braze RESTエンドポイントへのリクエストに対してのみ`true`に設定されます。その他の送信先では省略されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Connected Contentに追加される送信リクエストヘッダー" }