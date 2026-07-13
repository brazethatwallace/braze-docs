# 활용 사례: 예약 알림 이메일 시스템 {#use-case-booking-reminder-email-system}

> Braze는 프로그래밍 방식으로 높은 수준의 제어가 가능하도록 설계된 종합 고객 참여 플랫폼입니다. 이 활용 사례에서는 예약 시스템과 같이 제품과 마케팅의 교차점에 있는 사용 사례에 연결할 수 있는 Braze의 기능을 몇 가지 소개합니다.

이 활용 사례에서는 Braze 기능을 사용하여 예약 알림 이메일 메시징 서비스를 구축하는 방법을 보여줍니다. 이 서비스를 통해 사용자는 약속을 예약할 수 있으며, 다가오는 약속에 대한 알림 메시지를 받게 됩니다. 이 활용 사례에서는 이메일 메시지를 사용하지만, 고객 프로필에 대한 단일 업데이트를 기반으로 하나 또는 여러 채널을 통해 메시지를 보낼 수 있습니다.

이 서비스를 구축하면 다음과 같은 추가 이점이 있습니다:
- 전송된 메시지에 대한 전체 추적 및 보고가 가능합니다.
- 비기술 직군의 회사 사용자도 메시지 콘텐츠를 업데이트할 수 있습니다.
- 메시지는 Campaign 구성에 따라 고객 프로필의 옵트인 및 옵트아웃 상태를 준수합니다.
- 예약 데이터와 메시지 상호작용 데이터를 모두 사용하여 추가 메시징을 위해 사용자를 세분화하고 타겟팅할 수 있습니다. 예를 들어, 초기 알림 메시지를 열지 않은 사용자에게 약속 전에 추가 알림을 리타겟할 수 있습니다.

