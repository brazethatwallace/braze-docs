---
nav_title: セキュリティ設定
article_title: セキュリティ設定
page_order: 2
toc_headers: h2
page_type: reference
description: "このリファレンス記事では、認証ルール、IPの許可リスト、PII、2 要素認証（2FA）など、一般的な企業横断的セキュリティ設定について説明します。"

---

# セキュリティ設定 {#security-settings}

> 管理者にとって、セキュリティは最も優先度の高い懸念事項の1つです。**セキュリティ設定**ページでは、認証ルール、IPの許可リスト、2 要素認証など、一般的な企業横断的セキュリティ設定を管理できます。

このページにアクセスするには、**設定** > **会社設定** > **管理者設定** > **セキュリティ設定**に移動します。

## 認証ルール {#authentication-rules}

### パスワードの長さ {#password-length}

このフィールドを使用して、必要なパスワードの最小文字数を変更します。デフォルトの最小値は8文字です。

### パスワードの複雑さ {#password-complexity}

**複雑なパスワードを強制する**を選択すると、パスワードに以下のそれぞれを少なくとも1つ含めることが要求されます。
- 大文字
- 小文字
- 数字
- 特殊文字（文字や数字以外の文字。`!`、`@`、`#`、`(` など）

### パスワードの再利用 {#password-re-usability}

ユーザーがパスワードを再利用できるようになるまでに設定する必要がある新しいパスワードの最小数を決定します。デフォルトは3です。

### パスワードの有効期限ルール {#password-expiration-rules}

このフィールドを使用して、Brazeアカウントのユーザーにパスワードのリセットを求めるタイミングを設定します。

### セッション期間のルール {#session-duration-rules}

このフィールドを使用して、Brazeがセッションをアクティブに維持する期間を定義します。Brazeがセッションを非アクティブと判断した場合（定義された分数の間アクティビティがない場合）、Brazeはユーザーをログアウトします。入力できる最大分数は、2要素認証が会社に対して適用されている場合は10,080分（1週間に相当）です。それ以外の場合、最大セッション期間は1,440分（24時間に相当）です。

### シングルサインオン（SSO）認証 {#single-sign-on-sso-authentication}

パスワードまたはSSOを使用したユーザーのログインを制限できます。

[SAML SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on)の場合、適用する前にSAML設定をセットアップする必要があります。Google SSOを使用する場合は、追加の作業なしにセキュリティ設定ページを適用するだけで済みます。

## ダッシュボードIPアローリスト {#dashboard-ip-allowlisting}

表示されたフィールドを使用して、ユーザーがアカウントにログインできる特定のIPアドレスとサブネットをアローリストに登録します（例：社内ネットワークやVPNから）。IPアドレスとサブネットは、CIDR範囲としてカンマ区切りのリストで指定します。指定しない場合、ユーザーは任意のIPアドレスからログインできます。

## 2要素認証（2FA） {#two-factor-authentication-2fa}

2要素認証は、すべての会社ユーザーに必要です。アカウントログインに2番目の本人確認レベルを追加し、ユーザー名とパスワードだけの場合よりも安全にします。ダッシュボードが2要素認証をサポートできない場合は、カスタマーサクセスマネージャーにお問い合わせください。

2要素認証がオンになると：

- パスワードの入力に加えて、ユーザーはBrazeアカウントにログインする際に確認コードを入力する必要があります。コードは認証アプリ、メール、またはSMSを通じて送信できます。
- **このアカウントを30日間記憶する**チェックボックスがユーザーに表示されるようになります。

Brazeは、2要素認証を設定しないユーザーをBrazeアカウントからロックアウトします。Brazeアカウントユーザーは、管理者が要求していなくても、**アカウント設定**から自分で2要素認証を設定することもできます。

ページを離れる前に、必ず変更を保存してください！

### このアカウントを30日間記憶する {#remember-me}

この機能は、2要素認証がオンになっている場合に利用できます。

**このアカウントを30日間記憶する**を選択すると、デバイスにCookieが保存され、30日間で1回だけ2要素認証でのログインが必要になります。

