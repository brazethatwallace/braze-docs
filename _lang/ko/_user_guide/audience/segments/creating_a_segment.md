---
nav_title: 세그먼트 생성
article_title: 세그먼트 생성
page_order: 1
page_type: tutorial
description: "이 사용 방법 문서에서는 Braze를 사용하여 Segment를 설정하고 생성하는 방법을 안내합니다."
tool: Segments
search_rank: 3
---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"}세그먼트 생성 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomsegmentation-course-stylefloatrightwidth120pxborder0-classnoimgbordercreate-a-segment}

> 세분화를 사용하면 인구통계학적, 행동적 또는 기술적 특성과 행동을 기반으로 사용자를 타겟팅할 수 있습니다. 세분화와 메시징 자동화를 창의적이고 지능적으로 활용하면 사용자를 첫 접점에서 장기 고객으로 원활하게 전환할 수 있습니다. Segment는 데이터가 변경될 때 실시간으로 업데이트되며, 타겟팅 및 메시징 목적에 필요한 만큼 Segment를 생성할 수 있습니다.

## 1단계: Segments 섹션으로 이동 {#step-1-navigate-to-the-segments-section}

**오디언스** > **Segments**로 이동합니다.

## 2단계: Segment 이름 지정 {#step-2-name-your-segment}

**세그먼트 생성**을 선택하여 Segment 구축을 시작합니다. 필터링하려는 사용자 유형을 설명하여 Segment의 이름을 지정합니다. 이렇게 하면 Campaigns 또는 Canvases에서 타겟팅할 때 Segment를 쉽게 식별할 수 있습니다. 모호한 Segment 제목은 혼란을 줄 수 있습니다.

선택적으로 다음을 수행할 수 있습니다:
- Segment에 설명을 추가하여 이 오디언스의 의도에 대한 자세한 내용을 제공하고 다른 팀원이 참조할 수 있는 메모를 남깁니다.
- Segment에 [팀]({{site.baseurl}}/user_guide/administer/global/user_management/teams/)을 추가합니다.
- 추가 정리를 위해 Segment에 [태그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/)를 추가합니다.

![Segment 이름이 'Lapsed Users'이고 Segment 설명이 'This is our main Lapsed User segment to target non-actives within the past fourteen days.'인 세그먼트 생성 모달. 취소 및 세그먼트 생성 두 개의 버튼이 있습니다.]({% image_buster /assets/img_archive/segment_app_selection.png %}){: style="max-width:80%;"}

## 3단계: 앱 또는 플랫폼 선택 {#step-3-choose-your-app-or-platform}

**모든 앱의 사용자**(기본값) 또는 **특정 앱의 사용자**를 선택하여 타겟팅할 앱 또는 플랫폼을 선택합니다. **특정 앱의 사용자**는 지정된 앱에서 최소 한 번의 세션이 있는 사용자를 타겟팅합니다.

예를 들어, iOS 기기에만 인앱 메시지를 보내려면 iOS 앱을 선택합니다. 이렇게 하면 iOS와 Android 기기를 모두 사용하는 사용자가 iOS 기기에서만 메시지를 받게 됩니다. 특정 앱 목록에서 **앱이 없는 사용자** 옵션을 사용하면 세션이 없고 앱 데이터가 없는 사용자(일반적으로 사용자 가져오기 또는 REST API를 통해 생성됨)를 포함할 수 있습니다.

![앱 사용 섹션에서 '모든 앱의 사용자' 옵션이 선택된 Segment 세부 정보 패널.]({% image_buster /assets/img_archive/Segment2.png %}){: style="max-width:80%;"}

## 4단계: Segment에 필터 추가 {#step-4-add-filters-to-your-segment}

Segment에 최소 하나의 필터를 추가합니다. 세분화를 더 구체적으로 만들기 위해 원하는 만큼 필터를 결합할 수 있습니다.

{% multi_lang_include alerts/note_alerts.md alert='Segment profiles first app use' %}

### 필터 그룹 {#filter-groups}

필터는 필터 그룹으로 구성됩니다. 모든 필터는 최소 하나의 필터가 있는 필터 그룹에 속해야 합니다. Segment에는 여러 필터 그룹이 있을 수 있습니다. 필터 그룹을 추가하려면 **필터 그룹 추가**를 선택합니다. 필터 그룹 이름 옆에 마우스를 올리면 나타나는 아이콘을 선택하여 필터 그룹 이름을 편집합니다.

![필터 그룹 이름 옆에 편집 아이콘이 있는 필터 그룹.]({% image_buster /assets/img_archive/edit_filter_group_name.png %})

각 필터 옆의 아이콘을 선택하여 필터 편집기를 접거나 개별 필터를 복제합니다. 필터를 복제한 후 각 드롭다운에서 값을 조정할 수 있습니다.

