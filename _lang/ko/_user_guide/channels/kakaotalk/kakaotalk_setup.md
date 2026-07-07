---
nav_title: KakaoTalk 설정
article_title: KakaoTalk 설정
description: "이 참조 문서에서는 사용자 설정, 사용자 ID 조정, 테스트 사용자 생성 등 KakaoTalk 채널을 설정하는 방법을 설명합니다."
page_order: 0
alias: /kakaotalk_setup/
channel:
  - KakaoTalk
---

# KakaoTalk 설정 {#set-up-kakaotalk}

> 이 문서에서는 사용자 설정, 사용자 ID 조정, KakaoTalk 테스트 사용자 생성 등 Braze에서 [KakaoTalk 메시징 채널]({{site.baseurl}}/kakaotalk)을 설정하는 방법을 다룹니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| 지원되는 KakaoTalk 파트너 계정 | KakaoTalk 메시징 채널을 사용하려면 지원되는 KakaoTalk 파트너인 [CJ OliveNetworks](https://www.braze.com/partners/solutions-partners/cjolivenetworks/) 또는 Infobip의 계정이 필요합니다. |
| KakaoTalk 비즈니스 채널 | Braze를 통해 KakaoTalk 메시지를 발송하려면 KakaoTalk 계정이 KakaoTalk 비즈니스 채널이어야 합니다. 계정을 생성하면 기본 상태는 일반입니다. 비즈니스 채널로 전환하려면 사업자 인증을 완료하고 관련 서류를 제출해야 합니다. |
| KakaoTalk 발신프로필 키 | 유효한 KakaoTalk 발신프로필 키가 필요합니다. |
| 연락처 전화번호 | KakaoTalk 채널 관리자의 연락처 전화번호가 필요합니다. |
| Braze 클러스터 IP 허용 목록 등록 | 모든 고객에게 IP 허용 목록 등록이 필요합니다. Braze에서 KakaoTalk을 통합하기 전에 클러스터에 해당하는 Braze IP 주소를 등록하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

### Braze IP 주소 등록 {#register-braze-ip-addresses}

Comm.One 대시보드에서 클러스터에 해당하는 Braze IP 주소를 등록합니다.

1. Comm.One 대시보드에서 **Account Management (계정 관리)**로 이동하여 메뉴 아이콘을 선택한 후 **View Details (자세히보기)**를 선택합니다.
2. **Center & Upload IP Allowlist (센터&업로드 IP 화이트리스트)**를 선택합니다.
3. Braze 클러스터에 해당하는 IP 주소를 추가합니다. 클러스터별 전체 IP 목록은 [IP 허용 목록]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting)을 참조하세요.

![IP 주소를 추가할 수 있는 위치를 보여주는 Comm.One 대시보드.]({% image_buster /assets/img/kakaotalk/register_braze_ip.png %})

### KakaoTalk 계정 유형 {#types-of-kakaotalk-accounts}

| 계정 유형 | 설명 |
| --- | --- |
| 일반 채널 | 모든 조직이 설정할 수 있는 표준 KakaoTalk 채널입니다. KakaoTalk을 통한 대량 메시지 발송 및 1:1 채팅이 가능합니다. |
| [비즈니스 채널](https://www.kakaocorp.com/page/service/service/KakaoTalkChannel) | 신청 및 인증 절차가 필요한 사업자 인증 KakaoTalk 채널입니다. 다음과 같은 향상된 기능을 제공합니다. {::nomarkdown}<ul><li>인증 배지</li><li>추천 채널로 노출</li><li>비즈니스 메시징 지원</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="KakaoTalk 계정 유형" }

#### 비즈니스 채널 신청 {#apply-for-a-business-channel}

신청을 시작하기 전에 다음 사업자 서류를 준비하세요:
- 사업자등록증
- 대표자 신분증
- 재직증명서
- 업종별 인허가증

{% alert important %}
KakaoTalk 채널 정보(채널명, 프로필 이미지 등)는 공식 제출 서류의 정보와 정확히 일치해야 합니다.
{% endalert %}

서류를 준비한 후 다음 단계를 따르세요:

1. [카카오톡 채널 관리자센터](https://center-pf.kakao.com/)에 로그인합니다.
2. 업그레이드하려는 기존 KakaoTalk 채널을 선택합니다.
3. **Management (관리)** 섹션에서 **Business Channel Application (비즈니스 채널 신청)** 옵션을 선택합니다.
4. **Apply** 또는 **Request button (신청)**을 선택하여 절차를 시작합니다.
5. 필요한 정보를 입력합니다.
6. 심사 결과 알림을 기다립니다.

## KakaoTalk 통합 {#integrate-kakaotalk}

### 1단계: KakaoTalk 채널을 Braze에 연결 {#step-1-connect-the-kakaotalk-channel-to-braze}

1. **Partner Integrations** > **Technology Partners**로 이동하여 KakaoTalk 제공업체를 선택합니다.
2. 제공업체에 필요한 자격 증명을 수집한 후(아래 참조) **Technology Partners** 페이지에 입력하고 저장합니다.
3. 새로 저장한 자격 증명을 사용하여 발송합니다.

#### CJ OliveNetworks

[Comm.One 대시보드](https://ums.cjmplace.com/)로 이동하여 다음 정보를 수집합니다.

| 필드 | 위치 |
| --- | --- |
| **Comm.One Login ID (로그인 아이디)** | 프로필을 선택합니다. |
| **Sender Key (발신프로필 키)** | **Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)**로 이동합니다. |
| **Channel name (카카오톡 채널 프로필명)** | Comm.One 대시보드에서 **Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)**로 이동합니다. |
| **Sender number (연락처)** | {::nomarkdown}<ol><li><b>Account Management (계정 관리)</b>로 이동하여 메뉴 아이콘을 선택한 후 <b>View Details (자세히보기)</b>를 선택합니다.</li><li><b>Business Detailed Information (업체 상세 정보)</b> > <b>Company Information (기업정보)</b>로 이동합니다.</li></ol>{:/} |
| **Credential (ID) & Password (비밀번호)** | **Sender number (사업자 등록번호)**와 동일한 위치로 이동한 후 **API** > **Brand Message (브랜드 메시지)**로 이동합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="CJ OliveNetworks" }

