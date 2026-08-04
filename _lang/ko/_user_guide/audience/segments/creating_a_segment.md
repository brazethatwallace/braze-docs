---
nav_title: 세그먼트 생성
article_title: 세그먼트 생성
page_order: 1
page_type: tutorial
description: "이 사용 방법 문서에서는 Braze를 사용하여 세그먼트를 설정하고 생성하는 방법을 안내합니다."
tool: Segments
search_rank: 3
---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"}세그먼트 생성 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomsegmentation-course-stylefloatrightwidth120pxborder0-classnoimgbordercreate-a-segment}

> 세분화를 사용하면 인구통계학적, 행동적 또는 기술적 특성과 행동을 기반으로 사용자를 타겟팅할 수 있습니다. 세분화와 메시징 자동화를 창의적이고 지능적으로 활용하면 사용자를 첫 접점에서 장기 고객으로 원활하게 전환할 수 있습니다. Segment는 데이터가 변경될 때 실시간으로 업데이트되며, 타겟팅 및 메시징 목적에 필요한 만큼 세그먼트를 생성할 수 있습니다.

## 1단계: Segments 섹션으로 이동 {#step-1-navigate-to-the-segments-section}

**오디언스** > **Segments**로 이동합니다.

## 2단계: Segment 이름 지정 {#step-2-name-your-segment}

**Segment 만들기**를 선택하여 Segment 구축을 시작합니다. 필터링하려는 사용자 유형을 설명하여 Segment의 이름을 지정합니다. 이렇게 하면 Campaigns 또는 Canvases에서 타겟팅할 때 Segment를 쉽게 식별할 수 있습니다. 모호한 Segment 제목은 혼란을 줄 수 있습니다.

또한 Operator에게 타겟 오디언스에 대한 설명을 바탕으로 Segment의 필터 로직을 구축하도록 요청할 수 있습니다. 자세한 내용은 [Operator로 할 수 있는 것]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#campaigns-and-audiences)을 참조하세요.

선택적으로 다음을 수행할 수 있습니다:
- Segment에 설명을 추가하여 이 오디언스의 의도에 대한 세부 정보를 제공하고 다른 팀원이 참고할 수 있는 메모를 남깁니다.
- Segment에 [팀]({{site.baseurl}}/user_guide/administer/global/user_management/teams)을 추가합니다.
- 추가적인 정리를 위해 Segment에 [태그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)를 추가합니다.

Segment는 **Segment 만들기**를 선택하는 즉시 저장됩니다. Segment 편집기에서 먼저 **저장**을 선택할 필요가 없습니다.

{% alert note %}
팀 수준의 "Edit Segments" 권한만 있고 워크스페이스 수준 권한이 없는 경우, Braze는 Segment가 생성될 때 팀을 할당합니다:
<br><br>
- **적격 팀이 하나인 경우:** 해당 팀이 자동으로 할당됩니다.
- **적격 팀이 여러 개인 경우:** Braze는 적격 팀 목록에서 첫 번째 팀을 할당합니다. Segment를 공유하거나 사용하기 전에 Segment 편집기에서 팀을 변경할 수 있습니다.
{% endalert %}

## 3단계: 앱 또는 플랫폼 선택 {#step-3-choose-your-app-or-platform}

**모든 앱의 사용자**(기본값) 또는 **특정 앱의 사용자**를 선택하여 타겟팅할 앱이나 플랫폼을 선택합니다. **특정 앱의 사용자**는 지정된 앱에서 하나 이상의 세션이 있는 사용자를 타겟팅합니다.

예를 들어, iOS 기기에만 인앱 메시지를 보내려면 iOS 앱을 선택합니다. 이렇게 하면 iOS와 Android 기기를 모두 사용하는 사용자가 iOS 기기에서만 메시지를 수신하게 됩니다. 특정 앱 목록에서 **앱이 없는 사용자** 옵션을 사용하면 세션이 없고 앱 데이터가 없는 사용자(일반적으로 사용자 가져오기 또는 REST API를 통해 생성된 사용자)를 포함할 수 있습니다.

