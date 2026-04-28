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

> この記事では、ユーザーのセットアップ、ユーザーIDの照合、KakaoTalkテストユーザーの作成など、Brazeで[KakaoTalkメッセージングチャネル]({{site.baseurl}}/kakaotalk/)をセットアップする方法について説明します。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| --- | --- |
| サポートされているKakaoTalkパートナーのアカウント | KakaoTalkメッセージングチャネルを使用するには、サポートされているKakaoTalkパートナーである[CJ OliveNetworks](https://www.braze.com/partners/solutions-partners/cjolivenetworks/)またはInfobipのアカウントが必要です。 |
| KakaoTalkビジネスチャネル | BrazeからKakaoTalkメッセージを送信するには、KakaoTalkアカウントがKakaoTalkビジネスチャネルである必要があります。アカウントを作成すると、デフォルトのステータスはベーシックになります。アカウントをビジネスチャネルにするには、ビジネスの認証を行い、関連するドキュメントを提出する必要があります。 |
| KakaoTalk発信キー | 有効なKakaoTalk発信キーが必要です。 |
| 連絡先電話番号 | KakaoTalkチャネルの管理者の連絡先電話番号が必要です。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### KakaoTalkアカウントの種類 {#types-of-kakaotalk-accounts}

| アカウントの種類 | 説明 |
| --- | --- |
| ベーシックチャネル | どの組織でもセットアップできる標準的なKakaoTalkチャネルです。KakaoTalkを通じたブロードキャストメッセージングと1:1チャットが可能です。 |
| [ビジネスチャネル](https://www.kakaocorp.com/page/service/service/KakaoTalkChannel) | アップグレードされたビジネス認証済みのKakaoTalkチャネルで、申請と認証プロセスが必要です。以下のような拡張機能を提供します。{::nomarkdown}<ul><li>認証バッジ</li><li>おすすめチャネルとしての表示</li><li>ビジネスメッセージングのサポート</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### ビジネスチャネルの申請 {#apply-for-a-business-channel}

申請を開始する前に、以下のビジネスドキュメントを準備してください：
- 韓国事業者登録証
- 事業代表者の身分証明書
- 在職証明書
- 業種別許認可証

{% alert important %}
KakaoTalkチャネルの情報（チャネル名、プロフィール画像など）は、公式に提出したドキュメントの情報と正確に一致する必要があります。
{% endalert %}

ドキュメントを準備したら、以下のステップに従ってください：

1. [KakaoTalkチャネル管理センター](https://center-pf.kakao.com/)にログインします。
2. アップグレードしたい既存のKakaoTalkチャネルを選択します。
3. **Management（관리）**セクションで、**Business Channel Application（비즈니스 채널 신청）**のオプションを選択します。
4. **Apply**または**Request button（신청）**を選択してプロセスを開始します。
5. 必要な情報を入力します。
6. 審査結果の通知を待ちます。

## KakaoTalkの統合 {#integrate-kakaotalk}

### ステップ1: KakaoTalkチャネルをBrazeに接続する {#step-1-connect-the-kakaotalk-channel-to-braze}

1. **パートナー連携** > **テクノロジーパートナー**に移動し、KakaoTalkプロバイダーを選択します。
2. プロバイダーに必要な認証情報を収集し（以下を参照）、**テクノロジーパートナー**ページに入力して保存します。
3. 新しく保存した認証情報を使用して送信します。

#### CJ OliveNetworks

[Comm.Oneダッシュボード](https://ums.cjmplace.com/)にアクセスし、以下の情報を収集します。

| フィールド | 場所 |
| --- | --- |
| **Comm.One Login ID（로그인 아이디）** | プロファイルを選択します。 |
| **Sender Key（발신프로필 키）** | **Template Management（템플릿 관리）** > **Sender Profile Management（발신프로필 관리）**に移動します。 |
| **Channel name（카카오톡 채널 프로필명）** | Comm.Oneダッシュボードで、**Template Management（템플릿 관리）** > **Sender Profile Management（발신프로필 관리）**に移動します。 |
| **Sender number（연락처）** | {::nomarkdown}<ol><li><b>Account Management（계정 관리）</b>に移動し、メニューアイコンを選択してから<b>View Details（자세히보기）</b>を選択します。</li><li><b>Business Detailed Information（업체 상세 정보）</b> > <b>Company Information（기업정보）</b>に移動します。</li></ul>{:/} |
| **Credential（ID）& Password（비밀번호）** | **Sender number（사업자 등록번호）**と同じ場所に移動し、**API** > **Brand Message（브랜드 메시지）**に移動します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% tabs local %}
{% tab Comm.One Login ID (로그인 아이디) %}

![ログインIDがマスクされたComm.Oneダッシュボード。]({% image_buster /assets/img/kakaotalk/comm.one_login_id.png %})

{% endtab %}
{% tab Sender Key (발신프로필 키) %}

![発信キーがマスクされたComm.Oneダッシュボード。]({% image_buster /assets/img/kakaotalk/sender_key.png %})

{% endtab %}
{% tab Channel name (카카오톡 채널 프로필명) %}

![チャネル名がマスクされたComm.Oneダッシュボード。]({% image_buster /assets/img/kakaotalk/channel_profile_name.png %})

{% endtab %}
{% tab Credential (ID) & Password (비밀번호) %}

![認証情報IDとパスワードがマスクされたComm.Oneダッシュボード。]({% image_buster /assets/img/kakaotalk/id_and_password.png %})

{% endtab %}
{% endtabs %}

![CJ OliveNetworksのテクノロジーパートナーページのフィールド。]({% image_buster /assets/img/kakaotalk/cj_olivenetworks.png %}){: style="max-width:30%;"}

![Braze KakaoTalkチャネルの認証情報。]({% image_buster /assets/img/kakaotalk/cj_credentials.png %})

{% alert note %}
単一の共通IDにマッピングされたチャネルのみ登録できます。
{% endalert %}

#### Infobip

Infobipダッシュボードにアクセスし、以下の情報を収集します。

| フィールド | 場所 |
| --- | --- |
| **API Base URL** | **Developer Tools** > **API Keys**を選択します。 |
| **APIキー** | **Developer Tools** > **API Keys**を選択します。 |
| **Sender name / Sender key** | **Channels and Numbers** > **Channels**を選択し、**Senders**タブを選択します。 |
| **Sender profile UUID** | Infobipから直接提供されます。この情報がない場合は、Infobipにお問い合わせください。 |
| **Channel name** | Infobipから直接提供されます。この情報がない場合は、Infobipにお問い合わせください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユーザープロファイルの設定 {#set-user-profiles}

KakaoTalkでメッセージを送信するには、ユーザープロファイルに電話番号が必要です。電話番号はユーザープロファイルに表示され、提供された形式のまま表示されます。現在、SMSやWhatsAppとは異なり、KakaoTalkは標準の電話番号フィールドを使用します（E.164形式に変換された番号ではありません）。

![編集されていない形式の電話番号を持つテストユーザーのユーザープロファイル。]({% image_buster /assets/img/kakaotalk/standard_phone_number.png %}){: style="max-width:50%;"}

### 電話番号のインポート {#import-phone-numbers}

[CSVのアップロードまたはAPIの使用]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/)により電話番号をインポートしてユーザーを作成します。