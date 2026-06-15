---
nav_title: 병합 동작
article_title: 사용자 병합 동작
page_order: 1
page_type: reference
description: "Braze가 삭제 예정 사용자, 테스트 사용자, 전역 제어 그룹 사용자에 대해 사용자 병합을 처리하는 방법을 알아보세요."
---

# 사용자 병합 동작 {#user-merge-behavior}

> Braze가 사용자 병합을 처리하는 방법을 알아보세요. 기본 동작이 적용되지 않는 세 가지 사용자 유형(삭제 예정 사용자, 테스트 사용자, 전역 제어 그룹 사용자)에 대해서도 설명합니다.

이 동작은 [개별 병합]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/#individual-merging), [일괄 병합]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/#bulk-merging), [사용자 병합 API 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) 등 모든 병합에 적용됩니다.

## 일반 병합 동작 {#general-merge-behavior}

두 개의 고객 프로필을 병합하면, Braze는 유지할 프로필의 비어 있는 필드를 병합할 프로필의 값으로 채웁니다. 두 프로필 모두 해당 필드에 값이 있는 경우, Braze는 유지할 프로필의 값을 보존합니다.

예를 들어, 값이 하나의 프로필에만 존재하는 경우 Braze는 해당 값을 유지합니다:

| 필드 | 병합할 프로필 | 유지할 프로필 | 결과 프로필 |
|---|---|---|---|
| `first_name` | Alex | (비어 있음) | Alex |
| `last_name` | (비어 있음) | Sterling | Sterling |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

두 프로필 모두 동일한 필드에 값이 있는 경우, Braze는 유지할 프로필의 값을 유지합니다:

| 필드 | 병합할 프로필 | 유지할 프로필 | 결과 프로필 |
|---|---|---|---|
| `first_name` | Alex | Al | Al |
| `last_name` | (비어 있음) | Sterling | Sterling |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

이 동작은 기본 속성과 커스텀 속성에 잘 적용됩니다. 그러나 Braze는 다음 사용자 유형에 대해서는 다르게 처리합니다.

## 동작 요약 {#behavior-summary}

| 사용자 유형 | 동작 | 이유 |
|---|---|---|
| 삭제 예정 사용자 | 병합하지 않음 | 삭제 예정으로 표시된 프로필은 7일 이내에 삭제되므로 데이터를 보존할 필요가 없습니다. |
| 테스트 사용자 | 병합하며, 테스트 사용자 상태 유지 | 테스트 사용자 상태를 유지하면 병합 후에도 사용 가능한 테스트 모집단을 유지할 수 있습니다. |
| 전역 제어 그룹 사용자 | 병합하지 않음 | 병합하면 무작위 버킷 번호가 변경되어 실험 및 보고에 영향을 줄 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 삭제 예정 사용자 {#users-marked-for-deletion}

[일괄 사용자 삭제 도구]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users/)를 사용하여 Segment를 삭제하면, Braze는 해당 고객 프로필을 향후 7일 이내에 삭제 예정으로 표시합니다. Braze는 삭제 예정으로 표시된 프로필은 유지할 프로필이든 병합할 프로필이든 병합하지 않습니다.

삭제 예정으로 표시된 프로필을 병합해야 하는 경우, 먼저 [Segment 삭제를 취소]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users/#cancel)하거나 해당 사용자를 삭제 대상에서 제거하여 프로필의 표시를 해제하세요.

## 테스트 사용자 {#test-users}

Braze는 테스트 사용자 프로필의 병합을 허용하며, 결과 프로필에서 테스트 사용자 상태를 보존합니다. 이는 유지할 프로필의 값을 유지하는 [일반 병합 동작](#general-merge-behavior)과 다릅니다.

다음 표는 각 조합에 대한 결과 테스트 사용자 상태를 보여줍니다:

| 병합할 프로필 | 유지할 프로필 | 결과 프로필 |
|---|---|---|
| 테스트 사용자 아님 | 테스트 사용자 아님 | 테스트 사용자 아님 |
| 테스트 사용자 | 테스트 사용자 | 테스트 사용자 |
| 테스트 사용자 | 테스트 사용자 아님 | 테스트 사용자 |
| 테스트 사용자 아님 | 테스트 사용자 | 테스트 사용자 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

테스트 사용자에 대한 자세한 내용은 [내부 그룹]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/)을 참조하세요.

## 전역 제어 그룹 사용자 {#global-control-group-users}

Braze는 [전역 제어 그룹]({{site.baseurl}}/user_guide/audience/global_control_group/)에 속한 고객 프로필은 유지할 프로필이든 병합할 프로필이든 병합하지 않습니다.

전역 제어 그룹 멤버십은 사용자의 [무작위 버킷 번호]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/)에 의해 결정됩니다. 병합하면 그룹에 속하는 사용자가 변경되어 실험 및 보고에 영향을 줄 수 있습니다.

## 관련 문서 {#related-articles}

- [중복 사용자 병합]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/)
- [POST: 사용자 병합]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)
- [사용자 삭제]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users/)
- [전역 제어 그룹]({{site.baseurl}}/user_guide/audience/global_control_group/)
- [무작위 버킷 번호]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/)
- [내부 그룹]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/)