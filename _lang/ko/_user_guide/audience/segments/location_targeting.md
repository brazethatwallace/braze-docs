---
nav_title: 위치 타겟팅
article_title: 위치 타겟팅
page_order: 7
page_type: tutorial
tool:
- Segments
- Location
description: "이 사용법 문서에서는 위치 타겟팅을 설정하여 위치별로 사용자를 세분화하는 방법을 안내합니다."

---

# 위치 타겟팅 {#location-targeting}

> 이 문서에서는 위치 타겟팅을 설정하여 가장 최근 위치를 기준으로 사용자를 세분화하는 방법을 안내합니다. 위치 기반 Campaign(캠페인) 및 전략을 검토하고 있다면 이 기능이 적합합니다.

## 1단계: Segment 생성하기 {#step-1-create-your-segment}

**오디언스** 아래의 **Segments** 페이지로 이동하여 현재 사용자 Segment를 모두 확인합니다. 이 페이지에서 새 Segment를 생성하고 이름을 지정할 수 있습니다. 시작하려면 **세그먼트 생성**을 선택하고 Segment에 이름을 지정합니다.

![Segment를 생성하는 모달.]({% image_buster /assets/img_archive/createsegment2.png %}){: style="max-width:70%;"}

## 2단계: 위치 맞춤 설정하기 {#step-2-customize-your-location}

Segment를 생성한 후 **가장 최근 위치** 필터를 추가하여 사용자가 마지막으로 앱을 사용한 장소를 기준으로 타겟팅합니다. 표준 원형 영역 또는 커스텀 다각형 영역의 범위 안이나 밖에 있는 사용자를 강조 표시할 수 있습니다.

![원형 범위 내 가장 최근 위치에 대한 필터.]({% image_buster /assets/img_archive/filter_recent_location.png %})

{% tabs %}
{% tab 원형 %}

### 원형 영역 {#circular-regions}

원형 영역의 경우 원점을 이동하고 세분화를 위한 위치 반경을 조정할 수 있습니다.

![뉴저지와 뉴욕 사이 도시들의 원형 윤곽선.]({% image_buster /assets/img_archive/location_circle.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab 다각형 %}

### 다각형 영역 {#polygonal-regions}

다각형 영역의 경우 Segment에 포함할 영역을 더 구체적으로 지정할 수 있습니다.

![선택된 다각형 영역으로서의 뉴욕주 윤곽선.]({% image_buster /assets/img_archive/create_polygon.png %}){: style="max-width:70%;"}

{% endtab %}
{% endtabs %}

## 비콘 및 지오펜스에 대한 파트너 지원 {#partnership-support-for-beacon-and-geofence}

기존 비콘 또는 지오펜스 지원을 타겟팅 및 메시징 기능과 결합하면 사용자의 물리적 행동에 대한 더 많은 정보를 얻을 수 있으므로 그에 맞게 메시지를 보낼 수 있습니다. 다음 파트너를 통해 위치 추적을 활용할 수 있습니다:

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion/)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)