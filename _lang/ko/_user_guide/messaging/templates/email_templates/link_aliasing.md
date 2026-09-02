---
nav_title: 링크 별칭 지정
article_title: 링크 별칭 지정
alias: /link_aliasing/
page_order: 3
description: "이 문서에서는 링크 별칭 지정의 작동 방식을 설명하고 링크가 어떻게 표시되는지에 대한 예시를 제공합니다."
channel:
  - email

---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/link-aliasing){: style="float:right;width:120px;border:0;" class="noimgborder"}링크 별칭 지정 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomlink-aliasing-stylefloatrightwidth120pxborder0-classnoimgborderlink-aliasing}

> 링크 별칭 지정을 사용하여 Braze에서 발송하는 이메일 메시지의 링크를 식별할 수 있는 사용자 정의 이름을 생성합니다. 이러한 링크는 세분화 리타겟팅, 행동 기반 트리거링 및 링크 분석에 활용할 수 있습니다.

## 링크 별칭 지정 정보 {#about-link-aliasing}

링크 별칭 지정을 사용하면 이메일에서 전송된 링크를 식별하고 추적하기 위해 사용자가 직접 이름을 생성할 수 있습니다. 이를 통해 전체 링크를 참조할 필요 없이 이메일에서 인식 가능한 링크 별칭을 효율적으로 사용하여 인게이지먼트를 추적하고 캠페인 성능을 분석할 수 있습니다.

링크 별칭 지정을 사용하면 다음을 수행할 수 있습니다:

- **특정 링크를 클릭한 사용자를 리타겟:** 링크를 클릭한 사용자를 식별하고 타겟팅합니다.
- **액션 기반 트리거 생성:** 사용자가 링크를 클릭할 때 이메일을 전송합니다.
- **측정기준 분석:** 링크 A와 링크 B를 클릭한 사용자 수를 비교합니다.

### 작동 방식 {#how-it-works}

Braze는 모든 링크 URL에 `lid`(링크 식별자라고도 함)라는 추가 파라미터를 붙여 이메일 내 링크를 고유하게 식별합니다. 이 `lid` 값을 통해 Braze는 나머지 URL 파라미터가 다를 수 있더라도 해당 링크와의 사용자 상호작용을 추적, 모니터링 및 집계할 수 있습니다. 이를 통해 이메일 캠페인 콘텐츠에 사용자가 어떻게 참여하는지에 대한 인사이트를 제공합니다.

이메일 메시지가 포함된 Campaign, Canvas 또는 Content Blocks가 복제되면 링크 식별자도 함께 업데이트됩니다.

## 링크 별칭 만들기 {#creating-a-link-alias}

{% alert important %}
**Link Management**는 Braze가 계정에 대해 링크 관리를 활성화하면 Campaign 또는 Canvas 이메일 작성기에 나타납니다. **링크 별칭**을 생성하고 편집하려면 링크 별칭 지정이 켜져 있어야 합니다. **Link Management**가 표시되지 않으면 계정 매니저에게 연락하여 링크 별칭 지정을 켜주세요.
{% endalert %}

링크 별칭을 만들려면 Campaign 또는 Canvas 구성 요소에서 이메일 본문을 열고, **Content** 영역에서 **Link Management**를 엽니다. 드래그 앤 드롭 및 HTML 작성기는 동일한 사이드바 레이아웃을 사용합니다:

### 드래그 앤 드롭 편집기 {#drag-and-drop-editor}

1. **Edit Email Body**를 선택하여 드래그 앤 드롭 작성기를 엽니다.
2. 작성기 사이드바에서 **Content**를 선택합니다(**Sending Settings** 및 **Preview & Test** 옆에 있음). 이 레이아웃에 대한 자세한 내용은 [드래그 앤 드롭으로 이메일 만들기]({{site.baseurl}}/user_guide/channels/email/drag_and_drop)를 참조하세요.
3. **Content** 하위 메뉴에서 **Link Management**를 선택합니다(**Design and Build** 아래에 표시됨). 하위 메뉴가 접혀 있으면 사이드바의 화살표 컨트롤을 사용하여 펼칩니다.