### AND 및 OR을 사용한 세분화 로직 {#segmentation-logic-using-and-and-or}

필터 그룹 내에서 필터는 "AND" 또는 "OR"로 결합할 수 있습니다. 필터 그룹 간에도 "AND" 또는 "OR"로 결합할 수 있습니다. 필터 그룹을 사용하면 다음과 같은 세분화 로직을 만들 수 있습니다:
- (A AND B AND C) OR (C AND E AND F)
- (A OR B OR C) AND (C OR D OR F)

필터에 "OR"를 선택하면 해당 필터 중 하나, 일부 또는 전부의 조합을 충족하는 사용자가 Segment에 포함됩니다. "AND"를 선택하면 해당 필터를 통과하지 못하는 사용자는 Segment에 포함되지 않습니다.

{% alert tip %}
부정 필터(예: 구독 그룹에서 "다음이 아님")를 포함하는 필터에 "OR"를 선택할 때, 사용자는 Segment에 포함되기 위해 "OR" 필터 중 하나만 충족하면 된다는 점을 기억하세요. 다른 필터와 관계없이 부정 필터를 적용하려면 [제외 그룹](#exclusion)을 사용하세요.
{% endalert %}

{% details OR 연산자를 피해야 하는 경우 %}

`OR` 연산자를 사용하지 않아야 하는 사용자 타겟팅 상황이 있을 수 있습니다. `OR` 연산자는 사용자가 구문 내 하나 이상의 필터 기준을 충족하면 참으로 평가되는 구문을 만듭니다. 예를 들어, "Foodies"에 속하지만 "Non-foodies" 또는 "Candy-lovers"에 속하지 않는 사용자의 Segment를 만들려면 `OR` 연산자가 여기서 작동합니다.

!['foodies' Segment에 속하고 'non-foodies' 또는 'candy-lovers' Segment에 속하지 않는 사용자를 위한 필터 그룹.]({% image_buster /assets/img_archive/or_operator_segment.png %})

그러나 "Foodies" Segment에 속하면서 "Non-foodies"와 "Candy-lovers" Segment 모두에 속하지 않는 사용자를 세분화하려면 `AND` 연산자를 사용하세요. 이렇게 하면 Campaign 또는 Canvas를 받는 사용자가 의도한 Segment("foodies")에 속하면서 동시에 다른 Segment("Non-foodies" 및 "Candy-lovers")에 속하지 않게 됩니다.

다음 부정 타겟팅 기준은 두 개 이상의 필터가 동일한 속성을 참조할 때 `OR` 연산자와 함께 사용하면 안 됩니다:

- `not included`
- `is not`
- `does not equal`
- `does not match regex`

`not included`, `is not`, `does not equal` 또는 `does not match regex`가 구문에서 `OR` 연산자와 함께 두 번 이상 사용되면, 관련 속성의 모든 값을 가진 사용자가 타겟팅됩니다.

{% enddetails %}

### 필터 연산자 {#filter-operators}

선택한 특정 필터에 따라 필터 값을 식별하기 위한 다양한 연산자가 제공됩니다. 다양한 유형의 커스텀 속성에 사용할 수 있는 연산자에 대해 자세히 알아보려면 [커스텀 속성 저장]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#setting-custom-attributes)을 참조하세요. "is any of" 연산자를 사용할 때 해당 필드에 포함할 수 있는 최대 항목 수는 256개입니다.

{% alert note %}
Braze는 사용자가 앱을 처음 사용할 때까지 프로필을 생성하지 않으므로, 아직 앱을 열지 않은 사용자를 타겟팅할 수 없습니다.
{% endalert %}

![AND 연산자가 있는 세분화 필터 그룹.]({% image_buster /assets/img_archive/segmenter_filter_groups.png %})

{% alert important %}
이미 **Segment 멤버십** 필터를 사용하는 Segment는 다른 Segment에 추가로 포함하거나 중첩할 수 없습니다. 이는 Segment A가 Segment B를 포함하고, Segment B가 다시 Segment A를 포함하려는 순환을 방지합니다. 이런 일이 발생하면 Segment가 계속 자기 자신을 참조하게 되어 실제로 누가 속해 있는지 계산하는 것이 불가능해집니다.

또한 이와 같이 Segment를 중첩하면 복잡성이 증가하고 속도가 느려질 수 있습니다. 대신 포함하려는 Segment를 동일한 필터를 사용하여 다시 생성하세요.
{% endalert %}

### 제외 그룹(선택 사항) {#exclusion}

Segment를 구축할 때 하나 이상의 제외 그룹을 적용할 수 있습니다. 제외 그룹에는 Segment에서 제외할 사용자를 식별하는 기준이 포함되며, 항상 "AND NOT" 연산자로 필터 그룹에 연결됩니다.

제외 그룹은 Segment 기준보다 우선합니다. 사용자가 제외 그룹 기준에 해당하면 필터 그룹 내의 기준을 충족하더라도 Segment에 포함되지 않습니다.

필터 그룹과 마찬가지로 필터를 추가하여 제외 그룹을 만듭니다. 제외 그룹의 *예상 도달 가능 사용자* 통계는 제외 기준이 적용된 후 Segment에 남아 있는 예상 사용자 수를 보여줍니다.

제외된 사용자는 Segment의 *총 도달 가능 사용자* 통계에 포함되지 않습니다.

![두 개의 필터가 있는 제외 그룹.]({% image_buster /assets/img_archive/segmenter_exclusion_groups.png %})

### 퍼널 통계 보기 {#viewing-funnel-statistics}

**퍼널 통계 보기**를 선택하여 해당 필터 그룹의 통계를 표시하고 추가된 각 필터가 Segment 통계에 미치는 영향을 확인합니다. 해당 시점까지의 모든 필터에 의해 타겟팅된 사용자의 예상 수와 비율을 볼 수 있습니다. 필터 그룹에 대한 통계가 표시되면 필터를 변경할 때마다 자동으로 업데이트됩니다. 이 통계는 추정치이며 생성하는 데 시간이 걸릴 수 있습니다.

필터 사이에 AND를 사용하면 퍼널 통계가 감소하고, OR을 사용하면 퍼널 통계가 증가한다는 점을 유의하세요.

![Segment 퍼널 통계가 있는 두 개의 필터.]({% image_buster /assets/img_archive/segment_funnel_statistics.png %})

사용자 흐름을 기록하는 필터를 추가하면 사용자가 이탈하는 지점을 확인할 수 있습니다. 예를 들어, 소셜 네트워킹 앱에서 온보딩 과정 중 사용자를 잃는 지점을 확인하려면 가입, 친구 추가, 첫 메시지 보내기에 대한 커스텀 데이터 필터를 추가할 수 있습니다. 85%의 사용자가 가입하고 친구를 추가하지만 45%만 첫 메시지를 보냈다면, 온보딩 및 마케팅 Campaigns에서 더 많은 메시지 발송을 장려하는 데 집중해야 한다는 것을 알 수 있습니다.

### Segment 테스트 {#testing-segments}

Segment에 앱과 필터를 추가한 후, 사용자를 조회하여 Segment 기준에 일치하는지 확인함으로써 Segment가 예상대로 설정되었는지 테스트할 수 있습니다. 이를 위해 **사용자 조회** 섹션에서 사용자의 `external_id` 또는 `braze_id`를 검색합니다.

{% alert note %}
**사용자 조회**에서는 `external_id`와 `braze_id`만 사용할 수 있습니다. 이메일 주소, 전화번호 또는 기타 식별자는 사용할 수 없습니다. 이메일, 전화번호 또는 기타 필드로 프로필을 찾으려면 [**사용자 검색**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/#access-profiles)을 사용하세요.
{% endalert %}

![검색 필드가 있는 사용자 조회 섹션.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%;"}

사용자 조회는 다음 경우에 사용할 수 있습니다:
- Segment 생성 시
- Campaign 또는 Canvas 오디언스 설정 시
- 오디언스 경로 단계 설정 시

사용자가 Segment, 필터 및 앱 기준에 일치하면 알림이 표시됩니다.

!['testuser'에 대한 사용자 조회가 'testuser matches all of the segments, filters, and apps.'라는 알림을 표시합니다.]({% image_buster /assets/img_archive/user_lookup_match.png %})

사용자가 Segment, 필터 또는 앱 기준의 일부 또는 전부에 일치하지 않으면 문제 해결을 위해 누락된 기준이 나열됩니다.

!['test1 does not match the following targeting criteria:'라는 알림과 함께 누락된 기준을 표시하는 사용자 조회.]({% image_buster /assets/img_archive/user_lookup_nomatch.png %})

### 단일 사용자 Segment {#single-user-segments}

사용자 이름이나 사용자 ID와 같은 고유 속성을 사용하여 단일 사용자 Segment(또는 소수의 사용자 Segment)를 만들 수 있습니다.

그러나 세분화 통계 또는 미리보기에 이 개별 사용자가 표시되지 않을 수 있습니다. 이는 Segment 통계가 결과가 +/- 1% 이내인 95% 신뢰 구간의 무작위 표본을 기반으로 계산되기 때문입니다. 사용자 기반이 클수록 Segment 크기가 대략적인 추정치일 가능성이 높습니다. Segment에 타겟팅하는 단일 사용자가 포함되어 있는지 확인하려면 **정확한 통계 계산**을 선택합니다. 이렇게 하면 99.999% 이상의 정확도로 Segment의 정확한 사용자 수를 계산합니다.

Braze에는 사용자 ID 또는 이메일 주소로 특정 사용자를 타겟팅하는 테스트 필터가 있습니다.

## 5단계: Segment 저장 {#step-5-save-your-segment}

**저장**을 선택합니다. 이제 사용자에게 메시지를 보낼 준비가 되었습니다!

## Segment 크기 측정 {#measuring-segment-size}

Segment의 멤버십과 크기를 모니터링하는 방법에 대해 알아보려면 [Segment 크기 측정]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size/)을 참조하세요.

## Segment 아카이브 {#archiving-segments}

특정 Segment가 더 이상 필요하지 않거나 폐기하려면 **Segments** 페이지로 이동하여 해당 Segment 행의 메뉴에서 **아카이브**를 선택하여 아카이브할 수 있습니다.

{% alert warning %}
Segment를 아카이브하면 해당 Segment를 사용하는 모든 Campaigns 또는 Canvases(단일 Canvas 구성요소에서만 사용되는 경우 포함)도 함께 아카이브됩니다. 이는 중첩된 Segment에도 적용되며, 두 Segment와 이를 사용하는 모든 Campaigns 또는 Canvases도 아카이브됩니다.
<br><br>
연결된 Segment를 아카이브하면 어떤 Campaigns와 Canvases가 아카이브되는지 경고가 표시됩니다.
{% endalert %}

**Segments** 페이지에서 해당 Segment로 이동한 후 **아카이브 해제**를 선택하여 Segment의 아카이브를 해제할 수 있습니다.

## 사용자가 여러 기기를 사용하는 경우의 타겟팅 동작 {#targeting-behavior-when-users-have-multiple-devices}

사용자가 여러 기기에서 동일한 계정에 로그인하면 둘 이상의 기기를 가지게 됩니다. [고객 프로필]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/)의 **최근 기기** 섹션에서 여러 기기를 확인할 수 있습니다.

기기 종속 필터(기기 모델, 기기 OS, 앱 버전)로 세분화할 때 Segment에는 필터 기준에 일치하는 모든 사용자가 포함됩니다. 이 사용자들은 필터 기준을 충족하지 않을 수 있는 기기를 포함하여 모든 기기에서 메시지를 받게 됩니다. 예를 들어, 사용자 A가 두 개의 기기를 가지고 있다고 가정합니다: 기기 1은 OS 13.0이고 기기 2는 OS 10.0입니다. Segment가 OS 10.0인 사용자를 타겟팅하면 이 사용자는 해당 Segment에 포함되어 두 기기 모두에서 메시지를 받게 됩니다.

### 푸시 알림 {#push-notifications}

각 사용자에게 하나의 푸시 알림만 전송되도록 지정할 수 있습니다. [메시지 작성]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/#step-4-compose-your-push-message) 시 **추가 설정**에서 **사용자의 마지막 사용 기기에만 전송**을 선택합니다.

![사용자의 마지막 사용 기기에만 전송하는 체크박스가 있는 '추가 설정'.]({% image_buster /assets/img_archive/send_to_last_device.png %}){: style="max-width:60%;"}

### 고려 사항 {#considerations}

- **메시지 발송 수가 오디언스 크기를 초과할 수 있습니다.** 일부 사용자가 둘 이상의 기기를 가지고 있으면 각 기기가 메시지를 받을 수 있습니다. 이로 인해 Segment의 사용자 수보다 메시지 발송 수가 더 많아질 수 있습니다.
- **사용자의 Segment 멤버십이 예상과 다르게 보일 수 있습니다.**
    - 사용자가 다른 기기와 연결된 속성을 기반으로 현재 기기에서 타겟팅될 수 있습니다. 사용자가 메시지를 받을 것으로 예상하지 않았다면 고객 프로필에서 여러 기기를 확인하세요.
    - 사용자가 발송 시점에 타겟 Segment에 속해 있었지만, 기기 중 하나와 관련된 행동으로 인해 이후에는 해당 Segment에 속하지 않을 수 있습니다. 이로 인해 사용자가 현재 필터 기준에 일치하지 않더라도 Campaign 또는 Canvas를 받을 수 있습니다. <br><br>예를 들어, 사용자가 현재 OS 13.0을 사용하고 있더라도 최신 앱 버전이 OS 10.0인 사용자를 타겟팅하는 메시지를 받을 수 있습니다. 이 경우 메시지가 발송될 때 사용자가 OS 10.0을 사용하고 있었고 이후에 OS 13.0으로 업그레이드한 것입니다.<br><br> 마찬가지로, 사용자가 나중에 다른 앱 버전의 기기를 사용하면 고객 프로필이 새로운 최신 앱 버전으로 업데이트됩니다. 이로 인해 사용자가 메시지에 적합하지 않았어야 하는 것처럼 보일 수 있지만, 실제로는 발송 시점에 적합했던 것입니다.