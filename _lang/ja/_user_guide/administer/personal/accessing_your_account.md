---
nav_title: アカウントへのアクセス
article_title: アカウントへのアクセス
page_order: 0
page_type: reference
description: "この記事では、Brazeアカウントの取得方法、アクセス権が付与された後のログイン方法、ダッシュボードへのアクセスやダッシュボードのパフォーマンスに関するトラブルシューティング方法について説明します。"

---

# アカウントへのアクセス {#access-your-account}

> この記事では、Brazeアカウントの取得方法、アクセス権が付与された後のログイン方法、ダッシュボードへのアクセスやダッシュボードのパフォーマンスに関するトラブルシューティング方法について説明します。

あなたが会社で最初のBrazeユーザーであり、初めてログインする場合、契約開始日に `@alerts.braze.com` からウェルカムメールが届き、メールアドレスの確認とログインを求められます。

アカウントを確認した後、ダッシュボードの[会社ユーザー]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users)ページからユーザーを追加できます。追加されたすべてのユーザーには、アカウントの確認を求めるメールが届きます。

会社のBrazeアカウントの最初のユーザーでない場合は、会社のBrazeアカウント管理者に連絡してアカウントの作成を依頼してください。その後、`@alerts.braze.com` からウェルカムメールが届き、メールアドレスの確認とログインを求められます。

## ログイン {#logging-in}

初めてのログインでも、何度目のログインでも、ダッシュボードへのアクセス方法は同じです。会社で最初のユーザーの場合は、前のセクションのガイダンスに従ってください。それ以外の場合は、会社のBraze管理者がアカウントを作成した後にログインできます。

[Braze.com](https://www.braze.com) のホームサイトからログインするか、特定の[Brazeインスタンス]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)に対応するダッシュボードURLを使用できます。利便性のため、Brazeでは以下のようなシングルサインオン（SSO）オプションを提供しています。

* [SAML SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup)
    * [SAMLジャストインタイムプロビジョニング]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning)
* [Microsoft Entra SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso)
* [Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta)
* [OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin)

SSOでBrazeにログインした後は、パスワードを使用してダッシュボードにログインすることはできなくなります。両方のメールアドレスは同じ受信トレイにメールを送信しますが、ログイン時にBrazeはそれらを別々のアカウントとして認識します。Cookieをクリアするとログアウトされるため、保存されていない作業は失われます。

## サポートされているブラウザ {#supported-browsers}

Brazeダッシュボードは以下のブラウザをサポートしています：
- Chrome（バージョン87以降）
- Firefox（バージョン85以降）
- Safari（バージョン15.4以降）
- Edge（バージョン87以降）

Brazeダッシュボードで予期しないエラーが表示され、ブラウザのコンソールツールに`ReferenceError: structuredClone is not defined`というエラーが表示される場合、ブラウザが古くなっています。このエラーが繰り返し発生する場合は、ブラウザをアンインストールしてから再インストールしてください。

## 複数のBrazeダッシュボードへのアクセス {#accessing-multiple-braze-dashboards}

Brazeでは、同じクラスター内の複数のダッシュボードユーザーに同じメールアドレスを登録することはできません（例えば、US-01に2つのダッシュボードがある場合）。異なるクラスターでは同じメールアドレスを使用してアカウントを作成できます（例えば、US-01に1つ、US-05に1つのダッシュボードがある場合）。同じクラスター内の複数のBrazeダッシュボードにアクセスする必要がある場合は、以下の方法を使用できます。

### メールエイリアスを使用する {#use-email-aliases}

メールプロバイダーがGmailの場合、メールアドレスに `+` 記号とテキストを追加してエイリアスを作成できます。例：
- **元のメールアドレス：** `rocky@gmail.com`
- **エイリアスメールアドレス：** `rocky+1@gmail.com`

どちらのメールアドレスも同じ受信トレイにメールが届きますが、Brazeではログイン時に別々のアカウントとして認識されます。

### 他のプロバイダーで別のエイリアスを作成する {#create-separate-aliases-with-other-providers}

メールプロバイダーが `+` エイリアスをサポートしていない場合でも、別のエイリアスを作成できます。例えば、`rocky@braze.com` を `rocky.lotito@braze.com` に転送するように設定できます。これにより、複数のアドレスが同じ受信トレイに集約されながら、Brazeでは異なるメールアドレスとして認識されます。

### マルチカンパニー開発者を使用する {#use-multi-company-developers}

マルチカンパニー開発者機能を使用すると、1つのユーザーアカウントを複数の会社間で共有できます。ダッシュボードユーザーは、ユーザープロファイルメニューから異なる会社のダッシュボードを切り替えることができます。

