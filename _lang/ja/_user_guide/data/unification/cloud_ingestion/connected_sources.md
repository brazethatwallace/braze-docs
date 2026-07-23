---
nav_title: 接続されたソース
article_title: 接続されたソース
description: "このページでは、Brazeのクラウドデータ取り込みを使用して、関連するデータをSnowflake、Redshift、BigQuery、およびDatabricksの連携と同期する方法について説明します。"
page_order: 2
page_type: reference

---

# 接続されたソース {#connected-sources}

> 接続されたソースは、Brazeのクラウドデータ取り込み（CDI）機能を使ってデータを直接同期するのではなく、ゼロコピーの代替手段です。接続されたソースはデータウェアハウスに直接クエリを行い、基盤となるデータをBrazeに一切コピーせずに新しいセグメントを作成します。

接続されたソースをBrazeワークスペースに追加すると、セグメントエクステンション内にCDIセグメントを作成できます。CDIセグメントエクステンションを使えば、データウェアハウスを直接クエリするSQLを記述し（CDI接続ソースを通じて利用可能になったデータを使用）、Braze内でターゲティング可能なユーザーグループを作成・維持できます。

このソースでセグメントを作成する方法の詳細については、[CDIセグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments)を参照してください。

{% alert warning %}
接続されたソースはデータウェアハウス上で直接実行されるため、データウェアハウスでこれらのクエリの実行に関連するすべてのコストが発生します。接続されたソースはデータポイントをログに記録せず、CDIセグメントエクステンションはSQLセグメントクレジットを消費しません。
{% endalert %}

## 接続ソースの統合 {#integrating-connected-sources}

### ステップ1: リソースを接続する {#step-1-connect-your-resources}

クラウドデータ取り込みの接続ソースには、Brazeとお使いのインスタンスの両方でいくつかの設定が必要です。以下のステップに従って統合を設定してください。一部のステップはデータウェアハウスで、一部のステップはBrazeダッシュボードで行います。

{% tabs %}
{% tab Snowflake %}
**データウェアハウスで**
1. ロールを作成し、スキーマ内のテーブルのクエリと作成の権限を付与します。
2. ウェアハウスを設定し、そのロールにアクセス権を付与します。
3. そのロール用のユーザーを作成します。
4. 構成によっては、SnowflakeのネットワークポリシーでBrazeのIPアドレスを許可する必要がある場合があります。

**Brazeダッシュボードで**

{: start="5"}
5. Brazeダッシュボードで新しい接続ソースを作成します。
6. 接続ソースの同期の詳細を設定します。
7. Brazeダッシュボードで提供される公開キーを取得します。

**データウェアハウスで**

{: start="8"}
8. Brazeダッシュボードの公開キーを[認証用のSnowflakeユーザー](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)に追加します。完了したら、接続ソースを使用して1つ以上のCDIセグメントエクステンションを作成できます。
{% endtab %}

{% tab Redshift %}
1. Redshift環境でソースデータと必要なリソースを設定します。
2. Brazeダッシュボードで新しい接続ソースを作成します。
3. 統合をテストします。
4. 接続ソースを使用して1つ以上のCDIセグメントエクステンションを作成します。
{% endtab %}

{% tab BigQuery %}
1. BigQuery環境でソースデータと必要なリソースを設定します。
2. サービスアカウントを作成し、同期するデータを含むBigQueryプロジェクトとデータセットへのアクセスを許可します。
3. Brazeダッシュボードで新しい接続ソースを作成します。
4. 統合をテストします。
5. 接続ソースを使用して1つ以上のCDIセグメントエクステンションを作成します。
{% endtab %}

{% tab Databricks %}
1. Databricks環境でソースデータと必要なリソースを設定します。
2. サービスアカウントを作成し、同期するデータを含むDatabricksプロジェクトとデータセットへのアクセスを許可します。
3. Brazeダッシュボードで新しい接続ソースを作成します。
4. 統合をテストします。
5. 接続ソースを使用して1つ以上のCDIセグメントエクステンションを作成します。

{% alert important %}
BrazeがClassicおよびPro SQLインスタンスに接続する際、2〜5分のウォームアップ時間が発生する場合があり、接続の設定やテスト、CDIセグメントエクステンションの作成や更新時に遅延が生じることがあります。サーバーレスSQLインスタンスを使用するとウォームアップ時間を最小限に抑え、クエリのスループットを向上させることができますが、統合コストがやや高くなる場合があります。
{% endalert %}

