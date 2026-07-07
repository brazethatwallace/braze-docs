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

> SMS(단문 메시지 서비스), MMS(멀티미디어 메시지 서비스), RCS(리치 커뮤니케이션 서비스)는 전화번호를 활용하여 실시간으로 연락할 수 있으므로, 대부분의 다른 메시징 채널보다 더 직접적으로 사용자에게 도달할 수 있습니다.

SMS는 전 세계에서 가장 널리 사용되는 채널 중 하나로, 매일 수십억 건의 문자 메시지가 전송됩니다. 빠르고 직접적이며 고객에게 익숙하기 때문입니다.

## 필수 조건 {#prerequisites}

SMS, MMS, RCS의 사용 가능 여부는 Braze 패키지에 따라 다릅니다. 시작하려면 계정 매니저 또는 고객 성공 매니저에게 문의하세요.

시작하기 전에 다음 사항을 준비하세요:

- 짧은 코드, 긴 코드 또는 영숫자 발신자 ID가 구성되어 있어야 합니다. 자세한 내용은 [발신자 설정]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup)을 참조하세요.
- TCPA 및 통신사 요구 사항을 포함한 SMS 관련 법률 및 규정에 대한 이해가 필요합니다. 자세한 내용은 [법률 및 규정]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)을 참조하세요.
- 사용자로부터 명시적인 옵트인 동의를 수집해야 합니다. 자세한 내용은 [사용자 옵트인 수집]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins)을 참조하세요.

## 활용 사례 {#use-cases}

| 활용 사례 | 설명 |
| --- | --- |
| 예약 알림 | 예약된 일정 전에 적시에 알림을 보내 노쇼를 줄이고 고객에게 정보를 제공합니다. |
| 주문 업데이트 | 주문 확인, 배송 상태, 배달 업데이트를 실시간으로 고객에게 알립니다. |
| 2단계 인증 | 계정 로그인 및 트랜잭션 확인을 위한 일회용 인증 코드를 전달합니다. |
| 프로모션 제안 | 시간 제한 프로모션, 반짝 세일, 개인화된 할인 정보를 고객의 휴대폰으로 직접 전달합니다. |
| 고객지원 | 양방향 대화를 통해 고객 문의를 해결하고, 피드백을 수집하거나, 서비스 요청을 확인합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="활용 사례" }

## SMS, MMS, RCS 비교 {#sms-mms-and-rcs-compared}

- **SMS**는 최대 160자(유니코드의 경우 70자)의 텍스트 전용 메시지를 전달합니다. 모든 모바일 기기와 통신사에서 보편적으로 지원됩니다.
- **MMS**는 이미지, GIF, 오디오 등 멀티미디어 콘텐츠를 지원하여 SMS를 확장합니다. MMS는 통신사 및 기기 지원이 필요합니다.
- **RCS**는 차세대 비즈니스 메시징으로, 브랜드 발신자 프로필, 추천 답장, 캐러셀, 읽음 확인 등 풍부한 기능을 제공합니다. RCS 사용 가능 여부는 통신사 및 기기 지원에 따라 다릅니다.

### RCS를 사용하는 이유 {#why-use-rcs}

RCS(리치 커뮤니케이션 서비스)는 지원되는 기기의 기본 메시징 앱에서 더 풍부하고 앱과 유사한 경험을 제공하여 SMS를 기반으로 발전시킨 서비스입니다. 브랜드는 다음과 같은 목적으로 RCS를 사용합니다:

- 일반 텍스트 대신 고해상도 이미지와 동영상을 전달합니다.
- 추천 답장과 동작을 추가하여 고객이 한 번의 탭으로 응답할 수 있도록 합니다.
- 브랜딩이 포함된 인증된 발신자 프로필을 표시하여 메시지의 신뢰성을 높입니다.
- 통신사가 허용하는 경우 읽음 확인 및 입력 중 표시를 지원합니다.

RCS는 트랜잭션 업데이트(배송, 예약), 풍부한 크리에이티브를 활용한 프로모션, 빠른 답장 경로를 통한 고객지원, 미디어와 구조화된 동작이 유용한 온보딩 또는 튜토리얼 등의 사용 사례에 적합합니다. 설정 및 SMS에서의 마이그레이션에 대한 자세한 내용은 [RCS 설정]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup)을 참조하세요.

## 다음 단계 {#next-steps}

- [메시지 설정]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup)
- [메시지 만들기]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create)