![사용된 앱 섹션에서 '모든 앱의 사용자' 옵션이 선택된 Segment 세부 정보 패널.]({% image_buster /assets/img_archive/Segment2.png %}){: style="max-width:80%;"}

## 4단계: Segment에 필터 추가하기 {#step-4-add-filters-to-your-segment}

Segment에 최소 하나의 필터를 추가하세요. 원하는 만큼 필터를 조합하여 세분화를 더 구체적으로 만들 수 있습니다.

{% multi_lang_include alerts/note_alerts.md alert='Segment profiles first app use' %}

### 필터 그룹 {#filter-groups}

필터는 필터 그룹으로 구성됩니다. 모든 필터는 최소 하나의 필터가 포함된 필터 그룹에 속해야 합니다. Segment에는 여러 필터 그룹을 포함할 수 있습니다. 필터 그룹을 추가하려면 **필터 그룹 추가**를 선택하세요. 필터 그룹 이름 옆에 마우스를 올리면 나타나는 아이콘을 선택하여 이름을 편집할 수 있습니다.

![필터 그룹 이름 옆에 편집 아이콘이 있는 필터 그룹.]({% image_buster /assets/img_archive/edit_filter_group_name.png %})

각 필터 옆의 아이콘을 선택하여 필터 편집기를 접거나 개별 필터를 복제할 수 있습니다. 필터를 복제한 후 각 드롭다운에서 값을 조정할 수 있습니다.

### AND 및 OR을 사용한 세분화 로직 {#segmentation-logic-using-and-and-or}

필터 그룹 내에서 필터는 "AND" 또는 "OR"로 결합할 수 있습니다. 필터 그룹 간에도 "AND" 또는 "OR"로 결합할 수 있습니다. 필터 그룹을 사용하면 다음과 같은 세분화 로직을 만들 수 있습니다:
- (A AND B AND C) OR (C AND E AND F)
- (A OR B OR C) AND (C OR D OR F)

필터에 "OR"를 선택하면 해당 필터 중 하나, 일부 또는 전부의 조합을 충족하는 사용자가 Segment에 포함됩니다. "AND"를 선택하면 해당 필터를 통과하지 못한 사용자는 Segment에 포함되지 않습니다.