{% endtab %}

{% tab Microsoft Fabric %}
1. サービスプリンシパルを作成し、統合に使用するFabricワークスペースへのアクセスを許可します。
2. Fabricワークスペースでソースデータを設定し、サービスプリンシパルに権限を付与します。
3. Brazeダッシュボードで新しい接続ソースを作成します。
4. 統合をテストします。
5. 接続ソースを使用して1つ以上のCDIセグメントエクステンションを作成します。
{% endtab %}

{% endtabs %}

### ステップ2: データウェアハウスを設定する {#step-2-set-up-your-data-warehouse}

データウェアハウス環境でソースデータと必要なリソースを設定します。接続ソースは1つ以上のテーブルを参照できるため、Brazeユーザーが接続ソース内の必要なすべてのテーブルにアクセスできる権限を持っていることを確認してください。

{% tabs %}
{% tab Snowflake %}
#### ステップ2.1: ロールを作成し権限を付与する {#step-21-create-a-role-and-grant-permissions}

接続ソースで使用するロールを作成します。このロールは、CDIセグメントエクステンションで利用可能なテーブルのリストを生成し、ソーステーブルをクエリして新しいセグメントを作成するために使用されます。接続ソースが作成されると、Brazeはソーススキーマ内でユーザーが利用可能なすべてのテーブルの名前と説明を検出します。

スキーマ内のすべてのテーブルへのアクセスを付与するか、特定のテーブルのみに権限を付与するかを選択できます。Brazeロールがアクセスできるテーブルはすべて、CDIセグメントエクステンションでクエリに使用できます。

`create table`権限は、BrazeがCDIセグメントエクステンションのクエリ結果を使用してテーブルを作成し、Brazeでセグメントを更新するために必要です。Brazeはセグメントごとに一時テーブルを作成し、そのテーブルはBrazeがセグメントを更新している間のみ保持されます。

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT CREATE TABLE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;

-- grant access to all current and future tables or views in the schema
GRANT SELECT ON ALL TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON FUTURE TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;

-- grant access to specific tables or views in the schema
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;

```

#### ステップ2.2: ウェアハウスを設定しBrazeロールにアクセスを付与する {#step-22-set-up-the-warehouse-and-give-access-to-braze-role}

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
ウェアハウスには**auto-resume**フラグがオンになっている必要があります。オンになっていない場合、クエリの実行時にBrazeがウェアハウスをオンにできるよう、ウェアハウスに対する追加の`OPERATE`権限をBrazeに付与する必要があります。
{% endalert %}

#### ステップ2.3: ユーザーを設定する {#step-23-set-up-the-user}
```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

接続情報をBrazeと共有し、後のステップでユーザーに追加する公開キーを受け取ります。

{% alert note %}
異なるワークスペースを同じSnowflakeアカウントに接続する場合、統合を作成する各Brazeワークスペースに対して一意のユーザーを作成する必要があります。ワークスペース内では、統合間で同じユーザーを再利用できますが、同じSnowflakeアカウント上のユーザーがワークスペース間で重複している場合、統合の作成は失敗します。
{% endalert %}

#### ステップ2.4: SnowflakeネットワークポリシーでBrazeのIPを許可する（オプション） {#step-24-allow-braze-ips-in-your-snowflake-network-policy-optional}

Snowflakeアカウントの構成によっては、Snowflakeのネットワークポリシーで以下のIPアドレスを許可する必要がある場合があります。この方法の詳細については、[ネットワークポリシーの変更](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies)に関するSnowflakeの関連ドキュメントを参照してください。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}
{% endtab %}

{% tab Redshift %}
#### ステップ2.1: ユーザーを作成し権限を付与する {#step-21-create-user-and-grant-permissions}

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT CREATE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

接続ソースで使用するユーザーを作成します。このユーザーは、CDIセグメントエクステンションで利用可能なテーブルのリストを生成し、ソーステーブルをクエリして新しいセグメントを作成するために使用されます。接続ソースが作成されると、Brazeはソーススキーマ内でユーザーが利用可能なすべてのテーブルの名前と説明を検出します。複数のCDI統合を作成する場合は、スキーマに対して権限を付与するか、グループを使用して権限を管理することをお勧めします。

