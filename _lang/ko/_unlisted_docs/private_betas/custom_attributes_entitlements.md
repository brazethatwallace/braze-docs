---
article_title: 커스텀 속성
permalink: "/custom_attributes_entitlements/"
hidden: true
---

# [![Braze 학습 과정]({% image_buster /assets/unlisted_docs/img/logos/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}커스텀 속성 {#braze-learning-course-image_buster-assetsunlisted_docsimglogosbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-attributes}

> 이 페이지에서는 사용자의 고유한 특성을 모아 놓은 커스텀 속성에 대해 다룹니다. 커스텀 속성은 사용자에 대한 속성이나 애플리케이션 내 가치가 낮은 행동에 대한 정보를 저장하는 데 가장 적합합니다.

Braze에 저장된 커스텀 속성은 오디언스 Segment를 구축하고 Liquid를 사용하여 메시징을 개인화하는 데 활용할 수 있습니다. 커스텀 속성에 대해서는 시계열 정보가 저장되지 않으므로, 커스텀 이벤트처럼 그래프를 기반으로 데이터를 확인할 수 없다는 점에 유의하세요.

## 할당량 {#entitlements}

할당량은 커스텀 속성 용량을 결정하며, 정의한 서로 다른 속성 이름의 수를 추적합니다. 워크스페이스당 최대 1,000개의 커스텀 속성을 사용할 수 있습니다. 용량을 늘려야 하는 경우 Braze 계정 매니저에게 문의하여 자세한 정보를 확인하세요.

워크스페이스가 최대 커스텀 속성 수에 가까워지면 대시보드와 이메일을 통해 알림을 받아 관리할 수 있습니다.

용량에 도달한 후에도 기존 커스텀 속성은 계속 수신할 수 있습니다. 그러나 새로운 커스텀 속성을 생성할 수는 없습니다. 이미 존재하지 않는 커스텀 속성에 대해 수신된 데이터는 처리되지 않습니다.

## 커스텀 속성 관리 {#managing-custom-attributes}

대시보드에서 커스텀 속성을 생성하고 관리하려면 **데이터 설정** > **커스텀 속성**으로 이동합니다.

![부울 유형의 네 가지 커스텀 속성]({% image_buster /assets/unlisted_docs/img/custom_attributes_entitlements/export_custom_attributes.png %})

**마지막 업데이트** 열에는 커스텀 속성이 마지막으로 편집된 시간이 표시됩니다. 예를 들어 마지막으로 차단 목록에 추가되거나 활성 상태로 설정된 시간 등이 포함됩니다.

{% alert important %}
올바른 메시지 타겟팅을 위해 커스텀 속성 데이터 유형이 실제 커스텀 속성과 일치하는지 확인하세요.
{% endalert %}

이 페이지에서 기존 커스텀 속성을 조회, 관리, 생성 또는 차단 목록에 추가할 수 있습니다. 커스텀 속성 옆의 메뉴를 선택하면 다음 작업을 수행할 수 있습니다.

### 차단 목록 추가 {#blocklisting}

커스텀 속성은 작업 메뉴에서 개별적으로 차단 목록에 추가하거나, 최대 100개의 속성을 선택하여 일괄적으로 차단 목록에 추가할 수 있습니다. 커스텀 속성을 차단하면 해당 속성에 대한 데이터가 수집되지 않으며, 기존 데이터는 다시 활성화하지 않는 한 사용할 수 없고, 차단된 속성은 필터나 그래프에 표시되지 않습니다. 또한 해당 속성이 현재 Braze 대시보드의 다른 영역에서 필터나 트리거에 의해 참조되고 있는 경우, 해당 필터 또는 트리거의 모든 인스턴스가 제거되고 아카이브된다는 경고 모달이 표시됩니다.

### 개인 식별 정보(PII)로 표시 {#marking-as-personally-identifiable-information-pii}

관리자는 이 페이지에서 커스텀 속성을 생성하고 PII로 표시할 수도 있습니다. 이러한 속성은 관리자와 "PII로 표시된 커스텀 속성 보기" 권한이 있는 대시보드 사용자에게만 표시됩니다.

### 설명 추가 {#adding-descriptions}

