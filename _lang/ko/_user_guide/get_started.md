---
nav_title: 시작하기
article_title: "시작하기&#58; Braze 개요"
page_order: 1
page_type: reference
description: "Braze에서 작업할 때 알아야 할 핵심 개념에 대해 알아보세요."
---

# 시작하기: Braze 개요 {#get-started-braze-overview}

> Braze에 오신 것을 환영합니다! 이 문서 모음은 플랫폼을 시작하는 데 도움이 되며 Braze의 주요 용어, 기능 및 특징을 소개합니다. 이 페이지에서는 Braze에서 작업할 때 알아야 할 핵심 개념을 소개합니다.

{% alert tip %}
이 문서와 함께 무료 [실무자 학습 경로](https://learning.braze.com/page/practitioner) 강좌를 확인해 보시기를 적극 추천합니다. 이 강좌에는 특별한 로그인이나 계정이 필요하지 않습니다. Braze의 기술적인 개요를 찾고 있는 개발자라면 <a href="/docs/developer_guide/getting_started/platform_overview">개발자를 위한 시작하기</a> 도 확인해 보세요.
{% endalert %}

시작하기 섹션에서는 Braze의 일반적인 구현에 중점을 두고 설명합니다. 하지만 Braze는 매우 유연하며 다양한 방식으로 조직에 가치를 제공하도록 커스텀할 수 있습니다. 명확성과 간결성을 위해 엄격한 지침을 제공하는 대신 기본값 설정에 대한 설명적인 개요를 제공했습니다. 모든 조직이 각기 다른 요구사항을 가지고 있다는 것을 알고 있으며, Braze는 특정 요구사항에 맞는 다양한 커스텀 옵션을 제공할 수 있도록 설계되었습니다.

Braze의 강력한 기능을 함께 살펴보겠습니다.

## Braze 작동 방식 {#how-braze-works}

Braze는 다양한 채널을 통해 개인화되고 타겟팅된 Campaigns를 만들 수 있도록 모든 규모의 브랜드를 지원하는 고객 인게이지먼트 플랫폼입니다. Braze를 사용하면 고객의 목소리에 귀를 기울이고, 고객의 행동이 무엇을 의미하는지 이해한 다음, 적절한 채널을 통해 적절한 시점에 적절한 메시지를 전송하여 행동할 수 있습니다.

{% alert tip %}
[동료를 Braze에 추가]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users)하여 함께 플랫폼을 탐색해 보세요.
{% endalert %}

## 사용자 및 Segments {#users-and-segments}

사용자는 여러분의 고객으로, Braze를 사용하여 보내는 메시지를 받는 사람들입니다. 사용자에 대해 수집하고 Braze에 수집한 모든 데이터는 인구 통계, 개인 정보, 선호도, 행동 등 고객 프로필에 저장됩니다. 이 정보는 메시징을 지원하며, 적절한 사용자에게 맞춤 메시지를 전달할 수 있도록 해줍니다.

![사용자 및 Segments와 관련된 스크린샷.]({% image_buster /assets/img/getting_started/user_profile.png %})

Segments는 고객 기반을 더 작은 그룹으로 나누어 특정 메시징으로 타겟팅할 수 있도록 합니다. 성별, 위치, 연령과 같은 특성부터 이전 Campaigns와의 상호작용 패턴이나 고객 여정에서의 위치와 같은 행동까지 다양한 변수를 사용하여 Segments를 생성할 수 있습니다.

Segments는 동적입니다. 사용자는 자신의 행동과 브랜드와의 관계에 따라 실시간으로 Segments에 들어가거나 나올 수 있습니다. 이를 통해 고객이 언제든지 가장 관련성 높은 메시지를 받을 수 있습니다. 타겟팅 및 메시징 목적에 필요한 만큼 많은 Segments를 생성할 수 있습니다.

![Segments는 동적입니다. 사용자는 자신의 행동과 브랜드와의 관계에 따라 실시간으로 Segments에 들어가거나 나올 수 있습니다. 이를 통해 고객이 언제든지 가장 관련성 높은 메시지를 받을 수 있습니다. 타겟팅 및 메시징 목적에 필요한 만큼 많은 Segments를 생성할 수 있습니다.]({% image_buster /assets/img/getting_started/segment.png %})

자세한 내용은 [시작하기: 사용자 및 Segments]({{site.baseurl}}/user_guide/get_started/users_and_segments)를 확인하세요.

## Campaigns 및 Canvases {#campaigns-and-canvases}

Campaigns와 Canvases는 사용자에게 메시지를 보내는 방법입니다.

Campaigns는 다양한 채널을 통해 특정 오디언스 Segment에 단일 메시지를 보내는 데 가장 적합합니다. Campaign에서 지원되는 모든 메시징 채널(이메일, 푸시, 인앱 메시지, SMS 등)을 활용할 수 있습니다.

