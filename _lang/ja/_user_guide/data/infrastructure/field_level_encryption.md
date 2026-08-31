---
nav_title: 識別子フィールドレベルの暗号化
article_title: 識別子フィールドレベルの暗号化
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

メールアドレスは、Brazeに追加される前にハッシュ化および暗号化される必要があります。メッセージが送信されると、復号化されたメールアドレスを取得するためにAWS KMSへの呼び出しが行われます。次に、ハッシュ化されたメールアドレスが配信およびエンゲージメントイベントのメタデータに挿入され、元のユーザーに紐付けられます。これにより、Brazeはメール分析を追跡できます。Brazeは、含まれているプレーンテキストのメールアドレスを除去し、ユーザーのプレーンテキストのメールアドレスを保存しません。

## 前提条件 {#prerequisites}

識別子フィールドレベル暗号化を使用するには、AWS KMSにアクセスして、Brazeに送信する**前に**メールアドレスを[暗号化](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html)および[ハッシュ化](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html)する必要があります。

以下の手順に従って、AWSシークレットキー認証方法を設定してください。

1. アクセスキーIDとシークレットアクセスキーを取得するには、AWS Key Management Serviceの権限ポリシーを持つ[IAMユーザーと管理者グループを作成](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html#create-an-admin)します。IAMユーザーには、[kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html)と[kms:GenerateMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html)の権限が必要です。詳細については、[AWS KMS権限](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html)を参照してください。
2. **Show User Security Credentials**を選択して、アクセスキーIDとシークレットアクセスキーを表示します。AWS KMSキーを接続する際にこれらを入力する必要があるため、認証情報をメモするか、**Download Credentials**ボタンを選択してください。
3. 以下のAWSリージョンでKMSを設定する必要があります：
    - **Braze USクラスター：** `us-east-1`
    - **Braze EUクラスター：** `eu-central-1`
    - **Braze AUクラスター：** `ap-southeast-2`
    - **Braze IDクラスター：** `ap-southeast-3`
    - **Braze JPクラスター：** `ap-northeast-1`
4. AWS Key Management Serviceで2つのキーを作成し、IAMユーザーがキー使用権限に追加されていることを確認してください：
    - **[暗号化/復号](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk)：** **Symmetric**キータイプと**Encrypt and Decrypt**キー用途を選択します。
    - **[ハッシュ](https://docs.aws.amazon.com/kms/latest/developerguide/hmac-create-key.html)：** **Symmetric**キータイプと**Generate and Verify MAC**キー用途を選択します。キースペックは**HMAC_256**にする必要があります。キーを作成した後、Brazeで入力する必要があるため、HMACキーIDをメモしておいてください。

![Symmetric、Generate and Verify MAC、HMAC_256のオプションが選択されたキー設定の構成画面。]({% image_buster /assets/img/field_level_encryption_aws_prereq.png %})

## ステップ1：AWS KMSキーを接続する {#step-1-connect-your-aws-kms-keys}

Brazeダッシュボードで、**データ設定** > **フィールドレベル暗号化**に移動します。AWS KMS設定に、以下を入力します。

- アクセスキーID
- シークレットアクセスキー
- HMACキー識別子（キーIDまたはキーARN。保存後は更新できません）

## ステップ2: 暗号化するフィールドを選択する {#step-2-select-your-encrypted-fields}

次に、**メールアドレス**を選択してフィールドを暗号化します。

フィールドの暗号化をオンにすると、復号化されたフィールドに戻すことはできません。つまり、暗号化は永続的な設定です。メールアドレスの暗号化を設定する際は、ワークスペースにメールアドレスを持つユーザーがいないことを確認してください。これにより、ワークスペースでこの機能をオンにしたときに、プレーンテキストのメールアドレスがBrazeに保存されないようになります。

![フィールドレベル暗号化の設定。]({% image_buster /assets/img/field_level_encryption.png %})

## ステップ3：ユーザーのインポートと更新 {#step-3-import-and-update-users}

識別子フィールドレベルの暗号化が有効になっている場合、Brazeに追加する前にメールアドレスをハッシュ化および暗号化する必要があります。ハッシュ化する前に、メールアドレスを小文字に変換してください。詳細については、[ユーザー属性オブジェクト](#user-attributes-object)を参照してください。

Brazeでメールアドレスを更新する場合、`email`が含まれるすべての箇所でハッシュ化されたメール値を使用する必要があります。これには以下が含まれます：

- RESTエンドポイント：
    - `/users/track`
    - `/campaigns/trigger/send`
    - `/canvas/trigger/send`
    - `/transactional/v1/campaigns/{campaign_id}/send`
- CSVによるユーザーの追加または更新

{% alert note %}
メールアドレスを使用して新しいユーザーを作成する場合、ユーザーの暗号化されたメール値を含む`email_encrypted`を追加する必要があります。これを行わないと、ユーザーは作成されません。同様に、メールアドレスを持たない既存のユーザーにメールアドレスを追加する場合、`email_encrypted`を追加する必要があります。これを行わないと、ユーザーは更新されません。
{% endalert %}

## 考慮事項 {#considerations}

識別子フィールドレベル暗号化では、以下の機能はサポートされていません。

- SDKによるメールアドレスの識別とキャプチャ
- アプリ内メッセージのメールキャプチャフォーム
- メールインサイトのメールボックスプロバイダーチャートを含む、受信者ドメインに関するレポート
- 正規表現によるメールアドレスフィルター
- オーディエンス同期
- Shopify連携

### ユーザー属性オブジェクト {#user-attributes-object}

`/users/track` エンドポイントで識別子フィールドレベル暗号化を使用する場合、[ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object)の以下のフィールドの詳細に注意してください。

- `email` フィールドには、メールのハッシュ化された値を指定する必要があります。
- `email_encrypted` フィールドには、メールの暗号化された値を指定する必要があります。

## よくある質問 {#frequently-asked-questions}

### 暗号化とハッシュ化の違いは何ですか？ {#what-is-the-difference-between-encrypting-and-hashing}

暗号化はデータの暗号化と復号が可能な双方向の機能です。同じ平文の値を複数回暗号化した場合、AWSの暗号化アルゴリズム（AES-256-GCM）は異なる暗号化値を生成します。ハッシュ化は平文を復号できない形に変換する一方向の機能です。ハッシュ化では毎回同じ値が生成されます。これにより、同じメールアドレスを共有する複数のユーザー間で購読状態を維持できます。

### テスト送信ではどのメールアドレスを使用すればよいですか？ {#what-email-address-should-i-use-in-my-test-send}

テスト送信では平文のメールアドレスがサポートされています。特定のユーザーに対してメールがどのように表示されるかを確認するには、以下を行います。

1. **ユーザーとしてメッセージをプレビュー**を選択します。
2. **テスト送信**で、**受信者の属性を現在のプレビューユーザーの属性でオーバーライドする**を選択します。

### HMACキーにARNを使用できますか？ {#can-i-use-an-arn-for-the-hmac-key}

はい。**データ設定** > **フィールドレベル暗号化**で、HMACキー識別子はキーIDまたはキーARNのいずれかを受け付けます。

### HMACキーを削除またはリセットするにはどうすればよいですか？ {#how-do-i-remove-or-reset-an-hmac-key}

ダッシュボードでHMACキーを保存した後に削除またはリセットすることはできません。HMACキーのリセットまたは識別子フィールドレベル暗号化設定の削除をリクエストするには、Brazeアカウントマネージャーに連絡するか、[サポートチケット]({{site.baseurl}}/braze_support)を作成してください。

{%raw%}
### Brazeでこのメールアドレス Liquid `{{${email_address}}}` を追加するとどうなりますか？ {#what-happens-if-i-add-this-email-address-liquid-email_address-in-braze}

Brazeはメール送信時に平文のメールアドレスをレンダリングします。プレビューでは、メールアドレスの暗号化されたバージョンが表示されます。カスタムワンクリックURLでユーザーを参照する場合は、ユーザーのexternal IDを使用することをお勧めします。

`{{${email_address}}}` は現在、ユーザー設定センターおよび購読解除ページではサポートされていません。
{%endraw%}

### Currentsではどのメールアドレスが表示されますか？ {#what-email-address-should-i-expect-to-see-in-currents}

メール配信およびエンゲージメントイベントには、ハッシュ化されたメールアドレスが含まれます。

### メッセージアーカイブではどのメールアドレスが表示されますか？ {#what-email-address-should-i-expect-to-see-in-message-archiving}

メッセージアーカイブには平文のメールアドレスが含まれます。これらは顧客のクラウドストレージプロバイダーに直接送信され、メール本文にはその他の個人データが含まれる場合があります。

### 識別子フィールドレベル暗号化で購読管理にmail-to list-unsubscribeを使用できますか？ {#can-i-use-mail-to-list-unsubscribe-for-subscription-management-with-identifier-field-level-encryption}

いいえ。mail-to list-unsubscribeを使用すると、復号された平文のメールアドレスがBrazeに送信されます。識別子フィールドレベル暗号化を有効にしている場合は、ワンクリックを含むURLベースのHTTPメソッドをサポートしています。また、メール本文にワンクリック購読解除リンクを含めることをお勧めします。

### 識別子フィールドレベル暗号化は電話番号など他の識別子をサポートしていますか？ {#does-identifier-field-level-encryption-support-other-identifiers-like-phone}

いいえ。現在、識別子フィールドレベル暗号化はメールアドレスのみでサポートされています。