SSOを使用していてマルチカンパニー開発者を設定したい場合は、カスタムSAML SSO統合を設定してSAMLカスタムエンティティIDを有効にする必要があります。[サービスプロバイダー（SP）によるログイン]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup)の手順に従い、以下の変更を適用してください：
- 各ダッシュボード統合の**エンティティID**を `braze_dashboard_<companyID>` に変更します。
- カスタマーサクセスマネージャーまたはアカウントマネージャーに連絡して、各ダッシュボードの `saml_sso_custom_entity_id` 機能フリッパーを有効にしてもらいます。

#### 2要素認証（2FA） {#two-factor-authentication-2fa}

マルチカンパニー開発者における2FAの動作は、2FAの方法によって異なります：

- **メールとSMS：** 2FA設定はリンクされたすべての開発者アカウントにコピーされます。1つのアカウントでメールまたはSMSの2FAを設定すると、同じ方法がすべての会社のダッシュボードに適用されます。
- **時間ベースのワンタイムパスワード（TOTP）：** TOTP設定はアカウント間で同期されません。認証アプリを使用している場合は、直接サインインする各ダッシュボードに対して個別のコードを設定する必要があります。

ダッシュボード内でアカウントを切り替える場合、2FAの完了が必要なのは1回だけです。そのセッション中にリンクされたアカウントに最初にサインインしたときのみです。

### シングルサインオン（SSO）に関する注意事項 {#considerations-for-single-sign-on-sso}

シングルサインオン（SSO）を使用している場合、複数の異なるメールアドレスを持つことで問題が発生する可能性があることに注意してください。アクセスの問題を避けるために、SSO設定が正しく構成されていることを確認してください。

## トラブルシューティング {#troubleshooting}

### パスワードのリセット {#resetting-your-password}

パスワードをリセットするには、ダッシュボードのログインページで**Forgot your password?**リンクを選択します。メールアドレスの入力を求められ、パスワードリセット用のリンクが送信されます。

![「Forgot your password?」プロンプトが表示されたダッシュボードログイン画面。]({% image_buster /assets/img_archive/enable_reset.png %}){: style="max-width:60%"}

### ブラウザのキャッシュとCookieのクリア {#clearing-your-browser-cache-and-cookies}

ダッシュボードやセグメントのパフォーマンスリストが読み込まれないなど、ダッシュボードのパフォーマンスに問題がある場合は、お使いのブラウザに応じた手順でブラウザのキャッシュとCookieをクリアしてください。

{% alert important %}
Cookieをクリアするとログアウトされるため、保存されていない作業内容は失われます。
{% endalert %}

