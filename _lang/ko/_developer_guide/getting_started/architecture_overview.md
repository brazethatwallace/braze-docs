---
nav_title: 아키텍처 개요
article_title: 아키텍처 개요
page_order: 3
description: "이 문서에서는 Braze 기술 스택의 다양한 부분과 구성요소를 설명하며, 관련 문서에 대한 링크를 포함합니다."
platform:
  - iOS
  - Android
  - Web
  - React Native
  - Flutter
  - Cordova
  - Roku
  - Swift
  - Unity
---

# 시작하기: 아키텍처 개요 {#getting-started-architectural-overview}

> 이 문서에서는 Braze 기술 스택의 다양한 부분과 구성요소를 설명하며, 관련 문서에 대한 링크를 포함합니다.

Braze는 기본적으로 데이터를 다룹니다. Braze 플랫폼은 SDK, REST API 및 파트너 통합을 통해 데이터를 집계하고 활용할 수 있도록 지원합니다.

![Braze에는 다양한 레이어가 있습니다. 전체적으로 SDK, API, 대시보드, 파트너 통합으로 구성되어 있습니다. 각각 데이터 수집 레이어, 분류 레이어, 오케스트레이션 레이어, 개인화 레이어 및 작업 레이어의 일부에 기여합니다. 작업 레이어에는 푸시, 인앱 메시지, 연결된 카탈로그, 웹훅, SMS, 이메일 등 다양한 채널이 있습니다.]({% image_buster /assets/img/getting-started/braze_listen_understand_act.png %}){: style="display:block;margin:auto;" }

