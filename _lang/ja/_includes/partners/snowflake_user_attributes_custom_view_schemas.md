{% if include.schema == "history" %}

| カラム名     | データ型     | 説明 |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Brazeワークスペースの識別子 |
| `USER_ID` | VARCHAR | Brazeの一意のユーザー識別子 |
| `APP_ID` | VARCHAR | ワークスペース内の特定のアプリ |
| `EXTERNAL_USER_ID` | VARCHAR | ユーザー独自の識別子（設定されている場合） |
| `TIME` | NUMBER | プロファイル更新のUnixタイムスタンプ（秒） |
| `TIME_MS` | NUMBER | プロファイル更新のUnixタイムスタンプ（ミリ秒） |
| `UPDATE_SOURCE` | VARCHAR | 属性更新のソース（API、SDK、ダッシュボードなど） |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Snowflakeでデータが最後に更新された日時 |
| `CUSTOM_ATTRIBUTES` | VARIANT | すべてのカスタム属性（キーと値のペア）を含むJSONオブジェクト |
| `ARCHIVED` | BOOLEAN | ユーザープロファイルがアーカイブされているかどうか |
| `EFF_DT` | TIMESTAMP_NTZ | 有効日：この属性状態が開始された日時 |
| `END_DT` | TIMESTAMP_NTZ | 終了日：この属性状態が終了した日時（現在の状態の場合はNULL） |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERCUSTOMATTRIBUTESHISTORYVIEWSHARED schema" }

{% elsif include.schema == "latest" %}

| カラム名     | データ型     | 説明 |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Brazeワークスペースの識別子 |
| `USER_ID` | VARCHAR | Brazeの一意のユーザー識別子 |
| `EXTERNAL_USER_ID` | VARCHAR | ユーザー独自の識別子（設定されている場合） |
| `TIME` | NUMBER | プロファイル更新のUnixタイムスタンプ（秒） |
| `TIME_MS` | NUMBER | プロファイル更新のUnixタイムスタンプ（ミリ秒） |
| `UPDATE_SOURCE` | VARCHAR | 属性更新のソース（API、SDK、ダッシュボードなど） |
| `ARCHIVED` | BOOLEAN | ユーザープロファイルがアーカイブされているかどうか |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Snowflakeでデータが最後に更新された日時 |
| `APP_ID` | VARCHAR | ワークスペース内の特定のアプリ |
| `CUSTOM_ATTRIBUTES` | OBJECT | すべてのカスタム属性（キーと値のペア）を含むJSONオブジェクト |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERLATESTSTATECUSTOMATTRIBUTEVIEWSHARED schema" }

{% alert note %}
このビューでは、`CUSTOM_ATTRIBUTES` に `VARIANT` ではなく `OBJECT` 型を使用します。個々の属性をクエリするには、同じJSONアクセサー構文（`:attribute_name::TYPE`）を使用してください。
{% endalert %}

{% endif %}