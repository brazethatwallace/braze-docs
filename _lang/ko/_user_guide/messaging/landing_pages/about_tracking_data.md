---
nav_title: 추적 데이터 정보
article_title: 랜딩 페이지 추적 데이터 정보
description: "Braze 랜딩 페이지의 추적 및 익명화된 데이터에 대해 알아보세요."
page_order: 10
alias: /landing_pages/data_tracking/
---

# 랜딩 페이지 추적 데이터 정보 {#about-landing-page-tracking-data}

> Braze 랜딩 페이지의 추적 및 익명화된 데이터에 대해 알아보세요.

## 추적 방법 {#tracking-methods}

### 웹 SDK {#web-sdk}

Braze 웹 SDK는 사용자가 랜딩 페이지에서 양식을 제출할 때 초기화됩니다. 양식 제출 전에는 개인 데이터가 수집되지 않으며, SDK는 사용자를 능동적으로 추적하지 않습니다. 초기화가 완료된 후에도 SDK는 브라우저에 어떠한 데이터도 저장하지 않습니다(쿠키, 로컬 스토리지 등).

Braze 웹 SDK는 사용자가 Braze 메시지의 {% raw %}`{% landing_page_url %}`{% endraw %} Liquid 태그로 생성된 링크를 통해 랜딩 페이지로 이동하면 즉시 초기화됩니다.

양식이 제출되면 SDK는 다음 데이터를 수집합니다:

- 양식 제출 이벤트(이벤트 이름 및 제출 시간)
- 팀이 양식에 지정한 데이터(이름, 이메일, 전화번호 등)
- 세션 시작 시간
- 기기 ID(기기에 대해 생성되지만 저장되지 않는 고유 ID)
- IP 주소로 결정된 국가

### 익명화된 데이터 {#anonymized-data}

사용자가 양식을 제출하기 전에 랜딩 페이지에서 추적되는 데이터는 익명화된 비식별 정보로만 구성됩니다. 이는 랜딩 페이지가 수신하는 페이지 조회수(노출 횟수) 및 클릭 수와 같은 표준 웹사이트 집계 측정기준으로 구성됩니다.

이 데이터는 식별 가능한 사용자에게 연결되지 않으므로, 개별 사용자 행동을 리타겟하거나 추적하는 데 사용할 수 없습니다.

## 중복 고객 프로필 병합 {#merging-duplicate-user-profiles}

Braze는 랜딩 페이지 양식이 제출될 때 이메일이나 전화번호와 같은 속성을 기반으로 사용자를 자동으로 병합하지 않습니다. 기존 고객 프로필과 일치하는 이메일 또는 전화번호로 양식이 제출되면, Braze는 별도의 고객 프로필을 생성합니다.

중복 고객 프로필을 병합하려면 다음을 수행할 수 있습니다:

- 랜딩 페이지 양식이 제출될 때 [`/users/merge` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)를 트리거하여 새 프로필을 기존 프로필과 병합합니다.
- [일괄 병합]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/#bulk-merging)을 스케줄하여 일치하는 식별자를 기반으로 중복 프로필을 주기적으로 병합합니다.