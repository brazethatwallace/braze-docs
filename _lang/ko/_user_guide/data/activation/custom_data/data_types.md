---
nav_title: 데이터 유형
article_title: 데이터 유형
page_order: 1
page_type: reference
description: "Braze에서 커스텀 속성, 이벤트 속성정보, 카탈로그에 지원되는 데이터 유형에 대한 참조입니다."
toc_headers: h2
---

# 데이터 유형 {#data-types}

> 이 페이지에서는 커스텀 속성, 이벤트 속성정보, 카탈로그에 지원되는 데이터 유형을 통합하여 설명합니다. 각 커스텀 데이터 유형은 지원하는 데이터 유형과 제약 조건이 약간씩 다릅니다.

## 정의 {#definitions}

이 표를 참고하여 고객 프로필 속성, 이벤트 데이터 또는 카탈로그 항목에 사용할 수 있는 데이터 유형을 확인하세요. 각 유형의 사용법과 제약 조건은 이어지는 섹션을 참조하세요.

<table role="presentation" class="definitions-table reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4 reset-td-br-5">
  <thead>
    <tr>
      <th>데이터 유형</th>
      <th>정의</th>
      <th>커스텀 속성</th>
      <th>이벤트 속성정보</th>
      <th>카탈로그</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>부울</td>
      <td>값 <code>true</code> 또는 <code>false</code></td>
      <td>✅ 지원됨</td>
      <td>✅ 지원됨</td>
      <td>✅ 지원됨</td>
    </tr>
    <tr>
      <td>숫자</td>
      <td>정수 또는 소수</td>
      <td>✅ 지원됨</td>
      <td>✅ 지원됨</td>
      <td>✅ 지원됨</td>
    </tr>
    <tr>
      <td>문자열</td>
      <td>텍스트; 255자 이하</td>
      <td>✅ 지원됨</td>
      <td>✅ 지원됨</td>
      <td>✅ 지원됨</td>
    </tr>
    <tr>
      <td>시간</td>
      <td>표준 형식의 날짜 및 시간(<a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a>)</td>
      <td>✅ 지원됨</td>
      <td>✅ 지원됨</td>
      <td>✅ 지원됨</td>
    </tr>
    <tr>
      <td>배열</td>
      <td>정렬된 값 목록</td>
      <td>✅ 지원됨</td>
      <td>✅ 지원됨</td>
      <td>✅ 지원됨</td>
    </tr>
    <tr>
      <td>오브젝트</td>
      <td>명명된 필드가 있는 구조화된 데이터(중첩 키-값)</td>
      <td>✅ 지원됨</td>
      <td>✅ 지원됨</td>
      <td>✅ 지원됨</td>
    </tr>
    <tr>
      <td>오브젝트 배열</td>
      <td>오브젝트 목록</td>
      <td>✅ 지원됨</td>
      <td>❌ 지원되지 않음</td>
      <td>❌ 지원되지 않음</td>
    </tr>
  </tbody>
</table>

### 중요 고려 사항 {#important-considerations}

- **배열:** 커스텀 속성과 이벤트 속성정보에는 크기 제한이 있습니다. 이벤트 속성정보의 배열 내에서는 날짜/시간이 지원되지 않습니다. 카탈로그는 문자열 배열만 지원하며, 최대 100개의 요소를 포함할 수 있습니다.
- **오브젝트:** Braze에서 이 유형은 커스텀 속성의 경우 "중첩 커스텀 속성", 이벤트 속성정보의 경우 "중첩 오브젝트", 카탈로그의 경우 "JSON 오브젝트"로 표시됩니다.
- **시간:** 이벤트 속성정보에서 이 유형은 "Datetime"으로 표시됩니다.

## 커스텀 속성 데이터 유형 {#custom-attribute-data-types}

