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

初めてのログインでも100回目のログインでも、ダッシュボードへのアクセス方法は以下のとおりです。会社の最初のユーザーの場合は、前のセクションのガイダンスに従ってください。それ以外の場合は、会社のBraze管理者がアカウントを作成した後にログインできます。

[Braze.com](https://www.braze.com)のホームサイトからログインするか、特定の[Brazeインスタンス]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)に対応するダッシュボードURLを使用できます。利便性のため、Brazeでは以下のようなシングルサインオン（SSO）オプションを提供しています。

* [SAML SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup)
    * [SAMLジャストインタイムプロビジョニング]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning)
* [Microsoft Entra SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso)
* [Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta)
* [OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin)

SSOでBrazeにログインした後は、パスワードを使用してダッシュボードにログインすることはできなくなります。両方のメールアドレスは同じ受信トレイにメールを配信しますが、ログイン時にBrazeはそれらを別々のアカウントとして認識します。Cookieをクリアするとログアウトされるため、保存されていない作業は失われます。

## サポートされているブラウザー {#supported-browsers}

Brazeダッシュボードは以下のブラウザーをサポートしています。
- Chrome（バージョン87以降）
- Firefox（バージョン85以降）
- Safari（バージョン15.4以降）
- Edge（バージョン87以降）

Brazeダッシュボードで予期しないエラーが表示され、ブラウザーのコンソールツールに `ReferenceError: structuredClone is not defined` というエラーが表示される場合、ブラウザーが古くなっています。このエラーが繰り返し発生する場合は、ブラウザーをアンインストールして再インストールしてください。

## 複数のBrazeダッシュボードへのアクセス {#accessing-multiple-braze-dashboards}

Brazeでは、同じクラスター内の複数のダッシュボードユーザーに同じメールアドレスを登録することはできません（例えば、US-01に2つのダッシュボードがある場合）。異なるクラスターのアカウントには同じメールアドレスを使用できます（例えば、US-01に1つ、US-05に1つのダッシュボードがある場合）。同じクラスター内の複数のBrazeダッシュボードにアクセスする必要がある場合は、以下の方法を使用できます。

### メールエイリアスを使用する {#use-email-aliases}

メールプロバイダーがGmailの場合、メールアドレスに `+` 記号とテキストを追加してエイリアスを作成できます。例：
- **元のメール:** `rocky@gmail.com`
- **エイリアスメール:** `rocky+1@gmail.com`

両方のメールアドレスは同じ受信トレイにメールを配信しますが、ログイン時にBrazeはそれらを別々のアカウントとして認識します。

### 他のプロバイダーで別のエイリアスを作成する {#create-separate-aliases-with-other-providers}

メールプロバイダーが `+` エイリアスをサポートしていない場合でも、`rocky@braze.com` を `rocky.lotito@braze.com` に転送するように設定するなど、別のエイリアスを作成できます。これにより、複数のアドレスが同じ受信トレイに集約されながら、Brazeでは異なるメールとして認識されます。

### マルチカンパニー開発者を使用する {#use-multi-company-developers}

マルチカンパニー開発者機能を使用すると、1つのユーザーアカウントを複数の会社間で共有できます。ダッシュボードユーザーはユーザープロファイルメニューから異なる会社のダッシュボードを切り替えることができます。

SSOを使用していてマルチカンパニー開発者を設定する場合は、カスタムSAML SSO統合を設定してSAMLカスタムエンティティIDを有効にする必要があります。[サービスプロバイダー（SP）起動ログイン]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup)の手順に従い、以下の変更を適用してください。
- 各ダッシュボード統合の**Entity ID**を `braze_dashboard_<companyID>` に変更します。
- カスタマーサクセスマネージャーまたはアカウントマネージャーに連絡して、各ダッシュボードの `saml_sso_custom_entity_id` 機能フリッパーを有効にしてもらいます。

#### 2要素認証（2FA） {#two-factor-authentication-2fa}

マルチカンパニー開発者の2FAの動作は、2FAの方法によって異なります。

- **メールとSMS:** 2FA設定はリンクされたすべての開発者アカウントにコピーされます。1つのアカウントでメールまたはSMSの2FAを設定すると、同じ方法がすべての会社ダッシュボードに適用されます。
- **時間ベースのワンタイムパスワード（TOTP）:** TOTP設定はアカウント間で同期されません。認証アプリを使用している場合は、直接サインインする各ダッシュボードに対して個別のコードを設定する必要があります。