スキーマ内のすべてのテーブルへのアクセスを付与するか、特定のテーブルのみに権限を付与するかを選択できます。Brazeロールがアクセスできるテーブルはすべて、CDIセグメントエクステンションでクエリに使用できます。新しいテーブルが作成された際には、ユーザーにアクセス権を付与するか、デフォルトの権限を設定してください。

`create table`権限は、BrazeがCDIセグメントエクステンションのクエリ結果を使用してテーブルを作成し、Brazeでセグメントを更新するために必要です。Brazeはセグメントごとに一時テーブルを作成し、そのテーブルはBrazeがセグメントを更新している間のみ保持されます。


#### ステップ2.2: BrazeのIPへのアクセスを許可する {#step-22-allow-access-to-braze-ips}

ファイアウォールやその他のネットワークポリシーがある場合は、RedshiftインスタンスへのネットワークアクセスをBrazeに付与する必要があります。Brazeダッシュボードのリージョンに対応する以下のIPからのアクセスを許可してください。

また、RedshiftのデータへのBrazeアクセスを許可するために、セキュリティグループの変更が必要になる場合があります。以下のセクションのIPアドレスと、Redshiftクラスターのクエリに使用するポート（デフォルトは5439）でのインバウンドトラフィックを明示的に許可してください。インバウンドルールが「すべて許可」に設定されている場合でも、このポートでのRedshift TCP接続を明示的に許可する必要があります。また、Brazeがクラスターに接続するためには、Redshiftクラスターのエンドポイントがパブリックにアクセス可能である必要があります。

Redshiftクラスターをパブリックにアクセス可能にしたくない場合は、VPCとEC2インスタンスを設定してSSHトンネルを使用し、Redshiftデータにアクセスできます。詳細については、[AWS: ローカルマシンからプライベートAmazon Redshiftクラスターにアクセスする方法](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)を参照してください。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% tab BigQuery %}
#### ステップ2.1: サービスアカウントを作成し権限を付与する {#step-21-create-a-service-account-and-grant-permissions}

GCPでBrazeがテーブルに接続してデータを読み取るためのサービスアカウントを作成します。サービスアカウントには以下のセクションの権限が必要です：

- **BigQuery Connection User:** Brazeが接続を行うことを許可します。
- **BigQuery User:** Brazeにクエリの実行、データセットメタデータの読み取り、テーブルの一覧表示へのアクセスを提供します。
- **BigQuery Data Viewer:** Brazeにデータセットとその内容の表示へのアクセスを提供します。
- **BigQuery Job User:** Brazeにジョブの実行へのアクセスを提供します。
- **bigquery.tables.create** セグメントの更新時にBrazeが一時テーブルを作成するためのアクセスを提供します。

接続ソースで使用するサービスアカウントを作成します。このユーザーは、CDIセグメントエクステンションで利用可能なテーブルのリストを生成し、ソーステーブルをクエリして新しいセグメントを作成するために使用されます。接続ソースが作成されると、Brazeはソーススキーマ内でユーザーが利用可能なすべてのテーブルの名前と説明を検出します。

データセット内のすべてのテーブルへのアクセスを付与するか、特定のテーブルのみに権限を付与するかを選択できます。Brazeロールがアクセスできるテーブルはすべて、CDIセグメントエクステンションでクエリに使用できます。

`create table`権限は、BrazeがCDIセグメントエクステンションのクエリ結果を使用してテーブルを作成し、Brazeでセグメントを更新するために必要です。Brazeはセグメントごとに一時テーブルを作成し、そのテーブルはBrazeがセグメントを更新している間のみ保持されます。

サービスアカウントを作成して権限を付与した後、JSONキーを生成します。詳細については、[Google Cloud: サービスアカウントキーの作成と削除](https://cloud.google.com/iam/docs/keys-create-delete)を参照してください。このキーは後でBrazeダッシュボードにアップロードします。

#### ステップ2.2: BrazeのIPへのアクセスを許可する

ネットワークポリシーが設定されている場合は、BigQueryインスタンスへのネットワークアクセスをBrazeに付与する必要があります。Brazeダッシュボードのリージョンに対応する以下のIPからのアクセスを許可してください。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Databricks %}
#### ステップ2.1: アクセストークンを作成する {#step-21-create-an-access-token}

