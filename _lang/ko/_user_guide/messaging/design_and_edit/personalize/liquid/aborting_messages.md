---
nav_title: 메시지 중단
article_title: Liquid 메시지 중단
page_order: 7
description: "이 참조 문서에서는 Liquid 메시지 중단과 몇 가지 사용 사례 예시를 다룹니다."

---

# 메시지 중단 {#abort-messages}

> 선택적으로 조건문 내에서 `abort_message("optional reason for aborting")` Liquid 메시지 태그를 사용하여 사용자에게 메시지가 발송되는 것을 방지할 수 있습니다. 이 참조 문서에서는 마케팅 Campaign(캠페인)에서 이 기능을 활용하는 몇 가지 예시를 소개합니다.

{% alert note %}
Canvas에서 메시지 단계가 중단되면 사용자는 Canvas를 **종료하지 않으며** 다음 단계로 **계속 진행합니다**.
{% endalert %}

## `abort_message()`를 사용한 테스트 발송 {#test-sends-with-abort_message}

`abort_message()`는 조건을 충족하지 않는 사용자에 대한 발송을 중지합니다. 해당 메시지는 사용자 프로필에 표시되지 않으며 전달 또는 최대 게재빈도 설정에 집계되지 않습니다.

테스트 발송이 도착하지 않는 경우, 중단 조건을 충족하는 사용자로 미리보기한 다음 **테스트 발송**에서 **현재 미리보기 사용자의 속성으로 수신자 속성 재정의**를 활성화하세요(또는 조건을 충족하는 콘텐츠 테스트 그룹 멤버를 추가하세요).

## "Number Games Attended" = 0인 경우 메시지 중단 {#abort-message-if-number-games-attended-0}

예를 들어, 경기에 참석하지 않은 고객에게는 메시지를 보내고 싶지 않다고 가정해 보겠습니다:

{% raw %}
```liquid
{% if custom_attribute.${Number_Game_Attended} == 1 %}
Loved the game? Get 10% off your second one with code SAVE10.
{% elsif custom_attribute.${Number_Game Attended} > 1 %}
Love the games? Get 10% off your next one with code SAVE10.
{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

이 메시지는 경기에 참석한 것으로 확인된 고객에게만 발송됩니다.

## 영어를 사용하는 고객에게만 메시지 보내기 {#message-english-speaking-customers-only}

고객의 언어가 영어인 경우에 일치하는 "if" 문과, 영어를 사용하지 않거나 프로필에 언어가 설정되지 않은 사용자에 대해 메시지를 중단하는 "else" 문을 만들어 영어를 사용하는 고객에게만 메시지를 보낼 수 있습니다.

{% raw %}
```liquid

{% if ${language} == 'en' %}
Send this message in English!
{% else %}
{% abort_message() %}
{% endif %}
```

기본적으로 Braze는 메시지 활동 로그에 일반적인 오류 메시지를 기록합니다:

```text
{% abort_message %} called
```

괄호 안에 문자열을 포함하여 중단 메시지가 메시지 활동 로그에 특정 내용을 기록하도록 할 수도 있습니다:

```liquid
{% abort_message('language was nil') %}
```
{% endraw %}

![개발자 콘솔의 메시지 오류 로그에 "language was nil"이라는 중단 메시지가 표시된 화면.]({% image_buster /assets/img_archive/developer_console.png %})

## 중단 메시지 쿼리 {#query-for-abort-messages}

[쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder) 또는 Braze에 연결된 데이터 웨어하우스를 사용하여 Liquid 로직으로 인해 메시지가 중단될 때 트리거되는 특정 중단 메시지를 쿼리할 수 있습니다.

## 중단 로직이 평가되는 시점 {#when-abort-logic-is-evaluated}

중단 로직 평가 시점은 메시지 채널에 따라 다릅니다.

### 푸시, 이메일, SMS, 웹훅, Content Cards {#push-email-sms-webhooks-and-content-cards}

중단 로직은 Braze가 전달을 위해 메시지를 처리하는 발송 시점에 평가됩니다.

### 인앱 메시지 {#in-app-messages}

중단 로직은 [템플릿 인앱 메시지]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#templated_iam-templated)에 한해 메시지가 처음 기기로 전송되는 시점이 아니라, 인앱 메시지가 트리거되는 시점(예: 사용자가 트리거 이벤트를 수행하거나 세션을 시작할 때)에만 평가됩니다. 인앱 메시지는 세션 시작 시 SDK로 전달되어 로컬에 캐시되며, `abort_message()` 호출을 포함한 Liquid는 트리거 조건이 충족될 때 실행됩니다.

## 고려 사항 {#considerations}

`abort_message()` Liquid 메시지 태그는 사용자에게 메시지가 발송되는 것을 방지합니다. 즉, 메시지가 고객 프로필에 표시되지 않으며 전달 또는 최대 게재빈도 설정에 집계되지 않습니다.