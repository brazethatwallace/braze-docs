---
nav_title: Meta 리소스
article_title: Meta 리소스
page_order: 6
description: "이 문서에서는 WhatsApp 통합에 대한 이해를 높이는 데 도움이 되는 Meta 설명서, 정보 및 리소스를 제공합니다."
alias: /meta_resources/
page_type: reference
channel:
  - WhatsApp

---

# Meta 리소스 {#meta-resources}

> 이 페이지에서는 Braze와의 WhatsApp 통합에 대한 이해를 높이는 데 도움이 되는 Meta 설명서, 제품 업데이트 및 자주 묻는 질문을 제공합니다.

## Meta 설명서 {#meta-documentation}

표시 이름, 전화번호 등에 대한 안내는 다음 Meta 설명서를 참조하세요.

- [표시 이름 안내](https://www.facebook.com/business/help/757569725593362)
- [Meta 인사이트 활성화](https://www.facebook.com/business/help/218116047387456)
- [전화번호 요구 사항](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)
- [메시징 제한](https://developers.facebook.com/docs/whatsapp/messaging-limits)
- [품질 등급](https://www.facebook.com/business/help/896873687365001)

## WhatsApp 제품 업데이트 {#whatsapp-product-updates}

### 2026: 비즈니스 사용자 이름 {#2026-business-usernames}
*최종 업데이트: 2026년 5월*

Meta는 WhatsApp용 비즈니스 사용자 이름을 도입하고 있습니다. 이는 비즈니스가 WhatsApp 전화번호에 대해 채택할 수 있는 선택적 표시 이름입니다. 사용자 이름이 설정되면 WhatsApp 및 WhatsApp Business 앱 채팅 창에서 전화번호 대신 표시됩니다. 사용자 이름을 채택해도 전화번호가 숨겨지지는 않으며, 비즈니스 프로필에서 항상 확인할 수 있습니다.

사용자 이름은 모든 WhatsApp 전화번호에서 고유합니다. 소비자든 비즈니스든 두 개의 번호가 같은 사용자 이름을 공유할 수 없습니다. 고유성 목적상 대소문자를 구분하지 않지만, 마침표와 밑줄은 서로 다른 문자로 취급됩니다. 예를 들어, `myid`, `my.id`, `my_id`는 모두 다른 사용자 이름으로 간주되지만, `myID`와 `myid`는 같은 것으로 처리됩니다.

비즈니스 사용자 이름은 다음 형식 요구 사항을 충족해야 합니다:

- 영문자(a–z), 숫자(0–9), 마침표(`.`), 밑줄(`_`)만 포함
- 3자 이상 35자 이하
- 영문자가 최소 1개 포함
- 마침표로 시작하거나 끝나지 않으며, 연속된 두 개의 마침표를 포함하지 않음
- `www`로 시작하지 않음
- 일반적인 도메인 접미사(예: `.com`, `.org`, `.net`)로 끝나지 않음

#### 예약된 사용자 이름 신청 {#claiming-a-reserved-username}

사용자 이름 기능이 광범위하게 제공되기 전에, Meta가 비즈니스를 위해 사용자 이름을 사전 예약했을 수 있습니다. 일반적으로 기존 Facebook 페이지 또는 Instagram 사용자 이름과 일치합니다. [WhatsApp Manage](https://business.facebook.com/wa/manage/)를 통해 이 예약된 사용자 이름을 신청하거나 다른 이름을 선택할 수 있습니다. 신청된 사용자 이름은 Meta가 기능을 제공할 때까지 활성화되지 않습니다.

예약된 사용자 이름이 Facebook 페이지 또는 Instagram 계정에 이미 연결된 사용자 이름과 일치하는 경우, 먼저 비즈니스 전화번호를 해당 페이지 또는 계정에 연결해야 합니다. WhatsApp Manager 또는 Meta Business Suite에서 사용자 이름을 신청하는 동안 이 작업을 수행하거나, 해당 페이지 또는 계정에서 직접 전화번호를 추가할 수 있습니다. 연결하려면 페이지 또는 계정에 대한 전체 제어 권한이 필요하거나, `manage_phone` 권한이 있는 기본적인 부분 접근 권한이 필요합니다.

#### 채팅 창에서의 표시 우선순위 {#display-priority-in-chat-windows}

비즈니스 프로필이 채팅 창에 표시될 때, WhatsApp은 다음 우선순위(높은 것부터 낮은 순서)를 사용합니다:

1. 저장된 연락처 이름
2. 인증된 비즈니스 이름 또는 공식 비즈니스 계정(OBA) 이름
3. 사용자 이름
4. 전화번호

자세한 내용은 Meta의 [비즈니스 사용자 이름](https://developers.facebook.com/documentation/business-messaging/whatsapp/business-scoped-user-ids/#business-usernames) 설명서를 참조하세요.

### 2026년 4월: 비활성 템플릿 자동 보관 {#april-2026-automatic-archival-of-inactive-templates}
*최종 업데이트: 2026년 4월*

- Meta는 12개월 이상 비활성 상태인 템플릿을 자동으로 보관합니다.
- 자동 보관은 모든 WhatsApp 비즈니스 계정에 대해 활성화되어 있으며 비활성화할 수 없습니다.
- 템플릿 활동에는 템플릿 생성, 편집, 전송, 이의 제기 또는 보관 해제가 포함됩니다.
- 보관된 템플릿은 전송할 수 없으며 28일 후 영구 삭제가 예약됩니다.
- 28일 이내에 템플릿 보관을 해제하여 복원하고 예약된 삭제를 취소할 수 있습니다.
- `message_template_status_update` 웹훅, 이메일 및 일회성 WhatsApp Manager 배너를 통해 알림이 전송됩니다.

자세한 내용은 Meta의 [템플릿 보관](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-archival) 설명서를 참조하세요.

### 2026년 6월: 비즈니스 범위 사용자 ID {#june-2026-business-scoped-user-ids}
*최종 업데이트: 2026년 3월*

- Meta는 개인정보 보호를 위해 전화번호 공유를 대체하는 사용자 ID를 도입하고 있습니다
- Braze는 출시에 앞서 솔루션을 준비하고 있습니다
- Meta의 2026년 6월 출시 예정

### 2025년 11월: [WhatsApp 마케팅 메시지 API](https://developers.facebook.com/documentation/business-messaging/whatsapp/marketing-messages/overview/) (이전 Marketing Messages Lite API) {#november-2025-marketing-messages-api-for-whatsapp-formerly-marketing-messages-lite-api}
*최종 업데이트: 2026년 3월*

- 정적 Cloud API 제한을 동적 참여 기반 제한으로 대체
- 최적화된 전달을 위해 EMEA, 일본 또는 한국에서는 사용할 수 없음
- 유틸리티/인증은 Cloud API를 통해 자동으로 계속됨

### 2025년 10월: 공식 비즈니스 계정(OBA) 승인 프로세스 변경 {#october-2025-official-business-account-oba-approval-process-changed}
*최종 업데이트: 2026년 3월*

- 이전에는 WhatsApp Manager를 통해 모든 고객에게 개방
- 현재 정부/대형 Meta 광고주, 직접 광고주 또는 Braze와 같은 BSP를 통해서만 가능(주당 최대 5개)
- 새로운 전제 조건: 비즈니스 인증, 2단계 인증, 승인된 표시 이름, 주목도
- 도움이 필요하면 고객 성공 매니저에게 문의하세요

### 2025년 10월: 지역별 가격 인하 {#october-2025-regional-pricing-rate-cuts}
*최종 업데이트: 2026년 3월*

- 아르헨티나, 이집트, 멕시코, 북미에서 유틸리티/인증 요금 인하
- 멕시코에서 마케팅 요금 인하(2025년 10월 1일부터 적용)

### 2025년 10월: 메시징 제한이 전화번호별에서 비즈니스 포트폴리오별로 변경 {#october-2025-messaging-limits-change-from-per-phone-to-per-business-portfolio}
*최종 업데이트: 2026년 3월*

- 이제 포트폴리오 내 모든 전화번호에서 제한이 공유됨
- 포트폴리오는 기존 최고 제한을 상속
- 더 높은 제한에 더 빠르게 접근 가능(6시간 이내)
- 위험: "무제한" 번호가 없는 비즈니스는 총 제한이 감소할 수 있음

### 2025년 7월 1일: 가격 체계 개편 {#july-1-2025-pricing-overhaul}
*최종 업데이트: 2026년 3월*

- 메시지당 과금이 대화당 과금을 대체
- 24시간 서비스 창 내에서 전송된 유틸리티 메시지가 무료로 전환
- 여러 시장에서 유틸리티/인증 요금 업데이트, 새로운 볼륨 티어 추가
- 유틸리티 템플릿 오분류에 대한 새로운 규칙 - 비즈니스가 템플릿 거부 및 제출 제한에 직면할 수 있음

### 2025년 4월: 미국 전화번호에 대한 마케팅 메시지 일시 중지 {#april-2025-pause-of-marketing-messages-to-us-phone-numbers}
*최종 업데이트: 2026년 8월*

Meta는 미국 전화번호(다이얼링 코드 `+1`과 미국 지역 코드로 구성된 번호)를 가진 WhatsApp 사용자와의 새로운 비즈니스 발신 마케팅 대화를 일시 중지합니다. 현재 이 일시 중지가 해제될 예정 날짜는 없습니다.

마케팅 템플릿은 24시간 고객 서비스 창 또는 [WhatsApp 클릭 광고]({{site.baseurl}}/user_guide/channels/whatsapp/use_cases/ads_that_click_to_whatsapp#considerations)에 의해 열린 72시간 무료 진입점 창과 같은 사용자 발신 대화 창이 열려 있는 동안에는 계속 전달될 수 있습니다. 이러한 창 외에서 미국 전화번호로 마케팅 템플릿을 전송하려고 하면 오류 `131049`가 발생합니다. 유틸리티, 인증, 서비스 및 응답 메시지는 계속 사용할 수 있습니다.

### 2025년 3월: 템플릿 카테고리 오용 제한 {#march-2025-template-category-misuse-restrictions}
*최종 업데이트: 2026년 3월*

- Meta는 유틸리티/마케팅 분류를 오용하는 비즈니스에 대한 제재를 도입
- 7~30일간 템플릿 생성 및 카테고리 검토 제한이 발생할 수 있음

### 2025년 3월: 사용자별 마케팅 템플릿 메시지 제한 {#march-2025-per-user-marketing-template-message-limits}
*최종 업데이트: 2025년 8월*

Meta는 특정 기간 내에 모든 비즈니스로부터 사용자가 받을 수 있는 마케팅 템플릿 메시지 수를 제한하며, 읽힐 가능성이 낮은 메시지부터 시작합니다.

한 가지 예외로, 사용자가 마케팅 메시지에 응답하면 24시간 고객 서비스 창이 시작됩니다. 이 창 내에서 전송된 마케팅 메시지는 해당 사용자의 제한에 포함되지 않습니다.

구체적인 제한은 사용자의 참여 수준에 따라 다릅니다. WhatsApp의 사용자별 마케팅 템플릿 메시지 제한에 대해 자세히 알아보려면 [WhatsApp의 사용자별 마케팅 템플릿 메시지 제한 설명서](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates#per-user-marketing-template-message-limits)를 참조하세요.

### 2025년 1월: WhatsApp, 4월 1일부터 미국 사용자에 대한 마케팅 메시지 전송 일시 중지 {#january-2025-whatsapp-pausing-marketing-message-sending-to-us-users-starting-april-1}
*최종 업데이트: 2025년 1월*

WhatsApp은 2025년 4월 1일부터 미국 사용자(미국 전화번호를 가진 사람들)에 대한 마케팅 메시지 전송을 일시 중지합니다. [유틸리티, 서비스, 인증](https://developers.facebook.com/docs/whatsapp/pricing/) 메시지와 [응답 메시지]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message)는 미국에서 계속 허용됩니다.

다른 모든 국가 또는 지역에 대한 마케팅 메시지 전송(및 기타 모든 메시지 유형)은 계속 허용되며 영향을 받지 않습니다.

Meta는 WhatsApp이 빠르게 성장하고 있지만 아직 초기 단계에 있는 미국에서 WhatsApp 생태계의 건전성을 유지하기 위해 이 업데이트를 수행한다고 알렸습니다(예: 마케팅 메시지가 다른 지역보다 낮은 참여를 보임). 미국 시장이 마케팅 메시지를 재개할 준비가 되었는지 계속 평가할 것입니다.

미국 지역 코드가 있는 전화번호로의 마케팅 메시지 전달은 WhatsApp에 의해 거부되며 오류 코드 131049가 반환됩니다.

### 2024년 11월: WhatsApp 옵트인 정책 변경 {#november-2024-changes-to-whatsapp-opt-in-policy}
*최종 업데이트: 2025년 1월*

Meta는 최근 [옵트인 정책](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)을 업데이트했습니다. 채널별 동의를 요구하는 대신, 다음 조건이 충족되면 비즈니스가 플랫폼에서 사용자에게 메시지를 보낼 수 있습니다:

1. 해당 사용자가 전화번호를 제공한 경우.
2. 해당 사용자가 WhatsApp에 한정되지 않는 일반 메시징에 대한 옵트인 권한을 제공한 경우.

비즈니스는 옵트인을 받을 때 여전히 모든 현지 법률을 준수하고 다음 요구 사항을 따라야 합니다:

- 비즈니스는 해당 사용자가 비즈니스로부터 커뮤니케이션을 수신하는 데 옵트인한다는 것을 명확히 안내해야 합니다
- 비즈니스는 해당 사용자가 메시지를 수신하도록 옵트인하는 비즈니스 이름을 명확히 안내해야 합니다
- 비즈니스는 관련 법률을 준수해야 합니다

WhatsApp이 정책을 완화했지만, Braze는 최상의 고객 경험과 참여율을 위해 여전히 WhatsApp 채널에 특화된 옵트인을 수집할 것을 권장합니다. 항상 법무 팀과 상의하여 브랜드에 적합한 방법을 확인하세요.

### 2024년 11월: 연말 시즌을 앞두고 미국 사용자에 대한 사용자별 마케팅 템플릿 제한 업데이트 {#november-2024-updates-to-the-per-user-marketing-template-limit-for-people-in-the-us-ahead-of-the-holiday-season}
*최종 업데이트: 2024년 12월*

Meta가 사용자별 마케팅 템플릿 제한을 도입한 이후, 사용자 열람율과 감정에서 상당한 개선이 나타났습니다.

연말 시즌을 앞두고 지금부터, 미국의 사용자들은 새로운 마케팅 대화를 더 적게 받게 됩니다. Meta는 이 변경이 더 참여도 높은 오디언스를 만들어 궁극적으로 비즈니스에 더 나은 성과로 이어질 것으로 기대합니다. 미국 전화번호로 마케팅 메시지를 전송하는 경우, 비즈니스의 전달률이 낮아질 수 있으며, 이는 Braze 커런츠 및 메시지 활동 로그를 통해 오류 코드 `131049`로 모니터링할 수 있습니다.

미국의 비즈니스는 다른 지역에서는 계속 마케팅 메시지를 전달할 수 있으며, 유틸리티, 인증 또는 서비스 메시지, 또는 사용자 발신 대화 창(예: WhatsApp 클릭 광고, 제품 캐러셀 또는 대화의 일부로 전송된 쿠폰 템플릿) 내에서 전송된 마케팅 템플릿 메시지에는 영향이 없습니다.

### 2024년 11월: WhatsApp, 열람율을 포함하도록 품질 기반 계정 제재 확대 {#november-2024-whatsapp-expanding-quality-based-account-enforcements-to-include-read-rates}
*최종 업데이트: 2024년 12월*

WhatsApp은 플랫폼에서 스팸성 행동을 줄이는 등 비즈니스가 고객에게 양질의 경험을 제공할 수 있도록 새로운 방법에 지속적으로 투자하고 있습니다.

11월 22일부터, WhatsApp은 열람율이 극히 낮은 WhatsApp 비즈니스 계정(WABA)에 대한 기존 계정 수준의 품질 제재를 확대하기 시작했습니다. 이 변경은 전 세계적으로 적용됩니다.

계정의 열람율이 크게 떨어지면(예: 계정에서 전송한 대부분의 메시지가 읽히지 않는 경우), 해당 계정에 메시징 차단이 적용됩니다. 대규모로 지속적으로 낮은 열람율이 나타나면 차단의 심각도가 증가합니다.

계정의 열람율이 극히 낮은 경우 다음 조치가 취해집니다:

- 계정이 비즈니스 발신 메시지 전송이 차단됩니다. 고객 발신 메시지에 대한 응답은 계속 가능합니다. 이 초기 차단은 "소프트 잠금"이며, 계정 품질에서 확인 버튼을 선택하여 메시징을 다시 시작할 수 있습니다.
- 소프트 잠금 후에도 열람율이 계속 떨어지거나 낮게 유지되면, 비즈니스는 점진적인 제재 조치에 직면할 수 있습니다(예: 며칠간의 메시징 제한).
- 비즈니스는 적용된 제한이 해제될 때까지 기다려야 메시징을 다시 시작할 수 있습니다. 반복적인 소프트 잠금 후에도 열람율이 계속 낮게 유지되면, 해당 계정은 최종적으로 서비스에서 제외됩니다.

#### 경고 및 제재에 대한 최신 정보 확인 방법 {#how-to-stay-updated-on-these-warnings-and-enforcements}

기존 플랫폼 제재와 마찬가지로, 비즈니스는 WhatsApp Business Manager의 계정 품질 페이지를 통해 이러한 조치에 대한 알림을 받고 확인할 수 있습니다. 제재 알림 이메일이 해당 정보를 기반으로 전송되므로, WhatsApp Business Manager에 모든 필요한 관리자의 올바른 연락처 정보가 등록되어 있는지 확인하세요.

심각한 스팸 위반에 대한 알림은 다음과 같이 전달됩니다:

- WhatsApp Business Manager 알림 센터에 표시
- WhatsApp Manager에 배너로 표시
- WhatsApp Business Manager에 설정된 모든 관리자에게 이메일 전송

### 2024년 5월: Cloud API 튀르키예에서 서비스 개시 {#may-2024-cloud-api-going-live-in-trkiye}
*최종 업데이트: 2024년 5월*

Meta는 이제 Cloud API 비즈니스에 튀르키예에서의 비즈니스 메시징 접근을 제공합니다. 이전에는 WhatsApp Cloud API를 튀르키예의 비즈니스가 사용할 수 있었지만, 튀르키예 번호를 가진 WhatsApp 사용자는 Cloud API를 통해 전송된 메시지를 보내거나 받을 수 없었습니다.

Meta는 사용자가 Meta에 의해 호스팅되는 비즈니스와 채팅할 때 항상 이를 명확히 하며, 모든 사용자는 비즈니스 메시징을 진행하기 위해 관련 WhatsApp 이용약관 및 개인정보 보호정책에 동의해야 합니다. 튀르키예에서의 2021년 이용약관 및 개인정보 보호정책 업데이트는 일시 중지되었다가 현재 진행 중입니다. 이 업데이트는 개인정보 보호에 대한 Meta의 약속을 변경하지 않습니다. 개인 대화는 종단 간 암호화로 보호되어 본인과 의도된 수신자만 볼 수 있습니다. 이 업데이트를 통해 튀르키예 사용자는 원할 경우 선택적 비즈니스 기능에 접근할 수 있으며, WhatsApp의 작동 방식에 대한 투명성이 향상됩니다.

Cloud API 비즈니스는 이제 튀르키예 번호를 가진 WhatsApp 사용자와 대화를 시작할 수 있으며, 기존의 오류 코드 131026 대신 "전송됨" 대화로 웹훅이 반환됩니다.

비즈니스 메시지가 "전달됨" 또는 "읽음"으로 처리되려면 사용자가 WhatsApp 약관에 동의해야 합니다. 메시지가 전달되지 않는 한 비즈니스에 요금이 청구되지 않습니다.

Cloud API 비즈니스로부터 메시지를 받거나 보내려고 하는 사용자에게는 약관 업데이트에 대한 앱 내 알림이 표시되며, WhatsApp 업데이트를 수락할 때까지 Cloud API 비즈니스에 메시지를 보낼 수 없다는 것이 명확히 안내됩니다. 또한, 앱을 등록하거나 재등록하는 사용자에게는 WhatsApp 업데이트를 수락하라는 메시지가 표시됩니다.

사용자가 업데이트를 수락하면 Cloud API 비즈니스와 채팅할 때 기존의 Cloud API 시스템 메시지 알림이 표시됩니다.

### 2024년 5월: 사용자별 마케팅 템플릿 메시지 제한 {#may-2024-per-user-marketing-template-message-limits}
*최종 업데이트: 2024년 5월*

Meta는 WhatsApp 플랫폼에서 고품질 사용자 경험을 유지하고 마케팅 템플릿 메시지의 참여를 극대화하기 위한 새로운 접근 방식을 도입하고 있습니다. 2024년 5월 23일부터, 특정 기간 동안 각 개별 사용자가 상호작용하는 모든 비즈니스로부터 받을 수 있는 마케팅 템플릿 메시지 수를 제한하며, 읽힐 가능성이 낮은 소수의 대화부터 시작합니다. 이 제한은 해당 사용자가 어떤 비즈니스로부터든 이미 받은 마케팅 템플릿 메시지 수에 따라 결정되며, 특정 브랜드와 관련된 것은 아닙니다. 그러나 이는 마케팅 템플릿 메시지의 전달 가능성에 영향을 미칠 수 있습니다.

이 제한은 일반적으로 새로운 마케팅 대화를 시작하는 마케팅 템플릿 메시지에만 적용됩니다. 브랜드와 WhatsApp 사용자 간에 이미 마케팅 대화가 열려 있는 경우, 해당 사용자에게 전송된 마케팅 템플릿 메시지는 영향을 받지 않습니다.

제한으로 인해 마케팅 템플릿 메시지가 특정 사용자에게 전달되지 않는 경우, Cloud API는 오류 코드 131026을 반환합니다. 다만, 이러한 오류 코드는 메시지 미전달을 초래할 수 있는 다양한 문제를 포함하며, 개인정보 보호를 위해 Meta는 실제로 제한으로 인해 메시지가 전달되지 않았는지 여부를 공개하지 않습니다. 미전달 사유에 대한 설명과 근본 원인을 파악하는 방법은 Cloud API의 [문제 해결 문서](https://developers.facebook.com/docs/whatsapp/cloud-api/support#troubleshooting)를 참조하세요.

이러한 오류 코드를 받은 경우 제한 때문일 수 있다고 판단되면, 템플릿 메시지를 즉시 재전송하지 마세요. 또 다른 오류 응답만 초래할 것입니다.

이 전달 가능성 업데이트에 대한 자세한 내용, 전달 가능성 모니터링 방법 및 WhatsApp 마케팅 메시징의 기타 모범 사례에 대해서는 최근 [블로그 게시물](https://www.braze.com/resources/articles/meta-introduces-deliverability-updates-for-whatsapp?utm_campaign=fy25-q2-global-customer-customer-meta-deliverability-updates-for-whatsapp&utm_medium=email-cdb&utm_source=braze&utm_content=blog-meta-deliverability-updates-for-wa-blog)을 참조하세요.

### 2024년 4월: 유틸리티 템플릿에 대한 템플릿 페이싱 {#april-2024-template-pacing-for-utility-templates}
*최종 업데이트: 2024년 4월*

작년에 WhatsApp은 비즈니스가 템플릿 참여를 개선하고 가치 있는 사용자 경험을 만들 수 있도록 마케팅 메시지에 대한 템플릿 페이싱을 도입했습니다. 4월 30일부터 템플릿 페이싱이 유틸리티 메시지로 확대됩니다. 계정의 유틸리티 템플릿이 사용자 피드백으로 인해 일시 중지되면, 향후 7일간 해당 계정에 대해 생성되는 새로운 유틸리티 템플릿에 페이싱이 적용됩니다.

### 2024년 4월: 열람율이 마케팅 템플릿의 품질 등급에 영향 {#april-2024-read-rates-will-affect-quality-rating-for-marketing-templates}
*최종 업데이트: 2024년 3월*

WhatsApp은 인도의 소비자를 시작으로 더 가치 있는 경험을 만들고 비즈니스의 마케팅 대화에 대한 참여를 극대화하기 위한 새로운 접근 방식을 테스트하고 있습니다. 여기에는 특정 기간 동안 소비자가 어떤 비즈니스로부터든 받는 마케팅 대화 수를 제한하는 것이 포함될 수 있으며, 읽힐 가능성이 낮은 소수의 대화부터 시작합니다. 메시지가 전달되지 않는 경우 Braze는 오류 코드를 받게 됩니다.

WhatsApp은 차단 및 신고와 같은 기존 측정기준 외에 열람율을 마케팅 템플릿의 품질 등급에 포함하기 시작합니다. WhatsApp은 2024년 4월 1일부터 볼륨을 확대하기 전에 가장 낮은 참여를 보이는 템플릿을 개선할 시간을 주기 위해 열람율이 낮은 마케팅 메시지 Campaign을 일시적으로 중지할 수 있습니다.

### 2024년 2월: 마케팅 대화 실험 {#february-2024-marketing-conversations-experimentation}
*최종 업데이트: 2024년 2월*

2024년 2월 6일부터, WhatsApp은 인도의 소비자를 시작으로 더 가치 있는 경험을 만들고 브랜드의 마케팅 대화에 대한 고객 참여를 극대화하기 위한 새로운 접근 방식을 테스트하고 있습니다. 여기에는 특정 기간 동안 사용자가 브랜드로부터 받는 마케팅 대화 수를 제한하는 것이 포함될 수 있으며, 읽힐 가능성이 낮은 소수의 대화부터 시작합니다.

### 2023년 10월: 템플릿 페이싱 {#october-2023-template-pacing}
*최종 업데이트: 2023년 10월*

2023년 10월 12일부터, WhatsApp은 마케팅 메시지에 대해 "템플릿 페이싱"이라는 개념을 도입합니다. 전체 Campaign 오디언스에게 동시에 메시지를 보내는 대신, "템플릿 페이싱"은 먼저 소규모 사용자 하위 집합에게 메시지를 전달하여 Campaign 수신자로부터 실시간 피드백을 수집한 후 나머지 메시지를 전송합니다.

"페이스 제한"(처음 전송되는 메시지의 하위 집합)은 템플릿에 따라 가변적입니다. 초기 전송 후, WhatsApp은 나머지 메시지를 최대 30분간 보류합니다. 이 보류 기간 동안 고객 피드백을 기반으로 템플릿의 품질을 평가합니다. 피드백이 긍정적이어서 고품질 템플릿임을 나타내면 나머지 메시지를 전달합니다. 피드백이 부정적이면 미전달된 나머지 메시지를 삭제하여 더 많은 고객으로부터의 추가적인 부정적 피드백을 방지하고 잠재적인 품질 제재 문제(예: 전화번호 품질 등급 영향)를 피하는 데 도움을 줍니다.

WhatsApp은 템플릿 페이싱에서 템플릿 품질을 평가하는 데 템플릿 일시 중지와 동일한 시스템을 사용합니다. 따라서 템플릿 페이싱 중 미전달된 메시지(저품질 템플릿으로 인한)는 더 큰 규모에서 일시 중지되었을 동일한 메시지입니다.

궁극적으로, 이 업데이트는 더 빠른 피드백 루프(템플릿 일시 중지의 수 시간 또는 수 일 대비 30분)를 제공하여, 템플릿을 조정하고 더 나은 고객 경험을 제공할 수 있도록 합니다.

**이 업데이트에 대해 추가 질문이 있으시면 Meta 파트너 담당자에게 문의하세요.**

### 2023년 6월: 메시징 실험 {#june-2023-messaging-experimentation}
*최종 업데이트: 2023년 6월*

2023년 6월 14일부터, Meta는 마케팅 메시지가 소비자 경험과 참여에 미치는 영향을 평가하기 위해 WhatsApp 플랫폼에 새로운 실험 방식을 도입합니다. 이 실험은 Braze를 통한 WhatsApp Business API에서 전송되는 마케팅 메시지에 영향을 미칠 수 있습니다.

Meta는 WhatsApp 플랫폼에서 이러한 실험을 계속할 예정입니다. 자세한 내용은 [Meta의 설명서](https://developers.facebook.com/docs/whatsapp/on-premises/guides/experiments?content_id=86oue5PtwEgcBJl)를 참조하세요.

**WhatsApp 실험은 마케팅 메시지에만 영향을 미칩니다.** 이 실험은 마케팅 템플릿 메시지의 전달에 영향을 미칠 수 있습니다. 유틸리티 및 인증 템플릿은 실험의 영향 없이 계속 전달됩니다.

실험에서 Meta는 WhatsApp 소비자의 약 1%를 참가자로 무작위 선정합니다. 선정된 경우, 다음 조건 중 하나가 충족되지 않는 한 Meta는 해당 소비자에게 마케팅 메시지 템플릿을 전달하지 않습니다:

- 소비자가 지난 24시간 이내에 회신한 경우
- 기존 마케팅 대화가 열려 있는 경우
- 소비자가 지난 72시간 이내에 WhatsApp 광고를 클릭한 경우

## 자주 묻는 질문 {#faq}

### Meta의 실험으로 인해 마케팅 메시지가 영향을 받았는지 어떻게 알 수 있나요? {#how-will-i-know-if-my-marketing-message-was-impacted-by-metas-experiment}

실험으로 인해 메시지가 전달되지 않은 경우, 활동 로그 및 Currents에서 특정 오류 코드가 표시됩니다. 해당 메시지는 실패로 집계되며 Braze 대시보드의 모든 보고서에서 WhatsApp 실패 측정기준에 포함됩니다. 이러한 메시지에 대해서는 요금이 부과되지 않습니다.

이 130472 오류 코드는 "User's number is part of an experiment."라고 표시됩니다. WhatsApp Cloud API 오류 코드에 대한 자세한 내용은 [Meta의 설명서](https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes?content_id=8SJRLBEjYGvXO9k)를 참조하세요.

### Meta의 실험에서 옵트아웃할 수 있나요? {#can-i-opt-out-of-metas-experiment}

아니요, Meta는 실험 옵트아웃을 허용하지 않습니다. 모든 WhatsApp Business API 제공업체 및 사용자는 이 Meta 실험의 대상입니다.

### 나중에 템플릿을 다시 발송해 볼 수 있나요? {#can-i-try-to-resend-a-template-later}

이 실험에는 정해진 기간이 없습니다. 따라서 소비자는 계속 실험 대상이 될 수 있습니다.

### Meta의 실험으로 인해 마케팅 메시지가 전달되지 않으면 어떻게 해야 하나요? {#what-can-i-do-if-my-marketing-messages-are-not-delivered-due-to-metas-experiment}

이메일, SMS, 푸시 알림 또는 인앱 메시지와 같은 다른 Braze 채널을 사용하여 의도한 사용자에게 유사한 콘텐츠의 메시지를 발송하는 것을 권장합니다.