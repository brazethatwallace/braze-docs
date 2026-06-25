---
nav_title: 커스텀 속성
article_title: 커스텀 속성
page_order: 1
page_type: reference
description: "이 페이지에서는 커스텀 속성에 대해 설명하고 다양한 커스텀 속성 데이터 유형에 대해 설명합니다."
search_rank: 1
---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}커스텀 속성 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-attributes}

> 이 페이지에서는 사용자 고유 특성의 모음인 커스텀 속성에 대해 설명합니다. 커스텀 속성은 사용자에 대한 속성이나 애플리케이션 내에서 가치가 낮은 동작에 대한 정보를 저장하는 데 가장 적합합니다.

Braze에 저장된 커스텀 속성을 사용하여 오디언스 Segment를 구축하고 Liquid를 사용하여 메시지를 개인화할 수 있습니다. Braze는 커스텀 속성에 대해 시계열 정보를 저장하지 않으므로 커스텀 이벤트에서와 같이 해당 속성을 기반으로 한 그래프를 얻을 수 없다는 점에 유의하세요.

{% alert important %}
**이름은 정확히 일치해야 합니다.** 커스텀 속성 키는 **대소문자를 구분합니다**. 예를 들어 `Home_City`와 `home_city`는 서로 다른 속성입니다. [REST API]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 또는 SDK를 통해 데이터를 전송하면 Braze는 속성 이름에서 **앞뒤 공백을 제거**하므로 `greeting`과 ` greeting `은 동일한 키로 처리됩니다. 속성을 참조하는 모든 곳(**데이터 설정** > **커스텀 속성**, API 및 SDK 페이로드, CSV 가져오기)에서 동일한 철자와 대소문자를 사용하세요. [데이터 유형을 강제 지정]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/#data-type-coercion)할 때 Braze가 수신 값을 변환하는 방법에 대해서는 [커스텀 데이터 관리]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/)를 참조하세요.
{% endalert %}

## 활용 사례 {#use-cases}

일반적인 커스텀 속성 활용 사례는 다음과 같습니다:

- 로열티 등급, 구독 상태, 선호 언어, 요금제 유형 등의 특성을 기반으로 사용자를 세분화하여 오디언스를 타겟팅하거나 제외
- 사용자의 이름, 리워드 포인트, 선호 카테고리 등의 속성을 참조하여 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/)로 메시지 개인화
- 온보딩 단계, 계정 상태, 체험판 종료일 등 라이프사이클 단계 및 사용자 상태 추적
- 사용자가 기능을 볼 때마다 `feature_views_count` 속성을 증가시키는 것처럼 [숫자 속성]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#numbers)으로 가치가 낮은 동작 횟수 기록
- `last_support_ticket_at` 또는 `last_password_reset_at`처럼 [시간 속성]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#time)을 사용하여 가치가 낮은 동작이 마지막으로 발생한 시점 기록
- 선호 장르나 최근 조회한 콘텐츠 등을 [배열]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#arrays)로 저장하여 관심사 기반 타겟팅에 활용
- 구조화된 선호도나 여러 저장된 주소 등 더 풍부한 프로필 데이터를 [오브젝트]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support/) 또는 [오브젝트 배열]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects/)로 저장
- 사용자의 `rewards_tier`가 변경될 때 등급 상승 알림을 보내는 것처럼 [속성 트리거]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers/)를 사용하여 속성 값이 변경될 때 액션 기반 메시지 트리거

## 커스텀 속성 관리 {#managing-custom-attributes}

대시보드에서 커스텀 속성을 만들고 관리하려면 **데이터 설정** > **커스텀 속성**으로 이동합니다.

![네 개의 부울 커스텀 속성.]({% image_buster /assets/img/export_custom_attributes.png %})

**마지막 업데이트** 열에는 커스텀 속성을 마지막으로 편집한 시간(예: 차단 목록 또는 활성으로 마지막으로 설정한 시간)이 나열됩니다.

{% alert important %}
적절한 메시지 타겟팅을 위해서는 커스텀 속성 데이터 유형이 실제 커스텀 속성과 일치하는지 확인하세요. <br><br>예를 들어, `newsletter_subscribed`가 문자열로 정의되면 Liquid 구문은 {% raw %}`{% if {{custom_attribute.${newsletter_subscribed}}} == 'true' %}`{% endraw %}와 같아야 합니다. `newsletter_subscribed`가 부울로 정의되면 Liquid 구문에는 작은따옴표가 없어야 합니다: {% raw %}`{% if {{custom_attribute.${newsletter_subscribed}}} == true %}`{% endraw %}.
{% endalert %}

