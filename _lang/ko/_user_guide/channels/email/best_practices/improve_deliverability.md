---
nav_title: 이메일 전달 가능성
article_title: 이메일 전달 가능성 개선
page_order: 6
page_type: reference
description: "이 참조 문서에서는 마케팅 이메일이 스팸 폴더에 도달하는 이유와 발송 패턴, 메시지 콘텐츠, 수신자 동작이 받은편지함 배치에 미치는 영향을 설명합니다."
channel: email

---

# 이메일 전달 가능성 개선

> 메일박스 공급자(MBP)는 메시지를 수락하거나 반송할 때 발송 도메인의 평판을 고려합니다. 메시지가 수락되더라도 받은편지함에 배치되지 않는 경우가 있습니다. 대신 스팸 폴더로 라우팅될 수 있으며, 이 경우 수신자가 메시지를 확인할 가능성이 낮아집니다.

다음은 스팸 폴더 배치와 낮은 참여를 줄이기 위한 일반적인 가이드입니다.

## 발송 패턴

발송 패턴은 도메인 평판에 영향을 미칩니다. 다음 모범 사례와 맞지 않으면 MBP가 메일을 반송하거나 필터링할 가능성이 높아집니다.

- **고품질 가입자 데이터를 수집하세요.** 유효한 주소를 수집하고, 명확한 문구와 함께 자발적 옵트인을 사용하며, 확인 옵트인 또는 유효성 검사 서비스를 고려하여 가입자가 무엇에 가입하는지 알 수 있도록 하세요. 가입 흐름을 명확하고 사기성 가입에 강하게 설계하세요.
- **콘텐츠와 빈도에 대한 기대를 설정하고 준수하세요.** 가입자가 동의하지 않은 제품이나 발송 주기로 메일을 보내지 마세요.
- **가입자가 열어보고 상호작용하고 싶은 메일을 보내세요.** 스케줄을 잡기 전에 각 발송이 어떤 가치를 제공하는지 먼저 생각해 보세요.
- **최근에 옵트인했거나 참여한 수신자를 우선시하세요** (열기, 클릭, 웹사이트 활동이 기록된 사용자 등). 비활성 주소에 반복적으로 메일을 보내는 것을 피하세요.
- **트랜잭션 메일과 마케팅 메일을 분리하세요.** 많은 인터넷 서비스 공급자(ISP)는 트랜잭션 메일과 마케팅 메일을 다르게 처리합니다. 적절한 경우 두 가지를 분리하세요. 예를 들어, 별도의 발신자 이메일 주소만으로도 충분한 분리가 될 수 있습니다.

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

## 메시지 콘텐츠

콘텐츠 필터는 MBP가 피싱, 멀웨어, 원치 않는 메일로부터 사용자를 보호하는 데 도움을 줍니다. 크리에이티브가 무해해 보일 수 있지만, 필터가 감시하는 패턴과 유사할 수 있습니다.

- **메시지의 최근 변경 사항을 검토하세요.** 예를 들어, HTML, 이미지 비율, 이미지 호스트의 변경 및 새 템플릿의 포함은 MBP 콘텐츠 필터를 트리거할 수 있습니다.
- **참여가 떨어지면 템플릿과 카피를 새롭게 바꾸세요.** 오래되고 반복적인 발송은 가입자에게 열어볼 이유를 거의 주지 못합니다.

## 수신자 신고 및 동작

가입자의 행동은 평판 시스템과 향후 받은편지함 결정에 모두 영향을 미칩니다. 높은 불만 건수는 이후 메시지를 스팸으로 전환할 수 있으며, 이는 MBP 또는 가입자가 메일의 품질을 신뢰하지 않을 때 격리와 같은 역할을 합니다.

- **관련성 있는 제목란과 명확한 행동 유도 문구가 포함된 본문 콘텐츠를 작성하세요.** 열지 않고 삭제하는 것, 낮은 참여, 약한 제목란은 본문을 읽기 전에 이미 무관심을 나타내는 신호입니다.
- **옵트인 시점에 가입자에게 발신자 주소를 이메일 연락처 목록에 추가하도록 요청하세요.** 이렇게 하면 발신자 평판이 향상되고 메일이 받은편지함에 도달할 가능성이 높아집니다.

## 관련 리소스

- [일몰 정책]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies/)
- [IP 워밍]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/)
- [전달 가능성 함정 및 스팸 트랩]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps/)
- [발송 전 알아야 할 사항]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/know_before_you_send/#general)
- [동의 및 주소 수집]({{site.baseurl}}/user_guide/channels/email/email_setup/consent_and_address_collection/#subscriber-states)
- [이메일 FAQ]({{site.baseurl}}/user_guide/channels/email/faq/#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address)