---
nav_title: Microsoft Azure Blob Storage
article_title: Microsoft Azure Blob Storage
alias: /partners/microsoft_azure_blob_storage_for_currents/
description: "このリファレンス記事では、Braze CurrentsとMicrosoft Azure Blob Storageのパートナーシップについて説明します。Microsoft Azure Blob Storageは、非構造化データのための大規模拡張可能オブジェクトストレージです。"
page_type: partner
tool: Currents
search_tag: Partner

---

# Microsoft Azure Blob Storage

> [Microsoft Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/) は、MicrosoftがAzure製品群の一部として提供する、非構造化データのための大規模拡張可能オブジェクトストレージです。

{% alert important %}
クラウドストレージプロバイダーを切り替える場合は、Brazeカスタマーサクセスマネージャーに連絡し、新しい統合の設定と検証についてサポートを受けてください。
{% endalert %}

BrazeとMicrosoft Azure Blob Storageの統合により、データをAzureにエクスポートし、Currentsデータをストリーミングできます。その後、ETLプロセス（抽出、変換、読み込み）を使用してデータを他の場所に転送できます。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| ----------- | ----------- |
| Microsoft AzureおよびAzureストレージアカウント | このパートナーシップを利用するには、Microsoft AzureおよびAzureストレージアカウントが必要です。 |
| Currents | Currentsにデータをエクスポートするには、アカウントに[Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents)が設定されている必要があります。メッセージアーカイブのみを設定する場合、Currentsは必要ありません。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携 {#integration}

Microsoft Azure Blob Storageと連携するには、Brazeがデータをエクスポートしたり、Currentsデータをストリーミングしたりできるようにするためのストレージアカウントとコンテナが必要です。Brazeは2つの認証方法をサポートしています。

- [接続文字列方式](#connection-string-auth-method)
- [証明書サービスプリンシパル方式](#certificate-service-principal-auth-method)（Currentsのみ）

## 接続文字列認証方式 {#connection-string-auth-method}

### ステップ1:ストレージアカウントを作成する {#step-1-create-a-storage-account}

Microsoft Azureで、サイドバーの**Storage Accounts**に移動し、**+ Add**をクリックして新しいストレージアカウントを作成します。次に、ストレージアカウント名を入力します。その他のデフォルト設定は更新する必要はありません。最後に、**Review + create**を選択します。

すでにストレージアカウントをお持ちの場合でも、Brazeデータ専用に新しいストレージアカウントを作成することをお勧めします。

![Microsoft Azureのストレージアカウント作成ページの「Basics」タブ。ストレージアカウント名フィールドがハイライトされています。]({% image_buster /assets/img/azure-currents-step-1.png %})

### ステップ2:接続文字列を取得する {#step-2-get-the-connection-string}

ストレージアカウントがデプロイされたら、ストレージアカウントから**Access Keys**メニューに移動し、接続文字列をメモします。

Microsoftは、一方のキーを再生成している間にもう一方のキーで接続を維持できるよう、2つのアクセスキーを提供しています。どちらか一方の接続文字列のみが必要です。

{% alert note %}
Brazeはこのメニューのキーではなく、接続文字列を使用します。
{% endalert %}

![Azureストレージアカウントのアクセスキーページ。key1の下にある接続文字列フィールドがハイライトされています。]({% image_buster /assets/img/azure-currents-step-2.png %})

### ステップ3:Blobサービスコンテナを作成する {#step-3-create-a-blob-service-container}

ストレージアカウントの**Blob Service**セクションにある**Blobs**メニューに移動します。先ほど作成したストレージアカウント内にBlobサービスコンテナを作成します。

Blobサービスコンテナの名前を入力します。その他のデフォルト設定は更新する必要はありません。

![Azureストレージアカウントの「Blob Service」配下のBlobsページ。コンテナを追加するオプションが表示されています。]({% image_buster /assets/img/azure-currents-step-3.png %})

### ステップ4:Currentsを設定する {#step-4-set-up-currents}

Brazeで、**Currents > + Create Current > Azure Blob Data Export**に移動し、連携名と連絡先メールアドレスを入力します。

{% multi_lang_include currents/contact_email_notifications.md %}

次に、接続文字列、コンテナ名、BlobStorageプレフィックス（任意）を入力します。

![BrazeのMicrosoft Azure Blob Storage Currentsページ。このページには、連携名、連絡先メール、接続文字列、コンテナ名、プレフィックスのフィールドがあります。]({% image_buster /assets/img/maz.png %})

最後に、ページの下部までスクロールし、エクスポートしたいメッセージエンゲージメントイベントまたは顧客行動イベントを選択します。完了したら、Currentを起動します。

### ステップ5:Azureデータエクスポートを設定する {#step-5-set-up-azure-data-export}

以下は、次の用途で使用される認証情報を設定します。
1. APIを通じたセグメントエクスポート
2. CSVエクスポート（キャンペーン、セグメント、キャンバスのユーザーデータをダッシュボードからエクスポート）
3. エンゲージメントレポート

Brazeで、**パートナー連携** > **テクノロジーパートナー** > **Microsoft Azure**に移動し、接続文字列、Azureストレージコンテナ名、Azureストレージプレフィックスを入力します。

次に、**Make this the default data export destination**チェックボックスがオンになっていることを確認します。これにより、エクスポートされたデータがAzureに送信されます。完了したら、連携を保存します。

![BrazeのMicrosoft Azureデータエクスポートページ。このページには、接続文字列、コンテナ名、プレフィックスのフィールドがあります。]({% image_buster /assets/img/azure_data_export.png %})

{% alert important %}
接続文字列を常に最新の状態に保つことが重要です。コネクタの認証情報が期限切れになると、コネクタはイベントの送信を停止します。この状態が48時間以上続くと、コネクタのイベントは破棄され、データは永久に失われます。
{% endalert %}

## 証明書サービスプリンシパル認証方式 {#certificate-service-principal-auth-method}

この方式は、証明書を使用して Microsoft Entra ID に認証し、共有アカウントキーを使用せずに Azure ロールベースアクセス制御 (RBAC) を通じてコンテナーに書き込みます。この方式は Braze Currents でのみ利用できます。

{% alert note %}
Microsoft Entra ID にアップロードするのは公開証明書のみです。秘密キーが Azure に送信されることはありません。Braze は証明書と秘密キーを保存時に暗号化し、割り当てた [Storage Blob Data Contributor](#cert-sp-4) ロールを通じてのみアクセスを許可します。Azure のアプリ登録から証明書を削除することで、いつでもアクセスを取り消すことができます。
{% endalert %}

開始する前に、[接続文字列方式](#connection-string-auth-method)の説明に従って、[ストレージアカウントを作成](#step-1-create-a-storage-account)し、[Blob サービスコンテナーを作成](#step-3-create-a-blob-service-container)してください。

### ステップ1: アプリケーションを登録する {#cert-sp-1}

Microsoft Azure で、**Microsoft Entra ID** > **App registrations** > **+ New registration** に移動します。名前を入力し（例: `braze-currents`）、**Register** を選択します。詳細な手順については、Microsoft の [Register an application with the Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app) を参照してください。

新しいアプリ登録の **Overview** ページで、以下の値をメモしてください。[ステップ6](#cert-sp-6)で両方を Braze に入力します。

- **Application (client) ID**
- **Directory (tenant) ID**

### ステップ2: 証明書を作成する {#cert-sp-2}

Braze は証明書を使用して認証します。**公開証明書**を Azure にアップロードし、**証明書と秘密キー**を Braze に提供します。

自己署名証明書と暗号化されていない 2048 ビット RSA 秘密キーを生成するには、以下を実行します。

```bash
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem \
  -days 730 -nodes -subj "/CN=braze-currents"
```

これにより、2つのファイルが作成されます。

| ファイル | 用途 |
| ---- | ------- |
| `cert.pem` | 公開証明書。次のステップで Azure にアップロードします。 |
| `key.pem` | 秘密キー。Azure にはアップロードしないでください。[ステップ6](#cert-sp-6)で Braze に提供します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="証明書ファイル" }

{% alert important %}
秘密キーは暗号化されていない状態である必要があります。パスフレーズで保護することはできません。Azure にアップロードするのは公開証明書のみです。秘密キーは絶対にアップロードしないでください。
{% endalert %}

**既に証明書をお持ちですか？** 既存の証明書が `.pfx` ファイルとしてある場合（例: Azure Key Vault、認証局、または [Microsoft の PowerShell 方式](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-self-signed-certificate)から取得したもの）、新しい証明書を生成する代わりに、Braze が必要とする形式に変換してください。

```bash
# The public certificate to upload to Azure (Step 3)
openssl pkcs12 -in your-cert.pfx -nokeys -out cert.pem

# The certificate and its unencrypted private key to give to Braze (Step 6)
openssl pkcs12 -in your-cert.pfx -nodes -out braze-currents.pem
```

プロンプトが表示されたら `.pfx` パスワードを入力してください。`-nodes` フラグは、Braze が必要とする暗号化されていない状態で秘密キーをエクスポートします。

### ステップ3: 証明書をアップロードする {#cert-sp-3}

アプリ登録で、**Certificates & secrets** > **Certificates** > **Upload certificate** に移動し、前のステップで作成した `cert.pem` ファイルをアップロードします。説明を追加して **Add** を選択します。詳細な手順については、Microsoft の [Add and manage app credentials in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-credentials) を参照してください。

証明書の有効期限をメモしてください。[Currents の Azure 認証情報の更新](#updating-currents-credentials)を参照してください。

### ステップ4: ストレージアカウントへのアクセスを許可する {#cert-sp-4}

次に、アプリ登録にコンテナーへの書き込み権限を付与します。

ストレージアカウントに移動し、**Access Control (IAM)** > **+ Add** > **Add role assignment** を選択します。次に以下を行います。

1. **Role** タブで、**[Storage Blob Data Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/storage#storage-blob-data-contributor)** を選択します。
2. **Members** タブで、**User, group, or service principal** を選択し、**+ Select members** を選択して、[ステップ1](#cert-sp-1)で作成したアプリ登録名を検索します。
3. **Review + assign** を選択します。

詳細な手順については、Microsoft の [Assign an Azure role for access to blob data](https://learn.microsoft.com/en-us/azure/storage/blobs/assign-azure-role-data-access) を参照してください。

![ストレージアカウントの Access Control (IAM) ロール割り当てタブ。サービスプリンシパルとグループに Storage Blob Data Contributor ロールが割り当てられています。]({% image_buster /assets/img/azure-currents-cert-sp-1.png %})

{% alert note %}
ロールは個々のコンテナーではなく、**ストレージアカウント**レベルで割り当ててください。
{% endalert %}

{% alert important %}
このロール割り当てがないと、Braze は Microsoft Entra ID に認証できますが、コンテナーに書き込むことはできません。
{% endalert %}

### ステップ5: アカウントエンドポイントを取得する {#cert-sp-5}

ストレージアカウントから、**Settings** > **Endpoints** に移動し、**Blob service** エンドポイントをメモします。`https://<your-storage-account>.blob.core.windows.net` のような形式です。

![ストレージアカウントのエンドポイントページ。Blob service エンドポイントがハイライトされています。]({% image_buster /assets/img/azure-currents-cert-sp-2.png %})

{% alert note %}
証明書サービスプリンシパル認証は、パブリック Azure クラウドのみをサポートしています。Blob エンドポイントは `.blob.core.windows.net` で終わる必要があります。
{% endalert %}

### ステップ6: Currents を設定する {#cert-sp-6}

Braze には、証明書と暗号化されていない秘密キーを含む単一の PEM ファイルが必要です。[ステップ2](#cert-sp-2)で新しい証明書を生成した場合は、2つのファイルを1つに結合します。

```bash
cat cert.pem key.pem > braze-currents.pem
```

[ステップ2](#cert-sp-2)で既存の `.pfx` を変換した場合は、この `braze-currents.pem` ファイルが既にあります。

Braze で、**Currents** > **+ Create Current** > **Azure Blob Data Export** に移動し、連携名と連絡先メールアドレスを入力します。

{% multi_lang_include currents/contact_email_notifications.md %}

**Credentials** で、**Certificate Service Principal** を選択し、以下を入力します。

| フィールド | 値 |
| ----- | ----- |
| Tenant ID | [ステップ1](#cert-sp-1)の **Directory (tenant) ID**。 |
| Client ID | [ステップ1](#cert-sp-1)の **Application (client) ID**。 |
| Account Endpoint | [ステップ5](#cert-sp-5)の **Blob service** エンドポイント。 |
| Certificate | 証明書と暗号化されていない秘密キーを含む `braze-currents.pem` ファイル。 |
| Container Name | Blob コンテナーの名前。 |
| Prefix | オプション。コンテナー内のエクスポートデータのパスプレフィックス。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="証明書サービスプリンシパルのフィールド" }

![Braze の Azure Blob Data Export ページ。Certificate Service Principal が選択され、Tenant ID、Client ID、Account Endpoint、Certificate、Container Name、Prefix のフィールドが表示されています。]({% image_buster /assets/img/azure-currents-cert-sp-3.png %})

保存すると、Braze は入力された認証情報を検証します。

最後に、ページの下部までスクロールし、エクスポートするメッセージエンゲージメントイベントまたは顧客行動イベントを選択します。完了したら、Current を起動します。

## Currentsの Azure 認証情報の更新 {#updating-currents-credentials}

既存のBraze Currentsコネクターの Azure 認証情報を、連携を停止したり、コンテナにすでにエクスポートされたデータを失ったりすることなく更新できます。

認証情報を更新する場合、または**接続文字列**と**証明書サービスプリンシパル**の方法を切り替える場合は、この記事の前半で説明した、選択した方法の Azure 側のステップを完了してください。次に、Brazeで**Currents**に移動し、リストから Azure Blob コネクターを見つけて**Edit Current**を選択し、**Credentials**を更新してから**Update Current**を選択します。Brazeは入力された認証情報を検証します。コネクターは引き続き動作し、コンテナ内のデータはそのまま利用可能です。詳細については、[Currentsの設定でのCurrentsの更新]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents#updating-currents)を参照してください。

{% alert important %}
証明書を最新の状態に保つことが重要です。証明書の有効期限が切れると、有効な証明書を提供するまでコネクターはイベントの送信を停止します。長期間の中断はデータ損失につながる可能性があります。
{% endalert %}

## エクスポートの動作 {#export-behavior}

クラウドデータストレージソリューションを統合しており、APIエクスポート、ダッシュボードレポート、またはCSVレポートをエクスポートしようとしているユーザーは、以下の動作を経験します。

- すべてのAPIエクスポートは、レスポンスボディにダウンロードURLを返さず、データストレージから取得する必要があります。
- すべてのダッシュボードレポートとCSVレポートは、ダウンロード用にユーザーのメールに送信され（ストレージ権限は不要）、データストレージにバックアップされます。

{% alert important %}
**JSON形式の要件**: JSONエクスポートの場合、Brazeは[JSONL](https://jsonlines.org/)（改行区切りJSON）形式を使用します。各行には個別のJSONオブジェクトが含まれます。この形式は、単一のJSON配列またはオブジェクトである標準JSONとは異なります。エクスポートされたファイルの各行は有効なJSONオブジェクトですが、ファイル全体は単一の有効なJSONドキュメントではありません。これらのファイルを処理する際は、ファイル全体を単一のJSONドキュメントとして解析しようとするのではなく、各行を個別のJSONオブジェクトとして解析してください。<br><br> Currentsエクスポートは[Apache Avro](https://avro.apache.org/)形式（`.avro`ファイル）を使用し、JSONは使用しません。このJSON形式の要件は、ダッシュボードデータエクスポートおよびJSON形式を使用するAPIエクスポートに適用されます。
{% endalert %}

## FAQ

### BrazeはAzure Blob Storageの許可リストに追加するIPアドレスを提供できますか？ {#can-braze-provide-ip-addresses-to-allowlist-for-azure-blob-storage}

Brazeは、Azure Blob StorageへのCurrentsまたはダッシュボードエクスポート用の固定IP許可リストを公開していません。Brazeは、お客様が提供する認証情報とコンテナー名を使用してコンテナーに書き込みを行い、Azureはストレージアカウントの設定（ストレージアカウントのファイアウォールルールやプライベートエンドポイントなど）を通じてネットワークアクセスを制御します。

セキュリティチームがIPベースの制限を必要とする場合は、BrazeからのIPリストではなく、ストレージアカウントのAzureネットワーキング機能を使用してください。設定手順については、[Azure Storageのセキュリティに関するMicrosoftのドキュメント](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)を参照してください。