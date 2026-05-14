---
nav_title: 위치 및 지오펜스
article_title: 위치 및 지오펜스
page_order: 4
layout: dev_guide
guide_top_header: "위치 및 지오펜스"
guide_top_text: "모바일 기술의 보편성과 유연성 덕분에 마케터, 제품 매니저, 성장 팀은 어디서든 사용자에게 도달할 수 있으며, 디지털과 현실 세계 경험의 경계를 허물고 있습니다. 이 섹션의 문서를 참조하여 위치 추적, 지오펜스 생성 등에 대해 자세히 알아보세요."
page_type: landing
tool: Location
description: "이 랜딩 페이지에는 위치 및 지오펜스에 관한 문서가 포함되어 있습니다. 여기에서 위치 추적, 지오펜스 생성 등에 대한 리소스를 찾을 수 있습니다."
search_rank: 10
guide_featured_title: "섹션 문서"
guide_featured_list:
  - name: 위치 추적
    link: /docs/user_guide/audience/locations_and_geofences/location_tracking
    image: /assets/img/braze_icons/marker-pin-01.svg
  - name: 지오펜스 생성
    link: /docs/user_guide/audience/locations_and_geofences/creating_geofences
    image: /assets/img/braze_icons/marker-pin-01.svg
---

## 위치 및 지오펜스 소개 {#about-locations-and-geofences}

Braze를 사용하면 실제 세계에서의 사용자 위치를 기반으로 사용자와의 관계를 구축하고 강화할 수 있으며, 깊이 연결된 강력한 인터랙션 세트를 활용할 수 있습니다:

- 브랜드의 모든 오프라인 매장 위치를 업로드하고, 충성 사용자가 근처를 지나갈 때 매장 내 프로모션을 알리는 푸시 알림을 보낼 수 있습니다.
- 다가오는 콘서트 위치를 업로드하고, 사용자가 행사장에 도착했을 때 등록 장소를 안내하는 메시지를 보낼 수 있습니다. 그런 다음 사용자가 떠난 후 한 시간 뒤에 감사 메시지를 보내 후속 조치를 취할 수 있습니다.

사용자 위치 데이터를 수집하고 활용하는 방법은 몇 가지가 있습니다:

- 사용자가 앱을 열면 위치 추적이 GPS 위치 데이터를 사용하여 가장 최근 위치를 캡처합니다. 이를 통해 사용자가 어디에 있었는지 확인하고 이 데이터를 기반으로 세그먼트를 생성할 수 있습니다.
- 지오펜스는 정의된 가상 지리적 영역입니다. 사용자가 백그라운드 위치 추적을 활성화한 경우, 지오펜스를 사용하여 사용자가 지오펜스 내에 있을 때 실시간으로 Campaign을 트리거할 수 있습니다.