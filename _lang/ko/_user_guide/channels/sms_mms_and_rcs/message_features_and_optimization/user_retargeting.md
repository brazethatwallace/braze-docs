---
nav_title: "사용자 리타겟팅"
article_title: "사용자 리타겟팅"
description: "이 참조 문서에서는 사용자의 SMS 및 RCS 상호작용을 기반으로 메시지를 리타겟팅하는 방법을 다룹니다."
page_type: reference
page_order: 4
alias: /sms_mms_rcs_user_retargeting/
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS

---

# 사용자 리타겟팅 {#user-retargeting}

> Braze는 수신 키워드를 기반으로 사용자의 구독 상태를 변경하고 자동 응답을 보내는 것 외에도, 메시지 필터링 및 트리거를 위해 고객 프로필에 상호작용을 기록합니다.<br><br>이러한 필터와 트리거를 사용하면 SMS, MMS, RCS Campaign을 수신했거나 응답한 사용자를 기준으로 동작을 필터링하거나, 단축 URL을 클릭한 사용자와 추가로 인게이지먼트할 수 있습니다.

{% alert tip %}
커스텀 키워드와 이러한 리타겟팅 옵션을 활용하기 위한 양방향 메시징 설정 방법에 대해 자세히 알아보려면 [커스텀 키워드]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling) 문서를 참조하세요.
{% endalert %}

## 리타겟팅 옵션 {#retargeting-options}

{% alert note %}
사용자 리타겟팅으로 오디언스를 구축할 때, 사용자의 선호도에 따라 특정 사용자를 포함하거나 제외할 수 있으며, CUP에 따른 '판매 또는 공유 금지' 권리와 같은 개인정보 보호법을 준수해야 합니다. 마케터는 Canvas 및/또는 Campaign 진입 기준 내에서 사용자 자격에 대한 관련 필터를 구현해야 합니다.
{% endalert %}

### SMS, MMS, RCS로 사용자 필터링 {#filter-users-by-sms-mms-and-rcs}

사용자는 마지막으로 SMS, MMS 또는 RCS를 수신한 시점이나 특정 Campaign에서 SMS, MMS 또는 RCS를 수신했는지 여부를 기준으로 필터링할 수 있습니다. 필터는 캠페인 빌더의 **타겟 오디언스** 단계에서 설정할 수 있습니다.

{% alert note %}
메시지가 수신, 열람 또는 클릭되면, Braze는 상호작용을 기록한 프로필과 동일한 전화번호를 공유하는 모든 프로필의 데이터를 업데이트합니다. 메시지를 수신, 열람 또는 클릭한 사용자와 전화번호를 공유하는 사용자는 원래 Campaign에 포함되지 않았거나 메시지를 직접 수신하지 않았더라도 이 필터에 일치할 수 있습니다.
{% endalert %}

#### 마지막 SMS/MMS/RCS 수신 기준 필터링 {#filter-by-last-received-smsmmsrcs}

![2020년 12월 8일 이후 마지막으로 SMS를 수신한 세분화 필터.]({% image_buster /assets/img/sms/filter2.png %})

#### SMS/MMS/RCS Campaign에서 수신한 메시지 기준 필터링 {#filter-by-received-messages-from-smsmmsrcs-campaign}

특정 Campaign에서 메시지를 수신한 사용자를 필터링합니다. 이 필터를 사용하면 Campaign에서 메시지를 수신하지 않은 사용자를 필터링하는 옵션도 있습니다.

!['SMS 리타겟팅' Campaign에서 메시지를 수신한 세분화 필터.]({% image_buster /assets/img/sms/filter1.png %})

### 사용자가 SMS, MMS 또는 RCS를 수신할 때 메시지 트리거 {#trigger-messages}

사용자가 특정 Campaign에서 SMS, MMS 또는 RCS 메시지를 수신할 때 메시지를 트리거하려면, 행동 기반 Campaign의 트리거 동작으로 **Interact with Campaign**을 선택합니다. 그런 다음 **Receive SMS**와 사용하려는 SMS, MMS 또는 RCS Campaign을 선택합니다.

