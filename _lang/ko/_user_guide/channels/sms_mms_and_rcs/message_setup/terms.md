---
page_order: 5
nav_title: 알아야 할 용어
article_title: SMS, MMS, RCS 알아야 할 용어
alias: /sms_terms_to_know/

layout: glossary_page
glossary_top_header: "알아야 할 용어"
glossary_top_text: "다음 용어를 확인하여 SMS, MMS, RCS 생태계, 기술 및 프로세스에 대해 자세히 알아보세요."
page_type: glossary
description: "이 용어집은 알아야 할 다양한 SMS, MMS, RCS 용어를 정의합니다."
channel:
  - SMS
  - MMS
  - RCS

glossaries:
  - name: SMS (Short Message Service)
    description: 1980년에 만들어진 메시징 채널로 가장 오래된 문자 기술 중 하나입니다. 또한 모든 문자 채널 중 가장 널리 보급되고 자주 사용되는 채널이기도 합니다. 이 채널은 사용자와 고객의 개인 전화번호를 활용하여 연락하기 때문에 대부분의 다른 메시징 채널보다 더 직접적으로 사용자와 고객에게 도달할 수 있는 방법입니다. 따라서 SMS에는 다른 메시징 채널보다 더 많은 규칙과 규정이 적용됩니다.
  - name: Short Code
    description: 발신자가 긴 번호보다 더 일관된 속도로 더 많은 메시지를 보낼 수 있게 해주는 짧고 기억하기 쉬운 5~6자리 숫자 시퀀스입니다(초당 1개 메시지).<br><br>짧은 코드 또는 긴 코드 중 하나가 필요합니다.
  - name: Long Code
    description: 발신자가 초당 1개 메시지 속도로 메시지를 보낼 수 있게 해주는 표준 10자리 전화번호(대부분의 국가에서)입니다.<br><br>짧은 코드 또는 긴 코드 중 하나가 필요합니다.
  - name: Encoding
    description: 무엇이든 코드화된 형태로 변환하는 것입니다. SMS 콘텐츠는 GSM-7 또는 UCS-2로 인코딩할 수 있습니다.
  - name: GSM-7 Encoding (Global System for Mobile Communications)
    description: GSM-7은 대부분의 SMS 메시징에서 가장 많이 사용되는 인코딩 표준입니다. 대부분의 그리스어 및 영어 알파벳과 일부 추가 문자를 사용합니다. GSM-7 인코딩 및 사용할 수 있는 문자 집합에 대해 <a href='https://en.wikipedia.org/wiki/GSM_03.38#GSM_7-bit_default_alphabet_and_extension_table_of_3GPP_TS_23.038_.2F_GSM_03.38' title="GSM 7비트 기본 알파벳 및 확장 테이블">Wikipedia</a> 에서 자세히 알아볼 수 있습니다. 중국어, 한국어, 일본어 등의 언어는 16비트 UCS-2 문자 인코딩을 사용하여 전송해야 합니다. <br> <br> 이 유형의 인코딩에서 세그먼트당 문자 제한은 약 128자로 추정할 수 있습니다.
  - name: UCS-2 Encoding (Universal Coded Character Set)
    description: UCS-2 인코딩은 대체 인코딩 표준으로, 특히 메시지를 GSM-7로 인코딩할 수 없거나 언어를 렌더링하는 데 128자 이상이 필요한 경우에 사용됩니다. UCS-2는 "문자"가 아닌 <a href='https://en.wikipedia.org/wiki/Code_point'>코드 포인트</a> 로 측정하는 것이 더 적합합니다. 그럼에도 불구하고 이 유형의 인코딩에서 세그먼트당 문자 제한은 약 67자로 추정할 수 있습니다.
  - name: Subscription Groups for SMS
    description: 구독 그룹은 사용자 또는 고객의 특정 구독 수준을 타겟팅할 수 있게 해주는 Braze 도구입니다. SMS 구독 그룹은 메시지 서비스를 기반으로 내부적으로 구성되며 워크스페이스 간에 공유할 수 없습니다.
  - name: Message Segments
    description: 메시지 세그먼트는 단일 SMS 발송으로 전송되는 정의된 문자 수(GSM-7 인코딩의 경우 160자, UCS-2 인코딩의 경우 67자)까지의 그룹입니다. GSM-7 인코딩을 사용하여 161자의 SMS를 발송하면 두(2)개의 메시지 세그먼트가 전송된 것을 확인할 수 있습니다. 여러 메시지 세그먼트를 전송하면 추가 요금이 발생할 수 있습니다.
  - name: Message Service
    description: Braze로 SMS 메시지를 보내는 데 사용되는 긴 코드, 짧은 코드 및 영숫자 ID의 모음입니다.
  - name: Keyword
    description: "사전 정의된 SMS 프로그램과 상호작용하거나 특정 프로그램 또는 코드의 모든 프로그램에서 수신 거부를 요청하기 위해 짧은 코드 또는 긴 코드로 전송되는 짧은 단어입니다. 예를 들어, <code>STOP</code>. 키워드는 다음 조건을 충족해야 합니다: <br> - 영숫자여야 합니다 <br> - 공백이 없어야 합니다 <br> - 10자 미만이어야 합니다. <br> <br> 특정 키워드와 짧은 코드 조합은 한 번에 하나의 활성 프로그램에서만 사용할 수 있습니다. 다른 프로그램에서 이미 사용 중인 키워드를 입력하면 유효성 검사 오류가 나타납니다. <br> <br> 모든 SMS 콘텐츠 제공업체가 준수해야 하는 두 가지 필수 키워드 카테고리가 있습니다: <code>STOP</code> 및 <code>HELP</code>."
  - name: Mandatory Keyword HELP
    description: SMS Campaign 매니저 플랫폼에서 생성되는 각 프로그램에 대해 이 키워드의 콘텐츠를 제공해야 하며, SMS 트래픽이 전송 및 수신되는 국가 또는 지역별 모범 사례 및 이동통신사 규정을 준수해야 합니다. 대부분의 경우 이 콘텐츠에는 SMS 프로그램에 대한 간략한 설명과 수신 거부 방법이 포함되어야 합니다.
  - name: Global STOP Keywords
    description: 변형에는 <code>STOP</code>, <code>END</code>, <code>QUIT</code>, <code>UNSUBSCRIBE</code>, <code>CANCEL</code>, <code>STOPALL</code>이 포함됩니다. 이를 <code>Global-Stop-Keywords</code>라고 합니다. 이러한 키워드 중 하나가 짧은 코드 또는 긴 코드로 문자 전송되면, 해당 모바일 번호(발신 휴대전화 번호)가 해당 코드에 연결된 모든 활성 SMS 프로그램에서 수신 거부됩니다.
  - name: Vanity Code
    description: 배니티 짧은 코드는 브랜드가 특별히 선택한 5~6자리 전화번호입니다. 배니티 짧은 코드는 브랜드화되어 있어 소비자가 기억하기 쉽습니다.
  - name: Shared Short Code
    description: 공유 짧은 코드를 사용하면 어떤 비즈니스나 조직이 보내든 모든 문자 메시지가 동일한 5~6자리 전화번호에서 소비자의 모바일 기기에 도착합니다. 공유 짧은 코드는 비용이 비교적 저렴하고 즉시 사용할 수 있지만, 비즈니스에 전용 짧은 코드가 없으며 다른 비즈니스가 공유 짧은 코드에 대해 올바른 프로토콜을 따르는지에 영향을 받습니다.
  - name: Alphanumeric Sender ID
    description: 영숫자 발신자 ID를 사용하면 지원되는 국가에 단방향 메시지를 보낼 때 영숫자 문자를 사용하여 회사 이름이나 브랜드를 발신자 ID로 설정할 수 있습니다.
  - name: Toll-Free Number
    description: 수신자 부담 전화번호 또는 무료 전화번호는 발신 전화 가입자에게 요금을 부과하는 대신 모든 수신 통화에 대해 요금이 청구되는 전화번호입니다. 미국과 캐나다의 수신자 부담 번호는 SMS가 활성화되어 있으며, 가입자에게 수신 및 발신 문자에 대한 요금이 부과됩니다.<br><br>수신자 부담 메시징은 고객 지원이나 영업과 같이 발신자와 수신자가 문자로 대화하는 개인 간 사용 사례에 가장 적합합니다.
  - name: One-Way Messaging
    description: 단방향 메시징을 사용하면 문자 메시지를 보내 고객과 소통할 수 있습니다. 단방향 메시징은 긴 코드와 짧은 코드를 사용할 수 없는 시장에서 영숫자 발신자 ID를 구현하는 경우에 유용합니다.
  - name: Two-Way Messaging
    description: 양방향 메시징을 사용하면 문자 메시지를 보내고 받아 대화를 이어갈 수 있습니다.
  - name: MMS (Multimedia Message Service)
    description: MMS는 멀티미디어 자산(JPEG, GIF, PNG)이 포함된 메시지를 휴대전화로 보내는 데 사용됩니다. SMS와 마찬가지로 MMS는 고객에게 즉시 소통할 수 있는 긴급성이 높은 메시징 채널입니다. MMS는 텍스트 전용 SMS에 미디어를 추가할 수 있는 기능을 제공하여 SMS의 기능을 확장합니다.
  - name: RCS (Rich Communication Services)
    description: 리치 커뮤니케이션 서비스(RCS)는 기존 SMS를 향상시켜 브랜드가 정보를 전달할 뿐만 아니라 훨씬 더 매력적인 메시지를 전달할 수 있게 합니다. RCS는 고품질 미디어, 인터랙티브 버튼, 브랜드 발신자 프로필과 같은 기능을 사용자의 기본 설치 메시징 앱에 직접 제공합니다.
  - name: RCS-Verified Sender
    description: RCS 메시지의 발신 주체로, 수신자가 기기에서 메시지의 출처를 식별하기 위해 보는 정보입니다. RCS 인증 발신자에는 회사 이름, 캡션, 시각적 브랜딩 및 인증 배지가 포함됩니다. 필요한 RCS 발신자 등록 정보를 Braze에 제공하면, Braze가 등록 및 구독 그룹 설정을 처리합니다.
  - name: SMS Fallback
    description: RCS 메시지를 전달할 수 없는 경우(예를 들어 해당 지역에서 이동통신사 지원이 부족한 경우), 구독 그룹 내에 SMS 코드가 있으면 Braze는 여전히 SMS를 통해 메시지를 전달하려고 시도합니다.
  - name: Basic RCS
    description: 160자 이하의 텍스트 전용 RCS 메시지입니다. 단일 메시지로 과금됩니다. 이 카테고리는 글로벌 모델에서만 사용됩니다.
  - name: Single RCS
    description: 160자를 초과하거나 버튼이나 미디어와 같은 리치 요소를 포함하는 텍스트 전용 RCS 메시지입니다. 이 카테고리는 글로벌 모델에서만 사용됩니다.
  - name: Rich RCS
    description: 제한된 제안이나 버튼이 포함되거나 포함되지 않은 텍스트 전용 RCS 메시지입니다. 세그먼트(160 UTF-8 바이트)당 과금됩니다. 이 카테고리는 미국 모델에서만 사용됩니다.
  - name: Rich Media RCS
    description: 미디어 파일(이미지, 동영상) 또는 리치 카드를 포함하는 RCS 메시지입니다. 메시지 길이에 관계없이 단일 메시지로 과금됩니다. 이 카테고리는 미국 모델에서만 사용됩니다.
---