커스텀 속성은 [정의](#definitions) 표에 나열된 데이터 유형을 지원합니다. 다음은 지원되는 각 데이터 유형의 사용법과 세분화에 대한 설명입니다.

{% tabs %}
{% tab 부울 %}

동작 메뉴에서 커스텀 속성을 개별적으로 차단 목록에 추가하거나, 최대 100개의 속성을 선택하여 일괄 차단 목록에 추가할 수 있습니다. 커스텀 속성을 차단하면 해당 속성에 대한 데이터가 수집되지 않으며, 기존 데이터는 다시 활성화하지 않는 한 사용할 수 없고, 차단 목록에 추가된 속성은 필터나 그래프에 표시되지 않습니다. 또한 해당 속성이 현재 Braze 대시보드의 다른 영역에서 필터나 트리거에 의해 참조되고 있는 경우, 해당 속성을 참조하는 모든 필터 또는 트리거 인스턴스가 제거되고 아카이브된다는 경고 모달이 표시됩니다.

### 개인 식별 정보(PII)로 표시 {#marking-as-personally-identifiable-information-pii}

관리자는 이 페이지에서 커스텀 속성을 생성하고 PII로 표시할 수도 있습니다. 이러한 속성은 관리자와 "View Custom Attributes Marked as PII" 권한이 있는 대시보드 사용자에게만 표시됩니다.

### 설명 추가 {#adding-descriptions}

`Manage Events, Attributes, Purchases` [사용자 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)이 있는 경우 커스텀 속성을 생성한 후 설명을 추가할 수 있습니다. 커스텀 속성을 편집하고 팀을 위한 메모 등 원하는 내용을 입력하세요.

### 태그 추가 {#adding-tags}

"Manage Events, Attributes, Purchases" [사용자 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)이 있는 경우 커스텀 속성을 생성한 후 태그를 추가할 수 있습니다. 그런 다음 태그를 사용하여 속성 목록을 필터링할 수 있습니다.

### 커스텀 속성 제거 {#removing-custom-attributes}

고객 프로필에서 커스텀 속성을 제거하는 방법은 두 가지입니다:

* [사용자 업데이트 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#removing-custom-attributes)에서 제거할 커스텀 속성 이름을 선택합니다.
* [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#user-track)에 대한 API 요청에서 `null` 값을 설정합니다.

#### `null` 값 설정 {#setting-the-null-value}

{% alert important %}
속성을 `null`로 설정하는 것과 `""`(빈 문자열)로 설정하는 것은 같지 않습니다.
{% endalert %}

- `null`은 고객 프로필에서 속성을 완전히 제거합니다. 프로필에 표시되지 않으며 **IS NOT BLANK** 필터와 일치하지 않습니다.
- `""`는 속성을 빈 문자열 값으로 설정합니다. 속성은 프로필에 빈 문자열 값으로 표시되지만, **IS NOT BLANK** 필터와 일치하지 않습니다(빈 값으로 처리됩니다).

또한 `""`는 문자열 유형 속성에만 유효합니다. 대시보드에서 속성의 데이터 유형이 문자열이 아닌 유형(부울, 숫자 또는 시간 등)으로 설정된 경우, `""`를 보내도 값이 지워지지 않으므로 대신 `null`을 사용하세요.

### 데이터 내보내기 {#exporting-data}

커스텀 속성 목록을 CSV 파일로 내보내려면 페이지 상단에서 **Export all**을 선택합니다. 시스템이 CSV 파일을 생성하고 다운로드 링크를 이메일로 보내드립니다.

## 사용 보고서 보기 {#viewing-usage-reports}

사용 보고서에는 특정 커스텀 속성을 사용하는 모든 Canvases, Campaigns, Segments가 나열됩니다. 이 목록에는 Liquid 사용은 포함되지 않습니다.

해당 커스텀 속성 옆의 체크박스를 선택한 다음 **View usage report**를 선택하면 한 번에 최대 100개의 사용 보고서를 볼 수 있습니다.

### 값 탭 {#values-tab}

사용 보고서를 볼 때 **Values** 탭을 선택하면 약 250,000명의 사용자 샘플을 기반으로 선택한 커스텀 속성의 상위 값을 확인할 수 있습니다. 결과는 사용자의 하위 집합에서 샘플링되므로 기존의 모든 값이 포함되지 않을 수 있습니다. 따라서 **Values** 탭은 문제 해결이나 모든 사용자의 데이터를 포함해야 하는 사용 사례에는 사용하지 않는 것이 좋습니다.

![선택한 커스텀 속성의 사용 보고서에서 "Values" 탭이 열려 있으며, "US" 및 "PR" 등의 국가 속성 값을 보여주는 원형 차트가 표시됩니다.]({% image_buster /assets/img/usage_report_values.png %}){: style="max-width:80%;"}

## 커스텀 속성 설정 {#setting-custom-attributes}

다음은 다양한 플랫폼에서 커스텀 속성을 설정하는 데 사용되는 메서드 목록입니다.

{% details 플랫폼별 설명서 펼치기 %}

- [Android 및 FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=unity)
- [.NET MAUI (이전 Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/)

{% enddetails %}

## 커스텀 속성 저장 {#custom-attribute-storage}

**고객 프로필**에 저장된 모든 데이터(커스텀 속성 데이터 포함)는 각 프로필이 [활성]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users) 상태인 한 무기한 보존됩니다.

## 커스텀 속성 데이터 유형

커스텀 속성은 뛰어난 타겟팅을 가능하게 하는 매우 유연한 도구입니다.

다음 데이터 유형을 커스텀 속성으로 저장할 수 있습니다:

- [부울](#booleans)
- [숫자](#numbers)
- [문자열](#strings)
- [배열](#arrays)
- [시간](#time)
- [오브젝트]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/)
- [오브젝트 배열]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/)

### 부울 (참/거짓) {#booleans}

부울 속성은 구독 상태와 같은 사용자에 대한 간단한 이진 데이터를 저장하는 데 유용합니다. 변수가 명시적으로 참 또는 거짓 값으로 설정된 사용자뿐만 아니라, 해당 속성이 아직 기록되지 않은 사용자도 찾을 수 있습니다.

**부울** 속성에 대해 다음과 같은 세분화 옵션을 사용할 수 있습니다.

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 | 예시 |
| ---------------------| --------------- | ------------- | -------- |
| 부울 값이 참, 거짓, 참 또는 미설정, 거짓 또는 미설정 중 하나**인지** 확인 | **IS**  | **TRUE**, **FALSE**, **TRUE OR NOT SET**, 또는 **FALSE OR NOT SET** | 이 필터가 `coffee_drinker`를 지정하는 경우, 사용자는 다음 상황에서 이 필터와 일치합니다: <br> {::nomarkdown}<ul><li>이 필터가 <code>true</code>이고 사용자에게 <code>coffee_drinker</code> 값이 있는 경우</li><li>이 필터가 <code>false</code>이고 사용자에게 <code>coffee_drinker</code> 값이 없는 경우</li><li>이 필터가 <code>true or not set</code>이고 사용자에게 <code>coffee_drinker</code> 값이 있거나 값이 없는 경우</li><li>이 필터가 <code>false or not set</code>이고 사용자에게 <code>coffee_drinker</code> 또는 어떤 값도 없는 경우</li></ul>{:/} |
| 부울 값이 사용자 프로필에 **존재하고** null이 아닌지 확인 | **IS NOT BLANK**  | **N/A** | 이 필터가 `coffee_drinker`를 지정하고 사용자에게 `coffee_drinker` 속성에 대한 값이 있는 경우, 사용자는 이 필터와 일치합니다. |
| 부울 값이 사용자 프로필에 **존재하지 않거나** null인지 확인 | **IS BLANK**  | **N/A** | 이 필터가 `coffee_drinker`를 지정하고 사용자에게 `coffee_drinker` 속성이 없거나 `coffee_drinker` 값이 null인 경우, 사용자는 이 필터와 일치합니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Booleans (true/false) #booleans" }

{% endtab %}
{% tab 숫자 %}

{% alert tip %}
지출 금액은 이 방법으로 기록하면 안 됩니다. 대신 [구매 이벤트]({{site.baseurl}}/user_guide/data/activation/events/purchase_events/)를 통해 기록해야 합니다.
{% endalert %}

**숫자** 속성에 대해 다음과 같은 세분화 옵션을 사용할 수 있습니다.

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 | 예시 |
| ---------------------| --------------- | ------------- | -------- |
| 숫자 속성이 **숫자**와 **정확히 일치하는지** 확인| **EXACTLY** | **NUMBER** | 이 필터가 `10`을 지정하고 고객 프로필에 `10` 값이 있는 경우, 사용자는 이 필터와 일치합니다. |
| 숫자 속성이 **숫자**와 **같지 않은지** 확인| **DOES NOT EQUAL** | **NUMBER** | 이 필터가 `10`을 지정하고 고객 프로필에 `10` 값이 없는 경우, 사용자는 이 필터와 일치합니다. |
| 숫자 속성이 **숫자**보다 **큰지** 확인| **MORE THAN** | **NUMBER** | 이 필터가 `10`을 지정하고 고객 프로필에 `10`보다 큰 값이 있는 경우, 사용자는 이 필터와 일치합니다. |
| 숫자 속성이 **숫자**보다 **작은지** 확인| **LESS THAN** | **NUMBER** | 이 필터가 `10`을 지정하고 고객 프로필에 `10`보다 작은 값이 있는 경우, 사용자는 이 필터와 일치합니다. |
| 숫자 속성이 사용자 프로필에 **존재하고** null이 아닌지 확인 | **IS NOT BLANK** | **N/A** | 고객 프로필에 지정된 숫자 속성이 포함되어 있으면 값에 관계없이 사용자는 이 필터와 일치합니다. |
| 숫자 속성이 사용자 프로필에 **존재하지 않거나** null인지 확인 | **IS BLANK** | **N/A** | 고객 프로필에 지정된 숫자 속성이 포함되어 있지 않거나 속성 값이 null인 경우, 사용자는 이 필터와 일치합니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Booleans (true/false) #booleans" }

#### 숫자 속성 세부 정보 {#number-attribute-details}

- "정확히 0" 및 "미만" 필터에는 NULL 필드가 있는 사용자가 포함됩니다
  - 커스텀 속성에 값이 없는 사용자를 제외하려면 **is not blank** 필터를 포함해야 합니다.

{% endtab %}
{% tab 문자열 %}

문자열 속성은 최대 255자까지 가능합니다. 단어 사이, 앞 또는 뒤에 공백이 포함된 값을 입력하면 Braze도 동일한 공백을 확인합니다.

**문자열** 속성에 대해 다음과 같은 세분화 옵션을 사용할 수 있습니다.

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 | 예시 |
| ---------------------| --------------- | ------------- | -------- |
| 문자열 속성이 입력된 문자열 **또는** 정규표현식과 **부분적으로 일치하는지** 확인 | **MATCHES REGEX** | **STRING** **또는** **REGULAR EXPRESSION** <br>대소문자 구분 없음; 최대 32,764자 |
| 문자열 속성이 입력된 문자열 **또는** 정규표현식과 **부분적으로 일치하지 않는지** 확인 | **DOES NOT MATCH REGEX** * | **STRING** **또는** **REGULAR EXPRESSION**<br>대소문자 구분 없음; 최대 32,764자 |
| 문자열 속성이 사용자 프로필에 **존재하고** 빈 문자열이 아닌지 확인 | **IS NOT BLANK** | **N/A** | 이 필터가 `favorite_genre`를 지정하고 고객 프로필에 `favorite_genre` 속성이 있는 경우, 속성 값에 관계없이 사용자는 이 필터와 일치합니다. 예를 들어 사용자는 `sci-fi`, `romance` 또는 다른 값을 가질 수 있습니다.|
| 문자열 속성이 사용자 프로필에 **존재하지 않는지** 확인 | **BLANK** | **N/A** | 이 필터가 `favorite_genre`를 지정하고 고객 프로필에 `favorite_genre` 속성이 없는 경우, 사용자는 이 필터와 일치합니다.|
| 문자열이 입력된 문자열 중 **하나와 정확히 일치하는지** 확인 | **IS ANY OF** | **STRING**<br>대소문자 구분; 여러 문자열 허용(최대 256개) | 이 필터가 `book`, `bookmark`, `reading light`를 지정하고 고객 프로필에 해당 문자열 중 하나 이상이 있는 경우, 사용자는 이 필터와 일치합니다. |
| 문자열 속성이 입력된 문자열 중 **어느 것과도 정확히 일치하지 않는지** 확인 | **IS NONE OF** |**STRING**<br>대소문자 구분; 여러 문자열 허용(최대 256개) | 이 필터가 `book`, `bookmark`, `reading light`를 지정하고 고객 프로필에 해당 문자열이 포함되어 있지 않은 경우, 사용자는 이 필터와 일치합니다.|
| 문자열 속성이 입력된 문자열 중 **하나와 부분적으로 일치하는지** 확인 | **CONTAINS ANY OF** | **STRING**<br>대소문자 구분; 여러 문자열 허용(최대 256개) | 이 필터가 `gold`를 지정하고 고객 프로필에 `gold_tier` 또는 `former_gold_tier`와 같이 `gold`가 포함된 문자열이 있는 경우, 사용자는 이 필터와 일치합니다. |
| 문자열 속성이 입력된 문자열 중 **어느 것과도 부분적으로 일치하지 않는지** 확인 | **DOESN'T CONTAIN ANY OF** | **STRING**<br>대소문자 구분; 여러 문자열 허용(최대 256개) | 이 필터가 `gold`를 지정하고 고객 프로필에 `gold`가 포함된 문자열이 없는 경우, 사용자는 이 필터와 일치합니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Number attribute details" }

{% multi_lang_include alerts/note_alerts.md alert='Custom Attributes time attribute' %}

{% alert important %}
**DOES NOT MATCH REGEX** 필터를 사용하여 세분화할 때, 해당 고객 프로필에 이미 값이 할당된 커스텀 속성이 있어야 합니다. Braze는 사용자가 올바르게 타겟팅되도록 커스텀 속성이 비어 있는지 확인하기 위해 "OR" 로직을 사용할 것을 권장합니다.
{% endalert %}

{% endtab %}
{% tab 배열 %}

배열의 최대 크기는 100&nbsp;KB입니다. 속성의 기본 길이는 최대 500개 항목입니다(예: "시청한 영화"와 같은 속성을 500으로 설정한 경우, 사용자가 501번째 영화를 시청하면 첫 번째 영화가 제거되고 가장 최근 영화가 추가됩니다). 단어 사이, 앞 또는 뒤에 공백이 포함된 값을 입력하면 Braze도 동일한 공백을 확인합니다.

배열 유형 커스텀 속성은 [CSV 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/)를 통해 가져올 수 없습니다. 배열 값을 업로드하려면 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 또는 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/cloud_ingestion/)을 사용하세요.

{% alert note %}
속성이 데이터 유형을 자동으로 감지하도록 설정된 경우 최대 길이를 늘리는 옵션을 사용할 수 없습니다. 데이터 유형을 배열로 설정해야 합니다.
{% endalert %}

**배열** 속성에 대해 다음과 같은 세분화 옵션을 사용할 수 있습니다.

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 | 예시 |
| ---------------------| --------------- | ------------- | -------- |
| 배열 속성이 입력된 값과 **정확히 일치하는 값을 포함하는지** 확인| **INCLUDES VALUE** | **STRING** | 이 필터가 `sci-fi`를 지정하고 고객 프로필에 `sci-fi` 값이 있는 경우, 사용자는 이 필터와 일치합니다.|
| 배열 속성이 입력된 값과 **정확히 일치하는 값을 포함하지 않는지** 확인| **DOESN'T INCLUDE VALUE** | **STRING** | 이 필터가 `sci-fi`를 지정하고 고객 프로필에 `sci-fi` 값이 없는 경우, 사용자는 이 필터와 일치합니다.|
| 배열 속성이 입력된 값 **또는** 정규표현식과 **부분적으로 일치하는 값을 포함하는지** 확인 | **MATCHES REGEX** | **STRING** **또는** **REGULAR EXPRESSION**<br>최대 32,764자 | |
| 배열 속성에 **값이 있거나** 비어 있지 않은지 확인 | **HAS A VALUE** | **N/A** | 이 필터가 `favorite_genres`를 지정하고 고객 프로필에 어떤 값이든 포함된 `favorite_genres`가 있는 경우, 사용자는 이 필터와 일치합니다. |
| 배열 속성이 **비어 있거나** 존재하지 않는지 확인 | **IS EMPTY** | **N/A** | 이 필터가 `favorite_genres`를 지정하고 고객 프로필에 `favorite_genres`가 없거나 `favorite_genres`가 있지만 값이 없는 경우, 사용자는 이 필터와 일치합니다.|
| 배열 속성이 입력된 값 중 **하나와 정확히 일치하는 값을 포함하는지** 확인 | **INCLUDES ANY OF** | **STRING**<br>대소문자 구분; 여러 값 허용(최대 256개) | 이 필터가 `sci-fi, fantasy, romance`를 지정하고 고객 프로필에 `sci-fi`, `fantasy` 또는 `romance`의 조합이 있는 경우(하나만 있는 경우, 예: `sci-fi`만 있는 경우 포함). 사용자는 `sci-fi`, `fantasy`, `romance` 중 하나라도 있으면 `horror` 또는 다른 값도 가질 수 있습니다.|
| 배열 속성이 입력된 값 중 **어느 것과도 정확히 일치하는 값을 포함하지 않는지** 확인 | **INCLUDES NONE OF** | **STRING**<br>대소문자 구분; 여러 값 허용(최대 256개) | 이 필터가 `sci-fi, fantasy, romance`를 지정하고 고객 프로필에 `sci-fi`, `fantasy` 또는 `romance`의 조합이 없는 경우, 사용자는 이 필터와 일치합니다. 사용자는 `sci-fi`, `fantasy`, `romance` 중 어느 것도 없다면 `horror` 또는 다른 값을 가질 수 있습니다.|
| 배열 속성이 입력된 값 중 **하나와 부분적으로 일치하는 값을 포함하는지** 확인 | **VALUES CONTAIN ANY OF** | **STRING**<br>대소문자 구분; 여러 값 허용(최대 256개) | 이 필터가 `gold`를 지정하고 고객 프로필 배열에 하나 이상의 문자열에 `gold`가 포함되어 있는 경우, 사용자는 이 필터와 일치합니다. 여기에는 `gold_tier`, `former_gold_tier` 등의 문자열 값이 포함됩니다.|
| 배열 속성이 입력된 값 중 **어느 것과도 부분적으로 일치하는 값을 포함하지 않는지** 확인 | **VALUES DON'T CONTAIN ANY OF** | **STRING**<br>대소문자 구분; 여러 값 허용(최대 256개) | 이 필터가 `gold`를 지정하고 고객 프로필 배열에 어떤 문자열에도 `gold`가 포함되어 있지 않은 경우, 사용자는 이 필터와 일치합니다. 즉, `gold_tier` 및 `former_gold_tier`와 같은 문자열 값을 가진 사용자는 이 필터와 일치하지 않습니다.|
| 배열 속성이 입력된 값을 **모두 포함하는지** 확인 | **IS ALL OF** | **STRING**<br>대소문자 구분; 여러 값 허용(최대 256개) | 이 필터가 `sci-fi, fantasy, romance`를 지정하고 고객 프로필에 해당 값이 모두 있는 경우, 사용자는 이 필터와 일치합니다. 사용자는 `horror` 또는 다른 값도 가지고 있어도 이 필터와 일치할 수 있습니다.|
| 배열 속성이 입력된 값을 **모두 포함하지 않는지** 확인 | **ISN'T ALL OF** | **STRING**<br>대소문자 구분; 여러 값 허용(최대 256개)|  이 필터가 `sci-fi, fantasy, romance`를 지정하고 고객 프로필에 해당 값이 모두 있지 않은 경우, 사용자는 이 필터와 일치합니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Number attribute details" }

{% alert tip %}
정규표현식(regex) 사용 방법에 대한 자세한 내용은 다음 리소스를 참조하세요:
- [Perl 호환 정규표현식(PCRE)](https://www.regextester.com/pregsyntax.html)
- [Braze에서의 정규식]({{site.baseurl}}/user_guide/audience/segments/regex/)
- [정규식 디버거 및 테스터](https://www.regex101.com/)
- [정규식 튜토리얼](https://www.medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

{% endtab %}
{% tab 시간 %}

시간 속성은 특정 동작이 마지막으로 수행된 시간을 저장하는 데 유용하므로, 사용자에게 콘텐츠별 재참여 메시징을 제공할 수 있습니다.

상대적 날짜를 사용하는 시간 필터(예: 1일 전 이상, 2일 전 미만)는 1일을 24시간으로 측정합니다. 이러한 필터를 사용하여 실행하는 모든 Campaign은 24시간 단위로 모든 사용자를 포함합니다. 예를 들어, `last used app more than 1 day ago`는 Campaign이 실행되는 정확한 시간으로부터 "24시간 이상 전에 마지막으로 앱을 사용한" 모든 사용자를 캡처합니다. 더 긴 날짜 범위로 설정된 Campaign에도 동일하게 적용됩니다. 따라서 활성화로부터 5일은 이전 120시간을 의미합니다.

시간 범위 내에 해당하는 시간 속성을 가진 사용자를 타겟팅하려면 두 개의 오디언스 필터를 사용하세요: 하한에는 `in more than`, 상한에는 `in less than`을 사용합니다. 단일 필터로는 해당 범위의 양쪽을 표현할 수 없습니다. 예를 들어, 향후 24시간(지금부터 1일 후 사이) 내의 시간 속성을 가진 사용자를 타겟팅하려면 `in more than 0 days`와 `in less than 1 day`를 적용하세요.

{% alert warning %}
커스텀 이벤트 또는 구매 이벤트가 마지막으로 발생한 날짜는 자동으로 기록되므로 커스텀 시간 속성을 통해 다시 기록하면 안 됩니다.
{% endalert %}

**시간** 속성에 대해 다음과 같은 세분화 옵션을 사용할 수 있습니다.

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 | 예시 |
| ---------------------| --------------- | ------------- | -------- |
| 시간 속성이 **선택한 날짜** **이전인지** 확인| **BEFORE** | **CALENDAR DATE SELECTOR** | 이 필터가 `2024-01-31`을 지정하고 고객 프로필에 `2024-1-31` 이전 날짜가 있는 경우, 사용자는 이 필터와 일치합니다. |
| 시간 속성이 **선택한 날짜** **이후인지** 확인| **AFTER** | **CALENDAR DATE SELECTOR** | 이 필터가 `2024-01-31`을 지정하고 고객 프로필에 `2024-1-31` 이후 날짜가 있는 경우, 사용자는 이 필터와 일치합니다. |
| 시간 속성이 **X일** **이전보다 더 오래되었는지** 확인 | **MORE THAN** | **NUMBER OF DAYS AGO** | 이 필터가 `7`을 지정하고 고객 프로필에 7일 이전보다 더 오래된 날짜가 있는 경우, 사용자는 이 필터와 일치합니다. |
| 시간 속성이 **X일** **이전보다 덜 오래되었는지** 확인| **LESS THAN** | **NUMBER OF DAYS AGO** | 이 필터가 `7`을 지정하고 고객 프로필에 7일 이전보다 덜 오래된 날짜가 있는 경우, 사용자는 이 필터와 일치합니다.|
| 시간 속성이 **미래 X일** **이후인지** 확인 | **IN MORE THAN** | **NUMBER OF DAYS IN FUTURE** | 이 필터가 `7`을 지정하고 고객 프로필에 미래 7일 이후의 날짜가 있는 경우, 사용자는 이 필터와 일치합니다.|
| 시간 속성이 **미래 X일** **이내인지** 확인 | **IN LESS THAN** | **NUMBER OF DAYS IN FUTURE**  | 이 필터가 `7`을 지정하고 고객 프로필에 미래 7일 이내의 날짜가 있는 경우, 사용자는 이 필터와 일치합니다.|
| 시간 속성이 사용자 프로필에 **존재하고** null이 아닌지 확인 | **IS NOT BLANK** | **N/A** | 이 필터가 고객 프로필에 있는 시간 속성을 지정하는 경우, 사용자는 이 필터와 일치합니다.|
| 시간 속성이 사용자 프로필에 **존재하지 않거나** null인지 확인 | **IS BLANK** | **N/A** | 이 필터가 고객 프로필에 없는 시간 속성을 지정하는 경우, 사용자는 이 필터와 일치합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Number attribute details" }

#### 시간 속성 세부 정보 {#time-attribute-details}

- 반복 이벤트의 날짜
  - "반복 이벤트의 날짜" 필터를 사용하고 "반복 이벤트의 캘린더 날짜"를 선택하라는 메시지가 표시되면, `IS LESS THAN` 또는 `IS MORE THAN`을 선택한 경우 현재 날짜가 해당 세분화 필터에 포함됩니다.
  - 예를 들어, 2020년 3월 10일에 속성 날짜를 `LESS THAN ... March 10, 2020`으로 선택한 경우, 2020년 3월 10일을 포함하여 그 이전 날짜의 속성이 고려됩니다.
- X일 전 미만: "X일 전 미만" 필터에는 X일 전부터 현재 날짜/시간 사이의 날짜가 포함됩니다.
- 미래 X일 이내: 현재 날짜/시간부터 미래 X일 사이의 날짜가 포함됩니다.

{% endtab %}
{% tab 오브젝트 %}

중첩 커스텀 속성을 사용하여 오브젝트를 커스텀 속성의 데이터 유형으로 전송할 수 있습니다. 자세한 내용은 [중첩 커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support/)을 참조하세요.

{% endtab %}
{% tab 오브젝트 배열 %}

오브젝트 배열을 사용하여 관련 속성을 그룹화할 수 있습니다. 자세한 내용은 [오브젝트 배열]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects/)을 참조하세요.

{% endtab %}
{% endtabs %}

커스텀 속성의 데이터 유형을 변경할 수 있지만, 그 영향을 인지해야 합니다. 자세한 내용은 [커스텀 속성 또는 이벤트 데이터 유형 변경](#changing-custom-attribute-or-event-data-type)을 참조하세요.

### 통합된 연산자 {#consolidated-operators}

속성 필터, 커스텀 속성 필터, 중첩 커스텀 속성 필터에서 사용할 수 있는 연산자 목록을 통합했습니다. 이러한 연산자를 사용하는 기존 필터가 있는 경우, 새 연산자를 사용하도록 자동으로 업데이트됩니다.

| 데이터 유형 | 이전 연산자 | 새 연산자 | 값 |
| --- | --- | --- | --- |
| 문자열 | equals | is any of | 최소 1개 값 |
| 문자열 | does not equal | is none of | 최소 1개 값 |
| 배열 | includes value | includes any of | 최소 1개 값 |
| 배열 | doesn't include value | includes none of | 최소 1개 값 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Consolidated operators #consolidated-operators" }

## 이벤트 속성정보 데이터 유형 {#event-property-data-types}

이벤트를 기록할 때 추가 정보(예: 제품 이름 또는 가격)를 이벤트 속성정보로 첨부할 수 있습니다. 각 속성정보에는 이름과 값이 있습니다. 이벤트 속성정보 값은 [정의](#definitions) 표의 데이터 유형을 지원합니다(이벤트 속성정보에서 시간은 "Datetime"으로 표시됩니다).

### 예상 형식 {#expected-format}

속성정보 값은 오브젝트로 전송됩니다: 키는 속성정보 이름이고, 값은 속성정보 값입니다. 속성정보 이름은 비어 있지 않은 문자열이어야 하며, 255자 이하이고, 앞에 달러 기호(`$`)가 없어야 합니다.

이벤트 속성정보 관련 규칙:

- **시간 (Datetime):** [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) 또는 `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 형식을 사용합니다. 배열 내에서는 지원되지 않습니다.
- **배열:** 배열 내에서는 날짜/시간이 지원되지 않습니다.
- **중첩 오브젝트:** [중첩 오브젝트]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects/)를 참조하세요.
- **페이로드:** 배열 또는 오브젝트 값을 포함하는 이벤트 속성정보 오브젝트는 최대 102,400바이트(100&nbsp;KiB)까지 가능합니다.

커스텀 이벤트 속성정보의 데이터 유형을 변경할 수 있지만, 데이터가 수집된 후 [데이터 유형을 변경](#changing-custom-attribute-or-event-data-type)하는 것의 영향을 인지해야 합니다.

이벤트 속성정보의 전체 동작, 예약 키, 트리거 및 개인화에서의 사용에 대해서는 [커스텀 이벤트 속성정보]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties/)를 참조하세요.

## 구매 이벤트 및 매출 {#purchase-events-and-revenue}

구매 및 매출 데이터는 [구매 이벤트]({{site.baseurl}}/user_guide/data/activation/events/purchase_events/) 또는 권장 이커머스 이벤트를 통해 기록됩니다.

{% alert note %}
권장 이벤트에는 설정된 데이터 유형이 포함된 사전 정의된 스키마가 있습니다. 자세한 내용은 [이커머스 권장 이벤트]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/)를 참조하세요.
{% endalert %}

구매 이벤트를 기록하면 각 고객 프로필에 대한 생애주기 가치(LTV)가 설정되며, 이 데이터는 매출 페이지에서 시계열로 확인할 수 있습니다. 지출 금액, 마지막 구매 날짜, 기간 내 구매 횟수 등으로 세분화할 수 있습니다.

### 구매 이벤트 속성정보 데이터 유형 {#purchase-event-property-data-types}

구매 이벤트 속성정보 값(구매의 `properties` 오브젝트)은 [정의](#definitions) 표의 데이터 유형을 지원하며, [이벤트 속성정보](#expected-format)와 동일한 구조 및 명명 규칙을 따릅니다.

{% include data_activation/purchase_event_property_data_types.md %}

전체 구매 오브젝트 스키마 및 예시는 [구매 오브젝트]({{site.baseurl}}/api/objects_filters/purchase_object/)를 참조하세요. 구매 이벤트 기록, 세분화 필터 및 전체 세부 정보는 [구매 이벤트]({{site.baseurl}}/user_guide/data/activation/events/purchase_events/)를 참조하세요.

## 커스텀 속성 또는 이벤트 데이터 유형 변경 {#changing-custom-attribute-or-event-data-type}

커스텀 속성 또는 이벤트의 데이터 유형을 변경하려면:

1. **데이터 설정**으로 이동하여 **커스텀 속성** 또는 **커스텀 이벤트**를 선택합니다.
2. 목록에서 속성 또는 이벤트를 찾고 <i class="fa fa-ellipsis-v" aria-hidden="true"></i> **추가 동작**을 선택합니다.
3. 드롭다운에서 새 **데이터 유형**을 선택합니다.
4. **저장**을 선택합니다.

커스텀 속성 또는 이벤트의 데이터 유형을 변경하는 경우(예: `time`을 `string`으로 변경), 다음 사항을 고려하세요:

- **필터가 자동으로 업데이트되지 않습니다.** 변경된 속성 또는 이벤트를 사용하는 Segments, Campaigns, Canvases 또는 기타 위치는 업데이트되지 않습니다. 데이터 유형을 변경하기 전에 Segments 또는 필터에서 해당 속성을 사용하는 Campaigns이나 Canvases를 중지하고, 해당 속성을 참조하는 필터에서 속성을 제거하세요.
- **기존 사용자 데이터는 소급 업데이트되지 않습니다.** 변경 전에 고객 프로필에 변경된 속성이 있었다면, 해당 값은 이전 데이터 유형으로 유지됩니다. 필터가 새 데이터 유형을 찾기 때문에 사용자가 변경된 속성을 포함하는 Segment에서 빠질 수 있습니다. 해당 고객 프로필을 업데이트하여(예: [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 사용) 새 유형과 일치하도록 하고 필요한 경우 Segment에 다시 포함되도록 하세요.
- **새 데이터는 새 유형과 일치해야 합니다.** 변경된 속성에 대해 이전 데이터 유형을 전송하는 API 호출은 수락되지 않습니다. 새 데이터 유형을 전송하세요.

{% alert important %}
자동 감지가 커스텀 속성 데이터 유형을 업데이트하는 것을 방지하는 기능은 현재 얼리 액세스 중입니다. 참여에 관심이 있으시면 고객 성공 매니저에게 문의하세요.
{% endalert %}

## 카탈로그 데이터 유형 {#catalog-data-types}

카탈로그는 [정의](#definitions) 표에 나열된 유형을 지원합니다. 다음 표에는 각 유형, 생성 또는 업데이트 방법, 형식 및 예시가 나와 있습니다.

| 데이터 유형 | 설명 | CSV 업로드로 사용 가능 | API 및 CDI로 사용 가능 |
| --- | --- | --- | --- |
| 문자열 | 문자 시퀀스(예: 이름, 설명, ID). | ✅ 예 | ✅ 예 |
| 숫자 | 정수 또는 플로트 숫자 값(예: 가격, 수량, 평점). | ✅ 예 | ✅ 예 |
| 부울 | `true` 또는 `false` 값. | ✅ 예 | ✅ 예 |
| 시간 | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) 형식 또는 초 단위 Unix 타임스탬프의 날짜 및 시간. | ✅ 예 | ✅ 예 |
| JSON 오브젝트 (오브젝트) | 키-값 페어가 있는 중첩 오브젝트. 플랫폼에 표시되지만 API 또는 CDI를 통해서만 생성하거나 업데이트할 수 있습니다. | ❌ 아니요 | ✅ 예 |
| 문자열 배열 (배열) | 문자열 목록. 플랫폼에 표시되지만 API 또는 CDI를 통해서만 생성하거나 업데이트할 수 있습니다. 최대 100개 요소. | ❌ 아니요 | ✅ 예 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Catalog data types #catalog-data-types" }

### 형식 및 예시 {#format-and-examples}

| 데이터 유형 | 형식 | 예시 |
| --- | --- | --- |
| 문자열 | 텍스트 | <code>"Hello World"</code> |
| 시간 | ISO 8601 또는 Unix 타임스탬프(초) | <code>"2024-03-15T14:30:00Z"</code> |
| 부울 | <code>true</code> 또는 <code>false</code> | <code>true</code> |
| 숫자 | 정수 또는 소수 | <code>42</code> 또는 <code>19.99</code> |
| 오브젝트 | JSON 오브젝트 | <code>{"key": "value", "price": 10}</code> |
| 배열 | 문자열 배열 | <code>["red", "blue", "green"]</code> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Format and examples" }

카탈로그 생성 및 업데이트에 대해서는 [카탈로그 생성]({{site.baseurl}}/user_guide/data/activation/catalogs/create/)을 참조하세요.