BrazeがDatabricksにアクセスするには、パーソナルアクセストークンを作成する必要があります。

1. Databricksワークスペースで、上部バーのDatabricksユーザー名を選択し、ドロップダウンから**User Settings**を選択します。
2. サービスアカウントが接続ソースに使用するスキーマに対して`CREATE TABLE`権限を持っていることを確認します。
3. **Access tokens**タブで、**Generate new token**を選択します。
4. このトークンを識別するのに役立つコメント（「Braze CDI」など）を入力し、Lifetime (days)ボックスを空白のままにしてトークンの有効期限を無期限に変更します。
5. **Generate**を選択します。
6. 表示されたトークンをコピーし、**Done**を選択します。

このトークンは、CDIセグメントエクステンションで利用可能なテーブルのリストを生成し、ソーステーブルをクエリして新しいセグメントを作成するために使用されます。接続ソースが作成されると、Brazeはソーススキーマ内でユーザーが利用可能なすべてのテーブルの名前と説明を検出します。

スキーマ内のすべてのテーブルへのアクセスを付与するか、特定のテーブルのみに権限を付与するかを選択できます。Brazeロールがアクセスできるテーブルはすべて、CDIセグメントエクステンションでクエリに使用できます。

`create table`権限は、BrazeがCDIセグメントエクステンションのクエリ結果を使用してテーブルを作成し、Brazeでセグメントを更新するために必要です。Brazeはセグメントごとに一時テーブルを作成し、そのテーブルはBrazeがセグメントを更新している間のみ保持されます。

認証情報の作成ステップでBrazeダッシュボードに入力する必要があるまで、トークンを安全な場所に保管してください。

#### ステップ2.2: BrazeのIPへのアクセスを許可する

ネットワークポリシーが設定されている場合は、DatabricksインスタンスへのネットワークアクセスをBrazeに付与する必要があります。Brazeダッシュボードのリージョンに対応する以下のIPからのアクセスを許可してください。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Microsoft Fabric %}
#### ステップ2.1: Fabricリソースへのアクセスを付与する {#step-21-grant-access-to-fabric-resources}
BrazeはEntra ID認証を使用するサービスプリンシパルでFabricウェアハウスに接続します。Brazeが使用する新しいサービスプリンシパルを作成し、必要に応じてFabricリソースへのアクセスを付与します。Brazeが接続するには以下の情報が必要です：

{% multi_lang_include data_unification/azure_service_principal_credentials.md %}

{% multi_lang_include data_unification/azure_app_registration_steps.md %}

{% alert note %}
Azureではサービスプリンシパルのシークレットに無期限の有効期限を設定できません。Brazeへのデータフローを維持するために、認証情報の有効期限が切れる前に更新することを忘れないでください。
{% endalert %}

#### ステップ2.2: Fabricリソースへのアクセスを付与する {#step-22-grant-access-to-fabric-resources}
BrazeがFabricインスタンスに接続するためのアクセスを提供します。Fabric管理ポータルで、**Settings** > **Governance and insights** > **Admin portal** > **Tenant settings**に移動します。

* **Developer settings**で「Service principals can use Fabric APIs」を有効にして、BrazeがMicrosoft Entra IDを使用して接続できるようにします。
* **OneLake settings**で「Users can access data stored in OneLake with apps external to Fabric」を有効にして、サービスプリンシパルが外部アプリからデータにアクセスできるようにします。

#### ステップ2.3: ウェアハウスの接続文字列を取得する {#step-23-get-warehouse-connection-string}

Brazeが接続するには、ウェアハウスのSQLエンドポイントが必要です。SQLエンドポイントを取得するには、Fabricの**ワークスペース**に移動し、アイテムのリストでウェアハウス名にカーソルを合わせ、**Copy SQL connection string**を選択します。
この値はステップ3の認証情報設定で使用するため、保存しておいてください。

#### ステップ2.4: ファイアウォールでBrazeのIPを許可する（オプション） {#step-24-allow-braze-ips-in-firewall-optional}

Microsoft Fabricアカウントの構成によっては、Brazeからのトラフィックを許可するために、ファイアウォールで以下のIPアドレスを許可する必要がある場合があります。この有効化の詳細については、[Entra条件付きアクセス](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access)に関する関連ドキュメントを参照してください。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### ステップ3: Brazeダッシュボードで接続ソースを作成する {#step-3-create-a-connected-source-in-the-braze-dashboard}