`Manage Events, Attributes, Purchases` [사용자 권한](https://www.braze.com/docs/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)이 있는 경우 커스텀 속성이 생성된 후 설명을 추가할 수 있습니다. 커스텀 속성을 편집하고 팀을 위한 메모 등 원하는 내용을 입력하세요.

### 태그 추가 {#adding-tags}

"Manage Events, Attributes, Purchases" [사용자 권한](https://www.braze.com/docs/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)이 있는 경우 커스텀 속성이 생성된 후 태그를 추가할 수 있습니다. 태그를 사용하여 속성 목록을 필터링할 수 있습니다.

### 커스텀 속성 제거 {#removing-custom-attributes}

고객 프로필에서 커스텀 속성을 제거하는 방법은 두 가지가 있습니다.

* [사용자 업데이트 단계](https://www.braze.com/docs/user_guide/engagement_tools/canvas/canvas_components/user_update/#removing-custom-attributes)에서 제거할 커스텀 속성 이름을 선택합니다.
* API 요청에서 [`/users/track` 엔드포인트](https://www.braze.com/docs/api/endpoints/user_data/post_user_track#user-track)에 `null` 값을 설정합니다.

### 사용 보고서 보기 {#viewing-usage-reports}

사용 보고서에는 특정 커스텀 속성을 사용하는 모든 Canvases, Campaigns, Segments가 나열됩니다. 이 목록에는 Liquid 사용은 포함되지 않습니다.

해당 커스텀 속성 옆의 체크박스를 선택한 다음 **사용 보고서 보기**를 선택하면 한 번에 최대 100개의 사용 보고서를 볼 수 있습니다.

### 데이터 내보내기 {#exporting-data}

커스텀 속성 목록을 CSV 파일로 내보내려면 페이지 상단에서 **모두 내보내기**를 선택합니다. CSV 파일이 생성되고 다운로드 링크가 이메일로 전송됩니다.

## 커스텀 속성 설정 {#setting-custom-attributes}

다음은 다양한 플랫폼에서 커스텀 속성을 설정하는 데 사용되는 메서드 목록입니다.

{% details 플랫폼별 설명서 펼치기 %}

- [Android 및 FireOS](https://www.braze.com/docs/developer_guide/analytics/setting_user_attributes/?sdktab=android)
- [iOS](https://www.braze.com/docs/developer_guide/analytics/setting_user_attributes/?sdktab=swift)
- [Web](https://www.braze.com/docs/developer_guide/analytics/setting_user_attributes/?sdktab=web)
- [React Native](https://www.braze.com/docs/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-attributes)
- [Unity](https://www.braze.com/docs/developer_guide/platform_integration_guides/unity/Analytics/setting_custom_attributes/)
- [Xamarin](https://www.braze.com/docs/developer_guide/platform_integration_guides/xamarin/analytics/#setting-custom-attributes)
- [Roku](https://www.braze.com/docs/developer_guide/analytics/setting_user_attributes/)

{% enddetails %}

## 커스텀 속성 저장 {#custom-attribute-storage}

**고객 프로필**에 저장된 모든 데이터(커스텀 속성 데이터 포함)는 각 프로필이 [활성](https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users) 상태인 한 무기한 보존됩니다.

## 커스텀 속성 데이터 유형 {#custom-attribute-data-types}

커스텀 속성은 매우 유연한 도구로, 뛰어난 타겟팅을 가능하게 합니다.

다음 데이터 유형을 커스텀 속성으로 저장할 수 있습니다.

- [부울](#booleans)
- [숫자](#numbers)
- [문자열](#strings)
- [배열](#arrays)
- [시간](#time)
- [오브젝트](https://www.braze.com/docs/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/)
- [오브젝트 배열](https://www.braze.com/docs/user_guide/data/custom_data/custom_attributes/array_of_objects/)

### 부울(참/거짓) {#booleans}

부울 속성은 구독 상태와 같은 사용자에 대한 간단한 이진 데이터를 저장하는 데 유용합니다. 변수가 명시적으로 참 또는 거짓 값으로 설정된 사용자뿐만 아니라, 해당 속성이 아직 기록되지 않은 사용자도 찾을 수 있습니다.

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 | 예시 |
| ---------------------| --------------- | ------------- | -------- |
| 부울 값이 참, 거짓, 참 또는 설정되지 않음, 거짓 또는 설정되지 않음 중 하나**인지** 확인 | **IS**  | **TRUE**, **FALSE**, **TRUE OR NOT SET**, 또는 **FALSE OR NOT SET** | 이 필터가 `coffee_drinker`를 지정하는 경우, 사용자는 다음 상황에서 이 필터에 일치합니다: <br> {::nomarkdown}<ul><li>이 필터가 <code>true</code>이고 사용자에게 <code>coffee_drinker</code> 값이 있는 경우</li><li>이 필터가 <code>false</code>이고 사용자에게 <code>coffee_drinker</code> 값이 없는 경우</li><li>이 필터가 <code>true or not set</code>이고 사용자에게 <code>coffee_drinker</code> 값이 있거나 값이 없는 경우</li><li>이 필터가 <code>false or not set</code>이고 사용자에게 <code>coffee_drinker</code> 또는 어떤 값도 없는 경우</li></ul>{:/} |
| 부울 값이 사용자 프로필에 **존재하고** null이 아닌지 확인 | **IS NOT BLANK**  | **N/A** | 이 필터가 `coffee_drinker`를 지정하고 사용자에게 `coffee_drinker` 속성에 대한 값이 있는 경우, 사용자는 이 필터에 일치합니다. |
| 부울 값이 사용자 프로필에 **존재하지 않거나** null인지 확인 | **IS BLANK**  | **N/A** | 이 필터가 `coffee_drinker`를 지정하고 사용자에게 `coffee_drinker` 속성이 없거나 `coffee_drinker` 값이 null인 경우, 사용자는 이 필터에 일치합니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### 숫자 {#numbers}

숫자 속성에는 [정수](https://en.wikipedia.org/wiki/Integer)와 [플로트](https://en.wikipedia.org/wiki/Floating-point_arithmetic)가 포함되며, 다양한 사용 사례가 있습니다. 증분 숫자 커스텀 속성은 데이터 한도에 영향을 주지 않으면서 특정 행동이나 이벤트가 발생한 횟수를 저장하는 데 유용합니다. 표준 숫자는 다음과 같은 다양한 용도로 사용됩니다.

- 신발 사이즈
- 허리 사이즈
- 사용자가 특정 제품 기능이나 카테고리를 조회한 횟수

{% alert tip %}
지출 금액은 이 방법으로 기록하면 안 됩니다. 대신 [구매 메서드](#purchase-revenue-tracking)를 통해 기록해야 합니다.
{% endalert %}

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 | 예시 |
| ---------------------| --------------- | ------------- | -------- |
| 숫자 속성이 **숫자**와 **정확히 일치하는지** 확인| **EXACTLY** | **NUMBER** | 이 필터가 `10`을 지정하고 고객 프로필에 `10` 값이 있는 경우, 사용자는 이 필터에 일치합니다. |
| 숫자 속성이 **숫자**와 **같지 않은지** 확인| **DOES NOT EQUAL** | **NUMBER** | 이 필터가 `10`을 지정하고 고객 프로필에 `10` 값이 없는 경우, 사용자는 이 필터에 일치합니다. |
| 숫자 속성이 **숫자**보다 **큰지** 확인| **MORE THAN** | **NUMBER** | 이 필터가 `10`을 지정하고 고객 프로필에 `10`보다 큰 값이 있는 경우, 사용자는 이 필터에 일치합니다. |
| 숫자 속성이 **숫자**보다 **작은지** 확인| **LESS THAN** | **NUMBER** | 이 필터가 `10`을 지정하고 고객 프로필에 `10`보다 작은 값이 있는 경우, 사용자는 이 필터에 일치합니다. |
| 숫자 속성이 사용자 프로필에 **존재하고** null이 아닌지 확인 | **IS NOT BLANK** | **N/A** | 고객 프로필에 지정된 숫자 속성이 포함되어 있으면 값에 관계없이 사용자는 이 필터에 일치합니다. |
| 숫자 속성이 사용자 프로필에 **존재하지 않거나** null인지 확인 | **IS BLANK** | **N/A** | 고객 프로필에 지정된 숫자 속성이 포함되어 있지 않거나 속성 값이 null인 경우, 사용자는 이 필터에 일치합니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 숫자 속성 세부 정보 {#number-attribute-details}

- "정확히 0" 및 "미만" 필터에는 NULL 필드가 있는 사용자가 포함됩니다
  - 커스텀 속성에 값이 없는 사용자를 제외하려면 **is not blank** 필터를 포함해야 합니다.

### 문자열(영숫자 문자) {#strings}

문자열 속성은 좋아하는 브랜드, 전화번호 또는 애플리케이션 내 마지막 검색 문자열과 같은 사용자 입력을 저장하는 데 유용합니다. 문자열 속성은 최대 255자까지 가능합니다.

단어 사이, 앞 또는 뒤에 공백이 포함된 값을 입력하면 Braze도 동일한 공백을 확인합니다.

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 | 예시 |
| ---------------------| --------------- | ------------- | -------- |
| 문자열 속성이 입력된 문자열과 **정확히 일치하는지** 확인| **EQUALS** | **STRING**<br>대소문자 구분 | 이 필터가 `book`을 지정하고 고객 프로필에 `book`을 포함하는 `last_item_purchased` 문자열 속성이 있는 경우, 사용자는 이 필터에 일치합니다. |
| 문자열 속성이 입력된 문자열 **또는** 정규표현식과 **부분적으로 일치하는지** 확인 | **MATCHES REGEX** | **STRING** **또는** **REGULAR EXPRESSION** <br>대소문자 구분 안 함; 최대 32,764자 |
| 문자열 속성이 입력된 문자열 **또는** 정규표현식과 **부분적으로 일치하지 않는지** 확인 | **DOES NOT MATCH REGEX** * | **STRING** **또는** **REGULAR EXPRESSION**<br>대소문자 구분 안 함; 최대 32,764자 |
| 문자열 속성이 입력된 문자열과 **일치하지 않는지** 확인| **DOES NOT EQUAL** | **STRING**<br>대소문자 구분 안 함  | 이 필터가 `book`을 지정하고 고객 프로필에 `book`을 포함하지 않는 `last_item_purchased` 문자열 속성이 있는 경우, 사용자는 이 필터에 일치합니다.|
| 문자열 속성이 사용자 프로필에 **존재하고** 빈 문자열이 아닌지 확인 | **IS NOT BLANK** | **N/A** | 이 필터가 `favorite_genre`를 지정하고 고객 프로필에 `favorite_genre` 속성이 있는 경우, 속성 값에 관계없이 사용자는 이 필터에 일치합니다. 예를 들어 사용자는 `sci-fi`, `romance` 또는 다른 값을 가질 수 있습니다.|
| 문자열 속성이 사용자 프로필에 **존재하지 않는지** 확인 | **BLANK** | **N/A** | 이 필터가 `favorite_genre`를 지정하고 고객 프로필에 `favorite_genre` 속성이 없는 경우, 사용자는 이 필터에 일치합니다.|
| 문자열이 입력된 문자열 중 **하나와 정확히 일치하는지** 확인 | **IS ANY OF** | **STRING**<br>대소문자 구분; 여러 문자열 허용(최대 256개) | 이 필터가 `book`, `bookmark`, `reading light`를 지정하고 고객 프로필에 해당 문자열 중 하나 이상이 있는 경우, 사용자는 이 필터에 일치합니다. |
| 문자열 속성이 입력된 문자열 중 **어느 것과도 정확히 일치하지 않는지** 확인 | **IS NONE OF** |**STRING**<br>대소문자 구분; 여러 문자열 허용(최대 256개) | 이 필터가 `book`, `bookmark`, `reading light`를 지정하고 고객 프로필에 해당 문자열이 하나도 포함되어 있지 않은 경우, 사용자는 이 필터에 일치합니다.|
| 문자열 속성이 입력된 문자열 중 **하나와 부분적으로 일치하는지** 확인 | **CONTAINS ANY OF** | **STRING**<br>대소문자 구분; 여러 문자열 허용(최대 256개) | 이 필터가 `gold`를 지정하고 고객 프로필에 `gold_tier` 또는 `former_gold_tier`와 같이 `gold`를 포함하는 문자열이 있는 경우, 사용자는 이 필터에 일치합니다. |
| 문자열 속성이 입력된 문자열 중 **어느 것과도 부분적으로 일치하지 않는지** 확인 | **DOESN'T CONTAIN ANY OF** | **STRING**<br>대소문자 구분; 여러 문자열 허용(최대 256개) | 이 필터가 `gold`를 지정하고 고객 프로필에 `gold`를 포함하는 문자열이 없는 경우, 사용자는 이 필터에 일치합니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
"12-1-2021" 또는 "12/1/2021"과 같은 날짜 문자열은 datetime 오브젝트로 변환되어 [시간 속성](https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#time)으로 처리됩니다.
{% endalert %}

{% alert important %}
**DOES NOT MATCH REGEX** 필터를 사용하여 세분화할 때는 해당 고객 프로필에 값이 할당된 커스텀 속성이 이미 있어야 합니다. Braze에서는 커스텀 속성이 비어 있는지 확인하기 위해 "OR" 로직을 사용하여 사용자가 올바르게 타겟팅되도록 하는 것을 권장합니다.
{% endalert %}

### 배열 {#arrays}

배열 속성은 사용자에 대한 관련 정보 목록을 저장하는 데 적합합니다. 예를 들어 사용자가 시청한 마지막 100개의 콘텐츠를 배열에 저장하면 특정 관심사 기반 세분화가 가능합니다.

기본적으로 속성의 배열 최대 길이는 25로 설정되어 있으며, 개별 배열에 대해 100까지 늘릴 수 있습니다. 예를 들어 "시청한 영화"와 같은 속성을 전송하고 100으로 설정된 경우, 사용자가 101번째 영화를 시청하면 첫 번째 영화가 배열에서 제거되고 가장 최근 영화가 추가됩니다.

이 최대값을 늘리려면 고객 성공 매니저에게 문의하세요. 대시보드 관리자는 **설정 관리** 페이지의 **커스텀 속성** 탭에서 개별 배열의 최대 길이를 100 이상으로 늘릴 수 있습니다.

단어 사이, 앞 또는 뒤에 공백이 포함된 값을 입력하면 Braze도 동일한 공백을 확인합니다.

{% alert note %}
속성이 데이터 유형을 자동으로 감지하도록 설정된 경우 최대 길이를 늘리는 옵션을 사용할 수 없습니다. 데이터 유형을 배열로 설정해야 합니다.
{% endalert %}

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 | 예시 |
| ---------------------| --------------- | ------------- | -------- |
| 배열 속성이 입력된 값과 **정확히 일치하는 값을 포함하는지** 확인| **INCLUDES VALUE** | **STRING** | 이 필터가 `sci-fi`를 지정하고 고객 프로필에 `sci-fi` 값이 있는 경우, 사용자는 이 필터에 일치합니다.|
| 배열 속성이 입력된 값과 **정확히 일치하는 값을 포함하지 않는지** 확인| **DOESN'T INCLUDE VALUE** | **STRING** | 이 필터가 `sci-fi`를 지정하고 고객 프로필에 `sci-fi` 값이 없는 경우, 사용자는 이 필터에 일치합니다.|
| 배열 속성이 입력된 값 **또는** 정규표현식과 **부분적으로 일치하는 값을 포함하는지** 확인 | **MATCHES REGEX** | **STRING** **또는** **REGULAR EXPRESSION**<br>최대 32,764자 | |
| 배열 속성에 **값이 있거나** 비어 있지 않은지 확인 | **HAS A VALUE** | **N/A** | 이 필터가 `favorite_genres`를 지정하고 고객 프로필에 어떤 값이든 포함된 `favorite_genres`가 있는 경우, 사용자는 이 필터에 일치합니다. |
| 배열 속성이 **비어 있거나** 존재하지 않는지 확인 | **IS EMPTY** | **N/A** | 이 필터가 `favorite_genres`를 지정하고 고객 프로필에 `favorite_genres`가 없거나 `favorite_genres`가 있지만 값이 없는 경우, 사용자는 이 필터에 일치합니다.|
| 배열 속성이 입력된 값 중 **하나와 정확히 일치하는 값을 포함하는지** 확인 | **INCLUDES ANY OF** | **STRING**<br>대소문자 구분; 여러 값 허용(최대 256개) | 이 필터가 `sci-fi, fantasy, romance`를 지정하고 고객 프로필에 `sci-fi`, `fantasy`, `romance`의 조합이 있는 경우(하나만 있는 경우, 예: `sci-fi`만 포함). 사용자는 `sci-fi`, `fantasy`, `romance` 중 하나라도 있으면 `horror` 또는 다른 값도 가질 수 있습니다.|
| 배열 속성이 입력된 값 중 **어느 것과도 정확히 일치하는 값을 포함하지 않는지** 확인 | **INCLUDES NONE OF** | **STRING**<br>대소문자 구분; 여러 값 허용(최대 256개) | 이 필터가 `sci-fi, fantasy, romance`를 지정하고 고객 프로필에 `sci-fi`, `fantasy`, `romance`의 조합이 없는 경우, 사용자는 이 필터에 일치합니다. 사용자는 `sci-fi`, `fantasy`, `romance`가 없으면 `horror` 또는 다른 값을 가질 수 있습니다.|
| 배열 속성이 입력된 값 중 **하나와 부분적으로 일치하는 값을 포함하는지** 확인 | **VALUES CONTAIN ANY OF** | **STRING**<br>대소문자 구분; 여러 값 허용(최대 256개) | 이 필터가 `gold`를 지정하고 고객 프로필 배열에 하나 이상의 문자열에 `gold`가 포함된 경우, 사용자는 이 필터에 일치합니다. `gold_tier`, `former_gold_tier` 등의 문자열 값이 포함됩니다.|
| 배열 속성이 입력된 값 중 **어느 것과도 부분적으로 일치하는 값을 포함하지 않는지** 확인 | **VALUES DON'T CONTAIN ANY OF** | **STRING**<br>대소문자 구분; 여러 값 허용(최대 256개) | 이 필터가 `gold`를 지정하고 고객 프로필 배열에 어떤 문자열에도 `gold`가 포함되어 있지 않은 경우, 사용자는 이 필터에 일치합니다. 즉, `gold_tier` 및 `former_gold_tier`와 같은 문자열 값을 가진 사용자는 이 필터에 일치하지 않습니다.|
| 배열 속성이 입력된 값을 **모두 포함하는지** 확인 | **IS ALL OF** | **STRING**<br>대소문자 구분; 여러 값 허용(최대 256개) | 이 필터가 `sci-fi, fantasy, romance`를 지정하고 고객 프로필에 해당 값이 모두 있는 경우, 사용자는 이 필터에 일치합니다. 사용자는 `horror` 또는 다른 값도 가지고 있어도 이 필터에 일치합니다.|
| 배열 속성이 입력된 값을 **모두 포함하지 않는지** 확인 | **ISN'T ALL OF** | **STRING**<br>대소문자 구분; 여러 값 허용(최대 256개)| 이 필터가 `sci-fi, fantasy, romance`를 지정하고 고객 프로필에 해당 값이 모두 있지 않은 경우, 사용자는 이 필터에 일치합니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
정규표현식(regex) 사용 방법에 대한 자세한 내용은 다음 리소스를 참조하세요.
- [Perl 호환 정규표현식(PCRE)](https://www.regextester.com/pregsyntax.html)
- [Braze에서의 정규표현식](https://www.braze.com/docs/user_guide/engagement_tools/segments/regex/)
- [정규표현식 디버거 및 테스터](https://www.regex101.com/)
- [정규표현식 튜토리얼](https://www.medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

### 시간 {#time}

시간 속성은 특정 행동이 마지막으로 수행된 시간을 저장하는 데 유용하며, 사용자에게 콘텐츠별 재참여 메시지를 제공할 수 있습니다.

상대적 날짜를 사용하는 시간 필터(예: 1일 전 이상, 2일 전 미만)는 1일을 24시간으로 측정합니다. 이러한 필터를 사용하여 실행하는 모든 Campaign은 24시간 단위로 모든 사용자를 포함합니다. 예를 들어 `last used app more than 1 day ago`는 Campaign이 실행되는 정확한 시간으로부터 "24시간 이상 전에 마지막으로 앱을 사용한" 모든 사용자를 캡처합니다. 더 긴 날짜 범위로 설정된 Campaign에도 동일하게 적용됩니다. 따라서 활성화로부터 5일은 이전 120시간을 의미합니다.

예를 들어 미래 24시간에서 48시간 사이의 시간 속성을 가진 사용자를 타겟팅하는 Segment를 구축하려면 `in more than 1 day in the future` 및 `in less than 2 days in the future` 필터를 적용합니다.

{% alert warning %}
커스텀 이벤트 또는 구매 이벤트가 마지막으로 발생한 날짜는 자동으로 기록되므로 커스텀 시간 속성을 통해 다시 기록하면 안 됩니다.
{% endalert %}

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 | 예시 |
| ---------------------| --------------- | ------------- | -------- |
| 시간 속성이 **선택한 날짜 이전인지** 확인| **BEFORE** | **캘린더 날짜 선택기** | 이 필터가 `2024-01-31`을 지정하고 고객 프로필에 `2024-1-31` 이전 날짜가 있는 경우, 사용자는 이 필터에 일치합니다. |
| 시간 속성이 **선택한 날짜 이후인지** 확인| **AFTER** | **캘린더 날짜 선택기** | 이 필터가 `2024-01-31`을 지정하고 고객 프로필에 `2024-1-31` 이후 날짜가 있는 경우, 사용자는 이 필터에 일치합니다. |
| 시간 속성이 **X일 전보다 이전인지** 확인 | **MORE THAN** | **일 전 숫자** | 이 필터가 `7`을 지정하고 고객 프로필에 7일 전보다 이전인 날짜가 있는 경우, 사용자는 이 필터에 일치합니다. |
| 시간 속성이 **X일 전보다 이후인지** 확인| **LESS THAN** | **일 전 숫자** | 이 필터가 `7`을 지정하고 고객 프로필에 7일 전보다 이후인 날짜가 있는 경우, 사용자는 이 필터에 일치합니다.|
| 시간 속성이 **미래 X일 이상인지** 확인 | **IN MORE THAN** | **미래 일 수** | 이 필터가 `7`을 지정하고 고객 프로필에 미래 7일 이상인 날짜가 있는 경우, 사용자는 이 필터에 일치합니다.|
| 시간 속성이 **미래 X일 미만인지** 확인 | **IN LESS THAN** | **미래 일 수**  | 이 필터가 `7`을 지정하고 고객 프로필에 미래 7일 미만인 날짜가 있는 경우, 사용자는 이 필터에 일치합니다.|
| 시간 속성이 사용자 프로필에 **존재하고** null이 아닌지 확인 | **IS NOT BLANK** | **N/A** | 이 필터가 고객 프로필에 있는 시간 속성을 지정하는 경우, 사용자는 이 필터에 일치합니다.|
| 시간 속성이 사용자 프로필에 **존재하지 않거나** null인지 확인 | **IS BLANK** | **N/A** | 이 필터가 고객 프로필에 없는 시간 속성을 지정하는 경우, 사용자는 이 필터에 일치합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 시간 속성 세부 정보 {#time-attribute-details}

- 반복 이벤트의 날짜
  - "반복 이벤트의 날짜" 필터를 사용하고 "반복 이벤트의 캘린더 날짜"를 선택하라는 메시지가 표시되면, `IS LESS THAN` 또는 `IS MORE THAN`을 선택하면 현재 날짜가 해당 세분화 필터에 포함됩니다.
  - 예를 들어 2020년 3월 10일에 속성 날짜를 `LESS THAN ... March 10, 2020`으로 선택한 경우, 2020년 3월 10일을 포함하여 그 이전 날짜의 속성이 고려됩니다.
- X일 전 미만: "X일 전 미만" 필터에는 X일 전부터 현재 날짜/시간 사이의 날짜가 포함됩니다.
- 미래 X일 미만: 현재 날짜/시간부터 미래 X일 사이의 날짜가 포함됩니다.

### 오브젝트 {#objects}

중첩 커스텀 속성을 사용하여 오브젝트를 커스텀 속성의 데이터 유형으로 전송할 수 있습니다. 자세한 내용은 [중첩 커스텀 속성](https://www.braze.com/docs/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/)을 참조하세요.

### 오브젝트 배열 {#arrays-of-objects}

오브젝트 배열을 사용하여 관련 속성을 그룹화할 수 있습니다. 자세한 내용은 [오브젝트 배열](https://www.braze.com/docs/user_guide/data/custom_data/custom_attributes/array_of_objects/) 문서를 참조하세요.

### 통합된 연산자 {#consolidated-operators}

속성 필터, 커스텀 속성 필터 및 중첩 커스텀 속성 필터에서 사용할 수 있는 연산자 목록이 통합되었습니다. 이러한 연산자를 사용하는 기존 필터가 있는 경우 새 연산자를 사용하도록 자동으로 업데이트됩니다.

| 데이터 유형 | 이전 연산자 | 새 연산자 | 값 |
| --- | --- | --- | --- |
| 문자열 | equals | is any of | 최소 1개 값 |
| 문자열 | does not equal | is none of | 최소 1개 값 |
| 배열 | includes value | includes any of | 최소 1개 값 |
| 배열 | doesn't include value | includes none of | 최소 1개 값 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 구매 및 매출 추적 {#purchase-revenue-tracking}

구매 메서드를 사용하여 인앱 구매를 기록하면 각 개별 고객 프로필에 대한 생애주기 가치(LTV)가 설정됩니다. 이 데이터는 매출 페이지에서 시계열로 확인할 수 있습니다.

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 | 예시 |
| ---------------------| --------------- | ------------- | -------- |
| 총 지출 금액이 **숫자**보다 **큰지** 확인| **GREATER THAN** | **NUMBER** | 이 필터가 `500`을 지정하고 고객 프로필에 `500`보다 큰 값이 있는 경우, 사용자는 이 필터에 일치합니다. |
| 총 지출 금액이 **숫자**보다 **작은지** 확인| **LESS THAN** | **NUMBER** | 이 필터가 `500`을 지정하고 고객 프로필에 `500`보다 작은 값이 있는 경우, 사용자는 이 필터에 일치합니다.|
| 총 지출 금액이 **숫자**와 **정확히 일치하는지** 확인| **EXACTLY** | **NUMBER** | 이 필터가 `500`을 지정하고 고객 프로필에 `500` 값이 있는 경우, 사용자는 이 필터에 일치합니다. |
| 마지막 구매가 **X 날짜 이후에** 발생했는지 확인 | **AFTER** | **TIME** | 이 필터가 `2024/31/1`을 지정하고 사용자의 마지막 구매가 `2024/31/1` 이후인 경우, 사용자는 이 필터에 일치합니다.|
| 마지막 구매가 **X 날짜 이전에** 발생했는지 확인 | **BEFORE** | **TIME** | 이 필터가 `2024/31/1`을 지정하고 사용자의 마지막 구매가 `2024/31/1` 이전인 경우, 사용자는 이 필터에 일치합니다.|
| 마지막 구매가 **X일 전보다 이전에** 발생했는지 확인 | **MORE THAN** | **TIME** | 이 필터가 `7`을 지정하고 사용자의 마지막 구매가 오늘로부터 7일 전보다 이전인 경우, 사용자는 이 필터에 일치합니다.|
| 마지막 구매가 **X일 전보다 이후에** 발생했는지 확인 | **LESS THAN** | **TIME** | 이 필터가 `7`을 지정하고 사용자의 마지막 구매가 오늘로부터 7일 전보다 이후인 경우, 사용자는 이 필터에 일치합니다.|
| 구매가 **X회(최대 = 50) 이상** 발생했는지 확인 | **MORE THAN** | 지난 **Y일(Y = 1,3,7,14,21,30)** 동안 | 이 필터가 `7`회 및 `21`일을 지정하고 사용자가 지난 21일 동안 7회 이상 구매한 경우, 사용자는 이 필터에 일치합니다.|
| 구매가 **X회(최대 = 50) 미만** 발생했는지 확인 | **LESS THAN** | 지난 **Y일(Y = 1,3,7,14,21,30)** 동안 | 이 필터가 `7`회 및 `21`일을 지정하고 사용자가 지난 21일 동안 7회 미만 구매한 경우, 사용자는 이 필터에 일치합니다.|
| 구매가 **정확히 X회(최대 = 50)** 발생했는지 확인 | **EXACTLY** | 지난 **Y일(Y = 1,3,7,14,21,30)** 동안 | 이 필터가 `7`회 및 `21`일을 지정하고 사용자가 지난 21일 동안 정확히 7회 구매한 경우, 사용자는 이 필터에 일치합니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
특정 구매가 발생한 횟수를 기준으로 세분화하려면 해당 구매를 [증분 커스텀 속성](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/#incrementingdecrementing-custom-attributes)으로 개별적으로 기록해야 합니다.
{% endalert %}

커스텀 속성의 데이터 유형을 변경할 수 있지만, [데이터 유형 변경](https://www.braze.com/docs/help/help_articles/data/change_custom_data_type/)의 영향에 대해 알고 있어야 합니다.