### HTML 편집기 {#html-editor}

1. 작성기에서 이메일 본문으로 이동합니다.
2. 작성기 사이드바에서 **Content**를 선택합니다.
3. **Content** 하위 메뉴에서 **Design and Build** 아래의 **Link Management**를 선택합니다.

**Link Management**에서:

1. Braze가 각 링크에 대해 고유한 기본 링크 별칭을 자동으로 생성합니다.
2. 별칭에 이름을 지정합니다. 별칭은 이메일 캠페인 배리언트 또는 Canvas 구성 요소별로 고유한 이름을 지정해야 합니다.

리포팅이나 세분화를 처리할 때 특정 링크를 참조하는 데 사용할 별칭도 설정할 수 있습니다.

![네 개의 링크 별칭이 있는 Link Management 페이지.]({% image_buster /assets/img/link_aliasing_composer.png %})

{% alert note %}
링크 별칭 지정은 쿼리 파라미터를 안전하게 추가할 수 있는 HTML 앵커 태그 내의 `href` 속성에서만 지원됩니다. Braze가 `lid` 값을 쉽게 추가할 수 있도록 링크 끝에 물음표(?)를 포함하는 것이 모범 사례입니다. `lid` 값이 추가되지 않으면 Braze가 링크 별칭 지정을 위해 URL을 인식하지 못합니다.
{% endalert %}

{% alert important %}
드래그 앤 드롭 편집기에서는 링크 별칭이 **Link Management** 탭에 나타나려면 URL의 해시 기호(`#`) 앞에 물음표(`?`)가 포함되어야 합니다.
{% endalert %}

## 링크 별칭 관리하기 {#managing-link-aliases}

추적된 모든 링크 별칭을 확인하려면 다음을 수행합니다:

1. **설정** > **작업 공간 설정** 아래의 **이메일 환경설정**으로 이동합니다.
2. **링크 별칭 지정 설정** 탭을 선택합니다.

여기에서 링크 별칭을 정렬, 검색하고 추적을 해제할 수 있습니다.

![다양한 캠페인과 연결된 활성 및 비활성 링크 별칭을 보여주는 추적된 링크 별칭 페이지.]({% image_buster /assets/img/tracked_aliases.png %})

{% alert tip %}
[Campaign 링크 별칭 목록]({{site.baseurl}}/get_campaign_link_alias) 및 [Canvas 링크 별칭 목록]({{site.baseurl}}/get_canvas_link_alias) 엔드포인트를 사용하여 Campaign의 각 메시지 배리언트 또는 이메일 전용 Canvas 구성 요소에 설정된 `alias`를 추출할 수 있습니다.
{% endalert %}

Braze에서는 이메일 내의 링크를 평가하고, 링크 템플릿을 추가하며, 세분화 및 보고 목적에 적합한 명명 규칙을 마련할 것을 권장합니다. 이를 통해 모든 링크를 효과적으로 관리할 수 있습니다.

링크 별칭 지정이 켜져 있을 때 메시지, Content Blocks 및 링크 템플릿은 수정되지 않습니다. 링크 템플릿이나 Content Blocks를 사용하는 기존 메시지는 그대로 유지됩니다. 그러나 메시지를 업데이트하면 모든 링크에 링크 별칭 마크업이 적용되므로, 링크가 표시되려면 링크 템플릿을 다시 적용해야 합니다.

## 링크 별칭 지정으로 링크가 업데이트되는 방식 {#how-links-are-updated-with-link-aliasing}

다음 표에서는 이메일 본문의 링크, 링크 별칭 지정 결과, 그리고 원래 링크가 링크 별칭 지정을 통해 어떻게 업데이트되는지에 대한 설명과 예시를 제공합니다.

### 고정 링크 {#permalink}

**로직:** Braze는 물음표(?)를 삽입하고 첫 번째 쿼리 매개변수를 URL에 추가합니다.

| 이메일 본문의 링크 | 별칭이 적용된 링크 |
|-----------------------|----------------------------------------|
| `https://www.braze.com` | `https://www.braze.com?lid=slfdldtqdhdk` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="고정 링크" }