{% tabs %}
{% tab Snowflake %}
#### ステップ3.1: Snowflakeの接続情報とソーステーブルを追加する {#step-31-add-snowflake-connection-information-and-source-table}

Brazeダッシュボードで接続ソースを作成します。**Data Settings** > **Cloud Data Ingestion** > **Connected Sources**に移動し、**Add data source**を選択してから**Snowflake**を選択します。

**Setup source**で以下を入力します：
- **Credentials:** **Account Locator**、**Username**、**Role**
- **Configuration:** **Warehouse**、**Database**、**Schema**

新しいSnowflake認証情報を作成する場合は、接続をテストする前に**Save credentials and generate RSA key**を選択します。

#### ステップ3.2: 同期の詳細を設定する {#step-32-configure-sync-details}

接続ソースの名前を選択します。この名前は、新しいCDIセグメントエクステンションを作成する際に利用可能なソースのリストに表示されます。

このソースの最大実行時間を設定します。Brazeは最大実行時間を超えるクエリを自動的に中止します。許可される最大実行時間は60分です。実行時間を短くすると、Snowflakeアカウントで発生するコストを削減できます。この設定は、このソースを通じて実行されるクエリ（同期やこのソースを使用するCDIセグメントエクステンションを含む）に適用されます。

{% alert note %}
クエリが常にタイムアウトし、最大実行時間を60分に設定している場合は、クエリの実行時間を最適化するか、Brazeユーザーにより大きなウェアハウスを割り当てることを検討してください。
{% endalert %}

#### ステップ3.3: 公開キーを記録する {#step-33-note-the-public-key}

**Test connection**ステップで、RSA公開キーを記録します。Snowflakeでの統合を完了するために必要になります。

{% endtab %}
{% tab Redshift %}
#### ステップ3.1: Redshiftの接続情報とソーステーブルを追加する {#step-31-add-redshift-connection-information-and-source-table}

Brazeダッシュボードで接続ソースを作成します。**Data Settings** > **Cloud Data Ingestion** > **Connected Sources**に移動し、**Add data source**を選択してから**Amazon Redshift**を選択します。

**Setup source**で以下を入力します：
- **Credentials:** **Redshift Host URL**、**Username**、**Password**、**Port**
- **Configuration:** **Database**、**Schema**

必要に応じて、**Connect with SSH Tunnel**を有効にし、**Tunnel Host**、**Tunnel Port**、**Tunnel Username**を入力します。

#### ステップ3.2: 同期の詳細を設定する

接続ソースの名前を選択します。この名前は、新しいCDIセグメントエクステンションを作成する際に利用可能なソースのリストに表示されます。

このソースの最大実行時間を設定します。Brazeは最大実行時間を超えるクエリを自動的に中止します。許可される最大実行時間は60分です。実行時間を短くすると、Redshiftアカウントで発生するコストを削減できます。
この設定は、このソースを通じて実行されるクエリ（同期やこのソースを使用するCDIセグメントエクステンションを含む）に適用されます。

{% alert note %}
クエリが常にタイムアウトし、最大実行時間を60分に設定している場合は、クエリの実行時間を最適化するか、Brazeユーザーにより大きなウェアハウスを割り当てることを検討してください。
{% endalert %}

#### ステップ3.3: 公開キーを記録する（オプション） {#step-33-note-the-public-key-optional}

認証情報で**Connect with SSH Tunnel**が選択されている場合は、**Test connection**ステップでRSA公開キーを記録します。Redshiftでの統合を完了するために必要になります。

{% endtab %}
{% tab BigQuery %}
#### ステップ3.1: BigQueryの接続情報とソーステーブルを追加する {#step-31-add-bigquery-connection-information-and-source-table}

Brazeダッシュボードで接続ソースを作成します。**Data Settings** > **Cloud Data Ingestion** > **Connected Sources**に移動し、**Add data source**を選択してから**Google BigQuery**を選択します。

**Setup source**で以下を入力します：
- **Credentials:** **Credential name**と**JSONキー**のアップロード
- **Configuration:** **Project**、**Dataset**

