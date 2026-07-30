---
nav_title: "사용자 옵트인 수집"
article_title: 사용자 SMS 옵트인 수집 모범 사례
page_order: 3
description: "이 참조 문서에서는 사용자 옵트인을 수집하기 위한 세 가지 모범 사례를 다룹니다."
page_type: reference
channel:
  - SMS

---

# 사용자 옵트인 수집 {#collect-user-opt-ins}

> 다음 문서에서는 일반적인 SMS 옵트인 방법을 소개합니다.

## 옵션 1: 사용자에게 숏 코드 또는 긴 코드로 문자를 보내도록 요청 {#option-1-ask-users-to-text-your-short-or-long-code}

사용자에게 "START", "UNSTOP", "YES" 또는 커스텀 옵트인 키워드를 귀하의 번호로 문자 전송하도록 요청하면 자동으로 구독 그룹에 추가됩니다. 웹사이트, 모바일 앱, 또는 광고에서 사용자에게 이 방법으로 옵트인하도록 안내할 수 있으며, 필요하다면 인센티브를 제공할 수도 있습니다.

## 옵션 2: 인앱 메시지를 통한 사용자 옵트인 {#option-2-users-opt-in-via-in-app-message}

사용자가 인앱 메시지를 통해 SMS에 옵트인할 수 있도록 하려면, Braze에서 제공하는 [전화번호 수집 양식]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/phone_number_capture)을 사용하여 전화번호를 수집하고 SMS 목록을 확장할 수 있는 브랜드 양식을 만드세요.

![전화번호 수집 템플릿이 적용된 인앱 메시지 작성기.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%;"}

Braze에서는 [SMS 이중 옵트인]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) 기능도 함께 사용하는 것을 권장합니다. 이 기능은 인앱 메시지 전화번호 수집 양식과 자동으로 연동되어, 사용자가 양식을 통해 전화번호를 제출한 후 의도를 확인하도록 안내합니다.

## 옵션 3: 가입 흐름 {#option-3-sign-up-flow}

새로운 사용자가 웹사이트 또는 앱에서 가입하거나 등록할 때, 전화번호와 이메일을 요청합니다. 프로모션 이메일 및 SMS 수신에 동의하는 체크박스를 포함합니다.

사용자가 가입한 후 다음을 수행합니다:

1. [`/subscription/status/set` 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)를 사용하여 사용자를 생성하고 속성을 저장합니다.

{% raw %}
```http
POST 'https://rest.iad-03.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "xyz-abcd-1234567",
  "subscription_state": "subscribed",
  "external_id": "external_identifier",
  "phone": "+12223334444",
  "use_double_opt_in_logic": true
}
'
```
{% endraw %}

{: start="2"}
2. [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)를 사용하여 사용자를 SMS에 구독시킵니다.

{% raw %}
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "external_identifier",
      "phone": "+12223334444",
      "subscription_groups": [
        {
          "subscription_group_id": "xyz-abcd-1234567",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}'
```
{% endraw %}

{% alert note %}
REST API를 통해 구독할 때 사용자를 [SMS 이중 옵트인]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) 워크플로에 진입시키려면, 요청에서 `use_double_opt_in_logic`을 `true`로 설정합니다. 이 파라미터는 [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status), [`/v2/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2), [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)에서 지원됩니다.
<br><br>
REST API를 통한 구독 업데이트는 환영 메시지를 자동으로 트리거하지 않습니다. 환영 메시지를 보내려면 [구독 그룹 상태 업데이트]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#update-subscription-group-status) 트리거를 사용하여 액션 기반 Campaign을 생성하고 업데이트 소스를 **REST API**로 설정합니다.
{% endalert %}