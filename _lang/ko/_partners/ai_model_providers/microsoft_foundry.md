---
nav_title: Microsoft Foundry
article_title: Microsoft Foundry
description: "이 참조 문서에서는 Braze와 Microsoft Foundry 간의 파트너십에 대해 설명합니다. 이 통합을 통해 Foundry에서 관리하는 AI 모델을 Braze에 연결하여 커스텀 AI 에이전트에 사용할 수 있습니다."
alias: /partners/microsoft_foundry/
page_type: partner
search_tag: Partner

---

# Microsoft Foundry

> [Microsoft Foundry](https://azure.microsoft.com/en-us/products/ai-foundry)는 엔터프라이즈 AI 운영, 모델 빌더 및 애플리케이션 개발을 위한 통합 Azure 서비스형 플랫폼(PaaS)입니다.

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Microsoft Foundry integration' %}

## 통합 소개 {#about-the-integration}

Braze와 Microsoft Foundry 통합을 사용하면 커스텀 AI 에이전트를 구축할 때 Microsoft Foundry에서 관리하는 생성형 AI 모델을 사용할 수 있습니다. 이 통합은 현재 gpt-5.4-mini와 gpt-5.4-nano 두 가지 모델을 지원합니다. 이 통합을 통해 에이전트는 개인화된 문구를 생성하거나, 실시간 의사결정을 내리거나, Foundry에서 관리하는 모델을 사용하여 카탈로그 필드를 업데이트할 수 있습니다.

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| 활성 구독이 있는 Azure 계정 | 도움이 필요하면 관리자에게 문의하거나 [Azure 계정 옵션](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account)을 참조하세요. |
| Microsoft Foundry 인스턴스 | 프로젝트를 생성하기 위한 Microsoft Foundry 인스턴스입니다. |
| Microsoft Foundry 프로젝트 | 배포된 모델을 보관할 Foundry 인스턴스 내의 프로젝트입니다. |
| 배포된 모델 | Foundry 프로젝트 내에 배포된 지원 모델이 하나 이상 필요합니다. |
| Braze 인스턴스 | Braze 인스턴스는 [API 개요 페이지]({{site.baseurl}}/api/basics#endpoints)에서 확인하거나 Braze 온보딩 매니저에게 문의하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## Foundry에서 지원 모델 배포하기 {#deploy-supported-models-in-foundry}

Braze와 Microsoft Foundry 통합은 gpt-5.4-mini와 gpt-5.4-nano 두 가지 모델을 지원합니다. 두 모델 모두 통합하려는 Foundry 인스턴스 내의 Foundry 프로젝트에 배포해야 합니다.

Foundry 프로젝트를 생성하고 모델을 배포하려면 [Microsoft Foundry 설명서](https://learn.microsoft.com/en-us/azure/foundry/tutorials/quickstart-create-foundry-resources?tabs=portal)를 참조하세요.

1. Azure 포털을 통해 Microsoft Foundry에 로그인합니다.
2. Microsoft Foundry에서 Braze와 통합할 모델을 보관할 프로젝트를 생성합니다.
3. gpt-5.4-mini, gpt-5.4-nano 또는 둘 다 사용할지 결정합니다.
4. 사용하려는 각 모델에 대해 Microsoft Foundry 설명서를 참조하여 배포합니다. 기본 배포 이름을 변경하지 마세요. 변경하면 해당 모델의 통합이 중단될 수 있습니다.

## 통합 {#integration}

Foundry 인스턴스를 Braze에 연결하려면 다음을 수행합니다.

1. Braze 대시보드에서 **파트너 통합** > **기술 파트너**로 이동하여 **Microsoft Foundry**를 찾습니다.
2. **Microsoft Foundry API 키**를 입력합니다.
3. **Microsoft Foundry 인스턴스 이름**을 입력합니다. 이는 `.services.ai.azure.com` 앞의 하위 도메인입니다.
4. **저장**을 선택합니다.

저장하면 Braze에 연결 상태와 연결 날짜 및 시간이 표시됩니다. 에이전트 콘솔에서 [커스텀 에이전트를 생성]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)할 때 Foundry 모델을 선택할 수 있습니다.

{% alert important %}
gpt-5.4-mini 또는 gpt-5.4-nano를 사용하려면 기본 배포 이름을 변경하지 않고 Foundry 프로젝트에 각 모델을 배포해야 합니다.
{% endalert %}

통합이 정상적으로 작동하는지 확인하려면 에이전트 콘솔로 이동하여 배포된 모델 중 하나를 사용하여 테스트 에이전트를 생성합니다. "농담 하나 해줘"와 같은 간단한 지시를 입력하고 테스트 호출을 실행하여 모델이 예상대로 응답하는지 확인합니다.

통합을 제거하려면 **Microsoft Foundry 통합** 페이지에서 **연결 해제**를 선택합니다.

통합과 관련된 문제나 질문이 있으면 [Azure 고객지원](https://azure.microsoft.com/en-us/support/options/)에 문의하세요.