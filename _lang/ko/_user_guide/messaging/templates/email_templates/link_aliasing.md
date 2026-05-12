---
nav_title: 링크 별칭 지정
article_title: 링크 별칭 지정
alias: /link_aliasing/
page_order: 3
description: "이 문서에서는 링크 별칭 지정의 작동 방식을 설명하고 링크가 어떻게 표시되는지에 대한 예시를 제공합니다."
channel:
  - email

---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/link-aliasing){: style="float:right;width:120px;border:0;" class="noimgborder"}링크 별칭 지정 {#braze-learning-course-imagebuster-assetsimgblicon3png-httpslearningbrazecomlink-aliasing-stylefloatrightwidth120pxborder0-classnoimgborderlink-aliasing}

> 링크 별칭 지정을 사용하여 Braze에서 발송하는 이메일 메시지의 링크를 식별할 수 있는 사용자 정의 이름을 생성합니다. 이러한 링크는 세분화 리타겟팅, 행동 기반 트리거링 및 링크 분석에 활용할 수 있습니다.

## 링크 별칭 지정 소개 {#about-link-aliasing}

링크 별칭 지정을 사용하면 이메일에서 발송되는 링크를 식별하고 추적하기 위한 사용자 정의 이름을 생성할 수 있습니다. 이를 통해 전체 링크를 참조하지 않고도 이메일에서 인식 가능한 링크 별칭을 효율적으로 사용하여 참여를 추적하고 캠페인 성과를 분석할 수 있습니다.

링크 별칭 지정을 사용하면 다음을 수행할 수 있습니다:

- **특정 링크를 클릭한 사용자를 리타겟팅:** 링크를 클릭한 사용자를 식별하고 타겟팅합니다.
- **행동 기반 트리거 생성:** 사용자가 링크를 클릭하면 이메일을 발송합니다.
- **측정기준 분석:** 링크 A와 링크 B를 클릭한 사용자 수를 비교합니다.

### 작동 방식 {#how-it-works}

Braze는 모든 링크 URL에 `lid`(링크 식별자라고도 함)라는 추가 매개변수를 추가하여 이메일 내 링크를 고유하게 식별합니다. 이 `lid` 값을 통해 Braze는 나머지 URL 매개변수가 다르더라도 링크에 대한 사용자 상호작용을 추적, 모니터링 및 집계할 수 있습니다. 이를 통해 사용자가 이메일 캠페인의 콘텐츠에 어떻게 참여하는지에 대한 인사이트를 제공합니다.

이메일 캠페인, 이메일 메시지가 포함된 Canvas 또는 Content Blocks이 복제되면 링크 식별자도 업데이트됩니다.

## 링크 별칭 생성 {#creating-a-link-alias}

링크 별칭을 생성하려면 다음 단계를 따르세요:

1. 캠페인 또는 Canvas 구성요소에서 이메일 본문으로 이동합니다.
2. **Link Management** 탭을 선택합니다.
3. Braze가 각 링크에 대해 고유한 기본 링크 별칭을 자동으로 생성합니다.
4. 별칭에 이름을 지정합니다. 별칭은 이메일 캠페인 배리언트 또는 Canvas 구성요소별로 고유하게 이름을 지정해야 합니다.

보고 또는 세분화를 처리할 때 특정 링크를 참조하는 데 사용할 별칭을 설정할 수도 있습니다.

![네 개의 링크 별칭이 있는 Link Management 페이지.]({% image_buster /assets/img/link_aliasing_composer.png %})

{% alert note %}
링크 별칭 지정은 쿼리 매개변수를 안전하게 추가할 수 있는 HTML 앵커 태그 내의 `href` 속성에서만 지원됩니다. Braze가 `lid` 값을 쉽게 추가할 수 있도록 링크 끝에 물음표(?)를 포함하는 것이 모범 사례입니다. `lid` 값을 추가하지 않으면 Braze가 링크 별칭 지정을 위해 URL을 인식하지 못합니다.
{% endalert %}

## 링크 별칭 관리 {#managing-link-aliases}

추적된 모든 링크 별칭을 보려면 다음을 수행하세요:

1. **설정** > **워크스페이스 설정** 아래의 **이메일 환경설정**으로 이동합니다.
2. **Link Aliasing Settings** 탭을 선택합니다.

{% alert important %}
[이전 탐색]({{site.baseurl}}/user_guide/administer/personal/the_braze_dashboard/)을 사용하는 경우 이러한 설정은 **설정 관리** 아래에 있습니다.
{% endalert %}

여기에서 링크 별칭을 정렬, 검색하고 추적을 해제할 수 있습니다.

![다양한 캠페인과 연결된 활성 및 비활성 링크 별칭을 보여주는 추적된 링크 별칭 페이지.]({% image_buster /assets/img/tracked_aliases.png %})

{% alert tip %}
[Campaign의 링크 별칭 목록]({{site.baseurl}}/get_campaign_link_alias/) 및 [Canvas의 링크 별칭 목록]({{site.baseurl}}/get_canvas_link_alias/) 엔드포인트를 사용하여 캠페인의 각 메시지 배리언트 또는 이메일 전용 Canvas 구성요소에 설정된 `alias`를 추출할 수 있습니다.
{% endalert %}

Braze는 이메일 내 링크를 평가하고, 링크 템플릿을 추가하며, 세분화 및 보고 목적에 적합한 명명 규칙을 제공할 것을 권장합니다. 이를 통해 모든 링크를 추적할 수 있습니다.

링크 별칭 지정이 활성화되면 메시지, Content Blocks 및 링크 템플릿은 수정되지 않습니다. 링크 템플릿이나 Content Blocks을 사용하는 기존 메시지는 동일하게 유지됩니다. 그러나 메시지를 업데이트하면 링크 별칭 마크업이 모든 링크에 적용되므로 링크가 표시되려면 링크 템플릿을 다시 적용해야 합니다.

## 링크 별칭 지정으로 링크가 업데이트되는 방식 {#how-links-are-updated-with-link-aliasing}

다음 표는 이메일 본문의 링크, 링크 별칭 지정 결과 및 원래 링크가 링크 별칭 지정으로 어떻게 업데이트되는지에 대한 설명의 예시를 제공합니다.

### 고정 링크 {#permalink}

**로직:** Braze가 물음표(?)를 삽입하고 URL에 첫 번째 쿼리 매개변수를 추가합니다.

| 이메일 본문의 링크 | 별칭이 적용된 링크 |
|-----------------------|----------------------------------------|
| `https://www.braze.com` | `https://www.braze.com?lid=slfdldtqdhdk` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 추가 쿼리 매개변수가 있는 링크 {#link-with-more-query-parameters}

**로직:** Braze가 다른 쿼리 매개변수를 감지하고 URL 끝에 `lid=`를 추가합니다.

| 이메일 본문의 링크 | 별칭이 적용된 링크 |
|---------------------------------------------------------------|--------------------------------------------------------------------------------|
| `https://www.braze.com?utm_campaign=retention&utm_source=email` | `https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### HTML 링크 {#html-link}

**로직:** Braze가 링크가 URL이며 이미 물음표(?)가 있음을 인식하여 물음표 뒤에 `lid` 쿼리 매개변수를 추가합니다.

| 이메일 본문의 링크 | 별칭이 적용된 링크 |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| {%raw%}`<a href="{{custom_attribute.{product_url}}}?">`{%endraw%} | {%raw%}`<a href="{{custom_attribute.{product_url}}}?lid=ac7a548g5kl7">`{%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 앵커가 있는 링크 {#link-with-anchor}

**로직:** Braze는 URL이 물음표(?) 뒤에 앵커(#)가 있는 표준 구조를 사용할 것으로 예상합니다. Braze는 왼쪽에서 오른쪽으로 읽기 때문에 물음표와 `lid` 값이 앵커 앞에 추가됩니다.

| 이메일 본문의 링크 | 별칭이 적용된 링크 |
|--------------------------------------------------|-------------------------------------------------------------------|
| `https://www.braze.com#bookmark1?utm_source=email` | `https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 앵커와 캡처 태그가 있는 링크 {#link-with-anchor-and-capture-tag}

**로직:** 앵커(#)가 포함된 URL에서 링크 별칭 지정을 사용할 때, Braze는 앵커가 쿼리 매개변수 뒤에 배치될 것으로 예상합니다. 즉, 적절한 추적을 위해 `lid` 값이 앵커 **앞에** 추가되어야 하며, Braze가 URL을 왼쪽에서 오른쪽으로 읽기 때문에 물음표(?)와 `lid`가 앵커 앞에 와야 합니다.

| 이메일 본문의 링크 | 별칭이 적용된 링크 |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| {%raw%}`<a href="https://www.braze.com/promotions#special-offer">Check out our special offer!</a>`{%endraw%}  | {%raw%}`<a href="https://www.braze.com/promotions?lid={{link_alias}}#special-offer">Check out our special offer!</a>` {%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 링크 별칭 추적 {#tracking-link-aliases}

**Link Management** 탭에서 세분화 목적으로 "추적"할 별칭을 선택하고 세분화 필터에 표시되도록 합니다. 추적된 별칭은 세분화 목적으로만 사용되며 보고 목적의 링크 추적에는 영향을 미치지 않습니다.

{% alert tip %}
링크 참여 측정기준을 추적하려면 링크가 HTTP 또는 HTTPS로 시작하는지 확인하세요. 특정 링크의 클릭 추적을 해제하려면 [유니버설 링크 및 앱 링크]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links/#turning-off-click-tracking-on-a-link-to-link-basis)를 참조하세요.
{% endalert %}

Braze에서는 추적할 링크를 무제한으로 선택할 수 있지만, 가장 최근에 열어본 링크에 대해서만 사용자를 리타겟팅할 수 있습니다. 사용자 프로필에는 가장 최근에 클릭한 100개의 링크가 포함됩니다. 예를 들어, 500개의 링크를 추적하고 사용자가 500개 모두를 클릭한 경우, 가장 최근에 클릭한 100개의 링크를 기반으로 리타겟팅하거나 세그먼트를 생성할 수 있습니다.

![두 개의 링크가 선택된 Link Management 탭.]({% image_buster /assets/img/link_management_dnd.png %})

{% alert note %}
Braze는 프로필 수준에서 마지막으로 클릭한 링크 별칭 100개까지만 추적합니다.
{% endalert %}

### 행동 기반 필터 {#action-based-filters}

모든 링크(추적 또는 비추적)를 타겟팅하는 행동 기반 메시지를 생성하거나, 이메일 캠페인 또는 Canvas 구성요소에서 별칭을 클릭했는지 여부에 따라 사용자를 리타겟팅할 수 있습니다.

![사용자가 Canvas 구성요소에서 별칭을 클릭했거나 캠페인과 상호작용한 경우를 타겟팅하는 행동 기반 옵션.]({% image_buster /assets/img/link_aliasing_action_based_filters.png %})

### 세분화 필터 {#segmentation-filters}

Braze에서 이메일에 링크 별칭이 있고 사용자가 이를 클릭하면 해당 이벤트가 별칭과 함께 사용자 프로필에 기록됩니다.

"모든 Campaign 또는 캔버스 단계에서 별칭 클릭" 세분화 필터를 사용한 후 이 링크 별칭의 이름을 변경하기로 결정하면, 사용자 프로필의 이전 클릭 데이터는 **업데이트되지 않으며** 여전히 이전 링크 별칭으로 표시됩니다. 따라서 새 링크 별칭을 기반으로 사용자를 타겟팅하면 이전 링크 별칭의 데이터는 포함되지 않습니다.

"Campaign에서 별칭 클릭" 또는 "Canvas에서 별칭 클릭" 세분화 필터를 사용하면 특정 캠페인 또는 Canvas에서 특정 별칭을 클릭했는지 여부로 사용자를 필터링합니다. 여러 사용자가 동일한 이메일 주소를 공유하고 링크 별칭이 클릭되면, 해당 이메일 주소를 공유하는 다른 모든 사용자의 프로필이 업데이트됩니다. 이러한 프로필은 클릭 이벤트뿐만 아니라 전달 및 열기 이벤트에 의해서도 업데이트됩니다.

다음 세분화 필터는 이벤트가 처리되는 시점에 추적되는 클릭 이벤트에 적용됩니다. 즉, 추적되지 않은 링크는 기존 데이터를 제거하지 않으며 링크를 추적해도 데이터가 소급 적용되지 않습니다. 자세한 내용은 [세분화 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/)를 참조하세요.

#### 링크 추적 해제 {#untracking-links}

링크 추적을 해제해도 추적 해제된 별칭에 대한 필터가 있는 기존 세그먼트가 재할당되지 않습니다. 이전 데이터는 새로운 데이터로 대체될 때까지 사용자 프로필에 남아 있습니다.

아카이브된 메시지의 링크는 자동으로 추적이 해제됩니다. 그러나 아카이브된 메시지가 아카이브 해제되면 링크를 다시 추적해야 합니다. 링크 별칭이 추적되면 링크 보고는 최상위 도메인이나 전체 URL 대신 별칭으로 인덱싱됩니다.

이메일 캠페인의 모든 링크와 해당 총 클릭 수를 보려면 **Message Analytics** > **이메일 성과** > **Preview & Heatmap**으로 이동하여 **Show Heatmap** 토글을 선택합니다.

![링크 별칭과 총 클릭 수가 표시된 총 클릭 수별 링크 테이블 패널.]({% image_buster /assets/img/link_alias_total_clicks.png %}){: style="max-width:60%;"}

### 이메일 클릭 이벤트 {#email-clicks-event}

Currents로 참여 데이터를 내보내는 경우, 링크 별칭 지정이 활성화되어 있으면 이메일 클릭 이벤트가 약간 다릅니다. 링크 별칭 지정이 활성화되면 [이메일 클릭 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-clicks-events/)에 `link_id`와 `link_alias`라는 두 개의 추가 필드가 포함됩니다.

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
`dispatch_id`의 동작은 Canvas와 Campaigns 간에 다릅니다. Braze는 Canvas 단계(스케줄할 수 있는 진입 단계 제외)를 "스케줄"된 경우에도 트리거된 이벤트로 처리하기 때문입니다. Canvas와 Campaigns에서의 [`dispatch_id` 동작]({{site.baseurl}}/help/help_articles/data/dispatch_id/)에 대해 자세히 알아보세요.

_2019년 8월에 업데이트되었습니다._
{% endalert %}

## Content Blocks에서의 링크 별칭 지정 {#link-aliasing-in-content-blocks}

새 Content Blocks은 해당되는 경우 Braze가 각 링크에 `lid={{placeholder}}`를 추가하여 링크가 수정됩니다. 이 플레이스홀더 값은 이메일 메시지 배리언트에 삽입될 때 확인됩니다.

Braze가 링크 별칭 지정을 활성화하기 전에 생성된 기존 Content Blocks 내의 링크를 수정하려면 기존 Content Blocks을 복제한 다음 복제된 Content Blocks 내의 링크를 수정하세요.

`lid` 값이 없는 Content Blocks이 새 메시지에 삽입되면 해당 Content Blocks의 링크는 별칭으로 추적되지 않습니다. 새 Content Blocks이 "이전" 메시지 배리언트에 삽입되면 해당 메시지 배리언트의 링크는 링크 별칭 지정에 의해 인식됩니다. Content Blocks의 링크도 인식됩니다. 그러나 "이전" Content Blocks은 "새" Content Blocks을 중첩할 수 없습니다.

{% alert tip %}
Content Blocks의 경우, Braze는 새 메시지에서 사용할 기존 Content Blocks의 사본을 생성할 것을 권장합니다. 이는 일괄 복제를 통해 수행할 수 있으며, 새 메시지에서 링크 별칭 지정이 활성화되지 않은 Content Blocks을 참조하는 시나리오를 방지할 수 있습니다.
{% endalert %}

## Liquid로 생성된 URL에 대한 링크 별칭 지정 {#link-aliasing-for-urls-generated-by-liquid}

HTML의 `assign` 문이나 Content Blocks에서 생성된 것과 같이 Liquid로 생성된 URL의 경우, Liquid 태그에 물음표(`?`)를 추가해야 합니다. 이를 통해 Braze가 쿼리 매개변수(`lid=somevalue`)를 추가하여 링크 별칭 지정이 올바르게 작동할 수 있습니다.

쿼리 매개변수를 추가할 위치를 식별하지 않으면 링크 별칭 지정이 이러한 URL을 인식하지 못하며 링크 템플릿이 적용되지 않습니다.

### 예시 {#example}

링크의 권장 형식에 대한 링크 별칭 지정 예시를 확인하세요:

{% raw %}
```liquid
{% assign link1 = "https://www.braze1.com" %}

<a href="{{link1}}?">Click Here</a>
```
{% endraw %}

링크에 물음표(`?`)가 포함된 매개변수가 있는 경우, 다음 예시와 같이 앵커 태그에서 앰퍼샌드(`&`)로 대체할 수 있습니다:

{% raw %}
```liquid
{% assign link_with_params = "https://www.braze1.com?param_1&param_2" %}

<a href="{{link_with_params}}&">Click Here</a>
```
{% endraw %}

### 조건부 Liquid가 포함된 URL {#urls-with-conditional-liquid}

조건부 Liquid 태그가 `href` 내에서 사용되는 경우(예: {% raw %}`{% if %}`, `{% unless %}`{% endraw %}를 사용하여 조건부로 URL을 설정하는 경우), 링크 별칭 지정이 해당 링크에 적용되지 않습니다. 즉, 이러한 링크는 **Link Management**에 표시되지 않으며 클릭 추적을 위한 `lid`를 받지 않습니다.

{% raw %}`{% capture %}`{% endraw %} 블록을 사용하여 `href` 외부에서 URL을 구성한 다음 다음 예시와 같이 변수로 참조할 수 있습니다:

{% raw %}
```liquid
  {%- if condition -%}
    https://example.com/url1
  {%- else -%}
    https://example.com/url2
  {%- endif -%}
{%- endcapture -%}

<a href="{{ url }}?">Click here</a>
```
{% endraw %}