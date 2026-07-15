---
nav_title: 전달 가능성 센터
article_title: 전달 가능성 센터
alias: "/deliverability_center/"
page_order: 4
description: "이 참조 문서에서는 마케터가 이메일 발송 도메인 및 IP 평판을 확인하고 이메일 전달 가능성을 파악할 수 있는 기능인 전달 가능성 센터를 설정하는 방법을 다룹니다."
channel:
  - email

---

# 전달 가능성 센터 {#deliverability-center}

> 전달 가능성 센터는 [Gmail Postmaster Tools](https://www.gmail.com/postmaster/)를 활용하여 발송된 이메일에 대한 데이터를 추적하고 발송 도메인에 대한 데이터를 수집함으로써 이메일 성능에 대한 더 깊은 인사이트를 제공합니다.

이메일 전달 가능성은 Campaign 성공의 핵심입니다. Braze 대시보드의 전달 가능성 센터를 사용하면 **IP Reputation** 또는 **Delivery Errors**별로 도메인을 확인하여 이메일 전달 가능성과 관련된 잠재적 문제를 발견하고 해결할 수 있습니다.

전달 가능성 센터에 접근하려면 워크스페이스에 대해 아래 드롭다운에 나열된 [사용자 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)이 필요합니다.

{% details 전달 가능성 센터에 필요한 사용자 권한 %}

- Campaigns 보기
- Campaigns 편집
- Campaigns 아카이브
- Canvases 보기
- Canvases 편집
- Canvases 아카이브
- 최대 게재빈도 설정 규칙 보기
- 최대 게재빈도 설정 규칙 편집
- 메시지 우선순위 보기
- 메시지 우선순위 편집
- Content Blocks 보기
- 기능 플래그 보기
- 기능 플래그 편집
- 기능 플래그 아카이브
- Segments 보기
- Segments 편집
- IAM 템플릿 보기
- IAM 템플릿 편집
- IAM 템플릿 아카이브
- 이메일 템플릿 보기
- 이메일 템플릿 편집
- 이메일 템플릿 아카이브
- 웹훅 템플릿 보기
- 웹훅 템플릿 편집
- 웹훅 템플릿 아카이브
- 이메일 링크 템플릿 보기
- 이메일 링크 템플릿 편집
- 미디어 라이브러리 자산 보기
- 미디어 라이브러리 자산 편집
- 미디어 라이브러리 자산 삭제
- 위치 보기
- 위치 편집
- 위치 아카이브
- 프로모션 코드 보기
- 프로모션 코드 편집
- 프로모션 코드 내보내기
- 환경설정 센터 보기
- 환경설정 센터 편집
- 보고서 보기
- 보고서 편집
- 사용 데이터 보기

{% enddetails %}

## Google Postmaster 계정 설정 {#set-up-your-google-postmaster-account}

전달 가능성 센터에 연결하기 전에 Google Postmaster Tools 계정을 설정해야 합니다. 업무용 또는 개인 Gmail 계정을 사용하여 Google Postmaster를 설정할 수 있습니다.

1. [Google Postmaster Tools 대시보드](https://postmaster.google.com/managedomains?pli=1)로 이동합니다.
2. 페이지 하단에서 <i class="fas fa-plus-circle"></i> **도메인 추가**를 선택합니다.
3. 이메일을 인증할 루트(상위) 도메인을 입력합니다. TXT 레코드가 Braze를 통해 사용하는 하위 도메인이 **아닌** 이 루트(상위) 도메인에 연결되어 있는지 확인하세요. 루트(상위) 도메인을 인증하면 나중에 추가 TXT 레코드를 생성하지 않고도 Postmaster Tools에 하위 도메인을 추가할 수 있습니다. 예를 들어, `braze.com`을 인증하면 나중에 Postmaster Tools에서 `demo.braze.com`을 별도의 하위 도메인으로 추가하여 하위 도메인 수준의 측정기준을 확인할 수 있습니다.
4. Google에서 도메인의 DNS에 직접 추가할 수 있는 TXT 레코드를 생성합니다. 이는 일반적으로 DNS를 관리하는 담당자가 소유합니다. 특정 DNS를 업데이트하는 방법에 대한 정보와 안내는 [도메인 인증(호스트별 단계)](https://support.google.com/a/topic/1409901)을 참조하세요.
5. **Next**를 선택합니다. <br>![이메일을 인증하기 위한 예시 도메인 "demo.braze.com".]({% image_buster /assets/img_archive/domain_authentication.png %})
6. TXT 레코드가 DNS에 추가된 후 Google Postmaster Tools 대시보드로 돌아가서 **Verify**를 선택합니다. 이 단계에서 도메인 소유권을 확인하여 Postmaster 계정에서 Gmail 전달 가능성 측정기준에 접근할 수 있습니다. <br>![도메인 "demo.braze.com"의 소유권을 인증하라는 프롬프트.]({% image_buster /assets/img_archive/domain_verification.png %})
7. 루트(상위) 도메인을 인증한 후 발송 하위 도메인을 Google Postmaster에 추가합니다.

{% alert note %}
하위 도메인이 Google Postmaster의 전달 가능성 센터에 표시되지 않는 경우, 루트(상위) 도메인만 Google Postmaster에 추가한 결과일 수 있습니다. Google Postmaster에서 루트 도메인이 인증된 후 하위 도메인을 추가하면 자동으로 인증됩니다. 이 프로세스를 통해 Google이 하위 도메인 수준의 측정기준을 보고할 수 있으며, 이 데이터는 Braze 전달 가능성 센터로 가져올 수 있습니다.
{% endalert %}

## Google Postmaster 통합 {#integrating-google-postmaster}

{% alert important %}
**Google Postmaster Tools v2 마이그레이션**<br>
Google은 기존 Postmaster Tools(v1)를 지원 중단하고 최신 사용자 인터페이스와 새로운 대시보드(Gmail의 발신자 가이드라인 준수를 모니터링하는 데 도움이 되는 규정 준수 대시보드 포함)를 갖춘 차세대 버전(v2)을 출시했습니다. 모든 사용자는 2026년 10월 31일까지 v2로 마이그레이션해야 합니다.<br><br>
Google Postmaster Tool 연결을 재승인하려면 **파트너 통합** > **기술 파트너**로 이동하여 **Google Postmaster**를 열고 **Change Account**를 선택하여 새로운 v2 권한으로 재인증합니다. 완료되면 v2로 업그레이드되어 새로운 대시보드와 데이터에 접근할 수 있습니다.<br><br>
자세한 내용은 [새로운 Postmaster Tools에 대한 Google의 공지](https://support.google.com/mail/answer/16594218?hl=en)를 참조하세요.
{% endalert %}

전달 가능성 센터를 설정하기 전에 도메인이 [Gmail Postmaster Tools에 추가](https://support.google.com/mail/answer/9981691?hl=en)되었는지 확인하세요.

다음 단계에 따라 Google Postmaster와 통합하고 전달 가능성 센터를 설정합니다:

1. **Analytics** > **Email Performance**로 이동합니다.
2. **Deliverability Center** 탭을 선택합니다. <br>![Google Postmaster가 연결되지 않은 전달 가능성 센터.]({% image_buster /assets/img_archive/deliverability_center1.png %})
3. **Connect with Google Postmaster**를 선택합니다.
4. Google 계정을 선택한 다음 **Allow**를 선택하여 Braze가 Postmaster Tools에 등록된 도메인의 이메일 트래픽 측정기준을 볼 수 있도록 허용합니다.

인증된 도메인이 전달 가능성 센터에 표시됩니다.

![중간 및 낮은 평판을 가진 Google Postmaster의 두 개의 인증된 도메인.]({% image_buster /assets/img_archive/deliverability_center2.png %})

Braze 대시보드에서 **파트너 통합** > **기술 파트너** > **Google Postmaster**로 이동하여 Google Postmaster에 접근할 수도 있습니다. 통합 후 Braze는 최근 30일간의 평판 및 오류 데이터를 가져옵니다. 데이터가 즉시 사용 가능하지 않을 수 있으며 채워지는 데 몇 분이 걸릴 수 있습니다.

### 유효하지 않거나 만료된 승인 {#invalid-or-expired-authorization}

Google Postmaster Tools 승인 자격 증명이 유효하지 않다는 알림을 받더라도 Braze에서의 이메일 발송에는 영향이 **없습니다**. Braze와 Google Postmaster 간의 연결만 끊어지며, 다시 연결할 때까지 Gmail 평판 및 오류 데이터가 전달 가능성 센터에 동기화되지 않습니다.

통합을 복원하려면 **파트너 통합** > **기술 파트너**로 이동하여 **Google Postmaster**를 열고 **Disconnect**를 선택한 다음 연결 흐름을 다시 진행합니다([Google Postmaster 통합](#integrating-google-postmaster)과 동일한 단계).

### 측정기준 및 정의 {#metrics-and-definitions}

다음 측정기준 및 정의는 Google Postmaster Tools에 적용됩니다.

#### IP 평판 {#ip-reputation}

IP 평판 등급을 이해하려면 다음 표를 참조하세요:

| 평판 등급 | 정의 |
| ----- | ---------- |
| 높음 | 낮은 스팸 신고율(예: 사용자가 "스팸" 버튼을 클릭하는 경우)을 유지한 좋은 실적이 있습니다. |
| 중간/보통 | 긍정적인 참여를 생성하는 것으로 알려져 있지만 가끔 스팸 신고를 받습니다. 이 도메인에서 보낸 대부분의 이메일은 받은편지함으로 전달되지만, 스팸 신고가 증가하면 예외가 될 수 있습니다. |
| 낮음 | 정기적으로 높은 스팸 신고율을 받는 것으로 알려져 있습니다. 이 발신자의 이메일은 스팸 폴더로 필터링될 가능성이 높습니다. |
| 나쁨 | 높은 스팸 신고율을 받은 이력이 있습니다. 이 도메인의 이메일은 거의 항상 연결 시 거부되거나 스팸 폴더로 필터링됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="IP 평판" }

#### 도메인 평판 {#domain-reputation}

다음 표를 사용하여 도메인 평판 등급을 모니터링하고 이해하여 스팸 폴더로 필터링되는 것을 방지하세요.

| 평판 등급 | 정의 |
| ----- | ---------- |
| 높음 | 매우 낮은 스팸 신고율을 유지한 좋은 실적이 있습니다. Gmail의 발신자 가이드라인을 준수합니다. 이메일이 스팸 폴더로 필터링되는 경우가 거의 없습니다. 매우 낮은 스팸 비율을 유지한 좋은 실적이 있습니다. [Gmail의 발신자 가이드라인](https://developers.google.com/gmail/markup/registering-with-google)을 준수합니다. |
| 중간/보통 | 긍정적인 참여를 생성하는 것으로 알려져 있지만 가끔 소량의 스팸 신고를 받은 적이 있습니다. 이 도메인에서 보낸 대부분의 이메일은 받은편지함에 도달합니다(스팸 수준이 눈에 띄게 증가하는 경우 제외). |
| 낮음 | 정기적으로 스팸 신고를 받는 것으로 알려져 있습니다. 이 발신자의 이메일은 스팸 폴더로 필터링될 가능성이 높습니다. |
| 나쁨 | 높은 스팸 신고율을 받은 이력이 있습니다. 이 도메인의 이메일은 거의 항상 연결 시 거부되거나 스팸 폴더로 필터링됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="도메인 평판" }

#### 인증 {#authentication}

인증 대시보드를 사용하여 Sender Policy Framework(SPF), DomainKeys Identified Mail(DKIM), Domain-based Message Authentication, Reporting and Conformance(DMARC)를 통과한 이메일의 비율을 검토할 수 있습니다.

| 그래프 유형 | 정의 |
| ----- | ---------- |
| SPF | SPF를 시도한 도메인의 모든 이메일 중 SPF를 통과한 이메일의 비율을 표시합니다. 스푸핑된 메일은 제외됩니다. |
| DKIM | DKIM을 시도한 도메인의 모든 이메일 중 DKIM을 통과한 이메일의 비율을 표시합니다. |
| DMARC | SPF 또는 DKIM을 통과한 도메인에서 수신된 모든 이메일 중 DMARC 정렬을 통과한 이메일의 비율을 표시합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="인증" }

#### 암호화 {#encryption}

이 표를 참조하여 인바운드 및 아웃바운드 트래픽 중 암호화된 비율을 파악하세요.

| 용어 | 정의 |
| ----- | ---------- |
| TLS 인바운드 | 해당 도메인에서 수신된 모든 메일 중 TLS를 통과한 수신 메일(Gmail로)의 비율을 표시합니다. |
| TLS 아웃바운드 | 해당 도메인으로 발송된 모든 메일 중 TLS를 통해 수락된 발신 메일(Gmail에서)의 비율을 표시합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="암호화" }

전달 가능성을 개선하는 더 많은 아이디어는 [전달 가능성 함정 및 스팸 트랩]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps)을 참조하세요. 이메일 Campaign을 발송하기 전에 확인해야 할 사항은 [이메일 모범 사례]({{site.baseurl}}/user_guide/channels/email/best_practices)를 참조하세요.

## Microsoft Smart Network Data Services(SNDS) 설정 {#set-up-microsoft-smart-network-data-services-snds}

Microsoft가 주요 메일박스 제공업체인 경우 전달 가능성 센터에서 Microsoft SNDS 데이터를 확인할 수 있습니다. 여기에는 Amazon SES, SendGrid 또는 SparkPost를 사용하는 워크스페이스의 전용 발송 IP가 포함됩니다. 이 데이터를 사용하여 IP 상태를 모니터링하고 Microsoft 받은편지함 제공업체가 발송을 어떻게 평가하는지 파악할 수 있습니다.

Microsoft SNDS는 Outlook, Hotmail, Live 등 Microsoft 받은편지함 제공업체가 보고하는 스팸 신고, 스팸 트랩 히트 및 발송량에 대한 IP 수준 데이터를 제공합니다.

{% alert important %}
전달 가능성 센터에 데이터가 표시되지 않는 경우 IP 주소 목록과 함께 [고객지원]({{site.baseurl}}/user_guide/administer/personal/braze_support)에 문의하세요.
{% endalert %}

### Amazon SES

Amazon SES를 통해 이메일을 발송하는 워크스페이스의 경우, 전달 가능성 센터에 전용 발송 IP에 대한 Microsoft SNDS 측정기준이 표시됩니다. Braze는 이 기능이 워크스페이스에서 활성화되면 최대 90일간의 과거 SNDS 데이터를 백필합니다.

{% alert note %}
Amazon SES는 **Trap message period start** 또는 **Trap message period end** 측정기준을 제공하지 않습니다. SES 발송 IP의 경우 해당 열은 Microsoft SNDS 표에서 숨겨집니다. 해당 IP에 대한 스팸 트랩 히트를 포함한 다른 SNDS 측정기준은 계속 확인할 수 있습니다.
{% endalert %}

![샘플 IP, 수신자, RCPT 명령, 데이터 명령, 필터 결과, 불만 비율, 트랩 메시지 기간 시작 및 종료, 스팸 트랩 히트를 포함한 Microsoft SNDS 결과 예시.]({% image_buster /assets/img_archive/deliverability_center_msnds.png %})

### 측정기준 및 정의

다음 측정기준은 Microsoft SNDS에 적용됩니다.

#### 수신자 {#recipients}

이 측정기준은 해당 IP에서 전송된 메시지의 수신자 수를 나타냅니다.

#### DATA 명령 {#data-commands}

이 측정기준은 해당 IP에서 보낸 DATA 명령의 수를 추적합니다. DATA 명령은 메일을 보내는 데 사용되는 SMTP 프로토콜의 일부입니다.

#### 필터 결과 {#filter-results}

필터 결과를 이해하려면 다음 표를 참조하세요.

| 결과 | 정의 |
| ----- | ---------- |
| 녹색 | 주어진 기간의 최대 10%까지 Microsoft의 스팸 필터에 의해 스팸으로 판정되었습니다. |
| 노란색 | 주어진 기간의 10%에서 90% 사이에서 Microsoft의 스팸 필터에 의해 스팸으로 판정되었습니다. |
| 빨간색 | 주어진 기간의 90% 이상에서 Microsoft의 스팸 필터에 의해 스팸으로 판정되었습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필터 결과" }

#### 불만 비율 {#complaint-rate}

활동 기간 동안 해당 IP에서 수신된 메시지에 대해 Hotmail 또는 Windows Live 사용자가 불만을 제기한 비율입니다. 사용자는 웹 사용자 인터페이스를 통해 거의 모든 메시지를 정크로 신고할 수 있습니다.

불만 비율을 계산하려면 불만 수를 메시지 수신자 수로 나눕니다.

| 결과 | 정의 |
| ----- | ---------- |
| 0.3% 미만 | 이상적인 불만 비율입니다. |
| 0.3% 초과 | 가입 프로세스를 검토하고 탈퇴 링크가 작동하는지 확인하세요. 또한 메일이 오디언스에 맞게 더 잘 개인화될 수 있는지 고려하세요. |
| 100% 초과 | SNDS는 불만이 신고된 날짜를 기준으로 불만을 표시하며, 불만 대상 메일이 전달된 날짜를 소급하여 표시하지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="불만 비율" }

#### 스팸 트랩 히트 {#spam-trap-hits}

스팸 트랩 히트는 "트랩 계정"으로 전송된 메시지 수입니다. 트랩 계정은 Outlook.com에서 유지 관리하는 계정으로 어떤 메일도 요청하지 않습니다. 이러한 트랩 계정으로 전송된 메시지는 스팸으로 간주될 가능성이 높으므로 이 측정기준을 모니터링하여 낮게 유지하는 것이 중요합니다. 스팸 트랩 히트가 낮다는 것은 메시지가 이러한 계정으로 전송되지 않고 실제 계정으로 전송되고 있음을 의미합니다.

#### 트랩 메시지 기간 시작 및 종료 {#trap-message-period-start-and-end}

이 열은 활동 기간 동안 해당 IP에서 트랩 계정으로 전송된 첫 번째 및 마지막 메시지가 수신된 시점을 표시합니다. Amazon SES는 이러한 측정기준을 제공하지 않으므로 Microsoft SNDS 표에서 SES 발송 IP만 확인할 때 해당 열은 숨겨집니다.

{% alert tip %}
Braze에서 인증된 도메인 중 하나와 관련된 기록을 찾고 있다면, 전달 가능성 센터는 Google Postmaster 또는 Microsoft SNDS의 데이터를 나열하므로 해당 플랫폼에 Braze와 공유할 데이터가 없을 수 있습니다. 또는 일관된 이메일 전달을 유지하면 더 높은 평판으로 이어질 수 있습니다.
{% endalert %}