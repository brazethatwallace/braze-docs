---
nav_title: 사용자 타겟팅
article_title: 사용자 타겟팅
page_order: 12
page_type: reference
description: "이 참조 문서에서는 Campaign 및 Canvas 편집기에서 오디언스를 타겟팅하는 방법을 다룹니다."
tool:
    - Campaigns
    - Canvas
---

# 사용자 타겟팅 {#target-users}

> Campaign 또는 Canvas를 만들 때 사용자를 어떻게 타겟팅할지 결정하는 것은 가장 중요한 단계 중 하나입니다. 사용자의 행동, 선호도, 인구통계를 기반으로 오디언스를 세분화하는 방법을 이해하면 메시징을 맞춤화하고 개인화할 수 있습니다.

## 타겟 오디언스 만들기 {#creating-a-target-audience}

### 1단계: 사용자 선택 {#step-1-choose-users}

**타겟팅 옵션**에서 다음 옵션을 사용하여 Campaign 또는 Canvas에서 타겟팅할 사용자를 선택할 수 있습니다. 정의한 기준에 맞는 사용자만 메시지를 수신합니다. 정확한 Segment 멤버십은 항상 메시지가 발송되기 직전에 계산된다는 점을 유의하세요.

{% tabs local %}
{% tab 단일 Segment %}
이전에 생성한 Segment의 멤버를 타겟팅하려면 **세그먼트별로 사용자 타겟팅** 아래의 드롭다운에서 하나의 Segment를 선택하세요.
{% endtab %}

{% tab 다중 Segments %}
이전에 생성한 여러 Segments에 해당하는 사용자를 타겟팅하려면 **세그먼트별로 사용자 타겟팅** 아래의 드롭다운에서 여러 Segments를 추가하세요. 결과 타겟 오디언스는 첫 번째 Segment와 두 번째 Segment, 세 번째 Segment 등에 모두 속하는 사용자가 됩니다.
{% endtab %}

{% tab 다중 필터 %}
Segment를 추가하지 않고 사용자를 타겟팅하려면 일련의 필터를 사용할 수 있습니다. 이는 메시지 생성 중 임시 오디언스를 만드는 것으로, 일회성 오디언스에 발송할 때 Segment 생성을 건너뛸 수 있습니다.

![하루 이내에 마지막으로 앱을 열었고, Campaign 또는 캔버스 단계를 수신한 적이 없으며, 30일 이내에 구매한 사용자를 타겟팅하는 메시지의 추가 필터.]({% image_buster /assets/img_archive/additional_filters.png %}){: style="max-width:90%;"}
{% endtab %}

{% tab Segments 및 필터 %}
이전에 생성한 하나 이상의 Segments에 속하면서 추가 필터에도 해당하는 사용자를 타겟팅할 수도 있습니다. 먼저 Segments를 선택한 후 **추가 필터** 섹션에서 오디언스를 더 세분화할 수 있습니다. 다음 스크린샷은 "일일 활성 사용자" Segment, "이메일을 열어본 적 없음" Segment에 속하면서 30일 이전에 구매한 사용자를 타겟팅하는 예시입니다.

![두 개의 Segments를 포함하고 30일 이내에 마지막 구매가 이루어진 추가 필터가 있는 메시지의 타겟팅 옵션.]({% image_buster /assets/img_archive/target_segmenter.png %}){: style="max-width:90%;"}
{% endtab %}

{% tab 특정 앱 %}

Campaign 메시지 또는 캔버스 단계를 특정 앱에 전달할 수 있습니다. 예를 들어 인앱 메시지나 푸시 알림을 Android 또는 iOS 앱에만 보낼 수 있습니다.

그러나 한 사용자가 여러 앱을 사용할 수 있다는 점을 기억하세요. "앱 보유" 필터는 선택한 앱을 가진 모든 사용자를 식별하지만, 어떤 앱이 메시지를 수신하는지는 제어하지 않습니다. 예를 들어 "앱 보유"가 Android로 설정된 Segment 필터를 적용하면, iOS 앱도 가지고 있는 사용자는 iOS 앱에서도 메시지를 수신합니다.

!["Hello, World (Android)" 앱을 보유한 사용자를 위한 필터.]({% image_buster /assets/img_archive/has_app_hello_world.png %}){: style="max-width:60%;"}

