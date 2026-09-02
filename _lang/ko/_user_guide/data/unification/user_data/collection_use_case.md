---
nav_title: 수집 사용 사례
article_title: 수집 사용 사례
page_order: 3
page_type: reference
description: "이 참조 문서에서는 차량 공유 앱에서 수집할 사용자 데이터를 결정하는 방법에 대한 사용자 데이터 수집 사용 사례를 다룹니다."

---

# 수집 사용 사례 {#collection-use-case}

> 이 문서에서는 차량 공유 앱이 어떤 사용자 데이터를 수집할지 결정하는 방법에 대한 사용자 데이터 수집 사용 사례를 다룹니다.

StyleRyde라는 택시 또는 차량 공유 앱이 어떤 사용자 데이터를 수집할지 결정하려고 한다고 가정해 보겠습니다. 다음 질문과 브레인스토밍 프로세스는 마케팅 및 개발 팀이 따라야 할 훌륭한 모델입니다. 이 연습이 끝나면 두 팀 모두 목표를 달성하기 위해 어떤 커스텀 이벤트와 속성을 수집하는 것이 적합한지 확실히 이해하게 될 것입니다.

## 사례 질문 1: 목표는 무엇인가요? {#case-question-1-what-is-the-goal}

StyleRyde의 목표는 간단합니다. 사용자가 앱을 통해 택시를 호출하도록 하는 것입니다.

## 사례 질문 2: 앱 설치 후 해당 목표에 도달하기 위한 단계는 무엇인가요? {#case-question-2-what-are-the-steps-to-reach-that-goal-after-app-installation}

1. StyleRyde는 사용자가 등록 프로세스를 시작하고 개인 정보를 입력해야 합니다.
2. StyleRyde는 사용자가 단문 메시지 서비스를 통해 받은 코드를 앱에 입력하여 등록 프로세스를 완료하고 인증해야 합니다.
3. StyleRyde는 사용자가 택시를 호출하도록 해야 합니다.
4. StyleRyde는 사용자가 택시를 호출할 때 이용 가능해야 합니다.

이러한 액션은 다음과 같은 커스텀 이벤트로 태그할 수 있습니다:

- Began Registration
- Completed Registration
- Successful Taxi Hails
- Unsuccessful Taxi Hails

이벤트를 구현한 후 StyleRyde는 다음과 같은 Campaigns를 실행할 수 있습니다:

1. Began Registration을 했지만 일정 기간 내에 Completed Registration을 하지 않은 사용자에게 메시지를 보냅니다.
2. Completed Registration을 완료한 사용자에게 축하 메시지를 보냅니다.
3. Unsuccessful Taxi Hails를 경험한 후 일정 시간 내에 Successful Taxi Hail이 이어지지 않은 사용자에게 사과 메시지와 프로모션 크레딧을 보냅니다.
4. Successful Taxi Hails가 많은 파워 사용자에게 로열티에 대한 감사의 의미로 프로모션을 보냅니다.

## 사례 질문 3: 메시징에 활용할 수 있는 다른 사용자 정보에는 어떤 것이 있을까요? {#case-question-3-what-other-user-information-could-we-collect-and-use-to-inform-our-messaging}

- 사용자에게 프로모션 크레딧이 있는지 여부
- 사용자가 드라이버에게 부여한 평균 평점
- 사용자별 고유 프로모션 코드

이러한 특성은 다음과 같은 커스텀 속성으로 태그할 수 있습니다:

- 프로모션 크레딧 잔액 (소수점 유형)
- 평균 드라이버 평점 (정수 유형)
- 고유 프로모션 코드 (문자열 유형)

이러한 속성을 활용하면 다음과 같은 Campaign을 사용자에게 보낼 수 있습니다:

1. 7일 동안 앱을 사용하지 않았으며 계정에 프로모션 크레딧이 남아 있는 사용자에게 앱으로 돌아와 크레딧을 사용하도록 리마인더를 보냅니다.
2. 메시지 템플릿과 [개인화 기능]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize)을 사용하여 고유 프로모션 코드 속성을 사용자에게 전달하는 메시징에 삽입합니다.

{% alert important %}
Braze는 세션이 5,000,000개 이상이거나, 고유 커스텀 이벤트 이름이 20,000개 이상이거나, 구매 내 고유 제품 이름이 20,000개 이상인 고객 프로필("더미 사용자")을 차단합니다. 이는 일반적으로 잘못된 통합의 결과이기 때문입니다. 프로필이 차단되면 Braze는 SDK와 REST API 모두에서 해당 프로필에 대한 모든 인바운드 데이터 수집을 중단합니다. 정상적인 사용자에게 이러한 상황이 발생한 경우, Braze 계정 매니저에게 문의하세요.
{% endalert %}