![사용자가 특정 Campaign에서 SMS, MMS 또는 RCS 메시지를 수신할 때 메시지를 트리거하려면, 행동 기반 Campaign의 트리거 동작으로 Interact with Campaign을 선택합니다. 그런 다음 Receive SMS와 사용하려는 SMS, MMS 또는 RCS Campaign을 선택합니다.]({% image_buster /assets/img/sms/trigger.png %})

### 고급 추적 링크로 필터링 {#filter-by-advanced-tracking-links}

[고급 추적 링크]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening)가 포함된 Campaign을 클릭한 사용자를 리타겟팅합니다.
고급 추적이 활성화된 Campaign만 다음 드롭다운에 표시됩니다:

#### 특정 SMS, MMS 또는 RCS Campaign을 클릭한 사용자 리타겟팅 {#retarget-users-who-have-clicked-a-specific-sms-mms-or-rcs-campaign}

1. **Clicked/Opened Campaign** 필터를 사용하여 Segment를 생성합니다.
2. **clicked shortened sms link**를 선택합니다.
3. 원하는 Campaign을 선택합니다.

![특정 SMS, MMS 또는 RCS Campaign을 클릭한 사용자를 리타겟팅하는 스크린샷.]({% image_buster /assets/img/sms/retargeting5.png %})

#### 특정 캔버스 단계를 클릭한 사용자 리타겟팅 {#retarget-users-who-have-clicked-a-specific-canvas-step}

1. **Clicked/Opened Step** 필터를 사용하여 Segment를 생성합니다.
2. **clicked shortened sms link**를 선택합니다.
3. 원하는 Canvas와 캔버스 단계를 선택합니다.

![특정 캔버스 단계를 클릭한 사용자를 리타겟팅하는 스크린샷.]({% image_buster /assets/img/keyword_example1.jpg %})

## 키워드 카테고리별 리타겟팅 {#keyword-category-specific-retargeting}

세 가지 기본 키워드 카테고리(옵트인, 옵트아웃, 도움말) 외에도 최대 25개의 자체 키워드 카테고리를 생성하여 임의의 키워드와 응답을 식별할 수 있습니다. 이러한 카테고리는 필터링 및 리타겟팅에 사용할 수 있습니다. 글로벌 키워드 카테고리와 설정 방법에 대해 자세히 알아보려면 [키워드 처리]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing)를 참조하세요.

### 최근성 기준 필터링 {#filter-by-recency}

사용자가 SMS, MMS 또는 RCS 프로그램에 응답한 최근성을 기준으로 필터링합니다. 이 필터는 사용자가 키워드 카테고리 중 하나에 해당하는 인바운드 메시지를 보낸 마지막 날짜를 평가합니다.

!['마케팅 SMS' 구독 그룹에 '옵트인' 키워드로 2020년 8월 11일 이후 마지막으로 SMS를 보낸 세분화 필터.]({% image_buster /assets/img/sms/retargeting1.png %})

### Campaign 또는 Canvas 기여도 기준 필터링 {#filter-by-campaign-or-canvas-attribution}

특정 SMS, MMS 또는 RCS Campaign이나 Canvas 구성요소, 키워드 카테고리 또는 태그에 응답한 사용자를 필터링합니다.

#### 키워드 카테고리로 특정 Campaign에 응답한 기준 필터링 {#filter-by-replied-to-a-specific-campaign-with-keyword-category}

!['SMS-283' Campaign '프로모션'에 대해 'SMS에 응답함' 필터가 있는 Campaign. 필터 아래에 '이 필터는 활성 Campaign에서 사용되지 않는 경우 "프로모션"에서 마지막 메시지가 발송된 후 25개월 후에 만료됩니다.'라는 안내가 표시됩니다.]({% image_buster /assets/img/sms/clicked_opened_campaign.png %})

