---
nav_title: 커스텀 데이터 관리
article_title: 커스텀 데이터 관리
page_order: 2
page_type: reference
description: "이 참조 문서에서는 커스텀 이벤트와 속성을 미리 채우고, 설명과 태그를 추가하고, 이벤트 등록정보를 관리하고, 데이터 유형을 강제 지정하고, 속성을 PII로 표시하는 등 커스텀 데이터를 관리하는 방법을 다룹니다."
---

# 커스텀 데이터 관리 {#manage-custom-data}

> 이 페이지에서는 Campaign(캠페인) 및 Segment에 커스텀 데이터를 미리 채우고, 커스텀 이벤트와 속성 및 등록정보를 관리하고, 데이터 유형을 구성하는 방법을 다룹니다. 커스텀 데이터의 차단 및 삭제에 대해서는 [커스텀 데이터 차단]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data)을 참조하세요.

특히 커스텀 속성을 관리하는 방법(설명 추가, 태그 추가, 속성을 PII로 표시하는 방법 포함)을 알아보려면 [커스텀 속성 관리하기]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#managing-custom-attributes)를 참조하세요.

## 커스텀 데이터 미리 채우기 {#pre-populate-custom-data}

개발 팀이 해당 커스텀 데이터를 통합하기 전에 커스텀 데이터를 사용하여 캠페인 및 Segment를 설정하고 싶은 경우가 있을 수 있습니다. Braze에서는 이러한 데이터가 추적되기 전에 대시보드에서 커스텀 이벤트 및 속성을 미리 채워서 드롭다운 및 캠페인 생성 프로세스의 일부로 사용할 수 있도록 합니다.

커스텀 이벤트 및 속성을 미리 채우려면 다음을 수행합니다:

1. **데이터 설정** > **커스텀 이벤트** 또는 **커스텀 속성** 또는 **제품**으로 이동합니다.

![커스텀 속성 또는 커스텀 이벤트 또는 제품으로 이동합니다.]({% image_buster /assets/img_archive/prepopulate_page.png %}){: style="max-width:90%;" }

{: start="2"}
2. 커스텀 속성, 이벤트 또는 제품을 추가하려면 해당 페이지로 이동하여 **커스텀 속성 추가** 또는 **커스텀 이벤트 추가** 또는 **제품 추가**를 선택합니다.<br><br>커스텀 속성의 경우 이 속성의 [데이터 유형]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types)을 선택합니다(예: 부울 또는 문자열). 속성의 데이터 유형은 해당 속성에 사용할 수 있는 세분화 필터를 결정합니다. <br><br>![새 속성 또는 이벤트 추가]({% image_buster /assets/img_archive/prepopulate_add.png %}){: style="max-width:80%;" }
3. **저장**을 선택합니다.

### 커스텀 이벤트 및 커스텀 속성 이름 지정 {#naming-custom-events-and-custom-attributes}

커스텀 이벤트 및 커스텀 속성은 대소문자를 구분합니다. 나중에 개발 팀이 이러한 커스텀 이벤트 또는 속성을 통합할 때 이 점을 염두에 두세요. 팀은 커스텀 이벤트 또는 속성의 이름을 여기에서 지정한 것과 정확히 동일하게 지정해야 하며, 그렇지 않으면 Braze가 별도의 커스텀 이벤트 또는 속성을 생성합니다.

## 등록정보 관리 {#managing-properties}

커스텀 이벤트 또는 제품을 생성한 후 해당 이벤트 또는 제품에 대해 **등록정보 관리**를 선택하여 새 등록정보를 추가하고, 기존 등록정보를 차단 목록에 추가하고, [트리거 이벤트]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)에서 이 등록정보를 사용하는 Campaign 또는 Canvases를 확인할 수 있습니다.

![커스텀 이벤트의 커스텀 등록정보.]({% image_buster /assets/img_archive/manageproperties1.png %}){: style="max-width:80%"}

이벤트 또는 제품 등록정보를 차단하려면 등록정보 페이지의 동작 메뉴를 사용합니다. 커스텀 속성, 이벤트 또는 제품 전체를 차단하려면 [커스텀 데이터 차단]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data)을 참조하세요.

이러한 추가된 커스텀 속성, 이벤트, 제품 또는 이벤트 등록정보를 추적 가능하게 만들려면 개발 팀에 요청하여 이전에 추가할 때 사용한 것과 정확히 동일한 이름을 사용하여 SDK에서 생성해야 합니다. 또는 Braze [API]({{site.baseurl}}/api/basics)를 사용하여 해당 속성에 대한 데이터를 가져올 수 있습니다. 그러면 커스텀 속성, 이벤트 또는 기타 항목이 활성화되어 사용자에게 적용됩니다.

{% include alerts/note_alerts.md alert='Manage custom data storage' %}

## 환경 간 데이터 유형 감지 {#data-type-detection-across-environments}

