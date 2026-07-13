<ul>
<li><code>dispatch_id</code>は、キャンペーン送信などの特定のメッセージディスパッチのIDです。同じディスパッチから発生するすべてのプッシュイベントには、同じ<code>dispatch_id</code>が含まれます。<code>dispatch_id</code>を使用して同じディスパッチに属するイベントをグループ化することで、そのディスパッチにおけるプッシュメッセージのライフサイクル（送信、バウンス、開封など）をまとめて関連付けることができます。</li>
<li><code>state_change_source</code>は、完全なソース名の文字列を返します。たとえば、ソースがCSVインポートの場合、文字列<code>CSV import</code>を返します。利用可能なソースは以下のとおりです。</li>
</ul>
<table class="reset-td-br-1 reset-td-br-2" role="presentation">
<thead>
<tr><th>ソース</th><th>説明</th></tr>
</thead>
<tbody>
<tr><td>SDK</td><td>SDKエンドポイント</td></tr>
<tr><td>ダッシュボード</td><td>ダッシュボードのユーザープロファイルページからユーザーの購読状態が更新された場合</td></tr>
<tr><td>サブスクリプションページ</td><td>ユーザー設定センター以外のメールリンクを介してユーザーが購読解除した場合</td></tr>
<tr><td>REST API</td><td>REST APIエンドポイント</td></tr>
<tr><td>CSVインポート</td><td>CSVユーザーインポート</td></tr>
<tr><td>ユーザー設定センター</td><td>ユーザー設定センターからユーザーが更新された場合</td></tr>
<tr><td>受信メッセージ</td><td>SMSなどのチャネルを通じたエンドユーザーからの受信メッセージによってユーザーが更新された場合</td></tr>
<tr><td>移行</td><td>内部移行またはメンテナンススクリプトによってユーザーが更新された場合</td></tr>
<tr><td>ユーザーマージ</td><td>ユーザーマージ処理によってユーザーが更新された場合</td></tr>
<tr><td>キャンバスユーザー更新ステップ</td><td>キャンバスユーザー更新ステップによってユーザーが更新された場合</td></tr>
</tbody>
</table>