![「このアカウントを30日間記憶する」チェックボックス]({% image_buster /assets/img/remember_me.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

ダッシュボード企業配下に複数のアカウントを持つ顧客は、Cookieが特定のデバイスに紐付けられているため、この機能の使用で問題が発生する場合があります。ユーザーが同じデバイスを使用して複数のアカウントにログインすると、そのデバイス上で以前に認証されたアカウントのCookieが置き換えられます。Brazeは、1つのデバイスが1つのアカウントに関連付けられることを想定しており、1つのデバイスで複数のアカウントを使用することは想定していません。

### ユーザー認証のリセット {#resetting-user-authentication}

2要素認証でのログインに問題がある場合は、会社の管理者に連絡して2要素認証をリセットしてもらってください。管理者は以下の手順を実行できます：

1. **設定** > **会社設定** > **ユーザー管理** > **会社ユーザー**に移動します。
2. 表示されたリストからユーザーを選択します。
3. **2要素認証**の下にある**リセット**を選択します。

リセットにより、認証アプリのトラブル、メール認証が送信されない問題、SMS障害やユーザーエラーによるログイン失敗など、一般的な認証の問題を解決できます。

### 会社レベルでの2FA要件 {#requirements-for-2fa-at-the-company-level}

まず、**設定** > **会社設定** > **管理者設定** > **セキュリティ設定** > **2要素認証**に移動して、ダッシュボードで2FAが有効になっているかどうかを確認してください。トグルがグレーの場合、会社で2FAが有効になっておらず、すべての会社ユーザーに必須ではありません。

#### 2FAが必須でない場合のユーザーオプション {#user-options-when-2fa-isnt-mandatory}

2FAが会社レベルで強制されていない場合、個々のユーザーはアカウント設定ページから自分で2FAを設定できます。この場合、設定しなくてもアカウントからロックアウトされることはありません。どのユーザーが2FAを有効にしたかは、**会社ユーザー**リストで確認できます。

#### 2FAが必須の場合の要件 {#requirements-when-2fa-is-mandatory}

2FAが会社レベルで強制されている場合、ログイン時に自分のアカウントで2FAを設定しないユーザーはダッシュボードからロックアウトされます。アクセスを維持するには、ユーザーは2FAの設定を完了する必要があります。

{% alert important %}
2FAは、シングルサインオン（SSO）が有効でない場合にのみ、すべての会社ユーザーに必要です。SSOが使用されている場合、会社レベルで2FAを強制する必要はありません。
{% endalert %}

## 2FAを手動で設定する {#manually-set-up-2fa}

Brazeアカウントで2要素認証（2FA）を手動で有効にするには、以下のステップに従ってください。

1. Brazeでグローバルヘッダーのプロファイルアイコンを選択し、**アカウントを管理**を選択します。**2要素認証**セクションまでスクロールし、**設定を開始**を選択します。
2. ログインモーダルにパスワードを入力し、**パスワードを確認**を選択します。
3. **2要素認証の設定**モーダルで電話番号を入力し、**有効にする**を選択します。
4. メールまたはSMSメッセージから生成された7桁のコードをコピーし、Brazeに戻って**2要素認証の設定**モーダルに貼り付けます。**確認**を選択します。
5. （オプション）今後30日間2FAの入力を省略するには、**このアカウントを30日間記憶する**オプションを有効にします。

## 権限の昇格 {#elevated-access}

権限の昇格は、Brazeダッシュボードでの機密性の高いアクションに対して、セキュリティの追加レイヤーを提供します。有効にすると、ユーザーはセグメントのエクスポートやAPIキーの表示を行う前に、アカウントを再確認する必要があります。権限の昇格を使用するには、**設定** > **会社設定** > **管理者設定** > **セキュリティ設定**に移動し、トグルをオンにします。

ユーザーが再確認できない場合、元の画面にリダイレクトされ、機密性の高いアクションを続行できません。再確認が正常に完了すると、次の1時間は再確認の必要はありません（ただし、先にログアウトした場合を除きます）。

## セキュリティイベントレポートのダウンロード {#security-event-report}

セキュリティイベントレポートは、アカウントの招待、アカウントの削除、ログインの失敗と成功、その他のアクティビティなどのセキュリティイベントのCSVレポートです。内部監査に使用できます。

このレポートをダウンロードするには、以下の手順に従ってください。

1. **設定** > **会社の設定** > **管理者設定** > **セキュリティ設定**に移動します。
2. **セキュリティイベントのダウンロード**セクションに移動します。
3. **レポートをダウンロード**を選択します。

この手動レポートダウンロードには、アカウントの最新10,000件のセキュリティイベントのみが含まれます。エクスポートしたCSVがちょうど10,001行（ヘッダー行を含む）の場合、10,000件のレポート上限に達しており、古いイベントが含まれていない可能性があります。

この行数制限なしでセキュリティイベントをAmazon S3にエクスポートするには、[Amazon S3でのセキュリティイベントのエクスポート]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/security_export_s3)を参照してください。

### CSV列の定義 {#csv-column-definitions}

セキュリティイベントレポートのCSVには以下の列が含まれます。

| 列 | 説明 |
|--------|-------------|
| CreatedAt | イベントが記録されたタイムスタンプ（UTC）。 |
| EmailAtTimeOfEvent | イベントをトリガーしたダッシュボードユーザーのメールアドレス（イベント発生時に記録されたもの）。 |
| CurrentEmail | イベントをトリガーしたダッシュボードユーザーの現在のメールアドレス。ユーザーが存在しなくなった場合は、開発者IDが代わりに使用されます。 |
| EventName | セキュリティイベントのタイプ。この表の後にある**レポートされるセキュリティイベント**ドロップダウンを参照してください。 |
| OtherAccount | イベントの影響を受けた別のダッシュボードユーザーのメールアドレス（該当する場合。例：アカウントの追加や削除時）。 |
| JsonProperties | JSON形式のイベント固有のプロパティ。含まれるフィールドはイベントタイプによって異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="CSV列の定義" }