#### 특정 태그가 있는 Campaign 또는 Canvas에 응답한 기준 필터링 {#filter-by-replied-to-a-campaign-or-canvas-with-a-specific-tag}

!['Curbside Messaging Service C' 태그가 있는 Campaign 또는 Canvas에 대해 'SMS에 응답함' 필터가 있는 Campaign.]({% image_buster /assets/img/sms/clicked_opened_campaign_canvas_tag.png %})

#### 특정 단계에 응답한 기준 필터링 {#filter-by-replied-to-a-specific-step}

!['SMS Double Opt' 'Step - Help'에 대해 'SMS에 응답함' 필터가 있는 Campaign.]({% image_buster /assets/img/sms/clicked_opened_step.png %})

### 키워드로 메시지 트리거 {#trigger-messages-by-keyword}

사용자가 키워드 카테고리(사용자가 키워드 중 하나를 보낸 경우) 또는 기타 키워드(사용자가 기존 카테고리에 해당하지 않는 키워드를 보낸 경우)를 기반으로 인바운드 메시지를 보낼 때 메시지를 트리거할 수 있습니다. 이러한 트리거는 캠페인 빌더의 전달 단계에서 설정됩니다.

인바운드 메시지가 정의된 트리거 이벤트에 해당하는지 평가할 때, 평가가 시작되기 전에 앞뒤 공백이 제거됩니다.

{% alert tip %}
인바운드 SMS 또는 MMS 메시지에 의해 행동 기반 Canvas가 트리거되는 경우, 다음 행동 경로까지 모든 캔버스 단계에서 [지원되는 SMS Liquid 속성]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)을 참조할 수 있습니다.
{% endalert %}

#### 인바운드 키워드 카테고리로 트리거 {#trigger-by-inbound-keyword-category}

!['마케팅 SMS' 구독 그룹에 '옵트인' 키워드를 보낸 세분화 필터가 있는 행동 기반 SMS Campaign.]({% image_buster /assets/img/sms/retargeting2.png %}){: style="margin-top:10px;"}

#### 임의 키워드로 트리거 {#trigger-by-arbitrary-keywords}

'기타' 키워드 응답으로 메시지를 트리거할 때, 키워드 본문을 정확한 텍스트 일치로 평가할 수 있습니다. 이 일치는 언급된 것과 동일한 규칙을 따릅니다: **정확한 단일 단어 메시지**만 처리됩니다(대소문자 *구분 없음*). `Hello Braze!`라는 키워드를 보낸 경우 다음 예시에 표시된 기준과 일치하지 않습니다.

![키워드 카테고리가 '기타'이고 메시지 본문이 정확히 'Hello' 또는 'Hey'인 행동 기반 SMS Campaign.]({% image_buster /assets/img/sms/retargeting3.png %}){: style="margin-top:10px;"}

#### 키워드 템플릿 {#template-keywords}

인바운드 SMS 또는 MMS에서 Campaign이나 Canvas 구성요소를 트리거할 때, 사용자가 보낸 텍스트 또는 미디어 첨부 파일을 Liquid를 사용하여 Campaign이나 Canvas 본문에 선택적으로 템플릿화할 수 있습니다. 이를 통해 사용자의 응답에 접근하여 답장에 포함하거나, 조건 로직을 적용하거나, Liquid로 할 수 있는 모든 작업을 수행할 수 있습니다.

{% raw %}

```liquid
Sorry, we didn't recognize {{sms.${inbound_message_body}}}. Text HELP for help or STOP to stop.
```

```liquid
{% if {{sms.${inbound_message_body}}} == "SNEAKERS" %}
OK, you're subscribed to updates on all our sneaker deals!
{% elsif {{sms.${inbound_message_body}}} == "SHIRTS" %}
Shirt deals coming up for you!
{% else %}
Want to receive a specific deal? Just text us the category you're interested in. For example SHIRTS or SNEAKERS.
{% endif %}
```

{% endraw %}

[16]: {% image_buster /assets/img/keyword_example1.jpg %}
[16]: {% image_buster /assets/img/sms/retargeting4.png %}