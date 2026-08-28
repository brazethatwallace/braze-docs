---
nav_title: "SMS, MMS, RCS"
article_title: "SMS, MMS, RCS"
page_order: 8
page_type: landing
channel:
  - SMS
  - MMS
  - RCS
search_rank: 3
description: "이 랜딩 페이지는 SMS(단문 메시지 서비스), MMS(멀티미디어 메시지 서비스), RCS(리치 커뮤니케이션 서비스)에 대한 정보를 제공합니다. 이러한 서비스는 사용자의 전화번호를 활용하여 실시간으로 연락할 수 있으므로, 대부분의 다른 메시징 채널보다 더 직접적으로 사용자에게 도달할 수 있습니다."
---

# SMS, MMS, RCS {#sms-mms-and-rcs}

> SMS(단문 메시지 서비스), MMS(멀티미디어 메시지 서비스), RCS(리치 커뮤니케이션 서비스)는 사용자의 전화번호를 활용하여 실시간으로 도달할 수 있는 직접적인 메시징 채널입니다. SMS는 빠르고 익숙하며, 시간에 민감한 업데이트에 효과적이기 때문에 전 세계에서 가장 널리 사용되는 채널 중 하나입니다. 이 허브에서는 Braze에서 SMS, MMS, RCS를 위한 발신자 설정, 규정 준수, 옵트인 수집, 메시지 작성 및 보고에 대해 다룹니다. 첫 메시지를 보내기 전에 [법률 및 규정]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)과 [사용자 옵트인 수집]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins)을 검토하세요.

## 사전 요구 사항 {#prerequisites}

SMS, MMS, RCS 사용 가능 여부는 Braze 패키지에 따라 다릅니다. 시작하려면 계정 매니저 또는 고객 성공 매니저에게 문의하세요.

시작하기 전에 다음 사항을 확인하세요:

- 짧은 코드, 긴 코드 또는 영숫자 발신자 ID가 구성되어 있어야 합니다. 자세한 내용은 [발신자 설정]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup)을 참조하세요.
- TCPA 및 이동통신사 요구 사항을 포함한 SMS 관련 법률 및 규정에 대한 이해가 필요합니다. 자세한 내용은 [법률 및 규정]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)을 참조하세요.
- 사용자로부터 명시적인 옵트인 동의를 수집해야 합니다. 자세한 내용은 [사용자 옵트인 수집]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins)을 참조하세요.

## 사용 사례 {#use-cases}

| 사용 사례 | 설명 |
| --- | --- |
| 예약 알림 | 예약된 일정 전에 적시에 알림을 보내어 노쇼를 줄이고 고객에게 정보를 제공합니다. |
| 주문 업데이트 | 주문 확인, 배송 상태, 배달 업데이트를 실시간으로 고객에게 알립니다. |
| 2단계 인증 | 계정 로그인 및 트랜잭션 확인을 위한 일회용 인증 코드를 전달합니다. |
| 프로모션 오퍼 | 시간 제한 프로모션, 반짝 세일, 개인화된 할인 정보를 고객의 휴대폰으로 직접 전달합니다. |
| 고객 지원 | 양방향 대화를 통해 고객 문의를 해결하고, 피드백을 수집하거나, 서비스 요청을 확인합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사용 사례" }

## SMS, MMS, RCS 비교 {#sms-mms-and-rcs-compared}

- **SMS**는 최대 160자(유니코드 사용 시 70자)의 텍스트 전용 메시지를 전송합니다. 모든 모바일 기기와 통신사에서 범용적으로 지원됩니다.
- **MMS**는 이미지, GIF, 오디오 등 멀티미디어 콘텐츠를 지원하여 SMS를 확장합니다. MMS를 사용하려면 통신사 및 기기의 지원이 필요합니다.
- **RCS**는 브랜드 발신자 프로필, 추천 답장, 캐러셀, 읽음 확인 등 풍부한 기능을 제공하는 차세대 비즈니스 메시징입니다. RCS 이용 가능 여부는 통신사 및 기기 지원에 따라 달라집니다.

### RCS를 사용해야 하는 이유 {#why-use-rcs}

RCS(리치 커뮤니케이션 서비스)는 지원 기기의 기본 메시징 앱에서 앱과 유사한 풍부한 경험을 제공하여 SMS를 발전시킵니다. 브랜드는 다음과 같은 이유로 RCS를 사용합니다:

- 일반 텍스트만 전송하는 대신 고해상도 이미지와 비디오를 전달할 수 있습니다.
- 추천 답장과 액션을 추가하여 고객이 한 번의 탭으로 응답할 수 있습니다.
- 브랜딩이 포함된 인증된 발신자 프로필을 표시하여 메시지 신뢰도를 높일 수 있습니다.
- 통신사가 허용하는 경우 읽음 확인 및 입력 표시 기능을 지원합니다.

RCS는 트랜잭션 업데이트(배송, 예약), 리치 크리에이티브를 활용한 프로모션, 빠른 답장 경로를 통한 고객 지원, 미디어와 구조화된 액션을 활용하는 온보딩 또는 튜토리얼과 같은 사용 사례에 적합합니다. 설정 및 SMS에서의 마이그레이션에 대한 자세한 내용은 [RCS 설정]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup)을 참조하세요.

## 자주 묻는 질문 {#frequently-asked-questions}

### Braze에서 SMS를 발송하기 전에 옵트인 동의가 필요한가요? {#do-i-need-opt-in-consent-before-sending-sms-in-braze}

네. 명시적인 옵트인 동의를 수집하고 TCPA 및 이동통신사 요구 사항 등 관련 법률을 준수해야 합니다. [사용자 옵트인 수집]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins) 및 [법률 및 규정]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)을 참조하세요.

### SMS, MMS, RCS의 차이점은 무엇인가요? {#what-is-the-difference-between-sms-mms-and-rcs}

SMS는 텍스트 전용 메시지를 전송하고, MMS는 이미지 등의 멀티미디어를 추가하며, RCS는 브랜드 발신자 프로필 및 추천 답장과 같은 리치 기능을 지원하는 기기에서 제공합니다. 이 페이지 앞부분의 **SMS, MMS, RCS 비교**를 참조하세요.

### SMS 발신자 번호는 어떻게 구성하나요? {#how-do-i-configure-sender-numbers-for-sms}

캠페인 실행 전에 Braze에서 짧은 코드, 긴 코드 또는 영숫자 발신자 ID를 설정하세요. [발신자 설정]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup)을 참조하세요.

## 다음 단계 {#next-steps}

- [메시지 설정]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup)
- [메시지 만들기]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create)