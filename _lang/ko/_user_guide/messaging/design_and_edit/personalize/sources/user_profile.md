---
nav_title: 고객 프로필
article_title: 고객 프로필
page_order: 0
description: "표준 속성, 커스텀 속성, 이벤트 등록정보를 포함한 고객 프로필 데이터를 사용하여 메시지를 개인화하는 방법을 알아보세요."
---

# 고객 프로필

> 표준 속성, 커스텀 속성, 이벤트 등록정보를 포함하여 각 사용자의 프로필에 저장된 데이터로 메시지를 개인화하세요. Braze는 메시지 콘텐츠에 직접 삽입할 수 있는 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) 태그를 통해 이 데이터를 제공합니다.

## 표준 속성

{% raw %}
표준 속성은 Braze가 자동으로 추적하는 사전 정의된 프로필 필드로, `{{${first_name}}}`, `{{${email_address}}}`, `{{${city}}}` 등이 있습니다. 이러한 속성은 일관된 명명 규칙을 따르므로 추가 설정 없이 모든 메시지에서 참조할 수 있습니다.

예를 들어, 사용자의 이름으로 인사하려면 다음과 같이 작성합니다:

```liquid
Hi {{${first_name} | default: 'there'}}, check out our latest picks for you!
```
{% endraw %}

표준 속성 태그의 전체 목록은 [지원되는 개인화 태그]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/)를 참조하세요.

## 커스텀 속성

{% raw %}
커스텀 속성은 로열티 등급, 선호 카테고리, 계정 유형 등 워크스페이스에 고유한 프로필 필드입니다. `{{custom_attribute.${attribute_name}}}` 태그를 사용하여 참조할 수 있습니다.

예를 들어, 사용자의 멤버십 등급에 따라 메시지를 개인화하려면 다음과 같이 작성합니다:

```liquid
{% if custom_attribute.${membership_tier} == 'gold' %}
  As a Gold member, you get early access to our new collection.
{% else %}
  Upgrade your membership for early access to new collections.
{% endif %}
```
{% endraw %}

커스텀 속성 생성 및 관리에 대한 자세한 내용은 [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/)을 참조하세요.

## 이벤트 등록정보

{% raw %}
캠페인 또는 캔버스가 커스텀 이벤트나 구매에 의해 트리거되면 해당 이벤트의 등록정보를 개인화에 사용할 수 있습니다. `{{event_properties.${property_name}}}`를 사용하여 참조합니다.

예를 들어, 커스텀 이벤트 `completed_purchase`에 `product_name` 등록정보가 포함된 경우:

```liquid
Thanks for purchasing {{event_properties.${product_name}}}! Your order is on its way.
```
{% endraw %}

이벤트 등록정보는 액션 기반 캠페인과 액션 기반 캔버스의 첫 번째 단계에서 사용할 수 있습니다. 자세한 내용은 [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)를 참조하세요.

## API 트리거 등록정보

{% raw %}
API를 통해 트리거되는 캠페인과 캔버스의 경우, 트리거 등록정보 오브젝트를 사용하여 추가 데이터를 전달할 수 있습니다. `{{api_trigger_properties.${property_name}}}`로 이 값을 참조합니다.

예를 들어:

```liquid
Your verification code is {{api_trigger_properties.${verification_code}}}.
```
{% endraw %}

자세한 내용은 [API 트리거 등록정보 오브젝트]({{site.baseurl}}/api/objects_filters/trigger_properties_object/)를 참조하세요.

## 기기 속성

{% raw %}
사용자가 가장 최근에 사용한 기기의 속성도 참조할 수 있습니다. 예를 들어, `{{most_recently_used_device.${model}}}`은 기기 모델명을 반환하고, `{{most_recently_used_device.${os}}}`는 운영체제를 반환합니다.
{% endraw %}

기기 속성 태그의 전체 목록은 [지원되는 개인화 태그]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/#most-recently-used-device-information)를 참조하세요.

## 기본값 설정

특정 사용자의 프로필 필드가 비어 있으면 Braze는 기본적으로 빈 문자열을 렌더링합니다. 불완전해 보이는 메시지를 방지하려면 `default` Liquid 필터를 사용하여 대체 값을 설정하세요.

{% raw %}
```liquid
Hi {{${first_name} | default: 'there'}},
```
{% endraw %}

자세한 내용은 [기본값 설정]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values/)을 참조하세요.