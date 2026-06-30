---
nav_title: 接続されたソース
article_title: 接続されたソース
description: "このページでは、Brazeのクラウドデータ取り込みを使用して、関連するデータをSnowflake、Redshift、BigQuery、およびDatabricksの連携と同期する方法について説明します。"
page_order: 2
page_type: reference

---

# 接続されたソース {#connected-sources}

> 接続されたソースは、Brazeのクラウドデータ取り込み（CDI）機能を使ってデータを直接同期するのではなく、ゼロコピーの代替手段です。接続されたソースはデータウェアハウスに直接クエリを行い、基盤となるデータをBrazeに一切コピーせずに新しいSegmentを作成します。

接続されたソースをBrazeワークスペースに追加すると、セグメントエクステンション内にCDI Segmentを作成できます。CDIセグメントエクステンションを使えば、データウェアハウスを直接クエリするSQLを記述し（CDI接続ソースを通じて利用可能になったデータを使用）、Braze内でターゲティング可能なユーザーグループを作成・維持できます。

このソースでSegmentを作成する方法の詳細については、[CDIセグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments)を参照してください。

{% alert warning %}
接続されたソースはデータウェアハウス上で直接実行されるため、データウェアハウスでこれらのクエリの実行に関連するすべてのコストが発生します。接続されたソースはデータポイントをログに記録せず、CDIセグメントエクステンションはSQLセグメントクレジットを消費しません。
{% endalert %}

## 接続されたソースの統合 {#integrating-connected-sources}

### ステップ1：リソースを接続する {#step-1-connect-your-resources}

クラウドデータ取り込みの接続されたソースは、Braze側とインスタンス側での設定が必要です。統合を設定するには、次の手順に従います。一部はデータウェアハウスで実行され、一部はBrazeダッシュボードで実行されます。

{% tabs %}
{% tab Snowflake %}
**データウェアハウスで次を行います。**
1. ロールを作成し、スキーマ内のテーブルのクエリと作成の権限を付与します。
2. ウェアハウスを設定し、そのロールにアクセス権を付与します。
3. そのロールのユーザーを作成します。
4. 設定によっては、SnowflakeネットワークポリシーでBraze IPを許可する必要があります。

**Brazeダッシュボードで次を行います。**

{: start="5"}
5. Brazeダッシュボードで接続されたソースを新規作成します。
6. 接続されたソースの同期の詳細を設定します。
7. Brazeダッシュボードで提供された公開キーを取得します。

**データウェアハウスで次を行います。**

{: start="8"}
8. Brazeダッシュボードの公開キーを[認証用のSnowflakeユーザー](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)に追加します。作業が終わったら、接続されたソースを使って1つ以上のCDIセグメントエクステンションを作成できます。
{% endtab %}

{% tab Redshift %}
1. Redshift環境にソースデータと必要なリソースをセットアップします。
2. Brazeダッシュボードで接続されたソースを新規作成します。
4. 統合をテストします。
5. 接続されたソースを使用して、1つ以上のCDIセグメントエクステンションを作成します。
{% endtab %}

{% tab BigQuery %}
1. BigQuery環境でソースデータと必要なリソースをセットアップします。
2. サービスアカウントを作成し、同期するデータを含むBigQueryのプロジェクトとデータセットへのアクセスを許可します。
3. Brazeダッシュボードで接続されたソースを新規作成します。
4. 統合をテストします。
5. 接続されたソースを使用して、1つ以上のCDIセグメントエクステンションを作成します。
{% endtab %}

{% tab Databricks %}
1. Databricks環境でソースデータと必要なリソースをセットアップします。
2. サービスアカウントを作成し、同期するデータを含むDatabricksのプロジェクトとデータセットへのアクセスを許可します。
3. Brazeダッシュボードで接続されたソースを新規作成します。
4. 統合をテストします。
5. 接続されたソースを使用して、1つ以上のCDIセグメントエクステンションを作成します。

