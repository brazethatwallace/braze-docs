---
nav_title: Infillion
article_title: Infillion
alias: /partners/infillion/
description: "이 참조 문서에서는 위치 데이터를 활용하여 마케팅 관련성을 높일 수 있는 Braze와 Infillion 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# Infillion

> [Infillion](https://infillion.com/)은 위치 데이터를 활용하여 마케팅 관련성을 높일 수 있도록 지원합니다. 지오펜싱 소프트웨어 및 비콘과 결합된 위치 SDK는 관련성 높은 개인화된 근접 인식 모바일 경험을 제공합니다.

비콘 또는 지오펜스 지원을 Braze 타겟팅 및 메시징 기능과 결합하여 사용자의 물리적 행동에 대해 더 많이 알아보고 그에 맞게 메시지를 보낼 수 있습니다. 이 파트너십 통합을 통해 다양한 사용 사례가 열립니다:

- **마케팅:** 상황에 맞는 메시지를 전송하고 경험적인 소비자 여정을 구축하세요.
- **경쟁사 분석:** 경쟁 위치 주변에 트리거를 설정하여 소비자 트렌드와 패턴을 파악합니다.
- **오디언스 인사이트:** 사용자의 방문 행동을 파악하고 이러한 학습을 기반으로 추가로 세분화합니다.

{% alert note %}
이 통합은 Infillion 비콘과 Infillion 지오펜스 솔루션 모두에서 동일하게 작동합니다.
{% endalert %}

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| [Infillion 매니저 계정](https://manager.gimbal.com/login/users/sign_in) | 이 파트너십을 활용하려면 Infillion 매니저 계정이 필요합니다. |
| [Infillion Location SDK](https://docs.gimbal.com/index.html) | Infillion Location SDK는 근접 비콘과 지오펜스를 사용하여 매크로 및 마이크로 위치 기반 모바일 경험을 제공하며, 앱 사용자와 더 효과적으로 소통할 수 있도록 합니다. SDK를 구현하고 지오펜스(또는 비콘)를 설정해야 합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **Settings** > **API Keys**에서 생성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## SDK 통합 {#sdk-integration}

Braze와 Infillion을 통합하려면 Infillion Location SDK를 구현하고 Infillion 매니저 계정을 생성해야 합니다. Android, FireOS 및 iOS용 다음 통합은 사용자가 새로 들어오는 각 장소에 대해 고유한 커스텀 이벤트를 생성하며, 이러한 이벤트는 Campaigns 및 Canvases에서 트리거 및 리타겟팅에 사용할 수 있습니다.

50개 이상의 장소를 생성할 예정이라면 일반 `Places Entered` 커스텀 이벤트를 만들고 장소 이름을 이벤트 속성정보로 추가하는 것이 좋습니다.

1. [Infillion 설명서](https://docs.gimbal.com/)의 지침에 따라 Android 및 iOS용 [Infillion SDK](https://manager.gimbal.com/sdk_downloads)를 앱에 통합합니다.
2. Infillion의 [place REST API](https://docs.gimbal.com/rest.html)를 사용하여 사용자 `places`를 가져옵니다.
3. Braze [REST API 키](https://manager.gimbal.com/apps)를 입력하여 Infillion 계정을 Braze에 연결합니다.
4. Braze SDK에서 [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/)를 설정합니다. [Android 및 FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#gimbal-beacons)와 [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/#gimbal-beacons)에서 Infillion과 Braze를 통합할 수 있습니다.
5. 이러한 이벤트에 대한 속성정보(장소 이름, 체류 시간)를 기록합니다.
6. 이러한 속성정보와 이벤트를 사용하여 Braze에서 Campaigns 및 Canvases를 트리거할 수 있습니다.