[S3エクスポート]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/security_export_s3)には、これらの列に加えて`Version`（エクスポート形式のスキーマバージョン、現在は`1`）が含まれます。

{% details レポートされるセキュリティイベント %}
### ログインとアカウント {#login-and-account}
- Signed In
- Failed Login
- Two-Factor Auth Setup Completed
- Two-Factor Auth Reset Completed
- Cleared Developer 2FA
- Added Additional Developer
- Added Account
- Developer Suspended
- Developer Unsuspended
- Developer Updated
- Removed Developer
- Removed Account
- User Subscription Status Updated
- User Updated
- Developer Account Updated

### 昇格アクセス
- Started Elevated Access Flow
- Completed Elevated Access Flow
- Failed 2FA Verification For Elevated Access
- Enabled Elevated Access Enforcement
- Disabled Elevated Access Enforcement

キャンペーン
- Added キャンペーン
- Edited キャンペーン

キャンバス
- Added キャンバス
- Edited キャンバス

### セグメント {#segment}
- Added セグメント
- Edited セグメント
- Exported data to CSV
- Exported セグメント via API
- セグメント Users Deleted
- Cleared Cohort

### REST APIキー {#rest-api-key}
- Added REST API key
- Removed REST API key

### 基本認証の認証情報 {#basic-authentication-credential}
- Added Basic Auth credential
- Updated Basic Auth credential
- Removed Basic Auth credential

### 権限 {#permission}
- Cleared Developer 2FA
- Updated Account Permission
- Added Team
- Edited Team
- Archived Team
- Unarchived Team
- Created App Group Permission Set
- Edited App Group Permission Set
- Removed App Group Permission Set
- Created Custom Role
- Updated Custom Role
- Deleted Custom Role

### 会社の設定 {#company-settings}
- Added App Group
- Added App
- Company Settings Changed
- Updated Company Security Settings
- Updated Security Event Cloud Export
- Added Landing Pages Custom Domain
- Removed Landing Pages Custom Domain
- Custom Domain Created
- Custom Domain Deleted
- Enabled Global Control Group
- Disabled Global Control Group
- Updated Global Control Exclusions
- Updated Subscription Group SMS Allow List

### メールテンプレート {#email-template}
- Added Email Template
- Updated Email Template

### プッシュ認証情報 {#push-credential}
Updated Push Credential
Removed Push Credential

### SDKデバッガー {#sdk-debugger}
- Started SDK Debugger Session
- Exported SDK Debugger Log

### ユーザー {#users}
- Users Deleted
- Users Viewed
- User Import Started
- User Subscription Group Status Updated
- User Deleted
- Single User Deletion Cancelled
- Bulk User Deletion Cancelled

### カタログ {#catalogs}
- Catalog Created
- Catalog Deleted

### Braze Agents
- Created Agent
- Edited Agent

### BrazeAI Operator
- Requested BrazeAI Operator Response
- BrazeAI Operator Responded
{% enddetails %}

## 個人を特定できる情報（PII）の表示 {#view-pii}

**PIIを表示**権限は、一部の会社ユーザーのみがアクセスできます。デフォルトでは、すべての管理者のユーザー権限で**PIIを表示**権限がオンになっています。これにより、会社がPIIとして定義したすべての標準属性項目とカスタム属性をダッシュボード全体で確認できます。この権限がユーザーに対してオフになっている場合、そのユーザーはこれらの属性を表示できません。

