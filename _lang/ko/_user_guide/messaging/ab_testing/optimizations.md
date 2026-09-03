---
nav_title: 최적화
article_title: A/B 테스트 최적화
page_order: 1
page_type: reference
description: "BrazeAI를 사용하여 다변량 및 A/B Campaign 테스트를 최적화하는 방법을 알아보세요."
---

# A/B 테스트 최적화 {#optimizing-ab-tests}

> **BrazeAI<sup>TM</sup>로 최적화**를 사용하여 여러 배리언트가 포함된 Campaign을 자동으로 최적화할 수 있습니다.

**타겟 오디언스** 단계에서 **A/B 테스트**로 이동한 다음, **BrazeAI<sup>TM</sup>로 최적화**를 켜세요.

1회 발송 Campaign의 경우, BrazeAI<sup>TM</sup>가 초기 테스트를 발송한 후 가장 성과가 좋은 배리언트를 나머지 오디언스에게 발송합니다. 반복 발송 Campaign의 경우, BrazeAI<sup>TM</sup>가 12시간마다 성과를 검토하고 더 성과가 좋은 배리언트로 더 많은 사용자를 이동시킵니다.

사전 요구사항, 구성 옵션 및 리포팅 세부 정보는 [BrazeAI를 사용한 A/B 테스트 최적화]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection)를 참조하세요.

{% alert note %}
개인화된 배리언트를 사용하는 기존 Campaigns는 해당 최적화 및 분석을 계속 지원합니다. 새 Campaign을 생성할 때는 개인화된 배리언트를 사용할 수 없습니다.
{% endalert %}

Braze는 1회 발송 최적화에서 두 번째 발송 전에 사용자 자격 요건을 다시 확인합니다. 초기 테스트에 자격이 없었던 사용자가 나머지 오디언스에 포함될 수 있으며, 더 이상 자격이 없는 사용자는 후속 발송을 수신하지 못합니다.

Campaign 결과에 대한 자세한 내용은 [A/B 테스트 분석]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics)을 참조하세요.