### 추가 쿼리 매개변수가 있는 링크 {#link-with-more-query-parameters}

**로직:** Braze는 다른 쿼리 매개변수를 감지하고 URL 끝에 `lid=`를 추가합니다.

| 이메일 본문의 링크 | 별칭이 적용된 링크 |
|---------------------------------------------------------------|--------------------------------------------------------------------------------|
| `https://www.braze.com?utm_campaign=retention&utm_source=email` | `https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="추가 쿼리 매개변수가 있는 링크" }

### HTML 링크 {#html-link}

**로직:** Braze는 링크가 URL이며 이미 물음표(?)가 있음을 인식하여, `lid` 쿼리 매개변수를 물음표 뒤에 추가합니다.

| 이메일 본문의 링크 | 별칭이 적용된 링크 |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| {%raw%}`<a href="{{custom_attribute.{product_url}}}?">`{%endraw%} | {%raw%}`<a href="{{custom_attribute.{product_url}}}?lid=ac7a548g5kl7">`{%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="HTML 링크" }

### 앵커가 있는 링크 {#link-with-anchor}

**로직:** Braze는 URL이 물음표(?) 뒤에 앵커(#)가 오는 표준 구조를 사용할 것으로 예상합니다. Braze는 왼쪽에서 오른쪽으로 읽기 때문에, 물음표와 `lid` 값이 앵커 앞에 추가됩니다.

| 이메일 본문의 링크 | 별칭이 적용된 링크 |
|--------------------------------------------------|-------------------------------------------------------------------|
| `https://www.braze.com#bookmark1?utm_source=email` | `https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="앵커가 있는 링크" }

### 앵커와 캡처 태그가 있는 링크 {#link-with-anchor-and-capture-tag}