Braze는 수신하는 첫 번째 값을 기반으로 커스텀 속성의 데이터 유형을 자동으로 감지합니다. 개발 환경에서 `100`과 같은 숫자 값을 먼저 전송하면 해당 속성은 숫자로 저장됩니다. 프로덕션 환경의 첫 번째 값이 문자열(예: 따옴표로 감싼 `"100"`)로 도착하면 해당 속성은 문자열로 저장됩니다.

이를 방지하려면 모든 환경에서 일관된 데이터 유형을 전송하도록 통합을 구성하세요. 잘못된 유형이 이미 설정된 경우 **데이터 설정** > **커스텀 속성**에서 [데이터 유형 드롭다운](#forcing-data-type-comparisons)을 사용하여 올바른 데이터 유형을 강제 지정할 수 있습니다.

## 데이터 유형 비교 강제 지정 {#forcing-data-type-comparisons}

Braze는 전송된 속성 데이터의 데이터 유형을 자동으로 인식합니다. 그러나 여러 데이터 유형이 단일 속성에 적용되는 경우, 속성의 데이터 유형을 강제로 지정하여 Braze에 실제 유형을 알려줄 수 있습니다. **데이터 유형** 열의 드롭다운에서 선택합니다.

{% alert note %}
2026년 3월 30일부터 자동 감지는 최초 수집 시에만 데이터 유형을 설정합니다. 최초 수집 후 데이터 유형을 변경하려면 다음 단계를 사용하여 수동으로 업데이트하세요.
{% endalert %}

{% alert note %}
데이터 유형 강제 지정은 이벤트 등록정보 또는 구매 속성정보에는 적용되지 않습니다.
{% endalert %}

![커스텀 속성 데이터 유형 드롭다운]({% image_buster /assets/img_archive/custom_events_view_data_type_dropdown.png %})

{% alert warning %}
속성의 데이터 유형을 강제로 지정하면, 지정된 유형이 아닌 데이터가 들어올 경우 해당 유형으로 변환됩니다. 이러한 변환이 불가능한 경우(예: 문자가 포함된 문자열을 숫자로 변환) 데이터는 무시됩니다. 유형 변경 전에 수집된 데이터는 이전 유형으로 계속 저장되며(따라서 세분화가 불가능할 수 있음), 영향을 받는 사용자의 프로필에서 해당 속성 옆에 경고가 표시됩니다.
{% endalert %}

### 유형 변경 후 기존 데이터 {#existing-data-after-a-type-change}

데이터 유형 변경을 강제하면 Braze로 들어오는 새 데이터에만 영향을 미칩니다. 유형 변경 전에 수집된 데이터는 이전 유형으로 계속 저장되며 새 유형의 필터로 세분화가 불가능할 수 있습니다. 영향을 받는 사용자의 프로필에 경고가 표시됩니다. 새로 들어오는 데이터의 경우, 값이 강제 유형과 일치하지 않으면 Braze가 강제 유형으로 변환할 수 있습니다(예: 문자열 `"100"`을 숫자 `100`으로). 변환할 수 없는 값은 무시되며 속성이 업데이트되지 않습니다.

기존 사용자 데이터가 모두 새 유형과 일치해야 하는 경우, SDK, API 또는 CSV 가져오기를 통해 해당 사용자의 속성 값을 다시 전송해야 합니다. 기존 데이터에 대한 자동 일괄 변환은 지원되지 않습니다.

### 데이터 유형 변환 {#data-type-coercion}

| 강제 데이터 유형 | 설명 |
|------------------|-------------|
| 부울 | `1`, `true`, `t`(대소문자 구분 없음) 입력은 `true`로 저장됩니다 |
| 부울 | `0`, `false`, `f`(대소문자 구분 없음) 입력은 `false`로 저장됩니다 |
| 숫자 | 정수 또는 플로트(`1`, `1.5` 등)는 숫자로 저장됩니다 |
| 숫자 | 숫자 문자열(`"100"` 또는 `"3.14"` 등)은 속성이 **숫자**로 강제 지정된 경우 숫자로 변환될 수 있습니다 |
| 문자열 | 숫자 값은 속성이 **문자열**로 강제 지정된 경우 문자열 형태로 변환될 수 있습니다 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="데이터 유형 변환" }

다양한 데이터 유형 비교에서 노출되는 특정 필터 옵션에 대한 자세한 내용은 [보고 구성]({{site.baseurl}}/user_guide/analytics/reports/configure_reporting)을 확인하세요. 사용 가능한 다양한 데이터 유형에 대한 자세한 내용은 [데이터 유형]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types)을 참조하세요.

{% alert note %}
Braze로 전송된 데이터는 변경할 수 없으며 수신 후 삭제하거나 수정할 수 없습니다. 그러나 대시보드에서 추적하는 항목을 제어하려면 앞의 섹션에 나열된 단계를 사용할 수 있습니다. 커스텀 데이터를 차단하거나 삭제하려면 [커스텀 데이터 차단]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data)을 참조하세요.
{% endalert %}