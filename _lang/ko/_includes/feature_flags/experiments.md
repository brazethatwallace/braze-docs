# 기능 플래그 실험 {#feature-flag-experiments}

> 기능 플래그 실험을 통해 애플리케이션의 변경 사항을 A/B 테스트하여 전환율을 최적화할 수 있습니다. 마케터는 기능 플래그를 사용하여 새로운 기능이 전환율에 긍정적인 영향을 미치는지 부정적인 영향을 미치는지, 또는 어떤 기능 플래그 속성 집합이 가장 적합한지 결정할 수 있습니다.

## 전제 조건 {#prerequisites}

실험에서 사용자 데이터를 추적하려면 먼저 앱에서 사용자가 기능 플래그와 상호 작용하는 시점을 기록해야 합니다. 이를 기능 플래그 노출이라고 합니다. 사용자가 대조군에 속해 있더라도 테스트 중인 기능을 보았거나 볼 수 있었을 때마다 기능 플래그 노출을 기록해야 합니다.

기능 플래그 노출 로깅에 대해 자세히 알아보려면 [기능 플래그 생성]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#impressions)을 참조하세요.

{% tabs %}
{% tab 웹 %}

```javascript
const featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag?.enabled) {
   return <NewFeature />
} else {
   return <ExistingFeature />
}
```

{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

```java
FeatureFlag featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag != null && featureFlag.getEnabled()) {
  return new NewFeature();
} else {
  return new ExistingFeature();
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("my-new-feature")
braze.logFeatureFlagImpression("my-new-feature")
if (featureFlag?.enabled == true) {
  return NewFeature()
} else {
  return ExistingFeature()
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 기능 플래그 실험 만들기 {#creating-a-feature-flag-experiment}

### 1단계: 실험 만들기 {#step-1-create-an-experiment}

1. **메시징** > **Campaigns**로 이동한 다음 **+ 캠페인 만들기**를 선택합니다.
2. **기능 플래그 실험**을 선택합니다.
3. 캠페인에 명확하고 의미 있는 이름을 지정하세요.

### 2단계: 실험 배리언트 추가 {#step-2-add-experiment-variants}

다음으로 배리언트를 만듭니다. 각 배리언트에 대해 켜거나 끄려는 기능 플래그를 선택한 다음 할당된 속성을 검토합니다.

기능의 영향을 테스트하려면 배리언트를 사용하여 트래픽을 두 개 이상의 그룹으로 분할하세요. 한 그룹의 이름을 "My control group"으로 지정하고 해당 그룹의 기능 플래그를 끕니다.

기능 플래그 실험은 최대 9개의 그룹을 지원합니다: 대조군 1개와 최대 8개의 배리언트.

### 3단계: 속성 덮어쓰기(선택 사항) {#step-3-overwrite-properties-optional}

특정 캠페인 배리언트를 수신하는 사용자에 대해 처음에 설정한 기본 속성을 덮어쓰도록 선택할 수 있습니다.

추가 기본 속성을 편집, 추가 또는 제거하려면 **메시징** > **기능 플래그**에서 기능 플래그 자체를 편집하세요. 배리언트가 비활성화되면 SDK는 지정된 기능 플래그에 대한 빈 속성 객체를 반환합니다.

![실험 배리언트 섹션에서 link 변수 키가 /sales로 덮어쓰기된 모습]({% image_buster /assets/img/feature_flags/feature_flag_experiment_override.png %}){: style="max-width:80%"}

### 4단계: 타겟팅할 사용자 선택 {#step-4-choose-users-to-target}

Segments 또는 필터 중 하나를 사용하여 [타겟 사용자]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users)를 선택합니다. 예를 들어, **수신된 기능 플래그 배리언트** 필터를 사용하여 이미 A/B 테스트를 수신한 사용자를 리타겟할 수 있습니다.

![필터 그룹 검색창에서 수신된 기능 플래그 배리언트가 강조 표시된 기능 플래그 실험의 대상 페이지]({% image_buster /assets/img/feature_flags/variant-filter-dropdown.png %}){: style="max-width:70%"}

{% alert note %}
Segment 멤버십은 특정 사용자에 대한 기능 플래그가 새로 고쳐질 때 계산됩니다. 앱에서 기능 플래그를 새로 고치거나 새 세션을 시작할 때 변경 사항이 적용됩니다.
{% endalert %}

### 5단계: 배리언트 배포 {#step-5-distribute-variants}

실험의 백분율 분포를 선택합니다. 모범 사례로, 실험을 시작한 후에는 배포를 변경하지 않는 것이 좋습니다.

### 6단계: 전환 할당 {#step-6-assign-conversions}

Braze를 사용하면 사용자가 캠페인을 수신한 후 특정 행동, [전환 이벤트]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events)를 얼마나 자주 수행하는지 추적할 수 있습니다. 사용자가 지정된 작업을 수행하면 전환으로 계산되는 기간을 최대 30일까지 지정할 수 있습니다.

### 7단계: 검토 및 시작 {#step-7-review-and-launch}

실험의 마지막 빌드를 완료한 후 세부 정보를 검토한 다음 **실험 시작**을 선택합니다.

## 결과 검토 {#reviewing-the-results}

기능 플래그 실험이 완료되면 실험에 대한 노출 데이터를 검토할 수 있습니다. **메시징** > **Campaigns**로 이동하여 기능 플래그 실험이 포함된 캠페인을 선택합니다.

### 캠페인 분석 {#campaign-analytics}

**캠페인 분석**은 다음과 같은 실험 성과에 대한 높은 수준의 개요를 제공합니다:

- 총 노출 횟수
- 고유 노출 횟수
- 주요 전환율
- 메시지에서 발생한 총 매출
- 예상 오디언스

또한 전달, 오디언스 및 전환에 대한 실험의 설정을 볼 수도 있습니다.

### 기능 플래그 실험 성능 {#feature-flag-experiment-performance}

**기능 플래그 실험 성능**은 다양한 차원에서 메시지가 얼마나 잘 수행되었는지를 보여줍니다. 표시되는 구체적인 측정기준은 선택한 메시징 채널과 다변량 테스트를 실행하는지 여부에 따라 달라집니다. 각 배리언트와 관련된 기능 플래그 값을 확인하려면 **미리 보기**를 선택합니다.