{% alert tip %}
부정 필터(예: 구독 그룹에서 "아님")를 포함하는 필터에 "OR"를 선택할 때, 사용자는 "OR" 필터 중 하나만 충족하면 Segment에 포함된다는 점을 기억하세요. 다른 필터와 관계없이 부정 필터를 적용하려면 [제외 그룹](#exclusion)을 사용하세요.
{% endalert %}

{% details OR 연산자를 피해야 하는 경우 %}

사용자 타겟팅 상황에서 `OR` 연산자 사용을 피해야 하는 경우가 있습니다. `OR` 연산자는 사용자가 구문 내 필터 중 하나 이상의 기준을 충족하면 참으로 평가되는 구문을 생성합니다. 예를 들어, "Foodies"에 속하지만 "Non-foodies" 또는 "Candy-lovers"에는 속하지 않는 사용자의 Segment를 만들고 싶다면, 여기서 `OR` 연산자를 사용할 수 있습니다.

![Segment "foodies"에 속하고 Segment "non-foodies" 또는 "candy-lovers"에 속하지 않는 사용자를 위한 필터 그룹.]({% image_buster /assets/img_archive/or_operator_segment.png %})

그러나 "Foodies" Segment에 속하면서 "Non-foodies"와 "Candy-lovers" Segment 모두에 속하지 않는 사용자를 세분화하려면 `AND` 연산자를 사용하세요. 이렇게 하면 Campaign 또는 Canvas를 수신하는 사용자가 의도한 Segment("foodies")에 속하면서 동시에 다른 Segment("Non-foodies" 및 "Candy-lovers")에는 속하지 않게 됩니다.

다음 부정 타겟팅 기준은 두 개 이상의 필터가 동일한 속성을 참조할 때 `OR` 연산자와 함께 사용하면 안 됩니다:

- `not included`
- `is not`
- `does not equal`
- `does not match regex`

`not included`, `is not`, `does not equal` 또는 `does not match regex`가 구문에서 `OR` 연산자와 함께 두 번 이상 사용되면, 해당 속성의 모든 값을 가진 사용자가 타겟팅됩니다.

{% enddetails %}

### 필터 연산자 {#filter-operators}

선택한 특정 필터에 따라 필터 값을 식별하기 위한 다양한 연산자가 제공됩니다. 다양한 유형의 커스텀 속성에 사용할 수 있는 연산자에 대해 자세히 알아보려면 [커스텀 속성 저장]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#set-custom-attributes)을 참조하세요. "is any of" 연산자를 사용할 때 해당 필드에 포함할 수 있는 최대 항목 수는 256개입니다.

{% alert note %}
Braze는 사용자가 앱을 처음 사용할 때까지 프로필을 생성하지 않으므로, 아직 앱을 열지 않은 사용자를 타겟팅할 수 없습니다.
{% endalert %}

![AND 연산자가 적용된 세분화 필터 그룹.]({% image_buster /assets/img_archive/segmenter_filter_groups.png %})

{% alert important %}
**Segment 멤버십** 필터를 이미 사용하고 있는 Segments는 다른 Segments에 추가로 포함하거나 중첩할 수 없습니다. 이는 Segment A가 Segment B를 포함하고, Segment B가 다시 Segment A를 포함하려는 순환을 방지하기 위함입니다. 이런 상황이 발생하면 Segment가 계속 자기 자신을 참조하게 되어 실제로 누가 해당 Segment에 속하는지 계산하는 것이 불가능해집니다.

또한 이렇게 Segments를 중첩하면 복잡성이 증가하고 속도가 느려질 수 있습니다. 대신 포함하려는 Segment를 동일한 필터를 사용하여 다시 만드세요.
{% endalert %}

### 제외 그룹 (선택 사항) {#exclusion}

Segment를 구축할 때 하나 이상의 제외 그룹을 적용할 수 있습니다. 제외 그룹에는 Segment에서 제외할 사용자를 식별하는 기준이 포함되며, 항상 "AND NOT" 연산자로 필터 그룹에 연결됩니다.

제외 그룹은 Segment 기준보다 우선합니다. 사용자가 제외 그룹 기준에 해당하면, 필터 그룹 내의 기준을 충족하더라도 해당 Segment에 포함되지 않습니다.

필터 그룹과 마찬가지로 필터를 추가하여 제외 그룹을 만드세요. 제외 그룹의 *예상 도달 가능 사용자* 통계는 제외 기준이 적용된 후 Segment에 남아 있는 예상 사용자 수를 보여줍니다.

제외된 사용자는 Segment의 *총 도달 가능 사용자* 통계에 포함되지 않습니다.

![두 개의 필터가 있는 제외 그룹.]({% image_buster /assets/img_archive/segmenter_exclusion_groups.png %})

### 퍼널 통계 보기 {#viewing-funnel-statistics}

**퍼널 통계 보기**를 선택하면 해당 필터 그룹의 통계를 표시하고 추가된 각 필터가 Segment 통계에 미치는 영향을 확인할 수 있습니다. 해당 시점까지의 모든 필터에 의해 타겟팅된 사용자의 예상 수와 비율을 볼 수 있습니다. 필터 그룹의 통계가 표시되면 필터를 변경할 때마다 자동으로 업데이트됩니다. 이 통계는 추정치이며 생성하는 데 잠시 시간이 걸릴 수 있습니다.

필터 사이에 AND를 사용하면 퍼널 통계가 감소하고, OR을 사용하면 퍼널 통계가 증가한다는 점을 기억하세요.

![Segment 퍼널 통계가 표시된 두 개의 필터.]({% image_buster /assets/img_archive/segment_funnel_statistics.png %})

사용자 흐름을 기록하는 필터를 추가하면 사용자가 이탈하는 지점을 확인할 수 있습니다. 예를 들어, 소셜 네트워킹 앱에서 온보딩 과정 중 사용자를 잃는 지점을 파악하고 싶다면, 가입, 친구 추가, 첫 메시지 전송에 대한 커스텀 데이터 필터를 추가할 수 있습니다. 85%의 사용자가 가입하고 친구를 추가하지만 45%만 첫 메시지를 보냈다면, 온보딩 및 마케팅 캠페인에서 더 많은 메시지 전송을 유도하는 데 집중해야 한다는 것을 알 수 있습니다.

### 테스트 세그먼트 {#testing-segments}

Segment에 앱과 필터를 추가한 후, 사용자를 조회하여 Segment 기준에 부합하는지 확인함으로써 Segment가 예상대로 설정되었는지 테스트할 수 있습니다. 이를 위해 **사용자 조회** 섹션에서 사용자의 `external_id` 또는 `braze_id`를 검색하세요.

{% alert note %}
**사용자 조회**는 `external_id`와 `braze_id`만 허용합니다. 이메일 주소, 전화번호 또는 기타 식별자는 허용되지 않습니다. 이메일, 전화번호 또는 기타 필드로 프로필을 찾으려면 [**사용자 검색**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#access-profiles)을 대신 사용하세요.
{% endalert %}

![검색 필드가 있는 사용자 조회 섹션.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%;"}

사용자 조회는 다음 경우에 사용할 수 있습니다:
- Segment 생성 시
- Campaign 또는 Canvas 오디언스 설정 시
- 오디언스 경로 단계 설정 시

사용자가 Segment, 필터 및 앱 기준에 부합하면 이를 알리는 알림이 표시됩니다.

!["testuser"에 대한 사용자 조회 결과, "testuser가 모든 Segments, 필터 및 앱에 부합합니다."라는 알림이 표시됩니다.]({% image_buster /assets/img_archive/user_lookup_match.png %})

사용자가 Segment, 필터 또는 앱 기준의 일부 또는 전부에 부합하지 않으면, 문제 해결을 위해 누락된 기준이 나열됩니다.

!["test1이 다음 타겟팅 기준에 부합하지 않습니다:"라는 알림과 함께 누락된 기준이 표시된 사용자 조회 결과.]({% image_buster /assets/img_archive/user_lookup_nomatch.png %})

### 단일 사용자 Segments {#single-user-segments}

사용자 이름이나 사용자 ID와 같이 사용자를 식별하는 고유 속성을 사용하여 단일 사용자 Segments(또는 소수의 사용자로 구성된 Segments)를 만들 수 있습니다.

그러나 세분화 통계 또는 미리보기에서 이 개별 사용자가 표시되지 않을 수 있습니다. Segment 통계는 결과가 +/- 1% 이내일 95% 신뢰 구간의 무작위 표본을 기반으로 계산되기 때문입니다. 사용자 기반이 클수록 Segment 크기가 대략적인 추정치일 가능성이 높습니다. 타겟팅하는 단일 사용자가 Segment에 포함되어 있는지 확인하려면 **정확한 통계 계산**을 선택하세요. 이렇게 하면 99.999% 이상의 정확도로 Segment 내 정확한 사용자 수를 계산합니다.

Braze에는 사용자 ID 또는 이메일 주소로 특정 사용자를 타겟팅하기 위한 테스트 필터가 있습니다.

## 5단계: Segment 저장 {#step-5-save-your-segment}

**저장**을 선택합니다. 이제 사용자에게 메시지를 보낼 준비가 되었습니다!

## Segment 크기 측정 {#measuring-segment-size}

Segment의 멤버십과 크기를 모니터링하는 방법에 대해 알아보려면 [Segment 크기 측정]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size)을 참조하세요.

## Segments 보관하기 {#archiving-segments}

특정 Segment가 더 이상 필요하지 않거나 사용을 중단하려면, **Segments** 페이지로 이동하여 해당 Segment 행의 메뉴에서 **Archive**를 선택하여 보관할 수 있습니다.

{% alert warning %}
Segment를 보관하면, 해당 Segment를 사용하는 모든 Campaigns 또는 Canvases(단일 Canvas 구성 요소에서만 사용되는 경우 포함)도 함께 보관됩니다. 여기에는 중첩된 Segments도 포함되며, 두 Segments와 이를 사용하는 모든 Campaigns 또는 Canvases도 함께 보관됩니다.
<br><br>
연결된 Segment를 보관할 때 어떤 Campaigns와 Canvases가 함께 보관되는지 알려주는 경고 메시지가 표시됩니다.
{% endalert %}

**Segments** 페이지에서 해당 Segment로 이동한 다음 **Unarchive**를 선택하면 보관을 해제할 수 있습니다.

## 사용자가 여러 기기를 사용하는 경우의 타겟팅 동작 {#targeting-behavior-when-users-have-multiple-devices}

사용자가 여러 기기에서 동일한 계정으로 로그인하면 둘 이상의 기기를 보유하게 됩니다. [고객 프로필]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles)의 **최근 기기** 섹션에서 여러 기기를 확인할 수 있습니다.

기기 종속 필터(기기 모델, 기기 OS, 앱 버전)로 세분화할 때, Segment에는 필터 기준에 일치하는 모든 사용자가 포함됩니다. 이 사용자들은 필터 기준을 충족하지 않는 기기를 포함하여 모든 기기에서 메시지를 수신합니다. 예를 들어, 사용자 A가 두 대의 기기를 보유하고 있다고 가정합니다. 기기 1은 OS 13.0이고, 기기 2는 OS 10.0입니다. Segment가 OS 10.0 사용자를 타겟팅하는 경우, 이 사용자는 해당 Segment에 포함되어 두 기기 모두에서 메시지를 수신합니다.

### 푸시 알림 {#push-notifications}

각 사용자에게 하나의 푸시 알림만 전송되도록 지정할 수 있습니다. [메시지를 작성]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#step-4-compose-your-push-message)할 때, **추가 설정**에서 **사용자의 마지막 사용 기기에만 전송**을 선택합니다.

!["추가 설정"에서 사용자의 마지막 사용 기기에만 전송하는 체크박스.]({% image_buster /assets/img_archive/send_to_last_device.png %}){: style="max-width:60%;"}

### 고려 사항 {#considerations}

- **메시지 전송 수가 오디언스 규모를 초과할 수 있습니다.** 일부 사용자가 둘 이상의 기기를 보유한 경우, 각 기기에서 메시지를 수신할 수 있습니다. 이로 인해 Segment 내 사용자 수보다 메시지 전송 수가 더 많아질 수 있습니다.
- **사용자의 Segment 멤버십이 예상과 다를 수 있습니다.**
    - 사용자가 다른 기기와 연결된 속성을 기반으로 현재 기기에서 타겟팅될 수 있습니다. 사용자가 메시지를 수신할 것으로 예상하지 않았다면, 고객 프로필에서 여러 기기를 확인해 보세요.
    - 사용자가 전송 시점에 타겟 Segment에 포함되어 있었지만, 보유한 기기 중 하나와 관련된 행동으로 인해 이후에는 해당 Segment에 포함되지 않을 수 있습니다. 이로 인해 사용자가 현재 필터 기준에 일치하지 않더라도 Campaign 또는 Canvas를 수신할 수 있습니다. <br><br>예를 들어, 사용자가 현재 OS 13.0을 사용하고 있더라도 최신 앱 버전이 OS 10.0인 사용자를 타겟팅하는 메시지를 수신할 수 있습니다. 이 경우, 메시지가 전송될 때 사용자가 OS 10.0을 사용하고 있었고 이후에 OS 13.0으로 업그레이드한 것입니다.<br><br> 마찬가지로, 사용자가 나중에 다른 앱 버전의 기기를 사용하면 고객 프로필이 새로운 최신 앱 버전으로 업데이트됩니다. 이로 인해 사용자가 메시지 수신 자격이 없었던 것처럼 보일 수 있지만, 실제로는 전송 시점에 자격을 충족했던 것입니다.