#### ステップ3.2: 同期の詳細を設定する

接続ソースの名前を選択します。この名前は、新しいCDIセグメントエクステンションを作成する際に利用可能なソースのリストに表示されます。

このソースの最大実行時間を設定します。Brazeは最大実行時間を超えるクエリを自動的に中止します。許可される最大実行時間は60分です。実行時間を短くすると、BigQueryアカウントで発生するコストを削減できます。この設定は、このソースを通じて実行されるクエリ（同期やこのソースを使用するCDIセグメントエクステンションを含む）に適用されます。

{% alert note %}
クエリが常にタイムアウトし、最大実行時間を60分に設定している場合は、クエリの実行時間を最適化するか、Brazeユーザーにより大きなウェアハウスを割り当てることを検討してください。
{% endalert %}

#### ステップ3.3: 接続をテストする {#step-33-test-the-connection}

**Test Connection**を選択して、ユーザーに表示されるテーブルのリストが期待どおりであることを確認し、**Done**を選択します。接続ソースが作成され、CDIセグメントエクステンションで使用する準備が整いました。

{% endtab %}
{% tab Databricks %}
#### ステップ3.1: Databricksの接続情報とソーステーブルを追加する {#step-31-add-databricks-connection-information-and-source-table}

Brazeダッシュボードで接続ソースを作成します。**Data Settings** > **Cloud Data Ingestion** > **Connected Sources**に移動し、**Add data source**を選択してから**Databricks**を選択します。

**Setup source**で以下を入力します：
- **Credentials:** **Credential Name**、**Hostname**、**HTTP Path**、**Access Token**
- **Configuration:** **Catalog**、**Schema**

#### ステップ3.2: 同期の詳細を設定する

接続ソースの名前を選択します。この名前は、新しいCDIセグメントエクステンションを作成する際に利用可能なソースのリストに表示されます。

このソースの最大実行時間を設定します。Brazeは最大実行時間を超えるクエリを自動的に中止します。許可される最大実行時間は60分です。実行時間を短くすると、Databricksアカウントで発生するコストを削減できます。この設定は、このソースを通じて実行されるクエリ（同期やこのソースを使用するCDIセグメントエクステンションを含む）に適用されます。

{% alert note %}
クエリが常にタイムアウトし、最大実行時間を60分に設定している場合は、クエリの実行時間を最適化するか、Brazeユーザーにより大きなウェアハウスを割り当てることを検討してください。
{% endalert %}

#### ステップ3.3: 接続をテストする

**Test Connection**を選択して、ユーザーに表示されるテーブルのリストが期待どおりであることを確認し、**Done**を選択します。接続ソースが作成され、CDIセグメントエクステンションで使用する準備が整いました。

{% endtab %}
{% tab Microsoft Fabric %}
#### ステップ3.1: Microsoft Fabricの接続情報とソーステーブルを追加する {#step-31-add-microsoft-fabric-connection-information-and-source-table}

Brazeダッシュボードで接続ソースを作成します。**Data Settings** > **Cloud Data Ingestion** > **Connected Sources**に移動し、**Add data source**を選択してから**Microsoft Fabric**を選択します。

**Setup source**で以下を入力します：
- **Credentials:** **Credentials Name**、**Tenant ID**、**Principal ID**、**Client Secret**、**Connection String**
- **Configuration:** **Database**、**Schema**

ワークスペースで**Connect with SSH Tunnel**が利用可能で、設定に必要な場合は、**Tunnel Host**、**Tunnel Port**、**Tunnel Username**も入力します。

#### ステップ3.2: 同期の詳細を設定する

接続ソースの名前を選択します。この名前は、新しいCDIセグメントエクステンションを作成する際に利用可能なソースのリストに表示されます。

このソースの最大実行時間を設定します。Brazeは最大実行時間を超えるクエリを自動的に中止します。許可される最大実行時間は60分です。実行時間を短くすると、Microsoft Fabricアカウントで発生するコストを削減できます。この設定は、このソースを通じて実行されるクエリ（同期やこのソースを使用するCDIセグメントエクステンションを含む）に適用されます。

{% alert note %}
クエリが常にタイムアウトし、最大実行時間を60分に設定している場合は、クエリの実行時間を最適化するか、Fabricのキャパシティをスケーリングすることを検討してください。
{% endalert %}