{% tabs local %}
{% tab Comm.One Login ID (로그인 아이디) %}

![마스킹 처리된 로그인 ID가 표시된 Comm.One 대시보드.]({% image_buster /assets/img/kakaotalk/comm.one_login_id.png %})

{% endtab %}
{% tab Sender Key (발신프로필 키) %}

![마스킹 처리된 발신프로필 키가 표시된 Comm.One 대시보드.]({% image_buster /assets/img/kakaotalk/sender_key.png %})

{% alert important %}
KakaoTalk 발신프로필 키는 한 번에 하나의 워크스페이스에만 통합할 수 있습니다. 동일한 발신프로필 키를 다른 워크스페이스에서 사용하려면 먼저 기존 워크스페이스에서 KakaoTalk 구독 그룹을 아카이브한 후 [Braze 고객지원]({{site.baseurl}}/braze_support)에 연락하여 통합을 제거해야 합니다. Braze에서 통합을 제거한 후 새 워크스페이스에서 통합을 설정할 수 있습니다.
{% endalert %}

![Braze KakaoTalk 채널의 자격 증명.]({% image_buster /assets/img/kakaotalk/cj_credentials.png %})

{% endtab %}
{% tab Channel name (카카오톡 채널 프로필명) %}

![마스킹 처리된 채널명이 표시된 Comm.One 대시보드.]({% image_buster /assets/img/kakaotalk/channel_profile_name.png %})

{% endtab %}
{% tab Credential (ID) & Password (비밀번호) %}

![마스킹 처리된 자격 증명 ID와 비밀번호가 표시된 Comm.One 대시보드.]({% image_buster /assets/img/kakaotalk/id_and_password.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
하나의 공통 ID에 매핑된 채널만 등록할 수 있습니다.
{% endalert %}

![CJ OliveNetworks의 Technology Partners 페이지 필드.]({% image_buster /assets/img/kakaotalk/cj_olivenetworks.png %}){: style="max-width:30%;"}

#### Infobip

Infobip 대시보드로 이동하여 다음 정보를 수집합니다.

| 필드 | 위치 |
| --- | --- |
| **API Base URL** | **Developer Tools** > **API Keys**를 선택합니다. |
| **API 키** | **Developer Tools** > **API Keys**를 선택합니다. |
| **Sender name / Sender key** | **Channels and Numbers** > **Channels**를 선택한 후 **Senders** 탭을 선택합니다. |
| **Sender profile UUID** | Infobip에서 직접 제공합니다. 이 정보가 없는 경우 Infobip에 문의하세요. |
| **Channel name** | Infobip에서 직접 제공합니다. 이 정보가 없는 경우 Infobip에 문의하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Infobip" }

## 고객 프로필 설정 {#set-user-profiles}

KakaoTalk을 통해 메시지를 보내려면 고객 프로필에 E.164 형식의 전화번호가 있어야 합니다. 전화번호는 고객 프로필에 표시됩니다. KakaoTalk은 전화번호가 E.164 형식이어야 합니다(예: `+821025749774`). 이는 여러 형식의 전화번호를 허용하는 다른 메시징 채널과 다릅니다.

### 전화번호 가져오기 {#import-phone-numbers}

[CSV 업로드 또는 API를 사용]({{site.baseurl}}/user_guide/data/unification/user_data/import_users)하여 전화번호를 가져오고 사용자를 생성합니다. 가져오기 전에 전화번호가 E.164 형식인지 확인하세요.