이 활용 사례를 구현하려면 다음 단계를 따르세요:
1. [Braze 고객 프로필에 다가오는 예약 데이터 기록하기](#step-1)
2. [예약 알림 메시지 설정 및 시작하기](#step-2)
3. [업데이트된 예약 및 취소 처리하기](#step-3)

## 1단계: Braze 고객 프로필에 다가오는 예약 데이터 기록하기 {#step-1}

예약이 발생할 때마다 Braze [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) 엔드포인트를 사용하여 고객 프로필에 [중첩 고객 속성]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support)을 기록합니다. 중첩 고객 속성에 알림 메시지를 전송하고 개인화하는 데 필요한 모든 정보가 포함되어 있는지 확인하세요. 이 활용 사례에서는 중첩 고객 속성의 이름을 "trips"로 지정합니다.

### 예약 추가 {#add-booking}

사용자가 예약을 생성하면, `/users/track` 엔드포인트를 통해 Braze에 데이터를 전송하기 위해 다음과 같은 오브젝트 배열 구조를 사용합니다.

{% raw %}
```json
{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": [
               {"trip_id":"1","name":"London Trip","start_date"{$time:"2025-11-11"}},
               {"trip_id":"2","name":"Sydney Trip","start_date"{$time:"2025-11-11"}}
           ]
       }
   ]
}
```
{% endraw %}

중첩 고객 속성 "trips"는 고객 프로필에 다음과 같이 표시됩니다.

![런던 여행과 시드니 여행에 대한 두 개의 중첩 고객 속성.]({% image_buster /assets/img/use_cases/2_nested_attributes.png %}){: style="max-width:70%;"}

### 예약 업데이트 {#update-booking}
사용자가 예약을 업데이트하면, `/users/track` 엔드포인트를 통해 Braze에 데이터를 전송하기 위해 다음과 같은 오브젝트 배열 구조를 사용합니다.

{% raw %}
```json
{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": {
               "$update:":[
                   {
                       "$identifier_key":"trip_id",
                       "$identifier_value":"1",
                       "$new_object":{"trip_id":"1","name":"London Trip","start_date":{"$time":"2025-11-11"}}
                   }
               ]
           }
       }
 ]
}
```
{% endraw %}

### 예약 제거 {#remove-booking}

{% tabs %}
{% tab /users/track endpoint %}
#### `/users/track` 엔드포인트를 통해 데이터 전송 {#send-data-through-the-userstrack-endpoint}
사용자가 예약을 삭제하면, `/users/track` 엔드포인트를 통해 Braze에 데이터를 전송하기 위해 다음과 같은 오브젝트 배열 구조를 사용합니다.

{% raw %}
```json

{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": {
               "$remove:":[
                   {
                       "$identifier_key":"trip_id",
                       "$identifier_value": "1"
                   }
               ]
           }
       }
   ]
}
```
{% endraw %}
{% endtab %}
{% tab SDK %}
#### SDK를 통해 고객 프로필에 중첩 속성 기록하기 {#write-nested-attributes-to-user-profiles-through-the-sdk}

앱, 웹사이트 또는 둘 다를 통해 예약을 수집하고 해당 데이터를 고객 프로필에 직접 기록하려면 Braze SDK를 사용하여 이 데이터를 전송할 수 있습니다. 다음은 웹 SDK를 활용한 예시입니다:

{% raw %}
```json
const json = [{
  "id": 1,
  "name": "London Trip",
  "start_date": {"$time”: “2025-05-08”}
}, {
  "id": 1,
  "name": "Sydney Trip",
  "start_date": {"$time”: “2025-11-11”}
}];
braze.getUser().setCustomUserAttribute("trips", json);
```
{% endraw %}
{% endtab %}
{% endtabs %}

Braze는 고객 프로필의 중첩 고객 속성에서 지정된 예약을 제거하고 남아 있는 예약을 표시합니다.

![런던 여행에 대한 중첩 고객 속성.]({% image_buster /assets/img/use_cases/1_nested_attribute.png %}){: style="max-width:70%;"}

## 2단계: 예약 알림 메시지 설정 및 시작하기 {#step-2}

### 2a단계: 타겟 오디언스 생성 {#step-2a-create-a-target-audience}
다중 기준 세분화를 사용하여 알림을 받을 타겟 오디언스를 생성합니다. 예를 들어, 예약 날짜 이틀 전에 알림을 보내려면 다음을 선택합니다:

- 시작 날짜가 **1일 이상** 그리고
- 시작 날짜가 **2일 미만**

![시작 날짜가 1일 이상이고 2일 미만인 기준을 가진 중첩 고객 속성 "trips".]({% image_buster /assets/img/use_cases/custom_nested_attribute.png %})

### 2b단계: 메시지 작성하기 {#step-2b-create-your-message}

[커스텀 HTML로 이메일 만들기]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor)의 단계를 따라 알림 이메일 메시지를 작성합니다. Liquid를 사용하여 생성한 커스텀 고객 속성("trips")의 데이터로 메시지를 개인화합니다. 다음 예시를 참고하세요.

{% raw %}
```liquid
{% assign dates = {{custom_attribute.${trips}}} %}
{% assign today = "now" | date: "%s" %}
{% assign two_days = today | plus: 172800 | date: "%F" %}
You have the following booked in 2 days! Check the information below:
{% for date in dates %}
{% if date.start_date == two_days %}
{{date.trip_id}}
{{date.name}}
{% endif %}
{% endfor %}
```
{% endraw %}

### 2c단계: Campaign 시작하기 {#step-2c-launch-your-campaign}

알림 이메일 메시지 Campaign을 시작합니다. 이제 Braze가 "trips" 커스텀 속성을 수신할 때마다, 해당 예약 오브젝트에 포함된 데이터에 따라 메시지를 스케줄합니다.

## 3단계: 업데이트된 예약 및 취소 처리하기 {#step-3}

이제 알림 메시지를 보내고 있으므로, 예약이 업데이트되거나 취소될 때 전송할 확인 메시지를 설정할 수 있습니다.

### 3a단계: 업데이트된 데이터 전송 {#step-3a-send-updated-data}

{% tabs %}
{% tab /users/track %}

#### `/users/track` 엔드포인트를 통해 데이터 전송
사용자가 예약을 업데이트하거나 취소할 때 커스텀 이벤트를 전송하기 위해 Braze [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) 엔드포인트를 사용합니다. 해당 이벤트에서 변경 사항을 확인하는 데 필요한 데이터를 이벤트 등록정보에 포함합니다.

이 활용 사례에서 사용자가 시드니 여행 날짜를 업데이트했다고 가정해 보겠습니다. 이벤트는 다음과 같습니다:

{% raw %}
```json
{
  "events": [
    {
      "external_id": "user_id",
      "name": "trip_updated",
      "time": "2025-03-07T08:19:23+01:00",
      "properties": {
        "id": 2,
        "name": "Sydney Trip",
        "old_time": "2025-11-12"
        "new_time": "2026-01-21"
      }
    }
  ]
}
```
{% endraw %}
{% endtab %}
{% tab SDK %}

#### SDK를 통해 고객 프로필에 커스텀 이벤트 전송하기

SDK를 통해 고객 프로필에 커스텀 이벤트를 전송합니다. 예를 들어, 웹 SDK를 사용하고 있다면 다음과 같이 전송할 수 있습니다:

{% raw %}
```json
braze.logCustomEvent("trip_updated", {
  id: 2,
  name: "Sydney Trip",
  old_time: "2025-11-12",
  new_time: "2026-01-21"
});
```
{% endraw %}
{% endtab %}
{% endtabs %}

### 3b단계: 업데이트 확인 메시지 작성하기 {#step-3b-create-a-message-to-confirm-the-update}

사용자에게 업데이트된 예약 확인을 보내기 위해 [행동 기반 Campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery)을 생성합니다. [Liquid를 사용하여 이벤트 등록정보를 템플릿화]({{site.baseurl}}/user_guide/data/custom_data/custom_events)하면 예약의 이름, 이전 시간, 새로운 시간(취소인 경우 이름만)을 메시지에 반영할 수 있습니다.

예를 들어, 다음과 같은 메시지를 작성할 수 있습니다:

{% raw %}
```liquid
Hi {{${first_name}}}, you have successfully updated the date of your trip, {{event_properties.${name}}}, from {{event_properties.${old_time}}} to {{event_properties.${new_time}}}
```
{% endraw %}

### 3c단계: 업데이트를 반영하도록 고객 프로필 수정하기 {#step-3c-modify-the-user-profile-to-reflect-the-update}

마지막으로, 1단계와 2단계의 예약 알림을 최신 데이터에 기반하여 전송하려면 중첩 고객 속성을 업데이트하여 예약의 변경 또는 취소를 반영해야 합니다.

#### 업데이트된 예약 {#updated-booking}

이 활용 사례에서 사용자가 시드니 여행을 업데이트한 경우, `/users/track` 엔드포인트를 사용하여 다음과 같은 호출로 날짜를 변경합니다:

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "trips": {
	  "$update": [
	    {
            "$identifier_key": "id",
            "$identifier_value": 2,
            "$new_object": {
              "start_date": "2026-01-21"
            }
          }
        ]
      }
    }
  ]
}
```
{% endraw %}

#### 취소된 예약 {#cancelled-booking}

이 활용 사례에서 사용자가 시드니 여행을 취소한 경우, `/users/track` 엔드포인트에 다음 호출을 전송합니다:

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "trips": {
	  "$remove": [
	   {
            "$identifier_key": "id",
            "$identifier_value": 2
          }
         ]
      }
    }
  ]
}
```
{% endraw %}

이 호출이 전송되고 고객 프로필이 업데이트되면, 예약 알림 메시지는 사용자의 예약 날짜에 대한 최신 데이터를 반영합니다.