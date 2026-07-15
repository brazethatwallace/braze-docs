---
nav_title: 익명 사용자
article_title: 익명 사용자
page_order: 0
page_type: reference
description: "이 도움말에서는 익명 사용자와 사용자 별칭에 대한 개요와 함께 그 중요성 및 메시지에서 이를 활용하는 방법을 간략하게 설명합니다."

---

# 익명 사용자 {#anonymous-users}

> 게스트 방문자처럼 로그인하지 않고 웹사이트나 애플리케이션을 방문하는 사용자는 익명 사용자로 인식됩니다. 이러한 사용자에게는 Braze API로 고객 프로필을 업데이트하는 데 사용되는 `external_ids`가 없지만 여전히 [데이터 포인트]({{site.baseurl}}/user_guide/data/infrastructure/data_points)가 할당되어 있으며 Segments에서 타겟팅할 수 있습니다.

익명 사용자가 웹사이트나 애플리케이션을 방문하면 Braze SDK가 '익명' 고객 프로필을 생성하여 할당합니다. 사용자가 브라우징하는 동안 커스텀 속성 및 커스텀 이벤트를 설정한 경우 SDK는 사용 정보, 기기 정보 등 익명 고객 프로필에 대한 데이터를 자동으로 캡처합니다.

캡처한 익명 사용자로 다음을 수행할 수 있습니다:

- 로그인하기 전에 사용자에게 메시지 보내기
- 로그인하기 전에 사용자의 프로필을 수집하여 관련 데이터를 놓치지 않기
- 사용자가 프로필을 부분적으로만 작성한 경우 메시지로 프로필 작성을 독려하기
- 로그인 시 사용자의 프로필을 완성하여 다른 플랫폼에서 메시징을 취소하기(예: 사용자가 이미 앱 주문을 한 경우 "첫 번째 앱 주문 시 무료 배송" 메시지를 보내지 않음)
- 이탈 의도를 보이는 사용자에게 프로필 생성, 장바구니 결제 또는 다른 동작을 취하도록 유도하여 참여를 이끌어내기

## 작동 방식 {#how-it-works}

{% multi_lang_include anonymous_users/about_anonymous_users.md section='user_guide' %}

## 사용자 별칭 할당 {#assigning-user-aliases}

{% multi_lang_include anonymous_users/about_user_aliases.md section='user_guide' %}

## 익명 사용자 병합하기 {#merging-anonymous-users}

익명 사용자 프로필이 다른 사용자 프로필과 전화번호나 이메일 주소가 같은 중복 프로필인 경우가 있습니다. 중복된 항목 중 하나는 식별된 고객 프로필일 수도 있습니다. 이러한 중복 프로필은 [POST: 사용자 병합 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) 또는 Braze 플랫폼의 병합 도구(예: [규칙 기반 병합]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users#rules-based-merging)) 중 하나를 사용하여 하나의 고객 프로필로 병합할 수 있습니다.

## 익명 사용자 조회하기 {#looking-up-an-anonymous-user}

익명 사용자에게는 `external_id`가 없으므로 기기 ID를 사용하여 특정 프로필을 검색할 수 있습니다. 다음 단계에서는 Web SDK 통합에서 현재 사용자의 기기 ID를 가져오는 방법을 설명합니다:

1. 브라우저의 개발자 도구를 엽니다(예: Chrome에서 Mac은 **Command + Option + J**, Windows는 **Ctrl + Shift + I**를 누릅니다).
2. **Console** 탭에서 다음을 실행합니다:

```javascript
console.log(braze.getDeviceId());
```

{:start="3"}
3. Braze 대시보드에서 [사용자 검색]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search)을 사용하여 반환된 기기 ID를 검색합니다.

## 활용 사례 {#use-cases}

### Segment에서 익명 사용자 타겟팅 {#target-anonymous-users-in-your-segment}

익명 사용자에게는 `external_id`가 없으므로 세분화 필터 **외부 사용자 ID가 비어 있음**을 사용하여 일괄적으로 타겟팅할 수 있습니다. 정확도를 높이려면 타겟팅하려는 익명 사용자에 커스텀 속성을 추가하고 해당 속성으로 필터링할 수 있습니다.

각 익명 사용자 프로필에 커스텀 속성 "is_lead_profile"을 할당한다고 가정해 보겠습니다. 다음 필터 중 하나 또는 둘 모두를 사용하여 이러한 프로필을 타겟팅할 수 있습니다:

- **외부 사용자 ID가 비어 있음**
- "is_lead_profile" **이 참임**

![빈 외부 사용자 ID와 참인 "is_lead_profile" 커스텀 속성에 대한 Segment 필터.]({% image_buster /assets/img/getting_started/anonymous_users.png %})

### 익명 사용자의 결제 데이터 캡처 {#capture-checkout-data-from-an-anonymous-user}

결제 프로세스 중에 사용자 별칭 프로필을 생성하여 익명 사용자(또는 게스트 방문자)의 결제 데이터를 캡처할 수 있습니다. 익명 사용자가 웹 캡처 양식을 사용하여 결제할 때 API 호출을 트리거하여 사용자 별칭 프로필을 생성하고 구매 이벤트를 기록합니다. 그런 다음 Braze API를 통해 생성된 고객 프로필을 업데이트할 수 있습니다.

다음은 웹 캡처 양식이 제출될 때 생성되는 페이로드의 예시입니다:

{% raw %}
```json
{
    "purchase":[
        {
            "user_alias": {"alias_name": "Joedoe", "alias_label": "full_name"},
            "app_id": "11dk3k9d-2183-3948-k02b-kw3938109k12od",
            "product_id": "jacket",
            "currency": "USD",
            "price": 80.00,
            "time": "2025-01-05T19:20:30+01:00",
            "properties": {
                "color": "brown",
                "monogram": "ABC",
                "checkout_duration": 180,
                "size": "Small",
                "brand": "Natural Essence"
            }
        }
    ]
}
```
{% endraw %}