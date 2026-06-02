## サポートされるデータタイプ {#supported-data-types}

以下のデータタイプがサポートされています。

<table aria-label="サポートされるデータタイプ">
  <thead>
    <tr>
      <th>データタイプ</th>
      <th>説明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>数値</td>
      <td><code>1</code> や <code>5.5</code> などの数値です。</td>
    </tr>
    <tr>
      <td>文字列</td>
      <td><code>"Hello"</code> や <code>"The Hobbit"</code> などのテキスト値です。</td>
    </tr>
    <tr>
      <td>ブール値</td>
      <td><code>true</code> または <code>false</code> のいずれかに評価される値です。</td>
    </tr>
    <tr>
      <td>配列</td>
      <td><code>["red", "blue", "green"]</code> などの値のリストです。</td>
    </tr>
    <tr>
      <td>時刻</td>
      <td>
        日付と時刻の比較に使用されるタイムスタンプ値です。ネストされた時刻カスタム属性をフィルターする際に、以下を選択できます。<br><br>
        <ul>
          <li><strong>Day of Year</strong>: <code>03-15</code> のように、月と日のみを比較対象としてチェックします。</li>
          <li><strong>Time</strong>: <code>2023-03-15T12:00:00Z</code> のように、年を含む完全なタイムスタンプを比較します。</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>オブジェクト</td>
      <td><code>{"author": "Tolkien"}</code> のようなキーと値のペアを持つ構造化された値です。</td>
    </tr>
    <tr>
      <td>オブジェクトの配列</td>
      <td>
        <code>[{"title": "The Hobbit"}, {"title": "Dune"}]</code> のようなオブジェクトのリストです。
        詳細については、<a href="{{site.baseurl}}/array_of_objects/">オブジェクトの配列</a> を参照してください。
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 aria-label="Supported data types" }