Canvases는 여러 채널에 걸쳐 개인화된 고객 여정을 자동화하고 오케스트레이션할 수 있는 고급 Campaign 워크플로입니다. Canvas 내에서 분기 로직, 지연, 의사 결정 포인트, 전환 이벤트를 설정하여 일련의 상호 작용을 통해 고객을 안내할 수 있습니다. Canvases는 다양한 터치포인트에서 일관되고 원활한 커뮤니케이션을 보장하여 고객 참여와 전환 가능성을 높여 줍니다.

자세한 내용은 [시작하기: Campaigns 및 Canvases]({{site.baseurl}}/user_guide/get_started/campaigns_and_canvases)를 확인하세요.

## 워크스페이스 {#workspaces}

워크스페이스는 사용자, Segments, Campaigns, Canvases 등의 데이터를 하나의 위치에 그룹화합니다. 워크스페이스 간에는 정보가 공유되지 않으므로, 워크스페이스에 웹사이트와 앱을 추가할 때 이 점을 유의하세요. 모범 사례로, 동일하거나 매우 유사한 앱의 다른 버전만 하나의 워크스페이스에 함께 넣는 것을 권장합니다.

워크스페이스의 활용 사례:

- 서로 다른 제품 라인 또는 앱
- 서로 다른 오디언스(예: 배달 기사와 고객)
- 별도의 사업부
- 테스트 환경

자세한 내용은 [시작하기: 워크스페이스]({{site.baseurl}}/user_guide/get_started/workspaces)를 참조하세요.

## Braze 통합하기 {#integrating-braze}

Braze는 빠르고 쉽게 시작할 수 있도록 설계되었습니다. 수백 개 브랜드로 구성된 고객 기반에서 평균 가치 실현 시간은 6주입니다.

![Braze 통합과 관련된 스크린샷.]({% image_buster /assets/img/getting_started/timetovalue.png %})

다음은 병렬로 진행할 수 있는 네 가지 구성 요소를 기반으로 통합 기간을 예상하는 Braze 프레임워크입니다. 일반적인 범위는 30일에서 180일이며, 대부분의 계정은 45일에서 60일 이내에 통합을 완료합니다.

- **Campaign 마이그레이션 복잡도 수준:** Campaign을 마이그레이션하는 데 걸리는 시간은 보유한 Campaign 수, 개인화 정도, 그리고 사용 가능한 리소스에 따라 달라집니다. 마이그레이션할 Campaign이 10개 미만이면 60일 이내에 완료할 수 있습니다. 하지만 100개 이상의 Campaign이 있다면 더 복잡해집니다. 한 사람이 100개의 Campaign을 마이그레이션하는 것과 10명이 100개를 마이그레이션하는 것은 다릅니다.

{% alert tip %}
마이그레이션에 도움이 필요하신가요? [인증된 Braze 파트너](https://www.braze.com/partners/solutions-partners)가 도와드릴 수 있습니다!
{% endalert %}

- **이메일 발송량:** 이메일을 발송하려면 IP를 워밍업해야 합니다. [IP 워밍]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming)은 새로 할당된 IP 주소로 발송자 평판을 구축하는 과정입니다. 하루에 200~300만 통 미만의 이메일을 발송하는 경우, IP 워밍은 30일 이내에 완료됩니다. 피크 발송량도 고려하세요. 평소 하루에 200만 통의 이메일을 발송하지만 시즌 기간에 700만 통을 발송할 계획이라면, 해당 "피크" 발송량에 맞춰 워밍업해야 합니다. 대량 발송자는 여러 IP를 사용하여 워밍업 과정을 단축할 수 있습니다.
- **조직 복잡도:** 온보딩 과정은 비즈니스 요구에 맞게 조정할 수 있습니다. 단일 사업부, 센터 오브 엑설런스, 여러 독립 사업부, 또는 에이전시를 활용하여 팀을 보강하는 경우 등 Braze는 모든 시나리오에서의 경험을 보유하고 있습니다.
- **데이터 인프라 정교성:** Braze SDK만 구현하거나 이미 고객 데이터 플랫폼(고객 데이터 플랫폼)을 사용하고 있다면 30일 만에 모든 설정을 완료할 수 있습니다. 최신 고객 데이터 플랫폼를 사용하면 과정을 더 빠르게 진행할 수 있습니다. 하지만 Braze와 연결해야 할 백엔드 시스템, 도구 또는 데이터베이스가 많은 경우 시간이 더 오래 걸리고 설정을 완료하기 위해 더 많은 전담 리소스가 필요할 수 있습니다.

자세한 내용은 다음을 참조하세요: [시작하기: 통합 개요]({{site.baseurl}}/user_guide/get_started/integrations).