이 페이지에서 기존 커스텀 속성을 확인, 관리, 생성 또는 차단 목록에 추가할 수 있습니다. 다음 동작을 수행하려면 커스텀 속성 옆의 메뉴를 선택합니다:

### 차단 목록에 추가 {#blocklisting}

동작 메뉴를 통해 개별 커스텀 속성을 차단 목록에 추가하거나, 최대 100개의 속성을 선택하여 일괄 차단할 수 있습니다.

커스텀 속성을 차단하면:

- 해당 속성에 대한 향후 데이터가 수집되지 않습니다.
- 해당 속성의 차단이 해제되지 않는 한 기존 데이터를 사용할 수 없습니다.
- 해당 속성이 필터나 그래프에 표시되지 않습니다.

또한 차단된 커스텀 속성이 현재 Braze의 다른 영역에서 필터나 트리거에 의해 참조되고 있는 경우, 해당 필터 또는 트리거의 모든 인스턴스가 제거되고 아카이브된다는 경고 모달이 표시됩니다.

커스텀 데이터 차단 및 삭제에 대한 자세한 내용은 [커스텀 데이터 차단 목록]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data/)을 참조하세요.

### 개인 식별 정보(PII)로 표시 {#mark-as-personally-identifiable-information-pii}

관리자는 이 페이지에서 커스텀 속성을 생성하고 PII로 표시할 수도 있습니다. 이러한 속성은 관리자와 "View Custom Attributes Marked as PII" 권한이 있는 대시보드 사용자에게만 표시됩니다.

### 설명 추가 {#add-descriptions}

`Manage Events, Attributes, Purchases` [사용자 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/)이 있는 경우 커스텀 속성이 생성된 후 설명을 추가할 수 있습니다. 커스텀 속성의 **설명 편집**을 선택하고 팀을 위한 메모 등 원하는 내용을 입력하세요.

### 태그 추가 {#add-tags}

"Manage Events, Attributes, Purchases" [사용자 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/)이 있는 경우 커스텀 속성이 생성된 후 태그를 추가할 수 있습니다. 태그를 사용하여 속성 목록을 필터링할 수 있습니다.

### 커스텀 속성 제거 {#remove-custom-attributes}

고객 프로필에서 커스텀 속성을 제거하는 방법은 두 가지가 있습니다:

