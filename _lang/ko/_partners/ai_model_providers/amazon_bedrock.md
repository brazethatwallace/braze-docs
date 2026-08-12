---
nav_title: Amazon Bedrock
article_title: Amazon Bedrock
description: "이 참조 문서에서는 Braze와 Amazon Bedrock 간의 파트너십에 대해 설명합니다. 이 통합을 통해 Bedrock 모델을 Braze에 연결하여 커스텀 AI 에이전트에서 사용할 수 있습니다."
alias: /partners/amazon_bedrock/
page_type: partner
search_tag: Partner

---

# Amazon Bedrock

> [Amazon Bedrock](https://aws.amazon.com/bedrock/)은 통합 API를 통해 주요 AI 기업의 파운데이션 모델에 대한 액세스를 제공하는 완전 관리형 AWS 서비스로, 브랜드가 AWS에서 생성형 AI 애플리케이션을 구축하고 확장할 수 있도록 합니다.

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Amazon Bedrock integration' %}

## 통합 소개 {#about-the-integration}

Braze와 Amazon Bedrock 통합을 사용하면 Amazon Bedrock 자격 증명을 Braze에 연결하여 커스텀 AI 에이전트를 구축할 때 Bedrock에서 호스팅하는 모델을 사용할 수 있습니다. 이 통합을 통해 에이전트는 Amazon Bedrock을 통해 사용 가능한 모델을 활용하여 개인화된 카피를 생성하고, 실시간 의사결정을 내리거나, 카탈로그 필드를 업데이트할 수 있습니다.

Amazon Bedrock을 연결하면 Braze에서 커스텀 에이전트용으로 큐레이트된 Bedrock 모델 세트를 표시합니다. Braze에서 사용 가능한 모델은 AWS 계정의 전체 카탈로그와 다를 수 있습니다.

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

## 전제 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Amazon Bedrock 액세스가 가능한 AWS 계정 | 모델이 호스팅되는 AWS 리전에서 Amazon Bedrock에 액세스할 수 있는 AWS 계정이 필요합니다. 도움이 필요하면 관리자 또는 [AWS Support](https://aws.amazon.com/support)에 문의하세요. |
| Amazon Bedrock 모델 액세스 | 사용하려는 Bedrock 모델에 대한 AWS 계정 내 액세스 권한이 필요합니다. Anthropic 모델과 같은 일부 모델은 AWS 계정에서 액세스 권한을 부여받아야 합니다. 모든 모델이 모든 AWS 리전에서 사용 가능한 것은 아닙니다. |
| 인증 자격 증명 | 장기 [Amazon Bedrock API 키](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html) 또는 워크스페이스에서 IAM 역할 인증이 활성화된 경우 Braze가 맡을 수 있는 IAM 역할이 필요합니다. |
| Braze 인스턴스 | Braze 인스턴스는 [API 개요 페이지]({{site.baseurl}}/api/basics#endpoints)에서 확인하거나 Braze 온보딩 매니저에게 문의하여 확인할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="전제 조건" }

## 통합 {#integration}

Amazon Bedrock을 Braze에 연결하려면 다음을 수행합니다.

1. Braze 대시보드에서 **파트너 통합** > **기술 파트너**로 이동한 다음 **Amazon Bedrock**을 검색하여 선택합니다.
2. **인증 방법**에서 **API 키** 또는 **AWS IAM 역할**(사용 가능한 경우)을 선택합니다.
3. 선택한 방법에 따라 설정을 완료합니다.
   - **API 키:** 장기 **Amazon Bedrock API 키**를 입력합니다. Bedrock 모델이 호스팅되는 **AWS 리전**을 선택합니다. **저장**을 선택합니다.
   - **AWS IAM 역할:** Braze에서 표시하는 값을 사용하여 IAM 역할 신뢰 정책을 구성한 다음 Braze에 역할 세부 정보를 입력합니다.
     1. **Braze AWS 계정 ID**를 복사하고 IAM 역할의 신뢰 정책에서 해당 계정을 신뢰합니다.
     2. **Braze 외부 ID**를 복사하고 `sts:ExternalId` 조건을 사용하여 역할의 신뢰 정책에서 이를 요구합니다. 새 값이 필요한 경우 **새 외부 ID 생성**을 선택합니다.
     3. Amazon Bedrock 권한이 있는 IAM 역할의 **AWS 역할 ARN**을 입력합니다. ARN은 `arn:aws:iam::<account-id>:role/<role-name>` 형식과 일치해야 합니다.
     4. Bedrock 모델이 호스팅되는 **AWS 리전**을 선택합니다.
     5. **저장**을 선택합니다.

{% alert note %}
**AWS IAM 역할**은 이 인증 옵션이 활성화된 워크스페이스에서만 표시됩니다. IAM 역할 인증을 사용하면 Braze가 사용자의 역할을 맡아 단기 Amazon Bedrock 자격 증명을 생성하며, 장기 API 키를 저장하지 않습니다.
{% endalert %}

저장하면 Braze에서 연결 날짜 및 시간과 함께 연결 상태를 표시합니다. Agent Console에서 [커스텀 에이전트를 생성]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)할 때 Amazon Bedrock 모델을 선택할 수 있습니다.

{% alert note %}
모든 Amazon Bedrock 모델이 모든 AWS 리전에서 사용 가능한 것은 아닙니다. 사용하려는 모델을 지원하는 리전을 선택하세요. 연결된 리전에서 사용할 수 없는 모델은 에이전트 호출 시 오류를 반환합니다.
{% endalert %}

통합이 정상적으로 작동하는지 확인하려면 Agent Console로 이동하여 Bedrock 모델 중 하나를 사용하여 테스트 에이전트를 생성합니다. "농담 하나 해줘"와 같은 지시를 입력하고 테스트 호출을 실행하여 모델이 예상대로 응답하는지 확인합니다.

통합을 제거하려면 **Amazon Bedrock 통합** 페이지에서 **연결 해제**를 선택합니다.

Amazon Bedrock 계정 또는 자격 증명에 문제가 있는 경우 [AWS Support](https://aws.amazon.com/support)에 문의하세요.