#### ステップ3.3: 接続をテストする

**Test Connection**を選択して、ユーザーに表示されるテーブルのリストが期待どおりであることを確認し、**Done**を選択します。接続ソースが作成され、CDIセグメントエクステンションで使用する準備が整いました。

{% endtab %}
{% endtabs %}

### ステップ4: データウェアハウスの設定を完了する {#step-4-finalize-the-data-warehouse-configuration}

{% tabs %}
{% tab Snowflake %}
前のステップで記録した公開キーをSnowflakeのユーザーに追加します。これにより、BrazeがSnowflakeに接続できるようになります。この方法の詳細については、[Snowflakeのドキュメント](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)を参照してください。

キーをローテーションしたい場合は、**Cloud Data Ingestion**の**Data Access Management**に移動し、該当するアカウントの**Generate New Key**を選択して新しい公開キーを作成できます。

```sql
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='{INSERT_YOUR_KEY}';
```

Snowflakeのユーザーにキーを追加した後、Brazeで**Test Connection**を選択し、**Done**を選択します。接続ソースが作成され、CDIセグメントエクステンションで使用する準備が整いました。
{% endtab %}

{% tab Redshift %}
SSHトンネルで接続する場合は、前のステップで記録した公開キーをSSHトンネルユーザーに追加します。

ユーザーにキーを追加した後、Brazeで**Test Connection**を選択し、**Done**を選択します。接続ソースが作成され、CDIセグメントエクステンションで使用する準備が整いました。

{% endtab %}
{% tab BigQuery %}
BigQueryには該当しません。

{% endtab %}
{% tab Databricks %}
Databricksには該当しません。

{% endtab %}
{% tab Microsoft Fabric %}
Microsoft Fabricには該当しません。

{% endtab %}
{% endtabs %}

{% alert note %}
ソースが「下書き」状態から「アクティブ」状態に移行するには、テストに成功する必要があります。作成ページを閉じる必要がある場合でも、統合は保存されるため、詳細ページに戻って変更やテストを行うことができます。
{% endalert %}

## 追加のインテグレーションまたはユーザーの設定（オプション） {#setting-up-additional-integrations-or-users-optional}

{% tabs %}
{% tab Snowflake %}
Brazeとの複数のインテグレーションを設定できますが、各インテグレーションは異なるスキーマに接続するように構成する必要があります。追加の接続を作成する際、同じSnowflakeアカウントに接続する場合は既存の認証情報を再利用できます。

インテグレーション間で同じユーザーとロールを再利用する場合、公開キーを再度追加する必要はありません。
{% endtab %}

{% tab Redshift %}
Brazeとの複数のデータソースを設定できますが、各データソースは異なるスキーマに接続するように構成する必要があります。追加のデータソースを作成する際、同じRedshiftアカウントに接続する場合は既存の認証情報を再利用できます。
{% endtab %}

{% tab BigQuery %}
Brazeとの複数のデータソースを設定できますが、各データソースは異なるデータセットに接続するように構成する必要があります。追加のデータソースを作成する際、同じBigQueryアカウントに接続する場合は既存の認証情報を再利用できます。
{% endtab %}

{% tab Databricks %}
Brazeとの複数のデータソースを設定できますが、各データソースは異なるスキーマに接続するように構成する必要があります。追加のデータソースを作成する際、同じDatabricksアカウントに接続する場合は既存の認証情報を再利用できます。
{% endtab %}

{% tab Microsoft Fabric %}
Brazeとの複数のデータソースを設定できますが、各データソースは異なるスキーマに接続するように構成する必要があります。追加のデータソースを作成する際、同じAzureアカウントに接続する場合は既存の認証情報を再利用できます。
{% endtab %}
{% endtabs %}

## 接続済みソースの使用 {#using-the-connected-source}

ソースが作成されたら、それを使用して1つ以上のCDIセグメントエクステンションを作成できます。このソースを使用してセグメントを作成する方法の詳細については、[CDIセグメントエクステンションのドキュメント]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments)を参照してください。

{% alert note %}
クエリが常にタイムアウトし、最大実行時間を60分に設定している場合は、クエリの実行時間を最適化するか、Brazeユーザーにより多くのコンピューティングリソース（より大きなデータウェアハウスなど）を割り当てることを検討してください。
{% endalert %}