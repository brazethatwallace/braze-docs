---
nav_title: 識別子フィールドレベルの暗号化
article_title: 識別子フィールドレベル暗号化
page_order: 2
alias: "/field_level_encryption/"
description: "このリファレンス記事では、Brazeで共有される個人を特定できる情報（PII）を最小限に抑えるために、メールアドレスを暗号化する方法について説明します。"
page_type: reference
---

# 識別子フィールドレベルの暗号化 {#identifier-field-level-encryption}

> メールアドレスを暗号化して、Brazeで共有される個人を特定できる情報（PII）を最小限に抑えます。

{% multi_lang_include data_activation/field_level_encryption_pii_description.md %}

{% alert important %}
識別子フィールドレベルの暗号化は、アドオン機能として利用できます。識別子フィールドレベルの暗号化を始めるには、Brazeアカウントマネージャーにお問い合わせください。
{% endalert %}

## 仕組み {#how-it-works}

メールアドレスは、Brazeに追加される前にハッシュ化および暗号化される必要があります。メッセージが送信されると、復号化されたメールアドレスを取得するためにAWS KMSへの呼び出しが行われます。次に、ハッシュ化されたメールアドレスが配信およびエンゲージメントイベントのメタデータに挿入され、元のユーザーにリンクされます。これがBrazeがメール分析を追跡する仕組みです。Brazeは含まれているプレーンテキストのメールアドレスを墨消しし、ユーザーのプレーンテキストのメールアドレスを保存しません。

## 前提条件 {#prerequisites}

識別子フィールドレベルの暗号化を使用するには、メールアドレスをBrazeに送信する**前に**、AWS KMSへアクセスしてメールアドレスを[暗号化](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html)および[ハッシュ化](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html)する必要があります。

次の手順に従って、AWSシークレットキー認証方法を設定します。

