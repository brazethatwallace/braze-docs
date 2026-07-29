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
| サポートされている KakaoTalk パートナーのアカウント | KakaoTalk メッセージングチャネルを使用するには、サポートされている KakaoTalk パートナーである [CJ OliveNetworks](https://www.braze.com/partners/solutions-partners/cjolivenetworks/) または [Infobip](https://marketplace.braze.com/partners/infobip) のアカウントが必要です。 |
| KakaoTalk ビジネスチャネル | Braze を通じて KakaoTalk メッセージを送信するには、KakaoTalk アカウントが KakaoTalk ビジネスチャネルである必要があります。アカウントを作成すると、デフォルトのステータスはベーシックになります。アカウントをビジネスチャネルにするには、ビジネスの認証を行い、関連するドキュメントを提出する必要があります。 |
| KakaoTalk 送信者キー | 有効な KakaoTalk 送信者キーが必要です。 |
| 連絡先電話番号 | KakaoTalk チャネルの管理者の連絡先電話番号が必要です。 |
| Braze クラスター IP の許可リスト登録 | すべての顧客に IP 許可リストの登録が必要です。KakaoTalk を Braze に連携する前に、お使いのクラスターの Braze IP アドレスを登録してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

### Braze IP アドレスの登録 {#register-braze-ip-addresses}

Comm.One ダッシュボードで、お使いのクラスターの Braze IP アドレスを登録します。

1. Comm.One ダッシュボードで、**Account Management (계정 관리)** に移動し、メニューアイコンを選択してから、**View Details (자세히보기)** を選択します。
2. **Center & Upload IP Allowlist (센터&업로드 IP 화이트리스트)** を選択します。
3. お使いの Braze クラスターの IP アドレスを追加します。クラスター別の IP の完全なリストについては、[IP 許可リスト]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting)を参照してください。

![IP アドレスを追加できる場所を示す Comm.One ダッシュボード。]({% image_buster /assets/img/kakaotalk/register_braze_ip.png %})

### KakaoTalk アカウントの種類 {#types-of-kakaotalk-accounts}

| アカウントの種類 | 説明 |
| --- | --- |
| ベーシックチャネル | どの組織でも設定できる標準的な KakaoTalk チャネルです。KakaoTalk を通じたブロードキャストメッセージングと1対1チャットが可能です。 |
| [ビジネスチャネル](https://www.kakaocorp.com/page/service/service/KakaoTalkChannel) | 申請と認証プロセスが必要な、ビジネス認証済みのアップグレードされた KakaoTalk チャネルです。以下のような拡張機能を提供します。{::nomarkdown}<ul><li>認証バッジ</li><li>おすすめチャネルとしての表示</li><li>ビジネスメッセージングのサポート</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="KakaoTalk アカウントの種類" }

#### ビジネスチャネルの申請 {#apply-for-a-business-channel}

申請を開始する前に、以下のビジネス関連書類を準備してください。
- 韓国事業者登録証
- 事業代表者の身分証明書
- 在職証明書
- 業種別許認可証

{% alert important %}
KakaoTalk チャネルの情報（チャネル名、プロフィール画像など）は、公式に提出した書類の情報と正確に一致している必要があります。
{% endalert %}

書類を準備したら、以下のステップに従ってください。

1. [KakaoTalk Channel Admin Center](https://center-pf.kakao.com/) にログインします。
2. アップグレードしたい既存の KakaoTalk チャネルを選択します。
3. **Management (관리)** セクションで、**Business Channel Application (비즈니스 채널 신청)** のオプションを選択します。
4. **Apply** または **Request button (신청)** を選択してプロセスを開始します。
5. 必要な情報を入力します。
6. 審査結果の通知をお待ちください。

## KakaoTalkを連携する {#integrate-kakaotalk}

### ステップ1：KakaoTalkチャネルをBrazeに接続する {#step-1-connect-the-kakaotalk-channel-to-braze}

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

![Comm.Oneダッシュボードに表示されたマスク済みのログインID。]({% image_buster /assets/img/kakaotalk/comm.one_login_id.png %})

{% endtab %}
{% tab Sender Key (발신프로필 키) %}

![Comm.Oneダッシュボードに表示されたマスク済みのSender Key。]({% image_buster /assets/img/kakaotalk/sender_key.png %})

{% alert important %}
KakaoTalkのSender Keyは、一度に1つのワークスペースにのみ連携できます。同じSender Keyを別のワークスペースで使用するには、まず元のワークスペースでKakaoTalk購読グループをアーカイブしてから、[Brazeサポート]({{site.baseurl}}/braze_support)に連絡して連携を削除してもらう必要があります。Brazeが連携を削除した後、新しいワークスペースで連携を設定できます。
{% endalert %}

![Braze KakaoTalkチャネルの認証情報。]({% image_buster /assets/img/kakaotalk/cj_credentials.png %})

{% endtab %}
{% tab Channel name (카카오톡 채널 프로필명) %}

![Comm.Oneダッシュボードに表示されたマスク済みのチャネル名。]({% image_buster /assets/img/kakaotalk/channel_profile_name.png %})

{% endtab %}
{% tab Credential (ID) & Password (비밀번호) %}

![Comm.Oneダッシュボードに表示されたマスク済みの認証情報IDとパスワード。]({% image_buster /assets/img/kakaotalk/id_and_password.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
単一の共通IDにマッピングされたチャネルのみ登録できます。
{% endalert %}

![CJ OliveNetworksのテクノロジーパートナーページのフィールド。]({% image_buster /assets/img/kakaotalk/cj_olivenetworks.png %}){: style="max-width:30%;"}

#### Infobip

Infobipダッシュボードにアクセスし、以下の情報を収集します。

| フィールド | 場所 |
| --- | --- |
| **API Base URL** | **Developer Tools** > **API Keys**を選択します。 |
| **APIキー** | **Developer Tools** > **API Keys**を選択します。 |
| **Sender name / Sender key** | **Channels and Numbers** > **Channels**を選択し、**Senders**タブを選択します。 |
| **Sender profile UUID** | Infobipから直接提供されます。この情報がない場合は、Infobipにお問い合わせください。 |
| **Channel name** | Infobipから直接提供されます。この情報がない場合は、Infobipにお問い合わせください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Infobip" }

## ユーザープロファイルの設定 {#set-user-profiles}

ユーザープロファイルには、KakaoTalk を通じてメッセージを送信するために E.164 形式の電話番号が必要です。電話番号はユーザープロファイルに表示されます。KakaoTalk では電話番号が E.164 形式（例: `+821025749774`）である必要があります。これは、複数の形式の電話番号を受け入れる他のメッセージングチャネルとは異なります。

### 電話番号のインポート {#import-phone-numbers}

[CSV のアップロードまたは API の使用]({{site.baseurl}}/user_guide/data/unification/user_data/import_users)により電話番号をインポートしてユーザーを作成します。インポートする前に、電話番号が E.164 形式であることを確認してください。