{% alert important %}
BrazeがClassicおよびPro SQLインスタンスに接続する際、2分から5分のウォームアップ時間が発生する可能性があります。これにより、接続設定やテスト中、ならびにCDIセグメントエクステンションの作成や更新中に遅延が生じます。サーバーレスSQLインスタンスを使用すると、ウォームアップ時間が最小限に抑えられ、クエリのスループットが向上しますが、連携コストが若干高くなる場合があります。
{% endalert %}

{% endtab %}

{% tab Microsoft Fabric %}
1. サービスプリンシパルを作成し、統合に使用するFabricワークスペースへのアクセスを許可します。
2. Fabricワークスペースで、ソースデータを設定し、サービスプリンシパルに権限を付与します。
3. Brazeダッシュボードで接続されたソースを新規作成します。
4. 統合をテストします。
5. 接続されたソースを使用して、1つ以上のCDIセグメントエクステンションを作成します。
{% endtab %}

{% endtabs %}

### ステップ2：データウェアハウスをセットアップする {#step-2-set-up-your-data-warehouse}

データウェアハウス環境でソースデータと必要なリソースを設定します。接続されたソースは1つまたは複数のテーブルを参照する可能性があるため、Brazeユーザーが接続されたソース内の必要なすべてのテーブルにアクセスできる権限を持っていることを確認してください。

{% tabs %}
{% tab Snowflake %}
#### ステップ2.1：ロールを作成し、権限を付与する {#step-21-create-a-role-and-grant-permissions}

接続されたソースが使用するロールを作成します。このロールは、CDIセグメントエクステンションで利用可能なテーブルの一覧を生成し、ソーステーブルをクエリして新しいSegmentを作成するために使用されます。接続されたソースが作成されると、Brazeはソーススキーマ内のユーザーが利用可能なすべてのテーブルの名前と説明を検出します。

スキーマ内のすべてのテーブルにアクセス権を付与するか、特定のテーブルにのみ権限を付与するかを選択できます。Brazeのロールがアクセス権を持つテーブルは、すべてCDIセグメントエクステンションでクエリ可能となります。

`create table`権限は、BrazeがCDIセグメントエクステンションのクエリ結果をテーブルに作成し、その後Braze内でSegmentを更新するために必要です。BrazeはSegmentごとに一時テーブルを作成し、そのテーブルはBrazeがSegmentを更新している間だけ保持されます。

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

#### ステップ2.2：ウェアハウスの設定と、Brazeロールへのアクセス権の付与 {#step-22-set-up-the-warehouse-and-give-access-to-braze-role}

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
ウェアハウスの**自動再開**フラグをオンにする必要があります。オンになっていない場合は、Brazeがクエリの実行時にオンにできるように、Brazeに追加の`OPERATE`権限を付与する必要があります。
{% endalert %}

