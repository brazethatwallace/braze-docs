---
nav_title: 메시지 추가 정보 태그
article_title: 메시지 추가 정보 태그
page_order: 1
description: "이 문서에서는 메시지 추가 정보 Liquid 태그를 사용하는 방법과 구문을 확인하는 방법을 설명합니다."
alias: "/message_extras_tag/"
---

# 메시지 추가 정보 Liquid 태그 {#message-extras-liquid-tag}

> `message_extras` Liquid 태그를 사용하여 연결된 콘텐츠, 카탈로그, 커스텀 속성(예: 언어, 국가), Canvas 진입 등록정보 또는 기타 데이터 소스의 동적 데이터로 발송 이벤트에 주석을 달 수 있습니다.

`message_extras` Liquid 태그는 Currents 및 Snowflake 데이터 공유의 해당 발송 이벤트에 키-값 페어를 추가합니다.

Currents 또는 Snowflake 데이터 공유 발송 이벤트에 동적 또는 추가 데이터를 다시 보내려면 메시지 본문에 적절한 Liquid 태그를 삽입하세요.

다음은 `message_extras`의 표준 Liquid 태그 형식 예시입니다:

{% raw %}
```liquid
{% message_extras :key test :value 123 %}
```
{% endraw %}

메시지 본문에서 키-값 페어에 필요한 만큼 이러한 태그를 추가할 수 있습니다. 그러나 모든 키와 값의 길이는 1,000바이트(1&nbsp;KB)를 초과하지 않아야 합니다. Currents 및 Snowflake 데이터 공유에서 발송 이벤트에 대해 `message_extras`라는 새 이벤트 필드를 확인할 수 있습니다. 이 필드는 하나의 필드에 JSON 직렬화된 문자열을 생성합니다.

## Currents를 사용하여 메시지 추가 정보 데이터를 보내는 방법 {#how-message-extras-data-is-sent-using-currents}

**메시지 추가 정보**는 발송 시점에 첨부되는 키-값 페어입니다. 구성은 채널에 따라 다릅니다. 이메일의 경우 헤더를 사용하여 추가됩니다. iOS 푸시의 경우 푸시 페이로드에 포함됩니다. 지원되는 모든 발송 이벤트는 메시지가 발송되면 Currents(및 Snowflake)에서 동일한 `message_extras` 필드를 표시합니다.

## 지원되는 채널 {#supported-channels}

`message_extras` 태그는 발송 이벤트가 있는 모든 메시지 유형과 인앱 메시지 노출 횟수 이벤트에서 지원됩니다. 인앱 메시지에서 `message_extras`를 사용하려면 특정 [최소 SDK 버전](#iam-sdk)을 충족해야 합니다.

## `message_extras` 태그 사용 방법 {#how-to-use-the-message_extras-tag}

1. 채널의 메시지 본문에 `message_extras` Liquid 태그를 입력합니다. 또는 **개인화 추가** 모달을 사용하여 개인화 유형으로 **Message Extras**를 선택할 수 있습니다.

![개인화 유형으로 Message Extras가 선택된 개인화 추가 모달.]({% image_buster /assets/img_archive/message_extras1.png %}){: style="max-width:35%;"}

{: start="2"}

2. 각 `message_extras` 태그에 대한 [키-값 페어]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs)를 입력합니다.

![메시지 추가 정보 태그의 키-값 페어 예시. 제목 필드에는 "Your New Favorites"라고 표시됩니다. 메시지에는 메시지 추가 정보 태그의 키-값 페어와 다음 문장이 표시됩니다: "We're excited to bring you a side selection of fresh and exciting products that are sure to become your new go-to favorites"]({% image_buster /assets/img_archive/message_extras2.png %}){: style="max-width:70%;"}

{: start="3"}

3. Campaign 또는 Canvas가 발송된 후, Braze는 Currents 또는 Snowflake 데이터 공유 발송 이벤트를 통해 발송 시점에 동적 데이터를 `message_extras` 필드에 첨부합니다.

## 구문 확인 {#checking-syntax}

위에서 설명한 태그 표준과 일치하지 않는 다른 입력은 Currents 또는 Snowflake로 전달되지 않을 수 있습니다. 구문이나 형식에 다음 사항이 포함되어 있지 않은지 확인하세요:

- 존재하지 않거나, 비어 있거나, 잘못 입력된 구분 기호
- 중복 키(Braze는 기본적으로 처음 발견된 키-값 페어를 발송합니다)
- 키 또는 값이 정의되기 전의 추가 텍스트
- 순서가 잘못된 키와 값
  - {% raw %}예: `{% message_extras :value 123 :key test %}`{% endraw %}

## Currents에 프로모션 코드 정보 보내기 {#sending-promotion-code-information-to-currents}

{% multi_lang_include partners/shopify.md section='Liquid promotion codes with Currents' %}

## 고려 사항 {#considerations}

- 1,000바이트(1&nbsp;KB)를 초과하는 키-값은 잘립니다.
- 공백은 문자 수에 포함됩니다. Braze는 앞뒤 공백을 생략합니다.
- 결과 JSON은 문자열 값만 출력합니다.
- Liquid 변수를 키 또는 값으로 포함할 수 있지만, `message_extras` 내부에 추가 Liquid 태그를 중첩할 수는 없습니다.
  - 예를 들어, 다음과 같은 Liquid를 사용할 수 있습니다: {% raw %}`{% assign value = '123' %} {% assign key = 'test' %} {% message_extras :key {{key}} :value {{value}} %}`{% endraw %}

## 자주 묻는 질문 {#frequently-asked-questions}

### 발송 이벤트의 message_extras 필드를 열기 및 클릭과 같은 참여 이벤트에 어떻게 연결할 수 있나요? {#how-can-i-associate-the-message_extras-field-in-the-send-events-to-my-engagement-events-like-opens-and-clicks}

`dispatch_id`가 생성되어 발송 이벤트에 제공되며, 이를 고유 식별자로 사용하여 특정 클릭, 열기 또는 전달 이벤트에 연결할 수 있습니다. Currents 또는 Snowflake에서 이 필드를 쿼리할 수 있습니다. 자세한 내용은 [Dispatch ID 동작]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id)을 참조하세요.

#### 인앱 메시지에서 message_extras를 사용할 수 있나요? {#iam-sdk}

네, 사용자의 기기가 다음 최소 SDK 버전을 충족하는 한 인앱 메시지에서 `message_extras`를 사용할 수 있습니다:

{% sdk_min_versions web:5.2.0 android:30.4.0 swift:8.4.0 %}