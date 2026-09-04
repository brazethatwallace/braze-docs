---
nav_title: 이메일 전달 가능성 용어집
article_title: 이메일 전달 가능성 용어집
layout: glossary_page
glossary_top_header: "이메일 전달 가능성 용어집"
glossary_top_text: "이 용어집은 Braze를 통해 이메일을 발송할 때 접할 수 있는 일반적인 이메일 전달 가능성 및 이메일 인프라 용어를 정의합니다."
page_order: 1
page_type: glossary
description: "이 용어집은 Braze를 통해 이메일을 발송할 때 접할 수 있는 일반적인 이메일 전달 가능성 및 이메일 인프라 용어를 정의합니다."
channel:
  - email

glossaries:
  - name: Allowlist
    description: 사용자가 이메일 수신을 허용하며 휴지통이나 스팸 폴더로 필터링되거나 보내지지 않아야 한다고 판단한 연락처 목록입니다.
  - name: Block
    description: 차단 반송은 메일함 공급자가 이메일 전달을 수락하지 않은 결과입니다. 많은 메일함 공급자는 스팸이나 바이러스를 발송하는 것으로 보고된 IP 주소 또는 도메인, 또는 이메일 정책이나 스팸 필터를 위반하는 콘텐츠가 포함된 이메일을 차단합니다. SendGrid는 일반적으로 소프트 반송이라고 불리는 것을 "차단"이라고 합니다. SendGrid에서 차단은 기술적 또는 일시적인 이유로 이메일 전달이 수락되지 않을 때 발생합니다.
  - name: Blocklist
    description: 알려진 스팸 발송원으로 보고되고 등록된 IP 주소 목록입니다. 공개 및 비공개 차단 목록이 있습니다. 공개 차단 목록은 게시되어 대중에게 제공되며, 무료 서비스인 경우가 많고 때로는 유료입니다.
  - name: Bounce
    description: 하드 반송이라고도 하며, 반송된 주소는 영구적으로 전달 불가능하며 이후 발송에서 제외됩니다. Braze에서의 반송에 대한 자세한 내용은 이메일 분석 용어집의 <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#bounces">반송</a> 을 참조하세요.
  - name: Bulk folder
    description: 일부 이메일 클라이언트에서는 정크 또는 스팸 폴더라고도 합니다.
  - name: CAN-SPAM Act
    description: "상업용 이메일을 규제하는 미국 법률입니다(정식 명칭: 2003년 비요청 포르노그래피 및 마케팅 공격 통제법)."
  - name: Click rate
    description: 수신자가 메시지 내 링크를 클릭한 비율입니다. 자세한 내용은 이메일 분석 용어집의 <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#unique-clicks">고유 클릭</a> 을 참조하세요.
  - name: Content filters
    description: 이메일 자체의 텍스트, 단어, 문구 또는 헤더 정보를 기반으로 이메일을 차단하는 소프트웨어 필터입니다.
  - name: Deferred
    description: 메시지가 첫 번째 시도에서 전달되지 못하면 해당 메시지는 지연된 것으로 간주됩니다. 대부분의 지연된 메일은 결국 전달됩니다.
  - name: Deliverability
    description: 전달 가능성 커뮤니티에서 전달 가능성은 주로 받은편지함에 도달하는 능력에 초점을 맞춥니다. 이 비율은 Braze가 직접 추적할 수 없으므로, 받은편지함 배치에 대한 추론을 위해 다른 사용 가능한 데이터를 활용해야 합니다.
  - name: Delivery rate
    description: 받은편지함 배치 여부나 메일이 열람되었는지와 관계없이 성공적으로 전달된 비율입니다. 자세한 내용은 이메일 분석 용어집의 <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#deliveries">전달률 %</a> 를 참조하세요.
  - name: DKIM
    description: DomainKeys Identified Mail은 조직이 전송 중인 메시지에 대해 책임을 질 수 있도록 합니다. 해당 조직은 메시지의 발신자이거나 중개자로서 메시지의 핸들러입니다. 조직의 평판은 메시지를 전달할 것인지 신뢰할 수 있는지 평가하는 기준이 됩니다.
  - name: DMARC
    description: Domain-based Message Authentication, Reporting & Conformance는 이메일 피싱 및 사기를 줄이기 위해 조직들이 만든 기술 사양입니다. 현재 Google, Yahoo, Microsoft를 포함한 모든 주요 메일함 공급자가 사용하고 있습니다.
  - name: Drop
    description: SendGrid는 각 사용자의 반송, 스팸 신고 및 탈퇴를 추적하기 위한 이메일 목록을 유지합니다. 사용자가 자신의 계정 내 이러한 목록에 존재하는 이메일 주소로 메시지를 보내면, SendGrid는 자동으로 해당 메시지를 드롭합니다(즉, 해당 주소로 발송하지 않습니다).
  - name: ESP (email service provider)
    description: 이메일 마케터에게 이메일 발송 및 전송 기능을 제공하는 회사입니다. 오늘날 많은 마케팅, CRM 및 고객 인게이지먼트 플랫폼에는 이메일 발송 구성 요소가 포함되어 있으며, 이메일 발송 기능과 관련하여 일반적으로 ESP라고 합니다. 예시로는 ConstantContact, MailChimp, Emarsys, Salesforce Marketing Cloud, Cheetah Digital, Sailthru 등이 있습니다.
  - name: Feedback loop (FBL)
    description: 발신자가 스팸 신고를 통보받아 스팸 신고율을 계산하고 향후 발송에서 해당 주소를 제거할 수 있도록 하는 메커니즘입니다.
  - name: Hard bounce
    description: 유효하지 않거나, 폐쇄되었거나, 존재하지 않는 이메일 계정으로 보낸 메시지입니다. 일반적으로 하드 반송된 이메일은 500 시리즈 SMTP 응답 코드로 식별할 수 있습니다. 자세한 내용은 이메일 분석 용어집의 <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#hard-bounce">하드 반송</a> 을 참조하세요.
  - name: IP
    description: 인터넷에 연결된 각 기기에 할당된 고유 번호입니다.
  - name: ISP (Internet Service Provider)
    description: AT&T, British Telecom, Comcast(Xfinity), Cox, Orange, Sky, Spectrum, Tiscali, TalkTalk, Virgin 등 소비자에게 인터넷 서비스를 제공하는 회사입니다. 구어적으로 Gmail, Yahoo, Microsoft와 같은 메일함 공급자도 포함합니다.
  - name: List hygiene
    description: 하드 반송 및 탈퇴한 이름을 메일링에서 제거하여 목록을 유지 관리하는 행위입니다.
  - name: List-Unsubscribe
    description: List-Unsubscribe 헤더는 메시지의 헤더 부분에 포함할 수 있는 텍스트로, 수신자가 향후 메시지를 자동으로 중지하기 위해 선택할 수 있는 탈퇴 버튼을 볼 수 있도록 합니다.
  - name: Mailbox provider (MBP)
    description: Gmail, Yahoo, Microsoft 등 수신자에게 이메일 액세스를 제공하는 공급자입니다.
  - name: MX record
    description: MX 레코드는 도메인 이름 시스템(DNS)에서 SMTP(Simple Mail Transfer Protocol)를 사용하여 인터넷 이메일이 어떻게 라우팅되어야 하는지를 지정하는 리소스 레코드 유형입니다.
  - name: NDR (non-delivery report)
    description: 이메일 수신자가 이메일 전달을 수락하지 않기로 선택했을 때 SMTP 응답 형태로 제공되는 피드백입니다. NDR은 흔히 반송이라고 합니다.
  - name: Opens unique rate
    description: 열람 추적 픽셀이 로드된 비율로, 고유 수신자만 계산합니다(중복 제외). 자세한 내용은 이메일 분석 용어집의 <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#unique-opens">고유 열람</a> 을 참조하세요.
  - name: Phishing
    description: 사기꾼이 진짜처럼 보이는 이메일을 사용하여 수신자를 속여 신용카드 또는 은행 계좌 번호, 사회보장번호 및 기타 개인 식별 정보(PII)와 같은 민감한 개인 정보를 제공하도록 하는 신원 도용의 한 형태입니다.
  - name: Re-engagement campaign
    description: 비활성 또는 무응답 사용자에게 보내는 이메일 캠페인으로, 이들을 다시 확보하고 열람, 클릭 및 전환의 형태로 이메일에 다시 참여하도록 하기 위한 것입니다. 재참여 캠페인은 단독 캠페인 또는 일련의 캠페인으로 비활성 사용자에게 발송할 수 있습니다.
  - name: Reverse DNS (rDNS)
    description: 도메인 이름이 IP 주소에 매칭되는 것이 아니라, IP 주소가 도메인 이름에 올바르게 매칭되는 프로세스입니다. 스팸 필터나 프로그램이 IP 주소를 도메인 이름에 매칭할 수 없으면 이메일을 거부할 수 있습니다.
  - name: Smart Network Data Services (SNDS)
    description: Windows Live Hotmail에서 제공하는 SNDS는 Hotmail 가입자에게 실제로 발송된 메일을 기반으로 발신자에게 데이터를 제공합니다. 보고되는 측정기준에는 불만 사항, SmartScreen 필터 결과 및 스팸 트랩 적중이 포함됩니다.
  - name: Soft bounce
    description: "메일함 가득 참", "사용자 할당량 초과", "스팸과 유사한 특성으로 인해 메일 차단", "조직 정책 위반으로 메시지 거부" 또는 "서버 일시적 사용 불가"와 같은 일시적 또는 과도적 문제로 인한 반송입니다. SendGrid는 이를 "차단"이라고 합니다.<br><br>일시적 문제로 판단되는 소프트 반송(일반적으로 SMTP 4xx 코드)에 대해서는 메시지가 전달되거나 72시간이 경과할 때까지 전달이 재시도됩니다. 소프트 반송된 메시지가 72시간 후에도 전달되지 않으면 추가 전달 시도가 중단되고 실패한 메시지 전달은 반송으로 집계됩니다. 자세한 내용은 이메일 분석 용어집의 <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#soft-bounce">소프트 반송</a> 을 참조하세요.
  - name: Spam
    description: 원치 않는 이메일입니다. 측정기준에서 사용자가 이러한 이메일을 스팸으로 표시해야 합니다(이메일이 먼저 전달되어야 하므로 이 수치는 전달에 포함됩니다). 자세한 내용은 이메일 분석 용어집의 <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#spam">스팸</a> 을 참조하세요.
  - name: SpamCop
    description: 이전에는 개인 소유였으나 현재 이메일 벤더 Ironport의 일부인 차단 목록 및 IP 주소 데이터베이스입니다. 많은 메일함 공급자는 수신 이메일의 IP 주소를 SpamCop의 기록과 대조하여 해당 주소가 스팸 불만으로 인해 차단 목록에 등록되었는지 확인합니다.
  - name: Spam rate
    description: 수신자가 메시지를 보면서 스팸으로 표시한 비율입니다. 이 비율에는 스팸 폴더에 도착한 메일은 포함되지 않습니다. 또한 Gmail 및 iCloud와 같이 피드백 루프가 없는 메일함 공급자의 불만도 포함되지 않습니다. 자세한 내용은 이메일 분석 용어집의 <a href="/docs/user_guide/channels/email/reporting/analytics_glossary#spam">스팸</a> 을 참조하세요.
  - name: Spam trap
    description: ISP 및 스팸 방지 조직이 스팸을 수집하고 탐지하기 위해 사용하는 이메일입니다. 스팸트랩이라고도 합니다. 자세한 내용은 <a href="/docs/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps">전달 가능성 함정 및 스팸 트랩</a> 을 참조하세요.
  - name: Suppression list
    description: Braze에는 억제 목록이 없지만, <a href="/docs/user_guide/channels/email/best_practices/sunset_policies">일몰 정책</a> 에 문서화된 대로 일몰 정책을 만들 수 있습니다. 이메일 가입 관리에 대한 자세한 내용은 <a href="/docs/user_guide/channels/email/subscriptions">가입</a> 을 참조하세요.
  - name: Throttling
    description: 발송자가 한 번에 하나의 메일함 공급자 또는 메일 서버에 보내는 이메일 메시지 수를 조절하는 관행입니다. 일부 메일함 공급자는 너무 많은 메시지를 수신하면 이메일을 반송합니다.
  - name: Transactional mail
    description: 트랜잭션 메시지는 CAN-SPAM법에 따라 "이전에 합의된 거래를 촉진, 완료 또는 확인하는" 이메일로 정의됩니다. 상업용 메시지와 달리 트랜잭션 메시지에는 미국 우편 서비스 주소나 탈퇴 링크가 필요하지 않습니다.

---