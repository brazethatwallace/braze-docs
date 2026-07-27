---
nav_title: 사용자 리타겟팅
article_title: 사용자 리타겟팅
description: "랜딩 페이지를 통해 양식을 제출한 사용자를 리타겟팅하는 방법을 알아보세요."
page_order: 3
---

# 랜딩 페이지를 통한 사용자 리타겟팅 {#retarget-users-through-a-landing-page}

> 전용 Segment를 생성하거나 양식 제출 시 메시지를 트리거하여, 랜딩 페이지를 통해 양식을 제출한 사용자를 리타겟팅하는 방법을 알아보세요.

## 사전 요구 사항 {#prerequisites}

시작하기 전에 [랜딩 페이지]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)를 만들어야 합니다.

## 사용자 리타겟팅 {#retargeting-users}

Braze는 사용자가 랜딩 페이지 양식을 제출할 때 자동으로 추적합니다. [랜딩 페이지 분석]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#view-analytics)에서 양식의 총 제출 수를 확인할 수 있습니다. 그러나 사용자별 리타겟팅을 위해서는 다음 방법 중 하나를 사용하여 랜딩 페이지 양식을 통해 사용자를 리타겟해야 합니다.

- **Segment 사용:** 새 Segment를 생성하여 랜딩 페이지 양식을 제출했거나 제출하지 않은 사용자를 자동으로 식별할 수 있습니다.
- **메시지 트리거 사용:** 메시지 트리거를 설정하여 사용자가 양식을 제출한 후 자동으로 메시지를 보내거나 Canvas에 진입시킬 수 있습니다.

{% tabs local %}
{% tab Segment 사용 %}
[Segment를 생성]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)할 때, "리타겟팅" 그룹에서 **Submitted form on Landing Page**를 선택합니다.

![필터 그룹이 "Submitted Form on Landing Page"로 선택된 Segment 생성 화면.]({% image_buster /assets/img/landing_pages/segmentation_selected.png %})

여기에서 사용자가 랜딩 페이지 양식을 제출했는지 여부에 따라 사용자를 세분화할 수 있습니다.
{% endtab %}

{% tab 메시지 트리거 사용 %}
[Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) 또는 [Canvas]({{site.baseurl}}/user_guide/messaging/canvas)의 전달 옵션을 선택할 때, **실행 기반 전달**을 선택한 다음 **Submitted Landing Page form**을 선택합니다.

이 랜딩 페이지 양식을 통해 양식을 제출하는 모든 사용자는 선택한 메시징 채널을 통해 메시지를 받거나 선택한 Canvas에 진입하게 됩니다.

![메시징의 랜딩 페이지 트리거 동작.]({% image_buster /assets/img/landing_pages/trigger.png %})

{% alert note %}
랜딩 페이지의 실행 기반 전달 옵션은 인앱 메시지에는 사용할 수 없습니다. 랜딩 페이지에서 양식을 제출한 사용자를 인앱 메시지로 타겟팅하려면, Campaign의 **타겟팅 옵션**에서 **Submitted Form on Landing Page** 필터를 선택하세요.
{% endalert %}

{% endtab %}
{% endtabs %}