Android 앱에만 인앱 메시지를 보내고 싶다고 가정해 보겠습니다.

1. Segment를 생성하고 **타겟팅할 앱 및 웹사이트**를 **특정 앱의 사용자**로 설정한 다음 Android 앱을 선택합니다.

![특정 앱 "Test_Android"의 사용자를 타겟팅하는 Segment.]({% image_buster /assets/img_archive/app_test_android.png %}){: style="max-width:60%;"}

{: start="2"}
2. **타겟 오디언스** 단계에서 **세그먼트별로 사용자 타겟팅** 섹션에 Segment가 추가되었는지 확인합니다.

![예시 Segment가 선택된 "타겟 오디언스" 단계.]({% image_buster /assets/img_archive/target_users_by_segment_example.png %})

{% alert note %}
Segment 멤버십 필터를 통해 **추가 필터** 섹션에 Segment를 추가하면 이 방법은 작동하지 않습니다. 해당 앱에만 메시지를 전달하려면 **세그먼트별로 사용자 타겟팅**에서 Segment를 직접 참조해야 합니다.
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert tip %}
이메일 Campaign의 경우 **시드 그룹** 섹션에서 시드 그룹을 타겟팅할 수 있습니다. 시드 그룹은 API Campaign에서는 사용할 수 없지만, Campaign에서 API 트리거 진입을 통해 시드 그룹을 포함할 수 있습니다. 자세한 내용은 [시드 그룹]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups)을 참조하세요.
{% endalert %}

### 2단계: 오디언스 테스트 {#step-2-test-your-audience}

오디언스에 Segments와 필터를 추가한 후 [사용자 조회]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)를 통해 오디언스가 예상대로 설정되었는지 테스트하여 오디언스 기준에 맞는지 확인할 수 있습니다.

!["사용자 조회" 버튼이 있는 "사용자 조회" 섹션.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%"}

#### 오디언스 요약 {#audience-summary}

**오디언스 요약**은 타겟 오디언스에 누가 포함되어 있는지에 대한 개요를 보여줍니다. 여기에서 최대 사용자 수 상한을 설정하거나 [사용량 제한]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) 전달 속도를 설정하여 오디언스를 추가로 제한할 수 있습니다.

![최대 사용자 수 상한 또는 사용량 제한 전달 속도를 설정하는 옵션이 있는 "오디언스 요약" 섹션.]({% image_buster /assets/img_archive/audience_summary.png %})

#### A/B 테스트 {#ab-testing}

**A/B 테스트** 섹션에서는 동일한 마케팅 Campaign의 여러 버전에 대한 사용자 반응을 비교하는 테스트를 설정할 수 있습니다. 이러한 버전은 유사한 마케팅 목표를 공유하지만 문구와 스타일이 다릅니다. 목표는 마케팅 목표를 가장 잘 달성하는 Campaign 버전을 식별하는 것입니다.

자세한 내용과 모범 사례는 [다변량 및 A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing)를 참조하세요.

#### 오디언스 통계 {#audience-statistics}

Braze는 하단에 타겟팅된 채널의 상세한 오디언스 통계를 제공합니다. 사용자 기반이 클수록 **도달 가능 사용자** 수는 대략적인 추정치일 가능성이 높습니다. [글로벌 컨트롤 그룹]({{site.baseurl}}/user_guide/audience/global_control_group)을 사용하거나 메시지 자격 조건을 설정하면 도달 가능 사용자 수가 줄어들 수 있습니다.

- 도달 가능 사용자의 정확한 수를 확인하려면 [정확한 통계 계산]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#calculating-exact-statistics)을 선택하세요. 이 기능은 사용자 기반의 모든 사용자를 검색합니다.
- 사용자 기반 중 타겟팅되는 비율이나 이 Segment의 LTV(LTV)를 확인하려면 **추가 통계 보기**를 선택하세요.

##### 타겟 오디언스 수와 도달 가능 사용자 수가 다를 수 있는 이유 {#why-the-target-audience-count-could-differ-from-the-reachable-users-count}

{% multi_lang_include audience/segments.md section='Differing audience size' %}

