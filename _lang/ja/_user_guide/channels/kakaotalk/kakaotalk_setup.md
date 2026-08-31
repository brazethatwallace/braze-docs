---
nav_title: KakaoTalkのセットアップ
article_title: KakaoTalkのセットアップ
description: "このリファレンス記事では、ユーザーのセットアップ、ユーザーIDの照合、テストユーザーの作成など、KakaoTalkチャネルのセットアップ方法について説明しています。"
page_order: 0
alias: /kakaotalk_setup/
channel:
  - KakaoTalk
---

# KakaoTalkのセットアップ {#set-up-kakaotalk}

> この記事では、ユーザーのセットアップ、ユーザーIDの照合、KakaoTalkテストユーザーの作成など、Brazeで[KakaoTalkメッセージングチャネル]({{site.baseurl}}/kakaotalk)をセットアップする方法について説明します。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| --- | --- |
| サポートされている KakaoTalk パートナーのアカウント | KakaoTalk メッセージングチャネルを使用するには、サポートされている KakaoTalk パートナー ([CJ OliveNetworks](https://www.braze.com/partners/solutions-partners/cjolivenetworks/) または [Infobip](https://marketplace.braze.com/partners/infobip)) のアカウントが必要です。 |
| KakaoTalk ビジネスチャネル | Braze を通じて KakaoTalk メッセージを送信するには、KakaoTalk アカウントが KakaoTalk ビジネスチャネルである必要があります。アカウントを作成すると、デフォルトのステータスはベーシックです。アカウントをビジネスチャネルにするには、ビジネスの認証を行い、関連するドキュメントを提出する必要があります。 |
| KakaoTalk 送信者キー | 有効な KakaoTalk 送信者キー。 |
| 連絡先電話番号 | KakaoTalk チャネル管理者の連絡先電話番号。 |
| Braze クラスター IP の許可リスト登録 | すべての顧客に IP 許可リストの登録が必要です。KakaoTalk を Braze に連携する前に、お使いのクラスターの Braze IP アドレスを登録してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

### Braze IP アドレスの登録 {#register-braze-ip-addresses}

お使いのクラスターの Braze IP アドレスを Comm.One ダッシュボードに登録します。

1. Comm.One ダッシュボードで、**Account Management (계정 관리)** に移動し、メニューアイコンを選択してから **View Details (자세히보기)** を選択します。
2. **Center & Upload IP Allowlist (센터&업로드 IP 화이트리스트)** を選択します。
3. Braze クラスターの IP アドレスを追加します。クラスター別の IP の完全なリストについては、[IP 許可リスト]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting)を参照してください。

![IP アドレスを追加できる場所を示す Comm.One ダッシュボード。]({% image_buster /assets/img/kakaotalk/register_braze_ip.png %})

### KakaoTalk アカウントの種類 {#types-of-kakaotalk-accounts}

| アカウントの種類 | 説明 |
| --- | --- |
| ベーシックチャネル | あらゆる組織が設定できる標準的な KakaoTalk チャネルです。KakaoTalk を通じたブロードキャストメッセージングと 1:1 チャットが可能です。 |
| [ビジネスチャネル](https://www.kakaocorp.com/page/service/service/KakaoTalkChannel) | アップグレードされた、ビジネス認証済みの KakaoTalk チャネルで、申請と認証プロセスが必要です。以下のような拡張機能を提供します。{::nomarkdown}<ul><li>認証バッジ</li><li>おすすめチャネルとしての表示</li><li>ビジネスメッセージングのサポート</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="KakaoTalk アカウントの種類" }

#### ビジネスチャネルの申請 {#apply-for-a-business-channel}

申請を開始する前に、以下のビジネスドキュメントを準備してください。
- 韓国事業者登録証明書
- 事業代表者の身分証明書
- 在職証明書
- 業種別ライセンス

{% alert important %}
KakaoTalk チャネルの情報（チャネル名、プロフィール画像など）は、提出した公式ドキュメントの情報と正確に一致する必要があります。
{% endalert %}

ドキュメントを準備したら、以下のステップに従います。

1. [KakaoTalk Channel Admin Center](https://center-pf.kakao.com/) にログインします。
2. アップグレードしたい既存の KakaoTalk チャネルを選択します。
3. **Management (관리)** セクションで、**Business Channel Application (비즈니스 채널 신청)** のオプションを選択します。
4. **Apply** または **Request button (신청)** を選択してプロセスを開始します。
5. 必要な情報を入力します。
6. 審査結果の通知をお待ちください。

## KakaoTalkを連携する {#integrate-kakaotalk}

### KakaoTalkチャネルをBrazeに接続する {#connect-the-kakaotalk-channel-to-braze}

1. **パートナー連携** > **テクノロジーパートナー**に移動し、KakaoTalkプロバイダーを選択します。
2. プロバイダーに必要な認証情報を収集し（次のセクションを参照）、**テクノロジーパートナー**ページに入力して保存します。
3. 新しく保存した認証情報を使用して送信します。

#### CJ OliveNetworks

[Comm.Oneダッシュボード](https://ums.cjmplace.com/)にアクセスし、以下の情報を収集します。

| フィールド | 場所 |
| --- | --- |
| **Comm.One Login ID (로그인 아이디)** | プロフィールを選択します。 |
| **Sender Key (발신프로필 키)** | **Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)**に移動します。 |
| **Channel name (카카오톡 채널 프로필명)** | Comm.Oneダッシュボードで、**Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)**に移動します。 |
| **Sender number (연락처)** | {::nomarkdown}<ol><li><b>Account Management (계정 관리)</b>に移動し、メニューアイコンを選択してから<b>View Details (자세히보기)</b>を選択します。</li><li><b>Business Detailed Information (업체 상세 정보)</b> > <b>Company Information (기업정보)</b>に移動します。</li></ul>{:/} |
| **Credential (ID) & Password (비밀번호)** | **Sender number (사업자 등록번호)**と同じ場所に移動し、**API** > **Brand Message (브랜드 메시지)**に移動します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="CJ OliveNetworks" }

{% tabs local %}
{% tab Comm.One Login ID (로그인 아이디) %}

![マスクされたログインIDが表示されたComm.Oneダッシュボード。]({% image_buster /assets/img/kakaotalk/comm.one_login_id.png %})

{% endtab %}
{% tab Sender Key (발신프로필 키) %}

![マスクされたSender Keyが表示されたComm.Oneダッシュボード。]({% image_buster /assets/img/kakaotalk/sender_key.png %})

{% alert important %}
KakaoTalkのSender Keyは、一度に1つのワークスペースにのみ連携できます。同じSender Keyを別のワークスペースで使用するには、まず元のワークスペースでKakaoTalk購読グループをアーカイブしてから、[Brazeサポート]({{site.baseurl}}/braze_support)に連絡して連携を解除してもらう必要があります。Brazeが連携を解除した後、新しいワークスペースで連携を設定できます。
{% endalert %}

![Braze KakaoTalkチャネルの認証情報。]({% image_buster /assets/img/kakaotalk/cj_credentials.png %})

{% endtab %}
{% tab Channel name (카카오톡 채널 프로필명) %}

![マスクされたチャネル名が表示されたComm.Oneダッシュボード。]({% image_buster /assets/img/kakaotalk/channel_profile_name.png %})

{% endtab %}
{% tab Credential (ID) & Password (비밀번호) %}

![マスクされた認証情報IDとパスワードが表示されたComm.Oneダッシュボード。]({% image_buster /assets/img/kakaotalk/id_and_password.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
単一の共通IDにマッピングされたチャネルのみ登録できます。
{% endalert %}

![CJ OliveNetworks用のテクノロジーパートナーページのフィールド。]({% image_buster /assets/img/kakaotalk/cj_olivenetworks.png %}){: style="max-width:30%;"}

#### Infobip

Infobipダッシュボードと[KakaoTalk Channel Admin Center](https://center-pf.kakao.com/)にアクセスし、以下の情報を収集します。

| フィールド | 場所 |
| --- | --- |
| **API Base URL** | Infobipポータルで、**Developer Tools** > **API Keys**に移動します。 |
| **API キー** | Infobipポータルで、**Developer Tools** > **API Keys**に移動します。 |
| **Sender name / Sender key** | Infobipポータルで、**Channels and Numbers** > **Channels**に移動し、**Senders**タブを選択します。 |
| **Sender profile UUID** | KakaoTalk Channel Admin Centerで、**Channels**に移動し、チャネル情報ウィンドウで**Search ID**を見つけます。 |
| **Channel name** | KakaoTalk Channel Admin Centerで、同じチャネル情報ウィンドウで**チャネル名**を見つけます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Infobip" }

##### APIキーとベースURL {#api-key-and-base-url}

1. Infobipポータルで、**Developer Tools** > **API Keys**を選択します。
2. **API keys**ページで、**API base URL**をコピーします。

![APIベースURLが表示されたInfobip API Keysページ。]({% image_buster /assets/img/kakaotalk/infobip_api_keys_page.png %})

{: start="3"}
3. **CREATE API KEY**を選択します。
4. **Name**を入力し、**Expiration date**を選択してから、KakaoTalkに必要なAPIスコープを選択します。これらのスコープは、キーが実行できるInfobip APIアクションを制御します。

![名前、有効期限、APIスコープのフィールドが表示されたInfobip Create API Keyページ。]({% image_buster /assets/img/kakaotalk/infobip_api_key_scopes.png %})

{: start="5"}
5. **CREATE**を選択してキーを生成します。
6. 生成されたキーをコピーします。このページに戻って、名前、有効期限、またはAPIスコープを更新できます。

##### Sender profile UUIDとチャネル名 {#sender-profile-uuid-and-channel-name}

1. [KakaoTalk Channel Admin Center](https://center-pf.kakao.com/)で、**Channels**を選択します。
2. **Channel Information**ウィンドウで、**Channel name**と**Search id**（sender UUID）を見つけます。
3. **Customer center contact information**を入力します。これは広告メッセージを送信する際に必要です。

![顧客センターの連絡先情報フィールドが表示されたKakaoTalkチャネル情報ウィンドウ。]({% image_buster /assets/img/kakaotalk/kakao_customer_center_contact.png %})

{: start="4"}
4. 別のチャネルを表示するには、メニュー上部のチャネルアイコンを選択します。
5. **My channel**リストで、表示したいチャネルを選択し、前のステップを繰り返します。

## ユーザープロファイルの設定 {#set-user-profiles}

ユーザープロファイルには、KakaoTalkを通じてメッセージを送信するためにE.164形式の電話番号が必要です。電話番号はユーザープロファイルに表示されます。KakaoTalkでは、電話番号がE.164形式（例: `+821025749774`）である必要があります。これは、複数の形式の電話番号を受け入れる他のメッセージングチャネルとは異なります。

### 電話番号のインポート {#import-phone-numbers}

[CSVをアップロードするかAPIを使用]({{site.baseurl}}/user_guide/audience/manage_audience/import_users)して、ユーザーを作成することで電話番号をインポートします。インポートする前に、電話番号がE.164形式であることを確認してください。