* [사용자 업데이트 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/#removing-custom-attributes)에서 제거할 커스텀 속성 이름을 선택합니다.
* [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#user-track)에 대한 API 요청에서 `null` 값을 설정합니다.

### 데이터 내보내기 {#export-data}

커스텀 속성 목록을 CSV 파일로 내보내려면 페이지 상단의 **모두 내보내기**를 선택합니다. CSV 파일이 생성되고 다운로드 링크가 이메일로 전송됩니다.

## 커스텀 속성 유형 변경 {#change-custom-attribute-type}

### 필수 조건 {#prerequisites}

커스텀 속성이 현재 활성 Campaigns, Canvases 또는 Segments에서 사용 중이지 않아야 합니다. 속성이 아직 참조되고 있는 상태에서 데이터 유형을 변경하려고 하면 대시보드에 오류가 표시되고 변경이 차단됩니다.

### 데이터 유형 변경 {#changing-the-data-type}

1. Segments 또는 필터에서 해당 속성을 사용하는 활성 Campaigns이나 Canvases를 중지합니다.
2. 모든 Segment, Campaign, Canvas 필터에서 해당 속성을 제거합니다.
3. **데이터 설정** > **커스텀 속성**(또는 **커스텀 이벤트**)으로 이동하여 해당 속성을 찾고 원하는 데이터 유형으로 업데이트합니다.
4. 기존 고객 프로필의 속성 값을 새 데이터 유형에 맞게 업데이트합니다(예: [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 사용).
5. 관련 Segments, Campaigns, Canvases에 속성을 다시 적용한 후 중지했던 Campaigns이나 Canvases를 다시 활성화합니다.

### 알아두어야 할 사항 {#things-to-know}

- **사용자 데이터는 소급 업데이트되지 않습니다.** 고객 프로필에 이전 데이터 유형의 속성 값이 있는 경우 해당 값은 변경되지 않습니다. 세분화 필터는 새 데이터 유형을 기준으로 조회하므로, 이전 값을 가진 사용자는 프로필이 업데이트될 때까지 일치하는 Segments에서 제외됩니다.
- **새 데이터는 새 데이터 유형과 일치해야 합니다.** 변경 후 이 속성에 대해 이전 데이터 유형을 전송하는 API 호출이나 SDK 이벤트는 수락되지 않습니다. 새 데이터 유형과 일치하는 값만 수집됩니다.
- **필터는 자동으로 업데이트되지 않습니다.** 변경된 속성을 참조하는 Segments 및 Campaign 필터는 소급 업데이트되지 않습니다. 변경 후 해당 필터를 제거하고 다시 추가해야 합니다.

## 사용 보고서 보기 {#view-usage-reports}

사용 보고서에는 특정 커스텀 속성을 사용하는 모든 Canvases, Campaigns, Segments가 나열됩니다. 이 목록에는 Liquid 사용은 포함되지 않습니다.

해당 커스텀 속성 옆의 체크박스를 선택한 후 **사용 보고서 보기**를 선택하면 한 번에 최대 100개의 사용 보고서를 볼 수 있습니다.

### 값 탭 {#values-tab}

사용 보고서를 볼 때 **값** 탭을 선택하면 약 250,000명의 사용자 샘플을 기반으로 선택한 커스텀 속성의 상위 값을 확인할 수 있습니다. 결과는 사용자의 하위 집합에서 샘플링되므로 모든 기존 값이 포함되지 않을 수 있습니다. 따라서 **값** 탭은 문제 해결이나 모든 사용자의 데이터를 포함해야 하는 사용 사례에는 사용하지 않는 것이 좋습니다.

!["US" 및 "PR" 등의 국가 속성 값을 보여주는 원형 차트가 있는 값 탭이 열린 선택된 커스텀 속성의 사용 보고서.]({% image_buster /assets/img/usage_report_values.png %}){: style="max-width:80%;"}

## 커스텀 속성 설정 {#set-custom-attributes}

다음은 다양한 플랫폼에서 커스텀 속성을 설정하는 데 사용되는 메서드 목록입니다.

{% details 플랫폼별 설명서 펼치기 %}

- [Android 및 FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=unity)
- [.NET MAUI(이전 Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/)

{% enddetails %}

## 커스텀 속성 저장 {#custom-attribute-storage}

**고객 프로필**에 저장된 모든 데이터(커스텀 속성 데이터 포함)는 각 프로필이 [활성]({{site.baseurl}}/user_archival/#active-users) 상태인 한 무기한 보존됩니다.

부울, 숫자, 문자열, 배열, 시간, 오브젝트, 오브젝트 배열 등 커스텀 속성으로 저장할 수 있는 모든 데이터 유형에 대한 전체 참조는 [커스텀 속성 데이터 유형]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/)을 확인하세요.

### 빈 문자열과 null 값 비교 {#blank-strings-versus-null-values}

커스텀 속성을 지우거나 설정 해제할 때 빈 문자열(`""`)을 전달하는지 `null`을 전달하는지에 따라 동작이 달라집니다:

| 값 | 동작 |
| --- | --- |
| `""` (빈 문자열) | 속성이 빈 값으로 설정되며 고객 프로필에 계속 표시됩니다. |
| `null` | 속성이 고객 프로필에서 완전히 제거됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="빈 문자열과 null 값 비교" }
{: .reset-td-br-1 .reset-td-br-2 aria-label="빈 문자열과 null 값 비교" }
{: .reset-td-br-1 .reset-td-br-2 aria-label="빈 문자열과 null 값 비교" }

{% alert important %}
Braze 대시보드에서 데이터 유형을 수동으로 설정한(자동 감지가 아닌) 비문자열 데이터 유형의 경우 값을 설정 해제하려면 `null`을 사용해야 합니다. `""`를 전달하는 것은 문자열 속성에만 유효합니다. 예를 들어 부울 속성을 `""`로 설정하면 빈 문자열로 처리되며, 이는 해당 유형에 유효하지 않은 값입니다. 부울을 설정 해제하려면 `null`을 전달하세요.

CSV 가져오기는 `null`을 지원하지 않습니다. CSV 가져오기에서 부울 값은 `TRUE` 또는 `FALSE`여야 합니다.
{% endalert %}