- [Chrome でキャッシュとCookieをクリアする](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [Mac の Safari でCookieをクリアする](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [Firefox でCookieとサイトデータをクリアする](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Microsoft Edge ですべてのCookieを削除する](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

ブラウザのキャッシュとCookieをクリアしても問題が解決しない場合は、[サポート]({{site.baseurl}}/support_contact)にお問い合わせください。

### Google Chrome の「Aw, Snap!」エラー {#aw-snap-error-in-google-chrome}

Google Chrome で「Aw, Snap!」エラーが表示される場合、Chrome がBrazeダッシュボードページの読み込みに問題を抱えています。トラブルシューティングの手順については、[Chrome の一般的なエラーメッセージに関するヘルプ](https://support.google.com/chrome/answer/95669?co=GENIE.Platform%3DDesktop&hl=en)を参照してください。

### ダッシュボード操作中の「Please Refresh Page」または「Unexpected Error」 {#please-refresh-page-or-unexpected-error-while-navigating-the-dashboard}

このエラーは、企業ユーザーがどのワークスペースにも所属していない場合に表示されることがあります。トラブルシューティングの手順は以下のとおりです。

1. [企業ユーザー]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users)ページに移動します。
2. ユーザーがワークスペースに追加されているか確認します。
3. どのワークスペースにも所属していない場合は、ユーザーを追加し、適切な権限を割り当てます。
4. ユーザーにダッシュボードを更新するよう依頼します。
5. 問題が解決しない場合は、[サポート]({{site.baseurl}}/support_contact)にお問い合わせください。

### ドラッグ＆ドロップエディターへのアクセス {#accessing-the-drag-and-drop-editor}

ほとんどの企業ユーザーの場合、ドラッグ＆ドロップエディターは正常に読み込まれます。ただし、VPNを使用している場合やファイアウォールの背後にいる場合は、ドメインを許可リストに追加する必要がある場合があります。IT管理者に連絡して、`*.bz-rndr.com` が許可リストに追加されているか確認してください。

エディターは以下の原因で読み込みの問題が発生する場合があります。

- **一時的なエラー：**接続、通信、またはデータ転送に影響を与える一時的な障害です。通常、短期間の状態が原因であり、システム全体の問題を示すものではないため、大きな対応を必要とせず自然に解決します。
- **重大なエラー：**基盤となるインフラまたは製品の問題が関係している可能性があります。[Brazeシステムステータスページ](https://braze.statuspage.io/)を確認してください。状況を把握し、解決に向けて積極的に取り組んでいる可能性があります。

{% alert important %}
それでも問題が解決しない場合は、[サポートチケットを作成]({{site.baseurl}}/user_guide/administer/personal/braze_support)してください。その前に、IT管理者が `*.bz-rndr.com` が許可リストに追加されていることを確認済みであることをご確認ください。
{% endalert %}

### Braze Learningへのアクセス {#accessing-braze-learning}

Braze Learningへのログインに問題があり、ダッシュボードにリダイレクトされるループに陥っている場合は、以下の手順を実行してください。

1. 複数のBrazeアカウントをお持ちの場合、誤ったアカウントで2回ログインするとBrazeダッシュボードに送られます。正しいアカウントでログインしていることを確認してください。
2. 広告ブロッカーを使用している場合は、オフになっていることを確認してください。シングルサインオン機能に必要なCookieがブロックされている可能性があります。
3. **会社設定** > **セキュリティ設定**に移動し、シングルサインオン（SSO）がオンになっていることを確認します。
4. ダッシュボードのユーザープロファイルに姓と名の両方が含まれていることを確認します。姓がない場合、ログインプロセスが中断される可能性があります。
5. ダッシュボードから**サポート** > **Braze Learning**に移動してBraze Learningにアクセスします。
6. 引き続き問題が発生する場合は、アカウントの再作成を検討してください。無料トライアル期間中にBraze Learningにアクセスしたユーザーは、現在アクセスに問題が生じる場合があります。

### 2要素認証（2FA）の問題 {#two-factor-authentication-2fa-issues}

ユーザーが2要素認証（2FA）に問題を抱えており、Brazeダッシュボードにアクセスできない場合、いくつかの原因が考えられます。最も一般的なのは、登録された電話番号やAuthyアプリがインストールされているデバイスにアクセスできなくなっている場合です。

管理者は、以下の手順で影響を受けたユーザーの2FAをリセットする必要があります。

1. **ユーザーの管理**に移動します。
2. 2FAの問題が発生しているユーザーの**ユーザーを編集**を選択します。
3. 2FAをリセットするオプションを選択します。
4. プロンプトが表示されたら、2FAのリセットを確認します。
5. リセットしても問題がすぐに解決しない場合は、Cookieとキャッシュをクリアしてください。

セキュリティ上の理由から、Brazeはユーザーに代わって2FAをリセットすることはできません。管理者が2FAをリセットできない場合は、サポートチケットを作成してください。

#### 考慮事項 {#considerations}

- 2FAが企業レベルで強制されている場合：リセット後、Brazeは次回ログイン時にユーザーに2FAの再設定を求めます。
- 2FAが企業レベルで強制されていない場合：ユーザーは2FAの再設定なしでダッシュボードにログインできます。2FAを有効にしたい場合は、アカウント設定から行うことができます。

{% alert note %}
このリセットプロセスは、過去1時間以内にトークンを要求しすぎてアカウントからロックアウトされたユーザーにも適用されます。
{% endalert %}

### アカウントからのロックアウト {#locked-out-of-account}

Brazeアカウントからロックアウトされた場合は、以下の手順で再度アクセスできます。

受け取ったエラーメッセージから、どのようなロックアウトが発生しているかを判断できます。

- [パスワードに関するエラーが表示される。](#password-error)
- [エラーは表示されないが、Brazeにログインできない。](#instance-error)
- [アカウント停止に関するエラーが表示される。](#account-suspension)

#### パスワードエラー {#password-error}

アカウントのセキュリティは重要であるため、Brazeアカウントへのログインにはパスワードが必要です。
- 正しい[Brazeダッシュボードインスタンス]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)にログインしていることを確認してください。アカウント管理者またはBrazeアカウントマネージャーに確認してください。
- パスワードの有効期限が切れている可能性があるため、[リセット](#resetting-your-password)が必要です。
- [シングルサインオン]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup)サービスを使用している場合は、アカウント管理者に設定が正しく完了しているか確認してください。
- 会社が複数のBrazeインスタンスを使用している場合、ログインに誤ったメールアドレスを使用している可能性があります。

不明な場合は、いつでも[パスワードをリセット](#resetting-your-password)できます。

#### インスタンスエラー {#instance-error}

通常使用しているマシンでログインしている場合、Brazeは自動的に正しいインスタンスを検出します。ただし、検出されない場合や初めてログインする場合は、以下を検討してください。

- 正しい[Brazeダッシュボードインスタンス]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)にログインしていることを確認してください。アカウント管理者またはBrazeアカウントマネージャーに確認してください。
- 会社が複数のBrazeインスタンスを使用している場合、ログインに誤ったメールアドレスを使用している可能性があります。

#### アカウント停止 {#account-suspension}

これは頻繁に発生するものではありませんが、Brazeはアカウントの停止と削除を非常に重要視しています。このエラーが発生した場合は、会社のBraze管理者、Brazeアカウントマネージャー、または[サポート][support]にお問い合わせください。

### Brazeダッシュボードが読み込まれない、または期待どおりに動作しない {#braze-dashboard-wont-load-or-work-as-expected}

まず、別のブラウザでダッシュボードが読み込まれるかテストしてください。別のブラウザで問題が発生しない場合は、以下を試してください。

- **ダッシュボードを再起動する：**ログアウトし、ブラウザを終了してから、ダッシュボードに再度ログインしてください。
- **ローカルブラウザを更新する：**[CookieとブラウザキャッシュをクリアしてからI](#clearing-your-browser-cache-and-cookies)、ダッシュボードに再度ログインしてください。
- **互換性のあるプラグインまたはサードパーティツールを使用する：**広告ブロッカーやセキュリティソフトウェアがBrazeダッシュボードの読み込みを妨げている可能性があります。広告ブロッカーを無効にしてから、Brazeダッシュボードにログインしてテストしてください。
        - ブラウザのコンソールログも確認できます。`ERR_BLOCKED_BY_CLIENT` に関連するエラーは、コンテンツが広告ブロッカーによってブロックされていることを示している可能性があります。
- **接続品質を確認する：**接続品質が低い可能性があります。別のデバイスでBrazeダッシュボードにログインしてみてください。
- **正しいクラスターにアクセスしていることを確認する：**会社に割り当てられたクラスターにログインしていることを確認してください。たとえば、US-03に割り当てられているのに、US-01にログインしている場合があります。
- **ブラウザを更新する：**ブラウザを最新の[サポートされているブラウザ](#supported-browsers)に更新してから、ダッシュボードにログインしてください。

すべてのブラウザで問題が発生する場合は、以下を試してください。

- **ネットワーク接続を確認する：**可能であればVPNをオフにするか、ネットワーク接続を無効にしてから再度有効にしてください。
- **デバイスを再起動する：**デバイスを再起動してから、Brazeダッシュボードにログインしてみてください。

上記の問題を解決してもダッシュボードが読み込まれない、または期待どおりに動作しない場合は、[サポート]({{site.baseurl}}/braze_support)にお問い合わせください。

### ユーザーがどのワークスペースにも所属していない {#the-user-belongs-to-no-workspace}

**設定** > **企業ユーザー**に移動し、ユーザーのワークスペースレベルの権限を確認してください。必要なワークスペースを**ワークスペース**に追加してください。

### 新規ユーザーとしてのトラブルシューティング {#troubleshooting-as-a-new-user}

Brazeの新規ユーザーで、初めてのログインやアカウントへのアクセスに問題がある場合は、以下の手順で一般的な問題を解決してください。

#### ウェルカムメールが届かない {#i-never-received-the-welcome-email}

- 迷惑メールフォルダを確認する：アカウント有効化メールが迷惑メールフォルダにフィルタリングされていないか確認してください。
- メールアドレスを確認する：管理者に、新しいBrazeアカウントに関連付けられたメールアドレスが正しいか確認してもらってください。
- ITポリシー：有効化メールの受信を妨げるポリシーがないか、ITチームに確認してください。

#### メールは届いたが、2要素認証（2FA）の設定で行き詰まっている {#i-received-the-email-but-im-stuck-setting-up-two-factor-authentication-2fa}

- 2FAのリセット：2FAの設定に問題がある場合、管理者が設定でユーザーアカウントの2FAをリセットできます。
- ユーザーの再追加：問題が解決しない場合、管理者がダッシュボードからユーザーアカウントを削除し、再度追加できます。これにより、同じ詳細情報でユーザーを再作成できます。

これらの手順を実行しても問題が解決しない場合は、[サポート]({{site.baseurl}}/braze_support)にお問い合わせください。

## 次のステップ {#next-steps}

アカウントにアクセスした後、以下のリソースをご確認ください。

- [Brazeダッシュボード]({{site.baseurl}}/user_guide/administer/personal/the_braze_dashboard)で、主要な機能やツールの操作方法を学びましょう。
- [言語設定]({{site.baseurl}}/user_guide/administer/personal/language_settings)で、ダッシュボードの表示言語を設定できます。