1. アクセスキーIDとシークレットアクセスキーを取得するには、AWS Key Management Serviceの権限ポリシーを使用してAWSで[IAMユーザーと管理者グループを作成します](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html#create-an-admin)。IAMユーザーは[kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html)および[kms:GenerateMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html)の権限を持っている必要があります。詳細については、[AWS KMSの権限](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html)を参照してください。
2. **Show User Security Credentials**を選択して、アクセスキーIDとシークレットアクセスキーを表示します。これらの認証情報をどこかにメモするか、**Download Credentials**ボタンを選択してください。AWS KMSキーに接続する際にこれらを入力する必要があります。
3. 次のAWSリージョンでKMSを設定する必要があります:
    - **Braze USクラスター:** `us-east-1`
    - **Braze EUクラスター:** `eu-central-1`
    - **Braze AUクラスター:** `ap-southeast-2`
    - **Braze IDクラスター:** `ap-southeast-3`
    - **Braze JPクラスター:** `ap-northeast-1`
4. AWS Key Management Serviceで2つのキーを作成し、IAMユーザーがキー使用権限に追加されていることを確認します:
    - **[暗号化/復号化](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk):** **Symmetric**キータイプと**Encrypt and Decrypt**キー使用法を選択します。
    - **[ハッシュ](https://docs.aws.amazon.com/kms/latest/developerguide/hmac-create-key.html):** **Symmetric**キータイプと**Generate and Verify MAC**キー使用法を選択します。キーの仕様は**HMAC_256**にする必要があります。キーを作成した後、HMACキーIDをどこかにメモしておいてください。Brazeで入力する必要があります。

![Symmetric、Generate and Verify MAC、HMAC_256が選択されたキー設定の構成画面。]({% image_buster /assets/img/field_level_encryption_aws_prereq.png %})

## ステップ 1: AWS KMSキーを接続する {#step-1-connect-your-aws-kms-keys}

Brazeダッシュボードで、**データ設定** > **フィールドレベルの暗号化**に移動します。AWS KMS設定には、次の内容を入力してください:

- アクセスキーID
- シークレットアクセスキー
- HMACキーID（保存後に更新することはできません）

## ステップ 2: 暗号化フィールドを選択する {#step-2-select-your-encrypted-fields}

次に、**Email address**を選択してフィールドを暗号化します。

フィールドの暗号化がオンになっている場合、復号化されたフィールドに戻すことはできません。これは暗号化が永続的な設定であることを意味します。メールアドレスの暗号化を設定する際、ワークスペースにメールアドレスを持つユーザーがいないことを確認してください。これにより、ワークスペースの機能を有効にするときに、プレーンテキストのメールアドレスがBrazeに保存されないようになります。

![フィールドレベルの暗号化設定。]({% image_buster /assets/img/field_level_encryption.png %})

## ステップ 3: ユーザーをインポートして更新する {#step-3-import-and-update-users}

識別子フィールドレベルの暗号化がオンになっている場合、Brazeに追加する前にメールアドレスをハッシュ化して暗号化する必要があります。ハッシュ化する前にメールアドレスを小文字にしてください。詳細については、[ユーザー属性オブジェクト](#user-attributes-object)を参照してください。

Brazeでメールアドレスを更新する際は、`email`が含まれるすべての場所でハッシュ化されたメールの値を使用する必要があります。これには以下が含まれます:

- RESTエンドポイント:
    - `/users/track`
    - `/campaigns/trigger/send`
    - `/canvas/trigger/send`
    - `/transactional/v1/campaigns/{campaign_id}/send`
- CSVを介してユーザーを追加または更新する

{% alert note %}
メールアドレスで新しいユーザーを作成する際には、ユーザーの暗号化されたメールの値を`email_encrypted`に追加する必要があります。追加しない場合、ユーザーは作成されません。同様に、メールアドレスを持っていない既存のユーザーにメールアドレスを追加する場合は、`email_encrypted`を追加する必要があります。追加しない場合、ユーザーは更新されません。
{% endalert %}

## 考慮事項 {#considerations}

識別子フィールドレベルの暗号化では、以下の機能はサポートされていません:

- SDKを介してメールアドレスを識別およびキャプチャする
- アプリ内メッセージのメールキャプチャフォーム
- Email Insightsのメールボックスプロバイダーチャートを含む、受信者ドメインに関するレポート
- 正規表現によるメールアドレスフィルター
- オーディエンス同期
- Shopify統合

### ユーザー属性オブジェクト {#user-attributes-object}

`/users/track`エンドポイントで識別子フィールドレベルの暗号化を使用する場合、[ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens)のフィールドの詳細に注意してください:

- `email`フィールドはメールのハッシュ値でなければなりません。
- `email_encrypted`フィールドはメールの暗号化された値でなければなりません。

## よくある質問 {#frequently-asked-questions}

### 暗号化とハッシュ化の違いは何ですか？ {#what-is-the-difference-between-encrypting-and-hashing}

暗号化は、データを暗号化および復号化することが可能な双方向機能です。同じプレーンテキストの値が複数回暗号化された場合、AWSの暗号化アルゴリズム（AES-256-GCM）は異なる暗号化値を生成します。ハッシュ化は、プレーンテキストが復号できない方法でスクランブルされる一方向関数です。ハッシュ化は毎回同じ値を生成します。これにより、同じメールアドレスを共有する複数のユーザー間でサブスクリプション状態を維持することができます。

### テスト送信にどのメールアドレスを使用すればよいですか？ {#what-email-address-should-i-use-in-my-test-send}

プレーンテキストのメールアドレスはテスト送信でサポートされています。特定のユーザーに対してメールがどのように表示されるかを確認するには、次の操作を行います:

1. **Preview message as a user**を選択します。
2. **Test Send**で、**Override recipients attributes with current preview user's attributes**を選択します。

{%raw%}
### このメールアドレスLiquid `{{${email_address}}}` をBrazeに追加するとどうなりますか？ {#what-happens-if-i-add-this-email-address-liquid-email_address-in-braze}

Brazeはメールを送信する際にプレーンテキストのメールアドレスをレンダリングします。プレビューでは、メールの暗号化されたバージョンが表示されます。カスタムワンクリックURLでユーザーを参照する場合は、ユーザーのexternal IDを使用することをお勧めします。

`{{${email_address}}}`は現在、ユーザー設定センターおよび配信停止ページではサポートされていません。
{%endraw%}

### Currentsではどのメールアドレスが表示されますか？ {#what-email-address-should-i-expect-to-see-in-currents}

ハッシュ化されたメールアドレスが、メール配信およびエンゲージメントイベントに含まれています。

### メッセージのアーカイブではどのメールアドレスが表示されますか？ {#what-email-address-should-i-expect-to-see-in-message-archiving}

プレーンテキストのメールアドレスがメッセージのアーカイブに含まれています。これらは顧客のクラウドストレージプロバイダーに直接送信され、メール本文に他の個人データが含まれている場合があります。

### 識別子フィールドレベルの暗号化を使用したサブスクリプション管理にmail-to list-unsubscribeを使用できますか？ {#can-i-use-mail-to-list-unsubscribe-for-subscription-management-with-identifier-field-level-encryption}

いいえ。mail-to list-unsubscribeを使用すると、プレーンテキストの復号化されたメールアドレスがBrazeに送信されます。識別子フィールドレベルの暗号化がオンの場合、ワンクリックを含むURLベースのHTTPメソッドをサポートしています。また、メール本文にワンクリックで配信停止できるリンクを含めることをお勧めします。

### 識別子フィールドレベルの暗号化は、電話番号などの他の識別子をサポートしていますか？ {#does-identifier-field-level-encryption-support-other-identifiers-like-phone}

いいえ。現時点では、識別子フィールドレベルの暗号化はメールアドレスでのみサポートされています。