{% alert note %}
[クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder/building_queries)を使用するには**PIIを表示**権限が必要です。クエリビルダーでは一部の顧客データに直接アクセスできるためです。
{% endalert %}

既存のチーム権限機能については、[ユーザー権限の設定]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)を参照してください。

### PIIの定義 {#defining-pii}

{% alert important %}
特定のフィールドをPIIフィールドとして選択・定義しても、Brazeダッシュボードでユーザーが表示できる内容にのみ影響し、当該PIIフィールドのエンドユーザーデータの取り扱い方法には影響しません。<br><br>[データ保持]({{site.baseurl}}/data_retention)に関連するものを含め、会社に適用されるプライバシー規制やポリシーとダッシュボードの設定を整合させるために、法務チームにご相談ください。
{% endalert %}

ダッシュボードで会社がPIIとして指定するフィールドを選択できます。これを行うには、**設定** > **会社の設定** > **管理者設定** > **セキュリティ設定**に移動します。

以下の属性はPIIとして指定でき、**PIIを表示**権限を持たない会社ユーザーから非表示にできます。

#### PIIの可能性がある属性 {#potential-pii-attributes}

| 標準属性項目 | カスタム属性 |
| ------------------- | ----------------- |
| {::nomarkdown}<ul> <li>メールアドレス</li> <li>電話番号</li> <li>名</li> <li>姓</li> <li>性別</li> <li>生年月日</li> <li>デバイスID</li> <li>LINE ID</li> <li>最新のロケーション</li> </ul> {:/} | {::nomarkdown} <ul> <li>すべてのカスタム属性<ul><li>すべての属性を非表示にする必要がない場合は、個々のカスタム属性をPIIとしてマークできます。</li></ul></li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="PIIの可能性がある属性" }

### 制限されるエリア {#limited-areas}

以下は、すべてのフィールドがPIIとして設定されており、記載されているユーザーがBrazeプラットフォームを使用する会社ユーザーであることを前提としています。また、「前述の」属性は[PIIの可能性がある属性](#potential-pii-attributes)テーブルの属性を指します。ユーザーからPII権限を削除すると、ここに記載されたエリア以外にも使いやすさに影響を与える可能性があります。

| ダッシュボードナビゲーション | 結果 | 注記 |
| -------------------- | ------ | ----- |
| ユーザー検索 | ログインしたユーザーは、メールアドレス、電話番号、名、または姓で検索できません。{::nomarkdown} <ul> <li>ユーザープロファイルを表示する際に、前述の標準属性項目とカスタム属性が表示されません。</li> <li>Brazeダッシュボードからユーザープロファイルの前述の標準属性項目を編集できません。</li> <li>ユーザープロファイルの購読ステータスを更新できません。</li></ul> {:/} | このセクションへのアクセスには、ユーザープロファイルの表示権限が引き続き必要です。 |
| ユーザーインポート | ユーザーは**ユーザーインポート**ページからファイルをダウンロードできません。 | |
| {::nomarkdown} <ul> <li>セグメント</li> <li>キャンペーン</li> <li>キャンバス</li> </ul> {:/} | **ユーザーデータ**ドロップダウンで：{::nomarkdown} <ul> <li>ユーザーには<b>メールアドレスをCSV形式でエクスポート</b>オプションが表示されません。</li> <li><b>ユーザーデータをCSV形式でエクスポート</b>を選択した場合、CSVファイルに前述の標準属性項目とカスタム属性が含まれません。</li> </ul> {:/} | |
| 内部テストグループ | ユーザーは、内部テストグループに追加されたユーザーの前述の標準属性項目にアクセスできません。 | |
| メッセージアクティビティログ | ユーザーは、メッセージアクティビティログで特定されたユーザーの前述の標準属性項目にアクセスできません。 | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="制限されるエリア" }