**로직:** 앵커(#)가 포함된 URL에서 링크 별칭 지정을 사용하는 경우, Braze는 앵커가 쿼리 매개변수 뒤에 위치할 것으로 예상합니다. 즉, 올바른 추적을 위해 `lid` 값이 앵커 **앞에** 추가되어야 하며, Braze가 URL을 왼쪽에서 오른쪽으로 읽기 때문에 물음표(?)와 `lid`가 앵커 앞에 와야 합니다.

| 이메일 본문의 링크 | 별칭이 적용된 링크 |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| {%raw%}`<a href="https://www.braze.com/promotions#special-offer">Check out our special offer!</a>`{%endraw%} | {%raw%}`<a href="https://www.braze.com/promotions?lid={{link_alias}}#special-offer">Check out our special offer!</a>` {%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="앵커와 캡처 태그가 있는 링크" }

## 링크 별칭 추적하기 {#tracking-link-aliases}

작성기 사이드바에서 **콘텐츠** > **링크 관리**(**디자인 및 빌드** 아래)를 선택한 다음, **추적**하려는 별칭을 선택합니다. 추적된 별칭은 링크 별칭을 참조하는 세분화 필터에서 사용할 수 있습니다([세분화 필터](#segmentation-filters) 참조). 또한 사용자가 이메일에서 링크 별칭을 클릭할 때 액션 기반 메시지를 보내거나 Canvas를 통해 사용자를 이동시킬 수 있습니다([액션 기반 필터](#action-based-filters) 참조). **추적** 설정은 해당 링크의 클릭이 이메일 성능 리포팅에서 집계되는지 여부에 영향을 주지 않습니다.

{% alert tip %}
링크 인게이지먼트 측정기준을 추적하려면 링크 앞에 HTTP 또는 HTTPS가 있어야 합니다. 특정 링크에 대한 클릭 추적을 끄려면 [유니버설 링크 및 앱 링크]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links#turning-off-click-tracking-on-a-link-to-link-basis)를 참조하세요.
{% endalert %}

Braze에서는 무제한으로 링크를 추적할 수 있지만, 사용자가 가장 최근에 열람한 링크에 대해서만 리타겟할 수 있습니다. 고객 프로필에는 가장 최근에 클릭한 링크 100개가 포함됩니다. 예를 들어, 500개의 링크를 추적하고 사용자가 500개 모두를 클릭한 경우, 가장 최근에 클릭한 100개의 링크를 기반으로 리타겟하거나 Segment를 만들 수 있습니다.

![두 개의 링크가 선택된 링크 관리 탭.]({% image_buster /assets/img/link_management_dnd.png %})

{% alert note %}
Braze는 프로필 수준에서 최근 클릭한 링크 별칭을 최대 100개까지만 추적합니다.
{% endalert %}

### 액션 기반 필터 {#action-based-filters}

워크스페이스에서 링크 별칭 지정이 활성화되어 있으면, 모든 링크(추적 또는 비추적)를 타겟팅하는 액션 기반 메시지를 만들거나 이메일 Campaign 또는 Canvas 구성 요소에서 별칭을 클릭했는지 여부를 기반으로 사용자를 리타겟할 수 있습니다.

![Canvas 구성 요소에서 별칭을 클릭했거나 Campaign과 인터랙션한 사용자를 타겟팅하는 액션 기반 옵션.]({% image_buster /assets/img/link_aliasing_action_based_filters.png %})

- Campaign이 보관되면 링크 추적이 해제되며 해당 링크 별칭은 다른 필터에서 사용할 수 없습니다.
- 링크에 추적이 켜져 있고 Campaign에서 클릭된 경우, 해당 메시지에서 최소 하나의 링크가 여전히 추적되고 있는 한, 링크 추적이 이후에 해제되더라도 세분화 필터에서 해당 Campaign을 사용 가능한 옵션으로 찾을 수 있습니다.
- 추적된 링크를 필터로 선택하려면 **캔버스 단계에서 별칭 클릭** 필터 드롭다운을 사용하여 활성(시작된) Canvas에 있어야 합니다. 링크가 Canvas 초안에서 추적되고 있는 경우, 추적된 링크를 필터로 선택할 수 없습니다.

링크를 비추적으로 설정하려면 **설정** > **이메일 환경 설정** > **링크 별칭 지정 설정**으로 이동합니다.

### 세분화 필터 {#segmentation-filters}

Braze에서 이메일에 링크 별칭이 있고 사용자가 이를 클릭하면, 해당 이벤트가 별칭과 함께 사용자 프로필에 기록됩니다.

"모든 Campaign 또는 캔버스 단계에서 별칭 클릭" 세분화 필터를 사용한 후 나중에 이 링크 별칭의 이름을 변경하면, 고객 프로필의 이전 클릭 데이터는 **업데이트되지 않으며**, 여전히 이전 링크 별칭으로 표시됩니다. 따라서 새 링크 별칭을 기반으로 사용자를 타겟팅하면 이전 링크 별칭의 데이터는 포함되지 않습니다.

"Campaign에서 별칭 클릭" 또는 "Canvas에서 별칭 클릭" 세분화 필터를 사용하면 사용자가 특정 Campaign 또는 Canvas에서 특정 별칭을 클릭했는지 여부로 필터링됩니다. 여러 사용자가 동일한 이메일 주소를 공유하고 링크 별칭이 클릭되면, 해당 이메일 주소를 공유하는 다른 모든 사용자의 프로필이 업데이트됩니다. 이 프로필은 클릭 이벤트뿐만 아니라 전송 및 열람 이벤트에 의해서도 업데이트됩니다.

다음 세분화 필터는 이벤트가 처리되는 시점에 추적된 클릭 이벤트에 적용됩니다. 즉, 비추적 링크는 기존 데이터를 제거하지 않으며, 링크를 추적해도 데이터가 소급 적용되지 않습니다. 자세한 내용은 [세분화 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)를 참조하세요.

#### 링크 추적 해제 {#untracking-links}

링크 추적을 해제해도 해당 필터가 포함된 기존 Segment가 비추적 별칭으로 재배정되지 않습니다. 기존 데이터는 새로운 데이터로 교체될 때까지 고객 프로필에 남아 있습니다.

보관된 메시지의 링크는 자동으로 추적 해제됩니다. 그러나 보관된 메시지가 보관 해제되면, 링크를 다시 추적해야 합니다. 링크 별칭이 추적되면 링크 리포팅은 최상위 도메인이나 전체 URL 대신 별칭으로 인덱싱됩니다.

이메일 Campaign에서 모든 링크와 각각의 총 클릭 수를 확인하려면 **메시지 분석** > **이메일 성능** > **미리보기 및 히트맵**으로 이동한 다음 **히트맵 표시** 토글을 선택합니다.

![링크 별칭과 총 클릭 수가 표시된 총 클릭 기준 링크 테이블 패널.]({% image_buster /assets/img/link_alias_total_clicks.png %}){: style="max-width:60%;"}

### 이메일 클릭 이벤트 {#email-clicks-event}

Currents로 인게이지먼트 데이터를 내보내는 경우, 링크 별칭 지정이 활성화되어 있으면 이메일 클릭 이벤트가 약간 달라집니다. 링크 별칭 지정이 켜져 있을 때 [이메일 클릭 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-click-events)에 `link_id`와 `link_alias`라는 두 개의 추가 필드가 포함됩니다.

```json
// Email Click: users.messages.email.Click
{
  "id": (string) unique ID of this event,
  "user_id": (string) Braze user ID of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) ID of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) ID of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) ID of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "url": (string) the URL that was clicked (Email Click events only),
  "user_agent": (string) description of the user's system and browser for the event (Email Click and Open events only),
  "ip_pool": (string) IP pool used for message sending,
  "link_id": (string) unique value generated by Braze for the URL,
  "link_alias": (string) alias name set when the message was sent
}
```

{% alert update %}
`dispatch_id`의 동작은 Canvas와 Campaigns 간에 다릅니다. Braze는 캔버스 단계(스케줄 가능한 항목 단계를 제외)를 "스케줄"되어 있더라도 트리거된 이벤트로 처리하기 때문입니다. Canvas와 Campaigns에서의 [`dispatch_id` 동작]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id)에 대해 자세히 알아보세요.

_2019년 8월에 업데이트되었습니다._
{% endalert %}

## Content Blocks에서의 링크 별칭 지정 {#link-aliasing-in-content-blocks}

새로운 Content Blocks는 해당하는 각 링크에 Braze가 `lid={{placeholder}}`를 추가하여 링크가 수정됩니다. 이 입력 안내 값은 이메일 메시지 배리언트에 삽입될 때 확인됩니다.

Braze에서 링크 별칭 지정을 활성화하기 전에 생성된 기존 Content Blocks 내의 링크를 수정하려면 기존 Content Blocks를 복제한 다음, 복제된 Content Blocks 내의 링크를 수정합니다.

`lid` 값이 없는 Content Blocks가 새 메시지에 삽입되면 해당 Content Blocks의 링크는 별칭으로 추적되지 않습니다. 새 Content Blocks가 "이전" 메시지 배리언트에 삽입되면 해당 메시지 배리언트의 링크는 링크 별칭 지정에 의해 인식됩니다. Content Blocks의 링크도 인식됩니다. 그러나 "이전" Content Blocks는 "새" Content Blocks를 중첩할 수 없습니다.

{% alert tip %}
Content Blocks의 경우, Braze는 새 메시지에서 사용할 기존 Content Blocks의 사본을 만드는 것을 권장합니다. 이는 일괄 복제를 통해 수행할 수 있으며, 새 메시지에서 링크 별칭 지정이 활성화되지 않은 Content Blocks를 참조하는 시나리오를 방지하는 데 도움이 됩니다.
{% endalert %}

## Liquid로 생성된 URL의 링크 별칭 지정 {#link-aliasing-for-urls-generated-by-liquid}

Liquid로 생성된 URL(예: HTML의 `assign`, Content Blocks에서 가져온 값, 커스텀 속성의 Liquid)의 경우, Braze는 `lid` 쿼리 파라미터를 삽입할 명확한 위치가 필요합니다. 대부분의 경우 URL에 Liquid가 남아 있으면 구분자를 직접 추가하지 않는 한 Braze는 `?`로 새 쿼리 문자열을 시작할지 `&`로 기존 쿼리에 연결할지 추론하지 않습니다.

다음을 수행하세요:

- URL에 이미 쿼리 문자열이 **포함되어 있지 않은** 경우, Liquid 뒤에 `?`를 추가합니다(예: `{{my_url}}?`).
- URL에 **이미** `?`와 쿼리 파라미터가 포함된 경우, Liquid 뒤에 `&`를 추가합니다(예: `{{my_url}}&`).

{% alert note %}
Liquid로 생성된 URL에 [링크 템플릿]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template)을 사용하면, Liquid 실행 후 렌더링된 URL에 쿼리 구분자로 사용된 `?` 문자가 정확히 두 개 포함된 경우, Braze가 보수적으로 URL을 정규화할 수 있습니다. 두 번째 `?`는 Braze가 URL을 가능한 한 적게 변경하도록 `&`로 재작성될 수 있습니다. <br><br>Braze는 모든 중복 `?` 패턴을 수정하려고 시도하지 않으며, 더 복잡한 URL의 처리는 의도적으로 제한됩니다. 먼저 마크업에 올바른 `?` 또는 `&`를 추가하고, 정규화는 제한된 보호 장치로 취급하세요—올바른 형식의 URL이나 구분자가 없을 때 **Link Management**에서 링크가 인식되도록 하는 것의 대체가 아닙니다.
{% endalert %}

후행 `?` 또는 `&`(또는 다른 지원되는 삽입 지점)가 없으면, 링크 별칭 지정이 URL을 인식하지 못하고 **Link Management**에 표시되지 않으며 링크 템플릿도 적용되지 않습니다.

### URL 프래그먼트(`#`)와 추적 파라미터 {#url-fragments-and-tracking-parameters}

프래그먼트(`#`와 그 뒤의 모든 것)는 일반적인 링크 요청에서 서버로 전송되지 않습니다. Braze는 `lid`를 쿼리 문자열에 삽입하며, 이는 `#` 앞에 나타나야 합니다. `href`에 Liquid와 `#` 프래그먼트가 있지만 `#` 앞에 `?` 또는 `&`가 없는 경우, Braze는 안전하게 `lid`를 추가할 수 없으므로 해당 링크가 **Link Management**에 표시되지 않거나 링크 별칭으로 추적되지 않을 수 있습니다.

이 문제는 드래그 앤 드롭 편집기에서 버튼 URL이 Liquid를 해시 기반 패턴과 혼합할 때(예: 정적 경로 뒤에 `#`, 그 다음 추가 키-값 페어) 특히 흔합니다. 이 경우 `#` 바로 앞에 `?`를 추가하여 쿼리 문자열(`lid` 포함)이 프래그먼트 앞에 파싱되도록 하세요.

{% raw %}
```text
https://example.com/campaign/to/abc123?#user_id={{${user_id}}}&source=email
```
{% endraw %}

위 예제에서 `#` 앞의 `?`는 Braze에 `lid`를 추가할 쿼리 세그먼트를 제공합니다. 이것이 없으면 링크가 **Link Management**에 표시되지 않을 수 있습니다.

쿼리 파라미터를 추가할 위치를 식별할 수 없으면, 링크 별칭 지정이 이러한 URL을 인식하지 못하고 링크 템플릿도 적용되지 않습니다. 동적 URL에 대해 **Failed to be assigned an LID**와 같은 오류가 표시되면, `href`가 이 섹션의 예제에 표시된 `?` 또는 `&` 패턴을 사용하는지 확인하세요.

### 드래그 앤 드롭 편집기 고려사항 {#drag-and-drop-editor-considerations}

드래그 앤 드롭 편집기에서 링크를 보유하는 필드(예: 버튼 **URL**)는 Liquid가 실행되기 전에 기본 `href`의 유효성을 검사합니다. 공백, 줄 바꿈 및 URL에 안전하지 않은 기타 문자는 Braze가 링크 템플릿이나 링크 별칭 지정 파라미터를 추가할 때 예기치 않은 동작을 유발할 수 있습니다. 목적지에 대해 분기 Liquid가 필요한 경우, HTML 블록에서 `assign`으로 URL을 설정하고(다음 섹션 참조) 해당 필드에 복잡한 Liquid를 직접 넣는 대신 드래그 앤 드롭 URL 필드에서 단일 변수를 참조하세요.

### Content Blocks 예제 {#content-block-example}

{% raw %}
Content Blocks에 후행 `?` 또는 `&`가 없는 `https://www.braze.com/{{custom_attribute.${offer_id}}}` 같은 링크가 포함되어 있으면, Braze는 `lid`를 어디에 추가해야 할지 알 수 없으므로 해당 링크가 **Link Management**에 포착되지 않습니다. Content Blocks의 URL 끝에 `?` 또는 `&`를 추가하고(쿼리 문자열이 이미 존재하는지에 따라), Content Blocks를 저장하면 링크가 인식될 수 있습니다.
{% endraw %}

### URL이 사용자마다 다를 때의 리포팅 {#reporting-when-the-url-varies-per-user}

메시지의 각 고유 `href`는 **Link Management** 및 별칭 기반 리포팅에서 **하나의** 링크 ID와 하나의 링크 별칭에 매핑됩니다. 링크 별칭이 추적되면, 대시보드 내 이메일 리포팅은 가능한 모든 확인된 URL이 아닌 별칭에 의해 색인됩니다.

먼저 Braze에서 다음 접근 방식을 사용하세요:

- **Campaign 및 Canvas 이메일 분석:** [링크 추적 해제](#untracking-links)에 설명된 대로 **Show Heatmap**을 켠 상태에서 **Message Analytics** > **Email Performance** > **Preview & Heatmap**에서 링크별 집계 클릭을 검토합니다.
- **쿼리 빌더의 수신자별 클릭:** Campaign 또는 Canvas에 대해 **Email URLs clicked** [쿼리 빌더 템플릿]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates#email-templates)을 실행합니다. 이 템플릿은 요약 카운트를 위해 비개인화된 링크를 표시합니다. CSV 내보내기에는 클릭한 사용자의 사용자 ID, 클릭한 링크 및 타임스탬프가 포함됩니다. (비개인화된 URL은 요약 보기를 위해 Liquid 태그를 제거합니다. 자세한 내용은 템플릿 설명을 참조하세요.)
- **작성기의 별칭 수준 분석:** 각 목적지(예: 각 `offer_id`)를 **Link Management** 및 별칭 기반 리포팅에서 자체 행으로 표시해야 하는 경우, 사용자마다 경로가 변경되는 하나의 링크 대신 별도의 `href` 값(따라서 별도의 별칭)을 사용하세요—예를 들어, 분기별 개별 링크.

스트리밍 인게이지먼트 내보내기도 사용하는 경우, 이메일 클릭 이벤트에는 **`url`** 필드가 포함됩니다. 해당 페이로드가 링크 별칭 지정과 어떻게 관련되는지는 이 페이지의 [이메일 클릭 이벤트](#email-clicks-event)를 참조하세요.

### 예제 {#example}

할당된 URL에 쿼리 파라미터가 없을 때 이 패턴을 사용하세요:

{% raw %}
```liquid
{% assign link1 = "https://www.braze1.com" %}

<a href="{{link1}}?">Visit Braze</a>
```
{% endraw %}

할당된 URL에 이미 `?`와 쿼리 파라미터가 포함된 경우, `?` 대신 Liquid 뒤에 `&`를 추가하세요:

{% raw %}
```liquid
{% assign link_with_params = "https://www.braze1.com?campaign=test" %}

<a href="{{link_with_params}}&">Visit Braze</a>
```
{% endraw %}

### 조건부 Liquid가 포함된 URL {#urls-with-conditional-liquid}

`href` 내부에서 조건부 Liquid 태그가 사용되는 경우(예: {% raw %}`{% if %}`, `{% elsif %}`, 또는 `{% unless %}`{% endraw %}로 URL을 설정하는 경우), 링크 별칭 지정이 해당 링크에 적용되지 않습니다. 이는 이러한 링크가 **Link Management**에 표시되지 않고 클릭 추적을 위한 `lid`를 받지 않는다는 것을 의미합니다.

**권장사항:** HTML 블록에서 `assign`(또는 {% raw %}`{% capture %}`{% endraw %})으로 최종 URL을 빌드한 다음, 링크가 필요한 곳에서 해당 변수를 참조하세요. 드래그 앤 드롭 편집기에서는 적절하게 후행 `?` 또는 `&`를 포함하여 버튼 **URL** 필드에 변수를 붙여넣으세요—예: `{{url}}?`.

{% raw %}
```liquid
{% if {{custom_attribute.${account_tier}}} == "pro" %}
{% assign url = "https://example.com/pro/verify" %}
{% else %}
{% assign url = "https://example.com/retail/account" %}
{% endif %}
```
{% endraw %}

버튼 **URL** 필드(드래그 앤 드롭) 또는 HTML에서, `href`를 구분자와 함께 변수로 지정하세요:

{% raw %}
```liquid
<a href="{{ url }}?">Go to account</a>
```
{% endraw %}

또는 URL을 하나의 변수로 캡처할 수 있습니다:

{% raw %}
```liquid
{% capture url %}
  {%- if condition -%}
    https://example.com/url1
  {%- else -%}
    https://example.com/url2
  {%- endif -%}
{% endcapture %}

<a href="{{ url }}?">Go to account</a>
```
{% endraw %}

## 문제 해결 {#troubleshooting}

### `lid` 매개변수를 허용하지 않는 대상 {#destinations-that-dont-accept-the-lid-parameter}

이메일 편집기에서 테스트 메시지를 보내면 Braze가 링크에 {% raw %}`lid={{placeholder}}`{% endraw %}를 추가합니다(입력 안내 값은 발송 시 고유한 값으로 대체됩니다). 대상 사이트나 API가 추가 쿼리 매개변수를 허용하지 않는 경우, 편집기에서는 링크가 작동하지만 이메일에서 열 때는 실패할 수 있습니다.

`lid` 값이 없으면 Braze는 해당 URL을 추적 및 세분화를 위한 링크 별칭 지정 대상으로 처리하지 않습니다. 백엔드나 사이트를 업데이트하여 `lid` 쿼리 매개변수가 있을 때 이를 무시하도록 설정하는 것을 권장합니다. 이렇게 하면 이 문서에서 설명하는 링크 별칭 지정, 리포팅, Segment 사용 사례가 유지됩니다.

또는 백엔드 변경을 계획하는 동안 대시보드에서 링크 별칭 지정을 끌 수 있습니다. **설정** > **이메일 환경설정** > **링크 별칭 지정 설정**으로 이동하세요.

대상 시스템을 변경할 수 없는 경우, [Braze 지원팀]({{site.baseurl}}/user_guide/administer/personal/braze_support)에 연락하여 워크스페이스의 링크 별칭 지정을 비활성화하도록 요청하세요. 워크스페이스에서 링크 별칭 지정이 꺼진 경우 다음 사항을 고려하세요:

- 새 이메일 메시지와 Content Blocks는 일반적으로 새 링크 별칭 마크업(`lid` 쿼리 매개변수 등)을 받지 않습니다.
- 링크 별칭 지정이 켜져 있을 때 생성된 기존 메시지는 HTML에 링크 별칭 마크업이 여전히 포함되어 있을 수 있습니다. 더 이상 필요하지 않은 곳에서 남아 있는 `lid` 매개변수를 수동으로 제거해야 할 수 있습니다.
- 기존 Campaign, Canvas 이메일 단계 또는 Content Block을 편집하는 경우, 템플릿화된 링크가 올바르게 표시되도록 링크 템플릿을 다시 추가해야 할 수 있습니다.
- 링크 별칭 지정이 켜져 있을 때 발송된 클릭 리포팅은 기능이 꺼진 후의 리포팅과 정확하게 일치하지 않을 수 있습니다.
- 링크 별칭 기반 필터(예: **Clicked Alias** 필터)를 사용하는 Segments는 예상하는 오디언스를 더 이상 반환하지 않을 수 있습니다.