#### ステップ2.3：ユーザーの設定 {#step-23-set-up-the-user}
```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Brazeと接続情報を共有し、後のステップでユーザーに付加する公開キーを受け取ります。

{% alert note %}
異なるワークスペースを同じSnowflakeアカウントに接続する場合は、連携を作成するBrazeワークスペースごとに一意のユーザーを作成する必要があります。ワークスペース内では、複数の連携にわたって同じユーザーを再利用できますが、同じSnowflakeアカウントのユーザーが複数のワークスペースで重複すると、連携の作成に失敗します。
{% endalert %}

#### ステップ2.4：Snowflakeネットワークポリシー内でBraze IPを許可する（省略可） {#step-24-allow-braze-ips-in-your-snowflake-network-policy-optional}

Snowflakeアカウントの設定によっては、Snowflakeのネットワークポリシー内で以下のIPアドレスを許可する必要があります。この方法の詳細については、[ネットワークポリシーの変更](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies)に関するSnowflakeの関連ドキュメントを参照してください。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}
{% endtab %}

{% tab Redshift %}
#### ステップ2.1：ユーザーの作成と権限の付与 {#step-21-create-user-and-grant-permissions}

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT CREATE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

接続されたソースが使用するユーザーを作成します。このユーザーは、CDIセグメントエクステンションで利用可能なテーブルの一覧を生成し、新しいSegmentを作成するためにソーステーブルをクエリするために使用されます。接続されたソースが作成されると、Brazeはソーススキーマ内のユーザーが利用可能なすべてのテーブルの名前と説明を検出します。CDI連携を複数作成する場合は、スキーマに権限を付与したり、グループを使用して権限を管理したりできます。

スキーマ内のすべてのテーブルにアクセス権を付与するか、特定のテーブルにのみ権限を付与するかを選択できます。Brazeのロールがアクセス権を持つテーブルは、すべてCDIセグメントエクステンションでクエリ可能となります。新しいテーブルを作成する際には、必ずそのユーザーにアクセス権を付与するか、そのユーザーにデフォルトのアクセス権を設定してください。

`create table`権限は、BrazeがCDIセグメントエクステンションのクエリ結果をテーブルに作成し、その後Braze内でSegmentを更新するために必要です。BrazeはSegmentごとに一時テーブルを作成し、BrazeがSegmentを更新している間だけ保持されます。


#### ステップ2.2：Braze IPへのアクセスの許可 {#step-22-allow-access-to-braze-ips}

ファイアウォールや他のネットワークポリシーがある場合は、RedshiftインスタンスにBrazeネットワークへのアクセスを許可する必要があります。Brazeダッシュボードのリージョンに対応する以下のIPからのアクセスを許可してください。

また、RedshiftのデータへのアクセスをBrazeに許可するように、セキュリティグループを変更しなければならないこともあります。以下のIPとRedshiftクラスターのクエリに使用するポート（デフォルトは5439）のインバウンドトラフィックを明示的に許可してください。インバウンドルールが「すべて許可」に設定されている場合でも、このポートでRedshift TCP接続を明示的に許可する必要があります。さらに、Brazeがクラスターにアクセスするために、Redshiftクラスターのエンドポイントがパブリックにアクセス可能であることが重要です。

Redshiftクラスターにパブリックアクセスを許可しない場合は、SSHトンネルを使用してRedshiftデータにアクセスするようにVPCとEC2インスタンスを設定できます。詳しくは、[AWS：ローカルマシンからAmazon Redshiftのプライベートクラスターにアクセスするには？](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)を参照してください。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% tab BigQuery %}
#### ステップ2.1：サービスアカウントの作成と権限の付与 {#step-21-create-a-service-account-and-grant-permissions}

GCPで、Brazeがテーブルに接続してデータを読み取るために使用するサービスアカウントを作成します。サービスアカウントには次の権限が必要です。

- **BigQuery Connection User：** Brazeに接続を許可します。
- **BigQuery User：** クエリの実行、データセットメタデータの読み取り、およびテーブルの一覧表示を行うためのアクセスをBrazeに提供します。
- **BigQuery Data Viewer：** データセットとその内容を閲覧するためのアクセスをBrazeに提供します。
- **BigQuery Job User：** ジョブを実行するためのアクセスをBrazeに提供します。
- **bigquery.tables.create：** Segment更新時に一時テーブルを作成するためのアクセスをBrazeに提供します。

接続されたソースが使用するサービスアカウントを作成します。このユーザーは、CDIセグメントエクステンションで利用可能なテーブルの一覧を生成し、新しいSegmentを作成するためにソーステーブルをクエリするために使用されます。接続されたソースが作成されると、Brazeはソーススキーマ内のユーザーが利用可能なすべてのテーブルの名前と説明を検出します。

データセット内のすべてのテーブルにアクセス権を付与するか、特定のテーブルだけに権限を付与するかを選択できます。Brazeのロールがアクセス権を持つテーブルは、すべてCDIセグメントエクステンションでクエリ可能となります。

`create table`権限は、BrazeがCDIセグメントエクステンションのクエリ結果をテーブルに作成し、その後Braze内でSegmentを更新するために必要です。BrazeはSegmentごとに一時テーブルを作成し、そのテーブルはBrazeがSegmentを更新している間だけ保持されます。

サービスアカウントを作成して権限を付与したら、JSONキーを生成します。詳しくは、[Google Cloud：サービスアカウントキーの作成と削除](https://cloud.google.com/iam/docs/keys-create-delete)を参照してください。これを後でBrazeダッシュボードにアップロードします。

#### ステップ2.2：Braze IPへのアクセスの許可

ネットワークポリシーを設定している場合は、BrazeにBigQueryインスタンスへのネットワークアクセスを許可する必要があります。Brazeダッシュボードのリージョンに対応する以下のIPからのアクセスを許可してください。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Databricks %}
#### ステップ2.1：アクセストークンを作成する {#step-21-create-an-access-token}

BrazeがDatabricksにアクセスするには、パーソナルアクセストークンを作成する必要があります。

1. Databricksワークスペースで、上部バーにあるDatabricksユーザー名をクリックし、ドロップダウンから**User Settings**を選択します。
2. サービスアカウントが接続されたソースで使用されるスキーマに対する`CREATE TABLE`権限を持っていることを確認してください。
3. **Access tokens**タブで、**Generate new token**を選択します。
4. 「Braze CDI」など、このトークンの識別に役立つコメントを入力し、Lifetime (days) ボックスを空（空白）のままにして、トークンの有効期間を無期限に変更します。
5. **Generate**を選択します。
6. 表示されたトークンをコピーして、**Done**を選択します。

このトークンは、CDIセグメントエクステンションで利用可能なテーブルのリストを生成し、ソーステーブルをクエリして新しいSegmentを作成するために使用されます。接続されたソースが作成されると、Brazeはソーススキーマ内のユーザーが利用可能なすべてのテーブルの名前と説明を検出します。

スキーマ内のすべてのテーブルにアクセス権を付与するか、特定のテーブルにのみ権限を付与するかを選択できます。Brazeのロールがアクセス権を持つテーブルは、すべてCDIセグメントエクステンションでクエリ可能となります。

`create table`権限は、BrazeがCDIセグメントエクステンションのクエリ結果をテーブルに作成し、その後Braze内でSegmentを更新するために必要です。BrazeはSegmentごとに一時テーブルを作成し、BrazeがSegmentを更新している間だけ保持されます。

認証情報の作成ステップでBrazeダッシュボードへの入力が必要になるまで、トークンを安全な場所に保管してください。

#### ステップ2.2：Braze IPへのアクセスの許可

ネットワークポリシーを設定している場合は、BrazeにDatabricksインスタンスへのネットワークアクセスを許可する必要があります。Brazeダッシュボードのリージョンに対応する以下のIPからのアクセスを許可してください。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Microsoft Fabric %}
#### ステップ2.1：Fabricリソースへのアクセスを許可する {#step-21-grant-access-to-fabric-resources}
BrazeはEntra ID認証でサービスプリンシパルを使用してFabricウェアハウスに接続します。Brazeが使用する新しいサービスプリンシパルを作成し、必要に応じてFabricリソースへのアクセスを許可します。Brazeの接続には以下の詳細が必要となります。

* AzureアカウントのテナントID（ディレクトリとも呼ばれます）
* サービスプリンシパルのプリンシパルID（アプリケーションIDとも呼ばれます）
* Brazeが認証するためのクライアントシークレット

1. Azureポータルで、Microsoft Entra管理センターに移動し、**App Registrations**を選択します。
2. **Identity** > **Applications** > **App registrations**で**+ New registration**を選択します。
3. 名前を入力し、サポートされているアカウントの種類として`Accounts in this organizational directory only`を選択します。次に、**Register**を選択します。
4. 作成したアプリケーション（サービスプリンシパル）を選択し、**Certificates & secrets** > **+ New client secret**に移動します。
5. シークレットの説明を入力し、有効期限を設定します。そして、**Add**を選択します。
6. Brazeのセットアップで使用するために作成したクライアントシークレットをメモしてください。

{% alert note %}
Azureでは、サービスプリンシパルシークレットの有効期限を無制限に設定することはできません。Brazeへのデータフローを維持するために、認証情報が失効する前に忘れずに更新してください。
{% endalert %}

#### ステップ2.2：Fabricリソースへのアクセスを許可する {#step-22-grant-access-to-fabric-resources}
BrazeがFabricインスタンスに接続するためのアクセスを提供します。Fabricの管理ポータルで、**Settings** > **Governance and insights** > **Admin portal** > **Tenant settings**の順に移動します。

* **Developer settings**で、「Service principals can use Fabric APIs」を有効にして、BrazeがMicrosoft Entra IDを使用して接続できるようにします。
* **OneLake settings**で、サービスプリンシパルが外部アプリからデータにアクセスできるように、「Users can access data stored in OneLake with apps external to Fabric」を有効にします。

#### ステップ2.3：ウェアハウスの接続文字列を取得する {#step-23-get-warehouse-connection-string}

Brazeを接続するには、ウェアハウスのSQLエンドポイントが必要です。SQLエンドポイントを取得するには、Fabricで**ワークスペース**に移動し、項目の一覧でウェアハウスの名前にカーソルを合わせ、**Copy SQL connection string**を選択します。

![Microsoft Azureの「Fabricコンソール」ページ。ユーザーはここでSQL接続文字列を取得します。]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})

#### ステップ2.4：ファイアウォールでBraze IPを許可する（オプション） {#step-24-allow-braze-ips-in-firewall-optional}

Microsoft Fabricアカウントの設定によっては、Brazeからのトラフィックを許可するように、ファイアウォールで以下のIPアドレスを許可する必要があります。これを有効にする方法の詳細については、[Entra Conditional Access](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access)の関連ドキュメントを参照してください。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### ステップ3：Brazeダッシュボードで接続されたソースを作成する {#step-3-create-a-connected-source-in-the-braze-dashboard}

{% tabs %}
{% tab Snowflake %}
#### ステップ3.1：Snowflakeの接続情報とソーステーブルの追加 {#step-31-add-snowflake-connection-information-and-source-table}

Brazeダッシュボードで接続されたソースを作成します。**データ設定** > **クラウドデータ取り込み** > **接続されたソース**の順に移動し、**Create new data sync** > **Snowflake Import**を選択します。

![新しいデータ同期を作成するオプションが表示された接続されたソースページ。]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Snowflakeデータウェアハウスとソーススキーマの情報を入力し、次のステップに進みます。

![ウェアハウスとソーススキーマのSnowflake接続フィールド。]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_1.png %})

#### ステップ3.2：同期の詳細の設定 {#step-32-configure-sync-details}

接続されたソースの名前を選択します。この名前は、新しいCDIセグメントエクステンションを作成する際に、利用可能なソースのリストで使用されます。

このソースの最大実行時間を設定します。Brazeは、Segmentを作成または更新する際に、最大実行時間を超えるクエリを自動的に中止します。許容される最大実行時間は60分です。実行時間を短くすると、Snowflakeアカウントに課金されるコストが削減されます。

{% alert note %}
クエリが常にタイムアウトしており、最大実行時間を60分に設定している場合は、クエリの実行時間を最適化するか、Brazeユーザーにより大きなウェアハウスを割り当てることを検討してください。
{% endalert %}

![Snowflakeの同期名と最大実行時間の設定。]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_2.png %})

#### ステップ3.3：公開キーを書き留める {#step-33-note-the-public-key}

**Test connection**ステップに表示されているRSA公開キーをメモします。Snowflakeでの統合を完了するために必要です。

![RSA公開キーが表示されたSnowflakeの接続テストステップ。]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_3.png %})

{% endtab %}
{% tab Redshift %}
#### ステップ3.1：Redshiftの接続情報とソーステーブルの追加 {#step-31-add-redshift-connection-information-and-source-table}

Brazeダッシュボードで接続されたソースを作成します。**データ設定** > **クラウドデータ取り込み** > **接続されたソース**の順に移動し、**Create data connection** > **Amazon Redshift Import**を選択します。

![新しいデータ同期を作成するオプションが表示された接続されたソースページ。]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Redshiftデータウェアハウスとソーススキーマの情報を入力し、次のステップに進みます。

![ウェアハウスとソーススキーマのRedshift接続フィールド。]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_1.png %})

#### ステップ3.2：同期の詳細の設定

接続されたソースの名前を選択します。この名前は、新しいCDIセグメントエクステンションを作成する際に、利用可能なソースのリストで使用されます。

このソースの最大実行時間を設定します。Brazeは、Segmentを作成または更新する際に、最大実行時間を超えるクエリを自動的に中止します。許容される最大実行時間は60分です。実行時間を短くすると、Redshiftアカウントに課金されるコストが削減されます。

{% alert note %}
クエリが常にタイムアウトしており、最大実行時間を60分に設定している場合は、クエリの実行時間を最適化するか、Brazeユーザーにより大きなウェアハウスを割り当てることを検討してください。
{% endalert %}

![Redshiftの同期名と最大実行時間の設定。]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_2.png %})

#### ステップ3.3：公開キーを書き留める（省略可） {#step-33-note-the-public-key-optional}

認証情報で**Connect with SSH Tunnel**が選択されている場合は、**Test connection**ステップに表示されているRSA公開キーをメモします。Redshiftでの統合を完了するために必要です。

![RSA公開キーが表示されたRedshiftの接続テストステップ。]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_3.png %})

{% endtab %}
{% tab BigQuery %}
#### ステップ3.1：BigQueryの接続情報とソーステーブルの追加 {#step-31-add-bigquery-connection-information-and-source-table}

Brazeダッシュボードで接続されたソースを作成します。**データ設定** > **クラウドデータ取り込み** > **接続されたソース**の順に移動し、**Create new data sync** > **Google BigQuery Import**を選択します。

![新しいデータ同期を作成するオプションが表示された接続されたソースページ。]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

BigQueryプロジェクトとデータセットの情報を入力し、次のステップに進みます。

![BigQueryの接続情報とソーステーブルの追加に関するスクリーンショット。]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_1.png %})

#### ステップ3.2：同期の詳細の設定

接続されたソースの名前を選択します。この名前は、新しいCDIセグメントエクステンションを作成する際に、利用可能なソースのリストで使用されます。

このソースの最大実行時間を設定します。Brazeは、Segmentを作成または更新する際に、最大実行時間を超えるクエリを自動的に中止します。許容される最大実行時間は60分です。実行時間を短くすると、BigQueryアカウントに課金されるコストが削減されます。

{% alert note %}
クエリが常にタイムアウトしており、最大実行時間を60分に設定している場合は、クエリの実行時間を最適化するか、Brazeユーザーにより大きなウェアハウスを割り当てることを検討してください。
{% endalert %}

![同期の詳細の設定に関するスクリーンショット。]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_2.png %})

#### ステップ3.3：接続をテストする {#step-33-test-the-connection}

**Test Connection**を選択し、ユーザーに表示されるテーブルのリストが期待どおりであることを確認してから、**Done**を選択します。接続されたソースが作成され、CDIセグメントエクステンションで使用できる状態になりました。

![接続されたソースで利用可能なテーブルが表示された接続テストステップ。]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% tab Databricks %}
#### ステップ3.1：Databricksの接続情報とソーステーブルの追加 {#step-31-add-databricks-connection-information-and-source-table}

Brazeダッシュボードで接続されたソースを作成します。**データ設定** > **クラウドデータ取り込み** > **接続されたソース**の順に移動し、**Create new data sync** > **Databricks Import**を選択します。

![新しいデータ同期を作成するオプションが表示された接続されたソースページ。]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Databricks認証情報、オプションのカタログとソーススキーマの情報を入力してから、次のステップに進みます。

![認証情報とソーススキーマのDatabricks接続フィールド。]({% image_buster /assets/img/cloud_ingestion/connected_source_databricks_1.png %})

#### ステップ3.2：同期の詳細の設定

接続されたソースの名前を選択します。この名前は、新しいCDIセグメントエクステンションを作成する際に、利用可能なソースのリストで使用されます。

このソースの最大実行時間を設定します。Brazeは、Segmentを作成または更新する際に、最大実行時間を超えるクエリを自動的に中止します。許容される最大実行時間は60分です。実行時間を短くすると、Databricksアカウントに課金されるコストが削減されます。

{% alert note %}
クエリが常にタイムアウトしており、最大実行時間を60分に設定している場合は、クエリの実行時間を最適化するか、Brazeユーザーにより大きなウェアハウスを割り当てることを検討してください。
{% endalert %}

![Databricksの同期名と最大実行時間の設定。]({% image_buster /assets/img/cloud_ingestion/connected_source_db_2.png %})

#### ステップ3.3：接続をテストする

**Test Connection**を選択し、ユーザーに表示されるテーブルのリストが期待どおりであることを確認してから、**Done**を選択します。接続されたソースが作成され、CDIセグメントエクステンションで使用できる状態になりました。

![接続されたソースで利用可能なテーブルが表示された接続テストステップ。]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% tab Microsoft Fabric %}
#### ステップ3.1：Microsoft Fabricの接続情報とソーステーブルを追加する {#step-31-add-microsoft-fabric-connection-information-and-source-table}

Brazeダッシュボードで接続されたソースを作成します。**データ設定** > **クラウドデータ取り込み** > **接続されたソース**の順に移動し、**Create new data sync** > **Microsoft Fabric Import**を選択します。

![新しいデータ同期を作成するオプションが表示された接続されたソースページ。]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Microsoft Fabricの認証情報およびソースウェアハウス、スキーマの情報を入力し、次のステップに進みます。

![認証情報とソーススキーマのMicrosoft Fabric接続フィールド。]({% image_buster /assets/img/cloud_ingestion/connected_source_mf_1.png %})

#### ステップ3.2：同期の詳細の設定

接続されたソースの名前を選択します。この名前は、新しいCDIセグメントエクステンションを作成する際に、利用可能なソースのリストで使用されます。

このソースの最大実行時間を設定します。Brazeは、Segmentを作成または更新する際に、最大実行時間を超えるクエリを自動的に中止します。許容される最大実行時間は60分です。実行時間を短くすると、Microsoft Fabricアカウントに課金されるコストが削減されます。

{% alert note %}
クエリが常にタイムアウトしており、最大実行時間を60分に設定している場合は、クエリの実行時間を最適化するか、Fabric容量を拡張することを検討してください。
{% endalert %}

![Microsoft Fabricの同期名と最大実行時間の設定。]({% image_buster /assets/img/cloud_ingestion/connected_source_mf_2.png %})

#### ステップ3.3：接続をテストする

**Test Connection**を選択し、ユーザーに表示されるテーブルのリストが期待どおりであることを確認してから、**Done**を選択します。接続されたソースが作成され、CDIセグメントエクステンションで使用できる状態になりました。

![接続されたソースで利用可能なテーブルが表示された接続テストステップ。]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% endtabs %}

### ステップ4：データウェアハウスの構成を確定する {#step-4-finalize-the-data-warehouse-configuration}

{% tabs %}
{% tab Snowflake %}
最後のステップで書き留めた公開キーをSnowflakeのユーザーに追加します。これにより、BrazeがSnowflakeに接続できるようになります。この方法の詳細については、[Snowflakeのドキュメント](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)を参照してください。

任意の時点でキーのローテーションを行う場合は、新しい公開キーを作成できます。このためには、**クラウドデータ取り込み**の**Data Access Management**に移動し、該当するアカウントの**Generate New Key**を選択します。

![Snowflakeデータアクセスの認証情報のデータアクセス管理。新しいキーを生成するボタンが表示されています。]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_4.png %})

```sql
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='{INSERT_YOUR_KEY}';
```

Snowflakeでユーザーにキーを追加したら、Brazeで**Test Connection**を選択し、**Done**を選択します。接続されたソースが作成され、CDIセグメントエクステンションで使用できる状態になりました。
{% endtab %}

{% tab Redshift %}
SSHトンネルで接続する場合は、最後のステップで書き留めた公開キーをSSHトンネルユーザーに追加します。

ユーザーにキーを追加したら、Brazeで**Test Connection**を選択し、**Done**を選択します。接続されたソースが作成され、CDIセグメントエクステンションで使用できる状態になりました。

{% endtab %}
{% tab BigQuery %}
これはBigQueryには適用されません。

{% endtab %}
{% tab Databricks %}
これはDatabricksには適用されません。

{% endtab %}
{% tab Microsoft Fabric %}
これはMicrosoft Fabricには適用されません。

{% endtab %}
{% endtabs %}

{% alert note %}
「下書き」状態から「アクティブ」状態に移行する前に、ソースのテストに成功する必要があります。作成ページを閉じる必要がある場合は、連携が保存されるので、詳細ページに再度アクセスして変更やテストを行うことができます。
{% endalert %}

## 追加の統合またはユーザーを設定する（オプション） {#setting-up-additional-integrations-or-users-optional}

{% tabs %}
{% tab Snowflake %}
Brazeと複数の統合を設定できますが、各統合は異なるスキーマを接続するように設定する必要があります。追加の接続を作成する際、同じSnowflakeアカウントに接続する場合は既存の認証情報を再利用できます。

同じユーザーとロールを統合間で再利用する場合、公開キーを再度追加する必要はありません。
{% endtab %}

{% tab Redshift %}
Brazeで複数のソースを設定できますが、各ソースは異なるスキーマを接続するように設定する必要があります。追加のソースを作成する際、同じRedshiftアカウントに接続する場合は既存の認証情報を再利用できます。
{% endtab %}

{% tab BigQuery %}
Brazeで複数のソースを設定できますが、各ソースは異なるデータセットを接続するように設定する必要があります。追加のソースを作成する際、同じBigQueryアカウントに接続する場合は既存の認証情報を再利用できます。
{% endtab %}

{% tab Databricks %}
Brazeで複数のソースを設定できますが、各ソースは異なるスキーマを接続するように設定する必要があります。追加のソースを作成する際、同じDatabricksアカウントに接続する場合は既存の認証情報を再利用できます。
{% endtab %}

{% tab Microsoft Fabric %}
Brazeで複数のソースを設定できますが、各ソースは異なるスキーマを接続するように設定する必要があります。追加のソースを作成する際、同じAzureアカウントに接続する場合は既存の認証情報を再利用できます。
{% endtab %}
{% endtabs %}

## 接続されたソースの使用 {#using-the-connected-source}

ソースが作成された後、それを使って1つ以上のCDIセグメントエクステンションを作成できます。このソースを使用したSegmentの作成に関する詳細情報は、[CDIセグメントエクステンションのドキュメント]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments)を参照してください。

{% alert note %}
クエリが常にタイムアウトしており、最大実行時間を60分に設定している場合は、クエリの実行時間を最適化するか、より多くのコンピューティングリソース（より大きなウェアハウスなど）をBrazeユーザーに割り当てることを検討してください。
{% endalert %}