{% alert note %}
メッセージをプレビューする際、**PIIを表示**権限は適用されないため、メッセージ内でLiquidを通じて参照されている場合、ユーザーは[前述の標準属性項目](#potential-pii-attributes)を確認できます。
{% endalert %}

## データ削除の設定 {#data-deletion-preferences}

この設定を使用して、ユーザー削除プロセス中にBrazeが特定のフィールドをイベントから削除するかどうかの設定を行うことができます。これらの設定は、Brazeが削除したユーザーのデータにのみ適用されます。

ユーザーが削除されると、BrazeはイベントデータからすべてのPII（個人を特定できる情報）を除去しますが、分析目的で匿名化されたデータは保持します。エンドユーザー情報をBrazeに送信している場合、一部のユーザー定義フィールドにPIIが含まれている可能性があります。これらのフィールドにPIIが含まれている場合は、Brazeが削除されたユーザーのイベントデータを匿名化する際にそのデータを削除するよう選択できます。フィールドにPIIが含まれていない場合は、分析のために保持できます。

ワークスペースに対する正しい設定を決定するのはお客様の責任です。適切な設定を決定する最善の方法は、Brazeにイベントデータを送信している社内チーム、およびBrazeでメッセージエクストラを使用しているチームと確認し、フィールドにPIIが含まれる可能性があるかどうかを確認することです。

### 関連フィールド {#relevant-fields}

| イベント名またはタイプ | フィールド | 備考 |
| -------------------- | ------ | ----- |
| カスタムイベント | properties |  |
| 購入イベント | properties |  |
| メッセージ送信 | message_extras | いくつかのイベントタイプに`message_extras`フィールドが含まれています。この設定は、将来追加されるイベントタイプを含め、`message_extras`をサポートするすべてのメッセージ送信イベントタイプに適用されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="関連フィールド" }

{% alert warning %}
**削除は永久的です！** 削除されたユーザーのSnowflakeからフィールドを除去することを選択した場合、この設定はワークスペース内のすべての過去のデータと、将来削除されるユーザーのすべてのイベントに適用されます。Brazeが削除されたユーザーの過去のイベントデータに設定を適用するプロセスを実行した後は、データを**復元することはできません**。
{% endalert %}

### 設定の構成 {#configure-preferences}

Brazeがユーザーの削除時に除去すべきフィールドのチェックボックスをオンにして、デフォルトの設定を行います。PIIが含まれるフィールドを選択してください。この設定は、ワークスペースが設定グループに明示的に追加されない限り、現在および将来のすべてのワークスペースに適用されます。

ワークスペースごとに設定をカスタマイズするには、デフォルトとは異なる設定の設定グループを追加できます。追加の設定グループに追加されていないワークスペース（将来作成されるワークスペースを含む）には、デフォルトの設定が適用されます。

![ワークスペースごとにデータ削除設定をカスタマイズするトグルがオンになっている「データ削除の設定」セクション。]({% image_buster /assets/img/deletion_preferences_1.png %})

## トラブルシューティング {#troubleshooting}

### 2要素認証（2FA）設定のループ問題 {#two-factor-authentication-2fa-setup-loop-issues}

2FAの電話番号入力に成功した後、ログインページにリダイレクトされるループに陥った場合、最初の試行で認証に失敗したことが原因である可能性があります。この問題を解決するには、次の手順に従ってください。

1. 広告ブロッカーをオフにします。
2. ブラウザの設定でCookieを有効にします。
3. PCまたはノートパソコンを再起動します。
4. 2FAの設定を再試行します。

これらの手順を実行しても問題が解決しない場合は、[サポート]({{site.baseurl}}/braze_support)にお問い合わせください。

### 2要素認証（2FA）を有効にできない {#cant-enable-two-factor-authentication-2fa}

2FAが有効になっているにもかかわらず、**有効にする**ボタンを選択しても何も起こらない場合、ブラウザがSMSで認証コードを送信するために必要なリダイレクトをブロックしていることが原因である可能性があります。この問題をトラブルシューティングする手順は次のとおりです。

1. ブラウザで有効にしている広告ブロッカーを一時的に停止します。
2. ブラウザの設定でサードパーティCookieが有効になっていることを確認します。
3. 2FAの設定を試みます。

### 認証コードが送信されない {#verification-code-doesnt-send}

Authyページで電話番号を入力した際にSMSが届かない問題が発生した場合は、次の手順に従ってください。

1. スマートフォンにAuthyアプリをインストールし、Authy認証アプリにログインします。
2. 電話番号を入力し、Authyアプリに変更やSMS通知がないか確認します。
3. それでもSMSが届かない場合は、自宅のネットワークや企業以外のWi-Fiなど、別のネットワーク接続を試してください。企業ネットワークには、SMS配信を妨げるセキュリティポリシーが設定されている場合があります。

問題が解決しない場合は、Authyアプリで古いプロファイルを削除し、QRコードを再スキャンして2FAを設定し直してください。再設定を試みる前に、広告ブロッカーを無効にし、サードパーティCookieを有効にするか、別のブラウザを使用していることを確認してください。

## 次のステップ {#next-steps}

認証とアクセスの詳細については、以下を参照してください。

- [SAML & シングルサインオン]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on): IDプロバイダーでSSOを設定します。
- [権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions): ダッシュボードでユーザーが実行できるアクションを制御します。