* [데이터 수집](#ingestion): Braze는 다양한 소스에서 데이터를 가져옵니다.
* [분류](#classification): 마케팅 팀은 이러한 측정기준을 사용하여 사용자 기반을 동적으로 세분화합니다.
* [오케스트레이션](#orchestration): Braze는 이상적인 시간에 다양한 오디언스 세그먼트에 메시지를 지능적으로 조정합니다.
* [작업](#action): 마케팅 팀은 데이터를 기반으로 SMS 및 이메일과 같은 다양한 메시징 채널을 통해 콘텐츠를 생성합니다.
* [개인화](#personalization): 데이터는 오디언스에 대한 개인화된 정보로 실시간 변환됩니다.
* [내보내기](#exporting-data): 그런 다음, Braze는 이 메시징에 대한 사용자의 참여를 추적하고 이를 플랫폼에 다시 공급하여 루프를 생성합니다. 실시간 보고서 및 분석을 통해 이 데이터에 대한 인사이트를 얻을 수 있습니다.

이 모든 기능이 함께 작동하여 사용자 기반과 브랜드 사이에서 성공적인 상호 작용을 만들어 목표를 달성할 수 있습니다. Braze는 수직 통합 스택이라는 맥락에서 이 모든 작업을 수행합니다. 각 레이어를 하나씩 살펴보겠습니다.

## 데이터 수집 {#ingestion}

Braze는 Snowflake, Kafka, MongoDB 및 Redis를 활용한 스트리밍 데이터 아키텍처를 기반으로 구축되었습니다. 여러 소스의 데이터는 SDK와 API를 통해 Braze에 로드할 수 있습니다. 플랫폼은 데이터가 중첩되거나 구조화되는 방식에 관계없이 실시간으로 모든 데이터를 처리할 수 있습니다. Braze의 데이터는 고객 프로필에 저장됩니다.

{% alert tip %}
Braze는 사용자가 익명 상태일 때부터 앱에 로그인하여 알려진 상태가 될 때까지의 전체 여정에서 데이터를 추적할 수 있습니다. 각 사용자에 대해 Braze에서 `external_id`라고 하는 사용자 ID를 설정해야 합니다. 이 ID는 사용자가 앱을 열 때 변경되지 않고 접근할 수 있어야 하며, 이를 통해 기기와 플랫폼 전반에서 사용자를 추적할 수 있습니다. 모범 사례에 대해서는 [사용자 수명 주기 문서]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)를 참조하세요.
{% endalert %}

![Braze는 API에서 백엔드 데이터 소스를, SDK에서 프론트엔드 데이터 소스를, Braze 클라우드 데이터 수집에서 데이터 웨어하우스 데이터를, 파트너 통합에서 데이터를 가져옵니다. 이 데이터는 Braze API를 통해 내보내집니다.]({% image_buster /assets/img/getting-started/import-export.png %}){: style="display:block;margin:auto;" }

{% alert note %}
이 사람 중심의 고객 프로필 데이터베이스는 실시간 대화형 속도를 지원합니다. Braze는 데이터가 도착하면 값을 미리 계산하고 빠른 검색을 위해 경량 문서 형식으로 결과를 저장합니다. 플랫폼이 처음부터 이러한 방식으로 설계되었기 때문에 대부분의 메시징 사용 사례에 적합합니다. 특히 연결된 콘텐츠, 제품 카탈로그 및 중첩된 속성과 같은 다른 데이터 개념과 결합할 때 더욱 그렇습니다.
{% endalert %}

### 데이터 소스 분석 {#data-source-breakdown}

Braze는 다양한 기능을 위해 서로 다른 데이터 저장 시스템을 사용합니다. 어떤 기능이 어떤 데이터 소스를 사용하는지 이해하는 것은 데이터 관리 및 문제 해결에 중요합니다.

#### MongoDB 기반 기능 {#mongodb-powered-features}
- 커스텀 이벤트(SDK와 API로 추적됨)
- 커스텀 속성
- 고객 프로필
- 구매 이벤트
- 대부분의 세분화 및 타겟팅 기능

#### Snowflake 기반 기능 {#snowflake-powered-features}
- [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)
- [예측 스위트]({{site.baseurl}}/user_guide/brazeai)
- [개인화된 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/personalized_paths) 및 [개인화된 배리언트]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations#personalized-variant)
- [AI 개인화된 아이템 추천]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai)
- [추정 실제 열람률]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#estimated-real-open-rate)(커스텀 이벤트를 사용하지 않음)

{% alert important %}
**데이터 제거 고려사항:** 커스텀 이벤트는 MongoDB에 저장되며 Snowflake 데이터와는 별개입니다. 잘못된 커스텀 이벤트 데이터를 제거해야 하는 경우 MongoDB에서 처리해야 합니다. Snowflake 기반 기능(예: SQL 세그먼트 확장 및 기타 Snowflake 기반 기능)은 Snowflake의 데이터를 사용하며, 이는 별도로 처리됩니다. 한 시스템에서 데이터를 제거한다고 해서 다른 시스템에서 자동으로 제거되는 것은 아닙니다.
{% endalert %}

### Braze API를 통한 백엔드 데이터 소스 {#backend-data-sources-through-the-braze-api}
Braze는 [REST API]({{site.baseurl}}/api/endpoints/user_data)를 통해 사용자 데이터베이스, 오프라인 트랜잭션, 데이터 웨어하우스에서 데이터를 가져올 수 있습니다.

### Braze SDK를 통한 프론트엔드 데이터 소스 {#frontend-data-sources-through-braze-sdk}
Braze는 [Braze SDK]({{site.baseurl}}/user_guide/get_started/sdk_overview)를 통해 사용자의 기기와 같은 프론트엔드 데이터 소스에서 퍼스트파티 데이터를 자동으로 캡처합니다. SDK는 새로운(익명) 사용자를 처리하고 수명 주기 동안 고객 프로필의 데이터를 관리합니다.

### 파트너 통합 {#partner-integrations}
Braze에는 "Alloys"라고 부르는 150개 이상의 기술 파트너가 있습니다. [상호 운용 가능한 기술 및 데이터 API]({{site.baseurl}}/partners/home)로 구성된 강력한 네트워크를 통해 데이터 피드를 보완할 수 있습니다.

### Braze 클라우드 데이터 수집을 통한 직접 웨어하우스 연결 {#direct-warehouse-connection-through-braze-cloud-data-ingestion}
[Braze 클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)을 통해 단 몇 분 만에 데이터 웨어하우스에서 플랫폼으로 고객 데이터를 스트리밍하여 관련 사용자 속성, 이벤트 및 구매를 동기화할 수 있습니다. 클라우드 데이터 수집 통합은 중첩된 JSON 및 오브젝트 배열을 포함하는 복잡한 데이터 구조를 지원합니다.

클라우드 데이터 수집은 Snowflake, Amazon Redshift, Databricks 및 Google BigQuery에서 데이터를 동기화할 수 있습니다.

## 분류 {#classification}
분류 레이어를 통해 팀은 Braze를 통과하는 데이터를 기반으로 [세그먼트]({{site.baseurl}}/user_guide/audience/segments)라고 하는 오디언스를 동적으로 분류하고 구축할 수 있습니다.

{% alert note %}
분류, 오케스트레이션, 개인화 레이어는 마케팅 팀이 많은 작업을 수행하는 곳입니다. 주로 웹 인터페이스인 Braze 대시보드를 통해 이러한 레이어와 상호 작용합니다. 개발자는 이러한 레이어를 설정하고 커스터마이징하는 역할을 합니다.
{% endalert %}

이름, 이메일, 생년월일, 국가 등과 같은 일반적인 유형의 사용자 속성은 기본적으로 SDK에 의해 자동으로 추적됩니다. 개발자는 팀과 협력하여 사용 사례에 맞게 추적할 추가적인 커스텀 데이터를 정의합니다. 커스텀 데이터는 사용자 기반이 분류되고 세분화되는 방식에 영향을 미칩니다. 구현 과정에서 이 데이터 모델을 설정하게 됩니다.

[자동 수집 데이터 및 커스텀 데이터]({{site.baseurl}}/developer_guide/analytics)에 대해 자세히 알아보세요.

## 오케스트레이션 {#orchestration}
오케스트레이션 레이어를 통해 마케팅 팀은 사용자 데이터 및 이전 참여를 기반으로 사용자 여정을 설계할 수 있습니다. 이 작업은 대부분 대시보드 인터페이스를 통해 이루어지지만, [API를 통해 Campaign을 시작]({{site.baseurl}}/api/api_campaigns#api-campaigns)할 수 있는 옵션도 있습니다. 예를 들어, 대시보드에서 마케터가 설계한 메시지와 Campaign을 보내는 시점을 백엔드에서 Braze에 알리고, 백엔드 로직에 따라 트리거할 수 있습니다. API 트리거 메시지의 예로는 비밀번호 재설정 또는 배송 확인이 있습니다.

{% alert note %}
API 트리거 Campaign은 고급 트랜잭션 사용 사례에 적합합니다. 이를 통해 마케터가 Campaign 카피, 다변량 테스트 및 재적격성 규칙을 Braze 대시보드 내에서 관리하면서 서버 및 시스템에서 해당 콘텐츠의 전달을 트리거할 수 있습니다. 메시지를 트리거하는 API 요청에는 실시간으로 메시지에 템플릿화할 추가 데이터를 포함할 수도 있습니다.
{% endalert %}


### 피처 플래그 {#feature-flags}
Braze에서는 [피처 플래그]({{site.baseurl}}/developer_guide/feature_flags)를 통해 일부 사용자에 대한 기능을 원격으로 활성화 또는 비활성화할 수 있습니다. 이를 통해 마케터는 전체 오디언스에 아직 롤아웃하지 않은 기능에 대한 메시징을 사용자 기반의 올바른 세그먼트에 타겟팅할 수 있습니다. 그뿐만 아니라 피처 플래그를 사용하면 추가 코드 배포나 앱 스토어 업데이트 없이 프로덕션에서 기능을 켜고 끌 수 있습니다. 이를 통해 새로운 기능을 안심하고 안전하게 롤아웃할 수 있습니다.

## 개인화 {#personalization}
개인화 레이어는 메시지에서 동적 콘텐츠를 제공하는 기능을 나타냅니다. 널리 사용되는 개인화 언어인 Liquid를 사용하여 팀은 기존 데이터를 동적으로 가져와 각 수신자에게 맞춤화된 메시지를 표시할 수 있습니다. 또한 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)를 사용하면 웹 서버에서 접근할 수 있는 모든 정보나 API를 통해 직접 푸시 알림이나 이메일 등 전송하는 메시지에 삽입할 수 있습니다. 연결된 콘텐츠는 Liquid를 기반으로 구축되며 친숙한 구문을 사용합니다.

이 동적 콘텐츠는 프로그래밍 가능하기 때문에 마케터는 계산된 값, 다른 호출의 응답 또는 제품 카탈로그 항목을 포함할 수 있습니다. 구현 중에 이러한 시스템을 설정한 후에는 마케팅 팀이 기술 팀의 지원 없이 또는 거의 지원 없이도 이를 수행할 수 있습니다.

## 작업 {#action}
작업 레이어에서는 사용자에 대한 실제 메시징을 수행합니다. 작업 레이어의 목적은 이전에 논의된 모든 레이어를 통해 사용할 수 있는 데이터를 기반으로 적절한 시간에 적절한 사용자에게 적절한 메시지를 보내는 것입니다. 메시징은 앱 또는 사이트 내부(예: 인앱 메시지 전송 또는 Content Cards 캐러셀 및 배너와 같은 그래픽 요소를 통해) 또는 앱 경험 외부(예: 푸시 알림 또는 이메일 전송)에서 이루어집니다.

### 메시징 채널 {#messaging-channels}
Braze는 채널에 구애받지 않는 사용자 중심의 데이터 모델을 통해 진화하는 기술 환경을 처리하도록 설계되었습니다. 대시보드는 메시지 전달 및 트랜잭션 트리거를 관리합니다. 예를 들어, 마케터는 사용자가 특정 위치 근처에 설정된 지오펜스에 들어갈 때 새로 개장한 매장의 쿠폰을 제공하는 SMS 메시지를 트리거하거나, 사용자가 좋아하는 프로그램의 새 시즌이 나왔음을 알리는 이메일을 보낼 수 있습니다.

[Braze SDK]({{site.baseurl}}/user_guide/get_started/sdk_overview)는 푸시, 인앱 메시지, Content Cards 등 추가적인 메시징 채널을 지원합니다. 마케팅 팀이 Braze 대시보드를 사용하여 지원되는 모든 메시징 채널에서 Campaign을 조정할 수 있도록 SDK를 앱 또는 사이트에 통합합니다.

![SDK를 통해 사용할 수 있는 Braze 메시징 채널 다이어그램]({% image_buster /assets/img/getting_started/channels.png %})

## 데이터 내보내기 {#exporting-data}
중요한 점은 Braze와의 모든 최종 사용자 상호 작용이 추적되어 참여와 도달 범위를 측정할 수 있다는 것입니다. Braze가 이러한 모든 소스에서 데이터를 집계한 후 다양한 도구를 사용하여 데이터를 기술 스택으로 다시 내보내 루프를 닫을 수 있습니다.

### Currents
[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)는 세분화된 스트리밍 내보내기를 제공하여 스택의 다른 대상에 지속적으로 공급하는 Braze 선택적 애드온입니다. Currents는 사용자별 이벤트당 원시 데이터 피드로, 5분마다 또는 15,000개의 이벤트마다(둘 중 먼저 도래하는 시점) 데이터를 내보냅니다. Currents의 다운스트림 대상 예로는 Segment, S3, Redshift, Mixpanel 등이 있습니다.

### Snowflake 데이터 공유 {#snowflake-data-sharing}
Snowflake의 [보안 데이터 공유]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake) 기능을 사용하면 일반적인 데이터 제공업체 관계에서 발생하는 워크플로 마찰, 장애 지점, 불필요한 비용에 대한 걱정 없이 Snowflake 포털의 데이터에 안전하게 접근할 수 있습니다. 모든 공유는 Snowflake의 고유한 서비스 레이어 및 메타데이터 저장소를 통해 수행됩니다. 실제로 데이터는 계정 간에 복사되거나 전송되지 않습니다. 이것은 중요한 개념입니다. 공유된 데이터는 소비자 계정에 저장 공간을 차지하지 않으므로 월간 데이터 스토리지 요금에 기여하지 않기 때문입니다. 소비자에게 부과되는 유일한 요금은 공유 데이터를 쿼리하는 데 사용되는 컴퓨팅 리소스(즉, 가상 웨어하우스)에 대한 요금입니다.

### Braze 내보내기 API {#braze-export-apis}
Braze API는 집계 분석을 프로그래밍 방식으로 내보내고 개별 사용자 데이터를 내보낼 수 있는 [엔드포인트]({{site.baseurl}}/api/endpoints/export)를 제공합니다. 모든 규모의 오디언스 및 세그먼트에 대해 이 데이터를 내보낼 수 있습니다.

### CSV {#csvs}
마지막으로, 대시보드에서 집계 수준 데이터를 [CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data)로 직접 다운로드할 수 있는 옵션이 있습니다. CSV 옵션을 사용하면 팀원이 Braze에서 데이터를 쉽게 내보낼 수 있습니다.

{% alert tip %}
CSV 내보내기에는 기본적으로 500,000개의 행 제한이 있지만, API에는 이와 관련된 제한이 없습니다.
{% endalert %}

## 종합 정리 {#putting-it-all-together}

사용자 중 한 명인 Mel이 방금 제품 발표 소식을 받았다고 가정해 보겠습니다. 그 이면에서는 Braze 플랫폼의 모든 레이어가 함께 작동하여 이 과정이 원활하게 진행되도록 했습니다.

Mel의 정보는 CSV 가져오기를 통해 기존 고객 참여 플랫폼에서 Braze로 가져왔습니다. 통합 후 Mel이 앱과 상호 작용할 때마다 더 많은 데이터가 고객 프로필에 추가되었습니다.

제품 발표는 앱에서 유사한 항목에 좋아요를 표시한 모든 고객에게 전송되었습니다. 이 데이터를 커스텀 이벤트로 정의했습니다. SDK가 이 이벤트를 추적하고 사용자 기반을 적절히 세분화했습니다. Braze는 이 발표를 보낼 최적의 시간을 조정하고, Mel의 선호하는 이름을 사용하여 발표를 개인화했습니다.

Mel이 발표를 열면 새 제품을 위시리스트에 추가합니다. Braze는 Mel이 이메일을 클릭한 것을 자동으로 추적합니다. SDK는 Mel이 새 제품을 위시리스트에 추가했음을 추적합니다. 사용자가 브랜드와 상호 작용할 때마다 여러분과 사용자는 서로에 대해 더 많이 알아가게 됩니다.

![Braze가 메시징 채널 전반에서 사용자 행동을 추적하는 방법을 보여주는 다이어그램]({% image_buster /assets/img/getting-started/putting-it-all-together.png %})