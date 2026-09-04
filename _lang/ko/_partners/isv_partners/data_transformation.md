---
nav_title: 데이터 변환
hidden: true
---

# Braze 데이터 변환 {#braze-data-transformation}

> Braze [데이터 변환]({{site.baseurl}}/user_guide/data/unification/data_transformation)은 파트너 플랫폼에서 웹훅을 수집하고, 고객이 해당 웹훅의 페이로드를 Braze 고객 프로필의 속성, 이벤트, 구매 등 원하는 사용자 데이터로 변환하는 매핑을 정의할 수 있도록 해줍니다.

## 데이터 변환 기반 통합의 모습 {#what-a-data-transformation-based-integration-would-look-like}

데이터 변환 기능을 기반으로 한 파트너 통합은 공개 설명서를 통해 고객에게 공유되는 변환 코드 템플릿 형태가 될 수 있습니다.

상호 고객의 경우, 다음과 같은 절차로 진행됩니다:

1. 파트너 플랫폼에 로그인하여 웹훅을 설정합니다.
2. Braze 팀과 협력하여 Braze 데이터 변환에 대한 액세스를 확보하고 Braze 대시보드에서 새 변환을 만듭니다.
3. 변환에서 생성된 URL을 복사합니다.
4. Braze로 돌아가서 복사한 변환 URL로 테스트 웹훅을 전송합니다.
5. Braze에서 변환 코드 템플릿을 복사하여 붙여넣습니다.
6. 변환을 활성화합니다.
7. 활성화되면 Braze 사용자 검색 도구를 통해 웹훅에 따라 고객 프로필이 업데이트되었는지 확인하고, 필요에 따라 변환 코드를 편집할 수 있습니다.

{% alert tip %}
변환 코드 예시를 구축할 때는 Braze에 전송하는 웹훅 유형별로 변환을 만드는 것을 권장합니다.
{% endalert %}