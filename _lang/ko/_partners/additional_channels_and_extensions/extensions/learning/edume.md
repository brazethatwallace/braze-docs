---
nav_title: eduMe
article_title: eduMe
description: "이 참조 문서에서는 Braze와 eduMe 간의 파트너십에 대해 설명합니다. eduMe는 모바일 기반 교육 도구로, Braze 연결된 콘텐츠를 활용하여 Braze Campaigns에서 사용자에게 eduMe 과정 및 레슨에 대한 액세스를 제공할 수 있습니다."
alias: /partners/edume/
page_type: partner
search_tag: Partner

---

# eduMe

> [eduMe](https://edume.com)는 모바일 기반 교육 도구로, 직원들이 필요한 시점에 어디서든 성공에 필요한 지식을 제공합니다.

_이 통합은 eduMe에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 eduMe 통합은 Braze [연결된 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content)를 활용하여 Braze Campaigns에서 사용자에게 eduMe 과정 및 레슨에 대한 액세스를 제공합니다. 개인 및 그룹 진행 상황은 eduMe 보고 기능을 통해 추적할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| eduMe 계정 | 이 파트너십을 활용하려면 eduMe 계정이 필요합니다. |
| eduMe API 키 | eduMe 고객 성공 담당자에게 API 키를 요청해야 합니다. 이 키는 Braze 연결된 콘텐츠 호출에서 사용됩니다. |
| eduMe 링크 서명 시크릿 | eduMe 고객 성공 담당자에게 조직의 링크 서명 시크릿 설정을 요청해야 합니다. 이 시크릿은 연결된 콘텐츠에서 원활한 링크를 활성화하는 데 사용됩니다. 이 시크릿으로 별도의 작업을 수행할 필요는 없습니다. |
| eduMe 그룹 및 콘텐츠 ID | 이러한 식별자는 연결된 콘텐츠 호출을 설정하는 데 필요합니다. 이러한 식별자를 얻는 데 도움이 필요하면 eduMe 고객 서비스 담당자에게 문의하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 {#integration}

### 연결된 콘텐츠 호출 생성 {#create-your-connected-content-call}

사용자에게 과정, 레슨 또는 eNPS 설문조사에 대한 액세스를 제공하고 eduMe에서 내부 사용자 ID에 대한 진행 상황을 추적하려면 이 예시에 표시된 API 호출을 따르세요.

{% raw %}
```
Welcome to my Rickshaw App platform.
Access your onboarding course at:

{% connected_content
  https://connect.edume.com/
  EDUME-CONTENT-LINK-AND-CONTENT-ID&groupId=5681&externalUserId={{${driver_id}}}
  :headers {
       "x-api-key": "YOUR-EDUME-API-KEY"
  }
%}
```
{% endraw %}

1. `YOUR-EDUME-API-KEY`를 eduMe API 키로 교체합니다.<br><br>
2. `EDUME-CONTENT-LINK-AND-CONTENT-ID`를 해당 콘텐츠 링크 문자열 및 모듈, 레슨 또는 설문조사 식별자로 교체합니다. 이러한 식별자는 eduMe 계정에서 찾을 수 있습니다.
  - 과정: `getCourseLink?moduleId=12087`
  - 레슨: `getLessonLink?lessonId=25805`
  - eNPS 설문조사: `getSurveyLink?surveyId=654`<br><br>
3. 이 링크를 통해 eduMe에 도착한 사용자는 선택한 eduMe 팀 또는 그룹에 추가됩니다. `groupId`를 관련 팀 ID 또는 eduMe 그룹 ID로 교체합니다. 등록이 필요한 과정을 제외하고는 일반적으로 팀 ID를 사용하며, 등록이 필요한 과정의 경우 그룹 ID를 사용해야 합니다.<br><br>
4. `externalUserId` 필드에 매핑할 적절한 필드를 포함합니다. 예시 연결된 콘텐츠 호출에서는 `driver_id`를 사용하지만, 실제 필드는 다를 수 있습니다. 이 ID는 eduMe 보고서에서 확인할 수 있으므로 내부 시스템과 상호 연관시킬 수 있습니다.<br><br>
5. 마지막으로, 필요에 따라 메시지를 커스터마이즈하고 테스트합니다. 최소 하나의 테스트 메시지를 보내고, eduMe 콘텐츠에 액세스하고, 레슨 또는 과정을 완료한 후 eduMe 분석이 올바르게 기록되고 있는지 확인하는 것을 권장합니다.