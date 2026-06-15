---
nav_title: Storyly
article_title: Storyly
description: "이 참조 문서에서는 앱 소유자가 세그먼트를 타겟팅하고 Braze에 더 많은 퍼스트파티 데이터를 제공할 수 있게 해주는 경량 SDK인 Braze와 Storyly 간의 파트너십에 대해 설명합니다."
alias: /partners/storyly/
page_type: partner
search_tag: Partner

---

# Storyly

> [Storyly](https://www.storyly.io/)는 앱이나 웹사이트에 스토리를 제공하는 경량 SDK입니다. 직관적인 디자인 스튜디오, 통찰력 있는 분석, 원활한 연결성을 갖춘 Storyly는 오디언스 경험을 풍부하게 만드는 강력한 도구입니다.

*이 통합은 Storyly에서 유지 관리합니다.*

## 통합 정보 {#about-the-integration}

Braze와 Storyly 통합을 사용하면 Braze의 Segments를 Storyly 플랫폼에서 오디언스로 활용할 수 있습니다. 이 통합을 통해 다음을 수행할 수 있습니다.
- 특정 스토리로 세그먼트를 타겟팅
- 사용자 속성을 사용하여 스토리 콘텐츠를 개인화

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Storyly 계정 | 이 파트너십을 활용하려면 Storyly 계정이 필요합니다. |
| Storyly SDK | [Storyly SDK](https://integration.storyly.io/)를 설치해야 합니다. |
| Braze REST API 키 | 다음 권한이 있는 Braze REST API 키 <br><br> `users.export.ids`<br> `users.export.segments`<br> `segments.list`<br> `segments.details` <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 활용 사례 {#use-cases}

Braze와 Storyly 통합을 통해 앱 소유자는 Braze의 모든 세그먼트에 스토리를 표시하고 사용자 속성으로 스토리를 개인화할 수 있습니다.

일반적인 사용 사례는 다음과 같습니다.

__Storyly에서 Braze Segments 타겟팅__<br>통합이 완료되면 Braze Segments를 기반으로 Storyly 오디언스를 생성할 수 있습니다. 인구통계 또는 행동 기반 세그먼트가 될 수 있습니다. 예를 들어, 특정 위치에 거주하는 사용자, 앱에서 특정 동작을 수행하는 사용자, 또는 특정 제품에 관심이 있는 사용자를 특정 스토리로 타겟팅하여 전환을 높일 수 있습니다.<br>
__사용자 속성을 활용한 개인화된 스토리__<br>Braze 사용자 속성은 Storyly에서 동적 스토리를 생성하는 데에도 사용할 수 있습니다. 사용자의 이름, 장바구니에 담긴 제품, 또는 즐겨찾기한 제품을 포함하여 사용자에게 고유한 개인화된 스토리를 제공할 수 있습니다. 개인화는 스토리의 전환율과 전체 스토리 참여율을 높이는 데 도움이 됩니다.

## 데이터 내보내기 통합 {#data-export-integration}

Braze Storyly 통합은 다음 동영상에서 설명합니다.

{% multi_lang_include video.html id="3-OEqQs48Zw" source="youtube" %}

Storyly 통합에 커스텀 매개변수가 포함되어 있는지 확인하세요. 이 매개변수는 Braze `external id` 사용자 속성과 매칭됩니다. 커스텀 매개변수 구현은 [iOS](https://integration.storyly.io/ios/personalization-customaudience.html), [Android](https://integration.storyly.io/android/personalization-customaudience.html), [React Native](https://integration.storyly.io/react-native/personalization-customaudience.html), [Flutter](https://integration.storyly.io/flutter/personalization-customaudience.html), [Web](https://integration.storyly.io/web/personalization-customaudience.html)에서 확인할 수 있습니다.

자세한 내용은 [Storyly](https://docs.storyly.io/page/connect-your-braze-audiences-with-storyly) 설명서를 참조하세요.

### 1단계: Storyly 대시보드에서 통합 설정 {#step-1-set-the-integration-on-storyly-dashboard}

**Storyly Dashboard > Settings > Integrations > Connect with Braze**에서 통합을 생성할 수 있습니다. 여기에서 Braze REST API 키와 Braze REST 엔드포인트가 필요합니다.

### 2단계: 세그먼트 가져오기 {#step-2-get-your-segments}

다음으로, Braze Segments를 사용하여 Storyly 오디언스를 생성할 수 있습니다. **Storyly Dashboard > Settings > Audiences > New Audience > Create Audience with Braze**에서 생성할 수 있습니다.

여기에서 두 가지 동기화 옵션이 제공됩니다. 특정 Campaign 스토리에는 **One-time sync**를, 장기 스토리에는 **Daily Sync**를 선택하세요.