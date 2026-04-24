---
nav_title: 커스텀 데이터 차단 목록
article_title: 커스텀 데이터 차단 목록
page_order: 3
page_type: reference
description: "이 참조 문서에서는 Braze에서 커스텀 이벤트와 속성을 차단 목록에 추가하고 삭제하는 방법을 다룹니다."
---

# 커스텀 데이터 차단 목록

> 더 이상 유용하지 않은 커스텀 데이터의 추적을 중지하려면 차단 목록을 사용합니다. 차단 목록에 추가한 후 고객 프로필에서 커스텀 이벤트와 속성을 영구적으로 제거하려면 삭제를 사용합니다. 사전 채우기, 등록정보 관리, 데이터 유형 구성에 대해서는 [커스텀 데이터 관리]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/)를 참조하세요.

## 커스텀 데이터 차단 목록에 추가하기

때때로 너무 많은 데이터 포인트를 기록하거나, 마케팅 전략에 더 이상 유용하지 않거나, 실수로 기록된 커스텀 속성, 커스텀 이벤트 또는 구매 이벤트를 발견할 수 있습니다.

이 데이터가 Braze로 전송되는 것을 중지하려면, 엔지니어링 팀이 앱이나 웹사이트의 백엔드에서 해당 데이터를 제거하는 작업을 진행하는 동안 커스텀 데이터 오브젝트를 차단 목록에 추가할 수 있습니다. 차단 목록에 추가하면 특정 커스텀 데이터 오브젝트가 Braze에 더 이상 기록되지 않으므로, 특정 사용자를 검색할 때 표시되지 않습니다.

커스텀 데이터를 차단 목록에 추가하려면 워크스페이스에 대해 다음 드롭다운에 나열된 [사용자 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/)이 필요합니다.

{% details 커스텀 데이터 차단 목록에 필요한 사용자 권한 %}

{% multi_lang_include deprecations/user_permissions.md %}

- View Campaigns
- Edit Campaigns
- Archive Campaigns
- View Canvases
- Edit Canvases
- Archive Canvases
- View Frequency Capping Rules
- Edit Frequency Capping Rules
- View Message Prioritization
- Edit Message Prioritization
- View Content Blocks
- View Feature Flags
- Edit Feature Flags
- Archive Feature Flags
- View Segments
- Edit Segments
- View IAM Templates
- Edit IAM Templates
- Archive IAM Templates
- View Email Templates
- Edit Email Templates
- Archive Email Templates
- View Webhook Templates
- Edit Webhook Templates
- View Link Templates
- Edit Link Templates
- View Media Library Assets
- Edit Media Library Assets
- Delete Media Library Assets
- View Locations
- Edit Locations
- Archive Locations
- View Promotion Codes
- Edit Promotion Codes
- Export Promotion Codes
- View Preference Centers
- Edit Preference Centers
- View Reports
- Edit Reports

{% enddetails %}

차단 목록에 추가된 데이터는 SDK에서 전송되지 않으며, Braze 대시보드는 다른 소스(예: API)에서 오는 차단 목록 데이터를 처리하지 않습니다. 그러나 차단 목록에 추가해도 고객 프로필에서 데이터가 제거되거나 해당 커스텀 데이터 오브젝트에 대해 발생한 데이터 포인트 양이 소급하여 감소하지는 않습니다. 차단 목록에 추가된 데이터는 숨겨지지만 Liquid 템플릿에는 여전히 사용할 수 있습니다.

### 커스텀 속성, 커스텀 이벤트 및 제품 차단 목록에 추가하기

{% alert important %}
이벤트 또는 속성이 차단 목록에 추가되면, 해당 이벤트 또는 속성을 사용하는 모든 세그먼트, 캠페인 또는 캔버스가 아카이브됩니다.
{% endalert %}

특정 커스텀 속성, 이벤트 또는 제품의 추적을 중지하려면 다음 단계를 따르세요:

1. **커스텀 속성**, **커스텀 이벤트** 또는 **제품** 페이지에서 검색합니다.
2. 커스텀 속성, 이벤트 또는 제품을 선택합니다. 커스텀 속성과 이벤트의 경우 한 번에 최대 100개까지 선택하여 차단 목록에 추가할 수 있습니다.
3. **차단 목록**을 선택합니다.

![커스텀 속성 페이지에서 차단 목록에 추가된 여러 커스텀 속성이 선택된 모습.]({% image_buster /assets/img_archive/blocklist_custom_attr.png %})

최대 300개의 커스텀 속성과 300개의 커스텀 이벤트를 차단 목록에 추가할 수 있습니다. 특정 기기 속성의 수집을 방지하려면 [SDK 가이드]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection)를 참조하세요.

{% alert important %}
**휴지통** 상태의 커스텀 속성 또는 커스텀 이벤트는 삭제될 때까지 차단 목록 한도에 포함됩니다.
{% endalert %}

커스텀 이벤트 또는 속성이 차단 목록에 추가되면 다음이 적용됩니다:

- Braze로 전송된 데이터는 처리되지 않으며, 차단 목록에 추가된 이벤트와 속성은 더 이상 데이터 포인트로 집계되지 않습니다
- 기존 데이터는 다시 활성화하지 않는 한 사용할 수 없습니다
- 차단 목록에 추가된 이벤트와 속성은 필터나 그래프에 표시되지 않습니다
- 활성 캔버스의 초안에서 차단 목록에 추가된 데이터에 대한 참조는 잘못된 값으로 로드되어 오류가 발생할 수 있습니다
- 차단 목록에 추가된 이벤트 또는 속성을 사용하는 모든 항목이 아카이브됩니다

이를 위해 Braze는 차단 목록 정보를 각 기기로 전송합니다. 이는 수십만 또는 수백만 개의 이벤트와 속성을 차단 목록에 추가하는 경우 데이터 집약적인 작업이 될 수 있으므로 중요한 고려 사항입니다.

### 차단 목록 추가 시 고려 사항

많은 수의 이벤트와 속성을 차단 목록에 추가하는 것은 가능하지만 권장되지 않습니다. 이벤트가 수행되거나 속성이 Braze로 전송될 때마다 해당 이벤트 또는 속성을 전체 차단 목록과 대조하여 확인해야 하기 때문입니다.

최대 300개의 항목이 차단 목록을 위해 SDK로 전송됩니다. 300개 이상의 항목을 차단 목록에 추가하면 이 데이터는 SDK에서 전송됩니다. 향후 이벤트 또는 속성을 사용할 필요가 없다면 다음 릴리스 시 앱 코드에서 제거하는 것을 고려하세요. 차단 목록 변경 사항이 전파되는 데 몇 분이 걸릴 수 있습니다. 차단 목록에 추가된 이벤트 또는 속성은 언제든지 다시 활성화할 수 있습니다.

## 커스텀 데이터 삭제

타겟 캠페인과 세그먼트를 구축하면서 더 이상 커스텀 이벤트나 커스텀 속성이 필요하지 않다는 것을 알게 될 수 있습니다. 예를 들어, 일회성 캠페인의 일부로 특정 커스텀 속성을 사용한 경우, [차단 목록에 추가](#blocklisting-custom-attributes-custom-events-and-products)한 후 이 데이터를 삭제하고 앱에서 해당 참조를 제거할 수 있습니다. 문자열, 숫자, 중첩 고객 속성 등 모든 데이터 유형을 삭제할 수 있습니다.

{% alert important %}
커스텀 데이터를 삭제하려면 [Braze 관리자]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#admin)여야 합니다.
{% endalert %}

커스텀 이벤트 또는 커스텀 속성을 삭제하려면 다음을 수행하세요:

1. 삭제하려는 데이터 유형에 따라 **데이터 설정** > **커스텀 속성** 또는 **커스텀 이벤트**로 이동합니다.
2. 커스텀 데이터로 이동하여 <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;**동작** > **차단 목록**을 선택합니다.
3. 커스텀 데이터가 7일 동안 차단 목록에 추가된 후 <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;**동작** > **삭제**를 선택합니다.

### 삭제 작동 방식

커스텀 데이터를 삭제하면 다음이 발생합니다:

- **커스텀 속성의 경우:** 모든 사용자의 프로필에서 속성 데이터가 영구적으로 제거됩니다.
- **커스텀 이벤트의 경우:** 모든 사용자의 프로필에서 이벤트 메타데이터가 영구적으로 제거됩니다.

속성 또는 이벤트가 삭제 대상으로 선택되면 상태가 **휴지통**으로 변경됩니다. 이후 7일 동안 속성 또는 이벤트를 복원할 수 있습니다. 7일 후에도 복원하지 않으면 데이터가 영구적으로 삭제됩니다. 속성 또는 이벤트를 복원하면 차단 목록 상태로 되돌아갑니다.

삭제해도 고객 프로필에 커스텀 데이터 오브젝트가 추가로 기록되는 것을 방지하지 않으므로, 이벤트 또는 속성을 삭제하기 전에 커스텀 데이터가 더 이상 기록되지 않는지 확인하세요.

### 알아두어야 할 사항

커스텀 데이터를 삭제할 때 다음 사항을 유의하세요:

* **삭제는 영구적입니다.** 데이터를 복구할 수 없습니다.
* 데이터는 Braze 플랫폼과 고객 프로필에서 제거됩니다.
* 삭제 후 커스텀 속성 이름이나 커스텀 이벤트 이름을 "재사용"할 수 있습니다. 즉, 삭제 후 Braze에서 커스텀 데이터가 "다시 나타나는" 경우, 이는 중지되지 않은 통합이 동일한 커스텀 데이터 이름으로 데이터를 전송하고 있기 때문일 수 있습니다.
* 삭제로 인해 커스텀 데이터가 다시 나타나는 경우 항목을 다시 차단 목록에 추가해야 할 수 있습니다. 커스텀 데이터가 삭제되었으므로 차단 목록 상태는 유지되지 않습니다.
* 커스텀 데이터를 삭제해도 [데이터 포인트]({{site.baseurl}}/user_guide/data/infrastructure/data_points)가 기록되지 않으며 새로운 데이터 포인트가 생성되지도 않습니다.