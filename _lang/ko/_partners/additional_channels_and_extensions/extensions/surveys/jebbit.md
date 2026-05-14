---
nav_title: Jebbit
article_title: Jebbit
description: "이 참조 문서에서는 Braze와 Jebbit의 파트너십에 대해 설명합니다. Jebbit은 Jebbit Campaign에서 사용자 이메일과 속성을 Braze에 실시간으로 사용자 데이터로 전달할 수 있는 PaaS입니다."
alias: /partners/jebbit/
page_type: partner
search_tag: Partner

---

# Jebbit

> [Jebbit](https://www.jebbit.com/)은 사용자를 위한 매력적인 경험을 구축하여 퍼스트파티 데이터를 수집할 수 있는 PaaS입니다.

_이 통합은 Jebbit에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Jebbit 통합을 사용하면 Jebbit Campaign에서 사용자 이메일과 속성을 Braze에 실시간으로 사용자 데이터로 전달할 수 있습니다. 이 데이터는 개인화된 이메일 Campaign 및 트리거와 같은 마케팅 이니셔티브를 추진하는 데 사용할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Jebbit 계정 | 이 파트너십을 활용하려면 Jebbit 계정이 필요합니다. |
| Braze REST API 키 | 모든 사용자 데이터 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL. 엔드포인트는 [인스턴스]({{site.baseurl}}/api/basics/#endpoints)의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

Jebbit과의 통합을 요청할 때 반드시 지켜야 할 마감 기한이 있는지 알려주세요. 또한 Braze에 전달하려는 속성이 Jebbit 경험에 매핑되어 있는지 확인하세요.

### 1단계: API 자격 증명 제공 {#step-1-provide-api-credentials}

Dropbox 파일 요청을 통해 텍스트 파일로 API 자격 증명을 Jebbit에 제공하세요.
다음 [Dropbox URL](https://www.dropbox.com/request/RqKQHkJHXw1cFBKbXpZx)을 사용하여 파일을 제출하세요.

### 2단계: 테스트 제출 확인 {#step-2-confirm-test-submission}

통합에 배정된 Jebbit 엔지니어가 Jebbit에서 Braze로 테스트 제출을 진행하여 Braze 환경에서 데이터가 어떻게 표시되는지 확인할 수 있도록 합니다. 이것이 통합을 활성화하는 마지막 단계입니다. Jebbit 데이터가 설정되었으므로 이를 활용하여 마케팅 이니셔티브를 추진하세요.

{% alert note %}
Jebbit에서 설정한 속성 ID가 Braze에서 속성 필드 이름으로 표시됩니다.
{% endalert %}

## 커스터마이제이션 {#customization}

현재 [사용자 데이터]({{site.baseurl}}/api/endpoints/user_data/) 엔드포인트를 특히 지원하고 있으며, 다른 엔드포인트에 대한 요청도 지원할 수 있습니다.

속성 필드 이름도 원하는 대로 커스터마이즈할 수 있습니다.

Braze에서 Jebbit의 추가 속성을 원하는 경우 Jebbit 계정에서 새 속성을 매핑하세요. 해당 속성에 대한 데이터를 수집하면 속성이 Braze에 자동으로 표시됩니다.