ダッシュボード内でアカウントを切り替える場合、2FAの完了は1回のみ必要です。そのセッション中にリンクされたアカウントに最初にサインインしたときだけです。

### シングルサインオン（SSO）に関する注意事項 {#considerations-for-single-sign-on-sso}

シングルサインオン（SSO）を使用している場合、複数の異なるメールアドレスを持つことで問題が発生する可能性があることに注意してください。アクセスの問題を避けるために、SSO設定が正しく構成されていることを確認してください。

## トラブルシューティング {#troubleshooting}

### パスワードのリセット {#resetting-your-password}

パスワードをリセットするには、ダッシュボードのログインページで**Forgot your password?**リンクを選択します。メールアドレスの入力を求められ、パスワードをリセットするためのリンクが送信されます。

![「Forgot your password?」プロンプトが表示されたダッシュボードログイン画面。]({% image_buster /assets/img_archive/enable_reset.png %}){: style="max-width:60%"}

### ブラウザーのキャッシュとCookieのクリア {#clearing-your-browser-cache-and-cookies}

ダッシュボードやセグメントパフォーマンスリストが読み込まれないなど、ダッシュボードのパフォーマンスに問題がある場合は、使用しているブラウザーの手順に従ってブラウザーのキャッシュとCookieをクリアしてください。

{% alert important %}
Cookieをクリアするとログアウトされるため、保存されていない作業は失われます。
{% endalert %}

