---
nav_title: "사용자 별칭 오브젝트"
article_title: API 사용자 별칭 오브젝트
page_order: 11
page_type: reference
description: "이 참조 문서에서는 사용자 별칭 오브젝트의 다양한 구성요소에 대해 설명합니다."

---

# 사용자 별칭 오브젝트 {#user-alias-object}

> 별칭은 대체 고유 사용자 식별자 역할을 합니다. 사용자 별칭 오브젝트를 사용하면 모바일 앱이나 웹사이트에 로그인하기 전과 후에 특정 사용자를 추적하는 분석에 일관된 식별자를 설정할 수 있습니다. 이 오브젝트를 사용하여 서드파티 공급업체가 사용하는 식별자를 회사 사용자에 추가하여 외부에서 데이터를 더 쉽게 조정할 수도 있습니다.

사용자 별칭 오브젝트는 식별자 자체를 나타내는 `alias_name`과 별칭 유형을 나타내는 `alias_label`, 두 부분으로 구성됩니다. 사용자는 레이블이 다른 여러 개의 별칭을 가질 수 있지만, `alias_label`당 `alias_name`은 하나만 사용할 수 있습니다.

이 오브젝트는 모든 엔드포인트에서 자주 사용되며, 다른 오브젝트 내에서도 자주 사용됩니다.

## 오브젝트 본문 {#object-body}

```json
{
  "user_alias" : {
    "alias_name" : (required, string),
    "alias_label" : (required, string)
  }
}
```

| 필드 | 데이터 유형 | 예시 | 설명 |
|---|---|---|---|
| `alias_name` | 문자열 | `john_doe_123` | 서드파티 시스템의 ID와 같은 사용자의 고유 식별자입니다. 이 값은 비어 있지 않아야 하며 236바이트 이하여야 합니다. |
| `alias_label` | 문자열 | `crm_id` | 별칭 유형을 정의하는 비어 있지 않은 커스텀 문자열입니다. 이 값은 특정 옵션에 제한되지 않습니다. `email_id`, `amplitude_id`, `salesforce_lead_id` 또는 사용 사례에 맞는 다른 값 등 의미 있는 레이블을 사용할 수 있습니다. 이 값은 236바이트 이하여야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Object body" }
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Object body" }

### 예시 {#example}

```json
{
  "user_alias": {
    "alias_name": "john_doe_123",
    "alias_label": "crm_id"
  },
  "external_id": "user_456"
}
```

이 예시에서 `crm_id`는 별칭이 고객 관계 관리 시스템 식별자를 나타냄을 표시하는 커스텀 레이블입니다.

### 추가 예시 {#additional-example}

```json
{
  "user_alias": {
    "alias_name": "a9f3c102",
    "alias_label": "amplitude_id"
  }
}
```

이 예시에서 `amplitude_id`는 가능한 레이블 값 중 하나입니다. `email_id`나 `salesforce_lead_id` 같은 레이블 또는 식별자 체계에 맞는 다른 커스텀 레이블을 사용할 수도 있습니다.