![각 타겟팅된 채널의 도달 가능 사용자에 대한 추정 수가 포함된 "전체 모집단" 섹션.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

{% alert note %}
정확한 통계를 계산하는 데 몇 분이 걸릴 수 있습니다. 이 기능은 Segment 수준에서만 정확한 통계를 계산하며, 필터 또는 필터 그룹 수준에서는 계산하지 않습니다.<br><br>
대규모 Segments의 경우 정확한 통계를 계산하더라도 약간의 변동이 있는 것은 정상입니다. 이 기능의 정확도는 99.999% 이상으로 예상됩니다.
{% endalert %}

## 타겟 오디언스와 진입 기준의 상호 작용 {#how-target-audience-and-entry-criteria-work-together}

Braze에서 Campaign 또는 Canvas를 구축할 때 타겟팅은 두 부분으로 이루어집니다:

1. **타겟 오디언스:** 누가 자격이 있는지
2. **진입 기준:** 무엇이 전달을 트리거하는지

순서가 중요합니다. Braze는 진입 기준을 평가하기 전에 해당 사용자가 타겟 오디언스에 속하는지 먼저 확인합니다. 사용자가 해당 시점에 오디언스 자격을 갖추지 못하면, 나중에 진입 이벤트를 트리거하더라도 Campaign 또는 Canvas에 진입하지 않습니다. 타겟 오디언스를 대기실이라고 생각하세요. 트리거가 발생할 때 이미 안에 있는 사용자만 앞으로 진행할 수 있습니다.

### 예시 1 {#example-1}

사용자의 첫 번째 세션 중에 푸시 메시지를 보내고 싶습니다.

다음과 같이 설정합니다:

- **타겟 오디언스:** 세션 수 = 0인 사용자
- **진입 이벤트:** 세션 시작

사용자가 앱을 열면 Braze는 세션 수가 이제 1이 된 것을 확인하고, 해당 사용자는 더 이상 오디언스 자격을 갖추지 못합니다. 진입 이벤트는 자격이 있는 시점 이후에 발생하므로 메시지가 발송되지 않습니다.

이를 작동시키려면 세션이 시작되기 전에 사용자가 오디언스 자격을 갖추어야 합니다(타겟 오디언스와 진입 트리거를 뒤바꾸세요).

### 예시 2 {#example-2}

지난 7일 동안 $10 이상을 지출한 사용자에게 이메일을 보내고 싶습니다.

다음과 같이 설정합니다:

- **타겟 오디언스:** 지난 7일 동안 $10 이상을 지출한 사용자
- **진입 이벤트:** 모든 구매

이제 사용자가 오늘 $12를 지출했다고 가정해 보겠습니다. 이것은 메시지를 트리거하지 않습니다. 오디언스에 진입할 자격만 부여할 뿐입니다. 나중에 다른 구매를 하지 않으면 이메일을 수신하지 않습니다.

더 나은 접근 방식은 더 넓은 오디언스를 사용하고 필터를 진입 기준으로 이동하는 것입니다:

- **오디언스:** 모든 사용자(또는 기본 오디언스)
- **진입 이벤트:** 구매하기
- **진입 필터:** 지난 7일 총 지출 > $10

이렇게 하면 자격을 갖춘 구매가 필터를 충족하고 메시지를 트리거합니다. 두 번째 동작이 필요하지 않습니다.

## 모범 사례 {#best-practices}

- 진입 기준이 발생하기 전에 오디언스 Segment에 사용자가 포함되어 있는지 확인하세요.
- 이벤트 이후에만 적용되는 오디언스 필터를 사용하지 마세요. 필터가 트리거 시점에 발생하는 것에 의존하는 경우(예: "세션 수 = 0"), Braze가 확인할 때 사용자가 더 이상 자격을 갖추지 못할 수 있습니다.
- 시간 기반 로직을 신중하게 사용하세요. 예를 들어 신규 사용자를 타겟팅하려면:
    - 타겟 오디언스를 "지난 7일 이내에 처음 앱을 사용한 사용자"로 설정합니다.
    - 진입 이벤트를 "세션 시작"으로 설정합니다.
    - 이렇게 하면 첫 주 이내에 있는 사용자만 자격을 갖추고 세션을 시작할 때 진입합니다.