- [ChromeでキャッシュとCookieをクリアする](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [MacのSafariでCookieをクリアする](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [FirefoxでCookieとサイトデータをクリアする](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Microsoft EdgeですべてのCookieを削除する](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

ブラウザーのキャッシュとCookieをクリアしても問題が解決しない場合は、[サポート]({{site.baseurl}}/support_contact)にお問い合わせください。

### Google Chromeの「Aw, Snap!」エラー {#aw-snap-error-in-google-chrome}

Google Chromeで「Aw, Snap!」エラーが表示される場合、ChromeがBrazeダッシュボードページの読み込みに問題を抱えています。トラブルシューティングの手順については、[Chromeの一般的なエラーメッセージに関するヘルプ](https://support.google.com/chrome/answer/95669?co=GENIE.Platform%3DDesktop&hl=en)を参照してください。

### ダッシュボードのナビゲーション中に「Please Refresh Page」または「Unexpected Error」が表示される {#please-refresh-page-or-unexpected-error-while-navigating-the-dashboard}

このエラーは、会社ユーザーがどのワークスペースにも属していない場合に表示されることがあります。トラブルシューティングの手順：

1. [会社ユーザー]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users)ページに移動します。
2. ユーザーがワークスペースに追加されているか確認します。
3. どのワークスペースにも属していない場合は、ユーザーを追加して適切な権限を割り当てます。
4. ユーザーにダッシュボードを更新するよう依頼します。
5. 問題が解決しない場合は、[サポート]({{site.baseurl}}/support_contact)にお問い合わせください。

### ドラッグ＆ドロップエディターへのアクセス {#accessing-the-drag-and-drop-editor}

ほとんどの会社ユーザーの場合、ドラッグ＆ドロップエディターは読み込まれます。ただし、VPNを使用しているか、ファイアウォールの背後にいる場合は、ドメインを許可リストに追加する必要がある場合があります。IT管理者に連絡して、`*.bz-rndr.com` が許可リストに追加されていることを確認してください。

エディターは以下の理由で読み込みの問題が発生する場合があります。

- **一時的なエラー:** 接続、通信、またはデータ転送に影響を与える可能性のある一時的な障害です。通常、短期間の状態が原因であり、システム的な問題を示すものではないため、大きな介入を必要とせずに自然に解決します。
- **重大なエラー:** 基盤となるインフラまたは製品の問題が関係している可能性があります。[Brazeシステムステータスページ](https://braze.statuspage.io/)を確認してください。状況を把握し、解決に向けて積極的に取り組んでいる可能性があります。

{% alert important %}
それでも問題が発生する場合は、[サポートチケットを作成]({{site.baseurl}}/user_guide/administer/personal/braze_support)してください。その前に、IT管理者が `*.bz-rndr.com` が許可リストに追加されていることを確認してください。
{% endalert %}

### Braze Learningへのアクセス {#accessing-braze-learning}

Braze Learningへのログインに問題があり、ダッシュボードにリダイレクトされるループに陥っている場合は、以下の手順を実行してください。

1. 複数のBrazeアカウントをお持ちの場合、間違ったアカウントで2回ログインするとBrazeダッシュボードに送られます。正しいアカウントでログインしていることを確認してください。
2. 広告ブロッカーを使用している場合は、オフになっていることを確認してください。シングルサインオン機能に必要なCookieがブロックされている可能性があります。
3. **会社の設定** > **セキュリティ設定**に移動し、シングルサインオン（SSO）がオンになっていることを確認します。
4. ダッシュボードのユーザープロファイルに姓と名の両方が含まれていることを確認します。姓がないとログインプロセスが中断される可能性があります。
5. ダッシュボードから**サポート** > **Braze Learning**に移動してBraze Learningにアクセスします。
6. 引き続き問題が発生する場合は、アカウントの再作成を検討してください。無料トライアル期間中にBraze Learningにアクセスしたユーザーは、現在アクセスに問題が発生する場合があります。

### 2要素認証（2FA）の問題 {#two-factor-authentication-2fa-issues}

ユーザーが2要素認証（2FA）に問題があり、Brazeダッシュボードにアクセスできない場合、いくつかの原因が考えられます。最も一般的なのは、登録された電話番号やAuthyアプリがインストールされているデバイスにアクセスできなくなった場合です。

管理者は、以下の手順で影響を受けたユーザーの2FAをリセットする必要があります。

1. **ユーザーを管理**に移動します。
2. 2FAの問題が発生しているユーザーの**ユーザーを編集**を選択します。
3. 2FAをリセットするオプションを選択します。
4. プロンプトが表示されたら2FAのリセットを確認します。
5. リセットしても問題がすぐに解決しない場合は、Cookieとキャッシュをクリアしてください。

セキュリティ上の理由から、Brazeはユーザーに代わって2FAをリセットすることはできません。管理者が2FAをリセットできない場合は、サポートチケットを作成してください。

#### 注意事項 {#considerations}

- 2FAが会社レベルで強制されている場合：リセット後、次回ログイン時にBrazeがユーザーに2FAの再設定を求めます。
- 2FAが会社レベルで強制されていない場合：ユーザーは2FAを再設定する必要なくダッシュボードにログインできます。2FAを有効にしたい場合は、アカウント設定で行うことができます。

{% alert note %}
このリセットプロセスは、過去1時間以内にトークンを要求しすぎてアカウントからロックアウトされたユーザーにも適用されます。
{% endalert %}

### アカウントからのロックアウト {#locked-out-of-account}

Brazeアカウントからロックアウトされた場合は、以下の手順に従ってアクセスを回復できます。

受信するエラーメッセージから、どのようなロックアウトが発生しているかを判断できます。

- [パスワードに関するエラーが表示される。](#password-error)
- [エラーは表示されないが、Brazeにログインできない。](#instance-error)
- [アカウント停止に関するエラーが表示される。](#account-suspension)

#### パスワードエラー {#password-error}

アカウントのセキュリティは重要であるため、Brazeアカウントへのログインにはパスワードが必要です。
- 正しい[Brazeダッシュボードインスタンス]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)にログインしていることを確認してください。アカウント管理者またはBrazeアカウントマネージャーに確認してください。
- パスワードの有効期限が切れている可能性があるため、[リセット](#resetting-your-password)が必要です。
- [シングルサインオン]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup)サービスを使用している場合は、アカウント管理者に設定が正しく完了しているか確認してください。
- 会社がBrazeの複数のインスタンスを使用している場合、ログインに間違ったメールアドレスを使用している可能性があります。

迷った場合は、いつでも[パスワードをリセット](#resetting-your-password)できます。

#### インスタンスエラー {#instance-error}

通常使用しているマシンでログインしている場合、Brazeは自動的に正しいインスタンスを検出します。ただし、検出されない場合や初めてログインする場合は、以下を検討してください。

- 正しい[Brazeダッシュボードインスタンス]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)にログインしていることを確認してください。アカウント管理者またはBrazeアカウントマネージャーに確認してください。
- 会社がBrazeの複数のインスタンスを使用している場合、ログインに間違ったメールアドレスを使用している可能性があります。

#### アカウント停止 {#account-suspension}

これはあまり頻繁には発生しませんが、Brazeはアカウントの停止と削除を非常に重要視しています。このエラーが発生した場合は、会社のBraze管理者、Brazeアカウントマネージャー、または[サポート][support]にお問い合わせください。

### Brazeダッシュボードが読み込まれない、または期待どおりに動作しない {#braze-dashboard-wont-load-or-work-as-expected}

まず、別のブラウザーでダッシュボードが読み込まれるかテストしてください。別のブラウザーで問題が発生しない場合は、以下を試してください。

- **ダッシュボードを再起動する:** ログアウトし、ブラウザーを終了してから、ダッシュボードにログインし直してください。
- **ローカルブラウザーを更新する:** [Cookieとブラウザーキャッシュをクリア](#clearing-your-browser-cache-and-cookies)してから、ダッシュボードに再度ログインしてください。
- **互換性のあるプラグインまたはサードパーティツールを使用する:** 広告ブロッカーやセキュリティソフトウェアがBrazeダッシュボードの読み込みを妨げている可能性があります。広告ブロッカーを無効にしてから、Brazeダッシュボードにログインしてテストしてください。
        - ブラウザーのコンソールログも確認できます。`ERR_BLOCKED_BY_CLIENT` に関連するエラーは、コンテンツが広告ブロッカーによってブロックされていることを示している可能性があります。
- **接続品質を確認する:** 接続品質が低い可能性があります。別のデバイスでBrazeダッシュボードにログインしてみてください。
- **正しいクラスターにアクセスしていることを確認する:** 会社に割り当てられたクラスターにログインしていることを確認してください。例えば、US-03に割り当てられているのにUS-01にログインしている可能性があります。
- **ブラウザーを更新する:** ブラウザーを最新の[サポートされているブラウザー](#supported-browsers)に更新してから、ダッシュボードにログインしてください。

すべてのブラウザーで問題が発生する場合は、以下を試してください。

- **ネットワーク接続を確認する:** 可能であればVPNをオフにするか、ネットワーク接続を無効にしてから再度有効にしてください。
- **デバイスを再起動する:** デバイスを再起動してから、Brazeダッシュボードにログインしてみてください。

上記の問題を解決してもダッシュボードが読み込まれない、または期待どおりに動作しない場合は、[サポート]({{site.baseurl}}/braze_support)にお問い合わせください。

### ユーザーがどのワークスペースにも属していない {#the-user-belongs-to-no-workspace}

**設定** > **会社ユーザー**に移動し、ユーザーのワークスペースレベルの権限を確認してください。必要なワークスペースを**ワークスペース**に追加してください。

### 新規ユーザーとしてのトラブルシューティング {#troubleshooting-as-a-new-user}

新しいBrazeユーザーで、初めてのログインやアカウントへのアクセスに問題がある場合は、以下の手順に従って一般的な問題を解決してください。

#### ウェルカムメールが届かない {#i-never-received-the-welcome-email}

- 迷惑メールフォルダーを確認する：アカウント有効化メールが迷惑メールフォルダーにフィルタリングされていないか確認してください。
- メールアドレスを確認する：管理者に、新しいBrazeアカウントに関連付けられたメールアドレスが正しいか確認してもらってください。
- ITポリシー：有効化メールの受信を妨げるポリシーがないか、ITチームに確認してください。

#### メールは届いたが、2要素認証（2FA）の設定で行き詰まっている {#i-received-the-email-but-im-stuck-setting-up-two-factor-authentication-2fa}

- 2FAをリセットする：2FAの設定に問題がある場合、管理者が設定でユーザーアカウントの2FAをリセットできます。
- ユーザーを再追加する：問題が解決しない場合、管理者がダッシュボードからユーザーアカウントを削除し、再度追加できます。これにより、同じ詳細情報でユーザーを作成し直すことができます。

これらの手順を実行しても問題が解決しない場合は、[サポート]({{site.baseurl}}/braze_support)にお問い合わせください。

## 次のステップ {#next-steps}

アカウントにアクセスした後、以下のリソースをご覧ください。

- [Brazeダッシュボード]({{site.baseurl}}/user_guide/administer/personal/the_braze_dashboard)で、主要な機能やツールのナビゲーション方法を学びましょう。
- [言語設定]({{site.baseurl}}/user_guide/administer/personal/language_settings)で、ダッシュボードの優先言語を設定しましょう。